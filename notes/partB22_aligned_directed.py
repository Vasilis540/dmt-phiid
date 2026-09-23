"""
partB22_aligned_directed.py — B22: the aligned and directed cross-lag statistics without selection, the per-SD exchange
rate, and a spin test of the network structure of the regional map.
Pre-run entry: manuscript/analysis_record.md, "The aligned and directed cross-lag statistics without selection, the per-SD
exchange rate and the network spin test (B22): pre-run entry, 23 Sep 2026" (round 16, Part A).

Data: ts_gsr and ts_demean; region 20 excluded; non-finite TRs dropped as scripts/01 drops them; W = 60 windows of the
kept TRs as partB4_diagnostic.py forms them (a window with five kept TRs or fewer skipped); the whole-run matrices from all
kept TRs (partB15's run level). Per window and pair, partB15's deviations: a_x = C[0,2], a_y = C[1,3], q = the mean of
C[0,1] and C[2,3], δ_sym and δ_anti.
  window-sign  mean over pairs of sign(q_w)·δ_sym (partB15 l. 121; the selected statistic): its DiDs must reproduce
               −0.00119 (ts_gsr) and −0.00390 (ts_demean); its run means crosslag_deviation.csv's
               w60_signq_weighted_mean_deviation (1e-10).
  (a) A_other  mean over pairs of sign(q̄_other)·δ_sym, q̄_other = ½(C[0,1] + C[2,3]) of the pair's whole-run matrix in the
               same subject's other run; A_same with the whole same run's q̄; the share of pairs whose sign differs
               between the two runs.
  (b) B        the OLS slope of δ_sym on q across the 6,555 pairs of the window (np.polyfit), algebraically partB10's
               slope of the stacked deviations on q; its run means checked against w60_slope_deviation_on_q (1e-10).
  (c) D, Sym   partB15's closed-form response of sts to δ_anti alone and to δ_sym alone, averaged over pairs; their sum;
               the response to both ("Both") for reference; the residual (observed − AR(1)-substituted sts, partB4)
               checked against diag_series_<variant>_W60.npz (1e-10); the RMS δ_anti, its DiD checked against
               directed_crosslag_tables.md (ts_gsr +0.00631, p = 0.0829; ts_demean +0.00352, p = 0.2977).
  Every statistic: the DMT pre-injection level (windows 1–4), the post − pre change per run (windows 6–14 minus 1–4)
  and the DiD, each with its mean, exact sign-flip p, inverted interval (notes/rev_inference_inverted.py) and
  negative/14; per-window values written to aligned_directed.csv.
  (d) per window the SD (ddof = 1) over pairs of r₁ = ½(a_x + a_y) and of |q|; their means over the 112 pre-injection
      windows (windows 1–4 of both runs, 14 subjects); the ratio (6.0705 · SD_r₁)/(0.1892 · SD_|q|), with the mean of
      the per-window ratios beside it; the two derivatives recomputed in closed form at (0.85, 0.25) (central
      differences, h = 1e-4, as partB19 (a)) and required to equal 6.0705 and −0.1892 to four decimals. Group level:
      per pair the mean r₁ and |q| over the 14 subjects × 8 pre windows, their SDs over the 6,555 pairs, the same
      ratio. Over the 392 windows per variant: OLS with intercept of pair sts on (r₁, |q|, |a_x − a_y|), unstandardised,
      and standardised as partB19 (b) (each column z-scored with ddof = 1 within the window); means over windows; the
      standardised means required to reproduce exchange_rates_tables.md (b) at three decimals.
  (e) the `sts` and `sts_resid_win` maps and the `network` column of regional_partial.csv (partB20: seven Yeo networks
      from the parcel names, the 16 subcortical parcels as one class); the one-way ANOVA F over the eight classes;
      perm_id from external/DMT_NCT/fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat read as partB11 reads it; per
      rotation the 100-parcel cortical vector (region 20 NaN) indexed by perm_id[:, r], each parcel keeping its own
      class (from the LUT), the NaN dropped wherever it lands, the 16 subcortical values fixed; p = the share of rotations
      with F ≥ the observed F; the SomMot − Default and Vis − Default contrasts, two-sided (share of |d_spin| ≥ |d_obs|),
      for the residual map and, beside them, for the unpartialled map.
The conversion of the DiDs to residual-DiD equivalents (B23's aligned conversions) and their comparison with B24's and
B23 (b)'s expectations are made in the outcome entry (B23 and B24 run after this script).
Free choices: those above; no random draws anywhere; a failed check is printed as CHECK FAILED, counted in the table
header, and the run goes on.
Outputs (notes/review_results/partB/): aligned_directed_tables.md, aligned_directed.csv (one row per variant, subject,
run and window), aligned_directed_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB22_aligned_directed.py   (minutes; needs the .mat and the
rotation file of the data clone)
"""
import csv
import re
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_inference_inverted import signflip_inversion
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
SPIN = REPO / "external" / "DMT_NCT" / "fxns" / "SpinTests" / "rotated_maps" / "rotated_Schaefer_100.mat"
LUT = REPO / "data" / "Schaefer2018_100Parcels_7Networks_order.lut"
REGIONS = np.array([r for r in range(116) if r != 20])
S = ATOMS.index("sts")
W, N_WIN = 60, 14
PRE, POST = np.arange(0, 4), np.arange(5, 14)
NETS = ("Vis", "SomMot", "DorsAttn", "SalVentAttn", "Limbic", "Cont", "Default", "Subcortex")
DSTS_DR1, DSTS_DQ = 6.0705, -0.1892                       # exchange_rates_tables.md (a), checked below
t0 = time.time()
nan = float("nan")
if __name__ == "__main__" and not (MAT.exists() and SPIN.exists()):
    sys.exit("partB22: needs external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat and "
             "external/DMT_NCT/fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat (the data clone)")
