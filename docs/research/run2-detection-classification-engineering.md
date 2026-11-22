# Minimum Credible Detection Architecture for Rock–Ice Collapse Cascades in the Upper Bhote Koshi

**Deep-research run · 28 August 2026 · Anchored on the 26 August 2026 Langtang Lirung / Lhende Khola / Bhote Koshi disaster**

---

## 0. Headline finding

There are **two different problems** in this corridor, and conflating them is the main analytical error available.

- **Syabrubesi (~14 km, ~10 minutes)** is a seconds-to-minutes geophysics problem. Only a source-side trigger — seismic — can act inside that window. No satellite, no gauge, no human loop can.
- **The Trishuli towns (Betrawati, Bidur/Trishuli Bazaar, Devighat, Galchhi, Malekhu, Gaidakot)** had **hours**. The flood took **6 h 50 min** from Rasuwagadhi to Gaidakot, arriving 15:30 (*Nepalnews, 27 Aug 2026*). They were not failed by detection physics. They were failed by the destruction of the four in-corridor gauges and by a dissemination and authority chain that could not convert a known upstream event into a downstream evacuation.

Against the hard rule — *what caused an operational warning before a comparable destructive event* — the honest scoreboard is short. **Regional seismic networks have never issued an operational public warning before a destructive rock–ice avalanche cascade anywhere.** Satellite has never issued a days-ahead operational instability warning anywhere. Only three classes have a real record: in-torrent geophone/AFM alarm systems, lake-outlet tripwire systems, and slope-mounted GNSS/radar on *already-identified* slopes.

A note on the public timeline: the record as of today is internally inconsistent. The collapse seismic signal is timed at **08:37 NPT (02:52:10 UTC)** (*EarthSky, 27 Aug 2026*), yet DHM reports the flood crossing into Nepal at **08:40** (*Nepalnews, 27 Aug 2026*). A 3-minute interval is not compatible with a form-and-breach damming cascade. USGS records **a second seismic event ~3 hours later, energy equivalent to M4.2** (*USGS Landslide Hazards Program, 27 Aug 2026*), which is the more plausible breach signature. **The damming interval is currently unknown**, and every lead-time number below is stated as a function of it.

---

## 1. Capability matrix — judged on operational record

| Method | P(detect ≤60/120/180 s) | Classification latency + accuracy | Localization | False alarm | Miss | Survivability in-event | Capex / Opex | Maintenance | **Has it ever caused an operational warning?** |
|---|---|---|---|---|---|---|---|---|---|
| **Regional broadband seismic (50–150 km)** | Signal present <30 s; automated *assessment* demonstrated at **~3 min** (Alaska) | ~3 min, volumes ≥0.5 Mm³; admitted false triggers from regional/teleseismic events | **<5 km** with good geometry; "considerable error" where <few stations within 2° | Not quantified | Not quantified | High (stations outside corridor) | ShakeAlert reference: **$39.4M capex / $28.6M-yr opex** (US West Coast) | Low per station | **No.** Alaska prototype notifies *scientists*, not the public (*Alaska Beacon, 12 Sep 2025*) |
| **Local source-side geophone (≤10 km)** | High (immediate on arrival) | Amplitude + **duration discrimination**: collapses = continuous minutes; Mw 5.6 quake ≈1 min | Implicit (single catchment) | **3 false in 12 triggers** (25%), May–Dec 2022 | 0 of 3 major chain events missed | Station destroyed once by debris flow (Mar 2021), rebuilt higher | "Low-cost"; helicopter deployment | High; monsoon cloud starves solar | **Yes — Sedongpu Valley EWS, Tibet**: 3 major chain events + 7 small events warned (*Yang et al., NHESS 23:3015–3029, 2023*) |
| **In-torrent geophone alarm (Alpine debris flow)** | High, but only when flow reaches the sensor | Immediate; threshold-based | Sensor location = location | **1 false in 20 automated alerts** | Not stated | Sensor sits in the flow path | Geophones ~10² €, stage sensors ~10³ €, Doppler radar ~10⁴ € (equipment only) | High (abrasion, burial) | **Yes — Illgraben**: 3 debris flows + 16 flood flows, **5–15 min** warning (*Badoux et al., Natural Hazards, 2009*) |
| **Lake-outlet tripwire + geophone + stage (ERLAWS, Ruapehu)** | High | Immediate, multi-sensor concurrence | Fixed | Not published | 0 for the design event | Sensors in the outlet | Not published | Moderate | **Yes — 18 Mar 2007 dam-break lahar**, activated 10:47, "worked as planned," up to **2 h** to Tangiwai (*GNS/ERLAWS record*) |
| **Volcano lahar AFM (Mount Rainier)** | Original: ≥4 min delay; modernized: real-time | Multi-instrument rejection of eruption/earthquake signals | Fixed stations | No published record | No published record | Valley-floor sensors | >40 stations planned | Moderate | **No confirmed real lahar detection found.** Designed for 5 min (in park) to 15–60 min downstream (*USGS; Moran, SSA, 2 May 2024*) |
| **Infrasound arrays** | Only for large, near events | POD **~80%** for large avalanches within 3–4 km; **only 3% of all observed avalanches** auto-detected | Back-azimuth; range-limited | **FAR 10–30%**; only 22% of auto-detections confirmed | Very high overall | Good (ridge sites) | Moderate | High (wind noise, snow) | **No** (*Mayer et al., ISSW 2018*) |
| **Seismic mini-arrays (7 elements, ~300 m aperture)** | 12/13 avalanches detected on a validated window | 117 raw detections → 21 retained (82% rejection); MUSIC at 3× real time | Detection range only **2–3 km** for weak signals | Not quantifiable | Not quantifiable | Good | Moderate | High | **No** (*Heck et al., Earth Surface Dynamics 7:491, 2019*) |
| **GNSS + crack gauge + tiltmeter on a known slope** | n/a (precursor mode) | Days-to-hours; threshold + inverse velocity | Exact | Not published; 5 consecutive successes claimed | n/a | n/a (pre-event) | Moderate | High at altitude | **Yes — Guizhou, 17 Feb 2019**: **53 min**, >400 evacuated, 5th success since 2017 (*SKLGP, Landslides, 2019*) |
| **GB-InSAR / Doppler radar (Brienz, Blatten)** | n/a (precursor + event-confirmation) | Creep: mm accuracy, 2 min–3 h scans. Doppler: traffic lights red **"within seconds"** | Exact | **No false alarms** at Brienz | 0 | Solar + methanol fuel cell, mobile backhaul | Not published | Moderate; road/heli access assumed | **Yes — Brienz/Brinzauls** staged evacuation 5–12 May 2023 before the 15 June collapse (*Loew et al., Landslides, 2024*) |
| **Spaceborne SAR (Sentinel-1, ICEYE, ALOS-2/SAOCOM)** | n/a | Days–months | Exact | n/a | Chamoli: precursors visible 5 yrs, **"could likely not have been forecast from satellite data alone"** | Full | Sentinel free; ICEYE commercial | None | **No days-ahead operational warning found anywhere.** Blatten (L-band 2016–2024) and Brienz (ICEYE, 1.6 d mean revisit, RMSE 0.08 m) both **retrospective** |
| **River stage gauges in corridor** | n/a — downstream of the hazard | n/a | n/a | Low | n/a | **Destroyed.** All four swept away 26 Aug 2026 | Low | Moderate | **Yes, for slow floods** (Nepal EWS: 30 min–6 h). **No** for this class |
| **DAS on fibre** | Research only | Research only | Metre-scale along fibre | Unknown | Unknown | Fibre in corridor dies with the corridor | Interrogator high | Low | **No** |

