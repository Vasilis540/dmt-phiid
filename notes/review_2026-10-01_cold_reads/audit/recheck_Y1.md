# Y1 — S19 Table: Part B read against the whole paper, the changed cells of Part A, and the head note

Tree: VT at HEAD (clean), compared with `checked3` and with 8bd189e. Line numbers are those of HEAD. MT =
`manuscript/draft_v2.md`; S1 … S5 = `manuscript/si/S1_Text.md` … `S5_Text.md`; SUP = `manuscript/supplementary.md`;
CSV = `manuscript/main_text_numbers.csv` (file lines; line 1 its head note, line 2 its column names); REC =
`manuscript/analysis_record.md`; DISP = `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`; PB =
`notes/review_2026-10-01_cold_reads/audit/partB_reading.md`; X1 = `notes/review_2026-10-01_cold_reads/audit/recheck_X1.md`.
S19 Table is SUP lines 1599–1712: head note 1601, Part A rows 1607–1687, Part B rows 1695–1712.

Twelve findings: 0 errors, 7 inexact, 5 notes. No number, date, time, count or quotation in the cells that changed
between `checked3` and HEAD, in the five new rows of Part B or in S2 Text's new sentence was found wrong. What was
found inexact: the rule that the head note now states for Part A, which the cells do not follow outside the main
text's values (Y1-1, Y1-2), with the disposition that says no place is missing (Y1-3); one clause of the head note on
S17 Table (Y1-4); one file named for more than it holds in a new row of Part B (Y1-5); and two statements of the
dispositions' closing section (Y1-6, Y1-7).

## Findings

**Y1-1**
- Where: SUP, S19 Table, head note (line 1601): "In Part A the last column names the places of the paper that give the
  row's outcome, by a value of the outcome, by a number derived from one, or in words"; the last cells of the fourteen
  rows listed under Evidence (none of them changed between `checked3` and HEAD).
- Problem: The rule is stated for "the places of the paper", with no exception. In fourteen rows a supporting text or a
  supporting table prints a value of the row's outcome cell, or a number derived from one, as that quantity, and the
  row's cell does not name it. The reading that completed the cells was of the main text (DISP, the disposition of
  W3-4, lines 1954–1956), and the third check searched the outcome values in the main text only (Y1-3).
