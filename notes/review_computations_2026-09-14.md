# Review computations, 14 Sep 2026 — items 1–5
git=d507728

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

**autocorr ts_gsr W60** — pre-injection level (windows 1–4) DMT 0.8479, PCB 0.8455

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.0146 [-0.0251, -0.0052] | 0.0106 | 12 | 0.0729 | -0.0097 (0.043) | +0.0050 (0.142) | 0.34 | -0.0123 [-0.0199, -0.0041], 0.0135 | yes |
| sensitivity (5–14) | -0.0131 [-0.0231, -0.0032] | 0.0211 | 10 | 0.1229 | -0.0099 (0.035) | +0.0032 (0.313) | 0.24 | -0.0102 [-0.0178, -0.0018], 0.0369 | yes |
| early (6–9) | -0.0213 [-0.0304, -0.0125] | 0.0006 | 13 | 0.0250 | -0.0180 (0.001) | +0.0033 (0.346) | 0.16 | -0.0170 [-0.0241, -0.0096], 0.0012 | yes |
| late (10–14) | -0.0093 [-0.0214, +0.0022] | 0.1615 | 9 | 0.3387 | -0.0030 (0.555) | +0.0063 (0.075) | 0.67 | -0.0085 [-0.0178, +0.0018], 0.1240 | no |
| trend (a): placebo line | -0.0162 [-0.0262, -0.0069] | 0.0049 | 12 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0190 [-0.0282, -0.0103] | 0.0016 | 13 | – | – | – | – | – | – |

**autocorr ts_demean W60** — pre-injection level (windows 1–4) DMT 0.8382, PCB 0.8329

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.0216 [-0.0319, -0.0116] | 0.0017 | 13 | 0.0390 | -0.0114 (0.055) | +0.0102 (0.008) | 0.47 | -0.0175 [-0.0250, -0.0085], 0.0033 | yes |
| sensitivity (5–14) | -0.0181 [-0.0279, -0.0080] | 0.0048 | 12 | 0.0939 | -0.0101 (0.067) | +0.0081 (0.022) | 0.44 | -0.0141 [-0.0218, -0.0050], 0.0103 | yes |
| early (6–9) | -0.0244 [-0.0331, -0.0157] | 0.0005 | 12 | 0.0539 | -0.0181 (0.006) | +0.0063 (0.073) | 0.26 | -0.0211 [-0.0286, -0.0134], 0.0007 | yes |
| late (10–14) | -0.0193 [-0.0316, -0.0069] | 0.0114 | 11 | 0.1179 | -0.0060 (0.321) | +0.0133 (0.003) | 0.69 | -0.0146 [-0.0245, -0.0028], 0.0294 | yes |
| trend (a): placebo line | -0.0228 [-0.0341, -0.0120] | 0.0020 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0235 [-0.0345, -0.0125] | 0.0022 | 13 | – | – | – | – | – | – |

**autocorr ts_gsr W30** — pre-injection level (windows 1–8) DMT 0.8218, PCB 0.8192

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 11–28) | -0.0142 [-0.0233, -0.0044] | 0.0165 | 13 | 0.0110 | -0.0087 (0.068) | +0.0054 (0.062) | 0.38 | -0.0126 [-0.0206, -0.0035], 0.0175 | yes |
| sensitivity (10–28) | -0.0139 [-0.0234, -0.0040] | 0.0210 | 11 | 0.0120 | -0.0094 (0.054) | +0.0045 (0.107) | 0.32 | -0.0122 [-0.0204, -0.0029], 0.0228 | yes |
| early (11–18) | -0.0200 [-0.0289, -0.0107] | 0.0020 | 12 | 0.0010 | -0.0159 (0.003) | +0.0041 (0.212) | 0.20 | -0.0171 [-0.0249, -0.0083], 0.0034 | yes |
| late (19–28) | -0.0095 [-0.0202, +0.0016] | 0.1274 | 10 | 0.1658 | -0.0030 (0.570) | +0.0065 (0.025) | 0.69 | -0.0090 [-0.0182, +0.0015], 0.1090 | no |
| trend (a): placebo line | -0.0151 [-0.0237, -0.0059] | 0.0089 | 12 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0177 [-0.0262, -0.0088] | 0.0028 | 13 | – | – | – | – | – | – |

**autocorr ts_gsr run-standardised bins** — pre-injection level (bins 1–8) DMT 1.1035, PCB 0.8054

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.4580 [-0.6018, -0.3200] | 0.0001 | 14 | 0.0010 | -0.3448 (0.000) | +0.1133 (0.002) | 0.25 | -0.3705 [-0.5024, -0.2456], 0.0004 | yes |
| sensitivity (10–28) | -0.4517 [-0.5968, -0.3171] | 0.0002 | 13 | 0.0010 | -0.3536 (0.000) | +0.0980 (0.008) | 0.22 | -0.3670 [-0.4952, -0.2451], 0.0005 | yes |
| early (11–18) | -0.5008 [-0.6158, -0.3872] | 0.0001 | 14 | 0.0010 | -0.4728 (0.000) | +0.0280 (0.298) | 0.06 | -0.4310 [-0.5547, -0.3188], 0.0001 | yes |
| late (19–28) | -0.4238 [-0.5957, -0.2551] | 0.0009 | 12 | 0.0010 | -0.2423 (0.011) | +0.1815 (0.000) | 0.43 | -0.3220 [-0.4636, -0.1744], 0.0017 | yes |
| trend (a): placebo line | -0.5189 [-0.6709, -0.3737] | 0.0001 | 14 | – | – | – | – | – | – |
| trend (b): shared slope | -0.5585 [-0.6989, -0.4204] | 0.0001 | 14 | – | – | – | – | – | – |