---

## 2. Question-by-question

### Q1–Q2. Detection and classification — the latency/accuracy trade is real and already resolved in the field

The 2026 event was catalogued by USGS as an **M4.4 earthquake** before being reclassified ("the seismic energy was instead generated by a landslide" — *EarthSky, 27 Aug 2026*); USGS later put the collapse at **M5.2-equivalent**. This is not a scandal — it is the expected behaviour of a global tectonic pipeline applied to a non-tectonic source.

**The classification problem is already solved in the operational literature, cheaply, using duration.** At Sedongpu, the discriminator is that a collapse produces a continuous waveform lasting **several minutes**, while a Mw 5.6 earthquake produced roughly **one minute** of signal. Over May–December 2022, that logic gave **12 triggers → 9 confirmed debris flows → 3 false positives**, one being the 10 Nov 2022 Mw 5.6 earthquake. That is ~25% over-warning at threshold — and it is the right answer to the latency/accuracy trade.

Concretely: a system that declares "mass movement, not earthquake" at **T+40–60 s** with ~75–85% precision is operationally superior to one that is 98% right at T+15 min, because at Syabrubesi 15 minutes *is* the entire event. **Correct-but-retrospective is failure**, and every regional-network result to date — Chamoli, Blatten, Bhote Koshi — is in that category.

**Physics ceiling on classification:** you cannot classify faster than the source radiates a distinguishing signal. The diagnostic for a rock–ice avalanche is emergent onset plus long, cigar-shaped, low-frequency-rich coda. **20–45 s of coda is a hard floor** for a confident non-tectonic call. Sub-20 s classification at high confidence is not an engineering gap; it is a physical one. What *can* be compressed to <10 s is a **presumptive** trigger — "large non-impulsive source in catchment X" — which is what a source-side geophone at ≤10 km delivers.

### Q3. Localization — narrowing to the catchment is what makes the alert actionable

Published anchors:
- **Back-projection**: ~2 km uncertainty, preliminary result in **<5 min**, 20–30 km interstation spacing (*Lee, Liao, Chen & Mu, Geofluids 2019*).
- **Coastal Alaska**: **<5 km** absolute error where coverage is good (Barry Arm); "considerable relative error" where few stations within 2° (*The Seismic Record 4(1):43, 2024*).
- **Dam-formation "D-phase"**: only observable at **source–receiver distance ≤40 km** (*Chao et al., Scientific Reports 6:19259, 2016*).

Does narrowing from "somewhere in a 50 km zone" to "this catchment" in 60–90 s change what can be alerted? **Yes, decisively.** A 50 km-radius uncertainty spans the Bhote Koshi, the Langtang Khola, and the Trishuli headwaters — you cannot tell which valley to evacuate, so the only defensible action is to alert everyone, every time, which destroys the alert's credibility within a season. Catchment-level resolution converts a regional advisory into "clear the Bhote Koshi channel now."

