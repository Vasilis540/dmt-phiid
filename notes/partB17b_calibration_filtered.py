"""
partB17b_calibration_filtered.py — B17b: B17's calibration of the residual diagnostic repeated on the band-passed
generator of review_v2_residual_null.py (no external data).
Pre-run entry: manuscript/analysis_record.md, "Calibration of the diagnostic on the band-passed generator (B17b):
pre-run entry, 21 Sep 2026" (specification, predictions and rule as commissioned on 21 Sep 2026, round 14, Stage A).

Generator (review_v2_residual_null.py, imported): per pair two white noises e₁, e₂ of T = 840 samples with correlation
q, each filtered by multiplying its rfft by √(psd_weights(f, β, lo, hi)) — the smooth 0.01–0.08 Hz band-pass with
0.004 Hz cosine edges and the low-frequency tilt exp(−β f²), at the lo and hi that fit_filter returns for the placebo
target ACF — circularly over the run's 840 samples, exactly as that script's gen filters over its 3,000 (a free
choice). Per pair β ~ N(β̄, 0.5 β̄) clipped below at 5 and q ~ N(0, σ_q) clipped to ±0.95, as there.
Solves, each done once by brentq on calibration draws of the null's size (3,000 pairs × 3,000 samples, W = 60 windows;
the window-level pair a and |q| by that script's window_corr and residual, which are partB4's definitions) and then
held fixed for every replicate: β̄ so that the window-level mean a is 0.8632, then σ_q so that the mean |q| is 0.2842
(the DMT-pre operating point of residual_source.log); β̄_post so that the mean a is 0.8482 (Δa = −0.0150 at window
level, the data's Δr₁); δ so that the window-level mean a_x − a_y is 0.03 when x is filtered at β + δ and y at β − δ.
Structure as partB17_calibration.py: N_SUBJ = 14 subjects × 2 runs × 840 samples of N_PAIRS = 300 pairs; the
placebo run at the pre parameters; the DMT run's white noises filtered twice — at the pre parameters and at the post
parameters (each pair's β scaled by β̄_post/β̄, which keeps N(β̄, 0.5 β̄) → N(β̄_post, 0.5 β̄_post)) — and spliced at
CHANGE_AT = 300 (samples 0–299 from the pre filtering, 300–839 from the post; a window and a bin boundary).
Conditions: (i) the post filtering; (ii) Δc ∈ {+0.01, +0.02, +0.03, −0.02}: on the post samples t ≥ 300,
x_t ← x_t + c y_{t−1} and y_t ← y_t + c x_{t−1} with the unmodified series on the right-hand sides (t = 300 uses the
last pre sample), each post segment then rescaled to the standard deviation it had before the coupling was added (the
re-standardisation; a free choice); (iii) (i)'s post filtering and (ii)'s coupling at Δc = +0.02; (iv) x at β + δ and
y at β − δ throughout, with (i)'s post filtering (β scaled, the same δ). The (ii) rows are read by their δ_sym DiD,
not by c (a different coupling from B17's VAR(1)).
Pipeline, statistics and table exactly as partB17 (analyse_run, did, signflip_p and boot_ci copied verbatim): the
closed-form estimator PairPhiID on the 300 pairs of each W = 60 window and on the whole run (atoms_bins over 28 bins
of 30 samples); the diagnostic's prediction from the measured (a_x, a_y, q) per window, and at the global fit the
run-level and the period-level prediction; per replicate the DiD (windows 6–14 minus 1–4; bins 11–28 minus 1–8; DMT
minus placebo) of observed, predicted and residual sts, the residual's exact sign-flip p and subject-bootstrap CI
(1,000 draws), and the δ_sym and RMS δ_anti DiDs. N_REP = 50 replicates per condition (--n-rep N for a smoke test);
one generator seeded 20261120: the calibration solves first, then the conditions in B17's order.
Population reference for B17's AR(1) conditions (i) and (iv): 20,000 draws of B17's distributions (a_x, a_y ~
N(0.85, 0.0125) independently; for (iv) a_x = a + 0.015, a_y = a − 0.015 with a ~ N(0.85, 0.0125); q from
scope_map_overlay_points.npz, pre_w1to4_q), the closed-form sts at (a_x, a_y, q) pre and at (a_x − 0.015, a_y − 0.015)
post with the innovation correlation held as B17 holds it (the lag-0 q recomputed from it), tabulated beside B17's
W = 60 and global-fit levels and changes read from the committed calibration.csv.
Outputs (notes/review_results/partB/): calibration_filtered_tables.md, calibration_filtered.csv (one row per
condition × estimator × replicate, B17's columns), calibration_filtered_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB17b_calibration_filtered.py   (about an hour; B17 took
3,382 s on V.S.'s machine)
"""
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from review_v2_residual_null import psd_weights, fit_filter, window_corr, residual, TARGET_ACF
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
S = ATOMS.index("sts")
SEED = 20261120
TR = 2.0
N_PAIRS, N_SUBJ, T, W, N_BOOT = 300, 14, 840, 60, 1000
N_REP = int(sys.argv[sys.argv.index("--n-rep") + 1]) if "--n-rep" in sys.argv else 50
CHANGE_AT = 300
CAL_PAIRS, CAL_T = 3000, 3000
TARGET_A, TARGET_Q, TARGET_A_POST, TARGET_ASYM = 0.8632, 0.2842, 0.8482, 0.03
PRE, POST = np.arange(0, 4), np.arange(5, 14)
PRE_B, POST_B = np.arange(0, 8), np.arange(10, 28)
SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))
CONDITIONS = [("(i) Δa (post filter)", True, 0.0, False), ("(ii) Δc = +0.01", False, 0.01, False), ("(ii) Δc = +0.02", False, 0.02, False),
              ("(ii) Δc = +0.03", False, 0.03, False), ("(ii) Δc = −0.02", False, -0.02, False), ("(iii) Δa and Δc = +0.02", True, 0.02, False),
              ("(iv) a_x − a_y = 0.03 with Δa", True, 0.0, True)]
