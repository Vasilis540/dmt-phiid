"""11_ccs_agree_share_check.py — the investigation of the one difference beyond tolerance that the comparisons of
the final run of run_all.sh (26 September 2026, at c25a310) found: the arrays
notes/review_results/partB/ccs_agree_share_ts_gsr.npy and ccs_agree_share_ts_demean.npy, which 8_binary_compare.py
found to differ from their committed versions by up to 4.4e-5 and 3.62e-5.

Usage, from the repository root, in the pinned environment, on the working tree the run left (nothing in the
repository is written or changed; the output folder must lie outside the repository):
    .venv/bin/python <this script> <reference commit> <output folder>
It goes twice through the fits of notes/partB2_ccs_run.py with that script's code (notes/rev_phiid_fast.py, imported
unchanged): once as the run did, and once in a child process of itself in which only the numerical kernels differ
(OpenBLAS forced to its Nehalem kernels, and NumPy's AVX2 and AVX-512 dispatch groups disabled where the machine has
them); the code and the data are the same.

What the arrays hold. For each variant, subject, run and fit (windows 1-14 of W = 60, and the global fit),
notes/partB2_ccs_run.py writes the share of the fit's pair-samples at which phyid's CCS mask keeps the double
co-information D as the double redundancy: the samples where sign(I_xta) = sign(I_xtb) = sign(I_yta) = sign(I_ytb)
= sign(D) (notes/rev_phiid_fast.py, ccs_local_knowns). The mean of a fit's shares over its pairs is its entry.

The explanation tested. D = -I_xta - I_xtb - I_yta - I_ytb + I_xtab + I_ytab + I_xyta + I_xytb - I_xytab + R_xyta
+ R_xytb - R_xytab + R_abtx + R_abty - R_abtxy, where each single-target CCS redundancy R is its co-information
where four signs agree and 0 elsewhere. Of the 64 patterns of kept and zeroed redundancies, exactly two make D
identically zero as a function of the nine local mutual informations (this script derives them with integer
arithmetic and prints them): R_xyta, R_xytb and R_xytab kept with R_abtx, R_abty and R_abtxy zeroed, and the reverse
("the two patterns"). At such a sample the
computed D is the rounding residual of fifteen terms that cancel, and its sign is set by the last bits of the
arithmetic; where the other four signs agree ("an ambiguous sample"), the mask's decision is therefore set by the
machine and the numerical build, not by the data. The D kept at such a sample is of the order of 1e-16, so the
atoms do not see the decision; the share counts it. The committed arrays were written on 14 September 2026 (709415d)
by a Claude session, whose NumPy/SciPy build differed from the laptop's .venv (the record, "The end-to-end run of
run_all.sh and its reproduction checks", 16 September 2026, item 2); the regenerated ones on V.S.'s laptop.

Predictions, fixed before this script ran:
 (1) Reproduction on this machine: every share and every W = 60 atom mean recomputed here equals, exactly, the
     value in the regenerated arrays (ccs_agree_share_<variant>.npy, ccs_atoms_win60_<variant>.npy), and the fits
     the run skipped are NaN there.
 (2) Separation: in every fit, every sample of the two patterns has |D| < 1e-12, and no other sample has.
 (3) The mechanism, by reordering: D summed in the reverse order of its fifteen terms (algebraically the same sum)
     changes the mask's decision at ambiguous samples only.
 (4) The mechanism, by changing the kernels: in the child process, sample by sample, the samples where the four
     single-target signs agree, the samples of the two patterns and the decisions at every sample that is not
     ambiguous are identical to this process's in every fit, so that the two processes' counts of kept samples
     differ only by their counts of ambiguous samples kept.
 (5) Consistency with the committed arrays: in every fit the committed share times the fit's number of
     pair-samples N is an integer k_c (within 1e-6), and k_c lies between the number of samples kept at samples
     that are not ambiguous and that number plus the number of ambiguous samples.
 (6) If the stash of 16 September 2026 ("section-6 rerun at d145e1c", V.S.'s regeneration on this laptop) exists:
     the two arrays the run regenerated are byte-identical to that day's. Every other binary the run modified is
     listed as identical to that day's regeneration or not (reported, not predicted).

Writes into the output folder: 11_ccs_agree_share_check.log (this report, also printed), 11_ccs_agree_share_cells.csv
(one row per fit), fits_this_process.json and fits_child_process.json (the counts and the per-fit sha256 of the masks
compared in (4)), and copies of the two arrays as regenerated, as committed at the reference commit and as stashed
on 16 September; then packs the folder into <output folder>.tar.gz beside it.
"""
import csv
import hashlib
import io
import itertools
import json
import os
import platform
import subprocess
import sys
import tarfile
import time
from pathlib import Path

