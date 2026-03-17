5 complete variations written to `simulations/quest/golden/topic-plan-variate-R20-2026-03-15.md`.

---

## Round 20 Variations Summary

**New criteria targeted** (v19 rubric):
- **C-62** — INERTIA-GATE block definition enumerates its own reproduction sites
- **C-63** — Null declarations are type-labeled (`ADDITIONS: none — inertia holds...`)
- **C-64** — "Inertia Rejected Because [REQUIRED]" column symmetric across ALL change-type tables

| | Axis | C-62 | C-63 | C-64 |
|---|---|:---:|:---:|:---:|
| **V-01** | Inertia framing | YES | — | — |
| **V-02** | Output format (split tables) | — | — | YES |
| **V-03** | Phrasing register (typed nulls) | — | YES | — |
| **V-04** | Combination | YES | YES | — |
| **V-05** | Full combination | YES | YES | YES |

**Key design decisions:**

- **V-02** renames the justification column from "Why this beats NO CHANGE" to "Inertia Rejected Because [REQUIRED]" — the `[REQUIRED]` label in the column header itself is part of the enforcement contract
- **V-02** adds **Rule 5** to the COLUMN CONTRACT specifying the symmetry requirement across tables
- **V-04 is the discriminating case for C-64** — it has C-62 + C-63 but a single proposals table, so REMOVE/REPRIORITIZE rows have no per-type inertia justification enforcement
- **V-01** adds [INERTIA-GATE] at Step 6 (diff step), expanding from 3 to 4 reproduction sites
- **Predicted structural risk**: V-05 > V-02 > V-04 > V-01 > V-03
