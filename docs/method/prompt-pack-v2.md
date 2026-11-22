# Flash Flood Early Warning — Deep Research Pack v2

## The decision this research supports

Can a small, deployable system detect this class of cascading mountain hazard early enough, reliably enough, and with enough downstream response capacity to measurably reduce deaths — and if not, where in the chain does the highest-value intervention actually sit?

## The north star (the system this research is trying to earn)

A live, continuously monitored view of every prioritized hazard source above the corridor — watched 24/7 by machines, analyzed automatically for large movements and anomalies — triggering alerts without waiting for a human to look out of a window, delivered through the channels Nepalis actually use, fast enough that no minute of physically available warning time is wasted. Stated as targets, not claims: collapse-class event detected and classified in ≤2 minutes; alert on phones, radios, and sirens, carrying a named safe destination, in ≤5 minutes; every settlement in the corridor receiving the maximum lead time physics allows.

Physics sets the ceiling on available warning time. Everything between current practice and that ceiling is engineering, money, and persistence. The research's job is to measure the ceiling with cold precision and map the fastest route toward it — never to conclude the target is too ambitious.

## The causal chain

Every run attaches to one segment of a single causal chain:

**hazard state → observable signal → detection → classification → confidence → source localization → propagation/travel-time → alert trigger → communication → comprehension → movement → survival**

The survival equation governing everything:

**usable lead time = impact time − (detection + classification + decision + transmission + comprehension + movement)**

## Rules embedded in every run (they appear inside each prompt; summary here)

1. **Three detectability labels.** Every signal must be classified as RETROSPECTIVE (visible in hindsight), OPERATIONAL (available and correctly interpretable in real time under realistic conditions), or ACTIONABLE (strong enough to justify protective action given false-alarm costs). These are different things and may not be conflated.
2. **Operational evidence standard.** No technology gets credit for "working" unless evidence shows it changed — or credibly could have changed — the time available for a real protective decision before impact. "Can detect landslides" is not evidence. "Caused an operational warning before a comparable destructive event" is.
3. **Hypotheses, not facts.** Context figures are drawn from early reporting on a days-old event and are supplied as hypotheses to test against primary sources (USGS event pages, Copernicus EMS Rapid Mapping activations, ICIMOD, DHM/NDRRMA statements), never as ground truth to repeat.
4. **The no-solution branch is a valid finding.** "No viable early-warning intervention exists for this segment; value lies in siting, zoning, safe havens, and post-event response" is an acceptable — and important — conclusion. Do not force a technology recommendation. A wall in one segment redirects the ambition toward other segments; it never ends the program.
5. **Common schema.** Every run ends by filling the shared table below so the seven outputs compose into one system model instead of seven essays.
6. **No wall verdicts.** For every obstacle found — technical, legal, political, financial — the research must report (a) what it would take to break or bypass it: cost, time, precedent, and who could act; (b) the interim workaround; (c) what remains buildable if it never falls. "Not possible" is reserved for physics, and even then the physical ceiling must be stated precisely. Low-probability, low-cost moves (a request that will likely go unanswered) are paths with a price, never walls.

## The common schema table (final section of every run's output)

| # | Variable |
|---|----------|
| 1 | Cascade stage(s) addressed (source instability / collapse / damming / breach / propagation / warning / movement / survival) |
| 2 | Earliest observable signal |
| 3 | Earliest OPERATIONALLY detectable signal |
| 4 | Detection latency |
| 5 | Classification latency + accuracy at that latency |
| 6 | Source location uncertainty |
| 7 | False alarm rate |
| 8 | Miss rate — P(detection within 60 / 120 / 180 s of event) |
| 9 | Downstream travel time to named locations |
| 10 | Communication latency to end recipients |
| 11 | Comprehension + reaction time |
| 12 | Time needed to reach safety, by location/population |
| 13 | Infrastructure survival probability during the event |
| 14 | Population reachable with ≥5 / ≥10 / ≥15 min of warning |
| 15 | Capex / annual opex |
| 16 | Institutional dependency (who must act) |
| 17 | Political dependency (what cooperation is assumed) |

Each filled row carries an evidence grade — **measured / operationally demonstrated / modeled / vendor-claimed / speculative** — and a source. Rows a run cannot support are marked "not addressed here," never guessed.

## Run order

