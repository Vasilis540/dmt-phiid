## Third-round code audit of B26 (agent C): 3 major and 6 minor findings, no critical defect in the run as planned — and I accidentally stopped the R2 rehearsal

**Incident — act on this first.** At about 20:28:50 UTC I stopped the R2 rehearsal by accident, which the prompt forbade.
- **How.** To test an interrupted runner, I ran `pkill -TERM -f 'partB26_positive_definite.py'` against my own scratch run. The pattern also matched R2's runner (PID 18118) and its `--child` running B16 (PID 18893).
- **R2's state.**
  - `R2.out` ends with `=== runner exit 143`. R2 was about 9 minutes into step 3 (B16); steps 1–2 had finished.
  - R2's tree holds the regenerated outputs of steps 1–2 and a partial `prewhiten_run.log` (49 of the 60 lines B16 printed).
  - No CSV was written, and `/tmp/b26_s948v6x2` is left behind.
- **O2 was not touched** and is still running.
- **What I did.** I messaged "main" immediately. I did not restart or change R2.
- **To restart R2.** Its outputs must first be restored, because the runner refuses a dirty tree. The build's «SYNTHETIC» placeholder, and so `deliver32.py`, wait on R2.
- **Afterwards** I only signalled process groups I had started myself, with TMPDIR set to my scratch folder.

### Findings, most severe first

**1. MAJOR (CRITICAL if the run is interrupted): an interrupted runner leaves no counts, so rule (iv)'s `--from` cannot be used and the evidence script refuses to run.**
- **Where:** `notes/partB26_positive_definite.py` l.403–404, 412/416–419, 428–468 and 348–349; `vs/b26_evidence.sh.in` l.35–37.
- **What is wrong:**
  - The per-site counts live only in a JSONL inside a private `mkdtemp()` directory under /tmp.
  - The CSV and the tables are written once, after the last step.
  - `--from` requires that CSV (l.348–349).
  - Each step's log is written through a buffered handle (l.412), not written through as `tee` does.
  - The evidence script stops unless the unit log contains `=== unit exit`.
- **Tested** on a copy of runt: SIGTERM during the last step.
  - `--from 15_figures_v2` then prints `B26 --from NOT RUN: notes/review_results/partB/positive_definite.csv of a full run at d3e14f7 is not there`.
  - A new full run prints `B26 NOT RUN: the tree is not clean ([' M notes/review_computations_2026-09-14.md', …])`.
- **Same effect** from a power loss or `systemctl stop runb26`. After a reboot, /tmp is emptied, so the completed steps' counts are gone. `b26_evidence.sh` keeps printing "The run has not ended".
- **Step logs lose their tail:**
  - The killed rehearsal R's `calibration_run.log` is 0 bytes, although `R.out` shows B17's `git=` line and 9 progress lines.
  - R2's `prewhiten_run.log` has 49 of 60 lines.
- **Why it matters:** both attempts of the final run ended in a power-off, and rule (iv) was written for exactly this case.
- **Fix:**
  - (a) Factor l.440–466 into `write_csv(final)` and call it after each `RESULTS.append(...)`, adding `f"; partial: {len(RESULTS)} of {len(STEPS)} steps"` to the first line. Strip that suffix from `head_old` in `--from`. `--from <interrupted step>` then works.
  - (b) Open step logs line-buffered: `open(dest, "w", encoding="utf-8", buffering=1)`.
  - (c) In the evidence script, when there is no `=== unit exit` line and `systemctl show runb26 -p ActiveState --value` is not `active` (or the unit is gone after a reboot), continue with a note instead of exiting.
  - (d) Give `--from` a start mode with the same inhibitor and heartbeat. Today it runs from a terminal, and the evidence's heartbeat and journal checks cover only the unit's time window.

**2. MAJOR: rule (i)'s list of rewordings leaves out B15's changed label.**
- **Where:** `manuscript/analysis_record.md` l.7979–7981, against `notes/partB15_directed_crosslag.py` l.230.
- **What is wrong:** the run turns "(residual_source.log; recomputed in this script's run-level section above)" into "(this script's run-level section above)". The old text is in `directed_crosslag_tables.md` l.42 and `directed_crosslag_run.log` l.71 at d108d66; the change is disposition 16. Rule (i) lists "…the two sentences of B15 and B22, the label of the null's last line". The two sentences are the ones naming the pairs; this label is not among them.
- **Scenario (certain):** `b26_changes.py` lists this line. It is neither a listed rewording nor traceable to counted matrices, so rule (i), read literally, declares a fault.
- **Fix:** add ", B15's label of its run-level residual" to the list.

