# VE: verification of the record's last entry, "The revision of 1–2 October 2026: the cold reads applied"

The entry holds up in substance: all 70 dispositions are present and almost all are borne out by the text at HEAD. I found 1 error, 12 inexact statements and 12 notes.

Object: `manuscript/analysis_record.md`, lines 9130–9429 at HEAD 9caa60b of VT (`$SP/r24/vtree`). Paths below are relative to VT; "the entry" is that entry and line numbers are those of the record at HEAD. Scratch work is under `$SP/r24/vwork/VE/`. Nothing under VT was changed (`git status --short` is empty at the end). No internet and no subject data were used.

## Findings

### VE-1 — error
- **Where:** lines 9263–9264 (list B, MINOR 9): "the leave-one-out of the residual's slope is in Table 3 and that of the sts slope (4.26: 4.14 to 4.54) in S3 Text §5".
- **Problem:** The upper end is 4.53 at two decimals. S3 Text §5 prints 4.139 to 4.535; 4.54 is a second rounding of 4.535, and a committed file holds the less rounded value.
- **Evidence:**
  - `manuscript/si/S3_Text.md` line 260: "4.139 (without subject 14) to 4.535 (without subject 8)".
  - `notes/review_results/partB/inference_revision_tables.md` line 242: "+4.1392 to +4.5346".
  - My recomputation from `notes/review_results/partB/baseline_gap.csv`: 4.262661 with all 14; 4.139204 without subject 14; 4.534629 without subject 8.

### VE-2 — inexact
- **Where:** lines 9400–9401 ("The checks."): "the locators of committed rows that the audit found wrong are corrected (13 anchors, 33 rows of N = 14, 1 held string)".
- **Problem:** 33 is not a count of committed rows. The committed table has 19 rows of 14 citing line 2 of `results/primary_b_ts_gsr_win60.csv`; all 19 are carried and now cite line 48 of the record. The other 14 rows at that locator are added by the revision: Results 2 paragraph 1 ("14 of 14"), eight in Table 2's body, Results 2 paragraph 2 ("13 of 14"), Table 3's caption, Results 7, Limitations ("7 of 14"), and Methods, Inference ("12 for the 14 subjects"). The 13 anchors and the 1 held string are committed rows: 18 committed rows had the stale anchors, 5 of them were deleted.
- **Evidence:** my counts on `git show 8bd189e:manuscript/main_text_numbers.csv` against the file at HEAD. `notes/review_2026-10-01_cold_reads/checks/numbers_update.out` lines 27–30 and the table's head note carry the qualification the entry drops: "Corrected in committed rows, and in the new rows that take their source from them".

### VE-3 — inexact
- **Where:** lines 9399–9400: "and 444 added, each with its source and line".
- **Problem:** Not each. Of the 444 added rows, 84 or 85 are label rows with empty `source_file` and `locator`, and 19 are derived rows with a derivation in place of a file and line; about 340 name a file and a line.
- **Evidence:**
  - Category counts: label 215 at 8bd189e, 251 at HEAD, 48 or 49 label rows among the 264 deleted; derived 44, 54, 9 deleted.
  - Examples at HEAD: "Results / 7. Remedies | Table 4, body | 1 | label | AR(1): a name"; "Table 3, title and caption | 91 | derived: 91 leave-two-out sets: 14 × 13 / 2".

### VE-4 — inexact
- **Where:** lines 9396–9397: "one on every number token of the main text apart from the kinds its head note names (citation years, cross-references by number, dates, the Zenodo DOI)".
- **Problem:**
  - The head note names two more kinds, "commit identifiers" and "code spans" (and "pages" among the cross-references).
  - Nine number tokens in headings have no row and are of no kind the head note names: the section numbers 1–7 of the Results headings (`manuscript/draft_v2.md` lines 37, 85, 112, 118, 144, 150, 156), "lag-0" in the heading of Results 4 (line 118), and "AR(1)" in "### The AR(1)-substituted estimate and its calibration" (line 243). The title's "AR(1)" does have a row (section "Title").
  - The ten numbers of the captions' own labels ("Fig 1." to "Fig 6.", "Table 1." to "Table 4.") have no row either.
