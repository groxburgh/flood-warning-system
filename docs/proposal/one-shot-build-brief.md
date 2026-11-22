# One-Shot Build Brief: Himalayan Flood Warning Software

**For: Greg's brother. From: Greg (research by Claude, 28 Aug 2026).**
**Read time: 10 minutes. Everything you need is in this file; the seven research reports exist if you want the evidence behind any claim, but you should not need them to start.**

## The mission, in one paragraph

On 26 August 2026 a glacier collapsed on the Nepal-Tibet border and the resulting flood killed 500+ people down the Bhote Koshi/Trishuli valley. The seismic signal of the collapse was on public global networks within minutes — catalogued as an earthquake. Nepal's river gauges were destroyed by the flood *before* crossing their alert thresholds, and went silent with nothing watching for silence. The government's flood office learned of the disaster by telephone, 23 minutes in, from a man who saw it. Their SMS machine then worked well — 679,295 texts in 16 minutes, a school of 1,650 kids evacuated. The gap is not sensors and not dissemination. It is **software between signals that already exist and institutions that already act**. We are going to build that software. Two tools, both free, both feeding institutions only (never the public — that matters legally, see the last section).

## Product 1 — STATION SENTINEL (build this first)

**What it is:** a watcher on Nepal's existing river-gauge telemetry that alerts the flood office when a station goes silent or behaves anomalously.

**Why it matters — CORRECTED 29 Aug after two external reviews; read `review-adjudication.md`.** An earlier draft of this brief claimed the alarm would have bought ~20 minutes on 26 August. That was wrong: it was computed before we measured BIPAD's 5–15 minute ingest lag and was never updated afterwards. Recomputed honestly, a two-missed-samples rule on Rasuwagadhi fires between **09:05 and 09:20** against an actual SMS dispatch at **09:16** and DHM's own telephone knowledge at **09:00**. The real gain on this event is **−4 to +11 minutes**. Do not repeat the 20-minute figure to anyone.

What survives the correction is an argument about variance, not about this event. 26 August happened at 08:40 on a clear morning at a border post with hundreds of people present; the phone call was luck, and Nepali commentators said so. The case for the tool is the event that happens at 3 a.m., or in an upper catchment with nobody in it, where there is no one to make the call at all.

The stronger product framing (both reviewers converged on it independently, and it is now the primary): **this is a network-health tool first**. The corridor's Ghodatalbela station has been silent since **4 August** — three weeks before the disaster, unnoticed. The sensing layer every future warning depends on was already degraded and nobody knew. Warning systems die of dead batteries and unpaid telecom bills far more often than of bad algorithms.

**Data source — RESOLVED (recon done 28-29 Aug, see tech-stack.md for verified details):** the BIPAD portal REST API at `https://bipadportal.gov.np/api/v1/` is live, public, and unauthenticated, mirroring DHM telemetry ("dataSource": "hydrology.gov.np") at 10-minute cadence with 5-15 min ingest lag and ~5 weeks of retained history. `/river-stations/` gives every station's latest reading in one call; `/river/?ordering=-id` gives the time series. Three traps, verified: `ordering=-createdOn`/`-waterLevelOn` and all date filters are SILENTLY IGNORED (use `ordering=-id` only and assert freshness every poll); the `count` field is a garbage sentinel; the `earthquake` endpoint is a year stale (never use it). **The kill criterion is retired: Sentinel is buildable today with no DHM cooperation.** DHM engagement is now step two, done from a working demo. Two gifts in the data: the API still holds the 26 Aug gauge deaths in downstream order (Rasuwagadhi 08:40 → Syabrubesi 08:50 → Betrawati 09:20, all BELOW WARNING LEVEL, while Dhunche off the flood path never stopped) — your demo is a replay of reality; and the Ghodatalbela station has been silent since 4 August, three weeks before the disaster, apparently unnoticed — the network-health story writes itself.

**Logic spec — two products in the data model, not just in the prose:**
1. Poll every station on a short interval; store (station, timestamp, level) in SQLite.
2. **NETWORK HEALTH (primary):** station misses N expected reports → SILENT. Delivered as a low-priority digest, phrased as a telemetry observation and nothing more. This channel has a natural owner, no alert-fatigue risk, and value on ordinary days.
3. **HAZARD SIGNAL (secondary, dual confirmation required):** SILENT escalates only on correlated evidence — (a) an adjacent station in the same basin also silent within a short window; (b) anomalous rise at a surviving neighbour; (c) a seismic flag from Product 2. Single-station silence never escalates on its own. CAP `certainty: Possible`, phrased as evidence rather than instruction.
4. **Rate-of-change trigger:** independent of thresholds, level rising faster than X m per 10 min → ALERT (the 26 Aug wave was +9 m in 30 min at Galchhi; normal monsoon rises are far slower — calibrate X from historical data you pull in recon).
5. Alerts go to a configured recipient list (during development: you and Greg only; after an MoU: DHM Flood Forecasting Division, NDRRMA). Email + Telegram bot is fine for v1.

