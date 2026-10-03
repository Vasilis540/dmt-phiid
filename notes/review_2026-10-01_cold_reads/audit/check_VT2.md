# VT2 — verification of the dispositions of T32–T63 (HEAD 9caa60b of VT)

All 32 findings were read with the sources they cite, and each disposition (with the R dispositions it points to) was checked at HEAD. Every correction is in the tree at the place named, and in every case the corrected manuscript text agrees with its source. What is left: 1 wrong number in the record's last entry, 8 inexactnesses (three in the wording of `dispositions_revision.md` itself), and 8 notes. VT was not modified (`git status` clean); scratch files are under VW/VT2/.

## Findings

**VT2-1 — inexact**
- Where: `audit/dispositions_revision.md`, T37 (L576): "Both say "the caption of what was then Table 3 (the residual table, now in S3 Text §6)"."
- Problem: The phrase is word for word in S5 Text §5 only. §6 reads "71cf932 (1 Oct, the correction of the caption of what was then Table 3, now the residual table of S3 Text §6)". The correction itself is made in both places.
- Evidence: `manuscript/si/S5_Text.md` L33, L37.

**VT2-2 — inexact**
- Where: `README.md` L73 (Repository layout, row `notes/`): "the correction of Table 3's caption with its checks and audit (`review_2026-10-01/`)".
- Problem: T37's stale name persists here. That table is now the residual table of S3 Text §6, and Table 3 is the per-subject-slopes table. The same file says "in the caption of the then Table 3" at L35–36.
- Evidence: README.md L35–36, L73; S3_Text.md L319–321; draft L126.

**VT2-3 — inexact**
- Where: `dispositions_revision.md`, R22 (the disposition of T47), L170: ""B27, outcome", item (v), and the disposition of B's MINOR 9 say both."
- Problem: Item (v) of "B27, outcome" states the assumptions only. The leave-one-out of the sts slope is in the same entry, but in the paragraph "The sts rows and (c), as the run reproduced them".
- Evidence: `manuscript/analysis_record.md` L8963–8965 (item (v)); L8937–8939.

**VT2-4 — error**
- Where: `manuscript/analysis_record.md` L9264 (last entry, B, MINOR 9): "that of the sts slope (4.26: 4.14 to 4.54) in S3 Text §5".
- Problem: The upper end of the leave-one-out range is 4.5346, which is 4.53 at two decimals. 4.54 is a second rounding of the printed 4.535.
- Evidence: `notes/review_results/partB/inference_revision_tables.md` L242 ("+4.1392 to +4.5346"); `derived_r24.out` item 8 ("+4.535"). Recomputed from `inference_rows_raw.pkl`: 4.1392 (without subject 14) to 4.5346 (without subject 8); from `baseline_gap.csv`: 4.53463. S3 Text §5 (L260) and "B27, outcome" give 4.139 to 4.535, which is right.

**VT2-5 — inexact**
- Where: `dispositions_revision.md`, T58 (ii), L680–681: "Results 4 and Fig 3's caption call the three rates "ratios of means under one change of r₁"".
- Problem: Word for word in Results 4 only. Fig 3's caption has "each a ratio of means under one change of r₁".
- Evidence: draft L124, L110; `scripts/15_figures_v2.py` L352.

