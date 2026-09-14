#!/usr/bin/env python3
"""
11_regional_analysis.py — EXPLORATORY regional analysis (manuscript/analysis_record.md,
"Exploratory: regional analysis", pre-specified 13 Sep 2026 before this file
was written). Not pre-registered before the primary result existed; every
part is reported regardless of outcome. No predictions.

Steps, exactly as recorded:
  1. Robustness A global fit per pair (same code path and settings as
     01_synergy_timecourse.py: calc_PhiID gaussian/MMI/tau=1, one fit per
     pair per run, non-finite TRs dropped, region 20 excluded -> 115 regions,
     6,555 pairs). Per-region sts and rtr = mean over the 114 pairs containing
     the region, per 30-TR bin, subject, condition. Internal check: the mean
     over regions equals the saved whole-brain pair mean.
  2. Per-region DiD = (post bins 11-28 - pre bins 1-8)_DMT - (same)_PCB;
     exact sign-flip across 14 subjects (2^14), two-sided; Benjamini-Hochberg
     FDR q = 0.05 across 115 regions.
  3. Spatial correlation of the group-mean DiD map with 5-HT2A: Spearman;
     spin test on the 99 cortical parcels using the Vasa rotations in
     external/DMT_NCT/fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat
     (10,000 rotations, both directions, NaN-complete rows); subcortex cannot
     be spun, so the 115-region rho is descriptive only. Same test against
     5-HT1A, 5-HT1B, 5-HT4, 5-HTT; BH FDR across the five.
  4. Workspace comparison (Luppi et al. eLife 2024) via the network-level
     proxies fixed in manuscript/analysis_record.md: primary = Yeo Default (gateway proxy) +
     Control (broadcaster proxy); named-subregion proxy as sensitivity;
     non-workspace = remaining cortical parcels (subcortex added as a
     sensitivity). Per subject: mean DiD(workspace) - mean DiD(non-workspace);
     sign-flip test; subject-bootstrap CI.
  5. Descriptive rank-rule check on the placebo run (synergy strength rank >
     redundancy strength rank), overlap with the proxy. No test, no selection.

Usage: python3 scripts/11_regional_analysis.py --variant ts_gsr|ts_demean
Outputs: results/regional_atoms_bins_115regions-all_<variant>_global.npy
         results/regional_did_map_<variant>.csv
         results/regional_analysis_<variant>.csv
"""
import argparse
import subprocess
import time
from itertools import combinations, product
from pathlib import Path

import h5py
import numpy as np
import scipy.io as sio
from scipy.stats import rankdata, spearmanr

from phyid.calculate import calc_PhiID
from phyid.utils import PhiID_atoms_abbr

# ------------------------------------------------------------------ constants
SEED = 20261120
N_BOOT = 10000
TAU = 1
KIND = "gaussian"
REDUNDANCY = "MMI"
EXCLUDE_REGIONS = (20,)
N_SUBJ = 14
N_BINS = 28
TRS_PER_BIN = 30
N_CORTICAL = 100
CONDITIONS = ("DMT", "PCB")
ATOMS = tuple(PhiID_atoms_abbr)
STS = ATOMS.index("sts")
RTR = ATOMS.index("rtr")
PRE = np.arange(0, 8)          # bins 1-8
POST = np.arange(10, 28)       # bins 11-28
FDR_Q = 0.05
RECEPTORS = ("mean5HT2A_sch116", "mean5HT1A_sch116", "mean5HT1B_sch116",
             "mean5HT4_sch116", "mean5HTT_sch116")
NETS = ("Vis", "SomMot", "DorsAttn", "SalVentAttn", "Limbic", "Cont", "Default")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean"))
args = ap.parse_args()
V = args.variant

DATA = Path("external/DMT_NCT/data")
SPIN = Path("external/DMT_NCT/fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat")
LUT = Path("data/Schaefer2018_100Parcels_7Networks_order.lut")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)
rng = np.random.default_rng(SEED)
try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"
HEADER = (f"# 11_regional_analysis.py EXPLORATORY variant={V} regions=115 excluded_regions=20 "
          f"pre=bins1-8 post=bins11-28 signflip=exact2^14 two-sided fdr=BH q={FDR_Q} "
          f"spin=rotated_Schaefer_100 (10000 rotations, cortical only) bootstrap={N_BOOT} seed={SEED} git={sha}")
