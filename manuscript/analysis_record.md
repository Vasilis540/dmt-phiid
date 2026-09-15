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

**W = 30 positive control (ts_gsr, 28 windows, git ac1fdc0;
`results/primary_b_ts_gsr_win30.csv`, log `results/run_06_ts_gsr_win30.log`;
recorded 13 Sep 2026).** Pre = bins 1–8, primary post = bins 11–28,
sensitivity = bins 10–28.
- DiD raw **−0.0686 [−0.1084, −0.0293]**, sign-flip p = 0.0042,
  phase-randomised p = 0.0010, negative in 13 of 14, −6.7 % of the
  pre-injection DMT mean (1.1554 at W = 60 → the W = 30 pre mean is in
  the file). DMT post − pre −0.0390 [−0.0680, −0.0058], p = 0.0354; PCB
  post − pre +0.0296 [+0.0076, +0.0531], p = 0.0269 (the placebo rise
  is present at W = 30 too). **FD-residualised DiD −0.0545 [−0.0836,
  −0.0215], p = 0.0065, survives**, negative in 13 of 14. Sensitivity
  bins 10–28: DiD −0.0658 [−0.1072, −0.0261], p = 0.0067; residualised
  −0.0514 [−0.0799, −0.0179], p = 0.0109, survives.
- **Same sign as W = 60, smaller magnitude. Ratio W30 / W60 =
  0.0686 / 0.0809 = 0.85**, against the pre-registered prediction of
  one-third to two-thirds. Per the recorded criterion this is **not
  inconsistent with the shrinkage model** (inconsistency required the
  opposite sign or a larger magnitude), **but the ratio falls outside
  the predicted range.**
- **Where the prediction came from, and what the correct comparison
  gives.** The predicted range was computed from the stationary
  absorption table ((1 − absorb₃₀)/(1 − absorb₆₀) = 0.37–0.56 across
  the four stationary cells). The relevant simulation is the
  non-stationary step condition, which has the same pre/post form as
  the real contrast. From the 20,000-run `bias_check_nonstat.csv`,
  recovered step (estimated post − pre as a share of the true step,
  sts, identical on the full and primary post sets): coupling 47.8 %
  at W = 30, 84.2 % at W = 60 → **predicted ratio 0.57**; noise-corr
  28.1 % / 66.6 % → **0.42**. The step table therefore predicts
  0.42–0.57, in the same range as the stationary table, and **the
  observed 0.85 is not near either. The shrinkage model over-predicts
  attenuation on real data.**
- **Reason, checked rather than assumed (SUPERSEDED by the AR-shift
  outcome and diagnostic below: the lag-1 test used here was the wrong
  test, and the milder-structure explanation stands).** The candidate
  explanation "real autocorrelation structure is milder than the
  VAR(1) parameters" was tested on lag-1 autocorrelation and appeared
  **contradicted**: on ts_gsr the
  regional lag-1 autocorrelation is 0.867 pooled (median 0.868, 5–95 %
  0.833–0.900; DMT 0.864, PCB 0.870), against 0.53 in the simulated
  baseline; real autocorrelation is far *stronger*. Real zero-lag
  pairwise correlation is weaker than simulated (mean |r| 0.195,
  median 0.161, signed mean −0.004, 5–95 % −0.375 to +0.451, against
  0.33). The most likely reason consistent with these numbers: **the
  real covariance change is of a type the bias check never
  simulated.** The simulation shifted cross-coupling (c) or innovation
  correlation (q) with the autoregressive a fixed, whereas on real
  data the largest atom changes after sts are the within-region
  self-transfer atoms xtx and yty (global fit: −0.046 and −0.037), i.e.
  a change in autocorrelation, and the pairs sit in a regime (a ≈ 0.87,
  weak cross-correlation) far from the simulated one. The shrinkage
  factors measured for c- and q-shifts at a ≈ 0.5 do not transfer to
  an a-shift at a ≈ 0.87. This is a limitation of the bias check to
  state in the paper, not a reason to revise the W = 60 primary
  result; an a-shift condition at realistic autocorrelation is the
  obvious addition to `02_bias_check.py` if the shrinkage figures are
  to be quoted as applying to these data.
- **AR-shift step condition added to `02_bias_check.py` (13 Sep 2026,
  parameters fixed and prediction recorded BEFORE the run).** Purpose:
  test the shrinkage model on the covariance-change type the real data
  showed. `nonstat_step_ar`: baseline a = (0.87, 0.87) (the measured
  real lag-1 autocorrelation), c = (0.025, 0.01), q = 0.05,
  s = (1.0, 1.4), giving pairwise corr(x, y) = 0.197 against the
  measured mean |r| = 0.195, implied autocorrelation (0.877, 0.871),
  analytic sts 1.384 (close to the real whole-brain ≈ 1.16–1.31),
  rtr 0.016, no MMI candidate tied, spectral radius 0.886 (the 0.75
  transient bound of the other conditions does not hold; transients
  after the switch decay as 0.886^t, ≈ 30 % at 10 TRs, and are part of
  what is measured, as for the other conditions). Shift: a → a − 0.0085
  with c, q, s fixed, bins 9–28, true sts 1.3844 → 1.3284, step −0.0560
  (asym coupling step: −0.0562). Kept in a separate parameter dict so
  the stationary tables are unchanged; run with
  `--only-nonstat nonstat_step_ar --out results/nonstat_ar_step
  --n-runs 2000`, step condition only, no tracking criterion.
  **Prediction, recorded before the run:** if the W = 30 / W = 60
  step-recovery ratio for this condition is near the observed 0.85,
  the shrinkage model is confirmed on the condition that actually
  matches the data, and the pre-registered range (one-third to
  two-thirds) was wrong because it came from the wrong shift type
  (c- and q-shifts at a ≈ 0.5, ratios 0.42–0.57). If the ratio is again
  ≈ 0.4–0.6, the shift type is not the explanation and the
  over-attenuation on real data remains unexplained; if the recovery at
  W = 60 itself is far from 84 %, the W = 60 shrinkage cost quoted for
  the primary result must be restated from this condition.
  - **Outcome (2,000 runs, 100 s, git f3b435d;
    `results/nonstat_ar_step/bias_check_nonstat*.csv`).** Recovered
    step, sts (estimated post − pre as a share of the true −0.0560):
    **W = 30 32.9 % (full post) / 34.4 % (primary post); W = 60 55.4 %
    / 57.3 %; ratio W30 / W60 = 0.59 / 0.60.** Per-window bias in the
    pre regime −0.898 at W = 30 and −0.576 at W = 60 on a true value
    of 1.384 (65 % and 42 %); SD per window 0.30 / 0.28; global-fit
    estimate 1.269 against the mixture truth 1.344. **The prediction's
    first branch fails: the ratio is 0.60, not 0.85, so the shift type
    is not the explanation.** The third clause is also triggered (W = 60
    recovery 57 % against the 84 % quoted for the coupling step), but
    see the diagnostic below before restating any cost from this
    condition.
  - **Diagnostic, run after the outcome and recorded with it: this
    condition does not match the real data either, and the reason
    corrects the record above.** (i) Real windowed-vs-global gap in
    pre-injection whole-brain sts on ts_gsr: global fit 1.3085 (DMT) /
    1.2893 (PCB); W = 60 1.1554 / 1.1378 (gap −0.153 / −0.152); W = 30
    1.0223 / 1.0063 (gap −0.286 / −0.283). The simulated per-window
    bias at a = 0.87 is −0.576 (W = 60) and −0.898 (W = 30): **3.8 and
    3.1 times the real gap.** (ii) Real autocorrelation function of the
    regional series (ts_gsr, pooled over regions, subjects, conditions)
    against AR(1) with a = 0.87:

    | lag | 1 | 2 | 3 | 5 | 8 | 10 | 15 | 20 |
    |---|---|---|---|---|---|---|---|---|
    | real ACF | 0.867 | 0.534 | 0.161 | −0.187 | −0.089 | −0.219 | −0.127 | −0.062 |
    | AR(1) 0.87 | 0.870 | 0.757 | 0.659 | 0.498 | 0.328 | 0.248 | 0.124 | 0.062 |

    The real ACF matches at lag 1 and nothing else: it falls to 0.16 by
    lag 3 and is negative from lag 5 (the signature of band-pass
    filtered fMRI), whereas AR(1) at 0.87 is still 0.66 and 0.50 at
    those lags. Integrated autocorrelation time, crude (1 + 2·Σ over
    the lags above): **≈ 2.8 real against 14.4 for the AR(1)**, i.e.
    the real 60-TR window carries several times more effective samples
    than the simulated one. The finite-window log-det bias is governed
    by the effective sample size, which is why the simulated per-window
    bias is 3–4 × the real gap and why the simulated shrinkage of a
    step is larger than observed. **Correction to the entry above:**
    the explanation "real autocorrelation structure is milder than the
    VAR(1) parameters" was recorded as *contradicted* on the basis of
    lag-1 autocorrelation alone (0.87 real vs 0.53 simulated). Lag-1
    autocorrelation was the wrong test. In the quantity that governs
    the bias, the integrated autocorrelation time, **the real structure
    is far milder than every simulated family** (0.53-AR(1): 3.3;
    0.87-AR(1): 14.4; real ≈ 2.8), and that explanation stands as the
    most likely one. The "shift type" explanation is withdrawn as the
    primary reason; it may still contribute but is not needed.
  - **Consequences.** No simulated family reproduces the real
    dependence structure, so **no simulated shrinkage figure (49 / 84 %,
    28 / 67 %, or 34 / 57 %) is quoted as the cost of the W = 60 primary
    result.** What can be said: the W = 30 / W = 60 ratio observed on
    real data is 0.85, both estimators agree in sign, and the real
    windowed-vs-global gaps (−0.15 at W = 60, −0.29 at W = 30) bound the
    per-window bias on these data directly. The paper states the
    windowed estimates as biased low by an amount of that order, common
    to both conditions, with the DiD's shrinkage on real data unknown
    from simulation but bounded by the two window lengths agreeing to
    within 15 %. The obvious addition to `02_bias_check.py`, not run:
    a process matching the real ACF (band-passed noise or an AR(2) with
    a negative lobe, matched on integrated autocorrelation time ≈ 3),
    which is the condition that would actually test the shrinkage on
    these data. All four simulated shift conditions remain valid as
    what they are: bias characterisation at longer correlation times
    than the data have, i.e. conservative for the level bias and
    pessimistic for the step shrinkage.
- Tier-2 lines at W = 30, reported as a check that decides nothing:
  group-mean-series ρ_S −0.9752 raw, −0.8535 FD-residualised on bins
  11–28 (both above 0.80, negative); per-subject means −0.388 / −0.408
  raw, −0.267 / −0.279 residualised, all p ≤ 0.002; control (a) clears
  on raw (ρ_DMT − ρ_PCB −0.223 [−0.415, −0.043]) and is **void on the
  residualised data** (−0.146 [−0.337, +0.031]); sensitivity bins 10–28
  void on raw as well (−0.164 [−0.334, +0.003]). Same pattern as W = 60.

**Rule-6 variant check: ts_demean, W = 60, 115 regions, windowed
estimator, run 13 Sep 2026, git f3b435d (both the atoms file and the
inference); values verbatim from `results/primary_b_ts_demean_win60.csv`
(log `results/run_06_ts_demean_win60.log`). Same windows, tests, seeds
and surrogate counts as the ts_gsr result above.**

Step contrast (primary windows 6–14):

