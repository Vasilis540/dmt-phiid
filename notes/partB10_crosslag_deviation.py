"""
partB10_crosslag_deviation.py — run-level mean cross-lag deviation (the test of the pooling mechanism named
in Results 4 as a candidate explanation of the run-level residual; Limitations listed it as not run).
Pre-run entries: manuscript/analysis_record.md, "Run-level mean cross-lag deviation and the regional sts–r₁ test:
pre-run entry, 15 Sep 2026 15:35 UTC" (the signed mean, prediction recorded there) and "The sign(q)-weighted
cross-lag deviation: pre-run entry, 15 Sep 2026" (the two statistics added after the fifth review, predictions
recorded there).

Per subject and run, from the run-level 4 × 4 correlation matrices of every pair (all finite TRs of the run,
the matrices of partB4_diagnostic.py's run-level rows), the per-pair deviations
    d_xy = corr(x_t, y_{t+1}) − a_y q   and   d_yx = corr(y_t, x_{t+1}) − a_x q,
where a_x = corr(x_t, x_{t+1}), a_y = corr(y_t, y_{t+1}) are the run-level lag-1 autocorrelations and q the mean
of the two lag-0 correlations, exactly as the diagnostic defines them. Both variants. Three statistics per run,
each over the 2 × 6,555 deviations:
  1. the signed mean (the statistic of the first pre-run entry);
  2. the sign(q)-weighted mean, mean of sign(q) × d — the statistic the pooling mechanism implies (the fifth
     review): on the family sts is invariant under y → −y, which flips q and d together, so the deviation that
     lowers sts below the AR(1) prediction is positive for q > 0 and negative for q < 0, and a signed mean over
     pairs of both signs of q cancels where the sign(q)-weighted mean does not (checked in the header lines);
  3. the slope of d on q across pairs (ordinary least squares with intercept), the same mechanism's other
     signature (a deviation proportional to q).
Reported for each: the per-run means (DMT, placebo), the grand mean over the 28 runs with a subject-bootstrap
95 % CI (10,000 draws, seed 20261120; one set of draws per variant, shared by the three statistics, so that the
signed mean's interval is the one reported at 152cc6d) and an exact sign-flip p over the 14 subjects (2^14
assignments, two-sided, on the per-subject mean of the two runs), the number of subjects positive, and the
correlation with the run-level residual of the diagnostic across the 28 runs. Descriptive, no inference: the
share of pairs with q < 0, the mean deviation among the q > 0 and among the q < 0 pairs, the SD of the deviation
across pairs, the run-level residual of the diagnostic for the same runs, and the mean pair a and |q|.

Outputs: notes/review_results/partB/crosslag_deviation_tables.md, crosslag_deviation.csv (one row per run),
crosslag_deviation_run.log (via run_all.sh's nstep, or stdout).
Run from the repository root: .venv/bin/python notes/partB10_crosslag_deviation.py   (about a minute)
"""
import subprocess
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS

REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
OUT = REPO / "notes" / "review_results" / "partB"
OUT.mkdir(parents=True, exist_ok=True)
REGIONS = np.array([r for r in range(116) if r != 20])
S = ATOMS.index("sts")
SEED = 20261120
N_BOOT = 10000
CONDITIONS = ("DMT", "PCB")
REQUIRED = 0.006          # the sign(q)-weighted deviation a coupling account of the −0.01 run-level residual requires (record, 15 Sep 2026 10:05 UTC)

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=REPO).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "notes/*.py", "manuscript/analysis_record.md"],
                               text=True, cwd=REPO).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"


def family_sts(a, q, d):
    """sts of the symmetric AR(1) pair (a, q) with both cross-lag entries displaced by d."""
    C = ar1_corr(a, a, q)
    C[:, 0, 3] += d; C[:, 3, 0] += d; C[:, 1, 2] += d; C[:, 2, 1] += d
    return atoms_from_corr(C)[0, S]


# family check of the sign convention: sts(a, q, d) = sts(a, −q, −d); at q = +0.25, d = +0.006 lowers sts by ≈ 0.01
base = family_sts(0.85, 0.25, 0.0)
chk_plus, chk_minus = family_sts(0.85, 0.25, 0.0188), family_sts(0.85, -0.25, -0.0188)
chk_wrong = family_sts(0.85, -0.25, 0.0188)
res_required = family_sts(0.85, 0.25, REQUIRED) - base
res_required_neg = family_sts(0.85, -0.25, REQUIRED) - base
assert abs(chk_plus - chk_minus) < 1e-12 and chk_wrong > base > chk_plus

SIGNS = ((np.arange(1 << 14)[:, None] >> np.arange(14)) & 1) * 2 - 1        # 16,384 sign assignments


