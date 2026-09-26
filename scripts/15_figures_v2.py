"""
15_figures_v2.py — manuscript figures for draft_v2 (the methods frame), drawn from saved results only.
Revised 21 Sep 2026 (the restructuring), 23 Sep 2026 (the shortened text: "predicted" became "AR(1)-substituted";
the mirrored q = −0.25 curve; Figure 3 redrawn; the residual map's network means; every interval of a mean over
subjects the inverted sign-flip interval of B21, notes/rev_inference_inverted.py) and 25 Sep 2026 (the review of
24 Sep 2026 applied: the figures renumbered by order of first citation in the text and their files renamed; the
atoms figure's annotation follows the unequal-coefficient finding; the expectation band of Fig 5c drawn as error
bars; the contour labels of Fig 1a moved clear of the density; the captions carry no computation labels or file
paths, their provenance being the "Source" sentence at the end of each, which the main text does not reproduce);
then the error-only check of 25 Sep 2026 applied (the Fig 2 caption's mirror and cross-prediction ranges computed
from the atoms; the Fig 1 caption's r₁ named as pair r₁; the Fig 6 caption's τ = 5 sentence stated through the
intervals and exact p; mathtext subscripts in legends, titles and labels; Fig 2's annotation lowered clear of the
legend; Fig 3's index labels placed nearest their own points, with a light backing, and panel b's annotation
within its axes; Fig 4b's labels with minus signs and Fig 4c's contrasts at five decimals; Fig 5c's legend below
the axis; the SHA rule of notes/rev_git.py for the captions header).

Fig 1   (a) the (r₁, q) scope map of two AR(1) processes correlated only at lag 0, with one subject's pre-injection
        pairs (the saved overlay) pooled (closed form, notes/rev_phiid_fast.py;
        notes/review_results/partB/scope_map_overlay_points.npz); (b) the excess sts − (xtx + yty); (c) sts against
        the coupling c of the symmetric VAR(1) pair at fixed (r₁, q), with the q = −0.25 curve mirrored by the
        invariance (c, q) → (−c, −q)  (notes/review_results/partB/coupling_map_tables.md; partB8)
        [file fig1_v2_scope_map; the figure numbered 2 in the drafts up to 23 Sep 2026]
Fig 2   the sixteen Gaussian-MMI atoms, observed and AR(1)-substituted, DMT pre-injection level and primary DiD,
        ts_gsr, W = 60  (notes/review_results/partB/family_atoms_ts_gsr_W60.npz; partB14)
        [file fig2_v2_atoms_observed_substituted; formerly Figure 1]
Fig 3   per subject: (a) the MMI-sts DiD against the whole-brain r₁ DiD, with the OLS fit and the band-passed
        generator's rate; (b) the cross-half relation; (c) the residual DiD against the r₁ DiD, with the OLS fit and
        the generators' rates  (notes/review_results/inference_rows_{raw,diag}.pkl;
        notes/review_results/partB/splithalf_subjects.csv; the rates from bandpassed_expectations_tables.md,
        diagnostic_alternatives_tables.md and notes/review_results/logs/review_v2_residual_null.log; the
        disattenuated ratio from inference_revision_tables.md)  [file fig3_v2_per_subject; unchanged number]
Fig 4   (a) regional sts against regional r₁, 115 regions coloured by network; (b) the sensory − association
        contrast of the sts and sts − rtr maps before and after partialling regional r₁ out; (c) the residual map's
        network means with the eight-class F and its spin test  (notes/review_results/partB/regional_partial.csv;
        partB20; the spin test from notes/review_results/partB/aligned_directed_tables.md, B22 (e))
        [file fig4_v2_regional; formerly Figure 6]
Fig 5   the AR(1)-substituted estimate by window: (a) observed and AR(1)-substituted whole-brain sts, (b) the
        residual, (c) the DMT − placebo residual difference per window against its expectation under a pure
        autocorrelation change, group means ± 1 within-subject SEM (Cousineau, 2005; Morey, 2008)
        (notes/review_results/partB/diag_series_ts_gsr_W60.npz; the expectation from
        notes/review_results/partB/calibration_filtered_tables.md when present, otherwise calibration_tables.md)
        [file fig5_v2_residual_diagnostic; formerly Figure 4]
Fig 6   the lag dependence of S14 Table  (notes/review_results/inference_rows_lag.pkl)
        [file fig6_v2_lag_dependence; formerly Figure 5]
Outputs manuscript/figures/fig{1..6}_v2_*.{png,pdf} and manuscript/figures/captions_v2.md. The v1 figures and the
earlier fig1_v2_atoms_mmi_ccs files are left in place.
Run from the repository root: .venv/bin/python scripts/15_figures_v2.py
"""
import csv
import pickle
import re
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.stats import f_oneway, pearsonr, spearmanr, t as t_dist

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "notes"))
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS
from rev_inference_inverted import signflip_inversion

RES, RR, FIG = REPO / "results", REPO / "notes" / "review_results", REPO / "manuscript" / "figures"
FIG.mkdir(exist_ok=True)
IX = {n: i for i, n in enumerate(ATOMS)}
PRE, POST = np.arange(0, 4), np.arange(5, 14)
SEED = 20261120
rng = np.random.default_rng(SEED)
# the SHA rule of the notes/ writers (notes/rev_git.py): -dirty only if scripts/, notes/*.py or the record have
# uncommitted changes. The whole-tree test used until 25 Sep 2026 would tag the captions of the final run -dirty,
# because by this last step of run_all.sh every regenerated output is a modified tracked file.
from rev_git import SHA as GIT
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 150, "savefig.dpi": 300})
C_OBS, C_PRED, C_DMT, C_PCB, C_RES, C_CCS = "#4C72B0", "#55A868", "#C44E52", "#4C72B0", "#8172B3", "#DD8452"
captions = ["# Figure captions (draft_v2)", "",
            f"Generated by `scripts/15_figures_v2.py` at git {GIT}, seed {SEED}. Every value is read from the saved results files named in the Source sentence that ends each caption; the main text carries each caption without that sentence.", ""]


def did_per_subject(A):
    """A: (14, 2, 14 windows[, k]) → per-subject primary DiD (post windows 6–14 minus pre 1–4, DMT minus placebo)."""
    ch = A[:, :, POST].mean(2) - A[:, :, PRE].mean(2)
    return ch[:, 0] - ch[:, 1]


def inv_ci(v):
    """B21's inverted sign-flip 95 % interval of the mean over subjects (notes/rev_inference_inverted.py)."""
    r = signflip_inversion(np.asarray(v, float))
    return r["lo"], r["hi"]


