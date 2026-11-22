#!/usr/bin/env python3
"""
MASS-MOVEMENT WATCHER — starter prototype
==========================================
Companion to one-shot-build-brief.md (Product 2). Runs OFFLINE on synthetic
waveforms so the classification logic can be developed and understood before
touching real data. The discriminants implemented here are the ones the
operational Sedongpu system (Yang et al., NHESS 23:3015, 2023) and the Chamoli
literature (Cook et al., Science 2021) say matter:

  1. DURATION   — a collapse/debris flow radiates for minutes; an M4-5
                  earthquake radiates for ~1 minute or less.
  2. EMERGENCE  — earthquakes begin with an impulsive P arrival; mass
                  movements ramp up gradually.
  3. SPECTRUM   — at regional distance, mass-movement signals are relatively
                  enriched in low frequencies (long low-frequency coda).

THE GO/NO-GO GATE (from the build brief): before building anything else,
swap the synthetic events for the three real reference events + ~20 regional
earthquake controls via fetch_real_waveforms() below, and demand correct
classification of all three within 3 simulated minutes of data availability.

Dependencies: numpy only (pip install numpy). Real-data path needs obspy.
Usage: python3 watcher_prototype.py
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass

RNG = np.random.default_rng(42)
FS = 20.0  # sample rate (Hz) — typical for regional broadband channels (BH*)


# ----------------------------------------------------------------------------
# 1. SYNTHETIC EVENTS (replace with real waveforms at the go/no-go gate)
# ----------------------------------------------------------------------------

@dataclass
class Event:
    name: str
    truth: str          # "EARTHQUAKE" or "MASS_MOVEMENT"
    data: np.ndarray    # single-channel velocity trace, arbitrary units
    fs: float = FS


def _noise(n: int, level: float = 1.0) -> np.ndarray:
    """Band-limited background noise (microseism-ish)."""
    white = RNG.normal(0, level, n)
    kernel = np.hanning(int(FS))  # ~1 s smoothing -> reddened spectrum
    return np.convolve(white, kernel / kernel.sum(), mode="same")


def _envelope(n: int, onset: int, rise: float, fall: float) -> np.ndarray:
    """Asymmetric event envelope: rise/fall in samples (exponential ramps)."""
    env = np.zeros(n)
    t = np.arange(n - onset, dtype=float)
    env[onset:] = (1 - np.exp(-t / rise)) * np.exp(-t / fall)
    return env


def make_earthquake(mag_scale: float = 30.0, dur_s: float = 55.0) -> np.ndarray:
    """Impulsive onset, short duration, higher-frequency content."""
    n = int(600 * FS)  # 10-minute window
    onset = int(120 * FS)
    env = _envelope(n, onset, rise=0.4 * FS, fall=(dur_s / 4) * FS)  # sharp rise
    carrier = RNG.normal(0, 1, n)
    # Earthquake energy concentrated 1-8 Hz at regional distance
    from numpy.fft import irfft, rfft, rfftfreq
    spec = rfft(carrier)
    f = rfftfreq(n, 1 / FS)
    shape = np.exp(-((f - 4.0) ** 2) / (2 * 2.5 ** 2))
    carrier = irfft(spec * shape, n)
    carrier /= np.abs(carrier).max()
    return _noise(n) + mag_scale * env * carrier


def make_mass_movement(mag_scale: float = 18.0, dur_s: float = 210.0) -> np.ndarray:
    """Emergent onset, minutes-long duration, low-frequency enriched."""
    n = int(600 * FS)
    onset = int(120 * FS)
    env = _envelope(n, onset, rise=15.0 * FS, fall=(dur_s / 2.2) * FS)  # slow rise
    carrier = RNG.normal(0, 1, n)
    from numpy.fft import irfft, rfft, rfftfreq
    spec = rfft(carrier)
    f = rfftfreq(n, 1 / FS)
    shape = np.exp(-((f - 1.0) ** 2) / (2 * 1.2 ** 2))  # energy hugs 0.3-3 Hz
    carrier = irfft(spec * shape, n)
    carrier /= np.abs(carrier).max()
    return _noise(n) + mag_scale * env * carrier


def synthetic_catalog(n_eq: int = 20, n_mm: int = 8) -> list[Event]:
    events = []
    for i in range(n_eq):
        events.append(Event(
            name=f"synthetic_quake_{i:02d}", truth="EARTHQUAKE",
            data=make_earthquake(mag_scale=RNG.uniform(15, 60),
                                 dur_s=RNG.uniform(35, 90))))
    for i in range(n_mm):
        events.append(Event(
            name=f"synthetic_collapse_{i:02d}", truth="MASS_MOVEMENT",
            data=make_mass_movement(mag_scale=RNG.uniform(8, 40),
                                    dur_s=RNG.uniform(150, 340))))
    RNG.shuffle(events)
    return events


# ----------------------------------------------------------------------------
# 2. DETECTION
# ----------------------------------------------------------------------------
# LESSON LEARNED (kept on purpose): the first version of this file used a
# classic short-window STA/LTA (2 s / 60 s) as the trigger, and the synthetic
# replay missed most mass movements. Emergent, minutes-long signals defeat a
# naive STA/LTA because the long-term average climbs along with the signal —
# the ratio never spikes. This is a known operational problem; real systems
# either FREEZE the LTA once the ratio starts rising, or (as at Sedongpu)
# trigger on absolute amplitude vs a pre-event noise floor. The replay here
# uses the noise-floor method; sta_lta() is kept below because a live system
# should run both (with LTA freezing) for redundancy.

def sta_lta(x: np.ndarray, fs: float, sta_s: float = 10.0,
            lta_s: float = 180.0) -> np.ndarray:
    """STA/LTA on the squared trace. For live use, freeze the LTA while the
    ratio exceeds ~2 so emergent signals cannot drag the baseline up."""
    p = x ** 2
    sta_n, lta_n = int(sta_s * fs), int(lta_s * fs)
    sta = np.convolve(p, np.ones(sta_n) / sta_n, mode="same")
    lta = np.convolve(p, np.ones(lta_n) / lta_n, mode="same")
    lta[lta < 1e-12] = 1e-12
    ratio = sta / lta
    ratio[: lta_n] = 1.0
    return ratio


def _runs(mask: np.ndarray, bridge: int) -> list[tuple[int, int]]:
    """Contiguous True runs in mask, merging gaps shorter than `bridge`."""
    runs, start, in_run = [], 0, False
    for i, a in enumerate(mask):
        if a and not in_run:
            start, in_run = i, True
        elif not a and in_run:
            runs.append([start, i]); in_run = False
    if in_run:
        runs.append([start, len(mask)])
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < bridge:
            merged[-1][1] = r[1]
        else:
            merged.append(r)
    return [tuple(r) for r in merged]


# ----------------------------------------------------------------------------
# 3. DISCRIMINANTS
# ----------------------------------------------------------------------------

def measure(ev: Event, snr_trigger: float = 4.0) -> dict | None:
    """Detect the first event via envelope vs pre-event noise floor and return
    the three discriminants, or None if nothing crosses the trigger.

    Live-operation note: the replay assumes the first 60 s of the window are
    pre-event (true for event-feed-triggered pulls, which is how the watcher
    is invoked). A continuously running detector must instead maintain a
    trailing noise floor that FREEZES while any trigger condition is active.
    """
    x, fs = ev.data, ev.fs

    # Smoothed amplitude envelope (5 s smoothing).
    env = np.abs(x)
    smooth_n = int(5 * fs)
    env = np.convolve(env, np.ones(smooth_n) / smooth_n, mode="same")

    # Noise floor from the first 60 s (pre-event by construction here).
    noise_floor = float(np.median(env[: int(60 * fs)])) or 1e-12

    # Trigger: envelope above snr_trigger x noise floor for >= 5 s (debounce).
    above_trig = env > snr_trigger * noise_floor
    trig_runs = [r for r in _runs(above_trig, bridge=int(10 * fs))
                 if (r[1] - r[0]) >= int(5 * fs)]
    if not trig_runs:
        return None
    t0 = trig_runs[0][0]

    # -- DURATION: the above-noise run (at a gentler 3x threshold) containing
    #    the trigger, with sub-10 s dips bridged so envelope wobble doesn't
    #    split one event into fragments.
    above_dur = env > 3.0 * noise_floor
    dur_s = 0.0
    for start, end in _runs(above_dur, bridge=int(10 * fs)):
        if start <= t0 < end:
            dur_s = (end - start) / fs
            t_start, t_end = start, end
            break
    else:
        t_start, t_end = t0, min(t0 + int(60 * fs), env.size)
        dur_s = (t_end - t_start) / fs

    # -- EMERGENCE: amplitude in the first 5 s of the event vs its peak.
    #    Impulsive earthquakes are near peak almost immediately (ratio -> 1);
    #    emergent mass movements ramp for tens of seconds (ratio << 1).
    early = env[t_start: t_start + int(5 * fs)].max()
    peak = env[t_start: t_end].max()
    emergence = float(early / peak) if peak > 0 else 1.0

    # -- SPECTRUM: energy below 2 Hz vs 2-8 Hz over the event window.
    from numpy.fft import rfft, rfftfreq
    seg = x[t_start: t_end]
    spec = np.abs(rfft(seg)) ** 2
    f = rfftfreq(seg.size, 1 / fs)
    low = spec[(f >= 0.3) & (f < 2.0)].sum()
    high = spec[(f >= 2.0) & (f < 8.0)].sum()
    lf_ratio = float(low / (high + 1e-12))

    return {"trigger_s": t0 / fs, "duration_s": dur_s,
            "emergence": emergence, "lf_ratio": lf_ratio}


# ----------------------------------------------------------------------------
# 4. CLASSIFIER — transparent scoring, tune every threshold at the gate
# ----------------------------------------------------------------------------

def classify(m: dict) -> tuple[str, float, list[str]]:
    """Return (label, score in [0,1] toward mass movement, reasons)."""
    reasons, score = [], 0.0
    if m["duration_s"] >= 120:
        score += 0.5; reasons.append(f"duration {m['duration_s']:.0f}s >= 120s")
    elif m["duration_s"] >= 90:
        score += 0.25; reasons.append(f"duration {m['duration_s']:.0f}s (90-120s)")
    else:
        reasons.append(f"duration {m['duration_s']:.0f}s (earthquake-like)")
    if m["emergence"] < 0.35:
        score += 0.3; reasons.append(f"emergent onset ({m['emergence']:.2f})")
    else:
        reasons.append(f"impulsive onset ({m['emergence']:.2f})")
    if m["lf_ratio"] > 2.0:
        score += 0.2; reasons.append(f"low-freq enriched (LF/HF {m['lf_ratio']:.1f})")
    else:
        reasons.append(f"LF/HF {m['lf_ratio']:.1f}")
    if score >= 0.6:
        return "MASS_MOVEMENT", score, reasons
    if score >= 0.35:
        return "AMBIGUOUS", score, reasons
    return "EARTHQUAKE", score, reasons


# ----------------------------------------------------------------------------
# 5. REPLAY HARNESS
# ----------------------------------------------------------------------------

def replay(events: list[Event]) -> None:
    tp = fp = fn = tn = amb = miss = 0
    print(f"{'event':<26} {'truth':<14} {'call':<15} {'score':>5}  evidence")
    print("-" * 110)
    for ev in events:
        m = measure(ev)
        if m is None:
            miss += 1
            print(f"{ev.name:<26} {ev.truth:<14} {'NO TRIGGER':<15}")
            continue
        label, score, reasons = classify(m)
        mark = ""
        if label == "AMBIGUOUS":
            amb += 1
        elif label == "MASS_MOVEMENT" and ev.truth == "MASS_MOVEMENT":
            tp += 1
        elif label == "MASS_MOVEMENT" and ev.truth == "EARTHQUAKE":
            fp += 1; mark = "  <-- FALSE ALARM"
        elif label == "EARTHQUAKE" and ev.truth == "MASS_MOVEMENT":
            fn += 1; mark = "  <-- MISSED EVENT (the bad one)"
        else:
            tn += 1
        print(f"{ev.name:<26} {ev.truth:<14} {label:<15} {score:>5.2f}  "
              f"{'; '.join(reasons)}{mark}")
    print("-" * 110)
    print(f"true mass movements caught: {tp} | false alarms: {fp} | "
          f"MISSED mass movements: {fn} | quakes passed: {tn} | "
          f"ambiguous: {amb} | no trigger: {miss}")
    print("\nOperational benchmark (Sedongpu, Tibet, 2022): ~25% false alarms "
          "at threshold, ZERO missed major events.\nTune thresholds so that "
          "fn == 0 first; only then minimize fp. A missed collapse is the "
          "failure mode\nthat kills people; a false 'check now' to an "
          "institution is survivable one time in four.")


# ----------------------------------------------------------------------------
# 6. REAL DATA — the go/no-go gate (run on your own machine, needs obspy)
# ----------------------------------------------------------------------------

def fetch_real_waveforms():
    """
    NOT called by default. Swap this in for the synthetic catalog to run the
    go/no-go gate from the build brief. Sketch (verify station availability —
    Nepal's national network is not public; use openly federated stations):

        from obspy.clients.fdsn import Client
        from obspy import UTCDateTime

        client = Client("IRIS")
        # Reference event 1 — Bhote Koshi collapse, 26 Aug 2026
        # (USGS event us7000tbwb, origin ~2026-08-26T02:52:10 UTC; verify on
        #  the USGS event page and correct before use)
        t0 = UTCDateTime("2026-08-26T02:45:00")
        st = client.get_waveforms(network="IU", station="LSA", location="00",
                                  channel="BHZ", starttime=t0,
                                  endtime=t0 + 1800)
        st.detrend().filter("bandpass", freqmin=0.3, freqmax=8.0)
        tr = st[0]
        ev = Event(name="bhotekoshi_2026", truth="MASS_MOVEMENT",
                   data=tr.data.astype(float), fs=tr.stats.sampling_rate)

    Reference events to assemble:
      - 26 Aug 2026 Bhote Koshi (truth: MASS_MOVEMENT)
      - 08 Jul 2025 Rasuwa outburst (truth: MASS_MOVEMENT — weaker seismic
        source; it may not trigger, which is itself a finding)
      - 07 Feb 2021 Chamoli, ~05:21 UTC (truth: MASS_MOVEMENT; literature
        reports detection at stations up to ~100 km)
      - ~20 ordinary M4-5.5 earthquakes from the same region/years
        (truth: EARTHQUAKE) pulled from the USGS FDSN event API as controls.

    Gate: all three mass movements classified correctly within 3 simulated
    minutes of first data availability, zero of them missed, and a false-alarm
    rate on the controls you would be willing to defend to DHM. If the gate
    fails after honest tuning: stop, write down why, tell Greg. That outcome
    is a success of the process, not a failure of yours.
    """
    raise NotImplementedError("Run the sketch above manually with obspy.")


if __name__ == "__main__":
    print("Mass-Movement Watcher — synthetic replay\n")
    replay(synthetic_catalog())
    print("\nNext step: implement fetch_real_waveforms() per its docstring and "
          "re-run the replay on the three real reference events + controls.")
