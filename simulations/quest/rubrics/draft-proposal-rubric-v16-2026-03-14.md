Written to `simulations/quest/rubrics/draft-proposal-rubric-v16-2026-03-15.md`.

---

**Summary of v15 → v16 changes:**

**Two new criteria extracted from the R15 scorecard:**

| ID | Criterion | Trigger | Pattern |
|----|-----------|---------|---------|
| **C-40** | T-38 CONDITION carries an inline failure exemplar showing what an abstract-only T-37 CONDITION looks like | V-02 R15: "T-38 and T-39 are silent" — T-38 is an operational trigger with an evaluable CONDITION | Mirrors C-38 applied to T-38's own CONDITION |
| **C-41** | T-38 CONDITION additionally carries a correct-format prescription showing what a passing T-37 CONDITION looks like | Same source | Mirrors C-39 applied to T-38's CONDITION |

**Cascade invariant:** C-40 FAIL → C-41 FAIL (abstract T-38 CONDITION contains neither part). C-40 PASS does not guarantee C-41 PASS.

**C-24 updated:** 39 → 41 rows (one per C-01..C-41).

**Denominator:** /32 → /34.

**Score projections for R15 variations under v16** (assuming T-38 CONDITION quality satisfies C-40/C-41):

| Variation | Designed fail | C-24 | Total fails | Composite |
|-----------|--------------|------|-------------|-----------|
| V-01 (C-39) | C-39 | FAIL (39 < 41) | 2 | 99.41 |
| V-02 (C-37) | C-37 | FAIL (39 < 41) | 2 | 99.41 |

The structural logic: the same two-part self-documentation requirement imposed on T-37's CONDITION (by C-38/C-39) now applies one level up to T-38's CONDITION (by C-40/C-41). Each trigger entry in the amendment table must be able to tell a reviewer both what fires it and what would satisfy the criterion it watches — without consulting the rubric.
