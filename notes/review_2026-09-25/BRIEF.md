# Brief: error-only read of the finished paper (25 September 2026)

You are an independent checker for a methods paper that is about to be typeset, posted to bioRxiv and submitted to PLOS Computational Biology (Methods article). The analysis, the interpretation and the wording choices are frozen. Your only job is to find **outright errors**. You are the last reader before typesetting, so be exhaustive within that scope and quiet outside it.

## The material

Repository (a git clone at commit ddae618, working tree clean):
`<a clone of the repository at ddae618>`

Do not edit, commit or push anything in that repository. Write only in
`<the checker's folder>`.

Read every line of these files, in this order:

1. `manuscript/draft_v2.md`: the paper, including the title, Abstract, Author summary, Introduction, Results, Discussion, Materials and methods, the statements, References and the Supporting-information captions. Tables 1–3 and the six figure captions are inline, each after the paragraph that first cites it.
2. `manuscript/figures/captions_v2.md`: the caption strings the figure script uses. Compare each with its caption in the paper.
3. The six figures `manuscript/figures/fig1_v2_scope_map.png` … `fig6_v2_lag_dependence.png`. Open them with the Read tool and compare panel letters, axis labels, legends and annotated values with the captions and the text.
4. `manuscript/si/S1_Text.md`, `S2_Text.md`, `S3_Text.md`, `S4_Text.md`, `S5_Text.md`.
5. `manuscript/supplementary.md`: S1 to S20 Table.

Several paragraphs in these files are single lines longer than 2,000 characters, and the Read tool cuts such lines off. Read the reading copies in `<the checker's folder>/wrapped/` instead. Each line there starts with its original line number, as `[123]`. A long line continues on lines marked `[123+]`. Cite the original line numbers. When you need the exact characters of a quote, copy them from the repository file.

Supporting files you may consult as evidence:

- `manuscript/main_text_numbers.csv`: every number of the main text, one row per occurrence, with its source file and a line locator.
- The result files under `results/` and `notes/review_results/` (CSV, `*_tables.md`, logs).
- `notes/review_2026-09-24/checks/derived_r17.out`: the derived numbers such as ratios, Fieller intervals and leave-one-out values.
- `manuscript/analysis_record.md`: the dated record. The paper cites its entries by their titles in quotes.
- `CLAUDE.md`: the project's state.

## What to report

Report only these four kinds of problem.

**T: text errors.**
- Typos and spelling.
- Grammar that is wrong, such as a missing or doubled word, broken agreement, or a sentence that does not parse.
- Wrong or inconsistent symbols, such as r₁ written as r1 in one place, a wrong subscript, a minus sign written as a hyphen in a number, or unbalanced brackets.
- Inconsistent spelling of the same term across files.
- Markdown that will not render as intended, such as a table row with the wrong number of cells, or broken emphasis.

**N: numbers.**
- A number that does not match its source file.
- A rounding error at the printed precision.
- A sign error.
- An interval that does not contain its point estimate, or whose endpoints are swapped.
- A count or percentage that does not match its parts (for example, the S19 Table tally of 52 predictions = 25 met + 13 partly + 14 missed + 0 not evaluable must match the rows).
- A total that does not add up.

The main text's numbers are indexed in `main_text_numbers.csv` and are being re-checked mechanically in a separate pass, so do not re-verify that file row by row. Spend your number effort on three things:
- the numbers of the SI, checked against the files they cite;
- every quantity that appears in more than one place (main text vs SI vs tables vs captions vs figures): it must carry the same value, sign and precision everywhere, or a stated reason for differing;
- any main-text number that looks wrong on reading.

**X: cross-references.** A reference that points to something that does not exist or does not say what is claimed. This covers:
- a Fig, Table, S Table or S Text reference, including its section (§) numbers;
- an equation reference;
- "record, '<entry title>'": the title must match a heading in `analysis_record.md`;
- a citation (author and year) with no reference-list entry, or with the wrong year;
- a reference-list entry never cited in the main text.

