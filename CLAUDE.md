# DMT ΦID Project

Secondary analysis of open DMT fMRI data, applying Integrated Information
Decomposition (ΦID) to test whether synergistic information tracks subjective
intensity. Produced as evidence of computational neuroimaging competence for a
PhD application to the Cognition and Consciousness Imaging Group (CCIG),
Division of Anaesthesia, University of Cambridge (Prof. Emmanuel Stamatakis).

## Hard deadlines

- **20 Nov 2026** — public preprint + documented repo
- **8 Dec 2026** — Cambridge application (Gates Cambridge / Cambridge Trust)

## The scientific claim under test

Luppi et al. (eLife 2024, 10.7554/eLife.88173.4) showed the brain's
"synergistic workspace" collapses under propofol anaesthesia and in disorders
of consciousness. Nobody has applied time-resolved ΦID to a psychedelic fMRI
dataset, nor coupled it to a continuous subjective-intensity measure.

Hypothesis: whole-brain synergy is dynamically up-regulated under DMT and
tracks per-subject subjective intensity over the ~20-minute experience.

Nearest prior work, must be cited and differentiated from:
- Luppi et al., eLife 2024 — the anaesthesia/DoC version of this measure
- Liardi, Rosas, Carhart-Harris, Bor, Mediano (arXiv:2410.11583, 2024) —
  static PID on MEG under LSD/psilocybin/ketamine. NOT fMRI, NOT DMT, NOT
  time-resolved, NOT intensity-coupled. Preprint, not peer reviewed.
- Timmermann et al., PNAS 2023 (10.1073/pnas.2218949120) — source paper for
  the data; found intensity correlates with raw pairwise connectivity. Our
  contribution reframes the neural side as an information-theoretic quantity.
- Singleton et al., Commun Biol 2025 (10.1038/s42003-025-08078-9) — network
  control energy on this same dataset. This is whose repo the data lives in.
  Do not duplicate their analysis.

## Data — all verified present and loadable (11 Sep 2026)

Source: https://github.com/singlesp/DMT_NCT (data committed in-repo, NOT
behind the Zenodo DOI). No data-use agreement, no request email.
**On disk the files live under `external/DMT_NCT/data/`** (the submodule
checkout); the `data/` paths below are relative to that directory. Subject
index 2, PCB run, TR 839 is NaN across all regions in every variant;
`01_synergy_timecourse.py` drops non-finite TRs.

`data/DMT_clean_mni_continuous_fullPreprocsch116.mat`  (81 MB)
- Four preprocessing variants, each a (14, 2) object array:
  `ts` (raw), `ts_demean`, `ts_gsr`, `ts_z`
- Indexing: `[subject, condition]`, 14 subjects × 2 conditions
- Each element: **(116 regions, 840 TRs) float64**, Schaefer-116 parcellation
- The GSR/no-GSR variants give the GSR robustness check for free
- Condition axis confirmed from the original MATLAB
  (`external/DMT_NCT/scripts/01_gen_time_resolved_ce.m` uses `TS{i,1}` for DMT
  and `TS{i,2}` for PCB). In Python: **index 0 = DMT, index 1 = placebo.**

`data/intensity_ratings.mat`
- `dmt_intensity` (14, 28) uint8, `pcb_intensity` (14, 28) uint8
- **Per-subject, not group-mean**
- 840 TRs / 28 ratings = **exactly 30 TRs per rating bin**, no interpolation needed
- Mean DMT curve: ~0 for bins 1-8, jumps to 8.5, peaks 9.3 at bin 10, decays
  to ~0.4 by bin 28. Placebo flat at ~0 throughout.

`data/Schaefer116_HCP_DTI_count.mat` — `connectivity` (116,116) float32 and
`vol_normalized_sc` (116,116) float64. Structural connectome, same parcellation.

`data/5HTvecs_sch116.mat` — `mean5HT1A/1B/2A/4/TT_sch116`, each (116,1).
Serotonin receptor densities in the same space.

`data/FDlong.mat` — `FDDMT` (840,14), `FDPCB` (840,14). Framewise displacement
per TR per subject. Use this; DMT drives motion.

`data/sch116_to_yeo.csv` — network assignments.

**No LICENSE file in the repo.** Cite Singleton et al. 2025 and the Zenodo DOI
(10.5281/zenodo.15177511); confirm reuse terms before the preprint goes public.

## Method — verified working (11 Sep 2026)

`phyid` is NOT on PyPI. Install from source:
`pip install git+https://github.com/Imperial-MIND-lab/integrated-info-decomp.git`

```python
from phyid.calculate import calc_PhiID
from phyid.utils import PhiID_atoms_abbr
atoms_res, _ = calc_PhiID(x, y, tau=1, kind='gaussian', redundancy='MMI')
# returns 16 atoms × (T-tau) timepoints
# synergy = atoms_res['sts'], redundancy = atoms_res['rtr']
```

Benchmarked at ~3 ms per region pair. Full pairwise (6,670 pairs × 14 subjects
× 2 conditions) ≈ **9 minutes single-core**. No GPU needed.

## Non-negotiable methodological rules

These are what a Cambridge reviewer will check first. Violating any of them
makes the work worse than useless.

1. **Spatial nulls.** Any brain-map correlation (e.g. synergy map vs 5-HT2A)
   uses spin tests (Alexander-Bloch et al. 2018) or BrainSMASH (Burt et al.
   2020). Never naive parametric p-values. `SpinTests/` exists in DMT_NCT/fxns.
2. **Temporal nulls.** Phase-randomised surrogate timeseries for any
   synergy-vs-intensity correlation.
3. **No double-dipping.** Never select regions on an effect and re-test them
   on the same data (Kriegeskorte et al. 2009).
4. **Motion.** Report FD. Regress it. Test whether any effect survives. DMT
   increases motion and autonomic arousal — this is the most likely confound.
5. **N=14.** Report effect sizes with confidence intervals, not just p-values.
   Frame as proof-of-concept, never as established.
6. **Parcellation and preprocessing sensitivity.** Report results across the
   `ts_gsr` and `ts_demean` variants at minimum.
7. **FDR** across regions/edges, method stated explicitly.
8. **Reproducibility.** Pinned environment, fixed seeds, data provenance in
   the README. Every figure regenerable from a single script.

## Kill criteria

- **2 Nov 2026** — if the synergy×intensity effect vanishes under motion
  control AND across both preprocessing variants, write it honestly as a
  null/methods contribution. Do not abandon; do not overclaim.
- Fallback project if this collapses entirely: OpenNeuro `ds003059` (LSD,
  fully preprocessed), gradient/complexity analysis.

## Working conventions

- Python-first. No MATLAB licence required despite `.mat` files and the
  original repo's MATLAB scripts (`scipy.io.loadmat` handles ingestion).
