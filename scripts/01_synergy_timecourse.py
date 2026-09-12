"""
01_synergy_timecourse.py — whole-brain mean synergy per 30-TR bin.

Computes ΦID synergy ('sts' atom) on every pair of regions, averages across
pairs, then averages within each of the 28 30-TR bins that align with the
per-subject intensity ratings. Output: (14 subjects, 2 conditions, 28 bins).

REGION_SELECTION chooses which regions enter the pairwise computation:
  "all"    — all 116 parcels (N_REGIONS ignored). The reportable setting.
  "first"  — the first N_REGIONS parcels. Fast shape/sanity check only; these
             are contiguous in the Schaefer ordering, so it is one chunk of
             cortex, not a sample of the brain. Never report from this.
  "random" — a seeded random subsample of N_REGIONS parcels.

Preprocessing variant fixed to ts_gsr (matches CLAUDE.md primary variant).
Condition axis: index 0 = DMT, index 1 = PCB (confirmed against
external/DMT_NCT/scripts/01_gen_time_resolved_ce.m — TS{i,1}=DMT, TS{i,2}=PCB).

FIT_MODE selects how the Gaussian is fitted for the local-atom evaluation:
  "global"   — single fit on the full 840-TR series (phyid's native behaviour;
               currently the only implemented mode; used as robustness variant A).
  "window"   — refit per sliding window (pre-registered primary analysis B;
               30-TR non-overlapping windows, see WINDOW_TRS/WINDOW_STRIDE).
  "placebo"  — fit on the first half of this subject's placebo run, evaluate
               local atoms on the held-out placebo half and on the full DMT
               run, so both are out-of-sample (robustness variant C).
"""

import itertools
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

from phyid.calculate import calc_PhiID

# ---------------------------------------------------------------- config
SEED = 20261120
N_REGIONS = 116            # ignored when REGION_SELECTION == "all"
REGION_SELECTION = "all"   # "all" | "first" | "random"
VARIANT = "ts_gsr"

# Pre-registered region exclusion (CLAUDE.md, "Pre-registered analysis
# choices"). Region 20 (0-based; Yeo network 3 / dorsal attention, left
# hemisphere) is all-zero for subject index 7, DMT, in every preprocessing
# variant including raw `ts` — an upstream defect in the source data. It is
# dropped for ALL subjects and BOTH conditions so every comparison is over the
# same pair set (115 regions, 6,555 pairs). Applied after REGION_SELECTION.
EXCLUDE_REGIONS = (20,)
TAU = 1
KIND = "gaussian"
REDUNDANCY = "MMI"
ATOM = "sts"               # synergy (unique higher-order)
N_BINS = 28
TRS_PER_BIN = 30           # 840 TRs / 28 ratings = exactly 30
FIT_MODE = "global"        # "global" | "window" | "placebo"

# Pre-registered window for FIT_MODE="window" (primary analysis B). TR = 2 s
# (external/DMT_NCT/scripts/02_global_ce_analyses.m:179 — TR=2; window=60/TR),
# so 30 TRs = 60 s = exactly one intensity-rating bin, and matches the window
# Singleton et al. 2025 used on this dataset. Non-overlapping => 28 windows,
# one per rating. Fixed before any windowed run; do not tune on results.
WINDOW_TRS = 30
WINDOW_STRIDE = 30

# Condition axis of ts_gsr — confirmed from the original MATLAB
# (external/DMT_NCT/scripts/01_gen_time_resolved_ce.m: TS{i,1}=DMT, TS{i,2}=PCB).
CONDITIONS = ("DMT", "PCB")

DATA = Path("external/DMT_NCT/data")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)

rng = np.random.default_rng(SEED)

if FIT_MODE == "window":
    raise NotImplementedError(
        "FIT_MODE='window' (sliding-window ΦID, primary analysis B) not "
        f"implemented yet. Window is pre-registered: {WINDOW_TRS}-TR windows, "
        f"stride {WINDOW_STRIDE}, non-overlapping."
    )
if FIT_MODE == "placebo":
    raise NotImplementedError(
        "FIT_MODE='placebo' (robustness C) not implemented yet. Design is "
        "pre-registered: fit on the first half of PCB, evaluate local atoms "
        "on the held-out PCB half and on the full DMT run, so both are "
        "out-of-sample."
    )
if FIT_MODE != "global":
    raise ValueError(f"FIT_MODE must be 'global', 'window', or 'placebo'; got {FIT_MODE!r}")

