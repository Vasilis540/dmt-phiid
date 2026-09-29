# B25: the binarised estimators on the symmetric AR(1) family (partB25_binarised.py)
git=b36178d
run 29 Sep 2026 09:20 UTC
binarised.csv sha256 7e8007801769e67ebc3c438947691e13b7baf381150f9623e3da34704097fe20

Pre-run entry: record, "The binarised estimators on the AR(1) family (B25): pre-run entry". python 3.12.3, numpy 2.5.3, scipy 1.18.1, phyid 0+untagged.8.g6c5f2e9. Checks: 150, failed 0. Values in nats (bits × ln 2). MMI: phyid's discrete path under MMI; CCS-pub / CCS-code: phyid's discrete path under CCS with the published / phyid's double-redundancy mask; CCS EC: str + stx + sty + sts under CCS (either mask); Ince EC: the synergy of x_t, y_t about the joint future in Ince's PID (Luppi et al., 2023); 2A: I(x_t; x_t+1) + I(y_t; y_t+1) of the binarised series; EC: emergence capacity, str + stx + sty + sts.

## (a) The long-series limit

### q = 0.1

| r₁ | MMI sts | MMI EC | 2A | CCS-pub sts | CCS-code sts | CCS EC | Ince EC | Gaussian-MMI sts | Gaussian-MMI EC (= S) |
|---|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.17145 | 0.08583 | 0.17287 | -0.00949 | -0.01047 | +0.00755 | +0.00751 | 0.44448 | 0.22314 |
| 0.65 | 0.20874 | 0.10449 | 0.21041 | -0.01125 | -0.01231 | +0.00900 | +0.00896 | 0.54693 | 0.27452 |
| 0.70 | 0.25274 | 0.12651 | 0.25468 | -0.01319 | -0.01431 | +0.01063 | +0.01058 | 0.67089 | 0.33667 |
| 0.75 | 0.30538 | 0.15284 | 0.30761 | -0.01534 | -0.01647 | +0.01246 | +0.01240 | 0.82386 | 0.41334 |
| 0.80 | 0.36968 | 0.18500 | 0.37224 | -0.01771 | -0.01881 | +0.01453 | +0.01448 | 1.01844 | 0.51083 |
| 0.85 | 0.45100 | 0.22567 | 0.45389 | -0.02033 | -0.02134 | +0.01692 | +0.01688 | 1.27831 | 0.64097 |
| 0.90 | 0.56027 | 0.28030 | 0.56352 | -0.02326 | -0.02410 | +0.01976 | +0.01972 | 1.65666 | 0.83037 |
| 0.95 | 0.72774 | 0.36401 | 0.73138 | -0.02660 | -0.02714 | +0.02336 | +0.02333 | 2.32337 | 1.16395 |

### q = 0.25

| r₁ | MMI sts | MMI EC | 2A | CCS-pub sts | CCS-code sts | CCS EC | Ince EC | Gaussian-MMI sts | Gaussian-MMI EC (= S) |
|---|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.16392 | 0.08264 | 0.17287 | -0.02050 | -0.02237 | +0.01771 | +0.01746 | 0.43491 | 0.22314 |
| 0.65 | 0.19987 | 0.10071 | 0.21041 | -0.02443 | -0.02659 | +0.02114 | +0.02086 | 0.53567 | 0.27452 |
| 0.70 | 0.24241 | 0.12207 | 0.25468 | -0.02884 | -0.03124 | +0.02499 | +0.02469 | 0.65779 | 0.33667 |
| 0.75 | 0.29347 | 0.14768 | 0.30761 | -0.03378 | -0.03633 | +0.02934 | +0.02902 | 0.80878 | 0.41334 |
| 0.80 | 0.35607 | 0.17905 | 0.37224 | -0.03932 | -0.04192 | +0.03429 | +0.03398 | 1.00124 | 0.51083 |
| 0.85 | 0.43554 | 0.21883 | 0.45389 | -0.04560 | -0.04807 | +0.04001 | +0.03972 | 1.25883 | 0.64097 |
| 0.90 | 0.54282 | 0.27246 | 0.56352 | -0.05279 | -0.05492 | +0.04682 | +0.04657 | 1.63476 | 0.83037 |
| 0.95 | 0.70815 | 0.35498 | 0.73138 | -0.06130 | -0.06272 | +0.05549 | +0.05532 | 2.29887 | 1.16395 |

### q = 0.5

