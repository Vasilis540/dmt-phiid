"""
check_A1_atoms_family.py  -- independent verification of the paper's analytic account (Part A).

Independent implementation of the Gaussian PhiID lattice with MMI redundancy and
Moebius inversion, written from the definitions (Barrett 2015 MMI; Mediano et al. 2021
product lattice), NOT from notes/rev_phiid_fast.py.  Cross-checked against `phyid`
(commit 6c5f2e9d..., the commit pinned in requirements.lock.txt).

Verifies, for the bivariate AR(1) family of Methods ("Closed-form atoms of a bivariate
AR(1) pair"):
  1. the 16 atoms claimed in Methods
  2. sts = -ln(1-a^2) + 0.5*ln(1-a^2 q^2)
  3. the two derivatives
  4. derivative ratio: the 32-fold claim, the "0 of 18,336 / 0 of 36,481" counts,
     and the minima of Figure 2(c)
  5. the shared-slow-component formula d = q(1-lam_y)(a_s-a_n) and the tau=1
     equivalence with lagged coupling
  6. d(sts)/d(cross-lag correlation) used for the "44 % / 37 %" reading of Results 4
"""
import itertools, numpy as np

# ---------------------------------------------------------------- lattice ----
# single redundancy lattice for 2 sources: 0='r' ({1}{2}), 1='x' ({1}), 2='y' ({2}), 3='s' ({12})
NAMES = ['r', 'x', 'y', 's']
# subsets of {0,1} that each node stands for, as a source/target *collection*
NODE_SETS = {0: [(0,), (1,)], 1: [(0,)], 2: [(1,)], 3: [(0, 1)]}
# partial order on the single lattice (a <= b)
LEQ = np.array([[1,1,1,1],
                [0,1,0,1],
                [0,0,1,1],
                [0,0,0,1]], dtype=bool)

def prod_leq(n1, n2):
    """(a1,b1) <= (a2,b2) in the product lattice."""
    return LEQ[n1[0], n2[0]] and LEQ[n1[1], n2[1]]

# --------------------------------------------------------- gaussian MI -------
def mi(S, A, B):
    """Gaussian mutual information I(A;B), A/B index tuples into correlation matrix S."""
    A, B = list(A), list(B)
    dA = np.linalg.det(S[np.ix_(A, A)])
    dB = np.linalg.det(S[np.ix_(B, B)])
    dAB = np.linalg.det(S[np.ix_(A + B, A + B)])
    return 0.5 * np.log(dA * dB / dAB)

def mmi_cum(S):
    """
    I_cap^{alpha->beta} for all 16 product-lattice nodes, MMI redundancy.
    Variable order in S: (x_t, y_t, x_{t+1}, y_{t+1}); past = 0,1 ; future = 2,3.
    """
    past = {0: [(0,), (1,)], 1: [(0,)], 2: [(1,)], 3: [(0, 1)]}
    fut  = {0: [(2,), (3,)], 1: [(2,)], 2: [(3,)], 3: [(2, 3)]}
    cum = {}
    for a in range(4):
        for b in range(4):
            # MMI: minimum over every (source-collection member, target-collection member) pair
            cum[(a, b)] = min(mi(S, A, B) for A in past[a] for B in fut[b])
    return cum

def phiid_mmi(S):
    """Moebius inversion of the MMI cumulative function over the product lattice."""
    cum = mmi_cum(S)
    nodes = [(a, b) for a in range(4) for b in range(4)]
    # order nodes so that every strict predecessor comes first
    nodes.sort(key=lambda n: (bin(n[0]).count('1') + bin(n[1]).count('1'), n))
    order = sorted(nodes, key=lambda n: sum(LEQ[:, n[0]]) + sum(LEQ[:, n[1]]))
    atoms = {}
    for n in order:
        s = 0.0
        for m in order:
            if m != n and prod_leq(m, n):
                s += atoms[m]
        atoms[n] = cum[n] - s
    return {NAMES[a] + 't' + NAMES[b]: v for (a, b), v in atoms.items()}

