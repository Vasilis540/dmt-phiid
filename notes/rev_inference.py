"""
rev_inference.py — the step-contrast inference of scripts/06_primary_b_analysis.py (Section A),
factored so it can be applied to ANY per-window scalar series with a TR-resolution local series:
whole-brain sts (to validate: reproduces Table 1 bit for bit), mean regional lag-1 autocorrelation,
ΦR, and their HRF-deconvolved versions.

For a series x (14 subjects, 2 conditions [0 = DMT, 1 = PCB], n_win) and its TR-local series
x_local (14, 2, 840) with NaN at unattributed TRs, and window sets PRE / POST:
  * per-subject DiD = (post − pre)_DMT − (post − pre)_PCB; mean; subject-bootstrap 95 % CI
    (10,000 draws); exact two-sided sign-flip p over 2^14 assignments
  * phase-randomised temporal null: per subject and condition the finite local samples are
    phase-randomised (same power spectrum), written back, re-averaged into the windows, DiD
    recomputed; 1,000 surrogates; two-sided p = (count + 1) / (N + 1)            [as in 06]
  * FD DiD in the same form; FD-residualised DiD (OLS of window-mean x on window-mean FD across
    all windows, per subject × condition, intercept); "survives" = same sign as raw and the
    residualised bootstrap CI excludes zero                                        [as in 06]
The random-number stream is consumed in the same order as 06 for the primary and sensitivity
sets, so applying this to the saved sts series reproduces results/primary_b_*.csv exactly.

Extra sets (early = windows 6-9, late = 10-14 at W = 60; bins 11-18 / 19-28 at the bin level)
and two per-subject linear time-trend corrections are computed after the 06-order block:
  (a) placebo-trend DiD: fit x_PCB,w = a + b·w over all windows; predicted placebo change =
      mean_post(fit) − mean_pre(fit); DiD_trend = (post − pre)_DMT − predicted placebo change
  (b) shared-slope model per subject on the pre and post windows of both runs:
      x_{c,w} = a_c + b·w + δ·[c = DMT and w in post]; δ is the drug effect net of a common
      linear drift with run-specific offsets; δ is sign-flip tested and bootstrapped.
"""
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio

SEED = 20261120
N_BOOT = 10000
N_SURR = 1000
N_SUBJ, N_TRS = 14, 840
DATA = Path(__file__).resolve().parents[1] / "external" / "DMT_NCT" / "data"
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))


def signflip_p(v):
    v = np.asarray(v, float)
    obs = abs(v.mean())
    perm = np.abs((_SIGNS * v).mean(1))
    return float(np.mean(perm >= obs - 1e-12))


