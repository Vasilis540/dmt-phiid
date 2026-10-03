# VR — the dispositions of R01–R57, verified at HEAD (9caa60b on 8bd189e)

VT = $SP/r24/vtree. All paths below are under VT. Nothing under VT was changed (`git status` is empty at the end). Scratch files are in $SP/r24/vwork/VR/.

## Result

Every one of the 57 dispositions names a correction that is in the tree, and every phrase quoted as present text occurs word for word in the file named. Seventeen things are not exact: 2 errors, 9 inexact, 6 notes. No number of the main text is affected.

- **Errors:** a wrong number in the record that R22's correction introduced (VR-1), and a stale table pointer in two notes of the numbers table (VR-2).
- **Dispositions that say something untrue of the tree (task item d):** R19 (VR-10), R22 (VR-11), R48 (VR-4), R56 (VR-5).
- **Problems that persist elsewhere (task item c):** R07 in S4 Text (VR-7), R53 in a numbers-table note (VR-6), R50 in S19 Table and S3 Text (VR-12).

## Findings

**VR-1 — error**
- Where: `manuscript/analysis_record.md`, revision entry, B MINOR 9, line 9264: "that of the sts slope (4.26: 4.14 to 4.54) in S3 Text §5"
- Problem: 4.54 is the three-decimal 4.535 rounded a second time. The largest leave-one-out slope (without subject 8) is 4.5346, which is 4.53 at two decimals. R22's disposition says the disposition of B's MINOR 9 states the leave-one-out; it does, with this value.
- Evidence: own OLS on `notes/review_results/partB/baseline_gap.csv` (sts and r1, ts_gsr, W = 60, column `did`): 4.262661 with all 14; 4.139204 without subject 14; 4.534629 without subject 8 (4.53453 to 4.53473 under the CSV's six-decimal rounding). `checks/derived_r24.out` line 69, `S3_Text.md` line 260 and record lines 8937–8939 print 4.535. "4.54" occurs nowhere else in scope.

**VR-2 — error**
- Where: `manuscript/main_text_numbers.csv`, CSV lines 772 and 773 (Results 4, paragraph 2, rows of 0.012 and 0.015), notes: "the AR(1) generator's window-level pair r₁ change under condition (i), −0.01243 (Table 3), the smallest of the three" and "the band-passed generator's window-level pair r₁ change, −0.01540 (Table 3), the largest of the three; the null's is −0.0146"
- Problem: neither value is in Table 3 of the revised main text. Both are in the residual table of S3 Text §6, the former Table 3. The notes are unchanged from 8bd189e (CSV lines 678–679 there); moving the table made the pointer wrong.
- Evidence: `draft_v2.md` lines 126–139; `S3_Text.md` lines 327–328. No other note points to Table 3 for a value it no longer holds, and no manuscript file has a stale "Table 3".

**VR-3 — inexact**
- Where: `manuscript/si/S3_Text.md` §5, line 231: 'Record, "The pre-injection gap and the per-subject relations (B27): pre-run entry" and "B27, outcome" (1 October 2026);' — the same form at line 264 (B29) and §6, line 393 (B28).
- Problem: only the pre-run entries are of 1 October; the outcome entries are headed 2 Oct 2026. S18 Table's source gives the same pair as "1–2 Oct 2026" and S11 Table's as "pre-run entry and outcome 1–2 Oct 2026".
- Evidence: record headings at lines 8575, 8671, 8757 ("1 Oct 2026 18:50 UTC") and 8875, 8968, 9028 ("2 Oct 2026 18:40 UTC"); `supplementary.md` lines 1590 and 256. Found by R43's search; not in base, not raised by any audit.

**VR-4 — inexact**
- Where: record, "The figures", (1), lines 9408–9411: "which `checks/figures_check.py` tests as stated here" … "Fig 2's caption is the committed one."; `audit/dispositions_revision.md`, R48, line 327: "Fig 2's is the committed one".
- Problem: the script tests one condition more than the paragraph states. For Fig 2 it also requires that the caption hold a Source sentence and, without it, equal the main text's caption. The script's own docstring says so; the record and the disposition do not. Every other condition of (1)–(3) is tested exactly as stated and nothing stated is left untested. The parenthesis in (2) on what is redrawn is description, not a tested condition; it agrees with the figure script's diff from 8bd189e.
- Evidence: `checks/figures_check.py` lines 89–92 (`okc = old[i] == new[i] and b is not None and b == main.get(k)`) and docstring lines 10–11, read line by line against record lines 9407–9419.

**VR-5 — inexact**
- Where: `CLAUDE.md`, "Remaining work", lines 455–456: "the PNG files of Figs 2, 4 and 6 are identical or differ by anti-aliasing alone, and their PDF files are identical once their dates are masked"; dispositions, R56, line 376: "gives the conditions as the record does".
- Problem: the record and the script mask the two date fields, the cross-reference table and the `startxref` offset. CLAUDE.md's PNG condition now agrees with the record (R56's point); its PDF condition is still narrower.
- Evidence: record lines 9416–9418; `figures_check.py` lines 128–132.

