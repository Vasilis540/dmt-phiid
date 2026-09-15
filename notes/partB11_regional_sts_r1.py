"""
partB11_regional_sts_r1.py — regional test of the spatial-map claim (Discussion, "A distinction for
applicability"; Limitations listed it as not run). Pre-run entry: manuscript/analysis_record.md, "Run-level mean
cross-lag deviation and the regional sts–r₁ test: pre-run entry, 15 Sep 2026" (prediction recorded there).

Per region, MMI-sts averaged over the region's 114 pairs, from the saved regional atoms of
scripts/11_regional_analysis.py (results/regional_atoms_bins_115regions-all_ts_gsr_global.npy: global fit, local
atoms averaged per 30-TR bin; here the placebo run, pre-injection bins 1–8, mean over bins and over the 14 subjects),
against the region's lag-1 autocorrelation on the same run and span (windowed, W = 60: each region standardised
within the window with its own mean and ddof-1 variance, r₁ = mean of z_t z_{t+1} over the window's consecutive
kept TRs, as rev_series.autocorr_series computes it; windows 1–4, mean over windows and subjects). The whole-span
value (TRs 0–239 standardised as one segment) is reported beside it as a check. ts_gsr. Pearson and Spearman
across the 115 regions (descriptive; subcortex has no spatial null), and a spin test on the 100 cortical parcels
(region 20 NaN, 99 valid) with the Vasa rotations in external/DMT_NCT/fxns/SpinTests/rotated_maps/
rotated_Schaefer_100.mat (10,000 rotations, both directions, two-sided p and Vasa one-sided-average p, exactly as
scripts/11 applies them). The same is reported for rtr and for sts − rtr (synergy minus redundancy), and the
per-subject correlations across regions are given as a robustness check. Everything is reported regardless of
outcome; the pre-specified quantity is the correlation of regional sts with regional r₁.

Outputs: notes/review_results/partB/regional_sts_r1_tables.md, regional_sts_r1.csv (one row per region),
regional_sts_r1_run.log (via run_all.sh's nstep, or stdout).
Run from the repository root: .venv/bin/python notes/partB11_regional_sts_r1.py   (about a minute)
"""
import subprocess
import sys
import time
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.stats import pearsonr, spearmanr

REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
SPIN = REPO / "external" / "DMT_NCT" / "fxns" / "SpinTests" / "rotated_maps" / "rotated_Schaefer_100.mat"
LUT = REPO / "data" / "Schaefer2018_100Parcels_7Networks_order.lut"
ATOMS_REG = REPO / "results" / "regional_atoms_bins_115regions-all_ts_gsr_global.npy"
OUT = REPO / "notes" / "review_results" / "partB"
OUT.mkdir(parents=True, exist_ok=True)
SEED = 20261120
N_BOOT = 10000
N_CORTICAL = 100
EXCLUDE = 20
REGIONS = np.array([r for r in range(116) if r != EXCLUDE])          # 115 original indices
W = 60
PRE_BINS = slice(0, 8)                                               # bins 1–8 = TRs 0–239
PRE_WINDOWS = range(4)                                               # windows 1–4 = TRs 0–239
PCB = 1                                                              # condition axis: 0 = DMT, 1 = PCB

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=REPO).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "notes/*.py", "manuscript/analysis_record.md"],
                               text=True, cwd=REPO).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

t0 = time.time()
lut = [l.split() for l in LUT.read_text().strip().splitlines()]
names = [l[4].replace("7Networks_", "") for l in lut] + [f"SUB_{k + 1}" for k in range(116 - N_CORTICAL)]
is_cortical = REGIONS < N_CORTICAL

# regional atoms of scripts/11: (14 subjects, 2 conditions, 28 bins, 115 regions, [sts, rtr]); placebo run, bins 1–8
A = np.load(ATOMS_REG)
assert A.shape == (14, 2, 28, 115, 2) and np.isfinite(A).all()
sts_subj = A[:, PCB, PRE_BINS, :, 0].mean(1)                         # (14, 115)
rtr_subj = A[:, PCB, PRE_BINS, :, 1].mean(1)
sts_map, rtr_map = sts_subj.mean(0), rtr_subj.mean(0)
smr_subj = sts_subj - rtr_subj
smr_map = smr_subj.mean(0)

# regional lag-1 autocorrelation, placebo run, windows 1–4 (windowed) and TRs 0–239 as one segment (span)
ts = sio.loadmat(MAT)["ts_gsr"]
r1_win_subj = np.full((14, 115), np.nan); r1_span_subj = np.full((14, 115), np.nan)
for s in range(14):
    X = np.asarray(ts[s, PCB], float)[REGIONS]
    kept = np.where(np.all(np.isfinite(X), axis=0))[0]
    per_w = []
    for w in PRE_WINDOWS:
        in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
        Xw = X[:, in_w]
        Z = (Xw - Xw.mean(1, keepdims=True)) / np.sqrt(Xw.var(1, ddof=1, keepdims=True))
        consecutive = (in_w[1:] - in_w[:-1]) == 1
        per_w.append((Z[:, :-1] * Z[:, 1:])[:, consecutive].mean(1))
    r1_win_subj[s] = np.mean(per_w, axis=0)
    span = kept[kept < 240]
    Xs = X[:, span]
    Z = (Xs - Xs.mean(1, keepdims=True)) / np.sqrt(Xs.var(1, ddof=1, keepdims=True))
    consecutive = (span[1:] - span[:-1]) == 1
    r1_span_subj[s] = (Z[:, :-1] * Z[:, 1:])[:, consecutive].mean(1)
r1_win, r1_span = r1_win_subj.mean(0), r1_span_subj.mean(0)

