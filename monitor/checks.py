"""The two checks: is a station silent, and is the water rising fast."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from . import config

OK, LATE, SILENT, NO_DATA = "OK", "LATE", "SILENT", "NO DATA"


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def reading_of(station: dict) -> tuple[datetime | None, float | None]:
    wl = station.get("waterLevel") or {}
    when = parse_time(wl.get("datetime"))
    try:
        value = float(wl["value"]) if wl.get("value") is not None else None
    except (TypeError, ValueError):
        value = None
    return when, value


def silence(station: dict, now: datetime) -> tuple[str, float | None]:
    """Return (state, age in minutes) for a station's latest reading."""
    when, value = reading_of(station)
    if when is None or value is None:
        return NO_DATA, None
    age = (now - when).total_seconds() / 60
    if age > config.SILENT_AFTER_MIN:
        return SILENT, age
    if age > config.LATE_AFTER_MIN:
        return LATE, age
    return OK, age


def rapid_rise(history: list[tuple[datetime, float]]) -> float | None:
    """Return the rise in metres if the latest reading is RISE_M above any
    reading in the preceding RISE_WINDOW_MIN; otherwise None.

    `history` is (reading_time, value) for one station, any order.
    """
    if len(history) < 2:
        return None
    pts = sorted(history)
    latest_t, latest_v = pts[-1]
    window_start = latest_t - timedelta(minutes=config.RISE_WINDOW_MIN)
    earlier = [v for t, v in pts[:-1] if t >= window_start]
    if not earlier:
        return None
    rise = latest_v - min(earlier)
    return rise if rise >= config.RISE_M else None


def national_summary(stations: list[dict], now: datetime) -> dict:
    counts = {OK: 0, LATE: 0, SILENT: 0, NO_DATA: 0}
    for s in stations:
        state, _ = silence(s, now)
        counts[state] += 1
    return {"total": len(stations), **counts}
