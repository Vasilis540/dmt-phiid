The recomputation of the primary contrast (whole-brain mean MMI-sts) and of the whole-brain r₁ contrast in GNU Octave,
3 October 2026 (record, "The primary and the r₁ contrasts recomputed in GNU Octave"; S5 Text §4).
`octave_crosscheck.m`: the script, written by the AI system, which calls none of the repository's Python code; run by
V.S. on his computer in GNU Octave 8.4.0 on the released series. `octave_crosscheck.out`: what the run printed.
`octave_crosscheck_windows.csv`: r₁ and sts of every subject, run (1 = DMT, 2 = placebo) and window.
`text_replacements_2026-10-03_octave.json`: the replacements that name the recomputation in the text. `checks/`: the
outputs of the checks at the text commit. To run it: `octave --no-gui octave_crosscheck.m` after setting the path of
the time-series file at the top of the script or in the environment variable `DMT_TS_FILE`.