- Scripts numbered by execution order, each independently runnable.
- `SEED = 20261120` everywhere (the preprint deadline; arbitrary but fixed).
- Every result written to `results/` with the script and git SHA that made it.
- Figures to `figs/`, regenerable, no manual editing.

## Pre-registered analysis choices

Recorded here **before any results were inspected.**

- `calc_PhiID(..., kind='gaussian')` fits mean and covariance **once** over
  the entire timeseries (see `phyid/calculate.py`, `_get_entropy_four_vec` at
  lines 16-19: `X_cov = np.cov(X); X_mu = np.mean(X, axis=1)`). The
  per-timepoint atoms it returns are therefore **local values under a
  globally-fitted stationary Gaussian model** — not evidence that the
  underlying joint distribution is non-stationary. This distinction matters
  because our whole scientific claim is that synergy is non-stationary and
  tracks intensity.
- **Robustness A (global fit)**: single global fit over the full 840-TR
  timeseries, as `calc_PhiID` does natively. This is the cheap baseline and
  what `01_synergy_timecourse.py` computes at `FIT_MODE="global"`.

- **Primary B (sliding window)**: sliding-window ΦID with the Gaussian model
  **refit per window** (`FIT_MODE="window"`). This is the primary analysis;
  it keeps the B slot so the A/B/C record of how the decision was made stays
  intact.
  - **Window length: 30 TRs = 60 s.** Fixed before the run, on three
    independent grounds:
    1. TR = 2 s for this dataset, confirmed in the original MATLAB
       (`external/DMT_NCT/scripts/02_global_ce_analyses.m:179` —
       `TR=2; window=60/TR;`).
    2. 30 TRs is exactly one intensity-rating bin (840 TRs / 28 ratings), so
       each window yields one synergy value per rating with no interpolation,
       resampling, or alignment choice left free.
    3. 60 s is the window Singleton et al. 2025 used on this same dataset, so
       it is inherited rather than tuned by us.
  - **Stride: 30 TRs (non-overlapping)** — follows from (2): 28 windows, one
    per rating. Overlapping strides would produce autocorrelated windows that
    get averaged back into the same 28 bins anyway.
  - **Cost to report**: a 30-TR window leaves 29 lag-1 transition samples to
    fit a 4×4 covariance (10 free parameters). Gaussian entropy estimates
    carry O(1/N) bias, so window-level atoms will be noisier and more biased
    than the global fit. That bias is common to both conditions and all
    windows, but it must be stated, not assumed harmless.
  - **Window-length robustness at 60 TRs** (two rating bins per window,
    stride 60, 14 windows; each rating pair averaged to match). This check is
    **load-bearing, not optional**: at ~3 samples per parameter, Gaussian
    entropy bias cannot be assumed equal across conditions if DMT shifts the
    covariance structure — and a shift in covariance structure is precisely
    the hypothesis under test. A 30-TR effect that does not survive at 60 TRs
    is a bias artefact until shown otherwise.
  - **Bias-check outcome (`02_bias_check.py`; simulated VAR(1) data with
    analytic ground truth, 2,000 windows per cell, no real data touched).**
    First run 12 Sep 2026 at git e01c836 with symmetric A, Q; re-run the
    same day after adding an asymmetric family (a1 ≠ a2, c12 ≠ c21,
    unequal innovation variances) because the symmetric parameters left
    two of the four MMI candidates analytically tied, which no real region
    pair is, and after splitting each bias into an entropy-estimation
    component and an MMI-selection component ("oracle selection" = same
    fitted entropies, selections forced to the analytic choice). Numbers
    are in `results/bias_check.csv` and `results/bias_check_differential.csv`.
    - **Share of a true between-condition sts difference absorbed by the
      estimator (differential bias / true difference).** Symmetric family:
      **~70–77 % at W = 30** (70 % coupling shift, 77 % noise-correlation
      shift), **18–45 % at W = 60**. Asymmetric family: **52–66 % at
      W = 30, 15–31 % at W = 60.** Global 840-TR fit: see the next bullet;
      the "5–11 %" and "< 1 %" figures previously recorded here hid a
      sign difference.
    - **Global 840-TR fit (corrected 12 Sep 2026 after an independent
      re-read of the CSVs).** Per-condition sts bias as a share of the
      analytic value: symmetric **−11 / −19 / −13 %** (baseline /
      coupling shift / noise-corr shift), asymmetric **−0.0 / −0.4 /
      −0.9 %**. Differential sts bias: the symmetric coupling shift is
      estimated at −0.0743 nats against a true −0.0671 (**overshoot**,
      10.7 % of the true difference) and the symmetric noise-corr shift
      at −0.0639 against −0.0671 (shrinkage, 4.8 %); the asymmetric
      shifts are −0.0563 vs −0.0562 and −0.0549 vs −0.0546 (both marginal
      overshoot, 0.3 % and 0.6 %). The symmetric global-fit bias is
      almost entirely the selection component (oracle-selection sts bias
      −0.003 / −0.003 / −0.002 nats against totals of −0.029 / −0.036 /
      −0.026) and is therefore a tie artefact of the symmetric family.
      **Once candidates are untied, the global fit is essentially
      unbiased** — on stationary data; see the limitation bullet below.
    - **At W = 30 and W = 60 the bias behaves as multiplicative
      shrinkage**: in all eight cells (two shifts × two families × two
      window lengths) the estimated difference has the true sign and a
      smaller magnitude. **Sign is preserved; magnitude is not.** This
      does **not** hold at the 840-TR global fit, where three of the four
      cells overshoot (symmetric coupling shift by 10.7 %, both asymmetric
      shifts marginally; numbers above). Two shift types in two parameter
      families is evidence, not a theorem, and no cell tested a null with
      equal true sts but different covariance (open question below).
    - **The bias changes sign across conditions, not only magnitude, and
      this is the mechanism of the differential bias.** At W = 30 the
      asymmetric baseline sts is biased **−37.6 %** of its analytic value
      (−0.035 nats) while `asym_shift_noisecorr` is biased **+1.7 %**
      (+0.0007 nats, 95 % CI spanning zero). The differential bias is the
      difference of two per-condition biases, so a covariance shift that
      moves the per-condition bias from strongly negative to ~zero
      produces most of the +0.036 nats differential in that cell. The
      estimator is not applying one shrinkage factor to both conditions;
      it is biased by a different amount under each covariance.
    - **SNR ≈ 1 per pair-window at W = 30** (window-mean / SD across
      windows 0.7–0.9 in all six conditions; 0.8–1.5 at W = 60; 3–7.5 at
      840). **Regional or edge-level windowed maps are therefore not
      viable at W = 30**; only quantities averaged over many pairs (the
      whole-brain mean) can be read at that window length.
    - **MMI min-selection error at W = 30: 13–30 % of windows** in the
      symmetric family (13.5 / 30.2 / 16.2 %, counted only against
      analytically untied minima), **30–40 %** in the asymmetric family
      where nothing is tied (39.9 / 32.4 / 30.3 %); at least one of the
      seven selections wrong in 47–84 % of windows; 3–22 % (rtr) at W = 60;
      0 % at 840. **Condition-dependent** at every window length below
      840, so it feeds differential bias. **It affects rtr more than sts**
      once candidates are untied: in the asymmetric family the selection
      component is 16–97 % of rtr's analytic value (−0.009 to −0.014 nats)
      but within ±0.008 nats of zero for sts (0.6–21 % of analytic). The
      large sts selection component in the symmetric family (−0.07 to
      −0.10 nats, ~35 % of analytic) is a tie artefact: rtr, R_xytab and
      R_abtxy are then minima over analytically tied candidates, each
      biased low by the winner's curse, and each enters sts with
      coefficient +1.
    - **Where the remaining sts bias comes from.** With selections forced
      to the analytic choice, the sts bias at W = 30 is −0.083 nats
      (symmetric baseline) and −0.036 (asymmetric baseline), against
      +0.02 for iid samples: the Wishart/digamma bias of the plug-in
      log-det cancels in sts down to 0.5·[ψ((N−3)/2) − ψ((N−4)/2)]
      ≈ 1/(2(N−4)) (derived from the lattice coefficients; confirmed by an
      iid simulation, +0.022 at N = 29). The negative bias on real windows
      is therefore driven by within-window autocorrelation of the
      four-vector samples, and in the asymmetric family the differential
      sts bias is almost entirely this component (60–68 % of the true
      difference at W = 30 with oracle selection).
    - **`joint_lag_cov` verified twice.** The block placement of
      Cov(z_t+τ, z_t) = A^τ S0 was checked against a 2e6-sample
      simulation of an asymmetric condition (recorded in the function's
      docstring, `scripts/02_bias_check.py`) and independently a second
      time on 12 Sep 2026 against a 4e6-sample asymmetric simulation:
      max deviation **0.0006 as written versus 0.041 for the transposed
      placement**. The analytic ground truth that every bias figure above
      is measured against is therefore not itself in question.
    - **Limitation: every simulated condition is stationary.** Each
      window is drawn from a process whose (A, Q) is constant, so the
      bias check measures recovery of a constant true value. It says
      nothing about estimator behaviour under a mid-run covariance
      change, which is the actual DMT case (intensity ≈ 0 for rating bins
      1–8, then a rise and a ~20-minute decay). In particular, **the
      global fit's near-zero bias at 840 TRs is measured on stationary
      data only and does not license using the global fit for a
      non-stationarity claim**: one Gaussian fitted across a covariance
      change is a model of neither regime.
  - **Pre-registered decision tree for the window / correction choice
    (recorded 12 Sep 2026).** Why this is a legitimate update and not a
    post-hoc change: (i) the bias check ran on simulated data with known
    ground truth and never touched the empirical timeseries; (ii) no
    windowed result on real data exists — `FIT_MODE="window"` in
    `01_synergy_timecourse.py` still raises `NotImplementedError`, and
    `results/` holds only the 20-region global-fit sanity run and the
    bias-check tables; (iii) the pre-registration above required reading
    the bias check *before interpreting any windowed result*, so acting on
    it is executing the plan, not departing from it. The tree:
    1. **Implement analytic bias correction for the Gaussian plug-in
       log-det entropy**: replace each `log det Ŝ_k` (k = 1..4; `np.cov`,
       ddof = 1; N = W − τ four-vector samples) by
       `log det Ŝ_k − Σ_{i=1..k} [ψ((N−i)/2) − ln((N−1)/2)]`, the unbiased
       log-det estimator under iid Gaussian sampling (ψ = digamma). The
       window-mean local atoms equal the plug-in atoms built from these
       log-dets (the per-sample Mahalanobis terms sum to k(N−1)/N and
       cancel in every MI; phyid's per-variable standardisation cancels
       the same way), so the correction is a per-window constant per
       entropy term and leaves the MMI selections as they are.
    2. **Validate it with `02_bias_check.py`**: corrected estimator
       reported alongside the plug-in, all six conditions, all three
       window lengths.
    3. **Criterion, evaluated on sts at W = 30 in every condition and
       every shift of both families**: corrected |bias| < 10 % of the
       analytic sts value **and** corrected |differential bias| < 15 % of
       the true between-condition sts difference → **W = 30 with
       correction is Primary B**, and the 60-TR robustness check is kept
       and run with the same correction. **Otherwise → W = 60,
       uncorrected, is Primary B**, carrying the 15–45 % shrinkage
       measured above as a stated cost.
    4. **Decide before any real windowed result.** The branch is chosen on
       the simulation output alone and recorded here with the numbers
       before `FIT_MODE="window"` is implemented.
    - **Prediction recorded with the tree, before step 1 was run.** The
      step-1 correction depends only on (k, N), not on the covariance, and
      every MMI candidate set compares MIs of identical dimension, so it
      changes no selection. It therefore shifts every condition's sts by
      the same constant, −0.5·[ψ((N−3)/2) − ψ((N−4)/2)] ≈ −0.02 nats at
      N = 29, and **changes the differential bias by exactly zero**. The
      measured differential sts bias at W = 30 is 52–77 % of the true
      difference, so criterion (3) is expected to fail on its second
      clause and the fallback (W = 60, uncorrected) is the expected
      branch. Step 2 is still run: if the prediction fails, the derivation
      is wrong, and that matters more than the branch.
    - **Not yet decided; decide and record before the first real windowed
      run:** what replaces the 60-TR window-length robustness check if the
      fallback branch is taken (candidates: W = 120, four rating bins per
      window, 7 windows; or the global fit A alone).
  - **Pre-registered addition (recorded 12 Sep 2026, before any windowed
    real-data run): why the windowed analysis is primary.** The primary
    justification for windowing is that the global fit **cannot detect
    non-stationarity by construction** — it fits one covariance to the
    whole run and returns local values under that single model — not
    that the global fit is biased (on stationary data it is essentially
    unbiased once candidates are untied; see the bias-check outcome). A
    time-resolved synergy claim therefore needs the windowed estimator
    whatever the bias figures say. To measure what windowing buys and
    what the global fit loses, `02_bias_check.py` gets a
    **non-stationary condition** in which the VAR(1) parameters switch
    partway through an 840-TR run. **Revised 12 Sep 2026, still before
    implementation**: the first version had a single coupling step and no
    criterion; decay conditions, the noise-correlation type, an effective
    sample size and a pass/fail criterion were added. Parameters fixed
    here:
    - **Four conditions, one code path.** Every non-stationary run is a
      staircase of 28 rating bins × 30 TRs with one stationary VAR(1)
      regime per bin. Bin b uses θ_b = θ_base + f_b (θ_shift − θ_base),
      with (θ_base, θ_shift) = (`asym_baseline`, `asym_shift_coupling`)
      for the **coupling** type (θ = c = (c12, c21)) and (`asym_baseline`,
      `asym_shift_noisecorr`) for the **noise-correlation** type (θ = q);
      a and s are fixed. Asymmetric, so no candidate is tied; the run
      asserts this for every bin.
      - `nonstat_step_coupling`, `nonstat_step_noisecorr`: f_b = 0 for
        bins 1–8, 1 for bins 9–28. The switch at TR 240 is the end of
        rating bin 8, where the mean DMT intensity curve leaves zero, and
        a window boundary at both W = 30 (window 9 of 28) and W = 60
        (window 5 of 14), so no window straddles it.
      - `nonstat_decay_coupling`, `nonstat_decay_noisecorr`: f_b = 0 for
        bins 1–8; for bins 9–28, f_b = Ī_b / max Ī, where Ī is the
        14-subject mean DMT intensity rating (`intensity_ratings.mat`,
        `dmt_intensity`). Values, fixed as literals in the script so it
        still touches no data file: 0.9154, 1.0000, 0.9385, 0.8462,
        0.7308, 0.6308, 0.5462, 0.4769, 0.4000, 0.3462, 0.2615, 0.2154,
        0.1846, 0.1462, 0.1308, 0.1077, 0.0846, 0.0692, 0.0769, 0.0462
        (bins 9–28). Bin 9 is 0.915 of the full shift, not 1: the decay
        condition follows the curve literally; the step condition is the
        idealised switch. Bin 27 is above bin 26 (one adjacent pair with
        a true increase), left as is and scored against its own sign.
      - **Why both shift types**: which kind of covariance change DMT
        produces is unknown, and the stationary cells show the two types
        differ by a factor of two in absorption at W = 60 (18 % vs 45 %
        symmetric, 15 % vs 31 % asymmetric).
      - **Why a decay and not only a step**: the step is confounded with
        injection onset (and everything that co-occurs with it: motion,
        arousal), so the decay phase is where the tracking claim is
        identified, and it is the phase that requires resolving small
        differences between adjacent windows.
    - **Burn-in:** 200 TRs under the bin-1 regime. No burn-in after any
      regime change: transients are part of what is being measured and
      are reported, not discarded. Spectral radius of A is ≤ 0.75 in every
      bin, so a transient is ~5 % of its initial size after 10 TRs.
    - **Truth per window, piecewise constant.** At W = 30 the truth for
      window b is the stationary analytic sts of (A_b, Q_b) via
      `joint_lag_cov`. At W = 60 each window spans two bins, and its
      truth is the analytic sts of the equal-weight mixture of the two
      bins' stationary 4×4 lag covariances, the same construct as the
      global-fit target below. Transients are not in the truth; they
      show up as estimator error.
    - **Estimators:** windowed at W = 30 (28 windows, stride 30) and
      W = 60 (14 windows, stride 60), and the global 840-TR fit, all on
      the same simulated runs. 2,000 replicate runs per condition, seed
      20261120. The stationary cells are re-run in the same invocation so
      one git SHA covers every table.
    - **Global-fit reference points:** the pre-switch and peak regime
      values, the sample-weighted mean of the 28 per-bin analytic sts
      values, and the analytic sts of the equal-weight mixture of the 28
      per-bin 4×4 covariances (what the global fit converges to as
      N → ∞). For the step conditions the last two use weights 8/28 and
      20/28.
    - **Effective sample size for the pooled whole-brain mean (method
      and number recorded 12 Sep 2026, before use).** The real analysis
      pools 6,555 non-independent pairs from 115 regions in 14 subjects.
      n_eff = participation ratio (Σλ)² / Σλ² of the eigenvalues λ of the
      115 × 115 Pearson correlation matrix of each subject's **placebo**
      run (region 20 dropped, non-finite TRs dropped), averaged over the
      14 subjects. Result: **ts_demean 10.8** (SD 3.0, range 5.8–17.8;
      ts_z and raw ts are identical because correlation is invariant to
      per-region demeaning and scaling), **ts_gsr 14.3** (SD 2.3, range
      11.3–18.4). DMT runs, for reference only: 10.3 and 15.3. **Choice
      (revised 12 Sep 2026, before the run): primary M = 14 × C(14.3, 2)
      = 1,338 from ts_gsr, with M = 14 × C(10.8, 2) = 742 from ts_demean
      as the conservative sensitivity; the criterion must pass at both.**
      The first draft used the ts_demean figure alone as "more
      conservative and less processed"; it was changed because ts_gsr is
      the analysis stream for every other result, so the deciding
      precision figure should come from the same stream, while keeping
      the smaller M as a required sensitivity guards against the choice
      flattering the estimator. Subjects are treated as independent and
      pairs of independent components as independent noise draws, which
      they are not exactly since two pairs can share a component, so both
      M values are upper bounds. Reported but not deciding: M = 151
      (14 × n_eff, one unit per component rather than per pair).
      Translation: SE of the whole-brain mean sts per window ≈
      SD_pair-window / √M; at W = 60 the asymmetric stationary cells give
      SD 0.037–0.074 nats, so SE ≈ 0.0010–0.0020 nats at M = 1,338, and
      an adjacent-window difference has SE ≈ √2 × that. The
      per-pair SD is from a single simulated pair; real pairs are
      heterogeneous, and between-subject spread of the true value is not
      in this figure because the tracking claim is within-subject.
    - **Pre-registered pass/fail criterion for adjacent-pair tracking
      (recorded before the run; threshold and M revised 12 Sep 2026, also
      before the run).** Question decided: can a windowed estimator
      resolve gradual covariance change at the pooling available here?
      Decay pairs are the adjacent window pairs inside the decay: at
      W = 30, windows 10→11 … 27→28 (18 pairs); at W = 60, windows
      5→6 … 13→14 (9 pairs). Every decay pair has a non-zero true sts
      difference by construction. Procedure, per decay condition, window
      length and M: B = 2,000 bootstrap draws; each draw takes M replicate
      runs with replacement, averages each window's estimated sts across
      them (the simulated whole-brain mean), takes the adjacent
      differences over the decay pairs and scores each against the sign
      of the true difference. **S = the mean over draws of the fraction
      of correctly signed decay pairs**, with its 2.5–97.5 % range over
      draws; the per-pair correct-sign probability is also reported
      against |true Δsts|. **Pass at W = 60: S ≥ 0.80 for both decay
      conditions at both M = 1,338 and M = 742.** Reasoning: under a null
      the sign of an estimated adjacent difference is a coin flip, so
      chance is S = 0.5 and the criterion is a distance from chance, not
      an absolute score. S = 0.80 means at most one adjacent decay step
      in five reads the wrong way. The first draft set 0.75; it was
      raised because one step in four pointing the wrong way is not a
      tracking claim worth defending, and because the real data add
      motion, arousal and between-subject heterogeneity on top of the
      simulated estimator noise, so the simulation should clear the bar
      with margin. **Fail: S < 0.80 in any deciding cell.** The W = 30
      result is reported at the same M values but decides nothing, since
      the window-length branch is decided by the tree above on the
      stationary cells alone. The step conditions have no criterion:
      they are read out for whether the windowed estimator recovers the
      change (sign, magnitude within the stationary shrinkage at that W)
      and how far the global fit lands from either regime.
    - **Noise-floor prediction, recorded before the run and derived from
      existing numbers only.** From the pre-registered parameters, the
      analytic per-bin truths in the decay conditions differ between
      adjacent bins by ~0.001–0.006 nats. From the stationary cells, the
      per-pair-window sts SD is ~0.08 nats at W = 30 (asym_baseline
      0.076) and 0.037–0.074 at W = 60. Pooling M = 1,338 divides the SD
      by ~37, to ~0.002 nats per window at W = 30 and ~0.001–0.002 at
      W = 60, and an adjacent difference carries √2 × that. The smallest
      adjacent differences therefore sit at or below the pooled noise
      floor, and the largest are only a few SE above it. **Prediction:
      the adjacent-pair criterion will be marginal or fail, with the
      smallest pairs (late decay, bins ~20–28) near chance and the early
      decay pairs correctly signed.** This is a calculation from the
      stationary tables and the parameters, not from any non-stationary
      result; none existed when it was written.
    - **Pre-registered intermediate fallback: full-decay tracking
      (recorded before the run).** Between "adjacent-pair pass" and "step
      contrast only": the claim that pooled synergy correlates with
      intensity **across** the decay, bins 10–28, rather than resolving
      each successive step. This pools 19 bins spanning the full decay
      range, where the total change in true sts (~0.05 nats) is an order
      of magnitude larger than any adjacent step; it remains a
      within-drug claim identified away from onset; and it is a
      substantially easier estimation problem. Statistic, per decay
      condition, W and M, on the same bootstrap draws: the Spearman rank
      correlation ρ_S between the pooled estimated sts per decay window
      and the intensity scale f per window (W = 30: windows 10–28, 19
      windows, f_b; W = 60: windows 5–14, 10 windows, mean f of the two
      bins), multiplied by the sign of ρ_S between the analytic truth
      and f (−1 by construction: sts decreases monotonically in f, so
      the truth is perfectly rank-ordered against intensity; the script
      reports this value rather than assuming it). **R = the mean over
      draws of that sign-corrected ρ_S**, with its 2.5–97.5 % range.
      Spearman rather than Pearson because the truth is monotone but not
      linear in f. **Pass at W = 60: R ≥ 0.80 for both decay conditions
      at both M = 1,338 and M = 742.** Reasoning: chance is ρ_S = 0; with
      10 windows, ρ_S ≥ 0.80 bounds the sum of squared rank displacements
      at 33, so three adjacent-window swaps or one window displaced by
      four ranks still pass and more disorder than that fails. The same
      0.80 is used for both statistics so the two tiers differ only in
      what is being resolved, not in stringency.
    - **Pre-registered ordering of outcomes for the paper's primary
      empirical claim.** (1) **Adjacent-pair tracking passes** → the
      headline is that whole-brain synergy follows the within-subject
      intensity time course step by step. (2) **Adjacent fails,
      full-decay passes** → the headline is that synergy correlates with
      intensity across the decay phase, with the explicit statement that
      successive windows cannot be resolved at this pooling. (3) **Both
      fail** → the primary result is the step-change contrast (pre-onset
      bins 1–8 vs post-onset bins 9–28, DMT vs placebo, at W = 60) plus
      the methods contribution (bias characterisation and the global
      fit's smearing of non-stationarity). Passing one decay condition
      but not the other counts as a fail at that tier; the passing type
      is reported with the statement that the real covariance-change
      type is not identified. The tier is fixed by the simulation
      before the first real windowed run.
    - **Bootstrap caveat and analytic counterpart (recorded 12 Sep 2026
      before any non-stationary verdict existed; the first full run was
      stopped before its non-stationary section to add this).** The
      pooled mean is emulated by drawing M runs with replacement from
      N_RUNS = 2,000. **M / N_RUNS = 0.67 (M = 1,338) and 0.37 (M =
      742).** Every draw is therefore centred on the same 2,000-run
      sample mean, whose own SE is √(M/N_RUNS) = 0.82 and 0.61 of the
      pooled SD. The bootstrap spread measures resampling variability
      around a fixed centre, not the variability of fresh pools of M
      units, and a per-pair correct-sign probability from it is
      conditional on where the realised sample mean happened to fall.
      Alongside the bootstrap S the script computes, per decay pair,
      **P_analytic = Φ(sign(true Δ) · d̂ / SD_pooled)** under approximate
      normality of the pooled mean, with d̂ the 2,000-run mean difference,
      SD_pooled = √(v/M), and an interval from d̂ ± 1.96·√(v/N_RUNS);
      **S_analytic = mean of P_analytic over decay pairs**, with the
      interval carried through. **The tier-1 verdict is taken on
      S_analytic**, and where the two versions differ materially
      (> 0.02 in S, or a different pass/fail) the analytic value is the
      one to trust: it uses the full-sample SD rather than a resampled
      one, has no resampling noise or discretisation at 0 and 1, and
      makes the centring assumption explicit through the interval. Both
      versions share that centring, which is the true limitation, and
      the remedy is more runs, not more draws. **Undetermined rule:** if
      in any deciding cell the analytic interval of S, or the bootstrap
      2.5–97.5 % range of R (which has no simple analytic counterpart and
      carries the same caveat), straddles 0.80, no tier is assigned; the
      run is repeated with `--n-runs 20000` (M / N_RUNS ≤ 0.07, ≈ 4.5 h
      single-core) and the tier is taken from that run.
    - **Tier 2 controls, pre-registered before any verdict.** Tier 2
      rewards any estimator that preserves a monotone trend: ρ_S ≥ 0.80
      over 10 windows says the ordering survived, not that magnitudes
      were recovered, and it is satisfied by an estimator that shrinks
      the whole decay by half. On real data the decay phase confounds
      drug washout with **motion settling, arousal decline and time in
      scanner, all of which are monotone over the same windows**, so a
      monotone synergy trend across bins 10–28 is evidence for tracking
      only if it is absent from data with the same time course and no
      drug. **Tier 2's evidential value is therefore lower than tier 1's
      for causal as well as statistical reasons, and a tier-2 pass on
      simulation licenses the analysis, not the causal claim.** Required
      controls on real data, fixed now; the intensity template is the
      14-subject mean DMT curve f (the same one used in simulation),
      windows are the tier-2 decay windows at the deciding W (W = 60:
      windows 5–14), and the tier-2 statistic on real data is each
      subject's ρ_S between window-mean whole-brain synergy on the DMT
      run and intensity over those windows, tested at group level
      against the phase-randomised temporal null (rule 2).
      - **Which intensity: per-subject ratings are primary on real data
        (fixed 12 Sep 2026, before any real windowed run).** Two versions
        exist: each subject's own DMT ratings (`dmt_intensity[s, :]`,
        bins 10–28; at W = 60 the mean of the two bins' ratings per
        window), or the group-mean template f. **Per-subject is primary**:
        it uses between-subject variation in the intensity time course,
        and it is the actual claim (synergy tracks *that subject's*
        experience), not a claim about the group-average curve. **The
        group template is a sensitivity analysis**, kept because it is
        the only version the simulation can validate: the simulation has
        one intensity curve, so tier 2 on simulation tests the template
        version and says nothing directly about the per-subject one.
        The first draft of this section named the template as primary
        with the per-subject version "reported alongside"; that was
        reversed here, before any real windowed result existed, for the
        two reasons just given. Ratings are integers 0–10, so ties are
        common; ρ_S uses average ranks, and a subject whose ratings are
        constant over the decay windows has no defined ρ_S, is excluded
        from that statistic and counted in the report. The controls
        below are defined against the template because a placebo run has
        no per-subject intensity variation to correlate with; the primary
        per-subject claim must still clear both controls as written, and
        the FD-residualised recomputation in (b) is run on both versions.
      - **(a) Time-in-scanner control.** The identical statistic on each
        subject's **placebo** run: ρ_S between window-mean synergy on
        the PCB run and the same template f over the same windows.
        Placebo ratings are flat, so this correlates synergy with time
        alone. **Void rules:** the tier-2 claim is void if the
        within-subject difference ρ_DMT − ρ_PCB has a 95 % CI including
        zero (subject-level bootstrap, 10,000 resamples, seed 20261120),
        **or** if the sign-corrected group-mean ρ_PCB has the same sign
        as ρ_DMT and is at least half its magnitude, meaning time alone
        reproduces at least half the trend even when the difference is
        detectable.
      - **(b) Motion-settling control.** Window-mean framewise
        displacement per subject from `FDlong.mat` (`FDDMT`, and `FDPCB`
        for reference) over the same windows, and ρ_S between it and f.
        The group-mean FD correlation with the template is reported with
        its CI. Then the tier-2 statistic is recomputed on **FD-residualised
        synergy**: within each subject, window-mean synergy regressed on
        window-mean FD across the decay windows, residuals correlated
        with f. **Void rule:** the tier-2 claim is void unless the
        FD-residualised statistic also passes control (a) in full. With
        10 windows a within-subject regression is crude and can
        over-remove, so the same residualised analysis at W = 30 (19
        windows) is reported as a check but does not decide.
      - A claim that survives (a) and (b) is reported as "synergy tracks
        intensity across the decay above what time and motion predict",
        never as "synergy tracks intensity"; a claim voided by either is
        reported at tier 3 with the control result stated.
    - **Outcome of the first full non-stationary run (2,000 runs, 12 Sep
      2026, git e01c836-dirty; tables `results/bias_check_nonstat*.csv`).**
      - **Verdict: UNDETERMINED under the pre-registered rule.** All four
        deciding cells pass nominally, but every analytic S interval
        straddles 0.80, so no tier is assigned and the 20,000-run repeat
        was started the same day (`--n-runs 20000 --out
        results/nonstat_n20000`, ≈ 2 h). Deciding cells (W = 60):

        | condition | M | S_boot | S_analytic [interval] | R [range] |
        |---|---|---|---|---|
        | decay_coupling | 1,338 | 0.808 | 0.807 [0.677, 0.936] | 0.975 [0.939, 0.988] |
        | decay_coupling | 742 | 0.806 | 0.808 [0.651, 0.924] | 0.970 [0.915, 1.000] |
        | decay_noisecorr | 1,338 | 0.850 | 0.848 [0.493, 0.977] | 0.967 [0.903, 1.000] |
        | decay_noisecorr | 742 | 0.811 | 0.812 [0.493, 0.960] | 0.953 [0.867, 1.000] |

        W = 30 (report only): S 0.55–0.73, R 0.79–0.95. Bootstrap and
        analytic S agree to 0.002 in every deciding cell, so the trust
        rule was not triggered; the interval width is the centring
        problem the rule anticipated. **Tier 2 passes in every deciding
        cell** (R 0.953–0.975, lower bounds 0.867–0.939). **M = 151
        (reported, not deciding) at W = 60: tier 1 fails in both decay
        conditions (S_analytic 0.740 [0.583, 0.857] coupling, 0.687
        [0.494, 0.839] noise-corr) and tier 2 passes in both (R 0.934
        [0.830, 0.988], 0.892 [0.733, 0.988]).** At W = 30, M = 151
        fails tier 2 for noise-corr (R 0.563) and passes for coupling
        (0.826); M = 742 noise-corr also fails tier 2 at W = 30
        (R 0.789). Full table: `results/bias_check_nonstat_criterion.csv`.
      - **Noise-floor prediction: half right.** Early-decay pairs are
        correctly signed with P ≥ 0.95 as predicted. The late pairs are
        not near chance through noise: **two pairs per condition are
        wrong in expectation**, with the 2,000-run mean difference on the
        wrong side of zero and 3–5 SE from the truth (coupling W = 60:
        windows 11→12, true +0.0066, estimated −0.0032; 13→14, true
        +0.0021, estimated −0.0020; noise-corr 13→14, true +0.0015,
        estimated −0.0020). Pooling cannot fix these. The prediction
        assumed a constant bias across the decay; it is not.
      - **Mechanism, from the per-window tables and the analytic
        candidates.** The per-window sts bias is a function of f: ≈ 0
        mid-decay (f 0.3–0.6), −0.006 to −0.008 nats near the peak, and
        −0.02 to −0.035 as f → 0 and the regime returns to baseline
        (whose stationary W = 30 bias is −0.035). This is the
        cross-condition sign change already recorded, now seen as a
        continuous curve: the estimate rises from 0.032 to 0.059 across
        the decay while the truth rises from 0.038 to 0.088, so the late
        decay is flattened in expectation. On top of that, **the MMI
        candidates for R_abty (min of I_yta, I_ytb) cross during the
        decay**: their analytic gap falls to 0.0005 at f = 0.26 (coupling,
        bin 19) and 0.0008 at f = 0.40 (noise-corr, bin 17). At the
        crossing the min-selection is a coin flip and its winner's-curse
        bias is largest; the analytic truth also has a kink there, so the
        crossing bin carries the largest true step of the decay while the
        estimate points the wrong way (W = 30 coupling 19→20: true
        +0.0065, estimated −0.0032). **A candidate crossing inside the
        decay is a hard limit on adjacent-pair resolution that no pooling
        removes.** Whether real region pairs cross during the DMT decay
        is unknown and pair-specific; a whole-brain mean over 6,555
        heterogeneous pairs would spread any crossings over different f
        values rather than concentrate one at a single bin as this
        single-pair simulation does. That cuts both ways and is a
        limitation of the simulation design, recorded here for the
        writeup, not a reason to change the criterion.
      - **Step conditions.** Recovered step (post minus pre, share of
        true): W = 30 49 % (coupling) / 30 % (noise-corr); W = 60 87 % /
        67 %, consistent with the stationary shrinkage. **Global fit
        smears exactly as predicted by construction**: it lands on the
        analytic sts of the mixture covariance to within 0.0003 for both
        steps (0.0461 vs 0.0463; 0.0459 vs 0.0457) and within 0.002–0.0045
        for the decays, i.e. between the regimes (0.094 / 0.038) and
        below the sample-weighted mean of the bin truths. Its SD across
        runs is 0.011–0.022, so a single global value has no information
        about when the change happened.
      - **Prediction for the repeat, recorded before it finished.** The
        analytic per-pair intervals will narrow by √10, the wrong-in-
        expectation pairs will settle near or below P = 0.5, and S_analytic
        for the coupling condition at W = 60 is expected to fall toward
        (7 + 2·P_flip)/9 with P_flip ≤ 0.5, i.e. **≤ 0.89 and plausibly
        below 0.80**; noise-corr has one such pair and is expected to
        stay ≥ 0.80. Tier 1 requires both, so the expected outcome is
        **tier 1 FAIL, tier 2 PASS (R 0.95–0.98 with lower bounds ≥ 0.87)
        → outcome tier 2**. If the repeat still straddles, the rule does
        not provide a further repeat; the verdict is then recorded as
        undetermined at tier 1 and tier 2 is used, with that stated.
      - **Decision on a still-straddling repeat, fixed 12 Sep 2026 before
        any 20,000-run non-stationary output existed.** The repeat was
        launched at 21:22 (`python3 -u scripts/02_bias_check.py --n-runs
        20000 --out results/nonstat_n20000`); at the time of this entry it
        had written only its stationary tables (`bias_check.csv`,
        `bias_check_differential.csv` in that directory) and had not
        reached the non-stationary section, so nothing below is informed
        by it. The 20,000-run job narrows the analytic S intervals by
        about √10, which may not resolve an estimate this close to the
        threshold (2,000-run point estimates 0.807–0.848 against 0.80).
        **Rule: if any deciding cell (W = 60, M = 1,338 or 742, either
        decay condition) still has an analytic S interval straddling 0.80
        after 20,000 runs, tier 2 is the assigned tier.** Tier 1 is then
        reported as *marginal*, with its point estimate and interval in
        every deciding cell and the M = 151 result alongside (which
        fails tier 1 and passes tier 2 at 2,000 runs, see above). No
        further repeat is run. **Rationale:** that is the truthful
        description of the evidence, and "synergy correlates with
        intensity across the decay; successive windows cannot be
        resolved at this pooling" is a more defensible claim than a
        marginal tier-1 pass whose interval includes chance-adjacent
        values. If the repeat resolves cleanly in either direction (all
        four deciding intervals on one side of 0.80), the pre-registered
        tiers apply as written and this rule is moot.