**3. MAJOR: call ordinals are capped at 2,000 per site, the total is never counted, and the tables misreport it.**
- **Where:** `partB26_positive_definite.py` l.79, 161–163, 528.
- **What is wrong:** only the first 2,000 flagged calls are kept, and no count of such calls exists. The tables print `({len(bc):,} calls, the first 2,000 in the CSV)`, that is "(2,000 calls…)".
- **Scenario:** B17 l.104 had 11,494 non-positive-definite matrices over 137,200 calls of 300 pairs in the preview, and 340 of the 350 W60 replicate rows changed. That is thousands of flagged calls. Ordinals stop within the first conditions, so the changed rows of (ii) to (iv) cannot be traced to windows, as the entry's run paragraph says they can. A synthetic step with 3,000 flagged calls printed "… (2,000 calls, the first 2,000 in the CSV)".
- **Fix:**
  - Add `"bad_calls_n": 0` to `entry()`. In `record()`: `if n_bad: e["bad_calls_n"] += 1` before the capped append.
  - Add a CSV column `bad_calls_n` and print `f"({n:,} calls; the first {len(bc):,} in the CSV)"`.
  - To keep every ordinal, store runs of ordinals, or raise the cap together with `csv.field_size_limit(sys.maxsize)` in the runner (l.445, 471) and in the evidence summary (l.218). The default limit of 131,072 characters is reached at about 8,700 entries.

**4. MINOR: the evidence summary accepts a crashed comparison and has lost some of the final run's checks.**
- **Where:** `vs/b26_evidence.sh.in` l.242–243, 183–185 and 193–200.
- **What is wrong:**
  - Scripts 6, 8 and 10 never call `sys.exit`, so exit status 1 means a traceback. It is still marked "ran to the end (exit status 0 or 1)".
  - The final run's evidence required `ex == "0"` plus each script's last line. It also checked that the output folders held only ' M' and '??' entries (catching a deleted output), that no header said `nogit`, and B21–B24's check counts.
  - The kernel check says "ok" when the journal is unreadable, because the "Hint:" line is filtered out before the search.
- **Fix:**

  ```python
  LAST = {"6_committed_compare": "untracked files under the output folders: ", "8_binary_compare": "summary: ",
          "10_logs_figures_compare": "10_logs_figures_compare: "}
  for k, head in LAST.items():
      ex = read(E / f"{k}.exit").strip()
      check(f"{k}.py ran to the end (exit status 0)", ex == "0" and head in read(E / f"{k}.txt"), ex)
  ```

  Restore the codes, nogit and kernel-readability checks, and the B22–B24 counts (22, 63 and 10 run, 0 failed; modF reproduces them).

**5. MINOR: `b26_changes.py` pairs lines wrongly when a block has insertions or deletions.**
- **Where:** `notes/review_2026-09-28/checks/b26_changes.py` l.90–101.
- **What is wrong:** inside "replace" blocks, lines are paired by position.
- **Tested:** old `line two 3.14159` and new `INSERTED 7` + `line two 3.14160` are listed as "l.6→l.6 − line two… + INSERTED 7" and "l.—→l.7 + line two 3.14160". This is the case of B21's table (a) losing a row.
- **Fix (tested; it pairs these correctly):** within non-equal opcodes, re-align on `sk = lambda l: split(mask(l))[0]`. Pair lines in "equal" sub-blocks (and equal-length "replace" sub-blocks) through `agree`, and report the rest unpaired.

**6. MINOR: `b26_changes.py` listing details.**
- **Where:** l.338, 190–195 and 44.
- **What is wrong:**
  - `n_changed` counts "the same pixels" PNGs and "the same once /CreationDate…" PDFs as changed. On V.S.'s machine that is every regenerated PDF.
  - A change in the NaN pattern alone prints "largest difference 0".
  - An entry that is ±inf in both files gives inf − inf, printing "largest difference nan" plus a RuntimeWarning captured in `b26_changes.txt`.
  - CAP is 2,000 entries per array, while rule (i) and the evidence say "listed in full". B4's `local_res` has 23,520 entries per array.
  - Date stripping ignores xref offsets. A UTC "Z" date is 6 bytes shorter than "+03'00'", so every PDF regenerated in this sandbox reads "differs". V.S.'s machine is unaffected.
- **Fix:** count "agrees" and "the same" separately; wrap the comparison in `np.errstate`; give the max over finite pairs; state the cap in rule (i) or write the full listing to a file.

**7. MINOR: B14 and B15 crash, instead of printing CHECK FAILED, when `diag_tables.md` is missing or unreadable.**
- **Where:** `partB14_family_atoms.py` l.38; `partB15_directed_crosslag.py` l.226.
- **What is wrong:** only a regex miss falls back to CHECK FAILED; `read_text()` raises. In B15 this happens after all the computation, so no tables are written. The null's `data_refs` does catch OSError.
- **Fix:** `try: t = (OUT / "diag_tables.md").read_text(encoding="utf-8")` `except (OSError, UnicodeError): t = ""`.

**8. MINOR (can block delivery): `check32.py`'s B25 comparison fails on float noise.**
- **Where:** `kit/check32.py` l.164–187.
- **What is wrong:**
  - Tables lines must match exactly once the time, the sha256 and the wall-clock are masked, but B25's Checks table prints noise-level values with `{d:.3g}`, e.g. `abs(P.sum()-1)` and the symmetries.
  - CSV values are printed with `.10g` and compared at 1e-9 absolute, about one unit in the last digit for values ≥ 1.
