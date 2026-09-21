# The CCS-sts increase decomposed: mask-selected share and double co-information of the rejected samples (partB18_ccs_decomposition.py)
git=f1f5fcc

Per pair and period CCS-sts = −(1 − s) c̄_rej exactly (samples of the period's windows or bins pooled): s the mask-selected share, c̄_rej the mean double co-information over the rejected samples. Masks: code (phyid's), pub (published). The pre → post change of the pair-mean CCS-sts is split per pair into c̄_pre Δs (share term), −(1 − s_pre) Δc̄ (co-information term) and +Δs Δc̄ (interaction), averaged over pairs. DiD = DMT minus placebo (pre = windows 1–4 / bins 1–8; post = windows 6–14 / bins 11–28). Seed 20261120; bootstrap 10000 draws; exact sign-flip p over 2^14. Region 20 excluded.

## ts_gsr, W60

| mask | quantity | DMT pre | DMT post | PCB pre | PCB post | DMT change | PCB change | DiD [95 % CI], sign-flip p, neg/14 |
|---|---|---|---|---|---|---|---|---|
| code | s (selected share) | 0.2994 | 0.2838 | 0.2957 | 0.3005 | -0.01560 | +0.00479 | -0.02039 [-0.03210, -0.00768], p = 0.0104, 11 |
| code | c̄_rej (nats) | 0.0555 | 0.0524 | 0.0509 | 0.0545 | -0.00314 | +0.00362 | -0.00676 [-0.01227, -0.00111], p = 0.0422, 10 |
| code | CCS-sts (nats) | -0.0387 | -0.0375 | -0.0357 | -0.0382 | +0.00119 | -0.00243 | +0.00362 [-0.00010, +0.00724], p = 0.0845, 4 |
| code | share term c̄_pre Δs | — | — | — | — | -0.00147 | -0.00026 | -0.00122 [-0.00202, -0.00038], p = 0.0188, 11 |
| code | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.00176 | -0.00299 | +0.00475 [+0.00072, +0.00858], p = 0.0432, 4 |
| code | interaction Δs Δc̄ | — | — | — | — | +0.00091 | +0.00082 | +0.00009 [-0.00016, +0.00034], p = 0.5233, 4 |
| code | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 1.7e-18 |
| pub | s (selected share) | 0.3569 | 0.3405 | 0.3545 | 0.3591 | -0.01637 | +0.00459 | -0.02096 [-0.03262, -0.00829], p = 0.0089, 11 |
| pub | c̄_rej (nats) | 0.0755 | 0.0700 | 0.0709 | 0.0749 | -0.00546 | +0.00398 | -0.00944 [-0.01613, -0.00236], p = 0.0256, 11 |
| pub | CCS-sts (nats) | -0.0480 | -0.0459 | -0.0454 | -0.0477 | +0.00212 | -0.00226 | +0.00438 [+0.00033, +0.00820], p = 0.0562, 3 |
| pub | share term c̄_pre Δs | — | — | — | — | -0.00176 | +0.00003 | -0.00179 [-0.00287, -0.00066], p = 0.0127, 11 |
| pub | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.00311 | -0.00282 | +0.00593 [+0.00143, +0.01018], p = 0.0272, 2 |
| pub | interaction Δs Δc̄ | — | — | — | — | +0.00077 | +0.00053 | +0.00024 [-0.00003, +0.00052], p = 0.1178, 4 |
| pub | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 1.7e-18 |

## ts_gsr, global

