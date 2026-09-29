# Audit of the software-readiness files (treeA_v1), 28 Sep 2026

Scope: `tools/ar1_diagnostic.py`, `tests/conftest.py`, `tests/test_closed_form.py`, `tests/test_ar1_diagnostic.py`,
`.github/workflows/tests.yml`, `LICENSE`, `LICENSE-CC-BY-4.0.md`, `CITATION.cff`, the new README.md sections (badge,
layout rows, "### Tests", "## Checking your own synergy values", the licence paragraph) and the new sentences of the
Data and code availability paragraph of `manuscript/draft_v2.md` (line 246).

Environment: `SP/v312` (CPython 3.12.3, numpy 2.5.3, scipy 1.18.1, pytest 9.1.1, phyid editable at 6c5f2e9), x86-64,
the same manylinux numpy wheel CI would install. A copy of the tree is in `SP/b32/audit/scratch_ci/tree`, a simulated CI
workspace in `SP/b32/audit/scratch_ci/ci_sim` (fresh venv, exact workflow commands), check scripts in
`SP/b32/audit/scratch_ci/checks/`, and a patched copy that tests the proposed code corrections in
`SP/b32/audit/scratch_ci/fixcheck/`.

Headline: the tool computes phyid's Gaussian-MMI window means correctly. Its maximum difference from phyid is 7e-14,
across single fits, windows, pairs and τ = 1–3, and from `notes/rev_phiid_fast.py` it is 8e-15. The AR(1)-substituted
estimate matches partB4's lines to 3e-15. The tests (104 passed), the doctest and the B25 self-test all pass. The
workflow is valid and runs, apart from the OSF download, which cannot be reached from here. The errors are in the
tool's handling of inputs outside the AR(1) family and of too-short samples, in the fragility of some tests and the
doctest, and in the licence scope and its consistency with the manuscript.

---

## Findings (most serious first)

### 1. [High] The tool raises for a whole call when one pair's AR(1)-substituted matrix is not positive definite; the paper's code silently returns a meaningless value there