**autocorr ts_demean run-standardised bins** — pre-injection level (bins 1–8) DMT 1.0306, PCB 0.7903

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.3846 [-0.5419, -0.2464] | 0.0004 | 13 | 0.0010 | -0.2685 (0.000) | +0.1160 (0.017) | 0.30 | -0.2964 [-0.4293, -0.1812], 0.0007 | yes |
| sensitivity (10–28) | -0.3737 [-0.5306, -0.2356] | 0.0005 | 12 | 0.0010 | -0.2755 (0.000) | +0.0982 (0.031) | 0.26 | -0.2932 [-0.4269, -0.1746], 0.0007 | yes |
| early (11–18) | -0.4202 [-0.5545, -0.2919] | 0.0001 | 14 | 0.0010 | -0.3888 (0.000) | +0.0314 (0.385) | 0.07 | -0.3788 [-0.4981, -0.2723], 0.0001 | yes |
| late (19–28) | -0.3560 [-0.5455, -0.1849] | 0.0011 | 11 | 0.0010 | -0.1723 (0.044) | +0.1837 (0.005) | 0.52 | -0.2304 [-0.3878, -0.0788], 0.0121 | yes |
| trend (a): placebo line | -0.4427 [-0.5985, -0.3031] | 0.0001 | 14 | – | – | – | – | – | – |
| trend (b): shared slope | -0.4805 [-0.6268, -0.3456] | 0.0001 | 14 | – | – | – | – | – | – |

Run-standardised caveat. The bin mean of the run-standardised product is (lag-1 covariance within the bin)/(run variance), so it moves with the bin's variance as much as with its correlation. It is in fact the window-variance ratio: per run, the correlation across bins between this series and mean_i var_window(x_i)/var_run(x_i) is 0.995 (ts_gsr; min 0.987 over the 28 runs) and 0.993 (ts_demean). The variance itself is strongly non-stationary: window variance / run variance (mean over regions, W = 60) is 1.277 in the DMT pre-injection windows and 0.889 in windows 6–14 (window 4: 1.425; window 6: 0.707), against 0.936 → 1.062 in the placebo run; DiD −0.514 [−0.674, −0.358], p = 0.0001, 14/14 negative (ts_demean −0.428 [−0.617, −0.267], p = 0.0004, 13/14). So the run-standardised rows are a variance contrast, not an autocorrelation contrast, and the numbers in them are not comparable with the windowed rows. (The global-fit sts bins are not simply variance: their correlation with the variance ratio is +0.37 on average per run, range −0.53 to +0.75.)

Relation to the sts contrast (same subjects, same windows). Per-subject DiDs, W = 60 primary set: autocorrelation vs sts Pearson r = +0.953 (ts_gsr), +0.958 (ts_demean); Spearman +0.90 / +0.93. Group-mean window series (14 windows × 2 conditions): r = +0.977 (ts_gsr), +0.938 (ts_demean); within the DMT run alone +0.986 / +0.920. The subject with the only positive sts DiD (subject 14) also has the only clearly positive autocorrelation DiD (+0.024).

Phase-randomised null, DiD in units of the null SD (primary set): autocorrelation ts_gsr W60 1.76 SD (p = 0.073), ts_demean W60 2.06 (p = 0.039), ts_gsr W30 2.44 (p = 0.011), deconvolved ts_gsr W60 2.64 (p = 0.016; item 3); sts 3.2–3.9 SD on every estimator and variant (3.77 W60 ts_gsr, 3.45 W30, 3.30 global ts_gsr, 3.91 W60 ts_demean, 3.23 global ts_demean; p ≤ 0.002).

Level of r₁ in band-passed data (supporting fact, `rev_extra.py`). 99.2 % of the power of the released series lies inside 0.01–0.08 Hz. White noise passed through an ideal 0.01–0.08 Hz band-pass at TR = 2 s has r₁ = 0.818; the observed run-level r₁ is 0.866 (ts_gsr) / 0.856 (ts_demean). The in-band spectral centroid (power-weighted mean frequency within 0.01–0.08 Hz, TRs 0–239 vs 300–839) moves up under DMT: DiD +0.0023 Hz [+0.0006, +0.0040], p = 0.022, 12/14 positive (ts_gsr); +0.0029 Hz [+0.0011, +0.0047], p = 0.011, 12/14 (ts_demean).

What it shows. The windowed autocorrelation DiD is negative on both variants and at both window lengths, significant by exact sign-flip (p = 0.011 ts_gsr W60, 0.0017 ts_demean W60, 0.016 W30), 12–13 of 14 subjects, and survives FD residualisation in the primary and sensitivity sets on every estimator and variant (the late set does not on ts_gsr at either window length). Against the phase-randomised temporal null it does not reach 0.05 for the primary cell (ts_gsr, W = 60: p = 0.073; sensitivity set 0.123) and does on ts_demean (0.039), at W = 30 (0.011) and after deconvolution (0.016). The placebo run's own r₁ rises over the session (+0.0050 primary, p = 0.14, ts_gsr; +0.0102, p = 0.008, ts_demean) and contributes 34 % / 47 % of the DiD — the same structure as the sts contrast. Early windows carry the effect (−0.0213, p = 0.0006, 13/14, placebo share 0.16); the late set is not significant on ts_gsr (−0.0093, p = 0.16). Both trend corrections leave it significant. Per subject the autocorrelation DiDs and the sts DiDs are collinear (Pearson r = 0.95 / 0.96, Spearman 0.90 / 0.93), and so are the group-mean window series (r = 0.98 / 0.94). The run-standardised (global-fit-analogue) version measures variance non-stationarity, not autocorrelation.

## 2. ΦR with full inference

ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr, with I(X;X′) = rtr + rtx + xtr + xtx and I(Y;Y′) = rtr + rty + ytr + yty, computed from the saved window-mean atoms and, for the temporal null, from the saved TR-local atoms (ΦR is linear in the atoms, so the local series is exact).

**PhiR ts_gsr W60** — pre-injection level (windows 1–4) DMT 0.0961, PCB 0.1003

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | +0.0007 [-0.0078, +0.0100] | 0.8971 | 8 | 0.8372 | -0.0026 (0.165) | -0.0033 (0.406) | 5.01 | +0.0007 [-0.0056, +0.0077], 0.8381 | no |
| sensitivity (5–14) | +0.0006 [-0.0074, +0.0101] | 0.9094 | 8 | 0.8541 | -0.0022 (0.264) | -0.0028 (0.466) | 4.76 | +0.0006 [-0.0052, +0.0072], 0.8628 | no |
| early (6–9) | +0.0005 [-0.0090, +0.0113] | 0.9355 | 8 | 0.9071 | -0.0033 (0.183) | -0.0038 (0.364) | 8.06 | +0.0001 [-0.0080, +0.0088], 0.9910 | no |
| late (10–14) | +0.0008 [-0.0084, +0.0099] | 0.8663 | 7 | 0.8352 | -0.0021 (0.188) | -0.0029 (0.496) | 3.59 | +0.0013 [-0.0049, +0.0076], 0.6975 | no |
| trend (a): placebo line | +0.0001 [-0.0082, +0.0088] | 0.9862 | 8 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0011 [-0.0084, +0.0069] | 0.7822 | 9 | – | – | – | – | – | – |

