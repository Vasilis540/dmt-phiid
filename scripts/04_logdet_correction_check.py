"""
04_logdet_correction_check.py — decision-tree step 2 (CLAUDE.md, Primary B).

The analytic bias correction for the Gaussian plug-in log-det entropy replaces
each log det S_k (k = 1..4 dims, N four-vector samples) by
    log det S_k - sum_{i=1..k} [psi((N-i)/2) - ln((N-1)/2)],
the unbiased log-det estimator under iid Gaussian sampling. Because the
correction depends only on (k, N), every MI shifts by a constant that depends
only on the dimensions of its two argument sets, every MMI candidate set
compares MIs of identical dimensions (so no min-selection can change), and
each window-mean atom therefore shifts by a fixed constant per (atom, N)
obtainable by pushing the MI constants through phyid's lattice inverse.

This script
  (a) computes that constant for all 16 atoms at N = W - tau for W = 30, 60,
      840 and checks the recorded prediction for sts,
      -0.5 [psi((N-3)/2) - psi((N-4)/2)];
  (b) applies it post hoc to the 2,000-run bias tables committed at 18ad8b4
      (the working-tree tables are being overwritten by the 20,000-run job),
      re-reporting per-condition bias and differential bias with and without
      the correction and evaluating criterion clauses 1 and 2 at W = 30;
  (c) validates the derivation empirically: the correction is applied INSIDE
      the estimator (to the entropy terms, before MI, MMI selection and the
      lattice solve) on freshly simulated VAR(1) windows, and the per-window
      difference from the plug-in atoms is compared with the analytic
      constant, with selections checked window by window.

Touches no real data. Reads the committed tables via `git show`.
"""

import csv
import importlib.util
import inspect
import io
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.special import digamma

from phyid.calculate import (_get_atoms_four_vec, _get_coinfo_four_vec,
                             _get_double_redundancy_four_vec,
                             _get_redundancy_four_vec, calc_PhiID)
from phyid.utils import PhiID_atoms_abbr as ATOMS

SEED = 20261120
TABLES_COMMIT = "18ad8b4"
N_WINDOWS_EMPIRICAL = 500
EMPIRICAL_CONDITIONS = ("baseline", "asym_baseline", "asym_shift_coupling")
RESULTS = Path("results")
OUT_CSV = RESULTS / "logdet_correction_check.csv"

_argv = sys.argv
sys.argv = [_argv[0]]
spec = importlib.util.spec_from_file_location("bc", "scripts/02_bias_check.py")
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)
sys.argv = _argv
CONDS = next(v for v in vars(bc).values() if isinstance(v, dict) and "asym_baseline" in v)

KNOWNS = ["rtr", "R_xyta", "R_xytb", "R_xytab", "R_abtx", "R_abty", "R_abtxy",
          "I_xta", "I_xtb", "I_yta", "I_ytb", "I_xyta", "I_xytb", "I_xtab", "I_ytab", "I_xytab"]
DIMS = {"rtr": (1, 1), "R_xyta": (1, 1), "R_xytb": (1, 1), "R_xytab": (1, 2), "R_abtx": (1, 1),
        "R_abty": (1, 1), "R_abtxy": (2, 1), "I_xta": (1, 1), "I_xtb": (1, 1), "I_yta": (1, 1),
        "I_ytb": (1, 1), "I_xyta": (2, 1), "I_xytb": (2, 1), "I_xtab": (1, 2), "I_ytab": (1, 2),
        "I_xytab": (2, 2)}
CANDIDATE_SETS = [("I_xta", "I_yta"), ("I_xtb", "I_ytb"), ("I_xtab", "I_ytab"),
                  ("I_xta", "I_xtb"), ("I_yta", "I_ytb"), ("I_xyta", "I_xytb"),
                  ("I_xta", "I_xtb", "I_yta", "I_ytb")]

# phyid's lattice matrix, read from its own source so it cannot drift
_src = inspect.getsource(_get_atoms_four_vec)
_s = _src.index("knowns_to_atoms_mat = [")
_e = _src.index("]\n\n", _s) + 1
LATTICE = np.array(eval(_src[_s:_e].split("=", 1)[1]))