| mask | quantity | DMT pre | DMT post | PCB pre | PCB post | DMT change | PCB change | DiD [95 % CI], sign-flip p, neg/14 |
|---|---|---|---|---|---|---|---|---|
| code | s (selected share) | 0.2872 | 0.3077 | 0.3099 | 0.3024 | +0.02055 | -0.00751 | +0.02806 [+0.01339, +0.04222], p = 0.0035, 2 |
| code | c̄_rej (nats) | 0.0491 | 0.0310 | 0.0287 | 0.0406 | -0.01813 | +0.01195 | -0.03008 [-0.03868, -0.02219], p = 0.0001, 14 |
| code | CCS-sts (nats) | -0.0335 | -0.0200 | -0.0191 | -0.0267 | +0.01347 | -0.00755 | +0.02102 [+0.01533, +0.02693], p = 0.0001, 0 |
| code | share term c̄_pre Δs | — | — | — | — | +0.00212 | +0.00046 | +0.00165 [+0.00080, +0.00254], p = 0.0033, 2 |
| code | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.01295 | -0.00686 | +0.01981 [+0.01468, +0.02530], p = 0.0001, 0 |
| code | interaction Δs Δc̄ | — | — | — | — | -0.00160 | -0.00115 | -0.00045 [-0.00086, -0.00006], p = 0.0588, 11 |
| code | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 6.9e-18 |
| pub | s (selected share) | 0.3405 | 0.3717 | 0.3740 | 0.3630 | +0.03120 | -0.01097 | +0.04217 [+0.02551, +0.05845], p = 0.0007, 2 |
| pub | c̄_rej (nats) | 0.0570 | 0.0408 | 0.0385 | 0.0515 | -0.01622 | +0.01299 | -0.02921 [-0.03811, -0.02105], p = 0.0001, 14 |
| pub | CCS-sts (nats) | -0.0358 | -0.0236 | -0.0230 | -0.0305 | +0.01221 | -0.00745 | +0.01966 [+0.01416, +0.02540], p = 0.0002, 1 |
| pub | share term c̄_pre Δs | — | — | — | — | +0.00314 | +0.00039 | +0.00275 [+0.00160, +0.00395], p = 0.0010, 1 |
| pub | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.01102 | -0.00640 | +0.01741 [+0.01270, +0.02243], p = 0.0001, 0 |
| pub | interaction Δs Δc̄ | — | — | — | — | -0.00195 | -0.00145 | -0.00050 [-0.00099, -0.00005], p = 0.0618, 9 |
| pub | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 3.5e-18 |

## ts_demean, W60

| mask | quantity | DMT pre | DMT post | PCB pre | PCB post | DMT change | PCB change | DiD [95 % CI], sign-flip p, neg/14 |
|---|---|---|---|---|---|---|---|---|
| code | s (selected share) | 0.3003 | 0.3042 | 0.2950 | 0.3024 | +0.00394 | +0.00746 | -0.00352 [-0.01521, +0.00762], p = 0.5747, 8 |
| code | c̄_rej (nats) | 0.0351 | 0.0250 | 0.0276 | 0.0379 | -0.01010 | +0.01031 | -0.02041 [-0.03321, -0.00891], p = 0.0042, 12 |
| code | CCS-sts (nats) | -0.0255 | -0.0192 | -0.0206 | -0.0277 | +0.00633 | -0.00704 | +0.01337 [+0.00545, +0.02229], p = 0.0052, 3 |
| code | share term c̄_pre Δs | — | — | — | — | -0.00049 | -0.00030 | -0.00019 [-0.00097, +0.00054], p = 0.6429, 7 |
| code | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.00651 | -0.00745 | +0.01396 [+0.00572, +0.02311], p = 0.0046, 3 |
| code | interaction Δs Δc̄ | — | — | — | — | +0.00030 | +0.00071 | -0.00040 [-0.00109, +0.00028], p = 0.2893, 9 |
| code | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 6.9e-18 |
| pub | s (selected share) | 0.3624 | 0.3664 | 0.3587 | 0.3643 | +0.00395 | +0.00566 | -0.00171 [-0.01433, +0.01052], p = 0.8014, 8 |
| pub | c̄_rej (nats) | 0.0586 | 0.0497 | 0.0502 | 0.0618 | -0.00891 | +0.01160 | -0.02052 [-0.03217, -0.00993], p = 0.0028, 12 |
| pub | CCS-sts (nats) | -0.0378 | -0.0327 | -0.0331 | -0.0400 | +0.00510 | -0.00687 | +0.01197 [+0.00522, +0.01944], p = 0.0040, 3 |
| pub | share term c̄_pre Δs | — | — | — | — | -0.00021 | +0.00014 | -0.00035 [-0.00138, +0.00063], p = 0.5240, 8 |
| pub | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.00517 | -0.00727 | +0.01245 [+0.00560, +0.01982], p = 0.0033, 2 |
| pub | interaction Δs Δc̄ | — | — | — | — | +0.00014 | +0.00027 | -0.00012 [-0.00075, +0.00048], p = 0.6893, 7 |
| pub | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 6.9e-18 |

