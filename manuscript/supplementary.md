# Supplementary tables

Companion to `manuscript/draft_v2.md`, which cites S1–S8 Tables from its S1 Text (the original pre-specified analysis; `manuscript/draft.md`, which they first accompanied, is kept as a record) and S9 Table from Results 4 and S3 Text. Every value is quoted from the named results file. Nats throughout; N = 14; sign-flip p exact over 2^14 assignments, two-sided; CIs are subject-bootstrap 95 % (10,000 draws); seed 20261120.

## S1 Table. Step contrast on the sensitivity windows 5–14 (bins 9–28) vs pre-injection windows 1–4, W = 60

Source: `results/primary_b_ts_gsr_win60.csv` (git e46df8a), `results/primary_b_ts_demean_win60.csv` (git f3b435d).

| quantity | ts_gsr | ts_demean |
|---|---|---|
| DMT post − pre | −0.0491 [−0.0823, −0.0128], p = 0.0227 | −0.0621 [−0.1055, −0.0130], p = 0.0300 |
| PCB post − pre | +0.0242 [−0.0020, +0.0496], p = 0.1040 | +0.0314 [+0.0013, +0.0585], p = 0.0637 |
| DiD raw | −0.0733 [−0.1180, −0.0291], p = 0.0070; phase-randomised p = 0.0020; 12/14 negative; −6.3 % of baseline | −0.0935 [−0.1431, −0.0426], p = 0.0039; phase-randomised p = 0.0010; 12/14 negative; −8.5 % |
| FD DiD | +0.0191 [−0.0008, +0.0402], p = 0.1083 | same |
| DiD FD-residualised | −0.0555 [−0.0864, −0.0210], p = 0.0100; 13/14 | −0.0714 [−0.1106, −0.0298], p = 0.0073; 12/14 |

W = 30 positive control (`results/primary_b_ts_gsr_win30.csv`, git ac1fdc0), ts_gsr, pre = bins 1–8: primary post bins 11–28, DiD raw −0.0686 [−0.1084, −0.0293], p = 0.0042, phase-randomised p = 0.0010, 13/14 negative, −6.7 % of the W = 30 pre-injection DMT mean of 1.0223; DMT post − pre −0.0390 [−0.0680, −0.0058], p = 0.0354; PCB post − pre +0.0296 [+0.0076, +0.0531], p = 0.0269; FD-residualised −0.0545 [−0.0836, −0.0215], p = 0.0065, 13/14. Sensitivity bins 10–28: DiD −0.0658 [−0.1072, −0.0261], p = 0.0067; residualised −0.0514 [−0.0799, −0.0179], p = 0.0109.

## S2 Table. Tier-2 intensity tracking, decay windows, DMT run, W = 60

Source: as S1 Table. ρ_S = Spearman correlation. "Group-mean series" is the 14-subject mean sts series vs the group intensity template f (thresholded at |ρ| ≥ 0.80; p vs the phase-randomised null). "Per-subject" is the group mean of per-subject ρ_S vs own ratings (primary) or vs f (sensitivity), tested for existence against the null, not thresholded. Control (a): the within-subject difference ρ_DMT − ρ_PCB (template) must have a CI excluding zero and PCB must be below half of DMT. Control (b): the same three conditions on FD-residualised sts. Sign is negative in every cell against the pre-specified positive direction.

