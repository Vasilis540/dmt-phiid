## Third-round text audit of commit A (work32A_d/tree2): report

Paths: `tree2` = `…/b32/audit3/work32A_d/tree2` and `kit` = `…/b32/audit3/kit`. I changed nothing outside `…/audit3/agentT/`. I did not report the «SYNTHETIC» or «ENTRY_TIME» placeholders.

The most serious problems:
- The preview misses three quotations in the supporting information whose values change.
- Rule (i) leaves out one wording change that this round itself introduced.
- The root README's list of what a run before B26 writes differently is incomplete.

### Findings, most severe first

**1. MAJOR — The preview's list of quotations misses three passages whose values change. The B26 entry's B17 sentence and disposition findings2_text 3 have the same gap.**
- **Where:** `tree2/notes/review_2026-09-28/checks/b26_preview.md` l. 2111–2122; record l. 7945–7946 ("S10 Table and S3 Text §7 transcribe them; the preview lists each"); `dispositions.md` l. 229–234 ("ten quotations"). Sources: `kit/preview_cfg.json` (`si_quotes`) and `kit/b26_preview.json` (`b17`).
- **Evidence (modF `calibration_tables.md`, lines 17, 20 and 26):** the corrected B17 prints −0.0108 ± 0.0017 at Δc = +0.03 (was −0.0109), −0.0056 ± 0.0018 at Δc = −0.02 (was −0.0055), and +0.0051 ± 0.0017 for (iv) (was ± 0.0018). Three passages quote these values:
  - (a) `supplementary.md` l. 1597, S19 Table, B17 (ii): "Residual −0.0010, −0.0052, −0.0109, −0.0055 at Δc = …" should become "−0.0010, −0.0052, −0.0108, −0.0056".
  - (b) `supplementary.md` l. 1599, S19 Table, B17 (iv): "residual +0.0051 ± 0.0018" should become "± 0.0017".
  - (c) `S3_Text.md` l. 349: "(the four rows give −17, −24, −22 and −25)". These are residual / δ_sym² for B17's (ii) rows.
    - From the 50 replicates of `calibration.csv` (the method the 26 Sep verification, N2, used first) they are now −17.82, −23.61, −22.15 and −24.85, so the first rounds to **−18** (it was −17.04).
    - From the printed table they are −17.40, −23.74, −22.11 and −25.06, so it stays −17.
    - The two methods agreed before the correction and now disagree.
- The preview itself already uses B17's corrected −0.0056 in its S19 (a4) re-check (l. 2114), but does not list where S19 quotes that value.
- **Fix:**
  - Add three entries to `si_quotes`: l. 1597 → "Residual −0.0010, −0.0052, −0.0108, −0.0056" (verdict "missed" stands); l. 1599 → "residual +0.0051 ± 0.0017" ("met" stands); S3 l. 349 with both values and the method stated. Then regenerate the preview.
  - Change the `b17` phrase to "…(S10 Table and S3 Text §7 transcribe them, S19 Table's rows B17 (ii) and (iv) and S3 Text §7's ratios quote them; the preview lists each)".
  - Change disposition 3 to "thirteen quotations (S3 Text l. 241, 347 and 349; `supplementary.md` l. 339, 1417, 1597, 1599, 1623 and 1673; …)".
  - Recompute item 11's hashes.

**2. MAJOR — Rule (i)'s list of this commit's wording changes leaves out B15's relabelled sentence (F27). The correction for findings2_code 16 introduced this gap.**
- **Where:** record l. 7979–7981; source in `kit/entry32.py`.
- **Evidence:**
  - In the second-round build F27 still printed "(residual_source.log; recomputed in this script's run-level section above)". It now prints "(this script's run-level section above)".
  - The committed `directed_crosslag_tables.md` l. 42 and `directed_crosslag_run.log` l. 71 carry the old text, so every B26 run will show this line as changed, whatever the matrices.
  - The list names B5's line, B10's statement, B23's brackets and note, B4's lines, "the two sentences of B15 and B22" (F24, F39) and the null's last line (F52), but not F27. By the rule, an unlisted difference "is a fault … before anything is read or committed".
- **Fix:** add "B15's label of the run-level residual in its sentence on the null's residual levels" to the list, and name it in the correction paragraph (l. 7902).