**PhiR ts_demean W60** — pre-injection level (windows 1–4) DMT 0.1208, PCB 0.1248

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | +0.0157 [+0.0010, +0.0326] | 0.0853 | 4 | 0.0380 | +0.0116 (0.129) | -0.0041 (0.378) | 0.26 | +0.0152 [+0.0007, +0.0320], 0.0928 | yes |
| sensitivity (5–14) | +0.0136 [-0.0002, +0.0294] | 0.1071 | 5 | 0.0649 | +0.0111 (0.129) | -0.0025 (0.558) | 0.18 | +0.0126 [-0.0004, +0.0281], 0.1334 | no |
| early (6–9) | +0.0127 [-0.0017, +0.0293] | 0.1523 | 5 | 0.1239 | +0.0107 (0.183) | -0.0020 (0.620) | 0.16 | +0.0107 [-0.0028, +0.0269], 0.2152 | no |
| late (10–14) | +0.0181 [+0.0013, +0.0379] | 0.0944 | 5 | 0.0260 | +0.0123 (0.161) | -0.0058 (0.284) | 0.32 | +0.0188 [+0.0016, +0.0384], 0.0901 | yes |
| trend (a): placebo line | +0.0163 [+0.0033, +0.0303] | 0.0441 | 4 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0139 [+0.0005, +0.0280] | 0.0797 | 5 | – | – | – | – | – | – |

**PhiR ts_gsr global-bins** — pre-injection level (bins 1–8) DMT 0.0257, PCB 0.0250

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.0062 [-0.0127, +0.0003] | 0.0953 | 9 | 0.0230 | -0.0075 (0.002) | -0.0013 (0.535) | -0.21 | -0.0059 [-0.0111, -0.0006], 0.0581 | yes |
| sensitivity (10–28) | -0.0065 [-0.0127, -0.0003] | 0.0756 | 9 | 0.0120 | -0.0078 (0.001) | -0.0014 (0.499) | -0.21 | -0.0061 [-0.0112, -0.0009], 0.0455 | yes |
| early (11–18) | -0.0088 [-0.0157, -0.0017] | 0.0370 | 9 | 0.0050 | -0.0103 (0.001) | -0.0015 (0.422) | -0.17 | -0.0080 [-0.0140, -0.0018], 0.0304 | yes |
| late (19–28) | -0.0042 [-0.0112, +0.0027] | 0.2736 | 9 | 0.1588 | -0.0054 (0.016) | -0.0012 (0.661) | -0.28 | -0.0042 [-0.0094, +0.0012], 0.1512 | no |
| trend (a): placebo line | -0.0072 [-0.0141, -0.0006] | 0.0652 | 10 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0090 [-0.0153, -0.0026] | 0.0208 | 10 | – | – | – | – | – | – |

**PhiR ts_demean global-bins** — pre-injection level (bins 1–8) DMT 0.0464, PCB 0.0506

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | +0.0180 [-0.0002, +0.0380] | 0.1177 | 5 | 0.0190 | +0.0137 (0.160) | -0.0043 (0.278) | 0.24 | +0.0181 [+0.0002, +0.0399], 0.1166 | yes |
| sensitivity (10–28) | +0.0180 [-0.0001, +0.0378] | 0.1171 | 5 | 0.0180 | +0.0131 (0.171) | -0.0049 (0.221) | 0.27 | +0.0176 [-0.0003, +0.0390], 0.1243 | no |
| early (11–18) | +0.0136 [-0.0044, +0.0344] | 0.2484 | 5 | 0.1399 | +0.0115 (0.275) | -0.0020 (0.616) | 0.15 | +0.0111 [-0.0044, +0.0301], 0.2698 | no |
| late (19–28) | +0.0216 [+0.0011, +0.0445] | 0.0856 | 5 | 0.0100 | +0.0155 (0.145) | -0.0061 (0.153) | 0.28 | +0.0236 [+0.0023, +0.0489], 0.0950 | yes |
| trend (a): placebo line | +0.0168 [+0.0016, +0.0339] | 0.0837 | 4 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0142 [-0.0012, +0.0306] | 0.1350 | 5 | – | – | – | – | – | – |

Relation to sts: per-subject ΦR DiD vs sts DiD, W = 60 primary set, Pearson r = −0.55 (p = 0.041, ts_gsr), −0.55 (p = 0.043, ts_demean); Spearman −0.48 / −0.70. ΦR's pre-injection level is 0.096 (W60) / 0.026 (global) nats against sts 1.16 / 1.31.

What it shows. On the primary estimator and variant ΦR does not change: +0.0007 [−0.0078, +0.0100], p = 0.90, 8/14 negative, phase p = 0.84, and every window set and both trend corrections give the same null. On ts_demean at W = 60 the DiD is positive, +0.0157 [+0.0010, +0.0326], sign-flip p = 0.085, phase p = 0.038, 4/14 negative, FD-resid CI excludes zero; trend (a) p = 0.044. At the global fit the two variants disagree in sign: ts_gsr −0.0062 [−0.0127, +0.0003], p = 0.095, phase p = 0.023, driven by the DMT run alone (−0.0075, p = 0.002; placebo −0.0013), early set −0.0088, p = 0.037, trend (b) p = 0.021; ts_demean +0.0180 [−0.0002, +0.0380], p = 0.118, phase p = 0.019. In no cell is the primary-set sign-flip p below 0.05; the phase-null p is below 0.05 in three cells (ts_demean W60, ts_gsr global, ts_demean global) whose signs disagree across variants: ts_gsr is negative at the global fit and zero at W = 60, ts_demean is positive on both estimators. After deconvolution (item 3) the ts_gsr global cell goes to −0.0032, p = 0.41, phase p = 0.23, while the W = 60 cells become positive and significant on both variants (+0.0178, p = 0.0099; +0.0350, p = 0.0009).

