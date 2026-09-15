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

| check | max abs difference |
|---|---|
| (1) W60 window means vs saved, ts_gsr | 8.22e-15 |
| (2) W30 window means vs saved, ts_gsr | 9.33e-15 |
| (3) global bin means vs saved, ts_gsr | 1.22e-14 |
| (4) 11's per-region global sts vs closed form, ts_gsr | 1.43e-14 |
| (4) 11's per-region global rtr vs closed form, ts_gsr | 1.22e-15 |
| (1) W60 window means vs saved, ts_demean | 7.99e-15 |
| (3) global bin means vs saved, ts_demean | 1.27e-14 |
| (4) 11's per-region global sts vs closed form, ts_demean | 2.04e-14 |
| (4) 11's per-region global rtr vs closed form, ts_demean | 9.99e-16 |
| (5) deconvolved W60 window means vs saved, ts_gsr | 5.11e-15 |
| (5) deconvolved global bin means vs saved, ts_gsr | 7.88e-15 |
| (5) deconvolved W60 window means vs saved, ts_demean | 5.33e-15 |
| (5) deconvolved global bin means vs saved, ts_demean | 7.11e-15 |
| (6) 200 random (subject, run, window, pair) draws vs phyid.calc_PhiID, all 16 atoms | 7.33e-15 |
| (7) TR-local pair-mean atom series vs saved atoms_win60_local / atoms_bins_local (4 runs × 3 windows + 4 global) | 1.01e-13 |

The internal consistency check of every regional run (mean over regions of the per-region 16 atoms vs the saved whole-brain pair means of `01`) is at most 7.3e-15 across the eight cells (`logs/regional_consistency.log`).

## 1. The prediction, on the cell it was made for (deconvolved, ts_gsr, W = 60)

**deconvolved ts_gsr W60** — per-subject mean ΦR DiD inside minus outside the proxy (positive = larger increase inside)

| comparison | difference [95 % CI], p | positive/14 | n inside / n outside |
|---|---|---|---|
| primary proxy (Default + Control) vs non-workspace cortex | -0.0047 [-0.0079, -0.0013], p = 0.0233 | 4 | 37 / 62 |
| gateway proxy (Default) vs non-workspace cortex | -0.0013 [-0.0051, +0.0027], p = 0.5317 | 7 | 24 |
| broadcaster proxy (Control) vs non-workspace cortex | -0.0109 [-0.0161, -0.0052], p = 0.0037 | 2 | 13 |
| gateway proxy minus broadcaster proxy | +0.0095 [+0.0028, +0.0158], p = 0.0176 | – | 24 / 13 |
| primary proxy vs non-workspace cortex + subcortex | -0.0032 [-0.0060, -0.0004], p = 0.0563 | 5 | 37 / 78 |
| named-subregion proxy vs non-workspace cortex | -0.0028 [-0.0074, +0.0016], p = 0.2582 | 6 | 26 / 73 |
| named gateway (21) vs non-workspace cortex | -0.0008 [-0.0055, +0.0039], p = 0.7618 | 6 | 21 |
| named broadcaster (Cont_PFCl, 5) vs non-workspace cortex | -0.0115 [-0.0187, -0.0045], p = 0.0101 | 3 | 5 |

Mean DiD inside the primary proxy +0.0156 [+0.0041, +0.0271], p = 0.0244; outside +0.0203 [+0.0091, +0.0328], p = 0.0035. Composition of the inside-minus-outside difference: DMT-run change +0.0007 [-0.0012, +0.0026], p = 0.4911; placebo-run change +0.0054 [+0.0020, +0.0090], p = 0.0138.

Per-region: 3 of 115 regions survive BH FDR (q = 0.05; p threshold 0.00130), all three with a positive DiD — LH_SomMot_4 (+0.0305, p = 0.0007), RH_SomMot_4 (+0.0250, p = 0.0006), RH_Default_Temp_3 (+0.0364, p = 0.0001, positive in 14/14); 38 of 115 have uncorrected p < 0.05; the group-mean DiD is positive in 112 of 115 regions; its SD across regions is 0.0085 against a mean of 0.0178 (range −0.0058 to +0.0364). Network means (all positive): Vis +0.0221 (p = 0.008), DorsAttn +0.0208 (0.002), SalVentAttn +0.0206 (0.017), SomMot +0.0202 (0.020), Default +0.0190 (0.008), Subcortex +0.0129 (0.028), Limbic +0.0121 (0.027), Control +0.0094 (0.203). Spin test against 5-HT2A on the 99 cortical parcels: ρ = −0.139, two-sided p = 0.195 (Vasa one-sided-average p = 0.068); no receptor map reaches p < 0.05.

Outcome against the recorded rule. The predicted outcome (inside − outside positive, p < 0.05) is not observed: the difference is negative, −0.0047 [−0.0079, −0.0013], p = 0.023, positive in 4 of 14 subjects. The recorded alternative ("spatially uniform or absent regionally": a difference indistinguishable from zero, or no FDR region with a null difference) is not observed either: the difference is distinguishable from zero and three regions survive FDR. The outcome falls in neither recorded branch; it is a difference of the sign opposite to the predicted one. Its composition: −0.0047 is the 37-parcel mean of a Default difference of −0.0013 (24 parcels, p = 0.53) and a Control difference of −0.0109 (13 parcels, p = 0.004), so the Control (broadcaster) proxy accounts for 82 % of it; and it is present in the placebo run's change (inside − outside +0.0054 [+0.0020, +0.0090], p = 0.014), while the DMT run's is +0.0007 [−0.0012, +0.0026], p = 0.49. Regionally the increase is broad (group-mean DiD positive in 112/115; three FDR regions, two somatomotor and one temporal Default) and not significantly correlated with the 5-HT2A map (ρ = −0.139, p = 0.195).

