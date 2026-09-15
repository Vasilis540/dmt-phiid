"""
review_checks.py — every computation quoted in notes/adversarial_review_2026-09-14.md
that is not already in results/*.csv. Run from the repository root with the project
venv (needs phyid for the CCS block; everything else reads saved arrays only):

    .venv/bin/python notes/review_checks.py            # all blocks (~3 min)
    .venv/bin/python notes/review_checks.py --no-ccs   # skip the phyid recomputation

Nothing here writes to results/.
"""
import argparse
import itertools
import sys
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy import stats

ATOMS = "rtr,rtx,rty,rts,xtr,xtx,xty,xts,ytr,ytx,yty,yts,str,stx,sty,sts".split(",")
IX = {n: i for i, n in enumerate(ATOMS)}
R = Path("results")
DATA = Path("external/DMT_NCT/data")
SIGNS = np.array(list(itertools.product([1, -1], repeat=14)))


def signflip_p(v):
    v = np.asarray(v, float)
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= abs(v.mean()) - 1e-12))


def did(x, pre, post):
    ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
    return ch[:, 0] - ch[:, 1]


def phi_r(A):
    """Revised integrated information (Mediano et al. 2021): TDMI - I(X;X') - I(Y;Y') + rtr,
    with I(X;X') = rtr+rtx+xtr+xtx and I(Y;Y') = rtr+rty+ytr+yty on the phyid lattice."""
    ixx = A[..., IX["rtr"]] + A[..., IX["rtx"]] + A[..., IX["xtr"]] + A[..., IX["xtx"]]
    iyy = A[..., IX["rtr"]] + A[..., IX["rty"]] + A[..., IX["ytr"]] + A[..., IX["yty"]]
    return A.sum(-1) - ixx - iyy + A[..., IX["rtr"]]


def block(title):
    print("\n" + "=" * 78 + f"\n{title}\n" + "=" * 78)


# ------------------------------------------------------------------ 1. all 16 atoms
block("1. All 16 atoms: baseline level and DiD (the draft's Table 2 shows 6 of them)")
cells = [("windowed W60", "ts_gsr", "atoms_win60_115regions-all_ts_gsr_window.npy", np.arange(0, 4), np.arange(5, 14)),
         ("windowed W60", "ts_demean", "atoms_win60_115regions-all_ts_demean_window.npy", np.arange(0, 4), np.arange(5, 14)),
         ("global fit", "ts_gsr", "atoms_bins_115regions-all_ts_gsr_global.npy", np.arange(0, 8), np.arange(10, 28)),
         ("global fit", "ts_demean", "atoms_bins_115regions-all_ts_demean_global.npy", np.arange(0, 8), np.arange(10, 28))]
for est, var, f, pre, post in cells:
    A = np.load(R / f)
    lvl = np.nanmean(A[:, 0, pre, :], axis=(0, 1))
    d = np.array([did(A[..., a], pre, post).mean() for a in range(16)])
    syn_block = [IX[n] for n in ("sts", "rts", "str", "xts", "yts", "stx", "sty")]
    print(f"\n[{est}, {var}]  DMT pre-injection whole-brain means:")
    print("   " + "  ".join(f"{n}={lvl[i]:+.3f}" for i, n in enumerate(ATOMS)))
    print("   DiD per atom:")
    print("   " + "  ".join(f"{n}={d[i]:+.4f}" for i, n in enumerate(ATOMS)))
    print(f"   TDMI DiD {d.sum():+.4f} | sts+rts+str+xts+yts+stx+sty {d[syn_block].sum():+.4f} | "
          f"xtx+yty {d[IX['xtx']] + d[IX['yty']]:+.4f} | rtr {d[IX['rtr']]:+.4f}")
    for lab, X in (("PhiR", phi_r(A)), ("xtx+yty", A[..., IX["xtx"]] + A[..., IX["yty"]])):
        v = did(X, pre, post)
        print(f"   {lab:8s} level {np.nanmean(X[:, 0, pre]):+.4f}  DiD {v.mean():+.4f}  p={signflip_p(v):.4f}  negative {(v < 0).sum()}/14")

