"""
partB14_family_atoms.py — B14: the family-predicted sixteen atoms per pair (asymmetric diagonal family).
Pre-run entry: manuscript/analysis_record.md, "Family-predicted sixteen atoms per pair (B14): pre-run entry,
20 Sep 2026" (specification, prediction and rule as in notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5).

For every subject, run and W = 60 window, and for each of the 6,555 pairs: the window's PairPhiID matrices give
the observed sixteen MMI atoms (atoms_mean) and the measured (a_x, a_y, q) exactly as partB4_diagnostic.py takes
them (a_x = C[0, 2], a_y = C[1, 3], q = mean of C[0, 1] and C[2, 3]); rev_phiid_fast.atoms_from_corr(ar1_corr(a_x,
a_y, q)) gives the predicted sixteen; both averaged over pairs. Global fit: the run-level (a_x, a_y, q) give one
prediction per run, constant across its 28 bins (levels only; the predicted DiD is zero by construction).
Free choices: variants ts_gsr and ts_demean; W = 60 windows 1–14 (window 5 excluded from the DiD as everywhere);
levels = DMT pre-injection windows 1–4, mean over subjects and windows; primary DiD = windows 6–14 minus 1–4,
DMT minus placebo, per subject, mean over subjects; region 20 excluded; non-finite TRs dropped as scripts/01 drops
them. Seed 20261120 (no random draws).
Outputs (notes/review_results/partB/): family_atoms_tables.md, family_atoms_<variant>_W60.npz (obs, pred:
(14, 2, 14, 16)), family_atoms_ts_gsr_W60.csv (one row per atom), family_atoms_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB14_family_atoms.py   (about the time of partB4)
"""
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
SEED = 20261120
PRE, POST = np.arange(0, 4), np.arange(5, 14)
PRE_B, POST_B = np.arange(0, 8), np.arange(10, 28)
MIRRORS = ("xts", "yts", "stx", "sty")
t0 = time.time()
ts = sio.loadmat(MAT)


def did(x):
    """x (14, 2, n_win, ...) → per-subject DiD (14, ...): (post − pre)_DMT − (post − pre)_PCB."""
    ch = x[:, :, POST].mean(2) - x[:, :, PRE].mean(2)
    return ch[:, 0] - ch[:, 1]


def fmt_did(d):
    return f"{d.mean():+.4f} ({int((d < 0).sum())})"


lines = ["# Family-predicted sixteen atoms per pair, asymmetric diagonal family (partB14_family_atoms.py)", f"git={SHA}", "",
         "Per window and pair: observed MMI atoms (PairPhiID.atoms_mean) and predicted atoms atoms_from_corr(ar1_corr(a_x, a_y, q)) from the window's "
         "measured (a_x, a_y, q), averaged over the 6,555 pairs; level = DMT windows 1–4, DiD = windows 6–14 minus 1–4, DMT minus placebo "
         f"(mean over 14 subjects; in brackets the number of subjects with a negative DiD). W = 60; seed {SEED}; region 20 excluded.", ""]
