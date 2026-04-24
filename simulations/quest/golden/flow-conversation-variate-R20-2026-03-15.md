# flow-conversation Variate — Round 20
**Date:** 2026-03-15
**Rubric:** v19 (C-77 + C-78 introduced)
**Target criteria:** C-77 (LIFECYCLE_PROTOCOL SOLE_AUTHORITY + two-layer closure narrative), C-78 (CONTRACT_AUDIT_GATE_HONORED explicit standalone completeness declaration)
**Chain dependencies:** C-77 → C-76 → C-73 → C-70 → C-66 → C-63; C-78 → C-75 → C-72 ∧ C-74

---

## Round 20 Variation Map

| Variation | Axis | C-77 | C-78 | Notes |
|-----------|------|------|------|-------|
| V-01 | Lifecycle emphasis | PASS | PARTIAL | LIFECYCLE_PROTOCOL foregrounded as design-intent document with SOLE_AUTHORITY; gate standalone declaration implicit |
| V-02 | Output format | PARTIAL | PASS | Gate block formatted as FIELD\|VALUE table with STANDALONE_DECLARATION row; SOLE_AUTHORITY narrative present but closure statement generic |
| V-03 | Phrasing register (formal imperative) | PASS | PASS | DIRECTIVE: fields for both SOLE_AUTHORITY narrative and STANDALONE_DECLARATION; no prose hedging space for omission |
| V-04 | Role sequence + Lifecycle emphasis | PASS | PARTIAL | Phase -1 Manifest Issuer pre-declares LIFECYCLE_PROTOCOL design contract; TA receives it; gate standalone framing arrives organically but may miss explicit statement |
| V-05 | Combined: Lifecycle emphasis + Output format + Phrasing register | PASS | PASS | SOLE_AUTHORITY + two-layer narrative required as FIELD\|VALUE block; gate table requires STANDALONE_DECLARATION row with exact phrase; ceiling variation for 164+ |

---

## V-01 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** Foregrounding LIFECYCLE_PROTOCOL as a named design-intent document — rather than a procedural checklist — creates pressure to explain *why* the protocol works as a system. A design-intent document naturally names both layers (declaration layer, reference layer) and their interaction; the "neither layer alone closes the system" statement follows structurally from that framing. C-77 fires because the SOLE_AUTHORITY block is a required section header, not an optional annotation. C-78 fires partially: the gate's standalone capability becomes visible when both C-72 and C-74 fields are present, but no explicit framing statement is required by this variation.

---

You are simulating a Copilot Studio conversation-flow trace for: {{topic}}

You execute five sequential roles. Each role reads the prior output and extends it. Silent fallthrough between roles is a structural violation — every role boundary must carry an explicit handoff token and receive acknowledgment.

---

### LIFECYCLE PROTOCOL — DESIGN INTENT

This section is the sole declaration layer for all role-transition lifecycle events in this protocol. It exists as a named, standalone section — not as inline notes within role instructions. Any role instruction that re-declares a transition outside this section creates an unauthorized divergence point.

**SOLE_AUTHORITY DECLARATION**

This LIFECYCLE_PROTOCOL section is the declaration layer for the single-source enforcement system governing role transitions. Phase 6-A LIFECYCLE_POINTER_AUDIT is the reference layer: it verifies that every pointer of the form "per LIFECYCLE_PROTOCOL Transition N" in role instruction blocks resolves to a labeled transition declared here. Neither the declaration layer alone nor the reference layer alone closes the enforcement system — both must operate simultaneously. The declaration layer prevents transition re-declarations; the reference layer catches dangling pointers to transitions that do not exist or have been re-numbered.

**DESIGN PROPERTY:** A conforming trace satisfies both layers. A trace where role instructions contain no unauthorized re-declarations (C-70 PASS) but Phase 6-A carries no LIFECYCLE_POINTER_AUDIT does not close the system. A trace where Phase 6-A verifies pointers but role instructions contain inline re-declarations has reference-level discipline with declaration-level leakage. Closure requires both.

**Transition registry (all five transitions declared here and nowhere else):**

| Transition | From | To | Token Issued | Token Received |
|------------|------|----|-------------|----------------|
| T-1 | Phase -1 (Manifest Issuer) | Topology Architect | `HANDOFF_TO: TOPOLOGY ARCHITECT` | `"Received PRE_FLIGHT_MANIFEST."` |
| T-2 | Topology Architect | Contract Auditor | `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1` | `"Received Phase 0-A artifacts."` |
| T-3 | Contract Auditor | Developer | `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER` | `"Received GATE_STATUS: [value]. Proceeding\|Blocked."` |
| T-4 | Developer | Auditor | `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR` | `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` |
| T-5 | Auditor | Report Producer | `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER` | `"Received AUDITOR_CERTIFICATION: COMPLETE."` |

Role instructions reference these transitions by number (e.g., "per LIFECYCLE_PROTOCOL Transition T-3"). Phase 6-A LIFECYCLE_POINTER_AUDIT verifies every such reference resolves to a row in this table.

---

### PHASE -1 — CONTRACT AUDITOR (Pre-Flight Manifest)

**Role:** Contract Auditor. You issue the PRE_FLIGHT_MANIFEST before the Topology Architect begins any Phase 0-A authoring. You do not build the trace; you gate it.

Issue a PRE_FLIGHT_MANIFEST table:

| REQUIRED_DECLARATION | PHASE_REF | SCHEMA_TYPE | STATUS |
|----------------------|-----------|-------------|--------|
| Topic graph (0-D-1) | Phase 0-D-1 | list | PENDING |
| Vocabulary gate (0-D-2) | Phase 0-D-2 | list | PENDING |
| Session variable registry (0-D-3) | Phase 0-D-3 | list | PENDING |
| Invariant register (0-D-4) | Phase 0-D-4 | list | PENDING |
| Transition map (0-D-5) | Phase 0-D-5 | list | PENDING |
| Session variable timeline contract (0-A-6) | Phase 0-A-6 | FIELD\|VALUE | PENDING |
| Invariant register with CHAIN_ID (0-A-7) | Phase 0-A-7 | list | PENDING |
| DEVIATION_BUDGET (0-A-8) | Phase 0-A-8 | FIELD\|VALUE | PENDING |
| CONV_CHAIN_BUDGET (0-A-9) | Phase 0-A-9 | FIELD\|VALUE | PENDING |
| TURN_PREDICTION_CONTRACT (0-A-10) | Phase 0-A-10 | FIELD\|VALUE | PENDING |
| STATUS_QUO_METHOD (0-A-11) | Phase 0-A-11 | FIELD\|VALUE | PENDING |

Close with: `HANDOFF_TO: TOPOLOGY ARCHITECT`

---

### PHASE 0 — TOPOLOGY ARCHITECT

**Role:** Topology Architect. Open with: `"Received PRE_FLIGHT_MANIFEST."` Author all Phase 0-A sections in order. Role instructions reference lifecycle transitions per LIFECYCLE_PROTOCOL — do not re-declare transition semantics here. Close with: `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`.

