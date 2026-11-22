# Adjudication of the External Build Reviews

**29 August 2026. Two independent reviews (ChatGPT with citations; Gemini) of the build plan. This file records what we accept, what we reject, what they found that we missed, and the revised plan. It supersedes the corresponding sections of `one-shot-build-brief.md`, which has been patched.**

---

## 1. ACCEPTED — the lead-time claim was wrong, and it was our error

Both reviewers caught the same thing, and an independent recomputation confirms them.

Verified inputs: Rasuwagadhi's last reading `waterLevelOn` 08:40 NPT; 10-minute cadence; BIPAD ingest lag measured at 5–15 minutes; a 5-minute poller interval; Syabrubesi's gauges last reporting 08:50. Benchmarks: DHM knew by telephone at **09:00**; SMS dispatched at **09:16**.

| Rule | Ingest lag 5 min | Ingest lag 15 min |
|---|---|---|
| N=1, Rasuwagadhi alone | fires 08:55–09:00 | fires 09:05–09:10 |
| **N=2, Rasuwagadhi (the proposed rule)** | **fires 09:05–09:10** | **fires 09:15–09:20** |
| Correlated N=1, two stations | fires 09:05–09:10 | fires 09:15–09:20 |

Against the 09:16 SMS, the proposed N=2 rule buys **−4 to +11 minutes**. Against DHM's actual knowledge at 09:00 it is **worse in every scenario except the most favourable single-station variant**. The "+20 minutes" figure in the brief came from the pre-recon estimate (which assumed alerting on the raw missed poll, before we had measured the 5–15 minute ingest lag) and was never propagated forward when the lag was discovered. That is a straightforward failure to update a headline claim after its input changed, and it is exactly the error we would flag in anyone else's work. Corrected in the brief.

**What neither reviewer said, and what survives the correction.** The 26 August event had an unusually favourable human-observation profile: 08:40 on a clear morning, at a border crossing with a customs post, dry port, police and hundreds of people present. The telephone call was luck, and the Nepali commentary said so. The right question is not "would software have beaten the phone call on 26 August" but "what is the distribution of human-report latency across events" — including night, low season, and upper catchments with nobody in them. Gemini made a version of this point (unwitnessed and nighttime failures); ChatGPT did not. It is the strongest surviving argument for the product, and it is an argument about *variance*, not about this event's mean. Any future pitch must be built on it, and must not repeat the 20-minute claim.

## 2. ACCEPTED — the false-positive replay becomes milestone 0, using ChatGPT's method

Both reviewers demand the retrospective test before further code. Agreed. ChatGPT's methodology is materially better than Gemini's and is adopted:

- Count outage **episodes**, not missing samples. A three-week outage is one episode, not three thousand alarms. Gemini's framing would have produced a meaningless denominator.
- Report **actionable alerts per recipient per week**, not a false-positive percentage. An institution experiences volume, not rates.
- Classify every replayed alert into: isolated single-station dropout / correlated multi-station dropout / genuine hydrological anomaly / known system outage / indeterminate.
- Test outage thresholds at 20, 30, 40 and 60 minutes rather than fixing N=2 by assumption.
- Do not treat the absence of a BIPAD `incident` record as proof a dropout was innocent.

**Acceptance gate (engineering judgment, not an established standard):** more than one unambiguously false *actionable* alert per recipient per 30 days in replay kills the hazard-signal channel in its current design. Both reviewers proposed thresholds in this region; neither has an empirical basis for a specific number, and neither claimed one.

## 3. ACCEPTED, THEN PUSHED FURTHER — the network-health reframe

Both reviewers concluded that the Sentinel should be reframed from flood warning to network health, with hazard escalation only on dual confirmation. Accepted. Two products in the data model, not merely in the prose:

- **NETWORK HEALTH** (primary): "Rasuwagadhi telemetry absent 25 minutes." A maintenance observation. Low priority, digest delivery, `certainty: Observed` about the telemetry and nothing else.
- **HAZARD SIGNAL** (secondary): correlated silence across adjacent stations in one basin, plus anomalous behaviour in a surviving neighbour, plus (where available) seismic corroboration. Higher priority, CAP `certainty: Possible`, explicitly evidence rather than instruction.

Both reviewers treated this reframe as a demotion. It is closer to a promotion, and their own evidence supports it. The corridor's Ghodatalbela station has been dark since **4 August** — three weeks before the disaster, apparently unnoticed by anyone. The sensing layer that every future warning depends on was already degraded and no one knew. A tool that surfaces that has a natural institutional owner, no alert-fatigue problem, no legal exposure, and value on ordinary days rather than only on catastrophic ones. Warning systems die of unpaid telecom bills and dead batteries far more often than of bad algorithms, which is the finding our own governance research produced and then failed to apply to the product design.

