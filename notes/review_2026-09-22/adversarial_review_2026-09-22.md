# Referee report

**Manuscript:** "The Gaussian-MMI synergy atom of integrated information decomposition is mostly self-prediction: a closed form on the AR(1) family, a per-pair diagnostic, and a within-subject DMT fMRI test" (`manuscript/draft_v2.md`, repository `dmt-phiid` at commit 0b8d1a4), submitted as a Methods article to *PLOS Computational Biology*.

**Referee date:** 22 September 2026.

**Scope and independence.** I read the main text in full, S1–S5 Text and `manuscript/supplementary.md`. I checked numbers against `results/` and `notes/review_results/`, and mathematical claims against `notes/rev_phiid_fast.py`. I opened `manuscript/analysis_record.md` and `manuscript/prespecification_summary.md` only to check claims about what was recorded when. I did not open `notes/review_2026-09-20/`, any `notes/` file whose name contains review/adversarial/audit/plan/defence/companion (including the review appendices that S3 cites as sources for some numbers), or anything outside the repository. The raw time series are not in the repository, so every data check below uses saved per-subject arrays (`did_subjects` in `notes/review_results/inference_rows_*.pkl`, the `partB` csv/npz files). My check scripts are in `scratchpad/refcheck/` (`var1.py`, `popresid.py`, `popdelta.py`, `winsim.py`, `winsim2.py`, `persub.py`). As instructed, I treated the [TK] items, the pending final run and the figure PDFs as out of scope.

---

## (i) Overall judgement

**Major revision, close to reject-and-resubmit.** The analytic core is correct. I reproduced the sixteen-atom closed form on the symmetric AR(1) family to machine precision, along with the q = 0 identity for unequal coefficients, the aggregate identity, the exchange rates and the coupled-family values. On this dataset the evidence that whole-brain MMI-sts moves with lag-1 autocorrelation is convincing: the closed form, the cross-half analysis, the lag series and the regional correlation all point the same way. That part deserves publication.

The paper then claims considerably more than it shows:

- **The residual diagnostic (claim d) is wrong as stated.** The conclusion the abstract builds on it, that "a coupling change of either sign would have lowered" the residual and so "the data carry no evidence of a change in lagged interaction", is an artefact of how the calibration parameterises coupling. Under the paper's own matched coupled family (Results 1, Fig 2c) the effect reverses. It also reverses in a generator-free population calculation and in a W = 60 simulation that reproduces the paper's calibration rows. The "bound" for sign(q)-aligned coupling uses a statistic that the paper's own S9 Table declares superseded, and on the sensitivity variant that statistic is significant in the residual-raising direction.
- **The "prediction" is not a prediction.** It is the same plug-in estimator applied to the same window matrices with two of six correlations replaced, so its agreement with the observation (r = 0.99) is largely built in.
- **The "confirmatory" test was specified after a same-data global fit had already shown the decrease** (DiD −0.075; per-subject DiDs correlating 0.95 with the windowed ones). The main text does not say this, although S5 does.
- **Several recommendations to the field contradict the paper's own numbers:** CCS "does not follow r₁", the run-level fit is preferable, prewhitening "is not a remedy", and the per-pair diagnostic "says how much of a synergy contrast autocorrelation accounts for".

A revision that keeps (a) and (b), states the provenance of the confirmatory test plainly, withdraws or properly calibrates (d), and rewrites the recommendations would be a solid, much shorter Methods paper.

---

## (ii) The three most serious problems, in order

1. **The residual diagnostic's central inference is reversed by a change of generator (Findings 1–4).** The claims that a coupling change of either sign lowers the residual, that the residual's rise is "in the direction that no coupling change produces", that its excess "is not attributable to coupling", and that "the data carry no evidence of a change in lagged interaction" all hold only for the calibration's generator. That generator adds a VAR(1) cross-coefficient with the innovation covariance fixed, so each 0.01 of coupling also shifts every pair's lag-0 correlation (by about +0.036 in mean window-level q). The GSR data cannot show such a shift and do not.
   - With coupling changed at fixed (r₁, q), as in the paper's own coupled family, the residual *rises* for either sign: +0.0065 at |Δc| = 0.02 at W = 60, and +0.0036 to +0.015 in population for |δ| = 0.01 to 0.02.
   - Sign(q)-aligned coupling, and the weakening of a shared slow component that the paper says is indistinguishable from coupling at τ = 1, move the residual at first order. A decrease produces exactly the observed rise, in proportion to the r₁ fall.
   - The "bound" on the aligned case uses the window-sign statistic that S9 Table supersedes for selection bias. On ts_demean that statistic's DiD is −0.0039 [−0.0063, −0.0014], p = 0.013, in the residual-raising direction.
   - The calibration also fails to reproduce the data's residual–Δr₁ relation (slope −0.75 [−1.13, −0.37] against an implied −0.18 to −0.37).
   - The calibration's pre-registered coupling prediction (first order) failed, and the direction argument was built afterwards.

2. **Circular "prediction" and a confirmatory label the record does not support (Findings 5–6).**
   - The abstract's "change predicted from each pair's measured autocorrelations and lag-0 correlation" (−0.092 against −0.081), the r = 0.99 across subjects and "no free parameter" are the estimator evaluated twice on the same 4×4 window matrices. The two versions differ only in the cross-lag entries.
   - The per-subject regression of the sts DiD on the r₁ DiD has slope 4.26 [3.41, 5.12] and intercept −0.018 [−0.039, +0.002]. The closed-form rate (6.07) and the band-passed generator's rate (6.27) both lie outside that slope interval.
   - The one "confirmatory" statistic was written 56 minutes after a same-data global fit of the same contrast had been committed.
   - The estimator account was built after the result, on the same data; the abstract's "We test it ... with one confirmatory contrast" misstates this.