| r₁ | MMI sts | MMI EC | 2A | CCS-pub sts | CCS-code sts | CCS EC | Ince EC | Gaussian-MMI sts | Gaussian-MMI EC (= S) |
|---|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.13593 | 0.07063 | 0.17287 | -0.02908 | -0.02908 | +0.03035 | +0.02945 | 0.39913 | 0.22314 |
| 0.65 | 0.16670 | 0.08642 | 0.21041 | -0.03521 | -0.03567 | +0.03639 | +0.03539 | 0.49323 | 0.27452 |
| 0.70 | 0.20353 | 0.10524 | 0.25468 | -0.04230 | -0.04368 | +0.04326 | +0.04217 | 0.60801 | 0.33667 |
| 0.75 | 0.24830 | 0.12800 | 0.30761 | -0.05053 | -0.05281 | +0.05110 | +0.04996 | 0.75090 | 0.41334 |
| 0.80 | 0.30400 | 0.15618 | 0.37224 | -0.06019 | -0.06323 | +0.06015 | +0.05900 | 0.93447 | 0.51083 |
| 0.85 | 0.37590 | 0.19236 | 0.45389 | -0.07166 | -0.07522 | +0.07074 | +0.06964 | 1.18233 | 0.64097 |
| 0.90 | 0.47488 | 0.24186 | 0.56352 | -0.08562 | -0.08924 | +0.08353 | +0.08258 | 1.54759 | 0.83037 |
| 0.95 | 0.63106 | 0.31946 | 0.73138 | -0.10350 | -0.10632 | +0.10008 | +0.09943 | 2.20005 | 1.16395 |

### Rates at the operating point (0.85, 0.25), nats per unit (central differences, step 10⁻⁴; step 10⁻³ in brackets)

A rate marked * differs between the two steps by more than 1 % (+ 10⁻⁶): the quantity is not differentiable there on the 10⁻³ scale (a CCS sign mask changes within the step).

| quantity | ∂/∂r₁ | ∂/∂q |
|---|---|---|
| MMI sts | +1.8153 (+1.8153) | -0.1496 (-0.1496) |
| MMI EC | +0.9080 (+0.9080) | -0.0662 (-0.0662) |
| CCS-pub sts | -0.1339 (-0.1339) | -0.1465 (-0.1465) |
| CCS-code sts | -0.1295 (-0.1295) | -0.1554 (-0.1554) |
| CCS EC | +0.1239 (+0.1239) | +0.1439 (+0.1439) |
| Ince EC | +0.1244 (+0.1244) | +0.1415 (+0.1415) |
| 2A | +1.8605 (+1.8606) | +0.0000 (+0.0000) |
| TDMI | +1.8389 (+1.8389) | -0.0588 (-0.0588) |
| MMI rtr | +0.0223 (+0.0223) | +0.0760 (+0.0760) |

MMI sts: ∂/∂r₁ +1.8153, ∂/∂q -0.1496; per unit ratio 12.13; per SD of the pairs' variation within a window (r₁ 0.0284, |q| 0.1957) 1.76.

Patterns at which a quantity a CCS mask tests is below 10⁻¹² in absolute value: 0 over the 24 grid points ().

Maximum-entropy fits (Ince EC): 72,043, of which 17 from the support; largest marginal error 1.0e-15.

### The limit against phyid at the operating point (10 series of 10⁵ samples)

| quantity | limit | phyid, mean ± SE | difference | within 4 SE + 2e-4 |
|---|---|---|---|---|
| MMI sts | +0.43554 | +0.43492 ± 0.00136 | -0.00062 | yes |
| MMI EC | +0.21883 | +0.21856 ± 0.00065 | -0.00027 | yes |
| CCS-pub sts | -0.04560 | -0.04473 ± 0.00076 | +0.00087 | yes (reported, not checked) |
| CCS-code sts | -0.04807 | -0.04722 ± 0.00072 | +0.00085 | yes (reported, not checked) |
| CCS EC | +0.04001 | +0.03935 ± 0.00078 | -0.00066 | yes (reported, not checked) |
| Ince EC | +0.03972 | +0.03902 ± 0.00071 | -0.00070 | yes (reported, not checked) |
| 2A | +0.45389 | +0.45462 ± 0.00127 | +0.00073 | yes |
| TDMI | +0.44669 | +0.44771 ± 0.00125 | +0.00103 | yes |
| MMI rtr | +0.00932 | +0.00880 ± 0.00037 | -0.00052 | yes |

## (b) Finite length: replicate means ± SE (1,000 replicates) and the difference from the limit

