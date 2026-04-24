Here is the complete v13 rubric. Summary of what changed:

---

**4 new aspirational criteria, C-59 through C-62 (+10 pts). Max score: 212 → 222.**

| ID | What it captures | Wt | Source |
|----|------------------|----|--------|
| C-59 | PRE_FLIGHT_MANIFEST table issued by Contract Auditor *before* Topology Architect begins — `REQUIRED_DECLARATION \| PHASE_REF \| STATUS: PENDING` covering all Phase 0-A artifacts; updated to `COMPLETE\|MISSING` at Phase 0-CA-1; non-empty MISSING blocks Phase 1 | 3 | V-04 exclusive |
| C-60 | Explicit role handoff token at every boundary — Contract Auditor emits `GATE_STATUS: PASS\|FAIL`; Developer opens Phase 1 with "Received GATE_STATUS: [value]. Proceeding\|Blocked."; Developer closes Phase 5 with `DEVELOPER_CERTIFICATION: COMPLETE`; Auditor acknowledges before Phase 6-A | 2 | V-04 exclusive |
| C-61 | Column-schema contract for every Phase 1 derived column — `COLUMN_NAME \| FORMAT \| ALLOWED_VALUES \| REQUIRED_WHEN` in Phase 0; Contract Auditor verifies `COLUMN_SCHEMA_COMPLETE: PASS\|FAIL`; prose-specified columns (PREDICTION_MATCH as a pipe-delimited list, etc.) do not satisfy | 3 | V-02 / V-04 |
| C-62 | `FIELD\|VALUE` table schema for structured Phase 0 declarations — STATUS_QUO_METHOD blind-spots checklist, TURN_PREDICTION_CONTRACT path entries, DEVIATION_BUDGET thresholds, CONV_CHAIN_BUDGET entries; missing row = schema gap (enforceable); missing prose field = invisible | 2 | V-02 / V-04 |

**Cluster structure:**
- C-59/C-60 — Role interlock via manifest and token (V-04's pre-flight blocking role pattern)
- C-61/C-62 — Schema-first enforcement (V-02/V-04's table-driven declaration advantage)

The distinction between the two clusters maps to the two independent axes in V-04:
- V-01 had C-59/C-60 (role-sequence gate) but not C-61/C-62 (table schemas) → strongest gate, weakest schema enforcement
- V-02 had C-61/C-62 but not C-59/C-60 → strongest schemas, weakest gate
- V-04 had all four → no additional PARTIAL
