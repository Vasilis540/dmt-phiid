#!/usr/bin/env bash
# b26_commit.sh — commits the outputs of B26 exactly as the run wrote them, and pushes that commit.
#
# Run it as yourself, on the laptop the run was made on:   bash ~/Downloads/b26_commit.sh
# It checks everything first and changes nothing unless every check holds:
#   - the repository is on master, and master and origin/master are at d5a65bd;
#   - nothing is staged, and `git status` lists exactly the 99 files the run left (96 modified, 3 new) and nothing else;
#   - each of the 99 files has the sha256 that the run's evidence recorded (checked by the planning session).
# Then it commits those 99 files and nothing else (as vilalius <sampalisvasilis@gmail.com>), checks the commit file by
# file, and pushes it. Run again after a stop, it resumes: once the commit is made it checks it again and only pushes.
set -u
REPO=/home/vilalius/dmt-phiid
BASE=d5a65bdcb2cc9d073f71829c264894937dbe1dc4
SUBJECT='B26: the outputs of its run at d5a65bd, as the run wrote them'
EXPECTED_SHA='f056c3fdb07734ce5494e7e51aa3822fd8e778f420d755f677b8b2cb9e793d55  notes/review_results/partB/positive_definite.csv
73ab5e18cccca32d545b698009d95508ece79535cd293bfcae226c6427ba35cb  notes/review_results/partB/positive_definite_run.log
b06533e8abb7277be2647a0924df37fb5e4f2bd11f1f03844803d7766a9bcee1  notes/review_results/partB/positive_definite_tables.md
2b32339d624320bd75996d2f9a592d1556ce5403a802ad524095fb78e3613243  manuscript/figures/captions_v2.md
291bc0ab9f880d5fca75bb51b671b211f632611e5b371a2c3cd689c84324faf3  manuscript/figures/fig1_v2_scope_map.pdf
1c137503097c90669ca1f9dd10ebf45f068a1c32465833bf8fe040142844ea3d  manuscript/figures/fig2_v2_atoms_observed_substituted.pdf
b2acc9912ec95f20287ac72c426fab9c3c1f17d4bed2bb358c20347b34a73bcf  manuscript/figures/fig3_v2_per_subject.pdf
f3734f08f01c11d9e0f0bf1345c99fc92bef7955fefc3754b5e527e105a11f84  manuscript/figures/fig3_v2_per_subject.png
b3044774801c56b1494f9ae3925023655dd686ac22903a21ca48f1351dae5250  manuscript/figures/fig4_v2_regional.pdf
a292648044c5c5209c6fe984f3565a98dd468d597944397941efed2ae11864e8  manuscript/figures/fig5_v2_residual_diagnostic.pdf
d2a32f7566000b83336ea70e58d898859b8259043789c00297b3d469d377ac9b  manuscript/figures/fig5_v2_residual_diagnostic.png
d11eff51f6ca5dbbdd431feb713d716e72115ca96a7d11b6ace16d7272e03ecd  manuscript/figures/fig6_v2_lag_dependence.pdf
928e80cb225d35b70ae99facb6186458862cd2a631bd79cd4dd0fb5c611e2ab0  notes/review_computations_2026-09-14.md
cbe962f11eb256d2693e46d9ef11e119ee2c6a23516ba3e9d4c2005a5da9a02d  notes/review_results/inference_rows_ccs.csv
3781efa3fa626fb58e6d2c2c06c2f4bfbefe8a4bef8895190fdd6f52ac2c630f  notes/review_results/inference_rows_ccs_pub.csv
0b596216d91c3ad2c9b120465be4de039b6634df0dad21d72a83bfe389109cec  notes/review_results/inference_rows_diag.csv
a870875e24133d0dec36b3ed7f5361470aedfa46bd593bffaea915e3fca5cf37  notes/review_results/inference_rows_diag.pkl
f3d5d30fc830c7c8eef85bfa0ab77245f79d7300f0d8728e287bc3ec56a65332  notes/review_results/inference_rows_lag.csv
c132743daa63cc20db527a3d87c2479aae18ae879d822c1f0b30f300c8e8f073  notes/review_results/inference_rows_prewhiten.csv
49ec325102cca09d7acaf1e9cdf0109f8b1eb03f5d7bf2ea94f4c051d6958290  notes/review_results/inference_rows_prewhiten.pkl
6d1c83a583cf90dc7074564fbaed6082683b41a7322f72bb37499a4ee456e017  notes/review_results/logs/phiid_fast_validate.log
f645ae3bd8d9c7d7d3e91a16bc6133d283c49ceaf925fad77b51a61af7604031  notes/review_results/logs/rev_extra.log
fba74d97e17e6ff72e019502733c854a4578294087c31de8f0ff6ac71aaa75e7  notes/review_results/logs/rev_run_raw.log
d644536ca0cb13e1a04f53f172a60c2b43d13230679ccc3a1e89c9f1df8a8704  notes/review_results/logs/review_checks.log
39dfe3ea3b56f13a90dae43dc5e0ed7cbe247b94c3a894183ccf7803aadc7f66  notes/review_results/logs/review_v2_residual_null.log
ac13d5f998db864d97049e2ae0c624ac077c8b9897a37764ffaa1dc035c9a8bc  notes/review_results/logs/sts_matched_null_F1.log
d2705f4d155a55eb331e8d120687cde778da7147a88d28d3ff916ac51ec89f4d  notes/review_results/logs/sts_matched_null_F2.log
3851c3dc57f4683252795e8af17995e3f688ba3275f90421c5e927db4ada575b  notes/review_results/logs/sts_matched_null_F3.log
ded7223416eab78847e4ca0741ddb36a884c489971a0eb4c507b262597675f42  notes/review_results/partB/aligned_directed.csv
ce1e7aade1068b98272a83e3b281157161d7e27519606ef13f8266db09045c55  notes/review_results/partB/aligned_directed_run.log
088617843ba3075176f693fd1c20be1e0ca5b26e60698cd99776cada2ccc9d77  notes/review_results/partB/aligned_directed_tables.md
08d0e88f83f3d89495844dd9a639836b5dd0a9a786e1b0d1be0b3bc30f56c006  notes/review_results/partB/bandpassed_expectations.csv
647435d726811fb61ede0dadf587662b44a6a881674b465d6bfc8a5940b4392b  notes/review_results/partB/bandpassed_expectations_run.log
455451e1b7729ec5dd3c49e3fdad20e232c8a2997eb95063e0d642e392b790d5  notes/review_results/partB/bandpassed_expectations_tables.md
af192a456e7ecf87e0a1f5c86eb35c935ed7446bad983360311cf4952c6a14ea  notes/review_results/partB/bca_intervals.csv
c94bb3d31d3ebfc850d9a32ffbcea285d6eca1a69efa6c6454e882185aaada18  notes/review_results/partB/calibration.csv
9b7aaec9261c54d466eaf676555ca904ef542fb44b19020a2822fa955b347ae1  notes/review_results/partB/calibration_filtered.csv
52c33b6c8a09bd0ef1d81893cd1d5384550bff197ff57abc97c3f6c29c0ea26a  notes/review_results/partB/calibration_filtered_run.log
b959a7d13f8c310161a76079a0fdad25613942d59212d42f49d813b403fe5bf1  notes/review_results/partB/calibration_filtered_tables.md
a7e9ca03b7ed7f0f350aa471036a5a3ee0b011251fb9c67c8a08b7ef0d368102  notes/review_results/partB/calibration_run.log
2df63b03b6fcb968ae6a811999ce4d63b87df215163dda92414cbf9d1dac85ef  notes/review_results/partB/calibration_tables.md
17b8264c0cffdfa6ae2ba378c852616bf8288d20df370e9538ea160e90804db2  notes/review_results/partB/ccs_decomposition.csv
1bd30d040dae979c150f889ac620ed0f0a44ffbd163f58f6b28551a56c7d72bd  notes/review_results/partB/ccs_decomposition_run.log
c2e88a9d3939ac9ad124e553b22838f9045bea8c1a9b8898db25f071145c6838  notes/review_results/partB/ccs_decomposition_tables.md
e2766e9d76875ccef9afb46d6ef517761d8d74b37b39b290035e70a4b8560142  notes/review_results/partB/ccs_definition_check.log
4c8a01c7a1e56b56df78019ac1f0134c05f8e3488259d0ced93a01e6fa0a7329  notes/review_results/partB/ccs_pub_tables.md
c57f66ab15934d453643d72c009a341c901d3ea4bcd1232fa30f14530aba0029  notes/review_results/partB/ccs_tables.md
610ba6e511cfbebdf9556100fa6014b4d333f9e37f9a2ba945715daf23010da9  notes/review_results/partB/coupling_map_run.log
edda1e8f73788a0cac0ac1cac96e70a54f356589053f543572516c76b6eecd07  notes/review_results/partB/coupling_map_tables.md
0b68e80691d0bd1cd8b75688fabb530f09d5fe0a5bcd314b3a781d04aac64246  notes/review_results/partB/crosslag_budget_null_run.log
84d310c4307dc71068ac9768116d71b5c8010a4ebf563048623f8eca571391b7  notes/review_results/partB/crosslag_budget_null_tables.md
d47efc480d918b6e8a218ac75a006b5c31a58d488fbec6340e741cc8cae01e4e  notes/review_results/partB/crosslag_budget_run.log
b94513668d506b9c87c2a1ff77894e5b67ddabd2f28e33b895f8bd6a686ea32b  notes/review_results/partB/crosslag_budget_tables.md
b950afe3214441c965f88d8ce97f2ab172f9d70fffd9f5eb061c6d4b9e7569eb  notes/review_results/partB/crosslag_deviation.csv
beb4d21f969c9b605d52f035d4c9da3cbc3ae299f5cbd9ea11757dd5a5292a42  notes/review_results/partB/crosslag_deviation_run.log
6bd45f16da4497130f7372c9e07449fa38c5c6d14ecc392b3aafb424c5862b34  notes/review_results/partB/crosslag_deviation_tables.md
7a86f709d496839e0662a15c9e75245a3b53069b2c680c35326fcecb79a8ddd5  notes/review_results/partB/diag_series_ts_demean_W30.npz
09d36f175bc95bac4e5e620b6efd4a1fffd8d5bbe02e986978296d62bae31169  notes/review_results/partB/diag_series_ts_demean_W60.npz
b93baa5f87c4ba0da4efeebd0bb701d30d9c2a3f4af3f6569d148ee2a02d4f56  notes/review_results/partB/diag_series_ts_gsr_W30.npz
f406bfce040d74a7d5e3c1b0e9cc5c80ec9daef8c495c14a4dd72f3c82b0643a  notes/review_results/partB/diag_series_ts_gsr_W60.npz
32719813d2a3272b6f617032d58f59ab4a08a2d517d5d40013b67008c9a253ff  notes/review_results/partB/diag_tables.md
887a20b92a9d5c3f3fd1382be99cae2d6e7dbc370071997e21f9f7a566837806  notes/review_results/partB/diagnostic_alternatives.csv
a4502ca82f54fb52f681506ee20d53c6c496d37ff4c998d89c61ca2f029ab761  notes/review_results/partB/diagnostic_alternatives_run.log
16206440c75489f927c6f4a746a8bb2d279c0ae4dbcb69abf42ae0476f627cdc  notes/review_results/partB/diagnostic_alternatives_tables.md
d3ffa5dc37c92abc48f356f3aaf70fe94fdf616d4e027fb66a494cd2c353b472  notes/review_results/partB/directed_crosslag.csv
077aa103fbb10c3484ef81dd624442679723054cc323cf58668fed6bb1ac3a13  notes/review_results/partB/directed_crosslag_run.log
2dfd36ac040097ca1516125660f59dd42ff84cea7456413e74b424b561544202  notes/review_results/partB/directed_crosslag_tables.md
cbde03f497fd4c3e42199a7fcdb4c47d90338b993f6f9a9dd0ac61b4ec8b0394  notes/review_results/partB/exchange_rates_run.log
6259e7b7b96c001bee4b51ae415932124c3a7099513ed907c2dc4b0a4ce6a0bf  notes/review_results/partB/exchange_rates_tables.md
7f9480740d7299614fc2a4370ea81f5678165a5d73cc0b19000351c0e794992f  notes/review_results/partB/family_atoms_run.log
c1395fdbdc887609365ff27f152bc866aa075f02d880847c23c200d67493bba5  notes/review_results/partB/family_atoms_tables.md
b619adabbbaa4a0d22893a6d6a22fe999c8c573d1b74a868ac7c116fdf7f3660  notes/review_results/partB/family_atoms_ts_demean_W60.npz
50533f03e3131a2cde28f9268fa69d8891ba97356b5d65dfa76a5a9c9c32cbbf  notes/review_results/partB/family_atoms_ts_gsr_W60.csv
f47dfa72093d7515372ecf653441281cd5050ff6302a566cc33f155a973ecff2  notes/review_results/partB/family_atoms_ts_gsr_W60.npz
54462aa618f38982868ce7039641e271c3b367cc5254e3162125f82ecbbe6e69  notes/review_results/partB/family_checks.log
4fd993d03a7773d1d221f21ff3570015097e93e6b6b84a961c8f1c0315dcec24  notes/review_results/partB/inference_revision.csv
eea2d403e4fe01312226bb2945ea287a5c13ec5a224b2412187a4c175fd7a72d  notes/review_results/partB/inference_revision_run.log
eb99681ce6c9903327d3e5dbff9c52a2a7e17bf2e2f375b750664911a7cda1bb  notes/review_results/partB/inference_revision_tables.md
d9c1ab64fa5696b5c5152abbc7b7ff947e9ef464139b7f2b94fcc29fa4a40039  notes/review_results/partB/lag_tables.md
8eb51fdea162945cbb604484223ab0385890b2fcabdd68fdcef71bab5342d039  notes/review_results/partB/leave_two_out.csv
2825db34b6c6e394dbab5fbb1bc4c2ca2f2ba88ca3427816fed8646c82e8f549  notes/review_results/partB/leave_two_out.log
30aa7f11c3a4619ac6d1748b814008cb24fc8abd7d7da24c974338c46d5f97ba  notes/review_results/partB/overlay_points_run.log
ded5d8ace53055bdc5b8aabc34ac064c733a02ec56f93054fbfef40000f7b162  notes/review_results/partB/prewhiten_orders.csv
f0d387781d413cac85cd6da794ca66ccf721125cc6e782d08882804b864a043e  notes/review_results/partB/prewhiten_run.log
67b48554d87f8f9ccc4d2ad4328eba88ddf5de6c02c6687327dfe4b7f6634eac  notes/review_results/partB/prewhiten_tables.md
a23b0714cc82ea0958ac1bd3a87d9643d1886a1ed4eacafe99f56a96d8be36ce  notes/review_results/partB/regional_partial.csv
9b0acba2b81b0e3f5279d3c5d1a47ca2c20e09312a758bf05a09f6c27af7cabf  notes/review_results/partB/regional_partial_run.log
26b256abf47d69415d2eaf3c5fbd2bc026450b3714b01b4d85bbeaf0524586af  notes/review_results/partB/regional_partial_tables.md
3c81127bf2d05d8c269eb3fc962ee6e44a565b8124e29dc62b831287f64aca18  notes/review_results/partB/regional_sts_r1_run.log
ebeba526a1457cae1bfedd131162d0a98d3a41fc08c767adf34e76f2ded5eff4  notes/review_results/partB/regional_sts_r1_tables.md
55d9f763ab0567df3276321b8c2b3829fc338292591b6d347a00aef6921cbb79  notes/review_results/partB/residual_source.log
4721e85ca7985aa41217c8c62afb49120dc49dccc21fc07865f13657bdac1cb6  notes/review_results/partB/scope_map_overlay.csv
a93adb9d1e7839b7e7f0a1dbe69b068d33b36cd95abc2ad8b17591e1b8ce2fb9  notes/review_results/partB/scope_map_run.log
32dfceb35b5a73fa017dc2893ee000bbcdd4ed70f04d17ae71faeb43cf9cdd4e  notes/review_results/partB/scope_map_tables.md
186fb18cfd06bcef0e65543515c806d73a8fb9e23a1f8f71e58c5301f97832ee  notes/review_results/partB/splithalf.log
8ad945bb34a3dcff186954d52d3284e4ca83a6f13abf5fc39b4271eed65d282c  notes/review_results/partB/splithalf_subjects.csv
25810b5ddbf6f7e2dbb0adf337c3df185c8f3e6318106415e29c52086bd0a9f3  notes/review_results/partB/splithalf_tables.md
85925137d37ea8545997b47e929a52169c15218703c26fdc783d28462f5be773  notes/review_results/partB/whitened_spectrum_run.log
f4972d72992f774cacf3dd9b55f86bfe560dd966b53bf6fc3d0a7271797ba885  notes/review_results/partB/whitened_spectrum_tables.md'
EXPECTED_STATUS=' M manuscript/figures/captions_v2.md
 M manuscript/figures/fig1_v2_scope_map.pdf
 M manuscript/figures/fig2_v2_atoms_observed_substituted.pdf
 M manuscript/figures/fig3_v2_per_subject.pdf
 M manuscript/figures/fig3_v2_per_subject.png
 M manuscript/figures/fig4_v2_regional.pdf
 M manuscript/figures/fig5_v2_residual_diagnostic.pdf
 M manuscript/figures/fig5_v2_residual_diagnostic.png
 M manuscript/figures/fig6_v2_lag_dependence.pdf
 M notes/review_computations_2026-09-14.md
 M notes/review_results/inference_rows_ccs.csv
 M notes/review_results/inference_rows_ccs_pub.csv
 M notes/review_results/inference_rows_diag.csv
 M notes/review_results/inference_rows_diag.pkl
 M notes/review_results/inference_rows_lag.csv
 M notes/review_results/inference_rows_prewhiten.csv
 M notes/review_results/inference_rows_prewhiten.pkl
 M notes/review_results/logs/phiid_fast_validate.log
 M notes/review_results/logs/rev_extra.log
 M notes/review_results/logs/rev_run_raw.log
 M notes/review_results/logs/review_checks.log
 M notes/review_results/logs/review_v2_residual_null.log
 M notes/review_results/logs/sts_matched_null_F1.log
 M notes/review_results/logs/sts_matched_null_F2.log
 M notes/review_results/logs/sts_matched_null_F3.log
 M notes/review_results/partB/aligned_directed.csv
 M notes/review_results/partB/aligned_directed_run.log
 M notes/review_results/partB/aligned_directed_tables.md
 M notes/review_results/partB/bandpassed_expectations.csv
 M notes/review_results/partB/bandpassed_expectations_run.log
 M notes/review_results/partB/bandpassed_expectations_tables.md
 M notes/review_results/partB/bca_intervals.csv
 M notes/review_results/partB/calibration.csv
 M notes/review_results/partB/calibration_filtered.csv
 M notes/review_results/partB/calibration_filtered_run.log
 M notes/review_results/partB/calibration_filtered_tables.md
 M notes/review_results/partB/calibration_run.log
 M notes/review_results/partB/calibration_tables.md
 M notes/review_results/partB/ccs_decomposition.csv
 M notes/review_results/partB/ccs_decomposition_run.log
 M notes/review_results/partB/ccs_decomposition_tables.md
 M notes/review_results/partB/ccs_definition_check.log
 M notes/review_results/partB/ccs_pub_tables.md
 M notes/review_results/partB/ccs_tables.md
 M notes/review_results/partB/coupling_map_run.log
 M notes/review_results/partB/coupling_map_tables.md
 M notes/review_results/partB/crosslag_budget_null_run.log
 M notes/review_results/partB/crosslag_budget_null_tables.md
 M notes/review_results/partB/crosslag_budget_run.log
 M notes/review_results/partB/crosslag_budget_tables.md
 M notes/review_results/partB/crosslag_deviation.csv
 M notes/review_results/partB/crosslag_deviation_run.log
 M notes/review_results/partB/crosslag_deviation_tables.md
 M notes/review_results/partB/diag_series_ts_demean_W30.npz
 M notes/review_results/partB/diag_series_ts_demean_W60.npz
 M notes/review_results/partB/diag_series_ts_gsr_W30.npz
 M notes/review_results/partB/diag_series_ts_gsr_W60.npz
 M notes/review_results/partB/diag_tables.md
 M notes/review_results/partB/diagnostic_alternatives.csv
 M notes/review_results/partB/diagnostic_alternatives_run.log
 M notes/review_results/partB/diagnostic_alternatives_tables.md
 M notes/review_results/partB/directed_crosslag.csv
 M notes/review_results/partB/directed_crosslag_run.log
 M notes/review_results/partB/directed_crosslag_tables.md
 M notes/review_results/partB/exchange_rates_run.log
 M notes/review_results/partB/exchange_rates_tables.md
 M notes/review_results/partB/family_atoms_run.log
 M notes/review_results/partB/family_atoms_tables.md
 M notes/review_results/partB/family_atoms_ts_demean_W60.npz
 M notes/review_results/partB/family_atoms_ts_gsr_W60.csv
 M notes/review_results/partB/family_atoms_ts_gsr_W60.npz
 M notes/review_results/partB/family_checks.log
 M notes/review_results/partB/inference_revision.csv
 M notes/review_results/partB/inference_revision_run.log
 M notes/review_results/partB/inference_revision_tables.md
 M notes/review_results/partB/lag_tables.md
 M notes/review_results/partB/leave_two_out.csv
 M notes/review_results/partB/leave_two_out.log
 M notes/review_results/partB/overlay_points_run.log
 M notes/review_results/partB/prewhiten_orders.csv
 M notes/review_results/partB/prewhiten_run.log
 M notes/review_results/partB/prewhiten_tables.md
 M notes/review_results/partB/regional_partial.csv
 M notes/review_results/partB/regional_partial_run.log
 M notes/review_results/partB/regional_partial_tables.md
 M notes/review_results/partB/regional_sts_r1_run.log
 M notes/review_results/partB/regional_sts_r1_tables.md
 M notes/review_results/partB/residual_source.log
 M notes/review_results/partB/scope_map_overlay.csv
 M notes/review_results/partB/scope_map_run.log
 M notes/review_results/partB/scope_map_tables.md
 M notes/review_results/partB/splithalf.log
 M notes/review_results/partB/splithalf_subjects.csv
 M notes/review_results/partB/splithalf_tables.md
 M notes/review_results/partB/whitened_spectrum_run.log
 M notes/review_results/partB/whitened_spectrum_tables.md
