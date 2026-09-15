#!/usr/bin/env python3
"""
10_subject_alignment_check.py — is the subject axis shared across data files?

The analysis assumes that the timeseries subject axis
(DMT_clean_mni_continuous_fullPreprocsch116.mat, rows of the (14, 2) cell),
the columns of FDlong.mat, the rows of intensity_ratings.mat and the rows of
RegressorLZInterpscrubbedConvolvedAvg.mat are one ordering. No file carries
subject IDs on its numeric arrays. This script collects every piece of
evidence available from the repository and the files themselves:

  A. how the original MATLAB scripts index each file (one loop variable?);
  B. file metadata (shapes, creation dates);
  C. the one known defect in the timeseries (subject index 2, PCB, TR 839 is
     NaN in all variants): what FD and LZ hold at the same (subject, condition,
     TR);
  D. the opaque MATLAB `table` objects saved inside intensity_ratings.mat
     (DMT_intensity / PCB_intensity), which carry subject ID row names: the
     14-row uint8 arrays are matched row-by-row against the 20-row tables.
     The row names are participant codes; since 15 Sep 2026 (data governance)
     this script reports table row indices and counts only and never prints a
     code (record, "Data-governance note, 15 Sep 2026");
  E. matched-versus-mismatched subject pairings: for pairs of per-subject
     28-bin series from different files (group-mean shape removed), the mean
     Spearman rho of the matched pairing against a permutation null over
     subject assignments. Alignment predicts matched > mismatched.
  F. TR-level FD versus DVARS (frame-to-frame RMS signal change), matched vs
     mismatched, reported for completeness.

Outputs: results/subject_alignment_check.txt (this report) and
results/subject_alignment_permtests.csv. No file is modified.
"""
import io
import re
import subprocess
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.io.matlab._mio5 import MatFile5Reader
from scipy.stats import spearmanr

SEED = 20261120
N_PERM = 20000
rng = np.random.default_rng(SEED)
DATA = Path("external/DMT_NCT/data")
MSCRIPTS = Path("external/DMT_NCT/scripts")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)
try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

lines = []


def say(s=""):
    print(s)
    lines.append(s)


say(f"# subject alignment check — 10_subject_alignment_check.py, git={sha}, seed={SEED}")

# ------------------------------------------------------------------ A. MATLAB indexing
say("\n## A. How the original MATLAB indexes each file")
patterns = {
    "01_gen_time_resolved_ce.m": [r"for i = 1:nsub", r"TS\{i,1\}", r"TS\{i,2\}"],
    "02_global_ce_analyses.m": [r"win_dmt_ce_global\(i,:\)',dmt_intensity\(i,:\)'",
                                r"win_pcb_ce_global\(i,:\)',pcb_intensity\(i,:\)'",
                                r"global_CE_dmt\(i,:\)',RegDMT2\(i,:\)'",
                                r"global_CE_pcb\(i,:\)',RegPCB2\(i,:\)'",
                                r"m_dmt_fd = mean\(FDDMT\(2:839,:\)'\)",
                                r"win_dmt_fd\(:,i\) = mean\(FDDMT\(k:k\+window,:\)',2\)",
                                r"m_win_fd_diff = mean\(win_dmt_fd-win_pcb_fd\)"],
}
for fname, pats in patterns.items():
    src = (MSCRIPTS / fname).read_text().splitlines()
    for pat in pats:
        hits = [(i + 1, l.strip()) for i, l in enumerate(src) if re.search(pat, l)]
        for ln, txt in hits[:2]:
            say(f"  {fname}:{ln}: {txt}")
        if not hits:
            say(f"  {fname}: pattern not found: {pat}")
say("  Reading: TS{i,cond}, dmt_intensity(i,:), pcb_intensity(i,:), RegDMT2(i,:), RegPCB2(i,:) are all")
say("  indexed by the same loop variable i in 1:nsub, i.e. the authors treat the timeseries subject axis,")
say("  the ratings rows and the LZ rows as one ordering. FD is indexed as columns = subjects")
say("  (FDDMT(TRs, subjects)); its transpose gives one row per subject, but the MATLAB uses FD only at the")
say("  group level (mean over subjects of window FD, and a group-mean partial correlation), so FD-to-subject")
say("  alignment is asserted by the layout, not exercised per subject, in the original code.")

# ------------------------------------------------------------------ B. metadata
say("\n## B. File metadata")
files = {
    "timeseries": "DMT_clean_mni_continuous_fullPreprocsch116.mat",
    "FD": "FDlong.mat",
    "ratings": "intensity_ratings.mat",
    "LZ": "RegressorLZInterpscrubbedConvolvedAvg.mat",
}
mats = {}
for k, f in files.items():
    m = sio.loadmat(DATA / f)
    mats[k] = m
    hdr = m["__header__"].decode()
    created = hdr.split("Created on:")[-1].strip()
    arrs = [(n, v.shape, str(v.dtype)) for n, v in m.items() if not n.startswith("__") and hasattr(v, "shape")]
    say(f"  {f}: created {created}; {arrs}")
