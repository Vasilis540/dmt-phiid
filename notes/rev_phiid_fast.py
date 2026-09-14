"""
rev_phiid_fast.py — closed-form, batched Gaussian-MMI ΦID for every region pair at once.

What phyid.calc_PhiID(kind="gaussian", redundancy="MMI", tau) does per pair: it standardises
the four vectors [x_past, y_past, x_future, y_future] (std, ddof = 1), fits one Gaussian
(np.cov, ddof = 1 → the 4 × 4 Pearson correlation matrix C), evaluates LOCAL entropies per
sample under that Gaussian, forms the nine local mutual informations, picks each MMI
redundancy as the candidate local MI with the smaller MEAN (double redundancy rtr = the
smallest-mean of the four single MIs), and solves the fixed 16 × 16 lattice system per sample.

Two identities make this a closed form of C:
  * the time-mean over the fitting sample of a local Gaussian MI i(A;B) equals the plug-in
    MI ½ log(det C_A det C_B / det C_AB): the quadratic terms average to ½ dim (n−1)/n and
    cancel because dim(AB) = dim(A) + dim(B);
  * the lattice solve is linear, so the time-mean of the atoms is the solve of the
    time-mean knowns.
Hence the window means that scripts/01_synergy_timecourse.py (--fit-mode window) stores are
closed-form functions of each window's C, and the 30-TR bin means of the global fit
(--fit-mode global, and scripts/11_regional_analysis.py) are obtained from the same C plus
the bin's second-moment matrices S^bin in the fit's standardised coordinates:
    mean_bin i(A;B) = plug-in MI + ½ [tr(C_A⁻¹ S_A) + tr(C_B⁻¹ S_B) − tr(C_AB⁻¹ S_AB)].
All pairs share three region-level matrices (past–past, future–future, past–future), so a
whole run of 6,555 pairs is a few matrix products. rev_phiid_fast_validate.py checks the
result against the saved phyid outputs to ~1e-12 before anything downstream uses it.
"""
from itertools import combinations

import numpy as np

ATOMS = ("rtr", "rtx", "rty", "rts", "xtr", "xtx", "xty", "xts",
         "ytr", "ytx", "yty", "yts", "str", "stx", "sty", "sts")          # phyid order
KNOWNS = ("rtr", "R_xyta", "R_xytb", "R_xytab", "R_abtx", "R_abty", "R_abtxy",
          "I_xta", "I_xtb", "I_yta", "I_ytb", "I_xyta", "I_xytb", "I_xtab", "I_ytab", "I_xytab")
_M = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # rtr
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Rxyta
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Rxytb
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Rxytab
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Rabtx
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Rabty
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # Rabtxy
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ixta
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ixtb
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # Iyta
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Iytb
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],  # Ixyta
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # Ixytb
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Ixtab
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],  # Iytab
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Ixytab
], float)
_MINV_T = np.linalg.inv(_M).T                      # atoms = knowns @ _MINV_T
# variable order inside the 4-vector: sp = 0 (x past), tp = 1 (y past), sf = 2 (x future), tf = 3 (y future)
_MI_SETS = {                                       # (A, B) for each of the nine MIs
    "I_xta": ((0,), (2,)), "I_xtb": ((0,), (3,)), "I_yta": ((1,), (2,)), "I_ytb": ((1,), (3,)),
    "I_xyta": ((0, 1), (2,)), "I_xytb": ((0, 1), (3,)), "I_xtab": ((0,), (2, 3)), "I_ytab": ((1,), (2, 3)),
    "I_xytab": ((0, 1), (2, 3)),
}
_SUBSETS = sorted({A for A, B in _MI_SETS.values()} | {B for A, B in _MI_SETS.values()} |
                  {tuple(sorted(A + B)) for A, B in _MI_SETS.values()}, key=lambda t: (len(t), t))


def standardised_lag_pair(X, tau=1):
    """X (R, T) finite → (P, F): past and future segments, each row centred and scaled by its
    own ddof-1 std (phyid's standardisation followed by np.cov's centring)."""
    P = X[:, :-tau].astype(float)
    F = X[:, tau:].astype(float)
    P = (P - P.mean(1, keepdims=True)) / P.std(1, ddof=1, keepdims=True)
    F = (F - F.mean(1, keepdims=True)) / F.std(1, ddof=1, keepdims=True)
    return P, F


def _blocks(P, F, weight):
    return P @ P.T * weight, F @ F.T * weight, P @ F.T * weight      # (pp, ff, pf); pf[i, j] = <p_i, f_j>


