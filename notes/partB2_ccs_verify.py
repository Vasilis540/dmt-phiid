"""
partB2_ccs_verify.py — Part B item 2, step 1: what phyid's CCS branch is, and what it can be
verified against (notes/partB_prespec_2026-09-14.md, B2).

(A) Reference toolbox. phyid pins the MATLAB toolbox pmediano/PhiID at a633cc1 as a git
    submodule ("matlab @ a633cc1"); the checkout is in the uv cache of this environment. Its
    PhiIDFull.m hard-codes RedFun = @RedundancyMMI and DoubleRedFun = @DoubleRedundancyMMI, its
    private/ folder contains DoubleRedundancyMMI.m and DoubleRedundancyMMIDiscrete.m only, and its
    README says the library computes ΦID "using Barrett's Minimum Mutual Info (MMI) redundancy
    function". There is no CCS anywhere in the reference. phyid's redundancy_ccs and
    double_redundacy_ccs (docstrings "To be implemented") therefore have no reference counterpart
    to be compared with. This script records those facts (grep of the reference sources).

(B) Algebra. phyid's CCS double redundancy is the "double co-information"
        D = −I_xta − I_xtb − I_yta − I_ytb + I_xtab + I_ytab + I_xyta + I_xytb − I_xytab
            + R_xyta + R_xytb − R_xytab + R_abtx + R_abty − R_abtxy
    masked to samples where sign(I_xta) = sign(I_xtb) = sign(I_yta) = sign(I_ytb) = sign(D).
    On the ΦID lattice (knowns = M · atoms) D ≡ rtr − sts identically — the four-variable
    analogue of the PID identity co-information = redundancy − synergy that Ince's CCS is built on
    (redundancy = co-information where the signs agree, synergy takes the remainder). Consequence,
    checked numerically below: under phyid's CCS, at every sample where the signs agree sts = 0
    and rtr = D; at every other sample rtr = 0 and sts = −D. So mi_lst[-1] is not an arbitrary
    element: it is D, and the construction is the pointwise-exclusive one of Ince (2017) lifted
    to the double lattice. Whether this is the wording of Mediano et al. (2021/2025) could not be
    confirmed from this session (the paper's full text was not retrievable); it is the only
    definition consistent with the sign-mask logic phyid applies to the six single-target
    redundancies.

(C) Verification against the definition, independently of phyid's code:
    (1) Gaussian: an independent implementation of Ince's CCS (closed-form Gaussian local
        entropies, local MIs, co-information with the four-way sign rule for the six single-target
        redundancies, D with the five-way rule for the double redundancy, lattice solve) compared
        with phyid.calc_PhiID(redundancy="CCS") on 200 random (subject, run, window, pair) draws
        of the real data, all 16 atoms.
    (2) Hand-computable binary case: four binary variables with a tabulated joint distribution;
        every local MI is log2 of a ratio of tabulated probabilities, computed here from the
        table with elementary arithmetic; compared with phyid (kind="discrete", redundancy="CCS").
    (3) The single-target CCS redundancy alone against Ince's definition on the same data.
Outputs: notes/review_results/partB/ccs_verify.log (this script's printout)
"""
import re
import sys
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import _M, KNOWNS, ATOMS, _MI_SETS, _SUBSETS
from phyid.calculate import calc_PhiID

REPO = Path(__file__).resolve().parents[1]
REGIONS = np.array([r for r in range(116) if r != 20])
rng = np.random.default_rng(20261120)
MINV_T = np.linalg.inv(_M).T

# ------------------------------------------------------------------ (A) the reference toolbox
print("== (A) reference MATLAB toolbox pinned by phyid")
import phyid
cands = list(Path("/root/.cache/uv/git-v0/checkouts").glob("*/*/matlab/PhiIDFull.m"))
if cands:
    mdir = cands[0].parent
    src = (mdir / "PhiIDFull.m").read_text()
    print(f"   {mdir}")
    for pat in (r"RedFun = @\w+;", r"DoubleRedFun = @\w+;"):
        for m in re.finditer(pat, src):
            print("   PhiIDFull.m:", m.group(0))
    print("   private/:", sorted(p.name for p in (mdir / "private").iterdir()))
    print("   occurrences of 'ccs' (case-insensitive) in the toolbox:", sum(len(re.findall("ccs", p.read_text(errors='ignore'), re.I)) for p in mdir.rglob("*.m")))
    readme = (mdir / "README.md").read_text()
    for line in readme.splitlines():
        if "MMI" in line and "redundancy" in line.lower():
            print("   README:", line.strip())
    gm = (cands[0].parents[1] / ".gitmodules")
    if gm.exists():
        print("   .gitmodules:", " ".join(gm.read_text().split()))
