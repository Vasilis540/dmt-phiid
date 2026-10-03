VB — bookkeeping of the prepared revision (HEAD 9caa60b against 8bd189e): numbers table, replacements file, bookkeeping files, check outputs

Paths. VT = $SP/r24/vtree ; every file named below is under VT. My scripts and outputs are in $SP/r24/vwork/VB/ . Nothing under VT was changed (`git status --short` in VT is empty at the end). Rows of manuscript/main_text_numbers.csv are numbered as check_numbers.py numbers them: row n is line n + 2 of the file. "JSON" = notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json; "update list" = notes/review_2026-10-01_cold_reads/checks/numbers_update.out.

Result in one line: the table, the replacements and the check outputs reproduce (application byte-identical, all five checks byte-identical, every locator holds); 6 errors, 13 inexact statements and 14 notes follow, none of which changes a number printed in the paper.

FINDINGS

Errors

VB-1 — error
Where: update list, deleted list, lines 316–318: "paragraph 3 | −0.0006 | taken out of the paragraph | S3 Text §6 and S18 Table (A_other's DiD)"; the entries of −0.0017 and +0.0004 likewise ("S3 Text §6 and S18 Table").
Problem: the data's A_other DiD and its interval are in S3 Text §6 but not in S18 Table.
Evidence: manuscript/si/S3_Text.md line 341 ("changed by −0.0006 [−0.0017, +0.0004] under DMT relative to placebo") and lines 325, 349 (−0.00059 [−0.00166, +0.00041]). In manuscript/supplementary.md, S18 Table (lines 1339–1598) has for this statistic only line 1577, "| A_other (sign from the other run) | −0.00028 ± 0.00019 | +0.00001 ± 0.00031 |", the generator's level and expectation (which the two following entries, +0.0000 and 0.0003, rightly cite); the data's −0.00059 is at line 1648 (S19 Table, Part A) and its interval is not in the file. (The why of R403 names "S3 Text §6 and S18 Table" for the constructions, the former Table 3 and A_other's change together, which holds only of the three taken together.)

VB-2 — error
Where: update list, lines 298, 299, 301, 302: "paragraph 3 | 0.349 | taken out of the paragraph | S3 Text §5 and Fig 3b" (likewise 0.913, 0.174, 0.876). The same in the why of R205 ("The two cross-half correlations (0.742 [0.349, 0.913] and 0.645 [0.174, 0.876]) are in S3 Text §5 and Fig 3b") and in manuscript/analysis_record.md line 9345 ("the two cross-half correlations with their intervals (S3 Text §5; Fig 3b)").
Problem: Fig 3b gives the two correlations, not their intervals.
Evidence: manuscript/draft_v2.md line 110, caption (b): "(filled circles, r = +0.742)", "(open triangles, r = +0.645)", then the interval of the mean only; the panel prints the same (scripts/15_figures_v2.py lines 342, 343, 349). None of 0.349, 0.913, 0.174, 0.876 occurs in draft_v2.md; all four are at S3_Text.md line 167. In the same why, "the band-passed generator's −0.0944 for a fall of 0.0154 in S13 Table and the Discussion" is not exact for the Discussion, which has "(−0.094)" and no 0.0154 (draft line 183).

VB-3 — error
Where: main_text_numbers.csv, row 562 (added; Results 2, paragraph 3, "10,000", design): source notes/review_results/partB/inference_revision_tables.md, locator "line 284; anchor: | ts_gsr | +0.742 | +0.645 | +0.694 |", note "B21 (d): 10,000 subject-bootstrap draws (the table's 'draws excluded' column counts them)".
Problem: the named file does not hold the setting, and the column the note names counts the excluded draws.
Evidence: no "10,000" or "10000" in inference_revision_tables.md; line 284 ends "| [+0.617, +0.991] | 366 |" under the header "draws excluded"; the setting is `N_BOOT = 10000`, notes/partB21_inference_revision.py line 82.

VB-4 — error
Where: JSON, why of A01: "The cross-half correlation's interval is printed from its six-decimal value (`derived_r24.out`, item 6: [0.258077, 0.894889])".
Problem: the file's lower limit is 0.258078.
Evidence: notes/review_2026-10-01_cold_reads/checks/derived_r24.out line 58: "interval [+0.258078, +0.894889]"; recomputed from notes/review_results/partB/splithalf_subjects.csv: 0.2580778, 0.8948893. The printed 0.26 and 0.89 are not affected.

VB-5 — error
Where: JSON, why of R102: "A's m2 (the exchange rate for lagged coupling and the pair-averaged response, from S3 Text §3 and §7 and S18 Table (b))".
Problem: the pair-averaged response the text quotes (+0.009 nats for c = +0.02) is in part (a) of S18 Table, not (b).
Evidence: supplementary.md line 1367, under "### (a) Population residual changes, closed form": "| (a3) coupled family, r₁ and q held | c = +0.02 | +0.00912 |"; (b)'s row for the same change (line 1450) has "+0.00335 ± 0.00047". Row 155 of the numbers table sources the +0.009 to B23 (a3) (diagnostic_alternatives_tables.md line 30).

VB-6 — error
Where: JSON, whys of U17.5 ("C's M5 (b): an observation about a paper that does not bear on its applicability, removed.") and LT07.5 ("C's M5 (b).").
Problem: the replacement removes nothing, and the finding it answers is C's M4, not M5 (b).
Evidence: old "**HRF deconvolution not mentioned anywhere in the PDF** (the Supplementary Methods it defers to are not included)", new "**HRF deconvolution not mentioned in the main text** (the Supplementary Methods it defers to were not read)". notes/review_2026-10-01_cold_reads/reviews/read_C.md line 26 (M4, last sentence) is the finding on this cell of S20 Table's row 5; line 30 (M5 (b)) lists rows 2, 3, 1, 4, 6, 8 and 11, the seven that U17.1–.4 and U17.6–.8 answer. The record (lines 9289–9296) puts row 5 under M4 and counts seven observations under M5 (b).

Inexact

VB-7 — inexact
Where: update list, lines 296 and 331: "Results / 2. The DMT contrast | paragraph 1 | 14 | re-created | still in the paragraph, in a rewritten sentence: the token has a new row with its own source"; "Results / 7. Remedies | paragraph 1 | 1 | re-created | …" (head note: "where a new row replaces the old one").
Problem: for these two of the six, the deleted row's quantity is no longer in the paragraph; the new rows of that number there belong to other quantities.
Evidence: (a) the committed row (design, results/loo_did_win60.csv, note "one refit per dropped subject: 14 per variant") sat on "in each of the 14 leave-one-out refits"; draft line 87 now reads "in each leave-one-out refit on each variant"; the added rows of 14 in that paragraph (rows 383, 384) are of "negative in 14 of 14". (b) the committed row (design, prewhiten_tables.md line 4, note "the AR orders searched") sat on "BIC, in 1–5"; the paragraph at HEAD has no "1–5"; the added row of 1 there (row 1054) is the label of "AR(1)-substituted"; the range is now in Table 4's caption (row 1062, same source). The other four entries are as described.

VB-8 — inexact
Where: update list, lines 12–14: "apart from the kinds the table does not list: 105 citation years, 73 cross-references by number (Results, Fig, Table, Eq., Example, Definition), 12 dates with their month and the Zenodo DOI (1)".
Problem: the list accounts for 191 tokens; 203 have no row (headings apart), and the 105 are not all citation years.
Evidence: own tokenisation at HEAD (title to the end of Data and code availability, and the SI list): without a row are 95 citation years and the 10 years of dates (together 105), 12 day numbers, 73 cross-references in running text (Results 28, Table 17, Fig/Fig./Figure 17, Eq./Eqs. 7, Definition 3, Example 1), the 10 numbers of the caption heads ("**Fig 1." to "**Table 4."), the leading digits of two commit identifiers (77af7aa, 13e7299) and the DOI (1).

VB-9 — inexact
Where: update list, lines 11–12: "Every number token of the revised text without a row then received a new row with its source file, line and held string"; record, lines 9399–9400: "444 added, each with its source and line".
Problem: true of 276 of the 444.
Evidence: the added rows are 276 data (file, line, held string), 62 design and 3 literature (file, line and anchor, no held string), 19 derived (no file; a derivation) and 84 label (no file, no locator).

VB-10 — inexact
Where: update list, line 365: "Data and code availability | paragraph 1 | 10 | taken out of the paragraph | S5 Text §4 (the level of the differences of the full run, 10⁻¹⁶; A's m13)"; line 353: "the sentence now says that the exposure is almost the same at every TR and names no TR".
Problem: the places are right, the glosses are not.
Evidence: the committed row's derivation was "10⁻¹⁶: the level of the differences in the re-run of the data-free computations of 23 September 2026", and manuscript/si/S5_Text.md line 25 has it of B23 and B24 "re-run independently by a separate session", not of the full run. Draft line 193 still names a TR ("at TR 0.72 s, fall outside the table's TR range, but …"); what it no longer names is the committed sentence's "TR 2 s".

VB-11 — inexact
Where: head note of main_text_numbers.csv: "17 locators moved to the lines the edits of supplementary.md, the S3 Text, the literature file and the figure script moved them to (4 held strings and 5 anchors updated on edited lines)".
Problem: none of the 17 is a locator into the S3 Text.
Evidence: the 17 carried rows whose line changed are rows 103, 108–110, 119–123, 751, 752 (scripts/15_figures_v2.py), row 1170 (notes/partB5_literature_v2.md, line 27 to 28) and rows 1349–1353 (supplementary.md, line 1637 to 1689: the 4 held strings and 5 anchors). No committed row had an S3 Text source; the 8 rows with that source at HEAD are added rows.

VB-12 — inexact
Where: head note: "69 of numbers the revision takes out of their paragraph, to the supporting information, to a table or to another paragraph".
Problem: by the list's own entries four of the 69 went to none of these.
Evidence: update list lines 322 (Results 6, 0.0112: "the clause that repeated its upper limit now gives the share alone"), 323 and 328 (0.05 twice: "replaced by the p values themselves") and 306 (Results 3, 0.0001: "'p < 1/10,000' (the same statement; B's W1)").

VB-13 — inexact
Where: main_text_numbers.csv, row 161 (added; Results 1, paragraph 10, "0.0000"): category label, note "0.0000: the printed AR(1)-substituted DiDs of rty, xtr and xty in Table 1".
Problem: the row sits on a printed value of Table 1; the head note defines a label as "a name, index, date or formula constant, not a quantity".
Evidence: draft lines 67, 69, 71 (Table 1: −0.0000, −0.0000, +0.0000), from notes/review_results/partB/family_atoms_tables.md lines 12, 14, 16.

VB-14 — inexact
Where: JSON, why of A01: "MINOR 1 and W5 (the excess and the minimal detectable difference, B27, printed at the table's four decimals)".
Problem: the Abstract prints the excess at three decimals.
Evidence: draft line 15: "0.006–0.009 above simulated pure autocorrelation changes: a test detecting 0.0155"; rows 29 and 30 of the numbers table say "+0.0061, to three decimals" and "+0.0088, to three decimals" (baseline_gap_tables.md line 43).

VB-15 — inexact
Where: JSON, whys of D01 ("A's m3 ('can move it either way, non-monotonically at the operating point'); condensed for the word limit, no statement removed."), D04 ("… condensed for the word limit, no statement removed.") and M07 ("… condensed for the word limit, no statement removed (…)").
Problem: each replacement drops clauses from its paragraph, and D01's quoted words are in neither its `new` nor A's m3.
Evidence: D01 drops "balanced by four negative atoms of the kind MMI can produce (Results 1)" and "MMI takes the smaller self-information" (Results 1, draft lines 49 and 51, still states both); its `new` has "can move it either way." and read_A.md line 30 has 'Write "can move it non-monotonically" or "at the operating point"'. D04 drops "in these data it fell under DMT relative to placebo and rose within the placebo run;" (Results 2, line 106, still says it) and "whose main texts were read in full" (Methods, line 253). M07 drops "so that it carries approximately the data's fall of pair r₁" (the −0.0146 stays).

VB-16 — inexact
Where: JSON, why of DCA01: "the run inventory pointed to in S5 Text §4, which holds every detail removed here".
Problem: three removed details are not in S5 Text §4.
Evidence: the pointers notes/review_2026-09-24/checks/derived_r17.out and notes/review_2026-09-30/checks/derived_r17_b26.out (no "derived_r17" in S5_Text.md; they are named at S3_Text.md line 130 and supplementary.md line 1707); the nine review-folder names (S5_Text.md line 33, which is §5); the script names `notes/partB14_*.py`–`partB26_*.py`, `partB16b_*.py`, `partB17b_*.py` (in no manuscript file; the new sentence has `notes/partB*.py`).

VB-17 — inexact
Where: JSON, why of REF-Schartner: "Reference added: Schartner."
Problem: the replacement adds two references.
Evidence: its `new` holds Schartner et al. (2017) and Seth, Chorley & Barnett (2013); the six REF entries add seven references.

VB-18 — inexact
Where: JSON, why of T01: "A's m10 (its last point): the TDMI row's residual DiD read beside that of sts".
Problem: it is not the last point.
Evidence: read_A.md line 44: the TDMI point ("Related: Table 1 (p.4) shows …") is the second of four; the last is on Rosas et al. (2020).

VB-19 — inexact
Where: CLAUDE.md, the "Remaining work" bullet (lines 465–467): "check that Data and code availability's sentence on the final run (at c25a310, its outputs in the commit that follows) still describes the commits that follow it".
Problem: that sentence no longer says where the run's outputs are.
Evidence: draft line 267: "it was executed as one run at commit c25a310 on V.S.'s machine on 26 September 2026 (475 min wall-clock), and every output it regenerated reproduced its committed version …"; DCA01 removed "and its outputs, the figures among them, are in the commit that follows c25a310"; S5_Text.md line 25 now holds it ("are committed in the commit that follows").

Notes

VB-20 — note. Committed design rows, carried by the revision, whose named line holds the anchor but not the setting. notes/review_results/partB/family_atoms_tables.md line 6 is the heading "## ts_gsr, W = 60: Table 1's columns with the family-predicted atoms" (the windows and N = 14 are on its line 4): rows 167–173, 347, 348, 599, 600, 952, 953 (the 1, 4, 6, 14 of the window sets and of "14 subjects") and rows 164, 165, 175, 338, 342 (the "1" of "AR(1)") cite it. manuscript/analysis_record.md line 189 ("shift), **18–45 % at W = 60**. Asymmetric family: **52–66 % at") is cited by rows 353, 410, 956 ("95"), 405–408 ("6", "14", "1", "4") and 409 (the "N = 14" of Table 2's caption, an N = 14 row not among the 33 moved to the record's line 48). Row 47 (the "1" of "lag-1") cites the record's line 1747 as "window and bin sets"; row 1330 (the "1" of "BIC over 1–5") has the locator and note of "p = 1" ("line 157; anchor: Chosen AR orders (ar1 ts_gsr)").

VB-21 — note. Committed label rows carried with a note that is not about their token: row 11 ("4.7 to 1"; note "AR(1), lag-1: names"), rows 101 and 695 ("lag-1 autocorrelation"; note "½ ln(1 + α²): formula"), row 1187 ("as r₁ approaches 1"; note "lag-1, AR(1): names"), row 1247 ("AR(1) processes"; note "unit variance, t+1: formula").

VB-22 — note. Row 1335 has the number "1.7" where the token of the text is "1.7.0" ("rsHRF 1.7.0"): the only row not on a whole token (head note: "A row sits on one number token of the text").

VB-23 — note. The five bound rows (399, 1244, 1245, 1263, 1269) have "bound on X" as their held string; X is on the line, the words are not (update list line 31: "the anchor and the held string of every row with a line locator are on the line it names"). Row 1269 holds "bound on 5.6e-16" while its note names "largest |entry| of the (f) grid, 6.7e-16"; line 209 of diagnostic_alternatives_tables.md has both, and 7 × 10⁻¹⁶ bounds the larger.

VB-24 — note. Nine number tokens in headings have no row and are not among the head note's excepted kinds: the section numbers 1–7 of Results, "lag-0" (heading of Results 4) and "AR(1)" ("### The AR(1)-substituted estimate and its calibration"); the title's "AR(1)" has row 1.

VB-25 — note. Head note: "sourced to the run's tables (…), to `notes/review_2026-10-01_cold_reads/checks/derived_r24.out`, to the committed tables they quote and to the claim record of the source papers": among the added rows, 21 design rows cite manuscript/analysis_record.md, 3 cite scripts (notes/partB28_matched_slope.py, scripts/15_figures_v2.py) and 2 the files under pubmed_search/.

VB-26 — note. JSON, why of S318c: "the six authors of Liardi et al. (2025) include four of the seven of Mediano et al. (2021), not its first author": true of Liardi et al.'s first author; the four do include Mediano, the first author of Mediano et al. (2021) (draft lines 331, 341).

VB-27 — note. CLAUDE.md line 19: "each table and figure caption in the text after the paragraph of its first citation": Table 3 is first named in Fig 3's caption (draft line 110, in Results 2: "rescaled and floored as Table 3's caption says"); its caption (line 126) follows the first paragraph of running text that cites it (line 124). The other nine follow their first citation directly (Fig 2 after Table 1).

VB-28 — note. CLAUDE.md, "Remaining work": "and their PDF files are identical once their dates are masked": the record's condition (3) ("once the two date fields, the cross-reference table and the `startxref` offset are masked") and figures_check.py (lines 128–132) mask more than the dates.

VB-29 — note. CLAUDE.md line 19 (text the revision does not change): "Every interval of a mean over subjects is B21's inverted sign-flip interval": the main text has two means over subjects with a percentile interval, each named as such: line 114 ("per subject +0.756 [+0.715, +0.790] (a subject-bootstrap percentile interval)", committed) and line 187 ("−0.24, percentile interval [−0.40, −0.08]", added by D03).

VB-30 — note. README.md line 73 and CLAUDE.md lines 19 and 589 still say "Table 3's caption" for the correction of 1 October (README's state paragraph, line 37, says "the caption of the then Table 3"). Both notes rows name one PubMed search for review_2026-10-01_cold_reads/ (README: "the PubMed search of that day"); the folder now also holds the search of 2 October (pubmed_search/psychedelic_phiid_search.md, pubmed_psychedelic_search.csv).

VB-31 — note. "8,498 words with headings" (CLAUDE.md, README.md, the record) is wc.py's output, in which a heading line is counted with `len(s.split())` (notes/review_2026-09-25/checks/wc.py lines 18–21), so its "##" or "###" counts as a word: 29 heading lines. Own count: 8,469 with headings, 8,371 without. Both are under 8,500.

VB-32 — note. notes/review_2026-10-01_cold_reads/README.md lines 50–52: "each with a `why` that names the finding or the rule it answers (and, where a sentence was condensed, where its statements now are)": 70 of the 243 whys name no finding of a read and no rule of an entry (the references, row numbers, figure script, bookkeeping files, and five that say only "Condensed for the word limit"), and D01 and D04 do not say where their dropped clauses are (VB-15).

VB-33 — note (the figures, a later commit). In a scratch clone at HEAD with my libraries (matplotlib 3.10.9, numpy 2.4.4; requirements.lock.txt pins 3.11.1 and 2.5.3), scripts/15_figures_v2.py followed by figures_check.py gives condition (1) met in full, and the PNGs of Figs 1, 3 and 5 redrawn within 3 % (largest change +0.40 %, −0.42 %, −2.22 %). Figs 2, 4 and 6 come out a few pixels different in size, so conditions (2)–(3) for them cannot be judged outside the pinned environment (no replacement touches their drawing code).

CHECKED AND FOUND EXACT

A. Numbers table (own splitter, tokenizer and matcher; the repository's scripts not used)
- Forms: head note (LF) + column line + 1,378 rows, body CRLF, 10 cells in every record; 786 data, 275 design, 251 label, 54 derived, 7 literature, 5 bound; every `check` cell "ok"; no duplicate (section, paragraph, number, occurrence). The 54 derived rows have an empty source and "derived: …" (all 54 derivations recomputed and right); the 251 label rows have no source, no locator and a note.
- Coverage and placement: every row's context is in the block its section and paragraph name, its number is a token at that context, rows are in reading order and occurrences are right. Of 1,581 number tokens (title to the end of Data and code availability plus the SI list, headings apart) 1,377 carry a row (and row 1335 sits on "1.7.0"); the rest are the kinds of VB-8. The 5 label rows on excepted tokens (rows 37–40, Barrett's Eqs. 79–82 and Varley's Eqs. 4–6; row 1230, one citation year) are carried rows, as the head note says. No computation label anywhere in draft_v2.md. The same matcher passes on the committed table (1,198 rows).
- Locators: 1,073 rows with a line locator (791 with a held string, 282 anchor-only): every anchor is on its line (170 with `@L…|` or `@pct|` prefixes, the line inside the range); every held string is on its line; every held value equals the printed number at the printed precision (half away from zero), Table 4's five shares as percentages; the two half-way cases are right against unrounded values (0.108 from 0.1075: exact p 1762/16384 = 0.10754; 0.263 from +0.2625: 0.262547 in notes/review_results/inference_rows_prewhiten.csv line 21); no printed sign contradicts its held value; the five bounds hold (0.008 ≥ 0.00757; 1.3e-14 ≥ 1.24e-14; 2.3e-14 ≥ 2.21e-14; 4e-15 ≥ 3.6e-15; 7e-16 ≥ 6.7e-16). All 276 added data rows were read against their source line: the held value is in the cell or clause the note names (for example the mean-FD DiD +0.0935 of subject 8 is the largest of the fourteen in censoring_tables.md (a)).
- The update: 1,198 and 1,378 rows; 264 deleted (161 / 69 / 28 / 6), every entry present in the committed table; 934 carried; 444 added; 4 numbers changed in place (56→67, 28→36, 14→15, 14→16); 279 contexts recomputed; 0 relabelled; 17 locators moved (4 held strings, 5 anchors); 13 anchors corrected (all in inference_revision_tables.md); 33 rows of N = 14 on the record's line 48 (19 carried from results/primary_b_ts_gsr_win60.csv line 2, 14 added); 1 held string (the Discussion's 0.003: +0.0027); 1 note reworded (row 103). The classes agree with the deleted rows' categories (the 28 "label" entries are 28 label rows). The former Table 3 is 49 caption and 112 body rows; its body (13 lines) is verbatim at S3_Text.md lines 323–335 and its caption verbatim but for its head. The 20 fallback entries: every quotation is verbatim in the committed and the revised text, and each row is the same quantity from the same source. "Where the number now is" holds for every "taken out" entry other than those of VB-1, VB-2 and VB-10 (checked in S3 Text §4, §5, §6, §8, §10, S5 Text §4, S13 and S15 Tables, Tables 2, 3, 4 and their captions, Results 1, 2, 4, the Discussion), including "a new row with the same source" for −0.0649, −0.1010, −0.0260, 99.2, 3,218, 3,220.
- Head note: four tables in its first sentence; 264 / 444 / 4 / 279 / 13 / 33 / 1 / 1; 1,378 rows; 5 label rows on excepted tokens.

B. Replacements file
- 243 entries, 243 distinct ids. Applied in order to the files at 8bd189e, every `old` occurs exactly `count` times at its point (241 once; U06b.3 twice; U09 four times). The result is byte-identical with HEAD for 14 files, and for manuscript/analysis_record.md once the time in its five new headings is masked ("2 Oct 2026 18:40 UTC", the simulated commit's time); the record is append-only (its 8bd189e content is a prefix of HEAD's). checks/apply_revision.out has 243 "ok" lines in the JSON's order and its 15 sha256 equal my application. The revision is these 15 files and 21 new files (36 changed).
- All 243 whys read against `old`, `new` and the places they name. Apart from VB-2, VB-4–VB-6, VB-14–VB-18 and VB-26, they are true as written; verified in particular: the moves of R107, R316/S316 and T01 (S3 Text §6 line 303 and 307), R404/S306 (verbatim), R703/S318 (S3 Text §9), L01/S320 (S3 Text §2 line 106), S321 (S3 Text §8), S314b and D05 (S3 Text §10, §4 and §6: +0.799, +0.094, +0.0197), M09 and S501 (S5 Text §4: both occasions), M10/S504 (S5 Text §1: the same eight deviations), I02, I03 and R401 (the statements are where the whys say); A01's "eight of the ten studies state MMI" (S20 Table rows 1, 3–8, 10); A02's positive DiDs (subject 14 for sts; subjects 5 and 14 for r₁, baseline_gap.csv); R205's exclusion rule and N_BOOT; R301's +2.6450 and B22 (e)'s range; R601's −0.01535 to −0.03637; R602's seven p values (S15 Table); D03's S6 Table values and the single "artefact" in the main text; M08's four records; U06's 67 = 36 + 15 + 16 with 11 new and B26's cell; S318c's four of seven authors; F08/F09b's ratios; REC01 (nothing above edited). Every reviewer label cited exists in the reads. Statements about what cited works say were not checked (not in this task).

C. Bookkeeping files at HEAD
- CLAUDE.md, README.md and the review folder's README: commits 24919ea → 13e7299 → 8bd189e as described; the run at 13e7299 on 1 October (UTC) with outputs at 8bd189e; 8bd189e's four evidence files; the first JSON's ids; abstract 300 and Author summary 200 words; 8,498 / 8,371 by wc.py; limit 8,500; four tables, six figures, numbered in order of first citation; 1,378 rows; S19 Table Part A: 81 rows, 36 met, 15 partly met, 16 missed = 67, the other 14 as the sentence after Part A lists them; 70 findings of the reads and 145 of the audits; seven references added; S5 Text §1 and §4–§6 changed; `B1–B29`; no file path or code span in the main text outside Data and code availability; no round, stage or bundle name and no reviewer's letter in the manuscript files; session names only in S5_Text.md line 33 (§5). Every file under notes/review_2026-10-01_cold_reads/ is named in its README and every file it names exists (`figures.out` is to come). The statements on the figures are plans consistent with the record's paragraph "The figures" and with figures_check.py (thresholds 3 %, 0.1 % of pixels, 32 of 255); the items for the note to C.T. and S.P.S. equal the record's list.

D. Check outputs
- Re-run from VT without writing: check_numbers.py ("rows 1378, data rows 786, flagged 11"), check_cells.py ("flagged 0"), tablecheck.py ("rows with a wrong cell count: 0"), wc.py and abstract_summary.py are byte-identical with their committed `*_revision.out`. derived_r24.py on a copy: identical but for its header (git=nogit against git=8bd189e). The four scripts of scripts_check_revision.out parse.
- The 11 "SIGN DIFFERS" rows (10, 88, 91, 534, 582, 725, 727, 756, 771, 772, 1213) are right in direction: each prints a magnitude whose direction the words give ("fell by 0.0164", "exceeds the observed level by 4.3 % … 1.1 %", "by 0.049 nats", "a fall of 0.012–0.015", "to within 0.053", "moves … by" with ∂sts/∂q = −0.19 beside it), and row 582's is the hyphen of the range "0.680-0.830", not a sign.
