# Run-level mean cross-lag deviation (partB10_crosslag_deviation.py; git=9a19b10; seed=20261120)

Per subject and run, over the 2 × 6,555 deviations corr(x_t, y_(t+1)) − a_y q and corr(y_t, x_(t+1)) − a_x q of the run-level 4 × 4 correlation matrices (all finite TRs of the run; a_x, a_y and q as in partB4_diagnostic.py): (1) the signed mean, (2) the sign(q)-weighted mean, mean of sign(q) × deviation, (3) the OLS slope of the deviation on q across pairs. Predictions recorded before the runs (analysis_record.md): for (1), the pre-run entry of 15 Sep 2026 15:35 UTC (negative on ts_gsr and near zero on ts_demean if pooling of non-stationary segments explains the run-level residual; near zero on both otherwise); for (2) and (3), the entry "The sign(q)-weighted cross-lag deviation: pre-run entry, 15 Sep 2026" (if pooling operates as described, (2) on ts_gsr is positive and of order +0.006; near zero or far below that, pooling does not account for the run-level residual). 'Near zero' = subject-bootstrap 95 % CI includes zero. The three statistics share one set of bootstrap draws per variant; the signed mean's numbers are those reported at 152cc6d.

Family check of the sign convention (symmetric AR(1) pair, a = 0.85, both cross-lag entries displaced by d): sts(q = +0.25, d = +0.0188) = 1.23142 = sts(q = −0.25, d = −0.0188) = 1.23142, against sts(q = −0.25, d = +0.0188) = 1.30246 and 1.25883 at d = 0; so sign(q) × d > 0 is what lowers sts below the AR(1) prediction. At q = +0.25 a deviation of +0.006 gives a residual of -0.0103 (the ≈ −0.01 run-level residual on ts_gsr); at q = −0.25 the same +0.006 gives +0.0120.

Population check of the common-slow-component identity (added 16 Sep 2026; x = s + n_x, y = ±s + n_y, λ = var(s)/var(x), equal regional variances; the true cross-lag correlation is ±λ a_s, the AR(1) substitution gives a_y q with a_y = λ a_s + (1 − λ) a_n and q = ±λ): λ = 0.25, a_s = 0.95, a_n = 0.8, loading +1: q = +0.250, d = +0.028125, λ(1 − λ)(a_s − a_n)·sign = +0.028125; λ = 0.25, a_s = 0.95, a_n = 0.8, loading -1: q = -0.250, d = -0.028125, λ(1 − λ)(a_s − a_n)·sign = -0.028125; λ = 0.1, a_s = 0.9, a_n = 0.85, loading +1: q = +0.100, d = +0.004500, λ(1 − λ)(a_s − a_n)·sign = +0.004500; λ = 0.1, a_s = 0.9, a_n = 0.85, loading -1: q = -0.100, d = -0.004500, λ(1 − λ)(a_s − a_n)·sign = -0.004500; λ = 0.4, a_s = 0.8, a_n = 0.9, loading +1: q = +0.400, d = -0.024000, λ(1 − λ)(a_s − a_n)·sign = -0.024000; λ = 0.4, a_s = 0.8, a_n = 0.9, loading -1: q = -0.400, d = +0.024000, λ(1 − λ)(a_s − a_n)·sign = +0.024000.

## ts_gsr

Signed mean cross-lag deviation: DMT +0.00009, PCB +0.00009; grand mean +0.00009 [+0.00005, +0.00013] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0004, positive in 13/14 subjects; r(statistic, run-level residual) across the 28 runs -0.277. SD of the deviation across pairs within a run 0.0390; mean absolute deviation 0.0312. Run-level residual of the diagnostic on the same runs: -0.0137 (-1.1 % of observed 1.2883). Mean pair a 0.8666, mean pair |q| 0.1945.
Per-subject signed mean deviation (two runs): [ 3.75264e-05  7.15375e-05  2.19891e-05  2.66087e-04  9.34147e-05  1.57059e-04 -1.70303e-05  1.25757e-04  2.05576e-04  7.91719e-05  3.42781e-05  1.53955e-04  3.10311e-05  8.60420e-06]
Reading under the pre-run entry of 15:35 UTC: positive.