else:
    print("   (checkout not found)")
import inspect
from phyid import measures
print("   phyid.measures.redundancy_ccs docstring:", inspect.getdoc(measures.redundancy_ccs).splitlines()[-1])
print("   phyid.measures.double_redundacy_ccs docstring:", inspect.getdoc(measures.double_redundacy_ccs).splitlines()[-1])

# ------------------------------------------------------------------ (B) algebra
print("\n== (B) D ≡ rtr − sts on the lattice; pointwise exclusivity under phyid's CCS")
K = {n: i for i, n in enumerate(KNOWNS)}


def D_of(k):
    g = lambda n: k[..., K[n]]
    return (-g("I_xta") - g("I_xtb") - g("I_yta") - g("I_ytb") + g("I_xtab") + g("I_ytab") + g("I_xyta") + g("I_xytb") - g("I_xytab")
            + g("R_xyta") + g("R_xytb") - g("R_xytab") + g("R_abtx") + g("R_abty") - g("R_abtxy"))


worst = 0.0
for _ in range(1000):
    a = rng.standard_normal(16)
    worst = max(worst, abs(D_of(_M @ a) - (a[0] - a[15])))
print(f"   max |D − (rtr − sts)| over 1,000 random consistent atom vectors: {worst:.1e}")

# ------------------------------------------------------------------ (C1) independent Gaussian CCS
def local_entropies(Z, C):
    """Z (4, n) standardised & centred samples; C (4, 4) their covariance (ddof 1). Local Gaussian
    entropies for every subset, closed form: ½ log((2π)^d det C_A) + ½ z_A' C_A^{-1} z_A."""
    out = {}
    for A in _SUBSETS:
        idx = np.array(A)
        CA = C[np.ix_(idx, idx)]
        inv = np.linalg.inv(CA)
        q = np.einsum("kt,kl,lt->t", Z[idx], inv, Z[idx])
        out[A] = 0.5 * len(A) * np.log(2 * np.pi) + 0.5 * np.log(np.linalg.det(CA)) + 0.5 * q
    return out


def ccs_red(mi1, mi2, mi12):
    """Ince (2017): redundancy = co-information where sign(mi1) = sign(mi2) = sign(mi12) = sign(coI), else 0."""
    coI = mi1 + mi2 - mi12
    s = np.stack([np.sign(mi1), np.sign(mi2), np.sign(mi12), np.sign(coI)], 1)
    agree = np.all(s == s[:, [0]], axis=1)
    return np.where(agree, coI, 0.0)


def independent_ccs_atoms(x, y, tau=1):
    X = np.stack([x[:-tau], y[:-tau], x[tau:], y[tau:]])
    X = X / X.std(1, ddof=1, keepdims=True)
    Z = X - X.mean(1, keepdims=True)
    C = np.cov(X)
    h = local_entropies(Z, C)
    mi = {k: h[A] + h[B] - h[tuple(sorted(A + B))] for k, (A, B) in _MI_SETS.items()}
    R = {"R_xyta": ccs_red(mi["I_xta"], mi["I_yta"], mi["I_xyta"]), "R_xytb": ccs_red(mi["I_xtb"], mi["I_ytb"], mi["I_xytb"]),
         "R_xytab": ccs_red(mi["I_xtab"], mi["I_ytab"], mi["I_xytab"]), "R_abtx": ccs_red(mi["I_xta"], mi["I_xtb"], mi["I_xtab"]),
         "R_abty": ccs_red(mi["I_yta"], mi["I_ytb"], mi["I_ytab"]), "R_abtxy": ccs_red(mi["I_xyta"], mi["I_xytb"], mi["I_xytab"])}
    n = x.size - tau
    k = np.zeros((n, 16))
    for name in KNOWNS[1:]:
        k[:, K[name]] = mi[name] if name in mi else R[name]
    D = D_of(k)
    s = np.stack([np.sign(mi["I_xta"]), np.sign(mi["I_xtb"]), np.sign(mi["I_yta"]), np.sign(mi["I_ytb"]), np.sign(D)], 1)
    agree = np.all(s == s[:, [0]], axis=1)
    k[:, 0] = np.where(agree, D, 0.0)
    atoms = k @ MINV_T
    return atoms, D, agree, mi, R