3. **Headline quantitative statements and recommendations contradict the paper's own results (Findings 7–9).**
   - "A ratio of 2 to 1 per standard deviation" mixes a group-averaged regional SD with a single-window pair SD. Like-for-like it is 4.7:1 by the closed form and 1.4–1.7:1 empirically.
   - The windowed estimator's sensitivity to |q| is 2.5 times the closed-form rate.
   - CCS-sts correlates with group-mean r₁ at −0.64, and its DMT contrast changes sign under AR(1) prewhitening (−0.0057, p = 0.0065).
   - The run-level fit manufactures +29 % in the most data-like matched pair.
   - "Prewhitening is not a remedy" rests on an AR-order cap of 5 that BIC hit in 3,218 of 3,220 series, with no atoms computed at higher orders.

---

## (iii) Findings

Severity: fatal / major / minor / presentation. Class: VERIFIED ERROR / UNSUPPORTED / JUDGEMENT / PRESENTATION. Line numbers refer to `manuscript/draft_v2.md`.

### Finding 1. The residual's response to a coupling change depends on the generator; under the paper's own coupled family it reverses

- **Severity:** fatal to claim (d) as stated; major for the paper.
- **Class:** VERIFIED ERROR.

**Location.**
- Abstract (l. 15): "leaves a residual that a coupling change of either sign would have lowered, with its calibrated expectation inside its interval: the data carry no evidence of a change in lagged interaction."
- Results 4 (l. 118): "A coupling change (ii) lowers the residual for either sign of Δc ... roughly as Δc², because the first-order response of sts to c is odd in q and averages out over pairs of either sign of q."
- Results 4 (l. 120): "A coupling change applied independently of sign(q) lowers the residual, quadratically and for either sign of Δc, so it cannot raise it above the pure-autocorrelation expectation ... Its excess over that expectation is not attributable to coupling."
- Discussion (l. 199): "The residual's change is therefore in the direction that no coupling change produces."

**Problem.** The calibration (B17) adds a VAR(1) cross-coefficient while holding the innovation covariance at its baseline value. Coupling therefore also moves each pair's lag-0 correlation and lag-1 autocorrelation. The diagnostic's prediction uses the measured (a_x, a_y, q), follows those moves, and rises. The observed sts barely changes (Table 7: sts DiD about 0; predicted DiD +0.0020 to +0.0110). That is why the residual falls.

The sign therefore reflects the parameterisation, not lagged interaction as such. When coupling changes at fixed (r₁, q) — the construction the paper itself uses to show "what lagged interaction does" (Results 1, l. 48; Fig 2c; Methods l. 239) — the prediction does not move. sts is convex in the cross-lag departure (curvature +40 per unit c², S3 §3), and the residual *rises* for either sign.

**Checks.**
- **Generator-free, population** (`refcheck/popdelta.py`). The paper's own non-separability argument (l. 239: every positive-definite lag-0/lag-1 structure is a VAR(1)) makes the population residual at fixed (r₁, q) a function of the cross-lag departure alone. I took the closed form (`atoms_from_corr` on `ar1_corr` with δ added to both cross-lag entries), a = 0.85, and q ~ N(0, 0.342), which is the data's window-level q, sign-symmetric as on ts_gsr.
  - A uniform δ of +0.01 and −0.01 raises the pool-mean residual by +0.0036 and +0.0037.
  - A uniform δ of ±0.02 raises it by +0.0154 and +0.0158; the result is similar at a = 0.8632.
  - An aligned departure δ·sign(q) moves it at first order: −0.0224 per +0.01 and +0.0297 per −0.01.
