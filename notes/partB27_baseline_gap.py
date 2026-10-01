"""
partB27_baseline_gap.py — B27: the pre-injection gap between the two runs, the post-injection gap, the baseline-adjusted
contrast, and what the per-subject relations rest on; with the leave-one-out and leave-two-out of the residual's
per-subject slope, the sensitivity of the residual's test and Fieller's g.
Pre-run entry: manuscript/analysis_record.md, "The pre-injection gap and the per-subject relations (B27): pre-run
entry" (specification, predictions and rule).

For each quantity below, per subject, from the saved series at W = 60 (and W = 30 on ts_gsr for all four): the pre-injection
mean of each run (windows 1–4), the post-injection mean (windows 6–14; at W = 30 bins 1–8 and 11–28), the pre-injection
gap (DMT pre − placebo pre), the post-injection gap (DMT post − placebo post) and the DiD (post gap − pre gap, the
identity DiD = (DMT post − DMT pre) − (placebo post − placebo pre)). The quantities: whole-brain MMI-sts (observed), the
whole-brain lag-1 autocorrelation r₁ (regional, averaged; rev_series.autocorr_series in window mode), the
AR(1)-substituted sts and the residual (observed minus substituted) of partB4, on ts_gsr and ts_demean.
Statistics (exact sign-flip p over the 2^14 assignments, as everywhere; for the means, B21's inverted sign-flip 95 %
intervals, rev_inference_inverted.signflip_inversion, the text's interval for a mean over subjects; t intervals on 12 df
for regression coefficients): the gap's and the post gap's mean, p and share of subjects; the baseline-adjusted contrast,
the intercept of the regression of the post gap on the pre gap (the post gap expected at a pre gap of zero, the
expectation of the gap under the counterbalanced order), with its slope; the correlation of the DiD with the pre gap
and with the post gap; across quantities, on each variant, the per-subject correlations r(sts DiD, r₁ DiD), r(sts pre
gap, r₁ DiD), r(sts post gap, r₁ post gap), r(sts pre gap, r₁ pre gap) and r(sts DiD, r₁ DiD | sts pre gap) (the
partial correlation given the sts pre gap).
Then, on ts_gsr at W = 60: the OLS slope of the residual DiD on the r₁ DiD (the data's −0.75 per unit; the intercept
free, as in B21 (c)) with its t interval, recomputed with each subject left out (14 slopes) and each pair of subjects
left out (91 slopes): the range of the slopes, the number of intervals that contain zero and that contain each of the
three generator rates of Table 3 (−0.18, −0.39, −0.37); the same for the correlation r(sts DiD, r₁ DiD); the minimal
difference from a point expectation that the residual DiD's test detects with 80 % power at the two-sided 5 % level
(the one-sample t approximation on 13 df, SE = SD/√14); and Fieller's g = (t · SE(denominator) / denominator)² for the
two ratio intervals of Results 2 and 4 (sts DiD and residual DiD per unit of whole-brain r₁ DiD).
Free choices: the regression with intercept; the t approximation for the sensitivity; the three rates compared.
No new data are read beyond the released series the saved series come from (the .mat, for r₁, as rev_series reads it).
The script stops unless the per-subject DiDs of the saved sts, r₁ and residual series at W = 60 and W = 30 equal the
saved ones (B21's inputs) to 10⁻⁹.
Outputs (notes/review_results/partB/): baseline_gap_tables.md, baseline_gap.csv (one row per quantity × variant ×
subject), baseline_gap_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB27_baseline_gap.py   (seconds)
--smoke: for a shape test on a tree whose saved series are not the data's (the planning session's test on synthetic
files): the checks that the series reproduce the saved per-subject DiDs are printed instead of enforced.
"""
import pickle
import sys
import time
from itertools import combinations, product
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_series import autocorr_series
from rev_inference_inverted import signflip_inversion
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
S = 15                                                                    # sts in the atom order of rev_series.ATOMS
RATES = {"band-passed": -0.18, "AR(1)": -0.39, "null": -0.37}             # Table 3's generator rates per unit of pair r₁
SIGNS = np.array(list(product((-1, 1), repeat=14)))
SMOKE = "--smoke" in sys.argv
t0 = time.time()


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def tint(v):
    """mean and B21's inverted sign-flip 95 % interval (the interval of the paper for a mean over subjects)."""
    r = signflip_inversion(np.asarray(v, float))
    assert r["grid_violations"] == 0, "the inverted interval's grid check"
    return r["mean"], r["lo"], r["hi"]