| statistic | ts_gsr, windows 6–14 (primary) | ts_gsr, windows 5–14 (sensitivity) | ts_demean, windows 6–14 | ts_demean, windows 5–14 |
|---|---|---|---|---|
| Raw group-mean series ρ_S (p) | −0.9833 (0.0020), PASS | −0.8667 (0.0300), PASS | −0.9333 (0.0120), PASS | −0.6727 (0.1968), fail |
| Raw per-subject vs own ratings | −0.4826 [−0.6291, −0.3362], p = 0.0010 | −0.4267 [−0.5949, −0.2473], p = 0.0010 | −0.3041 [−0.4882, −0.1027], p = 0.0210 | −0.2403 [−0.4233, −0.0366], p = 0.0639 |
| Raw per-subject vs template | −0.5333 [−0.6750, −0.3845], p = 0.0010 | −0.4658 [−0.6294, −0.2840], p = 0.0010 | −0.3667 [−0.5476, −0.1548], p = 0.0090 | −0.2883 [−0.4874, −0.0675], p = 0.0260 |
| Raw control (a): PCB ρ_S vs template | −0.1940 [−0.3143, −0.0785], p = 0.0809 | −0.3307 [−0.4494, −0.2087], p = 0.0050 | −0.2345 [−0.3786, −0.0893], p = 0.0330 | −0.3550 [−0.4909, −0.1931], p = 0.0020 |
| Raw control (a): ρ_DMT − ρ_PCB | −0.3393 [−0.5179, −0.1619], clears | −0.1351 [−0.2935, +0.0338], VOID | −0.1321 [−0.3655, +0.1084], VOID | +0.0667 [−0.1195, +0.2658], VOID |
| Control (b): FD (DMT) ρ_S vs template | +0.4060 [+0.1774, +0.6000] | +0.5117 [+0.3489, +0.6632] | +0.4060 [+0.1774, +0.6000] | +0.5117 [+0.3489, +0.6632] |
| FD-resid group-mean series ρ_S (p) | −0.9500 (0.0010), PASS | −0.5152 (0.2168), fail | −0.8833 (0.0060), PASS | −0.4545 (0.3167), fail |
| FD-resid per-subject vs own ratings | −0.3310 [−0.4761, −0.1592], p = 0.0010 | −0.2358 [−0.3757, −0.0903], p = 0.0130 | −0.1874 [−0.3608, −0.0026], p = 0.0689 | −0.1243 [−0.3226, +0.0836], p = 0.2068 |
| FD-resid per-subject vs template | −0.3643 [−0.5179, −0.1810], p = 0.0010 | −0.2797 [−0.4277, −0.1203], p = 0.0050 | −0.2429 [−0.4333, −0.0500], p = 0.0210 | −0.1766 [−0.3827, +0.0545], p = 0.0799 |
| FD-resid control (a): PCB ρ_S | −0.1571 [−0.3155, −0.0190], p = 0.0500 | −0.2848 [−0.4199, −0.1558], p = 0.0010 | −0.1000 [−0.2036, +0.0071], p = 0.2208 | −0.2831 [−0.4017, −0.1532], p = 0.0010 |
| FD-resid control (a): ρ_DMT − ρ_PCB | −0.2071 [−0.4345, +0.0345], VOID | +0.0052 [−0.2017, +0.2026], VOID | −0.1429 [−0.3357, +0.0667], VOID | +0.1065 [−0.0918, +0.3126], VOID |
| Tier-2 claim | VOID | VOID | VOID | VOID |

W = 30 (ts_gsr, bins 11–28; check only, decides nothing): group-mean series ρ_S −0.9752 raw, −0.8535 FD-residualised; per-subject means −0.388 / −0.408 raw, −0.267 / −0.279 residualised, all p ≤ 0.002; control (a) clears on raw (−0.223 [−0.415, −0.043]) and is void on the residualised data (−0.146 [−0.337, +0.031]).

## S3 Table. Exploratory regional DiD: regions surviving BH FDR (q = 0.05)

Source: `results/regional_analysis_<variant>.csv`, `results/regional_did_map_<variant>.csv` (git 4f7437b). Global fit; pre bins 1–8, post bins 11–28; group-mean DiD negative in 114 of 115 regions on both variants; the one positive region is subcortical parcel 104 (+0.028, p = 0.495 on ts_gsr; +0.019, p = 0.566 on ts_demean). BH thresholds: p = 0.00304 (ts_gsr, 7 regions), 0.00826 (ts_demean, 19 regions). All survivors negative and cortical. **Exploratory.**

ts_gsr:

| region | idx | Yeo net | DiD | p | negative/14 |
|---|---|---|---|---|---|
| LH_DorsAttn_Post_2 | 16 | 3 | −0.147383 | 0.00073 | 13 |
| LH_DorsAttn_PrCv_1 | 21 | 3 | −0.143504 | 0.00269 | 12 |
| LH_Default_Par_1 | 39 | 7 | −0.168352 | 0.00024 | 13 |
| RH_SomMot_3 | 60 | 2 | −0.103882 | 0.00195 | 12 |
| RH_SomMot_8 | 65 | 2 | −0.116150 | 0.00256 | 11 |
| RH_SalVentAttn_TempOccPar_2 | 74 | 4 | −0.105710 | 0.00183 | 13 |
| RH_Default_Temp_3 | 92 | 7 | −0.152747 | 0.00085 | 13 |

