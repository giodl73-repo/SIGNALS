Written to `simulations/quest/rubrics/topic-status-rubric-v17-variate-R20-2026-03-15.md`.

---

## Round 20 -- Design Summary

**Context:** R19 closed the final tier-16 gap (C-47 FAIL + C-49 FAIL with C-48 PASS). The tier-16 ablation matrix is exhausted. R20 pivots to v18 seeding.

**Two candidate criteria introduced:**

| Candidate | Name | Axis | Description |
|-----------|------|------|-------------|
| C-50 | STOP predicate phase labels | Output format | `[P-N-ADVERSARY DEFEAT:]` prefixes on STOP CONDITION predicates (2)-(3)-(4), matching preamble ADVERSARY CHAIN labels |
| C-51 | Preamble defeat forecast | Lifecycle emphasis | Nested `DEFEAT CONDITION:` sub-component in each P-N-ADVERSARY preamble entry, forecasting the execution-body observable defeat property |

**Ablation matrix (all score 300 under v17; differentiation emerges under v18):**

| Variant | C-50 | C-51 | v17 | v18 projected | Isolation purpose |
|---------|------|------|-----|---------------|-------------------|
| V-01 | PASS | PASS | 300 | 310 | Full tier-17 seeding baseline |
| V-02 | FAIL | PASS | 300 | 305 | Isolates C-50 (numbered STOP predicates) |
| V-03 | PASS | FAIL | 300 | 305 | Isolates C-51 (preamble two-part entries only) |
| V-04 | FAIL | FAIL | 300 | 300 | Pure v17 max reference (= R19 V-01) |
| V-05 | PASS | PARTIAL | 300 | 305* | Probes C-51 all-or-nothing vs partial; P1 preamble DEFEAT absent |

**V-03 vs V-05 delta** under v18 will resolve the key question: does C-51 require defeat forecasts at all three P-N-ADVERSARY entries (all-or-nothing) or does P2+P3 without P1 still earn partial credit?