def ols(x, y):
    """OLS slope and intercept with t intervals on n − 2 df."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = x.size; X = np.c_[np.ones(n), x]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta; s2 = e @ e / (n - 2)
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    tq = t_dist.ppf(0.975, n - 2)
    return dict(b=beta[1], a=beta[0], b_lo=beta[1] - tq * se[1], b_hi=beta[1] + tq * se[1])


def fisher_ci(r, n=14):
    z = np.arctanh(r); h = 1.959964 / np.sqrt(n - 3)
    return np.tanh(z - h), np.tanh(z + h)


def table_line(path, startswith):
    for l in (RR / path).read_text().splitlines():
        if l.startswith(startswith):
            return l
    raise ValueError(f"no line starting {startswith!r} in {path}")


def num(s):
    return float(s.replace("−", "-").replace("+", ""))


def um(text):
    """Typographic minus for a signed number in running text (Python's formatting writes a hyphen)."""
    return re.sub(r"(?<![\w.])-(?=\d)", "−", text)


def save(fig, stem):
    fig.savefig(FIG / f"{stem}.png", bbox_inches="tight")
    fig.savefig(FIG / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)
    print("wrote", FIG / f"{stem}.png")


def caption(n, title, legend, source):
    """One caption: bold label and title, the legend, then the Source sentence (the text omits the last)."""
    assert "Source:" not in legend and title.endswith(".") and source.startswith("Source: ")
    captions.extend([f"## Fig {n}", "", f"**Fig {n}. {title}** {legend} {source}", ""])


# ------------------------------------------------------------------ Fig 1: scope map with the pooled pairs, the excess, and sts against c
STEP = 0.01   # the grid of the scope-map tables (notes/partB1_scope_map.md; Methods)


def grid(qlim):
    r1g = np.round(np.arange(0.0, 0.95 + 1e-9, STEP), 6); qg = np.round(np.arange(-qlim, qlim + 1e-9, STEP), 6)
    R1, Q = np.meshgrid(r1g, qg, indexing="ij")
    A = atoms_from_corr(ar1_corr(R1.ravel(), R1.ravel(), Q.ravel()))
    sts = A[:, IX["sts"]].reshape(R1.shape); selfp = (A[:, IX["xtx"]] + A[:, IX["yty"]]).reshape(R1.shape)
    return r1g, qg, R1, Q, sts, selfp


def coupling_rows(section_title):
    """Parse the matched-view table (c, sts) of one section of coupling_map_tables.md."""
    txt = (RR / "partB" / "coupling_map_tables.md").read_text()
    i = txt.index(section_title); j = txt.index("### Raw view", i)
    rows = [l for l in txt[i:j].splitlines() if l.startswith("| ") and not l.startswith("| c |")]
    c = np.array([float(l.split("|")[1]) for l in rows]); sts = np.array([float(l.split("|")[6]) for l in rows])
    return c, sts


r1g, qg, R1, Q, sts, selfp = grid(0.6)
ov = np.load(RR / "partB" / "scope_map_overlay_points.npz")
pool_r1 = np.concatenate([ov["pre_w1to4_r1"].ravel()]); pool_q = np.concatenate([ov["pre_w1to4_q"].ravel()])
fin = np.isfinite(pool_r1) & np.isfinite(pool_q); pool_r1, pool_q = pool_r1[fin], pool_q[fin]
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.1), constrained_layout=True)
ext = [qg[0], qg[-1], r1g[0], r1g[-1]]
im0 = axes[0].imshow(sts, origin="lower", extent=ext, aspect="auto", cmap="Blues")
fig.colorbar(im0, ax=axes[0], fraction=0.05, pad=0.02, label="sts (nats)")
LEVELS = [0.25, 0.5, 1.0, 1.5, 2.0]
cs0 = axes[0].contour(Q, R1, sts, levels=LEVELS, colors="k", linewidths=0.5)
# the orange density contours of the pairs occupy r₁ 0.79–0.93 at every q, where the 1, 1.5 and 2 nat contours run,
# so only the two levels below the density are labelled inline (at q = −0.45), and a note names all five levels
# (the review of 24 Sep 2026, item 20)
iq = int(np.argmin(np.abs(qg - (-0.45))))
label_pos = [(qg[iq], float(np.interp(lv, sts[:, iq], r1g))) for lv in LEVELS[:2]]
axes[0].clabel(cs0, levels=LEVELS[:2], fmt="%.2g", fontsize=6.5, manual=label_pos, inline_spacing=3)
axes[0].text(0.98, 0.03, "black contours: sts = 0.25, 0.5, 1, 1.5 and 2 nats, from the bottom", transform=axes[0].transAxes, ha="right", va="bottom", fontsize=6.5, color="0.2")
H, xe, ye = np.histogram2d(np.clip(pool_q, -0.6, 0.6), pool_r1, bins=[60, 48], range=[[-0.6, 0.6], [0.0, 0.95]])
axes[0].contour(0.5 * (xe[1:] + xe[:-1]), 0.5 * (ye[1:] + ye[:-1]), H.T, levels=np.percentile(H[H > 0], [50, 80, 95]), colors="#FF6F00", linewidths=0.8)
axes[0].scatter([0.25], [0.85], marker="x", color="black", s=50, lw=1.4, zorder=5)
axes[0].set_title("a  sts = −ln(1 − r₁²) + ½ ln(1 − r₁²q²); orange: the pre-injection pairs", loc="left", fontsize=8.5)
im1 = axes[1].imshow(sts - selfp, origin="lower", extent=ext, aspect="auto", cmap="Reds")
fig.colorbar(im1, ax=axes[1], fraction=0.05, pad=0.02, label="sts − (xtx + yty) = rtr (nats)")
axes[1].set_title("b  the excess of sts over self-prediction (= rtr, symmetric family)", loc="left", fontsize=8.5)
for ax in axes[:2]:
    ax.set_xlabel("q, lag-0 cross-correlation"); ax.set_ylabel("r₁, lag-1 autocorrelation")
cvals = {}
for title, lab, col in (("## (r1, q) held at (0.85, 0.25)", "(r₁, q) = (0.85, 0.25), the operating point", "black"),
                        ("## (r1, q) held at (0.85, 0.0)", "(0.85, 0.0)", "0.55"), ("## (r1, q) held at (0.6, 0.25)", "(0.6, 0.25)", "#4C72B0")):
    c, s_c = coupling_rows(title)
    cvals[lab] = (c, s_c)
    axes[2].plot(c, s_c, "-o", color=col, ms=4, lw=1.2, label=lab)
    if col == "black":   # the family is invariant under (c, q) → (−c, −q): the q = −0.25 curve is the mirror image
        axes[2].plot(-c, s_c, "--", marker="o", mfc="white", color=col, ms=4, lw=1.0, label="(0.85, −0.25), by (c, q) → (−c, −q)")