### T = 160, q = 0.1

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.13489 ± 0.00162 | -0.03655 | 0.08249 ± 0.00087 | -0.00334 | -0.01538 ± 0.00108 | +0.01587 ± 0.00066 | +0.02053 ± 0.00045 | +0.01302 |
| 0.65 | 0.16551 ± 0.00181 | -0.04323 | 0.09786 ± 0.00095 | -0.00663 | -0.01719 ± 0.00107 | +0.01849 ± 0.00067 | +0.02281 ± 0.00050 | +0.01386 |
| 0.70 | 0.20265 ± 0.00201 | -0.05009 | 0.11660 ± 0.00104 | -0.00991 | -0.02026 ± 0.00107 | +0.02101 ± 0.00070 | +0.02576 ± 0.00053 | +0.01518 |
| 0.75 | 0.24741 ± 0.00233 | -0.05797 | 0.13920 ± 0.00119 | -0.01364 | -0.02337 ± 0.00110 | +0.02448 ± 0.00075 | +0.02938 ± 0.00060 | +0.01697 |
| 0.80 | 0.29872 ± 0.00256 | -0.07097 | 0.16609 ± 0.00131 | -0.01892 | -0.02627 ± 0.00112 | +0.03011 ± 0.00080 | +0.03455 ± 0.00071 | +0.02007 |
| 0.85 | 0.36166 ± 0.00287 | -0.08934 | 0.19815 ± 0.00145 | -0.02751 | -0.03072 ± 0.00113 | +0.03799 ± 0.00088 | +0.04103 ± 0.00081 | +0.02415 |
| 0.90 | 0.43938 ± 0.00339 | -0.12089 | 0.23771 ± 0.00167 | -0.04259 | -0.04214 ± 0.00119 | +0.04743 ± 0.00102 | +0.05141 ± 0.00096 | +0.03169 |
| 0.95 | 0.53634 ± 0.00432 | -0.19140 | 0.28827 ± 0.00208 | -0.07574 | -0.05787 ± 0.00140 | +0.06590 ± 0.00125 | +0.06872 ± 0.00124 | +0.04539 |

### T = 160, q = 0.25

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.12663 ± 0.00156 | -0.03728 | 0.07942 ± 0.00082 | -0.00322 | -0.01788 ± 0.00099 | +0.02322 ± 0.00069 | +0.02749 ± 0.00051 | +0.01003 |
| 0.65 | 0.15714 ± 0.00176 | -0.04272 | 0.09496 ± 0.00091 | -0.00575 | -0.02085 ± 0.00101 | +0.02655 ± 0.00072 | +0.03089 ± 0.00058 | +0.01003 |
| 0.70 | 0.19297 ± 0.00200 | -0.04944 | 0.11329 ± 0.00102 | -0.00878 | -0.02519 ± 0.00105 | +0.03001 ± 0.00077 | +0.03489 ± 0.00064 | +0.01020 |
| 0.75 | 0.23636 ± 0.00233 | -0.05711 | 0.13514 ± 0.00117 | -0.01254 | -0.02907 ± 0.00106 | +0.03406 ± 0.00080 | +0.03874 ± 0.00071 | +0.00971 |
| 0.80 | 0.28757 ± 0.00262 | -0.06850 | 0.16162 ± 0.00131 | -0.01743 | -0.03401 ± 0.00109 | +0.04018 ± 0.00088 | +0.04440 ± 0.00080 | +0.01043 |
| 0.85 | 0.34537 ± 0.00293 | -0.09017 | 0.19130 ± 0.00147 | -0.02753 | -0.03934 ± 0.00115 | +0.04768 ± 0.00100 | +0.05094 ± 0.00094 | +0.01122 |
| 0.90 | 0.42245 ± 0.00350 | -0.12038 | 0.23054 ± 0.00171 | -0.04192 | -0.04861 ± 0.00130 | +0.05615 ± 0.00112 | +0.05958 ± 0.00111 | +0.01301 |
| 0.95 | 0.52299 ± 0.00441 | -0.18516 | 0.28253 ± 0.00208 | -0.07246 | -0.06337 ± 0.00143 | +0.07237 ± 0.00132 | +0.07509 ± 0.00131 | +0.01977 |

