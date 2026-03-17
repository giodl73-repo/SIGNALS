Here is the complete v12 rubric. Summary of what changed:

---

**10 new aspirational criteria, C-49 through C-58 (+28 pts). Max score: 184 → 212.**

| ID | What it captures | Wt | Source |
|----|------------------|----|--------|
| C-49 | REMEDIATION PLANNER role (Phase 7) — 5th role after Auditor; topologically sorted REMEDIATION_PLAN with one PLAN_ITEM per FOUND defect; DEPENDENCY_ON from ENABLES entanglement; PLAN_TIER by severity; PLAN_SUMMARY with cycle check | 4 | V-01, V-04 |
| C-50 | Phase 6-H PLAN_INTEGRITY_AUDIT — every EXECUTION_HALT block represented in plan; every CHAIN_REPAIR CONV-NN in scope; DEPENDENCY_ORDER_VALID per item; DEPENDENCY_CYCLE_CHECK | 2 | V-01, V-04 |
| C-51 | Phase 0-A-10 TURN_PREDICTION_CONTRACT — HAPPY_PATH + up to 3 ALT_PATHs; PATH_ID, PATH_CRITICALITY, PREDICTED_TURN_SEQUENCE; TURN_PREDICTION_CONTRACT_SIGNED: YES; Contract Auditor verifies before Phase 1 | 3 | V-02, V-04, V-05 |
| C-52 | PREDICTION_MATCH column in Phase 1 (ON_PATH / DEVIATION / OFF_ALL_PATHS) + PATH_IDS_MATCHED in Phase 1-T + PREDICTION_DEVIATION as 9th defect class with DEVIATION_IMPACT, PATH_CRITICALITY, CRITICAL auto-elevation to P1 minimum | 4 | V-02, V-04, V-05 |
| C-53 | PATH_ADHERENCE_RATIO = turns_on_any_path / total_turns as 5th coverage ratio; Phase 6-H PATH_ADHERENCE_AUDIT with per-turn PREDICTION_MATCH verification, PATH_ADHERENCE_RATIO_VERIFIED, CRITICAL_PATH_ESCALATION_VERIFIED | 2 | V-02, V-04, V-05 |
| C-54 | PLAN_TIER_OVERRIDE: IMMEDIATE on CRITICAL-path PREDICTION_DEVIATION defects in Phase 2; Planner honors override as 2nd-priority tier rule; Phase 6-H PLAN_TIER_OVERRIDE_PRESENT + OVERRIDE_TIER_HONORED verification | 2 | V-04 |
| C-55 | Phase 0-A-11 STATUS_QUO_METHOD declaration — METHOD_NAME, METHOD_DESCRIPTION, METHOD_COVERAGE, structured METHOD_BLIND_SPOTS checklist (5 dimensions: YES/NO); STATUS_QUO_METHOD_SIGNED; Contract Auditor verifies | 3 | V-05 |
| C-56 | Phase 4-SQ STATUS_QUO_SIMULATION — abbreviated parallel trace using declared informal method only; no CONSTRAINT_VERDICTS/CHAIN_EFFECTS/PREDICTION_MATCH/TIMELINE_ANOMALY/CHAIN_BUDGET; STATUS_QUO_FINDINGS summary | 3 | V-05 |
| C-57 | Phase 5-F STATUS_QUO_COVERAGE table — DETECTION_METHOD + SQ_BLIND_SPOT per defect; structural auto-classification rules from declared blind spots; STATUS_QUO_GAP_SUMMARY with STRUCTURAL_BLIND_SPOTS_ACTIVATED and STATUS_QUO_GAP_NARRATIVE; satisfies C-35 automatically | 3 | V-05 |
| C-58 | Phase 6-H STATUS_QUO_COVERAGE_AUDIT — per-defect detection method verification; AUTOMATIC_CLASSIFICATION_VERIFIED for PREDICTION_DEVIATION, CHAIN_BUDGET_EXCEEDED, TIMELINE_ANOMALY; STATUS_QUO_COVERAGE_AUDIT: PASS\|FAIL | 2 | V-05 |

**C-35 pass condition updated** — added note that an artifact satisfying C-57 automatically satisfies C-35; C-57 is the evidenced, grounded form of C-35.

**Cluster structure:**
- C-49/C-50 — Remediation Planner (defect catalog → executable work plan)
- C-51/C-52/C-53 — Turn Prediction Contract (pre-declared path expectations → prediction-vs-reality coverage dimension)
- C-54 — merges both clusters: CRITICAL-path deviations carry plan tier urgency regardless of severity class
- C-55/C-56/C-57/C-58 — Status Quo Simulation (asserted SIMULATION_DELTA → demonstrated gap via parallel informal trace)