axes[2].axvline(0, color="0.8", lw=0.6)
axes[2].set_xlabel("c, symmetric lagged coupling of the VAR(1) pair"); axes[2].set_ylabel("sts (nats) at fixed (r₁, q)")
axes[2].set_title("c  coupling of the same sign as q lowers sts; of the opposite sign, raises it", loc="left", fontsize=8.5)
axes[2].legend(frameon=False, fontsize=7.5, loc="center", bbox_to_anchor=(0.55, 0.36))
save(fig, "fig1_v2_scope_map")
c_op, s_op = cvals["(r₁, q) = (0.85, 0.25), the operating point"]
row = lambda cv: s_op[np.argmin(np.abs(c_op - cv))]
caption(1, "The scope map and the coupled family.",
        f"(a) Gaussian-MMI sts of two AR(1) processes correlated only at lag 0, as a function of the pair's lag-1 autocorrelation r₁ and lag-0 cross-correlation q (closed form of Methods; grid step {STEP}), with the density of one subject's saved pre-injection pairs — the overlay holds subject 1 only (ts_gsr, the variant with global signal regression; windows 1–4 of both runs, {pool_r1.size:,} pair × window points; contours at the 50th, 80th and 95th percentiles of the occupied cells; r₁ = pair r₁, the mean of the pair's two lag-1 correlations in its window's 4 × 4 matrix, q = the pair's within-window lag-0 correlation; median r₁ {np.median(pool_r1):.3f}, median |q| {np.median(np.abs(pool_q)):.3f}) and the operating point (0.85, 0.25) marked; the black contours are sts = 0.25, 0.5, 1, 1.5 and 2 nats from the bottom (the two below the density are labelled inline). (b) sts − (xtx + yty), which on the symmetric family equals rtr and is zero at q = 0. (c) sts against the coupling c of the symmetric first-order vector autoregressive (VAR(1)) pair x_{{t+1}} = a x_t + c y_t + ε, y_{{t+1}} = a y_t + c x_t + η, with a and the innovation correlation re-solved at each c so that the pair's r₁ and q stay fixed. The four curves: (r₁, q) = (0.85, 0.25), the operating point, solid black; (0.85, 0), grey; (0.6, 0.25), blue; and, dashed with open markers, (0.85, −0.25), obtained from the family's invariance under (c, q) → (−c, −q). At the operating point sts is {row(0):.4f} at c = 0, {row(0.02):.4f} at +0.02, {row(0.05):.4f} at +0.05 and {row(0.10):.4f} at +0.10, and {row(-0.02):.4f} and {row(-0.05):.4f} at −0.02 and −0.05: coupling of the same sign as q lowers sts; of the opposite sign, raises it, and the response is not monotone.",
        "Source: `notes/rev_phiid_fast.py` (closed form), `notes/review_results/partB/scope_map_overlay_points.npz`, `notes/review_results/partB/coupling_map_tables.md` (matched view; partB8).")

# ------------------------------------------------------------------ Fig 2: observed against AR(1)-substituted atoms (B14)
fam = np.load(RR / "partB" / "family_atoms_ts_gsr_W60.npz")
obs16, pred16 = fam["obs"], fam["pred"]                                            # (14, 2, 14, 16)
order = ["rtr", "rtx", "rty", "xtr", "ytr", "xty", "ytx", "xtx", "yty", "rts", "str", "xts", "yts", "stx", "sty", "sts"]
groups = [("double\nredundancy", ["rtr"]), ("cross-prediction", ["rtx", "rty", "xtr", "ytr", "xty", "ytx"]), ("self-\nprediction", ["xtx", "yty"]),
          ("redundancy ↔\nsynergy", ["rts", "str"]), ("mirror atoms", ["xts", "yts", "stx", "sty"]), ("synergy", ["sts"])]
lvl_o, lvl_p = obs16[:, 0][:, PRE].mean((0, 1)), pred16[:, 0][:, PRE].mean((0, 1))
did_o = np.stack([did_per_subject(obs16[..., IX[a]]) for a in ATOMS], 1)             # (14 subjects, 16)
did_p = np.stack([did_per_subject(pred16[..., IX[a]]) for a in ATOMS], 1)
fig, axes = plt.subplots(2, 1, figsize=(8.6, 6.2), sharex=True, gridspec_kw=dict(hspace=0.12))
x = np.arange(16); wbar = 0.38
for ax, (vo, vp, ylab, title) in zip(axes, ((lvl_o, lvl_p, "atom value, DMT pre-injection (nats)", "a  level (windows 1–4, DMT run)"),
                                           (did_o.mean(0), did_p.mean(0), "primary DiD (nats)", "b  DMT − placebo, post − pre (windows 6–14 vs 1–4)"))):
    ax.bar(x - wbar / 2, [vo[IX[a]] for a in order], wbar, color=C_OBS, label="observed (MMI)")
    ax.bar(x + wbar / 2, [vp[IX[a]] for a in order], wbar, color=C_PRED, label="AR(1)-substituted, from each pair's ($a_x$, $a_y$, $q$)")
    if ylab.startswith("primary"):
        for k, a in enumerate(order):
            for off, d in ((-wbar / 2, did_o[:, IX[a]]), (wbar / 2, did_p[:, IX[a]])):
                lo, hi = inv_ci(d)
                ax.plot([x[k] + off] * 2, [lo, hi], color="black", lw=0.8)
    ax.axhline(0, color="black", lw=0.6)
    ax.set_ylabel(ylab); ax.set_title(title, loc="left", fontsize=9.5)
    for g0 in np.cumsum([len(g[1]) for g in groups])[:-1]:
        ax.axvline(g0 - 0.5, color="0.85", lw=0.8)
axes[0].legend(frameon=False, loc="upper left")
axes[1].set_xticks(x); axes[1].set_xticklabels(order)
pos = 0
for name, members in groups:
    axes[1].text(pos + (len(members) - 1) / 2, axes[1].get_ylim()[0] - 0.22 * np.diff(axes[1].get_ylim())[0], name, ha="center", va="top", fontsize=7.5, color="0.35")
    pos += len(members)
exc_o = lvl_o[IX["sts"]] - lvl_o[IX["xtx"]] - lvl_o[IX["yty"]]; exc_p = lvl_p[IX["sts"]] - lvl_p[IX["xtx"]] - lvl_p[IX["yty"]]
# the annotation sits at the left of panel (a), above the cross-prediction atoms, and its leader runs to the sts bar
# without crossing the text (the review of 24 Sep 2026, item 17); the asymmetry threshold is B23 (f)'s, S18 Table
axes[0].annotate(um(f"sts − (xtx + yty): observed {exc_o:+.3f},\nAR(1)-substituted {exc_p:+.3f} (the\nsymmetric family gives +rtr; unequal\ncoefficients make it negative beyond\nan asymmetry $|a_x - a_y|$ of 0.008\nat (0.85, 0.25))"),
                 xy=(15, lvl_o[IX["sts"]]), xytext=(0.4, 0.57), fontsize=7.5, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color="0.5", lw=0.6, shrinkA=4, shrinkB=2))
