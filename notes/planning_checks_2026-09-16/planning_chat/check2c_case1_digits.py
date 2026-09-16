# debug: does the pooling term recover the population covariance of a and q across windows?
import numpy as np
rng = np.random.default_rng(11)
W, NW = 60, 14; T = W*NW; n = 20000

def c4(X, Y):
    P = np.stack([X[:, :-1], Y[:, :-1]], 1); F = np.stack([X[:, 1:], Y[:, 1:]], 1)
    P = (P - P.mean(2, keepdims=True))/P.std(2, ddof=1, keepdims=True); F = (F - F.mean(2, keepdims=True))/F.std(2, ddof=1, keepdims=True)
    Z = np.concatenate([P, F], 1); return np.einsum('nit,njt->nij', Z, Z)/(Z.shape[2]-1)

def dev(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5*(C[:, 0, 1] + C[:, 2, 3])
    return C[:, 0, 3] - ay*q, C[:, 1, 2] - ax*q, ax, ay, q

def run(var_het, mean_shift, cov_scale):
    X = np.empty((n, T)); Y = np.empty((n, T)); A = np.empty((n, NW)); Q = np.empty((n, NW))
    sgn = rng.choice([-1, 1], n); base_q = rng.uniform(0.1, 0.4, n)
    for w in range(NW):
        aw = np.clip(0.80 + 0.06*rng.standard_normal(n), 0.5, 0.95)
        qabs = np.clip(base_q + cov_scale*(aw - 0.80), 0.0, 0.9); qw = sgn*qabs
        A[:, w] = aw; Q[:, w] = qw
        e1 = rng.standard_normal((n, W)); e2 = qw[:, None]*e1 + np.sqrt(1 - qw[:, None]**2)*rng.standard_normal((n, W))
        x = np.empty((n, W)); y = np.empty((n, W)); x[:, 0] = e1[:, 0]; y[:, 0] = e2[:, 0]
        for t in range(1, W):
            x[:, t] = aw*x[:, t-1] + np.sqrt(1 - aw**2)*e1[:, t]; y[:, t] = aw*y[:, t-1] + np.sqrt(1 - aw**2)*e2[:, t]
        g = np.exp(var_het*rng.standard_normal(n)); m = mean_shift*rng.standard_normal((n, 1))
        X[:, w*W:(w+1)*W] = g[:, None]*x + m; Y[:, w*W:(w+1)*W] = g[:, None]*y + sgn[:, None]*m
    pop_cov = np.mean(np.mean((A - A.mean(1, keepdims=True))*np.abs(Q), 1))
    dxy, dyx, *_ , q = dev(c4(X, Y)); s = np.sign(q); d_run = np.mean(s*0.5*(dxy + dyx))
    Xwd = X.copy(); Ywd = Y.copy()
    for w in range(NW):
        sl = slice(w*W, (w+1)*W); Xwd[:, sl] -= Xwd[:, sl].mean(1, keepdims=True); Ywd[:, sl] -= Ywd[:, sl].mean(1, keepdims=True)
    a1, a2, *_ = dev(c4(Xwd, Ywd)); d_wd = np.mean(s*0.5*(a1 + a2))
    dxw = np.empty((n, NW)); dyw = np.empty((n, NW)); axw = np.empty((n, NW)); ayw = np.empty((n, NW)); qw_ = np.empty((n, NW)); sx = np.empty((n, NW)); sy = np.empty((n, NW))
    for w in range(NW):
        sl = slice(w*W, (w+1)*W)
        dxw[:, w], dyw[:, w], axw[:, w], ayw[:, w], qw_[:, w] = dev(c4(X[:, sl], Y[:, sl])); sx[:, w] = X[:, sl].std(1, ddof=1); sy[:, w] = Y[:, sl].std(1, ddof=1)
    pi = sx*sy/np.sqrt((sx**2).sum(1, keepdims=True)*(sy**2).sum(1, keepdims=True))
    abx = ((sx**2/(sx**2).sum(1, keepdims=True))*axw).sum(1, keepdims=True); aby = ((sy**2/(sy**2).sum(1, keepdims=True))*ayw).sum(1, keepdims=True)
    within = np.mean(s*0.5*(dxw.mean(1) + dyw.mean(1)))
    dvar = np.mean(s*0.5*((pi*dxw).sum(1) + (pi*dyw).sum(1))) - within
    daq = np.mean(s*0.5*((pi*(ayw - aby)*qw_).sum(1) + (pi*(axw - abx)*qw_).sum(1)))
    print(f"within_pi {within+dvar:+.6f} within {within:+.6f} aq {daq:+.6f} means {d_run-d_wd:+.6f}"); print(f"var_het {var_het:.1f} mean_shift {mean_shift:.1f} cov_scale {cov_scale:.1f}: population cov(a,|q|) {pop_cov:+.5f} | "
          f"d_run {d_run:+.5f} d_wd {d_wd:+.5f} means {d_run - d_wd:+.5f} | within {within:+.5f} var {dvar:+.5f} aq {daq:+.5f} eps {d_wd - within - dvar - daq:+.6f}")

for args in ((0.0, 0.0, 0.0),):
    run(*args)