### T = 160, q = 0.5

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.09957 ± 0.00145 | -0.03636 | 0.06922 ± 0.00074 | -0.00142 | -0.02165 ± 0.00076 | +0.03872 ± 0.00068 | +0.04066 ± 0.00051 | +0.01122 |
| 0.65 | 0.12439 ± 0.00171 | -0.04231 | 0.08251 ± 0.00085 | -0.00391 | -0.02718 ± 0.00077 | +0.04392 ± 0.00070 | +0.04593 ± 0.00057 | +0.01054 |
| 0.70 | 0.15559 ± 0.00191 | -0.04795 | 0.09859 ± 0.00095 | -0.00665 | -0.03415 ± 0.00083 | +0.04981 ± 0.00075 | +0.05196 ± 0.00063 | +0.00979 |
| 0.75 | 0.19251 ± 0.00229 | -0.05579 | 0.11736 ± 0.00110 | -0.01064 | -0.04105 ± 0.00083 | +0.05609 ± 0.00075 | +0.05809 ± 0.00066 | +0.00813 |
| 0.80 | 0.23529 ± 0.00254 | -0.06870 | 0.13996 ± 0.00123 | -0.01622 | -0.04780 ± 0.00090 | +0.06457 ± 0.00082 | +0.06600 ± 0.00075 | +0.00700 |
| 0.85 | 0.29060 ± 0.00293 | -0.08530 | 0.16838 ± 0.00140 | -0.02398 | -0.05729 ± 0.00095 | +0.07343 ± 0.00090 | +0.07476 ± 0.00087 | +0.00512 |
| 0.90 | 0.36005 ± 0.00363 | -0.11483 | 0.20357 ± 0.00170 | -0.03829 | -0.06735 ± 0.00111 | +0.08216 ± 0.00102 | +0.08418 ± 0.00102 | +0.00160 |
| 0.95 | 0.45306 ± 0.00468 | -0.17800 | 0.25063 ± 0.00219 | -0.06883 | -0.07798 ± 0.00125 | +0.09288 ± 0.00124 | +0.09442 ± 0.00124 | -0.00502 |

### T = 300, q = 0.1

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.14345 ± 0.00123 | -0.02800 | 0.07959 ± 0.00063 | -0.00624 | -0.01354 ± 0.00078 | +0.01017 ± 0.00048 | +0.01401 ± 0.00031 | +0.00649 |
| 0.65 | 0.17642 ± 0.00139 | -0.03231 | 0.09622 ± 0.00071 | -0.00827 | -0.01622 ± 0.00078 | +0.01187 ± 0.00050 | +0.01595 ± 0.00035 | +0.00699 |
| 0.70 | 0.21506 ± 0.00159 | -0.03768 | 0.11588 ± 0.00081 | -0.01063 | -0.01887 ± 0.00078 | +0.01383 ± 0.00051 | +0.01830 ± 0.00040 | +0.00773 |
| 0.75 | 0.26127 ± 0.00180 | -0.04411 | 0.13918 ± 0.00091 | -0.01366 | -0.02036 ± 0.00080 | +0.01744 ± 0.00057 | +0.02172 ± 0.00048 | +0.00932 |
| 0.80 | 0.31677 ± 0.00201 | -0.05292 | 0.16735 ± 0.00101 | -0.01766 | -0.02434 ± 0.00085 | +0.02159 ± 0.00063 | +0.02567 ± 0.00055 | +0.01119 |
| 0.85 | 0.38428 ± 0.00221 | -0.06672 | 0.20129 ± 0.00111 | -0.02438 | -0.02712 ± 0.00091 | +0.02776 ± 0.00073 | +0.03122 ± 0.00067 | +0.01434 |
| 0.90 | 0.47508 ± 0.00267 | -0.08519 | 0.24760 ± 0.00131 | -0.03269 | -0.03545 ± 0.00102 | +0.03622 ± 0.00088 | +0.03933 ± 0.00085 | +0.01961 |
| 0.95 | 0.60131 ± 0.00326 | -0.12643 | 0.31136 ± 0.00160 | -0.05265 | -0.04778 ± 0.00124 | +0.05216 ± 0.00111 | +0.05431 ± 0.00109 | +0.03098 |