| quantity | value | 95 % CI | p |
|---|---|---|---|
| pre-injection DMT mean sts | 1.1004 | | |
| pre-injection PCB mean sts | 1.0819 | | |
| DMT post − pre | −0.0633 | [−0.1088, −0.0123] | 0.0333 |
| PCB post − pre | +0.0398 | [+0.0089, +0.0692] | 0.0306 |
| **DiD raw** | **−0.1031** | **[−0.1558, −0.0522]** | **0.0026** (sign-flip); **0.0010** (phase-randomised; null mean −0.0003, SD 0.0264) |
| FD DiD, same form | +0.0143 | [−0.0070, +0.0365] | 0.2452 |
| **DiD FD-residualised** | **−0.0824** | **[−0.1224, −0.0372]** | **0.0048** |

DiD raw is −9.4 % of the pre-injection DMT mean, negative in 12 of 14;
FD-residualised negative in 13 of 14, survives motion control under the
pre-registered definition. Sign −1 against the pre-registered +1:
refutation, as on ts_gsr. Sensitivity windows 5–14: DMT post − pre
−0.0621 [−0.1055, −0.0130], p = 0.0300; PCB post − pre +0.0314
[+0.0013, +0.0585], p = 0.0637; DiD raw −0.0935 [−0.1431, −0.0426],
p = 0.0039, phase-randomised p = 0.0010, −8.5 % of baseline, negative
in 12 of 14; FD DiD +0.0191 [−0.0008, +0.0402], p = 0.1083;
FD-residualised −0.0714 [−0.1106, −0.0298], p = 0.0073, survives,
negative in 12 of 14.

**The ts_demean step contrast replicates the ts_gsr one**: DiD negative
and significant on both nulls, on both window sets, raw and
FD-residualised (ts_gsr primary: −0.0809; ts_demean primary: −0.1031).

Tier-2 tracking, primary windows 6–14, ts_demean, verbatim:
- Group-mean-series ρ_S vs template (thresholded): raw −0.9333
  (p = 0.0120), FD-residualised −0.8833 (p = 0.0060); both PASS
  |ρ| ≥ 0.80, sign negative.
- Per-subject existence test: raw vs own ratings −0.3041 [−0.4882,
  −0.1027], p = 0.0210, 14 of 14 defined, |ρ| ≥ 0.80 in 1; vs template
  −0.3667 [−0.5476, −0.1548], p = 0.0090. FD-residualised: vs own
  ratings −0.1874 [−0.3608, −0.0026], p = 0.0689, **not significant**;
  vs template −0.2429 [−0.4333, −0.0500], p = 0.0210.
- Control (a) raw: PCB ρ_S vs template −0.2345 [−0.3786, −0.0893],
  p = 0.0330; ρ_DMT − ρ_PCB −0.1321 [−0.3655, +0.1084]: **VOID on the
  raw data** (CI includes zero; PCB same sign and ≥ half of DMT), which
  differs from ts_gsr, where raw cleared (a) on the primary windows.
- Control (b): FD (DMT) vs template +0.4060 [+0.1774, +0.6000] (FD is
  variant-independent). FD-residualised control (a): PCB −0.1000
  [−0.2036, +0.0071], p = 0.2208; ρ_DMT − ρ_PCB −0.1429 [−0.3357,
  +0.0667]: VOID.
- **Tier-2 claim on the primary windows: VOID** (own ratings: raw
  gm_pass = True, subj_sig = True, same_dir = True, (a) void = True;
  resid gm_pass = True, subj_sig = False, (a) void = True. Template:
  raw and resid gm_pass = True, subj_sig = True, (a) void = True).

Tier-2, sensitivity windows 5–14, ts_demean: raw group-mean-series ρ_S
−0.6727 (p = 0.1968, fails the threshold); per-subject vs own ratings
−0.2403 [−0.4233, −0.0366], p = 0.0639 (not significant), vs template
−0.2883 [−0.4874, −0.0675], p = 0.0260; control (a) raw: PCB −0.3550
[−0.4909, −0.1931], p = 0.0020, ρ_DMT − ρ_PCB +0.0667 [−0.1195,
+0.2658], VOID; FD (DMT) vs template +0.5117 [+0.3489, +0.6632].
FD-residualised: group-mean-series −0.4545 (p = 0.3167, fails);
per-subject −0.1243 [−0.3226, +0.0836], p = 0.2068, and −0.1766
[−0.3827, +0.0545], p = 0.0799; control (a): PCB −0.2831 [−0.4017,
−0.1532], p = 0.0010, ρ_DMT − ρ_PCB +0.1065 [−0.0918, +0.3126], VOID.
**Tier-2 claim on the sensitivity windows: VOID.** Tier 3 on this
variant as on ts_gsr.

**Estimator comparison: rtr, total TDMI and the self-transfer atoms
under the windowed W = 60 estimator against the global fit
(`07_windowed_atoms_did.py`, ts_gsr, git 553e919;
`results/windowed_atoms_did_ts_gsr_win60.csv`, log
`results/run_07_ts_gsr_win60.log`).** Per-subject DiD = (post − pre)
DMT − (post − pre) PCB, exact sign-flip p (two-sided), subject-bootstrap
95 % CI (10,000 draws, seed 20261120); no temporal null, no motion
handling. The global-fit atoms are re-summarised on the identical bin
sets (pre bins 1–8; primary bins 11–28; sensitivity bins 9–28; peak
bins 9–14), so the two estimators are compared like for like. Values
in nats; "neg" = subjects with negative DiD out of 14.

Primary (pre windows 1–4 / bins 1–8; post windows 6–14 / bins 11–28):

| atom | windowed DiD [CI], p, neg | global DiD [CI], p, neg |
|---|---|---|
| sts | −0.0809 [−0.1253, −0.0365], 0.0038, 13 | −0.0801 [−0.1302, −0.0310], 0.0071, 12 |
| rtr | −0.0078 [−0.0135, −0.0016], 0.0312, 10 | −0.0060 [−0.0131, +0.0014], 0.1378, 10 |
| total | −0.1037 [−0.1600, −0.0479], 0.0034, 12 | −0.1216 [−0.1917, −0.0526], 0.0051, 13 |
| xtx | −0.0523 [−0.0839, −0.0221], 0.0065, 12 | −0.0544 [−0.0885, −0.0216], 0.0081, 12 |
| yty | −0.0396 [−0.0673, −0.0130], 0.0131, 13 | −0.0431 [−0.0767, −0.0128], 0.0137, 13 |
| rts | −0.0407 [−0.0645, −0.0178], 0.0051, 12 | −0.0396 [−0.0661, −0.0141], 0.0090, 12 |

Pre-injection levels, windowed / global: sts 1.1554 / 1.3085 (DMT),
1.1378 / 1.2893 (PCB); rtr 0.0388 / 0.0248, 0.0375 / 0.0225; total
1.4772 / 1.4421, 1.4597 / 1.4046; xtx 0.6273 / 0.6897; yty 0.6125 /
0.6719; rts 0.5669 / 0.6435. Sensitivity (post windows 5–14 / bins
9–28), windowed: sts −0.0733 [−0.1179, −0.0298], p = 0.0070, 12; rtr
−0.0071 [−0.0127, −0.0010], p = 0.0424, 10; total −0.0930 [−0.1495,
−0.0370], p = 0.0072, 12; xtx −0.0467, p = 0.0137; yty −0.0351,
p = 0.0239; rts −0.0371, p = 0.0079. Global: sts −0.0735 [−0.1242,
−0.0251], p = 0.0112, 12; rtr −0.0060 [−0.0127, +0.0012], p = 0.1285,
10; total −0.1138 [−0.1835, −0.0441], p = 0.0079, 11; xtx −0.0503,
p = 0.0121; yty −0.0393, p = 0.0210; rts −0.0362, p = 0.0131. Peak
(post windows 5–7 / bins 9–14), windowed: sts −0.0700 [−0.1065,
−0.0301], p = 0.0055, 13; rtr −0.0103 [−0.0164, −0.0036], p = 0.0120,
11; total −0.0929 [−0.1414, −0.0417], p = 0.0051, 12; xtx −0.0396,
p = 0.0363; yty −0.0313, p = 0.0361; rts −0.0345, p = 0.0096. Global:
sts −0.0752 [−0.1108, −0.0336], p = 0.0044, 13; rtr −0.0091 [−0.0152,
−0.0027], p = 0.0203, 10; total −0.1175 [−0.1701, −0.0603],
p = 0.0018, 13; xtx −0.0460, p = 0.0128; yty −0.0373, p = 0.0155; rts
−0.0353, p = 0.0082. (The global peak-window rtr and total DiDs here,
−0.0091 and −0.1175, are the figures recorded under Robustness A as
−0.0091 and −0.118.)

**Under the windowed estimator rtr and total TDMI move in the same
direction as under the global fit**: every DiD in the table is
negative for both estimators on all three window sets. The windowed
rtr DiD is significant on the primary windows (p = 0.0312) where the
global-fit one is not (p = 0.1378); the total's DiD is smaller under
the windowed estimator (−0.1037 vs −0.1216, primary).

**Provenance note (13 Sep 2026).** The Robustness C atoms files
(`atoms_bins_115regions-all_ts_gsr_placebo.npy/.csv`,
`atoms_bins_local_115regions-all_ts_gsr_placebo.npy`) and the 07
comparison (`windowed_atoms_did_ts_gsr_win60.csv`) were first produced
at f3b435d-dirty and rerun at 553e919 with the committed scripts. The
rerun is bitwise identical to the dirty-tagged versions: both `.npy`
files equal with max |difference| 0 and the same NaN pattern, and both
CSV bodies and the 07 log body identical line for line; only the git tag
in the header changed.

**Robustness C (placebo-fitted model): atoms computed at 553e919
(`01_synergy_timecourse.py --fit-mode placebo --variant ts_gsr`,
115 regions, 6,555 pairs, 271 s). Inference script
`08_robustness_c_analysis.py` written 13 Sep 2026; because PCB is
scored only on its out-of-sample half (bins 15–28), the DiD form does
not apply, and the script reports (i) the within-DMT step, bins 11–28
minus 1–8 (9–28 sensitivity), and (ii) DMT minus PCB on the matched
out-of-sample bins 15–28, each with the sign-flip test and bootstrap CI,
alongside the same contrasts from the native global fit on the identical
bins.**

**Robustness C result (ts_gsr, 115 regions; inference git 2af901c,
`results/robustness_c_ts_gsr.csv`, log
`results/run_08_robustness_c_ts_gsr.log`; recorded 13 Sep 2026).**
Whole-brain pair-mean atoms in nats, N = 14; sign-flip test exact over
16,384 assignments, two-sided; subject-bootstrap 95 % CI, 10,000 draws,
seed 20261120. **Both evaluations are out-of-sample under a model
fitted to a segment neither evaluation touches** (PCB TRs 0–419): DMT
bins 1–28 and the held-out PCB half, bins 15–28. No temporal null, no
motion handling.

- **Contrast (ii), DMT minus PCB on matched out-of-sample bins 15–28:
  sts −0.1110 [−0.1803, −0.0593], p = 0.0005, negative in 13 of 14
  (DMT 1.3213, PCB 1.4323; −7.8 % of PCB); total TDMI −0.0817
  [−0.1438, −0.0332], p = 0.0031, 13 of 14; rtr +0.0028 [−0.0020,
  +0.0075], p = 0.2781, 7 of 14.** Native global fit on the same bins:
  sts −0.0536 [−0.0941, −0.0241], p = 0.0010, 12 of 14 (DMT 1.2696,
  PCB 1.3232); total −0.0748, p = 0.0024; rtr −0.0024, p = 0.3341.
  **Sign and significance of the DMT-below-PCB result are confirmed
  under the independent model. The magnitude is not comparable to the
  native fit**: out-of-sample inflation relative to the native fit is
  +0.109 on PCB (1.323 → 1.432) and +0.052 on DMT (1.270 → 1.321), and
  the asymmetry, −0.057, is by construction identical to the
  difference between the placebo-fitted and native contrasts
  (−0.111 − (−0.054) = −0.057), so the doubling of the contrast is
  entirely the unequal inflation.
