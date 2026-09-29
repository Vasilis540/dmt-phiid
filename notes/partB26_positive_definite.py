"""
partB26_positive_definite.py — B26: the matrices that are not positive definite, corrected and counted. Pre-run entry:
manuscript/analysis_record.md, "The matrices that are not positive definite (B26): pre-run entry". It reads the data
(through the steps it runs).

Until B26, rev_phiid_fast._logdets took the logarithm of |det| of every block of a matrix (np.linalg.slogdet, its sign
discarded), so a matrix that is not positive definite, the lag covariance of no process, still yielded sixteen numbers.
The AR(1)-substituted matrix of a pair, ar1_corr(a_x, a_y, q), is positive definite if and only if |q| < 1 and
(1 − a_x²)(1 − a_y²) > q²(1 − a_x a_y)², which a pair's measured a_x, a_y and q need not satisfy, and the matrices with
measured cross-lag deviations added (partB15, partB22, partB23, partB24) need not be either. In the commit of B26's
pre-run entry rev_phiid_fast.atoms_from_corr returns NaN for such a matrix, and every computation that averages its
atoms takes its means over the matrices where they exist. This script runs section 6 of run_all.sh with that code, in
place, and counts the matrices that are not positive definite.

How. The steps are those of section 6 of run_all.sh, read from run_all.sh at run time, in its order and with its
arguments, except B25 (partB25_binarised.py: no data, no atoms from rev_phiid_fast, its outputs tied to its own
pre-run entry); the HRF-deconvolution steps only if their sandbox is present, as in run_all.sh. Each step's output is
written where run_all.sh writes it (nstep: notes/review_results/<log>.log; step: results/run_<log>.log; nrun: the
script's own logs), so the regenerated files are those of a run of section 6. Each step runs in this file's --child
mode, which imports rev_phiid_fast, wraps two of its functions and then runs the step's script as __main__ (runpy):
_logdets(C), through which every atom rev_phiid_fast computes passes (PairPhiID and atoms_from_corr), and
atoms_from_corr(C). The wrappers return exactly what the functions return. They record, per site — the calling line
(the first frame outside rev_phiid_fast.py and outside the wrappers), its column (two calls on one line are two sites),
the chain of up to two frames of the repository, outside .venv, that led to it (so that, for instance, the evaluations
inside a root search and the final evaluation of the same function are told apart) and the path (PairPhiID,
atoms_from_corr, other) —: the calls; the matrices; those with a non-finite entry; those whose smallest eigenvalue
(np.linalg.eigvalsh) is ≤ 0, "not positive definite"; among these, those with a block determinant ≤ 0; the smallest
eigenvalue; the matrices with a smallest eigenvalue in (0, 10⁻³], "near-singular"; the number of the site's calls that
held matrices that are not positive definite or not finite, and the ordinal of each such call with its number of them,
from which a step's own loop order gives the window of each; and, for the matrices that are not positive definite and
pass through atoms_from_corr, the sts that the code before B26 gave them, recomputed from the unsigned log-determinants
(count, sum, smallest, largest, and the first 20 with their a_x = C[0, 2], a_y = C[1, 3], q = ½(C[0, 1] + C[2, 3]) and
cross-lag entries C[0, 3], C[1, 2]). A matrix counted on the atoms_from_corr path has no atoms (NaN) and is left out of
whatever that site's result feeds; one counted on the other paths (PairPhiID, other) is not corrected (none is expected:
a sample correlation matrix of more than four points is positive definite unless its series are collinear) and is
reported. The same data window, or the same whole run, may be evaluated by several steps (partB4,
partB4_residual_source, partB10, partB14, partB15, partB19, partB22), so the counts of different steps are not to be
added. A step that fails is reported (its exit status, and its own message or traceback in its log) and the others go
on. The CSV and the tables are written before the first step and after every step, each write replacing the file whole,
so that a run that is interrupted (a power loss, a stopped unit) leaves the counts of the steps it finished; the CSV's
first line then ends "; partial: k of n steps".
--from STEP re-runs the named step and every later step of the section (their names as the tables give them) under the
same wrappers, at the commit of the full run, on the tree that run left (complete or interrupted), and replaces their
rows in positive_definite.csv, from which the tables are made again: the rule of the pre-run entry for a step that did
not run to its end, since the later steps read the outputs of the earlier ones. Every step before STEP must have run to
its end (its row in the CSV, exit status 0); the CSV's first line keeps the run's, with "; interrupted after k of n
steps" where it was partial, and adds the re-run. --check-from STEP makes the checks of --from and runs nothing.
--steps prints the names of the steps, in order (the names --from takes), and does nothing else.
--selftest checks the wrappers and the child mode without git, data or the steps: on positive-definite matrices and on
two that are not (the AR(1) matrix of a pair sharing a slow signal under unequal noise) they return what the functions
return, bit for bit, count what they should, recover the values the code before B26 gave the two, tell apart two calls
on one line, record the call that held the matrix that is not positive definite, and a step's own exit message and
status pass through the child.

Outputs: the files that section 6 writes; notes/review_results/partB/positive_definite.csv (a first line with the
commit, the time of the run, the versions of Python and NumPy and any re-run; then one row per step, with its exit status
and duration, and one per step and site, with the calls that held the matrices and the examples as JSON) and
positive_definite_tables.md (its header carries that first line and the sha256 of the CSV), which is made from the CSV
alone; positive_definite_run.log via tee.
Run from the repository root, with the data clone in place, at the commit of the pre-run entry or a later one that
changes none of the steps' scripts, the tree clean (about three hours, an estimate from section 6 of the final run of
run_all.sh, 2 h 40 min, and the wrappers' eigenvalues):
  .venv/bin/python -u notes/partB26_positive_definite.py 2>&1 | tee notes/review_results/partB/positive_definite_run.log
and, only if a step did not run to its end and its cause is outside the code (the rule of the pre-run entry):
  .venv/bin/python -u notes/partB26_positive_definite.py --from <step> 2>&1 | tee -a notes/review_results/partB/positive_definite_run.log
"""
import csv
import hashlib
import io
import json
import os
import platform
import re
import runpy
import shlex
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
NEAR = 1e-3
N_EXAMPLES = 20
FIELDS = ["kind", "step", "script", "args", "exit", "seconds", "file", "line", "col", "chain", "path", "calls", "matrices",
          "nonfinite", "not_pd", "negdet", "min_eig", "near_singular", "old_sts_n", "old_sts_min", "old_sts_max", "old_sts_sum",
          "bad_calls_n", "bad_calls", "examples"]
