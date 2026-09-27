# Checker B: findings on S1–S5 Text (final error-only read, 26 September 2026)

**Counts:** T 4, N 3, X 6, C 3, U 12 (28 findings).

## T: text errors

**T1**
- **Location:** `manuscript/si/S5_Text.md` line 19, and line 27 (three times).
- **Quote:**
  - Line 19: `record, "Stage B of round 16: the shortened text", 23 September 2026`
  - Line 27: `(record, "Round 14: the restructuring")`, `(record, "Stage B of round 16: the shortened text", 23 September 2026)` and `(record, "Round 17: the review of 24 September 2026 applied")`
- **Problem:** These are process labels (round, stage) in a manuscript file. They come from the record's headings.
- **Evidence:**
  - The headings are at `analysis_record.md` lines 5297 (21 Sep 15:12 UTC), 6571 (23 Sep 21:40 UTC) and 6733 (25 Sep 16:34 UTC).
  - The 25 Sep check reported this as T5. Its verification, V49, kept the titles verbatim, so the labels are still in the text.
  - S5 §4 already cites a labelled entry by date and time instead: "record, the correction entry of 23 September 2026, 15:36 UTC".
  - `supplementary.md` line 339 carries the same "Stage B of round 16" citation. That is outside these files.
- **Fix:**
  - Line 19: `record, the entry of 23 September 2026, 21:40 UTC, on the shortened text`
  - Line 27: `(record, the entry of 21 September 2026, 15:12 UTC, on the restructuring)`, `(record, the entry of 23 September 2026, 21:40 UTC, on the shortened text)` and `(record, the entry of 25 September 2026, 16:34 UTC, on the revision)`

**T2**
- **Location:** `S3_Text.md` line 245.
- **Quote:** "is about half the directed and half the symmetric part of the cross-lag departure (above)"
- **Problem:** The sentence says the residual equals half of each part. In fact the residual is the sum of the two responses, and about half of it comes from each. This typo fix was accepted but never applied.
- **Evidence:**
  - S3 line 237 gives −0.0064 + −0.0071 ≈ −0.0137.
  - `notes/review_2026-09-24/adversarial_review_2026-09-24.md` line 291: "L116: … → 'is about half directed and half symmetric'".
  - `review_verification_2026-09-24.md` line 320: "Typos. All taken: l. 116".
  - S19 Table (`supplementary.md` line 1594) uses the corrected wording.
- **Fix:** "is about half directed and half symmetric (above)"

**T3**
- **Location:** `S3_Text.md` lines 227, 233, 235 and 321.
- **Quote:**
  - Line 227: "shrinking as a and |q| fall under DMT"
  - Line 233: "solved to the data's run-level mean a, mean |q̂|"
  - Line 235: "(a 0.8666, |q| 0.1945)"
  - Line 321: "realised window-level mean a 0.8637 against a target of 0.8632" and "post-injection a 0.8483 against 0.8482"
- **Problem:** A bare "a" is used here for the measured pair lag-1 autocorrelation (the mean of a_x and a_y). In the paper's notation that quantity is pair r₁, and "pair-level a" is withdrawn. The same file writes "pair r₁" elsewhere, e.g. line 227 "where pair r₁ and |q| are higher" and line 347 "its pair r₁ (the mean of a pair's a_x and a_y)".
- **Evidence:** The labels come from the result files (`directed_crosslag_tables.md` line 9: "Mean pair a 0.8666"). S3 line 3's convention allows file labels only as copied labels, not as prose notation.
- **Fix:** Replace the "a" with "pair r₁" in each place:
  - "shrinking as pair r₁ and |q| fall under DMT"
  - "solved to the data's run-level mean pair r₁, mean |q̂|"
  - "(pair r₁ 0.8666, |q| 0.1945)"
  - "realised window-level mean pair r₁ 0.8637 against a target of 0.8632"
  - "post-injection pair r₁ 0.8483 against 0.8482"

**T4**
- **Location:** `S5_Text.md` line 23.
- **Quote:** "the file was moved out of the clone for the rest of that session"
- **Problem:** The antecedent is plural ("held `external/DMT_NCT/data/*.mat`", "ran on them there"), but the verb is singular. The record uses the same words (`analysis_record.md` B19 outcome, around line 5111), so if only one named file was moved, it should be named instead.
- **Fix:** "the files were moved out of the clone for the rest of that session"

