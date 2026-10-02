# The atoms and the DMT contrast after prewhitening at fixed orders (partB16c_prewhiten_fixed.py)
git=13e7299

Whitening per region and run: 'ar10' = residuals of the region's AR(10) fit, 'ar20' = of its AR(20) fit (B16's ar_fit, the order fixed). The first p TRs of each run are dropped (non-finite). Atoms as partB2_ccs_run.py (MMI: PairPhiID.atoms_mean / atoms_bins; CCS: atoms_ccs, phyid's mask); inference as the primary (rev_inference.Engine, seed 20261120); the diagnostic as partB4 (per-pair AR(1) prediction from the whitened window's a_x, a_y, q). Level = DMT pre-injection (windows 1–4; bins 1–8); DiD = post minus pre, DMT minus placebo.

## ar10 ts_gsr W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0062 | -0.0003 (9) | +0.0077 | +0.0008 (5) |
| rtx | +0.0105 | +0.0000 (7) | +0.0052 | +0.0004 (6) |
| rty | +0.0098 | -0.0006 (7) | +0.0047 | -0.0010 (11) |
| rts | +0.0271 | -0.0043 (9) | -0.0064 | +0.0009 (6) |
| xtr | +0.0099 | +0.0002 (7) | +0.0052 | +0.0001 (6) |
| xtx | +0.0296 | -0.0134 (12) | +0.0381 | -0.0148 (13) |
| xty | +0.0171 | +0.0048 (5) | +0.0252 | +0.0040 (6) |
| xts | -0.0015 | +0.0001 (6) | +0.0289 | -0.0040 (11) |
| ytr | +0.0102 | -0.0008 (10) | +0.0056 | -0.0012 (11) |
| ytx | +0.0205 | +0.0055 (6) | +0.0290 | +0.0044 (7) |
| yty | +0.0259 | -0.0095 (11) | +0.0340 | -0.0098 (12) |
| yts | -0.0017 | +0.0036 (3) | +0.0288 | -0.0009 (11) |
| str | +0.0269 | -0.0042 (10) | -0.0058 | +0.0009 (6) |
| stx | +0.0031 | -0.0013 (8) | +0.0319 | -0.0048 (13) |
| sty | -0.0007 | +0.0032 (4) | +0.0285 | -0.0010 (10) |
| sts | +0.0866 | -0.0191 (13) | +0.0188 | -0.0100 (13) |
| TDMI (sum) | +0.2794 | -0.0361 | +0.2794 | -0.0361 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.1368; its DiD -0.0733 (raw series -0.0146); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.445; r(MMI sts DiD, raw autocorrelation DiD) = +0.594; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.631; raw MMI sts DiD -0.0809.
Diagnostic on the whitened series (W = 60): observed sts level 0.0861, predicted 0.0296, residual +0.0564; DiD observed -0.0191, predicted -0.0100, residual -0.0091 (negative in 11/14).

## ar10 ts_gsr global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0017 | +0.0001 (7) | +0.0018 | +0.0005 (6) |
| rtx | +0.0044 | -0.0007 (8) | +0.0013 | +0.0004 (5) |
| rty | +0.0046 | -0.0008 (11) | +0.0019 | -0.0004 (9) |
| rts | +0.0216 | -0.0045 (10) | -0.0082 | +0.0026 (1) |
| xtr | +0.0037 | -0.0004 (8) | +0.0018 | +0.0003 (7) |
| xtx | +0.0237 | -0.0104 (10) | +0.0285 | -0.0127 (11) |
| xty | +0.0135 | +0.0045 (6) | +0.0180 | +0.0030 (7) |
| xts | -0.0038 | -0.0023 (9) | +0.0244 | -0.0082 (14) |
| ytr | +0.0043 | -0.0008 (11) | +0.0024 | -0.0003 (9) |
| ytx | +0.0163 | +0.0060 (6) | +0.0212 | +0.0040 (7) |
| yty | +0.0193 | -0.0056 (9) | +0.0238 | -0.0070 (11) |
| yts | -0.0049 | +0.0024 (7) | +0.0232 | -0.0037 (12) |
| str | +0.0203 | -0.0040 (10) | -0.0072 | +0.0024 (2) |
| stx | -0.0002 | -0.0041 (10) | +0.0244 | -0.0090 (13) |
| sty | -0.0039 | +0.0019 (6) | +0.0210 | -0.0037 (12) |
| sts | +0.0730 | -0.0212 (12) | +0.0155 | -0.0082 (10) |
| TDMI (sum) | +0.1937 | -0.0399 | +0.1937 | -0.0399 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.1819; its DiD -0.1032 (raw series -0.4580); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.570; r(MMI sts DiD, raw autocorrelation DiD) = +0.785; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.378; raw MMI sts DiD -0.0801.

