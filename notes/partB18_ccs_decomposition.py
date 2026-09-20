"""
partB18_ccs_decomposition.py — B18: the CCS-sts increase decomposed into the mask-selected share and the double
co-information of the rejected samples.
Pre-run entry: manuscript/analysis_record.md, "The CCS increase decomposed (B18): pre-run entry, 20 Sep 2026"
(specification and rule as in notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5; no prediction).

Under CCS the double redundancy is the local double co-information c_i (D of rev_phiid_fast.ccs_local_knowns, D ≡
rtr − sts on the lattice) on the mask-selected samples S and 0 elsewhere, so the time-mean CCS-sts of a pair over M
samples is −(1/M) Σ_{i∉S} c_i = −(1 − s) c̄_rej, with s = |S|/M the mask-selected share and c̄_rej the mean of c over
the rejected samples (checked here against PairPhiID.atoms_ccs for phyid's mask). Two masks: "code" (phyid's: the
four single MIs and D share a sign) and "pub" (the published: the four single MIs and i(x; y) share a sign; partB6).
Per pair, W = 60 window (local MIs under the window's own fit) and 30-TR bin (local MIs under the run's fit, the
global fit): the counts n_selected, n_samples and the sum of c over the rejected samples. Per subject, run and
period (pre = windows 1–4 or bins 1–8; post = windows 6–14 or bins 11–28) the samples of the period's windows or
bins are pooled: s = Σ n_selected / Σ n_samples, c̄_rej = Σ c_rejected / Σ n_rejected, and −(1 − s) c̄_rej is exactly
the period's sample-mean CCS-sts. The pre → post change of the pair-mean CCS-sts is then split exactly, per pair,
into c̄_pre Δs (the share term), −(1 − s_pre) Δc̄ (the co-information term) and +Δs Δc̄ (the interaction), each
averaged over pairs; the DiD (DMT minus placebo) of s, c̄_rej, the three terms and CCS-sts, with the subject
bootstrap (10,000 draws, seed 20261120) and the exact sign-flip p.
Free choices: variants ts_gsr and ts_demean; W = 60 (window 5 excluded from both periods, as everywhere); region 20
excluded; non-finite TRs dropped as scripts/01 drops them; chunks of 800 pairs (memory only). Seed 20261120.
Outputs (notes/review_results/partB/): ccs_decomposition_tables.md, ccs_decomposition.csv (one row per variant ×
estimator × mask × subject × run), ccs_decomposition_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB18_ccs_decomposition.py   (about partB6's time)
"""
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, ATOMS, _ccs_red
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
SEED = 20261120
N_BOOT = 10000
CHUNK = 800
N_PAIRS = 6555
PRE, POST = np.arange(0, 4), np.arange(5, 14)
PRE_B, POST_B = np.arange(0, 8), np.arange(10, 28)
SIGNS = np.array(list(product((-1, 1), repeat=14)))
MASKS = ("code", "pub")
t0 = time.time()


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def boot_ci(v, r):
    v = np.asarray(v, float)
    draws = v[r.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def double_coinfo_and_masks(mi):
    """From local MIs (dict of (n_sel, n) arrays): D (n_sel, n) and the two masks, as partB6 defines them."""
    R = {"R_xyta": _ccs_red(mi["I_xta"], mi["I_yta"], mi["I_xyta"]), "R_xytb": _ccs_red(mi["I_xtb"], mi["I_ytb"], mi["I_xytb"]),
         "R_xytab": _ccs_red(mi["I_xtab"], mi["I_ytab"], mi["I_xytab"]), "R_abtx": _ccs_red(mi["I_xta"], mi["I_xtb"], mi["I_xtab"]),
         "R_abty": _ccs_red(mi["I_yta"], mi["I_ytb"], mi["I_ytab"]), "R_abtxy": _ccs_red(mi["I_xyta"], mi["I_xytb"], mi["I_xytab"])}
    D = (-mi["I_xta"] - mi["I_xtb"] - mi["I_yta"] - mi["I_ytb"] + mi["I_xtab"] + mi["I_ytab"] + mi["I_xyta"] + mi["I_xytb"] - mi["I_xytab"]
         + R["R_xyta"] + R["R_xytb"] - R["R_xytab"] + R["R_abtx"] + R["R_abty"] - R["R_abtxy"])
    s0 = np.sign(mi["I_xta"])
    four = (s0 == np.sign(mi["I_xtb"])) & (s0 == np.sign(mi["I_yta"])) & (s0 == np.sign(mi["I_ytb"]))
    return D, {"code": four & (s0 == np.sign(D)), "pub": four & (s0 == np.sign(mi["I_xytab"]))}


def counts(pp, slot=None, n_slots=1):
    """Per mask: arrays (n_slots, n_pairs, 3) of [n_selected, n_samples, sum of c over rejected samples] per slot (slot = None: one slot)."""
    out = {m: np.zeros((n_slots, N_PAIRS, 3)) for m in MASKS}
    sl = np.zeros(pp.n, int) if slot is None else slot
    for start in range(0, N_PAIRS, CHUNK):
        sel = np.arange(start, min(start + CHUNK, N_PAIRS))
        D, masks = double_coinfo_and_masks(pp._local_mis(sel))
        for m, agree in masks.items():
            rej = ~agree
            for t in range(n_slots):
                mm = sl == t
                if not mm.any():
                    continue
                out[m][t, sel, 0] = agree[:, mm].sum(1); out[m][t, sel, 1] = mm.sum(); out[m][t, sel, 2] = (D[:, mm] * rej[:, mm]).sum(1)
    return out


def period_quantities(cnt):
    """cnt (n_pairs, 3) pooled counts → s, c̄_rej, sts per pair."""
    n_sel, n_tot, sum_c = cnt[:, 0], cnt[:, 1], cnt[:, 2]
    s = n_sel / n_tot
    n_rej = n_tot - n_sel
    cbar = np.where(n_rej > 0, sum_c / np.maximum(n_rej, 1), 0.0)
    return s, cbar, -(1 - s) * cbar


ts = sio.loadmat(MAT)
lines = ["# The CCS-sts increase decomposed: mask-selected share and double co-information of the rejected samples (partB18_ccs_decomposition.py)", f"git={SHA}", "",
         "Per pair and period CCS-sts = −(1 − s) c̄_rej exactly (samples of the period's windows or bins pooled): s the mask-selected share, c̄_rej the mean double co-information over the rejected samples. "
         "Masks: code (phyid's), pub (published). The pre → post change of the pair-mean CCS-sts is split per pair into c̄_pre Δs (share term), −(1 − s_pre) Δc̄ (co-information term) and +Δs Δc̄ (interaction), averaged over pairs. "
         f"DiD = DMT minus placebo (pre = windows 1–4 / bins 1–8; post = windows 6–14 / bins 11–28). Seed {SEED}; bootstrap {N_BOOT} draws; exact sign-flip p over 2^14. Region 20 excluded.", ""]
csv = ["variant,estimator,mask,subject,run,s_pre,s_post,cbar_pre,cbar_post,sts_pre,sts_post,term_share,term_coinfo,term_interaction,change_sts"]
check = []
for var in ("ts_gsr", "ts_demean"):
    Q = {est: {m: np.full((14, 2, 2, 3, N_PAIRS), np.nan) for m in MASKS} for est in ("W60", "global")}   # [subject, run, period, (s, cbar, sts), pair]
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            pooled = {m: np.zeros((2, N_PAIRS, 3)) for m in MASKS}
            for w in range(14):
                if w == 4:
                    continue
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                cnt = counts(pp)
                if s == 0 and c == 0 and w in (0, 5):
                    ref = pp.atoms_ccs()[0][:, IX["sts"]]
                    check.append(float(np.max(np.abs(period_quantities(cnt["code"][0])[2] - ref))))
                for m in MASKS:
                    pooled[m][0 if w in PRE else 1] += cnt[m][0]
            for m in MASKS:
                for per in range(2):
                    Q["W60"][m][s, c, per] = np.stack(period_quantities(pooled[m][per]))
            pp = PairPhiID(X[:, kept])
            cnt = counts(pp, kept[:pp.n] // 30, 28)
            for m in MASKS:
                for per, bins in enumerate((PRE_B, POST_B)):
                    Q["global"][m][s, c, per] = np.stack(period_quantities(cnt[m][bins].sum(0)))
        print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    for est in ("W60", "global"):
        lines += [f"## {var}, {est}", "", "| mask | quantity | DMT pre | DMT post | PCB pre | PCB post | DMT change | PCB change | DiD [95 % CI], sign-flip p, neg/14 |", "|---|---|---|---|---|---|---|---|---|"]
        for m in MASKS:
            A = Q[est][m]                                   # (14, 2, 2, 3, pairs)
            s_pre, s_post = A[:, :, 0, 0], A[:, :, 1, 0]; c_pre, c_post = A[:, :, 0, 1], A[:, :, 1, 1]; y_pre, y_post = A[:, :, 0, 2], A[:, :, 1, 2]
            term_share = (c_pre * (s_post - s_pre)).mean(-1); term_co = (-(1 - s_pre) * (c_post - c_pre)).mean(-1); term_int = ((s_post - s_pre) * (c_post - c_pre)).mean(-1)
            change = (y_post - y_pre).mean(-1)
            exact = float(np.max(np.abs(term_share + term_co + term_int - change)))
            r = np.random.default_rng(SEED)
            for name, pre_v, post_v, ch in (("s (selected share)", s_pre.mean(-1), s_post.mean(-1), (s_post - s_pre).mean(-1)),
                                             ("c̄_rej (nats)", c_pre.mean(-1), c_post.mean(-1), (c_post - c_pre).mean(-1)),
                                             ("CCS-sts (nats)", y_pre.mean(-1), y_post.mean(-1), change),
                                             ("share term c̄_pre Δs", None, None, term_share), ("co-information term −(1 − s_pre) Δc̄", None, None, term_co), ("interaction Δs Δc̄", None, None, term_int)):
                d = ch[:, 0] - ch[:, 1]
                lo, hi = boot_ci(d, r)
                cells = [f"{pre_v[:, 0].mean():.4f}", f"{post_v[:, 0].mean():.4f}", f"{pre_v[:, 1].mean():.4f}", f"{post_v[:, 1].mean():.4f}"] if pre_v is not None else ["—"] * 4
                lines.append(f"| {m} | {name} | " + " | ".join(cells) + f" | {ch[:, 0].mean():+.5f} | {ch[:, 1].mean():+.5f} | {d.mean():+.5f} [{lo:+.5f}, {hi:+.5f}], p = {signflip_p(d):.4f}, {int((d < 0).sum())} |")
            lines.append(f"| {m} | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = {exact:.1e} |")
            for s in range(14):
                for c in range(2):
                    csv.append(f"{var},{est},{m},{s + 1},{'DMT' if c == 0 else 'PCB'},{s_pre[s, c].mean():.6f},{s_post[s, c].mean():.6f},{c_pre[s, c].mean():.6f},{c_post[s, c].mean():.6f},"
                               f"{y_pre[s, c].mean():.6f},{y_post[s, c].mean():.6f},{term_share[s, c]:.6f},{term_co[s, c]:.6f},{term_int[s, c]:.6f},{change[s, c]:.6f}")
        lines.append("")
lines += [f"Check of the identity CCS-sts = −(1 − s) c̄_rej against PairPhiID.atoms_ccs (phyid's mask; subject 1 DMT windows 1 and 6, per pair): max |difference| = {max(check):.1e}.", "",
          "Rule of the pre-run entry: the plain reading (which of the share and the co-information terms carries the CCS-sts change) replaces \"no established reading\"; it does not make the CCS increase a finding about DMT. No prediction was recorded."]
(OUT / "ccs_decomposition.csv").write_text(f"# partB18_ccs_decomposition.py; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "ccs_decomposition_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
