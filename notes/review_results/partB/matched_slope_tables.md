# The per-subject slope under a pure autocorrelation change of the data's heterogeneity (partB28_matched_slope.py)
git=13e7299

B17b's band-passed generator (β̄ = 185.4, σ_q = 0.2637; window-level mean a 0.8628, |q| 0.2828 on the check draw), 14 subjects × 2 runs × 300 pairs × 840 samples; the DMT run's post parameters β̄_s per subject so that its window-level mean a is 0.8632 + Δa_s, Δa_s the subject's whole-brain r₁ DiD rescaled to mean -0.0150 (Δa_s: -0.0165, -0.0025, -0.0267, -0.0205, +0.0005, -0.0191, -0.0086, -0.0657, -0.0319, -0.0206, -0.0147, -0.0082, -0.0003, +0.0248; the generator's floor is Δa = -0.0375, below which subjects [8] are set to it; β̄_s: 99, 172, 52, 80, 188, 87, 138, 6, 30, 80, 108, 140, 184, 351; the check draws give a − 0.8632 of -0.0163, -0.0018, -0.0269, -0.0207, +0.0010, -0.0189, -0.0086, -0.0376, -0.0318, -0.0204, -0.0146, -0.0083, +0.0001, +0.0248). B17's AR(1) generator (a_x, a_y ~ N(0.85, 0.0125), q from the data's window-level pair q, burn-in 200): the subject's change is exactly Δa_s on both coefficients. (i) and (iii) the step at sample 300; (ii) and (iv) the ramp from sample 300 to 420. W = 60; DiD = windows 6–14 minus 1–4, DMT minus placebo; the slope = OLS of the residual DiD on the pair-a DiD across the 14 subjects (intercept free), with its 95 % t interval (12 df); 100 replicates per condition; seed 20261120.

The data (ts_gsr, W = 60): slope -0.753 [-1.133, -0.373] per unit of whole-brain r₁ DiD, r = -0.780; ratio of means -0.788 per unit of whole-brain r₁ DiD (the main text's −0.74 is per unit of pair r₁).

| condition | slope: mean ± SD | slope percentiles 2.5 / 50 / 97.5 | share of replicates with slope ≤ the data's | r: mean ± SD | r percentiles 2.5 / 50 / 97.5 | share with r ≤ the data's | per-replicate ratio of means: mean ± SD | its percentiles 2.5 / 50 / 97.5 | ratio of the replicate-mean DiDs | slope intervals containing that ratio; containing 0 | residual DiD | sts DiD | pair-a DiD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (i) band-passed, step | -0.200 ± 0.091 | -0.407 / -0.205 / -0.012 | 0.000 | -0.591 ± 0.204 | -0.856 / -0.627 / -0.044 | 0.190 | -0.167 ± 0.077 | -0.311 / -0.174 / -0.008 | -0.167 | 0.91; 0.30 | +0.0022 ± 0.0010 | -0.0741 ± 0.0026 | -0.0131 ± 0.0004 |
| (ii) band-passed, ramp | -0.185 ± 0.096 | -0.360 / -0.176 / -0.025 | 0.000 | -0.501 ± 0.209 | -0.797 / -0.526 / -0.081 | 0.070 | -0.173 ± 0.101 | -0.366 / -0.173 / +0.005 | -0.174 | 0.95; 0.51 | +0.0020 ± 0.0012 | -0.0670 ± 0.0028 | -0.0117 ± 0.0003 |
| (iii) AR(1), step | -0.355 ± 0.087 | -0.513 / -0.354 / -0.179 | 0.000 | -0.731 ± 0.122 | -0.904 / -0.751 / -0.428 | 0.370 | -0.349 ± 0.129 | -0.588 / -0.345 / -0.115 | -0.351 | 0.97; 0.05 | +0.0049 ± 0.0019 | -0.0402 ± 0.0031 | -0.0138 ± 0.0008 |
| (iv) AR(1), ramp | -0.375 ± 0.094 | -0.580 / -0.363 / -0.227 | 0.000 | -0.706 ± 0.109 | -0.863 / -0.727 / -0.447 | 0.280 | -0.339 ± 0.139 | -0.550 / -0.343 / -0.072 | -0.343 | 0.96; 0.06 | +0.0042 ± 0.0019 | -0.0362 ± 0.0029 | -0.0123 ± 0.0008 |

One change for every subject, at W = 60: B17b's (i) residual DiD +0.0027 ± 0.0014 (calibration_filtered_tables.md), B17's (i) +0.0049 ± 0.0017 (calibration_tables.md); the data's residual DiD +0.0115 and r₁ DiD −0.01465 (whole-brain), −0.0155 (pair).

## Reading under the rule of the pre-run entry

The entry's predictions (the generators' slopes more negative than their ratios of means; the data's slope against the central 95 % of each condition's slopes; the ramps' residual DiDs against the steps') are read against the table in the outcome entry, and Results 4 and the Discussion state the per-subject scaling as the rule of the entry says.
