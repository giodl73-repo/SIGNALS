---

## Round 12 — Variation Axes

All 5 variations carry the full v11 baseline (C-01 through C-48).

### Axes explored

**Single-axis (3):**

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | **Lifecycle emphasis — Remediation Planner role** | A 5th role (REMEDIATION PLANNER) runs after AUDITOR certification. Reads EXECUTION_HALT blocks and Phase 3-E ENTANGLEMENT_MAP to produce a topologically sorted REMEDIATION_PLAN: PLAN_ITEMs with DEPENDENCY_CHAIN ordering and PLAN_TIER (IMMEDIATE / NEXT_SPRINT / BACKLOG). Phase 6-H PLAN_INTEGRITY_AUDIT verifies every EXECUTION_HALT block is represented and every CHAIN_REPAIR CONV-NN is in scope. |
| V-02 | **Output format — Turn Prediction Contract** | Topology Architect pre-declares TURN_PREDICTION_CONTRACT (Phase 0-A-10): HAPPY_PATH + up to 3 ALT_PATHs with PATH_CRITICALITY. Phase 1 gains PREDICTION_MATCH column. PREDICTION_DEVIATION is the 9th structural defect class. CRITICAL path deviations auto-elevate to P1 minimum. PATH_ADHERENCE_RATIO is the 5th coverage ratio. Phase 6-H PATH_ADHERENCE_AUDIT closes the loop. |
| V-03 | **Phrasing register — Imperative second-person** | Identical v11 structure rewritten in imperative second-person ("You will declare...", "Emit an EXECUTION_HALT block...", "Do not leave any turn without..."). No structural changes. Tests whether directive register reduces hedging and improves per-phase execution fidelity. |

**Combined (2):**

| V | Axes | Hypothesis |
|---|------|------------|
| V-04 | **D + E** | Remediation Planner + Turn Prediction Contract. CRITICAL_PATH deviations carry PLAN_TIER_OVERRIDE: IMMEDIATE, ensuring path breaks receive the same urgency as P0s without manual adjudication. Phase 6-H merges plan integrity and path adherence verification into one Auditor phase. |
| V-05 | **E + inertia extension** | Turn Prediction Contract + STATUS_QUO_SIMULATION (Phase 4-SQ). Developer re-runs the scenario using only the declared STATUS_QUO_METHOD (Phase 0-A-11) — abbreviated trace, no CONSTRAINT_VERDICTS / CHAIN_EFFECTS / PREDICTION_MATCH. Phase 5-F STATUS_QUO_COVERAGE table replaces simple SIMULATION_DELTA: each defect is matched against the method's declared blind spots with automatic structural proofs (PREDICTION_DEVIATION defects are structurally FOUND_BY_SIMULATION_ONLY when the method doesn't consult path contracts). |

---

**Candidate v12 criteria extracted from these variations:**

| ID | Source | What it captures |
|----|--------|-----------------|
| C-49 | V-01 | REMEDIATION_PLANNER role emits topologically sorted REMEDIATION_PLAN after Auditor certification |
| C-50 | V-01 | DEPENDENCY_CHAIN topological sort in REMEDIATION_PLAN — no PLAN_ITEM precedes its dependency |
| C-51 | V-01 | PLAN_TIER classification (IMMEDIATE/NEXT_SPRINT/BACKLOG) with TIER_RATIONALE |
| C-52 | V-01 | Phase 6-H PLAN_INTEGRITY_AUDIT — every EXECUTION_HALT block has a PLAN_ITEM; every CHAIN_REPAIR CONV-NN in scope |
| C-53 | V-02 | TURN_PREDICTION_CONTRACT in Phase 0-A-10 — paths declared before tracing |
| C-54 | V-02 | PREDICTION_MATCH column in Phase 1 — ON_PATH vs DEVIATION per turn |
| C-55 | V-02 | PREDICTION_DEVIATION as 9th structural defect class with DEVIATION_IMPACT and auto-escalation |
| C-56 | V-02 | PATH_ADHERENCE_RATIO as 5th coverage ratio |
| C-57 | V-02 | Phase 6-H PATH_ADHERENCE_AUDIT |
| C-58 | V-05 | STATUS_QUO_METHOD declaration in Phase 0-A-11 with METHOD_BLIND_SPOTS |
| C-59 | V-05 | Phase 4-SQ STATUS_QUO_SIMULATION abbreviated parallel trace |
| C-60 | V-05 | Phase 5-F STATUS_QUO_COVERAGE table with structural blind-spot proofs per defect |

**Files:**
- Variations: `simulations/quest/variations/flow-conversation-variations-R12-2026-03-15.md`
- Full prompt bodies: `simulations/quest/rubrics/flow-conversation-rubric-v11-variations-R12-2026-03-15.md`