- Evidence (row; its cell; the place not named, with the line and the words):
  - Line 1611, the W = 30 positive control; cell "S1 Text (in summary); Results 2 (the W = 30 contrast)". S1 Table
    (SUP line 17): "W = 30 positive control (`results/primary_b_ts_gsr_win30.csv`, git ac1fdc0), ts_gsr, pre = bins
    1–8: primary post bins 11–28, DiD raw −0.0686 [−0.1142, −0.0242], p = 0.0042"; S12 Table (SUP line 340, row "ts_gsr,
    W = 30", observed DiD −0.0686); S3 Text §5 (S3 line 245, B27's table (a), row "sts | ts_gsr | 30": "−0.0686
    [−0.1142, −0.0242] | 0.0042").
  - Line 1613, the redundancy prediction; cell "S1 Text; Table 1 (the rtr DiD at W = 60)". S3 Text §1 (S3 line 82: "|
    rtr | +0.0388 | −0.0078 (10) |", the same DiD); S3 Text §10 (S3 line 560: "On this dataset synergy and redundancy
    both fell under DMT: rtr by 0.0078").
  - Line 1618, B3; cell "Results 5; Fig 6; S3 Text §9; S14 Table". S3 Text §5 (S3 lines 213–215, the rows "sts tau2",
    "sts tau3" and "sts tau5": −0.0429, −0.0043 and −0.0024 with their p and intervals).
  - Line 1619, B4; cell "Abstract; Results 4; Discussion; Tables 1 and 3; Figs 2, 3 and 5; S3 Text §6 (its residual
    table); S12 Table; S5 Text §1 (the deviations)". S3 Text §5 (S3 line 203: "diag residual sts ts_gsr W60 [primary] |
    +0.0115 | 0.0421 | [+0.0021, +0.0211]" with "[+0.0005, +0.0226]" in the last column, the two intervals of the
    outcome cell; line 240; line 254, r = −0.780; line 258, "the data's residual DiD, +0.0115"); S13 Table (SUP line
    363: "−0.74 in the data (+0.0115 for −0.0155"); S5 Text §2 (S5 line 15: "the residual DiD, 0.042").
  - Line 1623, the regional sts–r₁ test; cell "Abstract; Results 3; S3 Text §4; Fig 4". S5 Table (SUP line 101): "sts
    against windowed regional r₁, Spearman ρ = +0.771 on the 99 cortical parcels, spin p < 1/10,000".
  - Lines 1631 and 1642, B17 (i) and B17b (i); cells "Results 4; Discussion; Fig 5; S3 Text §6 (its residual table)
    and §7; S10 Table", the second with "S5 Text §1 (the deviations)". S12 Table (SUP line 345): "+0.0027 ± 0.0014
    (band-passed generator, B17b; p = 0.108); +0.0049 ± 0.0017 (AR(1) pairs, B17; p = 0.218)"; S3 Text §5 (S3 line 258):
    "exceeds the three expectations (+0.0027, +0.0049, +0.0054) by +0.0088, +0.0066 and +0.0061".
  - Line 1645, B17b, the population reference for B17; cell "S3 Text §7; S13 Table". S10 Table (SUP lines 248 and
    250): "| (i) | 1.1936 | 1.1121 | −0.0816 |" and "| (iv) − (i), pre level | −0.0463 |"; S13 Table does not print
    the −0.0463.
  - Line 1651, B22 (d); cell "Abstract; Results 1; Discussion; S3 Text §4". S3 Text §3 (S3 line 120): "B22 (d) replaces
    them with the within-window SDs of pair r₁ and pair |q| (0.0284 and 0.1957, a per-SD ratio of 4.66 at the family's
    derivatives; 3.28 with each pair averaged over subjects and windows first"; S3 Text §11 (S3 line 568): "against 4.7
    for the Gaussian atom".
  - Line 1658, B23 (b); cell "S18 Table; S3 Text §6 (its residual table); Results 4, Table 3 and Fig 3 (the AR(1)
    pairs' rate, −0.39, from its condition (i))". S13 Table (SUP line 363): "−0.39 on AR(1) pairs (B23 (b) (i))"; S3
    Text §5 (S3 line 258): "11 contain −0.39 (the AR(1) generator's)".
  - Line 1661, B23 (e); cell "S13 and S18 Tables". S3 Text §7 (S3 line 462): "Δr₁ = −0.01629 (0.8678 → 0.8515) and
    Δsts = −0.11263 (1.3795 → 1.2669; B23 (e))"; S10 Table (SUP line 252): "Δr₁ = −0.01629 and Δsts = −0.11263 (B23
    (e); S13 Table)".
  - Line 1663, B24, the check against B17b; cell "Abstract and Discussion (the sts DiD, −0.094); Results 2 and 4,
    Table 3 and Fig 3 (the rates per unit of pair r₁, 6.1 and −0.18); S3 Text §6 (its residual table); S13 and S18
    Tables". S3 Text §7 (S3 line 462): "sts falls by 6.13 per unit of pair r₁ on the band-passed generator (B24:
    −0.09441 for −0.01540)"; S3 Text §5 (S3 line 258): "0 contain −0.18 (the band-passed generator's rate)".
  - Line 1670, B26; cell "Table 1; Methods, The AR(1)-substituted estimate and its calibration; S3 Text §6". S12 Table
    (SUP line 335): "(S3 Text §6; B26): 4 of the 2,569,560 at W = 60 on each variant, 1,617 (ts_gsr) and 1,661
    (ts_demean) of the 5,139,120 at W = 30".
  - Line 1686, B16c (d); cell "Results 7; Table 4; S3 Text §8". S11 Table (SUP line 331): "the per-subject correlation
    of the MMI-sts DiD with the whitened r₁ DiD is +0.445 and +0.333 against +0.495 at p ≤ 5 (S3 Text §8)".
  - S17 Table. The head note sets S17 Table aside for the second column of Part B, not for Part A; in Part A it is
    named in the cells of B19 (d) and B21 (a) only. It prints the outcome values of other rows too, for example its
    rows 229 (B4: +0.01153, [+0.00214, +0.02107], [+0.00047, +0.02265]), 313 (B3 at τ = 2), 361 (B16) and 697 (the
    W = 30 control: −0.06863, 0.0042).
- Grade: inexact

**Y1-2**
- Where: SUP, S19 Table, head note (line 1601), the same sentence: "… or in words"; the last cells of the rows listed
  under Evidence, three of them cells that changed between `checked3` and HEAD (lines 1622, 1625, 1684).
- Problem: Places that state a row's outcome in words, with no value of it, are named in some cells ("Limitations (in
  words)", lines 1632 and 1643; "Results 4 (in words)", line 1648; S3 Text §6 with "(in words: a signed mean cancels on
  ts_gsr)" and "(in words: the window-sign statistic superseded)", lines 1622 and 1625) and are not named in the cells
  below, although the place states the outcome.
- Evidence:
  - Results 4, third paragraph (MT line 142): "on AR(1) pairs it rises, falls or moves with the sign of q according to
    the construction, and a weakening of a slow component shared by the two regions raises it in proportion to the fall
    of r₁". These are the outcomes of B23 (a1) ("positive for either sign"), (a2), (a4) ("Negative for either sign") and
    (a5) ("Rises"); their cells (lines 1653, 1654, 1656, 1657) read "S18 Table; S3 Text §6 (its residual table)". The
    cell of B22 (a) (line 1648) names Results 4 "(in words)" for the parenthesis that closes the same sentence.
  - Abstract (MT line 15): "Under the common-change-in-surprisal (CCS) redundancy function the atom is near zero and, on
    the family, nearly flat in r₁; prewhitening removes r₁ only at orders leaving mostly stop-band residue, where a
    smaller contrast remains". The outcomes of B2 (line 1617, "CCS-sts small"), B23 (c) (line 1659, "flatter than
    predicted"), B16b (line 1640) and B16c (c) (line 1685); none of the four cells names the Abstract.
  - Discussion, What the finding is and is not (MT line 181): "with unequal coefficients it falls below that sum, the
    pattern the data's atom table shows (Results 1)": B14 (line 1628; cell "Results 1; Table 1; S3 Text §1; Fig 2").
    MT line 183: "the regional map follows regional r₁": the regional sts–r₁ test (line 1623; cell "Abstract; Results
    3; S3 Text §4; Fig 4").
  - Discussion, Recommendations (MT line 197): "the prewhitening orders that remove r₁ leave mostly stop-band residue,
    with a lower level and a smaller contrast (Results 7)": B16b (line 1640), B16c (b) (line 1684, a changed cell:
    "Table 4; S11 Table; S3 Text §8; Results 7 (the level at p = 20 only as the base of a share, 18 %)") and B16c (c)
    (line 1685).
  - Methods, Redundancy functions (MT line 221): "phyid applies a different fifth condition (S3 Text). The prewhitened
    CCS values of S11 Table, and those S3 Text, S17 and S19 Tables label as phyid's, use phyid's mask; every other one
    uses the published definition." B6's outcome is "The two definitions differ … every CCS value is the
    published-definition value" (line 1620; cell "S3 Text §1–2").
  - S5 Text §1 (S5 line 7): "a fifth review found that a signed mean cannot test the mechanism, since pairs of opposite
    q cancel": the run-level mean cross-lag deviation (line 1622, a changed cell, which counts the same statement of S3
    Text §6 as "in words: a signed mean cancels on ts_gsr"). The same line: "Its W = 60 and finite-sample-null values
    (16 September, 10:23 and 10:32 UTC) took the sign from each window and read the null at the wrong q̂ density; a
    correction note (16:24 UTC) records the defects", then "the budget … replaces those readings. The superseded values
    are in S9 Table.": the outcome of the W = 60 statistic and the null (line 1625, a changed cell), more fully than S3
    Text §6 has it.
  - S5 Text §4 (S5 line 25): "of the 96 committed files whose bytes it changed, 46 differ only in the commit and the
    times, and every change of the other 50 traces to the matrices the run counts": B26 (line 1670).
  - The opening note of the supporting tables (SUP line 3): "reproduced the committed values under the rule of its
    pre-run entry, apart from two arrays of B2" and "every change of them tracing to the matrices it counts": the final
    end-to-end run (line 1665; cell "Data and code availability; S5 Text §4") and B26 (line 1670).