csv.field_size_limit(sys.maxsize)                         # a site's list of calls can exceed the default 131,072 characters


# ------------------------------------------------------------------ the wrappers (used by --child and --selftest)
def instrument(rp, stats, root):
    """Wrap rp._logdets and rp.atoms_from_corr of the module rp; the wrappers return what the functions return and
    record into the dict stats, keyed by (calling file, line, column, chain, path)."""
    own = Path(rp.__file__).resolve()
    me = Path(__file__).resolve()
    root = Path(root).resolve()
    venv = root / ".venv"
    orig_logdets, orig_atoms = rp._logdets, rp.atoms_from_corr
    sts_i = rp.ATOMS.index("sts")
    WRAPPERS = set()

    def rel(p):
        try:
            return Path(p).resolve().relative_to(root).as_posix()
        except ValueError:
            return str(p)

    def site():
        """(calling file, line, column, chain, path): the first frame outside rev_phiid_fast.py and outside these
        wrappers, the column of the call in it, and up to two frames of the repository that led to it."""
        f = sys._getframe(1)
        path = "other"
        while f is not None and (f.f_code in WRAPPERS or Path(f.f_code.co_filename).resolve() == own):
            if f.f_code not in WRAPPERS:
                if f.f_code.co_name == "atoms_from_corr":
                    path = "atoms_from_corr"
                elif f.f_code.co_name == "__init__" and path == "other":
                    path = "PairPhiID"
            f = f.f_back
        if f is None:
            return ("?", 0, 0, "", path)
        try:
            col = list(f.f_code.co_positions())[f.f_lasti // 2][2] or 0
        except (IndexError, TypeError):
            col = 0
        chain, g = [], f.f_back
        while g is not None and len(chain) < 2:
            if not g.f_code.co_filename.startswith("<"):                     # not runpy's frozen frames
                fn = Path(g.f_code.co_filename).resolve()
                if fn != own and fn != me and root in fn.parents and venv not in fn.parents:   # nor this file's, nor .venv's
                    chain.append(f"{rel(fn)}:{g.f_lineno}")
            g = g.f_back
        return (rel(f.f_code.co_filename), f.f_lineno, col, " < ".join(chain), path)

    def entry(key):
        if key not in stats:
            stats[key] = {"calls": 0, "matrices": 0, "nonfinite": 0, "not_pd": 0, "negdet": 0, "min_eig": float("inf"),
                          "near_singular": 0, "sts_n": 0, "sts_sum": 0.0, "sts_min": float("inf"),
                          "sts_max": float("-inf"), "examples": [], "bad_calls": [], "bad_calls_n": 0}
        return stats[key]

    def min_eigs(C):
        C = np.asarray(C, float).reshape(-1, 4, 4)
        fin = np.isfinite(C).all(axis=(1, 2))
        lam = np.full(C.shape[0], np.nan)
        if fin.any():
            lam[fin] = np.linalg.eigvalsh(C[fin]).min(axis=1)
        return C, fin, lam

    def old_sts(Cb):
        """the sts the code before B26 gave matrices: _plugin_mis on the unsigned log-determinants."""
        with np.errstate(all="ignore"):
            ld = orig_logdets(Cb)
            mi = {k: 0.5 * (ld[A] + ld[B] - ld[tuple(sorted(A + B))]) for k, (A, B) in rp._MI_SETS.items()}
            return (rp._assemble(mi, rp._mmi_choice(mi)) @ rp._MINV_T)[:, sts_i]

    def record(e, C3, fin, lam):
        bad = fin & (lam <= 0)
        e["calls"] += 1
        e["matrices"] += int(C3.shape[0])
        e["nonfinite"] += int((~fin).sum())
        e["not_pd"] += int(bad.sum())
        e["near_singular"] += int((fin & (lam > 0) & (lam <= NEAR)).sum())
        if fin.any():
            e["min_eig"] = min(e["min_eig"], float(np.nanmin(lam)))
        n_bad = int(bad.sum() + (~fin).sum())
        if n_bad:                                           # every such call: its ordinal and its number of matrices
            e["bad_calls_n"] += 1
            e["bad_calls"].append([e["calls"], n_bad])
        if bad.any():
            neg = np.zeros(C3.shape[0], bool)
            for A in rp._SUBSETS:
                if len(A) > 1:
                    idx = np.array(A)
                    sign = np.linalg.slogdet(C3[bad][:, idx[:, None], idx[None, :]])[0]
                    neg[np.where(bad)[0][sign <= 0]] = True
            e["negdet"] += int(neg.sum())
        return bad

    def logdets(C):
        out = orig_logdets(C)
        key = site()
        if key[4] != "atoms_from_corr":                  # the atoms_from_corr wrapper records its own matrices, before
            record(entry(key), *min_eigs(C))             # atoms_from_corr puts placeholders in the rows without atoms
        return out

    def atoms_from_corr(C):
        A = orig_atoms(C)
        C3, fin, lam = min_eigs(C)
        key = site()
        bad = record(entry(key[:4] + ("atoms_from_corr",)), C3, fin, lam)
        if bad.any():
            e = entry(key[:4] + ("atoms_from_corr sts",))
            s = old_sts(C3[bad])
            fs = s[np.isfinite(s)]
            e["sts_n"] += int(s.size)
            e["sts_sum"] += float(np.sum(fs))
            if fs.size:
                e["sts_min"] = min(e["sts_min"], float(np.min(fs)))
                e["sts_max"] = max(e["sts_max"], float(np.max(fs)))
            for k, v in zip(np.where(bad)[0][:max(0, N_EXAMPLES - len(e["examples"]))], s):
                M = C3[k]
                e["examples"].append([float(M[0, 2]), float(M[1, 3]), float(0.5 * (M[0, 1] + M[2, 3])), float(M[0, 3]),
                                      float(M[1, 2]), float(lam[k]), float(v)])
        return A

    WRAPPERS.update({logdets.__code__, atoms_from_corr.__code__, site.__code__, old_sts.__code__, record.__code__,
                     rel.__code__})
    rp._logdets = logdets
    rp.atoms_from_corr = atoms_from_corr
    return orig_logdets, orig_atoms


def num_or_none(x):
    return x if np.isfinite(x) else None


def dump(stats, path, step):
    with open(path, "a", encoding="utf-8") as fh:
        for (f, line, col, chain, p), e in stats.items():
            d = dict(e)
            for k in ("min_eig", "sts_min", "sts_max"):
                d[k] = num_or_none(d[k])
            fh.write(json.dumps({"step": step, "file": f, "line": line, "col": col, "chain": chain, "path": p, **d}) + "\n")


# ------------------------------------------------------------------ --child: one step under the wrappers
if len(sys.argv) > 1 and sys.argv[1] == "--child":
    jsonl, step, script, args = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]
    root = Path.cwd().resolve()
    sys.path.insert(0, str(root / "notes"))
    import rev_phiid_fast  # noqa: E402  (the repository's copy, found first)
    assert Path(rev_phiid_fast.__file__).resolve().parent == root / "notes", rev_phiid_fast.__file__
    STATS = {}
    instrument(rev_phiid_fast, STATS, root)
    sys.argv = [str(root / script)] + args
    try:                                                 # a SystemExit or an exception of the step passes through, with
        runpy.run_path(str(root / script), run_name="__main__")      # its message or traceback, as when run directly
    finally:
        dump(STATS, jsonl, step)
    sys.exit(0)


