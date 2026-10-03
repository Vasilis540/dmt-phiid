REPORT OF VERIFIER VS — supporting information and literature file (HEAD 9caa60b against 8bd189e)

Root (absolute): VT = $SP/r24/vtree
Files verified:
- $SP/r24/vtree/manuscript/si/S1_Text.md, S3_Text.md, S4_Text.md, S5_Text.md
- $SP/r24/vtree/manuscript/supplementary.md
- $SP/r24/vtree/notes/partB5_literature_v2.md
Checked against (all under VT): manuscript/draft_v2.md at HEAD, manuscript/analysis_record.md, notes/review_results/ (partB/baseline_gap*, matched_slope*, censoring*, prewhiten_fixed*, prewhiten_tables.md, regional_sts_r1*, inference_rows_prewhiten*.csv/.pkl, regional/regional_atoms_raw_ts_gsr_win60.npy), results/lz_vs_tdmi_*.csv, notes/review_2026-10-01_cold_reads/ (checks/derived_r24.out and .py, b27/, pubmed_search/, claims/claims_2026-10-01.md, audit/, reviews/), notes/partB_prespec_2026-09-14.md, notes/partB16c/B27/B28/B29 scripts, tests/, .github/workflows/tests.yml, git log.
Nothing under VT was changed; scratch only in $SP/r24/vwork/VS. No internet, no subject data (recomputations used committed result files only).

RESULT IN ONE LINE: no wrong number, verdict or count found in the changed passages; 7 findings graded inexact (2 dates, 3 pointers/statements in S19/S18, 2 cells of S4 Text) and 5 notes.

FINDINGS

VS-1 — inexact
Where: S3_Text.md §5, line 231: 'Record, "The pre-injection gap and the per-subject relations (B27): pre-run entry" and "B27, outcome" (1 October 2026)'; same form at line 264 (B29) and §6 line 393 (B28).
Problem: one date follows two entries; the outcome entries are of 2 October 2026.
Evidence: analysis_record.md headings, lines 8575, 8671, 8757 ("… pre-run entry, 1 Oct 2026 18:50 UTC") and 8875, 8968, 9028 ("B27, outcome, 2 Oct 2026 18:40 UTC"; B28, B29 likewise). supplementary.md gives the pair as "1–2 Oct 2026" (line 256, S11 source; line 1590, S18 B28 source).

VS-2 — inexact
Where: S3_Text.md §8, line 527: "The atoms at fixed orders p = 10 and p = 20 were computed on 1–2 October 2026 (B16c;"
Problem: the same run is dated 1 October elsewhere: S5_Text.md §4, line 25, "B27, B28, B29 and B16c were run on 1 Oct 2026 at 13e7299 in one root unit" (UTC times), and draft_v2.md line 267, "the runs of 29 September and 1 October 2026, at d5a65bd and 13e7299".
Evidence: b27/evidence.txt and b27_unit.log lines 156, 686: B16c started 2026-10-02 00:01:08 local, "done (2040s)" = 21:01:08–21:35:08 UTC on 1 October; wholly 1 October in UTC, wholly 2 October in local time.

VS-3 — inexact (pointer)
Where: supplementary.md, S19 Table, line 1664, row "B24, the pure-autocorrelation expectations": "| partly met (D missed) | Results 4; S3 Text §6 (its residual table); S18 Table |"
Problem: Results 4 at HEAD carries none of the row's values (A_other +0.00001, A_same, B, D, Sym). The sentence that did ("against +0.0000 ± 0.0003 under a pure autocorrelation change on the band-passed generator") was in Results 4 at 8bd189e and is now only in S3 Text §6 (line 341). Of B24, Results 4 keeps only the rate −0.18, which comes from the row above (the check against B17b).
Evidence: draft_v2.md lines 120–142 at HEAD (A_other appears once, line 142, without an expectation); `git show 8bd189e:manuscript/draft_v2.md` line 136.