print(HEADER)

rows = []   # (section, name, value, ci_lo, ci_hi, p, note)


def rec(section, name, value, lo=np.nan, hi=np.nan, p=np.nan, note=""):
    rows.append((section, name, value, lo, hi, p, note))
    ci = "" if np.isnan(lo) else f" [{lo:+.4f}, {hi:+.4f}]"
    ps = "" if np.isnan(p) else f" p={p:.4f}"
    print(f"  {section:26s} {name:44s} {value:+.4f}{ci}{ps}  {note}")


# ------------------------------------------------------------------ parcels
lut = [l.split() for l in LUT.read_text().strip().splitlines()]
assert len(lut) == N_CORTICAL
cort_names = [l[4].replace("7Networks_", "") for l in lut]
yeo116 = np.array([int(float(x)) for x in (DATA / "sch116_to_yeo.csv").read_text().strip().split(",")])
assert yeo116.shape == (116,)
assert all(NETS.index(n.split("_")[1]) + 1 == yeo116[i] for i, n in enumerate(cort_names)), "LUT order != sch116_to_yeo"
assert (yeo116[N_CORTICAL:] == 8).all()
names116 = cort_names + [f"SUB_{k + 1}" for k in range(116 - N_CORTICAL)]
region_idx = np.array([r for r in range(116) if r not in EXCLUDE_REGIONS])      # 115 original indices
n_regions = region_idx.size
pairs = list(combinations(range(n_regions), 2))
n_pairs = len(pairs)
assert n_regions == 115 and n_pairs == 6555
pos_of = {int(r): k for k, r in enumerate(region_idx)}     # original index -> position in 115 arrays
is_cortical115 = region_idx < N_CORTICAL                    # 99 True
net115 = yeo116[region_idx]


def positions(orig_indices):
    return np.array(sorted(pos_of[int(r)] for r in orig_indices if int(r) in pos_of), int)


# workspace proxies (manuscript/analysis_record.md), in original 0-99 indices, then positions
def cort_where(pred):
    return [i for i, n in enumerate(cort_names) if pred(n)]


gateway_net = cort_where(lambda n: "_Default_" in n)                       # 24
broadcaster_net = cort_where(lambda n: "_Cont_" in n)                      # 13
gateway_named = cort_where(lambda n: "_Default_" in n and (
    "pCunPCC" in n or "_PFC" in n or "_Par_" in n or n.startswith("LH_Default_Temp")))   # 21
broadcaster_named = cort_where(lambda n: "_Cont_PFCl_" in n)               # 5
assert (len(gateway_net), len(broadcaster_net), len(gateway_named), len(broadcaster_named)) == (24, 13, 21, 5), \
    (len(gateway_net), len(broadcaster_net), len(gateway_named), len(broadcaster_named))
cortical_all = set(range(N_CORTICAL)) - set(EXCLUDE_REGIONS)
subcortical_all = set(range(N_CORTICAL, 116))
PROXIES = {
    "primary_Default+Cont": (set(gateway_net) | set(broadcaster_net), set(gateway_net), set(broadcaster_net)),
    "named_subregion": (set(gateway_named) | set(broadcaster_named), set(gateway_named), set(broadcaster_named)),
}

