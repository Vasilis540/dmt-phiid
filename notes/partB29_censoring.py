"""
partB29_censoring.py — B29: the volumes the release's preprocessing replaced (framewise displacement above 0.4 mm), by
window and run, against r₁ and sts; and the one non-finite TR.
Pre-run entry: manuscript/analysis_record.md, "The replaced volumes and the autocorrelation (B29): pre-run entry"
(specification, predictions and rule).

The data authors' Reporting Summary (Singleton et al., 2025, "Volume censoring") states that volumes with a framewise
displacement greater than 0.4 were replaced with the mean of the surrounding volumes, and that six of twenty
participants were discarded for more than 20 % of scrubbed volumes at that threshold. A replaced volume is a local
average, which raises the lag-1 autocorrelation around it; DMT raised head motion in the first minutes after the
injection (Timmermann et al., 2023, SI Appendix, Fig. S4). This script counts, from the released per-TR framewise
displacement (data/FDlong.mat: FDDMT, FDPCB, 840 TRs × 14 subjects), the TRs above 0.4 mm per subject, run and
window (W = 60; the replaced volumes cannot be told from the series themselves), and reads them against the window's
whole-brain r₁ (rev_series.autocorr_series in window mode on ts_gsr and ts_demean) and against the saved per-subject
DiDs of r₁ and sts (inference_rows_raw.pkl, "autocorr <variant> W60" and "sts <variant> W60"):
(a) per subject and run the number of TRs above 0.4 mm, their share, and the mean FD; per subject the DiD (windows
6–14 minus 1–4, DMT minus placebo) of the count per window and of the mean FD, with their means, exact sign-flip p and
shares of subjects; (b) across subjects, the correlation of the count DiD with the r₁ DiD and with the sts DiD on each
variant, beside the correlation of the mean-FD DiD with them; (c) within subjects and runs, the correlation across
windows between a window's count and its r₁, each subject-run's 14 windows centred on their own means, pooled over
the 28 runs, on each variant; (d) subjects 8 and 14 (the largest fall and the rise of whole-brain r₁ on ts_gsr) by
run: their counts, mean FD and r₁ by window; (e) the non-finite TR of the release: its subject, run and TR, and
that it is the run's last.
Free choices: the threshold 0.4 mm (the release's); counts per window of 60 TRs; the centring in (c). Non-finite FD
values, if any, count as not above the threshold and are left out of the means (rev_inference.fd_windows takes the
same means).
Outputs (notes/review_results/partB/): censoring_tables.md, censoring.csv (one row per subject × run × window),
censoring_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB29_censoring.py   (seconds)
--smoke: for a shape test on a tree whose saved DiDs are not the series' (the planning session's test on synthetic
files): the check that the r₁ series reproduce the saved per-subject DiDs is printed instead of enforced.
"""
import pickle
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_series import autocorr_series
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
DATA = REPO / "external" / "DMT_NCT" / "data"
THR = 0.4
W = 60
PRE, POST = np.arange(0, 4), np.arange(5, 14)
SIGNS = np.array(list(product((-1, 1), repeat=14)))
SMOKE = "--smoke" in sys.argv
t0 = time.time()


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def pdid(label, st="primary"):
    for d in pickle.load(open(RR / "inference_rows_raw.pkl", "rb")):
        if d["label"] == label and d["set"] == st:
            return np.asarray(d["did_subjects"], float)
    raise KeyError(label)


def did(x):
    ch = np.nanmean(x[:, :, POST], 2) - np.nanmean(x[:, :, PRE], 2)
    return ch[:, 0] - ch[:, 1]


