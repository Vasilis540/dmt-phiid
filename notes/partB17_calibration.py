"""
partB17_calibration.py — B17: ground-truth calibration of the residual diagnostic (no external data).
Pre-run entry: manuscript/analysis_record.md, "Ground-truth calibration of the diagnostic (B17): pre-run entry,
20 Sep 2026" (specification, predictions and rule as in notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5).

Simulation: 14 "subjects" × 2 "runs" (DMT, placebo) × 840 samples of N_PAIRS = 300 independent pairs. Per pair the
coupled VAR(1)  x_{t+1} = a_x x_t + c y_t + ε_t,  y_{t+1} = a_y y_t + c x_t + η_t  with unit-variance innovations of
correlation q_ε, solved in closed form (c = 0 at baseline) so that the lag-0 correlation of (x, y) equals the drawn q
at baseline. a_x, a_y ~ N(0.85, 0.0125) independently (regional heterogeneity; the window-level scatter of a arises
from sampling); q drawn with replacement from the data's window-level pair q on ts_gsr (the 52,440 values of
pre_w1to4_q in notes/review_results/partB/scope_map_overlay_points.npz); c = 0 at baseline; burn-in 200 samples.
The "post-injection" change is applied from sample 300 (window 6) of the DMT run only; the placebo run is
stationary. Conditions: (i) Δa = −0.015, Δc = 0; (ii) Δa = 0, Δc ∈ {+0.01, +0.02, +0.03, −0.02}; (iii) Δa = −0.015,
Δc = +0.02; (iv) a_x − a_y = 0.03 fixed (a_x = a + 0.015, a_y = a − 0.015, a ~ N(0.85, 0.0125)), Δa = −0.015, Δc = 0.
Pipeline, the actual estimator: rev_phiid_fast.PairPhiID on the 300 pairs of each W = 60 window (14 windows) and on
the whole run with atoms_bins for the 28 bins of 30 samples (the global fit); observed sts; the diagnostic's
prediction from the measured (a_x, a_y, q) of each window (at the global fit both the run-level prediction, constant
across bins, and a period-level one from the pre and the post samples fitted separately); the residual;
δ_sym and δ_anti per window (as partB15 defines them). Per replicate: the DiD (windows 6–14 minus 1–4; bins 11–28
minus 1–8; DMT minus placebo) of observed, predicted and residual sts, its exact sign-flip p over the 14 subjects and
its subject-bootstrap 95 % CI (1,000 draws), and the DiDs of δ_sym and δ_anti. N_REP = 50 replicate datasets per
condition; one generator seeded 20261120, conditions in the order listed.
Outputs (notes/review_results/partB/): calibration_tables.md, calibration.csv (one row per condition × estimator ×
replicate), calibration_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB17_calibration.py   (minutes)
"""
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
S = ATOMS.index("sts")
SEED = 20261120
N_PAIRS, N_SUBJ, T, BURN, W, N_REP, N_BOOT = 300, 14, 840, 200, 60, 50, 1000
CHANGE_AT = 300
PRE, POST = np.arange(0, 4), np.arange(5, 14)
PRE_B, POST_B = np.arange(0, 8), np.arange(10, 28)
SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))
CONDITIONS = [("(i) Δa = −0.015, Δc = 0", -0.015, 0.0, 0.0), ("(ii) Δc = +0.01", 0.0, 0.01, 0.0), ("(ii) Δc = +0.02", 0.0, 0.02, 0.0),
              ("(ii) Δc = +0.03", 0.0, 0.03, 0.0), ("(ii) Δc = −0.02", 0.0, -0.02, 0.0), ("(iii) Δa = −0.015, Δc = +0.02", -0.015, 0.02, 0.0),
              ("(iv) a_x − a_y = 0.03, Δa = −0.015", -0.015, 0.0, 0.03)]
t0 = time.time()
rng = np.random.default_rng(SEED)
Q_POOL = np.load(OUT / "scope_map_overlay_points.npz")["pre_w1to4_q"]
Q_POOL = Q_POOL[np.isfinite(Q_POOL)]


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def boot_ci(v):
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def innov_corr(ax, ay, q_target):
    """Innovation correlation q_ε giving lag-0 correlation q_target for the diagonal (c = 0) pair, in closed form:
    cov(x, y) = q_ε / (1 − a_x a_y), var(x) = 1 / (1 − a_x²), so q = q_ε √((1 − a_x²)(1 − a_y²)) / (1 − a_x a_y). Clipped to ±0.999."""
    return np.clip(q_target * (1 - ax * ay) / np.sqrt((1 - ax ** 2) * (1 - ay ** 2)), -0.999, 0.999)


