# The pre-injection gap and the per-subject relations (partB27_baseline_gap.py)
git=13e7299

Per subject: pre = mean of windows 1–4 (bins 1–8 at W = 30), post = windows 6–14 (bins 11–28); pre gap = DMT pre − placebo pre; post gap = DMT post − placebo post; DiD = post gap − pre gap. Means with B21's inverted sign-flip 95 % intervals and exact sign-flip p (2^14 assignments); 'adjusted' = the intercept of the OLS regression of the post gap on the pre gap (the post gap expected at a pre gap of zero), with its 95 % t interval (12 df), and the regression's slope; r(DiD, pre gap) and r(DiD, post gap) across the 14 subjects. nats for sts and the residual; r₁ dimensionless.

## (a) The gaps, the DiD and the baseline-adjusted contrast

| quantity | variant | W | pre gap (DMT − placebo) | p; share > 0 | post gap | p; share < 0 | DiD | p | adjusted (post gap at pre gap 0) | slope on pre gap | r(DiD, pre gap) | r(DiD, post gap) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sts | ts_gsr | 60 | +0.0176 [-0.0131, +0.0465] | 0.2307; 10/14 | -0.0633 [-0.0917, -0.0369] | 0.0001; 14/14 | -0.0809 [-0.1317, -0.0310] | 0.0038 | -0.0544 [-0.0806, -0.0283] | -0.503 [-0.992, -0.013] | -0.888 | +0.868 |
| r1 | ts_gsr | 60 | +0.0025 [-0.0044, +0.0092] | 0.4417; 10/14 | -0.0122 [-0.0187, -0.0064] | 0.0002; 13/14 | -0.0146 [-0.0261, -0.0037] | 0.0106 | -0.0110 [-0.0170, -0.0050] | -0.480 [-0.997, +0.038] | -0.874 | +0.860 |
| substituted | ts_gsr | 60 | +0.0227 [-0.0105, +0.0543] | 0.1576; 10/14 | -0.0697 [-0.1041, -0.0386] | 0.0001; 14/14 | -0.0924 [-0.1503, -0.0348] | 0.0037 | -0.0566 [-0.0888, -0.0245] | -0.576 [-1.119, -0.033] | -0.877 | +0.886 |
| residual | ts_gsr | 60 | -0.0051 [-0.0111, +0.0006] | 0.0775; 5/14 | +0.0064 [-0.0007, +0.0141] | 0.0782; 3/14 | +0.0115 [+0.0005, +0.0226] | 0.0421 | +0.0044 [-0.0042, +0.0130] | -0.398 [-1.165, +0.369] | -0.754 | +0.859 |
| sts | ts_demean | 60 | +0.0185 [-0.0207, +0.0562] | 0.3116; 9/14 | -0.0846 [-0.1208, -0.0480] | 0.0001; 14/14 | -0.1031 [-0.1629, -0.0435] | 0.0026 | -0.0796 [-0.1170, -0.0421] | -0.272 [-0.834, +0.290] | -0.818 | +0.788 |
| r1 | ts_demean | 60 | +0.0054 [-0.0031, +0.0136] | 0.1871; 9/14 | -0.0162 [-0.0242, -0.0086] | 0.0002; 13/14 | -0.0216 [-0.0331, -0.0102] | 0.0017 | -0.0161 [-0.0250, -0.0073] | -0.016 [-0.606, +0.574] | -0.735 | +0.691 |
| substituted | ts_demean | 60 | +0.0285 [-0.0188, +0.0750] | 0.2103; 8/14 | -0.0929 [-0.1352, -0.0506] | 0.0001; 14/14 | -0.1213 [-0.1874, -0.0554] | 0.0022 | -0.0903 [-0.1369, -0.0438] | -0.089 [-0.647, +0.469] | -0.775 | +0.706 |
| residual | ts_demean | 60 | -0.0100 [-0.0223, +0.0021] | 0.1011; 7/14 | +0.0083 [-0.0012, +0.0186] | 0.0895; 4/14 | +0.0182 [+0.0072, +0.0293] | 0.0040 | +0.0127 [+0.0025, +0.0228] | +0.442 [-0.007, +0.892] | -0.615 | +0.346 |
| sts | ts_gsr | 30 | +0.0160 [-0.0124, +0.0427] | 0.2417; 10/14 | -0.0526 [-0.0776, -0.0299] | 0.0002; 13/14 | -0.0686 [-0.1142, -0.0242] | 0.0042 | -0.0453 [-0.0689, -0.0218] | -0.453 [-0.929, +0.022] | -0.887 | +0.852 |
| r1 | ts_gsr | 30 | +0.0026 [-0.0045, +0.0093] | 0.4419; 9/14 | -0.0116 [-0.0172, -0.0064] | 0.0005; 12/14 | -0.0142 [-0.0249, -0.0032] | 0.0165 | -0.0105 [-0.0156, -0.0054] | -0.411 [-0.835, +0.012] | -0.903 | +0.838 |
| substituted | ts_gsr | 30 | +0.0214 [-0.0109, +0.0519] | 0.1692; 10/14 | -0.0655 [-0.0986, -0.0360] | 0.0005; 12/14 | -0.0869 [-0.1430, -0.0317] | 0.0046 | -0.0538 [-0.0854, -0.0222] | -0.544 [-1.095, +0.007] | -0.870 | +0.878 |
| residual | ts_gsr | 30 | -0.0054 [-0.0136, +0.0026] | 0.1754; 6/14 | +0.0129 [+0.0044, +0.0221] | 0.0037; 2/14 | +0.0183 [+0.0047, +0.0318] | 0.0134 | +0.0115 [+0.0014, +0.0216] | -0.246 [-0.938, +0.447] | -0.749 | +0.810 |

