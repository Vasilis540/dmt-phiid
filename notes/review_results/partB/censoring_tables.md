# The replaced volumes and the autocorrelation (partB29_censoring.py)
git=13e7299

TRs with framewise displacement above 0.4 mm (the release's scrubbing threshold, at which the data authors' Reporting Summary says the volume was replaced by the mean of the surrounding volumes), from data/FDlong.mat, per subject, run and window of 60 TRs; r₁ = the window's whole-brain lag-1 autocorrelation (rev_series.autocorr_series, window mode). DiD = windows 6–14 minus 1–4, DMT minus placebo; p = exact sign-flip over the 14 subjects.

## (a) TRs above the threshold per run, and the DiD of the count per window and of the mean FD

| subject | DMT: count (share), mean FD | placebo: count (share), mean FD | count per window: DMT pre / post, placebo pre / post | count DiD | mean-FD DiD |
|---|---|---|---|---|---|
| 1 | 62 (0.074), 0.187 | 5 (0.006), 0.130 | 0.75 / 5.33, 0.00 / 0.56 | +4.03 | +0.0033 |
| 2 | 14 (0.017), 0.145 | 38 (0.045), 0.164 | 2.25 / 0.00, 2.50 / 2.56 | -2.31 | -0.0389 |
| 3 | 0 (0.000), 0.068 | 0 (0.000), 0.094 | 0.00 / 0.00, 0.00 / 0.00 | +0.00 | -0.0077 |
| 4 | 3 (0.004), 0.111 | 24 (0.029), 0.148 | 0.25 / 0.22, 4.50 / 0.56 | +3.92 | +0.0602 |
| 5 | 6 (0.007), 0.102 | 4 (0.005), 0.093 | 0.00 / 0.67, 0.50 / 0.22 | +0.94 | -0.0125 |
| 6 | 30 (0.036), 0.145 | 7 (0.008), 0.120 | 1.50 / 2.67, 1.25 / 0.22 | +2.19 | +0.0669 |
| 7 | 102 (0.121), 0.235 | 1 (0.001), 0.132 | 0.75 / 10.33, 0.00 / 0.11 | +9.47 | +0.0737 |
| 8 | 24 (0.029), 0.120 | 6 (0.007), 0.090 | 0.25 / 1.00, 1.50 / 0.00 | +2.25 | +0.0935 |
| 9 | 21 (0.025), 0.127 | 0 (0.000), 0.080 | 0.75 / 0.11, 0.00 / 0.00 | -0.64 | -0.0273 |
| 10 | 8 (0.010), 0.171 | 19 (0.023), 0.168 | 0.25 / 0.44, 0.00 / 1.78 | -1.58 | +0.0161 |
| 11 | 29 (0.035), 0.142 | 6 (0.007), 0.133 | 2.25 / 1.56, 0.00 / 0.67 | -1.36 | -0.0361 |
| 12 | 11 (0.013), 0.138 | 21 (0.025), 0.163 | 0.50 / 0.44, 0.00 / 2.00 | -2.06 | -0.0322 |
| 13 | 19 (0.023), 0.105 | 7 (0.008), 0.086 | 0.00 / 1.67, 0.00 / 0.78 | +0.89 | +0.0226 |
| 14 | 2 (0.002), 0.117 | 4 (0.005), 0.159 | 0.00 / 0.00, 0.25 / 0.33 | -0.08 | +0.0192 |
| mean | 23.6 (0.028), 0.137 | 10.1 (0.012), 0.126 | 0.68 / 1.75, 0.75 / 0.70 | +1.12 (p = 0.2166; 7/14 positive) | +0.0143 (p = 0.2452; 8/14 positive) |

## (b) Across subjects: the count DiD and the mean-FD DiD against the r₁ DiD and the sts DiD