sys.dont_write_bytecode = True           # nothing is written into the repository, not even a bytecode cache

CHILD = len(sys.argv) > 1 and sys.argv[1] == "--child"
ARGS = sys.argv[2:] if CHILD else sys.argv[1:]
if len(ARGS) != 2:
    raise SystemExit(__doc__)
REPO = Path.cwd().resolve()
OUT = Path(ARGS[1]).expanduser().resolve()
if not ((REPO / "notes" / "rev_phiid_fast.py").is_file() and (REPO / "notes" / "partB2_ccs_run.py").is_file()
        and (REPO / ".git").exists()):
    raise SystemExit(f"STOP: run this from the repository root (the folder that holds notes/ and .git); "
                     f"the current folder is {REPO}")
if OUT == REPO or REPO in OUT.parents:
    raise SystemExit(f"STOP: the output folder {OUT} lies inside the repository; give one outside it")

import numpy as np                        # noqa: E402  (after the checks, as the child's kernels depend on its environment)
import scipy                              # noqa: E402
import scipy.io as sio                    # noqa: E402

sys.path.insert(0, str(REPO / "notes"))
from rev_phiid_fast import PairPhiID, ccs_local_knowns, _MINV_T   # noqa: E402  (the run's code, unchanged)

PARTB = "notes/review_results/partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
VARIANTS = ("ts_gsr", "ts_demean")
RUNS = ("DMT", "PCB")
CHUNK = 800                               # as PairPhiID.atoms_ccs
SMALL = 1e-12
MI_NAMES = ("I_xta", "I_xtb", "I_yta", "I_ytb", "I_xyta", "I_xytb", "I_xtab", "I_ytab", "I_xytab")
# the six single-target CCS redundancies, in ccs_local_knowns' order and with its arguments (columns 1-6 of K)
TRIPLES = (("I_xta", "I_yta", "I_xyta"), ("I_xtb", "I_ytb", "I_xytb"), ("I_xtab", "I_ytab", "I_xytab"),
           ("I_xta", "I_xtb", "I_xtab"), ("I_yta", "I_ytb", "I_ytab"), ("I_xyta", "I_xytb", "I_xytab"))
COUNTS = ("k", "pattern", "ambiguous", "k_amb", "k_rev", "rev_changed", "rev_changed_outside", "pattern_not_small",
          "off_small", "exact_zero")


def zero_patterns():
    """the patterns of kept (1) and zeroed (0) redundancies, in the order of TRIPLES, under which D is identically
    zero as a linear form of the nine local MIs: its integer coefficient vector vanishes"""
    ix = {k: i for i, k in enumerate(MI_NAMES)}
    base = [0] * 9
    for sg, k in ((-1, "I_xta"), (-1, "I_xtb"), (-1, "I_yta"), (-1, "I_ytb"), (1, "I_xtab"), (1, "I_ytab"),
                  (1, "I_xyta"), (1, "I_xytb"), (-1, "I_xytab")):
        base[ix[k]] += sg
    signs = (1, 1, -1, 1, 1, -1)          # the signs of R_xyta, R_xytb, R_xytab, R_abtx, R_abty, R_abtxy in D
    out = []
    for pat in itertools.product((0, 1), repeat=6):
        v = list(base)
        for kept, sg, (a, b, ab) in zip(pat, signs, TRIPLES):
            if kept:                      # a kept redundancy is its co-information m_a + m_b - m_ab
                v[ix[a]] += sg
                v[ix[b]] += sg
                v[ix[ab]] -= sg
        if not any(v):
            out.append(pat)
    return out


ZERO = zero_patterns()


def git(*a, check=True):
    p = subprocess.run(["git", "--no-optional-locks", *a], capture_output=True, cwd=REPO)
    if check and p.returncode:
        raise SystemExit(f"STOP: git {' '.join(a)}: {p.stderr.decode(errors='replace').strip()}")
    return p.stdout


def kept_flag(m1, m2, m12):
    """whether _ccs_red keeps the co-information: its own test, on the same expressions"""
    co = m1 + m2 - m12
    return (np.sign(m1) == np.sign(m2)) & (np.sign(m1) == np.sign(m12)) & (np.sign(m1) == np.sign(co)), co


