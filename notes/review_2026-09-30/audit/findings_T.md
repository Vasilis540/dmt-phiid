*Copy for the repository: paths of the planning session's scratch space are shortened to SP/; the opening sentence on where the report could not be saved is left out.*

The audit is finished: 13 findings. None changes a conclusion, a test verdict or the word limit (6,997 ≤ 7,000).

**Summary (13 findings, most severe first)**
1. **inaccuracy** — S3_Text.md:274 (B32): "+0.01153 − 0.00267 = +0.00887" should be +0.00886 (the files give 0.0088649893).
2. **inaccuracy, last digit** — S3_Text.md:274 (B32): "+0.00405" should be +0.00404 and "−0.00108" should be −0.00109; B24's expectation was taken at its rounded +0.00001.
3. **inaccuracy** — supplementary.md:1317: S18 Table's source note still says the files are "both at a9d9ca4", reproduced "byte for byte". Part (b) is now B26's regeneration at d5a65bd, and B56 fixed only S17's note.
4. **inaccuracy, minor** — draft_v2.md:166 (L02): "but not the other two" says the slope interval does not exclude the null's rate. The paper's own figures (−0.3699 against an interval end of −0.3735) and Results 4 ("ends at the null's") say otherwise. Word-neutral fix: "but not the AR(1) generator's".
5. **wording** — S3_Text.md:225 (B24): the W = 30 clause names 2 of 8 moved S12 values. "The four W = 60 pair-windows" should be four on each variant (the record, l. 8296–8297, has the same slip).
6. **wording** — analysis_record.md:8302–8309: "except three" (L05, −2 words) is counted among the length cuts, though it is a check correction. By entry it is +19, +2 and −22; the 6,997 total is right.
7. **wording** — draft_v2.md:216 (L03): removing "Inference:" left a sentence with no main verb.
8. **wording** — draft_v2.md:120 (Table 3 caption): the rates −1.58 and −2.76 are taken over the residual's pairs. The table's own columns give −1.57 and −2.73, and the caption doesn't say so.
9. **wording** — draft_v2.md:61 (B02): the relative clause "whose substituted matrix…" grammatically attaches to "the 2,569,560".
10. **wording** — draft_v2.md:114/224 (B06): Results 4's "(Methods)" now points to a sentence that refers back to Results 4 for the definition.
11. **wording, provenance only** — main_text_numbers.csv:697/699/700 and S3_Text.md:286: −0.79, [−1.60, −0.08] and the partial r's rest on pre-B26 files. Recomputed, they are unchanged.
12. **wording** — S3_Text.md:229: "per pair … averaged over pairs" no longer describes how the residual is now computed (B26 rule 1).
13. **wording, bookkeeping** — the JSON has no B14–B19, though the record cites "B01–B66".

=== FULL CONTENT FOR SP/b36/r22/audit/findings_T.md ===

# Audit T: B26's numbers in the revised text (rule (ii)), the exclusion statements (rule (iii)), the numbers table and the word count

