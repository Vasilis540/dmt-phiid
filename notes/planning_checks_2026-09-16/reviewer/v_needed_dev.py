# "Deviation needed" by B8's own derivation (matched symmetric VAR(1)), for residual -0.01 vs -0.0137, at (0.85, 0.25)
# and at the ts_gsr run-level operating point (0.867, 0.1945). Re-implements partB8's corr4/matched (partB8 writes files on import).
import sys, numpy as np
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import least_squares, brentq
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/dmt-phiid/notes")
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS
S = ATOMS.index("sts")
def corr4(a, c, qe):
    A = np.array([[a, c], [c, a]]); Q = np.array([[1.0, qe], [qe, 1.0]])
    S0 = solve_discrete_lyapunov(A, Q); S1 = A @ S0; C = np.block([[S0, S1.T], [S1, S0]]); d = np.sqrt(np.diag(C)); return C / np.outer(d, d)
def matched(c, r1, q):
    f = lambda p: [corr4(p[0], c, p[1])[0, 2] - r1, corr4(p[0], c, p[1])[0, 1] - q]
    lim = 0.995 - abs(c); sol = least_squares(f, [min(r1, lim - 0.01), q], bounds=([0.0, -0.995], [lim, 0.995]), xtol=1e-12, ftol=1e-12); return sol.x
def res_dev(c, r1, q):
    a, qe = matched(c, r1, q); C = corr4(a, c, qe)
    return atoms_from_corr(C)[0, S] - atoms_from_corr(ar1_corr(C[0, 2], C[1, 3], C[0, 1]))[0, S], C[0, 3] - C[1, 3] * C[0, 1]
for r1, q in ((0.85, 0.25), (0.867, 0.1945)):
    for target in (-0.01, -0.0137):
        c = brentq(lambda c: res_dev(c, r1, q)[0] - target, 0.0, 0.03)
        print(f"(r1, q) = ({r1}, {q}): residual {target}: c = {c:+.4f}, cross-lag deviation = {res_dev(c, r1, q)[1]:+.4f}")