ts_all = mats["timeseries"]
FDD, FDP = mats["FD"]["FDDMT"], mats["FD"]["FDPCB"]
DI, PI = mats["ratings"]["dmt_intensity"].astype(float), mats["ratings"]["pcb_intensity"].astype(float)
LD, LP = mats["LZ"]["RegDMT2"], mats["LZ"]["RegPCB2"]
N = 14
say("  Every per-subject array has 14 subjects; timeseries (14,2) cell of (116,840); FD (840,14); ratings (14,28); LZ (14,840).")

# ------------------------------------------------------------------ C. co-located defect
say("\n## C. The subject-index-2 PCB TR-839 defect across files")
for v in ("ts", "ts_demean", "ts_gsr", "ts_z"):
    A = ts_all[v]
    bad = [(s, c, np.where(~np.isfinite(A[s, c]).all(0))[0].tolist()) for s in range(N) for c in range(2)
           if not np.isfinite(A[s, c]).all()]
    say(f"  {v}: non-finite TRs (subject, cond, TRs) = {bad}; regions non-finite at those TRs = "
        f"{[int((~np.isfinite(A[s, c][:, t])).sum()) for s, c, ts in bad for t in ts]}")
say(f"  FDPCB[839, 2] = {FDP[839, 2]!r}; FDDMT[839, 2] = {FDD[839, 2]:.4f}")
say(f"  FDPCB[830:840, 2] = {np.round(FDP[830:, 2], 4).tolist()}")
say(f"  FDPCB[839, :] (all subjects) = {np.round(FDP[839], 3).tolist()}")
say(f"  FD non-finite: DMT {int((~np.isfinite(FDD)).sum())}, PCB {int((~np.isfinite(FDP)).sum())}")
say(f"  FD == 0 count per subject, DMT {(FDD == 0).sum(0).tolist()}, PCB {(FDP == 0).sum(0).tolist()} "
    f"(TR 0 is 0 for every column; the only other exact zero in all 28 columns is FDPCB[839, 2])")
say(f"  FDPCB[839, 2] percentile within its own column: {(FDP[:, 2] < FDP[839, 2]).mean() * 100:.1f} % "
    f"(column median {np.median(FDP[:, 2]):.3f}, 5th pct {np.percentile(FDP[:, 2], 5):.3f})")
say(f"  LZ RegPCB2[2, 835:840] = {np.round(LP[2, 835:], 3).tolist()}; RegPCB2[:, 839] range "
    f"{LP[:, 839].min():.2f}..{LP[:, 839].max():.2f}; LZ non-finite: {int((~np.isfinite(LD)).sum() + (~np.isfinite(LP)).sum())}")
say("  Reading: the timeseries has a missing final volume for exactly one (subject, condition); the FD file")
say("  has an exact 0 (the value FD takes when no displacement can be computed) at exactly the same")
say("  (subject, condition, TR) and nowhere else beyond TR 0. The FD subject axis and the timeseries")
say("  subject axis agree at subject index 2. LZ shows nothing at that TR (it is an interpolated,")
say("  HRF-convolved EEG series, so a single missing fMRI volume need not appear in it).")
say(f"  Region-20 defect (subject index 7, DMT, constant zero): FDDMT[:, 7] mean {FDD[:, 7].mean():.3f}, "
    f"nothing abnormal expected or seen in FD or LZ for a single-parcel dropout.")

# ------------------------------------------------------------------ D. table decode
say("\n## D. Subject IDs inside intensity_ratings.mat (MATLAB table objects DMT_intensity / PCB_intensity)")
fw = mats["ratings"]["__function_workspace__"].tobytes()
rd = MatFile5Reader(io.BytesIO(fw[8:]), byte_order="<")
rd.initialize_read()
hdr, _ = rd.read_var_header()
res = rd.read_var_array(hdr, process=False)
md = np.asarray(res["MCOS"][0, 0]["_ObjectMetadata"]).ravel()
while md.size == 1 and md.dtype == object and isinstance(md[0], np.ndarray):
    md = md[0].ravel()


def strs(c):
    return [str(np.asarray(x).ravel()[0]) for x in np.asarray(c).ravel()]


def build(rn_i, var_i):
    rows = strs(md[rn_i])
    v = np.asarray(md[var_i]).ravel()
    varnames = strs(md[var_i + 5])
    cols = [np.asarray(v[k]).ravel().astype(float) for k in range(1, 29)]
    return rows, varnames, np.stack(cols, 1)