**1 → 2 → 3 → (4 ∥ 5) → 6 → 7.** Runs 1–2 establish whether the problem is technically solvable and build the counterfactual clock. Run 3 establishes what minutes are worth (a 10-minute warning means nothing until you know what can be done with 10 minutes). Runs 4–5 establish who can act and what cooperation is realistic. Run 6 establishes where intervention creates the most value. Run 7 is synthesis, not fresh research — it takes the six filled tables as input and produces the build decision. Corridor geography lives inside Run 1 (the clock table needs travel times); the comparative corridor scan is deliberately late (Run 6) because it informs where to intervene, not whether.

---

## RUN 1 — Event forensics and the counterfactual warning clock

```
GOAL: Reconstruct the 26 August 2026 Bhote Koshi disaster (Nepal-Tibet border,
Rasuwa district: Lhende Khola -> Bhote Koshi -> Trishuli) and the July 2025
flood in the same valley, and produce a counterfactual warning clock: under
realistic architectures, when would the first credible alert have been
available to a person at each named downstream location? This supports a
go/no-go decision on building warning capability for this hazard class.

ANCHOR: Glacier/slope collapse reported ~08:37-08:40 NPT on 26 Aug 2026 near
Langtang Lirung; debris flood through Rasuwa, Nuwakot, Dhading districts.
Prior event: 8 July 2025 outburst flood, same valley.

HYPOTHESES TO TEST (from early reporting; verify against primary sources -
USGS event pages, Copernicus EMS Rapid Mapping activations, ICIMOD, DHM Flood
Forecasting Division, NDRRMA, Dave Petley's AGU landslide blog - and correct
any that are wrong):
H1. Collapse from ~5,000-5,200 m; ice-rock avalanche dammed the Lhende Khola;
    dam then breached.
H2. Seismic energy equivalent to ~M5.2, initially catalogued as an earthquake;
    a second event (~M4.2) reported roughly three hours later.
H3. Flood crossed at Rasuwagadhi and reached Syabrubesi (~14 km) in ~10 min;
    Trishuli rose ~9 m in ~30 min.
H4. DHM river gauges in the corridor were destroyed before crossing alert
    thresholds; first automated alert would have fired hours late, far
    downstream.
H5. First institutional knowledge came by telephone ~09:00; mass SMS from
    ~09:16.
H6. Not rainfall-driven.

QUESTIONS:
1. Authoritative timeline, minute by minute, both events: collapse, damming
   (how long did the dam hold?), breach, arrival at each named location
   (Rasuwagadhi, Timure, Syabrubesi, Betrawati, Bidur/Battar, Trishuli Bazar,
   Gajuri/Malekhu), each warning action, and the multi-pulse sequence -
   was there a second collapse or surge, and what does that imply for
   warning during rescue and re-entry?
2. Valley geometry and propagation: channel distances, gradients, observed
   wave speeds between points; was there an observable flow DROP downstream
   while the dam impounded water (a distinctive pre-breach signal), and if
   so, for how long?
3. Mechanism and trigger: current scientific position, is the
   earthquake-vs-collapse question settled, what remains provisional?
4. Precursors, labeled: for every claimed precursor (thermal anomaly,
   deformation, meltwater ponding, crevassing, prior activity), assign
   RETROSPECTIVE / OPERATIONAL / ACTIONABLE and justify. The test for
   OPERATIONAL: could a realistic system have produced something like
   "slope velocity exceeded X for Y hours; collapse probability elevated"
   before 08:37, at what confidence? A crack visible in imagery after the
   fact does not qualify by itself.
5. Chamoli comparison (7 Feb 2021, Uttarakhand; Shugar et al., Science 2021):
   which precursors were found in hindsight, and would any have passed the
   OPERATIONAL test with technology deployed at the time or now?
6. Had any published assessment flagged this valley after July 2025?

CENTERPIECE OUTPUT - the counterfactual clock table. Rows: detection pathway
(satellite precursor monitoring / source radar+GNSS / seismic / infrasound /
upstream water-level tripwire / downstream gauge / human observation).
Columns: first physically detectable signal (T-/T+), detection latency,
classification latency, earliest credible alert time, resulting lead time at
each named location. Mark every cell with its evidence grade; leave cells
unknown rather than smoothing.

RULES: Apply the three detectability labels. Name every source in full
(organization + document title + date). Label claims confirmed /
single-source / disputed. All casualty and damage figures carry an as-of
date. Do not invent figures; state unknowns plainly. Finish by filling the
common schema table (17 variables, evidence grade per row; mark unsupported
rows "not addressed here").
```

