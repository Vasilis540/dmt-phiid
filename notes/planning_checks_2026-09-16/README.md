# Planning checks, 16 Sep 2026 (round-7 commission: the cross-lag budget)

Synthetic checks and arithmetic from the planning session. No DMT data were touched: that session held only
the public clone at d145e1c, without external/. Scripts are kept as run; the reviewer scripts' sys.path lines
point at that session's scratch folders and need editing to re-run here. Each .log is the printed output of
the .py of the same name.

- planning_chat/: run before any value from the null's generator had been seen. check1_lookalike (the
  shared-slow-component formula; the VAR(1) equivalence of the worked example), check2_budget,
  check2b_budget_debug, check2c_case1_digits (the budget identity on synthetic AR(1) windows),
  check3_signsel (sign-selection bias on a toy AR(1)). Not the null's generator.
- reviewer/: an adversarial reviewer subagent's checks, re-run by the planning chat to record exact values.
  v_null_periodic, v_null_qshape, v_mechanisms and v_means_unshared use the filter family and gen() of
  notes/review_v2_residual_null.py (placebo fit, heterogeneity 0.5, T = 840, q drawn ad hoc, not solved
  to the data). v_aq_weights is synthetic AR(1); v_needed_dev and v_slope_q are analytic (B8 family,
  closed-form atoms).
- reproduction_checks/: V.S.'s comparison of the regenerated run_all.sh outputs (sections 0–5 of 15 Sep, section 6 of
  16 Sep at d145e1c) with the committed files, commands and terminal outputs; see its README.
- audit/: audit_bundle15.py, the arithmetic behind items (i)–(iv) of the round-7 correction note, on the
  numbers printed in crosslag_deviation_tables.md at 9a19b10 (bundle 15) and in the reviewer logs. Written
  after the 10:32 UTC outcome of 16 Sep had been seen.

Sequence, as stated in the pre-run entry: the budget, the run-level sign and the thresholds were drafted
before the planning session had seen any value from the null's generator; the mixture configuration, the
controls, the δ_pool relabelling, the attribution clause and the branch ordering were added after the
reviewer's values were seen; the correction note and rule (e) after the 10:32 outcome.