**Phase 0-D-1** TOPIC_GRAPH: Declare all topics, trigger phrases, entry conditions, exit targets.
**Phase 0-D-2** VOCABULARY_GATE: Permitted and prohibited terms. Sign.
**Phase 0-D-3** SESSION_VARIABLE_REGISTRY: All variables with PERSISTENCE_CLASS and initial value.
**Phase 0-D-4** INVARIANT_REGISTER: All CONV-NN invariants with falsification conditions.
**Phase 0-D-5** TRANSITION_MAP: All graph edges as TRANS-NN (source, target, condition, REQUIRED|OPTIONAL).
**Phase 0-A-6** SESSION_VARIABLE_TIMELINE_CONTRACT: Full lifecycle per variable (FIRST_WRITTEN_TOPIC, CLEARED_BY, READ_AFTER_CLEARED, AUTHORIZED_REWRITERS). FIELD|VALUE format.
**Phase 0-A-7** INVARIANT_REGISTER_EXTENDED: Add PROPAGATION list and CHAIN_ID to every CONV-NN.
**Phase 0-A-8** DEVIATION_BUDGET: P0_MAX|P1_MAX|P2_MAX|P3_MAX|BUDGET_RATIONALE. FIELD|VALUE. Lock after authoring.
**Phase 0-A-9** CONV_CHAIN_BUDGET: Per-chain CHAIN_ID|HEAD_CONV|CHAIN_LENGTH|CHAIN_BUDGET|BUDGET_RATIONALE. FIELD|VALUE.
**Phase 0-A-10** TURN_PREDICTION_CONTRACT: HAPPY_PATH + up to 3 ALT_PATHs. Per path: PATH_ID|PATH_DESCRIPTION|PATH_CRITICALITY|PREDICTED_TURN_SEQUENCE. FIELD|VALUE. Sign.
**Phase 0-A-11** STATUS_QUO_METHOD: METHOD_NAME|METHOD_DESCRIPTION|METHOD_COVERAGE|METHOD_BLIND_SPOTS (5 YES|NO rows). FIELD|VALUE. Sign.

**COLUMN_SCHEMA_CONTRACT** (declare before Phase 1): Every non-core Phase 1 column as COLUMN_NAME|FORMAT|ALLOWED_VALUES|REQUIRED_WHEN.

---

### PHASE 0-CA-1 — CONTRACT AUDITOR (Completeness Gate)

**Role:** Contract Auditor. Open with: `"Received Phase 0-A artifacts."` Update PRE_FLIGHT_MANIFEST rows to COMPLETE|MISSING|WRONG_SCHEMA. Verify:

- VARS_IN_TOPOLOGY vs VARS_IN_CONTRACT delta
- CHAINS_IN_TOPOLOGY vs CHAINS_IN_BUDGET delta (CHAIN_BUDGET_DELTA)
- PREDICTION_CONTRACT_SIGNED: YES|NO
- STATUS_QUO_METHOD_SIGNED: YES|NO
- COLUMN_SCHEMA_COMPLETE: PASS|FAIL
- DECLARATION_SCHEMA_COMPLETE: PASS|FAIL per FIELD|VALUE declaration, with parenthetical row count: `NAME: PASS|FAIL (count N rows: [breakdown])`
- PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL

Close with: `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER`

---

### PHASE 1–5 — DEVELOPER

**Role:** Developer. Open with: `"Received GATE_STATUS: [value]. Proceeding|Blocked."` If GATE_STATUS: FAIL, document block reason and stop.

**Phase 1** TURN TABLE — columns per COLUMN_SCHEMA_CONTRACT. Include all schema-declared columns for every row. Author Phase 1-S SESSION_TIMELINE (mutation log) before Phase 1 SESSION_STATE. Each SESSION_STATE cell cites its Phase 1-S entry.

**Phase 1-T** TOPIC_AGGREGATE: Topic-indexed summary additive to Phase 1 (not replacing it).

**Phase 2** DEFECT CLASSIFICATION: FOUND/CONFIRMED_ABSENT for each of the nine defect classes. P0 defects: emit EXECUTION_HALT block (HALT_TRIGGER, ROOT_CAUSE, MVF_RECOMMENDATION, MVF_SCOPE, UNBLOCKED_BY, CHAIN_BREAK_TRACE, CHAIN_REPAIR) before lower-severity defects.

**Phase 3** ENTANGLEMENT_MAP (3-E): Every FOUND defect carries ENTANGLEMENT_VERDICT (ISOLATED|ENABLES[…]|MASKED_BY[…]).

**Phase 4** FALLBACK, ESCALATION, DISAMBIGUATION paths traced in full.

**Phase 4-SQ** STATUS_QUO_SIMULATION: Re-run using only STATUS_QUO_METHOD capabilities. Per turn: TURN_ID|TOPIC_MATCHED|AGENT_RESPONSE_SUMMARY|SQ_DEFECT_FOUND|SQ_DEFECT_CLASS|REMARKS. Write STATUS_QUO_FINDINGS after.

**Phase 5** Coverage summary in order:
1. DEVIATION_BUDGET_UTILIZATION block (SEVERITY|BUDGET|ACTUAL_DEVIATES|STATUS per class; OVERALL_BUDGET_STATUS)
2. CHAIN_BUDGET_UTILIZATION block (per CHAIN-NN: HEAD_CONV|CHAIN_BUDGET|HEAD_DEVIATES_COUNT|STATUS)
3. COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (CLEAN requires TIMELINE_ANOMALY_RATE = 0)
4. CONSTRAINT_CHAIN_STATUS_SUMMARY (per CHAIN-NN: CHAIN_ID|HEAD_CONV|CHAIN_LENGTH|TURNS_SUSPENDED|FINAL_STATUS)
5. Coverage ratios: topic_coverage_ratio, transitions_exercised/total_declared, slot_path_coverage, TIMELINE_ANOMALY_RATE, PATH_ADHERENCE_RATIO (all PROVISIONAL if DEGRADED)
6. Phase 5-F STATUS_QUO_COVERAGE table: per FOUND defect DEFECT_ID|DEFECT_CLASS|FOUND_BY_SIMULATION|FOUND_BY_STATUS_QUO|DETECTION_METHOD|SQ_BLIND_SPOT; STATUS_QUO_GAP_SUMMARY after.

Close with: `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR`

---

### PHASE 7 — REMEDIATION PLANNER

**Role:** Remediation Planner. Read all EXECUTION_HALT blocks and Phase 3-E ENTANGLEMENT_MAP. Produce topologically sorted REMEDIATION_PLAN: per FOUND defect one PLAN_ITEM (PLAN_ID, DEFECT_REF, SEVERITY_CLASS, SCOPE, DEPENDENCY_ON, PLAN_TIER, TIER_RATIONALE, CHAIN_REPAIR_ITEMS, UNBLOCKED_BY). CRITICAL-path PREDICTION_DEVIATION defects carry PLAN_TIER_OVERRIDE: IMMEDIATE. Close with PLAN_SUMMARY (PLAN_ITEM_COUNT, IMMEDIATE_COUNT, NEXT_SPRINT_COUNT, BACKLOG_COUNT, DEPENDENCY_CYCLE_CHECK).

Open with: `"Received AUDITOR_CERTIFICATION: COMPLETE."`

---

### PHASE 6 — AUDITOR

**Role:** Auditor. Open with: `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."`

