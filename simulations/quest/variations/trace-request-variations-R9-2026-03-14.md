Written to `simulations/quest/rubrics/trace-request-rubric-v8-R9-2026-03-15.md`.

---

# trace-request rubric v8 -- Skill Body Prompt Variations R9

## Variation Summary

| V | Axis | Key change | C-24 | C-25 | New signal | Predicted |
|---|------|-----------|------|------|------------|-----------|
| V-01 | Phrasing register: C-24 advisory | Step 10b cross-check table softened to suggestion; gate summary (C-22) still required | FAIL | PASS | none | 175/180 |
| V-02 | Phrasing register: C-25 advisory | Step 8a scope enumeration table softened to suggestion; re-walk findings (C-11) still required | PASS | FAIL | none | 175/180 |
| V-03 | Lifecycle emphasis: scope-gap Rem# propagation | Step 8b requires every Gap?=Y row to cite a dedicated Rem# in Step 11 with exact scope string parameter | PASS | PASS | **C-26a**: scope-gap entries traceable to Rem# | 180/180 |
| V-04 | Output format: vocabulary conformance gate | New Step 3a after traversal: VT# terms from Step 0 cited at Step 3 cells; D deviations integer; D>0 is a correction block | PASS | PASS | **C-26b**: vocabulary conformance computable | 180/180 |
| V-05 | Two-axis combination (V-03 + V-04) | Both scope-gap Rem# propagation and vocabulary conformance gate | PASS | PASS | Both candidates + ES-3 speculative | 180/180 |

---

## What's new in R9 vs R8

**R8 introduced** C-24 (cross-check table backing the gate integers) and C-25 (per-boundary scope enumeration table before re-walk). R8 V-05 body is the baseline for all five R9 variations.

**R9 regression tests (V-01, V-02)**: If either softened variation still scores 180, the DISQUALIFIER wording in the rubric needs hardening. The test validates that both new criteria are load-bearing before building above them.

**Two new candidate axes**:

- **V-03 / C-26a — scope-gap Rem# propagation**: The C-25 scope table already forces `Gap? = Y` entries to be named. V-03 extends the contract: each `Gap? = Y` row must cite a `Rem#` in Step 11 carrying the exact scope string as the `Permission Fix` parameter. This creates a three-structure cross-link: Step 8a → Step 11 → Steps 7/9. ES-3 from R8 is now a concrete testable path rather than speculative.

- **V-04 / C-26b — vocabulary conformance gate**: C-02 already requires vocabulary commitment at Step 0. V-04 forces a structured conformance check at Step 3a — a table mapping each `VT#` term to the Step 3 cell(s) where it appears verbatim, with a `D` integer counting deviations. `D > 0` is a correction block, not a note. This makes the C-02 binding verifiable rather than narrative.

**V-05 combines both**: If it produces responses satisfying all C-01–C-25 plus both new structural properties, that establishes the two criteria for v9. The speculative ES-3 (scope-gap three-way cross-link: Step 8a → Step 11 → Step 7/9 Rem# citation) is possible if the scope-gap `Rem#` from V-03 happens to be the same `Rem#` cited at a divergence boundary in Step 7.