### T = 300, q = 0.25

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.13542 ± 0.00122 | -0.02850 | 0.07650 ± 0.00062 | -0.00614 | -0.01901 ± 0.00069 | +0.01878 ± 0.00052 | +0.02208 ± 0.00036 | +0.00462 |
| 0.65 | 0.16800 ± 0.00140 | -0.03186 | 0.09329 ± 0.00071 | -0.00742 | -0.02271 ± 0.00072 | +0.02205 ± 0.00055 | +0.02549 ± 0.00042 | +0.00464 |
| 0.70 | 0.20551 ± 0.00156 | -0.03690 | 0.11231 ± 0.00079 | -0.00977 | -0.02621 ± 0.00074 | +0.02552 ± 0.00059 | +0.02927 ± 0.00048 | +0.00458 |
| 0.75 | 0.24797 ± 0.00178 | -0.04550 | 0.13389 ± 0.00089 | -0.01380 | -0.02985 ± 0.00078 | +0.03029 ± 0.00065 | +0.03377 ± 0.00056 | +0.00474 |
| 0.80 | 0.30283 ± 0.00204 | -0.05324 | 0.16182 ± 0.00100 | -0.01723 | -0.03458 ± 0.00086 | +0.03574 ± 0.00072 | +0.03912 ± 0.00064 | +0.00515 |
| 0.85 | 0.36999 ± 0.00228 | -0.06555 | 0.19574 ± 0.00112 | -0.02309 | -0.03983 ± 0.00093 | +0.04296 ± 0.00081 | +0.04579 ± 0.00075 | +0.00608 |
| 0.90 | 0.45747 ± 0.00268 | -0.08536 | 0.24023 ± 0.00130 | -0.03222 | -0.04827 ± 0.00110 | +0.05109 ± 0.00097 | +0.05380 ± 0.00095 | +0.00723 |
| 0.95 | 0.58146 ± 0.00343 | -0.12669 | 0.30252 ± 0.00165 | -0.05246 | -0.05940 ± 0.00130 | +0.06394 ± 0.00122 | +0.06601 ± 0.00121 | +0.01069 |

### T = 300, q = 0.5

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.10737 ± 0.00116 | -0.02856 | 0.06570 ± 0.00057 | -0.00493 | -0.02599 ± 0.00054 | +0.03385 ± 0.00050 | +0.03420 ± 0.00035 | +0.00476 |
| 0.65 | 0.13435 ± 0.00132 | -0.03235 | 0.07987 ± 0.00065 | -0.00655 | -0.03153 ± 0.00055 | +0.03952 ± 0.00052 | +0.03988 ± 0.00038 | +0.00450 |
| 0.70 | 0.16605 ± 0.00150 | -0.03749 | 0.09628 ± 0.00073 | -0.00896 | -0.03811 ± 0.00056 | +0.04611 ± 0.00054 | +0.04621 ± 0.00042 | +0.00403 |
| 0.75 | 0.20507 ± 0.00175 | -0.04323 | 0.11657 ± 0.00084 | -0.01143 | -0.04560 ± 0.00059 | +0.05380 ± 0.00058 | +0.05401 ± 0.00047 | +0.00405 |
| 0.80 | 0.25050 ± 0.00197 | -0.05349 | 0.13987 ± 0.00094 | -0.01632 | -0.05441 ± 0.00061 | +0.06230 ± 0.00064 | +0.06267 ± 0.00054 | +0.00367 |
| 0.85 | 0.30961 ± 0.00227 | -0.06630 | 0.17002 ± 0.00108 | -0.02234 | -0.06295 ± 0.00070 | +0.07240 ± 0.00068 | +0.07239 ± 0.00063 | +0.00275 |
| 0.90 | 0.38955 ± 0.00280 | -0.08533 | 0.21064 ± 0.00131 | -0.03122 | -0.07559 ± 0.00083 | +0.08294 ± 0.00084 | +0.08401 ± 0.00081 | +0.00143 |
| 0.95 | 0.50613 ± 0.00382 | -0.12493 | 0.26898 ± 0.00179 | -0.05048 | -0.08729 ± 0.00108 | +0.09512 ± 0.00109 | +0.09629 ± 0.00108 | -0.00314 |