## N: numbers

**N1**
- **Location:** `S3_Text.md` line 120.
- **Quote:** "(at c = +0.02, sts − (xtx + yty) = +0.005 while rtr = 0.028)"
- **Problem:** Both values were rounded twice. At three decimals they are +0.004 and 0.027.
- **Evidence:** `notes/review_results/partB/coupling_map_tables.md` line 12 (the c = +0.02 row) prints +0.0045 and 0.0275. A closed-form recomputation of the matched coupled family gives +0.004498 and 0.027480. The c = −0.02 values that follow (+0.059, 0.019, from +0.0586 and 0.0191) are correct.
- **Fix:** "(at c = +0.02, sts − (xtx + yty) = +0.0045 while rtr = 0.0275)"

**N2**
- **Location:** `S3_Text.md` line 349.
- **Quote:** "(the four rows give −17, −24, −22 and −24)"
- **Problem:** The fourth ratio rounds to −25.
- **Evidence:**
  - From `partB/calibration.csv` (W60, (ii) rows, means over 50 replicates), residual / δ_sym² is −0.00098/0.00758² = −17.04, −0.00516/0.01480² = −23.57, −0.01085/0.02210² = −22.22 and −0.00550/0.01495² = −24.63.
  - From S3's printed table (lines 302, 305, 308, 311) the ratios are −17.4, −23.7, −22.3 and −24.6.
  - The record's B17b outcome (line 5559) has the same error.
- **Fix:** "(the four rows give −17, −24, −22 and −25)"

**N3**
- **Location:** `S3_Text.md` line 349.
- **Quote:** "(+0.0076, +0.0148, +0.0221, −0.0150; ratios 30 to 34)"
- **Problem:** −0.0150 is the table's −0.01495 rounded a second time. At four decimals the value is −0.0149.
- **Evidence:** In `partB/calibration.csv`, the (ii) Δc = −0.02 W60 row has mean sym_did −0.01494898. S3 line 311 prints −0.01495 ± 0.00066. The record repeats −0.0150 at lines 5053 and 5558. The ratio 0.01495/0.00044 = 33.7 stays within "30 to 34".
- **Fix:** "(+0.0076, +0.0148, +0.0221, −0.0149; ratios 30 to 34)"

## X: cross-references

**X1**
- **Location:** `S1_Text.md` line 5.
- **Quote:** "which carries nothing the public source release does not (S5 Text)"
- **Problem:** S5 Text says nothing about the participant codes or about what the git history exposes.
- **Evidence:** The statement is in the record entry "Git history and the participant codes" (`analysis_record.md` lines 2766–2774: "already public in the data authors' own release, so this repository's history adds no exposure").
- **Fix:** "which carries nothing the public source release does not (record, "Git history and the participant codes")"

**X2**
- **Location:** `S2_Text.md` line 7.
- **Quote:** "The share of power inside 0.01–0.08 Hz and the run-level r₁ of the deconvolved series are in `rev_extra.log`."
- **Problem:** The committed log does not contain these values.
- **Evidence:**
  - `notes/review_results/logs/rev_extra.log` (git=d507728, committed at a75d015), section (g), lines 55–57: "deconvolution outputs not present" for both variants.
  - The values (0.7899 and 0.991; 0.7761 and 0.991) are only in the version committed at 9318997, and in `notes/review_computations_2026-09-14.md` §3 line 149 (0.866 → 0.790; 99.1 %).
- **Fix:** "… of the deconvolved series are in `notes/review_computations_2026-09-14.md`, section 3 (and in `rev_extra.log` as committed at 9318997; its regeneration at d507728 ran without the deconvolution outputs)."

**X3**
- **Location:** `S3_Text.md` line 424.
- **Quote:** "(run-level r₁ 0.866 → 0.790 on ts_gsr, about 30 % of the sts level removed, the sts contrast unchanged, −0.0782 against −0.0809 at W = 60; S2 Text)"
- **Problem:** S2 Text does not give 0.866 → 0.790. It gives whole-brain r₁ 0.848 → 0.783 (DMT pre-injection, W = 60).
- **Evidence:** `notes/review_computations_2026-09-14.md` §3, lines 149 and 276.
- **Fix:** "…; S2 Text; `notes/review_computations_2026-09-14.md`, section 3)"

