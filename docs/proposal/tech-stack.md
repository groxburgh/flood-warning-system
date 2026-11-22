# Recon Report: Data & Tooling for "Station Sentinel" and "Mass-Movement Watcher"
**Bhote Koshi / Trishuli corridor, Nepal — prepared 28 August 2026**

Every claim below carries one of three labels:
- **VERIFIED-BY-FETCH** — fetched and seen.
- **DOCUMENTED** — a credible page describes it, but it could not be exercised.
- **INFERRED** — judgment or arithmetic derived from verified facts.

Access constraints that shaped this recon: several key hosts — **service.iris.edu, service.earthscope.org, docs.obspy.org, daq.hydrology.gov.np, eida-federator.ethz.ch** — refused automated fetch (robots.txt/TLS). Those failures are recorded inline; they are *this environment's* limits, not necessarily yours. A browser or curl from your own laptop will very likely reach all of them.

---

## 1. Nepal Hydrology Data — the Sentinel's feed

### 1.1 The headline

**The Sentinel can be built on fully public, unauthenticated data, at 10-minute cadence, today.** This was the single biggest unknown and it resolves favourably — but not via the source you expected.

### 1.2 What failed

- `https://hydrology.gov.np/` — **VERIFIED-BY-FETCH (as a failure).** A client-side JavaScript SPA; no station data, no timestamps in served HTML. Not scrapeable without a headless browser.
- `https://hydrology.gov.np/api/v1/` — HTTP 404.
- `https://daq.hydrology.gov.np/` — JS shell ("DHM | Data Management System"); DHM's internal data-acquisition system; API root unknown.
- `https://bipad.gov.np/` — 302 redirect to `https://ndrrma.gov.np/`, itself a JS shell.

### 1.3 What works: the BIPAD portal REST API

`https://bipadportal.gov.np/api/v1/` — **VERIFIED-BY-FETCH.** A live, publicly browsable Django REST Framework API root. **No authentication, no API key, no referer check.** It lists **165 endpoints**, including `river`, `river-stations`, `rain`, `rain-stations`, `earthquake`, `flood-station`, `station-location`, `streamflow`, `alert`, `incident`, `hazard`.

Every river record carries `"dataSource": "hydrology.gov.np"` — **VERIFIED-BY-FETCH.** BIPAD is mirroring DHM. **This is the route to DHM telemetry without DHM cooperation.**

**Two endpoints matter:**

**`/api/v1/river/`** — append-only **time series**, one row per station per 10-minute interval. **VERIFIED-BY-FETCH.** A full record:

```json
{"id":24226146,"createdOn":"2026-07-23T09:05:10.021345+05:45",
 "modifiedOn":"2026-07-23T09:05:10.021348+05:45",
 "title":"Langtang Khola at Shyaprubesi","basin":"Narayani",
 "point":{"type":"Point","coordinates":[85.34611111,28.16222222]},
 "waterLevel":2.93400001526,
 "image":"http://daq.hydrology.gov.np/images/9656ba736c6d3c61c56673d3e4c3b23a",
 "dangerLevel":null,"warningLevel":3.75,
 "waterLevelOn":"2026-07-23T08:50:00+05:45",
 "status":"BELOW WARNING LEVEL","elevation":1484,"steady":"STEADY",
 "description":"Hydrological Station with RLS","stationSeriesId":2788,
 "dataSource":"hydrology.gov.np","dataSourceId":null,
 "ward":1429,"municipality":29001,"district":23,"province":3,"station":49}
```

**`/api/v1/river-stations/`** — the **station registry**, one row per physical station carrying its most recent reading. Highest observed `id` is 281, so ~280 stations nationally (**INFERRED** — ids may have gaps).

### 1.4 Query mechanics — verified quirks

- **`count` is useless:** every response returns `"count": 9223372036854775807` (2^63−1). Paginate by `limit`/`offset` or by `id`.
- **`ordering=-id` WORKS** — the critical discovery.
- **`ordering=-createdOn` and `ordering=-waterLevelOn` are silently IGNORED** — they return oldest-first. A naive poller built on these would read five-week-old data and never know.
- **Date filters silently IGNORED** (`?waterLevelOn__gt=...` returned July records). No server-side time filtering.
- **`search=` WORKS** against station title (`?search=Trishuli`, `?search=Bhote`, `?search=Dhunche`).
- **`district=` WORKS** on `river-stations` (`?district=23` → exactly 6 Rasuwa stations).
- **Retention:** default page starts 2026-07-23; newest id 25009598 / 2026-08-29 — roughly a **5-week rolling archive** (**INFERRED**), enough to bootstrap baselines.