### T = 840, q = 0.1

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.15454 ± 0.00074 | -0.01691 | 0.08021 ± 0.00037 | -0.00562 | -0.01008 ± 0.00045 | +0.00737 ± 0.00029 | +0.00944 ± 0.00020 | +0.00193 |
| 0.65 | 0.18933 ± 0.00084 | -0.01940 | 0.09773 ± 0.00042 | -0.00676 | -0.01145 ± 0.00045 | +0.00907 ± 0.00031 | +0.01111 ± 0.00023 | +0.00215 |
| 0.70 | 0.23090 ± 0.00093 | -0.02184 | 0.11855 ± 0.00047 | -0.00796 | -0.01347 ± 0.00048 | +0.01089 ± 0.00034 | +0.01293 ± 0.00027 | +0.00235 |
| 0.75 | 0.28055 ± 0.00102 | -0.02483 | 0.14346 ± 0.00051 | -0.00938 | -0.01590 ± 0.00050 | +0.01285 ± 0.00038 | +0.01504 ± 0.00033 | +0.00264 |
| 0.80 | 0.33940 ± 0.00114 | -0.03028 | 0.17285 ± 0.00057 | -0.01216 | -0.01733 ± 0.00053 | +0.01583 ± 0.00042 | +0.01746 ± 0.00038 | +0.00298 |
| 0.85 | 0.41512 ± 0.00134 | -0.03588 | 0.21092 ± 0.00067 | -0.01475 | -0.02081 ± 0.00060 | +0.01941 ± 0.00049 | +0.02102 ± 0.00046 | +0.00414 |
| 0.90 | 0.51596 ± 0.00159 | -0.04431 | 0.26153 ± 0.00079 | -0.01877 | -0.02558 ± 0.00070 | +0.02469 ± 0.00062 | +0.02622 ± 0.00060 | +0.00650 |
| 0.95 | 0.66504 ± 0.00200 | -0.06269 | 0.33660 ± 0.00099 | -0.02741 | -0.03655 ± 0.00093 | +0.03746 ± 0.00081 | +0.03856 ± 0.00081 | +0.01523 |

### T = 840, q = 0.25

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.14678 ± 0.00074 | -0.01714 | 0.07731 ± 0.00037 | -0.00533 | -0.01878 ± 0.00039 | +0.01810 ± 0.00032 | +0.01897 ± 0.00021 | +0.00151 |
| 0.65 | 0.18030 ± 0.00084 | -0.01956 | 0.09428 ± 0.00042 | -0.00643 | -0.02246 ± 0.00040 | +0.02157 ± 0.00034 | +0.02243 ± 0.00025 | +0.00158 |
| 0.70 | 0.22000 ± 0.00092 | -0.02241 | 0.11427 ± 0.00046 | -0.00780 | -0.02666 ± 0.00045 | +0.02528 ± 0.00036 | +0.02620 ± 0.00029 | +0.00152 |
| 0.75 | 0.26819 ± 0.00104 | -0.02528 | 0.13853 ± 0.00052 | -0.00916 | -0.03133 ± 0.00049 | +0.02945 ± 0.00040 | +0.03052 ± 0.00034 | +0.00149 |
| 0.80 | 0.32546 ± 0.00119 | -0.03061 | 0.16719 ± 0.00059 | -0.01186 | -0.03598 ± 0.00054 | +0.03454 ± 0.00045 | +0.03524 ± 0.00041 | +0.00126 |
| 0.85 | 0.39930 ± 0.00136 | -0.03624 | 0.20428 ± 0.00067 | -0.01455 | -0.04136 ± 0.00064 | +0.04025 ± 0.00054 | +0.04094 ± 0.00051 | +0.00122 |
| 0.90 | 0.49782 ± 0.00162 | -0.04500 | 0.25371 ± 0.00079 | -0.01874 | -0.04770 ± 0.00078 | +0.04673 ± 0.00069 | +0.04768 ± 0.00067 | +0.00111 |
| 0.95 | 0.64573 ± 0.00205 | -0.06242 | 0.32795 ± 0.00100 | -0.02704 | -0.05634 ± 0.00108 | +0.05691 ± 0.00097 | +0.05766 ± 0.00098 | +0.00234 |

### T = 840, q = 0.5

| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0.11820 ± 0.00071 | -0.01773 | 0.06588 ± 0.00034 | -0.00476 | -0.02799 ± 0.00030 | +0.03197 ± 0.00030 | +0.03116 ± 0.00020 | +0.00171 |
| 0.65 | 0.14661 ± 0.00080 | -0.02009 | 0.08051 ± 0.00039 | -0.00591 | -0.03376 ± 0.00030 | +0.03789 ± 0.00031 | +0.03684 ± 0.00022 | +0.00146 |
| 0.70 | 0.18099 ± 0.00090 | -0.02254 | 0.09822 ± 0.00044 | -0.00702 | -0.04098 ± 0.00032 | +0.04438 ± 0.00032 | +0.04359 ± 0.00025 | +0.00141 |
| 0.75 | 0.22261 ± 0.00101 | -0.02569 | 0.11948 ± 0.00049 | -0.00852 | -0.04876 ± 0.00033 | +0.05206 ± 0.00034 | +0.05116 ± 0.00028 | +0.00120 |
| 0.80 | 0.27393 ± 0.00118 | -0.03006 | 0.14549 ± 0.00057 | -0.01070 | -0.05803 ± 0.00036 | +0.06097 ± 0.00037 | +0.06001 ± 0.00033 | +0.00102 |
| 0.85 | 0.34029 ± 0.00135 | -0.03561 | 0.17894 ± 0.00065 | -0.01342 | -0.06889 ± 0.00040 | +0.07144 ± 0.00042 | +0.07052 ± 0.00039 | +0.00088 |
| 0.90 | 0.43034 ± 0.00170 | -0.04454 | 0.22415 ± 0.00080 | -0.01771 | -0.08178 ± 0.00047 | +0.08360 ± 0.00051 | +0.08298 ± 0.00049 | +0.00040 |
| 0.95 | 0.56991 ± 0.00232 | -0.06115 | 0.29364 ± 0.00109 | -0.02582 | -0.09688 ± 0.00074 | +0.09861 ± 0.00074 | +0.09845 ± 0.00074 | -0.00098 |

## The facts the pre-run entry's predictions read

- (a) steps of MMI sts and MMI EC along r₁ (7 per curve, 3 values of q) that rise in the limit: 42 of 42.
- (b) at (0.85, 0.25): ∂(MMI sts)/∂r₁ = +1.8153, ∂(MMI sts)/∂q = -0.1496; per-unit ratio 12.13; per-SD ratio 1.76.
- (c) steps of the replicate means of MMI sts and MMI EC along r₁ (7 per curve, 3 values of q, 3 lengths) that rise: 126 of 126.

## Checks