## 3. The primary contrast after HRF deconvolution

Method (`rev_deconv.py`). rsHRF 1.7.0 (the Python port of the toolbox Luppi et al. used), Wu et al. 2013 blind deconvolution with the toolbox defaults: canonical HRF with temporal and dispersion derivatives (`canon2dd`), point-process events at local maxima above 1 SD (`localK = 1` for TR ≤ 2 s), onset search 4–8 s, HRF length 24 s, microtime T = 3, AR(1) noise, 0.01–0.08 Hz passband for the HRF estimate; one HRF per region per run, estimated from the whole run (pre- and post-injection samples pooled); classic non-iterative Wiener deconvolution (regularisation 0.1 × mean |H|², the toolbox's `wiener = False` branch). The toolbox z-scores each series first, so the deconvolved series are in those units. Subject 2 PCB TR 839 (NaN) is filled for the estimation and restored to NaN afterwards; the constant region-20 series of subject 8 DMT is passed through as zeros so `01` excludes region 20 exactly as before. Then `scripts/01_synergy_timecourse.py` ran unchanged (`--fit-mode global` and `--fit-mode window --window-trs 60`, both variants) from a sandbox whose `external/DMT_NCT/data/` holds the deconvolved file, and the engine of section 0 ran on the outputs.

Effect on the series. The estimated HRFs do not differ between runs at the group level (time-to-peak 6.08 s DMT vs 6.07 s PCB, ts_gsr; 6.23 vs 6.16 ts_demean; 40.7–42.0 detected events per region, the same in the two runs). Run-level r₁ falls from 0.866 to 0.790 (ts_gsr) and 0.856 to 0.776 (ts_demean), i.e. below the 0.818 of a flat in-band spectrum: the Wiener step whitens within the band. 99.1 % of the deconvolved power is still inside 0.01–0.08 Hz — the released series are already band-passed, and the toolbox band-passes only its HRF-estimation input (0.01–0.08 Hz) while its deconvolution input is unfiltered (`passband_deconvolve` default all-pass). The MMI atom profile keeps its shape at a lower level — global fit, DMT pre-injection whole-brain means, raw → deconvolved (ts_gsr): sts 1.309 → 0.924, xtx 0.690 → 0.492, yty 0.672 → 0.476, rts/str 0.644 → 0.453, the four mirror atoms xts/yts/stx/sty −0.639 → −0.448, rtr 0.025 → 0.016; sts ≈ xtx + yty still (0.924 vs 0.968). Deconvolved 16-atom DiD (global, ts_gsr): sts −0.0772, xtx −0.0563, yty −0.0437, rts −0.0382, str −0.0385, xts/yts/stx/sty +0.0365 to +0.0369, rtr −0.0041; TDMI −0.1147; ts_demean: sts −0.1135, xtx −0.0969, yty −0.0744, TDMI −0.1247. At W = 60 (ts_gsr, DMT pre-injection, raw → deconvolved): sts 1.155 → 0.832, xtx 0.627 → 0.448, yty 0.613 → 0.436, rts/str 0.567 → 0.406, mirror atoms −0.535/−0.536 → −0.366/−0.367, rtr 0.039 → 0.026, TDMI 1.477 → 1.144, ΦR 0.096 → 0.119; deconvolved W60 DiD: sts −0.0782, xtx −0.0585, yty −0.0469, rts/str −0.0375/−0.0377, mirrors +0.0433 to +0.0439, rtr −0.0045.

**sts_deconv ts_gsr W60** — pre-injection level (windows 1–4) DMT 0.8315, PCB 0.8078

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.0782 [-0.1182, -0.0424] | 0.0013 | 13 | 0.0010 | -0.0532 (0.004) | +0.0250 (0.057) | 0.32 | -0.0695 [-0.0983, -0.0390], 0.0016 | yes |
| sensitivity (5–14) | -0.0727 [-0.1117, -0.0367] | 0.0017 | 12 | 0.0010 | -0.0554 (0.003) | +0.0173 (0.168) | 0.24 | -0.0628 [-0.0908, -0.0336], 0.0022 | yes |
| early (6–9) | -0.0959 [-0.1354, -0.0568] | 0.0006 | 13 | 0.0010 | -0.0773 (0.000) | +0.0185 (0.156) | 0.19 | -0.0806 [-0.1145, -0.0482], 0.0007 | yes |
| late (10–14) | -0.0641 [-0.1089, -0.0236] | 0.0096 | 12 | 0.0020 | -0.0339 (0.078) | +0.0302 (0.031) | 0.47 | -0.0606 [-0.0924, -0.0243], 0.0071 | yes |
| trend (a): placebo line | -0.0821 [-0.1211, -0.0482] | 0.0009 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0856 [-0.1221, -0.0536] | 0.0004 | 13 | – | – | – | – | – | – |

**sts_deconv ts_demean W60** — pre-injection level (windows 1–4) DMT 0.7869, PCB 0.7613

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.1003 [-0.1459, -0.0591] | 0.0004 | 13 | 0.0010 | -0.0694 (0.008) | +0.0309 (0.046) | 0.31 | -0.0873 [-0.1219, -0.0520], 0.0006 | yes |
| sensitivity (5–14) | -0.0935 [-0.1375, -0.0529] | 0.0006 | 12 | 0.0010 | -0.0704 (0.006) | +0.0231 (0.117) | 0.25 | -0.0795 [-0.1141, -0.0460], 0.0009 | yes |
| early (6–9) | -0.1102 [-0.1521, -0.0698] | 0.0002 | 13 | 0.0010 | -0.0927 (0.001) | +0.0174 (0.195) | 0.16 | -0.0946 [-0.1307, -0.0610], 0.0002 | yes |
| late (10–14) | -0.0924 [-0.1460, -0.0444] | 0.0020 | 11 | 0.0010 | -0.0508 (0.063) | +0.0416 (0.021) | 0.45 | -0.0814 [-0.1254, -0.0381], 0.0038 | yes |
| trend (a): placebo line | -0.1074 [-0.1575, -0.0635] | 0.0005 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.1070 [-0.1540, -0.0650] | 0.0004 | 13 | – | – | – | – | – | – |

**sts_deconv ts_gsr global-bins** — pre-injection level (bins 1–8) DMT 0.9244, PCB 0.9006

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.0772 [-0.1230, -0.0382] | 0.0018 | 13 | 0.0010 | -0.0536 (0.010) | +0.0236 (0.094) | 0.31 | -0.0693 [-0.1015, -0.0356], 0.0024 | yes |
| sensitivity (10–28) | -0.0766 [-0.1211, -0.0373] | 0.0017 | 13 | 0.0010 | -0.0559 (0.008) | +0.0207 (0.132) | 0.27 | -0.0685 [-0.0985, -0.0352], 0.0023 | yes |
| early (11–18) | -0.0982 [-0.1438, -0.0574] | 0.0005 | 13 | 0.0010 | -0.0777 (0.001) | +0.0205 (0.121) | 0.21 | -0.0850 [-0.1185, -0.0509], 0.0006 | yes |
| late (19–28) | -0.0603 [-0.1126, -0.0149] | 0.0204 | 11 | 0.0090 | -0.0342 (0.122) | +0.0261 (0.098) | 0.43 | -0.0567 [-0.0932, -0.0178], 0.0157 | yes |
| trend (a): placebo line | -0.0760 [-0.1220, -0.0372] | 0.0016 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0825 [-0.1244, -0.0467] | 0.0007 | 13 | – | – | – | – | – | – |

**sts_deconv ts_demean global-bins** — pre-injection level (bins 1–8) DMT 0.8676, PCB 0.8406

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.1135 [-0.1712, -0.0586] | 0.0020 | 13 | 0.0010 | -0.0790 (0.022) | +0.0346 (0.050) | 0.30 | -0.1024 [-0.1528, -0.0513], 0.0024 | yes |
| sensitivity (10–28) | -0.1122 [-0.1697, -0.0574] | 0.0020 | 13 | 0.0010 | -0.0799 (0.020) | +0.0323 (0.065) | 0.29 | -0.1005 [-0.1496, -0.0490], 0.0024 | yes |
| early (11–18) | -0.1233 [-0.1729, -0.0728] | 0.0010 | 13 | 0.0010 | -0.1049 (0.004) | +0.0184 (0.223) | 0.15 | -0.1095 [-0.1529, -0.0656], 0.0007 | yes |
| late (19–28) | -0.1058 [-0.1777, -0.0396] | 0.0072 | 12 | 0.0020 | -0.0583 (0.109) | +0.0475 (0.025) | 0.45 | -0.0967 [-0.1604, -0.0368], 0.0111 | yes |
| trend (a): placebo line | -0.1181 [-0.1828, -0.0585] | 0.0024 | 12 | – | – | – | – | – | – |
| trend (b): shared slope | -0.1208 [-0.1823, -0.0611] | 0.0024 | 13 | – | – | – | – | – | – |

**autocorr_deconv ts_gsr W60** — pre-injection level (windows 1–4) DMT 0.7833, PCB 0.7766

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.0220 [-0.0327, -0.0116] | 0.0021 | 12 | 0.0160 | -0.0157 (0.007) | +0.0063 (0.077) | 0.29 | -0.0200 [-0.0286, -0.0105], 0.0024 | yes |
| sensitivity (5–14) | -0.0203 [-0.0309, -0.0097] | 0.0034 | 12 | 0.0220 | -0.0165 (0.004) | +0.0038 (0.275) | 0.19 | -0.0178 [-0.0261, -0.0087], 0.0040 | yes |
| early (6–9) | -0.0285 [-0.0384, -0.0185] | 0.0004 | 13 | 0.0030 | -0.0242 (0.000) | +0.0043 (0.199) | 0.15 | -0.0247 [-0.0334, -0.0163], 0.0002 | yes |
| late (10–14) | -0.0167 [-0.0296, -0.0040] | 0.0248 | 10 | 0.0809 | -0.0089 (0.139) | +0.0079 (0.054) | 0.47 | -0.0162 [-0.0268, -0.0041], 0.0208 | yes |
| trend (a): placebo line | -0.0238 [-0.0346, -0.0139] | 0.0009 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0255 [-0.0352, -0.0160] | 0.0005 | 13 | – | – | – | – | – | – |

**autocorr_deconv ts_demean W60** — pre-injection level (windows 1–4) DMT 0.7713, PCB 0.7643

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.0264 [-0.0380, -0.0153] | 0.0009 | 12 | 0.0160 | -0.0180 (0.026) | +0.0083 (0.076) | 0.32 | -0.0237 [-0.0333, -0.0132], 0.0017 | yes |
| sensitivity (5–14) | -0.0230 [-0.0345, -0.0114] | 0.0023 | 12 | 0.0370 | -0.0175 (0.026) | +0.0055 (0.226) | 0.24 | -0.0203 [-0.0299, -0.0099], 0.0037 | yes |
| early (6–9) | -0.0280 [-0.0388, -0.0178] | 0.0002 | 13 | 0.0310 | -0.0249 (0.004) | +0.0031 (0.462) | 0.11 | -0.0255 [-0.0345, -0.0174], 0.0002 | yes |
| late (10–14) | -0.0250 [-0.0399, -0.0106] | 0.0060 | 11 | 0.0410 | -0.0125 (0.138) | +0.0125 (0.023) | 0.50 | -0.0223 [-0.0365, -0.0072], 0.0149 | yes |
| trend (a): placebo line | -0.0295 [-0.0428, -0.0170] | 0.0009 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0290 [-0.0420, -0.0165] | 0.0011 | 13 | – | – | – | – | – | – |

**PhiR_deconv ts_gsr W60** — pre-injection level (windows 1–4) DMT 0.1193, PCB 0.1317

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | +0.0178 [+0.0069, +0.0293] | 0.0099 | 3 | 0.0010 | +0.0064 (0.027) | -0.0113 (0.027) | 0.64 | +0.0158 [+0.0071, +0.0248], 0.0057 | yes |
| sensitivity (5–14) | +0.0179 [+0.0073, +0.0293] | 0.0077 | 3 | 0.0010 | +0.0077 (0.012) | -0.0103 (0.039) | 0.57 | +0.0158 [+0.0075, +0.0240], 0.0042 | yes |
| early (6–9) | +0.0229 [+0.0087, +0.0382] | 0.0109 | 3 | 0.0010 | +0.0104 (0.013) | -0.0125 (0.042) | 0.55 | +0.0185 [+0.0072, +0.0311], 0.0123 | yes |
| late (10–14) | +0.0136 [+0.0038, +0.0236] | 0.0159 | 3 | 0.0190 | +0.0033 (0.176) | -0.0104 (0.030) | 0.76 | +0.0137 [+0.0056, +0.0208], 0.0084 | yes |
| trend (a): placebo line | +0.0150 [+0.0055, +0.0252] | 0.0109 | 2 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0156 [+0.0064, +0.0255] | 0.0079 | 2 | – | – | – | – | – | – |

**PhiR_deconv ts_demean W60** — pre-injection level (windows 1–4) DMT 0.1494, PCB 0.1629

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | +0.0350 [+0.0188, +0.0523] | 0.0009 | 1 | 0.0020 | +0.0189 (0.045) | -0.0161 (0.022) | 0.46 | +0.0304 [+0.0154, +0.0465], 0.0018 | yes |
| sensitivity (5–14) | +0.0321 [+0.0168, +0.0490] | 0.0013 | 1 | 0.0020 | +0.0178 (0.044) | -0.0144 (0.035) | 0.45 | +0.0274 [+0.0136, +0.0432], 0.0020 | yes |
| early (6–9) | +0.0333 [+0.0147, +0.0520] | 0.0052 | 2 | 0.0130 | +0.0216 (0.025) | -0.0117 (0.106) | 0.35 | +0.0288 [+0.0131, +0.0458], 0.0043 | yes |
| late (10–14) | +0.0364 [+0.0174, +0.0597] | 0.0009 | 1 | 0.0040 | +0.0168 (0.136) | -0.0196 (0.008) | 0.54 | +0.0317 [+0.0129, +0.0543], 0.0037 | yes |
| trend (a): placebo line | +0.0340 [+0.0181, +0.0516] | 0.0013 | 2 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0316 [+0.0150, +0.0479] | 0.0038 | 3 | – | – | – | – | – | – |

**PhiR_deconv ts_gsr global-bins** — pre-injection level (bins 1–8) DMT 0.0230, PCB 0.0240

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.0032 [-0.0100, +0.0046] | 0.4105 | 10 | 0.2328 | -0.0054 (0.030) | -0.0022 (0.397) | -0.69 | -0.0032 [-0.0088, +0.0031], 0.3229 | no |
| sensitivity (10–28) | -0.0033 [-0.0100, +0.0040] | 0.3783 | 10 | 0.2048 | -0.0055 (0.023) | -0.0022 (0.391) | -0.66 | -0.0033 [-0.0088, +0.0027], 0.2864 | no |
| early (11–18) | -0.0034 [-0.0113, +0.0050] | 0.4420 | 9 | 0.2897 | -0.0065 (0.044) | -0.0032 (0.219) | -0.94 | -0.0037 [-0.0107, +0.0039], 0.3470 | no |
| late (19–28) | -0.0031 [-0.0104, +0.0048] | 0.4436 | 8 | 0.2957 | -0.0046 (0.029) | -0.0015 (0.627) | -0.47 | -0.0028 [-0.0087, +0.0032], 0.3837 | no |
| trend (a): placebo line | -0.0049 [-0.0119, +0.0025] | 0.2124 | 10 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0056 [-0.0124, +0.0017] | 0.1526 | 10 | – | – | – | – | – | – |

**PhiR_deconv ts_demean global-bins** — pre-injection level (bins 1–8) DMT 0.0463, PCB 0.0513

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | +0.0209 [+0.0007, +0.0423] | 0.0933 | 3 | 0.0370 | +0.0147 (0.168) | -0.0062 (0.289) | 0.29 | +0.0199 [+0.0017, +0.0406], 0.0780 | yes |
| sensitivity (10–28) | +0.0206 [+0.0007, +0.0418] | 0.0922 | 3 | 0.0390 | +0.0139 (0.182) | -0.0067 (0.245) | 0.33 | +0.0192 [+0.0011, +0.0395], 0.0829 | yes |
| early (11–18) | +0.0167 [-0.0035, +0.0401] | 0.1998 | 5 | 0.1688 | +0.0141 (0.242) | -0.0026 (0.653) | 0.16 | +0.0142 [-0.0024, +0.0326], 0.1506 | no |
| late (19–28) | +0.0242 [+0.0013, +0.0507] | 0.0831 | 4 | 0.0290 | +0.0152 (0.200) | -0.0090 (0.158) | 0.37 | +0.0244 [+0.0023, +0.0503], 0.0812 | yes |
| trend (a): placebo line | +0.0193 [+0.0016, +0.0389] | 0.0828 | 4 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0173 [-0.0019, +0.0369] | 0.1221 | 4 | – | – | – | – | – | – |

Raw vs deconvolved, primary set, side by side:

| series | raw | deconvolved |
|---|---|---|
| sts ts_gsr W60 | -0.0809 [-0.1261, -0.0377], p = 0.0038, phase p = 0.0020, 13/14, FD-resid survives | -0.0782 [-0.1182, -0.0424], p = 0.0013, phase p = 0.0010, 13/14, FD-resid survives |
| sts ts_demean W60 | -0.1031 [-0.1558, -0.0522], p = 0.0026, phase p = 0.0010, 12/14, FD-resid survives | -0.1003 [-0.1459, -0.0591], p = 0.0004, phase p = 0.0010, 13/14, FD-resid survives |
| sts ts_gsr global-bins | -0.0801 [-0.1310, -0.0315], p = 0.0071, phase p = 0.0010, 12/14, FD-resid survives | -0.0772 [-0.1230, -0.0382], p = 0.0018, phase p = 0.0010, 13/14, FD-resid survives |
| sts ts_demean global-bins | -0.1035 [-0.1687, -0.0365], p = 0.0132, phase p = 0.0010, 11/14, FD-resid survives | -0.1135 [-0.1712, -0.0586], p = 0.0020, phase p = 0.0010, 13/14, FD-resid survives |
| autocorr ts_gsr W60 | -0.0146 [-0.0251, -0.0052], p = 0.0106, phase p = 0.0729, 12/14, FD-resid survives | -0.0220 [-0.0327, -0.0116], p = 0.0021, phase p = 0.0160, 12/14, FD-resid survives |
| autocorr ts_demean W60 | -0.0216 [-0.0319, -0.0116], p = 0.0017, phase p = 0.0390, 13/14, FD-resid survives | -0.0264 [-0.0380, -0.0153], p = 0.0009, phase p = 0.0160, 12/14, FD-resid survives |
| PhiR ts_gsr W60 | +0.0007 [-0.0078, +0.0100], p = 0.8971, phase p = 0.8372, 8/14, FD-resid does not survive | +0.0178 [+0.0069, +0.0293], p = 0.0099, phase p = 0.0010, 3/14, FD-resid survives |
| PhiR ts_demean W60 | +0.0157 [+0.0010, +0.0326], p = 0.0853, phase p = 0.0380, 4/14, FD-resid survives | +0.0350 [+0.0188, +0.0523], p = 0.0009, phase p = 0.0020, 1/14, FD-resid survives |
| PhiR ts_gsr global-bins | -0.0062 [-0.0127, +0.0003], p = 0.0953, phase p = 0.0230, 9/14, FD-resid survives | -0.0032 [-0.0100, +0.0046], p = 0.4105, phase p = 0.2328, 10/14, FD-resid does not survive |
| PhiR ts_demean global-bins | +0.0180 [-0.0002, +0.0380], p = 0.1177, phase p = 0.0190, 5/14, FD-resid survives | +0.0209 [+0.0007, +0.0423], p = 0.0933, phase p = 0.0370, 3/14, FD-resid survives |

What it shows. Deconvolution removes about 30 % of the sts level (1.309 → 0.924 global, 1.155 → 0.832 at W = 60) and takes r₁ from 0.866 to 0.790. The sts contrast is unchanged: W = 60 ts_gsr −0.0782 [−0.1182, −0.0424], p = 0.0013, phase p = 0.0010, 13/14, survives FD residualisation, placebo share 0.32 (raw −0.0809, p = 0.0038, share 0.40); ts_demean −0.1003 [−0.1459, −0.0591], p = 0.0004 (raw −0.1031, p = 0.0026); global fit −0.0772 (raw −0.0801) and −0.1135 (raw −0.1035); early/late and both trend corrections as before (late set p = 0.0096 / 0.0020, raw 0.034 / 0.013). The autocorrelation contrast is larger and passes the temporal null on both variants: −0.0220, p = 0.0021, phase p = 0.016 (raw −0.0146, p = 0.011, phase p = 0.073); ts_demean −0.0264, p = 0.0009, phase p = 0.016 (raw −0.0216, p = 0.0017, phase p = 0.039). ΦR changes: at W = 60 the deconvolved ΦR DiD is positive and passes both nulls on both variants — ts_gsr +0.0178 [+0.0069, +0.0293], p = 0.0099, phase p = 0.0010, 3/14 negative, survives (raw +0.0007, p = 0.90); ts_demean +0.0350 [+0.0188, +0.0523], p = 0.0009, phase p = 0.0020, 1/14 negative (raw +0.0157, p = 0.085) — made of a placebo-run fall (ts_gsr −0.0113, p = 0.027; placebo share 0.64) and a DMT-run rise (+0.0064, p = 0.027); at the global fit the deconvolved ΦR is −0.0032, p = 0.41 (ts_gsr) and +0.0209, p = 0.093 (ts_demean), so the two estimators disagree on ΦR for ts_gsr after deconvolution as they did before it (raw +0.0007 at W = 60, −0.0062 global). The W = 60 ΦR level is 0.119 nats deconvolved (0.096 raw) against 0.023 (0.026 raw) at the global fit; by the formula, the +0.096 excess of the windowed over the global level (deconvolved, ts_gsr, DMT pre-injection) is +0.105 from the larger windowed TDMI (1.144 vs 1.040) and +0.084 from the smaller windowed xtx + yty (0.884 vs 0.968), against −0.083 from the larger windowed cross atoms rtx/rty/xtr/ytr (0.029 vs 0.008 each) and −0.009 from rtr (0.026 vs 0.016). Most of the W = 60 ΦR level is therefore estimator-dependent. The four-atom MMI structure (sts ≈ xtx + yty, mirror atoms ≈ −sts/2) is unchanged by deconvolution. Two limits of the procedure: the HRF is estimated per run from all 840 TRs, so a change of HRF shape that occurs within the DMT run after injection is not removed by it (the run-level HRFs of the two runs are indistinguishable); and the deconvolved series remain band-limited to 0.01–0.08 Hz, which by itself imposes r₁ ≈ 0.82 on white noise.

## 4. Windows 6–9 vs 10–14, and the per-subject linear trend corrections

Early/late sets and the two trend corrections for sts on every estimator and variant (the same rows for the autocorrelation and ΦR are in their tables above):

**sts ts_gsr W60** — pre-injection level (windows 1–4) DMT 1.1554, PCB 1.1378

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.0809 [-0.1261, -0.0377] | 0.0038 | 13 | 0.0020 | -0.0485 (0.027) | +0.0324 (0.042) | 0.40 | -0.0649 [-0.0966, -0.0289], 0.0048 | yes |
| sensitivity (5–14) | -0.0733 [-0.1180, -0.0291] | 0.0070 | 12 | 0.0020 | -0.0491 (0.023) | +0.0242 (0.104) | 0.33 | -0.0555 [-0.0864, -0.0210], 0.0100 | yes |
| early (6–9) | -0.1029 [-0.1464, -0.0601] | 0.0009 | 13 | 0.0010 | -0.0842 (0.001) | +0.0187 (0.221) | 0.18 | -0.0806 [-0.1151, -0.0455], 0.0018 | yes |
| late (10–14) | -0.0633 [-0.1147, -0.0118] | 0.0337 | 10 | 0.0060 | -0.0199 (0.388) | +0.0434 (0.014) | 0.69 | -0.0523 [-0.0909, -0.0078], 0.0345 | yes |
| trend (a): placebo line | -0.0890 [-0.1347, -0.0461] | 0.0021 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0995 [-0.1424, -0.0599] | 0.0007 | 13 | – | – | – | – | – | – |

**sts ts_demean W60** — pre-injection level (windows 1–4) DMT 1.1004, PCB 1.0819

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 6–14) | -0.1031 [-0.1558, -0.0522] | 0.0026 | 12 | 0.0010 | -0.0633 (0.033) | +0.0398 (0.031) | 0.39 | -0.0824 [-0.1224, -0.0372], 0.0048 | yes |
| sensitivity (5–14) | -0.0935 [-0.1431, -0.0426] | 0.0039 | 12 | 0.0010 | -0.0621 (0.030) | +0.0314 (0.064) | 0.34 | -0.0714 [-0.1106, -0.0298], 0.0073 | yes |
| early (6–9) | -0.1183 [-0.1673, -0.0679] | 0.0012 | 13 | 0.0010 | -0.0975 (0.003) | +0.0208 (0.177) | 0.18 | -0.0953 [-0.1394, -0.0518], 0.0020 | yes |
| late (10–14) | -0.0910 [-0.1522, -0.0319] | 0.0128 | 11 | 0.0030 | -0.0360 (0.245) | +0.0550 (0.012) | 0.60 | -0.0721 [-0.1229, -0.0177], 0.0233 | yes |
| trend (a): placebo line | -0.1126 [-0.1690, -0.0595] | 0.0018 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.1193 [-0.1736, -0.0683] | 0.0012 | 13 | – | – | – | – | – | – |