| variant | r(count DiD, r₁ DiD) | r(count DiD, sts DiD) | r(mean-FD DiD, r₁ DiD) | r(mean-FD DiD, sts DiD) | r(count DiD, mean-FD DiD) |
|---|---|---|---|---|---|
| ts_gsr | -0.107 | -0.100 | -0.363 | -0.339 | +0.708 |
| ts_demean | +0.037 | +0.008 | -0.301 | -0.252 | +0.708 |

## (c) Within subjects and runs, across windows: the window's count against its r₁ (each run's 14 windows centred on their own means; 392 windows)

ts_gsr: r = -0.124 (windows with at least one TR above the threshold: 137 of 392; mean r₁ in them 0.8428, in the others 0.8451).
ts_demean: r = -0.025 (windows with at least one TR above the threshold: 137 of 392; mean r₁ in them 0.8342, in the others 0.8352).

## (d) Subjects 8 and 14 by window (count above the threshold / mean FD / r₁ on ts_gsr)

subject 8, DMT: w1 0 / 0.10 / 0.852; w2 0 / 0.15 / 0.859; w3 1 / 0.09 / 0.851; w4 0 / 0.05 / 0.884; w5 14 / 0.27 / 0.825; w6 3 / 0.18 / 0.829; w7 2 / 0.13 / 0.834; w8 1 / 0.15 / 0.806; w9 1 / 0.13 / 0.819; w10 0 / 0.09 / 0.820; w11 0 / 0.09 / 0.830; w12 0 / 0.10 / 0.824; w13 2 / 0.08 / 0.850; w14 0 / 0.07 / 0.839
subject 8, placebo: w1 2 / 0.16 / 0.860; w2 3 / 0.14 / 0.826; w3 0 / 0.11 / 0.807; w4 1 / 0.15 / 0.872; w5 0 / 0.12 / 0.829; w6 0 / 0.10 / 0.862; w7 0 / 0.08 / 0.851; w8 0 / 0.08 / 0.870; w9 0 / 0.06 / 0.875; w10 0 / 0.06 / 0.891; w11 0 / 0.06 / 0.879; w12 0 / 0.05 / 0.880; w13 0 / 0.04 / 0.877; w14 0 / 0.04 / 0.861
subject 14, DMT: w1 0 / 0.14 / 0.828; w2 0 / 0.14 / 0.825; w3 0 / 0.14 / 0.803; w4 0 / 0.13 / 0.783; w5 2 / 0.18 / 0.830; w6 0 / 0.10 / 0.830; w7 0 / 0.11 / 0.822; w8 0 / 0.09 / 0.835; w9 0 / 0.08 / 0.812; w10 0 / 0.09 / 0.823; w11 0 / 0.11 / 0.827; w12 0 / 0.11 / 0.850; w13 0 / 0.10 / 0.865; w14 0 / 0.12 / 0.860
subject 14, placebo: w1 0 / 0.19 / 0.833; w2 1 / 0.22 / 0.842; w3 0 / 0.19 / 0.839; w4 0 / 0.16 / 0.816; w5 0 / 0.23 / 0.806; w6 0 / 0.19 / 0.821; w7 0 / 0.16 / 0.836; w8 0 / 0.13 / 0.844; w9 0 / 0.14 / 0.837; w10 0 / 0.11 / 0.845; w11 0 / 0.12 / 0.825; w12 1 / 0.12 / 0.834; w13 0 / 0.13 / 0.832; w14 2 / 0.13 / 0.837

## (e) The non-finite TR

Non-finite TRs of ts_gsr (subject, run, TR index from 0): (3, placebo, 839); it is the last TR of its run (index 839) and falls at the end of window 14.

## Reading under the rule of the pre-run entry

Reported as computed; the entry's predictions (more marked TRs after the injection on the DMT run than before, relative to placebo, in the count and in the mean FD; within runs the count correlating positively with r₁ on both variants; no sign prediction for the count DiD against the r₁ DiD across subjects) are read against (a)–(c) in the outcome entry, and the Dataset paragraph, Results 2 or Limitations and S4 Text state the replacement and what it can and cannot do to r₁ as the rule says.