- **Robustness C (placebo-fitted model)**: fit the Gaussian on a subject's
  placebo data, then evaluate local atoms on **both** of that subject's runs
  under that one model (`FIT_MODE="placebo"`). Controls for the concern that
  "synergy rises under DMT" might reduce to "the covariance structure
  shifts", which the global fit absorbs. Evaluating on DMT alone would leave
  no baseline to compare against.

  **Correction, made before any variant-C results existed.** The obvious
  version of this design — fit on a subject's *full* placebo run, score both
  runs under it — is biased. Placebo is then in-sample and DMT out-of-sample.
  Local entropy is a negative log-likelihood and cross-entropy is bounded
  below by entropy, so held-out data scores systematically higher regardless
  of any drug effect. The atoms are sums and differences of local entropies,
  so the bias may partially cancel, but this cannot be assumed.
  **Corrected design**: split each subject's placebo run in half, fit the
  Gaussian on the first half, and evaluate local atoms on the held-out
  placebo half and on the full DMT run. Both are then out-of-sample and the
  comparison is symmetric. This halves the data available for the fit, which
  is a cost to be reported.

- **Region exclusion: region 20 (0-based) dropped for all subjects and both
  conditions → 115 regions, 6,555 pairs.** Recorded 12 Sep 2026, before any
  115-region result existed.
  - **Defect.** Subject index 7 (subject 8), DMT run, region 20 is exactly
    constant (840 zeros) in every preprocessing variant *including raw `ts`*,
    so the defect is upstream in the source data, not introduced by
    preprocessing. The same subject's PCB run has full signal in that region.
    No other region in any subject/condition/variant is zero-variance or
    region-specifically non-finite (`01_synergy_timecourse.py` QC block).
    Region 20 is Yeo network 3 (dorsal attention), left hemisphere
    (`sch116_to_yeo.csv`; LH cortical parcels are indices 0–49).
  - **Why global, not per-subject.** Dropping the region only for subject 8
    DMT would make that subject's DMT synergy an average over a different
    pair set than their own PCB synergy, contaminating the within-subject
    contrast with a pair-set difference; with N=14 that moves the group mean.
    Dropping the region for everyone costs 115 of 6,670 pairs (1.7%) and
    keeps every comparison symmetric.
  - **Undocumented in the source papers.** Neither Timmermann et al. 2023
    (PNAS; n=16, 112-region Schaefer+AAL parcellation) nor Singleton et al.
    2025 (Commun Biol; n=14, Schaefer-116, "all 116 parcels") mentions
    excluded parcels, coverage dropout, or missing regional data — both
    report only motion-based *subject* exclusion (searched full texts via
    Europe PMC, PMC10068756 and PMC12008288, 12 Sep 2026). The original
    MATLAB (`external/DMT_NCT/scripts/*.m`) uses `nanmean` throughout, which
    would silently absorb a NaN produced from this region, but we have not
    verified that this is what happened. Worth one line in the writeup as a
    data-quality note; not a criticism of either paper.