def one_fit(Xf):
    """One fit as notes/partB2_ccs_run.py makes it (PairPhiID(...).atoms_ccs(), chunks of 800 pairs), with the
    counts and masks of the predictions."""
    pp = PairPhiID(Xf)
    n_pairs, n = len(pp.pairs), pp.n
    share_pair = np.empty(n_pairs)
    atoms_pair = np.empty((n_pairs, 16))
    cnt = dict.fromkeys(COUNTS, 0)
    max_pat, min_off = 0.0, float("inf")
    h = {m: hashlib.sha256() for m in ("mi", "four", "pattern", "decided")}
    for start in range(0, n_pairs, CHUNK):
        sel = np.arange(start, min(start + CHUNK, n_pairs))
        mi = pp._local_mis(sel)
        K, D, agree = ccs_local_knowns(mi)
        atoms_pair[sel] = (K @ _MINV_T).mean(1)
        share_pair[sel] = agree.mean(1)
        kept = []
        for col, (a, b, ab) in enumerate(TRIPLES, start=1):
            f, co = kept_flag(mi[a], mi[b], mi[ab])
            if not np.array_equal(np.where(f, co, 0.0), K[..., col]):
                raise SystemExit(f"STOP: the redundancy of column {col} is not reproduced by _ccs_red's test")
            kept.append(f)
        pattern = np.zeros(kept[0].shape, bool)
        for pat in ZERO:
            m = np.ones(kept[0].shape, bool)
            for flag, bit in zip(kept, pat):
                m &= flag if bit else ~flag
            pattern |= m
        s0 = np.sign(mi["I_xta"])
        four = (s0 == np.sign(mi["I_xtb"])) & (s0 == np.sign(mi["I_yta"])) & (s0 == np.sign(mi["I_ytb"]))
        if not np.array_equal(agree, four & (s0 == np.sign(D))):
            raise SystemExit("STOP: the mask is not reproduced from its five signs")
        amb = pattern & four
        R = [K[..., col] for col in range(1, 7)]
        terms = [-mi["I_xta"], -mi["I_xtb"], -mi["I_yta"], -mi["I_ytb"], mi["I_xtab"], mi["I_ytab"], mi["I_xyta"],
                 mi["I_xytb"], -mi["I_xytab"], R[0], R[1], -R[2], R[3], R[4], -R[5]]
        fwd = terms[0]
        for t in terms[1:]:
            fwd = fwd + t
        if not np.array_equal(fwd, D):
            raise SystemExit("STOP: D is not reproduced from its fifteen terms in their order")
        rev = terms[-1]
        for t in terms[-2::-1]:
            rev = rev + t
        agree_rev = four & (s0 == np.sign(rev))
        changed = agree != agree_rev
        aD = np.abs(D)
        cnt["k"] += int(agree.sum())
        cnt["pattern"] += int(pattern.sum())
        cnt["ambiguous"] += int(amb.sum())
        cnt["k_amb"] += int((agree & amb).sum())
        cnt["k_rev"] += int(agree_rev.sum())
        cnt["rev_changed"] += int(changed.sum())
        cnt["rev_changed_outside"] += int((changed & ~amb).sum())
        cnt["pattern_not_small"] += int((pattern & (aD >= SMALL)).sum())
        cnt["off_small"] += int((~pattern & (aD < SMALL)).sum())
        cnt["exact_zero"] += int((pattern & (D == 0)).sum())
        if pattern.any():
            max_pat = max(max_pat, float(aD[pattern].max()))
        if (~pattern).any():
            min_off = min(min_off, float(aD[~pattern].min()))
        h["mi"].update(b"".join(np.ascontiguousarray(mi[k]).tobytes() for k in MI_NAMES))
        for name, m in (("four", four), ("pattern", pattern), ("decided", agree & ~amb)):
            h[name].update(np.packbits(m).tobytes())
    return {"n": int(n), "N": int(n_pairs * n), "share": float(share_pair.mean()),
            "atoms": [float(v) for v in atoms_pair.mean(0)], **cnt, "max_absD_pattern": max_pat,
            "min_absD_off": min_off, **{f"sha_{k}": v.hexdigest() for k, v in h.items()}}


