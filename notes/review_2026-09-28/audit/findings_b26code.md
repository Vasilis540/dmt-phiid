## Audit of the B26 correction (F01–F30), the B26 runner and the draft entry

**Scope and what I ran.** Paths below are in the audit tree (`…/b32/audit2/tree`). I changed nothing in either tree; `git status --porcelain --ignored` is clean apart from the `__pycache__` that was already in `final31/gh`, dated 16:08. Every run that writes outputs was done in a copy of the audit tree (`agent1/tc`). The scripts I ran and their logs are in `agent1/`:
- **Core checks:** `t1_core.py` compares `atoms_from_corr` old against new; `t2_means.py` tests bit-identity of the new means, masks and `pearsonr`.
- **Positive-definiteness checks:** `t3_grids.py` covers the other callers; `t5_b17b.py` covers F19 and the overlay counts; `t8_b17sim.py` simulates B17-like windows; `t9_null30.py` covers the null at W = 30.
- **Runner checks:**
  - B23 under `--child`: `b23_child.log` and `b23.jsonl`.
  - B5 and B8, run directly and under `--child`.
  - An end-to-end run of the runner on a small section 6: B5, B21, B14 and B25.
  - `--selftest` in the audit tree. It passes: "4 sites; atoms_from_corr 52 matrices (2 not PD … −0.2941 to −0.2794); _logdets 52 (2); PairPhiID 10 (0); 0 failed", exit 0.

**Summary.** Nothing I found would crash a step or put NaN into an output. The code implements the rule, with two exceptions (findings 3 and 9). The draft entry misstates what happens in B23 (finding 1). Three gaps affect what the run reports or can catch (findings 2, 4 and 5).

### Findings

**1. MAJOR — the draft entry's B23 sentence is wrong** (`b26_entry_draft.md` l.55–57)
- **What the entry says.** All failing matrices "have deviations added"; "none of its AR(1) matrices" fails; "D, its only quantity that reads them"; "every other number of its tables is unchanged".
- **What the run shows.** I ran B23 under the runner's `--child`, and it reproduces the preview exactly: 4,336,546 matrices, 172 not positive definite (PD), 66 near-singular.
  - 109 of the failures are at `partB23_diagnostic_alternatives.py:200`. That line is `base = atoms_from_corr(ar1_corr(ax, ay, q))`, the AR(1)-substituted window matrices of simulation (b).
  - 61 are at l.201 (δ_anti) and 2 at l.202 (δ_sym); none are at l.203.
- **What changes in the tables.** The AR(1)-substituted sts, residual, D and "residual change / Δr₁" columns all change, as do the levels line, the (a5) base row and 70 CSV cells. Examples:
  - Levels: AR(1)-substituted sts +0.78780 → +0.78788 [11]; residual −0.07027 → −0.06998 [11].
  - Ratio for (i): −0.390 → −0.387. This value feeds Fig 3 through `15_figures_v2.py` l.269–271.
- **Fix.** Replace the sentence with something like: "B23: 172 of its 4,336,546 matrices, all in simulation (b): 109 AR(1)-substituted window matrices (l. 200) and 63 with deviations added (61 δ_anti, l. 201; 2 δ_sym, l. 202). The AR(1)-substituted sts, residual, D and ratio leave out 5–20 of the 3,000 pairs per condition (11 unperturbed) and change; every other number is unchanged."

