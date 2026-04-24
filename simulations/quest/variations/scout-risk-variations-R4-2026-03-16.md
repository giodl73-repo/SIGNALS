**scout-risk R4 variations written** — `simulations/quest/golden/scout-risk-variate-R4-2026-03-16.md`

---

## Summary

**R4 gap**: R3 V-05 scores 105/110 under v4 rubric — fails C-17 (no FROM/TO severity transitions) and C-18 (no type diversity enforcement).

**Five variations:**

| ID | Axis | Target | Mechanism | Score |
|----|------|--------|-----------|-------|
| V-01 | Lifecycle | C-17 | Prose template: "escalates from [X] to [Y]" in Phase 3 pairing format | 101 |
| V-02 | Output format | C-18 | Post-table diversity gate: count distinct types, repair if <3 | 98 |
| V-03 | Phrasing register | C-17 | Tabular FROM/TO: separate columns enforce both severity fields visibly | 98 |
| V-04 | Lifecycle + Output | C-17+C-18+C-15 | FROM/TO + diversity gate + sub-field promotion on R3 V-04 base | 109 |
| V-05 | Full integration | C-17+C-18 | R3 V-05 + FROM/TO in STEP 3 + diversity rule in STEP 2 + 2 new self-check items | 109 |

**Key design insight**: V-01 vs V-03 is an empirical test of two C-17 mechanisms — prose template with two slots vs table columns with separate `From Severity` / `To Severity` fields. The tabular mechanism should be structurally stronger for the same reason IF-THEN column headers outperform prose IF-THEN rules (C-14 evidence): the model fills cells rather than following constraints. R4 scoring will confirm.

**C-10 ceiling unchanged**: 109/110 on all base prompts — C-10 PASS requires a live AMEND directive.