Also check that:
- the figures and tables are first cited in ascending order;
- each table and figure caption follows the paragraph of its first citation;
- every S item cited exists and appears in the Supporting-information captions;
- every S item listed there exists in the SI files.

**C: contradictions.**
- The same quantity with two different values in two places.
- A count stated inconsistently, such as the number of subjects, runs, windows, regions, pairs, predictions, sign-flip assignments or table rows.
- A method or setting described two different ways, such as a window length, filter band, seed, lag or estimator.
- Two statements that cannot both be true.

If you are unsure, report the item under **U: uncertain**, with your reasoning, and do not report it as an error.

## Not in scope: do not report

- Interpretation, framing, emphasis or strength of claims.
- Whether a conclusion follows from the evidence.
- New analyses, extra citations, reorganisation, length, or style preferences where the existing text is correct and clear.

A sentence that is correct and parses is out of scope even if you would have written it differently.

These deliberate choices are not errors:

- **Citation form.** Citations are author–year for the preprint. The numbered form is made at submission.
- **[TK] placeholders.** These await the co-authors, the data owner's reply or the final run: affiliations, co-authors, the ethics reference number, funding statements, contributions, competing interests, the sentence about the final run, and the acknowledgments.
- **Pre-submission leftovers.** The line "Manuscript for co-author review; not for citation or distribution." stays until the co-author review. Funding, Competing interests, Data and code availability and Author contributions stay in the file and move to the submission system at submission.
- **SI packaging.** The SI is five S Text files plus one file holding S1–S20 Table. They are split into separate files at submission.
- **Nichols et al. 2017.** It is cited only in S4 Text, and its reference entry is in S4 Text.
- **Caption labels.** They are "Fig N." and "Table N."; in-text references are "Fig N" and "Table N".
- **Labels and paths.** The main text carries no computation label (B1–B24) and no file path, except in the section Data and code availability; the SI may carry both. A computation label or a file path in the main text outside that section *is* an error. Report it.
- **Process labels.** No manuscript file carries a process label (round, stage, bundle, session or writer/planner names); dated descriptions replace them, as defined in S5 Text §5. Such a label in any file listed under "The material" *is* an error. Report it.
- **Notation.** It is: regional r₁ (a region's lag-1 autocorrelation in a window), whole-brain r₁ (the mean of regional r₁ over regions) and pair r₁ (the mean of a pair's two lag-1 correlations). The phrase "pair-level a" is withdrawn, so any occurrence *is* an error. Report it.
- **Fig 5c legend.** Its placement is already scheduled for a fix. Do not report it.

## Rules

- **No analysis scripts.** Do not run anything under `scripts/` or any analysis script under `notes/`: they need subject data that is not here, and no analysis is re-run in this check.
- **Small checks only.** You may run small Python checks that read committed files, such as CSV, `*_tables.md`, `.out`, `.log`, `.npy` and `.pkl` under `results/` and `notes/review_results/`. Use `<the pinned environment's Python>`. Also allowed: `notes/review_2026-09-24/checks/derived_r17.py`, which reads only committed result files; run it from the repository root.
- **No web.** Do not use the web.
- **Write as you go.** After each file, append that file's findings to `findings.md` in the output folder, so nothing is lost if you run long.

## Output

Write `<the checker's folder>/findings.md`. Give each finding these fields:

- **ID**: T1, N1, X1, C1, U1 and so on.
- **Location**: the file and line number.
- **Quote**: the exact current text, verbatim, long enough to be unique in the file.
- **Problem**: what is wrong, in one or two sentences.
- **Evidence**: for N and C, the source file, line and the value found there; for X, what exists instead.
- **Fix**: the exact replacement text, changing as little as possible. For a main-text fix, say whether it changes the word count.

End the file with a **Coverage** section:
- the files read in full;
- the figures inspected;
- which SI numbers you checked against which files;
- which cross-reference classes you checked exhaustively and which by sample;
- anything you could not check and why.

Your final message must be only two things: the count of findings per class, and the path of `findings.md`. Do not repeat the findings in the final message.