**2. MAJOR — hard-coded copies of values that B26 can change; rule (i) cannot detect them going stale**
These strings are identical before and after the run, so the comparison against the committed outputs passes them even when the values they copy have moved.
- **B21's expectations.** `partB21_inference_revision.py:87` has `EXPECTATIONS = (0.0027, 0.0049, 0.0054)`. These are B17b's and B17's (i) W60 residual DiDs (`calibration_filtered_tables.md` l.8, `calibration_tables.md` l.8) and the null's DiD. B21 (b) computes its p-values against them.
- **The figure script.** `15_figures_v2.py:420` looks up B21's rows by those same strings (P_EXP). `calibrated_expectation()` at l.404 reads the *regenerated* B17b table. If B17b's value moves, Fig 5 would combine a new expectation with p-values computed against the old one.
- **Quoted data values** in outputs:
  - `partB14_family_atoms.py:102` ("−0.0489")
  - `partB15_directed_crosslag.py:224` ("−0.0489 … −0.0137")
  - `review_v2_residual_null.py:91` ("[data: W30 -9.7 %, W60 -4.3 %, run-level -1.1 %]") and l.98 ("DMT +0.0077, PCB -0.0038, DiD +0.0115 …")
- **These values can plausibly move.** I simulated B17-like W60 windows: 0.018 % of the AR(1)-substituted matrices are not PD (21 of 117,600 per replicate). So «b17» and «b17b» will not be zero, and the +0.0049 and +0.0027 may move at the printed precision. The data run will likely have failures too, which could move −0.0489 and −0.0137.
- **Fix.** Add a check to rule (i)/(ii): compare these constants with the regenerated values at their printed precision. If any differs, edit them and re-run B21, B14, B15, the null and `15_figures_v2`. Better still, have B21 read its expectations from the regenerated tables now; the P_EXP lookup in `15_figures_v2` must then change with it, or it raises "no line starting …".
- **Severity.** This becomes CRITICAL (a wrong number) if any of these values changes at its printed precision.

**3. MAJOR — F04 in B4 breaks rule (1) in the subject-1 pair lines** (`partB4_diagnostic.py:87–88`, printed at l.99–100)
- **The problem.** F04 stores `o[ok], p[ok], ax[ok], ay[ok], q[ok]`. The line at l.100 then prints "obs mean/SD" over the PD subset, and "residual mean/SD" as the mean over pairs where both exist. Rule (1) says the observed mean stays over all pairs and the residual is obs(all) − pred(valid).
- **Consequence.** If subject 1's windows 2 or 6 contain a non-PD pair, the regenerated `diag_tables.md` will show a changed observed mean, which the rule cannot explain.
- **Fix.**
  - Store the mask instead: `pair_stats.append((c, w, o, p, ax, ay, q, ok))`.
  - At l.100, use `o.mean()` and `o.std()` over all pairs, `p[ok].mean()` and `p[ok].std()` for the prediction, and residual mean `o.mean() - p[ok].mean()`.
  - Compute the residual SD and all correlations over `ok` (rule 2), and optionally print `[k]` for the pairs left out.

**4. MAJOR — the run's counts cannot be read as "matrices left out per step and calling line"** (rule (ii); runner `site()` l.71–84, key l.137)
- **Evaluations that feed no output are counted with those that do.** The null's root searches, B10 section B's `null_cell` searches, B15's `brentq` solves (l.163–164) and B17b's calibration solves all go through `review_v2_residual_null.py:69`. So the null step will report 126 there, although only 115 matrices (W = 30) are left out of anything.
- **Helper functions hide the caller.** Calls made through a helper are attributed to the helper's own line: B23 `sts()` l.119 and `response()` l.200–203; the null's l.67/69 when called from B10, B15 and B17b.
- **Two calls on one line are merged.** `partB4_residual_source.py:53` evaluates both CA and CB on one line, so their counts are merged.
- **The grand total double-counts data matrices.** The same data W60 window matrices are evaluated in B4 (l.75), B14 (l.73), B19 (l.149) and B22 (l.119), so the header total counts each failing data matrix up to four times. Rule (iii)'s "number of matrices left out" needs a defined source, for example B4 l.75 split by W and variant.
- **Fix.**
  - Add to the key the innermost frame in the step's own script.
  - Add the column offset for calls on the same line (`f.f_code.co_positions()` at `f.f_lasti // 2`).
  - Name the source of the number the text will quote.
  - For the null sections of B10 and B15, count final evaluations separately, as `b26_null_sections.py` does for the null itself.

