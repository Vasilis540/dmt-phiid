"""
01_synergy_timecourse.py — whole-brain mean ΦID atoms per 30-TR bin.

Computes all 16 ΦID atoms on every pair of regions, averages across pairs,
then averages within each of the 28 30-TR bins that align with the
per-subject intensity ratings. Output: (14 subjects, 2 conditions, 28 bins,
16 atoms), atom order as phyid.utils.PhiID_atoms_abbr (rtr ... sts).
Synergy is atoms[..., ATOMS.index("sts")]; redundancy is rtr. Saving every
atom from the one run means any secondary atom (e.g. the pre-registered rtr
prediction, manuscript/analysis_record.md) is read from the same computation as sts, never from
a separate rerun.

REGION_SELECTION chooses which regions enter the pairwise computation:
  "all"    — all 116 parcels (N_REGIONS ignored). The reportable setting.
  "first"  — the first N_REGIONS parcels. Fast shape/sanity check only; these
             are contiguous in the Schaefer ordering, so it is one chunk of
             cortex, not a sample of the brain. Never report from this.
  "random" — a seeded random subsample of N_REGIONS parcels.

Preprocessing variant: ts_gsr by default (manuscript/analysis_record.md primary stream);
`--variant ts_demean` runs the rule-6 sensitivity stream. The variant is in
the output filename, so the streams never overwrite each other.
Condition axis: index 0 = DMT, index 1 = PCB (confirmed against
external/DMT_NCT/scripts/01_gen_time_resolved_ce.m — TS{i,1}=DMT, TS{i,2}=PCB).

FIT_MODE (constant, overridable with --fit-mode) selects how the Gaussian is
fitted for the local-atom evaluation:
  "global"   — single fit on the full 840-TR series (phyid's native behaviour;
               robustness variant A). Output per 30-TR rating bin,
               (14, 2, 28, 16).
  "window"   — refit per non-overlapping window (primary analysis B). Every
               window is an independent calc_PhiID call on that window's
               samples alone: covariance, mean AND the MMI min-selections are
               all per window, exactly what 02_bias_check.py simulates.
               Default WINDOW_TRS = 60, stride 60 => 14 windows, two rating
               bins each; output per window, (14, 2, 14, 16), prefix
               atoms_win60. `--window-trs 30` (28 windows, one per bin,
               prefix atoms_win30) is the pre-registered positive control for
               the shrinkage model (manuscript/analysis_record.md), not a primary analysis.
  "placebo"  — robustness variant C, split-half design (manuscript/analysis_record.md): fit mean
               and covariance of the four-vector on the FIRST HALF of this
               subject's placebo run (TRs 0-419), fix the MMI selections from
               that model's analytic Gaussian MIs, and evaluate local atoms
               under that one model on the held-out placebo half (TRs 420-839)
               and on the full DMT run. Both evaluations are out-of-sample.
               Output per 30-TR bin, (14, 2, 28, 16); PCB bins 0-13 are NaN
               (in-sample, not evaluated).
Neither "window" nor "placebo" is to be run on the full real data until the
20,000-run bias check assigns a tier (manuscript/analysis_record.md); both are smoke-tested only.
"""

import argparse
import itertools
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

from phyid.calculate import (_get_atoms_four_vec, _get_coinfo_four_vec,
                             calc_PhiID)
from phyid.measures import local_entropy_mvn
from phyid.utils import PhiID_atoms_abbr

# ---------------------------------------------------------------- config
SEED = 20261120
N_REGIONS = 116            # ignored when REGION_SELECTION == "all"
REGION_SELECTION = "all"   # "all" | "first" | "random"
_ap = argparse.ArgumentParser(description="whole-brain mean ΦID atoms per bin")
_ap.add_argument("--variant", default="ts_gsr",
                 choices=("ts_gsr", "ts_demean", "ts_z", "ts"),
                 help="preprocessing variant in the .mat (default ts_gsr)")
_ap.add_argument("--fit-mode", default=None, choices=("global", "window", "placebo"),
                 help="override FIT_MODE (default: the constant below)")
_ap.add_argument("--window-trs", type=int, default=60, choices=(30, 60),
                 help="window length for --fit-mode window (default 60; 30 = positive control)")
_args = _ap.parse_args()
VARIANT = _args.variant