save(fig, "fig2_v2_atoms_observed_substituted")
res_lvl = lvl_o - lvl_p; res_did = did_o.mean(0) - did_p.mean(0)
# the caption's ranges over the four mirror atoms and the six cross-prediction atoms (the error-only check of 25 Sep 2026)
MIRROR, CROSS = ["xts", "yts", "stx", "sty"], ["rtx", "rty", "xtr", "ytr", "xty", "ytx"]
mir = [res_lvl[IX[a]] for a in MIRROR]; cr_res = [abs(res_lvl[IX[a]]) for a in CROSS]; cr_sub = [abs(lvl_p[IX[a]]) for a in CROSS]
caption(2, "The sixteen atoms, observed and AR(1)-substituted.",
        f"The sixteen Gaussian-MMI ΦID atoms of the whole-brain pair mean (6,555 pairs, 14 subjects, ts_gsr, windowed estimator W = 60), observed (blue) and AR(1)-substituted (green): the atoms of each pair's 4 × 4 matrix with its measured lag-1 autocorrelations a_x, a_y kept, its two lag-0 entries set to their mean q and its two cross-lag correlations replaced by a_y q and a_x q, evaluated per pair and window and averaged over pairs; the atoms are grouped by kind, as the annotations under the axis name them (the figure draws Table 1). (a) DMT pre-injection level (windows 1–4). (b) Primary difference-in-differences, DMT minus placebo, post (windows 6–14) minus pre (windows 1–4); whiskers are inverted sign-flip 95 % intervals of the mean over subjects (Methods). Panel (a) carries no uncertainty: its bars are group means of the level. Atom codes: first letter the past-side type, last letter the future-side type (r redundant, x unique to region X, y unique to Y, s synergistic; e.g. rts = redundancy-to-synergy). The AR(1)-substituted atoms reproduce the structure of the table: the excess sts − (xtx + yty) is negative in the data ({exc_o:+.4f}) and in the substituted atoms ({exc_p:+.4f}), as the family with unequal coefficients gives beyond an asymmetry |a_x − a_y| of 0.008 at (0.85, 0.25) (S18 Table); rts and str lie below xtx and yty; the four mirror atoms are negative. What the substitution leaves is the residual pattern of Table 1: sts {res_lvl[IX['sts']]:+.4f}, the self-prediction atoms {res_lvl[IX['xtx']]:+.4f} and {res_lvl[IX['yty']]:+.4f}, the mirror atoms {min(mir):+.4f} to {max(mir):+.4f}, the six cross-prediction atoms ±{min(cr_res):.4f} to ±{max(cr_res):.4f} where the substituted atoms are ±{min(cr_sub):.4f} to ±{max(cr_sub):.4f}; the residual DiDs of the other fifteen atoms are at most {np.abs(np.delete(res_did, IX['sts'])).max():.5f} in absolute value, against {res_did[IX['sts']]:+.4f} for sts.",
        "Source: `notes/review_results/partB/family_atoms_ts_gsr_W60.npz` (partB14); the asymmetry threshold from `notes/review_results/partB/diagnostic_alternatives_tables.md` (B23 (f)).")

# ------------------------------------------------------------------ Fig 3: per-subject scatters
def rows(f):
    return pickle.load(open(RR / f"inference_rows_{f}.pkl", "rb"))


def get(rs, label, st="primary"):
    return np.asarray([r for r in rs if r["label"] == label and r["set"] == st][0]["did_subjects"], float)


raw, diag = rows("raw"), rows("diag")
d_sts, d_ac = get(raw, "sts ts_gsr W60"), get(raw, "autocorr ts_gsr W60")
d_res = get(diag, "diag residual sts ts_gsr W60")
# the generators' rates within one simulation, per unit of pair r₁ (the mean of a pair's a_x and a_y)
BE = "partB/bandpassed_expectations_tables.md"
be_sts = num(table_line(BE, "| observed sts |").split("|")[2].split("±")[0])
be_res = num(table_line(BE, "| residual |").split("|")[2].split("±")[0])
be_a = num(table_line(BE, "| window-level mean pair r₁ |").split("|")[3].split("±")[0])
RATE_BP_STS, RATE_BP_RES = be_sts / be_a, be_res / be_a                                  # B24
da_i = [c.strip() for c in table_line("partB/diagnostic_alternatives_tables.md", "| (i) Δa = −0.015 |").split("|")]
RATE_AR1_STS = num(da_i[3].split("±")[0]) / num(da_i[6].split("±")[0])                   # B23 (b) (i)
RATE_AR1_RES = num(da_i[11])
nl = (RR / "logs" / "review_v2_residual_null.log").read_text()
wa = {k: float(re.search(k + r"\s*: window a=([0-9.]+)", nl).group(1)) for k in ("DMT pre", "DMT post", "PCB pre", "PCB post")}
null_a = (wa["DMT post"] - wa["DMT pre"]) - (wa["PCB post"] - wa["PCB pre"])
null_res = float(re.search(r"null residual change: .*DiD ([+-][0-9.]+)", nl).group(1))
RATE_NULL_RES = null_res / null_a                                                          # the finite-sample null
rsl = (RR / "partB" / "residual_source.log").read_text()
data_a = float(re.search(r"pair a: .*primary DiD ([+-][0-9.]+)", rsl).group(1))              # the data's pair r₁ DiD
sh = list(csv.reader(open(RR / "partB" / "splithalf_subjects.csv")))
shh = sh[1]; shb = [r for r in sh[2:] if r and r[0] == "ts_gsr"]
H = {k: np.array([float(r[shh.index(k)]) for r in shb]) for k in ("sts_odd", "sts_even", "r1_odd", "r1_even")}
r_oe, r_eo = pearsonr(H["r1_even"], H["sts_odd"])[0], pearsonr(H["r1_odd"], H["sts_even"])[0]
r_half = 0.5 * (r_oe + r_eo); half_lo, half_hi = fisher_ci(r_half)
dis = [c.strip() for c in table_line("partB/inference_revision_tables.md", "| ts_gsr | +").split("|")]   # (d): the disattenuated ratio
CEIL, DIS, DIS_CI = float(dis[7]), num(dis[8]), dis[9]
f_sts, f_res = ols(d_ac, d_sts), ols(d_ac, d_res)
r_full = pearsonr(d_ac, d_sts)[0]; full_lo, full_hi = fisher_ci(r_full)
SCALE_PCT = 100 * (abs(data_a) / abs(d_ac.mean()) - 1)                                     # pair r₁ against whole-brain r₁: the DiDs differ by this share
# index labels moved from their default place (3 pt right and up) so that each is nearer its own point than any
# other (the two nearly coincident pairs of (a), 13 and 5 and 7 and 12, labelled on opposite sides) and clear of the
# other labels and points and of the lines' crossing: in (a) subjects 1, 2, 3, 5, 6, 7, 10, 12 and 13; in (c)
# subjects 2, 11 and 12. A light backing keeps the digits legible where a line passes under them.
UL, LR, LL, LEFT, BELOW = ((-3, 3, "right", "baseline"), (3, -3, "left", "top"), (-3, -3, "right", "top"),
                           (-4, 0, "right", "center_baseline"), (0, -4, "center", "top"))
LABEL_AT = {(True, 13): UL, (True, 5): LR, (True, 7): LEFT, (True, 12): LR, (True, 1): LEFT, (True, 2): LR, (True, 3): LL,
            (True, 6): UL, (True, 10): LR, (False, 2): LEFT, (False, 11): BELOW, (False, 12): LR}
fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.1), gridspec_kw=dict(wspace=0.34))
for ax, (xv, yv, fit, rates, xl, yl, title) in zip((axes[0], axes[2]), (
        (d_ac, d_sts, f_sts, [(RATE_BP_STS, "band-passed generator", C_DMT, "--")],
         "whole-brain r₁ DiD", "MMI-sts DiD (nats)", "a  the sts contrast against the r₁ contrast"),
        (d_ac, d_res, f_res, [(RATE_BP_RES, "band-passed generator", C_DMT, "--"), (RATE_AR1_RES, "AR(1) pairs", C_OBS, ":"),
                              (RATE_NULL_RES, "finite-sample null", "0.45", "-.")],
         "whole-brain r₁ DiD", "residual DiD (nats)", "c  the residual against the r₁ contrast"))):
    xx = np.linspace(min(xv.min(), 0) - 0.002, max(xv.max(), 0) + 0.002, 20)
    ax.plot(xx, fit["a"] + fit["b"] * xx, color="0.25", lw=1.0, label=um(f"OLS fit: {fit['b']:+.2f} [{fit['b_lo']:+.2f}, {fit['b_hi']:+.2f}]"))
    for rate, lab, col, ls in rates:
        ax.plot(xx, rate * xx, color=col, lw=1.1, ls=ls, label=um(f"{lab}: {rate:+.2f}"))
    ax.scatter(xv, yv, s=28, color="0.15", zorder=3)
    for k in range(14):
        dx, dy, ha, va = LABEL_AT.get((ax is axes[0], k + 1), (3, 3, "left", "baseline"))
        ax.annotate(str(k + 1), (xv[k], yv[k]), xytext=(dx, dy), textcoords="offset points", fontsize=6.5, color="0.4",
                    ha=ha, va=va, bbox=dict(boxstyle="square,pad=0.05", fc="white", ec="none", alpha=0.75))
    ax.axhline(0, color="0.8", lw=0.6); ax.axvline(0, color="0.8", lw=0.6)
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title, loc="left", fontsize=9)
    ax.legend(frameon=False, fontsize=6.8, loc="lower right" if ax is axes[0] else "upper right", title="per unit of r₁ (generators: pair r₁)", title_fontsize=6.8)
axes[0].text(0.03, 0.95, f"r = {r_full:+.3f} [{full_lo:+.3f}, {full_hi:+.3f}], N = 14", transform=axes[0].transAxes, fontsize=8, va="top")
axes[2].set_ylim(top=0.075)
axes[1].plot(H["r1_even"], H["sts_odd"], ls="none", marker="o", ms=5.5, color="0.15", label=f"sts on odd windows, r₁ on even: r = {r_oe:+.3f}", zorder=3)
axes[1].plot(H["r1_odd"], H["sts_even"], ls="none", marker="^", ms=6, mfc="white", mec="0.15", label=f"sts on even windows, r₁ on odd: r = {r_eo:+.3f}", zorder=3)
axes[1].axhline(0, color="0.8", lw=0.6); axes[1].axvline(0, color="0.8", lw=0.6)
axes[1].set_xlabel("whole-brain r₁ DiD, one half of the windows"); axes[1].set_ylabel("MMI-sts DiD, the other half (nats)")
axes[1].set_title("b  the cross-half relation", loc="left", fontsize=9)
axes[1].set_ylim(top=0.26)
axes[1].legend(frameon=False, fontsize=6.8, loc="upper left", bbox_to_anchor=(0.0, 0.86), numpoints=1)
axes[1].text(0.03, 0.95, f"mean r = {r_half:+.3f} [{half_lo:+.3f}, {half_hi:+.3f}]\nceiling {CEIL:.3f}; disattenuated {DIS:+.3f} {DIS_CI}", transform=axes[1].transAxes, fontsize=7.0, va="top")
save(fig, "fig3_v2_per_subject")
caption(3, "Per-subject contrasts: sts against r₁, the cross-half relation, and the residual.",
        f"Per-subject difference-in-differences (post windows 6–14 minus pre windows 1–4, DMT minus placebo; ts_gsr, W = 60; one marker per subject, labelled by index in (a) and (c)). The x-axis of (a) and (c) is the whole-brain r₁ DiD. The generators' rates are per unit of pair r₁ and are drawn on the whole-brain-r₁ axis; the two DiDs differ by 6 % in the data ({data_a:+.4f} against {d_ac.mean():+.4f}), so the lines are placed to that accuracy; each rate is taken within one simulation and drawn through the origin. (a) Whole-brain MMI-sts DiD against the r₁ DiD: the OLS fit, {f_sts['b']:+.2f} per unit (t interval, 12 df, [{f_sts['b_lo']:+.2f}, {f_sts['b_hi']:+.2f}]; intercept {f_sts['a']:+.3f}), and the band-passed generator's rate, {RATE_BP_STS:.2f} per unit of pair r₁ ({be_sts:+.5f} / {be_a:+.5f}; the second computation of the pure-autocorrelation expectations, S18 Table); r = {r_full:+.3f}, Fisher-z 95 % interval [{full_lo:+.3f}, {full_hi:+.3f}]. Both DiDs are read off the same windows, so r includes estimation error they share. (b) The cross-half relation: each subject's sts DiD on the odd windows against its r₁ DiD on the even windows (filled circles, r = {r_oe:+.3f}) and the sts DiD on the even windows against the r₁ DiD on the odd windows (open triangles, r = {r_eo:+.3f}); mean r = {r_half:+.3f}, Fisher-z interval of the mean [{half_lo:+.3f}, {half_hi:+.3f}] (an approximation), against a ceiling of {CEIL:.3f} set by the two halves' split-half reliabilities; disattenuated, {DIS:+.3f} {DIS_CI} (subject bootstrap; S3 Text §5). (c) The residual DiD (observed minus AR(1)-substituted sts) against the r₁ DiD: the OLS fit, {f_res['b']:+.2f} per unit (t interval [{f_res['b_lo']:+.2f}, {f_res['b_hi']:+.2f}]; intercept {f_res['a']:+.4f}), and the rates of the band-passed generator ({RATE_BP_RES:+.2f}; S18 Table), of AR(1) pairs ({RATE_AR1_RES:+.2f}; the AR(1) generator, S18 Table) and of the finite-sample null ({RATE_NULL_RES:+.2f}: {null_res:+.4f} / {null_a:+.4f}; Methods), per unit of pair r₁; on that basis the data's group means give {d_res.mean() / data_a:+.2f} ({d_res.mean():+.4f} / {data_a:+.4f}).",
        "Source: `notes/review_results/inference_rows_raw.pkl` and `inference_rows_diag.pkl` (field `did_subjects`, primary set); `notes/review_results/partB/splithalf_subjects.csv`, `inference_revision_tables.md` (d), `bandpassed_expectations_tables.md` (B24), `diagnostic_alternatives_tables.md` (b; B23), `residual_source.log`; `notes/review_results/logs/review_v2_residual_null.log`.")

# ------------------------------------------------------------------ Fig 4: the regional map, the partialled contrast (B20) and the residual map's network means (B22 (e))
reg = list(csv.reader(open(RR / "partB" / "regional_partial.csv")))
hdr = reg[1]; body = [r for r in reg[2:] if r]
col = {k: hdr.index(k) for k in hdr}
net = np.array([r[col["network"]] for r in body])
sts_r = np.array([float(r[col["sts"]]) for r in body]); smr_r = np.array([float(r[col["sts_minus_rtr"]]) for r in body])
r1_r = np.array([float(r[col["r1_windowed"]]) for r in body])
sts_res = np.array([float(r[col["sts_resid_win"]]) for r in body]); smr_res = np.array([float(r[col["smr_resid_win"]]) for r in body])
NETS = ["Vis", "SomMot", "DorsAttn", "SalVentAttn", "Limbic", "Cont", "Default", "Subcortex"]
NETCOL = {"Vis": "#781286", "SomMot": "#4682B4", "DorsAttn": "#00760E", "SalVentAttn": "#C43AFA", "Limbic": "#DCF8A4", "Cont": "#E69422", "Default": "#CD3E4E", "Subcortex": "0.4"}
sens = np.isin(net, ["Vis", "SomMot"]); assoc = np.isin(net, ["Default", "Cont"])
fig, axes = plt.subplots(1, 3, figsize=(15.6, 4.0), gridspec_kw=dict(wspace=0.32, width_ratios=[1.35, 1, 1.25]))
for n in NETS:
    m = net == n
    axes[0].scatter(r1_r[m], sts_r[m], s=22, color=NETCOL[n], edgecolor="0.3" if n == "Limbic" else "none", lw=0.4, label=f"{n} ({int(m.sum())})", zorder=3)