ts_demean:

| region | idx | Yeo net | DiD | p | negative/14 |
|---|---|---|---|---|---|
| LH_Vis_3 | 2 | 1 | −0.159528 | 0.00623 | 11 |
| LH_Vis_4 | 3 | 1 | −0.133486 | 0.00562 | 11 |
| LH_Vis_6 | 5 | 1 | −0.182763 | 0.00745 | 12 |
| LH_Vis_8 | 7 | 1 | −0.122007 | 0.00806 | 12 |
| LH_Vis_9 | 8 | 1 | −0.158145 | 0.00427 | 11 |
| LH_SomMot_4 | 12 | 2 | −0.107238 | 0.00598 | 11 |
| LH_DorsAttn_Post_2 | 16 | 3 | −0.151416 | 0.00293 | 12 |
| LH_DorsAttn_Post_4 | 18 | 3 | −0.135552 | 0.00134 | 12 |
| LH_DorsAttn_PrCv_1 | 21 | 3 | −0.164079 | 0.00220 | 12 |
| LH_DorsAttn_FEF_1 | 22 | 3 | −0.162117 | 0.00317 | 12 |
| LH_Cont_pCun_1 | 35 | 6 | −0.127629 | 0.00708 | 12 |
| LH_Default_Par_1 | 39 | 7 | −0.137965 | 0.00085 | 13 |
| LH_Default_pCunPCC_1 | 48 | 7 | −0.159728 | 0.00256 | 12 |
| RH_Vis_5 | 54 | 1 | −0.123981 | 0.00562 | 12 |
| RH_Vis_7 | 56 | 1 | −0.122318 | 0.00732 | 11 |
| RH_Vis_8 | 57 | 1 | −0.144144 | 0.00159 | 12 |
| RH_SalVentAttn_TempOccPar_2 | 74 | 4 | −0.105911 | 0.00818 | 12 |
| RH_Default_PFCv_2 | 94 | 7 | −0.133180 | 0.00525 | 12 |
| RH_Default_pCunPCC_1 | 98 | 7 | −0.114772 | 0.00781 | 12 |

Common to both variants: LH_DorsAttn_Post_2, LH_DorsAttn_PrCv_1, LH_Default_Par_1, RH_SalVentAttn_TempOccPar_2.

## S4 Table. Exploratory workspace comparison

Source: `results/regional_analysis_<variant>.csv`. Per-subject mean regional DiD inside the proxy minus outside it (negative = larger decrease inside). Primary proxy = Yeo Default ∪ Control (37 cortical parcels; gateway proxy = Default 24, broadcaster proxy = Control 13); named-subregion proxy = 26 parcels (gateway 21, broadcaster 5). Non-workspace = remaining cortical parcels, or remaining cortical + 16 subcortical ("+ subcortex"). **Exploratory.**

| proxy | non-workspace set | ts_gsr Δ [CI], p, negative/14 | ts_demean Δ [CI], p, negative/14 |
|---|---|---|---|
| primary | cortical (62) | −0.0095 [−0.0230, +0.0050], 0.216, 9 | −0.0050 [−0.0225, +0.0120], 0.590, 7 |
| primary | + subcortex (78) | −0.0124 [−0.0264, +0.0024], 0.130, 10 | −0.0119 [−0.0300, +0.0063], 0.242, 8 |
| named | cortical (73) | −0.0108 [−0.0305, +0.0099], 0.325, 8 | −0.0070 [−0.0305, +0.0170], 0.583, 8 |
| named | + subcortex (89) | −0.0135 [−0.0337, +0.0074], 0.235, 9 | −0.0130 [−0.0363, +0.0110], 0.318, 9 |
| gateway proxy − non-workspace (primary, cortical) | | −0.0189 [−0.0356, −0.0012], 0.060, 10 | −0.0094 [−0.0315, +0.0129], 0.442, 8 |
| gateway proxy − non-workspace (primary, + subcortex) | | −0.0219 [−0.0399, −0.0028], 0.047, 9 | −0.0163 [−0.0392, +0.0078], 0.211, 11 |
| broadcaster proxy − non-workspace (primary, cortical) | | +0.0079 [−0.0128, +0.0285], 0.474, 5 | +0.0030 [−0.0195, +0.0276], 0.813, 7 |
| gateway − broadcaster (primary) | | −0.0268 [−0.0514, −0.0007], 0.072 | −0.0124 [−0.0436, +0.0183], 0.459 |