**5. MAJOR — rule (iv) cannot be carried out under the wrappers** (runner l.263–266 and l.316–334)
- **The problem.** The runner always runs all of section 6 and requires a clean tree. There is no way to re-run one failed step under the wrappers and merge its counts into `positive_definite.csv`.
- **Consequence.** A step re-run "alone" (rule iv) with plain `python` produces no counts. Meanwhile, later steps in the full run have read the failed step's stale committed outputs. For example, B22's check at l.251 compares against `diag_series` res and would fail if B4 had failed.
- **Fix.** Add `--only <step>`: run the listed steps, relax the clean check to their outputs, and append to or replace their rows in a persistent stats file.

**6. MINOR — string `sys.exit` messages are swallowed in `--child`** (runner l.181–187)
- `sys.exit("…")` becomes exit code 1 with no message printed. I confirmed this with B21's missing-data exit: its step log contained only `git=…`. B21 l.79 and B22 l.78 exit this way.
- Fix: `try: runpy.run_path(...)` followed by `finally: dump(...)`, letting SystemExit and exceptions propagate naturally; drop the `except` clause and the final `sys.exit(code)`.

**7. MINOR — the runner can lose all counts at the very end** (l.336–338 and l.391–395)
- The JSONL is deleted before the tables and CSV are written. If `sts_min` or `sts_max` is None (old sts ±inf or all NaN, which needs an exactly singular block), `f"{None:+.4f}"` raises and three hours of counts are lost.
- Also: the CSV prints "None" for missing values; the parent decodes child output with strict decoding.
- Fix: write the CSV first; guard None in formatting; unlink the JSONL last; use `errors="replace"` in Popen.

**8. MINOR — F27 shifts every later line of `diagnostic_alternatives_tables.md` by 2** (`partB23…:491–493`)
- The note adds two lines before "Predictions", which is at committed line 120.
- About 19 locators in `manuscript/main_text_numbers.csv` point at lines 144, 150, 156, 190, 192, 196, 201, 204, 208 and 209 (for example the 0.0080 at l.204 quoted in Results 1 and the Fig 2 caption). `notes/review_2026-09-25/checks/check_numbers.py` would report "HELD STRING NOT ON LINE" for numbers that did not change.
- Fix: append the note to the existing (b) description line (l.449, which still holds "3000 pairs"), or put it at the end of the file.

**9. MINOR — B23's D does not follow rule (3)** (`partB23…:412`, `"D": rs(r_anti)`)
- B23 leaves a pair-window out of D only where the base or δ_anti matrix fails. B22 and B24 also leave it out where the δ_sym or both matrix fails. In the preview, 2 δ_sym failures (l.202) stay in B23's D.
- Fix: `ok4 = isfinite(r_anti) & isfinite(r_sym) & isfinite(r_both)`, then `"D": rs(np.where(ok4, r_anti, nan))`.

**10. MINOR — B23 displays numbers that no longer add up**
- **Levels line (l.451).** observed − substituted ≠ residual (0.71753 − 0.78788 = −0.07035, but −0.06998 is printed). Rule (4) makes the residual per pair, unlike rule (1); the entry should say so.
- **Ratio column (l.465–469).** Its Δr₁ is over `mr`, while the printed Δr₁ column is over `m`. So the ratio is not Δresidual ÷ Δr₁ as printed, and it carries no bracket.
- **CSV (l.462).** It records no counts of pairs left out.

**11. MINOR — some edits are not bit-identical even when every matrix is PD; the rule should expect these differences**
- F10/F11 (B10 l.334, l.375), F16 (B15 l.173) and F29/F30 (null l.78, l.91) replace `mean(obs − pred)` with `mean(obs) − nanmean(pred)`. These differ by up to 2e-16 in 98 % of my tests: inside rule (i)'s 1e-9 tolerance, but not "unchanged".
- If exact identity is wanted: `np.mean(obs - pred) if np.isfinite(pred).all() else np.mean(obs) - np.nanmean(pred)`.
- The intended text changes (the F08 line format, F12, F27, the brackets) should be listed in rule (i) as expected differences.