## RUN 2 — Detection and classification engineering (operational evidence only)

```
GOAL: Establish the minimum technically credible detection + classification
architecture for sudden rock-ice collapse cascades (collapse -> river
blockage -> dam breach -> debris flood) in high Himalayan terrain - judged
strictly by operational track record, not capability claims. Context case:
the 26 Aug 2026 Bhote Koshi disaster (Nepal), where downstream gauges were
destroyed before alerting and the hazard source sits at ~5,000 m near or
beyond an international border.

HARD RULE: For every technology, answer: what evidence exists that it has
CAUSED an operational warning to be issued before a comparable destructive
event? If none exists, say so plainly. "Can detect landslides" is not
evidence. Label every vendor claim as vendor-claimed. Prefer peer-reviewed
system evaluations and post-event reports over marketing.

QUESTIONS:
1. Seismic and infrasound event detection: for operational systems (Alpine
   debris-flow networks, Sichuan systems, Alaska landslide monitoring,
   volcano lahar systems), report P(detection within 60/120/180 s | event),
   false alarm rate, MISS rate, availability/outage record, and cost.
2. Classification as a separate stage: the 2026 signal was reportedly
   catalogued initially as an earthquake by global networks. How quickly can
   existing systems distinguish a large slope failure from tectonic events,
   avalanches, blasts, and noise - and what is the latency-accuracy
   tradeoff? (A system that is 85% correct in 45 s may beat one that is 98%
   correct in 15 min. Treat "correct but retrospective" as failure.)
3. Source localization: how fast can a detected mass-movement signal be
   geolocated, and to what radius? Does narrowing from "somewhere in a 50 km
   zone" to "this specific catchment" within 60-90 s materially change what
   can be alerted, and what station geometry does that require near the
   Nepal-Tibet border?
4. Cascade-transition signals: which transitions emit observable signals -
   e.g., anomalous downstream flow drop during damming, lake-level rise,
   breach onset - and has any system operationally exploited them?
5. Satellite: decompose the full pipeline latency (tasking/capture ->
   downlink -> processing -> algorithm or analyst -> alert) for Sentinel-1/2,
   Landsat, and commercial SAR (ICEYE, Capella) - not revisit time alone.
   Is operational days-ahead instability warning demonstrated anywhere, or
   is satellite currently precursor-screening and after-action mapping?
6. In-situ source monitoring: ground-based interferometric radar, GNSS,
   cameras, lake sensors, upstream tripwire gauges, DAS on infrastructure -
   power, telecom, winter survivability, maintenance burden at 4,000-5,000 m,
   and track record (Peru Lake 513, Tsho Rolpa, Bhutan, Central Asia).
7. Blatten (Birch Glacier, Valais, May 2025) - property-by-property
   comparison, not analogy: prolonged observable instability phase? prior
   known hazard focus? road access for instrument deployment? monitoring
   density? escalating decision authority over days? For each property:
   present or absent at Bhote Koshi? State explicitly which parts of the
   Swiss result transfer and which do not.
8. Fusion: what evidence exists that combining modalities (seismic +
   satellite + gauges + weather) materially improves confidence or latency
   over single modes in operational settings? Test this; do not assume it.
9. Robustness: evaluate every candidate architecture under a post-impact
   infrastructure failure model - assume in-corridor gauges, telecom, grid
   power, and roads fail DURING the event. What still works? What requires
   independent power, satellite backhaul, geographic separation?
10. The live-view target: specify and cost what CONTINUOUS 24/7 observation
    of the top 5-10 prioritized hazard sources above this corridor would
    actually require - in-situ mesh (radar, GNSS, cameras, seismic) plus
    satellite cadence plus communications backhaul plus automated analysis -
    as a staged bill of materials with an end-to-end latency budget. This is
    a costing exercise, not a feasibility opinion.

OUTPUT: capability matrix (method x P(detect in 60/120/180 s) x
classification latency+accuracy x localization x false alarm x miss x
survivability x capex/opex x maintenance); the Blatten property table; 1-2
minimum credible architectures with what each buys in lead time at
Syabrubesi vs the Trishuli towns, with cost bands. Name sources in full
(organization + title + date). State uncertainty explicitly. Report
obstacles as costs, not verdicts: for every wall, state what it would take
to break or bypass it - cost, time, precedent, who could act - plus the
interim workaround; reserve "not possible" for physics, stated as a precise
ceiling. Finish by filling the common schema table (17 variables, evidence
grades).
```

