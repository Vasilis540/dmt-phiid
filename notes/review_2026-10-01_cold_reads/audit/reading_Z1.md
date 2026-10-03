# Z1 — the paper's files, the derived numbers' script, the claim record and the reasons of the replacements

HEAD of VT (9f89c23) against `checked4` (26156b8). Verified: everything that changed between the two in
`manuscript/draft_v2.md` (one sentence of the list of supporting information), in `manuscript/si/` (one sentence each
of S2, S3, S4 and S5 Text), in `manuscript/supplementary.md` (seven lines: S17 Table's source note, S19 Table's head
note, three rows of its Part B, rows 1 and 5 of S20 Table), in `notes/partB5_literature_v2.md` (the same two rows), in
`derived_r24.py`, `derived_r24.out` and `scripts_check_revision.out`, in the claim record (its head and the item on
Luppi et al., 2026) and in the replacements file (four new entries and the reasons of ten more); and the dispositions
of the fourth check that concern these files.

**Result.** No number, page, date or pointer that the corrections changed or added in these files was found wrong.
Three findings: 0 errors, 2 inexact, 1 note. The inexact ones are the parenthesis that the correction for Y1-4 put
into S17 Table's source note, which holds of a part of what the run of 1 October 2026 saved, and a count in the
reason recorded with the replacement of S19 Table's head note (the disposition of Y1-7 has the same count). The note
is on two values that S2 Text quotes for comparison.

**How checked.** Nothing under VT was changed (`git status --short --ignored` empty at the end). Scratch files are
under VW/Z1/: the word diffs of the files (`diff_*.txt`); the rows of S19 Table as data (`parse_s19.py`,
`s19_rows.json`); the search of the values of Part A's outcome cells in the main text (`search_partA.py`,
`search_partA_int.py`, their outputs and the hits at places that a cell does not name, `flag_asprinted.txt`,
`flag_round2sig.txt`, `flag_round1sig.txt`); the check of the supporting places that Part A names (`si_check.py`);
`tree/`, a copy taken from HEAD with `git archive` of `derived_r24.py`, of `notes/rev_inference_inverted.py` and of
the nineteen files that the script reads, in which the script was run (`derived_r24.run.out`); `pdf/`, the text of
the pages read and images of pp. 33–41 of Luppi2026.pdf; the replacements file at the two states
(`repl_checked4.json`, `repl_head.json`). No internet and no subject data: every computation is on committed result
files. Paths are relative to VT and line numbers are those of HEAD. SUP is `manuscript/supplementary.md`, MT
`manuscript/draft_v2.md`, "the record" `manuscript/analysis_record.md`; "review folder" is
`notes/review_2026-10-01_cold_reads/`, "replacements file" its
`revision/text_replacements_2026-10-01_cold_reads_revision.json`, "dispositions" its
`audit/dispositions_revision.md`; `derived_r24.py` and `derived_r24.out` are in its `checks/`; result files named
without a folder are in `notes/review_results/partB/`.

## Findings

**Z1-1**
- Where: SUP, S17 Table, source note (line 400): "(the per-subject values that the run of 1 October 2026 saved,
  those of B27, B29 and B16c, are not among them; their intervals are in S3 Text §5 and §8 and in S11 Table)".
- Problem: The parenthesis holds of a part of what the run saved. (1) "are not among them": B27's per-subject file
  holds, beside the pre- and post-injection means and the two gaps, the per-subject DiDs of the twelve quantities of
  its table (a), and these are the vectors that B21 read, that is, twelve of S17 Table's 932 quantities; B29's file
  holds each window's mean framewise displacement and r₁, whose DiDs are quantities of S17 Table too. S17 Table does
  not hold B27's gaps, B29's counts or B16c's rows. (2) "their intervals are in S3 Text §5 and §8 and in S11 Table":
  that holds of B27's gaps and DiDs and of B29's count DiD (S3 Text §5). Of B16c's 264 rows (44 quantities in six
  window sets, each with 14 per-subject DiDs) the two other places give the primary-set intervals of 25: S11 Table
  those of the MMI-sts, CCS-sts and whitened-r₁ contrasts in the eight cells, S3 Text §8 sixteen of these and that
  of the AR(1)-substituted estimate at p = 20 on ts_gsr. The eight contrasts of xtx + yty, three of the four
  substituted estimates, the four residual DiDs and every row of the five other window sets have no interval at the
  three places.
