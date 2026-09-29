# B25 audit: `notes/partB25_binarised.py`, its pre-run entry and `b25_fill.py` (28 Sep 2026)

Tree audited: `b32/audit/treeA_v1` (read only). Everything that runs was run in the copy `b32/audit/scratch_b25/tree` with
`v312/bin/python` (numpy 2.5.3, scipy 1.18.1, phyid 6c5f2e9, identical to `phyid_src`). The audit's scripts are in
`b32/audit/scratch_b25/tools/` (t1–t12). `tools/b25lib.py` loads the script's function definitions by executing its source
only up to `if SELFTEST:` (l. 478). Every evaluation of the family comes after that line.

**Pre-registration.** Nothing binarised was computed for the symmetric AR(1) family. `partB25_binarised.py` was run only
with `--selftest`, in the copy. That run gave 53 checks, 0 failed, 74 s, and reproduced the entry's 9.8 × 10⁻⁹ and
2.8 × 10⁻¹⁷. The other tests used five kinds of input:
- random correlation matrices;
- VAR(1) pairs with lagged coupling, the symmetric ones chosen far from the family (coupling 0.3–0.6, a ≤ 0.5);
- Ince's textbook distributions;
- the family's continuous moments only, at off-grid (a, q);
- synthetic outputs of arbitrary numbers for `b25_fill.py`.

The planning session's f′ values in the entry's (iii) (1.34 and 0.13 bits per unit) were **not** checked, because checking
them needs a binarised quantity of the family.

---

## Findings (most serious first)

### 1. Checks on quantities that carry no prediction can stop the pre-registered report (script l. 381, 531–535; fill l. 71–73; record l. 7784–7786)

