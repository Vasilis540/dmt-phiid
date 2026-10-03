# VO — verification of the four outcome entries (B27, B28, B29, B16c)

Scope: `manuscript/analysis_record.md` lines 8875–9129 at HEAD (9caa60b), against the committed outputs, the evidence of the run, the pre-run entries, and the places of the paper the entries name. Nothing under VT was changed. Scratch scripts and outputs are in `VW/VO/` (a `git archive` copy of HEAD is in `VW/VO/tree`).

**Result in one line:** no number, sign, verdict, count or quoted value in the four entries is wrong. I found 4 inexact statements and 9 notes; none is graded `error`.

## Findings

**VO-1**
- Where: `analysis_record.md`, "B28, outcome", first paragraph (lines 8971–8972): "The run read no data but the subjects' whole-brain r₁ DiDs, from the committed `inference_rows_raw.pkl` and `inference_rows_diag.pkl`."
- Problem: B28 reads three committed data-derived inputs, not one. The r₁ DiDs come from `inference_rows_raw.pkl` alone; `inference_rows_diag.pkl` supplies the residual DiDs (for the data's slope and r); and the AR(1) conditions draw q from B17's pool of the data's window-level pair q, which the sentence leaves out. S18 Table's B28 source line repeats the narrower statement ("No data but the subjects' whole-brain r₁ DiDs").
- Evidence: `notes/partB28_matched_slope.py` lines 77–78 (`scope_map_overlay_points.npz`, key `pre_w1to4_q`, 52,440 values), 98–99, 228; the pre-run entry, record lines 8673–8676, names all three; `run_all.sh` line 179 ("the saved r₁ DiDs and B17's pool of q"); `supplementary.md` line 1590.
- Grade: inexact

**VO-2**
- Where: "B16c, outcome", (e) (lines 9114–9115): "CCS-sts, the global-fit contrasts, xtx + yty and the diagnostic on the whitened series are in the tables file". Same statement in `S3_Text.md` §8 (line 540) and in S19 Table row B16c (e) (`supplementary.md` line 1687, outcome cell "S11 Table and `prewhiten_fixed_tables.md`").
- Problem: `prewhiten_fixed_tables.md` has no xtx + yty entry; xtx and yty are separate rows of each atom table. The contrast of the sum that the script computes (label "MMI xtx+yty", with p and count) is only in `inference_rows_prewhiten_fixed.csv`/`.pkl` and `derived_r24.out` item 1. S11 Table has no xtx + yty row for p = 10 or 20, and no manuscript file reports it.
- Evidence: no match for "xtx+yty" or "xtx + yty" in `prewhiten_fixed_tables.md`; CSV label kinds (8 "MMI xtx+yty" labels); `derived_r24.out` (e.g. ts_gsr W60: −0.0229, p = 0.0077 at p = 10; −0.0060, p = 0.0037 at p = 20); S11 rows at `supplementary.md` lines 284–307 are MMI-sts, CCS-sts and autocorrelation only.
- Grade: inexact

**VO-3**
- Where: "B27, outcome", "The script's closing paragraph" (lines 8942–8943): "paraphrases the predictions as they stood before the audit of the prepared commit (…), which the audit restated to the criteria above (its item 3)".
- Problem: The audit restated nothing. Its item 3 reports that the group means of the r₁ gaps follow from committed rows and that the clauses "should be labelled as known". The restatement is the writer's disposition of that finding.
- Evidence: `notes/review_2026-10-01_cold_reads/audit/findings.md` item 3; `audit/dispositions.md` item 3 ("Applied: … predictions (a) and (b) are restated to what is open").
- Grade: inexact

**VO-4**
- Where: `S3_Text.md` §5, line 231: 'Record, "The pre-injection gap and the per-subject relations (B27): pre-run entry" and "B27, outcome" (1 October 2026)'; the same form at line 264 (B29) and §6 line 393 (B28).
- Problem: The three outcome entries are dated 2 Oct 2026 18:40 UTC; only the pre-run entries are of 1 October. Elsewhere S3 Text puts each entry's own date after its title, and S11 and S18 Tables give "1–2 Oct 2026" for the same pairs.
- Evidence: record headings at lines 8875, 8968, 9028; `supplementary.md` lines 256 and 1590; S3 Text's other citations (e.g. 'record, "B17b, outcome", 21 September 2026').
- Grade: inexact

**VO-5**
- Where: "B27, outcome", "The run" (line 8890): "the unit ran on battery to its end".
- Problem: The heartbeat shows the charger disconnected in every line from 23:57:10 to its last line at 00:32:10. No line covers the remaining 178 s to the end at 00:35:08, so the statement is an inference for that stretch.
- Evidence: `b27/b27_heartbeat.log` line 11; `b27/evidence.txt` line 3.
- Grade: note

**VO-6**
- Where: "B27, outcome", "The outputs" (lines 8902–8903): "The values the pre-run entry lists as known (item (i)) are reproduced by the run at the printed precision (the sts rows of (a), the sts correlations of (b), and (c))."
- Problem: The statement is true, but the parenthesis is narrower than item (i), and nine of its values are not printed in the tables file.
  - Item (i) also lists AR(1)-substituted and residual rows of (a) and r(residual pre gap, r₁ DiD); the tables reproduce these too.
  - Not printed in `baseline_gap_tables.md`: r² = 0.79, the SDs 0.0887 and 0.0485, subject 14's +0.0949, −0.1121 and −0.0172, subject 8's −0.2795 and +0.0914, and the intercept +0.0005. They follow from `baseline_gap.csv`.
  - The ratio of means −0.788 is printed by B28's tables, not B27's.
- Evidence: record lines 8604–8628; my recomputation from `baseline_gap.csv` (`VW/VO/b27_recompute.out`) reproduces all of them; `matched_slope_tables.md` line 6.
- Grade: note

**VO-7**
- Where: "B27, outcome", item (ii) (line 8953): 'with one word changed from the rule's "in the same words"'.
- Problem: Only within the quoted phrase does one word differ ("creates" / "enlarges"). The two sentences differ further: S2 Text has "a pre-injection baseline gap in the direction that creates it"; Results 2 has "the runs' pre-injection gap … lies in the direction that enlarges the DiD".
- Evidence: `S2_Text.md` line 9; `draft_v2.md` line 87.
- Grade: note

**VO-8**
- Where: "B27, outcome", item (iv) (line 8962): 'every "not distinguished" statement (Abstract, Results 4, Discussion)'; "B28, outcome", item (iv) (line 9025): '"not identified" stays'.
- Problem: Neither quoted phrase occurs in the Abstract. It says "a test detecting 0.0155 does not resolve this" and "its source is unidentified". "not distinguished" is in Results 4 and the Discussion; "not identified" is in Results 4 and the Discussion. The Abstract does carry the content (0.0155 beside 0.006–0.009).
- Evidence: `draft_v2.md` lines 15, 124, 142, 183.
- Grade: note

**VO-9**
- Where: "B28, outcome", item (i) (lines 9020–9021): "the three rates of the residual table stay as the group-level comparison with its Fieller interval".
- Problem: The pre-run rule says the comparison with the rates "stays only as the group-level comparison". In the text the rates also stand against the data's per-subject slope: Table 3's rows 2–3 count the leave-out t intervals that contain −0.18, −0.39 and −0.37 (required by B27's rule (iv)), and Fig 3c draws the three rates on the per-subject panel. The entry drops "only" without saying the two rules pull apart.
- Evidence: record lines 8742–8743 and 8660–8661; `draft_v2.md` lines 131–132 and 110.
- Grade: note

**VO-10**
- Where: "B28, outcome", item (iii) (lines 9022–9023): "The subject at the floor is named where the band-passed conditions are reported (Table 3's caption; S3 Text §6)."
- Problem: The two places named do name subject 8. S18 Table's B28 section also reports the two band-passed rows and does not name the floored subject or the floor; it points to S3 Text §6.
- Evidence: `supplementary.md` lines 1588–1597; `draft_v2.md` line 126; `S3_Text.md` line 393.
- Grade: note

**VO-11**
- Where: "B28, outcome", item (v) (line 9026): "S18 Table its slope columns"; S19 Table row B28 (d), "reported at": "S3 Text §6; S18 Table".
- Problem: S18's B28 table has 11 of the 14 columns, not only the slope columns. It omits the r percentiles, the share with r ≤ the data's, and the ratio's percentiles. So the shares of r that row B28 (d) reports (0.190, 0.070, 0.370, 0.280) are in S3 Text §6 only.
- Evidence: `supplementary.md` lines 1592–1597 and 1678; `matched_slope_tables.md` line 8.
- Grade: note

**VO-12**
- Where: "B16c, outcome", (e) (lines 9115–9116): "(the diagnostic at W = 60 on ts_gsr: residual +0.0564 at p = 10 and +0.0624 at p = 20 …)"; S11 Table's Note (`supplementary.md` line 331).
- Problem: The numbers are the tables file's, but they are means over both runs and all 14 windows, while the file's header and S11's column define "level" as DMT pre-injection. The pre-injection residuals are +0.0511 and +0.0605. S3 Text §8 states the difference; the entry and S11's Note do not, and S11's sentence puts them beside the pre-injection levels 0.0866 and 0.0719.
- Evidence: `notes/partB16c_prewhiten_fixed.py` line 184 (`np.nanmean(R['obs'])` etc.); CSV `pre_dmt` of the "diag residual sts ts_gsr W60" rows; the all-window mean of the saved array is 0.0861 and 0.0705.
- Grade: note

**VO-13**
- Where: "B27, outcome", item (vi) (line 8966): "S3 Text §5 transcribes the tables".
- Problem: Tables (a) and (b) are transcribed cell for cell. For (c), the last column of the three named rows is not carried: r(sts DiD, r₁ DiD) = +0.921, +0.931, +0.846 without subject 8, without 14, without both. +0.931 occurs in no manuscript file; the other two appear only as range ends.
- Evidence: `baseline_gap_tables.md` lines 39–41; `S3_Text.md` line 258.
- Grade: note

## Checked and found exact

**1. Numbers, entry against output**
- Every numeric token of every paragraph of the four entries was extracted by script and looked up; each sentence was then read for attachment.
- Field-by-field structured comparison, 0 differences:
  - B27 (a), (b), (c), (d) and the sts row against `baseline_gap_tables.md`;
  - B28's four conditions (26 fields each) against `matched_slope_tables.md`;
  - B16c's eight cells (9 fields each) against `prewhiten_fixed_tables.md` and `derived_r24.out` item 1.
- B27's (c) block (ranges, the 0/0/11/11 and 1/13/71/63 counts in the right order, the three omissions, SE 0.0051, 0.0155, the excesses, g 0.611 twice, −0.01465, 0.00530) and all of B29 (a)–(d) were checked by reading against the tables.
- The values B16c quotes from B16 and B16b match `prewhiten_tables.md` and `whitened_spectrum_tables.md` (0.2202, 0.2350, 0.1042, 0.1306, −0.0262, +0.495, +0.899; 0.1368, 0.0739, 0.0524, 0.0323).

**2. Recomputed from committed files**
- `baseline_gap.csv` (168 rows, 12 cells × 14 subjects): all of table (a), (b) and (c) reproduce. One fourth-decimal difference is rounding only: the r₁ ts_demean pre-gap p is 0.1873 from the six-decimal CSV against the table's 0.1871 (one symmetric pair of assignments lies within 10⁻⁷ of the threshold).
- Also from that CSV: the SDs 0.0887, 0.0485, 0.0524; r² = 0.79; the intercept +0.0005; the sts slope 4.263 with leave-one-out 4.139 (without 14) to 4.535 (without 8).
- `matched_slope.csv` (400 rows, 11 fields under a 10-column header): all 4 × 13 cells; means +0.002182, +0.002034, +0.004851, +0.004232; differences 0.000148 and 0.000620; no replicate slope at or below −0.753 in any condition.
- `censoring.csv` (392 rows) with `inference_rows_raw.pkl`: every cell of (a), (b), (c), the per-window lines, 473 TRs above threshold, and +0.0935 as the largest mean-FD DiD.
- B16c: the sixteen arrays reproduce all 136 atom-table rows. The pickle reproduces levels, DiDs, inverted intervals, exact p (equal to the CSV's `did_p`), negative counts and correlations of the eight cells. 264 rows = 44 labels × 6 sets = 192 + 72.
- An independent inversion of the sign-flip test reproduces ten of the intervals.
- `derived_r24.py`, re-run in the copy, gives output identical to `derived_r24.out` apart from the git header line.

**3. Predictions, by the criterion alone**
All verdicts and the reasons given agree with the pre-run criteria:
- B27 (a), (b), (c) met; (d) six uncounted readings, all met.
- B28 (a) met (−0.2001 < −0.1665; −0.3548 < −0.3495 unrounded); (b) met, four of four; (c) met; (d) no prediction.
- B29 (a) partly met (7 of 14 fails the count clause; 8 of 14 meets the FD clause); (b) missed; (c) no prediction; (d) confirmed on ts_gsr.
- B16c (a) check, equal in four cells; (b) met; (c) missed (p = 0.0002 at p = 20); (d) met; (e) no prediction.

**4. "The run" paragraph**
- Commit 13e7299; clean tree (prestatus 0 lines); start 23:37:10 local, +0300; last step at 00:01:08 plus 2,040 s gives 00:35:08; log last written 00:35:10; 20:37:10–21:35:08 UTC; 3,478 s.
- Versions 3.12.3 / 2.5.3 / 1.18.1 / 3.11.1, matching `requirements.lock.txt`; data clone 77af7aa.
- Durations 7, 1,428, 1, 2,040 s. Exit 0 for every step (no "=== step" line, "=== unit exit 0", no traceback).
- 11 heartbeat lines, 8 disconnected from line 4 (23:57:10), line 3 connected, battery 99 % to 83 %, largest gap 300 s.
- The inhibitor and the charger requirement are in `b27_start.sh`; the checks named are in `b27_commit.sh`.
- 29 outputs with sha256 equal to `outputs.sha256`; exactly the twelve text outputs carry `git=13e7299`; the unit log is the four run logs plus step and exit lines; the four scripts are unchanged since 13e7299 and match the hashes in `b27_start.sh`.
- Not verifiable from the tree: "The writer's session noted the difference on 1 October 2026 before the run".

**5. "What the text says"**
Every item of the four paragraphs was read against the place named, and the values there are right: Table 2 and its caption; Results 2; Results 4 and Table 3 with caption; Results 7 and Table 4; Abstract; Author summary (one and two risers); Discussion; Recommendations; Limitations; Methods (Dataset, Inference); S1 Text; S2 Text; S4 Text (D4, P6, P8, the five documents); S3 Text §5, §6, §8; S11, S18, S19.
- Quoted phrases occur word for word where the entry places them, except as in VO-8.
- The three replaced sentences are absent at HEAD and were present at 8bd189e.
- 221 numbers-table rows that cite the new output files point to the right line with the right value.

**6. Record rules**
The old file is a byte prefix of the new one (556 added lines, 0 removed). No added non-heading line exceeds 120 characters (maximum 120, counted in characters). All five headings have the required form.

**7. Consistency**
- S19 rows B27 (a)–(d), B28 (a)–(d), B29 (a)–(d), B16c (a)–(e): criterion, value and verdict agree with the entries and outputs, except the pointer in VO-2.
- S3 Text transcriptions, 0 differences: B27 (a) 12 × 13 and (b) 3 × 10 cells; B29 (a) 15 × 6, (b) 2 × 6 and the four per-window lines; B28 4 × 14; the B16c table 8 × 11.
- S18's B28 table (4 × 11) and all 48 rows of S11 Table: 0 differences.
- Verdicts in S3 Text agree with the entries.
- Methods count: S19 Part A has 81 rows, of which 36 met, 15 partly met and 16 missed (67), and 14 not counted, as its closing sentence itemises. No old row's verdict changed since 8bd189e (56 = 28/14/14, plus 8/1/2).
