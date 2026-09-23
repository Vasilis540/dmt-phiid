"""
partB23_diagnostic_alternatives.py — B23: the residual's response to the alternatives of the withdrawn direction argument
(population and a W = 60 simulation), CCS-sts against autocorrelation, the exposure of sts across the literature's
bands and TRs, the population Δr₁ of the calibration generators, and the unequal-coefficient grid. No data.
Pre-run entry: manuscript/analysis_record.md, "The residual's response to the alternatives of the direction argument,
CCS-sts against autocorrelation, exposure across datasets and the unequal-coefficient grid (B23): pre-run entry,
23 Sep 2026" (round 16, Part A).

One generator, np.random.default_rng(20261120), parts in the order (a)–(f); the q pool (20,000 draws of N(0, 0.3424)
clipped to ±0.8) is its first draw. residual = mean over pairs of sts(true 4 × 4) − sts(AR(1) matrix of a_x = C[0,2],
a_y = C[1,3], q = ½(C[0,1] + C[2,3])), partB4's substitution; matrices that are not positive definite are excluded from a
pool mean and their share reported. a = 0.85, and a = 0.8632 as a sensitivity, for all of (a).
(a1) δ added to both cross-lag entries at fixed (a, q); (a2) δ·sign(q); (a3) the symmetric coupled VAR(1) with (a, q_ε)
     re-solved so that r₁ = a and q are held (partB19's coupled_corr4, copied verbatim and checked at run time; the solve
     by least squares as partB19's coupled_sts_matched, polished by fsolve where its residual exceeds 1e-12; every solve
     required to hold r₁ and q to 1e-10), on a q grid from −0.8 to 0.8 in steps of 0.001, interpolated at
     the pool's q by a cubic spline; accuracy = the change in each pool mean when the step is doubled (required
     < 1e-5); c·sign(q) and −c through the invariance (c, q) → (−c, −q), checked at five grid points; (a4) B17's
     construction: A = [[a, c], [c, a]], unit innovations with correlation q, Γ₀ from the discrete Lyapunov equation;
     (a5) the shared slow component λ = |q|, a_s = a_n + 0.06, a_n = a − 0.06λ, the matrix in closed form; (a6) a pure
     Δa = −0.015 (residual zero by construction; required below 1e-12).
(b)  3,000 pairs (q from the same distribution), common random numbers (one set of standard-normal innovations per pair
     for the main run and one for an independent other run, shared by every condition); per condition and pair the
     VAR(1) with A = Γ₁Γ₀⁻¹ and Σ = Γ₀ − AΓ₀Aᵀ from the condition's population matrix (a pair whose Σ is not positive
     definite or whose A is not stable is excluded and counted), z₀ = 0, a burn-in of 200, 840 samples kept, 14 windows
     of 60 by review_v2_residual_null.window_corr (partB4's estimator); per pair and window the observed and
     AR(1)-substituted sts, the residual, r₁, δ_sym, δ_anti, D (partB15's response, copied verbatim); A_other with the
     sign of the pair's whole-run lag-0 correlation in the other run, A_same with the main run's; B per window. A change
     = the mean over pairs of the per-pair difference of the 14-window means against the unperturbed pairs, SE = SD over
     pairs / √N; B's change with its SE over the 14 windows. (a5) is simulated as three unit-variance AR(1) components
     and its changes are taken against the (a5) model at its base parameters.
(c)  symmetric AR(1) pairs (scipy.signal.lfilter, stationary start), one series of 10⁶ samples per point of r₁ ∈ {0.80,
     0.83, 0.85, 0.87, 0.90} × q ∈ {0.10, 0.25, 0.40} and one at (0.835, 0.25), the same two standard-normal streams at
     every point; PairPhiID fitted globally; CCS atoms by atoms_ccs under partB6's published mask (make_knowns and
     use_mask copied verbatim and checked at run time); MMI-sts from the same fit and in closed form.
(d)  the eleven band × TR settings of notes/partB5_literature_v2.md Table B item 2 and the primary setting; r₁ =
     ∫S(f) cos(2πf·TR) df / ∫S(f) df by scipy.integrate.quad, S = 1 or exp(−βf²) (f in Hz), β = 100, 200, 400; the flat
     value checked against the closed formula; sts in closed form at (r₁, r₁, 0.25).
(e)  B17b's generator (psd_weights and fit_filter imported from review_v2_residual_null.py; β̄, σ_q and β̄_post read from
     calibration_filtered_tables.md): 20,000 pairs, β ~ N(β̄, 0.5β̄) clipped at 5, q ~ N(0, σ_q) clipped to ±0.95; r₁(β)
     = acov[1]/acov[0], acov = the inverse real FFT of the weights on the 840-sample grid; sts in closed form at
     (r₁, r₁, q); post with β·β̄_post/β̄. The AR(1) generator's window-level Δr₁ under (i) by simulating B17's (i)
     (innov_corr and simulate_run copied verbatim from partB17_calibration.py and checked): 3,000 pairs, a_x, a_y ~
     N(0.85, 0.0125), q from scope_map_overlay_points.npz, a DMT run with Δa = −0.015 from sample 300, a placebo run
     without; the DiD of the window-level mean pair r₁ (windows 6–14 minus 1–4), SE over pairs.
(f)  atoms_from_corr(ar1_corr(a + d/2, a − d/2, q)) over mean a ∈ {0.80, 0.85, 0.90} × q ∈ {0.05, 0.10, 0.25, 0.40, 0.50,
     0.70} × d = |a_x − a_y| from 0 to 0.10 in steps of 0.0005.
Free choices: those above. --scale N divides the pool, the pairs, the series lengths and the (a3) grid resolution by N
(a check that the script runs; the accuracy check need not hold on the coarser grid). A failed check is printed as CHECK FAILED,
counted in the table header, and the run goes on.
Outputs (notes/review_results/partB/): diagnostic_alternatives_tables.md, diagnostic_alternatives.csv (one row per part,
condition, a and quantity), diagnostic_alternatives_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB23_diagnostic_alternatives.py   (minutes)
"""
import csv
import re
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import fsolve, least_squares
from scipy.signal import lfilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rev_phiid_fast as RPF
from rev_phiid_fast import PairPhiID, ATOMS, KNOWNS, _ccs_red, atoms_from_corr, ar1_corr
from review_v2_residual_null import psd_weights, fit_filter, window_corr, TARGET_ACF
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
SEED = 20261120
SCALE = int(sys.argv[sys.argv.index("--scale") + 1]) if "--scale" in sys.argv else 1
IX = {n: i for i, n in enumerate(ATOMS)}
S = IX["sts"]
N_POOL = 20000 // SCALE
N_B = 3000 // SCALE
N_C = 10 ** 6 // SCALE
N_E = 20000 // SCALE
N_E_AR1 = 3000 // SCALE
T, BURN, W, CHANGE_AT = 840, 200, 60, 300
TR_DATA = 2.0
A_LIST = (0.85, 0.8632)
PRE, POST = np.arange(0, 4), np.arange(5, 14)
t0 = time.time()
nan = float("nan")
CHECKS, CSV = [], ["part,condition,a,quantity,value,se"]
rng = np.random.default_rng(SEED)
POOL = np.clip(rng.normal(0, 0.3424, N_POOL), -0.8, 0.8)