**Phase 6-A** — Open with:
```
CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL
  WRONG_SCHEMA_RESIDUAL_SWEEP: CONFIRMED|NOT_CONFIRMED (sweep scope: [declaration names checked] — or CLEAN if none existed)
  PARENTHETICAL_VERIFICATION: CONFIRMED|NOT_CONFIRMED ([DECLARATION: N rows CONFIRMED, ...])
  BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
  BUDGET_STATUS_CONSISTENT: PASS|FAIL
  LIFECYCLE_POINTER_AUDIT:
    | ROLE | POINTER_TEXT | TARGET_TRANSITION | RESOLVED: YES|NO |
    (one row per "per LIFECYCLE_PROTOCOL Transition T-N" reference found in role instructions)
  SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

**Phase 6-B** Severity Co-Residency Audit — structured table: every FOUND defect row has SEVERITY_CLASS and INVARIANT_CITE. EXEMPT locks CONFIRMED_ABSENT rows.

**Phase 6-C** Entanglement map consistency audit against Phase 1 turn-level evidence.

**Phase 6-D** Topic aggregate consistency audit: conformance_rollup in Phase 1-T vs DEVIATES count from Phase 1; TOPIC_ROLLUP_MISMATCH findings.

**Phase 6-E** Session timeline consistency: replay Phase 1-S mutations turn-by-turn, compare to Phase 1 SESSION_STATE; TIMELINE_STATE_MISMATCH findings.

**Phase 6-F** Fix Viability Audit: per EXECUTION_HALT block — CONV_VIOLATIONS_INTRODUCED, CONV_VIOLATIONS_DETAIL, VIABILITY, CHAIN_REPAIR_COMPLETE.

**Phase 6-G** Chain Integrity Audit: per CHAIN-NN verify CHAIN_EFFECTS in Phase 1 against upstream CONV-NN verdicts; CHAIN_VERDICT_INCONSISTENCY findings; CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED table.

**Phase 6-H** Combined audit — PATH_ADHERENCE_AUDIT (per-turn PREDICTION_MATCH reported vs audited), PATH_ADHERENCE_RATIO_VERIFIED, CRITICAL_PATH_ESCALATION_VERIFIED, PLAN_TIER_OVERRIDE_PRESENT, OVERRIDE_TIER_HONORED, PLAN_INTEGRITY_AUDIT (EXECUTION_HALT_IN_PLAN, CHAIN_REPAIR_IN_SCOPE, DEPENDENCY_ORDER_VALID per item), STATUS_QUO_COVERAGE_AUDIT (DETECTION_METHOD per defect, AUTOMATIC_CLASSIFICATION_VERIFIED).

Close with: `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** Formatting CONTRACT_AUDIT_GATE_HONORED as a mandatory FIELD|VALUE table — with STANDALONE_DECLARATION as a required row — makes the standalone completeness statement verifiable by schema rather than by prose discipline. When the gate is a table, the Contract Auditor cannot close Phase 6-A without populating every row; a missing STANDALONE_DECLARATION row is a schema gap the Auditor can flag identically to a WRONG_SCHEMA finding. C-78 fires because the framing statement is a table-enforced field, not an optional sentence. C-77 partially fires: the LIFECYCLE_PROTOCOL section exists with a SOLE_AUTHORITY header, but the two-layer closure narrative is described rather than structurally required as a named field.

---

You are simulating a Copilot Studio conversation-flow trace for: {{topic}}

Five sequential roles execute this protocol. Silent fallthrough is a structural violation — every role boundary carries a handoff token and receive acknowledgment, declared in the LIFECYCLE_PROTOCOL section.

---

### LIFECYCLE_PROTOCOL

This section is the sole declaration layer for role-transition lifecycle events. Role instructions reference transitions by number. Phase 6-A LIFECYCLE_POINTER_AUDIT verifies resolution.

**SOLE_AUTHORITY:** This section declares all five lifecycle transitions. Neither this section alone nor Phase 6-A alone closes the enforcement system — the declaration layer (here) prevents re-declarations; the reference layer (Phase 6-A LIFECYCLE_POINTER_AUDIT) catches dangling pointers.

| Transition | From | To | Outgoing Token | Incoming Acknowledgment |
|------------|------|----|----------------|------------------------|
| T-1 | Phase -1 | Topology Architect | `HANDOFF_TO: TOPOLOGY ARCHITECT` | `"Received PRE_FLIGHT_MANIFEST."` |
| T-2 | Topology Architect | Contract Auditor | `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1` | `"Received Phase 0-A artifacts."` |
| T-3 | Contract Auditor | Developer | `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER` | `"Received GATE_STATUS: [value]. Proceeding\|Blocked."` |
| T-4 | Developer | Auditor | `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR` | `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` |
| T-5 | Auditor | Report Producer | `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER` | `"Received AUDITOR_CERTIFICATION: COMPLETE."` |

---

### PHASE -1 — CONTRACT AUDITOR (Pre-Flight Manifest)

Issue PRE_FLIGHT_MANIFEST table (REQUIRED_DECLARATION|PHASE_REF|SCHEMA_TYPE|STATUS: PENDING for all 11 artifacts). SCHEMA_TYPE = FIELD|VALUE for 0-A-6, 0-A-8, 0-A-9, 0-A-10, 0-A-11. Close: `HANDOFF_TO: TOPOLOGY ARCHITECT`

---

### PHASE 0 — TOPOLOGY ARCHITECT

Open: `"Received PRE_FLIGHT_MANIFEST."` Author all Phase 0-D and Phase 0-A sections against the manifest. All FIELD|VALUE declarations use two-column table format (FIELD|VALUE rows — no prose substitution). Include COLUMN_SCHEMA_CONTRACT table (COLUMN_NAME|FORMAT|ALLOWED_VALUES|REQUIRED_WHEN) for every non-core Phase 1 column. Close: `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`

---

### PHASE 0-CA-1 — CONTRACT AUDITOR (Completeness Gate)

Open: `"Received Phase 0-A artifacts."` Update manifest rows to COMPLETE|MISSING|WRONG_SCHEMA. Verify all deltas. Per FIELD|VALUE declaration include parenthetical: `NAME: PASS|FAIL (count N rows: [breakdown])`. Emit PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL.

Close — emit this gate block as a FIELD|VALUE table:

```
CONTRACT_AUDIT_GATE_HONORED block (FIELD|VALUE format):

| FIELD | VALUE |
|-------|-------|
| STATUS | PASS|FAIL |
| STANDALONE_DECLARATION | This CONTRACT_AUDIT_GATE_HONORED block is a complete standalone audit summary. A verifier reading this block alone can confirm format compliance and row-count completeness without navigating to Phase 6-A tables or Phase 0-CA-1 output. |
| WRONG_SCHEMA_RESIDUAL_SWEEP | CONFIRMED|NOT_CONFIRMED (sweep scope: [declaration names]) |
| PARENTHETICAL_VERIFICATION | CONFIRMED|NOT_CONFIRMED ([DECLARATION: N rows CONFIRMED, ...]) |
| BUDGET_UTILIZATION_VERIFIED | PASS|FAIL |
| BUDGET_STATUS_CONSISTENT | PASS|FAIL |
```

*(Note: this gate block appears in Phase 6-A, authored by the post-execution Auditor — the schema is declared here so the Auditor knows the required field set.)*

Close: `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER`

---

### PHASE 1–5 — DEVELOPER

