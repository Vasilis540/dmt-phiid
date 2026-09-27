# Layout check of main.pdf and SI.pdf (commit c25a310-dirty)

The preview PDFs checked here were typeset outside the repository (pandoc and XeLaTeX) from the text of c25a310 with the pending edits of the outputs commit applied; the faults below are faults of that typesetting, not of the manuscript files.

**Counts:** main.pdf: 6 faults. SI.pdf: 14 faults.

**Checked:**
- `main.pdf`: 25 pages, A4 portrait, with line numbers.
- `SI.pdf`: 132 pages; pp. 1–48 portrait, pp. 49–132 landscape.
- Markdown line numbers refer to the repository files (`draft_v2.md`, `si/S*_Text.md`, `supplementary.md`), not to the pandoc inputs `main.md` and `SI.md`.

**Positions:** "y" is measured in points from the top of the page. On portrait pages (842 pt tall) the text block ends near y 777; on landscape pages (595 pt tall) it ends near y 530.

**Counting rule:** one fault is one defect with one cause.
- Page-layout events count once per place: a stranded heading, a blank page, a split caption.
- A glyph or markup defect that recurs counts once, with every place listed.

## Summary

| PDF | faults | critical | moderate | minor |
|---|---|---|---|---|
| main.pdf | 6 | 0 | 2 | 4 |
| SI.pdf | 14 | 1 | 9 | 4 |

The worst fault is on SI.pdf p. 120. The first row of S20 Table A is taller than a page, and about 39 lines of its last column fall below the page edge, where no one can see them. The same row also causes S2–S4:
- p. 119 is blank;
- the heading "Table A. Studies" is left alone on p. 118;
- the table header is printed twice on p. 120.

## main.pdf

**M1 (moderate). Table 1's caption is separated from its table (pp. 4–5).**
- **Where:** foot of p. 4, lines 148–152 (y 701 to the end of the text block): "Table 1. The sixteen whole-brain atoms under MMI, observed and AR(1)-substituted. …".
- **What is wrong:** only the caption's last words, "the table." (line 153), are on p. 5, directly above the table body (y 90–313).
- **Source:** `draft_v2.md` line 61 (caption) and lines 63–81 (table).

**M2 (minor). Table 3's caption starts a page before its table (pp. 10–11).**
- **Where:** p. 10, lines 315–326 (from y 592 to the foot): "Table 3. The residual of the AR(1)-substituted estimate: …".
- **What is wrong:** the caption continues on p. 11 (lines 327–337) and the table follows on p. 11 (y 250–571). The title and the first half of this 23-line caption are on the page before the table.
- **Source:** `draft_v2.md` line 120 (caption) and lines 122–134 (table).

**M3 (moderate). Figures 1, 3 and 4 are shrunk so far that their lettering prints at about 3–4 pt (pp. 4, 7, 8).**
The figure files are much wider than the 465-pt text block, so the build scales them down:

| figure | page and position | drawn width | printed at | lettering drawn at | lettering printed at |
|---|---|---|---|---|---|
| Fig 1 | p. 4, y 128–272 | 1024.8 pt | 45 % | 6.5–9 pt | 2.9–4.1 pt |
| Fig 3 | p. 7, y 326–482 | 804 pt | 58 % | 6.5–9 pt | 3.8–5.2 pt |
| Fig 4 | p. 8, y 421–564 | 925 pt | 50 % | 6.5–9 pt | 3.4–4.5 pt |

- In Fig 1 this hits the ticks, the colour bars, the legend, the contour labels "0.25" and "0.5", and the note "black contours: …". In Fig 4 it hits the legend "Vis (17) …" and the ticks.
- This is too small to read in print; body text is 10.95 pt and the line numbers are 5.2 pt.
- Figs 2, 5 and 6 print at 86 %, 67 % and 78 %, with lettering of 4.7–8.2 pt; Fig 5 is borderline.
- **Source:** the figures are inserted before the captions at `draft_v2.md` lines 55, 104 and 110. The files are `fig1_v2_scope_map.pdf`, `fig3_v2_per_subject.pdf` and `fig4_v2_regional.pdf`.

**M4 (minor). The "Author summary" heading has a single line under it at the foot of p. 1.**
- **Where:** lines 31–32 (y 723 to the end of the text block). Under the heading is only "Functional brain imaging asks how regions carry information together, not only which are active. A widely"; the section continues on p. 2.
- **Source:** `draft_v2.md` lines 17–19.

