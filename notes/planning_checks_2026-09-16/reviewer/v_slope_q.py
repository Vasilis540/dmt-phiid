# First-order response of the B4 residual to a cross-lag deviation, as a function of q (analytic; no data).
# Perturb the cross-lag entries of the AR(1) matrix by +d*sign... directly: C = ar1_corr(a, a, q); C[0,3]=C[3,0]+=d; C[1,2]=C[2,1]+=d.
import sys, numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/dmt-phiid/notes")
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS
S = ATOMS.index("sts")
a = 0.867; h = 1e-4
for q in (0.0, 0.02, 0.05, 0.10, 0.19, 0.25, 0.40):
    base = ar1_corr(a, a, q)
    def res(d):
        C = base.copy(); C[:, 0, 3] += d; C[:, 3, 0] += d; C[:, 1, 2] += d; C[:, 2, 1] += d
        return atoms_from_corr(C)[0, S] - atoms_from_corr(base)[0, S]
    slope = (res(h) - res(-h)) / (2 * h); curv = (res(h) + res(-h)) / h ** 2
    print(f"q {q:+.2f}: d(residual)/d(deviation) {slope:+.3f}   slope/q {slope / q if q else float('nan'):+.2f}   curvature {curv:+.1f}")
