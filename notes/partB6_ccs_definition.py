"""
partB6_ccs_definition.py — Part B item 6 (pre-run entry in manuscript/analysis_record.md, 15 Sep 2026):
the CCS double-redundancy mask of the published definition (Mediano et al., arXiv:2109.13186v1, Appendix,
Definition 1) against phyid's mask, on the same samples, and the CCS results under the published definition.

Masks (which local signs must agree for the double co-information D to be kept as the double redundancy):
  code : sign(I_xta) = sign(I_xtb) = sign(I_yta) = sign(I_ytb) = sign(D)          (phyid; partB2_ccs_run.py)
  pub  : sign(I_xta) = sign(I_xtb) = sign(I_yta) = sign(I_ytb) = sign(I_xytab)    (Definition 1, reading fixed in the record)
  pub8 : the eight partial MIs (the four above + I_xtab, I_ytab, I_xyta, I_xytb) and I_xytab   (sensitivity only)
  pubD : the pub five signs and sign(D)                                            (sensitivity only)
D itself, the six single-target CCS redundancies (Ince 2017) and the lattice solve are identical in every version.

Outputs (notes/review_results/partB/): ccs_definition_check.log, ccs_pub_tables.md,
  ccs_pub_atoms_win60_<variant>.npy (14, 2, 14, 16), ccs_pub_atoms_bins_<variant>.npy (14, 2, 28, 16),
  ccs_pub_agree_share_<variant>.npy (14, 2, 15); notes/review_results/inference_rows_ccs_pub.csv (+ .pkl).
Run from the repository root: .venv/bin/python notes/partB6_ccs_definition.py   (≈ 25 min single-core)
"""
import pickle
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.stats import pearsonr, spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rev_phiid_fast as RPF
from rev_phiid_fast import PairPhiID, ATOMS, KNOWNS, _ccs_red
from rev_inference import Engine, fmt, window_sets
from rev_series import autocorr_series

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
t0 = time.time()
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def make_knowns(mask):
    """A drop-in for rev_phiid_fast.ccs_local_knowns with the requested double-redundancy mask."""
    def knowns(mi):
        R = {"R_xyta": _ccs_red(mi["I_xta"], mi["I_yta"], mi["I_xyta"]), "R_xytb": _ccs_red(mi["I_xtb"], mi["I_ytb"], mi["I_xytb"]),
             "R_xytab": _ccs_red(mi["I_xtab"], mi["I_ytab"], mi["I_xytab"]), "R_abtx": _ccs_red(mi["I_xta"], mi["I_xtb"], mi["I_xtab"]),
             "R_abty": _ccs_red(mi["I_yta"], mi["I_ytb"], mi["I_ytab"]), "R_abtxy": _ccs_red(mi["I_xyta"], mi["I_xytb"], mi["I_xytab"])}
        D = (-mi["I_xta"] - mi["I_xtb"] - mi["I_yta"] - mi["I_ytb"] + mi["I_xtab"] + mi["I_ytab"] + mi["I_xyta"] + mi["I_xytb"] - mi["I_xytab"]
             + R["R_xyta"] + R["R_xytb"] - R["R_xytab"] + R["R_abtx"] + R["R_abty"] - R["R_abtxy"])
        s0 = np.sign(mi["I_xta"])
        four = (s0 == np.sign(mi["I_xtb"])) & (s0 == np.sign(mi["I_yta"])) & (s0 == np.sign(mi["I_ytb"]))
        if mask == "code":
            agree = four & (s0 == np.sign(D))
        elif mask == "pub":
            agree = four & (s0 == np.sign(mi["I_xytab"]))
        elif mask == "pub8":
            agree = four & (s0 == np.sign(mi["I_xtab"])) & (s0 == np.sign(mi["I_ytab"])) & (s0 == np.sign(mi["I_xyta"])) & (s0 == np.sign(mi["I_xytb"])) & (s0 == np.sign(mi["I_xytab"]))
        elif mask == "pubD":
            agree = four & (s0 == np.sign(mi["I_xytab"])) & (s0 == np.sign(D))
        else:
            raise ValueError(mask)
        K = np.empty(mi["I_xta"].shape + (16,))
        K[..., 0] = np.where(agree, D, 0.0)
        for c, name in enumerate(KNOWNS[1:], start=1):
            K[..., c] = mi[name] if name in mi else R[name]
        return K, D, agree
    return knowns


