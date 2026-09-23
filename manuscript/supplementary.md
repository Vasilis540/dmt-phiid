# Supplementary tables

Companion to `manuscript/draft_v2.md`, which cites S1–S8 Tables from its S1 Text (the original pre-specified analysis; `manuscript/draft.md`, which they first accompanied, is kept as a record), S9–S11 Tables from S3 Text, and S12–S18 Tables, which carry material moved from the main text in Stage B of round 16 and the results of B21–B24. Every value is quoted from the named results file. Nats throughout; N = 14; sign-flip p exact over 2^14 assignments, two-sided; the interval of a mean over subjects is the inverted sign-flip 95 % interval of B21 (S17 Table), and the intervals marked "percentile" are subject-bootstrap 95 % percentile intervals (10,000 draws) of quantities with no saved per-subject vector; seed 20261120.

## S1 Table. Step contrast on the sensitivity windows 5–14 (bins 9–28) vs pre-injection windows 1–4, W = 60

Source: `results/primary_b_ts_gsr_win60.csv` (git e46df8a), `results/primary_b_ts_demean_win60.csv` (git f3b435d); the intervals are B21's inverted intervals (S17 Table), where the source files hold percentile intervals.

| quantity | ts_gsr | ts_demean |
|---|---|---|
| DMT post − pre | −0.0491 [−0.0877, −0.0089], p = 0.0227 | −0.0621 [−0.1137, −0.0077], p = 0.0300 |
| PCB post − pre | +0.0242 [−0.0060, +0.0544], p = 0.1040 | +0.0314 [−0.0021, +0.0646], p = 0.0637 |
| DiD raw | −0.0733 [−0.1238, −0.0238], p = 0.0070; phase-randomised p = 0.0020; 12/14 negative; −6.3 % of baseline | −0.0935 [−0.1506, −0.0361], p = 0.0039; phase-randomised p = 0.0010; 12/14 negative; −8.5 % |
| FD DiD | +0.0191 [−0.0050, +0.0434], p = 0.1083 | same |
| DiD FD-residualised | −0.0555 [−0.0909, −0.0174], p = 0.0100; 13/14 | −0.0714 [−0.1170, −0.0237], p = 0.0073; 12/14 |

W = 30 positive control (`results/primary_b_ts_gsr_win30.csv`, git ac1fdc0), ts_gsr, pre = bins 1–8: primary post bins 11–28, DiD raw −0.0686 [−0.1142, −0.0242], p = 0.0042, phase-randomised p = 0.0010, 13/14 negative, −6.7 % of the W = 30 pre-injection DMT mean of 1.0223; DMT post − pre −0.0390 [−0.0727, −0.0034], p = 0.0354; PCB post − pre +0.0296 [+0.0041, +0.0560], p = 0.0269; FD-residualised −0.0545 [−0.0875, −0.0187], p = 0.0065, 13/14. Sensitivity bins 10–28: DiD −0.0658 [−0.1115, −0.0212], p = 0.0067; residualised −0.0514 [−0.0846, −0.0155], p = 0.0109.

## S2 Table. Tier-2 intensity tracking, decay windows, DMT run, W = 60

Source: as S1 Table. ρ_S = Spearman correlation. "Group-mean series" is the 14-subject mean sts series vs the group intensity template f (thresholded at |ρ| ≥ 0.80; p vs the phase-randomised null). "Per-subject" is the group mean of per-subject ρ_S vs own ratings (primary) or vs f (sensitivity), tested for existence against the null, not thresholded. Control (a): the within-subject difference ρ_DMT − ρ_PCB (template) must have a CI excluding zero and PCB must be below half of DMT. Control (b): the same three conditions on FD-residualised sts. Sign is negative in every cell against the pre-specified positive direction. The intervals are subject-bootstrap percentile intervals: `scripts/06_primary_b_analysis.py` writes the group means only, and the ratings are in the data clone, so no per-subject vector is saved.

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

## S3 Table. Exploratory regional DiD: regions passing BH FDR (q = 0.05)

Source: `results/regional_analysis_<variant>.csv`, `results/regional_did_map_<variant>.csv` (git 4f7437b). Global fit; pre bins 1–8, post bins 11–28; group-mean DiD negative in 114 of 115 regions on both variants; the one positive region is subcortical parcel 104 (+0.028, p = 0.495 on ts_gsr; +0.019, p = 0.566 on ts_demean). BH thresholds: p = 0.00304 (ts_gsr, 7 regions), 0.00826 (ts_demean, 19 regions). All of them negative and cortical. **Exploratory.**

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

Source: `results/regional_analysis_<variant>.csv`. Per-subject mean regional DiD inside the proxy minus outside it (negative = larger decrease inside). Primary proxy = Yeo Default ∪ Control (37 cortical parcels; gateway proxy = Default 24, broadcaster proxy = Control 13); named-subregion proxy = 26 parcels (gateway 21, broadcaster 5). Non-workspace = remaining cortical parcels, or remaining cortical + 16 subcortical ("+ subcortex"). The intervals are subject-bootstrap percentile intervals (`scripts/11_regional_analysis.py` writes the group values only). **Exploratory.**

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

Source: `results/regional_analysis_<variant>.csv`. Spearman ρ between the group-mean regional DiD map and receptor density on the 99 cortical parcels; two-sided spin p over 10,000 parcel rotations (the spin test of Alexander-Bloch et al., 2018, with the rotations of Váša et al., 2018, released with the data; Váša one-sided-average p in brackets); BH across the five maps: no map passes on either variant. The 115-region ρ including subcortex has no spatial null and is descriptive. **Exploratory.** The same spin test applied to the regional sts–r₁ correlations of the main text's Results 3 (placebo run, pre-injection; `notes/review_results/partB/regional_sts_r1_tables.md`): sts against windowed regional r₁, Spearman ρ = +0.771 on the 99 cortical parcels, spin p < 0.0001 (Váša p < 0.0001; null SD 0.131); sts − rtr, ρ = +0.618, spin p < 0.0001; rtr, ρ = +0.504, spin p = 0.0002 (Váša p = 0.0002); against whole-span r₁, ρ = +0.827, +0.672 and +0.494 with spin p < 0.0001, < 0.0001 and 0.0003. The partialled map's correlation with regional r₁, zero by construction, is not spin-tested; its network structure was spin-tested by B22 (e) (S3 Text, section 4).

| map | ts_gsr ρ (p) [Váša p] | 115-region ρ | ts_demean ρ (p) [Váša p] | 115-region ρ |
|---|---|---|---|---|
| 5-HT2A | −0.160 (0.116) [0.070] | −0.230 | −0.055 (0.677) [0.360] | −0.263 |
| 5-HT1A | +0.009 (0.929) [0.467] | −0.099 | +0.265 (0.032) [0.012] | +0.038 |
| 5-HT1B | −0.094 (0.352) [0.185] | −0.144 | −0.263 (0.050) [0.033] | −0.314 |
| 5-HT4 | −0.084 (0.422) [0.228] | +0.008 | +0.182 (0.160) [0.066] | +0.231 |
| 5-HTT | +0.104 (0.324) [0.145] | +0.196 | +0.202 (0.096) [0.039] | +0.365 |

Receptor inter-correlations (Spearman, 115 regions): 1A–2A 0.532, 1B–2A 0.528, 2A–4 0.436, 2A–HTT −0.451, 1A–4 0.405, 1B–HTT −0.364, 1A–HTT −0.100, 4–HTT 0.068, 1B–4 0.056, 1A–1B −0.002.

## S6 Table. EEG Lempel-Ziv complexity vs ΦID quantities, global fit, 28 bins

Source: `results/lz_vs_tdmi_<variant>.csv` (git 84ea657). Per-subject Spearman ρ across the 28 bins, group mean with subject-bootstrap percentile CI (no per-subject vector is saved); p against 1,000 phase-randomised surrogates of the LZ series (one-sided in the predicted direction; two-sided in brackets); "series" = ρ of the group-mean series with its two-sided p.

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

Source: `results/global_fc_did_<variant>.csv` (git 66b570e-dirty). Mean Pearson r over the 6,555 pairs; DiD form as in the main text; the whole-brain sts DiD from the global-fit atoms on the identical bins alongside; intervals inverted (B21).

| variant | bin set | mean r DiD [CI], p, neg/pos | sts DiD (nats) [CI], p, neg/pos |
|---|---|---|---|
| ts_demean | primary 11–28 | +0.0526 [+0.0008, +0.1041], 0.0470, 4/10 | −0.1035 [−0.1784, −0.0267], 0.0132, 11/3 |
| ts_demean | sensitivity 9–28 | +0.0532 [+0.0059, +0.1000], 0.0322, 4/10 | −0.0909 [−0.1640, −0.0169], 0.0175, 11/3 |
| ts_demean | peak 9–14 | +0.0746 [+0.0232, +0.1314], 0.0046, 3/11 | −0.0810 [−0.1545, −0.0068], 0.0348, 11/3 |
| ts_gsr | primary 11–28 | −0.0034 [−0.0053, −0.0014], 0.0024, 11/3 | −0.0801 [−0.1362, −0.0251], 0.0071, 12/2 |
| ts_gsr | peak 9–14 | −0.0032 [−0.0053, −0.0012], 0.0023, 12/2 | −0.0752 [−0.1162, −0.0303], 0.0044, 13/1 |

Pre-injection mean r: ts_demean DMT 0.1905, PCB 0.1813; ts_gsr DMT −0.0020, PCB −0.0039 (GSR pins the mean near zero by construction; every ts_gsr bin lies within −0.0058 to −0.0008).

## S8 Table. Post-hoc proportionality: sts / TDMI ratio DiD, four cells

Source: `results/proportionality.csv` (script `14_proportionality.py` at git dbf2311; interpretation rule recorded in the script docstring and in the project orientation file before the run). Post-hoc, specified after the primary result, reported regardless of outcome. Ratio = sts / TDMI (TDMI = Σ 16 atoms) per subject, condition and window (W = 60) or bin (global fit); DiD = (post − pre)_DMT − (post − pre)_PCB on the mean ratio over the window set; exact sign-flip p over 2^14 assignments, two-sided; the inverted sign-flip 95 % interval (B21; S17 Table). Windows: W = 60, pre 1–4, post 6–14; global fit, pre bins 1–8, post 11–28. Verdict by the pre-recorded rule, which was stated for the bootstrap CI (the inverted intervals give the same four verdicts): interval includes zero → proportional; interval below zero → more than proportional; interval above zero → less than proportional. (i) = sts share of TDMI at pre-injection baseline on the DMT run (subject mean, with CI); (ii) = sts DiD / TDMI DiD on the group means, with a subject-bootstrap percentile CI of the ratio of means (a ratio of group means, not a mean over subjects). (i) and (ii) are comparable within a cell, not across estimators: the windowed and global fits give different baseline shares because per-window finite-sample bias falls on sts and on the self-transfer atoms. No temporal null, no motion handling.

| estimator | variant | ratio DiD [CI], p, neg/14 | verdict | (i) baseline share [CI] | (ii) share of TDMI DiD [CI] | sts DiD (nats) | TDMI DiD (nats) |
|---|---|---|---|---|---|---|---|
| windowed W = 60 | ts_gsr | +0.0005 [−0.0091, +0.0096], 0.9138, 6 | proportional | 0.7820 [0.7775, 0.7864] | 0.7797 [0.6531, 0.9362] | −0.0809 [−0.1317, −0.0310] | −0.1037 [−0.1671, −0.0410] |
| windowed W = 60 | ts_demean | −0.0095 [−0.0255, +0.0067], 0.2195, 9 | proportional | 0.7670 [0.7579, 0.7760] | 0.8697 [0.6909, 1.0063] | −0.1031 [−0.1629, −0.0435] | −0.1186 [−0.1785, −0.0596] |
| global fit | ts_gsr | +0.0204 [+0.0032, +0.0380], 0.0248, 4 | less than proportional | 0.9082 [0.8983, 0.9180] | 0.6584 [0.4864, 0.8174] | −0.0801 [−0.1362, −0.0251] | −0.1216 [−0.1998, −0.0439] |
| global fit | ts_demean | +0.0071 [−0.0197, +0.0334], 0.5623, 5 | proportional | 0.8967 [0.8841, 0.9092] | 0.7867 [0.5004, 1.0127] | −0.1035 [−0.1784, −0.0267] | −0.1315 [−0.2104, −0.0524] |

Within-condition ratio changes (post − pre): windowed ts_gsr DMT +0.0034 [−0.0009, +0.0077], p = 0.1097, PCB +0.0028 [−0.0038, +0.0098], p = 0.3990; windowed ts_demean DMT −0.0093 [−0.0231, +0.0039], p = 0.1621, PCB +0.0001 [−0.0081, +0.0085], p = 0.9712; global ts_gsr DMT +0.0167 [+0.0035, +0.0299], p = 0.0183, PCB −0.0037 [−0.0127, +0.0054], p = 0.3949; global ts_demean DMT +0.0015 [−0.0208, +0.0239], p = 0.8799, PCB −0.0056 [−0.0156, +0.0050], p = 0.2753. The sts DiD reproduces Table 2 of `draft_v2.md` and the TDMI DiD its Table 1, and both reproduce `results/windowed_atoms_did_ts_gsr_win60.csv`; the intervals are the inverted intervals the main text reports. On the symmetric family, under a common change of r₁ at the operating point (0.85, 0.25), sts carries 0.99 of the change in TDMI against a baseline share of 0.98 (closed form, TDMI = 2S and sts = 2S − C; main text, Results 1); unequal changes of a_x and a_y move that share. The less-than-proportional cell (the global fit on ts_gsr: sts carried 0.66 of the TDMI drop against a baseline share of 0.91) is not explained here (moved from the main text's Results 2).

## S9 Table. The cross-lag budget (S3 Text, section 6): data, finite-sample null, null-corrected terms and shares; the controls; the superseded values of 16 September 2026, 10:32 UTC

Source: `notes/review_results/partB/crosslag_budget_tables.md` (data; `partB12_crosslag_budget.py`) and `crosslag_budget_null_tables.md` (null, controls, null-corrected budget and the reading under the rules; `partB13_crosslag_budget_null.py`), both at git 6b5181a, seed 20261120; definitions in Methods and `notes/rev_crosslag_budget.py`; the rules in the record's pre-run entry of 16 September 2026, 16:24 UTC, and the outcome of 16:37 UTC. Terms per subject and run are means over the 6,555 pairs, s = the sign of the pair's run-level q; grand mean = mean over subjects of the per-subject mean of the two runs, with the inverted sign-flip 95 % interval (B21; the ts_demean grand-mean δ_run interval [−0.00528, +0.00006], p = 0.053, includes zero, where the committed percentile interval did not); the null value is the mean over the two run types of ≥ 25,000 simulated pair-runs each (Monte-Carlo SE in parentheses); the null-corrected value is data minus null with the data interval shifted; the range is over the six null configurations (0 primary: heterogeneity 0.5, DMT-post/placebo ACF, mixture q solved to the run-level a, |q̂| and fraction |q̂| < 0.05; 1 heterogeneity 0.25; 2 heterogeneity 1.0; 3 placebo ACF for both run types; 4 Gaussian q; 5 mixture solved to the W = 60 window-level means). Identity (by construction): δ_run = δ_within + δ_pool + δ_means + ε, to 6.9 × 10⁻¹⁸. Nats-free (correlation units).

| ts_gsr | δ_run | δ_within | δ_pool | δ_means | ε | δ_60 (run-level sign) | window-sign value |
|---|---|---|---|---|---|---|---|
| data, grand mean [CI] | +0.00340 [+0.00294, +0.00386] | +0.00291 [+0.00252, +0.00330] | +0.00050 [+0.00036, +0.00063] | +0.00001 [+0.00000, +0.00003] | −0.00002 [−0.00004, +0.00001] | +0.00245 [+0.00205, +0.00285] | +0.00611 [+0.00552, +0.00671] |
| data, DMT run [CI] | +0.00381 [+0.00332, +0.00429] | +0.00310 [+0.00273, +0.00347] | +0.00069 [+0.00050, +0.00088] | +0.00002 [+0.00000, +0.00005] | −0.00000 [−0.00005, +0.00005] | +0.00264 [+0.00222, +0.00306] | +0.00615 [+0.00568, +0.00663] |
| data, placebo run [CI] | +0.00299 [+0.00225, +0.00373] | +0.00272 [+0.00207, +0.00336] | +0.00030 [+0.00017, +0.00044] | +0.00000 [−0.00002, +0.00003] | −0.00003 [−0.00005, −0.00001] | +0.00226 [+0.00162, +0.00289] | +0.00608 [+0.00522, +0.00695] |
| null, primary configuration (SE) | +0.00039 (0.00003) | +0.00040 (0.00003) | +0.00003 (0.00001) | −0.00002 (0.00000) | −0.00002 (0.00000) | +0.00017 (0.00003) | +0.00352 (0.00003) |
| null, primary, DMT type / placebo type | +0.00031 / +0.00047 | +0.00034 / +0.00047 | +0.00003 / +0.00004 | −0.00004 / −0.00001 | −0.00002 / −0.00002 | +0.00013 / +0.00022 | +0.00330 / +0.00373 |
| null, range over configurations 0–5 | +0.00029 to +0.00046 | +0.00031 to +0.00044 | +0.00002 to +0.00005 | −0.00002 to −0.00001 | −0.00002 to −0.00002 | +0.00007 to +0.00021 | +0.00332 to +0.00364 |
| null-corrected, primary [CI] | +0.00301 [+0.00255, +0.00347] | +0.00250 [+0.00211, +0.00289] | +0.00046 [+0.00033, +0.00060] | +0.00004 [+0.00002, +0.00005] | +0.00000 [−0.00002, +0.00003] | +0.00228 [+0.00188, +0.00268] | +0.00259 [+0.00201, +0.00319] |
| null-corrected, range | +0.00294 to +0.00311 | +0.00247 to +0.00260 | +0.00045 to +0.00048 | +0.00002 to +0.00004 | −0.00000 to +0.00001 | +0.00224 to +0.00238 | +0.00247 to +0.00279 |
| share of δ_run,c, primary (range) | — | 0.833 (0.833–0.839) | 0.154 (0.152–0.155) | 0.012 (0.007–0.012) | 0.001 (−0.000 to 0.002) | — | — |
| label under rule (b), the same in every configuration | — | most | a minor part | a minor part | — | — | — |

| ts_demean (no null; not read) | δ_run | δ_within | δ_pool | δ_means | ε | δ_60 (run-level sign) | window-sign value |
|---|---|---|---|---|---|---|---|
| data, grand mean [CI] | −0.00262 [−0.00528, +0.00006] | −0.00226 [−0.00455, +0.00005] | −0.00030 [−0.00071, +0.00007] | +0.00000 [−0.00002, +0.00002] | −0.00005 [−0.00012, +0.00001] | −0.00274 [−0.00505, −0.00041] | +0.00160 [−0.00040, +0.00367] |
| data, DMT run [CI] | −0.00324 [−0.00638, −0.00036] | −0.00270 [−0.00518, −0.00036] | −0.00047 [−0.00124, +0.00020] | −0.00000 [−0.00003, +0.00004] | −0.00007 [−0.00014, +0.00000] | −0.00313 [−0.00568, −0.00073] | +0.00108 [−0.00112, +0.00318] |
| data, placebo run [CI] | −0.00199 [−0.00493, +0.00089] | −0.00182 [−0.00445, +0.00077] | −0.00014 [−0.00042, +0.00013] | +0.00000 [−0.00002, +0.00002] | −0.00004 [−0.00015, +0.00007] | −0.00235 [−0.00501, +0.00026] | +0.00212 [−0.00011, +0.00430] |

| controls (primary parameters; mean over run types) | δ_run | δ_within | δ_pool | δ_means | ε | shares within / pool / means / ε |
|---|---|---|---|---|---|---|
| (i) common drive: λ = 0.2, a_s − a_n = 0.10 (population d = +0.01600) | +0.01438 | +0.01291 | +0.00129 | +0.00027 | −0.00010 | 0.898 / 0.090 / 0.019 / −0.007 |
| (ii) pooling: q and filter change at TR 240 (β₁ ~ N(6β̄, h·6β̄), β₂ ~ N(β̄/5, h·β̄/5), q₂ = q₁(1 − g), g ~ U(0.5, 1); δ_pool at 49 and 44 Monte-Carlo SEs) | +0.00131 | +0.00040 | +0.00095 | −0.00002 | −0.00001 | 0.303 / 0.723 / −0.015 / −0.011 |

Rule (e), the per-subject difference DMT − placebo, null-corrected at the primary configuration: δ_pool,c +0.00039 (exact sign-flip p = 0.0006, positive in 12 of 14; +0.00037 to +0.00041, p ≤ 0.0007, in the other configurations), 0.11 of the DMT-run δ_run,c (+0.00349) — "pooling is larger on the DMT run"; δ_within,c +0.00052 (p = 0.1368) and δ_means,c +0.00005 (p = 0.0112), reported with no rule. Reading under rules (a)–(f), the same in every configuration: finite sampling a minor part (F = δ_run,null / δ_run from 0.085 to 0.135); the within-window term most, pooling and the window means a minor part each; the null's q distribution is symmetric (fraction q̂ < 0 0.50) where the data's has 0.545 of pairs below zero.

Superseded values of 16 September 2026, 10:32 UTC (`crosslag_deviation_tables.md`, sections A and B at git 9a19b10; record, correction note of 16 September, 16:24 UTC), reported here and no longer read: at W = 60 with the sign of each window's own q, `ts_gsr` +0.00611 [+0.00552, +0.00671] (DMT +0.00615, placebo +0.00608; slope of the deviation on q +0.0201) and `ts_demean` +0.00160 [−0.00040, +0.00367]; the finite-sample null with the same weight, homogeneous filter, +0.00348 at W = 60 (the four operating-point cells +0.00344, +0.00311, +0.00325, +0.00356) and +0.00662 at W = 30; the same null's run-level value +0.00025 ± 0.00005 at W = 840 (mean |q̂| 0.222 against the data's 0.1945). The readings drawn from them — "near zero: finite sampling removed" and "comparable to the run-level value (1.80 raw, 0.77–0.81 net): a stationary mechanism rather than pooling" — are superseded because the window's sign selects on the same samples as the deviation (about half of +0.00611 is that selection: the null's +0.00348), the null's run-level value was read at a different density of q̂ near zero (the null solved to the data gives +0.00029 to +0.00046), and the ratio compared two differently biased statistics without computing pooling; the budget above computes it.

Earlier values of the same statistic, removed from Results 4 in the revision of 16 September and kept here (record, 15 September 2026, 15:36 and 18:18 UTC, and 16 September, 10:32 UTC; `crosslag_deviation_tables.md`): the signed mean over pairs, `ts_gsr` +0.00009 [+0.00004, +0.00014] (sign-flip p = 0.0004, positive in 13 of 14; pair-level SD of the deviation 0.0390) and `ts_demean` −0.00738 [−0.00920, −0.00563] (p = 0.0001, negative in 14 of 14), which on `ts_gsr` cancels between the 54.5 % of pairs with q < 0 (mean deviation −0.00304) and the pairs with q > 0 (+0.00384); the correlation across the 28 runs of the run-level statistic with the run-level residual, −0.767 (sign(q)-weighted) against −0.277 (signed) on `ts_gsr` and −0.969 against −0.890 on `ts_demean`; the slope of the deviation on q across pairs, +0.0163 [+0.0137, +0.0190] at the run level and +0.0201 [+0.0180, +0.0223] at W = 60 on `ts_gsr`, +0.0211 [+0.0191, +0.0230] and +0.0237 [+0.0216, +0.0258] on `ts_demean`; on `ts_demean` the run-level sign(q)-weighted mean −0.00262 (sign-flip p = 0.0532, positive in 5 of 14; −0.00582 among the q > 0 pairs, −0.01441 among the q < 0 pairs) and the W = 60 window-sign value +0.00160 (p = 0.1061); and the family-scale conversion at the operating point (0.85, 0.25), where a deviation of +0.006 gives a residual of −0.0103, +0.0034 gives −0.0061 (44 % of the observed −0.0137) and, at the pairs' mean run-level a and |q| (0.8666, 0.1945), −0.0051 (37 %).


## S10 Table. Calibration of the residual diagnostic at both estimators: the AR(1) generator and the band-passed generator

Source: `notes/review_results/partB/calibration_tables.md` (B17; record, pre-run entry 20 Sep 2026, outcome 21 Sep 2026) and `calibration_filtered_tables.md` (B17b; pre-run entry 21 Sep 2026). N_PAIRS = 300 per subject, 14 subjects × 2 runs × 840 samples, the change from sample 300 of the DMT run only, 50 replicates per condition (± is the SD over replicates); DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo. At the global fit two AR(1)-substituted estimates are tabulated: the pipeline's run-level one (constant across a run's bins, so its DiD is zero and the residual DiD equals the observed DiD) and a period-level one from (a_x, a_y, q) measured on the pre and the post samples separately. "residual p" is the exact sign-flip p of the residual DiD against zero (mean over replicates; share of replicates below 0.05): that a test against zero tests the wrong null, since a pure autocorrelation change moves the residual's expectation away from zero, is what the calibration establishes (main text, Results 4). The coupling rows calibrate one construction of coupling, the VAR(1) cross-coefficient with the innovations held; B23 gives the others (S18 Table). AR(1) generator: a_x, a_y ~ N(0.85, 0.0125); q from the data's window-level pool; Δa = −0.015 in population; coupling as a VAR(1) cross-coefficient.

| condition | estimator | sts level (pre) | sts DiD | AR(1)-substituted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |
|---|---|---|---|---|---|---|---|---|
| (i) Δa = −0.015, Δc = 0 | W60 | 0.7152 | -0.0422 ± 0.0034 | -0.0471 ± 0.0036 | +0.0049 ± 0.0017 | 0.056; 0.82 | +0.00014 ± 0.00065 | +0.00130 ± 0.00050 |
| (i) Δa = −0.015, Δc = 0 | global (run-level substitution) | 1.1317 | -0.0675 ± 0.0058 | -0.0000 ± 0.0000 | -0.0675 ± 0.0058 | 0.000; 1.00 | — | — |
| (i) Δa = −0.015, Δc = 0 | global (period-level substitution) | 1.1317 | -0.0675 ± 0.0058 | -0.0764 ± 0.0048 | +0.0089 ± 0.0028 | 0.046; 0.62 | — | — |
| (ii) Δc = +0.01 | W60 | 0.7153 | +0.0010 ± 0.0036 | +0.0020 ± 0.0037 | -0.0010 ± 0.0018 | 0.460; 0.08 | +0.00758 ± 0.00072 | -0.00014 ± 0.00065 |
| (ii) Δc = +0.01 | global (run-level substitution) | 1.1390 | +0.0003 ± 0.0049 | -0.0000 ± 0.0000 | +0.0003 ± 0.0049 | 0.537; 0.04 | — | — |
| (ii) Δc = +0.01 | global (period-level substitution) | 1.1390 | +0.0003 ± 0.0049 | +0.0028 ± 0.0040 | -0.0025 ± 0.0027 | 0.461; 0.12 | — | — |
| (ii) Δc = +0.02 | W60 | 0.7154 | +0.0002 ± 0.0039 | +0.0053 ± 0.0037 | -0.0052 ± 0.0016 | 0.055; 0.76 | +0.01480 ± 0.00069 | -0.00037 ± 0.00063 |
| (ii) Δc = +0.02 | global (run-level substitution) | 1.1446 | -0.0033 ± 0.0050 | -0.0000 ± 0.0000 | -0.0033 ± 0.0050 | 0.403; 0.14 | — | — |
| (ii) Δc = +0.02 | global (period-level substitution) | 1.1446 | -0.0033 ± 0.0050 | +0.0092 ± 0.0039 | -0.0124 ± 0.0029 | 0.010; 0.92 | — | — |
| (ii) Δc = +0.03 | W60 | 0.7152 | +0.0001 ± 0.0031 | +0.0110 ± 0.0034 | -0.0109 ± 0.0017 | 0.001; 1.00 | +0.02210 ± 0.00071 | -0.00083 ± 0.00055 |
| (ii) Δc = +0.03 | global (run-level substitution) | 1.1512 | -0.0080 ± 0.0037 | -0.0000 ± 0.0000 | -0.0080 ± 0.0037 | 0.206; 0.26 | — | — |
| (ii) Δc = +0.03 | global (period-level substitution) | 1.1512 | -0.0080 ± 0.0037 | +0.0198 ± 0.0035 | -0.0278 ± 0.0027 | 0.000; 1.00 | — | — |
| (ii) Δc = −0.02 | W60 | 0.7152 | -0.0002 ± 0.0038 | +0.0053 ± 0.0037 | -0.0055 ± 0.0018 | 0.039; 0.80 | -0.01495 ± 0.00066 | -0.00027 ± 0.00059 |
| (ii) Δc = −0.02 | global (run-level substitution) | 1.1438 | -0.0045 ± 0.0050 | +0.0000 ± 0.0000 | -0.0045 ± 0.0050 | 0.408; 0.14 | — | — |
| (ii) Δc = −0.02 | global (period-level substitution) | 1.1438 | -0.0045 ± 0.0050 | +0.0089 ± 0.0041 | -0.0134 ± 0.0033 | 0.009; 0.94 | — | — |
| (iii) Δa = −0.015, Δc = +0.02 | W60 | 0.7153 | -0.0419 ± 0.0035 | -0.0427 ± 0.0033 | +0.0009 ± 0.0016 | 0.521; 0.00 | +0.01500 ± 0.00080 | +0.00093 ± 0.00056 |
| (iii) Δa = −0.015, Δc = +0.02 | global (run-level substitution) | 1.1364 | -0.0694 ± 0.0049 | -0.0000 ± 0.0000 | -0.0694 ± 0.0049 | 0.000; 1.00 | — | — |
| (iii) Δa = −0.015, Δc = +0.02 | global (period-level substitution) | 1.1364 | -0.0694 ± 0.0049 | -0.0687 ± 0.0040 | -0.0006 ± 0.0035 | 0.525; 0.10 | — | — |
| (iv) a_x − a_y = 0.03, Δa = −0.015 | W60 | 0.7131 | -0.0422 ± 0.0036 | -0.0473 ± 0.0038 | +0.0051 ± 0.0018 | 0.052; 0.72 | +0.00013 ± 0.00071 | +0.00130 ± 0.00056 |
| (iv) a_x − a_y = 0.03, Δa = −0.015 | global (run-level substitution) | 1.1127 | -0.0677 ± 0.0046 | +0.0000 ± 0.0000 | -0.0677 ± 0.0046 | 0.000; 1.00 | — | — |
| (iv) a_x − a_y = 0.03, Δa = −0.015 | global (period-level substitution) | 1.1127 | -0.0677 ± 0.0046 | -0.0746 ± 0.0045 | +0.0069 ± 0.0030 | 0.114; 0.64 | — | — |

Band-passed generator (the same conditions on series with the data's spectrum and window-level operating point; the (ii) rows read by their δ_sym DiD, not by c, because this construction injects about a thirtieth of the AR(1) generator's lagged structure at the same c). Source: `notes/review_results/partB/calibration_filtered_tables.md` and `calibration_filtered.csv` (B17b; record, pre-run entry 21 Sep 2026, outcome 21 Sep 2026). The generator was solved once and held fixed at β̄ = 185.4, σ_q = 0.2637, β̄_post = 105.7 and δ = 82.6, giving a realised window-level mean a of 0.8637, mean |q| 0.2844, post-injection a 0.8483 and a_x − a_y 0.0300.

| condition | estimator | sts level (pre) | sts DiD | AR(1)-substituted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |
|---|---|---|---|---|---|---|---|---|
| (i) Δa (post filter) | W60 | 1.1883 | -0.0940 ± 0.0028 | -0.0966 ± 0.0027 | +0.0027 ± 0.0014 | 0.136; 0.54 | -0.00005 ± 0.00030 | +0.00641 ± 0.00104 |
| (i) Δa (post filter) | global (run-level substitution) | 1.3262 | -0.1046 ± 0.0035 | +0.0000 ± 0.0000 | -0.1046 ± 0.0035 | 0.000; 1.00 | — | — |
| (i) Δa (post filter) | global (period-level substitution) | 1.3262 | -0.1046 ± 0.0035 | -0.1089 ± 0.0030 | +0.0043 ± 0.0020 | 0.116; 0.62 | — | — |
| (ii) Δc = +0.01 | W60 | 1.1878 | +0.0001 ± 0.0029 | -0.0002 ± 0.0025 | +0.0003 ± 0.0011 | 0.464; 0.04 | +0.00025 ± 0.00031 | -0.00021 ± 0.00096 |
| (ii) Δc = +0.01 | global (run-level substitution) | 1.3349 | -0.0003 ± 0.0034 | -0.0000 ± 0.0000 | -0.0003 ± 0.0034 | 0.494; 0.08 | — | — |
| (ii) Δc = +0.01 | global (period-level substitution) | 1.3349 | -0.0003 ± 0.0034 | -0.0002 ± 0.0024 | -0.0002 ± 0.0021 | 0.459; 0.06 | — | — |
| (ii) Δc = +0.02 | W60 | 1.1878 | +0.0002 ± 0.0025 | +0.0004 ± 0.0026 | -0.0002 ± 0.0012 | 0.517; 0.04 | +0.00045 ± 0.00024 | -0.00002 ± 0.00103 |
| (ii) Δc = +0.02 | global (run-level substitution) | 1.3353 | -0.0001 ± 0.0034 | +0.0000 ± 0.0000 | -0.0001 ± 0.0034 | 0.569; 0.02 | — | — |
| (ii) Δc = +0.02 | global (period-level substitution) | 1.3353 | -0.0001 ± 0.0034 | -0.0000 ± 0.0028 | -0.0001 ± 0.0020 | 0.477; 0.04 | — | — |
| (ii) Δc = +0.03 | W60 | 1.1883 | -0.0009 ± 0.0028 | -0.0005 ± 0.0026 | -0.0004 ± 0.0012 | 0.453; 0.06 | +0.00069 ± 0.00024 | -0.00018 ± 0.00096 |
| (ii) Δc = +0.03 | global (run-level substitution) | 1.3361 | -0.0010 ± 0.0041 | -0.0000 ± 0.0000 | -0.0010 ± 0.0041 | 0.440; 0.16 | — | — |
| (ii) Δc = +0.03 | global (period-level substitution) | 1.3361 | -0.0010 ± 0.0041 | -0.0005 ± 0.0028 | -0.0005 ± 0.0022 | 0.390; 0.08 | — | — |
| (ii) Δc = −0.02 | W60 | 1.1879 | -0.0002 ± 0.0026 | +0.0000 ± 0.0024 | -0.0002 ± 0.0012 | 0.469; 0.04 | -0.00044 ± 0.00030 | +0.00019 ± 0.00077 |
| (ii) Δc = −0.02 | global (run-level substitution) | 1.3354 | -0.0004 ± 0.0039 | -0.0000 ± 0.0000 | -0.0004 ± 0.0039 | 0.422; 0.14 | — | — |
| (ii) Δc = −0.02 | global (period-level substitution) | 1.3354 | -0.0004 ± 0.0039 | -0.0004 ± 0.0027 | -0.0000 ± 0.0019 | 0.518; 0.04 | — | — |
| (iii) Δa and Δc = +0.02 | W60 | 1.1875 | -0.0944 ± 0.0026 | -0.0971 ± 0.0026 | +0.0027 ± 0.0011 | 0.115; 0.50 | +0.00060 ± 0.00031 | +0.00645 ± 0.00092 |
| (iii) Δa and Δc = +0.02 | global (run-level substitution) | 1.3255 | -0.1055 ± 0.0028 | +0.0000 ± 0.0000 | -0.1055 ± 0.0028 | 0.000; 1.00 | — | — |
| (iii) Δa and Δc = +0.02 | global (period-level substitution) | 1.3255 | -0.1055 ± 0.0028 | -0.1091 ± 0.0024 | +0.0036 ± 0.0014 | 0.132; 0.44 | — | — |
| (iv) a_x − a_y = 0.03 with Δa | W60 | 1.1668 | -0.0889 ± 0.0026 | -0.0920 ± 0.0027 | +0.0031 ± 0.0012 | 0.064; 0.62 | -0.00002 ± 0.00028 | +0.00592 ± 0.00108 |
| (iv) a_x − a_y = 0.03 with Δa | global (run-level substitution) | 1.2526 | -0.0913 ± 0.0028 | -0.0000 ± 0.0000 | -0.0913 ± 0.0028 | 0.000; 1.00 | — | — |
| (iv) a_x − a_y = 0.03 with Δa | global (period-level substitution) | 1.2526 | -0.0913 ± 0.0028 | -0.1014 ± 0.0028 | +0.0101 ± 0.0016 | 0.001; 1.00 | — | — |

Population reference for the AR(1) conditions (closed form at the drawn (a_x, a_y, q); 20,000 draws of B17's distributions and its q pool):

| condition | population sts, pre | population sts, post | population change | B17 W60 level (pre) | B17 W60 sts DiD | B17 global level (pre) | B17 global sts DiD |
|---|---|---|---|---|---|---|---|
| (i) | 1.1936 | 1.1121 | -0.0816 | 0.7152 | -0.0422 | 1.1317 | -0.0675 |
| (iv) | 1.1474 | 1.0699 | -0.0775 | 0.7131 | -0.0422 | 1.1127 | -0.0677 |
| (iv) − (i), pre level | -0.0463 | — | — | -0.0021 | — | -0.0190 | — |

Note. The residual DiD under a pure autocorrelation change is +0.0027 ± 0.0014 on the band-passed generator against +0.0049 ± 0.0017 on AR(1) pairs; the main text quotes both. The window-level change of pair-level a under (i) is −0.01540 ± 0.00035 on the band-passed generator (B24) and −0.01243 ± 0.00101 on AR(1) pairs (B23 (e)); the band-passed generator's population change is Δr₁ = −0.01629 and Δsts = −0.11263 (B23 (e); S13 Table). At the global fit with a period-level AR(1)-substituted estimate, condition (iv) leaves +0.0101 ± 0.0016 with a sign-flip p below 0.05 in every replicate, so the global-fit residual is not a safe read when the pairs are asymmetric.

## S11 Table. The prewhitening check and the whitened series' spectrum

Source: `notes/review_results/inference_rows_prewhiten.csv` and `partB/prewhiten_tables.md` (B16; record, pre-run entry 20 Sep 2026, outcome 21 Sep 2026); `partB/whitened_spectrum_tables.md` (B16b; pre-run entry 21 Sep 2026). Each region's series replaced, per run, by the residuals of its own AR(p) fit by ordinary least squares, the first p TRs dropped (p by BIC over 1–5, which chose p = 5 for 3,218 of the 3,220 region × run series on ts_gsr and 3,215 on ts_demean), or of its AR(1) fit; the atoms, the diagnostic and the DMT contrast recomputed unchanged with the primary inference. "Lag-1 autocorrelation of the whitened series" is `rev_series.autocorr_series` in window mode at W = 60 and, at the global fit, in run mode (the series standardised over the whole run and the lag-1 products averaged within 30-TR bins, a quantity that can exceed 1). **A remedy check, not a finding about DMT.**

| whitening | variant | estimator | quantity | DMT pre-injection level | DiD [inverted 95 % interval] | sign-flip p | negative/14 |
|---|---|---|---|---|---|---|---|
| AR(p), p by BIC in 1–5 | ts_gsr | W = 60 | MMI-sts | 0.2202 | −0.0262 [−0.0636, +0.0107] | 0.1406 | 8 |
| AR(p), p by BIC in 1–5 | ts_gsr | W = 60 | CCS-sts (`phyid`'s mask) | 0.0159 | −0.0135 [−0.0230, −0.0034] | 0.0160 | 11 |
| AR(p), p by BIC in 1–5 | ts_gsr | W = 60 | lag-1 autocorrelation of the whitened series | 0.2625 | −0.0544 [−0.1077, +0.0006] | 0.0520 | 12 |
| AR(p), p by BIC in 1–5 | ts_gsr | global fit | MMI-sts | 0.1042 | −0.0264 [−0.0771, +0.0237] | 0.2736 | 8 |
| AR(p), p by BIC in 1–5 | ts_gsr | global fit | CCS-sts (`phyid`'s mask) | −0.0030 | −0.0045 [−0.0129, +0.0039] | 0.2610 | 7 |
| AR(p), p by BIC in 1–5 | ts_gsr | global fit | lag-1 autocorrelation of the whitened series (run-standardised bins) | 0.2831 | −0.2044 [−0.3062, −0.1062] | 0.0006 | 13 |
| AR(p), p by BIC in 1–5 | ts_demean | W = 60 | MMI-sts | 0.2350 | −0.0274 [−0.0682, +0.0136] | 0.1654 | 9 |
| AR(p), p by BIC in 1–5 | ts_demean | W = 60 | CCS-sts (`phyid`'s mask) | 0.0324 | −0.0168 [−0.0365, +0.0043] | 0.1073 | 10 |
| AR(p), p by BIC in 1–5 | ts_demean | W = 60 | lag-1 autocorrelation of the whitened series | 0.2583 | −0.0418 [−0.1318, +0.0434] | 0.3459 | 9 |
| AR(p), p by BIC in 1–5 | ts_demean | global fit | MMI-sts | 0.1306 | −0.0264 [−0.0770, +0.0228] | 0.2831 | 8 |
| AR(p), p by BIC in 1–5 | ts_demean | global fit | CCS-sts (`phyid`'s mask) | 0.0171 | −0.0028 [−0.0154, +0.0100] | 0.6385 | 7 |
| AR(p), p by BIC in 1–5 | ts_demean | global fit | lag-1 autocorrelation of the whitened series (run-standardised bins) | 0.2703 | −0.1448 [−0.2772, −0.0256] | 0.0162 | 11 |
| AR(1) | ts_gsr | W = 60 | MMI-sts | 0.7176 | −0.0620 [−0.0928, −0.0326] | 0.0006 | 13 |
| AR(1) | ts_gsr | W = 60 | CCS-sts (`phyid`'s mask) | −0.0552 | −0.0057 [−0.0098, −0.0017] | 0.0065 | 12 |
| AR(1) | ts_gsr | W = 60 | lag-1 autocorrelation of the whitened series | 0.7506 | −0.0196 [−0.0291, −0.0106] | 0.0010 | 12 |
| AR(1) | ts_gsr | global fit | MMI-sts | 0.8043 | −0.0559 [−0.0903, −0.0239] | 0.0015 | 13 |
| AR(1) | ts_gsr | global fit | CCS-sts (`phyid`'s mask) | −0.0298 | +0.0134 [+0.0077, +0.0192] | 0.0005 | 1 |
| AR(1) | ts_gsr | global fit | lag-1 autocorrelation of the whitened series (run-standardised bins) | 0.9215 | −0.3164 [−0.4375, −0.2019] | 0.0004 | 13 |
| AR(1) | ts_demean | W = 60 | MMI-sts | 0.6822 | −0.0784 [−0.1110, −0.0465] | 0.0004 | 13 |
| AR(1) | ts_demean | W = 60 | CCS-sts (`phyid`'s mask) | −0.0469 | +0.0035 [−0.0057, +0.0137] | 0.5170 | 5 |
| AR(1) | ts_demean | W = 60 | lag-1 autocorrelation of the whitened series | 0.7426 | −0.0276 [−0.0384, −0.0168] | 0.0004 | 13 |
| AR(1) | ts_demean | global fit | MMI-sts | 0.7648 | −0.0871 [−0.1350, −0.0387] | 0.0020 | 13 |
| AR(1) | ts_demean | global fit | CCS-sts (`phyid`'s mask) | −0.0287 | +0.0204 [+0.0106, +0.0307] | 0.0004 | 1 |
| AR(1) | ts_demean | global fit | lag-1 autocorrelation of the whitened series (run-standardised bins) | 0.8631 | −0.2412 [−0.3872, −0.1065] | 0.0013 | 13 |

The AR(1)-substituted estimate on the AR(p)-whitened series, ts_gsr, W = 60: observed sts level 0.2766, AR(1)-substituted 0.2426, residual +0.0341; DiD observed −0.0262, AR(1)-substituted −0.0192, residual −0.0070 (negative in 8/14). The CCS-sts values of this table were computed with `phyid`'s mask, not the published definition (review of 22 September, Finding 8). The lag-1 autocorrelation DiD of the AR(p)-whitened series on ts_gsr at W = 60 is −0.0544 [−0.1077, +0.0006], p = 0.052, an interval that includes zero where the committed percentile interval did not. The AR(1) residual's lag-1 autocorrelation of 0.75 is the value ρ₁(ρ₁² − ρ₂)/(1 − ρ₁²) takes for the pooled placebo function (ρ₁ = 0.868, ρ₂ = 0.539). Power shares inside, below and above 0.01–0.08 Hz, the run-level r₁ and the W = 60 r₁ of the raw, AR(1), AR(p ≤ 5), AR(10) and AR(20) residual series (B16b; means over the 28 runs, SD over runs in brackets; the BIC orders of B16 reproduced exactly):

**ts_gsr**

| series | in-band share (0.01–0.08 Hz) | share below 0.01 Hz | share above 0.08 Hz | run-level r₁ | W = 60 r₁, DMT windows 1–4 | kept samples per run |
|---|---|---|---|---|---|---|
| raw | 0.992 (0.003) | 0.007 (0.003) | 0.001 (0.000) | +0.8661 (0.0076) | +0.8479 (0.0147) | 840.0 |
| ar1 | 0.996 (0.001) | 0.001 (0.000) | 0.003 (0.001) | +0.7572 (0.0055) | +0.7506 (0.0107) | 839.0 |
| arp | 0.655 (0.051) | 0.007 (0.002) | 0.338 (0.050) | +0.2944 (0.0698) | +0.2625 (0.0814) | 835.0 |
| p10 | 0.479 (0.049) | 0.008 (0.002) | 0.512 (0.050) | +0.0943 (0.0794) | +0.1368 (0.0844) | 830.0 |
| p20 | 0.391 (0.015) | 0.012 (0.002) | 0.597 (0.015) | +0.0002 (0.0076) | +0.0524 (0.0429) | 820.0 |

**ts_demean**

| series | in-band share (0.01–0.08 Hz) | share below 0.01 Hz | share above 0.08 Hz | run-level r₁ | W = 60 r₁, DMT windows 1–4 | kept samples per run |
|---|---|---|---|---|---|---|
| raw | 0.992 (0.003) | 0.007 (0.003) | 0.001 (0.000) | +0.8561 (0.0104) | +0.8382 (0.0165) | 840.0 |
| ar1 | 0.996 (0.002) | 0.001 (0.001) | 0.003 (0.001) | +0.7483 (0.0091) | +0.7426 (0.0131) | 839.0 |
| arp | 0.670 (0.070) | 0.006 (0.002) | 0.324 (0.070) | +0.3011 (0.1061) | +0.2583 (0.1153) | 835.0 |
| p10 | 0.457 (0.042) | 0.008 (0.002) | 0.535 (0.042) | +0.0346 (0.0584) | +0.0739 (0.0855) | 830.0 |
| p20 | 0.387 (0.018) | 0.012 (0.002) | 0.600 (0.017) | -0.0024 (0.0089) | +0.0323 (0.0445) | 820.0 |

Note. The AR(p ≤ 5) whitening leaves 65.5 % of the power in band and 33.8 % above it, where the raw series has 0.1 % above it; at fixed orders 10 and 20 the above-band share rises to 51.2 % and 59.7 % while the run-level r₁ falls to 0.09 and 0.00. Reference values: the raw in-band share is 0.992, ideal flat-spectrum noise on the band at TR 2 s has r₁ = 0.8176, and the band is 0.28 of the Nyquist range.

## S12 Table. The residual of the AR(1)-substituted estimate by variant and estimator

Moved from the main text (Table 4 of the drafts of 21–22 September) in Stage B of round 16. Source: `notes/review_results/partB/diag_tables.md` (B4) and `notes/review_results/inference_rows_diag.csv`; the intervals are B21's inverted sign-flip 95 % intervals (`partB/inference_revision.csv`) and the correlations carry B21 (d)'s Fisher-z intervals. The AR(1)-substituted estimate is the sts of each window's 4 × 4 matrix with the pair's measured a_x, a_y and q kept and the two cross-lag correlations set to a_y q and a_x q (main text, Results 4); the residual is observed minus AR(1)-substituted, averaged over pairs. Level columns are means over all subjects, both runs and all windows (392 combinations at W = 60) and, in the run-level rows, over subjects and runs; they are not the pre-injection means of the main text's Tables 1 and 2. In the run-level rows the AR(1)-substituted value is one value per run, so its DiD is zero and the residual DiD equals the observed DiD. Across the 392 windows of the primary row the residual's SD (0.0161) is a fifth of the observed sts's (0.0790). The last row gives the expectations of the W = 60 residual DiD under a pure autocorrelation change, with the exact sign-flip p of the observed residual DiD against each (B21 (b)).

| variant, estimator | observed level | AR(1)-substituted | residual (% of observed) | observed DiD | AR(1)-substituted DiD [interval] | residual DiD [interval], negative/14 | r(AR(1)-substituted DiD, observed DiD) [Fisher-z] | r(residual DiD, autocorrelation DiD) [Fisher-z] |
|---|---|---|---|---|---|---|---|---|
| ts_gsr, W = 60 | 1.1377 | 1.1865 | −0.0489 (−4.3 %) | −0.0809 | −0.0924 [−0.1503, −0.0348] | +0.0115 [+0.0005, +0.0226], 4 | +0.989 [+0.966, +0.997] | −0.780 [−0.927, −0.426] |
| ts_gsr, W = 30 | 1.0082 | 1.1062 | −0.0980 (−9.7 %) | −0.0686 | −0.0869 [−0.1430, −0.0317] | +0.0182 [+0.0045, +0.0319], 2 | +0.987 [+0.957, +0.996] | −0.825 [−0.943, −0.523] |
| ts_demean, W = 60 | 1.0802 | 1.1181 | −0.0378 (−3.5 %) | −0.1031 | −0.1213 [−0.1874, −0.0554] | +0.0182 [+0.0072, +0.0293], 2 | +0.990 [+0.967, +0.997] | −0.597 [−0.856, −0.097] |
| ts_demean, W = 30 | 0.9636 | 1.0471 | −0.0835 (−8.7 %) | −0.0877 | −0.1136 [−0.1728, −0.0529] | +0.0259 [+0.0117, +0.0403], 3 | +0.981 [+0.940, +0.994] | −0.604 [−0.859, −0.108] |
| ts_gsr, run level | 1.2883 | 1.3021 | −0.0137 [−0.0146, −0.0129] (−1.1 %) | −0.0801 | constant within run | = observed by construction | — | — |
| ts_demean, run level | 1.2205 | 1.2197 | +0.0008 [−0.0060, +0.0074] (+0.1 %) | −0.1035 | constant within run | = observed by construction | — | — |
| expectation, W = 60, pure autocorrelation change | — | — | — | — | — | +0.0027 ± 0.0014 (band-passed generator, B17b; p = 0.108); +0.0049 ± 0.0017 (AR(1) pairs, B17; p = 0.219); +0.0054 (finite-sample null with the data's autocorrelation function; p = 0.251) | — | — |

## S13 Table. The sts change that the autocorrelation change produces, by estimator, with the autocorrelation change each row carries

Moved from the main text (Table 5 of the drafts of 21–22 September) in Stage B of round 16, with the population and window-level autocorrelation changes added (review of 22 September, Finding 14; B23 (e), B24). Nats; ts_gsr. Each row answers the question in its last column; the observed DiD is the last row. The two simulated conditions are condition (i) of the calibration, a fall of 0.015 in the population autocorrelation of the AR(1) pairs and the tilt change that gives the band-passed generator the data's window-level change (S10 Table). "Population Δr₁" is the change of the process's lag-1 autocorrelation; "window-level Δr₁" is the change of the mean pair-level a (the mean of a pair's a_x and a_y within a window), the quantity the estimators see, as a DiD for the generators and the data. The rows are not comparable across columns without the Δr₁ columns: the Gaussian-process row changes its population lag-1 autocorrelation by −0.010 (0.868 → 0.858 at q = 0.2; `sts_matched_null_F3.log`), the AR(1) row by −0.015 and the band-passed row by −0.0163.

| quantity | value | population Δr₁ | window-level Δr₁ | what it answers |
|---|---|---|---|---|
| map projection: the mean regional r₁ change (−0.0146) through ∂sts/∂r₁ = 5.99 at the pairs' point (0.848, 0.24) | −0.087 | — | −0.0146 (regional r₁) | the mean change passed through the slope at one point |
| the AR(1)-substituted estimate from each window's (a_x, a_y, q), W = 60 | −0.0924 | — | −0.0155 (pair-level a); −0.0146 (regional r₁) | each pair's own point, averaged over pairs, at the windowed estimator |
| true change of sts under the whole autocorrelation-function change at fixed q (Gaussian process with the placebo and the post-DMT function) | −0.069 | −0.010 | — | the population change before any estimator |
| — what the W = 60 estimator returns of it | −0.056 | | — | the estimator's shrinkage of that change |
| simulated Δa = −0.015 on AR(1) pairs (condition (i)): population closed form | −0.0816 (1.1936 → 1.1121) | −0.015 (by construction) | | a known population change of the family |
| — W = 60 estimator / global fit | −0.042 / −0.068 | | −0.01243 ± 0.00101 (W = 60; B23 (e)) | what the two estimators return of it |
| the same on the band-passed generator: population (B23 (e)) | −0.1126 (1.3795 → 1.2669) | −0.0163 (0.8678 → 0.8515) | | the population change on series with the data's spectrum |
| — W = 60 estimator / global fit (B17b) | −0.0940 / −0.1046 | | −0.01540 ± 0.00035 (W = 60; B24) | what the two estimators return of it |
| observed DiD: W = 60 / global fit | −0.0809 / −0.0801 | — | −0.0155 (pair-level a); −0.0146 (regional r₁) | the data |

Note. Rates taken within one simulation, per unit of window-level pair-level a (the decision entry of Stage B of round 16): sts changes by +6.13 on the band-passed generator (B24: −0.09441 for −0.01540) and by +3.08 on AR(1) pairs (B23 (b) (i), a whole-run change against the unperturbed pairs: −0.04240 for −0.01377), against +5.2 in the data (−0.0809 for −0.0155; +5.5, that is 0.0055 nats per 0.001, per unit of regional r₁). The residual changes by −0.18 on the band-passed generator (B24: +0.00279 for −0.01540), −0.39 on AR(1) pairs (B23 (b) (i)), −0.37 under the finite-sample null (+0.0054 for its own −0.0146; `notes/review_results/logs/review_v2_residual_null.log`) and −1.59 and −2.73 under a weakening of a shared slow component's autocorrelation and of its weight (B23 (b), (a5)), against −0.74 in the data (+0.0115 for −0.0155) and −0.75 per unit of regional r₁ as the per-subject OLS slope (B21 (c)). The data's pair-level a change is `residual_source.log`'s (12 of 14 subjects negative).

## S14 Table. Lag dependence

Moved from the main text (Table 6 of the drafts of 21–22 September) in Stage B of round 16. ts_gsr; nats; DMT pre-injection means; DiD with its inverted sign-flip 95 % interval (B21) and exact p; W = 60 except the last column, the global fit; the per-subject correlations with their Fisher-z intervals (B21 (d)). Source: `notes/review_results/partB/lag_tables.md`, `inference_rows_lag.csv`. The relative size of the contrast at each lag, the overlap of the autocorrelation contrasts' intervals and the spectral centroid are in S3 Text, section 9.

| τ | mean r_τ | sts level | sts DiD [interval], p | lag-τ autocorrelation DiD [interval], p | r(sts DiD, r_τ DiD) per subject [Fisher-z] | global-fit sts DiD [interval], p |
|---|---|---|---|---|---|---|
| 1 | 0.848 | 1.1554 | −0.0809 [−0.1317, −0.0310], 0.0038 | −0.0146 [−0.0261, −0.0037], 0.0106 | +0.953 [+0.854, +0.985] | −0.0801 [−0.1362, −0.0251], 0.0071 |
| 2 | 0.513 | 0.1797 | −0.0429 [−0.0692, −0.0173], 0.0037 | −0.0468 [−0.0799, −0.0138], 0.0090 | +0.970 [+0.906, +0.991] | −0.0485 [−0.0846, −0.0134], 0.0098 |
| 3 | 0.139 | 0.0262 | −0.0043 [−0.0066, −0.0019], 0.0018 | −0.0681 [−0.1185, −0.0173], 0.0132 | +0.626 [+0.143, +0.868] | −0.0116 [−0.0189, −0.0049], 0.0012 |
| 5 | −0.202 | 0.0415 | −0.0024 [−0.0081, +0.0032], 0.3688 | −0.0108 [−0.0514, +0.0304], 0.5670 | −0.832 [−0.945, −0.540] | +0.0015 [−0.0109, +0.0133], 0.7997 |

## S15 Table. CCS-sts and ΦR by variant and estimator

Moved from the main text (Table 3 of the drafts of 21–22 September) in Stage B of round 16. DMT contrast of CCS-sts (published double-redundancy definition) and of ΦR (nats; inverted sign-flip 95 % interval, B21; exact sign-flip p; phase-randomised p as a stationarity check; subjects negative of 14); both exploratory. The correlation with the autocorrelation DiD carries its Fisher-z interval (B21 (d)). Source: `notes/review_results/inference_rows_ccs_pub.csv`, `inference_rows_raw.csv`, `partB/ccs_pub_tables.md`. The CCS-sts cell at W = 60 on ts_gsr and the ΦR cell at W = 60 on ts_demean have intervals that include zero (+0.0044 [−0.0001, +0.0088], p = 0.056; +0.0157 [−0.0024, +0.0341], p = 0.085); the committed percentile intervals of earlier drafts did not include it (S17 Table).

| variant, estimator | CCS-sts DiD [interval], p, phase p, neg/14 | r(CCS-sts DiD, autocorrelation DiD) [Fisher-z] | ΦR DiD [interval], p, phase p, neg/14 |
|---|---|---|---|
| ts_gsr, W = 60 | +0.0044 [−0.0001, +0.0088], 0.0559, 0.0060, 3 | −0.420 [−0.777, +0.143] | +0.0007 [−0.0093, +0.0112], 0.8971, 0.8372, 8 |
| ts_gsr, global | +0.0197 [+0.0133, +0.0261], 0.0002, 0.0010, 1 | −0.275 [−0.703, +0.299] | −0.0062 [−0.0138, +0.0013], 0.0953, 0.0230, 9 |
| ts_demean, W = 60 | +0.0120 [+0.0041, +0.0201], 0.0040, 0.0020, 3 | −0.428 [−0.781, +0.133] | +0.0157 [−0.0024, +0.0341], 0.0853, 0.0380, 4 |
| ts_demean, global | +0.0355 [+0.0208, +0.0503], 0.0001, 0.0010, 0 | −0.297 [−0.715, +0.277] | +0.0180 [−0.0040, +0.0405], 0.1177, 0.0190, 5 |

## S16 Table. Manufacture

Moved from the main text (Table 8 of the drafts of 21–22 September) in Stage B of round 16. The sts difference the estimator returns between two simulated conditions of equal analytic sts and different covariance, as a share of the observed contrast (−0.0809), by fitting length; the difference is estimated over 4,000 independent windows at W = 30, 60 and 840 (± is the standard error over those windows where the difference is not distinguishable from zero). The four matched pairs are described in S3 Text, section 6 (`notes/rev_sts_matched_null.py`; review of 14 September, section 5; a post hoc computation).

| matched pair | W = 30 | W = 60 | 840 samples |
|---|---|---|---|
| lowered autocorrelation, cross-coupling re-solved (asymmetric VAR(1)) | −6 % | −9 % | +2 % |
| raised noise correlation, autocorrelation re-solved (asymmetric VAR(1)) | +33 % | +16 % | +1 % |
| raised noise correlation, autocorrelation re-solved (VAR(1) at a = 0.87) | +6 % ± 8 % | +7 % ± 8 % | +29 % |
| post-DMT autocorrelation function tilted back to the placebo r₁ (Gaussian process) | −1 % ± 8 % | −8 % ± 6 % | +2 % |

## S17 Table. Every interval of a mean over subjects, by method (B21)

Source: `notes/review_results/partB/inference_revision.csv` and `inference_revision_tables.md` (record, the B21 pre-run entry and outcome of 23 September 2026; B21 was run at a9d9ca4). All 932 quantities with a saved per-subject vector: the 738 rows of the eight `notes/review_results/inference_rows_*.pkl` (every window set and field), 36 recomputations of the per-run changes and FD-residualised DiDs of Table 2 and S1 Table ("engine"), and 158 other saved per-subject quantities ("saved"). For each: the mean over the 14 subjects; the exact sign-flip p against zero (relative tolerance 1e-12) beside the committed p; the committed subject-bootstrap percentile interval (10,000 draws); the inverted sign-flip interval {μ : p(μ) > 0.05}, which the paper reports; the t interval, mean ± t(0.975, 13)·SD/√14; the ratio of the inverted to the percentile width; whether zero lies inside the percentile, inverted and t interval; and negative/14. The inverted interval excludes zero exactly when p ≤ 0.05 (932 of 932), and the monotonicity grid found no point where p rose away from the mean.

Note. The width ratio has median 1.143 (quartiles 1.127–1.156) and range 1.039–1.288. That range includes three S9 Table cross-lag budget cells whose committed limits were printed at five decimals, so that their percentile widths carry rounding of the order of the widths themselves (δ_means on ts_gsr, DMT run, 1.288; δ_means on ts_demean, placebo run, 1.039; ε on ts_demean, grand mean, 1.231); the other 929 ratios lie in 1.072–1.192, so that the percentile intervals were narrower by 6.7–16.1 % (median 12.5 %). Zero-inclusion differs between the percentile and the inverted interval for 39 quantities (marked "changes"): nine of them were quoted in the text and are rewritten there as effect and interval, and the other 30 are reported here. The exact p differs from the committed p by more than the committed p's precision for seven quantities, all rows of the CCS decomposition (B18), none of which is quoted in the text; all seven were recomputed from the six-decimal per-run values of `ccs_decomposition.csv`: the interaction Δs Δc̄ on ts_gsr at W = 60, code mask 0.5227 (committed 0.5233) and published mask 0.1176 (0.1178), and at the global fit, code mask 0.0592 (0.0588); on ts_demean at W = 60 the selected share s, code mask 0.5748 (0.5747) and published mask 0.8015 (0.8014), the share term c̄_pre Δs, published mask 0.5244 (0.5240), and the interaction, published mask 0.6897 (0.6893). Bias-corrected and accelerated (BCa) intervals for the 29 intervals the drafts of 20–22 September quoted differed from their percentile intervals by less than 10 % of their width (largest ratio 1.04; B19 (d); S3 Text, section 5); BCa corrects bias and skew, not the narrowness of percentile intervals at N = 14, and is not used. Quantity labels are those of the result files, in which "predicted" names the AR(1)-substituted estimate and "diag" its computation (B4). Quantities with no saved per-subject vector keep their subject-bootstrap percentile intervals and are marked "percentile" where they are quoted: S2 Table's group means of the per-subject Spearman ρ, S6 Table's Lempel–Ziv correlations, S4 Table's workspace contrasts, the mean per-subject r(regional sts, regional r₁) of Results 3, +0.756 [+0.715, +0.790], the deconvolved ΦR values of S2 Text and the spectral centroid of S3 Text, section 9; S8 Table's share (ii) of the TDMI DiD is a ratio of group means, not a mean over subjects, and keeps its percentile interval (e.g. 0.7797 [0.6531, 0.9362]). "quoted at" names the file and line of the text at 90690f4 where the committed interval was quoted.

| # | group | quantity | set | field | mean | exact p (committed) | percentile interval (committed) | inverted interval | t interval | width ratio | zero in pct / inv / t | neg/14 | quoted at (90690f4) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | pickle | CCS sts ts_gsr W60 | primary | did | +0.00362 | 0.0844 (0.0844) | [−0.00006, +0.00717] | [−0.00058, +0.00780] | [−0.00055, +0.00779] | 1.159 | yes / yes / yes | 4 | — |
| 2 | pickle | CCS sts ts_gsr W60 | sensitivity | did | +0.00381 | 0.0516 (0.0516) | [+0.00045, +0.00708] | [−0.00004, +0.00767] | [−0.00001, +0.00763] | 1.163 | no / yes / yes, changes | 4 | — |
| 3 | pickle | CCS sts ts_gsr W60 | early | did | +0.00383 | 0.0967 (0.0967) | [−0.00024, +0.00799] | [−0.00084, +0.00855] | [−0.00084, +0.00850] | 1.141 | yes / yes / yes | 5 | — |
| 4 | pickle | CCS sts ts_gsr W60 | late | did | +0.00345 | 0.1367 (0.1367) | [−0.00077, +0.00749] | [−0.00125, +0.00810] | [−0.00123, +0.00814] | 1.132 | yes / yes / yes | 3 | — |
| 5 | pickle | CCS sts ts_gsr W60 | trend_a_placebo_line | did | +0.00331 | 0.0684 (0.0684) | [+0.00026, +0.00648] | [−0.00026, +0.00687] | [−0.00028, +0.00689] | 1.146 | no / yes / yes, changes | 3 | — |
| 6 | pickle | CCS sts ts_gsr W60 | trend_b_shared_slope | did | +0.00332 | 0.0300 (0.0300) | [+0.00078, +0.00602] | [+0.00034, +0.00632] | [+0.00033, +0.00631] | 1.141 | no / no / no | 4 | — |
| 7 | pickle | CCS xtx+yty ts_gsr W60 | primary | did | −0.09091 | 0.0049 (0.0049) | [−0.14405, −0.03999] | [−0.15084, −0.03281] | [−0.15098, −0.03085] | 1.134 | no / no / no | 12 | — |
| 8 | pickle | CCS xtx+yty ts_gsr W60 | sensitivity | did | −0.08115 | 0.0095 (0.0095) | [−0.13374, −0.02930] | [−0.14058, −0.02317] | [−0.14084, −0.02146] | 1.124 | no / no / no | 12 | — |
| 9 | pickle | CCS xtx+yty ts_gsr W60 | early | did | −0.11285 | 0.0012 (0.0012) | [−0.16512, −0.06286] | [−0.17244, −0.05331] | [−0.17245, −0.05326] | 1.165 | no / no / no | 12 | — |
| 10 | pickle | CCS xtx+yty ts_gsr W60 | late | did | −0.07336 | 0.0333 (0.0333) | [−0.13260, −0.01368] | [−0.14088, −0.00672] | [−0.14146, −0.00526] | 1.128 | no / no / no | 10 | — |
| 11 | pickle | CCS xtx+yty ts_gsr W60 | trend_a_placebo_line | did | −0.10051 | 0.0022 (0.0022) | [−0.15298, −0.05135] | [−0.15691, −0.04461] | [−0.15774, −0.04327] | 1.105 | no / no / no | 13 | — |
| 12 | pickle | CCS xtx+yty ts_gsr W60 | trend_b_shared_slope | did | −0.11076 | 0.0009 (0.0009) | [−0.16090, −0.06498] | [−0.16455, −0.05680] | [−0.16512, −0.05640] | 1.123 | no / no / no | 13 | — |
| 13 | pickle | CCS rtr ts_gsr W60 | primary | did | −0.01241 | 0.0326 (0.0326) | [−0.02145, −0.00275] | [−0.02352, −0.00129] | [−0.02336, −0.00145] | 1.189 | no / no / no | 10 | — |
| 14 | pickle | CCS rtr ts_gsr W60 | sensitivity | did | −0.01147 | 0.0413 (0.0413) | [−0.02050, −0.00189] | [−0.02246, −0.00056] | [−0.02218, −0.00076] | 1.177 | no / no / no | 10 | — |
| 15 | pickle | CCS rtr ts_gsr W60 | early | did | −0.02069 | 0.0010 (0.0010) | [−0.02891, −0.01232] | [−0.03024, −0.01121] | [−0.03016, −0.01121] | 1.147 | no / no / no | 12 | — |
| 16 | pickle | CCS rtr ts_gsr W60 | late | did | −0.00579 | 0.3501 (0.3501) | [−0.01679, +0.00635] | [−0.01916, +0.00748] | [−0.01890, +0.00733] | 1.152 | yes / yes / yes | 9 | — |
| 17 | pickle | CCS rtr ts_gsr W60 | trend_a_placebo_line | did | −0.01198 | 0.0386 (0.0386) | [−0.02152, −0.00221] | [−0.02319, −0.00075] | [−0.02310, −0.00086] | 1.162 | no / no / no | 9 | — |
| 18 | pickle | CCS rtr ts_gsr W60 | trend_b_shared_slope | did | −0.01608 | 0.0054 (0.0054) | [−0.02469, −0.00713] | [−0.02607, −0.00602] | [−0.02605, −0.00611] | 1.142 | no / no / no | 12 | — |
| 19 | pickle | CCS sts ts_gsr global-bins | primary | did | +0.02101 | 0.0001 (0.0001) | [+0.01537, +0.02696] | [+0.01442, +0.02767] | [+0.01438, +0.02764] | 1.144 | no / no / no | 0 | — |
| 20 | pickle | CCS sts ts_gsr global-bins | sensitivity | did | +0.02047 | 0.0001 (0.0001) | [+0.01496, +0.02636] | [+0.01396, +0.02705] | [+0.01390, +0.02703] | 1.148 | no / no / no | 0 | — |
| 21 | pickle | CCS sts ts_gsr global-bins | early | did | +0.01991 | 0.0001 (0.0001) | [+0.01443, +0.02578] | [+0.01346, +0.02659] | [+0.01333, +0.02648] | 1.157 | no / no / no | 0 | — |
| 22 | pickle | CCS sts ts_gsr global-bins | late | did | +0.02189 | 0.0002 (0.0002) | [+0.01521, +0.02866] | [+0.01434, +0.02949] | [+0.01434, +0.02945] | 1.126 | no / no / no | 1 | — |
| 23 | pickle | CCS sts ts_gsr global-bins | trend_a_placebo_line | did | +0.02422 | 0.0001 (0.0001) | [+0.01803, +0.03033] | [+0.01723, +0.03121] | [+0.01724, +0.03120] | 1.137 | no / no / no | 0 | — |
| 24 | pickle | CCS sts ts_gsr global-bins | trend_b_shared_slope | did | +0.02416 | 0.0001 (0.0001) | [+0.01815, +0.03020] | [+0.01728, +0.03115] | [+0.01721, +0.03111] | 1.151 | no / no / no | 0 | — |
| 25 | pickle | CCS xtx+yty ts_gsr global-bins | primary | did | −0.08071 | 0.0201 (0.0201) | [−0.14243, −0.02150] | [−0.14884, −0.01333] | [−0.14973, −0.01169] | 1.121 | no / no / no | 13 | — |
| 26 | pickle | CCS xtx+yty ts_gsr global-bins | sensitivity | did | −0.07824 | 0.0232 (0.0232) | [−0.14011, −0.01932] | [−0.14590, −0.01147] | [−0.14660, −0.00987] | 1.113 | no / no / no | 13 | — |
| 27 | pickle | CCS xtx+yty ts_gsr global-bins | early | did | −0.10380 | 0.0018 (0.0018) | [−0.16022, −0.05232] | [−0.16549, −0.04398] | [−0.16529, −0.04232] | 1.126 | no / no / no | 13 | — |
| 28 | pickle | CCS xtx+yty ts_gsr global-bins | late | did | −0.06224 | 0.1208 (0.1208) | [−0.13434, +0.01024] | [−0.14219, +0.01779] | [−0.14332, +0.01884] | 1.107 | yes / yes / yes | 11 | — |
| 29 | pickle | CCS xtx+yty ts_gsr global-bins | trend_a_placebo_line | did | −0.08287 | 0.0188 (0.0188) | [−0.14296, −0.02323] | [−0.15023, −0.01521] | [−0.15164, −0.01410] | 1.128 | no / no / no | 12 | — |
| 30 | pickle | CCS xtx+yty ts_gsr global-bins | trend_b_shared_slope | did | −0.09632 | 0.0050 (0.0050) | [−0.15420, −0.04139] | [−0.15976, −0.03413] | [−0.16054, −0.03209] | 1.114 | no / no / no | 13 | — |
| 31 | pickle | CCS rtr ts_gsr global-bins | primary | did | −0.02231 | 0.0006 (0.0006) | [−0.03177, −0.01280] | [−0.03328, −0.01133] | [−0.03320, −0.01143] | 1.157 | no / no / no | 13 | — |
| 32 | pickle | CCS rtr ts_gsr global-bins | sensitivity | did | −0.02216 | 0.0006 (0.0006) | [−0.03161, −0.01296] | [−0.03297, −0.01134] | [−0.03288, −0.01143] | 1.160 | no / no / no | 13 | — |
| 33 | pickle | CCS rtr ts_gsr global-bins | early | did | −0.02698 | 0.0002 (0.0002) | [−0.03427, −0.01956] | [−0.03545, −0.01838] | [−0.03551, −0.01845] | 1.161 | no / no / no | 13 | — |
| 34 | pickle | CCS rtr ts_gsr global-bins | late | did | −0.01858 | 0.0120 (0.0120) | [−0.03000, −0.00705] | [−0.03183, −0.00529] | [−0.03185, −0.00531] | 1.157 | no / no / no | 11 | — |
| 35 | pickle | CCS rtr ts_gsr global-bins | trend_a_placebo_line | did | −0.02461 | 0.0007 (0.0007) | [−0.03489, −0.01466] | [−0.03625, −0.01303] | [−0.03615, −0.01308] | 1.148 | no / no / no | 12 | — |
| 36 | pickle | CCS rtr ts_gsr global-bins | trend_b_shared_slope | did | −0.02776 | 0.0004 (0.0004) | [−0.03732, −0.01852] | [−0.03865, −0.01684] | [−0.03862, −0.01690] | 1.159 | no / no / no | 13 | — |
| 37 | pickle | CCS sts ts_demean W60 | primary | did | +0.01337 | 0.0052 (0.0052) | [+0.00562, +0.02211] | [+0.00388, +0.02309] | [+0.00374, +0.02300] | 1.165 | no / no / no | 3 | — |
| 38 | pickle | CCS sts ts_demean W60 | sensitivity | did | +0.01198 | 0.0065 (0.0065) | [+0.00459, +0.02036] | [+0.00316, +0.02110] | [+0.00297, +0.02099] | 1.137 | no / no / no | 3 | — |
| 39 | pickle | CCS sts ts_demean W60 | early | did | +0.01023 | 0.0159 (0.0159) | [+0.00312, +0.01744] | [+0.00206, +0.01846] | [+0.00205, +0.01842] | 1.145 | no / no / no | 2 | — |
| 40 | pickle | CCS sts ts_demean W60 | late | did | +0.01588 | 0.0100 (0.0100) | [+0.00584, +0.02744] | [+0.00347, +0.02839] | [+0.00355, +0.02821] | 1.154 | no / no / no | 3 | — |
| 41 | pickle | CCS sts ts_demean W60 | trend_a_placebo_line | did | +0.01154 | 0.0093 (0.0093) | [+0.00427, +0.01942] | [+0.00293, +0.02038] | [+0.00277, +0.02031] | 1.151 | no / no / no | 3 | — |
| 42 | pickle | CCS sts ts_demean W60 | trend_b_shared_slope | did | +0.00900 | 0.0219 (0.0219) | [+0.00260, +0.01600] | [+0.00127, +0.01678] | [+0.00118, +0.01682] | 1.158 | no / no / no | 2 | — |
| 43 | pickle | CCS xtx+yty ts_demean W60 | primary | did | −0.13050 | 0.0018 (0.0018) | [−0.18758, −0.07278] | [−0.19617, −0.06419] | [−0.19642, −0.06458] | 1.150 | no / no / no | 13 | — |
| 44 | pickle | CCS xtx+yty ts_demean W60 | sensitivity | did | −0.11567 | 0.0024 (0.0024) | [−0.16984, −0.05812] | [−0.17934, −0.05130] | [−0.17941, −0.05194] | 1.146 | no / no / no | 12 | — |
| 45 | pickle | CCS xtx+yty ts_demean W60 | early | did | −0.13920 | 0.0006 (0.0006) | [−0.18987, −0.08675] | [−0.19822, −0.07934] | [−0.19848, −0.07993] | 1.153 | no / no / no | 13 | — |
| 46 | pickle | CCS xtx+yty ts_demean W60 | late | did | −0.12354 | 0.0066 (0.0066) | [−0.19333, −0.05230] | [−0.20528, −0.04270] | [−0.20383, −0.04326] | 1.153 | no / no / no | 11 | — |
| 47 | pickle | CCS xtx+yty ts_demean W60 | trend_a_placebo_line | did | −0.14004 | 0.0013 (0.0013) | [−0.20271, −0.07828] | [−0.20991, −0.06942] | [−0.21013, −0.06995] | 1.129 | no / no / no | 13 | — |
| 48 | pickle | CCS xtx+yty ts_demean W60 | trend_b_shared_slope | did | −0.14205 | 0.0012 (0.0012) | [−0.20233, −0.08286] | [−0.20994, −0.07272] | [−0.21028, −0.07382] | 1.148 | no / no / no | 13 | — |
| 49 | pickle | CCS rtr ts_demean W60 | primary | did | +0.00500 | 0.4977 (0.4977) | [−0.00794, +0.01945] | [−0.01022, +0.02065] | [−0.01042, +0.02042] | 1.127 | yes / yes / yes | 8 | — |
| 50 | pickle | CCS rtr ts_demean W60 | sensitivity | did | +0.00696 | 0.3916 (0.3916) | [−0.00532, +0.02253] | [−0.00760, +0.02298] | [−0.00870, +0.02262] | 1.098 | yes / yes / yes | 8 | — |
| 51 | pickle | CCS rtr ts_demean W60 | early | did | −0.00059 | 0.9523 (0.9523) | [−0.01534, +0.01704] | [−0.01793, +0.01845] | [−0.01948, +0.01830] | 1.123 | yes / yes / yes | 8 | — |
| 52 | pickle | CCS rtr ts_demean W60 | late | did | +0.00947 | 0.2526 (0.2526) | [−0.00481, +0.02446] | [−0.00676, +0.02630] | [−0.00727, +0.02621] | 1.130 | yes / yes / yes | 5 | — |
| 53 | pickle | CCS rtr ts_demean W60 | trend_a_placebo_line | did | +0.00652 | 0.3965 (0.3965) | [−0.00530, +0.02064] | [−0.00777, +0.02174] | [−0.00855, +0.02159] | 1.137 | yes / yes / yes | 6 | — |
| 54 | pickle | CCS rtr ts_demean W60 | trend_b_shared_slope | did | +0.00299 | 0.6584 (0.6584) | [−0.00818, +0.01596] | [−0.01079, +0.01700] | [−0.01087, +0.01685] | 1.152 | yes / yes / yes | 10 | — |
| 55 | pickle | CCS sts ts_demean global-bins | primary | did | +0.03215 | 0.0001 (0.0001) | [+0.02161, +0.04311] | [+0.01976, +0.04471] | [+0.01975, +0.04454] | 1.161 | no / no / no | 0 | — |
| 56 | pickle | CCS sts ts_demean global-bins | sensitivity | did | +0.03170 | 0.0001 (0.0001) | [+0.02145, +0.04279] | [+0.01944, +0.04414] | [+0.01944, +0.04396] | 1.158 | no / no / no | 0 | — |
| 57 | pickle | CCS sts ts_demean global-bins | early | did | +0.02942 | 0.0001 (0.0001) | [+0.02083, +0.03859] | [+0.01911, +0.03989] | [+0.01909, +0.03975] | 1.170 | no / no / no | 0 | — |
| 58 | pickle | CCS sts ts_demean global-bins | late | did | +0.03433 | 0.0004 (0.0004) | [+0.02129, +0.04773] | [+0.01909, +0.04962] | [+0.01921, +0.04946] | 1.155 | no / no / no | 1 | — |
| 59 | pickle | CCS sts ts_demean global-bins | trend_a_placebo_line | did | +0.03622 | 0.0001 (0.0001) | [+0.02475, +0.04849] | [+0.02261, +0.04987] | [+0.02268, +0.04976] | 1.149 | no / no / no | 0 | — |
| 60 | pickle | CCS sts ts_demean global-bins | trend_b_shared_slope | did | +0.03504 | 0.0001 (0.0001) | [+0.02449, +0.04637] | [+0.02251, +0.04768] | [+0.02249, +0.04758] | 1.150 | no / no / no | 0 | — |
| 61 | pickle | CCS xtx+yty ts_demean global-bins | primary | did | −0.11326 | 0.0106 (0.0106) | [−0.18098, −0.04225] | [−0.19289, −0.03224] | [−0.19373, −0.03278] | 1.158 | no / no / no | 12 | — |
| 62 | pickle | CCS xtx+yty ts_demean global-bins | sensitivity | did | −0.10996 | 0.0126 (0.0126) | [−0.17788, −0.03891] | [−0.18864, −0.02988] | [−0.18957, −0.03035] | 1.142 | no / no / no | 11 | — |
| 63 | pickle | CCS xtx+yty ts_demean global-bins | early | did | −0.12573 | 0.0024 (0.0024) | [−0.18477, −0.06454] | [−0.19346, −0.05623] | [−0.19433, −0.05713] | 1.141 | no / no / no | 12 | — |
| 64 | pickle | CCS xtx+yty ts_demean global-bins | late | did | −0.10328 | 0.0405 (0.0405) | [−0.18656, −0.01566] | [−0.20040, −0.00512] | [−0.20075, −0.00581] | 1.143 | no / no / no | 11 | — |
| 65 | pickle | CCS xtx+yty ts_demean global-bins | trend_a_placebo_line | did | −0.11522 | 0.0122 (0.0122) | [−0.18636, −0.04110] | [−0.19836, −0.03047] | [−0.19957, −0.03087] | 1.156 | no / no / no | 12 | — |
| 66 | pickle | CCS xtx+yty ts_demean global-bins | trend_b_shared_slope | did | −0.12396 | 0.0066 (0.0066) | [−0.19563, −0.05108] | [−0.20549, −0.04076] | [−0.20650, −0.04142] | 1.140 | no / no / no | 12 | — |
| 67 | pickle | CCS rtr ts_demean global-bins | primary | did | −0.01827 | 0.0082 (0.0082) | [−0.03134, −0.00718] | [−0.03229, −0.00492] | [−0.03208, −0.00446] | 1.133 | no / no / no | 11 | — |
| 68 | pickle | CCS rtr ts_demean global-bins | sensitivity | did | −0.01722 | 0.0128 (0.0128) | [−0.03036, −0.00591] | [−0.03123, −0.00378] | [−0.03108, −0.00337] | 1.123 | no / no / no | 10 | — |
| 69 | pickle | CCS rtr ts_demean global-bins | early | did | −0.02227 | 0.0046 (0.0046) | [−0.03379, −0.01059] | [−0.03593, −0.00866] | [−0.03581, −0.00874] | 1.175 | no / no / no | 10 | — |
| 70 | pickle | CCS rtr ts_demean global-bins | late | did | −0.01507 | 0.0732 (0.0732) | [−0.03097, −0.00127] | [−0.03218, +0.00136] | [−0.03195, +0.00181] | 1.129 | no / yes / yes, changes | 10 | — |
| 71 | pickle | CCS rtr ts_demean global-bins | trend_a_placebo_line | did | −0.02094 | 0.0022 (0.0022) | [−0.03398, −0.00970] | [−0.03527, −0.00737] | [−0.03500, −0.00688] | 1.149 | no / no / no | 11 | — |
| 72 | pickle | CCS rtr ts_demean global-bins | trend_b_shared_slope | did | −0.02439 | 0.0006 (0.0006) | [−0.03688, −0.01333] | [−0.03815, −0.01107] | [−0.03792, −0.01085] | 1.150 | no / no / no | 12 | — |
| 73 | pickle | CCSpub sts ts_gsr W60 | primary | did | +0.00438 | 0.0559 (0.0559) | [+0.00036, +0.00813] | [−0.00012, +0.00882] | [−0.00012, +0.00888] | 1.151 | no / yes / yes, changes | 3 | S3_Text.md:193; draft_v2.md:165; draft_v2.md:171 |
| 74 | pickle | CCSpub sts ts_gsr W60 | sensitivity | did | +0.00448 | 0.0356 (0.0356) | [+0.00079, +0.00800] | [+0.00035, +0.00858] | [+0.00036, +0.00861] | 1.142 | no / no / no | 3 | — |
| 75 | pickle | CCSpub sts ts_gsr W60 | early | did | +0.00519 | 0.0320 (0.0320) | [+0.00109, +0.00927] | [+0.00052, +0.00990] | [+0.00053, +0.00985] | 1.147 | no / no / no | 3 | — |
| 76 | pickle | CCSpub sts ts_gsr W60 | late | did | +0.00373 | 0.1505 (0.1505) | [−0.00108, +0.00818] | [−0.00156, +0.00894] | [−0.00154, +0.00900] | 1.134 | yes / yes / yes | 4 | — |
| 77 | pickle | CCSpub sts ts_gsr W60 | trend_a_placebo_line | did | +0.00406 | 0.0486 (0.0486) | [+0.00061, +0.00763] | [+0.00003, +0.00807] | [+0.00003, +0.00810] | 1.145 | no / no / no | 3 | — |
| 78 | pickle | CCSpub sts ts_gsr W60 | trend_b_shared_slope | did | +0.00442 | 0.0107 (0.0107) | [+0.00156, +0.00740] | [+0.00111, +0.00776] | [+0.00109, +0.00774] | 1.139 | no / no / no | 2 | — |
| 79 | pickle | CCSpub xtx+yty ts_gsr W60 | primary | did | −0.08940 | 0.0055 (0.0055) | [−0.14306, −0.03824] | [−0.14975, −0.03092] | [−0.14975, −0.02905] | 1.134 | no / no / no | 12 | — |
| 80 | pickle | CCSpub xtx+yty ts_gsr W60 | sensitivity | did | −0.07980 | 0.0106 (0.0106) | [−0.13272, −0.02771] | [−0.13951, −0.02197] | [−0.13967, −0.01992] | 1.119 | no / no / no | 12 | — |
| 81 | pickle | CCSpub xtx+yty ts_gsr W60 | early | did | −0.11014 | 0.0016 (0.0016) | [−0.16315, −0.05924] | [−0.17097, −0.04922] | [−0.17089, −0.04938] | 1.172 | no / no / no | 12 | — |
| 82 | pickle | CCSpub xtx+yty ts_gsr W60 | late | did | −0.07281 | 0.0333 (0.0333) | [−0.13206, −0.01363] | [−0.14010, −0.00648] | [−0.14058, −0.00504] | 1.128 | no / no / no | 10 | — |
| 83 | pickle | CCSpub xtx+yty ts_gsr W60 | trend_a_placebo_line | did | −0.09900 | 0.0023 (0.0023) | [−0.15209, −0.05000] | [−0.15562, −0.04273] | [−0.15638, −0.04161] | 1.106 | no / no / no | 13 | — |
| 84 | pickle | CCSpub xtx+yty ts_gsr W60 | trend_b_shared_slope | did | −0.10856 | 0.0010 (0.0010) | [−0.15892, −0.06257] | [−0.16297, −0.05404] | [−0.16329, −0.05384] | 1.131 | no / no / no | 13 | — |
| 85 | pickle | CCSpub rtr ts_gsr W60 | primary | did | −0.01165 | 0.0295 (0.0295) | [−0.02000, −0.00276] | [−0.02183, −0.00141] | [−0.02175, −0.00155] | 1.185 | no / no / no | 10 | — |
| 86 | pickle | CCSpub rtr ts_gsr W60 | sensitivity | did | −0.01080 | 0.0374 (0.0374) | [−0.01916, −0.00197] | [−0.02083, −0.00082] | [−0.02064, −0.00095] | 1.165 | no / no / no | 10 | — |
| 87 | pickle | CCSpub rtr ts_gsr W60 | early | did | −0.01933 | 0.0006 (0.0006) | [−0.02676, −0.01178] | [−0.02793, −0.01074] | [−0.02789, −0.01077] | 1.148 | no / no / no | 13 | — |
| 88 | pickle | CCSpub rtr ts_gsr W60 | late | did | −0.00551 | 0.3385 (0.3385) | [−0.01579, +0.00575] | [−0.01788, +0.00682] | [−0.01769, +0.00666] | 1.147 | yes / yes / yes | 9 | — |
| 89 | pickle | CCSpub rtr ts_gsr W60 | trend_a_placebo_line | did | −0.01123 | 0.0363 (0.0363) | [−0.02009, −0.00227] | [−0.02156, −0.00082] | [−0.02151, −0.00094] | 1.163 | no / no / no | 9 | — |
| 90 | pickle | CCSpub rtr ts_gsr W60 | trend_b_shared_slope | did | −0.01498 | 0.0054 (0.0054) | [−0.02294, −0.00671] | [−0.02426, −0.00572] | [−0.02421, −0.00574] | 1.142 | no / no / no | 12 | — |
| 91 | pickle | CCSpub sts ts_gsr global-bins | primary | did | +0.01965 | 0.0002 (0.0002) | [+0.01422, +0.02541] | [+0.01328, +0.02608] | [+0.01323, +0.02608] | 1.144 | no / no / no | 1 | S3_Text.md:193; draft_v2.md:165; draft_v2.md:172 |
| 92 | pickle | CCSpub sts ts_gsr global-bins | sensitivity | did | +0.01912 | 0.0001 (0.0001) | [+0.01376, +0.02483] | [+0.01286, +0.02550] | [+0.01278, +0.02546] | 1.142 | no / no / no | 0 | — |
| 93 | pickle | CCSpub sts ts_gsr global-bins | early | did | +0.01842 | 0.0001 (0.0001) | [+0.01289, +0.02446] | [+0.01190, +0.02519] | [+0.01174, +0.02510] | 1.148 | no / no / no | 0 | — |
| 94 | pickle | CCSpub sts ts_gsr global-bins | late | did | +0.02064 | 0.0002 (0.0002) | [+0.01425, +0.02700] | [+0.01346, +0.02783] | [+0.01352, +0.02777] | 1.127 | no / no / no | 1 | — |
| 95 | pickle | CCSpub sts ts_gsr global-bins | trend_a_placebo_line | did | +0.02265 | 0.0001 (0.0001) | [+0.01681, +0.02840] | [+0.01602, +0.02930] | [+0.01602, +0.02928] | 1.146 | no / no / no | 0 | — |
| 96 | pickle | CCSpub sts ts_gsr global-bins | trend_b_shared_slope | did | +0.02244 | 0.0001 (0.0001) | [+0.01668, +0.02835] | [+0.01588, +0.02914] | [+0.01578, +0.02911] | 1.136 | no / no / no | 0 | — |
| 97 | pickle | CCSpub xtx+yty ts_gsr global-bins | primary | did | −0.08342 | 0.0164 (0.0164) | [−0.14508, −0.02451] | [−0.15125, −0.01646] | [−0.15215, −0.01470] | 1.118 | no / no / no | 13 | — |
| 98 | pickle | CCSpub xtx+yty ts_gsr global-bins | sensitivity | did | −0.08093 | 0.0194 (0.0194) | [−0.14230, −0.02186] | [−0.14829, −0.01403] | [−0.14905, −0.01282] | 1.115 | no / no / no | 13 | — |
| 99 | pickle | CCSpub xtx+yty ts_gsr global-bins | early | did | −0.10678 | 0.0015 (0.0015) | [−0.16226, −0.05606] | [−0.16754, −0.04785] | [−0.16736, −0.04620] | 1.127 | no / no / no | 13 | — |
| 100 | pickle | CCSpub xtx+yty ts_gsr global-bins | late | did | −0.06474 | 0.1082 (0.1082) | [−0.13686, +0.00802] | [−0.14497, +0.01537] | [−0.14587, +0.01639] | 1.107 | yes / yes / yes | 11 | — |
| 101 | pickle | CCSpub xtx+yty ts_gsr global-bins | trend_a_placebo_line | did | −0.08601 | 0.0150 (0.0150) | [−0.14592, −0.02646] | [−0.15340, −0.01843] | [−0.15456, −0.01745] | 1.130 | no / no / no | 12 | — |
| 102 | pickle | CCSpub xtx+yty ts_gsr global-bins | trend_b_shared_slope | did | −0.09976 | 0.0039 (0.0039) | [−0.15739, −0.04523] | [−0.16303, −0.03772] | [−0.16368, −0.03585] | 1.117 | no / no / no | 13 | — |
| 103 | pickle | CCSpub rtr ts_gsr global-bins | primary | did | −0.02367 | 0.0009 (0.0009) | [−0.03365, −0.01362] | [−0.03520, −0.01209] | [−0.03515, −0.01218] | 1.154 | no / no / no | 13 | — |
| 104 | pickle | CCSpub rtr ts_gsr global-bins | sensitivity | did | −0.02350 | 0.0009 (0.0009) | [−0.03350, −0.01375] | [−0.03486, −0.01211] | [−0.03483, −0.01218] | 1.152 | no / no / no | 13 | — |
| 105 | pickle | CCSpub rtr ts_gsr global-bins | early | did | −0.02847 | 0.0002 (0.0002) | [−0.03630, −0.02044] | [−0.03755, −0.01923] | [−0.03760, −0.01933] | 1.155 | no / no / no | 13 | — |
| 106 | pickle | CCSpub rtr ts_gsr global-bins | late | did | −0.01983 | 0.0106 (0.0106) | [−0.03186, −0.00768] | [−0.03372, −0.00578] | [−0.03379, −0.00587] | 1.156 | no / no / no | 11 | — |
| 107 | pickle | CCSpub rtr ts_gsr global-bins | trend_a_placebo_line | did | −0.02618 | 0.0007 (0.0007) | [−0.03698, −0.01572] | [−0.03851, −0.01392] | [−0.03839, −0.01397] | 1.157 | no / no / no | 12 | — |
| 108 | pickle | CCSpub rtr ts_gsr global-bins | trend_b_shared_slope | did | −0.02948 | 0.0004 (0.0004) | [−0.03958, −0.01970] | [−0.04102, −0.01792] | [−0.04097, −0.01799] | 1.162 | no / no / no | 13 | — |
| 109 | pickle | CCSpub sts ts_demean W60 | primary | did | +0.01197 | 0.0040 (0.0040) | [+0.00541, +0.01920] | [+0.00412, +0.02011] | [+0.00390, +0.02005] | 1.160 | no / no / no | 3 | draft_v2.md:173 |
| 110 | pickle | CCSpub sts ts_demean W60 | sensitivity | did | +0.01070 | 0.0050 (0.0050) | [+0.00435, +0.01773] | [+0.00332, +0.01846] | [+0.00302, +0.01838] | 1.132 | no / no / no | 3 | — |
| 111 | pickle | CCSpub sts ts_demean W60 | early | did | +0.00944 | 0.0087 (0.0087) | [+0.00363, +0.01518] | [+0.00285, +0.01603] | [+0.00284, +0.01603] | 1.141 | no / no / no | 2 | — |
| 112 | pickle | CCSpub sts ts_demean W60 | late | did | +0.01400 | 0.0083 (0.0083) | [+0.00532, +0.02393] | [+0.00349, +0.02484] | [+0.00335, +0.02465] | 1.147 | no / no / no | 3 | — |
| 113 | pickle | CCSpub sts ts_demean W60 | trend_a_placebo_line | did | +0.01007 | 0.0081 (0.0081) | [+0.00386, +0.01674] | [+0.00286, +0.01752] | [+0.00266, +0.01749] | 1.139 | no / no / no | 2 | — |
| 114 | pickle | CCSpub sts ts_demean W60 | trend_b_shared_slope | did | +0.00800 | 0.0145 (0.0145) | [+0.00261, +0.01374] | [+0.00170, +0.01440] | [+0.00153, +0.01446] | 1.142 | no / no / no | 2 | — |
| 115 | pickle | CCSpub xtx+yty ts_demean W60 | primary | did | −0.13330 | 0.0020 (0.0020) | [−0.19175, −0.07405] | [−0.20058, −0.06527] | [−0.20091, −0.06569] | 1.150 | no / no / no | 13 | — |
| 116 | pickle | CCSpub xtx+yty ts_demean W60 | sensitivity | did | −0.11823 | 0.0029 (0.0029) | [−0.17394, −0.05948] | [−0.18314, −0.05249] | [−0.18340, −0.05307] | 1.141 | no / no / no | 12 | — |
| 117 | pickle | CCSpub xtx+yty ts_demean W60 | early | did | −0.14080 | 0.0006 (0.0006) | [−0.19287, −0.08655] | [−0.20142, −0.07881] | [−0.20215, −0.07945] | 1.153 | no / no / no | 13 | — |
| 118 | pickle | CCSpub xtx+yty ts_demean W60 | late | did | −0.12731 | 0.0063 (0.0063) | [−0.19903, −0.05492] | [−0.21090, −0.04488] | [−0.20928, −0.04534] | 1.152 | no / no / no | 11 | — |
| 119 | pickle | CCSpub xtx+yty ts_demean W60 | trend_a_placebo_line | did | −0.14297 | 0.0013 (0.0013) | [−0.20681, −0.07986] | [−0.21439, −0.07103] | [−0.21461, −0.07133] | 1.129 | no / no / no | 13 | — |
| 120 | pickle | CCSpub xtx+yty ts_demean W60 | trend_b_shared_slope | did | −0.14405 | 0.0012 (0.0012) | [−0.20542, −0.08352] | [−0.21378, −0.07292] | [−0.21387, −0.07424] | 1.155 | no / no / no | 13 | — |
| 121 | pickle | CCSpub rtr ts_demean W60 | primary | did | +0.00360 | 0.5797 (0.5797) | [−0.00790, +0.01634] | [−0.00990, +0.01742] | [−0.01007, +0.01726] | 1.127 | yes / yes / yes | 8 | — |
| 122 | pickle | CCSpub rtr ts_demean W60 | sensitivity | did | +0.00568 | 0.4448 (0.4448) | [−0.00529, +0.01963] | [−0.00737, +0.01993] | [−0.00838, +0.01974] | 1.095 | yes / yes / yes | 8 | — |
| 123 | pickle | CCSpub rtr ts_demean W60 | early | did | −0.00139 | 0.8748 (0.8748) | [−0.01440, +0.01411] | [−0.01667, +0.01542] | [−0.01811, +0.01533] | 1.125 | yes / yes / yes | 8 | — |
| 124 | pickle | CCSpub rtr ts_demean W60 | late | did | +0.00759 | 0.3081 (0.3081) | [−0.00522, +0.02110] | [−0.00702, +0.02270] | [−0.00745, +0.02262] | 1.129 | yes / yes / yes | 5 | — |
| 125 | pickle | CCSpub rtr ts_demean W60 | trend_a_placebo_line | did | +0.00506 | 0.4696 (0.4696) | [−0.00565, +0.01778] | [−0.00776, +0.01871] | [−0.00850, +0.01862] | 1.130 | yes / yes / yes | 6 | — |
| 126 | pickle | CCSpub rtr ts_demean W60 | trend_b_shared_slope | did | +0.00199 | 0.7408 (0.7408) | [−0.00793, +0.01342] | [−0.01027, +0.01455] | [−0.01035, +0.01433] | 1.163 | yes / yes / yes | 10 | — |
| 127 | pickle | CCSpub sts ts_demean global-bins | primary | did | +0.03550 | 0.0001 (0.0001) | [+0.02313, +0.04846] | [+0.02075, +0.05032] | [+0.02090, +0.05011] | 1.167 | no / no / no | 0 | draft_v2.md:174 |
| 128 | pickle | CCSpub sts ts_demean global-bins | sensitivity | did | +0.03507 | 0.0001 (0.0001) | [+0.02310, +0.04801] | [+0.02042, +0.04979] | [+0.02056, +0.04957] | 1.179 | no / no / no | 0 | — |
| 129 | pickle | CCSpub sts ts_demean global-bins | early | did | +0.03262 | 0.0001 (0.0001) | [+0.02247, +0.04353] | [+0.02023, +0.04501] | [+0.02042, +0.04482] | 1.176 | no / no / no | 0 | — |
| 130 | pickle | CCSpub sts ts_demean global-bins | late | did | +0.03781 | 0.0002 (0.0002) | [+0.02320, +0.05295] | [+0.02050, +0.05518] | [+0.02064, +0.05498] | 1.166 | no / no / no | 1 | — |
| 131 | pickle | CCSpub sts ts_demean global-bins | trend_a_placebo_line | did | +0.03896 | 0.0001 (0.0001) | [+0.02590, +0.05284] | [+0.02350, +0.05464] | [+0.02353, +0.05440] | 1.156 | no / no / no | 0 | — |
| 132 | pickle | CCSpub sts ts_demean global-bins | trend_b_shared_slope | did | +0.03756 | 0.0001 (0.0001) | [+0.02576, +0.05027] | [+0.02343, +0.05198] | [+0.02336, +0.05177] | 1.165 | no / no / no | 0 | — |
| 133 | pickle | CCSpub xtx+yty ts_demean global-bins | primary | did | −0.10655 | 0.0110 (0.0110) | [−0.17026, −0.03985] | [−0.18122, −0.03075] | [−0.18225, −0.03084] | 1.154 | no / no / no | 12 | — |
| 134 | pickle | CCSpub xtx+yty ts_demean global-bins | sensitivity | did | −0.10322 | 0.0123 (0.0123) | [−0.16784, −0.03664] | [−0.17664, −0.02824] | [−0.17802, −0.02842] | 1.131 | no / no / no | 12 | — |
| 135 | pickle | CCSpub xtx+yty ts_demean global-bins | early | did | −0.11932 | 0.0022 (0.0022) | [−0.17499, −0.06309] | [−0.18215, −0.05444] | [−0.18317, −0.05546] | 1.141 | no / no / no | 13 | — |
| 136 | pickle | CCSpub xtx+yty ts_demean global-bins | late | did | −0.09633 | 0.0435 (0.0435) | [−0.17551, −0.01238] | [−0.18810, −0.00357] | [−0.18859, −0.00406] | 1.131 | no / no / no | 11 | — |
| 137 | pickle | CCSpub xtx+yty ts_demean global-bins | trend_a_placebo_line | did | −0.10974 | 0.0120 (0.0120) | [−0.17809, −0.03893] | [−0.18882, −0.02994] | [−0.19009, −0.02939] | 1.142 | no / no / no | 12 | — |
| 138 | pickle | CCSpub xtx+yty ts_demean global-bins | trend_b_shared_slope | did | −0.11891 | 0.0062 (0.0062) | [−0.18789, −0.04999] | [−0.19630, −0.04051] | [−0.19734, −0.04047] | 1.130 | no / no / no | 12 | — |
| 139 | pickle | CCSpub rtr ts_demean global-bins | primary | did | −0.01491 | 0.0741 (0.0741) | [−0.03052, −0.00106] | [−0.03198, +0.00154] | [−0.03174, +0.00191] | 1.138 | no / yes / yes, changes | 9 | — |
| 140 | pickle | CCSpub rtr ts_demean global-bins | sensitivity | did | −0.01385 | 0.1001 (0.1001) | [−0.02948, +0.00011] | [−0.03097, +0.00273] | [−0.03081, +0.00310] | 1.139 | yes / yes / yes | 9 | — |
| 141 | pickle | CCSpub rtr ts_demean global-bins | early | did | −0.01907 | 0.0355 (0.0355) | [−0.03354, −0.00370] | [−0.03641, −0.00156] | [−0.03637, −0.00176] | 1.168 | no / no / no | 10 | — |
| 142 | pickle | CCSpub rtr ts_demean global-bins | late | did | −0.01159 | 0.2404 (0.2404) | [−0.03017, +0.00486] | [−0.03177, +0.00793] | [−0.03156, +0.00838] | 1.134 | yes / yes / yes | 9 | — |
| 143 | pickle | CCSpub rtr ts_demean global-bins | trend_a_placebo_line | did | −0.01820 | 0.0253 (0.0253) | [−0.03341, −0.00485] | [−0.03507, −0.00222] | [−0.03474, −0.00165] | 1.150 | no / no / no | 10 | — |
| 144 | pickle | CCSpub rtr ts_demean global-bins | trend_b_shared_slope | did | −0.02186 | 0.0078 (0.0078) | [−0.03661, −0.00850] | [−0.03805, −0.00613] | [−0.03790, −0.00582] | 1.136 | no / no / no | 11 | — |
| 145 | pickle | autocorr_deconv ts_gsr W60 | primary | did | −0.02199 | 0.0021 (0.0021) | [−0.03269, −0.01156] | [−0.03417, −0.01012] | [−0.03423, −0.00974] | 1.138 | no / no / no | 12 | S2_Text.md:7 |
| 146 | pickle | autocorr_deconv ts_gsr W60 | sensitivity | did | −0.02033 | 0.0034 (0.0034) | [−0.03088, −0.00975] | [−0.03254, −0.00839] | [−0.03250, −0.00816] | 1.143 | no / no / no | 12 | — |
| 147 | pickle | autocorr_deconv ts_gsr W60 | early | did | −0.02854 | 0.0004 (0.0004) | [−0.03843, −0.01849] | [−0.04012, −0.01699] | [−0.04010, −0.01698] | 1.160 | no / no / no | 13 | — |
| 148 | pickle | autocorr_deconv ts_gsr W60 | late | did | −0.01674 | 0.0248 (0.0248) | [−0.02963, −0.00400] | [−0.03145, −0.00239] | [−0.03141, −0.00207] | 1.134 | no / no / no | 10 | — |
| 149 | pickle | autocorr_deconv ts_gsr W60 | trend_a_placebo_line | did | −0.02384 | 0.0009 (0.0009) | [−0.03456, −0.01389] | [−0.03546, −0.01246] | [−0.03557, −0.01210] | 1.113 | no / no / no | 13 | — |
| 150 | pickle | autocorr_deconv ts_gsr W60 | trend_b_shared_slope | did | −0.02553 | 0.0005 (0.0005) | [−0.03519, −0.01602] | [−0.03635, −0.01484] | [−0.03650, −0.01456] | 1.122 | no / no / no | 13 | — |
| 151 | pickle | sts_deconv ts_gsr W60 | primary | did | −0.07819 | 0.0013 (0.0013) | [−0.11818, −0.04238] | [−0.12213, −0.03619] | [−0.12206, −0.03432] | 1.134 | no / no / no | 13 | S2_Text.md:7 |
| 152 | pickle | sts_deconv ts_gsr W60 | sensitivity | did | −0.07273 | 0.0017 (0.0017) | [−0.11169, −0.03670] | [−0.11636, −0.03117] | [−0.11604, −0.02943] | 1.136 | no / no / no | 12 | — |
| 153 | pickle | sts_deconv ts_gsr W60 | early | did | −0.09587 | 0.0006 (0.0006) | [−0.13539, −0.05677] | [−0.14210, −0.05004] | [−0.14149, −0.05026] | 1.171 | no / no / no | 13 | — |
| 154 | pickle | sts_deconv ts_gsr W60 | late | did | −0.06405 | 0.0096 (0.0096) | [−0.10893, −0.02365] | [−0.11409, −0.01743] | [−0.11355, −0.01456] | 1.133 | no / no / no | 12 | — |
| 155 | pickle | sts_deconv ts_gsr W60 | trend_a_placebo_line | did | −0.08209 | 0.0009 (0.0009) | [−0.12110, −0.04821] | [−0.12412, −0.04275] | [−0.12390, −0.04028] | 1.116 | no / no / no | 13 | — |
| 156 | pickle | sts_deconv ts_gsr W60 | trend_b_shared_slope | did | −0.08558 | 0.0004 (0.0004) | [−0.12206, −0.05365] | [−0.12408, −0.04861] | [−0.12433, −0.04684] | 1.103 | no / no / no | 13 | — |
| 157 | pickle | PhiR_deconv ts_gsr W60 | primary | did | +0.01775 | 0.0099 (0.0099) | [+0.00689, +0.02926] | [+0.00509, +0.03069] | [+0.00490, +0.03061] | 1.144 | no / no / no | 3 | S2_Text.md:9 |
| 158 | pickle | PhiR_deconv ts_gsr W60 | sensitivity | did | +0.01794 | 0.0077 (0.0077) | [+0.00725, +0.02931] | [+0.00522, +0.03085] | [+0.00526, +0.03062] | 1.162 | no / no / no | 3 | — |
| 159 | pickle | PhiR_deconv ts_gsr W60 | early | did | +0.02290 | 0.0109 (0.0109) | [+0.00866, +0.03823] | [+0.00566, +0.04028] | [+0.00585, +0.03994] | 1.170 | no / no / no | 3 | — |
| 160 | pickle | PhiR_deconv ts_gsr W60 | late | did | +0.01364 | 0.0159 (0.0159) | [+0.00379, +0.02357] | [+0.00287, +0.02477] | [+0.00246, +0.02482] | 1.108 | no / no / no | 3 | — |
| 161 | pickle | PhiR_deconv ts_gsr W60 | trend_a_placebo_line | did | +0.01504 | 0.0109 (0.0109) | [+0.00555, +0.02518] | [+0.00375, +0.02632] | [+0.00378, +0.02629] | 1.149 | no / no / no | 2 | — |
| 162 | pickle | PhiR_deconv ts_gsr W60 | trend_b_shared_slope | did | +0.01557 | 0.0079 (0.0079) | [+0.00640, +0.02547] | [+0.00487, +0.02636] | [+0.00484, +0.02630] | 1.127 | no / no / no | 2 | — |
| 163 | pickle | sts_deconv ts_gsr global-bins | primary | did | −0.07716 | 0.0018 (0.0018) | [−0.12303, −0.03816] | [−0.12624, −0.03190] | [−0.12596, −0.02837] | 1.112 | no / no / no | 13 | — |
| 164 | pickle | sts_deconv ts_gsr global-bins | sensitivity | did | −0.07660 | 0.0017 (0.0017) | [−0.12109, −0.03726] | [−0.12444, −0.03225] | [−0.12425, −0.02895] | 1.100 | no / no / no | 13 | — |
| 165 | pickle | sts_deconv ts_gsr global-bins | early | did | −0.09819 | 0.0005 (0.0005) | [−0.14380, −0.05739] | [−0.14801, −0.05004] | [−0.14749, −0.04888] | 1.134 | no / no / no | 13 | — |
| 166 | pickle | sts_deconv ts_gsr global-bins | late | did | −0.06034 | 0.0204 (0.0204) | [−0.11261, −0.01493] | [−0.11577, −0.00904] | [−0.11544, −0.00525] | 1.093 | no / no / no | 11 | — |
| 167 | pickle | sts_deconv ts_gsr global-bins | trend_a_placebo_line | did | −0.07599 | 0.0016 (0.0016) | [−0.12196, −0.03725] | [−0.12458, −0.03135] | [−0.12468, −0.02731] | 1.100 | no / no / no | 13 | — |
| 168 | pickle | sts_deconv ts_gsr global-bins | trend_b_shared_slope | did | −0.08245 | 0.0007 (0.0007) | [−0.12443, −0.04672] | [−0.12704, −0.04135] | [−0.12711, −0.03780] | 1.103 | no / no / no | 13 | — |
| 169 | pickle | PhiR_deconv ts_gsr global-bins | primary | did | −0.00322 | 0.4105 (0.4105) | [−0.00995, +0.00456] | [−0.01157, +0.00515] | [−0.01154, +0.00510] | 1.152 | yes / yes / yes | 10 | — |
| 170 | pickle | PhiR_deconv ts_gsr global-bins | sensitivity | did | −0.00334 | 0.3783 (0.3783) | [−0.01002, +0.00397] | [−0.01138, +0.00475] | [−0.01138, +0.00469] | 1.153 | yes / yes / yes | 10 | — |
| 171 | pickle | PhiR_deconv ts_gsr global-bins | early | did | −0.00337 | 0.4420 (0.4420) | [−0.01134, +0.00503] | [−0.01274, +0.00612] | [−0.01272, +0.00599] | 1.151 | yes / yes / yes | 9 | — |
| 172 | pickle | PhiR_deconv ts_gsr global-bins | late | did | −0.00310 | 0.4436 (0.4436) | [−0.01036, +0.00475] | [−0.01171, +0.00572] | [−0.01177, +0.00557] | 1.153 | yes / yes / yes | 8 | — |
| 173 | pickle | PhiR_deconv ts_gsr global-bins | trend_a_placebo_line | did | −0.00486 | 0.2124 (0.2124) | [−0.01187, +0.00249] | [−0.01307, +0.00339] | [−0.01300, +0.00329] | 1.147 | yes / yes / yes | 10 | — |
| 174 | pickle | PhiR_deconv ts_gsr global-bins | trend_b_shared_slope | did | −0.00556 | 0.1526 (0.1526) | [−0.01236, +0.00168] | [−0.01348, +0.00251] | [−0.01351, +0.00239] | 1.139 | yes / yes / yes | 10 | — |
| 175 | pickle | autocorr_deconv ts_gsr run-standardised bins | primary | did | −0.35915 | 0.0001 (0.0001) | [−0.47585, −0.24866] | [−0.49133, −0.23114] | [−0.48987, −0.22843] | 1.145 | no / no / no | 14 | — |
| 176 | pickle | autocorr_deconv ts_gsr run-standardised bins | sensitivity | did | −0.35633 | 0.0001 (0.0001) | [−0.47487, −0.24859] | [−0.48518, −0.23123] | [−0.48443, −0.22823] | 1.122 | no / no / no | 14 | — |
| 177 | pickle | autocorr_deconv ts_gsr run-standardised bins | early | did | −0.38600 | 0.0001 (0.0001) | [−0.48250, −0.28940] | [−0.49709, −0.27579] | [−0.49743, −0.27457] | 1.146 | no / no / no | 14 | — |
| 178 | pickle | autocorr_deconv ts_gsr run-standardised bins | late | did | −0.33767 | 0.0010 (0.0010) | [−0.47315, −0.20481] | [−0.48989, −0.18679] | [−0.49022, −0.18512] | 1.130 | no / no / no | 11 | — |
| 179 | pickle | autocorr_deconv ts_gsr run-standardised bins | trend_a_placebo_line | did | −0.41483 | 0.0001 (0.0001) | [−0.53847, −0.29664] | [−0.55132, −0.27800] | [−0.55264, −0.27702] | 1.130 | no / no / no | 14 | — |
| 180 | pickle | autocorr_deconv ts_gsr run-standardised bins | trend_b_shared_slope | did | −0.44116 | 0.0001 (0.0001) | [−0.55756, −0.32692] | [−0.57631, −0.30771] | [−0.57448, −0.30783] | 1.165 | no / no / no | 14 | — |
| 181 | pickle | autocorr_deconv ts_demean W60 | primary | did | −0.02635 | 0.0009 (0.0009) | [−0.03803, −0.01527] | [−0.03933, −0.01357] | [−0.03926, −0.01344] | 1.132 | no / no / no | 12 | — |
| 182 | pickle | autocorr_deconv ts_demean W60 | sensitivity | did | −0.02299 | 0.0023 (0.0023) | [−0.03446, −0.01138] | [−0.03623, −0.00981] | [−0.03615, −0.00984] | 1.144 | no / no / no | 12 | — |
| 183 | pickle | autocorr_deconv ts_demean W60 | early | did | −0.02803 | 0.0002 (0.0002) | [−0.03884, −0.01779] | [−0.04010, −0.01597] | [−0.04006, −0.01600] | 1.146 | no / no / no | 13 | — |
| 184 | pickle | autocorr_deconv ts_demean W60 | late | did | −0.02501 | 0.0060 (0.0060) | [−0.03986, −0.01056] | [−0.04184, −0.00839] | [−0.04168, −0.00834] | 1.142 | no / no / no | 11 | — |
| 185 | pickle | autocorr_deconv ts_demean W60 | trend_a_placebo_line | did | −0.02948 | 0.0009 (0.0009) | [−0.04281, −0.01699] | [−0.04420, −0.01528] | [−0.04417, −0.01479] | 1.120 | no / no / no | 13 | — |
| 186 | pickle | autocorr_deconv ts_demean W60 | trend_b_shared_slope | did | −0.02897 | 0.0011 (0.0011) | [−0.04201, −0.01647] | [−0.04365, −0.01455] | [−0.04371, −0.01423] | 1.140 | no / no / no | 13 | — |
| 187 | pickle | sts_deconv ts_demean W60 | primary | did | −0.10031 | 0.0004 (0.0004) | [−0.14585, −0.05909] | [−0.15063, −0.05164] | [−0.15009, −0.05053] | 1.141 | no / no / no | 13 | — |
| 188 | pickle | sts_deconv ts_demean W60 | sensitivity | did | −0.09349 | 0.0006 (0.0006) | [−0.13748, −0.05291] | [−0.14248, −0.04589] | [−0.14188, −0.04509] | 1.142 | no / no / no | 12 | — |
| 189 | pickle | sts_deconv ts_demean W60 | early | did | −0.11015 | 0.0002 (0.0002) | [−0.15206, −0.06980] | [−0.15801, −0.06280] | [−0.15750, −0.06281] | 1.157 | no / no / no | 13 | — |
| 190 | pickle | sts_deconv ts_demean W60 | late | did | −0.09243 | 0.0020 (0.0020) | [−0.14603, −0.04437] | [−0.15184, −0.03619] | [−0.15111, −0.03375] | 1.138 | no / no / no | 11 | — |
| 191 | pickle | sts_deconv ts_demean W60 | trend_a_placebo_line | did | −0.10737 | 0.0005 (0.0005) | [−0.15749, −0.06349] | [−0.16154, −0.05513] | [−0.16111, −0.05362] | 1.132 | no / no / no | 13 | — |
| 192 | pickle | sts_deconv ts_demean W60 | trend_b_shared_slope | did | −0.10699 | 0.0004 (0.0004) | [−0.15401, −0.06496] | [−0.15845, −0.05694] | [−0.15796, −0.05601] | 1.140 | no / no / no | 13 | — |
| 193 | pickle | PhiR_deconv ts_demean W60 | primary | did | +0.03499 | 0.0009 (0.0009) | [+0.01884, +0.05234] | [+0.01546, +0.05474] | [+0.01550, +0.05449] | 1.172 | no / no / no | 1 | — |
| 194 | pickle | PhiR_deconv ts_demean W60 | sensitivity | did | +0.03214 | 0.0013 (0.0013) | [+0.01678, +0.04904] | [+0.01389, +0.05097] | [+0.01353, +0.05074] | 1.149 | no / no / no | 1 | — |
| 195 | pickle | PhiR_deconv ts_demean W60 | early | did | +0.03326 | 0.0052 (0.0052) | [+0.01467, +0.05198] | [+0.01158, +0.05492] | [+0.01180, +0.05472] | 1.162 | no / no / no | 2 | — |
| 196 | pickle | PhiR_deconv ts_demean W60 | late | did | +0.03638 | 0.0009 (0.0009) | [+0.01739, +0.05965] | [+0.01393, +0.06103] | [+0.01175, +0.06101] | 1.115 | no / no / no | 1 | — |
| 197 | pickle | PhiR_deconv ts_demean W60 | trend_a_placebo_line | did | +0.03402 | 0.0013 (0.0013) | [+0.01809, +0.05157] | [+0.01489, +0.05328] | [+0.01487, +0.05317] | 1.147 | no / no / no | 2 | — |
| 198 | pickle | PhiR_deconv ts_demean W60 | trend_b_shared_slope | did | +0.03156 | 0.0038 (0.0038) | [+0.01499, +0.04789] | [+0.01236, +0.05081] | [+0.01268, +0.05045] | 1.169 | no / no / no | 3 | — |
| 199 | pickle | sts_deconv ts_demean global-bins | primary | did | −0.11354 | 0.0020 (0.0020) | [−0.17121, −0.05856] | [−0.17879, −0.04811] | [−0.17860, −0.04848] | 1.160 | no / no / no | 13 | — |
| 200 | pickle | sts_deconv ts_demean global-bins | sensitivity | did | −0.11221 | 0.0020 (0.0020) | [−0.16966, −0.05737] | [−0.17609, −0.04817] | [−0.17618, −0.04824] | 1.139 | no / no / no | 13 | — |
| 201 | pickle | sts_deconv ts_demean global-bins | early | did | −0.12327 | 0.0010 (0.0010) | [−0.17292, −0.07278] | [−0.18049, −0.06489] | [−0.18071, −0.06584] | 1.154 | no / no / no | 13 | — |
| 202 | pickle | sts_deconv ts_demean global-bins | late | did | −0.10576 | 0.0072 (0.0072) | [−0.17771, −0.03956] | [−0.18624, −0.02837] | [−0.18570, −0.02581] | 1.143 | no / no / no | 12 | — |
| 203 | pickle | sts_deconv ts_demean global-bins | trend_a_placebo_line | did | −0.11808 | 0.0024 (0.0024) | [−0.18276, −0.05847] | [−0.19104, −0.04619] | [−0.19037, −0.04579] | 1.165 | no / no / no | 12 | — |
| 204 | pickle | sts_deconv ts_demean global-bins | trend_b_shared_slope | did | −0.12084 | 0.0024 (0.0024) | [−0.18230, −0.06106] | [−0.19081, −0.05032] | [−0.19072, −0.05097] | 1.159 | no / no / no | 13 | — |
| 205 | pickle | PhiR_deconv ts_demean global-bins | primary | did | +0.02087 | 0.0933 (0.0933) | [+0.00071, +0.04226] | [−0.00355, +0.04545] | [−0.00327, +0.04500] | 1.179 | no / yes / yes, changes | 3 | — |
| 206 | pickle | PhiR_deconv ts_demean global-bins | sensitivity | did | +0.02062 | 0.0922 (0.0922) | [+0.00065, +0.04175] | [−0.00335, +0.04463] | [−0.00312, +0.04435] | 1.168 | no / yes / yes, changes | 3 | — |
| 207 | pickle | PhiR_deconv ts_demean global-bins | early | did | +0.01669 | 0.1998 (0.1998) | [−0.00349, +0.04005] | [−0.00733, +0.04212] | [−0.00866, +0.04203] | 1.136 | yes / yes / yes | 5 | — |
| 208 | pickle | PhiR_deconv ts_demean global-bins | late | did | +0.02421 | 0.0831 (0.0831) | [+0.00131, +0.05074] | [−0.00319, +0.05329] | [−0.00442, +0.05284] | 1.142 | no / yes / yes, changes | 4 | — |
| 209 | pickle | PhiR_deconv ts_demean global-bins | trend_a_placebo_line | did | +0.01933 | 0.0828 (0.0828) | [+0.00159, +0.03892] | [−0.00261, +0.04167] | [−0.00275, +0.04140] | 1.186 | no / yes / yes, changes | 4 | — |
| 210 | pickle | PhiR_deconv ts_demean global-bins | trend_b_shared_slope | did | +0.01727 | 0.1221 (0.1221) | [−0.00195, +0.03686] | [−0.00520, +0.04026] | [−0.00544, +0.03999] | 1.171 | yes / yes / yes | 4 | — |
| 211 | pickle | autocorr_deconv ts_demean run-standardised bins | primary | did | −0.26913 | 0.0006 (0.0006) | [−0.40650, −0.15067] | [−0.41752, −0.13031] | [−0.41654, −0.12172] | 1.123 | no / no / no | 13 | — |
| 212 | pickle | autocorr_deconv ts_demean run-standardised bins | sensitivity | did | −0.26383 | 0.0006 (0.0006) | [−0.40467, −0.14523] | [−0.41137, −0.12636] | [−0.40990, −0.11776] | 1.099 | no / no / no | 13 | — |
| 213 | pickle | autocorr_deconv ts_demean run-standardised bins | early | did | −0.29481 | 0.0013 (0.0013) | [−0.42065, −0.17521] | [−0.43826, −0.15376] | [−0.43776, −0.15186] | 1.159 | no / no / no | 11 | — |
| 214 | pickle | autocorr_deconv ts_demean run-standardised bins | late | did | −0.24858 | 0.0037 (0.0037) | [−0.41102, −0.10666] | [−0.42213, −0.08501] | [−0.42060, −0.07655] | 1.108 | no / no / no | 11 | — |
| 215 | pickle | autocorr_deconv ts_demean run-standardised bins | trend_a_placebo_line | did | −0.32871 | 0.0002 (0.0002) | [−0.45994, −0.21462] | [−0.47104, −0.19655] | [−0.46945, −0.18797] | 1.119 | no / no / no | 13 | — |
| 216 | pickle | autocorr_deconv ts_demean run-standardised bins | trend_b_shared_slope | did | −0.35356 | 0.0001 (0.0001) | [−0.48377, −0.24058] | [−0.49444, −0.21739] | [−0.49218, −0.21494] | 1.139 | no / no / no | 14 | — |
| 217 | pickle | diag observed sts ts_gsr W60 | primary | did | −0.08087 | 0.0038 (0.0038) | [−0.12611, −0.03769] | [−0.13174, −0.03102] | [−0.13207, −0.02967] | 1.139 | no / no / no | 13 | draft_v2.md:156; draft_v2.md:91 |
| 218 | pickle | diag observed sts ts_gsr W60 | sensitivity | did | −0.07334 | 0.0070 (0.0070) | [−0.11803, −0.02914] | [−0.12381, −0.02381] | [−0.12396, −0.02273] | 1.125 | no / no / no | 12 | supplementary.md:13 |
| 219 | pickle | diag observed sts ts_gsr W60 | early | did | −0.10285 | 0.0009 (0.0009) | [−0.14640, −0.06009] | [−0.15354, −0.05225] | [−0.15331, −0.05240] | 1.174 | no / no / no | 13 | — |
| 220 | pickle | diag observed sts ts_gsr W60 | late | did | −0.06328 | 0.0337 (0.0337) | [−0.11472, −0.01179] | [−0.12208, −0.00535] | [−0.12225, −0.00430] | 1.134 | no / no / no | 10 | — |
| 221 | pickle | diag observed sts ts_gsr W60 | trend_a_placebo_line | did | −0.08904 | 0.0021 (0.0021) | [−0.13474, −0.04610] | [−0.13871, −0.04016] | [−0.13908, −0.03900] | 1.112 | no / no / no | 13 | — |
| 222 | pickle | diag observed sts ts_gsr W60 | trend_b_shared_slope | did | −0.09953 | 0.0007 (0.0007) | [−0.14243, −0.05988] | [−0.14607, −0.05312] | [−0.14647, −0.05259] | 1.126 | no / no / no | 13 | — |
| 223 | pickle | diag predicted sts ts_gsr W60 | primary | did | −0.09239 | 0.0037 (0.0037) | [−0.14440, −0.04142] | [−0.15032, −0.03484] | [−0.15120, −0.03359] | 1.121 | no / no / no | 13 | draft_v2.md:128; draft_v2.md:78 |
| 224 | pickle | diag predicted sts ts_gsr W60 | sensitivity | did | −0.08418 | 0.0068 (0.0068) | [−0.13580, −0.03367] | [−0.14257, −0.02686] | [−0.14262, −0.02573] | 1.133 | no / no / no | 12 | — |
| 225 | pickle | diag predicted sts ts_gsr W60 | early | did | −0.12077 | 0.0006 (0.0006) | [−0.16977, −0.07255] | [−0.17564, −0.06645] | [−0.17555, −0.06599] | 1.123 | no / no / no | 13 | — |
| 226 | pickle | diag predicted sts ts_gsr W60 | late | did | −0.06970 | 0.0476 (0.0476) | [−0.13134, −0.01021] | [−0.13988, −0.00063] | [−0.13996, +0.00056] | 1.150 | no / no / yes | 11 | — |
| 227 | pickle | diag predicted sts ts_gsr W60 | trend_a_placebo_line | did | −0.09966 | 0.0024 (0.0024) | [−0.15085, −0.04981] | [−0.15697, −0.04282] | [−0.15734, −0.04199] | 1.130 | no / no / no | 13 | — |
| 228 | pickle | diag predicted sts ts_gsr W60 | trend_b_shared_slope | did | −0.11295 | 0.0009 (0.0009) | [−0.15994, −0.06830] | [−0.16550, −0.06046] | [−0.16609, −0.05982] | 1.146 | no / no / no | 13 | — |
| 229 | pickle | diag residual sts ts_gsr W60 | primary | did | +0.01153 | 0.0422 (0.0422) | [+0.00213, +0.02107] | [+0.00046, +0.02265] | [+0.00048, +0.02258] | 1.171 | no / no / no | 4 | S3_Text.md:199; draft_v2.md:116; draft_v2.md:120; draft_v2.md:128 |
| 230 | pickle | diag residual sts ts_gsr W60 | sensitivity | did | +0.01083 | 0.0491 (0.0491) | [+0.00134, +0.02004] | [+0.00005, +0.02157] | [+0.00010, +0.02156] | 1.151 | no / no / no | 4 | — |
| 231 | pickle | diag residual sts ts_gsr W60 | early | did | +0.01791 | 0.0012 (0.0012) | [+0.00988, +0.02597] | [+0.00861, +0.02725] | [+0.00864, +0.02718] | 1.159 | no / no / no | 2 | S3_Text.md:199 |
| 232 | pickle | diag residual sts ts_gsr W60 | late | did | +0.00642 | 0.3243 (0.3243) | [−0.00582, +0.01831] | [−0.00725, +0.02015] | [−0.00721, +0.02005] | 1.135 | yes / yes / yes | 5 | — |
| 233 | pickle | diag residual sts ts_gsr W60 | trend_a_placebo_line | did | +0.01063 | 0.0538 (0.0538) | [+0.00145, +0.02002] | [−0.00011, +0.02146] | [−0.00014, +0.02139] | 1.162 | no / yes / yes, changes | 5 | — |
| 234 | pickle | diag residual sts ts_gsr W60 | trend_b_shared_slope | did | +0.01343 | 0.0089 (0.0089) | [+0.00530, +0.02177] | [+0.00397, +0.02293] | [+0.00403, +0.02283] | 1.151 | no / no / no | 3 | — |
| 235 | pickle | diag observed sts ts_gsr W30 | primary | did | −0.06863 | 0.0042 (0.0042) | [−0.10836, −0.02931] | [−0.11424, −0.02422] | [−0.11467, −0.02258] | 1.139 | no / no / no | 13 | S1_Text.md:17; supplementary.md:17 |
| 236 | pickle | diag observed sts ts_gsr W30 | sensitivity | did | −0.06585 | 0.0067 (0.0067) | [−0.10715, −0.02612] | [−0.11153, −0.02120] | [−0.11207, −0.01962] | 1.115 | no / no / no | 12 | supplementary.md:17 |
| 237 | pickle | diag observed sts ts_gsr W30 | early | did | −0.08394 | 0.0012 (0.0012) | [−0.12669, −0.04511] | [−0.13026, −0.03795] | [−0.13014, −0.03774] | 1.132 | no / no / no | 13 | — |
| 238 | pickle | diag observed sts ts_gsr W30 | late | did | −0.05638 | 0.0321 (0.0321) | [−0.10243, −0.01175] | [−0.10810, −0.00531] | [−0.10861, −0.00414] | 1.134 | no / no / no | 11 | — |
| 239 | pickle | diag observed sts ts_gsr W30 | trend_a_placebo_line | did | −0.07663 | 0.0021 (0.0021) | [−0.11468, −0.03862] | [−0.11939, −0.03430] | [−0.12013, −0.03312] | 1.119 | no / no / no | 13 | — |
| 240 | pickle | diag observed sts ts_gsr W30 | trend_b_shared_slope | did | −0.08492 | 0.0010 (0.0010) | [−0.12253, −0.04947] | [−0.12556, −0.04389] | [−0.12638, −0.04347] | 1.118 | no / no / no | 13 | — |
| 241 | pickle | diag predicted sts ts_gsr W30 | primary | did | −0.08687 | 0.0046 (0.0046) | [−0.13680, −0.03733] | [−0.14301, −0.03167] | [−0.14357, −0.03017] | 1.119 | no / no / no | 12 | draft_v2.md:129 |
| 242 | pickle | diag predicted sts ts_gsr W30 | sensitivity | did | −0.08464 | 0.0062 (0.0062) | [−0.13486, −0.03515] | [−0.14090, −0.02875] | [−0.14152, −0.02776] | 1.125 | no / no / no | 12 | — |
| 243 | pickle | diag predicted sts ts_gsr W30 | early | did | −0.11020 | 0.0007 (0.0007) | [−0.15858, −0.06383] | [−0.16366, −0.05713] | [−0.16373, −0.05667] | 1.124 | no / no / no | 13 | — |
| 244 | pickle | diag predicted sts ts_gsr W30 | late | did | −0.06821 | 0.0424 (0.0424) | [−0.12618, −0.01066] | [−0.13429, −0.00273] | [−0.13477, −0.00165] | 1.139 | no / no / no | 11 | — |
| 245 | pickle | diag predicted sts ts_gsr W30 | trend_a_placebo_line | did | −0.09386 | 0.0026 (0.0026) | [−0.14169, −0.04661] | [−0.14698, −0.04076] | [−0.14795, −0.03977] | 1.117 | no / no / no | 13 | — |
| 246 | pickle | diag predicted sts ts_gsr W30 | trend_b_shared_slope | did | −0.10577 | 0.0007 (0.0007) | [−0.15030, −0.06298] | [−0.15512, −0.05628] | [−0.15608, −0.05546] | 1.132 | no / no / no | 13 | — |
| 247 | pickle | diag residual sts ts_gsr W30 | primary | did | +0.01825 | 0.0137 (0.0137) | [+0.00657, +0.02993] | [+0.00455, +0.03189] | [+0.00469, +0.03181] | 1.170 | no / no / no | 2 | draft_v2.md:129 |
| 248 | pickle | diag residual sts ts_gsr W30 | sensitivity | did | +0.01879 | 0.0116 (0.0116) | [+0.00711, +0.03046] | [+0.00512, +0.03235] | [+0.00531, +0.03227] | 1.166 | no / no / no | 2 | — |
| 249 | pickle | diag residual sts ts_gsr W30 | early | did | +0.02626 | 0.0005 (0.0005) | [+0.01605, +0.03723] | [+0.01419, +0.03826] | [+0.01424, +0.03829] | 1.137 | no / no / no | 1 | — |
| 250 | pickle | diag residual sts ts_gsr W30 | late | did | +0.01183 | 0.1385 (0.1385) | [−0.00220, +0.02575] | [−0.00459, +0.02815] | [−0.00440, +0.02807] | 1.171 | yes / yes / yes | 5 | — |
| 251 | pickle | diag residual sts ts_gsr W30 | trend_a_placebo_line | did | +0.01723 | 0.0150 (0.0150) | [+0.00568, +0.02851] | [+0.00400, +0.03045] | [+0.00409, +0.03037] | 1.158 | no / no / no | 3 | — |
| 252 | pickle | diag residual sts ts_gsr W30 | trend_b_shared_slope | did | +0.02085 | 0.0031 (0.0031) | [+0.01033, +0.03153] | [+0.00874, +0.03288] | [+0.00887, +0.03283] | 1.139 | no / no / no | 2 | — |
| 253 | pickle | diag observed sts ts_demean W60 | primary | did | −0.10311 | 0.0026 (0.0026) | [−0.15585, −0.05224] | [−0.16293, −0.04352] | [−0.16274, −0.04349] | 1.153 | no / no / no | 12 | S1_Text.md:7; draft_v2.md:76; draft_v2.md:91 |
| 254 | pickle | diag observed sts ts_demean W60 | sensitivity | did | −0.09352 | 0.0039 (0.0039) | [−0.14310, −0.04256] | [−0.15060, −0.03610] | [−0.15074, −0.03631] | 1.139 | no / no / no | 12 | supplementary.md:13 |
| 255 | pickle | diag observed sts ts_demean W60 | early | did | −0.11825 | 0.0012 (0.0012) | [−0.16733, −0.06788] | [−0.17599, −0.06035] | [−0.17571, −0.06080] | 1.163 | no / no / no | 13 | — |
| 256 | pickle | diag observed sts ts_demean W60 | late | did | −0.09100 | 0.0128 (0.0128) | [−0.15222, −0.03192] | [−0.16052, −0.02217] | [−0.16022, −0.02178] | 1.150 | no / no / no | 11 | — |
| 257 | pickle | diag observed sts ts_demean W60 | trend_a_placebo_line | did | −0.11260 | 0.0018 (0.0018) | [−0.16903, −0.05953] | [−0.17502, −0.05127] | [−0.17486, −0.05034] | 1.130 | no / no / no | 13 | — |
| 258 | pickle | diag observed sts ts_demean W60 | trend_b_shared_slope | did | −0.11925 | 0.0012 (0.0012) | [−0.17357, −0.06826] | [−0.17958, −0.05864] | [−0.17956, −0.05894] | 1.148 | no / no / no | 13 | — |
| 259 | pickle | diag predicted sts ts_demean W60 | primary | did | −0.12134 | 0.0022 (0.0022) | [−0.17762, −0.06312] | [−0.18742, −0.05540] | [−0.18732, −0.05537] | 1.153 | no / no / no | 12 | draft_v2.md:130 |
| 260 | pickle | diag predicted sts ts_demean W60 | sensitivity | did | −0.10709 | 0.0035 (0.0035) | [−0.16152, −0.05297] | [−0.17023, −0.04393] | [−0.17035, −0.04382] | 1.164 | no / no / no | 11 | — |
| 261 | pickle | diag predicted sts ts_demean W60 | early | did | −0.13652 | 0.0006 (0.0006) | [−0.18655, −0.08468] | [−0.19455, −0.07763] | [−0.19446, −0.07858] | 1.148 | no / no / no | 13 | — |
| 262 | pickle | diag predicted sts ts_demean W60 | late | did | −0.10920 | 0.0118 (0.0118) | [−0.17859, −0.03875] | [−0.19043, −0.02862] | [−0.18955, −0.02885] | 1.157 | no / no / no | 11 | — |
| 263 | pickle | diag predicted sts ts_demean W60 | trend_a_placebo_line | did | −0.12743 | 0.0021 (0.0021) | [−0.18892, −0.06713] | [−0.19732, −0.05803] | [−0.19735, −0.05752] | 1.144 | no / no / no | 12 | — |
| 264 | pickle | diag predicted sts ts_demean W60 | trend_b_shared_slope | did | −0.13345 | 0.0013 (0.0013) | [−0.19221, −0.07514] | [−0.20145, −0.06507] | [−0.20127, −0.06564] | 1.165 | no / no / no | 13 | — |
| 265 | pickle | diag residual sts ts_demean W60 | primary | did | +0.01823 | 0.0040 (0.0040) | [+0.00894, +0.02774] | [+0.00716, +0.02932] | [+0.00719, +0.02927] | 1.179 | no / no / no | 2 | draft_v2.md:130 |
| 266 | pickle | diag residual sts ts_demean W60 | sensitivity | did | +0.01356 | 0.0161 (0.0161) | [+0.00410, +0.02307] | [+0.00282, +0.02456] | [+0.00264, +0.02448] | 1.146 | no / no / no | 2 | — |
| 267 | pickle | diag residual sts ts_demean W60 | early | did | +0.01826 | 0.0001 (0.0001) | [+0.01282, +0.02344] | [+0.01209, +0.02441] | [+0.01214, +0.02438] | 1.160 | no / no / no | 0 | — |
| 268 | pickle | diag residual sts ts_demean W60 | late | did | +0.01820 | 0.0321 (0.0321) | [+0.00363, +0.03286] | [+0.00184, +0.03473] | [+0.00176, +0.03465] | 1.125 | no / no / no | 4 | — |
| 269 | pickle | diag residual sts ts_demean W60 | trend_a_placebo_line | did | +0.01483 | 0.0164 (0.0164) | [+0.00489, +0.02494] | [+0.00324, +0.02651] | [+0.00321, +0.02645] | 1.160 | no / no / no | 3 | — |
| 270 | pickle | diag residual sts ts_demean W60 | trend_b_shared_slope | did | +0.01420 | 0.0138 (0.0138) | [+0.00492, +0.02381] | [+0.00339, +0.02504] | [+0.00338, +0.02502] | 1.146 | no / no / no | 3 | — |
| 271 | pickle | diag observed sts ts_demean W30 | primary | did | −0.08769 | 0.0029 (0.0029) | [−0.13104, −0.04271] | [−0.13809, −0.03704] | [−0.13880, −0.03659] | 1.144 | no / no / no | 13 | — |
| 272 | pickle | diag observed sts ts_demean W30 | sensitivity | did | −0.08551 | 0.0037 (0.0037) | [−0.13069, −0.04019] | [−0.13646, −0.03457] | [−0.13667, −0.03436] | 1.126 | no / no / no | 12 | — |
| 273 | pickle | diag observed sts ts_demean W30 | early | did | −0.09855 | 0.0018 (0.0018) | [−0.14530, −0.05247] | [−0.15022, −0.04669] | [−0.15053, −0.04656] | 1.115 | no / no / no | 13 | — |
| 274 | pickle | diag observed sts ts_demean W30 | late | did | −0.07901 | 0.0114 (0.0114) | [−0.12976, −0.02926] | [−0.13763, −0.02076] | [−0.13740, −0.02061] | 1.163 | no / no / no | 11 | — |
| 275 | pickle | diag observed sts ts_demean W30 | trend_a_placebo_line | did | −0.09507 | 0.0016 (0.0016) | [−0.13976, −0.05064] | [−0.14596, −0.04462] | [−0.14620, −0.04394] | 1.137 | no / no / no | 13 | — |
| 276 | pickle | diag observed sts ts_demean W30 | trend_b_shared_slope | did | −0.09917 | 0.0011 (0.0011) | [−0.14340, −0.05588] | [−0.14841, −0.05022] | [−0.14860, −0.04974] | 1.122 | no / no / no | 13 | — |
| 277 | pickle | diag predicted sts ts_demean W30 | primary | did | −0.11355 | 0.0021 (0.0021) | [−0.16476, −0.05958] | [−0.17283, −0.05294] | [−0.17391, −0.05320] | 1.140 | no / no / no | 12 | draft_v2.md:131 |
| 278 | pickle | diag predicted sts ts_demean W30 | sensitivity | did | −0.10969 | 0.0026 (0.0026) | [−0.16139, −0.05702] | [−0.16905, −0.04931] | [−0.16989, −0.04950] | 1.147 | no / no / no | 12 | — |
| 279 | pickle | diag predicted sts ts_demean W30 | early | did | −0.12571 | 0.0007 (0.0007) | [−0.17236, −0.07569] | [−0.17913, −0.07078] | [−0.18038, −0.07103] | 1.121 | no / no / no | 13 | — |
| 280 | pickle | diag predicted sts ts_demean W30 | late | did | −0.10383 | 0.0098 (0.0098) | [−0.16593, −0.03932] | [−0.17666, −0.03100] | [−0.17635, −0.03131] | 1.150 | no / no / no | 11 | — |
| 281 | pickle | diag predicted sts ts_demean W30 | trend_a_placebo_line | did | −0.11829 | 0.0018 (0.0018) | [−0.17328, −0.06353] | [−0.18030, −0.05614] | [−0.18084, −0.05574] | 1.131 | no / no / no | 13 | — |
| 282 | pickle | diag predicted sts ts_demean W30 | trend_b_shared_slope | did | −0.12299 | 0.0013 (0.0013) | [−0.17512, −0.07010] | [−0.18338, −0.06172] | [−0.18398, −0.06201] | 1.158 | no / no / no | 13 | — |
| 283 | pickle | diag residual sts ts_demean W30 | primary | did | +0.02586 | 0.0020 (0.0020) | [+0.01354, +0.03830] | [+0.01174, +0.04032] | [+0.01165, +0.04007] | 1.155 | no / no / no | 3 | draft_v2.md:131 |
| 284 | pickle | diag residual sts ts_demean W30 | sensitivity | did | +0.02418 | 0.0023 (0.0023) | [+0.01219, +0.03638] | [+0.01049, +0.03835] | [+0.01027, +0.03809] | 1.152 | no / no / no | 3 | — |
| 285 | pickle | diag residual sts ts_demean W30 | early | did | +0.02716 | 0.0002 (0.0002) | [+0.01897, +0.03513] | [+0.01767, +0.03660] | [+0.01776, +0.03655] | 1.171 | no / no / no | 1 | — |
| 286 | pickle | diag residual sts ts_demean W30 | late | did | +0.02482 | 0.0171 (0.0171) | [+0.00836, +0.04189] | [+0.00534, +0.04455] | [+0.00523, +0.04442] | 1.170 | no / no / no | 4 | — |
| 287 | pickle | diag residual sts ts_demean W30 | trend_a_placebo_line | did | +0.02322 | 0.0054 (0.0054) | [+0.01006, +0.03637] | [+0.00840, +0.03805] | [+0.00841, +0.03804] | 1.127 | no / no / no | 3 | — |
| 288 | pickle | diag residual sts ts_demean W30 | trend_b_shared_slope | did | +0.02383 | 0.0045 (0.0045) | [+0.01115, +0.03671] | [+0.00909, +0.03848] | [+0.00919, +0.03846] | 1.150 | no / no / no | 2 | — |
| 289 | pickle | autocorr lag1 ts_gsr W60 | primary | did | −0.01465 | 0.0106 (0.0106) | [−0.02507, −0.00516] | [−0.02609, −0.00370] | [−0.02609, −0.00320] | 1.124 | no / no / no | 12 | S3_Text.md:153; draft_v2.md:156; draft_v2.md:78 |
| 290 | pickle | autocorr lag1 ts_gsr W60 | sensitivity | did | −0.01307 | 0.0211 (0.0211) | [−0.02306, −0.00322] | [−0.02434, −0.00217] | [−0.02438, −0.00176] | 1.117 | no / no / no | 10 | — |
| 291 | pickle | autocorr lag1 ts_gsr W60 | early | did | −0.02128 | 0.0006 (0.0006) | [−0.03036, −0.01248] | [−0.03156, −0.01132] | [−0.03151, −0.01105] | 1.132 | no / no / no | 13 | — |
| 292 | pickle | autocorr lag1 ts_gsr W60 | late | did | −0.00934 | 0.1615 (0.1615) | [−0.02135, +0.00215] | [−0.02295, +0.00372] | [−0.02286, +0.00419] | 1.134 | yes / yes / yes | 9 | — |
| 293 | pickle | autocorr lag1 ts_gsr W60 | trend_a_placebo_line | did | −0.01623 | 0.0049 (0.0049) | [−0.02618, −0.00692] | [−0.02706, −0.00563] | [−0.02714, −0.00533] | 1.112 | no / no / no | 12 | — |
| 294 | pickle | autocorr lag1 ts_gsr W60 | trend_b_shared_slope | did | −0.01901 | 0.0016 (0.0016) | [−0.02822, −0.01029] | [−0.02904, −0.00893] | [−0.02917, −0.00884] | 1.122 | no / no / no | 13 | — |
| 295 | pickle | sts tau1 ts_gsr W60 | primary | did | −0.08087 | 0.0038 (0.0038) | [−0.12611, −0.03769] | [−0.13174, −0.03102] | [−0.13207, −0.02967] | 1.139 | no / no / no | 13 | draft_v2.md:156; draft_v2.md:91 |
| 296 | pickle | sts tau1 ts_gsr W60 | sensitivity | did | −0.07334 | 0.0070 (0.0070) | [−0.11803, −0.02914] | [−0.12381, −0.02381] | [−0.12396, −0.02273] | 1.125 | no / no / no | 12 | supplementary.md:13 |
| 297 | pickle | sts tau1 ts_gsr W60 | early | did | −0.10285 | 0.0009 (0.0009) | [−0.14640, −0.06009] | [−0.15354, −0.05225] | [−0.15331, −0.05240] | 1.174 | no / no / no | 13 | — |
| 298 | pickle | sts tau1 ts_gsr W60 | late | did | −0.06328 | 0.0337 (0.0337) | [−0.11472, −0.01179] | [−0.12208, −0.00535] | [−0.12225, −0.00430] | 1.134 | no / no / no | 10 | — |
| 299 | pickle | sts tau1 ts_gsr W60 | trend_a_placebo_line | did | −0.08904 | 0.0021 (0.0021) | [−0.13474, −0.04610] | [−0.13871, −0.04016] | [−0.13908, −0.03900] | 1.112 | no / no / no | 13 | — |
| 300 | pickle | sts tau1 ts_gsr W60 | trend_b_shared_slope | did | −0.09953 | 0.0007 (0.0007) | [−0.14243, −0.05988] | [−0.14607, −0.05312] | [−0.14647, −0.05259] | 1.126 | no / no / no | 13 | — |
| 301 | pickle | sts tau1 ts_gsr global-bins | primary | did | −0.08008 | 0.0071 (0.0071) | [−0.13102, −0.03152] | [−0.13624, −0.02506] | [−0.13728, −0.02288] | 1.117 | no / no / no | 12 | draft_v2.md:156; draft_v2.md:76 |
| 302 | pickle | sts tau1 ts_gsr global-bins | sensitivity | did | −0.07730 | 0.0085 (0.0085) | [−0.12801, −0.02776] | [−0.13252, −0.02285] | [−0.13368, −0.02093] | 1.094 | no / no / no | 12 | — |
| 303 | pickle | sts tau1 ts_gsr global-bins | early | did | −0.10631 | 0.0009 (0.0009) | [−0.15454, −0.06124] | [−0.15973, −0.05438] | [−0.15967, −0.05295] | 1.129 | no / no / no | 13 | — |
| 304 | pickle | sts tau1 ts_gsr global-bins | late | did | −0.05910 | 0.0773 (0.0773) | [−0.11939, +0.00192] | [−0.12508, +0.00796] | [−0.12651, +0.00831] | 1.097 | yes / yes / yes | 10 | — |
| 305 | pickle | sts tau1 ts_gsr global-bins | trend_a_placebo_line | did | −0.08300 | 0.0070 (0.0070) | [−0.13538, −0.03216] | [−0.14052, −0.02597] | [−0.14184, −0.02415] | 1.110 | no / no / no | 13 | — |
| 306 | pickle | sts tau1 ts_gsr global-bins | trend_b_shared_slope | did | −0.09814 | 0.0020 (0.0020) | [−0.14811, −0.05078] | [−0.15249, −0.04477] | [−0.15326, −0.04302] | 1.107 | no / no / no | 13 | — |
| 307 | pickle | autocorr lag2 ts_gsr W60 | primary | did | −0.04676 | 0.0090 (0.0090) | [−0.07539, −0.01744] | [−0.07985, −0.01379] | [−0.08035, −0.01317] | 1.140 | no / no / no | 12 | draft_v2.md:157 |
| 308 | pickle | autocorr lag2 ts_gsr W60 | sensitivity | did | −0.04147 | 0.0176 (0.0176) | [−0.07116, −0.01232] | [−0.07443, −0.00838] | [−0.07496, −0.00797] | 1.122 | no / no / no | 11 | — |
| 309 | pickle | autocorr lag2 ts_gsr W60 | early | did | −0.06682 | 0.0006 (0.0006) | [−0.09441, −0.04117] | [−0.09694, −0.03695] | [−0.09702, −0.03661] | 1.127 | no / no / no | 13 | — |
| 310 | pickle | autocorr lag2 ts_gsr W60 | late | did | −0.03072 | 0.1198 (0.1198) | [−0.06563, +0.00380] | [−0.07035, +0.00897] | [−0.07073, +0.00928] | 1.142 | yes / yes / yes | 11 | — |
| 311 | pickle | autocorr lag2 ts_gsr W60 | trend_a_placebo_line | did | −0.05201 | 0.0042 (0.0042) | [−0.08004, −0.02308] | [−0.08434, −0.01947] | [−0.08463, −0.01938] | 1.139 | no / no / no | 12 | — |
| 312 | pickle | autocorr lag2 ts_gsr W60 | trend_b_shared_slope | did | −0.06083 | 0.0013 (0.0013) | [−0.08791, −0.03413] | [−0.09082, −0.03012] | [−0.09145, −0.03021] | 1.129 | no / no / no | 13 | — |
| 313 | pickle | sts tau2 ts_gsr W60 | primary | did | −0.04288 | 0.0037 (0.0037) | [−0.06537, −0.02044] | [−0.06917, −0.01734] | [−0.06915, −0.01660] | 1.154 | no / no / no | 12 | draft_v2.md:157 |
| 314 | pickle | sts tau2 ts_gsr W60 | sensitivity | did | −0.03884 | 0.0060 (0.0060) | [−0.06179, −0.01661] | [−0.06458, −0.01343] | [−0.06455, −0.01313] | 1.132 | no / no / no | 11 | — |
| 315 | pickle | sts tau2 ts_gsr W60 | early | did | −0.05426 | 0.0004 (0.0004) | [−0.07621, −0.03385] | [−0.07848, −0.03006] | [−0.07823, −0.03029] | 1.143 | no / no / no | 13 | — |
| 316 | pickle | sts tau2 ts_gsr W60 | late | did | −0.03377 | 0.0338 (0.0338) | [−0.06081, −0.00737] | [−0.06497, −0.00296] | [−0.06484, −0.00270] | 1.160 | no / no / no | 11 | — |
| 317 | pickle | sts tau2 ts_gsr W60 | trend_a_placebo_line | did | −0.04765 | 0.0015 (0.0015) | [−0.07079, −0.02525] | [−0.07356, −0.02196] | [−0.07372, −0.02159] | 1.133 | no / no / no | 13 | — |
| 318 | pickle | sts tau2 ts_gsr W60 | trend_b_shared_slope | did | −0.05363 | 0.0005 (0.0005) | [−0.07536, −0.03357] | [−0.07762, −0.03001] | [−0.07753, −0.02974] | 1.140 | no / no / no | 13 | — |
| 319 | pickle | sts tau2 ts_gsr global-bins | primary | did | −0.04851 | 0.0098 (0.0098) | [−0.08106, −0.01731] | [−0.08457, −0.01335] | [−0.08509, −0.01193] | 1.117 | no / no / no | 12 | draft_v2.md:157 |
| 320 | pickle | sts tau2 ts_gsr global-bins | sensitivity | did | −0.04647 | 0.0120 (0.0120) | [−0.07923, −0.01578] | [−0.08198, −0.01166] | [−0.08252, −0.01041] | 1.108 | no / no / no | 12 | — |
| 321 | pickle | sts tau2 ts_gsr global-bins | early | did | −0.06656 | 0.0011 (0.0011) | [−0.09714, −0.03748] | [−0.10019, −0.03412] | [−0.10022, −0.03289] | 1.108 | no / no / no | 12 | — |
| 322 | pickle | sts tau2 ts_gsr global-bins | late | did | −0.03408 | 0.1105 (0.1105) | [−0.07274, +0.00439] | [−0.07624, +0.00831] | [−0.07710, +0.00894] | 1.096 | yes / yes / yes | 9 | — |
| 323 | pickle | sts tau2 ts_gsr global-bins | trend_a_placebo_line | did | −0.05046 | 0.0103 (0.0103) | [−0.08461, −0.01847] | [−0.08792, −0.01350] | [−0.08835, −0.01257] | 1.125 | no / no / no | 13 | — |
| 324 | pickle | sts tau2 ts_gsr global-bins | trend_b_shared_slope | did | −0.06084 | 0.0020 (0.0020) | [−0.09307, −0.03039] | [−0.09602, −0.02612] | [−0.09635, −0.02532] | 1.115 | no / no / no | 13 | — |
| 325 | pickle | autocorr lag3 ts_gsr W60 | primary | did | −0.06808 | 0.0132 (0.0132) | [−0.11199, −0.02130] | [−0.11847, −0.01727] | [−0.11931, −0.01684] | 1.116 | no / no / no | 11 | draft_v2.md:158 |
| 326 | pickle | autocorr lag3 ts_gsr W60 | sensitivity | did | −0.05949 | 0.0258 (0.0258) | [−0.10255, −0.01392] | [−0.10957, −0.00862] | [−0.11058, −0.00840] | 1.139 | no / no / no | 10 | — |
| 327 | pickle | autocorr lag3 ts_gsr W60 | early | did | −0.09853 | 0.0005 (0.0005) | [−0.13855, −0.05935] | [−0.14390, −0.05321] | [−0.14405, −0.05301] | 1.145 | no / no / no | 13 | — |
| 328 | pickle | autocorr lag3 ts_gsr W60 | late | did | −0.04371 | 0.1506 (0.1506) | [−0.09594, +0.01193] | [−0.10448, +0.01822] | [−0.10553, +0.01811] | 1.138 | yes / yes / yes | 10 | — |
| 329 | pickle | autocorr lag3 ts_gsr W60 | trend_a_placebo_line | did | −0.07709 | 0.0070 (0.0070) | [−0.12069, −0.03162] | [−0.12669, −0.02607] | [−0.12794, −0.02625] | 1.130 | no / no / no | 12 | — |
| 330 | pickle | autocorr lag3 ts_gsr W60 | trend_b_shared_slope | did | −0.09140 | 0.0017 (0.0017) | [−0.13175, −0.04791] | [−0.13825, −0.04359] | [−0.13913, −0.04367] | 1.129 | no / no / no | 13 | — |
| 331 | pickle | sts tau3 ts_gsr W60 | primary | did | −0.00426 | 0.0018 (0.0018) | [−0.00635, −0.00223] | [−0.00660, −0.00192] | [−0.00660, −0.00193] | 1.139 | no / no / no | 12 | draft_v2.md:158 |
| 332 | pickle | sts tau3 ts_gsr W60 | sensitivity | did | −0.00395 | 0.0023 (0.0023) | [−0.00592, −0.00195] | [−0.00625, −0.00165] | [−0.00623, −0.00167] | 1.158 | no / no / no | 12 | — |
| 333 | pickle | sts tau3 ts_gsr W60 | early | did | −0.00459 | 0.0005 (0.0005) | [−0.00688, −0.00252] | [−0.00711, −0.00204] | [−0.00708, −0.00209] | 1.165 | no / no / no | 12 | — |
| 334 | pickle | sts tau3 ts_gsr W60 | late | did | −0.00400 | 0.0078 (0.0078) | [−0.00633, −0.00171] | [−0.00674, −0.00129] | [−0.00672, −0.00129] | 1.179 | no / no / no | 12 | — |
| 335 | pickle | sts tau3 ts_gsr W60 | trend_a_placebo_line | did | −0.00448 | 0.0004 (0.0004) | [−0.00626, −0.00279] | [−0.00653, −0.00245] | [−0.00651, −0.00245] | 1.176 | no / no / no | 13 | — |
| 336 | pickle | sts tau3 ts_gsr W60 | trend_b_shared_slope | did | −0.00475 | 0.0001 (0.0001) | [−0.00642, −0.00321] | [−0.00662, −0.00292] | [−0.00660, −0.00291] | 1.152 | no / no / no | 14 | — |
| 337 | pickle | sts tau3 ts_gsr global-bins | primary | did | −0.01157 | 0.0012 (0.0012) | [−0.01846, −0.00582] | [−0.01894, −0.00494] | [−0.01888, −0.00425] | 1.109 | no / no / no | 12 | draft_v2.md:158 |
| 338 | pickle | sts tau3 ts_gsr global-bins | sensitivity | did | −0.01099 | 0.0017 (0.0017) | [−0.01785, −0.00544] | [−0.01812, −0.00454] | [−0.01804, −0.00393] | 1.094 | no / no / no | 12 | — |
| 339 | pickle | sts tau3 ts_gsr global-bins | early | did | −0.01428 | 0.0006 (0.0006) | [−0.02090, −0.00842] | [−0.02157, −0.00753] | [−0.02148, −0.00709] | 1.125 | no / no / no | 13 | — |
| 340 | pickle | sts tau3 ts_gsr global-bins | late | did | −0.00939 | 0.0150 (0.0150) | [−0.01690, −0.00289] | [−0.01758, −0.00187] | [−0.01749, −0.00130] | 1.122 | no / no / no | 10 | — |
| 341 | pickle | sts tau3 ts_gsr global-bins | trend_a_placebo_line | did | −0.01244 | 0.0006 (0.0006) | [−0.01947, −0.00645] | [−0.02014, −0.00523] | [−0.02004, −0.00484] | 1.144 | no / no / no | 13 | — |
| 342 | pickle | sts tau3 ts_gsr global-bins | trend_b_shared_slope | did | −0.01379 | 0.0004 (0.0004) | [−0.02069, −0.00786] | [−0.02118, −0.00684] | [−0.02109, −0.00649] | 1.118 | no / no / no | 13 | — |
| 343 | pickle | autocorr lag5 ts_gsr W60 | primary | did | −0.01083 | 0.5670 (0.5670) | [−0.04526, +0.02635] | [−0.05143, +0.03037] | [−0.05156, +0.02989] | 1.142 | yes / yes / yes | 9 | draft_v2.md:159 |
| 344 | pickle | autocorr lag5 ts_gsr W60 | sensitivity | did | −0.00482 | 0.7964 (0.7964) | [−0.03885, +0.03137] | [−0.04531, +0.03605] | [−0.04514, +0.03551] | 1.159 | yes / yes / yes | 9 | — |
| 345 | pickle | autocorr lag5 ts_gsr W60 | early | did | −0.02993 | 0.0972 (0.0972) | [−0.06224, +0.00086] | [−0.06672, +0.00726] | [−0.06644, +0.00658] | 1.172 | yes / yes / yes | 9 | — |
| 346 | pickle | autocorr lag5 ts_gsr W60 | late | did | +0.00444 | 0.8593 (0.8593) | [−0.04154, +0.05324] | [−0.04900, +0.05933] | [−0.04942, +0.05830] | 1.143 | yes / yes / yes | 6 | — |
| 347 | pickle | autocorr lag5 ts_gsr W60 | trend_a_placebo_line | did | −0.02152 | 0.2922 (0.2922) | [−0.05792, +0.01628] | [−0.06426, +0.02185] | [−0.06431, +0.02126] | 1.160 | yes / yes / yes | 9 | — |
| 348 | pickle | autocorr lag5 ts_gsr W60 | trend_b_shared_slope | did | −0.03517 | 0.0729 (0.0729) | [−0.06788, −0.00080] | [−0.07461, +0.00396] | [−0.07401, +0.00367] | 1.171 | no / yes / yes, changes | 11 | — |
| 349 | pickle | sts tau5 ts_gsr W60 | primary | did | −0.00239 | 0.3688 (0.3688) | [−0.00732, +0.00223] | [−0.00814, +0.00320] | [−0.00794, +0.00316] | 1.187 | yes / yes / yes | 6 | draft_v2.md:159 |
| 350 | pickle | sts tau5 ts_gsr W60 | sensitivity | did | −0.00294 | 0.2689 (0.2689) | [−0.00784, +0.00173] | [−0.00860, +0.00255] | [−0.00840, +0.00251] | 1.164 | yes / yes / yes | 6 | — |
| 351 | pickle | sts tau5 ts_gsr W60 | early | did | +0.00043 | 0.8794 (0.8794) | [−0.00458, +0.00576] | [−0.00535, +0.00632] | [−0.00547, +0.00633] | 1.130 | yes / yes / yes | 9 | — |
| 352 | pickle | sts tau5 ts_gsr W60 | late | did | −0.00465 | 0.1697 (0.1697) | [−0.01111, +0.00113] | [−0.01151, +0.00195] | [−0.01151, +0.00221] | 1.099 | yes / yes / yes | 6 | — |
| 353 | pickle | sts tau5 ts_gsr W60 | trend_a_placebo_line | did | −0.00123 | 0.6401 (0.6401) | [−0.00600, +0.00289] | [−0.00647, +0.00367] | [−0.00641, +0.00394] | 1.140 | yes / yes / yes | 6 | — |
| 354 | pickle | sts tau5 ts_gsr W60 | trend_b_shared_slope | did | +0.00029 | 0.8948 (0.8948) | [−0.00387, +0.00404] | [−0.00436, +0.00474] | [−0.00431, +0.00488] | 1.152 | yes / yes / yes | 6 | — |
| 355 | pickle | sts tau5 ts_gsr global-bins | primary | did | +0.00152 | 0.7997 (0.7997) | [−0.00977, +0.01127] | [−0.01087, +0.01327] | [−0.01067, +0.01371] | 1.147 | yes / yes / yes | 4 | draft_v2.md:159 |
| 356 | pickle | sts tau5 ts_gsr global-bins | sensitivity | did | +0.00082 | 0.8910 (0.8910) | [−0.01086, +0.01054] | [−0.01179, +0.01279] | [−0.01159, +0.01322] | 1.148 | yes / yes / yes | 4 | — |
| 357 | pickle | sts tau5 ts_gsr global-bins | early | did | +0.01024 | 0.0205 (0.0205) | [+0.00283, +0.01711] | [+0.00202, +0.01842] | [+0.00200, +0.01848] | 1.149 | no / no / no | 3 | — |
| 358 | pickle | sts tau5 ts_gsr global-bins | late | did | −0.00546 | 0.5250 (0.5250) | [−0.02124, +0.00812] | [−0.02250, +0.01042] | [−0.02219, +0.01128] | 1.122 | yes / yes / yes | 8 | — |
| 359 | pickle | sts tau5 ts_gsr global-bins | trend_a_placebo_line | did | +0.00343 | 0.5835 (0.5835) | [−0.00827, +0.01359] | [−0.00965, +0.01588] | [−0.00950, +0.01636] | 1.169 | yes / yes / yes | 5 | — |
| 360 | pickle | sts tau5 ts_gsr global-bins | trend_b_shared_slope | did | +0.00948 | 0.0945 (0.0945) | [−0.00067, +0.01893] | [−0.00190, +0.02077] | [−0.00181, +0.02076] | 1.157 | yes / yes / yes | 3 | — |
| 361 | pickle | prewhiten arp MMI sts ts_gsr W60 | primary | did | −0.02620 | 0.1406 (0.1406) | [−0.05890, +0.00487] | [−0.06362, +0.01073] | [−0.06279, +0.01040] | 1.166 | yes / yes / yes | 8 | draft_v2.md:178; supplementary.md:260 |
| 362 | pickle | prewhiten arp MMI sts ts_gsr W60 | sensitivity | did | −0.01857 | 0.3035 (0.3035) | [−0.05102, +0.01412] | [−0.05702, +0.01966] | [−0.05635, +0.01921] | 1.177 | yes / yes / yes | 7 | — |
| 363 | pickle | prewhiten arp MMI sts ts_gsr W60 | early | did | −0.03793 | 0.1420 (0.1420) | [−0.08344, +0.00842] | [−0.09155, +0.01577] | [−0.09094, +0.01508] | 1.168 | yes / yes / yes | 8 | — |
| 364 | pickle | prewhiten arp MMI sts ts_gsr W60 | late | did | −0.01681 | 0.2518 (0.2518) | [−0.04393, +0.00857] | [−0.04726, +0.01299] | [−0.04677, +0.01316] | 1.148 | yes / yes / yes | 7 | — |
| 365 | pickle | prewhiten arp MMI sts ts_gsr W60 | trend_a_placebo_line | did | +0.02732 | 0.0291 (0.0291) | [+0.00669, +0.04750] | [+0.00353, +0.05118] | [+0.00368, +0.05096] | 1.167 | no / no / no | 4 | — |
| 366 | pickle | prewhiten arp MMI sts ts_gsr W60 | trend_b_shared_slope | did | +0.02595 | 0.0667 (0.0667) | [+0.00089, +0.05071] | [−0.00214, +0.05415] | [−0.00199, +0.05389] | 1.130 | no / yes / yes, changes | 4 | — |
| 367 | pickle | prewhiten arp MMI xtx+yty ts_gsr W60 | primary | did | −0.04143 | 0.0529 (0.0529) | [−0.07949, −0.00599] | [−0.08415, +0.00066] | [−0.08342, +0.00055] | 1.154 | no / yes / yes, changes | 8 | — |
| 368 | pickle | prewhiten arp MMI xtx+yty ts_gsr W60 | sensitivity | did | −0.03254 | 0.1240 (0.1240) | [−0.07043, +0.00364] | [−0.07611, +0.01037] | [−0.07530, +0.01021] | 1.167 | yes / yes / yes | 8 | — |
| 369 | pickle | prewhiten arp MMI xtx+yty ts_gsr W60 | early | did | −0.04294 | 0.1241 (0.1241) | [−0.09234, +0.00511] | [−0.09998, +0.01384] | [−0.09925, +0.01337] | 1.168 | yes / yes / yes | 8 | — |
| 370 | pickle | prewhiten arp MMI xtx+yty ts_gsr W60 | late | did | −0.04022 | 0.0284 (0.0284) | [−0.07574, −0.00993] | [−0.07848, −0.00403] | [−0.07789, −0.00256] | 1.131 | no / no / no | 9 | — |
| 371 | pickle | prewhiten arp MMI xtx+yty ts_gsr W60 | trend_a_placebo_line | did | +0.04973 | 0.0074 (0.0074) | [+0.02052, +0.07744] | [+0.01669, +0.08208] | [+0.01715, +0.08231] | 1.149 | no / no / no | 2 | — |
| 372 | pickle | prewhiten arp MMI xtx+yty ts_gsr W60 | trend_b_shared_slope | did | +0.07246 | 0.0023 (0.0023) | [+0.03757, +0.10303] | [+0.03459, +0.10872] | [+0.03543, +0.10949] | 1.132 | no / no / no | 2 | — |
| 373 | pickle | prewhiten arp CCS sts ts_gsr W60 | primary | did | −0.01346 | 0.0160 (0.0160) | [−0.02165, −0.00418] | [−0.02303, −0.00337] | [−0.02343, −0.00349] | 1.125 | no / no / no | 11 | draft_v2.md:178; supplementary.md:261 |
| 374 | pickle | prewhiten arp CCS sts ts_gsr W60 | sensitivity | did | −0.01342 | 0.0120 (0.0120) | [−0.02101, −0.00470] | [−0.02233, −0.00390] | [−0.02285, −0.00400] | 1.130 | no / no / no | 12 | — |
| 375 | pickle | prewhiten arp CCS sts ts_gsr W60 | early | did | −0.01926 | 0.0093 (0.0093) | [−0.03015, −0.00697] | [−0.03193, −0.00580] | [−0.03257, −0.00595] | 1.127 | no / no / no | 12 | — |
| 376 | pickle | prewhiten arp CCS sts ts_gsr W60 | late | did | −0.00881 | 0.1069 (0.1069) | [−0.01879, +0.00072] | [−0.01984, +0.00207] | [−0.01989, +0.00226] | 1.123 | yes / yes / yes | 9 | — |
| 377 | pickle | prewhiten arp CCS sts ts_gsr W60 | trend_a_placebo_line | did | −0.02317 | 0.0006 (0.0006) | [−0.03230, −0.01413] | [−0.03389, −0.01256] | [−0.03369, −0.01265] | 1.174 | no / no / no | 12 | — |
| 378 | pickle | prewhiten arp CCS sts ts_gsr W60 | trend_b_shared_slope | did | −0.02560 | 0.0004 (0.0004) | [−0.03396, −0.01685] | [−0.03556, −0.01563] | [−0.03543, −0.01577] | 1.165 | no / no / no | 13 | — |
| 379 | pickle | prewhiten arp autocorr ts_gsr W60 | primary | did | −0.05439 | 0.0520 (0.0520) | [−0.10234, −0.00534] | [−0.10772, +0.00056] | [−0.10952, +0.00074] | 1.116 | no / yes / yes, changes | 12 | supplementary.md:262 |
| 380 | pickle | prewhiten arp autocorr ts_gsr W60 | sensitivity | did | −0.04807 | 0.0955 (0.0955) | [−0.09627, +0.00338] | [−0.10238, +0.00889] | [−0.10528, +0.00915] | 1.117 | yes / yes / yes | 12 | — |
| 381 | pickle | prewhiten arp autocorr ts_gsr W60 | early | did | −0.03602 | 0.3232 (0.3232) | [−0.09599, +0.03396] | [−0.10521, +0.03925] | [−0.11088, +0.03884] | 1.112 | yes / yes / yes | 11 | — |
| 382 | pickle | prewhiten arp autocorr ts_gsr W60 | late | did | −0.06909 | 0.0059 (0.0059) | [−0.11476, −0.02798] | [−0.11817, −0.02260] | [−0.11811, −0.02008] | 1.101 | no / no / no | 10 | — |
| 383 | pickle | prewhiten arp autocorr ts_gsr W60 | trend_a_placebo_line | did | +0.09901 | 0.0009 (0.0009) | [+0.05857, +0.13472] | [+0.05514, +0.14111] | [+0.05549, +0.14252] | 1.129 | no / no / no | 1 | — |
| 384 | pickle | prewhiten arp autocorr ts_gsr W60 | trend_b_shared_slope | did | +0.16042 | 0.0001 (0.0001) | [+0.11517, +0.19992] | [+0.11083, +0.20985] | [+0.11149, +0.20934] | 1.168 | no / no / no | 0 | — |
| 385 | pickle | prewhiten arp diag observed sts ts_gsr W60 | primary | did | −0.02620 | 0.1406 (0.1406) | [−0.05890, +0.00487] | [−0.06362, +0.01073] | [−0.06279, +0.01040] | 1.166 | yes / yes / yes | 8 | draft_v2.md:178; supplementary.md:260 |
| 386 | pickle | prewhiten arp diag observed sts ts_gsr W60 | sensitivity | did | −0.01857 | 0.3035 (0.3035) | [−0.05102, +0.01412] | [−0.05702, +0.01966] | [−0.05635, +0.01921] | 1.177 | yes / yes / yes | 7 | — |
| 387 | pickle | prewhiten arp diag observed sts ts_gsr W60 | early | did | −0.03793 | 0.1420 (0.1420) | [−0.08344, +0.00842] | [−0.09155, +0.01577] | [−0.09094, +0.01508] | 1.168 | yes / yes / yes | 8 | — |
| 388 | pickle | prewhiten arp diag observed sts ts_gsr W60 | late | did | −0.01681 | 0.2518 (0.2518) | [−0.04393, +0.00857] | [−0.04726, +0.01299] | [−0.04677, +0.01316] | 1.148 | yes / yes / yes | 7 | — |
| 389 | pickle | prewhiten arp diag observed sts ts_gsr W60 | trend_a_placebo_line | did | +0.02732 | 0.0291 (0.0291) | [+0.00669, +0.04750] | [+0.00353, +0.05118] | [+0.00368, +0.05096] | 1.167 | no / no / no | 4 | — |
| 390 | pickle | prewhiten arp diag observed sts ts_gsr W60 | trend_b_shared_slope | did | +0.02595 | 0.0667 (0.0667) | [+0.00089, +0.05071] | [−0.00214, +0.05415] | [−0.00199, +0.05389] | 1.130 | no / yes / yes, changes | 4 | — |
| 391 | pickle | prewhiten arp diag predicted sts ts_gsr W60 | primary | did | −0.01922 | 0.3462 (0.3462) | [−0.05670, +0.01817] | [−0.06200, +0.02385] | [−0.06212, +0.02368] | 1.147 | yes / yes / yes | 7 | — |
| 392 | pickle | prewhiten arp diag predicted sts ts_gsr W60 | sensitivity | did | −0.01126 | 0.5784 (0.5784) | [−0.05009, +0.02640] | [−0.05492, +0.03291] | [−0.05488, +0.03236] | 1.148 | yes / yes / yes | 7 | — |
| 393 | pickle | prewhiten arp diag predicted sts ts_gsr W60 | early | did | −0.02059 | 0.5011 (0.5011) | [−0.07726, +0.03512] | [−0.08615, +0.04528] | [−0.08573, +0.04455] | 1.170 | yes / yes / yes | 7 | — |
| 394 | pickle | prewhiten arp diag predicted sts ts_gsr W60 | late | did | −0.01813 | 0.2458 (0.2458) | [−0.04672, +0.00844] | [−0.05061, +0.01342] | [−0.05005, +0.01380] | 1.161 | yes / yes / yes | 7 | — |
| 395 | pickle | prewhiten arp diag predicted sts ts_gsr W60 | trend_a_placebo_line | did | +0.06968 | 0.0010 (0.0010) | [+0.04202, +0.09638] | [+0.03832, +0.10088] | [+0.03884, +0.10051] | 1.151 | no / no / no | 3 | — |
| 396 | pickle | prewhiten arp diag predicted sts ts_gsr W60 | trend_b_shared_slope | did | +0.08407 | 0.0010 (0.0010) | [+0.05147, +0.11522] | [+0.04704, +0.12064] | [+0.04760, +0.12053] | 1.155 | no / no / no | 3 | — |
| 397 | pickle | prewhiten arp diag residual sts ts_gsr W60 | primary | did | −0.00697 | 0.3809 (0.3809) | [−0.02112, +0.00803] | [−0.02314, +0.00974] | [−0.02352, +0.00957] | 1.128 | yes / yes / yes | 8 | — |
| 398 | pickle | prewhiten arp diag residual sts ts_gsr W60 | sensitivity | did | −0.00731 | 0.3597 (0.3597) | [−0.02130, +0.00698] | [−0.02331, +0.00914] | [−0.02369, +0.00908] | 1.147 | yes / yes / yes | 9 | — |
| 399 | pickle | prewhiten arp diag residual sts ts_gsr W60 | early | did | −0.01734 | 0.0967 (0.0967) | [−0.03575, +0.00094] | [−0.03810, +0.00348] | [−0.03836, +0.00368] | 1.133 | yes / yes / yes | 11 | — |
| 400 | pickle | prewhiten arp diag residual sts ts_gsr W60 | late | did | +0.00132 | 0.8552 (0.8552) | [−0.01184, +0.01520] | [−0.01388, +0.01663] | [−0.01396, +0.01660] | 1.128 | yes / yes / yes | 8 | — |
| 401 | pickle | prewhiten arp diag residual sts ts_gsr W60 | trend_a_placebo_line | did | −0.04236 | 0.0004 (0.0004) | [−0.05677, −0.02780] | [−0.05924, −0.02544] | [−0.05915, −0.02558] | 1.166 | no / no / no | 13 | — |
| 402 | pickle | prewhiten arp diag residual sts ts_gsr W60 | trend_b_shared_slope | did | −0.05811 | 0.0001 (0.0001) | [−0.07356, −0.04189] | [−0.07636, −0.03988] | [−0.07631, −0.03992] | 1.152 | no / no / no | 14 | — |
| 403 | pickle | prewhiten arp MMI sts ts_gsr global-bins | primary | did | −0.02640 | 0.2736 (0.2736) | [−0.07001, +0.01589] | [−0.07708, +0.02369] | [−0.07646, +0.02367] | 1.173 | yes / yes / yes | 8 | supplementary.md:263 |
| 404 | pickle | prewhiten arp MMI sts ts_gsr global-bins | sensitivity | did | −0.02579 | 0.2906 (0.2906) | [−0.06980, +0.01747] | [−0.07694, +0.02506] | [−0.07653, +0.02495] | 1.169 | yes / yes / yes | 8 | — |
| 405 | pickle | prewhiten arp MMI sts ts_gsr global-bins | early | did | −0.02415 | 0.4121 (0.4121) | [−0.07776, +0.03005] | [−0.08719, +0.03931] | [−0.08665, +0.03836] | 1.173 | yes / yes / yes | 8 | — |
| 406 | pickle | prewhiten arp MMI sts ts_gsr global-bins | late | did | −0.02820 | 0.1753 (0.1753) | [−0.06772, +0.00634] | [−0.07088, +0.01258] | [−0.07053, +0.01413] | 1.127 | yes / yes / yes | 9 | — |
| 407 | pickle | prewhiten arp MMI sts ts_gsr global-bins | trend_a_placebo_line | did | −0.01593 | 0.3694 (0.3694) | [−0.04713, +0.01614] | [−0.05225, +0.02020] | [−0.05224, +0.02038] | 1.145 | yes / yes / yes | 10 | — |
| 408 | pickle | prewhiten arp MMI sts ts_gsr global-bins | trend_b_shared_slope | did | −0.01785 | 0.2981 (0.2981) | [−0.04783, +0.01416] | [−0.05286, +0.01819] | [−0.05353, +0.01783] | 1.146 | yes / yes / yes | 11 | — |
| 409 | pickle | prewhiten arp MMI xtx+yty ts_gsr global-bins | primary | did | −0.05929 | 0.0328 (0.0328) | [−0.10878, −0.01286] | [−0.11558, −0.00527] | [−0.11479, −0.00380] | 1.150 | no / no / no | 9 | — |
| 410 | pickle | prewhiten arp MMI xtx+yty ts_gsr global-bins | sensitivity | did | −0.05822 | 0.0377 (0.0377) | [−0.10872, −0.01134] | [−0.11492, −0.00361] | [−0.11420, −0.00224] | 1.143 | no / no / no | 9 | — |
| 411 | pickle | prewhiten arp MMI xtx+yty ts_gsr global-bins | early | did | −0.04961 | 0.1138 (0.1138) | [−0.10622, +0.00435] | [−0.11407, +0.01410] | [−0.11297, +0.01376] | 1.159 | yes / yes / yes | 8 | — |
| 412 | pickle | prewhiten arp MMI xtx+yty ts_gsr global-bins | late | did | −0.06704 | 0.0074 (0.0074) | [−0.11748, −0.02599] | [−0.11971, −0.01873] | [−0.11923, −0.01485] | 1.104 | no / no / no | 11 | — |
| 413 | pickle | prewhiten arp MMI xtx+yty ts_gsr global-bins | trend_a_placebo_line | did | −0.00420 | 0.8442 (0.8442) | [−0.04444, +0.03193] | [−0.04776, +0.03688] | [−0.04756, +0.03916] | 1.108 | yes / yes / yes | 6 | — |
| 414 | pickle | prewhiten arp MMI xtx+yty ts_gsr global-bins | trend_b_shared_slope | did | +0.01348 | 0.4829 (0.4829) | [−0.02318, +0.04752] | [−0.02709, +0.05343] | [−0.02695, +0.05391] | 1.139 | yes / yes / yes | 6 | — |
| 415 | pickle | prewhiten arp CCS sts ts_gsr global-bins | primary | did | −0.00451 | 0.2610 (0.2610) | [−0.01177, +0.00267] | [−0.01288, +0.00386] | [−0.01282, +0.00380] | 1.159 | yes / yes / yes | 7 | supplementary.md:264 |
| 416 | pickle | prewhiten arp CCS sts ts_gsr global-bins | sensitivity | did | −0.00459 | 0.2534 (0.2534) | [−0.01188, +0.00250] | [−0.01297, +0.00380] | [−0.01291, +0.00374] | 1.166 | yes / yes / yes | 8 | — |
| 417 | pickle | prewhiten arp CCS sts ts_gsr global-bins | early | did | −0.00614 | 0.1827 (0.1827) | [−0.01428, +0.00211] | [−0.01566, +0.00338] | [−0.01559, +0.00331] | 1.161 | yes / yes / yes | 8 | — |
| 418 | pickle | prewhiten arp CCS sts ts_gsr global-bins | late | did | −0.00321 | 0.4003 (0.4003) | [−0.01025, +0.00367] | [−0.01126, +0.00493] | [−0.01126, +0.00485] | 1.163 | yes / yes / yes | 8 | — |
| 419 | pickle | prewhiten arp CCS sts ts_gsr global-bins | trend_a_placebo_line | did | −0.00147 | 0.6646 (0.6646) | [−0.00780, +0.00479] | [−0.00874, +0.00574] | [−0.00868, +0.00574] | 1.150 | yes / yes / yes | 7 | — |
| 420 | pickle | prewhiten arp CCS sts ts_gsr global-bins | trend_b_shared_slope | did | −0.00349 | 0.2675 (0.2675) | [−0.00928, +0.00200] | [−0.01008, +0.00303] | [−0.01000, +0.00302] | 1.163 | yes / yes / yes | 7 | — |
| 421 | pickle | prewhiten arp autocorr ts_gsr global-bins | primary | did | −0.20436 | 0.0006 (0.0006) | [−0.29513, −0.12012] | [−0.30621, −0.10624] | [−0.30525, −0.10347] | 1.143 | no / no / no | 13 | supplementary.md:265 |
| 422 | pickle | prewhiten arp autocorr ts_gsr global-bins | sensitivity | did | −0.20190 | 0.0007 (0.0007) | [−0.29353, −0.11672] | [−0.30344, −0.10415] | [−0.30271, −0.10110] | 1.127 | no / no / no | 13 | — |
| 423 | pickle | prewhiten arp autocorr ts_gsr global-bins | early | did | −0.20264 | 0.0020 (0.0020) | [−0.30067, −0.10684] | [−0.31013, −0.09388] | [−0.31183, −0.09345] | 1.116 | no / no / no | 13 | — |
| 424 | pickle | prewhiten arp autocorr ts_gsr global-bins | late | did | −0.20574 | 0.0005 (0.0005) | [−0.30386, −0.12007] | [−0.30971, −0.10644] | [−0.30895, −0.10253] | 1.106 | no / no / no | 12 | — |
| 425 | pickle | prewhiten arp autocorr ts_gsr global-bins | trend_a_placebo_line | did | −0.09337 | 0.0552 (0.0552) | [−0.18313, −0.01200] | [−0.19237, +0.00186] | [−0.19100, +0.00425] | 1.135 | no / yes / yes, changes | 9 | — |
| 426 | pickle | prewhiten arp autocorr ts_gsr global-bins | trend_b_shared_slope | did | −0.05127 | 0.2946 (0.2946) | [−0.14294, +0.03200] | [−0.15264, +0.04796] | [−0.15176, +0.04922] | 1.147 | yes / yes / yes | 7 | — |
| 427 | pickle | prewhiten arp MMI sts ts_demean W60 | primary | did | −0.02744 | 0.1654 (0.1654) | [−0.06291, +0.00771] | [−0.06822, +0.01358] | [−0.06799, +0.01312] | 1.158 | yes / yes / yes | 9 | supplementary.md:266 |
| 428 | pickle | prewhiten arp MMI sts ts_demean W60 | sensitivity | did | −0.01788 | 0.3677 (0.3677) | [−0.05429, +0.01823] | [−0.06039, +0.02480] | [−0.06005, +0.02429] | 1.175 | yes / yes / yes | 8 | — |
| 429 | pickle | prewhiten arp MMI sts ts_demean W60 | early | did | −0.03852 | 0.1544 (0.1544) | [−0.08573, +0.01059] | [−0.09436, +0.01746] | [−0.09384, +0.01680] | 1.161 | yes / yes / yes | 9 | — |
| 430 | pickle | prewhiten arp MMI sts ts_demean W60 | late | did | −0.01857 | 0.2892 (0.2892) | [−0.05083, +0.01276] | [−0.05555, +0.01825] | [−0.05498, +0.01785] | 1.161 | yes / yes / yes | 7 | — |
| 431 | pickle | prewhiten arp MMI sts ts_demean W60 | trend_a_placebo_line | did | +0.01744 | 0.2413 (0.2413) | [−0.00983, +0.04425] | [−0.01416, +0.04874] | [−0.01370, +0.04859] | 1.163 | yes / yes / yes | 5 | — |
| 432 | pickle | prewhiten arp MMI sts ts_demean W60 | trend_b_shared_slope | did | +0.01594 | 0.3572 (0.3572) | [−0.01835, +0.04714] | [−0.02149, +0.05307] | [−0.02094, +0.05282] | 1.139 | yes / yes / yes | 5 | — |
| 433 | pickle | prewhiten arp MMI xtx+yty ts_demean W60 | primary | did | −0.03636 | 0.1979 (0.1979) | [−0.08932, +0.01221] | [−0.09452, +0.02094] | [−0.09386, +0.02114] | 1.137 | yes / yes / yes | 8 | — |
| 434 | pickle | prewhiten arp MMI xtx+yty ts_demean W60 | sensitivity | did | −0.02380 | 0.3838 (0.3838) | [−0.07329, +0.02288] | [−0.08116, +0.03216] | [−0.08032, +0.03271] | 1.178 | yes / yes / yes | 7 | — |
| 435 | pickle | prewhiten arp MMI xtx+yty ts_demean W60 | early | did | −0.03219 | 0.4449 (0.4449) | [−0.10807, +0.03764] | [−0.11827, +0.05034] | [−0.11709, +0.05271] | 1.157 | yes / yes / yes | 8 | — |
| 436 | pickle | prewhiten arp MMI xtx+yty ts_demean W60 | late | did | −0.03970 | 0.0862 (0.0862) | [−0.08081, −0.00018] | [−0.08618, +0.00654] | [−0.08564, +0.00623] | 1.150 | no / yes / yes, changes | 8 | — |
| 437 | pickle | prewhiten arp MMI xtx+yty ts_demean W60 | trend_a_placebo_line | did | +0.02883 | 0.2051 (0.2051) | [−0.01240, +0.07008] | [−0.01882, +0.07612] | [−0.01823, +0.07588] | 1.151 | yes / yes / yes | 6 | — |
| 438 | pickle | prewhiten arp MMI xtx+yty ts_demean W60 | trend_b_shared_slope | did | +0.04391 | 0.1221 (0.1221) | [−0.00721, +0.09244] | [−0.01458, +0.10141] | [−0.01350, +0.10132] | 1.164 | yes / yes / yes | 6 | — |
| 439 | pickle | prewhiten arp CCS sts ts_demean W60 | primary | did | −0.01681 | 0.1073 (0.1073) | [−0.03403, +0.00304] | [−0.03650, +0.00429] | [−0.03772, +0.00410] | 1.101 | yes / yes / yes | 10 | supplementary.md:267 |
| 440 | pickle | prewhiten arp CCS sts ts_demean W60 | sensitivity | did | −0.01749 | 0.0985 (0.0985) | [−0.03502, +0.00197] | [−0.03743, +0.00395] | [−0.03863, +0.00365] | 1.118 | yes / yes / yes | 10 | — |
| 441 | pickle | prewhiten arp CCS sts ts_demean W60 | early | did | −0.02912 | 0.1311 (0.1311) | [−0.06185, +0.00549] | [−0.06675, +0.00933] | [−0.06764, +0.00941] | 1.130 | yes / yes / yes | 10 | — |
| 442 | pickle | prewhiten arp CCS sts ts_demean W60 | late | did | −0.00697 | 0.3154 (0.3154) | [−0.01993, +0.00532] | [−0.02157, +0.00757] | [−0.02136, +0.00743] | 1.154 | yes / yes / yes | 8 | — |
| 443 | pickle | prewhiten arp CCS sts ts_demean W60 | trend_a_placebo_line | did | −0.01798 | 0.0293 (0.0293) | [−0.03123, −0.00434] | [−0.03350, −0.00223] | [−0.03356, −0.00240] | 1.163 | no / no / no | 11 | — |
| 444 | pickle | prewhiten arp CCS sts ts_demean W60 | trend_b_shared_slope | did | −0.01967 | 0.0461 (0.0461) | [−0.03632, −0.00224] | [−0.03894, −0.00038] | [−0.03897, −0.00036] | 1.131 | no / no / no | 10 | — |
| 445 | pickle | prewhiten arp autocorr ts_demean W60 | primary | did | −0.04179 | 0.3459 (0.3459) | [−0.12381, +0.03150] | [−0.13180, +0.04345] | [−0.13065, +0.04707] | 1.128 | yes / yes / yes | 9 | supplementary.md:268 |
| 446 | pickle | prewhiten arp autocorr ts_demean W60 | sensitivity | did | −0.03297 | 0.4507 (0.4507) | [−0.11439, +0.03956] | [−0.12269, +0.05142] | [−0.12167, +0.05574] | 1.131 | yes / yes / yes | 9 | — |
| 447 | pickle | prewhiten arp autocorr ts_demean W60 | early | did | −0.01942 | 0.7794 (0.7794) | [−0.15215, +0.09875] | [−0.16737, +0.12134] | [−0.16539, +0.12654] | 1.151 | yes / yes / yes | 7 | — |
| 448 | pickle | prewhiten arp autocorr ts_demean W60 | late | did | −0.05968 | 0.0319 (0.0319) | [−0.11059, −0.01207] | [−0.11648, −0.00545] | [−0.11611, −0.00326] | 1.127 | no / no / no | 10 | — |
| 449 | pickle | prewhiten arp autocorr ts_demean W60 | trend_a_placebo_line | did | +0.08427 | 0.0276 (0.0276) | [+0.01920, +0.14670] | [+0.01083, +0.15669] | [+0.01112, +0.15743] | 1.144 | no / no / no | 2 | — |
| 450 | pickle | prewhiten arp autocorr ts_demean W60 | trend_b_shared_slope | did | +0.13260 | 0.0099 (0.0099) | [+0.04657, +0.21053] | [+0.03939, +0.22497] | [+0.03906, +0.22613] | 1.132 | no / no / no | 2 | — |
| 451 | pickle | prewhiten arp diag observed sts ts_demean W60 | primary | did | −0.02744 | 0.1654 (0.1654) | [−0.06291, +0.00771] | [−0.06822, +0.01358] | [−0.06799, +0.01312] | 1.158 | yes / yes / yes | 9 | supplementary.md:266 |
| 452 | pickle | prewhiten arp diag observed sts ts_demean W60 | sensitivity | did | −0.01788 | 0.3677 (0.3677) | [−0.05429, +0.01823] | [−0.06039, +0.02480] | [−0.06005, +0.02429] | 1.175 | yes / yes / yes | 8 | — |
| 453 | pickle | prewhiten arp diag observed sts ts_demean W60 | early | did | −0.03852 | 0.1544 (0.1544) | [−0.08573, +0.01059] | [−0.09436, +0.01746] | [−0.09384, +0.01680] | 1.161 | yes / yes / yes | 9 | — |
| 454 | pickle | prewhiten arp diag observed sts ts_demean W60 | late | did | −0.01857 | 0.2892 (0.2892) | [−0.05083, +0.01276] | [−0.05555, +0.01825] | [−0.05498, +0.01785] | 1.161 | yes / yes / yes | 7 | — |
| 455 | pickle | prewhiten arp diag observed sts ts_demean W60 | trend_a_placebo_line | did | +0.01744 | 0.2413 (0.2413) | [−0.00983, +0.04425] | [−0.01416, +0.04874] | [−0.01370, +0.04859] | 1.163 | yes / yes / yes | 5 | — |
| 456 | pickle | prewhiten arp diag observed sts ts_demean W60 | trend_b_shared_slope | did | +0.01594 | 0.3572 (0.3572) | [−0.01835, +0.04714] | [−0.02149, +0.05307] | [−0.02094, +0.05282] | 1.139 | yes / yes / yes | 5 | — |
| 457 | pickle | prewhiten arp diag predicted sts ts_demean W60 | primary | did | −0.01316 | 0.6553 (0.6553) | [−0.06916, +0.03838] | [−0.07513, +0.04686] | [−0.07444, +0.04813] | 1.134 | yes / yes / yes | 7 | — |
| 458 | pickle | prewhiten arp diag predicted sts ts_demean W60 | sensitivity | did | −0.00065 | 0.9847 (0.9847) | [−0.05961, +0.05169] | [−0.06478, +0.06137] | [−0.06399, +0.06270] | 1.134 | yes / yes / yes | 7 | — |
| 459 | pickle | prewhiten arp diag predicted sts ts_demean W60 | early | did | −0.00641 | 0.8877 (0.8877) | [−0.09475, +0.07756] | [−0.10734, +0.09241] | [−0.10648, +0.09366] | 1.159 | yes / yes / yes | 7 | — |
| 460 | pickle | prewhiten arp diag predicted sts ts_demean W60 | late | did | −0.01855 | 0.3066 (0.3066) | [−0.05281, +0.01246] | [−0.05603, +0.01839] | [−0.05573, +0.01862] | 1.140 | yes / yes / yes | 7 | — |
| 461 | pickle | prewhiten arp diag predicted sts ts_demean W60 | trend_a_placebo_line | did | +0.05319 | 0.0253 (0.0253) | [+0.01181, +0.08990] | [+0.00805, +0.09729] | [+0.00867, +0.09771] | 1.143 | no / no / no | 3 | — |
| 462 | pickle | prewhiten arp diag predicted sts ts_demean W60 | trend_b_shared_slope | did | +0.06425 | 0.0348 (0.0348) | [+0.00977, +0.11181] | [+0.00576, +0.12113] | [+0.00655, +0.12195] | 1.131 | no / no / no | 3 | — |
| 463 | pickle | prewhiten arp diag residual sts ts_demean W60 | primary | did | −0.01428 | 0.4154 (0.4154) | [−0.04362, +0.02012] | [−0.04861, +0.02243] | [−0.05061, +0.02206] | 1.115 | yes / yes / yes | 9 | — |
| 464 | pickle | prewhiten arp diag residual sts ts_demean W60 | sensitivity | did | −0.01723 | 0.3363 (0.3363) | [−0.04839, +0.01674] | [−0.05240, +0.02037] | [−0.05442, +0.01995] | 1.117 | yes / yes / yes | 9 | — |
| 465 | pickle | prewhiten arp diag residual sts ts_demean W60 | early | did | −0.03211 | 0.2982 (0.2982) | [−0.08564, +0.02703] | [−0.09501, +0.03387] | [−0.09715, +0.03293] | 1.144 | yes / yes / yes | 9 | — |
| 466 | pickle | prewhiten arp diag residual sts ts_demean W60 | late | did | −0.00001 | 0.9987 (0.9987) | [−0.01467, +0.01665] | [−0.01708, +0.01798] | [−0.01781, +0.01779] | 1.120 | yes / yes / yes | 9 | — |
| 467 | pickle | prewhiten arp diag residual sts ts_demean W60 | trend_a_placebo_line | did | −0.03575 | 0.0194 (0.0194) | [−0.06057, −0.00968] | [−0.06384, −0.00697] | [−0.06466, −0.00683] | 1.118 | no / no / no | 11 | — |
| 468 | pickle | prewhiten arp diag residual sts ts_demean W60 | trend_b_shared_slope | did | −0.04831 | 0.0164 (0.0164) | [−0.08090, −0.01402] | [−0.08579, −0.01053] | [−0.08669, −0.00993] | 1.125 | no / no / no | 12 | — |
| 469 | pickle | prewhiten arp MMI sts ts_demean global-bins | primary | did | −0.02644 | 0.2831 (0.2831) | [−0.07182, +0.01555] | [−0.07697, +0.02280] | [−0.07653, +0.02364] | 1.142 | yes / yes / yes | 8 | supplementary.md:269 |
| 470 | pickle | prewhiten arp MMI sts ts_demean global-bins | sensitivity | did | −0.02548 | 0.3051 (0.3051) | [−0.07049, +0.01747] | [−0.07666, +0.02438] | [−0.07624, +0.02529] | 1.149 | yes / yes / yes | 8 | — |
| 471 | pickle | prewhiten arp MMI sts ts_demean global-bins | early | did | −0.02860 | 0.3615 (0.3615) | [−0.08854, +0.02308] | [−0.09317, +0.03373] | [−0.09234, +0.03514] | 1.137 | yes / yes / yes | 7 | — |
| 472 | pickle | prewhiten arp MMI sts ts_demean global-bins | late | did | −0.02472 | 0.2333 (0.2333) | [−0.06244, +0.01115] | [−0.06749, +0.01760] | [−0.06716, +0.01773] | 1.156 | yes / yes / yes | 8 | — |
| 473 | pickle | prewhiten arp MMI sts ts_demean global-bins | trend_a_placebo_line | did | −0.01465 | 0.4597 (0.4597) | [−0.05181, +0.01979] | [−0.05626, +0.02635] | [−0.05588, +0.02657] | 1.154 | yes / yes / yes | 9 | — |
| 474 | pickle | prewhiten arp MMI sts ts_demean global-bins | trend_b_shared_slope | did | −0.01842 | 0.3940 (0.3940) | [−0.05914, +0.01824] | [−0.06339, +0.02585] | [−0.06289, +0.02604] | 1.153 | yes / yes / yes | 8 | — |
| 475 | pickle | prewhiten arp MMI xtx+yty ts_demean global-bins | primary | did | −0.03878 | 0.2145 (0.2145) | [−0.09538, +0.01725] | [−0.10414, +0.02633] | [−0.10341, +0.02585] | 1.158 | yes / yes / yes | 9 | — |
| 476 | pickle | prewhiten arp MMI xtx+yty ts_demean global-bins | sensitivity | did | −0.03723 | 0.2302 (0.2302) | [−0.09368, +0.01914] | [−0.10283, +0.02785] | [−0.10181, +0.02734] | 1.158 | yes / yes / yes | 9 | — |
| 477 | pickle | prewhiten arp MMI xtx+yty ts_demean global-bins | early | did | −0.03380 | 0.3514 (0.3514) | [−0.10235, +0.03045] | [−0.11145, +0.04299] | [−0.11005, +0.04245] | 1.163 | yes / yes / yes | 8 | — |
| 478 | pickle | prewhiten arp MMI xtx+yty ts_demean global-bins | late | did | −0.04276 | 0.1434 (0.1434) | [−0.09572, +0.00888] | [−0.10257, +0.01663] | [−0.10213, +0.01661] | 1.140 | yes / yes / yes | 8 | — |
| 479 | pickle | prewhiten arp MMI xtx+yty ts_demean global-bins | trend_a_placebo_line | did | +0.00205 | 0.9362 (0.9362) | [−0.04458, +0.04925] | [−0.05202, +0.05600] | [−0.05175, +0.05585] | 1.151 | yes / yes / yes | 6 | — |
| 480 | pickle | prewhiten arp MMI xtx+yty ts_demean global-bins | trend_b_shared_slope | did | +0.01125 | 0.6427 (0.6427) | [−0.03452, +0.05517] | [−0.04075, +0.06337] | [−0.04087, +0.06336] | 1.161 | yes / yes / yes | 7 | — |
| 481 | pickle | prewhiten arp CCS sts ts_demean global-bins | primary | did | −0.00278 | 0.6385 (0.6385) | [−0.01352, +0.00818] | [−0.01545, +0.01003] | [−0.01544, +0.00988] | 1.174 | yes / yes / yes | 7 | supplementary.md:270 |
| 482 | pickle | prewhiten arp CCS sts ts_demean global-bins | sensitivity | did | −0.00285 | 0.6326 (0.6326) | [−0.01372, +0.00826] | [−0.01555, +0.00998] | [−0.01555, +0.00985] | 1.162 | yes / yes / yes | 7 | — |
| 483 | pickle | prewhiten arp CCS sts ts_demean global-bins | early | did | −0.00537 | 0.4556 (0.4556) | [−0.01822, +0.00757] | [−0.02010, +0.00955] | [−0.02034, +0.00960] | 1.150 | yes / yes / yes | 8 | — |
| 484 | pickle | prewhiten arp CCS sts ts_demean global-bins | late | did | −0.00070 | 0.9041 (0.9041) | [−0.01207, +0.00965] | [−0.01328, +0.01156] | [−0.01320, +0.01179] | 1.144 | yes / yes / yes | 6 | — |
| 485 | pickle | prewhiten arp CCS sts ts_demean global-bins | trend_a_placebo_line | did | +0.00025 | 0.9602 (0.9602) | [−0.00914, +0.00966] | [−0.01054, +0.01103] | [−0.01045, +0.01096] | 1.147 | yes / yes / yes | 6 | — |
| 486 | pickle | prewhiten arp CCS sts ts_demean global-bins | trend_b_shared_slope | did | −0.00372 | 0.4441 (0.4441) | [−0.01280, +0.00524] | [−0.01424, +0.00681] | [−0.01412, +0.00669] | 1.167 | yes / yes / yes | 7 | — |
| 487 | pickle | prewhiten arp autocorr ts_demean global-bins | primary | did | −0.14480 | 0.0162 (0.0162) | [−0.26721, −0.04050] | [−0.27716, −0.02563] | [−0.27544, −0.01415] | 1.109 | no / no / no | 11 | supplementary.md:271 |
| 488 | pickle | prewhiten arp autocorr ts_demean global-bins | sensitivity | did | −0.14127 | 0.0195 (0.0195) | [−0.26605, −0.03827] | [−0.27399, −0.02154] | [−0.27285, −0.00970] | 1.108 | no / no / no | 11 | — |
| 489 | pickle | prewhiten arp autocorr ts_demean global-bins | early | did | −0.13982 | 0.0610 (0.0610) | [−0.28901, −0.01329] | [−0.29825, +0.00576] | [−0.29648, +0.01683] | 1.103 | no / yes / yes, changes | 11 | — |
| 490 | pickle | prewhiten arp autocorr ts_demean global-bins | late | did | −0.14878 | 0.0104 (0.0104) | [−0.26254, −0.05261] | [−0.27019, −0.03724] | [−0.26855, −0.02901] | 1.110 | no / no / no | 11 | — |
| 491 | pickle | prewhiten arp autocorr ts_demean global-bins | trend_a_placebo_line | did | −0.05177 | 0.3805 (0.3805) | [−0.16050, +0.04397] | [−0.17008, +0.05913] | [−0.16855, +0.06502] | 1.121 | yes / yes / yes | 7 | — |
| 492 | pickle | prewhiten arp autocorr ts_demean global-bins | trend_b_shared_slope | did | −0.01824 | 0.7728 (0.7728) | [−0.13343, +0.08773] | [−0.14815, +0.10613] | [−0.14606, +0.10957] | 1.150 | yes / yes / yes | 6 | — |
| 493 | pickle | prewhiten ar1 MMI sts ts_gsr W60 | primary | did | −0.06199 | 0.0006 (0.0006) | [−0.08994, −0.03639] | [−0.09283, −0.03255] | [−0.09264, −0.03134] | 1.125 | no / no / no | 13 | supplementary.md:272 |
| 494 | pickle | prewhiten ar1 MMI sts ts_gsr W60 | sensitivity | did | −0.05801 | 0.0009 (0.0009) | [−0.08589, −0.03294] | [−0.08875, −0.02848] | [−0.08852, −0.02749] | 1.138 | no / no / no | 13 | — |
| 495 | pickle | prewhiten ar1 MMI sts ts_gsr W60 | early | did | −0.07296 | 0.0005 (0.0005) | [−0.10293, −0.04336] | [−0.10820, −0.03817] | [−0.10763, −0.03829] | 1.176 | no / no / no | 13 | — |
| 496 | pickle | prewhiten ar1 MMI sts ts_gsr W60 | late | did | −0.05321 | 0.0027 (0.0027) | [−0.08517, −0.02498] | [−0.08809, −0.02042] | [−0.08774, −0.01869] | 1.124 | no / no / no | 12 | — |
| 497 | pickle | prewhiten ar1 MMI sts ts_gsr W60 | trend_a_placebo_line | did | −0.06286 | 0.0002 (0.0002) | [−0.08923, −0.03982] | [−0.09131, −0.03661] | [−0.09106, −0.03466] | 1.107 | no / no / no | 13 | — |
| 498 | pickle | prewhiten ar1 MMI sts ts_gsr W60 | trend_b_shared_slope | did | −0.06576 | 0.0002 (0.0002) | [−0.09006, −0.04420] | [−0.09224, −0.04042] | [−0.09217, −0.03936] | 1.130 | no / no / no | 13 | — |
| 499 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr W60 | primary | did | −0.08175 | 0.0009 (0.0009) | [−0.12188, −0.04586] | [−0.12553, −0.04040] | [−0.12522, −0.03828] | 1.120 | no / no / no | 13 | — |
| 500 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr W60 | sensitivity | did | −0.07664 | 0.0015 (0.0015) | [−0.11638, −0.04134] | [−0.12004, −0.03506] | [−0.11981, −0.03346] | 1.133 | no / no / no | 13 | — |
| 501 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr W60 | early | did | −0.09425 | 0.0012 (0.0012) | [−0.13920, −0.05131] | [−0.14605, −0.04323] | [−0.14500, −0.04350] | 1.170 | no / no / no | 12 | — |
| 502 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr W60 | late | did | −0.07174 | 0.0023 (0.0023) | [−0.11427, −0.03532] | [−0.11698, −0.03004] | [−0.11695, −0.02654] | 1.101 | no / no / no | 12 | — |
| 503 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr W60 | trend_a_placebo_line | did | −0.08256 | 0.0004 (0.0004) | [−0.11865, −0.05127] | [−0.12136, −0.04744] | [−0.12095, −0.04418] | 1.097 | no / no / no | 13 | — |
| 504 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr W60 | trend_b_shared_slope | did | −0.08389 | 0.0004 (0.0004) | [−0.11820, −0.05358] | [−0.12129, −0.04819] | [−0.12110, −0.04668] | 1.131 | no / no / no | 13 | — |
| 505 | pickle | prewhiten ar1 CCS sts ts_gsr W60 | primary | did | −0.00566 | 0.0065 (0.0065) | [−0.00937, −0.00223] | [−0.00980, −0.00166] | [−0.00974, −0.00158] | 1.139 | no / no / no | 12 | supplementary.md:273 |
| 506 | pickle | prewhiten ar1 CCS sts ts_gsr W60 | sensitivity | did | −0.00494 | 0.0182 (0.0182) | [−0.00865, −0.00151] | [−0.00906, −0.00090] | [−0.00902, −0.00087] | 1.144 | no / no / no | 12 | — |
| 507 | pickle | prewhiten ar1 CCS sts ts_gsr W60 | early | did | −0.00747 | 0.0029 (0.0029) | [−0.01197, −0.00339] | [−0.01240, −0.00264] | [−0.01244, −0.00250] | 1.138 | no / no / no | 11 | — |
| 508 | pickle | prewhiten ar1 CCS sts ts_gsr W60 | late | did | −0.00421 | 0.0331 (0.0331) | [−0.00778, −0.00091] | [−0.00814, −0.00040] | [−0.00810, −0.00032] | 1.127 | no / no / no | 9 | — |
| 509 | pickle | prewhiten ar1 CCS sts ts_gsr W60 | trend_a_placebo_line | did | −0.00549 | 0.0033 (0.0033) | [−0.00884, −0.00258] | [−0.00912, −0.00203] | [−0.00907, −0.00192] | 1.133 | no / no / no | 10 | — |
| 510 | pickle | prewhiten ar1 CCS sts ts_gsr W60 | trend_b_shared_slope | did | −0.00579 | 0.0018 (0.0018) | [−0.00907, −0.00289] | [−0.00936, −0.00243] | [−0.00929, −0.00230] | 1.119 | no / no / no | 12 | — |
| 511 | pickle | prewhiten ar1 autocorr ts_gsr W60 | primary | did | −0.01963 | 0.0010 (0.0010) | [−0.02816, −0.01160] | [−0.02912, −0.01057] | [−0.02908, −0.01018] | 1.120 | no / no / no | 12 | supplementary.md:274 |
| 512 | pickle | prewhiten ar1 autocorr ts_gsr W60 | sensitivity | did | −0.01815 | 0.0013 (0.0013) | [−0.02652, −0.01011] | [−0.02770, −0.00880] | [−0.02765, −0.00864] | 1.152 | no / no / no | 12 | — |
| 513 | pickle | prewhiten ar1 autocorr ts_gsr W60 | early | did | −0.02469 | 0.0002 (0.0002) | [−0.03232, −0.01723] | [−0.03334, −0.01612] | [−0.03336, −0.01603] | 1.142 | no / no / no | 13 | — |
| 514 | pickle | prewhiten ar1 autocorr ts_gsr W60 | late | did | −0.01558 | 0.0139 (0.0139) | [−0.02619, −0.00513] | [−0.02785, −0.00375] | [−0.02772, −0.00345] | 1.144 | no / no / no | 11 | — |
| 515 | pickle | prewhiten ar1 autocorr ts_gsr W60 | trend_a_placebo_line | did | −0.01982 | 0.0002 (0.0002) | [−0.02772, −0.01263] | [−0.02844, −0.01163] | [−0.02839, −0.01124] | 1.114 | no / no / no | 13 | — |
| 516 | pickle | prewhiten ar1 autocorr ts_gsr W60 | trend_b_shared_slope | did | −0.02085 | 0.0002 (0.0002) | [−0.02763, −0.01460] | [−0.02834, −0.01354] | [−0.02838, −0.01332] | 1.136 | no / no / no | 13 | — |
| 517 | pickle | prewhiten ar1 diag observed sts ts_gsr W60 | primary | did | −0.06199 | 0.0006 (0.0006) | [−0.08994, −0.03639] | [−0.09283, −0.03255] | [−0.09264, −0.03134] | 1.125 | no / no / no | 13 | supplementary.md:272 |
| 518 | pickle | prewhiten ar1 diag observed sts ts_gsr W60 | sensitivity | did | −0.05801 | 0.0009 (0.0009) | [−0.08589, −0.03294] | [−0.08875, −0.02848] | [−0.08852, −0.02749] | 1.138 | no / no / no | 13 | — |
| 519 | pickle | prewhiten ar1 diag observed sts ts_gsr W60 | early | did | −0.07296 | 0.0005 (0.0005) | [−0.10293, −0.04336] | [−0.10820, −0.03817] | [−0.10763, −0.03829] | 1.176 | no / no / no | 13 | — |
| 520 | pickle | prewhiten ar1 diag observed sts ts_gsr W60 | late | did | −0.05321 | 0.0027 (0.0027) | [−0.08517, −0.02498] | [−0.08809, −0.02042] | [−0.08774, −0.01869] | 1.124 | no / no / no | 12 | — |
| 521 | pickle | prewhiten ar1 diag observed sts ts_gsr W60 | trend_a_placebo_line | did | −0.06286 | 0.0002 (0.0002) | [−0.08923, −0.03982] | [−0.09131, −0.03661] | [−0.09106, −0.03466] | 1.107 | no / no / no | 13 | — |
| 522 | pickle | prewhiten ar1 diag observed sts ts_gsr W60 | trend_b_shared_slope | did | −0.06576 | 0.0002 (0.0002) | [−0.09006, −0.04420] | [−0.09224, −0.04042] | [−0.09217, −0.03936] | 1.130 | no / no / no | 13 | — |
| 523 | pickle | prewhiten ar1 diag predicted sts ts_gsr W60 | primary | did | −0.06257 | 0.0005 (0.0005) | [−0.09075, −0.03672] | [−0.09383, −0.03251] | [−0.09369, −0.03145] | 1.135 | no / no / no | 13 | — |
| 524 | pickle | prewhiten ar1 diag predicted sts ts_gsr W60 | sensitivity | did | −0.05930 | 0.0010 (0.0010) | [−0.08668, −0.03349] | [−0.09029, −0.02927] | [−0.09012, −0.02849] | 1.147 | no / no / no | 13 | — |
| 525 | pickle | prewhiten ar1 diag predicted sts ts_gsr W60 | early | did | −0.07555 | 0.0004 (0.0004) | [−0.10466, −0.04771] | [−0.10835, −0.04280] | [−0.10813, −0.04296] | 1.151 | no / no / no | 13 | — |
| 526 | pickle | prewhiten ar1 diag predicted sts ts_gsr W60 | late | did | −0.05219 | 0.0072 (0.0072) | [−0.08644, −0.02121] | [−0.09048, −0.01586] | [−0.08980, −0.01457] | 1.144 | no / no / no | 11 | — |
| 527 | pickle | prewhiten ar1 diag predicted sts ts_gsr W60 | trend_a_placebo_line | did | −0.06224 | 0.0002 (0.0002) | [−0.08982, −0.03887] | [−0.09156, −0.03516] | [−0.09132, −0.03317] | 1.107 | no / no / no | 13 | — |
| 528 | pickle | prewhiten ar1 diag predicted sts ts_gsr W60 | trend_b_shared_slope | did | −0.06632 | 0.0002 (0.0002) | [−0.09027, −0.04543] | [−0.09239, −0.04119] | [−0.09230, −0.04033] | 1.142 | no / no / no | 13 | — |
| 529 | pickle | prewhiten ar1 diag residual sts ts_gsr W60 | primary | did | +0.00058 | 0.8635 (0.8635) | [−0.00512, +0.00546] | [−0.00567, +0.00621] | [−0.00560, +0.00676] | 1.123 | yes / yes / yes | 5 | — |
| 530 | pickle | prewhiten ar1 diag residual sts ts_gsr W60 | sensitivity | did | +0.00130 | 0.6805 (0.6805) | [−0.00444, +0.00588] | [−0.00478, +0.00670] | [−0.00473, +0.00732] | 1.112 | yes / yes / yes | 5 | — |
| 531 | pickle | prewhiten ar1 diag residual sts ts_gsr W60 | early | did | +0.00259 | 0.4104 (0.4104) | [−0.00360, +0.00784] | [−0.00398, +0.00864] | [−0.00388, +0.00905] | 1.103 | yes / yes / yes | 5 | — |
| 532 | pickle | prewhiten ar1 diag residual sts ts_gsr W60 | late | did | −0.00103 | 0.7716 (0.7716) | [−0.00756, +0.00412] | [−0.00764, +0.00501] | [−0.00754, +0.00549] | 1.083 | yes / yes / yes | 7 | — |
| 533 | pickle | prewhiten ar1 diag residual sts ts_gsr W60 | trend_a_placebo_line | did | −0.00062 | 0.8346 (0.8346) | [−0.00605, +0.00396] | [−0.00643, +0.00480] | [−0.00640, +0.00516] | 1.122 | yes / yes / yes | 5 | — |
| 534 | pickle | prewhiten ar1 diag residual sts ts_gsr W60 | trend_b_shared_slope | did | +0.00055 | 0.8324 (0.8324) | [−0.00455, +0.00477] | [−0.00475, +0.00547] | [−0.00473, +0.00583] | 1.097 | yes / yes / yes | 6 | — |
| 535 | pickle | prewhiten ar1 MMI sts ts_gsr global-bins | primary | did | −0.05590 | 0.0015 (0.0015) | [−0.08769, −0.02804] | [−0.09032, −0.02388] | [−0.09004, −0.02176] | 1.114 | no / no / no | 13 | supplementary.md:275 |
| 536 | pickle | prewhiten ar1 MMI sts ts_gsr global-bins | sensitivity | did | −0.05487 | 0.0017 (0.0017) | [−0.08695, −0.02701] | [−0.08894, −0.02303] | [−0.08878, −0.02097] | 1.099 | no / no / no | 13 | — |
| 537 | pickle | prewhiten ar1 MMI sts ts_gsr global-bins | early | did | −0.06530 | 0.0015 (0.0015) | [−0.10006, −0.03349] | [−0.10347, −0.02808] | [−0.10304, −0.02756] | 1.132 | no / no / no | 13 | — |
| 538 | pickle | prewhiten ar1 MMI sts ts_gsr global-bins | late | did | −0.04838 | 0.0076 (0.0076) | [−0.08275, −0.01827] | [−0.08573, −0.01390] | [−0.08543, −0.01133] | 1.114 | no / no / no | 12 | — |
| 539 | pickle | prewhiten ar1 MMI sts ts_gsr global-bins | trend_a_placebo_line | did | −0.05467 | 0.0009 (0.0009) | [−0.08534, −0.02906] | [−0.08779, −0.02501] | [−0.08757, −0.02178] | 1.116 | no / no / no | 13 | — |
| 540 | pickle | prewhiten ar1 MMI sts ts_gsr global-bins | trend_b_shared_slope | did | −0.05723 | 0.0006 (0.0006) | [−0.08600, −0.03310] | [−0.08804, −0.02934] | [−0.08787, −0.02659] | 1.110 | no / no / no | 13 | — |
| 541 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr global-bins | primary | did | −0.06756 | 0.0017 (0.0017) | [−0.10747, −0.03322] | [−0.11033, −0.02817] | [−0.11019, −0.02492] | 1.107 | no / no / no | 13 | — |
| 542 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr global-bins | sensitivity | did | −0.06637 | 0.0020 (0.0020) | [−0.10651, −0.03215] | [−0.10865, −0.02746] | [−0.10848, −0.02427] | 1.092 | no / no / no | 13 | — |
| 543 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr global-bins | early | did | −0.07453 | 0.0029 (0.0029) | [−0.11761, −0.03490] | [−0.12147, −0.02820] | [−0.12136, −0.02769] | 1.128 | no / no / no | 12 | — |
| 544 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr global-bins | late | did | −0.06198 | 0.0043 (0.0043) | [−0.10402, −0.02554] | [−0.10741, −0.02090] | [−0.10731, −0.01665] | 1.102 | no / no / no | 12 | — |
| 545 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr global-bins | trend_a_placebo_line | did | −0.06712 | 0.0006 (0.0006) | [−0.10536, −0.03632] | [−0.10665, −0.03158] | [−0.10690, −0.02734] | 1.087 | no / no / no | 13 | — |
| 546 | pickle | prewhiten ar1 MMI xtx+yty ts_gsr global-bins | trend_b_shared_slope | did | −0.06805 | 0.0007 (0.0007) | [−0.10345, −0.03766] | [−0.10580, −0.03355] | [−0.10594, −0.03015] | 1.098 | no / no / no | 13 | — |
| 547 | pickle | prewhiten ar1 CCS sts ts_gsr global-bins | primary | did | +0.01345 | 0.0005 (0.0005) | [+0.00860, +0.01856] | [+0.00774, +0.01925] | [+0.00767, +0.01922] | 1.156 | no / no / no | 1 | supplementary.md:276 |
| 548 | pickle | prewhiten ar1 CCS sts ts_gsr global-bins | sensitivity | did | +0.01312 | 0.0005 (0.0005) | [+0.00826, +0.01834] | [+0.00752, +0.01885] | [+0.00744, +0.01881] | 1.123 | no / no / no | 1 | — |
| 549 | pickle | prewhiten ar1 CCS sts ts_gsr global-bins | early | did | +0.01242 | 0.0002 (0.0002) | [+0.00815, +0.01699] | [+0.00736, +0.01759] | [+0.00731, +0.01754] | 1.158 | no / no / no | 1 | — |
| 550 | pickle | prewhiten ar1 CCS sts ts_gsr global-bins | late | did | +0.01426 | 0.0006 (0.0006) | [+0.00836, +0.02029] | [+0.00759, +0.02100] | [+0.00756, +0.02097] | 1.125 | no / no / no | 1 | — |
| 551 | pickle | prewhiten ar1 CCS sts ts_gsr global-bins | trend_a_placebo_line | did | +0.01557 | 0.0004 (0.0004) | [+0.01046, +0.02074] | [+0.00968, +0.02148] | [+0.00968, +0.02145] | 1.148 | no / no / no | 1 | — |
| 552 | pickle | prewhiten ar1 CCS sts ts_gsr global-bins | trend_b_shared_slope | did | +0.01535 | 0.0001 (0.0001) | [+0.01065, +0.02028] | [+0.00982, +0.02096] | [+0.00977, +0.02093] | 1.157 | no / no / no | 0 | — |
| 553 | pickle | prewhiten ar1 autocorr ts_gsr global-bins | primary | did | −0.31635 | 0.0004 (0.0004) | [−0.42567, −0.21571] | [−0.43751, −0.20191] | [−0.43587, −0.19684] | 1.122 | no / no / no | 13 | supplementary.md:277 |
| 554 | pickle | prewhiten ar1 autocorr ts_gsr global-bins | sensitivity | did | −0.31281 | 0.0004 (0.0004) | [−0.42356, −0.21447] | [−0.43200, −0.20085] | [−0.43009, −0.19552] | 1.105 | no / no / no | 13 | — |
| 555 | pickle | prewhiten ar1 autocorr ts_gsr global-bins | early | did | −0.32838 | 0.0002 (0.0002) | [−0.42361, −0.23722] | [−0.43612, −0.22369] | [−0.43569, −0.22107] | 1.140 | no / no / no | 13 | — |
| 556 | pickle | prewhiten ar1 autocorr ts_gsr global-bins | late | did | −0.30673 | 0.0006 (0.0006) | [−0.43346, −0.18892] | [−0.44459, −0.17424] | [−0.44354, −0.16993] | 1.106 | no / no / no | 13 | — |
| 557 | pickle | prewhiten ar1 autocorr ts_gsr global-bins | trend_a_placebo_line | did | −0.36370 | 0.0001 (0.0001) | [−0.47615, −0.25857] | [−0.48910, −0.24190] | [−0.48833, −0.23906] | 1.136 | no / no / no | 14 | — |
| 558 | pickle | prewhiten ar1 autocorr ts_gsr global-bins | trend_b_shared_slope | did | −0.38191 | 0.0001 (0.0001) | [−0.48854, −0.28142] | [−0.50263, −0.26366] | [−0.50141, −0.26241] | 1.154 | no / no / no | 14 | — |
| 559 | pickle | prewhiten ar1 MMI sts ts_demean W60 | primary | did | −0.07835 | 0.0004 (0.0004) | [−0.10700, −0.05007] | [−0.11103, −0.04649] | [−0.11089, −0.04581] | 1.134 | no / no / no | 13 | supplementary.md:278 |
| 560 | pickle | prewhiten ar1 MMI sts ts_demean W60 | sensitivity | did | −0.07153 | 0.0005 (0.0005) | [−0.09978, −0.04419] | [−0.10390, −0.03965] | [−0.10369, −0.03936] | 1.156 | no / no / no | 12 | — |
| 561 | pickle | prewhiten ar1 MMI sts ts_demean W60 | early | did | −0.08452 | 0.0005 (0.0005) | [−0.11489, −0.05428] | [−0.11916, −0.04989] | [−0.11901, −0.05002] | 1.143 | no / no / no | 13 | — |
| 562 | pickle | prewhiten ar1 MMI sts ts_demean W60 | late | did | −0.07342 | 0.0013 (0.0013) | [−0.10878, −0.04115] | [−0.11182, −0.03570] | [−0.11157, −0.03526] | 1.126 | no / no / no | 11 | — |
| 563 | pickle | prewhiten ar1 MMI sts ts_demean W60 | trend_a_placebo_line | did | −0.08149 | 0.0002 (0.0002) | [−0.11290, −0.05260] | [−0.11641, −0.04799] | [−0.11606, −0.04693] | 1.134 | no / no / no | 13 | — |
| 564 | pickle | prewhiten ar1 MMI sts ts_demean W60 | trend_b_shared_slope | did | −0.08022 | 0.0004 (0.0004) | [−0.11190, −0.05156] | [−0.11525, −0.04600] | [−0.11490, −0.04555] | 1.148 | no / no / no | 13 | — |
| 565 | pickle | prewhiten ar1 MMI xtx+yty ts_demean W60 | primary | did | −0.12586 | 0.0002 (0.0002) | [−0.17071, −0.08054] | [−0.17825, −0.07341] | [−0.17792, −0.07380] | 1.163 | no / no / no | 13 | — |
| 566 | pickle | prewhiten ar1 MMI xtx+yty ts_demean W60 | sensitivity | did | −0.11277 | 0.0004 (0.0004) | [−0.15634, −0.06809] | [−0.16383, −0.06196] | [−0.16325, −0.06230] | 1.154 | no / no / no | 13 | — |
| 567 | pickle | prewhiten ar1 MMI xtx+yty ts_demean W60 | early | did | −0.12828 | 0.0002 (0.0002) | [−0.17269, −0.08392] | [−0.17974, −0.07669] | [−0.17953, −0.07703] | 1.161 | no / no / no | 13 | — |
| 568 | pickle | prewhiten ar1 MMI xtx+yty ts_demean W60 | late | did | −0.12393 | 0.0011 (0.0011) | [−0.17952, −0.07043] | [−0.18668, −0.06166] | [−0.18603, −0.06182] | 1.146 | no / no / no | 11 | — |
| 569 | pickle | prewhiten ar1 MMI xtx+yty ts_demean W60 | trend_a_placebo_line | did | −0.12793 | 0.0002 (0.0002) | [−0.17431, −0.08275] | [−0.18062, −0.07474] | [−0.18065, −0.07521] | 1.156 | no / no / no | 13 | — |
| 570 | pickle | prewhiten ar1 MMI xtx+yty ts_demean W60 | trend_b_shared_slope | did | −0.12129 | 0.0004 (0.0004) | [−0.16811, −0.07456] | [−0.17503, −0.06682] | [−0.17502, −0.06756] | 1.157 | no / no / no | 13 | — |
| 571 | pickle | prewhiten ar1 CCS sts ts_demean W60 | primary | did | +0.00350 | 0.5170 (0.5170) | [−0.00440, +0.01303] | [−0.00573, +0.01370] | [−0.00658, +0.01358] | 1.114 | yes / yes / yes | 5 | supplementary.md:279 |
| 572 | pickle | prewhiten ar1 CCS sts ts_demean W60 | sensitivity | did | +0.00289 | 0.5889 (0.5889) | [−0.00453, +0.01155] | [−0.00556, +0.01237] | [−0.00649, +0.01227] | 1.115 | yes / yes / yes | 7 | — |
| 573 | pickle | prewhiten ar1 CCS sts ts_demean W60 | early | did | −0.00067 | 0.8812 (0.8812) | [−0.00845, +0.00771] | [−0.00980, +0.00866] | [−0.00998, +0.00865] | 1.142 | yes / yes / yes | 7 | — |
| 574 | pickle | prewhiten ar1 CCS sts ts_demean W60 | late | did | +0.00683 | 0.2977 (0.2977) | [−0.00331, +0.01874] | [−0.00529, +0.02000] | [−0.00604, +0.01971] | 1.147 | yes / yes / yes | 7 | — |
| 575 | pickle | prewhiten ar1 CCS sts ts_demean W60 | trend_a_placebo_line | did | +0.00350 | 0.5133 (0.5133) | [−0.00447, +0.01333] | [−0.00573, +0.01376] | [−0.00674, +0.01373] | 1.095 | yes / yes / yes | 6 | — |
| 576 | pickle | prewhiten ar1 CCS sts ts_demean W60 | trend_b_shared_slope | did | +0.00141 | 0.7903 (0.7903) | [−0.00560, +0.01039] | [−0.00690, +0.01076] | [−0.00787, +0.01069] | 1.104 | yes / yes / yes | 8 | — |
| 577 | pickle | prewhiten ar1 autocorr ts_demean W60 | primary | did | −0.02759 | 0.0004 (0.0004) | [−0.03702, −0.01821] | [−0.03837, −0.01681] | [−0.03839, −0.01679] | 1.146 | no / no / no | 13 | supplementary.md:280 |
| 578 | pickle | prewhiten ar1 autocorr ts_demean W60 | sensitivity | did | −0.02414 | 0.0006 (0.0006) | [−0.03335, −0.01450] | [−0.03497, −0.01318] | [−0.03502, −0.01325] | 1.156 | no / no / no | 12 | — |
| 579 | pickle | prewhiten ar1 autocorr ts_demean W60 | early | did | −0.02934 | 0.0001 (0.0001) | [−0.03948, −0.01980] | [−0.04055, −0.01806] | [−0.04049, −0.01820] | 1.143 | no / no / no | 14 | — |
| 580 | pickle | prewhiten ar1 autocorr ts_demean W60 | late | did | −0.02619 | 0.0020 (0.0020) | [−0.03830, −0.01416] | [−0.04000, −0.01238] | [−0.03996, −0.01242] | 1.144 | no / no / no | 12 | — |
| 581 | pickle | prewhiten ar1 autocorr ts_demean W60 | trend_a_placebo_line | did | −0.02747 | 0.0004 (0.0004) | [−0.03776, −0.01761] | [−0.03883, −0.01618] | [−0.03880, −0.01613] | 1.124 | no / no / no | 13 | — |
| 582 | pickle | prewhiten ar1 autocorr ts_demean W60 | trend_b_shared_slope | did | −0.02559 | 0.0004 (0.0004) | [−0.03542, −0.01604] | [−0.03672, −0.01441] | [−0.03678, −0.01440] | 1.151 | no / no / no | 13 | — |
| 583 | pickle | prewhiten ar1 diag observed sts ts_demean W60 | primary | did | −0.07835 | 0.0004 (0.0004) | [−0.10700, −0.05007] | [−0.11103, −0.04649] | [−0.11089, −0.04581] | 1.134 | no / no / no | 13 | supplementary.md:278 |
| 584 | pickle | prewhiten ar1 diag observed sts ts_demean W60 | sensitivity | did | −0.07153 | 0.0005 (0.0005) | [−0.09978, −0.04419] | [−0.10390, −0.03965] | [−0.10369, −0.03936] | 1.156 | no / no / no | 12 | — |
| 585 | pickle | prewhiten ar1 diag observed sts ts_demean W60 | early | did | −0.08452 | 0.0005 (0.0005) | [−0.11489, −0.05428] | [−0.11916, −0.04989] | [−0.11901, −0.05002] | 1.143 | no / no / no | 13 | — |
| 586 | pickle | prewhiten ar1 diag observed sts ts_demean W60 | late | did | −0.07342 | 0.0013 (0.0013) | [−0.10878, −0.04115] | [−0.11182, −0.03570] | [−0.11157, −0.03526] | 1.126 | no / no / no | 11 | — |
| 587 | pickle | prewhiten ar1 diag observed sts ts_demean W60 | trend_a_placebo_line | did | −0.08149 | 0.0002 (0.0002) | [−0.11290, −0.05260] | [−0.11641, −0.04799] | [−0.11606, −0.04693] | 1.134 | no / no / no | 13 | — |
| 588 | pickle | prewhiten ar1 diag observed sts ts_demean W60 | trend_b_shared_slope | did | −0.08022 | 0.0004 (0.0004) | [−0.11190, −0.05156] | [−0.11525, −0.04600] | [−0.11490, −0.04555] | 1.148 | no / no / no | 13 | — |
| 589 | pickle | prewhiten ar1 diag predicted sts ts_demean W60 | primary | did | −0.08674 | 0.0004 (0.0004) | [−0.11803, −0.05491] | [−0.12289, −0.05023] | [−0.12298, −0.05050] | 1.151 | no / no / no | 13 | — |
| 590 | pickle | prewhiten ar1 diag predicted sts ts_demean W60 | sensitivity | did | −0.07810 | 0.0005 (0.0005) | [−0.11001, −0.04695] | [−0.11504, −0.04141] | [−0.11441, −0.04180] | 1.167 | no / no / no | 12 | — |
| 591 | pickle | prewhiten ar1 diag predicted sts ts_demean W60 | early | did | −0.09010 | 0.0004 (0.0004) | [−0.12065, −0.05869] | [−0.12560, −0.05418] | [−0.12572, −0.05447] | 1.153 | no / no / no | 13 | — |
| 592 | pickle | prewhiten ar1 diag predicted sts ts_demean W60 | late | did | −0.08406 | 0.0015 (0.0015) | [−0.12403, −0.04571] | [−0.12915, −0.03911] | [−0.12875, −0.03936] | 1.150 | no / no / no | 12 | — |
| 593 | pickle | prewhiten ar1 diag predicted sts ts_demean W60 | trend_a_placebo_line | did | −0.08801 | 0.0005 (0.0005) | [−0.12311, −0.05570] | [−0.12660, −0.05041] | [−0.12641, −0.04961] | 1.130 | no / no / no | 13 | — |
| 594 | pickle | prewhiten ar1 diag predicted sts ts_demean W60 | trend_b_shared_slope | did | −0.08513 | 0.0005 (0.0005) | [−0.11887, −0.05248] | [−0.12330, −0.04701] | [−0.12346, −0.04679] | 1.149 | no / no / no | 13 | — |
| 595 | pickle | prewhiten ar1 diag residual sts ts_demean W60 | primary | did | +0.00839 | 0.0621 (0.0621) | [+0.00069, +0.01743] | [−0.00042, +0.01812] | [−0.00126, +0.01804] | 1.107 | no / yes / yes, changes | 4 | — |
| 596 | pickle | prewhiten ar1 diag residual sts ts_demean W60 | sensitivity | did | +0.00658 | 0.1774 (0.1774) | [−0.00125, +0.01577] | [−0.00260, +0.01656] | [−0.00331, +0.01646] | 1.126 | yes / yes / yes | 5 | — |
| 597 | pickle | prewhiten ar1 diag residual sts ts_demean W60 | early | did | +0.00558 | 0.2045 (0.2045) | [−0.00178, +0.01383] | [−0.00290, +0.01454] | [−0.00330, +0.01446] | 1.117 | yes / yes / yes | 5 | — |
| 598 | pickle | prewhiten ar1 diag residual sts ts_demean W60 | late | did | +0.01064 | 0.0830 (0.0830) | [+0.00078, +0.02194] | [−0.00138, +0.02323] | [−0.00180, +0.02307] | 1.163 | no / yes / yes, changes | 4 | — |
| 599 | pickle | prewhiten ar1 diag residual sts ts_demean W60 | trend_a_placebo_line | did | +0.00652 | 0.1510 (0.1510) | [−0.00073, +0.01555] | [−0.00189, +0.01602] | [−0.00296, +0.01599] | 1.100 | yes / yes / yes | 4 | — |
| 600 | pickle | prewhiten ar1 diag residual sts ts_demean W60 | trend_b_shared_slope | did | +0.00490 | 0.2882 (0.2882) | [−0.00196, +0.01346] | [−0.00309, +0.01400] | [−0.00412, +0.01392] | 1.109 | yes / yes / yes | 6 | — |
| 601 | pickle | prewhiten ar1 MMI sts ts_demean global-bins | primary | did | −0.08715 | 0.0020 (0.0020) | [−0.12889, −0.04543] | [−0.13503, −0.03866] | [−0.13522, −0.03908] | 1.155 | no / no / no | 13 | supplementary.md:281 |
| 602 | pickle | prewhiten ar1 MMI sts ts_demean global-bins | sensitivity | did | −0.08580 | 0.0021 (0.0021) | [−0.12679, −0.04413] | [−0.13338, −0.03772] | [−0.13353, −0.03807] | 1.157 | no / no / no | 13 | — |
| 603 | pickle | prewhiten ar1 MMI sts ts_demean global-bins | early | did | −0.08998 | 0.0020 (0.0020) | [−0.12997, −0.04835] | [−0.13558, −0.04318] | [−0.13596, −0.04401] | 1.132 | no / no / no | 12 | — |
| 604 | pickle | prewhiten ar1 MMI sts ts_demean global-bins | late | did | −0.08488 | 0.0045 (0.0045) | [−0.13696, −0.03660] | [−0.14238, −0.02836] | [−0.14191, −0.02785] | 1.136 | no / no / no | 12 | — |
| 605 | pickle | prewhiten ar1 MMI sts ts_demean global-bins | trend_a_placebo_line | did | −0.08873 | 0.0017 (0.0017) | [−0.13238, −0.04762] | [−0.13858, −0.03941] | [−0.13836, −0.03910] | 1.170 | no / no / no | 12 | — |
| 606 | pickle | prewhiten ar1 MMI sts ts_demean global-bins | trend_b_shared_slope | did | −0.08833 | 0.0029 (0.0029) | [−0.13174, −0.04415] | [−0.13820, −0.03833] | [−0.13844, −0.03822] | 1.140 | no / no / no | 12 | — |
| 607 | pickle | prewhiten ar1 MMI xtx+yty ts_demean global-bins | primary | did | −0.12619 | 0.0017 (0.0017) | [−0.18710, −0.06670] | [−0.19656, −0.05617] | [−0.19582, −0.05655] | 1.166 | no / no / no | 12 | — |
| 608 | pickle | prewhiten ar1 MMI xtx+yty ts_demean global-bins | sensitivity | did | −0.12426 | 0.0018 (0.0018) | [−0.18382, −0.06580] | [−0.19352, −0.05524] | [−0.19292, −0.05561] | 1.172 | no / no / no | 12 | — |
| 609 | pickle | prewhiten ar1 MMI xtx+yty ts_demean global-bins | early | did | −0.12465 | 0.0015 (0.0015) | [−0.18434, −0.06681] | [−0.19097, −0.05864] | [−0.19055, −0.05875] | 1.126 | no / no / no | 12 | — |
| 610 | pickle | prewhiten ar1 MMI xtx+yty ts_demean global-bins | late | did | −0.12741 | 0.0028 (0.0028) | [−0.20251, −0.05918] | [−0.21067, −0.04692] | [−0.20965, −0.04517] | 1.142 | no / no / no | 12 | — |
| 611 | pickle | prewhiten ar1 MMI xtx+yty ts_demean global-bins | trend_a_placebo_line | did | −0.12605 | 0.0017 (0.0017) | [−0.18613, −0.06851] | [−0.19421, −0.05710] | [−0.19494, −0.05716] | 1.166 | no / no / no | 13 | — |
| 612 | pickle | prewhiten ar1 MMI xtx+yty ts_demean global-bins | trend_b_shared_slope | did | −0.12337 | 0.0026 (0.0026) | [−0.18350, −0.06309] | [−0.19245, −0.05382] | [−0.19230, −0.05444] | 1.151 | no / no / no | 13 | — |
| 613 | pickle | prewhiten ar1 CCS sts ts_demean global-bins | primary | did | +0.02042 | 0.0004 (0.0004) | [+0.01214, +0.02984] | [+0.01060, +0.03070] | [+0.01025, +0.03059] | 1.136 | no / no / no | 1 | supplementary.md:282 |
| 614 | pickle | prewhiten ar1 CCS sts ts_demean global-bins | sensitivity | did | +0.02000 | 0.0002 (0.0002) | [+0.01186, +0.02929] | [+0.01043, +0.02994] | [+0.01012, +0.02988] | 1.119 | no / no / no | 1 | — |
| 615 | pickle | prewhiten ar1 CCS sts ts_demean global-bins | early | did | +0.01851 | 0.0001 (0.0001) | [+0.01260, +0.02537] | [+0.01152, +0.02606] | [+0.01112, +0.02591] | 1.138 | no / no / no | 0 | — |
| 616 | pickle | prewhiten ar1 CCS sts ts_demean global-bins | late | did | +0.02194 | 0.0011 (0.0011) | [+0.01138, +0.03400] | [+0.00956, +0.03501] | [+0.00907, +0.03481] | 1.125 | no / no / no | 2 | — |
| 617 | pickle | prewhiten ar1 CCS sts ts_demean global-bins | trend_a_placebo_line | did | +0.02345 | 0.0001 (0.0001) | [+0.01469, +0.03330] | [+0.01293, +0.03429] | [+0.01269, +0.03421] | 1.147 | no / no / no | 0 | — |
| 618 | pickle | prewhiten ar1 CCS sts ts_demean global-bins | trend_b_shared_slope | did | +0.02203 | 0.0001 (0.0001) | [+0.01471, +0.03008] | [+0.01320, +0.03105] | [+0.01313, +0.03093] | 1.161 | no / no / no | 0 | — |
| 619 | pickle | prewhiten ar1 autocorr ts_demean global-bins | primary | did | −0.24123 | 0.0013 (0.0013) | [−0.37621, −0.12509] | [−0.38718, −0.10653] | [−0.38606, −0.09639] | 1.118 | no / no / no | 13 | supplementary.md:283 |
| 620 | pickle | prewhiten ar1 autocorr ts_demean global-bins | sensitivity | did | −0.23535 | 0.0016 (0.0016) | [−0.37041, −0.11865] | [−0.38076, −0.10223] | [−0.37944, −0.09126] | 1.106 | no / no / no | 13 | — |
| 621 | pickle | prewhiten ar1 autocorr ts_demean global-bins | early | did | −0.25541 | 0.0020 (0.0020) | [−0.38491, −0.13424] | [−0.40080, −0.11208] | [−0.40034, −0.11049] | 1.152 | no / no / no | 10 | — |
| 622 | pickle | prewhiten ar1 autocorr ts_demean global-bins | late | did | −0.22988 | 0.0040 (0.0040) | [−0.39012, −0.09917] | [−0.39706, −0.07679] | [−0.39527, −0.06449] | 1.101 | no / no / no | 12 | — |
| 623 | pickle | prewhiten ar1 autocorr ts_demean global-bins | trend_a_placebo_line | did | −0.28808 | 0.0002 (0.0002) | [−0.42012, −0.17788] | [−0.43039, −0.15983] | [−0.42934, −0.14682] | 1.117 | no / no / no | 13 | — |
| 624 | pickle | prewhiten ar1 autocorr ts_demean global-bins | trend_b_shared_slope | did | −0.30742 | 0.0001 (0.0001) | [−0.44013, −0.19762] | [−0.44694, −0.17766] | [−0.44536, −0.16948] | 1.110 | no / no / no | 14 | — |
| 625 | pickle | sts ts_gsr W60 | primary | did | −0.08087 | 0.0038 (0.0038) | [−0.12611, −0.03769] | [−0.13174, −0.03102] | [−0.13207, −0.02967] | 1.139 | no / no / no | 13 | draft_v2.md:156; draft_v2.md:91 |
| 626 | pickle | sts ts_gsr W60 | sensitivity | did | −0.07334 | 0.0070 (0.0070) | [−0.11803, −0.02914] | [−0.12381, −0.02381] | [−0.12396, −0.02273] | 1.125 | no / no / no | 12 | supplementary.md:13 |
| 627 | pickle | sts ts_gsr W60 | early | did | −0.10285 | 0.0009 (0.0009) | [−0.14640, −0.06009] | [−0.15354, −0.05225] | [−0.15331, −0.05240] | 1.174 | no / no / no | 13 | — |
| 628 | pickle | sts ts_gsr W60 | late | did | −0.06328 | 0.0337 (0.0337) | [−0.11472, −0.01179] | [−0.12208, −0.00535] | [−0.12225, −0.00430] | 1.134 | no / no / no | 10 | — |
| 629 | pickle | sts ts_gsr W60 | trend_a_placebo_line | did | −0.08904 | 0.0021 (0.0021) | [−0.13474, −0.04610] | [−0.13871, −0.04016] | [−0.13908, −0.03900] | 1.112 | no / no / no | 13 | — |
| 630 | pickle | sts ts_gsr W60 | trend_b_shared_slope | did | −0.09953 | 0.0007 (0.0007) | [−0.14243, −0.05988] | [−0.14607, −0.05312] | [−0.14647, −0.05259] | 1.126 | no / no / no | 13 | — |
| 631 | pickle | PhiR ts_gsr W60 | primary | did | +0.00066 | 0.8971 (0.8971) | [−0.00778, +0.00996] | [−0.00934, +0.01121] | [−0.00976, +0.01108] | 1.159 | yes / yes / yes | 8 | S2_Text.md:5; draft_v2.md:165; draft_v2.md:171 |
| 632 | pickle | PhiR ts_gsr W60 | sensitivity | did | +0.00058 | 0.9094 (0.9094) | [−0.00738, +0.01014] | [−0.00898, +0.01073] | [−0.00947, +0.01063] | 1.125 | yes / yes / yes | 8 | — |
| 633 | pickle | PhiR ts_gsr W60 | early | did | +0.00047 | 0.9355 (0.9355) | [−0.00895, +0.01134] | [−0.01088, +0.01249] | [−0.01137, +0.01231] | 1.152 | yes / yes / yes | 8 | — |
| 634 | pickle | PhiR ts_gsr W60 | late | did | +0.00081 | 0.8663 (0.8663) | [−0.00840, +0.00990] | [−0.00959, +0.01104] | [−0.00964, +0.01127] | 1.127 | yes / yes / yes | 7 | — |
| 635 | pickle | PhiR ts_gsr W60 | trend_a_placebo_line | did | +0.00008 | 0.9862 (0.9862) | [−0.00822, +0.00878] | [−0.00948, +0.00971] | [−0.00957, +0.00973] | 1.129 | yes / yes / yes | 8 | — |
| 636 | pickle | PhiR ts_gsr W60 | trend_b_shared_slope | did | −0.00111 | 0.7822 (0.7822) | [−0.00839, +0.00692] | [−0.00971, +0.00758] | [−0.00975, +0.00752] | 1.130 | yes / yes / yes | 9 | — |
| 637 | pickle | autocorr ts_gsr W60 | primary | did | −0.01465 | 0.0106 (0.0106) | [−0.02507, −0.00516] | [−0.02609, −0.00370] | [−0.02609, −0.00320] | 1.124 | no / no / no | 12 | S3_Text.md:153; draft_v2.md:156; draft_v2.md:78 |
| 638 | pickle | autocorr ts_gsr W60 | sensitivity | did | −0.01307 | 0.0211 (0.0211) | [−0.02306, −0.00322] | [−0.02434, −0.00217] | [−0.02438, −0.00176] | 1.117 | no / no / no | 10 | — |
| 639 | pickle | autocorr ts_gsr W60 | early | did | −0.02128 | 0.0006 (0.0006) | [−0.03036, −0.01248] | [−0.03156, −0.01132] | [−0.03151, −0.01105] | 1.132 | no / no / no | 13 | — |
| 640 | pickle | autocorr ts_gsr W60 | late | did | −0.00934 | 0.1615 (0.1615) | [−0.02135, +0.00215] | [−0.02295, +0.00372] | [−0.02286, +0.00419] | 1.134 | yes / yes / yes | 9 | — |
| 641 | pickle | autocorr ts_gsr W60 | trend_a_placebo_line | did | −0.01623 | 0.0049 (0.0049) | [−0.02618, −0.00692] | [−0.02706, −0.00563] | [−0.02714, −0.00533] | 1.112 | no / no / no | 12 | — |
| 642 | pickle | autocorr ts_gsr W60 | trend_b_shared_slope | did | −0.01901 | 0.0016 (0.0016) | [−0.02822, −0.01029] | [−0.02904, −0.00893] | [−0.02917, −0.00884] | 1.122 | no / no / no | 13 | — |
| 643 | pickle | sts ts_gsr global-bins | primary | did | −0.08008 | 0.0071 (0.0071) | [−0.13102, −0.03152] | [−0.13624, −0.02506] | [−0.13728, −0.02288] | 1.117 | no / no / no | 12 | draft_v2.md:156; draft_v2.md:76 |
| 644 | pickle | sts ts_gsr global-bins | sensitivity | did | −0.07730 | 0.0085 (0.0085) | [−0.12801, −0.02776] | [−0.13252, −0.02285] | [−0.13368, −0.02093] | 1.094 | no / no / no | 12 | — |
| 645 | pickle | sts ts_gsr global-bins | early | did | −0.10631 | 0.0009 (0.0009) | [−0.15454, −0.06124] | [−0.15973, −0.05438] | [−0.15967, −0.05295] | 1.129 | no / no / no | 13 | — |
| 646 | pickle | sts ts_gsr global-bins | late | did | −0.05910 | 0.0773 (0.0773) | [−0.11939, +0.00192] | [−0.12508, +0.00796] | [−0.12651, +0.00831] | 1.097 | yes / yes / yes | 10 | — |
| 647 | pickle | sts ts_gsr global-bins | trend_a_placebo_line | did | −0.08300 | 0.0070 (0.0070) | [−0.13538, −0.03216] | [−0.14052, −0.02597] | [−0.14184, −0.02415] | 1.110 | no / no / no | 13 | — |
| 648 | pickle | sts ts_gsr global-bins | trend_b_shared_slope | did | −0.09814 | 0.0020 (0.0020) | [−0.14811, −0.05078] | [−0.15249, −0.04477] | [−0.15326, −0.04302] | 1.107 | no / no / no | 13 | — |
| 649 | pickle | PhiR ts_gsr global-bins | primary | did | −0.00623 | 0.0953 (0.0953) | [−0.01275, +0.00027] | [−0.01377, +0.00131] | [−0.01372, +0.00126] | 1.159 | yes / yes / yes | 9 | draft_v2.md:172 |
| 650 | pickle | PhiR ts_gsr global-bins | sensitivity | did | −0.00647 | 0.0756 (0.0756) | [−0.01274, −0.00028] | [−0.01378, +0.00081] | [−0.01369, +0.00074] | 1.172 | no / yes / yes, changes | 9 | — |
| 651 | pickle | PhiR ts_gsr global-bins | early | did | −0.00878 | 0.0370 (0.0370) | [−0.01572, −0.00171] | [−0.01682, −0.00071] | [−0.01677, −0.00078] | 1.150 | no / no / no | 9 | — |
| 652 | pickle | PhiR ts_gsr global-bins | late | did | −0.00419 | 0.2736 (0.2736) | [−0.01124, +0.00266] | [−0.01218, +0.00383] | [−0.01216, +0.00378] | 1.151 | yes / yes / yes | 9 | — |
| 653 | pickle | PhiR ts_gsr global-bins | trend_a_placebo_line | did | −0.00716 | 0.0652 (0.0652) | [−0.01406, −0.00060] | [−0.01489, +0.00056] | [−0.01485, +0.00052] | 1.148 | no / yes / yes, changes | 10 | — |
| 654 | pickle | PhiR ts_gsr global-bins | trend_b_shared_slope | did | −0.00898 | 0.0208 (0.0208) | [−0.01531, −0.00261] | [−0.01622, −0.00170] | [−0.01620, −0.00177] | 1.144 | no / no / no | 10 | — |
| 655 | pickle | autocorr ts_gsr run-standardised bins | primary | did | −0.45804 | 0.0001 (0.0001) | [−0.60185, −0.31997] | [−0.62150, −0.29744] | [−0.62048, −0.29559] | 1.150 | no / no / no | 14 | — |
| 656 | pickle | autocorr ts_gsr run-standardised bins | sensitivity | did | −0.45166 | 0.0002 (0.0002) | [−0.59681, −0.31712] | [−0.61273, −0.29327] | [−0.61141, −0.29191] | 1.142 | no / no / no | 13 | — |
| 657 | pickle | autocorr ts_gsr run-standardised bins | early | did | −0.50085 | 0.0001 (0.0001) | [−0.61576, −0.38716] | [−0.63294, −0.36950] | [−0.63318, −0.36851] | 1.152 | no / no / no | 14 | — |
| 658 | pickle | autocorr ts_gsr run-standardised bins | late | did | −0.42379 | 0.0009 (0.0009) | [−0.59569, −0.25507] | [−0.62039, −0.22920] | [−0.61872, −0.22886] | 1.148 | no / no / no | 12 | — |
| 659 | pickle | autocorr ts_gsr run-standardised bins | trend_a_placebo_line | did | −0.51887 | 0.0001 (0.0001) | [−0.67091, −0.37371] | [−0.69020, −0.34949] | [−0.68865, −0.34909] | 1.146 | no / no / no | 14 | — |
| 660 | pickle | autocorr ts_gsr run-standardised bins | trend_b_shared_slope | did | −0.55848 | 0.0001 (0.0001) | [−0.69894, −0.42041] | [−0.72215, −0.39535] | [−0.72027, −0.39669] | 1.173 | no / no / no | 14 | — |
| 661 | pickle | sts ts_demean W60 | primary | did | −0.10311 | 0.0026 (0.0026) | [−0.15585, −0.05224] | [−0.16293, −0.04352] | [−0.16274, −0.04349] | 1.153 | no / no / no | 12 | S1_Text.md:7; draft_v2.md:76; draft_v2.md:91 |
| 662 | pickle | sts ts_demean W60 | sensitivity | did | −0.09352 | 0.0039 (0.0039) | [−0.14310, −0.04256] | [−0.15060, −0.03610] | [−0.15074, −0.03631] | 1.139 | no / no / no | 12 | supplementary.md:13 |
| 663 | pickle | sts ts_demean W60 | early | did | −0.11825 | 0.0012 (0.0012) | [−0.16733, −0.06788] | [−0.17599, −0.06035] | [−0.17571, −0.06080] | 1.163 | no / no / no | 13 | — |
| 664 | pickle | sts ts_demean W60 | late | did | −0.09100 | 0.0128 (0.0128) | [−0.15222, −0.03192] | [−0.16052, −0.02217] | [−0.16022, −0.02178] | 1.150 | no / no / no | 11 | — |
| 665 | pickle | sts ts_demean W60 | trend_a_placebo_line | did | −0.11260 | 0.0018 (0.0018) | [−0.16903, −0.05953] | [−0.17502, −0.05127] | [−0.17486, −0.05034] | 1.130 | no / no / no | 13 | — |
| 666 | pickle | sts ts_demean W60 | trend_b_shared_slope | did | −0.11925 | 0.0012 (0.0012) | [−0.17357, −0.06826] | [−0.17958, −0.05864] | [−0.17956, −0.05894] | 1.148 | no / no / no | 13 | — |
| 667 | pickle | PhiR ts_demean W60 | primary | did | +0.01572 | 0.0853 (0.0853) | [+0.00097, +0.03264] | [−0.00240, +0.03411] | [−0.00246, +0.03390] | 1.153 | no / yes / yes, changes | 4 | draft_v2.md:173 |
| 668 | pickle | PhiR ts_demean W60 | sensitivity | did | +0.01361 | 0.1071 (0.1071) | [−0.00020, +0.02939] | [−0.00298, +0.03074] | [−0.00328, +0.03050] | 1.140 | yes / yes / yes | 5 | — |
| 669 | pickle | PhiR ts_demean W60 | early | did | +0.01274 | 0.1523 (0.1523) | [−0.00173, +0.02930] | [−0.00443, +0.03108] | [−0.00539, +0.03087] | 1.145 | yes / yes / yes | 5 | — |
| 670 | pickle | PhiR ts_demean W60 | late | did | +0.01810 | 0.0944 (0.0944) | [+0.00132, +0.03790] | [−0.00262, +0.03927] | [−0.00268, +0.03888] | 1.145 | no / yes / yes, changes | 5 | — |
| 671 | pickle | PhiR ts_demean W60 | trend_a_placebo_line | did | +0.01632 | 0.0441 (0.0441) | [+0.00334, +0.03033] | [+0.00053, +0.03202] | [+0.00077, +0.03187] | 1.167 | no / no / no | 4 | — |
| 672 | pickle | PhiR ts_demean W60 | trend_b_shared_slope | did | +0.01393 | 0.0797 (0.0797) | [+0.00054, +0.02796] | [−0.00190, +0.02990] | [−0.00185, +0.02971] | 1.159 | no / yes / yes, changes | 5 | — |
| 673 | pickle | autocorr ts_demean W60 | primary | did | −0.02157 | 0.0017 (0.0017) | [−0.03189, −0.01165] | [−0.03314, −0.01020] | [−0.03318, −0.00997] | 1.133 | no / no / no | 13 | S3_Text.md:153 |
| 674 | pickle | autocorr ts_demean W60 | sensitivity | did | −0.01811 | 0.0048 (0.0048) | [−0.02788, −0.00799] | [−0.02948, −0.00669] | [−0.02960, −0.00662] | 1.146 | no / no / no | 12 | — |
| 675 | pickle | autocorr ts_demean W60 | early | did | −0.02440 | 0.0005 (0.0005) | [−0.03308, −0.01575] | [−0.03440, −0.01445] | [−0.03441, −0.01439] | 1.151 | no / no / no | 12 | — |
| 676 | pickle | autocorr ts_demean W60 | late | did | −0.01931 | 0.0114 (0.0114) | [−0.03162, −0.00689] | [−0.03360, −0.00523] | [−0.03356, −0.00506] | 1.147 | no / no / no | 11 | — |
| 677 | pickle | autocorr ts_demean W60 | trend_a_placebo_line | did | −0.02284 | 0.0020 (0.0020) | [−0.03412, −0.01197] | [−0.03532, −0.01037] | [−0.03541, −0.01027] | 1.127 | no / no / no | 13 | — |
| 678 | pickle | autocorr ts_demean W60 | trend_b_shared_slope | did | −0.02345 | 0.0022 (0.0022) | [−0.03453, −0.01248] | [−0.03614, −0.01050] | [−0.03617, −0.01074] | 1.163 | no / no / no | 13 | — |
| 679 | pickle | sts ts_demean global-bins | primary | did | −0.10347 | 0.0132 (0.0132) | [−0.16868, −0.03648] | [−0.17838, −0.02666] | [−0.17948, −0.02746] | 1.148 | no / no / no | 11 | — |
| 680 | pickle | sts ts_demean global-bins | sensitivity | did | −0.09994 | 0.0139 (0.0139) | [−0.16408, −0.03382] | [−0.17355, −0.02415] | [−0.17494, −0.02493] | 1.147 | no / no / no | 11 | — |
| 681 | pickle | sts ts_demean global-bins | early | did | −0.12503 | 0.0034 (0.0034) | [−0.18455, −0.06200] | [−0.19399, −0.05409] | [−0.19507, −0.05498] | 1.142 | no / no / no | 12 | — |
| 682 | pickle | sts ts_demean global-bins | late | did | −0.08623 | 0.0594 (0.0594) | [−0.16400, −0.00778] | [−0.17488, +0.00295] | [−0.17548, +0.00303] | 1.138 | no / yes / yes, changes | 10 | — |
| 683 | pickle | sts ts_demean global-bins | trend_a_placebo_line | did | −0.10892 | 0.0093 (0.0093) | [−0.17579, −0.04239] | [−0.18568, −0.03091] | [−0.18666, −0.03117] | 1.160 | no / no / no | 13 | — |
| 684 | pickle | sts ts_demean global-bins | trend_b_shared_slope | did | −0.12388 | 0.0057 (0.0057) | [−0.19080, −0.05480] | [−0.19967, −0.04555] | [−0.20100, −0.04676] | 1.133 | no / no / no | 13 | — |
| 685 | pickle | PhiR ts_demean global-bins | primary | did | +0.01801 | 0.1177 (0.1177) | [−0.00021, +0.03799] | [−0.00403, +0.04052] | [−0.00410, +0.04013] | 1.166 | yes / yes / yes | 5 | draft_v2.md:174 |
| 686 | pickle | PhiR ts_demean global-bins | sensitivity | did | +0.01805 | 0.1171 (0.1171) | [−0.00014, +0.03780] | [−0.00395, +0.04059] | [−0.00404, +0.04014] | 1.174 | yes / yes / yes | 5 | — |
| 687 | pickle | PhiR ts_demean global-bins | early | did | +0.01356 | 0.2484 (0.2484) | [−0.00435, +0.03439] | [−0.00785, +0.03658] | [−0.00904, +0.03616] | 1.147 | yes / yes / yes | 5 | — |
| 688 | pickle | PhiR ts_demean global-bins | late | did | +0.02158 | 0.0856 (0.0856) | [+0.00108, +0.04452] | [−0.00322, +0.04707] | [−0.00350, +0.04665] | 1.158 | no / yes / yes, changes | 5 | — |
| 689 | pickle | PhiR ts_demean global-bins | trend_a_placebo_line | did | +0.01683 | 0.0837 (0.0837) | [+0.00157, +0.03390] | [−0.00232, +0.03612] | [−0.00227, +0.03594] | 1.189 | no / yes / yes, changes | 4 | — |
| 690 | pickle | PhiR ts_demean global-bins | trend_b_shared_slope | did | +0.01419 | 0.1350 (0.1350) | [−0.00124, +0.03058] | [−0.00459, +0.03320] | [−0.00457, +0.03295] | 1.187 | yes / yes / yes | 5 | — |
| 691 | pickle | autocorr ts_demean run-standardised bins | primary | did | −0.38456 | 0.0004 (0.0004) | [−0.54192, −0.24635] | [−0.55479, −0.22086] | [−0.55389, −0.21522] | 1.130 | no / no / no | 13 | — |
| 692 | pickle | autocorr ts_demean run-standardised bins | sensitivity | did | −0.37369 | 0.0005 (0.0005) | [−0.53062, −0.23563] | [−0.54279, −0.21206] | [−0.54123, −0.20614] | 1.121 | no / no / no | 12 | — |
| 693 | pickle | autocorr ts_demean run-standardised bins | early | did | −0.42023 | 0.0001 (0.0001) | [−0.55446, −0.29187] | [−0.57466, −0.26760] | [−0.57356, −0.26689] | 1.169 | no / no / no | 14 | — |
| 694 | pickle | autocorr ts_demean run-standardised bins | late | did | −0.35602 | 0.0011 (0.0011) | [−0.54549, −0.18493] | [−0.56204, −0.15773] | [−0.56014, −0.15190] | 1.121 | no / no / no | 11 | — |
| 695 | pickle | autocorr ts_demean run-standardised bins | trend_a_placebo_line | did | −0.44266 | 0.0001 (0.0001) | [−0.59850, −0.30306] | [−0.61232, −0.28042] | [−0.61071, −0.27460] | 1.123 | no / no / no | 14 | — |
| 696 | pickle | autocorr ts_demean run-standardised bins | trend_b_shared_slope | did | −0.48047 | 0.0001 (0.0001) | [−0.62677, −0.34561] | [−0.64353, −0.32254] | [−0.64140, −0.31954] | 1.142 | no / no / no | 14 | — |
| 697 | pickle | sts ts_gsr W30 | primary | did | −0.06863 | 0.0042 (0.0042) | [−0.10836, −0.02931] | [−0.11424, −0.02422] | [−0.11467, −0.02258] | 1.139 | no / no / no | 13 | S1_Text.md:17; supplementary.md:17 |
| 698 | pickle | sts ts_gsr W30 | sensitivity | did | −0.06585 | 0.0067 (0.0067) | [−0.10715, −0.02612] | [−0.11153, −0.02120] | [−0.11207, −0.01962] | 1.115 | no / no / no | 12 | supplementary.md:17 |
| 699 | pickle | sts ts_gsr W30 | early | did | −0.08394 | 0.0012 (0.0012) | [−0.12669, −0.04511] | [−0.13026, −0.03795] | [−0.13014, −0.03774] | 1.132 | no / no / no | 13 | — |
| 700 | pickle | sts ts_gsr W30 | late | did | −0.05638 | 0.0321 (0.0321) | [−0.10243, −0.01175] | [−0.10810, −0.00531] | [−0.10861, −0.00414] | 1.134 | no / no / no | 11 | — |
| 701 | pickle | sts ts_gsr W30 | trend_a_placebo_line | did | −0.07663 | 0.0021 (0.0021) | [−0.11468, −0.03862] | [−0.11939, −0.03430] | [−0.12013, −0.03312] | 1.119 | no / no / no | 13 | — |
| 702 | pickle | sts ts_gsr W30 | trend_b_shared_slope | did | −0.08492 | 0.0010 (0.0010) | [−0.12253, −0.04947] | [−0.12556, −0.04389] | [−0.12638, −0.04347] | 1.118 | no / no / no | 13 | — |
| 703 | pickle | autocorr ts_gsr W30 | primary | did | −0.01416 | 0.0165 (0.0165) | [−0.02328, −0.00439] | [−0.02492, −0.00321] | [−0.02511, −0.00322] | 1.150 | no / no / no | 13 | — |
| 704 | pickle | autocorr ts_gsr W30 | sensitivity | did | −0.01390 | 0.0210 (0.0210) | [−0.02342, −0.00400] | [−0.02490, −0.00270] | [−0.02505, −0.00276] | 1.143 | no / no / no | 11 | — |
| 705 | pickle | autocorr ts_gsr W30 | early | did | −0.02003 | 0.0020 (0.0020) | [−0.02885, −0.01071] | [−0.03022, −0.00959] | [−0.03039, −0.00967] | 1.137 | no / no / no | 12 | — |
| 706 | pickle | autocorr ts_gsr W30 | late | did | −0.00947 | 0.1274 (0.1274) | [−0.02015, +0.00158] | [−0.02193, +0.00317] | [−0.02203, +0.00309] | 1.155 | yes / yes / yes | 10 | — |
| 707 | pickle | autocorr ts_gsr W30 | trend_a_placebo_line | did | −0.01511 | 0.0089 (0.0089) | [−0.02366, −0.00588] | [−0.02506, −0.00478] | [−0.02545, −0.00477] | 1.140 | no / no / no | 12 | — |
| 708 | pickle | autocorr ts_gsr W30 | trend_b_shared_slope | did | −0.01775 | 0.0028 (0.0028) | [−0.02624, −0.00885] | [−0.02716, −0.00788] | [−0.02760, −0.00789] | 1.109 | no / no / no | 13 | — |
| 709 | pickle | PhiR_deconv ts_gsr W30 | primary | did | +0.03067 | 0.0023 (0.0023) | [+0.01480, +0.04715] | [+0.01234, +0.04943] | [+0.01205, +0.04930] | 1.147 | no / no / no | 2 | — |
| 710 | pickle | PhiR_deconv ts_gsr W30 | sensitivity | did | +0.03093 | 0.0024 (0.0024) | [+0.01523, +0.04758] | [+0.01246, +0.04964] | [+0.01235, +0.04951] | 1.149 | no / no / no | 2 | — |
| 711 | pickle | PhiR_deconv ts_gsr W30 | early | did | +0.03797 | 0.0023 (0.0023) | [+0.01846, +0.05905] | [+0.01465, +0.06128] | [+0.01479, +0.06114] | 1.149 | no / no / no | 1 | — |
| 712 | pickle | PhiR_deconv ts_gsr W30 | late | did | +0.02484 | 0.0042 (0.0042) | [+0.01117, +0.04033] | [+0.00889, +0.04166] | [+0.00820, +0.04148] | 1.124 | no / no / no | 2 | — |
| 713 | pickle | PhiR_deconv ts_gsr W30 | trend_a_placebo_line | did | +0.02826 | 0.0015 (0.0015) | [+0.01497, +0.04259] | [+0.01274, +0.04444] | [+0.01225, +0.04428] | 1.148 | no / no / no | 1 | — |
| 714 | pickle | PhiR_deconv ts_gsr W30 | trend_b_shared_slope | did | +0.03036 | 0.0006 (0.0006) | [+0.01742, +0.04391] | [+0.01559, +0.04537] | [+0.01533, +0.04538] | 1.124 | no / no / no | 1 | — |
| 715 | pickle | sts_deconv ts_gsr W30 | primary | did | −0.06707 | 0.0013 (0.0013) | [−0.10115, −0.03516] | [−0.10551, −0.03058] | [−0.10535, −0.02878] | 1.135 | no / no / no | 13 | — |
| 716 | pickle | sts_deconv ts_gsr W30 | sensitivity | did | −0.06636 | 0.0017 (0.0017) | [−0.10125, −0.03494] | [−0.10458, −0.02979] | [−0.10438, −0.02835] | 1.128 | no / no / no | 12 | — |
| 717 | pickle | sts_deconv ts_gsr W30 | early | did | −0.08013 | 0.0005 (0.0005) | [−0.11601, −0.04765] | [−0.11929, −0.04171] | [−0.11888, −0.04139] | 1.135 | no / no / no | 13 | — |
| 718 | pickle | sts_deconv ts_gsr W30 | late | did | −0.05661 | 0.0094 (0.0094) | [−0.09648, −0.02131] | [−0.10001, −0.01559] | [−0.09969, −0.01354] | 1.123 | no / no / no | 11 | — |
| 719 | pickle | sts_deconv ts_gsr W30 | trend_a_placebo_line | did | −0.06941 | 0.0009 (0.0009) | [−0.10258, −0.03987] | [−0.10556, −0.03496] | [−0.10552, −0.03331] | 1.126 | no / no / no | 13 | — |
| 720 | pickle | sts_deconv ts_gsr W30 | trend_b_shared_slope | did | −0.07085 | 0.0006 (0.0006) | [−0.10179, −0.04299] | [−0.10431, −0.03879] | [−0.10430, −0.03740] | 1.114 | no / no / no | 13 | — |
| 721 | pickle | PhiR_deconv ts_demean W30 | primary | did | +0.05088 | 0.0013 (0.0013) | [+0.02859, +0.07288] | [+0.02533, +0.07641] | [+0.02559, +0.07616] | 1.153 | no / no / no | 1 | — |
| 722 | pickle | PhiR_deconv ts_demean W30 | sensitivity | did | +0.05082 | 0.0015 (0.0015) | [+0.02883, +0.07219] | [+0.02509, +0.07642] | [+0.02546, +0.07617] | 1.184 | no / no / no | 2 | — |
| 723 | pickle | PhiR_deconv ts_demean W30 | early | did | +0.05008 | 0.0023 (0.0023) | [+0.02507, +0.07433] | [+0.02233, +0.07749] | [+0.02249, +0.07768] | 1.120 | no / no / no | 1 | — |
| 724 | pickle | PhiR_deconv ts_demean W30 | late | did | +0.05151 | 0.0017 (0.0017) | [+0.02677, +0.07843] | [+0.02196, +0.08232] | [+0.02153, +0.08149] | 1.168 | no / no / no | 3 | — |
| 725 | pickle | PhiR_deconv ts_demean W30 | trend_a_placebo_line | did | +0.05068 | 0.0006 (0.0006) | [+0.02893, +0.07271] | [+0.02529, +0.07622] | [+0.02551, +0.07584] | 1.163 | no / no / no | 1 | — |
| 726 | pickle | PhiR_deconv ts_demean W30 | trend_b_shared_slope | did | +0.04909 | 0.0012 (0.0012) | [+0.02756, +0.07025] | [+0.02453, +0.07394] | [+0.02468, +0.07351] | 1.157 | no / no / no | 2 | — |
| 727 | pickle | sts_deconv ts_demean W30 | primary | did | −0.07909 | 0.0007 (0.0007) | [−0.11622, −0.04556] | [−0.12018, −0.03999] | [−0.11995, −0.03823] | 1.135 | no / no / no | 12 | — |
| 728 | pickle | sts_deconv ts_demean W30 | sensitivity | did | −0.07813 | 0.0007 (0.0007) | [−0.11512, −0.04489] | [−0.11876, −0.03923] | [−0.11840, −0.03785] | 1.133 | no / no / no | 12 | — |
| 729 | pickle | sts_deconv ts_demean W30 | early | did | −0.08814 | 0.0004 (0.0004) | [−0.12513, −0.05489] | [−0.12792, −0.04946] | [−0.12756, −0.04873] | 1.117 | no / no / no | 13 | — |
| 730 | pickle | sts_deconv ts_demean W30 | late | did | −0.07184 | 0.0031 (0.0031) | [−0.11454, −0.03349] | [−0.11947, −0.02653] | [−0.11891, −0.02477] | 1.147 | no / no / no | 11 | — |
| 731 | pickle | sts_deconv ts_demean W30 | trend_a_placebo_line | did | −0.08194 | 0.0006 (0.0006) | [−0.12142, −0.04675] | [−0.12510, −0.04057] | [−0.12516, −0.03872] | 1.132 | no / no / no | 13 | — |
| 732 | pickle | sts_deconv ts_demean W30 | trend_b_shared_slope | did | −0.08107 | 0.0005 (0.0005) | [−0.11971, −0.04728] | [−0.12285, −0.04098] | [−0.12236, −0.03978] | 1.130 | no / no / no | 13 | — |
| 733 | pickle | PhiR ts_gsr W30 | primary | did | +0.00072 | 0.9155 (0.9155) | [−0.01085, +0.01353] | [−0.01278, +0.01485] | [−0.01325, +0.01469] | 1.133 | yes / yes / yes | 8 | — |
| 734 | pickle | PhiR ts_gsr W30 | sensitivity | did | +0.00026 | 0.9685 (0.9685) | [−0.01085, +0.01266] | [−0.01291, +0.01400] | [−0.01331, +0.01383] | 1.145 | yes / yes / yes | 8 | — |
| 735 | pickle | PhiR ts_gsr W30 | early | did | −0.00038 | 0.9623 (0.9623) | [−0.01325, +0.01457] | [−0.01600, +0.01591] | [−0.01646, +0.01570] | 1.147 | yes / yes / yes | 9 | — |
| 736 | pickle | PhiR ts_gsr W30 | late | did | +0.00160 | 0.8033 (0.8033) | [−0.00992, +0.01363] | [−0.01169, +0.01523] | [−0.01191, +0.01512] | 1.143 | yes / yes / yes | 6 | — |
| 737 | pickle | PhiR ts_gsr W30 | trend_a_placebo_line | did | +0.00123 | 0.8378 (0.8378) | [−0.00884, +0.01248] | [−0.01069, +0.01363] | [−0.01108, +0.01353] | 1.141 | yes / yes / yes | 6 | — |
| 738 | pickle | PhiR ts_gsr W30 | trend_b_shared_slope | did | +0.00038 | 0.9460 (0.9460) | [−0.00927, +0.01113] | [−0.01083, +0.01199] | [−0.01112, +0.01187] | 1.118 | yes / yes / yes | 7 | — |
| 739 | engine | sts ts_gsr W60 | primary | dmt_change | −0.04847 | 0.0267 (0.0267) | [−0.08195, −0.01130] | [−0.08824, −0.00676] | [−0.08942, −0.00752] | 1.153 | no / no / no | 11 | draft_v2.md:89 |
| 740 | engine | sts ts_gsr W60 | primary | pcb_change | +0.03240 | 0.0425 (0.0425) | [+0.00531, +0.06060] | [+0.00133, +0.06376] | [+0.00129, +0.06350] | 1.129 | no / no / no | 4 | draft_v2.md:90 |
| 741 | engine | sts ts_gsr W60 | primary | fd_did | +0.01435 | 0.2452 (0.2452) | [−0.00704, +0.03646] | [−0.01147, +0.04026] | [−0.01116, +0.03985] | 1.189 | yes / yes / yes | 6 | draft_v2.md:92 |
| 742 | engine | sts ts_gsr W60 | primary | resid_did | −0.06491 | 0.0048 (0.0048) | [−0.09662, −0.02889] | [−0.10096, −0.02600] | [−0.10348, −0.02634] | 1.107 | no / no / no | 13 | S1_Text.md:7; draft_v2.md:76; draft_v2.md:93 |
| 743 | engine | sts ts_gsr W60 | sensitivity | dmt_change | −0.04914 | 0.0227 (0.0227) | [−0.08227, −0.01278] | [−0.08770, −0.00889] | [−0.08910, −0.00918] | 1.134 | no / no / no | 11 | supplementary.md:11 |
| 744 | engine | sts ts_gsr W60 | sensitivity | pcb_change | +0.02420 | 0.1040 (0.1040) | [−0.00196, +0.04958] | [−0.00597, +0.05441] | [−0.00585, +0.05425] | 1.171 | yes / yes / yes | 4 | supplementary.md:12 |
| 745 | engine | sts ts_gsr W60 | sensitivity | fd_did | +0.01911 | 0.1083 (0.1083) | [−0.00080, +0.04023] | [−0.00498, +0.04335] | [−0.00477, +0.04299] | 1.178 | yes / yes / yes | 6 | supplementary.md:14 |
| 746 | engine | sts ts_gsr W60 | sensitivity | resid_did | −0.05548 | 0.0100 (0.0100) | [−0.08639, −0.02102] | [−0.09088, −0.01740] | [−0.09324, −0.01773] | 1.124 | no / no / no | 13 | supplementary.md:15 |
| 747 | engine | sts ts_demean W60 | primary | dmt_change | −0.06333 | 0.0333 (0.0333) | [−0.10880, −0.01228] | [−0.11749, −0.00660] | [−0.11958, −0.00709] | 1.149 | no / no / no | 10 | draft_v2.md:89 |
| 748 | engine | sts ts_demean W60 | primary | pcb_change | +0.03978 | 0.0306 (0.0306) | [+0.00894, +0.06919] | [+0.00511, +0.07425] | [+0.00537, +0.07419] | 1.148 | no / no / no | 3 | draft_v2.md:90 |
| 749 | engine | sts ts_demean W60 | primary | fd_did | +0.01435 | 0.2452 (0.2452) | [−0.00704, +0.03646] | [−0.01147, +0.04026] | [−0.01116, +0.03985] | 1.189 | yes / yes / yes | 6 | draft_v2.md:92 |
| 750 | engine | sts ts_demean W60 | primary | resid_did | −0.08242 | 0.0048 (0.0048) | [−0.12237, −0.03723] | [−0.13018, −0.03220] | [−0.13148, −0.03336] | 1.151 | no / no / no | 13 | draft_v2.md:93 |
| 751 | engine | sts ts_demean W60 | sensitivity | dmt_change | −0.06209 | 0.0300 (0.0300) | [−0.10553, −0.01301] | [−0.11375, −0.00773] | [−0.11604, −0.00813] | 1.146 | no / no / no | 10 | supplementary.md:11 |
| 752 | engine | sts ts_demean W60 | sensitivity | pcb_change | +0.03144 | 0.0637 (0.0637) | [+0.00134, +0.05849] | [−0.00210, +0.06457] | [−0.00179, +0.06466] | 1.167 | no / yes / yes, changes | 4 | supplementary.md:12 |
| 753 | engine | sts ts_demean W60 | sensitivity | fd_did | +0.01911 | 0.1083 (0.1083) | [−0.00080, +0.04023] | [−0.00498, +0.04335] | [−0.00477, +0.04299] | 1.178 | yes / yes / yes | 6 | supplementary.md:14 |
| 754 | engine | sts ts_demean W60 | sensitivity | resid_did | −0.07138 | 0.0073 (0.0073) | [−0.11057, −0.02978] | [−0.11704, −0.02369] | [−0.11832, −0.02444] | 1.156 | no / no / no | 12 | supplementary.md:15 |
| 755 | engine | sts ts_gsr W30 | primary | dmt_change | −0.03902 | 0.0354 (0.0354) | [−0.06800, −0.00584] | [−0.07275, −0.00338] | [−0.07438, −0.00366] | 1.116 | no / no / no | 11 | supplementary.md:17 |
| 756 | engine | sts ts_gsr W30 | primary | pcb_change | +0.02961 | 0.0269 (0.0269) | [+0.00760, +0.05314] | [+0.00414, +0.05603] | [+0.00372, +0.05549] | 1.139 | no / no / no | 4 | supplementary.md:17 |
| 757 | engine | sts ts_gsr W30 | primary | fd_did | +0.01435 | 0.2452 (0.2452) | [−0.00696, +0.03683] | [−0.01147, +0.04026] | [−0.01116, +0.03985] | 1.181 | yes / yes / yes | 6 | — |
| 758 | engine | sts ts_gsr W30 | primary | resid_did | −0.05448 | 0.0065 (0.0065) | [−0.08363, −0.02153] | [−0.08753, −0.01867] | [−0.08981, −0.01915] | 1.109 | no / no / no | 13 | supplementary.md:17 |
| 759 | engine | sts ts_gsr W30 | sensitivity | dmt_change | −0.04069 | 0.0311 (0.0311) | [−0.06977, −0.00843] | [−0.07412, −0.00513] | [−0.07606, −0.00531] | 1.125 | no / no / no | 12 | — |
| 760 | engine | sts ts_gsr W30 | sensitivity | pcb_change | +0.02516 | 0.0490 (0.0490) | [+0.00348, +0.04763] | [+0.00022, +0.05068] | [−0.00016, +0.05048] | 1.143 | no / no / yes | 4 | — |
| 761 | engine | sts ts_gsr W30 | sensitivity | fd_did | +0.01740 | 0.1550 (0.1550) | [−0.00376, +0.03933] | [−0.00774, +0.04265] | [−0.00751, +0.04231] | 1.169 | yes / yes / yes | 6 | — |
| 762 | engine | sts ts_gsr W30 | sensitivity | resid_did | −0.05136 | 0.0109 (0.0109) | [−0.07992, −0.01793] | [−0.08456, −0.01545] | [−0.08688, −0.01583] | 1.115 | no / no / no | 12 | supplementary.md:17 |
| 763 | engine | diag residual sts ts_gsr W60 | primary | dmt_change | +0.00771 | 0.0797 (0.0797) | [−0.00011, +0.01493] | [−0.00112, +0.01643] | [−0.00100, +0.01643] | 1.167 | yes / yes / yes | 4 | S3_Text.md:199 |
| 764 | engine | diag residual sts ts_gsr W60 | primary | pcb_change | −0.00382 | 0.1929 (0.1929) | [−0.00908, +0.00136] | [−0.00986, +0.00220] | [−0.00981, +0.00218] | 1.156 | yes / yes / yes | 10 | S3_Text.md:199 |
| 765 | engine | diag residual sts ts_gsr W60 | primary | fd_did | +0.01435 | 0.2452 (0.2452) | [−0.00704, +0.03646] | [−0.01147, +0.04026] | [−0.01116, +0.03985] | 1.189 | yes / yes / yes | 6 | draft_v2.md:92 |
| 766 | engine | diag residual sts ts_gsr W60 | primary | resid_did | +0.00999 | 0.0580 (0.0580) | [+0.00085, +0.01849] | [−0.00040, +0.02014] | [−0.00027, +0.02024] | 1.165 | no / yes / yes, changes | 3 | — |
| 767 | engine | CCSpub sts ts_gsr W60 | primary | dmt_change | +0.00212 | 0.1667 (0.1667) | [−0.00055, +0.00485] | [−0.00097, +0.00524] | [−0.00099, +0.00523] | 1.150 | yes / yes / yes | 4 | — |
| 768 | engine | CCSpub sts ts_gsr W60 | primary | pcb_change | −0.00226 | 0.1093 (0.1093) | [−0.00469, +0.00017] | [−0.00511, +0.00061] | [−0.00510, +0.00058] | 1.177 | yes / yes / yes | 9 | — |
| 769 | engine | CCSpub sts ts_gsr W60 | primary | fd_did | +0.01435 | 0.2452 (0.2452) | [−0.00704, +0.03646] | [−0.01147, +0.04026] | [−0.01116, +0.03985] | 1.189 | yes / yes / yes | 6 | draft_v2.md:92 |
| 770 | engine | CCSpub sts ts_gsr W60 | primary | resid_did | +0.00388 | 0.0535 (0.0535) | [+0.00047, +0.00726] | [−0.00006, +0.00770] | [−0.00004, +0.00780] | 1.143 | no / yes / yes, changes | 2 | S3_Text.md:193 |
| 771 | engine | autocorr ts_gsr W60 | primary | dmt_change | −0.00967 | 0.0430 (0.0430) | [−0.01720, −0.00137] | [−0.01877, −0.00036] | [−0.01893, −0.00041] | 1.164 | no / no / no | 11 | — |
| 772 | engine | autocorr ts_gsr W60 | primary | pcb_change | +0.00498 | 0.1423 (0.1423) | [−0.00076, +0.01132] | [−0.00175, +0.01186] | [−0.00186, +0.01181] | 1.126 | yes / yes / yes | 4 | — |
| 773 | engine | autocorr ts_gsr W60 | primary | fd_did | +0.01435 | 0.2452 (0.2452) | [−0.00704, +0.03646] | [−0.01147, +0.04026] | [−0.01116, +0.03985] | 1.189 | yes / yes / yes | 6 | draft_v2.md:92 |
| 774 | engine | autocorr ts_gsr W60 | primary | resid_did | −0.01226 | 0.0135 (0.0135) | [−0.01994, −0.00410] | [−0.02095, −0.00305] | [−0.02136, −0.00316] | 1.130 | no / no / no | 12 | S3_Text.md:153 |
| 775 | saved | run-level residual (observed − AR(1)-substituted sts, whole-run matrices) ts_gsr | run level | mean of the two runs | −0.01373 | 0.0001 (—) | [−0.01448, −0.01302] | [−0.01457, −0.01291] | [−0.01457, −0.01289] | 1.141 | no / no / no | 14 | S3_Text.md:199; draft_v2.md:122; draft_v2.md:132 |
| 776 | saved | run-level residual (observed − AR(1)-substituted sts, whole-run matrices) ts_demean | run level | mean of the two runs | +0.00079 | 0.7904 (—) | [−0.00482, +0.00669] | [−0.00598, +0.00742] | [−0.00572, +0.00731] | 1.164 | yes / yes / yes | 9 | — |
| 777 | saved | signed mean cross-lag deviation, run level (superseded; S9 Table) ts_gsr | run level | grand mean (mean of the two runs) | +0.00009 | 0.0004 (0.0004) | [+0.00005, +0.00013] | [+0.00004, +0.00014] | [+0.00004, +0.00014] | 1.179 | no / no / no | 1 | supplementary.md:187 |
| 778 | saved | slope of the deviation on q, run level (superseded; S9 Table) ts_gsr | run level | grand mean (mean of the two runs) | +0.01633 | 0.0001 (0.0001) | [+0.01410, +0.01870] | [+0.01368, +0.01901] | [+0.01368, +0.01898] | 1.159 | no / no / no | 0 | supplementary.md:187 |
| 779 | saved | slope of the deviation on q, W = 60 (superseded; S9 Table) ts_gsr | W = 60 | grand mean (mean of the two runs) | +0.02014 | 0.0001 (0.0001) | [+0.01840, +0.02220] | [+0.01803, +0.02233] | [+0.01797, +0.02230] | 1.132 | no / no / no | 0 | supplementary.md:187 |
| 780 | saved | signed mean cross-lag deviation, run level (superseded; S9 Table) ts_demean | run level | grand mean (mean of the two runs) | −0.00738 | 0.0001 (0.0001) | [−0.00902, −0.00588] | [−0.00920, −0.00563] | [−0.00917, −0.00559] | 1.138 | no / no / no | 14 | supplementary.md:187 |
| 781 | saved | slope of the deviation on q, run level (superseded; S9 Table) ts_demean | run level | grand mean (mean of the two runs) | +0.02106 | 0.0001 (0.0001) | [+0.01940, +0.02270] | [+0.01913, +0.02301] | [+0.01913, +0.02298] | 1.174 | no / no / no | 0 | supplementary.md:187 |
| 782 | saved | slope of the deviation on q, W = 60 (superseded; S9 Table) ts_demean | W = 60 | grand mean (mean of the two runs) | +0.02370 | 0.0001 (0.0001) | [+0.02190, +0.02550] | [+0.02159, +0.02581] | [+0.02161, +0.02579] | 1.171 | no / no / no | 0 | supplementary.md:187 |
| 783 | saved | closed-form response of sts to δ_anti alone (directed share), run level ts_gsr | run level | mean of the two runs | −0.00641 | 0.0001 (—) | [−0.00692, −0.00586] | [−0.00700, −0.00580] | [−0.00701, −0.00580] | 1.137 | no / no / no | 14 | S3_Text.md:209; draft_v2.md:122 |
| 784 | saved | closed-form response of sts to δ_anti alone (directed share), run level ts_demean | run level | mean of the two runs | −0.00851 | 0.0001 (—) | [−0.00991, −0.00720] | [−0.01007, −0.00694] | [−0.01006, −0.00697] | 1.154 | no / no / no | 14 | S3_Text.md:209 |
| 785 | saved | CCS-sts decomposition: s (selected share) (code mask) ts_gsr W60 | primary | DiD | −0.02039 | 0.0104 (0.0104) | [−0.03210, −0.00768] | [−0.03455, −0.00618] | [−0.03440, −0.00638] | 1.162 | no / no / no | 11 | — |
| 786 | saved | CCS-sts decomposition: c̄_rej (nats) (code mask) ts_gsr W60 | primary | DiD | −0.00676 | 0.0422 (0.0422) | [−0.01227, −0.00111] | [−0.01327, −0.00025] | [−0.01324, −0.00028] | 1.166 | no / no / no | 10 | — |
| 787 | saved | CCS-sts decomposition: CCS-sts (nats) (code mask) ts_gsr W60 | primary | DiD | +0.00362 | 0.0845 (0.0845) | [−0.00010, +0.00724] | [−0.00058, +0.00780] | [−0.00055, +0.00779] | 1.142 | yes / yes / yes | 4 | — |
| 788 | saved | CCS-sts decomposition: share term c̄_pre Δs (code mask) ts_gsr W60 | primary | DiD | −0.00122 | 0.0188 (0.0188) | [−0.00202, −0.00038] | [−0.00217, −0.00026] | [−0.00216, −0.00028] | 1.164 | no / no / no | 11 | — |
| 789 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (code mask) ts_gsr W60 | primary | DiD | +0.00475 | 0.0432 (0.0432) | [+0.00072, +0.00858] | [+0.00017, +0.00934] | [+0.00018, +0.00932] | 1.166 | no / no / no | 4 | — |
| 790 | saved | CCS-sts decomposition: interaction Δs Δc̄ (code mask) ts_gsr W60 | primary | DiD | +0.00009 | 0.5227 (0.5233) | [−0.00016, +0.00034] | [−0.00019, +0.00038] | [−0.00020, +0.00038] | 1.148 | yes / yes / yes | 4 | — |
| 791 | saved | CCS-sts decomposition: s (selected share) (pub mask) ts_gsr W60 | primary | DiD | −0.02096 | 0.0089 (0.0089) | [−0.03262, −0.00829] | [−0.03512, −0.00681] | [−0.03495, −0.00697] | 1.164 | no / no / no | 11 | — |
| 792 | saved | CCS-sts decomposition: c̄_rej (nats) (pub mask) ts_gsr W60 | primary | DiD | −0.00944 | 0.0256 (0.0256) | [−0.01613, −0.00236] | [−0.01745, −0.00140] | [−0.01745, −0.00143] | 1.165 | no / no / no | 11 | — |
| 793 | saved | CCS-sts decomposition: CCS-sts (nats) (pub mask) ts_gsr W60 | primary | DiD | +0.00438 | 0.0562 (0.0562) | [+0.00033, +0.00820] | [−0.00012, +0.00882] | [−0.00012, +0.00888] | 1.136 | no / yes / yes, changes | 3 | — |
| 794 | saved | CCS-sts decomposition: share term c̄_pre Δs (pub mask) ts_gsr W60 | primary | DiD | −0.00179 | 0.0127 (0.0127) | [−0.00287, −0.00066] | [−0.00308, −0.00049] | [−0.00307, −0.00052] | 1.172 | no / no / no | 11 | — |
| 795 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (pub mask) ts_gsr W60 | primary | DiD | +0.00593 | 0.0272 (0.0272) | [+0.00143, +0.01018] | [+0.00084, +0.01100] | [+0.00082, +0.01103] | 1.162 | no / no / no | 2 | — |
| 796 | saved | CCS-sts decomposition: interaction Δs Δc̄ (pub mask) ts_gsr W60 | primary | DiD | +0.00024 | 0.1176 (0.1178) | [−0.00003, +0.00052] | [−0.00007, +0.00056] | [−0.00007, +0.00056] | 1.131 | yes / yes / yes | 4 | — |
| 797 | saved | CCS-sts decomposition: s (selected share) (code mask) ts_gsr global | primary | DiD | +0.02806 | 0.0035 (0.0035) | [+0.01339, +0.04222] | [+0.01164, +0.04428] | [+0.01172, +0.04440] | 1.132 | no / no / no | 2 | — |
| 798 | saved | CCS-sts decomposition: c̄_rej (nats) (code mask) ts_gsr global | primary | DiD | −0.03008 | 0.0001 (0.0001) | [−0.03868, −0.02219] | [−0.03962, −0.02068] | [−0.03955, −0.02062] | 1.149 | no / no / no | 14 | — |
| 799 | saved | CCS-sts decomposition: CCS-sts (nats) (code mask) ts_gsr global | primary | DiD | +0.02102 | 0.0001 (0.0001) | [+0.01533, +0.02693] | [+0.01443, +0.02769] | [+0.01439, +0.02764] | 1.143 | no / no / no | 0 | — |
| 800 | saved | CCS-sts decomposition: share term c̄_pre Δs (code mask) ts_gsr global | primary | DiD | +0.00165 | 0.0033 (0.0033) | [+0.00080, +0.00254] | [+0.00065, +0.00265] | [+0.00066, +0.00265] | 1.151 | no / no / no | 2 | — |
| 801 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (code mask) ts_gsr global | primary | DiD | +0.01981 | 0.0001 (0.0001) | [+0.01468, +0.02530] | [+0.01369, +0.02602] | [+0.01365, +0.02597] | 1.161 | no / no / no | 0 | — |
| 802 | saved | CCS-sts decomposition: interaction Δs Δc̄ (code mask) ts_gsr global | primary | DiD | −0.00045 | 0.0592 (0.0588) | [−0.00086, −0.00006] | [−0.00091, +0.00002] | [−0.00091, +0.00001] | 1.162 | no / yes / yes, changes | 11 | — |
| 803 | saved | CCS-sts decomposition: s (selected share) (pub mask) ts_gsr global | primary | DiD | +0.04217 | 0.0007 (0.0007) | [+0.02551, +0.05845] | [+0.02321, +0.06087] | [+0.02331, +0.06103] | 1.143 | no / no / no | 2 | — |
| 804 | saved | CCS-sts decomposition: c̄_rej (nats) (pub mask) ts_gsr global | primary | DiD | −0.02921 | 0.0001 (0.0001) | [−0.03811, −0.02105] | [−0.03909, −0.01951] | [−0.03902, −0.01939] | 1.148 | no / no / no | 14 | — |
| 805 | saved | CCS-sts decomposition: CCS-sts (nats) (pub mask) ts_gsr global | primary | DiD | +0.01966 | 0.0002 (0.0002) | [+0.01416, +0.02540] | [+0.01328, +0.02610] | [+0.01324, +0.02609] | 1.140 | no / no / no | 1 | S3_Text.md:193; draft_v2.md:165; draft_v2.md:172 |
| 806 | saved | CCS-sts decomposition: share term c̄_pre Δs (pub mask) ts_gsr global | primary | DiD | +0.00275 | 0.0010 (0.0010) | [+0.00160, +0.00395] | [+0.00142, +0.00409] | [+0.00142, +0.00408] | 1.136 | no / no / no | 1 | — |
| 807 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (pub mask) ts_gsr global | primary | DiD | +0.01741 | 0.0001 (0.0001) | [+0.01270, +0.02243] | [+0.01177, +0.02313] | [+0.01174, +0.02309] | 1.168 | no / no / no | 0 | draft_v2.md:165 |
| 808 | saved | CCS-sts decomposition: interaction Δs Δc̄ (pub mask) ts_gsr global | primary | DiD | −0.00050 | 0.0618 (0.0618) | [−0.00099, −0.00005] | [−0.00104, +0.00003] | [−0.00103, +0.00003] | 1.138 | no / yes / yes, changes | 9 | — |
| 809 | saved | CCS-sts decomposition: s (selected share) (code mask) ts_demean W60 | primary | DiD | −0.00352 | 0.5748 (0.5747) | [−0.01521, +0.00762] | [−0.01693, +0.00979] | [−0.01683, +0.00979] | 1.171 | yes / yes / yes | 8 | — |
| 810 | saved | CCS-sts decomposition: c̄_rej (nats) (code mask) ts_demean W60 | primary | DiD | −0.02041 | 0.0042 (0.0042) | [−0.03321, −0.00891] | [−0.03443, −0.00659] | [−0.03435, −0.00647] | 1.146 | no / no / no | 12 | — |
| 811 | saved | CCS-sts decomposition: CCS-sts (nats) (code mask) ts_demean W60 | primary | DiD | +0.01337 | 0.0052 (0.0052) | [+0.00545, +0.02229] | [+0.00388, +0.02309] | [+0.00374, +0.02300] | 1.141 | no / no / no | 3 | — |
| 812 | saved | CCS-sts decomposition: share term c̄_pre Δs (code mask) ts_demean W60 | primary | DiD | −0.00019 | 0.6429 (0.6429) | [−0.00097, +0.00054] | [−0.00106, +0.00066] | [−0.00105, +0.00067] | 1.140 | yes / yes / yes | 7 | — |
| 813 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (code mask) ts_demean W60 | primary | DiD | +0.01396 | 0.0046 (0.0046) | [+0.00572, +0.02311] | [+0.00430, +0.02386] | [+0.00416, +0.02377] | 1.125 | no / no / no | 3 | — |
| 814 | saved | CCS-sts decomposition: interaction Δs Δc̄ (code mask) ts_demean W60 | primary | DiD | −0.00040 | 0.2893 (0.2893) | [−0.00109, +0.00028] | [−0.00118, +0.00040] | [−0.00119, +0.00038] | 1.154 | yes / yes / yes | 9 | — |
| 815 | saved | CCS-sts decomposition: s (selected share) (pub mask) ts_demean W60 | primary | DiD | −0.00171 | 0.8015 (0.8014) | [−0.01433, +0.01052] | [−0.01613, +0.01260] | [−0.01608, +0.01266] | 1.156 | yes / yes / yes | 8 | — |
| 816 | saved | CCS-sts decomposition: c̄_rej (nats) (pub mask) ts_demean W60 | primary | DiD | −0.02052 | 0.0028 (0.0028) | [−0.03217, −0.00993] | [−0.03326, −0.00810] | [−0.03320, −0.00783] | 1.131 | no / no / no | 12 | — |
| 817 | saved | CCS-sts decomposition: CCS-sts (nats) (pub mask) ts_demean W60 | primary | DiD | +0.01197 | 0.0040 (0.0040) | [+0.00522, +0.01944] | [+0.00412, +0.02011] | [+0.00390, +0.02005] | 1.124 | no / no / no | 3 | — |
| 818 | saved | CCS-sts decomposition: share term c̄_pre Δs (pub mask) ts_demean W60 | primary | DiD | −0.00035 | 0.5244 (0.5240) | [−0.00138, +0.00063] | [−0.00152, +0.00081] | [−0.00150, +0.00081] | 1.159 | yes / yes / yes | 8 | — |
| 819 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (pub mask) ts_demean W60 | primary | DiD | +0.01245 | 0.0033 (0.0033) | [+0.00560, +0.01982] | [+0.00467, +0.02050] | [+0.00442, +0.02047] | 1.113 | no / no / no | 2 | — |
| 820 | saved | CCS-sts decomposition: interaction Δs Δc̄ (pub mask) ts_demean W60 | primary | DiD | −0.00012 | 0.6897 (0.6893) | [−0.00075, +0.00048] | [−0.00082, +0.00056] | [−0.00083, +0.00058] | 1.120 | yes / yes / yes | 7 | — |
| 821 | saved | CCS-sts decomposition: s (selected share) (code mask) ts_demean global | primary | DiD | +0.04077 | 0.0004 (0.0004) | [+0.02350, +0.05883] | [+0.02099, +0.06124] | [+0.02042, +0.06112] | 1.139 | no / no / no | 1 | — |
| 822 | saved | CCS-sts decomposition: c̄_rej (nats) (code mask) ts_demean global | primary | DiD | −0.04803 | 0.0001 (0.0001) | [−0.06454, −0.03194] | [−0.06711, −0.02916] | [−0.06682, −0.02924] | 1.164 | no / no / no | 14 | — |
| 823 | saved | CCS-sts decomposition: CCS-sts (nats) (code mask) ts_demean global | primary | DiD | +0.03216 | 0.0001 (0.0001) | [+0.02145, +0.04336] | [+0.01977, +0.04471] | [+0.01976, +0.04455] | 1.138 | no / no / no | 0 | — |
| 824 | saved | CCS-sts decomposition: share term c̄_pre Δs (code mask) ts_demean global | primary | DiD | +0.00217 | 0.0017 (0.0017) | [+0.00106, +0.00335] | [+0.00086, +0.00350] | [+0.00085, +0.00348] | 1.156 | no / no / no | 2 | — |
| 825 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (code mask) ts_demean global | primary | DiD | +0.03197 | 0.0001 (0.0001) | [+0.02115, +0.04348] | [+0.01904, +0.04505] | [+0.01908, +0.04486] | 1.165 | no / no / no | 0 | — |
| 826 | saved | CCS-sts decomposition: interaction Δs Δc̄ (code mask) ts_demean global | primary | DiD | −0.00198 | 0.0233 (0.0233) | [−0.00376, −0.00048] | [−0.00388, −0.00022] | [−0.00386, −0.00010] | 1.118 | no / no / no | 10 | — |
| 827 | saved | CCS-sts decomposition: s (selected share) (pub mask) ts_demean global | primary | DiD | +0.05864 | 0.0004 (0.0004) | [+0.03652, +0.08176] | [+0.03341, +0.08466] | [+0.03275, +0.08452] | 1.133 | no / no / no | 1 | — |
| 828 | saved | CCS-sts decomposition: c̄_rej (nats) (pub mask) ts_demean global | primary | DiD | −0.05862 | 0.0001 (0.0001) | [−0.08014, −0.03753] | [−0.08378, −0.03359] | [−0.08348, −0.03375] | 1.178 | no / no / no | 14 | — |
| 829 | saved | CCS-sts decomposition: CCS-sts (nats) (pub mask) ts_demean global | primary | DiD | +0.03552 | 0.0001 (0.0001) | [+0.02295, +0.04858] | [+0.02076, +0.05033] | [+0.02091, +0.05013] | 1.154 | no / no / no | 0 | — |
| 830 | saved | CCS-sts decomposition: share term c̄_pre Δs (pub mask) ts_demean global | primary | DiD | +0.00443 | 0.0005 (0.0005) | [+0.00238, +0.00680] | [+0.00198, +0.00699] | [+0.00190, +0.00697] | 1.132 | no / no / no | 1 | — |
| 831 | saved | CCS-sts decomposition: co-information term −(1 − s_pre) Δc̄ (pub mask) ts_demean global | primary | DiD | +0.03432 | 0.0001 (0.0001) | [+0.02168, +0.04778] | [+0.01920, +0.04953] | [+0.01932, +0.04933] | 1.162 | no / no / no | 0 | — |
| 832 | saved | CCS-sts decomposition: interaction Δs Δc̄ (pub mask) ts_demean global | primary | DiD | −0.00324 | 0.0210 (0.0210) | [−0.00626, −0.00084] | [−0.00638, −0.00041] | [−0.00634, −0.00014] | 1.102 | no / no / no | 9 | — |
| 833 | saved | cross-lag budget δ_run ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00340 | 0.0001 (0.0001) | [+0.00300, +0.00380] | [+0.00294, +0.00386] | [+0.00294, +0.00386] | 1.151 | no / no / no | 0 | S3_Text.md:207; supplementary.md:161 |
| 834 | saved | cross-lag budget δ_run ts_gsr | DMT run | S9 Table | +0.00381 | 0.0001 (—) | [+0.00339, +0.00424] | [+0.00332, +0.00429] | [+0.00333, +0.00429] | 1.143 | no / no / no | 0 | supplementary.md:162 |
| 835 | saved | cross-lag budget δ_run ts_gsr | placebo run | S9 Table | +0.00299 | 0.0001 (—) | [+0.00235, +0.00363] | [+0.00225, +0.00373] | [+0.00226, +0.00373] | 1.158 | no / no / no | 0 | supplementary.md:163 |
| 836 | saved | cross-lag budget δ_run ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00301 | 0.0001 (—) | [+0.00261, +0.00340] | [+0.00255, +0.00347] | [+0.00255, +0.00346] | 1.153 | no / no / no | 0 | S3_Text.md:207; supplementary.md:167 |
| 837 | saved | cross-lag budget δ_wd ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00339 | 0.0001 (0.0001) | [+0.00299, +0.00378] | [+0.00293, +0.00384] | [+0.00294, +0.00384] | 1.153 | no / no / no | 0 | — |
| 838 | saved | cross-lag budget δ_wd ts_gsr | DMT run | S9 Table | +0.00379 | 0.0001 (—) | [+0.00338, +0.00421] | [+0.00331, +0.00426] | [+0.00331, +0.00426] | 1.149 | no / no / no | 0 | — |
| 839 | saved | cross-lag budget δ_wd ts_gsr | placebo run | S9 Table | +0.00299 | 0.0001 (—) | [+0.00235, +0.00363] | [+0.00225, +0.00372] | [+0.00226, +0.00372] | 1.150 | no / no / no | 0 | supplementary.md:163 |
| 840 | saved | cross-lag budget δ_wd ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00297 | 0.0001 (—) | [+0.00258, +0.00336] | [+0.00251, +0.00343] | [+0.00252, +0.00342] | 1.157 | no / no / no | 0 | — |
| 841 | saved | cross-lag budget δ_means ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00001 | 0.1365 (0.1365) | [+0.00000, +0.00003] | [−0.00000, +0.00003] | [−0.00000, +0.00003] | 1.138 | yes / yes / yes | 6 | supplementary.md:161 |
| 842 | saved | cross-lag budget δ_means ts_gsr | DMT run | S9 Table | +0.00002 | 0.1078 (—) | [+0.00000, +0.00004] | [−0.00000, +0.00005] | [−0.00001, +0.00005] | 1.288 | yes / yes / yes | 5 | supplementary.md:162 |
| 843 | saved | cross-lag budget δ_means ts_gsr | placebo run | S9 Table | +0.00000 | 0.7253 (—) | [−0.00002, +0.00002] | [−0.00002, +0.00003] | [−0.00002, +0.00003] | 1.082 | yes / yes / yes | 5 | supplementary.md:163; supplementary.md:176 |
| 844 | saved | cross-lag budget δ_means ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00004 | 0.0001 (—) | [+0.00002, +0.00005] | [+0.00002, +0.00005] | [+0.00002, +0.00005] | 1.161 | no / no / no | 0 | supplementary.md:167 |
| 845 | saved | cross-lag budget δ_within ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00291 | 0.0001 (0.0001) | [+0.00257, +0.00325] | [+0.00252, +0.00330] | [+0.00252, +0.00330] | 1.149 | no / no / no | 0 | supplementary.md:161 |
| 846 | saved | cross-lag budget δ_within ts_gsr | DMT run | S9 Table | +0.00310 | 0.0001 (—) | [+0.00277, +0.00343] | [+0.00273, +0.00347] | [+0.00273, +0.00347] | 1.133 | no / no / no | 0 | supplementary.md:162 |
| 847 | saved | cross-lag budget δ_within ts_gsr | placebo run | S9 Table | +0.00272 | 0.0001 (—) | [+0.00215, +0.00327] | [+0.00207, +0.00336] | [+0.00207, +0.00336] | 1.157 | no / no / no | 0 | supplementary.md:163 |
| 848 | saved | cross-lag budget δ_within ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00250 | 0.0001 (—) | [+0.00217, +0.00285] | [+0.00211, +0.00289] | [+0.00212, +0.00289] | 1.153 | no / no / no | 0 | supplementary.md:167 |
| 849 | saved | cross-lag budget δ_pool ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00050 | 0.0001 (0.0001) | [+0.00038, +0.00062] | [+0.00036, +0.00063] | [+0.00036, +0.00063] | 1.147 | no / no / no | 0 | supplementary.md:161 |
| 850 | saved | cross-lag budget δ_pool ts_gsr | DMT run | S9 Table | +0.00069 | 0.0001 (—) | [+0.00053, +0.00086] | [+0.00050, +0.00088] | [+0.00050, +0.00087] | 1.150 | no / no / no | 0 | supplementary.md:162 |
| 851 | saved | cross-lag budget δ_pool ts_gsr | placebo run | S9 Table | +0.00030 | 0.0002 (—) | [+0.00019, +0.00042] | [+0.00017, +0.00044] | [+0.00017, +0.00044] | 1.151 | no / no / no | 1 | supplementary.md:163 |
| 852 | saved | cross-lag budget δ_pool ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00046 | 0.0001 (—) | [+0.00035, +0.00059] | [+0.00033, +0.00060] | [+0.00033, +0.00060] | 1.169 | no / no / no | 0 | supplementary.md:167 |
| 853 | saved | cross-lag budget δ_eps ts_gsr | grand mean (mean of the two runs) | S9 Table | −0.00002 | 0.2068 (0.2068) | [−0.00004, +0.00001] | [−0.00004, +0.00001] | [−0.00004, +0.00001] | 1.102 | yes / yes / yes | 9 | supplementary.md:161 |
| 854 | saved | cross-lag budget δ_eps ts_gsr | DMT run | S9 Table | −0.00000 | 0.8984 (—) | [−0.00005, +0.00004] | [−0.00005, +0.00005] | [−0.00005, +0.00005] | 1.149 | yes / yes / yes | 8 | supplementary.md:162 |
| 855 | saved | cross-lag budget δ_eps ts_gsr | placebo run | S9 Table | −0.00003 | 0.0072 (—) | [−0.00005, −0.00001] | [−0.00005, −0.00001] | [−0.00005, −0.00001] | 1.080 | no / no / no | 10 | supplementary.md:163 |
| 856 | saved | cross-lag budget δ_eps ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00000 | 0.8184 (—) | [−0.00002, +0.00003] | [−0.00002, +0.00003] | [−0.00002, +0.00003] | 1.126 | yes / yes / yes | 6 | supplementary.md:167 |
| 857 | saved | cross-lag budget δ_60 (run-level sign) ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00245 | 0.0001 (0.0001) | [+0.00212, +0.00281] | [+0.00205, +0.00285] | [+0.00205, +0.00285] | 1.153 | no / no / no | 0 | supplementary.md:161 |
| 858 | saved | cross-lag budget δ_60 (run-level sign) ts_gsr | DMT run | S9 Table | +0.00264 | 0.0001 (—) | [+0.00227, +0.00301] | [+0.00222, +0.00306] | [+0.00222, +0.00306] | 1.143 | no / no / no | 0 | supplementary.md:162 |
| 859 | saved | cross-lag budget δ_60 (run-level sign) ts_gsr | placebo run | S9 Table | +0.00226 | 0.0001 (—) | [+0.00170, +0.00280] | [+0.00162, +0.00289] | [+0.00163, +0.00289] | 1.153 | no / no / no | 0 | supplementary.md:163 |
| 860 | saved | cross-lag budget δ_60 (run-level sign) ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00228 | 0.0001 (—) | [+0.00194, +0.00263] | [+0.00188, +0.00268] | [+0.00188, +0.00267] | 1.149 | no / no / no | 0 | supplementary.md:167 |
| 861 | saved | cross-lag budget window-sign value (partB10) ts_gsr | grand mean (mean of the two runs) | S9 Table | +0.00611 | 0.0001 (0.0001) | [+0.00563, +0.00665] | [+0.00552, +0.00671] | [+0.00553, +0.00670] | 1.163 | no / no / no | 0 | supplementary.md:161; supplementary.md:185 |
| 862 | saved | cross-lag budget window-sign value (partB10) ts_gsr | DMT run | S9 Table | +0.00615 | 0.0001 (—) | [+0.00575, +0.00660] | [+0.00568, +0.00663] | [+0.00567, +0.00663] | 1.121 | no / no / no | 0 | supplementary.md:162 |
| 863 | saved | cross-lag budget window-sign value (partB10) ts_gsr | placebo run | S9 Table | +0.00608 | 0.0001 (—) | [+0.00535, +0.00685] | [+0.00522, +0.00695] | [+0.00522, +0.00694] | 1.151 | no / no / no | 0 | supplementary.md:163 |
| 864 | saved | cross-lag budget window-sign value (partB10) ts_gsr, null-corrected (primary configuration) | grand mean − null | S9 Table | +0.00259 | 0.0001 (—) | [+0.00211, +0.00313] | [+0.00201, +0.00319] | [+0.00201, +0.00318] | 1.159 | no / no / no | 0 | supplementary.md:167 |
| 865 | saved | cross-lag budget δ_run ts_demean | grand mean (mean of the two runs) | S9 Table | −0.00262 | 0.0532 (0.0532) | [−0.00495, −0.00037] | [−0.00528, +0.00006] | [−0.00523, −0.00000] | 1.166 | no / yes / no, changes | 9 | S3_Text.md:207; supplementary.md:174 |
| 866 | saved | cross-lag budget δ_run ts_demean | DMT run | S9 Table | −0.00324 | 0.0273 (—) | [−0.00614, −0.00079] | [−0.00638, −0.00036] | [−0.00634, −0.00014] | 1.126 | no / no / no | 9 | supplementary.md:175 |
| 867 | saved | cross-lag budget δ_run ts_demean | placebo run | S9 Table | −0.00199 | 0.1711 (—) | [−0.00465, +0.00041] | [−0.00493, +0.00089] | [−0.00489, +0.00091] | 1.150 | yes / yes / yes | 9 | supplementary.md:176 |
| 868 | saved | cross-lag budget δ_wd ts_demean | grand mean (mean of the two runs) | S9 Table | −0.00262 | 0.0536 (0.0536) | [−0.00495, −0.00037] | [−0.00527, +0.00006] | [−0.00524, +0.00000] | 1.166 | no / yes / yes, changes | 9 | S3_Text.md:207; supplementary.md:174 |
| 869 | saved | cross-lag budget δ_wd ts_demean | DMT run | S9 Table | −0.00324 | 0.0281 (—) | [−0.00615, −0.00078] | [−0.00639, −0.00034] | [−0.00635, −0.00013] | 1.125 | no / no / no | 9 | — |
| 870 | saved | cross-lag budget δ_wd ts_demean | placebo run | S9 Table | −0.00199 | 0.1692 (—) | [−0.00465, +0.00040] | [−0.00491, +0.00088] | [−0.00489, +0.00090] | 1.147 | yes / yes / yes | 9 | — |
| 871 | saved | cross-lag budget δ_means ts_demean | grand mean (mean of the two runs) | S9 Table | +0.00000 | 0.9149 (0.9149) | [−0.00001, +0.00002] | [−0.00002, +0.00002] | [−0.00002, +0.00002] | 1.081 | yes / yes / yes | 8 | supplementary.md:174 |
| 872 | saved | cross-lag budget δ_means ts_demean | DMT run | S9 Table | −0.00000 | 0.9552 (—) | [−0.00003, +0.00003] | [−0.00003, +0.00004] | [−0.00004, +0.00004] | 1.154 | yes / yes / yes | 9 | supplementary.md:175 |
| 873 | saved | cross-lag budget δ_means ts_demean | placebo run | S9 Table | +0.00000 | 0.7657 (—) | [−0.00002, +0.00002] | [−0.00002, +0.00002] | [−0.00002, +0.00002] | 1.039 | yes / yes / yes | 6 | supplementary.md:163; supplementary.md:176 |
| 874 | saved | cross-lag budget δ_within ts_demean | grand mean (mean of the two runs) | S9 Table | −0.00226 | 0.0537 (0.0537) | [−0.00428, −0.00034] | [−0.00455, +0.00005] | [−0.00451, −0.00001] | 1.168 | no / yes / no, changes | 8 | supplementary.md:174 |
| 875 | saved | cross-lag budget δ_within ts_demean | DMT run | S9 Table | −0.00270 | 0.0237 (—) | [−0.00498, −0.00073] | [−0.00518, −0.00036] | [−0.00515, −0.00025] | 1.133 | no / no / no | 9 | supplementary.md:175 |
| 876 | saved | cross-lag budget δ_within ts_demean | placebo run | S9 Table | −0.00182 | 0.1589 (—) | [−0.00418, +0.00036] | [−0.00445, +0.00077] | [−0.00441, +0.00077] | 1.150 | yes / yes / yes | 9 | supplementary.md:176 |
| 877 | saved | cross-lag budget δ_pool ts_demean | grand mean (mean of the two runs) | S9 Table | −0.00030 | 0.1296 (0.1296) | [−0.00069, +0.00001] | [−0.00071, +0.00007] | [−0.00071, +0.00010] | 1.119 | yes / yes / yes | 8 | supplementary.md:174 |
| 878 | saved | cross-lag budget δ_pool ts_demean | DMT run | S9 Table | −0.00047 | 0.2703 (—) | [−0.00120, +0.00011] | [−0.00124, +0.00020] | [−0.00123, +0.00029] | 1.098 | yes / yes / yes | 8 | supplementary.md:175 |
| 879 | saved | cross-lag budget δ_pool ts_demean | placebo run | S9 Table | −0.00014 | 0.3501 (—) | [−0.00041, +0.00009] | [−0.00042, +0.00013] | [−0.00042, +0.00014] | 1.096 | yes / yes / yes | 6 | supplementary.md:176 |
| 880 | saved | cross-lag budget δ_eps ts_demean | grand mean (mean of the two runs) | S9 Table | −0.00005 | 0.1117 (0.1117) | [−0.00011, +0.00000] | [−0.00012, +0.00001] | [−0.00012, +0.00001] | 1.231 | yes / yes / yes | 10 | supplementary.md:174 |
| 881 | saved | cross-lag budget δ_eps ts_demean | DMT run | S9 Table | −0.00007 | 0.0479 (—) | [−0.00013, −0.00001] | [−0.00014, −0.00000] | [−0.00014, −0.00000] | 1.170 | no / no / no | 9 | supplementary.md:175 |
| 882 | saved | cross-lag budget δ_eps ts_demean | placebo run | S9 Table | −0.00004 | 0.4934 (—) | [−0.00014, +0.00005] | [−0.00015, +0.00007] | [−0.00015, +0.00007] | 1.145 | yes / yes / yes | 7 | supplementary.md:176 |
| 883 | saved | cross-lag budget δ_60 (run-level sign) ts_demean | grand mean (mean of the two runs) | S9 Table | −0.00274 | 0.0270 (0.0270) | [−0.00478, −0.00079] | [−0.00505, −0.00041] | [−0.00500, −0.00047] | 1.163 | no / no / no | 11 | supplementary.md:174 |
| 884 | saved | cross-lag budget δ_60 (run-level sign) ts_demean | DMT run | S9 Table | −0.00313 | 0.0112 (—) | [−0.00549, −0.00109] | [−0.00568, −0.00073] | [−0.00565, −0.00061] | 1.126 | no / no / no | 10 | supplementary.md:175 |
| 885 | saved | cross-lag budget δ_60 (run-level sign) ts_demean | placebo run | S9 Table | −0.00235 | 0.0763 (—) | [−0.00472, −0.00017] | [−0.00501, +0.00026] | [−0.00495, +0.00026] | 1.157 | no / yes / yes, changes | 9 | supplementary.md:176 |
| 886 | saved | cross-lag budget window-sign value (partB10) ts_demean | grand mean (mean of the two runs) | S9 Table | +0.00160 | 0.1061 (0.1061) | [−0.00019, +0.00326] | [−0.00040, +0.00367] | [−0.00038, +0.00359] | 1.178 | yes / yes / yes | 5 | supplementary.md:174; supplementary.md:185 |
| 887 | saved | cross-lag budget window-sign value (partB10) ts_demean | DMT run | S9 Table | +0.00108 | 0.2986 (—) | [−0.00090, +0.00285] | [−0.00112, +0.00318] | [−0.00109, +0.00326] | 1.148 | yes / yes / yes | 5 | supplementary.md:175 |
| 888 | saved | cross-lag budget window-sign value (partB10) ts_demean | placebo run | S9 Table | +0.00212 | 0.0624 (—) | [+0.00010, +0.00393] | [−0.00011, +0.00430] | [−0.00009, +0.00433] | 1.152 | no / yes / yes, changes | 4 | supplementary.md:176 |
| 889 | saved | S8 Table: ratio sts/TDMI: DiD ts_gsr windowed_W60 | primary | scripts/14 | +0.00053 | 0.9138 (0.9138) | [−0.00815, +0.00833] | [−0.00914, +0.00963] | [−0.00906, +0.01013] | 1.139 | yes / yes / yes | 6 | supplementary.md:148 |
| 890 | saved | S8 Table: ratio sts/TDMI: DMT post - pre ts_gsr windowed_W60 | primary | scripts/14 | +0.00338 | 0.1097 (0.1097) | [−0.00038, +0.00698] | [−0.00091, +0.00766] | [−0.00093, +0.00769] | 1.163 | yes / yes / yes | 4 | supplementary.md:153 |
| 891 | saved | S8 Table: ratio sts/TDMI: PCB post - pre ts_gsr windowed_W60 | primary | scripts/14 | +0.00285 | 0.3990 (0.3990) | [−0.00300, +0.00902] | [−0.00382, +0.00977] | [−0.00403, +0.00972] | 1.131 | yes / yes / yes | 7 | supplementary.md:153 |
| 892 | saved | S8 Table: (i) sts share of TDMI, pre-injection DMT (subject mean) ts_gsr windowed_W60 | primary | scripts/14 | +0.78196 | 0.0001 (—) | [+0.77793, +0.78569] | [+0.77748, +0.78636] | [+0.77756, +0.78637] | 1.144 | no / no / no | 0 | supplementary.md:148 |
| 893 | saved | S8 Table: sts share of TDMI, pre-injection PCB (subject mean) ts_gsr windowed_W60 | primary | scripts/14 | +0.77951 | 0.0001 (—) | [+0.77369, +0.78488] | [+0.77302, +0.78576] | [+0.77306, +0.78596] | 1.139 | no / no / no | 0 | — |
| 894 | saved | S8 Table: sts DiD (nats) ts_gsr windowed_W60 | primary | scripts/14 | −0.08087 | 0.0038 (0.0038) | [−0.12658, −0.03715] | [−0.13174, −0.03102] | [−0.13207, −0.02967] | 1.126 | no / no / no | 13 | supplementary.md:148 |
| 895 | saved | S8 Table: TDMI DiD (nats) ts_gsr windowed_W60 | primary | scripts/14 | −0.10372 | 0.0034 (0.0034) | [−0.15974, −0.04811] | [−0.16714, −0.04103] | [−0.16763, −0.03981] | 1.130 | no / no / no | 12 | supplementary.md:148 |
| 896 | saved | S8 Table: ratio sts/TDMI: DiD ts_demean windowed_W60 | primary | scripts/14 | −0.00947 | 0.2195 (0.2195) | [−0.02350, +0.00489] | [−0.02548, +0.00669] | [−0.02548, +0.00655] | 1.133 | yes / yes / yes | 9 | supplementary.md:149 |
| 897 | saved | S8 Table: ratio sts/TDMI: DMT post - pre ts_demean windowed_W60 | primary | scripts/14 | −0.00934 | 0.1621 (0.1621) | [−0.02150, +0.00192] | [−0.02313, +0.00392] | [−0.02290, +0.00421] | 1.155 | yes / yes / yes | 9 | supplementary.md:153 |
| 898 | saved | S8 Table: ratio sts/TDMI: PCB post - pre ts_demean windowed_W60 | primary | scripts/14 | +0.00012 | 0.9712 (0.9712) | [−0.00706, +0.00742] | [−0.00813, +0.00847] | [−0.00807, +0.00832] | 1.147 | yes / yes / yes | 7 | supplementary.md:153 |
| 899 | saved | S8 Table: (i) sts share of TDMI, pre-injection DMT (subject mean) ts_demean windowed_W60 | primary | scripts/14 | +0.76699 | 0.0001 (—) | [+0.75904, +0.77485] | [+0.75790, +0.77603] | [+0.75800, +0.77599] | 1.147 | no / no / no | 0 | supplementary.md:149 |
| 900 | saved | S8 Table: sts share of TDMI, pre-injection PCB (subject mean) ts_demean windowed_W60 | primary | scripts/14 | +0.76885 | 0.0001 (—) | [+0.76149, +0.77526] | [+0.76082, +0.77679] | [+0.76095, +0.77675] | 1.160 | no / no / no | 0 | — |
| 901 | saved | S8 Table: sts DiD (nats) ts_demean windowed_W60 | primary | scripts/14 | −0.10311 | 0.0026 (0.0026) | [−0.15404, −0.05155] | [−0.16293, −0.04352] | [−0.16274, −0.04349] | 1.165 | no / no / no | 12 | supplementary.md:149 |
| 902 | saved | S8 Table: TDMI DiD (nats) ts_demean windowed_W60 | primary | scripts/14 | −0.11856 | 0.0009 (0.0009) | [−0.17043, −0.06754] | [−0.17851, −0.05960] | [−0.17853, −0.05860] | 1.156 | no / no / no | 13 | supplementary.md:149 |
| 903 | saved | S8 Table: ratio sts/TDMI: DiD ts_gsr global_fit | primary | scripts/14 | +0.02039 | 0.0248 (0.0248) | [+0.00481, +0.03404] | [+0.00318, +0.03800] | [+0.00354, +0.03723] | 1.191 | no / no / no | 4 | draft_v2.md:80; supplementary.md:150 |
| 904 | saved | S8 Table: ratio sts/TDMI: DMT post - pre ts_gsr global_fit | primary | scripts/14 | +0.01672 | 0.0183 (0.0183) | [+0.00522, +0.02785] | [+0.00345, +0.02989] | [+0.00365, +0.02980] | 1.168 | no / no / no | 5 | supplementary.md:153 |
| 905 | saved | S8 Table: ratio sts/TDMI: PCB post - pre ts_gsr global_fit | primary | scripts/14 | −0.00366 | 0.3949 (0.3949) | [−0.01162, +0.00435] | [−0.01271, +0.00541] | [−0.01272, +0.00539] | 1.134 | yes / yes / yes | 8 | supplementary.md:153 |
| 906 | saved | S8 Table: (i) sts share of TDMI, pre-injection DMT (subject mean) ts_gsr global_fit | primary | scripts/14 | +0.90819 | 0.0001 (—) | [+0.89944, +0.91669] | [+0.89831, +0.91804] | [+0.89842, +0.91797] | 1.144 | no / no / no | 0 | supplementary.md:150 |
| 907 | saved | S8 Table: sts share of TDMI, pre-injection PCB (subject mean) ts_gsr global_fit | primary | scripts/14 | +0.91801 | 0.0001 (—) | [+0.91261, +0.92337] | [+0.91185, +0.92420] | [+0.91190, +0.92412] | 1.148 | no / no / no | 0 | — |
| 908 | saved | S8 Table: sts DiD (nats) ts_gsr global_fit | primary | scripts/14 | −0.08008 | 0.0071 (0.0071) | [−0.13198, −0.03158] | [−0.13624, −0.02506] | [−0.13728, −0.02288] | 1.107 | no / no / no | 12 | supplementary.md:150 |
| 909 | saved | S8 Table: TDMI DiD (nats) ts_gsr global_fit | primary | scripts/14 | −0.12164 | 0.0051 (0.0051) | [−0.19141, −0.05192] | [−0.19983, −0.04390] | [−0.20094, −0.04233] | 1.118 | no / no / no | 13 | supplementary.md:150 |
| 910 | saved | S8 Table: ratio sts/TDMI: DiD ts_demean global_fit | primary | scripts/14 | +0.00712 | 0.5623 (0.5623) | [−0.01672, +0.02916] | [−0.01970, +0.03342] | [−0.01930, +0.03355] | 1.158 | yes / yes / yes | 5 | supplementary.md:151 |
| 911 | saved | S8 Table: ratio sts/TDMI: DMT post - pre ts_demean global_fit | primary | scripts/14 | +0.00155 | 0.8799 (0.8799) | [−0.01831, +0.02029] | [−0.02079, +0.02393] | [−0.02051, +0.02360] | 1.158 | yes / yes / yes | 5 | supplementary.md:153 |
| 912 | saved | S8 Table: ratio sts/TDMI: PCB post - pre ts_demean global_fit | primary | scripts/14 | −0.00558 | 0.2753 (0.2753) | [−0.01430, +0.00417] | [−0.01558, +0.00505] | [−0.01612, +0.00497] | 1.117 | yes / yes / yes | 8 | supplementary.md:153 |
| 913 | saved | S8 Table: (i) sts share of TDMI, pre-injection DMT (subject mean) ts_demean global_fit | primary | scripts/14 | +0.89669 | 0.0001 (—) | [+0.88560, +0.90742] | [+0.88408, +0.90925] | [+0.88419, +0.90918] | 1.154 | no / no / no | 0 | supplementary.md:151 |
| 914 | saved | S8 Table: sts share of TDMI, pre-injection PCB (subject mean) ts_demean global_fit | primary | scripts/14 | +0.90888 | 0.0001 (—) | [+0.89943, +0.91633] | [+0.89901, +0.91757] | [+0.89912, +0.91863] | 1.098 | no / no / no | 0 | — |
| 915 | saved | S8 Table: sts DiD (nats) ts_demean global_fit | primary | scripts/14 | −0.10347 | 0.0132 (0.0132) | [−0.16780, −0.03594] | [−0.17838, −0.02666] | [−0.17948, −0.02746] | 1.151 | no / no / no | 11 | supplementary.md:151 |
| 916 | saved | S8 Table: TDMI DiD (nats) ts_demean global_fit | primary | scripts/14 | −0.13153 | 0.0039 (0.0039) | [−0.20014, −0.06102] | [−0.21037, −0.05240] | [−0.21115, −0.05192] | 1.135 | no / no / no | 12 | supplementary.md:151 |
| 917 | saved | S7 Table: mean_r DiD ts_gsr primary_bins11-28 | primary_bins11-28 | scripts/09 | −0.00335 | 0.0024 (0.0024) | [−0.00506, −0.00173] | [−0.00529, −0.00143] | [−0.00527, −0.00144] | 1.161 | no / no / no | 11 | supplementary.md:137 |
| 918 | saved | S7 Table: sts_global_fit_nats DiD ts_gsr primary_bins11-28 | primary_bins11-28 | scripts/09 | −0.08008 | 0.0071 (0.0071) | [−0.13025, −0.03104] | [−0.13624, −0.02506] | [−0.13728, −0.02288] | 1.121 | no / no / no | 12 | S1_Text.md:17; supplementary.md:137 |
| 919 | saved | S7 Table: mean_r DiD ts_gsr sensitivity_bins9-28 | sensitivity_bins9-28 | scripts/09 | −0.00320 | 0.0017 (0.0017) | [−0.00474, −0.00168] | [−0.00500, −0.00142] | [−0.00496, −0.00144] | 1.170 | no / no / no | 11 | — |
| 920 | saved | S7 Table: sts_global_fit_nats DiD ts_gsr sensitivity_bins9-28 | sensitivity_bins9-28 | scripts/09 | −0.07353 | 0.0112 (0.0112) | [−0.12368, −0.02357] | [−0.12895, −0.01900] | [−0.13005, −0.01701] | 1.098 | no / no / no | 12 | — |
| 921 | saved | S7 Table: mean_r DiD ts_gsr peak_bins9-14 | peak_bins9-14 | scripts/09 | −0.00322 | 0.0023 (0.0023) | [−0.00504, −0.00153] | [−0.00527, −0.00123] | [−0.00523, −0.00121] | 1.148 | no / no / no | 12 | supplementary.md:138 |
| 922 | saved | S7 Table: sts_global_fit_nats DiD ts_gsr peak_bins9-14 | peak_bins9-14 | scripts/09 | −0.07519 | 0.0044 (0.0044) | [−0.11143, −0.03352] | [−0.11624, −0.03025] | [−0.11959, −0.03080] | 1.104 | no / no / no | 13 | supplementary.md:138 |
| 923 | saved | S7 Table: mean_r DiD ts_demean primary_bins11-28 | primary_bins11-28 | scripts/09 | +0.05264 | 0.0470 (0.0470) | [+0.00734, +0.09762] | [+0.00083, +0.10409] | [+0.00120, +0.10407] | 1.144 | no / no / no | 4 | S3_Text.md:153; supplementary.md:134 |
| 924 | saved | S7 Table: sts_global_fit_nats DiD ts_demean primary_bins11-28 | primary_bins11-28 | scripts/09 | −0.10347 | 0.0132 (0.0132) | [−0.16781, −0.03571] | [−0.17838, −0.02666] | [−0.17948, −0.02746] | 1.149 | no / no / no | 11 | S1_Text.md:17; supplementary.md:134 |
| 925 | saved | S7 Table: mean_r DiD ts_demean sensitivity_bins9-28 | sensitivity_bins9-28 | scripts/09 | +0.05318 | 0.0322 (0.0322) | [+0.01133, +0.09299] | [+0.00592, +0.09999] | [+0.00631, +0.10005] | 1.152 | no / no / no | 4 | supplementary.md:135 |
| 926 | saved | S7 Table: sts_global_fit_nats DiD ts_demean sensitivity_bins9-28 | sensitivity_bins9-28 | scripts/09 | −0.09093 | 0.0175 (0.0175) | [−0.15355, −0.02540] | [−0.16398, −0.01685] | [−0.16493, −0.01692] | 1.148 | no / no / no | 11 | supplementary.md:135 |
| 927 | saved | S7 Table: mean_r DiD ts_demean peak_bins9-14 | peak_bins9-14 | scripts/09 | +0.07464 | 0.0046 (0.0046) | [+0.02928, +0.12816] | [+0.02322, +0.13137] | [+0.01867, +0.13061] | 1.094 | no / no / no | 3 | supplementary.md:136 |
| 928 | saved | S7 Table: sts_global_fit_nats DiD ts_demean peak_bins9-14 | peak_bins9-14 | scripts/09 | −0.08105 | 0.0348 (0.0348) | [−0.14458, −0.01765] | [−0.15449, −0.00682] | [−0.15458, −0.00752] | 1.163 | no / no / no | 11 | supplementary.md:136 |
| 929 | saved | Robustness C, placebo-fitted: (i) within-DMT step, primary (bins 11-28) (sts, ts_gsr) | bins | scripts/08 | −0.05077 | 0.1338 (0.1338) | [−0.10469, +0.01375] | [−0.11265, +0.01779] | [−0.11867, +0.01713] | 1.101 | yes / yes / yes | 11 | S1_Text.md:17 |
| 930 | saved | Robustness C, placebo-fitted: (ii) DMT minus PCB, bins 15-28 (sts, ts_gsr) | bins | scripts/08 | −0.11101 | 0.0005 (0.0005) | [−0.18030, −0.05927] | [−0.18158, −0.05183] | [−0.18139, −0.04063] | 1.072 | no / no / no | 13 | S1_Text.md:17 |
| 931 | saved | ΦR, placebo window 4 − window 1, raw series ts_gsr | W = 60 | S2 Text | −0.00840 | 0.0391 (0.0391) | [−0.01680, −0.00150] | [−0.01744, −0.00029] | [−0.01730, +0.00050] | 1.121 | no / no / yes | 11 | S2_Text.md:9 |
| 932 | saved | ΦR, placebo window 4 − window 1, raw series ts_demean | W = 60 | S2 Text | −0.00193 | 0.8883 (0.8883) | [−0.02490, +0.02460] | [−0.02892, +0.02694] | [−0.03045, +0.02659] | 1.128 | yes / yes / yes | 9 | — |

## S18 Table. The residual's response to changes in lagged structure, CCS-sts on the family, exposure per unit of spectral difference, the unequal-coefficient grid, and the pure-autocorrelation expectations of the new statistics (B23, B24)

Source: `notes/review_results/partB/diagnostic_alternatives_tables.md` and `diagnostic_alternatives.csv` (B23) and `bandpassed_expectations_tables.md` and `bandpassed_expectations.csv` (B24), both at a9d9ca4 (record, their pre-run entries and outcome entries of 23 September 2026). No data. B23: seed 20261120, one generator, parts (a)–(f) in order; the residual is the pool mean of sts on the true 4 × 4 matrix minus that on the AR(1) matrix of the measured a_x, a_y and q (the main text's substitution); q pool 20,000 draws of N(0, 0.3424) clipped to ±0.8; 63 checks, 0 failed. Its run log carries two `fsolve` RuntimeWarnings ("not making good progress", "xtol … too small"), which are expected: the (a3) polish keeps a point only if it improves on the least-squares solution, and every solve held r₁ and q to 10⁻¹⁰ (worst 9.95 × 10⁻¹³). Part (b) gives the (a5) base as differences from the unperturbed AR(1) pairs, so its levels are the sums (for example observed sts 0.71753 − 0.01423 = 0.70330), and the (a5) changes are taken against that base. B24: B17b's generator at its solved parameters, condition (i) only, 20 replicates; 10 checks, 0 failed. B23 and B24 were re-run independently by the planning session at a9d9ca4: `diagnostic_alternatives.csv` was reproduced byte for byte, the tables differ only in floating-point quantities near 10⁻¹⁶, and `bandpassed_expectations.csv` is identical apart from the sign of seven zeros.

### B23

### (a) Population residual changes, closed form (pool means; the unperturbed residual is 0 on the AR(1) family)

#### a = 0.85

| alternative | perturbation | residual change | share excluded (not positive definite) | notes |
|---|---|---|---|---|
| (a1) δ at fixed (a, q) | δ = +0.005 | +0.00105 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = -0.005 | +0.00073 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = +0.010 | +0.00393 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = -0.010 | +0.00329 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = +0.020 | +0.01609 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = -0.020 | +0.01482 | 0.0000 | |
| (a2) δ·sign(q) | δ = +0.005 × sign(q) | -0.01201 | 0.0000 | |
| (a2) δ·sign(q) | δ = -0.005 × sign(q) | +0.01379 | 0.0000 | |
| (a2) δ·sign(q) | δ = +0.010 × sign(q) | -0.02245 | 0.0000 | |
| (a2) δ·sign(q) | δ = -0.010 × sign(q) | +0.02968 | 0.0000 | |
| (a2) δ·sign(q) | δ = +0.020 × sign(q) | -0.03925 | 0.0000 | |
| (a2) δ·sign(q) | δ = -0.020 × sign(q) | +0.07015 | 0.0000 | |
| (a3) coupled family, r₁ and q held | c = +0.01 | +0.00237 | 0.0000 | grid step 0.001; step doubled: +0.00237 (difference 1.6e-16) |
| (a3) coupled family, r₁ and q held | c = +0.01 × sign(q) | -0.01671 | 0.0000 | grid step 0.001; step doubled: -0.01671 (difference 5.1e-15) |
| (a3) coupled family, r₁ and q held | c = -0.01 | +0.00188 | 0.0000 | grid step 0.001; step doubled: +0.00188 (difference 2.9e-16) |
| (a3) coupled family, r₁ and q held | c = -0.01 × sign(q) | +0.02097 | 0.0000 | grid step 0.001; step doubled: +0.02097 (difference 4.9e-15) |
| (a3) coupled family, r₁ and q held | c = +0.02 | +0.00912 | 0.0000 | grid step 0.001; step doubled: +0.00912 (difference 1.2e-16) |
| (a3) coupled family, r₁ and q held | c = +0.02 × sign(q) | -0.02960 | 0.0000 | grid step 0.001; step doubled: -0.02960 (difference 1.0e-14) |
| (a3) coupled family, r₁ and q held | c = -0.02 | +0.00813 | 0.0000 | grid step 0.001; step doubled: +0.00813 (difference 7.5e-16) |
| (a3) coupled family, r₁ and q held | c = -0.02 × sign(q) | +0.04684 | 0.0000 | grid step 0.001; step doubled: +0.04684 (difference 9.7e-15) |

(a4) B17's construction at a = 0.85: A = [[a, c], [c, a]], unit innovations with correlation q (the c = 0 lag-0 correlation).

| c | Δr₁ | Δ mean q | Δ mean \|q\| | mean δ_sym | residual change | residual / (mean δ_sym)² |
|---|---|---|---|---|---|---|
| +0.01 | +0.00051 | +0.05437 | +0.00320 | +0.00885 | -0.00190 | -24.28 |
| +0.02 | +0.00211 | +0.10899 | +0.01320 | +0.01755 | -0.00815 | -26.45 |
| +0.03 | +0.00482 | +0.16409 | +0.03016 | +0.02597 | -0.01893 | -28.08 |
| -0.02 | +0.00225 | -0.10891 | +0.01488 | -0.01753 | -0.00913 | -29.71 |

(a5) shared slow component at a = 0.85 (λ = |q|, a_n = a − 0.06λ, a_s = a_n + 0.06): base residual -0.02724, base mean(sign(q)·δ_sym) +0.00950.

| change | Δr₁ | Δ mean(sign(q)·δ_sym) | residual change | residual change / Δr₁ | share excluded |
|---|---|---|---|---|---|
| Δa_s = −0.01 | -0.00272 | -0.00158 | +0.00466 | -1.716 | 0.0000 |
| Δa_s = −0.02 | -0.00543 | -0.00317 | +0.00928 | -1.708 | 0.0000 |
| Δa_s = −0.03 | -0.00815 | -0.00475 | +0.01385 | -1.700 | 0.0000 |
| λ → 0.9λ | -0.00163 | -0.00034 | +0.00471 | -2.892 | 0.0000 |

(a6) pure Δa = −0.015 at a = 0.85: largest |residual| over the pool 0.0e+00.

#### a = 0.8632

| alternative | perturbation | residual change | share excluded (not positive definite) | notes |
|---|---|---|---|---|
| (a1) δ at fixed (a, q) | δ = +0.005 | +0.00126 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = -0.005 | +0.00091 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = +0.010 | +0.00476 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = -0.010 | +0.00407 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = +0.020 | +0.01994 | 0.0000 | |
| (a1) δ at fixed (a, q) | δ = -0.020 | +0.01856 | 0.0000 | |
| (a2) δ·sign(q) | δ = +0.005 × sign(q) | -0.01307 | 0.0000 | |
| (a2) δ·sign(q) | δ = -0.005 × sign(q) | +0.01524 | 0.0000 | |
| (a2) δ·sign(q) | δ = +0.010 × sign(q) | -0.02425 | 0.0000 | |
| (a2) δ·sign(q) | δ = -0.010 × sign(q) | +0.03308 | 0.0000 | |
| (a2) δ·sign(q) | δ = +0.020 × sign(q) | -0.04170 | 0.0000 | |
| (a2) δ·sign(q) | δ = -0.020 × sign(q) | +0.08019 | 0.0000 | |
| (a3) coupled family, r₁ and q held | c = +0.01 | +0.00287 | 0.0000 | grid step 0.001; step doubled: +0.00287 (difference 1.8e-16) |
| (a3) coupled family, r₁ and q held | c = +0.01 × sign(q) | -0.01807 | 0.0000 | grid step 0.001; step doubled: -0.01807 (difference 5.3e-15) |
| (a3) coupled family, r₁ and q held | c = -0.01 | +0.00234 | 0.0000 | grid step 0.001; step doubled: +0.00234 (difference 2.9e-16) |
| (a3) coupled family, r₁ and q held | c = -0.01 × sign(q) | +0.02328 | 0.0000 | grid step 0.001; step doubled: +0.02328 (difference 5.2e-15) |
| (a3) coupled family, r₁ and q held | c = +0.02 | +0.01112 | 0.0000 | grid step 0.001; step doubled: +0.01112 (difference 1.8e-16) |
| (a3) coupled family, r₁ and q held | c = +0.02 × sign(q) | -0.03149 | 0.0000 | grid step 0.001; step doubled: -0.03149 (difference 1.1e-14) |
| (a3) coupled family, r₁ and q held | c = -0.02 | +0.01002 | 0.0000 | grid step 0.001; step doubled: +0.01002 (difference 7.4e-16) |
| (a3) coupled family, r₁ and q held | c = -0.02 × sign(q) | +0.05263 | 0.0000 | grid step 0.001; step doubled: +0.05263 (difference 1.0e-14) |

(a4) B17's construction at a = 0.8632: A = [[a, c], [c, a]], unit innovations with correlation q (the c = 0 lag-0 correlation).

| c | Δr₁ | Δ mean q | Δ mean \|q\| | mean δ_sym | residual change | residual / (mean δ_sym)² |
|---|---|---|---|---|---|---|
| +0.01 | +0.00057 | +0.06012 | +0.00393 | +0.00884 | -0.00230 | -29.48 |
| +0.02 | +0.00234 | +0.12056 | +0.01623 | +0.01751 | -0.00984 | -32.09 |
| +0.03 | +0.00534 | +0.18162 | +0.03698 | +0.02582 | -0.02287 | -34.31 |
| -0.02 | +0.00248 | -0.12046 | +0.01809 | -0.01748 | -0.01091 | -35.70 |

(a5) shared slow component at a = 0.8632 (λ = |q|, a_n = a − 0.06λ, a_s = a_n + 0.06): base residual -0.02942, base mean(sign(q)·δ_sym) +0.00950.

| change | Δr₁ | Δ mean(sign(q)·δ_sym) | residual change | residual change / Δr₁ | share excluded |
|---|---|---|---|---|---|
| Δa_s = −0.01 | -0.00272 | -0.00158 | +0.00502 | -1.850 | 0.0000 |
| Δa_s = −0.02 | -0.00543 | -0.00317 | +0.01001 | -1.842 | 0.0000 |
| Δa_s = −0.03 | -0.00815 | -0.00475 | +0.01495 | -1.834 | 0.0000 |
| λ → 0.9λ | -0.00163 | -0.00034 | +0.00514 | -3.152 | 0.0000 |

(a6) pure Δa = −0.015 at a = 0.8632: largest |residual| over the pool 0.0e+00.

### (b) W = 60 simulation: changes against the unperturbed pairs (common random numbers; mean ± SE)

3000 pairs, q ~ N(0, 0.3424) clipped to ±0.8, a = 0.85; runs of 840 samples after a burn-in of 200; 14 windows of 60; the other run an independent realisation. SE over pairs of each pair's 14-window mean; B's SE over the 14 windows.

Unperturbed AR(1) pairs, levels: observed sts +0.71753; AR(1)-substituted sts +0.78780; residual -0.07027; r₁ +0.78638; A_other -0.00291; A_same -0.00117; D -0.01137; B +0.06122.

| condition | pairs excluded | Δ observed sts | Δ AR(1)-substituted sts | Δ residual | Δ r₁ | Δ A_other | Δ A_same | Δ D | Δ B | residual change / Δr₁ |
|---|---|---|---|---|---|---|---|---|---|---|
| (i) Δa = −0.015 | 0 | -0.04240 ± 0.00011 | -0.04777 ± 0.00012 | +0.00537 ± 0.00009 | -0.01377 ± 0.00002 | +0.00001 ± 0.00004 | +0.00001 ± 0.00005 | +0.00015 ± 0.00007 | +0.00034 ± 0.00004 | -0.390 |
| (a1) δ = +0.02 | 0 | +0.00521 ± 0.00078 | -0.00457 ± 0.00035 | +0.00978 ± 0.00093 | -0.00092 ± 0.00004 | +0.00041 ± 0.00034 | +0.00017 ± 0.00034 | +0.00032 ± 0.00014 | +0.00045 ± 0.00010 | -10.628 |
| (a1) δ = −0.02 | 0 | +0.00608 ± 0.00079 | -0.00409 ± 0.00037 | +0.01016 ± 0.00095 | -0.00089 ± 0.00004 | +0.00059 ± 0.00034 | +0.00070 ± 0.00034 | +0.00041 ± 0.00013 | +0.00032 ± 0.00011 | -11.358 |
| (a2) δ = +0.01 × sign(q) | 0 | -0.01064 ± 0.00028 | +0.00290 ± 0.00015 | -0.01354 ± 0.00030 | -0.00023 ± 0.00002 | +0.00782 ± 0.00011 | +0.00781 ± 0.00010 | -0.00007 ± 0.00006 | +0.01661 ± 0.00010 | +58.914 |
| (a2) δ = −0.01 × sign(q) | 0 | +0.01339 ± 0.00033 | -0.00511 ± 0.00020 | +0.01850 ± 0.00038 | -0.00021 ± 0.00002 | -0.00748 ± 0.00010 | -0.00762 ± 0.00010 | +0.00039 ± 0.00014 | -0.01680 ± 0.00009 | -87.358 |
| (a3) c = +0.02, r₁ and q held | 0 | +0.00335 ± 0.00047 | -0.00342 ± 0.00028 | +0.00677 ± 0.00055 | -0.00069 ± 0.00004 | +0.00014 ± 0.00031 | -0.00008 ± 0.00031 | +0.00010 ± 0.00009 | -0.00004 ± 0.00008 | -9.879 |
| (a4) c = +0.02, B17's construction | 0 | -0.00011 ± 0.00040 | +0.00468 ± 0.00036 | -0.00479 ± 0.00065 | +0.00129 ± 0.00012 | +0.00387 ± 0.00034 | +0.00401 ± 0.00035 | +0.00003 ± 0.00007 | -0.00165 ± 0.00012 | -3.722 |
| (a4) c = -0.02, B17's construction | 0 | +0.00006 ± 0.00040 | +0.00552 ± 0.00038 | -0.00546 ± 0.00066 | +0.00134 ± 0.00012 | +0.00405 ± 0.00033 | +0.00440 ± 0.00034 | -0.00010 ± 0.00012 | -0.00191 ± 0.00010 | -4.074 |
| (a5) base, against the unperturbed AR(1) pairs (levels differ by construction) | 0 | -0.01423 | +0.00041 | -0.01464 | -0.00170 | +0.00793 | +0.00802 | -0.00027 | +0.02031 | — |
| (a5) Δa_s = −0.03 (against the (a5) base) | 0 | -0.01470 ± 0.00020 | -0.02489 ± 0.00038 | +0.01020 ± 0.00023 | -0.00642 ± 0.00010 | -0.00371 ± 0.00006 | -0.00377 ± 0.00006 | +0.00008 ± 0.00005 | -0.01066 ± 0.00007 | -1.587 |
| (a5) λ → 0.9λ (against the (a5) base) | 0 | +0.00354 ± 0.00016 | -0.00037 ± 0.00013 | +0.00391 ± 0.00012 | -0.00143 ± 0.00003 | -0.00010 ± 0.00005 | -0.00003 ± 0.00005 | +0.00019 ± 0.00008 | +0.01095 ± 0.00007 | -2.727 |


### (c) Population CCS-sts (published mask) and MMI-sts on the symmetric AR(1) family

One series of 1000000 samples per point, fitted globally; the same two standard-normal streams at every point.

| r₁ | q | CCS-sts | MMI-sts (the fit) | MMI-sts (closed form) |
|---|---|---|---|---|
| 0.80 | 0.10 | -0.01535 | +1.01701 | +1.01844 |
| 0.83 | 0.10 | -0.01577 | +1.16230 | +1.16418 |
| 0.85 | 0.10 | -0.01597 | +1.27600 | +1.27831 |
| 0.87 | 0.10 | -0.01607 | +1.40763 | +1.41048 |
| 0.90 | 0.10 | -0.01585 | +1.65264 | +1.65666 |
| 0.80 | 0.25 | -0.03041 | +1.00004 | +1.00124 |
| 0.83 | 0.25 | -0.03135 | +1.14405 | +1.14564 |
| 0.85 | 0.25 | -0.03175 | +1.25689 | +1.25883 |
| 0.87 | 0.25 | -0.03189 | +1.38766 | +1.39005 |
| 0.90 | 0.25 | -0.03130 | +1.63141 | +1.63476 |
| 0.80 | 0.40 | -0.03412 | +0.96672 | +0.96764 |
| 0.83 | 0.40 | -0.03558 | +1.10804 | +1.10925 |
| 0.85 | 0.40 | -0.03613 | +1.21904 | +1.22051 |
| 0.87 | 0.40 | -0.03637 | +1.34795 | +1.34974 |
| 0.90 | 0.40 | -0.03547 | +1.58889 | +1.59133 |

Central-difference slope of CCS-sts in r₁ at q = 0.25 (0.83 to 0.87): -0.0134 per unit r₁ (MMI-sts from the same fits: +6.0903). Change of CCS-sts from Δa = −0.015 at (0.85, 0.25): +0.00034 (MMI-sts: -0.08607).

### (d) Exposure per unit of spectral difference: a flat band against the same band tilted by exp(−βf²), q = 0.25

| band | TR (s) | r₁ flat | β | Δr₁ | Δsts | Δsts / Δr₁ |
|---|---|---|---|---|---|---|
| 0.008–0.09 Hz | 2 | 0.7807 | 100 | +0.03759 | +0.1652 | +4.39 |
| 0.008–0.09 Hz | 2 | 0.7807 | 200 | +0.06887 | +0.3353 | +4.87 |
| 0.008–0.09 Hz | 2 | 0.7807 | 400 | +0.11319 | +0.6581 | +5.81 |
| 0.008–0.09 Hz | 1.838 | 0.8129 | 100 | +0.03221 | +0.1696 | +5.27 |
| 0.008–0.09 Hz | 1.838 | 0.8129 | 200 | +0.05900 | +0.3436 | +5.82 |
| 0.008–0.09 Hz | 1.838 | 0.8129 | 400 | +0.09690 | +0.6722 | +6.94 |
| 0.008–0.09 Hz | 0.72 | 0.9699 | 100 | +0.00528 | +0.1904 | +36.02 |
| 0.008–0.09 Hz | 0.72 | 0.9699 | 200 | +0.00966 | +0.3822 | +39.57 |
| 0.008–0.09 Hz | 0.72 | 0.9699 | 400 | +0.01581 | +0.7379 | +46.66 |
| 0.0025–0.05 Hz | 2 | 0.9321 | 100 | +0.00410 | +0.0599 | +14.61 |
| 0.0025–0.05 Hz | 2 | 0.9321 | 200 | +0.00800 | +0.1208 | +15.09 |
| 0.0025–0.05 Hz | 2 | 0.9321 | 400 | +0.01517 | +0.2440 | +16.09 |
| 0.0025–0.05 Hz | 2.4 | 0.9031 | 100 | +0.00583 | +0.0586 | +10.06 |
| 0.0025–0.05 Hz | 2.4 | 0.9031 | 200 | +0.01138 | +0.1182 | +10.39 |
| 0.0025–0.05 Hz | 2.4 | 0.9031 | 400 | +0.02157 | +0.2392 | +11.09 |
| 0.0025–0.05 Hz | 2.6 | 0.8868 | 100 | +0.00679 | +0.0579 | +8.52 |
| 0.0025–0.05 Hz | 2.6 | 0.8868 | 200 | +0.01326 | +0.1168 | +8.81 |
| 0.0025–0.05 Hz | 2.6 | 0.8868 | 400 | +0.02514 | +0.2364 | +9.40 |
| 0.0025–0.05 Hz | 3 | 0.8510 | 100 | +0.00890 | +0.0563 | +6.32 |
| 0.0025–0.05 Hz | 3 | 0.8510 | 200 | +0.01737 | +0.1136 | +6.54 |
| 0.0025–0.05 Hz | 3 | 0.8510 | 400 | +0.03295 | +0.2303 | +6.99 |
| 0.0025–0.05 Hz | 1.25 | 0.9732 | 100 | +0.00163 | +0.0617 | +37.86 |
| 0.0025–0.05 Hz | 1.25 | 0.9732 | 200 | +0.00318 | +0.1243 | +39.08 |
| 0.0025–0.05 Hz | 1.25 | 0.9732 | 400 | +0.00603 | +0.2508 | +41.62 |
| 0.01–0.1 Hz | 2 | 0.7301 | 100 | +0.05468 | +0.1926 | +3.52 |
| 0.01–0.1 Hz | 2 | 0.7301 | 200 | +0.09796 | +0.3908 | +3.99 |
| 0.01–0.1 Hz | 2 | 0.7301 | 400 | +0.15397 | +0.7517 | +4.88 |
| 0.01–0.1 Hz | 1 | 0.9284 | 100 | +0.01491 | +0.2249 | +15.08 |
| 0.01–0.1 Hz | 1 | 0.9284 | 200 | +0.02663 | +0.4497 | +16.89 |
| 0.01–0.1 Hz | 1 | 0.9284 | 400 | +0.04166 | +0.8477 | +20.35 |
| 0.01–0.1 Hz | 1.2 | 0.8978 | 100 | +0.02120 | +0.2201 | +10.38 |
| 0.01–0.1 Hz | 1.2 | 0.8978 | 200 | +0.03789 | +0.4410 | +11.64 |
| 0.01–0.1 Hz | 1.2 | 0.8978 | 400 | +0.05930 | +0.8334 | +14.05 |
| 0.01–0.08 Hz (this study) | 2 | 0.8174 | 100 | +0.02387 | +0.1257 | +5.27 |
| 0.01–0.08 Hz (this study) | 2 | 0.8174 | 200 | +0.04484 | +0.2549 | +5.68 |
| 0.01–0.08 Hz (this study) | 2 | 0.8174 | 400 | +0.07761 | +0.5071 | +6.53 |

### (e) Population Δr₁ and Δsts under condition (i)

Band-passed generator (B17b; β̄ = 185.4, σ_q = 0.2637, β̄_post = 105.7 from calibration_filtered_tables.md; filter edges 0.0064–0.080 Hz; 20000 pairs; exact circular lag-1 autocorrelation on the 840-sample grid): population r₁ 0.8678 → 0.8515 (Δr₁ -0.01629); population sts 1.3795 → 1.2669 (Δsts -0.11263).
AR(1) generator (B17's (i), simulated: calibration.csv holds no window-level r₁; 3000 pairs): population Δr₁ −0.015 by construction; window-level Δr₁ DiD (windows 6–14 minus 1–4, DMT minus placebo) -0.01243 ± 0.00101 (SE over pairs).

### (f) Unequal coefficients: mean a × q × |a_x − a_y| (0 to 0.10 in steps of 0.0005)

| mean a | q | max \|str − min(xtx, yty)\| | min(rts − str) | max(sts − (xtx + yty + rtr)) | asymmetry at which sts − (xtx + yty) first turns negative |
|---|---|---|---|---|---|
| 0.80 | 0.05 | 3.3e-16 | +0.0e+00 | -2.2e-16 | 0.0005 |
| 0.80 | 0.10 | 3.3e-16 | +1.1e-16 | +2.2e-16 | 0.0015 |
| 0.80 | 0.25 | 2.8e-16 | +0.0e+00 | +0.0e+00 | 0.0095 |
| 0.80 | 0.40 | 3.3e-16 | +0.0e+00 | -1.1e-16 | 0.0255 |
| 0.80 | 0.50 | 3.3e-16 | +0.0e+00 | +3.3e-16 | 0.0420 |
| 0.80 | 0.70 | 2.2e-16 | -1.1e-16 | +1.1e-16 | none |
| 0.85 | 0.05 | 4.4e-16 | +2.2e-16 | +0.0e+00 | 0.0005 |
| 0.85 | 0.10 | 4.4e-16 | +0.0e+00 | +0.0e+00 | 0.0015 |
| 0.85 | 0.25 | 4.4e-16 | +0.0e+00 | +0.0e+00 | 0.0080 |
| 0.85 | 0.40 | 4.4e-16 | +0.0e+00 | +0.0e+00 | 0.0210 |
| 0.85 | 0.50 | 3.3e-16 | +0.0e+00 | -2.2e-16 | 0.0345 |
| 0.85 | 0.70 | 3.3e-16 | -1.1e-16 | -2.2e-16 | 0.0915 |
| 0.90 | 0.05 | 5.6e-16 | +0.0e+00 | +2.2e-16 | 0.0005 |
| 0.90 | 0.10 | 5.6e-16 | +0.0e+00 | -6.7e-16 | 0.0010 |
| 0.90 | 0.25 | 5.6e-16 | +0.0e+00 | +0.0e+00 | 0.0060 |
| 0.90 | 0.40 | 5.6e-16 | -1.1e-16 | +4.4e-16 | 0.0150 |
| 0.90 | 0.50 | 5.6e-16 | +0.0e+00 | -2.2e-16 | 0.0250 |
| 0.90 | 0.70 | 4.4e-16 | -2.2e-16 | -4.4e-16 | 0.0680 |


### B24

### The check against B17b's condition (i), W = 60

| DiD | B24 (mean ± SD) | B17b (committed) | within one of B17b's SDs |
|---|---|---|---|
| observed sts | -0.09441 ± 0.00222 | -0.09400 ± 0.00280 | yes |
| AR(1)-substituted sts | -0.09719 ± 0.00205 | -0.09660 ± 0.00270 | yes |
| residual | +0.00279 ± 0.00122 | +0.00270 ± 0.00140 | yes |
| RMS δ_anti | +0.00669 ± 0.00100 | +0.00641 ± 0.00104 | yes |

### B17b's statistics, condition (i)

| estimator | sts level (pre) | sts DiD | AR(1)-substituted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |
|---|---|---|---|---|---|---|---|
| W60 | 1.1881 | -0.0944 ± 0.0022 | -0.0972 ± 0.0020 | +0.0028 ± 0.0012 | 0.121; 0.70 | -0.00008 ± 0.00032 | +0.00669 ± 0.00100 |
| global (run-level substitution) | 1.3261 | -0.1050 ± 0.0031 | +0.0000 ± 0.0000 | -0.1050 ± 0.0031 | 0.000; 1.00 | — | — |
| global (period-level substitution) | 1.3261 | -0.1050 ± 0.0031 | -0.1091 ± 0.0028 | +0.0041 ± 0.0016 | 0.112; 0.50 | — | — |

### B22's statistics under a pure autocorrelation change (W = 60)

| statistic | DMT pre-injection level | DiD |
|---|---|---|
| A_other (sign from the other run) | -0.00028 ± 0.00019 | +0.00001 ± 0.00031 |
| A_same (sign from the same run) | -0.00001 ± 0.00018 | +0.00004 ± 0.00037 |
| window-sign statistic (selected) | +0.00340 ± 0.00015 | -0.00087 ± 0.00033 |
| B, slope of δ_sym on q | +0.01092 ± 0.00045 | -0.00263 ± 0.00077 |
| D, response to δ_anti alone | -0.03508 ± 0.00030 | -0.00100 ± 0.00041 |
| Sym, response to δ_sym alone | -0.00030 ± 0.00049 | +0.00373 ± 0.00092 |
| D + Sym | -0.03538 ± 0.00056 | +0.00273 ± 0.00114 |
| window-level mean pair r₁ | +0.86339 ± 0.00028 | -0.01540 ± 0.00035 |

Sym's DiD minus (the residual DiD − D's DiD): -0.00006 ± 0.00017.
