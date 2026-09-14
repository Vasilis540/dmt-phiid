"""
partB1_scope_map.py — Part B item 1 (notes/partB_prespec_2026-09-14.md, B1): the scope map.

Model: two unit-variance AR(1) processes with common coefficient a (= lag-1 autocorrelation r1)
and innovation correlation q (= lag-0 cross-correlation); the lag-1 4-vector correlation matrix
is S4 = [[1, q, a, aq], [q, 1, aq, a], [a, aq, 1, q], [aq, a, q, 1]] (rev_phiid_fast.ar1_corr with
a_x = a_y). All 16 Gaussian-MMI atoms are closed-form functions of (r1, q) through S4
(rev_phiid_fast.atoms_from_corr, phyid's definitions).

Computed: sts, xtx + yty, sts − (xtx + yty) on r1 ∈ [0, 0.95] × q ∈ [−0.6, 0.6] (step 0.01);
∂sts/∂r1, ∂sts/∂q by central differences (h = 0.001); the region |∂sts/∂r1| > |∂sts/∂q| and its
boundary; the overlay of every pair's (r1, q) for subject 1 (index 0), both variants, both runs,
windows 1–4 and 6 at W = 60 (r1 of a pair = mean of its two regions' within-window lag-1
autocorrelations, q = the pair's within-window lag-0 correlation, both from the PairPhiID
standardised blocks); the fraction of real pairs in the autocorrelation-dominated region.
Real pairs with |q| > 0.6 are classified on an extended grid (|q| ≤ 0.95) and counted.

Outputs: notes/review_results/partB/scope_map_grid.npz, scope_map_tables.md,
         scope_map_overlay.csv, scope_map.png
"""
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
OUT.mkdir(parents=True, exist_ok=True)
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
SUBJ = 0
WINDOWS = (0, 1, 2, 3, 5)                                   # 0-based: windows 1–4 and 6
H = 1e-3
FLAT = 1e-3                                                 # both |derivatives| below this: "flat"
t0 = time.time()

# ------------------------------------------------------------------ 1. the map
r1_grid = np.round(np.arange(0.0, 0.95 + 1e-9, 0.01), 4)
q_grid = np.round(np.arange(-0.60, 0.60 + 1e-9, 0.01), 4)
q_ext = np.round(np.arange(-0.95, 0.95 + 1e-9, 0.01), 4)   # extended, for classifying real pairs


def maps(r1s, qs):
    R, Q = np.meshgrid(r1s, qs, indexing="ij")
    A = atoms_from_corr(ar1_corr(R.ravel(), R.ravel(), Q.ravel())).reshape(R.shape + (16,))
    sts = A[..., IX["sts"]]
    self_pred = A[..., IX["xtx"]] + A[..., IX["yty"]]
    d_r1 = (atoms_from_corr(ar1_corr((R + H).ravel(), (R + H).ravel(), Q.ravel()))[:, IX["sts"]]
            - atoms_from_corr(ar1_corr((R - H).ravel(), (R - H).ravel(), Q.ravel()))[:, IX["sts"]]).reshape(R.shape) / (2 * H)
    d_q = (atoms_from_corr(ar1_corr(R.ravel(), R.ravel(), (Q + H).ravel()))[:, IX["sts"]]
           - atoms_from_corr(ar1_corr(R.ravel(), R.ravel(), (Q - H).ravel()))[:, IX["sts"]]).reshape(R.shape) / (2 * H)
    region = np.where((np.abs(d_r1) < FLAT) & (np.abs(d_q) < FLAT), 0, np.where(np.abs(d_r1) > np.abs(d_q), 1, 2))   # 0 flat, 1 r1-dominated, 2 q-dominated
    return dict(R=R, Q=Q, atoms=A, sts=sts, self_pred=self_pred, d_r1=d_r1, d_q=d_q, region=region)


M = maps(r1_grid, q_grid)
M_ext = maps(r1_grid, q_ext)
np.savez(OUT / "scope_map_grid.npz", r1=r1_grid, q=q_grid, **{k: v for k, v in M.items() if k != "atoms"}, atoms=M["atoms"],
         q_ext=q_ext, region_ext=M_ext["region"], sts_ext=M_ext["sts"])
print(f"map computed ({time.time() - t0:.0f}s)")

