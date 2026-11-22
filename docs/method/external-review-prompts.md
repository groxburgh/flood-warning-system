# External Review Prompts — ChatGPT and Gemini

Four sessions: Prompt A (build critique) and Prompt B (action-plan critique), run once in each model. The prompt text is identical across models; a short tailoring note follows each. Read "Before you paste anything" first — it contains two warnings that determine whether these reviews are worth anything.

---

## Before you paste anything

**1. Neither model knows this event happened.** The Bhote Koshi disaster is three days old. Both models' training data almost certainly predates it. Expect one of three failure modes: flat denial that the event occurred, confident invention of details that never happened, or silent conflation with the 2021 Chamoli or 2023 Sikkim disasters. Both prompts below instruct the model to treat the attached files as the factual record and to flag rather than fill gaps — do not remove that instruction. If a model tells you something factual about the event that is not in your files, treat it as fabricated until you verify it yourself.

**2. Two LLMs are not two independent opinions.** They share training corpora, share a pull toward agreeable answers, and share a tendency to produce fluent, generic disaster-technology advice. If both come back enthusiastic, that tells you about the models, not about the plan. What genuinely counts as independent verification here is a domain expert — which is one more argument for the Cook and Petley emails, since neither model can tell you whether minute-scale seismic discrimination works on the stations that actually exist near Langtang.

**3. Use the disagreements, not the verdicts.** The value in this exercise sits in the specific objection you have not already thought of. When a model raises something the seven research runs already answered, that is noise. Keep a running list of only the objections that survive checking against the files.

---

## PROMPT A — Build critique

**Attach:** `one-shot-build-brief.md`, `tech-stack.md`, `watcher_prototype.py`, `run7-synthesis-build-decision.md`, `run2-detection-classification-engineering.md`

```
You are reviewing a technical plan that, if it is wrong, wastes the time of two
people and — worse — could give a national disaster agency false confidence in a
warning tool that does not work. Review it as the engineer who will be held
responsible when it fails.

Do not open with praise or a summary of what you have read. Start with your
strongest objection.

IMPORTANT — FACTUAL GROUND RULES. This concerns a disaster that occurred on 26
August 2026 on the Nepal-Tibet border. Your training data almost certainly
predates it. The attached files are the factual record for this review. Do not
supply details of the event from memory; if you find yourself recalling
something about it, you are probably confusing it with the 2021 Chamoli or 2023
Sikkim disasters. Where you need a fact the files do not contain, write
"UNKNOWN — would need to verify" rather than filling the gap. If you have web
search, use it to check technical claims (API behaviour, station availability,
library capabilities, published methods) and say explicitly which claims you
verified and which you did not.

CONTEXT IN BRIEF. On 26 August 2026 a rock-ice avalanche near Langtang Lirung
dammed the Lhende Khola on the Nepal-Tibet border; the dam breached and the
resulting debris flood killed 500+ people down the Bhote Koshi and Trishuli
valleys. Three things failed. The collapse's seismic signal was on public global
networks within minutes but was catalogued as an M4.4 earthquake and only
reclassified as an M5.2 landslide hours later. Every river gauge in the corridor
was destroyed by the flood BELOW its warning threshold, so the threshold-based
alerting never fired; the gauges died in downstream order (Rasuwagadhi 08:40,
Syabrubesi 08:50, Betrawati 09:20) and nothing was watching for that silence.
Nepal's flood office learned of the disaster by telephone at 09:00, 23 minutes
in, from people who saw it, and then dispatched 679,295 SMS by 09:16 — a
dissemination system that works.

THE PROPOSAL. A team of two (software-strong, unpaid, part-time, based outside
Nepal) proposes two tools, both alerting institutions only and never the public:
(1) "Station Sentinel" — watches Nepal's public river-gauge telemetry via the
BIPAD REST API for silent stations and anomalous rises, alerting the Department
of Hydrology and Meteorology and NDRRMA; (2) "Mass-Movement Watcher" — watches
seismic feeds and discriminates mass movements from earthquakes by signal
duration, onset emergence and spectral character, alerting the same recipients.
The attached files contain the full brief, verified data-source reconnaissance,
and a working prototype of the seismic discriminator that currently passes only
a synthetic test.

ANSWER THESE, IN THIS ORDER.

1. THE PREMISE. The Sentinel's core claim is that a river gauge going silent is
   an actionable flood signal. State the strongest case against that claim.
   Specifically: in a monsoon country with intermittent power and telemetry, how
   often will stations go silent for boring reasons, and at what false-positive
   rate does an institutional recipient stop reading the alerts? The team has 5
   weeks of retained history available to measure this. Design the specific
   analysis they should run before writing another line of code, including what
   result would kill the product.

2. THE COUNTERFACTUAL ARITHMETIC. The team claims a "two consecutive missed
   10-minute samples" rule on the border gauge, given a measured 5-15 minute
   ingest lag, would have alerted at roughly 09:05-09:15 on 26 August, versus
   the actual 09:16 SMS. Check that arithmetic against the timeline and the lag
   measurements in the files. Is the claimed lead time real, marginal, or an
   artefact of favourable assumptions? If marginal, does the product still have
   a rationale, and what is it?

3. THE SEISMIC PRODUCT'S VIABILITY. The nearest useful community seismometer is
   ~29 km from the source; its public data feed is deliberately embargoed by 30
   minutes; real-time access requires either a paid agreement or a partnership
   with the school network that hosts the stations. Assess honestly whether a
   ~3-minute alert product is achievable, and if the answer is no, whether the
   fallback (rapid post-event characterisation at T+35 minutes) has any value at
   all or is a consolation prize the team should drop. Separately: review the
   discriminator in watcher_prototype.py. Which of its three features (duration,
   onset emergence, low/high frequency ratio) will fail first on real waveforms
   at 29-80 km, and what does the published literature on landslide seismic
   discrimination say the team has got wrong?

4. DUPLICATION. Name who is likely already building this. ICIMOD, the Department
   of Hydrology and Meteorology, a $36.1M Green Climate Fund programme, academic
   groups, and commercial vendors are all active in this space. What is the
   realistic probability that these two tools already exist in some form, and
   how should the team check cheaply before investing months?

5. SUSTAINABILITY, APPLIED TO THEMSELVES. The team's own research documents that
   Nepal's Tsho Rolpa warning system has died twice in 25 years for want of
   maintenance. Two unpaid part-time people outside the country now propose to
   run 24/7 monitoring infrastructure. Make the case that this project becomes
   the thing it criticises, and specify what structural commitment (not
   intention) would have to exist for it not to.

6. HARM. Describe the realistic paths by which these tools make things worse
   rather than better — including alert fatigue at the receiving institution,
   displacing attention from better-funded fixes, a false negative during a real
   event after institutions have come to rely on the tool, and the political
   consequences of a foreign-built alerting layer inside a national system.

7. VERDICT. Choose one: BUILD AS SPECIFIED / BUILD WITH THE CHANGES YOU NAME /
   BUILD ONLY ONE OF THE TWO (say which) / DO NOT BUILD, and give the reasoning
   in under 150 words. If your verdict is to build, name the single test that
   should kill the project if it fails, and say what evidence would change your
   verdict in either direction.

FORMAT. No preamble. Number your answers. Mark every substantive claim as
VERIFIED (you checked a source this session, name it), FROM THE ATTACHED FILES,
or MY JUDGMENT. End with the three changes you would make, ranked by how much
they reduce the chance of the project failing.
```

