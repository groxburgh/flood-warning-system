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
    stale = [(t - timedelta(minutes=config.RISE_WINDOW_MIN + 30), 1.0), (t, 3.0)]
    assert checks.rapid_rise(slow) is None
    assert checks.rapid_rise(fast) == pytest.approx(config.RISE_M + 0.1)
    assert checks.rapid_rise(stale) is None


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
    assert run.main(["--store", str(store), "--site", str(site), "--html", str(bad), "--now", NOW.isoformat()]) == 1
    assert "could not read" in (site / "index.html").read_text()
    assert "SOURCE ERROR" in (store / "events.csv").read_text()
