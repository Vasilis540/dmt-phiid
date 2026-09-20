"""
partB15_directed_crosslag.py — B15: the directed (antisymmetric) cross-lag component.
Pre-run entry: manuscript/analysis_record.md, "The directed cross-lag component (B15): pre-run entry, 20 Sep 2026"
(specification, prediction and rule as in notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5).

Per pair: d_xy = corr(x_t, y_{t+1}) − a_y q, d_yx = corr(y_t, x_{t+1}) − a_x q, with a_x = C[0, 2], a_y = C[1, 3] and
q = mean of C[0, 1] and C[2, 3] as partB4_diagnostic.py and partB10 take them; δ_sym = (d_xy + d_yx)/2 (partB10's d),
δ_anti = (d_xy − d_yx)/2.
  Run level (whole-run matrices, all finite TRs): RMS of δ_anti over the 6,555 pairs per subject and run; the
  closed-form response of sts per pair to the antisymmetric deviation alone (the AR(1) matrix with C[0, 3] = a_y q +
  δ_anti and C[1, 2] = a_x q − δ_anti, symmetric entries alike; sts minus the AR(1) sts), to the symmetric deviation
  alone (both entries + δ_sym), and to both; averaged over pairs — beside the run-level residual of the diagnostic
  (observed run-level sts − AR(1) prediction) recomputed here.
  W = 60: the RMS of δ_anti per window, averaged over each run's windows; its DiD (windows 6–14 minus 1–4, DMT
  minus placebo) with subject bootstrap (10,000 draws, seed 20261120) and exact sign-flip p; the same for δ_sym's
  sign(q)-weighted mean (partB10's statistic) for reference.
  Finite-sample null: review_v2_residual_null.py's generator, filter fit and window statistics, reproduced from its
  functions, at the DMT pre operating point (a = 0.8632, |q| = 0.2842; W = 60, 3,000 pairs, T = 3,000), with two
  lead–lag-asymmetric configurations: (1) y_t = w x_{t−1} + √(1 − w²) n_t with n an independent filtered noise, w
  solved so that corr(x_t, y_t) = the target q; (2) the symmetric VAR(1) pair at the operating point with c_xy = +c,
  c_yx = −c, c ∈ {0.02, 0.04, 0.06}, innovation correlation solved so that the lag-0 correlation is the target. The
  null's own symmetric configuration is reproduced first (its residual should be close to the committed log's DMT pre
  value, the generator being at a different point of its stream than in that script's main block).
Free choices: variants ts_gsr and ts_demean; region 20 excluded; non-finite TRs dropped as scripts/01 drops them;
the null's grid, filter and clip exactly as review_v2_residual_null.py. Seed 20261120.
Outputs (notes/review_results/partB/): directed_crosslag_tables.md, directed_crosslag.csv (one row per subject and
run), directed_crosslag_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB15_directed_crosslag.py   (partB10's time plus minutes)
"""
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
import review_v2_residual_null as NULL
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
S = ATOMS.index("sts")
SEED = 20261120
N_BOOT = 10000
PRE, POST = np.arange(0, 4), np.arange(5, 14)
SIGNS = np.array(list(product((-1, 1), repeat=14)))
t0 = time.time()
rng = np.random.default_rng(SEED)


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def boot_ci(v, r):
    v = np.asarray(v, float)
    draws = v[r.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def deviations(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]
    q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    d_xy = C[:, 0, 3] - ay * q
    d_yx = C[:, 1, 2] - ax * q
    return ax, ay, q, 0.5 * (d_xy + d_yx), 0.5 * (d_xy - d_yx)


def with_deviation(ax, ay, q, d_xy, d_yx):
    """AR(1) matrices with the cross-lag entries corr(x_t, y_{t+1}) = a_y q + d_xy and corr(y_t, x_{t+1}) = a_x q + d_yx."""
    C = ar1_corr(ax, ay, q)
    C[:, 0, 3] = C[:, 3, 0] = ay * q + d_xy
    C[:, 1, 2] = C[:, 2, 1] = ax * q + d_yx
    return C


def response(ax, ay, q, sym, anti):
    """sts responses (per pair): to δ_anti alone, to δ_sym alone, to both; and the AR(1) sts."""
    base = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
    r_anti = atoms_from_corr(with_deviation(ax, ay, q, anti, -anti))[:, S] - base
    r_sym = atoms_from_corr(with_deviation(ax, ay, q, sym, sym))[:, S] - base
    r_both = atoms_from_corr(with_deviation(ax, ay, q, sym + anti, sym - anti))[:, S] - base
    return base, r_anti, r_sym, r_both


lines = ["# The directed (antisymmetric) cross-lag component (partB15_directed_crosslag.py)", f"git={SHA}", "",
         "Per pair d_xy = corr(x_t, y_{t+1}) − a_y q and d_yx = corr(y_t, x_{t+1}) − a_x q; δ_sym = (d_xy + d_yx)/2 (partB10's d), δ_anti = (d_xy − d_yx)/2. "
         f"Run level from the whole-run 4 × 4 matrices; W = 60 from each window's own. Seed {SEED}; subject bootstrap {N_BOOT} draws; exact sign-flip p over 2^14 assignments. Region 20 excluded.", ""]
csv = ["variant,subject,run,rms_anti_run,rms_sym_run,resp_anti_run,resp_sym_run,resp_both_run,residual_run,mean_a,mean_abs_q,rms_anti_w60_mean,signq_sym_w60_mean"]
ts = sio.loadmat(MAT)
for var in ("ts_gsr", "ts_demean"):
    rms_anti = np.full((14, 2), np.nan); rms_sym = np.full((14, 2), np.nan)
    resp = np.full((14, 2, 3), np.nan); resid = np.full((14, 2), np.nan); m_a = np.full((14, 2), np.nan); m_q = np.full((14, 2), np.nan)
    rms_w = np.full((14, 2, 14), np.nan); sq_w = np.full((14, 2, 14), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            pp = PairPhiID(X[:, kept])
            ax, ay, q, sym, anti = deviations(pp.C)
            base, r_anti, r_sym, r_both = response(ax, ay, q, sym, anti)
            rms_anti[s, c] = np.sqrt(np.mean(anti ** 2)); rms_sym[s, c] = np.sqrt(np.mean(sym ** 2))
            resp[s, c] = [r_anti.mean(), r_sym.mean(), r_both.mean()]
            resid[s, c] = pp.atoms_mean()[:, S].mean() - base.mean()
            m_a[s, c] = 0.5 * (ax + ay).mean(); m_q[s, c] = np.abs(q).mean()
            for w in range(14):
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= 5:
                    continue
                pw = PairPhiID(X[:, in_w])
                axw, ayw, qw, symw, antiw = deviations(pw.C)
                rms_w[s, c, w] = np.sqrt(np.mean(antiw ** 2)); sq_w[s, c, w] = (np.sign(qw) * symw).mean()
        print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    for s in range(14):
        for c in range(2):
            csv.append(f"{var},{s + 1},{'DMT' if c == 0 else 'PCB'},{rms_anti[s, c]:.6f},{rms_sym[s, c]:.6f},{resp[s, c, 0]:.6f},{resp[s, c, 1]:.6f},{resp[s, c, 2]:.6f},{resid[s, c]:.6f},{m_a[s, c]:.5f},{m_q[s, c]:.5f},{np.nanmean(rms_w[s, c]):.6f},{np.nanmean(sq_w[s, c]):.6f}")
    per_subj = rms_anti.mean(1)
    ci_dir = boot_ci(resp[:, :, 0].mean(1), np.random.default_rng(SEED))
    lines += [f"## {var}, run level (whole-run matrices; 28 runs)", "",
              f"RMS of δ_anti over pairs: mean over runs {rms_anti.mean():.5f} (DMT {rms_anti[:, 0].mean():.5f}, placebo {rms_anti[:, 1].mean():.5f}); per subject (mean of the two runs) min {per_subj.min():.5f}, max {per_subj.max():.5f}. RMS of δ_sym: {rms_sym.mean():.5f}. For reference, 1/√(kept TRs) ≈ {1 / np.sqrt(839):.4f}.",
              f"Mean pair a {m_a.mean():.4f}, mean pair |q| {m_q.mean():.4f}.",
              f"Closed-form response of the pair-mean sts (mean over runs): to δ_anti alone {resp[:, :, 0].mean():+.5f} [{ci_dir[0]:+.5f}, {ci_dir[1]:+.5f}] (subject bootstrap of the per-subject mean of the two runs) — the directed share; "
              f"to δ_sym alone {resp[:, :, 1].mean():+.5f} — the symmetric share; to both {resp[:, :, 2].mean():+.5f}; run-level residual of the diagnostic (observed − AR(1) prediction) {resid.mean():+.5f} (DMT {resid[:, 0].mean():+.5f}, placebo {resid[:, 1].mean():+.5f}); "
              f"the responses account for {100 * resp[:, :, 2].mean() / resid.mean():.0f} % of the residual (directed alone {100 * resp[:, :, 0].mean() / resid.mean():.0f} %, symmetric alone {100 * resp[:, :, 1].mean() / resid.mean():.0f} %).",
              f"Per-subject directed response (mean of the two runs): {np.array2string(resp[:, :, 0].mean(1), precision=5, floatmode='fixed', max_line_width=250)}; negative in {int((resp[:, :, 0].mean(1) < 0).sum())}/14; sign-flip p = {signflip_p(resp[:, :, 0].mean(1)):.4f}.",
              f"DMT − placebo of the run-level RMS of δ_anti: {(rms_anti[:, 0] - rms_anti[:, 1]).mean():+.5f}, sign-flip p = {signflip_p(rms_anti[:, 0] - rms_anti[:, 1]):.4f}; of the directed response: {(resp[:, 0, 0] - resp[:, 1, 0]).mean():+.5f}, p = {signflip_p(resp[:, 0, 0] - resp[:, 1, 0]):.4f}.", ""]
    d_rms = ((rms_w[:, 0, POST].mean(1) - rms_w[:, 0, PRE].mean(1)) - (rms_w[:, 1, POST].mean(1) - rms_w[:, 1, PRE].mean(1)))
    d_sq = ((sq_w[:, 0, POST].mean(1) - sq_w[:, 0, PRE].mean(1)) - (sq_w[:, 1, POST].mean(1) - sq_w[:, 1, PRE].mean(1)))
    lo, hi = boot_ci(d_rms, np.random.default_rng(SEED + 1)); lo2, hi2 = boot_ci(d_sq, np.random.default_rng(SEED + 2))
    lines += [f"## {var}, W = 60 (each window's own matrices)", "",
              f"RMS of δ_anti per window, mean over runs and windows {np.nanmean(rms_w):.5f} (DMT pre {np.nanmean(rms_w[:, 0, PRE]):.5f}, DMT post {np.nanmean(rms_w[:, 0, POST]):.5f}, placebo pre {np.nanmean(rms_w[:, 1, PRE]):.5f}, placebo post {np.nanmean(rms_w[:, 1, POST]):.5f}); for reference 1/√60 = {1 / np.sqrt(60):.4f}.",
              f"DiD of the RMS of δ_anti (windows 6–14 minus 1–4, DMT minus placebo): {d_rms.mean():+.5f} [{lo:+.5f}, {hi:+.5f}], sign-flip p = {signflip_p(d_rms):.4f}, negative in {int((d_rms < 0).sum())}/14.",
              f"DiD of the sign(q)-weighted mean of δ_sym (partB10's W = 60 statistic, for reference): {d_sq.mean():+.5f} [{lo2:+.5f}, {hi2:+.5f}], p = {signflip_p(d_sq):.4f}.", ""]
(OUT / "directed_crosslag.csv").write_text(f"# partB15_directed_crosslag.py; run level and W = 60; git={SHA}\n" + "\n".join(csv) + "\n")

# ---------------------------------------------------------------- the finite-sample null with lead–lag asymmetry
lines += ["## The finite-sample null with within-pair lead–lag asymmetry (DMT pre operating point, W = 60, 3,000 pairs, T = 3,000)", ""]
NULL.rng = np.random.default_rng(SEED)
fits = {k: NULL.fit_filter(t) for k, t in NULL.TARGET_ACF.items()}
lo_f, hi_f = fits["placebo"][2], fits["placebo"][3]
target_a, target_q = NULL.CELLS["DMT pre"][0], NULL.CELLS["DMT pre"][1]
n_pairs, T, W = 3000, 3000, 60


def stats_sym(bmean, qsd, r):
    betas = np.clip(r.normal(bmean, 0.5 * bmean, n_pairs), 5, None); q = np.clip(r.normal(0, qsd, n_pairs), -0.95, 0.95)
    X, Y = NULL.gen(n_pairs, T, betas, lo_f, hi_f, q)
    return X, Y, betas, q


# (0) the null's own symmetric configuration, solved as review_v2_residual_null.cell does (same call order)
NULL.rng = np.random.default_rng(SEED)
bmean = brentq(lambda b: NULL.residual(NULL.window_corr(*NULL.gen(n_pairs, T, np.clip(NULL.rng.normal(b, 0.5 * b, n_pairs), 5, None), lo_f, hi_f, np.clip(NULL.rng.normal(0, 0.27, n_pairs), -0.95, 0.95)), W))[2].mean() - target_a, 20, 800, xtol=3)
qsd = brentq(lambda s: NULL.residual(NULL.window_corr(*NULL.gen(n_pairs, T, np.clip(NULL.rng.normal(bmean, 0.5 * bmean, n_pairs), 5, None), lo_f, hi_f, np.clip(NULL.rng.normal(0, s, n_pairs), -0.95, 0.95)), W))[3].mean() - target_q, 0.05, 0.9, xtol=0.005)


def report(name, X, Y):
    C = NULL.window_corr(X, Y, W)
    obs, pred, a, aq = NULL.residual(C)
    ax, ay, q, sym, anti = deviations(C)
    _, r_anti, r_sym, r_both = response(ax, ay, q, sym, anti)
    lines.append(f"{name}: window a {a.mean():.4f}, |q| {aq.mean():.4f}; residual {np.mean(obs - pred):+.5f} ({100 * np.mean(obs - pred) / obs.mean():+.2f} %); RMS δ_anti {np.sqrt(np.mean(anti ** 2)):.5f}, RMS δ_sym {np.sqrt(np.mean(sym ** 2)):.5f}; "
                 f"closed-form response to δ_anti {r_anti.mean():+.5f}, to δ_sym {r_sym.mean():+.5f}, to both {r_both.mean():+.5f}.")
    return np.mean(obs - pred)


X, Y, betas, q = stats_sym(bmean, qsd, NULL.rng)
res0 = report("(0) symmetric filter null, as review_v2_residual_null.py (solved bmean %.0f, qsd %.3f)" % (bmean, qsd), X, Y)

# (1) y = x delayed by one sample, mixed with independent filtered noise: y_t = w x_{t−1} + sqrt(1 − w²) n_t
r1 = np.random.default_rng(SEED + 10)
betas1 = np.clip(r1.normal(bmean, 0.5 * bmean, n_pairs), 5, None); q1 = np.clip(r1.normal(0, qsd, n_pairs), -0.95, 0.95)
X1, N1 = NULL.gen(n_pairs, T + 1, betas1, lo_f, hi_f, np.zeros(n_pairs))     # independent x and n with the same filter
Xd = X1[:, 1:]; Xlag = X1[:, :-1]; N1 = N1[:, 1:]
sx = Xd.std(1, keepdims=True); Xd = Xd / sx; Xlag = Xlag / sx; N1 = N1 / N1.std(1, keepdims=True)
# corr(x_t, y_t) = w corr(x_t, x_{t−1}) (n independent), so w = q / a_lag1 of the filtered x
a1 = (Xd * Xlag).mean(1)
wmix = np.clip(q1 / a1, -0.99, 0.99)
Y1 = wmix[:, None] * Xlag + np.sqrt(1 - wmix[:, None] ** 2) * N1
res1 = report("(1) y = x delayed by one sample mixed with independent noise at the pair's q (w = q / r₁ of x, clipped to ±0.99)", Xd, Y1)

# (2) symmetric VAR(1) with c_xy = +c, c_yx = −c at the population operating point (a = 0.8632; q ~ N(0, qsd) with qsd from the filter
#     null's solve, clipped to the lag-0 range reachable at this c). Its window-level a and |q| are reported as measured: an AR(1) pair's
#     window estimates are biased further from the population values than the band-passed filter null's (larger sampling variance of the
#     lag-0 and lag-1 correlations at the same a), so this configuration cannot be matched to both window-level targets at once;
#     configuration (1) is the one matched to them.
def var1_pair(a0, cc, qsd_v, seed):
    r = np.random.default_rng(seed)
    A = np.array([[a0, cc], [-cc, a0]])

    def lag0_corr(qe):
        G0 = solve_discrete_lyapunov(A, np.array([[1.0, qe], [qe, 1.0]]))
        return G0[0, 1] / np.sqrt(G0[0, 0] * G0[1, 1])
    lo_q, hi_q = lag0_corr(-0.999), lag0_corr(0.999)
    qs = np.clip(r.normal(0, qsd_v, n_pairs), lo_q + 1e-6, hi_q - 1e-6)
    qe = np.array([brentq(lambda e, qt=qt: lag0_corr(e) - qt, -0.999, 0.999) for qt in qs])
    burn = 300
    E1 = r.standard_normal((n_pairs, T + burn)); E2 = r.standard_normal((n_pairs, T + burn))
    E2 = qe[:, None] * E1 + np.sqrt(1 - qe[:, None] ** 2) * E2
    Xv = np.zeros((n_pairs, T + burn)); Yv = np.zeros((n_pairs, T + burn))
    for t in range(1, T + burn):
        Xv[:, t] = a0 * Xv[:, t - 1] + cc * Yv[:, t - 1] + E1[:, t]
        Yv[:, t] = a0 * Yv[:, t - 1] - cc * Xv[:, t - 1] + E2[:, t]
    return Xv[:, burn:], Yv[:, burn:], (lo_q, hi_q)


res2 = {}
for k_c, cc in enumerate((0.02, 0.04, 0.06)):
    Xv, Yv, (lo_q, hi_q) = var1_pair(target_a, cc, qsd, SEED + 21 + k_c)
    res2[cc] = report(f"(2) symmetric VAR(1), population a = {target_a}, c_xy = +{cc}, c_yx = −{cc}, q ~ N(0, {qsd:.3f}) clipped to the reachable lag-0 range {lo_q:+.3f} to {hi_q:+.3f} (window a and |q| as measured, see the note in the script)", Xv, Yv)
lines += ["", f"Null residual levels: symmetric {res0:+.5f}; delayed-copy {res1:+.5f}; antisymmetric VAR(1) " + ", ".join(f"c = {c}: {v:+.5f}" for c, v in res2.items()) +
          ". These are W = 60 window-level residuals; the data's W = 60 residual is −0.0489 on ts_gsr (diag_tables.md) and its run-level residual −0.0137 (residual_source.log; recomputed in this script's run-level section above). Reported with their sizes; no branch labels (rule of the pre-run entry).", ""]
(OUT / "directed_crosslag_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
