"""
check_C2_variance_ratio.py -- the window-variance / run-variance ratio as a shared driver
of the windowed sts and windowed r1 series.  All inputs are quoted from committed logs
(notes/review_results/logs/rev_extra.log, section (b) and (d)); nothing is re-run.

The paper quotes the variance ratio only against the GLOBAL-FIT sts bins (+0.37 per run,
Results 6) and as a caveat on the global fit (Results 3, 6).  review_computations_2026-09-14.md
section 6 also reports +0.49 / +0.54 per run for the WINDOWED sts and the windowed r1, and
+0.77 / +0.73 for the group-mean series.  Reproduced here from the committed series.
"""
import numpy as np
from scipy import stats
out = []; P = out.append

# rev_extra.log section (d), raw ts_gsr, group means by window
vr_dmt = np.array([1.138,1.222,1.323,1.425,0.998,0.707,0.755,0.745,0.791,0.911,0.937,0.989,1.067,1.102])
vr_pcb = np.array([0.819,0.953,1.010,0.964,0.798,0.904,0.925,1.011,1.022,1.037,1.094,1.097,1.199,1.273])
# rev_extra.log section (b), ts_gsr
sts_dmt = np.array([1.163,1.145,1.139,1.176,1.100,1.047,1.069,1.079,1.090,1.101,1.130,1.127,1.140,1.179])
sts_pcb = np.array([1.121,1.128,1.150,1.152,1.088,1.146,1.140,1.174,1.166,1.171,1.181,1.182,1.193,1.178])
r1_dmt  = np.array([0.851,0.847,0.843,0.851,0.836,0.823,0.829,0.833,0.835,0.841,0.843,0.841,0.845,0.855])
r1_pcb  = np.array([0.844,0.841,0.849,0.848,0.833,0.848,0.844,0.851,0.852,0.851,0.851,0.850,0.853,0.853])

P("Group-mean window series, ts_gsr, W = 60 (14 windows x 2 runs):")
P(f"  r(windowed sts, variance ratio), DMT run     = {stats.pearsonr(sts_dmt, vr_dmt).statistic:+.3f}")
P(f"  r(windowed sts, variance ratio), placebo run = {stats.pearsonr(sts_pcb, vr_pcb).statistic:+.3f}")
P(f"  r(windowed r1 , variance ratio), DMT run     = {stats.pearsonr(r1_dmt,  vr_dmt).statistic:+.3f}")
P(f"  r(windowed r1 , variance ratio), placebo run = {stats.pearsonr(r1_pcb,  vr_pcb).statistic:+.3f}")
a = np.r_[sts_dmt, sts_pcb]; b = np.r_[r1_dmt, r1_pcb]; v = np.r_[vr_dmt, vr_pcb]
P(f"  pooled over the 28 condition-windows: r(sts, ratio) = {stats.pearsonr(a, v).statistic:+.3f}, "
  f"r(r1, ratio) = {stats.pearsonr(b, v).statistic:+.3f}")
P(f"  review_computations section 6 states +0.77 / +0.73 for the group-mean series and")
P(f"  +0.49 / +0.54 per run on average; the paper quotes only +0.37, for the GLOBAL-FIT bins.")
P("")
P("Partial correlation of the two group-mean series, controlling the variance ratio:")
def partial(x, y, z):
    rx = x - np.polyval(np.polyfit(z, x, 1), z); ry = y - np.polyval(np.polyfit(z, y, 1), z)
    return stats.pearsonr(rx, ry).statistic
P(f"  r(sts, r1) over the 28 condition-windows          = {stats.pearsonr(a, b).statistic:+.3f}"
  f"   [paper: +0.977]")
P(f"  the same, partialling out the variance ratio      = {partial(a, b, v):+.3f}")
P("")
P("The variance contrast itself (rev_extra.log section (d), raw ts_gsr):")
P("  DMT pre 1.277 -> post 0.889 ; PCB pre 0.936 -> post 1.062")
P("  DiD -0.5137 [-0.6740, -0.3581], sign-flip p = 0.0001, negative in 14/14")
P("  -- larger, more consistent and more significant than the r1 DiD")
P("     (-0.0146 [-0.0251, -0.0052], p = 0.0106, 12/14) which the paper calls")
P("     'the mechanism's input'.")
P("  The paper residualises on framewise displacement but not on the window-variance ratio,")
P("  and reports no control for it on the primary windowed contrast.")
print("\n".join(out))