- Evidence: (1) `baseline_gap.csv` (168 rows; columns `pre_gap`, `post_gap`, `did`): its twelve `did` vectors (sts,
  r1, substituted, residual; ts_gsr at W = 60 and 30, ts_demean at W = 60) equal, to the file's six decimals (largest
  difference 5 × 10⁻⁷), `did_subjects` of the primary-set rows "sts …" and "autocorr …" of
  `notes/review_results/inference_rows_raw.pkl` and "diag predicted sts …" and "diag residual sts …" of
  `inference_rows_diag.pkl`, which are rows 625, 637, 661, 673, 697, 703, 223, 229, 241, 247, 259 and 265 of S17
  Table (group "pickle", set "primary", field "did"). The record says so: "B27, outcome", "The outputs" (lines
  8900–8901), the per-subject DiDs "equal the saved ones (B21's inputs) to 10⁻⁹". `censoring.csv` (392 rows, subject
  × run × window): the DiD of `mean_fd` (windows 6–14 minus 1–4, DMT minus placebo) has mean +0.01435, the mean of
  S17 Table's rows `fd_did` (row 741: +0.01435 [−0.01147, +0.04026]), and S3 Text §5 (line 299) calls Table 2's FD
  DiD "the same quantity"; the DiDs of `r1_ts_gsr` and `r1_ts_demean` equal those of "autocorr ts_gsr W60" and
  "autocorr ts_demean W60" to the file's five decimals (largest difference 6 × 10⁻⁶). S17 Table's body (lines
  406–1337) has no label that holds "gap", "count", "prewhiten_fixed", "ar10" or "ar20". (2) S3 Text §5, table (a)
  (lines 235–248): the intervals of the two gaps and of the DiD in each of B27's twelve rows; line 299: the count
  DiD's "[−0.58, +2.97]". `notes/review_results/inference_rows_prewhiten_fixed.pkl`: 264 rows, 44 labels (per order
  four each of "MMI sts", "CCS sts", "MMI xtx+yty" and "autocorr", two each of "diag observed sts", "diag predicted
  sts" and "diag residual sts", the "diag observed" vectors being those of "MMI sts" at W = 60) in six sets. S11
  Table, lines 284–307: 24 rows of B16c, all of the primary set. S3 Text §8: the table of lines 535–542 (MMI-sts and
  whitened r₁, eight cells) and, in line 544, "−0.0037 [−0.0066, −0.0008]", the residual DiDs "−0.0091" and
  "−0.0090" with no interval, and "the contrast of their sum is in `inference_rows_prewhiten_fixed.csv` and in
  `derived_r24.out`, item 1"; `derived_r24.out`, lines 3–39, holds the 36 primary-set intervals of which the two
  places print 25.
- Grade: inexact

**Z1-2**
- Where: the replacements file, U09h, `why`, last sentence: "the predictions that Part A quotes as recorded, three of
  which (those of B17 (ii), of B19 (c) and of B17b's first row) cite a value of a computation of Part B, are set
  aside with it".
- Problem: The three predictions that the reason names do cite a value that a computation of Part B prints. At least
  four more prediction cells of Part A carry numbers that come from computations of Part B, so that the count of
  three is of the cells that quote a single printed value and not of all that cite one: (a) B17b (i) (SUP line
  1642), "near the data's own null, +0.004 to +0.008", names the finite-sample null of the residual and gives the
  range of its DiD; (b) B17 (i) (line 1631) gives the same range as "its finite-sample expectation"; (c) the
  sign(q)-weighted cross-lag deviation (line 1624), "of order +0.006", takes the value that B8's outcome entry
  derives on the coupled family; (d) B27 (a) (line 1671), "+0.0025, a known mean" and "−0.0122", takes the two means
  from the rows of the r₁ contrast of the review computations of 14 September 2026. The head note's own words, "some
  of which cite an earlier value", hold of all of these, and Part B's second column agrees with the clause: no
  second cell names S19 Table's Part A for a prediction (the cell of `derived_r24.out` names rows B28 (c) and B16c
  (e) for their outcome cells).