# ------------------------------------------------------------------ 2. placebo group-mean-series rho
block("2. The thresholded tracking statistic (group-mean-series rho vs template) on the PLACEBO run")
ratings = sio.loadmat(DATA / "intensity_ratings.mat")["dmt_intensity"].astype(float)
tmpl = ratings.mean(0) / ratings.mean(0).max()
tw = tmpl.reshape(14, 2).mean(1)
for var in ("ts_gsr", "ts_demean"):
    sts = np.load(R / f"atoms_win60_115regions-all_{var}_window.npy")[..., IX["sts"]]
    gm = sts.mean(0)
    for lab, w in (("6-14", slice(5, 14)), ("5-14", slice(4, 14))):
        rd = stats.spearmanr(gm[0, w], tw[w]).statistic
        rp = stats.spearmanr(gm[1, w], tw[w]).statistic
        rt = stats.spearmanr(gm[1, w], np.arange(14)[w]).statistic
        print(f"   {var:10s} windows {lab}: DMT {rd:+.4f}  PLACEBO {rp:+.4f}  (placebo vs plain time index {rt:+.4f})")

# ------------------------------------------------------------------ 3. early vs late post windows
block("3. Where the DiD comes from: drug-present windows 6-9 vs tail windows 10-14 (W60)")
for var in ("ts_gsr", "ts_demean"):
    sts = np.load(R / f"atoms_win60_115regions-all_{var}_window.npy")[..., IX["sts"]]
    pre = np.arange(0, 4)
    for lab, post in (("6-14", np.arange(5, 14)), ("6-9", np.arange(5, 9)), ("10-14", np.arange(9, 14))):
        d = did(sts, pre, post)
        dm = (sts[:, 0, post].mean(1) - sts[:, 0, pre].mean(1)).mean()
        pc = (sts[:, 1, post].mean(1) - sts[:, 1, pre].mean(1)).mean()
        print(f"   {var:10s} post {lab:6s} DiD {d.mean():+.4f} p={signflip_p(d):.4f} neg {(d < 0).sum()}/14 | "
              f"DMT {dm:+.4f} PCB {pc:+.4f} | placebo share {pc / -d.mean():.2f}")
    d3 = did(sts, np.arange(0, 3), np.arange(5, 14))
    print(f"   {var:10s} baseline windows 1-3 (bin 8 dropped), post 6-14: DiD {d3.mean():+.4f} p={signflip_p(d3):.4f}")