## RUN 3 — Downstream survival: what minutes are worth

```
GOAL: Quantify what warning minutes are worth in Nepal's Bhote Koshi-Trishuli
corridor: reception -> comprehension -> movement -> survival. This converts
lead time (from detection research) into lives, and is the basis for any
cost-per-person-protected estimate.

CONTEXT HYPOTHESES (verify; early reporting): on 26 Aug 2026 the working
channel was a ~09:00 telephone call to the Flood Forecasting Division,
followed by mass SMS from ~09:16 (~679,000 messages via Nepal Telecom and
Ncell); one school in Bidur reportedly evacuated ~1,650 students uphill on
receiving it; upstream settlements got no warning; hundreds of hydropower
workers were in tunnels; the valley hosts trekkers on foreign SIMs.

QUESTIONS:
1. Safe destinations - the governing question. For each named settlement
   (Timure, Syabrubesi, Betrawati, Bidur/Battar, Trishuli Bazar, Gajuri):
   where IS safety (elevation gain required, route, bridge dependence,
   night and monsoon accessibility, capacity), and what fraction of the
   population can physically reach it within 5 / 10 / 15 / 20 minutes? Use
   terrain data, evacuation-modeling literature, and any existing hazard
   zonation; where no study exists, model roughly and label it modeled.
2. Warning-to-action latency: evidence on comprehension time, trust and
   false-alarm fatigue, night events, tourists who don't read Nepali. The
   full equation is impact time minus detection, classification, decision,
   transmission, comprehension, movement - which terms dominate here?
3. Channels: cell broadcast vs SMS (latency, reach, foreign-SIM behavior);
   Nepal's actual cell-broadcast and Common Alerting Protocol status; Early
   Warnings for All rollout status in Nepal; sirens (cost, power, trigger
   chain, maintenance record - including the history of the Tsho Rolpa
   siren system: did it survive?). Also map the channels Nepalis actually
   use at scale - FM and community radio, loudspeakers, Facebook and other
   social platforms (officials used Facebook and media interviews in this
   event) - with reach and latency for each.
4. Special populations: what specifically made the Bidur school evacuation
   work; hydropower tunnel evacuation protocols and any legal warning
   obligations on licensees; trekking lodges and tour operators.
5. Multi-pulse hazard: warning arrangements for responders and returnees
   when secondary collapses or barrier-lake breaches follow the first wave
   (reported in this event) - who warns the rescuers?
6. Community-based EWS: the Karnali gauge-reader model (Practical Action
   and partners) - independently evaluated performance in real floods,
   costs, decay rates, and what keeps volunteer networks alive.
7. The location-based instruction concept: evidence for warnings that
   carry WHERE TO GO for the recipient's location ("reach point X uphill,
   Y minutes") vs generic alerts. Does any operational system do this?

OUTPUT: a population x lead-time table (people gaining protection at each
increment of warning at each location - this feeds cost-per-person-protected
later); last-mile interventions ranked by additional people reaching safety
per dollar, each with evidence grade (independently evaluated vs NGO
self-reported) and named implementers; an assessment of the location-based
instruction concept. Name sources in full (organization + title + date).
Thin evidence must be called thin. Finish by filling the common schema
table (17 variables, evidence grades).
```

## RUN 4 — Nepal's warning governance: authority, liability, money, decay