- Evidence: The three: `coupling_map_tables.md`, line 16 ("first derivative in c at 0: -1.7711") and the record, "B8
  outcome (analytic)", line 2573 ("≈ +0.94 c"); `notes/review_computations_2026-09-14.md`, line 85 ("r = +0.953");
  `notes/review_results/logs/review_v2_residual_null.log`, line 11 ("obs sts=1.1835"). (a) The record, "Calibration
  of the diagnostic on the band-passed generator (B17b): pre-run entry", lines 5247–5248, and "Correction note, 15
  Sep 2026 10:05 UTC", item 2, lines 2622–2625: the null's DiD "+0.0054" and, under the third review's variations of
  it, "+0.0059 / +0.0052 / +0.0077" and "+0.0037"; the reading of Part B (the review folder's
  `audit/partB_reading.md`, line 125) lists SUP lines 1625, 1641 and 1642 for the null, as "recorded rules and
  predictions". (b) The record, B17's pre-run entry, line 4774. (c) The record, lines 3024–3027 ("the ≈ +0.006 that
  the correction note of 10:05 UTC derived for a coupling account") and lines 2575–2578 ("a positive mean cross-lag
  deviation of about +0.006"); the correction note itself (lines 2584–2660) holds no 0.006. (d) The record, B27's
  pre-run entry, lines 8629–8631 ("the group means of the r₁ gaps follow from the committed rows of
  `inference_rows_raw.pkl`"); `notes/review_results/inference_rows_raw.csv`, row "autocorr ts_gsr W60", primary:
  pre_dmt − pre_pcb = +0.0025, and −0.0122 with the DiD. The same count stands in the disposition of Y1-7
  (dispositions, lines 2670–2671).
- Grade: inexact

**Z1-3**
- Where: `manuscript/si/S2_Text.md`, the head (line 3): "Every result in this text is post hoc except the outcome of
  the regional test, whose prediction was recorded before the test was run."; the same statement in MT, line 395.
- Problem: For the record of the reading. Every result that S2 Text reports of the exploration is of a computation
  that S19 Table's Part B lists, the regional test's outcome (Part A) apart, so that the sentence holds of them. The
  text also prints, for comparison, two values of the pre-specified analysis, "against −0.0809 on the raw series"
  and the raw level in "from 1.155 to 0.832" (line 7): read to the letter, they are results printed in this text
  that are not post hoc. Both stood in the text before the head was changed.
- Evidence: `manuscript/si/S1_Text.md`, line 9: "Result (`results/primary_b_ts_gsr_win60.csv`): DiD −0.0809 nats
  [−0.1317, −0.0310]"; the numbers table gives Table 2's 1.1554 to line 3 of the same file; the two phrases are in
  `manuscript/si/S2_Text.md` at 8bd189e, at `checked3` and at `checked4`.
- Grade: note

## Checked and found exact

**The dispositions of the fourth check that concern these files** (Y1-1, Y1-4, Y1-5, Y1-7, Y1-8, Y1-9, Y1-11, Y2-1
to Y2-8, Y3-1 for the parse check, Y3-10, Y3-11, Y4-2 to Y4-5): every text they quote stands at the place they name,
word for word (28 quotations searched in the files at HEAD, each found once), and each correction answers its
finding. Z1-1 and Z1-2 are on what the texts of two of them say (Y1-4, Y1-7).

**1. S19 Table's head note** (SUP line 1601).
- (a) The sentences on Part A, against its 81 rows (lines 1607–1687). Every decimal number of each outcome cell, as
  printed and in each rounding to fewer decimals down to one significant digit, and its percentages, counts "N of M"
  and integers of three or more digits, were searched in lines 1–263 of MT (title to the end of Materials and
  methods, with captions and table bodies), and every hit at a place that the row's last cell does not name was read
  (250 as printed, 163 at two or more significant digits, 786 at one, most of these round numbers such as 0.01 or
  0.1). None is the row's outcome printed there as that quantity. The hits are other quantities with the same digits;
  or values that an outcome cell quotes for comparison and that belong to another row or to the pre-specified
  analysis (the primary contrast −0.0809 in the row of the W = 30 positive control; the values at τ = 1 in B3's row,
  which Table 4, Results 6 and 7 and Methods print from other files by the numbers table; B17 (i)'s +0.0049 in the
  rows of B17 (iii) and B28 (c); B17b (i)'s +0.0027 in the rows of B17b (iii) and of B24's check; the residual's
  +0.0115 in B22 (c)'s row; the Gaussian 1.2588 in B25 (a)'s row); or the same quantity from another computation,
  as the cell says (B17b's −0.0940, which the Abstract and the Discussion print as B24's −0.094, named in the row
  of B24's check; Table 3's +0.0049 ± 0.0019, which is B28's). The Discussion's "0.003–0.005" (line 183) is of the
  three expectations of Results 4, those of B17b (i) and B17 (i) among them, whose cells name the Discussion. Five
  rows are "not quoted" (lines 1607–1610 and 1612) and no value of their outcomes is in the main text. Each of the
  other 76 names a supporting text or table, and each place named was opened: it reports the row's computation and
  holds the outcome, S1 Text "in summary" for the rows of lines 1611 and 1614, as their cells say, and at four
  decimals for that of line 1615; the total of B26's row ("42,681 of 473,262,025") stands in the row alone, S3 Text
  §6 holding the counts on the data. Cells that also name a derived number or a statement in words are as the note
  says (lines 1632 and 1643, "Limitations (in words)"; line 1648, "Results 4 (in words)"; line 1684, "the level at p
  = 20 only as the base of a share, 18 %"), and places of that kind that a cell does not name exist, as it says (the
  Abstract's "0.006–0.009" is derived from the outcomes of B17 (i) and B17b (i), whose cells do not name the
  Abstract).
- (b) "which holds the intervals of the quantities that had a saved per-subject vector when B21 ran": B21's two files
  carry `git=d5a65bd`; the trees of a9d9ca4, c25a310, d5a65bd and 13e7299 hold eight
  `notes/review_results/inference_rows_*.pkl` (72, 72, 72, 72, 72, 264, 84 and 30 rows: 738) and that of 8bd189e a
  ninth, `inference_rows_prewhiten_fixed.pkl` (264 rows); B21's script takes the pickles by that pattern (its line
  166); `inference_revision.csv` has 932 rows (738 "pickle", 36 "engine", 158 "saved") and S17 Table's body 932. No
  second cell of Part B names S17 Table or S4 Text, and S5 Text is named in two (lines 1706 and 1710, §1 and §4,
  which quote the values).
- (c) "or the predictions that Part A quotes as recorded, some of which cite an earlier value": the prediction cells
  of the 81 rows were read for values of earlier computations. Those that come from computations of Part B are in
  Z1-2; the other earlier values are of computations of Part A or of the pre-specified analysis (for example 0.85,
  +0.00340, 0.729, 0.715, +0.495, 6.89, −0.753, +0.0143), of the verification of 22 September 2026 (the rows of
  B23, as the head note says) or evaluations that the pre-run entries state themselves.

**2. S17 Table's source note** (SUP line 400). "when B21 ran" and "of that time": as 1 (b). The run of 1 October
2026: 8bd189e adds 29 outputs beside the evidence of the run (four tables files, four CSV files, four logs, sixteen
arrays and one pickle), as the record's "B27, outcome" says. Per-subject values are in `baseline_gap.csv` (168
rows), `censoring.csv` (392 rows), the pickle and the sixteen arrays of atoms; `matched_slope.csv` holds one row per
condition and replicate of a simulation. S3 Text §5 gives the intervals of B27's gaps and DiDs and of B29's count
DiD. The rest of the parenthesis: Z1-1.