def _pair_mats(pp, ff, pf, I, J):
    """(n_pairs, 4, 4) matrices in the order [sp, tp, sf, tf] for pairs (I[k], J[k])."""
    n = I.size
    M = np.empty((n, 4, 4))
    M[:, 0, 0] = pp[I, I]; M[:, 0, 1] = pp[I, J]; M[:, 0, 2] = pf[I, I]; M[:, 0, 3] = pf[I, J]
    M[:, 1, 0] = pp[J, I]; M[:, 1, 1] = pp[J, J]; M[:, 1, 2] = pf[J, I]; M[:, 1, 3] = pf[J, J]
    M[:, 2, 0] = pf[I, I]; M[:, 2, 1] = pf[J, I]; M[:, 2, 2] = ff[I, I]; M[:, 2, 3] = ff[I, J]
    M[:, 3, 0] = pf[I, J]; M[:, 3, 1] = pf[J, J]; M[:, 3, 2] = ff[J, I]; M[:, 3, 3] = ff[J, J]
    return M


def _logdets(C):
    """log det of every subset block of the (n, 4, 4) matrices C → dict subset → (n,)."""
    out = {}
    for A in _SUBSETS:
        idx = np.array(A)
        sub = C[:, idx[:, None], idx[None, :]]
        if len(A) == 1:
            out[A] = np.log(sub[:, 0, 0])
        else:
            sign, ld = np.linalg.slogdet(sub)
            out[A] = ld
    return out


def _plugin_mis(C):
    ld = _logdets(C)
    return {k: 0.5 * (ld[A] + ld[B] - ld[tuple(sorted(A + B))]) for k, (A, B) in _MI_SETS.items()}


def _mmi_choice(mi):
    """Return the selection of each MMI redundancy as (name of the chosen MI candidate per pair).
    phyid: redundancy_mmi(mi_1, mi_2, .) = mi_1 if mean(mi_1) < mean(mi_2) else mi_2;
           double_redundacy_mmi([xta, xtb, yta, ytb]) = the candidate with the smallest mean
           (first minimum)."""
    def pick(a, b):
        return np.where(mi[a] < mi[b], 0, 1)          # 0 → a, 1 → b (ties → b, as in phyid)
    sel = {
        "R_xyta": (("I_xta", "I_yta"), pick("I_xta", "I_yta")),
        "R_xytb": (("I_xtb", "I_ytb"), pick("I_xtb", "I_ytb")),
        "R_xytab": (("I_xtab", "I_ytab"), pick("I_xtab", "I_ytab")),
        "R_abtx": (("I_xta", "I_xtb"), pick("I_xta", "I_xtb")),
        "R_abty": (("I_yta", "I_ytb"), pick("I_yta", "I_ytb")),
        "R_abtxy": (("I_xyta", "I_xytb"), pick("I_xyta", "I_xytb")),
    }
    four = ("I_xta", "I_xtb", "I_yta", "I_ytb")
    stack = np.stack([mi[k] for k in four], 1)
    sel["rtr"] = (four, np.argmin(stack, axis=1))          # first minimum, as np.argmin in phyid
    return sel


def _assemble(mi_values, sel):
    """knowns (n, 16) from a dict of MI values (n,) and the MMI selections."""
    n = next(iter(mi_values.values())).size
    K = np.empty((n, 16))
    for c, name in enumerate(KNOWNS):
        if name in mi_values:
            K[:, c] = mi_values[name]
        else:
            cands, which = sel[name]
            stack = np.stack([mi_values[k] for k in cands], 1)
            K[:, c] = stack[np.arange(n), which]
    return K


