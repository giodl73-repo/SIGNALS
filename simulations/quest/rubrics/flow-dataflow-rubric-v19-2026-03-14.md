Here is the complete updated rubric — key changes from v18:

**Changelog entry (v19)**
> Added C-54..C-55 from R19 excellence signals: Phase Gate 0 multi-item structural completeness gate enforcing one item per [A-00] structural dimension, SC-0 as mandatory [A-00] governor with dual-slot anchoring maintained across all [A-00]-governing SCs

**C-54 — Phase Gate 0 multi-item structural completeness gate** (`behavior`)
Each structural dimension of [A-00] maps to a distinct checklist item in Phase Gate 0. A single-item gate (row count only) fails if [A-00] has additional declared dimensions (e.g., non-empty Responsible Role column). Fewer items than dimensions = FAIL.

**C-55 — SC-0 as mandatory [A-00] governor with per-SC dual-slot anchoring** (`format`)
Every prompt with [A-00] must include SC-0 governing [A-00] with dual-slot anchoring. When additional SCs govern [A-00] structural dimensions (e.g., SC-14 governing a column), each must independently carry `[A-00]` in both governed-artifact and enforcement slots — SC-0 does not supply the reference for the others.

**Weight adjustment**: 46 → 48 criteria, 10/48 ≈ **0.208 pts** per criterion (PARTIAL ≈ 0.104 pts).