Share of pairs with q < 0: 0.545 (DMT 0.543, PCB 0.546); mean deviation among the q > 0 pairs +0.00384, among the q < 0 pairs -0.00304 (descriptive).
Sign(q)-weighted mean cross-lag deviation: DMT +0.00381, PCB +0.00299; grand mean +0.00340 [+0.00300, +0.00380] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, run-level residual) across the 28 runs -0.767.
Per-subject sign(q)-weighted mean deviation (two runs): [0.00337 0.00200 0.00316 0.00440 0.00279 0.00453 0.00350 0.00386 0.00459 0.00245 0.00258 0.00372 0.00304 0.00361]
Reading under the pre-run entry for this statistic: positive and of the order required (within a factor of two of +0.006): consistent with pooling as the source of the run-level residual.
Slope of the deviation on q across pairs (OLS, per run): DMT +0.0184, PCB +0.0142; grand mean +0.0163 [+0.0141, +0.0187] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, run-level residual) across the 28 runs -0.545.
Per-subject slope (two runs): [0.0163 0.0095 0.0144 0.0244 0.0137 0.0248 0.0151 0.0180 0.0209 0.0101 0.0131 0.0174 0.0141 0.0166]
Reading: positive.

## ts_demean

Signed mean cross-lag deviation: DMT -0.00753, PCB -0.00723; grand mean -0.00738 [-0.00902, -0.00588] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 0/14 subjects; r(statistic, run-level residual) across the 28 runs -0.890. SD of the deviation across pairs within a run 0.0415; mean absolute deviation 0.0337. Run-level residual of the diagnostic on the same runs: +0.0008 (+0.1 % of observed 1.2205). Mean pair a 0.8567, mean pair |q| 0.2544.
Per-subject signed mean deviation (two runs): [-0.00890 -0.00631 -0.00775 -0.00567 -0.00676 -0.00454 -0.00484 -0.00705 -0.00863 -0.01276 -0.00414 -0.00889 -0.01393 -0.00316]
Reading under the pre-run entry of 15:35 UTC: negative.

Share of pairs with q < 0: 0.196 (DMT 0.162, PCB 0.230); mean deviation among the q > 0 pairs -0.00582, among the q < 0 pairs -0.01441 (descriptive).
Sign(q)-weighted mean cross-lag deviation: DMT -0.00324, PCB -0.00199; grand mean -0.00262 [-0.00495, -0.00037] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0532, positive in 5/14 subjects; r(statistic, run-level residual) across the 28 runs -0.969.
Per-subject sign(q)-weighted mean deviation (two runs): [-0.00559 -0.00065 -0.00046 -0.00090  0.00046  0.00245  0.00035 -0.00172 -0.00725 -0.00902  0.00188 -0.00828 -0.01042  0.00253]
Reading under the pre-run entry for this statistic: negative (CI excludes zero): the mechanism's signature is absent and the deviation has the sign that raises sts above the prediction.
Slope of the deviation on q across pairs (OLS, per run): DMT +0.0228, PCB +0.0193; grand mean +0.0211 [+0.0194, +0.0227] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, run-level residual) across the 28 runs -0.289.
Per-subject slope (two runs): [0.0216 0.0161 0.0207 0.0238 0.0192 0.0256 0.0204 0.0232 0.0274 0.0171 0.0183 0.0221 0.0169 0.0223]
Reading: positive.

## A. W = 60 (addition of 16 Sep 2026)

