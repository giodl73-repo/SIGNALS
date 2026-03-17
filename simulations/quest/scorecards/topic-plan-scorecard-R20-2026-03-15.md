## topic:plan — Round 20 Scorecard

**Rubric v20 (58 criteria). All 5 essential PASS for all variations.**

### Key findings

The most important result is the structural gap between single-axis stripped-down variations (V-01, V-02) and baseline-inheriting variations (V-03, V-04, V-05):

| Variation | Score | % | C-58 | Gate-0 |
|-----------|-------|---|------|--------|
| V-01 (role sequence) | 10.5/58 | 18% | FAIL | — |
| V-02 (temporal audit) | 12/58 | 21% | **PASS** | — |
| V-03 (Gate-0 arch) | 40.5/58 | 70% | FAIL | +6/13 |
| V-04 (V-01+V-02 combo) | 36/58 | 62% | **PASS** | — |
| **V-05 (full combo)** | **42.5/58** | **73%** | **PASS** | **+6/13** |

**Ranking: V-05 > V-03 > V-04 >> V-02 > V-01**

### Discriminating result

V-03 outscores V-04 (70% vs 62%) because Gate-0 architecture satisfies 6 criteria from C-43–C-55, worth more than C-58 alone (1 criterion). The Phase -1 / §ID architecture carries more rubric weight than any single behavioral column addition.

### Excellence signals from V-05

1. **Compound epistemic gating** — Gate-0 (schema completeness before proposals) + temporal audit (defense formed before signals read) close two independent epistemic gaps simultaneously. Neither criterion requires the other; together they prevent schema gaps AND post-hoc rationalization in one prompt.

2. **Inventory-first ordering** — V-01's role sequence axis identified a gap not yet in any rubric criterion: reading all 9 namespace tables before opening strategy.md prevents strategy vocabulary from anchoring the first-pass artifact classification. SIGNAL READ-LOCK blocks re-reading, not strategy-anchored initial labeling. Candidate for C-59.

```json
{"top_score": 73, "all_essential_pass": true, "new_patterns": ["Inventory-first epistemic ordering: completing all 9 namespace signal tables before strategy.md is opened prevents the strategy vocabulary from anchoring artifact classification on the first pass — SIGNAL READ-LOCK blocks re-reading but not strategy-anchored initial labeling; inventory-first makes the evidence base vocabulary-independent before the prior frame is visible; no rubric criterion in C-01–C-58 currently enforces this ordering constraint"]}
```