```
GOAL: Map who may detect, decide, warn, and evacuate in Nepal - de jure
versus de facto - and what keeps warning systems alive after installation.
Case: the 26 August 2026 Bhote Koshi disaster. This run defines the
institutional design constraints for any intervention, state or non-state.

QUESTIONS:
1. Failure-chain diagram for 26 Aug 2026. Nodes: signal generated -> signal
   observed -> transmitted -> interpreted -> authority notified -> decision
   made -> warning sent -> received -> understood -> action taken. Mark each
   node WORKED / PARTIAL / FAILED / UNKNOWN with evidence. (Reported: DHM
   learned by telephone from the Rasuwa District Administration and a
   gauge-station staffer ~20 min after the flood entered Nepal; SMS followed
   within ~16 min of DHM knowing. Verify.)
2. De jure vs de facto - keep these strictly separate. What do the DRRM Act
   2017 and related instruments actually assign to DHM, NDRRMA, district
   administrations, security forces, municipalities, and hydropower
   licensees for detection, alert decision, dissemination, evacuation? And
   who actually held each role on the day?
3. The legal right to warn: do NDRRMA/DHM hold a monopoly on public hazard
   alerts? What civil or criminal exposure does a non-state actor carry for
   a false alarm that causes panic, or a missed event? Treat the answer as
   a binding design constraint on any independent system (alerting
   institutions vs alerting the public are different products).
4. Trigger political economy: who can order evacuation, what a false alarm
   costs that official, and what research says about designing trigger
   authority (including automated triggers) so it actually gets pulled.
5. Funding inventory: active early-warning and disaster-risk projects in
   Nepal - World Bank, ADB, Green Climate Fund, bilateral, Early Warnings
   for All commitments - each named in full with amounts, dates, and what
   it pays for. Where does glacier/GLOF monitoring for Rasuwa/Langtang sit,
   especially post-July 2025?
6. Decay: documented cases of donor-installed systems going dark (sensors,
   telecom bills, batteries, staff turnover); failure-rate estimates from
   WMO/UNDRR/World Bank/academic evaluations; governance designs with
   evidence of 10+ year survival. Who pays recurring costs in each design?
7. Reform record: what concretely changed after the 2024 Kathmandu floods
   and the July 2025 Rasuwa flood - budgets, instruments, staffing - versus
   announcements?

OUTPUT: the marked failure-chain diagram; a de jure vs de facto authority
table; funding inventory; a "why systems die" synthesis with specific
countermeasures and who-pays models. Name sources in full (organization +
title + date). Where responsibility is contested, say contested. Report
obstacles as costs, not verdicts: for every legal or institutional wall,
state what it would take to change it, the interim workaround, and what
remains buildable within it. Finish by filling the common schema table
rows 16-17 plus any others supported.
```

## RUN 5 — The transboundary tiers

```
GOAL: Determine what warning value is achievable at each level of Chinese
cooperation, for hazards sourced in Tibet that kill people in Nepal (case:
the Lhende Khola / Bhote Koshi corridor, floods of July 2025 and 26 August
2026). The organising question is NOT how to fix China-Nepal data sharing;
it is what remains buildable when upstream cooperation is unavailable.

DO NOT begin from the assumption that China possessed actionable information
and failed to transmit it. Test six scenarios against evidence and assign
likelihoods: (1) knew and didn't send; (2) detected but couldn't classify in
time; (3) detected simultaneously with Nepal; (4) neither side had
meaningful warning; (5) had local information Nepal couldn't access; (6) a
warning was technically feasible but politically blocked. Note Chinese
official statements disputing failure-to-warn framing, and casualties on the
Chinese side.

QUESTIONS:
1. What does the post-July-2025 Nepal-China understanding on border
   water-risk data actually contain (official texts/statements from both
   sides), and is there evidence it functioned at all in August 2026?
2. China's data regime: how are hydro-meteorological and border-region
   geospatial data legally classified in China (state-secrecy provisions,
   surveying and mapping law)? What does that legally foreclose - foreign
   instruments, real-time feeds, joint stations?
3. TIER 1 - no Chinese cooperation: satellite observation, global/regional
   seismic and infrasound networks, cross-border remote sensing, sensing at
   the border on Nepali territory, public data, community observation. For
   each: what lead time does it buy for this corridor, alone and combined?
4. TIER 2 - partial cooperation: alert exchange, event-confirmation hotline,
   selective sensor feeds. Precedents where a reluctant upstream state
   shares alerts but not data?
5. TIER 3 - full cooperation: joint monitoring infrastructure, real-time
   upstream networks, joint operating centre. Any precedent for foreign or
   joint instrumentation on Chinese territory, or Chinese real-time (not
   seasonal) hydrological data sharing with any neighbour? Realistic this
   decade?
6. Comparators, each with legal basis, what is shared, latency, and
   performance under political stress: Mekong River Commission; EU EFAS /
   Danube; India-Nepal Kosi and Gandak arrangements (how well do they
   actually perform?); India-China Brahmaputra data arrangement and its
   suspensions; Central Asian GLOF cooperation; Alpine arrangements.
7. Third parties: ICIMOD's actual and possible roles, WMO mechanisms and
   Early Warnings for All, satellite operators. Can a third party
   substitute for bilateral trust, and where has that worked?
8. The persistence doctrine: identify the specific offices, institutes, and
   channels a small team or Nepali institution would petition for upstream
   cooperation (relevant Chinese ministries, Chinese Academy of Sciences /
   Institute of Tibetan Plateau Research groups, embassy channels, ICIMOD
   as broker), what precisely to ask for at Tier 2, and precedents where
   repeated low-odds requests eventually opened a channel. A slim chance of
   reply is a cost of the attempt, not a reason to skip it.

OUTPUT: a tier table showing incremental warning minutes bought at each
cooperation level (connect to detection findings where possible); the
six-scenario assessment with evidence; an honest near-term judgment of the
China channel; a ranked list of Tier-1 pathways. Name sources in full
(organization + title + date). Separate official positions from journalism;
where the record is unknown, say unknown. Report obstacles as costs, not
verdicts: for every wall, state what it would take to break or bypass it,
the interim workaround, and what remains buildable if it never falls.
Finish by filling the common
schema table (especially row 17), evidence grades throughout.
```

