"""
partB20_regional_partial.py — B20: the regional sts and sts − rtr maps with regional r₁ partialled out.
Pre-run entry: manuscript/analysis_record.md, "The regional map with regional r₁ partialled out (B20): pre-run entry,
20 Sep 2026" (specification, prediction and rule as in notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5).

Group maps (no external data): notes/review_results/partB/regional_sts_r1.csv (partB11; per region the placebo
pre-injection sts, rtr, sts − rtr and the windowed and whole-span r₁; 115 regions, ts_gsr). Ordinary least squares of
the sts map and of the sts − rtr map on regional r₁ (windowed; whole-span as a sensitivity) with intercept; the
residual maps; means by Yeo-7 network (from the parcel names of data/Schaefer2018_100Parcels_7Networks_order.lut)
and the 16 subcortical parcels as one class; the sensory (Vis + SomMot) minus association (Default + Cont) contrast
before and after partialling, in nats and in units of the map's SD across regions.
Per-subject version: per-subject regional sts from results/regional_atoms_bins_115regions-all_ts_gsr_global.npy
(placebo bins 1–8, mean over bins) against per-subject regional r₁ recomputed exactly as partB11 computes it
(placebo windows 1–4, standardised within the window; needs the .mat); the same regression per subject; the mean
and SD over subjects of the sensory − association contrast before and after partialling, with the exact sign-flip p.
Skipped, and said so, when the .mat is absent. No spin test (the two maps are algebraically linked). Seed 20261120
(no random draws).
Outputs (notes/review_results/partB/): regional_partial_tables.md, regional_partial.csv (one row per region),
regional_partial_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB20_regional_partial.py   (seconds)
"""
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
LUT = REPO / "data" / "Schaefer2018_100Parcels_7Networks_order.lut"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
ATOMS_REG = REPO / "results" / "regional_atoms_bins_115regions-all_ts_gsr_global.npy"
REGIONS = np.array([r for r in range(116) if r != 20])
SEED = 20261120
NETS = ("Vis", "SomMot", "DorsAttn", "SalVentAttn", "Limbic", "Cont", "Default", "Subcortex")
SENSORY, ASSOC = ("Vis", "SomMot"), ("Default", "Cont")
SIGNS = np.array(list(product((-1, 1), repeat=14)))
t0 = time.time()


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def partial_out(y, x):
    X = np.c_[np.ones(x.size), x]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta, beta[1], 1 - np.sum((y - X @ beta) ** 2) / np.sum((y - y.mean()) ** 2)


reg = np.genfromtxt(OUT / "regional_sts_r1.csv", delimiter=",", names=True, dtype=None, encoding="utf-8")
names = [str(n) for n in reg["name"]]
lut = [l.split()[4].replace("7Networks_", "") for l in LUT.read_text().strip().splitlines()]
assert all(names[i] == lut[r] for i, r in enumerate(REGIONS) if r < 100), "parcel names of regional_sts_r1.csv do not match the LUT"
net = np.array([("Subcortex" if n.startswith("SUB_") else n.split("_")[1]) for n in names])
assert set(net) <= set(NETS), set(net)
sts, rtr, smr = reg["sts_pcb_pre"], reg["rtr_pcb_pre"], reg["sts_minus_rtr"]
r1w, r1s = reg["r1_windowed"], reg["r1_span"]
is_sens = np.isin(net, SENSORY); is_assoc = np.isin(net, ASSOC)

lines = ["# The regional sts and sts − rtr maps with regional r₁ partialled out (partB20_regional_partial.py)", f"git={SHA}", "",
         "Group maps from regional_sts_r1.csv (partB11: placebo run, pre-injection; ts_gsr; 115 regions); OLS with intercept on regional r₁ (windowed W = 60 windows 1–4; whole-span TRs 0–239 as a sensitivity); "
         f"Yeo-7 networks from the parcel names, the 16 subcortical parcels as one class; sensory = Vis + SomMot ({int(is_sens.sum())} parcels), association = Default + Cont ({int(is_assoc.sum())} parcels). No spin test (the maps are algebraically linked). Seed {SEED}.", ""]