def c_k(N, k):
    return sum(digamma((N - i) / 2) - np.log((N - 1) / 2) for i in range(1, k + 1))


def delta_mi(N, ka, kb):
    return -0.5 * (c_k(N, ka) + c_k(N, kb) - c_k(N, ka + kb))


def atom_delta(N):
    d = np.array([delta_mi(N, *DIMS[k]) for k in KNOWNS])
    return dict(zip(ATOMS, np.linalg.solve(LATTICE, d)))


def git_table(name):
    txt = subprocess.check_output(["git", "show", f"{TABLES_COMMIT}:results/{name}"], text=True)
    return list(csv.DictReader(l for l in io.StringIO(txt) if not l.startswith("#")))


def corrected_atoms(x, y, N):
    """(plug-in atoms, corrected atoms, selections identical?) for one window."""
    atoms, calc = calc_PhiID(x, y, tau=bc.TAU, kind=bc.KIND, redundancy=bc.REDUNDANCY)
    h = {k: v - 0.5 * c_k(N, len(bc._ENTROPY_SETS[k])) for k, v in calc["h_res"].items()}
    I = _get_coinfo_four_vec(h)
    R = _get_redundancy_four_vec("MMI", I)
    c2 = {"h_res": h, "I_res": I, "R_res": R}
    c2["rtr"] = _get_double_redundancy_four_vec("MMI", c2)
    sel0 = [bc._argmin_mean(calc["I_res"], list(s)) for s in CANDIDATE_SETS]
    sel1 = [bc._argmin_mean(I, list(s)) for s in CANDIDATE_SETS]
    return atoms, _get_atoms_four_vec(c2), sel0 == sel1


