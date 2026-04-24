Written to `simulations/quest/rubrics/topic-status-rubric-v11-variations-R11-2026-03-15.md`.

---

## Variations: `topic:status` -- Round 11
**Rubric:** v11 (max 245) | **Date:** 2026-03-15

---

### Design Context

**R10 gap:** No variant achieved 245. C-37 and C-38 are structurally orthogonal:
- R10 V-04 satisfies C-37 (lifecycle GUARD entries carry inline trigger clauses) but not C-38 (third C-36 site is a lifecycle phase-definition OUTPUT field, not execution-body resident).
- R10 V-05 satisfies C-38 (execution-body PHASE 2 OUTPUT DECLARATION) but not C-37 (exits carry names only at the GUARD site; trigger sentences live only in the preamble).

**R11 hypothesis:** Combine R10 V-04's C-37 mechanism with R10 V-05's C-38 mechanism in a single variant.

**Predicted score map:**

| Variant | C-35 | C-36 | C-37 | C-38 | Predicted |
|---------|------|------|------|------|-----------|
| V-01 | PASS | PASS | PASS | PASS | 245/245 |
| V-02 | PASS | PASS | FAIL | PASS | 240/245 |
| V-03 | PASS | PASS | PASS | FAIL | 240/245 |
| V-04 | PASS | PASS | PASS | PASS | 245/245 |
| V-05 | PASS | PASS | PASS | PASS | 245/245 |

---

### Variation axes

| ID | Axis | C-37 mechanism | C-38 mechanism |
|----|------|----------------|----------------|
| V-01 | Min delta, execution-prose form | `Exit A -- file absent: fires when...` inline in prose | `PHASE 2 OUTPUT DECLARATION:` appended in execution body |
| V-02 | C-37 withheld | exits named only, no trigger clauses | same execution-body OUTPUT DECLARATION as V-01 |
| V-03 | C-38 withheld | exits with inline trigger clauses | COMMIT DECISION echo (post-execution, C-38 FAIL) |
| V-04 | Lifecycle GUARD form | GUARD contract entries carry trigger clauses | `PHASE 2 OUTPUT DECLARATION:` in execution section (below contract header) |
| V-05 | Lifecycle + elevated block | GUARD entries with trigger clauses | `+-- PHASE 2 OUTPUT DECLARATION --+` titled box in execution body |

**Key isolation tests:**
- **V-01 vs V-02** (C-37 isolation): preamble trigger sentences (C-35) are present in both -- C-37's GUARD-site co-location is independently necessary.
- **V-01 vs V-03** (C-38 isolation): C-36 is PASS in V-03 via COMMIT DECISION echo -- execution-body residency is independently necessary beyond C-36's minimum-sufficient third-site requirement.
- **V-01 vs V-04** (C-37 form-agnosticism): execution-prose vs GUARD-contract-field exit form.
- **V-01/V-04/V-05** (C-38 block-form): inline-appended label vs titled box; uniform 245 predicted if C-38 is form-agnostic within execution-body-resident forms.