**Tailoring.** For ChatGPT, add at the end: *"Think carefully before answering; I would rather wait for a considered response than receive a fast one."* For Gemini, add: *"Use search to verify the technical claims about the BIPAD API, Raspberry Shake data policy, ObsPy and SeisBench capabilities, and the landslide-seismic-discrimination literature. Report what you could not verify."*

---

## PROMPT B — Action-plan critique

**Attach:** `contacts-and-messages.md`, `run7-synthesis-build-decision.md`, `run4-governance-liability-decay.md`, `run5-transboundary-tiers.md`, `run3-last-mile-survival.md`

```
You are reviewing an outreach and strategy plan drafted by an outsider to the
disaster-management field who intends to contact government agencies, scientists
and research institutes about a fatal disaster that happened three days ago.
Review it as someone whose job is to protect the recipients of these messages
from wasted time, and to protect the sender from a self-inflicted mistake.

Do not open with praise or a summary. Start with your strongest objection.

IMPORTANT — FACTUAL GROUND RULES. This concerns a disaster that occurred on 26
August 2026 on the Nepal-Tibet border. Your training data almost certainly
predates it. The attached files are the factual record. Do not supply details of
the event from memory. Where you need a fact the files do not contain, write
"UNKNOWN — would need to verify" rather than filling the gap. If you have web
search, use it to check institutional facts (who holds what mandate, what
programmes are funded, whether the named people hold the roles claimed) and say
which claims you verified.

CONTEXT IN BRIEF. On 26 August 2026 a glacier collapse on the Nepal-Tibet border
produced a debris flood that killed 500+ people in Nepal's Rasuwa, Nuwakot and
Dhading districts. A seven-part research synthesis (attached in part) concluded
that the failure was concentrated in detection and classification rather than
dissemination, and that two small pieces of institution-facing software could
close part of the gap. The sender is an independent journalist and content
consultant based in Seoul, with no institutional affiliation in this field and
no prior relationship with any recipient. He intends to work on this with his
brother, a software developer. Both have full-time commitments elsewhere. The
attached file contains six drafted messages and a proposed sequence.

ANSWER THESE, IN THIS ORDER.

1. THE DHM MESSAGE. Nepal's flood forecasting office is currently running a mass
   casualty response. The plan includes an unsolicited message offering to build
   software for them. Argue the case that sending this at all — now or in six
   weeks — imposes a cost on people who cannot afford it, and say what would
   have to be true for the message to be worth a busy official's attention.
   Then, if you would send it, rewrite the opening paragraph to be worth 30
   seconds of their time.

2. THE CHINA LETTER. The plan includes writing to a Nepali scientist working at
   a Chinese Academy of Sciences institute, asking him to help obtain
   early-warning methodology and advocate for cross-border data sharing.
   Consider whether an unsolicited approach from a foreign national could create
   professional or personal difficulty for the named recipient, given the
   subject touches border-region hydrological data. If there is any such risk,
   say so plainly and propose a safer route to the same goal. Do not soften this
   answer.

3. TONE AND STANDING. Read the six drafted messages as their recipients would.
   Where do they overclaim, presume, or read as someone auditioning? Where do
   they undersell in a way that gets them deleted? Flag any sentence that a
   working scientist or civil servant would find naive, and rewrite the three
   worst offenders.

4. SEQUENCE. The current plan is: send two low-stakes emails (a vendor, a
   schools network) now, build until a working demonstration exists, then send
   the expert and institutional messages with results attached. Critique that
   ordering. Consider specifically whether building first risks the team
   investing months in something an expert could have killed in one reply, and
   whether the open post-disaster attention window (which the research suggests
   closes fast) argues for moving sooner.

5. WHO IS MISSING. Name the people, organisations and categories of actor absent
   from the contact list who would materially change this project's odds.
   Include anyone who could kill it early and cheaply, which is a service.
   Nepali-led organisations and individuals specifically: the plan is thin on
   them, and an outsider building tools for a country he does not live in should
   have Nepali partners at the centre rather than the periphery.

6. THE PARACHUTE PROBLEM. Two foreigners with no local presence propose to build
   warning infrastructure for Nepali institutions. Make the strongest version of
   the critique that this is well-meant outsider tech that will not be adopted,
   should not be adopted, or displaces local capability — and then say what
   would distinguish this effort from that pattern in practice, not in framing.

7. CAPACITY. Both participants are busy and unpaid. The plan requires sustained
   correspondence, ongoing operations, and a multi-year persistence campaign
   with a Chinese institute. Assess whether the scope is honest about what two
   part-time people can carry, and specify what to cut so that what remains
   actually survives.

8. VERDICT. Choose one: PROCEED AS PLANNED / PROCEED WITH THE CHANGES YOU NAME /
   NARROW SHARPLY (say to what) / DO NOT PROCEED, in under 150 words. Say what
   evidence would change your verdict.

FORMAT. No preamble. Number your answers. Mark every substantive claim as
VERIFIED (checked this session, name the source), FROM THE ATTACHED FILES, or MY
JUDGMENT. End with the three changes ranked by impact, and one sentence on the
single largest risk the sender appears not to have noticed.
```