rowsD, varsD, TD = build(2, 4)
rowsP, varsP, TP = build(11, 13)
NONSUBJ = rowsD[20:]   # the trailing SD / SEM / average rows; the 20 subject codes are never printed
say(f"  table row names (both tables identical: {rowsD == rowsP}): 20 subject codes (not reproduced; data governance, 15 Sep 2026) + {NONSUBJ}")
say(f"  table variables: {varsD[0]} + {len(varsD) - 1} rating columns ({varsD[1]}..{varsD[-1]}); 20 subjects + SD/SEM/average rows")
ids = []
for i in range(N):
    hits = [rowsD[j] for j in range(20) if np.array_equal(DI[i], TD[j])]
    ids.append(hits)
say(f"  dmt_intensity row -> table row index (0-based) with identical 28 ratings: {[(i, [rowsD.index(x) for x in h]) for i, h in enumerate(ids)]}")
unique = all(len(h) == 1 for h in ids)
order = [rowsD.index(h[0]) for h in ids] if unique else None
say(f"  every DMT row matches exactly one table subject: {unique}; table indices {order}; "
    f"monotone (14 rows are the table order with 6 subjects removed): {order == sorted(order) if unique else 'n/a'}")
say(f"  table row indices of the 20-row table absent from the 14-row array: {[j for j in range(20) if j not in (order or [])]} (six codes, not reproduced)")
pcb_nonzero = [i for i in range(N) if PI[i].any()]
for i in pcb_nonzero:
    hits = [rowsP[j] for j in range(20) if np.array_equal(PI[i], TP[j])]
    say(f"  pcb_intensity row {i} (non-zero ratings) -> table row index {[rowsP.index(x) for x in hits]}; same subject as DMT row {i}: {hits == ids[i]}")
say(f"  pcb rows that are all zero match every all-zero table subject and carry no ordering information: "
    f"{[i for i in range(N) if not PI[i].any()]}")
say("  Reading: the ratings arrays are the table rows in table order with six subjects (table indices above)")
say("  removed (14 of 20; Singleton et al. report 14 subjects after motion exclusion, Timmermann et al.")
say("  recruited 20). The DMT and PCB arrays share one ordering. No other file carries IDs, so this fixes")
say("  the ratings ordering (ascending subject code) but cannot by itself tie it to the timeseries.")

# ------------------------------------------------------------------ E. matched vs mismatched
say("\n## E. Matched versus mismatched subject pairings (28-bin series, group-mean shape removed)")
say(f"  Statistic: mean over the 14 matched pairs of Spearman rho between series A_i and B_i, against the")
say(f"  distribution of the same mean under {N_PERM} random permutations of the B subject labels.")
say(f"  p is two-sided about the mismatched mean. Alignment predicts matched != mismatched; a null result")
say(f"  means the two series carry too little subject-specific shape to discriminate, not misalignment.")


def binm(X):
    return X.reshape(N, 28, 30).mean(2)


def resid(X):
    return X - X.mean(0)


atoms = np.load(RESULTS / "atoms_bins_115regions-all_ts_gsr_global.npy")
series = {
    "ratings_DMT": resid(DI),
    "FD_DMT": resid(binm(FDD.T)), "FD_PCB": resid(binm(FDP.T)),
    "LZ_DMT": resid(binm(LD)), "LZ_PCB": resid(binm(LP)),
    "sts_gsrglobal_DMT": resid(atoms[:, 0, :, 15]), "sts_gsrglobal_PCB": resid(atoms[:, 1, :, 15]),
    "TDMI_gsrglobal_DMT": resid(atoms[:, 0].sum(-1)), "TDMI_gsrglobal_PCB": resid(atoms[:, 1].sum(-1)),
}
tests = [
    ("ratings_DMT", "LZ_DMT", "ratings vs EEG-LZ"),
    ("ratings_DMT", "FD_DMT", "ratings vs FD"),
    ("ratings_DMT", "sts_gsrglobal_DMT", "ratings vs timeseries-derived sts"),
    ("ratings_DMT", "TDMI_gsrglobal_DMT", "ratings vs timeseries-derived TDMI"),
    ("LZ_DMT", "FD_DMT", "EEG-LZ vs FD"),
    ("LZ_PCB", "FD_PCB", "EEG-LZ vs FD"),
    ("sts_gsrglobal_DMT", "LZ_DMT", "timeseries-derived sts vs EEG-LZ"),
    ("TDMI_gsrglobal_DMT", "LZ_DMT", "timeseries-derived TDMI vs EEG-LZ"),
    ("sts_gsrglobal_PCB", "LZ_PCB", "timeseries-derived sts vs EEG-LZ"),
    ("TDMI_gsrglobal_PCB", "LZ_PCB", "timeseries-derived TDMI vs EEG-LZ"),
    ("sts_gsrglobal_DMT", "FD_DMT", "timeseries-derived sts vs FD"),
    ("sts_gsrglobal_PCB", "FD_PCB", "timeseries-derived sts vs FD"),
    ("TDMI_gsrglobal_DMT", "FD_DMT", "timeseries-derived TDMI vs FD"),
    ("TDMI_gsrglobal_PCB", "FD_PCB", "timeseries-derived TDMI vs FD"),
]
csv = ["a,b,label,matched_mean_rho,mismatched_mean_rho,p_perm_two_sided,n_argmax_self"]
say(f"  {'A':22s} {'B':22s} {'matched':>8s} {'mismatch':>8s} {'p':>7s} argmax==self")
for a, b, label in tests:
    A, B = series[a], series[b]
    M = np.array([[spearmanr(A[i], B[j])[0] for j in range(N)] for i in range(N)])
    obs = np.nanmean(np.diag(M))
    off = np.nanmean(M[~np.eye(N, dtype=bool)])
    null = np.array([np.nanmean(M[np.arange(N), rng.permutation(N)]) for _ in range(N_PERM)])
    p = (np.sum(np.abs(null - off) >= np.abs(obs - off)) + 1) / (N_PERM + 1)
    nself = int(sum(np.nanargmax(M[i]) == i for i in range(N)))
    say(f"  {a:22s} {b:22s} {obs:+8.3f} {off:+8.3f} {p:7.4f} {nself:2d}/14")
    csv.append(f"{a},{b},{label},{obs:.4f},{off:.4f},{p:.4f},{nself}")