**sts ts_gsr W30** — pre-injection level (windows 1–8) DMT 1.0223, PCB 1.0063

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 11–28) | -0.0686 [-0.1084, -0.0293] | 0.0042 | 13 | 0.0010 | -0.0390 (0.035) | +0.0296 (0.027) | 0.43 | -0.0545 [-0.0836, -0.0215], 0.0065 | yes |
| sensitivity (10–28) | -0.0658 [-0.1072, -0.0261] | 0.0067 | 12 | 0.0010 | -0.0407 (0.031) | +0.0252 (0.049) | 0.38 | -0.0514 [-0.0799, -0.0179], 0.0109 | yes |
| early (11–18) | -0.0839 [-0.1267, -0.0451] | 0.0012 | 13 | 0.0010 | -0.0686 (0.002) | +0.0154 (0.236) | 0.18 | -0.0678 [-0.0978, -0.0364], 0.0020 | yes |
| late (19–28) | -0.0564 [-0.1024, -0.0118] | 0.0321 | 11 | 0.0080 | -0.0154 (0.444) | +0.0410 (0.005) | 0.73 | -0.0439 [-0.0783, -0.0035], 0.0474 | yes |
| trend (a): placebo line | -0.0766 [-0.1147, -0.0386] | 0.0021 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0849 [-0.1225, -0.0495] | 0.0010 | 13 | – | – | – | – | – | – |