**Effort:** a weekend for the poller+DB+dead-man core once the data source is understood; the calibration and the partnership are the long poles.

## Product 2 — MASS-MOVEMENT WATCHER

**What it is:** a classifier on public global seismic feeds that flags probable large mass movements (rock-ice avalanches, debris flows) in defined Himalayan border catchments and tells institutions which valley to look at, within ~3 minutes.

**Why it matters:** the 26 Aug collapse radiated seismic energy equivalent to M5.2. USGS's tectonic pipeline caught it instantly and called it an earthquake; the correct "landslide" call took hours. A Tibetan valley (Sedongpu) runs exactly this discrimination operationally — 12 triggers in 8 months, 9 real events, 3 false alarms, zero missed major events — using mostly **signal duration**: a collapse-debris flow radiates for several minutes, an earthquake of similar magnitude for ~1 minute, and the onset is emergent rather than impulsive.

**Data sources (recon done — tech-stack.md has the verified detail):**
- **The station that changes everything: Raspberry Shake `AM.R9445`, ~29 km from Langtang, directly on the corridor**, online since Nov 2024 — plus ~59 community stations within 2.5°, largely the Nepal School Seismology Network (NSSN, seismoschoolnp.org). Public FDSN access at `data.raspberryshake.org` (ObsPy: `Client('RASPISHAKE')`), **but embargoed to T-minus-30-minutes**. Real-time needs either a paid streaming agreement (sales@raspberryshake.org, price unknown — one email settles it) or an NSSN partnership (each Shake runs a LAN SeedLink server its host controls; a few cooperating schools = real-time for free). **Build at T+30 first: the detection/classification/alerting code is identical whether data arrives 30 minutes or 30 seconds late.** Swap the ingest layer when an agreement lands.
- Event veto channel: USGS GeoJSON feeds (updated every minute) + EMSC WebSocket (`wss://www.seismicportal.eu/standing_order/websocket`) — "a catalogued earthquake happened at this time" is the negative evidence that suppresses false alarms. First-solution latency for M4+ Asia is undocumented: **measure it** over a week of real events.
- Waveform archives for the replay gate: IRIS/EarthScope FDSN dataselect via ObsPy (IU.LSA Lhasa status unverified — check from your machine; blocked to our recon), plus RS FDSN (limits: 5 req/s, 30 req/min, 24h max per request).
- Training data: the **ESEC Exotic Seismic Events Catalog** (113 labeled mass movements, IRIS-hosted) and **USGS Seismogenic Landslides v3.0** (CC0, DOI 10.5066/P90VGCSK). Feature-extraction starter code: github.com/smousavi05/Seismic-Features-For-Machine-Learning. 113 positives is random-forest territory, not deep-learning territory — the literature agrees.
- Reference events for the replay gate: **26 Aug 2026 (USGS us7000tbwb, origin ~02:52:10 UTC)**, the **8 Jul 2025** Rasuwa flood, and **7 Feb 2021 Chamoli** (detection reported at stations up to 100 km). Bonus: check whether AM.R9445 recorded the 26 Aug collapse — at 29 km it almost certainly did, and that trace is your money chart.

**Logic spec:**
1. Watch the event feed for anything M≥4 inside defined watch polygons (start: a box around the Nepal-Tibet border from Langtang to the Arun; the corridors are in the research pack).
2. On trigger, pull waveforms from the nearest available stations and compute the discriminants: **total signal duration above noise** (collapse: >120–180 s; quake M4-5: <60–90 s), **onset emergence** (ratio of early-signal to peak amplitude — impulsive P onset says earthquake), **spectral character** (mass movements are depleted in high frequency at distance, long low-frequency coda).
3. Score → three states: TECTONIC / AMBIGUOUS / PROBABLE MASS MOVEMENT. On PROBABLE (and on AMBIGUOUS in a watch polygon): notify recipients with the event location, the intersecting river catchment ("possible mass movement, Lhende/Bhote Koshi catchment — check gauges and upstream contacts now"), confidence, and the raw evidence.
4. Accept ~25% false alarms at threshold — that's the operational benchmark from Tibet, and the recipients are institutions who can absorb a "check now" that's wrong one time in four. **Never auto-alert the public.**

**The go/no-go gate (do this before anything else on Product 2):** replay the three reference events through the classifier. If it cannot correctly classify all three as mass movements within 3 simulated minutes of first data availability — and correctly pass ordinary M4-5 Himalayan earthquakes (pull 20 from the same region/period as controls) — **stop and tell Greg**. That result is valuable too; it kills the idea cheaply, which is the point of the gate.