**Required geometry:** three to four stations within **20–40 km** of the source with usable azimuthal spread. The source sits at ~5,000 m near/beyond the Nepal–China border, so Nepali stations alone occupy a half-space and the location smears along the source–receiver azimuth. Two mitigations without Chinese cooperation:
1. **Mini-arrays** (7 elements, ~300 m aperture) give **back-azimuth from a single site**; two arrays 15–30 km apart on the Nepali flank triangulate. Months of work, low six figures.
2. **Ridge-top stations on the Nepali side of the divide** (Langtang, Gosainkunda, Kyirong-facing spurs) at 3,500–4,500 m, helicopter-placed.

Nepal's National Earthquake Monitoring and Research Center operates **42 seismic stations, 50 GPS stations and 36 accelerometers** nationwide — adequate for a national tectonic catalogue, not for 60-second catchment-scale mass-movement localization on the northern border.

### Q4. Cascade-transition signals — the most under-exploited channel, and it is cheap

| Transition | Signal | Operationally exploited? |
|---|---|---|
| Collapse → impact | High-amplitude, long-duration seismic; **M5.2-equivalent** on 26 Aug 2026 | Yes — Sedongpu geophones |
| Runout → river blockage | **"D-phase"**: strong late-arriving high-frequency phase when mass hits the channel. Compute "a few seconds on a desktop." Requires stations **≤40 km** | Method published, real-time-capable; **no operational deployment found** |
| Damming | **Anomalous downstream stage drop**; upstream impoundment rise. Sedongpu used water-level thresholds of **20/25/30 cm per 10 min** at Gyala, 6 km upstream of the outlet | Yes — Sedongpu; also the classic GLOF stage signature |
| Breach | Second seismic event (**M4.2-equivalent, ~3 h later**, 26 Aug 2026); rapid stage rise | **No.** Not exploited anywhere operationally for this class |

The damming/breach interval is the single largest free lead-time reservoir in this corridor, and the 26 August event demonstrates both its existence and the total failure to use it: the second (breach-consistent) seismic event was recorded, and China's notification of the *residual* 0.11 km² lake 18 km upstream of Rasuwagadhi reached Nepal on **27 August via the Ministry of Foreign Affairs**, a day later (*ANI, 27 Aug 2026*).

**A downstream stage-drop detector is close to free.** It reuses gauges already funded. Its weakness is exactly what killed it here: it must be *below* the dam and is therefore in the flood corridor.

### Q5. Satellite — decompose the pipeline, not the revisit

| Stage | Sentinel-1/2 | Landsat | Commercial SAR (ICEYE / Capella) |
|---|---|---|---|
| Tasking | None — fixed plan | None | ICEYE: late tasking to **40 min before pass** (vendor-claimed) |
| Revisit | S1 6-day; S2 5-day, 2–3 day effective mid-latitude | 8–16 day | ICEYE "hourly revisit" (vendor-claimed); measured at Brienz: **mean 1.6 d, min 25 min, max 4 d** |
| Downlink + processing | S2 NTC **≤24 h** from sensing. S1 NRT tier values **not verified — unknown** | Hours–day | ICEYE: **<1 h** tasking-to-delivery, **<3 h** cloud SLA (all vendor-claimed) |
| Algorithm / analyst | Hours–days; InSAR coherence over glaciated north faces often fails | Days | Hours |
| Alert | Copernicus EMS Rapid Mapping: self-described **"hours–days"** | n/a | n/a |

**Is days-ahead operational instability warning demonstrated anywhere? No.** The three best-documented cases are all retrospective:
- **Blatten**: ALOS-2/SAOCOM L-band showed acceleration from ~50 cm/yr (2023) to **>150 cm/yr by Aug 2024**, nine months before failure — but the analysis was "conducted in the aftermath" (*ESA EO4Society / GAMMA MODULATE, 8 Aug 2025*).
- **Chamoli**: >10 m of motion over 5 years, headwall crack visible from March 2016 — yet **"InSAR would not have provided an adequate tool for monitoring in this case, even with knowledge of the location"**; timing "could likely not have been forecast from satellite data alone" (*NHESS 22:3309, 2022*).
- **Brienz**: ICEYE pixel-offset matched ground radar to RMSE 0.08 m — retrospective (*Manconi et al., NHESS 24:3833, 2024*).

**Verdict:** satellite today is (a) precursor *screening* to build the watchlist, (b) after-action mapping, and (c) — demonstrably operational — **post-collapse dam-and-lake detection**, which is how the residual lake was found on 27 August 2026 and how the 8 July 2025 source lake was attributed within 24 hours (*Stimson Center, 22 Jul 2025*). That third role is real, valuable, and hours-to-days, not minutes.

### Q6. In-situ source monitoring at 4,000–5,000 m