### 1.5 Freshness — measured, not assumed

Newest record at fetch time: **`waterLevelOn: 2026-08-29T05:10:00+05:45`** — i.e. *now*. The feed is genuinely live. **VERIFIED-BY-FETCH.**

Ingest lag from `waterLevelOn` vs `createdOn` pairs — **VERIFIED-BY-FETCH**:

| Station | waterLevelOn | createdOn | lag |
|---|---|---|---|
| Trishuli at Betrawati | 09:00 | 09:05:19 | 5 min |
| Trishuli at Betrawati | 09:10 | 09:15:10 | 5 min |
| Trishuli at Betrawati | 09:20 | 09:35:10 | 15 min |
| Trishuli at Galchi | 05:10 | 05:25:10 | 15 min |

**INFERRED:** BIPAD ingests on a 10-minute cron firing at HH:x5:10. Sensor-to-API visibility is **5–15 minutes**; your poller adds its own interval. A 3-minute end-to-end hydrological alert is **impossible** on this feed; **10–25 minutes is the realistic floor.**

### 1.6 The corridor — full inventory and a validated flood signature

`?district=23` (Rasuwa) returns **exactly 6 stations** — **VERIFIED-BY-FETCH**:

| Station | Lon, Lat | Warn | Danger | Last reading (NPT) |
|---|---|---|---|---|
| Bhotekoshi at Rasuwagadi | 85.3776, 28.2713 | 6.0 | 7.0 | **2026-08-26 08:40** |
| Bhote Koshi at Shyaprubesi | 85.3426, 28.1707 | 5.5 | — | **2026-08-26 08:50** |
| Langtang Khola at Shyaprubesi | 85.3461, 28.1622 | 3.75 | — | **2026-08-26 08:50** |
| Phalakhu Khola at Betrawati | 85.1858, 27.9743 | 2.6 | 3.1 | **2026-08-26 09:20** |
| Trishuli Khola at Dhunche | 85.3186, 28.0982 | 3.2 | — | 2026-08-29 05:20 (live) |
| Langtang River at Ghodatalbela | 85.4581, 28.1993 | 3.0 | — | **2026-08-04 19:20** |

Plus via search: Trishuli at Betrawati (warn 4.1, danger 5.0) **last reported 2026-08-26 09:20**; Trishuli at Galchi, Furke Khola (Malekhu), Bhorle, Kali Khola, Tadi Khola at Rautar remain live.

**This is the product demo, and it is real.** The gauges died in strict downstream order — 08:40 Rasuwagadi (border), 08:50 both Syabrubesi gauges (~12.6 km downstream), 09:20 both Betrawati gauges (~25 km further) — while Dhunche, on a sub-catchment *outside* the flood path, never stopped. **INFERRED:** front speed ~75 km/h Rasuwagadi→Syabrubesi, 50–70 km/h Syabrubesi→Betrawati. A "two consecutive missed 10-minute samples" rule on Rasuwagadi, given the 5–15 min ingest lag, would have fired at roughly **09:05–09:15 NPT — before or as Betrawati was being destroyed**, and 30–60+ minutes before the surge reached Galchi and the settlements below.

**Also note Ghodatalbela: silent since 4 August — three weeks before the disaster, apparently unnoticed.** A silent-station monitor has standing value independent of floods: it is a network-health product as much as a warning product.

Caution — **INFERRED**: silence is ambiguous (power cuts, telemetry faults, monsoon damage). The false-positive rate is an empirical question answerable immediately from the 5 weeks of retained history plus BIPAD's `alert`/`incident` endpoints. Answer it before promising anything to an institution. Also: both Syabrubesi and Betrawati read **BELOW WARNING LEVEL** on their final samples — a threshold-only monitor would have said nothing. **Silence, not level, was the signal.**

### 1.7 Verdict

**Sentinel is buildable on public data alone, no DHM cooperation required, at 10-minute cadence with 5–15 minutes of ingest lag.** DHM cooperation would buy lower latency (direct DAQ), an SLA, and authority. Pursue it as a *second* step, from a working demo built on BIPAD.

---

## 2. Real-Time Seismic Access — the Watcher's feed

### 2.1 Station inventory

**Failed (robots.txt):** IRIS and EarthScope station services — **IU.LSA (Lhasa) status unknown to this recon; verify from your own machine** (one request).

