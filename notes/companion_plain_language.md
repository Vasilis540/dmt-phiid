# A plain-language companion to `manuscript/draft_v2.md`

Written 15 September 2026 for the first author. It follows the paper unit by unit — title, each abstract section, each Introduction paragraph, each Methods subsection, each numbered Results section and each table in it, each Discussion subsection, each figure with its caption, the Supplement pointers and the back-matter sections — and gives for each unit (a) what it says in plain language, (b) why it is there, and (c) the one or two hardest questions a reviewer or a senior scientist would ask about it, with the answer and where in the paper the answer lives. Every number below is quoted from the paper (`draft_v2.md`, `figures/captions_v2.md` or `supplementary.md`); where I do arithmetic on the paper's numbers I say so. The last section lists every place where writing the plain version showed the paper stating something without justifying it, using a term it never defines, compressing a step, or making a claim I could not rebuild from its own text. The paper itself is not edited by this document.

The paper's own notation, used throughout: each of the sixteen ΦID atoms is a two-letter code, first letter the kind of information in the past (r redundant, x unique to region X, y unique to region Y, s synergistic), last letter its kind in the future. So rtr is redundancy-to-redundancy, sts synergy-to-synergy, xtx region X predicting itself. r₁ is the lag-1 autocorrelation, q the lag-0 cross-correlation, and (0.85, 0.25) is the "operating point" at which the paper quotes every slope.

---

## Glossary

Every technical term the paper uses, one sentence each, alphabetical. Terms are defined again the first time they appear in the walk-through below, so you can read the walk-through without the glossary and use the glossary to look something up.

**a, a_x, a_y** — The lag-1 autocorrelation coefficient of a region's time series (how strongly this time point predicts the next one); the paper writes a for the closed form, a_x and a_y for the two regions of a real pair, and r₁ for the same quantity measured on data.

**adversarial review** — A deliberate attempt, written up as a document in `notes/`, to break the paper: re-trace every number, run extra computations, and look for what the analysis got wrong.

**aggregate forward synergy** — Varley's quantity, the sum of the four atoms whose past side is synergistic (str + stx + sty + sts).

**AI-use statement** — A declaration of which parts of the work were produced with an AI system's help and who takes responsibility for them.

**analysis plan (Part B plan)** — A written statement, committed before a computation was run, of what will be computed and by what rule the outcome will be reported.

**anonymised derivatives** — The processed outputs released by the data authors (regional time series, ratings, motion values), which carry no field that could identify a person.

**AR(1) process** — The simplest "sticky" random series: each value is a fraction a of the previous value plus fresh random noise, so the series remembers exactly one step back.

**association cortex** — The regions of cortex that are not primary sensory or motor areas and are involved in integrating information.

**atom code (rtr, rts, sts, xtx, ...)** — The paper's two-letter naming of atoms: first letter the kind of past information (r redundant, x unique to region X, y unique to region Y, s synergistic), last letter its kind in the future; so rts is redundancy-to-synergy, sts synergy-to-synergy and xtx the self-prediction of X.

**atom (ΦID atom)** — One of the sixteen pieces into which ΦID splits the total information that a pair's past carries about its future, labelled by the kind of information it was in the past and the kind it becomes in the future.

**autocorrelation** — The correlation of a series with a shifted copy of itself, i.e. how much a value at one time resembles the value a fixed number of steps later.

**autocorrelation function** — The list of autocorrelation values at lag 1, lag 2, lag 3 and so on, describing how quickly a series forgets its past.

**autocorrelation-independent component** — A part of an sts change that would remain after everything that lag-1 autocorrelation change can produce has been subtracted.

**band-pass filter (0.01–0.08 Hz)** — A processing step that keeps only the slow fluctuations of the BOLD signal, between one cycle per 100 seconds and one cycle per 12.5 seconds (the reciprocals of 0.01 and 0.08 Hz), discarding faster and slower ones, which by itself makes the series highly autocorrelated.

**baseline / pre-injection** — The part of a run before the injection (windows 1–4, the first eight minutes), used as the "before" in every contrast.

