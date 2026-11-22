# Research behind the monitor

Written **28–29 August 2026**, two and three days after the Bhote Koshi–Trishuli flood, and preserved unaltered. This is the evidence base the monitor in this repository was built on. It is not a current account of the event.

**Before citing any figure here, read [`ADDENDUM-2026-11.md`](ADDENDUM-2026-11.md).** The research was written against a toll of 538 dead and 977 missing. By 5 October 2026, when search and rescue ended, it was at least 1,455 dead and 5,285 missing in Nepal.

## Contents

| Path | What it is |
|---|---|
| [`research/`](research/) | Seven research runs: event forensics and a counterfactual warning clock; detection and classification judged on operational record; what warning minutes are worth downstream; Nepal's warning governance and why systems decay; what is achievable at each level of Chinese cooperation; hazard cascades and comparable corridors; and the synthesis |
| [`method/`](method/) | The prompt packs that structured the research, and the adversarial-review design used to attack its conclusions |
| [`review/`](review/) | What survived outside critique, and what did not — including a correction of this project's own central error |
| [`proposal/`](proposal/) | The pre-build specification, the verified data-source reconnaissance, and an unvalidated seismic prototype |

## How this relates to the monitor

The research identified gauge silence as the signal nobody was watching for, and the monitor on the `main` branch is the narrow, honest version of that: network health first, no public alerting, thresholds labelled as assumptions. Two things the research got wrong or incomplete, now superseded by the working code:

- `proposal/tech-stack.md` recommends Nepal's BIPAD portal API as the data source. The monitor reads DHM's flood-monitoring page directly instead, which is the better source and the one actually in production.
- `proposal/one-shot-build-brief.md` states that nothing has been built. That was true when written.

The research also claimed, before correction, that a dead-station alarm would have bought roughly 20 minutes of warning on 26 August. Recomputed against measured data lag, the figure is −4 to +11 minutes. `review/review-adjudication.md` records how that error happened: it was calculated before the lag was measured and was never updated afterwards.

## Reading order

`research/run7-synthesis-build-decision.md` first for the conclusions, then `review/review-adjudication.md` for what outside critique did to them. `research/run1-forensics-warning-clock.md` holds the minute-by-minute reconstruction.