**GEOFON FDSN station service worked** — **VERIFIED-BY-FETCH:** within 3° of 28.28N, 85.52E: 23 stations, of which 22 are the *terminated* XN post-Gorkha temporary network (2015–2020) and one is IO.EVN (EvK2CNR Pyramid Laboratory, Everest, 5010 m, open-ended). Within 8° with `endafter=2026-08-01`: **1 station — IO.EVN.** GEOFON's ~300-station open real-time feed contains essentially nothing near the corridor (caveat: GEOFON archive ≠ global federated view).

**Raspberry Shake FDSN worked and is the good news** — **VERIFIED-BY-FETCH**, maxradius 2.5°, endafter 2026-08-25: **59 currently registered AM-network stations.** The relevant ones:

- **`AM.R9445` — 28.018, 85.520, 2518 m — ~29 km south of Langtang, directly on the corridor.** The single most valuable station for the Watcher. Online since Nov 2024.
- `AM.R3B1E`, `AM.R3C0B` at 27.83, 85.57 (~50 km, since May 2026); `AM.R14FA`, `R9D38`, `RBCBE` at 28.0, 84.99 (~57 km west); a dense Kathmandu Valley cluster at ~70–80 km.

**INFERRED:** coordinates are quantised (~1 km privacy fuzzing) — fine for detection, a problem for precise back-azimuth.

**Context — DOCUMENTED** (raspberryshake.org/earthquake-monitoring-in-nepal/): these are largely the **Nepal School Seismology Network (NSSN)**, run under "Seismology at School in Nepal" (seismoschoolnp.org) — 1 pilot station to 21 by 2019, 33 by end-2022; in a year-long study the Shakes detected 273 earthquakes, 250 matching the national catalog, down to M0.8; <$1,000/station vs up to $25,000 professional.

### 2.2 The blocker

**`manual.raspberryshake.org/fdsn.html` — VERIFIED-BY-FETCH:** the public FDSN service serves data "**T minus 30 minutes and older**." Real-time streaming (SeedLink/CAPS) requires contacting **sales@raspberryshake.org** — no published price. Rate limits: 5 req/s, 30 req/min, throttle after 200 MB, max 24 h per request.

**This is the product-defining constraint. A ~3-minute alert on RS public FDSN is impossible.** Options:

1. **Buy RS real-time streaming** — unknown cost; one email to find out. The highest-value unknown in this report.
2. **Partner with NSSN / seismoschoolnp.org** — each Shake emits a local UDP datacast and runs its own LAN SeedLink server (**DOCUMENTED**); a handful of cooperating schools gives real-time for free. A relationships problem, not an engineering one.
3. **GEOFON's open SeedLink** (geofon.gfz.de:18000, no permission required — **VERIFIED-BY-FETCH**) — nearest useful station 600+ km; teleseismic context only.
4. **Reframe honestly** as rapid post-event characterisation at T+35–40 min rather than warning.

**Recommendation (INFERRED): build on public FDSN at T+30 first.** The signal-processing, feature-extraction, classification and alerting code is *identical* whether the waveform arrives 30 minutes late or 30 seconds late. Validate the discriminator against the 26 August event on archived data; swap the ingest layer when a real-time agreement exists. Do not let the streaming negotiation block the science.

### 2.3 SeedLink, when you get there

- **geofon.gfz.de:18000** — ~300 stations, openly available, "no special permission required." **VERIFIED-BY-FETCH.** No latency figures stated.
- **Protocol** (docs.fdsn.org) — **VERIFIED-BY-FETCH:** TCP 18000 (18500 TLS); 64-bit sequence numbers allow a client to crash, restart, and resume without data loss — the operationally important property.
- **Do not quote a SeedLink latency figure to anyone until you measure it yourself.** None is documented.

### 2.4 Event feeds (the veto channel)

- **USGS** GeoJSON feeds — hour/day/week/month × magnitude tiers, "updated every minute." **VERIFIED-BY-FETCH.** No documented first-solution latency for M4+ Asia — unknown; measure it.
- **EMSC** — WebSocket at `wss://www.seismicportal.eu/standing_order/websocket`, JSON on event insert/update, Python client examples. **VERIFIED-BY-FETCH.** No latency figure given.
- **GEOFON eqinfo** — fdsnws-event, QuakeML, RSS; automatic solutions flagged as potentially erroneous. **VERIFIED-BY-FETCH.**
- **BIPAD's earthquake endpoint is DEAD** — newest event Aug 2025, over a year stale. **VERIFIED-BY-FETCH.** Do not use.
- **Nepal NEMRC** (seismonepal.gov.np) — HTML tables only, no API/RSS advertised. **VERIFIED-BY-FETCH.**

