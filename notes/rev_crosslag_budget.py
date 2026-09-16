"""
rev_crosslag_budget.py — the exact budget of the run-level sign(q)-weighted cross-lag deviation (16 Sep 2026;
pre-run entry "The cross-lag budget: pre-run entry, 16 Sep 2026" in manuscript/analysis_record.md). One function,
budget_terms(), computes every statistic from the run-level matrices, the run-level matrices after window demeaning,
the window matrices, the window SDs and a per-pair weight; partB12_crosslag_budget.py (data) and
partB13_crosslag_budget_null.py (finite-sample null and controls) both call it, so that the data and the null are
scored by the same code.

Matrices are the phyid-style 4 × 4 correlation matrices of [x_t, y_t, x_{t+1}, y_{t+1}] (past and future blocks
standardised separately, ddof = 1), exactly as rev_phiid_fast.PairPhiID and review_v2_residual_null.window_corr
build them. Per pair, with a_x = C[0, 2], a_y = C[1, 3], q = ½(C[0, 1] + C[2, 3]):
    d_xy = C[0, 3] − a_y q,   d_yx = C[1, 2] − a_x q,   d = ½(d_xy + d_yx)                 (as partB10)
    s = the per-pair weight passed in: the sign of the pair's run-level q in that run, for every term.
Window quantities (w = 1 … NW; n_w TRs in window w; N = Σ n_w; σ_{x,w} the population SD, ddof = 0, of x over the
window's n_w TRs; S_x² = Σ n_w σ²_{x,w} / N, likewise S_y²):
    π_w = n_w σ_{x,w} σ_{y,w} / (N S_x S_y);   ψ^y_w = n_w σ²_{y,w} / (N S_y²);   ā_y = Σ_w ψ^y_w a_{y,w}
    (ψ^x_w and ā_x from x's SDs).
Terms, every one the mean of the two directions (x→y shown; y→x mirrors with a_x, ψ^x and ā_x):
    δ_run    = s · d(run-level matrix)
    δ_wd     = s · d(run-level matrix of the window-demeaned series)
    δ_means  = δ_run − δ_wd
    δ_within = s · Σ_w π_w d_w
    δ_pool   = s · Σ_w π_w (a_{y,w} − ā_y) q_w
    ε        = δ_wd − δ_within − δ_pool
so that δ_run = δ_within + δ_pool + δ_means + ε exactly. Beside the budget: δ_60 = s · mean_w d_w (equal weight,
run-level sign) and partB10's window-sign value, mean_w sign(q_w) d_w.
Aggregation (aggregate()): mean over pairs per run; per subject the mean of the two runs; grand mean with a
subject-bootstrap 95 % CI (10,000 draws, seed 20261120; boot_idx()) and an exact two-sided sign-flip p over the 14
subjects (2^14 assignments); count positive; per run type.
"""
import numpy as np

SEED = 20261120
N_BOOT = 10000
TERMS = ("run", "wd", "means", "within", "pool", "eps", "d60", "d60_winsign")
SIGNS14 = ((np.arange(1 << 14)[:, None] >> np.arange(14)) & 1) * 2 - 1        # 16,384 sign assignments


def parts(C):
    """(d_xy, d_yx, a_x, a_y, q) from (…, 4, 4) matrices."""
    ax, ay = C[..., 0, 2], C[..., 1, 3]
    q = 0.5 * (C[..., 0, 1] + C[..., 2, 3])
    return C[..., 0, 3] - ay * q, C[..., 1, 2] - ax * q, ax, ay, q


def budget_terms(C_run, C_wd, C_win, sd_win, n_win, s):
    """
    C_run  (n, 4, 4)      run-level matrices
    C_wd   (n, 4, 4)      run-level matrices after removing each region's mean within each window
    C_win  (n, NW, 4, 4)  window matrices
    sd_win (n, NW, 2)     population SD (ddof = 0) of x and of y over each window's TRs
    n_win  (NW,)          number of TRs in each window (the same for every pair of a run)
    s      (n,)           per-pair weight (the sign of the run-level q)
    Returns a dict of per-pair arrays (n,) for every term in TERMS, plus a, absq, q, sumpi.
    """
    n, NW = C_win.shape[:2]
    n_win = np.asarray(n_win, float)
    assert n_win.shape == (NW,) and sd_win.shape == (n, NW, 2) and C_run.shape == C_wd.shape == (n, 4, 4)
    dxy, dyx, ax, ay, q = parts(C_run)
    d_run = 0.5 * (dxy + dyx)
    dxy_wd, dyx_wd, _, _, _ = parts(C_wd)
    d_wd = 0.5 * (dxy_wd + dyx_wd)
    dw_xy, dw_yx, axw, ayw, qw = parts(C_win)                            # (n, NW)
    sx, sy = sd_win[:, :, 0], sd_win[:, :, 1]
    N = n_win.sum()
    Sx2 = (n_win * sx ** 2).sum(1, keepdims=True) / N
    Sy2 = (n_win * sy ** 2).sum(1, keepdims=True) / N
    pi = n_win * sx * sy / (N * np.sqrt(Sx2 * Sy2))
    psx = n_win * sx ** 2 / (N * Sx2)
    psy = n_win * sy ** 2 / (N * Sy2)
    abx = (psx * axw).sum(1, keepdims=True)
    aby = (psy * ayw).sum(1, keepdims=True)
    within = 0.5 * ((pi * dw_xy).sum(1) + (pi * dw_yx).sum(1))
    pool = 0.5 * ((pi * (ayw - aby) * qw).sum(1) + (pi * (axw - abx) * qw).sum(1))
    dw = 0.5 * (dw_xy + dw_yx)
    out = dict(run=s * d_run, wd=s * d_wd, within=s * within, pool=s * pool,
               d60=s * dw.mean(1), d60_winsign=(np.sign(qw) * dw).mean(1),
               a=0.5 * (ax + ay), absq=np.abs(q), q=q, sumpi=pi.sum(1))
    out["means"] = out["run"] - out["wd"]
    out["eps"] = out["wd"] - out["within"] - out["pool"]
    return out