def check(name, diff, tol):
    ok = bool(np.isfinite(diff) and diff <= tol)
    CHECKS.append((name, diff, tol, ok))
    if not ok:
        print(f"   CHECK FAILED: {name}: |difference| {diff:.3g} above {tol:.1g}", flush=True)
    return ok


def rec(part, cond, a, quantity, value, se=nan):
    CSV.append(f'{part},"{cond}",{a},"{quantity}",{value:.10g},{se:.6g}')


def verbatim(src_rel, first, last):
    """The block between this file's markers equals lines first–last of src_rel."""
    own = Path(__file__).read_text().split("\n")
    i = next(k for k, l in enumerate(own) if l.startswith(f"# ---- copied verbatim from {src_rel}, l. {first}–{last}"))
    j = next(k for k in range(i + 1, len(own)) if own[k].startswith("# ---- end of the copy"))
    src = (REPO / src_rel).read_text().split("\n")[first - 1:last]
    check(f"the copy of {src_rel} l. {first}–{last} is verbatim", 0.0 if own[i + 1:j] == src else 1.0, 0.0)


def sts(C):
    return atoms_from_corr(C)[:, S]


def pd_ok(C):
    return np.all(np.linalg.eigvalsh(C) > 0, axis=1)


def substituted(C):
    return ar1_corr(C[:, 0, 2], C[:, 1, 3], 0.5 * (C[:, 0, 1] + C[:, 2, 3]))


def residual_per_pair(C):
    """per-pair residual (NaN where the matrix is not positive definite)."""
    ok = pd_ok(C)
    r = np.full(C.shape[0], nan)
    r[ok] = sts(C[ok]) - sts(substituted(C[ok]))
    return r


def with_cross(C, d):
    C = C.copy()
    C[:, 0, 3] += d; C[:, 3, 0] += d; C[:, 1, 2] += d; C[:, 2, 1] += d
    return C


def var1_corr4_batch(A, Sig):
    """(n, 4, 4) lag-0/lag-1 correlation matrices of [x_t, y_t, x_{t+1}, y_{t+1}] for the VAR(1) z_{t+1} = A z_t + e,
    cov(e) = Sig, per pair: vec Γ₀ = (I − A ⊗ A)⁻¹ vec Sig, Γ₁ = A Γ₀ (E[z_{t+1} z_tᵀ])."""
    n = A.shape[0]
    K = np.eye(4)[None] - np.einsum("nij,nkl->nikjl", A, A).reshape(n, 4, 4)
    G0 = np.linalg.solve(K, Sig.reshape(n, 4, 1)).reshape(n, 2, 2)
    G1 = A @ G0
    M = np.concatenate([np.concatenate([G0, np.transpose(G1, (0, 2, 1))], 2), np.concatenate([G1, G0], 2)], 1)
    d = np.sqrt(np.einsum("nii->ni", M))
    return M / (d[:, :, None] * d[:, None, :])


# ---- copied verbatim from notes/partB19_exchange_rates.py, l. 75–79 (checked at run time)
def coupled_corr4(a, c, qe):
    A = np.array([[a, c], [c, a]]); Qm = np.array([[1.0, qe], [qe, 1.0]])
    S0 = solve_discrete_lyapunov(A, Qm); S1 = A @ S0
    C = np.block([[S0, S1.T], [S1, S0]]); d = np.sqrt(np.diag(C))
    return C / np.outer(d, d)
# ---- end of the copy


def coupled_matched(c, r1_target, q_target):
    """The coupled family's matrix at coupling c with (a, q_ε) re-solved so that r₁ and q stay at the targets
    (the least-squares solve of partB19's coupled_sts_matched, returning the matrix)."""
    def f(p):
        C = coupled_corr4(p[0], c, p[1]); return [C[0, 2] - r1_target, C[0, 1] - q_target]
    lim = 0.995 - abs(c)
    sol = least_squares(f, [min(r1_target, lim - 0.01), q_target], bounds=([0.0, -0.995], [lim, 0.995]), xtol=1e-12, ftol=1e-12)
    x, err = sol.x, float(np.abs(sol.fun).max())
    if err > 1e-12:                                          # polished from the least-squares solution (a free choice)
        x2 = fsolve(f, x, xtol=1e-14)
        err2 = float(np.abs(f(x2)).max())
        if err2 < err:
            x, err = x2, err2
    return coupled_corr4(x[0], c, x[1]), err


# ---- copied verbatim from notes/partB15_directed_crosslag.py, l. 70–92 (checked at run time)
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
# ---- end of the copy