- **Evidence:** head note of `manuscript/main_text_numbers.csv`, last sentence. My token-by-token alignment of the HEAD main text with the 1,378 rows puts every row on a token of its own paragraph. Tokens without a row: 95 citation years, 10 years and 12 day numbers of dates, 73 cross-references, the DOI, the ten caption labels, the nine heading tokens, digits inside four commit identifiers and one URL. The first four groups reconcile with `numbers_update.out`'s "105 citation years, 73 cross-references … 12 dates … the Zenodo DOI (1)".

### VE-5 — inexact
- **Where:** lines 9408 and 9410–9411 ("The figures."): "which `checks/figures_check.py` tests as stated here" and "Fig 2's caption is the committed one".
- **Problem:** The script tests one condition more than stated. For Fig 2 it requires, besides identity with the committed caption, that the caption holds a Source sentence and, without it, equals the main text's Fig 2 caption. It also requires the header's SHA to be followed by ", seed ", that is, without "-dirty". No stated condition is left untested.
- **Evidence:** `notes/review_2026-10-01_cold_reads/checks/figures_check.py` lines 89–92 (`okc = old[i] == new[i] and b is not None and b == main.get(k)`), its docstring lines 10–11 ("Fig 2's caption must be HEAD's and, without its Source sentence, the main text's"), and lines 77–78.

### VE-6 — inexact
- **Where:** lines 9358–9359: "No number left the paper: `checks/numbers_update.out` lists every deleted row of the numbers table with where its number now is."
- **Problem:** For the 28 rows of the class "label" the file gives no place. Its fifth field reads, for each, "a label (a section number, a date, a name, a formula constant) the rewritten sentence no longer carries". The other 236 rows have a place.
- **Evidence:** `numbers_update.out` line 103 (header "… | class | where the number now is") and the 28 lines with "| label |" (267, 272–279, 307–312, 314, 321, 347, 350, 356–358, 360–363, 366, 368).

### VE-7 — inexact
- **Where:** line 9343 ("the null's four-cell residual levels, the bracketed earlier p values and the one printed value that the exclusion moved (S3 Text §6)") and line 9269 ("W4 (the bracketed earlier p values)").
- **Problem:** The committed Results 4 had one bracketed earlier p value and one bracketed earlier cross-half correlation, not two p values.
- **Evidence:**
  - `git show 8bd189e:manuscript/draft_v2.md` line 118: "[0.219 before the exclusion in Methods]" and "[−0.052 before that exclusion]".
  - `manuscript/si/S3_Text.md` line 303 calls the second "the cross-half correlation r(res_even, ac_odd) (−0.052 to −0.051; Results 4)".
  - B's W4 names only the p value.

### VE-8 — inexact
- **Where:** lines 9354 and 9357–9358: "Sentences retired, each by a rule or a finding and not for length:" … "the Introduction's sentence listing the Results sections and the Author summary's first sentence".
- **Problem:** No rule or finding is named for these two, and none of the three reads has one. For the Author summary's first sentence the only reason given is the word limit.
- **Evidence:** `notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json`:
  - entry I03, why: "the section-by-section roadmap, which the headings give, not repeated";
  - entry A02, why: ends "; 200 words", after findings that concern other sentences of the summary.
  - A search of `reviews/read_A.md`, `read_B.md` and `read_C.md` finds no finding on either sentence.

