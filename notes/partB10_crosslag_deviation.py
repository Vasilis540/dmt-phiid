"""
partB10_crosslag_deviation.py — run-level mean cross-lag deviation (the test of the pooling mechanism named
in Results 4 as a candidate explanation of the run-level residual; Limitations listed it as not run).
Pre-run entries: manuscript/analysis_record.md, "Run-level mean cross-lag deviation and the regional sts–r₁ test:
pre-run entry, 15 Sep 2026 15:35 UTC" (the signed mean, prediction recorded there), "The sign(q)-weighted
cross-lag deviation: pre-run entry, 15 Sep 2026" (the two statistics added after the fifth review, predictions
recorded there) and "The sign(q)-weighted deviation at W = 60 and on the finite-sample null: pre-run entry,
16 Sep 2026" (the two additions below, rules recorded there).

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

Additions of 16 Sep 2026 (the run-level section above is unchanged, and so are its numbers):
  A. W = 60. The same three statistics per window, from each window's own 4 × 4 matrices exactly as
     partB4_diagnostic.py builds them (kept TRs in [60w, 60(w + 1)), all 14 windows of each run, both runs, both
     variants; a_x, a_y and q from the window; the sign is that of the window's q), averaged over the run's windows
     to one value per subject and run, with the run-level inference (grand mean over subjects of the per-subject
     mean of the two runs, subject bootstrap from a generator seeded 20261120 that is separate from the run-level
     one, exact sign-flip p) and the correlation with the W = 60 residual of Table 4 per run
     (diag_series_<variant>_W60.npz, mean over the run's windows). The windows are checked against the saved
     diagnostic: the mean |deviation| of every window must equal diag_series' xcorr_dev.
  B. The finite-sample null of notes/review_v2_residual_null.py, regenerated from its own functions, generator
     and call sequence (homogeneous-filter check at W = 30, 60, 840, then the four operating-point cells at W = 60),
     with the residual values its log reports reproduced as a check. On the same simulated windows: the
     sign(q)-weighted mean of each pair-window's two deviations (window's own a_x, a_y, q and sign of q), averaged
     over each pair's windows, mean over pairs with its standard error across pairs; the signed mean likewise; and
     the OLS slope of the deviation on q across the pairs of each window index, averaged over window indices, with
     its standard error across window indices.

Outputs: notes/review_results/partB/crosslag_deviation_tables.md, crosslag_deviation.csv (one row per run; W = 60
columns added), crosslag_deviation_run.log (via run_all.sh's nstep, or stdout).
Run from the repository root: .venv/bin/python notes/partB10_crosslag_deviation.py   (about ten minutes)
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
import review_v2_residual_null as NULL          # seeds its own generator (20261120) at import; used only in section B
from scipy.optimize import brentq

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


def common_component_C(lam, a_s, a_n, loading=+1.0):
    """Population 4 × 4 correlation matrix of [x_t, y_t, x_(t+1), y_(t+1)] for x = s + n_x, y = ±s + n_y, with s of
    variance lam and lag-1 autocorrelation a_s, independent regional parts n_x, n_y of variance 1 − lam and lag-1
    autocorrelation a_n (16 Sep 2026: the third look-alike of Results 4)."""
    cov0 = loading * lam                                     # cov(x_t, y_t)
    auto1 = lam * a_s + (1 - lam) * a_n                      # cov(x_t, x_(t+1)) = cov(y_t, y_(t+1))
    cross1 = loading * lam * a_s                             # cov(x_t, y_(t+1)) = cov(y_t, x_(t+1))
    return np.array([[1, cov0, auto1, cross1], [cov0, 1, cross1, auto1], [auto1, cross1, 1, cov0], [cross1, auto1, cov0, 1]], float)


cc_checks = []
for lam, a_s, a_n in ((0.25, 0.95, 0.80), (0.10, 0.90, 0.85), (0.40, 0.80, 0.90)):
    for loading in (+1.0, -1.0):
        Cp = common_component_C(lam, a_s, a_n, loading)
        q_p = 0.5 * (Cp[0, 1] + Cp[2, 3]); d_p = Cp[0, 3] - Cp[1, 3] * q_p
        formula = loading * lam * (1 - lam) * (a_s - a_n)
        assert abs(d_p - formula) < 1e-15
        cc_checks.append(f"λ = {lam}, a_s = {a_s}, a_n = {a_n}, loading {loading:+.0f}: q = {q_p:+.3f}, d = {d_p:+.6f}, λ(1 − λ)(a_s − a_n)·sign = {formula:+.6f}")

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


def fmt(per_run, idx, res, name, digits=5, res_label="run-level residual"):
    grand, lo, hi, p, npos, per_subj = infer(per_run, idx)
    r_res = np.corrcoef(per_run.ravel(), res.ravel())[0, 1]
    line = (f"{name}: DMT {per_run[:, 0].mean():+.{digits}f}, PCB {per_run[:, 1].mean():+.{digits}f}; grand mean {grand:+.{digits}f} "
            f"[{lo:+.{digits}f}, {hi:+.{digits}f}] (subject bootstrap, {N_BOOT} draws), exact sign-flip p = {p:.4f}, "
            f"positive in {npos}/14 subjects; r(statistic, {res_label}) across the 28 runs {r_res:+.3f}.")
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
         f"gives a residual of {res_required:+.4f} (the ≈ −0.01 run-level residual on ts_gsr); at q = −0.25 the same +{REQUIRED} gives {res_required_neg:+.4f}.", "",
         "Population check of the common-slow-component identity (added 16 Sep 2026; x = s + n_x, y = ±s + n_y, λ = var(s)/var(x), equal regional "
         "variances; the true cross-lag correlation is ±λ a_s, the AR(1) substitution gives a_y q with a_y = λ a_s + (1 − λ) a_n and q = ±λ): "
         + "; ".join(cc_checks) + ".", ""]
rows = []
RUNLEVEL = {}
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
    RUNLEVEL[var] = grand_q
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
print(f"run-level section done in {time.time() - t0:.0f} s", flush=True)

# ============================================================================================ A. W = 60 (16 Sep 2026)
W = 60
N_WIN = 840 // W
rng60 = np.random.default_rng(SEED)
HALF, DOUBLE = 0.5, 2.0
lines += ["## A. W = 60 (addition of 16 Sep 2026)", "",
          "Per window, exactly as partB4_diagnostic.py (kept TRs in [60w, 60(w + 1)); PairPhiID on the window; a_x, a_y, q and the sign of q "
          "from the window's own matrices): the signed mean, the sign(q)-weighted mean and the OLS slope of the 2 × 6,555 deviations on q; "
          "averaged over the run's 14 windows; inference as at the run level (bootstrap draws from a separate generator seeded 20261120). "
          "Rule recorded before the run (analysis_record.md, pre-run entry of 16 Sep 2026): if pooling of non-stationary segments is the source, "
          "the ts_gsr W = 60 value should be markedly smaller than the run-level value (read as below half of it); if comparable (within a factor "
          "of two), a stationary mechanism is indicated and pooling is not distinguished by run length. r(·, residual) uses the W = 60 residual "
          "of the diagnostic per run (diag_series_<variant>_W60.npz, mean over windows).", ""]
w60 = {}
for var in ("ts_gsr", "ts_demean"):
    dg = np.load(OUT / f"diag_series_{var}_W60.npz")
    dev = np.full((14, 2, N_WIN), np.nan); devq = dev.copy(); slope = dev.copy(); share_neg = dev.copy(); dpos = dev.copy(); dneg = dev.copy()
    qabs = dev.copy(); amean = dev.copy()
    n_checked = 0
    for s, c in product(range(14), range(2)):
        X = np.asarray(ts[var][s, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        for w in range(N_WIN):
            in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
            if in_w.size <= 5:
                continue
            pp = PairPhiID(X[:, in_w]); C = pp.C
            ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
            d = np.r_[C[:, 0, 3] - ay * q, C[:, 1, 2] - ax * q]
            q2 = np.r_[q, q]
            assert abs(np.abs(d).mean() - dg["xcorr_dev"][s, c, w]) < 1e-10, (var, s, c, w)
            n_checked += 1
            dev[s, c, w] = d.mean(); devq[s, c, w] = (np.sign(q2) * d).mean(); slope[s, c, w] = np.polyfit(q2, d, 1)[0]
            share_neg[s, c, w] = (q < 0).mean(); dpos[s, c, w] = d[q2 > 0].mean(); dneg[s, c, w] = d[q2 < 0].mean()
            qabs[s, c, w] = np.abs(q).mean(); amean[s, c, w] = (0.5 * (ax + ay)).mean()
    res60 = np.nanmean(dg["res"], axis=2)                                   # (14, 2): the W = 60 residual per run
    dev_r, devq_r, slope_r = np.nanmean(dev, 2), np.nanmean(devq, 2), np.nanmean(slope, 2)
    idx60 = rng60.integers(0, 14, (N_BOOT, 14))
    lines.append(f"### {var} (W = 60; {n_checked} windows checked against diag_series xcorr_dev)")
    lines.append("")
    lines.append(f"Share of pairs with q < 0 (window q): {np.nanmean(share_neg):.3f}; mean deviation among the q > 0 pairs {np.nanmean(dpos):+.5f}, among the q < 0 pairs {np.nanmean(dneg):+.5f}; "
                 f"mean pair a {np.nanmean(amean):.4f}, mean pair |q| {np.nanmean(qabs):.4f}; W = 60 residual of the diagnostic {np.nanmean(res60):+.4f} (descriptive).")
    l1, g1, lo1, hi1, ps1 = fmt(dev_r, idx60, res60, "W = 60 signed mean cross-lag deviation", res_label="W = 60 residual of the diagnostic, mean over the run's windows")
    lines.append(l1)
    l2, g2, lo2, hi2, ps2 = fmt(devq_r, idx60, res60, "W = 60 sign(q)-weighted mean cross-lag deviation", res_label="W = 60 residual of the diagnostic, mean over the run's windows")
    lines.append(l2)
    lines.append(f"Per-subject W = 60 sign(q)-weighted mean deviation (two runs): {np.array2string(ps2, precision=5, floatmode='fixed', max_line_width=250)}")
    rl = RUNLEVEL[var]
    ratio = g2 / rl
    if var == "ts_gsr":
        if g2 < HALF * rl:
            verdict = f"markedly smaller than the run-level {rl:+.5f} (ratio {ratio:.2f}, below half): the branch pooling requires"
        elif g2 <= DOUBLE * rl:
            verdict = f"comparable to the run-level {rl:+.5f} (ratio {ratio:.2f}, within a factor of two): a stationary mechanism is indicated and pooling is not distinguished by run length"
        else:
            verdict = f"larger than the run-level {rl:+.5f} (ratio {ratio:.2f}, more than twice)"
        lines.append(f"Reading under the rule of 16 Sep 2026: {verdict}.")
    else:
        lines.append(f"Ratio to the run-level value {rl:+.5f}: {ratio:.2f} (no rule for this variant).")
    l3, g3, lo3, hi3, ps3 = fmt(slope_r, idx60, res60, "W = 60 slope of the deviation on q across pairs (OLS per window, mean over windows)", digits=4, res_label="W = 60 residual of the diagnostic, mean over the run's windows")
    lines.append(l3)
    lines.append("")
    w60[var] = dict(dev=dev_r, devq=devq_r, slope=slope_r, res=res60)
    print("\n".join(lines[-9:]), flush=True)
for r in rows:
    k = 0 if r["condition"] == "DMT" else 1
    v = w60[r["variant"]]
    r["w60_mean_crosslag_deviation"] = v["dev"][r["subject"] - 1, k]
    r["w60_signq_weighted_mean_deviation"] = v["devq"][r["subject"] - 1, k]
    r["w60_slope_deviation_on_q"] = v["slope"][r["subject"] - 1, k]
    r["w60_residual"] = v["res"][r["subject"] - 1, k]
print(f"W = 60 section done in {time.time() - t0:.0f} s", flush=True)

# ============================================================================================ B. finite-sample null (16 Sep 2026)
RL = RUNLEVEL["ts_gsr"]
NEAR, COMPARABLE = 0.1, 0.5
lines += ["## B. The finite-sample null of notes/review_v2_residual_null.py (addition of 16 Sep 2026)", "",
          "Regenerated from the null's own functions, generator (seeded 20261120 at import) and call sequence; its construction sets the population "
          "cross-lag correlation to exactly r1·q (one filter per pair, shared by the pair's two series). Per pair-window: the two deviations from the "
          "window's a_x, a_y, q; sign(q)-weighted mean = mean of sign(q) × deviation, averaged over the pair's windows, then mean over pairs ± SE across "
          "pairs; slope = OLS of the deviation on q across the pairs of each window index, mean over window indices ± SE across them. "
          "Rule recorded before the run (analysis_record.md, pre-run entry of 16 Sep 2026), at W = 840 against the run-level ts_gsr value: near zero "
          "(|value| below a tenth of it) removes finite sampling as a source of the signature; comparable (at least half of it) means the statistic is "
          "not diagnostic; in between, reported as the share finite sampling produces, neither branch claimed.", ""]


def null_stats(C, n_pairs):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; qm = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    d_xy, d_yx = C[:, 0, 3] - ay * qm, C[:, 1, 2] - ax * qm
    n_w = C.shape[0] // n_pairs                                              # window_corr concatenates window by window
    sq = np.sign(qm)
    devq_pw = (0.5 * sq * (d_xy + d_yx)).reshape(n_w, n_pairs)
    dev_pw = (0.5 * (d_xy + d_yx)).reshape(n_w, n_pairs)
    devq_pair, dev_pair = devq_pw.mean(0), dev_pw.mean(0)
    q_w, dxy_w, dyx_w = qm.reshape(n_w, n_pairs), d_xy.reshape(n_w, n_pairs), d_yx.reshape(n_w, n_pairs)
    slopes = np.array([np.polyfit(np.r_[q_w[k], q_w[k]], np.r_[dxy_w[k], dyx_w[k]], 1)[0] for k in range(n_w)])
    se = lambda v: v.std(ddof=1) / np.sqrt(v.size)
    return dict(devq=devq_pair.mean(), devq_se=se(devq_pair), dev=dev_pair.mean(), dev_se=se(dev_pair),
                slope=slopes.mean(), slope_se=(se(slopes) if slopes.size > 1 else np.nan), n_w=n_w,
                share_neg=(qm < 0).mean(), qabs=np.abs(qm).mean())


def null_line(label, st, obs, pred):
    lo, hi = st["devq"] - 1.96 * st["devq_se"], st["devq"] + 1.96 * st["devq_se"]
    return (f"{label}: residual {np.mean(obs - pred):+.4f} ({100 * np.mean(obs - pred) / np.mean(obs):+.2f} %); share of pair-windows with q < 0 {st['share_neg']:.3f}, mean |q| {st['qabs']:.3f}; "
            f"sign(q)-weighted mean deviation {st['devq']:+.5f} ± {st['devq_se']:.5f} (SE; 95 % [{lo:+.5f}, {hi:+.5f}]); signed mean {st['dev']:+.5f} ± {st['dev_se']:.5f}; "
            f"slope on q {st['slope']:+.4f} ± {st['slope_se']:.4f} over {st['n_w']} window indices")


t1 = time.time()
fits = {k: NULL.fit_filter(t) for k, t in NULL.TARGET_ACF.items()}
lines.append("Homogeneous-filter check (placebo ACF; 2,000 pairs × 8,400 TRs per window length), as the null's first section; its log reports residual −8.52 %, −3.10 %, −0.34 % at W = 30, 60, 840:")
null_values = {}
for Wn in (30, 60, 840):
    betas = np.clip(NULL.rng.normal(200, 100, 2000), 5, None); qn = np.clip(NULL.rng.normal(0, 0.27, 2000), -0.95, 0.95)
    Xn, Yn = NULL.gen(2000, 8400, betas, fits["placebo"][2], fits["placebo"][3], qn)
    Cn = NULL.window_corr(Xn, Yn, Wn)
    obs, pred, a_, aq_ = NULL.residual(Cn)
    st = null_stats(Cn, 2000)
    null_values[Wn] = st
    lines.append(null_line(f"W = {Wn}", st, obs, pred))
    print(lines[-1], f"({time.time() - t1:.0f} s)", flush=True)
    del Xn, Yn, Cn


def null_cell(target_a, target_q, lo, hi, W=60, n_pairs=3000, T=3000, bsd=0.5):
    """review_v2_residual_null.cell, with the same draws in the same order, returning the final windows' matrices."""
    def draw(bmean, qsd):
        betas = np.clip(NULL.rng.normal(bmean, bsd * bmean, n_pairs), 5, None); q = np.clip(NULL.rng.normal(0, qsd, n_pairs), -0.95, 0.95)
        Xc, Yc = NULL.gen(n_pairs, T, betas, lo, hi, q)
        Cc = NULL.window_corr(Xc, Yc, W)
        return Cc, NULL.residual(Cc)
    bmean = brentq(lambda b: draw(b, 0.27)[1][2].mean() - target_a, 20, 800, xtol=3)
    qsd = brentq(lambda sd: draw(bmean, sd)[1][3].mean() - target_q, 0.05, 0.9, xtol=0.005)
    Cc, (obs, pred, a_, aq_) = draw(bmean, qsd)
    return Cc, obs, pred