# spin test on the cortical parcels (scripts/11's construction)
with h5py.File(SPIN, "r") as f:
    perm_id = f["perm_id"][()]
if perm_id.shape[0] != N_CORTICAL:
    perm_id = perm_id.T
perm_id = perm_id.astype(int) - int(perm_id.min())                   # (100, n_rot), zero-based
n_rot = perm_id.shape[1]
assert perm_id.shape == (N_CORTICAL, n_rot)


def cortical_vector(v115):
    out = np.full(N_CORTICAL, np.nan)
    out[REGIONS[is_cortical]] = v115[is_cortical]
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


rng = np.random.default_rng(SEED)
lines = [f"# Regional MMI-sts against regional lag-1 autocorrelation, placebo run, pre-injection (partB11_regional_sts_r1.py; git={sha}; seed={SEED})", "",
         "Regional sts = mean over the region's 114 pairs of the global-fit local sts (scripts/11 atoms), placebo run, bins 1–8, "
         "mean over subjects; regional r₁ = windowed lag-1 autocorrelation (W = 60, windows 1–4, standardised within window), mean over "
         "windows and subjects; ts_gsr; 115 regions. Prediction recorded before the run (analysis_record.md, pre-run entry of 15 Sep 2026): "
         "positive correlation of regional sts with regional r₁ if the spatial-map exposure is real on these data. "
         "Spin test: Vasa rotations of the 100 Schaefer parcels (10,000, both directions), region 20 NaN, two-sided p and Vasa one-sided-average p.", "",
         f"Regional r₁: mean {r1_win.mean():.4f}, min {r1_win.min():.4f}, max {r1_win.max():.4f} (windowed); whole-span TRs 0–239: mean {r1_span.mean():.4f}, "
         f"r(windowed, span) across regions {pearsonr(r1_win, r1_span)[0]:+.4f}. Regional sts: mean {sts_map.mean():.4f}, min {sts_map.min():.4f}, max {sts_map.max():.4f}; "
         f"regional rtr: mean {rtr_map.mean():.4f}, min {rtr_map.min():.4f}, max {rtr_map.max():.4f}.", "",
         "| map | against | Pearson r (115) | Spearman ρ (115) | Spearman ρ (99 cortical) | spin p two-sided | Vasa p | null SD |", "|---|---|---|---|---|---|---|---|"]
results = {}
for mname, m in (("sts", sts_map), ("rtr", rtr_map), ("sts − rtr", smr_map)):
    for rname, r in (("r₁ windowed", r1_win), ("r₁ whole-span", r1_span)):
        pr = pearsonr(m, r)[0]; rho = spearmanr(m, r)[0]
        rho_c, p_vasa, p_two, null_sd = spin_test(cortical_vector(m), cortical_vector(r))
        results[(mname, rname)] = (pr, rho, rho_c, p_two, p_vasa)
        lines.append(f"| {mname} | {rname} | {pr:+.3f} | {rho:+.3f} | {rho_c:+.3f} | {p_two:.4f} | {p_vasa:.4f} | {null_sd:.3f} |")
lines.append("")
# per-subject correlations across regions (robustness; windowed r₁)
per_subj = np.array([pearsonr(sts_subj[s], r1_win_subj[s])[0] for s in range(14)])
boot = per_subj[rng.integers(0, 14, (N_BOOT, 14))].mean(1)
lo, hi = np.percentile(boot, [2.5, 97.5])
lines.append(f"Per-subject Pearson r(regional sts, regional r₁) across the 115 regions: mean {per_subj.mean():+.3f} [{lo:+.3f}, {hi:+.3f}] "
             f"(subject bootstrap), min {per_subj.min():+.3f}, max {per_subj.max():+.3f}, positive in {int((per_subj > 0).sum())}/14.")
per_subj_smr = np.array([pearsonr(smr_subj[s], r1_win_subj[s])[0] for s in range(14)])
lines.append(f"Per-subject Pearson r(regional sts − rtr, regional r₁): mean {per_subj_smr.mean():+.3f}, positive in {int((per_subj_smr > 0).sum())}/14.")
# variance share and the between-region spread, for scale
r2 = results[("sts", "r₁ windowed")][0] ** 2
lines.append(f"Share of the between-region variance of sts carried by regional r₁ (r² of the 115-region Pearson): {r2:.3f}. "
             f"SD across regions: sts {sts_map.std(ddof=1):.4f}, rtr {rtr_map.std(ddof=1):.4f}, r₁ {r1_win.std(ddof=1):.4f}.")
lines.append(f"Cortical (99) vs subcortical (16) means: sts {sts_map[is_cortical].mean():.4f} vs {sts_map[~is_cortical].mean():.4f}; "
             f"r₁ {r1_win[is_cortical].mean():.4f} vs {r1_win[~is_cortical].mean():.4f}.")
pr, rho, rho_c, p_two, p_vasa = results[("sts", "r₁ windowed")]
verdict = "positive" if pr > 0 else "not positive"
lines.append(f"Reading under the pre-run entry: the pre-specified correlation (regional sts vs windowed regional r₁, Pearson) is {verdict} ({pr:+.3f}; spin p = {p_two:.4f} on the 99 cortical parcels).")
lines.append("")
pd.DataFrame(dict(region_index=REGIONS, name=[names[r] for r in REGIONS], cortical=is_cortical, sts_pcb_pre=sts_map, rtr_pcb_pre=rtr_map,
                  sts_minus_rtr=smr_map, r1_windowed=r1_win, r1_span=r1_span)).to_csv(OUT / "regional_sts_r1.csv", index=False)
(OUT / "regional_sts_r1_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done in {time.time() - t0:.0f} s; wrote {OUT / 'regional_sts_r1_tables.md'} and regional_sts_r1.csv")
