"""
partB5_family_checks.py — the closed-form inputs quoted in notes/partB5_literature.md, Table B items 1–2:
atom derivatives on the symmetric bivariate AR(1) family at two operating points; the exact identities
on that family (TDMI = −ln(1 − a²) independent of q; rtr + sts = TDMI hence ∂rtr/∂q = −∂sts/∂q;
ΦR ≡ rtr = −½ ln(1 − a² q²)); ΦR − rtr for unequal a_x ≠ a_y (seeded draws); the derivative ratio
|∂sts/∂r₁| / |∂sts/∂q| at the r₁ values implied by the studies' band-pass and TR; and the lag-1
autocorrelation of ideal band-passed white noise. Output: notes/review_results/partB/family_checks.log
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS

REPO = Path(__file__).resolve().parents[1]
IX = {n: i for i, n in enumerate(ATOMS)}
H = 1e-3
SEED = 20261120


def A(r, q, ax=None):
    r = np.atleast_1d(np.asarray(r, float)); q = np.atleast_1d(np.asarray(q, float))
    return atoms_from_corr(ar1_corr(r if ax is None else ax, r, q))


def phir(At):
    ixx = At[:, IX["rtr"]] + At[:, IX["rtx"]] + At[:, IX["xtr"]] + At[:, IX["xtx"]]
    iyy = At[:, IX["rtr"]] + At[:, IX["rty"]] + At[:, IX["ytr"]] + At[:, IX["yty"]]
    return At.sum(1) - ixx - iyy + At[:, IX["rtr"]]


def groups(At):
    return {"sts": At[:, IX["sts"]], "xtx+yty": At[:, IX["xtx"]] + At[:, IX["yty"]], "TDMI": At.sum(1), "rtr": At[:, IX["rtr"]],
            "rts+str": At[:, IX["rts"]] + At[:, IX["str"]], "mirrors": At[:, IX["xts"]] + At[:, IX["yts"]] + At[:, IX["stx"]] + At[:, IX["sty"]], "PhiR": phir(At)}


lines = ["# Family checks (partB5_family_checks.py)", ""]
for r, q in ((0.85, 0.25), (0.85, 0.5), (0.97, 0.25)):
    g0, gr1, gr2, gq1, gq2 = groups(A(r, q)), groups(A(r + H, q)), groups(A(r - H, q)), groups(A(r, q + H)), groups(A(r, q - H))
    lines.append(f"({r}, {q}): levels " + ", ".join(f"{k} {g0[k][0]:.4f}" for k in g0))
    lines.append("   d/dr1: " + ", ".join(f"{k} {((gr1[k] - gr2[k]) / (2 * H))[0]:+.3f}" for k in g0))
    lines.append("   d/dq:  " + ", ".join(f"{k} {((gq1[k] - gq2[k]) / (2 * H))[0]:+.3f}" for k in g0))
    lines.append(f"   ratio |dsts/dr1| / |dsts/dq| = {abs(((gr1['sts'] - gr2['sts']) / (2 * H))[0]) / abs(((gq1['sts'] - gq2['sts']) / (2 * H))[0]):.1f}; rtr / sts level = {100 * g0['rtr'][0] / g0['sts'][0]:.2f} %")
rng = np.random.default_rng(SEED)
a = rng.uniform(0, 0.95, 2000); q = rng.uniform(-0.9, 0.9, 2000)
At = A(a, q)
lines += ["", f"Symmetric family, 2,000 draws a ~ U(0, 0.95), q ~ U(−0.9, 0.9), seed {SEED}: max |TDMI + ln(1 − a²)| = {np.abs(At.sum(1) + np.log(1 - a ** 2)).max():.1e}; "
          f"max |rtr + sts − TDMI| = {np.abs(At[:, IX['rtr']] + At[:, IX['sts']] - At.sum(1)).max():.1e}; max |rtr + ½ ln(1 − a²q²)| = {np.abs(At[:, IX['rtr']] + 0.5 * np.log(1 - (a * q) ** 2)).max():.1e}; "
          f"max |ΦR − rtr| = {np.abs(phir(At) - At[:, IX['rtr']]).max():.1e}"]
ax = rng.uniform(0, 0.95, 2000); ay = rng.uniform(0, 0.95, 2000); q2 = rng.uniform(-0.9, 0.9, 2000)
At2 = atoms_from_corr(ar1_corr(ax, ay, q2)); d = phir(At2) - At2[:, IX["rtr"]]
lines.append(f"Unequal a_x, a_y (2,000 draws, same seed stream): ΦR − rtr min {d.min():+.3f}, max {d.max():+.3f}, mean {d.mean():+.3f}, share |ΦR − rtr| > 0.01: {(np.abs(d) > 0.01).mean():.2f}")
# derivative ratio at the studies' implied r1 for |q| = 0.25 and 0.6
lines += ["", "Ratio |dsts/dr1| / |dsts/dq| at the implied operating points:"]
for r in (0.78, 0.85, 0.93, 0.97):
    row = []
    for qq in (0.25, 0.6):
        dr = (A(r + H, qq)[0, IX["sts"]] - A(r - H, qq)[0, IX["sts"]]) / (2 * H); dq = (A(r, qq + H)[0, IX["sts"]] - A(r, qq - H)[0, IX["sts"]]) / (2 * H)
        row.append(f"|q| = {qq}: {abs(dr) / abs(dq):.1f}")
    lines.append(f"   r1 = {r}: " + "; ".join(row))


def r1_ideal(flo, fhi, tr):
    return (np.sin(2 * np.pi * fhi * tr) - np.sin(2 * np.pi * flo * tr)) / (2 * np.pi * (fhi - flo) * tr)


lines += ["", "Lag-1 autocorrelation of ideal band-passed white noise, r1 = [sin(2π f_hi TR) − sin(2π f_lo TR)] / [2π (f_hi − f_lo) TR]:"]
for name, flo, fhi, tr in (("0.008–0.09 Hz, TR 2 s", 0.008, 0.09, 2), ("0.008–0.09 Hz, TR 0.72 s", 0.008, 0.09, 0.72), ("0.0025–0.05 Hz, TR 2 s", 0.0025, 0.05, 2),
                           ("0.0025–0.05 Hz, TR 3 s", 0.0025, 0.05, 3), ("0.01–0.08 Hz, TR 2 s (this repository)", 0.01, 0.08, 2), ("0.01–0.08 Hz, TR 3 s", 0.01, 0.08, 3), ("0.01–0.1 Hz, TR 3 s", 0.01, 0.1, 3)):
    lines.append(f"   {name}: {r1_ideal(flo, fhi, tr):.3f}")
txt = "\n".join(lines) + "\n"
(REPO / "notes" / "review_results" / "partB" / "family_checks.log").write_text(txt)
print(txt)