class PairPhiID:
    """Batched ΦID for all pairs of the rows of X over a fitting sample."""

    def __init__(self, X, tau=1, pairs=None):
        R = X.shape[0]
        self.R = R
        self.tau = tau
        self.pairs = pairs if pairs is not None else list(combinations(range(R), 2))
        self.I = np.array([i for i, j in self.pairs])
        self.J = np.array([j for i, j in self.pairs])
        self.P, self.F = standardised_lag_pair(X, tau)
        self.n = self.P.shape[1]
        pp, ff, pf = _blocks(self.P, self.F, 1.0 / (self.n - 1))
        self.C = _pair_mats(pp, ff, pf, self.I, self.J)                   # correlation matrices
        self.mi = _plugin_mis(self.C)
        self.sel = _mmi_choice(self.mi)

    def atoms_mean(self):
        """(n_pairs, 16) time-mean atoms over the fitting sample (= phyid's window means)."""
        return _assemble(self.mi, self.sel) @ _MINV_T

    def atoms_bins(self, slot, n_slots):
        """(n_slots, n_pairs, 16) means of phyid's LOCAL atoms over the samples of each slot
        (slot: (n,) integer label per sample, −1 = ignore), evaluated under the fit on all samples."""
        inv = {A: np.linalg.inv(self.C[:, np.array(A)[:, None], np.array(A)[None, :]]) for A in _SUBSETS}
        out = np.full((n_slots, len(self.pairs), 16), np.nan)
        for t in range(n_slots):
            m = slot == t
            if not m.any():
                continue
            pp, ff, pf = _blocks(self.P[:, m], self.F[:, m], 1.0 / m.sum())
            S = _pair_mats(pp, ff, pf, self.I, self.J)                 # bin second moments
            q = {A: np.einsum("nij,nij->n", inv[A], S[:, np.array(A)[:, None], np.array(A)[None, :]]) for A in _SUBSETS}
            mi_bin = {k: self.mi[k] + 0.5 * (q[A] + q[B] - q[tuple(sorted(A + B))]) for k, (A, B) in _MI_SETS.items()}
            out[t] = _assemble(mi_bin, self.sel) @ _MINV_T
        return out


    def _local_mis(self, sel_pairs):
        """local MIs (dict of (n_sel, n) arrays) for the selected pair indices, under the fit on all samples."""
        I, J = self.I[sel_pairs], self.J[sel_pairs]
        n = self.n
        Z = np.empty((sel_pairs.size, 4, n))
        Z[:, 0] = self.P[I]; Z[:, 1] = self.P[J]; Z[:, 2] = self.F[I]; Z[:, 3] = self.F[J]
        C = self.C[sel_pairs]
        q = {}
        for A in _SUBSETS:
            idx = np.array(A)
            inv = np.linalg.inv(C[:, idx[:, None], idx[None, :]])
            q[A] = np.einsum("nkl,nkt,nlt->nt", inv, Z[:, idx], Z[:, idx])
        mi = {k: self.mi[k][sel_pairs][:, None] + 0.5 * (q[A] + q[B] - q[tuple(sorted(A + B))]) for k, (A, B) in _MI_SETS.items()}
        return mi

    def atoms_ccs(self, slot=None, n_slots=None, chunk=800):
        """CCS atoms (phyid's definitions, verified in partB2_ccs_verify.py) from the local MIs.
        Returns (atoms_mean (n_pairs, 16) over all samples, atoms_slot (n_slots, n_pairs, 16) or None,
        local_pairmean (n, 16), agree_share (n_pairs,))."""
        n_pairs, n = len(self.pairs), self.n
        atoms_mean = np.empty((n_pairs, 16))
        atoms_slot = None if slot is None else np.full((n_slots, n_pairs, 16), np.nan)
        local_sum = np.zeros((n, 16))
        agree_share = np.empty(n_pairs)
        for start in range(0, n_pairs, chunk):
            sel = np.arange(start, min(start + chunk, n_pairs))
            K, D, agree = ccs_local_knowns(self._local_mis(sel))          # (n_sel, n, 16)
            A = K @ _MINV_T
            atoms_mean[sel] = A.mean(1)
            local_sum += A.sum(0)
            agree_share[sel] = agree.mean(1)
            if slot is not None:
                for t in range(n_slots):
                    m = slot == t
                    if m.any():
                        atoms_slot[t, sel] = A[:, m].mean(1)
        return atoms_mean, atoms_slot, local_sum / n_pairs, agree_share

    def atoms_local_pairmean(self, chunk=800):
        """(n_samples, 16) mean over pairs of phyid's LOCAL atoms at every sample of the fit
        (what 01 stores per TR in atoms_*_local_*.npy); the time-mean of this equals atoms_mean().mean(0).
        Pairs are processed in chunks to bound memory."""
        n_pairs, n = len(self.pairs), self.n
        acc = np.zeros((n, 16))
        for start in range(0, n_pairs, chunk):
            sel = np.arange(start, min(start + chunk, n_pairs))
            mi_loc = self._local_mis(sel)
            K = np.empty((sel.size, n, 16))
            for c, name in enumerate(KNOWNS):
                if name in mi_loc:
                    K[:, :, c] = mi_loc[name]
                else:
                    cands, which = self.sel[name]
                    stack = np.stack([mi_loc[k] for k in cands], 0)         # (n_cands, n_sel, n)
                    K[:, :, c] = stack[which[sel], np.arange(sel.size)]
            acc += K.sum(0)
        return (acc / n_pairs) @ _MINV_T

def _ccs_red(mi1, mi2, mi12):
    """Ince (2017) CCS redundancy, pointwise: co-information where sign(mi1) = sign(mi2) = sign(mi12) = sign(coI), else 0."""
    coI = mi1 + mi2 - mi12
    agree = (np.sign(mi1) == np.sign(mi2)) & (np.sign(mi1) == np.sign(mi12)) & (np.sign(mi1) == np.sign(coI))
    return np.where(agree, coI, 0.0)


