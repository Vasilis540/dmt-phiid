# VM — verification of the main text (`manuscript/draft_v2.md`, HEAD 9caa60b against 8bd189e)

**Result: no finding of grade `error`.** Ten findings: 4 `inexact` (VM-1, VM-2, VM-8, VM-10; the last concerns the numbers table, not the text) and 6 `note`. Nothing under VT was modified (`git status --short --ignored` is empty at the end). The figure script was run only as a copy under `VW/VM/figrun/`, reading the committed result files.

## Findings

**VM-1** — grade: `inexact`
- Where: `draft_v2.md` line 241, Methods, "The primary contrast and the exploratory analyses": "(the text says so for the r₁ contrast and the leave-one-out, Results 2; the residual map's network structure, Results 3; the spectral centroid, Results 5; the deconvolved contrast, Results 7)".
- Problem: the enumeration is incomplete. The text states the status at four further places.
- Evidence:
  - Line 108 (Results 2): "S8 Table gives a post hoc check of the ratio sts / TDMI".
  - Line 114 (Results 3): "r = 0.898 (post hoc; S3 Text §4)".
  - Line 114 (Results 3): "fixed in the record before the partialled map was computed (S19 Table)".
  - Line 187 (Discussion): "a prediction recorded before it was computed (S1 Text; S6 Table)".
  - The sentence at line 241 is new in the revision; the baseline text carried no such list.

**VM-2** — grade: `inexact` (small)
- Where: line 114, Results 3: "it vanishes at its point estimate, but the interval admits up to half of it (Fig 4b)".
- Problem: the interval admits slightly more than half. Its lower limit, −0.0110, is 54 % of the contrast −0.0202.
- Evidence: the same sentence gives "+0.0007 [−0.0110, +0.0124]"; `regional_partial_tables.md` line 74 (+0.0007 ± 0.0203; t, 13 df, gives [−0.0110, +0.0124]); `derived_r17_b26.out` line 38. 0.0110 / 0.0202 = 0.545.

**VM-3** — grade: `note`
- Where: line 87, Results 2: "The DiD's between-subject variance is mostly the gap's (r(DiD, pre-injection gap) = −0.888, r² = 0.79; SD 0.0887 against 0.0485 for the post-injection gap)".
- Problem: the four numbers are exact, but r² = 0.79 does not by itself apportion the variance. The same source line gives r(DiD, post-injection gap) = +0.868 (r² = 0.75). Only the SD comparison carries "mostly".
- Evidence: `baseline_gap_tables.md` line 10 (−0.888 | +0.868). Recomputed from `baseline_gap.csv`: r(pre gap, post gap) = −0.543; Var(DiD) = 30 % post-gap variance + 35 % pre-gap variance + 35 % covariance term.

**VM-4** — grade: `note`
- Where: line 124, Results 4: "the ramp moves the generators' mean residual DiD by 0.0001 and 0.0006 nats from the step".
- Problem: exact from the unrounded means, but Table 3's printed cells differ by 0.0002 and 0.0007 (+0.0022 vs +0.0020; +0.0049 vs +0.0042). The main text does not say the figures come from unrounded means.
- Evidence: `derived_r24.out` lines 55–56 (+0.000148, +0.000620); Table 3, lines 135–138.

**VM-5** — grade: `note` (wording unchanged from the baseline)
- Where: line 124: "the per-subject relation holds across split halves on the primary variant (−0.700 and −0.385), not on the sensitivity variant (−0.598 and −0.051)".
- Problem: numbers exact. On each variant one cross-half correlation is clearly negative and one is not, so "holds / not" rests on −0.385 against −0.051.
- Evidence: `splithalf.log` line 12 (−0.385, p = 0.175; −0.700, p = 0.005) and line 24 (−0.598, p = 0.024; −0.051, p = 0.861). Fisher-z interval of −0.385 at N = 14 is [−0.760, +0.183], which includes zero.

**VM-6** — grade: `note`
- Where: line 108, Results 2: "5.2 on pair r₁, between the AR(1) pairs' 3.1 and the band-passed generator's 6.1 (S13 Table)"; also Fig 3's caption, line 110.
- Problem: "the AR(1) pairs" and "the band-passed generator" are used before they are introduced (Results 4, line 124; Methods, line 245). The baseline sentence carried a forward pointer ("the band-passed generator of Results 4 gives −0.0944…", old line 102); the revised sentence points only to S13 Table.
- The terms the task named are all defined at or before first use: DiD, regional / whole-brain / pair r₁, a_x, a_y, the AR(1)-substituted estimate, W = 60 and global fit in the Results' opening paragraph (line 35); the three readings in Results 2 and Table 2's caption.

