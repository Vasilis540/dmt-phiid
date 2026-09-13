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
    - **Step 2 EXECUTED 13 Sep 2026 (`scripts/04_logdet_correction_check.py`,
      `results/logdet_correction_check.csv`; applied post hoc to the
      2,000-run tables at commit 18ad8b4 via `git show`, since the
      working-tree tables were being overwritten by the 20,000-run job;
      no real data touched).** The correction is a per-(k, N) constant per
      entropy term, so each MI shifts by a constant fixed by the
      dimensions of its two argument sets, every MMI candidate set
      compares MIs of identical dimensions (checked against the candidate
      list), and each window-mean atom shifts by a fixed constant per
      (atom, N) obtained by pushing the MI constants through phyid's own
      lattice inverse. **Constants (nats, added to the plug-in estimate):**
      sts −0.02040 / −0.00917 / −0.00060 at N = 29 / 59 / 839, **equal to
      the recorded prediction −0.5·[ψ((N−3)/2) − ψ((N−4)/2)] to 1e-12**;
      rtr −0.01886 / −0.00885 / −0.00060; rts and str −0.01960 / −0.00901
      / −0.00060; **the other twelve atoms shift by exactly zero.**
      **Differential bias changes by exactly zero**: max |change| over all
      24 differential rows 1e-6, which is the tables' 6-decimal rounding
      (1e-17 when computed from unrounded values). **Empirical check of
      the derivation, not just the algebra:** the correction implemented
      *inside* the estimator (entropy terms corrected before MI, MMI
      selection and the lattice solve) on 3,000 freshly simulated VAR(1)
      windows (500 each: baseline, asym_baseline, asym_shift_coupling at
      W = 30 and 60) changed **no selection in any window** and the
      per-window (corrected − plug-in) equalled the analytic constant to
      6e-16 for all 16 atoms. **The derivation stands.** Criterion at
      W = 30, sts, corrected: clause 1 |bias| / analytic = 50–80 % in all
      six conditions (the correction *worsens* the per-condition bias
      because the dominant plug-in bias is the negative autocorrelation
      component and the iid correction is also negative); clause 2
      |differential bias| / true difference = 52–77 %, unchanged. **Both
      clauses FAIL as predicted → Primary B = W = 60, uncorrected, the
      fallback branch, carrying the 15–45 % shrinkage as a stated cost.**
      The W = 60 constant in `01_synergy_timecourse.py` now rests on an
      executed step 3, not on the prediction alone.
    - ~~Not yet decided; decide and record before the first real windowed
      run: what replaces the 60-TR window-length robustness check if the
      fallback branch is taken (candidates: W = 120, four rating bins per
      window, 7 windows; or the global fit A alone).~~ **Resolved 13 Sep
      2026, before any real windowed run, after step 2 put Primary B at
      W = 60.** The robustness check is **W = 30 (28 windows, one per
      rating bin, stride 30) run as a positive control for the shrinkage
      model**, plus Robustness A (the global fit). **W = 120 is not
      run.** Prediction for W = 30 on real data: **the same sign as
      W = 60 and a smaller magnitude**, with the W = 30 / W = 60 ratio
      of the whole-brain DMT-minus-PCB sts contrast consistent with the
      measured absorption, roughly 52–77 % absorbed at W = 30 against
      15–45 % at W = 60 (asymmetric family 52–66 % vs 15–31 %), i.e. the
      W = 30 contrast is expected at about one-third to two-thirds of
      the W = 60 contrast. A W = 30 result with the opposite sign, or
      larger than W = 60, is inconsistent with the shrinkage model and
      is reported as such; it does not change the W = 60 result's
      status. The 30-TR windows use the same code path
      (`01_synergy_timecourse.py --fit-mode window --window-trs 30`,
      output `atoms_win30_<tag>`), with bins 10–28 / 11–28 as the
      sensitivity / primary decay sets. Nothing at W = 30 is read at
      the regional or edge level (SNR ≈ 1 per pair-window).
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
      - **Sign handling on real data (fixed 13 Sep 2026, before any real
        windowed run).** The pre-registered direction is positive: the
        hypothesis is that synergy is up-regulated, so ρ_S between
        window-mean sts and intensity is predicted > 0. On real data
        **tracking is assessed on |ρ_S| ≥ 0.80** (the per-subject
        statistic, group-tested against the phase-randomised null), and
        **the sign is reported separately against the pre-registered
        direction**. A strong negative correlation is tracking in the
        opposite direction, reported as a refutation of the directional
        hypothesis (see the directional-failure rule below), **not as a
        failed tracking criterion**. Controls (a) and (b) apply to the
        magnitude whichever sign it carries. Motivation on record: the
        115-region global fit shows a synergy *decrease* under DMT, so
        a sign-blind criterion could otherwise be gamed either way; fixing
        it now removes that freedom. Mirrored in
        `01_synergy_timecourse.py` (`TIER2_ABS_RHO`, `PREREG_DIRECTION`).
      - **Direct evidence that bins 8–10 are onset-contaminated
        (recorded 13 Sep 2026, from the ts_demean global fit).** On the
        no-GSR data the whole-brain rtr shows a bump at bins 8–9 **in
        placebo** (0.042, 0.049 against a 0.028 baseline), the same
        bins in which DMT rtr peaks (0.072 at bin 9). Placebo has no
        drug, so the no-GSR data carry an injection response that is
        independent of drug (the injection itself, and whatever
        co-occurs with it: motion, arousal, the global signal that GSR
        would have removed). The sts series shows the matching
        single-bin placebo dip at bin 10 on ts_gsr. **This supports the
        decay-phase-only design**: any DMT-vs-PCB contrast that
        includes bins 8–10 mixes a drug effect with an injection event
        present in both arms, and the tier-2 decay windows (W = 60:
        windows 5–14, i.e. bins 9–28; W = 30: bins 10–28) should be
        read with the first decay window treated as onset-adjacent.
        Whether to start the decay at window 6 (bin 11) at W = 60 is a
        choice to fix before the first real windowed run; the
        pre-registered windows stand until then.
      - **Decay windows on real data, FIXED 13 Sep 2026 before any real
        windowed run and before the 20,000-run verdict.** **Real-data
        primary at W = 60: windows 6–14 (bins 11–28)**, excluding
        window 5 (bins 9–10) on the placebo onset response at bins 8–10,
        which came from Robustness A (global fit) and not from any
        windowed result. **Windows 5–14 are reported as the
        sensitivity.** At W = 30 the corresponding sets are bins 11–28
        (primary) and 10–28 (sensitivity). Mirrored in
        `01_synergy_timecourse.py` (`DECAY_WINDOWS_PRIMARY`,
        `DECAY_WINDOWS_SENSITIVITY`). **The tier is assigned from the
        20,000-run bias check on the pre-registered windows 5–14 and
        does not move.** When the 20,000-run tracking table lands, S and
        R are recomputed on windows 6–14 from it as a check that the
        tier survives the exclusion: `python3
        scripts/05_tier_check_decay_windows.py --tables-dir results`
        (S_analytic = mean per-pair analytic correct-sign probability
        over the 8 remaining pairs with its interval; R from the
        per-window pooled means with a parametric interval,
        N(est_mean, est_sd/√M) per window, 2,000 draws — the analytic
        counterpart of the bootstrap R, since the per-run arrays are not
        saved). **Dry run on the 2,000-run tables at 18ad8b4
        (`results/tier_check_decay_windows_n2000_18ad8b4.csv`; a check
        of the script, not the check itself):** the script reproduces
        the criterion table's S_analytic and intervals exactly on
        windows 5–14, and its parametric R lower bounds coincide with
        the bootstrap ones to three decimals. On windows 6–14, W = 60:
        coupling S_analytic 0.788 [0.695, 0.928] at M = 1,338 and 0.797
        [0.667, 0.916] at M = 742 (below 0.80, still straddling; pair
        5→6 was one of the best-signed pairs, P ≈ 0.98), noise-corr
        0.834 [0.486, 0.974] and 0.801 [0.487, 0.956]; **R 0.967–0.983
        in all four cells, lower bounds 0.82–0.92, tier 2 unaffected.**
        Consistent with the recorded expectation that tier 1 fails on
        the repeat. If the 20,000-run check moves the assigned tier's
        statistic below 0.80 on windows 6–14, the tier still stands as
        assigned and the primary real-data analysis is reported with
        that simulation result stated next to it.
      - **Tier-disagreement rule (fixed 13 Sep 2026, before any
        20,000-run table existed).** The tier assigned on the
        pre-registered windows 5–14 and the tier supported by the 6–14
        check can disagree. **The tier claimed on the real-data primary
        windows (6–14) is the LOWER of the two.** A higher tier on 5–14
        is reported as the sensitivity result, with the note that it
        includes the onset-adjacent window (bins 9–10) and is therefore
        weaker evidence. The 5–14 assignment itself is not revised: it
        stays on record as what the pre-registered criterion produced.
        The 2,000-run dry run already shows coupling tier 1 at
        0.79–0.80 on 6–14 (S_analytic 0.788 and 0.797, both straddling
        0.80), so under this rule a tier-1 assignment on 5–14 would not
        carry to the primary windows unless the 20,000-run check clears
        0.80 there in both decay conditions at both M.
      - **Primary step contrast at W = 60: inferential test (pre-registered
        13 Sep 2026, before any real windowed run).** The step contrast
        had no test on record. **Statistic, per subject:** (post − pre)
        on DMT minus (post − pre) on PCB, on the whole-brain mean sts
        from the windowed estimator, with **pre = windows 1–4** (bins
        1–8) and **post = windows 6–14 primary** (bins 11–28), **5–14
        sensitivity**. **Test:** exact sign-flip permutation across the
        14 subjects, all 2^14 = 16,384 assignments enumerated,
        two-sided p = fraction of assignments with |mean DiD| ≥ the
        observed |mean DiD|. **Effect size:** mean DiD with a
        subject-bootstrap 95 % CI, 10,000 draws, seed 20261120, in nats
        and as a share of the pre-injection DMT mean. **Second null
        (rule 2):** the phase-randomised temporal null for the same
        statistic, 1,000 surrogates. Surrogates are generated per
        subject and condition by phase-randomising the whole-brain
        mean sts local-value series at TR resolution (the concatenated
        per-window local atoms, each window's values under its own
        fit), then re-averaging into the same windows and recomputing
        the DiD; two-sided p = fraction of surrogates with |DiD| ≥
        observed. Randomising the 14-point window series instead was
        considered and rejected because 14 points give too coarse a
        phase spectrum; the TR-resolution version treats the
        concatenated local series as one process without window-locked
        structure, which is exactly the null being tested. **The
        directional-failure rule applies: a significant negative DiD is
        a refutation of the up-regulation hypothesis, reported as
        such.** Both preprocessing variants (rule 6), FDR not required
        (one whole-brain statistic per variant and window set; the
        primary/sensitivity and gsr/demean versions are reported
        together, not selected among).
      - **Primary step contrast at W = 60: motion handling (rule 4;
        pre-registered 13 Sep 2026, before any real windowed run).**
        Framewise displacement is from `FDlong.mat` (`FDDMT`, `FDPCB`,
        each (840 TRs, 14 subjects)). **Report window-mean FD per
        condition** (14 windows × 2 conditions, group mean with subject
        SD, and the pre/post FD contrast with the same DiD form as the
        synergy statistic). **Recompute the DiD on FD-residualised
        sts**: within each subject and condition, regress window-mean
        sts on window-mean FD across all 14 windows (ordinary least
        squares, intercept included, one slope per subject × condition;
        linear, per subject) and take the residuals; then form the
        same pre/post DiD from the residuals and run the same sign-flip
        test and bootstrap CI. **Report raw and residualised side by
        side.** **"Survives motion control" means the residualised DiD
        has the same sign as the raw DiD and its bootstrap 95 % CI
        excludes zero.** Any other outcome is reported as "does not
        survive motion control", with both estimates shown; it is not
        rescued by a different residualisation. A 14-window
        within-subject regression is crude and can over-remove signal
        when FD and drug effect share a time course, which they do at
        onset; this is a cost of the design and is stated with the
        result, and it is one reason the primary post window starts at
        window 6.
      - **Tier-2 threshold: corrected rule (13 Sep 2026, before any real
        windowed result; the Primary B ts_gsr W = 60 run was in progress
        and unread).** The pre-registration applied |ρ_S| ≥ 0.80 to "the
        per-subject statistic", but the simulation validated R on the
        pooled window means, which is the group-mean-series version;
        per-subject ρ over 9 windows was never simulated, and averaging
        noisy per-subject correlations attenuates (the LZ check showed
        it: −0.24 per-subject mean against −0.83 group-mean series on the
        same data). **Corrected rule:** |ρ_S| ≥ 0.80 applies to the
        group-mean-series ρ (14-subject mean sts over the decay windows
        vs the template f). The per-subject mean ρ (own ratings primary,
        template sensitivity) is tested for existence against the
        phase-randomised null with its subject-bootstrap CI and is **not**
        thresholded. **A tier-2 claim requires the group-mean-series
        threshold pass AND the per-subject mean significant against the
        null in the same direction AND controls (a) and (b) as written**,
        with (b) meaning that the same three conditions hold on the
        FD-residualised sts. Implemented in `06_primary_b_analysis.py`
        (`TIER2_DECIDES = "groupmean_series"`).
      - **Residualisation domains (confirmed 13 Sep 2026).** Section A's
        DiD spans all 14 windows, so its FD residualisation regresses over
        all 14 windows per subject and condition; control (b) protects
        decay-window tracking, so it regresses over the decay windows
        only. Each regression covers the domain of the analysis it
        protects. The asymmetry is intended.
      - **Disclosed pre-run observation (13 Sep 2026).** While exercising
        `06_primary_b_analysis.py` on random arrays in the scratchpad
        (no windowed sts involved), the script read the real FD and
        rating files, so one real-data number was seen: window-mean
        framewise displacement on the DMT run correlates with the
        intensity template over the decay windows at ρ_S ≈ 0.4–0.5
        (group mean of per-subject Spearman, W = 60). It touches no
        pre-registered decision and no synergy value; it is recorded so
        the sequence is complete. It does foreshadow that control (b)
        will remove template-shaped variance.
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
      - **Provenance of the bias-check tables (recorded 13 Sep 2026).**
        The 20,000-run repeat that is actually running was launched on
        13 Sep 2026 at 10:06 as `python3 -u scripts/02_bias_check.py
        --n-runs 20000` **without `--out`**, so it writes every
        `results/bias_check*.csv` in place (stationary tables first,
        the four `bias_check_nonstat*` tables when it finishes); the
        12 Sep launch into `results/nonstat_n20000/` did not complete
        and that directory holds only its stationary tables. **The
        2,000-run tables and the UNDETERMINED verdict above are read
        from commit 18ad8b4** (`git show 18ad8b4:results/bias_check.csv`
        etc.); commit 33f0b33 already carries the 20,000-run stationary
        tables captured mid-run. Once the job finishes, the working
        tree holds the 20,000-run versions of all six tables and the
        verdict recorded from them must cite that commit.
      - **VERDICT of the 20,000-run repeat (finished 13 Sep 2026 12:06
        after 7,182 s; every table header reads `git=18ad8b4`, i.e. the
        committed script ran unchanged; tables in `results/`, committed
        with this entry).** Deciding cells, W = 60:

        | condition | M | S_analytic [interval] | S_boot | R [range] |
        |---|---|---|---|---|
        | decay_coupling | 1,338 | **0.923** [0.851, 0.966] | 0.924 | 0.990 [0.964, 1.000] |
        | decay_coupling | 742 | **0.887** [0.821, 0.935] | 0.890 | 0.984 [0.939, 1.000] |
        | decay_noisecorr | 1,338 | **0.861** [0.763, 0.931] | 0.866 | 0.976 [0.927, 1.000] |
        | decay_noisecorr | 742 | **0.823** [0.735, 0.892] | 0.826 | 0.964 [0.903, 1.000] |

        **Tier 1: all four point estimates pass, but both
        noise-correlation intervals straddle 0.80. Per the
        pre-registered escalation rule, TIER 2 IS THE ASSIGNED TIER on
        windows 5–14; tier 1 is reported as marginal** with the
        intervals above and the M = 151 result (tier 1 fails in every
        cell: S_analytic 0.760 [0.710, 0.806] coupling, 0.695 [0.637,
        0.749] noise-corr). **Tier 2 passes cleanly at W = 60** in all
        four deciding cells (R 0.964–0.990, bootstrap lower bounds
        0.903–0.964; the parametric lower bounds from
        `05_tier_check_decay_windows.py` on the same windows are
        0.891–0.964). Bootstrap and analytic S agree to 0.005 in every
        cell. M / N_RUNS is now 0.07 and 0.04, so the centring caveat
        is largely resolved. W = 30 (report only): tier 1 fails
        everywhere (S 0.59–0.71), tier 2 passes at M = 1,338 and 742
        (R 0.88–0.96) and fails at M = 151 for noise-corr (0.68).
        **The prediction recorded before the repeat was wrong**: it
        expected coupling S_analytic ≤ 0.89 and plausibly < 0.80 with
        two pairs wrong in expectation; at 20,000 runs every decay pair
        in both conditions has the correct sign in expectation
        (coupling 11→12 P = 0.84, 13→14 P = 0.69; noise-corr 12→13
        P = 0.62, 13→14 P = 0.60), and coupling S rose to 0.923. The
        2,000-run "wrong in expectation" reading was sampling error on
        the sample-mean differences, not a bias, and the late-decay
        pairs are low-P rather than reversed. The candidate-crossing
        mechanism recorded from the 2,000-run tables is still a
        property of the analytic truths, but its claimed effect on the
        estimate was not confirmed.
      - **6–14 check (`05_tier_check_decay_windows.py --tables-dir
        results`, `results/tier_check_decay_windows.csv`, git b7e4595).**
        **Tier 2 R passes cleanly on 6–14** in all four deciding cells
        (point 1.000, parametric lower bounds 0.950 / 0.933 coupling,
        0.900 / 0.850 noise-corr at M = 1,338 / 742). Tier 1 S on 6–14
        is marginally *higher* than on 5–14 (0.925 / 0.894 coupling,
        0.874 / 0.839 noise-corr), **reversing the 2,000-run dry run**,
        which was noise (pair 5→6 is now P = 0.91 / 0.76, no longer a
        best pair); noise-corr still straddles 0.80 ([0.785, 0.936],
        [0.757, 0.901]). **Tier-disagreement rule: both window sets give
        tier 2, so TIER 2 IS THE CLAIMED TIER ON THE PRIMARY WINDOWS
        6–14.** **M = 151 limitation:** at M = 151 tier 2 straddles in
        some cells (5–14: noise-corr R 0.904 [0.769, 0.988]; 6–14
        parametric lower bounds 0.783 coupling, 0.683 noise-corr), so
        **if the true effective N is nearer one unit per component
        than one per pair, the full-decay claim is marginal**; this is
        stated wherever tier 2 is claimed.

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