**Audited:**
- SIM = `b36/r22/sim` at HEAD 6ae1cfa, against 31f1153 (B26's outputs) and d5a65bd (before the revision).
- `text_replacements_2026-09-30.json` and `b36/ev/b26_evidence/b26_changes.txt`.

Everything below was recomputed from the files; none of the revision's own claims were relied on. Line numbers are HEAD's.

## Findings (most severe first)

**1. manuscript/si/S3_Text.md:274 (B32) — inaccuracy**
- **What is wrong:** the text has "(+0.01153 − 0.00267 = +0.00887)", but the printed subtraction gives 0.00886.
- **Evidence:**
  - Residual DiD: 0.0115342293 (`partB/inference_revision.csv` l. 231).
  - B17b's condition (i) W = 60 expectation: 0.0026692400, the mean of the 50 replicates in `calibration_filtered.csv`.
  - Excess: 0.0088649893, which rounds to 0.00886.
  - +0.00887 is a double rounding: 0.011534 − 0.002669 = 0.008865, then rounded half up.
  - The fractions "0.16–0.19 [−0.12, +0.52]" are unaffected.
- **Fix:** "+0.00886".

**2. manuscript/si/S3_Text.md:274 (B32) — inaccuracy (last digit)**
- **What is wrong:** the text has "+0.00146 [−0.00096, +0.00405] at −2.42 and +0.00165 [−0.00108, +0.00457] at −2.73". Two bounds are off in the last digit.
- **Evidence, with unrounded inputs throughout:**
  - B22's A_other DiD on ts_gsr, from `aligned_directed.csv` with the inverted sign-flip interval of `notes/rev_inference_inverted.py`: −0.00059422 [−0.00166407, +0.00040695].
  - Less B24's expectation, +0.0000088 (mean of the 20 W60 replicates in `bandpassed_expectations.csv`): −0.00060302 [−0.00167287, +0.00039815].
  - Conversions from `diagnostic_alternatives.csv` part (b): 0.01807963/−0.00748490 = −2.41548 and 0.01012459/−0.00370929 = −2.72952.
  - Result: +0.00146 [−0.00096, +0.00404] and +0.00165 [−0.00109, +0.00457].
- **Where the printed values come from:** B32's "why" says the conversions are ratios of S18 (b)'s printed changes (−2.4171 and −2.7278). That method reproduces the printed values only when B24's expectation is subtracted at its printed +0.00001 while B22's values stay unrounded. With the file's +0.0000088, the same method gives +0.00404 and −0.00109 (and +0.00456).
- **Fix:** "+0.00404" and "−0.00109".

**3. manuscript/supplementary.md:1317 (S18 Table, source note) — inaccuracy**
- **What is wrong:** the note says the B23/B24 files are "both at a9d9ca4", and that the re-run there reproduced `diagnostic_alternatives.csv` "byte for byte".
- **Evidence:**
  - Both files now carry the header `git=d5a65bd` (B26's regeneration).
  - Part (b) as printed, including the new brackets and B57–B59's values, comes from that regeneration. 70 cells of part (b) differ from the earlier file (`b26_changes.txt`).
  - B56 made the equivalent fix to S17 Table's note; S18's note was not touched.
  - Data and code availability (draft_v2.md:246) records both runs and is consistent.
- **Fix:** after the a9d9ca4 parenthesis, add "; part (b) as B26's run regenerated them at d5a65bd (S3 Text §6)". Keep "byte for byte" for the a9d9ca4 files only.

**4. manuscript/draft_v2.md:166 (L02, Discussion) — inaccuracy (minor)**
- **What is wrong:** "which excludes the band-passed generator's rate but not the other two" says the interval [−1.13, −0.37] does not exclude the null's rate.
- **Evidence:**
  - The numbers table derives the null's rate as +0.0054/−0.0146 = −0.3699.
  - That lies just beyond the interval's end, −0.3735 (`inference_revision_tables.md` l. 243).
  - The inputs are four-decimal values (`review_v2_residual_null.log`; `derived_r17.out` item 6), so the comparison is within rounding. That is why Results 4 (l. 118) says the interval "ends at the null's", the wording L02 removed.
- **Fix (word-neutral):** "…rate but not the AR(1) generator's, and at the group level…".

**5. manuscript/si/S3_Text.md:225 (B24, the new first paragraph of §6) — wording**
- **(a) The W = 30 clause reads as a complete list but is not one.** It says "at W = 30 the substituted level and the residual DiD on `ts_gsr` move from 1.1062 to 1.1061 and from +0.0182 to +0.0183 (S12 Table)". Six other W = 30 values of S12 also moved at printed precision (supplementary.md l. 316, 318):
  - ts_gsr: residual level −0.0980 → −0.0979; residual-DiD interval [+0.0045, +0.0319] → [+0.0047, +0.0318]; the last column's upper Fisher-z bound −0.523 → −0.524.
  - ts_demean: substituted level 1.0471 → 1.0470; residual level −0.0835 → −0.0834; the substituted DiD's upper bound −0.0529 → −0.0530.
- **(b) "Leaving the four W = 60 pair-windows out"** — there are four on each variant, eight in all:
  - Table 1's DiD and the p come from ts_gsr's four.
  - The cross-half r comes from ts_demean's four.
  - The record's Rule (iii) paragraph (analysis_record.md:8296–8297, "The four W = 60 pair-windows move…") has the same slip.
- **Fix:** "the four W = 60 pair-windows of each variant"; and "at W = 30 several values of S12 Table move in their last digit, among them …".

**6. manuscript/analysis_record.md:8302–8309 (Rule (iii)) — wording**
- **What is wrong:** "except three" (L05, −2 words) is listed among the 24 words "taken out … to stay within the 7,000 words". The same sentence says the check made the phrase untrue, and L05's "why" files it as a correction from the claim-by-claim check.
- **Evidence, by entry:**
  - Exclusion statements: +19 (B03 +9, B04 +4, B06 +6).
  - Check corrections: +2 (Q02 +4, Q05 +4, Q06 −7, Q07 +3, L05 −2).
  - Length cuts: −22 (L01 −8, L02 −6, L03 −1, L04 −7).
  - The total, 6,998 → 6,997, is right either way.
- **Fix:** "the corrections of the claim-by-claim check 2 more (4, less the 2 of 'except three'); to stay within the 7,000 words, 22 were taken out". Alternatively, move "except three" out of the list of cuts.

**7. manuscript/draft_v2.md:216 (L03, Methods, Inference) — wording**
- **What is wrong:** without the label, the sentence has no main verb: "An exact sign-flip permutation over the 14 subjects (…), which assumes …, and a 95 % interval obtained by inverting that test — … — so that an interval excludes zero exactly when p < 0.05."
- **Fix:** "Inference uses an exact sign-flip permutation …" (+2 words, giving 6,999), or restore the label "Inference:" (+1, giving 6,998).

**8. manuscript/draft_v2.md:120 (Table 3 caption; B12, B13) — wording**
- **What is wrong:** the caption's rates do not follow from the table's own columns, and the caption doesn't say why.
- **Evidence:**
  - "−1.58 (Δa_s) and −2.76 (λ) per unit of pair r₁" are S18 (b)'s last column.
  - Since B26 that column divides the residual's change by r₁'s change over the residual's pairs. S18 says so (supplementary.md l. 1415); the caption does not.
  - The table's own columns give +0.0101/−0.00642 = −1.57 and +0.0039/−0.00143 = −2.73. At full precision, with Δr₁ over all 3,000 pairs, they give −1.576 and −2.745.
  - Before B26, the λ rate (−2.727) was the ratio of the displayed columns.
- **Fix:** "… per unit of pair r₁ over the residual's pairs". Captions are not counted.

**9. manuscript/draft_v2.md:61 (Table 1 caption; B02) — wording**
- **What is wrong:** in "all but 4 of the 2,569,560, whose substituted matrix is not positive definite", the relative clause attaches to "the 2,569,560".
- **Fix:** "all but the 4 of the 2,569,560 whose substituted matrix is not positive definite".

**10. manuscript/draft_v2.md:114 with :224 (B06) — wording**
- **What is wrong:** Results 4's definition still ends with "(Methods)". B06 replaced the Methods definition with the existence statement, which refers back to "(Results 4)". The replaced definition read: "keeps a window's two lag-1 autocorrelations, sets its two lag-0 entries to their mean q and replaces its two cross-lag correlations by a_y q and a_x q (S3 Text)".
- **Fix:** drop "(Methods)" at l. 114 (−1 word; l. 118 already points to "the exclusion in Methods"), or point it to S3 Text §6.

**11. manuscript/main_text_numbers.csv:697, 699, 700, and S3_Text.md:286 — wording (provenance; no value changes)**
- **What is wrong:** derived numbers rest on files from before B26, and nothing records that they were recomputed.
- **Evidence:**
  - −0.79 and the Fieller interval [−1.60, −0.08] are sourced to `derived_r17.out` (24 Sep 2026, git=66c6331), computed from the pre-B26 `inference_rows_diag.pkl`, which B26 regenerated.
  - Recomputed with `derived_r17.py`'s `fieller()` on the regenerated pickle: −0.7876 and [−1.6007, −0.0819], unchanged at printed precision.
  - S3 Text's partial r +0.83/+0.86 and +0.69/+0.82 (third review) recompute to 0.831/0.855 and 0.687/0.820, also unchanged.
- **Fix:** no text change is needed. The record's Rule (ii) paragraph does not say these were recomputed, and the table cites a pre-run file. Add a note to the three rows, or regenerate `derived_r17.out`.

**12. manuscript/si/S3_Text.md:229 — wording**
- **What is wrong:** "observed minus AR(1)-substituted sts per pair, subject, run and window, averaged over pairs" no longer describes rule (1), which l. 225 states: the observed mean over all pairs minus the substituted mean over the pairs where it exists.
- **Fix:** "observed minus AR(1)-substituted sts, each averaged over the pairs where it exists (above), per subject, run and window".

**13. text_replacements_2026-09-30.json; analysis_record.md:8272 — wording (bookkeeping)**
- **What is wrong:** the 171 B entries use ids B01–B13 and B20–B66. B14–B19 do not exist, but the record cites "B01–B66".
- **Fix:** say B14–B19 are unused, or renumber.

## Checked and found correct

**The JSON as a whole**
- Replayed in order on 31f1153, preserving CRLF: all 245 entries match their counts and reproduce HEAD byte for byte in all 14 files.
- Every B entry's "why" matches its change.
- All B values match the regenerated files at printed precision, except B32's (findings 1–2):
  - B01–B13: the 14 main-text numbers, the exclusion statements and the Fig 5 caption.
  - B20–B44: S3 Text.
  - B45–B65: supplementary, including S17's 73 rows and S18 (b).
  - B66: `partB5_literature_v2.md`.

**Checker runs**
- `check_numbers.py`: 1,196 rows, 670 data rows, exactly 12 "SIGN DIFFERS". These are the same 12 quantities as at d5a65bd (1,183/666/12).
- `check_cells.py`: 0 flagged.
- `tablecheck.py`: 0 bad rows in draft_v2, S1–S5 Text, supplementary and partB5_literature_v2. The record's 5 bad rows at l. 2516–2520 predate the revision.
- `wc.py`: 6,997 words with headings, 6,877 without; at d5a65bd, 6,998 / 6,878.

**Main text**
- All data rows agree with the regenerated sources.
- Table 1: 17 rows; only the TDMI substituted DiD changed (−0.1129 → −0.1130).
- Table 3 rows 6–11: every cell agrees at full precision.
- Derived values check out: −0.74, −0.18, −0.39, −0.37, 0.0115, "10 of 14", 2,980–2,995, and 12.5 %.
- The Fig 1–4 and Fig 6 captions are identical to `captions_v2.md`; Fig 5's differs only by the removed p values.

**Supporting information**
- S3 Text tables: the §1 ts_demean table (17 rows); the §5 BCa table (27 rows plus its inverted column); the §6 B22 table (20 rows); B15's five null lines; the §7 tables (21 + 21 + 3 rows).
- S3 Text prose:
  - Early, late and FD-residualised values; run changes; placebo share 0.33.
  - Split-half values; the B43 ratios.
  - §8 (B44); the ts_demean conversions; −2.42, −1.72, −2.73 and "about −40".
- Supplementary tables:
  - S10 (45 rows) and S12 (7 rows, intervals at full precision).
  - S17: all 932 rows. The note is also right: 40 changes, the 40th row 399, 31 others; ratio range 1.039–1.288, 929 in 1.072–1.191, 6.7–16.1 %.
  - S18 (b) (13 lines); the S11 and S13 notes.
  - S19 rows B4, B7, B17 (ii)/(iv), B22 (c), B23 (b) and B26.
  - S20 Table B item 1, identical to `partB5_literature_v2.md`.
- A search of all texts for every changed value found no stale old value.

**Exclusion statements (task 3)**
- Counts agree with `diag_tables.md` l. 6/18/30/42 and with `positive_definite.csv`: B4's 3,286 = 4 + 1,617 + 4 + 1,661; B16's 26,593 = 10,817 + 15,776.
- Run totals: 473,262,025 matrices, 42,681 not positive definite, 12,889 nearly singular, 13,529 s.
- The positive-definiteness condition holds on 200,000 random matrices (0 mismatches).
- Before-values at d5a65bd: −0.1129, 0.2188 → 0.219, −0.052.
- The p's move comes from the data, because B21's expectations are constants (`partB21_inference_revision.py` l. 87). So "before the exclusion in Methods" is right.
- B02, B03, B04 and B06 agree with B24 and with the record; B13's 2,980–2,995 agrees with S18's brackets.

**Numbers table (task 4)**
- Rows: 22 added, 9 deleted, 14 values changed, 16 locators moved, 101 contexts updated.
- Every number the revision added to the main text has a row, and no removed number keeps one. Sources and held strings are correct.
- Occurrences are consistent across 920 groups, and the table's conventions are kept.
- Not reproduced exactly: the head note's "65 held strings" and "16 notes". My mapping gives 61 and 15 on existing rows, plus the new rows.

**Word count (task 5):** each entry's word change sums to the record's totals (19, 4 and 24), giving 6,998 → 6,997; only the classification in finding 6 is off.

=== END OF CONTENT ===

**Side effects:**
- No tracked file was modified (`git status` in SIM is clean).
- I created working files under `SP/b36/r22/audit/`: `_T/`, `_T_check_numbers.out`, `_T_check_cells.out`, `_T_tablecheck.out`, `_T_wc.out`, `_T_json_list.txt` and `_T_rec_old.md`. They can be deleted.
- Importing `rev_inference_inverted` most likely created one git-ignored cache file, `SIM/notes/__pycache__/rev_inference_inverted.cpython-311.pyc`. It is harmless and I left it in place.
