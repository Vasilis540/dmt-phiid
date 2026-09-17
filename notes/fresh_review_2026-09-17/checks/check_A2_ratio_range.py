"""
check_A2_ratio_range.py -- the derivative ratio |d sts/d r1| / |d sts/d q| over the
operating REGION the overlay actually occupies, against the Abstract's single "32-fold".

Pair medians from notes/partB1_scope_map.md item 4 (all 20 variant x run x window cells of
subject 1): r1 medians 0.840-0.867 (ts_gsr) and 0.816-0.860 (ts_demean); median |q|
0.22-0.31 (ts_gsr) and 0.23-0.41 (ts_demean); 4-13 % (ts_gsr) and 7-30 % (ts_demean) of
pairs have |q| > 0.6.  Analytic; no data.
"""
import numpy as np
dsts_da = lambda a, q: 2*a/(1-a**2) - a*q**2/(1-a**2*q**2)
dsts_dq = lambda a, q: -a**2*q/(1-a**2*q**2)
ratio   = lambda a, q: abs(dsts_da(a, q)/dsts_dq(a, q))

print("ratio at the operating point the paper uses for every quoted derivative:")
print(f"  (0.85, 0.25) -> {ratio(0.85, 0.25):.2f}   [Abstract: '32-fold']")
print()
print("ratio across the observed median box (r1 0.816-0.867, |q| 0.22-0.41):")
for a in (0.816, 0.840, 0.850, 0.860, 0.867):
    print("  a = %.3f: " % a + "  ".join(f"|q|={q:.2f} -> {ratio(a, q):5.2f}"
                                          for q in (0.22, 0.24, 0.25, 0.31, 0.41)))
box = [ratio(a, q) for a in (0.816, 0.840, 0.850, 0.860, 0.867)
       for q in (0.22, 0.24, 0.25, 0.31, 0.41)]
print(f"  -> range over the box: {min(box):.2f} to {max(box):.2f}")
print()
print("and where the |q| > 0.6 minority sits (4-13 % of ts_gsr, 7-30 % of ts_demean pairs):")
for q in (0.60, 0.70, 0.80, 0.90, 0.95):
    print(f"  (0.85, {q:.2f}) -> {ratio(0.85, q):.2f}")
print()
print("the 'lower bound' points of Results 2 (ideal band-passed white noise), at |q| = 0.25:")
for a in (0.78, 0.82, 0.85, 0.93, 0.97):
    print(f"  ({a}, 0.25) -> {ratio(a, 0.25):.2f}")