## (b) The per-subject relations of sts and the residual with r₁: DiDs, gaps and the partial correlation

| variant | W | r(sts DiD, r₁ DiD) | r(sts pre gap, r₁ DiD) | r(sts pre gap, r₁ pre gap) | r(sts post gap, r₁ post gap) | r(sts DiD, r₁ DiD given sts pre gap) | r(residual DiD, r₁ DiD) | r(residual pre gap, r₁ DiD) | r(residual post gap, r₁ post gap) |
|---|---|---|---|---|---|---|---|---|---|
| ts_gsr | 60 | +0.953 | -0.844 | +0.922 | +0.939 | +0.824 | -0.780 | +0.374 | -0.838 |
| ts_demean | 60 | +0.958 | -0.735 | +0.920 | +0.895 | +0.914 | -0.597 | +0.342 | -0.731 |
| ts_gsr | 30 | +0.921 | -0.799 | +0.862 | +0.912 | +0.765 | -0.871 | +0.463 | -0.950 |

## (c) ts_gsr, W = 60: the residual DiD on the r₁ DiD across subjects, with subjects left out; the test's sensitivity; Fieller's g

All 14 subjects: slope -0.753 [-1.133, -0.373], r = -0.780; r(sts DiD, r₁ DiD) = +0.953.

| subjects left out | slopes (min to max) | intervals containing 0 | containing −0.18 (band-passed) | containing −0.39 (AR(1)) | containing −0.37 (null) | r(residual DiD, r₁ DiD) (min to max) | r(sts DiD, r₁ DiD) (min to max) |
|---|---|---|---|---|---|---|---|
| one (14 sets) | -0.791 to -0.699 | 0 | 0 | 11 | 11 | -0.871 to -0.670 | +0.921 to +0.964 |
| two (91 sets) | -0.906 to -0.642 | 1 | 13 | 71 | 63 | -0.930 to -0.465 | +0.846 to +0.973 |
| subject 8 (the largest fall of r₁) | -0.785 [-1.361, -0.208] | — | — | — | — | -0.670 | +0.921 |
| subject 14 (the rise of r₁) | -0.699 [-1.180, -0.218] | — | — | — | — | -0.694 | +0.931 |
| subjects 8 and 14 | -0.667 [-1.561, +0.227] | — | — | — | — | -0.465 | +0.846 |

Sensitivity: the residual DiD's SE over subjects is 0.0051 nats; the minimal difference from a point expectation detected with 80 % power at the two-sided 5 % level (one-sample t, 13 df) is 0.0155 nats; the data's residual DiD, +0.0115, exceeds the three expectations (+0.0027, +0.0049, +0.0054) by +0.0088, +0.0066 and +0.0061.
Fieller's g (the squared ratio of the denominator's half-width to the denominator; the interval is finite for g < 1 and widens as g grows): 0.611 for the sts DiD per unit of r₁ DiD and 0.611 for the residual DiD per unit of r₁ DiD (the same denominator, the whole-brain r₁ DiD, mean -0.01465, SE 0.00530).

## Reading under the rule of the pre-run entry

Reported as computed: the entry's predictions (the r₁ pre gap positive and not significant, the post gap negative and significant, the pre gap the smaller; r(r₁ DiD, r₁ pre gap) below −0.5 and the adjusted r₁ contrast negative; r(sts pre gap, r₁ pre gap) and r(sts post gap, r₁ post gap) above 0.7) are read against (a) and (b) in the outcome entry; (c) and the values the entry lists as known are reported, not predicted; and the text's statements on the primary contrast, the shared variance of the two contrasts and the residual's per-subject slope follow the rule the entry sets.