def all_fits():
    """every fit of notes/partB2_ccs_run.py, in its order; None where the run skips a window (5 samples or fewer)"""
    ts = sio.loadmat(MAT)
    fits, t0 = [], time.time()
    for var in VARIANTS:
        for s in range(14):
            for c in range(2):
                X = np.asarray(ts[var][s, c], float)[REGIONS]
                kept = np.where(np.all(np.isfinite(X), axis=0))[0]
                for w in range(15):
                    idx = kept if w == 14 else kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                    if w < 14 and idx.size <= 5:
                        fits.append(None)
                        continue
                    fits.append({"var": var, "s": s, "c": c, "w": w, **one_fit(X[:, idx])})
            print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    return fits, time.time() - t0


def environment():
    env = {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
           "machine": platform.machine(), "cpu": "unknown"}
    try:
        for line in open("/proc/cpuinfo", encoding="utf-8", errors="replace"):
            if line.startswith("model name"):
                env["cpu"] = line.split(":", 1)[1].strip()
                break
    except OSError:
        pass
    try:
        from numpy._core._multiarray_umath import __cpu_features__ as feats
        env["numpy_features_on"] = [k for k in ("X86_V2", "X86_V3", "X86_V4", "AVX2", "FMA3", "AVX512F")
                                    if feats.get(k)]
    except Exception as e:                # noqa: BLE001
        env["numpy_features_on"] = f"unavailable ({type(e).__name__})"
    try:
        from threadpoolctl import threadpool_info
        env["blas"] = "; ".join(f"{d.get('internal_api')} {d.get('version')} {d.get('architecture')}"
                                for d in threadpool_info() if d.get("user_api") == "blas") or "none found"
    except Exception as e:                # noqa: BLE001
        env["blas"] = f"threadpoolctl unavailable ({type(e).__name__})"
    env["OPENBLAS_CORETYPE"] = os.environ.get("OPENBLAS_CORETYPE", "")
    env["NPY_DISABLE_CPU_FEATURES"] = os.environ.get("NPY_DISABLE_CPU_FEATURES", "")
    return env


if CHILD:
    fits, secs = all_fits()
    (OUT / "fits_child_process.json").write_text(json.dumps({"environment": environment(), "seconds": secs,
                                                             "fits": fits}), encoding="utf-8")
    sys.exit(0)

# ------------------------------------------------------------------------------------------------ the parent process
REF = git("rev-parse", "--verify", ARGS[0] + "^{commit}").decode().strip()
HEAD = git("rev-parse", "HEAD").decode().strip()
if subprocess.run(["git", "--no-optional-locks", "diff", "--quiet", REF, "--", "notes/rev_phiid_fast.py",
                   "notes/partB2_ccs_run.py"], cwd=REPO).returncode != 0:
    raise SystemExit(f"STOP: notes/rev_phiid_fast.py or notes/partB2_ccs_run.py differs from {REF[:7]}")
OUT.mkdir(parents=True, exist_ok=True)
LOG = []


def say(s=""):
    print(s, flush=True)
    LOG.append(s)


def sha(b):
    return hashlib.sha256(b).hexdigest()


say("# The CCS agreement-share arrays of the final run: investigation (11_ccs_agree_share_check.py)")
say(f"script sha256 {sha(Path(__file__).read_bytes())}")
say(f"started {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}; repository HEAD {HEAD}; reference {REF}")
envp = environment()
say("this process: " + "; ".join(f"{k} {v}" for k, v in envp.items()))
say("patterns of kept redundancies (R_xyta, R_xytb, R_xytab, R_abtx, R_abty, R_abtxy) under which D is identically "
    "zero: " + ", ".join(str(p) for p in ZERO) + f" ({len(ZERO)} of 64)")
say("")

# the arrays: regenerated (working tree), committed (reference commit), stashed on 16 September
say("## The arrays")
arrays = {}
for var in VARIANTS:
    for kind in ("agree_share", "atoms_win60"):
        rel = f"{PARTB}/ccs_{kind}_{var}.npy" if kind == "atoms_win60" else f"{PARTB}/ccs_agree_share_{var}.npy"
        new_b = (REPO / rel).read_bytes()
        old_b = git("show", f"{REF}:{rel}")
        arrays[(kind, var)] = (np.load(io.BytesIO(new_b)), np.load(io.BytesIO(old_b)))
        if kind == "agree_share":
            (OUT / f"regenerated_{Path(rel).name}").write_bytes(new_b)
            (OUT / f"committed_{REF[:7]}_{Path(rel).name}").write_bytes(old_b)
        a, b = arrays[(kind, var)]
        same_nan = np.array_equal(np.isnan(a), np.isnan(b))
        d = np.abs(a - b)[~np.isnan(a)] if same_nan else np.array([np.nan])
        say(f"{rel}: regenerated sha256 {sha(new_b)[:16]}…, committed sha256 {sha(old_b)[:16]}…; NaN pattern "
            f"{'the same' if same_nan else 'DIFFERS'}; max|diff| {d.max():.3g}; entries that differ "
            f"{int((d > 0).sum())} of {d.size}")