**Where:** `tools/ar1_diagnostic.py:104-110` (`logdet` raises); `:120-143` (`atoms_from_corr`), `:146-150` (`ar1_corr`
docstring), `:195-244` (`diagnose`, `diagnose_windows`, `diagnose_pairs`); `tools/ar1_diagnostic.py:2` and
`README.md:69` ("for any pair of time series"); `manuscript/draft_v2.md:246` ("applies that estimate to any pair of time
series").

**What is wrong:** `ar1_corr(a_x, a_y, q)` is a correlation matrix only if (1 − a_x²)(1 − a_y²) > q²(1 − a_x a_y)².
That condition says the innovation covariance of the AR(1) pair is positive definite. Measured (a_x, a_y, q) from real
or simulated series often violate it: high |q| together with unequal autocorrelations is enough, as when two regions
share one slow signal under different noise. In that case `_mutual_informations` raises
`ValueError("a correlation matrix is not positive definite")`, and it does so for the whole stack. One such window makes
`diagnose_windows` fail for every window, and one such pair makes `diagnose_pairs` fail for every pair.

The paper's own code handles the same matrix differently. `notes/rev_phiid_fast.py:97-98` takes `slogdet` and ignores
the sign, and `notes/partB4_diagnostic.py:75` averages the result into the window means with no check. So the claim that
the tool reproduces "the code behind the paper's numbers" (tool docstring, lines 21-22) holds only on positive-definite
matrices. Nothing records whether any of the data's pair-windows are affected.

**Evidence:**

- Stable random VAR(1) (`checks/indep1.py`, `checks/nonpd2.py`; seed 12345, trial 6, n = 840, W = 60). Windows 4 and 5
  of pair (0, 1) measure (a_x, a_y, q) = (0.9850, 0.9597, −0.8935) and (0.9792, 0.9194, −0.8437). The observed matrices
  are positive definite (minimum eigenvalue +0.0059 and +0.0070). The substituted matrices are not (−0.00016 and
  −0.0018).
  - `diagnose()` on either window, and `diagnose_windows()` on the whole series, raise.
  - `rev_phiid_fast` returns sts_ar1 = 3.0788 and 1.6498, against observed sts of 0.4347 and 0.1978.
- A pair sharing one slow signal (`checks/nonpd_shared.py`): s is AR(1) with φ = 0.98, x = s + noise of variance 0.02,
  y = s + noise of variance 0.30.
  - Population (a_x, a_y, q) = (0.9608, 0.7538, 0.8684). The condition fails: (1 − a_x²)(1 − a_y²) = 0.0332 against
    q²(1 − a_x a_y)² = 0.0573, and the minimum eigenvalue of `ar1_corr` is −0.025.
  - On 840 samples, `diagnose`, `diagnose_windows(…, 60)` and `diagnose_pairs` (five rows including x and y) all raise.
  - partB4's lines (via `rev_phiid_fast`) give sts_ar1 = −0.2758 against observed 0.0011.
  - With the correction below, 7 of the 14 windows at W = 60 come back NaN.
- Plausibility on the paper's own data:
  - Subject 1's saved pre-injection pair-windows reach |q| = 0.986
    (`notes/review_results/partB/scope_map_overlay_points.npz`, `pre_w1to4_q`).
  - 6.5-10.2 % of pairs have |q| > 0.6 in DMT windows 1-3 (`scope_map_overlay.csv`).
  - At |q| = 0.986 an asymmetry |a_x − a_y| above 0.047 already breaks the condition at mean a = 0.85 (0.032 at
    mean a = 0.90). The window-level scatter of one member's a is 0.03 (`exchange_rates_tables.md`).
- The repository's own test `test_against_phyid[60]` would raise for this reason in 8/4,000 fresh draws of
  (0.8, 0.9, −0.4) and 19/4,000 of (0.6, 0.9, 0.3), about 0.7 % per fresh random state (`checks/spurious.py`). It
  passes now only because the seed and the test order are fixed (see finding 10).
- `notes/partB23_diagnostic_alternatives.py` (lines 11, 128-135) already excludes such matrices and reports their share,
  so the repository has precedent for the NaN treatment.

**Proposed correction** (verified in `fixcheck/`: tests 104 passed, doctest passes, the equivalence with phyid and
`rev_phiid_fast` is unchanged):

```python
# tools/ar1_diagnostic.py, in _mutual_informations.logdet (replace lines 107-110)
        sign, val = np.linalg.slogdet(sub)
        return np.where(sign > 0, val, np.nan)          # NaN where a block is not positive definite
# tools/ar1_diagnostic.py, end of atoms_from_corr (replace lines 142-143)
    A = K @ _SOLVE
    A[np.isnan(K).any(axis=1)] = np.nan                  # a matrix that is not positive definite has no atoms
    return A[0] if single else A
```

Add to the `ar1_corr` docstring: "It is a correlation matrix only if |q| < 1 and (1 − a_x²)(1 − a_y²) > q²(1 − a_x a_y)²;
otherwise no pair of AR(1) processes has these a_x, a_y and q, and atoms_from_corr returns NaN."

Add to the `diagnose` docstring: "sts_ar1, residual and atoms_ar1 are NaN where the pair's measured (a_x, a_y, q) are
those of no AR(1) pair (a high |q| with unequal autocorrelations, e.g. two regions sharing a slow signal under different
noise); average with np.nanmean and report the share."

After README.md:131 add: "Where a pair's measured a_x, a_y and q are those of no AR(1) pair, (1 − a_x²)(1 − a_y²) ≤
q²(1 − a_x a_y)², the substituted estimate does not exist and is returned as NaN; report the share of such pairs."

In draft_v2.md:246, change "applies that estimate to any pair of time series (usage in `README.md`)" to "applies that
estimate to any pair of time series (usage in `README.md`; NaN where the pair's measured a_x, a_y and q are those of no
AR(1) pair)".

Add the test `test_unrealisable_substitution_gives_nan` (`fixcheck/tests/test_proposed.py`, verified). For the paper,
count such pair-windows on the data by adding to partB4's loop
`n_bad += int((np.linalg.eigvalsh(ar1_corr(ax, ay, q)).min(1) <= 0).sum())`. If the count is not zero, Table 1 and
Figs 2 and 5 average values that exist only as log|det| artefacts; recompute them without those values and state the
share. This cannot be checked here because the data are not available.

### 2. [High] Too-short inputs pass the guard and can return finite nonsense; `diagnose_pairs` has no input check at all

**Where:** `tools/ar1_diagnostic.py:97-98` (`lag_corr`: "leave at least three lag pairs"); `:225-231` (`diagnose_pairs`,
no validation).

**What is wrong:** a 4 × 4 sample correlation matrix has rank at most m − 1, where m is the number of lag pairs. It is
therefore singular unless m ≥ 5, but the guard accepts m = 3 and m = 4. Rounding then sometimes gives `slogdet` a
positive sign, and the tool returns finite garbage instead of an error.

**Evidence** (`checks/short.py`, 2,000 random draws each):

- 4 samples (3 lag pairs): 21 finite results from a rank-2 matrix.
- 5 samples (4 lag pairs): 498 finite results, for example sts = 15.41 nats from a rank-3 matrix (slogdet sign +1,
  log det −36.8).
- The other draws raise the misleading "not positive definite".
- phyid refuses the same 5-sample input (`LinAlgError`). The paper's estimator skips such windows:
  `scripts/01_synergy_timecourse.py:371`, `if in_w.size <= TAU + 4: # cannot fit a 4x4 covariance`, and
  `notes/partB4_diagnostic.py:69`.
- `diagnose_pairs(X)` with T − τ = 4 gives the same nonsense. With `tau=0` it fails with a cryptic `matmul`
  core-dimension error, and with `tau=-1` it silently returns NaN (`checks/edge.py`).

**Proposed correction** (verified: 4- and 5-sample inputs now raise, 6-sample inputs are unchanged):

```python
# tools/ar1_diagnostic.py:97-98
    if not (tau >= 1 and x.size - tau >= 5):
        raise ValueError("tau must be at least 1 and leave at least five lag pairs (a 4 × 4 correlation needs five)")
# tools/ar1_diagnostic.py, after line 228 in diagnose_pairs
    if X.ndim != 2 or not (tau >= 1 and X.shape[1] - tau >= 5):
        raise ValueError("X must be (regions × samples) with at least tau + 5 samples, tau at least 1")
```

### 3. [Medium] CC BY 4.0 is granted on `manuscript/` while the manuscript says "not for citation or distribution"

**Where:** `LICENSE-CC-BY-4.0.md:5-8`; `README.md:72` and `:171-172`; the fifth sentence of the Data and code
availability paragraph (draft_v2.md:246), against its first sentence, "Manuscript for co-author review; not for citation
or distribution."

**What is wrong:** CC BY 4.0 grants anyone the right to share and adapt for any purpose, and cannot be withdrawn for
copies already obtained. The draft carrying that licence says it is not to be distributed.

**Evidence:**

- The repository is public: `git ls-remote https://github.com/Vasilis540/dmt-phiid` answers without credentials (HEAD
  d108d66 on `master`), and draft_v2.md:246 itself says "The repository's full history is public".
- The record's layout note (analysis_record.md, around line 6791) says the co-author-review line "stays until the
  co-author review".
- The draft names co-authors marked [TK] who have not yet reviewed it.

**Proposed correction:** decide before pushing. Either:

- (a) In draft_v2.md:246, replace "Manuscript for co-author review; not for citation or distribution." with
  "Manuscript for co-author review." The licence then governs.
- (b) Keep the line and hold the manuscript out of the licence until the review. Change LICENSE-CC-BY-4.0.md:5 from
  "The text (`manuscript/`, the Markdown files under `notes/`, `README.md`)" to "The text (the Markdown files under
  `notes/`, `README.md`; the files under `manuscript/` once the co-author review is complete, and until then they are
  not licensed for redistribution)". Make README.md:72 and :171-172 and the fifth sentence of draft_v2.md:246 match.