def infer(per_run, idx):
    """grand mean over subjects of the per-subject mean of the two runs; bootstrap CI on the shared draws; exact sign-flip p."""
    per_subj = per_run.mean(1)
    grand = per_subj.mean()
    boot = per_subj[idx].mean(1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    null = (SIGNS * per_subj).mean(1)
    p_flip = np.mean(np.abs(null) >= abs(grand) - 1e-15)
    return grand, lo, hi, p_flip, int((per_subj > 0).sum()), per_subj


def fmt(per_run, idx, res, name, digits=5):
    grand, lo, hi, p, npos, per_subj = infer(per_run, idx)
    r_res = np.corrcoef(per_run.ravel(), res.ravel())[0, 1]
    line = (f"{name}: DMT {per_run[:, 0].mean():+.{digits}f}, PCB {per_run[:, 1].mean():+.{digits}f}; grand mean {grand:+.{digits}f} "
            f"[{lo:+.{digits}f}, {hi:+.{digits}f}] (subject bootstrap, {N_BOOT} draws), exact sign-flip p = {p:.4f}, "
            f"positive in {npos}/14 subjects; r(statistic, run-level residual) across the 28 runs {r_res:+.3f}.")
    return line, grand, lo, hi, per_subj


lines = [f"# Run-level mean cross-lag deviation (partB10_crosslag_deviation.py; git={sha}; seed={SEED})", "",
         "Per subject and run, over the 2 × 6,555 deviations corr(x_t, y_(t+1)) − a_y q and corr(y_t, x_(t+1)) − a_x q of the "
         "run-level 4 × 4 correlation matrices (all finite TRs of the run; a_x, a_y and q as in partB4_diagnostic.py): "
         "(1) the signed mean, (2) the sign(q)-weighted mean, mean of sign(q) × deviation, (3) the OLS slope of the deviation on q "
         "across pairs. Predictions recorded before the runs (analysis_record.md): for (1), the pre-run entry of 15 Sep 2026 15:35 UTC "
         "(negative on ts_gsr and near zero on ts_demean if pooling of non-stationary segments explains the run-level residual; near zero "
         "on both otherwise); for (2) and (3), the entry \"The sign(q)-weighted cross-lag deviation: pre-run entry, 15 Sep 2026\" "
         "(if pooling operates as described, (2) on ts_gsr is positive and of order +0.006; near zero or far below that, pooling does "
         "not account for the run-level residual). 'Near zero' = subject-bootstrap 95 % CI includes zero. "
         "The three statistics share one set of bootstrap draws per variant; the signed mean's numbers are those reported at 152cc6d.", "",
         f"Family check of the sign convention (symmetric AR(1) pair, a = 0.85, both cross-lag entries displaced by d): "
         f"sts(q = +0.25, d = +0.0188) = {chk_plus:.5f} = sts(q = −0.25, d = −0.0188) = {chk_minus:.5f}, against sts(q = −0.25, d = +0.0188) = {chk_wrong:.5f} "
         f"and {base:.5f} at d = 0; so sign(q) × d > 0 is what lowers sts below the AR(1) prediction. At q = +0.25 a deviation of +{REQUIRED} "
         f"gives a residual of {res_required:+.4f} (the ≈ −0.01 run-level residual on ts_gsr); at q = −0.25 the same +{REQUIRED} gives {res_required_neg:+.4f}.", ""]
rows = []
ts = sio.loadmat(MAT)
rng = np.random.default_rng(SEED)
t0 = time.time()
for var in ("ts_gsr", "ts_demean"):
    dev = np.full((14, 2), np.nan); dev_sd = np.full((14, 2), np.nan); dev_abs = np.full((14, 2), np.nan)
    devq = np.full((14, 2), np.nan); slope = np.full((14, 2), np.nan); share_neg = np.full((14, 2), np.nan)
    dev_pos = np.full((14, 2), np.nan); dev_neg = np.full((14, 2), np.nan)
    obs = np.full((14, 2), np.nan); pred = np.full((14, 2), np.nan)
    a_mean = np.full((14, 2), np.nan); q_abs = np.full((14, 2), np.nan)
    for s, c in product(range(14), range(2)):
        X = np.asarray(ts[var][s, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        pp = PairPhiID(X[:, kept]); C = pp.C
        ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
        d = np.r_[C[:, 0, 3] - ay * q, C[:, 1, 2] - ax * q]
        q2 = np.r_[q, q]
        dev[s, c] = d.mean(); dev_sd[s, c] = d.std(); dev_abs[s, c] = np.abs(d).mean()
        devq[s, c] = (np.sign(q2) * d).mean()
        slope[s, c] = np.polyfit(q2, d, 1)[0]
        share_neg[s, c] = (q < 0).mean()
        dev_pos[s, c] = d[q2 > 0].mean(); dev_neg[s, c] = d[q2 < 0].mean() if (q2 < 0).any() else np.nan
        obs[s, c] = pp.atoms_mean()[:, S].mean(); pred[s, c] = atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean()
        a_mean[s, c] = (0.5 * (ax + ay)).mean(); q_abs[s, c] = np.abs(q).mean()
        rows.append(dict(variant=var, subject=s + 1, condition=CONDITIONS[c], n_trs=int(kept.size), mean_crosslag_deviation=dev[s, c],
                         signq_weighted_mean_deviation=devq[s, c], slope_deviation_on_q=slope[s, c], share_pairs_q_negative=share_neg[s, c],
                         mean_deviation_q_positive=dev_pos[s, c], mean_deviation_q_negative=dev_neg[s, c],
                         sd_across_pairs=dev_sd[s, c], mean_abs_deviation=dev_abs[s, c], observed_sts=obs[s, c], predicted_sts=pred[s, c],
                         residual=obs[s, c] - pred[s, c], mean_pair_a=a_mean[s, c], mean_pair_abs_q=q_abs[s, c]))
    res = obs - pred
    idx = rng.integers(0, 14, (N_BOOT, 14))                  # the draws of the 152cc6d run, now shared by the three statistics
    lines.append(f"## {var}")
    lines.append("")
    l1, grand, lo, hi, per_subj = fmt(dev, idx, res, "Signed mean cross-lag deviation")
    lines.append(l1 + f" SD of the deviation across pairs within a run {dev_sd.mean():.4f}; mean absolute deviation {dev_abs.mean():.4f}. "
                 f"Run-level residual of the diagnostic on the same runs: {res.mean():+.4f} ({100 * res.mean() / obs.mean():+.1f} % of observed {obs.mean():.4f}). "
                 f"Mean pair a {a_mean.mean():.4f}, mean pair |q| {q_abs.mean():.4f}.")
    lines.append(f"Per-subject signed mean deviation (two runs): {np.array2string(per_subj, precision=5, floatmode='fixed', max_line_width=250)}")
    verdict = "near zero (CI includes zero)" if lo <= 0 <= hi else ("negative" if grand < 0 else "positive")
    lines.append(f"Reading under the pre-run entry of 15:35 UTC: {verdict}.")
    lines.append("")
    lines.append(f"Share of pairs with q < 0: {share_neg.mean():.3f} (DMT {share_neg[:, 0].mean():.3f}, PCB {share_neg[:, 1].mean():.3f}); "
                 f"mean deviation among the q > 0 pairs {np.nanmean(dev_pos):+.5f}, among the q < 0 pairs {np.nanmean(dev_neg):+.5f} (descriptive).")
    l2, grand_q, lo_q, hi_q, per_subj_q = fmt(devq, idx, res, "Sign(q)-weighted mean cross-lag deviation")
    lines.append(l2)
    lines.append(f"Per-subject sign(q)-weighted mean deviation (two runs): {np.array2string(per_subj_q, precision=5, floatmode='fixed', max_line_width=250)}")
    if lo_q <= 0 <= hi_q:
        verdict_q = "near zero (CI includes zero): pooling does not account for the run-level residual"
    elif grand_q < 0:
        verdict_q = "negative (CI excludes zero): the mechanism's signature is absent and the deviation has the sign that raises sts above the prediction"
    elif grand_q < REQUIRED / 2:
        verdict_q = f"positive but far below the ≈ +{REQUIRED} required (less than half of it): pooling does not account for the run-level residual"
    elif grand_q <= 2 * REQUIRED:
        verdict_q = f"positive and of the order required (within a factor of two of +{REQUIRED}): consistent with pooling as the source of the run-level residual"
    else:
        verdict_q = f"positive and above the order required (more than twice +{REQUIRED})"
    lines.append(f"Reading under the pre-run entry for this statistic: {verdict_q}.")
    l3, grand_s, lo_s, hi_s, per_subj_s = fmt(slope, idx, res, "Slope of the deviation on q across pairs (OLS, per run)", digits=4)
    lines.append(l3)
    lines.append(f"Per-subject slope (two runs): {np.array2string(per_subj_s, precision=4, floatmode='fixed', max_line_width=250)}")
    verdict_s = "near zero (CI includes zero)" if lo_s <= 0 <= hi_s else ("negative" if grand_s < 0 else "positive")
    lines.append(f"Reading: {verdict_s}.")
    lines.append("")
    print("\n".join(lines[-11:]), flush=True)
print(f"done in {time.time() - t0:.0f} s")
pd.DataFrame(rows).to_csv(OUT / "crosslag_deviation.csv", index=False)
(OUT / "crosslag_deviation_tables.md").write_text("\n".join(lines) + "\n")
print(f"wrote {OUT / 'crosslag_deviation_tables.md'} and crosslag_deviation.csv")
