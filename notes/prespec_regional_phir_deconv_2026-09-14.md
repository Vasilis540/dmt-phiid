# Pre-specification: regional structure of the deconvolved ΦR increase (recorded 14 Sep 2026, 11:37 UTC / 14:37 Athens, before any regional ΦR number was computed)

Status: EXPLORATORY. ΦR (rather than sts), HRF deconvolution and the W = 60 estimator were each chosen after seeing results — ΦR because the review found it flat on the raw data, deconvolution as a review computation, W = 60 because the deconvolved ΦR increase appears on that estimator and not on the global fit. No confirmatory claim attaches to any outcome of what follows. Every part is reported regardless of outcome.

Context (already computed, `notes/review_computations_2026-09-14.md`, section 3): on the HRF-deconvolved series the whole-brain ΦR DiD at W = 60 is +0.0178 [+0.0069, +0.0293], sign-flip p = 0.0099, phase p = 0.0010, 3/14 negative (ts_gsr) and +0.0350, p = 0.0009 (ts_demean); the ts_gsr effect is 64 % a placebo-run fall (−0.0113, p = 0.027) and 36 % a DMT-run rise (+0.0064, p = 0.027). At the global fit the deconvolved ΦR DiD is −0.0032, p = 0.41 (ts_gsr) and +0.0209, p = 0.093 (ts_demean).

## Prediction (fixed now)

If the deconvolved ΦR increase under DMT reflects the same workspace structure Luppi et al. (eLife 2024) report for its collapse under propofol and disorders of consciousness, the per-region ΦR increase should be larger inside the Default/Control network proxy than outside it: the per-subject difference mean DiD(workspace proxy) − mean DiD(non-workspace cortex) should be positive, with the exact sign-flip p below 0.05 on the primary proxy. If the per-region increase is spatially uniform (workspace-minus-non-workspace difference indistinguishable from zero) or absent regionally (no region survives FDR and the proxy difference is null), the whole-brain ΦR increase does not connect to the workspace account.

What no outcome decides: whether ΦR is the right quantity for this dataset, whether the W = 60 ΦR level (0.12 nats, five times the global-fit level) is anything but estimator-dependent, and whether the placebo-run fall that carries most of the ts_gsr effect is drug-related.

## Analysis plan (fixed now; the machinery of `scripts/11_regional_analysis.py`, applied to ΦR on the deconvolved series)

1. Data: the rsHRF-deconvolved series of `notes/rev_deconv.py` (both variants, ts_gsr primary, ts_demean sensitivity), 115 regions (region 20 excluded), 6,555 pairs, non-finite TRs dropped as in `01`.
2. Estimators: (a) windowed W = 60 (refit per window, the estimator on which the whole-brain increase was found; primary for this check); (b) the global fit with 30-TR bins (the estimator `11` itself uses; secondary). Gaussian MMI ΦID, τ = 1, phyid's definitions, computed in closed form from each pair's 4 × 4 correlation matrix (time-mean of phyid's local atoms equals the plug-in log-determinant atoms exactly; the implementation is validated against the saved `atoms_win60_*` / `atoms_bins_*` whole-brain means and against `11`'s saved per-region sts/rtr before use, and the validation numbers are reported).
3. Per-region ΦR = mean over the 114 pairs containing the region of pair-wise ΦR = TDMI − I(X;X′) − I(Y;Y′) + rtr, per window (or bin), subject, condition. Internal check: mean over regions equals the whole-brain pair mean in `notes/review_results/deconv/`.
4. Per-region DiD = (post − pre)_DMT − (post − pre)_PCB per subject with the primary sets (W = 60: windows 6–14 vs 1–4; bins: 11–28 vs 1–8); group mean; exact two-sided sign-flip over 2¹⁴; Benjamini–Hochberg FDR q = 0.05 across 115 regions; counts of FDR-surviving regions by sign, cortical/subcortical.
5. Workspace comparison exactly as in `11`: primary proxy = Yeo Default (gateway proxy, 24 parcels) + Control (broadcaster proxy, 13); named-subregion proxy (21 + 5) as sensitivity; non-workspace = remaining cortical parcels (subcortex added as sensitivity). Per subject: mean DiD(workspace) − mean DiD(non-workspace); exact sign-flip p; 10,000-draw subject-bootstrap CI; the same for gateway and broadcaster sub-proxies and their difference. The prediction is tested on the primary proxy vs non-workspace cortex; the rest is reported.
6. Spatial correlation of the group-mean per-region DiD map with the 5-HT2A map (Spearman), spin test on the 99 cortical parcels with the Vasa rotations in `external/DMT_NCT/fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat` (10,000 rotations, both directions, two-sided p); the same against 5-HT1A, 5-HT1B, 5-HT4 and 5-HTT with BH across the five, as `11` does; 115-region ρ descriptive only.
7. For reference, the same per-region computation on the raw (non-deconvolved) series, both estimators, reported alongside without a prediction.

## Three whole-brain items requested at the same time (no prediction)

- The deconvolved ΦR contrast at W = 30, both variants, with the full inference of `notes/rev_inference.py` (sign-flip, bootstrap, phase-randomised null, FD residualisation, early/late, trend corrections); the W = 30 windowed fit is computed with the same validated closed form.
- The 14 per-subject ΦR DiDs (deconvolved W = 60, both variants; raw alongside), with the per-subject DMT and placebo changes that make them up.
- The placebo-run ΦR by window (deconvolved W = 60, group mean and SE for each of the 14 windows, both conditions), and the per-subject placebo change.

Nothing in this file or in the results file to follow is manuscript text.
