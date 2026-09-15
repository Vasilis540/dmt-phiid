"""
partB7_splithalf.py — Part B item 7 (pre-run entry in manuscript/analysis_record.md, 15 Sep 2026):
split-half test of the per-subject correlation between the B4 residual DiD and the CCS-sts DiD.

Halves (1-based windows; window 5 excluded as everywhere): odd = pre {1, 3}, post {7, 9, 11, 13};
even = pre {2, 4}, post {6, 8, 10, 12, 14}. Per subject, DiD_half = (post − pre)_DMT − (post − pre)_PCB on
the mean over that half's windows. Within-half r(CCS_odd, res_odd), r(CCS_even, res_even); cross-half
r(CCS_odd, res_even), r(CCS_even, res_odd); the same after partialling out the autocorrelation DiD of the
half each variable comes from; split-half reliabilities of every quantity. CCS-sts under the published
definition (B6, ccs_pub_atoms_win60_<variant>.npy) and, alongside, phyid's (ccs_atoms_win60_<variant>.npy).
Decision rule (record, B7): on ts_gsr, NOT window noise if both cross-half r > 0 and their mean ≥ half the
mean within-half r; estimation noise if the mean cross-half r < half the within-half mean or either
cross-half r < 0.
Outputs: notes/review_results/partB/splithalf_tables.md, splithalf.log.
Run from the repository root: .venv/bin/python notes/partB7_splithalf.py   (≈ 1 min)
"""
import sys
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.stats import pearsonr, spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_series import autocorr_series
from rev_phiid_fast import ATOMS

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
IX = {n: i for i, n in enumerate(ATOMS)}
HALVES = {"odd": (np.array([0, 2]), np.array([6, 8, 10, 12])), "even": (np.array([1, 3]), np.array([5, 7, 9, 11, 13])),
          "all": (np.arange(0, 4), np.arange(5, 14))}
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def did(x, pre, post):
    ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
    return ch[:, 0] - ch[:, 1]


def resid_on(y, z):
    X = np.c_[np.ones(z.size), z]
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ b


def r_str(a, b):
    r, p = pearsonr(a, b)
    return f"{r:+.3f} (p = {p:.3f}; ρ {spearmanr(a, b)[0]:+.3f})"


