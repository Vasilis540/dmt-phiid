# X1 — the paper's files: the main text, S3, S4 and S5 Text, the supplementary tables, the literature file

HEAD of VT (f50c1d3) against `checked2`. Files verified: `manuscript/draft_v2.md`, `manuscript/si/S3_Text.md`,
`manuscript/si/S4_Text.md`, `manuscript/si/S5_Text.md`, `manuscript/supplementary.md`,
`notes/partB5_literature_v2.md`, and the dispositions named in the task
(`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`).

**Result.** No number, page, count or quoted phrase that was changed or added between `checked2` and HEAD in these
files was found wrong: every recomputation agrees with the text at the printed precision, and every assigned
disposition names a correction that is in the files, each quoted phrase at its place word for word. Eleven findings:
0 errors, 5 inexact, 6 notes. The inexact ones are two general statements that the corrections wrote into S4 Text
(rows R1 and S6), the sentence on supplementary materials that the correction for W3-11 wrote into S20 Table's head
note and the literature file, and three "reported at" cells of S19 Table, Part A, that name a place which does not
hold the row's outcome (cells older than this revision). The independent reading of Part A found no place of the main
text that prints a value of a row's outcome as that row's result and is not named in the row's cell.

**How checked.** Nothing under VT was changed (`git status` empty at the end). Scratch files are under VW/X1/: the
word diff of the six files and its 40 changed passages; a copy of HEAD made with `git archive`, on which `wc.py`,
`abstract_summary.py` and `derived_r24.py` were run; the recomputations (`item2.py`, `item10.py`, `item11.py`,
`tableA.py`); and the scripts that read S19 Table, Part A, against the main text and the supporting information
(`rowscan.py`, `partA_auto.py`, `siscan.py`) with their outputs. No internet, no subject data. Paths are relative to
VT and line numbers are those of HEAD. "Numbers table" is `manuscript/main_text_numbers.csv`; "dispositions" is the
file named above; "literature file" is `notes/partB5_literature_v2.md`; "review folder" is
`notes/review_2026-10-01_cold_reads/`, whose `checks/derived_r24.out` is written `derived_r24.out`; result files named
without a folder are in `notes/review_results/partB/`; "p." of a cited work is the page of the PDF as saved.

## Findings

**X1-1**
- Where: `manuscript/si/S4_Text.md`, row R1 (line 62), the sentence added: "Where the main text gives a contrast as a
  point value or with its p alone, its interval is in the supporting information", with the list that follows it and,
  after the list, "The exceptions are ...".
- Problem: The sentence is general, and its list with the exceptions does not cover every such contrast of the main
  text. (i) Two have no interval in the supporting information and are not among the exceptions. Limitations gives the
  DiD of the count of replaced volumes per window as "+1.12 after the injection relative to placebo (p = 0.2166,
  positive in 7 of 14)"; S3 Text §5, which it cites, gives the same three values and no interval, and the fourteen
  per-subject values are saved and printed there, so that it is not a contrast "whose per-subject values were not
  saved". Results 7 gives the DiD of the AR(1)-substituted estimate on the series whitened at p = 20 as a point value,
  "the AR(1)-substituted estimate carries −0.0037 of it (S3 Text §8)"; S3 Text §8 and S11 Table print no interval for
  it (a committed result file holds one). (ii) Two more are given as a point value or with p alone, have their
  interval in the supporting information, and are not in the list: the deconvolved contrast of Results 7, "(−0.0782,
  p = 0.0013; ...)", and the whitened series' r₁ DiD at p = 20, "(−0.0927)". The five kinds that the sentence does
  list are right: each named place holds the interval (last section).