# --------------------------------------------------- the AR(1) family --------
def S4_ar1(a, q, ax=None, ay=None):
    """(x_t, y_t, x_{t+1}, y_{t+1}) correlation matrix of the Methods family."""
    if ax is None: ax = a
    if ay is None: ay = a
    # corr(x_t,y_t)=q ; corr(x_t,x_{t+1})=ax ; corr(y_t,y_{t+1})=ay
    # corr(x_t,y_{t+1})=ay*q ; corr(y_t,x_{t+1})=ax*q ; corr(x_{t+1},y_{t+1})=q
    return np.array([[1,     q,     ax,    ay*q],
                     [q,     1,     ax*q,  ay  ],
                     [ax,    ax*q,  1,     q   ],
                     [ay*q,  ay,    q,     1   ]], float)

def sts_closed(a, q):
    return -np.log(1 - a**2) + 0.5 * np.log(1 - a**2 * q**2)

out = []
P = out.append
P("=" * 78)
P("1. THE SIXTEEN ATOMS ON THE FAMILY, against the Methods claims")
P("=" * 78)
P("Methods claims: rtx=rty=xtr=ytr=xty=ytx=0 ; xtx=yty=rts=str=S-C ;")
P("                xts=yts=stx=sty=-(S-C) ; rtr=C ; sts=2S-C")
P("  with S=-0.5 ln(1-a^2), C=-0.5 ln(1-a^2 q^2)")
P("")
worst = {}
for a in [0.2, 0.5, 0.75, 0.85, 0.9, 0.95]:
    for q in [-0.6, -0.25, 0.0, 0.1, 0.25, 0.4, 0.6, 0.9]:
        S4 = S4_ar1(a, q)
        if np.linalg.eigvalsh(S4).min() <= 1e-12:
            continue
        at = phiid_mmi(S4)
        S = -0.5 * np.log(1 - a**2)
        C = -0.5 * np.log(1 - a**2 * q**2)
        pred = {'rtr': C, 'rtx': 0, 'rty': 0, 'rts': S - C,
                'xtr': 0, 'xtx': S - C, 'xty': 0, 'xts': -(S - C),
                'ytr': 0, 'ytx': 0, 'yty': S - C, 'yts': -(S - C),
                'str': S - C, 'stx': -(S - C), 'sty': -(S - C), 'sts': 2 * S - C}
        for k in pred:
            e = abs(at[k] - pred[k])
            worst[k] = max(worst.get(k, 0.0), e)
P("max |atom - Methods prediction| over 48 (a,q) settings, per atom:")
for k in ['rtr','rtx','rty','rts','xtr','xtx','xty','xts','ytr','ytx','yty','yts','str','stx','sty','sts']:
    P(f"   {k}: {worst[k]:.3e}")
P(f"  OVERALL MAX: {max(worst.values()):.3e}")
P("")