def use_mask(mask):
    RPF.ccs_local_knowns = make_knowns(mask)


ts = sio.loadmat(MAT)


def run_variant(var, mask, with_global=True, with_local=True):
    win = np.full((14, 2, 14, 16), np.nan)
    win_local = np.full((14, 2, 840, 16), np.nan)
    bins = np.full((14, 2, 28, 16), np.nan)
    bins_local = np.full((14, 2, 840, 16), np.nan)
    agree = np.full((14, 2, 15), np.nan)
    use_mask(mask)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            for w in range(14):
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                am, _, loc, ag = pp.atoms_ccs()
                win[s, c, w] = am.mean(0)
                if with_local:
                    win_local[s, c, in_w[:pp.n]] = loc
                agree[s, c, w] = ag.mean()
            if with_global:
                pp = PairPhiID(X[:, kept])
                am, ab, loc, ag = pp.atoms_ccs(kept[:pp.n] // 30, 28)
                bins[s, c] = np.nanmean(ab, axis=1)
                if with_local:
                    bins_local[s, c, kept[:pp.n]] = loc
                agree[s, c, 14] = ag.mean()
        log(f"   {var} [{mask}]: subject {s + 1}/14 done ({time.time() - t0:.0f}s)")
    return win, win_local, bins, bins_local, agree


# ---------------------------------------------------------------- 0. the masks on the same samples
log("# CCS definition check (partB6_ccs_definition.py)")
log("")
log("## 0. The four masks on identical samples: subject 1, ts_gsr, DMT window 6 and placebo window 2, all 6,555 pairs")
for (s, c, w) in ((0, 0, 5), (0, 1, 1)):
    X = np.asarray(ts["ts_gsr"][s, c], float)[REGIONS]
    kept = np.where(np.all(np.isfinite(X), axis=0))[0]
    in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
    pp = PairPhiID(X[:, in_w])
    res = {}
    for mask in ("code", "pub", "pub8", "pubD"):
        use_mask(mask)
        am, _, _, ag = pp.atoms_ccs()
        res[mask] = (am, ag)
    # sample-level agreement between the code and pub masks on the first 800 pairs
    mi = pp._local_mis(np.arange(800))
    K_code, D, a_code = make_knowns("code")(mi)
    K_pub, _, a_pub = make_knowns("pub")(mi)
    both = (a_code & a_pub).mean(); either = (a_code | a_pub).mean()
    log(f"subject 1 {'DMT' if c == 0 else 'PCB'} window {w + 1}: share of samples selected — code {a_code.mean():.3f}, pub {a_pub.mean():.3f}, both {both:.3f}, either {either:.3f}; "
        f"share where the two masks disagree {(a_code != a_pub).mean():.3f}")
    for mask in ("code", "pub", "pub8", "pubD"):
        am, ag = res[mask]
        log(f"   {mask:4s}: pair-mean sts {am[:, IX['sts']].mean():+.4f} (SD {am[:, IX['sts']].std():.4f}), rtr {am[:, IX['rtr']].mean():+.4f}, xtx+yty {am[:, IX['xtx']].mean() + am[:, IX['yty']].mean():+.4f}, agree share {ag.mean():.3f}")
    saved = np.load(OUT / "ccs_atoms_win60_ts_gsr.npy")[s, c, w]
    log(f"   code mask vs saved ccs_atoms_win60_ts_gsr.npy: max|diff| {np.abs(res['code'][0].mean(0) - saved).max():.1e}")
log(f"   ({time.time() - t0:.0f}s)")

# ---------------------------------------------------------------- 1. full run under the published mask, both variants
rows, lines = [], ["# CCS tables under the published double-redundancy definition (partB6_ccs_definition.py)", "",
                   "Mask 'pub' = Definition 1 of Mediano et al. (arXiv:2109.13186v1, Appendix): D kept where the four single-source, single-target local MIs and the local full MI i(x; y) share a sign. 'code' = phyid (D's own sign as the fifth). MMI from results/atoms_*.npy.", ""]
raw_rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))
diag_rows = pickle.load(open(RR / "inference_rows_diag.pkl", "rb"))
code_rows = pickle.load(open(RR / "inference_rows_ccs.pkl", "rb"))