### 4. [Medium] The licence scope omits a third-party file and 53 of the repository's own files

**Where:** `LICENSE-CC-BY-4.0.md:5-15`; `README.md:52-75` (no row for `data/`).

**What is wrong, with evidence:**

- (a) `data/Schaefer2018_100Parcels_7Networks_order.lut` is byte-identical to CBIG's file. I checked it with `cmp`
  against a sparse clone of github.com/ThomasYeoLab/CBIG,
  `stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/MNI/fsleyes_lut/`, and
  analysis_record.md:2074-2077 records that it was downloaded from there.
  - CBIG's `LICENSE.md` is MIT, "Copyright (c) 2016 Computational Brain Imaging Group (CBIG)", which requires the
    notice in all copies.
  - The repository ships the file without that notice, and the licence file does not list it among third-party
    material. Its catch-all, "the files of third parties that the result files cite", does not cover a file that is
    shipped in the repository and read by scripts.
- (b) 54 files fall under neither licence as written. One is the CBIG file above. The other 53 are:
  - `.github/workflows/tests.yml`, `.gitignore`, `CITATION.cff`, `CLAUDE.md`, `requirements.lock.txt`;
  - 48 files under `notes/` outside `notes/review_results/` that are neither `.py`/`.sh` nor `.md`. These are check
    logs and outputs, for example `notes/review_2026-09-28/checks/*.out`, `notes/review_2026-09-28/proposals.json`,
    `crosscheck_claims.csv`, `notes/planning_checks_2026-09-16/**/*.log` and
    `notes/review_2026-09-2x/revision/*.json`.

