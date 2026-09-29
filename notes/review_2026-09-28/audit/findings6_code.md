I audited items 1–5. I found no CRITICAL defect. The real flow works end to end: the sim passes, and so does my own replay of every step, which includes a real second run and check32c with its re-run. There is one MAJOR gap, in check32c, and eight MINOR points.

**Findings**

1. **MAJOR — `kit/check32c.py:169–177`** (the first run's outputs at A2; also `:192–196` for the second run's log, logic inherited from check32.py).
   - **What is wrong:** check32c masks the first run's wall-clock (`msk`, l.169) and nothing else pins it. Of the kept log it checks only line 1, the CHECK FAILED line(s) and the shape of the last line. The fill reads the wall-clock (`WALL0`, b25_fill.py:163) and writes it into S5 Text §4 through L07 ("({WALL0} s)"), while the entry states 514 s.
   - **Failure scenarios, built and run with `badbundles.py`:**
     - Kept tables and log edited from "Wall-clock 514 s." to 600: the fill prints READY, S5 Text reads "(600 s)", and check32c `--no-rerun --sim` reports 0 FAILS.
     - 36 lines deleted from the kept log after its CHECK FAILED line: 0 FAILS.
     - B's second-run log cut to 5 lines: 0 FAILS. The re-run compares only the CSV and the tables.
   - **Fix:** after l.177 add:
     ```python
     res("A2: the first run's tables and log give the wall-clock the entry states (514 s)",
         "Wall-clock 514 s." in T0L and "Wall-clock 514 s." in L0 and [l for l in L0 if l.strip()][-1].endswith("; 514 s"))
     ```
     and after l.196 add:
     ```python
     res("the second run's log has no CHECK FAILED line and ends with 150 checks, 0 failed", "CHECK FAILED" not in logt and bool(
         re.fullmatch(r"checks: 150, failed 0; wrote .*binarised_tables\.md and binarised\.csv; \d+ s",
                      [l for l in logt.split("\n") if l.strip()][-1])))
     ```
   - **Tested:** as `agentC6/check32c_fixed.py`. The sim bundle and my replay bundle each give 122 ok and 0 FAILS. The wall-clock and truncated-log bundles each fail exactly the new line. The writer's kit is unchanged.

2. **MINOR — the writer's prompt, step 8 (`prompt_bundle32_continued.md:96–97`).**
   - **What is wrong:** the exact `diff` covers three rounding-level columns that depend on the host's OpenBLAS kernel: (ii), (iii) and "mean of the atoms (pairwise) − exact". This host uses the SkylakeX kernels. Under `OPENBLAS_CORETYPE=Haswell` (Intel without AVX-512, or AMD Zen, which maps to Haswell in this build) or Prescott, those columns change: series 4 (iii) becomes 4.44e-16 instead of 0, and the largest (iii) becomes 4.44e-16 instead of 8.88e-16. The series, (i), knowns-mean-error and |known| columns stay identical.
   - **Why the stop is still right:** the first run's own script under Haswell gives a different binarised.csv. One row changes (`a,2A,d(2A)/dq [step 1e-3],0.85,0.25,inf`: 0 instead of 8.326672685e-14) and 16 check lines of the tables differ. On such a host the second run cannot equal the first, and the fill would stop after A2 is committed. The real first-run CSV matches the planning run, so the first run was on an AVX-512 host.
   - **Failure scenario:** if the writer's session has since moved to a non-AVX-512 host, step 8 fails, and the prompt presents that as the diagnosis not reproducing.
   - **Fix:** add after the command: "If only the columns (ii), (iii) and 'mean of the atoms (pairwise) − exact' differ, your machine's BLAS kernels differ from the first run's and B25's second run could not reproduce its values: stop and report it with `grep -m1 'model name' /proc/cpuinfo`."
   - **Alternative (drops the canary, so add a host check at step 1):** diff only the robust columns with `cut -s -d'|' -f2,3,6,8` on both sides. I verified this diff is empty under all four kernels.

3. **MINOR — `kit/b25_fill.py:178` (L03).**
   - **What is wrong:** the "already holds the entry of the first run" test uses the heading with its time (`mk.group(0) in rec0`). The entry's Rule says the fill stops unless the parent's record holds "not this one".
   - **Failure scenario:** a record at A0 that holds the entry with another time, or with «ENTRY_TIME», passes and the fill prints READY. It cannot happen in this flow: A is pinned by check32c's hashes, and the edit-above it needs is caught by step 7 and check32c's prefix check.
   - **Fix:**
     ```python
     if mh.group(0) not in rec0 or re.search(r"^## The binarised estimators on the AR\(1\) family \(B25\): the first run and the "
                                             r"correction of one check,", rec0, re.M):
     ```
   - **Tested:** the baseline and a clean rebuild give READY; same time, other time and placeholder are all refused. Changing L03 means rebuilding the JSON, the tarball and the prompt's sha256 values.

