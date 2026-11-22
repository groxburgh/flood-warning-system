# The Build Decision

**Run 7 — synthesis of Runs 1–6. Prepared 28 August 2026, day 3 of the disaster. Written for a 1–3 person, software-strong, modestly funded, non-governmental team deciding what — if anything — to build.**

Everything below is drawn from the six research runs (cited as R1–R6) and their named sources. Nothing new is asserted; where the runs left something unknown, it stays unknown here.

---

## Stage 1 — Where the chain actually breaks

The chain: hazard state → observable signal → detection → classification → confidence → localization → propagation → alert trigger → communication → comprehension → movement → survival.

Ranked by expected preventable deaths, on the evidence of 26 August:

**Break 1 — Classification, not detection.** The collapse's seismic signal was global and near-instant; USGS catalogued it as an M4.4 earthquake and took hours to call it an M5.2 landslide, an error that even propagated into Copernicus EMS's official activation record (R1). Sedongpu (Tibet) shows a duration-based discriminator resolves this operationally in 40–60 seconds at ~75% precision, with zero misses of major events across 2021–2022 (R2). The signal existed at 08:37. The *meaning* arrived by telephone at 09:00. That 23-minute gap is the single largest recoverable block of warning time in the whole event, and it is a software gap.

**Break 2 — Sensors sited in the kill zone, with no dead-station logic.** Every corridor gauge died *below* its warning threshold — the flood destroys the sensor before the sensor crosses the threshold, so a threshold architecture is structurally blind to this hazard class (R1). Yet the stations' deaths were themselves a signal: Rasuwagadhi stopped transmitting at 08:50. A missed-poll ("dead-man") alarm would have alerted DHM by ~08:53 — earlier than the human phone chain managed — **using hardware that already exists** (R1). Nobody was listening for silence.

**Break 3 — The instrumentation void at the source, across a border.** Nodes 1–4 of the failure chain (signal generated → observed → transmitted → interpreted) all failed because nothing was watching the Lhende catchment on either side (R4). The fix is operationally proven 400 km east: China's Sedongpu system — geophones, duration logic, water-level thresholds, satellite backhaul — has issued real warnings for three major ice-collapse cascades (R2). A Nepali-flank equivalent (Architecture A) costs an estimated $1.5–4M capex, $0.3–0.6M/yr opex, needs no Chinese cooperation, and buys ~14–19 minutes at Syabrubesi and 1–6.5 hours downstream (R2). That is state/donor money, not small-team money — but the concept note now exists.

**Break 4 — Comprehension and action downstream, where the hours already existed.** 66% of recorded deaths (as of 28 Aug, 15:00) sit in Chitwan and Nawalparasi East, districts that had roughly six to seven hours of warning; Rasuwa, which had none, records 12 of 538 (R1, R3). This is confounded — bodies were carried tens of kilometres downstream and are being relocated between districts; DNA-based origin tracing is weeks away (R3). But the baseline survey evidence stands regardless: 40% of Nepali recipients find flood SMS very hard to understand, 46% are very unlikely to act, and the channel people actually trust (in-person, voice) is not the channel the system uses (Budimir et al., Geoscience Communication, 2020; R3). The one clean success — 1,650 children evacuated at Bidur — was an institutional drill effect, not a technology effect (R3).

**Break 5 — Cross-border channel latency.** Even when China actively cooperated (the 27 August barrier lake: volume estimates, simulations, a real warning), the information routed through the Ministry of Foreign Affairs and cost about a day (R5). The six-scenario analysis found no evidence China withheld warning of the primary collapse — the best-supported reading is that neither side had meaningful warning (R5). The problem is channel design, not malice: a technical-to-technical hotline is a Tier 2 ask with a working precedent genre (Brahmaputra ELM, Nyalam–Sindhupalchok WeChat), and it converts ~24 hours of latency into hours for exactly the hazard sub-class (persistent lakes and dams) where warning demonstrably works.

**Break 6 — Decay.** Tsho Rolpa's warning system has died twice in 25 years and is dead now; the same valley's people believe otherwise (R3). DHM has no founding act; the corridor fix has been announced three times (2023, Aug 2025, May 2026) without being built; the reported DHM budget trajectory is sharply down (R4, exact figures unverified). Anything built without a named owner and a funded O&M line is a future Tsho Rolpa.

**The hard floor.** Timure and Syabrubesi are largely un-warnable for a no-damming-interval collapse: the physics ceiling is roughly (damming interval + ~10 min) − ~2–3 min, or about 8 minutes absolute if the dam holds no time at all (R2). For those two settlements the honest lever is not warning at all — it is pre-identified vertical safe points within 2–3 minutes' walk, drilled (R2, R3). No route survey exists for any settlement in the corridor; that absence is the single most important missing measurement in the entire evidence base (R2, R3).