?? notes/review_results/partB/positive_definite.csv
?? notes/review_results/partB/positive_definite_run.log
?? notes/review_results/partB/positive_definite_tables.md'
MSGFILE=$(mktemp)
trap 'rm -f "$MSGFILE"' EXIT
cat > "$MSGFILE" <<'MSG'
B26: the outputs of its run at d5a65bd, as the run wrote them

B26 (record, "The matrices that are not positive definite (B26): pre-run entry"):
the 39 steps of section 6 of run_all.sh, B25 excepted, run in place at d5a65bd by
notes/partB26_positive_definite.py on V.S.'s machine on 29 Sep 2026 (13:04 to 16:49
EEST, 225 min; one attempt, every step with exit status 0), with
rev_phiid_fast.atoms_from_corr returning NaN for a matrix that is not positive
definite. Of 473,262,025 matrix evaluations, 42,681 were not positive definite, all
of them passed to atoms_from_corr, the corrected path; none of the 215,276,476
sample correlation matrices. The data's pair-windows without an AR(1)-substituted
estimate: 4 of 2,569,560 at W = 60 in each variant, 1,617 (ts_gsr) and 1,661
(ts_demean) of 5,139,120 at W = 30; no whole-run pair.

The 96 files the run rewrote (86 under notes/review_results, 9 under
manuscript/figures, and the report notes/review_computations_2026-09-14.md; 50 with
changed content, 46 with only their commit and times changed) and B26's three new
files (its CSV, tables and log), as the run wrote them: their sha256 are those of
the run's evidence. The outcome entry and the text that reports the run follow in
the next commit.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0172Ln49VR8FQoNbX2oVTzzo
MSG
fail() { echo "STOP: $*"; echo "Nothing has been committed or pushed. Send the planning session the whole output."; exit 1; }
fail_after() { echo "STOP: $*"; echo "The commit is made on this laptop but NOT pushed; do not push it by hand. Send the planning session the whole output."; exit 1; }
check_commit() {  # the commit $1 against the expected files
  [ "$(git rev-parse "$1^")" = "$BASE" ] || { echo "its parent is not d5a65bd"; return 1; }
  [ "$(git log -1 --format=%s "$1")" = "$SUBJECT" ] || { echo "its subject is not the expected one"; return 1; }
  [ "$(git log -1 --format='%an <%ae>' "$1")" = "vilalius <sampalisvasilis@gmail.com>" ] || { echo "its author is not vilalius <sampalisvasilis@gmail.com>"; return 1; }
  [ "$(git diff --name-only "$BASE" "$1" | sort)" = "$(echo "$EXPECTED_SHA" | awk '{print $2}' | sort)" ] || { echo "it does not change exactly the 99 files"; return 1; }
  while read -r h f; do
    [ "$(git show "$1:$f" | sha256sum | cut -c1-64)" = "$h" ] || { echo "$f in the commit does not have the run's sha256"; return 1; }
  done <<< "$EXPECTED_SHA"
  return 0
}