b = np.polyfit(r1_r, sts_r, 1); xx = np.linspace(r1_r.min(), r1_r.max(), 10)
axes[0].plot(xx, np.polyval(b, xx), color="0.5", lw=0.9)
r_reg = pearsonr(r1_r, sts_r)[0]
axes[0].text(0.03, 0.95, f"r = {r_reg:+.3f}, slope {b[0]:+.2f} nats per unit r₁ (115 regions)", transform=axes[0].transAxes, fontsize=8, va="top")
axes[0].set_xlabel("regional lag-1 autocorrelation r₁ (placebo, windows 1–4)"); axes[0].set_ylabel("regional MMI-sts (placebo, bins 1–8; nats)")
axes[0].set_title("a  regional synergy against regional autocorrelation", loc="left", fontsize=9)
axes[0].legend(frameon=False, fontsize=6.8, loc="lower right", ncol=2, markerscale=1.1)
contr = [(sts_r[sens].mean() - sts_r[assoc].mean(), sts_res[sens].mean() - sts_res[assoc].mean()), (smr_r[sens].mean() - smr_r[assoc].mean(), smr_res[sens].mean() - smr_res[assoc].mean())]
xb = np.arange(2); wb = 0.36
axes[1].bar(xb - wb / 2, [c[0] for c in contr], wb, color="0.35", label="before partialling")
axes[1].bar(xb + wb / 2, [c[1] for c in contr], wb, color=C_PRED, label="after partialling regional r₁ out")
axes[1].axhline(0, color="k", lw=0.6)
axes[1].set_xticks(xb); axes[1].set_xticklabels(["sts", "sts − rtr"])
axes[1].set_ylabel("sensory − association contrast (nats)")
axes[1].set_title("b  the sensory–association contrast of the group map", loc="left", fontsize=9)
axes[1].set_ylim(-0.026, 0.013)
axes[1].legend(frameon=False, fontsize=7.5, loc="upper right")
for k, c in enumerate(contr):
    axes[1].text(xb[k] - wb / 2, c[0] - 0.0012, um(f"{c[0]:+.4f}"), ha="center", va="top", fontsize=7); axes[1].text(xb[k] + wb / 2, c[1] + 0.0008 if c[1] >= 0 else c[1] - 0.0012, um(f"{c[1]:+.4f}"), ha="center", va="bottom" if c[1] >= 0 else "top", fontsize=7)
AD = "partB/aligned_directed_tables.md"
spin = {}
for key, start in (("map", "| sts (unpartialled) |"), ("res", "| sts with regional r₁ partialled out (sts_resid_win) |")):
    cells = [c.strip() for c in table_line(AD, start).split("|")]
    spin[key] = dict(F=float(cells[2]), p=float(cells[3]), sm=num(cells[4]), sm_p=float(cells[5]), vd=num(cells[6]), vd_p=float(cells[7]), n_rot=int(cells[8]))
F_res = f_oneway(*[sts_res[net == n] for n in NETS]).statistic; F_map = f_oneway(*[sts_r[net == n] for n in NETS]).statistic
assert abs(F_res - spin["res"]["F"]) < 5e-4 and abs(F_map - spin["map"]["F"]) < 5e-4, "F differs from aligned_directed_tables.md (e)"
nm = np.array([sts_res[net == n].mean() for n in NETS]); nse = np.array([sts_res[net == n].std(ddof=1) / np.sqrt((net == n).sum()) for n in NETS])
xn = np.arange(len(NETS))
axes[2].bar(xn, nm, 0.7, yerr=nse, color=[NETCOL[n] for n in NETS], edgecolor=["0.3" if n == "Limbic" else "none" for n in NETS], lw=0.4, capsize=2, error_kw=dict(lw=0.7))
axes[2].axhline(0, color="k", lw=0.6)
axes[2].set_xticks(xn); axes[2].set_xticklabels([f"{n} ({int((net == n).sum())})" for n in NETS], fontsize=7, rotation=40, ha="right", rotation_mode="anchor")
axes[2].set_ylim(-0.033, 0.06)
axes[2].set_ylabel("residual map, network mean ± SEM (nats)")
axes[2].set_title("c  the residual map's network means", loc="left", fontsize=9)
axes[2].text(0.02, 0.97, um(f"eight-class F = {spin['res']['F']:.2f}, spin p = {spin['res']['p']:.4f}\n(unpartialled map: F = {spin['map']['F']:.2f}, spin p = {spin['map']['p']:.4f})\n"
             f"SomMot − Default {spin['res']['sm']:+.5f}, spin p = {spin['res']['sm_p']:.2f}\nVis − Default {spin['res']['vd']:+.5f}, spin p = {spin['res']['vd_p']:.2f}"),
             transform=axes[2].transAxes, fontsize=7, va="top")
save(fig, "fig4_v2_regional")
caption(4, "The regional map and regional autocorrelation.",
        f"Placebo run, pre-injection, ts_gsr, 115 regions, group means over 14 subjects. (a) Regional MMI-sts — the mean over a region's 114 pairs of the global-fit local sts, bins 1–8 — against the region's lag-1 autocorrelation r₁ (W = 60, windows 1–4), coloured by Yeo-7 network with the 16 subcortical parcels as one class (parcel counts in the legend); Pearson r = {r_reg:+.3f}, least-squares slope {b[0]:+.2f} nats per unit r₁. (b) The pre-defined contrast between sensory cortex (visual and somatomotor networks, {int(sens.sum())} parcels) and association cortex (default-mode and frontoparietal control networks, {int(assoc.sum())} parcels) of the sts map and of the sts − rtr map, before partialling (grey) and after regressing regional r₁ out of the group map (green): sts {contr[0][0]:+.4f} → {contr[0][1]:+.4f} nats, sts − rtr {contr[1][0]:+.4f} → {contr[1][1]:+.4f}; the per-subject version with its t intervals is in Results 3. (c) The network means of the map with regional r₁ partialled out (± standard error of the mean, SEM, over the network's parcels; parcel counts under the labels), from {nm.min():+.4f} ({NETS[int(np.argmin(nm))]}) to {nm.max():+.4f} ({NETS[int(np.argmax(nm))]}), and the spin test of their structure (the spin test of S3 Text §4; {spin['res']['n_rot']:,} rotations of the cortical parcels, each keeping its own class, the 16 subcortical values fixed): the eight-class one-way F is {spin['res']['F']:.3f}, spin p {spin['res']['p']:.4f}, against {spin['map']['F']:.3f}, spin p {spin['map']['p']:.4f}, for the unpartialled map; the residual map's somatomotor − default and visual − default contrasts are {spin['res']['sm']:+.5f} (spin p {spin['res']['sm_p']:.4f}) and {spin['res']['vd']:+.5f} ({spin['res']['vd_p']:.4f}). Partialling removes the pre-defined sensory–association contrast at its point estimate but not all network structure.",
        "Source: `notes/review_results/partB/regional_partial.csv` (partB20); `notes/review_results/partB/aligned_directed_tables.md` (B22 (e)).")