**M5 (minor). The last page holds a single line (p. 25).**
- **Where:** top of p. 25, line 853: "and the scope map's reading of each, with the inputs of that reading."
- **What is wrong:** this is the last line of the S20 Table caption, left alone on the final page (line 852 is at the foot of p. 24). The rest of p. 25 is blank.
- **Source:** `draft_v2.md` line 406.

**M6 (minor). A URL in the reference list is letter-spaced (p. 21, line 713).**
- **Where:** "https://github.com/Imperial-MIND-", in the reference "Imperial-MIND-lab (2026). phyid …".
- **What is wrong:** about 1.3 pt was added between every character to fill the justified line, so it reads "h t t p s : / / g i t h u b …".
- Milder stretching (0.5–0.6 pt per character) is on line 714 (its continuation), line 636 on p. 19 (the Vasilis540/dmt-phiid URL) and line 773 on p. 22 (the brb3.71352 DOI).
- **Source:** `draft_v2.md` line 298; the milder cases come from lines 246 and 332.

## SI.pdf

**S1 (critical). Row 1 of S20 Table A runs off the bottom of p. 120 and its text is lost.**
- **Where:** p. 120, landscape, last column ("scope-map reading") of row 1 (Luppi et al. 2022).
- **What is wrong:**
  - A longtable row cannot break across pages, and this one is taller than a page.
  - The cell runs through the bottom margin; its last visible words are "its correlations with", at the page edge.
  - About 39 more lines are outside the page box, still in the PDF but invisible. They run from "the macroscale maps were 0.09, 0.01, 0.17, 0.21, 0.26 and −0.16 (only glycolytic index, ρ = 0.26, spin p = 0.028, significant) against 0.40, …" to "… is not tested in either paper."
- **Source:** `supplementary.md` line 1658 (last cell).

**S2 (moderate). The S20 Table A header is printed twice (p. 120).**
- **Where:** top of p. 120. The header row "# | study | data (N, TR) | … | scope-map reading (see Table B for the inputs)" appears twice, one copy under the other.
- **Source:** `supplementary.md` line 1656. This is a side effect of S1.

**S3 (moderate). p. 119 is blank.**
- **What is wrong:** the page is empty apart from the folio and the footer. These print on the opposite long edge from every other landscape page. The page comes from S1.
- **Source:** between `supplementary.md` lines 1654 and 1658.

**S4 (moderate). The "Table A. Studies" heading is separated from its table (p. 118).**
- **Where:** the heading sits at y ≈ 185 of 595; the lower two-thirds of the page is empty.
- **What is wrong:** the table starts on p. 120, after the blank p. 119.
- **Source:** `supplementary.md` line 1654. This is also a consequence of S1.

**S5 (moderate). Heading stranded at the foot of p. 38.**
- **Where:** last line, y ≈ 751 of 842: "A. Acquisition" (S4 Text).
- **What is wrong:** its table starts on p. 39.
- **Source:** `si/S4_Text.md` line 19.

**S6 (moderate). Heading stranded at the foot of p. 39.**
- **Where:** last line, y ≈ 760: "S. Statistical modelling and inference".
- **What is wrong:** its table starts on p. 40.
- **Source:** `si/S4_Text.md` line 44.

**S7 (moderate). Heading stranded at the foot of p. 102.**
- **Where:** last line, y ≈ 489 of 595: the bold heading "a = 0.8632" in part (a) of the S18 Table.
- **What is wrong:** its table starts on p. 103.
- **Source:** `supplementary.md` line 1368.

**S8 (minor). A table label is separated from its table (p. 103).**
- **Where:** last line, y ≈ 477: "(a5) shared slow component at a = 0.8632 (λ = |q|, …): base residual −0.02942, …".
- **What is wrong:** its table is at the top of p. 104.
- **Source:** `supplementary.md` line 1402 (table at lines 1404–1409).

**S9 (minor). Nearly blank page with one table row (p. 53).**
- **What is wrong:** the page holds only the last row of the S3 Table's ts_demean list ("RH_Default_pCunPCC_1 | 98 | 7 | −0.114772 | 0.00781 | 12") under a repeated header, plus the one-line note "Common to both variants: …". The rest is blank.
- **Source:** `supplementary.md` lines 78 and 80.

