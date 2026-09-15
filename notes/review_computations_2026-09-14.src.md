# Review computations, 14 Sep 2026 — items 1–5

Companion to `notes/adversarial_review_2026-09-14.md`. Everything below is computed from the released data, the committed atom arrays and the committed scripts, in the clean environment described in that review (Python 3.12.3, numpy 2.5.3, scipy 1.18.1, phyid 6c5f2e9, rsHRF 1.7.0 for item 3). Nothing here is manuscript text and nothing proposes a framing; each item ends with what the computation shows and stops there. The CCS double-redundancy line of the review is withdrawn (your correction stands); nothing below depends on it.

Scripts (all in `notes/`, all re-runnable from the repository root with `.venv/bin/python`):

| file | what it does |
|---|---|
| `rev_inference.py` | the step-contrast inference of `06_primary_b_analysis.py` Section A (per-subject DiD, subject bootstrap 10,000, exact sign-flip over 2¹⁴, phase-randomised temporal null 1,000 surrogates, FD DiD, FD residualisation over all windows, the record's "survives" rule) factored so it applies to any per-window series with a TR-local counterpart; consumes the RNG in 06's order, `SEED = 20261120`; adds the early/late sets and the two trend corrections |
| `rev_series.py` | mean regional lag-1 autocorrelation series (window- and run-standardised) with their TR-local counterparts; ΦR from the 16 atoms |
| `rev_run.py` | runs the engine on every series (raw and deconvolved) → `notes/review_results/inference_rows_raw.csv`, `inference_rows_deconv.csv` (+ `.pkl` with per-subject DiDs) |
| `rev_deconv.py` | rsHRF blind deconvolution of every run, written as a `.mat` with the source file's structure so `01_synergy_timecourse.py` runs unchanged on it |
| `rev_sts_matched_null.py` | item 5 (three families, W = 30/60/840, 4,000 windows per condition) |
| `rev_extra.py` | the supporting facts quoted in sections 1, 3, 4 and 6 (per-subject and per-window agreement of the series, band-pass facts, variance non-stationarity, trend slopes, rsHRF summaries) |
| `rev_tables.py`, `rev_assemble.py` | render every table below from the CSVs and fill them into this note (`review_computations_2026-09-14.src.md` → `.md`); no number in a table was typed by hand |

Conventions. DiD = (post − pre)_DMT − (post − pre)_PCB per subject, group mean. W = 60: pre = windows 1–4, primary = 6–14, sensitivity = 5–14, early = 6–9, late = 10–14. W = 30 windows and the 30-TR bins of the global fit (28 units): pre 1–8, primary 11–28, sensitivity 10–28, early 11–18, late 19–28 — the sets `06_primary_b_analysis.py` uses (its sensitivity set at 30-TR resolution starts at TR 271, not at TR 241 as the W = 60 sensitivity set does). "PCB share" = placebo change / −DiD (the fraction of the DiD contributed by the placebo run's own change). "FD-resid" = the DiD after per-subject × condition OLS of the window means on window-mean FD over all windows; "survives" = same sign as raw and the residualised bootstrap CI excludes zero (the record's definition). Trend (a): a straight line fitted to all of the placebo run's windows (14 at W = 60, 28 at W = 30 and for bins) replaces the raw placebo change; trend (b): per subject, x_{c,w} = a_c + b·w + δ·[DMT ∧ post] fitted to the pre and post windows of both runs, δ reported. Units: nats for sts and ΦR; the autocorrelation is dimensionless. p-values are two-sided; 0.0010 is the floor of the 1,000-surrogate null.

## 0. Engine validation

Applied to the committed `atoms_win60_*` arrays the engine reproduces `results/primary_b_ts_gsr_win60.csv` and `primary_b_ts_demean_win60.csv` to the printed precision: ts_gsr −0.0809 [−0.1261, −0.0377], p = 0.0038, phase-null p = 0.0020 (null SD 0.0215), FD-resid −0.0649 [−0.0966, −0.0289], p = 0.0048; ts_demean −0.1031 [−0.1558, −0.0522], p = 0.0026, phase p = 0.0010 (SD 0.0264), FD-resid −0.0824 [−0.1224, −0.0372], p = 0.0048; the sensitivity rows likewise. The sts rows in the tables below are therefore the paper's own numbers, extended with the early/late sets and the trend corrections.

## 1. The lag-1 autocorrelation contrast as a primary quantity

Definition. For each subject × run × window, region i is standardised with the window's own mean and variance (ddof = 1) and the local product l_t = mean_i z_{i,t} z_{i,t+1} is stored at every consecutive TR pair inside the window; the window mean of l_t is exactly the standard lag-1 sample autocorrelation r₁ averaged over the 115 regions (checked: 0.837561 both ways). The TR-local series l_t is what the phase-randomised null scrambles, exactly as 06 scrambles the local sts series. The run-standardised variant (μ, σ² over the whole run, 30-TR bins) is the analogue of the global fit — see the caveat after its table.

{{TABLE: autocorr ts_gsr W60}}

{{TABLE: autocorr ts_demean W60}}

{{TABLE: autocorr ts_gsr W30}}

{{TABLE: autocorr ts_gsr run-standardised bins}}

{{TABLE: autocorr ts_demean run-standardised bins}}

Run-standardised caveat. The bin mean of the run-standardised product is (lag-1 covariance within the bin)/(run variance), so it moves with the bin's variance as much as with its correlation. It is in fact the window-variance ratio: per run, the correlation across bins between this series and mean_i var_window(x_i)/var_run(x_i) is 0.995 (ts_gsr; min 0.987 over the 28 runs) and 0.993 (ts_demean). The variance itself is strongly non-stationary: window variance / run variance (mean over regions, W = 60) is 1.277 in the DMT pre-injection windows and 0.889 in windows 6–14 (window 4: 1.425; window 6: 0.707), against 0.936 → 1.062 in the placebo run; DiD −0.514 [−0.674, −0.358], p = 0.0001, 14/14 negative (ts_demean −0.428 [−0.617, −0.267], p = 0.0004, 13/14). So the run-standardised rows are a variance contrast, not an autocorrelation contrast, and the numbers in them are not comparable with the windowed rows. (The global-fit sts bins are not simply variance: their correlation with the variance ratio is +0.37 on average per run, range −0.53 to +0.75.)

Relation to the sts contrast (same subjects, same windows). Per-subject DiDs, W = 60 primary set: autocorrelation vs sts Pearson r = +0.953 (ts_gsr), +0.958 (ts_demean); Spearman +0.90 / +0.93. Group-mean window series (14 windows × 2 conditions): r = +0.977 (ts_gsr), +0.938 (ts_demean); within the DMT run alone +0.986 / +0.920. The subject with the only positive sts DiD (subject 14) also has the only clearly positive autocorrelation DiD (+0.024).

Phase-randomised null, DiD in units of the null SD (primary set): autocorrelation ts_gsr W60 1.76 SD (p = 0.073), ts_demean W60 2.06 (p = 0.039), ts_gsr W30 2.44 (p = 0.011), deconvolved ts_gsr W60 2.64 (p = 0.016; item 3); sts 3.2–3.9 SD on every estimator and variant (3.77 W60 ts_gsr, 3.45 W30, 3.30 global ts_gsr, 3.91 W60 ts_demean, 3.23 global ts_demean; p ≤ 0.002).

Level of r₁ in band-passed data (supporting fact, `rev_extra.py`). 99.2 % of the power of the released series lies inside 0.01–0.08 Hz. White noise passed through an ideal 0.01–0.08 Hz band-pass at TR = 2 s has r₁ = 0.818; the observed run-level r₁ is 0.866 (ts_gsr) / 0.856 (ts_demean). The in-band spectral centroid (power-weighted mean frequency within 0.01–0.08 Hz, TRs 0–239 vs 300–839) moves up under DMT: DiD +0.0023 Hz [+0.0006, +0.0040], p = 0.022, 12/14 positive (ts_gsr); +0.0029 Hz [+0.0011, +0.0047], p = 0.011, 12/14 (ts_demean).

What it shows. The windowed autocorrelation DiD is negative on both variants and at both window lengths, significant by exact sign-flip (p = 0.011 ts_gsr W60, 0.0017 ts_demean W60, 0.016 W30), 12–13 of 14 subjects, and survives FD residualisation in the primary and sensitivity sets on every estimator and variant (the late set does not on ts_gsr at either window length). Against the phase-randomised temporal null it does not reach 0.05 for the primary cell (ts_gsr, W = 60: p = 0.073; sensitivity set 0.123) and does on ts_demean (0.039), at W = 30 (0.011) and after deconvolution (0.016). The placebo run's own r₁ rises over the session (+0.0050 primary, p = 0.14, ts_gsr; +0.0102, p = 0.008, ts_demean) and contributes 34 % / 47 % of the DiD — the same structure as the sts contrast. Early windows carry the effect (−0.0213, p = 0.0006, 13/14, placebo share 0.16); the late set is not significant on ts_gsr (−0.0093, p = 0.16). Both trend corrections leave it significant. Per subject the autocorrelation DiDs and the sts DiDs are collinear (Pearson r = 0.95 / 0.96, Spearman 0.90 / 0.93), and so are the group-mean window series (r = 0.98 / 0.94). The run-standardised (global-fit-analogue) version measures variance non-stationarity, not autocorrelation.

## 2. ΦR with full inference

ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr, with I(X;X′) = rtr + rtx + xtr + xtx and I(Y;Y′) = rtr + rty + ytr + yty, computed from the saved window-mean atoms and, for the temporal null, from the saved TR-local atoms (ΦR is linear in the atoms, so the local series is exact).

{{TABLE: PhiR ts_gsr W60}}

{{TABLE: PhiR ts_demean W60}}

{{TABLE: PhiR ts_gsr global-bins}}

{{TABLE: PhiR ts_demean global-bins}}

Relation to sts: per-subject ΦR DiD vs sts DiD, W = 60 primary set, Pearson r = −0.55 (p = 0.041, ts_gsr), −0.55 (p = 0.043, ts_demean); Spearman −0.48 / −0.70. ΦR's pre-injection level is 0.096 (W60) / 0.026 (global) nats against sts 1.16 / 1.31.

What it shows. On the primary estimator and variant ΦR does not change: +0.0007 [−0.0078, +0.0100], p = 0.90, 8/14 negative, phase p = 0.84, and every window set and both trend corrections give the same null. On ts_demean at W = 60 the DiD is positive, +0.0157 [+0.0010, +0.0326], sign-flip p = 0.085, phase p = 0.038, 4/14 negative, FD-resid CI excludes zero; trend (a) p = 0.044. At the global fit the two variants disagree in sign: ts_gsr −0.0062 [−0.0127, +0.0003], p = 0.095, phase p = 0.023, driven by the DMT run alone (−0.0075, p = 0.002; placebo −0.0013), early set −0.0088, p = 0.037, trend (b) p = 0.021; ts_demean +0.0180 [−0.0002, +0.0380], p = 0.118, phase p = 0.019. In no cell is the primary-set sign-flip p below 0.05; the phase-null p is below 0.05 in three cells (ts_demean W60, ts_gsr global, ts_demean global) whose signs disagree across variants: ts_gsr is negative at the global fit and zero at W = 60, ts_demean is positive on both estimators. After deconvolution (item 3) the ts_gsr global cell goes to −0.0032, p = 0.41, phase p = 0.23, while the W = 60 cells become positive and significant on both variants (+0.0178, p = 0.0099; +0.0350, p = 0.0009).

## 3. The primary contrast after HRF deconvolution

Method (`rev_deconv.py`). rsHRF 1.7.0 (the Python port of the toolbox Luppi et al. used), Wu et al. 2013 blind deconvolution with the toolbox defaults: canonical HRF with temporal and dispersion derivatives (`canon2dd`), point-process events at local maxima above 1 SD (`localK = 1` for TR ≤ 2 s), onset search 4–8 s, HRF length 24 s, microtime T = 3, AR(1) noise, 0.01–0.08 Hz passband for the HRF estimate; one HRF per region per run, estimated from the whole run (pre- and post-injection samples pooled); classic non-iterative Wiener deconvolution (regularisation 0.1 × mean |H|², the toolbox's `wiener = False` branch). The toolbox z-scores each series first, so the deconvolved series are in those units. Subject 2 PCB TR 839 (NaN) is filled for the estimation and restored to NaN afterwards; the constant region-20 series of subject 8 DMT is passed through as zeros so `01` excludes region 20 exactly as before. Then `scripts/01_synergy_timecourse.py` ran unchanged (`--fit-mode global` and `--fit-mode window --window-trs 60`, both variants) from a sandbox whose `external/DMT_NCT/data/` holds the deconvolved file, and the engine of section 0 ran on the outputs.

Effect on the series. The estimated HRFs do not differ between runs at the group level (time-to-peak 6.08 s DMT vs 6.07 s PCB, ts_gsr; 6.23 vs 6.16 ts_demean; 40.7–42.0 detected events per region, the same in the two runs). Run-level r₁ falls from 0.866 to 0.790 (ts_gsr) and 0.856 to 0.776 (ts_demean), i.e. below the 0.818 of a flat in-band spectrum: the Wiener step whitens within the band. 99.1 % of the deconvolved power is still inside 0.01–0.08 Hz — the released series are already band-passed, and the toolbox band-passes only its HRF-estimation input (0.01–0.08 Hz) while its deconvolution input is unfiltered (`passband_deconvolve` default all-pass). The MMI atom profile keeps its shape at a lower level — global fit, DMT pre-injection whole-brain means, raw → deconvolved (ts_gsr): sts 1.309 → 0.924, xtx 0.690 → 0.492, yty 0.672 → 0.476, rts/str 0.644 → 0.453, the four mirror atoms xts/yts/stx/sty −0.639 → −0.448, rtr 0.025 → 0.016; sts ≈ xtx + yty still (0.924 vs 0.968). Deconvolved 16-atom DiD (global, ts_gsr): sts −0.0772, xtx −0.0563, yty −0.0437, rts −0.0382, str −0.0385, xts/yts/stx/sty +0.0365 to +0.0369, rtr −0.0041; TDMI −0.1147; ts_demean: sts −0.1135, xtx −0.0969, yty −0.0744, TDMI −0.1247. At W = 60 (ts_gsr, DMT pre-injection, raw → deconvolved): sts 1.155 → 0.832, xtx 0.627 → 0.448, yty 0.613 → 0.436, rts/str 0.567 → 0.406, mirror atoms −0.535/−0.536 → −0.366/−0.367, rtr 0.039 → 0.026, TDMI 1.477 → 1.144, ΦR 0.096 → 0.119; deconvolved W60 DiD: sts −0.0782, xtx −0.0585, yty −0.0469, rts/str −0.0375/−0.0377, mirrors +0.0433 to +0.0439, rtr −0.0045.

{{TABLE: sts_deconv ts_gsr W60}}

{{TABLE: sts_deconv ts_demean W60}}

{{TABLE: sts_deconv ts_gsr global-bins}}

{{TABLE: sts_deconv ts_demean global-bins}}

{{TABLE: autocorr_deconv ts_gsr W60}}

{{TABLE: autocorr_deconv ts_demean W60}}

{{TABLE: PhiR_deconv ts_gsr W60}}

{{TABLE: PhiR_deconv ts_demean W60}}

{{TABLE: PhiR_deconv ts_gsr global-bins}}

{{TABLE: PhiR_deconv ts_demean global-bins}}

Raw vs deconvolved, primary set, side by side:

{{DECONV_COMPARISON}}

What it shows. Deconvolution removes about 30 % of the sts level (1.309 → 0.924 global, 1.155 → 0.832 at W = 60) and takes r₁ from 0.866 to 0.790. The sts contrast is unchanged: W = 60 ts_gsr −0.0782 [−0.1182, −0.0424], p = 0.0013, phase p = 0.0010, 13/14, survives FD residualisation, placebo share 0.32 (raw −0.0809, p = 0.0038, share 0.40); ts_demean −0.1003 [−0.1459, −0.0591], p = 0.0004 (raw −0.1031, p = 0.0026); global fit −0.0772 (raw −0.0801) and −0.1135 (raw −0.1035); early/late and both trend corrections as before (late set p = 0.0096 / 0.0020, raw 0.034 / 0.013). The autocorrelation contrast is larger and passes the temporal null on both variants: −0.0220, p = 0.0021, phase p = 0.016 (raw −0.0146, p = 0.011, phase p = 0.073); ts_demean −0.0264, p = 0.0009, phase p = 0.016 (raw −0.0216, p = 0.0017, phase p = 0.039). ΦR changes: at W = 60 the deconvolved ΦR DiD is positive and passes both nulls on both variants — ts_gsr +0.0178 [+0.0069, +0.0293], p = 0.0099, phase p = 0.0010, 3/14 negative, survives (raw +0.0007, p = 0.90); ts_demean +0.0350 [+0.0188, +0.0523], p = 0.0009, phase p = 0.0020, 1/14 negative (raw +0.0157, p = 0.085) — made of a placebo-run fall (ts_gsr −0.0113, p = 0.027; placebo share 0.64) and a DMT-run rise (+0.0064, p = 0.027); at the global fit the deconvolved ΦR is −0.0032, p = 0.41 (ts_gsr) and +0.0209, p = 0.093 (ts_demean), so the two estimators disagree on ΦR for ts_gsr after deconvolution as they did before it (raw +0.0007 at W = 60, −0.0062 global). The W = 60 ΦR level is 0.119 nats deconvolved (0.096 raw) against 0.023 (0.026 raw) at the global fit; by the formula, the +0.096 excess of the windowed over the global level (deconvolved, ts_gsr, DMT pre-injection) is +0.105 from the larger windowed TDMI (1.144 vs 1.040) and +0.084 from the smaller windowed xtx + yty (0.884 vs 0.968), against −0.083 from the larger windowed cross atoms rtx/rty/xtr/ytr (0.029 vs 0.008 each) and −0.009 from rtr (0.026 vs 0.016). Most of the W = 60 ΦR level is therefore estimator-dependent. The four-atom MMI structure (sts ≈ xtx + yty, mirror atoms ≈ −sts/2) is unchanged by deconvolution. Two limits of the procedure: the HRF is estimated per run from all 840 TRs, so a change of HRF shape that occurs within the DMT run after injection is not removed by it (the run-level HRFs of the two runs are indistinguishable); and the deconvolved series remain band-limited to 0.01–0.08 Hz, which by itself imposes r₁ ≈ 0.82 on white noise.

## 4. Windows 6–9 vs 10–14, and the per-subject linear trend corrections

Early/late sets and the two trend corrections for sts on every estimator and variant (the same rows for the autocorrelation and ΦR are in their tables above):

{{TABLE: sts ts_gsr W60}}

{{TABLE: sts ts_demean W60}}

{{TABLE: sts ts_gsr W30}}

{{TABLE: sts ts_gsr global-bins}}

{{TABLE: sts ts_demean global-bins}}

The slopes behind the trend corrections (sts, W = 60, mean over subjects, nats per window): placebo run over all 14 windows +0.0054 (ts_gsr) / +0.0066 (ts_demean); the shared slope b of model (b) +0.0068 / +0.0075; the DMT run over its own post windows 6–14 alone +0.0146 / +0.0138 (the post-injection recovery). Over the primary contrast (mean post index − mean pre index = 7.5 windows) the placebo line implies a placebo change of +0.0406 (ts_gsr) against the raw placebo change of +0.0324, and the shared slope +0.0511; the corrected DiDs are therefore larger in magnitude than the raw one, not smaller, and model (b)'s common slope contains the DMT run's recovery.

What it shows. sts, W = 60, ts_gsr: early −0.1029 [−0.1464, −0.0601], p = 0.0009, 13/14, phase p = 0.0010, placebo share 0.18, survives FD residualisation; late −0.0633 [−0.1147, −0.0118], p = 0.034, 10/14, phase p = 0.0060, placebo share 0.69 (placebo +0.0434, p = 0.014; DMT −0.0199, p = 0.39), survives. ts_demean: early −0.1183, p = 0.0012, share 0.18; late −0.0910, p = 0.013, share 0.60. W30 and the global fit give the same pattern (global late: ts_gsr −0.0591, p = 0.077, does not survive FD residualisation; ts_demean −0.0862, p = 0.059, does not survive). The DMT run's own late change is not distinguishable from zero on any estimator (p = 0.25–0.44); the placebo run's late rise is (p = 0.005–0.032). Trend (a): −0.0890, p = 0.0021 (ts_gsr W60); −0.1126, p = 0.0018 (ts_demean). Trend (b): −0.0995, p = 0.0007; −0.1193, p = 0.0012. Both corrections subtract more than the raw placebo change does (previous paragraph). The same early/late asymmetry holds for the autocorrelation (early −0.0213, p = 0.0006; late −0.0093, p = 0.16, ts_gsr W60) and is absent for ΦR (no set significant on ts_gsr W60).

## 5. The sts-matched null

The record (open questions, "The bias check has no sts-matched null"): "A pair of conditions with equal analytic sts but different covariance (e.g. different rtr) would test whether condition-dependent bias can manufacture an sts difference from nothing." Three families were built (`rev_sts_matched_null.py`; analytic atoms via `02_bias_check.analytic_atoms`, the same phyid downstream code the record's bias tables use; estimated sts = mean over 4,000 independent windows of `calc_PhiID` per window; "manufactured difference" = mean(shifted) − mean(baseline) ± SE, also as a share of the real primary DiD, −0.0809):

- F1: the record's asymmetric VAR(1) family (`asym_baseline`: a = (0.55, 0.40), c = (0.15, 0.05), q = 0.20, s = (1, 1.4); autocorrelation (0.605, 0.413), corr(x, y) 0.306; analytic sts 0.0942). (i) a lowered to (0.50, 0.364), the cross-coupling c solved so that analytic sts is unchanged: c = (0.107, 0.036), autocorrelation (0.536, 0.371), rtr 0.0137 → 0.0080. (ii) q raised to 0.60, a solved: a = (0.726, 0.528), autocorrelation (0.818, 0.561), corr(x, y) 0.646, rtr 0.0137 → 0.0838 (the record's "different rtr").
- F2: the record's AR family at a = 0.87 (`ar_baseline`: c = (0.025, 0.01), q = 0.05; autocorrelation (0.877, 0.871); analytic sts 1.3844, the level of the data's global fit). (i) a lowered to 0.85: no compensating value exists — over the whole stable range of c (0.001–0.237) the sts difference stays between −0.693 and −0.104, and over q ∈ [−0.9, 0.9] between −0.696 and −0.096. (ii) q raised 0.05 → 0.30, a solved: a = 0.8836, autocorrelation (0.898, 0.887), corr(x, y) 0.442, rtr 0.0163 → 0.0862.
- F3: Gaussian processes with the data's own autocorrelation function. Pooled ACF (mean over 14 subjects and 115 regions, lags 0–40, Hann-tapered to lag 40, PSD clipped at zero, NFFT 2,048): baseline = placebo run, all TRs; shifted = DMT run TRs 300–839. Realised ACFs, lags 1–6: placebo 0.868, 0.539, 0.172, −0.085, −0.174, −0.145; DMT post 0.858, 0.507, 0.123, −0.130, −0.194, −0.133. Each pair = one filter applied to two white noises with correlation q, so the lag-1 covariance is S₄ = [[1, q, r₁, q r₁], [q, 1, q r₁, r₁], [r₁, q r₁, 1, q], [q r₁, r₁, q, 1]] and the analytic atoms depend on (r₁, q) only.

Results:

| pair (true sts equal unless stated) | W = 30 | W = 60 | W = 840 |
|---|---|---|---|
| F1-i: a 0.55 → 0.50, c compensates (est. baseline sts at W60 0.0780 vs analytic 0.0942) | −0.0048 ± 0.0016 (−6 %) | −0.0075 ± 0.0015 (−9 %) | +0.0013 ± 0.0006 (+2 %) |
| F1-ii: q 0.20 → 0.60, a compensates | +0.0270 ± 0.0018 (+33 %) | +0.0127 ± 0.0016 (+16 %) | +0.0006 ± 0.0005 (+1 %) |
| F2-i: a 0.87 → 0.85 | no compensating c or q exists (true sts cannot be held fixed) | | |
| F2-ii: q 0.05 → 0.30, a compensates (est. baseline sts at W60 0.806 vs analytic 1.384) | +0.0051 ± 0.0068 (+6 %) | +0.0055 ± 0.0065 (+7 %) | +0.0236 ± 0.0023 (+29 %) |
| F3, matching by q: placebo ACF at q = 0.20 vs DMT-post ACF at any q ∈ [0, 0.95] | no matched pair: sts difference −0.599 to −0.054 | | |
| F3-b: identical S₄ (r₁ 0.8681, q = 0.20 in both), DMT PSD tilted by exp(−βω²) to restore r₁; higher lags 0.539, 0.172, −0.085, −0.173, −0.140 vs placebo 0.539, 0.172, −0.085, −0.174, −0.145 | −0.0010 ± 0.0067 (−1 %) | −0.0062 ± 0.0047 (−8 %) | +0.0013 ± 0.0013 (+2 %) |
| F3-c, **unmatched** reference: placebo ACF vs DMT-post ACF at q = 0.20; true sts 1.3853 vs 1.3166, true difference −0.0688 | −0.0511 ± 0.0066 | −0.0557 ± 0.0046 | −0.0680 ± 0.0013 |

Analytic sts of the F3 family as a function of r₁ (rows) and q (columns), nats:

| r₁ \ q | 0.00 | 0.20 | 0.40 | 0.60 | 0.80 |
|---|---|---|---|---|---|
| 0.80 | 1.022 | 1.009 | 0.968 | 0.891 | 0.758 |
| 0.84 | 1.223 | 1.209 | 1.163 | 1.076 | 0.922 |
| 0.86 | 1.346 | 1.331 | 1.283 | 1.191 | 1.025 |
| 0.87 | 1.414 | 1.399 | 1.350 | 1.255 | 1.083 |
| 0.88 | 1.489 | 1.473 | 1.423 | 1.326 | 1.147 |
| 0.90 | 1.661 | 1.644 | 1.591 | 1.488 | 1.295 |

Per-window level bias for reference: F3 baseline at W = 60 estimates 1.186 against an analytic 1.385 (−0.20); the data's W = 60 pre-injection sts is 1.155 against 1.309 at the global fit (−0.15). F2 (VAR(1) at a = 0.87) at W = 60 estimates 0.806 against 1.384 (−0.58), i.e. that family's finite-window behaviour is not the data's.

What it shows. Where an sts-matched pair can be built, the windowed estimator manufactures at W = 60 a difference of −9 % (F1-i), +16 % (F1-ii), +7 % ± 8 % (F2-ii) and −8 % ± 6 % (F3-b) of the real DiD, of either sign, and at W = 30 up to +33 % (F1-ii); at the full run length the manufactured difference is ≤ 2 % except F2-ii (+29 %, where both conditions are still 0.06–0.08 nats below their analytic value at 840 samples). Three of the matched pairs are of the kind the record's example asks for (equal analytic sts, different rtr: F1-i 0.0137 → 0.0080, F1-ii 0.0137 → 0.0838, F2-ii 0.0163 → 0.0862); F1-i manufactures a negative difference, F1-ii and F2-ii positive. F3-b has identical S₄ and therefore identical rtr and every other analytic atom; its −8 % ± 6 % at W = 60 is not distinguishable from zero. A matched pair in which the lag-1 autocorrelation falls, as it does in the data, could not be built at data-like autocorrelation: in the a = 0.87 family no cross-coupling or noise correlation restores the analytic sts after a 0.02 drop in a, and in the empirical-ACF family no cross-correlation restores it after the observed 0.010 drop in r₁, because the analytic sts of these Gaussian processes is a steep function of r₁ (≈ +0.07 nats per +0.01 in r₁ near 0.87) and a weak function of q. The observed ACF change alone, at fixed q, changes the true sts by −0.069 (against the observed DiD of −0.081) and the W = 60 estimator returns −0.056 of it.

## 6. Supporting facts not asked for (computed on the way; all in `rev_extra.py`, log `review_results/logs/rev_extra.log`)

- Variance non-stationarity (section 1 caveat): window variance / run variance, W = 60, ts_gsr, group means by window — DMT 1.14, 1.22, 1.32, 1.43, 1.00, 0.71, 0.76, 0.75, 0.79, 0.91, 0.94, 0.99, 1.07, 1.10; PCB 0.82, 0.95, 1.01, 0.96, 0.80, 0.90, 0.93, 1.01, 1.02, 1.04, 1.09, 1.10, 1.20, 1.27. The windowed sts and the window-standardised autocorrelation series each correlate with this ratio at +0.49 / +0.54 per run on average (group-mean series +0.77 / +0.73): the windows in which variance drops are the windows in which r₁ and sts drop. After deconvolution the variance DiD is −0.425 (ts_gsr), −0.303 (ts_demean).
- Group-mean sts and r₁ by window (W = 60, ts_gsr) — DMT r₁: 0.851, 0.847, 0.843, 0.851, 0.836, 0.823, 0.829, 0.833, 0.835, 0.841, 0.843, 0.841, 0.845, 0.855; DMT sts: 1.163, 1.145, 1.139, 1.176, 1.100, 1.047, 1.069, 1.079, 1.090, 1.101, 1.130, 1.127, 1.140, 1.179; PCB r₁: 0.844, 0.841, 0.849, 0.848, 0.833, 0.848, 0.844, 0.851, 0.852, 0.851, 0.851, 0.850, 0.853, 0.853; PCB sts: 1.121, 1.128, 1.150, 1.152, 1.088, 1.146, 1.140, 1.174, 1.166, 1.171, 1.181, 1.182, 1.193, 1.178.
- The per-subject sts DiDs (W60 primary, ts_gsr) are −0.0813, −0.0446, −0.1572, −0.1379, −0.0118, −0.0536, −0.0653, −0.2795, −0.1316, −0.1533, −0.0405, −0.0677, −0.0027, +0.0949, and the autocorrelation DiDs in the same order −0.0161, −0.0024, −0.0260, −0.0200, +0.0005, −0.0186, −0.0084, −0.0642, −0.0312, −0.0201, −0.0143, −0.0080, −0.0003, +0.0242.

## Files

`notes/review_results/inference_rows_raw.csv` (84 rows: every label × set in sections 1, 2, 4), `inference_rows_deconv.csv` (section 3, including the run-standardised deconvolved autocorrelation rows, which are a variance contrast like their raw counterparts: −0.359 ts_gsr, −0.269 ts_demean), the `.pkl` twins with per-subject DiDs; run logs in `notes/review_results/logs/` (`rev_run_raw.log`, `rev_run_deconv.log`, `sts_matched_null_F1/F2/F3.log`, `rev_deconv_<variant>.log`, `deconv_01_global_<variant>.log`, `deconv_01_win60_<variant>.log`, `rev_extra.log`). `notes/review_results/deconv/` holds the per-region HRFs (`hrf_<variant>.npy`, 14 × 2 × 116 × 12 at TR resolution), the event counts (`events_<variant>.npy`) and the deconvolved atom arrays (window and global, means and TR-local). The deconvolved `.mat` itself is not included (22 MB per variant, 44 MB merged); `rev_deconv.py` regenerates each variant in about 70 s.