CHECKS = []


def check(name, diff, tol):
    ok = bool(np.isfinite(diff) and diff <= tol)
    CHECKS.append((name, diff, tol, ok))
    if not ok:
        print(f"   CHECK FAILED: {name}: |difference| {diff:.3g} above {tol:.1g}", flush=True)
    return ok


def verbatim(src_rel, first, last):
    """The block between this file's markers equals lines first–last of src_rel."""
    own = Path(__file__).read_text().split("\n")
    i = next(k for k, l in enumerate(own) if l.startswith(f"# ---- copied verbatim from {src_rel}, l. {first}–{last}"))
    j = next(k for k in range(i + 1, len(own)) if own[k].startswith("# ---- end of the copy"))
    src = (REPO / src_rel).read_text().split("\n")[first - 1:last]
    check(f"the copy of {src_rel} l. {first}–{last} is verbatim", 0.0 if own[i + 1:j] == src else 1.0, 0.0)


# ---- copied verbatim from notes/partB15_directed_crosslag.py, l. 70–92 (checked at run time)
def deviations(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]
    q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    d_xy = C[:, 0, 3] - ay * q
    d_yx = C[:, 1, 2] - ax * q
    return ax, ay, q, 0.5 * (d_xy + d_yx), 0.5 * (d_xy - d_yx)


def with_deviation(ax, ay, q, d_xy, d_yx):
    """AR(1) matrices with the cross-lag entries corr(x_t, y_{t+1}) = a_y q + d_xy and corr(y_t, x_{t+1}) = a_x q + d_yx."""
    C = ar1_corr(ax, ay, q)
    C[:, 0, 3] = C[:, 3, 0] = ay * q + d_xy
    C[:, 1, 2] = C[:, 2, 1] = ax * q + d_yx
    return C


def response(ax, ay, q, sym, anti):
    """sts responses (per pair): to δ_anti alone, to δ_sym alone, to both; and the AR(1) sts."""
    base = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
    r_anti = atoms_from_corr(with_deviation(ax, ay, q, anti, -anti))[:, S] - base
    r_sym = atoms_from_corr(with_deviation(ax, ay, q, sym, sym))[:, S] - base
    r_both = atoms_from_corr(with_deviation(ax, ay, q, sym + anti, sym - anti))[:, S] - base
    return base, r_anti, r_sym, r_both