# Pre-registered region exclusion (manuscript/analysis_record.md, "Pre-registered analysis
# choices"). Region 20 (0-based; Yeo network 3 / dorsal attention, left
# hemisphere) is all-zero for subject index 7, DMT, in every preprocessing
# variant including raw `ts` — an upstream defect in the source data. It is
# dropped for ALL subjects and BOTH conditions so every comparison is over the
# same pair set (115 regions, 6,555 pairs). Applied after REGION_SELECTION.
EXCLUDE_REGIONS = (20,)
TAU = 1
KIND = "gaussian"
REDUNDANCY = "MMI"
ATOMS = tuple(PhiID_atoms_abbr)   # all 16 atoms, phyid order; sts = synergy
N_ATOMS = len(ATOMS)
assert N_ATOMS == 16 and ATOMS[0] == "rtr" and ATOMS[-1] == "sts", ATOMS
N_BINS = 28
TRS_PER_BIN = 30           # 840 TRs / 28 ratings = exactly 30
FIT_MODE = _args.fit_mode or "global"   # "global" | "window" | "placebo"

# Window for FIT_MODE="window" (primary analysis B). TR = 2 s
# (external/DMT_NCT/scripts/02_global_ce_analyses.m:179 — TR=2; window=60/TR).
# The original pre-registration was 30 TRs (one rating bin, the Singleton et
# al. 2025 window); the pre-registered decision tree (manuscript/analysis_record.md, Primary B)
# moves to W = 60, stride 60 — two rating bins per window, 14 windows, each
# rating pair averaged to match — when the W = 30 differential-bias criterion
# fails, which the bias check predicted and which the 13 Sep 2026 instruction
# adopts. Non-overlapping. Fixed before any windowed run; do not tune on
# results. W = 30 is retained as the pre-registered positive control for the
# shrinkage model (same sign, smaller magnitude expected). WINDOW_TRS must
# divide 840 and equal the stride (non-overlapping).
WINDOW_TRS = _args.window_trs
WINDOW_STRIDE = WINDOW_TRS
assert WINDOW_STRIDE == WINDOW_TRS and 840 % WINDOW_TRS == 0, (WINDOW_TRS, WINDOW_STRIDE)
N_WINDOWS = 840 // WINDOW_TRS
PLACEBO_FIT_TRS = 420      # FIT_MODE="placebo": fit on PCB TRs [0, 420), evaluate on [420, 840)

# Pre-registered tier-2 sign handling on real data (manuscript/analysis_record.md, "Sign handling
# on real data", fixed 13 Sep 2026 before any real windowed run). Tracking
# across the decay windows is assessed on |rho_S| >= TIER2_ABS_RHO, where
# rho_S is each subject's Spearman correlation between window-mean whole-brain
# sts and intensity, group-tested against the phase-randomised temporal null.
# The SIGN is reported separately against PREREG_DIRECTION (+1: the hypothesis
# is that synergy is UP-regulated, so a positive rho_S is the pre-registered
# direction). A strong negative correlation is tracking in the opposite
# direction and is reported as a refutation of the directional hypothesis,
# NOT as a failed tracking criterion. Do not fold the sign into the threshold.
TIER2_ABS_RHO = 0.80
PREREG_DIRECTION = +1
# Decay windows on real data (manuscript/analysis_record.md, "Decay windows on real data", fixed
# 13 Sep 2026 before any real windowed run): 1-based inclusive window ranges at
# W = 60. Primary excludes window 5 (bins 9-10) on the placebo injection
# response at bins 8-10 seen in the global fit; the pre-registered set 5-14 is
# the sensitivity analysis and the set on which the simulation tier is assigned.
DECAY_WINDOWS_PRIMARY = (6, 14)
DECAY_WINDOWS_SENSITIVITY = (5, 14)

# Condition axis of ts_gsr — confirmed from the original MATLAB
# (external/DMT_NCT/scripts/01_gen_time_resolved_ce.m: TS{i,1}=DMT, TS{i,2}=PCB).
CONDITIONS = ("DMT", "PCB")

DATA = Path("external/DMT_NCT/data")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)

rng = np.random.default_rng(SEED)

if FIT_MODE not in ("global", "window", "placebo"):
    raise ValueError(f"FIT_MODE must be 'global', 'window', or 'placebo'; got {FIT_MODE!r}")


