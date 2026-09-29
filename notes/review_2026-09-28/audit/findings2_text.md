# Audit of the round 21 revision (commit A, `work32A_c/tree2`): findings

Scope: the three new record entries, `dispositions.md`, the edits to the manuscript and SI, the numbers table, the READMEs, CLAUDE.md, run_all.sh, the licences, CITATION.cff, the workflow, and the B25 and B26 scripts. I checked these against the JSON, the check outputs, d108d66, the preview runs in `b32/codetest` (modP = final code; modN, modN2, modE = drafts) and short computations of my own. Placeholders are not reported.

One side effect to disclose: I imported `rev_phiid_fast` from `tree2/notes` once. That rewrote the stale, git-ignored cache file `tree2/notes/__pycache__/rev_phiid_fast.cpython-312.pyc` (at 18:51). Nothing else in the trees was touched.

## Findings, most severe first

**1. MAJOR — B23's section of `checks/b26_preview.md` (lines 42–68 and the run-log block) lists the output of a superseded draft, not of tree2's code.**
- **What it shows:** under "13 line(s) differ" it lists `− (none)` / `+ A number in brackets … (B26; the column 'pairs excluded' counts the pairs left out of every quantity).` as a *new line*.
- **Where that came from:** modN2's run (41ab285), where the note was two added lines (119–120 of `diagnostic_alternatives_tables.md`).
- **What tree2 actually does:** `partB23` (F41–F43) appends a longer note to the existing line 102 ("…(B26); the column … every quantity, and the last column divides the residual's change by r₁'s over the residual's pairs."). modP's regenerated tables and run log show exactly that.
- The numbers agree (modN2 and modP CSVs are identical apart from the header). But the "every changed line" listing that the entry cites misstates the final code's change, and it shows the very line insertion that findings_b26code #8 said would move the numbers-table locators.
- **Fix:** regenerate B23's section from modP (aed71a8), and state the tree used.

**2. MAJOR — B26 entry, record l. 7906–7910: the counts it quotes are not the preview's, although l. 7901–7903 say they are in `b26_preview.md`.**
- **B23:** the entry says "172 of its 4,336,530"; the preview (l. 33) says 4,336,546.
- **B24:** the entry says "none of its 12,264,000"; the preview (l. 172) says 17,640,000.
- The entry's figures are the `atoms_from_corr`-path counts only: P_counts/N_counts give B23 4,336,530 + 16 PairPhiID, and B24 12,264,000 + 5,376,000 PairPhiID. The preview gives all-path totals and no split.
- **The null:** "115 of the 560,000 at W = 30" is not in the preview (which has 126 of 10,010,000 at l. 69); it is in `checks/b26_null_sections.out`.
- The build's report flagged all three as STOP.
- **Fix:** write "172 of the 4,336,546 matrices it evaluates (4,336,530 through `atoms_from_corr`; 16 sample matrices)" and "none of its 17,640,000 (12,264,000 through `atoms_from_corr`)". Add the per-path split to the preview. Cite `checks/b26_null_sections.out` for the per-section count of the null.

**3. MAJOR — the preview has no list of "the numbers of the main text whose source changed", which the entry (l. 7902) and the review README (l. 54) say it contains. The data-free runs already fix several of them.**