summary = {}
for var in ("ts_gsr", "ts_demean"):
    obs = np.full((14, 2, 14, 16), np.nan); pred = np.full((14, 2, 14, 16), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            for w in range(14):
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]
                q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
                obs[s, c, w] = pp.atoms_mean().mean(0)
                pred[s, c, w] = atoms_from_corr(ar1_corr(ax, ay, q)).mean(0)
        print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    np.savez(OUT / f"family_atoms_{var}_W60.npz", obs=obs, pred=pred)
    res = obs - pred
    lvl_o, lvl_p = obs[:, 0, PRE].mean((0, 1)), pred[:, 0, PRE].mean((0, 1))
    d_o, d_p = did(obs), did(pred)
    d_r = d_o - d_p
    lines += [f"## {var}, W = 60: Table 1's columns with the family-predicted atoms", "",
              "| atom | observed level | predicted level | residual level | observed DiD (neg/14) | predicted DiD (neg/14) | residual DiD (neg/14) |",
              "|---|---|---|---|---|---|---|"]
    rows_csv = ["atom,observed_level,predicted_level,residual_level,observed_did,predicted_did,residual_did,observed_did_neg,predicted_did_neg,residual_did_neg"]
    for a, n in enumerate(ATOMS):
        lines.append(f"| {n} | {lvl_o[a]:+.4f} | {lvl_p[a]:+.4f} | {lvl_o[a] - lvl_p[a]:+.4f} | {fmt_did(d_o[:, a])} | {fmt_did(d_p[:, a])} | {fmt_did(d_r[:, a])} |")
        rows_csv.append(f"{n},{lvl_o[a]:.6f},{lvl_p[a]:.6f},{lvl_o[a] - lvl_p[a]:.6f},{d_o[:, a].mean():.6f},{d_p[:, a].mean():.6f},{d_r[:, a].mean():.6f},"
                        f"{int((d_o[:, a] < 0).sum())},{int((d_p[:, a] < 0).sum())},{int((d_r[:, a] < 0).sum())}")
    lines.append(f"| TDMI (sum) | {lvl_o.sum():+.4f} | {lvl_p.sum():+.4f} | {lvl_o.sum() - lvl_p.sum():+.4f} | {fmt_did(d_o.sum(1))} | {fmt_did(d_p.sum(1))} | {fmt_did(d_r.sum(1))} |")
    if var == "ts_gsr":
        (OUT / "family_atoms_ts_gsr_W60.csv").write_text(f"# partB14_family_atoms.py; ts_gsr W60; level = DMT windows 1–4; DiD = windows 6–14 minus 1–4, DMT minus placebo; git={SHA}\n" + "\n".join(rows_csv) + "\n")
    # the checks of the pre-run entry
    ex_o = lvl_o[IX["sts"]] - (lvl_o[IX["xtx"]] + lvl_o[IX["yty"]])
    ex_p = lvl_p[IX["sts"]] - (lvl_p[IX["xtx"]] + lvl_p[IX["yty"]])
    order_p = (lvl_p[IX["rts"]] < lvl_p[IX["xtx"]]) and (lvl_p[IX["rts"]] < lvl_p[IX["yty"]]) and (lvl_p[IX["str"]] < lvl_p[IX["xtx"]]) and (lvl_p[IX["str"]] < lvl_p[IX["yty"]])
    order_o = (lvl_o[IX["rts"]] < lvl_o[IX["xtx"]]) and (lvl_o[IX["rts"]] < lvl_o[IX["yty"]]) and (lvl_o[IX["str"]] < lvl_o[IX["xtx"]]) and (lvl_o[IX["str"]] < lvl_o[IX["yty"]])
    mir_p = np.array([lvl_p[IX[m]] for m in MIRRORS]); mir_o = np.array([lvl_o[IX[m]] for m in MIRRORS])
    # symmetric-a prediction for reference (as partB4's pred_sym), whole-brain level, DMT windows 1–4
    lines += ["", f"Excess sts − (xtx + yty), DMT windows 1–4: observed {ex_o:+.4f}; family-predicted from each pair's (a_x, a_y, q) {ex_p:+.4f}; rtr observed {lvl_o[IX['rtr']]:+.4f}, predicted {lvl_p[IX['rtr']]:+.4f}.",
              f"Ordering rts = str below xtx, yty: predicted {'yes' if order_p else 'no'} (rts {lvl_p[IX['rts']]:+.4f}, str {lvl_p[IX['str']]:+.4f}, xtx {lvl_p[IX['xtx']]:+.4f}, yty {lvl_p[IX['yty']]:+.4f}); "
              f"observed {'yes' if order_o else 'no'} (rts {lvl_o[IX['rts']]:+.4f}, str {lvl_o[IX['str']]:+.4f}, xtx {lvl_o[IX['xtx']]:+.4f}, yty {lvl_o[IX['yty']]:+.4f}).",
              f"Mirror atoms (xts, yts, stx, sty): predicted {np.array2string(mir_p, precision=4, floatmode='fixed')} against −rts predicted {-lvl_p[IX['rts']]:+.4f}; observed {np.array2string(mir_o, precision=4, floatmode='fixed')} against −rts observed {-lvl_o[IX['rts']]:+.4f}.",
              f"sts residual, all subjects, runs and windows: {np.nanmean(res[..., IX['sts']]):+.4f} (the diagnostic's, diag_tables.md: −0.0489 on ts_gsr); observed sts level {lvl_o[IX['sts']]:.4f}, predicted {lvl_p[IX['sts']]:.4f}; "
              f"sts DiD observed {d_o[:, IX['sts']].mean():+.4f}, predicted {d_p[:, IX['sts']].mean():+.4f}, residual {d_r[:, IX['sts']].mean():+.4f}.",
              f"Largest |residual level| over the sixteen atoms: {ATOMS[int(np.argmax(np.abs(lvl_o - lvl_p)))]} ({(lvl_o - lvl_p)[int(np.argmax(np.abs(lvl_o - lvl_p)))]:+.4f}); largest |residual DiD|: {ATOMS[int(np.argmax(np.abs(d_r.mean(0))))]} ({d_r.mean(0)[int(np.argmax(np.abs(d_r.mean(0))))]:+.4f}).", ""]
    summary[var] = dict(ex_o=ex_o, ex_p=ex_p, order_p=order_p, order_o=order_o, sign_match=(np.sign(ex_o) == np.sign(ex_p)), res_sts=float(np.nanmean(res[..., IX["sts"]])))
    # check against the diagnostic's saved series
    dz = OUT / f"diag_series_{var}_W60.npz"
    if dz.exists():
        z = np.load(dz)
        dev = np.nanmax(np.abs(res[..., IX["sts"]] - z["res"]))
        lines += [f"Check against diag_series_{var}_W60.npz: max |sts residual here − diagnostic's res| = {dev:.2e} (identical by construction up to floating point).", ""]