---

## Stage 2 — Interventions derived from the breaks

Attributes per candidate: chain segment / what decision changes, whose / time bought / dependencies / robustness / cost / effort for 1–3 people / main risk / kill criteria.

### A. The Dead-Station Alarm (from Break 2)
Software watching DHM's existing gauge telemetry for silence and anomalous behavior, alerting the Flood Forecasting Division automatically.
- **Decision changed:** FFD's decision to warn moves from "wait for a human to phone" to "silence from an upstream station + context = presumptive event." On 26 August this fires ~08:53 vs the actual 09:16 — roughly **+20 minutes for every settlement from Betrawati down**, turning Betrawati's +4 minutes into ~+25 (R1).
- **Dependencies:** DHM data access and willingness (institutional row: B2G alerting is the legally clean product — Nepal's DRRM Act §24(2) criminalizes false *public* alarms by "whoever," and §31's good-faith immunity covers officials, not outsiders; R4). Requires knowing the gauges' actual telemetry cadence — currently unknown (R1).
- **Robustness:** the alarm's whole premise is infrastructure failure; it works *because* things break.
- **Cost/effort:** near-zero marginal hardware; weeks of software for a small team, plus the partnership work, which is the real work.
- **Main risk:** DHM declines, or telemetry cadence (if 10-minute polling, per R6) blunts the alarm to +10 rather than +20 minutes.
- **Kill criteria:** no data access after a serious attempt; cadence or reliability makes silence indistinguishable from routine dropout at useful speed.

### B. The Seismic Mass-Movement Watcher (from Break 1)
Software on public global/regional seismic feeds (USGS/IRIS-class) running duration-plus-amplitude discrimination (the Sedongpu logic) over defined Himalayan border catchments, notifying designated institutions — DHM, NDRRMA, ICIMOD — within ~2–3 minutes of a long-duration, non-impulsive signal, with the catchment named.
- **Decision changed:** DHM learns "probable mass movement, Bhote Koshi catchment, check now" at ~T+3 min instead of learning by telephone at T+23. Feeding A's recipients, it also arms the downstream SMS machine ~20 minutes earlier.
- **Time bought:** ~15–20 minutes institutional lead; at ~75–85% precision initially, with ~25% over-warning at Sedongpu's threshold — acceptable for an institutional (not public) alert (R2).
- **Dependencies:** public feed latency for this region (unverified — the first technical task); a validation catalogue (thin: this hazard class has few well-recorded regional events; R1 flagged that no P(detect) curves exist).
- **Robustness:** total — nothing of it sits in the valley.
- **Cost/effort:** months for a small team, ideally with one collaborating seismologist. The 2025 and 2026 events plus Chamoli give a starter test set.
- **Main risk:** discrimination at 50–150 km regional stations proves too slow or too noisy; the classifier becomes correct-but-retrospective, which is failure by this project's own rule.
- **Kill criteria:** cannot classify the 26 Aug 2026 and 8 Jul 2025 events correctly within 3 minutes in retrospective replay; real-time feed latency exceeds ~5 minutes.

### C. The Persistence Campaign (from Break 5)
Not software. A specific, named set of asks: (1) Sedongpu/Cirenmaco threshold methodology transfer (the NHESS authors explicitly invite replication); (2) a standing DHM↔China Ministry of Water Resources technical hotline for routine monitoring, bypassing the MoFA gate for non-crisis updates; (3) confirmation that the Lhende source slope joins CAS's instrumented-site list, with alert-sharing even without raw data. Routed through ITPCAS (Dr. D.B. Kattel — a Nepali scientist inside the key Chinese institute), IMHE Chengdu, and ICIMOD, of which China is a full member (R5).
- **Decision changed:** whether the *next* barrier-lake warning takes a day or an hour to cross the border.
- **Cost:** letters, follow-ups, and patience. The Brahmaputra ELM took 16 years and survived a suspension; the record says persistent low-odds asking eventually works, and not asking guarantees the status quo (R5).
- **Kill criteria:** none. This is never killed, only continued.

