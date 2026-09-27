# Findings, checker C: manuscript/supplementary.md (head note, S1–S20 Table), 26 September 2026

**Counts:** T 1, N 4, X 3, C 2, U 3 (13 findings).

Line numbers are the original line numbers of `manuscript/supplementary.md` (repo at c25a310 with the pending edits applied).

## N: numbers

### N1
- **Location**: line 38 (S2 Table, the W = 30 paragraph).
- **Quote**: "per-subject means −0.388 / −0.408 raw"
- **Problem**: The raw per-subject mean ρ_S against the template at W = 30 is −0.40749, which rounds to −0.407. The −0.408 comes from rounding twice: the log prints −0.4075.
- **Evidence**: `results/primary_b_ts_gsr_win30.csv` line 76: −0.40748931151407936. `results/run_06_ts_gsr_win30.log` line 84 prints −0.4075. `analysis_record.md` line 1661 carries the same −0.408.
- **Fix**: "per-subject means −0.388 / −0.407 raw"

### N2
- **Location**: S9 Table, lines 161 and 162 (ts_gsr, δ_means column: grand-mean and DMT rows) and line 175 (ts_demean, ε column, DMT row). Also S17 Table lines 1222–1223 (rows 841–842, percentile column).
- **Quote**: "+0.00001 [+0.00000, +0.00003]" (line 161); "+0.00002 [+0.00000, +0.00005]" (line 162); "−0.00007 [−0.00014, +0.00000]" (line 175); in S17, "[+0.00000, +0.00003]" and "[+0.00000, +0.00004]" (percentile column).
- **Problem**: Three inverted-interval limits that are negative in the source are printed as "+0.00000". S17 prints the same three limits as "−0.00000" (rows 841, 842, 881), so the file contradicts itself. The ε limit matters: that interval excludes zero (p = 0.0479; S17 row 881 reads "no / no / no"), and "+0.00000" makes it look as if it reaches zero. S17's percentile column also turns the committed "−0.00000" of rows 841–842 into "+0.00000".
- **Evidence**: `inference_revision.csv` gives inv_lo −4.998e−06 (grand mean), −4.538e−06 (DMT run) and inv_hi −6.82e−07 (ε, ts_demean, DMT; p 0.0479). `inference_revision_tables.md` lines 199, 200 and 239 print "[-0.00000, +0.00003]", "[-0.00000, +0.00005]" and "[-0.00014, -0.00000]". `crosslag_budget_tables.md` prints the committed percentile limits as "[-0.00000, +0.00003]" and "[-0.00000, +0.00004]", as S9 did at 90690f4.
- **Fix**: line 161 "[−0.00000, +0.00003]"; line 162 "[−0.00000, +0.00005]"; line 175 "[−0.00014, −0.00000]"; lines 1222 and 1223 (percentile column) "[−0.00000, +0.00003]" and "[−0.00000, +0.00004]".

### N3
- **Location**: lines 1574 and 1575 (S19 Part A, first column).
- **Quote**: "Pre-registered analysis choices, the prediction for the 20,000-run repeat (13 Sep 2026)" and "Pre-registered analysis choices, the tier assignment (13 Sep 2026)"
- **Problem**: Both predictions were recorded on 12 September 2026, in commit 18ad8b4, which the two rows above them cite. The date 13 September belongs to the outcome.
- **Evidence**: `git show 18ad8b4:CLAUDE.md` lines 683–693 hold "Prediction for the repeat, recorded before it finished … ≤ 0.89 and plausibly below 0.80 … tier 1 FAIL, tier 2 PASS (R 0.95–0.98 with lower bounds ≥ 0.87) → outcome tier 2". `git log -S` finds these strings first at 18ad8b4 (2026-09-12 21:43 +0300). The record places the prediction (line 907) in the block "Outcome of the first full non-stationary run (2,000 runs, 12 Sep 2026" (line 836). The outcome, "finished 13 Sep 2026 12:06", is at line 956.
- **Fix**: "(18ad8b4, 12 Sep 2026)" in both rows.