**X4**
- **Location:** `S3_Text.md` line 424.
- **Quote:** "no output file holds them, since the scope map's grid stops at r₁ = 0.95"
- **Problem:** An output file does hold these values.
- **Evidence:** `notes/review_results/partB/family_checks.log` lines 12–13, at (0.97, 0.25): "d/dr1: sts +32.774 … rtr +0.064".
- **Fix:** "`partB/family_checks.log` holds them (the scope map's grid stops at r₁ = 0.95)"

**X5**
- **Location:** `S3_Text.md` line 104.
- **Quote:** "(DiD; The DMT contrast, below)"
- **Problem:** This pointer was left over from the main text's former Methods subsection "### The DMT contrast" (`draft_v2.md` at 106bd33^, line 71). In S3, "below" leads to §5 ("The DMT contrast: collinearity, leverage and the CCS contrast"), which does not define the DiD.
- **Evidence:** The DiD is defined in the main text, at the opening of Results (`draft_v2.md` line 35).
- **Fix:** "(DiD; main text, Results)"

**X6**
- **Location:** `S5_Text.md` line 15.
- **Quote:** "for the reasons the main text gives (Results 6)"
- **Problem:** Results 6 gives one reason ("a specification chosen after the results were seen"). The reasons are set out in S3 Text §5.
- **Evidence:** S3 line 217: "It is not read as a DMT finding for two stated reasons and one rule".
- **Fix:** "for the reasons S3 Text §5 gives (main text, Results 6)"

## C: contradictions

**C1**
- **Location:** `S3_Text.md` line 100 and line 104.
- **Quote:**
  - Line 100: "which is why the published values are used throughout"
  - Line 104: "all CCS values in this paper are under the published definition"
- **Problem:** Both statements leave out a stated exception: the prewhitened CCS values use `phyid`'s mask.
- **Evidence:**
  - S3 line 367: "the CCS atoms of the whitened series use `phyid`'s mask, not the published definition".
  - Main text, Redundancy functions (`draft_v2.md` line 200): "The prewhitened CCS values of S11 Table were computed with phyid's mask; every other CCS value in the paper uses the published definition."
- **Fix:**
  - Line 100: "which is why the published values are used throughout, except for the prewhitened series (section 8)"
  - Line 104: "all CCS values in this paper except the prewhitened ones (section 8; S11 Table) are under the published definition"

**C2**
- **Location:** `S3_Text.md` line 347.
- **Quote:** "an sts DiD of −0.0940 for a population Δa of −0.015"
- **Problem:** On the band-passed generator, condition (i) is not a population Δa of −0.015. It is a window-level target, and its population change is Δr₁ = −0.01629, as the same paragraph states later.
- **Evidence:**
  - B17b pre-run entry (`analysis_record.md` lines 5237–5239): "β̄_post solved so that the window-level mean a of the post period is 0.8482 (… unlike B17's population Δa)".
  - `calibration_filtered_tables.md` labels the row "(i) Δa (post filter)".
- **Fix:** "an sts DiD of −0.0940 for a window-level fall of 0.015 in pair r₁ (condition (i))"

**C3**
- **Location:** `S5_Text.md` line 7.
- **Quote:** "and were committed one by one before each was run"
- **Problem:** The five Part B plans were committed together, in one file and one commit, before any was run. Only the computations were committed one by one.
- **Evidence:**
  - `git show --stat 477cccc` (14 Sep 2026, 12:50:51 UTC): one file, `notes/partB_prespec_2026-09-14.md`.
  - The computations followed: 6c8c64e (12:55), 709415d (13:17), 24bde59 (13:43), 3781e00 (13:58) and e2d72d6 (14:24).
  - S5 §6 itself lists "477cccc (14 Sep, the Part B plans)".
- **Fix:** "and were committed together before any was run"

## U: uncertain

