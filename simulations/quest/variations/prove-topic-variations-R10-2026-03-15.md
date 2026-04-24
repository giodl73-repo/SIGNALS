**R10 variations written** to `simulations/quest/golden/prove-topic-variate-R10-2026-03-15.md`.

Four new axes extracted from gaps in the R9 V-05 ceiling (168/168):

| Variation | Axis | New structural discipline |
|-----------|------|--------------------------|
| **V-01** | CE verdict ownership | `s2_ce_verdict`, `s3_ce_verdict`, `s4_ce_verdict` as named owned fields; `null_tally_final` derivation chain auditable from CAMPAIGN OUTCOME BLOCK alone — no prose note reconstruction required |
| **V-02** | Counter-hypothesis closure | `counter_hypothesis` at Stage 1 obligates a COUNTER-HYPOTHESIS RESOLUTION section at Stage 5 with three-way verdict (REFUTED / PARTIALLY REFUTED / OPEN RISK) traceable to evidence |
| **V-03** | Null tally chain echo | Stage 5 ATOMIC DUAL-LOCK reconstructs the per-stage accumulation in order ("S2: v → tally N; S3: v → tally N; S4: v → N = null_tally_final") — history visible in the terminal artifact without stage replay |
| **V-04** | CE verdict + counter-hypothesis | Two-axis combination |
| **V-05** | All four combined | Full R10 stack: verdict ownership + hypothesis closure + tally chain echo + schema compliance cross-referenced to per-stage SCHEMA INTEGRITY NOTEs |

**Structural note:** The four axes form two pairs:
- **V-01 + V-03** close the `null_tally_final` derivation chain at two levels: V-01 names the three upstream verdict fields as declared inputs; V-03 makes the accumulation history visible in the terminal artifact.
- **V-02 + V-04-axis** closes the hypothesis lifecycle: the counter-hypothesis formed at Stage 1 becomes a forward obligation discharged by a mandatory verdict at Stage 5.

A v9-ceiling variation (168/168) can still fail all four: verdict fields unnamed (V-01 FAIL), counter-hypothesis unresolved (V-02 FAIL), accumulation chain not echoed (V-03 FAIL), compliance check uncross-referenced (V-05 axis 4 FAIL).