## 4. ACCEPTED — the seismic Watcher is parked, not killed

Both reviewers are right that a ~3-minute product is unachievable behind a 30-minute public embargo, and right that the low/high frequency ratio is the feature most likely to fail first at 29–80 km, because distance-dependent attenuation makes a remote earthquake look spectrally landslide-like. That is a real and well-documented effect, and ChatGPT's citations (Provost et al. 2017 random-forest classification of landslide seismicity; Manconi et al. 2016 regional rockslide detection; Rekapalli et al. 2024 on PSD-shape discrimination) are the right literature. The design correction is not to abandon the spectral feature but to make it distance-normalised and multi-station, with PSD shape rather than a single scalar ratio.

Two corrections to the reviews. First, Greg did not attach `watcher_prototype.py`, so both critiques of the code are aimed at a description rather than the file; ChatGPT said so plainly, Gemini did not and criticised an STA/LTA trigger the prototype no longer uses — the first version failed exactly that way in testing and was rebuilt around a noise-floor trigger, with the lesson kept in the comments. Second, "kill" is premature when the kill depends on a price quote nobody has requested. The correct status is **parked pending two emails** (Raspberry Shake pricing; NSSN partnership), with the offline replay harness against Chamoli 2021, Rasuwa 2025 and Bhote Koshi 2026 as the only work that proceeds meanwhile. That harness is worth building regardless: it answers whether the physics works, and it is the artefact that makes the eventual letter to Cook or Petley worth reading.

## 5. REJECTED — Gemini's legal claim

Gemini states the tool risks "potential violation of Nepal's Disaster Risk Reduction and Management Act §24(2) regarding non-authorized alerting." That misreads the provision. §24(2) penalises *false* alarms that cause panic; it is not an authorisation regime, and no licensing requirement for hazard alerting was found in the Act's text during the governance research. An institution-facing tool that relays observations attributively is outside its scope by design. Converting a false-alarm offence into a licensing requirement is a confident legal error of the kind that talks people out of legitimate work.

The genuine caution stands and is unchanged: none of us is a Nepali lawyer, non-state *public* alerting does carry real exposure, and the §31 good-faith immunity covers officials rather than outsiders. The resolution is the same as the sustainability answer — an institutional partner, who has counsel.

## 6. REJECTED — Gemini's invented numbers

"5–15% of stations dropping per day." "Above roughly 5–10% institutional recipients treat a channel as noise." "70–80% probability." None carries a source; all are stated with a precision the underlying evidence cannot support. This is the failure mode the review prompts warned about, arriving on schedule. Discount them entirely. ChatGPT labelled its equivalent estimate as judgment and cited real literature for the alert-fatigue claim, which is the difference between an opinion and a number.

## 7. THE FIND — NAXA, Pahiro Alert, and NSET

The most valuable output of this exercise is not a critique. ChatGPT surfaced three things our own recon missed:

- **Pahiro Alert** (landslide.naxa.com.np) — a community landslide early-warning system built by **NAXA**, a Nepali technology company. Nepali-built, operating, adjacent to exactly what we proposed.
- NAXA also sits in the ecosystem that built the **BIPAD portal** — the API our entire Sentinel depends on. The people who built our data source have already built a hazard-alerting product.
- **NSET** issued a 2026 procurement for a landslide early-warning system including seismometers, telemetry, hosting and up to six years of maintenance — evidence that the "who pays for maintenance" problem is being solved by someone locally, with a budget.
- ICIMOD reportedly ran a 2026 field programme involving seismic stations around Gyirong and Zhangmu. Gyirong is the corridor. **Verify this first**; if accurate, it changes the seismic picture materially.

This answers the parachute critique in the most useful way available: the local capability we should be worried about displacing has a name, a product, and an office in Kathmandu. NAXA becomes the highest-priority new contact, and the first message is not an offer but a question — what do you already have, and would you rather we contributed than competed.

## 8. WHAT ALL THREE OF US MISSED

**The cheapest kill test is an email we were avoiding.** Gemini named it without noticing what it implies: if DHM already runs missed-poll alarms on its own DAQ servers, the Sentinel is redundant on arrival. Nobody outside DHM can answer that. The question Greg was most nervous about asking is the one that could save three months of building, which reorders the nerve calculus entirely — the email is not an audition, it is a search for a reason not to work.

