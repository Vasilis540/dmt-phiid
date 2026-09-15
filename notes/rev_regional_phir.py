"""
rev_regional_phir.py — EXPLORATORY regional analysis of ΦR with the machinery of
scripts/11_regional_analysis.py (parcels, proxies, sign-flip, BH FDR, Vasa spin test), applied
to the HRF-deconvolved series (notes/rev_deconv.py) and, for reference, the raw series, on two
estimators: the windowed W = 60 fit (the estimator on which the whole-brain deconvolved ΦR
increase was found) and the global fit with 30-TR bins (11's own estimator).
Pre-specified in notes/prespec_regional_phir_deconv_2026-09-14.md before any number existed.

Per-region ΦR = mean over the 114 pairs containing the region of pair-wise
ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr (the 16 atoms per region are stored, so sts etc. are
available too). Atoms from notes/rev_phiid_fast.py (closed form of phyid's Gaussian-MMI ΦID,
validated to ~1e-14 against the saved phyid outputs by rev_phiid_fast_validate.py).

Usage: .venv/bin/python notes/rev_regional_phir.py [--series deconv|raw] [--variant ts_gsr|ts_demean] [--estimator win60|global]
Outputs (notes/review_results/regional/):
  regional_atoms_<series>_<variant>_<estimator>.npy        (14, 2, n_t, 115, 16)
  regional_phir_did_map_<series>_<variant>_<estimator>.csv per-region DiD map
  regional_phir_<series>_<variant>_<estimator>.csv         all statistics (section,name,value,ci_lo,ci_hi,p,note)
"""
import argparse
import sys
import time
from itertools import product
from pathlib import Path

import h5py
import numpy as np
import scipy.io as sio
from scipy.stats import spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, incidence, phir, ATOMS

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "external" / "DMT_NCT" / "data"
SPIN = REPO / "external" / "DMT_NCT" / "fxns" / "SpinTests" / "rotated_maps" / "rotated_Schaefer_100.mat"
LUT = REPO / "data" / "Schaefer2018_100Parcels_7Networks_order.lut"
RR = REPO / "notes" / "review_results"
OUT = RR / "regional"
OUT.mkdir(parents=True, exist_ok=True)
MAT = "DMT_clean_mni_continuous_fullPreprocsch116.mat"

SEED = 20261120
N_BOOT = 10000
N_SUBJ = 14
N_CORTICAL = 100
EXCLUDE = (20,)
FDR_Q = 0.05
RECEPTORS = ("mean5HT2A_sch116", "mean5HT1A_sch116", "mean5HT1B_sch116", "mean5HT4_sch116", "mean5HTT_sch116")
NETS = ("Vis", "SomMot", "DorsAttn", "SalVentAttn", "Limbic", "Cont", "Default")

ap = argparse.ArgumentParser()
ap.add_argument("--series", default="deconv", choices=("deconv", "raw"))
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean"))
ap.add_argument("--estimator", default="win60", choices=("win60", "global"))
args = ap.parse_args()
TAG = f"{args.series}_{args.variant}_{args.estimator}"
rng = np.random.default_rng(SEED)
t0 = time.time()

if args.estimator == "win60":
    W, N_T = 60, 14
    PRE, POST = np.arange(0, 4), np.arange(5, 14)
    set_note = "pre=windows1-4 post=windows6-14"
else:
    W, N_T = 30, 28
    PRE, POST = np.arange(0, 8), np.arange(10, 28)
    set_note = "pre=bins1-8 post=bins11-28"
HEADER = (f"# rev_regional_phir.py EXPLORATORY series={args.series} variant={args.variant} estimator={args.estimator} "
          f"regions=115 excluded_regions=20 {set_note} signflip=exact2^14 two-sided fdr=BH q={FDR_Q} "
          f"spin=rotated_Schaefer_100 (10000 rotations, cortical only) bootstrap={N_BOOT} seed={SEED}")
print(HEADER)

