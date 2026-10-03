# W6 — the numbers table, the replacements file and the bookkeeping files

Second verification of the prepared revision. Tree: VT at HEAD (eed9271), against `checked` (9caa60b) and 8bd189e.
Part: `manuscript/main_text_numbers.csv`, `notes/review_2026-10-01_cold_reads/checks/numbers_update.out`,
`notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json` (below: the JSON),
`CLAUDE.md`, `README.md`, `notes/review_2026-10-01_cold_reads/README.md`. "CSV line n" is the line of
`manuscript/main_text_numbers.csv` at HEAD (line 1 the head note, line 2 the column names); "draft line n" is the line
of `manuscript/draft_v2.md` at HEAD. Nothing under VT was changed.

20 findings: 2 error, 8 inexact, 10 note.

## Findings

### W6-1
- Where: `notes/review_2026-10-01_cold_reads/checks/numbers_update.out`, lines 13–14: "64 cross-references by number in
  the running text and the captions (Results, Fig, Table, Eq., Example, Definition, pages)".
- Problem: The count does not reproduce. Of the number tokens of the covered text (title to the end of Data and code
  availability, and the list of supporting information; headings apart) that have no row, 74 are cross-references by
  number: Results 29, Table 17, the paper's own Fig 14, "Fig." of cited works 2, "SI Figure" 1, Eq./Eqs. 7, Example 1,
  Definition 3. The 64 are those whose number is not directly followed by a letter. The ten of the form "Fig 1a" are in
  no count of the file, although they have no row and the sentence gives its counts as those of every token left
  without a row. The table does give rows to digits that a letter follows directly, two of them added in this revision.
  None of the 74 is a page.
- Evidence: a tokenisation of draft_v2.md at HEAD written for this check, set against the 1,381 rows (every row maps
  to one token; the sentence's other counts reproduce: 95, 13, 11, 10, the DOI, and 9 in the headings). The ten: draft
  line 53 "Fig 1a"; 57 "Fig 1c"; 108 "Fig 3a, b" and "Fig 3b"; 114 "Fig 4a", "Fig 4b", "Fig 4c"; 124 "Fig 3c"; 191
  "Fig 1a"; 441 "Fig 1a". Rows on a digit directly followed by a letter: CSV lines 68, 71, 1261, 1267 ("2S"; the last
  two are added rows), 1035 ("2π"), 110–112 ("50th, 80th and 95th"). The earlier check counted 73 at `checked`
  (`audit/check_VB.md`, line 51: "73 cross-references in running text (Results 28, Table 17, Fig/Fig./Figure 17,
  Eq./Eqs. 7, Definition 3, Example 1)"); HEAD adds "Results 4" in Results 2, paragraph 3 (draft line 108).
- Grade: error

### W6-2
- Where: the JSON, entry DCA01, `why`: "the names of the nine review folders, which S5 Text §5 gives; and the
  calibration scripts listed one by one, for which the sentence now has `notes/partB*.py`".
- Problem: The `why` gives these as details that the replacement takes out of Data and code availability. The
  committed sentence names eight review folders, not nine: the ninth that S5 Text §5 names,
  `notes/review_2026-10-01_cold_reads/`, was not in it. And the committed sentence does not list the calibration
  scripts one by one: it gives a range and two names. (The count is the error; the second point is an inexactness.)
- Evidence: DCA01's `old`: "(`notes/`, `notes/review_2026-09-20/`, `notes/review_2026-09-22/`,
  `notes/review_2026-09-24/`, `notes/review_2026-09-25/`, `notes/review_2026-09-26/`, `notes/review_2026-09-28/`,
  `notes/review_2026-09-30/`, `notes/review_2026-10-01/`)" and "(`notes/partB14_*.py`–`partB26_*.py`,
  `partB16b_*.py`, `partB17b_*.py`; `notes/review_results/partB/`)". `manuscript/si/S5_Text.md`, line 33 (§5), names
  those eight folders and `notes/review_2026-10-01_cold_reads/`.
- Grade: error

### W6-3
- Where: the JSON, entry R201, `why`, last sentence: "r² being as high for the post-injection gap (0.75) as for the
  pre-injection gap".