### N4
- **Location**: line 376 (S17 Table source note).
- **Quote**: "36 recomputations of the per-run changes and FD-residualised DiDs of Table 2 and S1 Table ("engine")"
- **Problem**: Only 24 of the 36 "engine" rows are Table 2 and S1 Table quantities. The other 12 (rows 763–774) are S3 Text quantities: the diag residual, CCSpub sts and autocorr, on ts_gsr at W = 60. Every block of four rows also includes the FD DiD, which the description leaves out.
- **Evidence**: the `source` column of `inference_revision.csv` has 16 + 8 rows "recomputed as rev_inference.Engine (Table 2, S1 Table)" and "(S1 Table (W = 30))", and 3 × 4 rows "recomputed as rev_inference.Engine (S3 Text)". The fields are dmt_change, pcb_change, fd_did and resid_did. Record, B21 pre-run entry (line ≈5952): "The same recomputation … covers the other per-run and FD-residualised values the text quotes … (S3 Text …)".
- **Fix**: "36 recomputations of the per-run changes, FD DiDs and FD-residualised DiDs of Table 2, S1 Table and S3 Text ("engine")"

## X: cross-references

### X1
- **Location**: line 365 (S16 Table source note).
- **Quote**: "(`notes/rev_sts_matched_null.py`; review of 14 September, section 5; a post hoc computation)"
- **Problem**: In this paper "the review of 14 September" means `notes/adversarial_review_2026-09-14.md` (S5 Text, line 7). Its section 5 is "Internal inconsistencies between draft, supplementary and pre-specification summary", not the sts-matched null. The matched null is section 5 of `notes/review_computations_2026-09-14.md`, which S3 Text calls "the review computations of 14 September".
- **Evidence**: `adversarial_review_2026-09-14.md` line 154; `review_computations_2026-09-14.md` line 341 ("## 5. The sts-matched null"); `S3_Text.md` lines 225 and 418.
- **Fix**: "review computations of 14 September, section 5"

### X2
- **Location**: S17 Table, last column, lines 1220, 1224, 1249 and 1254 (rows 839, 843, 868 and 873). Also the note, line 378 ("nine of them were quoted in the text").
- **Quote**: row 868 "cross-lag budget δ_wd ts_demean | grand mean (mean of the two runs) | … | S3_Text.md:207; supplementary.md:174"; row 839 "δ_wd ts_gsr | placebo run … | supplementary.md:163"; rows 843 and 873 "supplementary.md:163; supplementary.md:176"
- **Problem**: B21 matched intervals as strings, so this column names lines that quote a different quantity with the same numbers:
  - δ_wd's committed intervals equal δ_run's.
  - δ_means on the placebo run has the same interval on both variants.

  At 90690f4, S9 Table had no δ_wd column, S3_Text.md:207 quoted δ_run, line 163 was the ts_gsr row and line 176 the ts_demean row. As a result the column marks ten of the 39 "changes" rows as quoted (row 868 among them), while the note says nine.
- **Evidence**: `git show 90690f4:manuscript/supplementary.md` lines 159–176 (no δ_wd column). `git show 90690f4:manuscript/si/S3_Text.md` line 207: "On `ts_demean` δ_run is −0.00262 [−0.00495, −0.00037]". In `inference_revision.csv`, δ_wd's percentile intervals equal δ_run's: [−0.00495, −0.00037] (ts_demean, grand mean) and [+0.00235, +0.00363] (ts_gsr, placebo). The record's B21 outcome (lines 6346–6351) lists nine quoted "changes" quantities, without δ_wd.
- **Fix**: after '"quoted at" names the file and line of the text at 90690f4 where the committed interval was quoted.' add: "B21 matched intervals as strings, so rows 839 and 868 (δ_wd, whose committed intervals equal δ_run's) and rows 843 and 873 (δ_means on the placebo run, equal on the two variants) also carry lines that quote the other quantity." Alternatively, correct the four cells to "—", "supplementary.md:163", "—" and "supplementary.md:176".