# ------------------------------------------------------------------ parcels and proxies (verbatim logic of 11)
lut = [l.split() for l in LUT.read_text().strip().splitlines()]
assert len(lut) == N_CORTICAL
cort_names = [l[4].replace("7Networks_", "") for l in lut]
yeo116 = np.array([int(float(x)) for x in (DATA / "sch116_to_yeo.csv").read_text().strip().split(",")])
assert all(NETS.index(n.split("_")[1]) + 1 == yeo116[i] for i, n in enumerate(cort_names))
names116 = cort_names + [f"SUB_{k + 1}" for k in range(116 - N_CORTICAL)]
region_idx = np.array([r for r in range(116) if r not in EXCLUDE])
n_regions = region_idx.size
pos_of = {int(r): k for k, r in enumerate(region_idx)}
is_cortical115 = region_idx < N_CORTICAL
net115 = yeo116[region_idx]


def positions(orig):
    return np.array(sorted(pos_of[int(r)] for r in orig if int(r) in pos_of), int)


def cort_where(pred):
    return [i for i, n in enumerate(cort_names) if pred(n)]


gateway_net = cort_where(lambda n: "_Default_" in n)
broadcaster_net = cort_where(lambda n: "_Cont_" in n)
gateway_named = cort_where(lambda n: "_Default_" in n and ("pCunPCC" in n or "_PFC" in n or "_Par_" in n or n.startswith("LH_Default_Temp")))
broadcaster_named = cort_where(lambda n: "_Cont_PFCl_" in n)
assert (len(gateway_net), len(broadcaster_net), len(gateway_named), len(broadcaster_named)) == (24, 13, 21, 5)
cortical_all = set(range(N_CORTICAL)) - set(EXCLUDE)
subcortical_all = set(range(N_CORTICAL, 116))
PROXIES = {
    "primary_Default+Cont": (set(gateway_net) | set(broadcaster_net), set(gateway_net), set(broadcaster_net)),
    "named_subregion": (set(gateway_named) | set(broadcaster_named), set(gateway_named), set(broadcaster_named)),
}

rows = []


def rec(section, name, value, lo=np.nan, hi=np.nan, p=np.nan, note=""):
    rows.append((section, name, value, lo, hi, p, note))
    ci = "" if np.isnan(lo) else f" [{lo:+.4f}, {hi:+.4f}]"
    ps = "" if np.isnan(p) else f" p={p:.4f}"
    print(f"  {section:28s} {name:48s} {value:+.4f}{ci}{ps}  {note}")


# ------------------------------------------------------------------ 1. per-region atoms
if args.series == "deconv":
    mat = next(p for p in (RR / "deconv" / MAT, REPO.parent / "deconv_run" / "sandbox" / "external" / "DMT_NCT" / "data" / MAT) if p.exists())
else:
    mat = DATA / MAT
