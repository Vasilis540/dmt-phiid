# Reproduction checks of the run_all.sh outputs, 16 Sep 2026 (V.S., local machine, .venv)

Working tree at d145e1c after the section-6 rerun (`/tmp/run_tail.sh`, log `results/run_all_tail.log`), with the
sections 0–5 outputs of the run started 15 Sep 2026 10:25 UTC also present, uncommitted. Each .log is the terminal
output of the command in the file of the same number; the terminal's own echo of the heredoc is omitted.

0. The rerun's status: PID 4738 gone, log ends "=== all done in 51 min".
1. `git diff -I 'git' --stat`: the files whose changes are not all on lines containing "git" (SHA headers).
2. Every modified table compared with the committed version: CSVs parsed (header comments skipped) and compared
   numerically; text files by unified diff. The "non-numeric column differs" flags on `survives`, `note` and
   `condition` are empty cells compared with themselves (NaN ≠ NaN in pandas); check 3 confirms it for `survives`.
3. Three follow-ups: the `survives` flag; the 84 `nonstat_step_ar` rows against the 2,000-run file
   `results/nonstat_ar_step/bias_check_nonstat.csv` (different values, headers `n_runs=20000 git=2151be0` new,
   `git=18ad8b4` old); participant codes in the regenerated alignment report (none).
4. The regenerated outputs stashed, bundle 15 pulled (fast-forward d145e1c..0159fdf) and pushed.