fd = sio.loadmat(DATA / "FDlong.mat")
FD = np.stack([fd["FDDMT"].T, fd["FDPCB"].T], axis=1)                     # (14, 2, 840), as scripts/06 reads it
assert FD.shape == (14, 2, 840), FD.shape
ts = sio.loadmat(DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat")
R1 = {var: autocorr_series(ts[var], W, "window")[0] for var in ("ts_gsr", "ts_demean")}
above = FD > THR
cnt_w = above.reshape(14, 2, 14, W).sum(3)                                 # TRs above the threshold per window
fd_w = np.nanmean(FD.reshape(14, 2, 14, W), axis=3)                          # as rev_inference.fd_windows
cnt_run, share_run, fd_run = above.sum(2), above.sum(2) / np.isfinite(FD).sum(2), np.nanmean(FD, 2)
d_cnt, d_fd = did(cnt_w.astype(float)), did(fd_w)
print(f"   FD read: {int(above.sum())} TRs above {THR} mm of {FD.size} ({time.time() - t0:.0f}s)", flush=True)

lines = ["# The replaced volumes and the autocorrelation (partB29_censoring.py)", f"git={SHA}", "",
         f"TRs with framewise displacement above {THR} mm (the release's scrubbing threshold, at which the data authors' Reporting Summary says the volume was replaced by the mean of the surrounding volumes), "
         "from data/FDlong.mat, per subject, run and window of 60 TRs; r₁ = the window's whole-brain lag-1 autocorrelation (rev_series.autocorr_series, window mode). DiD = windows 6–14 minus 1–4, DMT minus placebo; p = exact sign-flip over the 14 subjects.", "",
         "## (a) TRs above the threshold per run, and the DiD of the count per window and of the mean FD", "",
         "| subject | DMT: count (share), mean FD | placebo: count (share), mean FD | count per window: DMT pre / post, placebo pre / post | count DiD | mean-FD DiD |", "|---|---|---|---|---|---|"]
csv = ["subject,run,window,n_above,mean_fd,r1_ts_gsr,r1_ts_demean"]
for s in range(14):
    lines.append(f"| {s + 1} | {int(cnt_run[s, 0])} ({share_run[s, 0]:.3f}), {fd_run[s, 0]:.3f} | {int(cnt_run[s, 1])} ({share_run[s, 1]:.3f}), {fd_run[s, 1]:.3f} | "
                 f"{cnt_w[s, 0, PRE].mean():.2f} / {cnt_w[s, 0, POST].mean():.2f}, {cnt_w[s, 1, PRE].mean():.2f} / {cnt_w[s, 1, POST].mean():.2f} | {d_cnt[s]:+.2f} | {d_fd[s]:+.4f} |")
    for c in range(2):
        for w in range(14):
            csv.append(f"{s + 1},{'DMT' if c == 0 else 'PCB'},{w + 1},{int(cnt_w[s, c, w])},{fd_w[s, c, w]:.5f},{R1['ts_gsr'][s, c, w]:.5f},{R1['ts_demean'][s, c, w]:.5f}")
lines += [f"| mean | {cnt_run[:, 0].mean():.1f} ({share_run[:, 0].mean():.3f}), {fd_run[:, 0].mean():.3f} | {cnt_run[:, 1].mean():.1f} ({share_run[:, 1].mean():.3f}), {fd_run[:, 1].mean():.3f} | "
          f"{cnt_w[:, 0, PRE].mean():.2f} / {cnt_w[:, 0, POST].mean():.2f}, {cnt_w[:, 1, PRE].mean():.2f} / {cnt_w[:, 1, POST].mean():.2f} | {d_cnt.mean():+.2f} (p = {signflip_p(d_cnt):.4f}; {int((d_cnt > 0).sum())}/14 positive) | "
          f"{d_fd.mean():+.4f} (p = {signflip_p(d_fd):.4f}; {int((d_fd > 0).sum())}/14 positive) |", ""]
lines += ["## (b) Across subjects: the count DiD and the mean-FD DiD against the r₁ DiD and the sts DiD", "",
          "| variant | r(count DiD, r₁ DiD) | r(count DiD, sts DiD) | r(mean-FD DiD, r₁ DiD) | r(mean-FD DiD, sts DiD) | r(count DiD, mean-FD DiD) |", "|---|---|---|---|---|---|"]
for var in ("ts_gsr", "ts_demean"):
    r1d, stsd = pdid(f"autocorr {var} W60"), pdid(f"sts {var} W60")
    same = np.allclose(did(R1[var]), r1d, atol=1e-9)
    assert same or SMOKE, "the r₁ series gives the saved DiDs"
    if not same:
        print(f"   SMOKE: the r₁ DiDs of {var} differ from the saved ones", flush=True)
    c = lambda a, b: f"{np.corrcoef(a, b)[0, 1]:+.3f}"
    lines.append(f"| {var} | {c(d_cnt, r1d)} | {c(d_cnt, stsd)} | {c(d_fd, r1d)} | {c(d_fd, stsd)} | {c(d_cnt, d_fd)} |")
lines += ["", "## (c) Within subjects and runs, across windows: the window's count against its r₁ (each run's 14 windows centred on their own means; 392 windows)", ""]
for var in ("ts_gsr", "ts_demean"):
    x = cnt_w - cnt_w.mean(2, keepdims=True); y = R1[var] - np.nanmean(R1[var], 2, keepdims=True)
    m = np.isfinite(y)
    lines.append(f"{var}: r = {np.corrcoef(x[m], y[m])[0, 1]:+.3f} (windows with at least one TR above the threshold: {int((cnt_w > 0).sum())} of 392; "
                 f"mean r₁ in them {np.nanmean(R1[var][cnt_w > 0]):.4f}, in the others {np.nanmean(R1[var][cnt_w == 0]):.4f}).")
lines += ["", "## (d) Subjects 8 and 14 by window (count above the threshold / mean FD / r₁ on ts_gsr)", ""]
for s in (7, 13):
    for c in range(2):
        lines.append(f"subject {s + 1}, {'DMT' if c == 0 else 'placebo'}: " + "; ".join(f"w{w + 1} {int(cnt_w[s, c, w])} / {fd_w[s, c, w]:.2f} / {R1['ts_gsr'][s, c, w]:.3f}" for w in range(14)))
nf = [(s + 1, "DMT" if c == 0 else "placebo", int(t)) for s in range(14) for c in range(2) for t in np.where(~np.all(np.isfinite(np.asarray(ts["ts_gsr"][s, c], float)), axis=0))[0]]
lines += ["", "## (e) The non-finite TR", "",
          "Non-finite TRs of ts_gsr (subject, run, TR index from 0): " + (", ".join(f"({s}, {r}, {t})" for s, r, t in nf) if nf else "none") +
          (f"; it is the last TR of its run (index 839) and falls at the end of window 14." if nf and all(t == 839 for _, _, t in nf) else ""), "",
          "## Reading under the rule of the pre-run entry", "",
          "Reported as computed; the entry's predictions (more marked TRs after the injection on the DMT run than before, relative to placebo, in the count and in the mean FD; within runs the count correlating positively with r₁ on both variants; "
          "no sign prediction for the count DiD against the r₁ DiD across subjects) are read against (a)–(c) in the outcome entry, and the Dataset paragraph, Results 2 or Limitations and S4 Text state the replacement and what it can and cannot do to r₁ as the rule says."]
(OUT / "censoring.csv").write_text(f"# partB29_censoring.py; per subject × run × window: TRs above {THR} mm, mean FD, whole-brain r₁; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "censoring_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