- Problem: r² of the DiD with the pre-injection gap is 0.79, with the post-injection gap 0.75. S3 Text §5, which the
  same sentence cites, says "nearly as closely".
- Evidence: `checks/derived_r24.out`, line 36 ("r(DiD, pre gap) -0.888, r² 0.79") and line 71 ("r(DiD, post gap)
  +0.868"); recomputed from `notes/review_results/partB/baseline_gap.csv` (sts, ts_gsr, W = 60): r = −0.88797 and
  +0.86807, r² = 0.7885 and 0.7535. `manuscript/si/S3_Text.md`, line 260: "the DiD follows the post-injection gap
  nearly as closely as the pre-injection gap (r = +0.868 against −0.888)".
- Grade: inexact

### W6-4
- Where: `manuscript/main_text_numbers.csv`, head note: "an anchor written "@La-b|" before a string names the table
  that occupies lines a to b of the file"; `numbers_update.out`, line 48: ""@La-b|", the table in lines a to b".
- Problem: Three ranges are in use. One names a line that is not a table: CSV line 1324 (Methods, 0.786) has "anchor:
  @L104-104|r₁ +0.78638", and line 104 of its source is a line of prose. Of the other two, "@L10-26" (165 rows) is the
  body of a table that occupies lines 8–26 of its file, and "@L11-20" (3 rows) is a table with its header.
- Evidence: `notes/review_results/partB/diagnostic_alternatives_tables.md`, line 104: "Unperturbed AR(1) pairs,
  levels: observed sts +0.71753; AR(1)-substituted sts +0.78788 [11]; residual -0.06998 [11]; r₁ +0.78638; …" (lines
  103 and 105 are blank; the table begins at line 106). `notes/review_results/partB/family_atoms_tables.md`: header
  and rule at lines 8–9, body at 10–26. `notes/review_results/partB/regional_partial_tables.md`: the table at lines
  11–20. The row of line 1324 is a committed row, the same at 8bd189e; the explanation of the notation is new at HEAD.
- Grade: inexact

### W6-5
- Where: `manuscript/main_text_numbers.csv`, head note, on the 7 rows of numbers no longer stated: "(a threshold
  replaced by the p values themselves, a repeated limit, a second mention, a count, a clause that is not carried)".
- Problem: The five kinds cover six of the seven rows (the threshold 0.05 twice, 0.0112, the 4 of Table 1's caption,
  the 14 of the refits, the 2 of "TR 2 s"). The seventh, Results 3's 0.0001, now written "p < 1/10,000", is of none of
  the five; the record's sentence names it as a sixth kind.
- Evidence: `numbers_update.out`, lines 314, 325, 335, 351, 352, 357, 382 (the seven rows "no longer stated"); line
  335: "the spin p is now written 'p < 1/10,000' (the same statement; B's W1), whose 1 and 10,000 have rows".
  `manuscript/analysis_record.md`, lines 9404–9406: "(a threshold replaced by the p values themselves, a repeated
  limit, a second mention, a count of refits, a clause that is not carried, and the spin p rewritten as p < 1/10,000)".
- Grade: inexact

### W6-6
- Where: `manuscript/main_text_numbers.csv`, the note of 17 rows: CSV lines 14, 20, 342 (committed rows) and 386, 454,
  460, 466, 472, 484, 490, 496, 502, 542, 813, 1052, 1207, 1301 (added rows): "N = 14 subjects (the per-subject rows of
  the primary result)".
- Problem: The parenthesis describes neither source of these rows. They cite the record's line on the shape of the
  data, which is not a per-subject row of a result; and the file of the primary result, which the three committed rows
  cited until this revision, holds no per-subject rows.
- Evidence: the 17 rows have `manuscript/analysis_record.md`, "line 48; anchor: 14 subjects × 2 conditions"; the
  record's line 48: "- Indexing: `[subject, condition]`, 14 subjects × 2 conditions".
  `results/primary_b_ts_gsr_win60.csv` (72 lines): a header line, the column names and 70 rows of group statistics
  (sections A, A.fd, A.primary, A.sensitivity, B.primary, B.sensitivity). The other 17 rows on the record's line 48
  have the notes "N = 14" (12), "N = 14 subjects" (4) and "design: N = 14" (1).
- Grade: inexact