4. **MINOR — the writer's prompt, step 6 (`prompt_bundle32_continued.md:63`).**
   - **What is wrong:** `grep -c '^-[^-]'` misses a removed line that starts with "-" (the record's many list items; the diff line reads "-- …") and a removed blank line.
   - **Failure scenario:** deleting "- **20 Nov 2026** — public preprint…" or a blank line above still prints 0 (tested). Step 7 and check32c catch it anyway.
   - **Fix:** require `git diff --numstat HEAD -- manuscript/analysis_record.md` to print `70	0	manuscript/analysis_record.md`, or `git diff -U0 HEAD -- manuscript/analysis_record.md | grep -v '^--- ' | grep -c '^-'` to print 0. Both hold on the correct flow.

5. **MINOR (pre-existing, not introduced by H01–H07) — `notes/partB25_binarised.py:632`.**
   - **What is wrong:** `DEVMAX = max(DEVMAX, dev)` drops a NaN (`max(0.0, nan)` is 0.0).
   - **Failure scenario:** a NaN replicate would pass the "every replicate" check, although `check()` fails on NaN and the new docstring says "in every replicate". In practice unreachable, since local MIs are finite.
   - **Fix:** `DEVMAX = float(np.maximum(DEVMAX, dev))`. Optional: it would be an H08 and change the sha256 quoted in planning_runs.md.

6. **MINOR — `kit/b25_fill.py:17–23` (the L01 docstring).**
   - **What is wrong:** it omits the stop at l.164–165 (either run not making 150 checks), and it describes the entry-at-A0 test more broadly than the code does (see 3).
   - **Fix:** add "if either run made other than 150 checks;".

7. **MINOR — `kit/check32c.py:176`.**
   - **What is wrong:** `wrote \S*binarised_tables\.md`.
   - **Failure scenario:** a correct bundle fails if the writer's repository path contains a space.
   - **Fix:** use `wrote .*binarised_tables\.md`.

8. **MINOR (wording) — the writer's prompt, step 7 (`:65`).**
   - **What is wrong:** it says "These 16 lines must be printed, exactly", but the commands print the record's line last while the block lists it third. The lines match as a set.
   - **Fix:** say "in any order", or order the block as the commands print it.

9. **MINOR (wording) — `commit_message_32_2of3.txt:1` and `commit_message_32_3of3.txt:1`.**
   - **What is wrong:** with A's fixed subject, the history reads "1 of 2", "2 of 3", "3 of 3".
   - **Fix:** add one sentence to A2's body saying A's subject was written before the first run, or drop the counts from A2's and B's subjects.

**Checked and found correct**

1. **B25 (H01–H07):**
   - The orig→kit diff is exactly H01–H07, and kit equals treeA2.
   - The new `dev` is the maximum, over samples and the 16 atoms, of |Kc@_MINV_T − phyid's local atoms|, with shapes (99999, 16), as the names and docstrings say.
   - The MMI call's `I_res` equals the CCS call's bitwise, and the old and new `phyid_quantities` return identical values.
   - CSV rows are identical for run_old vs run_new, the sim's second vs first run, and my own real second run vs the first run.
   - The tables differ only in the count line, the 11 rows of this check and the wall-clock.
   - The check is not vacuous: with the published mask it gives 0.13–0.21, a 2e-12 change to one sample gives 2e-12, and NaN fails.
   - Still 150 checks; the self-test is 54 checks, 0 failed. No test, CI step or run_all.sh depends on the check names.
2. **b25_fill.py:**
   - 45 cases in `filltests.py`: all the refusals the task lists, plus variants, stop with NOTHING WRITTEN and no file touched. The baseline is READY and byte-identical to B.
   - Order checks: equal minutes, month boundaries and 9→10 Oct are handled numerically.
   - Under el_GR.UTF-8 and de_DE.UTF-8, with and without `--now`, the fill is READY, identical to B, and writes English months.
   - Every hunk of the diff is one of L01–L11; the verdict code and the other templates are unchanged.
3. **b25_check_diagnosis.py:**
   - It runs from the root (and from `notes/`) in 7 s and writes nothing.
   - It reproduces the .out byte for byte on this host.
   - (i) is bitwise the orig check for all ten series.
   - (iii) is the corrected expression.
   - numpy's first-axis mean equals a row-by-row loop bit for bit.
   - The entry's figures match the .out.
4. **check32c:**
   - On the sim bundle with `--no-rerun --sim`: 120 ok, 0 FAILS. Without `--sim`, exactly the two designed FAILS.
   - With the re-run, on my replay bundle: 124 ok, 0 FAILS.
   - Wrong bundles it catches: A2 editing an earlier entry's text, A2 changing only an earlier heading's time, a changed first-run CSV row, a changed first-run check value, an extra file in A2, and B editing an earlier heading.
   - pull32.sh stops on a changed bundle, a dirty tracked file, a branch other than master, and an untracked file the bundle would overwrite. Otherwise it fast-forwards, pushes and prints DONE, and a second run is a no-op.
5. **The writer's prompt:**
   - The three sha256 values match the delivered files, the tarball holds exactly the six files, the 16-line block equals `expected_sha256_32c.txt`, and `deliver33.py` regenerates the prompt byte for byte.
   - I replayed every step on a fresh clone, including the ones sim33.sh skips:
     - step 5: ok ×28 and "all 28 entries applied";
     - step 6: 0/1/0;
     - step 7: 16 values and 19 files;
     - step 8: "107 passed", "Test passed.", 54 checks with 0 failed, B26 0 failed, and an empty diagnosis diff;
     - step 10: 19 files;
     - step 11: a real run at a051fc2, 150 checks, 0 failed, rows equal to the first run;
     - step 12: READY;
     - step 14: 13 files;
     - step 15: the bundle verifies.

Everything is in `/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/b33/audit6/agentC6/`:
- `filltests.py` / `filltests.out` — the fill tests
- `badbundles.py` / `badbundles.out` — the wrong bundles
- `item1.py` — the B25 check
- `check32c_fixed.py` — the tested check32c fix
- `filltest_fix.py` — the fill-fix test
- `repos/w` — the replay repo (A2 a051fc2, B eb7c3b1)
- `w_32_crosscheck.bundle` and `chk_w_rerun.out` — the replay bundle and its check with the re-run
- `oldrun_haswell/` — the first run's script under the Haswell kernel
