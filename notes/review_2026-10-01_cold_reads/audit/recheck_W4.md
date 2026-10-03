# W4 — the record's five new entries

Scope: lines 8875–9500 of `manuscript/analysis_record.md` at HEAD (eed9271) — "B27, outcome", "B28, outcome", "B29,
outcome", "B16c, outcome", "The revision of 1–2 October 2026: the cold reads applied"; the dispositions VO-1 to VO-13
and VE-1 to VE-25; the record's rules.

Result: 14 findings — 1 error, 5 inexact, 8 notes. No value of a result in the five entries was found wrong. The
error is a count in `checks/numbers_update.out`; the inexact ones are statements of the record, of the dispositions
and of the numbers table's head note about other files.

Paths are relative to VT; line numbers are those of HEAD. "The record" is `manuscript/analysis_record.md`; "the list"
is `notes/review_2026-10-01_cold_reads/checks/numbers_update.out`; "the dispositions file" is
`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`; "the main text" is `manuscript/draft_v2.md`.
Nothing under VT was changed (`git status --short` is empty at the end); scripts that write were run on exports under
VW/W4/.

## Findings

### W4-1 — error

- **Where:** the list, lines 13–14: "64 cross-references by number in the running text and the captions (Results, Fig,
  Table, Eq., Example, Definition, pages)". The record's paragraph "The checks" (lines 9459–9461, 9469) rests on this
  file and on the head note for the tokens that have no row, and three dispositions refer to its counts: VE-4
  (dispositions file, line 1092: "`numbers_update.out` counts each kind"), VR-9 (lines 1223–1225) and VB-8 (line
  1645: "The counts are those of the build's pass over every number token of the text").
- **Problem:** the cross-references by number that have no row are 74, not 64. With 64 the kinds of the sentence add
  to 194, and the number tokens of the covered text without a row are 204 (apart from the 9 tokens of the headings,
  the digits of commit identifiers and the numbers in the names S1–S20 of the supporting items, on which see W4-14).
  The other counts of the sentence are right.