- Evidence: `manuscript/draft_v2.md` line 201 (Limitations), line 158 (Results 7: −0.0927 and −0.0037) and line 171
  (Results 7: −0.0782). `manuscript/si/S3_Text.md` lines 284 and 299 (the count DiD with p and the count of positive
  subjects, no interval; lines 270–283 print the fourteen count DiDs; `notes/review_results/partB/censoring.csv` holds
  the counts per subject, run and window), line 544 ("the AR(1)-substituted estimate carries −0.0037", no interval),
  line 539 (−0.0927 [−0.1497, −0.0367]). `manuscript/supplementary.md` line 298 (S11 Table: the same interval), line
  331 (S11 Table's note: the diagnostic's residual DiD at p = 10 and 20, no interval of the estimate's DiD), line 556
  (S17 Table, row 151: the deconvolved contrast, inverted interval [−0.12213, −0.03619]). `manuscript/si/S2_Text.md`
  line 7 (−0.0782 [−0.1221, −0.0362]). `notes/review_results/inference_rows_prewhiten_fixed.csv` line 165 (the
  estimate's DiD at p = 20, −0.0037, with the file's limits −0.0063 and −0.0012);
  `notes/review_results/partB/prewhiten_fixed_tables.md` line 127 (the point value only). The main text was read from
  the Abstract to the end of Methods for contrasts given without an interval; none besides these four lies outside
  the list and the exceptions. Not counted as such contrasts: the bounds "p ≤ 0.008" (the leave-one-out refits,
  Results 2) and "0.085 or more" (ΦR's four cells, Results 6), the group-map contrasts of Results 3 and Fig 4 with
  their spin p, single subjects' values and simulated quantities.
- Grade: inexact

**X1-2**
- Where: `manuscript/si/S4_Text.md`, row S6 (line 53), the clause added: "the complete list is S19 Table's".
- Problem: S19 Table does not list every post hoc or review computation that the supporting texts quote. S3 Text §6
  quotes a computation of the third review of 15 September 2026: "partial r = +0.83 and +0.86 under the published CCS
  definition (computed by the third review from the committed per-subject DiDs, ... Appendix, computation 4; `phyid`'s
  mask gives +0.69 and +0.82)". S3 Text §3 quotes "a population computation without data, made in the audit of this
  revision's citations" (the two lag-1 transfer entropies after a filter, 0.0015 and 0.0004 nats). Neither has a row
  in Part B, and neither is in Part A, no prediction having been recorded for it. By the definition that S5 Text gives
  at its head, the first is a post hoc computation (run without a pre-run entry by one of the adversarial reviews of
  14–17 September 2026). The other clauses of the row hold: S3 Text says of many such computations, where it reports
  them, that they are post hoc or a review's, and the main text repeats the status for several.
- Evidence: `manuscript/si/S3_Text.md` line 384 and line 124. `manuscript/supplementary.md` lines 1695–1707 (Part B,
  thirteen rows): none names the third review, its file
  (`notes/adversarial_review_draft_v2_second_pass_2026-09-15.md`), the partial correlation, or the audit's script
  (`notes/review_2026-10-01_cold_reads/audit/te_filter_check.py`); the two file names occur nowhere in
  `manuscript/supplementary.md`. `manuscript/si/S5_Text.md` line 3 (the definition) and line 7 (the third review).
- Grade: inexact

**X1-3**
- Where: `manuscript/supplementary.md`, S20 Table, head note (line 1711): "The full texts are the studies' main
  articles, with supplementary materials only where a cell names them"; the literature file, search paragraph (line
  7): "What was read in full is each study's main article, with supplementary materials only where a cell names them".
- Problem: Row 1 (Luppi et al., 2022) takes two items from pages of that study's Reporting Summary, which no cell of
  the row names; row 5 does name "its Extended Data and its Reporting Summary". Row 1 gives "3 T (pp. 13, 36)" for the
  HCP data and "no volume censoring (pp. 13, 37)"; pp. 33–39 of the PDF are the Reporting Summary, and the statement
  on censoring is on p. 37 alone.
- Evidence: Luppi2022.pdf (39 pages): p. 33 opens the Reporting Summary, whose running head stands on pp. 33–39;
  p. 36, under "Field strength", "HCP and PET datasets: 3T"; p. 37, under "Volume censoring", "No volume censoring was
  used in this study."; p. 13 (Methods) has neither "censor" nor "scrub". `manuscript/supplementary.md` line 1717 and
  the literature file's line 13 (row 1); in the two tables the words "Reporting Summary" occur in row 5 only.
- Grade: inexact

**X1-4**
- Where: `manuscript/supplementary.md`, S19 Table, Part A, row "B19 (b), the within-window regression" (line 1636),
  "reported at": "Results 1; S3 Text §4".
- Problem: Results 1 prints none of the values of the row's outcome ("R² = 0.808 against r² = 0.462 for r₁ alone;
  standardised coefficients r₁ +0.66, \|q\| −0.46, \|a_x − a_y\| −0.43") and does not state that outcome in words.
  Its sentence on the regression gives the unstandardised slopes, "+5.13 per unit of r₁ and −0.53 per unit of |q|",
  and the per-SD ratio 1.4, which are values of row B22 (d), whose cell names Results 1. S3 Text §4 holds the row's
  values. The cell is as it was at 8bd189e.
- Evidence: `manuscript/draft_v2.md` line 53. The numbers table gives
  `notes/review_results/partB/aligned_directed_tables.md` line 29 as the source of +5.13 and −0.53 (note "B22 (d)")
  and derives 1.4 from lines 27 and 29 of that file. None of 0.808, 0.462, 0.66 and 0.46 occurs in the main text as
  an R², an r² or a coefficient.
  `manuscript/si/S3_Text.md` line 134 (R² = 0.808, r² = 0.462, +0.661, −0.463, −0.426);
  `notes/review_results/partB/exchange_rates_tables.md`, part (b).
- Grade: inexact

**X1-5**
- Where: `manuscript/supplementary.md`, S19 Table, Part A, rows "Pre-registered analysis choices, the tier assignment"
  (line 1610; "reported at": "S1 Text; S2 Table") and "The regional ΦR check after deconvolution" (line 1616;
  "reported at": "S2 Text").
- Problem: The named places of the supporting information hold neither a value of these rows' outcomes nor the
  outcomes in words. (i) The tier assignment's outcome is "Tier 2 R 0.964–0.990 with lower bounds 0.903–0.964 in the
  four deciding cells", the escalation rule and "tier 2 is the claimed tier on the primary windows 6–14". S1 Text
  defines the three tiers, says that a tier-2 criterion was pre-specified, and gives the result of its test, "the
  claimed tier is 3"; S2 Table gives that test on the data. Neither gives the values of R, the rule or the
  assignment; they are in the record only. (ii) The regional check's outcome is "Workspace minus non-workspace
  −0.0047 [−0.0079, −0.0013] (percentile), p = 0.023, positive in 4 of 14"; S2 Text says only that "a regional test
  with a prediction recorded before it was run was carried out", with the name of the report's file, and gives
  neither the values nor the sign. Both cells are as they were at 8bd189e.
- Evidence: `manuscript/si/S1_Text.md` line 11; `manuscript/supplementary.md` lines 19–38 (S2 Table);
  `manuscript/si/S2_Text.md` line 9; `manuscript/analysis_record.md` lines 963–1005 (the values of R and the
  assignment). "0.964", "0.990", "0.0047" and "0.0079" as these quantities occur in the manuscript files in the two
  rows of S19 Table only.
- Grade: inexact

**X1-6**
- Where: `manuscript/supplementary.md`, S19 Table, Part A, rows "The run-level mean cross-lag deviation" (line 1622)
  and "The W = 60 statistic and the finite-sample null" (line 1625), each with "S3 Text §6; S9 Table (superseded
  values)"; and row "B16c (b), the level falls with the order" (line 1684), "Results 7; Table 4; S11 Table; S3 Text
  §8".