Set means, primary proxy vs cortical non-workspace: ts_gsr workspace −0.0885 [−0.1457, −0.0329], p = 0.0078, non-workspace −0.0791 [−0.1299, −0.0290], p = 0.0083; ts_demean workspace −0.1115 [−0.1816, −0.0375], p = 0.0131, non-workspace −0.1065 [−0.1722, −0.0392], p = 0.0118. Rank-rule check on the placebo run (descriptive): 52 (ts_gsr) and 58 (ts_demean) of 115 regions have synergy rank above redundancy rank; overlap with the 37-parcel primary proxy 20 (Jaccard 0.323) and 32 (Jaccard 0.571).

## S5 Table. Exploratory receptor-map correlations

Source: `results/regional_analysis_<variant>.csv`. Spearman ρ between the group-mean regional DiD map and receptor density on the 99 cortical parcels; two-sided spin p over 10,000 rotations (Váša one-sided-average p in brackets); BH across the five maps: nothing significant on either variant. The 115-region ρ including subcortex has no spatial null and is descriptive. **Exploratory.**

| map | ts_gsr ρ (p) [Váša p] | 115-region ρ | ts_demean ρ (p) [Váša p] | 115-region ρ |
|---|---|---|---|---|
| 5-HT2A | −0.160 (0.116) [0.070] | −0.230 | −0.055 (0.677) [0.360] | −0.263 |
| 5-HT1A | +0.009 (0.929) [0.467] | −0.099 | +0.265 (0.032) [0.012] | +0.038 |
| 5-HT1B | −0.094 (0.352) [0.185] | −0.144 | −0.263 (0.050) [0.033] | −0.314 |
| 5-HT4 | −0.084 (0.422) [0.228] | +0.008 | +0.182 (0.160) [0.066] | +0.231 |
| 5-HTT | +0.104 (0.324) [0.145] | +0.196 | +0.202 (0.096) [0.039] | +0.365 |

Receptor inter-correlations (Spearman, 115 regions): 1A–2A 0.532, 1B–2A 0.528, 2A–4 0.436, 2A–HTT −0.451, 1A–4 0.405, 1B–HTT −0.364, 1A–HTT −0.100, 4–HTT 0.068, 1B–4 0.056, 1A–1B −0.002.

## S6 Table. EEG Lempel-Ziv complexity vs ΦID quantities, global fit, 28 bins

Source: `results/lz_vs_tdmi_<variant>.csv` (git 84ea657). Per-subject Spearman ρ across the 28 bins, group mean with subject-bootstrap CI; p against 1,000 phase-randomised surrogates of the LZ series (one-sided in the predicted direction; two-sided in brackets); "series" = ρ of the group-mean series with its two-sided p.

| variant | quantity | run | ρ mean [CI] | subjects in predicted sign | p one-sided (two-sided) | series ρ (p) |
|---|---|---|---|---|---|---|
| ts_gsr | TDMI | DMT | −0.2416 [−0.4011, −0.0765] | 10/14 | 0.0020 (0.0030) | −0.8276 (0.0030) |
| ts_gsr | TDMI | PCB | −0.0468 [−0.1375, +0.0387] | 8/14 | 0.2208 (0.4196) | −0.0969 (0.6603) |
| ts_gsr | sts | DMT | −0.2390 [−0.3800, −0.0930] | 9/14 | 0.0010 (0.0010) | −0.8041 (0.0070) |
| ts_gsr | rtr | DMT | −0.1621 [−0.2741, −0.0490] | 3/14 (predicted +) | 0.9910 (0.0240) | −0.7132 (0.0160) |
| ts_demean | TDMI | DMT | −0.2143 [−0.3679, −0.0644] | 10/14 | 0.0040 (0.0070) | −0.7230 (0.0490) |
| ts_demean | TDMI | PCB | −0.0926 [−0.1795, −0.0076] | 9/14 | 0.0450 (0.0879) | −0.1149 (0.6164) |
| ts_demean | sts | DMT | −0.2026 [−0.3457, −0.0674] | 9/14 | 0.0070 (0.0110) | −0.6694 (0.0709) |
| ts_demean | rtr | DMT | −0.0229 [−0.1101, +0.0685] | 5/14 (predicted +) | 0.6284 (0.7143) | +0.0668 (0.8282) |