Open: `"Received GATE_STATUS: [value]. Proceeding|Blocked."`

Author phases 1–5 per LIFECYCLE_PROTOCOL Transition T-3 receive semantics. Phase 1 turn table uses all schema-declared columns. Phase 1-S (mutation log) authored before Phase 1 SESSION_STATE. Each SESSION_STATE cell cites its Phase 1-S source entry.

**Phase 1** Full turn table (all COLUMN_SCHEMA_CONTRACT columns).
**Phase 1-S** SESSION_TIMELINE mutation log.
**Phase 1-T** TOPIC_AGGREGATE (additive).
**Phase 2** Nine defect classes. P0: EXECUTION_HALT block with CHAIN_BREAK_TRACE and CHAIN_REPAIR.
**Phase 3** ENTANGLEMENT_MAP.
**Phase 4** Fallback, escalation, disambiguation traces.
**Phase 4-SQ** STATUS_QUO_SIMULATION.
**Phase 5** DEVIATION_BUDGET_UTILIZATION → CHAIN_BUDGET_UTILIZATION → COVERAGE_QUALITY_GATE → CONSTRAINT_CHAIN_STATUS_SUMMARY → five coverage ratios → Phase 5-F STATUS_QUO_COVERAGE.

Close: `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR`

---

### PHASE 6 — AUDITOR

Open: `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."`

**Phase 6-A** — Emit CONTRACT_AUDIT_GATE_HONORED as the FIELD|VALUE table specified in Phase 0-CA-1 schema. Every field must be populated; a missing or empty STANDALONE_DECLARATION field is a schema gap reportable as a Phase 6-A finding. Include LIFECYCLE_POINTER_AUDIT sub-table (ROLE|POINTER_TEXT|TARGET_TRANSITION|RESOLVED).

**Phase 6-B** Severity Co-Residency Audit table.
**Phase 6-C** Entanglement map consistency.
**Phase 6-D** Topic aggregate conformance_rollup vs Phase 1 DEVIATES count.
**Phase 6-E** SESSION_TIMELINE replay verification.
**Phase 6-F** Fix Viability per EXECUTION_HALT block.
**Phase 6-G** Chain Integrity per CHAIN-NN.
**Phase 6-H** Combined PATH_ADHERENCE + PLAN_INTEGRITY + STATUS_QUO_COVERAGE audit.

Close: `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`

---

### PHASE 7 — REMEDIATION PLANNER

Open: `"Received AUDITOR_CERTIFICATION: COMPLETE."` Topologically sorted REMEDIATION_PLAN. PLAN_TIER_OVERRIDE: IMMEDIATE on CRITICAL-path PREDICTION_DEVIATION defects. PLAN_SUMMARY closing.

---

## V-03 — Phrasing Register (Formal Imperative)

**Axis:** Phrasing register
**Hypothesis:** Replacing descriptive prose ("the section should carry a SOLE_AUTHORITY header") with formal imperative directives ("DIRECTIVE: LIFECYCLE_PROTOCOL MUST carry a SOLE_AUTHORITY header. The header MUST include [exact fields].") eliminates the prose hedging space where C-77 and C-78 signals get omitted. When the prompt specifies exact required strings rather than describing properties, the LLM treats the absence of a required string as a gap rather than a stylistic choice. Both C-77 and C-78 pass because the required output strings are prescribed at directive level.

---

You are simulating a Copilot Studio conversation-flow trace for: {{topic}}

Execute five sequential roles in order. Each role MUST issue its outgoing handoff token; each receiving role MUST acknowledge it. Silent fallthrough is a structural violation.

---

### LIFECYCLE_PROTOCOL (MANDATORY STANDALONE SECTION)

**DIRECTIVE:** This section MUST exist as a named standalone section with header `LIFECYCLE_PROTOCOL`. It MUST NOT be reproduced as inline notes inside any role instruction block.

**DIRECTIVE — SOLE_AUTHORITY BLOCK:** The LIFECYCLE_PROTOCOL section MUST open with a SOLE_AUTHORITY block containing exactly these three statements:
1. "This section is the declaration layer: every role-transition event is declared exactly once, here."
2. "Phase 6-A LIFECYCLE_POINTER_AUDIT is the reference layer: it verifies every pointer of the form 'per LIFECYCLE_PROTOCOL Transition T-N' resolves to a labeled entry in this section."
3. "Neither layer alone closes the single-source enforcement system. Declaration-layer discipline without reference-layer verification leaves dangling pointers undetected. Reference-layer verification without declaration-layer discipline allows unauthorized re-declarations."

**DIRECTIVE — TRANSITION REGISTRY:** Declare all five transitions as a table: T-1 through T-5 (from, to, outgoing token, incoming acknowledgment). Role instructions MUST reference these by transition number only — no inline re-declaration of token semantics.

| T-1: Phase -1 → Topology Architect | `HANDOFF_TO: TOPOLOGY ARCHITECT` | `"Received PRE_FLIGHT_MANIFEST."` |
| T-2: Topology Architect → Contract Auditor | `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1` | `"Received Phase 0-A artifacts."` |
| T-3: Contract Auditor → Developer | `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER` | `"Received GATE_STATUS: [value]. Proceeding\|Blocked."` |
| T-4: Developer → Auditor | `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR` | `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` |
| T-5: Auditor → Report Producer | `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER` | `"Received AUDITOR_CERTIFICATION: COMPLETE."` |

---

### PHASE -1 — CONTRACT AUDITOR (Pre-Flight Manifest)

**DIRECTIVE:** Issue PRE_FLIGHT_MANIFEST table. All 11 required declarations, with STATUS: PENDING. Rows for 0-A-6, 0-A-8, 0-A-9, 0-A-10, 0-A-11 MUST carry SCHEMA_TYPE: FIELD|VALUE.

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL Transition T-1.

---

### PHASE 0 — TOPOLOGY ARCHITECT

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL Transition T-1 acknowledgment.

Author Phase 0-D-1 through 0-D-5 (topic graph, vocabulary gate, session variables, invariant register, transition map) and Phase 0-A-6 through 0-A-11 in order. FIELD|VALUE declarations MUST use two-column table rows — prose substitution violates the schema.

**DIRECTIVE — COLUMN_SCHEMA_CONTRACT:** Declare every non-core Phase 1 column as a table row (COLUMN_NAME|FORMAT|ALLOWED_VALUES|REQUIRED_WHEN) before Phase 1 begins. A column not declared here cannot be enforced by the Contract Auditor.

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL Transition T-2.

---

### PHASE 0-CA-1 — CONTRACT AUDITOR (Completeness Gate)

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL Transition T-2 acknowledgment.

Update PRE_FLIGHT_MANIFEST rows to COMPLETE|MISSING|WRONG_SCHEMA. A declaration in non-FIELD|VALUE format where the manifest specifies SCHEMA_TYPE: FIELD|VALUE MUST be marked WRONG_SCHEMA (not MISSING). Verify all deltas. Per FIELD|VALUE declaration: `DECLARATION_SCHEMA_COMPLETE: PASS|FAIL (count N rows: [breakdown])`. PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL.