- **Peru, Laguna 513 (4,491 m)**: 2 cameras + 4 geophones at 5 s sampling, relay at 3,189 m, data centre at Carhuaz, siren station, all solar+battery. **Locals dismantled the lake station on 24 November 2016** during a drought, believing it suppressed rain. Peruvian law restricted evacuation authority to the mayor alone (*WMO Bulletin, Huggel et al., 23 Mar 2020*). The failure was social and legal, not technical.
- **Sedongpu (Tibet)**: helicopter-installed May 2022 at 3,308 m; Asiasat 7 backhaul; **solar + wind hybrid** because monsoon cloud starves solar alone; optical/thermal cameras useless above 6,000 m in cloud; **EWS2 destroyed by a debris flow in March 2021 and rebuilt higher**. Authors recommend weather-independent radar.
- **Cirenmaco (Nyalam, adjacent Poiqu sub-basin)**: lake level, moraine displacement, ice collapse, downstream runoff; **Beidou + Inmarsat + mobile** transmission (*Wang, Zhang, Yao & An, IJDRR 73, 2022*). CAS reports these Tibetan systems have "successfully issued seven early warnings," one at the China–Nepal border last year — **agency-claimed, unverified** (*SCMP, 27 Aug 2026*).
- **Bhutan / Central Asia (GLOFCA)**: pilots exist; "GLOF early warnings must act within minutes" acknowledged; **no sensor specs, costs or performance metrics published** on accessible pages. Unknown.
- **Nepal**: Tsho Rolpa and Imja have community-based systems; the GCF-approved programme (**$36.1M GCF + ~$14M co-finance, 7 years**, DHM lead, Koshi and Gandaki basins, 1 Jul 2025) funds four lake-lowerings and EWS expansion — **none aimed at rock–ice collapse sources, none on the Chinese side of the divide**.
- **UAV docks**: EUR **15,000–40,000**; twice-daily automated flights ran at Blatten May–Nov 2025; cm-level accuracy; ~15 m/s wind limit; need stable power and satellite internet (*Maschler et al., NHESS 26:3107, Jul 2026*). The one genuinely new option since Chamoli.

**Winter survivability and maintenance are the recurring killers**: Alaska lost its first Barry Arm seismometer to an avalanche in 2020–21; monthly summer maintenance plus winter visits required. Any Bhote Koshi design must assume one station loss per two to three years and budget replacement, not repair.

### Q7. Blatten property table — property by property, not by analogy

| Property | Blatten / Birch Glacier (May 2025) | Bhote Koshi (Aug 2026) | Transfers? |
|---|---|---|---|
| **Prolonged observable instability phase** | **Present.** Kleines Nesthorn moved "a few cm a year," accelerating to **several metres per day around 13 May**; collapse 28 May, 15:24 | **Unknown / not observed.** Nothing was watching this cliff | **No** |
| **Prior known hazard focus** | **Present.** The peak was already under continuous monitoring | **Partial.** Langtang Lirung produced a several-million-m³ debris avalanche in 2015 (USGS); 47 potentially dangerous glacial lakes catalogued for Koshi/Gandaki/Karnali (**25 in TAR China, 21 Nepal, 1 India**) — but **rock–ice cliffs are not on any watchlist**, and the 8 Jul 2025 source lake "was not being actively monitored" | **Partially** — the inventory concept transfers; its scope must change from lakes to slopes |
| **Road access for instruments** | **Present.** Valley road, helicopter, dense national infrastructure | **Absent.** Source at ~5,000 m, at/beyond an international border; helicopter-only; no Nepali legal access | **No** |
| **Monitoring density** | **High.** Cameras, GNSS, GB-InSAR, Doppler rockfall radar, SED national network, two UAV docks | **Low.** 42 national seismic stations; **four** corridor river gauges — all destroyed | **No** |
| **Escalating decision authority over days** | **Present.** *First alert raised by the local natural hazard observer.* Evacuation ordered 17–19 May, ~9 days ahead, ~300 residents; one death outside the zone | **Absent across the border.** Nepal's channel to Chinese information ran through the **Ministry of Foreign Affairs**, delivering the residual-lake warning on **27 August** — the day after | **Partially** — the domestic escalation ladder transfers; the cross-border half does not exist |
| **Warning window available** | ~**9 days** | ~**10 minutes** at Syabrubesi; hours at Trishuli towns | — |
| **Precedent for costly precaution** | Present — a village abandoned on a forecast | Untested at this scale | Transferable at cost |

**What transfers:** the staged monitoring ladder (cheap cameras/GNSS → GB-InSAR → Doppler radar as escalation); empowering a *local* observer to raise the first alarm; pre-agreed thresholds tied to pre-agreed actions; institutional willingness to evacuate on an uncertain forecast.

**What does not transfer:** every property depending on a multi-day precursor window and on the hazard source lying inside your own jurisdiction, reachable, already instrumented. Blatten is a *slow-onset, in-jurisdiction, pre-instrumented* success. Bhote Koshi was a *sudden-onset, out-of-jurisdiction, un-instrumented* event. **Importing the Blatten playbook wholesale would produce nothing. Importing its ladder and its authority design, coupled to a seismic trigger rather than a deformation trigger, would produce something.**

### Q8. Fusion — tested, and the answer is narrower than the literature claims

