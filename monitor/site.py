"""Render the static status page (one HTML file, no JavaScript)."""

from __future__ import annotations

import html
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import config

NPT = timezone(timedelta(hours=5, minutes=45), "NPT")

STATE_CLASS = {"OK": "ok", "LATE": "late", "SILENT": "silent", "NO DATA": "nodata", "MISSING FROM FEED": "nodata"}


def _t(iso: str | None) -> str:
    if not iso:
        return "—"
    dt = datetime.fromisoformat(iso).astimezone(NPT)
    return dt.strftime("%d %b %H:%M NPT")


def _age(minutes: int | None) -> str:
    if minutes is None:
        return "—"
    if minutes < 90:
        return f"{minutes} min"
    if minutes < 48 * 60:
        return f"{minutes / 60:.1f} h"
    return f"{minutes / 1440:.1f} days"


def _spark(points: list[tuple[datetime, float]], w: int = 160, h: int = 36) -> str:
    if len(points) < 2:
        return '<span class="muted">not enough data</span>'
    pts = sorted(points)
    t0, t1 = pts[0][0].timestamp(), pts[-1][0].timestamp()
    vs = [v for _, v in pts]
    lo, hi = min(vs), max(vs)
    span_t = (t1 - t0) or 1
    span_v = (hi - lo) or 1
    coords = " ".join(
        f"{(t.timestamp() - t0) / span_t * (w - 4) + 2:.1f},{h - 2 - (v - lo) / span_v * (h - 4):.1f}"
        for t, v in pts
    )
    label = f"{lo:.2f}–{hi:.2f} m over {len(pts)} readings"
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{label}"><polyline points="{coords}" /></svg>'
            f'<div class="muted small">{label}</div>')


def _national_chart(rows: list[dict], w: int = 640, h: int = 120) -> str:
    rows = rows[-500:]
    if len(rows) < 2:
        return '<p class="muted">The chart appears after a few checks have run.</p>'
    shares = [int(r["ok"]) / max(int(r["total"]), 1) for r in rows]
    n = len(shares)
    coords = " ".join(f"{i / (n - 1) * (w - 40) + 36:.1f},{h - 18 - s * (h - 28):.1f}" for i, s in enumerate(shares))
    first, last = _t(rows[0]["fetched_at_utc"]), _t(rows[-1]["fetched_at_utc"])
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="Share of stations reporting on time">'
            f'<line x1="36" y1="{h - 18}" x2="{w - 4}" y2="{h - 18}" class="axis"/>'
            f'<text x="30" y="14" class="tick" text-anchor="end">100%</text>'
            f'<text x="30" y="{h - 18}" class="tick" text-anchor="end">0%</text>'
            f'<polyline points="{coords}" />'
            f'<text x="36" y="{h - 2}" class="tick">{first}</text>'
            f'<text x="{w - 4}" y="{h - 2}" class="tick" text-anchor="end">{last}</text></svg>')


CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a65;--line:#e4e1d9;--ok:#2f7d4f;--late:#b7791f;--silent:#b3261e;--nodata:#5b5b5b;--accent:#2b5c8a}
@media (prefers-color-scheme:dark){:root{--bg:#16171a;--fg:#ececea;--muted:#9a9a95;--line:#2c2e33;--ok:#5cc489;--late:#e0a84a;--silent:#ff7a70;--nodata:#9a9a9a;--accent:#7fb0e0}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:960px;margin:0 auto;padding:28px 18px 60px}h1{font-size:1.6rem;margin:0 0 4px}h2{font-size:1.15rem;margin:36px 0 8px}
.muted{color:var(--muted)}.small{font-size:.8rem}.notice{border:1px solid var(--line);border-left:4px solid var(--accent);padding:12px 14px;margin:18px 0;border-radius:6px}
.error{border-left-color:var(--silent)}table{width:100%;border-collapse:collapse;font-size:.92rem}th,td{text-align:left;padding:9px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.03em}.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:.78rem;font-weight:600;color:#fff;white-space:nowrap}
.ok{background:var(--ok)}.late{background:var(--late)}.silent{background:var(--silent)}.nodata{background:var(--nodata)}
.spark polyline,.chart polyline{fill:none;stroke:var(--accent);stroke-width:1.6}.chart{width:100%;height:auto}.axis{stroke:var(--line)}.tick{fill:var(--muted);font-size:10px}
.kpis{display:flex;gap:12px;flex-wrap:wrap}.kpi{border:1px solid var(--line);border-radius:8px;padding:10px 14px;min-width:120px}.kpi b{display:block;font-size:1.4rem}
.wrap{overflow-x:auto}a{color:var(--accent)}footer{margin-top:40px;font-size:.85rem}
@media (max-width:640px){table.cards,table.cards tbody,table.cards tr,table.cards td{display:block;width:100%}
table.cards tr.head{display:none}table.cards tr{border:1px solid var(--line);border-radius:8px;padding:6px 10px;margin:0 0 10px}
table.cards td{border:0;padding:4px 0}table.cards td[data-l]::before{content:attr(data-l);display:block;color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.03em}}
"""


def render(site_dir: Path, latest: dict | None, national_rows: list[dict], history: dict,
           events: list[dict], checked_at: datetime, source_error: str | None = None,
           archived_at: datetime | None = None) -> None:
    site_dir.mkdir(parents=True, exist_ok=True)
    esc = html.escape
    parts = [f"<!doctype html><html lang='en'><head><meta charset='utf-8'>"
             f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
             f"<title>Bhote Koshi–Trishuli gauge watch</title><style>{CSS}</style></head><body><main>",
             "<h1>Bhote Koshi–Trishuli gauge watch</h1>",
             f"<p class='muted'>Last checked {esc(_t(checked_at.isoformat()))}. "
             f"Readings from the <a href='{config.SOURCE_URL}'>{esc(config.SOURCE_NAME)}</a>.</p>",
             "<div class='notice'><b>This is not a warning system.</b> It is a public prototype that "
             "watches whether river gauges on one Himalayan corridor are reporting, and flags fast rises. "
             "Checks run roughly every 30 minutes and can be delayed. For flood warnings in Nepal, use "
             "<a href='https://www.dhm.gov.np/'>DHM</a> and "
             "<a href='https://hydrology.gov.np/'>hydrology.gov.np</a>.</div>"]

    if archived_at:
        parts.append(f"<div class='notice error'><b>Monitoring ended on {esc(_t(archived_at.isoformat()))}.</b> "
                     "This page is an archive of the last check. The readings below are not current. "
                     "The full record is on the repository's <code>data</code> branch.</div>")

    if source_error:
        parts.append(f"<div class='notice error'><b>The last check could not read DHM's page.</b> "
                     f"<span class='muted'>{esc(source_error)}</span> The table below is from the previous good check.</div>")

    if latest:
        parts.append("<h2>Corridor gauges, upstream to downstream</h2>"
                     f"<p class='muted small'>Late = no reading for {config.LATE_AFTER_MIN} min; "
                     f"silent = none for {config.SILENT_AFTER_MIN // 60} h; no data = DHM's feed lists the "
                     "station with no reading. Thresholds are assumptions, not DHM's.</p>"
                     "<div class='wrap'><table class='cards'><tr class='head'><th>Station</th><th>Reporting</th><th>Latest reading</th>"
                     "<th>DHM status</th><th>Last 48 h</th></tr>")
        for r in latest["corridor"]:
            cls = STATE_CLASS.get(r["state"], "nodata")
            value = f"{r['value']:.2f} m" if r["value"] is not None else "—"
            levels = []
            if r.get("warning_level"):
                levels.append(f"warning {esc(str(r['warning_level']))}")
            if r.get("danger_level"):
                levels.append(f"danger {esc(str(r['danger_level']))}")
            rise = (f"<div><span class='badge silent'>rapid rise +{r['rise_m']} m</span></div>"
                    if r.get("rise_m") is not None else "")
            parts.append(
                f"<tr><td><a href='https://www.dhm.gov.np/hydrology/hms-Single/{r['id']}'>{esc(r['label'])}</a>"
                f"<div class='muted small'>{esc(r['role'])}</div></td>"
                f"<td data-l='Reporting'><span class='badge {cls}'>{esc(r['state'])}</span><div class='muted small'>age {_age(r['age_min'])}</div></td>"
                f"<td data-l='Latest reading'>{value}<div class='muted small'>{esc(_t(r['reading_time']))}</div>{rise}</td>"
                f"<td data-l='DHM status'>{esc(r.get('dhm_status') or '—')}<div class='muted small'>{esc(r.get('dhm_trend') or '')}"
                f"{' · ' if levels and r.get('dhm_trend') else ''}{' · '.join(levels)}</div></td>"
                f"<td data-l='Last 48 h'>{_spark(history.get(r['id'], []))}</td></tr>")
        parts.append("</table></div>")

        n = latest["national"]
        parts.append("<h2>All DHM river stations</h2><div class='kpis'>"
                     f"<div class='kpi'><b>{n['OK']}</b>reporting</div>"
                     f"<div class='kpi'><b>{n['LATE']}</b>late</div>"
                     f"<div class='kpi'><b>{n['SILENT']}</b>silent</div>"
                     f"<div class='kpi'><b>{n['NO DATA']}</b>no data</div>"
                     f"<div class='kpi'><b>{n['total']}</b>listed</div></div>"
                     "<p class='muted small'>Share of listed stations reporting on time, per check:</p>"
                     + _national_chart(national_rows))

    if events:
        parts.append("<h2>Recent changes</h2><div class='wrap'><table><tr><th>When</th><th>Station</th><th>Change</th></tr>")
        for e in events:
            parts.append(f"<tr><td>{esc(_t(e['fetched_at_utc']))}</td><td>{esc(e['station'])}</td>"
                         f"<td>{esc(e['event'])}: {esc(e['detail'])}</td></tr>")
        parts.append("</table></div>")

    parts.append("<footer class='muted'>Code and method: "
                 "<a href='https://github.com/groxburgh/flood-warning-system'>github.com/groxburgh/flood-warning-system</a>. "
                 "Raw history (CSV): <a href='https://github.com/groxburgh/flood-warning-system/tree/data'>"
                 "<code>data</code> branch</a>.</footer></main></body></html>")
    (site_dir / "index.html").write_text("".join(parts), encoding="utf-8")
