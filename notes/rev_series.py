"""
rev_series.py — builders for the per-window series and their TR-local counterparts.

autocorr_series(ts_obj, W, mode): mean regional lag-1 autocorrelation.
  mode="window": within each W-TR window, region i is standardised with the window's own mean
    and variance (ddof = 1) and the local product l_t = mean_i (x_{i,t} − μ_i)(x_{i,t+1} − μ_i)/σ_i²
    is stored at TR t for every consecutive pair inside the window; the window mean of l_t is
    exactly the standard lag-1 sample autocorrelation r1 = Σ(x_t−μ)(x_{t+1}−μ)/Σ(x_t−μ)², averaged
    over regions. This is the autocorrelation analogue of the windowed (refit-per-window) estimator.
  mode="run": μ_i and σ_i² over the whole run (the analogue of the global fit); local products
    averaged into 30-TR bins.
  Non-finite TRs are dropped exactly as 01_synergy_timecourse.py drops them; region 20 excluded.
  lag (default 1): the products are z_t z_{t+lag} over pairs of kept TRs exactly lag apart (lag-τ
  autocorrelation r_τ; used by partB3_lag.py).

phir_from_atoms(A): ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr on the phyid lattice
  (I(X;X′) = rtr + rtx + xtr + xtx; I(Y;Y′) = rtr + rty + ytr + yty), applied to window-mean or
  TR-local atom arrays alike (it is linear in the atoms).
"""
import numpy as np

ATOMS = "rtr,rtx,rty,rts,xtr,xtx,xty,xts,ytr,ytx,yty,yts,str,stx,sty,sts".split(",")
IX = {n: i for i, n in enumerate(ATOMS)}
REGIONS = np.array([r for r in range(116) if r != 20])
N_TRS = 840


def autocorr_series(ts_obj, W=60, mode="window", lag=1):
    n_subj, n_cond = ts_obj.shape
    n_win = N_TRS // W
    local = np.full((n_subj, n_cond, N_TRS), np.nan)
    win = np.full((n_subj, n_cond, n_win), np.nan)
    for s in range(n_subj):
        for c in range(n_cond):
            X = np.asarray(ts_obj[s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            if mode == "run":
                Xk = X[:, kept]
                mu = Xk.mean(1, keepdims=True)
                var = Xk.var(1, ddof=1, keepdims=True)
                Z = (Xk - mu) / np.sqrt(var)
                consecutive = (kept[lag:] - kept[:-lag]) == lag
                prod = (Z[:, :-lag] * Z[:, lag:]).mean(0)
                local[s, c, kept[:-lag][consecutive]] = prod[consecutive]
                slot = np.arange(N_TRS) // 30
                for w in range(n_win):
                    m = np.isfinite(local[s, c]) & (slot == w)
                    if m.any():
                        win[s, c, w] = local[s, c, m].mean()
            else:
                for w in range(n_win):
                    in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
                    if in_w.size <= 5:
                        continue
                    Xw = X[:, in_w]
                    mu = Xw.mean(1, keepdims=True)
                    var = Xw.var(1, ddof=1, keepdims=True)
                    Z = (Xw - mu) / np.sqrt(var)
                    consecutive = (in_w[lag:] - in_w[:-lag]) == lag
                    prod = (Z[:, :-lag] * Z[:, lag:]).mean(0)
                    local[s, c, in_w[:-lag][consecutive]] = prod[consecutive]
                    win[s, c, w] = prod[consecutive].mean()
    return win, local


def phir_from_atoms(A):
    ixx = A[..., IX["rtr"]] + A[..., IX["rtx"]] + A[..., IX["xtr"]] + A[..., IX["xtx"]]
    iyy = A[..., IX["rtr"]] + A[..., IX["rty"]] + A[..., IX["ytr"]] + A[..., IX["yty"]]
    return A.sum(-1) - ixx - iyy + A[..., IX["rtr"]]