say("")

say("## The regeneration of 16 September 2026 (stash)")
stash_lines = git("stash", "list", "--format=%gd%x09%s").decode().splitlines()
S = next((l.split("\t")[0] for l in stash_lines if "section-6 rerun at d145e1c" in l), None)
say(f"stash entries: {len(stash_lines)}; the regeneration of 16 September: {S or 'NOT FOUND'}")
stash_same = None
if S:
    def in_stash(rel):
        """the file as V.S.'s regeneration of 16 September left it: None if it did not exist then, "unchanged" if that
        regeneration left it as committed at the time"""
        if subprocess.run(["git", "--no-optional-locks", "cat-file", "-e", f"{S}:{rel}"], cwd=REPO,
                          capture_output=True).returncode:
            return None
        b = git("show", f"{S}:{rel}")
        return "unchanged" if b == git("show", f"{S}^1:{rel}", check=False) else b

    status = git("status", "--porcelain", "--", "notes/review_results/", "results/").decode().splitlines()
    mod = sorted(l[3:].strip() for l in status if l[:2].strip() in ("M", "MM", "AM")
                 and l[3:].strip().endswith((".npy", ".npz", ".pkl")))
    tally = {}
    for rel in mod:
        b = in_stash(rel)
        v = ("not in the stash (new since)" if b is None else "not regenerated then" if b == "unchanged"
             else "identical to 16 Sep" if b == (REPO / rel).read_bytes() else "differs from 16 Sep")
        tally[v] = tally.get(v, 0) + 1
        say(f"   {v:<28} {rel}")
    say(f"binaries the run modified: {len(mod)}; " + "; ".join(f"{k} {v}" for k, v in tally.items()))
    stash_same = True
    for var in VARIANTS:
        rel = f"{PARTB}/ccs_agree_share_{var}.npy"
        b = in_stash(rel)
        if not isinstance(b, bytes):
            say(f"   {rel}: the stash holds no regeneration of it; prediction (6) is not tested")
            stash_same = None
            break
        (OUT / f"stash16_{Path(rel).name}").write_bytes(b)
        stash_same &= b == (REPO / rel).read_bytes()
say("")

# the two passes
say("## Pass 1: this process (the run's configuration)")
fits, secs = all_fits()
say(f"   done in {secs:.0f} s")
(OUT / "fits_this_process.json").write_text(json.dumps({"environment": envp, "seconds": secs, "fits": fits}),
                                            encoding="utf-8")
say("")
say("## Pass 2: a child process with other numerical kernels")
from numpy._core._multiarray_umath import __cpu_features__ as _F   # noqa: E402
cenv = dict(os.environ, OPENBLAS_CORETYPE="Nehalem")
groups = [g for g in ("X86_V3", "X86_V4") if _F.get(g)]
if groups:
    cenv["NPY_DISABLE_CPU_FEATURES"] = " ".join(groups)
    if subprocess.run([sys.executable, "-c", "import numpy"], env=cenv, capture_output=True).returncode:
        say(f"   NumPy does not start with NPY_DISABLE_CPU_FEATURES={cenv.pop('NPY_DISABLE_CPU_FEATURES')}; the child "
            "changes the OpenBLAS kernels only")
say(f"   OPENBLAS_CORETYPE=Nehalem; NPY_DISABLE_CPU_FEATURES={cenv.get('NPY_DISABLE_CPU_FEATURES', '(none)')}")
rc = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--child", REF, str(OUT)], cwd=REPO,
                    env=cenv).returncode
child = json.loads((OUT / "fits_child_process.json").read_text(encoding="utf-8")) if rc == 0 else None
if child:
    say("   child process: " + "; ".join(f"{k} {v}" for k, v in child["environment"].items()))
    say(f"   done in {child['seconds']:.0f} s")