t0 = time.time()
rng = np.random.default_rng(SEED)
Q_POOL = np.load(OUT / "scope_map_overlay_points.npz")["pre_w1to4_q"]
Q_POOL = Q_POOL[np.isfinite(Q_POOL)]
PAIRS = [(2 * k, 2 * k + 1) for k in range(N_PAIRS)]


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def boot_ci(v):
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


# ---------------------------------------------------------------- the generator
FIT = fit_filter(TARGET_ACF["placebo"])
LO, HI = FIT[2], FIT[3]
print(f"   filter fitted to the placebo ACF: beta={FIT[1]:.0f} lo={LO:.4f} hi={HI:.3f}; lags 1-6 {np.round(FIT[4][1:], 3)}", flush=True)


def filtered(e1, e2, betas_x, betas_y, n):
    """Filter the two white noises (n_pairs, n) with per-pair tilts β_x (for x) and β_y (for y); circular, as gen."""
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


def cal_stats(bmean, qsd, delta=0.0):
    """Calibration draw of the null's size: window-level (mean a, mean |q|, mean a_x − a_y) at W = 60."""
    betas, q = draw_params(CAL_PAIRS, bmean, qsd)
    e1, e2 = draw_noise(CAL_PAIRS, CAL_T, q)
    X, Y = filtered(e1, e2, np.clip(betas + delta, 5, None), np.clip(betas - delta, 5, None), CAL_T)
    C = window_corr(X, Y, W)
    _, _, a, aq = residual(C)
    return a.mean(), aq.mean(), (C[:, 0, 2] - C[:, 1, 3]).mean()


