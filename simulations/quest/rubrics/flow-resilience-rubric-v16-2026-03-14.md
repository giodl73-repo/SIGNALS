Written to `simulations/quest/rubrics/flow-resilience-rubric-v16-2026-03-15.md`.

---

**v16 summary — what changed:**

| | v15 | v16 |
|---|---|---|
| Denominator | 38 | **42** |
| New criteria | C-44, C-45, C-46 | **C-47, C-48, C-49, C-50** |
| R15 ceiling | 99.74 (37/38) | **98.81 (37/42)** |
| R16 ceiling | open | **99.76 (41/42) — V-04 and V-05 tied** |

---

**Four new criteria extracted from R16:**

**C-47 — Named Enforcement Mechanism Labels** *(E-39)* — Both C-45 mechanisms carry distinct named labels ("Placeholder Negation", "Enforcement Clause E1", "Rule A — No Deferral", or equivalent noun-bearing identifiers). V-01 FAIL (plain unlabeled sentences); V-02/V-03/V-04/V-05 PASS.

**C-48 — Co-located Enforcement Bundle in Single Named Structure** *(E-40)* — Both mechanisms appear within one named containing element (named blockquote, named enforcement contract section, or equivalent). Two separately named top-level clauses without a container (V-03's E1/E2 pattern) fail. V-01/V-03 FAIL; V-02/V-04/V-05 PASS. Depends on C-47.

**C-49 — Document-Level Pre-Read Enforcement Preamble with Inline Cross-Reference Reinforcement** *(E-41)* — Enforcement appears in a labeled preamble positioned *before all sub-parts*, with at least one sub-part containing inline reinforcement that cites preamble rules by label. V-04 PASS (Document Enforcement Contract preamble + "Rule A/B applies" inline); V-01/V-02/V-03/V-05 FAIL (all embed enforcement within a sub-part). Depends on C-48.

**C-50 — Multi-Location Enforcement with Three Independent Locations and Explicit Restatement Labeling** *(E-42)* — Enforcement appears in three or more independent locations spanning different document hierarchy levels, with at least one location carrying an explicit restatement label (e.g., "(restated for co-location)"). V-05 PASS (header + blockquote + row-descriptor, explicit restatement label); V-01/V-02/V-03/V-04 FAIL (two or fewer locations). Depends on C-47.

---

**R16 per-variation scores under v16:**

| Variation | C-47 | C-48 | C-49 | C-50 | Total | Composite |
|---|---|---|---|---|---|---|
| V-01 | FAIL | FAIL | FAIL | FAIL | 38/42 | 99.05 |
| V-02 | PASS | PASS | FAIL | FAIL | 40/42 | 99.52 |
| V-03 | PASS | FAIL | FAIL | FAIL | 39/42 | 99.29 |
| V-04 | PASS | PASS | PASS | FAIL | 41/42 | **99.76** |
| V-05 | PASS | PASS | FAIL | PASS | 41/42 | **99.76** |

The 100.00 ceiling now requires all ten post-C-40 axes (C-41–C-50). The remaining open axis: a variation that implements both C-49 (document-level preamble, V-04's approach) **and** C-50 (three independent locations with explicit restatement, V-05's approach) — these are the two axes that are currently mutually exclusive in the R16 field.
