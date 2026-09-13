"""
03_lz_vs_tdmi.py — whole-brain total TDMI vs EEG Lempel-Ziv complexity.

Pre-registered (CLAUDE.md, "EEG Lempel-Ziv complexity regressor", 13 Sep
2026, before any correlation was computed): whole-brain total TDMI (sum of
the 16 ΦID atoms from the global fit) under DMT anti-correlates with LZc
across the 28 30-TR bins.

Per subject: Spearman rho across the 28 bins between bin-mean atom value
(from results/atoms_bins_115regions-all_<variant>_global.npy) and bin-mean
LZc (RegDMT2 / RegPCB2 in RegressorLZInterpscrubbedConvolvedAvg.mat, each
(14, 840)). Group mean rho with a subject-level bootstrap CI. Null: the LZc
series of every subject is phase-randomised at the TR level (rule 2), binned,
and the group-mean rho recomputed; N_SURR surrogates. One-sided p in the
predicted direction (negative for total TDMI) and two-sided p reported.
Primary: total TDMI, DMT. Alongside: PCB run; sts and rtr atoms.

Descriptive, Robustness A status: global-fit atoms, no motion control, not a
test of the intensity-tracking hypothesis.
"""

import argparse
import subprocess
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.stats import spearmanr

from phyid.utils import PhiID_atoms_abbr

SEED = 20261120
N_BINS, TRS_PER_BIN = 28, 30
N_SURR = 1000
N_BOOT = 10000
ATOMS = tuple(PhiID_atoms_abbr)
QUANTITIES = ("total", "sts", "rtr")
PREDICTED_SIGN = {"total": -1, "sts": -1, "rtr": +1}   # total is the pre-registered one

ap = argparse.ArgumentParser()
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean", "ts_z", "ts"))
VARIANT = ap.parse_args().variant

DATA = Path("external/DMT_NCT/data")
RESULTS = Path("results")
ATOMS_NPY = RESULTS / f"atoms_bins_115regions-all_{VARIANT}_global.npy"
OUT_CSV = RESULTS / f"lz_vs_tdmi_{VARIANT}.csv"

rng = np.random.default_rng(SEED)

atoms = np.load(ATOMS_NPY)                       # (14, 2, 28, 16)
assert atoms.shape == (14, 2, N_BINS, 16), atoms.shape
lz = sio.loadmat(DATA / "RegressorLZInterpscrubbedConvolvedAvg.mat")
lz_tr = np.stack([lz["RegDMT2"], lz["RegPCB2"]], axis=1)   # (14, 2, 840)
assert lz_tr.shape == (14, 2, N_BINS * TRS_PER_BIN) and np.isfinite(lz_tr).all()
CONDITIONS = ("DMT", "PCB")

series = {
    "total": atoms.sum(-1),
    "sts": atoms[..., ATOMS.index("sts")],
    "rtr": atoms[..., ATOMS.index("rtr")],
}                                                 # each (14, 2, 28)


def to_bins(x):                                   # (..., 840) -> (..., 28)
    return x.reshape(*x.shape[:-1], N_BINS, TRS_PER_BIN).mean(-1)


def phase_randomise(x):
    """One surrogate per row of x (…, T): same power spectrum, random phases."""
    T = x.shape[-1]
    f = np.fft.rfft(x, axis=-1)
    ph = rng.uniform(0, 2 * np.pi, size=f.shape)
    ph[..., 0] = 0.0
    if T % 2 == 0:
        ph[..., -1] = 0.0
    return np.fft.irfft(f * np.exp(1j * ph), n=T, axis=-1)


def group_rho(y_bins, lz_bins):                   # both (14, 28) -> per-subject rho
    return np.array([spearmanr(y_bins[s], lz_bins[s]).correlation for s in range(14)])


lz_bins = to_bins(lz_tr)                          # (14, 2, 28)

# surrogate LZc, binned: (N_SURR, 14, 2, 28)
surr_bins = np.stack([to_bins(phase_randomise(lz_tr)) for _ in range(N_SURR)])

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "CLAUDE.md"],
                               text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

rows = []
print(f"variant={VARIANT}  atoms={ATOMS_NPY}  surrogates={N_SURR}  boot={N_BOOT}  git={sha}")
for qn in QUANTITIES:
    for c, cond in enumerate(CONDITIONS):
        rho = group_rho(series[qn][:, c], lz_bins[:, c])
        obs = rho.mean()
        boot = np.array([rho[rng.integers(0, 14, 14)].mean() for _ in range(N_BOOT)])
        lo, hi = np.percentile(boot, [2.5, 97.5])
        null = np.array([group_rho(series[qn][:, c], surr_bins[k, :, c]).mean()
                         for k in range(N_SURR)])
        sgn = PREDICTED_SIGN[qn]
        p_one = (np.sum(sgn * null >= sgn * obs) + 1) / (N_SURR + 1)
        p_two = (np.sum(np.abs(null) >= abs(obs)) + 1) / (N_SURR + 1)
        n_pred = int(np.sum(np.sign(rho) == sgn))
        # group-mean-series version, as the original MATLAB did it (baseline-corrected LZc)
        lz_bc = lz_bins[:, c] - lz_bins[:, c, :8].mean(-1, keepdims=True)
        rho_gm = spearmanr(series[qn][:, c].mean(0), lz_bc.mean(0)).correlation
        null_gm = np.array([spearmanr(series[qn][:, c].mean(0),
                                      (surr_bins[k, :, c] - surr_bins[k, :, c, :8].mean(-1, keepdims=True)).mean(0)).correlation
                            for k in range(N_SURR)])
        p_gm_two = (np.sum(np.abs(null_gm) >= abs(rho_gm)) + 1) / (N_SURR + 1)
        rows.append((qn, cond, obs, lo, hi, rho.std(ddof=1), n_pred, sgn, p_one, p_two,
                     null.mean(), null.std(), rho_gm, p_gm_two))
        print(f"  {qn:5s} {cond}: group-mean rho={obs:+.3f} [{lo:+.3f}, {hi:+.3f}] "
              f"(SD across subjects {rho.std(ddof=1):.3f}; {n_pred}/14 in predicted sign {sgn:+d}) "
              f"null mean {null.mean():+.3f} sd {null.std():.3f}  p_one={p_one:.3f} p_two={p_two:.3f} "
              f"| group-mean-series rho={rho_gm:+.3f} p_two={p_gm_two:.3f}")

with open(OUT_CSV, "w") as fh:
    fh.write(f"# script=03_lz_vs_tdmi.py variant={VARIANT} atoms_file={ATOMS_NPY.name} "
             f"n_surr={N_SURR} n_boot={N_BOOT} seed={SEED} git={sha}\n")
    fh.write("quantity,condition,rho_mean,ci_lo,ci_hi,rho_sd,n_subjects_predicted_sign,"
             "predicted_sign,p_one_sided,p_two_sided,null_mean,null_sd,"
             "rho_groupmean_series,p_two_sided_groupmean_series\n")
    for r in rows:
        fh.write(",".join(f"{v:.4f}" if isinstance(v, float) else str(v) for v in r) + "\n")
print(f"wrote {OUT_CSV}")