- **Contrast (i), within-DMT step, bins 11–28 minus bins 1–8 under the
  placebo-fitted model: sts −0.0508 [−0.1047, +0.0137], p = 0.1338,
  negative in 11 of 14** (pre 1.3549, post 1.3041; −3.7 %); rtr
  −0.0034 [−0.0075, +0.0005], p = 0.1359; total −0.0505 [−0.1103,
  +0.0198], p = 0.1741. Sensitivity bins 9–28: sts −0.0477 [−0.1001,
  +0.0148], p = 0.1467. Native global fit, same bins: sts −0.0521
  [−0.0947, −0.0068], p = 0.0450, 11 of 14. **Same point estimate as
  the native fit; the CI includes zero. Direction preserved,
  significance not.**
- **Reading of the inflation asymmetry (a reading, not a claim).** The
  native DMT model spans a drug peak and a decay and fits the decay
  phase as a compromise between regimes, so a placebo-fitted model is
  nearly as good there (+0.052). The placebo run is homogeneous, so its
  native model fits its own held-out half well and a model from half
  the run costs more (+0.109). Consistent with the DMT run being
  non-stationary and the placebo run not; not a test of it.
- **Summary: Robustness C supports the sign of the primary result under
  an independent model; magnitude and within-DMT significance do not
  transfer.**

## Subject alignment across files (checked 13 Sep 2026)

**Question.** The scripts assume the timeseries subject axis, the columns
of `FDlong.mat`, the rows of `intensity_ratings.mat` and the rows of the
EEG LZ regressor share one ordering. No numeric array carries subject IDs.
Evidence collected by `scripts/10_subject_alignment_check.py` (report
`results/subject_alignment_check.txt`, permutation table
`results/subject_alignment_permtests.csv`, log
`results/run_10_subject_alignment_check.log`; run at 66b570e-dirty, the
script itself being the uncommitted file). Results recorded, no
interpretation beyond the verdict.

- **(a) MATLAB indexing.** One loop variable `i` in `1:nsub` indexes
  `TS{i,1}` / `TS{i,2}` (`01_gen_time_resolved_ce.m:30-49`),
  `dmt_intensity(i,:)` and `pcb_intensity(i,:)`
  (`02_global_ce_analyses.m:545,560`), and `RegDMT2(i,:)` / `RegPCB2(i,:)`
  (`:514,529`). FD is laid out as (TRs, subjects) and used only at the
  group level (`:444,461,479`: mean over subjects), so FD-to-subject
  alignment is asserted by the layout, not exercised per subject, in the
  original code.