- Grade: inexact

**Y1-3**
- Where: DISP, the disposition of X1-8 (lines 2353–2361): "By that rule the session found no place missing from a
  cell."; with it the disposition of W3-4 (lines 1954–1956): "completed with the places that print a value of the row's
  outcome or a number derived from one, or that state the outcome in words".
- Problem: The rule quoted there covers "the places of the paper" and outcomes given "in words". The session did not
  read the cells by that rule: it searched the outcome values in the main text only, and it did not treat places that
  state an outcome only in words as missing. Read by the rule, places are missing from cells (Y1-1, in the supporting
  information; Y1-2, in words, six of them in the main text, which the disposition of W3-4 says was read for them).
- Evidence: X1, lines 294–301: "Places that state an outcome only in words were not treated as missing from a cell."
  and "Every decimal number of the 81 outcome cells was searched, as printed and in each rounding down to two
  significant digits, in every paragraph, table and caption of the main text before "## Supporting information"".
- Grade: inexact

**Y1-4**
- Where: SUP, S19 Table, head note (line 1601): "it does not name S17 Table, which holds every saved per-subject
  quantity with its intervals"; the same words in DISP, closing section, point (1) (line 2524), and in the `new` text
  of replacement U09h.
- Problem: S17 Table holds the 932 quantities of B21's run. Per-subject quantities saved since are not in it: the 264
  rows of `notes/review_results/inference_rows_prewhiten_fixed.pkl` (B16c, 1 October 2026), each with the 14
  per-subject DiDs, whose inverted intervals the paper takes from `derived_r24.out`, item 1 (Results 7, Table 4, S11
  Table); and the per-subject values of `notes/review_results/partB/baseline_gap.csv` (B27) and `censoring.csv` (B29).
- Evidence: S17 Table's own note (SUP line 400): "All 932 quantities with a saved per-subject vector: the 738 rows of
  the eight `notes/review_results/inference_rows_*.pkl`". VT holds nine such files with 72, 72, 72, 72, 72, 264, 264,
  84 and 30 rows (1,002); S17's body (SUP lines 404–1337) has 738 rows of the group "pickle" and no row whose label
  holds "prewhiten_fixed", "ar10" or "ar20"; each row of the ninth file has a field `did_subjects` of length 14;
  `notes/review_2026-10-01_cold_reads/checks/derived_r24.out`, line 2: "1. B16c, inverted sign-flip 95 % intervals
  (notes/review_results/inference_rows_prewhiten_fixed.pkl, field did_subjects, primary set)".