# ---- end of the copy


def window_stats(C, obs, sg_same, sg_other):
    """The per-window statistics of one window's pairs: C (n, 4, 4), observed pair sts, the two run-level signs."""
    ax, ay, q, sym, anti = deviations(C)
    base, r_anti, r_sym, r_both = response(ax, ay, q, sym, anti)
    r1p, aq, asym = 0.5 * (ax + ay), np.abs(q), np.abs(ax - ay)
    F = np.c_[r1p, aq, asym]
    Xu = np.c_[np.ones(obs.size), F]
    bu = np.linalg.lstsq(Xu, obs, rcond=None)[0][1:]
    Z = (F - F.mean(0)) / F.std(0, ddof=1)
    yz = (obs - obs.mean()) / obs.std(ddof=1)
    bs = np.linalg.lstsq(np.c_[np.ones(obs.size), Z], yz, rcond=None)[0][1:]
    st = dict(A_other=float(np.mean(sg_other * sym)), A_same=float(np.mean(sg_same * sym)), winsign=float(np.mean(np.sign(q) * sym)),
              B=float(np.polyfit(q, sym, 1)[0]), D=float(r_anti.mean()), Sym=float(r_sym.mean()), D_plus_Sym=float((r_anti + r_sym).mean()),
              Both=float(r_both.mean()), rms_anti=float(np.sqrt(np.mean(anti ** 2))), residual=float(obs.mean() - base.mean()),
              sd_r1=float(r1p.std(ddof=1)), sd_absq=float(aq.std(ddof=1)))
    return st, bu, bs, r1p, aq


STATS = ("A_other", "A_same", "winsign", "B", "D", "Sym", "D_plus_Sym", "Both", "rms_anti", "residual", "sd_r1", "sd_absq")
NAMES = {"A_other": "A_other (sign from the other run)", "A_same": "A_same (sign from the same run)", "winsign": "window-sign statistic (selected; partB15)",
         "B": "B, slope of δ_sym on q", "D": "D, response to δ_anti alone", "Sym": "Sym, response to δ_sym alone", "D_plus_Sym": "D + Sym",
         "Both": "response to both (reference)", "rms_anti": "RMS δ_anti", "residual": "residual (observed − AR(1)-substituted sts)",
         "sd_r1": "between-pair SD of r₁", "sd_absq": "between-pair SD of |q|"}


def summaries(x):
    """x (14, 2, 14) → dict of per-subject vectors: DMT pre level, DMT change, PCB change, DiD."""
    pre = np.nanmean(x[:, :, PRE], axis=2)
    post = np.nanmean(x[:, :, POST], axis=2)
    ch = post - pre
    return {"DMT pre level": pre[:, 0], "DMT post − pre": ch[:, 0], "placebo post − pre": ch[:, 1], "DiD": ch[:, 0] - ch[:, 1]}


def inf_cell(v):
    r = signflip_inversion(v)
    return f"{r['mean']:+.5f} [{r['lo']:+.5f}, {r['hi']:+.5f}], p = {r['p_zero']:.4f}, {r['n_neg']}", r


def sts_of(ax, ay, q):
    return atoms_from_corr(ar1_corr(ax, ay, q))[0, S]


