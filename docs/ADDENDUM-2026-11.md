# Addendum, 22 November 2026

Everything in `research/`, `proposal/`, `method/` and `review/` was written on **28–29 August 2026**, two and three days after the disaster, and is preserved unaltered. This addendum records what has changed since, so that nothing in this repository is mistaken for a current account. Sources were checked on 22 November 2026.

**Read this before citing any figure from the research files.**

## The casualty figures in the research are badly out of date

The research recorded the toll as of 15:00 NPT on 28 August 2026: **538 dead, 977 missing.** Those were explicitly provisional and labelled as such throughout. The government figures below are taken from UNICEF Nepal's humanitarian situation reports, each of which cites Nepal's National Disaster Risk Reduction and Management Authority (NDRRMA) or "government authorities".

| As of | Dead (Nepal) | Missing (Nepal) | Source |
|---|---|---|---|
| 28 Aug 2026, 15:00 NPT | 538 | 977 | The snapshot used throughout the research |
| 16 Sep 2026 | 1,403 | 6,150 | UNICEF Nepal, "Humanitarian Situation Report No. 4" (16 September 2026) |
| 22 Sep 2026 | 1,451 | 5,705 | UNICEF Nepal, "Humanitarian Situation Report No. 5" (22 September 2026), citing NDRRMA Situation Report #21 |
| 4 Oct 2026 | 1,455 | 5,285 | UNICEF Nepal, "Humanitarian Situation Report No. 6" (5 October 2026) |
| 13 Oct 2026 | 1,458 | 5,285 | UNICEF Nepal, "Humanitarian Situation Report No. 7" (13 October 2026) |

The government ended formal search and rescue on 5 October 2026. The missing count fell between mid-September and early October as records were reconciled, so it should not be read as people being found alive. Other tallies differ at the margins. For example, Nepal's Foreign Minister told the UN General Assembly that more than 1,400 had died and about 6,000 were unaccounted for (as reported in ICIMOD's press release of 25 September 2026). Tibet's figures (43 dead, 519 missing as of 16 September 2026) come from a secondary consolidation and were not checked against a Chinese primary source.

On any of these counts, the deaths are close to three times, and the missing more than five times, the figures the research was written against. Any per-district breakdown in the research files, including the Chitwan and Nawalparasi figures that Run 3 used to probe where people actually died, is a 28 August snapshot.

## What has since been settled

**The cause.** ICIMOD's "Kyirong-Rasuwa Flood 2026" page (published 28 August, updated 14 October 2026) describes a rock and ice mass falling about 1,200 m from the north face of Langtang Lirung into the Lhende Khola and becoming a debris flow. It places the trigger on the Nepali side and says the event was not a glacial lake outburst in the technical sense. Run 1's hypothesis H2 was correct. Two details remain open in the sources: the same page notes a rapid analysis suggesting failure on 25 August (which would imply a temporary dam), and reported magnitudes for the 08:37 seismic signal differ (4.4 from Nepal's Department of Mines and Geology, as reported by OnlineKhabar on 27 August 2026; an earlier draft of this addendum gave Ms 5.2 without a traceable source).

**The gauges.** The Flood Forecasting Division's technical report, as reported in OnlineKhabar's "Technical report details Bhotekoshi flood's journey from Tibet to Devghat" (27 August 2026), gives this sequence:

- 08:37: seismic signal recorded
- 08:50: the Bhotekoshi–Syafrubesi station stops transmitting; its last reading, at 08:40, was 1.62 m against a 6 m warning level
- 09:00: the Division hears of the flood by telephone, from the Rasuwa District Administration Office and staff at the Betrawati station
- 09:15–09:16: first SMS warnings, 679,295 messages along the corridor to Muglin
- 09:20: the Betrawati station stops transmitting

The first instrumental sign of the flood on Nepal's side was a gauge going silent. Setopati's "Government installs VSAT camera in Timure to monitor Bhotekoshi after flood" (3 September 2026) reports that the Rasuwagadhi, Syafrubesi and Betrawati stations were swept away, that they could not be restored immediately, and that the Flood Forecasting Division installed a camera at Timure as a stopgap. The gauge monitor in this repository found all three still without readings on 22 November 2026.

This sequence does not overturn the review's corrected estimate in `review/review-adjudication.md` that a dead-station alarm would have bought −4 to +11 minutes. That estimate already allows for the 5–15 minute delay before DHM's feed shows a missed reading.

## Institutional developments since the research

1. **Government expert committee.** On 16 September 2026 Nepal's Ministry of Energy, Water Resources and Irrigation formed a seven-member committee, coordinated by water policy expert Devesh Belbase, with members covering hydrology, glaciology, remote sensing, geology, hydropower infrastructure and disaster risk reduction (OnlineKhabar, "Expert panel formed to scientifically study Rasuwa Flood", 16 September 2026). It was given two months to report. No published report was found on 22 November 2026.
2. **Kathmandu 10 Action Points.** Agreed at a workshop on 15–17 September 2026 convened by ICIMOD, NDRRMA and the Embassy of Switzerland, and published in ICIMOD's press release "Kathmandu 10 Action Points: HKH countries chart a path to better preparedness after catastrophic Rasuwa-Gyirong flood" (25 September 2026). The points closest to this project are redesigning early-warning triggers for sudden-onset hazards (point 1), moving cross-border cooperation from raw data to decision-ready information (point 3), and a shared cross-agency data platform (point 8). The release does not mention river gauges or monitoring whether existing stations are working. It overlaps the build brief's aims but does not commit to the dead-station alarm specifically.
3. **Academic work.** Acharya and Paudel's preprint "The Bhote Koshi–Trishuli flash flood of 26 August 2026, Rasuwa, Nepal: warning latency exceeded flood travel time" (EarthArXiv, 2026) reaches the conclusion this research reached, and is cited in a peer-reviewed paper in the Journal of Earth System Science. Its full text could not be retrieved for this addendum. Anyone writing about this project should read it first and should not claim the latency finding as original.

## What this means for the repository

The research stands as a **time-stamped analytical record**: what could be established from public sources within 72 hours of a disaster, and a method for doing that. It is not a current account of the event, and the build recommendations were written before the expert committee and the Kathmandu 10 Action Points existed.

Nothing in `proposal/` was built as specified, and `proposal/watcher_prototype.py` has never been validated. The gauge monitor at the root of this repository was built later, in November 2026, and is deliberately narrower than the build brief: it watches DHM's public feed and sends no alerts. No institution has been contacted.