- **(b) Subject index 2, PCB, TR 839.** The timeseries is NaN in all 116
  regions in all four variants at that one (subject, condition, TR).
  **`FDPCB[839, 2] = 0.0 exactly**; it is the only exact zero beyond TR 0
  in any of the 28 FD columns (TR 0 is 0 for every column), and it is the
  0th percentile of its own column (median 0.091). `FDDMT[839, 2]` is
  0.058, normal. Verdict for that cell: **anomalous, co-located with the
  timeseries defect** (an FD of 0 is what a missing displacement
  computation yields). LZ shows nothing at that TR (interpolated,
  HRF-convolved EEG series).
- **(c) Other cross-file evidence.**
  - **Subject IDs recovered from `intensity_ratings.mat`.** The file also
    holds two opaque MATLAB `table` objects (`DMT_intensity`,
    `PCB_intensity`), decodable from scipy's `__function_workspace__`:
    23 rows (20 subject codes + SD/SEM/average) × 28 rating columns. The
    14-row `dmt_intensity` array matches, row by row and uniquely, table
    subjects **the 14 codes (not reproduced)** in that order, i.e. the
    table order with **the six codes of the excluded participants (not
    reproduced)** removed
    (14 of 20; Timmermann et al. recruited 20, Singleton et al. analyse
    14). The two placebo rows with non-zero ratings (indices 5 and 7)
    match the same two codes (not reproduced), the same subjects as their DMT rows, so the
    DMT and PCB rating arrays share one ordering. No other file carries
    IDs, so this fixes the ratings order as ascending subject code but
    cannot by itself tie it to the timeseries.
  - **Matched vs mismatched pairings** (per-subject 28-bin series with
    the group-mean curve removed; mean matched Spearman ρ against 20,000
    permutations of the subject assignment, two-sided about the
    mismatched mean). Timeseries-derived sts and total TDMI (ts_gsr
    global-fit atoms) vs EEG LZ on DMT: matched **−0.173 / −0.165**
    against mismatched +0.005 / +0.001, **p = 0.008 / 0.009**. TDMI vs
    FD on PCB: −0.111 vs +0.008, p = 0.043; LZ vs FD on PCB: +0.102 vs
    −0.010, p = 0.047. Ratings vs FD on DMT: +0.186 vs +0.014,
    p = 0.076. Ratings vs LZ, sts, TDMI: p = 0.24–0.56 (the ratings
    carry little subject-specific shape once the group curve is removed:
    every subject's first rating ≥ half-max is bin 9). All other cells
    null; full table in the CSV.
  - **TR-level FD vs DVARS** (frame-to-frame RMS change of raw `ts`):
    diagonal mean +0.05 / +0.06, off-diagonal −0.02 / +0.01, argmax on
    self in 4/14 rows for both conditions. Uninformative on these
    denoised, band-passed, scrub-interpolated timeseries; not evidence
    against alignment.
  - File creation dates differ (ratings Aug 2022, LZ Feb 2023,
    timeseries May 2023, FD Dec 2023); the submodule has a single
    squashed commit, so git history gives no provenance.
- **Verdict.** Timeseries ↔ FD: **verified at one subject** (the
  co-located defect), weakly supported statistically; a single co-located
  row does not exclude a permutation of the other 13, which the
  statistical tests lack power to detect. Timeseries ↔ EEG LZ:
  **verified** statistically (p < 0.01) and by the MATLAB per-subject
  loop. Ratings ↔ timeseries and ratings ↔ FD: **plausible, not
  verified** (MATLAB per-subject loop; ratings in ascending subject-code
  order; ratings-vs-FD in the expected direction at p = 0.08). Overall:
  **plausible with two pairs verified; nothing found contradicts a single
  shared ordering.** Full verification needs the authors' subject list.

## Global functional connectivity per bin (`09_global_fc_per_bin.py`, 13 Sep 2026)

Mean Pearson r over all 6,555 pairs (115 regions, region 20 excluded) per
subject, condition and 30-TR bin, each bin correlated on its own TRs
(subject index 2 PCB bin 28 uses 29 TRs). Arrays
`results/global_fc_bins_115regions-all_<variant>.npy` (14, 2, 28);
contrasts `results/global_fc_did_<variant>.csv`; logs
`results/run_09_<variant>.log`; run at 66b570e-dirty (the script was the
uncommitted file). DiD = (post − pre) DMT − (post − pre) PCB, pre = bins
1–8, post = bins 11–28 (primary) / 9–28 (sensitivity) / 9–14 (peak);
exact sign-flip test over 2^14 assignments, two-sided; subject-bootstrap
95 % CI, 10,000 draws, seed 20261120; no temporal null, no motion
handling. The whole-brain sts DiD from the global-fit atoms file on the
identical bins is placed alongside; the two numbers are reported side by
side and their relationship is not interpreted here.

**ts_gsr.** Group-mean r is ≈ −0.002 in every bin of both conditions
(DMT range −0.0058 to −0.0008, PCB −0.0053 to −0.0010): global signal
regression pins the pair-mean correlation near zero by construction, so
any contrast on this variant is a shift within that constraint and the
"share of baseline" figure is not meaningful (negative baseline).

| set | quantity | DMT post − pre | PCB post − pre | DiD [95 % CI] | p | neg/pos |
|---|---|---|---|---|---|---|
| primary 11–28 | mean r | −0.0020 (p 0.006) | +0.0013 (p 0.020) | **−0.0034 [−0.0051, −0.0017]** | **0.0024** | 11/3 |
| primary 11–28 | sts, global fit (nats) | −0.0521 (p 0.045) | +0.0280 (p 0.047) | −0.0801 [−0.1303, −0.0310] | 0.0071 | 12/2 |
| sensitivity 9–28 | mean r | −0.0020 (p 0.005) | +0.0012 (p 0.022) | −0.0032 [−0.0047, −0.0017] | 0.0017 | 11/3 |
| sensitivity 9–28 | sts (nats) | −0.0515 | +0.0220 | −0.0735 [−0.1237, −0.0236] | 0.0112 | 12/2 |
| peak 9–14 | mean r | −0.0025 (p 0.0002) | +0.0007 (p 0.28) | −0.0032 [−0.0050, −0.0015] | 0.0023 | 12/2 |
| peak 9–14 | sts (nats) | −0.0808 | −0.0056 | −0.0752 [−0.1114, −0.0335] | 0.0044 | 13/1 |

Pre-injection mean r: DMT −0.0020, PCB −0.0039. **On ts_gsr, mean
pairwise r does not rise under DMT; the DiD is negative** (DMT falls by
0.002, PCB rises by 0.001, within a quantity held near zero by GSR).

**ts_demean (no GSR).** Group-mean r per bin, DMT: 0.201 0.183 0.191
0.181 0.205 0.196 0.184 0.184 **0.326** 0.287 0.226 0.269 0.252 0.254
0.204 0.204 0.218 0.259 0.205 0.227 0.238 0.230 0.250 0.260 0.241 0.229
0.213 0.220; PCB: 0.210 0.201 0.153 0.149 0.154 0.155 0.151 **0.278
0.336** 0.142 0.155 0.152 0.154 0.171 0.189 0.174 0.195 0.161 0.162
0.183 0.159 0.195 0.168 0.170 0.170 0.180 0.172 0.172. Both conditions
show an injection-locked jump at bins 8–9 (PCB 0.278 / 0.336 against a
≈ 0.15 baseline; DMT 0.326 at bin 9), the same bins as the placebo rtr
bump recorded under Robustness A; DMT stays elevated afterwards
(0.20–0.27) while PCB returns to 0.14–0.20 by bin 10.

| set | quantity | DMT post − pre | PCB post − pre | DiD [95 % CI] | p | neg/pos |
|---|---|---|---|---|---|---|
| primary 11–28 | mean r | +0.0426 [+0.0006, +0.0872] (p 0.093) | −0.0100 (p 0.59) | **+0.0526 [+0.0073, +0.0976]** | **0.0470** | 4/10 |
| primary 11–28 | sts, global fit (nats) | −0.0684 (p 0.064) | +0.0351 (p 0.054) | −0.1035 [−0.1678, −0.0357] | 0.0132 | 11/3 |
| sensitivity 9–28 | mean r | +0.0500 (p 0.047) | −0.0032 (p 0.87) | +0.0532 [+0.0113, +0.0930] | 0.0322 | 4/10 |
| sensitivity 9–28 | sts (nats) | −0.0613 | +0.0297 | −0.0909 [−0.1536, −0.0254] | 0.0175 | 11/3 |
| peak 9–14 | mean r | +0.0783 (p 0.003) | +0.0037 (p 0.81) | +0.0746 [+0.0293, +0.1282] | 0.0046 | 3/11 |
| peak 9–14 | sts (nats) | −0.0887 | −0.0077 | −0.0810 [−0.1446, −0.0176] | 0.0348 | 11/3 |

Pre-injection mean r: DMT 0.1905, PCB 0.1813; primary DiD is +28 % of the
DMT pre-injection mean, positive in 10 of 14 subjects. **On ts_demean,
mean pairwise r rises under DMT** (DiD positive and significant on all
three post sets), which is the direction Timmermann et al. 2023 reported
for global functional connectivity. **It does not do so on ts_gsr.** The
sts DiD is negative on both variants on the same bins (ts_gsr −0.0801,
ts_demean −0.1035, primary set). The relationship between the two
quantities is not interpreted here.

**Reconciliation with Timmermann et al. 2023 (recorded 13 Sep 2026).**
On ts_demean, mean pairwise correlation rises under DMT (DiD +0.053
[+0.007, +0.098], p = 0.047, positive in 10 of 14; peak bins 9–14
+0.075, p = 0.005), replicating the global-connectivity increase
Timmermann et al. 2023 reported, while whole-brain synergy on the
identical bins falls (sts DiD −0.104). Zero-lag correlation and lag-1
predictable information move in opposite directions on the same data
and bins. On ts_gsr the comparison is uninformative because GSR pins
the mean correlation near zero by construction. Both conditions show an
injection-locked jump in mean r at bins 8–9 on ts_demean, consistent
with the placebo rtr bump already recorded under Robustness A.

## Exploratory: regional analysis (pre-specified 13 Sep 2026, before any code)

**Status: EXPLORATORY.** Specified after the primary result (Primary B,
whole-brain DiD negative, tier 3) and the global-fit Robustness A results
existed, so it is not a pre-registration in the sense of the sections
above. It is fixed here before any regional number is computed and before
`scripts/11_regional_analysis.py` is written, and **every part of it is
reported regardless of outcome**, labelled exploratory in every table and
figure. No prediction is recorded: none is made. Script is numbered 11
because 10 is the subject-alignment check.

**Data and estimator.** Robustness A global fit (one Gaussian per pair per
run, `calc_PhiID(kind='gaussian', redundancy='MMI', tau=1)`, non-finite TRs
dropped), ts_gsr primary, ts_demean sensitivity (rule 6). The saved atoms
files hold only the pair mean, so the per-pair local atoms are recomputed
with the identical code path and settings as `01_synergy_timecourse.py`
(≈ 9 min per variant). **Per-region synergy** = mean sts over the 114
pairs containing that region, per 30-TR bin, per subject, per condition
(115 regions, region 20 dropped as everywhere); rtr is kept alongside for
the descriptive rank check below. Saved as
`results/regional_atoms_bins_115regions-all_<variant>_global.npy`, shape
(14, 2, 28, 115, 2) for (sts, rtr). No motion handling (Robustness A
status; FD is not regressed at the regional level).

**Per-region contrast.** Per region and subject, DiD = (post bins 11–28
− pre bins 1–8) on DMT minus the same on PCB. Test per region: exact
sign-flip across the 14 subjects, all 2^14 assignments, two-sided.
**Multiple comparisons: Benjamini–Hochberg FDR at q = 0.05 across the 115
regions** (rule 7). Reported: the number of regions surviving FDR and their
sign, the group-mean DiD map (115 values), the per-region p and BH
threshold, and the sign count (how many of 115 group-mean DiDs are
negative). The whole-brain mean of the 115 regional DiDs equals the
whole-brain pair-mean DiD already recorded (each pair enters two regions),
which is checked as an internal consistency test.

**Spatial correlation with 5-HT2A (rule 1).** Spearman ρ between the
group-mean DiD map and `mean5HT2A_sch116` (`5HTvecs_sch116.mat`), region 20
dropped from both.
- **What `external/DMT_NCT/fxns/SpinTests` provides (checked 13 Sep
  2026).** `perm_sphere_p_al857.m` (Váša 2018) takes a precomputed
  `perm_id` array and correlates each permuted map with the unpermuted
  other map in both directions, averaging the two one-sided p-values (in
  the direction of the empirical sign). `rotated_maps/rotated_Schaefer_100.mat`
  (v7.3, read with h5py) holds `perm_id` of shape (10,000, 100), 1-based,
  each row a permutation of the 100 **cortical** Schaefer parcels; the
  rotations map left-hemisphere parcels (indices 0–49) to the left
  hemisphere in 98 % of entries (observed, not assumed). **There is no
  rotated map for the 16 subcortical parcels (indices 100–115, network 8
  in `sch116_to_yeo.csv`) and none can exist**: spin tests rotate points
  on the cortical sphere, and subcortical nuclei have no spherical
  coordinates. `quick_SpinTest.m` says so ("NB must be cortical only").
  Singleton et al. handled it the same way (`03_regional_ce_analyses.m:66`:
  "no subcortex so can spin", `rec_nosub = receptor_vec(1:100)`).
- **Handling fixed here.** (i) **Primary: the spin test is run on the 99
  cortical parcels** (100 minus region 20). Region 20 is set to NaN in
  both maps; each rotation is applied to the 100-parcel vectors and any
  position whose rotated source or target is NaN is dropped from that
  rotation's correlation (the `'rows','complete'` semantics of the MATLAB
  function). All 10,000 rotations, both directions, p as the MATLAB
  function computes it (mean of the two one-sided p in the empirical
  direction) and also the two-sided version (fraction of |ρ_null| ≥ |ρ|),
  which is the one reported as the test. (ii) **The 115-region ρ
  including subcortex is reported as a descriptive number without a p**:
  no spatial null is available for it, and a naive permutation of parcel
  labels ignores spatial autocorrelation, which rule 1 forbids. (iii)
  **Specificity: the same cortical spin test against 5-HT1A, 5-HT1B,
  5-HT4 and 5-HTT** from the same file, five correlations in one table,
  **BH FDR across the five** stated explicitly; the receptor maps are
  inter-correlated (their Spearman correlation matrix is printed), so
  specificity is bounded by that and is described, not claimed.
- Parcel names for the 100 cortical parcels come from
  `data/Schaefer2018_100Parcels_7Networks_order.lut`, downloaded 13 Sep
  2026 from the CBIG repository
  (`stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/MNI/fsleyes_lut/`);
  its network sequence equals the first 100 entries of `sch116_to_yeo.csv`
  exactly (checked), which fixes the parcel order as Schaefer-100
  7-network, LH 0–49, RH 50–99. Region 20 is `LH_DorsAttn_Post_6`. The 16
  subcortical parcel identities are not documented in the source repo and
  are not needed below.

**Workspace comparison (Luppi et al. eLife 2024).**
- **What Luppi et al. define (from the paper, PMC11257694, read 13 Sep
  2026).** The synergistic global workspace is the set of regions "whose
  rank, in terms of strength of synergy with the rest of the brain, is
  greater than the corresponding strength rank for redundancy", computed
  on 100 HCP subjects in the Schaefer-400 + Tian-54 parcellation (454
  ROIs; Schaefer-200 + Tian-32 as robustness). Within the workspace,
  **gateways** have a highly ranked participation coefficient for
  synergistic interactions and **broadcasters** for redundant ones.
  Anatomically: gateways "primarily in the brain's default mode
  network" (bilateral precuneus, medial prefrontal cortex, bilateral
  inferior parietal cortex, left temporal cortex); broadcasters "mainly
  located in the executive control network, especially lateral
  prefrontal cortex". The regions with reduced integrated information
  under propofol and in DoC were DMN gateways (bilateral precuneus, mPFC,
  bilateral inferior parietal). **No region list or count is published**;
  the map exists only as figures.
- **Mapping onto Schaefer-116, fixed here.** Because the workspace is a
  data-driven rank rule on a different parcellation and is available only
  as a figure, it is mapped at the network level using the Yeo-7 labels
  the parcellation carries:
  - **Workspace proxy (primary): Yeo Default ∪ Control = 24 + 13 = 37
    cortical parcels.** Gateway proxy = the 24 Default parcels;
    broadcaster proxy = the 13 Control parcels.
  - **Named-subregion proxy (sensitivity), closest to the text:** gateways
    = Default `pCunPCC` (4), Default `PFC` / `PFCv` / `PFCdPFCm` (12),
    Default `Par` (3), and left-hemisphere Default `Temp` (2) = 21
    parcels; broadcasters = Control `PFCl` (5 parcels). Workspace = 26.
  - **Non-workspace = the remaining cortical parcels** (62 for the
    primary proxy, 73 for the named proxy). The 16 subcortical parcels
    are excluded from the comparison in the primary form and included in
    the non-workspace set as a sensitivity, because Luppi et al.'s named
    workspace regions are all cortical while their parcellation did
    include subcortex.
  - **Limitations, recorded now:** (1) a network atlas is a proxy for a
    rank rule computed on other subjects at 4× the resolution; (2)
    Schaefer-100 parcels are large, so precuneus, PCC, mPFC and IPL are
    each one or two parcels and "inferior parietal" vs "Control Par"
    boundaries are atlas conventions; (3) the gateway / broadcaster split
    depends on participation coefficients we do not compute; (4) the
    proxy is fixed by atlas labels, not by any quantity from these data,
    so it involves no selection on the tested effect (rule 3).
- **Statistic.** Per subject: mean regional DiD over workspace parcels
  minus mean over non-workspace parcels; exact sign-flip test across 14
  subjects, two-sided; subject-bootstrap 95 % CI (10,000 draws, seed
  20261120). Reported for the primary proxy, the named proxy, and each of
  gateway proxy vs non-workspace and broadcaster proxy vs non-workspace;
  also the workspace and non-workspace group means with CIs. **Sign
  convention: a negative difference means the DMT synergy decrease is
  larger (more negative) in the workspace proxy than outside it.**
- **Descriptive check of whether these data reproduce the rank rule at
  all (no test, no selection).** Per region, mean sts strength and mean
  rtr strength over the **placebo run, all 28 bins, 14-subject mean**;
  rank each across the 115 regions; a region is "rank-rule workspace" if
  its synergy rank exceeds its redundancy rank. Reported: the count, the
  overlap with the network proxy (count and Jaccard index), and the
  Yeo-network composition of the rank-rule set. This is reported to show
  how far the proxy and the rule agree on these data; it is **not** used
  to define the workspace for the test above (it would share subjects
  with the tested contrast).
- **What this permits.** Only a sentence of the form "the DMT decrease in
  whole-brain synergy is / is not concentrated in a network-level proxy of
  the Luppi et al. synergistic workspace", with the proxy's limitations
  stated. It does **not** permit "synergy falls under DMT as it does under
  propofol / in DoC": Luppi et al. report integrated information (ΦR) on
  workspace regions, a different quantity, and the states differ. The
  caution recorded under Robustness A stands.

**Predictions recorded before running: none** (exploratory).

**Outputs.** `results/regional_analysis_<variant>.csv` (all tables),
`results/regional_atoms_bins_115regions-all_<variant>_global.npy`,
`results/regional_did_map_<variant>.csv` (115 rows: index, name, network,
group-mean DiD, p, BH-significant), log `results/run_11_<variant>.log`.
Seed 20261120; git SHA in every header. Run order: ts_gsr, then ts_demean.
The script is written after this entry is committed and is not run until
instructed.

**Outcome (both variants run 13 Sep 2026; every table header reads
`git=4f7437b`, the commit of the script; results committed at d76d758;
values verbatim from `results/regional_analysis_<variant>.csv`,
`results/regional_did_map_<variant>.csv` and the logs
`results/run_11_<variant>.log`). EXPLORATORY, Robustness A status: global
fit, no temporal null, no motion handling, 14-subject group means of the
per-region pair-mean; DiD in nats, pre bins 1–8, post bins 11–28; exact
sign-flip over 2^14 assignments, two-sided; BH FDR at q = 0.05 across
the 115 regions; spin test on the 99 cortical parcels, 10,000 rotations,
two-sided p reported; subject-bootstrap 95 % CI, 10,000 draws, seed
20261120.**

- **Consistency check.** Max |mean over regions − saved whole-brain
  pair-mean| per subject, condition and bin: sts **2.22e-15** on both
  variants, rtr 1.11e-16 (ts_gsr) / 3.05e-16 (ts_demean) (from the log;
  the CSV rounds these to 0.000000). Mean over the 115 regional DiDs:
  −0.080081 (ts_gsr) and −0.103471 (ts_demean), equal to the whole-brain
  pair-mean DiDs on the same bins recorded under `09_global_fc_per_bin.py`
  (−0.0801, −0.1035).

- **Per-region DiD.** Group-mean DiD negative in **114 of 115** regions on
  both variants; the one positive region is subcortical parcel index 104
  on both (`SUB_5`, +0.028, p = 0.495, 7 of 14 negative on ts_gsr;
  +0.019, p = 0.566, 6 of 14 on ts_demean). **BH FDR survivors: 7 on
  ts_gsr (p threshold 0.00304), 19 on ts_demean (0.00826), all negative,
  all cortical, 0 subcortical.** Minimum uncorrected p is
  `LH_Default_Par_1` on both variants (0.000244 / 0.000854).

  ts_gsr, 7 regions (index, Yeo network, DiD, p, negative subjects of 14):

  | region | idx | net | DiD | p | neg |
  |---|---|---|---|---|---|
  | LH_DorsAttn_Post_2 | 16 | 3 | −0.147383 | 0.00073 | 13 |
  | LH_DorsAttn_PrCv_1 | 21 | 3 | −0.143504 | 0.00269 | 12 |
  | LH_Default_Par_1 | 39 | 7 | −0.168352 | 0.00024 | 13 |
  | RH_SomMot_3 | 60 | 2 | −0.103882 | 0.00195 | 12 |
  | RH_SomMot_8 | 65 | 2 | −0.116150 | 0.00256 | 11 |
  | RH_SalVentAttn_TempOccPar_2 | 74 | 4 | −0.105710 | 0.00183 | 13 |
  | RH_Default_Temp_3 | 92 | 7 | −0.152747 | 0.00085 | 13 |

  ts_demean, 19 regions:

  | region | idx | net | DiD | p | neg |
  |---|---|---|---|---|---|
  | LH_Vis_3 | 2 | 1 | −0.159528 | 0.00623 | 11 |
  | LH_Vis_4 | 3 | 1 | −0.133486 | 0.00562 | 11 |
  | LH_Vis_6 | 5 | 1 | −0.182763 | 0.00745 | 12 |
  | LH_Vis_8 | 7 | 1 | −0.122007 | 0.00806 | 12 |
  | LH_Vis_9 | 8 | 1 | −0.158145 | 0.00427 | 11 |
  | LH_SomMot_4 | 12 | 2 | −0.107238 | 0.00598 | 11 |
  | LH_DorsAttn_Post_2 | 16 | 3 | −0.151416 | 0.00293 | 12 |
  | LH_DorsAttn_Post_4 | 18 | 3 | −0.135552 | 0.00134 | 12 |
  | LH_DorsAttn_PrCv_1 | 21 | 3 | −0.164079 | 0.00220 | 12 |
  | LH_DorsAttn_FEF_1 | 22 | 3 | −0.162117 | 0.00317 | 12 |
  | LH_Cont_pCun_1 | 35 | 6 | −0.127629 | 0.00708 | 12 |
  | LH_Default_Par_1 | 39 | 7 | −0.137965 | 0.00085 | 13 |
  | LH_Default_pCunPCC_1 | 48 | 7 | −0.159728 | 0.00256 | 12 |
  | RH_Vis_5 | 54 | 1 | −0.123981 | 0.00562 | 12 |
  | RH_Vis_7 | 56 | 1 | −0.122318 | 0.00732 | 11 |
  | RH_Vis_8 | 57 | 1 | −0.144144 | 0.00159 | 12 |
  | RH_SalVentAttn_TempOccPar_2 | 74 | 4 | −0.105911 | 0.00818 | 12 |
  | RH_Default_PFCv_2 | 94 | 7 | −0.133180 | 0.00525 | 12 |
  | RH_Default_pCunPCC_1 | 98 | 7 | −0.114772 | 0.00781 | 12 |

  **Four regions survive FDR on both variants: LH_DorsAttn_Post_2 (16),
  LH_DorsAttn_PrCv_1 (21), LH_Default_Par_1 (39) and
  RH_SalVentAttn_TempOccPar_2 (74).** Exploratory; not selected for any
  further test (rule 3).

- **Receptor maps: NULL. Nothing survives BH across the five maps on
  either variant** (`bh_threshold_across_5_maps` = 0 on both). Spearman ρ
  on the 99 cortical parcels, two-sided spin p (Váša one-sided-average p
  in brackets); the 115-region ρ including subcortex is descriptive only,
  no p:

  | map | ts_gsr ρ (p) [Váša p] | 115-region ρ | ts_demean ρ (p) [Váša p] | 115-region ρ |
  |---|---|---|---|---|
  | 5-HT2A | **−0.160** (0.116) [0.070] | −0.230 | **−0.055** (0.677) [0.360] | −0.263 |
  | 5-HT1A | +0.009 (0.929) [0.467] | −0.099 | **+0.265** (0.032) [0.012] | +0.038 |
  | 5-HT1B | −0.094 (0.352) [0.185] | −0.144 | −0.263 (0.050) [0.033] | −0.314 |
  | 5-HT4 | −0.084 (0.422) [0.228] | +0.008 | +0.182 (0.160) [0.066] | +0.231 |
  | 5-HTT | +0.104 (0.324) [0.145] | +0.196 | +0.202 (0.096) [0.039] | +0.365 |

  Spin-null SD 0.100–0.106 (ts_gsr), 0.122–0.135 (ts_demean). The
  largest uncorrected value is 5-HT1A +0.265 (p = 0.032) on ts_demean,
  which does not survive BH and is not replicated on ts_gsr (+0.009).
  **The two variants disagree on the sign of the 5-HT1A, 5-HT4 and
  5-HTT correlations and on the magnitude of 5-HT2A and 5-HT1B**;
  none is significant after correction on either. Receptor
  inter-correlations (Spearman, identical on both variants since the
  maps are variant-independent): 1A–2A 0.532, 1B–2A 0.528, 2A–4 0.436,
  2A–HTT −0.451, 1A–4 0.405, 1B–HTT −0.364, 1A–HTT −0.100, 4–HTT 0.068,
  1B–4 0.056, 1A–1B −0.002; specificity is bounded by these and is not
  claimed.

- **Workspace comparison: the DMT synergy decrease is spatially uniform,
  not workspace-concentrated, on both variants and both proxies.**
  Per-subject workspace minus non-workspace mean regional DiD (negative =
  larger decrease inside the proxy); non-workspace = remaining cortical
  parcels (primary) or remaining cortical + 16 subcortical (sensitivity):

  | proxy | non-workspace set | ts_gsr Δ [CI], p, neg | ts_demean Δ [CI], p, neg |
  |---|---|---|---|
  | primary (Default ∪ Control, 37) | cortical (62) | **−0.0095 [−0.0230, +0.0050], 0.216**, 9/14 | **−0.0050 [−0.0225, +0.0120], 0.590**, 7/14 |
  | primary | + subcortex (78) | −0.0124 [−0.0264, +0.0024], 0.130, 10/14 | −0.0119 [−0.0300, +0.0063], 0.242, 8/14 |
  | named subregion (26) | cortical (73) | −0.0108 [−0.0305, +0.0099], 0.325, 8/14 | −0.0070 [−0.0305, +0.0170], 0.583, 8/14 |
  | named | + subcortex (89) | −0.0135 [−0.0337, +0.0074], 0.235, 9/14 | −0.0130 [−0.0363, +0.0110], 0.318, 9/14 |

  Both sets are individually significant and of similar magnitude:
  primary proxy vs cortical non-workspace, ts_gsr, workspace mean DiD
  −0.0885 [−0.1457, −0.0329] p = 0.0078 and non-workspace −0.0791
  [−0.1299, −0.0290] p = 0.0083; ts_demean −0.1115 [−0.1816, −0.0375]
  p = 0.0131 and −0.1065 [−0.1722, −0.0392] p = 0.0118. Named proxy:
  ts_gsr −0.0905 / −0.0798 (p 0.0087 / 0.0084); ts_demean −0.1135 /
  −0.1066 (p 0.0137 / 0.0123). Gateway proxy minus non-workspace
  (primary proxy, cortical): ts_gsr −0.0189 [−0.0356, −0.0012] p = 0.060
  (10/14); with subcortex −0.0219 [−0.0399, −0.0028] p = 0.047 (9/14);
  ts_demean −0.0094 [−0.0315, +0.0129] p = 0.442 and −0.0163 [−0.0392,
  +0.0078] p = 0.211. Broadcaster proxy minus non-workspace: ts_gsr
  +0.0079 p = 0.474, ts_demean +0.0030 p = 0.813. Gateway minus
  broadcaster: ts_gsr −0.0268 [−0.0514, −0.0007] p = 0.072, ts_demean
  −0.0124 [−0.0436, +0.0183] p = 0.459. Named proxy: gateway minus
  non-workspace ts_gsr −0.0155 p = 0.202, ts_demean −0.0086 p = 0.525;
  broadcaster minus non-workspace +0.0091 p = 0.598 and −0.0002
  p = 0.993; gateway minus broadcaster −0.0246 p = 0.189 and −0.0084
  p = 0.715. The proxy limitations recorded above apply in full: a
  Yeo-network atlas standing in for a rank rule computed on other
  subjects at 4× the resolution, with no participation coefficients.

- **Rank-rule check on the placebo run (descriptive; not used for
  selection).** Regions whose placebo synergy rank exceeds their
  redundancy rank: **52 of 115 on ts_gsr** (45 cortical, 7 subcortical),
  **58 on ts_demean** (51 cortical, 7 subcortical). Overlap with the
  37-parcel primary proxy: 20 (Jaccard 0.323) on ts_gsr, 32 (Jaccard
  0.571) on ts_demean. Spearman correlation between the sts rank and the
  rtr rank across the 115 regions: 0.392 (ts_gsr), 0.115 (ts_demean).
  Yeo composition of the rule set (count of network size): ts_gsr Vis
  7/17, SomMot 2/14, DorsAttn 9/14, SalVentAttn 3/12, Limbic 4/5, Cont
  8/13, Default 12/24, Subcortex 7/16; ts_demean Vis 4/17, SomMot 0/14,
  DorsAttn 6/14, SalVentAttn 4/12, Limbic 5/5, Cont 12/13, Default
  20/24, Subcortex 7/16. On the DMT run (reported alongside, descriptive):
  45 rule regions on ts_gsr with 106 of 115 regions keeping their
  placebo membership; 62 on ts_demean with 93 of 115 unchanged. The rule
  set agrees with the network proxy more closely without GSR than with it.

- **What this permits (recorded 13 Sep 2026).** The Luppi et al. eLife
  2024 comparison can now be made as a **dissociation**: the synergy
  reduction under propofol and in disorders of consciousness is
  workspace-concentrated per Luppi et al. 2024, whereas the DMT synergy
  decrease here is spatially uniform (114 of 115 regions negative, no
  detectable workspace-vs-non-workspace difference on either variant or
  proxy). This is qualified by the proxy limitation (a network-level
  atlas proxy, not the rank-rule workspace) and by the exploratory status
  of this section. It still does not license "synergy falls under DMT as
  it does under propofol / in DoC": Luppi et al. report ΦR on workspace
  regions, a different quantity, and the states differ.

## Open questions to resolve

- Confirm reuse licence with Singleton / Timmermann before publishing.
- Ask the data authors to confirm that the timeseries subject order (rows
  of the (14, 2) cell) matches the 14 ratings IDs recovered from
  `intensity_ratings.mat` (the 14 codes (not reproduced), in that order),
  and that the FD and LZ files share it. See the subject-alignment
  section: verified for timeseries–FD (one subject) and timeseries–LZ,
  plausible only for the ratings.
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

## Correction note, 14 Sep 2026 (appended; nothing above edited)

Two lines above call `external/DMT_NCT/` a "submodule": the "Data" section
dated 11 Sep 2026 ("the submodule checkout") and the file-creation-dates
bullet of "Subject alignment across files (checked 13 Sep 2026)" ("the
submodule has a single squashed commit"). It is not a git submodule: this
repository has no `.gitmodules`, and `external/` is git-ignored. It is a
plain clone, `git clone https://github.com/singlesp/DMT_NCT.git
external/DMT_NCT`, as `run_all.sh` and `README.md` describe, checked at
upstream commit 77af7aa. The upstream clone has 1 commit on its
history, so the "single squashed commit" statement stands. Both
lines are left as written because they sit inside dated entries; nothing
else in either entry changes.

## Closure entry, 14 Sep 2026 (appended; nothing above edited): the search for a positive DMT finding is closed

Written after the 14 Sep 2026 adversarial review (`notes/adversarial_review_2026-09-14.md`),
the review computations (`notes/review_computations_2026-09-14.md`) and the pre-specified
regional ΦR check (`notes/prespec_regional_phir_deconv_2026-09-14.md`,
`notes/regional_phir_deconv_2026-09-14.md`). Every number below is quoted from those files
and their CSVs.

1. Regional ΦR against the recorded prediction. Prediction (fixed 11:37 UTC, before any
   regional number): if the deconvolved ΦR increase reflected the workspace structure of
   Luppi et al. (2024), the per-region increase would be larger inside the Default/Control
   proxy than outside it. Observed (deconvolved, ts_gsr, W = 60): workspace minus
   non-workspace cortex −0.0047 [−0.0079, −0.0013], exact sign-flip p = 0.023, positive in
   4 of 14 subjects — opposite in sign to the prediction, and in neither recorded branch
   (not the predicted positive difference; not "uniform or absent", since the difference is
   distinguishable from zero and three regions survive FDR). 82 % of it comes from the
   Control sub-proxy (−0.0109, p = 0.004; Default −0.0013, p = 0.53). It is present in the
   placebo run's change (inside − outside +0.0054 [+0.0020, +0.0090], p = 0.014) and absent
   from the DMT run's (+0.0007 [−0.0012, +0.0026], p = 0.49).

2. Why the whole-brain deconvolved ΦR increase (+0.0178 [+0.0069, +0.0293], p = 0.0099,
   W = 60, ts_gsr) supports no claim:
   (a) the pre-injection baseline gap runs in the direction that creates a positive DiD: DMT
       0.1193 vs placebo 0.1317, −0.0124 [−0.0210, −0.0042], p = 0.014, DMT lower in
       12 of 14 subjects;
   (b) the placebo run declines across the session (linear slope −0.00115 per window,
       p = 0.025, negative in 10 of 14; window 1 → 4: 0.1375, 0.1338, 0.1300, 0.1256, i.e.
       already within the pre-injection windows, −0.0120, p = 0.067), while the DMT run has
       no trend (slope −0.00003, p = 0.90);
   (c) both the gap and the slope are absent on the raw series (gap −0.0042, p = 0.28;
       slope −0.00036, p = 0.43): deconvolution creates them.
   In addition: the two estimators disagree (global fit −0.0032 [−0.0100, +0.0046],
   p = 0.41 on the same deconvolved ts_gsr series), and the placebo run's fall carries
   56–64 % of the DiD (64 % at W = 60, 56 % at W = 30). Contrast with sts, where the
   baseline imbalance runs against the finding: DMT pre-injection sts 1.1554 vs placebo
   1.1378 (+0.0176 [−0.0106, +0.0421], p = 0.23, DMT higher in 10 of 14), against a DiD
   of −0.0809.

3. ΦR (in place of sts), HRF deconvolution and the W = 60 estimator for ΦR were each chosen
   after seeing results. No confirmatory claim attaches to any of them, or to any outcome of
   the regional check.

4. No further specification will be run in search of a positive DMT result.

## Part B, items 6–8: pre-run entry, 15 Sep 2026 07:30 UTC (appended; nothing above edited)

Written in response to `notes/adversarial_review_draft_v2_2026-09-15.md` (sections 1.5, 5–6, 9.2),
before any number below was computed. Scripts `notes/partB6_ccs_definition.py`,
`notes/partB7_splithalf.py`, `notes/partB8_coupling_map.py`; outputs under `notes/review_results/`.
Standing rule of Part B unchanged: nothing here is a route back to a DMT-specific claim; the rule
of the closure entry (item 4) stands. Every outcome is reported regardless.

**B6. The CCS double-redundancy definition (check first, then use).** The 14 Sep review found
that phyid's CCS double redundancy keeps the double co-information D at the samples where the
signs of I_xta, I_xtb, I_yta, I_ytb and D agree, whereas the published definition (Mediano et
al., arXiv:2109.13186v1, Appendix, Definition 1; the PNAS 2025 text is not accessible from this
session) reads: "the double-redundancy based on common change in surprisal is defined as
I_∂,CCS^{{1}{2}→{1}{2}} := Σ_{i∈S} c(x^(i); y^(i))", with S "the subset of samples for which all
marginal pointwise mutual informations, as well as the pointwise full mutual information
i(x; y), have the same sign", and c the pointwise co-information summed over the product lattice
"excluding the lowest node". Reading adopted, fixed now: the marginal pointwise MIs are the four
i(x_i; y_j) between one past and one future variable (I_xta, I_xtb, I_yta, I_ytb); the full
pointwise MI is i(x; y) = I_xytab; c(x; y) is the code's D (checked algebraically: Eq. (5)'s
signed sum over the 15 non-bottom lattice nodes is the code's expression term by term, with
(−1)^{f+1} giving −I_xta, +I_xyta, −I_xytab, +R_xyta, −R_xytab, +R_abtx, −R_abtxy). So the
published mask is sign(I_xta) = sign(I_xtb) = sign(I_yta) = sign(I_ytb) = sign(I_xytab) and the
code's mask replaces I_xytab by D. Two other readings are computed as sensitivity only and decide
nothing: (i) all eight partial MIs (the four above plus I_xtab, I_ytab, I_xyta, I_xytb) plus
I_xytab; (ii) the published five signs plus sign(D). The single-target CCS redundancies (Ince
2017, four-sign rule including the co-information) are unchanged in every version.
Computation: on the same (subject, run, window, pair) samples, CCS atoms under the published mask
and under phyid's mask, W = 60 (per-window fit) and the global fit (30-TR bins), `ts_gsr` and
`ts_demean`, whole-brain pair means; the full inference engine (`rev_inference.py`) on the
published-mask CCS sts, xtx + yty and rtr; the 16-atom table and the per-subject correlations of
`partB2_ccs_run.py` repeated under the published mask.
Rule, fixed now: the two definitions "agree on these data" if every whole-brain CCS-sts level and
primary DiD (four cells) differs by less than 0.001 nats and no sign-flip p crosses 0.05 between
them; then phyid's numbers stand and the agreement is stated. Otherwise every CCS number in the
manuscript (Table 1, Table 4, Results 3, Discussion) is replaced by the published-definition
value, and phyid's values are reported beside them in `ccs_pub_tables.md` as the code's variant.
No CCS number is quoted in the manuscript until this has run. Expectation, not a prediction: the
masks select different samples, so sample-level atoms will differ; whether whole-brain means
differ materially is unknown.

**B7. Split-half test of the CCS-sts / residual correlation.** The review found, from the
committed per-subject DiDs, r(residual DiD, CCS-sts DiD) = +0.729 (ts_gsr W60) and +0.838
(ts_demean W60), surviving partialling out the autocorrelation DiD (+0.688, +0.820). Both
quantities are functions of the same per-window 4 × 4 matrices, so the shared variance may be a
common signal or common estimation noise in the same windows. Test, fixed now: recompute both
per-subject DiDs on odd windows only (pre {1, 3}, post {7, 9, 11, 13}) and on even windows only
(pre {2, 4}, post {6, 8, 10, 12, 14}); window 5 stays excluded. Report the within-half
correlations r(CCS_odd, res_odd), r(CCS_even, res_even) and the cross-half correlations
r(CCS_odd, res_even), r(CCS_even, res_odd), both variants, with and without partialling out the
autocorrelation DiD of the same half; CCS-sts under the definition selected by B6 (phyid's values
alongside). Common window noise cannot correlate across disjoint windows; a common signal can.
Decision rule, fixed now, on `ts_gsr` W = 60 (`ts_demean` reported as sensitivity): the shared
component is NOT window noise if both cross-half correlations are positive and their mean is at
least half the mean within-half correlation; then the residual and the CCS-sts change are
reported together as one exploratory observation of an autocorrelation-independent component
whose sign matches the original pre-specified direction, with the explicit statement that it
arose after four specification changes (windowed sts → sixteen atoms → CCS → diagnostic
residual) and requires an independent dataset. The shared component IS estimation noise if the
mean cross-half correlation is below half the within-half mean or either cross-half correlation
is negative; then both are reported as null with this test as the evidence. Either outcome is
exploratory; neither becomes a headline. Cross-half correlations are attenuated by the
half-length windows exactly as the within-half ones are, which is why the comparison is
within-half against cross-half and not against the full-set r = 0.73.

**B8. The family with lagged coupling (analytic, no data).** For the symmetric VAR(1) pair
x_{t+1} = a x_t + c y_t + ε_{t+1}, y_{t+1} = a y_t + c x_t + η_{t+1}, corr(ε, η) = q_ε, the
stationary covariance (discrete Lyapunov) and the lag-1 covariance give the population 4 × 4
matrix in closed form; all 16 Gaussian-MMI atoms, sts − (xtx + yty), the six cross-prediction
atoms and the population residual of the B4 diagnostic (sts of the true matrix minus sts of the
AR(1)-substituted matrix built from the true a_x, a_y, q) are tabulated over c ∈ [−0.3, 0.3] at
the data's operating point and at two others. Purpose: to state what lagged interaction does to
sts relative to r₁, what the diagnostic returns when true coupling exists, and what spread of
pair-specific coupling of either sign would produce a run-level residual of −0.01 nats. No
prediction.

## Part B, items 6–8: outcomes, 15 Sep 2026 07:55 UTC (appended; nothing above edited)

Scripts as named in the pre-run entry, run once each after it was written; every number below
is quoted from `notes/review_results/partB/ccs_pub_tables.md`, `ccs_definition_check.log`,
`notes/review_results/inference_rows_ccs_pub.csv`, `splithalf_tables.md`, `splithalf.log` and
`coupling_map_tables.md`. Nothing in the pre-run entry was changed after these numbers existed.

**B6 outcome: the two definitions DIFFER on these data; the rule's second branch applies.**
Whole-brain CCS-sts, published mask (Definition 1) against phyid's mask, DMT pre-injection level
and primary DiD with sign-flip p:

| cell | level pub / code | primary DiD pub / code | p pub / code | verdict (rule: |Δ| < 0.001 nats in both and no p crossing 0.05) |
|---|---|---|---|---|
| ts_gsr W60 | −0.0480 / −0.0387 | +0.0044 / +0.0036 | 0.0559 / 0.0844 | differs (level Δ 0.0094) |
| ts_gsr global | −0.0358 / −0.0335 | +0.0197 / +0.0210 | 0.0002 / 0.0001 | differs (level Δ 0.0023, DiD Δ 0.0014) |
| ts_demean W60 | −0.0378 / −0.0255 | +0.0120 / +0.0134 | 0.0040 / 0.0052 | differs (level Δ 0.0122, DiD Δ 0.0014) |
| ts_demean global | −0.0386 / −0.0297 | +0.0355 / +0.0321 | 0.0001 / 0.0001 | differs (level Δ 0.0088, DiD Δ 0.0034) |

Per-subject r(pub DiD, code DiD) 0.974, 0.992, 0.991, 0.956; the masks disagree on 6.3 % and
6.6 % of samples in the two per-pair test windows (subject 1, DMT window 6 and PCB window 2),
the published mask selecting 32–34 % of samples against the code's 26–28 %. Consequence, as
fixed in the pre-run entry: every CCS number in the manuscript (Table 1, Table 4, Results 3,
Discussion) is the published-definition value; phyid's values stand beside them in
`ccs_pub_tables.md` as the code's variant. Qualitative statements unchanged under either mask:
CCS-sts is near zero and negative at baseline; its primary DiD is positive in all four cells
(ts_gsr W60 +0.0044 [+0.0004, +0.0081], sign-flip p = 0.0559, phase p = 0.006, positive in
11/14, FD-residualised +0.0039 [+0.0005, +0.0073]; ts_gsr global +0.0197 [+0.0142, +0.0254],
p = 0.0002, phase p = 0.001, positive in 13/14, FD-residualised +0.0152; ts_demean W60 +0.0120
[+0.0054, +0.0192], p = 0.0040; ts_demean global +0.0355 [+0.0231, +0.0485], p = 0.0001,
positive in 14/14); at the ts_gsr global fit the DMT run rises (+0.0122, p < 0.001) and the
placebo run falls (−0.0075, p = 0.001). CCS-sts does not track r₁: per pair within a window
r = −0.011 and −0.018 (MMI sts +0.742, +0.697); per subject r(CCS-sts DiD, autocorrelation DiD)
= −0.420, −0.275, −0.428, −0.297 (p ≥ 0.127); across the 28 condition-window means −0.639
(MMI +0.977). CCS xtx + yty keeps the MMI values and tracks r₁ (r = +0.949, +0.963, +0.917,
+0.921). Per subject the CCS-sts DiD correlates with the B4 residual DiD at +0.799 (p = 0.001,
ts_gsr W60), +0.094 (ts_gsr global), +0.875 (ts_demean W60), +0.676 (ts_demean global). The two
sensitivity readings (eight partial MIs + full MI; published five signs + sign(D)) give ts_gsr
W60 sts −0.0468 / +0.0044 and −0.0425 / +0.0038; they decide nothing and are not quoted in the
manuscript.

**B7 outcome: the estimation-noise branch of the rule applies; both are reported as null.**
ts_gsr W60, published CCS: within-half r(CCS_odd, res_odd) = +0.847, r(CCS_even, res_even) =
+0.783 (mean +0.815); cross-half r(CCS_odd, res_even) = +0.160, r(CCS_even, res_odd) = +0.478
(mean +0.319; ratio 0.39, below the 0.50 threshold). Partialling out the same-half
autocorrelation DiD: within +0.815, cross +0.154 (ratio 0.19). Under the rule (mean cross-half
below half the within-half mean) the shared per-subject component of the residual DiD and the
CCS-sts DiD is estimation noise common to the same windows, and the two are reported as null
with respect to an autocorrelation-independent component, with this test as the evidence.
Sensitivity, ts_demean W60: within +0.881, cross +0.283 (ratio 0.32); partialled 0.849 / 0.287
(0.34); same branch. phyid's CCS: ts_gsr ratio 0.30 (partialled 0.02); ts_demean 0.38 (0.41).
Limitation of the test, stated so that the null is not over-read: the split-half reliabilities of
the two quantities are low (ts_gsr: residual DiD +0.494, published CCS-sts DiD +0.302;
ts_demean: +0.216, +0.417; for comparison autocorrelation DiD +0.741 / +0.712, MMI-sts DiD
+0.717 / +0.686), so the largest cross-half correlation two perfectly correlated reliable
components could show is √(0.494 × 0.302) = 0.39 on ts_gsr and 0.30 on ts_demean, and the
observed means (0.32, 0.28) sit at that ceiling. The test therefore establishes that most of the
within-half correlation is shared window noise and that the reliable components of both
quantities are small; it cannot establish that no reliable shared component exists. Both
quantities' group-mean DiDs are positive in both halves (residual odd +0.0067 / even +0.0164;
CCS-sts odd +0.0033 / even +0.0054). The recorded rule is applied as written; the ceiling is
reported beside the verdict wherever the verdict is quoted.

**B8 outcome (analytic).** Symmetric VAR(1) with lagged coupling c, (r₁, q) held at the
operating point (0.85, 0.25) by re-solving a and q_ε for each c: sts changes with c at fixed
(r₁, q) with slope −1.77 nats per unit c at c = 0 and curvature +40.3 nats per unit c²; the six
cross-prediction atoms stay at zero for every c (the symmetric family with equal coefficients
keeps the block structure that zeroes them); sts − (xtx + yty) equals rtr only at c = 0, falls
below it for c > 0 (c = +0.02: +0.0045 against rtr 0.0275; +0.05: +0.0032 against 0.0348) and
exceeds it for c < 0 (−0.02: +0.0586 against 0.0191); the population cross-lag correlation
departs from a_y q by ≈ +0.94 c. The population residual of the B4 diagnostic is 0 at c = 0, −0.027 at
c = +0.02, −0.043 at +0.05, +0.044 at −0.02 and +0.152 at −0.05. A zero-mean spread of
pair-specific coupling of SD σ_c gives an expected residual of +20 σ_c² at fixed (r₁, q), i.e.
positive: it cannot produce the run-level residual of −0.01 nats, which would require a positive
mean coupling of about +0.006 and a positive mean cross-lag deviation of about +0.006, whereas
the measured deviations have mean +0.00014 (`residual_source.log`). At (0.85, 0) the slope is 0
and the curvature +36.9; at (0.6, 0.25) the slope is −0.61 and the curvature +3.2. In the raw
view (a, q_ε fixed, c varied) ∂sts/∂c ≈ −1.3 to −1.5 at (0.85, 0.25) against ∂sts/∂r₁ ≈ +6.
Reported in the manuscript's Methods (family), Results 4 (residual) and Discussion; no data
claim rests on it.

## Correction note, 15 Sep 2026 10:05 UTC (appended; nothing above edited): the B7 rule, the finite-sample null, proportionality in the manuscript, and the title

Written after the third adversarial review (`notes/adversarial_review_draft_v2_second_pass_2026-09-15.md`).
The pre-run entry (07:30 UTC) and the outcomes entry (07:55 UTC) of items 6–8 stand as written; this
entry records what they got wrong and how `manuscript/draft_v2.md` now reads. Every number below is
quoted from `notes/review_results/partB/splithalf_tables.md`, `splithalf.log`,
`notes/review_results/logs/review_v2_residual_null.log`, `results/proportionality.csv` and the third
review's appendix.

1. **B7 rule: the pass criterion was unreachable, a flaw in the rule as recorded.** The pre-run entry
   fixed the "NOT window noise" branch as: both cross-half correlations positive and their mean at least
   half the mean within-half correlation. That threshold was set without reference to the split-half
   reliabilities of the two quantities. At the reliabilities observed (`ts_gsr`: residual DiD +0.494,
   published CCS-sts DiD +0.302) the largest cross-half correlation two perfectly correlated reliable
   components could show is √(0.494 × 0.302) = 0.386, and the threshold was 0.5 × 0.815 = 0.407; on
   `ts_demean` the ceiling is √(0.216 × 0.417) = 0.300 against a threshold of 0.5 × 0.881 = 0.44. The
   "not window noise" branch could not be reached whatever the truth, because shared window noise inflates
   the within-half correlation that the threshold is defined against. The outcome entry's verdict ("the
   estimation-noise branch of the rule applies; both are reported as null") is therefore superseded: the
   manuscript reports the test as **undetermined**. The observed mean cross-half correlation (+0.319; +0.160
   and +0.478, p = 0.585 and 0.084) sits at the ceiling and disattenuates to 0.319 / 0.386 = 0.82, which is
   consistent with a shared reliable component; the reliabilities are too low to distinguish that from a
   partial one or, at N = 14, from none. What the test does establish is that most of the within-half
   correlation (0.815 against a ceiling of 0.386) is estimation noise common to the same windows and that
   the reliable part of each quantity is small. Nothing is promoted: the residual and the CCS-sts change
   stay exploratory, they arose after four specification changes (windowed sts → sixteen atoms → CCS →
   diagnostic residual), no autocorrelation-independent component is reported, and a pre-specified test on
   an independent dataset remains the resolution. The outcome entry's "Limitation of the test" paragraph
   was written after the verdict and is a post-outcome qualification; that is recorded here too. Rule of
   the closure entry (item 4) unchanged.

2. **Finite-sample null of the B4 residual (`notes/review_v2_residual_null.py`): provenance and range.**
   This computation belongs to the second adversarial review (`notes/adversarial_review_draft_v2_2026-09-15.md`,
   Appendix B). It was written and run during that review, before the pre-run entry of items 6–8, and has
   no pre-run entry and no recorded rule in this record. The manuscript draft of 15 Sep (morning) described
   it as one of the additions "with their rules recorded before they were run (record, 'Part B, items
   6–8')"; that sentence was wrong and is corrected: the additions with pre-recorded rules are B6 and B7,
   B8 was entered with no prediction, and the null is reported as a review computation. The third review
   re-ran the script unchanged (it reproduces: four-cell levels −0.0353, −0.0313, −0.0350, −0.0364; DiD
   +0.0054) and varied two of its free choices: per-pair filter heterogeneity SD 0.25 / 0.5 / 1.0 of the
   mean → null DiD +0.0059 / +0.0052 / +0.0077; placebo ACF shape in every cell with the operating points
   unchanged → +0.0037 (1,500 pairs × 25 windows per cell; Monte-Carlo error about ±0.001). The manuscript
   quotes the range, a third to two-thirds of the observed +0.0115 [+0.0021, +0.0211], in place of "about
   half", and states that the rest, and the run-level residual (−1.1 % against the null's −0.34 %), are not
   accounted for by the null as specified. The null is stationary by construction; the runs are not
   (injection at TR 240 on DMT; r₁ and variance drift on placebo). The third review names pooling of
   segments with co-varying a and q under a single run-level fit as a candidate mechanism for the run-level
   residual; it has not been tested (the run-level mean cross-lag deviation is not among the saved outputs),
   and no claim rests on it. "A systematic departure ... exists" is withdrawn from the manuscript.

3. **Proportionality (`results/proportionality.csv`, four pre-specified cells; rule in `14_proportionality.py`).**
   The 15 Sep morning draft's Results 3 quoted the W = 60 `ts_gsr` cell only and read it as a confirmation
   of the mechanism. The main text now reports all four cells, as `draft.md` and Table S8 did: proportional
   at W = 60 on both variants and at the global fit on `ts_demean`; less than proportional at the global fit
   on `ts_gsr` (+0.0204 [+0.0048, +0.0340], p = 0.0248; sts's share of the TDMI drop 0.658 [0.486, 0.817]
   against a baseline share of 0.908) — the estimator Results 6 recommends for between-run contrasts, which
   now says so and rests the recommendation on manufacture grounds alone. Proportionality is no longer
   offered as a confirmation.

4. **Title and "demonstration".** "Reports lag-1 autocorrelation change as synergy change" and
   "demonstration" are withdrawn from the title in favour of the Conclusions' "dominated by"; the B4
   pre-specified criterion under which the DMT contrast would have been a demonstration (residual DiD near
   zero) was not met, so the word is not used for it. Two candidate titles are given in the draft [TK].

5. **Smaller corrections in the same revision.** The partial correlation between the residual DiD and the
   CCS-sts DiD is quoted under the published CCS definition (+0.831 / +0.855, `ts_gsr` / `ts_demean`; third
   review, Appendix, computation 4) as the B6 rule requires, with `phyid`'s values (+0.688 / +0.820) beside
   it. The Discussion's "both of which DMT produced" (r₁ and |q|) is corrected: the |q| fall is on `ts_gsr`
   only; on `ts_demean` the signed mean correlation rose (`results/global_fc_did_ts_demean.csv`). The
   Results 4 count of "both nulls" for the residual is replaced by the sign-flip p with the phase-null
   technicality stated. Table 3's null row gives −3.0 % for the four-cell level and −3.1 % for the
   homogeneous-filter level. The Figure 3 caption (`scripts/15_figures_v2.py`, `manuscript/figures/captions_v2.md`)
   says the split-half test could not separate signal from window noise. `README.md`, `CLAUDE.md` and
   `run_all.sh` are updated to name `draft_v2.md`, scripts 00–15 and the `notes/` scripts (section 6 of
   `run_all.sh`, not yet executed end-to-end); `manuscript/draft_v2-1.md` (an earlier variant with a
   different author list and abstract) is to be deleted.

## Leave-two-out on the sts / autocorrelation collinearity: pre-run entry, 15 Sep 2026 11:09 UTC (appended; nothing above edited)

Requested after the fourth review (the verification of the correction note, 15 Sep 2026, filed as
`notes/verification_correction_note_2026-09-15.md`), which asked for the
leave-two-out value of the per-subject correlation r(MMI-sts DiD, lag-1 autocorrelation DiD) = +0.953 (`ts_gsr`,
W = 60, primary set; Results 3, Figure 3a) beside the full-set value, since subjects 8 and 14 sit far from the
cloud. Script `notes/partB9_leave_two_out.py`; input the committed per-subject DiDs of
`notes/review_results/inference_rows_raw.pkl` (rows "sts ts_gsr W60" and "autocorr ts_gsr W60", field
`did_subjects`); every pair of subjects dropped in turn (C(14, 2) = 91 refits), Pearson r and Spearman ρ over
the remaining 12; outputs `notes/review_results/partB/leave_two_out.csv` and `leave_two_out.log`. Reported: the
full-set value, the range over the 91 refits, the minimum with the pair that gives it, in Results 3 and the
Figure 3a caption. No prediction; no inference; it changes no verdict (the collinearity is descriptive). The only
computation of this revision. Two reporting changes in the same revision, no numbers changed: `partB7_splithalf.py`
now prints the reliability ceiling √(rel_res × rel_CCS) beside the rule's branch, whether the threshold exceeded it,
and that the reading is then undetermined (correction note of 15 Sep, item 1), and its tables and log are
regenerated; `scripts/15_figures_v2.py` is re-run so that the figures and `captions_v2.md` come from one execution
(Figure 4 bands are now within-subject SEMs; a Figure 5, the lag dependence of Table 5, is added).

## Leave-two-out outcome, 15 Sep 2026 11:10 UTC (appended; nothing above edited)

`notes/partB9_leave_two_out.py`, run once after the entry above; numbers from `notes/review_results/partB/leave_two_out.log`.
Full set r = +0.953 (ρ = +0.903). Over the 91 refits the Pearson r ranges from +0.846 to +0.973 (median +0.954);
the minimum, +0.846, is without subjects 8 and 14 (the two the third review named; ρ +0.846 there too), the maximum
+0.973 without subjects 6 and 10; 90 of the 91 refits are at or above +0.90; the 66 refits that keep both subjects
8 and 14 lie between +0.948 and +0.973, the 24 that drop one of them between +0.913 and +0.947. Reported in
Results 3 beside the full-set value and in the Figure 3a caption. Nothing else changes.

## Data-governance note, 15 Sep 2026 12:15 UTC (appended; nothing above edited except as stated here)

The participant codes recovered from the MATLAB table objects of `intensity_ratings.mat` (20 codes of the
form S + two digits + initials: the 14 analysed subjects and the six excluded by the data authors) were
removed on 15 September 2026 for data governance from every tracked file that carried them: this record
(the "Subject alignment across files" section, item (c), and the "Open questions" entry on the subject
order — the lists are replaced by "the 14 codes (not reproduced)" and "the six codes of the excluded
participants (not reproduced)", and no other text of those entries was changed), `manuscript/draft.md`
(Dataset paragraph), `notes/adversarial_review_2026-09-14.md` (one parenthesis),
`scripts/10_subject_alignment_check.py` (it now prints table row indices and counts, never a code) and
its outputs `results/subject_alignment_check.txt` and `results/run_10_subject_alignment_check.log` (the
lists replaced by the corresponding table row indices; every number unchanged; a note line added under the
header). The codes remain in the source file (`external/`, git-ignored, not redistributed) and in the
repository history before this commit; purging them from the history requires a history rewrite, which
is recorded here as an open item for the public release. In the same commit the leave-two-out pre-run
entry above was given the file name of the verification pass it cites,
`notes/verification_correction_note_2026-09-15.md`, which now holds that pass.

## Finalisation pass, 15 Sep 2026 12:40 UTC (appended; nothing above edited)

No scientific content changed; no computation run except one re-execution of `scripts/15_figures_v2.py`
after the panel (b) title of Figure 4 was changed (same inputs, no number changed). From that run,
`fig4_v2_residual_diagnostic.png`/`.pdf` and `captions_v2.md` are committed; the other four figures, whose
content did not change, are left as committed after the leave-two-out revision, and `run_all.sh`
(section 6, running since 10:25 UTC) regenerates all five from the pinned environment. The edits to
`manuscript/draft_v2.md`:

1. Title: the alternative-title line marked TK in the correction note of 15 Sep 2026 (item 4) is deleted;
   the first title stands. That TK marker is resolved by this entry.
2. Ethics statement: a section before "Data and code availability", worded after the approval statement of
   Timmermann et al. (2023) as read on PubMed Central on 15 Sep 2026 (National Research Ethics Committee
   London – Brent and the Health Research Authority; Declaration of Helsinki 2000, ICH GCP, NHS Research
   Governance Framework; Imperial College London as sponsor; Home Office licence for Schedule 1 drugs;
   written informed consent). That paper gives no reference number, so the number stays a TK marker pending
   C. Timmermann. The statement adds that this is a secondary analysis of anonymised derivatives, with
   no new data and no participant identifiable.
3. Data reuse: the TK marker asking for the written confirmation to be attached is replaced by the confirmation by email from
   C. Timmermann (13 Sep 2026) and S. P. Singleton (14 Sep 2026), correspondence held by the corresponding
   author (also in README, "Licence", and CLAUDE.md).
4. Software versions in Methods, Estimator: Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.1
   from `requirements.lock.txt`; `phyid` at commit 6c5f2e9d33c985efbdf875d45cb5a2a6a5cdbf44 (the pinned
   commit, merge of the repository's pull request #4, 13 Mar 2026), cited in the reference list as a
   software entry; OS 64-bit Linux, release marked TK (to be confirmed on the workstation).
5. Reference verification: every entry checked against Crossref (`api.crossref.org/works/<DOI>`), the
   publisher page or the preprint server. Corrected: "Dong et al. (2025)" → Zhang, X., Han, C., Xia, J.,
   Deng, L., & Dong, J. (2025) (Dong is the last author; the in-text citation and the row label in
   `notes/partB5_literature.md` are corrected with a dated parenthesis); Nago, H., Kojima, H.,
   Yamaguchi, H., & Yamashita, Y. (2026), *Brain Informatics* 13(1), 25; Gatica et al. (2024) pages
   1032–1050, doi 10.1162/netn_a_00388; Faes et al. (2025) full author list, *Physical Review Letters*
   135(18), 187401, doi 10.1103/nrwj-n8lj; Liardi et al. (2025) 21(11), doi 10.1371/journal.pcbi.1013629;
   Luppi et al. (2023) full author list, *NeuroImage* 269, 119926, doi 10.1016/j.neuroimage.2023.119926;
   Luppi et al. (2026) full author list, 10(4), 777–802, doi 10.1038/s41562-025-02381-5; Mediano et al.
   (2025) full author list, 122(39); Wu et al. (2013) title ends "…resting state fMRI data", 17(3);
   Down et al. (2026) confirmed as a preprint only (no journal version found; the PubMed and PMC records
   are preprint records); issue numbers added to Barrett 2015, Huang 2018, Luppi 2022, Prichard & Theiler
   1994, Schaefer 2018, Singleton 2025, Timmermann 2023, Yeo 2011; the eLife entry marked as the version of
   record (v4, 18 Jul 2024). Every other entry verified as printed. No TK marker remains in the reference list.
6. Copy-edit: notation made uniform (r₁, ΦR, DiD, W = 60, p = …, CIs as [lower, upper]); Table 3 and
   Table 4 p-values written to four decimals throughout (the added digits are read from
   `notes/review_results/inference_rows_diag.csv` and `inference_rows_ccs_pub.csv`; the residual-row
   values 0.0422 and 0.0137 are 0.042236… and 0.013671…); sentences over 60 words split (74 → 6 by the
   splitter used, the six remaining being formula or enumeration sentences whose split would separate
   a value from its qualifier); tense regularised (past for what was done, present for what the family and
   the map show). No number and no claim changed; the only non-mechanical recasts are recorded in the
   closing report of this pass.
7. Figure 4 panel (b): title "same vertical scale as a" (untrue, the panel has its own y-limits) replaced
   by "same units as a; same nats per unit height", in the script and the caption.
8. Supplement S4 added: `manuscript/supplementary_cobidas.md`, the COBIDAS checklist (design, acquisition,
   preprocessing, statistics, results, sharing) with each item reported, not applicable or not reported.
9. Conflicts of interest: the TK marker on C.T.'s co-authorship of Singleton et al. (2025) is removed, the
   author list of that paper (Crossref record of 10.1038/s42003-025-08078-9: Singleton, Timmermann, Luppi,
   Eckernäs, Roseman, Carhart-Harris, Kuceyeski) confirming it.
10. The verification of the correction note is filed as `notes/verification_correction_note_2026-09-15.md`
   (the leave-two-out pre-run entry cites it by that name). Venue and preprint options are in
   `notes/venue_options.md`.

The TK markers remaining after this pass are listed in the closing report and in CLAUDE.md, "Remaining work".