- Grade: inexact

**Y1-5**
- Where: SUP line 1707 (a new row of Part B), first cell: "three entered with the check's pre-specification with no
  prediction (the deconvolved contrast at W = 30, the per-subject DiDs and the placebo run's series by window;
  `notes/review_results/inference_rows_w30.csv`)".
- Problem: The file named for the three items holds the first only.
- Evidence: `notes/review_results/inference_rows_w30.csv` has 30 rows: the six window sets of "PhiR_deconv ts_gsr
  W30", "PhiR_deconv ts_demean W30", "sts_deconv ts_gsr W30", "sts_deconv ts_demean W30" and "PhiR ts_gsr W30", each a
  whole-brain contrast at W = 30. The per-subject DiDs (W = 60) and the series by window are in the report itself,
  `notes/regional_phir_deconv_2026-09-14.md`, sections 3.2 and 3.3 (lines 181–218), and in
  `notes/review_results/logs/rev_phir_items.log` (its parts (2) and (3), from line 35 and line 55).
- Grade: inexact

**Y1-6**
- Where: DISP, closing section, last paragraph (lines 2556–2558): "arithmetic on printed values that an outcome entry
  or the text itself states (the conversion of the run-level departure to 44 % and 37 %; the Spearman–Brown ceilings; a
  closed-form share in S8 Table's note)".
- Problem: The conversion is not arithmetic on printed values. The residuals −0.0061 and −0.0051 that the departure
  +0.0034 "gives" (S3 Text §6, S3 line 315; S9 Table's note, SUP line 187) are evaluations of the family's sts with the
  cross-lag entries displaced, which the outcome entry states and no result file holds; only the two shares are
  arithmetic on them (0.0061 / 0.0137 and 0.0051 / 0.0137). The other two things named hold as described (2 × 0.72 /
  1.72 = 0.84 and 2 × 0.74 / 1.74 = 0.85; 6.07 / 6.13 = 0.99 and 1.2588 / 1.2820 = 0.98).
- Evidence: REC lines 3110–3112: "**Conversion to a residual on the family** (evaluated with
  `rev_phiid_fast.atoms_from_corr` on the symmetric AR(1) pair with both cross-lag entries displaced, as the script's
  family check does; stated here, not in a result file)"; the log of check C1 of the review of 17 September 2026
  (`notes/fresh_review_2026-09-17/checks/check_C1_residual_vs_null.log`), line 57: "operating point (0.85, 0.25): sts
  1.25883 -> 1.25278; change -0.00605 nats for delta_run = +0.00340".
- Grade: inexact

**Y1-7**
- Where: DISP, closing section, point (1) (lines 2525–2528), on what the rule takes of the report's kinds and what it
  leaves out: "those that state a result in words without naming the computation, the mentions in the history and the
  inventory of S5 Text, and the same number where the text or the numbers table gives another computation as its
  source".
- Problem: The sentence does not account for all that the report lists and the cells leave out.
  (i) Of the report's 22 places of the kind [H], 11 are not in S5 Text: the caption of Table 2 (PB line 37); Methods,
  Pre-registration and deviations, and Data and code availability (56, 57); S3 Text §6 and §7 (225, 357); S18 Table
  (84, 124, 361); S19 Table, Part A (85, 125, 229). One of these prints a value of a computation under its name: the
  prediction of B17b's first row (SUP line 1641), "The W = 60 sts level near the null's 1.18", which is the
  finite-sample null's pre-injection level and which no other place of the paper prints. The null's cell (line 1696)
  does not name S19 Table, Part A, a supporting table that the cell of `derived_r24.out` (line 1711) does name.
  (ii) Two places that the report marks [R] are left out for a reason the sentence does not give. For the two
  phase-randomised p of Table 2's body and for the "(1.155)" of Methods, The AR(1)-substituted estimate and its
  calibration, the numbers table gives the review computations' own file as the source, not another computation's; the
  report leaves them out as the pipeline's values that the review's file reproduces (PB lines 28, 38 and 54), and the
  cell of the review computations (line 1695) names neither place.
- Evidence: PB, the lines given; `notes/review_results/logs/review_v2_residual_null.log`, line 11: "DMT pre  : window
  a=0.8625 (SD 0.031) |q|=0.2803  obs sts=1.1835"; CSV lines 439, 446 and 1322 (source
  `notes/review_results/inference_rows_raw.csv`, lines 2 and 38); `results/primary_b_ts_gsr_win60.csv` holds the same
  0.0020 and 1.1554.
- Grade: inexact

