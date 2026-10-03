# W3 — the supplementary tables, S4 Text, S5 Text and the literature file (HEAD eed9271 of VT against `checked`, 9caa60b)

Files verified: `manuscript/supplementary.md`, `manuscript/si/S4_Text.md`, `manuscript/si/S5_Text.md`,
`notes/partB5_literature_v2.md`, and the dispositions named in the task
(`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`, last part).

Nothing under VT was changed (`git diff HEAD` empty and no untracked file at the end). Scratch is in VW/W3/: the
word and character diffs of the four files, the page texts of Luppi2026.pdf, Down2026.pdf and page 1 of Luppi2025.pdf,
the images and an OCR of Luppi2026.pdf pp. 33–41, the scripts used, and a copy of `derived_r24.py` with the thirteen
committed files it reads, on which it was re-run. No internet, no subject data.

**Result in one line.** No number, page, count or quoted phrase of the delta is wrong, and all 29 dispositions and the
paragraph "Found while the findings were settled" name corrections that are in the files, with every quoted phrase at
its place word for word. Twelve findings: 6 graded `inexact` (three pointers or statements of the manuscript files that
the corrections wrote, one "reported at" cell with the gap of VT2-8 that the corrections did not reach, and two
statements of the dispositions file) and 6 `note`. No finding is graded `error`.

## Findings

**W3-1**
- Where: `manuscript/supplementary.md`, S19 Table, head note (line 1601): "B21 (b) and (c), the residual's exact p
  against its three expectations and the per-subject regressions (main text, Abstract, Results 2 and 4, Table 3 and
  Fig 3)" and, for B27's values, "(main text, Tables 2 and 3 and Results 2 and 4; S3 Text §5)".
- Problem: the two lists of main-text places are not complete. Values of the second set are also in the Abstract and in
  the Discussion: the baseline-adjusted contrast (−0.054) and the test's sensitivity (0.0155, beside the excesses
  0.006–0.009) in both, the partial correlation (+0.82) in the Discussion. One value of the first set, the residual's
  per-subject slope (−0.75 per unit), is also in the Discussion. The first list names the Abstract, the second does
  not, and neither names the Discussion. (The dispositions of VT1-7 and of "Found while the findings were settled" say
  that the head note names where the main text has the two sets.)
