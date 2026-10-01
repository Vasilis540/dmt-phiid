"""
partB28_matched_slope.py — B28: the residual's per-subject slope on the r₁ DiD under a pure autocorrelation change of the
data's heterogeneity, on the band-passed generator of B17b and on the AR(1) generator of B17, as a step and as a ramp (no
external data; reads the saved per-subject r₁ and residual DiDs and B17's pool of q).
Pre-run entry: manuscript/analysis_record.md, "The per-subject slope under a pure autocorrelation change of the data's
heterogeneity (B28): pre-run entry" (specification, predictions and rule).

The data's per-subject slope (Results 4; B21 (c)): the OLS slope of the residual DiD on the whole-brain r₁ DiD across the
14 subjects, −0.75 per unit, with its t interval [−1.13, −0.37]. Table 3's generator rates are ratios of group means
under one change applied to every subject. This script gives the generator's own per-subject slope, under a change
that differs between subjects as the data's r₁ DiDs differ: B17b's band-passed generator (its solved β̄ and σ_q: the
window-level mean a 0.8632 and mean |q| 0.2842 of the DMT pre-injection windows), 14 subjects × 2 runs × 300 pairs ×
840 samples, the placebo run stationary at the pre parameters, the DMT run's white noises filtered at the pre
parameters and at the subject's own post parameters β̄_s, solved so that the window-level mean a of the post filtering
is 0.8632 + Δa_s, where Δa_s is the subject's saved whole-brain r₁ DiD (inference_rows_raw.pkl, "autocorr ts_gsr W60",
B21's input) rescaled so that the fourteen Δa_s average −0.0150 (B17b's Δa); β̄_s is read from a table of the
window-level mean a against β̄ on calibration draws of the null's size (3,000 pairs × 3,000 samples, thirteen
multiples of β̄ from 0.03 to 3, interpolated in a), each β̄_s then checked on one calibration draw; the generator's
window-level a has a floor (the band-pass alone, at the smallest tilt, about 0.0375 below the pre level), so a Δa_s
below the floor is set to it and the subject named.
On B17's AR(1) generator (a_x, a_y ~ N(0.85, 0.0125), q drawn from the data's window-level pair q, the innovation
correlation solved for q, burn-in 200) the subject's change is a_x + Δa_s, a_y + Δa_s exactly. Four conditions: (i)
the band-passed generator with the step of B17b, the DMT run spliced from its pre-filtered to its post-filtered
version at sample 300 (window 6, the first primary window); (ii) the band-passed generator with a ramp, the DMT run
the mixture (1 − w_t) x_pre + w_t x_post with w_t = 0 before sample 300, rising linearly to 1 at sample 420 (over
windows 6 and 7) and 1 after, an autocorrelation change that is not stationary within the first two primary windows,
as a drug response that builds up over minutes is not; (iii) the AR(1) generator with the step of B17 at sample 300;
(iv) the AR(1) generator with the coefficients ramped linearly from a to a + Δa_s over samples 300–419.
Per replicate: B17b's analysis at W = 60 (analyse_run, copied; PairPhiID on the 300 pairs of each window; the
substituted estimate from the measured (a_x, a_y, q); the window-level pair a as window_corr and residual of
review_v2_residual_null.py give it, the quantity B17b's calibration matches); per subject the DiDs (windows 6–14 minus
1–4, DMT minus placebo) of observed sts, substituted sts, the residual and the window-level pair a; across subjects the
OLS slope of the residual DiD on the pair-a DiD with its 95 % t interval (12 df), the correlation, the ratio of the
group means (the per-replicate ratio), and the mean residual DiD. N_REP = 100 replicates per condition (--n-rep N for a smoke test); one
generator seeded 20261120: the calibration table first, then (i) to (iv).
Tables: per condition the mean, SD and 2.5th, 50th and 97.5th percentiles of the slope, of the correlation and of the
per-replicate ratio of means; the share of replicates whose slope is at or below the data's −0.753 and whose
correlation is at or below the data's −0.780 (B27's full-set values, re-read from the saved DiDs here); the ratio of
the replicate-mean residual DiD to the replicate-mean pair-a DiD, and the share of replicate slope intervals that
contain that ratio and that contain zero; the residual DiD, the sts DiD and the pair-a DiD (mean ± SD over
replicates), the first two to be read beside B17b's and B17's (i).
Free choices: the rescaling of the Δa_s to mean −0.0150; the floor; the ramp over two windows; the interpolation
table; 100 replicates; the slope with intercept.
Outputs (notes/review_results/partB/): matched_slope_tables.md, matched_slope.csv (one row per condition × replicate),
matched_slope_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB28_matched_slope.py   (about 40 min: B17b's and B17's rates per replicate)
"""
import pickle
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from review_v2_residual_null import psd_weights, fit_filter, window_corr, residual, TARGET_ACF
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
S = ATOMS.index("sts")
SEED = 20261120
TR = 2.0
N_PAIRS, N_SUBJ, T, W = 300, 14, 840, 60
N_REP = int(sys.argv[sys.argv.index("--n-rep") + 1]) if "--n-rep" in sys.argv else 100
CHANGE_AT, RAMP_END = 300, 420
CAL_PAIRS, CAL_T = 3000, 3000
TARGET_A, TARGET_Q, DA_MEAN = 0.8632, 0.2842, -0.0150
PRE, POST = np.arange(0, 4), np.arange(5, 14)
BETA_GRID = np.array([0.03, 0.06, 0.12, 0.2, 0.3, 0.5, 0.7, 0.85, 1.0, 1.2, 1.5, 2.0, 3.0])   # multiples of β̄ for the table a(β̄); 0.03 β̄ ≈ 5.6, near the clip at 5
BURN = 200
Q_POOL = np.load(OUT / "scope_map_overlay_points.npz")["pre_w1to4_q"]
Q_POOL = Q_POOL[np.isfinite(Q_POOL)]
t0 = time.time()
rng = np.random.default_rng(SEED)
PAIRS = [(2 * k, 2 * k + 1) for k in range(N_PAIRS)]