- Problem: Places named that do not print the row's values, where the cell or the place makes this plain; for the
  record of the reading of Part A. (i) S3 Text §6 prints none of the values of the first two rows (+0.00009 with its
  intervals and p = 0.0004, −0.00738; the ratio 1.80, +0.00025 at W = 840, 7.3 %); it says in words that a signed mean
  cancels on ts_gsr and that the window-sign statistic is superseded, and gives the budget that replaced the readings.
  The values are in S9 Table, as the cells' parenthesis says (S9 Table has no "7.3 %"). (ii) Results 7 prints no
  MMI-sts level at p = 10 or p = 20 and does not say that the level falls with the order; it uses the level at p = 20
  once, in "18 % of the whitened level". The levels are in Table 4.
- Evidence: `manuscript/si/S3_Text.md` lines 315 and 347–363; `manuscript/supplementary.md` lines 185–187 (S9
  Table's two paragraphs of superseded values); `manuscript/draft_v2.md` line 158 and lines 164–168; the numbers
  table derives the 18 from 0.012673 / 0.071895.
- Grade: note

**X1-7**
- Where: `manuscript/supplementary.md`, S19 Table, Part A, row "B17 (iv), the calibration on AR(1) pairs, within-pair
  asymmetry" (line 1634), outcome "Level 0.7131 against 0.7152 at W = 60", "reported at": "S3 Text §7; S10 Table;
  Limitations"; and the first row of B17b (line 1641), prediction "near the null's 1.18 rather than B17's 0.715".
- Problem: The one value of an outcome cell that the main text prints at a place which no cell of its computation
  names. Methods, The AR(1)-substituted estimate and its calibration, prints the AR(1) generator's W = 60 level:
  "whose windowed sts level (0.715) lies far below the data's (1.155)". In row B17 (iv) the value is the level of
  condition (i), against which the row's own result (0.7131) is set, and it is not in the outcome cell of B17 (i); no
  cell of B17 or of B17b names Methods. Reported as a note because the value is the row's reference, not its result.
- Evidence: `manuscript/draft_v2.md` line 245; the numbers table gives
  `notes/review_results/partB/calibration_tables.md` line 8 (0.7152, condition (i), W = 60) as its source;
  `manuscript/supplementary.md` lines 1631–1634 and 1641–1645 (the cells of B17 (i)–(iv) and of B17b).
- Grade: note

**X1-8**
- Where: `manuscript/draft_v2.md`, Results 2 (line 108), Results 4 (line 124), Results 6 (line 152), the Discussion
  (line 191), Limitations (line 201) and Methods (line 245), against the "reported at" cells of S19 Table, Part A.
- Problem: Not values of an outcome cell, and so not counted as places missing from a cell; listed for the planning
  session's own rule (the dispositions' paragraph on W3-4: the cells were read "by the source of each number in the
  numbers table"). The numbers table gives a tables file or a log of a Part A computation as the source of these
  numbers, and the cell of the row concerned does not name the place: Results 2, "24 TRs above the motion threshold,
  against 23.6 on average" and the framewise-displacement DiD "+0.0935" (B29, table (a)); Results 2, "the AR(1)
  pairs' 3.1" (derived from B23 (b), condition (i): 0.04240 / 0.01377), beside the band-passed generator's 6.1, for
  which the row of B24's check does name Results 2; Methods, "0.786 at a = 0.85" (B23 (b)); Results 4, the 0.012 of
  "a fall of 0.012–0.015 in pair r₁" (B23 (e), the AR(1) generator's −0.01243); Results 4, the four cross-half
  correlations of the residual with r₁ (the "context" lines of the split-half log, B7); Results 6, "a split-half
  reliability of 0.30" (B7's tables); Limitations, "0.053 nats for sts and 0.04 for the mirror atoms" (B14's tables);
  the Discussion, "sts's 3.09" (B20's tables).
- Evidence: the numbers table's rows for these numbers (sources:
  `notes/review_results/partB/censoring_tables.md` lines 17 and 24;
  `notes/review_results/partB/diagnostic_alternatives_tables.md` lines 104 and 190 and its part (b), condition (i);
  `notes/review_results/partB/splithalf.log` lines 12 and 24; `notes/review_results/partB/splithalf_tables.md` line
  13; `notes/review_results/partB/family_atoms_tables.md` lines 17 and 25;
  `notes/review_results/partB/regional_partial_tables.md` line 8); `manuscript/supplementary.md` lines 1621 (B7),
  1628 (B14), 1639 (B20), 1658 (B23 (b)), 1661 (B23 (e)), 1663 (B24's check) and 1679–1682 (B29).
- Grade: note

**X1-9**
- Where: dispositions, the paragraph on W3-4 (lines 1939–1948): "Every "reported at" cell of Part A was read against
  the main text ... and completed with the places that print the row's values. Besides the six named: ... B22 (a)
  (Results 4, in words) ...".
- Problem: Results 4 was not added to the cell of B22 (a): it stood there at `checked2` ("Results 4; S3 Text §6 (its
  residual table)") and at 8bd189e ("Results 4; Table 3; S3 Text §6"). What HEAD adds to that cell is the qualifier
  "(in words)" and the longer pointer into S3 Text §6, "and, under the next heading, the text and the table of the
  aligned and directed statistics", which no disposition states for this row (the paragraph on W3-2 gives the pointer
  for the row of B24's expectations; the reason recorded with the replacement, U08.5 of the replacements file, does
  state it). The longer pointer itself holds. The other 23 cells of Part A that differ between `checked2` and HEAD are
  as the paragraphs on W3-4 and W3-2 say.
- Evidence: `git show checked2:manuscript/supplementary.md` and `git show 8bd189e:manuscript/supplementary.md`, row
  "B22 (a), A_other"; `manuscript/supplementary.md` line 1648; the review folder's
  `revision/text_replacements_2026-10-01_cold_reads_revision.json`, id U08.5; `manuscript/si/S3_Text.md` lines
  325–326 (the residual table's last column: −0.00059 and −0.00249) and lines 343–372 (the text and the table of the
  aligned and directed statistics: +0.00196 and −0.00251).
- Grade: note

**X1-10**
- Where: `manuscript/si/S4_Text.md`, row R1 (line 62), first sentence, unchanged since `checked2`: "(Table 2; Results
  2–6; intervals without p in the data rows of the residual table of S3 Text §6; ...)".
- Problem: Outside the delta; read with the row's new sentence. The parenthesis places the intervals without p in S3
  Text §6 alone, but the main text gives two contrasts with their interval and no p: in Results 4 the AR(1)-substituted
  DiD, "−0.0924 [−0.1503, −0.0348]", and the residual DiD, "+0.0115 [+0.0005, +0.0226]", the second also in Table 3's
  data row (at 8bd189e the clause read "intervals without p in Table 3's data rows", of the table that has since moved
  to S3 Text §6). The parenthesis also stops at Results 6, while Results 7 and Table 4 give contrasts with inverted
  intervals and exact p.
- Evidence: `manuscript/draft_v2.md` lines 120 and 130 (no p against zero for either DiD in the main text; S17
  Table, rows 223 and 229, has them, 0.0037 and 0.0421), lines 158 and 162–168;
  `git show 8bd189e:manuscript/si/S4_Text.md`, row R1.
- Grade: note

**X1-11**
- Where: `manuscript/supplementary.md`, S19 Table, Part B, "where quoted" of three rows: "The checks of the review of
  17 September 2026" (line 1702: "S3 Text §6 (...) and §9 (...)"), "The spectral centroid" (line 1698: "Results 5; S3
  Text §9") and "The review computations of 14 September 2026" (line 1695: "... S2 Text; S3 Text §4–6").
- Problem: Outside the delta; seen while S3 Text was read against row S6 of S4 Text. S3 Text quotes each of the three
  at a section that the row does not name: §4 gives "0 of 36,481" from a log of the review of 17 September
  (`check_A1_atoms_family.log`), a third check of that review beside the two that the row and S5 Text §1 name; §4
  gives the centroid's levels, 0.0369 Hz and 0.0374 Hz (`rev_extra.log`); §9 gives the ratio of window variance to run
  variance, 1.28 to 0.89, and the correlations with it, from sections 1 and 6 of the review computations of 14
  September. The other cells of Part B were not read for completeness, apart from the row of `derived_r24.out` (last
  section).
- Evidence: `manuscript/si/S3_Text.md` line 128 (§4) and line 550 (§9); `manuscript/si/S5_Text.md` line 7 ("two of
  its checks are quoted, as review computations, in S3 Text §6 and §9").
- Grade: note

## Checked and found exact

**1. The delta** (`git diff --word-diff checked2 HEAD` on the six files: 40 changed passages; main text 2, S3 Text 3,
S4 Text 2, S5 Text 1, `supplementary.md` 29, the literature file 3).

- Main text, Results 2 (line 87): "(the DiD's SD 0.0887 against the post-injection gap's 0.0485; r(DiD, pre-injection
  gap) = −0.888, r² = 0.79)". Recomputed from `notes/review_results/partB/baseline_gap.csv` (sts, ts_gsr, W = 60,
  divisor 13): SD of the DiD 0.088676, of the post-injection gap 0.048548 (of the pre-injection gap 0.052404),
  r = −0.887968, r² = 0.788487; `derived_r24.out`, item 2, prints the same. One DiD is positive, subject 14's, and
  that subject has the most negative pre-injection gap, as the sentence's last clause says.