else:
    say(f"   the child process FAILED (exit status {rc}); prediction (4) is not tested")
say("")

# the comparisons, fit by fit
rows = []
p1 = p2 = p3 = p4 = p5 = True
n_fit = n_skip = 0
for i, f in enumerate(fits):
    var, s, c, w = VARIANTS[i // 420], (i % 420) // 30, (i % 30) // 15, i % 15
    reg, com = (x[s, c, w] for x in arrays[("agree_share", var)])
    if f is None:
        n_skip += 1
        p1 &= bool(np.isnan(reg))
        p5 &= bool(np.isnan(com))
        if child:
            p4 &= child["fits"][i] is None
        continue
    n_fit += 1
    assert (f["var"], f["s"], f["c"], f["w"]) == (var, s, c, w)
    eq = f["share"] == reg
    if w < 14:
        eq &= bool(np.array_equal(np.asarray(f["atoms"]), arrays[("atoms_win60", var)][0][s, c, w]))
    p1 &= eq
    p2 &= f["pattern_not_small"] == 0 and f["off_small"] == 0
    p3 &= f["rev_changed_outside"] == 0
    k_dec = f["k"] - f["k_amb"]
    if np.isnan(com):                     # a fit computed here that the committed array does not hold
        kc, resid, inb = f["k"], float("inf"), False
    else:
        kc = int(round(float(com) * f["N"]))
        resid = abs(float(com) * f["N"] - kc)
        inb = resid < 1e-6 and k_dec <= kc <= k_dec + f["ambiguous"]
    p5 &= inb
    g = child["fits"][i] if child else None
    same_masks = g is not None and all(g[f"sha_{m}"] == f[f"sha_{m}"] for m in ("four", "pattern", "decided"))
    if child:
        p4 &= same_masks and g["k"] - f["k"] == g["k_amb"] - f["k_amb"]
    rows.append({"variant": var, "subject": s + 1, "run": RUNS[c], "fit": "global" if w == 14 else f"window {w + 1}",
                 "n": f["n"], "N": f["N"], "k": f["k"], "share": repr(f["share"]), "share_equals_regenerated": eq,
                 "share_committed": repr(float(com)), "k_committed": kc, "k_committed_residual": f"{resid:.1e}",
                 "dk_committed": kc - f["k"], "pattern": f["pattern"], "ambiguous": f["ambiguous"],
                 "k_amb": f["k_amb"], "k_decided": k_dec, "committed_in_bracket": inb,
                 "rev_changed": f["rev_changed"], "rev_changed_outside": f["rev_changed_outside"],
                 "max_absD_pattern": f"{f['max_absD_pattern']:.2e}", "min_absD_off": f"{f['min_absD_off']:.2e}",
                 "off_small": f["off_small"], "pattern_not_small": f["pattern_not_small"],
                 "exact_zero": f["exact_zero"],
                 "child_k": g["k"] if g else "", "child_k_amb": g["k_amb"] if g else "",
                 "child_dk": g["k"] - f["k"] if g else "", "child_mi_changed": (g["sha_mi"] != f["sha_mi"]) if g else "",
                 "child_masks_identical": same_masks if g else "",
                 "child_atoms_maxdiff": f"{np.abs(np.subtract(g['atoms'], f['atoms'])).max():.1e}" if g else ""})
with open(OUT / "11_ccs_agree_share_cells.csv", "w", newline="", encoding="utf-8") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0]))
    wr.writeheader()
    wr.writerows(rows)

