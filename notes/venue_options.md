# Venue and preprint options for `manuscript/draft_v2.md`

Written 15 September 2026 (finalisation pass). Every limit and fee below was read from the journal's own author pages or from Scimago on that date and can change; re-check before submission. Quartiles are Scimago Journal Rank 2025 quartiles for the subject categories named.

## What the draft is, in the terms the journals use

Main text about 12,900 words excluding tables and references (Introduction about 750, Methods about 4,200, Results about 4,900, Discussion about 2,000); structured abstract of about 350 words; 5 figures and 6 main-text tables; 24 references; a supplement of eight tables (`supplementary.md`) and a COBIDAS checklist (`supplementary_cobidas.md`); code and results in a public repository with a pinned environment; data not redistributed (the source authors' release, cited). The paper is a methods account (an estimator's dependence on lag-1 autocorrelation, with an analytic family, a residual diagnostic and a bias simulation) tested on a secondary analysis of one open pharmacological fMRI dataset. It is not a clinical paper.

## Three Q1 candidates

### 1. NeuroImage (Elsevier)

- Quartile: Q1 in Cognitive Neuroscience and in Neurology (SJR 2025 1.925).
- Limits: no word or figure limit for regular research papers; abstract at most 250 words; 1–7 keywords; Highlights required (3–5 bullets of at most 85 characters each); graphical abstract encouraged. Technical Notes are about 3,000 words and at most 5 figures, which the draft is not.
- Fee: fully open access; APC USD 3,540 (CC BY, CC BY-NC or CC BY-NC-ND).
- Preprint policy: sharing preprints "will not count as prior publication".
- Other requirements that touch the draft: the ethics statement must give "the date and reference number of any ethical approval(s) obtained", so the REC reference number [TK] has to be filled before submission; research data must be deposited or a statement given for why not (the Data and code availability section covers this: the derivatives are the source authors' release, cited, and the code is public).
- Fit of the current draft: the text fits as it stands apart from the abstract, which has to be cut from about 350 to 250 words and unstructured (the journal does not use labelled sections); the Highlights have to be written.
- One-sentence fit: the natural home for a paper whose subject is what an fMRI estimator measures, read by the people who run ΦID on BOLD.

### 2. Network Neuroscience (MIT Press)

- Quartile: Q1 in Neuroscience (miscellaneous), Applied Mathematics, Artificial Intelligence and Computer Science Applications (SJR 2025 1.450).
- Limits: Research and Methods articles at most about 6,000 words total excluding references; Introduction at most 800 words; Discussion at most 1,600 words; abstract at most 200 words; a required Author Summary of at most 125 words; at most 6 display items (figures plus tables) for Research articles.
- Fee: open access, CC BY; APC USD 2,250, billed on acceptance.
- Preprint policy: pre-submission posting on arXiv or bioRxiv "is encouraged".
- Other requirements: for Methods articles, data and code availability is "an absolute requirement" (met, code side; the data are the source authors' public release).
- Fit of the current draft: does not fit as it stands. The main text is more than twice the limit, the Discussion is about 400 words over, the abstract has to fall from about 350 to 200 words, and 11 display items have to become 6 (for example Figures 1–5 plus one table, with Tables 2–6 moved to the supplement). Cutting to 6,000 words means moving most of Methods (the closed-form atoms, the bias simulations, the family checks) and the secondary results (Results 4–5) to the supplement; the argument survives, the paper becomes a short report with a long supplement.
- One-sentence fit: the journal in which the ΦID-on-BOLD literature the paper addresses is partly published (Gatica et al., 2024), so the readers who most need the diagnostic are there, at the price of a heavy cut.

### 3. PLOS Computational Biology

- Quartile: Q1 in Computational Theory and Mathematics, Modeling and Simulation, Genetics, Molecular Biology and Ecology; Q2 in Cellular and Molecular Neuroscience (SJR 2025 1.466).
- Limits: no restriction on main-text length; abstract at most 300 words; a required non-technical Author Summary of 150–200 words; no stated figure or table limit. Research Article or Methods article types.
- Fee: open access, CC BY; publication fee USD 3,165 (as listed by PLOS, updated January 2025).
- Preprint policy: preprints encouraged; authors can opt in to have PLOS post the manuscript to bioRxiv at initial submission.
- Other requirements: all author-generated code must be public without restriction (met); data must be available (the source authors' release, cited).
- Fit of the current draft: fits as it stands except the abstract (about 350 to 300 words; PLOS accepts an unstructured abstract) and the Author Summary, which has to be written; the Methods article type suits a paper whose contribution is the diagnostic and the map. The null-model paper the draft cites (Liardi et al., 2025) is published there.
- One-sentence fit: the venue for the estimator-theory reading of the paper, where the analytic family and the null models are the contribution and the DMT dataset is the test case.

### Considered and set aside

Imaging Neuroscience (MIT Press; the journal the former NeuroImage editorial board founded; APC USD 1,600; preprints encouraged; no word limit) is the closest fit by scope and the cheapest, but Scimago lists it as Q2 in every category for 2025 (SJR 0.791; coverage from 2023), so it is not a Q1 candidate on today's numbers; it would be the first choice if the quartile constraint were dropped.

## Preprint server

The paper is a methods and basic-neuroscience paper on human data, not a clinical study, so both servers are in scope; bioRxiv asks that clinical papers go to medRxiv, which does not apply here.

### bioRxiv (Neuroscience category)

- What it needs: a single PDF with text, figures and tables embedded (a Word file with separate figure files is also accepted; LaTeX must be converted to PDF first); one subject category (Neuroscience); the article type New Results; a licence choice (CC BY, CC BY-NC, CC BY-ND, CC BY-NC-ND, CC0 or no reuse); the statement that all authors consented to deposition; the ethics and competing-interests statements as in the manuscript. Screening is for content, not peer review; posting usually within 72 hours, longer at weekends; a DOI is assigned; revised versions can be posted at any time before journal publication; full-text HTML is generated within about 48 hours; direct transfer to participating journals (B2J) is offered, and PLOS Computational Biology posts to bioRxiv on the author's behalf at submission if asked.
- Constraint: a paper already published in a journal cannot be posted, so the preprint has to go up before or during submission.
- Why it suits this paper: it is where secondary analyses of the same DMT fMRI data have been posted (for example "Brain substates induced by DMT relate to sympathetic output and meaningfulness of the experience", bioRxiv 10.1101/2024.02.14.580356, a secondary analysis of the same 14-subject DMT fMRI data from the data collectors' group), where the NeuroImage and Network Neuroscience readership looks, and it needs no endorsement.

### arXiv (q-bio.NC, Neurons and Cognition)

- What it needs: a registered account and, for a first submission to q-bio, an endorsement from an existing arXiv author in that domain (someone who has posted several q-bio papers in the last three months to five years; the endorsement request link is generated when the submission is started; an institutional e-mail address speeds the check); the source files if the PDF was produced from LaTeX (arXiv does not accept a PDF made from TeX source), otherwise a PDF; title, abstract and author metadata typed into the form; a licence grant (arXiv's non-exclusive licence or a CC licence); a category (q-bio.NC, with optional cross-lists such as physics.data-an or stat.ME for the estimator content). Submissions received by 14:00 US Eastern time are announced at 20:00 the same day, after moderation; versions can be replaced; a DOI is assigned.
- Why it might suit this paper: the information-decomposition literature the paper argues with (Mediano et al., 2021; Varley, 2024; Faes et al., 2025; Liardi et al., 2025) circulates on arXiv, and cross-listing reaches the information-theory readership.
- Why it is second choice: the endorsement step for a first q-bio submission, and the neuroimaging readership of the target journals reads bioRxiv.

### Recommendation

Post to bioRxiv, Neuroscience, New Results, under CC BY (the licence every candidate journal publishes under), on the day the journal submission goes in, with the [TK] items resolved first (a preprint with "[TK]" in the ethics statement is not acceptable). If PLOS Computational Biology is chosen, let PLOS post it. A later arXiv copy (q-bio.NC, cross-listed) is optional and needs an endorser.