## 2. All eight cells (deconvolved and raw; W = 60 and global fit; both variants)

| cell | whole-brain ΦR DiD, p | FDR regions (q = 0.05) | uncorrected p < 0.05 | group-mean DiD > 0 | primary proxy − non-workspace cortex [CI], p (pos/14) | gateway − non | broadcaster − non | named proxy − non | 5-HT2A ρ (spin p) |
|---|---|---|---|---|---|---|---|---|---|
| deconvolved ts_gsr W60 | +0.0178, 0.0099 | 3 (3 +, 0 −) | 38 | 112/115 | -0.0047 [-0.0079, -0.0013], 0.0233 (4) | -0.0013, 0.532 | -0.0109, 0.004 | -0.0028, 0.258 | -0.139 (0.19515) |
| deconvolved ts_demean W60 | +0.0350, 0.0009 | 55 (55 +, 0 −) | 72 | 114/115 | -0.0077 [-0.0147, -0.0008], 0.0625 (5) | -0.0052, 0.266 | -0.0122, 0.036 | -0.0029, 0.463 | -0.273 (0.02055) |
| deconvolved ts_gsr global | -0.0032, 0.4105 | 0 (0 +, 0 −) | 5 | 33/115 | -0.0017 [-0.0036, +0.0003], 0.1390 (6) | +0.0008, 0.594 | -0.0061, 0.002 | -0.0005, 0.731 | -0.040 (0.73855) |
| deconvolved ts_demean global | +0.0209, 0.0933 | 0 (0 +, 0 −) | 21 | 111/115 | -0.0019 [-0.0078, +0.0044], 0.5653 (6) | -0.0034, 0.374 | +0.0010, 0.829 | -0.0003, 0.941 | -0.087 (0.50880) |
| raw ts_gsr W60 | +0.0007, 0.8971 | 0 (0 +, 0 −) | 3 | 63/115 | -0.0026 [-0.0061, +0.0007], 0.1696 (5) | -0.0003, 0.871 | -0.0069, 0.043 | -0.0020, 0.316 | -0.193 (0.10460) |
| raw ts_demean W60 | +0.0157, 0.0853 | 0 (0 +, 0 −) | 12 | 110/115 | +0.0009 [-0.0035, +0.0054], 0.7094 (5) | -0.0001, 0.970 | +0.0027, 0.403 | +0.0008, 0.758 | +0.011 (0.92135) |
| raw ts_gsr global | -0.0062, 0.0953 | 0 (0 +, 0 −) | 18 | 10/115 | -0.0011 [-0.0030, +0.0009], 0.3209 (5) | +0.0008, 0.624 | -0.0044, 0.030 | -0.0002, 0.886 | -0.121 (0.37480) |
| raw ts_demean global | +0.0180, 0.1177 | 0 (0 +, 0 −) | 22 | 108/115 | +0.0024 [-0.0033, +0.0087], 0.4630 (6) | -0.0016, 0.569 | +0.0099, 0.074 | +0.0016, 0.617 | +0.031 (0.81820) |

Network means of the per-region DiD, sign-flip p, and the number of FDR-surviving regions in the network:

| cell | Vis | SomMot | DorsAttn | SalVentAttn | Limbic | Cont | Default | Subcortex |
|---|---|---|---|---|---|---|---|---|
| deconvolved ts_gsr W60 | +0.0221 (0.008; 0) | +0.0202 (0.020; 2) | +0.0208 (0.002; 0) | +0.0206 (0.017; 0) | +0.0121 (0.027; 0) | +0.0094 (0.203; 0) | +0.0190 (0.008; 1) | +0.0129 (0.028; 0) |
| deconvolved ts_demean W60 | +0.0449 (0.000; 15) | +0.0404 (0.005; 9) | +0.0403 (0.002; 7) | +0.0382 (0.001; 9) | +0.0209 (0.007; 0) | +0.0274 (0.034; 0) | +0.0344 (0.002; 13) | +0.0242 (0.005; 2) |
| deconvolved ts_gsr global | -0.0050 (0.352; 0) | -0.0025 (0.641; 0) | -0.0032 (0.388; 0) | -0.0006 (0.908; 0) | -0.0008 (0.855; 0) | -0.0090 (0.102; 0) | -0.0021 (0.584; 0) | -0.0018 (0.542; 0) |
| deconvolved ts_demean global | +0.0277 (0.055; 0) | +0.0196 (0.157; 0) | +0.0233 (0.062; 0) | +0.0265 (0.046; 0) | +0.0075 (0.448; 0) | +0.0240 (0.130; 0) | +0.0196 (0.137; 0) | +0.0120 (0.173; 0) |
| raw ts_gsr W60 | -0.0002 (0.975; 0) | +0.0017 (0.818; 0) | +0.0041 (0.397; 0) | +0.0021 (0.707; 0) | +0.0028 (0.474; 0) | -0.0051 (0.419; 0) | +0.0016 (0.769; 0) | -0.0008 (0.861; 0) |
| raw ts_demean W60 | +0.0171 (0.125; 0) | +0.0120 (0.253; 0) | +0.0180 (0.080; 0) | +0.0191 (0.059; 0) | +0.0124 (0.054; 0) | +0.0189 (0.101; 0) | +0.0160 (0.091; 0) | +0.0110 (0.136; 0) |
| raw ts_gsr global | -0.0094 (0.113; 0) | -0.0049 (0.396; 0) | -0.0052 (0.063; 0) | -0.0062 (0.080; 0) | -0.0013 (0.578; 0) | -0.0106 (0.055; 0) | -0.0054 (0.117; 0) | -0.0042 (0.134; 0) |
| raw ts_demean global | +0.0209 (0.118; 0) | +0.0155 (0.224; 0) | +0.0195 (0.090; 0) | +0.0215 (0.074; 0) | +0.0103 (0.188; 0) | +0.0285 (0.040; 0) | +0.0170 (0.175; 0) | +0.0086 (0.236; 0) |