## ar10 ts_demean W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0056 | +0.0003 (6) | +0.0081 | +0.0018 (5) |
| rtx | +0.0084 | +0.0007 (5) | +0.0037 | +0.0003 (5) |
| rty | +0.0080 | -0.0008 (11) | +0.0031 | -0.0019 (11) |
| rts | +0.0249 | -0.0042 (12) | -0.0079 | +0.0022 (5) |
| xtr | +0.0085 | +0.0013 (6) | +0.0043 | +0.0005 (9) |
| xtx | +0.0120 | -0.0076 (11) | +0.0184 | -0.0079 (12) |
| xty | +0.0234 | -0.0016 (8) | +0.0300 | -0.0012 (9) |
| xts | -0.0005 | -0.0000 (7) | +0.0305 | -0.0057 (13) |
| ytr | +0.0082 | -0.0005 (8) | +0.0039 | -0.0015 (10) |
| ytx | +0.0212 | +0.0004 (7) | +0.0278 | +0.0002 (8) |
| yty | +0.0134 | -0.0049 (8) | +0.0201 | -0.0043 (8) |
| yts | -0.0007 | +0.0032 (6) | +0.0302 | -0.0027 (11) |
| str | +0.0246 | -0.0036 (12) | -0.0076 | +0.0033 (1) |
| stx | -0.0000 | -0.0002 (6) | +0.0299 | -0.0060 (13) |
| sty | +0.0029 | +0.0045 (4) | +0.0327 | -0.0020 (11) |
| sts | +0.1075 | -0.0256 (13) | +0.0400 | -0.0138 (11) |
| TDMI (sum) | +0.2674 | -0.0386 | +0.2674 | -0.0386 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.0739; its DiD -0.0626 (raw series -0.0216); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.168; r(MMI sts DiD, raw autocorrelation DiD) = +0.556; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.644; raw MMI sts DiD -0.1031.
Diagnostic on the whitened series (W = 60): observed sts level 0.1160, predicted 0.0183, residual +0.0977; DiD observed -0.0256, predicted -0.0044, residual -0.0212 (negative in 12/14).

## ar10 ts_demean global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0011 | -0.0002 (7) | +0.0008 | -0.0010 (10) |
| rtx | +0.0026 | -0.0001 (6) | +0.0020 | +0.0012 (4) |
| rty | +0.0028 | -0.0004 (9) | +0.0018 | +0.0004 (6) |
| rts | +0.0240 | -0.0059 (12) | -0.0092 | +0.0011 (4) |
| xtr | +0.0022 | +0.0001 (8) | +0.0023 | +0.0011 (8) |
| xtx | +0.0092 | -0.0060 (9) | +0.0100 | -0.0075 (11) |
| xty | +0.0219 | -0.0019 (8) | +0.0230 | -0.0029 (10) |
| xts | -0.0071 | -0.0007 (9) | +0.0259 | -0.0075 (13) |
| ytr | +0.0020 | +0.0002 (9) | +0.0024 | +0.0009 (5) |
| ytx | +0.0195 | +0.0003 (8) | +0.0201 | -0.0010 (7) |
| yty | +0.0110 | -0.0043 (8) | +0.0118 | -0.0050 (9) |
| yts | -0.0083 | +0.0038 (5) | +0.0251 | -0.0033 (9) |
| str | +0.0213 | -0.0045 (12) | -0.0088 | +0.0019 (3) |
| stx | -0.0060 | -0.0015 (8) | +0.0231 | -0.0074 (11) |
| sty | -0.0046 | +0.0038 (5) | +0.0243 | -0.0026 (9) |
| sts | +0.1014 | -0.0329 (13) | +0.0383 | -0.0188 (13) |
| TDMI (sum) | +0.1929 | -0.0503 | +0.1929 | -0.0503 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.1033; its DiD -0.0634 (raw series -0.3846); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.014; r(MMI sts DiD, raw autocorrelation DiD) = +0.403; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.721; raw MMI sts DiD -0.1035.

