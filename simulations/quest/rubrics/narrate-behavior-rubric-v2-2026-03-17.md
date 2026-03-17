Written to `simulations/quest/rubrics/narrate-behavior-rubric-v9-2026-03-17.md`.

**Three R8 excellence signals codified as C-29 / C-30 / C-31:**

| Criterion | Pattern | Source | Key rule |
|-----------|---------|--------|----------|
| C-29 -- Inertia Surface as Pre-Simulation Structural Artifact | `inertia-surface-as-pre-simulation-artifact` | R8 SIGNAL-1 (V-38, V-40) | Pre-S1 compilation step assigns A-NN IDs to all anticipated inertia assumptions before any section executes; REPORT REQUIRE checks catalog coverage by count |
| C-30 -- Assumption Catalog Reconciliation as Report Arithmetic | `assumption-catalog-reconciliation-as-report-arithmetic` | R8 SIGNAL-2 (V-38, V-40) | REPORT block with three labeled fields: A-NNs-total / A-NNs-assigned / unassigned; REQUIRE: unassigned = 0; promotes C-24 prose obligation to verifiable equation |
| C-31 -- Assumption Conservation Equation in Report | `assumption-conservation-equation-in-report` | R8 SIGNAL-3 (V-39, V-40) | N_finding + N_covered + N_investigation + N_none = N_total; residual check against INERTIA SURFACE catalog; strongest C-28 realization — all dispositions partition the catalog arithmetically |

**Aspirational tier**: 24 criteria (C-08 -- C-31), cap 10, threshold: **any 12 of 24**.

Structural note on C-29 / C-30 / C-31 dependency: C-30 requires C-29 (needs a catalog baseline); C-31 requires C-29 (needs the catalog total for residual check) and C-24 (needs four dispositions defined). A variation can pass C-29 alone, C-29+C-30 without C-31, or all three — they compose additively toward threshold.
