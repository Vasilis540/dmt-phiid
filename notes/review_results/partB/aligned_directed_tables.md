# The aligned and directed cross-lag statistics without selection, the per-SD exchange rate and the network spin test (partB22_aligned_directed.py)
git=a9d9ca4

Exploratory; no threshold language. Per subject, run and W = 60 window, over the 6,555 pairs (region 20 excluded; non-finite TRs dropped as scripts/01): partB15's deviations of the window's 4 × 4 matrix. A_other = mean of sign(q̄_other)·δ_sym, q̄_other the pair's lag-0 correlation over the whole other run of the same subject; A_same with the whole same run's q̄; the window-sign statistic takes the sign of the window's own q (partB15, selected on the same samples). B = OLS slope of δ_sym on q across pairs. D and Sym = the closed-form response of the pair-mean sts to δ_anti alone and to δ_sym alone (partB15's response). Level = DMT windows 1–4; change = windows 6–14 minus 1–4; DiD = DMT minus placebo. Each cell: mean over subjects [inverted sign-flip 95 % interval], exact sign-flip p, negative/14.

## ts_gsr: (a)–(c) the per-window statistics

Pairs whose sign of q̄ differs between the two runs: mean share over subjects 0.209 (min 0.161, max 0.287).

| statistic | DMT pre-injection level | DMT post − pre | placebo post − pre | DiD |
|---|---|---|---|---|
| A_other (sign from the other run) | +0.00196 [+0.00124, +0.00268], p = 0.0002, 1 | -0.00028 [-0.00132, +0.00076], p = 0.5717, 7 | +0.00032 [-0.00037, +0.00101], p = 0.3280, 6 | -0.00059 [-0.00166, +0.00041], p = 0.2679, 9 |
| A_same (sign from the same run) | +0.00265 [+0.00181, +0.00349], p = 0.0001, 0 | +0.00002 [-0.00124, +0.00128], p = 0.9779, 7 | +0.00092 [-0.00005, +0.00189], p = 0.0612, 4 | -0.00090 [-0.00238, +0.00052], p = 0.2144, 10 |
| window-sign statistic (selected; partB15) | +0.00642 [+0.00505, +0.00770], p = 0.0001, 0 | -0.00044 [-0.00199, +0.00120], p = 0.5699, 10 | +0.00075 [-0.00052, +0.00204], p = 0.2231, 6 | -0.00119 [-0.00314, +0.00083], p = 0.2233, 10 |
| B, slope of δ_sym on q | +0.02019 [+0.01616, +0.02394], p = 0.0001, 0 | +0.00022 [-0.00421, +0.00486], p = 0.9198, 8 | +0.00255 [-0.00117, +0.00629], p = 0.1589, 6 | -0.00233 [-0.00837, +0.00387], p = 0.4226, 7 |
| D, response to δ_anti alone | -0.03823 [-0.04012, -0.03659], p = 0.0001, 14 | +0.00127 [-0.00062, +0.00335], p = 0.2274, 4 | +0.00016 [-0.00266, +0.00316], p = 0.9081, 9 | +0.00111 [-0.00332, +0.00518], p = 0.6143, 4 |
| Sym, response to δ_sym alone | -0.01338 [-0.01921, -0.00744], p = 0.0007, 12 | +0.00635 [-0.00114, +0.01368], p = 0.0869, 3 | -0.00398 [-0.00971, +0.00170], p = 0.1547, 10 | +0.01034 [+0.00138, +0.01943], p = 0.0266, 3 |
| D + Sym | -0.05161 [-0.05727, -0.04586], p = 0.0001, 14 | +0.00762 [-0.00065, +0.01578], p = 0.0670, 4 | -0.00383 [-0.00947, +0.00182], p = 0.1638, 10 | +0.01145 [+0.00101, +0.02192], p = 0.0342, 4 |
| response to both (reference) | -0.05357 [-0.05964, -0.04745], p = 0.0001, 14 | +0.00789 [-0.00095, +0.01658], p = 0.0735, 4 | -0.00408 [-0.01008, +0.00191], p = 0.1625, 10 | +0.01197 [+0.00091, +0.02309], p = 0.0360, 4 |
| RMS δ_anti | +0.10805 [+0.10271, +0.11348], p = 0.0001, 0 | +0.00417 [-0.00076, +0.00905], p = 0.0873, 4 | -0.00213 [-0.00723, +0.00295], p = 0.3828, 9 | +0.00631 [-0.00091, +0.01365], p = 0.0829, 6 |
| residual (observed − AR(1)-substituted sts) | -0.05302 [-0.05911, -0.04686], p = 0.0001, 14 | +0.00771 [-0.00112, +0.01643], p = 0.0797, 4 | -0.00382 [-0.00986, +0.00220], p = 0.1929, 10 | +0.01153 [+0.00046, +0.02265], p = 0.0422, 4 |