# ------------------------------------------------------------------ 1. per-region atoms
ts_all = sio.loadmat(DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat")[V]
assert ts_all.shape == (N_SUBJ, 2)


def finite_trs(X):
    return np.where(np.all(np.isfinite(X), axis=0))[0]


regional = np.full((N_SUBJ, 2, N_BINS, n_regions, 2), np.nan)     # (..., region, [sts, rtr])
t0 = time.time()
for s, c in product(range(N_SUBJ), range(2)):
    X = ts_all[s, c][region_idx, :]
    kept = finite_trs(X)
    n_samples = kept.size - TAU
    acc = np.zeros((n_regions, 2, n_samples))
    for i, j in pairs:
        atoms, _ = calc_PhiID(X[i, kept], X[j, kept], tau=TAU, kind=KIND, redundancy=REDUNDANCY)
        a_sts = np.asarray(atoms["sts"])
        a_rtr = np.asarray(atoms["rtr"])
        acc[i, 0] += a_sts; acc[j, 0] += a_sts
        acc[i, 1] += a_rtr; acc[j, 1] += a_rtr
    acc /= (n_regions - 1)
    slot = kept[:n_samples] // TRS_PER_BIN
    for t in range(N_BINS):
        m = slot == t
        if m.any():
            regional[s, c, t] = acc[:, :, m].mean(axis=2)
    print(f"  subject {s + 1:2d} {CONDITIONS[c]} done ({time.time() - t0:.0f}s)")
assert np.isfinite(regional).all()
np.save(RESULTS / f"regional_atoms_bins_115regions-all_{V}_global.npy", regional)

# internal consistency: mean over regions == saved whole-brain pair mean
saved = RESULTS / f"atoms_bins_115regions-all_{V}_global.npy"
if saved.exists():
    wb = np.load(saved)
    d_sts = np.nanmax(np.abs(regional[..., 0].mean(-1) - wb[..., STS]))
    d_rtr = np.nanmax(np.abs(regional[..., 1].mean(-1) - wb[..., RTR]))
    print(f"consistency vs {saved.name}: max |region-mean - pair-mean| sts {d_sts:.2e} rtr {d_rtr:.2e}")
    rec("consistency", "max_abs_diff_sts_vs_saved_pairmean", d_sts)
    rec("consistency", "max_abs_diff_rtr_vs_saved_pairmean", d_rtr)
    assert d_sts < 1e-8 and d_rtr < 1e-8

# ------------------------------------------------------------------ 2. per-region DiD
sts = regional[..., 0]                                        # (14, 2, 28, 115)
change = sts[:, :, POST].mean(2) - sts[:, :, PRE].mean(2)     # (14, 2, 115)
did = change[:, 0] - change[:, 1]                             # (14, 115)
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))      # (16384, 14)


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
print(f"\n== per-region DiD (EXPLORATORY): {sig.sum()} of 115 survive BH FDR q={FDR_Q} "
      f"(p threshold {p_thresh:.5f}); of these {int((did_mean[sig] < 0).sum())} negative, "
      f"{int((did_mean[sig] > 0).sum())} positive; group-mean DiD negative in {int((did_mean < 0).sum())}/115 regions")
rec("regional_did", "n_regions_fdr_significant", float(sig.sum()), note=f"BH q={FDR_Q}, p_thresh={p_thresh:.5f}")
rec("regional_did", "n_fdr_significant_negative", float((did_mean[sig] < 0).sum()))
rec("regional_did", "n_fdr_significant_positive", float((did_mean[sig] > 0).sum()))
rec("regional_did", "n_groupmean_negative_of_115", float((did_mean < 0).sum()))
rec("regional_did", "min_uncorrected_p", did_p.min(), note=f"region {names116[region_idx[did_p.argmin()]]}")
rec("regional_did", "mean_over_regions_of_did", did_mean.mean(), note="equals whole-brain pair-mean DiD")
rec("regional_did", "n_cortical_fdr_significant", float(sig[is_cortical115].sum()))
rec("regional_did", "n_subcortical_fdr_significant", float(sig[~is_cortical115].sum()))
with open(RESULTS / f"regional_did_map_{V}.csv", "w") as f:
    f.write(HEADER + "\n")
    f.write("orig_index,name,yeo_network,did_mean,did_sd,p_signflip,bh_significant,n_neg_of_14\n")
    for k in range(n_regions):
        f.write(f"{region_idx[k]},{names116[region_idx[k]]},{net115[k]},{did_mean[k]:.6f},{did[:, k].std(ddof=1):.6f},"
                f"{did_p[k]:.5f},{int(sig[k])},{int((did[:, k] < 0).sum())}\n")
for k in np.where(sig)[0]:
    rec("regional_did_fdr_regions", names116[region_idx[k]], did_mean[k], p=did_p[k],
        note=f"orig_index={region_idx[k]} net={net115[k]} neg={int((did[:, k] < 0).sum())}/14")

