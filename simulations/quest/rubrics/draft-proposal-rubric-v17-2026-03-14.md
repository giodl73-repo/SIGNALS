Written to `simulations/quest/rubrics/draft-proposal-rubric-v17-2026-03-15.md`.

---

**Summary of v16 → v17 changes:**

**Two new criteria extracted from the R16 excellence signals:**

| ID | Criterion | Trigger | Pattern |
|----|-----------|---------|---------|
| **C-42** | T-40 CONDITION carries an inline failure exemplar showing what an abstract-only T-38 CONDITION looks like | V-01 R16: T-40 and T-41 are silent — T-40 is an operational trigger with an evaluable CONDITION field | Mirrors C-40 applied to T-40's own CONDITION |
| **C-43** | T-40 CONDITION additionally carries a correct-format prescription showing what a passing T-38 CONDITION looks like | Same source | Mirrors C-41 applied to T-40's CONDITION |

**Cascade invariant:** C-42 FAIL → C-43 FAIL. C-42 PASS does not guarantee C-43 PASS.

**C-24 updated:** 41 → 43 rows (one per C-01..C-43).

**Denominator:** /34 → /36.

**Score projections for R16 variations under v17** (assuming T-40 CONDITION quality satisfies C-42/C-43):

| Variation | Designed fail | C-24 | Total fails | Composite |
|-----------|--------------|------|-------------|-----------|
| V-01 (C-39) | C-39 | FAIL (41 < 43) | 2 | 99.44 |
| V-02 (C-40 + C-41) | C-40, C-41 | FAIL (41 < 43) | 3 | 99.17 |

The structural logic: the same two-part self-documentation requirement imposed on T-37's CONDITION (C-38/C-39) and T-38's CONDITION (C-40/C-41) now applies one level up to T-40's CONDITION (C-42/C-43). Each trigger entry in the watch chain must carry both what fires it and what would satisfy the criterion it watches — without consulting the rubric.