P("=" * 78)
P("2. CROSS-CHECK MY LATTICE AGAINST phyid (kind='gaussian', tau=1, redundancy='MMI')")
P("=" * 78)
try:
    from phyid.calculate import calc_PhiID
    from phyid.utils import PhiID_atoms_abbr
    rng = np.random.default_rng(20261120)
    for (a, q, n) in [(0.85, 0.25, 400000), (0.6, -0.4, 400000)]:
        # simulate the exact family
        e = rng.multivariate_normal([0, 0], [[1, q], [q, 1]], size=n) * np.sqrt(1 - a**2)
        x = np.zeros(n); y = np.zeros(n)
        for t in range(1, n):
            x[t] = a * x[t-1] + e[t, 0]
            y[t] = a * y[t-1] + e[t, 1]
        x, y = x[1000:], y[1000:]
        atoms_ph, _ = calc_PhiID(x, y, tau=1, kind='gaussian', redundancy='MMI')
        ph = {k: float(np.mean(v)) for k, v in zip(PhiID_atoms_abbr, np.array([atoms_ph[k] for k in PhiID_atoms_abbr]))}
        # my lattice on the *sample* 4x4 correlation matrix (plug-in), same estimator
        Z = np.column_stack([x[:-1], y[:-1], x[1:], y[1:]])
        Zc = (Z - Z.mean(0)) / Z.std(0)
        Ssamp = np.corrcoef(Zc.T)
        mine = phiid_mmi(Ssamp)
        P(f"  a={a}, q={q}, n={len(x)}:")
        md = max(abs(mine[k] - ph[k]) for k in mine)
        P(f"    max |mine(plug-in 4x4) - phyid time-mean| over 16 atoms = {md:.3e}")
        P(f"    phyid sts = {ph['sts']:.6f}   mine = {mine['sts']:.6f}   "
          f"analytic = {sts_closed(a,q):.6f}")
except Exception as ex:
    P(f"  phyid check FAILED: {ex!r}")
P("")

P("=" * 78)
P("3. sts CLOSED FORM, DERIVATIVES, AND THE FOLD CLAIM")
P("=" * 78)
def dsts_da(a, q): return 2*a/(1-a**2) - a*q**2/(1-a**2*q**2)
def dsts_dq(a, q): return -a**2*q/(1-a**2*q**2)
# numerical derivative of the *lattice* sts, not of the closed form
def num_d(a, q, h=1e-6):
    fa = (phiid_mmi(S4_ar1(a+h, q))['sts'] - phiid_mmi(S4_ar1(a-h, q))['sts'])/(2*h)
    fq = (phiid_mmi(S4_ar1(a, q+h))['sts'] - phiid_mmi(S4_ar1(a, q-h))['sts'])/(2*h)
    return fa, fq
for (a, q) in [(0.85, 0.25), (0.85, 0.6), (0.848, 0.24), (0.87, 0.25), (0.97, 0.25),
               (0.78, 0.25), (0.93, 0.25), (0.84, 0.2), (0.84, 0.3)]:
    na, nq = num_d(a, q)
    P(f"  (r1={a}, q={q}): d/dr1 analytic {dsts_da(a,q):+.4f} lattice {na:+.4f} | "
      f"d/dq analytic {dsts_dq(a,q):+.4f} lattice {nq:+.4f} | "
      f"ratio {abs(dsts_da(a,q)/dsts_dq(a,q)):.2f}")
P("")
P(f"  sts(0.85,0)   = {sts_closed(0.85,0.0):.4f}   [paper 1.282]")
P(f"  sts(0.85,0.6) = {sts_closed(0.85,0.6):.4f}   [paper 1.131]")
for r in [0.2,0.6,0.8,0.85,0.9,0.95]:
    P(f"  sts(r1={r}, q=0) = {sts_closed(r,0.0):.4f}")
P("")

P("=" * 78)
P("4. GRID COUNTS AND THE MINIMUM OF FIGURE 2(c)")
P("=" * 78)
def grid_counts(rmin, rmax, qmin, qmax, step=0.01):
    r = np.round(np.arange(rmin, rmax + step/2, step), 10)
    q = np.round(np.arange(qmin, qmax + step/2, step), 10)
    R, Q = np.meshgrid(r, q, indexing='ij')
    with np.errstate(divide='ignore', invalid='ignore'):
        da = np.abs(dsts_da(R, Q)); dq = np.abs(dsts_dq(R, Q))
    n = R.size
    q_dom_strict = int(np.sum(dq > da))
    ties = int(np.sum(dq == da))
    return r, q, R, Q, da, dq, n, q_dom_strict, ties