**VR-6 — inexact**
- Where: `manuscript/main_text_numbers.csv`, CSV line 565 (Results 2, paragraph 3, the row of 366), note: "B21 (d): draws excluded (either half's reliability not positive)"
- Problem: this is the wording R53 corrected in the text. The reliabilities are those of the two DiDs (sts and r₁), not of the two halves. The row was added by this revision.
- Evidence: `notes/review_results/partB/inference_revision_tables.md` line 284 (columns rel(sts), rel(r₁)); `notes/partB21_inference_revision.py` lines 563–567 and 587–597; `draft_v2.md` line 108 as corrected.

**VR-7 — inexact**
- Where: `manuscript/si/S4_Text.md`, Sh3, line 76: "| Sh3 Analysis code | reported | Data and code availability: https://github.com/Vasilis540/dmt-phiid, pinned environment, every result table with its git SHA, `run_all.sh`. |"
- Problem: R07's unqualified claim persists here (row unchanged from 8bd189e). Data and code availability now gives the exceptions.
- Evidence: `S5_Text.md` §4, line 25 ("apart from five CSV files that carry no header by design"); `notes/review_results/inference_rows_raw.csv` begins with its column names; `results/synergy_bins_20regions_ts_gsr_global.csv` line 1 ends "git=nogit"; `draft_v2.md` line 267.

**VR-8 — inexact**
- Where: record, "The checks", lines 9399–9400: "and 444 added, each with its source and line"; `checks/numbers_update.out` lines 12–13: "received a new row with its source file, line and held string".
- Problem: 103 of the 444 added rows are label rows (84) or derived rows (19), which have no source file and no line.
- Evidence: rows without a source file are 259 at 8bd189e and 305 at HEAD; 57 of the 264 deleted rows had none (28 of the label class, 19 label and 6 derived rows of the former Table 3, 3 derived, 1 label re-created); 305 − (259 − 57) = 103. A per-paragraph comparison of the two tables gives the same 84 + 19.

**VR-9 — inexact**
- Where: `checks/numbers_update.out` lines 13–15: "apart from the kinds the table does not list: 105 citation years, 73 cross-references by number (Results, Fig, Table, Eq., Example, Definition), 12 dates with their month and the Zenodo DOI (1)"; also lines 331 and 298–302.
- Problem: four details of the description; the table itself is right.
  - (a) Of the 105, 95 are citation years and 10 are the years of the dates; the "12 dates" are the dates' twelve day numbers.
  - (b) The ten caption labels ("Fig 1." to "Fig 6.", "Table 1." to "Table 4.") are number tokens without a row and are in none of the four counts; 73 is the count in running text.
  - (c) Line 331 classes the deleted row "Results / 7. Remedies | paragraph 1 | 1" as "still in the paragraph, in a rewritten sentence: the token has a new row with its own source". The deleted row was the 1 of "in 1–5" (a design row), which the paragraph no longer has; its two "1" are the name AR(1), with label rows. The record's "6 of numbers still in their paragraph, whose token has a new row" (line 9399) counts it.
  - (d) Lines 298, 299, 301 and 302 give "S3 Text §5 and Fig 3b" for 0.349, 0.913, 0.174 and 0.876. The two intervals are in S3 Text §5 only; Fig 3b and its caption carry the two correlations. Record line 9345 has the same pairing.
- Evidence: own tokenizer over `draft_v2.md` (tokens without a row: 95 citation years; 22 date tokens = 12 days + 10 years; 83 cross-reference tokens = 73 + 10 caption labels; 1 DOI); CSV line 984 at 8bd189e and CSV lines 1040 and 1056 at HEAD; `S3_Text.md` line 167; `draft_v2.md` line 110; `scripts/15_figures_v2.py` lines 342–349.