**VM-7** — grade: `note`
- Where: line 19, Author summary: "compare each synergy contrast with the estimate our closed form gives from the regions' autocorrelations".
- Problem: the estimate also uses each pair's lag-0 correlation.
- Evidence: line 35 (a_x, a_y and q); Abstract ("at each pair's measured autocorrelations and lag-0 correlation"); line 197 ("from each pair's measured (a_x, a_y, q)").

**VM-8** — grade: `inexact` (titles); contents agree
- Where: the list of supporting information, lines 401–441.
- Problem: five table titles are not those of `manuscript/supplementary.md`.
  - S1 Table (line 403): list "…sensitivity windows 5–14 against pre-injection windows 1–4, W = 60."; file line 5 has "…windows 5–14 (bins 9–28) against…".
  - S9 Table (line 419): file line 155 adds "(S3 Text, section 6)" and ends "…16 September 2026, 10:32 UTC".
  - S17 Table (line 435): file line 398 ends "by method (B21)".
  - S18 Table (line 437): the list's bold title has "the other computations of 23 September 2026", which the file's title (line 1339) does not; the file's title ends "(B23, B24, B28)". The date itself agrees with S18's source note.
  - S20 Table (line 441): list "the reading of each on the sts surface of Fig 1a"; file line 1709 "the map's reading of each".
- Also: the description of S5 Text (line 401) names the contents of its §1, §2, §4, §5, §6 and not §3 ("The decisions of 20 September 2026").
- All other titles (S1–S5 Text; S2–S8, S10–S16, S19 Tables) and every description match the files.

**VM-9** — grade: `note`
- Where: the committed figure files and `manuscript/figures/captions_v2.md` at HEAD, against the captions of Figs 1, 3, 4, 5, 6 in the main text.
- Problem: the committed figures and captions are the previous generation (`captions_v2.md` line 3: "at git 71cf932").
  - Its captions of Figs 1, 3, 4, 5 and 6 differ from the main text's (Fig 2's is identical).
  - The committed `fig3_v2_per_subject.png` has no "two thin lines through the data's centroid".
  - The committed `fig5_v2_residual_diagnostic.png` draws (c) on −0.04 to +0.06, not "magnified four times (y-range −0.02 to +0.03 nats)".
- Evidence: a copy of `scripts/15_figures_v2.py` run on the committed result files gives six captions byte-identical to the main text's (script caption minus its final "Source: …" sentence) and the drawings the captions describe. S5 Text §6 says the regenerated figures and captions are "in the commit after it"; the main text is right once that commit is made.