# ---- copied verbatim from notes/partB6_ccs_definition.py, l. 51–80 (checked at run time)
def make_knowns(mask):
    """A drop-in for rev_phiid_fast.ccs_local_knowns with the requested double-redundancy mask."""
    def knowns(mi):
        R = {"R_xyta": _ccs_red(mi["I_xta"], mi["I_yta"], mi["I_xyta"]), "R_xytb": _ccs_red(mi["I_xtb"], mi["I_ytb"], mi["I_xytb"]),
             "R_xytab": _ccs_red(mi["I_xtab"], mi["I_ytab"], mi["I_xytab"]), "R_abtx": _ccs_red(mi["I_xta"], mi["I_xtb"], mi["I_xtab"]),
             "R_abty": _ccs_red(mi["I_yta"], mi["I_ytb"], mi["I_ytab"]), "R_abtxy": _ccs_red(mi["I_xyta"], mi["I_xytb"], mi["I_xytab"])}
        D = (-mi["I_xta"] - mi["I_xtb"] - mi["I_yta"] - mi["I_ytb"] + mi["I_xtab"] + mi["I_ytab"] + mi["I_xyta"] + mi["I_xytb"] - mi["I_xytab"]
             + R["R_xyta"] + R["R_xytb"] - R["R_xytab"] + R["R_abtx"] + R["R_abty"] - R["R_abtxy"])
        s0 = np.sign(mi["I_xta"])
        four = (s0 == np.sign(mi["I_xtb"])) & (s0 == np.sign(mi["I_yta"])) & (s0 == np.sign(mi["I_ytb"]))
        if mask == "code":
            agree = four & (s0 == np.sign(D))
        elif mask == "pub":
            agree = four & (s0 == np.sign(mi["I_xytab"]))
        elif mask == "pub8":
            agree = four & (s0 == np.sign(mi["I_xtab"])) & (s0 == np.sign(mi["I_ytab"])) & (s0 == np.sign(mi["I_xyta"])) & (s0 == np.sign(mi["I_xytb"])) & (s0 == np.sign(mi["I_xytab"]))
        elif mask == "pubD":
            agree = four & (s0 == np.sign(mi["I_xytab"])) & (s0 == np.sign(D))
        else:
            raise ValueError(mask)
        K = np.empty(mi["I_xta"].shape + (16,))
        K[..., 0] = np.where(agree, D, 0.0)
        for c, name in enumerate(KNOWNS[1:], start=1):
            K[..., c] = mi[name] if name in mi else R[name]
        return K, D, agree
    return knowns


def use_mask(mask):
    RPF.ccs_local_knowns = make_knowns(mask)
# ---- end of the copy


# ---- copied verbatim from notes/partB17_calibration.py, l. 67–86 (checked at run time)
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
# ---- end of the copy


verbatim("notes/partB19_exchange_rates.py", 75, 79)
verbatim("notes/partB15_directed_crosslag.py", 70, 92)
verbatim("notes/partB6_ccs_definition.py", 51, 80)
verbatim("notes/partB17_calibration.py", 67, 86)
lines = ["# The residual's response to the alternatives of the direction argument, CCS-sts against autocorrelation, exposure across datasets and the unequal-coefficient grid (partB23_diagnostic_alternatives.py)",
         f"git={SHA}", "",
         f"No data. Seed {SEED}, one generator, parts (a)–(f) in order; scale 1/{SCALE}. residual = pool mean of sts(true matrix) − sts(AR(1) matrix of the measured a_x, a_y and q) (partB4's substitution). "
         f"q pool: {N_POOL} draws of N(0, 0.3424) clipped to ±0.8.", ""]