- **Scenario:** this machine has AVX-512 (NumPy X86_V4). A writer on another CPU prints "4.44e-16" where this machine prints "2.22e-16". The check says FAILS and "NOT VERIFIED" on a correct bundle.
- **Fix:** compare tables lines with `b26_changes.agree` (or accept both values below their tolerance). For the CSV use `abs(fx-fy) <= 1e-9*max(1, abs(fx))`.

**9. MINOR: the self-test hides its own failures behind a TypeError.**
- **Where:** `partB26_positive_definite.py` l.315–318.
- **What is wrong:** with no sts row, `f"{sts.get('sts_min'):.4f}"` raises TypeError, so the FAILED list is replaced by a traceback. The start script still stops.
- **Fix:** `sts.get('sts_min', float('nan'))`, and the same for `sts_max`.

(Also minor: the tables are said to be made "from the CSV alone", but they print the invoking process's python and numpy versions and its wall-clock.)

### Checked and found correct

**The correction**
- All 52 code32 entries apply exactly once to d108d66 and reproduce tree2's files byte for byte. The JSON's F entries equal code32's.
- tree2's scripts equal modF's HEAD, except `partB25_binarised.py` and `phiid_indep.py` (not in modF), and `run_all.sh` and `15_figures_v2.py` (the known B25 and "coupled" changes).
- `atoms_from_corr` gives NaN exactly for matrices that are not positive definite or have a non-finite entry. Tested with |q| = 1 and NaN entries; the other rows are unchanged.

**Dispositions**
- 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 15 and 16 are in place and do what they say; 11 holds except for finding 7.
- Tested directly:
  - `--from` after a full run that includes `rev_assemble.py` works.
  - `.venv` frames are left out of the chain (fake `.venv` package with a callback).
  - `old_sts` prints no warning at |q| = 1.
  - The evidence's regexes on modF's outputs give (0.0027, 0.0049, 0.0054), equal to `EXPECTATIONS`.

**The runner**
- It parses 39 steps, or 50 with the sandbox, in `run_all.sh`'s order.
- Site key: two calls on one line are two sites; lambdas and imported modules are handled; root-search evaluations are told apart from the final one.
- Child mode: tracebacks and SystemExit statuses pass through; the counts are dumped in `finally`; no random numbers are consumed.
- Rehearsal R against O over steps 1–12: every output agrees within the masks.
- The CSV:
  - JSON columns round-trip.
  - The 2,000-entry cap stays under the csv field limit.
  - A failed step keeps its step row and partial site rows; a killed child records exit −9.
- `--from`:
  - It refuses an unknown step, a missing name, changed non-output files, and a CSV from another commit.
  - The merge, the row order and the first line are correct.
  - The tables' sha256 equals the file's.
- `--selftest` passes (0 failed) from a scratch copy, also with `-I` from another directory.
- The tables render the edge cases.

**`b26_changes.py`**
- On modF its output is byte-identical to `F_changes.txt`.
- Unquoted CSVs: `calibration.csv` is the only irregular one, with its commas in the first column.
- Binaries: npz keys, shapes and NaN patterns, lists of dicts with mixed types, and DataFrames; all d108d66 binaries load.
- Also correct: images, new and deleted files, `--dirs` and REF mode.
- No number the correction can change is hidden by the duration mask, and every text output is valid UTF-8.

**The new reads**
- The regexes read the held strings in modF.
- A failed read changes only the text within its line.
- The files the numbers table locates keep their line counts in modF.
- Every `atoms_from_corr` call in section 6 follows rules (1)–(4) or receives only positive-definite matrices.
- `rev_assemble.py` reads none of the changed CSVs.

**The start and evidence scripts**
- `bash -n` and shellcheck: nothing substantive.
- INNER has no `${` or `$$`; it is the final run's INNER plus pipefail and tee.
- GNU date parses EEST and EET.
- The data files the start script checks are exactly those section 6 opens; NSTEPS = 39.
- The summary runs cleanly on a simulated run.
- `notes/review_computations_2026-09-14.md` is handled throughout.

**`check32.py` and `deliver32.py`**
- The heading-time masks `TL` and `HEAD_RE` agree.
- The record's only guillemets are «ENTRY_TIME» and «SYNTHETIC».
- The mode checks are correct.
- The writer's steps produce exactly the checked files (the tests write only ignored files).
- Short SHAs stay 7 characters (1,619 objects in the clone).

Everything is in /tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/b32/audit3/agentC/:
- `rt/` — runt copy with a full run and a `--from` run
- `fk/` — synthetic runner tests
- `b26c/` — synthetic `b26_changes.py` inputs
- `OR_changes.txt` — rehearsal R against O
- `modF_changes.txt`
- `evE/` — the simulated evidence folder
