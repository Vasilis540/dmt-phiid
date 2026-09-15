# Regional structure of the deconvolved ΦR increase — results (14 Sep 2026)

EXPLORATORY. Prediction and analysis plan fixed before any number existed in `notes/prespec_regional_phir_deconv_2026-09-14.md` (written 11:37:29 UTC, sha256 30b7d4d2…; the first regional result was computed at 11:43:59 UTC, after the section-0 validation; the eight cells were re-run at 12:16–12:21 UTC to store p-values at full precision and the logs were copied into `logs/` afterwards, so the file times on disk no longer evidence that order — only the pre-specification file's own time does). ΦR, HRF deconvolution and the W = 60 estimator were each chosen after seeing results; no confirmatory claim attaches to any outcome below. Everything is reported regardless of outcome. Nothing here is manuscript text and nothing proposes a framing.

The prediction as recorded: if the deconvolved ΦR increase under DMT reflects the workspace structure Luppi et al. (2024) report for its collapse under propofol, the per-region ΦR increase should be larger inside the Default/Control network proxy than outside it (per-subject mean DiD inside − outside positive, exact sign-flip p < 0.05 on the primary proxy); if it is spatially uniform or absent regionally, the whole-brain ΦR increase does not connect to the workspace account.

Scripts (in `notes/`; all re-runnable from the repository root with `.venv/bin/python`):

| file | what it does |
|---|---|
| `rev_phiid_fast.py` | closed-form, batched Gaussian-MMI ΦID for all 6,555 pairs (window means, global-fit bin means of the local atoms, TR-local pair-mean series); the identities are in its docstring |
| `rev_phiid_fast_validate.py` | validation against the saved phyid outputs (section 0) |
| `rev_regional_phir.py` | the regional analysis with the machinery of `scripts/11_regional_analysis.py` (parcels, proxies, exact sign-flip, BH FDR, Vasa spin test) applied to per-region ΦR; one run per cell (series × variant × estimator) |
| `rev_phir_items.py` | the three whole-brain items (deconvolved ΦR at W = 30 with the inference engine of `rev_inference.py`; per-subject DiDs; ΦR by window) |
| `rev_regional_tables.py`, `rev_regional_note.py` | render every table below from the CSVs and fill them into this note; no number in a table was typed by hand |

Outputs: `notes/review_results/regional/` (per cell: `regional_atoms_<cell>.npy` (14, 2, n_t, 115, 16), `regional_phir_did_map_<cell>.csv`, `regional_phir_<cell>.csv`), `notes/review_results/inference_rows_w30.csv` (+ `.pkl`), the deconvolved W = 30 atom arrays in `notes/review_results/deconv/`, logs in `notes/review_results/logs/` (`regional_<cell>.log`, `rev_phir_items.log`, `phiid_fast_validate*.log`, `phir_baseline_and_slope.log`).

Conventions as in `notes/review_computations_2026-09-14.md`: DiD = (post − pre)_DMT − (post − pre)_PCB per subject; W = 60: pre = windows 1–4, post = 6–14; global fit: pre = bins 1–8, post = 11–28; W = 30: pre = windows 1–8, post = 11–28. Per-region ΦR = mean over the 114 pairs containing the region of pair-wise ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr (Gaussian MMI, τ = 1). Proxies exactly as in `11`: primary = Yeo Default (gateway proxy, 24 cortical parcels) + Control (broadcaster proxy, 13); named-subregion proxy (21 + 5) as sensitivity; non-workspace = the remaining 62 cortical parcels (subcortex, 16, added as sensitivity). Spin test: Vasa rotations of the 100 cortical parcels (10,000), region 20 NaN, two-sided p; BH across the five receptor maps. Units: nats.

## 0. Method validation (the closed form used for every number below)

`rev_phiid_fast.py` computes phyid's Gaussian-MMI atoms in closed form from each pair's 4 × 4 correlation matrix (the time-mean of phyid's local atoms equals the plug-in log-determinant atoms exactly, and the lattice solve is linear). Checked against the saved phyid outputs of `01` and `11` on the raw and the deconvolved data:

{{VALIDATION}}

The internal consistency check of every regional run (mean over regions of the per-region 16 atoms vs the saved whole-brain pair means of `01`) is at most 7.3e-15 across the eight cells (`logs/regional_consistency.log`).

## 1. The prediction, on the cell it was made for (deconvolved, ts_gsr, W = 60)

{{PREDICTION}}

Per-region: 3 of 115 regions survive BH FDR (q = 0.05; p threshold 0.00130), all three with a positive DiD — LH_SomMot_4 (+0.0305, p = 0.0007), RH_SomMot_4 (+0.0250, p = 0.0006), RH_Default_Temp_3 (+0.0364, p = 0.0001, positive in 14/14); 38 of 115 have uncorrected p < 0.05; the group-mean DiD is positive in 112 of 115 regions; its SD across regions is 0.0085 against a mean of 0.0178 (range −0.0058 to +0.0364). Network means (all positive): Vis +0.0221 (p = 0.008), DorsAttn +0.0208 (0.002), SalVentAttn +0.0206 (0.017), SomMot +0.0202 (0.020), Default +0.0190 (0.008), Subcortex +0.0129 (0.028), Limbic +0.0121 (0.027), Control +0.0094 (0.203). Spin test against 5-HT2A on the 99 cortical parcels: ρ = −0.139, two-sided p = 0.195 (Vasa one-sided-average p = 0.068); no receptor map reaches p < 0.05.

Outcome against the recorded rule. The predicted outcome (inside − outside positive, p < 0.05) is not observed: the difference is negative, −0.0047 [−0.0079, −0.0013], p = 0.023, positive in 4 of 14 subjects. The recorded alternative ("spatially uniform or absent regionally": a difference indistinguishable from zero, or no FDR region with a null difference) is not observed either: the difference is distinguishable from zero and three regions survive FDR. The outcome falls in neither recorded branch; it is a difference of the sign opposite to the predicted one. Its composition: −0.0047 is the 37-parcel mean of a Default difference of −0.0013 (24 parcels, p = 0.53) and a Control difference of −0.0109 (13 parcels, p = 0.004), so the Control (broadcaster) proxy accounts for 82 % of it; and it is present in the placebo run's change (inside − outside +0.0054 [+0.0020, +0.0090], p = 0.014), while the DMT run's is +0.0007 [−0.0012, +0.0026], p = 0.49. Regionally the increase is broad (group-mean DiD positive in 112/115; three FDR regions, two somatomotor and one temporal Default) and not significantly correlated with the 5-HT2A map (ρ = −0.139, p = 0.195).

## 2. All eight cells (deconvolved and raw; W = 60 and global fit; both variants)

{{CELLS}}

Network means of the per-region DiD, sign-flip p, and the number of FDR-surviving regions in the network:

{{NETWORKS}}

Spin tests (99 cortical parcels, 10,000 Vasa rotations, two-sided p; "sig" = survives BH across the five maps):

{{SPIN}}

Spread of the group-mean DiD map:

{{MAPSTATS}}

FDR-surviving regions in the two cells that have any:

{{FDR_GSR}}

{{FDR_DEMEAN}}

What the eight cells show. No cell has a positive proxy-minus-non-workspace difference at p < 0.05 (the two positive values, raw ts_demean W60 +0.0009 and raw ts_demean global +0.0024, have p = 0.71 and 0.46); the difference is negative at p < 0.05 in the deconvolved ts_gsr W60 cell only, and negative at p = 0.0625 in the deconvolved ts_demean W60 cell (−0.0077 [−0.0147, −0.0008], 5/14 positive). The broadcaster (Control) proxy has a smaller DiD than non-workspace cortex in all four ts_gsr cells (deconvolved W60 −0.0109, p = 0.004; deconvolved global −0.0061, p = 0.002; raw W60 −0.0069, p = 0.043; raw global −0.0044, p = 0.030) and in the deconvolved ts_demean W60 cell (−0.0122, p = 0.036), and not in the other three ts_demean cells (+0.0010, +0.0027, +0.0099; p = 0.83, 0.40, 0.074). The gateway (Default) proxy minus non-workspace cortex is between −0.0052 and +0.0008 in the eight cells, p ≥ 0.2657 in all of them. FDR-surviving regions exist only in the two deconvolved W = 60 cells (3 and 55, all positive); no region survives in any global-fit or raw cell. The deconvolved ts_demean W60 map — the one with 55 FDR regions, positive in 114/115 — correlates negatively with the 5-HT2A (ρ = −0.273, p = 0.02055), 5-HT1A (−0.476, p = 0.00030) and 5-HT4 (−0.499, p = 0.00035) maps, all three surviving BH across the five maps; its network means are Vis +0.045, SomMot +0.040, DorsAttn +0.040, SalVentAttn +0.038, Default +0.034, Control +0.027, Subcortex +0.024, Limbic +0.021. The deconvolved ts_gsr W60 map has the same signs against those three maps (ρ = −0.139, −0.069, −0.095) without reaching p < 0.05. In the global-fit and raw cells no region survives FDR and the primary-proxy difference does not reach p < 0.05 (every sub-proxy difference below p = 0.05 in those six cells, from the workspace sections of their `regional_phir_<cell>.csv`: deconvolved ts_gsr global — Control minus non-workspace cortex −0.0061, p = 0.002 (−0.0064, p = 0.005 with subcortex added), gateway minus broadcaster +0.0069, p = 0.009, named broadcaster (Cont_PFCl, 5 parcels) minus non-workspace −0.0074, p = 0.042 (−0.0076, p = 0.034 with subcortex), named gateway minus named broadcaster +0.0085, p = 0.026; raw ts_gsr W60 — Control −0.0069, p = 0.043, gateway minus broadcaster +0.0066, p = 0.047, named broadcaster −0.0073, p = 0.022 (−0.0069, p = 0.027 with subcortex), named gateway minus named broadcaster +0.0066, p = 0.031; raw ts_gsr global — Control −0.0044, p = 0.030 (−0.0048, p = 0.037 with subcortex); raw ts_demean global — gateway minus broadcaster −0.0115, p = 0.015, named gateway minus named broadcaster −0.0138, p = 0.025, and with subcortex added Control +0.0119, p = 0.040 and named broadcaster +0.0146, p = 0.047; none in deconvolved ts_demean global or raw ts_demean W60); their spin tests pass for some maps on ts_demean only — deconvolved ts_demean global: 5-HT1A −0.414 (p = 0.00380), 5-HT4 −0.387 (p = 0.00425), 5-HT1B +0.422 (p = 0.00085), all BH-significant; raw ts_demean W60 and global: 5-HT1B +0.314 (p = 0.00605) and +0.378 (p = 0.00415) — while the 5-HT2A map passes in the deconvolved ts_demean W60 cell only. On ts_gsr no map passes in any cell.

## 3. The three whole-brain items

### 3.1 The deconvolved ΦR contrast at W = 30 (full inference; the W = 30 atoms from the validated closed form)

{{TABLE: PhiR_deconv ts_gsr W30}}

{{TABLE: PhiR_deconv ts_demean W30}}

{{TABLE: PhiR ts_gsr W30}}

sts at W = 30 on the deconvolved series, for reference (rows in `inference_rows_w30.csv`): ts_gsr −0.0671 [−0.1012, −0.0352], p = 0.0013, phase p = 0.0010, 13/14 negative, survives FD residualisation; ts_demean −0.0791 [−0.1162, −0.0456], p = 0.0007. The raw ts_gsr W30 sts DiD is −0.0686 (`inference_rows_raw.csv`).

What it shows. At W = 30 the deconvolved ΦR DiD is positive on both variants and passes both nulls: ts_gsr +0.0307 [+0.0148, +0.0472], sign-flip p = 0.0023, phase p = 0.0010, 2/14 negative, survives FD residualisation (+0.0257 [+0.0121, +0.0392]); ts_demean +0.0509 [+0.0286, +0.0729], p = 0.0013, phase p = 0.0010, 1/14 negative. Both are larger than at W = 60 (+0.0178 / +0.0350), as is the level: the pre-injection whole-brain ΦR (DMT run, ts_gsr, deconvolved) is 0.235 at W = 30, 0.119 at W = 60 and 0.023 at the global fit. The placebo run's fall carries 56 % (ts_gsr; PCB −0.0172, p = 0.019, DMT +0.0135, p = 0.008) and 48 % (ts_demean) of the DiD, 75 % / 61 % in the late set. The raw ts_gsr W = 30 ΦR contrast is null (+0.0007, p = 0.92), as at W = 60.

### 3.2 The per-subject ΦR DiDs (W = 60, primary set)

DMT change (windows 6–14 minus 1–4 in the DMT run), placebo change, and their difference, per subject:

{{SUBJECTS}}

Per-subject agreement: deconvolved vs raw ΦR DiD r = +0.81 (ts_gsr; Spearman +0.84) and +0.88 (ts_demean; +0.94); deconvolved ΦR DiD vs deconvolved sts DiD r = −0.77 (ts_gsr; Spearman −0.68) and −0.71 (ts_demean; −0.80).

What it shows. On the deconvolved ts_gsr series the DiD is positive in 11 of 14 subjects (median +0.0129; mean +0.0178; without the subject of largest |DiD|, subject 8 at +0.0620, the mean is +0.0144); the DMT run rises in 11 of 14 (mean +0.0064) and the placebo run falls in 10 of 14 (mean −0.0113); both happen in 8 of 14 subjects, and the placebo change is the larger of the two in magnitude in 10 of 14. On ts_demean 13 of 14 are positive (median +0.0300). The same subjects order the raw DiDs (r = 0.81 and 0.88) although the raw ts_gsr DiD is null (6/14 positive, median −0.0041). The per-subject deconvolved ΦR DiDs and sts DiDs correlate at r = −0.77 / −0.71 (n = 14, no null test; both quantities are linear combinations of the same 16 atoms).

### 3.3 The placebo-run ΦR across windows (W = 60; group mean, SE over 14 subjects)

{{WINDOWS}}

Baseline and slope (per subject, exact sign-flip and 10,000-draw bootstrap CI; `phir_baseline_and_slope.log`). Not in the recorded plan: these four tests were added after looking at the window series above, and are descriptive.

| series | DMT pre − PCB pre (windows 1–4) | placebo-run linear slope per window (14 windows) | DMT-run slope | placebo window 4 − window 1 |
|---|---|---|---|---|
| deconvolved ts_gsr | −0.0124 [−0.0210, −0.0042], p = 0.014; DMT lower in 12/14 | −0.00115 [−0.00200, −0.00028], p = 0.025; negative in 10/14 | −0.00003, p = 0.90 | −0.0120 [−0.0234, −0.0007], p = 0.067 |
| deconvolved ts_demean | −0.0135 [−0.0266, −0.0009], p = 0.072; 9/14 | −0.00202 [−0.00321, −0.00074], p = 0.012; 11/14 | +0.00155, p = 0.17 | −0.0093 [−0.0475, +0.0298], p = 0.66 |
| raw ts_gsr | −0.0042 [−0.0114, +0.0025], p = 0.28; 8/14 | −0.00036 [−0.00117, +0.00050], p = 0.43; 8/14 | −0.00023, p = 0.12 | −0.0084 [−0.0168, −0.0015], p = 0.039 |
| raw ts_demean | −0.0040 [−0.0143, +0.0061], p = 0.47; 9/14 | −0.00063 [−0.00150, +0.00037], p = 0.22; 9/14 | +0.00114, p = 0.15 | −0.0019 [−0.0249, +0.0246], p = 0.89 |

What it shows. On the deconvolved ts_gsr series the placebo run's ΦR is highest in window 1 (0.1375) and declines through the run — 0.1338, 0.1300, 0.1256 over the pre-injection windows, 0.1308 at window 5, then 0.1156–0.1273 (mean 0.1192) over windows 6–9 and 0.1161–0.1269 (0.1214) over 10–14; a linear slope of −0.00115 per window (p = 0.025, negative in 10/14 subjects), with the pre-injection windows alone falling by 0.0120 (p = 0.067). The DMT run starts lower than the placebo run (pre-injection 0.1193 vs 0.1317, difference −0.0124, p = 0.014, lower in 12/14 subjects), rises to 0.1380 at window 5 (the injection window, excluded from every contrast), stays at 0.1297 over windows 6–9 and 0.1226 over 10–14, and has no linear trend (slope −0.00003). The two runs differ at baseline by 0.0124 (DMT lower), against a DiD of 0.0178; after injection the DMT run is above the placebo run by 0.0105 over windows 6–9 (0.1297 vs 0.1192) and by 0.0012 over windows 10–14 (0.1226 vs 0.1214). ts_demean: placebo highest at window 1 (0.1743), slope −0.00202 per window (p = 0.012, negative in 11/14); DMT pre − PCB pre −0.0135 (p = 0.072, DMT lower in 9/14). On the raw series the placebo decline and the baseline difference are both absent at p < 0.05 (slope −0.00036, p = 0.43; baseline −0.0042, p = 0.28, ts_gsr), and the window-1 placebo value (0.1042) is the highest of windows 1–13, with window 14 at 0.1072.