The residual DiD +0.01153 beside the DiD of D + Sym +0.01145 (their difference +0.00008: the lag-0 substitution and the non-additivity of the two responses).

## ts_gsr: (d) the per-SD exchange rate and the within-window regression

Within windows (the 112 pre-injection windows, windows 1–4 of both runs): mean between-pair SD of r₁ 0.0284, of |q| 0.1957; ratio (6.0705 × SD_r₁)/(0.1892 × SD_|q|) 4.66 (mean of the per-window ratios 4.69).
Group level (each pair averaged over the 14 subjects × 8 pre windows first; 112 windows): SD over the 6,555 pairs of r₁ 0.0082, of |q| 0.0799; ratio 3.28.
Within-window OLS of pair sts on (r₁, |q|, |a_x − a_y|) over 392 windows: mean unstandardised partial slopes +5.126 per unit r₁, -0.528 per unit |q|, -2.707 per unit |a_x − a_y|; mean standardised coefficients +0.661, -0.463, -0.426 (exchange_rates_tables.md (b): +0.661, -0.463, -0.426).

## ts_demean: (a)–(c) the per-window statistics

Pairs whose sign of q̄ differs between the two runs: mean share over subjects 0.186 (min 0.024, max 0.295).

| statistic | DMT pre-injection level | DMT post − pre | placebo post − pre | DiD |
|---|---|---|---|---|
| A_other (sign from the other run) | -0.00251 [-0.00458, -0.00047], p = 0.0221, 10 | -0.00019 [-0.00223, +0.00187], p = 0.8475, 8 | +0.00230 [+0.00031, +0.00436], p = 0.0245, 3 | -0.00249 [-0.00474, -0.00026], p = 0.0282, 11 |
| A_same (sign from the same run) | -0.00355 [-0.00604, -0.00106], p = 0.0043, 12 | +0.00006 [-0.00217, +0.00227], p = 0.9564, 7 | +0.00218 [+0.00020, +0.00417], p = 0.0289, 5 | -0.00212 [-0.00425, -0.00004], p = 0.0453, 10 |
| window-sign statistic (selected; partB15) | +0.00200 [-0.00025, +0.00424], p = 0.0760, 4 | -0.00176 [-0.00478, +0.00138], p = 0.2561, 9 | +0.00214 [+0.00022, +0.00407], p = 0.0321, 4 | -0.00390 [-0.00677, -0.00101], p = 0.0128, 12 |
| B, slope of δ_sym on q | +0.02441 [+0.01898, +0.02937], p = 0.0002, 1 | -0.00074 [-0.00674, +0.00536], p = 0.7946, 8 | -0.00037 [-0.00418, +0.00345], p = 0.8351, 9 | -0.00037 [-0.00814, +0.00747], p = 0.9203, 6 |
| D, response to δ_anti alone | -0.04231 [-0.04533, -0.03947], p = 0.0001, 14 | -0.00239 [-0.00608, +0.00123], p = 0.1887, 9 | -0.00096 [-0.00349, +0.00155], p = 0.4235, 8 | -0.00143 [-0.00613, +0.00327], p = 0.5184, 7 |
| Sym, response to δ_sym alone | +0.00252 [-0.00658, +0.01099], p = 0.5665, 5 | +0.00904 [-0.00317, +0.02124], p = 0.1382, 4 | -0.00956 [-0.01918, -0.00010], p = 0.0485, 10 | +0.01860 [+0.00698, +0.03041], p = 0.0048, 3 |
| D + Sym | -0.03979 [-0.04760, -0.03263], p = 0.0001, 14 | +0.00665 [-0.00509, +0.01836], p = 0.2458, 4 | -0.01052 [-0.01962, -0.00154], p = 0.0243, 11 | +0.01717 [+0.00696, +0.02744], p = 0.0038, 2 |
| response to both (reference) | -0.04047 [-0.04884, -0.03272], p = 0.0001, 14 | +0.00729 [-0.00541, +0.02000], p = 0.2410, 4 | -0.01127 [-0.02103, -0.00166], p = 0.0245, 11 | +0.01856 [+0.00750, +0.02964], p = 0.0034, 2 |
| RMS δ_anti | +0.11211 [+0.10687, +0.11727], p = 0.0001, 0 | +0.00261 [-0.00207, +0.00731], p = 0.2451, 6 | -0.00091 [-0.00652, +0.00471], p = 0.7211, 7 | +0.00352 [-0.00356, +0.01064], p = 0.2977, 5 |
| residual (observed − AR(1)-substituted sts) | -0.03987 [-0.04814, -0.03221], p = 0.0001, 14 | +0.00723 [-0.00543, +0.01987], p = 0.2426, 5 | -0.01100 [-0.02072, -0.00144], p = 0.0269, 11 | +0.01823 [+0.00716, +0.02932], p = 0.0040, 2 |