Spin tests (99 cortical parcels, 10,000 Vasa rotations, two-sided p; "sig" = survives BH across the five maps):

| cell | 5HT2A ρ (two-sided spin p; BH) | 5HT1A ρ (two-sided spin p; BH) | 5HT1B ρ (two-sided spin p; BH) | 5HT4 ρ (two-sided spin p; BH) | 5HTT ρ (two-sided spin p; BH) | 115-region ρ with 5-HT2A (no null) |
|---|---|---|---|---|---|---|
| deconvolved ts_gsr W60 | -0.139 (0.19515; ns) | -0.069 (0.64160; ns) | -0.007 (0.94865; ns) | -0.095 (0.42280; ns) | +0.131 (0.27925; ns) | +0.047 |
| deconvolved ts_demean W60 | -0.273 (0.02055; sig) | -0.476 (0.00030; sig) | +0.241 (0.04195; ns) | -0.499 (0.00035; sig) | +0.063 (0.64100; ns) | -0.014 |
| deconvolved ts_gsr global | -0.040 (0.73855; ns) | +0.203 (0.03350; ns) | -0.057 (0.64220; ns) | +0.060 (0.59740; ns) | +0.103 (0.31760; ns) | -0.082 |
| deconvolved ts_demean global | -0.087 (0.50880; ns) | -0.414 (0.00380; sig) | +0.422 (0.00085; sig) | -0.387 (0.00425; sig) | -0.109 (0.48180; ns) | +0.125 |
| raw ts_gsr W60 | -0.193 (0.10460; ns) | +0.173 (0.06115; ns) | -0.132 (0.27215; ns) | -0.020 (0.86205; ns) | +0.076 (0.47125; ns) | -0.077 |
| raw ts_demean W60 | +0.011 (0.92135; ns) | -0.163 (0.30430; ns) | +0.314 (0.00605; sig) | -0.189 (0.12820; ns) | -0.089 (0.49360; ns) | +0.121 |
| raw ts_gsr global | -0.121 (0.37480; ns) | +0.180 (0.17980; ns) | -0.141 (0.32180; ns) | +0.016 (0.90530; ns) | +0.028 (0.81900; ns) | -0.198 |
| raw ts_demean global | +0.031 (0.81820; ns) | -0.274 (0.14915; ns) | +0.378 (0.00415; sig) | -0.247 (0.10565; ns) | -0.129 (0.45855; ns) | +0.211 |

Spread of the group-mean DiD map:

| cell | SD of group-mean DiD across regions | range (min, max) | region with smallest p |
|---|---|---|---|
| deconvolved ts_gsr W60 | 0.0085 | 0.0422 (min -0.0058 max +0.0364) | region RH_Default_Temp_3 did=+0.0364 (p = 0.0001) |
| deconvolved ts_demean W60 | 0.0129 | 0.0715 (min -0.0063 max +0.0652) | region LH_Vis_4 did=+0.0482 (p = 0.0001) |
| deconvolved ts_gsr global | 0.0053 | 0.0296 (min -0.0190 max +0.0107) | region RH_Cont_PFCl_4 did=-0.0190 (p = 0.0125) |
| deconvolved ts_demean global | 0.0110 | 0.0530 (min -0.0055 max +0.0475) | region RH_Default_PFCv_2 did=+0.0475 (p = 0.0005) |
| raw ts_gsr W60 | 0.0057 | 0.0258 (min -0.0106 max +0.0152) | region LH_DorsAttn_PrCv_1 did=+0.0082 (p = 0.0165) |
| raw ts_demean W60 | 0.0088 | 0.0420 (min -0.0079 max +0.0340) | region LH_DorsAttn_Post_2 did=+0.0286 (p = 0.0101) |
| raw ts_gsr global | 0.0048 | 0.0275 (min -0.0222 max +0.0053) | region LH_Default_Par_1 did=-0.0074 (p = 0.0005) |
| raw ts_demean global | 0.0104 | 0.0459 (min -0.0058 max +0.0401) | region RH_Default_PFCv_2 did=+0.0401 (p = 0.0021) |

FDR-surviving regions in the two cells that have any:

**deconvolved ts_gsr W60** — regions surviving BH FDR q = 0.05 (3), by network

| network | regions (DiD, sign-flip p) |
|---|---|
| SomMot (2) | LH_SomMot_4 (+0.0305, 0.0007); RH_SomMot_4 (+0.0250, 0.0006) |
| Default (1) | RH_Default_Temp_3 (+0.0364, 0.0001) |

