"""
rev_run.py — run the 06-equivalent inference (rev_inference.Engine) on every series of interest
and write notes/review_results/inference_rows.csv (+ .pkl with per-subject DiDs).

Series (label → window/bin means, TR-local series):
  sts            saved atoms (results_orig), windowed W60 (both variants), W30 (ts_gsr), global bins
  autocorr       mean regional lag-1 autocorrelation, window-standardised W60/W30, run-standardised bins
  PhiR           ΦR from the same atom arrays
  *_deconv       the same three quantities on the HRF-deconvolved series (sandbox results), when present
"""
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_inference import Engine, fmt
from rev_series import autocorr_series, phir_from_atoms, IX
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
ORIG = REPO / "results"                            # committed atom arrays (the review's clean rerun reproduced them to machine precision)
NEW = REPO / "results"                             # + atoms_bins_local_*_global.npy when 01 --fit-mode global has been run here (else no temporal null for the global rows)
SAND = REPO / "notes" / "review_results" / "deconv"  # deconvolved atom arrays (01 run on the rev_deconv.py output)
OUT = REPO / "notes" / "review_results"
OUT.mkdir(exist_ok=True)
MAT = "DMT_clean_mni_continuous_fullPreprocsch116.mat"
only = sys.argv[1] if len(sys.argv) > 1 else "all"

rows = []


def run(label, W, x, x_local):
    E = Engine(W)
    rs = E.run(x, x_local, label=label)
    for r in rs:
        print(fmt(r), flush=True)
    rows.extend(rs)


def load_atoms(base, prefix, tag):
    """01 writes <prefix>_<tag>.npy (window/bin means) and <prefix>_local_<tag>.npy (TR-local)."""
    A = np.load(base / f"{prefix}_{tag}.npy")
    lpath = base / f"{prefix}_local_{tag}.npy"
    L = np.load(lpath) if lpath.exists() else None
    return A, L


ts_raw = sio.loadmat(REPO / "external" / "DMT_NCT" / "data" / MAT)
DECONV_MAT = next((p for p in (SAND / MAT, REPO.parent / "deconv_run" / "sandbox" / "external" / "DMT_NCT" / "data" / MAT) if p.exists()), None)
ts_dec = sio.loadmat(DECONV_MAT) if DECONV_MAT is not None else None      # rev_deconv.py output (both variants merged into one .mat)

if only in ("all", "raw"):
    for var in ("ts_gsr", "ts_demean"):
        # ---- windowed W60: sts, PhiR, autocorr
        A, L = load_atoms(ORIG, "atoms_win60", f"115regions-all_{var}_window")
        run(f"sts {var} W60", 60, A[..., IX["sts"]], L[..., IX["sts"]])
        run(f"PhiR {var} W60", 60, phir_from_atoms(A), phir_from_atoms(L))
        w, l = autocorr_series(ts_raw[var], 60, "window")
        run(f"autocorr {var} W60", 60, w, l)
        # ---- global fit (bins): sts, PhiR (local series from the regenerated results dir), autocorr run-standardised
        A, L = load_atoms(NEW, "atoms_bins", f"115regions-all_{var}_global")
        run(f"sts {var} global-bins", 30, A[..., IX["sts"]], L[..., IX["sts"]] if L is not None else None)
        run(f"PhiR {var} global-bins", 30, phir_from_atoms(A), phir_from_atoms(L) if L is not None else None)
        w, l = autocorr_series(ts_raw[var], 30, "run")
        run(f"autocorr {var} run-standardised bins", 30, w, l)
    # ---- W30 check, ts_gsr
    A, L = load_atoms(ORIG, "atoms_win30", "115regions-all_ts_gsr_window")
    run("sts ts_gsr W30", 30, A[..., IX["sts"]], L[..., IX["sts"]])
    w, l = autocorr_series(ts_raw["ts_gsr"], 30, "window")
    run("autocorr ts_gsr W30", 30, w, l)

if only in ("all", "deconv") and ts_dec is not None:
    for var in ("ts_gsr", "ts_demean"):
        w, l = autocorr_series(ts_dec[var], 60, "window")
        run(f"autocorr_deconv {var} W60", 60, w, l)
        for prefix, tag, W, name in (("atoms_win60", f"115regions-all_{var}_window", 60, "W60"),
                                     ("atoms_bins", f"115regions-all_{var}_global", 30, "global-bins")):
            if (SAND / f"{prefix}_{tag}.npy").exists():
                A, L = load_atoms(SAND, prefix, tag)
                run(f"sts_deconv {var} {name}", W, A[..., IX["sts"]], L[..., IX["sts"]])
                run(f"PhiR_deconv {var} {name}", W, phir_from_atoms(A), phir_from_atoms(L))
                if name == "W60":
                    print("   16-atom DiD (deconvolved, primary):", " ".join(
                        f"{n}={((A[:, 0, 5:14, i].mean(1) - A[:, 0, :4, i].mean(1)) - (A[:, 1, 5:14, i].mean(1) - A[:, 1, :4, i].mean(1))).mean():+.4f}"
                        for i, n in enumerate(IX)))
                    print("   16-atom DMT pre level (deconvolved):", " ".join(f"{n}={A[:, 0, :4, i].mean():+.3f}" for i, n in enumerate(IX)))
        w, l = autocorr_series(ts_dec[var], 30, "run")
        run(f"autocorr_deconv {var} run-standardised bins", 30, w, l)

suffix = "" if only == "all" else f"_{only}"
df = pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows])
df.to_csv(OUT / f"inference_rows{suffix}.csv", index=False)
with open(OUT / f"inference_rows{suffix}.pkl", "wb") as fh:
    pickle.dump(rows, fh)
print(f"\nwrote {OUT / f'inference_rows{suffix}.csv'} ({len(rows)} rows)")
