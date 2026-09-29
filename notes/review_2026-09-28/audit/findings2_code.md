## Second-round audit of B26: the code correction, the runner, the V.S. scripts and deliver32/check32

**Summary.** Four defects are certain and will block things before any data are read:
- The start script refuses to start the run.
- The runner's `--only` mode can never run after a full run.
- `check32.py` fails twice on a correct bundle.

The correction itself (F01–F52) matches the rule, and I found no path to NaN or a wrong number. The three constants that B21 and the figure script hold are confirmed unchanged by the corrected B17, B17b and null runs.

**What I did.** I changed nothing in the trees and did not touch the rehearsal. It was still in B16 (R and O) when I finished; its first two steps match O apart from the SHA and timing. My scratch work is in `…/b32/audit2/agentC/`:
- `rt1`: runner test repository (sites, child mode, CSV, tables, `--only`).
- `rt2`: shows `--only` refusing.
- `rt3`: old and new runner run side by side on B5.
- `evsim`: the evidence script's summary run on simulated inputs.
- `applied/`: d108d66 with code32 applied, for comparison with tree2.

`--selftest` passes in modP (exit 0, "…passed through; 0 failed"), and again from a scratch copy of tree2's runner, with `-I` and from another directory. modP's runner is byte-identical to tree2's.

### Findings

**1. CRITICAL — `vs/b26_start.sh.in:70–72`: the self-test check never passes, so the run cannot start.**
- **What is wrong.** The script checks the last line with `case "$t" in *", 0 failed")`. The runner prints `…the step's exit message and status passed through; 0 failed` (semicolon, not comma).
- **Failure.** Tested with the real output: every `--check` and every start prints "STOP: B26's self-test did not pass", then NOT READY / NOT STARTED.
- **Fix.** `case "$t" in *"; 0 failed") ;; *) stop "B26's self-test did not pass" ;; esac`

**2. CRITICAL (the recovery path of rule (iv)) — `notes/partB26_positive_definite.py:326–329`: `--only` always refuses after a full run.**
- **Cause.** Section 6 runs `nrun notes/rev_assemble.py`, which rewrites `notes/review_computations_2026-09-14.md`. That file lies outside the three output folders, and its `git=` line changes from c25a310 to the run's SHA. The final run's own outcome entry (item 2) records exactly this file.
- **Failure.** After the full run, any `--only X` exits with "B26 --only NOT RUN: files outside the output folders have changed ([' M notes/review_computations_2026-09-14.md'])". I reproduced the mechanism in `agentC/rt2`. The planning session's test (`runt`) used a 4-step section 6 without `rev_assemble`, so it did not show this.
- **Fix.** Add `OUTPUT_FILES = ("notes/review_computations_2026-09-14.md",)` and use `dirty = [l for l in status if not (p := l[3:].strip('"')).startswith(OUTPUT_DIRS) and p not in OUTPUT_FILES]`.

**3. CRITICAL (blocks delivery) — `kit/check32.py:100–101`: "A: every file mode 100644" runs over the whole tree.**
- **What is wrong.** `git ls-tree -r A` includes `run_all.sh`, which is `100755` at d108d66. `apply_replacements.py` rewrites the file in place, so the mode stays.
- **Failure.** On a correct bundle the check FAILS, then "NOT VERIFIED", and `pull32.sh` is never written.
- **Fix.** Check only the files A changes or adds, against their mode at BASE:
  ```python
  base = {l.split("\t")[1]: l.split()[0] for l in sh("git","ls-tree","-r",BASE,cwd=C).decode().splitlines()}
  modes = sh("git","ls-tree","-r",A,"--",*sorted(exp),cwd=C).decode().splitlines()
  res("A: modes as at d108d66, new files 100644", all(l.split()[0] == base.get(l.split("\t")[1], "100644") for l in modes))
  ```