# ------------------------------------------------------------------ --selftest: the wrappers and the child alone
def selftest():
    sys.path.insert(0, str(HERE))
    import importlib
    rp = importlib.import_module("rev_phiid_fast")
    rng = np.random.default_rng(20261120)
    B = rng.normal(size=(50, 4, 8))
    good = np.einsum("nij,nkj->nik", B, B)
    d = np.sqrt(np.einsum("nii->ni", good))
    good = good / (d[:, :, None] * d[:, None, :])
    bad = rp.ar1_corr(np.array([0.9608, 0.96]), np.array([0.7538, 0.75]), np.array([0.8684, 0.87]))
    C = np.concatenate([good, bad])
    ref_atoms = rp.atoms_from_corr(C)
    ref_ld = rp._logdets(C)
    ref_pair = rp.PairPhiID(rng.normal(size=(5, 120))).atoms_mean()
    ld_bad = rp._logdets(bad)                                 # the code before B26: its sts from the unsigned log-determinants
    mi_bad = {k: 0.5 * (ld_bad[A] + ld_bad[Bk] - ld_bad[tuple(sorted(A + Bk))]) for k, (A, Bk) in rp._MI_SETS.items()}
    ref_old = (rp._assemble(mi_bad, rp._mmi_choice(mi_bad)) @ rp._MINV_T)[:, rp.ATOMS.index("sts")]
    stats = {}
    o1, o2 = instrument(rp, stats, HERE.parent)
    fails = []
    try:
        got = rp.atoms_from_corr(C)
        got_ld = rp._logdets(C)
        rng2 = np.random.default_rng(20261120)
        rng2.normal(size=(50, 4, 8))
        got_pair = rp.PairPhiID(rng2.normal(size=(5, 120))).atoms_mean()
    finally:
        rp._logdets, rp.atoms_from_corr = o1, o2
    if not (np.array_equal(got, ref_atoms, equal_nan=True) and all(np.array_equal(got_ld[k], ref_ld[k]) for k in ref_ld)
            and np.array_equal(got_pair, ref_pair)):
        fails.append("the wrapped functions do not return what the functions return")
    if not (np.isnan(ref_atoms[50:]).all() and np.isfinite(ref_atoms[:50]).all()):
        fails.append("rev_phiid_fast.atoms_from_corr does not give NaN exactly for the two matrices that are not positive definite")
    by_path = {}
    for (f, line, col, chain, p), e in stats.items():
        by_path.setdefault(p, []).append(e)
    afc = sum(e["matrices"] for e in by_path.get("atoms_from_corr", []))
    afc_bad = sum(e["not_pd"] for e in by_path.get("atoms_from_corr", []))
    oth = sum(e["matrices"] for e in by_path.get("other", []))
    oth_bad = sum(e["not_pd"] for e in by_path.get("other", []))
    pair = sum(e["matrices"] for e in by_path.get("PairPhiID", []))
    pair_bad = sum(e["not_pd"] for e in by_path.get("PairPhiID", []))
    sts = by_path.get("atoms_from_corr sts", [{}])[0]
    if int((np.linalg.eigvalsh(C).min(axis=1) <= 0).sum()) != 2:
        fails.append("the test's two AR(1) matrices are not both non-positive-definite")
    if (afc, afc_bad) != (52, 2):
        fails.append(f"atoms_from_corr path: {afc} matrices, {afc_bad} not positive definite (expected 52, 2)")
    if (oth, oth_bad) != (52, 2):
        fails.append(f"direct _logdets path: {oth} matrices, {oth_bad} not positive definite (expected 52, 2)")
    if (pair, pair_bad) != (10, 0):
        fails.append(f"PairPhiID path: {pair} matrices, {pair_bad} not positive definite (expected 10, 0)")
    if [e["bad_calls"] for e in by_path.get("atoms_from_corr", [])] != [[[1, 2]]]:
        fails.append(f"the call that held the two matrices: {[e['bad_calls'] for e in by_path.get('atoms_from_corr', [])]}")
    if sts.get("sts_n") != 2 or len(sts.get("examples", [])) != 2 or \
            not np.allclose([x[6] for x in sts.get("examples", [])], ref_old, rtol=0, atol=1e-12):
        fails.append("the sts the code before B26 gave the two matrices were not recovered")
    for (f, line, col, chain, p), e in stats.items():
        if f != "notes/partB26_positive_definite.py":
            fails.append(f"a call attributed to {f}, not to this file")
    # the child: two calls on one line are two sites; the step's own exit message and status pass through
    with tempfile.TemporaryDirectory() as td:
        step = Path(td) / "b26_selftest_step.py"
        step.write_text("import sys\nsys.path.insert(0, 'notes')\nimport numpy as np\n"
                        "from rev_phiid_fast import atoms_from_corr, ar1_corr\n"
                        "a = atoms_from_corr(ar1_corr(0.9608, 0.7538, 0.8684)); b = atoms_from_corr(ar1_corr(0.85, 0.85, 0.25))\n"
                        "print('nan', bool(np.isnan(a).all()), 'finite', bool(np.isfinite(b).all()), flush=True)\n"
                        "sys.exit('B26 self-test step: its own exit message')\n", encoding="utf-8")
        js = Path(td) / "c.jsonl"
        p = subprocess.run([sys.executable, "-u", str(Path(__file__).resolve()), "--child", str(js), "selftest", str(step)],
                           cwd=HERE.parent, capture_output=True, text=True, errors="replace")
        rows = [json.loads(l) for l in js.read_text().splitlines()] if js.exists() else []
        sites = sorted((r["line"], r["col"], r["path"], r["matrices"], r["not_pd"]) for r in rows if r["path"] == "atoms_from_corr")
        if p.returncode != 1 or "B26 self-test step: its own exit message" not in p.stdout + p.stderr or "nan True finite True" not in p.stdout:
            fails.append(f"the child did not pass the step's output, exit message and status through (exit {p.returncode})")
        if len(sites) != 2 or sites[0][:2] == sites[1][:2] or sites[0][0] != 5 or [s[3:] for s in sites] != [(1, 1), (1, 0)]:
            fails.append(f"the child's sites: {sites}")
    print(f"B26 SELF-TEST: {len(stats)} sites; atoms_from_corr {afc} matrices ({afc_bad} not PD, NaN now; before B26 their sts "
          f"was {sts.get('sts_min', float('nan')):.4f} to {sts.get('sts_max', float('nan')):.4f}); _logdets {oth} ({oth_bad}); PairPhiID {pair} "
          f"({pair_bad}); the call that held them recorded; the child: two sites on one line, the step's exit message and "
          f"status passed through; {len(fails)} failed" + ("".join(f"\n   FAILED: {x}" for x in fails)))
    return len(fails)


