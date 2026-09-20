# The cross-lag budget on the data (partB12_crosslag_budget.py; git=d507728; seed=20261120)

Per subject and run, over the 6,555 pairs: δ_run = s·d at the run level (s = sign of the run-level q; d = mean of the two directions of corr(x_t, y_(t+1)) − a_y q), δ_wd = the same after removing each region's mean within each W = 60 window, δ_means = δ_run − δ_wd, δ_within = s·Σ_w π_w d_w, δ_pool = s·Σ_w π_w (a_(y,w) − ā_y) q_w, ε = δ_wd − δ_within − δ_pool (definitions and weights: notes/rev_crosslag_budget.py); beside them δ_60 = s·mean_w d_w and partB10's window-sign value mean_w sign(q_w) d_w. Mean over pairs per run; per subject the mean of the two runs; grand mean with subject-bootstrap 95 % CI (10,000 draws, seed 20261120, one set of draws per variant), exact sign-flip p, count positive; per run type. Rules recorded before the run: analysis_record.md, "The cross-lag budget: pre-run entry, 16 Sep 2026"; the null-corrected budget and the reading under those rules are in crosslag_budget_null_tables.md (partB13).

Population checks (no data):
  shared slow component λ_x = 0.25, λ_y = 0.25, a_s = 0.95, a_n = 0.8, loading +1: q = +0.2500, a_x = 0.8375, a_y = 0.8375, cross-lag +0.23750; d(x→y) = +0.028125 = q(1 − λ_y)(a_s − a_n) = +0.028125; d(y→x) = +0.028125 = q(1 − λ_x)(a_s − a_n) = +0.028125
  shared slow component λ_x = 0.25, λ_y = 0.25, a_s = 0.95, a_n = 0.8, loading -1: q = -0.2500, a_x = 0.8375, a_y = 0.8375, cross-lag -0.23750; d(x→y) = -0.028125 = q(1 − λ_y)(a_s − a_n) = -0.028125; d(y→x) = -0.028125 = q(1 − λ_x)(a_s − a_n) = -0.028125
  shared slow component λ_x = 0.3, λ_y = 0.2, a_s = 0.95, a_n = 0.8, loading +1: q = +0.2449, a_x = 0.8450, a_y = 0.8300, cross-lag +0.23270; d(x→y) = +0.029394 = q(1 − λ_y)(a_s − a_n) = +0.029394; d(y→x) = +0.025720 = q(1 − λ_x)(a_s − a_n) = +0.025720
  shared slow component λ_x = 0.1, λ_y = 0.4, a_s = 0.9, a_n = 0.85, loading -1: q = -0.2000, a_x = 0.8550, a_y = 0.8700, cross-lag -0.18000; d(x→y) = -0.006000 = q(1 − λ_y)(a_s − a_n) = -0.006000; d(y→x) = -0.009000 = q(1 − λ_x)(a_s − a_n) = -0.009000
  τ = 1 equivalence, worked example λ = 0.25, a_s = 0.95, a_n = 0.80: a = 0.8375, q = 0.2500, cross-lag 0.2375, d = +0.028125; A = Γ₁Γ₀⁻¹ = [[0.8300, 0.0300], [0.0300, 0.8300]], innovation correlation q_ε = 0.0932, c(1 − q²) = +0.028125; the VAR(1) with this A and Σ has the same Γ₀ and Γ₁ (Lyapunov check passed), so the same 4 × 4 matrix and the same sixteen τ = 1 atoms (sts = 1.15173, rtr = 0.02903).

## ts_gsr (392 windows checked against diag_series xcorr_dev; max |δ_run − (δ_within + δ_pool + δ_means + ε)| over pairs and runs 6.9e-18; δ_run and the window-sign value reproduce partB10's per-run values to 1e-12)

Run-level mean pair a 0.8666 (DMT 0.8638, PCB 0.8694); mean |q̂| 0.1945 (DMT 0.1904, PCB 0.1987); fraction of pairs with q̂ < 0 0.545, |q̂| < 0.05 0.168, |q̂| < 0.10 0.328; mean Σ_w π_w 0.9624.
δ_run: DMT +0.00381 [+0.00339, +0.00424], PCB +0.00299 [+0.00235, +0.00363]; grand mean +0.00340 [+0.00300, +0.00380] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects
δ_wd: DMT +0.00379 [+0.00338, +0.00421], PCB +0.00299 [+0.00235, +0.00363]; grand mean +0.00339 [+0.00299, +0.00378] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects
δ_means: DMT +0.00002 [-0.00000, +0.00004], PCB +0.00000 [-0.00002, +0.00002]; grand mean +0.00001 [-0.00000, +0.00003] (subject bootstrap, 10000 draws), exact sign-flip p = 0.1365, positive in 8/14 subjects
δ_within: DMT +0.00310 [+0.00277, +0.00343], PCB +0.00272 [+0.00215, +0.00327]; grand mean +0.00291 [+0.00257, +0.00325] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects
δ_pool: DMT +0.00069 [+0.00053, +0.00086], PCB +0.00030 [+0.00019, +0.00042]; grand mean +0.00050 [+0.00038, +0.00062] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects
δ_eps: DMT -0.00000 [-0.00005, +0.00004], PCB -0.00003 [-0.00005, -0.00001]; grand mean -0.00002 [-0.00004, +0.00001] (subject bootstrap, 10000 draws), exact sign-flip p = 0.2068, positive in 5/14 subjects
δ_60 (run-level sign): DMT +0.00264 [+0.00227, +0.00301], PCB +0.00226 [+0.00170, +0.00280]; grand mean +0.00245 [+0.00212, +0.00281] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects
window-sign value (partB10): DMT +0.00615 [+0.00575, +0.00660], PCB +0.00608 [+0.00535, +0.00685]; grand mean +0.00611 [+0.00563, +0.00665] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0001, positive in 14/14 subjects
Shares of δ_run (grand means): δ_within +0.856, δ_pool +0.146, δ_means +0.004, δ_eps -0.005
Per-subject δ_run (mean of the two runs): [0.00337 0.00200 0.00316 0.00440 0.00279 0.00453 0.00350 0.00386 0.00459 0.00245 0.00258 0.00372 0.00304 0.00361]
Per-subject δ_within: [0.00312 0.00167 0.00282 0.00396 0.00249 0.00400 0.00261 0.00300 0.00379 0.00224 0.00233 0.00322 0.00263 0.00286]
Per-subject δ_pool: [0.00032 0.00037 0.00032 0.00044 0.00030 0.00054 0.00076 0.00092 0.00086 0.00019 0.00028 0.00054 0.00038 0.00074]
Per-subject δ_means: [ 2.84342e-06 -1.43874e-06  2.27692e-05  4.24604e-05 -1.92625e-05  2.39385e-06  5.04457e-05 -1.99602e-05  6.76595e-05  4.34749e-05 -2.10285e-05 -1.69346e-06  1.71125e-05 -1.73262e-05]