**VR-10 — inexact**
- Where: dispositions, R19, lines 147–150: "and in the list of supporting information (the entries of S3 Text and S20 Table)"; "README.md describes Fig 1 as the surface".
- Problem: (i) S3 Text's entry in the list reads "the sts surface over (r₁, q)"; "the sts surface of Fig 1a" is in the Discussion and in S20 Table's entry only. (ii) README.md does not name Fig 1 there. The corrections themselves are in the tree.
- Evidence: `draft_v2.md` lines 191, 397, 441; `README.md` lines 22–23 ("the surface of `sts` over (r₁, q) with real pairs overlaid").

**VR-11 — inexact**
- Where: dispositions, R22, line 170: '"B27, outcome", item (v), and the disposition of B's MINOR 9 say both.'
- Problem: item (v) states the assumptions only. The leave-one-out of the sts slope is in the entry's paragraph "The sts rows and (c), as the run reproduced them".
- Evidence: record lines 8963–8965 (item (v)) and 8937–8939.

**VR-12 — note**
- Where: `manuscript/supplementary.md`, S19 Table, row B29 (d), line 1682: "… and no other | confirmed: (3, placebo, 839); it is the last TR of its run"; `S3_Text.md` §5, line 299: "(d) the non-finite TR is subject 3's placebo run's TR 839 and no other: confirmed."
- Problem: R50's qualification ("confirmed on ts_gsr, the variant the script reads for this check") is in "B29, outcome" (d) and in Methods, not in these two statements of the same verdict. S3 Text §5's item (e), two paragraphs above line 299, does name `ts_gsr`.
- Evidence: `notes/partB29_censoring.py` line 123; `censoring_tables.md` line 47; record lines 9052–9054.

**VR-13 — note**
- Where: `supplementary.md`, S19 Table, sentence after Part A, line 1689: "B28, B29 and B16c recorded none for one of their parts (rows B28 (d), B29 (c) and B16c (e))"
- Problem: read against the four pre-run entries, the sentence is right for the six rows it names. B27's pre-run entry also records a part without a prediction, which the sentence does not attribute to B27; it has no row of its own and stands in the outcome cell of row B27 (d).
- Evidence: record lines 8642–8644 ("No prediction for the residual's correlations with the r₁ gaps."); `supplementary.md` line 1674.