print("   solving the generator's parameters on calibration draws (3,000 pairs × 3,000 samples) ...", flush=True)
BMEAN = brentq(lambda b: cal_stats(b, 0.27)[0] - TARGET_A, 20, 800, xtol=1)
QSD = brentq(lambda s: cal_stats(BMEAN, s)[1] - TARGET_Q, 0.05, 0.9, xtol=0.005)
BMEAN_POST = brentq(lambda b: cal_stats(b, QSD)[0] - TARGET_A_POST, 20, 800, xtol=1)
DELTA = brentq(lambda d: cal_stats(BMEAN, QSD, d)[2] - TARGET_ASYM, 0.0, 0.9 * BMEAN, xtol=1)
chk_pre = cal_stats(BMEAN, QSD); chk_post = cal_stats(BMEAN_POST, QSD); chk_asym = cal_stats(BMEAN, QSD, DELTA)
print(f"   solved: β̄ = {BMEAN:.1f}, σ_q = {QSD:.4f}, β̄_post = {BMEAN_POST:.1f}, δ = {DELTA:.1f}; check draws: pre a = {chk_pre[0]:.4f}, |q| = {chk_pre[1]:.4f}; "
      f"post a = {chk_post[0]:.4f}; asymmetry a_x − a_y = {chk_asym[2]:.4f} ({time.time() - t0:.0f}s)", flush=True)


def simulate_run(betas, q, change, dc, asym):
    """One run of N_PAIRS pairs; returns X (2 N_PAIRS, T): rows (2k, 2k+1) are pair k."""
    e1, e2 = draw_noise(N_PAIRS, T, q)
    d = DELTA if asym else 0.0
    x, y = filtered(e1, e2, np.clip(betas + d, 5, None), np.clip(betas - d, 5, None), T)
    if change:
        bp = betas * (BMEAN_POST / BMEAN)
        xp, yp = filtered(e1, e2, np.clip(bp + d, 5, None), np.clip(bp - d, 5, None), T)
        x = np.concatenate([x[:, :CHANGE_AT], xp[:, CHANGE_AT:]], 1); y = np.concatenate([y[:, :CHANGE_AT], yp[:, CHANGE_AT:]], 1)
    if dc:
        sx, sy = x[:, CHANGE_AT:].std(1, ddof=1), y[:, CHANGE_AT:].std(1, ddof=1)
        xn = x[:, CHANGE_AT:] + dc * y[:, CHANGE_AT - 1:-1]; yn = y[:, CHANGE_AT:] + dc * x[:, CHANGE_AT - 1:-1]
        x = np.concatenate([x[:, :CHANGE_AT], xn * (sx / xn.std(1, ddof=1))[:, None]], 1)
        y = np.concatenate([y[:, :CHANGE_AT], yn * (sy / yn.std(1, ddof=1))[:, None]], 1)
    X = np.empty((2 * N_PAIRS, T)); X[0::2] = x; X[1::2] = y
    return X


# ---------------------------------------------------------------- copied verbatim from partB17_calibration.py
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
# ---------------------------------------------------------------- end of the copied block


lines = ["# Calibration of the residual diagnostic on the band-passed generator (partB17b_calibration_filtered.py)", f"git={SHA}", "",
         f"Generator of review_v2_residual_null.py: smooth {LO:.4f}–{HI:.3f} Hz band-pass (0.004 Hz cosine edges) with tilt exp(−β f²) applied to two white noises of correlation q, circularly over the run's {T} samples; "
         f"per pair β ~ N(β̄, 0.5 β̄) (clipped below at 5), q ~ N(0, σ_q) (clipped to ±0.95). Solved once on calibration draws of {CAL_PAIRS} pairs × {CAL_T} samples (W = {W}): β̄ = {BMEAN:.1f} (window-level mean a {chk_pre[0]:.4f}, target {TARGET_A}), "
         f"σ_q = {QSD:.4f} (mean |q| {chk_pre[1]:.4f}, target {TARGET_Q}), β̄_post = {BMEAN_POST:.1f} (mean a {chk_post[0]:.4f}, target {TARGET_A_POST}), δ = {DELTA:.1f} (mean a_x − a_y {chk_asym[2]:.4f}, target {TARGET_ASYM}); held fixed. "
         f"N_PAIRS = {N_PAIRS} pairs per subject, {N_SUBJ} subjects × 2 runs × {T} samples; the DMT run's white noises filtered at the pre and at the post parameters (β scaled by β̄_post/β̄) and spliced at sample {CHANGE_AT}; "
         f"(ii): x_t ← x_t + c y_(t−1), y_t ← y_t + c x_(t−1) on the post samples, each post segment rescaled to its SD before the coupling; (iv): x at β + δ, y at β − δ. W = {W}; bins of 30; {N_REP} replicates per condition; "
         f"bootstrap {N_BOOT} draws; sign-flip exact over 2^{N_SUBJ}; seed {SEED}. DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo, mean over subjects; ± is the SD over replicates. "
         "At the global fit the run-level prediction (constant across a run's bins; its DiD is zero and the residual DiD equals the observed DiD) and the period-level prediction ((a_x, a_y, q) measured on the pre and the post samples separately) are both tabulated, as in B17.", "",
         "| condition | estimator | sts level (pre) | sts DiD | predicted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |", "|---|---|---|---|---|---|---|---|---|"]