def pdid(pkl, label, st="primary"):
    for d in pickle.load(open(RR / pkl, "rb")):
        if d["label"] == label and d["set"] == st:
            return np.asarray(d["did_subjects"], float)
    raise KeyError(label)


def ols(x, y):
    n = x.size; X = np.c_[np.ones(n), x]; b = np.linalg.lstsq(X, y, rcond=None)[0]; e = y - X @ b
    se = np.sqrt((e ** 2).sum() / (n - 2) * np.linalg.inv(X.T @ X)[1, 1]); t = stats.t.ppf(0.975, n - 2)
    return b[1], b[1] - t * se, b[1] + t * se, np.corrcoef(x, y)[0, 1]


# ---------------------------------------------------------------- the data's per-subject r₁ DiDs and slope
R1 = pdid("inference_rows_raw.pkl", "autocorr ts_gsr W60")
RES = pdid("inference_rows_diag.pkl", "diag residual sts ts_gsr W60")
DATA_SLOPE, DATA_LO, DATA_HI, DATA_R = ols(R1, RES)
DA = R1 * (DA_MEAN / R1.mean())
print(f"   the data's r₁ DiDs (mean {R1.mean():+.5f}) rescaled to Δa_s with mean {DA.mean():+.4f}: {np.round(DA, 4).tolist()}; "
      f"the data's slope {DATA_SLOPE:+.3f} [{DATA_LO:+.3f}, {DATA_HI:+.3f}], r = {DATA_R:+.3f}", flush=True)

# ---------------------------------------------------------------- the generator (copied from partB17b_calibration_filtered.py, except where marked)
FIT = fit_filter(TARGET_ACF["placebo"])
LO, HI = FIT[2], FIT[3]
print(f"   filter fitted to the placebo ACF: beta={FIT[1]:.0f} lo={LO:.4f} hi={HI:.3f}", flush=True)


def filtered(e1, e2, betas_x, betas_y, n):
    f = np.fft.rfftfreq(n, d=TR)
    Hx = np.sqrt(psd_weights(f, betas_x, LO, HI)); Hy = np.sqrt(psd_weights(f, betas_y, LO, HI))
    return np.fft.irfft(np.fft.rfft(e1, axis=1) * Hx, n=n, axis=1), np.fft.irfft(np.fft.rfft(e2, axis=1) * Hy, n=n, axis=1)


def draw_noise(n_pairs, n, q):
    e1 = rng.standard_normal((n_pairs, n)); e2 = rng.standard_normal((n_pairs, n))
    return e1, q[:, None] * e1 + np.sqrt(1 - q[:, None] ** 2) * e2