The residual DiD +0.01823 beside the DiD of D + Sym +0.01717 (their difference +0.00106: the lag-0 substitution and the non-additivity of the two responses).

## ts_demean: (d) the per-SD exchange rate and the within-window regression

Within windows (the 112 pre-injection windows, windows 1–4 of both runs): mean between-pair SD of r₁ 0.0294, of |q| 0.2087; ratio (6.0705 × SD_r₁)/(0.1892 × SD_|q|) 4.52 (mean of the per-window ratios 4.56).
Group level (each pair averaged over the 14 subjects × 8 pre windows first; 112 windows): SD over the 6,555 pairs of r₁ 0.0081, of |q| 0.1039; ratio 2.51.
Within-window OLS of pair sts on (r₁, |q|, |a_x − a_y|) over 392 windows: mean unstandardised partial slopes +4.523 per unit r₁, -0.506 per unit |q|, -2.583 per unit |a_x − a_y|; mean standardised coefficients +0.594, -0.476, -0.413 (exchange_rates_tables.md (b): +0.594, -0.476, -0.413).

## (e) Spin test of the network structure of the regional maps (regional_partial.csv; eight classes: the seven Yeo networks and the subcortex)

| map | one-way F (8 classes) | spin p (F_spin ≥ F_obs) | SomMot − Default | spin p, two-sided | Vis − Default | spin p, two-sided | rotations | regions |
|---|---|---|---|---|---|---|---|---|
| sts (unpartialled) | 16.933 | 0.0564 | -0.00665 | 0.6107 | -0.01606 | 0.1990 | 10000 | 115 |
| sts with regional r₁ partialled out (sts_resid_win) | 8.146 | 0.0009 | -0.00965 | 0.2240 | +0.00875 | 0.3089 | 10000 | 115 |

Rotations: perm_id of the Schaefer-100 rotation file, one direction (the classes are fixed labels); region 20's missing value moves with its parcel and is dropped wherever it lands; the 16 subcortical values are not rotated.

## Checks

