# Bhote Koshi–Trishuli gauge watch

A public monitoring prototype for the river corridor in Nepal hit by flash floods in July 2025 and August 2026. Every 30 minutes it reads the live gauge feed published by Nepal's Department of Hydrology and Meteorology (DHM), checks whether each gauge on the corridor is still reporting, flags fast rises in water level, and publishes the result as a status page.

**Status page:** https://groxburgh.github.io/flood-warning-system/

This is not a warning system and must not be relied on as one. Checks run on GitHub's scheduler, which can delay or skip runs, and the thresholds are uncalibrated. For flood warnings in Nepal, use [DHM](https://www.dhm.gov.np/) and [hydrology.gov.np](https://hydrology.gov.np/).

## Why gauge silence matters

On 26 August 2026 an ice-rock avalanche from the north face of Langtang Lirung became a debris flow in the Lhende Khola and travelled down the Bhote Koshi into the Trishuli. According to the International Centre for Integrated Mountain Development's page "Kyirong-Rasuwa Flood 2026 | Nepal-China Cryosphere Risk" (published 28 August 2026, updated 14 October 2026), several gauging stations in the upper corridor were destroyed, the Rasuwagadhi gauge showed no rise before it was destroyed, and no warning reached Rasuwagadhi or Timure. Dr. Santosh Kumar Rauniyar's "The Langtang Collapse" (Sasakawa Peace Foundation, September 2026) names four hydrometric stations destroyed by the flood: Betrawati, Bhote Koshi, Syabrubesi and Malekhu. The two accounts give different minute-by-minute timings for when DHM learned of the flood and when SMS alerts went out; both place the alerts after the surge had reached the border settlements.

A gauge that stops reporting may have a technical fault, or it may have been hit by the flood it was there to measure. DHM's public feed does not distinguish between the two, and silence on this corridor is only noticed if someone happens to look. This project checks for it on a schedule and keeps a public record.

## What it does

| Check | Rule | Why |
|---|---|---|
| Reporting | OK if the latest reading is under 60 min old; **late** after 60 min; **silent** after 6 h; **no data** if DHM lists the station with no reading | Gauges that report every 5 to 10 minutes and then stop are a signal in themselves |
| Rapid rise | Flag a rise of 0.5 m or more within 60 min | A placeholder for "the river is doing something unusual" |
| DHM status | Shows DHM's own warning/danger status and trend | So the page never contradicts the official source silently |

It watches nine corridor stations from Rasuwagadi on the China border down to Bhorle, and also counts how many of DHM's ~330 listed river stations are reporting at each check.

All thresholds live in [`monitor/config.py`](monitor/config.py). They are assumptions: the 5 to 10 minute reporting cadence is what the feed shows at working stations, not a documented DHM figure, and the rise threshold has not been tested against any station's flood record.

## What the first run found

The first check (22 November 2026, about three months after the flood) recorded no current reading for the mainstem gauges at Rasuwagadi, Shyaprubesi and Betrawati. That fits the reports above that these stations were destroyed, but this project cannot confirm why a station is silent. In the same feed, DHM's status field still read "BELOW WARNING LEVEL" for each of those stations, so anyone reading the status alone would see a calm river rather than a missing gauge. Nationally, roughly half of the listed river stations had no reading in the feed. Some of those may be seasonal, manual or retired stations rather than failures; the feed does not say which.

## How it works

```
GitHub Actions (every 30 min)
  └─ monitor/fetch.py   read DHM's public flood-monitoring page, keep whitelisted fields only
  └─ monitor/checks.py  silence + rapid-rise checks
  └─ monitor/store.py   append to CSV history on the `data` branch
  └─ monitor/site.py    render a static page, deploy to GitHub Pages
```

- **Source.** DHM's [flood monitoring page](https://www.dhm.gov.np/hydrology/floodMonitoring) embeds the latest reading for every river-watch station. `tools/probe_dhm.py` is the headless-browser probe used to find it.
- **Privacy.** DHM's feed also contains station staff names and phone numbers. The parser keeps a fixed whitelist of fields, and a test checks that nothing else gets through.
- **Load on DHM.** One page request every 30 minutes, with a user agent that links back here.
- **History.** Raw readings, national counts and state changes are plain CSV on the [`data`](../../tree/data) branch, so the main branch history stays readable.
- **Failure.** If DHM's page changes shape, the run fails visibly, logs a `SOURCE ERROR`, and the status page says so while keeping the last good data.

Run it locally:

```bash
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q
python -m monitor.run --store store --site site      # writes site/index.html
```

## Limits

- GitHub's scheduler is best-effort, and GitHub disables scheduled workflows in public repositories after 60 days without repository activity.
- A 30-minute check is far too slow to warn anyone about a surge that, by the accounts above, crossed from the border to Betrawati in well under an hour.
- The rapid-rise check needs two readings inside its window, so it says nothing about a station that is already silent.
- The page shows what DHM publishes. It has no independent sensors.

## Research

Background research on warning options for this corridor (detection methods, travel times, institutional constraints) will be added under [`research/`](research/).

## Data and licence

River data is published by the Department of Hydrology and Meteorology, Government of Nepal. Code is MIT licensed.