**3. MAJOR — The root `README.md` (l. 50–57) understates what a run of `run_all.sh` before B26 changes.**
- It says such a run "writes B5's line…, the null's residual at W = 30 and B23's simulation (b) with their corrected values…, and any output that the data's matrices change".
- It leaves out B17 (7 table lines and 1,698 CSV cells change, per the preview) and B17b (2 lines and 54 cells). Neither change comes from the data.
- It also leaves out the wording changes that happen in any case: B4's level lines and subject-1 lines, B10's statement, B15's three sentences, B22's sentence and the null's last line.
- **Fix:** "…writes the outputs of B5, the null, B23, B17 and B17b with their corrected values (`b26_preview.md`), the lines the correction rewords (rule (i) of B26's entry), and any output that the data's matrices change."

**4. MINOR — Preview §2 numbers rows by d108d66's table (l. 2070–2099), not by the table committed with it at A.**
- In tree2's table the same 24 flagged rows are 547, 685, 738, 741, 742, 785–788, 800, 801, 810–813, 824–827, 838, 839, 847, 848 and 1023.
  - I got these by running `check_numbers.py` on tree2's text and table with modF's outputs: "rows 1183, data rows 666, flagged 36".
  - In A's table, the preview's row 752 is an A_other value (−0.00166), not −1.59.
- The baseline is also misdescribed. '"rows 1191, data rows 675, flagged 12" for d108d66's outputs (a table of 1,191 rows then)' is `notes/review_2026-09-25/checks/check_numbers.out` (committed at b02d5ba, before the final run). d108d66's own check, `notes/review_2026-09-26/checks/check_numbers.out`, reads "rows 1193, data rows 676, flagged 12".
- **Fix:** in `preview26.py`, run on A's table with modF's outputs, use the 09-26 (or 09-28) output as the baseline, and give A's row numbers.

**5. MINOR — Record l. 7937, "150 in the conditions (i) and (a1)–(a4)": 16 of the 150 are in the unperturbed reference pairs.**
- `F_counts.jsonl`, chain 406<423, call 1 (the unperturbed `run_condition(base_b)`): 11 at line 200 and 5 at line 201.
- **Fix:** "150 in the unperturbed pairs and the conditions (i) and (a1)–(a4) (16 and 134)" (in `kit/b26_preview.json`, `b23_split`).

**6. MINOR — Item 10 (record l. 7749–7756).**
- "this entry quoted the counts of one path of the matrices": the counts were in B26's pre-run entry (findings2_text 2), not in the revision's entry. Write "B26's pre-run entry quoted…".
- The description of `findings2_code.md` leaves out "the planning session's scripts that package the revision and check the writer's commits", which `dispositions.md` l. 10–12 includes and where two critical findings were (3 and 4).

**7. MINOR — "every changed … array entry and image listed in full by `b26_changes.py`" overstates what the script does.**
- **Where:** record l. 7977–7978; review README l. 57–59; dispositions findings2_text 5 and findings2_code 6.
- `b26_changes.py` lists at most the first 2,000 changed entries per array, and summarises a PNG as a count of differing pixels.
- `diag_series_*.npz` arrays `local_res`/`local_obs` hold 23,520 entries each.
- **Fix:** "every changed line and cell in full; for each changed array the number of entries, the largest difference and the first 2,000 entries; for each image the differing pixels (the files themselves in the evidence)".

**8. MINOR — The list of steps that evaluate the same data (record l. 7966; runner docstring l. 35–36) is incomplete.**
- The list "(B4, B4's residual source, B14, B19, B22)" leaves out B10 (l. 176–185) and B15 (l. 109–111). Both evaluate the same whole-run substituted matrices as B4 (F08) and B14 (l. 132–134).
- B4 prints counts only for pair-windows. A run-level pair that is left out (Results 4's "1.1 % at the run level", S12 Table's run-level rows) is counted only in the runner's site rows.
- **Fix:** add B10 and B15 ("and the whole-run matrices"), and say where run-level exclusions are read.