## ts_demean, global

| mask | quantity | DMT pre | DMT post | PCB pre | PCB post | DMT change | PCB change | DiD [95 % CI], sign-flip p, neg/14 |
|---|---|---|---|---|---|---|---|---|
| code | s (selected share) | 0.2905 | 0.3240 | 0.3076 | 0.3003 | +0.03351 | -0.00726 | +0.04077 [+0.02350, +0.05883], p = 0.0004, 1 |
| code | c̄_rej (nats) | 0.0426 | 0.0103 | 0.0129 | 0.0287 | -0.03231 | +0.01572 | -0.04803 [-0.06454, -0.03194], p = 0.0001, 14 |
| code | CCS-sts (nats) | -0.0297 | -0.0072 | -0.0096 | -0.0192 | +0.02252 | -0.00964 | +0.03216 [+0.02145, +0.04336], p = 0.0001, 0 |
| code | share term c̄_pre Δs | — | — | — | — | +0.00300 | +0.00084 | +0.00217 [+0.00106, +0.00335], p = 0.0017, 2 |
| code | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.02299 | -0.00898 | +0.03197 [+0.02115, +0.04348], p = 0.0001, 0 |
| code | interaction Δs Δc̄ | — | — | — | — | -0.00348 | -0.00150 | -0.00198 [-0.00376, -0.00048], p = 0.0233, 10 |
| code | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 6.9e-18 |
| pub | s (selected share) | 0.3584 | 0.4049 | 0.3833 | 0.3712 | +0.04649 | -0.01214 | +0.05864 [+0.03652, +0.08176], p = 0.0004, 1 |
| pub | c̄_rej (nats) | 0.0624 | 0.0235 | 0.0247 | 0.0445 | -0.03887 | +0.01974 | -0.05862 [-0.08014, -0.03753], p = 0.0001, 14 |
| pub | CCS-sts (nats) | -0.0386 | -0.0137 | -0.0156 | -0.0262 | +0.02485 | -0.01067 | +0.03552 [+0.02295, +0.04858], p = 0.0001, 0 |
| pub | share term c̄_pre Δs | — | — | — | — | +0.00537 | +0.00094 | +0.00443 [+0.00238, +0.00680], p = 0.0005, 1 |
| pub | co-information term −(1 − s_pre) Δc̄ | — | — | — | — | +0.02487 | -0.00946 | +0.03432 [+0.02168, +0.04778], p = 0.0001, 0 |
| pub | interaction Δs Δc̄ | — | — | — | — | -0.00538 | -0.00215 | -0.00324 [-0.00626, -0.00084], p = 0.0210, 9 |
| pub | exactness of the split | — | — | — | — | — | — | max abs(sum of terms − change) = 1.4e-17 |

Check of the identity CCS-sts = −(1 − s) c̄_rej against PairPhiID.atoms_ccs (phyid's mask; subject 1 DMT windows 1 and 6, per pair): max |difference| = 2.2e-16.

Rule of the pre-run entry: the plain reading (which of the share and the co-information terms carries the CCS-sts change) replaces "no established reading"; it does not make the CCS increase a finding about DMT. No prediction was recorded.