**The highest-leverage act might not be code at all.** A $36.1M GCF programme with DHM as lead is already funding early-warning expansion. Two outsiders with a rigorous seven-run synthesis and a documented three-week-dark station may do more good with a two-page memo to that programme's technical team than with a service they cannot staff. That option was never on the table and should be.

---

## REVISED PLAN

**Posture.** A research demonstrator operated by two people, designed from day one to be handed over. Not a warning service, and never described as one until a named institution owns it, with the handover conditions ChatGPT listed: written operating agreement, funded maintenance line, named primary and secondary operators, runbook, exercise schedule, institutional access to code and infrastructure, and a defined transfer mechanism.

**Order of work.**

0. **Ask before building.** One identical question to NAXA, DHM, ICIMOD, NSET, NSSN and the GCF/UNDP project team: does an operational or research system already detect hydrometric station silence or seismic mass movements and alert institutions, and may we contribute rather than duplicate? This is the lowest-ego email in the pack and it gates everything.
1. **The false-positive replay** on the five-week BIPAD archive, by the method in §2. It kills or validates the hazard channel before another line of production code.
2. **Sentinel as network health**, with the hazard channel behind dual confirmation, CAP output, and a "Sentinel Offline" notice sent to recipients as a first-class safety function rather than ops hygiene.
3. **The offline seismic replay harness** against three real events. No real-time claims until a data path exists.
4. **The expert letters**, with replay results attached.

**Dropped:** the 20-minute lead-time claim; the "~3-minute" seismic product framing; any description of either tool as an early-warning system prior to institutional adoption.

---

# PART II — Adjudication of the Action-Plan Reviews

**Both models reviewed the outreach plan. This part supersedes the corresponding sections of `contacts-and-messages.md`, which has been patched.**

## 9. ACCEPTED WITHOUT RESERVATION — the letter to Dr Kattel is withdrawn

Both reviewers independently identified the same problem, and they are right. The letter asked a Nepali scientist working inside a Chinese Academy of Sciences institute to supply operational thresholds beyond what the published paper contains, to say whether a specific border slope was entering China's instrumented network, and to help construct a technical channel that bypasses foreign ministries — all from an unaffiliated foreign national, about border-region hydrological data, three days after a disaster with casualties on both sides.

State the risk precisely rather than dramatically. We do not know that answering would cause Dr Kattel difficulty; ChatGPT marked this UNKNOWN and was right to, while Gemini's "immense professional danger" and "state security scrutiny" assert as fact something neither model verified. The decisive point does not depend on resolving it: **he should not have to perform that risk assessment on our behalf.** An unsolicited request that requires its recipient to work out whether replying is safe is a cost imposed on him, not a question asked of him.

The letter is withdrawn. The legitimate content survives through a different route: ICIMOD is an intergovernmental body of which both Nepal and China are members, with a documented convening record with ITPCAS and IMHE. Any request touching cross-border operational data goes to ICIMOD and Nepali institutions, and they decide whether and how to approach Chinese counterparts. If Dr Kattel is ever contacted, the first approach concerns published methodology and scientific interpretation only.

**Wider correction, which neither reviewer drew and which matters:** the persistence doctrine from Run 5 is sound advice *for Nepali and regional institutions* — the Brahmaputra channel took sixteen years of official patience. It is not a task two unpaid individuals can or should carry, and casting them as the persistent party was a category error. It stays in the research as a recommendation to institutions; it leaves Greg's task list entirely.

## 10. ACCEPTED — DHM gets evidence, not a proposal

Both reviewers reject the current DHM message, and ChatGPT's reasoning is the sharper one: the draft makes DHM part of our R&D process by asking them to supply the telemetry cadence, which the public BIPAD API already answers. An official in a mass-casualty response should not be asked to help an outsider discover whether an idea works.

The message is rewritten to ask an expert to judge a result rather than entertain a proposal, and it is not sent until that result exists. ChatGPT's proposed opening is adopted almost verbatim because its last clause is the honest and disarming part: *"If it is not, I will stop."*

## 11. ACCEPTED — Nepali actors move to the centre

Both reviewers are right that the list was too international and too top-down, and the combined additions are substantial: NAXA (from Part I), NSET, Kathmandu Living Labs, Tribhuvan University's Central Department of Hydrology and Meteorology and its seismology groups, Nepal's National Seismological Centre, NAST, DPNet-Nepal, Small Earth Nepal, Practical Action Nepal, and the district and municipal emergency operations structures in Rasuwa, Nuwakot and Dhading.

