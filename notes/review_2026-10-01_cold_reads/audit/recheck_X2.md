# X2 — the record's five new entries, the numbers table, the replacements file and the bookkeeping files

Third verification of the prepared revision. Trees: VT at HEAD (f50c1d3), against `checked2` (eed9271) and 8bd189e.
Part: `manuscript/analysis_record.md` (its last five entries), `manuscript/main_text_numbers.csv`,
`notes/review_2026-10-01_cold_reads/checks/`, the replacements file
`notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json` (below: the JSON),
`CLAUDE.md`, `README.md`, `notes/review_2026-10-01_cold_reads/README.md`, `scripts/15_figures_v2.py`, and the
dispositions that the task names. Paths are relative to VT. "The record" is `manuscript/analysis_record.md`; "the list"
is `notes/review_2026-10-01_cold_reads/checks/numbers_update.out`; "the dispositions file" is
`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`; "the main text" is `manuscript/draft_v2.md`;
`checks/` and `audit/` are those of `notes/review_2026-10-01_cold_reads/`. "CSV line n" is the line of the numbers table
at HEAD (line 1 the head note, line 2 the column names). Line numbers are those of HEAD. Nothing under VT was changed
(`git status --short` is empty at the end); every script was run on exports of HEAD, of `checked2` and of 8bd189e under
VW/X2/. No internet, no subject data.

Result: 10 findings — 0 errors, 2 inexact, 8 notes. No number, count, pointer, date or quotation that was changed or
added between `checked2` and HEAD in the files of this part was found wrong. The two inexact statements are a
description in the list, which came with the correction for W4-1, and a clause of the disposition of W6-13.

## Findings

### X2-1

- Where: the list, lines 13–15: "70 cross-references by number in the running text and the captions, to the paper's own
  sections, tables and figures (25 after "Results", 17 after "Table" and 14 after "Fig"". The disposition of W4-1
  describes the file in the same terms (the dispositions file, lines 1991–1992: "those to the paper's own sections,
  tables and figures and those to equations, definitions, an example and figures of cited works").
- Problem: One of the 17 numbers after "Table" is not of a table of the paper: "their Table 1", in the Discussion, is
  Table 1 of Luppi et al. (2022). The paper's own tables are referred to by number 16 times, and the references to
  cited works are 15, a table among them, where the sentence gives 14 in four kinds (7, 3, 1 and 3). The count of 17
  after "Table" and the total of 70 are right. The wording that separates the two groups came with the correction for
  W4-1: at `checked2` the sentence had "(Results, Fig, Table, Eq., Example, Definition, pages)".
- Evidence: the main text, line 193: "they argue against it for the six macroscale associations of their Table 1 on
  that dataset", of "The human (HCP) data of Luppi et al. (2022)"; `manuscript/si/S3_Text.md`, line 558: "the third of
  the three surrogates of their Table 1". Own tokenisation of the covered text (VW/X2/tokens.py, norow.py): the 17 are
  at lines 59, 83 (two), 87 (three), 106 (three), 110 (two), 124 (two), 158, 193, 249 and 397 of the main text; all
  but that of line 193 are Tables 1 to 4 of the paper. The 25 after "Results" and the 14 after "Fig" are all of the
  paper's own sections and figures.
- Grade: inexact

### X2-2

- Where: the dispositions file, the disposition of W6-13 (lines 2157–2158): "`check_numbers_revision.out` flags ten
  rows, each an unsigned print of a negative value whose direction the wording gives."
- Problem: Ten rows are flagged and each is an unsigned print of a negative held value. For three of the ten the
  sentence that holds the number gives a size and no direction: "moves it by 0.061 nats, 0.1 of the lag-0 correlation
  |q| by 0.019" (Abstract), "0.01 of within-pair asymmetry |a_x − a_y| by 0.031" (Results 1) and "only to within 0.053
  nats for sts" (Limitations). For the other seven the wording, or the sign printed beside the number, gives it ("fell
  by", "exceeds the observed level by", "a fall of", and for Results 1's 0.019 the derivative "∂sts/∂q = −0.19"). The
  report that the disposition answers has "whose direction or size the wording gives".
- Evidence: `checks/check_numbers_revision.out`, lines 2, 4 and 11 (its rows 10, 91 and 1216, which are CSV lines 11,
  92 and 1217; held −0.0189, −0.0309 and −0.0530); the main text, lines 15, 53 and 201; `audit/recheck_W6.md`, line
  272.
- Grade: inexact

### X2-3

- Where: the list, lines 17–18: "The digits of commit identifiers and of the names of the supporting items (S1 Text to
  S20 Table) and the numbers inside code spans are not tokens of the text". The head note of the numbers table and the
  record ("The checks", lines 9492–9493) say the same of the names of the supporting items.
- Problem: Two more digit groups of the covered text follow a letter directly, as those of the names do, have no row
  and are in none of the kinds that the three places name. One is the 4 of "Fig. S4", a figure of the SI Appendix of
  Timmermann et al. (2023): it is not in the name of one of the paper's supporting items, and it is not among the 3
  figures of cited works that the list counts ("Fig. 5", "SI Figure 14", "Fig. 3"). The other is the 540 of the
  repository's address, which is not in a code span. The head note covers the first as a cross-reference by number;
  nothing that is stated covers the second.
- Evidence: the main text, line 187: "(Timmermann et al., 2023, Methods and SI Appendix, Fig. S4; its DiD here +0.0143,
  p = 0.25)"; line 267: "are at https://github.com/Vasilis540/dmt-phiid". Own tokenisation: outside code spans,
  commit identifiers and the DOI, 150 digit groups follow a letter directly; 148 are in the names S1 Text to S20 Table
  and these are the other two. The three counted figures of cited works are at lines 27, 187 and 229. No row of the
  numbers table has the number 540, and none of the Discussion's subsection on the fall of r₁ the number 4.
