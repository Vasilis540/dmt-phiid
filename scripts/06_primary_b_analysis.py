"""
06_primary_b_analysis.py — Primary B inference on the windowed ΦID atoms.

Implements everything pre-registered in CLAUDE.md for the real-data windowed
analysis (13 Sep 2026 entries: "Primary step contrast at W = 60: inferential
test" and "motion handling", "Decay windows on real data", "Sign handling on
real data", "Which intensity", controls (a) and (b)). Run per variant:

    python3 scripts/06_primary_b_analysis.py --variant ts_gsr   [--window-trs 60]
    python3 scripts/06_primary_b_analysis.py --variant ts_demean

Inputs (all produced by 01_synergy_timecourse.py --fit-mode window):
    results/atoms_win{W}_115regions-all_{variant}_window.npy        (14, 2, n_win, 16)
    results/atoms_win{W}_local_115regions-all_{variant}_window.npy  (14, 2, 840, 16)
    external/DMT_NCT/data/intensity_ratings.mat   dmt_intensity (14, 28) uint8
    external/DMT_NCT/data/FDlong.mat              FDDMT, FDPCB (840, 14)
Condition axis: 0 = DMT, 1 = PCB. Atom 15 = sts (phyid order). Subject order
of FDlong columns and intensity rows is assumed to match the timeseries
subject axis (same source repo, same 14-subject cohort).

Window sets (1-based, inclusive; bins = 30-TR rating bins):
    W = 60: pre = windows 1-4 (bins 1-8); post/decay PRIMARY = windows 6-14
            (bins 11-28); SENSITIVITY = windows 5-14 (bins 9-28).
    W = 30: pre = bins 1-8; PRIMARY = bins 11-28; SENSITIVITY = bins 10-28
            (the pre-registered W = 30 decay set), reported as a check only.

SECTION A — step contrast (rule 5 effect sizes, rule 2 temporal null, rule 4 motion)
    Per subject: DiD = (post - pre)_DMT - (post - pre)_PCB on whole-brain mean sts.
    Test: exact sign-flip permutation over all 2^14 assignments, two-sided.
    Effect size: mean DiD, subject-bootstrap 95 % CI (N_BOOT draws), and as a
    share of the pre-injection DMT mean.
    Second null: phase-randomised temporal null. Per subject and condition the
    TR-resolution pair-mean sts local series (NaN at unattributed TRs) is
    compressed to its finite samples, phase-randomised (same power spectrum,
    random phases), written back to the same TR positions, re-averaged into
    the same windows, and the DiD recomputed; N_SURR surrogates; two-sided p.
    Motion: window-mean FD per condition reported (group mean, subject SD, and
    the FD DiD in the same form). FD-residualised sts: per subject and
    condition, OLS of window-mean sts on window-mean FD over ALL windows,
    intercept included; residuals replace sts and the identical DiD, sign-flip
    test and bootstrap CI are recomputed. "Survives motion control" = same sign
    as raw and residualised bootstrap CI excludes zero.
    Directional-failure rule: PREREG_DIRECTION = +1 (synergy up-regulated); a
    significant negative DiD is reported as a REFUTATION.

SECTION B — tier-2 tracking on the decay windows
    Per subject: Spearman rho_S (average ranks) between DMT window-mean sts and
    (i) that subject's own intensity ratings per window (mean of the bins in
    the window) — PRIMARY; subjects with constant ratings over the windows have
    no rho_S, are excluded and counted; (ii) the group template f (14-subject
    mean DMT rating per bin / its max, per window) — SENSITIVITY.
    Threshold rule (corrected 13 Sep 2026 before any real windowed result;
    CLAUDE.md "Tier-2 threshold: corrected rule"): |rho_S| >= TIER2_ABS_RHO
    applies to the GROUP-MEAN-SERIES rho — Spearman between the 14-subject
    mean sts series over the decay windows and the template f — because that
    is the pooled quantity the simulation validated (R on pooled window means);
    per-subject rho over 9 windows was never simulated and averaging noisy
    per-subject correlations attenuates. The per-subject mean rho (own ratings
    PRIMARY, template SENSITIVITY) is tested for EXISTENCE against the
    phase-randomised null (two-sided p; one-sided in the pre-registered
    direction also reported) with its subject-bootstrap CI, and is NOT
    thresholded. The sign of every rho is reported against PREREG_DIRECTION.
    TIER-2 CLAIM = group-mean-series |rho| >= 0.80  AND  per-subject mean rho
    significant (two-sided p < 0.05) against the null in the SAME direction as
    the group-mean-series rho  AND  control (a) not void  AND  control (b):
    the same three conditions hold on the FD-residualised sts.
    Control (a), time in scanner: the same statistic on the PCB run against
    the template. Void if the within-subject difference rho_DMT - rho_PCB has a
    subject-bootstrap 95 % CI including zero, or if the sign-corrected
    group-mean rho_PCB has the same sign as rho_DMT and >= half its magnitude.
    Control (b), motion settling: window-mean FD vs f (per-subject rho_S,
    group mean, CI); then sts residualised on FD within subject ACROSS THE
    DECAY WINDOWS ONLY, tier-2 statistic (both intensity versions) and control
    (a) recomputed in full on the residuals. Void unless the residualised
    statistic also passes control (a).

Outputs: results/primary_b_{variant}_win{W}.csv (long format, one row per
statistic) and a printed report. Seed 20261120 for bootstrap and surrogates.
No interpretation is written by this script; it reports numbers and the
pre-registered pass/void flags.
"""