**deconvolved ts_demean W60** — regions surviving BH FDR q = 0.05 (55), by network

| network | regions (DiD, sign-flip p) |
|---|---|
| Vis (15) | LH_Vis_1 (+0.0287, 0.0148); LH_Vis_3 (+0.0518, 0.0020); LH_Vis_4 (+0.0482, 0.0001); LH_Vis_5 (+0.0499, 0.0122); LH_Vis_6 (+0.0613, 0.0004); LH_Vis_8 (+0.0517, 0.0032); LH_Vis_9 (+0.0552, 0.0022); RH_Vis_1 (+0.0358, 0.0187); RH_Vis_2 (+0.0510, 0.0004); RH_Vis_3 (+0.0329, 0.0122); RH_Vis_4 (+0.0386, 0.0123); RH_Vis_5 (+0.0645, 0.0022); RH_Vis_6 (+0.0502, 0.0057); RH_Vis_7 (+0.0346, 0.0123); RH_Vis_8 (+0.0455, 0.0157) |
| SomMot (9) | LH_SomMot_1 (+0.0330, 0.0238); LH_SomMot_2 (+0.0409, 0.0011); LH_SomMot_5 (+0.0652, 0.0006); LH_SomMot_6 (+0.0570, 0.0134); RH_SomMot_3 (+0.0336, 0.0121); RH_SomMot_5 (+0.0348, 0.0217); RH_SomMot_6 (+0.0437, 0.0179); RH_SomMot_7 (+0.0509, 0.0043); RH_SomMot_8 (+0.0589, 0.0125) |
| DorsAttn (7) | LH_DorsAttn_Post_1 (+0.0332, 0.0232); LH_DorsAttn_Post_2 (+0.0549, 0.0002); LH_DorsAttn_Post_4 (+0.0614, 0.0016); LH_DorsAttn_PrCv_1 (+0.0415, 0.0149); LH_DorsAttn_FEF_1 (+0.0535, 0.0021); RH_DorsAttn_Post_5 (+0.0428, 0.0231); RH_DorsAttn_FEF_1 (+0.0387, 0.0059) |
| SalVentAttn (9) | LH_SalVentAttn_FrOperIns_2 (+0.0409, 0.0054); LH_SalVentAttn_PFCl_1 (+0.0409, 0.0166); LH_SalVentAttn_Med_1 (+0.0354, 0.0164); LH_SalVentAttn_Med_2 (+0.0365, 0.0127); LH_SalVentAttn_Med_3 (+0.0457, 0.0121); RH_SalVentAttn_TempOccPar_2 (+0.0339, 0.0120); RH_SalVentAttn_FrOperIns_1 (+0.0511, 0.0035); RH_SalVentAttn_Med_1 (+0.0379, 0.0022); RH_SalVentAttn_Med_2 (+0.0497, 0.0022) |
| Default (13) | LH_Default_Par_2 (+0.0327, 0.0074); LH_Default_PFC_2 (+0.0393, 0.0072); LH_Default_PFC_3 (+0.0356, 0.0070); LH_Default_PFC_4 (+0.0314, 0.0171); LH_Default_PFC_5 (+0.0443, 0.0043); LH_Default_PFC_6 (+0.0324, 0.0197); LH_Default_PFC_7 (+0.0498, 0.0042); LH_Default_pCunPCC_1 (+0.0442, 0.0040); LH_Default_pCunPCC_2 (+0.0422, 0.0125); RH_Default_Par_1 (+0.0397, 0.0044); RH_Default_Temp_1 (+0.0228, 0.0237); RH_Default_PFCv_2 (+0.0527, 0.0044); RH_Default_pCunPCC_2 (+0.0307, 0.0125) |
| Subcortex (2) | SUB_6 (+0.0285, 0.0148); SUB_13 (+0.0402, 0.0111) |