## RUN 6 — Target selection: hazard cascades and corridor scoring

```
GOAL: Establish where warning capability would create the most value: the
residual and future hazard of the Bhote Koshi-Trishuli corridor, and a
scored ranking of analogous Himalayan corridors. The output is an
intervention market assessment, not a hazard catalogue.

QUESTIONS:
1. Cascade inventory for this corridor - model hazards as state chains, not
   single events: source instabilities (glaciers, glacial lakes, unstable
   slopes above the Lhende/Bhote Koshi/Trishuli, from ICIMOD
   potentially-dangerous-lake inventories and academic assessments of the
   Langtang region) and their possible transitions (collapse -> avalanche ->
   damming -> breach -> debris flood; GLOF; multi-pulse sequences). Which
   transitions are in principle observable, and where are the detection
   points?
2. Current status: the barrier lake reportedly formed by the 26 Aug 2026
   event (reported rising in the days after - verify current state and
   official handling); any monitoring, satellite tasking, or programs
   announced for this corridor since the disaster.
3. Exposure below, verified: settlements and population in the flood path;
   the hydropower fleet - reported ~12 operating plants (~431 MW) damaged
   and ~15 under construction (~470 MW) affected, verify - plus roads, the
   dry port, tourism volumes. Is more hydropower being planned or built in
   this corridor despite two floods in 13 months?
4. Climate trend: peer-reviewed evidence (ICIMOD HKH assessments, recent
   glaciology) on ice-loss acceleration, permafrost degradation, and
   expected frequency of ice-rock avalanches and GLOFs in the central
   Himalaya. Report ranges, not point claims.
5. Corridor scoring - make the model explicit and show every input:
   risk = hazard probability x exposed population x infrastructure exposure
   x warning difficulty; then score INTERVENTION OPPORTUNITY separately:
   data availability, telecom coverage, accessible safe ground, community
   and institutional receptivity, monitoring access. A maximally dangerous
   valley with no feasible sensing, telecom, or safe ground may be a worse
   target than a slightly less dangerous one where intervention can work.
6. Apply the model: ranked shortlist of "the next Bhote Koshis" across
   Nepal, the Indian Himalaya, Bhutan, Pakistan, and Tibet-border rivers -
   corridors combining unstable ice above with hydropower cascades,
   settlements, or trekking populations below. Show the scoring per
   corridor, with evidence grade per input.

OUTPUT: cascade map with detection points; verified exposure summary;
the scored corridor ranking with visible reasoning and uncertainties; a
best-intervention-market shortlist (which may or may not be Bhote Koshi
itself). Name sources in full (organization + title + date); distinguish
measured from modeled from speculative throughout. Finish by filling the
common schema table where supported.
```

## RUN 7 — Synthesis: the build decision (run last, feed it the other six)