**DIRECTIVE — GATE BLOCK:** Emit CONTRACT_AUDIT_GATE_HONORED block. The block MUST contain:
- `CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL`
- `STANDALONE_DECLARATION: "This is a complete standalone audit summary. A verifier reading this block requires no navigation to Phase 6-A tables or Phase 0-CA-1 output to confirm format compliance and row-count completeness."`
- `WRONG_SCHEMA_RESIDUAL_SWEEP: CONFIRMED|NOT_CONFIRMED (sweep scope: [list declaration names checked]; or "CLEAN — no WRONG_SCHEMA rows" if none)`
- `PARENTHETICAL_VERIFICATION: CONFIRMED|NOT_CONFIRMED ([DECLARATION: N rows CONFIRMED, ...])`
- `BUDGET_UTILIZATION_VERIFIED: PASS|FAIL`
- `BUDGET_STATUS_CONSISTENT: PASS|FAIL`

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL Transition T-3.

---

### PHASE 1–5 — DEVELOPER

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL Transition T-3 acknowledgment. If GATE_STATUS: FAIL, stop and document block reason.

**Phase 1** Turn table — MUST include every column declared in COLUMN_SCHEMA_CONTRACT. Phase 1-S (SESSION_TIMELINE mutation log) MUST be authored before Phase 1 SESSION_STATE; SESSION_STATE cells MUST cite their Phase 1-S source.

**Phase 1-T** Topic aggregate (additive — MUST NOT replace Phase 1 turn table).

**Phase 2** Nine defect classes: dead end, infinite loop, intent collision, missing fallback, TIMELINE_ANOMALY, PREDICTION_DEVIATION, CHAIN_BUDGET_EXCEEDED, plus any additional. P0 defects: EXECUTION_HALT block (HALT_TRIGGER|ROOT_CAUSE|MVF_RECOMMENDATION|MVF_SCOPE|UNBLOCKED_BY|CHAIN_BREAK_TRACE|CHAIN_REPAIR) BEFORE lower-severity defects.

**Phase 3** ENTANGLEMENT_MAP — every FOUND defect carries ENTANGLEMENT_VERDICT.

**Phase 4** Fallback chain, escalation, disambiguation — full traces.

**Phase 4-SQ** STATUS_QUO_SIMULATION using only STATUS_QUO_METHOD capabilities (no constraint verdicts, no chain effects, no prediction match, no timeline anomaly tracking). Per turn: TURN_ID|TOPIC_MATCHED|AGENT_RESPONSE_SUMMARY|SQ_DEFECT_FOUND|SQ_DEFECT_CLASS|REMARKS.

**Phase 5** In order:
1. DEVIATION_BUDGET_UTILIZATION (SEVERITY|BUDGET|ACTUAL_DEVIATES|STATUS; OVERALL_BUDGET_STATUS)
2. CHAIN_BUDGET_UTILIZATION (per chain: HEAD_CONV|CHAIN_BUDGET|HEAD_DEVIATES_COUNT|STATUS; CHAIN_BUDGET_EXCEEDED findings)
3. COVERAGE_QUALITY_GATE: CLEAN|DEGRADED
4. CONSTRAINT_CHAIN_STATUS_SUMMARY (CHAIN_ID|HEAD_CONV|CHAIN_LENGTH|TURNS_SUSPENDED|FINAL_STATUS)
5. Five coverage ratios (all PROVISIONAL if DEGRADED): topic_coverage_ratio, transition coverage, slot-path coverage, TIMELINE_ANOMALY_RATE, PATH_ADHERENCE_RATIO
6. Phase 5-F STATUS_QUO_COVERAGE table with STATUS_QUO_GAP_SUMMARY

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL Transition T-4.

---

### PHASE 6 — AUDITOR

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL Transition T-4 acknowledgment.

**Phase 6-A:**

**DIRECTIVE:** Emit CONTRACT_AUDIT_GATE_HONORED block with all fields specified in Phase 0-CA-1. The STANDALONE_DECLARATION field MUST be populated with the exact prescribed text. A missing or empty STANDALONE_DECLARATION is a Phase 6-A structural finding, not a quality gap.

Include LIFECYCLE_POINTER_AUDIT sub-table: enumerate every "per LIFECYCLE_PROTOCOL Transition T-N" reference found in all role instruction blocks (ROLE|POINTER_TEXT|TARGET_TRANSITION|RESOLVED: YES|NO). Unresolved pointers are DANGLING_LIFECYCLE_POINTER findings. Include SIMULATION_DELTA_COMPLETE: PASS|FAIL.

**Phase 6-B** Severity Co-Residency Audit table (FOUND defects only; CONFIRMED_ABSENT rows EXEMPT).
**Phase 6-C** Entanglement map consistency audit.
**Phase 6-D** Topic aggregate conformance_rollup vs Phase 1 DEVIATES count per topic.
**Phase 6-E** Session timeline replay: reconstruct SESSION_STATE from Phase 1-S; compare to Phase 1 SESSION_STATE column.
**Phase 6-F** Fix Viability Audit per EXECUTION_HALT block (CONV_VIOLATIONS_INTRODUCED|CONV_VIOLATIONS_DETAIL|VIABILITY|CHAIN_REPAIR_COMPLETE).
**Phase 6-G** Chain Integrity Audit per CHAIN-NN (CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED; CHAIN_VERDICT_INCONSISTENCY findings).
**Phase 6-H** PATH_ADHERENCE_AUDIT + PLAN_INTEGRITY_AUDIT + STATUS_QUO_COVERAGE_AUDIT (combined).

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL Transition T-5.

---

### PHASE 7 — REMEDIATION PLANNER

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL Transition T-5 acknowledgment.

Topologically sorted REMEDIATION_PLAN. CRITICAL-path PREDICTION_DEVIATION defects carry PLAN_TIER_OVERRIDE: IMMEDIATE ("CRITICAL path deviation — overrides severity-based tier"). PLAN_SUMMARY close.

---

## V-04 — Role Sequence + Lifecycle Emphasis

**Axis:** Role sequence + Lifecycle emphasis
**Hypothesis:** Injecting the LIFECYCLE_PROTOCOL design contract as a Phase -1 deliverable — issued by the Manifest Issuer before the Topology Architect begins — means every subsequent role authors against a pre-declared design intent rather than discovering it retrospectively. When the design intent (SOLE_AUTHORITY + two-layer closure narrative) arrives as the first artifact, role instructions naturally cite it rather than re-declaring it. C-77 fires because the LIFECYCLE_PROTOCOL design contract is an explicit Phase -1 output the TA must "receive" before authoring Phase 0. C-78 fires partially: the gate's standalone capability is established by C-75, but the explicit framing statement is not required as a Phase -1 artifact and may arrive organically.

---

You are simulating a Copilot Studio conversation-flow trace for: {{topic}}

Five sequential roles execute this protocol. Role -1 issues two artifacts before the Topology Architect begins: the PRE_FLIGHT_MANIFEST (standard) and the LIFECYCLE_PROTOCOL_DESIGN_CONTRACT (new in this variation). The TA receives both before authoring any Phase 0-A section.

---

### PHASE -1 — CONTRACT AUDITOR (Pre-Flight Manifest + Lifecycle Design Contract)

**Role:** Contract Auditor. You issue two artifacts in Phase -1.

**Artifact 1 — PRE_FLIGHT_MANIFEST**

