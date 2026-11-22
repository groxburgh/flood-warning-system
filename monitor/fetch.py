"""Fetch and parse DHM's public flood-monitoring page.

The page embeds the latest reading for every river-watch station as a
JavaScript array (`var riverwatch_coordinates = [...]`). We read that array
and keep only whitelisted fields. The raw feed also carries station staff
names and phone numbers, which must never be stored or published.
"""

from __future__ import annotations

import json
import re
import time

import requests

from .config import FETCH_ATTEMPTS, FETCH_BACKOFF_S, SOURCE_URL

KEEP_FIELDS = (
    "id",
    "name",
    "stationIndex",
    "basin",
    "district",
    "latitude",
    "longitude",
    "series_id",
    "waterLevel",
    "status",
    "warning_level",
    "danger_level",
    "steady",
)

_ARRAY_RE = re.compile(r"var\s+riverwatch_coordinates\s*=\s*(\[.*?\]);\s*$", re.S | re.M)

USER_AGENT = (
    "bhote-koshi-watch/0.1 (public monitoring prototype; "
    "https://github.com/groxburgh/flood-warning-system)"
)


class SourceFormatError(RuntimeError):
    """The page no longer looks the way this parser expects."""


def fetch_page(url: str = SOURCE_URL, timeout: int = 60, attempts: int = FETCH_ATTEMPTS,
               backoff_s: float = FETCH_BACKOFF_S) -> str:
    """GET the page, retrying transient failures with a growing pause."""
    last_exc: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < attempts:
                time.sleep(backoff_s * attempt)
    raise last_exc  # type: ignore[misc]


def sanitize(station: dict) -> dict:
    clean = {k: station.get(k) for k in KEEP_FIELDS}
    wl = clean.get("waterLevel")
    if isinstance(wl, dict):
        clean["waterLevel"] = {"datetime": wl.get("datetime"), "value": wl.get("value")}
    else:
        clean["waterLevel"] = None
    return clean


def parse_stations(html: str) -> list[dict]:
    match = _ARRAY_RE.search(html)
    if not match:
        raise SourceFormatError("riverwatch_coordinates array not found on page")
    try:
        raw = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise SourceFormatError(f"riverwatch_coordinates is not valid JSON: {exc}") from exc
    if not isinstance(raw, list) or not raw:
        raise SourceFormatError("riverwatch_coordinates is empty or not a list")
    return [sanitize(s) for s in raw if isinstance(s, dict)]