def draw_params(n_pairs, bmean, qsd):
    betas = np.clip(rng.normal(bmean, 0.5 * bmean, n_pairs), 5, None)
    q = np.clip(rng.normal(0, qsd, n_pairs), -0.95, 0.95)
    return betas, q


def cal_stats(bmean, qsd):
    betas, q = draw_params(CAL_PAIRS, bmean, qsd)
    e1, e2 = draw_noise(CAL_PAIRS, CAL_T, q)
    X, Y = filtered(e1, e2, betas, betas, CAL_T)
    _, _, a, aq = residual(window_corr(X, Y, W))
    return a.mean(), aq.mean()


print("   solving β̄ and σ_q on calibration draws (3,000 pairs × 3,000 samples) ...", flush=True)
BMEAN = brentq(lambda b: cal_stats(b, 0.27)[0] - TARGET_A, 20, 800, xtol=1)
QSD = brentq(lambda s: cal_stats(BMEAN, s)[1] - TARGET_Q, 0.05, 0.9, xtol=0.005)
chk = cal_stats(BMEAN, QSD)
print(f"   solved: β̄ = {BMEAN:.1f}, σ_q = {QSD:.4f}; check draw: a = {chk[0]:.4f}, |q| = {chk[1]:.4f} ({time.time() - t0:.0f}s)", flush=True)
# the table a(β̄) and each subject's β̄_s (B28's addition)
A_TAB = np.array([cal_stats(BMEAN * m, QSD)[0] for m in BETA_GRID])
assert np.all(np.diff(A_TAB) > 0), "a(β̄) is not increasing on the grid"
FLOOR = A_TAB[0] - TARGET_A                                                 # the most negative Δa the generator reaches
DA_BP = np.maximum(DA, FLOOR)
FLOORED = [s + 1 for s in range(N_SUBJ) if DA[s] < FLOOR]
BETA_S = np.interp(TARGET_A + DA_BP, A_TAB, BMEAN * BETA_GRID)
A_CHK = np.array([cal_stats(b, QSD)[0] for b in BETA_S])
print("   table a(β̄): " + ", ".join(f"{m:g}β̄ → {a:.4f}" for m, a in zip(BETA_GRID, A_TAB)) + f"; floor Δa = {FLOOR:+.4f}; subjects at the floor: {FLOORED or 'none'}", flush=True)
print("   β̄_s and the check draws' a − 0.8632: " + ", ".join(f"{b:.0f} ({a - TARGET_A:+.4f} for {d:+.4f})" for b, a, d in zip(BETA_S, A_CHK, DA_BP)) + f" ({time.time() - t0:.0f}s)", flush=True)


# ---------------------------------------------------------------- B17's AR(1) generator (its innov_corr and simulate_run, the change per pair ramped when asked)
def innov_corr(ax, ay, q_target):
    """Innovation correlation that gives lag-0 correlation q_target for the uncoupled pair (B17's)."""
    return np.clip(q_target * (1 - ax * ay) / np.sqrt((1 - ax ** 2) * (1 - ay ** 2)), -0.999, 0.999)


def simulate_run_ar1(ax, ay, qe, da, ramp):
    """One run of N_PAIRS independent AR(1) pairs; the coefficients change by da from CHANGE_AT (a step, or a ramp to RAMP_END)."""
    n = ax.size
    E1 = rng.standard_normal((n, T + BURN)); E2 = rng.standard_normal((n, T + BURN))
    E2 = qe[:, None] * E1 + np.sqrt(1 - qe[:, None] ** 2) * E2
    x = np.zeros((n, T + BURN)); y = np.zeros((n, T + BURN))
    for t in range(1, T + BURN):
        tt = t - BURN
        w = 0.0 if tt < CHANGE_AT else (min(1.0, (tt - CHANGE_AT) / (RAMP_END - CHANGE_AT)) if ramp else 1.0)
        x[:, t] = (ax + w * da) * x[:, t - 1] + E1[:, t]
        y[:, t] = (ay + w * da) * y[:, t - 1] + E2[:, t]
    X = np.empty((2 * n, T)); X[0::2] = x[:, BURN:]; X[1::2] = y[:, BURN:]
    return X


