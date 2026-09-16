# Where do stationary mechanisms land in the budget? (common slow drive; symmetric VAR(1) coupling). Synthetic only.
import sys, numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/dmt-phiid/notes")
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify")
import review_v2_residual_null as N
from budget import budget
rng = np.random.default_rng(99)
TR = 2.0

def filt(n, T, beta, lo, hi):
    f = np.fft.rfftfreq(T, d=TR); H = np.sqrt(N.psd_weights(f, np.full(n, beta), lo, hi))
    e = rng.standard_normal((n, T)); x = np.fft.irfft(np.fft.rfft(e, axis=1) * H, n=T, axis=1)
    return x / x.std(1, keepdims=True)

def acf1(beta, lo, hi):
    return N.acf_of(beta, lo, hi)[1]

def show(name, X, Y):
    r = budget(X, Y, return_pairs=True)
    m = {k: v.mean() for k, v in r.items()}
    print(f"{name:52s} run {m['run']:+.5f} within {m['within']:+.5f} aq {m['aq']:+.5f} means {m['means']:+.5f} eps {m['eps']:+.5f} d60 {m['d60']:+.5f} | a {m['a']:.3f} |q| {m['absq']:.3f}"
          f"  share within {m['within']/m['run']:.2f} means {m['means']/m['run']:.2f}")

n, T, L = 5000, 840, 4200
for lam, (bs, los, his), (bn, lon, hin) in [
        (0.2, (600, 0.003, 0.05), (100, 0.0064, 0.08)),     # shared part slower, mostly < 0.05 Hz
        (0.2, (800, 0.002, 0.02), (100, 0.0064, 0.08)),     # shared part very slow (periods 50-500 s)
        (0.2, (100, 0.0064, 0.08), (600, 0.003, 0.05)),     # shared part faster
]:
    print(f"lambda {lam}: a_s {acf1(bs, los, his):.3f}, a_n {acf1(bn, lon, hin):.3f}; population d = {lam*(1-lam)*(acf1(bs, los, his)-acf1(bn, lon, hin)):+.5f}")
    o = 1000
    s = filt(n, L, bs, los, his)[:, o:o+T]; nx = filt(n, L, bn, lon, hin)[:, o:o+T]; ny = filt(n, L, bn, lon, hin)[:, o:o+T]
    sg = rng.choice([-1, 1], n)[:, None]
    X = np.sqrt(lam) * s + np.sqrt(1 - lam) * nx; Y = sg * np.sqrt(lam) * s + np.sqrt(1 - lam) * ny
    show(f"  common drive", X, Y)

# symmetric VAR(1) with lagged coupling, the worked example's matrix (a=0.83, c=0.03, q_eps from Sigma)
A = np.array([[0.83, 0.03], [0.03, 0.83]]); G0 = np.array([[1, .25], [.25, 1]]); Se = G0 - A @ G0 @ A.T
Lc = np.linalg.cholesky(Se); burn = 300
Z = np.zeros((n, 2)); Zs = np.empty((n, 2, T))
for t in range(burn + T):
    Z = Z @ A.T + rng.standard_normal((n, 2)) @ Lc.T
    if t >= burn: Zs[:, :, t - burn] = Z
sg = rng.choice([-1, 1], n)[:, None]
show("VAR(1) a=0.83 c=0.03 (worked example)", Zs[:, 0], sg * Zs[:, 1])