- **Same-stage concurrence logic: operationally proven, and it works.** ERLAWS combines geophones, tripwires and lake-level sensors and fired correctly on a real 1.29 Mm³ dam-break lahar. Rainier's modernization added instruments explicitly "to determine whether a seismic signal is really from a lahar, and not from an eruption or an earthquake" (*Moran, SSA, 2 May 2024*). Sedongpu's amplitude-plus-duration-plus-downstream-stage chain caught three cascades and rejected an Mw 5.6 earthquake. **This reduces false alarms. There is no evidence it reduces latency.**
- **Cross-stage fusion (seismic + satellite + gauges + weather): no operational evidence of improved latency.** The modalities run on incommensurable clocks — seismic in seconds, gauges in minutes, satellite in hours-to-days. Fusion produces a better *narrative* and a better *second-event* forecast — which is precisely what the 27 August NDRRMA advisory was. It does not compress the first alert.

**Conclusion: build fusion for confidence, not for speed. Do not let a fusion architecture delay the seismic trigger.**

### Q9. Robustness under post-impact infrastructure failure

The 26 August event is a complete field test of the failure model; treat it as the design specification:

- **Four telemetry gauges destroyed** (Rasuwa Bhote Koshi, Rasuwa Syabrubesi, Nuwakot Betrawati, Dhading Malekhu/Furke). The corridor's instruments died at the moment they became relevant.
- **40 km of road and 41 bridges destroyed in Rasuwa**; Prithvi Highway sections gone.
- **14 hydropower projects hit, >400 MW off the grid** — grid power in the corridor is not a survivable assumption.
- **Communication lines to several villages down.**

| Component | Survives? | Requirement |
|---|---|---|
| Source-side geophone/seismic on valley flank above runout | **Yes**, if sited above maximum credible runout — Sedongpu's EWS2 was destroyed once and moved uphill | Independent power, geographic separation from the channel |
| Ridge-top mini-arrays on the Nepali flank | **Yes** | Solar + wind hybrid; satellite backhaul |
| In-corridor river gauges | **No** — all four died | Pre-impact use only; expendable, duplicated on high banks |
| Terrestrial telecom / fibre / DAS | **No** | — |
| Grid power | **No** | Solar + battery + wind or methanol fuel cell (as at Brienz) |
| Cell broadcast to handsets | **Partial** — in-corridor towers fail; outside towers survive | Sirens as the in-corridor last resort |
| Satellite backhaul (Beidou / Inmarsat / Asiasat class) | **Yes** | Must be procured; Starlink licensing status in Nepal **unknown** |

**Design rule: nothing in the valley bottom is part of the warning chain. Everything load-bearing sits on the flank, runs on its own power, and talks to a satellite.**

---

## 3. Two minimum credible architectures

### Architecture A — "Source tripwire" (the minimum that is technically credible)

**Components**
1. **4–6 source-side seismic stations** on the Nepali flank of the Langtang/Kyirong divide, 3,500–4,500 m, helicopter-placed, within 10–25 km of the mapped priority sources.
2. **2 mini-arrays** (7 elements, ~300 m aperture) for single-site back-azimuth, 15–30 km apart.
3. **Duration-plus-amplitude classifier** on-station and at a national node: presumptive trigger at T+10–20 s, mass-movement declaration at T+40–60 s, catchment assignment at T+60–90 s.
4. **Two high-bank stage gauges** (Timure, Syabrubesi) on flood-proof mounts above the 2026 high-water mark, for stage-drop (damming) and stage-rise (breach) detection.
5. **Solar + wind + battery**, satellite backhaul.
6. **Dissemination**: hardwired sirens at Timure, Rasuwagadhi, Syabrubesi (automatic, no human in the loop for the source trigger); cell broadcast for the Trishuli corridor; pager/SMS to DHM, NDRRMA, hydropower operators and the Nepali Army.

**What it buys**
- **Syabrubesi**: alarm at T+60–90 s; siren immediate; **actionable time ≈ (damming interval D + ~10 min) − ~3 min**. If D≈0, ~7 minutes. If D = 60 min, ~67 minutes. This is the whole game, bounded by D, which is currently unknown.
- **Trishuli towns**: **1–6.5 hours** — the seismic trigger fires before the wave leaves the border zone. Gaidakot had 6 h 50 min in reality.

**Cost band (estimated; no single published price list exists for this configuration; ±50%):**
- Capex **US$1.5–4M** (helicopter emplacement dominates; assume 30–50% of hardware cost per station in logistics)
- Opex **US$300–600k/yr** (satellite airtime, two maintenance windows, one station replacement every 2–3 years, 24/7 duty desk)

### Architecture B — "Watched sources" (A, plus a prioritized live-view on the top 5–10 sources)

Adds: GB-InSAR or Doppler radar on the opposite flank (Brienz precedent: 2,500 m standoff, 2-minute scans, solar + methanol fuel cell); permanent GNSS + 42 MP time-lapse cameras with automated correlation; UAV docks (EUR 15–40k each, proven at Blatten May–Nov 2025); commercial SAR tasking retainer (ICEYE-class; vendor-claimed <1 h delivery) triggered by a seismic event or screening flag; automated Sentinel-1/2 + Landsat screening for the whole corridor.