- Grade: note

### X2-4

- Where: the record, "The length and the tables", lines 9420–9422: "Where a moved number stands at its new place with
  more decimals (the prewhitened values in Table 4; the band-passed generator's −0.0944 for a fall of 0.0154, the
  slope's interval in Table 3 and A_other's expectation in S18 Table;".
- Problem: The parenthesis, which the correction for W4-2 extended, now names every such number but two: the
  Abstract's 0.003 and 0.005 (committed: "against 0.003–0.005 in simulated pure autocorrelation changes"), which the
  list places in Results 4 as 0.0027 and 0.0049. What the sentence says holds of them too: the list gives both forms.
- Evidence: the list, lines 308–309: "Results 4 (the band-passed generator's residual DiD, 0.0027)" and "Results 4 (the
  AR(1) generator's residual DiD, 0.0049)"; the main text, line 124: "+0.0027 ± 0.0014" and "+0.0049 ± 0.0017". All
  64 moved numbers were compared with the form at each place named for them: more decimals stand at a named place for
  nine of the prewhitened values (Table 4), for the six that the correction added, for the 42 of Cliff et al. and for
  these two, and for each the list gives the form.
- Grade: note

### X2-5

- Where: the record, "The audits of the prepared revision", lines 9478–9485: "In the paper's files the corrections are:
  two parentheses of the main text", with the items that follow to "and two rows of S4 Text".
- Problem: Each item of the list is in the difference between `checked2` and HEAD, and every change of the main text,
  of S3 Text, of S4 Text and of the supplementary tables is one of its items. One more place of the paper's files
  changed, which the list does not name: S5 Text §5, where "and the checks of the corrections by ten further sessions,
  157 findings," became "the check of the corrections by ten further sessions, 157 findings, and a second check by
  seven more, 86 findings,". That clause answers no finding (it is the account of the second check), so that the list
  is complete as a list of the corrections and not as a list of what changed in the paper's files.
- Evidence: `git -C VT diff checked2 HEAD -- manuscript/`: `draft_v2.md` lines 87 and 241; `si/S3_Text.md` lines 260,
  406 and 556; `si/S4_Text.md` lines 53 and 62; `si/S5_Text.md` line 33; `supplementary.md` lines 1590, 1601, 24 rows
  of S19 Table's Part A (lines 1613–1686), 1706, 1711 and 1721; beside these the record and the numbers table, of
  which "The checks" speaks. No disposition of the last part of the dispositions file is of the sentence of S5 Text §5.
- Grade: note

### X2-6

- Where: the JSON, entry F09b, `why`: "with the panel 1.7 times as tall (0.20 of 0.70 for 0.10 of 0.60) the anchor is
  scaled so that the legend stays as far below the axis as it was".
- Problem: The entry's `new` now carries the comment as corrected for W5-16 ("about the same distance below the taller
  panel"), and the record, the disposition of R49 and the script's revision note say "about as far". The reason
  recorded with the replacement keeps the unqualified form. The distance is 2 % greater than it was.
- Evidence: the JSON, F09b (`old`: `bbox_to_anchor=(0.0, -0.42)`; `new`: `(0.0, -0.25)` with the comment);
  `scripts/15_figures_v2.py`, lines 26 and 474; the record, line 9515; the dispositions file, line 348. 0.25 × 0.20 /
  0.70 = 0.0714 against 0.42 × 0.10 / 0.60 = 0.0700 of the summed height ratios; 0.20 / 0.70 is 1.71 times 0.10 / 0.60.
- Grade: note

### X2-7

- Where: the record, the revision's entry, first paragraph, line 9156: "the parse check of the four scripts" (the words
  that the disposition of W4-11 quotes).