# ---------------------------------------------------------------- load
ts_all = sio.loadmat(DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat")[VARIANT]
n_subjects, n_conditions = ts_all.shape
assert (n_subjects, n_conditions) == (14, 2), ts_all.shape
assert len(CONDITIONS) == n_conditions, (CONDITIONS, n_conditions)

n_regions_total, n_trs = ts_all[0, 0].shape
assert n_trs == N_BINS * TRS_PER_BIN, (n_trs, N_BINS * TRS_PER_BIN)

if REGION_SELECTION == "all":
    region_idx = np.arange(n_regions_total)
elif REGION_SELECTION == "first":
    assert n_regions_total >= N_REGIONS, (n_regions_total, N_REGIONS)
    region_idx = np.arange(N_REGIONS)
elif REGION_SELECTION == "random":
    assert n_regions_total >= N_REGIONS, (n_regions_total, N_REGIONS)
    region_idx = np.sort(rng.choice(n_regions_total, N_REGIONS, replace=False))
else:
    raise ValueError(
        "REGION_SELECTION must be 'all', 'first', or 'random'; "
        f"got {REGION_SELECTION!r}"
    )
# ---------------------------------------------------------------- region QC
# Runs on ALL 116 regions before any ΦID call. A region is defective in a
# given (subject, condition) if it is non-finite at TRs where other regions
# are finite (whole-TR dropouts are handled per-TR in the compute loop), or
# if it has zero variance over the finite TRs (phyid divides by std and would
# fail deep inside the covariance fit). Every defect must be covered by the
# pre-registered EXCLUDE_REGIONS rule; anything else stops the run here.
def defective_regions(X):
    fin = np.isfinite(X)
    tr_dead = ~fin.any(axis=0)                 # TR non-finite for every region
    partial = (~fin[:, ~tr_dead]).any(axis=1)  # region-specific non-finite
    sd = X[:, fin.all(axis=0)].std(axis=1, ddof=1)
    out = {}
    for r in np.where(partial)[0]:
        out[int(r)] = "non-finite where other regions are finite"
    for r in np.where(sd == 0)[0]:
        out.setdefault(int(r), "zero variance (constant timeseries)")
    return out

defects = {}
for s in range(n_subjects):
    for c in range(n_conditions):
        d = defective_regions(ts_all[s, c])
        if d:
            defects[(s, c)] = d
            for r, why in d.items():
                print(f"  [qc] s={s} {CONDITIONS[c]} region {r}: {why}")

uncovered = sorted({r for d in defects.values() for r in d} - set(EXCLUDE_REGIONS))
if uncovered:
    raise RuntimeError(
        f"regions {uncovered} are defective in at least one (subject, "
        f"condition) but are not in EXCLUDE_REGIONS={EXCLUDE_REGIONS}. Record "
        "an exclusion rule in CLAUDE.md before running; do not let phyid "
        "crash on them."
    )
for r in EXCLUDE_REGIONS:
    where = [f"s={s} {CONDITIONS[c]}" for (s, c), d in defects.items() if r in d]
    print(f"  [qc] excluding region {r} for ALL subjects and BOTH conditions "
          f"(pre-registered rule; defective in: {', '.join(where) or 'none'})")

n_selected = region_idx.size
region_idx = region_idx[~np.isin(region_idx, EXCLUDE_REGIONS)]
n_regions = region_idx.size
print(f"  [qc] regions entering ΦID: {n_regions} (selected {n_selected}, "
      f"excluded {n_selected - n_regions})")

TAG = f"{n_regions}regions-{REGION_SELECTION}_{VARIANT}_{FIT_MODE}"
OUT_NPY = RESULTS / f"synergy_bins_{TAG}.npy"
OUT_CSV = RESULTS / f"synergy_bins_{TAG}.csv"

pairs = list(itertools.combinations(range(n_regions), 2))
n_pairs = len(pairs)

print(f"variant={VARIANT}  regions={n_regions}/{n_regions_total} "
      f"({REGION_SELECTION})  pairs={n_pairs}  subjects={n_subjects}  "
      f"conditions={CONDITIONS}")
print(f"TRs={n_trs}  bins={N_BINS}  TRs/bin={TRS_PER_BIN}  tau={TAU}  "
      f"fit_mode={FIT_MODE}")

# ---------------------------------------------------------------- compute
# NOTE: at least one (subject, condition) has non-finite TRs (sub 2 PCB TR 839
# is all-NaN across regions in every ts variant). We drop non-finite TRs, then
# attribute each sts sample to its ORIGINAL TR index so the 30-TR bins stay
# aligned with the intensity ratings.
synergy_bins = np.full((n_subjects, n_conditions, N_BINS), np.nan)
bin_counts = np.zeros((n_subjects, n_conditions, N_BINS), dtype=int)

t0 = time.time()
for s in range(n_subjects):
    for c in range(n_conditions):
        X = ts_all[s, c][region_idx, :]  # (n_regions, n_trs)

        finite = np.all(np.isfinite(X), axis=0)
        kept = np.where(finite)[0]
        n_dropped = n_trs - kept.size
        if n_dropped:
            # Warn if drops are not purely at the tail — a middle gap would let
            # phyid treat non-adjacent TRs as adjacent, which is a real problem.
            is_tail = np.array_equal(kept, np.arange(kept.size))
            note = "tail" if is_tail else "MIDDLE-GAP"
            print(f"  [warn] s={s} {CONDITIONS[c]}: dropped {n_dropped} "
                  f"non-finite TR(s) ({note})")
        X_clean = X[:, kept]

        # accumulate mean-over-pairs of sts on the cleaned series
        sts_sum = np.zeros(kept.size - TAU)
        for i, j in pairs:
            atoms, _ = calc_PhiID(X_clean[i], X_clean[j], tau=TAU,
                                  kind=KIND, redundancy=REDUNDANCY)
            sts_sum += np.asarray(atoms[ATOM])
        sts_mean = sts_sum / n_pairs

        # sts sample p corresponds to transition kept[p] -> kept[p+TAU];
        # attribute it to start TR kept[p]. Bin b covers TRs b*30..(b+1)*30-1.
        start_tr = kept[:sts_mean.size]
        bin_of = start_tr // TRS_PER_BIN
        for b in range(N_BINS):
            m = bin_of == b
            if m.any():
                synergy_bins[s, c, b] = sts_mean[m].mean()
                bin_counts[s, c, b] = int(m.sum())

    print(f"  subject {s + 1:2d}/{n_subjects} done  "
          f"({time.time() - t0:.1f}s elapsed)")

elapsed = time.time() - t0
print(f"compute finished in {elapsed:.1f}s "
      f"({elapsed / (n_subjects * n_conditions * n_pairs) * 1000:.1f} ms/pair)")

# ---------------------------------------------------------------- provenance
try:
    sha = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"], text=True,
        stderr=subprocess.DEVNULL,
    ).strip()
    # flag if the code that produced this result is not what HEAD contains
    if subprocess.check_output(
        ["git", "status", "--porcelain", "--", "scripts", "CLAUDE.md"],
        text=True, stderr=subprocess.DEVNULL,
    ).strip():
        sha += "-dirty"
