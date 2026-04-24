Written to `simulations/quest/rubrics/campaign-decide-rubric-v20-2026-03-17.md`.

**Changes from v19 → v20:**

| | v19 | v20 |
|-|-----|-----|
| Aspirational denominator | /41 | /44 |
| Aspirational total pts | 20.5 | 22.0 |
| Max composite | 110.5 | 112.0 |

**Three new criteria extracted from R20:**

**C-50 — Phase gate check status annotation (three-field go/no-go verdict)**
After the C-46 density line, a `Gate check: [min met? Y/N] | [FIDs closed? Y/N] | [Proceed? Y/N]` annotation converts the count comparison into an explicit binary decision. The three fields map individually to C-44 satisfaction, C-36 register closure, and the composite verdict — making phase-ready determination arithmetic-free and body-read-free. Implies C-46.

**C-51 — Recommendation delta sentence after recommendation record table**
A standalone sentence immediately after the Phase 5 recommendation record table names the PRE-COMMITMENT prior, the post-evidence recommendation, and whether the falsification condition was triggered. Converts the C-47 column comparison into a single scannable line. Implies C-47. Parallel to C-35 (hypothesis delta in table form) but at the recommendation level in sentence form.

**C-52 — Phase 3 Inertia Lock-in column**
Adds `Inertia Lock-in (H/M/L)` to the Phase 3 segment table alongside the C-12 Fit Score column, propagating the Phase 1a switching cost concept (C-31) to the market segment level. When C-44 is in effect, the Phase 3 `[min: ...]` annotation updates to name both dimensions. Implies C-12; independent of C-31 (which operates at competitor level).
