"""
rev_deconv.py — HRF-deconvolve every regional time series of the released dataset with the
rsHRF toolbox (Wu et al. 2013 blind deconvolution: point-process event detection, canonical HRF
with temporal and dispersion derivatives, Wiener deconvolution), the method Luppi et al. (2024)
applied before their ΦID analysis, and write the result as a .mat file with the SAME structure as
`DMT_clean_mni_continuous_fullPreprocsch116.mat` so that `scripts/01_synergy_timecourse.py` can be
run unchanged from a sandbox directory whose external/DMT_NCT/data/ holds the deconvolved file.

Settings: rsHRF defaults (estimation canon2dd, TR 2 s, microtime T = 3, localK = 1 for TR <= 2,
threshold 1 SD, onset search 4-8 s, HRF length 24 s, AR(1)), passband [0.01, 0.08] for the HRF
estimation as in the toolbox, classic (non-iterative) Wiener deconvolution as in Wu et al. 2013.
Per series the toolbox z-scores the input; the deconvolved output is returned in those units.

Usage (from the repository root): .venv/bin/python notes/rev_deconv.py --variant ts_gsr --out <sandbox>
  then merge the two variants' .mat files into one (keys ts_gsr, ts_demean) under
  <sandbox>/external/DMT_NCT/data/, symlink scripts/, FDlong.mat and intensity_ratings.mat, and run
  scripts/01_synergy_timecourse.py from <sandbox> with --fit-mode global and --fit-mode window --window-trs 60
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy import stats
from joblib import Parallel, delayed

from rsHRF import basis_functions, utils, processing, parameters
from rsHRF.utils import default_parameters as dp

ap = argparse.ArgumentParser()
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean"))
ap.add_argument("--out", type=Path, required=True)
ap.add_argument("--jobs", type=int, default=2)
args = ap.parse_args()

SRC = Path("external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat")
ts_all = sio.loadmat(SRC)[args.variant]
n_subj, n_cond = ts_all.shape
assert (n_subj, n_cond) == (14, 2)

para = dict(dp.default_parameters)
para["TR"] = 2.0
para["localK"] = 1                       # toolbox rule: TR <= 2 -> 1
para["dt"] = para["TR"] / para["T"]
para["lag"] = np.arange(np.fix(para["min_onset_search"] / para["dt"]),
                        np.fix(para["max_onset_search"] / para["dt"]) + 1, dtype="int")
para["wiener"] = False                   # Wu et al. 2013 Wiener filter (non-iterative)


def deconvolve_run(X):
    """X: (116, 840) regional series -> deconvolved (116, 840); NaN TRs restored afterwards."""
    X = np.asarray(X, float)
    nan_tr = ~np.all(np.isfinite(X), axis=0)           # whole-TR dropouts (subject 2 PCB TR 839)
    Xf = X.copy()
    Xf[:, nan_tr] = np.nanmean(X, axis=1, keepdims=True) if nan_tr.any() else 0.0
    data = Xf.T                                          # (T, N) as the toolbox expects
    sd = data.std(axis=0, ddof=1)
    const = sd == 0                                      # region 20 for subject 8 DMT
    bold = np.zeros_like(data)
    bold[:, ~const] = stats.zscore(data[:, ~const], ddof=1)
    bold = np.nan_to_num(bold)
    bold_deconv_in = processing.rest_filter.rest_IdealFilter(bold.copy(), para["TR"], para["passband_deconvolve"])
    bold_est = processing.rest_filter.rest_IdealFilter(bold.copy(), para["TR"], para["passband"])
    bf = basis_functions.basis_functions.get_basis_function(bold_est.shape, para)
    beta_hrf, event_bold = utils.hrf_estimation.compute_hrf(bold_est, para, [], args.jobs, bf=bf)
    hrfa = np.dot(bf, beta_hrf[np.arange(0, bf.shape[1]), :])
    from scipy import signal
    hrfa_TR = signal.resample_poly(hrfa, 1, para["T"]) if para["T"] > 1 else hrfa
    nobs = bold.shape[0]
    out = np.zeros_like(data)
    n_events = np.zeros(data.shape[1], int)
    for v in range(data.shape[1]):
        if const[v]:
            out[:, v] = 0.0
            continue
        hrf = hrfa_TR[:, v]
        H = np.fft.fft(np.append(hrf, np.zeros((nobs - max(hrf.shape), 1))), axis=0)
        M = np.fft.fft(bold_deconv_in[:, v])
        out[:, v] = np.real(np.fft.ifft(H.conj() * M / (H * H.conj() + 0.1 * np.mean((H * H.conj())))))
        n_events[v] = np.amax(event_bold[v].shape)
    Y = out.T                                            # (116, 840)
    Y[:, nan_tr] = np.nan                                # restore the dropout so 01 drops it as before
    Y[const, :] = 0.0                                    # keep the constant-region defect as it was
    return Y, hrfa_TR, n_events


t0 = time.time()
obj = np.empty((n_subj, n_cond), dtype=object)
hrfs = np.zeros((n_subj, n_cond, 116, 12))
events = np.zeros((n_subj, n_cond, 116), int)
for s in range(n_subj):
    for c in range(n_cond):
        Y, h, ne = deconvolve_run(ts_all[s, c])
        obj[s, c] = Y
        hrfs[s, c] = h[:12].T if h.shape[0] >= 12 else np.pad(h.T, ((0, 0), (0, 12 - h.shape[0])))
        events[s, c] = ne
        print(f"  s={s + 1:2d} c={c} done ({time.time() - t0:.0f}s); events/region median {np.median(ne):.0f}", flush=True)

out_dir = args.out / "external" / "DMT_NCT" / "data"
out_dir.mkdir(parents=True, exist_ok=True)
sio.savemat(out_dir / "DMT_clean_mni_continuous_fullPreprocsch116.mat", {args.variant: obj})
np.save(args.out / f"hrf_{args.variant}.npy", hrfs)
np.save(args.out / f"events_{args.variant}.npy", events)
print(f"wrote {out_dir / 'DMT_clean_mni_continuous_fullPreprocsch116.mat'} [{args.variant}] in {time.time() - t0:.0f}s")