| check | largest difference | tolerance | passed |
|---|---|---|---|
| the copy of notes/partB6_ccs_definition.py l. 51–76 is verbatim | 0 | 0 | yes |
| pattern probabilities positive at (0.6, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.6, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.6, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.6, 0.1) | 1.67e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.6, 0.1) | 2.78e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.65, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.65, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.65, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.65, 0.1) | 5.55e-17 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.65, 0.1) | 0 | 1e-12 | yes |
| pattern probabilities positive at (0.7, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.7, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.7, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.7, 0.1) | 2.78e-17 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.7, 0.1) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.75, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.75, 0.1) | 2.22e-16 | 1e-13 | yes |
| pattern marginals at (0.75, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.75, 0.1) | 3.89e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.75, 0.1) | 2.78e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.8, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.8, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.8, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.8, 0.1) | 1.11e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.8, 0.1) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.85, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.85, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.85, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.85, 0.1) | 0 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.85, 0.1) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.9, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.9, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.9, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.9, 0.1) | 1.11e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.9, 0.1) | 1.11e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.95, 0.1) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.95, 0.1) | 0 | 1e-13 | yes |
| pattern marginals at (0.95, 0.1) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.95, 0.1) | 2.22e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.95, 0.1) | 2.22e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.6, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.6, 0.25) | 0 | 1e-13 | yes |
| pattern marginals at (0.6, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.6, 0.25) | 1.39e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.6, 0.25) | 2.78e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.65, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.65, 0.25) | 0 | 1e-13 | yes |
| pattern marginals at (0.65, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.65, 0.25) | 5.55e-17 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.65, 0.25) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.7, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.7, 0.25) | 0 | 1e-13 | yes |
| pattern marginals at (0.7, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.7, 0.25) | 2.78e-17 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.7, 0.25) | 1.67e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.75, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.75, 0.25) | 0 | 1e-13 | yes |
| pattern marginals at (0.75, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.75, 0.25) | 1.11e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.75, 0.25) | 2.22e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.8, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.8, 0.25) | 0 | 1e-13 | yes |
| pattern marginals at (0.8, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.8, 0.25) | 1.11e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.8, 0.25) | 1.67e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.85, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.85, 0.25) | 0 | 1e-13 | yes |
| pattern marginals at (0.85, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.85, 0.25) | 1.67e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.85, 0.25) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.9, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.9, 0.25) | 2.22e-16 | 1e-13 | yes |
| pattern marginals at (0.9, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.9, 0.25) | 1.67e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.9, 0.25) | 0 | 1e-12 | yes |
| pattern probabilities positive at (0.95, 0.25) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.95, 0.25) | 4.44e-16 | 1e-13 | yes |
| pattern marginals at (0.95, 0.25) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.95, 0.25) | 5.55e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.95, 0.25) | 2.22e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.6, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.6, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.6, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.6, 0.5) | 8.33e-17 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.6, 0.5) | 1.25e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.65, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.65, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.65, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.65, 0.5) | 2.78e-17 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.65, 0.5) | 1.94e-16 | 1e-12 | yes |
| pattern probabilities positive at (0.7, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.7, 0.5) | 1.11e-16 | 1e-13 | yes |
| pattern marginals at (0.7, 0.5) | 5.55e-17 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.7, 0.5) | 3.61e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.7, 0.5) | 2.78e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.75, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.75, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.75, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.75, 0.5) | 0 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.75, 0.5) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.8, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.8, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.8, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.8, 0.5) | 1.11e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.8, 0.5) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.85, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.85, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.85, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.85, 0.5) | 0 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.85, 0.5) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.9, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.9, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.9, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.9, 0.5) | 0 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.9, 0.5) | 5.55e-17 | 1e-12 | yes |
| pattern probabilities positive at (0.95, 0.5) | 0 | 0 | yes |
| pattern probabilities sum to 1 at (0.95, 0.5) | 0 | 1e-13 | yes |
| pattern marginals at (0.95, 0.5) | 0 | 1e-13 | yes |
| I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at (0.95, 0.5) | 1.11e-16 | 1e-12 | yes |
| the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at (0.95, 0.5) | 2.22e-16 | 1e-12 | yes |
| three-variable closed forms against the reduction, every grid matrix | 5.55e-17 | 1e-12 | yes |
| four-variable reduction against Genz, every grid matrix | 5.33e-08 | 1e-06 | yes |
| rate d(MMI sts)/dr1 at the two steps within 1 % (+ 10⁻⁶) | -0.0181 | 1e-06 | yes |
| rate d(MMI sts)/dq at the two steps within 1 % (+ 10⁻⁶) | -0.0015 | 1e-06 | yes |
| rate d(MMI EC)/dr1 at the two steps within 1 % (+ 10⁻⁶) | -0.00907 | 1e-06 | yes |
| rate d(MMI EC)/dq at the two steps within 1 % (+ 10⁻⁶) | -0.000662 | 1e-06 | yes |
| rate d(2A)/dr1 at the two steps within 1 % (+ 10⁻⁶) | -0.0186 | 1e-06 | yes |
| rate d(2A)/dq at the two steps within 1 % (+ 10⁻⁶) | 8.33e-14 | 1e-06 | yes |
| rate d(TDMI)/dr1 at the two steps within 1 % (+ 10⁻⁶) | -0.0184 | 1e-06 | yes |
| rate d(TDMI)/dq at the two steps within 1 % (+ 10⁻⁶) | -0.000588 | 1e-06 | yes |
| rate d(MMI rtr)/dr1 at the two steps within 1 % (+ 10⁻⁶) | -0.000223 | 1e-06 | yes |
| rate d(MMI rtr)/dq at the two steps within 1 % (+ 10⁻⁶) | -0.00076 | 1e-06 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 1) | 0 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 2) | 0 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 3) | 2.22e-16 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 4) | 0 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 5) | 2.22e-16 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 6) | 2.22e-16 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 7) | 4.44e-16 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 8) | 0 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 9) | 8.88e-16 | 1e-12 | yes |
| operating point (0.85, 0.25): phyid's local CCS atoms recomputed from its local MIs, sample by sample (series 10) | 0 | 1e-12 | yes |
| operating point (0.85, 0.25): MMI sts of phyid at n = 100,000 within 4 SE + 2e-4 of the limit | -0.00481 | 0.0002 | yes |
| operating point (0.85, 0.25): MMI EC of phyid at n = 100,000 within 4 SE + 2e-4 of the limit | -0.00231 | 0.0002 | yes |
| operating point (0.85, 0.25): 2A of phyid at n = 100,000 within 4 SE + 2e-4 of the limit | -0.00434 | 0.0002 | yes |
| operating point (0.85, 0.25): TDMI of phyid at n = 100,000 within 4 SE + 2e-4 of the limit | -0.00398 | 0.0002 | yes |
| operating point (0.85, 0.25): MMI rtr of phyid at n = 100,000 within 4 SE + 2e-4 of the limit | -0.000963 | 0.0002 | yes |
| phyid's local CCS atoms equal their recomputation from its local MIs, sample by sample, every replicate | 4e-15 | 1e-12 | yes |
| the maximum-entropy fits' marginals | 9.99e-16 | 1e-12 | yes |

Wall-clock 482 s.