**Y1-8**
- Where: SUP line 1707 (a new row of Part B), second cell: "S2 Text (the placebo run's share at W = 30, 56 %; the gap,
  the placebo run's slope and its decline from window 1 to window 4)".
- Problem: One place of the main text points to where the row's test of the pre-injection gap is reported, and the cell
  does not name it. Other cells name places that only point ("S1 Text (S7 Table cited)", line 1699; "Results 2 and S1
  Text (S8 Table cited)", line 1704; "S14 Table (its source line points to S3 Text §9)", line 1698). Whether the
  parenthesis of Results 2 is such a pointer is a matter of reading; it names the scrutiny and the text that holds it,
  not a file or a value.
- Evidence: Results 2 (MT line 87): "the runs' pre-injection gap, DMT minus placebo, +0.0176 (p = 0.2307), lies in the
  direction that enlarges the DiD (the scrutiny S2 Text applies to the deconvolved ΦR contrast)"; S2 Text (S2 line 9):
  "a pre-injection baseline gap in the direction that creates it (deconvolved −0.0124, p = 0.014; raw −0.0042, p =
  0.28)".
- Grade: note

**Y1-9**
- Where: SUP line 1700, the coupled family, second cell: "Results 1; Fig 1c; S3 Text §3; S18 Table (the family named in
  the rows of B23 (a3), whose values those are)".
- Problem: By the head note's rule S18 Table is not a place this column names: it prints no value of B8, does not name
  B8 as a source and does not point to where B8 is reported, as the gloss itself says. The disposition says that it "is
  kept with what it holds". Other places that name the family in the same way are not named: S3 Text §6 and
  Limitations.
- Evidence: SUP lines 1363–1370 and 1408–1415 ("(a3) coupled family, r₁ and q held", the values B23 (a3)'s); S3 line
  315: "is the coupled family at coefficient 0.83, c = 0.03, q_ε = 0.093 (section 3)"; MT line 201: "the coupled family
  is symmetric"; DISP line 2533.
- Grade: note

**Y1-10**
- Where: SUP line 1712, the numbers derived on 24 September 2026, second cell: "Results 1 and the Discussion (the
  windowed estimator's per-SD ratio, 1.4)".
- Problem: For the same number the numbers table names `derived_r17.out` at Results 1 and not at the Discussion, so
  that by the rule of DISP's point (1), which follows the numbers table, the two places fall on different sides; the
  report had the Discussion's 1.4 as [R]. The cell is right that both places print the ratio and that item 5 of the
  output holds it (line 42, "= 1.41").
- Evidence: CSV line 99: "derived: (5.126 × 0.0284) / (0.528 × 0.1957) = 1.41 (AD lines 27 and 29; derived_r17.out
  item 5)"; CSV line 1146: "derived: (5.126 × 0.0284) / (0.528 × 0.1957) = 1.41 (AD lines 27 and 29)"; PB line 426.
- Grade: note

**Y1-11**
- Where: SUP line 1711, the numbers derived for the revision of 1–2 October 2026, second cell: "Results 7 and Table 4
  (the inverted intervals of the contrasts at p = 10 and 20; in Results 7 also, in words, the Fisher-z intervals of the
  whitened correlations)".
- Problem: Results 7 prints the interval at p = 20 only; that at p = 10 is in Table 4 alone. The gloss holds of the two
  places together and not of Results 7.
- Evidence: MT line 158: "at p = 20, −0.0127 [−0.0203, −0.0052] (p = 0.0002, negative in 13 of 14)", with no interval
  for p = 10; MT line 167: "| AR(10) residuals | 0.137 | 51.2 % | 0.0866 | −0.0191 [−0.0285, −0.0098] | 0.0002 |
  +0.445 |".
- Grade: note

**Y1-12**
- Where: outside S19 Table, in the record's entry on the revision (REC lines 9498–9500), which counts the table's
  changes: "in S19 Table, its head note, which states what the last column of Part A and the second column of Part B
  name, six cells of Part A, twelve of Part B and five new rows of Part B".
- Problem: Between `checked3` and HEAD thirteen cells of Part B changed, in twelve rows: the second cells of twelve
  rows and the third cell of the row of `derived_r24.out`. The six of Part A and the five new rows are as the diff has
  them.
- Evidence: the comparison of the two versions of SUP cell by cell: Part A, the last cells of lines 1610, 1622, 1625,
  1634, 1636 and 1684; Part B, the second cells of lines 1695–1700, 1702–1705, 1711 and 1712 and the third cell of line
  1711 ("six CSV files, two tables files" to "eight CSV files, five tables files", and the clause on items 13 and 14).
- Grade: note

## Checked and found exact

**1. Part B, each of the 18 rows: the computation's files and values, every place of the main text, of S1–S3 Text and
of the supporting tables that quotes it (by its file names, by its values, and through the `source_file`, `locator`
and `note` columns of the numbers table), the second cell against those places with every gloss, and the first and
third cells against their sources. Compared afterwards with PB: every place that PB marks [V], [D] or [N] and that
lies within the head note's rule is named in the HEAD cell; the places it marks [N] that the cells leave out are in S4
Text, S5 Text (no value) and S17 Table, which the rule excludes.**