```
ROLE: You are synthesizing six completed research runs into a build decision
for a small, technically capable, non-governmental team (1-3 people,
software-strong, modest budget, no authority over state sensors) considering
whether anything worth building exists in the warning chain for Himalayan
cascading mountain hazards (anchor corridor: Bhote Koshi-Trishuli, Nepal).

INPUT - paste before running:
[PASTE: the filled common schema tables and key findings from Runs 1-6]

THE CHAIN: hazard state -> observable signal -> detection -> classification
-> confidence -> source localization -> propagation/travel time -> alert
trigger -> communication -> comprehension -> movement -> survival.

STAGE 1 - locate the binding constraint. From the assembled tables, identify
where the chain actually breaks today for this corridor: precursor
observability? detection? classification speed? localization? propagation
modeling? trigger authority? channels? movement time? Rank the break points
by expected lives lost attributable to each.

STAGE 2 - derive interventions from the constraints BEFORE reading the
appendix below. For each candidate, state: (a) which chain segment it
repairs; (b) WHAT EXISTING DECISION CHANGES because it exists, and whose
decision ("provides visibility" fails this test; "moves expected evacuation
start from T+20 min to T+3 min" passes); (c) minutes bought, at what
confidence; (d) institutional and political dependencies (schema rows
16-17), respecting the legal-authority findings - if non-state public
alerting carries liability, the product alerts institutions, not the
public; (e) robustness when in-corridor infrastructure fails during the
event; (f) rough cost per additional person receiving >=10 min of
actionable warning, as a range with stated uncertainty; (g) effort estimate
for a 1-3 person team; (h) main failure risk; (i) kill criteria.
Also research here (this run's only fresh research): open-data access
mechanics and latencies (USGS/IRIS-EarthScope real-time seismic feeds and
their coverage of the Nepal-Tibet border zone; Sentinel-1/2 access latency;
DHM public gauge data/APIs); precedents of independent systems becoming
operationally useful to authorities (community seismic networks, volcano
collaborations) and cautionary cases of unofficial alerts causing harm or
being ignored; named groups to consult before building (ICIMOD, DHM,
NDRRMA, Practical Action, active university teams).

STAGE 3 - only now evaluate these candidate seeds against your derived
list; keep, merge, or kill each with reasons: (i) automated watcher on
public seismic feeds flagging mass-movement-like signals in defined
Himalayan border zones, notifying designated institutions; (ii) a
multi-signal fusion engine (seismic anomaly x mapped hazard-source
intersection x signal morphology x anomalous river behavior -> confidence
score -> institutional alert); (iii) satellite-change watchlist over named
hazard sources with automated diffs; (iv) English-language relay of
official alerts to trekking lodges and tour operators; (v) open corridor
hazard dashboard; (vi) last-mile phone-tree/roster software for community
EWS committees.

STAGE 4 - recommend. Choose among outcome classes with evidence: A -
precursor monitoring works, build source monitoring; B - precursors
unreliable but event detection works, build rapid detection + automated
institutional alerting; C - detection exists but classification/fusion is
the gap, build software; D - detection is adequate and response is the
bottleneck, build last-mile/safe-haven capability; E - nothing buys enough
time, the honest answer is siting, zoning, safe havens, and faster
post-event response. Also consider the null-build: the highest-value move
may be making EXISTING signals reach EXISTING institutions ten minutes
faster. Recommending E or the null-build is success, not failure.
Whatever the outcome class, produce a staged path toward the north-star
system (continuous 24/7 monitoring of prioritized sources, automated
movement analysis, autotriggered alerts through the channels people
actually use): for example v0 - capture existing signals and deliver them
to existing institutions minutes faster; v1 - automated event detection
with institutional autotrigger; v2 - continuous monitoring of the top
priority sources; v3 - full corridor live view with public dissemination.
Each stage must be independently valuable and must survive the later
stages never being funded. Obstacles on the path are reported as costs
(what it takes to break them, who could, the interim workaround), never
as verdicts.

OUTPUT: a decision memo (binding constraints ranked; derived candidates
with the nine attributes; seed dispositions; one recommendation with
reasoning and kill criteria) plus the final assembled master schema table.
Name sources in full (organization + title + date). State uncertainty
plainly; do not manufacture confidence the tables don't contain.
```