**9. MINOR — B25 wording is not consistent across files.**
- `b25_fill.py` l. 191–192 writes "not defined on the 10⁻³ scale" into S3 §11, S19 row B25 (d), S20 row 2 and the outcome entry. The entry (l. 7809), the docstring (l. 60) and the tables (l. 678–679) say "not differentiable on the 10⁻³ scale".
- The `partB25_binarised.py` docstring (l. 52, 60) gives the criterion as "1 %", where the entry and the code (l. 600–602) say "1 % (+ 10⁻⁶)".
- **Fix:** use "not differentiable" in `b25_fill`, and add "(+ 10⁻⁶)" to the docstring.

**10. MINOR — The B25 run-time figure disagrees with its own source.**
- The `partB25_binarised.py` docstring (l. 73) says "about 6, 8 and 15 ms each … (--selftest times the longest)", and disposition findings2_text 22 repeats 15 ms.
- The committed `checks/b25_selftest.out` prints "one replicate at T = 840: 18.8 ms" (the previous build printed 23.7).
- **Fix:** "about 6, 8 and 15–24 ms". The 15–30 minute estimate still holds.

**11. MINOR — Wrong cross-reference in `dispositions.md` l. 245** (findings2_text 8): "(`findings_b25.md` 15)" should be "(`findings_text.md` 15)". `findings_b25.md` has 14 findings.

**12. MINOR — Doubled comma in `crosscheck_claims.csv`.**
- C072 and C084 (`other_sources`) read "Prichard1994.pdf, among V.S.'s PDFs,, PDF page 1". The replacement of "in your folder" introduced it.
- **Fix:** "Prichard1994.pdf, among V.S.'s PDFs, PDF page 1".

**13. MINOR — Item 7's word accounting (record l. 7715–7721) mixes an addition and a condensation.**
- "The changes above add 61 words" is net of the Limitations' ground-truth sentence (24 words, removed in D01), which the item then lists as a condensation.
- The "joined to the Discussion's first sentence" part (C03) adds 8 words.
- Applying the edits one by one with `wc.py`: additions +85; condensations C01 −30, C02 −23, the sentence −24, C03 +8, C04 −18, total −87; 6,997 + 85 − 87 = 6,995.
- **Fix:** state it that way, or say "net of the ground-truth sentence".

**14. MINOR — Item 2 (l. 7646–7648) does not describe everything that differs in P48.** As applied, P48 also turns "third-party plotting functions it bundles" into "bundled third-party plotting functions" (the JSON against `proposals.json`). Mention it.

**15. MINOR — `README.md` l. 178 (P49) lacks the qualifier P48 adds.** "The source repository carries no licence of its own" has no "at 77af7aa". The main text adds "at that commit" in P48 for the same reason (the Zenodo licence field could not be read). Add "at 77af7aa".

**16. MINOR — The review README (l. 54–56) describes a section the preview does not have.** It says `b26_preview.md` contains section 6 "run … on synthetic series". tree2's preview has no such section (`preview_cfg.json` has no `part2`). Regenerate the preview with `part2` when the rehearsal ends (and recompute item 11's hash), or drop the clause.

**17. MINOR — Rule (iii) (l. 7990–7991) points to a section that Methods does not name.** It says "the section to which Methods points", but Methods cites only "(S3 Text)". S3 Text describes the substituted estimate in §3 (l. 108) and its residual in §6. Name the section.

**18. MINOR — Rule (i) (l. 7975–7977), "as the final run's were (… item 5)", lists three comparisons.** That item had four, including `9_wrapper_compare.py` for B21's two files. Say that it is left out and why (the committed B21 files are now the final run's own).

**19. MINOR — Two B17/B17b statements in the entry need correcting.**
- "move in their last printed digits" (l. 7945) is inexact: (iii)'s mean p goes 0.521 → 0.505, and (ii) +0.01's share 0.08 → 0.10.
- B17b's "8 of the 5,100,000 of the null's function" (l. 7947–7948) all come from the draws that solve its generator's parameters (`cal_stats`, l. 121, which uses only a and |q|). They reach no output; say so, as the entry does for the null's root searches.

**20. MINOR — Captions the correction makes inexact are not listed.** Table 3's caption ("Rows 6–11: … 3,000 pairs … ± SE over pairs") now covers means taken over 2,980–2,995 pairs for the substituted sts, the residual and D. The preview lists only S18 Table's description line for this. Add Table 3's caption (captions are outside the word count).