def c4_series(X, Y):
    """phyid-style (n, 4, 4) matrices of [x_t, y_t, x_{t+1}, y_{t+1}] for (n, T) arrays: past and future blocks
    standardised separately (ddof = 1), the same construction as PairPhiID for one pair and as window_corr."""
    P = np.stack([X[:, :-1], Y[:, :-1]], 1)
    F = np.stack([X[:, 1:], Y[:, 1:]], 1)
    P = (P - P.mean(2, keepdims=True)) / P.std(2, ddof=1, keepdims=True)
    F = (F - F.mean(2, keepdims=True)) / F.std(2, ddof=1, keepdims=True)
    Z = np.concatenate([P, F], 1)
    return np.einsum("nit,njt->nij", Z, Z) / (Z.shape[2] - 1)


def mats_from_series(X, Y, W=60):
    """For simulated pair series (n, T) with T a multiple of W: the five inputs of budget_terms plus s."""
    n, T = X.shape
    NW = T // W
    assert NW * W == T
    Xw, Yw = X.reshape(n, NW, W), Y.reshape(n, NW, W)
    C_run = c4_series(X, Y)
    Xd = (Xw - Xw.mean(2, keepdims=True)).reshape(n, T)
    Yd = (Yw - Yw.mean(2, keepdims=True)).reshape(n, T)
    C_wd = c4_series(Xd, Yd)
    C_win = np.empty((n, NW, 4, 4))
    for w in range(NW):
        C_win[:, w] = c4_series(Xw[:, w], Yw[:, w])
    sd_win = np.stack([Xw.std(2), Yw.std(2)], 2)
    s = np.sign(0.5 * (C_run[:, 0, 1] + C_run[:, 2, 3]))
    return C_run, C_wd, C_win, sd_win, np.full(NW, W), s


def boot_idx(seed=SEED, n_boot=N_BOOT, n_subj=14):
    return np.random.default_rng(seed).integers(0, n_subj, (n_boot, n_subj))


def boot_idx_variants(variants=("ts_gsr", "ts_demean"), seed=SEED, n_boot=N_BOOT, n_subj=14):
    """One set of bootstrap draws per variant from one generator, in this order, shared by every term of the variant
    and by partB12 and partB13 (so the null-corrected intervals are the data intervals shifted by the null value)."""
    rng = np.random.default_rng(seed)
    return {v: rng.integers(0, n_subj, (n_boot, n_subj)) for v in variants}


def aggregate(per_run, idx):
    """per_run (14, 2): mean over pairs per subject and run (column 0 DMT, 1 placebo). Returns a dict with the grand
    mean over subjects of the per-subject mean of the two runs, its bootstrap CI, exact sign-flip p, count positive,
    and the per-run-type means with their CIs."""
    per_subj = per_run.mean(1)
    grand = per_subj.mean()
    boot = per_subj[idx].mean(1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    null = (SIGNS14 * per_subj).mean(1)
    p = float(np.mean(np.abs(null) >= abs(grand) - 1e-15))
    out = dict(grand=grand, lo=lo, hi=hi, p=p, npos=int((per_subj > 0).sum()), per_subj=per_subj)
    for k, name in enumerate(("dmt", "pcb")):
        v = per_run[:, k]
        b = v[idx].mean(1)
        out[name] = v.mean()
        out[name + "_lo"], out[name + "_hi"] = np.percentile(b, [2.5, 97.5])
    return out


def signflip_p(values):
    """exact two-sided sign-flip p over 14 per-subject values."""
    values = np.asarray(values, float)
    null = (SIGNS14 * values).mean(1)
    return float(np.mean(np.abs(null) >= abs(values.mean()) - 1e-15))


def fmt_agg(name, r, digits=5):
    return (f"{name}: DMT {r['dmt']:+.{digits}f} [{r['dmt_lo']:+.{digits}f}, {r['dmt_hi']:+.{digits}f}], "
            f"PCB {r['pcb']:+.{digits}f} [{r['pcb_lo']:+.{digits}f}, {r['pcb_hi']:+.{digits}f}]; grand mean {r['grand']:+.{digits}f} "
            f"[{r['lo']:+.{digits}f}, {r['hi']:+.{digits}f}] (subject bootstrap, {N_BOOT} draws), exact sign-flip p = {r['p']:.4f}, "
            f"positive in {r['npos']}/14 subjects")