Values old → new (modP's `diagnostic_alternatives.csv`):
- **Table 3** (`draft_v2.md` l. 129–132):
  - c = +0.02 (innovations held): −0.0048 ± 0.0006 → −0.0047 ± 0.0006
  - c = −0.02: −0.0055 ± 0.0007 → −0.0056 ± 0.0006
  - coupling at fixed (r₁, q): +0.0068 ± 0.0006 → +0.0068 ± 0.0005
  - δ = ±0.02: +0.0098 ± 0.0009 / +0.0102 ± 0.0010 → +0.0093 ± 0.0009 / +0.0095 ± 0.0009
  - −0.01·sign(q): +0.0185 ± 0.0004 → +0.0181 ± 0.0004
  - Δa_s: +0.0102 ± 0.0002 → +0.0101 ± 0.0002
- **Table 3 caption** (l. 120), plus `S3_Text.md` l. 241 and `supplementary.md` l. 339: "−1.59 (Δa_s) and −2.73 (λ)" → −1.58 and −2.76.
- **S3 l. 241:** the same Table-3 values.
- **S18/S19** (supplementary l. 1417, 1623):
  - (i) +0.00537 → +0.00532
  - (a1) +0.00978/+0.01016 → +0.00931/+0.00951
  - (a2) −0.01354/+0.01850 → −0.01348/+0.01808
  - (a4) −0.00479/−0.00546 → −0.00471/−0.00565
  - The B23 verdicts stay the same by their criteria.
- **S20 Table B item 1** (l. 1673, and its mirror in `partB5_literature_v2.md`): "−1.36 to +4.59 … 57 %" → "+0.00 to +4.59 … 53 %".

**Fix:** add this list to the preview, and in the entry say which verdicts were re-read.

**4. MAJOR — the entry's sentence "Values that scripts held as quotations of other outputs that the correction can change are now read from those outputs" (l. 7879–7882) is not true.**
- `partB21_inference_revision.py:87` still holds `EXPECTATIONS = (0.0027, 0.0049, 0.0054)`: B17b's and B17's (i) W60 residual DiDs and the null's DiD.
- `scripts/15_figures_v2.py:420` looks up B21's rows by those strings.
- Rule (i) cannot see them go stale, because the strings print unchanged.
- `dispositions.md` (b26code #2) says they stand: B17 is still +0.0049 (modN's calibration table) and the null still +0.0054. B17b is pending «B17B».
- **Fix:** name them in the entry ("B21's three expectations and `15_figures_v2.py`'s look-up of them stay held; the corrected data-free steps reproduce them: …"). If B17b's +0.0027 moves, edit them before the run.

**5. MAJOR — rule (i) (l. 7933–7937) requires "every changed line and cell listed in full", but nothing in the tree does it.**
- `6_committed_compare.py` (l. 151–153) prints at most ten lines of 170 characters per file.
- `dispositions.md` l. 204–205 says `b26_evidence.sh` "saves the full diff"; that file is neither in tree2 nor named in the entry.
- **Fix:** commit the script (e.g. under `notes/review_2026-09-28/checks/`) and name it in rule (i), or state the exact commands (a full `git diff` plus a cell-level CSV listing).

**6. MAJOR — wrong range of the correction's entries.** `notes/review_2026-09-28/README.md` l. 39 says "(F01–F30; B26)", and so does `b26_preview.md` l. 3. The JSON has F01–F52, as the record's l. 7888 and dispositions l. 9 say. **Fix:** "F01–F52".

**7. MAJOR — references to a second audit round that is not in the tree.**
- The review README (l. 58–61) names "the second round of audits, `findings2_*.md`"; no such files exist.
- `dispositions.md` l. 9–10 says "The corrected revision was audited again (see the record's entry, item 10)", but item 10 (l. 7734–7746) describes no second round.
- Item 11's sha256 of `checks/b26_preview.md` and of `audit/dispositions.md` (which still carries «B17B» at l. 170) must be recomputed when those files are completed.
- **Fix:** add the files, their dispositions, a sentence in item 10 and their hashes in item 11 — or remove the mentions.

**8. MAJOR — the B25 entry says "the text `b25_fill.py` writes says nothing of the re-run" (l. 7843). It does mention it.**
- The outcome-entry template (`b25_fill.py` ~l. 465) writes "A separate session re-runs B25 at {A}; the commit that follows its re-run records the result."
- G17 (l. 370) writes "Remaining work: B25's re-run at {A} by a separate session …".
- The same wording is in `b25_fill.py`'s docstring (l. 17–18) and dispositions l. 60–61.
- **Fix:** "…states no result of the re-run; it names the re-run only as still to be made."

**9. MAJOR (planning) — B26 rule (iii) (l. 7946–7947) will push the main text over its word limit.**
- The rule requires new text in Methods.
- After `b25_fill`'s G06/G07, Introduction through Methods is exactly 7,000 words with headings (checked with `wc.py` on a copy with those edits), which is the limit.
- Any Methods addition from B26 will exceed 7,000.
- **Fix:** have the entry say where the words come from (a named condensation), or put the statement in S3 Text with a pointer from Methods.

**10. MINOR — the null's "11 more" is cited to the wrong source** (l. 7907–7908, "(11 more … root searches …, `checks/b26_null_sections.py`)"). That script's docstring (l. 6–7) says it does not count the root searches. The 11 come from the wrappers: 126 at l. 69 in the preview, minus 115; P_counts chains 75<76: 6 and 75<77: 5. **Fix:** cite the preview's wrapper count for the 11 and the script for the per-section counts.

**11. MINOR — `partB26` docstring and the entry misdescribe two things.**
- Docstring l. 31 says "A matrix counted at a site is left out of whatever that site's result feeds". That is false for the PairPhiID and "other" paths: their atoms still come from |det|. Rule (v) is right; reword the docstring.
- The list of steps that evaluate the same data windows, "(partB4, partB14, partB19, partB22)" (docstring l. 32; entry l. 7924–7925), omits `partB4_residual_source.py`. It substitutes on the same ts_gsr W = 60 windows (l. 50, 53).

**12. MINOR — the tables are not "both written from the CSV"** (entry l. 7927–7928; docstring l. 44–45). The tables' examples are not in the CSV (FIELDS has no examples column); they come from the in-memory rows, or from the previous tables under `--only`. Relatedly, dispositions l. 176–177 says "the tables say … that the number the text quotes is B4's"; the tables' text does not say this.

**13. MINOR — the "last bit" claim holds only on the machine that wrote the committed outputs** (entry l. 7895–7896, "every output equals d108d66's … differences in the last bit of a mean (below 10⁻¹⁵)").
- On the planning machine even the old atoms (modE) change `family_checks.log` ("TDMI +0.000 → −0.000", "0.0e+00 → 1.4e-17") and about 30 B23 lines, by up to 2.2e-15.
- The preview masks these, but only its B24 section states the 1e-9 rule.
- **Fix:** add "on the machine that wrote the committed outputs", and state the preview's tolerance once at its top.

**14. MINOR — preview l. 49** says "byte for byte this commit's (their scripts, the modules of notes/ they import …)" for B24, B17 and B17b.
- `review_v2_residual_null.py`, which B24 and B17b import, differs in modN: no `data_refs`, different `__main__`.
- The wrappers there are an earlier runner version.
- Outputs are unaffected; reword.
- Preview l. 3 also cites `preview26.py`, which is not in the repository.

**15. MINOR — entry l. 7890–7895: two inexact statements about other callers.**
- "they are unchanged": `scripts/15_figures_v2.py` is changed (caption wording, E07s/E07d). Say "their calls are unchanged".
- "The scripts outside `run_all.sh` that call it …" omits `tests/test_ar1_diagnostic.py`, which CI runs.

**16. MINOR — revision entry item 2 (l. 7646–7650) understates how P13 was changed.** P13 was also reworded: "of an example macaque time series (Fig. 3e)" became "in the caption of an example macaque time series" (P13/P13L). Mention the rewording as well as the dropped figure number.

**17. MINOR — revision entry item 3 (l. 7682–7683), "each as the paper states it":** the paper states where the excess changes sign (0.008; S18 Table's first negative is at 0.0080), not the values +0.0049 at 0.006 and −0.0012 at 0.008. Say "consistent with the sign change at 0.008 that the paper states".

**18. MINOR — "every package pinned" is not exact** (item 4 l. 7698; `tests.yml` comment l. 6: "Every package is pinned"). pip is upgraded unpinned, pytest's dependencies are unpinned, and Python is "3.12", not 3.12.3. Qualify: "the analysis packages, pytest and phyid's build backend pinned".

**19. MINOR — CLAUDE.md l. 373** says "three sessions audited the prepared round". There were four (findings_b26code), plus the second round.

**20. MINOR — JSON bookkeeping.** N12's `why` says "the record's two entries", but it appends three. The K ids skip K20.

**21. MINOR — B25 entry wording against the script.**
- l. 7794–7795 says "not defined on the 10⁻³ scale"; the script's docstring (l. 60) and tables (l. 677) say "not differentiable", and the criterion is "1 % (+ 10⁻⁶)".
- The rule's list of checks that can stop the fill (l. 7838–7840) omits the I(x_t; x_t+1) = 1 − H₂ check.
- l. 7835 says "the captions"; `b25_fill` changes one caption (S3 Text's, G10) and the labels B1–B25 (G02, G04).

**22. MINOR — B25 runtime estimate.** The docstring (l. 72–73) says "72,000 replicates at 4–10 ms each". `checks/b25_selftest.out` reports 23.7 ms per replicate at T = 840, so T = 840 alone is about 9.5 min; "10–15 min" (docstring and run_all.sh) is likely low.

**23. MINOR — `b25_fill.py` l. 254 (the S3 §11 template)** cites "(S20 Table, rows 1 and 2)" for Luppi et al. (2022)'s binarised replication. S20 row 1 does not state it; only row 2 mentions binarisation. Cite "Luppi et al., 2022, pp. 3, 14" or add the fact to row 1.

**24. MINOR — S1 Text l. 5 and S4 Text l. 55 cite "(S2 Text)" for joblib 1.6.0.** S2 Text names only rsHRF 1.7.0. S1's phrasing also suggests rsHRF is pinned in `requirements.lock.txt`; it is not (joblib is). **Fix:** "…pinned in `requirements.lock.txt`; the deconvolution (S2 Text) used rsHRF 1.7.0, not in the lock file, and joblib 1.6.0."

**25. MINOR — S4 Text l. 26:** "its parameters are not reported" should be "their parameters" (the images).

**26. MINOR — main-text wording.**
- l. 25: "which that study calls": the preceding citation is Luppi et al. 2022; name Luppi et al. (2024).
- l. 57: "most at c = +0.05" holds only among the computed c = 0.02, 0.05 and 0.10; the quadratic minimum is near 0.044. Say "lowest of the values computed at c = +0.05".
- l. 164: "the brain, for which these data have no ground truth" attaches to the wrong noun.
- l. 172: "addressed autocorrelation, in part, which is the subject of Varley (2024)" has an ambiguous "which".
- l. 246: "the repository carries no licence of its own at that commit": two repositories appear in the paragraph; say "the data release's repository".

**27. MINOR — `review_v2_residual_null.py` l. 115** still prints "data (residual_source.log): …". The values now come from `inference_rows_diag.csv`, and the interval [+0.0021, +0.0211] is not in `residual_source.log` (the old label had the same issue).

**28. MINOR — root README l. 40–49: at commit A the code carries the correction but the committed outputs predate it.** A run of `run_all.sh` at A would not reproduce B5's line, the null at W = 30 or B23 (b). Add a sentence saying so, pending B26.

**29. MINOR (style/advisory).**
- `crosscheck_claims.csv` has "Not in your PDF folder" / "in your folder" in 8 rows.
- `LICENSE-CC-BY-4.0.md` l. 5–9 puts under CC BY 4.0 the result files, which include per-subject derivatives of third-party data used under an email agreement. Consider saying whether that agreement covers their redistribution.

## Checked and found correct

- **Item 11 hashes:** all 12 sha256 values match the files.
- **Revision entry, item 1 (counts):**
  - 271 claims; verdicts 194/59/2/2/14; firsthand 252/1/18.
  - 759 PDF passages (120 for Luppi 2024/2026); 33 from other sources.
  - The not-supported claims are C210 and C256, and the cannot-check claims C072 and C084, as described.
- **Revision entry, item 2:**
  - 51 proposals; classes A 13, B 35, C 3.
  - Only P11, P13 and P48 differ from `proposals.json`, as noted above.
  - P50: phyid 6c5f2e9 is dated 2026-03-14 12:44:53 +0000.
  - Every S20 edit is mirrored in `partB5_literature_v2.md`, apart from pre-existing label differences.
- **Revision entry, items 3–5:**
  - Imports: pandas is used only in notes/; h5py only reads the spin file; joblib and rsHRF only in `rev_deconv`.
  - S1 named 4 packages and S4 5 at d108d66.
  - `phiid_indep.out` values are as quoted.
  - Tests: 107 (98 + 9, with tolerances as stated).
  - The doctest passes; the CITATION and workflow YAML parse; phyid's tests exist and download from OSF.
  - The licence statements agree across README, CLAUDE.md, CITATION.cff, the Data and code availability section and the licence files.
  - The MMI-lattice identities are right.
- **Revision entry, items 7–9:**
  - 6,996 words (re-run).
  - Numbers table: 1,193 − 13 + 3 = 1,183 rows; 21 contexts recomputed; the derived +0.05 row matches `coupling_map_tables.md` l. 12–14.
  - `check_numbers`, `check_cells` and `tablecheck` re-run with the same results.
  - Line counts are unchanged except supplementary −2; Varley 2023 is gone, with no dangling citation.
  - No process or B labels in the main text; verbatim copies 13/13; "coupled only at lag 0" applied everywhere.
- **B25 entry:**
  - Grid, lengths, replicates, the smooth set and the checks match the script.
  - sts = T − 2F + 2A − B and EC = T − F verified numerically on the lattice; the Gaussian and q = 0 cases hold.
  - f′ = 1.342 and 0.129 bits.
  - Self-test figures match (54 checks; 9.81e-9; 2.78e-17; 12 decompositions, 7 published; 54 fits, 5 from support).
  - Step counts 42/126; threshold 6.89 = 0.1957/0.0284 (S3 §4 l. 128; B22 (d)).
  - `b25_fill`'s verdict logic and stop conditions match; all 18 anchors occur once in tree2; the S19 rows have 5 cells.
- **B26 entry and code:**
  - The PD condition is right (0 mismatches against eigenvalues on 100,000 draws).
  - The corrected `atoms_from_corr` is bit-identical on PD rows and gives NaN exactly where λmin ≤ 0.
  - Rules (1)–(4) are implemented as stated in all 15 edited scripts, and the edited-file list equals the F01–F52 targets.
  - The other callers' matrices are PD.
  - B5 numbers are right (171/1,829; +0.000 to +4.585; +0.094; 0.53 against d108d66's).
  - The null's figures are right (115; 0 elsewhere; −0.0885, −8.51 %; −8.50 % alternative; log otherwise unchanged).
  - B23's 172 are all in (b), split 109/61/2 at lines 200/201/202, with the old sts ranges as stated.
  - The B24 count came from wrappers with the final counting logic.
  - Overlay points: 52,440; |q| up to 0.986; 2 and 83 as stated.
  - The runner is as described: 39 steps parsed from run_all.sh; outputs go where run_all.sh writes them; SystemExit passes through the child; sites are keyed by line, column and chain; the clean-tree and `--only` checks and the CSV/table headers work; the self-test passes.
  - B21's check against the 17 September log uses a 5.1e-6 tolerance; the comparison scripts exist; B17b's shifted matrix is always PD.
  - The new regexes in B14, B15 and the null reproduce the held strings exactly; F41 is idempotent.
- **Dispositions:** every "Corrected" item is in tree2 and does what it says, except those raised in findings 1, 5, 7, 8 and 12.