def fd_windows(W):
    fd = sio.loadmat(DATA / "FDlong.mat")
    fd_tr = np.stack([fd["FDDMT"].T, fd["FDPCB"].T], axis=1)          # (14, 2, 840)
    return np.nanmean(fd_tr.reshape(N_SUBJ, 2, N_TRS // W, W), axis=3)


def window_sets(W):
    if W == 60:
        return dict(PRE=np.arange(0, 4), primary=np.arange(5, 14), sensitivity=np.arange(4, 14),
                    early=np.arange(5, 9), late=np.arange(9, 14))
    return dict(PRE=np.arange(0, 8), primary=np.arange(10, 28), sensitivity=np.arange(9, 28),
                early=np.arange(10, 18), late=np.arange(18, 28))


class Engine:
    def __init__(self, W):
        self.W = W
        self.n_win = N_TRS // W
        self.sets = window_sets(W)
        self.fd_win = fd_windows(W)
        self.rng = np.random.default_rng(SEED)

    # -- primitives (same as 06) --------------------------------------------------------
    def did(self, x, post):
        change = x[:, :, post].mean(2) - x[:, :, self.sets["PRE"]].mean(2)
        return change[:, 0] - change[:, 1]

    def boot_ci(self, v):
        v = np.asarray(v, float)
        v = v[np.isfinite(v)]
        draws = v[self.rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
        return np.percentile(draws, [2.5, 97.5])

    def phase_randomise(self, x):
        T = x.size
        f = np.fft.rfft(x)
        ph = self.rng.uniform(0, 2 * np.pi, f.size)
        ph[0] = 0.0
        if T % 2 == 0:
            ph[-1] = 0.0
        return np.fft.irfft(f * np.exp(1j * ph), n=T)

    def surrogates(self, x_local):
        W, n_win = self.W, self.n_win
        out = np.empty((N_SURR, N_SUBJ, 2, n_win))
        win_of = np.arange(N_TRS) // W
        for s in range(N_SUBJ):
            for c in range(2):
                series = x_local[s, c]
                fin = np.isfinite(series)
                for k in range(N_SURR):
                    surr = np.full(N_TRS, np.nan)
                    surr[fin] = self.phase_randomise(series[fin])
                    out[k, s, c] = np.array([np.nanmean(surr[win_of == w]) for w in range(n_win)])
        return out

    @staticmethod
    def residualise(y, x, idx):
        out = np.full(y.shape, np.nan)
        for s in range(y.shape[0]):
            X = np.c_[np.ones(idx.size), x[s, idx]]
            beta, *_ = np.linalg.lstsq(X, y[s, idx], rcond=None)
            out[s, idx] = y[s, idx] - X @ beta
        return out

    # -- the analysis ------------------------------------------------------------------
    def run(self, x, x_local=None, label=""):
        """x: (14, 2, n_win); x_local: (14, 2, 840) or None (then no temporal null)."""
        assert x.shape == (N_SUBJ, 2, self.n_win), x.shape
        rows = []
        PRE = self.sets["PRE"]
        pre_dmt = x[:, 0, PRE].mean()
        pre_pcb = x[:, 1, PRE].mean()
        SURR = self.surrogates(x_local) if x_local is not None else None
        fd = self.fd_win
        x_res = self.residualise(x.reshape(N_SUBJ * 2, -1), fd.reshape(N_SUBJ * 2, -1),
                                 np.arange(self.n_win)).reshape(N_SUBJ, 2, -1)
        for set_name in ("primary", "sensitivity", "early", "late"):
            post = self.sets[set_name]
            r = dict(label=label, set=set_name, pre_dmt=pre_dmt, pre_pcb=pre_pcb)
            for c, cn in enumerate(("dmt", "pcb")):
                ch = x[:, c, post].mean(1) - x[:, c, PRE].mean(1)
                lo, hi = self.boot_ci(ch)
                r.update({f"{cn}_change": ch.mean(), f"{cn}_lo": lo, f"{cn}_hi": hi, f"{cn}_p": signflip_p(ch)})
            d = self.did(x, post)
            lo, hi = self.boot_ci(d)
            r.update(did=d.mean(), did_lo=lo, did_hi=hi, did_p=signflip_p(d), n_neg=int((d < 0).sum()),
                     share_of_pre=d.mean() / pre_dmt if pre_dmt else np.nan, did_subjects=d.copy())
            if SURR is not None:
                d_surr = np.array([self.did(SURR[k], post).mean() for k in range(N_SURR)])
                r["phase_p"] = (np.sum(np.abs(d_surr) >= abs(d.mean())) + 1) / (N_SURR + 1)
                r["phase_null_sd"] = d_surr.std()
            else:
                r["phase_p"] = np.nan
            d_fd = self.did(fd, post)
            lo, hi = self.boot_ci(d_fd)
            r.update(fd_did=d_fd.mean(), fd_lo=lo, fd_hi=hi, fd_p=signflip_p(d_fd))
            d_res = self.did(x_res, post)
            lo_r, hi_r = self.boot_ci(d_res)
            r.update(resid_did=d_res.mean(), resid_lo=lo_r, resid_hi=hi_r, resid_p=signflip_p(d_res),
                     resid_n_neg=int((d_res < 0).sum()),
                     survives=bool((np.sign(d_res.mean()) == np.sign(d.mean())) and (lo_r > 0 or hi_r < 0)))
            r["placebo_share"] = r["pcb_change"] / -d.mean() if d.mean() != 0 else np.nan
            rows.append(r)
        # -- linear time-trend corrections (primary set) ------------------------------
        post = self.sets["primary"]
        w = np.arange(self.n_win, dtype=float)
        # (a) placebo linear trend replaces the raw placebo change
        d_a = np.empty(N_SUBJ)
        for s in range(N_SUBJ):
            b, a = np.polyfit(w, x[s, 1], 1)
            fit = a + b * w
            pred_pcb = fit[post].mean() - fit[PRE].mean()
            d_a[s] = (x[s, 0, post].mean() - x[s, 0, PRE].mean()) - pred_pcb
        lo, hi = self.boot_ci(d_a)
        rows.append(dict(label=label, set="trend_a_placebo_line", did=d_a.mean(), did_lo=lo, did_hi=hi,
                         did_p=signflip_p(d_a), n_neg=int((d_a < 0).sum()), did_subjects=d_a.copy()))
        # (b) shared-slope model with run offsets, pre + post windows of both runs
        d_b = np.empty(N_SUBJ)
        keep = np.r_[PRE, post]
        for s in range(N_SUBJ):
            y = np.r_[x[s, 0, keep], x[s, 1, keep]]
            cond = np.r_[np.zeros(keep.size), np.ones(keep.size)]
            tt = np.r_[w[keep], w[keep]]
            drug = np.r_[np.isin(keep, post).astype(float), np.zeros(keep.size)]
            X = np.c_[np.ones(y.size), cond, tt, drug]
            beta, *_ = np.linalg.lstsq(X, y, rcond=None)
            d_b[s] = beta[3]
        lo, hi = self.boot_ci(d_b)
        rows.append(dict(label=label, set="trend_b_shared_slope", did=d_b.mean(), did_lo=lo, did_hi=hi,
                         did_p=signflip_p(d_b), n_neg=int((d_b < 0).sum()), did_subjects=d_b.copy()))
        return rows


def fmt(r):
    """One-line summary of a row."""
    s = f"{r['label']:34s} {r['set']:22s} DiD {r['did']:+.4f} [{r['did_lo']:+.4f}, {r['did_hi']:+.4f}] p={r['did_p']:.4f} neg {r['n_neg']}/14"
    if "phase_p" in r and np.isfinite(r.get("phase_p", np.nan)):
        s += f" | phase p={r['phase_p']:.4f}"
    if "resid_did" in r:
        s += (f" | DMT {r['dmt_change']:+.4f} (p={r['dmt_p']:.3f}) PCB {r['pcb_change']:+.4f} (p={r['pcb_p']:.3f}) placebo share {r['placebo_share']:.2f}"
              f" | FD DiD {r['fd_did']:+.4f} (p={r['fd_p']:.3f}) | FD-resid {r['resid_did']:+.4f} [{r['resid_lo']:+.4f}, {r['resid_hi']:+.4f}] p={r['resid_p']:.4f} {r['resid_n_neg']}/14 {'SURVIVES' if r['survives'] else 'does NOT survive'}")
    return s