Per window, exactly as partB4_diagnostic.py (kept TRs in [60w, 60(w + 1)); PairPhiID on the window; a_x, a_y, q and the sign of q from the window's own matrices): the signed mean, the sign(q)-weighted mean and the OLS slope of the 2 × 6,555 deviations on q; averaged over the run's 14 windows; inference as at the run level (bootstrap draws from a separate generator seeded 20261120). Rule recorded before the run (analysis_record.md, pre-run entry of 16 Sep 2026): if pooling of non-stationary segments is the source, the ts_gsr W = 60 value should be markedly smaller than the run-level value (read as below half of it); if comparable (within a factor of two), a stationary mechanism is indicated and pooling is not distinguished by run length. r(·, residual) uses the W = 60 residual of the diagnostic per run (diag_series_<variant>_W60.npz, mean over windows).

### ts_gsr (W = 60; 392 windows checked against diag_series xcorr_dev)

Share of pairs with q < 0 (window q): 0.515; mean deviation among the q > 0 pairs +0.00643, among the q < 0 pairs -0.00581; mean pair a 0.8596, mean pair |q| 0.2774; W = 60 residual of the diagnostic -0.0489 (descriptive).
W = 60 signed mean cross-lag deviation: DMT +0.00013, PCB +0.00014; grand mean +0.00014 [+0.00010, +0.00018] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, W = 60 residual of the diagnostic, mean over the run's windows) across the 28 runs -0.283.
W = 60 sign(q)-weighted mean cross-lag deviation: DMT +0.00615, PCB +0.00608; grand mean +0.00611 [+0.00563, +0.00665] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, W = 60 residual of the diagnostic, mean over the run's windows) across the 28 runs -0.635.
Per-subject W = 60 sign(q)-weighted mean deviation (two runs): [0.00573 0.00539 0.00524 0.00819 0.00614 0.00746 0.00527 0.00717 0.00694 0.00557 0.00514 0.00684 0.00544 0.00505]
Reading under the rule of 16 Sep 2026: comparable to the run-level +0.00340 (ratio 1.80, within a factor of two): a stationary mechanism is indicated and pooling is not distinguished by run length.
W = 60 slope of the deviation on q across pairs (OLS per window, mean over windows): DMT +0.0205, PCB +0.0198; grand mean +0.0201 [+0.0184, +0.0222] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, W = 60 residual of the diagnostic, mean over the run's windows) across the 28 runs -0.416.

### ts_demean (W = 60; 392 windows checked against diag_series xcorr_dev)

Share of pairs with q < 0 (window q): 0.275; mean deviation among the q > 0 pairs -0.00303, among the q < 0 pairs -0.01649; mean pair a 0.8504, mean pair |q| 0.3229; W = 60 residual of the diagnostic -0.0378 (descriptive).
W = 60 signed mean cross-lag deviation: DMT -0.00651, PCB -0.00696; grand mean -0.00674 [-0.00820, -0.00537] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 0/14 subjects; r(statistic, W = 60 residual of the diagnostic, mean over the run's windows) across the 28 runs -0.888.
W = 60 sign(q)-weighted mean cross-lag deviation: DMT +0.00108, PCB +0.00212; grand mean +0.00160 [-0.00019, +0.00326] (subject bootstrap, 10000 draws), exact sign-flip p = 0.1061, positive in 9/14 subjects; r(statistic, W = 60 residual of the diagnostic, mean over the run's windows) across the 28 runs -0.779.
Per-subject W = 60 sign(q)-weighted mean deviation (two runs): [-0.00151  0.00345  0.00330  0.00458  0.00463  0.00566  0.00301  0.00270 -0.00063 -0.00328  0.00435 -0.00402 -0.00361  0.00377]
Ratio to the run-level value -0.00262: -0.61 (no rule for this variant).
W = 60 slope of the deviation on q across pairs (OLS per window, mean over windows): DMT +0.0236, PCB +0.0238; grand mean +0.0237 [+0.0219, +0.0255] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects; r(statistic, W = 60 residual of the diagnostic, mean over the run's windows) across the 28 runs +0.029.

## B. The finite-sample null of notes/review_v2_residual_null.py (addition of 16 Sep 2026)

Regenerated from the null's own functions, generator (seeded 20261120 at import) and call sequence; its construction sets the population cross-lag correlation to exactly r1·q (one filter per pair, shared by the pair's two series). Per pair-window: the two deviations from the window's a_x, a_y, q; sign(q)-weighted mean = mean of sign(q) × deviation, averaged over the pair's windows, then mean over pairs ± SE across pairs; slope = OLS of the deviation on q across the pairs of each window index, mean over window indices ± SE across them. Rule recorded before the run (analysis_record.md, pre-run entry of 16 Sep 2026), at W = 840 against the run-level ts_gsr value: near zero (|value| below a tenth of it) removes finite sampling as a source of the signature; comparable (at least half of it) means the statistic is not diagnostic; in between, reported as the share finite sampling produces, neither branch claimed.

Homogeneous-filter check (placebo ACF; 2,000 pairs × 8,400 TRs per window length), as the null's first section; its log reports residual −8.52 %, −3.10 %, −0.34 % at W = 30, 60, 840:
W = 30: residual -0.0886 (-8.52 %); share of pair-windows with q < 0 0.503, mean |q| 0.354; sign(q)-weighted mean deviation +0.00662 ± 0.00008 (SE; 95 % [+0.00647, +0.00677]); signed mean +0.00000 ± 0.00005; slope on q +0.0169 ± 0.0001 over 280 window indices
W = 60: residual -0.0373 (-3.10 %); share of pair-windows with q < 0 0.505, mean |q| 0.291; sign(q)-weighted mean deviation +0.00348 ± 0.00007 (SE; 95 % [+0.00335, +0.00361]); signed mean +0.00000 ± 0.00005; slope on q +0.0107 ± 0.0001 over 140 window indices
W = 840: residual -0.0045 (-0.34 %); share of pair-windows with q < 0 0.516, mean |q| 0.222; sign(q)-weighted mean deviation +0.00025 ± 0.00005 (SE; 95 % [+0.00015, +0.00034]); signed mean +0.00000 ± 0.00005; slope on q +0.0012 ± 0.0001 over 10 window indices

Operating-point cells (W = 60; 3,000 pairs × 50 windows each), as the null's second section; its log reports residual −0.0353, −0.0313, −0.0350, −0.0364 and a DiD of +0.0054:
DMT pre: residual -0.0353 (-2.99 %); share of pair-windows with q < 0 0.496, mean |q| 0.280; sign(q)-weighted mean deviation +0.00344 ± 0.00007 (SE; 95 % [+0.00330, +0.00357]); signed mean -0.00015 ± 0.00006; slope on q +0.0112 ± 0.0002 over 50 window indices
DMT post: residual -0.0313 (-2.77 %); share of pair-windows with q < 0 0.507, mean |q| 0.268; sign(q)-weighted mean deviation +0.00311 ± 0.00007 (SE; 95 % [+0.00297, +0.00325]); signed mean -0.00007 ± 0.00007; slope on q +0.0106 ± 0.0002 over 50 window indices
PCB pre: residual -0.0350 (-3.00 %); share of pair-windows with q < 0 0.502, mean |q| 0.285; sign(q)-weighted mean deviation +0.00325 ± 0.00007 (SE; 95 % [+0.00311, +0.00339]); signed mean -0.00006 ± 0.00006; slope on q +0.0102 ± 0.0001 over 50 window indices
PCB post: residual -0.0364 (-3.02 %); share of pair-windows with q < 0 0.499, mean |q| 0.283; sign(q)-weighted mean deviation +0.00356 ± 0.00007 (SE; 95 % [+0.00342, +0.00369]); signed mean -0.00001 ± 0.00006; slope on q +0.0114 ± 0.0002 over 50 window indices
Null residual DiD +0.0054 (log: +0.0054). Mean of the four cells' sign(q)-weighted mean deviation +0.00334 ± 0.00004 (SE).

Reading under the rule of 16 Sep 2026 (W = 840 against the run-level ts_gsr value): near zero (|+0.00025| below a tenth of the run-level +0.00340; share +0.073): finite sampling is removed as a source of the signature.
At W = 60 (descriptive, no rule): null +0.00348 (homogeneous filter) and +0.00334 (four cells) against the data's ts_gsr W = 60 value +0.00611.