- Evidence: `manuscript/draft_v2.md` line 15 ("−0.054 adjusted for the runs' pre-injection gap"; "a test detecting
  0.0155"); line 183 ("−0.054 adjusted for the runs' pre-injection gap"; "partial r = +0.82 given the sts
  pre-injection gap"; "a test that detects 0.0155"; "at −0.75 per unit"). `manuscript/analysis_record.md` lines
  8608–8628 list −0.0544, +0.824, 0.0155 and the excesses as known before B27's run, and lines 5922–5923 the slope
  −0.753 (B21 (c)). `manuscript/main_text_numbers.csv` gives these rows of the Abstract and of the Discussion the notes
  "B27 (a)", "B27 (b)", "B27 (c)" and, for −0.75, line 243 of `inference_revision_tables.md`.
- Grade: inexact

**W3-2**
- Where: `manuscript/supplementary.md`, S19 Table, row "B24, the pure-autocorrelation expectations" (line 1664),
  reported at: "S3 Text §6 (its residual table, and the paragraph after it for A_other's expectation); S18 Table".
- Problem: at HEAD the paragraph after the residual table of S3 Text §6 is the sentence on the caption's −0.74, which
  the same pass added there (the correction of VT1-9). A_other's expectation as the text states it, "+0.0000 ± 0.0003",
  stands two paragraphs further, under the next heading. (In `checked`, before that sentence was added, the table was
  followed directly by the heading.) For the rest the cell holds: the residual table's third row has the value as
  +0.00001 ± 0.00031; the expectations of A_other, A_same, B and D are also in the last column of §6's table of the
  aligned and directed statistics (lines 351–355) and in the paragraph under it (line 372); the identity for Sym
  (−0.00006) is in S18 Table only.
- Evidence: `manuscript/si/S3_Text.md` line 337 ("The caption's −0.74 per unit of pair r₁ for the data's group means
  is the ratio of the two means …"), line 339 (the heading "### The residual's response to changes in lagged structure,
  the aligned statistic and the directed part …"), line 343 ("… against +0.0000 ± 0.0003 under a pure autocorrelation
  change on the band-passed generator"); `git show checked:manuscript/si/S3_Text.md`, lines 335–337.
- Grade: inexact

**W3-3**
- Where: `manuscript/si/S4_Text.md`, S6 (line 53): "the supporting texts label every post hoc or review computation
  where they report it, and the main text repeats the status for several (Methods, The primary contrast and the
  exploratory analyses)".
- Problem: the first clause does not hold of every one. S3 Text §5 reports the leave-two-out on the sts /
  autocorrelation collinearity, a post hoc computation of S19 Table's Part B ("entered with no prediction"), with its
  log named and no word on its status; the status is said in S5 Text §1 and in S19 Table. Numbers of the two derived
  outputs are likewise reported in S3 Text with the output named and no status (§4: `derived_r17.out`, item 4; §5:
  `derived_r24.out`, items 2, 8, 9 and 11; §6: item 5; §8: items 1 and 6), where items 7 and 10 of `derived_r24.out`
  and item 2 of `derived_r17.out` are labelled.
- Evidence: `manuscript/si/S3_Text.md` line 165 ("Dropping every pair of subjects in turn (91 refits) gives r = 0.846
  to 0.973 … (`notes/review_results/partB/leave_two_out.log`)"); `manuscript/supplementary.md` line 1701 (the Part B
  row); `manuscript/si/S5_Text.md` line 7 ("entered in the record with no prediction before it was run");
  `S3_Text.md` lines 130, 260, 404, 531 and 544 against lines 132, 169 and 406.
- Grade: inexact

**W3-4**
- Where: `manuscript/supplementary.md`, S19 Table, row "B21 (d), the Fisher-z intervals and the disattenuated ratio"
  (line 1647; not changed between `checked` and HEAD): "| partly met | Results 2; S3 Text §5 |".
- Problem: the gap that VT2-8 found in three cells is in this one too. The row's value, the disattenuated ratio
  (+0.951), is quoted in the Abstract and, new in this revision, in the Discussion, in both beside the cross-half
  correlation, whose row B19 (c) was corrected to "Abstract; Results 2; Discussion; S3 Text §5; Fig 3". For the
  record, cells that the revision did not touch have the same form for values that the Abstract or the Discussion
  already quoted at 8bd189e: B22 (d) (4.7 per within-window SD; Abstract and Discussion), B4 (0.0115; Abstract and
  Discussion), the regional sts–r₁ test (r = 0.86; Abstract), B17 (i) and B17b (i) (the Discussion's 0.003–0.005),
  while the cells of B19 (c), of B24's check and of B28 (b) now name the Abstract and the Discussion.
- Evidence: `manuscript/draft_v2.md` line 15 ("cross-half r 0.69 [0.26, 0.89], disattenuated 0.95") and line 183
  ("cross-half r = 0.69, disattenuated 0.95"); `git show 8bd189e:manuscript/draft_v2.md`: the Abstract has
  "disattenuated r 0.95 [0.62, 0.99]" and the first subsection of the Discussion has no 0.95;
  `main_text_numbers.csv` sources both 0.95 to line 284 of `inference_revision_tables.md` ("disattenuated +0.951").
  `supplementary.md` lines 1619, 1623, 1631, 1642 and 1651 for the older cells.
- Grade: inexact

**W3-5**
- Where: `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`, VN-1 (line 1440): "The second form of
  the citations audit's report lists the same ranges (the part above on the points it raised outside its findings)."
- Problem: the report does not list them. It names one page reference, the mice's, and of the rest says only that
  five ranges are wider than the pages that hold the facts and that it does not count them as inexact. Which five it
  meant cannot be read from it. (The narrowing itself is right: see "Checked and found exact".)
- Evidence: `audit/findings_citations.md` line 226: "where the cell gives "(pp. 4, 38–40)"" and "five page ranges of
  row 5 are wider than the pages that hold the facts, each fact lying within its range"; no other line of that file
  holds one of the ranges (search for 37–39, 38–39, 38–40, 37–40).
- Grade: inexact

**W3-6**
- Where: the same file, VM-8 (lines 1532–1534): "the file's titles carry bins (S1), a section reference and a time of
  day (S9) and computation labels (S17, S18), which the main text does not use, and the list's entries give the same
  contents without them."
- Problem: the reason holds for the time of day and for the computation labels, not for the other two. The main text
  uses bins and it uses section references to S3 Text. That the four titles are the committed ones and that the list's
  entries give their contents is right.
- Evidence: `manuscript/draft_v2.md` before "## Supporting information": line 237 ("Pre-injection windows are 1–4 (bins
  1–8), post windows 6–14 (bins 11–28)"), line 116 ("bins 1–8"), five occurrences of "bins" in all (lines 116, 187,
  217 and 237); 31 references of the form "S3 Text §n"; no "UTC" and no computation label. `git show 8bd189e:manuscript/supplementary.md` lines 5,
  155, 374 and 1315 for the four titles.
- Grade: inexact

**W3-7**
- Where: `manuscript/supplementary.md`, S19 Table, Part B, the row of `derived_r24.out` (line 1706): "Results 2 (r² and
  the SDs of the DiD and of the post-injection gap; the share of reliable variance at the disattenuated interval's
  lower limit; the FD-residualised r₁ DiD)".
- Problem: the gloss names every number of Results 2 that the numbers table sources to the output, but it no longer
  names the two shares that Results 2 states in words from item 4, "a fifth" and "a sixth" (0.197 and 0.163), the
  first of them again in the Discussion. The row as checked named them ("the shares the FD residualisation removes").
- Evidence: `checks/derived_r24.out` lines 47–48 ("removed 0.197 of the DiD"; "removed 0.163 of the DiD");
  `manuscript/draft_v2.md` line 106 ("removes a fifth of the sts contrast … and a sixth of r₁'s (−0.0123)") and line
  187 ("removes a fifth of the sts contrast"); `git show checked:manuscript/supplementary.md` line 1706.
- Grade: note

**W3-8**
- Where: the same row, last cell: "Computed from committed per-subject vectors, tables, CSV files, arrays and a log,
  with no pre-run entry and no random numbers".
- Problem: the script reads one array file, as it reads one log. The other kinds are right: two pickles of
  per-subject vectors, two tables, six CSV files, and no random draw.
- Evidence: `checks/derived_r24.py`: the only `np.load` is at line 168
  (`regional/regional_atoms_raw_ts_gsr_win60.npy`); `pickle.load` at lines 45 and 149; the tables at lines 94 and 268;
  the log at line 224.
- Grade: note

**W3-9**
- Where: `manuscript/supplementary.md`, S18 Table, B28, source line (line 1590): "S3 Text §6, which transcribes the
  table in full, the r percentiles and the share of replicates with r at or below the data's among its columns".
- Problem: true as written. S18 Table's part has eleven of the result file's fourteen columns and leaves out three;
  the line names two of them. The third, the 2.5th, 50th and 97.5th percentiles of the per-replicate ratio of means, is
  not named (the record's "B28, outcome", item (v), names all three).
- Evidence: `notes/review_results/partB/matched_slope_tables.md` line 8 (fourteen columns); `supplementary.md` line
  1592 (eleven); `S3_Text.md` line 397 (fourteen); `analysis_record.md` lines 9038–9040.
- Grade: note

**W3-10**
- Where: `manuscript/si/S4_Text.md`, R1 (line 62): "The exceptions are the atom DiDs of Table 1, which carry the number
  of negative subjects, and the contrasts whose per-subject values were not saved".
- Problem: the clause that the correction of VS-5 added is right (see below), but the list of exceptions is not
  complete for the main text at HEAD. Results 2 gives one contrast that this revision adds as a point value with
  neither interval nor p, the FD-residualised r₁ DiD (−0.0123), whose interval and p are in S3 Text §4. Older ones of
  the same form: the r₁ DiD without global signal regression (−0.0216), the early and late residual DiDs (+0.0179,
  +0.0064), and, with p and no interval, the W = 30 contrast (−0.0686) and the contrasts at τ = 2, 3 and 5 of Results 5.
- Evidence: `manuscript/draft_v2.md` lines 106, 120, 87 and 146; `git show 8bd189e:manuscript/draft_v2.md` has no
  "0.0123"; `manuscript/si/S3_Text.md` line 161 ("FD-residualised −0.0123 [−0.0210, −0.0031], p = 0.0135").
- Grade: note

**W3-11**
- Where: `notes/partB5_literature_v2.md`, the search paragraph (line 7, to which the delta adds its last clause): "On
  20 Sep 2026 all nine studies were read in full from the publishers' or preprint servers' PDFs saved by V.S."; the
  file's title: "every cell verified against the PDF"; S20 Table's head note (`supplementary.md` line 1711): "revised
  from the full texts on 20 September 2026".
- Problem: row 6 of the same table now says that the copy of Down et al. (2026) holds pages 1–25 of the preprint's 55
  and that its supplementary materials were not read. The three statements stand beside it without that
  qualification. (S5 Text §5 has it in general form: "main article; supplementary materials only where named".)
- Evidence: Down2026.pdf: 25 pages, each numbered "n/55"; references from p. 20 to their end on p. 25; the file's row 6
  (line 18).
- Grade: note

**W3-12**
- Where: `dispositions_revision.md`, VR-14 (lines 1246–1248): "The three say that the study was found by the search of
  1 October 2026 and read in full on that date, and that the row was added in the revision of 1–2 October 2026".
- Problem: true of S20 Table's head note and of S3 Text §10. The literature file's title says the second part only.
  The first part is in that file's search paragraph, whose sentence, not changed by the correction, still reads as one
  date for both acts.
- Evidence: `notes/partB5_literature_v2.md` line 1 ("with row 10 added in the revision of 1–2 October 2026") and line
  7 ("On 1 Oct 2026 V.S. ran the PubMed search … one, Gao et al. (2026), is a study in scope, read in full from
  V.S.'s copy on that date and added as row 10").
- Grade: note

## Checked and found exact

**1. The delta.** Every changed line of the four files was taken from a character-level comparison of `checked` and
HEAD (26 lines of `supplementary.md`, 3 of S4 Text, 3 of S5 Text, 4 of the literature file); each changed or added
statement was read against its source.

*The head note of the supplementary tables.* "the results of B21–B24 and of B28 (S18 Table)": B28's part is the last
section of S18 Table, and it is the only section or table of S12–S20 that the revision adds for a computation. B27,
B29 and B16c are named in S12–S20 only in S19 Table (B16c's rows are in S11 Table); B26 is named in the notes of S12,
S17 and S18, and B25's values stand in S19's rows and S20's row 2, as before the revision.

*S11 Table.*
- Source line: B16c's pre-run entry is of 1 Oct 2026 (record line 8816) and its outcome entry follows (line 9089).
- The line at p ≤ 5 and the note: the diagnostic's levels are `np.nanmean` over an array of 14 subjects × 2 runs × 14
  windows (`notes/partB16_prewhiten.py` line 205; `notes/partB16c_prewhiten_fixed.py` line 184). Recomputed from the
  committed arrays: 0.2766 over both runs and all windows against 0.2202 over the DMT pre-injection windows at p ≤ 5;
  0.0861 against 0.0866 at p = 10; 0.0705 against 0.0719 at p = 20.
- The values of the two sentences equal `prewhiten_tables.md` line 29 and `prewhiten_fixed_tables.md` lines 28–29 and
  126–127 (0.2766, 0.2438, +0.0328; −0.0262, −0.0181, −0.0080, 8/14; +0.0564, +0.0624; −0.0091, −0.0090; 11 and 12 of
  14; +0.445, +0.333).

*S18 Table, B28.*
- The script's inputs are the three the source line names and no other file: `inference_rows_raw.pkl` (the r₁ DiDs,
  line 98), `inference_rows_diag.pkl` (the residual DiDs, line 99) and `partB/scope_map_overlay_points.npz`, key
  `pre_w1to4_q` (line 77; 52,440 finite values; drawn from in the AR(1) conditions only, line 228). The other
  data-derived quantities are constants in the code.
- Subject 8 at the floor: result file line 4; S3 Text §6 line 395.
- "the SD with divisor 100": `SL.std()` and the like, NumPy's default divisor, over 100 replicates (lines 244–245).
- The table: 4 rows × 11 cells equal the result file's cells, and S3 Text §6's table equals it in all 4 × 14 (script,
  0 differences). The record's two entry titles are word for word.

*S19 Table.*
- Head note, against the record. B23: the pre-run entry lists what was "Already computed on 22 Sep, on other pools or
  designs" and says that B23 recomputes each (lines 6151–6155); the outcome entry reads each part against its
  prediction (lines 6489–6528; for (a1) in the words "as predicted"); the ten rows of B23 carry verdicts and are among
  the 67. B21: (b) and (c) are listed as "Known" (lines 5921–5925) and reported as "(reproduced)" (lines 6335–6336,
  6358–6365). B27: item (i) of "What is known before the run" (lines 8604–8629, "not predictions") and the outcome
  entry (lines 8902–8907, 8931–8943). The kinds of values the head note names for B27 are those of item (i). The places
  it names do hold them (Table 2, Table 3 rows 2–6, Results 2 and 4, S3 Text §5; Abstract, Results 2 and 4, Table 3 and
  Fig 3 for B21); what the lists leave out is W3-1.
- Changed "reported at" and outcome cells, each place opened:
  - B7: Discussion line 193 (the split-half test left undetermined); S3 Text §6 line 384 (0.318, 0.39); S5 Text §1.
  - B19 (c): Abstract (0.69), Results 2 (0.694, 0.729), Discussion (0.69), S3 Text §5 (+0.742, +0.645, +0.694, 0.729),
    Fig 3b.
  - B17b: S3 Text §7 line 462 (1.1883, −0.0940); S10 Table (both); S13 Table (−0.0940); neither value in the main text,
    whose −0.094 the numbers table sources to B24's −0.09441.
  - B24's check: Abstract and Discussion (−0.094); Results 2 (6.1); Results 4 and Table 3 (−0.18); Fig 3 (6.13 and
    −0.18); the residual table of S3 Text §6 (+0.0028 ± 0.0012, −0.01540, −0.18); S13 Table's note; S18 Table.
  - B24's expectations: Results 4 holds none of the row's values; S18 Table holds all five (but W3-2).
  - B25 (d): "as we read their Methods" is the record's and S3 Text §11's phrase; the five values equal S3 Text §11.
  - B27 (a): Results 2, Table 2 and S3 Text §5 hold both gaps with intervals and p. B27 (b): −0.0110 [−0.0170, −0.0050]
    in Results 2 (the value) and Table 2; r = −0.874 in S3 Text §5 only. B27 (c): +0.939 in Results 2; +0.922 in S3
    Text §5 only.
  - B28 (a): −0.200 and −0.355 in Table 3 and in Fig 3c's caption; the ratios −0.167 and −0.349 in S3 Text §6 and S18
    Table only. B28 (d): S18 Table has the sts DiDs and the coverage and no column for the shares of r.
  - B29 (d): `notes/partB29_censoring.py` line 123 reads `ts_gsr` alone; `censoring_tables.md` line 47 has the quoted
    words.
  - B16c (e): the tables file gives xtx and yty as two rows and has no row of their sum; the CSV has 48 rows labelled
    "MMI xtx+yty"; `derived_r24.out` item 1 has the eight contrasts; Results 7 has −0.0037 (tables file line 127).
- Recount of Part A: 81 rows; 36 met, 15 partly met, 16 missed (67); 14 others, which the sentence after Part A
  itemises as 7 + 1 + 3 + 3; none "could not be evaluated". Methods (line 261) has the same four counts. Row B27 (d)
  does note the residual's correlations with the r₁ gaps, for which the pre-run entry records no prediction (line
  8643).
- Part B, the row of `derived_r24.out`: each gloss against the place and the item. Abstract (0.69 [0.26, 0.89], item
  6) and Discussion (0.69); Results 2 (0.79, 0.0887, 0.0485, item 2; 38 %, item 4; −0.0123, item 4); Results 3 (0.898,
  2.30, item 7); Discussion (0.50, item 3); Results 4 (0.0001, 0.0006, item 5); Results 7 and Table 4 (the intervals
  at p = 10 and 20, item 1; the statement on the Fisher-z intervals, item 6); S3 Text §4 (item 7), §5 (items 2, 8, 9,
  11), §6 (items 5, 10), §8 (items 1, 6); S11 Table (item 1). These are all 20 rows that the numbers table sources to
  the output. Items 1–4, 5–8 and 9–12 are as the script's docstring dates them, and items 9–12 are the ten lines that
  HEAD adds to the output. `derived_r24.py`, re-run on a scratch copy of its thirteen input files, gives the committed
  output line for line but for the header.

*S20 Table and the literature file.*
- Table A: 12 rows × 10 cells compared by script. Rows 5 and 6 are identical cell for cell; the only differences in
  the table are three cells (rows 2, 11 and 12) where the file has computation labels for S20's section references.
- Row 5 against Luppi2026.pdf (41 pages: article 1–26, Extended Data 27–32, Reporting Summary 33–41; pp. 33–41 read
  on the images, all nine, and searched in an OCR of them):
  - p. 35: 20 recruited, 16 completed, 15 analysed; three anaesthesia levels; the two groups of five macaques, three
    awake and two with DBS; four marmosets.
  - p. 37: "five scanning sessions" and the four it names, "3 vol% burst-suppression" word for word; 350 volumes.
  - p. 3: deep anaesthesia; the macaques' three anaesthetics; four marmosets.
  - p. 4: the three mouse group sizes (10, 14, 19); p. 5: 43 mice.
  - p. 38: every acquisition parameter the cell gives (TR 1.838 s, 350 volumes, 3 T; 2,400 ms with the contrast
    agent and 1,250 ms, 500 volumes per run; 2,000 ms, 155 repetitions, 9.4 T; 1,000 and 1,200 ms, 7 T).
  - p. 39: the four parcellations with their region counts, the human denoising with CONN 17f, the macaque band and
    notch; p. 21: the four region counts.
  - p. 40: the marmoset and mouse band 0.01–0.1 Hz; "No global signal regression" (mouse); for the human data
    "global signal" only as a threshold of the outlier tool.
  - HRF deconvolution: on pp. 1–32 "deconvolution" occurs once (p. 16, of cell types) and "haemodynamic" once (p. 3);
    no "HRF"; on pp. 33–41 nothing (the one "convolution", p. 40, is the marmoset smoothing). The article defers its
    preprocessing to Supplementary Methods on p. 18. Both cells that the delta rewrites say this.
  - The row's page references that the delta leaves as they were are on their pages too: the surrogate quotation
    (p. 13), Eq. 9 (p. 20), the MMI double redundancy and the Gaussian solver (p. 19), the code (p. 22), the exception
    of the medetomidine–isoflurane mice (p. 5).
- Row 6 against Down2026.pdf (25 pages, numbered 1/55 to 25/55): the main text ends on pp. 19–20 and the references
  run from p. 20 to their last, no. 73, on p. 25; p. 4 refers to the supplementary materials for the fMRIPrep output
  and has "No blurring step"; no "global signal", "GSR", "deconvol", "HRF" or "h(a)emodynamic" on the 25 pages; the
  re-validation with the other redundancy function is announced for the supplement on p. 6. The row's other items
  are on the pages it gives (the counts on pp. 2–3; the regressors and the band on p. 4; "suitably Gaussian" on
  p. 6, in a sentence that begins on p. 5; the quotation of the effect on p. 1).
- Head notes and title: row 10 found by the search of 1 October, read on that date, added in the revision (the same
  in S3 Text §10); row 5's ranges narrowed; row 10's pages as the claim record of the revision (its title is "Claim
  record of the revision of 1–2 October 2026"); S20's title now has the words of the main text's list.
- The entry of Luppi et al. (2025): all 27 authors, in order, against page 1 of Luppi2025.pdf (the version posted on
  10 January 2026); the page prints "Légaré" with its accents and "David K. Menon", and "Rudiger", "Cofre", "Bechir"
  and "Misic" without accents, as the entry has them.

*S4 Text.*
- Sh3: Data and code availability has the same statement. A scan of the first lines of every text file under
  `results/` and `notes/review_results/` finds 23 tables without a commit (the five CSV files, and
  `inference_rows_deconv.csv`, `inference_rows_w30.csv` and the sixteen regional ΦR tables, which are written only
  with the sandbox) and nine files with `-dirty` or `nogit`, all among those S5 Text §4 lists.
- S6: Methods has "the text repeats it for several, in Results 2, 3, 5 and 7 and the Discussion" under the heading the
  cell names (the first clause is W3-3).
- R1: Table 2's two rows of baseline-adjusted contrasts carry t intervals and no p, and its caption calls them
  regression intercepts; the residual table's data rows carry intervals without p; the other exceptions named are as
  the main text has them (W3-10 is on the list's completeness).

*S5 Text.*
- §4, the run: heartbeat of 11 lines, connected at 23:42, 23:47 and 23:52, disconnected from 23:57:10 to the last
  line, 00:32:10; the last step began at 00:01:08 and printed 2,040 s, so it ended at 00:35:08, 178 s after that line;
  23:37:10 and 00:35:08 at +0300 are 20:37:10 and 21:35:08 UTC; the unit's log last written 00:35:10; 7, 1,428, 1 and
  2,040 s; no traceback, "=== unit exit 0"; 29 outputs in `outputs.sha256` (12 text files, 16 arrays, 1 pickle);
  `b27_start.sh` requires the charger and runs the unit under the four-way inhibitor; `b27_commit.sh` checks the 29
  sha256; 8bd189e is the commit of the outputs.
- §4, the audit's values: all eight are in `audit/findings_text.md` as quoted (T07: 2.644997, 0.576258; T10: −0.861
  [−1.299, −0.422], r = −0.777, −0.015468; T25: −0.015468, −0.014645, +0.011534, −0.7457). The file quotes two more
  numbers beside them, the slope at nine decimals (2.644996924) and −0.7876 in T25; the first is the listed value, and
  the second follows from committed per-subject values (recomputed from the two pickles: −0.014645, +0.011534,
  −0.7876) and was quoted by the audit of 30 September. The file's head says that T07, T10 and T25 rest on the released
  series, fetched outside the clone. None of the eight strings occurs in the main text, S1–S5 Text,
  `supplementary.md` or `captions_v2.md` outside this paragraph; the main text has 2.645 and "−0.74 per unit of pair
  r₁, from the printed means", and no slope on the pair r₁ DiD.
- §5: 63 + 57 + 32 = 152 findings in `findings_text.md`, `findings_record.md` and `findings_citations.md`; ten check
  reports with 13, 25, 17, 10, 17, 9, 11, 10, 12 and 33 findings, 157; `dispositions_revision.md` has a block for each
  of the 152 and a paragraph for each of the 157 (142 "Corrected.", 7 "Stated.", 8 "Kept."; grades 11, 69, 77). The
  claim record's head says what was added after the audit of the citations and after the checks.

**2. The dispositions.** For each of VS-3, VS-4, VS-5, VS-6, VS-7, VS-9, VS-10, VS-11, VO-1, VO-10, VO-11, VO-12,
VT1-6, VT1-7, VT1-8, VT1-10, VT2-8, VT2-11, VT2-16, VT2-17, VR-13, VR-14, VR-15, VN-1, VN-2, VN-3, VN-5, VN-11 and
VM-8 the finding was read in its check report and the disposition against HEAD.
- Every phrase a disposition puts in quotation marks is at the place it names, word for word (in S3 Text §5 the
  words of VS-11 stand with `ts_gsr` in code type).
- Each correction is in the files and answers its finding, with the remarks of W3-1 (VT1-7), W3-2 (VS-3), W3-3
  (VS-6, VT1-8), W3-4 (VT2-8), W3-5 (VN-1), W3-6 (VM-8) and W3-12 (VR-14).
- The record's places that these dispositions name were read too: "B28, outcome", first paragraph (the three inputs)
  and items (iii) and (v); "B16c, outcome" (e); "B27, outcome", "The run" and "The outputs"; the disposition of B's W1
  (lines 9294–9295).
- VT1-10: the heading of Results 6 is the committed one, and the section's second sentence is as quoted. VM-8: S20's
  title and the entry of S5 Text are as quoted, and the four other titles are those of 8bd189e. VN-3: the reasons
  recorded with the replacements U17.5, LT07.5, U17b.1 and LT07b.1 name the read's M4 and say what the cells state.
- "Found while the findings were settled": the committed head note (8bd189e, line 1566) has "(B21 (b) and (c); the
  reproductions in B23)"; the ten rows of B23 were and are counted (56 then, 67 now).

**3. Rules.** `supplementary.md`, S4 Text and S5 Text carry no round, stage or bundle name ("stage" occurs in a
paper's title, in "stage-specific" and in "data-release stage"; "r17" and "r24" only inside the file names
`derived_r17.out` and `derived_r24.out`) and no reviewer's letter (the three reads are named by role, S5 Text §5).
"planning session" and "writer's session" occur only in S5 Text line 33, which is §5. No phrasing that the last
corrections took out of the main text remains in these files.
