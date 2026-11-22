import json
from datetime import datetime, timedelta, timezone

import pytest

from monitor import checks, config, fetch, run

NOW = datetime(2026, 11, 22, 11, 0, tzinfo=timezone.utc)


def station(sid, minutes_ago=None, value=1.0, **extra):
    wl = None
    if minutes_ago is not None:
        wl = {"datetime": (NOW - timedelta(minutes=minutes_ago)).isoformat(), "value": value}
    return {"id": sid, "name": f"Station {sid}", "waterLevel": wl, "status": "BELOW WARNING LEVEL", **extra}


def page(stations):
    return f"<html><script>\nvar riverwatch_coordinates = {json.dumps(stations)};\n</script></html>"


def test_parse_keeps_only_whitelisted_fields():
    raw = station(1, 5, contact="Someone 98XXXXXXXX", meta_data={"SIM1": "secret"}, images=[{"id": 1}])
    parsed = fetch.parse_stations(page([raw]))
    assert set(parsed[0]) == set(fetch.KEEP_FIELDS)
    assert "secret" not in json.dumps(parsed) and "98XXXXXXXX" not in json.dumps(parsed)


def test_parse_fails_loudly_when_page_changes():
    with pytest.raises(fetch.SourceFormatError):
        fetch.parse_stations("<html>no data here</html>")


@pytest.mark.parametrize(
    "minutes_ago,expected",
    [(10, checks.OK), (config.LATE_AFTER_MIN + 1, checks.LATE), (config.SILENT_AFTER_MIN + 1, checks.SILENT), (None, checks.NO_DATA)],
)
def test_silence_states(minutes_ago, expected):
    state, _ = checks.silence(station(1, minutes_ago), NOW)
    assert state == expected


def test_rapid_rise_flags_only_above_threshold():
    t = NOW
    slow = [(t - timedelta(minutes=50), 1.0), (t, 1.0 + config.RISE_M / 2)]
    fast = [(t - timedelta(minutes=50), 1.0), (t, 1.0 + config.RISE_M + 0.1)]
    gap = [(t - timedelta(minutes=config.RISE_WINDOW_MIN + 30), 1.0), (t, 3.0)]
    assert checks.rapid_rise(slow, NOW) is None
    assert checks.rapid_rise(fast, NOW) == pytest.approx(config.RISE_M + 0.1)
    assert checks.rapid_rise(gap, NOW) is None


def test_old_rise_is_not_reported_as_current():
    # A rise that happened two days ago, after which the station went quiet,
    # must not keep showing as "rapid rise" on today's page.
    old = NOW - timedelta(days=2)
    history = [(old - timedelta(minutes=30), 1.0), (old, 2.0)]
    assert checks.rapid_rise(history, NOW) is None


def test_fetch_retries_then_succeeds(monkeypatch):
    calls = {"n": 0}

    class Resp:
        text = "ok"

        def raise_for_status(self):
            pass

    def flaky_get(*a, **k):
        calls["n"] += 1
        if calls["n"] < 3:
            raise fetch.requests.ConnectionError("down")
        return Resp()

    monkeypatch.setattr(fetch.requests, "get", flaky_get)
    assert fetch.fetch_page(attempts=3, backoff_s=0) == "ok"
    assert calls["n"] == 3


def test_after_end_date_page_is_archived_and_no_fetch(tmp_path, monkeypatch):
    ids = [c["id"] for c in config.CORRIDOR]
    src = tmp_path / "page.html"
    src.write_text(page([station(i, 10) for i in ids]), encoding="utf-8")
    store, site = tmp_path / "store", tmp_path / "site"
    assert run.main(["--store", str(store), "--site", str(site), "--html", str(src), "--now", NOW.isoformat()]) == 0

    def no_fetch(*a, **k):
        raise AssertionError("must not contact DHM after the end date")

    monkeypatch.setattr(fetch, "fetch_page", no_fetch)
    after = (datetime.fromisoformat(config.END_AT) + timedelta(minutes=5)).isoformat()
    assert run.main(["--store", str(store), "--site", str(site), "--now", after]) == 0
    html = (site / "index.html").read_text()
    assert "Monitoring ended" in html and "not current" in html
    assert (store / "ARCHIVED").exists()


def test_full_pass_offline(tmp_path):
    ids = [c["id"] for c in config.CORRIDOR]
    stations = [station(ids[0], None), station(ids[1], 10, 2.0)] + [station(i, 400) for i in ids[2:]] + [station(99999, 5)]
    src = tmp_path / "page.html"
    src.write_text(page(stations), encoding="utf-8")
    store, site = tmp_path / "store", tmp_path / "site"
    assert run.main(["--store", str(store), "--site", str(site), "--html", str(src), "--now", NOW.isoformat()]) == 0
    latest = json.loads((store / "latest.json").read_text())
    states = {r["id"]: r["state"] for r in latest["corridor"]}
    assert states[ids[0]] == checks.NO_DATA and states[ids[1]] == checks.OK and states[ids[2]] == checks.SILENT
    assert latest["national"]["total"] == len(stations)
    assert "This is not a warning system" in (site / "index.html").read_text()


def test_source_error_keeps_previous_page(tmp_path):
    bad = tmp_path / "bad.html"
    bad.write_text("<html>changed layout</html>")
    store, site = tmp_path / "store", tmp_path / "site"
    assert run.main(["--store", str(store), "--site", str(site), "--html", str(bad), "--now", NOW.isoformat()]) == 2
    assert "could not read" in (site / "index.html").read_text()
    assert "SOURCE ERROR" in (store / "events.csv").read_text()
