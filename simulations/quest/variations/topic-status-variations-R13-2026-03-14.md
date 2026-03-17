Written to `simulations/quest/rubrics/topic-status-rubric-v12-variations-R13-2026-03-15.md`.

---

## Round 13 -- Design Summary

**Rubric baseline:** v12 (max 255) — R12 added C-39 (trigger sentences within OUTPUT DECLARATION INVARIANT) and C-40 (INVARIANT:/OUTPUT FORM: labeled sub-components).

**Two C-candidates probed:**

| Candidate | Pattern | Site | Parallel |
|-----------|---------|------|----------|
| **C-41** | PHASE 3 OUTPUT DECLARATION with INVARIANT:/OUTPUT FORM: labels + Trigger: sentence | PHASE 3 execution body | Extends C-38/C-39/C-40 from PHASE 2 to PHASE 3 |
| **C-42** | `ADVERSARY:` clause at PHASE 2 execution entry | PHASE 2 execution body | Extends adversary framing from output-template-only (COMMIT DECISION) into execution body |

**Orthogonality:** C-41 = PHASE 3 output structure. C-42 = PHASE 2 entry framing. Neither implies the other.

**Variant map:**

| Variant | C-41 | C-42 | Axis |
|---------|------|------|------|
| V-01 | PASS | PASS | Min delta — both in execution-prose |
| V-02 | **FAIL** | PASS | C-41 withheld — isolation test |
| V-03 | PASS | **FAIL** | C-42 withheld — isolation test |
| V-04 | PASS | PASS | Lifecycle GUARD contract form |
| V-05 | PASS | PASS | Lifecycle + elevated titled blocks for both new structures |

All five score **255/255 under v12**. The structural gaps between V-01/V-02 and V-01/V-03 are the excellence signals that would define Tier 12 criteria.