import argparse
import csv
import subprocess
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.stats import spearmanr

SEED = 20261120
N_BOOT = 10000
N_SURR = 1000
TIER2_ABS_RHO = 0.80
PREREG_DIRECTION = +1
TIER2_DECIDES = "groupmean_series"  # threshold applies to the group-mean-series rho (see docstring)
STS = 15                            # phyid atom index of sts
N_SUBJ, N_TRS, N_BINS = 14, 840, 28
COND = ("DMT", "PCB")

ap = argparse.ArgumentParser()
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean", "ts_z", "ts"))
ap.add_argument("--window-trs", type=int, default=60, choices=(30, 60))
args = ap.parse_args()
V, W = args.variant, args.window_trs
N_WIN = N_TRS // W
BINS_PER_WIN = W // 30

# window sets as 0-based index arrays
if W == 60:
    PRE = np.arange(0, 4)                 # windows 1-4
    POST_PRIMARY = np.arange(5, 14)       # windows 6-14
    POST_SENS = np.arange(4, 14)          # windows 5-14
else:
    PRE = np.arange(0, 8)                 # bins 1-8
    POST_PRIMARY = np.arange(10, 28)      # bins 11-28
    POST_SENS = np.arange(9, 28)          # bins 10-28
SETS = {"primary": POST_PRIMARY, "sensitivity": POST_SENS}

DATA = Path("external/DMT_NCT/data")
RESULTS = Path("results")
TAG = f"115regions-all_{V}_window"
WIN_NPY = RESULTS / f"atoms_win{W}_{TAG}.npy"
LOCAL_NPY = RESULTS / f"atoms_win{W}_local_{TAG}.npy"
OUT_CSV = RESULTS / f"primary_b_{V}_win{W}.csv"

rng = np.random.default_rng(SEED)
rows = []


def rec(section, name, value, lo=np.nan, hi=np.nan, p=np.nan, note=""):
    rows.append(dict(section=section, statistic=name, value=value, ci_lo=lo, ci_hi=hi, p=p, note=note))
    ci = f" [{lo:+.4f}, {hi:+.4f}]" if np.isfinite(lo) else ""
    pp = f"  p={p:.4f}" if np.isfinite(p) else ""
    print(f"  {section:10s} {name:58s} {value:+.4f}{ci}{pp}  {note}")


# ---------------------------------------------------------------- load
atoms = np.load(WIN_NPY)
local = np.load(LOCAL_NPY)
assert atoms.shape == (N_SUBJ, 2, N_WIN, 16), atoms.shape
assert local.shape == (N_SUBJ, 2, N_TRS, 16), local.shape
sts = atoms[..., STS]                                   # (14, 2, n_win)
sts_local = local[..., STS]                             # (14, 2, 840) with NaN
assert np.isfinite(sts).all(), "window means must be finite"

fd = sio.loadmat(DATA / "FDlong.mat")
fd_tr = np.stack([fd["FDDMT"].T, fd["FDPCB"].T], axis=1)    # (14, 2, 840)
assert fd_tr.shape == (N_SUBJ, 2, N_TRS), fd_tr.shape
fd_win = np.nanmean(fd_tr.reshape(N_SUBJ, 2, N_WIN, W), axis=3)