**VR-14 — note**
- Where: `notes/partB5_literature_v2.md` line 1: "with row 10 added on 1 October 2026"; `supplementary.md`, S20 Table's head note, line 1711: "added from its full text on that date" and "as the claim record of 1 October 2026 gives them"; `S3_Text.md` §10, line 552: "added from its full text on that date".
- Problem: no "1 October 2026" still dates a move or a removal of this revision (R43's eight are corrected). These date an addition and a record of the same revision to 1 October. Whether the row was written on 1 October is not in the tree.
- Evidence: row 10 is absent from the literature file at 13e7299 and at 8bd189e and enters with this revision; the record's entry of 1 Oct 18:50 UTC says the two records "are to be assessed from their full texts in the revision that follows the run" (line 8570); the claim record is titled "Claim record of the revision of 1–2 October 2026" and says it was checked "on 1 and 2 October 2026".

**VR-15 — note**
- Where: `S5_Text.md` §4, line 25: "the unit running on battery from then to its end"; record line 8890: "the unit ran on battery to its end".
- Problem: the heartbeat's last line is at 00:32:10 (DISCONNECTED, 83 %) and the last step ends at 00:35:08. The last 2 min 58 s are not in the evidence. Same kind as R47.
- Evidence: `b27/b27_heartbeat.log` line 11; `b27/b27_unit.log` lines 156 and 686.

**VR-16 — note** (not an R finding; seen in the revision entry)
- Where: record, A w1, lines 9216–9218: "the main text has it once, to deny it ("the fall is not an artefact"), and S3 Text and S19 Table quote it where it is the plan's word"
- Problem: S3 Text also has the word once outside quotation, in a sentence unchanged from 8bd189e.
- Evidence: `S3_Text.md` §9, line 546: "not an artefact of scale"; the quoted uses are at `S3_Text.md` line 305 and `supplementary.md` lines 1617–1618.

**VR-17 — note**
- Where: dispositions, line 238: "### R33 — minor"
- Problem: T38's heading is "### T38 — minor (also R33)" (line 578) and T38 (iii) says "As R33"; R33's heading lacks "(also T38)". It is the only one-sided cross-reference among the 145 headings.
- Evidence: parse of all 145 headings.

## R01–R57, one by one

- **R01** — verified. `@@AUDIT_TEXT@@` occurs only in the three audit reports that quote it; `S5_Text.md` §5 (line 33) states three audits, 145 findings and `dispositions_revision.md`.
- **R02** — verified. Results 2's last sentence as quoted; S2 Table "−0.9833 (0.0020), PASS" with its note on the pre-specified positive direction; S1 Text "void under its controls"; record's C m18 the same.
- **R03** — verified in every place. Means from `matched_slope.csv` (first two fields rejoined, 100 replicates each): +0.00218249, +0.00203431, +0.00485131, +0.00423169; differences 0.00014818 and 0.00061962, that is 0.0001 and 0.0006. Places: Results 4 (line 124), S3 Text §6 (line 402), "B28, outcome" (c) (lines 9008–9011), S19 Table row B28 (c) (line 1677), numbers rows CSV 800–801 (on `derived_r24.out` lines 55–56), `derived_r24.out` item 5. "0.0002 and 0.0007" remains only where it is given as the difference of the rounded cells.
- **R04** — verified. Caption (line 122 and the figure script), title (script line 471), script comment and revision note, record's C m9. (c) spans 0.05 nats at ratio 0.20 against 0.30/0.30 and 0.20/0.20: a quarter.
- **R05** — verified. In all nine rows of sts, r₁ and substituted sts in `baseline_gap_tables.md` (a) the adjusted contrast is the smallest in size.
- **R06** — verified. Results 2 (line 87), S1 Text line 9, CLAUDE.md, README.md, record's B MINOR 6, R201's `why`.
- **R07** — verified at the place named (line 267). The unqualified claim persists in S4 Text Sh3 (VR-7).
- **R08** — verified. Four S3 Text passages name the reviewers by role with "(S5 Text §5)"; S5 Text §4 has "started by `b27_start.sh`"; session names occur only in `S5_Text.md` line 33 (§5); no round, stage or bundle name or reviewer's letter in the seven manuscript files.
- **R09** — verified for the table. Unsigned 0.0112 row and the "20" date row are gone; the second 0.05 (CSV 1294) and the second 1 of Remedies (CSV 1334) have rows; Inference 20 rows on 20 tokens, Remedies 6 on 6, Results 6 18 and 28. The descriptions are inexact (VR-8, VR-9).
- **R10** — verified in the tree: Methods (line 213), S1 Text, S4 Text D4 (both counts), claim record's pointer, "B29, outcome" item (i), numbers row CSV 1228.
- **R11** — verified. S3 Text §10 (line 552) as quoted; the files are in `pubmed_search/`.
- **R12** — verified. Abstract "underlies most fMRI synergy reports we found"; record's C m7 names the Abstract.
- **R13** — verified. Abstract 300 whitespace tokens (line 15), Author summary 200 (line 19); `abstract_summary_revision.out` says the same; no "299" in scope.
- **R14** — verified. +0.444867, +0.332750, +0.495364, +0.898873 from the pickles; Fisher-z intervals [−0.112, +0.789], [−0.240, +0.734], [−0.048, +0.812], [+0.704, +0.968].
- **R15** — verified. 0.0155 in the Abstract, Results 4 and Discussion; three rows on `baseline_gap_tables.md` line 43 with "(13 df)"; SE 0.0051146 × 3.030520 = 0.0155000.
- **R16** — verified. "2.645 per subject" (line 114); source "+2.6450"; S5 Text §4 records the audit's value as unused.
- **R17** — verified. 264 rows = 44 labels × 6 sets; 32 labels of the four quantities in eight cells = 192 rows; 12 diagnostic labels in the four W = 60 cells = 72 rows.
- **R18** — verified. 29 outputs: 12 text files with `git=13e7299`, 16 arrays and 1 pickle without a header; all 29 sha256 match `outputs.sha256`.
- **R19** — corrected in the tree (Discussion, both list entries, S3 Text §4, S5 Text §1, the numbers-table note at CSV 105). The disposition is inexact in two details (VR-10).
- **R20** — verified. Recommendations (line 197); "B16c, outcome" item (ii); record's A m4 and B MINOR 4.
- **R21** — verified. Abstract's parenthesis as quoted; record's A w4 quotes it.
- **R22** — corrected in Methods (line 237) and S3 Text §5 (line 260: 4.263; 4.139; 4.535, all right). The record's disposition of B's MINOR 9 has the wrong 4.54 (VR-1); the disposition misplaces the statement in "B27, outcome" (VR-11).
- **R23** — verified. Fig 4's caption (line 116) has no "pre-defined"; record's B W3 names it. The word remains only in the committed `figures/captions_v2.md`, regenerated at the figures commit.
- **R24** — verified. Methods (line 213) and S4 Text P8 (line 41).
- **R25** — verified. The seven observations C lists are gone from S20 Table and the literature file; the counts stay in rows 2 and 3; row 5's last cell ends "not mentioned in the main text".
- **R26** — verified. Item (ii), lines 8950–8955.
- **R27** — verified. Table 3 rows 2–3 against `baseline_gap_tables.md` (c): 14 sets 0 / 0, 11, 11; 91 sets 1 / 13, 71, 63; slope and r ranges; own refits agree.
- **R28** — verified. Limitations: −0.107 and +0.037; −0.124 and −0.025; "(the positive within-run relation it predicts was not found)"; item (ii) of "B29, outcome".
- **R29** — verified. Results 7; S3 Text §8's four intervals; seven of the eight cells include zero (only +0.570 [+0.057, +0.845] does not).
- **R30** — verified. Table 2's caption; three rows marked r₁.
- **R31** — verified. Table 3's caption; Results 4 "(Table 3, whose caption gives the regressors; Fig 3c)"; no "like-for-like"; Fig 3's caption.
- **R32** — verified. "The length and the tables" in three lists; no "eight statements" in CLAUDE.md.
- **R33** — verified. S5 Text §1's heading (line 9). Heading cross-reference: VR-17.
- **R34** — verified. S1 Text line 5.
- **R35** — verified. The six rows named match the pre-run entries (B28 (d), B29 (c), B16c (e): no prediction; B27 (d), B29 (d), B16c (a): not counted). VR-13 is a note on B27.
- **R36** — verified. S3 Text line 3.
- **R37** — verified. Results 6 (line 154) cites Rosas et al. (2020); claim record's pointer.
- **R38** — verified. Rows 5 and 10 in S20 Table (lines 1721, 1726) and the literature file (lines 17, 22); both supplements are items of the note in the record and CLAUDE.md.
- **R39** — verified. Label rows on the formula tokens ({t+1}, 2S, 2S − C, n − 2, "Rows 2–6", section signs); head note counts four tables; `numbers_update.out` names no script. See VR-9.
- **R40** — verified. Limitations (line 201); record's C M3.
- **R41** — verified. CLAUDE.md lines 46–60.
- **R42** — verified. Review README lines 26–27.
- **R43** — verified. The eight statements read "the revision of 1–2 October 2026" ("1–2 Oct 2026" in CLAUDE.md). All 64 remaining "1 Oct(ober) 2026" in scope were read: none dates a move or removal. See VR-3 and VR-14.
- **R44** — "The audit's instructions"; the verifiable part holds (the application's output equals `apply_revision.out`).
- **R45** — "The audit's instructions"; the rule holds (556 added record lines, longest 120 characters).
- **R46** — "Stated, not changed"; verified. File unchanged; "B28, outcome" and S3 Text §6 state its form; `derived_r24.py` joins the first two fields.
- **R47** — verified. 23:37:10 start; last step 00:01:08 + 2,040 s = 00:35:08; log last written 00:35:10; 20:37:10–21:35:08 UTC; 3,478 s; 7, 1,428, 1, 2,040 s; 11 heartbeat lines, DISCONNECTED in 8, line 3 at 23:52:10 connected, line 4 at 23:57:10 at 99 %, last at 83 %, largest gap 300 s. VR-15 is a note.
- **R48** — the script tests the stated conditions and one more (VR-4).
- **R49** — verified. Own scratch regeneration (matplotlib 3.10.9): Fig 5's PNG −1.10 % in width and +0.11 % in height; the other five sizes unchanged.
- **R50** — verified at the two places named. Unqualified in S19 Table and S3 Text §5 (VR-12).
- **R51** — verified. Results 2: 24, 23.6, +0.0935 the largest of the fourteen (from `censoring.csv`).
- **R52** — verified. Discussion against S6 Table (−0.0468, p 0.2208; −0.0926, p 0.0450); S1 Text gives both.
- **R53** — verified in Results 2 and Fig 3's caption. Bootstrap re-run on `splithalf_subjects.csv`: 366 left out (175 and 323), [0.617, 0.991]. The old wording persists in a numbers-table note (VR-6).
- **R54** — verified. Claim record items for Timmermann et al. (2023) and Gao et al. (2026).
- **R55** — verified. 243 entries, 243 distinct ids.
- **R56** — the audit files are in the tree; CLAUDE.md's PNG condition agrees with the record; its PDF condition does not (VR-5).
- **R57** — verified. Record's C M2; Use of AI tools points to S5 Text §4.

## Not verifiable from the tree

- The dispositions' statements about the planning session's packaging, its two checks of the numbers table, the build of the replacements file and the writer's prompt (R01, R08, R09, R44, R45, R55).
- The cited works themselves: the PDFs are not in the repository, so R10, R37, R38 and R54 were checked against the claim record only.
- Whether the charger stayed disconnected after the last heartbeat line, and the day on which S20's row 10 was written.

## Checked and found exact

- **Tree and record:** HEAD 9caa60b on 8bd189e; the record is append-only (its first 8,873 lines unchanged); the five new entries are 556 lines.
- **Replacements:** applying the 243 entries to 8bd189e in scratch reproduces `checks/apply_revision.out` byte for byte and the 15 files of HEAD, apart from the entry time in the record's five headings.
- **Dispositions file:** 145 headings (63 T, 57 R, 25 C), grades equal to the findings' (3/18/31/11; 1/12/30/14; 2/4/13/6); 140 "Corrected.", 2 "Stated, not changed." (R46, T25), 3 "The audit's instructions." (R44, R45, T53). All quoted phrases of the R dispositions located by script.
- **B27:** tables (a) and (b) and the leave-one-out and leave-two-out of (c) recomputed from `baseline_gap.csv`; SE, minimal detectable difference, excesses, g 0.611; sts slope 4.2627 with its leave-one-out.
- **B28:** the whole table recomputed from `matched_slope.csv` (means, SD with divisor 100, percentiles, shares, r, the DiDs).
- **B29:** counts, DiDs, p, shares and correlations from `censoring.csv`; subject 8 and subject 14.
- **B16c:** the eight cells and the p = 1 and p ≤ 5 rows from the two pickles, with own sign-flip test, inversion and Fisher-z intervals; all equal the record, S3 Text §8, Table 4 and `derived_r24.out`. `derived_r24.py` re-run in scratch gives its committed output but for the header line.
- **Numbers table:** own tokenizer and placement: 1,378 rows, one on each number token; no number token without a row apart from the kinds the head note names and 5 label rows on such tokens; none out of reading order; no occurrence-index error. Own locator check: 1,073 rows with a line locator, each held string and anchor on the named line. 1,198 − 264 + 444 = 1,378; 264 listed = 161 + 69 + 28 + 6; 20 fallback rows (17 + 3); 13 corrected anchors, 33 rows of N = 14 on record line 48, 1 held string. Each of the 69 numbers "taken out of the paragraph" was found where the list says, but for the four of VR-9 (d).
- **Committed checks:** check_numbers, check_cells, tablecheck, wc (8,498 and 8,371) and abstract_summary (300 and 200) re-run with outputs identical to the committed `*_revision.out` files.
- **Run evidence:** `evidence.txt`, `b27_unit.log`, `b27_heartbeat.log`, `outputs.sha256` and `b27_commit.sh` against the record's "The run" and S5 Text §4.
- **Figures:** `figures_check.py` read line by line. The figure script's changes from 8bd189e (colour-bar label, Fig 3c's two lines and 6.5 pt legend, Fig 5c's range, ratios and two-line title). Scratch regeneration with both scripts: Figs 2, 4 and 6 pixel-identical; the captions file has 29 lines and differs in six (header; Figs 1, 3, 4, 5, 6, each with a Source sentence and equal to the main text's); Fig 2's is unchanged and equal to the main text's.
- **S19 Table:** 81 rows in Part A, 67 counted = 36 + 15 + 16; the eleven new counted rows' verdicts against the pre-run criteria.
- **Labels in the manuscript:** no computation label before "## Supporting information"; the checks for round, stage and bundle names, reviewers' letters and session names as under R08.