## S7 Table. Global functional connectivity per bin set

Source: `results/global_fc_did_<variant>.csv` (git 66b570e-dirty). Mean Pearson r over the 6,555 pairs; DiD form as in the main text; the whole-brain sts DiD from the global-fit atoms on the identical bins alongside.

| variant | bin set | mean r DiD [CI], p, neg/pos | sts DiD (nats) [CI], p, neg/pos |
|---|---|---|---|
| ts_demean | primary 11–28 | +0.0526 [+0.0073, +0.0976], 0.0470, 4/10 | −0.1035 [−0.1678, −0.0357], 0.0132, 11/3 |
| ts_demean | sensitivity 9–28 | +0.0532 [+0.0113, +0.0930], 0.0322, 4/10 | −0.0909 [−0.1536, −0.0254], 0.0175, 11/3 |
| ts_demean | peak 9–14 | +0.0746 [+0.0293, +0.1282], 0.0046, 3/11 | −0.0810 [−0.1446, −0.0176], 0.0348, 11/3 |
| ts_gsr | primary 11–28 | −0.0034 [−0.0051, −0.0017], 0.0024, 11/3 | −0.0801 [−0.1303, −0.0310], 0.0071, 12/2 |
| ts_gsr | peak 9–14 | −0.0032 [−0.0050, −0.0015], 0.0023, 12/2 | −0.0752 [−0.1114, −0.0335], 0.0044, 13/1 |

Pre-injection mean r: ts_demean DMT 0.1905, PCB 0.1813; ts_gsr DMT −0.0020, PCB −0.0039 (GSR pins the mean near zero by construction; every ts_gsr bin lies within −0.0058 to −0.0008).

## S8 Table. Post-hoc proportionality: sts / TDMI ratio DiD, four cells

Source: `results/proportionality.csv` (script `14_proportionality.py` at git dbf2311; interpretation rule recorded in the script docstring and in the project orientation file before the run). Post-hoc, specified after the primary result, reported regardless of outcome. Ratio = sts / TDMI (TDMI = Σ 16 atoms) per subject, condition and window (W = 60) or bin (global fit); DiD = (post − pre)_DMT − (post − pre)_PCB on the mean ratio over the window set; exact sign-flip p over 2^14 assignments, two-sided; subject-bootstrap 95 % CI, 10,000 draws, seed 20261120. Windows: W = 60, pre 1–4, post 6–14; global fit, pre bins 1–8, post 11–28. Verdict by the pre-recorded rule: CI includes zero → proportional; significantly negative → more than proportional; significantly positive → less than proportional. (i) = sts share of TDMI at pre-injection baseline on the DMT run (subject mean, with CI); (ii) = sts DiD / TDMI DiD on the group means, with a subject-bootstrap CI of the ratio of means. (i) and (ii) are comparable within a cell, not across estimators: the windowed and global fits give different baseline shares because per-window finite-sample bias falls on sts and on the self-transfer atoms. No temporal null, no motion handling.