### D. The Safe-Haven Survey and Drill Layer (from Breaks 4 and the hard floor)
Village-by-village mapping of where safety *is* (elevation, route, bridge dependence, night access, capacity) for the eight corridor settlements — the measurement every other intervention silently assumes and nobody has made — plus assembly-point drills on the Bidur model, and a re-entry protocol for responders working under fresh barrier lakes (fixed radio check-ins, automatic withdrawal triggers; R3).
- **Decision changed:** what a person does with the minutes; whether a school or lodge acts as a unit or as 200 separate confused individuals.
- **Evidence:** the only intervention class with an operationally demonstrated life-save in this exact event (Bidur), and the cheapest per unit of effect (R3's ranked table).
- **Effort:** days per settlement, low-tech; a partnership project (local government, schools, Practical Action-type NGOs), not a solo build — but a small team can produce the survey method, the map templates, and the drill playbook.

### E. The Tourist Reach Fix (from Break 4's foreign-SIM gap)
SMS opt-in captured at the TIMS/park-permit checkpoint every trekker already passes, plus an English-language relay of official DHM/NDRRMA alerts to lodges and operators. Narrow, cheap, institutionally simple, and aimed at a documented gap (~500–600 foreign tourists unaccounted at peak; whether any foreign SIM received the 679,295 SMS is unknown; R3).

### What the cost-per-person row honestly says
It cannot be computed yet. The two missing denominators are ward-level exposed population by settlement (does not exist publicly; R3) and the mortality-location truth (DNA tracing, weeks away; R3). The calculation shape is ready — population × lead-time table (R3) ÷ intervention cost — and A and B sit at near-zero marginal cost against it, which is why they lead regardless of how the denominators resolve. Architecture A's $1.5–4M for the upper valley protects a population whose size is genuinely unknown; that number must be fought for before anyone spends the millions.

---

## Stage 3 — Disposition of the original six candidate seeds

| Seed | Verdict | Reason |
|---|---|---|
| (i) Seismic watcher | **KEEP** — becomes B | Directly targets Break 1; operational precedent at Sedongpu |
| (ii) Fusion engine | **DEFER** | R2: fusion improves confidence, not latency, and must never delay the seismic trigger. Build later on top of A+B outputs, as a confidence layer for institutional recipients |
| (iii) Satellite-change watchlist | **KILL as minutes-warning; KEEP narrowly as lake-watcher** | Chamoli is an operationally demonstrated negative for timing (5 years of visible precursor, no forecastable moment; R1/R2). But satellite demonstrably works for post-event barrier-lake detection and lake screening — the 27 Aug lake was found that way. Scope it to that |
| (iv) English alert relay for tourists | **KEEP** — becomes E, merged with the TIMS opt-in | Real, documented gap; legally clean if it relays official alerts attributively (R4) |
| (v) Open hazard dashboard | **KILL as standalone** | Fails the non-negotiable test — "provides visibility" changes no decision. A status view ships inside A/B for institutional users only |
| (vi) Phone-tree software | **MERGE into D** | The human network is the durable layer (Bangladesh CPP, 50+ years; R4), but its bottleneck is organization and drills, not software |

---

## Stage 4 — Recommendation

**Outcome class: B + D.** Precursor monitoring of sudden collapses does not work (Outcome A rejected — Chamoli's negative result is physical, not instrumental). Event detection works and is operationally proven next door; the gap between the signal and the institutions is software and channel design (Outcome B, with C's classification gap as its core). Downstream, where the hours already existed, response — comprehension, drills, safe havens — is the bottleneck (Outcome D). And for the two border settlements, the honest answer is Outcome E's: siting and safe points, because physics caps warning at minutes.

**The null-build insight turned out to be the build.** "Make existing signals reach existing institutions ten minutes faster" is not the consolation prize — it is precisely interventions A and B, and they are the highest-value, lowest-dependency, legally cleanest things a 1–3 person team can make.

**For this team, in order:**
1. **Build A (dead-station alarm)** — but open with the partnership question, since DHM's answer is the kill criterion. First technical step: establish the real telemetry cadence of DHM's gauges.
2. **Build B (seismic watcher)** — starting with retrospective replay against 26 Aug 2026, 8 Jul 2025, and Chamoli 2021. If it cannot classify those three inside three minutes in replay, stop.
3. **Run C (the persistence campaign) in parallel, forever.** Letters to ITPCAS, IMHE, ICIMOD, and Nepal's MoFA/DHM naming the three asks. Slim odds are the cost of the attempt.
4. **Publish D's method and E's proposal** as short concept notes to the institutions that can execute them (municipalities, Nepal Tourism Board, NGOs) — the team's leverage there is the analysis, not the implementation.
5. **Hand Architecture A/B (the $1.5–4M / $6–15M hardware tiers) to the people with money** — DHM, NDRRMA, GCF/World Bank/ADB channels, the hydropower licensees whose 900 MW of exposure is the most motivated capital in the valley (R4's El Salvador precedent: the utility pays because the river is its business). The post-disaster window is open now and the record says it closes fast.

**Talk to before building:** DHM Flood Forecasting Division (Binod Parajuli; Sauharda Joshi), NDRRMA, ICIMOD (Saswat Sanyal's team; DG's office), Practical Action Nepal, ITPCAS (D.B. Kattel; Wei Yang — Sedongpu lead author), IMHE Chengdu (Su Lijun), Dave Petley, Jakob Steiner (HiRISK), and the Stimson Center's Nepal early-warning project — every one of these names appears in the runs' primary sources.

**Resolve before anyone commits capital** (from R1): where people actually died (DNA tracing, ~2 weeks); gauge telemetry architecture; whether the 08:37 signal classifies in <3 minutes in replay; seismic false-alarm behavior for this region.

**The staged path to the north star:**

| Stage | What | Who pays | Status |
|---|---|---|---|
| v0 | Dead-station alarm + seismic watcher + hotline campaign — existing signals, minutes faster | A small team's time | **Buildable now** |
| v1 | Automated institutional autotrigger integrated at DHM; drills + safe-haven maps in the corridor | DHM/NGO/municipal budgets | Concept notes ready |
| v2 | Architecture A: Nepali-flank geophones, mini-arrays, high-bank gauges, sirens ($1.5–4M + $0.3–0.6M/yr, with hydropower co-funding and a named O&M owner) | State/donor/licensees | Costed; window open |
| v3 | Architecture B: watched sources, radar/GNSS/UAV docks on the top 5–10 slopes; Tier 2 cross-border alert exchange ($6–15M + $1.5–3M/yr) | Donor + bilateral | Requires v2 + C's success |

Each stage is independently valuable and survives the later ones never being funded.

**One caution to carry into all of it.** The most dangerous corridor scored as the worst intervention market, and the best market (Khumbu) is not where this week's dead are (R6). A team that wants impact per dollar builds the software (which is corridor-agnostic — A and B generalize to every Himalayan border catchment) and lets the hardware go first to where it can actually survive: that tension between where the grief is and where the system can work is real, and pretending otherwise is how projects fail nobly.

---

## Master schema — the assembled system (Bhote Koshi–Trishuli anchor)

| # | Variable | Best current answer | Grade | Run |
|---|---|---|---|---|
| 1 | Cascade stages | Collapse → damming → breach → propagation addressable; source-instability timing not addressable | Op. demonstrated (neg. for stage 0) | R1/R2 |
| 2 | Earliest observable signal | Multi-year slope deformation — retrospective only, no terminal acceleration | Measured (retrospective) | R1/R2 |
| 3 | Earliest operational signal | The collapse's own seismic radiation, T0 | Op. demonstrated (Sedongpu) | R2 |
| 4 | Detection latency | 10–20 s local geophone; ~1–3 min regional; actual event: 23 min by telephone | Op. dem. / measured | R2/R3 |
| 5 | Classification | 40–60 s at ~75% precision achievable; actual: hours, initially wrong | Op. dem. / measured | R2/R1 |
| 6 | Localization | <5 km with geometry; ≤40 km station distance needed for damming (D-phase) detection; border side of this source still disputed | Measured / disputed | R2/R1 |
| 7 | False alarms | ~25% at Sedongpu threshold; 1-in-20 Illgraben; unmeasured for Nepal | Measured elsewhere | R2 |
| 8 | Miss rate | 0 major-event misses at Sedongpu; N=1 total miss here; no P(detect) curves exist for this region | Op. dem. / unknown | R2/R1 |
| 9 | Travel times | Border→Syabrubesi ~10 min; →Betrawati ~40 min; →Galchhi ~2 h; →Gaidakot 6 h 50 m | Measured | R1/R6 |
| 10 | Communication | SMS dispatch ~16 min after border crossing; cell broadcast absent in Nepal; cross-border ~1 day via MoFA | Measured | R3/R5 |
| 11 | Comprehension | 40% find SMS very hard to understand; 46% very unlikely to act; drills flip this (Bidur) | Measured (survey) / op. dem. | R3 |
| 12 | Time to safety | **No survey exists for any settlement — the missing measurement** | Not measured | R2/R3 |
| 13 | Infrastructure survival | In-corridor gauges 0/4–5/8; nothing in the valley bottom can be load-bearing | Measured | R1/R6 |
| 14 | Population reachable | Structure known (near-zero at border, near-total below Galchhi); denominators unknown | Modeled / unknown | R3 |
| 15 | Capex/opex | v0 ≈ team time; Arch. A $1.5–4M + $0.3–0.6M/yr; Arch. B $6–15M + $1.5–3M/yr (±50%) | Estimated | R2 |
| 16 | Institutional | DHM warns fast once it knows and is legally protected; DHM has no founding act; systems decay without a named payer (Tsho Rolpa ×2) | Measured | R4 |
| 17 | Political | No Chinese cooperation needed for v0–v2; every hour beyond requires Tier 2; three announcement cycles, zero implementation, but the 27 Aug lake warning proves ad hoc cooperation exists | Measured | R5 |

*Full sources are carried in Runs 1–6; this memo introduces no new sources.*