if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
    sys.exit(1 if selftest() else 0)

# ------------------------------------------------------------------ the run
REPO = HERE.parent
sys.path.insert(0, str(HERE))
if len(sys.argv) > 1 and sys.argv[1] == "--steps":                  # the names --from takes, in order, and nothing else
    STEPS_ONLY = True
else:
    STEPS_ONLY = False
    from rev_git import SHA  # noqa: E402
    print(f"git={SHA}", flush=True)
FLAG = "--check-from" if "--check-from" in sys.argv else "--from"          # --check-from: the checks of --from, nothing run
CHECK_ONLY = FLAG == "--check-from"
FROM = sys.argv[sys.argv.index(FLAG) + 1] if FLAG in sys.argv and sys.argv.index(FLAG) + 1 < len(sys.argv) else None
if STEPS_ONLY:
    SHA = ""
if FLAG in sys.argv and FROM is None:
    sys.exit(f"B26 {FLAG} NOT RUN: name the step")
OUT = REPO / "notes" / "review_results" / "partB"
CSVP, TABP = OUT / "positive_definite.csv", OUT / "positive_definite_tables.md"
RUN_LOG = "notes/review_results/partB/positive_definite_run.log"             # the tee of the command in the docstring
OUTPUT_DIRS = ("results/", "notes/review_results/", "manuscript/figures/")
OUTPUT_FILES = ("notes/review_computations_2026-09-14.md",)                   # rewritten by rev_assemble.py, a step of section 6
status = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=REPO, capture_output=True,
                        text=True).stdout.splitlines() if not STEPS_ONLY else []