# ------------------------------------------------------------------ Fig 5: the AR(1)-substituted estimate by window, with the expectation under a pure autocorrelation change
z = np.load(RR / "partB" / "diag_series_ts_gsr_W60.npz")
obs, pred, res = z["obs"], z["pred"], z["res"]                                   # (14, 2, 14)
t = (np.arange(14) + 0.5) * 2.0                                                  # window centre, minutes


def within_sem(A):
    """Cousineau–Morey within-subject SEM per cell of A (subjects first): each subject's cells are centred on that
    subject's own mean (the between-subject spread of the level, which the paper does not test, is removed), the
    grand mean is added back, the SEM across subjects is taken per cell and multiplied by Morey's factor
    sqrt(M / (M − 1)) for M cells per subject."""
    M = int(np.prod(A.shape[1:]))
    norm = A - A.mean(axis=tuple(range(1, A.ndim)), keepdims=True) + A.mean()
    return norm.std(0, ddof=1) / np.sqrt(A.shape[0]) * np.sqrt(M / (M - 1))


def calibrated_expectation():
    """The residual DiD expected under a pure autocorrelation change at W = 60: condition (i) of the band-passed
    calibration (partB17b) when its table is present, otherwise of the AR(1) calibration (partB17)."""
    for fname, gen, src in (("calibration_filtered_tables.md", "band-passed generator, S10 Table", "partB17b, `calibration_filtered_tables.md`"),
                            ("calibration_tables.md", "AR(1) pairs, S10 Table", "partB17, `calibration_tables.md`")):
        f = RR / "partB" / fname
        if f.exists():
            for l in f.read_text().splitlines():
                if l.startswith("| (i)") and "| W60 |" in l:
                    cells = [c.strip() for c in l.split("|")]
                    m = re.match(r"([+-]\d+\.\d+) ± (\d+\.\d+)", cells[6])
                    return float(m.group(1)), float(m.group(2)), gen, src
    return np.nan, np.nan, "none", "none"


EXP, EXP_SD, EXP_SRC, EXP_FILE = calibrated_expectation()
P_EXP = [float(table_line("partB/inference_revision_tables.md", f"| {e} |").split("|")[2]) for e in ("+0.0027", "+0.0049", "+0.0054")]   # B21 (b)
YL_A, YL_B = (1.00, 1.30), (-0.15, 0.05)                                          # 0.30 and 0.20 nats: equal scale at height ratio 1.5 : 1
YL_C = (-0.04, 0.06)                                                             # the legend sits below the axis
fig, axes = plt.subplots(3, 1, figsize=(7.8, 9.8), sharex=True, gridspec_kw=dict(hspace=0.22, height_ratios=[YL_A[1] - YL_A[0], YL_B[1] - YL_B[0], YL_C[1] - YL_C[0]]))
for ax in axes:
    ax.axvspan(0, 8, color="0.92", zorder=0); ax.axvspan(8, 10, facecolor="none", hatch="///", edgecolor="0.6", lw=0, zorder=0)
    ax.axvline(8, color="k", ls="--", lw=0.8)
se_obs, se_pred, se_res = within_sem(obs), within_sem(pred), within_sem(res)
for c, cname, col in ((0, "DMT", C_DMT), (1, "placebo", C_PCB)):
    for arr, se, ls, lab in ((obs, se_obs, "-", "observed"), (pred, se_pred, "--", "AR(1)-substituted")):
        m = arr[:, c].mean(0)
        axes[0].plot(t, m, ls=ls, color=col, lw=1.4, label=f"{cname}, {lab}")
        axes[0].fill_between(t, m - se[c], m + se[c], color=col, alpha=0.15 if ls == "-" else 0.10, lw=0)
    m = res[:, c].mean(0)
    axes[1].plot(t, m, color=col, lw=1.4, label=f"{cname}, residual = observed − AR(1)-substituted"); axes[1].fill_between(t, m - se_res[c], m + se_res[c], color=col, alpha=0.15, lw=0)
diff = res[:, 0] - res[:, 1]                                                     # (14 subjects, 14 windows): DMT − placebo residual difference
se_diff = within_sem(diff)
m = diff.mean(0)
axes[2].plot(t, m, color=C_RES, lw=1.4, label="DMT − placebo residual difference (± 1 within-subject SEM)"); axes[2].fill_between(t, m - se_diff, m + se_diff, color=C_RES, alpha=0.18, lw=0)
pre_level = m[PRE].mean()
step = np.where(np.arange(14) >= 5, pre_level + EXP, pre_level)
axes[2].step(np.r_[0, t + 1.0], np.r_[step[0], step], where="pre", color="k", ls="--", lw=1.0, label=um(f"expectation under a pure autocorrelation change: pre-injection mean, then {EXP:+.4f} ({EXP_SRC})"))
# the calibration's ±1 replicate SD as an error bar at each post-injection window centre (the review of 24 Sep 2026, item 18)
axes[2].errorbar(t[5:], np.full(9, pre_level + EXP), yerr=EXP_SD, fmt="none", ecolor="k", elinewidth=0.9, capsize=2.5, capthick=0.9, label=um(f"the calibration's ±1 replicate SD (±{EXP_SD:.4f})"))
axes[0].set_ylim(*YL_A); axes[1].set_ylim(*YL_B); axes[2].set_ylim(*YL_C)
axes[0].set_ylabel("whole-brain mean sts (nats)"); axes[1].set_ylabel("residual (nats)"); axes[2].set_ylabel("DMT − placebo residual (nats)", fontsize=8); axes[2].set_xlabel("time in scan (min)")
axes[0].set_title("a  observed sts and the AR(1)-substituted estimate from each pair's measured ($a_x$, $a_y$, $q$)", loc="left", fontsize=9)
axes[1].set_title("b  the residual (same units as a; same nats per unit height)", loc="left", fontsize=9)
axes[2].set_title("c  the DMT − placebo residual difference against its expectation under a pure autocorrelation change", loc="left", fontsize=9)
axes[0].legend(frameon=False, fontsize=7.5, ncol=2, loc="lower right")
axes[1].legend(frameon=False, fontsize=7.5, loc="upper right", bbox_to_anchor=(1.0, 0.36))
axes[2].legend(frameon=False, fontsize=7.0, loc="upper left", bbox_to_anchor=(0.0, -0.42), borderaxespad=0.0)
axes[1].axhline(0, color="k", lw=0.5); axes[2].axhline(0, color="k", lw=0.5)
save(fig, "fig5_v2_residual_diagnostic")
did_o, did_p, did_r = did_per_subject(obs).mean(), did_per_subject(pred).mean(), did_per_subject(res).mean()
caption(5, "The AR(1)-substituted estimate by window.",
        f"ts_gsr, W = 60, N = 14; lines are group means. Shading is ± 1 within-subject SEM (Cousineau, 2005; Morey, 2008): each subject's values are centred on that subject's own mean before the SEM across subjects is taken, with Morey's correction, so the bands show the uncertainty of within-subject comparisons across windows and runs and not the between-subject spread of the level, which the paper does not test; the same band is drawn on the dashed lines of (a). Grey band = pre-injection windows 1–4; hatched = window 5, excluded from the primary post set; dashed vertical line = injection at 8 min. (a) Observed whole-brain sts (solid) and the AR(1)-substituted sts (dashed): the sts of each pair's 4 × 4 matrix with its measured lag-1 autocorrelations a_x, a_y kept, its two lag-0 entries set to their mean q and its two cross-lag correlations replaced by a_y q and a_x q; DMT (red) and placebo (blue); y-range {YL_A[0]:.2f}–{YL_A[1]:.2f} nats. (b) The residual, observed minus AR(1)-substituted, per run, in the same units as (a) and with the same nats per unit height, so that the residual's modulation can be read against the size of the level and of the contrast. The AR(1)-substituted estimate exceeds the observed level by {abs(res.mean()):.3f} nats on average, and its primary DiD is larger in size by {abs(did_p) - abs(did_o):.4f} nats (observed {did_o:+.4f}, AR(1)-substituted {did_p:+.4f}, residual DiD {did_r:+.4f}). (c) The DMT − placebo difference of the residual per window (mean over subjects ± 1 within-subject SEM), with its expectation under a pure autocorrelation change as the dashed step: the pre-injection mean of the difference, then that mean plus the residual DiD that the calibration gives for an autocorrelation change of the data's size ({EXP:+.4f} ± {EXP_SD:.4f}, condition (i) at W = 60 on the {EXP_SRC}); the error bars at the post-injection window centres are the calibration's ± 1 replicate SD over its replicate datasets. The dashed step, not zero, is the reference for reading the difference, because a pure autocorrelation change itself produces a positive residual DiD; Results 4 gives the data's exact sign-flip p against this and the two other expectations, +0.0049 and +0.0054 ({P_EXP[0]:.3f}, {P_EXP[1]:.3f} and {P_EXP[2]:.3f}).",
        f"Source: `notes/review_results/partB/diag_series_ts_gsr_W60.npz`; the expectation from `notes/review_results/partB/calibration_filtered_tables.md` when present, otherwise `calibration_tables.md` (here {EXP_FILE}); the p values from `inference_revision_tables.md` (b; B21).")