def simulate_run(ax, ay, qe, da, dc, change):
    """One run of N_PAIRS independent pairs; parameters change at CHANGE_AT if change. Returns X (2 N_PAIRS, T): rows (2k, 2k+1) are pair k."""
    n = ax.size
    E1 = rng.standard_normal((n, T + BURN)); E2 = rng.standard_normal((n, T + BURN))
    E2 = qe[:, None] * E1 + np.sqrt(1 - qe[:, None] ** 2) * E2
    x = np.zeros((n, T + BURN)); y = np.zeros((n, T + BURN))
    a_x, a_y, c = ax.copy(), ay.copy(), np.zeros(n)
    for t in range(1, T + BURN):
        if change and t == BURN + CHANGE_AT:
            a_x, a_y, c = ax + da, ay + da, np.full(n, dc)
        x[:, t] = a_x * x[:, t - 1] + c * y[:, t - 1] + E1[:, t]
        y[:, t] = a_y * y[:, t - 1] + c * x[:, t - 1] + E2[:, t]
    X = np.empty((2 * n, T)); X[0::2] = x[:, BURN:]; X[1::2] = y[:, BURN:]
    return X


PAIRS = [(2 * k, 2 * k + 1) for k in range(N_PAIRS)]


def deviations(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    d_xy = C[:, 0, 3] - ay * q; d_yx = C[:, 1, 2] - ax * q
    return ax, ay, q, 0.5 * (d_xy + d_yx), 0.5 * (d_xy - d_yx)


def analyse_run(X):
    """Window (14,) and bin (28,) whole-pair means of observed sts, predicted sts, δ_sym, δ_anti."""
    obs_w = np.empty(14); pred_w = np.empty(14); sym_w = np.empty(14); anti_w = np.empty(14)
    for w in range(14):
        pp = PairPhiID(X[:, w * W:(w + 1) * W], pairs=PAIRS)
        ax, ay, q, sym, anti = deviations(pp.C)
        obs_w[w] = pp.atoms_mean()[:, S].mean(); pred_w[w] = atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean()
        sym_w[w] = sym.mean(); anti_w[w] = np.sqrt(np.mean(anti ** 2))
    pp = PairPhiID(X, pairs=PAIRS)
    ax, ay, q, sym, anti = deviations(pp.C)
    obs_b = np.nanmean(pp.atoms_bins(np.arange(pp.n) // 30, 28)[..., S], axis=1)
    pred_b = np.full(28, atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean())          # the pipeline's run-level prediction, constant across bins
    pred_bp = np.empty(28)                                                            # period-level prediction: (a_x, a_y, q) measured on the pre and on the post samples
    for lo, hi, sl in ((0, CHANGE_AT, slice(0, CHANGE_AT // 30)), (CHANGE_AT, T, slice(CHANGE_AT // 30, 28))):
        pq = PairPhiID(X[:, lo:hi], pairs=PAIRS)
        axp, ayp, qp, _, _ = deviations(pq.C)
        pred_bp[sl] = atoms_from_corr(ar1_corr(axp, ayp, qp))[:, S].mean()
    return obs_w, pred_w, sym_w, anti_w, obs_b, pred_b, pred_bp


def cell(v):
    return '—' if np.isnan(v).all() else f"{np.nanmean(v):+.5f} ± {np.nanstd(v):.5f}"


def did(x, pre, post):
    ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
    return ch[:, 0] - ch[:, 1]


lines = ["# Ground-truth calibration of the residual diagnostic (partB17_calibration.py)", f"git={SHA}", "",
         f"N_PAIRS = {N_PAIRS} independent VAR(1) pairs per subject, {N_SUBJ} subjects × 2 runs × {T} samples, burn-in {BURN}; a_x, a_y ~ N(0.85, 0.0125); q from the data's window-level q "
         f"(scope_map_overlay_points.npz, pre_w1to4_q, {Q_POOL.size} values); change at sample {CHANGE_AT} of the DMT run only; W = {W}; bins of 30; {N_REP} replicates per condition; "
         f"bootstrap {N_BOOT} draws; sign-flip exact over 2^{N_SUBJ}; seed {SEED}. DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo, mean over subjects. "
         "At the global fit two predictions are tabulated: the pipeline's run-level prediction (constant across a run's bins, so its DiD is zero and the residual DiD equals the observed DiD, as partB4 records for the data) "
         f"and a period-level prediction from (a_x, a_y, q) measured on the pre (samples 0–{CHANGE_AT - 1}) and post (samples {CHANGE_AT}–{T - 1}) samples of each run separately, which is the reading the recorded prediction (i) refers to.", "",
         "| condition | estimator | sts level (pre) | sts DiD | predicted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |", "|---|---|---|---|---|---|---|---|---|"]
csv = ["condition,estimator,replicate,sts_level_pre,sts_did,pred_did,res_did,res_p,res_ci_lo,res_ci_hi,sym_did,anti_did"]
for name, da, dc, asym in CONDITIONS:
    acc = {est: {k: [] for k in ("lvl", "sts", "pred", "res", "p", "sym", "anti")} for est in ("W60", "global (run-level prediction)", "global (period-level prediction)")}
    for rep in range(N_REP):
        obs_w = np.empty((N_SUBJ, 2, 14)); pred_w = np.empty((N_SUBJ, 2, 14)); sym_w = np.empty((N_SUBJ, 2, 14)); anti_w = np.empty((N_SUBJ, 2, 14))
        obs_b = np.empty((N_SUBJ, 2, 28)); pred_b = np.empty((N_SUBJ, 2, 28)); pred_bp = np.empty((N_SUBJ, 2, 28))
        for s in range(N_SUBJ):
            a = rng.normal(0.85, 0.0125, N_PAIRS)
            if asym:
                ax, ay = a + asym / 2, a - asym / 2
            else:
                ax, ay = rng.normal(0.85, 0.0125, N_PAIRS), rng.normal(0.85, 0.0125, N_PAIRS)
            qt = rng.choice(Q_POOL, N_PAIRS)
            qe = innov_corr(ax, ay, qt)
            for c in range(2):
                X = simulate_run(ax, ay, qe, da, dc, change=(c == 0))
                obs_w[s, c], pred_w[s, c], sym_w[s, c], anti_w[s, c], obs_b[s, c], pred_b[s, c], pred_bp[s, c] = analyse_run(X)
        for est, o, p, sy, an, pre, post in (("W60", obs_w, pred_w, sym_w, anti_w, PRE, POST), ("global (run-level prediction)", obs_b, pred_b, None, None, PRE_B, POST_B),
                                             ("global (period-level prediction)", obs_b, pred_bp, None, None, PRE_B, POST_B)):
            d_o, d_p = did(o, pre, post), did(p, pre, post); d_r = d_o - d_p
            pr = signflip_p(d_r); lo, hi = boot_ci(d_r)
            d_s = did(sy, pre, post).mean() if sy is not None else np.nan; d_a = did(an, pre, post).mean() if an is not None else np.nan
            lvl = o[:, 0, pre].mean()
            for k, v in (("lvl", lvl), ("sts", d_o.mean()), ("pred", d_p.mean()), ("res", d_r.mean()), ("p", pr), ("sym", d_s), ("anti", d_a)):
                acc[est][k].append(v)
            csv.append(f"{name},{est},{rep + 1},{lvl:.6f},{d_o.mean():.6f},{d_p.mean():.6f},{d_r.mean():.6f},{pr:.4f},{lo:.6f},{hi:.6f},{d_s:.6f},{d_a:.6f}")
        if rep % 10 == 9:
            print(f"   {name}: replicate {rep + 1}/{N_REP} ({time.time() - t0:.0f}s)", flush=True)
    for est in ("W60", "global (run-level prediction)", "global (period-level prediction)"):
        A = {k: np.array(v) for k, v in acc[est].items()}
        lines.append(f"| {name} | {est} | {A['lvl'].mean():.4f} | {A['sts'].mean():+.4f} ± {A['sts'].std():.4f} | {A['pred'].mean():+.4f} ± {A['pred'].std():.4f} | {A['res'].mean():+.4f} ± {A['res'].std():.4f} | "
                     f"{A['p'].mean():.3f}; {np.mean(A['p'] < 0.05):.2f} | {cell(A['sym'])} | {cell(A['anti'])} |")
lines += ["", "Predictions recorded (plan §5, B17): (i) residual ≈ its finite-sample expectation (+0.004 to +0.008 at W = 60; near zero at the global fit); (ii) residual ≈ −1.77 Δc at the global fit (first order), smaller in magnitude at W = 60 through the bias, δ_sym ≈ 0.94 Δc; (iii) additive to first order; (iv) sts level lowered by the asymmetry with the residual near its expectation. "
          "Rule: this is the calibration the diagnostic lacked; its table is quoted wherever a residual is interpreted, and the finite-sample null of Results 4 is superseded by it where they overlap. Each condition's row is read against these in the outcome entry.",
          "Note: the diagnostic's prediction uses the measured (a_x, a_y, q); a Δc changes the measured lag-0 q and the lag-1 autocorrelations of the coupled pair as well as the cross-lag entries, so the residual under (ii) is the estimator's response to the part of the change the AR(1) substitution cannot follow."]
(OUT / "calibration.csv").write_text(f"# partB17_calibration.py; one row per condition × estimator × replicate; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "calibration_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