def ccs_local_knowns(mi_loc):
    """CCS knowns (..., 16) from local MIs (dict of (...,) arrays), phyid's definitions: six single-target
    CCS redundancies (Ince 2017) and the double redundancy = double co-information D where the signs of
    I_xta, I_xtb, I_yta, I_ytb and D agree, else 0 (D ≡ rtr − sts on the lattice)."""
    R = {"R_xyta": _ccs_red(mi_loc["I_xta"], mi_loc["I_yta"], mi_loc["I_xyta"]), "R_xytb": _ccs_red(mi_loc["I_xtb"], mi_loc["I_ytb"], mi_loc["I_xytb"]),
         "R_xytab": _ccs_red(mi_loc["I_xtab"], mi_loc["I_ytab"], mi_loc["I_xytab"]), "R_abtx": _ccs_red(mi_loc["I_xta"], mi_loc["I_xtb"], mi_loc["I_xtab"]),
         "R_abty": _ccs_red(mi_loc["I_yta"], mi_loc["I_ytb"], mi_loc["I_ytab"]), "R_abtxy": _ccs_red(mi_loc["I_xyta"], mi_loc["I_xytb"], mi_loc["I_xytab"])}
    D = (-mi_loc["I_xta"] - mi_loc["I_xtb"] - mi_loc["I_yta"] - mi_loc["I_ytb"] + mi_loc["I_xtab"] + mi_loc["I_ytab"] + mi_loc["I_xyta"] + mi_loc["I_xytb"] - mi_loc["I_xytab"]
         + R["R_xyta"] + R["R_xytb"] - R["R_xytab"] + R["R_abtx"] + R["R_abty"] - R["R_abtxy"])
    s0 = np.sign(mi_loc["I_xta"])
    agree = (s0 == np.sign(mi_loc["I_xtb"])) & (s0 == np.sign(mi_loc["I_yta"])) & (s0 == np.sign(mi_loc["I_ytb"])) & (s0 == np.sign(D))
    K = np.empty(mi_loc["I_xta"].shape + (16,))
    K[..., 0] = np.where(agree, D, 0.0)
    for c, name in enumerate(KNOWNS[1:], start=1):
        K[..., c] = mi_loc[name] if name in mi_loc else R[name]
    return K, D, agree


def atoms_from_corr(C):
    """(n, 16) Gaussian-MMI atoms (phyid definitions) from (n, 4, 4) correlation matrices of
    [x_t, y_t, x_{t+τ}, y_{t+τ}] — the analytic atoms of a Gaussian process with that lag
    covariance, or the plug-in (time-mean) atoms of a sample with that correlation matrix."""
    C = np.asarray(C, float)
    if C.ndim == 2:
        C = C[None]
    mi = _plugin_mis(C)
    return _assemble(mi, _mmi_choice(mi)) @ _MINV_T


def ar1_corr(a_x, a_y, q):
    """(n, 4, 4) lag-τ correlation matrices of the diagonal VAR(1) pair with lag-τ autocorrelations
    a_x, a_y and lag-0 cross-correlation q: [[1, q, a_x, a_y q], [q, 1, a_x q, a_y],
    [a_x, a_x q, 1, q], [a_y q, a_y, q, 1]] (the family F3 of the review's item 5 when a_x = a_y)."""
    a_x, a_y, q = np.broadcast_arrays(np.asarray(a_x, float), np.asarray(a_y, float), np.asarray(q, float))
    n = a_x.size
    a_x, a_y, q = a_x.ravel(), a_y.ravel(), q.ravel()
    C = np.empty((n, 4, 4))
    C[:, 0, 0] = 1; C[:, 0, 1] = q; C[:, 0, 2] = a_x; C[:, 0, 3] = a_y * q
    C[:, 1, 0] = q; C[:, 1, 1] = 1; C[:, 1, 2] = a_x * q; C[:, 1, 3] = a_y
    C[:, 2, 0] = a_x; C[:, 2, 1] = a_x * q; C[:, 2, 2] = 1; C[:, 2, 3] = q
    C[:, 3, 0] = a_y * q; C[:, 3, 1] = a_y; C[:, 3, 2] = q; C[:, 3, 3] = 1
    return C


def incidence(R, pairs):
    """(R, n_pairs) 0/1 matrix: region r ↔ pairs containing r (row sums R−1)."""
    inc = np.zeros((R, len(pairs)))
    for k, (i, j) in enumerate(pairs):
        inc[i, k] = 1.0
        inc[j, k] = 1.0
    return inc


def phir(atoms):
    """ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr from atoms (..., 16) in phyid order."""
    a = {n: atoms[..., k] for k, n in enumerate(ATOMS)}
    ixx = a["rtr"] + a["rtx"] + a["xtr"] + a["xtx"]
    iyy = a["rtr"] + a["rty"] + a["ytr"] + a["yty"]
    return atoms.sum(-1) - ixx - iyy + a["rtr"]