def spin_f_and_contrasts(v115, net115, region_index, class100, perm_id):
    """One-way F over the eight classes and the SomMot − Default, Vis − Default contrasts, observed and per rotation."""
    cort = region_index < 100
    v100 = np.full(100, np.nan)
    v100[region_index[cort]] = v115[cort]
    sub_vals, sub_n = v115[~cort], int((~cort).sum())
    P = np.c_[np.arange(100), perm_id]                                      # column 0: the identity (the observed map)
    spun = v100[P]                                                          # (100, 1 + n_rot)
    fin = np.isfinite(spun)
    sums, counts, sq = {}, {}, {}
    for g in NETS[:-1]:
        m = (class100 == g)[:, None] & fin
        sums[g] = np.where(m, spun, 0).sum(0); counts[g] = m.sum(0); sq[g] = np.where(m, spun ** 2, 0).sum(0)
    sums["Subcortex"] = np.full(P.shape[1], sub_vals.sum()); counts["Subcortex"] = np.full(P.shape[1], sub_n)
    sq["Subcortex"] = np.full(P.shape[1], (sub_vals ** 2).sum())
    N = sum(counts[g] for g in NETS); tot = sum(sums[g] for g in NETS); grand = tot / N
    ssb = sum(counts[g] * (sums[g] / counts[g] - grand) ** 2 for g in NETS)
    ssw = sum(sq[g] - sums[g] ** 2 / counts[g] for g in NETS)
    k = len(NETS)
    Fs = (ssb / (k - 1)) / (ssw / (N - k))
    mean = {g: sums[g] / counts[g] for g in NETS}
    d_sm = mean["SomMot"] - mean["Default"]
    d_vis = mean["Vis"] - mean["Default"]
    # the identity column reproduces the observed statistics computed directly from the 115 values
    direct = {g: v115[net115 == g].mean() for g in NETS}
    check("(e) identity rotation = the direct class means", max(abs(direct[g] - mean[g][0]) for g in NETS), 1e-12)
    return dict(F=(Fs[0], np.mean(Fs[1:] >= Fs[0])), SomMot_Default=(d_sm[0], np.mean(np.abs(d_sm[1:]) >= abs(d_sm[0]))),
                Vis_Default=(d_vis[0], np.mean(np.abs(d_vis[1:]) >= abs(d_vis[0]))), n_rot=perm_id.shape[1], N=int(N[0]),
                F_all=Fs, SomMot_Default_all=d_sm, Vis_Default_all=d_vis)