ts = sio.loadmat(MAT)
tables = ["# Split-half test of the CCS-sts / residual correlation (partB7_splithalf.py)", ""]
verdict = {}
for var in ("ts_gsr", "ts_demean"):
    z = np.load(OUT / f"diag_series_{var}_W60.npz")
    res, obs = z["res"], z["obs"]                                   # (14, 2, 14)
    ac = autocorr_series(ts[var], 60, "window")[0]                  # (14, 2, 14)
    ccs = {"pub": np.load(OUT / f"ccs_pub_atoms_win60_{var}.npy")[..., IX["sts"]],
           "code": np.load(OUT / f"ccs_atoms_win60_{var}.npy")[..., IX["sts"]]}
    log(f"# {var}, W = 60")
    d = {}
    for h, (pre, post) in HALVES.items():
        d[h] = dict(res=did(res, pre, post), sts=did(obs, pre, post), ac=did(ac, pre, post),
                    pub=did(ccs["pub"], pre, post), code=did(ccs["code"], pre, post))
    log(f"full-set check: r(res, pub CCS) = {r_str(d['all']['res'], d['all']['pub'])}; r(res, code CCS) = {r_str(d['all']['res'], d['all']['code'])}; r(res, autocorr) = {r_str(d['all']['res'], d['all']['ac'])}")
    log("split-half reliability (odd vs even) — residual DiD: " + r_str(d["odd"]["res"], d["even"]["res"]) +
        "; pub CCS-sts DiD: " + r_str(d["odd"]["pub"], d["even"]["pub"]) + "; code CCS-sts DiD: " + r_str(d["odd"]["code"], d["even"]["code"]) +
        "; autocorrelation DiD: " + r_str(d["odd"]["ac"], d["even"]["ac"]) + "; MMI sts DiD: " + r_str(d["odd"]["sts"], d["even"]["sts"]))
    log(f"group means — residual DiD odd {d['odd']['res'].mean():+.4f}, even {d['even']['res'].mean():+.4f}; pub CCS-sts DiD odd {d['odd']['pub'].mean():+.4f}, even {d['even']['pub'].mean():+.4f}; code CCS-sts DiD odd {d['odd']['code'].mean():+.4f}, even {d['even']['code'].mean():+.4f}")
    tables += [f"## {var}, W = 60", "", "| CCS version | r(CCS_odd, res_odd) | r(CCS_even, res_even) | mean within | r(CCS_odd, res_even) | r(CCS_even, res_odd) | mean cross | cross / within |", "|---|---|---|---|---|---|---|---|"]
    for ver in ("pub", "code"):
        w1 = pearsonr(d["odd"][ver], d["odd"]["res"])[0]; w2 = pearsonr(d["even"][ver], d["even"]["res"])[0]
        x1 = pearsonr(d["odd"][ver], d["even"]["res"])[0]; x2 = pearsonr(d["even"][ver], d["odd"]["res"])[0]
        mw, mx = 0.5 * (w1 + w2), 0.5 * (x1 + x2)
        log(f"[{ver}] within-half: r(CCS_odd, res_odd) = {r_str(d['odd'][ver], d['odd']['res'])}, r(CCS_even, res_even) = {r_str(d['even'][ver], d['even']['res'])} (mean {mw:+.3f})")
        log(f"[{ver}] cross-half:  r(CCS_odd, res_even) = {r_str(d['odd'][ver], d['even']['res'])}, r(CCS_even, res_odd) = {r_str(d['even'][ver], d['odd']['res'])} (mean {mx:+.3f}); cross/within = {mx / mw if mw else float('nan'):.2f}")
        # partial on the autocorrelation DiD of the half each variable comes from
        pw1 = pearsonr(resid_on(d["odd"][ver], d["odd"]["ac"]), resid_on(d["odd"]["res"], d["odd"]["ac"]))[0]
        pw2 = pearsonr(resid_on(d["even"][ver], d["even"]["ac"]), resid_on(d["even"]["res"], d["even"]["ac"]))[0]
        px1 = pearsonr(resid_on(d["odd"][ver], d["odd"]["ac"]), resid_on(d["even"]["res"], d["even"]["ac"]))[0]
        px2 = pearsonr(resid_on(d["even"][ver], d["even"]["ac"]), resid_on(d["odd"]["res"], d["odd"]["ac"]))[0]
        log(f"[{ver}] partial on the same-half autocorrelation DiD: within {pw1:+.3f}, {pw2:+.3f} (mean {0.5 * (pw1 + pw2):+.3f}); cross {px1:+.3f}, {px2:+.3f} (mean {0.5 * (px1 + px2):+.3f})")
        tables.append(f"| {ver} | {w1:+.3f} | {w2:+.3f} | {mw:+.3f} | {x1:+.3f} | {x2:+.3f} | {mx:+.3f} | {mx / mw if mw else float('nan'):.2f} |")
        tables.append(f"| {ver}, partial on autocorr | {pw1:+.3f} | {pw2:+.3f} | {0.5 * (pw1 + pw2):+.3f} | {px1:+.3f} | {px2:+.3f} | {0.5 * (px1 + px2):+.3f} | {0.5 * (px1 + px2) / (0.5 * (pw1 + pw2)) if (pw1 + pw2) else float('nan'):.2f} |")
        if ver == "pub":
            verdict[var] = dict(w=mw, x=mx, x1=x1, x2=x2)
    # context: the two halves against the autocorrelation contrast
    log("context — r(res_odd, ac_odd) = " + r_str(d["odd"]["res"], d["odd"]["ac"]) + "; r(res_even, ac_even) = " + r_str(d["even"]["res"], d["even"]["ac"]) +
        "; r(pubCCS_odd, ac_odd) = " + r_str(d["odd"]["pub"], d["odd"]["ac"]) + "; r(pubCCS_even, ac_even) = " + r_str(d["even"]["pub"], d["even"]["ac"]) +
        "; cross r(res_odd, ac_even) = " + r_str(d["odd"]["res"], d["even"]["ac"]) + "; r(res_even, ac_odd) = " + r_str(d["even"]["res"], d["odd"]["ac"]))
    tables += ["", f"Split-half reliabilities (odd vs even per-subject DiD): residual {pearsonr(d['odd']['res'], d['even']['res'])[0]:+.3f}; pub CCS-sts {pearsonr(d['odd']['pub'], d['even']['pub'])[0]:+.3f}; code CCS-sts {pearsonr(d['odd']['code'], d['even']['code'])[0]:+.3f}; autocorrelation {pearsonr(d['odd']['ac'], d['even']['ac'])[0]:+.3f}; MMI sts {pearsonr(d['odd']['sts'], d['even']['sts'])[0]:+.3f}.",
               f"Group-mean DiDs by half: residual odd {d['odd']['res'].mean():+.4f} / even {d['even']['res'].mean():+.4f}; pub CCS-sts odd {d['odd']['pub'].mean():+.4f} / even {d['even']['pub'].mean():+.4f}; autocorrelation odd {d['odd']['ac'].mean():+.4f} / even {d['even']['ac'].mean():+.4f}.", ""]
    log("")

v = verdict["ts_gsr"]
noise = (v["x"] < 0.5 * v["w"]) or (v["x1"] < 0) or (v["x2"] < 0)
signal = (v["x1"] > 0) and (v["x2"] > 0) and (v["x"] >= 0.5 * v["w"])
line = (f"VERDICT (rule of the record, ts_gsr, published CCS): within-half mean {v['w']:+.3f}, cross-half mean {v['x']:+.3f} ({v['x1']:+.3f}, {v['x2']:+.3f}) → "
        + ("shared component is NOT window noise: reported together as one exploratory observation of an autocorrelation-independent component" if signal else
           "shared component is estimation noise: both reported as null with this test as the evidence" if noise else "neither branch (should not happen)"))
log(line)
tables += ["## Verdict", "", line, ""]
(OUT / "splithalf_tables.md").write_text("\n".join(tables) + "\n")
(OUT / "splithalf.log").write_text("\n".join(LOG) + "\n")