if STEPS_ONLY:
    pass
elif FROM is None:
    dirty = [l for l in status if l[3:] != RUN_LOG]
    if SHA.endswith("-dirty") or dirty:
        sys.exit(f"B26 NOT RUN: the tree is not clean ({dirty[:3]}); commit or restore first")
else:
    dirty = [l for l in status if not l[3:].strip('"').startswith(OUTPUT_DIRS) and l[3:].strip('"') not in OUTPUT_FILES]
    if SHA.endswith("-dirty") or dirty:
        sys.exit(f"B26 --from NOT RUN: files outside the outputs have changed ({dirty[:3]})")
    if not CSVP.exists() or f"git={SHA};" not in CSVP.read_text(encoding="utf-8").split("\n", 1)[0]:
        sys.exit(f"B26 --from NOT RUN: {CSVP.relative_to(REPO)} of a full run at {SHA} is not there")
t0 = time.time()
G0 = time.gmtime()
RUN_UTC = f"{G0.tm_mday} {time.strftime('%b %Y %H:%M', G0)} UTC"
DECONV_MAT = REPO / "notes/review_results/deconv/DMT_clean_mni_continuous_fullPreprocsch116.mat"
SKIP = {"notes/partB25_binarised.py"}


def steps_of_section6():
    """(kind, log, script, args) of every step of run_all.sh's section 6, in order, B25 excepted; the deconvolution
    block expanded as run_all.sh expands it, and only if its sandbox is present."""
    lines = (REPO / "run_all.sh").read_text(encoding="utf-8").split("\n")
    i6 = next(i for i, l in enumerate(lines) if l.startswith("# 6."))
    out, in_deconv = [], False
    for l in lines[i6:]:
        s = l.strip()
        if s.startswith('if [ -f "$DECONV_MAT" ]'):
            in_deconv = True
            continue
        if s == "else" or s == "fi":
            in_deconv = False
            continue
        m = re.match(r"(nstep|nrun|step)\s+(.*)$", s)
        if not m:
            continue
        kind, toks = m.group(1), shlex.split(m.group(2))
        log, script, args = (None, toks[0], toks[1:]) if kind == "nrun" else (toks[0], toks[1], toks[2:])
        if in_deconv and not DECONV_MAT.exists():
            continue
        if script in SKIP:
            continue
        if "$" in " ".join(toks):                         # the deconvolution loop, expanded as run_all.sh does
            for se in ("deconv", "raw"):
                for v in ("ts_gsr", "ts_demean"):
                    for e in ("win60", "global"):
                        sub = {"s": se, "v": v, "e": e}
                        f = lambda t: re.sub(r"\$\{?([sve])\}?", lambda x: sub[x.group(1)], t)
                        out.append((kind, f(log), script, [f(a) for a in args]))
            continue
        out.append((kind, log, script, args))
    return out