except (subprocess.CalledProcessError, FileNotFoundError):
    sha = "nogit"

# ---------------------------------------------------------------- save
np.save(OUT_NPY, synergy_bins)

with open(OUT_CSV, "w") as fh:
    fh.write("# script=01_synergy_timecourse.py "
             f"variant={VARIANT} regions={n_regions} "
             f"region_selection={REGION_SELECTION} "
             f"excluded_regions={','.join(map(str, EXCLUDE_REGIONS)) or 'none'} "
             f"atom={ATOM} "
             f"tau={TAU} redundancy={REDUNDANCY} fit_mode={FIT_MODE} "
             f"seed={SEED} git={sha}\n")
    fh.write("subject,condition,bin,synergy_mean\n")
    for s in range(n_subjects):
        for c, cond_name in enumerate(CONDITIONS):
            for b in range(N_BINS):
                fh.write(f"{s},{cond_name},{b},{synergy_bins[s, c, b]:.6f}\n")

# ---------------------------------------------------------------- summary
print()
print(f"array shape: {synergy_bins.shape}")
print(f"finite fraction: {np.isfinite(synergy_bins).mean():.3f}")
print(f"samples/bin: min={bin_counts.min()} max={bin_counts.max()} "
      f"median={int(np.median(bin_counts))}")
print(f"global mean={np.nanmean(synergy_bins):.4f}  "
      f"std={np.nanstd(synergy_bins):.4f}  "
      f"min={np.nanmin(synergy_bins):.4f}  "
      f"max={np.nanmax(synergy_bins):.4f}")
print()
print("mean synergy across subjects, per bin:")
for c, cond_name in enumerate(CONDITIONS):
    print(f"  {cond_name}:", np.array2string(np.nanmean(synergy_bins[:, c], axis=0),
                                             precision=3, suppress_small=True))
print(f"\nwrote {OUT_NPY}")
print(f"wrote {OUT_CSV}")