def get_did(rows_, label, s="primary"):
    return np.asarray([r for r in rows_ if r["label"] == label and r["set"] == s][0]["did_subjects"], float)


summary = {}
for var in ("ts_gsr", "ts_demean"):
    win, win_local, bins, bins_local, agree = run_variant(var, "pub")
    np.save(OUT / f"ccs_pub_atoms_win60_{var}.npy", win)
    np.save(OUT / f"ccs_pub_atoms_bins_{var}.npy", bins)
    np.save(OUT / f"ccs_pub_agree_share_{var}.npy", agree)
    code_win = np.load(OUT / f"ccs_atoms_win60_{var}.npy")
    code_bins = np.load(OUT / f"ccs_atoms_bins_{var}.npy")
    mmi_win = np.load(REPO / "results" / f"atoms_win60_115regions-all_{var}_window.npy")
    mmi_bins = np.load(REPO / "results" / f"atoms_bins_115regions-all_{var}_global.npy")
    for est, A, L, CODE, MMI, W in (("W60", win, win_local, code_win, mmi_win, 60), ("global-bins", bins, bins_local, code_bins, mmi_bins, 30)):
        S = window_sets(W)
        PRE, POST = S["PRE"], S["primary"]
        for qname, x, xl in (("sts", A[..., IX["sts"]], L[..., IX["sts"]]),
                             ("xtx+yty", A[..., IX["xtx"]] + A[..., IX["yty"]], L[..., IX["xtx"]] + L[..., IX["yty"]]),
                             ("rtr", A[..., IX["rtr"]], L[..., IX["rtr"]])):
            E = Engine(W)
            rs = E.run(x, xl, label=f"CCSpub {qname} {var} {est}")
            for r in rs:
                log(fmt(r))
            rows.extend(rs)
        lvl = A[:, 0, PRE].mean((0, 1)); lvl_c = CODE[:, 0, PRE].mean((0, 1)); lvl_m = MMI[:, 0, PRE].mean((0, 1))
        did = ((A[:, 0, POST].mean(1) - A[:, 0, PRE].mean(1)) - (A[:, 1, POST].mean(1) - A[:, 1, PRE].mean(1)))
        did_c = ((CODE[:, 0, POST].mean(1) - CODE[:, 0, PRE].mean(1)) - (CODE[:, 1, POST].mean(1) - CODE[:, 1, PRE].mean(1)))
        did_m = ((MMI[:, 0, POST].mean(1) - MMI[:, 0, PRE].mean(1)) - (MMI[:, 1, POST].mean(1) - MMI[:, 1, PRE].mean(1)))
        lines += [f"## {var} {est}: 16 atoms, DMT pre-injection level and primary DiD — published mask, phyid's mask, MMI (nats)", "",
                  "| atom | pub level | code level | MMI level | pub DiD (mean, neg/14) | code DiD (neg/14) | MMI DiD |", "|---|---|---|---|---|---|---|"]
        for a, n in enumerate(ATOMS):
            lines.append(f"| {n} | {lvl[a]:+.4f} | {lvl_c[a]:+.4f} | {lvl_m[a]:+.4f} | {did[:, a].mean():+.4f} ({int((did[:, a] < 0).sum())}) | {did_c[:, a].mean():+.4f} ({int((did_c[:, a] < 0).sum())}) | {did_m[:, a].mean():+.4f} |")
        lines.append(f"| TDMI (sum) | {lvl.sum():+.4f} | {lvl_c.sum():+.4f} | {lvl_m.sum():+.4f} | {did.sum(1).mean():+.4f} | {did_c.sum(1).mean():+.4f} | {did_m.sum(1).mean():+.4f} |")
        d_sts = did[:, IX["sts"]]
        d_ac1 = get_did(raw_rows, f"autocorr {var} W60")
        d_res = get_did(diag_rows, f"diag residual sts {var} W60")
        d_code = did_c[:, IX["sts"]]
        lines += ["", f"Published-mask CCS sts: level {lvl[IX['sts']]:+.4f} vs phyid {lvl_c[IX['sts']]:+.4f} (difference {lvl[IX['sts']] - lvl_c[IX['sts']]:+.4f}); primary DiD {d_sts.mean():+.4f} vs phyid {d_code.mean():+.4f} (difference {d_sts.mean() - d_code.mean():+.4f}); per-subject r(pub, code) = {pearsonr(d_sts, d_code)[0]:+.3f}",
                  f"Per-subject pub CCS sts DiD vs the autocorrelation contrast (W60): Pearson r = {pearsonr(d_sts, d_ac1)[0]:+.3f} (p = {pearsonr(d_sts, d_ac1)[1]:.3f}), Spearman {spearmanr(d_sts, d_ac1)[0]:+.3f}; "
                  f"vs the MMI sts DiD of the same estimator: r = {pearsonr(d_sts, did_m[:, IX['sts']])[0]:+.3f}; "
                  f"vs the B4 residual DiD (W60): r = {pearsonr(d_sts, d_res)[0]:+.3f} (p = {pearsonr(d_sts, d_res)[1]:.3f}); "
                  f"pub CCS (xtx+yty) DiD vs autocorrelation contrast: r = {pearsonr(did[:, IX['xtx']] + did[:, IX['yty']], d_ac1)[0]:+.3f}",
                  f"pub CCS sts level / pub CCS (xtx + yty) level (DMT pre): {lvl[IX['sts']]:+.4f} / {lvl[IX['xtx']] + lvl[IX['yty']]:+.4f}; MMI: {lvl_m[IX['sts']]:+.4f} / {lvl_m[IX['xtx']] + lvl_m[IX['yty']]:+.4f}",
                  f"share of samples selected by the published mask (mean over runs): {np.nanmean(agree[:, :, :14] if est == 'W60' else agree[:, :, 14]):.3f}"]
        summary[(var, est)] = dict(pub_level=lvl[IX["sts"]], code_level=lvl_c[IX["sts"]], pub_did=d_sts.mean(), code_did=d_code.mean(),
                                   pub_p=[r for r in rows if r["label"] == f"CCSpub sts {var} {est}" and r["set"] == "primary"][0]["did_p"],
                                   code_p=[r for r in code_rows if r["label"] == f"CCS sts {var} {est}" and r["set"] == "primary"][0]["did_p"])
        if est == "W60":
            ac = autocorr_series(ts[var], 60, "window")[0].mean(0)
            g = A[..., IX["sts"]].mean(0); gm = MMI[..., IX["sts"]].mean(0)
            lines.append(f"Group-mean window series, pub CCS sts vs mean r1 (28 condition-windows): r = {pearsonr(g.ravel(), ac.ravel())[0]:+.3f}; MMI sts vs r1: {pearsonr(gm.ravel(), ac.ravel())[0]:+.3f}")
            for (s, c, w) in ((0, 0, 5), (0, 1, 1)):
                X = np.asarray(ts[var][s, c], float)[REGIONS]
                kept = np.where(np.all(np.isfinite(X), axis=0))[0]
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                pp = PairPhiID(X[:, in_w])
                use_mask("pub")
                am, _, _, ag = pp.atoms_ccs()
                r1p = 0.5 * (pp.C[:, 0, 2] + pp.C[:, 1, 3]); qp = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
                mm = pp.atoms_mean()
                lines.append(f"Per-pair, subject 1 {'DMT' if c == 0 else 'PCB'} window {w + 1}: pub CCS sts vs pair r1 r = {pearsonr(am[:, IX['sts']], r1p)[0]:+.3f}, vs |q| {pearsonr(am[:, IX['sts']], np.abs(qp))[0]:+.3f}, vs MMI sts {pearsonr(am[:, IX['sts']], mm[:, IX['sts']])[0]:+.3f}; MMI sts vs r1 {pearsonr(mm[:, IX['sts']], r1p)[0]:+.3f}; pub CCS sts pair mean {am[:, IX['sts']].mean():+.4f} (SD {am[:, IX['sts']].std():.4f}); agree share {ag.mean():.3f}")
        lines.append("")

