"""
partB8_coupling_map.py — Part B item 8 (pre-run entry in manuscript/analysis_record.md, 15 Sep 2026):
the symmetric VAR(1) pair with lagged coupling, x_{t+1} = a x_t + c y_t + ε, y_{t+1} = a y_t + c x_t + η,
corr(ε, η) = q_ε, in closed form (stationary covariance from the discrete Lyapunov equation, lag-1
covariance A Σ0), and what coupling does to the Gaussian-MMI atoms and to the B4 diagnostic.

Two views. (i) Raw: a and q_ε fixed, c varied — r1 and q then move with c. (ii) Matched: for each c, a and q_ε
re-solved so that the pair's r1 = corr(x_t, x_{t+1}) and q = corr(x_t, y_t) stay at the operating point;
the AR(1)-substituted prediction of B4 is then the same for every c, so the population residual
sts_true(c) − sts_pred is exactly what the diagnostic returns when lagged coupling of size c exists.
Outputs: notes/review_results/partB/coupling_map_tables.md. No data. Run: .venv/bin/python notes/partB8_coupling_map.py
"""
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import least_squares

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS, phir

OUT = Path(__file__).resolve().parents[1] / "notes" / "review_results" / "partB"
IX = {n: i for i, n in enumerate(ATOMS)}


def corr4(a, c, qe):
    """population 4x4 correlation matrix of (x_t, y_t, x_{t+1}, y_{t+1}) for the symmetric VAR(1)."""
    A = np.array([[a, c], [c, a]]); Q = np.array([[1.0, qe], [qe, 1.0]])
    S0 = solve_discrete_lyapunov(A, Q)                 # S0 = A S0 A' + Q
    S1 = A @ S0                                        # Cov(x_{t+1}, x_t)
    C = np.block([[S0, S1.T], [S1, S0]])
    d = np.sqrt(np.diag(C))
    return C / np.outer(d, d)


def stats(a, c, qe):
    C = corr4(a, c, qe)
    at = atoms_from_corr(C)[0]
    r1, q = C[0, 2], C[0, 1]
    xlag = C[0, 3]                                     # corr(x_t, y_{t+1})
    pred = atoms_from_corr(ar1_corr(r1, r1, q))[0]
    return dict(C=C, atoms=at, r1=r1, q=q, xlag=xlag, xlag_ar1=r1 * q, sts=at[IX["sts"]], pred=pred[IX["sts"]],
                self=at[IX["xtx"]] + at[IX["yty"]], rtr=at[IX["rtr"]], tdmi=at.sum(), phir=phir(at[None])[0],
                cross=at[IX["rtx"]] + at[IX["rty"]] + at[IX["xtr"]] + at[IX["ytr"]] + at[IX["xty"]] + at[IX["ytx"]])


def matched(c, r1_target, q_target):
    """(a, q_eps) such that the coupled pair has r1 = r1_target and q = q_target."""
    def f(p):
        C = corr4(p[0], c, p[1]); return [C[0, 2] - r1_target, C[0, 1] - q_target]
    lim = 0.995 - abs(c)                               # spectral radius of A is |a| + |c| < 1
    sol = least_squares(f, [min(r1_target, lim - 0.01), q_target], bounds=([0.0, -0.995], [lim, 0.995]), xtol=1e-12, ftol=1e-12)
    assert np.abs(sol.fun).max() < 1e-8, (c, sol.fun)
    return sol.x[0], sol.x[1]


lines = ["# Lagged coupling on the symmetric VAR(1) family (partB8_coupling_map.py)", ""]
for (r1_t, q_t, label) in ((0.85, 0.25, "the data's operating point"), (0.85, 0.0, "no instantaneous correlation"), (0.60, 0.25, "lower autocorrelation")):
    cs = [c for c in (-0.14, -0.10, -0.05, -0.02, 0.0, 0.02, 0.05, 0.10, 0.14) if abs(r1_t) + abs(c) < 0.99]
    lines += [f"## (r1, q) held at ({r1_t}, {q_t}) — {label}; a and q_ε re-solved for each c (matched view)", "",
              "| c | a | q_ε | corr(x_t, y_t+1) | a_y q (AR(1)) | sts | xtx + yty | sts − (xtx+yty) | rtr | six cross atoms | TDMI | ΦR | sts_pred (B4) | residual = sts − sts_pred |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    res_c = {}
    for c in cs:
        a, qe = matched(c, r1_t, q_t)
        s = stats(a, c, qe)
        res_c[c] = s
        lines.append(f"| {c:+.2f} | {a:.4f} | {qe:+.4f} | {s['xlag']:+.4f} | {s['xlag_ar1']:+.4f} | {s['sts']:.4f} | {s['self']:.4f} | {s['sts'] - s['self']:+.4f} | {s['rtr']:.4f} | {s['cross']:+.4f} | {s['tdmi']:.4f} | {s['phir']:.4f} | {s['pred']:.4f} | {s['sts'] - s['pred']:+.4f} |")
    # curvature of the residual in c at c = 0 (even function), and the coupling spread that gives −0.01 nats
    h = 0.02
    r0 = res_c[0.0]["sts"] - res_c[0.0]["pred"]; rp = res_c[h]["sts"] - res_c[h]["pred"]; rm = res_c[-h]["sts"] - res_c[-h]["pred"]
    curv = (rp + rm - 2 * r0) / h ** 2
    slope = (rp - rm) / (2 * h)
    lines += ["", f"Residual at c = 0: {r0:+.5f}; first derivative in c at 0: {slope:+.4f} nats per unit c; second derivative: {curv:+.3f} nats per unit c². "
              f"A spread of pair-specific coupling with zero mean and SD σ_c gives an expected residual of ½·{curv:+.3f}·σ_c² at fixed (r1, q); "
              f"σ_c = {np.sqrt(abs(0.02 / curv)) if curv else float('nan'):.3f} gives −0.01 nats" + (" (sign of curvature positive: coupling would raise the residual, not lower it)" if curv > 0 else "") + ".", ""]
    # raw view: a, q_eps fixed at the c = 0 solution
    a0, qe0 = matched(0.0, r1_t, q_t)
    lines += [f"### Raw view at the same point: a = {a0:.4f}, q_ε = {qe0:+.4f} fixed, c varied (r1 and q move with c)", "",
              "| c | r1 | q | sts | xtx + yty | ∂sts/∂c ≈ Δsts/Δc | for comparison ∂sts/∂r1 |", "|---|---|---|---|---|---|---|"]
    prev = None
    for c in cs:
        s = stats(a0, c, qe0)
        dsdr = (atoms_from_corr(ar1_corr(s["r1"] + 1e-4, s["r1"] + 1e-4, s["q"]))[0][IX["sts"]] - atoms_from_corr(ar1_corr(s["r1"] - 1e-4, s["r1"] - 1e-4, s["q"]))[0][IX["sts"]]) / 2e-4
        lines.append(f"| {c:+.2f} | {s['r1']:.4f} | {s['q']:+.4f} | {s['sts']:.4f} | {s['self']:.4f} | {'' if prev is None else f'{(s['sts'] - prev[1]) / (c - prev[0]):+.3f}'} | {dsdr:+.3f} |")
        prev = (c, s["sts"])
    lines.append("")
(OUT / "coupling_map_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