ChatGPT's framing of why is the one to keep: these people are the project's cheapest failure-detection mechanism, not obstacles to route around. And its statement of what would actually distinguish this from parachute technology is better than any assurance we could write — a Nepali institution able to say "don't build this," with the team stopping.

## 12. ACCEPTED — factual corrections before anything is sent

- **Dave Petley is no longer at the University of Hull.** He is reported as Vice-Chancellor and President of Nottingham Trent University. The draft's institutional line is stale.
- **Kristen Cook's current affiliation is uncertain** across sources (IRD / ISTerre / Université Grenoble Alpes in some, GFZ Potsdam in others). Verify before addressing her.
- Parajuli and Joshi's DHM roles check out against DHM's own staff listing.

Verify every name, title and institution on the day of sending. Getting someone's employer wrong in a cold email is a small error that answers the recipient's first question about how carefully you work.

## 13. REJECTED — Gemini's rewrites

Gemini judges the drafts to "undersell by heavily emphasizing the senders' lack of affiliation" and rewrites them into corporate voice: *"We are prototyping an open-source monitoring layer for DHM's telemetry."* That sentence claims a thing that does not exist and implies an organisation that does not exist. It is the precise opposite of ChatGPT's advice in the same round, and ChatGPT is right. An independent researcher who says exactly what he is cannot later be caught having overstated; a two-person project writing as "we are prototyping" invites one search and a permanent loss of credibility. The honest framing stays.

Gemini's own build-review warned that unvalidated foreign software inside a national warning system risks political backlash. Advising the same sender to sound more institutional than he is contradicts that.

## 14. THE REVIEWERS CONTRADICT EACH OTHER ON SEQUENCE — resolution

ChatGPT: contact falsifiers first, because a scientist's one-line reply can kill the classifier and months of engineering are a pure loss. Gemini: build first, because "data is your only viable credential" and an untested idea from an unaffiliated foreigner will not penetrate anyway.

Gemini's argument contains a non-sequitur — *"if you cannot build it independently, you lack the capacity to offer it"* conflates the capacity to build with the capacity to operate, which is the very conflation its own verdict elsewhere tells Greg to avoid. And "the risk of wasting months is irrelevant" is false for a team whose scarcest resource is hours.

The resolution both reviewers half-saw: **the question emails and the pitch emails are different objects.** Asking "does this already exist, and would you tell me if the premise is wrong" costs the recipient a minute and requires no credential at all. Asking an institution to consider adopting software requires a demonstrated result. So: questions now, demonstration next, institutional approach last. That is the revised order in §15, and it was already the direction of travel before either review.

One caution on ChatGPT's suggestion to publish a synthesis within 48–72 hours: bodies are still being recovered and identified. Publication timing is a judgment about the affected, not only about the attention window.

## 15. ACCEPTED, WITH ONE ADDITION — narrow sharply

Both reviewers say cut, and the cuts are correct: the ITPCAS persistence campaign, the tourism/TIMS concept, the hydropower co-funding strategy, the hardware tier, community drill work, and any framing in which the team operates an alerting service. Both are also right that two unpaid part-timers cannot carry life-critical operations, and that the honest posture is a research demonstrator built for handover.

**What both missed, and it changes the shape of the project.** Both reviewed Greg purely as a would-be software builder. He is a working financial journalist with a seven-run, evidence-graded synthesis of a three-day-old disaster, and one genuinely under-reported finding in hand: the corridor's Ghodatalbela gauge went dark on 4 August and nobody noticed, which means the sensing network was already degraded before the flood. A published, carefully sourced piece of journalism carries no maintenance burden, creates no orphaned system, has no parachute problem, requires no institutional permission, and reaches the funders and agencies with budgets more effectively than a prototype from two strangers ever will. It is also the one contribution where being an unaffiliated outsider with research skill is an advantage rather than a liability.

That does not replace the prototype. It reorders which deliverable carries the weight.

**Revised scope — one question, one experiment, one article.**

1. **The question emails** (duplication + falsification), to NAXA, NSET, Kathmandu Living Labs, ICIMOD, Tribhuvan University, NSSN, Stimson, and the vendor. No pitch, no offer, no meeting request beyond a reply.
2. **One falsifiable experiment**: the five-week BIPAD false-positive replay, and the offline seismic replay against three real events. Both answerable in weeks, both able to kill the premise cheaply.
3. **The journalism**, when the timing is decent and the findings are checked.
4. **DHM and NDRRMA last**, with results attached and the single question of whether the failure mode is technically meaningful.

Anything beyond that is deferred until a Nepali institution asks for it.
