# Run-level mean cross-lag deviation (partB10_crosslag_deviation.py; git=13f1c6d; seed=20261120)

Per subject and run, over the 2 × 6,555 deviations corr(x_t, y_(t+1)) − a_y q and corr(y_t, x_(t+1)) − a_x q of the run-level 4 × 4 correlation matrices (all finite TRs of the run; a_x, a_y and q as in partB4_diagnostic.py): (1) the signed mean, (2) the sign(q)-weighted mean, mean of sign(q) × deviation, (3) the OLS slope of the deviation on q across pairs. Predictions recorded before the runs (analysis_record.md): for (1), the pre-run entry of 15 Sep 2026 15:35 UTC (negative on ts_gsr and near zero on ts_demean if pooling of non-stationary segments explains the run-level residual; near zero on both otherwise); for (2) and (3), the entry "The sign(q)-weighted cross-lag deviation: pre-run entry, 15 Sep 2026" (if pooling operates as described, (2) on ts_gsr is positive and of order +0.006; near zero or far below that, pooling does not account for the run-level residual). 'Near zero' = subject-bootstrap 95 % CI includes zero. The three statistics share one set of bootstrap draws per variant; the signed mean's numbers are those reported at 152cc6d.

Family check of the sign convention (symmetric AR(1) pair, a = 0.85, both cross-lag entries displaced by d): sts(q = +0.25, d = +0.0188) = 1.23142 = sts(q = −0.25, d = −0.0188) = 1.23142, against sts(q = −0.25, d = +0.0188) = 1.30246 and 1.25883 at d = 0; so sign(q) × d > 0 is what lowers sts below the AR(1) prediction. At q = +0.25 a deviation of +0.006 gives a residual of -0.0103 (the ≈ −0.01 run-level residual on ts_gsr); at q = −0.25 the same +0.006 gives +0.0120.

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

