"""8_binary_compare.py — compare every tracked binary output (.npy, .npz, .pkl) that the section-6
verification run modified against its committed version at a reference commit.

Usage (from the repository root, pinned environment):
    .venv/bin/python notes/planning_checks_2026-09-16/reproduction_checks/8_binary_compare.py d507728

For each modified tracked binary under notes/review_results/ and results/: the committed bytes are read
with `git show <ref>:<path>`, both versions are loaded, and the largest absolute difference over all
numeric entries is printed (NaN patterns must agree). DataFrames (.pkl) are compared column by column:
numeric columns by largest absolute difference, other columns by equality. Nothing is written or changed.
Companion of 6_committed_compare.py, which covers the .md, .csv and .txt outputs.
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
        return "identical" if pickle.dumps(a) == pickle.dumps(b) else "DIFFERS (non-DataFrame pickle)"
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
            r = compare_frames(A[key], B[key]) if path.endswith(".pkl") else compare_arrays(A[key], B[key])
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
