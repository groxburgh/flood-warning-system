"""One monitoring pass: fetch, check, store, render.

    python -m monitor.run --store data --site site
    python -m monitor.run --store data --site site --html saved_page.html   # offline
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import checks, config, fetch, site, store


def corridor_status(stations: list[dict], history: dict, now: datetime) -> list[dict]:
    by_id = {s["id"]: s for s in stations}
    rows = []
    for spec in config.CORRIDOR:
        s = by_id.get(spec["id"])
        if s is None:
            rows.append({**spec, "state": "MISSING FROM FEED", "age_min": None, "value": None,
                         "reading_time": None, "dhm_status": None, "dhm_trend": None,
                         "warning_level": None, "danger_level": None, "rise_m": None})
            continue
        state, age = checks.silence(s, now)
        when, value = checks.reading_of(s)
        rise = checks.rapid_rise(history.get(spec["id"], []), now)
        rows.append({
            **spec,
            "state": state,
            "age_min": round(age) if age is not None else None,
            "value": value,
            "reading_time": when.isoformat() if when else None,
            "dhm_status": s.get("status"),
            "dhm_trend": s.get("steady") or None,
            "warning_level": s.get("warning_level") or None,
            "danger_level": s.get("danger_level") or None,
            "rise_m": round(rise, 2) if rise is not None else None,
        })
    return rows


def transitions(previous: dict | None, current: list[dict], fetched: datetime) -> list[list]:
    prev = {r["id"]: r for r in (previous or {}).get("corridor", [])}
    events = []
    for r in current:
        p = prev.get(r["id"])
        if p is None or p["state"] != r["state"]:
            before = p["state"] if p else "first check"
            events.append([fetched.isoformat(), r["id"], r["label"], "STATE", f"{before} -> {r['state']}"])
        if r["rise_m"] is not None and (p is None or p.get("rise_m") is None):
            events.append([fetched.isoformat(), r["id"], r["label"], "RAPID RISE",
                           f"+{r['rise_m']} m within {config.RISE_WINDOW_MIN} min"])
        if p and r["dhm_status"] and r["dhm_status"] != p.get("dhm_status"):
            events.append([fetched.isoformat(), r["id"], r["label"], "DHM STATUS",
                           f"{p.get('dhm_status')} -> {r['dhm_status']}"])
    return events


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", type=Path, required=True)
    ap.add_argument("--site", type=Path, required=True)
    ap.add_argument("--html", type=Path, help="parse a saved page instead of fetching")
    ap.add_argument("--now", help="override current time (ISO 8601), for testing")
    args = ap.parse_args(argv)

    args.store.mkdir(parents=True, exist_ok=True)
    now = datetime.fromisoformat(args.now) if args.now else datetime.now(timezone.utc)
    previous = store.load_latest(args.store)
    end_at = datetime.fromisoformat(config.END_AT)

    if now >= end_at:
        # Monitoring period is over: no request to DHM, page relabelled as an archive.
        last = datetime.fromisoformat(previous["checked_at"]) if previous else now
        site.render(args.site, previous, store.load_national(args.store),
                    store.load_corridor_history(args.store), store.load_events(args.store),
                    checked_at=last, archived_at=end_at)
        store.mark_archived(args.store, end_at)
        print(f"monitoring ended at {end_at.isoformat()}; archive page rendered")
        return 0

    try:
        html = args.html.read_text(encoding="utf-8") if args.html else fetch.fetch_page()
        stations = fetch.parse_stations(html)
    except Exception as exc:  # noqa: BLE001 - record source failure on the page and in the log
        store.append_events(args.store, [[now.isoformat(), "", "DHM source", "SOURCE ERROR", str(exc)[:300]]])
        site.render(args.site, previous, store.load_national(args.store),
                    store.load_corridor_history(args.store), store.load_events(args.store),
                    source_error=f"{type(exc).__name__}: {exc}"[:300], checked_at=now)
        print(f"source error: {exc}", file=sys.stderr)
        # Exit 2 marks a source error. The workflow treats it as handled (shown on the
        # page) so an unattended project does not send a failure email every 30 minutes.
        return 2

    corridor_ids = {c["id"] for c in config.CORRIDOR}
    readings = []
    for s in stations:
        if s["id"] in corridor_ids:
            when, value = checks.reading_of(s)
            if when is not None and value is not None:
                readings.append((s["id"], when, value))
    added = store.append_corridor_readings(args.store, readings, now)

    history = store.load_corridor_history(args.store)
    corridor = corridor_status(stations, history, now)
    national = checks.national_summary(stations, now)
    store.append_national(args.store, now, national)
    store.append_events(args.store, transitions(previous, corridor, now))

    latest = {"checked_at": now.isoformat(), "corridor": corridor, "national": national,
              "source": config.SOURCE_URL}
    store.save_latest(args.store, latest)

    cutoff = now - timedelta(hours=config.CHART_HOURS)
    chart_history = {sid: [(t, v) for t, v in pts if t >= cutoff] for sid, pts in history.items()}
    site.render(args.site, latest, store.load_national(args.store), chart_history,
                store.load_events(args.store), checked_at=now)

    print(f"{len(stations)} stations parsed; {added} new corridor readings; national {national}")
    for r in corridor:
        print(f"  {r['label']:<32} {r['state']:<18} age={r['age_min']} value={r['value']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
