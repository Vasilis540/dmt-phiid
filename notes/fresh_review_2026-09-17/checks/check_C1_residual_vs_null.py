"""
check_C1_residual_vs_null.py -- checks of existing outputs only (no re-run of the pipeline).

(1) Is the observed residual DiD (+0.0115) statistically distinguishable from the
    finite-sample null's value (+0.0054, range +0.0037 to +0.0077)?  The paper asserts
    "the rest ... is not accounted for by the null as specified".
(2) Is the run-level residual (-0.0137, -1.1 %) distinguishable from the null's
    (-0.0045, -0.34 %)?  The paper calls it "three times the null's".
(3) The attenuation ceiling on the headline per-subject collinearity r = 0.953, from the
    split-half reliabilities the paper itself reports (splithalf_tables.md).
(4) The family-scale conversion of delta_run into a residual: the paper's 44 % / 37 %.
"""
import csv, itertools, numpy as np, pickle
from pathlib import Path
from scipy import stats

R = Path('/mnt/user-data/uploads/dmt-phiid')
SIGNS = np.array(list(itertools.product((-1, 1), repeat=14)))
out = []; P = out.append

def sfp(v, mu=0.0):
    v = np.asarray(v, float) - mu
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= abs(v.mean()) - 1e-12))

def bci(v, seed=20261120, n=10000):
    rng = np.random.default_rng(seed); v = np.asarray(v, float)
    return np.percentile(v[rng.integers(0, v.size, (n, v.size))].mean(1), [2.5, 97.5])

rows = {}
for f in ['raw', 'diag']:
    for r in pickle.load(open(R / f'notes/review_results/inference_rows_{f}.pkl', 'rb')):
        rows[(f, r['label'], r['set'])] = r

P("="*78); P("(1) OBSERVED RESIDUAL DiD vs THE FINITE-SAMPLE NULL")
P("="*78)
res = np.asarray(rows[('diag', 'diag residual sts ts_gsr W60', 'primary')]['did_subjects'], float)
lo, hi = bci(res)
P(f"  observed residual DiD (ts_gsr W60, primary) = {res.mean():+.5f}  95 % CI [{lo:+.5f}, {hi:+.5f}]")
P(f"  sign-flip p against 0                        = {sfp(res):.4f}")
for nullv, lab in [(0.0054, "primary null (h = 0.5, DMT-post/placebo ACF)"),
                   (0.0037, "lowest of the third review's variations"),
                   (0.0077, "highest of the third review's variations"),
                   (0.0052, "third review, h = 0.5"), (0.0059, "third review, h = 0.25")]:
    inside = lo <= nullv <= hi
    P(f"  null = {nullv:+.4f} ({lab}):")
    P(f"      inside the observed 95 % CI? {'YES' if inside else 'no'};"
      f"  sign-flip p for (observed - null) = {sfp(res, nullv):.4f}")
P("  => EVERY null value, including the largest, lies inside the observed CI, and the")
P("     excess over the null is not significant at any of them.  The residual DiD is")
P("     statistically compatible with being entirely finite-sample under this null.")
P("")

P("="*78); P("(2) RUN-LEVEL RESIDUAL vs THE NULL'S -0.34 %")
P("="*78)
cl = list(csv.DictReader(open(R / 'notes/review_results/partB/crosslag_deviation.csv')))
for var in ['ts_gsr', 'ts_demean']:
    sub = [r for r in cl if r['variant'] == var]
    per = {}
    for r in sub:
        per.setdefault(int(r['subject']), {})[r['condition']] = (
            float(r['residual']), float(r['observed_sts']))
    v = np.array([np.mean([per[s][c][0] for c in ('DMT', 'PCB')]) for s in sorted(per)])
    o = np.array([np.mean([per[s][c][1] for c in ('DMT', 'PCB')]) for s in sorted(per)])
    lo, hi = bci(v)
    pct = 100 * v / o
    plo, phi = bci(pct)
    P(f"  {var}: run-level residual mean {v.mean():+.5f}  95 % CI [{lo:+.5f}, {hi:+.5f}]"
      f"   (as % of observed: {pct.mean():+.2f} % [{plo:+.2f}, {phi:+.2f}])")
    P(f"     sign-flip p against 0 = {sfp(v):.4f}; negative in {int((v<0).sum())}/14")
    if var == 'ts_gsr':
        for nullv in [-0.0045]:
            P(f"     null (W = 840, homogeneous filter) = {nullv:+.5f} "
              f"({-0.34:+.2f} %): inside the observed CI? "
              f"{'YES' if lo <= nullv <= hi else 'no'};"
              f"  sign-flip p for (observed - null) = {sfp(v, nullv):.4f}")
        P("     => the run-level residual IS significantly more negative than the null's")
        P("        value, so 'three times the null's' is supported in sign and order here,")
        P("        but no interval is given for it anywhere in the paper or the tables.")
P("")

P("="*78); P("(3) ATTENUATION CEILING ON THE HEADLINE r = 0.953")
P("="*78)
P("  Split-half (odd vs even window) reliabilities of the per-subject DiDs, from")
P("  notes/review_results/partB/splithalf_tables.md (the values the paper quotes as")
P("  '0.71-0.74 and 0.69-0.72'):")
for var, rel_sts, rel_r1, obs in [('ts_gsr', 0.717, 0.741, 0.9528),
                                  ('ts_demean', 0.686, 0.712, 0.9578)]:
    ceil_half = np.sqrt(rel_sts * rel_r1)
    sb = lambda r: 2 * r / (1 + r)                      # Spearman-Brown, half -> full
    ceil_full = np.sqrt(sb(rel_sts) * sb(rel_r1))
    P(f"  {var}: rel(MMI-sts DiD) = {rel_sts}, rel(r1 DiD) = {rel_r1}")
    P(f"     ceiling using the raw split-half values      = {ceil_half:.3f}"
      f"   (observed {obs:.3f} -> disattenuated {obs/ceil_half:.2f})")
    P(f"     ceiling using Spearman-Brown full-length rel = {ceil_full:.3f}"
      f"   (observed {obs:.3f} -> disattenuated {obs/ceil_full:.2f})")