# ------------------------------------------------------------------ 3. receptor maps and spin test
rec_mat = sio.loadmat(DATA / "5HTvecs_sch116.mat")
receptor = {k: rec_mat[k].ravel().astype(float) for k in RECEPTORS}
with h5py.File(SPIN, "r") as f:
    perm_id = f["perm_id"][()]
if perm_id.shape[0] != N_CORTICAL:
    perm_id = perm_id.T
perm_id = perm_id.astype(int) - int(perm_id.min())          # (100, n_rot), zero-based
n_rot = perm_id.shape[1]
assert perm_id.shape == (N_CORTICAL, n_rot) and all(len(np.unique(perm_id[:, j])) == N_CORTICAL for j in range(0, n_rot, 997))
print(f"\n== spin test: {n_rot} rotations of the 100 cortical parcels; region 20 NaN in both maps")


def cortical_vector(v115):
    """115-position vector -> 100 cortical positions with NaN at excluded parcels."""
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
    return rho, p_vasa, p_two, null_xy, null_yx


did_cort = cortical_vector(did_mean)
spin_rows = []
for key in RECEPTORS:
    rmap115 = receptor[key][region_idx]
    rho_all = spearmanr(did_mean, rmap115)[0]
    rho_c, p_vasa, p_two, nxy, nyx = spin_test(did_cort, cortical_vector(rmap115))
    spin_rows.append((key, rho_c, p_vasa, p_two, rho_all, np.concatenate([nxy, nyx]).std()))
p_two_all = np.array([r[3] for r in spin_rows])
sig5, thr5 = bh(p_two_all, FDR_Q)
for (key, rho_c, p_vasa, p_two, rho_all, null_sd), s5 in zip(spin_rows, sig5):
    short = key.replace("mean", "").replace("_sch116", "")
    rec("spatial_spin_cortical99", f"rho_{short}", rho_c, p=p_two,
        note=f"two-sided spin p; Vasa one-sided-avg p={p_vasa:.4f}; null SD {null_sd:.3f}; BH(5) sig={int(s5)}")
    rec("spatial_descriptive_115", f"rho_{short}_incl_subcortex_no_p", rho_all, note="no spatial null for subcortex")
rec("spatial_spin_cortical99", "bh_threshold_across_5_maps", thr5)
Rm = np.array([[spearmanr(receptor[a][region_idx], receptor[b][region_idx])[0] for b in RECEPTORS] for a in RECEPTORS])
print("receptor inter-correlation (Spearman, 115 regions):")
for a, row in zip(RECEPTORS, Rm):
    print(f"  {a.replace('mean', '').replace('_sch116', ''):6s} " + " ".join(f"{v:+.2f}" for v in row))
    for b, v in zip(RECEPTORS, row):
        if a < b:
            rec("receptor_intercorrelation", f"{a.replace('mean', '').replace('_sch116', '')}_vs_{b.replace('mean', '').replace('_sch116', '')}", v)

# ------------------------------------------------------------------ 4. workspace comparison
print("\n== workspace comparison (network-level proxies of Luppi et al. 2024; EXPLORATORY)")


def set_mean(per_subject_map, orig_set):
    return per_subject_map[:, positions(orig_set)].mean(1)


