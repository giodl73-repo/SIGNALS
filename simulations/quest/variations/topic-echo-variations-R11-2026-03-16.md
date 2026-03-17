Written to `simulations/quest/golden/topic-echo-variate-R11-2026-03-16.md`.

---

## Round 11 Variations: `topic:echo` -- v11 rubric (max 230)

**Three variation axes** (one per new v11 criterion):

| Axis | Targets | Implementation |
|------|---------|----------------|
| **A -- Lifecycle Emphasis** | C-34 | BC Step 1 split into `[SCAN]` / `[FREEZE]` / `[COVERAGE AUDIT]` sub-phases; BC-COVERAGE-RECORD is the `[COVERAGE AUDIT]` gate return, not an appended block |
| **B -- Output Format** | C-35 | PHASE-HANDOVER-EF and PHASE-HANDOVER-BC rendered as 5-row markdown tables (| Field | Value |), not code-block protocol declarations |
| **C -- Phrasing Register** | C-36 | STILL-LIVE FILTER rewritten as 4 unconditional imperative commands: evaluate, draft-if-qualifies, write-DISCARD-if-not, write-DISCARD-LOG-COMPLETE |

**Scoring profile:**

| Variation | Axis | C-34 | C-35 | C-36 | v11 |
|-----------|------|:----:|:----:|:----:|:---:|
| V-01 | A only | PASS | FAIL | FAIL | 220 |
| V-02 | B only | FAIL | PASS | FAIL | 220 |
| V-03 | C only | FAIL | FAIL | PASS | 220 |
| V-04 | A + B | PASS | PASS | FAIL | 225 |
| **V-05** | A + B + C | PASS | PASS | PASS | **230** |

**Key discriminants from R10:** R10 used appended blocks (BC-COVERAGE-RECORD bolted after PBI), code-block tokens (PHASE-HANDOVER in `-----` format), and conditional branching (`YES -> draft. NO -> write DISCARD`). R11 replaces each with a structurally distinct implementation: sub-phase lifecycle gating, table-format tokens, and imperative grammar respectively. The **implementation-robustness thesis**: if V-05 scores 230, C-34/C-35/C-36 are satisfiable by multiple prompt strategies -- the criteria are not implementation-specific.