for (lab, rr, qq) in [("|q|<=0.6 grid (Fig 2a/2b)", (0.0, 0.95), (-0.6, 0.6)),
                      ("|q|<=0.95 grid (Fig 2c)",   (0.0, 0.95), (-0.95, 0.95)),
                      ("r in [-0.95,0.95]^2 (lag)", (-0.95, 0.95), (-0.95, 0.95))]:
    r, q, R, Q, da, dq, n, qd, ties = grid_counts(rr[0], rr[1], qq[0], qq[1])
    P(f"  {lab}: {len(r)} x {len(q)} = {n} points; "
      f"points with |d/dq| > |d/dr1|: {qd}; exact ties: {ties}")
    ratio = np.where(dq > 0, da/np.where(dq==0, np.nan, dq), np.inf)
    m = np.nanmin(ratio)
    idx = np.unravel_index(np.nanargmin(ratio), ratio.shape)
    P(f"     min finite ratio = {m:.3f} at (r1={R[idx]:.2f}, q={Q[idx]:.2f})")
P("")

P("=" * 78)
P("5. SHARED SLOW COMPONENT, d, AND THE tau=1 EQUIVALENCE")
P("=" * 78)
lam, a_s, a_n = 0.25, 0.95, 0.80
# x = s + nx, y = s + ny, var(s)/var(x) = var(s)/var(y) = lam
vs, vn = lam, 1 - lam
q = vs / np.sqrt((vs+vn)*(vs+vn))
a_x = lam*a_s + (1-lam)*a_n
xl_true = q * a_s
d = q*(1-lam)*(a_s-a_n)
P(f"  worked example lam={lam}, a_s={a_s}, a_n={a_n}:")
P(f"    q = {q:.6f} [paper 0.25]; a = {a_x:.6f} [paper 0.8375]")
P(f"    true cross-lag corr = {xl_true:.6f} [paper 0.2375]")
P(f"    d formula q(1-lam_y)(a_s-a_n) = {d:.6f} [paper +0.028125]")
P(f"    d direct = true - a*q = {xl_true - a_x*q:.6f}  -> match {abs(d-(xl_true-a_x*q)):.2e}")
# the VAR(1) with a=0.83, c=0.03
G0 = np.array([[1, q], [q, 1]])
A = np.array([[0.83, 0.03], [0.03, 0.83]])
G1 = A @ G0
Sig = G0 - A @ G0 @ A.T
P(f"    VAR(1) a=0.83,c=0.03: r1 = {G1[0,0]:.6f}, cross-lag = {G1[0,1]:.6f}, "
  f"q_eps = {Sig[0,1]/Sig[0,0]:.6f} [paper 0.093]")
P(f"    d = c(1-q^2) = {0.03*(1-q**2):.6f}")
# the two 4x4 matrices
S_slow = np.array([[1, q, a_x, xl_true],
                   [q, 1, xl_true, a_x],
                   [a_x, xl_true, 1, q],
                   [xl_true, a_x, q, 1]])
S_var = np.block([[G0, G1.T], [G1, G0]])
P(f"    max |S4(slow) - S4(VAR)| = {np.abs(S_slow-S_var).max():.3e}")
at_s, at_v = phiid_mmi(S_slow), phiid_mmi(S_var)
P(f"    max |atoms(slow) - atoms(VAR)| over 16 = "
  f"{max(abs(at_s[k]-at_v[k]) for k in at_s):.3e}")
# the general claim: A = G1 G0^-1, Sigma = G0 - A G0 A' is PD and A is stable
rng = np.random.default_rng(7)
bad = 0; nchk = 0
for _ in range(20000):
    M = rng.normal(size=(4, 4)); S = M @ M.T
    dg = np.sqrt(np.diag(S)); S = S / np.outer(dg, dg)
    # force the stationary block structure  [[G0,G1'],[G1,G0]]
    G0_ = S[:2, :2]; G1_ = S[2:, :2]
    Sfull = np.block([[G0_, G1_.T], [G1_, G0_]])
    if np.linalg.eigvalsh(Sfull).min() <= 1e-10:
        continue
    nchk += 1
    A_ = G1_ @ np.linalg.inv(G0_)
    Sig_ = G0_ - A_ @ G0_ @ A_.T
    if np.linalg.eigvalsh((Sig_+Sig_.T)/2).min() <= -1e-10: bad += 1
    if np.max(np.abs(np.linalg.eigvals(A_))) >= 1 - 1e-12: bad += 1