def step_name(kind, log, script):
    return log or Path(script).stem


ALL = steps_of_section6()
NAMES = [step_name(*x[:3]) for x in ALL]
if STEPS_ONLY:
    print("\n".join(NAMES))
    sys.exit(0)
if FROM is not None and FROM not in NAMES:
    sys.exit(f"B26 --from NOT RUN: unknown step {FROM!r}; the steps: {NAMES}")
STEPS = ALL[NAMES.index(FROM):] if FROM is not None else ALL
HEAD_OLD, ROWS_OLD = "", []
if FROM is not None:
    # every step before FROM must have its row in the CSV, run to its end (exit status 0); an interrupted run's first line
    # ends "; partial: k of n steps", which becomes "; interrupted after k of n steps"
    _text = CSVP.read_text(encoding="utf-8")
    HEAD_OLD, _body = _text.split("\n", 1)
    _rows = list(csv.DictReader(io.StringIO(_body)))
    _done = {r["step"]: r["exit"] for r in _rows if r["kind"] == "step"}
    _gap = [n for n in NAMES[:NAMES.index(FROM)] if _done.get(n) != "0"]
    if _gap:
        sys.exit(f"B26 --from NOT RUN: the step {_gap[0]!r}, before {FROM!r}, did not run to its end in the run at {SHA} (its "
                 f"row: {'exit status ' + _done[_gap[0]] if _gap[0] in _done else 'none'}); resume from it")
    HEAD_OLD = re.sub(r"; partial: (\d+) of (\d+) steps$", r"; interrupted after \1 of \2 steps", HEAD_OLD)
    _redo = {step_name(*x[:3]) for x in STEPS}
    ROWS_OLD = [r for r in _rows if r["step"] not in _redo]
    if CHECK_ONLY:
        print(f"B26 --check-from {FROM}: ready; the run at {SHA} holds {len(_done)} step rows, the {NAMES.index(FROM)} before "
              f"{FROM!r} run to their end; {len(STEPS)} steps to run")
        sys.exit(0)
print(f"python {platform.python_version()}, numpy {np.__version__}; {len(STEPS)} of the {len(ALL)} steps of run_all.sh's "
      f"section 6 (B25 excepted)" + (f", re-run with --from {FROM} at {RUN_UTC}" if FROM is not None else ""), flush=True)
TMP = Path(tempfile.mkdtemp(prefix="b26_"))
JSONL = TMP / "stats.jsonl"
RESULTS = []
VERSIONS = f"python {platform.python_version()}, numpy {np.__version__}"


def fmt_cell(v):
    if v is None:
        return ""
    if isinstance(v, float):
        return repr(v)
    return str(v)


def I(r, k):
    return int(r[k]) if r[k] not in ("", None) else 0


def F(r, k):
    return float(r[k]) if r[k] not in ("", None) else float("nan")


def write_atomic(path, text):
    """written to a temporary file beside it, flushed to the disk and renamed over it, so that a power loss leaves the
    file as it was or as it is now, never a part of it"""
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)
    d = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(d)
    finally:
        os.close(d)