### X3
- **Location**: line 1647 (S19 Part B, the residual's source).
- **Quote**: "Table 3 (the pair r₁ and \|q\| DiDs)"
- **Problem**: Table 3 carries the pair r₁ DiD (−0.0155) but not the pair |q| DiD. The |q| DiD (−0.0164) is quoted in Results 2 and in S3 Text §4.
- **Evidence**: `draft_v2.md` line 124 (Table 3: "pair r₁ −0.0155"; no |q|); line 100 ("Mean pair |q| fell by 0.0164"); `S3_Text.md` line 155.
- **Fix**: "Table 3 (the pair r₁ DiD)"

## C: contradictions

### C1
- **Location**: line 1605 (S19, B16b row), against line 285 (S11 note) and `draft_v2.md` line 152 (Results 7, which this row cites).
- **Quote**: "AR(1) residual 0.996 in band, r₁ 0.76"
- **Problem**: The AR(1)-whitened series' r₁ is 0.76 here but 0.75 in S11's note and in Results 7 ("AR(1) residuals keep r₁ = 0.75"). None of the three says which r₁ it is: 0.76 is the run-level value, 0.75 the W = 60 value. The revision of 25 September fixed the same labelling in S3 Text (U2, "a run-level r₁ of 0.76 (0.75 at W = 60)").
- **Evidence**: S11 Table line 292 (from `whitened_spectrum_tables.md`): run-level +0.7572, W = 60 +0.7506. Record line 5496: "run-level r₁ 0.7572 (W = 60, DMT windows 1–4: 0.7506)".
- **Fix**: "AR(1) residual 0.996 in band, run-level r₁ 0.76"

### C2
- **Location**: line 1612 (S19, B21 (d) row).
- **Quote**: "the ratio +0.951 [+0.617, +0.991] on ts_gsr (met) and +0.987 [+0.901, +1.069] on ts_demean"
- **Problem**: These are subject-bootstrap percentile intervals of the disattenuated ratio, which has no per-subject vector. They are printed without the "percentile" mark that the head note (line 3) requires. S3 Text §5 labels the same interval as percentile, and the main text as "(subject bootstrap)". Read by the head note, an unmarked interval is an inverted sign-flip interval. This is the same kind of error as C10 of 25 September.
- **Evidence**: `inference_revision_tables.md` lines 359–360 (bootstrap 95 % CI of the disattenuated ratio); `S3_Text.md` line 161 ("subject-bootstrap percentile interval [+0.62, +0.99]"); `draft_v2.md` line 102.
- **Fix**: "the ratio +0.951 [+0.617, +0.991] (percentile) on ts_gsr (met) and +0.987 [+0.901, +1.069] (percentile) on ts_demean"

## T: text

### T1
- **Location**: line 339 (S13 Table note).
- **Quote**: '(record, "Stage B of round 16: the shortened text", 23 September 2026)'
- **Problem**: This is a process label ("Stage B of round 16") in a manuscript file, which the brief counts as an error. The verification of 25 September (T5, V49) kept it because it is the record heading's verbatim title. Elsewhere the paper cites entries by date and time, which avoids the label.
- **Evidence**: `analysis_record.md` line 6571.
- **Fix**: "(record, the entry of 23 September 2026, 21:40 UTC, on the shortened text)"

## U: uncertain

### U1
- **Location**: line 21 (S2 Table note).
- **Quote**: "Sign is negative in every cell against the pre-specified positive direction."
- **Problem**: Besides the FD row (line 30), which the 25 September verification accepted, three difference cells are positive: +0.0667 (line 29, ts_demean, windows 5–14), and +0.0052 and +0.1065 (line 35, ts_gsr and ts_demean, windows 5–14). The sentence is probably meant for the sts correlations only.
- **Evidence**: `primary_b_ts_demean_win60.csv` lines 64 and 70; `primary_b_ts_gsr_win60.csv` line 70.
- **Fix** (if wanted): "The sts correlations are negative in every cell, against the pre-specified positive direction."

### U2
- **Location**: line 376 ("of where the text of 23 September 2026 quoted each committed percentile interval") and line 380 (column header "quoted in the text of 23 September 2026 (file:line at 90690f4)").
- **Problem**: The text at 90690f4 is identical to 0b8d1a4's (21 September): `git diff 0b8d1a4 90690f4 -- manuscript/` is empty. S12–S16 call that text "the drafts of 21–22 September", while S8's note (line 153) uses "The main text of 23 September 2026" for the shortened text (526090d). The same name thus covers two texts: `draft_v2.md:89` is Table 2's DMT row at 90690f4 but the S8 sentence at 526090d. The "at 90690f4" disambiguates, hence U.
- **Fix**: "of where the drafts of 21–22 September (the text at 90690f4) quoted …", and in the header "quoted in the drafts of 21–22 September (file:line at 90690f4)".

### U3
- **Location**: lines 334 and 336 (S13 Table).
- **Quote**: "| — W = 60 estimator / global fit | −0.042 / −0.068 |" beside "| — W = 60 estimator / global fit (B17b) | −0.0940 / −0.1046 |"
- **Problem**: The B17 values appear at three decimals, with no stated reason, while the adjacent B17b row and S10 Table (lines 196–197: −0.0422, −0.0675) use four. The values are correct at their precision; this is reported only because the brief asks for the same precision everywhere.
- **Fix** (if wanted): "−0.0422 / −0.0675"

## Coverage

**Read in full**: every line of `supplementary.md` in the wrapped copy (head note, S1–S16, the S17 source, note and header, S18, S19, S20). S17's 932 data rows were checked by program.

**Checked against files**:
- **S1–S8**: `results/primary_b_*` (W60, W30), `regional_analysis_*`, `regional_did_map_*`, `lz_vs_tdmi_*`, `global_fc_did_*` (including per-bin ranges), `proportionality.csv`, `regional_sts_r1_tables.md`, and every interval against `inference_revision.csv` (inverted).
- **S9**: the three cross-lag files and B21, cell by cell.
- **S10, S11 (spectrum part), S18**: row by row by program against the calibration, whitened-spectrum, B23 and B24 tables.
- **S11–S15**: `prewhiten_tables.md`, `diag_tables.md`, `lag_tables.md`, B21 (a), (b) and (d), and the phase p of `inference_rows_raw.csv` and `inference_rows_ccs_pub.csv`.
- **S13**: `residual_source.log`, `sts_matched_null_F3.log`, B23 (b)/(e) and B24.
- **S16**: the F1–F3 logs.
- **S17**:
  - every cell of all 932 rows against the CSV: 0 mismatches except the zero signs of N2;
  - 12 rows recomputed from the pickles (mean, p, t interval): all agree;
  - all note statistics recomputed;
  - the 202 quoted-at entries analysed for co-located matches, which found X2.
- **S19**:
  - the tally (58 rows = 25 + 13 + 14 + 6) against the closing sentence and the main text;
  - every outcome number against the record and the tables (log-det constants recomputed);
  - dates via `git log -S`.
- **S20**: diffed against `notes/partB5_literature_v2.md` (only the stated replacements and escaped pipes differ); values checked against `family_checks.log`, S18 (d), the ideal band-pass formula, and review computations §3.
- **Shared with the main text and S Texts**: Table 2 and 3, Results 2–7, and S1/S3 Text quotations. All "value [lo, hi]" strings across the seven files were also cross-indexed: no interval shared by two values, no point outside its interval, no swapped endpoints.

**Cross-references checked exhaustively**:
- every S Text § and "section" pointer;
- every S Table, Table, Fig, Results and Methods heading pointer (existence);
- every record entry title or date-time (against the headings);
- every commit identifier (resolved in `git log`, dates checked);
- every backticked path (all exist);
- every author–year citation (reference list, or S20's own two entries);
- S heading against caption, for all 20.

**Checked by sample**: the content behind S19's "reported at" pointers (most rows).

**Markdown**: `tablecheck.py` found 0 bad rows. Brackets, backticks, bold and quotes are balanced. Also checked: hyphen-minus in numbers, "r1", "pair a", "post-hoc", "Lempel-Ziv", doubled words and process labels (only line 339). The 25 September fixes (N3, T3, T6, T7, X8, X10, C8–C10, U5, U7, V6, V19–V27, V33) are in place.

**Pending placeholders**: wording and cross-references only, per the brief; no errors found.

**Not checked**: external works (page numbers and quotations in S20, Luppi et al. 2022 Table 1 values), and anything needing subject data.