**Benjamini–Hochberg FDR** — A rule for deciding which of many tests count as positive while keeping the expected fraction of false positives among them below a chosen level (used only in the supplement's regional analysis).

**between-subject vs within-subject** — Between-subject spread is how much people differ from one another; within-subject comparisons look at changes inside the same person, which is what this paper's contrasts test.

**bias (finite-sample bias)** — A systematic error in an estimate that comes from having few data points, which does not average away by repeating the same short measurement.

**bin** — A block of 30 consecutive TRs (one minute) kept as the averaging unit for the global-fit values; a run has 28 bins.

**bivariate** — Involving exactly two variables, here two brain regions.

**block determinant** — The determinant of a sub-matrix of the correlation matrix, from which each Gaussian mutual information is built.

**block (synergy block)** — The paper's name for the three large positive MMI atoms sts + rts + str taken together.

**BOLD** — Blood-oxygen-level-dependent signal, the quantity fMRI measures, which tracks blood oxygenation changes that follow neural activity slowly.

**bootstrap (subject bootstrap)** — A way to estimate how much a group result would wobble on a different sample: re-draw the 14 subjects with replacement 10,000 times and recompute the statistic each time.

**C** — The paper's shorthand for the cross-lag mutual information on the AR(1) family, C = −½ ln(1 − a²q²), the information one region's present carries about the other region's next value.

**c (coupling coefficient)** — In the coupled VAR(1) family, the amount by which one region's past directly feeds the other region's next value.

**CCS (common change in surprisal)** — A way of defining redundancy time point by time point that keeps a shared-information quantity (co-information) only at the moments where all the relevant local signs agree, and counts zero elsewhere.

**cell (analysis cell)** — One combination of preprocessing variant and estimator (for example ts_gsr at W = 60) on which a result is reported; the same word is also used for the four run × period combinations of the finite-sample null.

**central differences** — A numerical way of estimating a slope: evaluate the function a tiny step above and below a point and divide the difference by the step.

**closed form** — A formula that gives the answer directly, without simulation or iteration.

**closure entry** — A dated entry in the record that ended the ΦR exploration, recorded why its positive result supports no claim, and stated that no confirmatory claim attaches to a specification chosen after seeing results and that no further specification would be run in search of a positive DMT result.

**COBIDAS** — A reporting checklist for MRI studies from the Organization for Human Brain Mapping, filled in as Supplement S4.

**co-information** — A three-way information quantity that is positive when the information is shared (redundant) and negative when it appears only in the combination (synergistic).

**collinearity** — Two quantities rising and falling together so closely across subjects that they behave like one quantity.

**commit / SHA** — A saved snapshot in the git version-control record, identified by a hash code (for example 44cec4f) that fixes what was written and in what order.

**commit trailer** — A line at the end of a git commit message that records extra information, here which AI session produced the change.

**common signal** — A genuine shared component, as opposed to shared estimation noise.

**conditional covariance** — The covariance of the future values once the past values are known, equal on the AR(1) family to the innovation covariance.

**conditional statement (applicability table)** — A sentence of the form: if a study's autocorrelation had changed in a stated direction, the map would produce its reported effect; applied identically to every study and making no claim about any study's actual data.

**confidence interval (CI)** — A range of values compatible with the data at a stated level; a 95 % CI that excludes zero is the usual sign that an effect is unlikely to be zero.

**confirmatory vs exploratory vs post-hoc** — Confirmatory means the test and its rule were fixed before the result existed; exploratory means it was run without a pre-fixed rule and is reported for what it is; post-hoc means it was added after the primary result was known.

**correction note** — The dated record entry listing what the third review found wrong in the previous draft and what was changed in response.

**correlation matrix** — A table of the correlations between every pair of variables in a set; the paper's 4 × 4 matrix holds the correlations among the two regions' present and next values.

**correlation (Pearson r)** — A number between −1 and +1 measuring how well two quantities track each other along a straight line, with 0 meaning no linear relation.

**Cousineau–Morey within-subject SEM** — A way of drawing error bands that shows the uncertainty of comparisons within the same person, by first removing each person's overall level.

**covariance** — How two quantities vary together in their original units; correlation is covariance scaled to lie between −1 and +1.

**CRediT** — A standard list of contributor roles (conceptualisation, software, writing, and so on) used to state who did what.

**cross-half correlation** — In the split-half test, the correlation between one quantity computed on the odd windows and the other computed on the even windows, which shared window noise cannot produce.

**cross-lag correlation** — The correlation between one region now and the other region one step later, corr(x_t, y_{t+1}).

**cross-lag deviation** — For a pair, the measured cross-lag correlation minus what the AR(1) model predicts for it (a_y q or a_x q); its mean over pairs at the run level is the paper's test of the pooling mechanism.

**cross-lag substitution** — The diagnostic's one modelling step: replace each pair's measured cross-lag correlations by the AR(1) values a_y q and a_x q.

**cross-prediction atoms** — The six atoms (rtx, rty, xtr, ytr, xty, ytx) in which information about one region's future comes partly from the other region; they are zero on the AR(1) family.

**Crossref** — A database of publication records against which the reference list was checked.

**curvature** — How fast a slope itself changes, the coefficient of the squared term.

**decay windows** — In the original analysis, the post-injection windows over which the drug effect fades and the intensity ratings were meant to be tracked.

**Declaration of Helsinki** — The international ethical standard for research involving human participants that the original study followed.

**deconvolution (HRF deconvolution)** — An attempt to undo the slow blood-flow response and recover a sharper neural-like series from BOLD.

**derivative (partial derivative, ∂)** — The slope of a function with respect to one input while the other inputs are held fixed; ∂sts/∂r₁ is how much sts changes per unit change of r₁ at fixed q.

**derivative ratio** — |∂sts/∂r₁| divided by |∂sts/∂q|, the number of units of sts change that a unit change in r₁ produces for every unit a change in q produces.

**determinant (log-determinant)** — A single number computed from a square matrix; for Gaussian data every mutual information is half the logarithm of a ratio of determinants of correlation matrices.

**DiD (difference-in-differences)** — The change after minus before on the DMT run, minus the same change on the placebo run, so that whatever happens with time alone is subtracted out.

**directional-failure rule** — The pre-recorded rule that a significant change in the direction opposite to the hypothesis would be reported as a refutation and not reframed.

**disattenuation** — Correcting a correlation for the unreliability of the two measured quantities to estimate what it would be if both were measured perfectly.

**disintegration (Varley)** — Replacing a coupled pair of processes by two independent processes that each keep their own autocorrelation, to see what an estimator reports when nothing joint is left.

**disorders of consciousness** — Clinical conditions of severely reduced consciousness after brain injury, used in the literature as low-consciousness comparisons.

**DMT (N,N-dimethyltryptamine)** — A short-acting psychedelic drug given here intravenously (20 mg of the fumarate salt over 30 s).

**double co-information (c)** — The four-variable co-information of the pair's past and future, which on the lattice equals rtr − sts.

**double redundancy (rtr)** — The atom for information that both regions carried redundantly in the past and both still carry redundantly in the future.

**early / late sets** — Post-hoc splits of the post-injection period into windows 6–9 and 10–14.

**effective samples** — The number of genuinely independent observations a stretch of autocorrelated data is worth; 60 consecutive TRs here are worth roughly 20.

**engine (inference engine)** — The one script (`notes/rev_inference.py`) that applies the same DiD, sign-flip test, bootstrap, phase null and motion control to every quantity.

**estimator** — The procedure that turns data into a number; here the Gaussian ΦID computation, either per window or once per run.

**even function (even in q)** — A function whose value is the same for q and −q, so it depends on q only through its size |q|.

**excess** — The paper's name for sts − (xtx + yty), the amount by which sts exceeds the two self-prediction atoms; the AR(1) family says it equals rtr.

**exploratory** — Reported without an inferential claim, because the test was not fixed in advance or was chosen after the primary result.

**family (AR(1) family, coupled family)** — A set of idealised model processes indexed by a few parameters (a, q, and for the coupled family c), on which the estimator's behaviour can be worked out exactly.

**FD (framewise displacement)** — A per-TR summary of how much the head moved between successive volumes.

**finite-sample null** — A simulation in which the model assumption is exactly true, so any residual it shows comes only from estimating with few samples.

**free choices (of a null)** — The settings a simulation leaves to its author (here the filter's per-pair heterogeneity and which autocorrelation shape is used), which have to be varied and reported.

**full mutual information** — The mutual information between the joint past (both regions) and the joint future (both regions).

**Gaussian estimator / Gaussian model** — The assumption that the data follow a multivariate bell-curve distribution, under which every information quantity is a function of correlations alone.

**git / git-tracked record** — The version-control system whose history fixes when each file changed; the record of decisions is kept in it so that ordering can be checked.

**global fit** — The estimator that fits one Gaussian to a whole 840-TR run and then reads off a value at each time point, averaged into bins; its per-bin values are not separate decompositions.

**global signal regression (GSR)** — A preprocessing step that removes the whole-brain average signal from every region's series, giving the ts_gsr variant.

**gradient (spatial)** — A smooth region-to-region rise or fall of a quantity across the cortex, such as synergy minus redundancy in Luppi et al. (2022).

**grid** — The set of (r₁, q) points, spaced 0.01 apart, at which the map was evaluated.

**group means (condition × window)** — The 28 values obtained by averaging over subjects for each of the two runs and fourteen windows.

**haemodynamic smoothing** — The blurring in time that the slow blood-flow response applies to neural activity, making BOLD series autocorrelated.

**hand case** — A tiny worked example (a 56-sample binary series) small enough to compute by hand, used to check the CCS code.

**HCP** — The Human Connectome Project, whose fMRI data have a fast TR of 0.72 s.

**HRF (haemodynamic response function)** — The characteristic slow rise and fall of blood flow that follows a burst of neural activity.

**identity** — An equation that holds exactly for every value of its variables, such as sts = xtx + yty + rtr on the AR(1) family.

**i.i.d.** — Independent and identically distributed, the assumption that successive samples are unrelated draws from the same distribution, which autocorrelated series violate.

**independent fit** — An estimate made from one window's samples alone, using nothing from other windows.

**inference row** — One line of a results file holding a DiD with its CI and p-values for one quantity, variant, estimator and window set; there are 474.

**innovation (ε, η)** — The fresh random noise added at each step of an AR process; the innovation correlation is the correlation between the two regions' noises.

**integrated autocorrelation time** — The number of consecutive samples that together are worth one independent sample, computed from the autocorrelation function (about 3 TRs here).

**integrated information** — A measure of how much a system's parts jointly do beyond what they do separately; ΦR is the version used in the workspace literature.

**intensity ratings** — Participants' 0–10 reports of how strong the drug experience was, given once per 30 TRs, here collected in a second session of the same day and not in the analysed run.

**lag (τ)** — The number of time steps between "past" and "future" in the decomposition; τ = 1 means one TR.

**lag-0 cross-correlation (q)** — The correlation between the two regions at the same time point.

**lag-1 autocorrelation (r₁)** — The correlation between a series and itself one TR later.

**lagged coupling / lagged interaction** — One region's past directly influencing the other region's next value, absent by construction from the AR(1) family.

**lattice (redundancy lattice, product lattice)** — The ordered diagram of all the ways two sources can share, split or combine information; ΦID uses the product of two such diagrams (past and future), and its nodes are where the sixteen atoms live.

**leave-one-out / leave-two-out** — Recomputing a result with each subject (or each pair of subjects) removed in turn, to check that no one or two subjects carry it.

**Lempel–Ziv complexity** — A measure of how compressible a signal is, used with EEG as an index of signal diversity in the original analysis (Supplement S1).

**level** — The value of a quantity in a given period, as opposed to its change.

**linear filter** — A processing step that forms each output value as a weighted sum of input values; the finite-sample null builds each pair by passing two correlated white noises through one filter.

**local (pointwise) atoms / local mutual information** — The contribution of a single time point to an information quantity, whose average over time points is the usual quantity.

**Lyapunov equation** — The matrix equation that gives the steady-state covariance of a VAR(1) process from its coefficients and noise.

**manufacture (estimator manufacture)** — A difference the estimator reports between two conditions whose true value of the quantity is identical, produced by finite samples and covariance changes.

**map (scope map)** — The picture of sts, and of its two derivatives, over all combinations of r₁ and q, with real pairs placed on it.

**mask (CCS sign mask)** — The rule that selects the time points at which CCS keeps the co-information; the published definition and the `phyid` code use different fifth sign conditions.

**matched null (sts-matched null)** — Pairs of simulated conditions built to have exactly equal true sts but different covariance, to see how much difference the estimator manufactures.

**maximum-entropy projection** — A step in the published version of Ince's CCS that computes the local quantities under a maximum-entropy distribution rather than the fitted one; the paper says it is not used here and does not describe it further.

**Möbius inversion** — The bookkeeping that turns the cumulative quantities on the lattice into the individual atoms by subtraction, which under MMI can give negative atoms.

**mean-filled parcel** — A region whose time series was replaced by a constant (its mean) in the released data; region 20 in one subject's DMT run, dropped everywhere.

**mirror atoms** — The four atoms xts, yts, stx, sty, which on the AR(1) family under MMI are each −(S − C) and offset the synergy block.

**MMI (minimum mutual information)** — The redundancy definition that takes the shared information of two sources about a target to be the smaller of the two individual mutual informations.

**motion control (FD residualisation)** — Within each subject and run, regress window values on window-mean head motion and recompute the contrast on what is left.

**multiplicity** — The problem that running many tests makes some of them come out "significant" by chance; the paper applies no correction and instead states how much weight each result gets.

**mutual information (MI)** — How much knowing one quantity reduces uncertainty about another, measured in nats; for Gaussian variables it depends only on their correlation.

**N = 14** — The number of subjects, each with a DMT run and a placebo run.

**nats** — The unit of information when logarithms are natural (base e); one nat is about 1.44 bits.

**net synergy** — In Barrett (2015), the joint mutual information minus the sum of the two individual ones, positive when the sources together carry more than separately.

**node (of the lattice)** — One position on the lattice diagram, corresponding to one way of combining sources and targets; the paper's double co-information c is a signed sum over the fifteen non-bottom nodes.

**non-stationary** — Having statistical properties (mean, variance, autocorrelation) that change over the course of the run, as an injection run does by design.

**null model / null distribution** — The distribution a statistic would have if nothing real were going on, obtained by relabelling, resampling or simulating; a result is judged against it.

**OLS** — Ordinary least squares, the standard straight-line fit.

**operating point** — The typical (r₁, q) location of real BOLD pairs, taken as (0.85, 0.25), at which the paper quotes every derivative.

**overlay** — Real pairs plotted as points on the map.

**pair** — Two regions considered together; 115 regions give 6,555 pairs.

**parcellation / parcel / region** — A division of the brain into named areas (Schaefer's 100 cortical parcels plus 16 subcortical ones), each yielding one averaged time series.

**Part B** — The set of five scope-and-diagnostic analyses (scope map, CCS, lag dependence, diagnostic, literature table) planned after the review computations, later extended by items 6–8.

**partial correlation (partial r)** — The correlation between two quantities after the linear influence of a third has been removed from both.

**permutation test (sign-flip)** — Ask whether the DMT and placebo labels matter by recomputing the group statistic for every one of the 2¹⁴ = 16,384 ways of flipping each subject's sign, and seeing where the real value falls.

**per-pair vs whole-brain** — Per-pair quantities are computed for each of the 6,555 region pairs; whole-brain values are their means.

**phase randomisation** — Building a surrogate series that keeps the original's frequency content but scrambles the timing of its rhythms, to test whether a contrast could arise from the series' own temporal structure by chance.

**ΦID (Phi-ID, integrated information decomposition)** — The extension of PID to the past and future of two variables, giving sixteen atoms.

**ΦR (Phi-R)** — A measure of integrated information built from the atoms, TDMI − I(X;X′) − I(Y;Y′) + rtr, used in the synergistic-workspace papers.

**ΦWMS** — A measure named in the ΦID authors' worked example that the paper mentions but does not define or use.

**phyid** — The Python software package that computes ΦID atoms, pinned to a specific code commit.

**PID (partial information decomposition)** — The framework that splits the information two sources carry about a target into redundant, unique and synergistic parts.

**placebo (PCB)** — The control run of the same form in which a placebo instead of DMT was injected.

**plug-in estimate** — Computing a quantity by inserting the sample correlations into the formula as if they were the true ones.

**pooling (of segments)** — Fitting one model to a run whose segments have different parameters, so that the fitted cross-lag correlation need not equal the product of the fitted autocorrelation and correlation.

**population value** — The value a quantity would have with infinite data, as opposed to its finite-sample estimate.

**positive control** — An analysis expected to show the effect if the method works at all, here the W = 30 windowed estimator, run to confirm the primary W = 60 result rather than to decide anything.

**post-hoc** — Added after the primary result was known; reported as such.

**pre-run entry** — A dated record entry made before a computation is run, holding its rule and, where there is one, its prediction.

**pre-specification / pre-registration** — Writing down the hypothesis, analysis and decision rules, and time-stamping them, before the result exists.

**primary contrast** — The one pre-specified test that carries inferential weight: whole-brain MMI-sts, ts_gsr, W = 60, windows 6–14 versus 1–4, DMT minus placebo.

**proportionality (sts / TDMI ratio)** — Whether sts fell by the same fraction as the total information TDMI, tested post hoc by a DiD of the ratio.

**p-value (sign-flip p, phase p)** — The fraction of null-model outcomes at least as extreme as the observed one; the paper reports two, from the sign-flip test and from the phase-randomised surrogates.

**q** — The lag-0 cross-correlation between the two regions of a pair (the same-time correlation), the second input of the map.

**r₁ (lag-1 autocorrelation)** — The correlation between a region's series and itself one TR later, the first input of the map; the paper's central quantity.

**rating bins** — The 28 one-minute bins in which intensity ratings were originally given, kept as averaging units.

**REC** — Research Ethics Committee, the body that approved the original study; its reference number is still to be obtained.

**record (analysis record)** — The append-only file `manuscript/analysis_record.md` in which every decision, prediction and result was entered with a date, and never edited afterwards.

**redundancy** — Information about the future that both regions' pasts carry, so that either would do.

**redundancy function** — The definition chosen for redundancy (MMI or CCS here), from which every other atom follows by the lattice bookkeeping.

**reference implementation** — An original, trusted version of a computation (here the MATLAB PhiID code) against which a new implementation is checked; it covers MMI only.

**regional test** — A per-region analysis, as opposed to a whole-brain average; the paper's regional test correlates each region's sts with its lag-1 autocorrelation across the 115 regions.

**reliability ceiling** — The largest correlation two quantities could show given their reliabilities, √(rel₁ × rel₂), even if their true values were perfectly correlated.

**reliability (split-half)** — How well a per-subject quantity agrees with itself when computed from two separate halves of the windows.

**residual** — What is left when the predicted value is subtracted from the observed value.

**residual diagnostic** — The per-pair procedure that predicts sts from the pair's measured (a_x, a_y, q) and tests whether the leftover changes under DMT.

**resting-state** — A scan with no task, used to study the brain's spontaneous activity.

**review computation** — A calculation that was run by one of the adversarial reviews, before any record entry and without a pre-recorded rule, and is reported as such.

**rsHRF** — A software toolbox for HRF deconvolution of resting-state data.

**r_τ** — The autocorrelation at lag τ TRs.

**run** — One continuous 840-TR (28-minute) scan; each subject has a DMT run and a placebo run.

**S** — The paper's shorthand for the self-information on the AR(1) family, S = −½ ln(1 − a²), the mutual information between a region's present and its own next value.

**sandbox** — A separate software environment needed to run the HRF-deconvolution scripts, which `run_all.sh` skips if it is absent.

**Schaefer parcellation** — A widely used atlas dividing the cortex into 100 parcels grouped into seven networks.

**Schedule 1 drugs / Home Office licence** — The UK legal category that includes DMT and the licence needed to do research with it.

**scope map** — See map; it shows where on the (r₁, q) plane the estimator's dependence on r₁ or q is stronger, and where real pairs sit.

**scoping rule** — A pre-fixed rule (here TR ≈ 1–3 s) for which studies enter the applicability table, stated to be a boundary and not a judgement.

**seed** — The starting number for the random-number generator (20261120), fixed so that every random step can be reproduced exactly.

**self-information** — The information a process carries about its own future, S on the family.

**self-prediction atoms (xtx, yty)** — The atoms for information that was unique to one region in the past and is unique to the same region in the future, i.e. each region predicting itself.

**sensitivity analysis / sensitivity set** — Repeating an analysis under a different reasonable choice (the ts_demean variant, or windows 5–14) to see whether the result depends on it.

**shrinkage (absorbed difference)** — The fraction of a true between-condition difference that the windowed estimator fails to report because of finite-sample bias.

**sign condition** — The requirement, in CCS, that a set of local information quantities all have the same sign for a time point to count.

**sign-blind criterion** — A test rule that scores the strength of a relation regardless of its direction, adopted for intensity tracking so that a decrease could not be reported as a pass.

**signed mean pairwise correlation** — The average of q over all pairs keeping its sign, as opposed to the average of |q|.

**single-source, single-target mutual information** — The mutual information between one past variable and one future variable, four of them in a pair.

**slope** — The rate of change of one quantity per unit change in another.

**spatial map** — A picture of a quantity's value region by region across the brain.

**spectral centroid** — The "centre of mass" of a signal's frequency content within the band; a rise means the signal shifted towards faster fluctuations.

**spin test** — A spatial null for the correlation between two cortical maps: the parcels are rotated on the sphere many times (here 10,000 rotations of the Schaefer-100 parcels) and the correlation recomputed for each, so that the maps' spatial smoothness cannot by itself produce it.

**split-half test** — Computing a quantity separately on odd-numbered and even-numbered windows, so that agreement across halves shows something stable and agreement only within a half shows shared noise.

**stationary** — Having statistical properties that do not change over time.

**step contrast** — The pre-defined before-versus-after comparison, as opposed to a correlation with a time course.

**sts (synergy-to-synergy)** — The atom for information that only the joint past of two regions carries about their joint future; the quantity most fMRI synergy papers report.

**surrogate** — An artificial series built from the real one to embody a null hypothesis.

**synergistic workspace** — In Luppi et al. (2024), the set of regions ranked highest on synergy, proposed as the brain's integrative core for consciousness.

**synergy** — Information about the future that neither region's past carries alone but the two together do, like two halves of a code.

**TDMI (time-delayed mutual information)** — The total information the joint past of a pair carries about its joint future, equal to the sum of the sixteen atoms.

**temporal null** — The phase-randomised surrogate test of a contrast.

**tier (tier-2)** — The original analysis's label for its second-level claim, that synergy tracks the intensity ratings, which was declared void under its own controls (Supplement S1, Table S2).

**[TK]** — An editorial mark for a value or wording that no file yet holds and that has to be supplied before submission.

**TR (repetition time)** — The time between successive brain volumes, 2 s here; one TR is one sample of every region's series.

**trend correction** — A post-hoc check that subtracts a linear drift across the session (the placebo run's, or a shared one) before recomputing the contrast.

**TR-resolution (TR-local) series** — A quantity computed at every single time point rather than per window.

**ts_gsr / ts_demean** — The two released preprocessing variants: with global signal regression (primary) and demeaned without it (sensitivity).

**two-sided test** — A test that counts extreme outcomes in either direction as evidence against the null.

**unique information** — Information about the future that only one of the two regions' pasts carries.

**upstream commit** — The specific version of the data repository (77af7aa) that was cloned.

**VAR(1)** — A vector autoregressive process of order one, in which each region's next value depends on both regions' current values plus noise.

**variance** — The average squared distance of values from their mean, a measure of spread; the ratio of window variance to run variance is used to show that the DMT run is not stationary.

**Varley's identity** — The result that for two independent autocorrelated processes the MMI aggregate synergy equals one process's self-information.

**Vasa rotations** — The set of spherical rotations of the Schaefer-100 parcels supplied with the data authors' code (`rotated_Schaefer_100.mat`) that the spin test uses; the Vasa p averages the one-sided p over rotating either map.

**verification (of the correction note)** — A further check, after the third review, that re-traced the correction note's changes and led to wording fixes, the within-subject bands of Figure 4, Figure 5 and the leave-two-out computation.

**void (tier-2 verdict)** — The pre-specified outcome label meaning the intensity-tracking claim failed its own controls and is not made.

**W = 60 / W = 30 (window length)** — The number of TRs in each window of the windowed estimator: 60 TRs (two minutes, 14 windows per run) is primary and 30 TRs is the positive control.

**weighting rule** — The paper's stated rule that inferential weight goes to the primary contrast and to results with sign-flip and phase-randomised p both at or below 0.005 across variants; anything with p between 0.01 and 0.06 is reported but not treated as established.

**white noise** — A series with no autocorrelation at all, each value an independent random draw.

**window noise / estimation noise** — The random error that estimating from one window's twenty effective samples adds to every quantity computed from that window, shared by all quantities computed from the same window.

**windowed estimator** — The estimator that fits a separate Gaussian to each non-overlapping 60-TR window of a run.

**within-half correlation** — In the split-half test, the correlation between two quantities computed on the same windows, which shared noise can inflate.

**within-run variance change** — The DMT run's variance falling after injection relative to the whole run, which moves every local information value under a single run-level fit.

**workspace account** — The hypothesis, from the synergistic-workspace papers, that synergy indexes conscious level; the original study tested it by asking whether whole-brain synergy rises under DMT.

**Yeo networks** — The seven large-scale brain networks of Yeo et al. (2011) used to order the Schaefer parcels.

**Zenodo** — A public archive that gives datasets a permanent DOI.

**z-score / standardised** — A value expressed as its distance from the mean in units of the standard deviation, computed here within each window.

---

## The walk-through

### The title

*Lag-1 autocorrelation dominates the Gaussian-MMI synergy atom of integrated information decomposition: an analytic account, a residual diagnostic, and a within-subject test on DMT fMRI*

**(a) What it says.** Brain scans (fMRI) produce, for each brain region, a series of numbers over time. *Autocorrelation* is how much a series resembles itself shifted by a step: if the value now is a good guess for the value two seconds later, the series has high autocorrelation at lag 1 (lag-1 autocorrelation, written r₁). An everyday version: today's temperature is a good guess for tomorrow's, a coin toss is no guess at all for the next toss. *Integrated information decomposition* (ΦID) is a method that takes two regions' series and splits the information their past carries about their future into sixteen named pieces, called *atoms*; the atom everyone reports is *synergy* (sts), meant to capture information that only the two regions together carry, like two halves of a torn map. The title claims that when this atom is computed the standard way (assuming the data are Gaussian, i.e. bell-shaped, and using the "MMI" definition of redundancy), the number it gives is controlled mostly by r₁ — by how sticky each series is on its own — rather than by anything the two regions do jointly. "Dominates" is later given a number: a change in r₁ moves sts 32 times more than an equal change in the regions' correlation does, at the point where real pairs sit. The title also lists the three things the paper delivers: a formula (the analytic account), a test anyone can run on their own data (the residual diagnostic), and a demonstration on a real dataset where each person is scanned twice, once on DMT and once on placebo (the within-subject test). *Warning on the temperature analogy*: autocorrelation is about linear resemblance at a fixed step, not about trends; a series can drift upward all day and still have low lag-1 autocorrelation if it is jittery step to step.

**(b) Why it is there.** The title is the claim. It commits the paper to an estimator story, not a brain story: it does not say DMT changes synergy, it says the synergy number responds to autocorrelation. Every section either derives that (Methods), demonstrates it (Results 1–5), qualifies it (Results 4 and 6), or says what follows for other people's studies (Discussion).

**(c) What a sceptic asks.** *"Dominates" — dominates what, measured how?* The answer is in Results 2 (the derivative ratio at the operating point, 32; minimum on the |q| ≤ 0.6 grid 6.55) and Discussion, "What the finding is and is not" ("on this dataset the autocorrelation change predicts the sign and 114 % of the magnitude of the sts change, and the per-subject collinearity is 0.95"). *Isn't "analytic account" too strong for a formula that the data violate?* The paper concedes this itself: Results 1 says the closed form "is an account of the estimator's structure, exact on the family, and only approximate on these data", and the Limitations repeat it.

---

### Abstract — Background

**(a) What it says.** Most fMRI papers that report "synergy" use ΦID with the MMI redundancy definition (MMI = *minimum mutual information*; more below). One paper, Varley (2024), already showed something alarming: if you take two series that have nothing to do with each other but are each autocorrelated, the MMI "synergy" between them is not zero — it equals the amount of information one series carries about its own future (its *self-information*). Three things were still unknown: which of the sixteen atoms this leaked self-information lands in; how the synergy atom sts depends on the two numbers a pair of BOLD series has (r₁, the lag-1 autocorrelation, and q, the same-time correlation between the two regions); and, when sts changes between two conditions, how much of that change is just a change in autocorrelation.

*Mutual information* is how much knowing one thing reduces your uncertainty about another — a weather forecast has high mutual information with tomorrow's weather. *Redundancy* is information that both sources carry (two witnesses who both saw the number plate). *MMI* is the rule that says: the redundancy between two sources about a target is the smaller of the two individual mutual informations. It is simple, but as this paper shows, it has consequences.

**(b) Why it is there.** It states the gap the paper fills. Without it a reader would think the paper is either a DMT paper or a repetition of Varley. The three "open" items are exactly the three deliverables of the title.

**(c) What a sceptic asks.** *Varley already concluded MMI should not be used; what is left to do?* The answer is Introduction paragraph 2: Varley's result is about an aggregate of four atoms and about what happens when a pair is "disintegrated"; nobody had said which atoms carry it, nor given sts as a function of (r₁, q), nor placed real pairs on that function, nor tested a real between-state change pair by pair. *Is "most fMRI synergy reports" documented?* Introduction paragraph 1 lists them (Luppi et al., 2022, 2024; Down et al., 2026; Nago et al., 2026; Zhang et al., 2025) and says "almost all of this work uses the Gaussian estimator with the MMI redundancy function"; Supplement S3 holds the table.

---

### Abstract — Methods

**(a) What it says.** Four things were done. First, a formula: for the simplest model of two autocorrelated series (a *bivariate AR(1) pair* — two series where each value is a fraction a of the previous value plus fresh noise, with the two noises correlated by q), all sixteen atoms were worked out exactly. Second, a map: sts was drawn over all combinations of r₁ and q, and real region pairs from the data were placed on it. Third, a comparison: MMI against a second redundancy definition, CCS. Fourth, a data test on 14 volunteers scanned on DMT and on placebo, comparing after-injection with before-injection on each drug and then subtracting the placebo change from the DMT change — a *difference-in-differences* (DiD). Because consecutive scan volumes are so alike, a 60-volume window (two minutes; TR, the time per volume, is 2 s) is worth only about 20 independent observations ("≈20 effective samples"). A *residual diagnostic* was added: for each pair of regions, predict what sts should be from the pair's own three measured numbers (its two autocorrelations a_x and a_y and its correlation q), and look at what is left over. Finally, a confession up front: the study did not start as any of this; it started as a pre-registered test of whether synergy goes up under DMT.

**(b) Why it is there.** It tells the reader the paper has an analytic part and an empirical part and that they are joined by the diagnostic. The last sentence is there because the History section later depends on it: the reader must know from the abstract that the hypothesis changed.

**(c) What a sceptic asks.** *Why an AR(1) model when BOLD series are not AR(1)?* The paper's answer (Methods, "The residual diagnostic"): the τ = 1 atoms depend only on lag-0 and lag-1 correlations, so the family's statements about (r₁, q) are statements about the estimator that hold whatever the process, and the only place the AR(1) assumption enters the diagnostic is the cross-lag substitution. *20 effective samples for a 4 × 4 fit — is that a serious estimator?* Methods, "Bias simulations" and Results 6 characterise the consequences; the paper does not hide them.

---

### Abstract — Results

**(a) What it says.** The formula came out as sts = −ln(1 − r₁²) + ½ ln(1 − r₁²q²), and this equals the two self-prediction atoms plus the double-redundancy atom: sts = xtx + yty + rtr. In words: on this model, "synergy" is each region predicting itself, plus a little redundancy, and four other atoms come out *negative* to balance the books (more on negative atoms under Results 1). The slope of sts with respect to r₁ is 32 times steeper than its slope with respect to q where real pairs sit. On the data the identity holds to 7 %, but the small leftover has the wrong sign: sts is 0.084 nats *below* xtx + yty, whereas the model says it should be *above* by rtr = 0.039. (A *nat* is the unit of information when you use natural logarithms; one nat is about 1.44 bits.) Under DMT the whole-brain sts fell (DiD −0.0809 nats, p = 0.0038), and so did r₁ (−0.0146, p = 0.0106, a measurement that was not planned in advance), and across the 14 people the two changes track each other at r = 0.953. The per-pair prediction reproduced the sts level to 4.3 % and the per-person DiD at r = 0.989, but over-predicted the group DiD by 14 %; a simulation with only finite-sample error in it (a computation of the second adversarial review, not pre-planned) accounts for a third to two-thirds of that leftover (+0.0037 to +0.0077 of +0.0115, p = 0.042). Under CCS, sts does not follow r₁ across pairs (r ≈ −0.01, against +0.7 for MMI) and it went *up* under DMT (labelled exploratory); its per-person change correlates with the leftover's at 0.80, but a test designed to tell real shared signal from shared noise had been set with a threshold no reliable measurement could reach, so it could not decide; the paper reports no autocorrelation-independent effect.

**(b) Why it is there.** It is the compressed evidence chain: formula → map → data agreement → data disagreement → residual → null → CCS → undetermined. Each clause maps to one Results section (1, 2, 3, 4, 3, 4).

**(c) What a sceptic asks.** *You say the identity "holds to 7 %" and in the same breath that the sign of the excess is wrong — which is it?* Both: 7 % is the size of the gap between sts and xtx + yty relative to their size; the sign of that gap is opposite to the model's. Results 1 gives the numbers (1.1554 against 1.2398; −0.084 against +0.039). *"Not significantly per subject (N = 14)" — not significantly what?* The abstract compresses: it means the per-subject CCS-sts DiD is not significantly correlated with the per-subject autocorrelation DiD (Results 3: r = −0.420 at the primary cell, all four cells p ≥ 0.127). The revised abstract says it: per subject the CCS-sts DiD is not significantly correlated with the r₁ DiD, a bound on the dependence rather than independence.

---

### Abstract — Conclusions

**(a) What it says.** Whenever two states or two groups differ in r₁, an MMI-sts contrast between them will be mostly the r₁ difference. Here the per-pair diagnostic's prediction from each pair's (a_x, a_y, q) gives the sign of the sts change and 114 % of its size (the revised abstract names which of the paper's three autocorrelation-based figures the 114 % is). Three practical instructions: always report r₁ next to sts; run the diagnostic; consider CCS or a longer lag.

**(b) Why it is there.** It converts the finding into a rule for other people's papers. The 114 % figure is the single number the paper most wants remembered: the autocorrelation explanation does not fall short of the observed change, it overshoots it.

**(c) What a sceptic asks.** *If r₁ explains 114 %, why is there a "remainder" at all?* Because 114 % is an over-prediction, and the over-prediction (the residual DiD, +0.0115) is itself significant at p = 0.042 and only partly reproduced by the null; Results 4 and Discussion, "What the finding is and is not", say the rest "is not located". *Why recommend CCS if you also say CCS has no established reading?* The paper is careful: "consider CCS", and Discussion, "Redundancy functions", says "CCS is not offered as the corrected estimator, only as the one whose sts does not carry the autocorrelation contrast the way MMI-sts does".

---

### Introduction — paragraph 1 (what ΦID is and who uses it)

**(a) What it says.** *Partial information decomposition* (PID) is a framework for asking, when two sources carry information about a target, how much of it is redundant (both have it), unique (only one has it), and synergistic (only the two together have it). ΦID applies this to time: the two "sources" are two regions' pasts and the "target" is their joint future, and because the future also has redundant/unique/synergistic parts, you get 4 × 4 = 16 atoms describing how each kind of past information becomes each kind of future information. The total being split is the *time-delayed mutual information* (TDMI), the information the joint past carries about the joint future. In fMRI the star atom is sts, synergy-to-synergy. Studies have found that it separates a redundancy-heavy sensory core from a synergy-heavy association cortex (Luppi et al., 2022), that the regions highest in synergy form a "synergistic workspace" whose integrated information drops under anaesthesia and in disorders of consciousness (Luppi et al., 2024), and that it differs between patient groups and controls in Alzheimer's disease, schizophrenia and neurodevelopmental conditions. Nearly all of this uses the Gaussian estimator (assume bell-shaped data, so everything is a function of correlations) with MMI at a lag of one TR, on BOLD series that are highly autocorrelated for two reasons: blood flow responds slowly to neural activity (haemodynamic smoothing), and the data are band-pass filtered (only slow fluctuations are kept).

**(b) Why it is there.** It establishes that the estimator under study is the one the field uses, so that a flaw in it matters. It also plants the two ingredients of the flaw — high r₁ from smoothing and filtering, and MMI — before the flaw is described.

**(c) What a sceptic asks.** *Is every cited study really Gaussian-MMI at τ = 1?* The paper says "almost all"; Supplement S3 (`notes/partB5_literature.md`) records what each study's Methods said and which could not be read. *Isn't the workspace result about ΦR, not sts?* Yes, and the paper keeps them apart: Results 3 reports ΦR separately and Discussion, "A distinction for applicability", says the r₁-dominance result "does not carry over to ΦR".

---

### Introduction — paragraph 2 (what was already known about MMI and autocorrelation)

**(a) What it says.** People knew MMI synergy and autocorrelation were tangled. Barrett (2015) found positive MMI "net synergy" in examples where a variable's own past is one of the sources. Varley (2024) showed, for the sum of the four atoms whose past side is synergistic (str + stx + sty + sts, the "aggregate forward synergy"), that MMI cannot tell a genuinely synergistic pair from two independent autocorrelated processes: if you "disintegrate" a pair (cut every link but keep each series' own autocorrelation), the MMI synergy equals the self-information of one of the processes (his Eq. 12), and how much it changes on disintegration depends on the pair's same-time mutual information (Eq. 13); on 1,000 region pairs of one person the change correlated with same-time mutual information at r = 0.97. He concluded MMI "should probably not continue to be used in its current form". Faes et al. (2025) state the general problem — PID on autocorrelated series under a hidden "independent samples" assumption misreads lagged structure — and propose a rate-based fix. The ΦID authors themselves have moved toward null-model normalisation (Liardi et al., 2025) and sometimes toward CCS. Their own worked example, back in 2021, was a coupled AR pair — so the model family used in this paper is the one the framework was introduced on. What none of this gives is an account at the level of the atoms people actually report: which atoms carry the self-information, how sts (not the aggregate) depends on r₁ and q, where real pairs sit on that dependence, whether CCS shares the property, and, for a real sts change, how much is autocorrelation and how to test the rest pair by pair.

**(b) Why it is there.** It is the priority statement. The paper must show it is not scooped by Varley and not made redundant by Faes or Liardi, and it does so by naming precisely what each left open. The remark that the ΦID authors' own worked example was a coupled AR pair pre-empts the objection that the AR(1) family is an unfair toy.

**(c) What a sceptic asks.** *Varley's Eq. 12 — is it general or only for discrete variables?* The paper says it is "derived from the additivity of mutual information under independence and the MMI maximum, so general rather than discrete-only". *Doesn't Liardi's null-model normalisation already fix this?* Discussion, "Redundancy functions", answers: that null preserves total mutual information but not autocorrelation, and it has not yet been reported for ΦID on BOLD; the two remedies are complementary.

---

### Introduction — paragraph 3 (how this study came to be, and what it gives)

**(a) What it says.** The study was not designed to do any of the above. It was pre-registered as a confirmatory test of whether whole-brain synergy rises under DMT — a state of intensified conscious content — against the workspace account's prediction that synergy indexes conscious level. Synergy fell instead. An adversarial review of the full sixteen-atom table then showed that the fall was carried by the atoms that carry the *level* — each region's prediction of itself — and that it was reproduced by the change in lag-1 autocorrelation; the formula in Methods was derived *after* that observation, to explain it. The question became what the estimator measures. The paper then lists what it delivers: the closed form; the identity sts = xtx + yty + rtr on the AR(1) family; the (r₁, q) map with the derivative ratio and the location of real pairs; the same map with lagged coupling; the CCS comparison under the published definition; the lag dependence; the residual diagnostic with its null; and the DMT contrast as the test case, including the sign violation and the remainder the data add. The original analysis and its results are in the supplement.

**(b) Why it is there.** This is the paragraph that keeps the paper honest and that reviewers will read twice. It tells the reader, before any result, that the hypothesis failed, that the reframing came after seeing the data, and that the formula was derived to explain an observation rather than predicting it. Without it the History section would look like a confession buried in Methods.

**(c) What a sceptic asks.** *So the "analytic account" is a rationalisation written after the fact?* The paper says so in plain words here and again in Results 1 ("the form was derived after this table had been inspected"). The defence is not that it was predicted but that it is exact (checked to 4 × 10⁻¹⁵, Methods, "Closed-form atoms") and that it made testable predictions afterwards — the diagnostic, the lag dependence (whose direction *was* recorded in advance, Results 5), and the CCS contrast. *Why should a reader care about a study whose hypothesis was wrong?* Because the reason it was wrong is the finding: the quantity it was stated on does not measure what the hypothesis needed (Discussion, "What the finding is and is not").

---
### Methods — Dataset

**(a) What it says.** The data are not new scans. They are the processed regional time series that Singleton et al. (2025) released on GitHub and Zenodo, from the DMT study of Timmermann et al. (2023). Fourteen people each have two runs of 840 volumes (TR = 2 s, so 28 minutes), one with an intravenous DMT injection at volume 240 (eight minutes in; 20 mg DMT fumarate over 30 s) and one with a placebo injection. Six of the original twenty participants had already been removed by the data authors for head movement. The intensity ratings that come with the data (0–10, once per 30 volumes, 28 "bins") were collected in a *second* session later the same day, not during the analysed run, so they enter no result in the main text. Head motion per volume (*framewise displacement*, FD) is supplied. Two versions of the series were analysed: one with *global signal regression* (the whole-brain average signal removed from every region; `ts_gsr`, primary) and one without (`ts_demean`, sensitivity). The series were band-pass filtered to 0.01–0.08 Hz — only fluctuations slower than one cycle per 12.5 s and faster than one per 100 s are kept — and this filtering alone gives even pure noise a lag-1 autocorrelation of about 0.82 at TR = 2 s. One volume in one placebo run was missing and dropped. The brain was divided into 100 cortical parcels (Schaefer atlas) plus 16 subcortical ones. One parcel (region 20, left dorsal-attention) was constant across the whole DMT run of subject 8 in every version of the data; the data authors confirmed it had been filled with its mean. It was dropped for everyone, leaving 115 regions and 6,555 pairs. The data have no licence file; both data authors confirmed by email that they may be used with attribution. Whether the time-series files and the motion files list the subjects in the same order was checked for one subject.

**(b) Why it is there.** A reader needs to know that the design is within-subject (each person is their own control), that the ratings do not belong to the analysed run (which matters for Supplement S1), that the filtering already imposes high r₁ (which is the mechanism), and that one bad parcel was removed before any result rather than after. The licence sentence and the subject-order sentence are the paper's due diligence on reusing someone else's data.

**(c) What a sceptic asks.** *If the ratings are from another session, the whole "synergy tracks intensity" design was broken from the start, wasn't it?* The paper says the ratings "enter no result in the main text" and puts the original analysis in Supplement S1, where the intensity-tracking claim was void under its own controls anyway (Table S2). *Subject order verified at one subject only?* Stated as such: the paper (Methods, Dataset) cites the record entry "Subject alignment across files" and does not say that the data authors have confirmed the order. If the order were wrong, the motion control would regress each subject's values on someone else's motion.

---

### Methods — Estimator

**(a) What it says.** The atoms were computed with `phyid`, the Python package for ΦID, pinned to an exact code version. It fits a *Gaussian model* — assumes the four numbers (region X now, region Y now, X next volume, Y next volume) follow a bell-shaped joint distribution, so that every information quantity is a function of the six correlations among them — and returns sixteen "local" atoms at every time point, in nats. Whole-brain values are the average over the 6,555 pairs. Two ways of fitting were used. *Windowed*: cut each run into 14 non-overlapping windows of 60 volumes and fit each window on its own (W = 60, the primary); also W = 30 with 28 windows. *Global fit*: fit one Gaussian to the whole run, then average the per-volume local atoms into the 28 rating bins. The catch is how few independent observations a window contains. The placebo runs' autocorrelation function (0.868 at lag 1, 0.539 at lag 2, 0.172, −0.085, −0.174, −0.145 at lags 3–6) implies that about 3 consecutive volumes are worth one independent sample, so a 60-volume window is worth about 20 samples for a fit that has to estimate a 4 × 4 correlation matrix. The consequences are characterised later. For the algebra, the authors wrote a closed-form version of the same computation: the time-average of `phyid`'s local Gaussian mutual information equals the textbook "plug-in" mutual information (half the log of a ratio of determinants of correlation matrices), and the step that turns redundancies into atoms is linear, so a window's mean atoms are an explicit function of that window's 4 × 4 correlation matrix. This reproduces `phyid` to about 10⁻¹⁴ on every saved output. Software versions and the machine are listed.

**(b) Why it is there.** Reproducibility (exact code version, seed, versions) and the two estimators, whose disagreement (Results 6) is part of the story. The closed-form implementation is what makes the scope map and the diagnostic possible: you cannot draw sts as a function of (r₁, q) by running a fitting routine on simulated data, you need the formula. The "20 effective samples" sentence is the paper's early warning that the windowed numbers are noisy and biased.

**(c) What a sceptic asks.** *Where does "about 3 TRs" come from?* The paper gives the six autocorrelation values and the phrase "integrated autocorrelation time" but not the formula; with the usual definition (1 + 2 × the sum of the autocorrelations) those six values give about 3.4, which the paper rounds to 3 (my arithmetic); the revised sentence names the definition, 1 + 2 Σ r_k, and cites the record's ≈ 2.8 over the eight lags it tabulates. *Is the closed form valid for CCS too?* The linearity argument holds for MMI; CCS keeps or discards each time point by a sign rule, so it is not a function of the window's correlation matrix alone. The paper now says so: the closed form holds for MMI, and the same module evaluates the CCS atoms pointwise because the sign masks are applied per sample (Methods, Estimator).

---

### Methods — The two redundancy functions and the CCS definition check

**(a) What it says.** Two ways of defining redundancy are compared. Under *MMI* (Barrett, 2015) the redundancy of two sources about one target is the smaller of the two mutual informations, and the "double redundancy" rtr — redundant in the past and redundant in the future — is the smallest of the four mutual informations between one past variable and one future variable. Under *CCS* (Ince, 2017) redundancy is decided moment by moment: at each time point you compute a three-way quantity called the *co-information* (positive when information is shared, negative when it only appears in the combination), and you count it as redundancy only at the time points where it and the mutual informations it is built from all have the same sign; elsewhere you count zero. For the double redundancy, the ΦID authors define (2021, Definition 1; 2025, SI Appendix, Definition 2) a four-variable version, the pointwise double co-information c, and keep it at time points where the four one-past-one-future mutual informations *and the full mutual information* (joint past with joint future) all share a sign. The `phyid` code, the paper found, uses a different fifth sign: c's own sign rather than the full mutual information's. Because on the lattice c is identically rtr − sts, CCS-sts is zero at the kept time points and −c at the others, whichever mask is used. The authors had earlier checked `phyid`'s single-target CCS against an independent implementation (agreement to 10⁻¹³) but its double redundancy only against the code's own algebra, since the MATLAB reference implements MMI only. So in this revision they implemented the published definition directly, ran it beside `phyid`'s on the same samples, and fixed in advance a rule: the two "agree" if every whole-brain CCS-sts level and DiD differs by less than 0.001 nats and no p-value crosses 0.05; otherwise every CCS number in the paper is the published-definition one. They differed (Results 1), so the paper uses the published definition throughout and gives `phyid`'s beside it. The journal version of the definition (2025) was checked and retains the same sign condition. CCS is computed on the fitted Gaussian of the data, as in Ince's original preprint, not with a "maximum-entropy projection" from Ince's published version.

*Lattice*: the ordered diagram of all the ways two sources can share, split or combine information; ΦID uses the product of two such diagrams (one for the past, one for the future), and its nodes are the sixteen atoms' addresses. Turning the redundancy values at each node into atoms is a subtraction scheme called *Möbius inversion*, like recovering daily spending from a running total.

**(b) Why it is there.** The CCS comparison is one of the paper's three main pieces of evidence that the property is specific to MMI, so the CCS numbers have to be right. The paragraph discloses that the standard code and the published definition disagree, says which the paper uses and why, and pre-commits the rule so the choice cannot be accused of being made after seeing which looked better.

**(c) What a sceptic asks.** *You found a discrepancy between `phyid` and the published definition — does that invalidate published CCS results?* The paper limits itself: the two masks differ on 6–7 % of samples and the whole-brain values by 0.002–0.012 nats (Results 1), and "the qualitative statements [are] unchanged" (Discussion, "Redundancy functions"); it makes no claim about other studies. *Why the fitted Gaussian rather than the maximum-entropy projection?* The paper says only that it follows the ΦID authors' usage ("As there") and Ince's original preprint; the revised sentence defines the projection in a clause and says that its effect on these data is not evaluated (Methods).

---

### Methods — Closed-form atoms of a bivariate AR(1) pair

**(a) What it says.** Take the simplest model of two sticky series. Region X's value at time t is a times its previous value plus fresh noise ε; Y likewise with noise η; the two noises are correlated by q. Both series are scaled to variance one. Then: X now correlates with X next at a; X now with Y now at q; X now with Y next at a × q (Y next is a × Y now plus noise, and only the "a × Y now" part relates to X). Put these into the 4 × 4 correlation matrix S₄ of (X now, Y now, X next, Y next). For Gaussian variables every mutual information is half the logarithm of a ratio of *determinants* (a single number computed from a square matrix) of blocks of that matrix. Two quantities do all the work: S = −½ ln(1 − a²), the information X now carries about X next (its *self-information*), and C = −½ ln(1 − a²q²), the information X now carries about Y next (the *cross-lag* information). Then: X now about (X next and Y next together) is still just S — Y next adds nothing that X's own next value didn't already contain; the total TDMI, joint past about joint future, is 2S, and does not depend on q at all. MMI then sets every "one source, one target" redundancy to C (the smaller of S and C), the two "one source, joint target" ones to S, and rtr = C. Running the Möbius inversion gives: the six cross-prediction atoms are all zero; xtx = yty = rts = str = S − C; the four "mirror" atoms xts, yts, stx, sty are each −(S − C) — negative; and

sts = 2S − C = −ln(1 − a²) + ½ ln(1 − a²q²).

In words: synergy-to-synergy is twice the self-information minus the cross-lag information. Consequences the paper draws: sts − (xtx + yty) = C = rtr (synergy exceeds the two self-prediction atoms by exactly the double redundancy; this "excess" is zero when q = 0 and grows with |q|); rtr + sts = TDMI; ΦR (the workspace measure, TDMI − I(X;X′) − I(Y;Y′) + rtr) equals C = rtr; and the two slopes are ∂sts/∂a = 2a/(1 − a²) − aq²/(1 − a²q²) and ∂sts/∂q = −a²q/(1 − a²q²). Varley's identity is the sum of four of these atoms at q = 0: (S − C) − 2(S − C) + (2S − C) = S. So the atom-level statement is: MMI puts the self-information into sts and into rts + str, and the four mirror atoms carry −(S − C) each so that all sixteen add to 2S. The model has a special property: Y now tells you nothing about X next beyond what X now already tells you (corr(Y now, X next) = corr(Y now, X now) × corr(X now, X next)), so every cross-prediction atom is zero, the pair's entire TDMI is self-prediction, and MMI assigns all of it except C to sts. The identities were checked numerically to 4 × 10⁻¹⁵ over 2,000 random (a, q) draws. When the two regions have different coefficients a_x ≠ a_y the same code evaluates the matrix numerically, and there ΦR − rtr is no longer zero.

*Why atoms can be negative*: the pie-chart picture of information being cut into slices breaks here. Under MMI the Möbius subtraction can produce negative pieces; the ΦID authors permit this (Mediano et al., 2021), and the four mirror atoms are the price MMI pays for putting so much into sts.

**(b) Why it is there.** This is the paper's theorem. Everything else — the map, the derivative ratio, the diagnostic's prediction, the interpretation of Table 1 — is this formula applied. It also shows exactly *how* Varley's aggregate result decomposes into atoms, which is the first of the three "open" items in the abstract.

**(c) What a sceptic asks.** *The formula says xtx = yty = rts = str; Table 1 has xtx = 0.6273 and rts = 0.5669. Why don't you mention that?* The paper reports the sign violation of the excess (sts − (xtx + yty) = −0.084 against +0.039) and, since the revision, the equality xtx = yty = rts = str as well (0.6273 and 0.6125 against 0.5669 and 0.5667, the mirrors matching −rts more nearly than −xtx), under the same "structural account, approximate on data" reading. *A model with no interaction — isn't the conclusion built in?* The paper agrees that the family "has no lagged interaction by construction" and adds the coupled family (next unit) to see what interaction does; the data statements (Results 3, 4) do not depend on the family being true, only on the estimator being what it is.

---

### Methods — The family with lagged coupling

**(a) What it says.** Because the AR(1) pair has no lagged link between the regions, anything it says about q is about same-time correlation only. To see what a real lagged influence does, the authors took a symmetric pair in which each region's next value depends on its own present (a) *and* on the other's present (c), with noise correlation q_ε, solved its steady-state covariance exactly (via the discrete Lyapunov equation), and for each c re-solved a and q_ε so that the pair's r₁ and q stay at the operating point (0.85, 0.25). This was added in this revision with no prediction recorded. Result: at fixed (r₁, q), sts changes with c at a slope of −1.77 nats per unit c and a curvature of +40 nats per unit c². The six cross-prediction atoms stay at zero for every c in this symmetric family. The excess sts − (xtx + yty) equals rtr only at c = 0: at c = +0.02 it is +0.005 while rtr = 0.028 (below rtr), at c = −0.02 it is +0.059 against rtr = 0.019 (above). The pair's cross-lag correlation departs from a_y q by about 0.94c. The conclusion: lagged interaction moves sts by amounts comparable to a change of a few hundredths in r₁ (whose slope is about 6 at this point), so the q-axis of the map must not be read as "the contribution of interaction".

**(b) Why it is there.** It answers the objection that the AR(1) family assumes away the very thing synergy is supposed to detect. It also supplies the mechanism the paper later uses to interpret the wrong-signed excess in the data: positive lagged coupling pushes the excess below rtr, which is what the data show (Results 1).

**(c) What a sceptic asks.** *"comparable to a change of a few hundredths in r₁" — for what value of c?* The paper gives the slope and curvature but never says what size of c is realistic; from its numbers, c = 0.02 moves sts by about −0.02 nats (−1.77 × 0.02 + 40 × 0.02²), which is about 0.003 in r₁, not a few hundredths (my arithmetic); the revised sentence quotes the table's sts values at c = ±0.02 and ±0.05 and converts them in words — of the order of a hundredth at |c| = 0.02, a few hundredths at |c| = 0.05 — and says no c is measured on the data. *Why is the coupling symmetric and why no prediction?* Stated as a limitation ("the coupled family is symmetric") and as a fact of the record ("entered ... with no prediction"); the Results use it only qualitatively (Results 1 and 4).

---

### Methods — The scope map

**(a) What it says.** Using the formula, sts, xtx + yty, and the two slopes were evaluated on a grid of r₁ from 0 to 0.95 and q from −0.6 to 0.6 in steps of 0.01 (slopes by *central differences*: nudge the input a tiny amount either way, h = 0.001, and divide), then on the wider |q| ≤ 0.95, and on the full square [−0.95, 0.95]² for the lag analysis. Because on this family the r₁-slope beats the q-slope at every single grid point except the line r₁ = 0, the map cannot be divided into an "r₁-dominated region" and a "q-dominated region" — there is no q-dominated region. What the map gives instead is the *ratio* of the two slopes at any point. Every region pair of subject 1 was then placed on it (the pair's r₁ = the average of its two regions' within-window lag-1 autocorrelations; its q = the pair's within-window correlation) for both data versions, both runs and windows 1–4 and 6, to read off where pairs sit and how large the ratio is there.

**(b) Why it is there.** The map turns the formula into a picture (Figure 2) and into the single number "32". It is also where the paper pre-empts a misreading of its own figure: the overlay does not show that pairs "fall in the dangerous region", because every region is dangerous; it shows the operating point.

**(c) What a sceptic asks.** *Why subject 1 only, and why windows 1–4 and 6?* The paper does not say why one subject suffices; the medians are reported (Results 2) and the whole-brain pairs' own point (0.848, 0.24) used for the projection agrees with them. *What does the map say about the brain?* Nothing — the paper is explicit that "the fact that all of a subject's pairs fall in the r₁-dominated region carries no information about the pairs" (Results 2).

---

### Methods — The DMT contrast

**(a) What it says.** For each person, the statistic is (after − before) on the DMT run minus (after − before) on the placebo run — the *difference-in-differences* (DiD) — applied to the whole-brain mean of whatever quantity is being tested. "Before" is windows 1–4 (bins 1–8, the first eight minutes). "After", in the primary analysis, is windows 6–14 (bins 11–28). Window 5 (bins 9–10, the two minutes after injection) was excluded before any windowed result existed, because the global fit on both runs showed an injection response at bins 8–10. The sensitivity analysis uses windows 5–14; early (6–9) and late (10–14) sets were added afterwards. Two tests of the group DiD: an *exact sign-flip permutation test* — if the DMT/placebo labels were meaningless, flipping the sign of each person's DiD should not matter, so compute the group mean for all 2¹⁴ = 16,384 flip patterns and see where the real one falls, two-sided — and a *subject bootstrap* 95 % confidence interval (re-draw the 14 people with replacement 10,000 times). A *temporal null*: phase-randomise each person's whole-brain time series (keep its frequency content, scramble its timing) 1,000 times, re-average into the same windows, and see whether the DiD could arise from the series' own rhythm. *Motion control*: within each person and run, regress the window values on the window-mean head motion (ordinary least squares over the 14 windows) and recompute the DiD on the residuals; "survives" means same sign with a bootstrap CI excluding zero. Two post-hoc *trend corrections*: subtract the placebo run's linear drift from both runs, or fit one shared slope to both. The same engine was applied to every quantity; MMI-sts is the only pre-specified one. The mean regional lag-1 autocorrelation is defined as: standardise each region within the window, multiply each value by the next (z_t z_{t+1}), average over regions — its window mean is the sample r₁ averaged over the 115 regions. That quantity, ΦR, and the sts-matched null were computed during the 14 September review, after the primary result, with no prediction. CCS-sts, the lag variants, the diagnostic and the literature table were set out in plans written after those review computations existed. Random seed 20261120 throughout.

**Multiplicity.** No correction for multiple testing. The result files hold 474 inference rows (79 quantity × variant × estimator combinations, each in six window sets); the phase-randomised null covers 316 of them and not the 158 trend-correction rows. The paper only quotes rows it names. Inferential weight goes to the pre-specified primary contrast and to results whose sign-flip *and* phase-randomised p are both ≤ 0.005 across both data versions; a p between 0.01 and 0.06 — the residual DiD at 0.042, CCS-sts at the primary cell at 0.056 — "is reported as such and is not treated as an established effect". The revised paragraph adds that this weighting rule is not pre-specified: it first entered the manuscript at commit 9318997 (15 September 2026, 08:47 UTC), after every result it governs existed, and has no record entry of its own.

**(b) Why it is there.** It fixes the inference so that every later number means the same thing, separates the one pre-specified quantity from the many that were not, and states the weighting rule by which the paper will later decline to read some of its own significant results. The DiD form is essential: the placebo run drifts across the session (Results 3), and a plain before/after on DMT alone would mix drug with time.

**(c) What a sceptic asks.** *Window 5 was excluded because of a response at bins 8–10 — but bin 8 is in your "before" set.* The revised Methods addresses it: the exclusion was fixed at whole windows, TR 240 is the end of bin 8 and a window boundary at both window lengths, so the pre-injection set is the four windows before it and bin 8, where the placebo rtr bump begins, stays in it; the record makes no separate decision about bin 8. The sensitivity set that includes window 5 gives the same sign (Table S1: −0.0733, p = 0.0070). *Your weighting rule requires both p ≤ 0.005 — the autocorrelation DiD that drives your whole account has sign-flip p = 0.0106 and phase p = 0.0729 on `ts_gsr` (Results 2). Doesn't it fail your own rule?* By the letter of the rule, yes, and the paper now says so in Results 2, in the sentence after the r₁ DiD. The account does not rest on that group-level p: it rests on the formula, on the per-subject collinearity of 0.953 (Results 3) and on the per-pair prediction at r = 0.989 (Results 4). *When was the weighting rule written?* Now stated in Methods, History and Limitations: it first entered the manuscript at commit 9318997 (15 September 2026, 08:47 UTC), after every result it governs existed, has no record entry of its own, and is not a pre-specified rule.

---

### Methods — The residual diagnostic

**(a) What it says.** For every pair, person, run and window you have a measured 4 × 4 correlation matrix and hence an observed sts. Now build a *predicted* sts: keep the pair's measured a_x, a_y (each region's own lag-1 autocorrelation) and q (their correlation), but replace the two measured cross-lag correlations (X now with Y next, Y now with X next) by what the AR(1) model says they would be, a_y q and a_x q, and compute sts from that matrix with the formula. The *residual* is observed minus predicted; both, averaged over pairs, go through the same inference engine. The plan written before the run named two possible outcomes: a residual DiD near zero (then the observed synergy change is accounted for by autocorrelation change), or a residual DiD that is significant *and* uncorrelated with r₁ (then it is exploratory evidence of a component that autocorrelation does not explain). Neither happened (Results 4). Because the lag-1 atoms depend only on lag-0 and lag-1 correlations, the AR(1) model enters the diagnostic at exactly one place: the cross-lag substitution.

Two additions in this revision, with rules recorded before they were run: the CCS definition check (above), and a *split-half test* of the correlation, across people, between the residual DiD and the CCS-sts DiD. Both DiDs were recomputed on odd windows only (pre 1, 3; post 7, 9, 11, 13) and on even windows only (pre 2, 4; post 6, 8, 10, 12, 14). Correlating quantities from the *same* windows can be inflated by shared window noise; correlating one quantity from the odd windows with the other from the even windows cannot. The rule: "not window noise" if both cross-half correlations are positive and their mean is at least half the within-half mean — in which case the two would be reported together as one exploratory observation of an autocorrelation-independent component in the direction of the original hypothesis, with a warning that it arose after four specification changes; "estimation noise" if the cross-half mean is below half the within-half mean or either is negative — then both are reported as null. That rule was written without considering the *reliability* of the two quantities — how well each agrees with itself across the two halves — and at the reliabilities observed, the pass threshold was higher than the largest cross-half correlation two perfectly correlated reliable quantities could produce. So the test could not discriminate; the flaw is recorded and the outcome reported as undetermined.

A third computation, the *finite-sample null* of the residual, is not the authors': it was written and run by the second adversarial review, before any record entry and with no rule. In it each pair is one linear filter (a band-pass 0.01–0.08 Hz times a Gaussian roll-off exp(−βf²), fitted to the placebo autocorrelation function: 0.872, 0.549, 0.179, −0.091, −0.196, −0.168 at lags 1–6) applied to two white noises correlated by q, so that the true cross-lag correlation is exactly r₁q and *every* residual is finite-sample error. For the DMT-post cell the filter is fitted to the post-injection DMT function. β and q vary across pairs so that the mean a and |q| match the four cells; 3,000 pairs × 50 windows per cell; the null is stationary by construction. The third review re-ran it and varied two free choices (per-pair filter heterogeneity; whether the DMT-post shape is applied); the paper quotes that range. One technicality: the residual's phase-randomised null scrambles the observed series against a fixed prediction, so it tests the observed series' temporal structure rather than the residual's construction; the sign-flip test and the bootstrap carry the residual inference.

**(b) Why it is there.** This is the paper's test that goes beyond collinearity: it asks, pair by pair, whether autocorrelation and correlation alone reproduce the sts numbers, and what is left. It pre-commits to two readings of the outcome, which is what lets the paper say later that neither obtained rather than choosing one. The split-half test is the attempt to settle whether the leftover is real; the null is the attempt to see whether the leftover is an artefact of estimating from 20 samples.

**(c) What a sceptic asks.** *You wrote a rule that could not pass — how did that happen?* The paper says it plainly: the rule "was set without reference to the split-half reliabilities of the two quantities", the ceiling is √(0.494 × 0.302) = 0.39 against a threshold of 0.41, and "that is a flaw in the rule, recorded as such" (Results 4; record, correction note of 15 September). *The null was written by a reviewer with no rule — why is it in the paper?* Because it is the only computation that can say how much of the residual is finite-sample, and the paper labels it a review computation every time it is mentioned and reports the range over its free choices rather than a single number.

---

### Methods — Bias simulations, the matched null, lag variants and deconvolution

**(a) What it says.** Before any windowed result, the estimator's *finite-sample bias* — the systematic error from having few samples — was measured on simulated VAR(1) processes (two-region autoregressive processes with known true atoms), 2,000 replicate windows per setting. The estimated sts difference between two conditions always had the true sign, but the estimator swallowed 52–77 % of the true difference at W = 30 and 15–45 % at W = 60; that is why W = 60 became primary and W = 30 the positive control. Because the real autocorrelation function decays faster than either simulated family, no simulated shrinkage number is applied to the real data. The *sts-matched null* (a review computation) asked the opposite question: can the estimator *manufacture* a difference between two conditions whose true sts is identical but whose covariance differs? Three families were built (the record's asymmetric VAR(1); a VAR(1) at a = 0.87; Gaussian processes with the data's own placebo and post-DMT autocorrelation functions), the second condition solved so that the true sts is unchanged, and the estimated difference measured over 4,000 windows at W = 30, 60 and 840. The *lag variants* repeat the decomposition with "future" two, three or five volumes ahead (τ = 2, 3, 5) on `ts_gsr`, windowed and global, with the lag-τ autocorrelation contrast built the same way; the plan recorded beforehand predicted that r_τ falls with τ and the artefact weakens. As a post-hoc exploration, the series were *deconvolved* (an attempt to undo the slow blood-flow response with rsHRF 1.7.0) and the pipeline rerun unchanged.

**(b) Why it is there.** The bias check justifies the window length; the matched null puts an upper bound on how much of a between-condition difference the windowed estimator can invent (Results 6); the lag variants test a prediction that was actually recorded in advance (Results 5); the deconvolution closes off a remedy readers will propose (Recommendations).

**(c) What a sceptic asks.** *Three families in Methods, "four matched pairs" in Results 6 — which is it?* The revised Methods explains it: the first family yields two pairs (F1-i, F1-ii), the second only its noise-correlation shift (F2-ii), the third a spectrum-tilted pair (F3-b); the ± figures are standard errors and the base is the real primary DiD, −0.0809. *If W = 60 swallows 15–45 % of a true difference, what does the observed −0.0809 mean?* The paper declines to correct it ("no simulated shrinkage figure is applied to the real contrast") and instead shows agreement with the global fit (−0.0801, Results 3), which does not have the per-window bias.

---

### Methods — Literature search for the applicability table

**(a) What it says.** On 14 September 2026 the authors searched the web for published fMRI ΦID studies reporting Gaussian-MMI synergy on BOLD at TR ≈ 1–3 s, and read each accessible Methods section for the quantity reported, preprocessing, parcellation, redundancy function, lag and any treatment of autocorrelation. The TR range was fixed before the search as a scoping rule, which places Luppi et al. (2022; TR 0.72 s) outside the set. For each study whose settings could be read, the table states which direction of r₁ change would, on the map, produce the reported effect — the same conditional sentence for every study, and not a claim about any study's data, since none reports regional r₁. The search record and the sources that could not be read are in Supplement S3.

**(b) Why it is there.** The paper's reach beyond one dataset is this table. The conditional form is the paper's way of saying "you are exposed" without saying "you are wrong".

**(c) What a sceptic asks.** *A web search on one day is not a systematic review.* The paper does not claim it is; it calls the TR range "a scoping rule, not a judgement" and lists the blocked sources. *Why exclude the most important study?* Discussion, "A distinction for applicability", addresses Luppi et al. (2022) separately and explicitly.

---

### Methods — History of the study

**(a) What it says.** A dated account of what was decided when, from the git record. The first commit (12 September 2026, 10:29) carries the up-regulation hypothesis, a statement that it was recorded before any results were inspected, and a 20-region real-data global fit written to disk seventeen minutes earlier whose DiD is negative in 12 of 14 subjects. The 115-region global fit was on disk at 10:15 on 13 September. The *directional-failure rule* — that a significant decrease would be reported as a refutation — was written after it and committed together with that result (10:40), immediately below the line "The direction is a DECREASE in synergy under DMT, opposite to the stated hypothesis". The sign-blind intensity-tracking rule (11:07) was adopted because the decrease was already known and a sign-blind rule could otherwise be gamed either way; the primary post set was moved from windows 5–14 to 6–14 (11:32) on real-data evidence. The windowed test's estimator, windows, nulls and motion rule were fixed before the windowed result existed, but the direction and rough size of the effect were known from the global fit, whose per-subject DiDs correlate at 0.95 with the windowed ones — "the git record establishes ordering, not blindness". The decrease was recorded on 13 September; the intensity-tracking claim was void. On 14 September an adversarial review with its own computations (the autocorrelation contrast and its collinearity with sts, ΦR, the trend corrections, the matched null, and a CCS decomposition on 400 random pairs showing an sts *increase* in 14 of 14 subjects) established that the decrease was carried by the self-prediction atoms and reproduced by the autocorrelation contrast. The study was reframed; an exploration of ΦR (including deconvolution and a regional test with a recorded prediction) was closed by a dated entry recording why its positive result supports no claim. The Part B plans (scope map, CCS, lag, diagnostic, literature) were written after those review computations, so the sign of every Part B outcome except the residual was known in outline beforehand; the plans fixed the computations and reporting rules and were committed one by one before each run. A second review (15 September) led to the CCS definition check and the split-half test, with rules recorded in a pre-run entry, and to the coupled family, with no prediction. The finite-sample null is that review's own computation. A third review the same day found the split-half threshold flaw, that the previous draft had called the null "pre-registered", and that Results 3 had dropped one of four proportionality cells; the corrections are in the record's correction note and nothing earlier was edited. A verification of that note led to wording fixes, the within-subject bands of Figure 4, Figure 5, and the leave-two-out computation, entered with no prediction before it was run.

**(b) Why it is there.** Because the abstract says the study "began as a pre-specified test" and a reviewer will want to know exactly what that pre-specification protects. This paragraph is the paper's answer, and it volunteers every weakness: the hypothesis commit came after a real-data result existed on disk; the refutation rule came after the refutation; the Part B plans came after the phenomenon was known. It also gives the timeline of the three reviews so that "review computation" has a meaning.

**(c) What a sceptic asks.** *Your hypothesis was committed seventeen minutes after a result showing the opposite direction was on disk. Was it looked at?* The revised History answers it: the hypothesis predates the fit, being the record's opening section, written before any script existed; the 20-region fit was a pipeline check under a setting the script's docstring marks as never to be reported from; it was inspected and showed a decrease; the initial commit carried both; and the hypothesis was kept as the workspace account's prediction rather than revised — while the record still "establishes ordering, not blindness". *Then what does the pre-specification establish?* That the windowed primary test's estimator, windows, nulls and motion rule were not tuned to the windowed result; that every later rule has a date; and that the direction of the effect was known before those rules and the paper says so (Limitations repeat it).

---
### Results 1 — The sixteen atoms under MMI and CCS, and a sign the data get wrong

**(a) What it says.** Table 1 and Figure 1 list all sixteen atoms twice — once under MMI, once under CCS with the published double-redundancy definition — as whole-brain averages in the DMT run before injection, and as DiDs. Under MMI the table looks the way the formula says it should (the formula was derived after looking at this table): sts (+1.1554 nats) is within 7 % of xtx + yty (+1.2398); rts and str are each about half of sts; and four big negative atoms (xts, yts, stx, sty, about −0.535 each) almost cancel the three big positive ones (sts + rts + str = +2.289 against −2.142). Under DMT the negative four went *up* while the positive three went *down*, so the net change of the block is only a small part of the change in the total TDMI (−0.1037). One thing does not match the formula: the family says sts − (xtx + yty) = rtr, a positive number, whereas the data give −0.084 nats at W = 60 against rtr = +0.039, and −0.053 at the global fit (1.3085 against 1.3616). The "excess" has the wrong sign, by 0.12 nats. The paper says this is the same fact as the diagnostic's over-prediction (Results 4) seen from the other side, and is consistent with the real autocorrelation function decaying faster than any AR(1): the formula describes the estimator's structure, exact on the family, approximate on the data. Two things could produce an excess below rtr — positive lagged coupling (the coupled family) or finite-sample scatter in the cross-lag entries — and the data do not separate them. Under CCS the self-prediction atoms and their DiDs are almost the same as under MMI, the mirror atoms and rts, str are near zero, and sts is *negative* and only 4 % of the MMI value in size (−0.0480); so "sts ≈ xtx + yty" is an MMI phenomenon, on both data versions and both estimators. `phyid`'s mask gives −0.0387 for the same quantity (DiD +0.0036 against +0.0044; the two DiDs correlate at 0.974 across people). The published mask keeps 35–38 % of time points (0.351, 0.365, 0.366, 0.384 in the four cells); in the two per-pair test windows it keeps 32–34 % against the code's 26–28 %, and the masks disagree on 6–7 % of time points. Their whole-brain values differ by more than the 0.001-nat agreement rule in every cell (0.002–0.012 nats), which is why the published values are used.

**(b) Why it is there.** It is the empirical version of the theorem: here are the sixteen numbers, and they have the shape the formula predicts, negatives and all. It is also where the paper shows the one place the data contradict the formula, before a reviewer finds it. And it discharges the CCS definition rule from Methods: the masks differed, so the published one is used.

**(c) What a sceptic asks.** *Four atoms that are supposed to be equal (S − C) differ by 10 % — xtx 0.6273 versus rts 0.5669 — and the mirror atoms (−0.535) are not the negative of xtx (0.627) either. Why report only the sign of the excess?* Results 1 now reports both departures — the excess sign and the equality xtx = yty = rts = str, which the data break by about a tenth — under the same sentence, that the form is "only approximate on these data". *Is the block's "small net change" a real statement?* Adding Table 1's DiDs, the block changes by −0.1624 and the four mirrors by +0.1607, a net of −0.0017 against a TDMI change of −0.1037 (my arithmetic on the table; the revised sentence gives the atoms' DiDs and the TDMI change beside the statement).

#### Table 1

**(a) What it says.** Sixteen rows, one per atom, plus a TDMI row that is the sum of the sixteen (+1.4772 and −0.1037 in every column — the three redundancy definitions split the same total differently). Columns: MMI level and DiD; CCS level and DiD under the published definition; the same under `phyid`'s mask. The number in brackets after each DiD is how many of the 14 people had a negative DiD. Read down the MMI column: the six cross-prediction atoms are tiny (±0.025), xtx and yty are 0.63 and 0.61, rts and str 0.57 each, the four mirrors −0.535 each, sts 1.1554. Read the DiD column: sts −0.0809 (13 of 14 negative), xtx −0.0523 (12), yty −0.0396 (13), rts and str −0.041 (12), the four mirrors +0.040 (only 2 negative each). Under CCS: xtx and yty and their DiDs barely move (0.6151, −0.0508; 0.6011, −0.0386); rtr is larger (0.0822); rts, str, and the cross-prediction atoms are near zero; the mirrors become small positives (+0.072); sts is −0.0480 with a DiD of +0.0044 (only 3 of 14 negative, i.e. 11 positive).

**(b) Why it is there.** It is the only place all sixteen atoms are printed, and the DiD-sign counts are the only per-subject consistency information for atoms other than sts.

**(c) What a sceptic asks.** *Your TDMI row is identical across definitions — is that a check or a triviality?* A triviality that is also a check: the atoms must sum to the same mutual information, so identical totals show the three decompositions were computed on the same fits. *Why no CIs in the table?* Figure 1b carries the bootstrap CIs; the table carries the counts.

---

### Results 2 — The scope map, the operating point of real pairs, and what DMT changes

**(a) What it says.** On the family, sts is symmetric in q (only |q| matters), decreases as |q| grows, and rises steeply with r₁ (Figure 2a): at q = 0 it is 0.041 at r₁ = 0.2, 0.446 at 0.6, 1.022 at 0.8, 1.282 at 0.85, 1.661 at 0.9, 2.328 at 0.95. At r₁ = 0.85 it only falls from 1.282 to 1.131 as |q| goes from 0 to 0.6. The r₁-slope beats the q-slope at every grid point except r₁ = 0 (0 exceptions out of 18,336 cells on |q| ≤ 0.95; 0 of 36,481 on the full square). So there is no region where q matters comparably, and the finding that all of a subject's pairs sit in the "r₁-dominated region" tells you nothing. What the overlay tells you is where the pairs sit and how large the ratio is there. At the operating point (0.85, 0.25) the slopes are 6.07 (per unit r₁) and −0.19 (per unit q), ratio 32; at (0.85, 0.6) they are 5.71 and −0.59, ratio 10. The ratio's minimum is 6.55 at (0.61, ±0.6) on the |q| ≤ 0.6 grid and 1.9 at (0.77, ±0.95) on the wider grid — parity is approached only at correlations far above what BOLD pairs have. Subject 1's pairs have median r₁ between 0.816 and 0.867 and median |q| between 0.22 and 0.41 across the cells examined. The lag-1 autocorrelation that ideal band-passed white noise would have at the published studies' settings is 0.78–0.93; real BOLD has its power at the low end of the band, so those are lower bounds (here 0.82 ideal against 0.866 measured); at those lower bounds the ratio is 25–60 at |q| = 0.25, rising to 131 at r₁ = 0.97. The same dependence shows pair by pair within one window: across subject 1's 6,555 pairs, MMI-sts correlates with the pair's r₁ at r = +0.742 (DMT window 6) and +0.697 (placebo window 2), so about half the between-pair variance of sts in a window is lag-1 autocorrelation (r² = 0.55, 0.49). Under CCS the same correlations are −0.011 and −0.018.

Then the data: DMT lowered r₁. The whole-brain mean lag-1 autocorrelation (a review computation) fell relative to placebo: DiD −0.0146 [−0.0251, −0.0052], sign-flip p = 0.0106, negative in 12 of 14, phase-randomised p = 0.0729, FD-residualised −0.0123, p = 0.0135 on `ts_gsr`; −0.0216, p = 0.0017, phase p = 0.0390 on `ts_demean`. Multiply the r₁ change by the slope at the pairs' own point (0.848, 0.24), where ∂sts/∂r₁ = 5.99, and you get −0.087 nats against an observed sts DiD of −0.081. On `ts_gsr`, DMT's effect on q is small on the map's scale: mean pair |q| went from 0.284 to 0.266 on DMT against 0.284 to 0.282 on placebo (DiD −0.0164, negative in 10 of 14, post-hoc), and 0.01 of |q| moves sts by only 0.002 at that point. On `ts_demean` q did move: the signed mean correlation rose from 0.190 to 0.233 on DMT (DiD +0.0526, p = 0.0470, 28 % of its baseline; a computation with no pre-specification entry); through a q-slope of about −0.15 to −0.23 that contributes about −0.01 nats, a tenth of the `ts_demean` sts DiD and in the same direction; the |q| DiD was computed on `ts_gsr` only.

**(b) Why it is there.** This is where the theorem meets the data at the coarsest level: one number (the r₁ change) times one slope reproduces the headline sts change. It also disarms the figure's most tempting misreading (that the pairs sit in a danger zone) and shows the same r₁ dependence across pairs within a single window, which does not depend on DMT at all.

**(c) What a sceptic asks.** *"DMT changes r₁" — with sign-flip p = 0.0106 and phase p = 0.0729, that fails the paper's own weighting rule.* True, and the paper now says so in the sentence after the r₁ DiD (Results 2). The answer is that the account rests on the per-subject and per-pair relations (Results 3 and 4), not on this p; the r₁ change is the input, its group-level p is not the evidence for the mechanism. *Why does the projection use (0.848, 0.24) and a slope of 5.99 when everything else uses (0.85, 0.25) and 6.07?* Because the projection is made at the pairs' own measured point; the paper gives −0.087 at 5.99 and does not report the value at 6.07, and the two points are a rounding apart. *"Lower bounds, not locations" — where is the evidence that BOLD power sits at the low end of the band?* Now two: the pre-injection in-band spectral centroid, 0.0369 Hz on DMT and 0.0374 Hz on placebo in a 0.01–0.08 Hz band (`rev_extra.log`), beside the ideal 0.82 against the measured 0.866 (Results 2).

---

### Results 2, added in the revision of 15 September 2026 — The regional test of the spatial-map claim

**(a) What it says.** The map says that a region with higher r₁ gets higher sts. The paper now asks, region by region rather than pair by pair, whether that holds on the placebo run before injection. For each of the 115 regions it takes the region's synergy — the mean over the 114 pairs the region belongs to, from the global-fit atoms saved by the regional analysis of `scripts/11_regional_analysis.py`, bins 1–8, `ts_gsr` — and the region's lag-1 autocorrelation (windowed, W = 60, windows 1–4), each averaged over the 14 people, and correlates the two across regions. The prediction, written into the record before the computation, was a positive correlation if the "spatial-map exposure" is real on these data. It is: Pearson +0.863 (Spearman +0.835) across the 115 regions; on the 99 cortical parcels Spearman +0.771 with spin p < 0.0001 over 10,000 Vasa rotations (a *spin test* rotates the cortical map on the sphere to build a null that keeps the map's spatial smoothness, so that neighbouring regions being alike cannot by itself produce the correlation); per person the correlation across regions is +0.756 [+0.715, +0.790], positive in 14 of 14. Three-quarters of the between-region variance of the baseline synergy map (r² = 0.745) is regional lag-1 autocorrelation, which ranges from 0.8118 to 0.8742 across regions. The synergy-minus-redundancy map, sts − rtr, correlates with regional r₁ at +0.792 (+0.618 on the cortical parcels, spin p < 0.0001), and rtr itself at +0.638 (spin p = 0.0002), where the family says ∂rtr/∂r₁ ≈ 0.06; rtr's spread across regions is a fifth of sts's (SD 0.0098 against 0.0447). The paper's reading: on these data a regional r₁ gradient and a regional sts gradient coincide, as the map says they must; it does not say which is the cause, since on these data the two cannot be told apart, and it says nothing about any published synergy map, none of which reports regional r₁.

**(b) Why it is there.** Before this revision the "spatial map" case of the Discussion — the case that bears on Luppi et al. (2022) — rested on the map plus the within-window pair correlations (r ≈ +0.7), and Limitations listed the regional test as not run. This is that test, with its prediction recorded first; it turns the conditional statement into one demonstrated on this dataset, and the Discussion's applicability paragraph and Limitations now cite it.

**(c) What a sceptic asks.** *sts is computed from a correlation matrix that contains r₁ — isn't a correlation between the two across regions guaranteed?* Not at this size: the paper's claim is precisely that the estimator makes sts follow r₁, and the test shows that dependence carries three-quarters of the between-region variance of real data (r² = 0.745); the map made the prediction, and it could have failed if the between-region variance of sts had been carried by something else. *So the synergistic core of Luppi et al. (2022) is autocorrelation?* The paper refuses that step in the same paragraph: the test shows the exposure is real here, "it does not say which is the cause", and it says nothing about a study whose regional r₁ is not reported. *rtr correlates with r₁ at +0.638 although the family says it should barely move — why?* The paper reports this as an observation outside the prediction, notes that rtr's spread is a fifth of sts's, and offers no explanation (Results 2; record, outcomes entry of 15 September 2026).

---

### Results 3 — The DMT contrast on MMI-sts, the autocorrelation contrast, CCS-sts and ΦR

**(a) What it says.** *The primary contrast (Table 2).* Whole-brain MMI-sts fell on the DMT run and rose on the placebo run: DiD −0.0809 nats [−0.1261, −0.0377], sign-flip p = 0.0038, phase-randomised p = 0.0020, negative in 13 of 14 people, −7.0 % of the pre-injection DMT mean, surviving motion control; without global signal regression −0.1031, p = 0.0026. It held at W = 30 (−0.0686, p = 0.0042), in the early and late sets (−0.1029, p = 0.0009; −0.0633, p = 0.0337 — with the placebo rise carrying 0.69 of the late DiD), under both trend corrections (−0.0890, p = 0.0021; −0.0995, p = 0.0007), and in all 28 leave-one-out refits. The global fit gives the same contrast (−0.0801, p = 0.0071), but that is two estimators agreeing on one within-run contrast, not independent confirmation, because the global fit's bins are local values under a single run-level fit and feel the within-run variance change (Results 6). The pre-specified direction was an increase, so under the directional-failure rule this is a refutation. A post-hoc check with its rule recorded first tested whether sts fell *in proportion* to the total TDMI (ratio sts/TDMI, four cells): three cells are proportional (W = 60 `ts_gsr` ratio DiD +0.0005, p = 0.91; `ts_demean` −0.0095, p = 0.22; global `ts_demean` +0.0071, p = 0.56) and one is less than proportional — the global fit on `ts_gsr`, the very estimator Results 6 recommends, where the ratio *rose* (+0.0204, p = 0.025; sts carried 0.66 of the TDMI drop against a baseline share of 0.91). Proportionality is what the map predicts for an r₁-driven change (on the family the sts-slope is 0.99 of the TDMI-slope at the operating point), and the primary estimator gives it (sts is 0.78 of TDMI and carries 0.78 [0.65, 0.94] of its DiD, against 0.98 on the family); the paper does not offer proportionality as confirmation of the mechanism. The baseline shares differ between estimators (0.78 windowed, 0.91 global) because the windowed estimator's finite-sample bias hits the atoms unequally.

*The autocorrelation contrast.* Per person, the sts DiD and the lag-1 autocorrelation DiD correlate at Pearson r = 0.953 (Spearman 0.903) on `ts_gsr` and 0.96 (0.93) on `ts_demean` (Figure 3a). Dropping every pair of people in turn (91 refits) gives r from 0.846 to 0.973, median 0.954, lowest without subjects 8 and 14, the two farthest from the cloud. Across the 28 run × window group means the two series correlate at 0.977 and 0.938. The autocorrelation contrast has the sts contrast's structure in every respect examined: the placebo run's r₁ rises across the session and carries 0.34 of the DiD (sts: 0.40); the early set is larger (−0.0213, p = 0.0006) than the late (−0.0093, p = 0.1615); both survive the trend corrections. Two things keep them from being identical. First, r = 0.953 leaves 9 % of the per-subject variance, "which the diagnostic finds significant" (Results 4). Second, under the temporal null the sts DiD sits 3.8 null standard deviations out (phase p = 0.0020) while the autocorrelation DiD sits 1.8 out (p = 0.0729), a difference the phase-randomised surrogate of a bounded, window-standardised statistic "does not by itself explain".

*CCS-sts (Table 3).* Under the published definition, CCS-sts does not track r₁ the way MMI-sts does — the data show that much, not independence. Per pair within a window it is uncorrelated with r₁ (r = −0.011, −0.018 against +0.742, +0.697), but a zero correlation for a quantity of low reliability (split-half 0.30 per subject) bounds the dependence rather than excluding it. Across the 28 group means it correlates with mean r₁ at −0.639 (MMI-sts: +0.977). Per person its DiD is not significantly correlated with the autocorrelation DiD in any cell (r = −0.420, −0.275, −0.428, −0.297; all p ≥ 0.127 at N = 14; the four share a sign, and "a null cannot be asserted from these values"), whereas the CCS xtx + yty DiD is (r = 0.949, 0.963, 0.917, 0.921). CCS-sts *rose* under DMT in every cell: at the primary cell +0.0044 [+0.0004, +0.0081], sign-flip p = 0.0559, phase p = 0.006, positive in 11 of 14, surviving motion control and both trend corrections; at the global fit on `ts_gsr` +0.0197, p = 0.0002, phase p = 0.001, positive in 13 of 14, the DMT run rising (+0.0122, p < 0.001) and the placebo run falling (−0.0075, p = 0.001); on `ts_demean` +0.0120 (p = 0.0040) at W = 60 and +0.0355 (p = 0.0001, 14 of 14) at the global fit. The two global-fit cells meet the paper's weighting rule and are, apart from the primary contrast, the only result that does. The paper still does not read them as a DMT finding, "so that the exclusion is seen to be by rule and not by evidence". The result is exploratory; its sign is the direction the study originally predicted for synergy. Two reasons and one rule: the global-fit cells, where the 13–14 of 14 consistency lives, are local values under one run-level fit and are exposed to the DMT run's variance change (window variance / run variance 1.28 before injection, 0.89 after), which moves every local mutual information; there is no null model or scope map for CCS-sts, whose value is −c averaged over the sign-disagreeing time points and has no established reading; and the record's closure entry forbids a DMT-specific claim from any specification chosen after the primary result. The CCS definition is *not* one of the reasons — the journal's SI Appendix retains it verbatim.

*ΦR.* The workspace quantity (a review computation) did not change at the primary cell (+0.0007 [−0.0078, +0.0100], p = 0.8971, phase p = 0.8372; every window set and trend correction null). No cell had a primary-set sign-flip p below 0.05, and the three cells with phase p below 0.05 disagree in sign across data versions.

**(b) Why it is there.** Results 3 carries the empirical weight: the refutation of the original hypothesis, the collinearity that turned the study into a methods paper, and the two quantities (CCS-sts, ΦR) whose behaviour under DMT the reader will most want to know. The long CCS paragraph exists because the paper is declining to report a result that meets its own rule, and it has to say exactly why.

**(c) What a sceptic asks.** *CCS-sts goes up in 13–14 of 14 people at p = 0.0002 — you were looking for synergy going up, and here it is. Why won't you say so?* Because of the two reasons and the rule above, and because it "arose after four specification changes" (Results 4); the paper's position is that a post-hoc positive result in the pre-specified direction is precisely the result a pre-registration exists to stop you claiming. The honest version of the answer is that the paper does not know what CCS-sts measures ("no established reading"). *You say 0.953 "leaves 9 % of the per-subject variance, which the diagnostic finds significant" — but the residual DiD is a group-level quantity, not that 9 %.* The revised sentence separates them: the 9 % is the per-subject variance of the sts DiD unshared with the autocorrelation DiD, and the residual DiD is a different, group-level remainder whose significance is not a test of that 9 % (Results 3). *If sts and r₁ are the same thing, why does the phase null treat them so differently (3.8 versus 1.8 SD)?* The paper says it cannot explain this and leaves it as one of the two facts separating the contrasts.

#### Table 2

**(a) What it says.** The primary step contrast for MMI-sts, W = 60, on both data versions. Row 1: pre-injection means, DMT and placebo (1.1554 / 1.1378 on `ts_gsr`; 1.1004 / 1.0819 on `ts_demean`). Row 2: DMT after minus before, −0.0485 [−0.0819, −0.0113], p = 0.0267 (`ts_demean` −0.0633, p = 0.0333). Row 3: placebo after minus before, +0.0324 [+0.0053, +0.0606], p = 0.0425 (+0.0398, p = 0.0306) — the placebo run *rises*. Row 4: the DiD, −0.0809, with its CI, sign-flip p, phase p and 13/14 (`ts_demean` −0.1031, 12/14). Row 5: the DiD of head motion itself, +0.0143, p = 0.2452 — motion did not change significantly. Row 6: the DiD after motion residualisation, −0.0649 [−0.0966, −0.0289], p = 0.0048, 13/14 (−0.0824, p = 0.0048).

**(b) Why it is there.** It shows the DiD's two halves separately, which the text needs for the "placebo run carries 0.40" statement (0.0324 of 0.0809, my division; the paper states 0.40), and the motion rows are the pre-specified motion rule made visible.

**(c) What a sceptic asks.** *The DMT within-run change is only p = 0.0267 and the placebo change p = 0.0425; the DiD gets its p = 0.0038 from the two moving in opposite directions. Is a rising placebo run a "control"?* The paper makes the same observation for the residual (Results 4: "the DiD's significance rests on the two runs moving in opposite directions") and treats the placebo rise as part of the phenomenon — r₁ drifts up across a session (Discussion, "A distinction for applicability"). *Motion residualisation shrinks the DiD from −0.0809 to −0.0649, about a fifth (my arithmetic); is a fifth of the effect motion?* The paper reports the survival by its pre-fixed definition (same sign, CI excluding zero) and does not interpret the shrinkage.

#### Table 3

**(a) What it says.** Four rows (`ts_gsr` W60, `ts_gsr` global, `ts_demean` W60, `ts_demean` global). For each: the CCS-sts DiD with CI, sign-flip p, phase p and the count of negative subjects (3, 1, 3, 0 of 14 — i.e. 11, 13, 11, 14 positive); the per-subject correlation of the CCS-sts DiD with the autocorrelation DiD (−0.420, −0.275, −0.428, −0.297); the same DiD under `phyid`'s mask (+0.0036, +0.0210, +0.0134, +0.0321); and the ΦR DiD (+0.0007, −0.0062, +0.0157, +0.0180) with its p-values (sign-flip 0.8971, 0.0953, 0.0853, 0.1177; phase 0.8372, 0.0230, 0.0380, 0.0190) and negative counts (8, 9, 4, 5).

**(b) Why it is there.** It is the evidence for three sentences: CCS-sts rises everywhere, its rise is not the autocorrelation rise (negative, non-significant correlations), and ΦR does nothing consistent.

**(c) What a sceptic asks.** *The CCS-sts/autocorrelation correlations are all negative and all around −0.3 to −0.4; with N = 14 that is not "no relation".* The paper says exactly this ("at this N a null cannot be asserted from these values, and the four share a sign"). *ΦR has phase p = 0.019–0.038 in three cells; why call it null?* Because the sign-flip p is never below 0.05 and the three phase-significant cells disagree in sign across data versions (Results 3, last paragraph).

---

### Results 4 — The residual diagnostic, its finite-sample null, and the shared variance with CCS-sts

**(a) What it says.** *The prediction works, almost.* Predicting each pair's sts from its measured (a_x, a_y, q) alone reproduces the observed level to within 4.3 % at W = 60 and 1.1 % at the run level, always over-predicting, with the residual's spread a fifth of the observed sts's across the 392 cells. A simpler variant with one autocorrelation for both regions (not in the plan) over-predicts by 16 %. The predicted DiD has the observed sign in every cell, overshoots it by 14–29 %, and tracks it per person at r = 0.98–0.99 (Table 4).

*The residual is not zero.* The residual DiD is positive in every cell, with a CI excluding zero and sign-flip p below 0.05 in all four windowed cells (+0.0115 [+0.0021, +0.0211], p = 0.042 at the primary cell; phase p also below 0.05 everywhere, with the Methods technicality). It survives motion control and is concentrated in the drug-present windows (early set +0.0179, p = 0.0012, positive in 12 of 14; late set +0.0064, p = 0.32). Within each run alone the change is not significant (DMT +0.0077, p = 0.080; placebo −0.0038, p = 0.19); the placebo run contributes 0.33 of the DiD, so the significance rests on the two runs moving oppositely. Neither pre-recorded outcome obtained: the residual DiD is not near zero, and it is not uncorrelated with r₁ — people whose r₁ fell more show the larger over-prediction (r = −0.780) — so the plan's signature of an autocorrelation-independent component is not met. The test stays what it was: pre-specified, with an outcome outside both branches. A post-hoc supplement traced the *level* residual to the diagnostic's one assumption, the cross-lag substitution: that step alone reproduces it (−0.0489 of −0.0489); the measured cross-lag correlations scatter around a_y q with no mean offset (+0.00014); and the residual is more negative where a and |q| are higher (R² = 0.74 on a, |q| and the scatter). Those facts cannot decide whether the *positive residual DiD* is that over-prediction shrinking as a and |q| fall under DMT, or a component that scales with the drug, because both predict them.

*The null can, partly.* With the data's own autocorrelation function, pair heterogeneity and the four cells' operating points, the finite-sample null gives a residual level of −0.035 (−3.0 %) against the observed −0.049 (−4.3 %) and a residual DiD of +0.0054 against the observed +0.0115, reproducing the DMT-run change (+0.0041 against +0.0077) but not the placebo-run change (−0.0013 against −0.0038). At W = 30, 60 and 840 it gives −8.5 %, −3.1 % and −0.34 % against the data's −9.7 %, −4.3 % and −1.1 %. Its value depends on free choices: per-pair filter heterogeneity of 0.25, 0.5 and 1.0 gives +0.0059, +0.0052 and +0.0077, and using the placebo autocorrelation shape everywhere gives +0.0037. So the null accounts for a third to two-thirds of the residual DiD, and the observed CI contains every one of those values. The direction of the residual DiD and a third to two-thirds of its size are what the cross-lag assumption produces with 20 samples. The rest — and on `ts_gsr` a run-level residual three times the null's (−1.1 % against −0.34 %; on `ts_demean` +0.1 %, i.e. absent) — is not accounted for. The null is stationary and the runs are not, by design (injection at TR 240; window variance / run variance 1.28 → 0.89 on DMT, 0.94 → 1.06 on placebo). Fitting one Gaussian to a run whose segments have different (a, q) makes the pooled cross-lag correlation differ from the product of pooled a and q by the covariance of a and |q| across segments, which is positive here because a and |q| fall together after injection. The third review named this pooling as a candidate mechanism for the run-level residual; the run-level cross-lag deviation, computed in the revision of 15 September 2026 (next unit), does not support it. On the coupled family, a zero-mean spread of pair-specific coupling makes the residual more negative (curvature +40 nats per unit c², i.e. +20σ_c²) and cannot produce the positive DiD; a positive mean coupling of about +0.006 could, but it would show as a mean cross-lag deviation of about +0.006, which the data do not have at W = 60. "The remainder is not located."

*The residual and CCS-sts are largely one quantity.* Across people the residual DiD and the CCS-sts DiD correlate at r = +0.799 (p = 0.001) on `ts_gsr` W = 60 and +0.875 on `ts_demean` (Figure 3b), and the relation survives partialling out the autocorrelation DiD (partial r = +0.83, +0.86). Both are computed from the same per-window matrices, so the shared variance may be common signal or common estimation noise. The split-half test (Table 5) was meant to separate them: on `ts_gsr` the within-half correlations are +0.847 and +0.783 (mean +0.815) and the cross-half +0.160 and +0.478 (mean +0.319, ratio 0.39); on `ts_demean` +0.881 within against +0.283 across (0.32). By the pre-fixed rule the cross-half mean (0.32) fell below half the within-half mean (0.41) — the "estimation noise" branch. But the rule cannot carry that label: the split-half reliabilities are low (residual DiD 0.49, CCS-sts DiD 0.30 on `ts_gsr`; 0.22 and 0.42 on `ts_demean`; for comparison the autocorrelation and MMI-sts DiDs are 0.71–0.74 and 0.69–0.72), so the largest cross-half correlation two perfectly correlated reliable components could show is √(0.494 × 0.302) = 0.39 (0.30 on `ts_demean`, against a threshold of 0.44). The pass threshold of 0.41 lay above that ceiling; the "not window noise" branch was unreachable. What the numbers say: the observed 0.32 sits at the ceiling and *disattenuates* (corrects for the unreliability) to 0.82, consistent with a shared reliable component, which the reliabilities cannot distinguish from a partial one or, at N = 14 (cross-half p = 0.59 and 0.08), from none. Verdict: undetermined. The test does establish that most of the within-half correlation (0.815 against a ceiling of 0.39) is estimation noise shared by the same windows, and that the reliable part of each quantity is small. Both group-mean DiDs are positive in both halves (residual +0.0067 / +0.0164; CCS-sts +0.0033 / +0.0054). No autocorrelation-independent component is reported; the residual and the CCS-sts change stay exploratory, having arisen after four specification changes (windowed sts → sixteen atoms → CCS → diagnostic residual), and an independent dataset with a pre-specified test is what would settle it. The run-level residual (−1.1 % against the null's −0.34 %) is the estimate least exposed to the windowed estimator's manufacture and the one most exposed to the runs' non-stationarity.

**(b) Why it is there.** This is the section that stops the paper from over-claiming in either direction. Without it the paper could say "sts change is autocorrelation change" (it cannot: the residual is significant) or that there is an autocorrelation-independent synergy increase (it cannot: the null accounts for up to two-thirds, and the split-half test is undetermined). It is also where the paper owns the flawed rule.

**(c) What a sceptic asks.** *Everything left over points in the direction of your original hypothesis: the residual DiD is positive, largest in the drug-present windows, and shares 80 % of its per-person variance with a CCS-sts increase. Aren't you burying a real DMT effect under "exploratory"?* The paper's answer is procedural and evidential: procedurally, the residual arose after four specification changes and the closure entry forbids a DMT-specific claim from any of them; evidentially, a stationary null with reasonable free choices produces a third to two-thirds of it, the run-level residual is absent on `ts_demean`, and the reliabilities (0.49, 0.30) are too low to say whether the shared component is signal. What it cannot say is that there is no effect — "the remainder is not located". *"A positive mean coupling of about +0.006 would" — would what?* Now named: the run-level residual, about −0.01 nats (−0.0137 on `ts_gsr`), with the sign logic stated — a positive coupling lowers sts, so +0.006 would produce a residual of that size but would show as a cross-lag deviation the data do not have at W = 60 (+0.00014) nor at the run level (+0.00009) (Results 4).

#### The run-level mean cross-lag deviation (added to Results 4 in the revision of 15 September 2026)

**(a) What it says.** Results 4 had one named candidate for the run-level residual (the −1.1 % on `ts_gsr`): *pooling* — fitting one Gaussian to a run whose segments have different (a, q), so that the run's cross-lag correlation need not equal the product of its a and q. The direct test is to measure, per person and run, the mean over the 6,555 pairs of the two measured cross-lag correlations minus what the AR(1) model predicts for them (a_y q and a_x q), from the same run-level matrices as the run-level rows of Table 4. The prediction written before the run, as commissioned: negative on `ts_gsr` and near zero on `ts_demean` if pooling explains the residual; near zero on both if it does not; "near zero" meaning a subject-bootstrap CI that includes zero. The record and the paper note that the commissioned sign is reversed relative to the coupled family's — on the family a *positive* deviation is what lowers sts below the prediction — and that a coupling account of the −0.01 residual requires about +0.006. The outcome fell outside both branches. On `ts_gsr` the deviation is +0.00009 [+0.00005, +0.00013] (sign-flip p = 0.0004, positive in 13 of 14): not zero by the CI, but tiny against the pair-level SD of 0.0390 and against the ≈ +0.006 the mechanism requires. On `ts_demean` it is −0.00738 [−0.00902, −0.00588] (p = 0.0001, negative in 14 of 14), on the variant whose run-level residual is +0.1 %. Across the 28 runs the deviation correlates with the run-level residual at −0.277 (`ts_gsr`) and −0.890 (`ts_demean`), the sign the family gives. The paper's conclusion: pooling, as named, does not account for the run-level residual on `ts_gsr`, which "remains unaccounted for by any mechanism named in this paper"; the `ts_demean` deviation is reported as a fact of the data without an interpretation.

**(b) Why it is there.** Without it the account of the run-level residual ended on a candidate mechanism that had not been tested, a loose end a reviewer would pull. With it, the candidate is closed and the paper says plainly that this part of the residual has no named explanation — which is more defensible than an untested explanation.

**(c) What a sceptic asks.** *The commissioned prediction had the wrong sign — doesn't that void the test?* The paper says the sign was reversed and reads the outcome under both signs: +0.00009 is far below the +0.006 the mechanism requires whichever way the sign is read, so the conclusion does not depend on it. *A deviation of −0.007 on `ts_demean`, in every subject, correlating at −0.89 with the residual across runs — that is not nothing.* The paper agrees it is a fact of the data and declines to interpret it; it is the second place where the two data versions part at the run level, the first being the residual itself (−1.1 % against +0.1 %).

#### Table 4

**(a) What it says.** One row per cell. For the four windowed cells: observed sts level (1.1377, 1.0082, 1.0802, 0.9636), predicted (1.1865, 1.1062, 1.1181, 1.0471), residual as a percentage (−4.3 %, −9.7 %, −3.5 %, −8.7 %), observed DiD (−0.0809, −0.0686, −0.1031, −0.0877), predicted DiD with CI and p (−0.0924, −0.0869, −0.1213, −0.1136; all p ≤ 0.0046), residual DiD with CI, sign-flip p, phase p and negative count (+0.0115, p = 0.0422, phase 0.0190, 4 negative; +0.0182, 0.0137, 0.0040, 2; +0.0182, 0.0040, 0.0180, 2; +0.0259, 0.0020, 0.0090, 3), the per-subject correlation of predicted with observed DiD (+0.989, +0.987, +0.990, +0.981) and of residual DiD with autocorrelation DiD (−0.780, −0.825, −0.597, −0.604). Two run-level rows: `ts_gsr` observed 1.2883, predicted 1.3021, residual −1.1 %; `ts_demean` 1.2205 against 1.2197, +0.1 %; in both, the prediction is constant within a run, so the residual DiD equals the observed DiD by construction. A last row for the null: level −0.035 (−3.0 %; homogeneous filter −3.1 %; −8.5 % at W = 30, −0.34 % at 840), DiD +0.0054 (DMT +0.0041, placebo −0.0013), range +0.0037 to +0.0077.

**(b) Why it is there.** It holds the numbers behind "14–29 %", "0.98–0.99", "positive in every cell", and the null comparison; and it shows that the W = 30 residual is about twice the W = 60 one (−9.7 % against −4.3 %), which is what finite-sample error should do.

**(c) What a sceptic asks.** *Your "observed level" here is 1.1377 but Table 2 says the DMT pre-injection mean is 1.1554; which sts level does the 4.3 % refer to?* The revised Table 4 caption says: the level columns are means over all subjects, both runs and all windows (the 392 subject × run × window cells at W = 60), and in the run-level rows the whole-run plug-in sts averaged over subjects and runs — not the pre-injection means of Tables 1 and 2. *The residual DiD's CIs exclude zero in every cell but the sign-flip p is only 0.042 at the primary cell — which do you trust?* The paper's weighting rule settles it: p between 0.01 and 0.06 is "reported as such and is not treated as an established effect".

#### Table 5

**(a) What it says.** Two rows, `ts_gsr` (decides) and `ts_demean` (sensitivity). For each: the two within-half correlations (odd–odd, even–even: +0.847, +0.783; +0.884, +0.878), the two cross-half correlations (+0.160, +0.478; +0.274, +0.292), their ratio (0.39, 0.32), the same after partialling out the autocorrelation DiD (within +0.815 / cross +0.154; +0.849 / +0.287), the split-half reliabilities of the residual DiD and the CCS-sts DiD (0.49, 0.30; 0.22, 0.42), the ceiling against the threshold (0.39 / 0.41; 0.30 / 0.44), and the verdict: noise branch, undetermined.

**(b) Why it is there.** It shows in one line why the test failed: in both rows the ceiling is below the threshold.

**(c) What a sceptic asks.** *The two cross-half correlations on `ts_gsr` are +0.160 and +0.478 — why so different?* The paper does not comment; with N = 14 and reliabilities of 0.3–0.5 the sampling error of a correlation is large, which is the point the ceiling makes. *Why is `ts_gsr` the row that "decides"?* Because the rule was "fixed in advance on `ts_gsr`" (Methods, "The residual diagnostic").

---

### Results 5 — Lag dependence

**(a) What it says.** Repeat everything with the "future" τ = 2, 3 or 5 volumes ahead instead of 1 (Table 6, Figure 5). As the plan predicted, r_τ falls with τ (0.848, 0.513, 0.139, −0.202) and the artefact weakens: the sts contrast is significant on both nulls at both estimators wherever the lag-τ autocorrelation contrast is (τ = 1, 2, 3) and null where it is not (τ = 5). Per person it tracks the lag-τ autocorrelation contrast (+0.953, +0.970, +0.626, −0.832), the sign reversing at τ = 5 because r₅ is negative and every AR(1) atom depends on the autocorrelation only through its square. At τ = 3 the tracking is only partial (0.626 at W = 60, 0.885 at the global fit) while the sts contrast is still significant on both nulls and survives motion control; so at τ = 3 the sts contrast is only partly the r₃ contrast, which is either a limit of the map at low r_τ (r₃ = 0.14, where the slope is small and the estimator's scatter is a larger share of the atom) or a second remainder — the data do not say which. The autocorrelation contrast itself *grows* with τ (−0.0146, −0.0468, −0.0681 at τ = 1, 2, 3): DMT changes the whole shape of the autocorrelation function toward faster decay, of which the r₁ change is only the lag-1 summary, and the in-band *spectral centroid* (the centre of mass of the signal's frequency content) rises accordingly (+0.0023 Hz, p = 0.022, 12 of 14). The paper does not interpret the shape change beyond this. No lag moves the pairs to a point where q contributes comparably, because no such point exists on the family at BOLD correlations.

**(b) Why it is there.** It is the one prediction of the reframed account that was recorded before the computation ("r_τ falls with τ and the artefact weakens"), and it closes off "just use a longer lag" as a fix: the artefact shrinks, but so does everything else.

**(c) What a sceptic asks.** *"Significant on both nulls at both estimators" — Table 6 only has sign-flip p at W = 60.* Table 6 now carries the phase-randomised p at W = 60 and the global-fit sts DiD with its p-values for every τ. *If the autocorrelation change is largest at τ = 3, why is the sts change smallest there?* Because sts at τ = 3 is only 0.026 nats to begin with (Table 6) — the atom itself has almost vanished, so its change is small even when the underlying autocorrelation change is large; Figure 5 shows the two panels moving oppositely.

#### Table 6

**(a) What it says.** Four rows, τ = 1, 2, 3, 5, on `ts_gsr` at W = 60: the DMT pre-injection mean r_τ (0.848, 0.513, 0.139, −0.202), the sts level (1.1554, 0.1797, 0.0262, 0.0415), the sts DiD with CI and p (−0.0809, p = 0.0038; −0.0429, p = 0.0037; −0.0043, p = 0.0018; −0.0024, p = 0.3688), the lag-τ autocorrelation DiD with p (−0.0146, 0.0106; −0.0468, 0.0090; −0.0681, 0.0132; −0.0108, 0.5670), and the per-subject correlation between the two DiDs (+0.953, +0.970, +0.626, −0.832).

**(b) Why it is there.** It shows the atom collapsing with lag (1.1554 → 0.1797 → 0.0262 nats) alongside the autocorrelation change growing (−0.015 → −0.047 → −0.068), which is the whole content of "a longer lag reduces the artefact by reducing everything".

**(c) What a sceptic asks.** *sts at τ = 5 (0.0415) is larger than at τ = 3 (0.0262) — why?* Because r₅ = −0.202 is larger in size than r₃ = 0.139, and sts depends on the square (the paper: "every AR(1) atom is even in the autocorrelation"). *A p of 0.0018 for a DiD of −0.0043 nats — is that meaningful?* It is a tiny effect measured precisely; the paper reads it only as tracking the r₃ change, partly.

---

### Results 6 — Estimator manufacture, and the global fit for between-state contrasts

**(a) What it says.** Where two simulated conditions can be built with *equal* true sts but different covariance, the windowed estimator at W = 60 reports a difference anyway: −9 %, +16 %, +7 % ± 8 % and −8 % ± 6 % of the real DiD in the four matched pairs, of either sign; at W = 30 up to +33 %; at the full run length ≤ 2 % except in one family (+29 %). A matched pair in which r₁ falls by the observed amount could not be built at data-like autocorrelation, because true sts is steep in r₁ (about +0.07 nats per +0.01 near 0.87) and flat in q. The observed change in the autocorrelation function alone, at fixed q, changes the *true* sts by −0.069 against the observed DiD of −0.081, and the W = 60 estimator returns −0.056 of it. The windowed whole-brain sts sits 0.1531 nats below the global fit before injection (1.1554 against 1.3085); the diagnostic decomposes that gap into lower within-window parameters (captured by the prediction from the window's own (a_x, a_y, q)) and a residual of −0.0489, against −0.0137 at the run level. On manufacture grounds the global fit is the better estimator for a contrast between *separately fitted* runs or groups: ≤ 2 % manufacture in three of four families at 840 samples (+29 % in the fourth) and a run-level residual of 1.1 % (`ts_gsr`) or 0.1 % (`ts_demean`). Two qualifications, and the recommendation rests on the manufacture figures alone. First, the global fit's per-bin values are local atoms under a single run-level covariance, not per-bin decompositions, so a pre/post contrast *within* a run — which is what this paper runs — is exposed to the within-run variance change (1.28 → 0.89 on DMT; the global-fit sts bins correlate with that ratio at +0.37 per run); the global-fit MMI-sts contrast (−0.0801 against −0.0809) is therefore agreement between estimators, not confirmation. Second, the global fit on `ts_gsr` is the one cell where sts fell less than proportionally to TDMI, so the estimator recommended here is the one at which the map's proportionality prediction fails; the recommendation is not made on that ground. W = 60 stays primary because it was pre-specified and the two agree.

**(b) Why it is there.** It bounds how much of the observed −0.0809 could be estimator artefact rather than r₁ change (up to about 16 % at W = 60 in the matched families), gives the paper's one practical recommendation about estimators, and immediately qualifies it so that the recommendation cannot be read as an endorsement of the global fit for the contrast this paper itself ran.

**(c) What a sceptic asks.** *Three predictions of the sts change from autocorrelation now exist — −0.087 from the map (Results 2), −0.0924 from the per-pair diagnostic (Results 4), −0.069 from the true-sts change in the matched family here — and they are never reconciled.* Results 6 now reconciles them — three questions, one sign, the differences being the residual and the manufacture figures seen from different sides — and the Abstract says the 114 % is the diagnostic's. *"Of the real DiD" — the real DiD of what?* Now stated: the real primary DiD, −0.0809, with the ± figures identified as standard errors over the 4,000 windows. *Why recommend the estimator on which your own proportionality prediction fails?* The paper says the recommendation "rests on the manufacture figures alone" and names the failure itself.

---
### Discussion — What the finding is and is not

**(a) What it says.** The paper says nothing about whether the brain has synergy in the intended sense; it says what the estimator responds to. On the AR(1) family the Gaussian-MMI synergy atom is self-prediction plus rtr, balanced by four negative atoms that CCS does not have, and its dependence on r₁ dominates its dependence on q everywhere BOLD pairs sit. That is a property of the estimator on a family without lagged interaction; with interaction, sts also moves at fixed (r₁, q). The consequence is narrow: when two states differ in r₁, the MMI-sts contrast between them is dominated by that difference, scaled by ∂sts/∂r₁, whether or not anything "synergy" is meant to capture has changed. On this dataset the r₁ change predicts the sign and 114 % of the size of the sts change, and the per-person collinearity is 0.95 — and that is what the dataset shows, not "sts change is autocorrelation change": the pre-specified criterion under which it would have shown more (a residual DiD near zero) was not met. Three things the data add are stated as they are: the excess has the wrong sign (sts 0.084 below xtx + yty where the family puts it above by rtr), so the closed form is a structural account, not an exact model; the residual is positive in every cell (p = 0.042, not "established" under the weighting rule), larger in the early windows, in the direction of the original hypothesis, a third to two-thirds of it reproduced by a stationary null that does not match non-stationary runs, the rest not accounted for, with the one named candidate mechanism, pooling, tested in the revision by the run-level cross-lag deviation and not supported (+0.00009 on `ts_gsr` against the ≈ +0.006 required); and the residual's per-person variance is largely shared with CCS-sts, which the flawed split-half rule could not classify (cross-half at the ceiling, disattenuating to 0.82; reliabilities 0.49, 0.30). No autocorrelation-independent synergy change is reported; the residual and CCS-sts stay exploratory; an independent dataset with a pre-specified test would settle it.

**(b) Why it is there.** It draws the boundary of the claim in both directions and puts the three uncomfortable facts (wrong-signed excess, unexplained residual, CCS-sts co-movement) in the first Discussion paragraph rather than the last.

**(c) What a sceptic asks.** *You say "dominated" and "114 %" but also that the criterion for "accounted for" was not met. Which sentence goes in my citation?* The paper's own: the contrast "is dominated by that difference ... whether or not anything the word 'synergy' is meant to capture has changed", with "what the dataset shows is that, not 'sts change is autocorrelation change'". *What would falsify the account on this dataset?* A residual DiD near zero would have confirmed it fully; a residual significant and uncorrelated with r₁ would have shown an independent component. The data gave neither, and the paper says so (Results 4).

---

### Discussion — Redundancy functions, null models, and what CCS costs

**(a) What it says.** The property was examined under two redundancy definitions and is not found in CCS-sts to the degree MMI-sts shows it. Other redundancy definitions (I_min, I_BROJA, dependency-based, information-geometric Gaussian decompositions) were not examined, so "MMI-specific" is not a licensed phrase. What CCS costs: its double redundancy is a masked double co-information, so CCS-sts is −c averaged over the time points where the five local signs disagree; it takes negative values; and its whole-brain value depends on which fifth sign the mask uses (−0.048 published against −0.039 `phyid`, qualitative statements unchanged). Its DMT increase is consistent across people at the global fit and survives motion and trend controls there and at the primary cell, and it is not read, for the reasons in Results 3. The ΦID authors' remedy — null-model normalisation of atoms (Liardi et al., 2025; a null preserving total mutual information, developed for PID on MEG, not yet reported for ΦID on BOLD) — is different in kind from the diagnostic here, which is per pair, analytic and specific to lag-1 autocorrelation; the two are complementary: a null preserving total mutual information does not preserve autocorrelation, and the diagnostic does not address the lattice's negativity. CCS is not offered as the corrected estimator, only as the one whose sts does not carry the autocorrelation contrast.

**(b) Why it is there.** It forecloses the two easy readings: "so switch to CCS" (CCS has its own costs and no established reading) and "Liardi already fixed this" (different problem).

**(c) What a sceptic asks.** *If "MMI-specific" is not licensed, what is the title's "Gaussian-MMI" claim?* A claim about MMI, not a claim that only MMI has the property; the paper limits itself to the two functions it examined. *"−c averaged over the samples where the five local signs disagree" — averaged over those samples, or over all samples with zeros at the others?* Methods says CCS-sts is "0 at the selected samples and −c elsewhere", which implies an average over all samples; the revision makes Methods, Results 3 and the Discussion agree: the average over all samples of a quantity that is zero at the mask-selected samples and −c elsewhere.

---

### Discussion — A distinction for applicability

**(a) What it says.** Two uses of MMI-sts must be distinguished. (1) A *contrast* — between states, between groups, or across a session — is exposed wherever the compared conditions differ in r₁: BOLD autocorrelation changes with anaesthetic depth and in disorders of consciousness (Huang et al., 2018), under DMT (this dataset), and within a placebo run with time (the placebo run's r₁ drift carries 0.34 of the DiD here); between-group designs are exposed to any group difference in r₁ from physiology, motion, age or scanner. (2) A *spatial map* of synergy across regions is exposed through regional differences in r₁: higher r₁ gives higher sts with rtr almost unmoved, so a regional autocorrelation gradient would produce a synergy-minus-redundancy gradient of the same spatial form, and within a single window half the between-pair variance of sts here is pair r₁. The applicability table (Supplement S3) gives every readable study the same conditional sentence; it is what the map predicts, not evidence about any study, since none reports regional r₁; every study gets the sentence and none is singled out. Luppi et al. (2022) falls outside the table's TR range (a scoping rule). By the map it would be the most exposed dataset, *under an assumption the text read does not settle*: its band-pass and TR are not stated there; the implied r₁ ≈ 0.97 — where ∂sts/∂r₁ = 32.8 against ∂rtr/∂r₁ = 0.06 — takes the HCP TR of 0.72 s and the 0.008–0.09 Hz band of two related papers. Its primary analysis is HRF-deconvolved; its gradient's replication without deconvolution is a supplementary figure of that paper; and this paper's own evidence that deconvolution leaves the mechanism in place comes from TR 2 s data (where deconvolution takes r₁ from 0.87 to 0.79) and does not transfer to TR 0.72 s. Its synergy-minus-redundancy gradient is the spatial-map case exactly, so the conditional statement applies, on those assumptions. Two limits on reach: because rtr + sts = TDMI (so ∂rtr/∂q = −∂sts/∂q) and ∂rtr/∂r₁ ≈ 0, a change in q moves synergy and redundancy oppositely by equal amounts while a change in r₁ leaves rtr almost untouched — so a pattern of synergy and redundancy moving in opposite directions (Down et al., 2026) is the q signature or a mixture, not the r₁ signature (a family statement the data follow only loosely: MMI rtr fell by a tenth of the sts fall, −0.0078 against −0.0809, where the family gives a hundredth), and this is "the one place the table argues against the mechanism"; and ΦR = rtr = −½ ln(1 − r₁²q²) on the family falls with a fall in *either* factor, so the r₁-dominance result does not carry over to ΦR (Luppi et al., 2024, 2026). Among the readable synergy-on-BOLD studies, none addressed autocorrelation; Varley (2024) is the study whose subject it is.

**(b) Why it is there.** This is the paragraph that determines whether the paper is read as an attack on Luppi et al. (2022) — the Cambridge group's flagship result — or as a diagnostic offered to everyone. The paper's strategy is to apply one identical conditional sentence to every study, to place Luppi 2022 outside the pre-fixed scope, and then to say, with every assumption named, that by the map it would be the most exposed.

**(c) What a sceptic asks.** *Are you saying the synergistic core of Luppi et al. (2022) is an autocorrelation artefact?* No, and the paper's exact words matter: it is "the spatial-map case exactly, so the same conditional statement applies to it, on those assumptions"; the assumptions (TR, band, r₁ ≈ 0.97) are not settled by the text read, none of the studies reports regional r₁, and the deconvolution evidence does not transfer. What the paper does say is that a regional r₁ gradient *would* produce such a map, and, since the revision of 15 September 2026, that on this dataset it does: regional sts follows regional r₁ at +0.863 and the synergy-minus-redundancy map at +0.792 (Results 2), which the applicability paragraph reads as showing the exposure is real here and nothing about that study. *If synergy and redundancy move oppositely in Down et al., doesn't that refute your mechanism?* The paper says it is the one place the table argues against the mechanism, and that the pattern is the q signature on the family.

---

### Discussion — Recommendations

**(a) What it says.** Report mean r₁ beside sts, per condition and person, and its contrast beside the sts contrast; if the two are collinear across people, test the remainder with the diagnostic rather than discarding it, "since here a 0.95 collinearity left a remainder with a sign-flip p of 0.042, reported and not treated as established". Run the residual diagnostic: predict each pair's sts from its measured (a_x, a_y, q), test the residual with the same inference as the observed contrast, compare it with a finite-sample null whose free choices are varied and reported, and state the cross-lag assumption. For a contrast between separately fitted runs or groups, prefer the global fit on manufacture grounds (≤ 2 % in three of four families at 840 samples; run-level residual 1 % on `ts_gsr`, 0.1 % on `ts_demean`); a pre/post contrast within one run under a single fit is exposed to within-run variance change and is not what the global fit is recommended for. Consider CCS under the published definition, with its costs. Consider τ > 1, with its signal cost: a longer lag reduces the artefact by reducing everything, and at no lag do pairs reach a point where q contributes comparably. HRF deconvolution, tried post hoc, left the sts contrast and its collinearity in place and changed ΦR's baseline and drift in ways the raw series only partly share; it is not a remedy on these data.

**(b) Why it is there.** A methods paper is judged by whether anyone can act on it; these are the actions.

**(c) What a sceptic asks.** *You call the remainder "significant" here and "not established" in the previous section — which?* The revised Recommendations say "a remainder with a sign-flip p of 0.042, reported and not treated as established (Methods, Multiplicity)", so the two sections agree. *Why recommend the global fit for between-group contrasts when your own between-run contrast is within-session?* The paper separates the two cases explicitly in this paragraph and in Results 6.

---

### Discussion — Limitations

**(a) What it says.** One dataset, one drug, one parcellation, N = 14; effect sizes with CIs; the DMT contrast is a proof of concept. The AR(1) family does not fit the data beyond lag 1 and its excess identity has the wrong sign on them; the map's q-axis and the diagnostic's substitution are AR(1) statements; the coupled family is symmetric; of the residual, a third to two-thirds is finite-sample under one stationary null and the rest is not accounted for. There is no ground truth for synergy in these data. Two redundancy functions, both Gaussian and continuous; the discrete CCS on binarised data used elsewhere was not examined; the CCS definition used is the published one. The windowed estimator's manufacture is not removed by the diagnostic, and the split-half rule was set without reference to the reliability ceiling, so that test decided nothing. An odd/even-*TR* split within windows was not used because adjacent TRs share most of their variance at r₁ ≈ 0.86; odd/even *windows* is the right design and is underpowered here (about 20 effective samples per window, N = 14). Two computations listed as not run in the previous revision were run in this one with their predictions recorded first: the regional test of the spatial-map claim (predicted branch obtained) and the run-level mean cross-lag deviation (outside both recorded branches; does not account for the run-level residual; the commissioned prediction's sign was reversed relative to the coupled family's, as the record states). Many statistics are reported without correction. The pre-specification history is as stated: the confirmatory test was of a different hypothesis, its directional-failure rule was written after the 115-region decrease was known, the Part B plans were written after the review computations; of this revision's additions, two had rules recorded on the day they were run, the coupled family was entered with no prediction, and the finite-sample null is a review computation with no rule. The git record establishes ordering, not blindness.

**(b) Why it is there.** It is the list a hostile reviewer would write, written first by the authors.

**(c) What a sceptic asks.** *You ran the two computations you had listed as not run — did they change anything?* Yes, both ways: the regional test made the spatial-map exposure a demonstrated fact on this dataset (Results 2), and the cross-lag deviation removed the only named explanation of the run-level residual, which the paper now calls unaccounted for (Results 4). *"There is no ground truth for synergy in these data" — then what would count as evidence that any of this matters for the brain?* The paper's answer is that it is not trying to: "the analysis establishes what the estimator responds to, not what the brain does".

---

### Figures

#### Figure 1 — The sixteen atoms under MMI and CCS, levels and DiDs

**What each panel shows.** Panel (a): sixteen pairs of bars, blue for MMI and orange for CCS (published definition), giving each atom's whole-brain mean in the DMT run's pre-injection windows 1–4; the atoms are grouped along the x-axis as double redundancy (rtr), cross-prediction (rtx, rty, xtr, ytr, xty, ytx), self-prediction (xtx, yty), redundancy↔synergy (rts, str), mirror atoms (xts, yts, stx, sty) and synergy (sts). No error bars, on purpose: the caption says the between-subject spread of a level is not the uncertainty of any contrast the paper tests. An annotation states that sts − (xtx + yty) = −0.084 under MMI where the AR(1) family gives +rtr = +0.039. Panel (b): the same sixteen atoms' primary DiDs (DMT minus placebo, windows 6–14 minus 1–4) with bootstrap 95 % CI whiskers.

**What to look at first.** In (a), the four tall blue bars pointing *down* (the mirror atoms, about −0.54 each) next to the three tall blue bars pointing up (rts, str at about 0.57, sts at 1.16), and the orange bars at those same positions sitting near zero. Then, in (b), the same four positions: the blue mirrors go up by about +0.04 with CIs excluding zero while sts, rts, str go down. Then the xtx and yty positions, where blue and orange are the same height in both panels.

**What it proves that the text alone does not.** The text says the CCS decomposition "has no counterpart" to the negative atoms; the figure shows the whole shape at once — MMI's synergy block and its negative mirror image, and CCS's flat profile with the self-prediction atoms identical under both. It also makes visible that the large DiDs — sts, xtx, yty, rts, str and the four mirrors, the block and its mirror image — have whiskers well clear of zero while the cross-prediction atoms barely move, so the DMT change under MMI has the same block-versus-mirrors structure as the level.

#### Figure 2 — The scope map

**What each panel shows.** Panel (a): sts as a colour map over q (horizontal, −0.6 to 0.6) and r₁ (vertical, 0 to 0.95), with contour lines at 0.25, 0.5, 1, 1.5, 2. Panel (b): the excess sts − (xtx + yty), equal on the family to rtr, which is zero along q = 0 and grows toward the top corners (the colour bar runs to about 0.175 nats). Panel (c): the derivative ratio |∂sts/∂r₁| / |∂sts/∂q| on the wider grid |q| ≤ 0.95, log colour scale, contours at 10, 30 and 100, with 1,500 of subject 1's 6,555 pairs (DMT run, window 6; median r₁ 0.840, median |q| 0.225) as orange points and the operating point (0.85, 0.25) as a cross, where the ratio is 32. The caption states that the ratio = 1 boundary does not exist on the grid (minimum 1.9 at (0.77, ±0.95); 6.55 on |q| ≤ 0.6).

**What to look at first.** In (a), that the contour lines are almost horizontal: moving left or right (changing q) barely changes sts, moving up (raising r₁) changes it a lot. In (c), the bright vertical band at q = 0 (where the q-slope vanishes and the ratio blows up), and the orange cloud sitting at r₁ ≈ 0.8–0.9 across a range of q, well inside the ratio ≥ 10 region.

**What it proves that the text alone does not.** The text gives the ratio at two points; the figure shows there is no place on the plane where the two inputs are comparable, and shows where real pairs sit relative to that. Panel (b) shows something the text states only as an identity: the excess is a q-effect, zero at q = 0, so the data's negative excess (Results 1) cannot be a point on this surface at all.

#### Figure 3 — Per-subject DiDs

**What each panel shows.** Panel (a): fourteen dots, labelled by subject index, with the lag-1 autocorrelation DiD on the horizontal axis (about −0.065 to +0.025) and the MMI-sts DiD on the vertical (about −0.28 to +0.10), a least-squares line, and the annotations r = +0.953 (p = 1.44 × 10⁻⁷), ρ = +0.90, N = 14, and "leave-two-out (91 refits): r = +0.846 to +0.973". Panel (b): the residual DiD of the diagnostic (horizontal, about −0.02 to +0.05) against the CCS-sts DiD (vertical, about −0.0125 to +0.02), r = +0.799 (p = 0.000602), ρ = +0.74.

**What to look at first.** In (a), the two extreme dots: subject 8 at the bottom left (the largest fall in both quantities) and subject 14 at the top right (the only rise in both) — these anchor the line, which is why the leave-two-out was run; then the twelve in between, which also lie on the line. In (b), the looser cloud: subjects 1 and 8 at the top right, subject 10 at the bottom left, subject 14 at the far left.

**What it proves that the text alone does not.** A correlation of 0.95 from 14 points can be two outliers and a blob; the figure lets the reader see that the middle twelve are ordered along the same line, and that the leave-two-out minimum (0.846, without 8 and 14) is not a collapse. Panel (b) shows that the residual–CCS relation, though r = 0.80, is carried by a spread that a few subjects dominate — which is what the low split-half reliabilities in Table 5 predict.

#### Figure 4 — The diagnostic by window

**What each panel shows.** Panel (a): whole-brain sts over the 28 minutes of the run (x-axis in minutes), DMT in red and placebo in blue, observed as solid lines and the AR(1) prediction from each pair's (a_x, a_y, q) as dashed lines; shading is ±1 within-subject SEM (Cousineau–Morey); a grey band marks the pre-injection windows 1–4, a hatched band window 5 (excluded from the primary post set), and a dashed vertical line the injection at 8 min; y-range 1.00–1.30 nats. Panel (b): the residual (observed minus predicted) per run, drawn with the same nats-per-unit-height as (a) so the two panels can be compared by eye (0.20 nats on a panel 67 % the height of (a)'s 0.30 nats).

**What to look at first.** In (a), that each dashed line runs about 0.05 nats *above* its solid line and follows every bend of it — the dip in both runs at window 5, the DMT run's fall after injection to about 1.05 and slow recovery, the placebo run's steady rise. Then in (b), how flat both residuals are (both near −0.05) and the one feature: the red residual rising to about −0.035 in the windows just after injection and returning.

**What it proves that the text alone does not.** The text reports the prediction as a level (4.3 %) and a DiD (114 %); the figure shows that the prediction reproduces the *whole time course*, including the placebo drift and the injection dip that appears in both runs, not just two summary numbers. It also shows the size of the residual's modulation against the size of the contrast, which no table does: the residual's bump is small next to the DMT run's fall. And it shows something the text mentions only in passing — that both runs, placebo included, dip at window 5, the injection response that led to excluding it.

#### Figure 5 — Lag dependence

**What each panel shows.** Panel (a): the whole-brain MMI-sts DiD at τ = 1, 2, 3, 5 (−0.0809, −0.0429, −0.0043, −0.0024) with bootstrap CIs, and the per-subject correlation with the lag-τ autocorrelation DiD printed (+0.95, +0.97, +0.63, −0.83). Panel (b): the mean lag-τ autocorrelation DiD at the same lags (−0.0146, −0.0468, −0.0681, −0.0108) with CIs; the x-axis labels give the pre-injection r_τ (+0.85, +0.51, +0.14, −0.20).

**What to look at first.** The two panels move in opposite directions from τ = 1 to τ = 3: the sts DiD shrinks toward zero while the autocorrelation DiD grows; at τ = 5 both CIs cross zero.

**What it proves that the text alone does not.** That the shrinking sts contrast is not the autocorrelation change disappearing — the autocorrelation change is *larger* at τ = 2 and 3 — but the atom itself vanishing (Table 6: 1.1554 → 0.1797 → 0.0262 nats). A reader of the text alone might take "the artefact weakens" to mean the lag fixes the problem; the figure shows it fixes it by removing the signal.

---

### Supplement (pointer)

**(a) What it says.** S1: the original pre-specified analysis and its results — the up-regulation hypothesis, the directional-failure rule, the windowed test, the intensity-tracking criterion with its controls and the void verdict, the redundancy prediction, the exploratory regional analysis, the EEG Lempel-Ziv check, robustness across estimators, and the commit-by-commit audit trail; in `draft.md` (kept as a record), `supplementary.md` (Tables S1–S8) and `prespecification_summary.md`. S2: the ΦR exploration (every result post-hoc) and why it was closed: ΦR with full inference on the raw series; HRF deconvolution and its effect on every quantity; the deconvolved whole-brain ΦR increase and a regional test against a prediction recorded before it was run; and the reasons the increase supports no claim — a pre-injection baseline gap in the direction that creates it (deconvolved −0.0124, p = 0.014; raw −0.0042, p = 0.28), a placebo-run decline across the 14 windows (deconvolved slope −0.00115 per window, p = 0.025; raw −0.00036, p = 0.43), estimator disagreement, and a 56–64 % placebo share; the within-pre-injection placebo decline is present on the raw series (−0.0084, p = 0.039) as well as after deconvolution (−0.0120, p = 0.067). S3: the full applicability table with its search record and blocked sources, the scope-map tables, the CCS definition check, the split-half tables, the leave-two-out table, the coupled-family tables, the lag tables, the diagnostic tables, the matched-null tables, and the cross-lag deviation and regional sts–r₁ tables of the revision. S4: the COBIDAS reporting checklist, each item marked reported (with location), not applicable (with reason) or not reported (with what is missing).

**(b) Why it is there.** The original study has to exist somewhere a reader can inspect it — otherwise "the study began as a pre-specified test" is unverifiable — and the ΦR exploration has to be shown closed rather than quietly dropped, since a positive ΦR result after deconvolution is exactly the kind of thing a sceptic would suspect had been hidden.

**(c) What a sceptic asks.** *A whole-brain ΦR increase after deconvolution, in the direction of the workspace account — and you closed it. Why?* The S2 pointer lists the four reasons with numbers: the baseline gap, the placebo decline, estimator disagreement, and a 56–64 % placebo share; the raw series shows no increase (Results 3: +0.0007, p = 0.90). *"The redundancy prediction" — what was it?* The revised S1 pointer says: under a redundancy-dominance reading of an sts decrease, rtr should have risen with a mirrored time course; it did not — on `ts_gsr` rtr fell with sts, positive in 4 of 14 subjects — and the reading is unsupported on either variant.

---

### Ethics statement

**(a) What it says.** The original study was approved by a named UK research ethics committee and the Health Research Authority, conducted under the Declaration of Helsinki, ICH Good Clinical Practice and the NHS Research Governance Framework, sponsored by Imperial College London under a Home Office licence for Schedule 1 drugs, with written informed consent; this wording follows Timmermann et al. (2023), which gives no reference number (a [TK] to obtain from C.T.). The present work is a secondary analysis of anonymised, parcellated time series and motion values released by the data authors; no new data, no participant contacted, no one identifiable.

**(b) Why it is there.** Journals require it, and a secondary analysis has to say whose approval it rides on and why no new approval is needed.

**(c) What a sceptic asks.** *Reusing data released without a licence file — is that ethical?* Methods, Dataset: use confirmed by email by both the data collector and the derivative author, with attribution, correspondence held by the corresponding author. *Where is the REC number?* Not yet held ([TK]).

---

### Data and code availability

**(a) What it says.** The time series, ratings, motion and EEG regressor are from the data authors' GitHub/Zenodo release (upstream commit 77af7aa), cloned locally and not redistributed. Everything else — analysis code, the pinned environment, every results table with the git SHA that produced it, the pre-specification record, the three adversarial reviews and Part B notes with result files, and the closed-form implementation — is at the paper's GitHub repository. `run_all.sh` regenerates the original analysis (sections 0–5) and, in a section added on 15 September, the review and Part B computations and the five figures. Each script was run individually as recorded; the section has not yet been executed end-to-end as one run (a [TK] to do before submission). The deconvolution items need a separate sandbox and are skipped without it. Seed 20261120 throughout.

**(b) Why it is there.** The paper's credibility rests on the record being inspectable; this section says where and how.

**(c) What a sceptic asks.** *You claim full reproducibility but have never run the pipeline end to end.* The paper says so and marks it [TK]; each script's output header carries the git SHA it ran at (repository layout), so the individual runs are traceable. *The repository history contains participant codes that were removed from tracked files — has the history been rewritten?* The paper does not mention this; the repository's orientation file says it has to be done before the repository is made public (not a claim of the paper; noted here because a reviewer with repository access will ask).

---

### Author contributions (CRediT)

**(a) What it says.** V.S.: conceptualisation, methodology, software, formal analysis, investigation, data curation (secondary), writing (original draft; review and editing), visualisation, project administration. C.T.: resources (data acquisition), writing (review and editing) [TK]. S.P.S.: data curation (the released derivatives), resources (data release), validation (the mean-filled parcel), writing (review and editing) [TK]. Further contributors to be nominated by C.T.

**(b) Why it is there.** It is what makes the AI-use statement's "under the direction of V.S." concrete: every intellectual role is assigned to V.S., and the data authors' roles are the data.

**(c) What a sceptic asks.** *Is the software really V.S.'s if an AI system wrote it?* The AI-use statement answers: produced with the assistance of an AI system under V.S.'s direction, every number checked against its source before commit, responsibility taken by V.S.

---

### Conflicts of interest

**(a) What it says.** V.S. is preparing an application for a PhD position in the Cambridge group whose members authored Luppi et al. (2022, 2024) — the studies whose estimator this paper analyses — and this work was produced in part as evidence of competence for that application, as the repository's public record states. C.T. co-authored the source data paper and the derivatives paper; S.P.S. is first author of the derivatives paper. No other conflicts.

**(b) Why it is there.** Because the obvious question — why is an outsider who wants to join this group publishing a critique of its estimator? — is better answered by the paper than by a reviewer.

**(c) What a sceptic asks.** *Isn't this either an audition or an attack?* The paper's position is that it is a declared interest and a public record: the study started as a test inside the workspace framework, the data turned it into a methods account, every study in the applicability table gets the same sentence, and Luppi 2022 is discussed under named assumptions (Discussion, "A distinction for applicability").

---

### AI-use statement

**(a) What it says.** The analysis code, verification scripts, the three adversarial reviews and the verification of the correction note, the Part B computations and the manuscript drafts were produced with the assistance of an AI system (Claude, Anthropic; model Claude Fable 5.1) working under V.S.'s direction; session outputs are committed with the session identified in the commit trailers; every number was checked against its source file before commit, and each adversarial review re-traced every number of the preceding draft, with findings (including errors found) in `notes/`; V.S. takes responsibility for analysis, text and claims. Journal-specific wording [TK].

**(b) Why it is there.** Disclosure, and an explanation of what "review computation" and "adversarial review" have meant throughout: reviews run by the same system under the author's direction, not by independent people.

**(c) What a sceptic asks.** *Three "adversarial reviews" by the same AI that wrote the paper — is that adversarial?* The paper does not argue the point; it states what the reviews did (re-traced every number, found the errors listed in `notes/`, wrote and ran the finite-sample null, found the split-half flaw, found the dropped proportionality cell) and where their findings are. *What did you do?* CRediT and this statement together: direction, the record's rules, the checking of every number, and responsibility.

---
## Where explaining it exposed a problem

Every place where writing the plain-language version showed the paper stating something without justifying it, using a term it never defines, compressing a step a reader needs, or making a claim I could not rebuild from the paper's own text. Listed in the order of the paper, with the location first. Where I quote my own arithmetic it is labelled as mine. Every item was addressed in the paper's revision of 15 September 2026 (record, "Text revision after the plain-language companion"; items 29(a) and 29(b) by computations run under a pre-run entry, the rest by text); the list is kept as the record of what was found, with the table numbers of the revised paper.

1. **Abstract, Results; Results 1 — "the excess" (undefined at first use).** The abstract says "the excess with the wrong sign (−0.084 nats against rtr +0.039)"; the term is defined only in Results 1 as sts − (xtx + yty). An abstract reader cannot tell what quantity has the wrong sign.

2. **Abstract, Results — "not significantly per subject (N = 14)" (compressed).** The sentence "CCS-sts is uncorrelated with r₁ across pairs (r ≈ −0.01; MMI-sts +0.7) and not significantly per subject (N = 14)" does not say what is not significantly correlated with what per subject. Results 3 shows it means the per-subject CCS-sts DiD against the per-subject autocorrelation DiD (r = −0.420 etc., all p ≥ 0.127). The abstract also says "uncorrelated" flatly where Results 3 says the zero correlation "bounds the dependence rather than excluding it".

3. **Abstract, Conclusions; Discussion, "What the finding is and is not" — "114 %" (three unreconciled versions of the same prediction).** The paper contains three different autocorrelation-based predictions of the sts DiD: −0.087 nats from the map projection at (0.848, 0.24) with ∂sts/∂r₁ = 5.99 (Results 2); −0.0924 from the per-pair diagnostic (Results 4, Table 4; this is the "114 %" and the "over-predicting by 14 %"); and −0.069 for the change in the *true* sts from the observed autocorrelation-function change at fixed q, of which the W = 60 estimator returns −0.056 (Results 6, matched-null family). No sentence relates the three, and a reader of the abstract cannot tell which is meant by "predicts ... 114 % of the magnitude".

4. **Introduction, paragraph 2 — "ΦWMS" and "innovation correlation" (undefined).** "with a = 0.4 and ΦWMS and ΦR plotted against the innovation correlation": ΦWMS is never defined or used again; "innovation" is only implicitly defined in Methods, "Closed-form atoms" (corr(ε_t, η_t) = q).

5. **Methods, Estimator — "integrated autocorrelation time is about 3 TRs" (no formula).** The six autocorrelation values are given but the definition of the integrated autocorrelation time is not. With the usual 1 + 2 × (sum of the lag-1 to lag-6 values) the six values give 1 + 2 × 1.175 = 3.35 (my arithmetic); a reader who does not know the formula cannot rebuild "about 3" or the "≈ 20 effective samples" that the abstract, Methods and Limitations all quote.

6. **Methods, Estimator — the closed-form implementation is "the same estimator" (scope not stated).** The argument given (time mean of local Gaussian MI equals the plug-in MI; lattice inversion is linear) holds for MMI. CCS keeps or discards each time point by a sign condition, so its atoms are not functions of the window's 4 × 4 matrix alone. The paper does not say whether `notes/rev_phiid_fast.py` is MMI-only or whether the map and the diagnostic (both MMI) are its only uses.

7. **Methods, "The two redundancy functions" — "product lattice", "non-bottom nodes", "maximum-entropy projection" (undefined).** The double co-information is defined as "the signed sum over the fifteen non-bottom nodes of the product lattice"; neither the product lattice nor its nodes are introduced, and the signs of the sum are not given. The last sentence contrasts "the fitted Gaussian of the data, p(x, y) as in Ince's original preprint" with "the maximum-entropy projection of Ince's published version" without saying what the projection is or what difference it makes; the reader cannot judge whether the choice matters.

8. **Methods, "Closed-form atoms"; Results 1; Table 1 — the family predicts xtx = yty = rts = str = S − C, and the mirror atoms each −(S − C); the data disagree, and only one disagreement is reported.** Table 1 has xtx = 0.6273, yty = 0.6125, rts = 0.5669, str = 0.5667, and the four mirrors at −0.5352 to −0.5358. The self-prediction atoms exceed rts and str by about 10 % and the mirrors match −rts more nearly than −xtx (my comparison of Table 1's entries). Results 1 reports the sign violation of sts − (xtx + yty) as "the one respect" in which the data violate the family ("The data violate the family in one respect") and says nothing about these.

9. **Methods, "The family with lagged coupling" — "amounts comparable to a change of a few hundredths in r₁" (not reconstructible).** The paper gives slope −1.77 nats per unit c and curvature +40 nats per unit c² but never says what size of c is realistic. From those numbers, c = 0.02 moves sts by −1.77 × 0.02 + 40 × 0.02² ≈ −0.02 nats, which at ∂sts/∂r₁ ≈ 6 is about 0.003 in r₁, not "a few hundredths"; the sentence is true only for |c| of order 0.05–0.1 (my arithmetic). The value of c the comparison assumes is missing.

10. **Methods, "The scope map" versus Figure 2 caption — which grid Figure 2 is drawn on.** Methods says the (r₁, q) evaluation was on r₁ ∈ [0, 0.95] × q ∈ [−0.6, 0.6], "the grid on which Figure 2 is also drawn"; the Figure 2 caption says panel (c) is drawn "on the wider grid |q| ≤ 0.95". Both are true of different panels, but the Methods sentence as written is wrong for panel (c).

11. **Methods, "The DMT contrast" — window 5 excluded for "an injection response at bins 8–10", but bin 8 is in the pre-injection set (windows 1–4 = bins 1–8).** The paper does not say why a response that begins at bin 8 leaves bin 8 in "pre" and removes only bins 9–10. Figure 4 shows the observed sts of both runs dipping at window 5 and the pre band ending at 8 min, so the figure and the window sets are consistent with each other; the "bins 8–10" sentence is what does not fit.

12. **Methods, "Multiplicity" — the weighting rule has no date, commit or record entry.** Every other rule in the paper carries a commit (febf599, 33f0b33, …) or a record entry and time. The rule that inferential weight goes to "results whose sign-flip and phase-randomised p are both ≤ 0.005 across variants" is the one by which the paper later declines to read the residual (p = 0.042) and the primary-cell CCS-sts (p = 0.056), and the paper does not say when it was set.

13. **Methods, "Multiplicity"; Results 2 — the central input fails the paper's own weighting rule, unremarked.** "DMT changes r₁" rests on a DiD with sign-flip p = 0.0106 and phase-randomised p = 0.0729 on `ts_gsr` (p = 0.0017 and 0.0390 on `ts_demean`). By the rule of Methods that is a result "reported as such and ... not treated as an established effect". The paper never says that the autocorrelation change itself does not meet the rule, nor that the account rests on the per-subject collinearity and the per-pair prediction rather than on this p. Results 3 does flag the discrepancy between the two contrasts under the temporal null (3.8 against 1.8 null SD) as unexplained.

14. **Methods, "The residual diagnostic" — "cell" used for two different partitions.** "the four cells of `residual_source.log`" (DMT-pre, DMT-post, placebo-pre, placebo-post, judging from "For the DMT-post cell") is not the same "four cells" as Table 4's and Table 3's variant × estimator cells. Neither meaning is defined.

15. **Methods, "Bias simulations"; Results 6 — "three families" become "four matched pairs" / "four matched families".** Methods lists three families for the sts-matched null (the record's asymmetric VAR(1); a VAR(1) at a = 0.87; Gaussian processes with the placebo and post-DMT autocorrelation functions). Results 6 reports manufacture "in the four matched pairs" and "in three of the four matched families". The paper does not say how three become four (presumably the third family yields two pairs), and two of the four manufacture figures carry "±" ranges while two do not, with no explanation of why.

16. **Results 1 — "the block's net change is a small fraction of the change in TDMI" (no number).** Adding Table 1's DiDs: block −0.1624, mirrors +0.1607, net −0.0017 against TDMI −0.1037 (my arithmetic). The sentence is right but the reader has to compute it.

17. **Results 2 — "Real BOLD has its power at the low end of the band, so these are lower bounds" (asserted from one number).** The only evidence given is that the ideal band-passed value 0.82 is below the measured 0.866 in this dataset; no spectrum or centroid is shown for the baseline, although a spectral centroid *change* is reported in Results 5.

18. **Results 3, paragraph 1 — "0.99 at the operating point" and "0.98 on the family" are two different family quantities, unlabelled.** "∂sts/∂r₁ / ∂TDMI/∂r₁ = 0.99 at the operating point" is the family's share of the *change*; "against 0.98 on the family" two clauses later is the family's baseline share sts/TDMI at the same point (2S − C over 2S; my identification from the closed form). The text gives both numbers without saying which is which, next to the data's 0.78 and 0.78, which are the baseline share and the share of the DiD respectively.

19. **Results 3, paragraph 2 — "r = 0.953 leaves 9 % of the per-subject variance, which the diagnostic finds significant (Results 4)".** The 9 % is the between-subject variance of the sts DiD not shared with the autocorrelation DiD. The diagnostic's significant quantity is the group-level DiD of a per-pair residual (+0.0115, p = 0.042). These are not the same remainder, and the sentence presents the second as a test of the first.

20. **Results 3, CCS paragraph; Methods, "History" — the closure entry's scope.** History describes the closure entry as the dated entry that closed the ΦR exploration "recording why its positive whole-brain result supports no claim". Results 3 cites "the record's closure entry" as a rule that "forbids a DMT-specific claim from any specification chosen after the primary result". The second is a general rule the first does not state; the reader cannot reconstruct its scope from the paper.

21. **Results 4, paragraph 2 — "A positive mean coupling of about +0.006 would" (referent unclear).** "would" what: produce the residual DiD (+0.0115), the level residual (−0.0489), or the part of the residual DiD the null does not account for? With the slope −1.77 nats per unit c, a coupling of +0.006 corresponds to about −0.011 nats of sts (my arithmetic), which matches the residual DiD's size but with the sign logic (positive coupling lowers sts, so a *fall* in coupling under DMT would raise the residual) left to the reader.

22. **Results 4; Table 4 — the "observed level" column is not the pre-injection level, and its averaging set is not stated.** Table 4 gives observed sts 1.1377 (W = 60) and 1.2883 (global) where Tables 1 and 2 and Results 6 give the DMT pre-injection means 1.1554 and 1.3085. The text's "392 cells" (presumably 14 subjects × 2 runs × 14 windows; my reading) suggests the level is an average over both runs and all windows, but the table and text never say so, and the 4.3 % is quoted throughout as if it referred to the same level as the DiDs.

23. **Results 4; Table 4 — "residual DiD = observed by construction" for the run-level rows (compressed).** The reader has to work out that a single run-level fit yields one predicted sts per run, so the predicted DiD is zero and the residual DiD equals the observed DiD. One clause would do it.

24. **Results 5 — "significant on both nulls at both estimators wherever the lag-τ autocorrelation contrast is" (numbers not in the paper).** Table 6 holds only the sign-flip p at W = 60; no phase-randomised p and no global-fit values for the lag variants appear anywhere in the paper. The claim is traceable only to `lag_tables.md`.

25. **Results 5 — "spectral centroid" (undefined).** "the in-band spectral centroid rises accordingly (+0.0023 Hz …)" is the only occurrence; the term is not defined and the reader is not told it is a review computation until the parenthesis "review, section 1".

26. **Results 6 — "of the real DiD" (base not stated).** "manufactures a difference at W = 60 of −9 %, +16 %, +7 % ± 8 % and −8 % ± 6 % of the real DiD": the real DiD of which quantity in which cell is not stated (presumably the observed −0.0809 on `ts_gsr`).

27. **Discussion, "Redundancy functions" versus Methods — what CCS-sts is averaged over.** Methods: "under either mask CCS-sts is 0 at the selected samples and −c elsewhere", i.e. an average over all samples with zeros at the selected ones (and the atoms must sum to TDMI over all samples). Discussion: "CCS-sts is −c averaged over the samples where the five local signs disagree", which reads as a conditional average over the disagreeing samples only. The two differ by the fraction of disagreeing samples (about 62–65 %, from the 35–38 % that Results 1 says the mask selects; my subtraction); one of the two wordings is loose.

28. **Discussion, "Recommendations" versus "What the finding is and is not" — the same p = 0.042 is "a significant remainder" in one and "not ... established" in the other.** Recommendations: "since here a 0.95 collinearity left a significant remainder". Discussion 1: "(p = 0.042 at the primary cell, which the weighting rule of Methods does not treat as established)". The reader is left to decide which sense of "significant" the recommendation relies on.

29. **Discussion, "Limitations" — two cheap computations "were not run", with no reason given.** The regional test of the spatial-map claim (which bears directly on the Luppi et al. 2022 discussion) and the run-level mean cross-lag deviation (which would test the pooling mechanism named as the candidate explanation of the run-level residual) are both described as extensions from saved outputs. The paper says they were not run but not why, given that the residual's remainder and the spatial-map claim are the two things most in need of them.

30. **Supplement pointer S1 — "the redundancy prediction" (named, never described).** The main text never says what was predicted about redundancy in the original analysis or what happened to it.

31. **Table numbering — out of order of appearance.** In the earlier draft the CCS/ΦR table was printed before the residual diagnostic's table but numbered after it, and the split-half table before the lag table likewise; the revision renumbers them in order of appearance (CCS/ΦR 3, residual 4, split-half 5, lag 6), the numbering used throughout this companion.

32. **Figure 2 caption versus Results 2 — the overlay's window.** Results 2 says subject 1's pairs were placed on the map "for both variants, both runs, windows 1–4 and 6"; the figure draws one cell (DMT run, window 6, 1,500 of 6,555 pairs). The text does not say the figure shows one of the ten cells or how the 1,500 were chosen.

33. **Methods, "History"; Abstract — what "pre-specified" protects.** The abstract says the study "began as a pre-specified test of synergy up-regulation". History says the initial commit carrying the hypothesis also carried a 20-region real-data global fit, written to disk seventeen minutes earlier, with a DiD negative in 12 of 14 subjects, and that the git record "establishes ordering, not blindness". The paper never says whether that 20-region result was inspected before the hypothesis was written, so the reader cannot reconstruct what the word "pre-specified" in the abstract is protecting beyond the ordering of the windowed test's rules.

34. **Methods, "The residual diagnostic"; Results 4 — "near zero" has no stated criterion.** The plan's first branch was "a residual DiD near zero"; Results 4 says the observed +0.0115 "is not near zero by this study's conventions". The paper never states the convention — a fraction of the observed DiD, a CI including zero, or a sign-flip p above some level — so the reader cannot check that the first branch was in fact missed rather than narrowly met (the observed CI is [+0.0021, +0.0211] and the null's own value is +0.0054).

35. **Figures; `figures/captions_v2.md` header — the figures carry no git SHA.** The captions file opens "Generated by `scripts/15_figures_v2.py` at git nogit, seed 20261120". Data and code availability says every results table carries the git SHA that produced it and that the figures are regenerated by that script; the captions show the figures were generated in a checkout without git, so the commit that produced the five figures in the paper is not recorded anywhere the reader can see.