def write_outputs(final):
    """positive_definite.csv from the steps run so far (and, under --from, the full run's other rows), then the tables
    from the CSV alone; called before the first step and after every step, so that an interrupted run leaves the counts
    of the steps it finished (the first line then ends "; partial: k of n steps")."""
    new = [json.loads(l) for l in JSONL.read_text(encoding="utf-8").splitlines()] if JSONL.exists() else []
    rows = list(ROWS_OLD)
    for res in RESULTS:
        rows.append({k: fmt_cell(res.get(k)) for k in FIELDS})
    for r in new:
        rows.append({"kind": "site", "step": r["step"], "file": r["file"], "line": r["line"], "col": r["col"],
                     "chain": r["chain"], "path": r["path"], "calls": r["calls"], "matrices": r["matrices"],
                     "nonfinite": r["nonfinite"], "not_pd": r["not_pd"], "negdet": r["negdet"],
                     "min_eig": fmt_cell(r["min_eig"]), "near_singular": r["near_singular"], "old_sts_n": r["sts_n"],
                     "old_sts_min": fmt_cell(r["sts_min"]), "old_sts_max": fmt_cell(r["sts_max"]),
                     "old_sts_sum": fmt_cell(r["sts_sum"]) if r["path"] == "atoms_from_corr sts" else "",
                     "bad_calls_n": r["bad_calls_n"] if r["path"] != "atoms_from_corr sts" else "",
                     "bad_calls": json.dumps(r["bad_calls"]) if r["bad_calls"] else "",
                     "examples": json.dumps(r["examples"]) if r["examples"] else ""})
    order = {n: i for i, n in enumerate(NAMES)}
    rows.sort(key=lambda r: (order.get(r["step"], 10 ** 6), r["kind"] != "step"))
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    head = (f"# partB26_positive_definite.py; git={SHA}; run {RUN_UTC}; {VERSIONS}" if FROM is None else
            HEAD_OLD + f"; re-run with --from {FROM} at {RUN_UTC}, {VERSIONS}")
    if not final:
        head += f"; partial: {len(RESULTS)} of {len(STEPS)} steps"
    csv_text = head + "\n" + buf.getvalue()
    OUT.mkdir(parents=True, exist_ok=True)
    write_atomic(CSVP, csv_text)
    tables(csv_text)
    return csv_text