VS-4 — inexact (pointers)
Where: supplementary.md, S19 Table, line 1675, row B28 (a): "band-passed step: slope −0.200 against ratio −0.167; AR(1) step: −0.355 against −0.349 | met | Results 4; S3 Text §6; S18 Table |"; line 1678, row B28 (d): "shares of replicates with r at or below the data's 0.190, 0.070, 0.370, 0.280; … | no prediction | S3 Text §6; S18 Table |"
Problem: (a) Results 4 and the main text's Table 3 give the slopes but neither the per-replicate ratios of means (−0.167, −0.349) nor the comparison; the ratios Results 4 names are −0.18, −0.39, −0.37 of other computations (against −0.39 the AR(1) slope −0.355 is the less negative). (d) S18 Table's B28 part has no column for the share of r; it has the sts DiDs and the coverage only.
Evidence: draft_v2.md lines 124–139; supplementary.md line 1592 (S18 header: 11 columns, none for r shares); S3_Text.md line 395 (the 14-column table has it).

VS-5 — inexact
Where: S4_Text.md, R1, line 62: "Contrasts of the data are given as mean DiDs with inverted sign-flip 95 % intervals and exact p (Table 2; Results 2–6; intervals without p in the data rows of the residual table of S3 Text §6)."
Problem: Table 2 at HEAD has two rows that are neither and are not among the exceptions the cell then lists: "Baseline-adjusted contrast" and "r₁, baseline-adjusted contrast", regression intercepts with t intervals (12 df) and no p, also quoted in Results 2 and the Abstract.
Evidence: draft_v2.md line 89 (Table 2's caption: "the intercept of the regression … with its t interval (12 df)"), lines 99 and 102.

VS-6 — inexact (unchanged cell against the revised Methods)
Where: S4_Text.md, S6, line 53: "every post hoc or review computation is labelled at first mention."
Problem: Methods at HEAD says the text labels five named computations and S19 Table covers the rest; other post hoc computations have an unlabelled first mention, e.g. the finite-sample null (a review computation by S19 Part B, line 1696, and by S4's own S9 cell, line 56), first named in Results 1.
Evidence: draft_v2.md line 241 ("S19 Table says of each computation whether it had a recorded prediction or was post hoc (the text says so for …)"); line 59 ("a stationary finite-sample null, in which those values hold in population, reproduces most of its level", no label).

VS-7 — inexact
Where: supplementary.md, S18 Table, B28 part, line 1590: "No data but the subjects' whole-brain r₁ DiDs, which set each simulated subject's change"
Problem: the script reads two further saved quantities derived from the data: the per-subject residual DiDs (for the data's slope, which the same paragraph quotes) and B17's pool of the data's window-level pair q.
Evidence: notes/partB28_matched_slope.py lines 3–4 ("reads the saved per-subject r₁ and residual DiDs and B17's pool of q"), 77, 98–99; analysis_record.md lines 8673–8676.

VS-8 — note
Where: S3_Text.md §6, line 393: "the methods and statistical reviewers' cold reads of 1 October 2026 (S5 Text §5) asked for the slope the generators themselves give when each simulated subject's change is the data's"; §8, line 527: "after the methods and statistical reviewers' cold reads of 1 October 2026 (S5 Text §5) asked what whitening harder leaves".
Problem: in both cases only the statistical reviewer's report asks for the computation; the methods reviewer's items raise the neighbouring point and ask for neither.
Evidence: reviews/read_B.md MAJOR 3 (lines 23–24: "The like-for-like comparison is the per-subject OLS slope computed inside generator replicates with heterogeneous Δa") and MINOR 4 (line 37: "Compute the atoms there."); reviews/read_A.md M1 (line 20: "the per-subject slope comparison is the right test", plus a within-window non-stationarity control) and m4 (line 32: "Prewhitening is presented one-sidedly"). The record's pre-run entries name both reads as the question's origin (lines 8678, 8821).

VS-9 — note (pointers that hold in part)
Where: supplementary.md, S19 Table, line 1641 (B17b): 'Level 1.1883; sts DiD −0.0940 ± 0.0028: "met, and better than predicted" | met | Results 2 and 4;'; line 1672 (B27 (b)): "r = −0.874; adjusted contrast −0.0110 [−0.0170, −0.0050] | met | Results 2; S3 Text §5 |"; line 1673 (B27 (c)): "+0.922 and +0.939 | met | Results 2; S3 Text §5 |".
Problem: B17b: at HEAD Results 2 keeps only the rate ("the band-passed generator's 6.1 (S13 Table)"), Results 4 neither the level nor the sts DiD; the DiD (as −0.094) is now in the Abstract and the Discussion, which the cell does not name. B27 (b), (c): Results 2 gives −0.0110 and +0.939; r = −0.874 and +0.922 are in S3 Text §5 only.
Evidence: draft_v2.md lines 15, 106, 108, 183; no "0.874" or "0.922" in draft_v2.md.

VS-10 — note
Where: S5_Text.md §4, line 27: "quotes what it computed there: the mean per-subject regional slope (2.644997), the mean pair r₁ DiD (−0.015468) and the data's slope of the residual DiD on the pair r₁ DiD (−0.861 [−1.299, −0.422])".
Problem: the findings file quotes further values from the same computations on the released series: mean r² 0.576258 (T07), r = −0.777 (T10), whole-brain r₁ DiD −0.014645, residual DiD +0.011534 and the ratio −0.7457 (T25). None of them, and none of the three listed, occurs elsewhere in the manuscript files (checked by search), so "The paper uses none" holds.
Evidence: audit/findings_text.md lines 78–82, 96–100, 186–190.

VS-11 — note
Where: supplementary.md, S19 Table, line 1682 (B29 (d)): "the non-finite TR is subject 3's placebo run's TR 839 and no other | confirmed: (3, placebo, 839);"; S3_Text.md line 299: "(d) the non-finite TR is subject 3's placebo run's TR 839 and no other: confirmed."
Problem: the check read ts_gsr only; the record's outcome and the main text say so, these two places do not (S3 Text §5 (e), line 297, does).
Evidence: notes/partB29_censoring.py line 123; analysis_record.md line 9053 ("confirmed on ts_gsr, the variant the script reads for this check"); draft_v2.md line 213 ("on ts_gsr the only one").

VS-12 — note (a result file, not the text)
Where: S3_Text.md §5, table (a), row r₁ / ts_demean / 60: "+0.0054 [−0.0031, +0.0136] | 0.1871; 9/14" (also main text Table 2).
Problem: the text equals the run's table, but the value is not reproducible from the committed per-subject CSV: from baseline_gap.csv (six decimals) the exact sign-flip p is 3,068/16,384 = 0.1873. Twelve assignments lie within 2 × 10⁻⁶ of the observed mean, so the CSV's rounding accounts for it. Every other cell of (a), (b), (c) reproduces.
Evidence: my recomputation with the script's signflip_p rule on notes/review_results/partB/baseline_gap.csv; baseline_gap_tables.md row "r1 | ts_demean | 60".

CHECKED AND FOUND EXACT

S3 Text
- Line 3: "(B1–B29, B16b, B16c, B17b)" = the scripts in notes/. Opening statement that the main text carries no path, commit id or timestamp outside Data and code availability and References: true at HEAD (search).
- §2 "Other Gaussian PIDs": verbatim the sentence removed from Limitations of 8bd189e; Limitations at HEAD has the clause and points to S3 Text §2.
- §3 transfer entropies: the partial correlation is zero on the family; te_filter_check.py run in scratch gives 0.90/0.70, innovation correlation 0.3, filter 1 + 0.6L + 0.3L², lag-1 TEs 0 before, 0.001508 and 0.000408 after (0.0015, 0.0004), 0.000000 on ten lags, 0 on the symmetric family; page locators equal the claim record; the corrections of audit findings C01 and C19 are in the text; pointer "main text, Results 1 and 7" holds.
- §4: changed heading and first sentence; "spin p < 1/10,000 … no rotation reaching the observed value" (source prints 0.0000 over 2 × 10,000 rotations); the windowed-atoms paragraph recomputed by me from regional_atoms_raw_ts_gsr_win60.npy and regional_sts_r1.csv and equal to derived_r24.out item 7: shape 14 × 2 × 14 × 115 × 16; 1.1554 / 1.1378; +0.898, +0.868, +0.850, +2.30; +0.863, +0.835, +0.807, +3.09; +0.686, +0.673, +0.541, +0.51; "2 October 2026" (items 5–8 added after the audits, derived_r24.py docstring); audit finding T07 did point to the array.
- §5 B27: tables (a) 12 rows × 13 cells, (b) 3 rows × 10 cells and paragraph (c) equal baseline_gap_tables.md and were recomputed from baseline_gap.csv (but for VS-12). "What the tables say": −0.888, r² 0.79, SDs 0.0887 / 0.0485 / 0.0524 (item 2); subject 14; the adjusted contrast the smallest of the three in all nine rows of sts, r₁ and substituted sts; 4.263, 4.139 to 4.535 (item 8); r₁ gaps; −0.844, +0.824, −0.735, +0.914, +0.922, +0.939; every verdict re-derived from the pre-run entry's criteria ((a), (b), (c) met on ts_gsr W = 60, ts_demean and W = 30) and equal to "B27, outcome" and S19. Main text Table 2, Table 3, Results 2 and 4 carry the same values.
- §5 B29: (a) 14 subject rows and the mean row, (b) 2 rows, (c), (d) (56 window entries), (e) equal censoring_tables.md and were recomputed from censoring.csv. Prose: 23.6 (0.028), 10.1 (0.012), +1.12 (0.2166; 7/14), +0.0143 (0.2452; 8/14), −0.107, −0.363, −0.124, −0.025, 137 of 392; subject 8: 24 (0.029), 0.120, 6, +2.25, +0.0935 (the largest of 14); subject 14: 2, 4, −0.08. Verdicts (a) partly met, (b) missed, (c) no sign prediction = record and S19. Limitations and Methods (Dataset) agree.
- §6: line 303 (three statements, 0.218 and −0.051 in Results 4, −0.1130 in Table 1); line 305 quotation verbatim in notes/partB_prespec_2026-09-14.md line 23. Residual table: its 13 table lines and the caption's body (2,454 characters) are identical to Table 3 of 8bd189e; only the bold heading differs. Pointer rewordings at lines 339, 341, 432 right. B28: every parameter (185.4, 0.2637, 0.8628, 0.2828, N(0.85, 0.0125²) = SD 0.0125 in the script, the 14 Δa_s, the 14 β̄_s, floor −0.0375, subject 8, 100 replicates, −0.753 [−1.133, −0.373], −0.780, −0.788) and the table (4 rows × 14 cells) equal matched_slope_tables.md; recomputed from matched_slope.csv (SD with divisor 100, percentiles, shares 0.000; steepest replicate slopes −0.442, −0.488, −0.566, −0.596); CSV field counts 10 / 11 as stated; 0.0001 and 0.0006 = item 5 (cells differ by 0.0002, 0.0007); verdicts (a), (b), (c) met, (d) none = record and S19.
- §8: line 525; B16c table (8 rows × 11 cells) equals prewhiten_fixed_tables.md, the CSV and item 1. Prose: 1.155 / 0.718 / 0.220 / 0.087 / 0.072; −0.0809 / −0.0620 / −0.0262 / −0.0191 / −0.0127; +0.445, +0.333, +0.495, +0.899 with the four Fisher-z intervals of item 6; ordering in four of four cells; diagnostic 0.0861 / 0.0296 / +0.0564 and 0.0705 / 0.0080 / +0.0624, −0.0091 (11/14), −0.0090 (12/14), −0.0037; 51.2 %, 59.7 %; 18 % and 7.0 %; −0.0733, −0.0927, −0.0146; −0.079 to +0.570 with seven of eight intervals including zero (critical |r| 0.5306); the diagnostic's levels are means over runs and windows (script line 184); verdicts = record and S19. Costs paragraph = the old Results 7 sentence with 41.8 % and the page locator of the claim record. Main text Results 7 and Table 4 agree (0.263 from 0.262547, 0.137 from 0.136827 in the CSVs).
- §9: the moved sentence is verbatim the old Results 7 sentence and gone from the main text; lag sentence (0.0262, 0.0415, −0.202) = Results 5 and S14 Table.
- §10: both PubMed strings character for character (318 and 526 characters); 11 and 2 records; screening 6 + 4 + 1, three not returned; the ten studies; Liardi et al.'s six authors (four of the ΦID paper's seven); +32.8 / +0.06 recomputed from the closed form; pointers to Methods (Literature search), Discussion, Results 3, Results 7, Table 1 (−0.0078, −0.0086).
- §11: the Rosas et al. sentence = the claim record (with audit finding C15's correction).

supplementary.md
- S5 Table note (line 101) against regional_sts_r1_tables.md. S11: source; 24 new rows (levels, DiDs, inverted intervals, p, counts) against the CSV and item 1; note (line 331). S12 note (the Results' opening paragraph does define the estimate). S13 note. S18: title; B28 part, 4 rows × 11 cells.
- S19 Part A: 17 new rows — criteria = pre-run entries, values = result tables, verdicts = outcome entries, date "1 Oct 2026, 18:50 UTC". Recount: 81 rows = 36 met + 15 partly met + 16 missed (67) + 14 others (seven rule or no-prediction entries; B25 (d); B28 (d), B29 (c), B16c (e); B27 (d), B29 (d), B16c (a)); 56 + 11 from the new rows (+8, +1, +2); the main text has the same counts. EEG row: −0.047 / 0.221, −0.093 / 0.045 = results/lz_vs_tdmi_*.csv. Every changed "reported at" cell read against HEAD (B4, B7, B17 (i), (ii), B17b (i), (ii), B22 (a), B23 (a1)–(a5), (b), B24 check, B25 (a), (b), (d), B26, and the new rows) holds but for VS-3, VS-4, VS-9. Part B: the derived_r24 row item by item and place by place; the finite-sample null row (row 5 of the residual table; Results 1 and 4); the review-computations row (Results 2, 4, 6, 7); the residual's-source row.
- S20: head note; the seven removals (rows 1, 2, 3, 4, 6, 8, 12); rows 2, 3, 5; row 10 item by item against the claim record, r₁ 0.82 recomputed (0.817); renumbering to 11, 12; every numbered row reference elsewhere (S3 Text lines 554, 560; S19 row B25 (d); line 1742; Table B items 2 and 4) still right.

notes/partB5_literature_v2.md: Table A's 12 rows × 10 cells equal S20 Table A except three cells that differ only by computation labels (row 2, row 11, row 12); header identical; the search paragraph = screening.md; the last paragraph (every work it names is cited and listed in the main text).

S1 Text: the three changed lines against the claim record (single-blind, who was blind, order of preprocessing steps, six of twenty and four plus three, ratings in the second session); −0.0468 (0.2208), −0.0926 (0.0450); the record entry "Git history and the participant codes" (15 Sep 2026) exists; pointers (Results 2, Discussion, Limitations, S3 Text §5); the ratings enter exactly one main-text statement.

S4 Text: changed cells against the claim record and the citation audit (corrections of C03, C08, C09, C20 present); every pointer of the D, A, P, S, R, Sh cells into Methods, Results, Limitations, Data and code availability read at HEAD (holds but for VS-5, VS-6); both quotations of Limitations exact; S17 Table has 932 rows.

S5 Text: §1 the eight deviations = the list removed from Methods, verbatim; 3 + 2 + 3; S19 has no row for the second null, the weighting rule or the withdrawn reading. §4 run sentence, every item against evidence.txt, b27_unit.log, b27_heartbeat.log (11 lines, disconnected from 23:57), b27_start.sh, b27_commit.sh; 29 sha256 OK; 0 tracebacks; 7 / 1,428 / 1 / 2,040 s. Audit paragraph: the three values. Details paragraph: tests/, tests.yml, the tool's NaN, figure names, 8 / 475 / 225 min. §5: 70 = 20 + 19 + 31; 145 = 63 + 57 + 25, all in dispositions_revision.md; seven works added to the reference list (41 to 48 entries), each marked as read on 1 October 2026. §6: 71cf932, 24919ea, 13e7299 (1 Oct), 8bd189e (2 Oct), HEAD's parent 8bd189e.

Rules: no round, stage or bundle name in the manuscript files (the only such strings are in the file names derived_r17…, derived_r24…; "stage" occurs in a paper's title and in "data-release stage"); no reviewer letter; session names only in S5 Text line 33; this revision's moves are dated "the revision of 1–2 October 2026" at every place (S3 lines 106, 303, 319, 321, 542, 546; S5 lines 9, 29; S20 head note); no computation label in the main text before "## Supporting information".

Pointer sweep: every occurrence of "Table 1–4", "Results 2/3/4/6/7", "Discussion", "Limitations", "Data and code availability", "Abstract" and the main text's "Methods" in S1–S5 Text and supplementary.md was read against HEAD; no stale "Table 3" remains (only historical mentions).

Not verifiable here: the cited papers are not in the tree, so statements about them were checked against the claim record and the citation audit only; "each subject's own order is not among the released files" was checked against the record only.