csv = ["condition,estimator,replicate,sts_level_pre,sts_did,pred_did,res_did,res_p,res_ci_lo,res_ci_hi,sym_did,anti_did"]
for name, change, dc, asym in CONDITIONS:
    acc = {est: {k: [] for k in ("lvl", "sts", "pred", "res", "p", "sym", "anti")} for est in ("W60", "global (run-level prediction)", "global (period-level prediction)")}
    for rep in range(N_REP):
        obs_w = np.empty((N_SUBJ, 2, 14)); pred_w = np.empty((N_SUBJ, 2, 14)); sym_w = np.empty((N_SUBJ, 2, 14)); anti_w = np.empty((N_SUBJ, 2, 14))
        obs_b = np.empty((N_SUBJ, 2, 28)); pred_b = np.empty((N_SUBJ, 2, 28)); pred_bp = np.empty((N_SUBJ, 2, 28))
        for s in range(N_SUBJ):
            betas, q = draw_params(N_PAIRS, BMEAN, QSD)
            for c in range(2):
                X = simulate_run(betas, q, change=(c == 0 and change), dc=(dc if c == 0 else 0.0), asym=asym)
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
        if rep % 10 == 9 or rep == N_REP - 1:
            print(f"   {name}: replicate {rep + 1}/{N_REP} ({time.time() - t0:.0f}s)", flush=True)
    for est in ("W60", "global (run-level prediction)", "global (period-level prediction)"):
        A = {k: np.array(v) for k, v in acc[est].items()}
        lines.append(f"| {name} | {est} | {A['lvl'].mean():.4f} | {A['sts'].mean():+.4f} ± {A['sts'].std():.4f} | {A['pred'].mean():+.4f} ± {A['pred'].std():.4f} | {A['res'].mean():+.4f} ± {A['res'].std():.4f} | "
                     f"{A['p'].mean():.3f}; {np.mean(A['p'] < 0.05):.2f} | {cell(A['sym'])} | {cell(A['anti'])} |")

# ---------------------------------------------------------------- population reference for B17's AR(1) conditions (i) and (iv)
N_POP = 20000


def sts_of(ax, ay, q):
    return atoms_from_corr(ar1_corr(ax, ay, q))[:, S]


def q_from_qe(ax, ay, qe):
    return qe * np.sqrt((1 - ax ** 2) * (1 - ay ** 2)) / (1 - ax * ay)


def qe_from_q(ax, ay, q):
    return np.clip(q * (1 - ax * ay) / np.sqrt((1 - ax ** 2) * (1 - ay ** 2)), -0.999, 0.999)