lines.append("")
lines.append("Operating-point cells (W = 60; 3,000 pairs × 50 windows each), as the null's second section; its log reports residual −0.0353, −0.0313, −0.0350, −0.0364 and a DiD of +0.0054:")
cell_res, cell_devq = {}, {}
for name, (ta, tq, acf) in NULL.CELLS.items():
    Cc, obs, pred = null_cell(ta, tq, fits[acf][2], fits[acf][3])
    st = null_stats(Cc, 3000)
    cell_res[name] = np.mean(obs - pred); cell_devq[name] = st
    lines.append(null_line(name, st, obs, pred))
    print(lines[-1], f"({time.time() - t1:.0f} s)", flush=True)
did = (cell_res["DMT post"] - cell_res["DMT pre"]) - (cell_res["PCB post"] - cell_res["PCB pre"])
cells_devq = np.mean([v["devq"] for v in cell_devq.values()]); cells_se = np.sqrt(np.sum([v["devq_se"] ** 2 for v in cell_devq.values()])) / 4
lines.append(f"Null residual DiD {did:+.4f} (log: +0.0054). Mean of the four cells' sign(q)-weighted mean deviation {cells_devq:+.5f} ± {cells_se:.5f} (SE).")
lines.append("")
v840 = null_values[840]["devq"]
share = v840 / RL
if abs(v840) < NEAR * RL:
    verdict = f"near zero (|{v840:+.5f}| below a tenth of the run-level {RL:+.5f}; share {share:+.3f}): finite sampling is removed as a source of the signature"