**Proposed correction:** replace LICENSE-CC-BY-4.0.md lines 5-15 with:

> Everything in this repository that is neither code nor third-party material (the text, including `manuscript/`,
> `README.md`, `CLAUDE.md`, `CITATION.cff` and the non-code files under `notes/`; the figures; and the result files
> under `results/` and `notes/review_results/`) is licensed under the Creative Commons Attribution 4.0 International
> licence (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/ (legal code:
> https://creativecommons.org/licenses/by/4.0/legalcode). You may share and adapt them for any purpose, provided you
> give appropriate credit, link to the licence and indicate if changes were made.
>
> The code (the `.py` and `.sh` files and `.github/workflows/tests.yml`) is licensed under the MIT licence in `LICENSE`.
>
> Not covered by either licence: the data of Singleton et al. (2025) and Timmermann et al. (2023), which this repository
> does not include or redistribute (`README.md`, "Data source, citation and licence"); the files of third parties that
> the result files cite; and `data/Schaefer2018_100Parcels_7Networks_order.lut`, copied unchanged from the CBIG
> repository (https://github.com/ThomasYeoLab/CBIG,
> `stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/MNI/fsleyes_lut/`) and distributed under
> CBIG's MIT licence, whose notice is in `data/LICENSE-CBIG.md`.

Create `data/LICENSE-CBIG.md` with the full text of CBIG's LICENSE.md. Add a README layout row:
"| `data/Schaefer2018_100Parcels_7Networks_order.lut` | parcel names of the Schaefer-100 7-network parcellation, from
CBIG (MIT; `data/LICENSE-CBIG.md`) |". If option (b) of finding 3 is chosen, keep its exclusion of `manuscript/`.

### 5. [Medium-low] The doctest's expected output holds only for its particular random stream, and it is the only non-derived seed in the code

**Where:** `tools/ar1_diagnostic.py:38` (`default_rng(0)`) and `:46-47` (`(1.26, 1.26, 1.2588)`); against
draft_v2.md:246 ("Seed 20261120 throughout.") and README.md:98-99 ("All scripts use seed 20261120.").

**Evidence** (`checks/` scripts; `scratch_ci/doctest_vals.py`):

- Seed 0 gives sts = 1.2574 and sts_ar1 = 1.2589, only 0.0024 and 0.0039 above the rounding boundary 1.255.
- Over seeds 1-40 the same code gives sts with mean 1.2542 and SD 0.0064, and prints something other than
  (1.26, 1.26) for 24 of the 40 seeds.
- With the repository's seed 20261120 it prints (1.25, 1.25).
- The finite-sample value lies below the closed form because MMI takes the smaller of two noisy self-informations; the
  mean error is −0.006 at n = 200,000.
- The doctest passes in CI (pinned numpy 2.5.3 and the same x86-64 wheel). A different numpy or LAPACK changes the
  stream (Generator streams carry no cross-version guarantee, and `multivariate_normal` depends on SVD sign
  conventions) and then flips the output in about 60 % of cases. The example also suggests the observed sts equals
  1.2588 to two decimals, which is not typical.

**Proposed correction** (verified to pass). Replace lines 38-39 and 46-47 with:

```
>>> rng = np.random.default_rng(20261120)
>>> # two AR(1) processes with a = 0.85 whose innovations are correlated at lag 0 (q = 0.25)
...
>>> round(closed_form(0.85, 0.25)["sts"], 4)
1.2588
>>> abs(d["sts"] - 1.2588) < 0.03, abs(d["residual"]) < 0.01
(True, True)
```

### 6. [Low] `diagnose_windows` accepts x and y of different lengths without error

**Where:** `tools/ar1_diagnostic.py:214-219`.

**Evidence:** `diagnose_windows(x[:150], y[:120], 60)` and `diagnose_windows(x[:120], y[:150], 60)` both return two
windows and silently ignore the longer series' extra samples, while `diagnose` raises for the same inputs. The CLI with
files of 100 and 840 lines and `--window 50` silently analyses the first 100 values of y.

**Proposed correction** (verified). After line 215 add:

```python
    if x.shape != y.shape or x.ndim != 1:
        raise ValueError("x and y must be 1-D arrays of the same length")
```

### 7. [Low] NaN and constant inputs are undocumented and handled inconsistently

**Where:** module docstring, `tools/ar1_diagnostic.py:1-33`.

**Evidence** (`checks/edge.py`):

- One NaN gives all-NaN atoms for that fit, window or every pair containing the row, with only a RuntimeWarning.
- A constant zero series gives NaN. A constant 0.1 or 0.3 series raises "not positive definite", because its mean is
  not exact.
- phyid raises for both cases.
- The paper's estimator drops non-finite TRs before windowing (`scripts/01_synergy_timecourse.py:309-326` and
  `:368-372`; subject 2's placebo TR 839 is all-NaN). `diagnose_windows` instead returns NaN for that window.

**Proposed correction:** after line 32 add: "Inputs must be finite and not constant: a NaN or a constant series gives NaN
atoms. The paper's estimator drops non-finite samples before forming windows (scripts/01_synergy_timecourse.py), so drop
or impute them first." With the correction of finding 1, constant series give NaN in every case.

### 8. [Low] Tests can pass vacuously: in-repository and pinned dependencies are imported with `importorskip`

**Where:** `tests/test_ar1_diagnostic.py:33` (`pytest.importorskip("rev_phiid_fast")`) and `:44`
(`pytest.importorskip("phyid.calculate")`).

**What is wrong:** if `notes/` is moved or renamed, or `conftest.py` stops adding it to the path, the comparison with the
paper's second implementation is silently skipped and CI stays green. The same happens with phyid, although the README
promises the phyid check and phyid is part of `requirements.lock.txt` and the CI install.

**Proposed correction:** at module top, `import rev_phiid_fast as rev` and `from phyid import calculate as phyid_calc`
(with `from phyid.utils import PhiID_atoms_abbr`). Delete lines 33 and 44 and use these names.

### 9. [Low] `test_substitution_matches_the_paper` is largely tautological

**Where:** `tests/test_ar1_diagnostic.py:54-64`.

**What is wrong:** it recomputes `sts_ar1` with the same `ar1_corr` and `atoms_from_corr` that `diagnose` uses, and
checks `residual = sts − sts_ar1`, which is the definition. It never exercises partB4's code path, the paper's code, as
its comment implies. Only the placement check (M[0,3] = a_y q, M[1,2] = a_x q) is informative.

**Proposed correction** (verified to pass): replace the body with partB4's lines 71-75 run through `rev_phiid_fast`:

```python
def test_substitution_matches_partB4():
    rng = np.random.default_rng([20261120, 3])
    X = np.stack(ar1_pair(300, 0.85, 0.8, 0.3, rng) + ar1_pair(300, 0.9, 0.7, -0.3, rng))
    pairs, d = diagnose_pairs(X)
    pp = rev.PairPhiID(X)                                     # notes/partB4_diagnostic.py, l. 71-75
    ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]
    q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
    p = rev.atoms_from_corr(rev.ar1_corr(ax, ay, q))[:, rev.ATOMS.index("sts")]
    assert pairs == [tuple(t) for t in pp.pairs]
    assert np.max(np.abs(d["sts_ar1"] - p)) < 1e-12
```

Keep the two placement asserts.

### 10. [Low] Test data depend on test order through a shared module-level generator

**Where:** `tests/test_ar1_diagnostic.py:8` (`RNG = np.random.default_rng(20261120)`, shared by five tests).

**What is wrong:** `-k` selection, a skip (finding 8), `pytest-randomly` or `pytest-xdist` changes every later test's
data. With a fresh stream, `test_against_phyid[60]` fails in about 0.7 % of cases for the reason in finding 1.

**Proposed correction:** give each test its own generator, `rng = np.random.default_rng([20261120, k])` with k = 1…5,
and pass it to `ar1_pair` and `random_corr`. Remove line 8.

### 11. [Low] The sign-change check does not pin the paper's "0.008"

**Where:** `tests/test_closed_form.py:58-60` (`excess(0.006) > 0 > excess(0.008)`).

**Evidence:** the exact crossing is at 0.00762 (brentq). The paper's 0.008 (draft_v2.md:51) is B23 (f)'s first negative
point on a 0.0005 grid (`diagnostic_alternatives_tables.md`, row (0.85, 0.25): 0.0080). The test's bracket would also
accept a crossing at 0.0061, which would make the paper's figure wrong.

**Proposed correction** (verified): `assert excess(0.0075) > 0 > excess(0.008)`, with the comment "(B23 (f): first
negative at 0.0080 on a 0.0005 grid; the crossing is at 0.0076)".

### 12. [Low] The manuscript says `tests/` checks the closed form against phyid and `rev_phiid_fast`; it does not

**Where:** draft_v2.md:246, "and `tests/` checks it and the closed form against phyid and `notes/rev_phiid_fast.py`".

**Evidence:** `tests/test_closed_form.py` compares `closed_form()` with the tool's own lattice solve
(`atoms_from_corr(ar1_corr(a, a, q))`), not with phyid or `rev_phiid_fast`. Only the tool is compared with those two
(`tests/test_ar1_diagnostic.py`). The README wording ("tests of the closed form and of the tool against …") parses
correctly.

**Proposed correction:** "and `tests/` checks it against phyid and `notes/rev_phiid_fast.py` and the closed form against
its lattice solve;".

### 13. [Low] "Two AR(1) processes correlated only at lag 0" is literally false

**Where:** `README.md:140`; `tools/ar1_diagnostic.py:13` and `:39`. The same shorthand is in draft_v2.md:15, :55 and
:164.

**Evidence:** on the family, corr(x_t, y_{t+1}) = aq (draft_v2.md:39 states it), which is 0.2125 at the operating point.
The processes are correlated at every lag; what is lag-0-only is the innovations' correlation, that is, there is no
lagged interaction.

**Proposed correction:** README.md:140 comment: "1.2588 nats: two AR(1) processes with no lagged interaction
(innovations correlated at lag 0)". Tool line 13: "…of two AR(1) processes with equal coefficients and no lagged
interaction". Line 39 as in finding 5. Apply the same change to the paper, or leave the shorthand everywhere
consistently.

---

## Observations (not errors in the files as they stand)

- **O1. CI durability and external dependencies.** The workflow runs the phyid clone from GitHub, installs phyid's newest
  build backend through build isolation, and downloads phyid's reference file from OSF.
  - Simulated with the latest setuptools 84.0.0 and versioneer 0.29, phyid builds but warns:
    - "File … README.md cannot be found";
    - "`project.license` as a TOML table is deprecated … By 2027-Feb-18, you need to update your project";
    - "License classifiers are deprecated".
    A later setuptools may stop building phyid. To pin it, use
    `python -m pip install setuptools==84.0.0 "versioneer[toml]==0.29"` followed by
    `python -m pip install --no-build-isolation -e ./phyid-src`.
  - phyid's `test_calculate.py` (four tests) could not be run here because OSF is blocked, so its pass with
    numpy 2.5.3 and scipy 1.18.1 is unverified. Its discrete-CCS case involves sign tests that the paper itself notes
    can be settled by rounding.
  - An OSF or GitHub outage turns the badge red. A separate job, or `continue-on-error: true` on the last step, would
    isolate that.
- **O2.** `actions/checkout@v4` and `actions/setup-python@v5` still resolve; v7 of both exists.
- **O3. `CITATION.cff`** is valid (`cffconvert --validate`: "valid according to schema version 1.2.0"). It has no
  `date-released` or `version`, so "Cite this repository" prints no year. `license: MIT` describes the code only. CFF
  treats a list of licences as alternatives, so leaving MIT is defensible; the message could mention CC BY 4.0 for the
  results.
- **O4. "The release carries no licence of its own" (draft_v2.md:246).** For the GitHub repository this is true: at
  77af7aa its only licence files are `fxns/brewermap/LICENSE.TXT` (Apache-2.0), `fxns/spiderplot/LICENSE.txt` and
  `fxns/violin/license.txt` (BSD), all plotting functions. The README states no licence or data-use terms; I checked
  with a blob-less clone, so no data were fetched. The Zenodo record 10.5281/zenodo.15177511 could not be checked
  because zenodo.org is blocked (403). Zenodo records carry a licence field, so check it before calling "the release"
  unlicensed.
- **O5. Side note, outside scope.** `SP/b32/work32A/expected_sha256_32A.txt` lists sha256 2cb6dab… for
  `manuscript/analysis_record.md`, but treeA_v1, `work32A/tree` and `work32A/tree2` all hold 9e0d6c0…. The other 31
  listed files match.
- **O6. Disclosure.** No tracked file of treeA_v1 was changed. Python rewrote two git-ignored bytecode caches when a
  check imported from the tree: `tools/__pycache__/ar1_diagnostic.cpython-312.pyc` and
  `notes/__pycache__/rev_phiid_fast.cpython-312.pyc`, at 14:53.

---

## Checked and found correct

**tools/ar1_diagnostic.py**

- The lattice matrix is identical row for row to phyid's `knowns_to_atoms_mat`. The nine MI index sets, the six MMI
  redundancies (ties go to the second argument, as phyid does) and the double redundancy (first minimum of
  [xta, xtb, yta, ytb]) all match. `atoms = K @ inv(M).T` is equivalent to phyid's `solve`.
- The window means equal phyid's `calc_PhiID(kind="gaussian", redundancy="MMI")`:
  - 12 random stable 4-variable VAR(1) systems (n ∈ {60, 120, 300, 840}): max |Δ| 6.6e-14 for `diagnose` over all
    ordered pairs, 4.3e-14 for `diagnose_windows` against phyid on each window, 8.3e-15 for `diagnose_pairs`;
  - τ = 2: 1.5e-14; τ = 3 in windows: 2.0e-15;
  - `diagnose_pairs` at τ = 1, 2, 3 on a 5-region VAR: at most 9.0e-15 against phyid and 1.8e-15 against
    `PairPhiID`.
- The AR(1)-substituted estimate matches the paper's definition: a_x = C[0,2], a_y = C[1,3], q the mean of C[0,1] and
  C[2,3], C[0,3] = a_y q for (x_t, y_{t+1}), C[1,2] = a_x q for (y_t, x_{t+1}), and the matrix is symmetric. It agrees
  with partB4's lines 71-75 (via `PairPhiID`) to 2.7e-15, and a_x, a_y and q agree to 1e-14.
- `diagnose_pairs` builds every 4 × 4 correlation correctly (all 16 entries checked). Its pair order equals
  `itertools.combinations` and `PairPhiID.pairs`.
- `diagnose_windows` uses non-overlapping windows with lag pairs inside the window and drops the trailing incomplete
  window, as scripts/01 (window mode) does.
- `closed_form` and `exchange_rates`: sts(0.85, 0.25) = 1.258831, ∂sts/∂r₁ = 6.0705, ∂sts/∂q = −0.18917. The formulas
  were re-derived and the docstring atoms checked against the lattice solve to 1e-12 on a 48-point grid.
- The CLI with and without `--window`, and with `--tau`, prints 1-based windows. `-h` works.
- "NumPy only" is true (plus the standard-library `argparse`). The module and function docstrings are accurate except
  where findings 1, 2, 5, 7 and 13 say otherwise. Lists and integer arrays are accepted.

**Tests and doctest**

- `SP/v312/bin/python -m pytest -q tests`: 104 passed in 1.4 s. `python -m doctest -v ar1_diagnostic.py` from `tools/`:
  9 passed.
- Every test asserts what its name says, except finding 9. Identities and numbers match Results 1: sts − (xtx + yty) =
  rtr, rtr + sts = 2S, ΦR = rtr, str + stx + sty + sts = S, four mirror atoms ≤ 0, and at q = 0 sts = 2 min(S_x, S_y)
  with rtr = 0.
- 6.07 and −0.19 are checked against finite differences of the lattice solve. The asymmetry rate is 0.0309 per 0.01
  (the one-sided rate at zero asymmetry, as the paper uses it). The actual drop over 0.01 is 0.0303.
- The long-series test has about 4 SD of margin: the error in sts has mean −0.006 and SD 0.006 over 30 runs, against a
  tolerance of 0.03. The residual has max |·| 0.0033 against 0.01.
- The phyid comparison uses a 1e-10 tolerance. Near-ties in the MMI choice cannot fail it, because the two candidates
  then have nearly equal values.
- `conftest.py` path handling works from any working directory. `.pytest_cache/` and `__pycache__/` are git-ignored.
  No stray `test_*.py` exists outside `tests/`.

**Workflow (.github/workflows/tests.yml)**

- The YAML is valid against GitHub's workflow schema (check-jsonschema 0.38.2, `vendor.github-workflows`).
- numpy 2.5.3 and scipy 1.18.1 have `cp312 manylinux_2_27/2_28 x86_64` wheels on PyPI.
- The exact steps were simulated in a fresh Python 3.12 venv in a git-initialised copy with `phyid-src` cloned from
  GitHub and checked out at 6c5f2e9. The git clone lets versioneer work: the version is `0+untagged.8.g6c5f2e9`, since
  phyid has no tags.
  - `pip install -e ./phyid-src` succeeds with setuptools 84.0.0.
  - Repository tests: 104 passed. Doctest: passed.
  - `notes/partB25_binarised.py --selftest`: 53 checks, 0 failed, exit 0, 71 s. It prints the real git SHA with no
    `-dirty` flag, because the untracked `phyid-src/` is outside rev_git's pathspec.
  - `python -m pytest -v --pyargs phyid` from `phyid-src` collects the same 11 items as phyid's own CI: 3 passed,
    4 xfailed, and 4 `test_calculate` errors that come only from the blocked OSF download. phyid has no doctests, so
    dropping `--doctest-modules` loses nothing.
- The working directories are correct.

**Licences and CFF**

- `LICENSE` is the MIT text word for word; it matches the MIT texts shipped by urllib3, PyYAML and pyrsistent. The
  "MIT License" header and "Copyright (c) 2026 Vasilis Sampalis" are present. No CRLF, BOM or tabs in any new file.
- In `LICENSE-CC-BY-4.0.md`, the CC BY 4.0 deed and legal-code URLs and the attribution summary are correct, and the
  data exclusion matches README.md:164-172 and draft_v2.md:246.
- The result files hold statistics, not copies of the source data.
- The README's statement that the source repository's three licence files belong to bundled plotting functions is
  verified (see O4).
- `CITATION.cff` validates. Its keys, types, SPDX licence and repository URL are correct.

**README.md**

- The badge URL has the correct form for `Vasilis540/dmt-phiid` and `tests.yml`; the repository exists, with default
  branch `master`.
- The layout rows, the "### Tests" commands and "## Checking your own synergy values" were checked:
  - The Python block runs verbatim from the repository root.
  - `closed_form(0.85, 0.25)["sts"]` = 1.2588305…; `exchange_rates` = {6.0705, −0.1892}.
  - The CLI line `python tools/ar1_diagnostic.py x.txt y.txt --window 60` works.
  - pytest is indeed absent from `requirements.lock.txt`, which pins numpy 2.5.3, scipy 1.18.1 and phyid 6c5f2e9, the
    same pins as CI. "Seconds" is accurate.
  - "Results 4" and "Recommendations" exist in the paper.
- No other README statement is contradicted by the new sections, apart from the seed statement in finding 5.

**manuscript/draft_v2.md:246 (new sentences)**

- The workflow does run the tests and phyid's own tests at the pinned commit, and those tests compare the Gaussian and
  discrete modes under MMI and CCS with reference outputs.
- The licence sentence matches the licence files.
- "The data are not included" is true.
- The number rows for this paragraph in `main_text_numbers.csv` include the new "4.0".