pop = {}
for cond, asym in (("(i)", False), ("(iv)", True)):
    if asym:
        a = rng.normal(0.85, 0.0125, N_POP); ax, ay = a + 0.015, a - 0.015
    else:
        ax, ay = rng.normal(0.85, 0.0125, N_POP), rng.normal(0.85, 0.0125, N_POP)
    qt = rng.choice(Q_POOL, N_POP); qe = qe_from_q(ax, ay, qt)
    pre = sts_of(ax, ay, qt).mean(); post = sts_of(ax - 0.015, ay - 0.015, q_from_qe(ax - 0.015, ay - 0.015, qe)).mean()
    pop[cond] = (pre, post)
b17 = {}
try:
    # B17's condition names contain commas and are not quoted, so the rows are split from the right: the last eleven
    # fields are the estimator, the replicate and the nine numeric columns; the remainder is the condition name.
    rows = [l.rsplit(",", 11) for l in (OUT / "calibration.csv").read_text().splitlines() if l and not l.startswith("#")][1:]
    for cond, key in (("(i)", "(i) Δa = −0.015, Δc = 0"), ("(iv)", "(iv) a_x − a_y = 0.03, Δa = −0.015")):
        for est, ek in (("W60", "W60"), ("global", "global (run-level prediction)")):
            sel = [r for r in rows if r[0] == key and r[1] == ek]
            assert sel, (key, ek)
            b17[(cond, est)] = (np.mean([float(r[3]) for r in sel]), np.mean([float(r[4]) for r in sel]))
except Exception as exc:                                                              # the committed B17 CSV is expected; the reference stands alone if it is absent
    print(f"   calibration.csv not read ({exc}); B17's columns left blank", flush=True)


def b17cell(cond, est, k):
    return f"{b17[(cond, est)][k]:{'+' if k else ''}.4f}" if (cond, est) in b17 else "—"


lines += ["", f"## Population reference for B17's AR(1) conditions (closed form at the drawn (a_x, a_y, q); {N_POP} draws of B17's distributions and its Q_POOL; post = (a_x − 0.015, a_y − 0.015) with the innovation correlation held as B17 holds it)", "",
          "| condition | population sts, pre | population sts, post | population change | B17 W60 level (pre) | B17 W60 sts DiD | B17 global level (pre) | B17 global sts DiD |", "|---|---|---|---|---|---|---|---|"]
for cond in ("(i)", "(iv)"):
    pre, post = pop[cond]
    lines.append(f"| {cond} | {pre:.4f} | {post:.4f} | {post - pre:+.4f} | {b17cell(cond, 'W60', 0)} | {b17cell(cond, 'W60', 1)} | {b17cell(cond, 'global', 0)} | {b17cell(cond, 'global', 1)} |")
def b17diff(est):
    return f"{b17[('(iv)', est)][0] - b17[('(i)', est)][0]:+.4f}" if ('(i)', est) in b17 and ('(iv)', est) in b17 else "—"


lines.append(f"| (iv) − (i), pre level | {pop['(iv)'][0] - pop['(i)'][0]:+.4f} | — | — | {b17diff('W60')} | — | {b17diff('global')} | — |")
lines += ["", "Predictions recorded (pre-run entry, B17b): the W = 60 sts level near the null's 1.18 rather than B17's 0.715; under (i) the sts DiD between −0.07 and −0.10 (the data's is −0.0809) and the residual DiD near the data's own null, +0.004 to +0.008; "
          "(ii) residual negative for either sign of Δc; (iii) additive; (iv) level lowered, residual near its (i) value; the population reference for B17 (i): a change of about −0.08 (1.19 → 1.11), and for (iv) − (i) a level difference of about −0.045. "
          "Rule: where B17 and B17b differ, the main text quotes B17b (the generator closer to the data) and S3 Text carries both; the finite-sample null of Results 4 is superseded by B17b where they overlap; the null's own DiD (+0.0054, review_v2_residual_null.log) is quoted beside B17b's (i). "
          "Each condition's row is read against these in the outcome entry."]
(OUT / "calibration_filtered.csv").write_text(f"# partB17b_calibration_filtered.py; one row per condition × estimator × replicate; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "calibration_filtered_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