**4. CRITICAL (blocks delivery) — `kit/check32.py:139–147`: the B25 re-run cannot import numpy.**
- **What is wrong.** `R/.venv/bin/python` is made a symlink to PY. A venv interpreter started through a symlink in a folder without `pyvenv.cfg` runs as the base Python. I tested this with `v312/bin/python`: `sys.prefix=/usr`, and `import numpy` raises ModuleNotFoundError.
- **Failure.** B25 exits 1. Then l.147 `(R / OUTS[0]).read_text()` raises FileNotFoundError, because B25's outputs do not exist at A, and check32 crashes.
- **Fix (tested).** `(R / ".venv").symlink_to(Path(PY).parent.parent)`, i.e. link the venv folder itself; or run `[PY, "-u", "notes/partB25_binarised.py"]` directly. Also guard the reads when the re-run failed.

**5. MAJOR — rule (iv) (record l.7947–7948) and the runner's `--only` re-run only the failed step; the later steps that read its outputs are not re-run.**
- **What is wrong.** A step that fails leaves its outputs as committed, or partly rewritten, for example B4's npz files, which it writes inside its loop. Every later step that reads them has already run on them:
  - B4's outputs feed B6, B7, B10, B12, B14, B15, B19, B21, B22, the null (`diag_tables.md`, `inference_rows_diag.csv`) and the figures.
  - B17b's feed B23, B24 and the figures.
- **Failure.** B4 is killed (an outside cause) and re-run with `--only partB4_diagnostic`. B14, B15, the null, B21, B22 and Fig 5 keep values computed from the stale B4 outputs; B14 and B15 quote the stale residual as if read. The comparison cannot detect this.
- **Fix.** Add `--from STEP`, which runs that step and every later one (`names = [step_name(*x[:3]) for x in ALL]; ONLY = names[names.index(FROM):]`). State in rule (iv) that the failed step and every later step are re-run.

**6. MAJOR — the evidence is not enough to apply rule (i) to the binary outputs (`vs/b26_evidence.sh.in:16, 220–223`; runner CSV).**
- **What is wrong.** `8_binary_compare.py` prints one max|diff| per array. The changed binaries stay on the laptop ("kept here, not sent"). These are `diag_series_*` (4 files, 1.6 MB), `family_atoms_*_W60.npz` (0.2 MB), `inference_rows_diag.pkl` and `inference_rows_prewhiten.pkl`, and the PNG/PDF figures.
- **What also cannot be traced.** The runner's counts are per site, not per call, so a changed window of `diag_series` cannot be traced to counted matrices. For example, B4 l.75 accumulates all 4 × (variant, W) × subject × run × window evaluations in one row.
- **Fix.**
  - Add the changed `.npz/.npy/.pkl` files under `notes/review_results` (about 2 MB) and the changed figures to `b26_evidence.tar.gz`.
  - Have the runner record, per site, the call ordinals that had not-positive-definite matrices, with their counts (capped), in the CSV. For B4 l.75 the ordinal maps to (variant, W, s, c, w).

**7. MINOR — `run_all.sh`'s `rev_assemble` report also trips the evidence script (`vs/b26_evidence.sh.in:28, 83, 186–187`).**
- The check "nothing changed outside the output folders" will always be marked DIFFERS, as in the final run.
- That file is also absent from `diffs.txt`, `text_outputs.tar.gz` and `outputs.sha256`.
- **Fix.** Exempt it in `outside`, and add it to `OUT` for the diff and the tar files.

**8. MINOR — the chain of a site includes `.venv` frames on V.S.'s machine (`notes/partB26_positive_definite.py:116`).**
- **What is wrong.** `.venv` sits inside the repository root, so `root in fn.parents` is true for scipy's frames.
- **Effect.** The null's root searches in B15 (l.165–166) get chains like `notes/partB15_directed_crosslag.py:165 < .venv/lib/python3.12/site-packages/scipy/optimize/_zeros_py.py:NNN`. These differ from the preview and rehearsal, whose venv is outside the tree, and from the docstring's "frames of the repository". Sites are still told apart.
- **Fix.** Add `and not fn.is_relative_to(root / ".venv")`.