**21. MINOR — Preview CSV rows are not numbered as the numbers table numbers them.** The preview's "row k" is a data row. The numbers table locates cells by file line (row 169 = `diagnostic_alternatives.csv:171`). State "row k = file line k + 2" in `b26_changes.py`'s header line.

**22. MINOR — Two stale or overstated statements in `CLAUDE.md`.**
- l. 19: "no computation label (B1–B24)" is stale now that B25 and B26 exist. `b25_fill`'s G14 will make it B1–B25, still leaving out B26.
- l. 373–374: "their findings were applied" is not true of all of them (findings2_code 13 and 14; the advisory items). Write "what was done with each is in `dispositions.md`".

**23. MINOR (wording).**
- `draft_v2.md` l. 164 (C03): "no ground truth for it; what it establishes" uses "it" twice in a row for different things (synergy, then the analysis). Suggest "for it; what the analysis establishes" (+1 word, 7,000 after G07).
- S1 Text (D02): "Python 3.12.3 … pinned in `requirements.lock.txt`", but the lock file does not pin Python.
- Data and code availability: `rev_phiid_fast` "computes the sixteen … atoms of any 4 × 4 correlation matrix". After F01 it returns NaN for a matrix that is not positive definite.
- Preview S19 re-check: "about half as large again" now describes ratios of 1.41 and 1.49.

### Checked and found correct

- **Preview §1 against the JSONL files.** Every count by path and by line, the not-positive-definite and near-singular counts, the smallest eigenvalues, the old-sts ranges and the chains:
  - B5: 4,047 / 171 / 3.
  - The null: 20,020,000 / 126 / 1,210 (115 / 6 / 5 by chain).
  - B23: 4,336,546 / 172 / 66 (109 / 61 / 2; 150 / 22).
  - B24: 17,640,000 / 0 / 15.
  - B17: 99,960,000 / 11,494 / 5,290.
  - B17b: 110,240,000 / 23 / 436.
- **Preview listings.** All 1,914 listing lines equal `b26_changes.py --dirs` on d108d66's against modF's `notes/review_results` (14 files differ in bytes, 11 with changes). `b26_null_sections.out` equals `F_null_sections.out`.
- **Preview §2.** The same 24 flags appear with tree2's table, and the 11 changes at printed precision are right. All ten listed quotations are on their stated tree2 lines, once each, and their new texts are right. The S10, S3 §7 and S18 rows match the regenerated lines. B23's verdicts stand (1.41/1.49 and 1.32/1.34; (a4) within 2 SE).
- **B26 entry against the code and outputs:**
  - B17 0.0048988 → 0.0049320; B17b 0.0026686 → 0.0026692; B21's constants reproduced; the evidence script compares them.
  - Rules (1)–(4) as coded (F01–F52); B17b's population reference; roles of B23 lines 200–202; brackets 5–20.
  - The fault examples (3.0788 against 0.4347; −0.2758 against 0.0011).
  - (ii): 52,440 points, |q| 0.986, 2 and 83; the √(1−q²)(1−r₁²) derivation.
  - The other callers of `atoms_from_corr` are complete.
  - tree2's `notes/*.py` equal modF's. In modN, the null differs only in `data_refs` and `__main__`, and `partB15` l. 78–92 are identical.
- **Item 11.** All 15 sha256 values match. The JSON in tree2 equals the applied bundle, and F01–F52 edit exactly the 15 named files.
- **Word count and checks.** Word count 6,995 (E09 −1; C01, C03, E10 unchanged in length). `check_numbers`, `check_cells` and `tablecheck` reproduce.
- **Numbers table.** 1,183 rows (13 deleted, 3 added). 23 contexts changed (21, plus the 2 corrections the table's header names). Every context is found in the text; rows are in reading order; occurrences run in sequence.
- **Other files.** Line counts: only `supplementary.md` changes (−2). `b25_fill`: all 18 anchors occur once, and its S3 §11 template and re-run wording agree with the entry. B25 facts: f′ = 1.342 and 0.129; self-test values as quoted. The crosscheck CSV's counts are right; nine rows were changed to the third person.
- **findings2_code fixes are in place:** the start script's "; 0 failed", the `OUTPUT_FILES` exemption, `--from`, `check32`'s modes, interpreter and NaN check, the `.venv` frames, the examples column, `errstate`, CHECK FAILED, the regex, and the evidence script's handling of B21's constants and of `review_computations`.