**S10 (minor). Nearly blank page with one table row (p. 71).**
- **What is wrong:** the page holds only the last row of the S12 Table ("expectation, W = 60, pure autocorrelation change …") under a repeated header. The rest is blank.
- **Source:** `supplementary.md` line 321.

**S11 (moderate). "file:line" is typeset as a hyperlink (pp. 77–100).**
- **Where:** the S17 Table's last-column header, "quoted in the text of 23 September 2026 (file:line at 90690f4)", which repeats on all 24 pages of the table.
- **What is wrong:** pandoc treated "file:line" as a bare URI. It prints in dark-blue link colour and is a live link to "file:line".
- **Source:** `supplementary.md` line 380.

**S12 (moderate). Underscores in 16 S17 Table rows are swallowed as italics (pp. 95–96).**
- **Where:** the "quantity" column of these rows:
  - ts_gsr rows 786, 788, 792, 794, 798, 800, 804, 806;
  - ts_demean rows 810, 812, 816, 818, 822, 824, 828, 830.
- **What is wrong:** the two underscores in "c̄_rej … ts_gsr" and "c̄_pre … ts_demean" became emphasis markers. The text between them is italic and both underscores are gone. For example, "c̄_rej (nats) (code mask) ts_gsr W60" prints as "c̄rej (nats) (code mask) tsgsr W60", with "rej (nats) (code mask) ts" in italics.
- **Source:** `supplementary.md` lines 1167, 1169, 1173, 1175, 1179, 1181, 1185, 1187, 1191, 1193, 1197, 1199, 1203, 1205, 1209, 1211.

**S13 (moderate). Subscripts print as raw "_" markup in 7 places.**
The build turns `x_y` into a subscript elsewhere (a_x, s_pre, δ_run, σ_q). It misses a subscript whose base has an accent (c̄, β̄), is a non-ASCII letter (ā), has a superscript (σ²) or is a closing bracket. These print literally:

| page | where | printed | source |
|---|---|---|---|
| 19–20 | S3 Text §5, CCS decomposition paragraph (last 4 lines of p. 19, top of p. 20) | "c̄_rej" (3×) and "c̄_pre"; the same sentence prints s_pre correctly | `si/S3_Text.md` 219 |
| 22 | S3 Text §6, y ≈ 197–233 | "σ²_{y,w}" with the braces, and "ā_y" (2×) | `si/S3_Text.md` 229, 231 |
| 30 | S3 Text §7, y ≈ 491 | "β̄_post" | `si/S3_Text.md` 321 |
| 58 | S8 Table source note, y ≈ 122 of 595 | "(post − pre)_DMT − (post − pre)_PCB" | `supplementary.md` 144 |
| 64 | S10 Table note, y ≈ 366 | "β̄_post" | `supplementary.md` 218 |
| 77 | S17 Table note, y ≈ 361 | "c̄_pre Δs" | `supplementary.md` 378 |
| 107 | S18 Table part (e), y ≈ 178 | "β̄_post" | `supplementary.md` 1503 |

Uncertain, not counted: "√(rel_res × rel_CCS)" on p. 28 (`si/S3_Text.md` 286) may also be meant as subscripts.

**S14 (minor). β̄ is printed with its bar displaced to the right (5 places).**
- **What is wrong:** the combining macron after β sits about 2.3–2.8 pt right of the letter's centre and hangs off its top-right corner, so the symbol reads "β¯". The other accented letters (c̄, q̂, P̂, q̄) are placed within 0.5 pt of centre. The likely cause is that Liberation Serif has no mark-attachment data for β.
- **Where:**

| page | where | occurrences | source |
|---|---|---|---|
| 22 | y ≈ 347 | 1 | `si/S3_Text.md` 233 |
| 30 | y ≈ 475 and 491 | 2 | `si/S3_Text.md` 321 |
| 61 | y ≈ 289, S9 Table controls row (ii), "N(6β̄, (h·6β̄)²) … N(β̄/5, (h·β̄/5)²)" | 4 | `supplementary.md` 181 |
| 64 | y ≈ 366 | 2 | `supplementary.md` 218 |
| 107 | y ≈ 178 | 2 | `supplementary.md` 1503 |

## Checked and not counted (cosmetic or by design)