def tables(csv_text):
    """positive_definite_tables.md, made from the CSV's text alone"""
    csv_sha = hashlib.sha256(csv_text.encode("utf-8")).hexdigest()
    head, body = csv_text.split("\n", 1)
    rows = list(csv.DictReader(io.StringIO(body)))
    steps_rows = [r for r in rows if r["kind"] == "step"]
    sites = [r for r in rows if r["kind"] == "site" and r["path"] != "atoms_from_corr sts"]
    failed = [r for r in steps_rows if I(r, "exit") != 0]
    n_mat, n_bad, n_nonfin = sum(I(r, "matrices") for r in sites), sum(I(r, "not_pd") for r in sites), sum(I(r, "nonfinite") for r in sites)
    n_near, n_neg = sum(I(r, "near_singular") for r in sites), sum(I(r, "negdet") for r in sites)
    eigs = [F(r, "min_eig") for r in sites if r["min_eig"] not in ("", None)]
    parts = head.split("; ")
    partial = re.search(r"partial: (\d+) of (\d+) steps", head)
    L = ["# B26: the matrices that are not positive definite, corrected and counted (partB26_positive_definite.py)",
         parts[1], "; ".join(parts[2:]), f"positive_definite.csv sha256 {csv_sha}", "",
         "Pre-run entry: record, \"The matrices that are not positive definite (B26): pre-run entry\". Made from "
         "positive_definite.csv alone (its first line: the commit, the time of the run, the versions and any re-run). "
         + (f"PARTIAL: {partial.group(1)} of the {partial.group(2)} steps of this invocation have run; the counts are "
            f"those of the steps listed below. " if partial else "")
         + f"Steps: {len(steps_rows)} of run_all.sh's section 6, B25 excepted, run in place with "
         f"rev_phiid_fast.atoms_from_corr returning NaN for a matrix that is not positive definite; "
         f"{len(steps_rows) - len(failed)} ran to the end"
         + (f", {len(failed)} did not ({', '.join(r['script'] for r in failed)})" if failed else "")
         + f"; they took {sum(I(r, 'seconds') for r in steps_rows):,} s in all, by their rows.", "",
         f"Evaluations of matrices by rev_phiid_fast, summed over the steps (a data window evaluated by several steps is "
         f"counted in each; the number of the data's pair-windows without a substituted estimate is partB4_diagnostic.py's, "
         f"on its level lines; the whole-run pairs without one are in the site rows of each step's run-level line): "
         f"{n_mat:,}; with a non-finite entry {n_nonfin:,}; not positive definite {n_bad:,}, of which {n_neg:,} with a block "
         f"determinant ≤ 0; near-singular (smallest eigenvalue in (0, 10⁻³]) {n_near:,}; smallest eigenvalue "
         f"{min(eigs) if eigs else float('nan'):.3g}.", "",
         "## By step", "",
         "| step | script | exit | s | matrices (PairPhiID) | matrices (atoms_from_corr) | not positive definite | non-finite | near-singular | smallest eigenvalue |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for res in steps_rows:
        rs = [r for r in sites if r["step"] == res["step"]]
        ev = [F(r, "min_eig") for r in rs if r["min_eig"] not in ("", None)]
        L.append(f"| {res['step']} | {' '.join(x for x in (res['script'], res['args']) if x)} | {res['exit']} | {res['seconds']} | "
                 f"{sum(I(r, 'matrices') for r in rs if r['path'] == 'PairPhiID'):,} | "
                 f"{sum(I(r, 'matrices') for r in rs if r['path'] == 'atoms_from_corr'):,} | {sum(I(r, 'not_pd') for r in rs):,} | "
                 f"{sum(I(r, 'nonfinite') for r in rs):,} | {sum(I(r, 'near_singular') for r in rs):,} | "
                 f"{min(ev) if ev else float('nan'):.3g} |")
    L += ["", "## Sites with matrices that are not positive definite or not finite", "",
          "A site is a calling line and column (file:line:column), with the frames of the repository that led to it in brackets; "
          "the last column gives the number of the site's calls that held such matrices and, for the first ten, the call's "
          "ordinal and its number of such matrices (#ordinal: matrices); the CSV lists every one.", ""]
    bad_rows = [r for r in sites if I(r, "not_pd") + I(r, "nonfinite") > 0]
    if not bad_rows:
        L.append("None.")
    else:
        L += ["| step | site | path | calls | matrices | not positive definite | non-finite | share | block determinant ≤ 0 | smallest eigenvalue | calls that held them |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in bad_rows:
            where = f"{r['file']}:{r['line']}:{r['col']}" + (f" ({r['chain']})" if r["chain"] else "")
            bc = json.loads(r["bad_calls"]) if r["bad_calls"] else []
            L.append(f"| {r['step']} | {where} | {r['path']} | {I(r, 'calls'):,} | {I(r, 'matrices'):,} | {I(r, 'not_pd'):,} | "
                     f"{I(r, 'nonfinite'):,} | {(I(r, 'not_pd') + I(r, 'nonfinite')) / max(I(r, 'matrices'), 1):.2e} | {I(r, 'negdet'):,} | "
                     f"{F(r, 'min_eig'):.3g} | {I(r, 'bad_calls_n'):,} — " + ", ".join(f"#{a}: {b}" for a, b in bc[:10])
                     + (" …" if len(bc) > 10 else "") + " |")
        L += ["", "The sts that the code before B26 gave the matrices that are not positive definite (atoms_from_corr path), and the "
              "first examples (a_x, a_y, q, C[0, 3], C[1, 2], smallest eigenvalue, sts before B26):", ""]
        for r in [r for r in rows if r["kind"] == "site" and r["path"] == "atoms_from_corr sts"]:
            ex = json.loads(r["examples"]) if r["examples"] else []
            ex_s = "; ".join("(" + ", ".join(f"{v:+.4f}" if i != 5 else f"{v:.2e}" for i, v in enumerate(x)) + ")" for x in ex[:5])
            lo, hi = r["old_sts_min"], r["old_sts_max"]
            rng_s = f"from {float(lo):+.4f} to {float(hi):+.4f}" if lo not in ("", None) and hi not in ("", None) else "not finite"
            L.append(f"- {r['step']}, {r['file']}:{r['line']}:{r['col']}" + (f" ({r['chain']})" if r["chain"] else "")
                     + f": {I(r, 'old_sts_n'):,} values, {rng_s}; examples: {ex_s}")
    write_atomic(TABP, "\n".join(L) + "\n")
    return L


write_outputs(final=False)                               # the counts exist from the start: "partial: 0 of n steps"
for kind, log, script, args in STEPS:
    dest = None if kind == "nrun" else (REPO / "notes/review_results" / f"{log}.log" if kind == "nstep"
                                        else REPO / "results" / f"run_{log}.log")
    cmd = " ".join([script] + args)
    print(f"=== {time.strftime('%Y-%m-%d %H:%M:%S')}  {cmd}" + (f"   -> {dest.relative_to(REPO)}" if dest else ""), flush=True)
    t1 = time.time()
    fh = open(dest, "w", encoding="utf-8", buffering=1) if dest else None         # line-buffered, as tee writes
    p = subprocess.Popen([sys.executable, "-u", str(Path(__file__).resolve()), "--child", str(JSONL), step_name(kind, log, script),
                          script] + args, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace",
                         bufsize=1)
    for line in p.stdout:
        sys.stdout.write(line)
        if fh:
            fh.write(line)
    code = p.wait()
    if fh:
        fh.close()
    RESULTS.append({"kind": "step", "step": step_name(kind, log, script), "script": script, "args": " ".join(args), "exit": code,
                    "seconds": f"{time.time() - t1:.0f}"})
    if code != 0:
        print(f"=== STEP FAILED (exit {code}): {cmd}", flush=True)
    write_outputs(final=False)
print(f"=== all done in {int((time.time() - t0) // 60)} min", flush=True)
write_outputs(final=True)
JSONL.unlink(missing_ok=True)
TMP.rmdir()
print(TABP.read_text(encoding="utf-8"), end="", flush=True)
sys.exit(1 if any(r["exit"] != 0 for r in RESULTS) else 0)