- **Robustness A result, 115 regions (recorded 13 Sep 2026; ts_gsr,
  global fit, 6,555 pairs, git 18ad8b4;
  `results/synergy_bins_115regions-all_ts_gsr_global.csv`).** Whole-brain
  mean sts per 30-TR bin, averaged over the 14 subjects:

  | window | DMT | PCB |
  |---|---|---|
  | pre-injection, bins 1–8 | 1.308 | 1.289 |
  | peak intensity, bins 9–14 | 1.228 | 1.284 |
  | within-condition change | −0.080 | −0.005 |

  Difference-in-differences −0.075 nats, ≈ 6 % of baseline. The DMT
  minimum is ≈ 1.20 at bins 11–13, one to three bins after the mean
  intensity peak at bin 10; DMT recovers to 1.34 by bins 27–28. PCB is
  flat (range 1.23–1.35) apart from a single-bin dip at bin 10 (1.232),
  coinciding with injection and recovered by bin 11; the DMT dip spans
  ≈ 10 bins. **The direction is a DECREASE in synergy under DMT, opposite
  to the stated hypothesis**, consistent with the earlier 20-region
  observation and no longer attributable to one contiguous block of
  cortex. This is a global-fit result (local values under one stationary
  Gaussian fitted to the full run) and is descriptive only: no null, no
  motion control, one preprocessing variant. It changes nothing about
  Primary B or its criteria.
  - **Pre-registered handling of a directional failure (recorded 13 Sep
    2026, before any Primary B result).** The hypothesis is directional
    (synergy is *up*-regulated under DMT). Primary B tests the sign. A
    significant decrease **refutes the stated hypothesis and is reported
    as a refutation**; it does not become a confirmation by reframing the
    hypothesis after the fact (e.g. as "synergy changes under DMT" or
    "synergy tracks intensity in either direction"). The tracking
    statistics under Primary B (tiers 1–3, controls (a) and (b)) are
    sign-agnostic by construction and are still run and reported, but a
    negative tracking result is reported as tracking in the direction
    opposite to the pre-registered one. The observation above comes from
    Robustness A and does not pre-empt Primary B: a global-fit decrease
    could still be a windowed null, or vice versa.
  - **Pre-registered secondary prediction on redundancy (recorded 13 Sep
    2026, BEFORE rtr was examined in any run).** Timmermann et al. 2023
    report increased global functional connectivity under DMT. Higher
    pairwise correlation implies more redundant information between
    regions, so under a redundancy-dominance reading of the sts decrease
    above, **rtr should increase under DMT while sts decreases, with a
    mirrored time course** (rtr peak where sts troughs, bins ≈ 10–14;
    return toward baseline by bins 27–28; placebo flat). **If rtr does
    not increase, the redundancy-dominance interpretation is
    unsupported** and the sts decrease is reported without it. Status:
    **rtr has not been examined to date** — every result so far
    (`synergy_bins_20regions_*`, `synergy_bins_115regions-all_*`) saved
    sts alone. To make this testable from the same computation,
    `01_synergy_timecourse.py` now saves all 16 atoms per bin, shape
    (14, 2, 28, 16) in phyid order (rtr … sts, names in the CSV header,
    outputs `atoms_bins_<tag>.npy/.csv`), so rtr and sts come from one
    run. **Rerun done 13 Sep 2026** (git 18ad8b4-dirty: script and
    CLAUDE.md edits uncommitted at run time; 6,555 pairs, 14 × 2 runs,
    ≈ 530 s): `results/atoms_bins_115regions-all_ts_gsr_global.npy/.csv`.
    Its sts column matches `synergy_bins_115regions-all_ts_gsr_global.npy`
    to 7e-16, so the sts-only file is superseded, not contradicted.
    **The rtr column of that file has not been read as of this entry**;
    the prediction above was written and this rerun completed before
    anyone opened it. The rtr prediction is assessed on Robustness A
    first (descriptive, same caveats as above) and then under Primary B
    with the same nulls and controls as sts.