print("\n== (C1) independent Gaussian CCS vs phyid.calc_PhiID(redundancy='CCS'), 200 random real-data draws (W = 60 windows, ts_gsr)")
ts = sio.loadmat(REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat")["ts_gsr"]
worst_atoms = worst_red = worst_excl = 0.0
agree_share = []
for _ in range(200):
    s, c, w = rng.integers(14), rng.integers(2), rng.integers(14)
    X = np.asarray(ts[s, c], float)[REGIONS]
    kept = np.where(np.all(np.isfinite(X), axis=0))[0]
    in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
    i, j = rng.choice(115, 2, replace=False)
    x, y = X[i, in_w], X[j, in_w]
    ref, calc = calc_PhiID(x, y, tau=1, kind="gaussian", redundancy="CCS")
    mine, D, agree, mi, R = independent_ccs_atoms(x, y)
    worst_atoms = max(worst_atoms, max(np.abs(np.asarray(ref[n]) - mine[:, a]).max() for a, n in enumerate(ATOMS)))
    worst_red = max(worst_red, max(np.abs(np.asarray(calc["R_res"][n]) - R[n]).max() for n in R))
    worst_excl = max(worst_excl, np.abs(np.asarray(ref["sts"])[agree]).max() if agree.any() else 0.0, np.abs(np.asarray(ref["sts"])[~agree] + D[~agree]).max() if (~agree).any() else 0.0)
    agree_share.append(agree.mean())
print(f"   max |atom difference| over 200 draws × 16 atoms × all samples: {worst_atoms:.1e}")
print(f"   max |single-target CCS redundancy difference| (Ince definition vs phyid), six redundancies: {worst_red:.1e}")
print(f"   pointwise exclusivity in phyid's output (sts = 0 where signs agree, sts = −D elsewhere): max deviation {worst_excl:.1e}")
print(f"   share of samples with all five signs agreeing: mean {np.mean(agree_share):.3f}, range {np.min(agree_share):.3f}–{np.max(agree_share):.3f}")

# ------------------------------------------------------------------ (C2) hand-computable binary case
print("\n== (C2) binary hand case: tabulated joint distribution of (x_t, y_t, x_{t+1}, y_{t+1}), every local MI = log2 of a ratio of table probabilities")
# a designed sample: 64 samples over the 16 cells with chosen counts (non-uniform so all MIs are non-trivial)
counts = {(0, 0, 0, 0): 10, (0, 0, 0, 1): 3, (0, 0, 1, 0): 3, (0, 0, 1, 1): 1, (0, 1, 0, 0): 2, (0, 1, 0, 1): 6, (0, 1, 1, 0): 1, (0, 1, 1, 1): 3,
          (1, 0, 0, 0): 2, (1, 0, 0, 1): 1, (1, 0, 1, 0): 7, (1, 0, 1, 1): 2, (1, 1, 0, 0): 1, (1, 1, 0, 1): 2, (1, 1, 1, 0): 3, (1, 1, 1, 1): 9}
samples = np.array([cell for cell, n in counts.items() for _ in range(n)])         # (64, 4) rows = samples
N = samples.shape[0]
# a time series realisation whose (x[:-1], y[:-1], x[1:], y[1:]) columns equal these samples is not needed:
# phyid's discrete path takes src/trg and forms the four vectors itself, so build x, y of length N+1 whose
# four-vector rows reproduce the table is impossible in general; instead call the internal four-vector
# routine of phyid on the tabulated columns directly, exactly as calc_PhiID does after _binarize.
from phyid.calculate import _get_entropy_four_vec, _get_coinfo_four_vec, _get_redundancy_four_vec, _get_double_redundancy_four_vec, _get_atoms_four_vec
Xb = samples.T.astype(int)                                                      # (4, N) [sp, tp, sf, tf]
h_res = _get_entropy_four_vec(Xb, kind="discrete")
I_res = _get_coinfo_four_vec(h_res)
R_res = _get_redundancy_four_vec("CCS", I_res)
calc_res = {"h_res": h_res, "I_res": I_res, "R_res": R_res}
calc_res["rtr"] = _get_double_redundancy_four_vec("CCS", calc_res)
phy = _get_atoms_four_vec(calc_res)


def p_of(vals, idx):
    """empirical probability of the sub-pattern vals on variables idx"""
    m = np.all(samples[:, idx] == np.array(vals), axis=1)
    return m.mean()


def local_mi_hand(t, A, B):
    a, b, ab = samples[t, list(A)], samples[t, list(B)], samples[t, list(A) + list(B)]
    return np.log2(p_of(ab, list(A) + list(B)) / (p_of(a, list(A)) * p_of(b, list(B))))


mi_hand = {k: np.array([local_mi_hand(t, A, B) for t in range(N)]) for k, (A, B) in _MI_SETS.items()}
R_hand = {"R_xyta": ccs_red(mi_hand["I_xta"], mi_hand["I_yta"], mi_hand["I_xyta"]), "R_xytb": ccs_red(mi_hand["I_xtb"], mi_hand["I_ytb"], mi_hand["I_xytb"]),
          "R_xytab": ccs_red(mi_hand["I_xtab"], mi_hand["I_ytab"], mi_hand["I_xytab"]), "R_abtx": ccs_red(mi_hand["I_xta"], mi_hand["I_xtb"], mi_hand["I_xtab"]),
          "R_abty": ccs_red(mi_hand["I_yta"], mi_hand["I_ytb"], mi_hand["I_ytab"]), "R_abtxy": ccs_red(mi_hand["I_xyta"], mi_hand["I_xytb"], mi_hand["I_xytab"])}
k = np.zeros((N, 16))
for name in KNOWNS[1:]:
    k[:, K[name]] = mi_hand[name] if name in mi_hand else R_hand[name]
D = D_of(k)
sg = np.stack([np.sign(mi_hand["I_xta"]), np.sign(mi_hand["I_xtb"]), np.sign(mi_hand["I_yta"]), np.sign(mi_hand["I_ytb"]), np.sign(D)], 1)
agree = np.all(sg == sg[:, [0]], axis=1)
k[:, 0] = np.where(agree, D, 0.0)
hand = k @ MINV_T
dmi = max(np.abs(np.asarray(I_res[n]) - mi_hand[n]).max() for n in mi_hand)
dR = max(np.abs(np.asarray(R_res[n]) - R_hand[n]).max() for n in R_hand)
drtr = np.abs(np.asarray(calc_res["rtr"]) - k[:, 0]).max()
datoms = max(np.abs(np.asarray(phy[n]) - hand[:, a]).max() for a, n in enumerate(ATOMS))
print(f"   {N} samples over 16 cells; local MIs (bits) from the table vs phyid: max |diff| {dmi:.1e}; six CCS redundancies: {dR:.1e}; double redundancy: {drtr:.1e}; all 16 atoms: {datoms:.1e}")
print(f"   sign-agreeing samples: {int(agree.sum())}/{N}; mean atoms (bits): rtr {hand[:, 0].mean():+.4f}, sts {hand[:, 15].mean():+.4f}, xtx {hand[:, 5].mean():+.4f}, yty {hand[:, 10].mean():+.4f}; mean D {D.mean():+.4f}")
print(f"   hand check of the exclusivity: max |sts| at agreeing samples {np.abs(hand[agree, 15]).max():.1e}; max |sts + D| elsewhere {np.abs(hand[~agree, 15] + D[~agree]).max():.1e}")
# one sample fully by hand, printed
t = 0
print(f"   sample 0 = {tuple(samples[0])}: p(x_t,x_t+1) = {p_of(samples[0, [0, 2]], [0, 2]):.4f}, p(x_t) = {p_of(samples[0, [0]], [0]):.4f}, p(x_t+1) = {p_of(samples[0, [2]], [2]):.4f} → i(x_t; x_t+1) = {mi_hand['I_xta'][0]:+.4f} bits (phyid {float(np.asarray(I_res['I_xta'])[0]):+.4f})")