**U1**
- **Location:** `S3_Text.md` line 3.
- **Quote:** "The computations are numbered as the record numbers them (B1–B24, B16b, B17b), each under a pre-run entry and an outcome entry"
- **Problem:** The record never uses B1, B3 or B12. Its B2, B5 and B9 label plan items of other entries (lines 5840, 5427, 5453). The pre-run plans of B1–B5 are in `notes/partB_prespec_2026-09-14.md`, as S3 lines 124 and 227 say themselves.
- **Fix:** Say that B1–B5 are numbered and planned in `notes/partB_prespec_2026-09-14.md`.

**U2**
- **Location:** `S5_Text.md` line 29 (heading).
- **Quote:** "## 6. Every commit identifier the text of this paper rests on"
- **Problem:** The §6 list omits commit identifiers that the text names:
  - in S5 §4: 0a25aaa, 66b570e, 8554b3d and e01c836;
  - in S3 line 104: a633cc1 (external, pmediano/PhiID);
  - in the S Table source notes: ac1fdc0 (line 17), 4f7437b (line 42), dbf2311 (line 144), 9a19b10 (line 185) and f3b435d (lines 7 and 1577).
  All of them exist, except the external one.
- **Fix:** Add them to the list, or narrow the heading.

**U3**
- **Location:** `S3_Text.md` line 124.
- **Quote:** "(0 of 36,481)"
- **Problem:** No cited file holds this count; `lag_tables.md` gives percentages only. The count is only in `notes/fresh_review_2026-09-17/checks/check_A1_atoms_family.log` line 66. (The 18,336 is in `notes/partB1_scope_map.md`, item 2.)

