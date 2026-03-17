Here are the 5 Round 11 variations for `flow-conversation` against the v10 rubric:

---

## Round 11 — Variation Axes

All 5 variations carry the full v10 baseline as given: mutation-first authoring (C-30), AUTHORIZED_REWRITERS (C-31), Contract Auditor pre-execution gate (C-32/C-33), COVERAGE_QUALITY_GATE (C-34), SIMULATION_DELTA (C-35), CONSTRAINT_VERDICTS with CONV-NN IDs (C-36), and arithmetic evidence (C-37).

### Axes explored

**Single-axis (3):**

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | **Lifecycle emphasis — P0 Execution Halt Gate** | Forcing an `EXECUTION_HALT` block with `MVF_RECOMMENDATION` after each P0 defect changes the artifact from a passive catalog to an active remediation prescription. Phase 6-F `FIX_VIABILITY_AUDIT` closes the loop by checking whether the fix would introduce new CONV-NN violations. |
| V-02 | **Output format — Constraint Chain Propagation** | Each CONV-NN declares a `PROPAGATION` list of downstream constraints whose evaluation depends on its `POST_VALUE`. Phase 1 adds a `CHAIN_EFFECTS` column. Phase 6-F `CHAIN_INTEGRITY_AUDIT` verifies that no downstream constraint shows CONFORMS during a SUSPENDED chain window — surfacing constraint causality that per-turn binary verdicts miss. |
| V-03 | **Inertia framing — Pre-committed Deviation Budget** | Developer declares `DEVIATION_BUDGET` (P0/P1/P2/P3 max allowed) in Phase 0 before tracing. Phase 5-A reports `BUDGET_UTILIZATION` before the quality gate. `BUDGET_EXCEEDED` is emitted as a gate finding — the team's own pre-committed bar was not met, self-justifying the artifact. Auditor verifies accuracy in Phase 6-A. |

**Combined (2):**

| V | Axes | Hypothesis |
|---|------|------------|
| V-04 | **A + B** | A P0 defect is most actionable with its causal chain visible. Each `EXECUTION_HALT` block extends to a `CHAIN_BREAK_TRACE` citing the broken `CHAIN-NN`, the first `TURN_ID` where the head CONV-NN deviated, which downstream constraints were suspended, and a `CHAIN_REPAIR` list the MVF must address. |
| V-05 | **B + C** | Per-chain budgets are more domain-meaningful than per-severity budgets. Each `CHAIN-NN` gets its own `CHAIN_BUDGET` declared by the Topology Architect in Phase 0-A-9. `CHAIN_BUDGET_EXCEEDED` becomes the **8th structural finding class**. The Contract Auditor gate (Phase 0-CA-1) is extended to verify that every chain in the topology has a budget entry. Phase 6-F `CHAIN_BUDGET_AUDIT` + Phase 6-G `CHAIN_INTEGRITY_AUDIT` close the loop. |

Saved to `simulations/quest/rubrics/flow-conversation-rubric-v10-variations-R11-2026-03-15.md`.