- Problem: The check that the commit adds, `checks/scripts_check_revision.out`, is of four scripts, as the phrase
  says, but not of those that the entries and the review folder's README call "the four scripts", which are the
  scripts of B27, B28, B29 and B16c. Their parse check is `checks/scripts_check.out`, a file of the earlier commit. The
  revision's is of `scripts/15_figures_v2.py`, `figures_check.py`, `derived_r24.py` and `abstract_summary.py`. The
  phrase does not say which four it means.
- Evidence: `checks/scripts_check_revision.out` (4 lines); `checks/scripts_check.out`, lines 1–4; the record, line
  8881 ("V.S. ran the four scripts on his machine at 13e7299"); `notes/review_2026-10-01_cold_reads/README.md`, lines
  39–40 and 44–45 ("the parse of the four scripts and of `run_all.sh` (`scripts_check.out`)").
- Grade: note

### X2-8

- Where: the dispositions file, beside the disposition of W6-19 (lines 2179–2182): R55 (line 382), "the build of the
  file stops on a repeated one", and W5-10 (lines 2085–2086), "the program that writes this file stops on a
  cross-reference that is not returned".
- Problem: W6-19 found that three dispositions spoke of a build that is not in the tree, and they and that of VE-20
  now speak of the planning session's preparation, "which is outside the repository". Two statements of the same kind
  are in the file without those words: R55's, which stands as it was, and W5-10's, written with the last part. No
  program that builds the replacements file and none that writes the dispositions file is in the tree. What the first
  is about holds: the 287 entries of the JSON have 287 different ids.
- Evidence: a search of the `*.py` and `*.sh` files of the tree for the names of the two files finds none; the
  numbers table is named by `notes/review_2026-09-25/checks/check_numbers.py`, `check_cells.py` and
  `notes/review_2026-09-28/revision/b25_fill.py` alone. Of the two checks "written apart from the builder" the
  disposition of R09 (lines 96–97) does say that they "are not part of the commit".
- Grade: note

### X2-9

- Where: the dispositions file, the disposition of W2-4 (lines 1897–1898): "no printed line named a computation".
- Problem: True of the printed lines of item 10, of which the finding says it ("the item's printed label names the
  file and no computation"). As written the clause is of the whole output, and printed lines of other items named
  computations then and name them now: "1. B16c", "2. B27", "3. B20", "5. B28", "B21 (d)'s formula" in item 6, "11.
  B27's table (a)" and, in item 12, "B27's pre-run entry".
- Evidence: `checks/derived_r24.out`, lines 2, 35, 41, 50, 57, 75 and 78 (the first six the same at `checked2`, where
  line 78 had "B27's pre-run entry" too); its line 72, the label of item 10, has "the split-half test's log prints
  (splithalf.log)" and no label of a computation; `audit/recheck_W2.md`, lines 74–75. The rest of the disposition
  holds: the comment of the script (its lines 222–223) names "the split-half test's log prints (splithalf.log, B7)".
- Grade: note

### X2-10

- Where: the record, "The audits of the prepared revision", lines 9473–9474: "and again no value of a result in the
  main text or in the supporting information was found wrong".
- Problem: True of the six findings graded error, none of which is of such a value. One finding graded inexact is of
  values: W2-1, three limits of the Fisher-z intervals of the residual's cross-half correlations in S3 Text §6, each
  of which the correction moved by 0.001. The same paragraph names them among the corrections (lines 9480–9481), so
  that the sentence holds of the findings graded error and not of every finding.
- Evidence: `audit/recheck_W2.md`, W2-1 (from line 17); `git -C VT diff checked2 HEAD -- manuscript/si/S3_Text.md`,
  line 406: "−0.270]" to "−0.269]", "−0.099]" to "−0.098]" and "[−0.566," to "[−0.567,"; own recomputation from the
  committed per-subject series gives [−0.897, −0.269], [−0.857, −0.098] and [−0.567, +0.493], and from the
  correlations at three decimals the earlier limits.
- Grade: note

## Not checkable from the tree

What the dispositions of VB-8, VB-20, VT2-14 and VE-20 say that the planning session's preparation of the table and of
the revision counts, stops on and tests (what they are about was checked: see below). That `recheck_W1.md` to
`recheck_W7.md` are as the sessions returned them (the review folder's README). The pages of the PDFs that the reasons
of PM02 and S314 give (they agree with W7-6 and W7-8, and those of S314 with the claim record's section on Gatica et
al., 2024). The commit in the first line of `checks/derived_r24.out` (`git=8bd189e`; an export has no history and
prints `nogit`). V.S.'s decision of 2 October 2026.

## Checked and found exact

**1. The record.**

- The rules. The file at 8bd189e (814,068 bytes) is a byte prefix of the file at HEAD (885,313 bytes); 660 lines are
  added. No line of the five entries is longer than 120 characters, headings apart (84 lines of exactly 120; no tab,
  no trailing space). The five headings have the form "## <title>, 3 Oct 2026 00:46 UTC (appended; nothing above
  edited)".
- The delta. The five entries were extracted at `checked2` and at HEAD, each paragraph's lines joined, and compared
  word by word: 42 paragraphs on each side; beside the time of the five headings ten paragraphs changed. Every changed
  span was read against its source.
- "B27, outcome". Item 12 of `checks/derived_r24.py` holds twelve values (`ENTRY12`) and each is the value that the
  pre-run entry's item (i) prints (record, lines 8610–8612, 8621–8622 and 8628: r² = 0.79; 0.0887 and 0.0485; +0.0949,
  −0.1121 and −0.0172; −0.2795 and +0.0914; −0.753, +0.0005 and −0.780; −0.788). The item recomputes the twelve and
  prints "compared with the entry's values as printed there: 12 of 12 equal"; an own recomputation from
  `notes/review_results/partB/baseline_gap.csv` gives the same twelve. `baseline_gap_tables.md` prints the slope and r
  (line 33; r in its table (b) too, line 27) and none of the nine others (the strings 0.0005 and 0.0172 stand there as
  a limit of an interval or a p value of other quantities, lines 13, 19 and 20); −0.788 is in
  `matched_slope_tables.md`, line 6.