**INFERRED:** use USGS + EMSC purely as a *veto channel* — "a catalogued earthquake occurred at this time" is the negative evidence that suppresses a false mass-movement alert. Cheap, high-value, no agreement needed.

---

## 3. Prior-Art Software — adopt vs build

- **SeisComP** — AGPL, observatory-scale, earthquake-shaped (impulsive P/S assumptions your target signals violate). **INFERRED: overkill and a licensing trap.** Reject.
- **ObsPy** — **v1.5.0, 13 March 2026, LGPL v3, actively maintained** (**VERIFIED-BY-FETCH**, github.com/obspy/obspy). The right base. RS FDSN shortcut `Client('RASPISHAKE')` confirmed in RS docs.
- **SeisBench** — unified API for deep-learning seismology; pretrained PhaseNet/EQTransformer etc. **Nothing in SeisBench does non-earthquake source classification.** (**VERIFIED-BY-FETCH**, seisbench.readthedocs.io.) **INFERRED — adopt it inverted:** run PhaseNet as a **negative detector**. A confident P-and-S pick pair with normal moveout says "earthquake, suppress." Absence of clean picks + long duration + emergent onset is your positive evidence. You get a well-tested earthquake discriminator free and build only the positive side.
- **Discrimination prior art** — **DOCUMENTED:** random-forest landslide-vs-earthquake discrimination literature exists (e.g. "Towards Automatic Landslide-Quake Identification Using a Random Forest Classifier," doi 10.3390/app10113670; icequake discrimination in Alaska; rockfall mass/velocity from seismic waves, ESurf 12:641, 2024). **VERIFIED-BY-FETCH as reusable code:** github.com/smousavi05/Seismic-Features-For-Machine-Learning (feature extraction from continuous seismic signals). No maintained ready-to-run landslide-discrimination repo located — implement the published feature definitions yourself.
- **Labelled data — the genuinely reusable asset:**
  - **ESEC (Exotic Seismic Events Catalog)** — 113 events: flows/lahars/debris flows/outburst floods (17), rock/debris falls (23), rock/ice/debris avalanches and slides (68), snow avalanches (5). DOI 10.1785/0220180402, hosted at IRIS. **VERIFIED-BY-FETCH** (USGS publication page).
  - **USGS Seismogenic Landslides and other Mass Movements v3.0 (May 2025)** — DOI **10.5066/P90VGCSK**, **CC0 public domain**, with locations, volumes, runouts, seismic detection info. **VERIFIED-BY-FETCH.**
  - **INFERRED:** 113 positive events is small for deep learning but ample for a feature-based classifier — which is why random forests dominate this literature. Do not train a neural network from scratch.

---

## 4. Alert Delivery and Formats

- **Telegram Bot API** — **VERIFIED-BY-FETCH:** 1 msg/s per chat, 20/min per group, ~30/s broadcast free tier. No delivery SLA documented — never the only channel.
- **CAP v1.2** — **VERIFIED-BY-FETCH** (OASIS standard, 1 July 2010): required alert elements `identifier, sender, sent, status, msgType, scope`; required info elements `category, event, urgency, severity, certainty`; msgType enum includes **Update, Cancel** — a principled retraction path for the false positives you will certainly emit; certainty enum (`Observed/Likely/Possible/...`) lets you say "a gauge went silent" (`Possible`) without saying "a flood is coming" (`Observed`) — the honest distinction the silence detector actually supports. **INFERRED, strongly: emit CAP XML from commit one.** It costs an afternoon and makes you adoptable by the institutional pipeline Nepal's EW4All work already speaks.
- **SMTP** — the redundant channel; use a transactional provider.
- **Healthchecks.io-style dead-man watchdog** — ping on every successful poll cycle, both nodes; self-hostable. **VERIFIED-BY-FETCH** (docs). **A monitor whose own death is silent is worse than no monitor — it manufactures false confidence. Non-negotiable.**

---

## 5. Hosting and Runtime (INFERRED — engineering judgment on verified facts)

**Placement:** ingest latency is dominated by the 5–15 min BIPAD lag and the 30-min RS embargo — network RTT is noise. Host wherever is cheap and reliable (a ~$5/mo Hetzner or DigitalOcean box). **Do not host in Nepal** — you would sit inside the failure domain of the disaster you are warning about; geographic separation is a feature.