**12. MINOR — two explanatory sentences are now incomplete** (B22 l.279 "their difference: the lag-0 substitution and the non-additivity"; B15 l.134 "the responses account for …%")
The residual is over the pairs whose AR(1) matrix is PD, and D, Sym and D + Sym are over the pairs whose four matrices are PD. So these sentences now also carry a pair-set difference they do not mention.

**13. MINOR — how the runner defines and counts "not PD"** (l.108, l.346–347)
- `not_pd` = finite and λ ≤ 0. F01 and the entry also NaN non-finite matrices, which the runner counts in a separate `nonfinite` column. That column is absent from the "Calling lines" table.
- PairPhiID non-PD sample matrices would be counted but not corrected (`_logdets` still discards the sign), and the entry has no rule for them.

**14. MINOR — the entry mentions files that are not in the audit tree, and one claim needs a qualifier**
- Not in the tree: the CI workflow that is said to run `--selftest` (draft l.71), `tools/ar1_diagnostic.py` (l.22) and `revision/text_replacements_2026-09-28.json` (l.36). Make sure the revision commit contains them.
- "for those that are not positive definite, the sts that the code before … gave them" is true only for the `atoms_from_corr` path.

**15. MINOR — F23 is not idempotent** (code32 F23)
Its old string (the KEYS line) is part of its new string, so applying the replacements twice inserts `nleft` twice while the count check still passes.

**16. MINOR — F19 is correct as it stands** (`partB17b…:249–250`)
- The post-shift matrix is always PD. Its q is built from q_e with |q_e| ≤ 0.999, so the PD condition reduces to 1 − q_e² > 0. Excluding by the pre-shift matrix is therefore sufficient.
- In 400,000 draws with the committed Q_POOL, 0 pre-shift and 0 post-shift matrices failed, so F19 changes nothing.
- Excluding the post values by the pre mask is a paired choice, not a literal application of rule (1); say so in the entry.

**17. MINOR — expected CHECK FAILED lines, and a truncated comparison listing**
- If the run-level residual moves, B21's check against the committed 17-Sep log (l.286–292, `check_C1_residual_vs_null.log`) will print CHECK FAILED; the entry should anticipate this.
- `6_committed_compare.py:151–153` lists at most 10 lines of 170 characters per file, but rule (i) needs every difference.

**18. MINOR — things outside this run to confirm**
- B25 is not in the audit tree. Confirm it reads no section-6 output (skipping it would otherwise leave it stale) and parses no bracketed B23 cell.
- Four scripts outside section 6 call `atoms_from_corr` and are neither re-run nor counted: `planning_checks…/reviewer/v_needed_dev.py`, `v_slope_q.py`, and `review_2026-09-22/refcheck/var1.py`, `popdelta.py`.

**19. MINOR — cosmetic**
- A trailing space appears in the "=== …" lines and in the "script" cells of the tables when there are no arguments.
- The expansion of the deconvolution loop is hard-coded rather than parsed from `run_all.sh`. It is correct today.

### Checked and found correct

**The core fix (F01)**
- Rows of PD matrices are bit-identical to d108d66. I tested batch sizes 1–42,000, AR(1) and PairPhiID matrices, and all-PD batches.
- NaN rows appear exactly where the smallest eigenvalue is ≤ 0 or an entry is non-finite.
- Two-dimensional and empty inputs work, and no warnings are raised (tested with warnings as errors).

**Identity of the new means**
- `np.nanmean`, masked `.mean()` and `pearsonr` on masked copies are bit-identical to the old forms when nothing is excluded: 81 cases, including strided columns and axis-0 means of (n, 16) arrays.
- So F02–F09, F13–F15, F17–F28 leave every output unchanged where all matrices are PD.