**Tailoring.** For ChatGPT, add: *"Take your time; a considered answer beats a fast one."* For Gemini, add: *"Use search to verify the institutional and legal claims — Nepal's DRRM Act provisions on false alarms, the mandates of DHM and NDRRMA, current funded early-warning programmes in Nepal, and whether the named individuals hold the roles described. Report what you could not verify."*

---

## Reading the responses

Keep a single sheet with three columns: the objection, whether the attached files already answer it, and what it would cost to act on. Anything the files already answer is discarded without argument. Anything new gets checked before it changes the plan, because a confident LLM objection is not evidence.

Watch for four specific failure patterns in what comes back. Invented facts about the disaster, which the ground rules should suppress but will not eliminate. Generic disaster-technology advice that would apply to any project in any country, which is filler. Sycophantic agreement dressed as critique ("your instinct here is excellent, though you might consider..."), which is worth nothing. And the reverse failure, reflexive discouragement of an unaffiliated builder, which is a real bias in these models and is not the same as a technical objection — weigh it only where it comes attached to a specific mechanism of failure.

If either model produces an objection that survives checking and that materially changes what gets built, that is the exercise paying for itself. One or two is a good outcome. If you get none, the plan is probably not wrong, but it is also probably not yet tested — and the test that counts is still a reply from someone who has actually deployed a warning system in mountain terrain.