**What it buys:** the possibility — unproven anywhere — of days-ahead warning for a *slow-onset* source. It does **not** improve the Syabrubesi number for a sudden collapse. It materially improves the second-pulse and residual-dam problem, which killed nobody on 26 August only by luck.

**Cost band (estimated):** capex **US$6–15M**; opex **US$1.5–3M/yr**. Scale reference: the GCF/UNDP Nepal glacial-flood programme is $36.1M + $14M over seven years across two entire basins; ShakeAlert cost $39.4M capex and $28.6M/yr for the US West Coast.

**Staged bill of materials and end-to-end latency budget (Architecture A):**

| Stage | Budget | Basis |
|---|---|---|
| Signal arrival at nearest station (≤25 km) | 4–9 s | P/S propagation |
| Presumptive trigger | +10–20 s | Amplitude threshold |
| Mass-movement classification | +40–60 s cumulative | Duration discrimination (Sedongpu) |
| Catchment assignment | +60–90 s cumulative | Array back-azimuth + ≥3-station location |
| Message generation + satellite hop | +5–20 s | Sedongpu/Cirenmaco backhaul |
| Siren activation (automatic) | +0–5 s | Brienz Doppler → traffic lights "within seconds" |
| Cell broadcast delivery | seconds; "unaffected by network congestion" (*WMO Bulletin, Gray et al., 15 Oct 2025*) | ~44 countries operational as of early 2025 |
| **Total alert latency** | **~90–130 s** | |
| Human comprehension + movement to high ground | 2–5 min | Budimir et al. survey evidence below |

---

## 4. Obstacles as costs

| Wall | What it would take to break or bypass | Interim workaround |
|---|---|---|
| **Source at/beyond the Chinese border; Nepal cannot instrument it** | Bilateral instrumentation MoU or joint station. Precedent: China already runs Sedongpu and Cirenmaco and has supplied Nepal with imagery and lake warnings. Actor: Nepal MoFA + China MWR/CAS. Cost: low. Time: 1–3 years, politically contingent | **Sensors on the Nepali flank only.** Seismic does not respect borders — a 20 km standoff still gives sub-2-minute detection |
| **Cross-border notification runs through foreign ministries (demonstrated latency ≈1 day)** | A standing 24/7 technical hotline DHM↔Tibet Hydrological Bureau with pre-agreed triggers. Cost: negligible. Time: months | Treat Chinese data as a *second-pulse* input only; never as the first alert |
| **In-corridor gauges die during the event** | Duplicate on high banks + satellite backhaul. ~$40–80k per site | Accept loss; use them for the pre-impact minutes only |
| **No cell broadcast in Nepal (SMS only, dispatched ~16–20 min after the flood crossed the border)** | Cell broadcast deployment. ~44 countries have it or are deploying. Actor: NTA + operators + NDRRMA. Cost: low-to-mid seven figures. Time: 12–24 months | Sirens in Rasuwa; SMS for the Trishuli corridor, which had hours |
| **Comprehension and trust** | Nepal's own evidence: **40% found EWS SMS "very hard to understand"; 46% "very unlikely to act"; only 21% "very likely to act"** (*Budimir et al., Geoscience Communication preprint, 2019*). Peru's Lake 513 station was **physically dismantled by residents**. Countermeasure: drills, local wardens, sustained engagement — the cheapest and most-skipped line item | Annual drills on the Rainier model; a paid local hazard observer per settlement, on the Blatten model |
| **False alarms at ~25% will erode credibility** | Tiered messaging (advisory/prepare/evacuate) as at Sedongpu and Nepal's existing three-code SMS scheme. Cost: negligible | Publish the false-alarm rate up front and drill on it |
| **Physics ceiling — precise** | **No system can warn Syabrubesi more than (damming interval + ~10 min) minus ~2 min ahead of impact if the trigger is the collapse.** With no damming interval the absolute ceiling is ~8 minutes. Classification below ~20 s of coda is not achievable at usable confidence. These are not budget problems | Move the ceiling by *shortening the reaction*, not the detection: pre-designated vertical evacuation points within 2–3 minutes' walk of every settlement |

---

## 5. Common schema — 17 variables (Architecture A, upper Bhote Koshi)