def main():
    import h5py
    verbatim("notes/partB15_directed_crosslag.py", 70, 92)
    import scipy.io as sio
    ts = sio.loadmat(MAT)
    lines = ["# The aligned and directed cross-lag statistics without selection, the per-SD exchange rate and the network spin test (partB22_aligned_directed.py)",
             f"git={SHA}", "",
             "Exploratory; no threshold language. Per subject, run and W = 60 window, over the 6,555 pairs (region 20 excluded; non-finite TRs dropped as scripts/01): partB15's deviations of the window's 4 × 4 matrix. "
             "A_other = mean of sign(q̄_other)·δ_sym, q̄_other the pair's lag-0 correlation over the whole other run of the same subject; A_same with the whole same run's q̄; the window-sign statistic takes the sign of the window's own q (partB15, selected on the same samples). "
             "B = OLS slope of δ_sym on q across pairs. D and Sym = the closed-form response of the pair-mean sts to δ_anti alone and to δ_sym alone (partB15's response). Level = DMT windows 1–4; change = windows 6–14 minus 1–4; DiD = DMT minus placebo. "
             "Each cell: mean over subjects [inverted sign-flip 95 % interval], exact sign-flip p, negative/14.", ""]
    csv_rows = ["variant,subject,run,window," + ",".join(STATS)]
    CLD = list(csv.DictReader(open(OUT / "crosslag_deviation.csv")))
    DCT = (OUT / "directed_crosslag_tables.md").read_text()
    EXR = (OUT / "exchange_rates_tables.md").read_text()
    d_r1 = (sts_of(0.85 + 1e-4, 0.85 + 1e-4, 0.25) - sts_of(0.85 - 1e-4, 0.85 - 1e-4, 0.25)) / 2e-4
    d_q = (sts_of(0.85, 0.85, 0.25 + 1e-4) - sts_of(0.85, 0.85, 0.25 - 1e-4)) / 2e-4
    check("(d) ∂sts/∂r₁ at (0.85, 0.25) = 6.0705", abs(round(d_r1, 4) - DSTS_DR1), 1e-9)
    check("(d) ∂sts/∂q at (0.85, 0.25) = −0.1892", abs(round(d_q, 4) - DSTS_DQ), 1e-9)
    D_OUT = {}
    for var in ("ts_gsr", "ts_demean"):
        arr = {k: np.full((14, 2, N_WIN), nan) for k in STATS}
        share_diff = np.full(14, nan)
        bu_all, bs_all = [], []
        sum_r1 = np.zeros(6555); sum_aq = np.zeros(6555); n_pre = 0
        for s in range(14):
            X, kept, qbar = {}, {}, {}
            for c in range(2):
                X[c] = np.asarray(ts[var][s, c], float)[REGIONS]
                kept[c] = np.where(np.all(np.isfinite(X[c]), axis=0))[0]
                pr = PairPhiID(X[c][:, kept[c]])
                qbar[c] = 0.5 * (pr.C[:, 0, 1] + pr.C[:, 2, 3])
            share_diff[s] = np.mean(np.sign(qbar[0]) != np.sign(qbar[1]))
            for c in range(2):
                for w in range(N_WIN):
                    in_w = kept[c][(kept[c] >= w * W) & (kept[c] < (w + 1) * W)]
                    if in_w.size <= 5:
                        continue
                    pw = PairPhiID(X[c][:, in_w])
                    obs = pw.atoms_mean()[:, S]
                    st, bu, bs, r1p, aq = window_stats(pw.C, obs, np.sign(qbar[c]), np.sign(qbar[1 - c]))
                    for k in STATS:
                        arr[k][s, c, w] = st[k]
                    bu_all.append(bu); bs_all.append(bs)
                    if w in PRE:
                        sum_r1 += r1p; sum_aq += aq; n_pre += 1
                    csv_rows.append(f"{var},{s + 1},{'DMT' if c == 0 else 'PCB'},{w + 1}," + ",".join(f"{st[k]:.8g}" for k in STATS))
            print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
        # ---- checks against the committed files
        dg = np.load(OUT / f"diag_series_{var}_W60.npz")["res"]
        check(f"{var} residual per window = diag_series res", float(np.nanmax(np.abs(arr["residual"] - dg))), 1e-10)
        for k, col in (("winsign", "w60_signq_weighted_mean_deviation"), ("B", "w60_slope_deviation_on_q")):
            ref = np.array([[float([r for r in CLD if r["variant"] == var and int(r["subject"]) == s + 1 and r["condition"] == cn][0][col])
                             for cn in ("DMT", "PCB")] for s in range(14)])
            check(f"{var} {k} run means = crosslag_deviation.csv {col}", float(np.max(np.abs(np.nanmean(arr[k], axis=2) - ref))), 1e-10)
        block = DCT.split(f"## {var}, W = 60")[1].split("\n## ")[0]
        m_ws = re.search(r"DiD of the sign\(q\)-weighted mean of δ_sym[^:]*: ([+−-]?\d\.\d+) \[[^\]]*\], p = (\d\.\d+)", block)
        m_rms = re.search(r"DiD of the RMS of δ_anti[^:]*: ([+−-]?\d\.\d+) \[[^\]]*\], sign-flip p = (\d\.\d+)", block)
        for k, m in (("winsign", m_ws), ("rms_anti", m_rms)):
            v = summaries(arr[k])["DiD"]
            r = signflip_inversion(v)
            if m is None:
                check(f"{var} {k} DiD located in directed_crosslag_tables.md", nan, 0)
                continue
            check(f"{var} {k} DiD = directed_crosslag_tables.md (5 decimals)", abs(r["mean"] - float(m.group(1).replace("−", "-"))), 5.1e-6)
            check(f"{var} {k} DiD sign-flip p = directed_crosslag_tables.md (4 decimals)", abs(r["p_zero"] - float(m.group(2))), 5.1e-5)
        bu_all, bs_all = np.array(bu_all), np.array(bs_all)
        committed_bs = [float(c.replace("−", "-")) for c in re.search(r"\n\| " + var + r" \|[^\n]*\| ([^|\n]*) \|\n", EXR.split("## (b)")[1]).group(1).split(",")]
        check(f"{var} (d) mean standardised coefficients = exchange_rates_tables.md (b) (3 decimals)", float(np.max(np.abs(bs_all.mean(0) - np.array(committed_bs)))), 5.1e-4)
        # ---- (a)–(c) summaries
        lines += [f"## {var}: (a)–(c) the per-window statistics", "",
                  f"Pairs whose sign of q̄ differs between the two runs: mean share over subjects {share_diff.mean():.3f} (min {share_diff.min():.3f}, max {share_diff.max():.3f}).", "",
                  "| statistic | DMT pre-injection level | DMT post − pre | placebo post − pre | DiD |", "|---|---|---|---|---|"]
        for k in STATS[:10]:
            sm = summaries(arr[k])
            cells = [inf_cell(sm[key])[0] for key in ("DMT pre level", "DMT post − pre", "placebo post − pre", "DiD")]
            lines.append(f"| {NAMES[k]} | " + " | ".join(cells) + " |")
        res_did = summaries(arr["residual"])["DiD"]; ds_did = summaries(arr["D_plus_Sym"])["DiD"]
        lines += ["", f"The residual DiD {res_did.mean():+.5f} beside the DiD of D + Sym {ds_did.mean():+.5f} (their difference {res_did.mean() - ds_did.mean():+.5f}: the lag-0 substitution and the non-additivity of the two responses).", ""]
        # ---- (d)
        m_sd_r1 = float(np.nanmean(arr["sd_r1"][:, :, PRE])); m_sd_q = float(np.nanmean(arr["sd_absq"][:, :, PRE]))
        ratio = (DSTS_DR1 * m_sd_r1) / (abs(DSTS_DQ) * m_sd_q)
        per_w = (DSTS_DR1 * arr["sd_r1"][:, :, PRE]) / (abs(DSTS_DQ) * arr["sd_absq"][:, :, PRE])
        g_r1, g_q = sum_r1 / n_pre, sum_aq / n_pre
        ratio_g = (DSTS_DR1 * g_r1.std(ddof=1)) / (abs(DSTS_DQ) * g_q.std(ddof=1))
        D_OUT[var] = (m_sd_r1, m_sd_q, ratio, float(np.nanmean(per_w)), g_r1.std(ddof=1), g_q.std(ddof=1), ratio_g, bu_all.mean(0), bs_all.mean(0), len(bu_all), n_pre)
        lines += [f"## {var}: (d) the per-SD exchange rate and the within-window regression", "",
                  f"Within windows (the {int(np.isfinite(arr['sd_r1'][:, :, PRE]).sum())} pre-injection windows, windows 1–4 of both runs): mean between-pair SD of r₁ {m_sd_r1:.4f}, of |q| {m_sd_q:.4f}; "
                  f"ratio (6.0705 × SD_r₁)/(0.1892 × SD_|q|) {ratio:.2f} (mean of the per-window ratios {np.nanmean(per_w):.2f}).",
                  f"Group level (each pair averaged over the 14 subjects × 8 pre windows first; {n_pre} windows): SD over the 6,555 pairs of r₁ {g_r1.std(ddof=1):.4f}, of |q| {g_q.std(ddof=1):.4f}; ratio {ratio_g:.2f}.",
                  f"Within-window OLS of pair sts on (r₁, |q|, |a_x − a_y|) over {len(bu_all)} windows: mean unstandardised partial slopes {bu_all.mean(0)[0]:+.3f} per unit r₁, {bu_all.mean(0)[1]:+.3f} per unit |q|, "
                  f"{bu_all.mean(0)[2]:+.3f} per unit |a_x − a_y|; mean standardised coefficients {bs_all.mean(0)[0]:+.3f}, {bs_all.mean(0)[1]:+.3f}, {bs_all.mean(0)[2]:+.3f} "
                  f"(exchange_rates_tables.md (b): {', '.join(f'{c:+.3f}' for c in committed_bs)}).", ""]
    (OUT / "aligned_directed.csv").write_text(f"# partB22_aligned_directed.py; one row per variant, subject, run and W = 60 window; git={SHA}\n" + "\n".join(csv_rows) + "\n")
    # ---- (e) the spin test
    reg = list(csv.DictReader(l for l in open(OUT / "regional_partial.csv") if not l.startswith("#")))
    region_index = np.array([int(r["region_index"]) for r in reg])
    net115 = np.array([r["network"] for r in reg])
    lut = [l.split()[4].replace("7Networks_", "") for l in LUT.read_text().strip().splitlines()]
    class100 = np.array([n.split("_")[1] for n in lut])
    check("(e) the network column of regional_partial.csv = the LUT class of each cortical parcel",
          float(sum(net115[i] != class100[region_index[i]] for i in range(115) if region_index[i] < 100)), 0)
    with h5py.File(SPIN, "r") as f:
        perm_id = f["perm_id"][()]
    if perm_id.shape[0] != 100:
        perm_id = perm_id.T
    perm_id = perm_id.astype(int) - int(perm_id.min())
    lines += ["## (e) Spin test of the network structure of the regional maps (regional_partial.csv; eight classes: the seven Yeo networks and the subcortex)", "",
              "| map | one-way F (8 classes) | spin p (F_spin ≥ F_obs) | SomMot − Default | spin p, two-sided | Vis − Default | spin p, two-sided | rotations | regions |", "|---|---|---|---|---|---|---|---|---|"]
    for label, col in (("sts (unpartialled)", "sts"), ("sts with regional r₁ partialled out (sts_resid_win)", "sts_resid_win")):
        v115 = np.array([float(r[col]) for r in reg])
        e = spin_f_and_contrasts(v115, net115, region_index, class100, perm_id)
        lines.append(f"| {label} | {e['F'][0]:.3f} | {e['F'][1]:.4f} | {e['SomMot_Default'][0]:+.5f} | {e['SomMot_Default'][1]:.4f} | {e['Vis_Default'][0]:+.5f} | {e['Vis_Default'][1]:.4f} | {e['n_rot']} | {e['N']} |")
    lines += ["", "Rotations: perm_id of the Schaefer-100 rotation file, one direction (the classes are fixed labels); region 20's missing value moves with its parcel and is dropped wherever it lands; the 16 subcortical values are not rotated.", ""]
    n_fail = sum(1 for c in CHECKS if not c[3])
    lines += ["## Checks", "", f"{len(CHECKS)} checks run, {n_fail} failed."] + [f"- {'ok' if ok else 'CHECK FAILED'}: {n} (|difference| {d:.3g}, tolerance {t:.1g})" for n, d, t, ok in CHECKS]
    lines += ["", "## Predictions and rule (pre-run entry, B22)", "",
              "Predictions: (a) ts_gsr A_other level +0.001 to +0.004, DiD −0.003 to +0.001; ts_demean level −0.001 to −0.004, DiD −0.005 to 0; A_same near A_other; ts_gsr level below the window-sign +0.0061 and near the run-sign +0.00245; ts_demean level of the sign of δ_run (−0.0026). "
              "(b) B level about +0.020 (ts_gsr) and +0.024 (ts_demean); the DiD negative if a shared slow structure weakened, near B24's expectation if not. (c) D DiD −0.002 to −0.006 on ts_gsr; the directed part lowers the residual DiD; Sym's DiD exceeds the residual DiD. "
              "(d) within windows SD r₁ 0.025–0.035, SD |q| 0.18–0.22, ratio 4–6; group level 0.010–0.016, 0.12–0.18, 2–4; unstandardised slopes +5 to +6 per r₁, −0.40 to −0.55 per |q|, −3 to −5 per asymmetry. "
              "(e) spin p < 0.05 for the unpartialled F; 0.01–0.3 for the residual F; > 0.05 for both contrasts (the last two uncertain).",
              "Rule: A_other reported, A_same and B beside it; the DiDs read against B24's (quoted) and B23 (b)'s expectations and converted to residual-DiD equivalents with B23's two aligned conversions, in the outcome entry; "
              "(d) replaces the per-SD ratio of the abstract and Results 1; (e) decides the network-structure statement."]
    (OUT / "aligned_directed_tables.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"   checks: {len(CHECKS)} run, {n_fail} failed")
    print(f"done ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
