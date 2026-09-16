# The cross-lag budget on the finite-sample null, the controls, and the null-corrected budget of the data (partB13_crosslag_budget_null.py; git=6b5181a; seed=20261120)

Data targets (ts_gsr), computed here: DMT run level: mean a 0.8638, mean |q̂| 0.1904, fraction q̂ < 0 0.543, |q̂| < 0.05 0.174, |q̂| < 0.10 0.337; DMT window level: mean a 0.8561, mean |q̂| 0.2721, fraction q̂ < 0 0.515, |q̂| < 0.05 0.111, |q̂| < 0.10 0.219; PCB run level: mean a 0.8694, mean |q̂| 0.1987, fraction q̂ < 0 0.546, |q̂| < 0.05 0.162, |q̂| < 0.10 0.319; PCB window level: mean a 0.8631, mean |q̂| 0.2828, fraction q̂ < 0 0.516, |q̂| < 0.05 0.106, |q̂| < 0.10 0.210

Filter fits (the null's own fit_filter): placebo: β = 200, band 0.0064–0.080 Hz; DMTpost: β = 100, band 0.0030–0.080 Hz

## Configuration 0: primary: h = 0.5, DMT-post/placebo ACF, mixture q solved to run-level a, |q̂|, fraction |q̂| < 0.05

   solved DMT (k = 0, targets at the run level: a 0.8638, |q̂| 0.1904, fraction |q̂| < 0.05 0.174): beta = 129.2379, w = 0.0822, sig2 = 0.2489; achieved on the solver batch a 0.8639, |q̂| 0.1904, fraction 0.174
   DMT (25000 pair-runs): null run-level mean a 0.8642 (data 0.8638), mean |q̂| 0.1909 (data 0.1904), fraction q̂ < 0 0.499 (data 0.543), |q̂| < 0.05 0.186 (data 0.174), |q̂| < 0.10 0.351 (data 0.337)
   DMT terms (mean ± Monte-Carlo SE): run +0.00031 ± 0.00004  wd +0.00035 ± 0.00004  means -0.00004 ± 0.00001  within +0.00034 ± 0.00004  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00013 ± 0.00004  d60_winsign +0.00330 ± 0.00004
   solved PCB (k = 0, targets at the run level: a 0.8694, |q̂| 0.1987, fraction |q̂| < 0.05 0.162): beta = 197.4144, w = 0.0741, sig2 = 0.2530; achieved on the solver batch a 0.8694, |q̂| 0.1987, fraction 0.162
   PCB (25000 pair-runs): null run-level mean a 0.8698 (data 0.8694), mean |q̂| 0.1982 (data 0.1987), fraction q̂ < 0 0.506 (data 0.546), |q̂| < 0.05 0.176 (data 0.162), |q̂| < 0.10 0.337 (data 0.319)
   PCB terms (mean ± Monte-Carlo SE): run +0.00047 ± 0.00004  wd +0.00048 ± 0.00004  means -0.00001 ± 0.00000  within +0.00047 ± 0.00004  pool +0.00004 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00022 ± 0.00004  d60_winsign +0.00373 ± 0.00004
   null value (mean over the two run types): run +0.00039 ± 0.00003  wd +0.00042 ± 0.00003  means -0.00002 ± 0.00000  within +0.00040 ± 0.00003  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00017 ± 0.00003  d60_winsign +0.00352 ± 0.00003

## Configuration 1: heterogeneity h = 0.25

   solved DMT (k = 1, targets at the run level: a 0.8638, |q̂| 0.1904, fraction |q̂| < 0.05 0.174): beta = 125.4377, w = 0.0130, sig2 = 0.2251; achieved on the solver batch a 0.8638, |q̂| 0.1904, fraction 0.173
   DMT (25000 pair-runs): null run-level mean a 0.8638 (data 0.8638), mean |q̂| 0.1848 (data 0.1904), fraction q̂ < 0 0.498 (data 0.543), |q̂| < 0.05 0.176 (data 0.174), |q̂| < 0.10 0.336 (data 0.337)
   DMT terms (mean ± Monte-Carlo SE): run +0.00029 ± 0.00004  wd +0.00032 ± 0.00004  means -0.00003 ± 0.00001  within +0.00031 ± 0.00004  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00009 ± 0.00004  d60_winsign +0.00351 ± 0.00004
   solved PCB (k = 1, targets at the run level: a 0.8694, |q̂| 0.1987, fraction |q̂| < 0.05 0.162): beta = 190.9599, w = 0.0062, sig2 = 0.2438; achieved on the solver batch a 0.8694, |q̂| 0.1987, fraction 0.162
   PCB (25000 pair-runs): null run-level mean a 0.8693 (data 0.8694), mean |q̂| 0.1994 (data 0.1987), fraction q̂ < 0 0.500 (data 0.546), |q̂| < 0.05 0.160 (data 0.162), |q̂| < 0.10 0.314 (data 0.319)
   PCB terms (mean ± Monte-Carlo SE): run +0.00029 ± 0.00004  wd +0.00030 ± 0.00004  means -0.00001 ± 0.00000  within +0.00030 ± 0.00004  pool +0.00002 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00004 ± 0.00004  d60_winsign +0.00378 ± 0.00004
   null value (mean over the two run types): run +0.00029 ± 0.00003  wd +0.00031 ± 0.00003  means -0.00002 ± 0.00000  within +0.00031 ± 0.00003  pool +0.00002 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00007 ± 0.00003  d60_winsign +0.00364 ± 0.00003

## Configuration 2: heterogeneity h = 1.0

   solved DMT (k = 2, targets at the run level: a 0.8638, |q̂| 0.1904, fraction |q̂| < 0.05 0.174): beta = 126.0645, w = 0.0198, sig2 = 0.2403; achieved on the solver batch a 0.8638, |q̂| 0.1904, fraction 0.174
   DMT (25000 pair-runs): null run-level mean a 0.8645 (data 0.8638), mean |q̂| 0.1961 (data 0.1904), fraction q̂ < 0 0.495 (data 0.543), |q̂| < 0.05 0.163 (data 0.174), |q̂| < 0.10 0.318 (data 0.337)
   DMT terms (mean ± Monte-Carlo SE): run +0.00026 ± 0.00004  wd +0.00028 ± 0.00004  means -0.00002 ± 0.00001  within +0.00028 ± 0.00004  pool +0.00003 ± 0.00001  eps -0.00003 ± 0.00000  d60 +0.00008 ± 0.00004  d60_winsign +0.00322 ± 0.00004
   solved PCB (k = 2, targets at the run level: a 0.8694, |q̂| 0.1987, fraction |q̂| < 0.05 0.162): beta = 198.5249, w = 0.0478, sig2 = 0.2486; achieved on the solver batch a 0.8694, |q̂| 0.1987, fraction 0.162
   PCB (25000 pair-runs): null run-level mean a 0.8704 (data 0.8694), mean |q̂| 0.1986 (data 0.1987), fraction q̂ < 0 0.510 (data 0.546), |q̂| < 0.05 0.167 (data 0.162), |q̂| < 0.10 0.318 (data 0.319)
   PCB terms (mean ± Monte-Carlo SE): run +0.00037 ± 0.00004  wd +0.00038 ± 0.00004  means -0.00001 ± 0.00000  within +0.00037 ± 0.00004  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00012 ± 0.00004  d60_winsign +0.00341 ± 0.00004
   null value (mean over the two run types): run +0.00031 ± 0.00003  wd +0.00033 ± 0.00003  means -0.00001 ± 0.00000  within +0.00033 ± 0.00003  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00010 ± 0.00003  d60_winsign +0.00332 ± 0.00003

## Configuration 3: placebo ACF for both run types

   solved DMT (k = 3, targets at the run level: a 0.8638, |q̂| 0.1904, fraction |q̂| < 0.05 0.174): beta = 167.5407, w = 0.0678, sig2 = 0.2458; achieved on the solver batch a 0.8638, |q̂| 0.1904, fraction 0.175
   DMT (25000 pair-runs): null run-level mean a 0.8641 (data 0.8638), mean |q̂| 0.1925 (data 0.1904), fraction q̂ < 0 0.503 (data 0.543), |q̂| < 0.05 0.176 (data 0.174), |q̂| < 0.10 0.338 (data 0.337)
   DMT terms (mean ± Monte-Carlo SE): run +0.00045 ± 0.00004  wd +0.00046 ± 0.00004  means -0.00001 ± 0.00000  within +0.00045 ± 0.00004  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00022 ± 0.00004  d60_winsign +0.00354 ± 0.00004
   solved PCB (k = 3, targets at the run level: a 0.8694, |q̂| 0.1987, fraction |q̂| < 0.05 0.162): beta = 196.9044, w = 0.0566, sig2 = 0.2555; achieved on the solver batch a 0.8694, |q̂| 0.1987, fraction 0.162
   PCB (25000 pair-runs): null run-level mean a 0.8694 (data 0.8694), mean |q̂| 0.1995 (data 0.1987), fraction q̂ < 0 0.504 (data 0.546), |q̂| < 0.05 0.172 (data 0.162), |q̂| < 0.10 0.331 (data 0.319)
   PCB terms (mean ± Monte-Carlo SE): run +0.00047 ± 0.00004  wd +0.00048 ± 0.00004  means -0.00001 ± 0.00000  within +0.00043 ± 0.00004  pool +0.00006 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00019 ± 0.00004  d60_winsign +0.00371 ± 0.00004
   null value (mean over the two run types): run +0.00046 ± 0.00003  wd +0.00047 ± 0.00003  means -0.00001 ± 0.00000  within +0.00044 ± 0.00003  pool +0.00005 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00021 ± 0.00003  d60_winsign +0.00363 ± 0.00003

## Configuration 4: q ~ N(0, σ_q) solved to run-level a and |q̂|

   solved DMT (k = 4, targets at the run level: a 0.8638, |q̂| 0.1904, fraction |q̂| < 0.05 0.174): beta = 129.7940, sigq = 0.2301; achieved on the solver batch a 0.8638, |q̂| 0.1904, fraction 0.165
   DMT (25000 pair-runs): null run-level mean a 0.8644 (data 0.8638), mean |q̂| 0.1904 (data 0.1904), fraction q̂ < 0 0.502 (data 0.543), |q̂| < 0.05 0.167 (data 0.174), |q̂| < 0.10 0.324 (data 0.337)
   DMT terms (mean ± Monte-Carlo SE): run +0.00032 ± 0.00004  wd +0.00034 ± 0.00004  means -0.00001 ± 0.00001  within +0.00033 ± 0.00004  pool +0.00002 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00012 ± 0.00004  d60_winsign +0.00349 ± 0.00004
   solved PCB (k = 4, targets at the run level: a 0.8694, |q̂| 0.1987, fraction |q̂| < 0.05 0.162): beta = 197.1746, sigq = 0.2394; achieved on the solver batch a 0.8694, |q̂| 0.1987, fraction 0.156
   PCB (25000 pair-runs): null run-level mean a 0.8697 (data 0.8694), mean |q̂| 0.1971 (data 0.1987), fraction q̂ < 0 0.501 (data 0.546), |q̂| < 0.05 0.158 (data 0.162), |q̂| < 0.10 0.312 (data 0.319)
   PCB terms (mean ± Monte-Carlo SE): run +0.00032 ± 0.00004  wd +0.00032 ± 0.00004  means -0.00000 ± 0.00000  within +0.00033 ± 0.00004  pool +0.00001 ± 0.00001  eps -0.00001 ± 0.00000  d60 +0.00007 ± 0.00004  d60_winsign +0.00368 ± 0.00004
   null value (mean over the two run types): run +0.00032 ± 0.00003  wd +0.00033 ± 0.00003  means -0.00001 ± 0.00000  within +0.00033 ± 0.00003  pool +0.00002 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00009 ± 0.00003  d60_winsign +0.00359 ± 0.00003

## Configuration 5: mixture solved to the W = 60 window-level means

   solved DMT (k = 5, targets at the window level: a 0.8561, |q̂| 0.2721, fraction |q̂| < 0.05 0.111): beta = 121.0496, w = 0.0852, sig2 = 0.2627; achieved on the solver batch a 0.8561, |q̂| 0.2721, fraction 0.111
   DMT (25000 pair-runs): null run-level mean a 0.8625 (data 0.8638), mean |q̂| 0.2005 (data 0.1904), fraction q̂ < 0 0.497 (data 0.543), |q̂| < 0.05 0.183 (data 0.174), |q̂| < 0.10 0.340 (data 0.337)
   DMT terms (mean ± Monte-Carlo SE): run +0.00027 ± 0.00004  wd +0.00030 ± 0.00004  means -0.00003 ± 0.00001  within +0.00031 ± 0.00004  pool +0.00002 ± 0.00001  eps -0.00003 ± 0.00000  d60 +0.00009 ± 0.00004  d60_winsign +0.00319 ± 0.00004
   solved PCB (k = 5, targets at the window level: a 0.8631, |q̂| 0.2828, fraction |q̂| < 0.05 0.106): beta = 186.0153, w = 0.1258, sig2 = 0.2809; achieved on the solver batch a 0.8631, |q̂| 0.2828, fraction 0.106
   PCB (25000 pair-runs): null run-level mean a 0.8674 (data 0.8694), mean |q̂| 0.2094 (data 0.1987), fraction q̂ < 0 0.504 (data 0.546), |q̂| < 0.05 0.188 (data 0.162), |q̂| < 0.10 0.341 (data 0.319)
   PCB terms (mean ± Monte-Carlo SE): run +0.00045 ± 0.00004  wd +0.00045 ± 0.00004  means -0.00001 ± 0.00000  within +0.00044 ± 0.00004  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00019 ± 0.00004  d60_winsign +0.00353 ± 0.00004
   null value (mean over the two run types): run +0.00036 ± 0.00003  wd +0.00038 ± 0.00003  means -0.00002 ± 0.00000  within +0.00038 ± 0.00003  pool +0.00003 ± 0.00001  eps -0.00002 ± 0.00000  d60 +0.00014 ± 0.00003  d60_winsign +0.00336 ± 0.00003

## Controls at the primary configuration's parameters (report-only)

   (i) common drive, DMT: λ = 0.2, regional parts at β̄ = 129.2 (population lag-1 a_n = 0.8650), shared part at β_s = 1258.6 (a_s = 0.9650); population d = λ(1 − λ)(a_s − a_n) = +0.01600; empirical/analytic variance ratios 1.0021 (regional), 0.9997 (shared); realised run-level mean a 0.8823, |q̂| 0.1998; 25000 pair-runs
      terms: run +0.01428 ± 0.00005  wd +0.01387 ± 0.00005  means +0.00041 ± 0.00001  within +0.01275 ± 0.00005  pool +0.00127 ± 0.00001  eps -0.00015 ± 0.00000  d60 +0.01231 ± 0.00005  d60_winsign +0.01147 ± 0.00005; shares of δ_run: within +0.893, pool +0.089, means +0.029, eps -0.010
   (ii) pooling, DMT: TRs 0–239 at β₁ ~ N(6.0 β̄, h·6.0 β̄) (population lag-1 0.9461) with q₁ from the primary mixture; TRs 240–839 at β₂ ~ N(β̄/5, h·β̄/5) (population lag-1 0.8402) with q₂ = q₁(1 − g), g ~ U(0.5, 1.0); last batch's segment means: a 0.9350, |q̂| 0.2214 before TR 240 and a 0.8400, |q̂| 0.0777 after; realised run-level mean a 0.8522, |q̂| 0.0875; 25000 pair-runs
      terms: run +0.00133 ± 0.00005  wd +0.00136 ± 0.00006  means -0.00003 ± 0.00001  within +0.00037 ± 0.00005  pool +0.00101 ± 0.00002  eps -0.00002 ± 0.00001  d60 +0.00031 ± 0.00004  d60_winsign +0.00299 ± 0.00004; shares of δ_run: within +0.280, pool +0.757, means -0.025, eps -0.013; δ_pool = 49.1 Monte-Carlo SEs
   (i) common drive, PCB: λ = 0.2, regional parts at β̄ = 197.4 (population lag-1 a_n = 0.8713), shared part at β_s = 1923.9 (a_s = 0.9713); population d = λ(1 − λ)(a_s − a_n) = +0.01600; empirical/analytic variance ratios 0.9983 (regional), 0.9977 (shared); realised run-level mean a 0.8878, |q̂| 0.1989; 25000 pair-runs
      terms: run +0.01449 ± 0.00005  wd +0.01435 ± 0.00005  means +0.00014 ± 0.00000  within +0.01307 ± 0.00005  pool +0.00132 ± 0.00001  eps -0.00004 ± 0.00000  d60 +0.01265 ± 0.00005  d60_winsign +0.01195 ± 0.00004; shares of δ_run: within +0.902, pool +0.091, means +0.009, eps -0.003
   (ii) pooling, PCB: TRs 0–239 at β₁ ~ N(6.0 β̄, h·6.0 β̄) (population lag-1 0.9571) with q₁ from the primary mixture; TRs 240–839 at β₂ ~ N(β̄/5, h·β̄/5) (population lag-1 0.8359) with q₂ = q₁(1 − g), g ~ U(0.5, 1.0); last batch's segment means: a 0.9457, |q̂| 0.2321 before TR 240 and a 0.8358, |q̂| 0.0804 after; realised run-level mean a 0.8465, |q̂| 0.0861; 25000 pair-runs
      terms: run +0.00130 ± 0.00006  wd +0.00130 ± 0.00006  means -0.00001 ± 0.00000  within +0.00042 ± 0.00005  pool +0.00089 ± 0.00002  eps -0.00001 ± 0.00001  d60 +0.00032 ± 0.00004  d60_winsign +0.00269 ± 0.00004; shares of δ_run: within +0.326, pool +0.688, means -0.005, eps -0.009; δ_pool = 43.7 Monte-Carlo SEs
   (i) common drive, mean over run types: run +0.01438 ± 0.00004  wd +0.01411 ± 0.00004  means +0.00027 ± 0.00000  within +0.01291 ± 0.00004  pool +0.00129 ± 0.00001  eps -0.00010 ± 0.00000  d60 +0.01248 ± 0.00004  d60_winsign +0.01171 ± 0.00003; shares: within +0.898, pool +0.090, means +0.019, eps -0.007
   (ii) pooling, mean over run types: run +0.00131 ± 0.00004  wd +0.00133 ± 0.00004  means -0.00002 ± 0.00000  within +0.00040 ± 0.00004  pool +0.00095 ± 0.00001  eps -0.00001 ± 0.00001  d60 +0.00032 ± 0.00003  d60_winsign +0.00284 ± 0.00003; shares: within +0.303, pool +0.723, means -0.015, eps -0.011

## Null-corrected budget of the data and the reading under the pre-run entry

Data, ts_gsr (from crosslag_budget.csv, partB12; the same bootstrap draws): δ_run +0.00340 [+0.00300, +0.00380]  δ_wd +0.00339 [+0.00299, +0.00378]  δ_means +0.00001 [-0.00000, +0.00003]  δ_within +0.00291 [+0.00257, +0.00325]  δ_pool +0.00050 [+0.00038, +0.00062]  δ_eps -0.00002 [-0.00004, +0.00001]  δ_d60 +0.00245 [+0.00212, +0.00281]  δ_d60_winsign +0.00611 [+0.00563, +0.00665]

(a) Finite sampling. δ_run,null by configuration: k = 0: +0.00039 ± 0.00003 (F = 0.116); k = 1: +0.00029 ± 0.00003 (F = 0.085); k = 2: +0.00031 ± 0.00003 (F = 0.092); k = 3: +0.00046 ± 0.00003 (F = 0.135); k = 4: +0.00032 ± 0.00003 (F = 0.095); k = 5: +0.00036 ± 0.00003 (F = 0.105). Branch: a minor part. The 10:32 UTC reading, as recorded: "near zero (+0.00025, 7.3 % of +0.00340): finite sampling is removed as a source of the signature".

k = 0, null-corrected: δ_run,c +0.00301 [+0.00261, +0.00340]  δ_within,c +0.00250 [+0.00217, +0.00285]  δ_pool,c +0.00046 [+0.00035, +0.00059]  δ_means,c +0.00004 [+0.00002, +0.00005]  δ_eps,c +0.00000 [-0.00002, +0.00003]; shares within +0.833, pool +0.154, means +0.012, eps +0.001; labels within: most, pool: a minor part, means: a minor part
k = 1, null-corrected: δ_run,c +0.00311 [+0.00271, +0.00351]  δ_within,c +0.00260 [+0.00227, +0.00294]  δ_pool,c +0.00047 [+0.00036, +0.00059]  δ_means,c +0.00003 [+0.00002, +0.00005]  δ_eps,c +0.00001 [-0.00002, +0.00003]; shares within +0.837, pool +0.152, means +0.010, eps +0.002; labels within: most, pool: a minor part, means: a minor part
k = 2, null-corrected: δ_run,c +0.00309 [+0.00269, +0.00348]  δ_within,c +0.00258 [+0.00225, +0.00293]  δ_pool,c +0.00047 [+0.00036, +0.00059]  δ_means,c +0.00003 [+0.00001, +0.00004]  δ_eps,c +0.00001 [-0.00002, +0.00003]; shares within +0.837, pool +0.152, means +0.009, eps +0.002; labels within: most, pool: a minor part, means: a minor part
k = 3, null-corrected: δ_run,c +0.00294 [+0.00254, +0.00334]  δ_within,c +0.00247 [+0.00213, +0.00281]  δ_pool,c +0.00045 [+0.00034, +0.00057]  δ_means,c +0.00002 [+0.00001, +0.00004]  δ_eps,c +0.00000 [-0.00002, +0.00003]; shares within +0.839, pool +0.153, means +0.007, eps +0.001; labels within: most, pool: a minor part, means: a minor part
k = 4, null-corrected: δ_run,c +0.00308 [+0.00268, +0.00348]  δ_within,c +0.00258 [+0.00224, +0.00292]  δ_pool,c +0.00048 [+0.00036, +0.00060]  δ_means,c +0.00002 [+0.00001, +0.00004]  δ_eps,c -0.00000 [-0.00002, +0.00002]; shares within +0.838, pool +0.155, means +0.007, eps -0.000; labels within: most, pool: a minor part, means: a minor part
k = 5, null-corrected: δ_run,c +0.00304 [+0.00264, +0.00344]  δ_within,c +0.00253 [+0.00220, +0.00288]  δ_pool,c +0.00047 [+0.00036, +0.00059]  δ_means,c +0.00003 [+0.00002, +0.00005]  δ_eps,c +0.00001 [-0.00002, +0.00003]; shares within +0.833, pool +0.155, means +0.011, eps +0.002; labels within: most, pool: a minor part, means: a minor part
(b) Apportioning. gate passed: the CI of δ_run,c lies above zero in every configuration; ε check passed in every configuration (|ε_c| ≤ δ_run,c / 10); validity from the controls: control (i) shares pool +0.090, means +0.019; control (ii) share within +0.303. Read: δ_within: most; δ_pool: a minor part; δ_means: a minor part.

(c) Reading: δ_within most: the signature is present inside 2-minute windows, where pooling across windows cannot act. The candidates are common slow drive or lagged coupling (not separable at τ = 1), non-stationarity faster than 2 minutes, or a within-window finite-sample effect that the null as specified does not reproduce. Pooling is not the principal account.

(d) δ_60 with the run-level sign, data +0.00245 [+0.00212, +0.00281], null (primary) +0.00017 ± 0.00003; partB10's window-sign value, data +0.00611, null (primary) +0.00352 ± 0.00003. The 10:32 UTC W = 60 reading, as recorded: "comparable to the run-level +0.00340 (ratio 1.80, within a factor of two): a stationary mechanism is indicated and pooling is not distinguished by run length"; superseded for the reasons of the correction note of 16 Sep 2026 (the window's sign selects on the same samples; the null's W = 60 value was read at a different q̂ density; the ratio compares two differently biased statistics).

(e) Run type (rule applied at the primary configuration k = 0; the others reported). k = 0: DMT − placebo per subject, null-corrected: δ_pool,c +0.00039 (sign-flip p = 0.0006, positive in 12/14) → pooling is larger on the DMT run: +0.00039, 0.11 of the DMT-run δ_run,c (+0.00349); δ_within,c +0.00052 (p = 0.1368), δ_means,c +0.00005 (p = 0.0112) (no rule) | k = 1: DMT − placebo per subject, null-corrected: δ_pool,c +0.00037 (sign-flip p = 0.0007, positive in 12/14) → pooling is larger on the DMT run: +0.00037, 0.11 of the DMT-run δ_run,c (+0.00352); δ_within,c +0.00037 (p = 0.2710), δ_means,c +0.00004 (p = 0.0189) (no rule) | k = 2: DMT − placebo per subject, null-corrected: δ_pool,c +0.00039 (sign-flip p = 0.0006, positive in 12/14) → pooling is larger on the DMT run: +0.00039, 0.11 of the DMT-run δ_run,c (+0.00355); δ_within,c +0.00047 (p = 0.1764), δ_means,c +0.00003 (p = 0.0795) (no rule) | k = 3: DMT − placebo per subject, null-corrected: δ_pool,c +0.00041 (sign-flip p = 0.0005, positive in 12/14) → pooling is larger on the DMT run: +0.00041, 0.12 of the DMT-run δ_run,c (+0.00336); δ_within,c +0.00037 (p = 0.2738), δ_means,c +0.00002 (p = 0.2560) (no rule) | k = 4: DMT − placebo per subject, null-corrected: δ_pool,c +0.00037 (sign-flip p = 0.0007, positive in 12/14) → pooling is larger on the DMT run: +0.00037, 0.11 of the DMT-run δ_run,c (+0.00349); δ_within,c +0.00038 (p = 0.2678), δ_means,c +0.00003 (p = 0.1044) (no rule) | k = 5: DMT − placebo per subject, null-corrected: δ_pool,c +0.00040 (sign-flip p = 0.0005, positive in 12/14) → pooling is larger on the DMT run: +0.00040, 0.11 of the DMT-run δ_run,c (+0.00354); δ_within,c +0.00052 (p = 0.1389), δ_means,c +0.00004 (p = 0.0157) (no rule)

(f) ts_demean, data only (no null; not read): δ_run -0.00262 [-0.00495, -0.00037]  δ_wd -0.00262 [-0.00495, -0.00037]  δ_means +0.00000 [-0.00001, +0.00002]  δ_within -0.00226 [-0.00428, -0.00034]  δ_pool -0.00030 [-0.00069, +0.00001]  δ_eps -0.00005 [-0.00011, +0.00000]  δ_d60 -0.00274 [-0.00478, -0.00079]  δ_d60_winsign +0.00160 [-0.00019, +0.00326]