What the eight cells show. No cell has a positive proxy-minus-non-workspace difference at p < 0.05 (the two positive values, raw ts_demean W60 +0.0009 and raw ts_demean global +0.0024, have p = 0.71 and 0.46); the difference is negative at p < 0.05 in the deconvolved ts_gsr W60 cell only, and negative at p = 0.0625 in the deconvolved ts_demean W60 cell (−0.0077 [−0.0147, −0.0008], 5/14 positive). The broadcaster (Control) proxy has a smaller DiD than non-workspace cortex in all four ts_gsr cells (deconvolved W60 −0.0109, p = 0.004; deconvolved global −0.0061, p = 0.002; raw W60 −0.0069, p = 0.043; raw global −0.0044, p = 0.030) and in the deconvolved ts_demean W60 cell (−0.0122, p = 0.036), and not in the other three ts_demean cells (+0.0010, +0.0027, +0.0099; p = 0.83, 0.40, 0.074). The gateway (Default) proxy minus non-workspace cortex is between −0.0052 and +0.0008 in the eight cells, p ≥ 0.2657 in all of them. FDR-surviving regions exist only in the two deconvolved W = 60 cells (3 and 55, all positive); no region survives in any global-fit or raw cell. The deconvolved ts_demean W60 map — the one with 55 FDR regions, positive in 114/115 — correlates negatively with the 5-HT2A (ρ = −0.273, p = 0.02055), 5-HT1A (−0.476, p = 0.00030) and 5-HT4 (−0.499, p = 0.00035) maps, all three surviving BH across the five maps; its network means are Vis +0.045, SomMot +0.040, DorsAttn +0.040, SalVentAttn +0.038, Default +0.034, Control +0.027, Subcortex +0.024, Limbic +0.021. The deconvolved ts_gsr W60 map has the same signs against those three maps (ρ = −0.139, −0.069, −0.095) without reaching p < 0.05. In the global-fit and raw cells no region survives FDR and the primary-proxy difference does not reach p < 0.05 (every sub-proxy difference below p = 0.05 in those six cells, from the workspace sections of their `regional_phir_<cell>.csv`: deconvolved ts_gsr global — Control minus non-workspace cortex −0.0061, p = 0.002 (−0.0064, p = 0.005 with subcortex added), gateway minus broadcaster +0.0069, p = 0.009, named broadcaster (Cont_PFCl, 5 parcels) minus non-workspace −0.0074, p = 0.042 (−0.0076, p = 0.034 with subcortex), named gateway minus named broadcaster +0.0085, p = 0.026; raw ts_gsr W60 — Control −0.0069, p = 0.043, gateway minus broadcaster +0.0066, p = 0.047, named broadcaster −0.0073, p = 0.022 (−0.0069, p = 0.027 with subcortex), named gateway minus named broadcaster +0.0066, p = 0.031; raw ts_gsr global — Control −0.0044, p = 0.030 (−0.0048, p = 0.037 with subcortex); raw ts_demean global — gateway minus broadcaster −0.0115, p = 0.015, named gateway minus named broadcaster −0.0138, p = 0.025, and with subcortex added Control +0.0119, p = 0.040 and named broadcaster +0.0146, p = 0.047; none in deconvolved ts_demean global or raw ts_demean W60); their spin tests pass for some maps on ts_demean only — deconvolved ts_demean global: 5-HT1A −0.414 (p = 0.00380), 5-HT4 −0.387 (p = 0.00425), 5-HT1B +0.422 (p = 0.00085), all BH-significant; raw ts_demean W60 and global: 5-HT1B +0.314 (p = 0.00605) and +0.378 (p = 0.00415) — while the 5-HT2A map passes in the deconvolved ts_demean W60 cell only. On ts_gsr no map passes in any cell.

## 3. The three whole-brain items

### 3.1 The deconvolved ΦR contrast at W = 30 (full inference; the W = 30 atoms from the validated closed form)

**PhiR_deconv ts_gsr W30** — pre-injection level (windows 1–8) DMT 0.2352, PCB 0.2526

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 11–28) | +0.0307 [+0.0148, +0.0472] | 0.0023 | 2 | 0.0010 | +0.0135 (0.008) | -0.0172 (0.019) | 0.56 | +0.0257 [+0.0121, +0.0392], 0.0045 | yes |
| sensitivity (10–28) | +0.0309 [+0.0152, +0.0476] | 0.0024 | 2 | 0.0010 | +0.0147 (0.006) | -0.0162 (0.023) | 0.52 | +0.0259 [+0.0122, +0.0392], 0.0040 | yes |
| early (11–18) | +0.0380 [+0.0185, +0.0591] | 0.0023 | 1 | 0.0010 | +0.0227 (0.001) | -0.0153 (0.057) | 0.40 | +0.0306 [+0.0134, +0.0479], 0.0063 | yes |
| late (19–28) | +0.0248 [+0.0112, +0.0403] | 0.0042 | 2 | 0.0080 | +0.0061 (0.209) | -0.0187 (0.008) | 0.75 | +0.0218 [+0.0097, +0.0323], 0.0054 | yes |
| trend (a): placebo line | +0.0283 [+0.0150, +0.0426] | 0.0015 | 1 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0304 [+0.0174, +0.0439] | 0.0006 | 1 | – | – | – | – | – | – |

**PhiR_deconv ts_demean W30** — pre-injection level (windows 1–8) DMT 0.2684, PCB 0.2868

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 11–28) | +0.0509 [+0.0286, +0.0729] | 0.0013 | 1 | 0.0010 | +0.0266 (0.019) | -0.0243 (0.004) | 0.48 | +0.0440 [+0.0228, +0.0647], 0.0029 | yes |
| sensitivity (10–28) | +0.0508 [+0.0288, +0.0722] | 0.0015 | 2 | 0.0010 | +0.0268 (0.019) | -0.0240 (0.006) | 0.47 | +0.0440 [+0.0230, +0.0648], 0.0026 | yes |
| early (11–18) | +0.0501 [+0.0251, +0.0743] | 0.0023 | 1 | 0.0010 | +0.0346 (0.005) | -0.0155 (0.061) | 0.31 | +0.0429 [+0.0208, +0.0656], 0.0028 | yes |
| late (19–28) | +0.0515 [+0.0268, +0.0784] | 0.0017 | 3 | 0.0010 | +0.0203 (0.113) | -0.0312 (0.001) | 0.61 | +0.0449 [+0.0196, +0.0716], 0.0059 | yes |
| trend (a): placebo line | +0.0507 [+0.0289, +0.0727] | 0.0006 | 1 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0491 [+0.0276, +0.0702] | 0.0012 | 2 | – | – | – | – | – | – |

**PhiR ts_gsr W30** — pre-injection level (windows 1–8) DMT 0.1992, PCB 0.2022

| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |
|---|---|---|---|---|---|---|---|---|---|
| primary (windows 11–28) | +0.0007 [-0.0108, +0.0135] | 0.9155 | 8 | 0.8651 | -0.0019 (0.517) | -0.0026 (0.579) | 3.64 | -0.0006 [-0.0098, +0.0093], 0.9116 | no |
| sensitivity (10–28) | +0.0003 [-0.0109, +0.0127] | 0.9685 | 8 | 0.9510 | -0.0020 (0.492) | -0.0023 (0.613) | 8.85 | -0.0011 [-0.0100, +0.0086], 0.8368 | no |
| early (11–18) | -0.0004 [-0.0133, +0.0146] | 0.9623 | 9 | 0.9471 | -0.0021 (0.575) | -0.0017 (0.729) | -4.44 | -0.0017 [-0.0126, +0.0107], 0.7904 | no |
| late (19–28) | +0.0016 [-0.0099, +0.0136] | 0.8033 | 6 | 0.7393 | -0.0018 (0.487) | -0.0034 (0.517) | 2.11 | +0.0003 [-0.0087, +0.0096], 0.9539 | no |
| trend (a): placebo line | +0.0012 [-0.0088, +0.0125] | 0.8378 | 6 | – | – | – | – | – | – |
| trend (b): shared slope | +0.0004 [-0.0093, +0.0111] | 0.9460 | 7 | – | – | – | – | – | – |

sts at W = 30 on the deconvolved series, for reference (rows in `inference_rows_w30.csv`): ts_gsr −0.0671 [−0.1012, −0.0352], p = 0.0013, phase p = 0.0010, 13/14 negative, survives FD residualisation; ts_demean −0.0791 [−0.1162, −0.0456], p = 0.0007. The raw ts_gsr W30 sts DiD is −0.0686 (`inference_rows_raw.csv`).

What it shows. At W = 30 the deconvolved ΦR DiD is positive on both variants and passes both nulls: ts_gsr +0.0307 [+0.0148, +0.0472], sign-flip p = 0.0023, phase p = 0.0010, 2/14 negative, survives FD residualisation (+0.0257 [+0.0121, +0.0392]); ts_demean +0.0509 [+0.0286, +0.0729], p = 0.0013, phase p = 0.0010, 1/14 negative. Both are larger than at W = 60 (+0.0178 / +0.0350), as is the level: the pre-injection whole-brain ΦR (DMT run, ts_gsr, deconvolved) is 0.235 at W = 30, 0.119 at W = 60 and 0.023 at the global fit. The placebo run's fall carries 56 % (ts_gsr; PCB −0.0172, p = 0.019, DMT +0.0135, p = 0.008) and 48 % (ts_demean) of the DiD, 75 % / 61 % in the late set. The raw ts_gsr W = 30 ΦR contrast is null (+0.0007, p = 0.92), as at W = 60.

### 3.2 The per-subject ΦR DiDs (W = 60, primary set)

DMT change (windows 6–14 minus 1–4 in the DMT run), placebo change, and their difference, per subject:

| subject | deconv ts_gsr: DMT Δ / PCB Δ / DiD | deconv ts_demean: DMT Δ / PCB Δ / DiD | raw ts_gsr: DMT Δ / PCB Δ / DiD | raw ts_demean: DMT Δ / PCB Δ / DiD |
|---|---|---|---|---|
| 1 | +0.0015 / -0.0119 / **+0.0134** | -0.0112 / -0.0004 / **-0.0109** | -0.0182 / -0.0029 / **-0.0153** | -0.0222 / +0.0036 / **-0.0258** |
| 2 | +0.0026 / -0.0407 / **+0.0433** | +0.0026 / -0.0071 / **+0.0097** | -0.0027 / -0.0081 / **+0.0054** | -0.0013 / +0.0137 / **-0.0150** |
| 3 | +0.0148 / -0.0165 / **+0.0313** | +0.0289 / -0.0065 / **+0.0353** | +0.0038 / -0.0171 / **+0.0208** | +0.0028 / -0.0140 / **+0.0168** |
| 4 | +0.0093 / +0.0023 / **+0.0070** | +0.0032 / -0.0129 / **+0.0161** | -0.0022 / +0.0031 / **-0.0053** | -0.0110 / -0.0150 / **+0.0040** |
| 5 | +0.0171 / +0.0028 / **+0.0143** | +0.0288 / +0.0189 / **+0.0099** | +0.0053 / -0.0037 / **+0.0091** | +0.0131 / +0.0081 / **+0.0050** |
| 6 | +0.0095 / -0.0029 / **+0.0124** | -0.0167 / -0.0183 / **+0.0016** | -0.0012 / +0.0029 / **-0.0042** | -0.0099 / +0.0011 / **-0.0110** |
| 7 | +0.0057 / +0.0097 / **-0.0040** | +0.0391 / +0.0126 / **+0.0264** | -0.0044 / +0.0088 / **-0.0132** | +0.0180 / +0.0104 / **+0.0076** |
| 8 | +0.0216 / -0.0404 / **+0.0620** | +0.0384 / -0.0147 / **+0.0531** | +0.0007 / -0.0163 / **+0.0170** | +0.0045 / -0.0012 / **+0.0056** |
| 9 | +0.0096 / -0.0232 / **+0.0328** | +0.0585 / -0.0417 / **+0.1001** | +0.0004 / -0.0014 / **+0.0018** | +0.0448 / -0.0172 / **+0.0619** |
| 10 | +0.0179 / -0.0275 / **+0.0455** | +0.0548 / -0.0305 / **+0.0853** | +0.0087 / -0.0353 / **+0.0440** | +0.0300 / -0.0163 / **+0.0463** |
| 11 | -0.0055 / -0.0135 / **+0.0081** | -0.0010 / -0.0346 / **+0.0336** | -0.0081 / -0.0041 / **-0.0040** | +0.0021 / -0.0060 / **+0.0081** |
| 12 | +0.0010 / -0.0023 / **+0.0032** | +0.0016 / -0.0647 / **+0.0663** | -0.0087 / +0.0004 / **-0.0092** | +0.0456 / -0.0396 / **+0.0852** |
| 13 | -0.0045 / +0.0140 / **-0.0185** | +0.0720 / +0.0103 / **+0.0617** | -0.0033 / +0.0257 / **-0.0290** | +0.0667 / +0.0273 / **+0.0394** |
| 14 | -0.0102 / -0.0082 / **-0.0020** | -0.0343 / -0.0360 / **+0.0017** | -0.0069 / +0.0017 / **-0.0086** | -0.0208 / -0.0128 / **-0.0080** |
| mean (count/14) | +0.0064 (11 rise) / -0.0113 (10 fall) / **+0.0178** (11 pos; median +0.0129) | +0.0189 (10 rise) / -0.0161 (11 fall) / **+0.0350** (13 pos; median +0.0300) | -0.0026 (5 rise) / -0.0033 (8 fall) / **+0.0007** (6 pos; median -0.0041) | +0.0116 (9 rise) / -0.0041 (8 fall) / **+0.0157** (10 pos; median +0.0066) |

