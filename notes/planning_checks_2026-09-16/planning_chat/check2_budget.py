# (c) budget identity on a synthetic non-stationary pair set (NOT the null's generator, NOT data):
#     d_run(window-demeaned) = sum_w pi_w d_w + sum_w pi_w (a_w - abar) q_w + eps
import numpy as np
rng = np.random.default_rng(7)
W, NW = 60, 14; T = W*NW; n = 20000

def c4(X, Y):
    """phyid-style 4x4 of [x_t, y_t, x_t+1, y_t+1], past/future blocks standardised separately (ddof=1)."""
    P = np.stack([X[:, :-1], Y[:, :-1]], 1); F = np.stack([X[:, 1:], Y[:, 1:]], 1)
    P = (P - P.mean(2, keepdims=True))/P.std(2, ddof=1, keepdims=True); F = (F - F.mean(2, keepdims=True))/F.std(2, ddof=1, keepdims=True)
    Z = np.concatenate([P, F], 1); return np.einsum('nit,njt->nij', Z, Z)/(Z.shape[2]-1)

def dev(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5*(C[:, 0, 1] + C[:, 2, 3])
    return C[:, 0, 3] - ay*q, C[:, 1, 2] - ax*q, ax, ay, q

# each window: bivariate AR(1) (diagonal A, correlated innovations) with window-specific a_w, q_w, variance g_w;
# a_w and |q_w| co-vary (pooling present), pair-specific sign of q, x and y variance profiles differ
X = np.empty((n, T)); Y = np.empty((n, T))
sgn = rng.choice([-1, 1], n); base_q = rng.uniform(0.05, 0.5, n)
for w in range(NW):
    aw = np.clip(0.80 + 0.06*rng.standard_normal(n), 0.5, 0.95)
    qw = sgn*np.clip(base_q + 1.5*(aw - 0.80) + 0.03*rng.standard_normal(n), 0.0, 0.9)
    gx = np.exp(0.3*rng.standard_normal(n)); gy = gx*np.exp(0.2*rng.standard_normal(n))
    e1 = rng.standard_normal((n, W)); e2 = qw[:, None]*e1 + np.sqrt(1 - qw[:, None]**2)*rng.standard_normal((n, W))
    x = np.empty((n, W)); y = np.empty((n, W)); x[:, 0] = e1[:, 0]; y[:, 0] = e2[:, 0]
    for t in range(1, W):
        x[:, t] = aw*x[:, t-1] + np.sqrt(1 - aw**2)*e1[:, t]; y[:, t] = aw*y[:, t-1] + np.sqrt(1 - aw**2)*e2[:, t]
    X[:, w*W:(w+1)*W] = gx[:, None]*x + 3.0*rng.standard_normal((n, 1)); Y[:, w*W:(w+1)*W] = gy[:, None]*y + 3.0*sgn[:, None]*rng.standard_normal((n, 1))

# run level, raw and window-demeaned
dxy, dyx, ax, ay, q = dev(c4(X, Y)); s = np.sign(q); D_run = np.mean(s*0.5*(dxy + dyx))
Xwd = X.copy(); Ywd = Y.copy()
for w in range(NW):
    sl = slice(w*W, (w+1)*W); Xwd[:, sl] -= Xwd[:, sl].mean(1, keepdims=True); Ywd[:, sl] -= Ywd[:, sl].mean(1, keepdims=True)
dxy_wd, dyx_wd, *_ = dev(c4(Xwd, Ywd)); D_wd = np.mean(s*0.5*(dxy_wd + dyx_wd))

# window level
dw_xy = np.empty((n, NW)); dw_yx = np.empty((n, NW)); axw = np.empty((n, NW)); ayw = np.empty((n, NW)); qw_ = np.empty((n, NW)); sx = np.empty((n, NW)); sy = np.empty((n, NW))
for w in range(NW):
    sl = slice(w*W, (w+1)*W)
    dw_xy[:, w], dw_yx[:, w], axw[:, w], ayw[:, w], qw_[:, w] = dev(c4(X[:, sl], Y[:, sl]))
    sx[:, w] = X[:, sl].std(1, ddof=1); sy[:, w] = Y[:, sl].std(1, ddof=1)
pi = sx*sy/np.sqrt((sx**2).sum(1, keepdims=True)*(sy**2).sum(1, keepdims=True))
psx = sx**2/(sx**2).sum(1, keepdims=True); psy = sy**2/(sy**2).sum(1, keepdims=True)
abx = (psx*axw).sum(1, keepdims=True); aby = (psy*ayw).sum(1, keepdims=True)
within_pi = 0.5*((pi*dw_xy).sum(1) + (pi*dw_yx).sum(1))
pool = 0.5*((pi*(ayw - aby)*qw_).sum(1) + (pi*(axw - abx)*qw_).sum(1))
D60_eq = np.mean(s*0.5*(dw_xy.mean(1) + dw_yx.mean(1)))
D60_pi = np.mean(s*within_pi); Pn = np.mean(s*pool)
eq_cov = 0.5*(np.mean((ayw - ayw.mean(1, keepdims=True))*qw_, 1) + np.mean((axw - axw.mean(1, keepdims=True))*qw_, 1))
print(f"D_run {D_run:+.5f} | D_run(window-demeaned) {D_wd:+.5f} | R_mean = D_run - D_wd {D_run - D_wd:+.5f}")
print(f"D_60 equal-weight {D60_eq:+.5f} | D_60 pi-weighted {D60_pi:+.5f} | P (pi-weighted) {Pn:+.5f} | P equal-weight {np.mean(s*eq_cov):+.5f}")
print(f"eps = D_wd - D_60pi - P = {D_wd - D60_pi - Pn:+.6f}  (per-pair eps SD {np.std(s*0.5*(dxy_wd+dyx_wd) - s*within_pi - s*pool):.5f}; per-pair d_wd SD {np.std(0.5*(dxy_wd+dyx_wd)):.5f})")
print(f"equal-weight budget remainder D_wd - D_60eq - P_eq = {D_wd - D60_eq - np.mean(s*eq_cov):+.6f}")