- **Implementation status of Primary B (window) and Robustness C
  (placebo) — code exists, smoke-tested, NOT run on real data (recorded
  13 Sep 2026).** `01_synergy_timecourse.py --fit-mode window|placebo`.
  - **Window mode**: `WINDOW_TRS = WINDOW_STRIDE = 60`, 14 non-overlapping
    windows, each an independent `calc_PhiID` call on that window's
    samples alone (covariance, mean and MMI selections all per window,
    matching what `02_bias_check.py` simulates; no sample straddles a
    boundary). Output `atoms_win60_<tag>.npy`, shape (14, 2, 14, 16).
    W = 60 is the decision tree's fallback branch; it was set on the
    13 Sep 2026 instruction and the recorded prediction that the W = 30
    criterion fails on its differential-bias clause. This file does not
    record a completed step-2 validation of the analytic log-det
    correction, so the branch rests on the prediction and the
    instruction, not on a recorded step-3 evaluation; if step 2 is run
    later and contradicts the prediction, that takes precedence.
  - **Placebo mode**: per subject and pair, mean and covariance of the
    four-vector fitted on PCB TRs 0–419, MMI selections fixed from that
    model's analytic Gaussian MIs, local atoms evaluated under that one
    model on PCB TRs 420–839 and on the full DMT run (both
    out-of-sample). Output `atoms_bins_<tag>_placebo.npy`, (14, 2, 28,
    16), PCB bins 0–13 NaN. The fixed-model code path reproduces
    `calc_PhiID` to 1e-13 on real pairs when fit and evaluation data
    coincide.
  - **Smoke tests (6 contiguous regions, `REGION_SELECTION="first"`,
    scratch directory, never a reportable setting):** global mode is
    bit-identical to the pre-patch script; window mode matches an
    independent per-window recomputation to 3e-16, including the 59-TR
    final window of subject 2 PCB; placebo mode gives the expected NaN
    pattern. Observation from the placebo smoke, 6 regions only and not
    a result: the held-out PCB half scores *higher* sts under the
    placebo-fitted model than the same TRs under the native global fit
    (1.49 vs 1.28), i.e. the out-of-sample inflation the corrected
    design anticipated is real even placebo-on-placebo, which is why
    both arms must be out-of-sample.
  - **No real windowed or placebo-fitted result will be produced until
    the 20,000-run bias check assigns a tier** (see "Decision on a
    still-straddling repeat"). The remaining pre-run decisions listed
    under Primary B (what replaces the 60-TR robustness check on the
    fallback branch; whether the decay starts at window 6) are still
    open.

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
  - **Outcome: rtr, total TDMI and per-atom change on the 115-region
    global fit (read 13 Sep 2026 from
    `results/atoms_bins_115regions-all_ts_gsr_global.npy`, after the
    prediction above was committed at 33f0b33).** Same status as the sts
    result: Robustness A, descriptive only, no null, no motion control,
    one preprocessing variant, 14-subject means of the whole-brain
    pair-mean. Values in nats.

    | quantity | window | DMT | PCB |
    |---|---|---|---|
    | rtr | pre-injection, bins 1–8 | 0.0248 | 0.0225 |
    | rtr | peak intensity, bins 9–14 | 0.0152 | 0.0221 |
    | rtr | within-condition change | −0.0096 | −0.0004 |
    | total (Σ 16 atoms = TDMI) | pre-injection, bins 1–8 | 1.442 | 1.405 |
    | total | peak intensity, bins 9–14 | 1.316 | 1.397 |
    | total | within-condition change | −0.126 | −0.008 |

    Difference-in-differences: rtr −0.0091 (37 % of the DMT baseline;
    per-subject DiD positive in 4 of 14), total −0.118 (8.1 % of the DMT
    baseline; per-subject DiD negative in 13 of 14). **sts per-subject
    DiD (recorded 13 Sep 2026): negative in 13 of 14** (mean −0.075,
    SD 0.077; the one positive subject is index 13, +0.13). Per-bin rtr means,
    bins 1–28: DMT 0.017 0.019 0.026 0.023 0.024 0.032 0.029 0.029 0.021
    0.013 0.013 0.015 0.016 0.013 0.016 0.014 0.017 0.017 0.017 0.023
    0.017 0.021 0.021 0.022 0.021 0.028 0.025 0.020; PCB 0.017 0.021
    0.017 0.025 0.026 0.025 0.025 0.023 0.021 0.019 0.023 0.027 0.023
    0.019 0.021 0.025 0.023 0.024 0.024 0.024 0.023 0.022 0.021 0.018
    0.021 0.022 0.021 0.021. Per-bin totals: DMT 1.432 1.366 1.433 1.457
    1.404 1.444 1.482 1.518 1.403 1.309 1.282 1.298 1.284 1.323 1.324
    1.320 1.324 1.342 1.346 1.382 1.359 1.374 1.370 1.391 1.405 1.416
    1.449 1.434; PCB 1.380 1.360 1.352 1.412 1.476 1.419 1.449 1.389
    1.381 1.342 1.416 1.449 1.406 1.385 1.420 1.474 1.444 1.429 1.446
    1.442 1.430 1.489 1.455 1.400 1.481 1.487 1.441 1.444.
    - **The rtr prediction does not hold.** rtr *falls* under DMT over
      the same window in which sts falls: the DMT-minus-PCB rtr
      difference is negative in every bin 10–19 (−0.006 to −0.013),
      the DMT rtr minimum (bins 10–11, 14) coincides with the sts trough
      rather than mirroring it, and the two time courses co-vary
      (Pearson r across the 28 bins: 0.66 between DMT rtr and DMT sts,
      0.68 between their per-bin DMT-minus-PCB differences). The
      pre-registered mirrored time course is absent. **The
      redundancy-dominance interpretation is therefore unsupported and
      the sts decrease is reported without it.** Under this estimator
      the whole-brain rtr is two orders of magnitude smaller than sts
      (0.02 vs 1.3 nats), so the "more correlation → more redundancy"
      step does not translate into the MMI rtr atom at the whole-brain
      mean; whether that reflects the MMI redundancy function or the
      Gaussian model is not resolved here.
    - **DMT reduces the total, it does not redistribute it.** The total
      TDMI falls by 0.118 nats (DiD), of which sts carries 0.075 (64 %),
      rtr 0.009 (8 %), and the within-region self-transfer atoms xtx
      and yty (lag-1 information a region carries about itself) 0.046
      and 0.037. No atom of consequence rises under DMT.
    - **Largest DMT-minus-PCB change in the peak window (|DiD|):** sts
      −0.075, xtx −0.046, yty −0.037, rts and str −0.035 each, xts, yts,
      stx and sty +0.032 each, rtr −0.009; the remaining six atoms
      (rtx, rty, xtr, xty, ytr, ytx) are within ±0.004. **Structural
      note for reading that list:** the whole-brain means obey lattice
      identities under MMI — xtr = rty, ytr = rtx, xty = −xtr,
      ytx = −ytr exactly, and rts ≈ str, xts ≈ yts ≈ stx ≈ sty ≈ −rts to
      three decimals — so the +0.032 changes are the mirror of the
      −0.035 in rts/str and cancel in the total. The independently
      moving atoms are sts, xtx, yty and rtr, all downward.
  - **Verdict on the pre-registered rtr prediction: FAILED (recorded
    13 Sep 2026).** rtr falls with sts (DiD −0.0091, 37 % of baseline),
    co-varies rather than mirrors (r = 0.66 across bins), positive DiD in
    only 4 of 14 subjects. The redundancy-dominance interpretation is
    unsupported on ts_gsr. Total TDMI: −0.118 DiD (8.1 %), dropping in
    13 of 14 subjects, sts carrying 64 %, xtx and yty most of the rest,
    rtr 8 %; a reduction of total information, not a redistribution.
  - **Pre-registered GSR confound and ts_demean prediction (recorded
    13 Sep 2026, before any computation on ts_demean).** Global signal
    regression removes the global component, which is where an increase
    in *global* functional connectivity (Timmermann et al. 2023) would
    live. The failed rtr prediction on ts_gsr therefore does not rule
    out the redundancy increase: GSR may have removed the very signal
    the prediction was about. **Prediction on ts_demean (no GSR):**
    (i) rtr rises under DMT (positive rtr DiD over bins 9–14 vs 1–8) if
    the Timmermann global-connectivity effect is real and GSR removed
    it; (ii) the sts decrease survives the variant change (negative sts
    DiD on ts_demean). Outcomes: both hold → the ts_gsr rtr failure is
    attributed to GSR and rtr is reported per variant; (i) fails on
    ts_demean too → the redundancy increase is unsupported in either
    stream and the interpretation is dropped; (ii) fails → the sts
    decrease is GSR-dependent and is reported as such under rule 6, not
    as a DMT effect. Run: 115-region global fit, all 16 atoms,
    `01_synergy_timecourse.py --variant ts_demean` (flag added for this
    purpose; default unchanged at ts_gsr), output
    `atoms_bins_115regions-all_ts_demean_global.*`. Same descriptive
    status as every Robustness A result.
    - **Outcome on ts_demean (run 13 Sep 2026, git 33f0b33-dirty; the
      uncommitted edits are the pre-registration text above, the
      `--variant` flag and `03_lz_vs_tdmi.py`;
      `results/atoms_bins_115regions-all_ts_demean_global.*`).** Values
      in nats, 14-subject means of the whole-brain pair-mean.

      | quantity | pre, bins 1–8 DMT / PCB | peak, bins 9–14 DMT / PCB | change DMT / PCB | DiD |
      |---|---|---|---|---|
      | rtr | 0.0301 / 0.0301 | 0.0452 / 0.0315 | +0.0151 / +0.0014 | **+0.0137** (46 % of baseline) |
      | sts | 1.240 / 1.224 | 1.152 / 1.216 | −0.089 / −0.008 | **−0.081** (6.5 %) |
      | total TDMI | 1.384 / 1.346 | 1.293 / 1.345 | −0.091 / −0.001 | **−0.090** (6.5 %) |

      **(ii) holds:** the sts decrease survives the variant change
      (DiD −0.081 on ts_demean vs −0.075 on ts_gsr; per-subject DiD
      positive in 3 of 14 vs 1 of 14). **(i) holds at the group mean
      only:** the rtr DiD flips sign from ts_gsr (−0.0091 → +0.0137)
      and the DMT-minus-PCB rtr difference is positive in every bin
      9–14 (+0.007 to +0.023), but the per-subject DiD is positive in
      **7 of 14** (SD 0.038, so the group mean rests on a few
      subjects), the DMT rtr maximum is the injection bin 9 (0.072)
      rather than the intensity peak, and **PCB shows the same
      injection-locked rtr bump at bins 8–9** (0.042, 0.049 against a
      0.028 baseline), so part of the DMT rise is an injection event
      present in both conditions. rtr and sts time courses are neither
      mirrored nor co-varying on this variant (r = 0.18 across bins;
      rtr max bin 9, sts min bin 13). Per the pre-registered outcome
      mapping this is the "both hold" branch: **the ts_gsr rtr failure
      is attributed to GSR and rtr is reported per variant**, with the
      three caveats just stated attached wherever it is reported and
      with the explicit statement that a 7-of-14 split is not a
      within-subject effect. The redundancy-dominance interpretation is
      therefore *not ruled out* on ts_demean; it is not supported
      either, since rtr does not mirror sts. **sts per-subject DiD:
      negative in 11 of 14** (mean −0.081, SD 0.127; positive: subject
      indices 0, 1, 13 at +0.07, +0.01, +0.18), against 13 of 14 on
      ts_gsr. Total TDMI again falls (2 of 14 subjects positive): sts −0.081, xtx −0.064, yty −0.048
      against rtr +0.014, so the reduction of total information is
      GSR-independent; ranked |DiD| in the peak window: sts, xtx, str /
      rts (−0.050), the four mirrored +0.048 atoms, yty, then rtr.
      Per-bin rtr, DMT: 0.026 0.027 0.029 0.031 0.031 0.035 0.031
      0.031 0.072 0.043 0.035 0.042 0.038 0.041 0.030 0.033 0.035 0.037
      0.026 0.045 0.041 0.037 0.038 0.056 0.036 0.048 0.045 0.037; PCB:
      0.029 0.029 0.025 0.029 0.032 0.027 0.028 0.042 0.049 0.023 0.028
      0.029 0.030 0.030 0.034 0.034 0.037 0.031 0.033 0.033 0.030 0.034
      0.034 0.024 0.027 0.029 0.028 0.037. Per-bin sts, DMT: 1.281
      1.192 1.221 1.299 1.216 1.221 1.246 1.247 1.316 1.171 1.136 1.109
      1.053 1.125 1.157 1.151 1.170 1.158 1.141 1.210 1.204 1.184 1.193
      1.202 1.161 1.195 1.264 1.281; PCB: 1.232 1.179 1.201 1.255 1.270
      1.234 1.269 1.148 1.218 1.191 1.239 1.239 1.211 1.196 1.254 1.280
      1.240 1.265 1.256 1.261 1.272 1.298 1.302 1.239 1.279 1.281 1.242
      1.300. Per-bin total, DMT: 1.390 1.320 1.348 1.425 1.344 1.388
      1.426 1.430 1.477 1.299 1.262 1.266 1.201 1.254 1.265 1.269 1.284
      1.279 1.270 1.338 1.310 1.304 1.314 1.367 1.290 1.358 1.414 1.388;
      PCB: 1.323 1.287 1.307 1.366 1.415 1.375 1.387 1.306 1.352 1.308
      1.358 1.372 1.343 1.334 1.387 1.415 1.391 1.402 1.390 1.398 1.404
      1.451 1.454 1.367 1.407 1.426 1.408 1.405.
  - **Caution on comparison with Luppi et al. eLife 2024 (recorded
    13 Sep 2026).** The "synergistic workspace" collapse under propofol
    and in disorders of consciousness is defined on a **workspace of
    regions** selected by their synergy-rank (gateway / broadcaster
    nodes), not on a whole-brain mean over all pairs. The whole-brain
    pair-mean reported here is a different quantity over a different
    region set. **No comparison across the two states (anaesthesia /
    DoC vs DMT), in either direction, is to be made until the regional
    definition is matched** — i.e. until synergy is computed on the same
    workspace definition, with the region selection fixed on independent
    data (rule 3). "Synergy falls under DMT as it does under propofol" is
    not a licensed sentence at this point.

- **EEG Lempel-Ziv complexity regressor (inspected 13 Sep 2026, before
  any correlation was computed).**
  `external/DMT_NCT/data/RegressorLZInterpscrubbedConvolvedAvg.mat`
  holds `RegDMT2`, `RegPCB2`, `Regdiff`, each **(14 subjects, 840 TRs)
  float64**, no non-finite values, per-subject and per-TR, zero-mean
  arbitrary units (DMT range −9.2 to 10.1). Same subject × TR grid as
  the fMRI. By the filename and its use in the original scripts it is
  the simultaneous-EEG Lempel-Ziv complexity (LZc) time course,
  interpolated over scrubbed frames, HRF-convolved and averaged (over
  channels), built as an fMRI regressor. The original MATLAB
  (`02_global_ce_analyses.m` lines 265–350, 497–520;
  `03_regional_ce_analyses.m:123`; `SI_regional_ce_placebo.m:119`)
  baseline-corrects each subject by the mean of TRs 1–240, drops the
  first and last TR (`2:839`) to match their CE series, and correlates
  the group-mean LZc with group-mean control energy (Spearman, shuffle
  permutation null) and per subject, plus a DMT-vs-PCB cluster test and
  a regional CE-vs-LZc map against 5-HT2A density. Group-mean DMT LZc
  per 30-TR bin: ≈ −1.0 to −1.2 for bins 1–8, jumps to +0.9 at bin 9,
  **peaks at bin 16 (2.45)**, i.e. later than the mean intensity peak
  (bin 10), and returns below baseline by bin 23. PCB is flat apart
  from a single-bin excursion at bin 9 (1.3). **Recorded before any
  correlation: whole-brain total TDMI (Σ 16 atoms, global fit) under
  DMT anti-correlates with LZc across the 28 bins.** Rationale: LZc
  indexes signal diversity / unpredictability, and TDMI is the
  predictability of the next sample from the current one, so a rise in
  LZc should coincide with the fall in total TDMI recorded above.
  Statistic: per-subject Spearman ρ across the 28 bins between
  bin-mean total TDMI and bin-mean LZc on the DMT run, group mean with
  a subject-level bootstrap CI (10,000 resamples), tested against a
  phase-randomised surrogate null of the LZc series (rule 2; 1,000
  surrogates per subject, seed 20261120), one-sided in the predicted
  direction with the two-sided value also reported; the PCB run and
  the sts and rtr atoms are reported alongside as controls / secondary.
  Script `03_lz_vs_tdmi.py`, output `results/lz_vs_tdmi_<variant>.csv`.
  Run on ts_gsr first (the file exists) and on ts_demean once its
  atoms file exists. Descriptive, Robustness A status; it is not a
  test of the intensity-tracking hypothesis and no motion control is
  applied here.
  - **Outcome on ts_gsr (13 Sep 2026, git 33f0b33-dirty — the
    uncommitted edits are this record, the `--variant` flag and
    `03_lz_vs_tdmi.py` itself; `results/lz_vs_tdmi_ts_gsr.csv`).**
    **Prediction holds descriptively.** Total TDMI vs LZc on the DMT
    run: group-mean per-subject ρ_S = **−0.242** [−0.401, −0.076]
    (subject bootstrap), 10 of 14 subjects negative, one-sided
    p = 0.002 and two-sided p = 0.003 against the phase-randomised
    LZc null (null mean 0.00, SD 0.08). PCB run: ρ_S = −0.047
    [−0.137, +0.039], p = 0.42, i.e. nothing. Group-mean-series
    version (as the original MATLAB computes it): ρ_S = −0.83 on DMT
    (p = 0.003), −0.10 on PCB. sts behaves the same (DMT −0.239
    [−0.380, −0.093], p = 0.001; PCB −0.03). rtr on DMT is also
    *negative* (−0.162 [−0.274, −0.049], two-sided p = 0.024; 3 of 14
    positive), consistent with the failed rtr prediction above.
    **Interpretive caution, recorded with the result:** LZc and every
    ΦID atom share the DMT onset step and the slow return, so a
    negative ρ_S across 28 bins is largely guaranteed for any two
    quantities that are drug-locked in opposite directions; the
    within-DMT correlation does not by itself show that TDMI tracks
    complexity beyond both tracking the drug. The stronger reading
    requires the decay-phase-only version with the tier-2 controls (a)
    and (b), which is not computed here. The PCB null shows the
    relationship is not a property of the scanner session alone.
  - **Outcome on ts_demean (13 Sep 2026, same git state;
    `results/lz_vs_tdmi_ts_demean.csv`).** Total TDMI vs LZc on DMT:
    ρ_S = **−0.214** [−0.368, −0.064], 10 of 14 negative, one-sided
    p = 0.004, two-sided 0.007; group-mean-series ρ_S = −0.72
    (p = 0.049). sts: −0.203 [−0.346, −0.067], p = 0.007. rtr: −0.023
    [−0.110, +0.069], nothing. **PCB on this variant shows a weak
    negative trend for total TDMI** (−0.093 [−0.179, −0.008], one-sided
    p = 0.045, two-sided 0.088; sts −0.089, two-sided 0.106) that was
    absent on ts_gsr, so the "not a session property" line above is
    weaker without GSR: the DMT effect is ≈ 2.3 × the PCB one on
    ts_demean, not ≫ it. Prediction holds on both variants at the
    descriptive level; the shared-drug-time-course caution applies in
    full.

## Primary B result

**ts_gsr, W = 60, 115 regions, windowed estimator (model refit per
window), run 13 Sep 2026, git e46df8a; inference by
`06_primary_b_analysis.py`, values verbatim from
`results/primary_b_ts_gsr_win60.csv` (run log
`results/run_06_ts_gsr_win60.log`).** Pre = windows 1–4; post/decay
primary = windows 6–14, sensitivity = windows 5–14. Whole-brain mean sts
in nats; N = 14; sign-flip test exact over 16,384 assignments,
two-sided; CIs subject-bootstrap 95 %, 10,000 draws; temporal null
phase-randomised, 1,000 surrogates; seed 20261120.

**Step contrast (primary windows).**

| quantity | value | 95 % CI | p |
|---|---|---|---|
| pre-injection DMT mean sts | 1.1554 | | |
| pre-injection PCB mean sts | 1.1378 | | |
| DMT post − pre | −0.0485 | [−0.0819, −0.0113] | 0.0267 |
| PCB post − pre | +0.0324 | [+0.0053, +0.0606] | 0.0425 |
| **DiD raw** | **−0.0809** | **[−0.1261, −0.0377]** | **0.0038** (sign-flip); **0.0020** (phase-randomised) |
| FD DiD, same form | +0.0143 | [−0.0070, +0.0365] | 0.2452 |
| **DiD FD-residualised** | **−0.0649** | **[−0.0966, −0.0289]** | **0.0048** |

DiD raw is −7.0 % of the pre-injection DMT mean and negative in 13 of
14 subjects; the FD-residualised DiD is negative in 13 of 14 and
**survives motion control** under the pre-registered definition (same
sign, CI excludes zero). Sensitivity windows 5–14: DiD raw −0.0733
[−0.1180, −0.0291], p = 0.0070, phase-randomised p = 0.0020, negative
in 12 of 14, −6.3 % of baseline; FD-residualised −0.0555 [−0.0864,
−0.0210], p = 0.0100, survives; DMT post − pre −0.0491 [−0.0823,
−0.0128], p = 0.0227; PCB post − pre +0.0242 [−0.0020, +0.0496],
p = 0.1040.

**Verdict on the directional hypothesis: REFUTATION.** The
pre-registered direction is up-regulation (+1); the DiD is negative and
significant on both nulls, on both window sets, raw and
FD-residualised. Per the directional-failure rule this is reported as a
refutation of the stated hypothesis, not as a confirmation of a
reframed one.

**Observation the global fit did not show:** on the placebo run,
whole-brain sts *increases* from pre to post (+0.0324 [+0.0053,
+0.0606], p = 0.0425 on the primary windows; +0.0242, p = 0.1040 on
the sensitivity windows). The 115-region global fit (Robustness A)
had PCB flat (within-condition change −0.005). Under the windowed
estimator, roughly 40 % of the DiD on the primary windows is the
placebo rise rather than the DMT fall.

**Tier-2 tracking, primary decay windows 6–14 (DMT run).**
- Group-mean-series ρ_S vs template (thresholded statistic): **raw
  −0.9833** (p = 0.0020), **FD-residualised −0.9500** (p = 0.0010);
  **both PASS the |ρ| ≥ 0.80 threshold**, sign negative against the
  pre-registered positive direction.
- Per-subject existence test (not thresholded): raw group mean ρ_S vs
  own ratings −0.4826 [−0.6291, −0.3362], p = 0.0010, 14 of 14 defined,
  |ρ| ≥ 0.80 in 3 subjects; vs template −0.5333 [−0.6750, −0.3845],
  p = 0.0010. FD-residualised: −0.3310 [−0.4761, −0.1592] and −0.3643
  [−0.5179, −0.1810], both p = 0.0010, |ρ| ≥ 0.80 in 0 subjects.
  **Significant against the null in the same (negative) direction as
  the group-mean series** in every version.
- Control (a), time in scanner, raw: PCB ρ_S vs template −0.1940
  [−0.3143, −0.0785], p = 0.0809; within-subject ρ_DMT − ρ_PCB −0.3393
  [−0.5179, −0.1619]: **clears control (a)** (CI excludes zero; PCB not
  ≥ half of DMT).
- Control (b), motion: window-mean FD (DMT) vs template ρ_S +0.4060
  [+0.1774, +0.6000]. **Control (a) on the FD-residualised data:** PCB
  ρ_S −0.1571 [−0.3155, −0.0190], p = 0.0500; within-subject
  ρ_DMT − ρ_PCB −0.2071 [−0.4345, +0.0345]: **VOID** (CI includes zero).
- **Tier-2 claim on the primary windows: VOID**, for both the
  per-subject-ratings and the template version, because control (a)
  fails on the FD-residualised data. Raw: gm_pass = True, subj_sig =
  True, same_dir = True, (a) void = False. Residualised: gm_pass = True,
  subj_sig = True, same_dir = True, **(a) void = True**.

**Tier-2 tracking, sensitivity windows 5–14.** Raw group-mean-series
ρ_S −0.8667 (p = 0.0300, PASS); per-subject −0.4267 [−0.5949, −0.2473]
and −0.4658 [−0.6294, −0.2840], both p = 0.0010. Control (a) raw: PCB
ρ_S −0.3307 [−0.4494, −0.2087], p = 0.0050; ρ_DMT − ρ_PCB −0.1351
[−0.2935, +0.0338]: **VOID on the raw data as well** (CI includes zero
and PCB is the same sign and ≥ half of DMT). FD (DMT) vs template
+0.5117 [+0.3489, +0.6632]. FD-residualised: group-mean-series ρ_S
−0.5152 (p = 0.2168, **fails** the threshold); per-subject −0.2358
[−0.3757, −0.0903], p = 0.0130, and −0.2797 [−0.4277, −0.1203],
p = 0.0050; control (a) ρ_DMT − ρ_PCB +0.0052 [−0.2017, +0.2026], VOID.
**Tier-2 claim on the sensitivity windows: VOID.**

**Reading of the control (a) numbers (recorded 13 Sep 2026; a reading,
not a reframing of the verdict).** After FD residualisation the DMT
per-subject mean remains significant (−0.331, p = 0.001) and the
DMT-minus-PCB difference remains negative (−0.207), but its CI
[−0.435, +0.035] includes zero. FD tracks the template at +0.406
[+0.177, +0.600], so residualisation removed roughly a third of the
DMT tracking (−0.483 → −0.331 own ratings; −0.533 → −0.364 template),
the over-removal cost recorded before the run. PCB tracks the template
at −0.194 on the primary windows and −0.331 on the sensitivity windows
(71 % of DMT's −0.466 there), which is the time-in-scanner effect the
control was designed to detect and which validates excluding window 5.
The void on the primary windows reflects attenuation plus a wide CI at
N = 14, not a placebo trend comparable to DMT's on those windows; the
void stands as written.

**Tier assignment for the paper's primary empirical claim: TIER 3.**
Per the pre-registered ordering of outcomes, with the tier-2 claim void
on both window sets, the primary result is the step-change contrast
(above, reported as a refutation of the directional hypothesis) plus
the methods contribution (bias characterisation, the global fit's
smearing of non-stationarity, and the tier-2 controls as applied). The
tier-2 statistics are reported in full with the void verdict and the
control that voided them; they are not claimed.

Still to come under Primary B, queued 13 Sep 2026: the W = 30 positive
control on ts_gsr (prediction: same sign, smaller magnitude), and the
ts_demean variant at W = 60 (rule 6), each through the same script.

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
