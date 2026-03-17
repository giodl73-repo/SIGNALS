Written to `simulations/quest/golden/campaign-track-variate-R6-2026-03-16.md`.

**Round 6 summary:**

R3 closed C-14/C-15/C-16 (prohibition lists, typed contracts, terminal checklist). The R6 rubric adds three refinements from scorecard excellence signals:

| Criterion | What changed | Bar raised from |
|-----------|-------------|----------------|
| **C-22** | Prohibition-count parity | "at least 1" per role → exactly 5, symmetric, auditable by count alone |
| **C-23** | Full-phase type coverage | "at least 2 phases typed" → all 4 phases, partial coverage declared invalid |
| **C-24** | Terminal checklist quality | Phase-level postconditions → 22 named field-level items, each independently verifiable with FAIL action |

**Five variations:**

- **V-01** -- Parity rule axis only (C-22): explicit symmetry declaration, numbered 1-5, structural invalidity of deviations called out
- **V-02** -- Full-phase typing axis only (C-23): all 4 phases typed, "partial coverage fails" as invariant
- **V-03** -- Field-level checklist axis only (C-24): 22 items, each names a specific artifact field with its type/value constraint and targeted FAIL action
- **V-04** -- C-22 + C-23 combined: active-role annotation repeats both rules at point of execution
- **V-05** -- Full stack C-22 + C-23 + C-24 + lifecycle emphasis: covers all 19 criteria; three structural rules kept salient via active-role annotations at each phase header

Predicted leaderboard: **V-05 > V-04 > V-03 > V-01 >= V-02**.