csv = ["region_index,name,network,sts,rtr,sts_minus_rtr,r1_windowed,r1_span,sts_resid_win,smr_resid_win,sts_resid_span,smr_resid_span"]
resid = {}
for label, y in (("sts", sts), ("sts − rtr", smr)):
    for rl, x in (("windowed", r1w), ("whole-span", r1s)):
        res, slope, r2 = partial_out(y, x)
        resid[(label, rl)] = res
        c_before = y[is_sens].mean() - y[is_assoc].mean(); c_after = res[is_sens].mean() - res[is_assoc].mean()
        lines += [f"## {label} map on regional r₁ ({rl})", "",
                  f"Slope {slope:+.4f} nats per unit r₁ (r² = {r2:.3f}); SD across regions of the map {y.std(ddof=1):.4f}, of the residual map {res.std(ddof=1):.4f}.",
                  f"Sensory − association contrast: before partialling {c_before:+.4f} nats ({c_before / y.std(ddof=1):+.2f} map SD); after partialling {c_after:+.4f} nats ({c_after / res.std(ddof=1):+.2f} residual-map SD); "
                  f"the same contrast of r₁ itself {x[is_sens].mean() - x[is_assoc].mean():+.4f}.", "",
                  "| network | n | map mean | residual mean | r₁ mean |", "|---|---|---|---|---|"]
        for n in NETS:
            m = net == n
            lines.append(f"| {n} | {int(m.sum())} | {y[m].mean():+.4f} | {res[m].mean():+.4f} | {x[m].mean():.4f} |")
        lines.append("")
for i in range(115):
    csv.append(f"{int(reg['region_index'][i])},{names[i]},{net[i]},{sts[i]:.6f},{rtr[i]:.6f},{smr[i]:.6f},{r1w[i]:.6f},{r1s[i]:.6f},"
               f"{resid[('sts', 'windowed')][i]:.6f},{resid[('sts − rtr', 'windowed')][i]:.6f},{resid[('sts', 'whole-span')][i]:.6f},{resid[('sts − rtr', 'whole-span')][i]:.6f}")
(OUT / "regional_partial.csv").write_text(f"# partB20_regional_partial.py; residual maps after partialling regional r₁; git={SHA}\n" + "\n".join(csv) + "\n")

# per-subject version
if MAT.exists():
    import scipy.io as sio
    A = np.load(ATOMS_REG)
    assert A.shape == (14, 2, 28, 115, 2)
    sts_subj = A[:, 1, 0:8, :, 0].mean(1); rtr_subj = A[:, 1, 0:8, :, 1].mean(1); smr_subj = sts_subj - rtr_subj
    ts = sio.loadmat(MAT)["ts_gsr"]
    r1_subj = np.full((14, 115), np.nan)
    for s in range(14):
        X = np.asarray(ts[s, 1], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        per_w = []
        for w in range(4):
            in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
            Xw = X[:, in_w]
            Z = (Xw - Xw.mean(1, keepdims=True)) / np.sqrt(Xw.var(1, ddof=1, keepdims=True))
            consecutive = (in_w[1:] - in_w[:-1]) == 1
            per_w.append((Z[:, :-1] * Z[:, 1:])[:, consecutive].mean(1))
        r1_subj[s] = np.mean(per_w, axis=0)
    lines += ["## Per-subject version (regional sts from results/regional_atoms_bins, placebo bins 1–8; regional r₁ recomputed as partB11, placebo windows 1–4)", "",
              "| map | contrast before partialling (mean ± SD over subjects; sign-flip p) | contrast after partialling (mean ± SD; p) | mean slope | mean r² |", "|---|---|---|---|---|"]
    for label, Y in (("sts", sts_subj), ("sts − rtr", smr_subj)):
        cb = np.array([Y[s][is_sens].mean() - Y[s][is_assoc].mean() for s in range(14)])
        ca = []; sl = []; rr = []
        for s in range(14):
            res, slope, r2 = partial_out(Y[s], r1_subj[s])
            ca.append(res[is_sens].mean() - res[is_assoc].mean()); sl.append(slope); rr.append(r2)
        ca = np.array(ca)
        lines.append(f"| {label} | {cb.mean():+.4f} ± {cb.std(ddof=1):.4f}; p = {signflip_p(cb):.4f} | {ca.mean():+.4f} ± {ca.std(ddof=1):.4f}; p = {signflip_p(ca):.4f} | {np.mean(sl):+.4f} | {np.mean(rr):.3f} |")
    lines.append("")
else:
    lines += ["## Per-subject version: skipped — external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat is not present in this checkout (the per-subject regional r₁ is recomputed from it as partB11 does).", ""]
lines += ["Prediction recorded (plan §5, B20): the residual map's sensory–association contrast is reduced; its sign is not predicted. Rule: reported as the partialled map; no spin test."]
(OUT / "regional_partial_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
