# shared budget function for the verification checks (synthetic only)
import numpy as np

def c4_blocks(X, Y):
    """phyid-style 4x4 for (n, T) arrays: past/future standardised separately, ddof=1."""
    P = np.stack([X[:, :-1], Y[:, :-1]], 1); F = np.stack([X[:, 1:], Y[:, 1:]], 1)
    P = (P - P.mean(2, keepdims=True)) / P.std(2, ddof=1, keepdims=True)
    F = (F - F.mean(2, keepdims=True)) / F.std(2, ddof=1, keepdims=True)
    Z = np.concatenate([P, F], 1)
    return np.einsum('nit,njt->nij', Z, Z) / (Z.shape[2] - 1)

def parts(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    return C[:, 0, 3] - ay * q, C[:, 1, 2] - ax * q, ax, ay, q

def budget(X, Y, W=60, return_pairs=False):
    n, T = X.shape; NW = T // W
    dxy, dyx, ax, ay, q = parts(c4_blocks(X, Y)); s = np.sign(q)
    d_run = s * 0.5 * (dxy + dyx)
    Xw = X.reshape(n, NW, W); Yw = Y.reshape(n, NW, W)
    Xd = (Xw - Xw.mean(2, keepdims=True)).reshape(n, T); Yd = (Yw - Yw.mean(2, keepdims=True)).reshape(n, T)
    a1, a2, *_ = parts(c4_blocks(Xd, Yd)); d_wd = s * 0.5 * (a1 + a2)
    dw1 = np.empty((n, NW)); dw2 = np.empty((n, NW)); axw = np.empty((n, NW)); ayw = np.empty((n, NW)); qw = np.empty((n, NW))
    for w in range(NW):
        dw1[:, w], dw2[:, w], axw[:, w], ayw[:, w], qw[:, w] = parts(c4_blocks(Xw[:, w], Yw[:, w]))
    sx = Xw.std(2, ddof=1); sy = Yw.std(2, ddof=1)
    Sx2 = (sx ** 2).mean(1, keepdims=True); Sy2 = (sy ** 2).mean(1, keepdims=True)
    pi = (sx * sy) / (NW * np.sqrt(Sx2 * Sy2))
    psx = sx ** 2 / (NW * Sx2); psy = sy ** 2 / (NW * Sy2)
    abx = (psx * axw).sum(1, keepdims=True); aby = (psy * ayw).sum(1, keepdims=True)
    within = s * 0.5 * ((pi * dw1).sum(1) + (pi * dw2).sum(1))
    aq = s * 0.5 * ((pi * (ayw - aby) * qw).sum(1) + (pi * (axw - abx) * qw).sum(1))
    # split of aq: pi-normalised covariance part and weight-mismatch part
    pit = pi / pi.sum(1, keepdims=True); spi = pi.sum(1)
    aq_cov = s * 0.5 * spi * (((pit * ayw).sum(1) * 0 + (pit * (ayw - (pit * ayw).sum(1, keepdims=True)) * qw).sum(1)) + (pit * (axw - (pit * axw).sum(1, keepdims=True)) * qw).sum(1))
    d60 = s * 0.5 * (dw1.mean(1) + dw2.mean(1))
    out = dict(run=d_run, wd=d_wd, means=d_run - d_wd, within=within, aq=aq, aq_cov=aq_cov, aq_wt=aq - aq_cov,
               eps=d_wd - within - aq, d60=d60, a=0.5 * (ax + ay), absq=np.abs(q), q=q, sumpi=spi)
    return out if return_pairs else {k: (v.mean(), v.std() / np.sqrt(v.size)) for k, v in out.items()}

def fmt(r, keys=("run", "within", "aq", "means", "eps", "d60", "a", "absq")):
    return "  ".join(f"{k} {r[k][0]:+.5f}({r[k][1]:.5f})" for k in keys)