# ================================================================ (a) population, closed form
lines += ["## (a) Population residual changes, closed form (pool means; the unperturbed residual is 0 on the AR(1) family)", ""]
A3 = {}
for a in A_LIST:
    base = ar1_corr(a, a, POOL)
    lines += [f"### a = {a}", "", "| alternative | perturbation | residual change | share excluded (not positive definite) | notes |", "|---|---|---|---|---|"]
    for kind in ("a1", "a2"):
        for dl in (0.005, -0.005, 0.01, -0.01, 0.02, -0.02):
            d = dl * (np.sign(POOL) if kind == "a2" else 1.0)
            r = residual_per_pair(with_cross(base, d))
            lab = f"δ = {dl:+.3f}" + (" × sign(q)" if kind == "a2" else "")
            lines.append(f"| ({kind}) {'δ at fixed (a, q)' if kind == 'a1' else 'δ·sign(q)'} | {lab} | {np.nanmean(r):+.5f} | {np.mean(np.isnan(r)):.4f} | |")
            rec(f"a_{kind}", lab, a, "residual change", float(np.nanmean(r)))
    # (a3) the coupled family, r₁ and q held
    step = 0.001 * SCALE
    grid = np.round(np.arange(-0.8, 0.8 + step / 2, step), 10)
    for c in (0.01, 0.02):
        res_g = np.empty(grid.size); worst = 0.0
        for k, qg in enumerate(grid):
            C, err = coupled_matched(c, a, qg)
            worst = max(worst, err)
            res_g[k] = (sts(C[None]) - sts(ar1_corr(C[0, 2], C[1, 3], 0.5 * (C[0, 1] + C[2, 3]))))[0]
        check(f"(a3) a = {a}, c = {c}: every grid solve holds r₁ and q to 1e-10", worst, 1e-10)
        spl = CubicSpline(grid, res_g)
        spl2 = CubicSpline(grid[::2], res_g[::2])
        for kk in np.linspace(0, grid.size - 1, 5).astype(int):              # invariance (c, q) → (−c, −q) at five grid points
            Cm, _ = coupled_matched(-c, a, -grid[kk])
            rm = (sts(Cm[None]) - sts(ar1_corr(Cm[0, 2], Cm[1, 3], 0.5 * (Cm[0, 1] + Cm[2, 3]))))[0]
            check(f"(a3) a = {a}: residual(−{c}, −q) = residual({c}, q) at q = {grid[kk]:+.3f}", abs(rm - res_g[kk]), 1e-8)
        for sign_c in (+1, -1):
            for mode in ("uniform", "aligned"):
                # residual(−c, q) = residual(c, −q); aligned: c·sign(q), so residual(c, |q|) for +c and residual(c, −|q|) for −c
                qq = (sign_c * POOL) if mode == "uniform" else (sign_c * np.abs(POOL))
                v, v2 = float(np.mean(spl(qq))), float(np.mean(spl2(qq)))
                check(f"(a3) a = {a}, c = {sign_c * c:+.2f} {mode}: pool mean stable when the grid step is doubled", abs(v - v2), 1e-5)
                lab = f"c = {sign_c * c:+.2f}" + (" × sign(q)" if mode == "aligned" else "")
                lines.append(f"| (a3) coupled family, r₁ and q held | {lab} | {v:+.5f} | 0.0000 | grid step {step:g}; step doubled: {v2:+.5f} (difference {abs(v - v2):.1e}) |")
                rec("a_a3", lab, a, "residual change", v)
                A3[(a, sign_c * c, mode)] = v
    # (a4) B17's construction
    lines += ["", f"(a4) B17's construction at a = {a}: A = [[a, c], [c, a]], unit innovations with correlation q (the c = 0 lag-0 correlation).", "",
              "| c | Δr₁ | Δ mean q | Δ mean \\|q\\| | mean δ_sym | residual change | residual / (mean δ_sym)² |", "|---|---|---|---|---|---|---|"]
    for c in (0.01, 0.02, 0.03, -0.02):
        Am = np.broadcast_to(np.array([[a, c], [c, a]]), (N_POOL, 2, 2)).copy()
        Sg = np.stack([np.stack([np.ones(N_POOL), POOL], 1), np.stack([POOL, np.ones(N_POOL)], 1)], 1)
        C = var1_corr4_batch(Am, Sg)
        if c == 0.01:
            ref = coupled_corr4(a, c, POOL[0])
            check(f"(a4) a = {a}: the batched Lyapunov matrix = coupled_corr4", float(np.max(np.abs(ref - C[0]))), 1e-10)
        ax, ay, q, sym, anti = deviations(C)
        r = residual_per_pair(C)
        dr1 = float(np.mean(0.5 * (ax + ay)) - a)
        lines.append(f"| {c:+.2f} | {dr1:+.5f} | {np.mean(q) - np.mean(POOL):+.5f} | {np.mean(np.abs(q)) - np.mean(np.abs(POOL)):+.5f} | {np.mean(sym):+.5f} | {np.nanmean(r):+.5f} | {np.nanmean(r) / np.mean(sym) ** 2:+.2f} |")
        for qn, v in (("Δr₁", dr1), ("Δ mean q", np.mean(q) - np.mean(POOL)), ("Δ mean |q|", np.mean(np.abs(q)) - np.mean(np.abs(POOL))),
                      ("mean δ_sym", np.mean(sym)), ("residual change", np.nanmean(r))):
            rec("a_a4", f"c = {c:+.2f}", a, qn, float(v))
    # (a5) the shared slow component
    lam = np.abs(POOL); sg = np.sign(POOL)

    def comp_matrix(a_s, a_n, lam_):
        r1 = lam_ * a_s + (1 - lam_) * a_n; rho0 = sg * lam_; kap = sg * lam_ * a_s
        C = np.empty((POOL.size, 4, 4))
        C[:, 0, 0] = C[:, 1, 1] = C[:, 2, 2] = C[:, 3, 3] = 1.0
        C[:, 0, 1] = C[:, 1, 0] = C[:, 2, 3] = C[:, 3, 2] = rho0
        C[:, 0, 2] = C[:, 2, 0] = C[:, 1, 3] = C[:, 3, 1] = r1
        C[:, 0, 3] = C[:, 3, 0] = C[:, 1, 2] = C[:, 2, 1] = kap
        return C, r1
    a_n0 = a - 0.06 * lam; a_s0 = a_n0 + 0.06
    C0, r10 = comp_matrix(a_s0, a_n0, lam)
    check(f"(a5) a = {a}: base r₁ = a", float(np.max(np.abs(r10 - a))), 1e-12)
    res0 = residual_per_pair(C0)
    al0 = np.mean(sg * deviations(C0)[3])
    lines += ["", f"(a5) shared slow component at a = {a} (λ = |q|, a_n = a − 0.06λ, a_s = a_n + 0.06): base residual {np.nanmean(res0):+.5f}, base mean(sign(q)·δ_sym) {al0:+.5f}.", "",
              "| change | Δr₁ | Δ mean(sign(q)·δ_sym) | residual change | residual change / Δr₁ | share excluded |", "|---|---|---|---|---|---|"]
    for lab, (a_s, a_n, lam_) in (("Δa_s = −0.01", (a_s0 - 0.01, a_n0, lam)), ("Δa_s = −0.02", (a_s0 - 0.02, a_n0, lam)),
                                  ("Δa_s = −0.03", (a_s0 - 0.03, a_n0, lam)), ("λ → 0.9λ", (a_s0, a_n0, 0.9 * lam))):
        C1, r11 = comp_matrix(a_s, a_n, lam_)
        res1 = residual_per_pair(C1)
        dr1 = float(np.mean(r11 - r10)); dres = float(np.nanmean(res1 - res0)); dal = float(np.mean(sg * deviations(C1)[3]) - al0)
        lines.append(f"| {lab} | {dr1:+.5f} | {dal:+.5f} | {dres:+.5f} | {dres / dr1:+.3f} | {np.mean(np.isnan(res1 - res0)):.4f} |")
        for qn, v in (("Δr₁", dr1), ("Δ mean(sign(q)·δ_sym)", dal), ("residual change", dres), ("residual change / Δr₁", dres / dr1)):
            rec("a_a5", lab, a, qn, v)
    # (a6) a pure autocorrelation change
    r6 = residual_per_pair(ar1_corr(a - 0.015, a - 0.015, POOL))
    check(f"(a6) a = {a}: the residual of a pure Δa = −0.015 is zero", float(np.nanmax(np.abs(r6))), 1e-12)
    lines += ["", f"(a6) pure Δa = −0.015 at a = {a}: largest |residual| over the pool {np.nanmax(np.abs(r6)):.1e}.", ""]
