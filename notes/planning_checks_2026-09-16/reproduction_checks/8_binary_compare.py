"""8_binary_compare.py — compare every tracked binary output (.npy, .npz, .pkl) that a run modified against its
committed version at a reference commit.

Usage (from the repository root, pinned environment):
    .venv/bin/python notes/planning_checks_2026-09-16/reproduction_checks/8_binary_compare.py <reference commit>

For each modified tracked binary under notes/review_results/ and results/: the committed bytes are read with
`git show <ref>:<path>`, both versions are loaded, and the largest absolute difference over all numeric entries is
printed (NaN patterns must agree). Pickles are compared structurally: DataFrames column by column (numeric columns
by largest absolute difference, other columns by equality), dicts key by key, lists and tuples element by element,
arrays and floats numerically, and every other value (strings, integers, booleans, None) by equality. Nothing is
written or changed. Companion of 6_committed_compare.py, which covers the .md, .csv and .txt outputs.

Revised 25 Sep 2026 (the error-only check of that day): the inference-row pickles are lists of dicts, which the
first version compared by their pickled bytes, so that a difference of 1e-13 in any float would have been
reported as REAL; they are now compared element by element under the same 1e-9 rule as every other output.
"""
import io
import pickle
import subprocess
import sys

import numpy as np

REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
ROOTS = ("notes/review_results/", "results/")
EXTS = (".npy", ".npz", ".pkl")


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True).stdout


def modified_binaries():
    out = git("status", "--porcelain", "--", *ROOTS).decode()
    files = []
    for line in out.splitlines():
        code, path = line[:2], line[3:].strip()
        if code.strip() in ("M", "MM", "AM") and path.endswith(EXTS):
            files.append(path)
    return sorted(files)


def load(path, data):
    if path.endswith(".npy"):
        return {"": np.load(io.BytesIO(data), allow_pickle=False)}
    if path.endswith(".npz"):
        z = np.load(io.BytesIO(data), allow_pickle=False)
        return {k: z[k] for k in z.files}
    obj = pickle.loads(data)
    return {"": obj}


def compare_arrays(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    if a.shape != b.shape:
        return f"SHAPE {a.shape} vs {b.shape}"
    if a.dtype.kind in "fc" and b.dtype.kind in "fc":
        na, nb = np.isnan(a), np.isnan(b)
        if not np.array_equal(na, nb):
            return "NAN PATTERN DIFFERS"
        d = np.abs(a[~na] - b[~nb])
        return f"max|diff| = {d.max() if d.size else 0.0:.3g}"
    return "identical" if np.array_equal(a, b) else "DIFFERS (non-float)"


def compare_frames(a, b):
    import pandas as pd
    if not isinstance(a, pd.DataFrame) or not isinstance(b, pd.DataFrame):
        return "DIFFERS (DataFrame against another type)"
    if list(a.columns) != list(b.columns) or a.shape != b.shape:
        return f"SHAPE/COLUMNS {a.shape} vs {b.shape}"
    worst = 0.0
    for col in a.columns:
        if pd.api.types.is_numeric_dtype(a[col]) and pd.api.types.is_numeric_dtype(b[col]):
            x, y = a[col].to_numpy(float), b[col].to_numpy(float)
            if not np.array_equal(np.isnan(x), np.isnan(y)):
                return f"NAN PATTERN DIFFERS in column {col}"
            m = np.nanmax(np.abs(x - y)) if len(x) else 0.0
            worst = max(worst, float(m))
        elif not a[col].astype(str).equals(b[col].astype(str)):
            return f"DIFFERS in non-numeric column {col}"
    return f"max|diff| = {worst:.3g} over numeric columns"


def compare_obj(a, b, where="obj"):
    """Structural comparison of two unpickled objects. Returns (largest numeric difference, list of problems)."""
    import pandas as pd
    if isinstance(a, pd.DataFrame) or isinstance(b, pd.DataFrame):
        r = compare_frames(a, b)
        return (float(r.split("=")[1].split()[0]), []) if r.startswith("max|diff|") else (0.0, [f"{where}: {r}"])
    if isinstance(a, dict) or isinstance(b, dict):
        if not (isinstance(a, dict) and isinstance(b, dict)) or list(a) != list(b):
            return 0.0, [f"{where}: keys or types differ"]
        worst, probs = 0.0, []
        for k in a:
            w, p = compare_obj(a[k], b[k], f"{where}[{k!r}]")
            worst, probs = max(worst, w), probs + p
        return worst, probs
    if isinstance(a, (list, tuple)) or isinstance(b, (list, tuple)):
        if type(a) is not type(b) or len(a) != len(b):
            return 0.0, [f"{where}: {type(a).__name__} of {len(a) if hasattr(a, '__len__') else '?'} against "
                         f"{type(b).__name__} of {len(b) if hasattr(b, '__len__') else '?'}"]
        worst, probs = 0.0, []
        for i, (x, y) in enumerate(zip(a, b)):
            w, p = compare_obj(x, y, f"{where}[{i}]")
            worst, probs = max(worst, w), probs + p
        return worst, probs
    if isinstance(a, (np.ndarray, float, np.floating)) or isinstance(b, (np.ndarray, float, np.floating)):
        r = compare_arrays(a, b)
        if r.startswith("max|diff|"):
            return float(r.split("=")[1].split()[0]), []
        return 0.0, ([] if r == "identical" else [f"{where}: {r}"])
    same = type(a) is type(b) and bool(a == b)
    return 0.0, ([] if same else [f"{where}: {a!r} against {b!r}"])


def main():
    files = modified_binaries()
    print(f"binary outputs modified by the run under {ROOTS}: {len(files)} (compared against {REF})")
    tally = {"identical": 0, "noise (<1e-9)": 0, "REAL": 0}
    for path in files:
        old = git("show", f"{REF}:{path}")
        new = open(path, "rb").read()
        if old == new:
            print(f"  identical bytes            {path}")
            tally["identical"] += 1
            continue
        try:
            A, B = load(path, old), load(path, new)
        except Exception as e:  # noqa: BLE001 — report and continue; nothing is written
            print(f"  COULD NOT LOAD             {path}   {type(e).__name__}: {e}")
            tally["REAL"] += 1
            continue
        parts = []
        worst = 0.0
        flag = False
        for key in sorted(set(A) | set(B)):
            if key not in A or key not in B:
                parts.append(f"{key}: MISSING"); flag = True; continue
            if path.endswith(".pkl"):
                w, probs = compare_obj(A[key], B[key])
                worst = max(worst, w)
                if probs:
                    flag = True
                    parts.append(f"{len(probs)} non-numeric difference(s), the first {probs[0]}")
                else:
                    parts.append(f"max|diff| = {w:.3g} over every numeric entry")
                continue
            r = compare_arrays(A[key], B[key])
            parts.append((key + ": " if key else "") + r)
            if r.startswith("max|diff|"):
                worst = max(worst, float(r.split("=")[1].split()[0]))
            elif r != "identical":
                flag = True
        verdict = "REAL" if flag or worst >= 1e-9 else ("identical" if worst == 0 else "noise (<1e-9)")
        tally[verdict] += 1
        print(f"  {verdict:<26} {path}   {'; '.join(parts)}")
    print("summary:", tally)


if __name__ == "__main__":
    main()