# ------------------------------------------------------------------ 4. lag-1 autocorrelation
block("4. Mean regional lag-1 autocorrelation per 60-TR window vs the sts contrast (ts_gsr)")
ts = sio.loadmat(DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat")["ts_gsr"]
regs = [r for r in range(116) if r != 20]
ac = np.full((14, 2, 14), np.nan)
for s in range(14):
    for c in range(2):
        X = ts[s, c][regs]
        for w in range(14):
            seg = X[:, w * 60:(w + 1) * 60]
            seg = seg[:, np.all(np.isfinite(seg), axis=0)]
            ac[s, c, w] = np.mean([np.corrcoef(seg[i, :-1], seg[i, 1:])[0, 1] for i in range(len(regs))])
W = np.load(R / "atoms_win60_115regions-all_ts_gsr_window.npy")
pre, post = np.arange(0, 4), np.arange(5, 14)
d_ac, d_sts = did(ac, pre, post), did(W[..., IX["sts"]], pre, post)
print(f"   lag-1 autocorr: DMT pre {ac[:, 0, pre].mean():.4f} post {ac[:, 0, post].mean():.4f}; "
      f"PCB pre {ac[:, 1, pre].mean():.4f} post {ac[:, 1, post].mean():.4f}")
print(f"   DiD {d_ac.mean():+.4f} p={signflip_p(d_ac):.4f} negative {(d_ac < 0).sum()}/14")
print(f"   per-subject r(autocorr DiD, sts DiD) = {stats.pearsonr(d_ac, d_sts)[0]:.3f}; "
      f"across 28 condition x window group means r = {stats.pearsonr(ac.mean(0).ravel(), W[..., IX['sts']].mean(0).ravel())[0]:.3f}")

# ------------------------------------------------------------------ 5. global vs windowed per subject
block("5. How independent was the 'pre-specified' windowed test of the global-fit result already in hand?")
G = np.load(R / "atoms_bins_115regions-all_ts_gsr_global.npy")[..., IX["sts"]]
dg = did(G, np.arange(0, 8), np.arange(10, 28))
print(f"   per-subject r(global-fit DiD, windowed DiD) = {stats.pearsonr(dg, d_sts)[0]:.3f}")
import pandas as pd
d20 = pd.read_csv(R / "synergy_bins_20regions_ts_gsr_global.csv", comment="#")
pv = d20.pivot_table(index=["subject", "condition"], columns="bin", values="synergy_mean")
v20 = np.array([(pv.loc[(s, "DMT")][10:28].mean() - pv.loc[(s, "DMT")][0:8].mean())
                - (pv.loc[(s, "PCB")][10:28].mean() - pv.loc[(s, "PCB")][0:8].mean()) for s in range(14)])
print(f"   20-region sanity run (written 12 Sep 10:12, git=nogit): DiD {v20.mean():+.4f}, negative {(v20 < 0).sum()}/14, "
      f"p={signflip_p(v20):.4f}; r with the primary windowed DiD = {stats.pearsonr(v20, d_sts)[0]:.3f}")

# ------------------------------------------------------------------ 6. Robustness C offset
block("6. Robustness C: the pre-drug offset inside contrast (ii)")
rc = pd.read_csv(R / "robustness_c_ts_gsr.csv", comment="#")
row_i = rc[(rc.estimator == "placebo-fitted") & rc.contrast.str.startswith("(i) within-DMT step, primary") & (rc.atom == "sts")].iloc[0]
row_ii = rc[(rc.estimator == "placebo-fitted") & rc.contrast.str.startswith("(ii)") & (rc.atom == "sts")].iloc[0]
print(f"   DMT pre-injection (bins 1-8) under the placebo-fitted model: {row_i.level_b:.4f}")
print(f"   PCB held-out half (bins 15-28) under the same model:        {row_ii.level_b:.4f}   -> pre-drug offset {row_i.level_b - row_ii.level_b:+.4f}")
print(f"   contrast (ii) DMT - PCB bins 15-28: {row_ii.diff_mean:+.4f} (p={row_ii.p_signflip:.4f});  "
      f"contrast (i) within-DMT step: {row_i.diff_mean:+.4f} [{row_i.ci_lo:+.4f}, {row_i.ci_hi:+.4f}] p={row_i.p_signflip:.4f}")

# ------------------------------------------------------------------ 7. MMI vs CCS
ap = argparse.ArgumentParser()
ap.add_argument("--no-ccs", action="store_true")
if not ap.parse_args().no_ccs:
    block("7. Redundancy-function dependence: MMI vs CCS on 400 random pairs, global fit (about 2 min)")
    from phyid.calculate import calc_PhiID
    rng = np.random.default_rng(20261120)
    allpairs = list(itertools.combinations(regs, 2))
    sel = [allpairs[k] for k in rng.choice(len(allpairs), 400, replace=False)]
    pre_tr, post_tr = np.arange(0, 240), np.arange(300, 840)
    for var in ("ts_gsr", "ts_demean"):
        tsv = sio.loadmat(DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat")[var]
        for red in ("MMI", "CCS"):
            res = np.zeros((14, 2, 2, 16))
            for s in range(14):
                for c in range(2):
                    X = tsv[s, c]
                    keep = np.where(np.all(np.isfinite(X), axis=0))[0]
                    X = X[:, keep]
                    acc = np.zeros((16, X.shape[1] - 1))
                    for i, j in sel:
                        a, _ = calc_PhiID(X[i], X[j], tau=1, kind="gaussian", redundancy=red)
                        for k, n in enumerate(ATOMS):
                            acc[k] += a[n]
                    acc /= len(sel)
                    tr = keep[:-1]
                    res[s, c, 0] = acc[:, np.isin(tr, pre_tr)].mean(1)
                    res[s, c, 1] = acc[:, np.isin(tr, post_tr)].mean(1)
            ch = res[:, :, 1, :] - res[:, :, 0, :]
            dd = ch[:, 0, :] - ch[:, 1, :]
            m = dd.mean(0)
            print(f"   {var:10s} {red}: sts baseline {res[:, 0, 0, IX['sts']].mean():+.3f}; sts DiD {m[IX['sts']]:+.4f} "
                  f"(negative {(dd[:, IX['sts']] < 0).sum()}/14, p={signflip_p(dd[:, IX['sts']]):.4f}); "
                  f"xtx+yty DiD {m[IX['xtx']] + m[IX['yty']]:+.4f}; TDMI DiD {m.sum():+.4f}")
print("\ndone")
