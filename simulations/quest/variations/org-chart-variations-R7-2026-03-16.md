**org-chart Variate -- Round 7 (Rubric v7 / C-25 + C-26)**

Written to `simulations/quest/golden/org-chart-variate-R7-C25C26-2026-03-16.md`

Note: `org-chart-variate-R7-2026-03-16.md` already exists from a parallel rubric lineage (Evolution Roadmap alignment, DRI mandate, row floor). This file uses the `-C25C26` suffix to distinguish.

---

### Variation Map

| V | Axis | New criteria targeted |
|---|------|-----------------------|
| V-01 | Lifecycle emphasis — per-gate `PRODUCES`/`REQUIRES` | C-25 in isolation |
| V-02 | Output format — all-gate `CONTAINMENT CONTRACT` lists | C-26 in isolation |
| V-03 | Phrasing register — systematic `DO` / `DO NOT` throughout | C-14 diagnostic (no C-25/C-26) |
| V-04 | Combined: C-25 + C-26 | Both new criteria simultaneously |
| V-05 | Combined: C-25 + C-26 + DO/DO NOT (full integration) | C-14 + C-25 + C-26 on V-05/R6 base |

---

### Design decisions

**C-25 implementation (V-01, V-04, V-05):** Each gate emits a `GATE N PRODUCES: Ax -- [artifact name]: [description]` block immediately after the STATUS line. Each gate opens with `REQUIRES: Ax -- [artifact name] (produced by GATE N-1)`. The artifact names are pinned (`A0`, `A1`, `A2`, `A3`) and both sides of each handoff use the same label, closing the inference gap that chain-level contracts leave open.

**C-26 implementation (V-02, V-04, V-05):** GATE 1, 2, and 3 each receive a `GATE N CONTAINMENT CONTRACT` with a numbered prohibited-content list before the production steps begin. The lists are gate-appropriate: GATE 1 prohibits diagram/headcount/rhythm/charter + pre-VERDICT structural conclusions; GATE 2 prohibits rhythm/charters + rogue inertia content + GATE 3 prerequisites; GATE 3 prohibits undeclared roles + inertia rows + diagram revisions.

**Bypass surface check:** C-25 and C-26 share no bypass path. A model can satisfy C-25 (name the right artifacts at boundaries) while still producing out-of-order content within a gate — C-26 closes that. A model can satisfy C-26 (enumerate prohibited content per gate) while leaving artifact identity inferential — C-25 closes that. V-04/V-05 require both to be satisfied simultaneously.

**V-03 diagnostic purpose:** If V-03 scores comparably to V-04/V-05 on C-25 and C-26, the rubric criteria are not detecting the structural absence — that would be a rubric gap. If V-03 scores lower on C-25/C-26 specifically (as expected), the criteria are working correctly and the axes are isolated.