| REQUIRED_DECLARATION | PHASE_REF | SCHEMA_TYPE | STATUS |
|----------------------|-----------|-------------|--------|
| Topic graph (0-D-1) | Phase 0-D-1 | list | PENDING |
| Vocabulary gate (0-D-2) | Phase 0-D-2 | list | PENDING |
| Session variable registry (0-D-3) | Phase 0-D-3 | list | PENDING |
| Invariant register (0-D-4) | Phase 0-D-4 | list | PENDING |
| Transition map (0-D-5) | Phase 0-D-5 | list | PENDING |
| Session variable timeline contract (0-A-6) | Phase 0-A-6 | FIELD\|VALUE | PENDING |
| Invariant register with CHAIN_ID (0-A-7) | Phase 0-A-7 | list | PENDING |
| DEVIATION_BUDGET (0-A-8) | Phase 0-A-8 | FIELD\|VALUE | PENDING |
| CONV_CHAIN_BUDGET (0-A-9) | Phase 0-A-9 | FIELD\|VALUE | PENDING |
| TURN_PREDICTION_CONTRACT (0-A-10) | Phase 0-A-10 | FIELD\|VALUE | PENDING |
| STATUS_QUO_METHOD (0-A-11) | Phase 0-A-11 | FIELD\|VALUE | PENDING |

**Artifact 2 — LIFECYCLE_PROTOCOL_DESIGN_CONTRACT**

Issue this as a standalone named artifact the TA will receive:

```
LIFECYCLE_PROTOCOL_DESIGN_CONTRACT

SOLE_AUTHORITY DECLARATION:
The LIFECYCLE_PROTOCOL section is the declaration layer for all role-transition events
in this protocol. Phase 6-A LIFECYCLE_POINTER_AUDIT is the reference layer. Neither
layer alone closes the single-source enforcement system:
  - Declaration layer (LIFECYCLE_PROTOCOL section): prevents unauthorized re-declarations
    by being the single location where all five transitions are defined.
  - Reference layer (Phase 6-A LIFECYCLE_POINTER_AUDIT): prevents dangling pointers by
    verifying every "per LIFECYCLE_PROTOCOL Transition T-N" reference in role instruction
    blocks resolves to a labeled entry in the declaration layer.
A trace where role instructions carry no re-declarations (C-70) but Phase 6-A carries no
LIFECYCLE_POINTER_AUDIT has declaration-level discipline with reference-level leakage.
A trace where Phase 6-A verifies all pointers but role instructions re-declare transitions
has reference-level discipline with declaration-level leakage. Closure requires both layers.

STRUCTURAL REQUIREMENT:
When the Topology Architect authors the LIFECYCLE_PROTOCOL section, it MUST reproduce
this SOLE_AUTHORITY DECLARATION verbatim (or in equivalent language) at the top of that
section, identifying itself as the declaration layer and naming Phase 6-A
LIFECYCLE_POINTER_AUDIT as the reference layer with the "neither layer alone" statement.
```

Close: `HANDOFF_TO: TOPOLOGY ARCHITECT`

---

### PHASE 0 — TOPOLOGY ARCHITECT

**Role:** Topology Architect. Open: `"Received PRE_FLIGHT_MANIFEST and LIFECYCLE_PROTOCOL_DESIGN_CONTRACT."`

Author LIFECYCLE_PROTOCOL section first, before any Phase 0-A authoring:

**LIFECYCLE_PROTOCOL** — reproduce SOLE_AUTHORITY DECLARATION from received LIFECYCLE_PROTOCOL_DESIGN_CONTRACT. Add transition registry (T-1 through T-5) as a table. Role instructions reference transitions by number — no inline re-declarations.

Then author Phase 0-D-1 through 0-D-5 and Phase 0-A-6 through 0-A-11 in order. FIELD|VALUE declarations use two-column table format. Author COLUMN_SCHEMA_CONTRACT.

Close: `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`

---

### PHASE 0-CA-1 — CONTRACT AUDITOR (Completeness Gate)

**Role:** Contract Auditor. Open: `"Received Phase 0-A artifacts."`

Verify PRE_FLIGHT_MANIFEST rows (COMPLETE|MISSING|WRONG_SCHEMA). Verify all deltas. Per FIELD|VALUE declaration: parenthetical row-count `NAME: PASS|FAIL (count N rows: [breakdown])`. PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL.

Emit CONTRACT_AUDIT_GATE_HONORED:
```
CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL
  WRONG_SCHEMA_RESIDUAL_SWEEP: CONFIRMED|NOT_CONFIRMED (sweep scope: [declarations checked])
  PARENTHETICAL_VERIFICATION: CONFIRMED|NOT_CONFIRMED ([DECLARATION: N rows CONFIRMED, ...])
  BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
  BUDGET_STATUS_CONSISTENT: PASS|FAIL
```

Close: `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER`

---

### PHASE 1–5 — DEVELOPER

Open: `"Received GATE_STATUS: [value]. Proceeding|Blocked."` (per LIFECYCLE_PROTOCOL Transition T-3)

Phase 1 (full turn table per COLUMN_SCHEMA_CONTRACT) → Phase 1-S (mutation log, before SESSION_STATE) → Phase 1-T (topic aggregate) → Phase 2 (nine defect classes, EXECUTION_HALT per P0) → Phase 3 (ENTANGLEMENT_MAP) → Phase 4 (fallback/escalation/disambiguation) → Phase 4-SQ (STATUS_QUO_SIMULATION) → Phase 5 (budget utilization → chain budget → quality gate → chain summary → five ratios → Phase 5-F STATUS_QUO_COVERAGE).

Close: `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR` (per LIFECYCLE_PROTOCOL Transition T-4)

---

### PHASE 6 — AUDITOR

Open: `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` (per LIFECYCLE_PROTOCOL Transition T-4)

**Phase 6-A**: Emit CONTRACT_AUDIT_GATE_HONORED with all fields. Add LIFECYCLE_POINTER_AUDIT sub-table enumerating all "per LIFECYCLE_PROTOCOL Transition T-N" references in role instructions (ROLE|POINTER_TEXT|TARGET_TRANSITION|RESOLVED). Add SIMULATION_DELTA_COMPLETE.

**Phase 6-B** through **Phase 6-H**: Co-residency, entanglement, topic aggregate, session timeline, fix viability, chain integrity, combined path/plan/SQ audit.

Close: `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER` (per LIFECYCLE_PROTOCOL Transition T-5)

---

### PHASE 7 — REMEDIATION PLANNER

Open: `"Received AUDITOR_CERTIFICATION: COMPLETE."` (per LIFECYCLE_PROTOCOL Transition T-5)

Topologically sorted REMEDIATION_PLAN with PLAN_TIER_OVERRIDE: IMMEDIATE on CRITICAL-path PREDICTION_DEVIATION defects. PLAN_SUMMARY close.

---

## V-05 — Combined: Lifecycle Emphasis + Output Format + Phrasing Register

**Axis:** Combined
**Hypothesis:** (1) LIFECYCLE_PROTOCOL required as a SOLE_AUTHORITY FIELD|VALUE block with a mandatory "neither layer alone" row forces C-77 via table-schema enforcement rather than prose discipline; (2) CONTRACT_AUDIT_GATE_HONORED required as a FIELD|VALUE table with a mandatory STANDALONE_DECLARATION row forces C-78 by identical schema-enforcement mechanism; (3) formal-imperative DIRECTIVE labels throughout eliminate the prose hedging space for omitting either signal. The ceiling variation: every C-77 and C-78 signal is a table row the Auditor can flag as WRONG_SCHEMA or MISSING — the omission path that plagued prior rounds becomes structurally visible.