for label, (ws, gw, bc) in PROXIES.items():
    non_cort = cortical_all - ws
    for non_label, non in (("vs_noncortex_ws", non_cort), ("vs_noncortex_ws+subcortex", non_cort | subcortical_all)):
        ws_m, non_m = set_mean(did, ws), set_mean(did, non)
        d = ws_m - non_m
        lo, hi = boot_ci(d)
        rec(f"workspace_{label}", f"workspace_minus_nonworkspace_{non_label}", d.mean(), lo, hi, signflip_p(d),
            note=f"n_ws={len(ws)} n_non={len(non)} neg={int((d < 0).sum())}/14")
        lo, hi = boot_ci(ws_m); rec(f"workspace_{label}", f"workspace_mean_did_{non_label}", ws_m.mean(), lo, hi, signflip_p(ws_m))
        lo, hi = boot_ci(non_m); rec(f"workspace_{label}", f"nonworkspace_mean_did_{non_label}", non_m.mean(), lo, hi, signflip_p(non_m))
        for sub_label, sub in (("gateway_proxy", gw), ("broadcaster_proxy", bc)):
            d2 = set_mean(did, sub) - non_m
            lo, hi = boot_ci(d2)
            rec(f"workspace_{label}", f"{sub_label}_minus_nonworkspace_{non_label}", d2.mean(), lo, hi, signflip_p(d2),
                note=f"n={len(sub)} neg={int((d2 < 0).sum())}/14")
    d3 = set_mean(did, gw) - set_mean(did, bc)
    lo, hi = boot_ci(d3)
    rec(f"workspace_{label}", "gateway_proxy_minus_broadcaster_proxy", d3.mean(), lo, hi, signflip_p(d3),
        note=f"n_gw={len(gw)} n_bc={len(bc)}")

# ------------------------------------------------------------------ 5. descriptive rank-rule check (placebo run)
print("\n== rank-rule check on the placebo run (descriptive; not used for selection)")
pcb_sts = regional[:, 1, :, :, 0].mean((0, 1))      # (115,) subject- and bin-mean synergy strength
pcb_rtr = regional[:, 1, :, :, 1].mean((0, 1))
rank_sts = rankdata(pcb_sts)                        # higher value -> higher rank
rank_rtr = rankdata(pcb_rtr)
rule = rank_sts > rank_rtr
rule_orig = set(int(region_idx[k]) for k in np.where(rule)[0])
ws_primary = PROXIES["primary_Default+Cont"][0]
inter = rule_orig & ws_primary
union = (rule_orig & cortical_all) | ws_primary
rec("rankrule_placebo", "n_rankrule_workspace_of_115", float(rule.sum()))
rec("rankrule_placebo", "n_rankrule_cortical", float(len(rule_orig & cortical_all)))
rec("rankrule_placebo", "n_rankrule_subcortical", float(len(rule_orig & subcortical_all)))
rec("rankrule_placebo", "overlap_with_primary_proxy_count", float(len(inter)), note=f"proxy n=37; rule cortical n={len(rule_orig & cortical_all)}")
rec("rankrule_placebo", "jaccard_rule_vs_primary_proxy_cortical", len(inter) / len(union) if union else np.nan)
rec("rankrule_placebo", "spearman_rank_sts_vs_rank_rtr_115", spearmanr(pcb_sts, pcb_rtr)[0])
for n_i, n_name in enumerate(NETS + ("Subcortex",), start=1):
    in_net = net115 == n_i
    rec("rankrule_placebo_composition", f"{n_name}_rule_count_of_{int(in_net.sum())}", float((rule & in_net).sum()))
# same rank rule on DMT run, descriptive only
dmt_sts = regional[:, 0, :, :, 0].mean((0, 1)); dmt_rtr = regional[:, 0, :, :, 1].mean((0, 1))
rule_dmt = rankdata(dmt_sts) > rankdata(dmt_rtr)
rec("rankrule_dmt_descriptive", "n_rankrule_workspace_of_115", float(rule_dmt.sum()))
rec("rankrule_dmt_descriptive", "n_regions_same_membership_as_placebo", float((rule_dmt == rule).sum()))

# ------------------------------------------------------------------ write
out = RESULTS / f"regional_analysis_{V}.csv"
with open(out, "w") as f:
    f.write(HEADER + "\n")
    f.write("section,name,value,ci_lo,ci_hi,p,note\n")
    for section, name, value, lo, hi, p, note in rows:
        f.write(f"{section},{name},{value:.6f},{'' if np.isnan(lo) else f'{lo:.6f}'},"
                f"{'' if np.isnan(hi) else f'{hi:.6f}'},{'' if np.isnan(p) else f'{p:.5f}'},\"{note}\"\n")
print(f"\nwrote {out}, {RESULTS / f'regional_did_map_{V}.csv'}, "
      f"{RESULTS / f'regional_atoms_bins_115regions-all_{V}_global.npy'}  ({time.time() - t0:.0f}s)")