# ---------------------------------------------------------------- fixed-model ΦID
# Used by FIT_MODE="placebo". phyid's calc_PhiID fits and evaluates on the same
# samples; here the Gaussian (mu, cov of the four-vector [x_past, y_past,
# x_future, y_future]) comes from one dataset and the local atoms are evaluated
# on another. No per-variable standardisation is applied: local MIs, and hence
# every atom, are invariant to a fixed per-variable rescaling applied to model
# and data alike, so this equals phyid's standardised computation whenever the
# fit and evaluation data coincide (checked in the smoke test to ~1e-10).
_IDX = {  # entropy term -> variable subset, in phyid's four-vector order
    "h_p1": [0], "h_p2": [1], "h_t1": [2], "h_t2": [3],
    "h_p1p2": [0, 1], "h_t1t2": [2, 3], "h_p1t1": [0, 2], "h_p1t2": [0, 3],
    "h_p2t1": [1, 2], "h_p2t2": [1, 3], "h_p1p2t1": [0, 1, 2],
    "h_p1p2t2": [0, 1, 3], "h_p1t1t2": [0, 2, 3], "h_p2t1t2": [1, 2, 3],
    "h_p1p2t1t2": [0, 1, 2, 3],
}


def four_vec(x, y, tau):
    """(4, T-tau) array [x_past, y_past, x_future, y_future], phyid's order."""
    return np.c_[x[:-tau], y[:-tau], x[tau:], y[tau:]].T


def fit_gaussian(X):
    """mu (4,), cov (4,4) of a four-vector sample (4, N); ddof=1 as np.cov."""
    return np.mean(X, axis=1), np.cov(X)


def analytic_mi(cov, a, b):
    """Gaussian MI between variable sets a and b under cov, in nats."""
    ld = lambda idx: np.linalg.slogdet(cov[np.ix_(idx, idx)])[1]
    return 0.5 * (ld(a) + ld(b) - ld(a + b))


def mmi_selections(cov):
    """MMI min-selections fixed from the model, not from evaluation samples.

    Returns the six redundancy choices as 0/1 (first/second candidate) and the
    rtr choice as an index into [I_xta, I_xtb, I_yta, I_ytb], all decided on
    the analytic Gaussian MIs of the fitted covariance. phyid decides the same
    choices on the mean local MI of the fit samples, which under a Gaussian fit
    to those same samples is the plug-in MI, i.e. the same number.
    """
    I = {
        "I_xta": analytic_mi(cov, [0], [2]), "I_xtb": analytic_mi(cov, [0], [3]),
        "I_yta": analytic_mi(cov, [1], [2]), "I_ytb": analytic_mi(cov, [1], [3]),
        "I_xyta": analytic_mi(cov, [0, 1], [2]), "I_xytb": analytic_mi(cov, [0, 1], [3]),
        "I_xtab": analytic_mi(cov, [0], [2, 3]), "I_ytab": analytic_mi(cov, [1], [2, 3]),
    }
    pairs = {
        "R_xyta": ("I_xta", "I_yta"), "R_xytb": ("I_xtb", "I_ytb"),
        "R_xytab": ("I_xtab", "I_ytab"), "R_abtx": ("I_xta", "I_xtb"),
        "R_abty": ("I_yta", "I_ytb"), "R_abtxy": ("I_xyta", "I_xytb"),
    }
    sel = {k: (0 if I[a] < I[b] else 1) for k, (a, b) in pairs.items()}
    sel["rtr"] = int(np.argmin([I["I_xta"], I["I_xtb"], I["I_yta"], I["I_ytb"]]))
    return sel, pairs


def local_atoms_under_model(X_eval, mu, cov, sel, pairs):
    """Local ΦID atoms (dict of (N,) arrays) of X_eval (4, N) under (mu, cov)."""
    h = {k: local_entropy_mvn(X_eval[idx].T, mu[idx], cov[np.ix_(idx, idx)])
         for k, idx in _IDX.items()}
    I = _get_coinfo_four_vec(h)
    R = {k: I[pairs[k][sel[k]]] for k in pairs}
    rtr = I[["I_xta", "I_xtb", "I_yta", "I_ytb"][sel["rtr"]]]
    return _get_atoms_four_vec({"h_res": h, "I_res": I, "R_res": R, "rtr": rtr})

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
        "an exclusion rule in manuscript/analysis_record.md before running; do not let phyid "
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
PREFIX = f"atoms_win{WINDOW_TRS}" if FIT_MODE == "window" else "atoms_bins"
OUT_NPY = RESULTS / f"{PREFIX}_{TAG}.npy"
OUT_CSV = RESULTS / f"{PREFIX}_{TAG}.csv"
# TR-resolution pair-mean local atoms, (14, 2, 840, 16): sample p of a run is
# stored at its start TR; NaN where no sample is attributed (dropped TRs and,
# in window mode, the last TR of every window). The pre-registered temporal
# null (manuscript/analysis_record.md, step-contrast test) phase-randomises this series.
OUT_LOCAL_NPY = RESULTS / f"{PREFIX}_local_{TAG}.npy"
# time axis of the output: rating bins (global, placebo) or windows (window)
N_T, T_LEN, T_NAME = ((N_WINDOWS, WINDOW_TRS, "window") if FIT_MODE == "window"
                      else (N_BINS, TRS_PER_BIN, "bin"))