- Line 1695, the review computations of 14 September 2026. The file has sections 0–6, the deconvolution its section 3.
  Results 2 (MT line 106: −0.0146 [−0.0261, −0.0037], p = 0.0106, 12 of 14; phase p 0.073; shares 0.34 and 0.40),
  Results 6 (MT line 154: ΦR +0.0007 [−0.0093, +0.0112], level 0.096) and Results 7 (MT line 171: 0.848 → 0.783,
  1.155 → 0.832, −0.0782, p = 0.0013); the captions of Fig 3 and Table 3 (−0.0146); Methods, Estimator (about 18, the
  pooled placebo function) and Remedies; S1 Text; S2 Text; S3 Text §4 to §10 (each section holds a value or names the
  file; §6 with rows 1 and 2 of its residual table); S11, S13, S15 and S20 Tables. Results 4 prints no value of these
  computations (its −0.79 is `derived_r17`'s; the r₁ DiD is in Table 3's caption). Third cell as the file and S3 Text
  §4 have it.
- Line 1696, the finite-sample null. `notes/review_results/logs/review_v2_residual_null.log`: residual DiD +0.0054
  (DMT +0.0041, placebo −0.0013), one simulation; the script first committed at 9318997 (15 September 2026); REC lines
  2615–2625 (run before any record entry, no recorded rule). Results 1 names it without a value; Results 4, the
  captions of Figs 3 and 5, Table 3 (−0.37), Methods, S3 Text §5, §6 (row 5 of the residual table) and §7, S12 and S13
  Tables hold +0.0054 or the rate; S9 Table names it, its values there being those of later simulations.
- Line 1697, the sts-matched null: Results 7, Methods' Remedies ("four matched pairs"), S3 Text §6 (the script named)
  and §9, S13 Table (−0.069, −0.056, `sts_matched_null_F3.log`) and S16 Table; the four pairs are F1-i, F1-ii, F2-ii
  and F3-b.
- Line 1698, the spectral centroid: `rev_extra.log` line 27 (+0.00231 [+0.00060, +0.00395], p 0.0217, 12 of 14);
  Results 5 (+0.0023 Hz, p = 0.022); S3 Text §4 (0.0369 and 0.0374 Hz, the log named) and §9; S14 Table's source line
  points to S3 Text §9; the interval is a percentile interval, no per-subject vector saved.
- Line 1699, global functional connectivity per bin: S1 Text (line 17) cites S7 Table; S3 Text §4 (+0.0526 [+0.0008,
  +0.1041], p = 0.0470; 0.190 to 0.233); S7 Table; the script first committed on 13 September 2026; no
  pre-specification entry in the record.
- Line 1700, the coupled family: Results 1 (the responses up to +0.10, most at +0.05), Fig 1c (the six values of
  `coupling_map_tables.md`), S3 Text §3; the pre-run entry of 15 September 2026, 07:30 UTC (REC line 2429) enters B8 as
  analytic, with no prediction. S18 Table: Y1-9.
- Line 1701, the leave-two-out: S3 Text §5; `leave_two_out.log`: 91 refits, +0.846 to +0.973; pre-run entry of 15
  September 2026, 11:09 UTC, with no prediction (REC line 2661).
- Line 1702, the checks of the review of 17 September 2026: the three glosses against the three logs (0 of 36,481;
  p = 0.0001; +0.974 to +0.946, printed as +0.95); the folder holds six checks.
- Line 1703, the leave-one-out: Results 2 ("p ≤ 0.008"); `results/loo_did_win60.csv`, 28 refits, largest p 0.00757.
- Line 1704, the proportionality check: Results 2 and S1 Text (line 19) cite S8 Table; S3 Text §9 (+0.0204 [+0.0032,
  +0.0380], p = 0.025); S8 Table; the script's commit of 14 September 2026 records the rule before the run.
- Line 1705, the residual's source: `residual_source.log` (pair r₁ DiD −0.0155; pair |q| DiD −0.0164, 10 of 14; mean
  residual −0.0489); Results 2 and 4 (−0.74), the three captions, S3 Text §3, §4, §6 and §7, S13 Table;
  `notes/partB4_diagnostic.md` says that the supplement was written after the diagnostic's numbers were seen.
- Line 1706 (new), the first review's own checks: `notes/review_checks.py` and its log exist; the log holds "per-subject
  r(global-fit DiD, windowed DiD) = 0.954", "DiD -0.0994, negative 12/14" for the 20-region fit and, for CCS under
  `phyid`'s mask on 400 random pairs, "negative 0/14"; S5 Text §1 quotes the three (−0.0994 and 12 of 14; 0.95; 14 of
  14) and no other place of the paper does; `notes/review_computations_2026-09-14.md` holds none of the three; no
  pre-run entry; the date is the review's, as in the rows of the other scripts of that review (all first committed at
  9318997).