def ols(x, y):
    """slope, its 95 % t interval (n − 2 df), intercept and its interval, r."""
    x, y = np.asarray(x, float), np.asarray(y, float); n = x.size
    X = np.c_[np.ones(n), x]; b = np.linalg.lstsq(X, y, rcond=None)[0]; e = y - X @ b
    cov = (e ** 2).sum() / (n - 2) * np.linalg.inv(X.T @ X); t = stats.t.ppf(0.975, n - 2)
    return b[1], b[1] - t * np.sqrt(cov[1, 1]), b[1] + t * np.sqrt(cov[1, 1]), b[0], b[0] - t * np.sqrt(cov[0, 0]), b[0] + t * np.sqrt(cov[0, 0]), np.corrcoef(x, y)[0, 1]


def partial_r(x, y, z):
    rxy, rxz, ryz = np.corrcoef(x, y)[0, 1], np.corrcoef(x, z)[0, 1], np.corrcoef(y, z)[0, 1]
    return (rxy - rxz * ryz) / np.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))


def fieller_g(y, x):
    n = x.size; t = stats.t.ppf(0.975, n - 1)
    return (t * x.std(ddof=1) / np.sqrt(n) / x.mean()) ** 2


def pdid(pkl, label, st="primary"):
    for d in pickle.load(open(RR / pkl, "rb")):
        if d["label"] == label and d["set"] == st:
            return np.asarray(d["did_subjects"], float)
    raise KeyError(label)


# ---------------------------------------------------------------- the series
ts = sio.loadmat(MAT)
SERIES = {}                                                               # (quantity, variant, W) -> (14, 2, n_win)
for var in ("ts_gsr", "ts_demean"):
    SERIES[("sts", var, 60)] = np.load(REPO / "results" / f"atoms_win60_115regions-all_{var}_window.npy")[..., S]
    SERIES[("r1", var, 60)] = autocorr_series(ts[var], 60, "window")[0]
    z = np.load(OUT / f"diag_series_{var}_W60.npz")
    SERIES[("substituted", var, 60)] = z["pred"]; SERIES[("residual", var, 60)] = z["res"]
    same = np.allclose(z["obs"], SERIES[("sts", var, 60)], equal_nan=True)
    assert same or SMOKE, "the diagnostic's observed series is the atoms file's"
    if not same:
        print(f"   SMOKE: diag_series_{var}_W60.npz obs differs from the atoms file", flush=True)
SERIES[("sts", "ts_gsr", 30)] = np.load(REPO / "results" / "atoms_win30_115regions-all_ts_gsr_window.npy")[..., S]
SERIES[("r1", "ts_gsr", 30)] = autocorr_series(ts["ts_gsr"], 30, "window")[0]
z = np.load(OUT / "diag_series_ts_gsr_W30.npz")
SERIES[("substituted", "ts_gsr", 30)] = z["pred"]; SERIES[("residual", "ts_gsr", 30)] = z["res"]
# the saved per-subject DiDs (B21's inputs) must be those the series give, at W = 60 and at W = 30
for var, W in (("ts_gsr", 60), ("ts_demean", 60), ("ts_gsr", 30)):
    pre, post = (slice(0, 4), slice(5, 14)) if W == 60 else (slice(0, 8), slice(10, 28))
    for q, pkl, lab in (("sts", "inference_rows_raw.pkl", f"sts {var} W{W}"), ("r1", "inference_rows_raw.pkl", f"autocorr {var} W{W}"),
                        ("residual", "inference_rows_diag.pkl", f"diag residual sts {var} W{W}")):
        x = SERIES[(q, var, W)]
        did = (np.nanmean(x[:, 0, post], 1) - np.nanmean(x[:, 0, pre], 1)) - (np.nanmean(x[:, 1, post], 1) - np.nanmean(x[:, 1, pre], 1))
        same = np.allclose(did, pdid(pkl, lab), atol=1e-9)
        assert same or SMOKE, (q, var, W)
        if not same:
            print(f"   SMOKE: the DiDs of {q} {var} W{W} differ from the saved ones", flush=True)
print(f"   series read; the per-subject DiDs {'checked against' if SMOKE else 'equal'} the saved ones ({time.time() - t0:.0f}s)", flush=True)


def gaps(x, W):
    pre, post = (slice(0, 4), slice(5, 14)) if W == 60 else (slice(0, 8), slice(10, 28))
    dpre, dpost = np.nanmean(x[:, 0, pre], 1), np.nanmean(x[:, 0, post], 1)
    ppre, ppost = np.nanmean(x[:, 1, pre], 1), np.nanmean(x[:, 1, post], 1)
    return dpre, dpost, ppre, ppost, dpre - ppre, dpost - ppost


