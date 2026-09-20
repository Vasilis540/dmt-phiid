# CCS tables under the published double-redundancy definition (partB6_ccs_definition.py)
git=d507728

Mask 'pub' = Definition 1 of Mediano et al. (arXiv:2109.13186v1, Appendix): D kept where the four single-source, single-target local MIs and the local full MI i(x; y) share a sign. 'code' = phyid (D's own sign as the fifth). MMI from results/atoms_*.npy.

## ts_gsr W60: 16 atoms, DMT pre-injection level and primary DiD — published mask, phyid's mask, MMI (nats)

| atom | pub level | code level | MMI level | pub DiD (mean, neg/14) | code DiD (neg/14) | MMI DiD |
|---|---|---|---|---|---|---|
| rtr | +0.0822 | +0.0916 | +0.0388 | -0.0117 (10) | -0.0124 (10) | -0.0078 |
| rtx | +0.0102 | +0.0008 | +0.0258 | -0.0001 (7) | +0.0007 (5) | -0.0012 |
| rty | +0.0095 | +0.0001 | +0.0254 | +0.0003 (6) | +0.0011 (4) | -0.0012 |
| rts | -0.0132 | -0.0038 | +0.5669 | -0.0000 (6) | -0.0008 (10) | -0.0407 |
| xtr | +0.0099 | +0.0005 | +0.0254 | +0.0001 (7) | +0.0008 (4) | -0.0012 |
| xtx | +0.6151 | +0.6245 | +0.6273 | -0.0508 (12) | -0.0515 (12) | -0.0523 |
| xty | -0.0373 | -0.0279 | -0.0254 | +0.0023 (4) | +0.0016 (6) | +0.0012 |
| xts | +0.0727 | +0.0633 | -0.5352 | -0.0034 (9) | -0.0026 (9) | +0.0399 |
| ytr | +0.0098 | +0.0004 | +0.0258 | +0.0003 (7) | +0.0010 (4) | -0.0012 |
| ytx | -0.0375 | -0.0281 | -0.0258 | +0.0025 (4) | +0.0018 (7) | +0.0012 |
| yty | +0.6011 | +0.6105 | +0.6125 | -0.0386 (13) | -0.0394 (12) | -0.0396 |
| yts | +0.0716 | +0.0622 | -0.5358 | -0.0027 (10) | -0.0020 (10) | +0.0404 |
| str | -0.0133 | -0.0039 | +0.5667 | -0.0001 (5) | -0.0008 (10) | -0.0408 |
| stx | +0.0727 | +0.0634 | -0.5350 | -0.0034 (9) | -0.0027 (9) | +0.0401 |
| sty | +0.0717 | +0.0623 | -0.5357 | -0.0029 (9) | -0.0021 (9) | +0.0403 |
| sts | -0.0480 | -0.0387 | +1.1554 | +0.0044 (3) | +0.0036 (4) | -0.0809 |
| TDMI (sum) | +1.4772 | +1.4772 | +1.4772 | -0.1037 | -0.1037 | -0.1037 |

Published-mask CCS sts: level -0.0480 vs phyid -0.0387 (difference -0.0094); primary DiD +0.0044 vs phyid +0.0036 (difference +0.0008); per-subject r(pub, code) = +0.974
Per-subject pub CCS sts DiD vs the autocorrelation contrast (W60): Pearson r = -0.420 (p = 0.135), Spearman -0.262; vs the MMI sts DiD of the same estimator: r = -0.256; vs the B4 residual DiD (W60): r = +0.799 (p = 0.001); pub CCS (xtx+yty) DiD vs autocorrelation contrast: r = +0.949
pub CCS sts level / pub CCS (xtx + yty) level (DMT pre): -0.0480 / +1.2162; MMI: +1.1554 / +1.2398
share of samples selected by the published mask (mean over runs): 0.351
Group-mean window series, pub CCS sts vs mean r1 (28 condition-windows): r = -0.639; MMI sts vs r1: +0.977
Per-pair, subject 1 DMT window 6: pub CCS sts vs pair r1 r = -0.011, vs |q| -0.073, vs MMI sts +0.236; MMI sts vs r1 +0.742; pub CCS sts pair mean -0.0430 (SD 0.0663); agree share 0.325
Per-pair, subject 1 PCB window 2: pub CCS sts vs pair r1 r = -0.018, vs |q| +0.010, vs MMI sts +0.236; MMI sts vs r1 +0.697; pub CCS sts pair mean -0.0452 (SD 0.0700); agree share 0.335

## ts_gsr global-bins: 16 atoms, DMT pre-injection level and primary DiD — published mask, phyid's mask, MMI (nats)

| atom | pub level | code level | MMI level | pub DiD (mean, neg/14) | code DiD (neg/14) | MMI DiD |
|---|---|---|---|---|---|---|
| rtr | +0.0642 | +0.0665 | +0.0248 | -0.0237 (13) | -0.0223 (13) | -0.0060 |
| rtx | +0.0025 | +0.0001 | +0.0076 | +0.0026 (3) | +0.0013 (4) | -0.0031 |
| rty | +0.0022 | -0.0001 | +0.0074 | +0.0021 (2) | +0.0008 (3) | -0.0028 |
| rts | -0.0088 | -0.0065 | +0.6435 | +0.0013 (5) | +0.0027 (5) | -0.0396 |
| xtr | +0.0023 | +0.0000 | +0.0074 | +0.0028 (2) | +0.0014 (2) | -0.0028 |
| xtx | +0.6605 | +0.6629 | +0.6897 | -0.0481 (12) | -0.0468 (12) | -0.0544 |
| xty | -0.0365 | -0.0342 | -0.0074 | +0.0099 (1) | +0.0112 (1) | +0.0028 |
| xts | +0.0480 | +0.0456 | -0.6386 | -0.0162 (14) | -0.0176 (14) | +0.0367 |
| ytr | +0.0027 | +0.0003 | +0.0076 | +0.0018 (4) | +0.0004 (6) | -0.0031 |
| ytx | -0.0369 | -0.0346 | -0.0076 | +0.0101 (1) | +0.0115 (1) | +0.0031 |
| yty | +0.6427 | +0.6450 | +0.6719 | -0.0353 (12) | -0.0339 (12) | -0.0431 |
| yts | +0.0480 | +0.0456 | -0.6388 | -0.0168 (14) | -0.0182 (14) | +0.0368 |
| str | -0.0091 | -0.0068 | +0.6435 | +0.0016 (5) | +0.0029 (5) | -0.0397 |
| stx | +0.0482 | +0.0459 | -0.6387 | -0.0163 (14) | -0.0177 (14) | +0.0368 |
| sty | +0.0480 | +0.0457 | -0.6388 | -0.0170 (14) | -0.0184 (14) | +0.0368 |
| sts | -0.0358 | -0.0335 | +1.3085 | +0.0197 (1) | +0.0210 (0) | -0.0801 |
| TDMI (sum) | +1.4421 | +1.4421 | +1.4421 | -0.1216 | -0.1216 | -0.1216 |

Published-mask CCS sts: level -0.0358 vs phyid -0.0335 (difference -0.0023); primary DiD +0.0197 vs phyid +0.0210 (difference -0.0014); per-subject r(pub, code) = +0.992
Per-subject pub CCS sts DiD vs the autocorrelation contrast (W60): Pearson r = -0.275 (p = 0.342), Spearman -0.503; vs the MMI sts DiD of the same estimator: r = -0.288; vs the B4 residual DiD (W60): r = +0.094 (p = 0.749); pub CCS (xtx+yty) DiD vs autocorrelation contrast: r = +0.963
pub CCS sts level / pub CCS (xtx + yty) level (DMT pre): -0.0358 / +1.3032; MMI: +1.3085 / +1.3616
share of samples selected by the published mask (mean over runs): 0.365

## ts_demean W60: 16 atoms, DMT pre-injection level and primary DiD — published mask, phyid's mask, MMI (nats)

| atom | pub level | code level | MMI level | pub DiD (mean, neg/14) | code DiD (neg/14) | MMI DiD |
|---|---|---|---|---|---|---|
| rtr | +0.0925 | +0.1047 | +0.0444 | +0.0036 (8) | +0.0050 (8) | +0.0005 |
| rtx | +0.0080 | -0.0042 | +0.0293 | -0.0010 (9) | -0.0024 (9) | +0.0040 |
| rty | +0.0069 | -0.0053 | +0.0288 | -0.0029 (9) | -0.0043 (8) | +0.0003 |
| rts | -0.0186 | -0.0064 | +0.5265 | -0.0054 (11) | -0.0040 (11) | -0.0643 |
| xtr | +0.0076 | -0.0046 | +0.0287 | -0.0036 (9) | -0.0050 (10) | +0.0003 |
| xtx | +0.5813 | +0.5935 | +0.5871 | -0.0765 (13) | -0.0751 (13) | -0.0823 |
| xty | -0.0337 | -0.0215 | -0.0286 | +0.0037 (5) | +0.0051 (4) | -0.0002 |
| xts | +0.0787 | +0.0665 | -0.4933 | +0.0024 (7) | +0.0010 (7) | +0.0621 |
| ytr | +0.0073 | -0.0049 | +0.0292 | -0.0001 (8) | -0.0015 (7) | +0.0040 |
| ytx | -0.0341 | -0.0219 | -0.0291 | +0.0021 (5) | +0.0035 (4) | -0.0039 |
| yty | +0.5616 | +0.5738 | +0.5658 | -0.0568 (12) | -0.0554 (12) | -0.0610 |
| yts | +0.0770 | +0.0648 | -0.4942 | +0.0036 (6) | +0.0022 (6) | +0.0635 |
| str | -0.0186 | -0.0064 | +0.5264 | -0.0054 (12) | -0.0040 (12) | -0.0646 |
| stx | +0.0790 | +0.0668 | -0.4929 | +0.0015 (5) | +0.0002 (7) | +0.0627 |
| sty | +0.0769 | +0.0647 | -0.4943 | +0.0042 (7) | +0.0028 (7) | +0.0636 |
| sts | -0.0378 | -0.0255 | +1.1004 | +0.0120 (3) | +0.0134 (3) | -0.1031 |
| TDMI (sum) | +1.4341 | +1.4341 | +1.4341 | -0.1186 | -0.1186 | -0.1186 |

Published-mask CCS sts: level -0.0378 vs phyid -0.0255 (difference -0.0122); primary DiD +0.0120 vs phyid +0.0134 (difference -0.0014); per-subject r(pub, code) = +0.991
Per-subject pub CCS sts DiD vs the autocorrelation contrast (W60): Pearson r = -0.428 (p = 0.127), Spearman -0.433; vs the MMI sts DiD of the same estimator: r = -0.357; vs the B4 residual DiD (W60): r = +0.875 (p = 0.000); pub CCS (xtx+yty) DiD vs autocorrelation contrast: r = +0.917
pub CCS sts level / pub CCS (xtx + yty) level (DMT pre): -0.0378 / +1.1429; MMI: +1.1004 / +1.1529
share of samples selected by the published mask (mean over runs): 0.366
Group-mean window series, pub CCS sts vs mean r1 (28 condition-windows): r = -0.612; MMI sts vs r1: +0.938
Per-pair, subject 1 DMT window 6: pub CCS sts vs pair r1 r = -0.183, vs |q| -0.093, vs MMI sts +0.148; MMI sts vs r1 +0.518; pub CCS sts pair mean -0.0547 (SD 0.0669); agree share 0.381
Per-pair, subject 1 PCB window 2: pub CCS sts vs pair r1 r = -0.036, vs |q| +0.149, vs MMI sts +0.291; MMI sts vs r1 +0.628; pub CCS sts pair mean -0.0281 (SD 0.0799); agree share 0.346

## ts_demean global-bins: 16 atoms, DMT pre-injection level and primary DiD — published mask, phyid's mask, MMI (nats)

| atom | pub level | code level | MMI level | pub DiD (mean, neg/14) | code DiD (neg/14) | MMI DiD |
|---|---|---|---|---|---|---|
| rtr | +0.0849 | +0.0938 | +0.0301 | -0.0149 (9) | -0.0183 (11) | +0.0078 |
| rtx | +0.0000 | -0.0088 | +0.0074 | -0.0002 (6) | +0.0031 (2) | +0.0017 |
| rty | -0.0006 | -0.0095 | +0.0085 | -0.0024 (6) | +0.0010 (5) | -0.0022 |
| rts | -0.0140 | -0.0052 | +0.5979 | -0.0066 (9) | -0.0100 (9) | -0.0644 |
| xtr | -0.0005 | -0.0094 | +0.0085 | -0.0018 (6) | +0.0016 (5) | -0.0022 |
| xtx | +0.6137 | +0.6226 | +0.6522 | -0.0658 (12) | -0.0692 (12) | -0.0901 |
| xty | -0.0452 | -0.0363 | -0.0085 | +0.0247 (1) | +0.0213 (0) | +0.0022 |
| xts | +0.0644 | +0.0555 | -0.5933 | -0.0178 (13) | -0.0144 (12) | +0.0624 |
| ytr | +0.0000 | -0.0088 | +0.0074 | -0.0010 (8) | +0.0024 (4) | +0.0017 |
| ytx | -0.0475 | -0.0387 | -0.0074 | +0.0257 (1) | +0.0223 (0) | -0.0017 |
| yty | +0.5853 | +0.5941 | +0.6236 | -0.0407 (11) | -0.0441 (11) | -0.0664 |
| yts | +0.0659 | +0.0571 | -0.5934 | -0.0208 (13) | -0.0174 (13) | +0.0625 |
| str | -0.0142 | -0.0053 | +0.5979 | -0.0064 (9) | -0.0098 (9) | -0.0648 |
| stx | +0.0663 | +0.0574 | -0.5934 | -0.0205 (13) | -0.0172 (13) | +0.0626 |
| sty | +0.0641 | +0.0553 | -0.5937 | -0.0185 (13) | -0.0152 (12) | +0.0628 |
| sts | -0.0386 | -0.0297 | +1.2403 | +0.0355 (0) | +0.0321 (0) | -0.1035 |
| TDMI (sum) | +1.3841 | +1.3841 | +1.3841 | -0.1315 | -0.1315 | -0.1315 |

Published-mask CCS sts: level -0.0386 vs phyid -0.0297 (difference -0.0088); primary DiD +0.0355 vs phyid +0.0321 (difference +0.0034); per-subject r(pub, code) = +0.956
Per-subject pub CCS sts DiD vs the autocorrelation contrast (W60): Pearson r = -0.297 (p = 0.303), Spearman -0.424; vs the MMI sts DiD of the same estimator: r = -0.426; vs the B4 residual DiD (W60): r = +0.676 (p = 0.008); pub CCS (xtx+yty) DiD vs autocorrelation contrast: r = +0.921
pub CCS sts level / pub CCS (xtx + yty) level (DMT pre): -0.0386 / +1.1990; MMI: +1.2403 / +1.2758
share of samples selected by the published mask (mean over runs): 0.384

## Sensitivity masks (ts_gsr, W = 60, window means only)

- pub8: sts level -0.0468, primary DiD +0.0044 (negative in 4/14), selected share 0.340
- pubD: sts level -0.0425, primary DiD +0.0038 (negative in 4/14), selected share 0.290

## Verdict

ts_gsr W60: level pub -0.0480 vs code -0.0387 (|Δ| 0.0094); DiD pub +0.0044 vs code +0.0036 (|Δ| 0.0008); p pub 0.0559 vs code 0.0844 → DIFFERS
ts_gsr global-bins: level pub -0.0358 vs code -0.0335 (|Δ| 0.0023); DiD pub +0.0197 vs code +0.0210 (|Δ| 0.0014); p pub 0.0002 vs code 0.0001 → DIFFERS
ts_demean W60: level pub -0.0378 vs code -0.0255 (|Δ| 0.0122); DiD pub +0.0120 vs code +0.0134 (|Δ| 0.0014); p pub 0.0040 vs code 0.0052 → DIFFERS
ts_demean global-bins: level pub -0.0386 vs code -0.0297 (|Δ| 0.0088); DiD pub +0.0355 vs code +0.0321 (|Δ| 0.0034); p pub 0.0001 vs code 0.0001 → DIFFERS
VERDICT: the definitions differ on these data; every CCS number in the manuscript is replaced by the published-definition value (this file), phyid values reported alongside as the code variant