---

You are simulating a Copilot Studio conversation-flow trace for: {{topic}}

Five sequential roles execute this protocol. Silent fallthrough between roles is a structural violation. Every role transition is bidirectionally locked: outgoing HANDOFF_TO token + incoming receive acknowledgment. All transitions are declared in the LIFECYCLE_PROTOCOL section; role instructions reference by transition number only.

---

### LIFECYCLE_PROTOCOL (SOLE_AUTHORITY — MANDATORY NAMED SECTION)

**DIRECTIVE:** This section MUST be authored as a FIELD|VALUE table. It is the declaration layer for all role-transition events.

| FIELD | VALUE |
|-------|-------|
| SECTION_NAME | LIFECYCLE_PROTOCOL |
| AUTHORITY_CLASS | SOLE_AUTHORITY |
| DECLARATION_LAYER | This section: every role-transition event is declared exactly once here, and nowhere else in role instruction blocks. |
| REFERENCE_LAYER | Phase 6-A LIFECYCLE_POINTER_AUDIT: verifies every pointer of the form "per LIFECYCLE_PROTOCOL Transition T-N" in role instruction blocks resolves to a labeled transition in this section. |
| CLOSURE_STATEMENT | Neither layer alone closes the single-source enforcement system. Declaration-layer discipline without reference-layer verification leaves dangling pointers to non-existent or re-numbered transitions undetected. Reference-layer verification without declaration-layer discipline allows unauthorized re-declarations that create divergence points. Both layers must operate simultaneously. |
| SILENT_FALLTHROUGH_RULE | Silent fallthrough between roles is a structural violation. Every role boundary MUST carry both an outgoing HANDOFF_TO token and an incoming receive acknowledgment. |
| T-1 | Phase -1 → Topology Architect. Outgoing: `HANDOFF_TO: TOPOLOGY ARCHITECT`. Incoming: `"Received PRE_FLIGHT_MANIFEST."` |
| T-2 | Topology Architect → Contract Auditor. Outgoing: `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`. Incoming: `"Received Phase 0-A artifacts."` |
| T-3 | Contract Auditor → Developer. Outgoing: `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER`. Incoming: `"Received GATE_STATUS: [value]. Proceeding\|Blocked."` |
| T-4 | Developer → Auditor. Outgoing: `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR`. Incoming: `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` |
| T-5 | Auditor → Report Producer. Outgoing: `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`. Incoming: `"Received AUDITOR_CERTIFICATION: COMPLETE."` |

**DIRECTIVE:** Every role instruction block MUST reference transitions by T-N number only. Any inline re-declaration of HANDOFF_TO or receive-acknowledgment text outside this section is an UNAUTHORIZED_DIVERGENCE_POINT structural violation.

---

### PHASE -1 — CONTRACT AUDITOR (Pre-Flight Manifest)

**DIRECTIVE:** Issue PRE_FLIGHT_MANIFEST (REQUIRED_DECLARATION|PHASE_REF|SCHEMA_TYPE|STATUS: PENDING). All 11 declarations. SCHEMA_TYPE = FIELD|VALUE for 0-A-6, 0-A-8, 0-A-9, 0-A-10, 0-A-11. Close per LIFECYCLE_PROTOCOL T-1.

---

### PHASE 0 — TOPOLOGY ARCHITECT

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-1 receive acknowledgment.

Author Phase 0-D-1 through 0-D-5 and Phase 0-A-6 through 0-A-11. FIELD|VALUE declarations: two-column table rows only; prose substitution is WRONG_SCHEMA by definition.

**COLUMN_SCHEMA_CONTRACT** (required table before Phase 1):

| COLUMN_NAME | FORMAT | ALLOWED_VALUES | REQUIRED_WHEN |
|-------------|--------|----------------|---------------|
| (declare all non-core columns here) | | | |

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-2.

---

### PHASE 0-CA-1 — CONTRACT AUDITOR (Completeness Gate)

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-2 receive acknowledgment.

Update manifest rows (COMPLETE|MISSING|WRONG_SCHEMA). A FIELD|VALUE declaration authored in multi-column or prose format MUST be marked WRONG_SCHEMA (not MISSING). Verify all deltas (COVERAGE_DELTA, CHAIN_BUDGET_DELTA, PREDICTION_CONTRACT_SIGNED, STATUS_QUO_METHOD_SIGNED, COLUMN_SCHEMA_COMPLETE). Per FIELD|VALUE declaration: `NAME: PASS|FAIL (count N rows: [breakdown])`. PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL.

**DIRECTIVE — CONTRACT_AUDIT_GATE_HONORED SCHEMA:** Emit as FIELD|VALUE table. Every field below is mandatory; a missing row is a schema gap the Phase 6-A Auditor MUST flag as a gate structural finding:

| FIELD | VALUE |
|-------|-------|
| STATUS | PASS\|FAIL |
| STANDALONE_DECLARATION | This CONTRACT_AUDIT_GATE_HONORED block is a complete standalone audit summary. A verifier reading this block does not need to navigate to Phase 6-A tables or Phase 0-CA-1 output to confirm format compliance (WRONG_SCHEMA sweep) and row-count completeness (parenthetical verification). |
| WRONG_SCHEMA_RESIDUAL_SWEEP | CONFIRMED\|NOT_CONFIRMED (sweep scope: [named declarations checked]; or "CLEAN — no WRONG_SCHEMA rows found") |
| PARENTHETICAL_VERIFICATION | CONFIRMED\|NOT_CONFIRMED ([DECLARATION: N rows CONFIRMED, ...]) |
| BUDGET_UTILIZATION_VERIFIED | PASS\|FAIL |
| BUDGET_STATUS_CONSISTENT | PASS\|FAIL |

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-3.

---

### PHASE 1–5 — DEVELOPER

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-3 receive acknowledgment. GATE_STATUS: FAIL blocks execution — document block reason and stop.

**Phase 1** Turn table: every COLUMN_SCHEMA_CONTRACT column present in every row. Phase 1-S SESSION_TIMELINE (mutation log) MUST precede Phase 1 SESSION_STATE authoring; SESSION_STATE cells MUST cite Phase 1-S source entry.

**Phase 1-T** Topic aggregate (strictly additive: does not replace Phase 1 turn table). Columns: TOPIC_ID|TURNS_VISITED|SESSION_VARIABLES_SET_READ|DEFECT_CITATIONS|ADVERSARIAL_INJECTION_COUNT|CONFORMANCE_ROLLUP|PATH_IDS_MATCHED.

**Phase 2** Nine defect classes:
1. Dead end 2. Infinite loop 3. Intent collision 4. Missing fallback 5. TIMELINE_ANOMALY 6. PREDICTION_DEVIATION 7. CHAIN_BUDGET_EXCEEDED 8–9. [remaining structural classes]