| estimator | variant | ratio DiD [CI], p, neg/14 | verdict | (i) baseline share [CI] | (ii) share of TDMI DiD [CI] | sts DiD (nats) | TDMI DiD (nats) |
|---|---|---|---|---|---|---|---|
| windowed W = 60 | ts_gsr | +0.0005 [−0.0081, +0.0083], 0.9138, 6 | proportional | 0.7820 [0.7779, 0.7857] | 0.7797 [0.6531, 0.9362] | −0.0809 [−0.1266, −0.0371] | −0.1037 [−0.1597, −0.0481] |
| windowed W = 60 | ts_demean | −0.0095 [−0.0235, +0.0049], 0.2195, 9 | proportional | 0.7670 [0.7590, 0.7748] | 0.8697 [0.6909, 1.0063] | −0.1031 [−0.1540, −0.0516] | −0.1186 [−0.1704, −0.0675] |
| global fit | ts_gsr | +0.0204 [+0.0048, +0.0340], 0.0248, 4 | less than proportional | 0.9082 [0.8994, 0.9167] | 0.6584 [0.4864, 0.8174] | −0.0801 [−0.1320, −0.0316] | −0.1216 [−0.1914, −0.0519] |
| global fit | ts_demean | +0.0071 [−0.0167, +0.0292], 0.5623, 5 | proportional | 0.8967 [0.8856, 0.9074] | 0.7867 [0.5004, 1.0127] | −0.1035 [−0.1678, −0.0359] | −0.1315 [−0.2001, −0.0610] |

Within-condition ratio changes (post − pre): windowed ts_gsr DMT +0.0034 [−0.0004, +0.0070], p = 0.1097, PCB +0.0028 [−0.0030, +0.0090], p = 0.3990; windowed ts_demean DMT −0.0093 [−0.0215, +0.0019], p = 0.1621, PCB +0.0001 [−0.0071, +0.0074], p = 0.9712; global ts_gsr DMT +0.0167 [+0.0052, +0.0279], p = 0.0183, PCB −0.0037 [−0.0116, +0.0044], p = 0.3949; global ts_demean DMT +0.0015 [−0.0183, +0.0203], p = 0.8799, PCB −0.0056 [−0.0143, +0.0042], p = 0.2753. The sts DiD reproduces Table 2 of `draft_v2.md` and the TDMI DiD its Table 1, and both reproduce `results/windowed_atoms_did_ts_gsr_win60.csv` (bootstrap CIs differ in the third decimal from the main-text values because the draw order differs; point estimates are identical).

## S9 Table. The cross-lag budget of Results 4: data, finite-sample null, null-corrected terms and shares; the controls; the superseded values of 16 September 2026, 10:32 UTC

Source: `notes/review_results/partB/crosslag_budget_tables.md` (data; `partB12_crosslag_budget.py`) and `crosslag_budget_null_tables.md` (null, controls, null-corrected budget and the mechanical reading; `partB13_crosslag_budget_null.py`), both at git 6b5181a, seed 20261120; definitions in Methods and `notes/rev_crosslag_budget.py`; the rules in the record's pre-run entry of 16 September 2026, 16:24 UTC, and the outcome of 16:37 UTC. Terms per subject and run are means over the 6,555 pairs, s = the sign of the pair's run-level q; grand mean = mean over subjects of the per-subject mean of the two runs, with subject-bootstrap 95 % CI (10,000 draws); the null value is the mean over the two run types of ≥ 25,000 simulated pair-runs each (Monte-Carlo SE in parentheses); the null-corrected value is data minus null with the data interval shifted; the range is over the six null configurations (0 primary: heterogeneity 0.5, DMT-post/placebo ACF, mixture q solved to the run-level a, |q̂| and fraction |q̂| < 0.05; 1 heterogeneity 0.25; 2 heterogeneity 1.0; 3 placebo ACF for both run types; 4 Gaussian q; 5 mixture solved to the W = 60 window-level means). Identity (by construction): δ_run = δ_within + δ_pool + δ_means + ε, to 6.9 × 10⁻¹⁸. Nats-free (correlation units).