say("## Fit by fit (11_ccs_agree_share_cells.csv has every fit)")
for var in VARIANTS:
    R = [r for r in rows if r["variant"] == var]
    fr = [f for f in fits if f is not None and f["var"] == var]
    amb_share = [r["ambiguous"] / r["N"] for r in R]
    say(f"{var}: {len(R)} fits ({sum(r['fit'] == 'global' for r in R)} global), N from {min(r['N'] for r in R):,} "
        f"to {max(r['N'] for r in R):,} pair-samples")
    say(f"   samples of the two patterns {sum(r['pattern'] for r in R):,} of {sum(r['N'] for r in R):,} "
        f"({sum(r['pattern'] for r in R) / sum(r['N'] for r in R):.4%}); ambiguous {sum(r['ambiguous'] for r in R):,} "
        f"({sum(r['ambiguous'] for r in R) / sum(r['N'] for r in R):.4%}; per fit at most {max(amb_share):.4%}), of "
        f"which kept here {sum(r['k_amb'] for r in R):,}; exactly zero D {sum(r['exact_zero'] for r in R):,}")
    say(f"   largest |D| on the two patterns {max(f['max_absD_pattern'] for f in fr):.2e}; smallest |D| elsewhere "
        f"{min(f['min_absD_off'] for f in fr):.2e}; samples of the patterns with |D| >= 1e-12: "
        f"{sum(r['pattern_not_small'] for r in R)}; other samples with |D| < 1e-12: {sum(r['off_small'] for r in R)}")
    say(f"   D summed in reverse order: decisions changed {sum(r['rev_changed'] for r in R):,} (at ambiguous "
        f"samples {sum(r['rev_changed'] - r['rev_changed_outside'] for r in R):,}, elsewhere "
        f"{sum(r['rev_changed_outside'] for r in R)}), in {sum(r['rev_changed'] > 0 for r in R)} fits")
    ne = [r for r in R if not r["share_equals_regenerated"]]
    say(f"   recomputed shares and atoms equal to the regenerated arrays: {len(R) - len(ne)} of {len(R)} fits")
    dk = [r for r in R if r["dk_committed"] != 0]
    say(f"   committed against this process: fits whose count differs {len(dk)} of {len(R)}; largest |k_c - k| "
        f"{max((abs(r['dk_committed']) for r in R), default=0)}; committed count outside its bracket in "
        f"{sum(not r['committed_in_bracket'] for r in R)} fits")
    if dk:
        say(f"   median |k_c - k| over those fits {float(np.median([abs(r['dk_committed']) for r in dk])):g}; largest "
            f"|k_c - k| / ambiguous samples {max(abs(r['dk_committed']) / r['ambiguous'] for r in dk):.3f}")
        r = max(dk, key=lambda r: abs(float(r["share_committed"]) - float(r["share"])))
        say(f"   the largest difference: subject {r['subject']} {r['run']} {r['fit']}: committed "
            f"{float(r['share_committed']):.6f}, here {float(r['share']):.6f} (difference "
            f"{float(r['share_committed']) - float(r['share']):+.3g}); k_c - k = {r['dk_committed']:+d} of N = "
            f"{r['N']:,}; ambiguous samples {r['ambiguous']:,}, of which kept here {r['k_amb']:,}")
    if child:
        cd = [r for r in R if r["child_dk"] != 0]
        gs = [child["fits"][i]["share"] - f["share"] for i, f in enumerate(fits) if f is not None and f["var"] == var]
        say(f"   child process: local MIs changed in {sum(bool(r['child_mi_changed']) for r in R)} of {len(R)} fits; "
            f"masks identical (four signs, patterns, decisions at non-ambiguous samples) in "
            f"{sum(bool(r['child_masks_identical']) for r in R)} of {len(R)}; counts differ in {len(cd)} fits, "
            f"largest |dk| {max((abs(r['child_dk']) for r in R), default=0)}, largest share difference "
            f"{max(abs(x) for x in gs):.3g}; largest atom difference "
            f"{max(float(r['child_atoms_maxdiff']) for r in R):.1e}")
say("")

say("## Predictions")
verdict = {
    "(1) the regenerated arrays reproduce exactly on this machine": p1,
    "(2) |D| < 1e-12 exactly at the samples of the two patterns": p2,
    "(3) reordering D changes decisions at ambiguous samples only": p3,
    "(4) other kernels: identical masks, counts differing only at ambiguous samples": p4 if child else None,
    "(5) every committed count an integer within its bracket": p5,
    "(6) the two arrays byte-identical to the regeneration of 16 September": stash_same,
}
verdict = {k: (None if v is None else bool(v)) for k, v in verdict.items()}
for k, v in verdict.items():
    say(f"{'holds    ' if v else ('NOT TESTED' if v is None else 'FAILS    ')} {k}")
say(f"fits: {n_fit} computed, {n_skip} skipped as by the run")
bad = [k for k, v in verdict.items() if v is False]
say("VERDICT: " + ("every prediction tested holds" if not bad else "FAILS: " + "; ".join(bad)))
say(f"finished {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
(OUT / "11_ccs_agree_share_check.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")
tgz = OUT.parent / (OUT.name + ".tar.gz")
with tarfile.open(tgz, "w:gz") as t:
    t.add(OUT, arcname=OUT.name)
print(f"packed {tgz} ({tgz.stat().st_size:,} bytes)")
