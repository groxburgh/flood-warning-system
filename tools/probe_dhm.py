"""One-off probe: find where DHM's station pages load their readings from.

Opens a few DHM pages in headless Chromium, clicks through the observation
controls, and records every network request the pages make. Output goes to
probe/output/ so it can be inspected after a GitHub Actions run.
"""

import json
import pathlib
import re

from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent / "probe_output"  # gitignored: raw pages contain staff contact details
OUT.mkdir(parents=True, exist_ok=True)

PAGES = {
    # Bhote Koshi at Shyaprubesi (station index 446.25)
    "station_191": "https://www.dhm.gov.np/hydrology/hms-Single/191",
    # Trishuli River at Kali Khola (downstream on the same corridor)
    "station_4781": "https://www.dhm.gov.np/hydrology/hms-Single/4781",
    "flood_monitoring": "https://www.dhm.gov.np/hydrology/floodMonitoring",
    "hydrology_gov_np": "https://hydrology.gov.np/",
}

INTERESTING = re.compile(r"(api|json|ajax|data|observ|water|level|station|graph|chart|river)", re.I)


def probe(page_name, url, browser):
    records = []
    ctx = browser.new_context(ignore_https_errors=True)
    page = ctx.new_page()

    def on_response(resp):
        req = resp.request
        if req.resource_type not in ("xhr", "fetch", "document", "script"):
            return
        entry = {
            "url": req.url,
            "method": req.method,
            "type": req.resource_type,
            "status": resp.status,
            "content_type": resp.headers.get("content-type", ""),
            "post_data": (req.post_data or "")[:2000],
        }
        if req.resource_type in ("xhr", "fetch"):
            try:
                entry["body_head"] = resp.text()[:4000]
            except Exception as exc:  # noqa: BLE001
                entry["body_head"] = f"<unreadable: {exc}>"
        records.append(entry)

    page.on("response", on_response)
    try:
        page.goto(url, wait_until="networkidle", timeout=60000)
    except Exception as exc:  # noqa: BLE001
        records.append({"error": f"goto failed: {exc}"})

    # Try the observation controls on station pages: pick Hourly, press VIEW.
    for label in ("Hourly", "7 Days Point", "Point"):
        try:
            page.get_by_text(label, exact=True).first.click(timeout=5000)
            page.get_by_text("VIEW", exact=True).first.click(timeout=5000)
            page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:  # noqa: BLE001
            pass

    (OUT / f"{page_name}.html").write_text(page.content(), encoding="utf-8")
    # Pull inline-script lines that mention likely endpoints.
    hints = sorted({line.strip()[:300] for line in page.content().splitlines() if INTERESTING.search(line) and ("http" in line or "url" in line.lower())})
    (OUT / f"{page_name}_hints.txt").write_text("\n".join(hints), encoding="utf-8")
    (OUT / f"{page_name}_network.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
    ctx.close()
    return records


def main():
    summary = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, url in PAGES.items():
            recs = probe(name, url, browser)
            summary[name] = [
                {k: r.get(k) for k in ("type", "method", "status", "url")}
                for r in recs
                if r.get("type") in ("xhr", "fetch") or "error" in r
            ]
        browser.close()
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
