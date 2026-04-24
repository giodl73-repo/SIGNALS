Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v16-variate-R16-2026-03-15.md`.

**Summary of R16 variations:**

| Variation | Axis | Targets | Expected |
|-----------|------|---------|----------|
| V-01 | Role sequence | None (R15 V-05 baseline) | 39/42 or 42/42 |
| V-02 | Output format | C-49 (EXCEPTION BLOCK ARCHITECTURE header) | 40/42 |
| V-03 | Lifecycle emphasis | C-50 (DIRECTION INVENTORY at CHAIN STATUS opening) | 40/42 |
| V-04 | Inertia framing | C-48 (Phase Refs per IM-ID + Phase->Baseline direction) | 40/42 |
| V-05 | All three | C-48 + C-49 + C-50 | 42/42 |

**Design decisions:**

- V-01 is intentionally the reliability test for R15 V-05 implicit scoring. If it scores 42/42, R16 adds zero structural risk. If it scores 39/42, the three single-axis variations isolate which explicit additions are load-bearing.
- C-48 lives entirely in INCUMBENT BASELINE (Phase Refs annotations) + one new CHAIN STATUS direction (`Phase->Baseline`). No phase structure changes needed.
- C-49 is a pure format criterion -- it adds a header table before the EX block template, adds zero new sub-fields, and explicitly binds the three already-present sub-fields into a declared architectural unit.
- C-50 is also a pure format criterion -- the DIRECTION INVENTORY table lives at CHAIN STATUS opening and enumerates exactly the four directions named in the rubric by their canonical string labels.
- All three additions are architecturally isolated and compose cleanly in V-05.