P(f"  general claim: over {nchk} random PD stationary 4x4 blocks, "
  f"violations of (Sigma PSD and rho(A)<1): {bad}")
P("")

P("=" * 78)
P("6. d(sts)/d(cross-lag corr): the scale used for the 44 %/37 % reading")
P("=" * 78)
for (a, q, lab) in [(0.85, 0.25, "operating point"), (0.848, 0.24, "pairs' mean point")]:
    h = 1e-5
    def sts_xl(delta):
        S = S4_ar1(a, q)
        S[0, 3] = S[3, 0] = a*q + delta
        S[1, 2] = S[2, 1] = a*q + delta
        return phiid_mmi(S)['sts']
    slope = (sts_xl(h) - sts_xl(-h)) / (2*h)
    P(f"  {lab} (r1={a}, q={q}): d sts / d(cross-lag corr) = {slope:+.4f} nats per unit")
    P(f"     delta_run=+0.00340 -> {slope*0.00340:+.6f} nats;"
      f"  as share of run-level residual -0.0137: {abs(slope*0.00340/0.0137)*100:.1f} %")
    P(f"     using the coupled family's -1.77 per unit c instead: "
      f"{-1.77*0.00340:+.6f} -> {abs(-1.77*0.0034/0.0137)*100:.1f} %")
# and the coupled-family slope itself, in c
def sts_c(a_, c_, qe):
    A_ = np.array([[a_, c_], [c_, a_]])
    # stationary covariance from the discrete Lyapunov equation
    Sig_ = np.array([[1.0, qe], [qe, 1.0]])
    G = np.eye(2); 
    for _ in range(200000):
        Gn = A_ @ G @ A_.T + Sig_
        if np.abs(Gn - G).max() < 1e-15: G = Gn; break
        G = Gn
    dg = np.sqrt(np.diag(G)); G0_ = G/np.outer(dg,dg)
    G1_ = (A_ @ G)/np.outer(dg,dg)
    return np.block([[G0_, G1_.T],[G1_, G0_]])
P("")
P("  coupled family at the operating point: re-solving (a,q_eps) so that (r1,q)=(0.85,0.25)")
from scipy.optimize import fsolve
def solve_ac(c):
    def f(v):
        S = sts_c(v[0], c, v[1]);  return [S[0,2]-0.85, S[0,1]-0.25]
    v = fsolve(f, [0.85, 0.25], full_output=False)
    return v
rows = {}
for c in [-0.05, -0.02, 0.0, 0.02, 0.05]:
    v = solve_ac(c); S = sts_c(v[0], c, v[1]); rows[c] = phiid_mmi(S)['sts']
    P(f"    c={c:+.2f}: a={v[0]:.5f}, q_eps={v[1]:.5f}, r1={S[0,2]:.5f}, q={S[0,1]:.5f}, "
      f"sts={rows[c]:.4f}")
P(f"    paper's table rows: c=+0.02 1.2315, -0.02 1.3023, +0.05 1.2155, -0.05 1.4111, c=0 1.2588")
P(f"    slope from +-0.02: {(rows[0.02]-rows[-0.02])/0.04:+.3f} nats per unit c  [paper -1.77]")
P(f"    curvature from +-0.02: "
  f"{(rows[0.02]+rows[-0.02]-2*rows[0.0])/0.02**2:+.1f} nats per unit c^2  [paper +40]")
print("\n".join(out))
