# Ground-truth calibration of the residual diagnostic (partB17_calibration.py)
git=f1f5fcc

N_PAIRS = 300 independent VAR(1) pairs per subject, 14 subjects × 2 runs × 840 samples, burn-in 200; a_x, a_y ~ N(0.85, 0.0125); q from the data's window-level q (scope_map_overlay_points.npz, pre_w1to4_q, 52440 values); change at sample 300 of the DMT run only; W = 60; bins of 30; 50 replicates per condition; bootstrap 1000 draws; sign-flip exact over 2^14; seed 20261120. DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo, mean over subjects. At the global fit two predictions are tabulated: the pipeline's run-level prediction (constant across a run's bins, so its DiD is zero and the residual DiD equals the observed DiD, as partB4 records for the data) and a period-level prediction from (a_x, a_y, q) measured on the pre (samples 0–299) and post (samples 300–839) samples of each run separately, which is the reading the recorded prediction (i) refers to.

| condition | estimator | sts level (pre) | sts DiD | predicted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |
|---|---|---|---|---|---|---|---|---|
| (i) Δa = −0.015, Δc = 0 | W60 | 0.7152 | -0.0422 ± 0.0034 | -0.0471 ± 0.0036 | +0.0049 ± 0.0017 | 0.056; 0.82 | +0.00014 ± 0.00065 | +0.00130 ± 0.00050 |
| (i) Δa = −0.015, Δc = 0 | global (run-level prediction) | 1.1317 | -0.0675 ± 0.0058 | -0.0000 ± 0.0000 | -0.0675 ± 0.0058 | 0.000; 1.00 | — | — |
| (i) Δa = −0.015, Δc = 0 | global (period-level prediction) | 1.1317 | -0.0675 ± 0.0058 | -0.0764 ± 0.0048 | +0.0089 ± 0.0028 | 0.046; 0.62 | — | — |
| (ii) Δc = +0.01 | W60 | 0.7153 | +0.0010 ± 0.0036 | +0.0020 ± 0.0037 | -0.0010 ± 0.0018 | 0.460; 0.08 | +0.00758 ± 0.00072 | -0.00014 ± 0.00065 |
| (ii) Δc = +0.01 | global (run-level prediction) | 1.1390 | +0.0003 ± 0.0049 | -0.0000 ± 0.0000 | +0.0003 ± 0.0049 | 0.537; 0.04 | — | — |
| (ii) Δc = +0.01 | global (period-level prediction) | 1.1390 | +0.0003 ± 0.0049 | +0.0028 ± 0.0040 | -0.0025 ± 0.0027 | 0.461; 0.12 | — | — |
| (ii) Δc = +0.02 | W60 | 0.7154 | +0.0002 ± 0.0039 | +0.0053 ± 0.0037 | -0.0052 ± 0.0016 | 0.055; 0.76 | +0.01480 ± 0.00069 | -0.00037 ± 0.00063 |
| (ii) Δc = +0.02 | global (run-level prediction) | 1.1446 | -0.0033 ± 0.0050 | -0.0000 ± 0.0000 | -0.0033 ± 0.0050 | 0.403; 0.14 | — | — |
| (ii) Δc = +0.02 | global (period-level prediction) | 1.1446 | -0.0033 ± 0.0050 | +0.0092 ± 0.0039 | -0.0124 ± 0.0029 | 0.010; 0.92 | — | — |
| (ii) Δc = +0.03 | W60 | 0.7152 | +0.0001 ± 0.0031 | +0.0110 ± 0.0034 | -0.0109 ± 0.0017 | 0.001; 1.00 | +0.02210 ± 0.00071 | -0.00083 ± 0.00055 |
| (ii) Δc = +0.03 | global (run-level prediction) | 1.1512 | -0.0080 ± 0.0037 | -0.0000 ± 0.0000 | -0.0080 ± 0.0037 | 0.206; 0.26 | — | — |
| (ii) Δc = +0.03 | global (period-level prediction) | 1.1512 | -0.0080 ± 0.0037 | +0.0198 ± 0.0035 | -0.0278 ± 0.0027 | 0.000; 1.00 | — | — |
| (ii) Δc = −0.02 | W60 | 0.7152 | -0.0002 ± 0.0038 | +0.0053 ± 0.0037 | -0.0055 ± 0.0018 | 0.039; 0.80 | -0.01495 ± 0.00066 | -0.00027 ± 0.00059 |
| (ii) Δc = −0.02 | global (run-level prediction) | 1.1438 | -0.0045 ± 0.0050 | +0.0000 ± 0.0000 | -0.0045 ± 0.0050 | 0.408; 0.14 | — | — |
| (ii) Δc = −0.02 | global (period-level prediction) | 1.1438 | -0.0045 ± 0.0050 | +0.0089 ± 0.0041 | -0.0134 ± 0.0033 | 0.009; 0.94 | — | — |
| (iii) Δa = −0.015, Δc = +0.02 | W60 | 0.7153 | -0.0419 ± 0.0035 | -0.0427 ± 0.0033 | +0.0009 ± 0.0016 | 0.521; 0.00 | +0.01500 ± 0.00080 | +0.00093 ± 0.00056 |
| (iii) Δa = −0.015, Δc = +0.02 | global (run-level prediction) | 1.1364 | -0.0694 ± 0.0049 | -0.0000 ± 0.0000 | -0.0694 ± 0.0049 | 0.000; 1.00 | — | — |
| (iii) Δa = −0.015, Δc = +0.02 | global (period-level prediction) | 1.1364 | -0.0694 ± 0.0049 | -0.0687 ± 0.0040 | -0.0006 ± 0.0035 | 0.525; 0.10 | — | — |
| (iv) a_x − a_y = 0.03, Δa = −0.015 | W60 | 0.7131 | -0.0422 ± 0.0036 | -0.0473 ± 0.0038 | +0.0051 ± 0.0018 | 0.052; 0.72 | +0.00013 ± 0.00071 | +0.00130 ± 0.00056 |
| (iv) a_x − a_y = 0.03, Δa = −0.015 | global (run-level prediction) | 1.1127 | -0.0677 ± 0.0046 | +0.0000 ± 0.0000 | -0.0677 ± 0.0046 | 0.000; 1.00 | — | — |
| (iv) a_x − a_y = 0.03, Δa = −0.015 | global (period-level prediction) | 1.1127 | -0.0677 ± 0.0046 | -0.0746 ± 0.0045 | +0.0069 ± 0.0030 | 0.114; 0.64 | — | — |

Predictions recorded (plan §5, B17): (i) residual ≈ its finite-sample expectation (+0.004 to +0.008 at W = 60; near zero at the global fit); (ii) residual ≈ −1.77 Δc at the global fit (first order), smaller in magnitude at W = 60 through the bias, δ_sym ≈ 0.94 Δc; (iii) additive to first order; (iv) sts level lowered by the asymmetry with the residual near its expectation. Rule: this is the calibration the diagnostic lacked; its table is quoted wherever a residual is interpreted, and the finite-sample null of Results 4 is superseded by it where they overlap. Each condition's row is read against these in the outcome entry.
Note: the diagnostic's prediction uses the measured (a_x, a_y, q); a Δc changes the measured lag-0 q and the lag-1 autocorrelations of the coupled pair as well as the cross-lag entries, so the residual under (ii) is the estimator's response to the part of the change the AR(1) substitution cannot follow.