print(f"   (a) done ({time.time() - t0:.0f}s)", flush=True)

# ================================================================ (b) the W = 60 simulation
qb = np.clip(rng.normal(0, 0.3424, N_B), -0.8, 0.8)
ZM = rng.standard_normal((N_B, 2, BURN + T)); ZO = rng.standard_normal((N_B, 2, BURN + T))
ZM5 = rng.standard_normal((N_B, 3, BURN + T)); ZO5 = rng.standard_normal((N_B, 3, BURN + T))


def simulate_var1(C, Z):
    """z_{t+1} = A z_t + L e_t with A = Γ₁Γ₀⁻¹, Σ = Γ₀ − AΓ₀Aᵀ = LLᵀ from the population matrices C (n, 4, 4); z₀ = 0;
    returns X, Y (n, T) after the burn-in, and the validity mask."""
    G0 = C[:, :2, :2]
    G1 = np.stack([np.stack([C[:, 0, 2], C[:, 1, 2]], 1), np.stack([C[:, 0, 3], C[:, 1, 3]], 1)], 1)     # E[z_{t+1} z_tᵀ]
    A = G1 @ np.linalg.inv(G0)
    Sig = G0 - A @ G0 @ np.transpose(A, (0, 2, 1))
    ok = np.all(np.linalg.eigvalsh(0.5 * (Sig + np.transpose(Sig, (0, 2, 1)))) > 0, axis=1) & (np.max(np.abs(np.linalg.eigvals(A)), axis=1) < 1)
    L = np.zeros_like(Sig)
    L[ok] = np.linalg.cholesky(0.5 * (Sig[ok] + np.transpose(Sig[ok], (0, 2, 1))))
    z = np.zeros((C.shape[0], 2)); out = np.empty((C.shape[0], 2, T))
    for t in range(1, BURN + T):
        z = np.einsum("nij,nj->ni", A, z) + np.einsum("nij,nj->ni", L, Z[:, :, t])
        if t >= BURN:
            out[:, :, t - BURN] = z
    return out[:, 0], out[:, 1], ok


def simulate_components(a_s, a_n, lam_, Z):
    """x = √λ s + √(1 − λ) n_x, y = sign(q)√λ s + √(1 − λ) n_y with unit-variance AR(1) s (a_s), n_x, n_y (a_n)."""
    coef = np.stack([a_s, a_n, a_n], 1)
    scale = np.sqrt(1 - coef ** 2)
    u = np.zeros((a_s.size, 3)); out = np.empty((a_s.size, 3, T))
    for t in range(1, BURN + T):
        u = coef * u + scale * Z[:, :, t]
        if t >= BURN:
            out[:, :, t - BURN] = u
    sgn = np.sign(qb)[:, None]
    return (np.sqrt(lam_)[:, None] * out[:, 0] + np.sqrt(1 - lam_)[:, None] * out[:, 1],
            sgn * np.sqrt(lam_)[:, None] * out[:, 0] + np.sqrt(1 - lam_)[:, None] * out[:, 2], np.ones(a_s.size, bool))