ratings = sio.loadmat(DATA / "intensity_ratings.mat")["dmt_intensity"].astype(float)   # (14, 28)
assert ratings.shape == (N_SUBJ, N_BINS)
rating_win = ratings.reshape(N_SUBJ, N_WIN, BINS_PER_WIN).mean(2)        # per-subject intensity per window
template_bin = ratings.mean(0) / ratings.mean(0).max()
template_win = template_bin.reshape(N_WIN, BINS_PER_WIN).mean(1)         # group template f per window

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "CLAUDE.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

print(f"variant={V} W={W} windows={N_WIN} sts from {WIN_NPY.name}; local from {LOCAL_NPY.name}; git={sha}")
print(f"pre={PRE + 1} primary post/decay={POST_PRIMARY + 1} sensitivity={POST_SENS + 1}")


# ---------------------------------------------------------------- helpers
def did(x, post):
    """(14,) per-subject DiD of x (14, 2, n_win): (post-pre)_DMT - (post-pre)_PCB."""
    change = x[:, :, post].mean(2) - x[:, :, PRE].mean(2)
    return change[:, 0] - change[:, 1]


def boot_ci(v):
    v = np.asarray(v, float)
    v = v[np.isfinite(v)]
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))       # (16384, 14)


def signflip_p(v):
    v = np.asarray(v, float)
    obs = abs(v.mean())
    perm = np.abs((_SIGNS * v).mean(1))
    return float(np.mean(perm >= obs - 1e-12))


def residualise(y, x, idx):
    """Per row: OLS residuals of y[idx] on x[idx] (intercept), returned at idx."""
    out = np.full(y.shape, np.nan)
    for s in range(y.shape[0]):
        X = np.c_[np.ones(idx.size), x[s, idx]]
        beta, *_ = np.linalg.lstsq(X, y[s, idx], rcond=None)
        out[s, idx] = y[s, idx] - X @ beta
    return out


def phase_randomise(x):
    T = x.size
    f = np.fft.rfft(x)
    ph = rng.uniform(0, 2 * np.pi, f.size)
    ph[0] = 0.0
    if T % 2 == 0:
        ph[-1] = 0.0
    return np.fft.irfft(f * np.exp(1j * ph), n=T)


def surrogate_window_means():
    """(N_SURR, 14, 2, n_win): phase-randomised sts local series, re-windowed."""
    out = np.empty((N_SURR, N_SUBJ, 2, N_WIN))
    for s in range(N_SUBJ):
        for c in range(2):
            series = sts_local[s, c]
            fin = np.isfinite(series)
            win_of = np.arange(N_TRS) // W
            for k in range(N_SURR):
                surr = np.full(N_TRS, np.nan)
                surr[fin] = phase_randomise(series[fin])
                out[k, s, c] = np.array([np.nanmean(surr[win_of == w]) for w in range(N_WIN)])
    return out


def rho_rows(x, target):
    """Per-subject Spearman between x[s] and target[s] (both (14, n)); NaN if undefined."""
    r = np.full(x.shape[0], np.nan)
    for s in range(x.shape[0]):
        if np.std(target[s]) > 0 and np.std(x[s]) > 0:
            r[s] = spearmanr(x[s], target[s]).correlation
    return r


print(f"\ngenerating {N_SURR} phase-randomised surrogates per subject and condition ...")
SURR = surrogate_window_means()

# ---------------------------------------------------------------- SECTION A
print("\nSECTION A — step contrast on whole-brain mean sts")
pre_dmt = sts[:, 0, PRE].mean()
rec("A", "pre-injection DMT mean sts (windows 1-4)", pre_dmt)
rec("A", "pre-injection PCB mean sts (windows 1-4)", sts[:, 1, PRE].mean())
for c in range(2):
    for w in range(N_WIN):
        rec("A.fd", f"window-mean FD {COND[c]} window {w + 1} (group mean; note = subject SD)",
            fd_win[:, c, w].mean(), note=f"sd={fd_win[:, c, w].std(ddof=1):.4f}")

sts_resid_all = residualise(sts.reshape(N_SUBJ * 2, N_WIN), fd_win.reshape(N_SUBJ * 2, N_WIN),
                            np.arange(N_WIN)).reshape(N_SUBJ, 2, N_WIN)