**Redundancy for a 1–3 person team:** skip leader election. **Run two identical instances in different regions and providers** (e.g. Hetzner EU + DigitalOcean Bangalore), both polling, both computing, deduplicating at delivery on a deterministic key like `sha256(product|station|event_type|triggering_sample_timestamp)`. The failure mode of a split brain is a doubled alert; the failure mode of a failed election is silence. For a warning system, duplicate-and-dedupe wins.

**Python 3.11+ / ObsPy / SQLite (WAL):** correct. Sentinel state is ~280 stations × 6 samples/hr ≈ 40k rows/day — trivial; single-file storage makes backup and forensic replay a `cp`. Each node's DB is local state, not shared truth. Waveforms as flat MiniSEED on disk, not in the database.

---

## RECOMMENDED STACK

**Ingest.** *Sentinel:* poll `https://bipadportal.gov.np/api/v1/river-stations/?format=json&limit=300` every 5 minutes (registry rows carry `waterLevelOn` — silence detection is a timestamp comparison, no per-station queries); `/api/v1/river/?ordering=-id` for time series and rate-of-rise. **Hard rule: `ordering=-id` only; never trust `-createdOn`, `-waterLevelOn`, or date filters (all silently ignored); assert freshness every poll.** *Watcher:* ObsPy FDSN against `data.raspberryshake.org` accepting T+30 (stations AM.R9445, R3B1E/R3C0B, the Kathmandu cluster as an array); migrate to SeedLink when a real-time agreement exists.

**Processing.** Python 3.11+, ObsPy 1.5.0. Sentinel: silence age + rate-of-rise + a **correlated-silence rule** (≥2 adjacent stations in one basin quiet within 30 min) — that rule alone fires on the 26 August signature. Watcher: SeisBench PhaseNet as negative detector + hand-built random forest on duration/emergence/spectral features, trained on ESEC + USGS CC0 catalog, with USGS/EMSC catalogue veto.

**Storage.** SQLite (WAL) per node; flat MiniSEED for waveforms.

**Alerting.** CAP v1.2 XML as the canonical artefact, rendered to Telegram + SMTP; deterministic dedupe; `Cancel`/`Update` for retraction; `certainty: Possible` for silence-only triggers.

**Hosting.** Two ~$5/mo VPS, different providers/regions, systemd, healthchecks dead-man on both.

**Adopt:** ObsPy, SeisBench (inverted), ESEC + USGS catalogs, CAP v1.2, healthchecks, BIPAD API, smousavi05 features. **Build:** the positive-side discriminator, silence/correlated-silence logic, CAP emitter, dedupe. **Reject:** SeisComP, BIPAD's dead earthquake endpoint, leader election.

**The single most important remaining unknown: the price and terms of Raspberry Shake real-time streaming — and whether NSSN/seismoschoolnp.org would grant direct school-station access for free.** Two emails settle it; the answer determines whether the Watcher is a ~3-minute product or a T+35-minute one. (Second-order unknowns: empirical false-positive rate of gauge silence — measurable today from the 5-week BIPAD archive; IU.LSA and GSN station openness near the corridor — one request from your own laptop.)

---

## Sources

**Fetched successfully:** bipadportal.gov.np/api/v1/ (root, river, river-stations, earthquake — multiple parameterized queries); geofon.gfz.de fdsnws station queries, waveform/seedlink.php, eqinfo; data.raspberryshake.org fdsnws station queries; manual.raspberryshake.org (fdsn, download, developersCorner, root); raspberryshake.org/earthquake-monitoring-in-nepal/ and /data-center/; earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php; seismicportal.eu/realtime.html; seismonepal.gov.np; seiscomp.de; github.com/obspy/obspy; seisbench.readthedocs.io (root + models); usgs.gov ESEC publication page; usgs.gov seismogenic mass movements dataset page; docs.oasis-open.org CAP-v1.2-os.html; core.telegram.org/bots/faq; healthchecks.io/docs; docs.fdsn.org SeedLink protocol; daq.hydrology.gov.np (title only).

**Failed fetches:** hydrology.gov.np (JS shell), hydrology.gov.np/api/v1/ (404), bipad.gov.np (302→ndrrma.gov.np JS shell), service.iris.edu + service.earthscope.org + docs.obspy.org (robots), eida-federator.ethz.ch (TLS), bipadportal.gov.np/api/v1/realtime-river/ (404).

**Search-derived (not individually fetched):** github.com/smousavi05/Seismic-Features-For-Machine-Learning; doi 10.3390/app10113670; esurf.copernicus.org/articles/12/641/2024; arxiv.org 2510.23795; sciencebase.gov 68221c34d4be02673d76ba1d; ds.iris.edu SeedLink node page.
