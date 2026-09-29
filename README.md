# The Gaussian-MMI synergy atom of integrated information decomposition is mostly self-prediction

[![tests](https://github.com/Vasilis540/dmt-phiid/actions/workflows/tests.yml/badge.svg)](https://github.com/Vasilis540/dmt-phiid/actions/workflows/tests.yml)

A secondary analysis of open DMT fMRI data (14 subjects, DMT and placebo runs,
115 regions of the Schaefer-100 and Tian subcortical parcellations) using Integrated
Information Decomposition (ΦID;
Gaussian model, MMI redundancy, lag 1). The study was pre-specified as a test
of whether whole-brain synergistic information is up-regulated under DMT; the
synergy atom `sts` *decreased* (difference-in-differences −0.081 nats [−0.132,
−0.031], the inverted sign-flip 95 % interval; exact sign-flip p = 0.004; negative in 13 of
14 subjects; replicated
without global signal regression at −0.103; survives motion control; robust to
dropping any single subject), which refutes the pre-specified hypothesis and is
reported as a refutation. Two adversarial reviews then showed that the decrease
is carried by the self-prediction atoms and is reproduced by the change in
lag-1 autocorrelation r₁, and the paper became an account of the estimator: the
sixteen Gaussian-MMI atoms of a bivariate AR(1) pair in closed form
(`sts = xtx + yty + rtr` on the symmetric family, balanced by four negative
atoms; `sts = 2 min(S_x, S_y)` with unequal coefficients at q = 0), the
exchange rates between the atom and a pair's lag-1 autocorrelation, lag-0
correlation, lagged coupling and within-pair asymmetry, a scope map of `sts`
over (r₁, q) with real pairs overlaid, a comparison with CCS redundancy under
its published definition, the lag dependence, a per-pair residual diagnostic
calibrated on simulated ground truth, and the DMT contrast as the test case.
The analysis plan, every decision rule and every prediction of the original
analysis were committed before the results they govern existed; the later
analyses were planned in dated record entries after the review computations had
characterised the phenomenon, and the record says so.

**The paper is `manuscript/draft_v2.md`**, restructured on 21 Sep 2026 for a
journal reader in the PLOS Computational Biology Methods-article order,
shortened on 23 Sep 2026, revised on 25 Sep 2026 to the adversarial review, the
citation check and their verification of 24 Sep 2026, and corrected to the
error-only check of 25 Sep 2026 and the error-only read of 26 Sep 2026, and to the
citation crosscheck of 28 Sep 2026 (Introduction through Methods 6,994 words with
headings; three tables and six figures, the captions in the text), with its
supporting information as five files under `manuscript/si/` and its tables
S1–S20 in `manuscript/supplementary.md`; every number of the main text is listed
with its source file and line in `manuscript/main_text_numbers.csv`. B16b, B17b
and B21–B24 have been run and their values are in the text, and the single
end-to-end run of `run_all.sh` was made at c25a310 on 26 September 2026 (475 min
by its own count): it reproduced the committed outputs under the rule of its
pre-run entry apart from two CCS agreement-share arrays of B2, which depend on
the machine and the numerical build and which no result of the paper uses
(record, "The final end-to-end run of `run_all.sh` at the final commit: the
difference in the two CCS agreement-share arrays"), and its outputs are in the
commit that follows (record, "The final end-to-end run of `run_all.sh` at the
final commit: outcome"). The [TK] marks left are the co-author items and the
archive's DOI (Data and code availability), filled at submission. The code now carries the
correction for the matrices that are not positive definite (record, "The
matrices that are not positive definite (B26): pre-run entry"); the committed
outputs predate it until B26's run replaces them: a run of `run_all.sh` before
then writes the outputs of B5, the null, B23, B17 and B17b, B10's and B15's
sections on synthetic series and Fig 3 (c) with their corrected values
(`notes/review_2026-09-28/checks/b26_preview.md`), the lines the correction
rewords (rule (i) of B26's entry), and any output that the data's matrices
change.
`manuscript/draft.md` is the superseded first draft, kept as a record.

## Repository layout

| path | contents |
|---|---|
| `manuscript/draft_v2.md` | **the paper** |
| `manuscript/draft.md` | the superseded first draft (the original pre-specified analysis), kept as a record |
| `manuscript/si/` | the supporting texts of `draft_v2.md`: `S1_Text.md` (the original pre-specified analysis), `S2_Text.md` (the ΦR exploration and deconvolution), `S3_Text.md` (the supporting tables of the estimator account), `S4_Text.md` (the COBIDAS reporting checklist, filled for this secondary analysis), `S5_Text.md` (provenance and audit trail) |
| `manuscript/supplementary.md` | supplementary tables S1–S20 (companion to `draft_v2.md`), every value quoted from `results/`, `notes/review_results/` and, for S19 and S20, the record and `notes/partB5_literature_v2.md` |
| `manuscript/main_text_numbers.csv` | every number of the main text (title to Methods, the figure and table captions, the Data and code availability statement and the Supporting-information captions), one row per number, with its section and paragraph, category, source file and line (or its derivation), and the result of checking it there |
| `manuscript/figures/` | `fig1_v2_scope_map`, `fig2_v2_atoms_observed_substituted`, `fig3_v2_per_subject`, `fig4_v2_regional`, `fig5_v2_residual_diagnostic` and `fig6_v2_lag_dependence` (pdf, png), numbered by order of first citation, and `captions_v2.md`, generated by `scripts/15_figures_v2.py` from committed result files (the captions file names the commit it ran at); `fig1_v2_atoms_mmi_ccs` is an earlier version's Figure 1, kept in place; the `draft.md` figures and `captions.md` (from `scripts/12_figures.py`) are kept in place |
| `manuscript/analysis_record.md` | the full pre-specification and results record, append-only, never retroactively edited (dated correction notes are appended, never edited in) |
| `manuscript/prespecification_summary.md` | **the audit trail of the original analysis**: each decision with the commit that fixed it, and whether it changed later; it does not cover the review computations or Part B, whose plans and outcomes are dated entries in the record |
| `scripts/00–15_*.py` | analysis scripts, numbered in execution order, each independently runnable (`14` proportionality, `15` the v2 figures) |
| `notes/` | the first three adversarial reviews (`adversarial_review_*.md`) and the fourth, the verification of the correction note (`verification_correction_note_2026-09-15.md`; the fifth review is quoted in the record's entry of 15 Sep 2026, 18:14 UTC), the sixth review of 17 Sep 2026 with its checks (`fresh_review_2026-09-17/`), the citation audit against the full texts, the independent adversarial review, its verification and the plan to submission of 20 Sep 2026 (`review_2026-09-20/`), the independent review and the citation pass of 22 Sep 2026 with their verification and the reviewer's check scripts (`review_2026-09-22/`), the adversarial review and the citation check of 24 Sep 2026 with their verification, the reviewers' check scripts and `checks/derived_r17.py` with its output (`review_2026-09-24/`), the error-only check of 25 Sep 2026 with its verification, the revision's replacements and the check scripts (`review_2026-09-25/`), the error-only read of 26 Sep 2026 with its verification, the corrections' replacements and the checks' outputs (`review_2026-09-26/`), the citation crosscheck of 28 Sep 2026 with the revision's replacements, the text that reports B25, the checks' outputs and B25's first run with the correction of one of its checks (`review_2026-09-28/`), the revised applicability table (`partB5_literature_v2.md`), the venue and preprint options (`venue_options.md`), the review computations (`rev_*.py`, `review_*.py`, `review_computations_2026-09-14.md`), the Part B plans and notes (`partB_prespec_2026-09-14.md`, `partB*.md`) and their scripts (`partB*.py`, including `partB10_crosslag_deviation.py` and `partB11_regional_sts_r1.py`, added 15 Sep 2026, and `partB14_family_atoms.py`–`partB20_regional_partial.py`, added 20 Sep 2026 under their pre-run entries and run by V.S. on 21 Sep 2026 (outputs at 96e2242; outcome entries of 21 Sep), and `partB16b_whitened_spectrum.py` and `partB17b_calibration_filtered.py`, added 21 Sep 2026 under their pre-run entries and run that day, outputs at ada6438, outcome entries of 21 Sep; and `partB21_inference_revision.py`–`partB24_bandpassed_expectations.py` with `rev_inference_inverted.py`, added 23 Sep 2026 under their pre-run entries and run by V.S. that day, outputs at 90690f4; and `partB25_binarised.py`, the binarised estimators on the family, and `partB26_positive_definite.py`, the run of section 6 with the correction for the matrices that are not positive definite, added under their pre-run entries in the revision that followed the citation crosscheck of 28 Sep 2026), the plain-language companion (`companion_plain_language.md`, retired 21 Sep 2026: its role is taken by the paper's Author summary and S5 Text) and the defence questions (`defence_questions.md`, rewritten 21 Sep 2026 to the restructured text); result files, tables and logs under `notes/review_results/` |
| `results/` | every table and array of the original analysis, with the script name and git SHA in its header; `run_*.log` are the run logs |
| `run_all.sh` | regenerates everything in dependency order: the original analysis (5 h 17 min in the final run) and, in its last section, the review and Part B computations and the v2 figures (2 h 39 min); 475 min end to end by its own count in the final run at c25a310, about twelve minutes more with the HRF-deconvolution sandbox present |
| `requirements.lock.txt` | pinned environment (Python 3.12) |
| `tools/ar1_diagnostic.py` | the paper's check for any pair of time series: MMI-sts beside its AR(1)-substituted estimate, the sixteen atoms, the closed form and its exchange rates (NumPy only; see "Checking your own synergy values") |
| `tests/` | pytest tests of the tool against `phyid` and `notes/rev_phiid_fast.py`, and of the closed form (no data) |
| `.github/workflows/tests.yml` | runs the tests, the tool's doctest, the self-tests of B25 and B26 and `phyid`'s own tests at the pinned commit on every push |
| `LICENSE`, `LICENSE-CC-BY-4.0.md` | MIT for the code; CC BY 4.0 for the result files and the text outside `manuscript/` (the manuscript, a draft for co-author review, is not yet licensed; the data are not included) |
| `CITATION.cff` | how to cite this repository |
| `data/Schaefer2018_100Parcels_7Networks_order.lut` | the parcel names of the Schaefer-100 7-network parcellation, copied unchanged from CBIG (MIT; `data/LICENSE-CBIG.md`) |
| `CLAUDE.md` | orientation for further work: current state, standing methodological rules |
| `external/DMT_NCT/` | the source data repository, cloned locally and git-ignored (see below) |

## Reproducing

```bash
git clone <this repository> dmt-phiid && cd dmt-phiid
git clone https://github.com/singlesp/DMT_NCT.git external/DMT_NCT   # data; checked at commit 77af7aa
python3.12 -m venv .venv && .venv/bin/pip install -r requirements.lock.txt
# phyid is not on PyPI; the lock file pins it to a commit of
# https://github.com/Imperial-MIND-lab/integrated-info-decomp
.venv/bin/python scripts/00_verify.py     # data and method integrity check, seconds
bash run_all.sh                           # everything, about 8 h in the final run; the header's per-step times are from earlier runs
```

The review and Part B computations (`notes/*.py`) read the arrays in `results/`
and write under `notes/review_results/`; `run_all.sh` runs them after the
original analysis, in dependency order. The HRF-deconvolution items need the
sandbox described in `notes/rev_deconv.py` and are skipped by `run_all.sh`
unless it is present.

Individual scripts can be run on their own once their inputs exist, for
example `scripts/06_primary_b_analysis.py --variant ts_gsr --window-trs 60`
for the primary inference (it reads the windowed atoms written by
`scripts/01_synergy_timecourse.py --fit-mode window`). All scripts use seed
20261120. Every script under `scripts/` that writes results (all but
`00_verify.py`) writes the git SHA of the working tree into its output header,
tagged `-dirty` if `scripts/` or the record had uncommitted changes; every
`notes/` script that writes under `notes/review_results/` does the same through
`notes/rev_git.py` (`partB10`–`partB13` since 15–16 September 2026, the others
since 18 September). The tables and reports that the final run of `run_all.sh`
wrote carry its SHA, c25a310, apart from five CSVs that carry none by design
(record, the final run's pre-run entry, item 3), and so do its logs that print
one; the files it did not regenerate, the HRF-deconvolution outputs among them,
keep the header of the run that wrote them.
Figures are regenerated from saved results only, never from a recomputation.

### Tests

```bash
.venv/bin/pip install pytest             # pytest is not part of the pinned analysis environment
.venv/bin/python -m pytest tests         # the tool against phyid, and the closed form; seconds, no data
```

`tests/test_ar1_diagnostic.py` checks `tools/ar1_diagnostic.py` against `phyid` and against
`notes/rev_phiid_fast.py`, the second implementation behind the paper's numbers, and its handling of matrices that
are the lag covariance of no process; `tests/test_closed_form.py` checks the closed form of Results 1 and the numbers
the paper quotes from it against the tool's lattice solve. The workflow in `.github/workflows/tests.yml` runs them on
every push, with the tool's doctest, the self-tests of `notes/partB25_binarised.py` and
`notes/partB26_positive_definite.py` and `phyid`'s own tests at the pinned commit (which compare its Gaussian and
discrete modes under MMI and CCS with reference outputs downloaded from OSF).

## Checking your own synergy values

`tools/ar1_diagnostic.py` (NumPy only) puts the Gaussian-MMI synergy atom `sts` of a pair of time series beside its
AR(1)-substituted estimate: the `sts` of the same 4 × 4 lag correlation matrix with the pair's two lag-1
autocorrelations kept, its two lag-0 entries set to their mean q and its two cross-lag correlations replaced by
a_y q and a_x q, which is what the pair's own autocorrelations and lag-0 correlation carry (the paper's Results 4).
The atoms are those of `phyid`'s `calc_PhiID(kind="gaussian", redundancy="MMI")`, in nats.

```python
import sys; sys.path.insert(0, "tools")
from ar1_diagnostic import diagnose, diagnose_windows, diagnose_pairs, closed_form, exchange_rates

d = diagnose(x, y)                       # one fit: d["sts"], d["sts_ar1"], d["residual"], d["r1"], d["q"], d["atoms"]
w = diagnose_windows(x, y, window=60)    # separately fitted non-overlapping windows (the paper's W = 60)
pairs, P = diagnose_pairs(X)             # every pair of the rows of a (regions × samples) array
closed_form(0.85, 0.25)["sts"]           # 1.2588 nats: two AR(1) processes with no lagged interaction
exchange_rates(0.85, 0.25)               # ∂sts/∂r₁ = 6.07 and ∂sts/∂q = −0.19 nats per unit
```

From the shell, for two files with one value per line: `python tools/ar1_diagnostic.py x.txt y.txt --window 60`.
Report the mean lag-1 autocorrelation beside `sts`, and each `sts` contrast beside the contrast of its
AR(1)-substituted estimate. Their difference is not by itself a measure of lagged interaction: it has a non-zero
expectation under a pure change of autocorrelation, which a simulation of the study's own design must supply (the
paper's Results 4 and Recommendations). Where a pair's measured a_x, a_y and q are those of no AR(1) pair,
(1 − a_x²)(1 − a_y²) ≤ q²(1 − a_x a_y)² (a high |q| with unequal autocorrelations, as when two regions share a slow
signal under different noise), the substituted estimate does not exist and the tool returns NaN: average with
`np.nanmean` and report the share of such windows or pairs. Inputs must be finite; drop or impute missing samples
first.

## Data source, citation and licence

The timeseries (four preprocessing variants), intensity ratings, framewise
displacement, EEG Lempel-Ziv regressor, structural connectome and serotonin
receptor maps are the files released in-repository by

> Singleton, S. P., et al. (2025). *Communications Biology*,
> doi:10.1038/s42003-025-08078-9. Code and data:
> https://github.com/singlesp/DMT_NCT, Zenodo doi:10.5281/zenodo.15177511.

acquired and first described by

> Timmermann, C., et al. (2023). *PNAS*, doi:10.1073/pnas.2218949120.

**Licence.** The source repository carries no licence of its own at 77af7aa (its three licence files belong to third-party plotting functions it bundles), and no
data-use agreement or request process is stated. The data are used with
the agreement of the data collectors and the derivative authors, confirmed
by email from C. Timmermann (13 September 2026) and S. P. Singleton
(14 September 2026), with attribution; the correspondence is held by the
corresponding author; this repository does not
redistribute them (they are cloned into a git-ignored directory). This
repository's code is released under the MIT licence (`LICENSE`) and its result files and
the text outside `manuscript/` under CC BY 4.0 (`LICENSE-CC-BY-4.0.md`); the manuscript,
a draft for co-author review, is not yet licensed, and none of these covers the
data. To cite the repository, see `CITATION.cff`.

One data-quality note not documented in the source papers: subject index 7
(DMT run) has region 20 constant at zero in every variant, so region 20 is
dropped for all subjects and both conditions (115 regions, 6,555 pairs).

## Pre-specification and audit trail

Start with **`manuscript/prespecification_summary.md`** for the original
analysis. It lists every analysis decision, the commit and date that fixed it,
and whether the decision's text changed afterwards, including the predictions
that failed. The review computations of 14 Sep, the Part B analyses and the
additions of 15 Sep are governed by dated entries in the record itself
(`notes/partB_prespec_2026-09-14.md`; record sections "Closure entry",
"Part B, items 6–8", "Correction note, 15 Sep 2026", "Leave-two-out",
"Data-governance note, 15 Sep 2026" and "Finalisation pass, 15 Sep 2026"), written after the
review computations had characterised the phenomenon; `manuscript/si/S5_Text.md`
states what was known when each was written, with the run inventory, the
reviews and audits, and every commit the paper cites.
The full record it summarises is `manuscript/analysis_record.md`, which
lived at `CLAUDE.md` until 14 Sep 2026 and was moved with `git mv`
(byte-identical; `git log --follow` carries its history). The record is a
git-tracked file, not an external pre-registration: what it establishes is
ordering within the commit history, nothing more.

Contact: Vasilis Sampalis, sampalisvasilis@gmail.com.