pairs = list(itertools.combinations(range(n_regions), 2))
n_pairs = len(pairs)

print(f"variant={VARIANT}  regions={n_regions}/{n_regions_total} "
      f"({REGION_SELECTION})  pairs={n_pairs}  subjects={n_subjects}  "
      f"conditions={CONDITIONS}")
print(f"TRs={n_trs}  {T_NAME}s={N_T}  TRs/{T_NAME}={T_LEN}  tau={TAU}  "
      f"fit_mode={FIT_MODE}")

# ---------------------------------------------------------------- compute
# NOTE: at least one (subject, condition) has non-finite TRs (sub 2 PCB TR 839
# is all-NaN across regions in every ts variant). We drop non-finite TRs, then
# attribute each atom sample to its ORIGINAL TR index so the 30-TR bins stay
# aligned with the intensity ratings.
atoms_bins = np.full((n_subjects, n_conditions, N_T, N_ATOMS), np.nan)
atoms_local = np.full((n_subjects, n_conditions, n_trs, N_ATOMS), np.nan)
bin_counts = np.zeros((n_subjects, n_conditions, N_T), dtype=int)


def finite_trs(X, label):
    """Indices of TRs finite in every region; warn if the drop is not a tail."""
    kept = np.where(np.all(np.isfinite(X), axis=0))[0]
    n_dropped = X.shape[1] - kept.size
    if n_dropped:
        is_tail = np.array_equal(kept, np.arange(kept.size))
        print(f"  [warn] {label}: dropped {n_dropped} non-finite TR(s) "
              f"({'tail' if is_tail else 'MIDDLE-GAP'})")
    return kept


def pair_mean_atoms_native(X_clean):
    """(N_ATOMS, T-tau) mean over pairs of phyid's native local atoms
    (fit and evaluation on the same samples)."""
    acc = np.zeros((N_ATOMS, X_clean.shape[1] - TAU))
    for i, j in pairs:
        atoms, _ = calc_PhiID(X_clean[i], X_clean[j], tau=TAU,
                              kind=KIND, redundancy=REDUNDANCY)
        for a, name in enumerate(ATOMS):
            acc[a] += np.asarray(atoms[name])
    return acc / n_pairs


def accumulate(s, c, atom_mean, start_tr):
    """Attribute atom sample p (transition start_tr[p] -> +TAU) to its
    time slot; slot t covers TRs t*T_LEN .. (t+1)*T_LEN-1."""
    n_samples = atom_mean.shape[1]
    atoms_local[s, c, start_tr[:n_samples], :] = atom_mean.T
    slot_of = start_tr[:n_samples] // T_LEN
    for t in range(N_T):
        m = slot_of == t
        if m.any():
            atoms_bins[s, c, t, :] = atom_mean[:, m].mean(axis=1)
            bin_counts[s, c, t] = int(m.sum())


