Written to `simulations/quest/golden/crew-roles-variate-R13-2026-03-17.md`.

---

## crew-roles — Variate R13 Summary

**Baseline**: R12 V-05 (100/100 on v6; already implements C-26 and C-27 now in v7).

**Two new excellence signals identified from R12 V-05**:

**ES-1 — Annotation validates term metadata but not term presence in question body**
CHECK 6's four failure modes (MISSING ANNOTATION, Q-NUMBER MISMATCH, TERM MISMATCH, ROW-ID MISMATCH) all operate on the annotation tag. A question like `"Is the system resilient?" [Q: Q2 — vocab: MC-1 — re-routing-cost]` passes all four: the annotation is present, Q-number is correct, term matches Phase 2, row-id matches. But "re-routing-cost" never appears in the question text — the annotation asserts a grounding the body does not demonstrate. A fifth failure mode `[TERM NOT IN QUESTION TEXT]` makes the annotation a content constraint, not merely metadata.

**ES-2 — Scope planning table and written scope are independently authored, never compared**
Phase 5 plans scope values; Phase 7 CHECK 3 confirms a gradient exists (>=2 distinct values). But CHECK 3 asks "does the set of written values have diversity?" — not "does each written value match its plan?" A role planned as `team` can silently become `cross-team` during Phase 6 writing without CHECK 3 detecting it (gradient still exists). A SCOPE BINDING sub-check (CHECK 3B) compares Phase 5 planned scope to Phase 6 written scope row-by-row, flagging `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]`.

**Variation axes**:

| V | Axis | Key mechanism |
|---|------|---------------|
| V-01 | Term-in-body enforcement | CHECK 6 fifth failure mode `[TERM NOT IN QUESTION TEXT]` |
| V-02 | Scope binding check | CHECK 3B row-by-row Phase 5 planned vs Phase 6 written scope |
| V-03 | Convergence summary | Phase 2 closes with `Q1-FINAL/Q2-FINAL/Q3-FINAL` named block; Phase 3+6 consume from it, not iteration log |
| V-04 | ES-1 + ES-2 | term-in-body + scope binding combined |
| V-05 | ES-1 + ES-2 + convergence summary | full three-axis synthesis |
