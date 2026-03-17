Written to `simulations/quest/rubrics/draft-spec-rubric-v8-variate-R8-2026-03-15.md`.

---

## Axis Map

| | Variation | Axis | Base | Hypothesis |
|---|---|---|---|---|
| V-01 | C-26 single | Branch B → 4 per-artifact sub-conditions (B-1 feasibility-only, B-2 compliance-only, B-3 both, B-4 catch-all) + anti-blend instruction | v7 V-01 minimal (merged INERTIA-TABLE, REQUIRES/PRODUCES/BLOCKS) | C-26 passes independently of C-22/C-23/C-24 |
| V-02 | C-27 single | Imperative actor-action-output directives throughout; REQUIRES/PRODUCES/BLOCKS absent | v7 V-03 INTAKE structure (split registers, no C-26) | C-27 passes without subdivided Branch B; phrasing axis is independent |
| V-03 | Role sequence single | Phase 1 (PM pre-assignment) runs **before** Phase 0B (inertia analysis); inertia guards can reference pre-assigned requirement IDs in Elimination Path | v7 V-05 full-combination (REQUIRES/PRODUCES/BLOCKS) | Reordering doesn't break any v7 criteria; guards gain precision from named requirement IDs |
| V-04 | C-26 + C-27 combined | B-1/B-2/B-3/B-4 VERBATIM sub-conditions + imperative phrasing throughout | v7 V-05 + both new axes | Non-interacting: C-26 adds Phase 0 copy, C-27 changes register in all other phases; combined should satisfy all 27 v8 criteria |
| V-05 | Full combination | All three axes: C-26 + C-27 + PM-first phase order | v7 V-05 + all three axes | Target 175/175 — PM-first strengthens IG guard Elimination Paths, C-26 discriminates sub-scenarios, C-27 applies uniformly |

**New v8 structural decisions:**
- C-26 Branch B priority rule: B-3 > B-2 > B-1 > B-4 (avoids ambiguity when multiple sub-conditions could fire)
- C-27 implementation: every role-phase block gets `"Actor: scan Source → fill Target"` form; `REQUIRES/PRODUCES/BLOCKS` headers absent
- V-03/V-05 PM-first ordering: `[PM-CONTRACT-SEAL]` gates `Phase 0B` (not the other way around), so inertia guards can see `[PM-COVERAGE-TABLE]` before authoring Elimination Paths
