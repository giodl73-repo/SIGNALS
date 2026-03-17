**scout-risk R3 — 5 variations written** to `simulations/quest/golden/scout-risk-variate-R3-2026-03-16.md`

---

## R3 Summary

**Context**: R2 V-05 already passes C-14 (IF-THEN token) and C-15 (type taxonomy) under v3 rubric — those criteria were issued because R2 produced them. The only v3 gap is **C-16** (requires ≥3 interdependency pairs; R2 enforced ≥2). Score ceiling under v3 from R2 V-05 baseline: 103/106.

| ID | Axes | New mechanism | C-14 | C-15 | C-16 | Score |
|----|------|---------------|------|------|------|-------|
| V-01 | Lifecycle | ≥3 pairs on R2 V-03 base | FAIL | FAIL | **PASS** | 99 |
| V-02 | Output format | IF-THEN as schema column template | **PASS** | FAIL | FAIL | 95 |
| V-03 | Phrasing register | Type contract sub-fields per type | FAIL | **PASS** | FAIL | 96 |
| V-04 | Lifecycle + Output format | ≥3 pairs + IF-THEN schema | **PASS** | **PASS** | **PASS** | **105** |
| V-05 | Full integration | R2 V-05 + all three v3 mechanisms | **PASS** | **PASS** | **PASS** | **105** |

**Key design decisions:**

- **V-01** isolates C-16 cleanly by building on R2 V-03 (the lifecycle base), not V-05. This separates the contribution of ≥3 pairs from IF-THEN and taxonomy.
- **V-02** tests whether embedding IF-THEN in the **column header** (`IF [condition], THEN risk activates`) is a stronger structural enforcer than R2 V-01's explicit rule — schema completion vs. constraint following.
- **V-03** introduces **structural obligation sub-fields** per mitigation type (Spike: Unknown + Time-box; Gate: Criterion; etc.) — raises C-15 from "type label present" to "type contract fulfilled."
- **V-04 and V-05 tie at 105** — C-10 PARTIAL (1 pt) is the unreducible ceiling on all base prompts without a live AMEND directive.