### W6-7
- Where: `numbers_update.out`, line 360 (Results 7, paragraph 1, the deleted "1"): "Table 4's caption ('p by BIC over
  1–5'), where it has a new row with the same source".
- Problem: The words in quotation marks are not in Table 4's caption, which has "chosen by the Bayesian information
  criterion (BIC) in 1–5". They are the new row's anchor (the words of the source line) and the words of Methods.
- Evidence: draft line 160 (Table 4's caption); draft line 249 (Methods: "(p by BIC over 1–5, or p fixed at 1, 10 or
  20; S11 Table; Table 4)"); `notes/review_results/partB/prewhiten_tables.md`, line 4 ("p by BIC over 1–5"); CSV line
  1065 (the new row: "line 4; anchor: p by BIC over 1–5"). The rest of the line holds: the committed row (line 984 of
  the table at 8bd189e) had the same source, locator and note.
- Grade: inexact

### W6-8
- Where: `numbers_update.out`, line 325 (Results 2, paragraph 1, the deleted "14"): "(the paragraph's other 14s are of
  '14 of 14')".
- Problem: The paragraph has four 14s at HEAD. Two are of "14 of 14"; the other two are of "13 of 14 subjects" and of
  "windows 5–14".
- Evidence: CSV lines 379 ("negative in 13 of 14 subjects"), 385 and 386 ("negative in 14 of 14"), 398 ("on windows
  5–14"); draft line 87.
- Grade: inexact

### W6-9
- Where: `numbers_update.out`, lines 332–333 ("−0.0944 | taken out of the paragraph | Fig 3's caption (a) and S13
  Table's note", and the line of 0.0154), lines 348–349 ("+0.0000 | taken out of the paragraph | S3 Text §6 and S18
  Table", and the line of 0.0003) and lines 377–378 ("−1.13 | taken out of the paragraph | Table 3 and Results 4",
  and the line of −0.37).
- Problem: Six numbers stand at a place the list names with more decimals than the deleted row had, and the list does
  not say so: −0.09441 and −0.01540 at both places named for them; +0.00001 ± 0.00031 in S18 Table (S3 Text §6 has
  +0.0000 ± 0.0003); −1.133 and −0.373 in Table 3 (Results 4 has −1.13 and −0.37; the −0.37 that Table 3 does print
  is the null's rate, another quantity). For the other numbers that stand at their new place in another form the
  list gives the form (0.0027, 0.0049, Table 4's values, 41.8 %), and the record says of the list that it does so.
  The other 58 numbers "taken out" stand at the places named as the deleted row had them or in the form the list gives.
  Two reasons of the JSON place the same numbers in the same way: R205 ("the band-passed generator's −0.0944 for a
  fall of 0.0154 is in S13 Table's note and Fig 3a's caption") and R403 ("its expectation under a pure autocorrelation
  change (+0.0000 ± 0.0003) in S3 Text §6 and S18 Table").
- Evidence: draft line 110 (Fig 3's caption (a)): "6.13 per unit of pair r₁ (−0.09441 / −0.01540;";
  `manuscript/supplementary.md`, line 363 (S13 Table's note): "(B24: −0.09441 for −0.01540)", and line 1577 (S18
  Table): "| A_other (sign from the other run) | −0.00028 ± 0.00019 | +0.00001 ± 0.00031 |";
  `manuscript/si/S3_Text.md`, line 343: "against +0.0000 ± 0.0003"; draft line 130 (Table 3): "| data | −0.753 |
  −1.133 to −0.373 |"; draft line 124 (Results 4): "(t interval [−1.13, −0.37])"; `manuscript/analysis_record.md`,
  lines 9407–9409: "Where a moved number stands at its new place with more decimals (the prewhitened values in Table 4;
  Cliff et al.'s 42 %, which is 41.8 % in S3 Text §8, as their text gives it), the list says so."
- Grade: inexact

### W6-10
- Where: `CLAUDE.md`, line 19 (replacement C12): "(Table 3 is named once before that, in Fig 3's caption)".
- Problem: Fig 3's caption names Table 3 twice.
- Evidence: draft line 110: "rescaled and floored as Table 3's caption says" and "pair r₁ DiD; Table 3; S3 Text §6;
  S18 Table)". The rest of the sentence holds: each of the ten captions stands after the paragraph of its first
  citation in the running text, and Table 3 is named at no other place before Results 4, paragraph 2 (draft line 124).
- Grade: inexact

### W6-11
- Where: `manuscript/main_text_numbers.csv`, head note: ""@pct|" marks a value that the text prints as a percentage".
- Problem: Six rows print as a percentage a value that the source holds as a fraction; one carries the mark. The five
  rows of Table 4's body, which the revision adds, do not (their notes say "as a percentage").
- Evidence: CSV line 1072 (99.2: "the line holds 0.992; anchor: @pct|| raw | 0.992"); CSV lines 1078, 1087, 1096, 1105,
  1114 (0.1, 0.3, 33.8, 51.2, 59.7; held 0.001, 0.003, 0.338, 0.512, 0.597; anchors "| raw |", "| ar1 |", "| arp |",
  "| p10 |", "| p20 |"); `notes/review_results/partB/whitened_spectrum_tables.md`, lines 10–14. In the table at
  8bd189e the rows of 34 and of 0.1 of Results 7 (its lines 989 and 990) carried the mark.
- Grade: note

### W6-12
- Where: `manuscript/main_text_numbers.csv`, three committed label rows: CSV line 1197 (Discussion, Recommendations,
  the 0 of "sits at q = 0"), note "lag-0: a name"; CSV lines 1278 and 1279 (Methods, The closed form, paragraph 3, the
  1s of "x_{t+1}, y_{t+1}"), note "Results 1, τ = 1, VAR(1), lag-1: names".
- Problem: The notes are about other tokens of their sentences, the kind that VB-21 found in five rows; these three are
  as they were. The notes of the other 259 label rows name their own token.
- Evidence: the rows' contexts: "A null that removes every cross-correlation sits at q = 0, where sts is at its
  maximum"; "stationary 4 × 4 matrix of (x_t, y_t, x_{t+1}, y_{t+1}) is the lag-0/lag-1 structu". All 262 label rows
  were read with the characters around their token.
- Grade: note

### W6-13
- Where: `manuscript/main_text_numbers.csv`, CSV line 583 (Results 2, paragraph 3, 0.83): "line 20; the line holds
  -0.830; anchor: ts_gsr: other twelve omissions, mean cross-half r 0.680-0.830".
- Problem: The "-" of the held string is the hyphen of the range, not a sign; the held value is 0.830.
  `checks/check_numbers_revision.out` lists the row among its eleven sign differences; the other ten are unsigned prints
  of negative values.
- Evidence: `notes/review_2026-09-24/checks/derived_r17.out`, line 20: "ts_gsr: other twelve omissions, mean cross-half
  r 0.680-0.830; ratio 0.949-0.970"; `checks/check_numbers_revision.out`, line 6: "582 | 0.83 | SIGN DIFFERS (check
  wording) | held=-0.830 printed=0.83". A committed row, the same at 8bd189e.
- Grade: note

### W6-14
- Where: `manuscript/main_text_numbers.csv`, head note, the sources of the added rows: "to the committed tables,
  scripts and lines of the record they quote, to the files of the two PubMed searches and to the claim record of the
  source papers".
- Problem: The list, as corrected for VB-25, names neither the supporting information nor a log. 8 added data rows
  cite `manuscript/si/S3_Text.md`, 7 of them lines of prose (line 568 five times, line 384 twice; the eighth, line 156,
  is a table row); 15 added rows cite `manuscript/supplementary.md` (S2, S6, S15 and S18 Tables); 1 cites
  `notes/review_results/partB/residual_source.log`.
- Evidence: the source files of the 447 added rows: CSV lines 671, 1025–1027, 1029, 1030, 1187, 1188 (S3 Text); 599,
  600, 988, 989, 1022–1024, 1162–1169 (supplementary.md); 815 (the log).
- Grade: note

### W6-15
- Where: `numbers_update.out`, line 382: "the sentence keeps that the exposure is almost the same at every TR (S3 Text
  §4)".
- Problem: The sentence's pointer at HEAD is "(S3 Text §4, §10)"; the line gives it as it was at `checked`.
- Evidence: draft line 193: "the exposure is almost the same at every TR (S3 Text §4, §10)"; the label row of that
  "10" (CSV line 1180) is one of the three rows that HEAD adds to the table of `checked`.
- Grade: note

### W6-16
- Where: `manuscript/main_text_numbers.csv`, CSV line 1053 (Results 7, paragraph 1, 18; an added row): "derived: 0.0127
  / 0.0719 = 17.7 %: the size of the AR(20) contrast as a share of the AR(20) level".
- Problem: The derivation takes the share from two printed values and gives 17.7 %; the run's file holds the share
  itself, 17.6 %. The text's 18 % is the same from either.
- Evidence: `notes/review_results/inference_rows_prewhiten_fixed.csv`, line 135 (prewhiten_fixed ar20 MMI sts ts_gsr
  W60, primary): did −0.012672600820255559, pre_dmt 0.07189525330901372, share_of_pre −0.176264777394793.
- Grade: note

### W6-17
- Where: the JSON, entry A01, `why`: "C's m7 ('most of the reports we found': eight of the ten studies state MMI)";
  entry D04, `why`: "m7 ('the ten studies we found' and the search's limits)".
- Problem: The words in quotation marks are not those of the two replacements.
- Evidence: A01's `new`: "underlies most fMRI synergy reports we found"; D04's `new`: "lists the ten empirical studies
  we found". Both reasons were changed after the checks at other places and are otherwise true of their replacements.
- Grade: note

### W6-18
- Where: `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`, VE-8 (line 1111 and after): "The reasons
  recorded with the two replacements say so."
- Problem: (VE-8 is not among the dispositions of this part; the two reasons are.) The reason of the Author summary's
  replacement says that the sentence went for the limit. The reason of the Introduction's replacement says that the
  headings give what the sentence listed, and does not say that it went for length.
- Evidence: the JSON, entry I03, `why` (the same at `checked`): "the sentence on the record's order, which Methods
  states, and the section-by-section roadmap, which the headings give, not repeated"; entry A02, `why`: "For the
  200-word limit the committed first sentence".
- Grade: note

### W6-19
- Where: `audit/dispositions_revision.md`: VB-8, "The counts are those of the build's pass over every number token of
  the text"; VB-20, "and the build asserts the count of each kind"; VT2-14, "The build's check now tests the anchor of
  each of these rows on its line, as it tests the held string".
- Problem: These three statements cannot be verified in the tree: no program that builds the table is in it, and the
  one committed check of the table tests the held string of the data rows and no anchor. What the statements are about
  was checked independently: every anchor and held string is on its line and the counts of the corrections are right;
  the count of the cross-references is W6-1.
- Evidence: at HEAD the programs that name `main_text_numbers.csv` are `notes/review_2026-09-25/checks/check_numbers.py`,
  `notes/review_2026-09-25/checks/check_cells.py` and `notes/review_2026-09-28/revision/b25_fill.py`;
  `check_numbers.py` passes over every row whose category is not data; of a data row it tests the source file, the
  line number, the held string (`if held not in line`) and the value, and it reads the anchor without testing it.
- Grade: note

### W6-20
- Where: `manuscript/supplementary.md`, line 1664 (S19 Table, row B24, last cell; replacement U08.4): "S3 Text §6 (its
  residual table, and the paragraph after it for A_other's expectation); S18 Table".
- Problem: (Outside this part; seen while reading the reason of U08.4, which is true.) A_other's expectation is not in
  the paragraph after the residual table. The table is followed by a sentence on the caption's −0.74, a subheading and
  a paragraph on the constructions; the expectation is in the paragraph after that one. The residual table's own last
  column holds it too.
- Evidence: `manuscript/si/S3_Text.md`: the table at lines 323–335 (line 327, last cell: "+0.00001 ± 0.00031"); line
  337; the subheading at line 339; line 341; line 343: "against +0.0000 ± 0.0003 under a pure autocorrelation change on
  the band-passed generator".
- Grade: note

## Checked and found exact

**1. The replacements reproduce HEAD.** In a copy of 8bd189e the JSON of HEAD was applied with
`notes/review_2026-09-25/revision/apply_replacements.py`: 277 entries, each `old` found exactly `count` times at its
turn (count 1 but for U06b.3, 2, and U09, 4), 277 distinct ids. 15 files written; 14 are byte-identical with HEAD's;
`manuscript/analysis_record.md` differs in its five new headings alone (lines 8875, 8975, 9042, 9089, 9147: «ENTRY_TIME»
against "2 Oct 2026 22:15 UTC"). The script's output is byte-identical with `checks/apply_revision.out`. The 15 are
all the files that existed at 8bd189e and differ at HEAD; the other 31 changed paths are new files.

**2. The numbers table at HEAD** (code written for this check). 1,381 rows: 787 data, 266 design, 262 label, 54
derived, 7 literature, 5 bound. Every context occurs exactly once in the block that its section and paragraph name,
with the row's number at the place the context centres on; every row maps to its own token; rows and occurrences are
in reading order. Tokens without a row: 95 citation years, 13 day numbers and 11 years of dates, the 10 numbers of the
captions' heads, the DOI, 9 tokens in headings, and the cross-references of W6-1; digits of commit identifiers, of
code spans and of names such as S3 are not tokens; exactly 5 label rows sit on excepted tokens (CSV lines 39–42 and
1235). All 1,065 line locators: the anchor is on the named line (prefixes removed) and, for the 792 data and bound
rows, the held string too; label rows have no source and derived rows a derivation. Values: all 787 data rows equal
their held value at the printed precision, half away from zero (450 with the sign as held, 305 unsigned prints of
non-negative values, 10 unsigned prints of negative values whose direction or size the wording gives, the row of
W6-13, Table 4's five shares as percentages, 15 held strings such as "14/14" or "11 records" that contain the number,
1 in scientific notation). The two ties are right against unrounded values: 0.108 from 0.1075, which is 1762/16384 =
0.10754 (the exact sign-flip p recomputed from the 14 per-subject residual DiDs of
`notes/review_results/partB/baseline_gap.csv` less 0.0027; the other two expectations give 3576 and 4108 of 16,384,
0.218 and 0.251); 0.263 from +0.2625, which is 0.262547 (`notes/review_results/inference_rows_prewhiten.csv`, line
21). The 5 bounds hold. All 54
derivations recompute; the "−0.2748 at full precision" of CSV line 1001 was recomputed from the two committed pickle
files (−0.27479).

**3. The delta of the table.** `checked` to HEAD by (section, paragraph, number, occurrence): no row lost; 3 rows
added (label rows of "§6" in Results 4, paragraph 2, and of "§10" in the Discussion, The fall of r₁ and The
literature); 51 rows changed in category, source, locator or note, 37 committed and 14 added; 16 changed in context
alone. Each changed locator and note was read against its source line: `family_atoms_tables.md` line 4 (the window
sets and the 14 subjects) and line 16 (xty, "+0.0000 (4)"; rty and xtr print "-0.0000 (10)" at lines 12 and 14); the
record's lines 48 and 1747; `prewhiten_tables.md` line 4; `partB21_inference_revision.py` line 82 (`N_BOOT = 10000`);
`inference_revision_tables.md` line 284 (366) with the script's exclusion of the draws whose ceiling is not positive;
`diagnostic_alternatives_tables.md` line 209 (6.7e-16); `S3_Text.md` lines 568 and 384; the claim record's lines 53
and 64; `psychedelic_phiid_search.md` line 79; the two notes "(the residual table of S3 Text §6)"; the rsHRF note; the
five label notes. 8bd189e to HEAD: 934 rows carried, of which 87 changed = 17 moved (11 in the figure script, 5 in
supplementary.md with 4 held strings and 5 anchors, 1 in the literature file) + 13 anchors + 19 rows of N = 14 + 1
held string + 37 (13 + 5 + 9 + 1 + 5 + 1 + 1 + 2), the reworded note being one of the 17. 34 rows cite the record's
line 48 (19 + 1 + 14).

**4. numbers_update.out.** 1,198 and 1,381 rows; 264 deleted, by class 161 / 64 / 7 / 28 / 4, the listed rows equal
as a multiset to the rows not carried, each present in the table of 8bd189e; the former Table 3 is 49 caption and 112
body rows, its body verbatim at S3 Text lines 323–335 and its caption verbatim in line 321 after the new head; every
one of the 64 "taken out" places was opened (with W6-7 and W6-9); the 7 "no longer stated" and the 4 "re-created" are
as the list says (with W6-8 and W6-15); the 28 label entries are label rows. 447 added: 277 / 62 / 3 / 19 / 86. 4
numbers changed in place. 281 contexts recomputed; 0 rows relabelled. 24 fallbacks (20 "only token", 4 "neighbouring
text"): each quotation is in the committed and in the revised text, each criterion holds, and category, source,
locator and note are the same before and after. The 9 heading tokens, the 17 locators by file and the corrected
locators are as stated.

**5. The whys.** 38 entries differ in `why` between `checked` and HEAD and 34 entries are new; I03 and S319 are
unchanged (S319 already gave pp. 14–15). Each changed or new `why` was read against its `old` and `new` and the places
it names: the reads (A's m3, m10, m14; B's MINOR 8, W4; C's m7, w3, M4), the citations audit (C27, C28, C32),
`derived_r24.out` (items 2, 5, 6, 9, 10), S3 Text §4–§6, §8, §10 and §11, S5 Text §1, §4 and §5, S2, S6, S13, S15, S18
and S19 Tables, the reference list. In particular: A01 (0.006–0.009 and 0.0155; [0.258078, 0.894889]), A02 (subjects
5 and 14; the merged first sentence), R102 (S18 Table (a), row (a3), +0.00912; the residual table), R205, R301 (0.0110 /
0.0202 = 0.54), R401, R403, T01, D01, D04, D05, M06 (each quantity it names is marked in the main text as it says),
M07, REF-Schartner (two references, consecutive in the list), S318c (four of the seven authors, Mediano among them;
Liardi not one of them), U17.5 and LT07.5 (C's M4, its last sentence), DCA01 (what the last paragraph of S5 Text §4
holds; with W6-2). The five reasons that say "no statement removed" (I02, R105, R106, R601, M03) hold. Not checked:
what the reasons say the PDFs of cited works print (pages and names in U19.1–5, U20.1–2, U21, U22, LT10.1–5, LT11.1–2,
U17.5, LT07.5), the PDFs not being part of this task.

**6. The bookkeeping files.** `CLAUDE.md`: 1,381 rows (twice); the then Table 3 is the residual table of S3 Text §6;
the captions' order; the statement on the intervals against Results 3, the Discussion, S6 Table's note and Methods;
the figures' conditions against `checks/figures_check.py` (header; the five changed captions; all six equal to the
main text's without their Source sentence; Fig 2's the committed one; Figs 1, 3 and 5 redrawn within 3 %; Figs 2, 4
and 6 by the two date fields, the cross-reference table and the `startxref` offset); the audit folder; S5 Text §4 on
the final run's outputs; 8,498 words. `README.md`: the then Table 3; two PubMed searches. The review folder's README:
all 53 tracked files of the folder are named; every file it names exists but `figures.out`, which it says comes with
the figures commit; all 277 entries have a `why`; `derived_r24.py` reads committed vectors, CSVs, arrays, two tables
files and a log; the ten check reports carry `$SP` and no absolute path.

**7. The dispositions** VB-1 to VB-33, VM-10, VT1-5, VT2-14, VR-2, VR-5, VR-8, VR-9, VE-2, VE-3, VE-4, VE-6, VE-13:
every quotation given after a verdict is at the place named at HEAD, word for word (VE-6's with its marked omission);
each correction answers its finding; the counts they give (37 = 28 + 5 + 1 + 1 + 2; 5, 1 and 11; 7 = 4 + 1 + 1 + 1; 29
heading lines) are right; VB-33's reason holds (no replacement touches the drawing code of Figs 2, 4 and 6). With
W6-1, W6-10, W6-12 and W6-19.

**8. The check outputs reproduce.** From a copy of HEAD: `check_numbers.py` ("rows 1381, data rows 787, flagged 11"),
`check_cells.py` ("flagged 0"), `tablecheck.py` on the seven manuscript files ("rows with a wrong cell count: 0"),
`wc.py` ("total with headings 8498 without 8371"), `abstract_summary.py` ("abstract 300 words (limit 300); author
summary 200 words (limit 200)") and the parse check of the four scripts give outputs byte-identical with the
`*_revision.out` files; `derived_r24.py` reproduces `derived_r24.out` but for the commit in its first line.
