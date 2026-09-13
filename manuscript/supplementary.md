# Supplementary tables

Companion to `manuscript/draft.md`. Every value is quoted from the named results file. Nats throughout; N = 14; sign-flip p exact over 2^14 assignments, two-sided; CIs are subject-bootstrap 95 % (10,000 draws); seed 20261120.

## Table S1. Step contrast on the sensitivity windows 5–14 (bins 9–28) vs pre-injection windows 1–4, W = 60

Source: `results/primary_b_ts_gsr_win60.csv` (git e46df8a), `results/primary_b_ts_demean_win60.csv` (git f3b435d).

| quantity | ts_gsr | ts_demean |
|---|---|---|
| DMT post − pre | −0.0491 [−0.0823, −0.0128], p = 0.0227 | −0.0621 [−0.1055, −0.0130], p = 0.0300 |
| PCB post − pre | +0.0242 [−0.0020, +0.0496], p = 0.1040 | +0.0314 [+0.0013, +0.0585], p = 0.0637 |
| DiD raw | −0.0733 [−0.1180, −0.0291], p = 0.0070; phase-randomised p = 0.0020; 12/14 negative; −6.3 % of baseline | −0.0935 [−0.1431, −0.0426], p = 0.0039; phase-randomised p = 0.0010; 12/14 negative; −8.5 % |
| FD DiD | +0.0191 [−0.0008, +0.0402], p = 0.1083 | same |
| DiD FD-residualised | −0.0555 [−0.0864, −0.0210], p = 0.0100; 13/14 | −0.0714 [−0.1106, −0.0298], p = 0.0073; 12/14 |

W = 30 positive control (`results/primary_b_ts_gsr_win30.csv`, git ac1fdc0), ts_gsr, pre = bins 1–8: primary post bins 11–28, DiD raw −0.0686 [−0.1084, −0.0293], p = 0.0042, phase-randomised p = 0.0010, 13/14 negative, −6.7 % of the W = 30 pre-injection DMT mean of 1.0223; DMT post − pre −0.0390 [−0.0680, −0.0058], p = 0.0354; PCB post − pre +0.0296 [+0.0076, +0.0531], p = 0.0269; FD-residualised −0.0545 [−0.0836, −0.0215], p = 0.0065, 13/14. Sensitivity bins 10–28: DiD −0.0658 [−0.1072, −0.0261], p = 0.0067; residualised −0.0514 [−0.0799, −0.0179], p = 0.0109.

## Table S2. Tier-2 intensity tracking, decay windows, DMT run, W = 60

Source: as Table S1. ρ_S = Spearman correlation. "Group-mean series" is the 14-subject mean sts series vs the group intensity template f (thresholded at |ρ| ≥ 0.80; p vs the phase-randomised null). "Per-subject" is the group mean of per-subject ρ_S vs own ratings (primary) or vs f (sensitivity), tested for existence against the null, not thresholded. Control (a): the within-subject difference ρ_DMT − ρ_PCB (template) must have a CI excluding zero and PCB must be below half of DMT. Control (b): the same three conditions on FD-residualised sts. Sign is negative in every cell against the pre-specified positive direction.

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

## Table S3. Exploratory regional DiD: regions surviving BH FDR (q = 0.05)

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

## Table S4. Exploratory workspace comparison

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

## Table S5. Exploratory receptor-map correlations

Source: `results/regional_analysis_<variant>.csv`. Spearman ρ between the group-mean regional DiD map and receptor density on the 99 cortical parcels; two-sided spin p over 10,000 rotations (Váša one-sided-average p in brackets); BH across the five maps: nothing significant on either variant. The 115-region ρ including subcortex has no spatial null and is descriptive. **Exploratory.**

| map | ts_gsr ρ (p) [Váša p] | 115-region ρ | ts_demean ρ (p) [Váša p] | 115-region ρ |
|---|---|---|---|---|
| 5-HT2A | −0.160 (0.116) [0.070] | −0.230 | −0.055 (0.677) [0.360] | −0.263 |
| 5-HT1A | +0.009 (0.929) [0.467] | −0.099 | +0.265 (0.032) [0.012] | +0.038 |
| 5-HT1B | −0.094 (0.352) [0.185] | −0.144 | −0.263 (0.050) [0.033] | −0.314 |
| 5-HT4 | −0.084 (0.422) [0.228] | +0.008 | +0.182 (0.160) [0.066] | +0.231 |
| 5-HTT | +0.104 (0.324) [0.145] | +0.196 | +0.202 (0.096) [0.039] | +0.365 |

Receptor inter-correlations (Spearman, 115 regions): 1A–2A 0.532, 1B–2A 0.528, 2A–4 0.436, 2A–HTT −0.451, 1A–4 0.405, 1B–HTT −0.364, 1A–HTT −0.100, 4–HTT 0.068, 1B–4 0.056, 1A–1B −0.002.

## Table S6. EEG Lempel-Ziv complexity vs ΦID quantities, global fit, 28 bins

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

## Table S7. Global functional connectivity per bin set

Source: `results/global_fc_did_<variant>.csv` (git 66b570e-dirty). Mean Pearson r over the 6,555 pairs; DiD form as in the main text; the whole-brain sts DiD from the global-fit atoms on the identical bins alongside.

| variant | bin set | mean r DiD [CI], p, neg/pos | sts DiD (nats) [CI], p, neg/pos |
|---|---|---|---|
| ts_demean | primary 11–28 | +0.0526 [+0.0073, +0.0976], 0.0470, 4/10 | −0.1035 [−0.1678, −0.0357], 0.0132, 11/3 |
| ts_demean | sensitivity 9–28 | +0.0532 [+0.0113, +0.0930], 0.0322, 4/10 | −0.0909 [−0.1536, −0.0254], 0.0175, 11/3 |
| ts_demean | peak 9–14 | +0.0746 [+0.0293, +0.1282], 0.0046, 3/11 | −0.0810 [−0.1446, −0.0176], 0.0348, 11/3 |
| ts_gsr | primary 11–28 | −0.0034 [−0.0051, −0.0017], 0.0024, 11/3 | −0.0801 [−0.1303, −0.0310], 0.0071, 12/2 |
| ts_gsr | peak 9–14 | −0.0032 [−0.0050, −0.0015], 0.0023, 12/2 | −0.0752 [−0.1114, −0.0335], 0.0044, 13/1 |

Pre-injection mean r: ts_demean DMT 0.1905, PCB 0.1813; ts_gsr DMT −0.0020, PCB −0.0039 (GSR pins the mean near zero by construction; every ts_gsr bin lies within −0.0058 to −0.0008).