- **Evidence:** own tokenisation of the main text (title; Abstract to the end of Data and code availability; the list
  of supporting information; code spans and URLs blanked), with each of the 1,381 rows of
  `manuscript/main_text_numbers.csv` placed on its token by its `context` column (all 1,381 placed, none off a
  token). Without a row: 95 citation years, 13 day numbers and 11 years of dates, the 10 numbers of the caption
  heads, the DOI and the 9 heading tokens — each as the list says — and 74 cross-references: Results 29, Table 17,
  Fig/Fig./Figure 17, Eq./Eqs. 7, Definition 3, Example 1 (four more tokens after "Eqs.", 79, 82, 4 and 6, carry label
  rows). The same count on `checked` gives 73 (Results 28), which is the number the list gave at `checked` and the
  number VB-8 counted (`audit/check_VB.md`, VB-8: "73 cross-references in running text (Results 28, Table 17,
  Fig/Fig./Figure 17, Eq./Eqs. 7, Definition 3, Example 1)", beside "the 10 numbers of the caption heads"); since
  `checked` the main text gained one ("(Results 4; S13 Table)", line 108; the four of Methods' "Results 2, 3, 5 and
  7", line 241, replace four). 64 is 74 less 10, the number of the caption heads, which the sentence counts apart.
  No page number is among the tokens of the covered text (the kind "pages" has no member there).
- **Grade:** error

### W4-2 — inexact

- **Where:** the record, "The length and the tables", lines 9407–9409: "Where a moved number stands at its new place
  with more decimals (the prewhitened values in Table 4; Cliff et al.'s 42 %, which is 41.8 % in S3 Text §8, as their
  text gives it), the list says so." The disposition of VE-13 repeats it (dispositions file, line 1137: "The entry
  says that the list marks a number that stands at its new place with more decimals.").
- **Problem:** for two of the 64 moved numbers the list names places where the number stands with more decimals and
  does not say so: −0.0944 and 0.0154 (Results 2, paragraph 3). For two more, −1.13 and −0.37, it names two places,
  at one of which the number has more decimals, without saying so. For every other moved number that stands at its
  named place in another form the list does give the form (0.003, 0.005, nine of the prewhitened values in Table 4,
  42).
- **Evidence:** the list, line 332: "−0.0944 | taken out of the paragraph | Fig 3's caption (a) and S13 Table's note
  (the band-passed generator's sts change; the Abstract and the Discussion give it as −0.094)"; line 333: "0.0154 |
  taken out of the paragraph | Fig 3's caption (a) and S13 Table's note (the generator's fall of pair r₁)". At the
  two places the values are −0.09441 and −0.01540: main text, line 110 ("(−0.09441 / −0.01540; the second
  computation of the pure-autocorrelation expectations, S18 Table)"); `manuscript/supplementary.md`, line 363 ("(B24:
  −0.09441 for −0.01540)"). The list, lines 377–378: "−1.13 | taken out of the paragraph | Table 3 and Results 4 (the
  slope's t interval)" and "−0.37 | … | Table 3 and Results 4": Table 3's data row (main text, line 130) has "−1.133
  to −0.373"; Results 4 (line 124) has "[−1.13, −0.37]". All 64 entries were compared with their named places.
- **Grade:** inexact

### W4-3 — inexact

- **Where:** the record, list A, w1, lines 9243–9244: "S3 Text §9 has it once more in its own voice, in committed text,
  of the scale of sts and not of the change in r₁ ("not an artefact of scale")". The same in the disposition of VT2-6
  (dispositions file, lines 1333–1334: "The sentence of S3 Text §9 is committed text and uses the word of the scale of
  sts, not of the change in r₁; it is kept."), to which VE-14 points ("As VT2-6").
- **Problem:** in S3 Text §9 the scale is that of the series' variance, not of sts, and the sentence is about a part of
  the change in r₁: it says that residualising on the variance ratio would remove that part, which is not an artefact
  of scale.
- **Evidence:** `manuscript/si/S3_Text.md`, line 550: "No contrast is residualised on the ratio: for the windowed
  estimator that would remove the part of the r₁ change that coincides with the variance change, not an artefact of
  scale." "The ratio" is, earlier in the same paragraph, "the ratio of window variance to run variance"; the
  paragraph says of the windowed series that "each window is standardised and fitted on its own samples, so its
  variance level cannot enter its atoms".
- **Grade:** inexact

### W4-4 — inexact

- **Where:** the disposition of VO-6, dispositions file, lines 1035–1037: "from `baseline_gap.csv`, which
  `derived_r24.py` now recomputes and compares with the pre-run entry's values (item 12 of its output; S19 Table's
  Part B has the row)".
- **Problem:** item 12 of the script recomputes the values and prints them; the script holds no expected value for
  them and compares nothing. (The record's own sentence, lines 8904–8906, says only that these values are reproduced
  "from `baseline_gap.csv` (`notes/review_2026-10-01_cold_reads/checks/derived_r24.out`, item 12)", which is exact.)
- **Evidence:** `notes/review_2026-10-01_cold_reads/checks/derived_r24.py`, lines 303–321: a header print, the helper
  `col` (its one assert, line 311, is on the 14 subjects' rows) and one print of the values; no assert or comparison
  on a value, where item 11 (lines 244–289) does compare ("each cell compared as printed"). `derived_r24.out`, lines
  78–79, prints r² 0.79, the SDs 0.0887 and 0.0485, subject 14's +0.0949, −0.1121 and −0.0172, subject 8's −0.2795 and
  +0.0914 and the intercept +0.0005; read against the pre-run entry's item (i) (record, lines 8604–8629), they agree.
- **Grade:** inexact

### W4-5 — inexact

- **Where:** the record, list C, M1, lines 9302–9303: "the Ethics statement replaced by a standard statement
  (derivatives released by the data authors, with no demographic, image or identifying field; no new data; no
  participant contacted)". (Not changed since `checked`; found in the reading of the entry in full.)
- **Problem:** the Ethics statement says "no demographic, image or identifying field" of the quantities the analysis
  uses, not of the released derivatives; of the release, S1 Text says that its ratings table carries subject codes,
  and whether those identify anyone is an item of the note to C.T. and S.P.S. in the same entry (lines 9494–9495).
- **Evidence:** main text, line 209: "This is a secondary analysis of derivatives released by the data authors
  (Singleton et al., 2025); the quantities it uses carry no demographic, image or identifying field, no new data were
  collected and no participant was contacted (S1 Text)."; `manuscript/si/S1_Text.md`, line 5: "the released ratings
  table carries subject codes, which this analysis does not use and which the repository's tracked files do not
  contain"; `manuscript/si/S4_Text.md`, line 78 (Sh5): "whose analysed quantities carry no demographic, image or
  identifying field".
- **Grade:** inexact

### W4-6 — inexact

- **Where:** `manuscript/main_text_numbers.csv`, head note (line 1), of the 7 deleted rows "of numbers the rewritten
  sentences no longer state": "(a threshold replaced by the p values themselves, a repeated limit, a second mention, a
  count, a clause that is not carried)".
- **Problem:** the five kinds cover six of the seven rows. The seventh, Results 3's 0.0001 (the spin p, now written p <
  1/10,000), is of none of them. The record's sentence (lines 9404–9406) and the list have it; the head note does not.
- **Evidence:** the list's seven rows of the class "no longer stated": lines 314 (the second mention of 4), 325 (the
  count of 14 refits), 335 ("0.0001 | no longer stated | the spin p is now written 'p < 1/10,000'"), 351 (the repeated
  limit 0.0112), 352 and 357 (the threshold 0.05, twice), 382 (the clause with "TR 2 s"). The record lists six kinds,
  the sixth "the spin p rewritten as p < 1/10,000".
- **Grade:** inexact

### W4-7 — note

- **Where:** the disposition of VO-2, dispositions file, lines 1012–1014: "The three places say that the contrast of
  the sum is in `inference_rows_prewhiten_fixed.csv` and, with its inverted interval, in `derived_r24.out`, item 1".
- **Problem:** one of the three places has the clause "with its inverted interval"; the other two say only that the
  contrast is in the two files.
- **Evidence:** the record, lines 9129–9131 (with the clause); `manuscript/si/S3_Text.md`, line 544: "the contrast of
  their sum is in `inference_rows_prewhiten_fixed.csv` and in `derived_r24.out`, item 1"; `manuscript/supplementary.md`,
  line 1687 (S19 Table, row B16c (e)): the same words as S3 Text. (`derived_r24.out`, item 1, does print the interval,
  and the two values the entry quotes are those of its lines for xtx+yty at ar10 and ar20, ts_gsr, W60.)
- **Grade:** note

### W4-8 — note

- **Where:** the record, "B28, outcome", item (iii), lines 9034–9035: "The subject at the floor is named where the
  band-passed conditions are reported (Table 3's caption; S3 Text §6; the source line of S18 Table's part on B28)."
- **Problem:** the three places do name subject 8. Two more places report values of the band-passed conditions and
  do not name the subject: Fig 3's caption (c), which points to Table 3's caption for the floor, and S19 Table's rows
  B28 (a) to (d), which mention neither the floor nor the subject. (VO-10 raised the same of S18 Table.)
- **Evidence:** main text, line 110 (Fig 3's caption): "rescaled and floored as Table 3's caption says and applied as
  a step at sample 300, the start of window 6 (band-passed −0.200, AR(1) −0.355, means over replicates"; no subject
  is named in the caption's part (c). `manuscript/supplementary.md`, lines 1675–1678 (e.g. "band-passed step: slope
  −0.200 against ratio −0.167"; "band-passed +0.0022 (step) against +0.0020 (ramp)").
- **Grade:** note

### W4-9 — note

- **Where:** the record, list B, MINOR 8, lines 9286–9287: "named as a recorded prediction: the sensory–association
  contrast and the residual map's network structure, whose p lies below the predicted range (Results 3 and Fig 4's
  caption)".
- **Problem:** of the residual map's network structure the two places speak of a prediction ("below the range
  predicted for it"). Of the sensory–association contrast they say that it was fixed beforehand and do not call it a
  prediction; the prediction recorded for it is in S19 Table, to which Results 3 points. (The same entry's disposition
  of B's W3, lines 9296–9297, describes the clause as "the contrast fixed before the partialled map was computed".)
- **Evidence:** main text, line 114: "fixed in the record before the partialled map was computed (S19 Table)"; line
  116 (Fig 4's caption): "fixed before the partialled map was computed (Results 3)"; `manuscript/supplementary.md`,
  line 1639 (S19 Table, B20): "The residual map's sensory–association contrast is reduced; its sign not predicted".
- **Grade:** note

### W4-10 — note

- **Where:** the record, list A, m8, lines 9220–9221: ""scope map" stays as the plans' name (S5 Text §1) and in file
  names (README.md, CLAUDE.md and the figure script's comments follow)".
- **Problem:** the name also stands as the plans' name in S3 Text §4, a place the sentence does not give (it gives S3
  Text §4 only as the place where "the map" is defined).
- **Evidence:** `manuscript/si/S3_Text.md`, line 128: "the plans called it the scope map, a name the file names keep";
  `manuscript/si/S5_Text.md`, line 7 (§1): "in the plans' own names, scope map, CCS, lag dependence, diagnostic and
  literature table". A search of the main text, S1–S5 Text and `supplementary.md` for "scope map" finds these two and
  file names only.
- **Grade:** note

### W4-11 — note

- **Where:** the record, the revision's entry, first paragraph, lines 9152–9154: "`checks/` the outputs of the checks
  (apply, check_numbers, check_cells, tablecheck, wc, the abstract and summary word counts, `derived_r24.py` with its
  output, the numbers table's update)".
- **Problem:** the commit adds two more files to `checks/` that the parenthesis does not name: the parse check of the
  scripts (`scripts_check_revision.out`), which the entry names nowhere, and `figures_check.py`, which it names in its
  paragraph "The figures".
- **Evidence:** `git diff --stat 8bd189e HEAD -- notes/review_2026-10-01_cold_reads/checks`: twelve files added, among
  them `scripts_check_revision.out` (4 lines: "parses: scripts/15_figures_v2.py" and three more) and
  `figures_check.py`; `notes/review_2026-10-01_cold_reads/README.md`, lines 67–70, lists both.
- **Grade:** note

### W4-12 — note

- **Where:** the record, "The revision.", lines 9177–9179: "each claim checked against the PDF (`claims/`), with Barrett
  (2015), Liardi et al. (2025), Luppi et al. (2022, 2024) and Cliff et al. (2021) cited for statements newly made from
  them".
- **Problem:** the claim record at HEAD, revised after the checks, holds sections on three works that the sentence
  does not name: Luppi et al. (2023), Luppi et al. (2026) and Murray et al. (2014). For one of them the revision adds
  statements made from the work: S20 Table's row 5 (Luppi et al., 2026).
- **Evidence:** `notes/review_2026-10-01_cold_reads/claims/claims_2026-10-01.md`, lines 9–12 ("and again after the
  checks of the corrections, which added the items on the exclusion criteria, on the Reporting Summary of Luppi et
  al. (2026), on Luppi et al. (2023) and on Murray et al. (2014)") and its sections at lines 150, 159 and 171.
  `manuscript/supplementary.md`, line 1721, has "(sevoflurane, propofol or ketamine; p. 3; p. 35)" and "not mentioned
  in the article, its Extended Data or its Reporting Summary", neither of which is in the row at 8bd189e. The claim
  record's item on Murray et al. (2014) says that its wording in Results 3 is a restored one, and S3 Text §11's
  statements about Luppi et al. (2023) are committed text.
- **Grade:** note

### W4-13 — note

- **Where:** the record, the revision's entry, first paragraph, lines 9159–9160: "`derived_r24.py` reads committed files
  only: per-subject vectors, arrays, CSV files, two tables files and a log" (quoted by the disposition of VE-23).
- **Problem:** the script reads one array file.
- **Evidence:** `derived_r24.py`: two pickles (lines 45, 149), six CSV files (lines 64, 79, 102, 116, 140, 172), two
  tables files (lines 94, 268), one log (line 224) and one array, line 168: `np.load(RR / "regional" /
  "regional_atoms_raw_ts_gsr_win60.npy")`. (S19 Table's Part B, `supplementary.md` line 1706, also has "arrays".)
- **Grade:** note

### W4-14 — note

- **Where:** the record, "The checks", lines 9459–9461, of the table's rows, one on "every number token of the main
  text apart from the kinds its head note names (citation years, cross-references by number, the numbers of the
  captions' own heads and of the headings, dates, commit identifiers, the Zenodo DOI, code spans)".
- **Problem:** the numbers in the names of the supporting items (S1 Text to S5 Text, S1 Table to S20 Table) have no
  row, and neither the head note nor the list names them among the kinds without a row or says that they are not
  tokens. The statement is exact only if they are not counted as number tokens.
- **Evidence:** the tokenisation of W4-1: 149 such numbers in the covered text (e.g. "S3 Text", "S11 Table", "S1–S7
  Tables"), none with a row. The head note's kinds are those the record lists; the list, lines 15–16, says of what is
  not a token only: "The digits of commit identifiers and the numbers inside code spans are not tokens of the text".
- **Grade:** note

## Checked and found exact

**The record's rules (task 3).** The file at 8bd189e (814,068 bytes) is a byte prefix of the file at HEAD (881,437
bytes); 627 lines are added. No line of the five entries exceeds 120 characters, headings apart (69 lines of exactly
120; no tab, no trailing space). The five headings have the form "## <title>, <time> UTC (appended; nothing above
edited)".

**The delta `checked` → HEAD (task 1).** The five entries were extracted from both commits, their paragraphs joined
and compared word by word: 22 of 42 paragraphs changed, in 151 spans, 5 of them the headings' time. Every span was
read against its source. Exact, apart from the findings above:

- *B27, "The run".* `b27/b27_unit.log`: start 23:37:10 EEST, steps at 23:37:10, 23:37:18, 00:01:07 and 00:01:08, done
  in 7, 1,428, 1 and 2,040 s, "=== unit exit 0"; 00:01:08 + 2,040 s = 00:35:08; 20:37:10 to 21:35:08 UTC is 3,478 s.
  `b27/b27_heartbeat.log`: 11 lines; line 3 (23:52:10) connected; lines 4 (23:57:10) to 11 (00:32:10) disconnected, 8
  lines; battery 99 % to 83 %; 00:32:10 to 00:35:08 is 178 s; the largest gap between lines 300 s. `b27_start.sh`: the
  lock (sleep, idle, lid switch, shutdown) and the charger requirement. `outputs.sha256`: 29 files, all verified;
  exactly the twelve text outputs carry `git=13e7299`; the versions against `requirements.lock.txt`; the data clone at
  77af7aa; `b27_commit.sh`'s checks; 8bd189e adds the 29 outputs and the four evidence files.
- *B27, "The outputs".* Every value of the pre-run entry's item (i) (record, lines 8604–8629): those the tables file
  prints are in tables (a), (b) and (c) of `baseline_gap_tables.md`; those it does not print (r² 0.79; SDs 0.0887,
  0.0485; subject 14: +0.0949, −0.1121, −0.0172; subject 8: −0.2795, +0.0914; intercept +0.0005) are in
  `derived_r24.out`, item 12, and were recomputed here from `baseline_gap.csv` (168 rows); −0.788 is in
  `matched_slope_tables.md`, line 6.
- *B27, the script's closing paragraph and item 3.* The two quoted phrases are in the tables file's last paragraph
  (line 48); item 3 of `audit/dispositions.md` and `audit/findings.md` is as the entry says.
- *B27, "What the text says".* The quotations are word for word: "a pre-injection baseline gap in the direction that
  creates it" (S2 Text, line 9); "lies in the direction that enlarges the DiD" (Results 2); "a test detecting 0.0155
  does not resolve this" (Abstract); "not distinguished" in Results 4 and the Discussion. S3 Text §5 carries table (a)
  (12 × 13 cells) and table (b) (3 × 10 cells) cell for cell and (c) in prose with every value.
- *B28.* The three inputs (script lines 77, 98–99; `inference_rows_raw.pkl`, `inference_rows_diag.pkl`,
  `scope_map_overlay_points.npz` with key `pre_w1to4_q` and 52,440 values); Table 3's rows on the leave-one-out and
  leave-two-out count the intervals that contain each rate; the committed figure script already drew the three rates
  on Fig 3c; S18 Table's source line names subject 8; "its source is unidentified" (Abstract) and "not identified"
  (Results 4, Discussion); S18 Table has eleven of the fourteen columns, without the three kinds the entry names.
- *B16c (e).* `prewhiten_fixed_tables.md` prints xtx and yty as two rows and no contrast of their sum; the two values
  of the sum's contrast (−0.0229 [−0.0409, −0.0053], p = 0.0077; −0.0060 [−0.0098, −0.0022], p = 0.0037) are in
  `derived_r24.out`, item 1, and were recomputed here by inverting the sign-flip test on the pickle's per-subject
  vectors; the diagnostic's levels are means over both runs and all windows (script line 184) and the cells' levels
  DMT pre-injection means (line 166).
- *The revision's entry, first paragraph and "The revision."* The folders hold what is said (W4-11 apart);
  `derived_r24.py` reads committed files only (W4-13 apart) and its output is reproduced on a scratch copy, header
  apart; supplementary tables changed between 8bd189e and HEAD: the head note, S5, S11, S12, S13, S18, S19, S20 and no
  other; S1, S3, S4 and S5 Text changed, S2 Text not; seven references added (41 to 48, none removed or changed, each
  cited); the two PubMed searches' files and the web-search file say what the entry says of them.
- *Lists A, B, C.* 70 dispositions (A 20, B 19, C 31), each read against its finding in `reviews/read_A.md`,
  `read_B.md`, `read_C.md` and against the text. The changed statements: A m4 (Cliff et al.'s condition and numbers
  under C's m14, S3 Text §8: pages 15–16, 41.8 %, over 88 %); A m8 (the two forms of the main text's name for the
  surface are at the three places named; W4-10 apart); A w1 (W4-3 apart: five occurrences of "artefact" in the
  manuscript files, as described); B MINOR 8 (each quantity listed as marked post hoc is so marked in the section
  named: Results 2 three times, Results 3, 5, 7; the EEG check in the Discussion as "a prediction recorded before it
  was computed"; Methods' sentence "(the text repeats it for several, in Results 2, 3, 5 and 7 and the Discussion)";
  W4-9 apart); B MINOR 9 (4.263: 4.139 to 4.535, `derived_r24.out` item 8 and S3 Text §5; Table 3 has the residual's
  leave-one-out); B W1 (p < 1/10,000 in Results 3, S3 Text §4, S5 Table's note and S19 Table's row); B W4 (both
  bracketed values gone from Results 4; S3 Text §6 gives both with the values before the exclusion); C M1 (the record's
  entries "Data-governance note" and "Git history and the participant codes": six tracked files, fa39ef2; W4-5
  apart); C M2 (the Use of AI tools statement's sentences); C M4 (S20 Table's row 5 says so); C M5 (a) (the
  Introduction's and S20 Table's forms; the seven observations removed from S20 Table and the literature file); C m4
  (README.md's licence paragraph: the emails of 13 and 14 September 2026); C m13 (the line stays; CLAUDE.md lists it);
  C w4 ("per within-window standard deviation" in the Abstract, "within a window" in Results 1). The unchanged
  statements with a number or a quotation were searched in the text and found as given (among them −1.74, 0.035,
  +0.009 for c = +0.02, −0.015 to −0.036 against S18 Table's grid, r = 0.80 and 0.09, p = 0.0002, 0.898, 2.30, 2.645,
  0.0051, 0.0155, 0.006–0.009, 366 of 10,000, 0.0564 and 0.0009, a fifth and a sixth, 0.50 and 3.09, ρ = −0.98, "most
  fMRI synergy reports we found", "the ten empirical studies we found", "in the texts we read", "lowers sts",
  "excludes zero exactly when p ≤ 0.05", "the fall is not an artefact", "the r₁-dependence included"; Fig 5c's
  quarter scale: 0.05 nats on a height of 0.20 against 0.30 on 0.30 and 0.20 on 0.20).
- *"The length and the tables".* The decision of 23 September 2026 is in the record (lines 6571–6578). Of the
  sections from the Introduction to Methods only "Redundancy functions" and "Regional maps" are word for word the
  committed ones. Each moved statement is at the place named and pointed to from the main text; the former Table 3's
  caption and body are verbatim in S3 Text §6. The five retired sentences and phrases were in the main text at 8bd189e
  (1, 1, 1, 3 and 1 occurrences) and are gone; the Introduction's sentence listing the Results sections is gone and
  the Author summary's first sentence is merged into its second. The list's deleted rows: 264 = 161 + 64 + 7 + 28 + 4;
  each of the 64 moved numbers is at its named place (W4-2 apart); the 7 rows are of the six kinds the record lists.
  `wc.py`: 8,498 with headings, 8,371 without; four tables and six figures.
- *"The audits of the prepared revision".* Headings counted: `findings_text.md` 63 (3 blocking, 18 to fix, 31 minor,
  11 notes); `findings_record.md` 57 (1, 12, 30, 14); `findings_citations.md` 32 (2, 5, 17, 8), its C01–C25 identical
  to the first form's 25 at `checked`, whose list of what was not checked for want of the PDF names eight works. The
  dispositions file: 152 findings, 147 "Corrected", 2 "Stated, not changed" (R46, T25: the form of one output file; a
  ratio of printed means) and 3 on the audits' instructions (R44, R45, T53). The ten check reports: 157 findings,
  counted in the reports: 11 errors (VO 0, VE 1, VR 2, VT1 1, VT2 1, VB 6, the others 0), 69 inexact, 77 notes; the
  eleven errors read: VE-1, VT1-1, VT2-4 and VR-1 are the one number (4.54 for 4.535); VR-2 (the notes of two rows),
  VB-3 (the source of one row), VB-1 and VB-2 (the places of two sets of moved numbers), VB-4, VB-5 and VB-6 (the
  reasons recorded with four replacements: A01, R102, U17.5, LT07.5): seven findings on the bookkeeping. No finding
  reports a wrong value of a result in the main text or the supporting information. The last part of the
  dispositions file: 142 "Corrected", 7 "Stated" (VO-9, VE-14, VR-16, VT2-6, VS-12, VB-22, VB-31), 8 "Kept" (VE-22,
  VE-25, VT2-10, VN-7, VN-8, VN-10, VM-9, VB-33). The text audit's T07, T10 and T25 are the three that rest on the
  released series (`findings_text.md`, lines 20–21).
- *"The checks".* The 277 replacements were applied to a scratch export of 8bd189e: all "ok", the output identical to
  `checks/apply_revision.out`, the 15 resulting files identical to HEAD's but for the time in the record's five
  headings. `wc.py`, `abstract_summary.py` (300 and 200), `check_numbers.py` (1,381 rows), `check_cells.py` and
  `tablecheck.py` reproduce the committed `*_revision.out` files exactly; 29 heading lines from the Introduction to
  the end of Methods (8,498 = 8,371 + 127 heading words). The numbers table at 8bd189e against HEAD, compared row by
  row: 1,198 − 264 + 447 = 1,381; added 277 data (each with file, line and held string), 62 design and 3 literature
  (file, line and anchor), 19 derived (a derivation), 86 label (no source); 13 anchors, 19 committed rows of N = 14
  moved to the record's line 48 with the 14 added ones, 1 held string, 1 note reworded, and 37 further committed rows
  corrected (13 + 5 + 9 + 1 + 5 + 1 + 1 + 2, as the head note lists them); 4 numbers changed in place; 24 rows in the
  list's two fallback lists (20 and 4). Every number token of the covered text has a row apart from the kinds named
  (W4-1 and W4-14 on the counts and the names S1–S20), and 5 label rows sit on tokens of those kinds (79, 82, 4, 6 and
  one year), as the head note says. No computation label stands before "## Supporting information"; no round, stage or
  bundle name and no reviewer's letter stands in the main text, S1–S5 Text or `supplementary.md`; "planning session"
  and "writer's session" occur only in S5 Text, line 33 (§5).
- *"The figures".* `checks/figures_check.py` tests the three conditions as the paragraph states them: the header with
  the short SHA and no "-dirty"; the same number of lines and differences in the header and the captions of Figs 1,
  3, 4, 5 and 6; each of the six captions with a Source sentence and, without it, equal to the main text's; Fig 2's
  the committed one; the PNGs of Figs 1, 3 and 5 different and within 3 % in width and height; those of Figs 2, 4 and
  6 identical or of the same size with at most 0.1 % of pixels different and no channel different by more than 32;
  the PDFs with the two date fields, the cross-reference table and the `startxref` offset masked. `git diff 8bd189e
  HEAD -- scripts/15_figures_v2.py` has exactly the drawing changes the paragraph names (Fig 1b's colour-bar label;
  Fig 3c's two slope lines, legend entries at 6.5 for 6.8, the legend title's size kept at 6.8; Fig 5c's y-range, two-line
  title, height ratios 0.30 : 0.20 : 0.20 for 0.30 : 0.20 : 0.10, the legend's anchor −0.25 for −0.42) and no other;
  0.30/0.70 is six-sevenths of 0.30/0.60, and 0.25 × 0.20/0.70 = 0.071 against 0.42 × 0.10/0.60 = 0.070. The figures
  were regenerated on a scratch copy with matplotlib 3.10.9, not the pinned 3.11.1: the six regenerated captions
  equal the main text's, and the two scripts in that one environment differ in Fig 5 by −1.10 % in width and +0.11 %
  in height (the figures quoted in the disposition of VE-22), with Figs 2, 4 and 6 identical; the size and
  anti-aliasing conditions were not tested in the pinned environment.
- *The note to C.T. and S.P.S.* Eight dispositions of the entry assign an item to the note (A's M2; B's MINOR 7; C's
  M1, M2, M4, m1, m4, m17) and no other does; the five added items are in the list in full and are assigned by none;
  the list is word for word CLAUDE.md's.

**The dispositions VO-1 to VO-13 and VE-1 to VE-25 (task 2).** Each was read against its finding in
`audit/check_VO.md` and `audit/check_VE.md` and against HEAD. The 33 passages they put in quotation marks are word
for word at the places named. Each correction answers its finding, and the reasons of the two kept ones hold (VE-22:
the comparison of the two scripts in one environment reproduced, see above; VE-25: nothing to change). Not exact:
VO-2 (W4-7), VO-6 (W4-4), VE-14 by its pointer to VT2-6 (W4-3), and the last sentence of VE-13 (W4-2); VE-4's "counts
each kind" holds, one of the counts being wrong (W4-1); VE-23 quotes the record's sentence of W4-13. VO-4: in S3 Text
§5 and §6 (lines 231, 264, 395) the date follows the pre-run entry's title alone and the titles are the record's
headings word for word.

**The five entries read in full (task 4).** Every value of the four outcome entries was compared with the result
files: B27 (a)–(d), the sts rows and (c) with `baseline_gap_tables.md` and `derived_r24.out` items 2 and 8; B28's four
conditions (23 values each), (a)–(d) and the generators' parameters with `matched_slope_tables.md`, `matched_slope.csv`
(400 rows, eleven fields under a header of ten) and `derived_r24.out` item 5; B29 (a)–(d) with `censoring_tables.md`
and `censoring.csv` (392 rows); B16c's eight cells, (a)–(e) and the Fisher-z intervals with `prewhiten_fixed_tables.md`,
`prewhiten_tables.md`, `inference_rows_prewhiten_fixed.csv` (264 rows, 44 labels in six sets, 192 + 72) and
`derived_r24.out` items 1 and 6. Their paragraphs "What the text says" were compared with the main text, S1–S5 Text
and S11, S18 and S19 Tables (S3 Text §6 has B28's table in full, 4 × 14; S11 Table's 24 rows of the fixed orders
equal `derived_r24.out`; Table 4's rows at p = 10 and 20 equal the entry's cells; Results 7's −0.0037 is −0.0127 less
the diagnostic's −0.0090). No statement of one entry was found to contradict another entry, the text or the result
files, apart from the findings above.

**Not checkable from the tree.** "The writer's session noted the difference on 1 October 2026 before the run" (B27,
closing paragraph); "about 9,000 words" for the first draft; V.S.'s decision of 2 October 2026 (CLAUDE.md states it
in the same terms; no other source is in the tree); the disposition of VE-20's "The build tests that these two and no
others are unchanged" (the build is not in the tree; the fact itself is as stated, see above); the outcome of
`figures_check.py` in the pinned environment.