### VE-9 — inexact
- **Where:** line 9421: "the dispositions above that name it assign these items to it".
- **Problem:** Several items of the list are assigned by no disposition that names the note:
  - "whether a testing day held one substance or both" (the phrase occurs only here and in CLAUDE.md);
  - "the censoring" (C's m3 disposition does not name the note);
  - "the Zenodo licence field and the written agreement" (C's m4 says "wait for the co-authors");
  - "the Supplementary Materials of Gao et al. 2026" (in no disposition).
  - A's M2 says the [TK] items are "for the co-authors", not items of the note.
- **Evidence:** the seven dispositions that name the note are A M2, B MINOR 7, C M1, M2, M4, m1 and m17 (lines 9173–9175, 9254–9255, 9276, 9279, 9292, 9304, 9328–9329).

### VE-10 — inexact
- **Where:** lines 9309–9310 (list C, m4): "the agreement and the acknowledgments wait for the co-authors".
- **Problem:** The disposition does not agree with other places on the agreement. C's finding was that the written agreement "must exist in writing from C.T. and S.P.S."
- **Evidence:**
  - `manuscript/draft_v2.md` line 267 (unchanged): "the data are used with the written agreement of the data collectors and the derivative authors".
  - `manuscript/si/S4_Text.md` line 75 (Sh2): "reuse terms confirmed by the data collectors and derivative authors".
  - `README.md` lines 180–183 and `CLAUDE.md` lines 40 and 698: "confirmed by email from C. Timmermann (13 September 2026) and S. P. Singleton (14 September 2026)".

### VE-11 — inexact
- **Where:** lines 9273–9277 (list C, M1): "M1 (the subject-code passage): the Ethics statement replaced by a standard statement".
- **Problem:** One part of the finding is neither answered nor said to be left. C wrote that the codes in the git history contradict "cloned into external/DMT_NCT/ and not redistributed". The disposition does not mention it and the sentence stands.
- **Evidence:** `reviews/read_C.md` (M1, "It also contradicts p. 20 l. 493 …"); `manuscript/draft_v2.md` line 267 ("cloned into `external/DMT_NCT/` and not redistributed"); `manuscript/si/S4_Text.md` line 75.

### VE-12 — inexact
- **Where:** lines 9266–9267 (list B, W1): "Results 3, S3 Text §4, S5 Table's note and S19 Table's row: p < 1/10,000, no rotation reaching the observed value".
- **Problem:** S19 Table's row has "spin p < 1/10,000" without the clause on the rotations. The other three places have both.
- **Evidence:** `manuscript/supplementary.md` line 1623 ('spin p < 1/10,000: "the predicted branch obtained"'), against `draft_v2.md` line 114, `S3_Text.md` line 130 and `supplementary.md` line 101.

### VE-13 — inexact
- **Where:** `notes/review_2026-10-01_cold_reads/checks/numbers_update.out`, the file the entry cites for where each deleted number now is.
- **Problem:** Two of its glosses do not match:
  - Line 365 glosses the deleted "10" as "the level of the differences of the full run, 10⁻¹⁶". The committed row and sentence concern the re-run of the data-free computations of 23 September 2026. The place (S5 Text §4) is right.
  - Line 345 sends "42" to S3 Text §8, which now prints the rate as 41.8 %. "42 %" is no longer in the paper; the quantity is.
- **Evidence:** committed CSV row "derived: 10⁻¹⁶: the level of the differences in the re-run of the data-free computations of 23 September 2026"; `manuscript/si/S5_Text.md` line 25; `manuscript/si/S3_Text.md` line 542.

### VE-14 — note
- **Where:** lines 9217–9218 (list A, w1): "the main text has it once, to deny it ("the fall is not an artefact"), and S3 Text and S19 Table quote it where it is the plan's word".
- **Problem:** S3 Text also uses the word once in its own voice, not as a quotation: "not an artefact of scale". It is committed text and is not said of the change in r₁.
- **Evidence:** `manuscript/si/S3_Text.md` line 546 (§9); the quotation of the plan is at line 305; S19 Table at `supplementary.md` lines 1617–1618.

### VE-15 — note
- **Where:** lines 9333–9334 (list C, w4): 'w4 ("within a window"): Abstract.'
- **Problem:** The Abstract does not have these words. It has "per within-window standard deviation", as A's w4 disposition quotes it. "within a window" is in Results 1.
- **Evidence:** `manuscript/draft_v2.md` lines 15 and 53.

### VE-16 — note
- **Where:** lines 9183–9185 (A m4), 9323 (C m13) and 9294–9295 (C M5 (a)).
- **Problem:** Three sub-points of findings are not mentioned in their own dispositions:
  - A's m4 asked that Cliff et al.'s condition and numbers be confirmed. This is answered under C's m14 (S3 Text §8), not under A's m4.
  - C's m13 said "Manuscript for co-author review; not for citation or distribution" must go at submission. The line stays (`draft_v2.md` line 267) and the disposition says only "condensed".
  - C's M5 (a) added "ideally, confirmed with those authors". The disposition is silent on it.
- **Evidence:** `reviews/read_A.md` (m4, last sentence); `reviews/read_C.md` (m13, M5 (a)).

### VE-17 — note
- **Where:** lines 9294–9295 (list C, M5 (a)): "the Introduction, S20 Table's row 3 and the literature file state it in one neutral form (the study names the quantity the persistent synergy and gives the whole-minus-max formula of its Eq. 5)".
- **Problem:** The Introduction's form lacks "whole-minus-max"; that phrase is in Results 1. S20 Table's row 3 and the literature file have the form as described.
- **Evidence:** `draft_v2.md` line 25 ("who name their synergy the persistent synergy and give its formula as their Eq. 5, the four-atom sum of Results 1"); `supplementary.md` line 1719; `notes/partB5_literature_v2.md` line 15.

### VE-18 — note
- **Where:** lines 9340–9341: "Statements of the committed main text that are now in the supporting information or in a table, each pointed to from the main text:".
- **Problem:** The list omits one such statement: the Use of AI tools sentence on the accidental copy of the data and its 28-second test, now only in S5 Text §4 and pointed to from the main text. C's M2 disposition and `numbers_update.out` line 359 do name it.
- **Evidence:** `git show 8bd189e:manuscript/draft_v2.md` line 236; `manuscript/si/S5_Text.md` line 25; `draft_v2.md` line 257.

### VE-19 — note
- **Where:** line 9348, in the same list: "the ideal-band-pass r₁ at TR 0.72 s and the derivative there (S3 Text §10)".
- **Problem:** At the statement's former place the main text now points to S3 Text §4, which does not hold the 32.8. Its pointer to S3 Text §10 is in the next sentence and is given for the rank gradient. The values 0.97 and 32.8 are in S3 Text §10.
- **Evidence:** `draft_v2.md` line 193; `S3_Text.md` lines 128, 552 and 556.

### VE-20 — note
- **Where:** lines 9339–9340: "the text was condensed in every section, before the audits and again after them".
- **Problem:** Two Methods subsections are word for word those of 8bd189e: "Redundancy functions" (113 words) and "Regional maps" (61 words).
- **Evidence:** section-by-section comparison of `git show 8bd189e:manuscript/draft_v2.md` with HEAD; `checks/wc.out` and `wc_revision.out` give the same counts for the two.

### VE-21 — note
- **Where:** lines 9411–9414: "Fig 5c's y-range and two-line title, with height ratios of 0.30 : 0.20 : 0.20 for 0.30 : 0.20 : 0.10, which leaves panels (a) and (b) six-sevenths of their height".
- **Problem:** The diff of the script has one drawing parameter more for Fig 5c that the paragraph does not name: the legend's anchor, `bbox_to_anchor=(0.0, -0.42)` to `(0.0, -0.25)`. By the GridSpec arithmetic the legend's distance below the axis goes from 0.42 to 0.4286 of the former panel height, about 2 % more. Also, in Fig 3c the legend's entries are 6.5 pt, while its title stays at 6.8 (`title_fontsize=6.8`).
- **Evidence:** `git diff 8bd189e HEAD -- scripts/15_figures_v2.py`. Everything else in the paragraph's list of drawing changes is right; see "Checked and found exact".

### VE-22 — note
- **Where:** line 9414: "each with a width and a height within 3 % of the committed file's".
- **Problem:** In a scratch regeneration, Fig 5's PNG is 2.22 % narrower than the committed one (2212 to 2163 px), which is 0.78 % inside the limit. My environment is not the pinned one (matplotlib 3.10.9, numpy 2.4.4, pillow 12.2.0, against 3.11.1, 2.5.3 and 12.3.0), and the three figures that are not redrawn differ here by up to 0.72 % in a dimension. Because of that, conditions (2) and (3) for Figs 2, 4 and 6 could not be assessed.
- **Evidence:** `scripts/15_figures_v2.py` and `figures_check.py` run in a clone under `VW/VE/figclone`. Condition (1) was met in full (header "at git 9caa60b, seed 20261120"; five captions changed and equal to the main text's; Fig 2's the committed one). Figs 1, 3 and 5 were redrawn within 3 % (+0.40 %/0.00 %; −0.09 %/−0.42 %; −2.22 %/+0.04 %).

### VE-23 — note
- **Where:** lines 9138–9139: "No computation of this commit was run on the data; `derived_r24.py` reads committed per-subject vectors, arrays and CSV files."
- **Problem:**
  - The same entry says later (lines 9389–9392) that the text audit fetched the released series and computed three values quoted in `audit/findings_text.md`, a file of this commit. The two statements have to be read together.
  - `derived_r24.py` also reads one Markdown table.
- **Evidence:** `notes/review_2026-10-01_cold_reads/audit/findings_text.md` lines 20–21, T07, T10, T25; `checks/derived_r24.py` line 86 (`inference_revision_tables.md`).

### VE-24 — note
- **Where:** lines 9152–9153: "S1, S3, S4 and S5 Text and S11, S18, S19 and S20 Tables as the outcome entries and the lists say".
- **Problem:** Three more tables of `supplementary.md` change. S5 Table's note is named in B's W1 disposition. S12 Table (its pointer now reads "the Results' opening paragraph") and S13 Table (the clause "the printed means: the pair r₁ DiD is saved at four decimals") are named nowhere in the entry. The sentence lists "the main changes" and does not claim to be complete.
- **Evidence:** table-by-table comparison of `git show 8bd189e:manuscript/supplementary.md` with HEAD.

### VE-25 — note
- **Where:** lines 9341–9351, the same list of moved statements, with the "each pointed to" claim.
- **Problem:** None beyond VE-18 and VE-19; recorded so the coverage is clear. A clause-by-clause comparison of the committed main text with HEAD (527 clauses, 251 not verbatim at HEAD) found no other statement that left the main text without being on the entry's lists. The remaining differences are rewordings or clauses whose content stays in the main text.

## Checked and found exact

**1. The 70 dispositions**
- The count is 20 + 19 + 31, one per finding, in the reads' order.
- Each was read against the finding in full and against the named place at HEAD; apart from the findings above, each named place holds what is stated.
- Quoted phrases found word for word:
  - "can move" / "either way" (Abstract, Results 1, Discussion);
  - "the sts surface of Fig 1a" (Discussion; S20 Table's caption in the SI list);
  - "the r₁-dependence included" (Results 5; Fig 6's caption);
  - "the fall is not an artefact";
  - "4.7 to 1 per within-window standard deviation; neither is lagged coupling, which can move it either way";
  - "excludes zero exactly when p ≤ 0.05";
  - "relative to placebo" (Author summary, Results 2);
  - "The fall of r₁ under DMT";
  - "Creative Commons Attribution 4.0 International";
  - "most fMRI synergy reports we found"; "the ten empirical studies we found"; "lowers sts"; "in the texts we read".
- Gone from the main text as stated: "pre-defined", "scope map", "the calibration is not validated", spin "p < 0.0001".
- Numbers in the dispositions checked against the sources:
  - −1.74, 0.035, +0.009; −0.015 to −0.036; 0.80 / 0.09 / p = 0.0002;
  - 0.898 and 2.30 (`derived_r24.out` item 7); 2.645;
  - SE 0.0051, 0.0155 (13 df, S3 Text §5), excesses 0.0088 / 0.0066 / 0.0061 and 0.006–0.009;
  - 0.0564 / 0.0009; a fifth and a sixth (0.197, 0.163);
  - 0.50 as a sixth of 3.09 (`derived_r24.out` item 3: 0.161);
  - |ρ| ≥ 0.80 and ρ = −0.98; pp. 15–16, 41.8 % and over 88 %;
  - ten studies / eight MMI / five Gaussian / one CCS;
  - y-range −0.02 to +0.03 and the quarter scale; 300 and 200 words.
- The disattenuation's exclusion rule: B21's bootstrap replicated from `splithalf_subjects.csv` with the script's seed gives 366 draws excluded, all for a non-positive reliability, an interval of [0.617, 0.991], and draws above one.
- Thirteen atoms of Table 1 have a non-zero printed substituted DiD with the same sign as observed; three print as 0.0000.
- S19 Table Part A counts 36 met, 15 partly met and 16 missed, 67 in all.
- The seven observations C listed are gone from S20 Table and `notes/partB5_literature_v2.md`.
- The record's entries named by the dispositions exist and say what is cited: the decisions of the entry on the cold reads, B28's rule (i) and (iv), "Git history and the participant codes".

**2. "The revision."**
- Exactly seven references are added (41 to 48 entries, none removed or changed), each cited before "## References".
- `claims/claims_2026-10-01.md` has sections for the seven, for Barrett 2015, Liardi 2025, Luppi 2022 and 2024, Cliff 2021 and for the two source papers.
- Each "main change" is present.
- `pubmed_search/`: 11 records; 2 records (PMID 27534393 and 39735490), neither ΦID on psychedelic data; three queries of 2 October recorded; Pope 2025 and Gao 2026 assessed in `screening.md`; `search_string.txt` says the Search details were not kept. Both strings are verbatim in S3 Text §10.
- Not checkable here: the readings of the PDFs, which are not in the tree.

**3. "The length and the tables."**
- The decision of 23 September 2026 is at record lines 6571–6578 and set what is said.
- Every listed moved statement was in the committed main text, is gone from HEAD in that form, and is at the named place; the moved sentences are verbatim in S3 Text §2, §8, §9 and S5 Text §1, each marked as moved. The pointers exist, apart from VE-19.
- The items "written for this revision" exist at HEAD and not at 8bd189e. B28's and B29's rows and B27's tables (a) and (b) are transcribed. B27 (c)'s three rows are given as prose; B16c appears as a summary table in §8 with the rest left to the tables file.
- The five quoted retired sentences were in the committed text and are gone.
- All 264 deleted rows were read: 161 former Table 3 (caption and body verbatim in S3 Text §6), 69 "taken out", 28 labels, 6 "re-created". Each of the 69 numbers is at its stated place. Every distinct number token of the committed main text occurs in the HEAD paper, except "−0.062" (Table 4 has −0.0620) and Cliff's "42 %" (now 41.8 %).
- `wc.py` gives 8,498 with headings and 8,371 without; my own count agrees. The main text has four tables and six figures.
- Not checkable: the first draft's "about 9,000 words".

**4. "The checks."**
- check_numbers ("rows 1378, data rows 786, flagged 11", all eleven "SIGN DIFFERS (check wording)"), check_cells ("flagged 0"), tablecheck (0 wrong cell counts), wc and abstract_summary reproduce the committed `*_revision.out` byte for byte.
- The 243 replacements, re-applied to the committed files in a scratch copy, give files with the sha256 of `apply_revision.out` and of HEAD. The record differs only by the five headings' «ENTRY_TIME», which the folder's README documents.
- Counts on the numbers table by my own mapping:
  - 1,198 − 264 + 444 = 1,378; classes 161 / 69 / 28 / 6;
  - 4 numbers changed in place; 17 locators moved; 13 anchors; 1 held string (0.003: +0.0027); 1 note reworded;
  - 279 contexts recomputed; 20 fallback rows (17 + 3), each the same quantity in its rewritten sentence.
- After the update every anchor and held string is on its line.
- There is no computation label in the main text before "## Supporting information", and no round, stage or bundle name and no reviewer's letter in any manuscript file. "planning session" and "writer's session" occur only in S5 Text §5 (line 33). S5 Text §4's "A drafting session's clone" is committed text and neither of the two names.

**5. "The figures."**
- `figures_check.py` was read line by line; conditions (1) to (3) and the closing message are tested as stated, apart from VE-5.
- Drawing changes named correctly: Fig 1b's colour-bar label; Fig 3c's two slope lines and legend entries at 6.5 for 6.8; Fig 5c's y-range, two-line title and ratios (the old third ratio was 0.06 − (−0.04) = 0.10). Six-sevenths is exact by the GridSpec arithmetic (figure size and hspace unchanged, no tight or constrained layout). The captions that change are 1, 3, 4, 5 and 6.

**6. "The audits of the prepared revision."**
- Finding counts: 63 (3, 18, 31, 11), 57 (1, 12, 30, 14), 25 (2, 4, 13, 6).
- 145 dispositions: 140 "Corrected", 2 "Stated, not changed" (R46, T25), 3 on the audits' instructions (R44, R45, T53).
- Each item of "What they changed" is in the tree, including the double roundings: 0.89, 2.645, 0.0155, 0.0001 / 0.0006, +0.445, with no old value left.
- `te_filter_check.py`, run on a scratch copy, gives the non-zero lag-1 transfer entropies after the filter.
- T07, T10 and T25 rest on the released series; their three values occur only in S5 Text §4.

**7. The last paragraph**
- The list of items is word for word CLAUDE.md's "Remaining work" list (829 characters).
- Every disposition that names the note has its item in the list.