cd "$REPO" 2>/dev/null || fail "$REPO not found"
echo "branch: $(git rev-parse --abbrev-ref HEAD)   HEAD: $(git log --oneline -1 | cut -c1-100)"
[ "$(git rev-parse --abbrev-ref HEAD)" = master ] || fail "not on master"
git fetch -q origin 2>/dev/null || echo "(could not reach GitHub to refresh origin/master; using the last known one)"

if [ "$(git rev-parse HEAD)" != "$BASE" ]; then
  # resume: the commit may be made already
  if check_commit HEAD >/dev/null 2>&1; then
    echo "The outputs commit is already made: $(git log --oneline -1 | cut -c1-100)"
  else
    fail "master is neither at d5a65bd nor at the outputs commit: $(check_commit HEAD)"
  fi
else
  [ "$(git rev-parse -q --verify origin/master)" = "$BASE" ] || fail "origin/master is not at d5a65bd"
  [ -z "$(git diff --cached --name-only)" ] || fail "something is staged: $(git diff --cached --name-only | head -5 | tr '\n' ' ')"
  got=$(git status --porcelain --untracked-files=all | sort)
  want=$(echo "$EXPECTED_STATUS" | sort)
  if [ "$got" != "$want" ]; then
    echo "git status differs from the run's (lines only in yours with >, only in the run's with <):"
    diff <(echo "$want") <(echo "$got") | grep '^[<>]' | head -20
    fail "the working tree is not exactly as the run left it"
  fi
  n=0
  while read -r h f; do
    [ -f "$f" ] || fail "$f is missing"
    [ "$(sha256sum < "$f" | cut -c1-64)" = "$h" ] || fail "$f does not have the sha256 of the run's evidence"
    n=$((n+1))
  done <<< "$EXPECTED_SHA"
  echo "the 99 files: $n checked, each with the run's sha256"
  echo "$EXPECTED_SHA" | awk '{print $2}' | tr '\n' '\0' | xargs -0 git add -- || fail "git add failed"
  [ "$(git diff --cached --name-only | sort)" = "$(echo "$EXPECTED_SHA" | awk '{print $2}' | sort)" ] || { git reset -q; fail "the staged files are not exactly the 99"; }
  git -c user.name=vilalius -c user.email=sampalisvasilis@gmail.com commit -q -F "$MSGFILE" || { git reset -q; fail "git commit failed"; }
  echo "committed: $(git log --oneline -1 | cut -c1-100)"
fi
r=$(check_commit HEAD) || fail_after "the commit does not check: $r"
[ -z "$(git status --porcelain --untracked-files=all)" ] || fail_after "git status is not empty after the commit"
echo "the commit checks: 99 files, each with the run's sha256; nothing else changed"
TIP=$(git rev-parse HEAD)
if [ "$(git rev-parse -q --verify origin/master)" = "$TIP" ]; then
  echo "Already pushed: origin/master is $(git rev-parse --short=7 HEAD)."
else
  git push origin master || fail_after "the push failed: run this script again to push"
fi
[ "$(git rev-parse -q --verify origin/master)" = "$TIP" ] || fail_after "origin/master is not the outputs commit after the push"
echo "DONE: master and origin/master are at $(git rev-parse --short=7 HEAD). Tell the planning session."
