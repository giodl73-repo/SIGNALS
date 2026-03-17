Written to `simulations/quest/golden/file-issue-variate-R4-2026-03-17.md`.

---

## file-issue — Round 4 Variations

**Rubric**: v4 (C-01 through C-15) | **Target**: 8/8 aspirational = 100

**Round 3 gap**: No variation achieved both C-14 (severity-first) and C-15 (macro-phase boundary) simultaneously. V-02 got C-14 via step isolation; V-04 got C-15 via DO NOT BEGIN — but each failed the other.

---

### Variation axes and hypotheses

| | Axis | C-14 | C-15 | Predicted |
|---|---|---|---|---|
| **V-01** | Role sequence: severity-first isolation | PASS — severity alone in Step 1, explicit gate | FAIL — step sequence, not macro-phase | **98.75** |
| **V-02** | Lifecycle: symmetric macro-phase | FAIL — severity in A1 table with other fields | PASS — DO NOT BEGIN instruction | **98.75** |
| **V-03** | Output format: table-driven collection | FAIL — table collects all fields together | FAIL — no macro-phase | **97.5** |
| **V-04** | Combined: role sequence + lifecycle | PASS — severity alone in A1, gates A2+A3 | PASS — two macro-phases, DO NOT BEGIN | **100** |
| **V-05** | Combined: all three axes | PASS — severity gates table load | PASS — two macro-phases, DO NOT BEGIN | **100** |

---

### Key structural decisions

**V-01** uses a step sequence (5 steps) where Step 1 asks for severity alone with the phrase "Do not collect any other field until a valid severity value is confirmed." Steps 2–5 follow after. This isolates C-14 without macro-phase apparatus.

**V-02** uses two symmetric macro-phases (PHASE A: collect+draft, PHASE B: validate+write) with "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE" at the boundary, but collects all four fields together in A1. C-15 achieved, C-14 deliberately absent.

**V-03** introduces a collection table with severity-applicability columns (crash/wrong-output/missing-feature/improvement as column headers), which presents all fields simultaneously. Neither C-14 nor C-15 — serves as a structural baseline for the combined variations.

**V-04** is the primary combined target: PHASE A has three sub-operations (A1: severity alone → A2: severity-gated form → A3: draft with severity template). PHASE B has three (B1: validate → B2: write → B3: offer). Single event (severity confirmation) triggers both form load and phase progression.

**V-05** adds the table-format axis: the intake table only loads after severity is confirmed (A1 → A2 table), so the table format reinforces rather than undermines C-14. Tests whether the three axes are mutually compatible or in tension.