# boundary r1*(q): smallest r1 at which the r1-dominated region begins (region == 1) above the flat zone, per q
lines = ["# Scope map tables (partB1_scope_map.py)", ""]
lines += ["## sts(r1, q), nats (rows r1, columns q)", "", "| r1 \\ q | " + " | ".join(f"{q:+.1f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |", "|---|" + "---|" * 7]
for r1 in (0.0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95):
    i = int(np.argmin(np.abs(r1_grid - r1)))
    lines.append(f"| {r1:.2f} | " + " | ".join(f"{M['sts'][i, int(np.argmin(np.abs(q_grid - q)))]:.4f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |")
lines += ["", "## xtx + yty (rows r1, columns q)", "", "| r1 \\ q | " + " | ".join(f"{q:+.1f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |", "|---|" + "---|" * 7]
for r1 in (0.0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95):
    i = int(np.argmin(np.abs(r1_grid - r1)))
    lines.append(f"| {r1:.2f} | " + " | ".join(f"{M['self_pred'][i, int(np.argmin(np.abs(q_grid - q)))]:.4f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |")
lines += ["", "## sts − (xtx + yty), nats, and as a share of sts (rows r1, columns q)", "", "| r1 \\ q | " + " | ".join(f"{q:+.1f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |", "|---|" + "---|" * 7]
for r1 in (0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95):
    i = int(np.argmin(np.abs(r1_grid - r1)))
    cells = []
    for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6):
        j = int(np.argmin(np.abs(q_grid - q)))
        d = M["sts"][i, j] - M["self_pred"][i, j]
        cells.append(f"{d:+.4f} ({100 * d / M['sts'][i, j]:+.1f} %)" if M["sts"][i, j] > 1e-9 else "0")
    lines.append(f"| {r1:.2f} | " + " | ".join(cells) + " |")
lines += ["", "## ∂sts/∂r1 and ∂sts/∂q (nats per unit; rows r1, columns q; entry = ∂/∂r1 / ∂/∂q)", "", "| r1 \\ q | " + " | ".join(f"{q:+.1f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |", "|---|" + "---|" * 7]
for r1 in (0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95):
    i = int(np.argmin(np.abs(r1_grid - r1)))
    lines.append(f"| {r1:.2f} | " + " | ".join(f"{M['d_r1'][i, int(np.argmin(np.abs(q_grid - q)))]:+.3f} / {M['d_q'][i, int(np.argmin(np.abs(q_grid - q)))]:+.3f}" for q in (-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6)) + " |")

# boundary: for each q, the r1 values where region changes; report the smallest r1 above which the map is r1-dominated for all larger r1
lines += ["", "## Boundary of the autocorrelation-dominated region: for each q, the r1 above which |∂sts/∂r1| > |∂sts/∂q| for every larger r1 on the grid (and the r1 range that is q-dominated, if any)", "",
          "| q | r1 above which r1-dominated | q-dominated r1 range | flat (both derivatives < 0.001) r1 range |", "|---|---|---|---|"]
for q in (-0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -0.05, 0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
    j = int(np.argmin(np.abs(q_grid - q)))
    reg = M["region"][:, j]
    dom = np.where(reg == 1)[0]
    qd = np.where(reg == 2)[0]
    fl = np.where(reg == 0)[0]
    # smallest index k such that reg[k:] all == 1
    k = len(reg)
    while k > 0 and reg[k - 1] == 1:
        k -= 1
    above = f"{r1_grid[k]:.2f}" if k < len(reg) else "never"
    lines.append(f"| {q:+.2f} | {above} | {('%.2f–%.2f' % (r1_grid[qd.min()], r1_grid[qd.max()])) if qd.size else 'none'} | {('%.2f–%.2f' % (r1_grid[fl.min()], r1_grid[fl.max()])) if fl.size else 'none'} |")
frac_dom = (M["region"] == 1).mean()
lines += ["", f"Share of the requested grid (r1 0–0.95 × q −0.6–0.6) that is r1-dominated: {100 * frac_dom:.1f} %; q-dominated: {100 * (M['region'] == 2).mean():.1f} %; flat: {100 * (M['region'] == 0).mean():.1f} %."]

# ------------------------------------------------------------------ 2. overlay: real pairs of subject 1
ts = sio.loadmat(MAT)
rows = ["variant,condition,window,n_pairs,frac_r1_dominated,frac_q_dominated,frac_flat,frac_abs_q_above_0.6,median_r1,p05_r1,p95_r1,median_q,p05_q,p95_q,median_abs_q,mean_observed_sts,mean_model_sts_at_pair_r1_q"]
overlay = {}
lines += ["", "## Real pairs of subject 1 (index 0) on the map, W = 60", "", "| variant | run | window | pairs | r1-dominated | q-dominated | flat | pairs with \\|q\\| > 0.6 | r1 median (5–95 %) | q median (5–95 %) | \\|q\\| median | observed sts, pair mean | model sts at the pairs' (r1, q), mean |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for var in ("ts_gsr", "ts_demean"):
    for c, cn in enumerate(("DMT", "PCB")):
        X = np.asarray(ts[var][SUBJ, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        for w in WINDOWS:
            in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
            pp = PairPhiID(X[:, in_w])
            r1_pair = 0.5 * (pp.C[:, 0, 2] + pp.C[:, 1, 3])          # mean of the two regions' lag-1 autocorrelations
            q_pair = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])           # lag-0 correlation (past block and future block averaged)
            obs = pp.atoms_mean()[:, IX["sts"]]
            model = atoms_from_corr(ar1_corr(r1_pair, r1_pair, q_pair))[:, IX["sts"]]
            ii = np.clip(np.round((r1_pair - r1_grid[0]) / 0.01).astype(int), 0, r1_grid.size - 1)
            jj = np.clip(np.round((q_pair - q_ext[0]) / 0.01).astype(int), 0, q_ext.size - 1)
            reg = M_ext["region"][ii, jj]
            overlay[(var, cn, w)] = (r1_pair, q_pair, obs, model)
            vals = [var, cn, w + 1, r1_pair.size, (reg == 1).mean(), (reg == 2).mean(), (reg == 0).mean(), (np.abs(q_pair) > 0.6).mean(),
                    np.median(r1_pair), np.percentile(r1_pair, 5), np.percentile(r1_pair, 95), np.median(q_pair), np.percentile(q_pair, 5), np.percentile(q_pair, 95), np.median(np.abs(q_pair)), obs.mean(), model.mean()]
            rows.append(",".join(f"{v:.6f}" if isinstance(v, float) else str(v) for v in vals))
            lines.append(f"| {var} | {cn} | {w + 1} | {r1_pair.size} | {100 * (reg == 1).mean():.1f} % | {100 * (reg == 2).mean():.1f} % | {100 * (reg == 0).mean():.1f} % | {100 * (np.abs(q_pair) > 0.6).mean():.1f} % | "
                         f"{np.median(r1_pair):.3f} ({np.percentile(r1_pair, 5):.3f}–{np.percentile(r1_pair, 95):.3f}) | {np.median(q_pair):+.3f} ({np.percentile(q_pair, 5):+.3f}–{np.percentile(q_pair, 95):+.3f}) | {np.median(np.abs(q_pair)):.3f} | {obs.mean():.4f} | {model.mean():.4f} |")
(OUT / "scope_map_overlay.csv").write_text("\n".join(rows) + "\n")
(OUT / "scope_map_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[-12:]))
np.savez(OUT / "scope_map_overlay_points.npz", **{f"{v}_{c}_w{w + 1}_{k}": arr for (v, c, w), tup in overlay.items() for k, arr in zip(("r1", "q", "obs", "model"), tup)})

# ------------------------------------------------------------------ 3. figure
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(15, 8.5), constrained_layout=True)
ext = [q_grid[0], q_grid[-1], r1_grid[0], r1_grid[-1]]
for ax, key, title, cmap, sym in ((axes[0, 0], "sts", "sts(r1, q), nats", "Blues", False),
                                  (axes[0, 1], "self_pred", "xtx + yty, nats", "Blues", False),
                                  (axes[0, 2], None, "sts − (xtx + yty), nats", "RdBu_r", True),
                                  (axes[1, 0], "d_r1", "∂sts/∂r1, nats per unit (all positive)", "Blues", False),
                                  (axes[1, 1], "d_q", "∂sts/∂q, nats per unit", "RdBu_r", True)):
    Z = (M["sts"] - M["self_pred"]) if key is None else M[key]
    vmax = np.nanmax(np.abs(Z))
    im = ax.imshow(Z, origin="lower", aspect="auto", extent=ext, cmap=cmap, vmin=-vmax if sym else 0, vmax=vmax)
    ax.contour(M["Q"], M["R"], M["region"], levels=[0.5, 1.5], colors=["#444444", "#000000"], linewidths=1.2)
    ax.set_title(title)
    ax.set_xlabel("q (lag-0 cross-correlation)")
    ax.set_ylabel("r1 (lag-1 autocorrelation)")
    fig.colorbar(im, ax=ax, shrink=0.85)
ax = axes[1, 2]
ax.imshow(M["region"], origin="lower", aspect="auto", extent=ext, cmap=matplotlib.colors.ListedColormap(["#e6e6e6", "#c6dbef", "#fdd0a2"]), vmin=-0.5, vmax=2.5)
for (var, cn, w), col, mk in ((("ts_gsr", "DMT", 5), "#08519c", "."), (("ts_gsr", "PCB", 1), "#e6550d", ".")):
    r1p, qp, _, _ = overlay[(var, cn, w)]
    ax.scatter(qp, r1p, s=2, c=col, marker=mk, alpha=0.35, label=f"subject 1 {var} {cn} window {w + 1}")
ax.set_xlim(q_grid[0], q_grid[-1]); ax.set_ylim(r1_grid[0], r1_grid[-1])
ax.set_title("regions (blue = r1-dominated; no q-dominated cell) + real pairs")
ax.set_xlabel("q (lag-0 cross-correlation)"); ax.set_ylabel("r1 (lag-1 autocorrelation)")
ax.legend(loc="lower left", fontsize=8, markerscale=6)
fig.suptitle("Scope map: Gaussian-MMI sts of a bivariate AR(1) pair as a function of (r1, q); black line = boundary |∂sts/∂r1| = |∂sts/∂q|, grey line = edge of the flat zone")
fig.savefig(OUT / "scope_map.png", dpi=130)
print(f"wrote {OUT / 'scope_map.png'} ({time.time() - t0:.0f}s)")
