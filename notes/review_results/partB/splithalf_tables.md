# Split-half test of the CCS-sts / residual correlation (partB7_splithalf.py)

## ts_gsr, W = 60

| CCS version | r(CCS_odd, res_odd) | r(CCS_even, res_even) | mean within | r(CCS_odd, res_even) | r(CCS_even, res_odd) | mean cross | cross / within |
|---|---|---|---|---|---|---|---|
| pub | +0.847 | +0.783 | +0.815 | +0.160 | +0.478 | +0.319 | 0.39 |
| pub, partial on autocorr | +0.814 | +0.816 | +0.815 | +0.132 | +0.176 | +0.154 | 0.19 |
| code | +0.773 | +0.752 | +0.763 | +0.075 | +0.385 | +0.230 | 0.30 |
| code, partial on autocorr | +0.711 | +0.718 | +0.714 | +0.003 | +0.023 | +0.013 | 0.02 |

Split-half reliabilities (odd vs even per-subject DiD): residual +0.494; pub CCS-sts +0.302; code CCS-sts +0.196; autocorrelation +0.741; MMI sts +0.717.
Group-mean DiDs by half: residual odd +0.0067 / even +0.0164; pub CCS-sts odd +0.0033 / even +0.0054; autocorrelation odd -0.0128 / even -0.0165.

## ts_demean, W = 60

| CCS version | r(CCS_odd, res_odd) | r(CCS_even, res_even) | mean within | r(CCS_odd, res_even) | r(CCS_even, res_odd) | mean cross | cross / within |
|---|---|---|---|---|---|---|---|
| pub | +0.884 | +0.878 | +0.881 | +0.274 | +0.292 | +0.283 | 0.32 |
| pub, partial on autocorr | +0.823 | +0.874 | +0.849 | +0.247 | +0.327 | +0.287 | 0.34 |
| code | +0.856 | +0.821 | +0.838 | +0.323 | +0.313 | +0.318 | 0.38 |
| code, partial on autocorr | +0.796 | +0.814 | +0.805 | +0.289 | +0.365 | +0.327 | 0.41 |

Split-half reliabilities (odd vs even per-subject DiD): residual +0.216; pub CCS-sts +0.417; code CCS-sts +0.518; autocorrelation +0.712; MMI sts +0.686.
Group-mean DiDs by half: residual odd +0.0193 / even +0.0179; pub CCS-sts odd +0.0137 / even +0.0106; autocorrelation odd -0.0215 / even -0.0221.

## Verdict

VERDICT (rule of the record, ts_gsr, published CCS): within-half mean +0.815, cross-half mean +0.319 (+0.160, +0.478) → shared component is estimation noise: both reported as null with this test as the evidence