## Open questions to resolve

- Confirm reuse licence with Singleton / Timmermann before publishing.
- ~~Decide sliding-window length for time-resolved ΦID~~ — **resolved**:
  30 TRs / 60 s, non-overlapping. See Primary B above for the justification.
- ~~Quantify the finite-sample entropy bias directly~~ — **done 12 Sep
  2026** (`scripts/02_bias_check.py`, symmetric and asymmetric VAR(1)
  families, 30/60/840-TR windows). Outcome, decision tree and a prediction
  for the tree's outcome are recorded under Primary B. Next steps, both
  before any windowed real-data run: the tree's step 1–2 (analytic
  log-det correction, validated on the same script) and the
  pre-registered non-stationary conditions (step and intensity-shaped
  decay, both shift types, tracking criterion; parameters fixed under
  Primary B). **Status 12 Sep 2026: implemented in `02_bias_check.py`
  (`run_nonstat`), smoke-tested only with `--quick --out <scratch dir>`,
  which cannot write to `results/`. First full run started 12 Sep 2026
  after the criterion, M values, noise-floor prediction and intermediate
  fallback were recorded; stopped before its non-stationary section to
  add the analytic correct-sign probability, the undetermined rule and
  the tier-2 controls; restarted the same day from the final script and
  completed (verdict UNDETERMINED by the pre-registered rule; 20,000-run
  repeat started; outcome recorded under the tier-2 controls bullet).**
  A consequence
  of the pre-registered parameters, visible from the analytic truths
  alone and not a result: in the decay conditions the true sts drops at
  onset and then *rises* back toward baseline as the shifted parameter
  relaxes, so "tracking" in the simulation means following that
  piecewise truth in whichever direction it moves, and adjacent decay
  bins differ in true sts by ~0.001–0.006 nats.
- **The bias check has no sts-matched null.** Every simulated pair differs
  in true sts, so "sign is preserved" was observed only where a true effect
  exists. A pair of conditions with equal analytic sts but different
  covariance (e.g. different rtr) would test whether condition-dependent
  bias can manufacture an sts difference from nothing. Add such a pair to
  `02_bias_check.py`, parameters fixed before the run, before interpreting
  any windowed DMT-vs-PCB contrast.
- Decide whether whole-brain synergy is summarised as mean over all pairs or
  restricted to a defined subnetwork — pre-register the choice.
  `REGION_SELECTION` in `01_synergy_timecourse.py` is the knob; `"all"`
  (mean over all pairs; 6,555 after the region-20 exclusion) is the
  current default and the only one used for a reported result so far.
  Constraint from the bias check: at W = 30 the per-pair-window SNR is
  ≈ 1, so any windowed summary must average over many pairs; regional or
  edge-level maps are only viable at the global fit.
- Whether to email Stamatakis to collision-check before or after first results.