P0 defects: EXECUTION_HALT block (HALT_TRIGGER|ROOT_CAUSE|MVF_RECOMMENDATION|MVF_SCOPE|UNBLOCKED_BY|CHAIN_BREAK_TRACE: BROKEN_CHAIN+CHAIN_HEAD_CONV+FIRST_DEVIATE_TURN+SUSPENDED_CONVS+BREAK_TO_DEFECT_PATH|CHAIN_REPAIR: list of CONV-NNs) BEFORE lower-severity defects.

**Phase 3** ENTANGLEMENT_MAP (3-E): ENTANGLEMENT_VERDICT per FOUND defect.

**Phase 4** Fallback chain trace to completion. Escalation path trace. Disambiguation strategy per intent collision.

**Phase 4-SQ** STATUS_QUO_SIMULATION: abbreviated trace using only STATUS_QUO_METHOD. No CONSTRAINT_VERDICTS, no CHAIN_EFFECTS, no PREDICTION_MATCH, no TIMELINE_ANOMALY, no CHAIN_BUDGET tracking. Per turn: TURN_ID|TOPIC_MATCHED|AGENT_RESPONSE_SUMMARY|SQ_DEFECT_FOUND|SQ_DEFECT_CLASS|REMARKS. STATUS_QUO_FINDINGS summary after.

**Phase 5** In sequence:
1. DEVIATION_BUDGET_UTILIZATION (SEVERITY|BUDGET|ACTUAL_DEVIATES|STATUS; OVERALL_BUDGET_STATUS; BUDGET_EXCEEDED_FINDING if exceeded)
2. CHAIN_BUDGET_UTILIZATION (HEAD_CONV|CHAIN_BUDGET|HEAD_DEVIATES_COUNT|STATUS per chain; CHAIN_BUDGET_EXCEEDED findings per exceeded chain)
3. COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (CLEAN requires TIMELINE_ANOMALY_RATE = 0; DEGRADED makes all five ratios PROVISIONAL)
4. CONSTRAINT_CHAIN_STATUS_SUMMARY (CHAIN_ID|HEAD_CONV|CHAIN_LENGTH|TURNS_SUSPENDED|FINAL_STATUS; BROKEN chains cross-reference EXECUTION_HALT block)
5. Five coverage ratios: topic_coverage_ratio (topics_visited/total_declared) · transitions_exercised/total_declared · slot_path_coverage · TIMELINE_ANOMALY_RATE · PATH_ADHERENCE_RATIO (turns_on_any_predicted_path/total_turns)
6. Phase 5-F STATUS_QUO_COVERAGE: per FOUND defect DEFECT_ID|DEFECT_CLASS|FOUND_BY_SIMULATION|FOUND_BY_STATUS_QUO|DETECTION_METHOD|SQ_BLIND_SPOT. STATUS_QUO_GAP_SUMMARY: FOUND_BY_SIMULATION_ONLY_COUNT + FOUND_BY_SIMULATION_ONLY_LIST + STRUCTURAL_BLIND_SPOTS_ACTIVATED + STATUS_QUO_GAP_NARRATIVE.

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-4.

---

### PHASE 6 — AUDITOR

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-4 receive acknowledgment.

**Phase 6-A:**

**DIRECTIVE:** Emit CONTRACT_AUDIT_GATE_HONORED as FIELD|VALUE table per schema declared in Phase 0-CA-1. Every field is mandatory. STANDALONE_DECLARATION field MUST be populated with prescribed text; an empty or missing STANDALONE_DECLARATION row is a Phase 6-A structural gap finding (equivalent to a MISSING gate field). Include:

- LIFECYCLE_POINTER_AUDIT sub-table: enumerate every "per LIFECYCLE_PROTOCOL Transition T-N" reference found across all role instruction blocks (ROLE|POINTER_TEXT|TARGET_TRANSITION|RESOLVED: YES|NO). Unresolved = DANGLING_LIFECYCLE_POINTER finding.
- SIMULATION_DELTA_COMPLETE: PASS|FAIL (every Phase 2 FOUND defect appears in exactly one DETECTION_METHOD category in Phase 5-F STATUS_QUO_COVERAGE).

**Phase 6-B** Severity Co-Residency Audit: structured table; every FOUND defect row verified for both SEVERITY_CLASS and INVARIANT_CITE; CONFIRMED_ABSENT rows EXEMPT.

**Phase 6-C** Entanglement consistency: verify Phase 3-E ENTANGLEMENT_MAP against Phase 1 turn-level evidence.

**Phase 6-D** Topic aggregate consistency: conformance_rollup in Phase 1-T vs DEVIATES count derived from Phase 1 per topic; TOPIC_ROLLUP_MISMATCH findings.

**Phase 6-E** Session timeline consistency: replay Phase 1-S mutations turn-by-turn; compare reconstructed SESSION_STATE to Phase 1 SESSION_STATE column; TIMELINE_STATE_MISMATCH findings.

**Phase 6-F** Fix Viability: per EXECUTION_HALT block — CONV_VIOLATIONS_INTRODUCED|CONV_VIOLATIONS_DETAIL|VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[CONV-NN list]|CHAIN_REPAIR_COMPLETE.

**Phase 6-G** Chain Integrity: per CHAIN-NN — verify CHAIN_EFFECTS in Phase 1 against upstream CONV-NN verdicts; CHAIN_VERDICT_INCONSISTENCY findings; CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED table with CONSISTENT: PASS|FAIL.

**Phase 6-H** Combined:
- PATH_ADHERENCE_AUDIT: per-turn PREDICTION_MATCH reported vs audited; PATH_ADHERENCE_RATIO_VERIFIED; CRITICAL_PATH_ESCALATION_VERIFIED.
- PLAN_INTEGRITY_AUDIT: EXECUTION_HALT_IN_PLAN + CHAIN_REPAIR_IN_SCOPE per EXECUTION_HALT block; DEPENDENCY_ORDER_VALID per PLAN_ITEM; PLAN_INTEGRITY_AUDIT: PASS|FAIL; DEPENDENCY_CYCLE_CHECK.
- PLAN_TIER_OVERRIDE_PRESENT + OVERRIDE_TIER_HONORED for CRITICAL-path PREDICTION_DEVIATION defects.
- STATUS_QUO_COVERAGE_AUDIT: DETECTION_METHOD_REPORTED vs DETECTION_METHOD_AUDITED per FOUND defect; AUTOMATIC_CLASSIFICATION_VERIFIED block (three auto-classification rules); STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL.

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-5.

---

### PHASE 7 — REMEDIATION PLANNER

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-5 receive acknowledgment.

Topologically sorted REMEDIATION_PLAN. Per FOUND defect: PLAN_ITEM (PLAN_ID: RP-NN|DEFECT_REF|SEVERITY_CLASS|SCOPE|DEPENDENCY_ON|PLAN_TIER|TIER_RATIONALE|CHAIN_REPAIR_ITEMS|UNBLOCKED_BY). CRITICAL-path PREDICTION_DEVIATION defects carry PLAN_TIER_OVERRIDE: IMMEDIATE ("CRITICAL path deviation — overrides severity-based tier"). Topological sort rule: no PLAN_ITEM before any item in its DEPENDENCY_ON list. PLAN_SUMMARY: PLAN_ITEM_COUNT|IMMEDIATE_COUNT|NEXT_SPRINT_COUNT|BACKLOG_COUNT|DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND.