def simulate_run(betas, q, beta_post, ramp):
    """One run of N_PAIRS pairs: stationary at betas when beta_post is None; else the DMT run with the post parameters β̄_s/β̄ from CHANGE_AT, as a step or a ramp."""
    e1, e2 = draw_noise(N_PAIRS, T, q)
    x, y = filtered(e1, e2, betas, betas, T)
    if beta_post is not None:
        bp = np.clip(betas * (beta_post / BMEAN), 5, None)                   # clipped at 5, as B17b clips its post β
        xp, yp = filtered(e1, e2, bp, bp, T)
        w = np.zeros(T)
        if ramp:
            w[CHANGE_AT:RAMP_END] = np.arange(RAMP_END - CHANGE_AT) / (RAMP_END - CHANGE_AT); w[RAMP_END:] = 1.0
        else:
            w[CHANGE_AT:] = 1.0
        x = (1 - w) * x + w * xp; y = (1 - w) * y + w * yp
    X = np.empty((2 * N_PAIRS, T)); X[0::2] = x; X[1::2] = y
    return X


def analyse_run(X):
    """Window (14,) whole-pair means of observed sts, substituted sts and the window-level pair a (B17b's analyse_run, W = 60 only, with a added)."""
    obs_w = np.empty(14); pred_w = np.empty(14); a_w = np.empty(14)
    for w in range(14):
        pp = PairPhiID(X[:, w * W:(w + 1) * W], pairs=PAIRS)
        ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]; q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
        obs_w[w] = pp.atoms_mean()[:, S].mean(); pred_w[w] = np.nanmean(atoms_from_corr(ar1_corr(ax, ay, q))[:, S])
        a_w[w] = (0.5 * (ax + ay)).mean()
    return obs_w, pred_w, a_w


def did(x):
    ch = x[:, :, POST].mean(2) - x[:, :, PRE].mean(2)
    return ch[:, 0] - ch[:, 1]