**VT2-6 — inexact**
- Where: `dispositions_revision.md`, T61 (iii), L705–706: "once in the main text, to deny it, and quoted as the plan's word in S3 Text and in S19 Table's rows of B2 and B3"; record L9217–9218 (A's w1).
- Problem: S3 Text has a second, unquoted occurrence in §9: "not an artefact of scale". The other four occurrences in the manuscript files are as stated.
- Evidence: S3_Text.md L546, L305; draft L187; supplementary.md L1617, L1618 (search for "artefact"/"artifact" in the main text, S1–S5 Text and supplementary.md: five occurrences).

**VT2-7 — note**
- Where: S3_Text.md §8, L497 and L501; supplementary.md S11 Table, L260 and L309: "observed sts level 0.2766, AR(1)-substituted 0.2438, residual +0.0328".
- Problem: T61 (ii) persists for the order p ≤ 5. 0.2202 is the DMT pre-injection level; 0.2766 is the mean over both runs and all windows. Neither place says so; the corrected sentence says it for p = 10 and 20 only.
- Evidence: `notes/partB16_prewhiten.py` L205 (`np.nanmean(R['obs'])`). From `prewhiten_atoms_arp_ts_gsr_mmi_win60.npy`: 0.2766 over both runs and all windows, 0.2202 over DMT windows 1–4.

**VT2-8 — inexact**
- Where: supplementary.md, S19 Table Part A, "reported at": B7 (L1621) "S3 Text §6; S5 Text §1 (the deviations)"; B19 (c) (L1637) "Results 2; S3 Text §5; Fig 3"; B16c (e) (L1687) "S11 Table; S3 Text §8".
- Problem: The kind of gap T57 (ii) describes persists in three cells. Each omits a place where this revision newly reports the item:
  - B7: the Discussion (draft L193, "a split-half test left undetermined whether what they share is signal").
  - B19 (c): the Abstract (L15, "cross-half r 0.69 [0.26, 0.89]") and the Discussion (L183).
  - B16c (e): Results 7 (L158, "the AR(1)-substituted estimate carries −0.0037 of it").
- Evidence: the lines named; `git show 8bd189e:manuscript/draft_v2.md` (cross-half correlation in Results 2 and Fig 3 only; no split-half clause in the Discussion); `prewhiten_fixed_tables.md` L127.

**VT2-9 — inexact**
- Where: `manuscript/analysis_record.md` L9421: "the dispositions above that name it assign these items to it".
- Problem: The list is word for word CLAUDE.md's, but five of its items are assigned to the note by no disposition above: whether a testing day held one substance or both; the censoring; the Zenodo licence field and the written agreement; the [TK] items; the Supplementary Materials of Gao et al. 2026.
- Evidence: the dispositions that name the note are A's M2, B's MINOR 7, C's M1, M2, M4, m1 and m17; those of C's m3 and m4 do not name it.

**VT2-10 — note**
- Where: `CLAUDE.md` L71: "follows regional r₁ at +0.86, spin p < 0.0001".
- Problem: The older form of the p in T55 (iii) stays in a history bullet dated 15 Sep 2026. Every manuscript file has "p < 1/10,000".

**VT2-11 — note**
- Where: record L9266–9267 (B's W1): "S5 Table's note and S19 Table's row: p < 1/10,000, no rotation reaching the observed value".
- Problem: S19 Table's row (supplementary.md L1623) has "spin p < 1/10,000" without the second clause. Results 3, S3 Text §4 and S5 Table's note have both.

**VT2-12 — note**
- Where: record L9279–9281 (C's M2): "the Use of AI tools statement says the same as before in fewer words".
- Problem: The statement at HEAD speaks of "the two occasions on which a session computed on the data" (draft L257); the committed one described one. The second occasion is new content, which the same entry does state in its paragraph on the audits.

**VT2-13 — note**
- Where: supplementary.md L1726 (S20 Table, row 10) against `claims/claims_2026-10-01.md`, Gao et al. (2026).
- Problem: Beyond the two details R54 added, row 10 holds items the claim record does not: three phrases in quotation marks ("persistent synergy", "persistent redundancy", "the Gaussian MMI solver"), "246 × 246", the year in "following Luppi et al. 2022", and "the t-statistic pattern". Not checkable in the tree.

**VT2-14 — note**
- Where: `manuscript/main_text_numbers.csv`, 175 rows; for example L183 "anchor: @L10-26|| sts |", L1071 "anchor: @pct|| raw | 0.992", L401 "the line holds bound on 0.007568359375".
- Problem: As written, 170 anchors and 5 held strings are not on the lines named. They are once the prefixes "@La-b|" (169 rows), "@pct|" (1) and "bound on" (5) are read as the table's notation, which the head note does not explain. The notation is in the committed table at 8bd189e too.
- Evidence: own script `VW/VT2/nt_locators.py`: 1,073 rows with a line locator; with the prefixes stripped, 0 fail.

**VT2-15 — note**
- Where: S3_Text.md L266: "(a) TRs above the threshold per run (count, share of the run's 840 TRs, mean framewise displacement)".
- Problem: The heading can be read as T34's sentence was. The table's mean framewise displacement is the run's: subject 3 has no TR above the threshold and means of 0.068 and 0.094.
- Evidence: `censoring_tables.md` table (a), row 3; `notes/partB29_censoring.py` L85.

**VT2-16 — note**
- Where: S3_Text.md §6 table (L395–400) and supplementary.md S18 Table, B28 (L1592–1597): "slope: mean ± SD".
- Problem: These are the same SDs with divisor 100 as Table 3's, whose caption now says so; these two tables do not.

**VT2-17 — note**
- Where: supplementary.md L1706 (Part B row of `derived_r24.out`): "Results 3 and the Discussion (rtr's slope on regional r₁; the regional relation on the windowed estimator's own atoms)".
- Problem: Every section of the main text that quotes a number of `derived_r24.out` is named. The glosses miss one quotation: the Discussion's "cross-half r = 0.69" (draft L183), which the numbers table (CSV L1148) sources to `derived_r24.out` item 6. The regional relation on the windowed atoms is in Results 3 only.

## Status of each finding

- **T32** verified. S3 Text L3 has "(B1–B29, B16b, B16c, B17b)".
- **T33** verified. S3 Text L393; consistent with L406, S10 note L192, Methods L245 and `partB17_calibration.py` L141/145.
- **T34** verified (L264; the script takes the mean over all TRs). See VT2-15.
- **T35** verified against S14 Table and `lag_tables.md`.
- **T36** verified. Of the 29 outputs, 12 text files carry `git=13e7299`; 16 arrays and the pickle do not; all 29 match `outputs.sha256`.
- **T37** corrected in both places. See VT2-1 and VT2-2.
- **T38** verified, all four parts. The eight deviations in S5 Text §1 are the committed Methods list; 3 replaced, 2 withdrawn, 3 with nothing put in their place. S19 Table has no "weighting", "stationarity", "phase-randomised" or "withdrawn". The five cells (B4, B7, B17 (ii), B17b (i), B17b (ii)) name S5 Text §1. No pointer to "Methods, Pre-registration and deviations" remains in S19.
- **T39** verified. All 35 cells of Table 4 recomputed; +0.899 with its interval is in S3 Text §8.
- **T40** verified against `results/lz_vs_tdmi_*.csv`, S6 Table and S1 Text. S19's row now gives the placebo values too.
- **T41, T42, T43** verified.
- **T44** verified. The Abstract has 300 words by my count and by the check.
- **T45** verified. The seven phrases are gone from S20 Table and the literature file; the two counts stay in rows 2 and 3; row 5's last cell reads "not mentioned in the main text".
- **T46** verified, parts (i)–(vii). See VT2-14.
- **T47** corrected in Methods and S3 Text §5. See VT2-3 and VT2-4.
- **T48, T50, T52, T54** verified. No "@@" marker remains in any manuscript file; all 48 references are cited in the main text.
- **T49** verified. No "track" wording is left for the whitened correlations; seven of the eight cells' intervals include zero.
- **T51** verified. The three clauses are restored. Against 8bd189e, no other clause is lost: Varley's identity is in Results 1; "none … reports regional r₁" is in the Discussion; 0.97 and 32.8 are in S3 Text §10; "does not rank datasets" is in S3 Text §4.
- **T53** concerns no file of the commit. `apply_revision.out` does list 15 files after its summary line. What the prompts say cannot be checked in the tree.
- **T55** verified, (i)–(v). See VT2-10, VT2-11, VT2-12.
- **T56** verified. The record's list and CLAUDE.md's are identical word for word; S20 rows 5 and 10 carry no promise. See VT2-9.
- **T57** verified: the Part B row exists and the four cells read as stated. See VT2-8 and VT2-17.
- **T58** verified, (i)–(iii). See VT2-5.
- **T59** verified, (i)–(iii). See VT2-16.
- **T60** verified, (i)–(iii).
- **T61** (i) and (ii) verified. (iii): see VT2-6. Also VT2-7.
- **T62** verified. `matched_slope.csv` and its script are unchanged; README L42–44 reads as quoted.
- **T63** verified. The claim record has the Timmermann (2023) item and both Gao details. See VT2-13.

## Checked and found exact

- **Quotations.** Every phrase the dispositions of T32–T63, and the R dispositions they point to, put in quotation marks was searched in the tree. All occur word for word in the file named, except the two of VT2-1 and VT2-5.
- **Table 4** (own script, from the three pickles):
  - r₁: 0.847926, 0.750611, 0.262547, 0.136827, 0.052358.
  - Levels, DiDs, inverted sign-flip intervals (my own inversion) and exact p: all as printed.
  - r: +0.952810, +0.898873, +0.495364, +0.444867, +0.332750.
  - Power shares as `whitened_spectrum_tables.md` gives them.
  - Results 7's 18 % (17.63 %) and 7 % (7.00 %).
  - The caption's definitions cover the raw row.
- **Fisher-z intervals at N = 14:** [+0.704, +0.968], [−0.048, +0.812], [−0.112, +0.789], [−0.240, +0.734], as in S3 Text §8 and `derived_r24.out` item 6.
- **Table 3** (from the pickles and `matched_slope.csv`):
  - Data: −0.7533 [−1.1331, −0.3735], r −0.7802.
  - One left out: −0.7914 to −0.6991; counts 0, 0, 11, 11.
  - Two left out: −0.9059 to −0.6423; counts 1, 13, 71, 63.
  - Without subject 8, 14, both: intervals on 11, 11 and 10 df, as printed.
  - Generator rows: SDs with divisor 100 (0.0912, 0.0964, 0.0874, 0.0943); steepest replicate −0.596.
- **Sensitivity and rates:** SE 0.00511; detectable difference 0.01550; excesses 0.0088, 0.0066, 0.0061; Fieller g 0.6106, intervals [4.45, 10.54] and [−1.60, −0.08]; FD shares 0.197 and 0.163.
- **Numbers table** (own scripts):
  - 1,378 rows. All 1,073 line locators hold their anchor and held string (see VT2-14).
  - All 786 data rows equal their held string at the printed precision, with no tie.
  - Every row's context is in the main text, on a distinct token, in reading order.
  - No uncovered number token other than citation years, cross-references, dates, commit identifiers, the DOI, code spans and headings.
  - 33 rows of N = 14 point to record L48; the 13 anchors hold 0.1075, 0.2183, 0.2507 and −0.7533; the Discussion's 0.003 holds +0.0027.
  - The head note says "the four table captions and bodies".
  - The repository's `check_numbers.py`, run read-only, reproduces `check_numbers_revision.out`.
- **S3 Text transcriptions:** the tables of B27 (a), (b), B29 (a), (b) and B28, and S18's B28 table, equal the result files cell by cell.
- **S19 Table:** 81 rows; 36 met, 15 partly met, 16 missed, 14 not counted.
- **The Discussion's statements on cited works** ("The fall of r₁ under DMT") are each in the claim record.
- **Rules of the text:** no computation label in the main text before "## Supporting information"; no round, stage or bundle name and no reviewer's letter in the manuscript files; session names only in S5 Text §5.
- **Figure captions:** the script's six caption templates match the main text's captions in every literal part (static comparison; nothing was run).
- **Not checkable in the tree:** what the audit and writer's prompts say (R44), the packaging check (R01) and the planning session's two uncommitted checks (R09).