# global fit: run-level (a_x, a_y, q) → one prediction per run; levels only
lines += ["## Global fit (run-level a_x, a_y, q; levels, placebo and DMT pre-injection bins 1–8 of the observed bins; the prediction is constant across a run's bins)", "",
          "| variant | atom | observed level (bins 1–8, DMT) | predicted level (run-level, DMT) | residual |", "|---|---|---|---|---|"]
for var in ("ts_gsr", "ts_demean"):
    A = np.load(REPO / "results" / f"atoms_bins_115regions-all_{var}_global.npy")
    pred_run = np.full((14, 2, 16), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            pp = PairPhiID(X[:, kept])
            ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]; q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
            pred_run[s, c] = atoms_from_corr(ar1_corr(ax, ay, q)).mean(0)
    lvl_o = A[:, 0, PRE_B].mean((0, 1)); lvl_p = pred_run[:, 0].mean(0)
    for a, n in enumerate(ATOMS):
        lines.append(f"| {var} | {n} | {lvl_o[a]:+.4f} | {lvl_p[a]:+.4f} | {lvl_o[a] - lvl_p[a]:+.4f} |")
    ex_o = lvl_o[IX["sts"]] - (lvl_o[IX["xtx"]] + lvl_o[IX["yty"]]); ex_p = lvl_p[IX["sts"]] - (lvl_p[IX["xtx"]] + lvl_p[IX["yty"]])
    lines.append(f"| {var} | excess sts − (xtx + yty) | {ex_o:+.4f} | {ex_p:+.4f} | {ex_o - ex_p:+.4f} |")
lines.append("")

# the rule of the pre-run entry, stated with the numbers
lines += ["## The rule of the pre-run entry", ""]
for var, sm in summary.items():
    lines.append(f"{var}: predicted excess {sm['ex_p']:+.4f} against observed {sm['ex_o']:+.4f} — sign {'matches' if sm['sign_match'] else 'does not match'}; "
                 f"predicted ordering rts = str < xtx, yty {'holds' if sm['order_p'] else 'fails'} and the observed ordering {'holds' if sm['order_o'] else 'fails'}; sts residual {sm['res_sts']:+.4f}.")
both = all(sm["sign_match"] and sm["order_p"] and sm["order_o"] for sm in summary.values())
lines.append("Reading under the rule: " + ("the predicted sign of the excess and the ordering rts < xtx, yty match the data on both variants, so Results 1's \"two departures\" and their ACF attribution are replaced by the asymmetric-family account and the per-atom residuals (round 14)."
                                            if both else "the predicted sign of the excess or the ordering does not match the data on at least one variant (see the lines above); the departures stand as reported."))
(OUT / "family_atoms_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