**main.pdf**
- **Line numbering works.** It runs continuously from 1 to 853, with no gaps, repeats or restarts. As usual with the lineno package, a few numbers label no text: line 4 (the empty author line under the title) and one or two numbers beside each figure (121, 154, 210, 250–251, 279, 356–357). Tables are not line-numbered.
- **Table 2 on p. 6:** in the row "DiD, FD-residualised", "13/" ends a line and "14" starts the next, in both columns. The break falls at the `\allowbreak` the build inserts, and the reading is unchanged.
- **p. 19, line 628:** the URL breaks inside "DMT" (".../singlesp/DM" then "T_NCT"). This is normal xurl behaviour.
- **Captions of Fig 2 and Fig 5** continue onto the next page, but each title stays directly under its figure.

**SI.pdf**
- **Single table rows carried onto the next page** under a repeated header, on pages that otherwise have content: pp. 19, 34, 61, 66, 68 and 107.
- **Short text tails of 3–5 lines** end up alone on pp. 59, 69 and 73, because each S Table starts on a new page.
- **Lead-in sentences ending in ":"** sit at the foot of pp. 11 and 32, with their tables on the next page.
- **The S17 Table is set at 6 pt** (`\tiny`) throughout. It is small but legible, and it is the size the build chose.
- **Partly empty pages by design:** pp. 37, 41, 48, 49 and others, because each S Text and S Table starts a new page. The landscape footer running along the long edge is the pdflscape convention.
- **PDF metadata:** SI.pdf has no Title (main.pdf has one). This is not visible on any page.

**Both PDFs**
- **Glyphs:** no missing glyphs.
  - Neither XeLaTeX log has a "Missing character" or "Overfull box" entry.
  - Every non-ASCII character in the input appears in the PDF in a font that contains it: r₁, 10⁻¹⁶ (the "⁻" comes from DejaVu Serif and sits level with the digits), the Greek letters, −, ×, ≤, ≥, ±, →, …, √, ≈, ≡, ≠, ∂, ∈, ∝, ∪, ≻ and ᵀ.
  - The one count difference, one ρ fewer in the SI text, is the ρ lost off the page in S1.
- **Margins and overlaps:** no text runs past the margins beyond 2 pt of ink on final punctuation, and no characters overlap outside figure artwork.
- **Raw markup:** none apart from S11–S13.
- **Tables:** every markdown table is typeset:
  - `draft_v2.md` has 3 tables and main.pdf has 3.
  - `si/S1`–`S5_Text.md` have 0 + 0 + 16 + 6 + 0 and `supplementary.md` has 40, for 62; SI.pdf has 62.
  - The last row of every one of the 65 tables was found in the PDF.
  - Every multi-page table repeats its header, no header is left without its body at a page break, and no table runs off the side of the page.
- **SI table of contents:** at depth 2 it has 50 entries: S1–S5 Text with their sections, "Supplementary tables", and S1–S20 Table. All are present, and every page number matches the page where the heading is printed.

## Coverage

**main.pdf: all pages (1–25)**
- Rendered at 70 dpi and viewed twice.
- At 110 dpi: pp. 1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16.
- At 150 dpi: pp. 4, 19, 21, 22.
- At 300 dpi: p. 16.
- Fig 1's own file was also rendered at 100 dpi.

**SI.pdf: all pages (1–132)**
- Rendered at 70 dpi; the landscape pages were viewed rotated.
- Pages 1–79 and 100–132 were viewed twice; pages 80–99 once.
- At 110 dpi: pp. 34, 58, 65, 66, 77, 78, and all of p. 120.
- At 150 dpi: p. 2 (table of contents).
- At 200 dpi: p. 95.
- At 300–400 dpi: accents and superscripts on pp. 11, 13, 19, 22, 30, 61, 64.

**Machine checks on all 157 pages**
- **Text and positions:** `pdftotext` layout and word boxes; pdfplumber position, font and size for every character.
- **Position checks:** margin overrun, text outside the page box, overlapping characters.
- **Characters:** every non-ASCII character counted against the pandoc input, with its font; accent placement.
- **main.pdf structure:** line-number continuity and alignment; where each caption sits relative to its figure or table.
- **Page breaks:** stranded headings and repeated lines on a page.
- **Tables:** markdown tables counted against the LaTeX longtables, and each table's last row found in the PDF.
- **Links:** every `\url` target in the LaTeX, and the PDF link annotations.
- **Table of contents:** the SI `.toc` checked against the printed contents and the heading pages.
- **Build logs:** both XeLaTeX logs read.