**What is wrong.** The fill writes nothing if B25 reports any failed check. The entry says the same ("it stops without writing
if … reports a failed check") and then says "The result is reported whatever it is". Two checks cover all nine QUANTS,
including the four quantities that carry no prediction: CCS-pub sts, CCS-code sts, CCS EC and Ince EC.
- The two-step rate check: |r(10⁻⁴) − r(10⁻³)| ≤ 1 % + 10⁻⁶.
- The comparison of phyid at 10 × 10⁵ with the limit.

In the limit these four quantities are not smooth. They jump wherever a local sign mask flips:
- a sign of a local MI inside `_ccs_red` or the double-redundancy mask;
- a sign of ds1, ds2 or dsj inside Iccs.

If a flip lies within ±10⁻³ of (0.85, 0.25) along either axis, the rate check fails. If a flip lies close enough that the
n = 10⁵ estimates straddle it, the phyid check can fail. Either way the fill refuses to write, so predictions (a)–(c) cannot
be reported by the text fixed before the run.

**Evidence.** The paths below are not the family (t10, t11):
- Symmetric VAR(1) with A = [[a, 0.3], [0.3, a]] and innovation correlation 0.3, a from 0.10 to 0.50 at step 5 × 10⁻⁴.
  CCS-pub sts, CCS-code sts and CCS EC each jump once, and Ince EC jumps twice. The jumps are 0.004–0.010 nats.
- An asymmetric path: CCS-pub sts and CCS-code sts jump once each.
- MMI sts never jumps on either path.
- 5 × 10⁻⁴ from the CCS-pub flip (a* = 0.229666, jump +0.00983 nats):
  - ∂(CCS-pub sts)/∂a is −0.1195 at step 10⁻⁴ and +4.7679 at step 10⁻³, so the rate check **FAILS**. At 2 × 10⁻³ from the
    flip it passes.
  - `long_series_check` printed "CHECK FAILED: … CCS EC of phyid at n = 100,000 within 4 SE + 2e-4 of the limit".

At the jump densities seen here (0–2 per 0.4 of parameter range for each of the 4 quantities, on 2 axes), the chance that
some flip lies within the ±10⁻³ window is of the order of a few per cent. On the family this cannot be known before the run.

**Proposed correction** (before the run; the entry and the script are not yet committed — «ENTRY_TIME» is still a placeholder):
- **(a) Script.**
  - Keep the stopping checks for the quantities that are smooth on the family: `SMOOTH = ("MMI sts", "MMI EC", "2A", "TDMI", "MMI rtr")`.
    Their MMI selections are strict (B < A) or exact ties.
  - In the rates loop (l. 531–535), call `check(...)` only when `k in SMOOTH`.
  - For the four CCS/Ince quantities, record the step-10⁻³ rate too, e.g. `rec("a", est, f"d({k})/d{lab} [step 1e-3]", …, rc)`,
    and print "not differentiable on the 10⁻³ scale" when the two steps differ.
  - Give `long_series_check` a `checked=` argument. Pass `SMOOTH` for the family's operating point and keep all QUANTS in
    the self-test.
- **(b) Fill.** Where the text quotes ∂/∂r₁ and ∂/∂q of Luppi et al. (2023)'s emergence capacity (RESULTS, S19 row (d), S20_G),
  quote them only if the two steps agree within the 1 % rule. Otherwise write "not differentiable at the operating point on
  the 10⁻³ scale (a sign mask changes there)".
- **(c) Entry, Rule.** Add: "A failed check on a quantity that carries no prediction is reported in the outcome entry and does
  not stop the verdicts of (a)–(c)."

### 2. The fill writes that a re-run reproduced every value before any re-run exists (fill l. 268–274 = G09, l. 278–283 = G11)

**What is wrong.** Two replacements assert a re-run the fill knows nothing about:
- G09 (main text, Data and code availability): "…it was run at {A} in a session of the AI system and re-run at the same
  commit by a separate session, which reproduced every value."
- G11 (S5 Text §4): "…and re-run at the same commit by a separate session, which reproduced every value".

The fill runs right after the writer's run. It has no input from any re-run, and no tolerance defines "every value". The
entry itself puts the re-run later ("a separate session re-runs it … before the commit that reports it is pushed"), and so
does the outcome entry that the fill writes (l. 381–382: "A separate session re-runs it at {A} before this commit is
pushed"). So the paper would assert, in the past tense, an event that has not happened and that nothing checks.

**Evidence.** Synthetic run `scratch_b25/fill_rising/tree` (arbitrary numbers). The fill wrote both sentences with "READY".
It holds no re-run information.

**Proposed correction.**
- Delete the clause from both templates:
  - G09's inserted text ends "…it was run at {A} in a session of the AI system. The HRF-deconvolution items".
  - G11 reads "…its outputs carry …) ; it was added to `run_all.sh` after the final run."
- Let the re-run session add the reproduction sentence, with the comparison it made (e.g. "every value of `binarised.csv`
  identical" or "within 10⁻⁹"), in the commit that follows the re-run.
- Alternatively, give the fill a third argument (the re-run's output directory). Compare every CSV value, and write the
  clause only if all agree within a stated tolerance.

### 3. The pre-run entry misreports the address Luppi et al. (2023) print (record l. 7739–7740; the same text in `notes/review_2026-09-28/revision/text_replacements_2026-09-28.json` l. 775)

**What is wrong.** The entry says: "no repository was found on 28 September 2026 at the address Luppi et al. (2023) print,
github.com/robince/partial-infodecomp". The paper does not print that address:
- On p. 12 it prints "https://github.com/robince/partial-info-" at a line end, then "decomp)" on the next line
  (`cite/txt/Luppi2023/p012.layout.txt` l. 11–12).
- The PDF's link annotation on that page is exactly `https://github.com/robince/partial-info-decomp`, the repository the
  script reads. Extraction with pypdf of `cite/pdf/Luppi2023.pdf`, page 12, `/Annots` → `/URI`.

The raw text (`p012.raw.txt`) dropped the line-end hyphen, which is how "partial-infodecomp" arose. The script's docstring
gives the correct address.

**Proposed correction** (record and JSON):
- Old text: "…of\ngithub.com/robince/partial-info-decomp at 3220716, read, not run; no repository was found on 28 September
  2026 at the\naddress Luppi et al. (2023) print, github.com/robince/partial-infodecomp)."
- New text: "…of\ngithub.com/robince/partial-info-decomp at 3220716, the repository Luppi et al. (2023, p. 12) print and link
  (the address\nbroken across a line at its own hyphen), read, not run)."

### 4. `binarised.csv` carries no git line, yet the fill's texts say all three outputs do, and the verdicts are read from that CSV (script l. 104, 638–639; fill l. 62–70, 280, 381)

**What is wrong.**
- The script writes `binarised.csv` with the header "part,estimator,quantity,r1,q,T,value,se" and no "# … git=" line (l. 104,
  639).
- The outcome entry template says "the three outputs, `…binarised_tables.md`, `binarised.csv` and `binarised_run.log`, carry
  `git={A}`" (l. 381). S5 Text (G11, l. 280) says "its outputs carry `git={A}`".
- The fill checks the commit only in the tables and the log (l. 67–70). The file every verdict is computed from is tied to
  the run only by the two step counts (l. 113–116).

**Proposed correction.**
- **Script.** Build the CSV text first, then add its hash to the table header before writing both:
  `L.insert(3, f"binarised.csv sha256 {hashlib.sha256(csv_text.encode()).hexdigest()}")`.
- **Fill.** Recompute the hash and stop if it differs.
- **Text.** "…`binarised_tables.md` and `binarised_run.log` carry `git={A}`, and the tables the sha256 of `binarised.csv`".

### 5. Ungrammatical sentence when MMI-sts and its emergence capacity get the same non-rising description (fill l. 154–156)

**What is wrong.** `MMI_DESC` appends "and so does its emergence capacity" whenever the two `desc_q` strings are equal. If the
shared string is "is not monotone in r₁ (it rises at k of the 7 steps) at each q", or a per-q list that begins with "is", the
S3 Text sentence becomes ungrammatical: "…binarised MMI-sts is not monotone in r₁ (…) at each q, and so does its emergence
capacity."

**Evidence.** Synthetic run `scratch_b25/fill_samenm` (arbitrary numbers, `sin` wiggle) produced exactly: "In the long-series
limit binarised MMI-sts is not monotone in r₁ (it rises at 4 of the 7 steps) at each q, and so does its emergence capacity."

**Proposed correction.**
```python
d_s, d_e = desc_q("MMI sts"), desc_q("MMI EC")
MMI_DESC = (f"binarised MMI-sts {d_s}, and so does its emergence capacity"
            if d_s == d_e and d_s in ("rises with r₁ at every step at each q", "falls with r₁ at every step at each q")
            else f"binarised MMI-sts {d_s}, and its emergence capacity {d_e}")
```

### 6. IPF stops silently without converging, taking 3–5 s each time (script l. 252–268, 275)

**What is wrong.** `ipf_maxent` returns `(Q, it_max, err)` after 100,000 sweeps when the tolerance of 10⁻¹⁵ is not reached.
`ince_pid` discards `it` and `err`, so nothing counts or reports this. It happens whenever the maximum-entropy solution lies
on the boundary: zeros that no single pairwise marginal forces. IPF then converges only sublinearly.

**Evidence** (t4, t4b, t4c, t9):
- Five of the self-test's twelve Ince examples (OR, AND, SUM, Reduced OR, W&B modified 2) end at 100,000 sweeps with marginal
  error 0.8–1.2 × 10⁻⁶, about 3.4 s each (≈17 s of the self-test).
- Plug-in tables of T = 160 VAR(1) pairs:
  - AR 0.85–0.97, random innovation covariance: 34 of 2,832 hit the limit, at 3.2–4.6 s each.
  - AR 0.6–0.95, lag-0 correlation 0.1–0.5, weak coupling: 0 of 4,500 at T = 160, 300 or 840.
- In a 60-replicate timing at T = 160, one such call raised the mean time per replicate from 4 ms (median) to 61 ms.
- Values are barely affected. Against the exact maxent (support by one LP per cell, then IPF on the support, converged in 1–21
  sweeps), the Ince EC differs by ≤ 3.5 × 10⁻⁶ bits on the 34 tables, and the Ince examples' PIDs by ≤ 3.6 × 10⁻⁶ bits.

So this is a silent approximation and a runtime risk, not a wrong result.

**Proposed correction.**
- Return `(it, err)` from `ince_pid`. Keep the largest `err` and the number of calls that reach `it_max`, and report them in the
  tables. Make `max err ≤ 10⁻⁹` a check.
- For speed and exactness: when 2,000 sweeps do not reach the tolerance, find the support with `scipy.optimize.linprog` (for
  each cell c, the maximum of Q(c) under the three pairwise-marginal constraints; c is in the support iff that maximum is
  > 10⁻¹²). Then restart IPF from the uniform distribution on the support. This is `maxent_exact` in
  `tools/t4b_ipf_error.py`.

### 7. Dates are hard-coded where the run or the fill may fall on 29 September (fill l. 279, 370, 377)

**What is wrong.** Three dates are fixed in the templates:
- "## B25, outcome, 28 Sep 2026 {TIME_B} UTC" (l. 377);
- "was run on 28 September 2026" (G11, l. 279);
- "The text that reports B25 (28 September 2026)" (numbers-table header, l. 370).

The script prints no date, so a run or fill after 24:00 UTC produces false dates.

**Proposed correction.**
- The script prints `time.strftime('%d %b %Y %H:%M UTC', time.gmtime())` beside `git=` in the tables' header.
- The fill reads the run's date from the tables, and its own date from a third argument (or `datetime.now(timezone.utc)`),
  and uses them in the three places.

### 8. "Seven further entries … (B18; the CCS quantities of B25)" miscounts (fill l. 236–239)

**What is wrong.** The B25 entry recorded three predictions, which are counted among the 56. It is not a "further entry" that
"recorded no prediction". Only its part (d) did.

**Proposed correction.** Keep "Six further entries … or recorded no prediction (B18)" and add ", and B25 recorded none for its
CCS quantities (row B25 (d))" before "; the branch that obtained is given in each row."

### 9. S20 Table row 2: the inserted sentence takes the antecedent of "inside it" (fill l. 222–224, 260–261)

**What is wrong.** G05 and G05L insert the S20_G sentence ("On the symmetric family this estimator … (S3 Text §11).")
between "…outside the map, which is Gaussian-MMI (…)." and "The Gaussian and the MMI validations are inside it if…". "It"
now reads as "this estimator" or "the family", not "the map". Seen in `scratch_b25/fill_rising/tree/manuscript/supplementary.md`.

**Proposed correction.** Extend the old and new strings of G05 and G05L by " The Gaussian and the MMI validations are inside
it", and replace it with "… (S3 Text §11). The Gaussian and the MMI validations are inside the map".

### 10. The per-SD ratio is printed at one decimal where the verdict turns on 1, and a negative ratio reads oddly (fill l. 164, 214)

**What is wrong.**
- RESULTS and S19 row (b) print `m(ratio_sd, 1)`. Any ratio from 0.95 to 1.049 prints "1.0", whether (b) is "met" or "partly
  met".
- When ∂/∂r₁ < 0, the text reads "the r₁ rate is −5.1 times the |q| rate" (seen in `fill_mixed`).

**Proposed correction.**
- Use `m(ratio_sd, 2)` in both places (the outcome entry already does).
- When `dr1 <= 0`, write "∂(MMI-sts)/∂r₁ is not positive, so the per-SD comparison does not arise" instead of the ratio.

### 11. Two statements of the entry do not match their sources (record l. 7760–7763, 7769–7771)

**What is wrong.**
- (a) "(0.0284 for pair r₁ and 0.1957 for |q|; main text, Results 1)": the main text prints 0.196 (draft_v2.md l. 53). The
  value 0.1957 is in S3 Text §4 and in `aligned_directed_tables.md` l. 27.
- (b) "reproducing, to their printed four decimals, the twelve decompositions that Ince (2017, Tables 6 and 8–11 and 13)
  publishes or … `examples2d_output.txt` prints": only Table 8 prints four decimals. Tables 6, 9, 10, 11 and 13 print two
  decimals or integers. The four-decimal values compared are those of `examples2d_output.txt`, which prints all twelve.

**Proposed correction.**
- (a) "(0.0284 and 0.1957; S3 Text §4, B22 (d); 0.196 in Results 1)".
- (b) "reproducing, to the four decimals of `examples2d_output.txt`, the twelve decompositions it prints, seven of which
  Ince (2017, Tables 6, 8–11 and 13) also publishes".

### 12. What the texts attribute to Luppi et al. (2023) beyond what the paper states (script docstring l. 20–25, 40–42; fill l. 170–173, 222–224)

**What is wrong.** The paper supports the following (pp. 11–12): "emergence capacity" (downward causation + causal
decoupling), computed "more directly from partial information decomposition tools" (the toolbox), the CCS method, and the
plug-in estimator "applied to the mean-binarised BOLD signals". Two points are B25's reading, not the paper's:
- **The target.** The joint future as one four-state target is not stated. It follows from "emergence capacity"
  (= Σ_β {12}→β = the PID synergy about the joint future). S20_G states it as the study's estimator ("with the joint future as
  target").
- **The binarisation.** At finite length B25 binarises phyid's four slices at four slice means. The paper binarises each BOLD
  signal once at its mean. The effect is negligible: on a VAR(1) pair at T = 160 (t12), 63 % of the tables differ, but the
  mean Ince EC difference is −3.8 × 10⁻⁵ ± 8.1 × 10⁻⁵ nats.

The paper also deconvolved the HRF before binarising (p. 12); S20 row 2 already says so.

**Proposed correction.**
- S20_G: "…this estimator, as we read it (Ince's CCS on mean-binarised signals, the joint future as one target)…".
- In the S3 section add "(each of the four lagged series binarised at its own mean, as phyid does; Luppi et al. binarise each
  signal once, which differs by O(1/T))".

### 13. Latent NaN in `estimators_of_pmf` for distributions with empty cells (script l. 318–319)

**What is wrong.** `self2` and `tdmi` use `np.dot(w, mi[...])` over all 16 patterns without the `keep` mask. When a pattern
probability is 0, the local value is inf − inf = NaN and the sum becomes NaN. On 60 finite VAR(1) tables (t1b), TDMI was NaN
in the 14 with an empty cell.

This is not triggered by the script: the limit has all 16 probabilities > 0, which is checked, and the finite path takes 2A
and TDMI from phyid.

**Proposed correction.** `self2 = float(np.dot(w[keep], mi["I_xta"][keep]) + np.dot(w[keep], mi["I_ytb"][keep]))`, and the
same for `tdmi`.

### 14. The fill crashes instead of stopping cleanly if the entry's time placeholder is left (fill l. 152–153)

**What is wrong.** If «ENTRY_TIME» is still in the record, `re.search(...).group(1)` raises `AttributeError`. It happens
before anything is written, so nothing is corrupted, but there is no "NOTHING WRITTEN" message.

**Evidence.** `scratch_b25/fill_notime`.

**Proposed correction.** Test the match and `sys.exit("NOTHING WRITTEN: the pre-run entry's time is not filled")`.

**Note on applying any change to `b25_fill.py`.** Its sha256, 8c5ba7e1…f98887 (verified), is quoted in the citation-crosscheck
entry (record, item 10, l. 7715) and in that entry's source in `text_replacements_2026-09-28.json`. Update both.

### Minor wording, no effect on numbers

- The docstring's "One generator" is not literally true: `genz4` makes its own `default_rng(SEED)` for every call. It is
  harmless and deterministic.
- S3 §11, "orthant probabilities … computed exactly": they are computed by quadrature to about 10⁻¹³.
- S3 §11 derivation paragraph: add "in the long-series limit (for 0 < q < 1, so that B < A)". At finite length the plug-in
  breaks F = I(x_t, y_t; x_{t+1}) and the ties.
- The CHECK FAILED message of `long_series_check` calls the excess over 4 SE a "|difference|".

---

## Checked and found correct

1. **Plackett's reduction** (l. 167–189).
   - It computes P₄ = 1/16 + ∫₀¹ Σ_{i<j} R_ij φ₂(0,0; tR_ij)[1/4 + arcsin ρ_{kl·ij}(t)/(2π)] dt along R(t) = I + t(R − I).
   - The conditional covariance is the Schur complement, φ₂(0,0;ρ) = 1/(2π√(1−ρ²)), and n = 3 uses the conditional 1/2.
   - Against Genz it agrees to 9.8 × 10⁻⁹ on 20 random matrices (self-test). It agrees to 4.6 × 10⁻⁸ on 40 lag-1 matrices of
     strongly autocorrelated VAR(1) pairs with lagged coupling (a up to 0.97, lag-0 correlation up to 0.6). There were no quad
     warnings, and each Genz call takes about 1.1 s.
   - The three-variable closed form agrees to 5.6 × 10⁻¹⁷.
2. **Inclusion–exclusion** (l. 198–217). All 16 pattern probabilities equal the Genz orthant probability of DRD, with
   D = diag(±1), to 3.5 × 10⁻⁸ (t2, 6 matrices). The sum and the pair-marginal checks are exact to about 10⁻¹⁶.
3. **The limit of per-slice mean binarisation is binarisation at 0.** The self-test's two VAR(1) pairs and two symmetric,
   time-reversible VAR(1) pairs (t8) match the limit within 4 SE + 2 × 10⁻⁴ for all nine quantities.
4. **The discrete path equals phyid**, read line by line:
   - `_MI_SETS` against `I_res`; the MMI candidate pairs and phyid's tie rule; the double-redundancy candidate order;
     `_ccs_red` against `redundancy_ccs`.
   - `rev_phiid_fast._M` equals `calculate.py`'s matrix, and ATOMS and KNOWNS are in phyid's order (checked programmatically).
   - Numerically (t1, t1b): on 60 finite VAR(1) samples (T = 160–5,000), the script's pattern-weighted estimators applied to
     the empirical pattern frequencies equal phyid's time-averaged atoms to ≤ 5.3 × 10⁻¹⁴ nats for every quantity. MMI
     selects by the mean; CCS uses pointwise masks.
5. **Ince's PID.**
   - `ince_pid` implements the NA = 2 branch of `Iccs.m`: ds1 and ds2 from P, dsj from P̂ with Ps from P, the sign chain,
     weighting by P̂, and nansum through the `valid` mask. It implements `calc_pi.m`'s synergy with no thresholding or
     normalisation, as in `compare.m`'s call.
   - It agrees with dit 2.3's `PID_CCS` (Definition 2 constraints) to ≤ 3.8 × 10⁻¹⁰ bits on 30 random full-support 2×2×4
     tables and 40 VAR(1) plug-in tables (t7).
   - IPF's P̂ equals `maxent_dist` by `mme2.py`'s route (all pairwise marginals of the 3-d array) to ≤ 9.4 × 10⁻¹¹.
   - `P.reshape(2, 2, 4)` gives the axes (x_t, y_t, 2x_{t+1} + y_{t+1}).
   - The 2023 change to `Iccs.m` does not alter the two-source branch; `fixsign` is defined but not used.
6. **Emergence capacity.** On phyid's lattice str + stx + sty + sts = I_xytab − I_xtab − I_ytab + R_xytab, for any
   redundancy. Under MMI this is the whole-minus-max of Luppi et al. (2024, Eq. 5; seen on p. 20). Under CCS it does not
   depend on the double-redundancy mask.
7. **The derivation** (entry (i)–(ii), S3 §11 text). A symbolic solve of phyid's 16 × 16 system (t5) gives
   sts = T − F − G + 2A − B and EC = T − F.
   - With G = F (time reversal): sts = T − 2F + 2A − B.
   - Gaussian F = A, T = 2A: 2A − B = 2S − C and EC = S.
   - q = 0: 2A and A.
   - The same holds through the script's own code path on 10⁴ random knowns (≤ 8.9 × 10⁻¹⁶).
   - The MMI selections need B < A, which holds for 0 < q < 1. A = 1 − H₂(arccos r₁/π) bits is correct.
8. **`simulate_family`.** `zi = (1−b)w₀` makes x₀ = w₀, a stationary start with correlation q. At off-grid (0.5, −0.3) and
   (0.3, 0.7), with continuous moments only (t6), the start has variance about 1 and correlation q, and the long-series lag-1
   matrix equals `ar1_corr(a, a, q)` to 3 decimals (cross-lag aq).
9. **The finite-length design.** Two `calc_PhiID` calls per replicate; published-mask atoms recomputed from `I_res`; the code-mask
   recomputation checked every replicate; P from phyid's `_binarize` of the four slices (T − 1 pairs); common random numbers
   (one Z per T, in the order T, replicate); N_REP = 1,000; SE = SD/√1,000.
10. **Runtime.** The median replicate takes 4, 5 and 10 ms at T = 160, 300 and 840, about 8–10 min for 72,000 replicates. The
    limit plus Genz takes about 1 min and the 10⁵ check about 15 s, plus any slow IPF calls (finding 6).
11. **Exactly tied MMI candidates** (the family's symmetry, on non-family processes, t8). The phyid-at-10⁵ check passes on two
    symmetric, reversible VAR(1) pairs. The min-bias is visible (−0.0014 nats on MMI sts) but inside 4 SE.
12. **The two-step rate check on exactly flat quantities.** It passes: ∂(2A)/∂R₀₁ on random matrices is about 10⁻¹³ against
    the 10⁻⁶ slack. MMI quantities have no kinks on the family, because the selections are strict or exact ties.
13. **Predictions against the fill's verdicts.**
    - VA, VB and VC implement (a)–(c) exactly (42 and 126 steps, "rise" = step > 0, per-SD > 1). The recomputed counts are
      cross-checked against the tables.
    - SD_R1 = 0.0284 and SD_Q = 0.1957 are B22 (d)'s values (`aligned_directed_tables.md` l. 27), and 6.89 = 0.1957/0.0284.
    - "4.7 for the Gaussian atom" is the paper's figure (4.66).
    - The fill's Gaussian values are correct: S at the operating point, 2S − C = 1.2588, and the table's 2S − C at q = 0.25.
14. **Fill mechanics.** All 16 replacement anchors occur once in the current tree. The synthetic runs (arbitrary numbers, three
    scenarios) end READY: Introduction through Methods 6,999 words (limit 7,000), check_numbers flagged 12, check_cells 0,
    table cell counts OK, no process labels or placeholders, and counts 56 = MET + PART + MISS. The outcome entry, S19 rows,
    S20 row and S3 table are well formed, apart from findings 5, 8, 9 and 10.
15. **Sources.**
    - Luppi 2022 (pp. 3, 14): the discretised replication, mean-binarised, plug-in.
    - Luppi 2023: p. 11 "emergence capacity"; p. 12 CCS, plug-in, mean-binarised BOLD, the toolbox, the HRF deconvolution.
    - Ince 2017, Definition 2 (p. 13): the three pairwise marginals.
    - Ince 2017, Tables 6, 8–11 and 13 agree with the self-test's values at their printed precision.