- Line 1707 (new), the whole-brain ΦR items: the pre-specification
  (`notes/prespec_regional_phir_deconv_2026-09-14.md`) lists "Three whole-brain items requested at the same time (no
  prediction)", the three of the cell; the report (line 220) says of the four tests "Not in the recorded plan: these
  four tests were added after looking at the window series above, and are descriptive"; the log holds the four (the
  gap, the placebo run's slope, the DMT run's slope, the placebo run's window 4 − window 1). S2 Text: 56 % is the
  placebo share at W = 30 (0.5599 in the file's first row); the gap −0.0124, p = 0.014, raw −0.0042, p = 0.28; the
  slope −0.00115, p = 0.025, raw −0.00036, p = 0.43; the decline −0.0084 [−0.0174, −0.0003], p = 0.039, and −0.0120, p
  = 0.067. First cell's file name: Y1-5. Second cell: Y1-8.
- Line 1708 (new), the third review's partial correlations: the review's Appendix, computation 4 (+0.831 / +0.855; with
  `phyid`'s mask +0.688 / +0.820); `partial_b26.out` (+0.831, +0.855; +0.687, +0.820); S3 Text §6 prints +0.83 and
  +0.86, +0.69 and +0.82, and names computation 3, the variations of the null, at two places without a value.
- Line 1709 (new), the transfer entropies: the script, copied to VW/Y1/ and run there, gives for coefficients 0.90
  and 0.70 and innovation correlation 0.3 lag-1 transfer entropies of 0 before the filter, 0.001508 and 0.000408
  after it, 0.000000 at ten lags, and 0 on the symmetric family, as S3 Text §3 prints them; no data, no random
  numbers, no pre-run entry.
- Line 1710 (new), the audit's values: `findings_text.md`, T07 (2.644997; 0.576258), T25 (−0.015468, −0.014645,
  +0.011534, −0.7457) and T10 (−0.861 [−1.299, −0.422], r = −0.777), as S5 Text §4 quotes them, with "The paper uses
  none of these".
- Line 1711, `derived_r24.out`: the script reads two pickles, eight CSV files, five tables files, three array files
  and one log, and draws no random numbers; items 1 to 14 hold what the third cell says (item 13, +0.00044 [−0.00061,
  +0.00149]; item 14, +1.12 [−0.58, +2.97]; the addition to item 1, −0.0037 [−0.0066, −0.0008]; item 6, eight
  intervals, seven including zero); every gloss of the second cell against its place but the one of Y1-11; S19 Table,
  Part A, rows B28 (c) and B16c (e) name items 5 and 1; no pre-run entry in the record.
- Line 1712, `derived_r17.out`: every gloss against its place and the output (5.5 [4.45, 10.54]; −0.064 and +0.024;
  0.486, 0.571, 0.68–0.83; 0.807; the two t intervals; 0.056; −0.79 [−1.60, −0.08]; −0.37 and −0.0146; 0.54; 1.4); the
  second output differs from the first in the residual's rate (−0.788 for −0.787) and one bootstrap bound only.

**2. Computations without a row.** Every file name in a code span of the main text, S1–S5 Text and the supporting
tables (281 distinct strings), the 54 source files of the numbers table and every place where the paper calls a
computation post hoc or a review computation were classed as pipeline, computation with a pre-run entry or with the
plan of 14 September, check of the pipeline's reproduction, or row of Part B: no quoted computation without a pre-run
entry lacks a row. Of the borderline kinds of the dispositions' last paragraph: the figure script's values (CSV lines
117, 118 and 371, from the saved pairs and the atoms table); the Spearman–Brown ceilings and the share of S8 Table's
note (arithmetic, Y1-6); the subject-alignment check (named in S1 Text, S4 Text and S5 Text §4, no result quoted);
the values that a pre-run entry lists as known (the head note; SUP line 1653); the validation of the second
implementation (planned in item 2 of the pre-specification's plan, reported in section 0 of the report). The
conversion to 44 % and 37 %: Y1-6.

**3. Part A, the changed cells.** Each named place was opened and the paper searched for the outcome's values.
- Line 1610, the tier assignment: R 0.964–0.990 and the lower bounds are in the record (REC lines 963–978) and at no
  place of the paper; S1 Text (line 11) defines the tiers and, with S2 Table, gives the tier-2 criterion on the data.
- Line 1616, the regional ΦR check (cell unchanged): S2 Text's new sentence, the row's outcome and the report's first
  table agree in every number (−0.0047 [−0.0079, −0.0013], p = 0.0233 printed 0.023, positive in 4 of 14); the
  interval is a subject-bootstrap percentile interval; inside +0.0156, outside +0.0203, so the increase is smaller
  inside; no other place gives the outcome.
- Line 1622: S3 Text §6 (line 315) says that a signed mean cancels on ts_gsr and prints none of the values; S9 Table
  (line 187) holds +0.00009 [+0.00004, +0.00014], p = 0.0004 and −0.00738 among its earlier values. S5 Text §1: Y1-2.
- Line 1625: S3 Text §6 (line 347) says that the window-sign statistic is superseded; S9 Table (line 185) holds 1.80
  and +0.00025 ± 0.00005 among its superseded values. S5 Text §1: Y1-2.
- Line 1634, B17 (iv): S3 Text §7 and S10 Table hold 0.7131, 0.7152 and +0.0051 ± 0.0017; Limitations states the
  outcome in words; Methods prints 0.715 (CSV line 1321: `calibration_tables.md`, condition (i), 0.7152).
- Line 1636, B19 (b): S3 Text §4 (line 134) holds R² = 0.808, r² = 0.462 and +0.661, −0.463, −0.426; Results 1 prints
  none of them, and its +5.13, −0.53 and 4.7 are B22 (d)'s (CSV lines 93–98).
- Line 1684, B16c (b): Table 4, S11 Table and S3 Text §8 hold the levels; Results 7 has "18 %" (0.0127 / 0.0719).
  Discussion: Y1-2.
- By value, in the main text, no outcome of the 81 rows is printed at a place its cell does not name. Searched: every
  decimal number of the 81 outcome cells, as printed, in the main text, S1–S5 Text and S1–S16, S18 and S20 Tables;
  for the numbers with three or more significant digits every hit at an unnamed place was read; for the others the
  hits were read where the number occurs up to twelve times and the number was otherwise searched with its ± or its
  interval; roundings to one and two fewer decimals where they occur up to eight times. S17 Table's body was read for
  the rows named in Y1-1 only. One derived number stands at a place that two cells do not name: the Abstract's
  excesses, "0.006–0.009 above simulated pure autocorrelation changes", are the residual DiD less the expectations of
  B17 (i) and B17b (i); the numbers table (CSV lines 31 and 32) gives B27 (c)'s sensitivity line as their source, and
  the head note places B27's values in the Abstract among other places.

**4. The head note.** "the sources of the other numbers of the main text are in `manuscript/main_text_numbers.csv`":
the table has 1,381 rows, every data, design, literature and bound row with a source file and locator, every derived
row with its derivation. Part B's rule as the cells follow it: no second cell names S17 Table or S4 Text; S5 Text is
named in two cells (lines 1706, 1710), where it quotes values; the main text's list of supporting information is named
in none. The two sentences are as replacement U09h has them. The rule for Part A: Y1-1, Y1-2; the clause on S17 Table:
Y1-4; S18 Table in the cell of the coupled family: Y1-9.

**5. The dispositions.** X1-2: Part B has the two rows, with the titles quoted; S4 Text's row S6 (S4 line 53) ends "S19
Table's Part B gives the status of each", and every computation that the paper calls post hoc or a review computation
has a row. X1-4, X1-5, X1-6, X1-7: the cells and S2 Text's sentence stand at the places named, word for word, and each
correction answers its finding. X1-9: the disposition of W3-4 now says that the cell of B22 (a) named Results 4
before. X1-11: the three cells name the sections, and S5 Text §1 has "three of its checks are quoted, as review
computations, in S3 Text §4, §6 and §9". X1-8: the head note's sentence is quoted word for word; the statement that
follows it is Y1-3. The closing section: Part B had thirteen rows at `checked3` and PB has thirteen sections; point
(1) quotes the head note word for word (what it says the rule leaves out: Y1-7); point (2): the eleven cells named
are the eleven that were completed, the parenthesis on Results 4 and on the places added holds against the two
versions of the cell, the cell of the leave-one-out lost "S4 Text" and that of the leave-two-out is unchanged; point
(3): the five rows are as described; the last paragraph: section 2 above.

**6. The replacements.** The 95 replacements of the file for `manuscript/supplementary.md`, applied in order to the
file of 8bd189e, each match the stated number of times and give the file of HEAD. For U06d, U08.8, U08.9, U08.10,
U09g.1 to U09g.5, U09h and U09i.1 to U09i.8 the `why` holds of `old`, of `new` and of the places it names: the old
Table 3 is the residual table of S3 Text §6; the deconvolution is section 3 of the review's file and Results 7 quotes
it; S1 Text and S2 Table give neither R nor the assignment; S3 Text §6 prints none of the values of the two cross-lag
rows; Methods prints 0.715; Results 1's slopes and ratio are B22 (d)'s; Methods' Remedies names the four matched
pairs, S3 Text §6 the null's script, S13 Table its log; S3 Text §4 gives the two centroids with the log; S1 Text
points to S7 Table and to S8 Table; S18 Table names the family in B23 (a3)'s rows and prints no value of B8; S3 Text §4
quotes the check with its log; the cell of the leave-one-out dropped S4 Text; the cell of `derived_r17.out` gained
what the reason lists. U06d's five rows stand before the row of `derived_r24.out`. The clause of U09h's `new` text on
S17 Table is Y1-4.