## ar20 ts_gsr W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0034 | -0.0002 (7) | +0.0035 | +0.0021 (4) |
| rtx | +0.0059 | -0.0001 (7) | +0.0031 | +0.0005 (6) |
| rty | +0.0051 | -0.0004 (8) | +0.0027 | -0.0008 (9) |
| rts | +0.0181 | -0.0013 (8) | -0.0042 | +0.0015 (3) |
| xtr | +0.0056 | -0.0003 (7) | +0.0030 | +0.0000 (7) |
| xtx | +0.0023 | -0.0034 (11) | +0.0076 | -0.0066 (13) |
| xty | +0.0259 | +0.0070 (2) | +0.0308 | +0.0048 (4) |
| xts | +0.0022 | -0.0038 (11) | +0.0220 | -0.0040 (12) |
| ytr | +0.0055 | -0.0004 (6) | +0.0030 | -0.0005 (9) |
| ytx | +0.0307 | +0.0080 (3) | +0.0358 | +0.0052 (4) |
| yty | +0.0017 | -0.0025 (11) | +0.0064 | -0.0043 (12) |
| yts | +0.0030 | -0.0005 (8) | +0.0230 | -0.0012 (9) |
| str | +0.0178 | -0.0012 (7) | -0.0042 | +0.0012 (1) |
| stx | +0.0048 | -0.0052 (11) | +0.0241 | -0.0047 (12) |
| sty | +0.0011 | -0.0014 (9) | +0.0209 | -0.0019 (10) |
| sts | +0.0719 | -0.0127 (13) | +0.0274 | -0.0098 (13) |
| TDMI (sum) | +0.2050 | -0.0184 | +0.2050 | -0.0184 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.0524; its DiD -0.0927 (raw series -0.0146); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.333; r(MMI sts DiD, raw autocorrelation DiD) = +0.650; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.677; raw MMI sts DiD -0.0809.
Diagnostic on the whitened series (W = 60): observed sts level 0.0705, predicted 0.0080, residual +0.0624; DiD observed -0.0127, predicted -0.0037, residual -0.0090 (negative in 12/14).

## ar20 ts_gsr global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0001 | +0.0001 (7) | -0.0018 | +0.0009 (6) |
| rtx | +0.0004 | -0.0002 (10) | +0.0009 | +0.0010 (2) |
| rty | +0.0003 | -0.0001 (6) | +0.0010 | +0.0006 (2) |
| rts | +0.0167 | -0.0034 (11) | -0.0049 | +0.0015 (0) |
| xtr | +0.0004 | -0.0002 (9) | +0.0010 | +0.0008 (3) |
| xtx | -0.0003 | +0.0002 (4) | +0.0005 | -0.0028 (12) |
| xty | +0.0243 | +0.0072 (5) | +0.0249 | +0.0048 (5) |
| xts | -0.0017 | -0.0044 (7) | +0.0186 | -0.0075 (11) |
| ytr | +0.0003 | -0.0000 (6) | +0.0009 | +0.0008 (5) |
| ytx | +0.0286 | +0.0083 (5) | +0.0295 | +0.0055 (5) |
| yty | -0.0002 | +0.0000 (8) | +0.0004 | -0.0022 (9) |
| yts | -0.0022 | +0.0001 (6) | +0.0181 | -0.0032 (8) |
| str | +0.0158 | -0.0027 (11) | -0.0049 | +0.0012 (3) |
| stx | +0.0006 | -0.0069 (11) | +0.0198 | -0.0088 (11) |
| sty | -0.0035 | -0.0015 (7) | +0.0160 | -0.0040 (11) |
| sts | +0.0687 | -0.0168 (14) | +0.0283 | -0.0088 (14) |
| TDMI (sum) | +0.1482 | -0.0202 | +0.1482 | -0.0202 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.0749; its DiD -0.0963 (raw series -0.4580); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.081; r(MMI sts DiD, raw autocorrelation DiD) = +0.441; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.565; raw MMI sts DiD -0.0801.