**3. Part B of S19 Table, the three rows.**
- The coupled family (line 1700), "Results 1; Fig 1c; S3 Text §3": S18 Table (lines 1339–1598) names the family only
  in the labels of the rows of B23 (a3) (lines 1363–1370 and 1408–1415), names neither B8 nor a file of it, and
  prints no value of `coupling_map_tables.md` (of the decimals of three or more places that the table and the file
  share, none is the same quantity). Fig 1's caption prints six values of the file's first table (its lines 8–14),
  and S3 Text §3 names the script and the file (lines 116–122).
- The whole-brain ΦR items (line 1707): `notes/review_results/logs/rev_phir_items.log` holds the three items (the
  contrasts at W = 30 in six window sets, "(2) per-subject ΦR" and "(3) ΦR by window");
  `notes/review_results/inference_rows_w30.csv` holds the first (30 rows: five labels in six sets, the placebo share
  of "PhiR_deconv ts_gsr W30" 0.56); `notes/review_results/logs/phir_baseline_and_slope.log` the four tests;
  `notes/prespec_regional_phir_deconv_2026-09-14.md` lists the three under "Three whole-brain items requested at the
  same time (no prediction)". Results 2 (MT line 87) points to S2 Text for the scrutiny of a pre-injection gap, and
  S2 Text (line 9) holds the share at W = 30, the gap, the placebo run's slope and its decline.