| ts_gsr | δ_run | δ_within | δ_pool | δ_means | ε | δ_60 (run-level sign) | window-sign value |
|---|---|---|---|---|---|---|---|
| data, grand mean [CI] | +0.00340 [+0.00300, +0.00380] | +0.00291 [+0.00257, +0.00325] | +0.00050 [+0.00038, +0.00062] | +0.00001 [−0.00000, +0.00003] | −0.00002 [−0.00004, +0.00001] | +0.00245 [+0.00212, +0.00281] | +0.00611 [+0.00563, +0.00665] |
| data, DMT run [CI] | +0.00381 [+0.00339, +0.00424] | +0.00310 [+0.00277, +0.00343] | +0.00069 [+0.00053, +0.00086] | +0.00002 [−0.00000, +0.00004] | −0.00000 [−0.00005, +0.00004] | +0.00264 [+0.00227, +0.00301] | +0.00615 [+0.00575, +0.00660] |
| data, placebo run [CI] | +0.00299 [+0.00235, +0.00363] | +0.00272 [+0.00215, +0.00327] | +0.00030 [+0.00019, +0.00042] | +0.00000 [−0.00002, +0.00002] | −0.00003 [−0.00005, −0.00001] | +0.00226 [+0.00170, +0.00280] | +0.00608 [+0.00535, +0.00685] |
| null, primary configuration (SE) | +0.00039 (0.00003) | +0.00040 (0.00003) | +0.00003 (0.00001) | −0.00002 (0.00000) | −0.00002 (0.00000) | +0.00017 (0.00003) | +0.00352 (0.00003) |
| null, primary, DMT type / placebo type | +0.00031 / +0.00047 | +0.00034 / +0.00047 | +0.00003 / +0.00004 | −0.00004 / −0.00001 | −0.00002 / −0.00002 | +0.00013 / +0.00022 | +0.00330 / +0.00373 |
| null, range over configurations 0–5 | +0.00029 to +0.00046 | +0.00031 to +0.00044 | +0.00002 to +0.00005 | −0.00002 to −0.00001 | −0.00002 to −0.00002 | +0.00007 to +0.00021 | +0.00332 to +0.00364 |
| null-corrected, primary [CI] | +0.00301 [+0.00261, +0.00340] | +0.00250 [+0.00217, +0.00285] | +0.00046 [+0.00035, +0.00059] | +0.00004 [+0.00002, +0.00005] | +0.00000 [−0.00002, +0.00003] | +0.00228 [+0.00194, +0.00263] | +0.00259 [+0.00211, +0.00313] |
| null-corrected, range | +0.00294 to +0.00311 | +0.00247 to +0.00260 | +0.00045 to +0.00048 | +0.00002 to +0.00004 | −0.00000 to +0.00001 | +0.00224 to +0.00238 | +0.00247 to +0.00279 |
| share of δ_run,c, primary (range) | — | 0.833 (0.833–0.839) | 0.154 (0.152–0.155) | 0.012 (0.007–0.012) | 0.001 (−0.000 to 0.002) | — | — |
| label under rule (b), the same in every configuration | — | most | a minor part | a minor part | — | — | — |

| ts_demean (no null; not read) | δ_run | δ_within | δ_pool | δ_means | ε | δ_60 (run-level sign) | window-sign value |
|---|---|---|---|---|---|---|---|
| data, grand mean [CI] | −0.00262 [−0.00495, −0.00037] | −0.00226 [−0.00428, −0.00034] | −0.00030 [−0.00069, +0.00001] | +0.00000 [−0.00001, +0.00002] | −0.00005 [−0.00011, +0.00000] | −0.00274 [−0.00478, −0.00079] | +0.00160 [−0.00019, +0.00326] |
| data, DMT run [CI] | −0.00324 [−0.00614, −0.00079] | −0.00270 [−0.00498, −0.00073] | −0.00047 [−0.00120, +0.00011] | −0.00000 [−0.00003, +0.00003] | −0.00007 [−0.00013, −0.00001] | −0.00313 [−0.00549, −0.00109] | +0.00108 [−0.00090, +0.00285] |
| data, placebo run [CI] | −0.00199 [−0.00465, +0.00041] | −0.00182 [−0.00418, +0.00036] | −0.00014 [−0.00041, +0.00009] | +0.00000 [−0.00002, +0.00002] | −0.00004 [−0.00014, +0.00005] | −0.00235 [−0.00472, −0.00017] | +0.00212 [+0.00010, +0.00393] |

| controls (primary parameters; mean over run types) | δ_run | δ_within | δ_pool | δ_means | ε | shares within / pool / means / ε |
|---|---|---|---|---|---|---|
| (i) common drive: λ = 0.2, a_s − a_n = 0.10 (population d = +0.01600) | +0.01438 | +0.01291 | +0.00129 | +0.00027 | −0.00010 | 0.898 / 0.090 / 0.019 / −0.007 |
| (ii) pooling: q and filter change at TR 240 (β₁ ~ N(6β̄, h·6β̄), β₂ ~ N(β̄/5, h·β̄/5), q₂ = q₁(1 − g), g ~ U(0.5, 1); δ_pool at 49 and 44 Monte-Carlo SEs) | +0.00131 | +0.00040 | +0.00095 | −0.00002 | −0.00001 | 0.303 / 0.723 / −0.015 / −0.011 |