- Main text, Methods (line 241): "(the text repeats it for several)" is true of the text: Results 2 (three places),
  Results 3 and Fig 4's caption, Results 5 and 7, the Discussion, Methods' next subsection and Limitations mark a
  quantity as post hoc or as resting on a rule or a prediction recorded beforehand.
- Word counts: `wc.py` gives 8,489 words with headings (8,362 without), within 8,500; `abstract_summary.py` gives 300
  and 200. Both outputs equal the review folder's `checks/wc_revision.out` and `checks/abstract_summary_revision.out`
  byte for byte.
- S3 Text §5, the note under table (a) (line 260). Recomputed with exact integers from the fourteen `pre_gap` values
  of r₁, ts_demean, W = 60 (sum 75,203 in units of 10⁻⁶): 3,068 of the 16,384 assignments have an absolute mean at
  least the observed one (p = 0.1873); 3,066 is the only even count that prints 0.1871. Besides the identity and its
  mirror, two assignments with their mirrors are counted by a margin within the bound k/14 × 10⁻⁶: one ties (nine
  values entering the difference), the other exceeds by 6/14 = 0.43 × 10⁻⁶ against 7/14 = 0.50 × 10⁻⁶; the nearest
  uncounted assignment is 0.71 × 10⁻⁶ away against its bound of 0.36 × 10⁻⁶. The run's count, "one such pair fewer",
  is 3,066 against 3,068. All 120 cells of table (a) recomputed independently (own inversion of the sign-flip test):
  119 equal as printed, and the one that differs is the cell the note names. `derived_r24.out`, item 11, agrees.