def main():
    try:
        sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
        if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "CLAUDE.md"],
                                   text=True).strip():
            sha += "-dirty"
    except Exception:
        sha = "nogit"
    out = []

    # (a) constants
    print("(a) analytic correction per window-mean atom, nats, ADDED to the plug-in estimate")
    for a, b in CANDIDATE_SETS[:6]:
        assert sorted(DIMS[a]) == sorted(DIMS[b]), (a, b)
    assert len({DIMS[k] for k in CANDIDATE_SETS[6]}) == 1
    print("    every MMI candidate set compares MIs of identical dimensions -> no selection can change")
    deltas = {}
    for W in (30, 60, 840):
        N = W - bc.TAU
        deltas[W] = atom_delta(N)
        pred = -0.5 * (digamma((N - 3) / 2) - digamma((N - 4) / 2))
        assert abs(deltas[W]["sts"] - pred) < 1e-12, (deltas[W]["sts"], pred)
        nonzero = {k: v for k, v in deltas[W].items() if abs(v) > 1e-12}
        print(f"    W={W:3d} N={N:3d}: " + "  ".join(f"{k}={v:+.5f}" for k, v in nonzero.items())
              + f"   (sts prediction -0.5[psi((N-3)/2)-psi((N-4)/2)] = {pred:+.5f}: matches)")
        for k, v in deltas[W].items():
            out.append(dict(section="constant", condition="", window=W, atom=k, value=v))

    # (b) post hoc on the committed tables
    print(f"\n(b) per-condition bias, plug-in vs corrected, from {TABLES_COMMIT} tables")
    clause1 = {}
    for r in git_table("bias_check.csv"):
        W, atom = int(r["window"]), r["atom"]
        an, b = float(r["analytic"]), float(r["bias"])
        bcorr = b + deltas[W][atom]
        print(f"    {r['condition']:22s} W={W:3d} {atom}: analytic {an:+.4f}  bias {b:+.4f} -> {bcorr:+.4f}"
              f"  (|corrected| = {abs(bcorr) / abs(an) * 100:5.1f} % of analytic)")
        out.append(dict(section="bias", condition=r["condition"], window=W, atom=atom,
                        analytic=an, bias_plugin=b, bias_corrected=bcorr,
                        corrected_over_analytic=abs(bcorr) / abs(an)))
        if atom == "sts" and W == 30:
            clause1[r["condition"]] = abs(bcorr) / abs(an)
    print("\n    differential bias, plug-in vs corrected")
    clause2 = {}
    max_change = 0.0
    for r in git_table("bias_check_differential.csv"):
        W, atom = int(r["window"]), r["atom"]
        tb, db = float(r["true_diff"]), float(r["diff_bias"])
        est = float(r["est_diff"])
        db_corr = (est + deltas[W][atom]) - (0.0 + deltas[W][atom]) - tb  # same constant, both arms
        change = db_corr - db                      # differs from 0 only by the table's 6-dp rounding
        max_change = max(max_change, abs(change))
        print(f"    {r['shift']:22s} W={W:3d} {atom}: true {tb:+.4f}  diff bias {db:+.4f} -> {db_corr:+.4f}"
              f"  change {change:+.1e}  ({abs(db_corr) / abs(tb) * 100:5.1f} % of true)")
        out.append(dict(section="differential", condition=r["shift"], window=W, atom=atom,
                        true_diff=tb, diff_bias_plugin=db, diff_bias_corrected=db_corr,
                        change=change, corrected_over_true=abs(db_corr) / abs(tb)))
        if atom == "sts" and W == 30:
            clause2[r["shift"]] = abs(db_corr) / abs(tb)
    c1 = all(v < 0.10 for v in clause1.values())
    c2 = all(v < 0.15 for v in clause2.values())
    print(f"\n    max |change in differential bias| across all rows: {max_change:.1e} "
          "(zero up to the tables' 6-decimal rounding)")
    print("    criterion, sts, W=30 -- clause 1 |bias| < 10 % of analytic: "
          + ", ".join(f"{k} {v * 100:.0f} %" for k, v in clause1.items()) + f" -> {'PASS' if c1 else 'FAIL'}")
    print("    criterion, sts, W=30 -- clause 2 |diff bias| < 15 % of true: "
          + ", ".join(f"{k} {v * 100:.0f} %" for k, v in clause2.items()) + f" -> {'PASS' if c2 else 'FAIL'}")
    branch = "W=30 corrected" if (c1 and c2) else "W=60 uncorrected (fallback)"
    print(f"    branch: Primary B = {branch}")

    # (c) empirical validation inside the estimator
    print(f"\n(c) empirical: correction applied inside the estimator, {N_WINDOWS_EMPIRICAL} simulated windows per cell")
    rng = np.random.default_rng(SEED)
    for cname in EMPIRICAL_CONDITIONS:
        A, Q = bc.var1_matrices(**CONDS[cname])
        for W in (30, 60):
            N = W - bc.TAU
            z = bc.simulate(A, Q, W, N_WINDOWS_EMPIRICAL, rng)
            worst, n_sel = 0.0, 0
            for n in range(N_WINDOWS_EMPIRICAL):
                a0, a1, same = corrected_atoms(z[n, 0], z[n, 1], N)
                n_sel += (not same)
                worst = max(worst, max(abs((np.mean(a1[k]) - np.mean(a0[k])) - deltas[W][k]) for k in ATOMS))
            print(f"    {cname:20s} W={W}: selections changed in {n_sel} windows; "
                  f"max |(corrected - plugin) - constant| over 16 atoms = {worst:.1e}")
            out.append(dict(section="empirical", condition=cname, window=W, atom="all",
                            n_windows=N_WINDOWS_EMPIRICAL, selections_changed=n_sel, max_abs_dev=worst))

    keys = sorted({k for r in out for k in r})
    with open(OUT_CSV, "w") as fh:
        fh.write(f"# script=04_logdet_correction_check.py tables_commit={TABLES_COMMIT} "
                 f"n_windows_empirical={N_WINDOWS_EMPIRICAL} seed={SEED} branch={branch!r} git={sha}\n")
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(out)
    print(f"\nwrote {OUT_CSV}")


if __name__ == "__main__":
    main()