ts_all = sio.loadmat(mat)[args.variant]
regional = np.full((N_SUBJ, 2, N_T, n_regions, 16), np.nan)
inc = None
for s, c in product(range(N_SUBJ), range(2)):
    X = np.asarray(ts_all[s, c], float)[region_idx]
    kept = np.where(np.all(np.isfinite(X), axis=0))[0]
    if args.estimator == "win60":
        for w in range(N_T):
            in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
            if in_w.size <= 5:
                continue
            pp = PairPhiID(X[:, in_w])
            inc = incidence(n_regions, pp.pairs) if inc is None else inc
            regional[s, c, w] = (inc @ pp.atoms_mean()) / (n_regions - 1)
    else:
        pp = PairPhiID(X[:, kept])
        inc = incidence(n_regions, pp.pairs) if inc is None else inc
        ab = pp.atoms_bins(kept[:pp.n] // W, N_T)
        for t in range(N_T):
            if np.isfinite(ab[t]).all():
                regional[s, c, t] = (inc @ ab[t]) / (n_regions - 1)
assert np.isfinite(regional).all()
np.save(OUT / f"regional_atoms_{TAG}.npy", regional)
print(f"per-region atoms computed ({time.time() - t0:.0f}s)")

# internal consistency: mean over regions == saved whole-brain pair mean
saved = {("deconv", "win60"): RR / "deconv" / f"atoms_win60_115regions-all_{args.variant}_window.npy",
         ("deconv", "global"): RR / "deconv" / f"atoms_bins_115regions-all_{args.variant}_global.npy",
         ("raw", "win60"): REPO / "results" / f"atoms_win60_115regions-all_{args.variant}_window.npy",
         ("raw", "global"): REPO / "results" / f"atoms_bins_115regions-all_{args.variant}_global.npy"}[(args.series, args.estimator)]
wb = np.load(saved)
d_all = np.nanmax(np.abs(regional.mean(-2) - wb))
rec("consistency", "max_abs_diff_region_mean_vs_saved_pair_mean_16atoms", d_all, note=saved.name)
assert d_all < 1e-8

# ------------------------------------------------------------------ 2. per-region ΦR DiD
PHIR = phir(regional)                                            # (14, 2, n_t, 115)
change = PHIR[:, :, POST].mean(2) - PHIR[:, :, PRE].mean(2)      # (14, 2, 115)
did = change[:, 0] - change[:, 1]                                # (14, 115)
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))


def signflip_p(v):
    v = np.asarray(v, float)
    return float(np.mean(np.abs(_SIGNS @ v) / v.size >= abs(v.mean()) - 1e-12))


def boot_ci(v):
    v = np.asarray(v, float)
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def bh(pvals, q):
    p = np.asarray(pvals, float)
    m = p.size
    order = np.argsort(p)
    thresh = q * (np.arange(1, m + 1) / m)
    passed = p[order] <= thresh
    k = np.max(np.where(passed)[0]) + 1 if passed.any() else 0
    sig = np.zeros(m, bool)
    sig[order[:k]] = True
    return sig, (thresh[k - 1] if k else 0.0)


did_mean = did.mean(0)
did_p = np.array([signflip_p(did[:, r]) for r in range(n_regions)])
sig, p_thresh = bh(did_p, FDR_Q)
print(f"\n== per-region ΦR DiD (EXPLORATORY): {sig.sum()} of 115 survive BH FDR q={FDR_Q} (p threshold {p_thresh:.5f}); "
      f"of these {int((did_mean[sig] > 0).sum())} positive, {int((did_mean[sig] < 0).sum())} negative; group-mean DiD positive in {int((did_mean > 0).sum())}/115 regions")
rec("regional_did", "whole_brain_did_mean_over_regions", did_mean.mean(), *boot_ci(did.mean(1)), signflip_p(did.mean(1)), note="equals whole-brain pair-mean ΦR DiD")
rec("regional_did", "n_regions_fdr_significant", float(sig.sum()), note=f"BH q={FDR_Q}, p_thresh={p_thresh:.5f}")
rec("regional_did", "n_fdr_significant_positive", float((did_mean[sig] > 0).sum()))
rec("regional_did", "n_fdr_significant_negative", float((did_mean[sig] < 0).sum()))
rec("regional_did", "n_groupmean_positive_of_115", float((did_mean > 0).sum()))
rec("regional_did", "n_uncorrected_p_below_0.05", float((did_p < 0.05).sum()))
rec("regional_did", "min_uncorrected_p", did_p.min(), note=f"region {names116[region_idx[did_p.argmin()]]} did={did_mean[did_p.argmin()]:+.4f}")
rec("regional_did", "n_cortical_fdr_significant", float(sig[is_cortical115].sum()))
rec("regional_did", "n_subcortical_fdr_significant", float(sig[~is_cortical115].sum()))
rec("regional_did", "sd_of_groupmean_did_across_regions", did_mean.std(ddof=1))
rec("regional_did", "range_of_groupmean_did_across_regions", did_mean.max() - did_mean.min(), note=f"min {did_mean.min():+.4f} max {did_mean.max():+.4f}")
for n_i, n_name in enumerate(NETS + ("Subcortex",), start=1):
    m = net115 == n_i
    v = did[:, m].mean(1)
    lo, hi = boot_ci(v)
    rec("network_mean_did", f"{n_name}_n{int(m.sum())}", v.mean(), lo, hi, signflip_p(v), note=f"pos={int((v > 0).sum())}/14; fdr_sig={int(sig[m].sum())}")
