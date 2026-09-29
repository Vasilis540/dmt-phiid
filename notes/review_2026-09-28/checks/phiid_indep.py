"""Independent Gaussian-MMI PhiID from a 4x4 covariance of (x_t, y_t, x_{t+1}, y_{t+1}), written from the
lattice definitions (Mediano et al. 2021, Appendix), without reference to phyid or the repository's code."""
import numpy as np, itertools
L = ['r', 'x', 'y', 's']            # {1}{2}, {1}, {2}, {12}
LE = {('r','r'),('r','x'),('r','y'),('r','s'),('x','x'),('x','s'),('y','y'),('y','s'),('s','s')}  # partial order <=
def le(a, b): return (a, b) in LE
def mi(C, A, B):
    A, B = list(A), list(B)
    d = lambda I: np.linalg.det(C[np.ix_(I, I)])
    return 0.5 * np.log(d(A) * d(B) / d(A + B))
P = {'x': [0], 'y': [1], 's': [0, 1]}     # past index sets
F = {'x': [2], 'y': [3], 's': [2, 3]}     # future index sets
def red(C, a, b):
    """MMI double-redundancy / redundancy / MI at node a->b."""
    if a != 'r' and b != 'r':
        return mi(C, P[a], F[b])
    if a == 'r' and b != 'r':   # sources X1, X2 (pasts), target F[b]
        return min(mi(C, [0], F[b]), mi(C, [1], F[b]))
    if a != 'r' and b == 'r':   # backward: sources Y1, Y2 (futures), target P[a]
        return min(mi(C, P[a], [2]), mi(C, P[a], [3]))
    return min(mi(C, [i], [j]) for i in (0, 1) for j in (2, 3))
def atoms(C):
    nodes = list(itertools.product(L, L))
    # topological order: by rank
    rank = {'r': 0, 'x': 1, 'y': 1, 's': 2}
    nodes.sort(key=lambda n: rank[n[0]] + rank[n[1]])
    A = {}
    for (a, b) in nodes:
        below = [(c, d) for (c, d) in A if le(c, a) and le(d, b) and (c, d) != (a, b)]
        A[(a, b)] = red(C, a, b) - sum(A[n] for n in below)
    return {f"{a}t{b}": v for (a, b), v in A.items()}
def ar1_cov(ax, ay, q):
    return np.array([[1, q, ax, ay*q], [q, 1, ax*q, ay], [ax, ax*q, 1, q], [ay*q, ay, q, 1]], float)
if __name__ == '__main__':
    worst = {}
    for a in [0.3, 0.6, 0.85, 0.95]:
        for q in [-0.6, -0.25, 0.0, 0.25, 0.7]:
            At = atoms(ar1_cov(a, a, q))
            S = -0.5*np.log(1-a*a); Cc = -0.5*np.log(1-a*a*q*q)
            chk = {'sts=2S-C': At['sts']-(2*S-Cc), 'xtx=S-C': At['xtx']-(S-Cc), 'rts=S-C': At['rts']-(S-Cc),
                   'xts=-(S-C)': At['xts']+(S-Cc), 'rtr=C': At['rtr']-Cc,
                   'zero atoms': max(abs(At[k]) for k in ['rtx','rty','xtr','ytr','xty','ytx']),
                   'sts-(xtx+yty)=rtr': At['sts']-(At['xtx']+At['yty'])-At['rtr'],
                   'TDMI=2S': sum(At.values())-2*S, 'aggregate=S': At['str']+At['stx']+At['sty']+At['sts']-S}
            for k, v in chk.items(): worst[k] = max(worst.get(k, 0), abs(v))
    for k, v in worst.items(): print(f"{k:22s} max |dev| = {v:.1e}")
    # derivatives at the operating point
    f = lambda a, q: atoms(ar1_cov(a, a, q))['sts']; h = 1e-6
    print('d sts/d r1 at (0.85,0.25):', (f(0.85+h, .25)-f(0.85-h, .25))/(2*h))
    print('d sts/d q  at (0.85,0.25):', (f(0.85, .25+h)-f(0.85, .25-h))/(2*h))
    # unequal coefficients, q = 0: sts = 2 min(Sx, Sy), rtr = 0
    for ax, ay in [(0.8, 0.9), (0.85, 0.86), (0.6, 0.95)]:
        At = atoms(ar1_cov(ax, ay, 0.0)); Sx, Sy = -0.5*np.log(1-ax*ax), -0.5*np.log(1-ay*ay)
        print(f"q=0 ax={ax} ay={ay}: sts-2min(S) = {At['sts']-2*min(Sx,Sy):.1e}, rtr = {At['rtr']:.1e}")
    # the excess sts-(xtx+yty) changes sign near |ax-ay| = 0.008 at (0.85, 0.25)
    for d in [0.004, 0.006, 0.008, 0.010, 0.012]:
        At = atoms(ar1_cov(0.85+d/2, 0.85-d/2, 0.25)); print(f"asym {d:.3f}: sts-(xtx+yty) = {At['sts']-At['xtx']-At['yty']:+.5f}")
    # d sts / d asymmetry at (0.85, 0.25)
    g = lambda d: atoms(ar1_cov(0.85+d/2, 0.85-d/2, 0.25))['sts']
    print('sts change for 0.01 asymmetry:', g(0.01)-g(0.0))