## ts_demean (392 windows checked against diag_series xcorr_dev; max |δ_run − (δ_within + δ_pool + δ_means + ε)| over pairs and runs 6.9e-18; δ_run and the window-sign value reproduce partB10's per-run values to 1e-12)

Run-level mean pair a 0.8567 (DMT 0.8532, PCB 0.8602); mean |q̂| 0.2544 (DMT 0.2684, PCB 0.2403); fraction of pairs with q̂ < 0 0.196, |q̂| < 0.05 0.128, |q̂| < 0.10 0.253; mean Σ_w π_w 0.9646.
δ_run: DMT -0.00324 [-0.00614, -0.00079], PCB -0.00199 [-0.00465, +0.00041]; grand mean -0.00262 [-0.00495, -0.00037] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0532, positive in 5/14 subjects
δ_wd: DMT -0.00324 [-0.00615, -0.00078], PCB -0.00199 [-0.00465, +0.00040]; grand mean -0.00262 [-0.00495, -0.00037] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0536, positive in 5/14 subjects
δ_means: DMT -0.00000 [-0.00003, +0.00003], PCB +0.00000 [-0.00002, +0.00002]; grand mean +0.00000 [-0.00001, +0.00002] (subject bootstrap, 10000 draws), exact sign-flip p = 0.9149, positive in 6/14 subjects
δ_within: DMT -0.00270 [-0.00498, -0.00073], PCB -0.00182 [-0.00418, +0.00036]; grand mean -0.00226 [-0.00428, -0.00034] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0537, positive in 6/14 subjects
δ_pool: DMT -0.00047 [-0.00120, +0.00011], PCB -0.00014 [-0.00041, +0.00009]; grand mean -0.00030 [-0.00069, +0.00001] (subject bootstrap, 10000 draws), exact sign-flip p = 0.1296, positive in 6/14 subjects
δ_eps: DMT -0.00007 [-0.00013, -0.00001], PCB -0.00004 [-0.00014, +0.00005]; grand mean -0.00005 [-0.00011, +0.00000] (subject bootstrap, 10000 draws), exact sign-flip p = 0.1117, positive in 4/14 subjects
δ_60 (run-level sign): DMT -0.00313 [-0.00549, -0.00109], PCB -0.00235 [-0.00472, -0.00017]; grand mean -0.00274 [-0.00478, -0.00079] (subject bootstrap, 10000 draws), exact sign-flip p = 0.0270, positive in 3/14 subjects
window-sign value (partB10): DMT +0.00108 [-0.00090, +0.00285], PCB +0.00212 [+0.00010, +0.00393]; grand mean +0.00160 [-0.00019, +0.00326] (subject bootstrap, 10000 draws), exact sign-flip p = 0.1061, positive in 9/14 subjects
Shares of δ_run (grand means): δ_within +0.864, δ_pool +0.116, δ_means -0.000, δ_eps +0.020
Per-subject δ_run (mean of the two runs): [-0.00559 -0.00065 -0.00046 -0.00090  0.00046  0.00245  0.00035 -0.00172 -0.00725 -0.00902  0.00188 -0.00828 -0.01042  0.00253]
Per-subject δ_within: [-5.28493e-03 -6.81841e-04  2.99972e-05 -9.22317e-04  4.14634e-04  2.10184e-03  2.40307e-04 -1.38265e-03 -5.72414e-03 -8.01739e-03  1.71123e-03 -7.80996e-03 -8.23768e-03  1.91994e-03]
Per-subject δ_pool: [-3.18937e-04  4.97321e-05 -3.62001e-04 -9.63657e-05  5.32312e-05  3.46460e-04  1.38382e-04 -2.84217e-04 -1.29174e-03 -7.69849e-04  2.21743e-04 -2.64544e-04 -2.14365e-03  4.68918e-04]
Per-subject δ_means: [ 4.13964e-05 -1.82712e-06  7.94587e-06  1.99351e-05 -2.59160e-05 -3.68599e-06 -1.35827e-05 -2.33879e-05 -2.78091e-05  6.54788e-05  1.70373e-05 -3.74814e-05  5.46367e-06 -1.17876e-05]