# ---------------------------------------------------------------- the replicates
lines = ["# The per-subject slope under a pure autocorrelation change of the data's heterogeneity (partB28_matched_slope.py)", f"git={SHA}", "",
         f"B17b's band-passed generator (β̄ = {BMEAN:.1f}, σ_q = {QSD:.4f}; window-level mean a {chk[0]:.4f}, |q| {chk[1]:.4f} on the check draw), {N_SUBJ} subjects × 2 runs × {N_PAIRS} pairs × {T} samples; "
         f"the DMT run's post parameters β̄_s per subject so that its window-level mean a is 0.8632 + Δa_s, Δa_s the subject's whole-brain r₁ DiD rescaled to mean {DA_MEAN:+.4f} "
         f"(Δa_s: {', '.join(f'{d:+.4f}' for d in DA)}; the generator's floor is Δa = {FLOOR:+.4f}, below which subjects {FLOORED or 'none'} are set to it; β̄_s: {', '.join(f'{b:.0f}' for b in BETA_S)}; "
         f"the check draws give a − 0.8632 of {', '.join(f'{a - TARGET_A:+.4f}' for a in A_CHK)}). B17's AR(1) generator (a_x, a_y ~ N(0.85, 0.0125), q from the data's window-level pair q, burn-in {BURN}): the subject's change is "
         f"exactly Δa_s on both coefficients. (i) and (iii) the step at sample {CHANGE_AT}; (ii) and (iv) the ramp from sample {CHANGE_AT} to {RAMP_END}. W = {W}; DiD = windows 6–14 minus 1–4, DMT minus placebo; the slope = OLS of the residual DiD on the pair-a DiD across the 14 subjects "
         f"(intercept free), with its 95 % t interval (12 df); {N_REP} replicates per condition; seed {SEED}.", "",
         f"The data (ts_gsr, W = 60): slope {DATA_SLOPE:+.3f} [{DATA_LO:+.3f}, {DATA_HI:+.3f}] per unit of whole-brain r₁ DiD, r = {DATA_R:+.3f}; ratio of means {RES.mean() / R1.mean():+.3f} per unit of whole-brain r₁ DiD (the main text's −0.74 is per unit of pair r₁).", "",
         "| condition | slope: mean ± SD | slope percentiles 2.5 / 50 / 97.5 | share of replicates with slope ≤ the data's | r: mean ± SD | r percentiles 2.5 / 50 / 97.5 | share with r ≤ the data's | per-replicate ratio of means: mean ± SD | its percentiles 2.5 / 50 / 97.5 | ratio of the replicate-mean DiDs | slope intervals containing that ratio; containing 0 | residual DiD | sts DiD | pair-a DiD |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
csv = ["condition,replicate,slope,slope_lo,slope_hi,r,ratio_of_means,res_did,sts_did,a_did"]
for cond, gen, ramp in (("(i) band-passed, step", "bp", False), ("(ii) band-passed, ramp", "bp", True), ("(iii) AR(1), step", "ar1", False), ("(iv) AR(1), ramp", "ar1", True)):
    SL, LO_, HI_, RRS, RATIO, RESD, STSD, AD = [], [], [], [], [], [], [], []
    for rep in range(N_REP):
        obs = np.empty((N_SUBJ, 2, 14)); pred = np.empty((N_SUBJ, 2, 14)); a = np.empty((N_SUBJ, 2, 14))
        for s in range(N_SUBJ):
            if gen == "bp":
                betas, q = draw_params(N_PAIRS, BMEAN, QSD)
            else:
                ax, ay = rng.normal(0.85, 0.0125, N_PAIRS), rng.normal(0.85, 0.0125, N_PAIRS)
                qe = innov_corr(ax, ay, rng.choice(Q_POOL, N_PAIRS))
            for c in range(2):
                if gen == "bp":
                    X = simulate_run(betas, q, BETA_S[s] if c == 0 else None, ramp)
                else:
                    X = simulate_run_ar1(ax, ay, qe, DA[s] if c == 0 else 0.0, ramp)
                obs[s, c], pred[s, c], a[s, c] = analyse_run(X)
        d_o, d_p, d_a = did(obs), did(pred), did(a); d_r = d_o - d_p
        sl, lo, hi, r = ols(d_a, d_r)
        SL.append(sl); LO_.append(lo); HI_.append(hi); RRS.append(r); RATIO.append(d_r.mean() / d_a.mean()); RESD.append(d_r.mean()); STSD.append(d_o.mean()); AD.append(d_a.mean())
        csv.append(f"{cond},{rep + 1},{sl:.6f},{lo:.6f},{hi:.6f},{r:.6f},{RATIO[-1]:.6f},{d_r.mean():.6f},{d_o.mean():.6f},{d_a.mean():.6f}")
        if rep % 20 == 19 or rep == N_REP - 1:
            print(f"   {cond}: replicate {rep + 1}/{N_REP}: slope so far {np.mean(SL):+.3f} ± {np.std(SL):.3f} ({time.time() - t0:.0f}s)", flush=True)
    SL, LO_, HI_, RRS, RATIO, RESD, STSD, AD = map(np.array, (SL, LO_, HI_, RRS, RATIO, RESD, STSD, AD))
    ratio_cond = RESD.mean() / AD.mean()
    pct = lambda v: " / ".join(f"{x:+.3f}" for x in np.percentile(v, [2.5, 50, 97.5]))
    lines.append(f"| {cond} | {SL.mean():+.3f} ± {SL.std():.3f} | {pct(SL)} | {np.mean(SL <= DATA_SLOPE):.3f} | {RRS.mean():+.3f} ± {RRS.std():.3f} | {pct(RRS)} | {np.mean(RRS <= DATA_R):.3f} | "
                 f"{RATIO.mean():+.3f} ± {RATIO.std():.3f} | {pct(RATIO)} | {ratio_cond:+.3f} | {np.mean((LO_ <= ratio_cond) & (ratio_cond <= HI_)):.2f}; {np.mean((LO_ <= 0) & (0 <= HI_)):.2f} | {RESD.mean():+.4f} ± {RESD.std():.4f} | {STSD.mean():+.4f} ± {STSD.std():.4f} | {AD.mean():+.4f} ± {AD.std():.4f} |")
lines += ["", "One change for every subject, at W = 60: B17b's (i) residual DiD +0.0027 ± 0.0014 (calibration_filtered_tables.md), B17's (i) +0.0049 ± 0.0017 (calibration_tables.md); the data's residual DiD +0.0115 and r₁ DiD −0.01465 (whole-brain), −0.0155 (pair).", "",
          "## Reading under the rule of the pre-run entry", "",
          "The entry's predictions (the generators' slopes more negative than their ratios of means; the data's slope against the central 95 % of each condition's slopes; the ramps' residual DiDs against the steps') are read against the table "
          "in the outcome entry, and Results 4 and the Discussion state the per-subject scaling as the rule of the entry says."]
(OUT / "matched_slope.csv").write_text(f"# partB28_matched_slope.py; one row per condition × replicate; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "matched_slope_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