- "B28, outcome", item (iii). Subject 8 is named at the floor in Table 3's caption (main text, line 126), in S3 Text
  §6 (line 395) and in the source line of S18 Table's part on B28 (`supplementary.md`, line 1590). Fig 3's caption
  (line 110) quotes −0.200 and has "rescaled and floored as Table 3's caption says", with no subject named. S19
  Table's rows B28 (a) to (d) (lines 1675–1678) give the conditions' values and name neither the floor nor the
  subject. Among the manuscript files "floor" stands at these four places and once more, in "the noise-floor
  prediction" of another row of S19 Table (line 1608).
- The revision's entry, first paragraph. `git -C VT diff --stat 8bd189e HEAD` shows twelve files added to `checks/`:
  the seven `*_revision.out` outputs (apply, check_numbers, check_cells, tablecheck, wc, abstract_summary,
  scripts_check), `abstract_summary.py`, `derived_r24.py`, `derived_r24.out`, `numbers_update.out` and
  `figures_check.py`. The paragraph's list names the seven outputs, `derived_r24.py` with its output, the update of
  the numbers table and `figures_check.py`; the twelfth file, `abstract_summary.py`, is the counter whose output it
  names (on the parse check, X2-7). `derived_r24.py` reads two pickles (its lines 45 and 149), six CSV files (64, 79,
  102, 116, 140 and again 251, 172), two tables files (94, 301), three array files (168; 257, for both variants) and
  one log (239), and no other file; the module it imports, `notes/rev_inference_inverted.py`, reads none.
- "The revision." Each of the nineteen works that the paragraph names (the seven added; Barrett, 2015; Liardi et al.,
  2025; Luppi et al., 2022, 2023, 2024 and 2026; Cliff et al., 2021; Down et al., 2026; Gatica et al., 2024; Murray et
  al., 2014; the two source papers) has a section in `claims/claims_2026-10-01.md`, and the claim record has no other
  section. The sentences on ketamine are those of S3 Text §10 (line 556): "ketamine[Title/Abstract]" is the last term
  of the string of 2 October 2026; the macaques of Luppi et al. (2026) "scanned awake and under sevoflurane, propofol
  or ketamine"; those of Gatica et al. (2024), "scanned under isoflurane", with "an injection of ketamine with other
  agents"; "Data under anaesthesia are not counted here as psychedelic data".
- A's m8. Fig 1's title (line 55); "the sts surface of Fig 1a" in the Discussion (line 191) and in the list's entry of
  S20 Table (line 441); "the sts surface over (r₁, q)" in its entry of S3 Text (line 397); "the plans called it the
  scope map, a name the file names keep" (S3 Text §4, line 128) and "in the plans' own names, scope map" (S5 Text §1,
  line 7). "scope map" occurs at no other place of the manuscript files outside file names.
- A's w1. "artefact" occurs five times in the manuscript files: once in the main text ("the fall is not an artefact",
  line 187), in S3 Text at line 305 (the plan's words, quoted) and at line 550 (§9, in the file at 8bd189e too), and
  in S19 Table's rows B2 and B3 (lines 1617 and 1618, the plan's word). The sentence of §9 is as the record now gives
  it: the paragraph's ratio is "the ratio of window variance to run variance", and residualising on it "would remove
  the part of the r₁ change that coincides with the variance change, not an artefact of scale".