def analyse(X, Y, Xo, Yo, ok):
    """per-pair 14-window means and the per-window slope B (over the valid pairs)."""
    n = X.shape[0]
    Cw = window_corr(X, Y, W)                                                  # window-major: index w·n + k
    ax, ay, q, sym, anti = deviations(Cw)
    base, r_anti, r_sym, r_both = response(ax, ay, q, sym, anti)
    obs = sts(Cw)
    qm = window_corr(X, Y, T); qo = window_corr(Xo, Yo, T)
    s_same = np.sign(0.5 * (qm[:, 0, 1] + qm[:, 2, 3])); s_other = np.sign(0.5 * (qo[:, 0, 1] + qo[:, 2, 3]))
    rs = lambda v: v.reshape(T // W, n)
    per = {"observed sts": rs(obs), "AR(1)-substituted sts": rs(base), "residual": rs(obs - base), "r₁": rs(0.5 * (ax + ay)),
           "A_other": rs(sym) * s_other[None], "A_same": rs(sym) * s_same[None], "D": rs(r_anti)}
    Bw = np.array([np.polyfit(rs(q)[w][ok], rs(sym)[w][ok], 1)[0] for w in range(T // W)])
    return {k: v.mean(0) for k, v in per.items()}, Bw


def run_condition(Cpop):
    X, Y, ok = simulate_var1(Cpop, ZM)
    Xo, Yo, ok2 = simulate_var1(Cpop, ZO)
    ok = ok & ok2
    X[~ok] = ZM[~ok, 0, BURN:]; Y[~ok] = ZM[~ok, 1, BURN:]; Xo[~ok] = ZO[~ok, 0, BURN:]; Yo[~ok] = ZO[~ok, 1, BURN:]   # placeholders, excluded below
    per, Bw = analyse(X, Y, Xo, Yo, ok)
    return per, Bw, ok


base_b = ar1_corr(0.85, 0.85, qb)
CONDS = [("(i) Δa = −0.015", ar1_corr(0.835, 0.835, qb)), ("(a1) δ = +0.02", with_cross(base_b, 0.02)), ("(a1) δ = −0.02", with_cross(base_b, -0.02)),
         ("(a2) δ = +0.01 × sign(q)", with_cross(base_b, 0.01 * np.sign(qb))), ("(a2) δ = −0.01 × sign(q)", with_cross(base_b, -0.01 * np.sign(qb)))]
C3 = np.empty((N_B, 4, 4)); worst = 0.0
for k in range(N_B):
    C3[k], err = coupled_matched(0.02, 0.85, qb[k]); worst = max(worst, err)
check("(b) (a3) every per-pair solve holds r₁ and q to 1e-10", worst, 1e-10)
CONDS.append(("(a3) c = +0.02, r₁ and q held", C3))
for c in (0.02, -0.02):
    Am = np.broadcast_to(np.array([[0.85, c], [c, 0.85]]), (N_B, 2, 2)).copy()
    Sg = np.stack([np.stack([np.ones(N_B), qb], 1), np.stack([qb, np.ones(N_B)], 1)], 1)
    CONDS.append((f"(a4) c = {c:+.02f}, B17's construction", var1_corr4_batch(Am, Sg)))
KEYS = ("observed sts", "AR(1)-substituted sts", "residual", "r₁", "A_other", "A_same", "D")
lines += ["## (b) W = 60 simulation: changes against the unperturbed pairs (common random numbers; mean ± SE)", "",
          f"{N_B} pairs, q ~ N(0, 0.3424) clipped to ±0.8, a = 0.85; runs of {T} samples after a burn-in of {BURN}; 14 windows of {W}; the other run an independent realisation. SE over pairs of each pair's 14-window mean; B's SE over the 14 windows.", ""]
per0, B0, ok0 = run_condition(base_b)
lines += ["Unperturbed AR(1) pairs, levels: " + "; ".join(f"{k} {per0[k][ok0].mean():+.5f}" for k in KEYS) + f"; B {B0.mean():+.5f}.", "",
          "| condition | pairs excluded | " + " | ".join(f"Δ {k}" for k in KEYS) + " | Δ B | residual change / Δr₁ |", "|" + "---|" * (len(KEYS) + 4)]


def change_row(lab, per, Bw, ok, per_ref, B_ref, ok_ref, part="b"):
    m = ok & ok_ref
    cells = []
    for k in KEYS:
        d = per[k][m] - per_ref[k][m]
        cells.append(f"{d.mean():+.5f} ± {d.std(ddof=1) / np.sqrt(m.sum()):.5f}")
        rec(part, lab, 0.85, f"Δ {k}", float(d.mean()), float(d.std(ddof=1) / np.sqrt(m.sum())))
    dB = Bw - B_ref
    rec(part, lab, 0.85, "Δ B", float(dB.mean()), float(dB.std(ddof=1) / np.sqrt(dB.size)))
    dres = float((per["residual"][m] - per_ref["residual"][m]).mean()); dr1 = float((per["r₁"][m] - per_ref["r₁"][m]).mean())
    ratio = dres / dr1 if abs(dr1) > 0 else nan
    rec(part, lab, 0.85, "residual change / Δr₁", ratio)
    return f"| {lab} | {int((~m).sum())} | " + " | ".join(cells) + f" | {dB.mean():+.5f} ± {dB.std(ddof=1) / np.sqrt(dB.size):.5f} | {ratio:+.3f} |"


for lab, Cpop in CONDS:
    per, Bw, ok = run_condition(Cpop)
    lines.append(change_row(lab, per, Bw, ok, per0, B0, ok0))
    print(f"   (b) {lab} done ({time.time() - t0:.0f}s)", flush=True)
lam_b = np.abs(qb); a_n_b = 0.85 - 0.06 * lam_b; a_s_b = a_n_b + 0.06


def run_components(a_s, a_n, lam_):
    X, Y, ok = simulate_components(a_s, a_n, lam_, ZM5)
    Xo, Yo, _ = simulate_components(a_s, a_n, lam_, ZO5)
    per, Bw = analyse(X, Y, Xo, Yo, ok)
    return per, Bw, ok


per5, B5, ok5 = run_components(a_s_b, a_n_b, lam_b)
lines.append(f"| (a5) base, against the unperturbed AR(1) pairs (levels differ by construction) | {int((~ok0).sum())} | " + " | ".join(f"{(per5[k] - per0[k])[ok0].mean():+.5f}" for k in KEYS) + f" | {(B5 - B0).mean():+.5f} | — |")
for lab, args in (("(a5) Δa_s = −0.03", (a_s_b - 0.03, a_n_b, lam_b)), ("(a5) λ → 0.9λ", (a_s_b, a_n_b, 0.9 * lam_b))):
    per, Bw, ok = run_components(*args)
    lines.append(change_row(lab + " (against the (a5) base)", per, Bw, ok, per5, B5, ok5))
lines += ["", "Predictions (pre-run entry): (a4) within 2 SE of Table 7's AR(1) rows (the review's −0.0049 and −0.0052 at c = +0.02 and −0.02); (a1) ±0.02 +0.0066 and +0.0064; (a2) +0.01 −0.0102 and −0.01 +0.0135; (i) +0.003 to +0.007.", ""]
print(f"   (b) done ({time.time() - t0:.0f}s)", flush=True)

# ================================================================ (c) CCS-sts against r₁
use_mask("pub")
E1 = rng.standard_normal(N_C); E2 = rng.standard_normal(N_C)


def ccs_point(a, q):
    e2 = q * E1 + np.sqrt(1 - q ** 2) * E2
    x = np.empty(N_C); y = np.empty(N_C)
    x[0], y[0] = E1[0] / np.sqrt(1 - a ** 2), e2[0] / np.sqrt(1 - a ** 2)            # stationary start
    x[1:] = lfilter([1.0], [1.0, -a], E1[1:], zi=[a * x[0]])[0]
    y[1:] = lfilter([1.0], [1.0, -a], e2[1:], zi=[a * y[0]])[0]
    pp = PairPhiID(np.vstack([x, y]))
    am = pp.atoms_ccs()[0]
    return float(am[0, S]), float(pp.atoms_mean()[0, S]), float(sts(ar1_corr(a, a, q))[0])


CC = {}
lines += ["## (c) Population CCS-sts (published mask) and MMI-sts on the symmetric AR(1) family", "",
          f"One series of {N_C} samples per point, fitted globally; the same two standard-normal streams at every point.", "",
          "| r₁ | q | CCS-sts | MMI-sts (the fit) | MMI-sts (closed form) |", "|---|---|---|---|---|"]
for q in (0.10, 0.25, 0.40):
    for a in (0.80, 0.83, 0.85, 0.87, 0.90):
        CC[(a, q)] = ccs_point(a, q)
        lines.append(f"| {a:.2f} | {q:.2f} | {CC[(a, q)][0]:+.5f} | {CC[(a, q)][1]:+.5f} | {CC[(a, q)][2]:+.5f} |")
        rec("c", f"r1 = {a}, q = {q}", a, "CCS-sts", CC[(a, q)][0]); rec("c", f"r1 = {a}, q = {q}", a, "MMI-sts (fit)", CC[(a, q)][1])
CC[(0.835, 0.25)] = ccs_point(0.835, 0.25)
slope = (CC[(0.87, 0.25)][0] - CC[(0.83, 0.25)][0]) / 0.04
slope_m = (CC[(0.87, 0.25)][1] - CC[(0.83, 0.25)][1]) / 0.04
dA = CC[(0.835, 0.25)][0] - CC[(0.85, 0.25)][0]
rec("c", "slope in r1 at q = 0.25", 0.85, "d CCS-sts / d r1", slope); rec("c", "Δa = −0.015 at (0.85, 0.25)", 0.85, "Δ CCS-sts", dA)
lines += ["", f"Central-difference slope of CCS-sts in r₁ at q = 0.25 (0.83 to 0.87): {slope:+.4f} per unit r₁ (MMI-sts from the same fits: {slope_m:+.4f}). "
          f"Change of CCS-sts from Δa = −0.015 at (0.85, 0.25): {dA:+.5f} (MMI-sts: {CC[(0.835, 0.25)][1] - CC[(0.85, 0.25)][1]:+.5f}).", ""]
print(f"   (c) done ({time.time() - t0:.0f}s)", flush=True)

# ================================================================ (d) exposure across the literature's bands and TRs
SETTINGS = [("0.008–0.09 Hz", 0.008, 0.09, tr) for tr in (2.0, 1.838, 0.72)] + [("0.0025–0.05 Hz", 0.0025, 0.05, tr) for tr in (2.0, 2.4, 2.6, 3.0, 1.25)] + \
           [("0.01–0.1 Hz", 0.01, 0.1, tr) for tr in (2.0, 1.0, 1.2)] + [("0.01–0.08 Hz (this study)", 0.01, 0.08, 2.0)]


def r1_band(lo, hi, tr, beta):
    num = quad(lambda f: np.exp(-beta * f * f) * np.cos(2 * np.pi * f * tr), lo, hi, limit=200)[0]
    den = quad(lambda f: np.exp(-beta * f * f), lo, hi, limit=200)[0]
    return num / den


lines += ["## (d) Exposure per unit of spectral difference: a flat band against the same band tilted by exp(−βf²), q = 0.25", "",
          "| band | TR (s) | r₁ flat | β | Δr₁ | Δsts | Δsts / Δr₁ |", "|---|---|---|---|---|---|---|"]
for lab, lo, hi, tr in SETTINGS:
    r_flat = r1_band(lo, hi, tr, 0.0)
    closed = (np.sin(2 * np.pi * hi * tr) - np.sin(2 * np.pi * lo * tr)) / (2 * np.pi * (hi - lo) * tr)
    check(f"(d) {lab} TR {tr}: flat r₁ by quadrature = the closed formula", abs(r_flat - closed), 1e-10)
    s_flat = sts(ar1_corr(r_flat, r_flat, 0.25))[0]
    for beta in (100.0, 200.0, 400.0):
        r_t = r1_band(lo, hi, tr, beta)
        ds = sts(ar1_corr(r_t, r_t, 0.25))[0] - s_flat
        lines.append(f"| {lab} | {tr:g} | {r_flat:.4f} | {beta:g} | {r_t - r_flat:+.5f} | {ds:+.4f} | {ds / (r_t - r_flat):+.2f} |")
        for qn, v in (("r1 flat", r_flat), ("Δr1", r_t - r_flat), ("Δsts", ds), ("Δsts/Δr1", ds / (r_t - r_flat))):
            rec("d", f"{lab}, TR {tr}, β {beta:g}", nan, qn, v)
lines.append("")

# ================================================================ (e) population Δr₁ and Δsts of the calibration generators
CFT = (OUT / "calibration_filtered_tables.md").read_text()
BMEAN = float(re.search(r"β̄ = (\d+\.\d+) \(window-level mean a", CFT).group(1))
QSD = float(re.search(r"σ_q = (\d\.\d+) \(mean \|q\|", CFT).group(1))
BMEAN_POST = float(re.search(r"β̄_post = (\d+\.\d+) \(mean a", CFT).group(1))
FIT = fit_filter(TARGET_ACF["placebo"])
LO, HI = FIT[2], FIT[3]
betas = np.clip(rng.normal(BMEAN, 0.5 * BMEAN, N_E), 5, None)
qe_ = np.clip(rng.normal(0, QSD, N_E), -0.95, 0.95)
f840 = np.fft.rfftfreq(T, d=TR_DATA)


def r1_filter(b):
    acov = np.fft.irfft(psd_weights(f840, b, LO, HI), n=T, axis=1)
    return acov[:, 1] / acov[:, 0]


r1_pre, r1_post = r1_filter(betas), r1_filter(betas * (BMEAN_POST / BMEAN))
s_pre, s_post = sts(ar1_corr(r1_pre, r1_pre, qe_)), sts(ar1_corr(r1_post, r1_post, qe_))
lines += ["## (e) Population Δr₁ and Δsts under condition (i)", "",
          f"Band-passed generator (B17b; β̄ = {BMEAN}, σ_q = {QSD}, β̄_post = {BMEAN_POST} from calibration_filtered_tables.md; filter edges {LO:.4f}–{HI:.3f} Hz; {N_E} pairs; exact circular lag-1 autocorrelation on the 840-sample grid): "
          f"population r₁ {r1_pre.mean():.4f} → {r1_post.mean():.4f} (Δr₁ {r1_post.mean() - r1_pre.mean():+.5f}); population sts {s_pre.mean():.4f} → {s_post.mean():.4f} (Δsts {s_post.mean() - s_pre.mean():+.5f})."]
rec("e", "band-passed generator (i)", nan, "population Δr1", float(r1_post.mean() - r1_pre.mean()))
rec("e", "band-passed generator (i)", nan, "population Δsts", float(s_post.mean() - s_pre.mean()))
Q_POOL = np.load(OUT / "scope_map_overlay_points.npz")["pre_w1to4_q"]
Q_POOL = Q_POOL[np.isfinite(Q_POOL)]
ax_e, ay_e = rng.normal(0.85, 0.0125, N_E_AR1), rng.normal(0.85, 0.0125, N_E_AR1)
qe_e = innov_corr(ax_e, ay_e, rng.choice(Q_POOL, N_E_AR1))
r1_runs = {}
for c, change in ((0, True), (1, False)):
    Xr = simulate_run(ax_e, ay_e, qe_e, -0.015, 0.0, change)
    Cw = window_corr(Xr[0::2], Xr[1::2], W)
    r1_runs[c] = (0.5 * (Cw[:, 0, 2] + Cw[:, 1, 3])).reshape(T // W, N_E_AR1)
d_pair = (r1_runs[0][POST].mean(0) - r1_runs[0][PRE].mean(0)) - (r1_runs[1][POST].mean(0) - r1_runs[1][PRE].mean(0))
lines += [f"AR(1) generator (B17's (i), simulated: calibration.csv holds no window-level r₁; {N_E_AR1} pairs): population Δr₁ −0.015 by construction; window-level Δr₁ DiD (windows 6–14 minus 1–4, DMT minus placebo) "
          f"{d_pair.mean():+.5f} ± {d_pair.std(ddof=1) / np.sqrt(N_E_AR1):.5f} (SE over pairs).", ""]
rec("e", "AR(1) generator (i), simulated", 0.85, "window-level Δr1 DiD", float(d_pair.mean()), float(d_pair.std(ddof=1) / np.sqrt(N_E_AR1)))
print(f"   (e) done ({time.time() - t0:.0f}s)", flush=True)

# ================================================================ (f) the unequal-coefficient grid
lines += ["## (f) Unequal coefficients: mean a × q × |a_x − a_y| (0 to 0.10 in steps of 0.0005)", "",
          "| mean a | q | max \\|str − min(xtx, yty)\\| | min(rts − str) | max(sts − (xtx + yty + rtr)) | asymmetry at which sts − (xtx + yty) first turns negative |", "|---|---|---|---|---|---|"]
dgrid = np.round(np.arange(0, 0.10 + 1e-12, 0.0005), 6)
for a in (0.80, 0.85, 0.90):
    for q in (0.05, 0.10, 0.25, 0.40, 0.50, 0.70):
        At = atoms_from_corr(ar1_corr(a + dgrid / 2, a - dgrid / 2, np.full(dgrid.size, q)))
        g = {n: At[:, i] for n, i in IX.items()}
        e1 = float(np.max(np.abs(g["str"] - np.minimum(g["xtx"], g["yty"]))))
        e2 = float(np.min(g["rts"] - g["str"]))
        e3 = float(np.max(g["sts"] - (g["xtx"] + g["yty"] + g["rtr"])))
        neg = np.where(g["sts"] - (g["xtx"] + g["yty"]) < 0)[0]
        first = f"{dgrid[neg[0]]:.4f}" if neg.size else "none"
        lines.append(f"| {a:.2f} | {q:.2f} | {e1:.1e} | {e2:+.1e} | {e3:+.1e} | {first} |")
        rec("f", f"a = {a}, q = {q}", a, "first negative asymmetry", float(dgrid[neg[0]]) if neg.size else nan)
lines.append("")

n_fail = sum(1 for c in CHECKS if not c[3])
lines[4:4] = [f"Checks: {len(CHECKS)} run, {n_fail} failed" + ("" if n_fail == 0 else " — listed as CHECK FAILED under Checks") + ".", ""]
lines += ["## Checks", ""] + [f"- {'ok' if ok else 'CHECK FAILED'}: {n} (|difference| {d:.3g}, tolerance {t:.1g})" for n, d, t, ok in CHECKS]
lines += ["", "## Predictions and rule (pre-run entry, B23)", "",
          "Predictions: (a1) +0.0036 and +0.0037 at ±0.01, +0.0154 and +0.0158 at ±0.02; (a2) −0.0224 at +0.01 and +0.0297 at −0.01; (a3) +0.0029 at +0.01, +0.0102 at +0.02, +0.0070 at −0.02 (a 400-draw pool), the aligned version at first order; "
          "(a4) negative for either sign, about −22 δ_sym²; (a5) the residual rises as the shared component weakens, about −1.2 per unit Δr₁. (b) (a4) within 2 SE of Table 7's AR(1) rows; (a1) ±0.02 +0.0066 and +0.0064; (a2) +0.01 −0.0102, −0.01 +0.0135; (i) +0.003 to +0.007. "
          "(c) CCS-sts falls as r₁ rises at fixed q, slope at (0.85, 0.25) between −2 and −0.1. (d) Δsts within ±15 % across TR 0.72–2 s while Δr₁ varies about sevenfold (0.008–0.09 Hz: β = 100 +0.190/+0.165; 200 +0.382/+0.335; 400 +0.738/+0.658). "
          "(e) population Δr₁ −0.010 to −0.020, Δsts −0.08 to −0.15. (f) extremes zero to rounding; at a = 0.85 the sign change at about 0.008 (q 0.25), 0.035 (0.5), 0.09 (0.7); none within 0.10 at (0.80, 0.70). "
          "Several are values already computed on 22 Sep on other pools or designs (the pre-run entry lists them).",
          "Rule: (a) and (b) replace the direction argument; (c) replaces \"does not follow autocorrelation\"; (d) replaces \"most exposed dataset\"; (e) completes Table 5's Δr₁ column; (f) replaces Results 1's two wrong statements (Finding 12)."]
(OUT / "diagnostic_alternatives.csv").write_text(f"# partB23_diagnostic_alternatives.py; one row per part, condition, a and quantity; git={SHA}\n" + "\n".join(CSV) + "\n")
(OUT / "diagnostic_alternatives_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"   checks: {len(CHECKS)} run, {n_fail} failed")
print(f"done ({time.time() - t0:.0f}s)")