- S3 Text §6, "The residual's relation to r₁ across split halves" (line 406). Recomputed from
  `diag_series_ts_gsr_W60.npz` and `diag_series_ts_demean_W60.npz` (key `res`, the halves as
  `notes/partB7_splithalf.py` forms them) with `splithalf_subjects.csv`: r = −0.384543 and −0.699541 on ts_gsr,
  −0.597558 and −0.051497 on ts_demean; Fisher-z limits [−0.760, +0.183], [−0.897, −0.269], [−0.857, −0.098] and
  [−0.567, +0.493]; means −0.542 and −0.325; reliabilities 0.494 and 0.741, 0.216 (p = 0.459) and 0.712; ceilings
  0.605 and 0.392; ratios 0.896 and 0.828; on each variant the larger correlation exceeds its ceiling. Every figure of
  the paragraph agrees, and the correlations and reliabilities equal `splithalf.log` at three decimals and
  `derived_r24.out`, item 10.
- S3 Text §10, the sentences on ketamine (line 556), against S20 Table's rows 4 and 5 and the PDFs. Gatica2024.pdf
  p. 12: isoflurane anaesthesia; "received injections of ketamine" with five other agents; scanning "about 2 hours
  after anesthesia"; p. 1: no drug in the title, the keywords or the abstract. Luppi2026.pdf p. 3: the macaques
  scanned awake and under sevoflurane, propofol or ketamine; p. 1: no drug named. The search note (the review
  folder's `pubmed_search/psychedelic_phiid_search.md`) lists 2 records, neither of them one of the two studies.
- S4 Text, row R1's new sentence, the five kinds: Results 2 gives the FD-residualised r₁ DiD (−0.0123) and the r₁ DiD
  without global signal regression (−0.0216) as point values, and S3 Text §4 (line 161) holds [−0.0210, −0.0031] and
  [−0.0331, −0.0102]; Results 4 gives +0.0179 and +0.0064, S3 Text §6 (line 307) holds the early interval and S17
  Table (rows 231 and 232) both; Results 2 gives the contrasts at W = 30 and on windows 5–14 with p, and S1 Table
  holds both intervals; Results 5 and Fig 6 give the contrasts at lags 2, 3 and 5 without intervals, and S14 Table
  holds them for the sts and for the autocorrelation contrasts. Row S6's other clauses as under X1-2.
- S5 Text §5 (line 33), against the files of the review folder's `audit/`: 63 + 57 + 32 = 152 findings in the three
  audits' files; 33 + 9 + 25 + 10 + 11 + 13 + 17 + 12 + 10 + 17 = 157 in the ten `check_V*.md`; 5 + 7 + 12 + 14 + 16 +
  20 + 12 = 86 in the seven `recheck_W*.md`; the last part of the dispositions has 86 paragraphs (6 errors, 40
  inexact, 40 notes).
- `supplementary.md`, S18 Table, source line of the part on B28 (line 1590): `matched_slope_tables.md` and the table
  of S3 Text §6 have fourteen columns and the part eleven; the three left out are those the line names.
- S19 Table, head note (line 1601). The two sets as the pre-run entries of B21 and B27 list them ("What is known
  before the run"). First list: the Abstract ("p = 0.11–0.25"), Results 2 (the slope 4.26 with its interval and
  intercept), Results 4, Table 3, Fig 3 and the Discussion (−0.75) each quote a value of B21 (b) or (c), and no other
  place does. Second list: the Abstract, Tables 2 and 3, Results 2 and 4, the Discussion, Methods, Inference (g =
  0.61) and S3 Text §5 each hold a value of B27's set, and no other place of the main text does.
- S19 Table, Part B, the row of `derived_r24.out` (line 1706): each gloss against the main text and the items of the
  output (items 1 to 12); the script reads two pickles, six CSV files, two tables files, three array files and one
  log, and draws no random numbers; run again on the copy, its output equals the committed one from the second line
  (the first carries `git=nogit` for `git=8bd189e`).
- S20 Table, head note and row 5's last cell (lines 1711 and 1721), and the same cells, the title and the search
  paragraph of the literature file: the row and the cell are identical in the two files; Luppi2026.pdf p. 18 defers
  the datasets and their preprocessing to the Supplementary Methods; "deconvolution" occurs once in pp. 1–32, of cell
  types (p. 16); pp. 33–41 of that copy have no text layer and were not read here. Down2026.pdf holds 25 pages
  numbered of 55. The head note's sentence is X1-3.

**2. S19 Table, Part A, all 81 rows** (lines 1607–1687; 67 counted predictions: 36 + 15 + 16, and 14 other rows).

- Convention. A place holds a row's outcome if it prints a value of the outcome cell as that quantity, at the cell's
  precision or rounded from it, or states the outcome in words. Places that state an outcome only in words were not
  treated as missing from a cell. A value that an outcome cell cites from another row, and the values of the primary
  contrast at lag 1 in the row of B3, were referred to the row whose result they are.
- (a) Every decimal number of the 81 outcome cells was searched, as printed and in each rounding down to two
  significant digits, in every paragraph, table and caption of the main text before "## Supporting information", and
  every hit at a place that the cell does not name was read (64 rows have such hits). The 45 numbers that the main
  text prints with one significant digit at three or more decimals were traced to their sources through the numbers
  table. None is the row's outcome printed at an unnamed place; the one value that comes near is X1-7. The numbers of
  a row's computation that are not in its outcome cell are X1-8.
- (b) Every named place was opened. The 24 cells that differ between `checked2` and HEAD each hold what they add
  (the Abstract, the Discussion, Limitations, Methods, Tables 1 to 4 and Figs 2, 3, 5 and 6, as named). Of the places
  of the main text, Results 1 for B19 (b) holds none of the outcome (X1-4) and Results 7 for B16c (b) holds no level
  (X1-6). Of the places of the supporting information, those of X1-5 and X1-6 do not hold the values; every other
  named section or table holds a value of its row or states its outcome in words (in words: S5 Text §1 for the five
  rows that name "the deviations", S1 Text for the rows that name it "in summary", S3 Text §2 for B6).

**3. The dispositions** (dispositions, last part, and the paragraphs named of the part before it).

- W1-1, W1-3, W2-1, W2-5, W2-6, W3-1, W3-2, W3-3, W3-7, W3-8, W3-9, W3-10, W3-11, W3-12, W5-9 and W7-8: each
  quotation of a corrected text stands at the place named, word for word; each correction answers its finding in
  `recheck_W1.md`, `recheck_W2.md`, `recheck_W3.md`, `recheck_W5.md` or `recheck_W7.md`; what each says of a file
  holds (for W2-1, W2-5 and W2-6 by the recomputations above; for W3-8 the same kinds and counts of files in S19
  Table's row, in the record's entry on the revision, lines 9163–9164, and in the review folder's README, lines
  65–66, and they are what the script reads). W3-4 holds with the remark of X1-9; the statements that the corrections
  for W3-3, W3-10 and W3-11 wrote are X1-2, X1-1 and X1-3.
- VM-1, VM-3, VM-8, VS-3, VS-11, VS-12, VT1-8, VT2-17, VR-14 and VN-3 as they now stand: each quotation is in the
  file named, and each statement holds of HEAD (VM-3 and VS-12 by the recomputations above; VN-3 and W5-9 of both
  cells of S20 Table's row 5 on deconvolution).

**4. The rules.**

- No computation label (B1–B29, B16b, B16c, B17b) in `manuscript/draft_v2.md`, before or after "## Supporting
  information" (line 391).
- No round, stage or bundle name and no reviewer's letter in the main text, S1–S5 Text or `supplementary.md`: the
  occurrences of "stage" are a cited work's title and its reported effect ("stage-specific") and "the data-release
  stage"; "bundled" is said of third-party files; "B's" is the statistic B's; R1–R7 in S4 Text are the checklist's
  items.
- "Planning session" and "writer's session" occur in S5 Text §5 (line 33) only.