**9. MINOR — 15 of the 20 recorded examples per site are lost (runner l.73–74, 437, 515).**
- The CSV drops the examples, the tables print 5, and the JSONL is deleted at the end.
- Rule (ii)'s "the sts the code before gave them" then survives only as count, sum, min and max plus 5 examples. The tables are not "both written from the CSV" as the docstring says.
- **Fix.** Write `json.dumps(examples)` into an `examples` CSV column and read it back in `--only`.

**10. MINOR — `old_sts` (l.136–140) can print a RuntimeWarning into a step's log.**
- For a not-positive-definite matrix with an exactly singular block (|q| = 1, and similar), log-determinants of −inf give inf − inf in `_plugin_mis` and the matmul. That would appear as an added line in the step's log.
- **Fix.** Wrap the body in `with np.errstate(all="ignore"):`.

**11. MINOR — a failed read is silent in B14 and B15, and cascades from the null.**
- `partB14_family_atoms.py:36–39` and `partB15_directed_crosslag.py:225–228` print "n/a" silently if the regex fails.
- `review_v2_residual_null.py:100` calls `data_refs()` first. A failed match (an AttributeError) kills the null, and the null's log keeps only the `git=` line and the traceback. `15_figures_v2.py:272–275` then fails on that log.
- The regexes do match the real formats: on the committed files, and with B4's count appended they give "−0.0489", −9.7, −4.3 and −1.1, and modP's null log reproduces the held strings. So this is robustness only.
- **Fix.** Print CHECK FAILED instead of "n/a", and have the null fall back to "n/a" as well.

**12. MINOR — B21's (a) table can lose a line that the numbers table depends on.**
- B21's (a) table lists only pickle rows that are quoted in the text. Its only such row is the diag residual DiD at `inference_revision_tables.md` l.21, quoted as "+0.0115 [+0.0021, +0.0211]" (`supplementary.md:1584`).
- If the run changes that interval at its printed precision, the row drops and lines 22 onward move up one. That shifts 67 of the numbers table's 73 locators into that file (l.234–284), although their numbers are unchanged.
- The entry's "no edit adds a line…" does not cover this case, which the data decide. Rule (ii)'s update must relocate them.