Per-subject agreement: deconvolved vs raw ΦR DiD r = +0.81 (ts_gsr; Spearman +0.84) and +0.88 (ts_demean; +0.94); deconvolved ΦR DiD vs deconvolved sts DiD r = −0.77 (ts_gsr; Spearman −0.68) and −0.71 (ts_demean; −0.80).

What it shows. On the deconvolved ts_gsr series the DiD is positive in 11 of 14 subjects (median +0.0129; mean +0.0178; without the subject of largest |DiD|, subject 8 at +0.0620, the mean is +0.0144); the DMT run rises in 11 of 14 (mean +0.0064) and the placebo run falls in 10 of 14 (mean −0.0113); both happen in 8 of 14 subjects, and the placebo change is the larger of the two in magnitude in 10 of 14. On ts_demean 13 of 14 are positive (median +0.0300). The same subjects order the raw DiDs (r = 0.81 and 0.88) although the raw ts_gsr DiD is null (6/14 positive, median −0.0041). The per-subject deconvolved ΦR DiDs and sts DiDs correlate at r = −0.77 / −0.71 (n = 14, no null test; both quantities are linear combinations of the same 16 atoms).

### 3.3 The placebo-run ΦR across windows (W = 60; group mean, SE over 14 subjects)

| series | run | w1 | w2 | w3 | w4 | w5 | w6 | w7 | w8 | w9 | w10 | w11 | w12 | w13 | w14 | pre 1–4 | 5 | 6–9 | 10–14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deconv ts_gsr | DMT | 0.1210 (0.0038) | 0.1153 (0.0032) | 0.1210 (0.0036) | 0.1199 (0.0062) | 0.1380 (0.0051) | 0.1306 (0.0032) | 0.1316 (0.0045) | 0.1302 (0.0067) | 0.1265 (0.0056) | 0.1283 (0.0049) | 0.1240 (0.0033) | 0.1207 (0.0039) | 0.1269 (0.0025) | 0.1131 (0.0031) | 0.1193 | 0.1380 | 0.1297 | 0.1226 |
| deconv ts_gsr | PCB | 0.1375 (0.0055) | 0.1338 (0.0082) | 0.1300 (0.0075) | 0.1256 (0.0029) | 0.1308 (0.0040) | 0.1179 (0.0056) | 0.1273 (0.0050) | 0.1160 (0.0036) | 0.1156 (0.0043) | 0.1248 (0.0081) | 0.1221 (0.0053) | 0.1161 (0.0026) | 0.1169 (0.0054) | 0.1269 (0.0089) | 0.1317 | 0.1308 | 0.1192 | 0.1214 |
| deconv ts_demean | DMT | 0.1424 (0.0062) | 0.1452 (0.0096) | 0.1526 (0.0146) | 0.1576 (0.0117) | 0.1569 (0.0083) | 0.1660 (0.0167) | 0.1905 (0.0231) | 0.1626 (0.0108) | 0.1650 (0.0078) | 0.1610 (0.0126) | 0.1664 (0.0155) | 0.1774 (0.0180) | 0.1809 (0.0220) | 0.1452 (0.0114) | 0.1494 | 0.1569 | 0.1710 | 0.1662 |
| deconv ts_demean | PCB | 0.1743 (0.0113) | 0.1511 (0.0097) | 0.1612 (0.0110) | 0.1650 (0.0196) | 0.1640 (0.0121) | 0.1563 (0.0137) | 0.1592 (0.0125) | 0.1487 (0.0100) | 0.1408 (0.0115) | 0.1413 (0.0070) | 0.1357 (0.0069) | 0.1436 (0.0092) | 0.1504 (0.0135) | 0.1455 (0.0126) | 0.1629 | 0.1640 | 0.1513 | 0.1433 |
| raw ts_gsr | DMT | 0.0952 (0.0021) | 0.0951 (0.0025) | 0.0976 (0.0021) | 0.0966 (0.0032) | 0.0982 (0.0040) | 0.0926 (0.0018) | 0.0951 (0.0029) | 0.0930 (0.0038) | 0.0904 (0.0025) | 0.0954 (0.0025) | 0.0918 (0.0021) | 0.0921 (0.0026) | 0.0970 (0.0028) | 0.0938 (0.0017) | 0.0961 | 0.0982 | 0.0928 | 0.0940 |
| raw ts_gsr | PCB | 0.1042 (0.0043) | 0.1008 (0.0046) | 0.1004 (0.0053) | 0.0958 (0.0019) | 0.1025 (0.0039) | 0.0981 (0.0046) | 0.1010 (0.0045) | 0.0946 (0.0031) | 0.0922 (0.0030) | 0.0988 (0.0041) | 0.0969 (0.0043) | 0.0905 (0.0022) | 0.0934 (0.0028) | 0.1072 (0.0079) | 0.1003 | 0.1025 | 0.0965 | 0.0974 |
| raw ts_demean | DMT | 0.1224 (0.0059) | 0.1187 (0.0065) | 0.1217 (0.0098) | 0.1204 (0.0083) | 0.1279 (0.0074) | 0.1277 (0.0154) | 0.1463 (0.0191) | 0.1288 (0.0113) | 0.1232 (0.0064) | 0.1236 (0.0096) | 0.1339 (0.0132) | 0.1350 (0.0152) | 0.1477 (0.0179) | 0.1253 (0.0087) | 0.1208 | 0.1279 | 0.1315 | 0.1331 |
| raw ts_demean | PCB | 0.1326 (0.0073) | 0.1159 (0.0045) | 0.1202 (0.0073) | 0.1307 (0.0146) | 0.1373 (0.0091) | 0.1245 (0.0091) | 0.1258 (0.0088) | 0.1216 (0.0095) | 0.1193 (0.0108) | 0.1182 (0.0055) | 0.1154 (0.0056) | 0.1102 (0.0049) | 0.1219 (0.0075) | 0.1294 (0.0119) | 0.1248 | 0.1373 | 0.1228 | 0.1190 |

