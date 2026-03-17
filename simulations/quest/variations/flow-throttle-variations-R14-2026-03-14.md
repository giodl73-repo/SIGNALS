Written to `simulations/quest/rubrics/flow-throttle-rubric-v14-variations-R14-2026-03-15.md`.

---

## R14 Variations — flow-throttle (v14 Rubric, 190-point max)

**Predicted scores (all 190/190 under v14):**

| Variation | Axis | C-39 | C-40 | Score |
|-----------|------|------|------|-------|
| V-01 | Role sequence: Round-1 `*Lead analyst: Throttle capacity modeler.*` before Phase 0 | PASS | PASS | 190 |
| V-02 | Output format: Phase-0 TABLE expanded to 5 cols (PA type + `→ TABLE 1 row`) | PASS | PASS | 190 |
| V-03 | Phrasing register: directive imperative throughout; new subtitles "Throttle Baseline" / "Bottleneck Correction Registry" / "Limit Source Verification" / "Limit source verifier" | PASS | PASS | 190 |
| V-04 | Combination: Round-1 role label + prominent inertia framing (status-quo row in TABLE 0) | PASS | PASS | 190 |
| V-05 | **Ceiling:** `### PRE-ANALYSIS SCENARIO MODEL (before any Phase 1 bottleneck analysis begins)` container within Round 1, with scope/independence declarations and `*Lead analyst: Throttle scenario modeler.*` | PASS | PASS | 190 |

**Design rationale:**

C-40 becomes uniform in R14 — all five variations carry a Phase 0 TABLE. This confirms C-40 as a stable property independent of role sequence, TABLE schema depth, phrasing register, inertia depth, or container structure.

**V-05 ceiling discovery:** The `PRE-ANALYSIS SCENARIO MODEL` container at Round 1 introduces two new structural anchors that parallel C-31 (mechanism-type container) and C-37 (evaluator-role label) at Round 2:
- A **Round-1 container with mechanism-type declaration** ("SCENARIO MODEL")
- A **Round-1 evaluator-role label** (`*Lead analyst: Throttle scenario modeler.*`)

These constitute potential **C-41** and **C-42** candidates — the same structural pattern as C-31/C-37 applied symmetrically at Round 1. If independently confirmable in R15 (container without role label, role label without container), they become separate criteria. If always co-occurring, they become a conjunction criterion analogous to C-39.

**Notable secondary findings in this round:**
- V-02's `→ TABLE 1 row` forward-reference column tests whether Phase 0 TABLE cross-phase traceability is distinct from C-40's minimum encoding requirement — potential C-41 candidate separate from V-05's discovery
- V-03 confirms "Throttle Baseline" (C-35), "Bottleneck Correction Registry" (C-36), and "Limit Source Verification" / "Limit source verifier" (C-32/C-37/C-38) as additional confirmed passing forms, extending the subtitle-text inertness evidence base