**13. MINOR — B21's expectations are still constants with no check in the run (`partB21_inference_revision.py:87`, `15_figures_v2.py:420, 456`).**
- They are confirmed at the printed precision:

  | Source | Committed mean | Corrected mean (planning session's re-runs) | Prints |
  |---|---|---|---|
  | B17 (i) W60 residual DiD (modN) | 0.0048988 | 0.0049320 | +0.0049 |
  | B17b (i) W60 residual DiD (modN, finished 19:25) | 0.0026686 | 0.0026692 | +0.0027 |
  | Null DiD (modP) | — | +0.005400 | +0.0054 |

- B24's outputs are unchanged, apart from sign-of-zero noise.
- **Suggestion.** Add a check in B21, which runs after all three: compare `EXPECTATIONS` with the three tables and print CHECK FAILED if they differ.

**14. MINOR — a matrix with a non-finite entry can put different windows into the observed and predicted levels.**
- Such a matrix (a constant series in a window) now leaves B4's `pred` finite while `obs` is NaN. The "predicted" level would then include a window that "observed" excludes, so observed − predicted ≠ residual on that line.
- This is not plausible on the data, and the runner's non-finite column would show it.

**15. MINOR — `kit/check32.py:155–158`: a NaN on one side of the B25 comparison is ignored.**
- A NaN in one CSV against a number in the other passes, because `max(dmax, nan)` keeps `dmax`.
- **Fix.** Fail when `math.isnan(x) != math.isnan(y)`.

**16. MINOR — wording and bookkeeping.**
- The null's log line "data (residual_source.log): …" now prints values read from `inference_rows_diag.csv`; its interval is not in `residual_source.log`.
- `partB15:230`'s "(residual_source.log; …)": that log holds no run-level residual, and the value is now B15's own.
- The evidence note's regex (l.205) captures a trailing comma ("not positive definite 6,").
- Disposition 4 says the tables state that "the number the text quotes is B4's"; they do not, only the evidence note does.
- The evidence script does not cover an `--only` re-run: its checks on the log read only the unit log, so they would still report the failed step.
- If the writer's clone were V.S.'s repository, `deliver32.py` step 3 (installing pytest into `.venv`) would make the start script's pip-freeze check stop. Probably not the case.

### Checked and found correct

**The correction**
- tree2's `notes/*.py` equal d108d66 with code32's F01–F52 applied, byte for byte. Each old string occurs exactly once in d108d66.
- The JSON's F entries equal code32's. The only other code changes are `15_figures_v2.py` ("coupled", twice, matching the committed `captions_v2.md` at A) and `run_all.sh` (comments and B25's lines).
- The 19 dispositions are implemented as described, except as noted in findings 2, 5 and 16.

**The new edits (item 2)**
- The regexes read the real formats: B14 and B15 get "−0.0489"; the null gets W30 −9.7, W60 −4.3 and run-level −1.1 %, plus the diag row from `inference_rows_diag.csv`; B15's own run-level value is −0.01373, printed "−0.0137".
- B4's subject-1 lines, B23's D under rule (3), `nleft` and the note are correct.
- No edit adds or moves a line in a file that the numbers table locates. In modP the regenerated files keep their line counts: B23's tables 284, the CSV 401, B5's log 33, the null's log 17. Every edit is within an existing line. The numbers table locates `.py` lines only in `15_figures_v2.py`, whose lines did not move.
- All 10 verbatim-copy checks pass.
- B21's `quoted_at` is not affected by the text edits of A or B: its 10 quoted rows are all in `supplementary.md` l.161–176 and 1584–1589, and the fill inserts at l.1632.

**Completeness (item 3)**
- Every call of `atoms_from_corr` in section 6 follows rules (1)–(4); the callers left unchanged give it only positive-definite matrices.
- No other log-determinant is taken of a substituted matrix; phyid is used only on sample matrices.
- No plausible NaN or RuntimeWarning path exists.
- No step reads a B4, B10, B15 or B17b output before section 6 regenerates it.

**The runner (item 4)**
- It parses 39 steps (50 with the sandbox), matching the final run's section 6 (65 − 26).
- Child mode:
  - SystemExit messages and tracebacks pass through, with the same exit status.
  - `argv[0]` is absolute, but no step uses it.
  - `scripts/` is not on `sys.path`, but `15_figures_v2.py` imports nothing from it.
  - `\r` would be translated to `\n`, but no step prints one.
- Site keys tell apart two calls on one line, a helper's different callers, and a root search from the final evaluation.
- The CSV is written first; None values are written empty. The `--only` merge keeps the other steps' rows and examples, and failed steps are listed. The tables print correctly.
- Performance overhead is about 0.5 ms of `eigvalsh` per 300 matrices, which fits "about three hours".

**The V.S. scripts (item 5)**
- `bash -n` passes and shellcheck finds nothing substantive.
- INNER contains no `${` or `$$`; its `%` signs are safe in a transient unit. Killing the heartbeat prints no "Terminated" line after "=== unit exit".
- The evidence summary runs on simulated inputs. NSTEPS = 39 is right.
- The heartbeat, logind, kernel, dpkg and SHA checks parse the actual formats. `date -d` fails on "EET" (winter time), but the script falls back to the first step line's time.

**deliver32 and check32 (item 6)**
- The writer prompt's `HEAD_RE` and check32's `TL` mask the heading times identically; «ENTRY_TIME» is the record's only guillemet placeholder.
- `b25_fill.py` and the checks it runs use only the standard library.
- The writer's steps produce exactly the checked files: the tests and self-tests write nothing that git tracks.