with open(OUT / f"regional_phir_did_map_{TAG}.csv", "w") as f:
    f.write(HEADER + "\n")
    f.write("orig_index,name,yeo_network,did_mean,did_sd,p_signflip,bh_significant,n_pos_of_14,dmt_change,pcb_change,pre_level_dmt\n")
    for k in range(n_regions):
        f.write(f"{region_idx[k]},{names116[region_idx[k]]},{net115[k]},{did_mean[k]:.6f},{did[:, k].std(ddof=1):.6f},{did_p[k]:.8f},"
                f"{int(sig[k])},{int((did[:, k] > 0).sum())},{change[:, 0, k].mean():.6f},{change[:, 1, k].mean():.6f},{PHIR[:, 0, PRE, k].mean():.6f}\n")
for k in np.where(sig)[0]:
    rec("regional_did_fdr_regions", names116[region_idx[k]], did_mean[k], p=did_p[k], note=f"orig_index={region_idx[k]} net={net115[k]} pos={int((did[:, k] > 0).sum())}/14")

# ------------------------------------------------------------------ 3. receptor maps and spin test (as 11)
rec_mat = sio.loadmat(DATA / "5HTvecs_sch116.mat")
receptor = {k: rec_mat[k].ravel().astype(float) for k in RECEPTORS}
with h5py.File(SPIN, "r") as f:
    perm_id = f["perm_id"][()]
if perm_id.shape[0] != N_CORTICAL:
    perm_id = perm_id.T
perm_id = perm_id.astype(int) - int(perm_id.min())
n_rot = perm_id.shape[1]
assert perm_id.shape == (N_CORTICAL, n_rot)


def cortical_vector(v115):
    out = np.full(N_CORTICAL, np.nan)
    for k in range(n_regions):
        if is_cortical115[k]:
            out[region_idx[k]] = v115[k]
    return out


def sp(a, b):
    ok = np.isfinite(a) & np.isfinite(b)
    return spearmanr(a[ok], b[ok])[0]


def spin_test(x100, y100):
    rho = sp(x100, y100)
    null_xy = np.array([sp(x100[perm_id[:, r]], y100) for r in range(n_rot)])
    null_yx = np.array([sp(y100[perm_id[:, r]], x100) for r in range(n_rot)])
    if rho > 0:
        p_vasa = 0.5 * (np.mean(null_xy > rho) + np.mean(null_yx > rho))
    else:
        p_vasa = 0.5 * (np.mean(null_xy < rho) + np.mean(null_yx < rho))
    p_two = 0.5 * (np.mean(np.abs(null_xy) >= abs(rho)) + np.mean(np.abs(null_yx) >= abs(rho)))
    return rho, p_vasa, p_two, np.concatenate([null_xy, null_yx]).std()


print(f"\n== spin test: {n_rot} rotations of the 100 cortical parcels ({time.time() - t0:.0f}s)")
did_cort = cortical_vector(did_mean)
spin_rows = []
for key in RECEPTORS:
    rmap115 = receptor[key][region_idx]
    rho_all = spearmanr(did_mean, rmap115)[0]
    rho_c, p_vasa, p_two, null_sd = spin_test(did_cort, cortical_vector(rmap115))
    spin_rows.append((key, rho_c, p_vasa, p_two, rho_all, null_sd))
