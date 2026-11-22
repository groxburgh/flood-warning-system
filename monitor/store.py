"""Plain-CSV storage kept on the repo's `data` branch."""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path

from .checks import parse_time

CORRIDOR_HISTORY = "corridor_history.csv"
NATIONAL_HISTORY = "national_history.csv"
EVENTS = "events.csv"
LATEST = "latest.json"


def _append(path: Path, header: list[str], rows: list[list]) -> None:
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(header)
        w.writerows(rows)


def load_corridor_history(store: Path) -> dict[int, list[tuple[datetime, float]]]:
    path = store / CORRIDOR_HISTORY
    out: dict[int, list[tuple[datetime, float]]] = {}
    if not path.exists():
        return out
    with path.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            t = parse_time(row["reading_time_utc"])
            if t is None:
                continue
            out.setdefault(int(row["station_id"]), []).append((t, float(row["value"])))
    return out


def append_corridor_readings(store: Path, readings: list[tuple[int, datetime, float]], fetched: datetime) -> int:
    """Append readings not already stored. Returns how many were new."""
    known = {(sid, t) for sid, pts in load_corridor_history(store).items() for t, _ in pts}
    rows = [
        [sid, t.isoformat(), value, fetched.isoformat()]
        for sid, t, value in readings
        if (sid, t) not in known
    ]
    _append(store / CORRIDOR_HISTORY, ["station_id", "reading_time_utc", "value", "fetched_at_utc"], rows)
    return len(rows)


def append_national(store: Path, fetched: datetime, summary: dict) -> None:
    _append(
        store / NATIONAL_HISTORY,
        ["fetched_at_utc", "total", "ok", "late", "silent", "no_data"],
        [[fetched.isoformat(), summary["total"], summary["OK"], summary["LATE"], summary["SILENT"], summary["NO DATA"]]],
    )


def load_national(store: Path) -> list[dict]:
    path = store / NATIONAL_HISTORY
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def append_events(store: Path, events: list[list]) -> None:
    if events:
        _append(store / EVENTS, ["fetched_at_utc", "station_id", "station", "event", "detail"], events)


def load_events(store: Path, limit: int = 20) -> list[dict]:
    path = store / EVENTS
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return rows[-limit:][::-1]


def load_latest(store: Path) -> dict | None:
    path = store / LATEST
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


ARCHIVED = "ARCHIVED"


def mark_archived(store: Path, end_at: datetime) -> None:
    """Leave a marker so later scheduled runs can skip all work."""
    (store / ARCHIVED).write_text(f"Monitoring ended {end_at.isoformat()}\n", encoding="utf-8")


def save_latest(store: Path, latest: dict) -> None:
    (store / LATEST).write_text(json.dumps(latest, indent=2), encoding="utf-8")
