Written to `simulations/quest/rubrics/quest-variate-rubric-v9-R9-2026-03-15.md`.

---

## R9 Variations Summary

**New structural element: Rubric Propagation Contract** — a labeled block in the role definition specifying what every generated rubric body must ensure its outputs contain. This is the single axis point for all 5 variations.

| V-ID | Axis | What changes in the Contract | What it measures |
|------|------|------------------------------|------------------|
| V-01 | Baseline | Dual-path hook + Phase 0 gate + rejection >= 3 + "or equivalent block" | R9 full-stack ceiling |
| V-02 | Evolution hook -- version-field ablation | Notes-trigger only; no `Version: N` field | Notes path alone: C-29 PASS, C-10 single-point-of-failure |
| V-03 | Evolution hook -- notes-trigger ablation | Version field only; no notes trigger | Version path alone: C-29 N/A, confirms v10 candidate gradient |
| V-04 | Lifecycle -- Phase 0 gate ablation | "analyze the skill" replaces failure-mode enumeration | C-30 ablation: does removing Phase 0 degrade C-04/C-08? |
| V-05 | Output format -- rejection log count | Rejection log >= 5 (up from >= 3) | `rejection-log-minimum-count-scales-with-aspirational-depth` |

**Evidence ladder for `evolution-hook-dual-path-confirmation`** (the v10 candidate that explicitly requested R9 ablation):
- V-03: version-field only → C-29 N/A (no trigger event in notes) = single-point-of-failure confirmed
- V-02: notes-only → C-29 PASS, C-10 via notes = other single-point-of-failure
- V-01: dual-path → both satisfied simultaneously = structural ceiling

**New checkpoint row** added to Phase 2: `Rubric Propagation Contract present` — ensures the Contract doesn't silently drop between variations under token pressure.