- B's MINOR 8. Each place was opened. Marked post hoc: the r₁ contrast (line 106), the leave-one-out (87) and S8
  Table's check (108) in Results 2; the relation on the windowed atoms in Results 3 (114); the spectral centroid in
  Results 5 (146); the deconvolved contrast in Results 7 (171), the deconvolution being named in the first row of S19
  Table's Part B (`supplementary.md`, line 1695). Said to rest on a rule or a prediction recorded beforehand: "fixed in
  the record before the partialled map was computed" (Results 3, line 114) and "fixed before the partialled map was
  computed" (Fig 4's caption, line 116), with "below the range predicted for it" at both; "a prediction recorded
  before it was computed" (Discussion, line 187); "were computed under rules and predictions recorded beforehand", of
  A_other, the five constructions with their expectations and the generators' slopes (Methods, line 245, under the
  heading of line 243); "several recorded predictions failed" (Limitations, line 201). ΦR's p values stand without a
  threshold (Results 6, line 154); the Author summary has "relative to placebo" (line 19). Methods has "(the text
  repeats it for several)" (line 241).
- C's M1. The Ethics statement (line 209): "This is a secondary analysis of derivatives released by the data authors
  (Singleton et al., 2025); the quantities it uses carry no demographic, image or identifying field, no new data were
  collected and no participant was contacted".