# ------------------------------------------------------------------ Fig 6: lag dependence (S14 Table)
lag = rows("lag")
TAUS = (1, 2, 3, 5)
L = {}
for tau in TAUS:
    s = [r for r in lag if r["label"] == f"sts tau{tau} ts_gsr W60" and r["set"] == "primary"][0]
    a = [r for r in lag if r["label"] == f"autocorr lag{tau} ts_gsr W60" and r["set"] == "primary"][0]
    L[tau] = dict(sts=s, ac=a, r=pearsonr(np.asarray(s["did_subjects"], float), np.asarray(a["did_subjects"], float))[0],
                  ci=dict(sts=inv_ci(s["did_subjects"]), ac=inv_ci(a["did_subjects"])))
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.7), gridspec_kw=dict(wspace=0.32, bottom=0.2))
xt = np.arange(len(TAUS))
for ax, key, col, ylab, title in ((axes[0], "sts", C_OBS, "MMI-sts DiD, W = 60 (nats)", "a  the sts contrast against the lag τ"),
                                  (axes[1], "ac", C_RES, "mean lag-τ autocorrelation DiD", "b  the lag-τ autocorrelation contrast")):
    v = np.array([L[tau][key]["did"] for tau in TAUS]); lo = np.array([L[tau]["ci"][key][0] for tau in TAUS]); hi = np.array([L[tau]["ci"][key][1] for tau in TAUS])
    ax.errorbar(xt, v, yerr=[v - lo, hi - v], fmt="o", color=col, capsize=3, lw=1.2, ms=5, zorder=3)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xticks(xt); ax.set_xticklabels([um(f"τ = {tau}\n$r_\\tau$ {L[tau]['ac']['pre_dmt']:+.2f}") for tau in TAUS], fontsize=8)
    ax.set_xlim(-0.6, len(TAUS) - 0.4)
    ax.set_ylabel(ylab); ax.set_title(title, loc="left", fontsize=9)
axes[0].text(0.98, 0.04, um("per-subject r(sts DiD, $r_\\tau$ DiD), N = 14:\n" + ", ".join(f"{L[tau]['r']:+.2f}" for tau in TAUS) + "  (τ = " + ", ".join(str(tau) for tau in TAUS) + ")"),
             transform=axes[0].transAxes, ha="right", va="bottom", fontsize=7.5, color="0.3")
save(fig, "fig6_v2_lag_dependence")
# the caption's reading of the whiskers, asserted so that a rerun cannot silently contradict it (the error-only check of 25 Sep 2026)
assert all(L[t]["ci"][k][1] < 0 for t in (1, 2, 3) for k in ("ac", "sts")) and all(L[5]["ci"][k][0] < 0 < L[5]["ci"][k][1] for k in ("ac", "sts"))
caption(6, "Lag dependence.",
        "S14 Table; ts_gsr, W = 60, N = 14; points are group-mean primary DiDs, DMT minus placebo, post windows 6–14 minus pre 1–4; whiskers are inverted sign-flip 95 % intervals of the mean over subjects (Methods); the exact p of every point is in S14 Table. (a) The whole-brain MMI-sts DiD at τ = "
        + ", ".join(f"{tau} ({L[tau]['sts']['did']:+.4f})" for tau in TAUS) + " nats, with r, the per-subject correlation between the sts DiD and the lag-τ autocorrelation DiD ("
        + ", ".join(f"{L[tau]['r']:+.3f}" for tau in TAUS) + "). (b) The whole-brain lag-τ autocorrelation DiD at the same lags ("
        + ", ".join(f"{L[tau]['ac']['did']:+.4f}" for tau in TAUS) + "); the x-axis labels give the DMT pre-injection mean r_τ (windows 1–4). Where the interval of the lag-τ autocorrelation contrast excludes zero (τ = 1, 2, 3), the sts contrast is negative and its interval excludes zero too; at τ = 5, where the autocorrelation contrast's interval includes zero (p = "
        + f"{L[5]['ac']['did_p']:.2f}), so does the sts contrast's (p = {L[5]['sts']['did_p']:.2f});"
        + " the r_τ DiD grows in size with τ up to τ = 3 while the sts DiD shrinks with the atom, and at τ = 3 the per-subject tracking is only partial (Results 5). A longer lag reduces everything, the artefact included.",
        "Source: `notes/review_results/inference_rows_lag.pkl` (rows `sts tauN ts_gsr W60` and `autocorr lagN ts_gsr W60`, primary set).")

(FIG / "captions_v2.md").write_text(um("\n".join(captions)) + "\n")
print("wrote", FIG / "captions_v2.md")
