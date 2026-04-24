Rubric written to `simulations/quest/rubrics/org-rob-rubric-v1-2026-03-16.md`.

**10 criteria across 3 tiers:**

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | essential | format |
| C-02 | Role-loaded perspective (from .roles/) | essential | correctness |
| C-03 | ROB document format compliance | essential | format |
| C-04 | Actionable findings (>=2 per stage run) | essential | depth |
| C-05 | Explicit go/no-go in tpm stage | essential | correctness |
| C-06 | Cross-stage coherence (escalation chain visible) | recommended | depth |
| C-07 | Risk register structure in tpm | recommended | depth |
| C-08 | Spire cascade tracing (mission->artifact link) | recommended | coverage |
| C-09 | Inter-stage blocker detection | aspirational | depth |
| C-10 | Cross-cutting theme elevation | aspirational | depth |

**Design decisions:**
- C-02 targets the core differentiator of org-rob: roles loaded from `.roles/` must visibly shape findings, not produce generic output any reviewer would write
- C-05 is essential (not just recommended) because the go/no-go is the whole point of a tpm stage — an implicit verdict defeats the governance purpose
- C-07 and C-08 are recommended because they only apply to specific stages (`tpm`, `spire`); making them essential would penalize single-stage runs that don't invoke those stages
- C-10 is aspirational because cross-cutting detection requires running 3+ stages with overlapping concerns — not achievable until the basic multi-stage format is stable