P("  A correlation between two *reliable* components cannot exceed sqrt(rel*rel) if the")
P("  two measurements' errors are independent.  The observed 0.953 exceeds both ceilings,")
P("  and disattenuates above 1.  Errors are therefore NOT independent: a material part of")
P("  the 0.953 is estimation noise shared by two quantities read off the same 60-TR")
P("  windows.  This is the argument the paper applies to the residual/CCS-sts pair")
P("  (Results 4: 'most of the within-half correlation ... is estimation noise common to")
P("  the same windows'); it is not applied to the 0.953, and no split-half of that pair")
P("  is reported, although splithalf_tables.md holds both reliabilities.")
P("")

P("="*78); P("(4) THE FAMILY-SCALE CONVERSION: 44 % AT THE OPERATING POINT, 37 % AT 'THE")
P("     PAIRS' MEAN POINT'")
P("="*78)
NAMES = ['r', 'x', 'y', 's']
LEQ = np.array([[1,1,1,1],[0,1,0,1],[0,0,1,1],[0,0,0,1]], bool)
def mi(S, A, B):
    A, B = list(A), list(B)
    return 0.5*np.log(np.linalg.det(S[np.ix_(A,A)])*np.linalg.det(S[np.ix_(B,B)])
                      / np.linalg.det(S[np.ix_(A+B, A+B)]))
def phiid(S):
    past = {0:[(0,),(1,)],1:[(0,)],2:[(1,)],3:[(0,1)]}
    fut  = {0:[(2,),(3,)],1:[(2,)],2:[(3,)],3:[(2,3)]}
    cum = {(a,b): min(mi(S,A,B) for A in past[a] for B in fut[b])
           for a in range(4) for b in range(4)}
    order = sorted(cum, key=lambda n: sum(LEQ[:,n[0]])+sum(LEQ[:,n[1]]))
    at = {}
    for n in order:
        at[n] = cum[n] - sum(at[m] for m in order
                             if m != n and LEQ[m[0],n[0]] and LEQ[m[1],n[1]])
    return {NAMES[a]+'t'+NAMES[b]: v for (a,b), v in at.items()}
def S4(a, q, dev=0.0):
    return np.array([[1, q, a, a*q+dev],[q, 1, a*q+dev, a],
                     [a, a*q+dev, 1, q],[a*q+dev, a, q, 1]], float)
for (a, q, lab) in [(0.85, 0.25, "operating point (0.85, 0.25)"),
                    (0.8666, 0.1945, "run-level mean pair point (0.8666, 0.1945)"),
                    (0.848, 0.24, "the 'pairs' own point' of Results 2 (0.848, 0.24)")]:
    d0 = phiid(S4(a, q))['sts']; d1 = phiid(S4(a, q, 0.00340))['sts']
    P(f"  {lab}: sts {d0:.5f} -> {d1:.5f}; change {d1-d0:+.5f} nats for delta_run = +0.00340")
    P(f"      as a share of the -0.0137 run-level residual: {100*abs(d1-d0)/0.0137:.1f} %")
P("  record (analysis_record.md, 'Conversion to a residual on the family'): -0.0061 (44 %)")
P("  at (0.85, 0.25) and -0.0051 (37 %) at (a 0.8666, |q| 0.1945).  Both reproduce.")
P("  NOTE: the point the paper calls 'the pairs' mean point' in Results 4 is the RUN-level")
P("  mean (0.8666, 0.1945); the point Results 2 calls 'the pairs' own point' is the")
P("  WINDOW-level mean (0.848, 0.24).  Neither Results 4 nor the Methods states which is")
P("  meant, and the two give 37 % and 43 %.")
print("\n".join(out))

# ---- appended: reconcile the planning-check slope (-2.090 at q = 0.25) with mine (-1.856)
print()
print("="*78)
print("(5) APPENDED: d sts / d(cross-lag deviation) as a function of a, to reconcile")
print("    notes/planning_checks_2026-09-16/reviewer/v_slope_q.log (a = 0.867) with")
print("    check_A1's value at the operating point (a = 0.85).")
print("="*78)
for a_ in (0.85, 0.8666, 0.867):
    for q_ in (0.02, 0.05, 0.10, 0.19, 0.25, 0.40):
        h = 1e-4
        s = (phiid(S4(a_, q_, h))['sts'] - phiid(S4(a_, q_, -h))['sts'])/(2*h)
        c = (phiid(S4(a_, q_, h))['sts'] + phiid(S4(a_, q_, -h))['sts']
             - 2*phiid(S4(a_, q_))['sts'])/h**2
        print(f"  a = {a_}: q {q_:+.2f}: slope {s:+.3f}  slope/q {s/q_:+.2f}  curvature {c:+.1f}")
    print()
print("  v_slope_q.log at a = 0.867: q 0.02 -0.157, 0.05 -0.393, 0.10 -0.793,")
print("  0.19 -1.546, 0.25 -2.090, 0.40 -3.720; curvature +47.8 to +82.4.")