(RESULTS / "subject_alignment_permtests.csv").write_text(
    f"# 10_subject_alignment_check.py git={sha} seed={SEED} n_perm={N_PERM}\n" + "\n".join(csv) + "\n")

# ------------------------------------------------------------------ F. TR-level FD vs DVARS
say("\n## F. TR-level FD versus DVARS (raw `ts`), matched vs mismatched")
for c, FD, nm in ((0, FDD, "DMT"), (1, FDP, "PCB")):
    D = []
    for s in range(N):
        d = np.diff(ts_all["ts"][s, c], axis=1)
        D.append(np.sqrt(np.nanmean(d ** 2, 0)))
    M = np.full((N, N), np.nan)
    for i in range(N):
        for j in range(N):
            ok = np.isfinite(D[i])
            M[i, j] = spearmanr(D[i][ok], FD[1:, j][ok])[0]
    say(f"  {nm}: diag mean {np.diag(M).mean():+.3f} (min {np.diag(M).min():+.3f}), off-diag mean "
        f"{M[~np.eye(N, dtype=bool)].mean():+.3f} (max {M[~np.eye(N, dtype=bool)].max():+.3f}); "
        f"argmax==self {int(sum(np.argmax(M[i]) == i for i in range(N)))}/14")
say("  Reading: the distributed timeseries are denoised and band-passed (motion regressors, scrubbing with")
say("  interpolation per the LZ filename), so frame-to-frame signal change no longer tracks FD in any")
say("  subject, matched or not. This test is uninformative on these data; it is not evidence against alignment.")

# ------------------------------------------------------------------ verdict
say("\n## Verdict (plain, per file pair)")
say("  timeseries <-> FD:      VERIFIED at one subject (co-located defect at subject index 2, PCB, TR 839; C),")
say("                          supported by the layout in the MATLAB (A); weak statistical support (E: TDMI vs FD on")
say("                          PCB p ~ 0.04, others null). A single co-located defect fixes one row; it does not by")
say("                          itself exclude a permutation of the other 13, which the E tests do not have power to detect.")
say("  timeseries <-> EEG LZ:  VERIFIED statistically (E: sts and TDMI vs LZ on DMT, matched clearly more negative than")
say("                          mismatched, p < 0.01, 20,000 permutations) and by the MATLAB per-subject loop (A).")
say("  ratings <-> timeseries: PLAUSIBLE. Asserted by the MATLAB per-subject loop (A); the ratings arrays are in")
say("                          ascending subject-code order (D); no statistical test discriminates (E: p 0.24-0.56)")
say("                          because after removing the group-mean curve the ratings carry little subject-specific shape.")
say("  ratings <-> FD:         PLAUSIBLE (E: p ~ 0.08, matched +0.19 vs mismatched +0.01, in the expected direction).")
say("  Overall: alignment VERIFIED for timeseries-FD (one subject) and timeseries-LZ; PLAUSIBLE, not verified, for")
say("  the ratings. Nothing found contradicts a single shared ordering. No file carries subject IDs on the")
say("  numeric arrays except the ratings tables, so a full verification would need the authors' subject list.")
(RESULTS / "subject_alignment_check.txt").write_text("\n".join(lines) + "\n")
print(f"\nwrote {RESULTS / 'subject_alignment_check.txt'} and {RESULTS / 'subject_alignment_permtests.csv'}")