| # | Variable | Value | Evidence grade | Source |
|---|---|---|---|---|
| 1 | Cascade stage(s) addressed | Collapse; runout; river blockage; breach | Operationally demonstrated (Sedongpu, stages 1–3) | Yang et al., NHESS 23:3015, 2023 |
| 2 | Earliest observable signal | Multi-year slope deformation (Blatten: 50→>150 cm/yr; Chamoli: >10 m over 5 yrs) | Measured, retrospective only | ESA/GAMMA MODULATE 2025; NHESS 22:3309, 2022 |
| 3 | Earliest **operationally** detectable signal | Collapse seismic radiation, T+0 | Operationally demonstrated | Sedongpu EWS; USGS 27 Aug 2026 |
| 4 | Detection latency | 10–20 s presumptive (local geophone ≤25 km); ~3 min regional automated assessment | Operationally demonstrated (local); measured (regional) | *The Seismic Record* 4(1):43, 2024 |
| 5 | Classification latency + accuracy | 40–60 s; ~75% precision at threshold (9 true / 3 false in 12), 0 misses of major events | Operationally demonstrated | Yang et al., NHESS 2023 |
| 6 | Source location uncertainty | <5 km with good geometry; ~2 km back-projection at <5 min; **≤40 km station distance required for D-phase** | Measured | Seismic Record 2024; Geofluids 2019; Chao et al. 2016 |
| 7 | False alarm rate | ~25% at trigger threshold (Sedongpu); 1 in 20 (Illgraben); 10–30% (infrasound) | Measured / operationally demonstrated | Yang 2023; Badoux 2009; Mayer 2018 |
| 8 | Miss rate / P(detect ≤60/120/180 s) | Local source station: high at all three. Regional network alone: ~0 / low / ~0.5–0.8. Satellite: 0 | Modeled from measured latencies | Composite |
| 9 | Downstream travel time | Border→Syabrubesi ~10 min (~14 km); Rasuwagadhi→Gaidakot 6 h 50 min (arrived 15:30); Galchhi +9 m in 30 min; Malekhu +7 m in 30 min | Measured (event record) | Nepalnews 27 Aug; Kathmandu Post 27 Aug 2026 |
| 10 | Communication latency | Cell broadcast: seconds, congestion-immune. Actual 26 Aug: SMS ~16–20 min after border crossing. Cross-border via MoFA: ~1 day | Measured | WMO Bulletin 15 Oct 2025; Nepalnews; ANI 27 Aug 2026 |
| 11 | Comprehension + reaction | 40% found EWS SMS very hard to understand; 46% very unlikely to act; 21% very likely | Measured (survey) | Budimir et al., 2019 |
| 12 | Time to reach safety | **Not addressed here — no published vertical-evacuation route survey exists for Syabrubesi, Timure or Betrawati. The single most important missing measurement** | Not addressed here | — |
| 13 | Infrastructure survival | In-corridor gauges 0/4; 41 bridges + 40 km road destroyed in Rasuwa; >400 MW off grid. Flank stations: one loss per 2–3 yrs (Sedongpu 2021; Barry Arm 2020–21) | Measured | Nepalnews; Yang 2023; Alaska Beacon 2025 |
| 14 | Population reachable ≥5/≥10/≥15 min | Syabrubesi/Timure: ≥5 min only if D≈0; ≥10–15 min only if damming interval exists. Trishuli corridor: ≥15 min for essentially all. Counts not addressed here | Modeled | Derived from row 9 |
| 15 | Capex/opex | A: $1.5–4M capex, $0.3–0.6M/yr. B: $6–15M, $1.5–3M/yr. References: GCF Nepal $36.1M+$14M/7yrs; ShakeAlert $39.4M+$28.6M/yr | Estimated (author-assembled) | Hürlimann 2019; UNDP/GCF 2025; USGS 2019; NHESS 26:3107, 2026 |
| 16 | Institutional dependency | DHM FFD, NEMRC/DMG, NDRRMA, NTA, Army; hydropower operators as siren hosts. Peru precedent: evacuation authority must be pre-delegated or the system cannot fire | Operationally demonstrated (failure mode) | WMO Bulletin, Huggel et al. 2020 |
| 17 | Political dependency | **Binding.** Source at/beyond the border; no standing technical hotline; 27 Aug residual-lake warning came via MoFA a day late. Architecture A deliberately functions **without** Chinese cooperation; every hour beyond it requires cooperation | Operationally demonstrated | ANI 27 Aug 2026; Stimson 22 Jul 2025 |

---

## 6. Statement of uncertainty

The damming interval on 26 August 2026 is **unknown**, and the public timeline (collapse 08:37, flood at the border 08:40, second seismic event ~3 h later) is internally inconsistent. Every Syabrubesi lead-time figure is conditional on it. Collapse volume is unconstrained. Sentinel-1 NRT tier latencies could not be verified and are marked unknown. All ICEYE figures are vendor-claimed. All capex/opex bands are author-assembled from cited anchors, not quoted prices — treat as ±50%. Chinese agency claims of "seven successful early warnings" are agency-claimed and independently unverified. No published vertical-evacuation route survey exists for any settlement in this corridor — the row that most directly determines whether a 90-second alert saves anyone is the row with no data in it.

---

## Sources

(Full names and dates in text. URLs:)