- The row on `derived_r24.out` (line 1711): Results 7 (MT line 158) prints the interval of the contrast at p = 20
  alone and states the Fisher-z intervals in words; Table 4 (lines 167–168) prints the intervals at p = 10 and 20;
  the numbers table gives the four limits to `derived_r24.out`, item 1. The counts of the row's third cell (two
  pickles, eight CSV files, five tables files, three array files and a log) are those of the nineteen files that the
  script opens.

**4. S20 Table, rows 1 and 5** (SUP lines 1722 and 1726; lines 13 and 17 of `notes/partB5_literature_v2.md`, which
hold the two cells in the same words).
- Row 1, Luppi2022.pdf (39 pages: the article to p. 20, the Extended Data on pp. 21–32, the Reporting Summary on pp.
  33–39): p. 13 has the removal of the first ten volumes and names a field strength once, for the scanner of the
  diffusion scan; p. 36, in the Reporting Summary, gives 3T for the HCP dataset; p. 37 states that no volume was
  censored.
- Row 5, Luppi2026.pdf (41 pages): pp. 1–26 are the article (the journal's pp. 777–802), pp. 27–32 the Extended
  Data (its Figs 1–4), pp. 33–41 the Reporting Summary (its pages 1–9, read from images). Every page that the row
  cites was read and lies in the part that the ranges give. Article: p. 3 (the humans' deep anaesthesia; five
  macaques and the three anaesthetics; four marmosets), pp. 4–5 (the mice, 10, 14 and 19: 43), p. 5 (the DBS dataset;
  the reported effect), p. 13 (the surrogate), p. 19 and p. 22 (the redundancy function, the solver, the code), p.
  20 (Eq. 9), p. 21 (the region counts). Reporting Summary, fifteen citations by page alone: p. 35 (20 recruited, 16
  completed, 15 analysed; three anaesthesia levels; the two macaque datasets, three animals awake and two with DBS;
  four marmosets), p. 37 (the five sessions; 350 volumes), p. 38 (3 T and 1.838 s; 2,400 ms with the contrast
  agent, 1,250 ms, 500 volumes per run; 9.4 T, 2,000 ms, 155; 7 T, 1000 and 1200 ms), p. 39 (the four
  parcellations; the human denoising, band and software version; the macaque filters), p. 40 (the band of the
  marmoset and mouse data; no global signal regression for the mouse). p. 18 defers the preprocessing to the
  Supplementary Methods; no HRF deconvolution is mentioned on the 41 pages.

**5. S2 Text's head and the main text's list of supporting information.** Every result of S2 Text by its
computation: ΦR on the raw series, the deconvolution, its HRFs, levels and contrasts, the power share and the
run-level r₁ of the deconvolved series and the deconvolved ΦR increase are of the review computations of 14
September 2026 (Part B, line 1695); the gap, the placebo run's slope and its decline are of the four tests, and the
share at W = 30 of the three items entered with no prediction (Part B, line 1707; the 64 % of the range is the
share at W = 60 of the review computations); the regional test's outcome is the row of Part A (line 1616), its
prediction recorded on 14 September 2026, 11:37 UTC, before any regional number (the pre-specification note; the
record's closure entry, lines 2393–2394). The sentence of MT line 395 says the same in other words. See Z1-3.

**6. S3 Text §4, S4 Text's row R1, S5 Text §5.**
- S3 Text §4 (line 128): `notes/fresh_review_2026-09-17/checks/check_A1_atoms_family.log`, line 66, has 191 × 191 =
  36,481 points and none at which the derivative in q is the larger; the folder is that of the review of 17
  September 2026 (`review.md`, dated so); §6 (line 307) and §9 (line 550) use the same words of their checks, and S5
  Text §1 (line 7) names the three sections.
- S4 Text, row R1 (line 62), "Results 2, 6 and 7": Results 2 (MT lines 87 and 106), 6 (line 154) and 7 (line 158)
  print DiDs with an inverted interval and an exact p; Results 3 prints no DiD; Results 4 (line 120) prints two with
  an interval and no p, as the parenthesis goes on to say; Results 5 (line 146) prints its DiDs with p alone.
- S5 Text §5 (line 33): the ids of the report files of the review folder's `audit/` give 63 + 57 + 32 = 152 for the
  three audits, 157 for the ten sessions of the first check, 86 for the seven of the second, 42 for the four of the
  third and 12 + 8 + 11 + 7 = 38 for the four of the fourth.

**7. `derived_r24.py`.** The docstring: item 2 prints "SD pre gap", "SD post gap" and "SD DiD"; the nineteen files
that the script opens, by the script that wrote each: B16c (the pickle and the tables file of the fixed orders), B27
(`baseline_gap.csv` and its tables file), B28 (`matched_slope.csv`), B29 (`censoring.csv` and its tables file); and
B4 (the two `diag_series_*_W60.npz`), B7 (`splithalf.log`), B11 (`regional_sts_r1.csv`), B15 (`directed_crosslag.csv`
and its tables file), B16 (`inference_rows_prewhiten.pkl`), B20 (`regional_partial.csv`), B21
(`inference_revision_tables.md`, `splithalf_subjects.csv`), the inference rows of the raw series
(`inference_rows_raw.csv`) and the regional atoms of the windowed estimator
(`regional/regional_atoms_raw_ts_gsr_win60.npy`). Item 6: the regular expression finds eight headings in
`prewhiten_fixed_tables.md` (lines 6, 31, 55, 80, 104, 129, 153, 178), each followed in its own section by the
printed r (+0.445, +0.570, +0.168, +0.014, +0.333, +0.081, +0.157, −0.079), and the comparison is asserted cell by
cell. Run from the root of the copy, the script ends without error and its output equals `derived_r24.out` in lines
2–103 (line 1 has `git=nogit` for `git=8bd189e`); line 68 of the output has the changed words.
`scripts_check_revision.out` names five scripts; each parses, and they are the four `.py` files that `git diff
--name-status 8bd189e HEAD` shows as added and the one it shows as modified (no `.sh` file is added or changed).

**8. The claim record.** Its head: between `checked3` and `checked4` three pointers changed (the items on Luppi et
al., 2026, Gatica et al., 2024, and Down et al., 2026), one heading gained "head note and" (Down et al.) and the two
descriptions of a Reporting Summary changed; between `checked4` and HEAD the pointer and the description of the
item on Luppi et al. (2026), and nothing else outside the head. Luppi2026.pdf, pp. 33–41: text extraction returns
nothing but a form feed for each page; one font is listed, on p. 35 alone; the content streams hold no
text-showing operator on pp. 33, 34 and 36–41 and eight on p. 35, each of one code, which the font's map gives as
U+2009, a thin space. The pointer: S20 Table's row 5 and the literature file give the five macaques and the three
anaesthetics and do not say that the animals were scanned awake; S3 Text §10 (line 556) and the review folder's
`pubmed_search/psychedelic_phiid_search.md` (lines 91–92) say both; of p. 1, S3 Text §10 says that neither abstract
names a drug and the search note that the abstract names no drug and none of the string's decomposition terms, and
neither says what the title names. p. 3 of the PDF has the five macaques scanned awake and under the three
anaesthetics.

**9. The reasons recorded with the replacements.** The file has 314 entries with no id twice; applied in order to
the files of 8bd189e, each `old` is found the number of times its `count` gives, and the sixteen files come out as
at HEAD, the record's five new headings apart (their time). The new entries: S202 and S203 (see 5), S325 (see 6) and
U25 (B21 last ran before the run of 1 October 2026 and did not read its files; the text of U25's `new` is the
subject of Z1-1). The changed reasons: S201 (the values are those of the table of section 1 of the report on the
regional check, its line 51); S417 (see 6); S422 (S1 Text has 0.82 and not 0.54); U09i.4 (see 3); U17.5 and LT07.5
(the page ranges; p. 18 defers to the Supplementary Methods); U24.1 and LT13.1 (see 4); LT13.2 (the sentence stands
in the literature file's search paragraph, its line 7; S20 Table has it in its head note); U09h with Z1-2. The
reasons that did not change of the six entries whose `new` changed (S502, U06d, N01, C08, RR03, REC01) still hold of
their texts.

**10. Rules.** No computation label stands in MT before "## Supporting information" (line 391). No manuscript file
holds a round, stage or bundle name ("stage" occurs in "data-release stage" and in a cited title and the effect
quoted from it, "bundled" of third-party files) or a reviewer's letter. "planning session" and "writer's session"
occur only in S5 Text, line 33 (§5). `python3 notes/review_2026-09-25/checks/wc.py manuscript/draft_v2.md` gives
the lines of `checks/wc_revision.out` (total with headings 8489, without 8362).