Baseline and slope (per subject, exact sign-flip and 10,000-draw bootstrap CI; `phir_baseline_and_slope.log`). Not in the recorded plan: these four tests were added after looking at the window series above, and are descriptive.

| series | DMT pre − PCB pre (windows 1–4) | placebo-run linear slope per window (14 windows) | DMT-run slope | placebo window 4 − window 1 |
|---|---|---|---|---|
| deconvolved ts_gsr | −0.0124 [−0.0210, −0.0042], p = 0.014; DMT lower in 12/14 | −0.00115 [−0.00200, −0.00028], p = 0.025; negative in 10/14 | −0.00003, p = 0.90 | −0.0120 [−0.0234, −0.0007], p = 0.067 |
| deconvolved ts_demean | −0.0135 [−0.0266, −0.0009], p = 0.072; 9/14 | −0.00202 [−0.00321, −0.00074], p = 0.012; 11/14 | +0.00155, p = 0.17 | −0.0093 [−0.0475, +0.0298], p = 0.66 |
| raw ts_gsr | −0.0042 [−0.0114, +0.0025], p = 0.28; 8/14 | −0.00036 [−0.00117, +0.00050], p = 0.43; 8/14 | −0.00023, p = 0.12 | −0.0084 [−0.0168, −0.0015], p = 0.039 |
| raw ts_demean | −0.0040 [−0.0143, +0.0061], p = 0.47; 9/14 | −0.00063 [−0.00150, +0.00037], p = 0.22; 9/14 | +0.00114, p = 0.15 | −0.0019 [−0.0249, +0.0246], p = 0.89 |

What it shows. On the deconvolved ts_gsr series the placebo run's ΦR is highest in window 1 (0.1375) and declines through the run — 0.1338, 0.1300, 0.1256 over the pre-injection windows, 0.1308 at window 5, then 0.1156–0.1273 (mean 0.1192) over windows 6–9 and 0.1161–0.1269 (0.1214) over 10–14; a linear slope of −0.00115 per window (p = 0.025, negative in 10/14 subjects), with the pre-injection windows alone falling by 0.0120 (p = 0.067). The DMT run starts lower than the placebo run (pre-injection 0.1193 vs 0.1317, difference −0.0124, p = 0.014, lower in 12/14 subjects), rises to 0.1380 at window 5 (the injection window, excluded from every contrast), stays at 0.1297 over windows 6–9 and 0.1226 over 10–14, and has no linear trend (slope −0.00003). The two runs differ at baseline by 0.0124 (DMT lower), against a DiD of 0.0178; after injection the DMT run is above the placebo run by 0.0105 over windows 6–9 (0.1297 vs 0.1192) and by 0.0012 over windows 10–14 (0.1226 vs 0.1214). ts_demean: placebo highest at window 1 (0.1743), slope −0.00202 per window (p = 0.012, negative in 11/14); DMT pre − PCB pre −0.0135 (p = 0.072, DMT lower in 9/14). On the raw series the placebo decline and the baseline difference are both absent at p < 0.05 (slope −0.00036, p = 0.43; baseline −0.0042, p = 0.28, ts_gsr), and the window-1 placebo value (0.1042) is the highest of windows 1–13, with window 14 at 0.1072.