elif v840 >= COMPARABLE * RL:
    verdict = f"comparable to the run-level {RL:+.5f} (share {share:.2f}, at least half): the statistic is not diagnostic"
elif v840 > 0:
    verdict = f"between the two branches: finite sampling produces {100 * share:.0f} % of the run-level {RL:+.5f}; neither branch is claimed"
else:
    verdict = f"negative beyond a tenth of the run-level value ({v840:+.5f}; share {share:+.3f}): finite sampling pushes the statistic the other way"
lines.append(f"Reading under the rule of 16 Sep 2026 (W = 840 against the run-level ts_gsr value): {verdict}.")
w60g = w60["ts_gsr"]["devq"].mean(1).mean()
lines.append(f"At W = 60 (descriptive, no rule): null {null_values[60]['devq']:+.5f} (homogeneous filter) and {cells_devq:+.5f} (four cells) against the data's ts_gsr W = 60 value {w60g:+.5f}.")
lines.append("")
print("\n".join(lines[-4:]), flush=True)
print(f"done in {time.time() - t0:.0f} s")
pd.DataFrame(rows).to_csv(OUT / "crosslag_deviation.csv", index=False)
(OUT / "crosslag_deviation_tables.md").write_text("\n".join(lines) + "\n")
print(f"wrote {OUT / 'crosslag_deviation_tables.md'} and crosslag_deviation.csv")
