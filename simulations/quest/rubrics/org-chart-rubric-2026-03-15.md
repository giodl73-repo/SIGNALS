Rubric written to `simulations/quest/rubrics/org-chart-rubric-v1-2026-03-15.md`.

**5 essential / 3 recommended / 2 aspirational** — key design decisions:

- **C-01 (inertia assessment) is the gate** — it's the defining principle of the skill. A run that skips it fails regardless of how good the org boxes look.
- **C-03 (roles input honored)** has a split pass condition — behavior differs when `.craft/roles/` is populated vs. absent, so the evaluator must check run context first.
- **C-05 (operating rhythm table)** sets a floor of three distinct entries (ROB + shiproom + governance) to prevent a single-entry table from passing.
- **C-06 (committee charters)** is recommended, not essential — a minimal org chart without charters is still useful; charters make it good.
- **C-09/C-10 (evolution path / anti-patterns)** are fully independent aspirational items — either can pass without the other.