## ar20 ts_demean W60: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | +0.0032 | +0.0005 (6) | +0.0033 | +0.0025 (6) |
| rtx | +0.0049 | +0.0007 (5) | +0.0031 | +0.0003 (6) |
| rty | +0.0048 | -0.0002 (9) | +0.0030 | -0.0012 (11) |
| rts | +0.0172 | -0.0022 (12) | -0.0060 | +0.0016 (4) |
| xtr | +0.0054 | +0.0005 (7) | +0.0036 | -0.0001 (10) |
| xtx | +0.0020 | -0.0024 (10) | +0.0055 | -0.0035 (10) |
| xty | +0.0248 | +0.0006 (6) | +0.0282 | +0.0002 (9) |
| xts | +0.0064 | -0.0022 (11) | +0.0278 | -0.0046 (13) |
| ytr | +0.0046 | -0.0002 (7) | +0.0030 | -0.0012 (11) |
| ytx | +0.0202 | +0.0015 (5) | +0.0235 | +0.0009 (5) |
| yty | +0.0012 | -0.0013 (9) | +0.0045 | -0.0013 (9) |
| yts | +0.0026 | +0.0011 (7) | +0.0242 | -0.0017 (11) |
| str | +0.0170 | -0.0027 (12) | -0.0063 | +0.0022 (4) |
| stx | +0.0028 | -0.0010 (9) | +0.0244 | -0.0042 (12) |
| sty | +0.0054 | +0.0026 (7) | +0.0271 | -0.0012 (11) |
| sts | +0.0978 | -0.0200 (13) | +0.0512 | -0.0134 (11) |
| TDMI (sum) | +0.2202 | -0.0247 | +0.2202 | -0.0247 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.0323; its DiD -0.0691 (raw series -0.0216); per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.157; r(MMI sts DiD, raw autocorrelation DiD) = +0.585; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.667; raw MMI sts DiD -0.1031.
Diagnostic on the whitened series (W = 60): observed sts level 0.1074, predicted 0.0074, residual +0.1000; DiD observed -0.0200, predicted -0.0010, residual -0.0190 (negative in 13/14).

## ar20 ts_demean global-bins: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)

| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |
|---|---|---|---|---|
| rtr | -0.0000 | +0.0002 (4) | -0.0047 | -0.0003 (9) |
| rtx | +0.0002 | -0.0001 (9) | +0.0040 | +0.0013 (2) |
| rty | +0.0001 | +0.0000 (7) | +0.0038 | +0.0011 (4) |
| rts | +0.0166 | -0.0035 (11) | -0.0085 | +0.0003 (5) |
| xtr | +0.0002 | -0.0002 (9) | +0.0040 | +0.0008 (5) |
| xtx | -0.0002 | +0.0002 (5) | -0.0030 | -0.0017 (10) |
| xty | +0.0244 | +0.0002 (7) | +0.0216 | -0.0013 (8) |
| xts | +0.0004 | -0.0022 (9) | +0.0246 | -0.0055 (9) |
| ytr | +0.0001 | +0.0000 (7) | +0.0040 | +0.0010 (4) |
| ytx | +0.0193 | +0.0015 (5) | +0.0163 | -0.0003 (7) |
| yty | -0.0001 | -0.0000 (8) | -0.0030 | -0.0015 (11) |
| yts | -0.0033 | +0.0015 (7) | +0.0210 | -0.0018 (9) |
| str | +0.0157 | -0.0043 (11) | -0.0086 | +0.0007 (4) |
| stx | -0.0031 | -0.0008 (9) | +0.0203 | -0.0049 (10) |
| sty | -0.0015 | +0.0037 (6) | +0.0218 | -0.0007 (7) |
| sts | +0.0923 | -0.0219 (13) | +0.0476 | -0.0127 (13) |
| TDMI (sum) | +0.1613 | -0.0256 | +0.1613 | -0.0256 |

Whitened series: mean lag-1 autocorrelation, DMT pre-injection +0.0521; its DiD -0.0652 (raw series -0.3846); per subject r(MMI sts DiD, whitened autocorrelation DiD) = -0.079; r(MMI sts DiD, raw autocorrelation DiD) = +0.220; r(MMI sts DiD whitened, MMI sts DiD raw) = +0.474; raw MMI sts DiD -0.1035.

## Reading under the rule of the pre-run entry

A remedy check, reported as such: not a finding about DMT, and the primary result (the raw MMI-sts DiD at W = 60) is unchanged by it. The predictions recorded (the whitened r₁ equal to B16b's at p = 10 and 20; the MMI-sts level falling with the order and below 0.1 nats at p = 20; the W = 60 contrast falling in magnitude with the order, with neither p below 0.05; the per-subject correlation with the whitened r₁ DiD weaker at p = 20 than at p ≤ 5) are read against the tables above in the outcome entry, beside B16's p ≤ 5 and p = 1.