**sts ts_gsr global-bins** — pre-injection level (bins 1–8) DMT 1.3085, PCB 1.2893

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.0801 [-0.1310, -0.0315] | 0.0071 | 12 | 0.0010 | -0.0521 (0.045) | +0.0280 (0.047) | 0.35 | -0.0637 [-0.1023, -0.0182], 0.0161 | yes |
| sensitivity (10–28) | -0.0773 [-0.1280, -0.0278] | 0.0085 | 12 | 0.0010 | -0.0538 (0.037) | +0.0235 (0.083) | 0.30 | -0.0605 [-0.0967, -0.0150], 0.0183 | yes |
| early (11–18) | -0.1063 [-0.1545, -0.0612] | 0.0009 | 13 | 0.0010 | -0.0873 (0.002) | +0.0190 (0.157) | 0.18 | -0.0847 [-0.1209, -0.0450], 0.0024 | yes |
| late (19–28) | -0.0591 [-0.1194, +0.0019] | 0.0773 | 10 | 0.0320 | -0.0240 (0.399) | +0.0351 (0.032) | 0.59 | -0.0469 [-0.0952, +0.0090], 0.1147 | no |
| trend (a): placebo line | -0.0830 [-0.1354, -0.0322] | 0.0070 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.0981 [-0.1481, -0.0508] | 0.0020 | 13 | – | – | – | – | – | – |