for label, post in SETS.items():
    for c in range(2):
        ch = sts[:, c, post].mean(1) - sts[:, c, PRE].mean(1)
        lo, hi = boot_ci(ch)
        rec(f"A.{label}", f"{COND[c]} post-pre sts", ch.mean(), lo, hi, signflip_p(ch))
    d_raw = did(sts, post)
    lo, hi = boot_ci(d_raw)
    p_perm = signflip_p(d_raw)
    rec(f"A.{label}", "DiD raw: mean", d_raw.mean(), lo, hi, p_perm,
        note=f"share of pre-injection DMT mean = {d_raw.mean() / pre_dmt * 100:+.1f} %; "
             f"negative in {(d_raw < 0).sum()}/14")
    # temporal null
    d_surr = np.array([did(SURR[k], post) .mean() for k in range(N_SURR)])
    p_surr = (np.sum(np.abs(d_surr) >= abs(d_raw.mean())) + 1) / (N_SURR + 1)
    rec(f"A.{label}", "DiD raw: phase-randomised null p (two-sided)", p_surr,
        note=f"null mean {d_surr.mean():+.4f} sd {d_surr.std():.4f}")
    sign_ok = np.sign(d_raw.mean()) == PREREG_DIRECTION
    verdict = ("consistent with up-regulation" if sign_ok else
               "REFUTATION of up-regulation (directional-failure rule)") if p_perm < 0.05 else "not significant"
    rec(f"A.{label}", "DiD raw: sign vs PREREG_DIRECTION (+1 = up)", float(np.sign(d_raw.mean())), note=verdict)
    # motion
    d_fd = did(fd_win, post)
    lo, hi = boot_ci(d_fd)
    rec(f"A.{label}", "FD DiD (same form)", d_fd.mean(), lo, hi, signflip_p(d_fd))
    d_res = did(sts_resid_all, post)
    lo_r, hi_r = boot_ci(d_res)
    p_res = signflip_p(d_res)
    survives = (np.sign(d_res.mean()) == np.sign(d_raw.mean())) and (lo_r > 0 or hi_r < 0)
    rec(f"A.{label}", "DiD FD-residualised (all windows, per subject x condition): mean",
        d_res.mean(), lo_r, hi_r, p_res,
        note=("SURVIVES motion control" if survives else "does NOT survive motion control")
             + f"; negative in {(d_res < 0).sum()}/14")

# ---------------------------------------------------------------- SECTION B
print("\nSECTION B — tier-2 tracking on the decay windows (DMT run)")


def tier2_block(label, dec, x_dmt, x_pcb, surr_dmt, surr_pcb, tag):
    """All tier-2 statistics and controls for one window set and one sts version.

    x_dmt, x_pcb: (14, n_win) sts (raw or residualised); surr_*: (N_SURR, 14, n_win).
    Returns dict with pass/void flags.
    """
    out = {}
    for iname, target in (("per-subject ratings [PRIMARY]", rating_win[:, dec]),
                          ("group template f [SENSITIVITY]", np.tile(template_win[dec], (N_SUBJ, 1)))):
        r = rho_rows(x_dmt[:, dec], target)
        n_def = int(np.isfinite(r).sum())
        m = np.nanmean(r)
        lo, hi = boot_ci(r)
        null = np.array([np.nanmean(rho_rows(surr_dmt[k][:, dec], target)) for k in range(N_SURR)])
        p_one = (np.sum(PREREG_DIRECTION * null >= PREREG_DIRECTION * m) + 1) / (N_SURR + 1)
        p_two = (np.sum(np.abs(null) >= abs(m)) + 1) / (N_SURR + 1)
        n_strong = int(np.sum(np.abs(r[np.isfinite(r)]) >= TIER2_ABS_RHO))
        exists = p_two < 0.05
        rec(f"B.{label}", f"{tag} rho_S DMT vs {iname}: group mean (existence test, not thresholded)",
            m, lo, hi, p_two,
            note=f"n_defined={n_def}/14; |rho|>=0.80 in {n_strong} subjects (report only); "
                 f"p_one(prereg dir)={p_one:.4f}; sign {'+' if m > 0 else '-'} vs prereg +; "
                 f"significant vs null: {'yes' if exists else 'no'}")
        out[iname] = dict(r=r, m=m, exists=exists)
    # group-mean-series version (what the simulation validated): THE thresholded statistic
    gm = spearmanr(x_dmt[:, dec].mean(0), template_win[dec]).correlation
    null_gm = np.array([spearmanr(surr_dmt[k][:, dec].mean(0), template_win[dec]).correlation for k in range(N_SURR)])
    gm_pass = abs(gm) >= TIER2_ABS_RHO
    rec(f"B.{label}", f"{tag} rho_S group-mean sts series vs template [THRESHOLDED]", gm,
        p=(np.sum(np.abs(null_gm) >= abs(gm)) + 1) / (N_SURR + 1),
        note=f"|rho|>=0.80: {'PASS' if gm_pass else 'fail'}; sign {'+' if gm > 0 else '-'} vs prereg +")
    out["gm"] = gm
    out["gm_pass"] = gm_pass
    # control (a): time in scanner, PCB vs template
    tmpl = np.tile(template_win[dec], (N_SUBJ, 1))
    r_pcb = rho_rows(x_pcb[:, dec], tmpl)
    r_dmt_t = out["group template f [SENSITIVITY]"]["r"]
    m_pcb = np.nanmean(r_pcb)
    lo_p, hi_p = boot_ci(r_pcb)
    null_pcb = np.array([np.nanmean(rho_rows(surr_pcb[k][:, dec], tmpl)) for k in range(N_SURR)])
    rec(f"B.{label}", f"{tag} control (a): rho_S PCB vs template, group mean", m_pcb, lo_p, hi_p,
        (np.sum(np.abs(null_pcb) >= abs(m_pcb)) + 1) / (N_SURR + 1))
    diff = r_dmt_t - r_pcb
    lo_d, hi_d = boot_ci(diff)
    m_dmt_t = np.nanmean(r_dmt_t)
    same_sign_half = (np.sign(m_pcb) == np.sign(m_dmt_t)) and (abs(m_pcb) >= 0.5 * abs(m_dmt_t))
    void_a = (lo_d <= 0 <= hi_d) or same_sign_half
    rec(f"B.{label}", f"{tag} control (a): within-subject rho_DMT - rho_PCB (template)", np.nanmean(diff), lo_d, hi_d,
        note=("VOID" if void_a else "clears control (a)")
             + f" (CI includes 0: {lo_d <= 0 <= hi_d}; PCB same sign & >= half: {same_sign_half})")
    out["void_a"] = void_a
    return out