**U4**
- **Location:** `S5_Text.md` line 23 (a pending sentence; the wording only was checked).
- **Quote:** "Each of the four comparisons passed:"
- **Problem:** The four clauses (CSV and reports; binaries; logs; figures) do not match the pre-run entry's four comparisons (`analysis_record.md` about lines 6935–6949):
  - `6_committed_compare` (CSV, md and txt);
  - `9_wrapper_compare` (B21's two files);
  - `8_binary_compare`;
  - `10_logs_figures_compare`, which covers logs and figures together.
  The wrapper comparison has no clause of its own.
- **Fix:** Join the logs and figures clauses, and add a clause for B21's two files.

**U5**
- **Location:** `S4_Text.md` line 3.
- **Quote:** "(COBIDAS, OHBM 2016; summarised in Nichols et al., 2017"
- **Problem:** "OHBM 2016" reads as an author–year citation with no reference entry.

**U6**
- **Location:** `S4_Text.md` line 78.
- **Quote:** "the subject codes of the released ratings table are stated (S1 Text)"
- **Problem:** S1 describes the codes (their form and removal) but does not state them.
- **Fix:** "described"

**U7**
- **Location:** `S4_Text.md` line 55.
- **Quote:** "S1 Text (software versions): … `phyid` at commit 6c5f2e9d…"
- **Problem:** S1 Text says "at the pinned commit" and gives no hash. The hash is in S5 §6 and in the main-text reference.

**U8**
- **Location:** `S5_Text.md` line 3.
- **Quote:** "entries dated to the day until 14 September 2026 and to the minute, UTC, from 15 September"
- **Problem:** The record heading "Git history and the participant codes, 15 Sep 2026" (line 2766) has no time. It is the only heading from 15 September on without one.

**U9**
- **Location:** `S3_Text.md` lines 282 and 284.
- **Quote:** "four specification changes (windowed sts → sixteen atoms → CCS → diagnostic residual)"
- **Problem:** The list names four specifications, which is three changes. The wording comes from the record's B7 rule (lines 2485 and 2609).

**U10**
- **Location:** `S5_Text.md` line 3.
- **Quote:** "Outside Data and code availability the main text carries no commit identifier, timestamp or file path"
- **Problem:** The main text's `phyid` reference entry (`draft_v2.md` line 298) carries "at commit 6c5f2e9d33c985efbdf875d45cb5a2a6a5cdbf44". The claim holds only if the reference list does not count as main text. The rest of the main text was scanned: no other commit identifier, no clock time, and file paths only in Data and code availability.
- **Fix:** "Outside Data and code availability and the reference list …"

**U11**
- **Location:** `draft_v2.md` line 332 (the Tarchi reference).
- **Quote:** "(read in full on 20 September 2026; a deconvolving study, see S3 Text)"
- **Problem:** S3 Text names Tarchi et al. only in a list of studies (§10, line 424). The deconvolution statement ("standard SPM methods") is in S20 Table: row 9 of Table A, and Table B item 4 (`supplementary.md` lines 1666 and 1678). So the pointer is indirect rather than wrong.
- **Fix:** "see S20 Table". The word count does not change (two words for two), and the reference list is outside the count anyway.

**U12**
- **Location:** `S5_Text.md` line 27.
- **Quote:** "the record's entries call them the writer's session and the planning session"
- **Problem:** The sentence names process labels in order to decode the record's terms. It looks deliberate (the §5 key), but the brief's rule reads as absolute. Other uses of "session" in S5 (lines 7, 23 and 27, e.g. "a separate session of the AI system") read as descriptions, not labels; "desktop session" (line 23) refers to the computer. Those were not reported.

## Coverage

**Read in full**
- S1–S5 Text: every line, from the reading copies, with quotes taken from the repository files.
- `draft_v2.md` and `supplementary.md`, for the quantities they share with the S Texts.
- The brief, and the 25 Sep findings and verification (their T5 disposition was checked).

**Numbers checked against files**
- Program-compared against source tables:
  - S3's tables: §1 (both), CCS, exchange rates, BCa with its inverted column, leave-one-out, B22 (80 cells plus the B24 column), both calibration tables and the population reference, prewhitening and whitened spectrum, network and per-subject.
  - Sources: `partB/*_tables.md`, `*.csv`, `inference_revision.csv`, `inference_rows_*.csv`.
- Recomputed:
  - the directed-response inverted intervals;
  - the RMS δ_anti bound;
  - the split-half ratio 0.8249;
  - partial r 0.831 and 0.855;
  - the CCS–r₁ correlation of −0.275;
  - the ratio range 22–146;
  - the stop-band, mixture and flat-equivalent r₁;
  - effective sample size 3.3 and 18;
  - the Fisher-z interval of r = 0.626;
  - the 20-region DiD of −0.0994 (12/14);
  - the coupled family, by an independent closed-form MMI-ΦID;
  - the residual/δ_sym² ratios and the δ_sym means.
- Double rounding:
  - a scan of the prose numbers in S1–S5 against values ending in 5 in the files each paragraph cites, and against S3's own tables;
  - the candidates checked by hand against the full-precision values. Only N1 and N3 held.
- Other sources used:
  - `rev_extra.log`, `family_checks.log`, `review_computations` §§1, 3, 5, 6;
  - `derived_r17.out`, `leave_two_out.log`, `ccs_definition_check.log`, `residual_source.log`, `diagnostic_alternatives_tables.md` (d);
  - `phir_baseline_and_slope.log`, `regional_sts_r1_tables.md`, `scope_map_overlay.csv`.

**Cross-reference classes checked exhaustively**
- Every record title quoted in S1–S5 against the headings of `analysis_record.md`. All match as prefixes, except the future outcome entry of the final run and the labelled titles in T1.
- Every commit identifier in S1–S5 against `git log`. All exist, except the external 6c5f2e9d, 77af7aa and a633cc1.
- S5 §6 dates and contents against `git show --stat`, outside the pending list.
- The S5 §1 times and quotations.
- The -dirty and nogit inventory against the file headers.
- S Table and S Text § references, and main-text section references, from the S Texts.
- Author–year citations in the S Texts against the reference lists.
- The S4 Nichols et al. 2017 entry: complete and cited.
- Process labels and "pair a" across S1–S5.

**Checked by sample**
- Quantities shared with the main text: `main_text_numbers.csv` is checked mechanically elsewhere, so not row by row here.

**Not checked, and why**
- The placeholder values of the pending run sentences (brief).
- The future record entry "The final end-to-end run of `run_all.sh` at the final commit: outcome", which does not exist yet.
- The content of external works (no web).
- Values that exist only as outputs of analyses needing subject data, where no full-precision file is committed (e.g. the spectral-centroid interval, taken as printed in `review_computations` §1).
