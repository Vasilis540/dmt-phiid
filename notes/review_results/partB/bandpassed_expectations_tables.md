# The pure-autocorrelation expectations of the new statistics on the band-passed generator (partB24_bandpassed_expectations.py)
git=a9d9ca4

B17b's generator at its solved parameters (β̄ = 185.4, σ_q = 0.2637, β̄_post = 105.7, read from calibration_filtered_tables.md; filter 0.0064–0.080 Hz), condition (i) only: 20 replicates × 14 subjects × 2 runs × 840 samples × 300 pairs, the DMT run spliced at sample 300. Seed 20261120. ± is the SD over replicates. DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo; level = the DMT pre-injection mean.

Checks: 10 run, 0 failed.

## The check against B17b's condition (i), W = 60

| DiD | B24 (mean ± SD) | B17b (committed) | within one of B17b's SDs |
|---|---|---|---|
| observed sts | -0.09441 ± 0.00222 | -0.09400 ± 0.00280 | yes |
| AR(1)-substituted sts | -0.09719 ± 0.00205 | -0.09660 ± 0.00270 | yes |
| residual | +0.00279 ± 0.00122 | +0.00270 ± 0.00140 | yes |
| RMS δ_anti | +0.00669 ± 0.00100 | +0.00641 ± 0.00104 | yes |

## B17b's statistics, condition (i)

| estimator | sts level (pre) | sts DiD | predicted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |
|---|---|---|---|---|---|---|---|
| W60 | 1.1881 | -0.0944 ± 0.0022 | -0.0972 ± 0.0020 | +0.0028 ± 0.0012 | 0.121; 0.70 | -0.00008 ± 0.00032 | +0.00669 ± 0.00100 |
| global (run-level prediction) | 1.3261 | -0.1050 ± 0.0031 | +0.0000 ± 0.0000 | -0.1050 ± 0.0031 | 0.000; 1.00 | — | — |
| global (period-level prediction) | 1.3261 | -0.1050 ± 0.0031 | -0.1091 ± 0.0028 | +0.0041 ± 0.0016 | 0.112; 0.50 | — | — |

## B22's statistics under a pure autocorrelation change (W = 60)

| statistic | DMT pre-injection level | DiD |
|---|---|---|
| A_other (sign from the other run) | -0.00028 ± 0.00019 | +0.00001 ± 0.00031 |
| A_same (sign from the same run) | -0.00001 ± 0.00018 | +0.00004 ± 0.00037 |
| window-sign statistic (selected) | +0.00340 ± 0.00015 | -0.00087 ± 0.00033 |
| B, slope of δ_sym on q | +0.01092 ± 0.00045 | -0.00263 ± 0.00077 |
| D, response to δ_anti alone | -0.03508 ± 0.00030 | -0.00100 ± 0.00041 |
| Sym, response to δ_sym alone | -0.00030 ± 0.00049 | +0.00373 ± 0.00092 |
| D + Sym | -0.03538 ± 0.00056 | +0.00273 ± 0.00114 |
| window-level mean pair r₁ | +0.86339 ± 0.00028 | -0.01540 ± 0.00035 |

Sym's DiD minus (the residual DiD − D's DiD): -0.00006 ± 0.00017.

## Checks

- ok: the filter edges = those in calibration_filtered_tables.md (printed precision) (|difference| 0, tolerance 1e-12)
- ok: the copy of notes/partB17b_calibration_filtered.py l. 81–88 is verbatim (|difference| 0, tolerance 0)
- ok: the copy of notes/partB17b_calibration_filtered.py l. 97–112 is verbatim (|difference| 0, tolerance 0)
- ok: the copy of notes/partB17b_calibration_filtered.py l. 135–150 is verbatim (|difference| 0, tolerance 0)
- ok: the copy of notes/partB17b_calibration_filtered.py l. 154–186 is verbatim (|difference| 0, tolerance 0)
- ok: the copy of notes/partB15_directed_crosslag.py l. 78–92 is verbatim (|difference| 0, tolerance 0)
- ok: (i) W60 sts DiD within one of B17b's replicate SDs of B17b's mean (-0.09400 ± 0.00280) (|difference| 0.000408, tolerance 0.003)
- ok: (i) W60 pred DiD within one of B17b's replicate SDs of B17b's mean (-0.09660 ± 0.00270) (|difference| 0.000595, tolerance 0.003)
- ok: (i) W60 res DiD within one of B17b's replicate SDs of B17b's mean (+0.00270 ± 0.00140) (|difference| 8.73e-05, tolerance 0.001)
- ok: (i) W60 anti DiD within one of B17b's replicate SDs of B17b's mean (+0.00641 ± 0.00104) (|difference| 0.000275, tolerance 0.001)

## Prediction and rule (pre-run entry, B24)

Prediction: the check passes; the A_other DiD within ±0.0005, the A_same DiD within ±0.001, the B DiD within ±0.003; the D DiD −0.002 to −0.006; Sym's DiD equal to the residual DiD minus D's within 0.001.
Rule: these are the pure-autocorrelation expectations against which B22's DiDs are read.