Rule (e), the per-subject difference DMT − placebo, null-corrected at the primary configuration: δ_pool,c +0.00039 (exact sign-flip p = 0.0006, positive in 12 of 14; +0.00037 to +0.00041, p ≤ 0.0007, in the other configurations), 0.11 of the DMT-run δ_run,c (+0.00349) — "pooling is larger on the DMT run"; δ_within,c +0.00052 (p = 0.1368) and δ_means,c +0.00005 (p = 0.0112), reported with no rule. Reading under rules (a)–(f), the same in every configuration: finite sampling a minor part (F = δ_run,null / δ_run from 0.085 to 0.135); the within-window term most, pooling and the window means a minor part each; the null's q distribution is symmetric (fraction q̂ < 0 0.50) where the data's has 0.545 of pairs below zero.

Superseded values of 16 September 2026, 10:32 UTC (`crosslag_deviation_tables.md`, sections A and B at git 9a19b10; record, correction note of 16 September, 16:24 UTC), reported here and no longer read: at W = 60 with the sign of each window's own q, `ts_gsr` +0.00611 [+0.00563, +0.00665] (DMT +0.00615, placebo +0.00608; slope of the deviation on q +0.0201) and `ts_demean` +0.00160 [−0.00019, +0.00326]; the finite-sample null with the same weight, homogeneous filter, +0.00348 at W = 60 (the four operating-point cells +0.00344, +0.00311, +0.00325, +0.00356) and +0.00662 at W = 30; the same null's run-level value +0.00025 ± 0.00005 at W = 840 (mean |q̂| 0.222 against the data's 0.1945). The readings drawn from them — "near zero: finite sampling removed" and "comparable to the run-level value (1.80 raw, 0.77–0.81 net): a stationary mechanism rather than pooling" — are superseded because the window's sign selects on the same samples as the deviation (about half of +0.00611 is that selection: the null's +0.00348), the null's run-level value was read at a different density of q̂ near zero (the null solved to the data gives +0.00029 to +0.00046), and the ratio compared two differently biased statistics without computing pooling; the budget above computes it.

Earlier values of the same statistic, removed from Results 4 in the revision of 16 September and kept here (record, 15 September 2026, 15:36 and 18:18 UTC, and 16 September, 10:32 UTC; `crosslag_deviation_tables.md`): the signed mean over pairs, `ts_gsr` +0.00009 [+0.00005, +0.00013] (sign-flip p = 0.0004, positive in 13 of 14; pair-level SD of the deviation 0.0390) and `ts_demean` −0.00738 [−0.00902, −0.00588] (p = 0.0001, negative in 14 of 14), which on `ts_gsr` cancels between the 54.5 % of pairs with q < 0 (mean deviation −0.00304) and the pairs with q > 0 (+0.00384); the correlation across the 28 runs of the run-level statistic with the run-level residual, −0.767 (sign(q)-weighted) against −0.277 (signed) on `ts_gsr` and −0.969 against −0.890 on `ts_demean`; the slope of the deviation on q across pairs, +0.0163 [+0.0141, +0.0187] at the run level and +0.0201 [+0.0184, +0.0222] at W = 60 on `ts_gsr`, +0.0211 [+0.0194, +0.0227] and +0.0237 [+0.0219, +0.0255] on `ts_demean`; on `ts_demean` the run-level sign(q)-weighted mean −0.00262 (sign-flip p = 0.0532, positive in 5 of 14; −0.00582 among the q > 0 pairs, −0.01441 among the q < 0 pairs) and the W = 60 window-sign value +0.00160 (p = 0.1061); and the family-scale conversion at the operating point (0.85, 0.25), where a deviation of +0.006 gives a residual of −0.0103, +0.0034 gives −0.0061 (44 % of the observed −0.0137) and, at the pairs' mean run-level a and |q| (0.8666, 0.1945), −0.0051 (37 %).