22 checks run, 0 failed.
- ok: the copy of notes/partB15_directed_crosslag.py l. 70–92 is verbatim (|difference| 0, tolerance 0)
- ok: (d) ∂sts/∂r₁ at (0.85, 0.25) = 6.0705 (|difference| 0, tolerance 1e-09)
- ok: (d) ∂sts/∂q at (0.85, 0.25) = −0.1892 (|difference| 0, tolerance 1e-09)
- ok: ts_gsr residual per window = diag_series res (|difference| 6.66e-16, tolerance 1e-10)
- ok: ts_gsr winsign run means = crosslag_deviation.csv w60_signq_weighted_mean_deviation (|difference| 1.73e-18, tolerance 1e-10)
- ok: ts_gsr B run means = crosslag_deviation.csv w60_slope_deviation_on_q (|difference| 1.39e-17, tolerance 1e-10)
- ok: ts_gsr winsign DiD = directed_crosslag_tables.md (5 decimals) (|difference| 6.65e-07, tolerance 5e-06)
- ok: ts_gsr winsign DiD sign-flip p = directed_crosslag_tables.md (4 decimals) (|difference| 3.34e-05, tolerance 5e-05)
- ok: ts_gsr rms_anti DiD = directed_crosslag_tables.md (5 decimals) (|difference| 3.09e-06, tolerance 5e-06)
- ok: ts_gsr rms_anti DiD sign-flip p = directed_crosslag_tables.md (4 decimals) (|difference| 1.43e-05, tolerance 5e-05)
- ok: ts_gsr (d) mean standardised coefficients = exchange_rates_tables.md (b) (3 decimals) (|difference| 0.000404, tolerance 0.0005)
- ok: ts_demean residual per window = diag_series res (|difference| 4.44e-16, tolerance 1e-10)
- ok: ts_demean winsign run means = crosslag_deviation.csv w60_signq_weighted_mean_deviation (|difference| 1.73e-18, tolerance 1e-10)
- ok: ts_demean B run means = crosslag_deviation.csv w60_slope_deviation_on_q (|difference| 2.08e-17, tolerance 1e-10)
- ok: ts_demean winsign DiD = directed_crosslag_tables.md (5 decimals) (|difference| 2.77e-06, tolerance 5e-06)
- ok: ts_demean winsign DiD sign-flip p = directed_crosslag_tables.md (4 decimals) (|difference| 1.74e-05, tolerance 5e-05)
- ok: ts_demean rms_anti DiD = directed_crosslag_tables.md (5 decimals) (|difference| 2.6e-07, tolerance 5e-06)
- ok: ts_demean rms_anti DiD sign-flip p = directed_crosslag_tables.md (4 decimals) (|difference| 2.95e-05, tolerance 5e-05)
- ok: ts_demean (d) mean standardised coefficients = exchange_rates_tables.md (b) (3 decimals) (|difference| 0.000444, tolerance 0.0005)
- ok: (e) the network column of regional_partial.csv = the LUT class of each cortical parcel (|difference| 0, tolerance 0)
- ok: (e) identity rotation = the direct class means (|difference| 2.22e-16, tolerance 1e-12)
- ok: (e) identity rotation = the direct class means (|difference| 2.6e-18, tolerance 1e-12)

## Predictions and rule (pre-run entry, B22)

Predictions: (a) ts_gsr A_other level +0.001 to +0.004, DiD −0.003 to +0.001; ts_demean level −0.001 to −0.004, DiD −0.005 to 0; A_same near A_other; ts_gsr level below the window-sign +0.0061 and near the run-sign +0.00245; ts_demean level of the sign of δ_run (−0.0026). (b) B level about +0.020 (ts_gsr) and +0.024 (ts_demean); the DiD negative if a shared slow structure weakened, near B24's expectation if not. (c) D DiD −0.002 to −0.006 on ts_gsr; the directed part lowers the residual DiD; Sym's DiD exceeds the residual DiD. (d) within windows SD r₁ 0.025–0.035, SD |q| 0.18–0.22, ratio 4–6; group level 0.010–0.016, 0.12–0.18, 2–4; unstandardised slopes +5 to +6 per r₁, −0.40 to −0.55 per |q|, −3 to −5 per asymmetry. (e) spin p < 0.05 for the unpartialled F; 0.01–0.3 for the residual F; > 0.05 for both contrasts (the last two uncertain).
Rule: A_other reported, A_same and B beside it; the DiDs read against B24's (quoted) and B23 (b)'s expectations and converted to residual-DiD equivalents with B23's two aligned conversions, in the outcome entry; (d) replaces the per-SD ratio of the abstract and Results 1; (e) decides the network-structure statement.
