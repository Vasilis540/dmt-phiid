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

## Open questions to resolve

- Confirm reuse licence with Singleton / Timmermann before publishing.
- ~~Decide sliding-window length for time-resolved ΦID~~ — **resolved**:
  30 TRs / 60 s, non-overlapping. See Primary B above for the justification.
- Decide whether whole-brain synergy is summarised as mean over all pairs or
  restricted to a defined subnetwork — pre-register the choice.
  `REGION_SELECTION` in `01_synergy_timecourse.py` is the knob; `"all"`
  (mean over all 6,670 pairs) is the current default and the only one used
  for a reported result so far.
- Whether to email Stamatakis to collision-check before or after first results.