# ---------------------------------------------------------------- 2. sensitivity masks, ts_gsr W60 window means only
log("")
log("## 2. Sensitivity masks (ts_gsr, W = 60, whole-brain window means only; decide nothing)")
S60 = window_sets(60); PRE, POST = S60["PRE"], S60["primary"]
sens = {}
for mask in ("pub8", "pubD"):
    win, _, _, _, agree = run_variant("ts_gsr", mask, with_global=False, with_local=False)
    np.save(OUT / f"ccs_{mask}_atoms_win60_ts_gsr.npy", win)
    d = ((win[:, 0, POST].mean(1) - win[:, 0, PRE].mean(1)) - (win[:, 1, POST].mean(1) - win[:, 1, PRE].mean(1)))
    sens[mask] = (win[:, 0, PRE].mean((0, 1))[IX["sts"]], d[:, IX["sts"]].mean(), int((d[:, IX["sts"]] < 0).sum()), np.nanmean(agree[:, :, :14]))
    log(f"   {mask}: CCS sts level {sens[mask][0]:+.4f}, primary DiD {sens[mask][1]:+.4f} (negative in {sens[mask][2]}/14), selected share {sens[mask][3]:.3f}")

# ---------------------------------------------------------------- 3. verdict under the recorded rule
log("")
log("## 3. Verdict under the rule recorded in the analysis record (agree = every whole-brain CCS-sts level and primary DiD within 0.001 nats and no sign-flip p crossing 0.05)")
agree_all = True
for k, v in summary.items():
    dl, dd = abs(v["pub_level"] - v["code_level"]), abs(v["pub_did"] - v["code_did"])
    cross = (v["pub_p"] < 0.05) != (v["code_p"] < 0.05)
    ok = (dl < 0.001) and (dd < 0.001) and not cross
    agree_all &= ok
    log(f"   {k[0]} {k[1]}: level pub {v['pub_level']:+.4f} vs code {v['code_level']:+.4f} (|Δ| {dl:.4f}); DiD pub {v['pub_did']:+.4f} vs code {v['code_did']:+.4f} (|Δ| {dd:.4f}); p pub {v['pub_p']:.4f} vs code {v['code_p']:.4f}{' — p crosses 0.05' if cross else ''} → {'within rule' if ok else 'DIFFERS'}")
log(f"   VERDICT: {'the two definitions agree on these data; phyid numbers stand' if agree_all else 'the definitions differ on these data; every CCS number in the manuscript is replaced by the published-definition value (this file), phyid values reported alongside as the code variant'}")
log(f"done ({time.time() - t0:.0f}s)")

pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows]).to_csv(RR / "inference_rows_ccs_pub.csv", index=False)
with open(RR / "inference_rows_ccs_pub.pkl", "wb") as fh:
    pickle.dump(rows, fh)
lines += ["## Sensitivity masks (ts_gsr, W = 60, window means only)", ""] + [f"- {m}: sts level {v[0]:+.4f}, primary DiD {v[1]:+.4f} (negative in {v[2]}/14), selected share {v[3]:.3f}" for m, v in sens.items()] + [""]
lines += ["## Verdict", ""] + [l.strip() for l in LOG if l.strip().startswith("VERDICT") or "→" in l] + [""]
(OUT / "ccs_pub_tables.md").write_text("\n".join(lines) + "\n")
(OUT / "ccs_definition_check.log").write_text("\n".join(LOG) + "\n")