**Effort:** the replay harness is a focused week with ObsPy. The starter file `watcher_prototype.py` (alongside this brief) has the STA/LTA trigger, the duration/onset/spectral discriminants, and a synthetic test harness already written; the `fetch_real_waveforms()` stub shows the ObsPy calls to swap in on your machine.

## Stack and posture

Per the verified recon (tech-stack.md, read it once in full): Python 3.11+ with ObsPy 1.5.0 (LGPL, current), SeisBench's PhaseNet run *inverted* as an earthquake-veto (clean P+S picks = suppress; it has no mass-movement class, which is fine — we build only the positive side), SQLite in WAL mode per node, flat MiniSEED for waveforms. Alerts are generated as **CAP v1.2 XML from commit one** (an afternoon's work; gives you principled `Update`/`Cancel` retractions and lets `certainty: Possible` honestly say "gauge silent" rather than "flood coming"), rendered to a Telegram bot + transactional SMTP. **Two identical ~$5/mo VPS instances, different providers and regions, both computing everything, deduplicating at delivery on `sha256(product|station|event_type|sample_timestamp)`** — duplicate-and-dedupe beats leader election because a split brain doubles an alert while a failed election produces silence. Not hosted in Nepal (never sit inside the failure domain you're warning about). Every successful cycle pings a healthchecks-style dead-man on both nodes — a monitor whose own death is silent manufactures false confidence, which is worse than no monitor. Rejected after evaluation: SeisComP (AGPL, observatory-scale, earthquake-shaped), BIPAD's earthquake endpoint (a year stale). Log everything with timestamps — the audit trail is a legal asset (below). No dashboard, no frontend, no accounts: v1's entire UI is the alert message and a daily "I'm alive, here's what I saw" digest. Repo private until the first institutional conversation, then open-source it.

## What NOT to build (each killed by the research)

A public alerting app (legal exposure — below — and it duplicates the SMS machine that already works). A satellite precursor predictor (Chamoli proved timing is not forecastable from orbit: five years of visible motion, no terminal acceleration). A hazard dashboard as a product ("visibility" changes no decision; a status page ships inside the alert digest, nothing more). Sensor hardware (that's the $1.5–4M government/donor tier; our concept note for it exists and is being handed to the people with money).

## The legal line (read twice)

Nepal's Disaster Risk Reduction and Management Act §24(2) criminalizes false public alarms — "whoever makes or circulates a false alarm… leading to panic," fines and up to six months — and the good-faith immunity in §31 covers officials, not us. Nepal's Electronic Transactions Act has a documented pattern of broad use against online speech. So the products alert **named institutional recipients under an agreed arrangement**, phrased attributively ("station X silent since 08:52, upstream station rising — per DHM feed"), with the full decision trail logged. Feeding DHM is legally clean and is also simply the right architecture: they own the trust, the SMS pipes, and the mandate. If anyone ever asks us to alert the public directly, the answer is: that's DHM's job, we make DHM faster.

## Milestones

| # | Milestone | Done when |
|---|---|---|
| 0 | Recon — **mostly done, see tech-stack.md** | Remaining: RS streaming price asked (sales@raspberryshake.org) and NSSN contacted; IU.LSA/GSN openness checked from your laptop; USGS/EMSC first-solution latency measured over a week; Sentinel false-positive baseline computed from the 5-week BIPAD archive (how often do stations go silent innocently?) |
| 0.5 | **False-positive replay — do this before any production code** | Five-week BIPAD archive replayed: outage **episodes** (not missing samples) counted per station; thresholds tested at 20/30/40/60 min; every generated alert classified (isolated dropout / correlated dropout / genuine anomaly / known outage / indeterminate); result reported as **actionable alerts per recipient per week**. Gate: more than one unambiguously false actionable alert per recipient per 30 days kills the hazard channel as designed |
| 1 | Replay gate | Classifier passes/fails the three reference events + 20 earthquake controls; decision logged either way |
| 2 | Sentinel live (private) | Polling Nepal gauges, dead-man + rate alarms firing to you and Greg only, two weeks of false-alarm stats |
| 3 | Watcher live (private) | Event-feed trigger + auto waveform pull + classification running continuously, alerts to you and Greg |
| 4 | First institutional conversation | Greg's DHM/ICIMOD contact sees a live demo with real stats, not a pitch |
| 5 | MoU + recipients switched | Alerts flow to DHM/NDRRMA under a written arrangement; repo opened |

Between milestones 3 and 4 the system just runs and accumulates a track record — that record, not the code, is what earns the meeting.

## Facts that could change the plan (Greg is tracking these)

Where people actually died (Nepal is DNA-tracing bodies carried downstream; result in ~2 weeks — if deaths were overwhelmingly downstream comprehension failures, the priority tilts toward the drill/safe-haven work and these tools become secondary). The DHM cadence answer. The replay gate result. Whether ICIMOD or the Cook group says someone already builds this — in which case we join them instead; the mission is the outcome, not our authorship.