**The tree matches the correction exactly**
- The audit tree equals d108d66 plus the 38 entries (each applied once), plus the runner and `b26_null_sections.py`, with nothing else changed. No other copy of a replaced line was left unedited.
- Every verbatim copy still passes: B22, B23 and B24 against B15 l.70–92 and l.78–92, B19 l.75–79, B6 l.51–80, B17 l.67–86, and B17b l.81–88, 97–112, 135–150 and 154–186. The line counts of the copied ranges are unchanged.
- B17b's `analyse_run` block appears verbatim in B17.
- The new `ok` variables collide with nothing.

**Callers left unchanged give only PD matrices** (smallest eigenvalues computed)
- B1 grid 0.00245; B3 0.00245; `15_figures_v2` grid 0.0196.
- B8 population matrices (0 non-PD when run under `--child`); B12's `Cw`; B1's symmetric overlay model.
- The unedited callers inside edited files: B10 `family_sts` 0.094; B19 `sts_of`, the coupled family and q = 0 at 0.05; B22 `sts_of`; B23 (f) grid 0.0134 and (a), (c), (d), (e) symmetric; B5's `A()` symmetric.

**Counts reproduced**
- B5: 4,047 matrices, 171 not PD at l.55, equal to the analytic condition count; stdout is identical run directly and under `--child`.
- Null at W = 30: 115 of 560,000 not PD; residual −0.0885 (−8.51 %) under rule (1) and −8.50 % over the pairs where both exist. This confirms F12 and the entry's figures.
- The B23 preview is reproduced exactly (counts, line attribution, tables and CSV), with no new warnings.
- B23's `nleft`, `change_row`, levels line and (a5) base row are consistent, and the bracket counts are correct.

**Saved arrays read by later steps stay finite, and formats stay compatible**
- `diag_series` (read by B7, B10, B12, B14, B19, B21, B22 and the figure script); `family_atoms` npz; `inference_rows_diag`; `crosslag_deviation.csv` and `directed_crosslag.csv`/tables; `exchange_rates`; the calibration tables; the null log.
- The figure script parses only B23 columns 3, 6 and 11, which carry no brackets.
- These cross-checks stay consistent under the new rules: B22 residual against `diag_series` res (within 1e-10), B14's check against the diagnostic, and B21's comparison of B10 with B15.
- No crash or NaN path exists short of every matrix in a batch failing.

**The runner**
- Section-6 parsing is correct: 39 steps without the deconvolution sandbox and 50 with it (the loop expands in `run_all.sh`'s order), with B25 skipped and `nrun`/`nstep`/`step` destinations as in `run_all.sh`.
- `--child` is faithful: `__main__`, `__file__`, `sys.argv`, `sys.path`, cwd and the warning paths all match a direct run. The machine is Linux, going by `/home/vilalius` in the committed log. No section-6 step uses multiprocessing, launches another Python script as a subprocess, reloads modules or pickles classes defined in a step.
- The wrappers return exactly what the functions return. There is no double counting: `_logdets` skips the `atoms_from_corr` path.
- The selftest's recovered old sts equal d108d66's (−0.29405, −0.27942).
- End-to-end: the clean-tree check passes with only the tee'd log new; the tables, CSV and sha256 are written; failed steps are listed; the exit code is 1 when any step fails.

**Values I can supply for the entry's «» fields**
- B5: 171 not PD; 1,829 kept; min +0.000, max +4.585, mean +0.094, share 0.53.
- Null: 115 at W = 30; 11 more in the root searches.
- B23: 172 of 4,336,546, split 109 / 61 / 2.
- B24: 17,640,000 (from the preview).
- From the overlay, 52,440 pair-windows: allowed asymmetry below 0.05 in 2 and below 0.10 in 83 using the entry's √(1 − q²)(1 − r₁²); the exact boundary gives 2 and 79.