for label, dec in SETS.items():
    print(f"\n  [{label}: decay windows {dec + 1}]")
    raw = tier2_block(label, dec, sts[:, 0], sts[:, 1], SURR[:, :, 0], SURR[:, :, 1], "raw")
    # control (b): motion settling
    r_fd = rho_rows(fd_win[:, 0, dec], np.tile(template_win[dec], (N_SUBJ, 1)))
    lo, hi = boot_ci(r_fd)
    rec(f"B.{label}", "control (b): rho_S window-mean FD (DMT) vs template, group mean", np.nanmean(r_fd), lo, hi)
    sts_res = np.stack([residualise(sts[:, c], fd_win[:, c], dec) for c in range(2)], axis=1)
    surr_res = np.stack([np.stack([residualise(SURR[k][:, c], fd_win[:, c], dec) for c in range(2)], axis=1)
                         for k in range(N_SURR)])
    res = tier2_block(label, dec, sts_res[:, 0], sts_res[:, 1], surr_res[:, :, 0], surr_res[:, :, 1], "FD-resid")
    for iname in ("per-subject ratings [PRIMARY]", "group template f [SENSITIVITY]"):
        def ok(blk):
            same_dir = np.sign(blk[iname]["m"]) == np.sign(blk["gm"])
            return blk["gm_pass"] and blk[iname]["exists"] and same_dir and not blk["void_a"]
        claim = ok(raw) and ok(res)
        rec(f"B.{label}", f"TIER-2 CLAIM ({iname}): gm threshold & subject existence & (a) & (b)", float(claim),
            note=f"raw: gm_pass={raw['gm_pass']}, subj_sig={raw[iname]['exists']}, "
                 f"same_dir={np.sign(raw[iname]['m']) == np.sign(raw['gm'])}, (a) void={raw['void_a']} | "
                 f"resid: gm_pass={res['gm_pass']}, subj_sig={res[iname]['exists']}, "
                 f"same_dir={np.sign(res[iname]['m']) == np.sign(res['gm'])}, (a) void={res['void_a']}; "
                 f"sign of raw gm: {'+' if raw['gm'] > 0 else '-'} (prereg +)")

# ---------------------------------------------------------------- save
with open(OUT_CSV, "w") as fh:
    fh.write(f"# script=06_primary_b_analysis.py variant={V} window_trs={W} pre={list(PRE + 1)} "
             f"primary={list(POST_PRIMARY + 1)} sensitivity={list(POST_SENS + 1)} n_boot={N_BOOT} "
             f"n_surr={N_SURR} tier2_abs_rho={TIER2_ABS_RHO} prereg_direction={PREREG_DIRECTION} "
             f"tier2_decides={TIER2_DECIDES} seed={SEED} git={sha}\n")
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"\nwrote {OUT_CSV}")