t0 = time.time()
for s in range(n_subjects):
    if FIT_MODE == "global":
        for c in range(n_conditions):
            X = ts_all[s, c][region_idx, :]
            kept = finite_trs(X, f"s={s} {CONDITIONS[c]}")
            accumulate(s, c, pair_mean_atoms_native(X[:, kept]), kept)

    elif FIT_MODE == "window":
        # Each window is fitted and evaluated on its own samples only, so the
        # first window sample is transition (w*W) -> (w*W+tau) and the last is
        # (w*W+W-1-tau) -> (w*W+W-1): no sample straddles a window boundary.
        for c in range(n_conditions):
            X = ts_all[s, c][region_idx, :]
            kept = finite_trs(X, f"s={s} {CONDITIONS[c]}")
            for w in range(N_WINDOWS):
                in_w = kept[(kept >= w * WINDOW_TRS) & (kept < (w + 1) * WINDOW_TRS)]
                if in_w.size <= TAU + 4:      # cannot fit a 4x4 covariance
                    continue
                accumulate(s, c, pair_mean_atoms_native(X[:, in_w]), in_w)

    elif FIT_MODE == "placebo":
        c_pcb = CONDITIONS.index("PCB")
        c_dmt = CONDITIONS.index("DMT")
        X_pcb = ts_all[s, c_pcb][region_idx, :]
        X_dmt = ts_all[s, c_dmt][region_idx, :]
        kept_pcb = finite_trs(X_pcb, f"s={s} PCB")
        kept_dmt = finite_trs(X_dmt, f"s={s} DMT")
        fit_trs = kept_pcb[kept_pcb < PLACEBO_FIT_TRS]
        eval_trs = kept_pcb[kept_pcb >= PLACEBO_FIT_TRS]
        assert np.array_equal(fit_trs, np.arange(PLACEBO_FIT_TRS)), \
            f"s={s}: PCB fit half must be complete and contiguous"
        acc_pcb = np.zeros((N_ATOMS, eval_trs.size - TAU))
        acc_dmt = np.zeros((N_ATOMS, kept_dmt.size - TAU))
        for i, j in pairs:
            mu, cov = fit_gaussian(four_vec(X_pcb[i, fit_trs], X_pcb[j, fit_trs], TAU))
            sel, prs = mmi_selections(cov)
            for acc, X, trs in ((acc_pcb, X_pcb, eval_trs), (acc_dmt, X_dmt, kept_dmt)):
                atoms = local_atoms_under_model(four_vec(X[i, trs], X[j, trs], TAU),
                                                mu, cov, sel, prs)
                for a, name in enumerate(ATOMS):
                    acc[a] += np.asarray(atoms[name])
        accumulate(s, c_pcb, acc_pcb / n_pairs, eval_trs)
        accumulate(s, c_dmt, acc_dmt / n_pairs, kept_dmt)

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
        ["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"],
        text=True, stderr=subprocess.DEVNULL,
    ).strip():
        sha += "-dirty"
except (subprocess.CalledProcessError, FileNotFoundError):
    sha = "nogit"

# ---------------------------------------------------------------- save
np.save(OUT_NPY, atoms_bins)
np.save(OUT_LOCAL_NPY, atoms_local)

with open(OUT_CSV, "w") as fh:
    fh.write("# script=01_synergy_timecourse.py "
             f"variant={VARIANT} regions={n_regions} "
             f"region_selection={REGION_SELECTION} "
             f"excluded_regions={','.join(map(str, EXCLUDE_REGIONS)) or 'none'} "
             f"atoms={','.join(ATOMS)} "
             f"tau={TAU} redundancy={REDUNDANCY} fit_mode={FIT_MODE} "
             f"window_trs={WINDOW_TRS if FIT_MODE == 'window' else 'na'} "
             f"placebo_fit_trs={PLACEBO_FIT_TRS if FIT_MODE == 'placebo' else 'na'} "
             f"seed={SEED} git={sha}\n")
    fh.write(f"subject,condition,{T_NAME}," + ",".join(ATOMS) + "\n")
    for s in range(n_subjects):
        for c, cond_name in enumerate(CONDITIONS):
            for b in range(N_T):
                vals = ",".join(f"{v:.6f}" for v in atoms_bins[s, c, b])
                fh.write(f"{s},{cond_name},{b},{vals}\n")

# ---------------------------------------------------------------- summary
print()
synergy_bins = atoms_bins[..., ATOMS.index("sts")]
print(f"array shape: {atoms_bins.shape}  (atoms: {', '.join(ATOMS)})")
print(f"finite fraction: {np.isfinite(atoms_bins).mean():.3f}")
_bc = bin_counts[bin_counts > 0]
print(f"samples/{T_NAME} (evaluated slots): min={_bc.min()} max={_bc.max()} "
      f"median={int(np.median(_bc))}; empty slots={(bin_counts == 0).sum()}")
print(f"sts global mean={np.nanmean(synergy_bins):.4f}  "
      f"std={np.nanstd(synergy_bins):.4f}  "
      f"min={np.nanmin(synergy_bins):.4f}  "
      f"max={np.nanmax(synergy_bins):.4f}")
print()
print(f"mean synergy (sts) across subjects, per {T_NAME}:")
for c, cond_name in enumerate(CONDITIONS):
    print(f"  {cond_name}:", np.array2string(np.nanmean(synergy_bins[:, c], axis=0),
                                             precision=3, suppress_small=True))
print(f"\nwrote {OUT_NPY}")
print(f"wrote {OUT_LOCAL_NPY}")
print(f"wrote {OUT_CSV}")
