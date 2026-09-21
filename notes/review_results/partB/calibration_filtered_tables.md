# Calibration of the residual diagnostic on the band-passed generator (partB17b_calibration_filtered.py)
git=106bd33

Generator of review_v2_residual_null.py: smooth 0.0064–0.080 Hz band-pass (0.004 Hz cosine edges) with tilt exp(−β f²) applied to two white noises of correlation q, circularly over the run's 840 samples; per pair β ~ N(β̄, 0.5 β̄) (clipped below at 5), q ~ N(0, σ_q) (clipped to ±0.95). Solved once on calibration draws of 3000 pairs × 3000 samples (W = 60): β̄ = 185.4 (window-level mean a 0.8637, target 0.8632), σ_q = 0.2637 (mean |q| 0.2844, target 0.2842), β̄_post = 105.7 (mean a 0.8483, target 0.8482), δ = 82.6 (mean a_x − a_y 0.0300, target 0.03); held fixed. N_PAIRS = 300 pairs per subject, 14 subjects × 2 runs × 840 samples; the DMT run's white noises filtered at the pre and at the post parameters (β scaled by β̄_post/β̄) and spliced at sample 300; (ii): x_t ← x_t + c y_(t−1), y_t ← y_t + c x_(t−1) on the post samples, each post segment rescaled to its SD before the coupling; (iv): x at β + δ, y at β − δ. W = 60; bins of 30; 50 replicates per condition; bootstrap 1000 draws; sign-flip exact over 2^14; seed 20261120. DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo, mean over subjects; ± is the SD over replicates. At the global fit the run-level prediction (constant across a run's bins; its DiD is zero and the residual DiD equals the observed DiD) and the period-level prediction ((a_x, a_y, q) measured on the pre and the post samples separately) are both tabulated, as in B17.

| condition | estimator | sts level (pre) | sts DiD | predicted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |
|---|---|---|---|---|---|---|---|---|
| (i) Δa (post filter) | W60 | 1.1883 | -0.0940 ± 0.0028 | -0.0966 ± 0.0027 | +0.0027 ± 0.0014 | 0.136; 0.54 | -0.00005 ± 0.00030 | +0.00641 ± 0.00104 |
| (i) Δa (post filter) | global (run-level prediction) | 1.3262 | -0.1046 ± 0.0035 | +0.0000 ± 0.0000 | -0.1046 ± 0.0035 | 0.000; 1.00 | — | — |
| (i) Δa (post filter) | global (period-level prediction) | 1.3262 | -0.1046 ± 0.0035 | -0.1089 ± 0.0030 | +0.0043 ± 0.0020 | 0.116; 0.62 | — | — |
| (ii) Δc = +0.01 | W60 | 1.1878 | +0.0001 ± 0.0029 | -0.0002 ± 0.0025 | +0.0003 ± 0.0011 | 0.464; 0.04 | +0.00025 ± 0.00031 | -0.00021 ± 0.00096 |
| (ii) Δc = +0.01 | global (run-level prediction) | 1.3349 | -0.0003 ± 0.0034 | -0.0000 ± 0.0000 | -0.0003 ± 0.0034 | 0.494; 0.08 | — | — |
| (ii) Δc = +0.01 | global (period-level prediction) | 1.3349 | -0.0003 ± 0.0034 | -0.0002 ± 0.0024 | -0.0002 ± 0.0021 | 0.459; 0.06 | — | — |
| (ii) Δc = +0.02 | W60 | 1.1878 | +0.0002 ± 0.0025 | +0.0004 ± 0.0026 | -0.0002 ± 0.0012 | 0.517; 0.04 | +0.00045 ± 0.00024 | -0.00002 ± 0.00103 |
| (ii) Δc = +0.02 | global (run-level prediction) | 1.3353 | -0.0001 ± 0.0034 | +0.0000 ± 0.0000 | -0.0001 ± 0.0034 | 0.569; 0.02 | — | — |
| (ii) Δc = +0.02 | global (period-level prediction) | 1.3353 | -0.0001 ± 0.0034 | -0.0000 ± 0.0028 | -0.0001 ± 0.0020 | 0.477; 0.04 | — | — |
| (ii) Δc = +0.03 | W60 | 1.1883 | -0.0009 ± 0.0028 | -0.0005 ± 0.0026 | -0.0004 ± 0.0012 | 0.453; 0.06 | +0.00069 ± 0.00024 | -0.00018 ± 0.00096 |
| (ii) Δc = +0.03 | global (run-level prediction) | 1.3361 | -0.0010 ± 0.0041 | -0.0000 ± 0.0000 | -0.0010 ± 0.0041 | 0.440; 0.16 | — | — |
| (ii) Δc = +0.03 | global (period-level prediction) | 1.3361 | -0.0010 ± 0.0041 | -0.0005 ± 0.0028 | -0.0005 ± 0.0022 | 0.390; 0.08 | — | — |
| (ii) Δc = −0.02 | W60 | 1.1879 | -0.0002 ± 0.0026 | +0.0000 ± 0.0024 | -0.0002 ± 0.0012 | 0.469; 0.04 | -0.00044 ± 0.00030 | +0.00019 ± 0.00077 |
| (ii) Δc = −0.02 | global (run-level prediction) | 1.3354 | -0.0004 ± 0.0039 | -0.0000 ± 0.0000 | -0.0004 ± 0.0039 | 0.422; 0.14 | — | — |
| (ii) Δc = −0.02 | global (period-level prediction) | 1.3354 | -0.0004 ± 0.0039 | -0.0004 ± 0.0027 | -0.0000 ± 0.0019 | 0.518; 0.04 | — | — |
| (iii) Δa and Δc = +0.02 | W60 | 1.1875 | -0.0944 ± 0.0026 | -0.0971 ± 0.0026 | +0.0027 ± 0.0011 | 0.115; 0.50 | +0.00060 ± 0.00031 | +0.00645 ± 0.00092 |
| (iii) Δa and Δc = +0.02 | global (run-level prediction) | 1.3255 | -0.1055 ± 0.0028 | +0.0000 ± 0.0000 | -0.1055 ± 0.0028 | 0.000; 1.00 | — | — |
| (iii) Δa and Δc = +0.02 | global (period-level prediction) | 1.3255 | -0.1055 ± 0.0028 | -0.1091 ± 0.0024 | +0.0036 ± 0.0014 | 0.132; 0.44 | — | — |
| (iv) a_x − a_y = 0.03 with Δa | W60 | 1.1668 | -0.0889 ± 0.0026 | -0.0920 ± 0.0027 | +0.0031 ± 0.0012 | 0.064; 0.62 | -0.00002 ± 0.00028 | +0.00592 ± 0.00108 |
| (iv) a_x − a_y = 0.03 with Δa | global (run-level prediction) | 1.2526 | -0.0913 ± 0.0028 | -0.0000 ± 0.0000 | -0.0913 ± 0.0028 | 0.000; 1.00 | — | — |
| (iv) a_x − a_y = 0.03 with Δa | global (period-level prediction) | 1.2526 | -0.0913 ± 0.0028 | -0.1014 ± 0.0028 | +0.0101 ± 0.0016 | 0.001; 1.00 | — | — |

## Population reference for B17's AR(1) conditions (closed form at the drawn (a_x, a_y, q); 20000 draws of B17's distributions and its Q_POOL; post = (a_x − 0.015, a_y − 0.015) with the innovation correlation held as B17 holds it)

| condition | population sts, pre | population sts, post | population change | B17 W60 level (pre) | B17 W60 sts DiD | B17 global level (pre) | B17 global sts DiD |
|---|---|---|---|---|---|---|---|
| (i) | 1.1936 | 1.1121 | -0.0816 | 0.7152 | -0.0422 | 1.1317 | -0.0675 |
| (iv) | 1.1474 | 1.0699 | -0.0775 | 0.7131 | -0.0422 | 1.1127 | -0.0677 |
| (iv) − (i), pre level | -0.0463 | — | — | -0.0021 | — | -0.0190 | — |

Predictions recorded (pre-run entry, B17b): the W = 60 sts level near the null's 1.18 rather than B17's 0.715; under (i) the sts DiD between −0.07 and −0.10 (the data's is −0.0809) and the residual DiD near the data's own null, +0.004 to +0.008; (ii) residual negative for either sign of Δc; (iii) additive; (iv) level lowered, residual near its (i) value; the population reference for B17 (i): a change of about −0.08 (1.19 → 1.11), and for (iv) − (i) a level difference of about −0.045. Rule: where B17 and B17b differ, the main text quotes B17b (the generator closer to the data) and S3 Text carries both; the finite-sample null of Results 4 is superseded by B17b where they overlap; the null's own DiD (+0.0054, review_v2_residual_null.log) is quoted beside B17b's (i). Each condition's row is read against these in the outcome entry.
