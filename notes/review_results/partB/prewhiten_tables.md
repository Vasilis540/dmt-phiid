# The atoms and the DMT contrast after prewhitening (partB16_prewhiten.py)
git=f1f5fcc

Whitening per region and run: 'arp' = residuals of the region's AR(p) fit, p by BIC over 1–5; 'ar1' = p = 1. The first p TRs of each run are dropped (non-finite). Atoms as partB2_ccs_run.py (MMI: PairPhiID.atoms_mean / atoms_bins; CCS: atoms_ccs, phyid's mask); inference as the primary (rev_inference.Engine, seed 20261120); the diagnostic as partB4 (per-pair AR(1) prediction from the whitened window's a_x, a_y, q). Level = DMT pre-injection (windows 1–4; bins 1–8); DiD = post minus pre, DMT minus placebo.

## arp ts_gsr W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0172 | +0.0012 (6) | +0.0262 | +0.0017 (6) |
| rtx | +0.0212 | +0.0022 (4) | +0.0071 | +0.0003 (6) |
| rty | +0.0213 | +0.0015 (2) | +0.0073 | -0.0003 (8) |
| rts | +0.0857 | -0.0073 (7) | -0.0121 | -0.0007 (8) |
| xtr | +0.0226 | +0.0028 (3) | +0.0093 | +0.0009 (4) |
| xtx | +0.1034 | -0.0236 (8) | +0.1218 | -0.0203 (8) |
| xty | +0.0114 | +0.0029 (5) | +0.0297 | +0.0062 (2) |
| xts | -0.0393 | +0.0074 (7) | +0.0543 | -0.0007 (6) |
| ytr | +0.0232 | +0.0013 (5) | +0.0097 | -0.0002 (6) |
| ytx | +0.0113 | +0.0028 (5) | +0.0299 | +0.0057 (2) |
| yty | +0.1026 | -0.0179 (9) | +0.1211 | -0.0149 (8) |
| yts | -0.0394 | +0.0099 (7) | +0.0539 | +0.0022 (6) |
| str | +0.0882 | -0.0068 (7) | -0.0093 | -0.0002 (6) |
| stx | -0.0362 | +0.0075 (7) | +0.0562 | -0.0005 (7) |
| sty | -0.0372 | +0.0102 (7) | +0.0553 | +0.0023 (6) |
| sts | +0.2202 | -0.0262 (8) | +0.0159 | -0.0135 (11) |
| TDMI (sum) | +0.5762 | -0.0321 | +0.5762 | -0.0321 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.2625; its DiD -0.0544 (raw series -0.0146); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.495; r(MMI sts DiD, raw autocorrelation DiD) = +0.552; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.473; raw MMI sts DiD -0.0809.
Diagnostic on the whitened series (W = 60): observed sts level 0.2766, predicted 0.2426, residual +0.0341; DiD observed -0.0262, predicted -0.0192, residual -0.0070 (negative in 8/14).

## arp ts_gsr global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0074 | +0.0007 (8) | +0.0089 | -0.0017 (10) |
| rtx | +0.0079 | -0.0025 (11) | +0.0009 | -0.0004 (5) |
| rty | +0.0080 | -0.0015 (9) | +0.0010 | -0.0003 (8) |
| rts | +0.0350 | -0.0093 (8) | -0.0199 | -0.0002 (5) |
| xtr | +0.0071 | -0.0019 (11) | +0.0054 | -0.0006 (8) |
| xtx | +0.0412 | -0.0325 (11) | +0.0485 | -0.0336 (10) |
| xty | +0.0187 | +0.0079 (2) | +0.0261 | +0.0079 (1) |
| xts | -0.0105 | +0.0057 (6) | +0.0441 | -0.0044 (10) |
| ytr | +0.0078 | -0.0017 (10) | +0.0059 | -0.0009 (10) |
| ytx | +0.0187 | +0.0079 (3) | +0.0262 | +0.0072 (2) |
| yty | +0.0380 | -0.0268 (9) | +0.0455 | -0.0264 (9) |
| yts | -0.0109 | +0.0083 (6) | +0.0436 | -0.0023 (10) |
| str | +0.0370 | -0.0085 (8) | -0.0139 | +0.0019 (5) |
| stx | -0.0051 | +0.0067 (7) | +0.0403 | -0.0040 (10) |
| sty | -0.0058 | +0.0094 (7) | +0.0395 | -0.0023 (9) |
| sts | +0.1042 | -0.0264 (8) | -0.0030 | -0.0045 (7) |
| TDMI (sum) | +0.2989 | -0.0646 | +0.2989 | -0.0646 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.2831; its DiD -0.2044 (raw series -0.4580); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.362; r(MMI sts DiD, raw autocorrelation DiD) = +0.508; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.457; raw MMI sts DiD -0.0801.

Chosen AR orders (arp ts_gsr), count over 115 regions × 28 runs: p = 1: 0, p = 2: 0, p = 3: 0, p = 4: 2, p = 5: 3218.

## arp ts_demean W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0193 | +0.0033 (7) | +0.0314 | +0.0091 (6) |
| rtx | +0.0221 | +0.0051 (6) | +0.0058 | -0.0002 (8) |
| rty | +0.0221 | +0.0009 (7) | +0.0056 | -0.0037 (9) |
| rts | +0.0816 | -0.0084 (8) | -0.0143 | -0.0004 (5) |
| xtr | +0.0240 | +0.0030 (6) | +0.0090 | -0.0019 (7) |
| xtx | +0.0939 | -0.0188 (9) | +0.1131 | -0.0144 (8) |
| xty | +0.0109 | +0.0011 (7) | +0.0304 | +0.0049 (4) |
| xts | -0.0374 | +0.0081 (6) | +0.0557 | +0.0010 (9) |
| ytr | +0.0237 | +0.0046 (6) | +0.0081 | -0.0004 (9) |
| ytx | +0.0110 | -0.0022 (8) | +0.0309 | +0.0022 (4) |
| yty | +0.0940 | -0.0176 (7) | +0.1142 | -0.0138 (7) |
| yts | -0.0347 | +0.0067 (6) | +0.0577 | -0.0004 (6) |
| str | +0.0839 | -0.0075 (8) | -0.0106 | +0.0010 (5) |
| stx | -0.0324 | +0.0063 (7) | +0.0578 | -0.0016 (9) |
| sty | -0.0310 | +0.0098 (6) | +0.0591 | +0.0025 (6) |
| sts | +0.2350 | -0.0274 (9) | +0.0324 | -0.0168 (10) |
| TDMI (sum) | +0.5860 | -0.0329 | +0.5860 | -0.0329 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.2583; its DiD -0.0418 (raw series -0.0216); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.429; r(MMI sts DiD, raw autocorrelation DiD) = +0.426; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.353; raw MMI sts DiD -0.1031.
Diagnostic on the whitened series (W = 60): observed sts level 0.2822, predicted 0.2246, residual +0.0576; DiD observed -0.0274, predicted -0.0132, residual -0.0143 (negative in 9/14).

## arp ts_demean global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0072 | +0.0039 (5) | +0.0135 | -0.0016 (6) |
| rtx | +0.0072 | +0.0007 (9) | +0.0007 | +0.0025 (8) |
| rty | +0.0086 | -0.0013 (9) | +0.0009 | +0.0014 (7) |
| rts | +0.0410 | -0.0098 (8) | -0.0141 | -0.0009 (7) |
| xtr | +0.0083 | -0.0014 (9) | +0.0062 | +0.0003 (7) |
| xtx | +0.0504 | -0.0219 (9) | +0.0526 | -0.0199 (7) |
| xty | +0.0185 | +0.0027 (5) | +0.0220 | +0.0038 (4) |
| xts | -0.0168 | +0.0083 (7) | +0.0425 | -0.0044 (12) |
| ytr | +0.0069 | +0.0023 (7) | +0.0051 | +0.0025 (5) |
| ytx | +0.0195 | -0.0008 (5) | +0.0215 | +0.0027 (4) |
| yty | +0.0459 | -0.0168 (8) | +0.0492 | -0.0142 (7) |
| yts | -0.0146 | +0.0079 (6) | +0.0450 | -0.0063 (11) |
| str | +0.0418 | -0.0100 (8) | -0.0103 | -0.0008 (6) |
| stx | -0.0117 | +0.0077 (7) | +0.0403 | -0.0053 (11) |
| sty | -0.0118 | +0.0124 (6) | +0.0389 | +0.0003 (11) |
| sts | +0.1306 | -0.0264 (8) | +0.0171 | -0.0028 (7) |
| TDMI (sum) | +0.3308 | -0.0426 | +0.3308 | -0.0426 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.2703; its DiD -0.1448 (raw series -0.3846); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.075; r(MMI sts DiD, raw autocorrelation DiD) = +0.459; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.602; raw MMI sts DiD -0.1035.

Chosen AR orders (arp ts_demean), count over 115 regions × 28 runs: p = 1: 0, p = 2: 0, p = 3: 0, p = 4: 5, p = 5: 3215.

## ar1 ts_gsr W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0218 | -0.0019 (10) | +0.0634 | -0.0044 (9) |
| rtx | +0.0323 | +0.0016 (7) | +0.0016 | +0.0000 (7) |
| rty | +0.0317 | +0.0022 (6) | +0.0010 | +0.0007 (6) |
| rts | +0.3541 | -0.0286 (12) | -0.0115 | -0.0017 (12) |
| xtr | +0.0317 | +0.0022 (6) | +0.0011 | +0.0005 (6) |
| xtx | +0.3651 | -0.0451 (13) | +0.3848 | -0.0394 (13) |
| xty | -0.0314 | -0.0019 (8) | -0.0117 | +0.0037 (3) |
| xts | -0.3088 | +0.0340 (1) | +0.0678 | +0.0029 (5) |
| ytr | +0.0323 | +0.0016 (8) | +0.0013 | +0.0002 (7) |
| ytx | -0.0319 | -0.0014 (6) | -0.0118 | +0.0040 (3) |
| yty | +0.3580 | -0.0366 (13) | +0.3781 | -0.0313 (13) |
| yts | -0.3094 | +0.0348 (1) | +0.0669 | +0.0040 (2) |
| str | +0.3542 | -0.0288 (13) | -0.0113 | -0.0018 (12) |
| stx | -0.3087 | +0.0343 (2) | +0.0677 | +0.0034 (3) |
| sty | -0.3094 | +0.0346 (1) | +0.0670 | +0.0037 (4) |
| sts | +0.7176 | -0.0620 (13) | -0.0552 | -0.0057 (12) |
| TDMI (sum) | +0.9992 | -0.0610 | +0.9992 | -0.0610 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.7506; its DiD -0.0196 (raw series -0.0146); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.899; r(MMI sts DiD, raw autocorrelation DiD) = +0.912; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.918; raw MMI sts DiD -0.0809.
Diagnostic on the whitened series (W = 60): observed sts level 0.7062, predicted 0.7511, residual -0.0449; DiD observed -0.0620, predicted -0.0626, residual +0.0006 (negative in 5/14).

## ar1 ts_gsr global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0122 | -0.0021 (10) | +0.0406 | -0.0110 (13) |
| rtx | +0.0087 | -0.0024 (10) | +0.0012 | +0.0004 (6) |
| rty | +0.0081 | -0.0017 (9) | +0.0007 | +0.0003 (5) |
| rts | +0.3946 | -0.0278 (13) | -0.0083 | +0.0023 (5) |
| xtr | +0.0081 | -0.0017 (9) | +0.0006 | +0.0008 (5) |
| xtx | +0.4139 | -0.0378 (13) | +0.4005 | -0.0342 (13) |
| xty | -0.0081 | +0.0017 (5) | -0.0216 | +0.0061 (2) |
| xts | -0.3885 | +0.0258 (2) | +0.0352 | -0.0108 (13) |
| ytr | +0.0087 | -0.0024 (10) | +0.0014 | -0.0002 (8) |
| ytx | -0.0087 | +0.0024 (4) | -0.0222 | +0.0064 (2) |
| yty | +0.4051 | -0.0297 (13) | +0.3915 | -0.0250 (13) |
| yts | -0.3886 | +0.0260 (2) | +0.0352 | -0.0109 (13) |
| str | +0.3946 | -0.0278 (13) | -0.0083 | +0.0024 (5) |
| stx | -0.3885 | +0.0259 (2) | +0.0353 | -0.0105 (13) |
| sty | -0.3886 | +0.0259 (2) | +0.0353 | -0.0113 (13) |
| sts | +0.8043 | -0.0559 (13) | -0.0298 | +0.0134 (1) |
| TDMI (sum) | +0.8874 | -0.0817 | +0.8874 | -0.0817 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.9215; its DiD -0.3164 (raw series -0.4580); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.024; r(MMI sts DiD, raw autocorrelation DiD) = +0.381; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.877; raw MMI sts DiD -0.0801.

Chosen AR orders (ar1 ts_gsr), count over 115 regions × 28 runs: p = 1: 3220, p = 2: 0, p = 3: 0, p = 4: 0, p = 5: 0.

## ar1 ts_demean W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0289 | +0.0025 (7) | +0.0829 | +0.0097 (6) |
| rtx | +0.0395 | +0.0076 (2) | -0.0040 | -0.0032 (10) |
| rty | +0.0389 | +0.0043 (3) | -0.0049 | -0.0052 (10) |
| rts | +0.3240 | -0.0483 (13) | -0.0136 | -0.0037 (13) |
| xtr | +0.0389 | +0.0043 (4) | -0.0047 | -0.0055 (9) |
| xtx | +0.3317 | -0.0700 (13) | +0.3648 | -0.0566 (13) |
| xty | -0.0379 | -0.0032 (11) | -0.0045 | +0.0089 (2) |
| xts | -0.2750 | +0.0522 (1) | +0.0730 | +0.0050 (5) |
| ytr | +0.0395 | +0.0078 (2) | -0.0047 | -0.0022 (8) |
| ytx | -0.0385 | -0.0059 (11) | -0.0049 | +0.0078 (2) |
| yty | +0.3197 | -0.0558 (13) | +0.3537 | -0.0435 (13) |
| yts | -0.2759 | +0.0528 (1) | +0.0716 | +0.0054 (4) |
| str | +0.3240 | -0.0480 (13) | -0.0134 | -0.0036 (12) |
| stx | -0.2747 | +0.0510 (1) | +0.0733 | +0.0029 (5) |
| sty | -0.2763 | +0.0537 (1) | +0.0714 | +0.0069 (4) |
| sts | +0.6822 | -0.0784 (13) | -0.0469 | +0.0035 (5) |
| TDMI (sum) | +0.9891 | -0.0733 | +0.9891 | -0.0733 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.7426; its DiD -0.0276 (raw series -0.0216); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.908; r(MMI sts DiD, raw autocorrelation DiD) = +0.948; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.953; raw MMI sts DiD -0.1031.
Diagnostic on the whitened series (W = 60): observed sts level 0.6682, predicted 0.7097, residual -0.0415; DiD observed -0.0784, predicted -0.0867, residual +0.0084 (negative in 4/14).

## ar1 ts_demean global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0215 | +0.0079 (5) | +0.0769 | -0.0070 (9) |
| rtx | +0.0107 | +0.0056 (4) | -0.0095 | +0.0015 (10) |
| rty | +0.0117 | -0.0000 (6) | -0.0116 | -0.0012 (7) |
| rts | +0.3622 | -0.0550 (13) | -0.0068 | -0.0086 (10) |
| xtr | +0.0117 | -0.0000 (6) | -0.0116 | -0.0008 (8) |
| xtx | +0.3857 | -0.0713 (13) | +0.3738 | -0.0515 (13) |
| xty | -0.0117 | +0.0000 (8) | -0.0205 | +0.0168 (2) |
| xts | -0.3560 | +0.0543 (3) | +0.0451 | -0.0077 (11) |
| ytr | +0.0107 | +0.0056 (4) | -0.0100 | +0.0015 (9) |
| ytx | -0.0107 | -0.0056 (10) | -0.0253 | +0.0175 (1) |
| yty | +0.3703 | -0.0549 (11) | +0.3588 | -0.0348 (12) |
| yts | -0.3563 | +0.0545 (3) | +0.0475 | -0.0109 (13) |
| str | +0.3624 | -0.0551 (13) | -0.0067 | -0.0088 (10) |
| stx | -0.3564 | +0.0544 (3) | +0.0479 | -0.0109 (13) |
| sty | -0.3566 | +0.0547 (3) | +0.0446 | -0.0076 (11) |
| sts | +0.7648 | -0.0871 (13) | -0.0287 | +0.0204 (1) |
| TDMI (sum) | +0.8640 | -0.0920 | +0.8640 | -0.0920 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.8631; its DiD -0.2412 (raw series -0.3846); per subject r(MMI sts DiD, whitened autocorrelation DiD) = -0.304; r(MMI sts DiD, raw autocorrelation DiD) = +0.076; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.962; raw MMI sts DiD -0.1035.

Chosen AR orders (ar1 ts_demean), count over 115 regions × 28 runs: p = 1: 3220, p = 2: 0, p = 3: 0, p = 4: 0, p = 5: 0.

## Reading under the rule of the pre-run entry

A remedy check, reported as such: not a finding about DMT, and the primary result (the raw MMI-sts DiD at W = 60) is unchanged by it. The prediction recorded — MMI-sts near zero after whitening and the DMT contrast shrunk to the order of the cross-lag contrast — is read against the tables above in the outcome entry.