**sts ts_demean global-bins** — pre-injection level (bins 1–8) DMT 1.2403, PCB 1.2235

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (bins 11–28) | -0.1035 [-0.1687, -0.0365] | 0.0132 | 11 | 0.0010 | -0.0684 (0.064) | +0.0351 (0.054) | 0.34 | -0.0854 [-0.1468, -0.0178], 0.0281 | yes |
| sensitivity (10–28) | -0.0999 [-0.1641, -0.0338] | 0.0139 | 11 | 0.0010 | -0.0684 (0.061) | +0.0315 (0.078) | 0.32 | -0.0815 [-0.1413, -0.0131], 0.0311 | yes |
| early (11–18) | -0.1250 [-0.1846, -0.0620] | 0.0034 | 12 | 0.0030 | -0.1080 (0.008) | +0.0171 (0.294) | 0.14 | -0.1056 [-0.1641, -0.0461], 0.0070 | yes |
| late (19–28) | -0.0862 [-0.1640, -0.0078] | 0.0594 | 10 | 0.0080 | -0.0367 (0.348) | +0.0495 (0.025) | 0.57 | -0.0692 [-0.1407, +0.0045], 0.1088 | no |
| trend (a): placebo line | -0.1089 [-0.1758, -0.0424] | 0.0093 | 13 | – | – | – | – | – | – |
| trend (b): shared slope | -0.1239 [-0.1908, -0.0548] | 0.0057 | 13 | – | – | – | – | – | – |

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