- https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood
- https://earthsky.org/earth/nepal-flash-flood-glacier-collapse-landslide-aug-26-2026/
- https://english.nepalnews.com/s/long-reads/bhote-koshi-catastrophe-exposes-limits-of-nepals-flood-warning-system/
- https://english.nepalnews.com/s/explainers/95-dead-hundreds-missing-what-we-know-so-far-about-bhote-koshi-flood/
- https://kathmandupost.com/national/2026/08/26/ice-avalanche-debris-lake-may-have-triggered-bhotekoshi-flood
- https://kathmandupost.com/columns/2026/08/27/the-flood-crossed-a-border-our-warning-systems-must-too
- https://aninews.in/news/world/asia/china-warns-nepal-of-fresh-major-flood-risk-from-lake-outburst-upstream-of-lhende-river-ndrrma-urges-necessary-caution20260827184259/
- https://www.geologypage.com/2026/08/nepal-flash-flood-august-2026.html
- https://www.mappr.co/nepal-flash-flood-rasuwagadhi/
- https://nhess.copernicus.org/articles/23/3015/2023/ (Yang et al., Sedongpu EWS)
- https://www.lakescientist.com/research-brief-early-warning-systems-in-himalayan-glacial-lakes/ (Cirenmaco summary)
- https://www.gfz.de/en/press/news/details/seismic-forensics-and-its-importance-for-early-warning (Cook et al.)
- https://blogs.agu.org/landslideblog/2021/10/04/the-seismic-signals-of-the-chamoli-landslide-and-debris-flow/
- https://nhess.copernicus.org/articles/22/3309/2022/ (Van Wyk de Vries et al.)
- https://www.nature.com/articles/s43247-026-03352-y (Ahmed et al., Comms Earth & Env 7:217, 2026)
- https://pubs.geoscienceworld.org/ssa/tsr/article/4/1/43/634286/ (Seismic Record, Alaska)
- https://alaskabeacon.com/2025/09/12/joint-effort-assesses-landslide-and-tsunami-risks-in-alaskas-prince-william-sound/
- https://link.springer.com/article/10.1007/s11069-008-9303-x (Badoux et al., Illgraben)
- https://www.parcs.ch/npf/pdf_public/2025/55950_20251203_141835_Hrlimann_Debris-flow_monitoring_EarthScienceReviews_2019.pdf
- https://en.wikipedia.org/wiki/Eastern_Ruapehu_Lahar_Alarm_and_Warning_System
- https://www.usgs.gov/volcanoes/mount-rainier/science/monitoring-lahars-mount-rainier · https://www.usgs.gov/observatories/cvo/science/automated-lahar-detection-systems
- https://www.seismosoc.org/news/lahar-detection-system-upgraded-for-mount-rainier/
- https://arc.lib.montana.edu/snow-science/item/2610 (Mayer et al., infrasound)
- https://esurf.copernicus.org/articles/7/491/2019/ (Heck et al., mini-arrays)
- https://www.nature.com/articles/srep19259 (Chao et al., D-phase)
- https://www.hindawi.com/journals/geofluids/2019/1426019/ (Lee et al., back-projection)
- https://attheu.utah.edu/facultystaff/seismic-monitoring-may-improve-early-warnings-for-glacial-lake-outburst-floods/ (Maurer et al.)
- https://link.springer.com/article/10.1007/s11431-019-1475-y (Baige barrier lake)
- https://link.springer.com/article/10.1007/s10346-019-01269-6 (Guizhou success)
- https://link.springer.com/article/10.1007/s10346-024-02380-z (Loew et al., Brienz)
- https://www.geopraevent.ch/project/monitoring-system-in-brienz-brinzauls-switzerland/?lang=en (vendor)
- https://nhess.copernicus.org/articles/24/3833/2024/ (Manconi et al., ICEYE at Brienz)
- https://eo4society.esa.int/2025/08/08/satellite-radars-reveal-early-signs-of-slope-instability-years-before-blatten-rock-ice-avalanche/
- https://www.nature.com/articles/s43247-025-02994-8 (Blatten warming context)
- https://blogs.egu.eu/divisions/nh/2025/06/11/the-blatten-landslide-in-switzerland/ · https://blogs.egu.eu/divisions/nh/2026/08/18/practical-use-of-natural-hazard-monitoring-systems-during-escalating-risk-scenarios/
- https://nhess.copernicus.org/articles/26/3107/2026/ (Maschler et al., UAV docks)
- https://wmo.int/media/magazine-article/glacier-lake-513-peru-lessons-early-warning-service-development
- https://www.stimson.org/2025/investigating-an-emerging-climate-hazard-transboundary-glacial-floods-on-the-china-nepal-border/
- https://www.scmp.com/news/china/science/article/3365488/china-and-nepal-built-early-warning-system-melting-glaciers-himalayas-does-it-work
- https://gc.copernicus.org/preprints/gc-2019-3/gc-2019-3-manuscript-version5.pdf (Budimir et al.)
- https://dmgnepal.gov.np/en/divisions/national-earthquake-monitoring-and-research-center-5634
- https://www.undp.org/nepal/press-releases/report-icimod-and-undp-identifies-potentially-dangerous-glacial-lakes-koshi-gandaki-and-karnali-river-basins
- https://www.undp.org/press-releases/green-climate-fund-approves-361-million-help-nepal-protect-lives-and-livelihoods-glacial-flood-risks
- https://wmo.int/resources/wmo-bulletin/wmo-bulletin-vol-74-2-2025/leveraging-common-alerting-protocol-and-cell-broadcast-technology-advancing-early-warnings-all
- https://www.usgs.gov/news/national-news-release/usgs-awards-more-125-million-advance-shakealert-earthquake-early-warning
- https://www.iceye.com/sar-data/tactical-access (vendor)
- https://creodias.eu/cases/timeliness-and-frequency-of-sentinel-satellite-products-explained/
- https://mapping.emergency.copernicus.eu/about/rapid-mapping-manual/product-overview/
- https://euronews.com/green/2025/06/04/swiss-glacier-collapse-highlights-urgent-need-for-monitoring-and-warning-systems-wmo-says
- https://glofca.org/en/early-warning-systems/