**VM-10** — grade: `inexact` (in `manuscript/main_text_numbers.csv` only; the text's numbers are right)
- Where and problem: locators that lead to a line that does not hold the number.
  - File lines 355, 407–412, 958: the "95" of the captions of Fig 2, Table 2 and Fig 6, and Table 2's caption's "6", "14", "1", "4", "14". All cite `manuscript/analysis_record.md` "line 189; anchor: W = 60". That line reads "shift), **18–45 % at W = 60**. Asymmetric family: **52–66 % at" — a statement of the estimator's bias shares, with no 95 % coverage, window set or N = 14. The table's head note says the N = 14 rows now cite the record's line on the shape of the data (line 48), which the row at file line 411 does not.
  - File lines 169–175, 349–350, 601–602, 954–955: the window sets 1–4 / 6–14 and "14 subjects" in the captions of Table 1, Figs 2, 3, 6. They cite `family_atoms_tables.md` line 6 (the heading "## ts_gsr, W = 60: Table 1's columns…"); the settings are on line 4 of that file.
  - File line 1271 ("7 × 10⁻¹⁶", a bound): the locator says "the line holds bound on 5.6e-16"; the bound is on 6.7e-16, on the same line (the row's own note says so).

## Checked and found exact

**1. Numbers of the changed text (numbers table, 1,378 rows)**
- Every row whose context lies in a changed or added paragraph, table or caption was opened at its source line: value at printed precision, sign and wording, quantity, variant, estimator, condition. All agree. The rest of the table was read the same way.
- Mechanical cross-checks: for the 1,073 located rows the anchor and held string are on the cited line (exceptions are the five bound rows and two formula contexts); for the 770 rows with a parsable held value, the printed number equals the held value rounded half away from zero, with no mismatch.
- Every row about ts_demean, W = 30, the global fit, the run level, deconvolution or phyid's mask cites a line of that variant or estimator, and no ts_gsr / W = 60 row cites another.
- All 54 derived rows redone.
- No second rounding found. Checked against the unrounded values: 0.108 / 0.218 / 0.251 (1762, 3576, 4108 of 16,384); 0.89 and 0.895 from 0.894889; −0.27 from −0.2748; 0.263 from 0.262547; 4.7 from 4.66; 0.0001 / 0.0006 from 0.000148 / 0.000620.
- Every number token before the reference list has a row; the uncovered tokens are years, cross-reference numbers, dates, commit identifiers and DOI digits.

**2. Tables**
- Table 1: body identical to the baseline; all 17 rows equal `family_atoms_tables.md`. Thirteen atoms with a non-zero substituted DiD share the observed DiD's sign; three print 0.0000 (rty, xtr, xty). Excess −0.0844 and −0.1003; the 16 atoms sum to 1.4772.
- Table 2: all twelve rows × two variants. The six new rows equal `baseline_gap_tables.md` (a), lines 10–11 and 14–15. The other rows equal `inference_revision.csv` and `inference_rows_raw.csv`. Means recomputed from `baseline_gap.csv`. Caption exact (12 df; intercept of the post gap on the pre gap).
- Table 3: all ten rows equal `baseline_gap_tables.md` (c) and `matched_slope_tables.md`.
  - Recomputed: slope −0.753 [−1.133, −0.373], r −0.780, intercept +0.0005; the leave-one-out and leave-two-out ranges and counts.
  - 0 of 100 replicates at or below the data's slope in each of the four conditions; minimum replicate slopes −0.442, −0.488, −0.566, −0.596.
  - Caption: rescaling to −0.015; subject 8 at −0.0657 held at the floor −0.0375; sample 300 is the start of window 6; ramp over samples 300–420; divisor 100.
- Table 4: all five rows.
  - r₁ and power above the band from `whitened_spectrum_tables.md`.
  - Levels 1.1554, 0.7176, 0.2202, 0.0866, 0.0719.
  - DiDs, intervals and p from `inference_revision.csv` and `derived_r24.out` item 1.
  - r: +0.953, +0.899, +0.495, +0.445, +0.333.
  - Caption: 3,218 of 3,220; 99.2 %.

**3. The paper against itself**
- Every number stated more than once agrees at compatible precision. Checked:
  - Primary contrast: −0.0809 [−0.1317, −0.0310], p 0.0038, against −0.081 [−0.132, −0.031], p 0.004.
  - −0.0544 / −0.054; −0.09441 / −0.094; 0.694 [0.258, 0.895] / 0.69 [0.26, 0.89]; 0.951 [0.617, 0.991] / 0.95 [0.62, 0.99]; 0.863 / 0.86.
  - 0.0115; excesses 0.0088, 0.0066, 0.0061 / 0.006–0.009; +0.0027, +0.0049, +0.0054 / 0.003–0.005; 0.0155; 0.108, 0.218, 0.251 / 0.11–0.25.
  - 4.7 and 1.4; −0.0146 and −0.0155; 0.953 [0.854, 0.985]; 4.26 [3.41, 5.12].
  - −0.75 [−1.13, −0.37]; −0.18, −0.39, −0.37; −0.74 and −0.79; 6.07; 3.09, 2.645, 2.30; 0.50 and 0.056 / 0.06.
  - 1.1554 / 1.155; 0.848; −0.0202 → +0.0037; 0.0009 and 0.0564.
  - FD +0.0143, p 0.2452 / 0.25; 23.6 and 10.1; g 0.61; ten studies = nine + Gao.
- Each claim of the Abstract and of the Author summary is a statement of the Results or captions, no wider. Includes "synergy rose in one volunteer, autocorrelation in two" (subject 14; subjects 5 and 14) and "partly through that gap" (−0.844, +0.939, partial +0.824, from `baseline_gap_tables.md` (b)).
- Cross-references: every "(Results N)", "(Table N)", "(Fig Nx)", "(Methods)" target exists and holds what is promised.
- SI pointers verified:
  - S1 Text, S2 Text (deconvolution; the series and sandbox are not in the repository), S4 Text.
  - S3 Text §2–§11, each pointer against its section.
  - S5 Text §1 (eight deviations), §4 (runs at c25a310, d5a65bd, 13e7299; 475 min) and §5.
  - S1, S2, S5, S6, S8, S9, S10–S18 Tables.
  - S19 Table: recounted 36 met, 15 partly met, 16 missed = 67; Part B lists every item the text calls post hoc.
  - S20 Table: rows 1–10 are the ten studies. MMI stated in rows 1, 3, 4, 5, 6, 7, 8, 10; a Gaussian estimator named in rows 1, 3, 4, 5, 10; CCS primary in row 2; lag of one TR in rows 2, 6, 10; surrogate |ρ| ≤ 0.26 against 0.22–0.54.
- The files and functions named in Data and code availability exist.

**4. Statistical statements (recomputed)**
- Sensitivity: (2.1604 + 0.8702) × 0.0051146 = 0.01550; exact noncentral t gives 0.015504.
- Fisher-z at N = 14: +0.495 gives [−0.048, +0.812] and +0.333 gives [−0.240, +0.734], both including zero; 0.953 gives [0.854, 0.985]; 0.6937 gives [0.258, 0.895].
- g = 0.6106. Fieller intervals [4.45, 10.54] and [−1.60, −0.08]; the latter contains −0.18, −0.39, −0.37.
- 38 % = 0.617²; r² 0.788; SD 0.0887 and 0.0485.
- "A fifth" 0.197; "a sixth" 0.163; placebo shares 0.34 and 0.40.
- "About nine times": 0.4981 / 0.0556 = 8.96. "A sixth": 0.161. "About half": 3.09 / 6.07.
- Table 4 phrases: 62 % and 77 % ("most"); 33.8 %, 19.1 %, 32.4 % ("a third, a fifth, a third"); 18 % against 7 %; cos(2π × 0.16) = 0.536; flat band 0.8176.
- "About 12 %": 0.0112 / 0.0961. ΦR sign-flip p all ≥ 0.0853; phase p 0.019–0.038 with signs −, +, +.
- CCS correlations −0.43 to −0.27, all intervals including zero; reliability 0.302.
- "Lies below the central 95 % of every condition's slopes" and "no replicate as steep": true.
- Degrees of freedom: 12 for the 14-subject regressions, 11 and 10 with subjects left out, 13 for the t intervals of means.
- Closed form, by my own implementation: identities to 3 × 10⁻¹⁵; ∂sts/∂r₁ 6.0705, ∂sts/∂q −0.1892, ∂sts/∂c −1.7402; asymmetry rate −3.09; sign change at 0.008; per-SD ratios 4.66 and 1.40; binarised 1.76.
- The claim that every positive-definite stationary 4 × 4 matrix is a stable VAR(1) is correct (Schur complement, Lyapunov).

**5. Rules of the text**
- No computation label anywhere in the file. No file path or code span before "## Data and code availability".
- No round, stage, bundle or session name and no reviewer's letter. "The cold reads" in Data and code availability names a kind of document.
- Word counts: `wc.py` gives 8,498 with headings (limit 8,500); it excludes tables, table and figure captions and four display-equation lines (87 tokens). Abstract 300 tokens (limit 300); Author summary 200 (limit 200).
- Citations: all 48 reference entries are cited before "## References", and every in-text citation, multi-year ones included, has an entry.

**6. Figure captions**
- All six main-text captions are byte-identical to the script's captions without the Source sentence; the script's own assertions pass.
- Caption statements about the drawing agree with the script and the regenerated figures: Fig 1 (grid step 0.01, percentile contours 50/80/95, the five contour levels with two labelled inline, the four curves); Fig 3 (markers, the thin lines and their slopes −0.200 and −0.355); Fig 4 (31 and 37 parcels, colours); Fig 5 (height ratios 0.30 : 0.20 : 0.20, so (c) is at a quarter of the nats per unit height; hatching; injection at 8 min); Fig 6.

**Not checked (outside what the tree allows offline)**
- Statements about cited papers, beyond their agreement with S20 Table.
- The licence statements about the external data repository and the Zenodo record.
- The eight [TK] placeholders (author list, affiliations, REC reference, Zenodo DOI, CRediT, funding, competing interests, acknowledgments) are unchanged from 8bd189e.