- **Coupled family, (r₁, q) held** (`refcheck/popresid.py`, Results 1's construction with a and the innovation correlation re-solved per pair). The pool-mean population residual is +0.0029 at c = +0.01, +0.0102 at +0.02 and +0.0070 at −0.02.
- **Finite sample, W = 60** (`refcheck/winsim.py`, `winsim2.py`). I used 40,000 pair-windows per condition, VAR(1) with population r₁ = 0.85, phyid-style past/future standardisation, and the prediction exactly as in `partB4_diagnostic.py` (l. 73–75).
  - With coupling parameterised as in B17, my simulation reproduces Table 7's AR(1) rows: residual changes of −0.0011, −0.0049, −0.0113 and −0.0052 at Δc = +0.01, +0.02, +0.03 and −0.02, against the paper's −0.0010, −0.0052, −0.0109 and −0.0055. Observed sts is unchanged and the prediction rises.
  - In that parameterisation the mean window-level q shifts by +0.036 per 0.01 of c.
  - With coupling at matched (r₁, q), a uniform Δc of +0.02 and −0.02 raises the residual by +0.0066 and +0.0064 (SE 0.0002). An aligned Δc of +0.01 lowers it by 0.0102; an aligned Δc of −0.01 raises it by 0.0135.
- **The calibration's coupling alternative does not match what the primary data can show.** It moves the whole lag-0 correlation distribution (≈ +0.07 in mean q at Δc = 0.02). On ts_gsr, global signal regression removes any such global shift (S7 Table: mean-correlation DiD −0.0034), and mean |q| moved by only −0.016. A coupling change in the underlying signals would therefore reach the GSR data with most of its lag-0 shift removed, which is closer to the matched parameterisation than to the calibration's. The matched alternative predicts the sign the data show.
- **A weakening of a shared slow component reproduces the data's pattern.** The paper states this alternative is indistinguishable from lagged coupling at τ = 1 (l. 239; S3 §3). Model: x = s + n_x, y = ±s + n_y, λ = 0.25, a_n = 0.84, a_s falling from 0.90 to 0.87. Then:
  - Δr₁ = −0.0075;
  - the aligned cross-lag departure falls from 0.0113 to 0.0056;
  - the population residual rises from −0.0186 to −0.0096 (+0.0090).
  The residual rise is proportional to the r₁ fall, which is exactly the relation the data show (Finding 3).

**Consequence.** The residual DiD (+0.0115; +0.0182 on ts_demean) is compatible with three explanations the data do not separate:
- a pure autocorrelation change under a generator the calibration does not match (Finding 3);
- a sign-independent lagged-coupling change at roughly fixed lag-0 structure;
- a weakening of sign(q)-aligned lagged structure or shared slow drive.

"Not attributable to coupling" is false, and "no evidence of a change in lagged interaction" is not supported.

**Resolution.** Withdraw the direction argument and the "no evidence" sentence from the abstract, Results 4 and the Discussion, and state that the residual cannot presently discriminate these alternatives. If an inference is wanted, calibrate over the relevant parameterisations on the band-passed generator, at perturbation sizes that actually move δ, and report the diagnostic's power:
- coupling with innovations fixed;
- coupling at matched (r₁, q);
- sign(q)-aligned coupling;
- a shared slow component with Δλ or Δa_s.

### Finding 2. The "bound" on sign(q)-correlated coupling uses a statistic the paper's own SI declares superseded; on the sensitivity variant it is significant in the residual-raising direction

- **Severity:** major.
- **Class:** VERIFIED ERROR (internal inconsistency).

**Location.**
- Results 4 (l. 120): "a coupling change correlated with sign(q) would move it at first order, and that statistic's own DMT contrast bounds it — the sign(q)-weighted mean cross-lag departure has a DiD of −0.0012 [−0.0029, +0.0006], p = 0.22, at this estimator and variant."
- Discussion (l. 199): "while one correlated with sign(q) is bounded by its own contrast."

**Checks.**
- The quoted DiD comes from `notes/review_results/partB/directed_crosslag_tables.md` ("partB10's W = 60 statistic, for reference"). It is computed in `notes/partB15_directed_crosslag.py` (l. 121) as `(np.sign(qw) * symw).mean()`, where `qw` is the window's own lag-0 correlation.
- Its level in `directed_crosslag.csv` is +0.006112 (ts_gsr) and +0.001601 (ts_demean). These are exactly the "window-sign" values that S9 Table lists as "superseded ... because the window's sign selects on the same samples as the deviation (about half of +0.00611 is that selection: the null's +0.00348)".
- No DiD of a selection-free version exists in any result file: neither δ_60 with the run-level sign (level +0.00245 in `crosslag_budget_tables.md`) nor the slope of d on q per window.
- The same statistic on ts_demean has DiD −0.00390 [−0.00633, −0.00137], p = 0.0128 (`directed_crosslag_tables.md`, l. 32). A negative value is the direction that *raises* the residual (S3 §6 convention). This value is not reported in the main text.
- The aligned case is the empirically relevant one. The baseline cross-lag departure is aligned with q: δ_run is +0.0034 (14 of 14 subjects), and the slope of d on q is +0.0163 at run level and +0.0201 at W = 60 (14 of 14; `crosslag_deviation_tables.md`).
- Even taken at face value, the ts_gsr interval's lower limit (−0.0029) at the family's conversion (S9: +0.006 → −0.0103) admits about +0.005 of residual DiD. That is roughly half the excess over the band-passed expectation (0.0088).

**Consequence.** By the paper's own logic, either the statistic is invalid (and there is no bound), or it signals a change in aligned cross-lag structure on the sensitivity variant (and the conclusion fails there).

**Resolution.** Compute, calibrate and report on both variants the DiD of a selection-free aligned statistic (run-level-sign δ per window, or the per-window slope of d on q), and drop "bounds".

### Finding 3. The calibration does not reproduce the data's residual–Δr₁ relation, and the "inside the interval" comparison is a low-power non-rejection

- **Severity:** major.
- **Class:** UNSUPPORTED (numbers VERIFIED).

**Location.** Abstract ("with its calibrated expectation inside its interval"); Results 4, ¶¶2–3; Table 4, last row; Table 7.

**Checks** (per-subject DiDs from `inference_rows_diag.pkl` and `inference_rows_raw.pkl`; `refcheck/persub.py`).
- **Across subjects, the residual DiD scales with the r₁ DiD.**
  - ts_gsr: slope −0.753, t-CI [−1.133, −0.374], bootstrap [−1.01, −0.46], leave-one-out range −0.79 to −0.70; intercept +0.0005 [−0.0086, +0.0096].
  - ts_demean: slope −0.568 [−1.048, −0.088].
- **The group ratios agree across splits:** residual/Δr₁ is 0.79 for the primary set (0.0115/0.0146), 0.84 for the early set (0.0179/0.0213) and 0.69 for the late set (0.0064/0.0093).
- **The calibrated generators imply much shallower ratios:** 0.0027/0.015 = 0.18 (band-passed), 0.33 (AR(1)), and 0.37 for the finite-sample null (+0.0054 at Δr₁ = −0.0146). The data's slope is 2–4 times steeper, and the band-passed and AR(1) ratios lie outside its confidence interval.
- **The relation is not only shared window noise.** Across halves, r(residual_even, r₁_odd) = −0.70 (`splithalf.log`).
- **The calibration has no between-subject heterogeneity.** It applies one Δa to every subject, so its replicate SD (0.0014) is about 1/3.6 of the data's between-subject SE (0.0051).
- **Against the preferred expectation (+0.0027), the exact sign-flip p is 0.108** (t-test 0.108). Against +0.0049 it is 0.22, and against +0.0054 it is 0.25. The data carry weak evidence of an excess, not none.
- **On the preferred (band-passed) generator the diagnostic is insensitive to coupling:** Table 7's (ii) rows are +0.0003 to −0.0004, because that construction injects about a thirtieth of the lagged structure. The diagnostic's power against coupling on the generator the text prefers was therefore never established.

**Resolution.** Draw per-subject Δa from the data's distribution; report the generator's residual–Δr₁ slope beside the data's; report power against the alternatives listed in Finding 1. If no generator reproduces a slope near −0.75, say that the calibration is not validated for this dataset.

### Finding 4. Calibration pre-registration: failed predictions and rule departures are missing from the deviation list, and the generator used for the direction argument is not at the data's operating point

- **Severity:** major.
- **Class:** UNSUPPORTED / PRESENTATION (record checked).

**Location.**
- Methods, "Pre-registration and deviations" (l. 275): "The deviations — the diagnostic's branch rule replaced by the calibrated reference, a write-up weighting rule withdrawn, a split-half rule whose threshold lay above the reliability ceiling — are stated where they arise and listed in S5 Text."
- Results 4 (l. 118): "14 subjects × 2 runs × 840 samples of 300 pairs at the data's operating point."

**Record checks.**
- **B17 pre-run entry (record, 20 Sep 19:07 UTC):** "(ii) residual ≈ −1.77 Δc at the global fit (first order), smaller in magnitude at W = 60." Under that prediction a coupling *decrease* raises the residual. The B17 outcome entry records (ii) as "wrong in form" (quadratic, the same sign for both Δc). The direction argument was built on this failed prediction afterwards.
- **B17b pre-run rule:** "where B17 and B17b differ, the main text quotes B17b." For the (ii) rows the main text quotes B17; S3 §7 acknowledges "a departure from the rule".
- **B17b's (ii) prediction**, "residual negative for either sign of Δc" (made after B17 had been seen), was not met: all rows are within 1 SD of zero.
- **B17b's (i) prediction** (+0.004 to +0.008) was missed (+0.0027).
- None of these appears in the main text's deviation list or in S5 §2–3.

**Operating point of the AR(1) generator.** In my simulation, an AR(1) at population a = 0.85 has window-level r₁ at W = 60 of 0.788 (SD 0.085), against the data's 0.848 (window scatter ≈ 0.03). Its W = 60 sts level is 0.715 against 1.155. The authors themselves reject this generator for the level and the exchange rate (B17 outcome: "these exchange rates are the family's, not the data's"), yet its (ii) rows carry the direction argument.

**Resolution.** Add these items to the deviation list. Correct "at the data's operating point" for the AR(1) generator. State in Results 4 that the direction reading was constructed after the pre-registered prediction failed.

### Finding 5. The per-pair "prediction" is the same estimator evaluated twice on the same matrices; its agreement with the observation is largely built in

- **Severity:** major.
- **Class:** UNSUPPORTED.

**Location.**
- Abstract: "the change predicted from each pair's measured autocorrelations and lag-0 correlation was −0.092".
- Results 2 (l. 78): "The sts change predicted from each pair's measured (a_x, a_y, q) alone, with no free parameter, is −0.0924 ... per subject the predicted and observed DiDs correlate at r = 0.99 (Fig 3b)".
- Results 1 (l. 50): "The family reproduces the structure".
- Author summary: "the apparent fall in synergy was predicted, in sign and size, by the fall in autocorrelation".
- Discussion (l. 199).

**Problem.**
- The windowed "observed" sts is the plug-in of each window's 4×4 sample correlation matrix through the same Gaussian-MMI map (`rev_phiid_fast.py`, validated against phyid to about 1e-14).
- The "prediction" evaluates that map on the same matrix after replacing the two cross-lag entries with a_y q and a_x q and the two lag-0 entries with their mean (`partB4_diagnostic.py`, l. 73–75).
- Both are computed from the same windows, and the prediction contains the measured changes in a_x, a_y and q. Agreement up to the cross-lag contribution is therefore guaranteed, and r = 0.99 reflects shared inputs rather than validation.
- The same applies to Table 1's "the family reproduces the structure". At W = 60 the window-level asymmetry is mostly sampling noise (≈0.03 per member against a between-region SD of 0.0125), and both columns take the MMI minimum of the same noisy estimates.
- The prediction also includes the q and asymmetry changes, so "predicted ... by the fall in autocorrelation" is inaccurate.

The informative evidence lies elsewhere: the map projection, the cross-half correlation, the lag series and the calibration's rate.

**Check.** Regression across subjects of the observed sts DiD on the r₁ DiD:
- ts_gsr: slope 4.26 [3.41, 5.12]; intercept −0.0184 [−0.0390, +0.0021], p = 0.074;
- ts_demean: slope 4.92 [3.99, 5.85]; intercept +0.003.

The closed-form 6.07 and the band-passed generator's 6.27 per unit lie outside the ts_gsr slope interval. At N = 14, the per-subject data cannot exclude that about a fifth of the ts_gsr contrast does not scale with Δr₁.

**Resolution.** Call it what it is (for example, "the AR(1)-substituted estimate"). Drop "prediction", "no free parameter" and Fig 3b as validation. If a prediction is wanted, predict each subject's held-out-half sts DiD from the other half's r₁ DiD through a calibrated rate.

### Finding 6. The "confirmatory" label and the abstract's "We test it" misstate the history; the record shows the test statistic was written after an equivalent same-data estimate had been seen

- **Severity:** major.
- **Class:** UNSUPPORTED / PRESENTATION (checked against the record).

**Location.**
- Abstract: "We test it on within-subject fMRI ... with one confirmatory contrast ..., which began as a planned directional test recorded before the primary analysis."
- Methods (l. 251, l. 275): "The up-regulation hypothesis, the windowed estimator, window sets, nulls and motion rule were recorded before the primary windowed result existed; the directional-failure rule was written after a 115-region global fit had shown a decrease, and the post set was moved".
- Limitations (l. 215).
- Results 4 (l. 120): "the pre-specified 'near zero' reading of the diagnostic obtains once the reference is the calibrated expectation rather than zero".

**Record.**
- `prespecification_summary.md` dates the "Step-contrast test and motion handling" to b7e4595 (13 Sep 11:36).
- The 115-region global fit ("Difference-in-differences −0.075 nats ... The direction is a DECREASE") is at 33f0b33 (10:40; on disk 10:15 according to S5).
- The record (l. 721–723) states that "The step contrast had no test on record" until that entry.
- S5 concedes: "the direction and approximate size of the effect were known from the global fit, whose per-subject DiDs correlate at 0.95 with the windowed ones". The initial commit also carried a 20-region fit that was negative in 12 of 14 subjects.
- The main text mentions only the directional-failure rule and the post-set change.
- The estimator account ("it") was derived after the result, on the same data (Introduction l. 29). No part of the account was tested confirmatorily.
- The "near zero" branch did not obtain as pre-specified: the residual was significant against zero and correlated with r₁ at −0.78. Declaring that it "obtains" after changing the reference is a post hoc reinterpretation.

**Verifiability.** The copy I received is a shallow clone rooted at 553e919 (13 Sep 15:51 +0300), which already contains `results/primary_b_ts_gsr_win60.csv`. None of the earlier SHAs the paper relies on (44cec4f, e16ebba, 33f0b33, b7e4595, e46df8a, febf599, cb1b2cf) is present, so I could not verify the ordering. The record itself says the hypothesis and the first fit "entered git together, in the initial commit".

**Resolution.**
- State in the abstract and in Methods that the test statistic was specified after a same-data global-fit estimate of the same contrast had been seen.
- Describe the windowed DiD as a replication across estimators rather than a confirmation.
- Say that the account is post hoc on the same data.
- Delete "obtains".
- Make the full history available to reviewers.

### Finding 7. "A ratio of 2 to 1 per standard deviation" mixes incommensurable SDs, and the windowed estimator's sensitivity to |q| is 2.5 times the closed-form rate

- **Severity:** major (abstract claim).
- **Class:** VERIFIED ERROR / UNSUPPORTED.

**Location.**
- Abstract: "0.01 of r₁ moves sts by 0.061 nats and 0.1 of the lag-0 correlation |q| by 0.019, a ratio of 2 to 1 per standard deviation of the data's variation".
- Results 1 (l. 46); Discussion (l. 197).
- Results 2 (l. 78): "mean pair |q| moved by −0.016, worth 0.003 nats".

**Checks.**
- The r₁ SD (0.0125) is the between-region SD of group-averaged regional r₁ (`regional_sts_r1_tables.md`). The |q| SD (0.196) is the SD over single-window pairs of subject 1 (52,440 pair-windows, `scope_map_overlay_points.npz`).
- On those same 52,440 pair-windows, the pair-r₁ SD is 0.029. The closed-form per-SD ratio is then 4.7:1.
- An OLS fit of observed sts on (r₁, |q|) over those pair-windows gives 5.48 per unit r₁ (close to the closed form) and **−0.47 per unit |q|, 2.5 times the closed-form −0.19**. The standardised coefficients are 0.73 and −0.43.
- The paper's own all-window regression (`exchange_rates_tables.md` (b)) gives standardised coefficients +0.661 (r₁), −0.463 (|q|) and −0.426 (asymmetry). These are not in the main text; r₁ alone gives R² = 0.462 against 0.808 for all three.
- B19's recorded prediction ("|a_x − a_y| carrying the difference") is logged as "met", although |q| carries as much as asymmetry.
- At the empirical rate, the |q| DiD is worth about 0.0075 nats (≈ 9 % of the sts DiD), not 0.003.

**Resolution.** Report per-SD ratios with like-for-like SDs, at both window level and group level. Put the empirical partial slopes and standardised coefficients in the main text. State that the finite-sample estimator's dependence on |q| exceeds the population rate (the level residual correlates with |q| at about −0.4 to −0.5 within windows, `diag_tables.md`).

### Finding 8. CCS: "does not follow autocorrelation" contradicts the paper's own numbers, and the "mechanical reading" is an accounting identity

- **Severity:** major.
- **Class:** UNSUPPORTED (numbers VERIFIED).

**Location.**
- Results 6 heading and l. 163: "Under CCS redundancy the synergy atom is near zero and does not follow autocorrelation".
- l. 165: "The increase has a mechanical reading".
- Recommendations (l. 211): "Use CCS as the comparison whose synergy atom is near zero and does not follow r₁".

**Checks.**
- **Group level:** across the 28 condition × window means, CCS-sts correlates with mean r₁ at −0.639 (`ccs_pub_tables.md`).
- **Subject level:** the per-subject DiD correlates with the r₁ DiD at −0.420, −0.275, −0.428 and −0.297 — all four negative.
- **Under prewhitening** (`inference_rows_prewhiten.pkl`), the CCS-sts DiD on ts_gsr W = 60 is:
  - −0.0057 [−0.0094, −0.0022], p = 0.0065, 12 of 14 negative, after AR(1) whitening, which leaves r₁ at 0.75;
  - −0.0135, p = 0.016, after AR(p) whitening;
  - against +0.0044 on the raw series.
  A mild filter reverses the sign of the contrast.
- **The decomposition is an identity.** CCS-sts = −(1 − s)c̄_rej is exact to 1e-18 and would split any change, real or artefactual. Calling it a "mechanical reading" implies an artefact without demonstrating one. The mechanical reading the paper's own numbers do suggest — CCS-sts tracks r₁ inversely — is not considered.
- CCS-sts is negative (−0.048) and has split-half reliability 0.30.

**Resolution.**
- Replace "does not follow autocorrelation" with the observed pattern.
- Test whether the change in c̄_rej is reproduced by the AR(1)-substituted CCS from (a_x, a_y, q).
- Report the AR(1)-whitened CCS result in the main text.
- Withdraw or heavily qualify the CCS recommendation.

### Finding 9. The remedies and recommendations are not supported by the paper's own results

- **Severity:** major.
- **Class:** UNSUPPORTED.

**Run-level fit** (l. 180: "The run-level fit is preferred ... on manufacture grounds (Table 8)"; Recommendations l. 211).
- In the most data-like matched pair (VAR(1) at a = 0.87) the 840-sample fit manufactures **+29 %** (+0.0236 ± 0.0023, `sts_matched_null_F2.log`), against +7 % ± 8 % at W = 60. In the pair built on the data's own ACF (F3-b) the figures are +2 % and −8 % ± 6 %.
- The W = 60 figures that favour the global fit (−9 % and +16 %) come from the F1 pairs, whose analytic sts is 0.094 nats (`sts_matched_null_F1.log`) — an order of magnitude below the data's regime.
- The global fit's period-level residual is biased under a pure autocorrelation change (+0.0089 on AR(1), +0.0043 band-passed) and under asymmetry (+0.0101; p < 0.05 in 100 % of replicates; S10 Table).
- For CCS-sts, the global fit's pre-injection gap between runs (DMT −0.0358 against placebo −0.0230, a difference of 0.0128) is five times the windowed estimator's gap (−0.0480 against −0.0454, 0.0026). That is consistent with the run-level covariance, which includes the drug period, contaminating the pre-injection bins. (For MMI-sts the two gaps agree: 0.019 against 0.018.)

**Prewhitening** (abstract: "prewhitening is not a remedy on band-passed data"; Recommendations: "the sts contrast on it is still predicted by that residual autocorrelation").
- BIC selected the cap (p = 5) in 3,218 of 3,220 series, and no atoms were computed at p = 10 or p = 20.
- AR(p) whitening removed 81 % of the level (1.155 → 0.22) and 68 % of the contrast (−0.081 → −0.026, p = 0.14).
- The per-subject r between the whitened sts DiD and the whitened r₁ DiD is +0.495 (`prewhiten_tables.md`), so "still predicted" is weak.
- The defensible statement is narrower: prewhitening *after* band-pass filtering cannot whiten without amplifying the stop-band residue, so it must precede filtering.

**The diagnostic** (author summary: "the per-pair diagnostic we provide, which says how much of a synergy contrast autocorrelation accounts for"). Its prediction includes q and asymmetry, and its residual cannot yet be interpreted (Findings 1–3).

**The recommended null** (l. 211: "use one that preserves each region's autocorrelation and removes the cross-correlations"). On the family this null sits at q = 0, where sts is at its maximum for a given r₁. Comparing against it tests lag-0 correlation, not lagged interaction. The relevant null preserves the auto-spectra and the zero-lag cross-correlation but not the lagged cross-structure.

**Resolution.** Rewrite Results 7 and the Recommendations so that they claim only what the tables show.

### Finding 10. The regional result depends on the grouping chosen; the residual map keeps network structure; rtr is not "almost unmoved"

- **Severity:** minor.
- **Class:** JUDGEMENT (numbers VERIFIED).

**Location.**
- Abstract: "its sensory–association contrast vanishes when r₁ is partialled out".
- Results 3 (l. 112): "every network mean of the residual map lies within ±0.024 nats".
- Discussion (l. 205): "higher r₁ gives higher sts with rtr almost unmoved".

**Checks** (`regional_partial.csv`).
- **SomMot − Default:** the r₁ contrast is +0.001, and the sts contrast is −0.0066 before and −0.0097 after partialling (it grows).
- **Vis − Default:** +0.0087 after partialling.
- **Residual network means** run from −0.0235 (subcortex) to +0.0207 (DorsAttn). That range (0.044) is twice the contrast that "vanishes". A one-way ANOVA across the eight classes gives F = 8.2 (descriptive; parcel-level; spatial autocorrelation ignored).
- **Cortex only:** Pearson r = 0.807, against 0.863 with the 16 subcortical parcels included, which sit at the low end of both maps.
- **rtr against r₁:** r = +0.638 across regions, a slope of about 0.50 nats per unit r₁. That is eight times the family's ∂rtr/∂r₁ = 0.06.
- The cited sensorimotor-to-association hierarchy (Raut; Ito) is not visible in these network r₁ means: SomMot 0.8493 ≈ Default 0.8484, and Vis is lowest.

**Resolution.** Report alternative groupings (SomMot vs Default; a continuous unimodal–transmodal gradient), add a spin-based test of residual network structure, correct the rtr statement, and temper "vanishes" and "follows".

### Finding 11. "Most exposed dataset" (Luppi et al., 2022) is a units artefact of ∂sts/∂r₁

- **Severity:** minor.
- **Class:** VERIFIED ERROR (reasoning).

**Location.** Discussion (l. 207): "By the map it would be the most exposed dataset in the table: at its stated TR of 0.72 s and 0.008–0.09 Hz band the ideal-band-pass r₁ is ≈ 0.97, where ∂sts/∂r₁ = 32.8 against ∂rtr/∂r₁ = 0.06".

**Check.** I took two regions whose in-band spectra (0.008–0.09 Hz) differ only by a tilt exp(−βf²), with β = 100, 200 and 400 against β = 0, and computed closed-form sts at q = 0.25.

| β | Δsts at TR 0.72 s | Δsts at TR 2 s | Δr₁ at TR 0.72 s | Δr₁ at TR 2 s |
|---|---|---|---|---|
| 100 | +0.19 | +0.17 | 0.0053 | 0.0376 |
| 200 | +0.38 | +0.34 | 0.0097 | 0.0689 |
| 400 | +0.74 | +0.66 | 0.0158 | 0.1132 |

As r₁ → 1, 1 − r₁ scales as TR²⟨f²⟩ while ∂sts/∂r₁ scales as 1/(1 − r₁). The sts difference produced by a given regional spectral difference is therefore nearly independent of TR, and ∂sts/∂r₁ does not rank exposure across TRs.

**Resolution.** Express exposure per unit of spectral difference. This removes the ranking and in fact generalises the paper's point across TRs.

### Finding 12. The unequal-coefficient statements about the family are false for small asymmetry

- **Severity:** minor.
- **Class:** VERIFIED ERROR.

**Location.**
- Results 1 (l. 44): "for q ≠ 0 the excess sts − (xtx + yty) is negative and grows with the asymmetry, rts = str lie below xtx and yty".
- Discussion (l. 197): "with unequal coefficients MMI takes the smaller self-information, so that the atom falls below the sum of the two".

**Check** (closed form, mean coefficient 0.85).
- At q = 0.25 the excess is +0.0231 at |a_x − a_y| = 0, +0.0079 at 0.005 and −0.0072 at 0.01. It crosses zero at about 0.0076.
- At q = 0.5 it stays positive up to about 0.033 (+0.0127 at 0.03).
- The excess starts at +rtr and *decreases* with asymmetry.
- Per pair, str equals the smaller self-prediction atom and rts can exceed it. At (0.9, 0.8, 0.5): rts = 0.4023, str = yty = 0.3977.
- The abstract's "falls below the sum" holds only if "the sum" means xtx + yty + rtr.

**Resolution.** State the q-dependent threshold, correct the ordering to "str = min(xtx, yty), rts ≥ str", and make the abstract unambiguous.

### Finding 13. Inference at N = 14: intervals are too narrow, and precision and "no change" statements are overstated

- **Severity:** minor.
- **Class:** VERIFIED / UNSUPPORTED.

**Location.**
- Methods (l. 247): "so the percentile intervals stand".
- Abstract: "the two share their reliable variance across subjects (cross-half r = 0.69, ceiling 0.73)".
- "ΦR ... did not change"; "The directed component does not change".

**Checks.**
- **The percentile intervals are narrow.** t-intervals, and intervals obtained by inverting the paper's own exact sign-flip test, are 13–16 % wider for every quantity I checked. BCa corrects bias and skew, not small-sample narrowness, so a width ratio of 1.00 says nothing about coverage.

  | quantity | percentile interval (paper) | t-interval | inverted sign-flip interval |
  |---|---|---|---|
  | primary sts DiD | [−0.1261, −0.0377] | [−0.1321, −0.0297] | [−0.1313, −0.0313] |
  | residual DiD | [+0.0021, +0.0211] | [+0.0005, +0.0226] | [+0.0005, +0.0226] |
  | CCS W = 60 DiD | [+0.0004, +0.0081] | — | [−0.0001, +0.0088] |

  For CCS the exact p is 0.056: the percentile interval excludes zero where the exact test does not.
- **The cross-half correlations are imprecise.** Fisher-z intervals at N = 14: 0.694 → [0.26, 0.90]; the reliabilities 0.717 → [0.30, 0.90] and 0.741 → [0.35, 0.91]. Simulating with the observed reliabilities, a true-score correlation of 0.7 yields a disattenuated estimate ≥ 0.95 in 11 % of samples; a true-score correlation of 1 gives a 95 % range of 0.75–1.41.
- **"No change" statements are absence-of-evidence claims.** At N = 14, "did not change" and "does not change" need equivalence bounds (for example, the ΦR interval of ±0.009 against a level of 0.096).
- **The r₁ DiD fails its phase-randomised null** (p = 0.073, against 0.002 for sts; S3 §5). Table 2 reports the sts phase p but not r₁'s.

**Resolution.** Report sign-flip-inverted intervals; give intervals for the cross-half and disattenuated correlations; use equivalence language only where it has been tested; report r₁'s phase p beside sts's.

### Finding 14. Table 5 mixes autocorrelation changes that cannot be compared

- **Severity:** minor.
- **Class:** PRESENTATION (VERIFIED).

**Location.**
- Table 5 and its caption: "so the population rows exceed the estimator rows" (l. 82).
- S3 §9: "The observed autocorrelation-function change alone, at fixed q, changes the true sts by −0.069 against the observed DiD of −0.081".

**Checks.**
- The Gaussian-process row (`sts_matched_null_F3.log`, F3-c) compares the pooled placebo ACF with the post-DMT ACF: lag 1 goes from 0.868 to 0.858, **Δr₁ = −0.010**. That is a between-condition difference close to the DMT-run change (−0.0097), not the DiD (−0.0146). The row also fixes q at 0.2.
- The AR(1) row's Δa is a population change; the band-passed row's is a window-level change (the B17b entry says so).
- The caption's "population rows exceed the estimator rows" is contradicted by the band-passed rows (−0.094 and −0.105 against −0.0816), for which no population change is given.

**Resolution.** Give each row's Δr₁ at population and window level, rescale the rows to −0.0146, compare the GP row with the DMT post − pre change, and add the band-passed generator's population change.

### Finding 15. The "directed component DiD" is not a DiD

- **Severity:** minor.
- **Class:** VERIFIED ERROR (mislabel).

**Location.** Results 4 (l. 122): "The directed component does not change under DMT (its DiD +0.0004, p = 0.38), so it contributes nothing to the residual DiD."

**Check** (`directed_crosslag_tables.md`).
- The value +0.00044 (p = 0.38) is the run-level DMT − placebo difference of the directed response, over whole runs including the pre-injection windows.
- The W = 60 DiD of RMS δ_anti is +0.00631 [+0.00006, +0.01278], p = 0.083. A pure autocorrelation change on the band-passed generator reproduces this (+0.0064), and that is the argument to make.
- No W = 60 DiD of the directed response exists.

**Resolution.** Relabel the quantity, and compute and report the W = 60 DiD of the directed response.

### Finding 16. "Drug-only estimate", and the placebo drift as a vigilance confound

- **Severity:** minor.
- **Class:** JUDGEMENT / PRESENTATION.

**Location.** Results 2 (l. 78): "so the change on the DMT run alone (sts −0.0485, p = 0.027; Table 2) is the drug-only estimate". Discussion (l. 205): "under DMT as this dataset shows".

**Problem.**
- DMT post − pre contains both the drug effect and the time-in-scanner effect. Under parallel trends, the DiD is the design's drug estimate.
- The placebo run's significant rise (sts +0.0324, p = 0.0425; it carries 0.40 of the sts DiD and 0.34 of the r₁ DiD) is plausibly vigilance-related: drowsiness raises low-frequency BOLD power, and DMT prevents it.
- This does not affect the estimator account, but the "drug-only" label is wrong, and "r₁ falls under DMT" should carry the qualification.

**Resolution.** Remove "drug-only" and discuss vigilance as a component of the r₁ DiD.

### Finding 17. The literature framing in the author summary and Introduction conflicts with the paper's own applicability table

- **Severity:** minor.
- **Class:** PRESENTATION (checked against `notes/partB5_literature_v2.md`).

**Location.**
- Author summary: "Synergy has been reported ... to fall under anaesthesia and in disorders of consciousness ... We show that, with the estimator almost all of these studies use, the synergy value is mostly ... its lag-1 autocorrelation."
- Introduction (l. 25): "The studies whose settings could be read (S3 Text) use the Gaussian estimator with the MMI redundancy function ... one TR where the lag is stated (Luppi et al., 2023; Down et al., 2026)".

**Problem.**
- The anaesthesia and disorders-of-consciousness results are ΦR (Luppi et al., 2024, 2026) or discrete-CCS emergence on mean-binarised signals (Luppi et al., 2023). The paper's own Discussion says the sts result "does not carry over to ΦR".
- The table records Luppi et al. (2023)'s primary estimator as CCS on binarised data, with Gaussian and MMI used only for validation.
- Tarchi et al. (2026) does not state its redundancy function.
- Four of the nine studies deconvolve.

**Resolution.** Align the author summary and the Introduction with the table.

### Finding 18. Statements about rates, signs and terms

- **Severity:** presentation.
- **Class:** PRESENTATION / JUDGEMENT.

- **"At the stated rate"** (Discussion l. 197). Estimator rates differ by more than a factor of two for the same population change:
  - W = 60 returns 0.52 of the AR(1) population change and the global fit 0.83;
  - per 0.001 of r₁, the AR(1) generator gives −0.0028 and the band-passed generator −0.0063.
- **"Positive lagged coupling lowers the atom"** (l. 48, l. 197). This holds only for coupling of the same sign as q. At q = −0.25, c = +0.02 raises sts by +0.0435, and 54.5 % of ts_gsr pairs have q < 0.
- **"Anti-conservative"** (l. 118, l. 199). A test against zero of a statistic whose expectation is nonzero is a valid test of a false null; the problem is the choice of null, not the test's size.
- **Proportionality** (l. 80). "The less-than-proportional result is consistent with the account and is not read further" cannot be falsified as written. The period-level prediction at the global fit could test it.

**Resolution.** Reword each of these statements accordingly.

### Finding 19. Provenance of some numbers

- **Severity:** presentation.
- **Class:** PRESENTATION.

**Location.** Data availability (l. 303): "Every number in this paper is quoted from the result files of the repository — results/*.csv, the record ..., and the review and calibration result files under notes/review_results/".

**Checks.**
- The range of the finite-sample null (+0.0037 to +0.0077; Results 4 and Table 4) and its components (+0.0059, +0.0052, +0.0077, +0.0037) appear in no file under `results/` or `notes/review_results/` (grep). S3 §6 sources them to an adversarial-review appendix.
- The same holds for the partial correlations of +0.83 and +0.86 (S3 §6) and for the run-level-against-null p = 0.0001, which is sourced to a fresh-review check log.
- Trivially, the text says "reproduces phyid to ≤ 2.1 × 10⁻¹⁴", while `phiid_fast_validate.log` has a maximum of 2.21 × 10⁻¹⁴.

**Resolution.** Move these computations into scripted, committed outputs.

### Finding 20. Length and novelty framing

- **Severity:** presentation.
- **Class:** JUDGEMENT.

**Problem.**
- The main text runs to about 10,000 words with eight tables; S3 adds about 14,600 words. Much of the Results is audit trail rather than argument, and many sentences carry five or more numbers.
- The closed form is a direct Möbius inversion on a 4×4 correlation matrix. Varley (2024) gave the aggregate identity and the disintegration result, and Barrett (2015) the dynamical example.
- The distinctive contributions are the atom-level map, the operating-point and exchange-rate analysis, and the DMT illustration.

**Resolution.** A paper of roughly half the length, centred on (a) and (b), with the diagnostic presented as exploratory and its limits stated, would serve PLOS CB readers better.

---

## Appendix A. Claims I checked and found correct

- **Symmetric AR(1) family.** The six cross-prediction atoms are 0. xtx = yty = rts = str = S − C (0.617863); the mirror atoms are −(S − C); rtr = C (0.023104); sts = 2S − C (1.2588306); TDMI = 2S. The identities sts − (xtx + yty) = rtr, str + stx + sty + sts = S and ΦR = rtr all hold. Checked against `rev_phiid_fast` to about 1e-16.
- **q = 0 with unequal coefficients.** sts = 2 min(S_x, S_y), rtr = 0, and the aggregate forward synergy equals min(S_x, S_y).
- **Exchange rates at (0.85, 0.25).** ∂sts/∂a = 6.0705, ∂sts/∂q = −0.1892, asymmetry rate −3.09 per unit; |∂sts/∂r₁| > |∂sts/∂q| everywhere except r₁ = 0 (analytically, the ratio is at least 1).
- **Coupled family** (re-solved Lyapunov construction). sts = 1.2315, 1.2155, 1.2569, 1.3023 and 1.4111 at c = +0.02, +0.05, +0.10, −0.02 and −0.05; cross-lag departure 0.9375c; ∂sts/∂c = −1.7402; cross-prediction atoms 0.
- **Band-pass values.** The ideal band-pass r₁ is 0.8174 at 0.01–0.08 Hz and TR 2 s, and 0.970 at 0.008–0.09 Hz and TR 0.72 s. ∂sts/∂r₁ = 32.8 and ∂rtr/∂r₁ = 0.06 at 0.97. The AR(1)-residual formula gives 0.754 for (0.868, 0.539). Bartlett's denominator is 3.26, i.e. about 18 effective samples per window.
- **Tables 1, 2, 3, 4, 6, 7 and 8, S8 and S10** agree with their source files: inference rows, `diag_tables`, `family_atoms_ts_gsr_W60.csv`, `lag_tables`, `calibration*_tables`, `sts_matched_null_F*.log` and `prewhiten_tables`, including the counts of negative subjects and the placebo shares.
- **Other results.** The leave-one-out refits (28), the cross-half values, the CCS decomposition terms, the prewhitening and spectrum values, and the regional correlations and partialled contrasts all agree with their source files.
- **Pre-registration disclosures.** The directional-failure rule and the change of post set are correctly described. S5's account of the history is accurate and candid; the main text is not (Finding 6).