sig5, thr5 = bh(np.array([r[3] for r in spin_rows]), FDR_Q)
for (key, rho_c, p_vasa, p_two, rho_all, null_sd), s5 in zip(spin_rows, sig5):
    short = key.replace("mean", "").replace("_sch116", "")
    rec("spatial_spin_cortical99", f"rho_{short}", rho_c, p=p_two, note=f"two-sided spin p; Vasa one-sided-avg p={p_vasa:.4f}; null SD {null_sd:.3f}; BH(5) sig={int(s5)}")
    rec("spatial_descriptive_115", f"rho_{short}_incl_subcortex_no_p", rho_all, note="no spatial null for subcortex")
rec("spatial_spin_cortical99", "bh_threshold_across_5_maps", thr5)

# ------------------------------------------------------------------ 4. workspace comparison (as 11)
print("\n== workspace comparison (network-level proxies of Luppi et al. 2024; EXPLORATORY)")


def set_mean(per_subject_map, orig_set):
    return per_subject_map[:, positions(orig_set)].mean(1)


for label, (ws, gw, bc) in PROXIES.items():
    non_cort = cortical_all - ws
    for non_label, non in (("vs_noncortex_ws", non_cort), ("vs_noncortex_ws+subcortex", non_cort | subcortical_all)):
        ws_m, non_m = set_mean(did, ws), set_mean(did, non)
        d = ws_m - non_m
        lo, hi = boot_ci(d)
        rec(f"workspace_{label}", f"workspace_minus_nonworkspace_{non_label}", d.mean(), lo, hi, signflip_p(d), note=f"n_ws={len(ws)} n_non={len(non)} pos={int((d > 0).sum())}/14")
        lo, hi = boot_ci(ws_m); rec(f"workspace_{label}", f"workspace_mean_did_{non_label}", ws_m.mean(), lo, hi, signflip_p(ws_m), note=f"pos={int((ws_m > 0).sum())}/14")
        lo, hi = boot_ci(non_m); rec(f"workspace_{label}", f"nonworkspace_mean_did_{non_label}", non_m.mean(), lo, hi, signflip_p(non_m), note=f"pos={int((non_m > 0).sum())}/14")
        for sub_label, sub in (("gateway_proxy", gw), ("broadcaster_proxy", bc)):
            d2 = set_mean(did, sub) - non_m
            lo, hi = boot_ci(d2)
            rec(f"workspace_{label}", f"{sub_label}_minus_nonworkspace_{non_label}", d2.mean(), lo, hi, signflip_p(d2), note=f"n={len(sub)} pos={int((d2 > 0).sum())}/14")
    d3 = set_mean(did, gw) - set_mean(did, bc)
    lo, hi = boot_ci(d3)
    rec(f"workspace_{label}", "gateway_proxy_minus_broadcaster_proxy", d3.mean(), lo, hi, signflip_p(d3), note=f"n_gw={len(gw)} n_bc={len(bc)}")
    # the two runs separately, to see what the proxy difference is made of
    for c, cn in enumerate(("dmt", "pcb")):
        dc = set_mean(change[:, c], ws) - set_mean(change[:, c], non_cort)
        lo, hi = boot_ci(dc)
        rec(f"workspace_{label}", f"{cn}_change_workspace_minus_nonworkspace_cortex", dc.mean(), lo, hi, signflip_p(dc))

# ------------------------------------------------------------------ write
out = OUT / f"regional_phir_{TAG}.csv"
with open(out, "w") as f:
    f.write(HEADER + "\n")
    f.write("section,name,value,ci_lo,ci_hi,p,note\n")
    for section, name, value, lo, hi, p, note in rows:
        f.write(f"{section},{name},{value:.6f},{'' if np.isnan(lo) else f'{lo:.6f}'},{'' if np.isnan(hi) else f'{hi:.6f}'},{'' if np.isnan(p) else f'{p:.8f}'},\"{note}\"\n")
print(f"\nwrote {out} ({time.time() - t0:.0f}s)")