lines = ["# The pre-injection gap and the per-subject relations (partB27_baseline_gap.py)", f"git={SHA}", "",
         "Per subject: pre = mean of windows 1–4 (bins 1–8 at W = 30), post = windows 6–14 (bins 11–28); pre gap = DMT pre − placebo pre; post gap = "
         "DMT post − placebo post; DiD = post gap − pre gap. Means with B21's inverted sign-flip 95 % intervals and exact sign-flip p (2^14 assignments); "
         "'adjusted' = the intercept of the OLS regression of the post gap on the pre gap (the post gap expected at a pre gap of zero), with its 95 % t "
         "interval (12 df), and the regression's slope; r(DiD, pre gap) and r(DiD, post gap) across the 14 subjects. nats for sts and the residual; r₁ dimensionless.", "",
         "## (a) The gaps, the DiD and the baseline-adjusted contrast", "",
         "| quantity | variant | W | pre gap (DMT − placebo) | p; share > 0 | post gap | p; share < 0 | DiD | p | adjusted (post gap at pre gap 0) | slope on pre gap | r(DiD, pre gap) | r(DiD, post gap) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
csv = ["quantity,variant,W,subject,dmt_pre,dmt_post,pcb_pre,pcb_post,pre_gap,post_gap,did"]
G = {}
for (q, var, W), x in SERIES.items():
    dpre, dpost, ppre, ppost, g, pg = gaps(x, W)
    did = (dpost - dpre) - (ppost - ppre)
    assert np.allclose(did, pg - g)
    G[(q, var, W)] = dict(pre_gap=g, post_gap=pg, did=did, dmt_pre=dpre, dmt_post=dpost, pcb_pre=ppre, pcb_post=ppost)
    m, lo, hi = tint(g); mp, plo, phi = tint(pg); md, dlo, dhi = tint(did)
    sl, sl_lo, sl_hi, ic, ic_lo, ic_hi, _ = ols(g, pg)
    lines.append(f"| {q} | {var} | {W} | {m:+.4f} [{lo:+.4f}, {hi:+.4f}] | {signflip_p(g):.4f}; {int((g > 0).sum())}/14 | {mp:+.4f} [{plo:+.4f}, {phi:+.4f}] | {signflip_p(pg):.4f}; {int((pg < 0).sum())}/14 | "
                 f"{md:+.4f} [{dlo:+.4f}, {dhi:+.4f}] | {signflip_p(did):.4f} | {ic:+.4f} [{ic_lo:+.4f}, {ic_hi:+.4f}] | {sl:+.3f} [{sl_lo:+.3f}, {sl_hi:+.3f}] | {np.corrcoef(did, g)[0, 1]:+.3f} | {np.corrcoef(did, pg)[0, 1]:+.3f} |")
    for s in range(14):
        csv.append(f"{q},{var},{W},{s + 1},{dpre[s]:.6f},{dpost[s]:.6f},{ppre[s]:.6f},{ppost[s]:.6f},{g[s]:.6f},{pg[s]:.6f},{did[s]:.6f}")

lines += ["", "## (b) The per-subject relations of sts and the residual with r₁: DiDs, gaps and the partial correlation", "",
          "| variant | W | r(sts DiD, r₁ DiD) | r(sts pre gap, r₁ DiD) | r(sts pre gap, r₁ pre gap) | r(sts post gap, r₁ post gap) | r(sts DiD, r₁ DiD given sts pre gap) | r(residual DiD, r₁ DiD) | r(residual pre gap, r₁ DiD) | r(residual post gap, r₁ post gap) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
for var, W in (("ts_gsr", 60), ("ts_demean", 60), ("ts_gsr", 30)):
    s_, r_, e_ = G[("sts", var, W)], G[("r1", var, W)], G[("residual", var, W)]
    c = lambda a, b: f"{np.corrcoef(a, b)[0, 1]:+.3f}"
    lines.append(f"| {var} | {W} | {c(s_['did'], r_['did'])} | {c(s_['pre_gap'], r_['did'])} | {c(s_['pre_gap'], r_['pre_gap'])} | {c(s_['post_gap'], r_['post_gap'])} | "
                 f"{partial_r(s_['did'], r_['did'], s_['pre_gap']):+.3f} | {c(e_['did'], r_['did'])} | {c(e_['pre_gap'], r_['did'])} | {c(e_['post_gap'], r_['post_gap'])} |")

# ---------------------------------------------------------------- (c) the residual's slope: leave-one-out and leave-two-out; sensitivity; Fieller's g
r1, sts, res = G[("r1", "ts_gsr", 60)]["did"], G[("sts", "ts_gsr", 60)]["did"], G[("residual", "ts_gsr", 60)]["did"]
full = ols(r1, res)
lines += ["", "## (c) ts_gsr, W = 60: the residual DiD on the r₁ DiD across subjects, with subjects left out; the test's sensitivity; Fieller's g", "",
          f"All 14 subjects: slope {full[0]:+.3f} [{full[1]:+.3f}, {full[2]:+.3f}], r = {full[6]:+.3f}; r(sts DiD, r₁ DiD) = {np.corrcoef(sts, r1)[0, 1]:+.3f}.", "",
          "| subjects left out | slopes (min to max) | intervals containing 0 | containing −0.18 (band-passed) | containing −0.39 (AR(1)) | containing −0.37 (null) | r(residual DiD, r₁ DiD) (min to max) | r(sts DiD, r₁ DiD) (min to max) |",
          "|---|---|---|---|---|---|---|---|"]
for k, label in ((1, "one (14 sets)"), (2, "two (91 sets)")):
    sl, lo, hi, rr, rs = [], [], [], [], []
    for drop in combinations(range(14), k):
        keep = [i for i in range(14) if i not in drop]
        o = ols(r1[keep], res[keep]); sl.append(o[0]); lo.append(o[1]); hi.append(o[2]); rr.append(o[6]); rs.append(np.corrcoef(sts[keep], r1[keep])[0, 1])
    lo, hi = np.array(lo), np.array(hi)
    cont = lambda v: int(((lo <= v) & (v <= hi)).sum())
    lines.append(f"| {label} | {min(sl):+.3f} to {max(sl):+.3f} | {cont(0.0)} | {cont(RATES['band-passed'])} | {cont(RATES['AR(1)'])} | {cont(RATES['null'])} | {min(rr):+.3f} to {max(rr):+.3f} | {min(rs):+.3f} to {max(rs):+.3f} |")
named = {}
for drop, name in (((7,), "subject 8 (the largest fall of r₁)"), ((13,), "subject 14 (the rise of r₁)"), ((7, 13), "subjects 8 and 14")):
    keep = [i for i in range(14) if i not in drop]; o = ols(r1[keep], res[keep]); named[name] = o
    lines.append(f"| {name} | {o[0]:+.3f} [{o[1]:+.3f}, {o[2]:+.3f}] | — | — | — | — | {o[6]:+.3f} | {np.corrcoef(sts[keep], r1[keep])[0, 1]:+.3f} |")
se = res.std(ddof=1) / np.sqrt(14); mde = se * (stats.t.ppf(0.975, 13) + stats.t.ppf(0.80, 13))
g_sts, g_res = fieller_g(sts, r1), fieller_g(res, r1)
lines += ["", f"Sensitivity: the residual DiD's SE over subjects is {se:.4f} nats; the minimal difference from a point expectation detected with 80 % power at the two-sided 5 % level (one-sample t, 13 df) is "
          f"{mde:.4f} nats; the data's residual DiD, {res.mean():+.4f}, exceeds the three expectations (+0.0027, +0.0049, +0.0054) by {res.mean() - 0.0027:+.4f}, {res.mean() - 0.0049:+.4f} and {res.mean() - 0.0054:+.4f}.",
          f"Fieller's g (the squared ratio of the denominator's half-width to the denominator; the interval is finite for g < 1 and widens as g grows): {g_sts:.3f} for the sts DiD per unit of r₁ DiD and {g_res:.3f} for the residual DiD per unit of r₁ DiD "
          f"(the same denominator, the whole-brain r₁ DiD, mean {r1.mean():+.5f}, SE {r1.std(ddof=1) / np.sqrt(14):.5f}).", "",
          "## Reading under the rule of the pre-run entry", "",
          "Reported as computed: the entry's predictions (the r₁ pre gap positive and not significant, the post gap negative and significant, the pre gap the smaller; r(r₁ DiD, r₁ pre gap) below −0.5 and the adjusted r₁ contrast negative; "
          "r(sts pre gap, r₁ pre gap) and r(sts post gap, r₁ post gap) above 0.7) are read against (a) and (b) in the outcome entry; (c) and the values the entry lists as known are reported, not predicted; and the text's statements on the primary contrast, "
          "the shared variance of the two contrasts and the residual's per-subject slope follow the rule the entry sets."]
(OUT / "baseline_gap.csv").write_text(f"# partB27_baseline_gap.py; per subject: pre and post means of each run, the gaps and the DiD; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "baseline_gap_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