- "The length and the tables". The six forms are at the places: "−0.09441 / −0.01540" (Fig 3's caption, line 110) and
  "−0.09441 for −0.01540" (S13 Table's note, `supplementary.md`, line 363); "−1.133 to −0.373" (Table 3, line 130)
  beside "[−1.13, −0.37]" (Results 4, line 124); "+0.00001 ± 0.00031" (S18 Table, line 1577) beside "+0.0000 ±
  0.0003" (S3 Text §6, line 343); 41.8 % in S3 Text §8 (line 546). The word counts are those of
  `checks/wc_revision.out`: 8,489 with headings and 8,362 without, with 29 heading lines and 127 heading words.
- "The audits of the prepared revision". The seven reports hold 5, 7, 12, 14, 16, 20 and 12 findings, 86 in all; by
  the grades that the findings carry, W1 0/4/1, W2 1/3/3, W3 0/6/6, W4 1/5/8, W5 2/7/7, W6 2/8/10, W7 0/7/5: 6 errors,
  40 inexact, 40 notes. The six errors are W2-4, W4-1, W5-1, W5-2, W6-1 and W6-2, which are four things (W4-1, W5-2
  and W6-1 are the count; 64, 74 and the ten panel references are as those reports found them, and 70 is the count at
  HEAD); none is of a value of a result in the paper's files (X2-10). The last part of the dispositions file has 86
  paragraphs, each with the grade of its report: 85 "Corrected." and 1 "Stated." (W5-14), fourteen of them by a
  pointer to another; twelve things were found by two or three sessions. The seven parts that the sentence names are
  those of the seven reports' titles. The list of the corrections: X2-5.
- "The checks". 1,381 rows; 264 deleted (161 + 64 + 7 + 28 + 4) and 447 added (277 + 65 + 19 + 86); the 7 that the
  second check found are 3 label notes (CSV lines 1197, 1278, 1279), 1 held string (583) and the note of 3 committed
  rows of N = 14 (14, 20, 342), which 14 added rows had taken too (386, 454, 460, 466, 472, 484, 490, 496, 502, 542,
  813, 1052, 1207, 1301). The main text carries no computation label before "## Supporting information" (line 391);
  "planning session" and "writer's session" occur in S5 Text line 33 (§5) alone among the manuscript files.
- A string test of the four outcome entries: each of the 299 different decimals of three or more places that they
  hold stands, its sign apart, in one of the four computations' tables files, in `prewhiten_tables.md` or in
  `checks/derived_r24.out`.

**2. The numbers table.**

- `checked2` to HEAD by (section, paragraph, number, occurrence): 1,381 rows on both sides, the same keys in the same
  order; 34 rows changed. 17 notes of N = 14, now "N = 14 subjects (the shape of the data: 14 subjects × 2
  conditions)", which is the record's line 48 ("- Indexing: `[subject, condition]`, 14 subjects × 2 conditions"); 34
  rows cite that line (19 committed rows of N = 14, 1 of Table 2's caption, 14 added). 4 contexts of Results 2,
  paragraph 1 (CSV lines 390–393), which follow the reworded parenthesis. 1 held string (CSV line 583: "0.830";
  `notes/review_2026-09-24/checks/derived_r17.out`, line 20: "ts_gsr: other twelve omissions, mean cross-half r
  0.680-0.830; ratio 0.949-0.970"). 1 derivation (CSV line 1053): line 135 of
  `notes/review_results/inference_rows_prewhiten_fixed.csv` is the row "prewhiten_fixed ar20 MMI sts ts_gsr
  W60,primary", with did −0.012672600820, pre_dmt 0.071895253309 and share_of_pre −0.176264777; 0.012673 / 0.071895 =
  17.6 %, the share is −0.1763, and the text's 18 % follows from it as from 17.7 %. 5 anchors with "@pct|" (CSV lines
  1078, 1087, 1096, 1105, 1114): lines 10–14 of `notes/review_results/partB/whitened_spectrum_tables.md` hold 0.001,
  0.003, 0.338, 0.512 and 0.597 in the column of the share above 0.08 Hz, and Table 4 prints 0.1, 0.3, 33.8, 51.2 and
  59.7 %; with the row of 99.2 (CSV line 1072) six rows carry the mark, and no other data row needs it. 3 label
  notes, each now of its own token ("q = 0: no cross-correlation"; "x_{t+1}, y_{t+1}: formula", twice). 3 locators
  moved in the claim record (CSV lines 1201 and 1230 to line 67, 1231 to line 56), where the anchors stand.
- The head note, word by word: nine changed spans, each true (the six kinds of the seven rows of numbers that the
  rewritten sentences no longer state; "a committed log" and the supporting information among the sources of the
  added rows; the sentence on the second check; the panel references, with "pages" gone, of which the covered text
  has none; the names of the supporting items, on which X2-3; the three forms of "@La-b|"). The three ranges in use
  are lines 10–26 of `family_atoms_tables.md` (165 rows; the body of a table whose head is at lines 8–9), lines 11–20
  of `regional_partial_tables.md` (3 rows; a table with its head) and line 104 of `diagnostic_alternatives_tables.md`
  (1 row; a line of prose).
- The whole table at HEAD, by own code (VW/X2/blocks.py, tokens.py, place3.py, locators.py, values.py, norow.py). 787
  data, 266 design, 262 label, 54 derived, 7 literature and 5 bound rows. Each of the 1,381 contexts occurs exactly
  once in the block that the row's section and paragraph name, with the row's number on a token 60 to 64 characters
  into it or as the ends of the block cut it (two contexts, of CSV lines 645 and 1229, end where their paragraph
  ended before the revision); the rows sit on 1,381 different tokens, in reading order, and each occurrence is the
  row's rank among the rows of its paragraph with its number. All 1,065 line locators: the anchor is on the named
  line, the prefixes removed, and the line lies in the range of the 169 rows with "@La-b|"; the held string is on the
  line for the 792 data and bound rows; the 262 label rows have no source and the 54 derived rows a derivation. The
  787 data rows equal their held string at the printed precision, half away from zero (761 with one held number, the
  six "@pct|" rows as percentages; 15 held strings that contain the number, such as "14/14"; 1 in scientific
  notation; the 10 unsigned prints of negative values).
- The tokens of the covered text (title; Abstract to the end of Data and code availability; the list of supporting
  information) without a row, by kind, as the list gives them: 95 citation years; 13 day numbers and 11 years of the
  dates; 10 numbers of the captions' heads; the DOI; 70 cross-references by number: 25 after "Results", 17 after
  "Table", 14 after "Fig", 10 of these before a panel letter, and 7, 3, 1 and 3 after "Eq." or "Eqs.", "Definition",
  "Example" and "Fig." or "Figure" of cited works (on these, X2-1 and X2-3). The headings hold 9 tokens (0 to 7 and
  the 1 of AR(1)). Exactly 5 label rows sit on tokens of the excepted kinds (CSV lines 39–42 and 1235). The version
  1.7.0 of rsHRF has one row, on 1.7, whose note says so. No other token is without a row.
- 8bd189e to HEAD: the 264 rows that the list gives as deleted are rows of the committed table, as a multiset; 934
  rows are carried and 447 added (277 data, 62 design, 3 literature, 19 derived, 86 label); 281 carried rows changed
  in context and 4 in number; 91 changed in source, locator or note: 17 moved (11 in the figure script, 5 in
  `supplementary.md`, 1 in the literature file), 13 anchors, 19 rows of N = 14, 1 held string, 37 (13 + 5 + 9 + 1 + 5 +
  1 + 1 + 2) and the 4 of the second check that are not among these. The added rows cite the sources that the head
  note lists: 8 cite S3 Text, 15 `supplementary.md` (lines of S2, S6, S15 and S18 Tables), 1 a log
  (`residual_source.log`), 21 the record, 3 the claim record, 2 the files of the PubMed searches, 4 scripts, the
  others the run's tables, `derived_r24.out` and committed tables.
- The list, read in full. The paragraph on the corrections after a second check; the explanation of the two prefixes;
  the six forms "as −0.09441", "as −0.01540", "as +0.00001", "as 0.00031", "as −1.133" and "as −0.373"; the two
  quotations ('chosen by the Bayesian information criterion (BIC) in 1–5' is in Table 4's caption, line 160; Results
  2, paragraph 1, has "in each leave-one-out refit on each variant" and four 14s: one of "13 of 14", two of "14 of 14",
  one of "windows 5–14"); "(S3 Text §4, §10)" (main text, line 193). The deleted rows are 161, 64, 7, 28 and 4 by
  class; each of the 64 numbers taken out of its paragraph is at the place named for it, in the form given. The 24
  rows carried by a fallback (20 by the only token, 4 by the neighbouring text) are quoted as they stand in the
  committed and in the revised text.
- The check outputs reproduce on an export of HEAD, byte for byte: `check_numbers.py` ("rows 1381, data rows 787,
  flagged 10"; 11 at `checked2`, the row of 0.83 among them), `check_cells.py` ("flagged 0"), `tablecheck.py` on the
  seven manuscript files ("rows with a wrong cell count: 0"), `wc.py` ("total with headings 8489 without 8362") and
  `abstract_summary.py` ("abstract 300 words (limit 300); author summary 200 words (limit 200)"); the four scripts of
  `scripts_check_revision.out` parse. The ten flagged rows were read (X2-2).

**3. The derived numbers.**

- `derived_r24.py` on an export of HEAD gives `checks/derived_r24.out` line for line but for the first (`git=nogit`
  against `git=8bd189e`).
- The difference of the script: the docstring names items 9 to 12 as they are; the comment of item 10 names the log
  of the split-half test (`splithalf.log`, B7), which `notes/partB7_splithalf.py` writes (its lines 20 and 141), and
  the item's printed label names the file and no computation (on the clause of the disposition, X2-9); the halves of
  item 10 are those of that script (line 40). Item 10 recomputed by own code from the two
  `diag_series_<variant>_W60.npz` files and `splithalf_subjects.csv`: −0.385 [−0.760, +0.183], −0.700 [−0.897,
  −0.269], −0.598 [−0.857, −0.098], −0.051 [−0.567, +0.493]; means −0.5420 and −0.3245; reliabilities 0.494 and
  0.741, 0.216 and 0.712; ceilings 0.605 and 0.392.
- Item 11. The bound holds: for an assignment whose mean has the observed sign the difference of the two absolute
  means is −2/14 times the sum of the flipped values, and for one of the other sign −2/14 times the sum of the others,
  so that values each within 0.5 × 10⁻⁶ move it by at most k/14 × 10⁻⁶; the file gives the gaps to six decimals
  (`notes/partB27_baseline_gap.py`, line 160). Exact recomputation in integers of 10⁻⁶ over the 16,384 assignments:
  3,068 counted (0.1873); two assignments and their mirrors counted with a margin within the bound (a tie, k = 9,
  0.64 × 10⁻⁶; 6/14 = 0.43 × 10⁻⁶, k = 7, 0.50 × 10⁻⁶); none uncounted within it; 3,064 to 3,068; 3,066 is the one
  even count that prints 0.1871.
- Item 12: as under "B27, outcome" above; the unrounded values are r² 0.78849, SDs 0.088676 and 0.048548, slope
  −0.75331, intercept 0.000502, r −0.78024 and ratio of means −0.78757.

**4. The replacements.**

- The JSON of HEAD applied to an export of 8bd189e with `notes/review_2026-09-25/revision/apply_replacements.py`: 287
  entries, each "ok", 287 different ids; 15 files written, which are all the files of 8bd189e that differ at HEAD; 14
  are identical with HEAD's and the record differs in its five headings alone (lines 8875, 8976, 9045, 9092, 9150:
  «ENTRY_TIME»). The output is identical with `checks/apply_revision.out`.
- `checked2` to HEAD: 277 entries to 287; no entry removed, no `old`, `count` or `file` changed. `why` changed in 21:
  A01, I03, R201, R205, R403, D04, M06, DCA01, PM02, S314, S417, S420, U08.1 to U08.6, U09b, U11, LT03 (`new` too in
  fifteen of them: all but A01, I03, R205, R403, D04 and DCA01). `new` alone changed in 18: S305, S310, S502, U05,
  U06, U06d, U09e, U17b.1, LT01, LT07b.1, F09b, N01, C03, C08, C12, K01, RR03, REC01. New: U09f.1 to U09f.10.
- Each changed or new `why` was read against its `old`, its `new` and the places it names, and is true; every phrase
  that one of them puts in quotation marks is at the place it gives it to (among them 'most fMRI synergy reports we
  found' and 'the ten empirical studies we found', in the `new` of A01 and of D04). In particular: I03 (the sentence
  on the record's order and the sentence listing the Results sections are in `old` and not in `new`; Methods has the
  first, line 261); R201 (r² 0.75 and 0.79; 0.30 of the variance, `derived_r24.out`, item 9, and S3 Text §5, line
  260); R205 and R403 (the forms at the places; −0.094 in the Abstract and in the Discussion); M06 (each place it
  names; S19 Table's row B22 (e), line 1652); DCA01 (eight review folders in `old`, each in S5 Text §5 with the folder
  of this revision; the scripts as a range and two names in `old` and `notes/partB*.py` in `new`; the last paragraph
  of S5 Text §4); S314 (C32 of the citations audit is on ketamine); S417 and S420 (what the two rows of S4 Text now
  say; S3 Text §5, line 165, gives the leave-two-out without a word on its status); U08.1 to U08.6, U09b and U09f.1 to
  U09f.10 (each place added to a cell prints the row's values or, where the cell says "in words", states the outcome:
  Table 1's "−0.0078 (10)"; the four contrasts of Fig 6's caption; the Abstract's "r = 0.86", "4.7" and "0.95", with
  [0.26, 0.89]; the Discussion's 0.0115, "0.003–0.005", "4.7-fold" and 0.95; Fig 2's "+0.0115" and "0.008"; Fig 5's
  +0.0115, +0.0027 and +0.0049; −0.39 in Results 4, Table 3 and Fig 3; Table 3's caption and its second and third
  rows for −0.18; "several recorded predictions failed, among them the calibration's for a coupling change" in
  Limitations; the two places of S3 Text §6, lines 323–335 and 339–372); U11 and LT03 (pages 1–25 of 55, S20 Table's
  row 6; the two dates of row 10). The reasons whose `why` did not change remain true of their changed `new` (on
  F09b, X2-6).

**5. The bookkeeping files.**

- `CLAUDE.md`: 8,489 and 8,362 words; "(Table 3 is named before that in Fig 3's caption, twice)" (the caption names
  Table 3 twice and no place before it does; each of the ten captions follows the paragraph of its first citation);
  "twice (ten sessions, then seven)". `README.md`: 8,489 words.
- `notes/review_2026-10-01_cold_reads/README.md`: the twelve values of item 12; the kinds and counts of the files
  that `derived_r24.py` reads; the seven `*_revision.out` outputs and `abstract_summary.py`; the audit folder's 24
  files are all named (the ten `check_V*.md`, `recheck_W1.md` to `recheck_W7.md`, the three `findings_*.md`,
  `te_filter_check.py`, `dispositions_revision.md`, `findings.md`, `dispositions.md`). The other 59 files of the
  folder are all named, and every file of the folder that it names exists but `figures.out`, which it says comes with
  the figures commit.
- `scripts/15_figures_v2.py`: one comment changed (line 474), as the disposition of W5-16 quotes it.

**6. The dispositions.**

- The last part: W2-2, W2-3, W2-4, W4-1 to W4-14, W5-16 and W6-1 to W6-20 were each read against its finding in
  `audit/recheck_W2.md`, `recheck_W4.md`, `recheck_W5.md` and `recheck_W6.md` and against HEAD. The grade each gives
  is the report's. Every passage they put in quotation marks after the verdict is at the place named, word for word
  (31 passages, tested by code and read), and the paragraphs that those of the form "As W2-3." point to hold (W2-3,
  W2-7, W3-2, W3-8, W4-1, W4-2, W4-6). Each correction answers its finding, with X2-1 on the wording of W4-1, X2-2 on
  a clause of W6-13 and X2-9 on a clause of W2-4.
- The part before it: VO-2 (S3 Text §8, line 544, and S19 Table's row B16c (e), line 1687, say "in
  `inference_rows_prewhiten_fixed.csv` and in `derived_r24.out`, item 1"; the entry alone has "with its inverted
  interval", and its two values are those of item 1), VO-6, VE-8 (the reasons of I03 and of A02), VE-13, VE-20 (of the
  27 sections between the Introduction and the end of Methods that have text of their own, Redundancy functions and
  Regional maps alone are word for word those of 8bd189e), VE-23, VB-8, VB-20 (13 + 5 + 9 + 1 rows, 37 with those of
  VB-21 to VB-23 and VR-2), VB-25, VB-27, VT2-14 (`check_numbers.py` tests the held string of the data rows and no
  anchor) and VM-10 (the three lines: line 4 of `family_atoms_tables.md`, the record's lines 1747 and 48) are true of
  HEAD as they now stand, and the 15 passages that they put in quotation marks after the verdict are at their places
  word for word.
