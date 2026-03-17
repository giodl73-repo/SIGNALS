Here is the complete v11 rubric. Summary of what changed:

---

**11 new aspirational criteria, C-38 through C-48 (+28 pts). Max score: 156 → 184.**

| ID | What it captures | Wt | Source |
|----|------------------|----|--------|
| C-38 | P0 EXECUTION_HALT block — per-P0 inline remediation prescription (HALT_TRIGGER, ROOT_CAUSE, MVF_RECOMMENDATION, MVF_SCOPE, UNBLOCKED_BY) immediately after each P0 classification | 3 | V-01, V-04 |
| C-39 | Phase 6-F Fix Viability Audit — Auditor verifies MVF addresses HALT_TRIGGER and does not introduce new CONV-NN violations; VIABLE\|SIDE_EFFECTS_FOUND verdict per block | 2 | V-01, V-04 |
| C-40 | PROPAGATION + CHAIN_ID in Phase 0-A-7 — transforms per-turn binary verdicts into a compositional proof system; CHAIN_SUSPENDED status when chain head DEVIATES | 4 | V-02, V-04, V-05 |
| C-41 | CHAIN_EFFECTS column in Phase 1 — per-turn downstream ACTIVATED\|SUSPENDED effects per CONV-NN evaluated | 2 | V-02, V-04, V-05 |
| C-42 | Phase 5 Constraint Chain Status Summary — one row per CHAIN-NN: HEAD_CONV, CHAIN_LENGTH, TURNS_SUSPENDED, FINAL_STATUS: INTACT\|BROKEN | 2 | V-02, V-04, V-05 |
| C-43 | Phase 6 Chain Integrity Audit — verifies CHAIN_EFFECTS against upstream verdicts; flags downstream CONFORMS during SUSPENDED window as CHAIN_VERDICT_INCONSISTENCY | 3 | V-02, V-04, V-05 |
| C-44 | CHAIN_BREAK_TRACE + CHAIN_REPAIR in EXECUTION_HALT — causal chain break path + re-evaluation list; additive to C-38 and C-40; closes P0 halt into a causally complete remediation record | 2 | V-04 |
| C-45 | DEVIATION_BUDGET pre-execution declaration — locked P0/P1/P2/P3 max thresholds before Phase 1-S; may not be revised after tracing begins | 3 | V-03 |
| C-46 | Phase 5 DEVIATION_BUDGET_UTILIZATION gate — actual vs budget per severity; BUDGET_EXCEEDED finding before coverage ratios; Phase 6-A BUDGET_UTILIZATION_VERIFIED | 2 | V-03 |
| C-47 | CONV_CHAIN_BUDGET Phase 0-A-9 — per-chain budget declaration; CA extended to CHAIN_BUDGET_DELTA; both deltas must be empty for PASS | 3 | V-05 |
| C-48 | CHAIN_BUDGET_EXCEEDED as 8th structural finding class — chain-level utilization block; CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY and EXEMPT from co-residency audit; Phase 6 CHAIN_BUDGET_AUDIT | 2 | V-05 |

**C-34 pass condition updated** — "Phase 5-A" label replaced with "structurally prior to coverage ratios"; a pre-committed budget block (C-46 or C-48) legitimately displaces COVERAGE_QUALITY_GATE from the first sub-phase position. Under v11, V-03 and V-05 would score C-34 as PASS.

**Cluster structure:**
- C-38/C-39 — P0 halt gate + fix viability (remediation prescription loop)
- C-40/C-41/C-42/C-43 — constraint chain propagation (compositional proof system)
- C-44 — merges both clusters into one causally complete EXECUTION_HALT record
- C-45/C-46 — deviation budget (pre-execution quality commitments by severity)
- C-47/C-48 — chain budget (domain-meaningful commitments by named constraint chain)
