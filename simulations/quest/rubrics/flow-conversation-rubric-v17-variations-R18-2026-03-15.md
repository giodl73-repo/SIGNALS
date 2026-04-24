# Quest Variations — flow-conversation — Round 18 (v17 rubric)

**Date:** 2026-03-15 | **Rubric version:** v17 | **Max score:** 246

---

## Variation Axes Selected

All 5 variations carry the full v17 baseline: C-01 through C-71. Each is designed to
surface one or more of the three new criteria C-72 through C-74.

**New axes for R18 (targeting C-72, C-73, C-74):**

- **Axis V — Pointer-resolution audit (C-73 target)**: Phase 6-A gains a
  LIFECYCLE_POINTER_AUDIT block that enumerates every pointer reference of the form
  "per LIFECYCLE_PROTOCOL Transition N" across all role instruction blocks and verifies
  each cited transition number resolves to a labeled entry in the LIFECYCLE_PROTOCOL
  section. Each pointer is reported as ROLE | POINTER_TEXT | TARGET_TRANSITION |
  RESOLVED: YES|NO. An unresolved pointer earns FINDING: DANGLING_LIFECYCLE_POINTER.
  A Phase 6-A carrying C-70 PASS but no LIFECYCLE_POINTER_AUDIT does not satisfy C-73.
  C-73 requires C-70 PASS.

- **Axis W — Sweep-scope citation in gate field (C-72 target)**: The
  WRONG_SCHEMA_RESIDUAL_SWEEP gate field (satisfying C-69) is extended to name every
  FIELD|VALUE-annotated declaration from Phase 0-CA-1 that was included in the residual
  sweep. Format when no WRONG_SCHEMA rows: `CLEAN (no WRONG_SCHEMA rows; sweep scope:
  Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9], Turn Prediction Contract
  [0-A-10], Status Quo Method [0-A-11])`. When rows existed and were resolved: `CLEAN
  ([N] row[s] resolved; sweep scope: [declaration names])`. When unresolved:
  `FINDINGS_PRESENT (sweep scope: [names with unresolved residuals])`. A gate field with
  only CONFIRMED|NOT_CONFIRMED satisfies C-69; C-72 requires explicit scope citation.
  C-72 requires C-69 PASS.

- **Axis X — Parenthetical declaration citation in gate field (C-74 target)**: The
  PARENTHETICAL_VERIFICATION gate field (satisfying C-71) is extended to name each
  verified declaration with its confirmed row count inline. Format: `PARENTHETICAL_
  VERIFICATION: PASS; declarations verified: DEVIATION_BUDGET: [N] rows CONFIRMED,
  CONV_CHAIN_BUDGET: [N] rows CONFIRMED, TURN_PREDICTION_CONTRACT: [N] rows CONFIRMED,
  STATUS_QUO_METHOD: [N] rows CONFIRMED before Phase 1: CONFIRMED`. A gate field with
  only CONFIRMED|NOT_CONFIRMED satisfies C-71; C-74 requires declaration names and row
  counts cited. C-74 requires C-71 PASS.

**Single-axis (3):** V, W, X

- **Axis V** — LIFECYCLE_POINTER_AUDIT in Phase 6-A; SOLE_AUTHORITY + pointer-only as
  C-70 prerequisite; gate uses simple sweep toggle (C-69, no scope) and simple
  parenthetical toggle (C-71, no declaration citation)
- **Axis W** — Sweep scope citation in gate first field; inline lifecycle (no
  SOLE_AUTHORITY, C-70/C-73 unaddressed); no LIFECYCLE_POINTER_AUDIT
- **Axis X** — Parenthetical declaration citation in gate second field; inline lifecycle
  with CONSTRAINT phrasing register; no LIFECYCLE_POINTER_AUDIT; no sweep scope citation

**Combined (2):**

- **Axes V+W** — LIFECYCLE_PROTOCOL section + LIFECYCLE_POINTER_AUDIT + sweep scope
  citation; parenthetical without declaration citation; targets C-73 + C-72
- **Axes V+W+X** — Full R18 combination; all three axes; targets C-73 + C-72 + C-74

---

## V-01 — Axis V: Lifecycle Pointer Resolution Audit

**Variation axis:** Lifecycle emphasis — Phase 6-A gains a LIFECYCLE_POINTER_AUDIT block
that enumerates every pointer reference of the form "per LIFECYCLE_PROTOCOL Transition N"
across all role instruction blocks and verifies each cited transition number resolves to
a labeled entry in the dedicated LIFECYCLE_PROTOCOL section. The SOLE_AUTHORITY declaration
and pointer-only role instructions (C-70 prerequisites) are carried forward from R17. The
gate uses the C-69 sweep field (simple CONFIRMED toggle, no scope citation) and the C-71
parenthetical field (simple CONFIRMED toggle, no declaration citation). The only new
addition is the LIFECYCLE_POINTER_AUDIT table in Phase 6-A.

**Hypothesis:** R17 achieved C-70 PASS by extracting all HANDOFF_TO and Received strings
into a dedicated LIFECYCLE_PROTOCOL section with SOLE_AUTHORITY, and replacing all inline
tokens in role instructions with pointer-only references. However, no R17 variation
verified that the pointer references themselves resolved — "per LIFECYCLE_PROTOCOL
Transition 6" would pass the C-70 check even if the section only defines Transitions 1–5.
C-73 requires Phase 6-A to enumerate every such pointer across all role instruction blocks,
check each against the section's labeled transitions, and emit DANGLING_LIFECYCLE_POINTER
findings for any that do not resolve. Without this audit, single-source enforcement is
verified at the declaration level only, not the reference level. C-72 (scope citation in
sweep field) and C-74 (declaration citation in parenthetical field) are not introduced.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this
section. Role instructions reference transitions by section name and transition number
only. A HANDOFF_TO or Received string appearing in any role instruction block is a
lifecycle single-source violation.

Every role transition is a declared protocol event. The outgoing role MUST emit the token
declared below before its successor begins. The incoming role MUST open with the matching
acknowledgment before authoring any content. Implicit phase adjacency does not satisfy
this contract.

```
Transition 1 — Phase -1 issuer → Topology Architect
  Outgoing:  HANDOFF_TO: TOPOLOGY ARCHITECT
  Incoming:  "Received PRE_FLIGHT_MANIFEST."

Transition 2 — Topology Architect → Contract Auditor
  Outgoing:  HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1
  Incoming:  "Received Phase 0 from Topology Architect."

Transition 3 — Contract Auditor → Developer
  Outgoing:  GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER
  Incoming:  "Received GATE_STATUS: [value]. Proceeding|Blocked."

Transition 4 — Developer → Auditor
  Outgoing:  DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR
  Incoming:  "Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."

Transition 5 — Auditor → Report Producer
  Outgoing:  AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER
  Incoming:  "Received AUDITOR_CERTIFICATION: COMPLETE."
```

A role that begins authoring without the incoming acknowledgment declared in this section
is a lifecycle gap finding, regardless of whether the outgoing token was present.

---

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10,
0-A-11) use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema
contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1 outgoing. The Topology Architect may
not begin Phase 0-D-0 until this manifest exists.

```
PRE_FLIGHT_MANIFEST (Phase -1):

REQUIRED_DECLARATION                           | PHASE_REF | SCHEMA_TYPE   | STATUS
-----------------------------------------------|-----------|---------------|--------
COLUMN_SCHEMA_REGISTRY                         | 0-D-0     | TABLE         | PENDING
Topic Registry                                 | 0-D-1     | TABLE         | PENDING
Vocabulary Gate                                | 0-D-2     | TABLE         | PENDING
Session Variable Registry                      | 0-D-3     | TABLE         | PENDING
Invariant Register                             | 0-D-4     | TABLE         | PENDING
Transition Map                                 | 0-D-5     | TABLE         | PENDING
Session Variable Timeline Contract             | 0-A-6     | TABLE         | PENDING
Invariant Chain Declaration                    | 0-A-7     | TABLE         | PENDING
Deviation Budget                               | 0-A-8     | FIELD|VALUE   | PENDING
Constraint Chain Budget                        | 0-A-9     | FIELD|VALUE   | PENDING
Turn Prediction Contract                       | 0-A-10    | FIELD|VALUE   | PENDING
Status Quo Method                              | 0-A-11    | FIELD|VALUE   | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
```

Close per LIFECYCLE_PROTOCOL Transition 1 outgoing.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per LIFECYCLE_PROTOCOL Transition 1 incoming.

**Phase 0-D-0 — Column Schema Registry (first artifact)**

| COLUMN_NAME         | FORMAT                          | ALLOWED_VALUES                                                        | REQUIRED_WHEN    |
|---------------------|---------------------------------|-----------------------------------------------------------------------|------------------|
| TURN_ID             | T-NN                            | T-01, T-02, ...                                                       | Every turn       |
| USER_UTTERANCE      | free text                       | any                                                                   | Every turn       |
| TOPIC_MATCHED       | TOPIC_ID                        | declared topics, CONTRACT_GAP                                         | Every turn       |
| NODES_EXECUTED      | comma-separated                 | any                                                                   | Every turn       |
| AGENT_RESPONSE      | free text                       | any                                                                   | Every turn       |
| TRANSITION_TARGET   | TOPIC_ID or terminal            | declared topics, TERMINAL, FALLBACK                                   | Every turn       |
| SESSION_STATE       | replayed from Phase 1-S         | variable=value pairs                                                  | Every turn       |
| CONFORMANCE         | verdict                         | CONFORMS, DEVIATES[CONV-NN]                                           | Every turn       |
| CONSTRAINT_VERDICTS | CONV-NN evaluation list         | PASS, FAIL, CHAIN_SUSPENDED[chain head: CONV-NN broke at TURN_ID]     | Every turn       |
| CHAIN_EFFECTS       | propagation effects             | CONV-NN → [CONV-NN: ACTIVATED\|SUSPENDED, ...]                        | Every turn       |
| PREDICTION_MATCH    | path match                      | ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual], OFF_ALL_PATHS | Every turn       |
| SLOT_FILL_STATUS    | slot=RESULT                     | FILLED, SKIPPED, INTERRUPTED                                          | Slot-fill turns  |

**Phase 0-D-1 — Topic Registry**
```
TOPIC_ID | TRIGGER_PHRASES | ENTRY_CONDITIONS | EXIT_TARGETS
```

**Phase 0-D-2 — Vocabulary Gate**
```
TERM | CLASS: PERMITTED|PROHIBITED | RATIONALE
```
Sign: VOCABULARY_GATE_SIGNED: YES

**Phase 0-D-3 — Session Variable Registry**
```
NAME | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL | INITIAL_VALUE
```

**Phase 0-D-4 — Invariant Register**
```
CONV-NN | DESCRIPTION | FALSIFICATION_CONDITION | PROPAGATION | CHAIN_ID
```

**Phase 0-D-5 — Transition Map**
```
TRANS-NN | SOURCE_TOPIC | TARGET_TOPIC | CONDITION | REQUIRED|OPTIONAL
```

**Phase 0-A-6 — Session Variable Timeline Contract**
```
VARIABLE | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED | AUTHORIZED_REWRITERS
```
Every variable from Phase 0-D-3 must have a row. A write from a topic absent from
FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS is an OFF_CONTRACT_WRITE anomaly.

**Phase 0-A-7 — Invariant Chain Declaration**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | PROPAGATION_SEQUENCE
```

**Phase 0-A-8 — Deviation Budget (FIELD|VALUE rows required)**
```
FIELD        | VALUE
-------------|-------------------------------------------
P0_MAX       | [0 = any P0 is BUDGET_EXCEEDED]
P1_MAX       | [integer]
P2_MAX       | [integer]
P3_MAX       | [integer]
RATIONALE    | [one sentence]
BUDGET_LOCK  | BUDGET LOCKED — may not be revised after Phase 1-S begins
```

**Phase 0-A-9 — Constraint Chain Budget (FIELD|VALUE block per chain)**
One block per CHAIN-NN from Phase 0-A-7:
```
FIELD          | VALUE
---------------|--------------------------------
CHAIN_ID       | CHAIN-NN
HEAD_CONV      | CONV-NN
CHAIN_LENGTH   | [integer]
CHAIN_BUDGET   | [max chain-head DEVIATES turns]
RATIONALE      | [one sentence]
```

**Phase 0-A-10 — Turn Prediction Contract (FIELD|VALUE block per path)**
HP-01 required; up to 3 ALT-NN paths:
```
FIELD                    | VALUE
-------------------------|--------------------------------
PATH_ID                  | HP-01 | ALT-NN
PATH_DESCRIPTION         | [scenario narrative]
PATH_CRITICALITY         | CRITICAL|IMPORTANT|INFORMATIONAL
PREDICTED_TURN_SEQUENCE  | [ordered TOPIC_ID list]
```
```
FIELD                            | VALUE
---------------------------------|------
TURN_PREDICTION_CONTRACT_SIGNED  | YES
```
CRITICAL paths: PREDICTION_DEVIATION auto-elevates to P1 minimum severity.

**Phase 0-A-11 — Status Quo Method Declaration (FIELD|VALUE rows required)**
```
FIELD                     | VALUE
--------------------------|----------------------------------------------------------
METHOD_NAME               | [short label]
METHOD_DESCRIPTION        | [one paragraph]
METHOD_COVERAGE           | [what the method checks]
BLIND_CONSTRAINT_VERDICTS | YES|NO
BLIND_CHAIN_EFFECTS       | YES|NO
BLIND_TIMELINE_ANOMALIES  | YES|NO
BLIND_PREDICTION_CONTRACT | YES|NO
BLIND_CHAIN_BUDGET        | YES|NO
STATUS_QUO_METHOD_SIGNED  | YES
```

Close per LIFECYCLE_PROTOCOL Transition 2 outgoing.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per LIFECYCLE_PROTOCOL Transition 2 incoming.

Update manifest. STATUS values: COMPLETE (present and correct format) | MISSING (absent
entirely) | WRONG_SCHEMA (present but uses prose or non-FIELD|VALUE format for a
FIELD|VALUE-annotated row). WRONG_SCHEMA counts as non-COMPLETE and blocks Phase 1
alongside MISSING rows.

```
PRE_FLIGHT_MANIFEST (resolved):

REQUIRED_DECLARATION                           | PHASE_REF | SCHEMA_TYPE   | STATUS
-----------------------------------------------|-----------|---------------|---------------------------
COLUMN_SCHEMA_REGISTRY                         | 0-D-0     | TABLE         | COMPLETE|MISSING
Topic Registry                                 | 0-D-1     | TABLE         | COMPLETE|MISSING
Vocabulary Gate                                | 0-D-2     | TABLE         | COMPLETE|MISSING
Session Variable Registry                      | 0-D-3     | TABLE         | COMPLETE|MISSING
Invariant Register                             | 0-D-4     | TABLE         | COMPLETE|MISSING
Transition Map                                 | 0-D-5     | TABLE         | COMPLETE|MISSING
Session Variable Timeline Contract             | 0-A-6     | TABLE         | COMPLETE|MISSING
Invariant Chain Declaration                    | 0-A-7     | TABLE         | COMPLETE|MISSING
Deviation Budget                               | 0-A-8     | FIELD|VALUE   | COMPLETE|MISSING|WRONG_SCHEMA
Constraint Chain Budget                        | 0-A-9     | FIELD|VALUE   | COMPLETE|MISSING|WRONG_SCHEMA
Turn Prediction Contract                       | 0-A-10    | FIELD|VALUE   | COMPLETE|MISSING|WRONG_SCHEMA
Status Quo Method                              | 0-A-11    | FIELD|VALUE   | COMPLETE|MISSING|WRONG_SCHEMA

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
```

Then emit Phase 0-CA-1 output. Row-count parentheticals are mandatory for each
DECLARATION_SCHEMA_COMPLETE verdict:

```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list — VARS_IN_TOPOLOGY not in VARS_IN_CONTRACT]
  CHAIN_BUDGET_DELTA: [empty or list — CHAINS_IN_TOPOLOGY not in CHAINS_IN_BUDGET]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET:         PASS|FAIL (count N rows: [breakdown, e.g. "6 rows: P0/P1/P2/P3/RATIONALE/BUDGET_LOCK"])
    CONV_CHAIN_BUDGET:        PASS|FAIL (count N rows: [5 fields per chain × M chains])
    TURN_PREDICTION_CONTRACT: PASS|FAIL (count N rows: [4 rows per path × M paths + 1 signed row])
    STATUS_QUO_METHOD:        PASS|FAIL (count N rows: [3 metadata + 5 BLIND + SIGNED = 9])
  PREDICTION_CONTRACT_SIGNED:    YES|NO
  STATUS_QUO_METHOD_SIGNED:      YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE
FAIL, any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 3 incoming. GATE_STATUS: FAIL blocks Phase 1.
Any Phase 1 content following a received GATE_STATUS: FAIL is an unauthorized execution
finding.

**Phase 1-S — Session Variable Mutation Log (author BEFORE Phase 1)**
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE cells in Phase 1 are derived by replaying Phase 1-S in turn order.

**Phase 1 — Turn-by-Turn Trace**
One row per turn; all columns from Phase 0-D-0. No turns skipped or collapsed.
No prohibited vocabulary (Phase 0-D-2). Inject at least one adversarial utterance;
record injection TURN_ID, system response, defect triggered (if any), recovery path.

**Phase 1-T — Topic Aggregate (additive to Phase 1)**
```
TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ |
DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP | PATH_IDS_MATCHED
```

**Phase 2 — Defect Classification**
Nine defect classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP.

For each FOUND defect:
```
DEFECT_ID | DEFECT_CLASS | LOCATION (topic/turn) | SEVERITY_CLASS: P0|P1|P2|P3 |
INVARIANT_CITE (CONV-NN) | REPRODUCTION_STEPS | RECOVERY |
ENTANGLEMENT_VERDICT | [PLAN_TIER_OVERRIDE: IMMEDIATE — CRITICAL path deviations only]
```

For each FOUND P0 defect, emit before classifying lower-severity defects:
```
EXECUTION_HALT:
  HALT_TRIGGER: [defect class and topic/turn]
  ROOT_CAUSE: [one sentence]
  MVF_RECOMMENDATION: [smallest change eliminating P0]
  MVF_SCOPE: [topics/transitions/variables touched]
  UNBLOCKED_BY: [observable confirmation]
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN: [CHAIN-NN]
    CHAIN_HEAD_CONV: [CONV-NN]
    FIRST_DEVIATE_TURN: [TURN_ID]
    SUSPENDED_CONVS: [list]
    BREAK_TO_DEFECT_PATH: [narrative]
  CHAIN_REPAIR: [CONV-NNs to re-evaluate]
```

**Phase 3-E — Entanglement Map**
```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_CLASS]|MASKED_BY[DEFECT_CLASS]
```

**Phase 4 — Fallback, Escalation, Disambiguation**
Trace one fallback path to completion. Trace one escalation (trigger, handoff node,
session state at handoff, receipt confirmation). For intent collisions: disambiguation
strategy with rationale.

**Phase 4-SQ — Status Quo Simulation**
Re-run using ONLY STATUS_QUO_METHOD from Phase 0-A-11. No CONSTRAINT_VERDICTS,
CHAIN_EFFECTS, PREDICTION_MATCH, TIMELINE_ANOMALY, or CHAIN_BUDGET tracking.
```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO |
SQ_DEFECT_CLASS | REMARKS
```
Close: STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND, SQ_DEFECTS_NOT_FOUND.

**Phase 5-A — Deviation Budget Utilization**
```
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
```
OVERALL_BUDGET_STATUS: WITHIN_BUDGET|EXCEEDED.

**Phase 5-B — Chain Budget Utilization**
```
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
```

**Phase 5-C — Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```

**Phase 5-D — Coverage Quality Gate + Five Ratios**
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (DEGRADED when TIMELINE_ANOMALY_RATE > 0).
1. TOPIC_COVERAGE_RATIO = topics_visited / total_declared
2. TRANSITION_COVERAGE_RATIO = transitions_exercised / total_declared
3. SLOT_PATH_COVERAGE_RATIO = slot_paths_completed / total_slot_paths
4. TIMELINE_ANOMALY_RATE = timeline_anomalies_found / total_variable_turn_events
5. PATH_ADHERENCE_RATIO = turns_on_any_predicted_path / total_turns

**Phase 5-F — Status Quo Coverage Table**
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION: YES|NO | FOUND_BY_STATUS_QUO: YES|NO |
DETECTION_METHOD | SQ_BLIND_SPOT
```
Auto-classification: PREDICTION_DEVIATION → FOUND_BY_SIMULATION_ONLY when
BLIND_PREDICTION_CONTRACT: YES; CHAIN_BUDGET_EXCEEDED when BLIND_CHAIN_BUDGET: YES;
TIMELINE_ANOMALY when BLIND_TIMELINE_ANOMALIES: YES.
Close with STATUS_QUO_GAP_SUMMARY.

Close per LIFECYCLE_PROTOCOL Transition 4 outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Run WRONG_SCHEMA_RESIDUAL_CHECK first:
```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO → FINDING: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows in Phase 0-CA-1) |
                              CLEAN (all WRONG_SCHEMA rows resolved) |
                              FINDINGS_PRESENT[list of unresolved declarations]
```

Run PARENTHETICAL_PRESENCE_VERIFICATION second:
```
PARENTHETICAL_PRESENCE_VERIFICATION:

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |

  PARENTHETICAL_PRESENT: YES iff CA output shows "(count N rows: [breakdown])" inline
  with the verdict. NO → FINDING: PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL[DECLARATION]

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical: list]
```

Run LIFECYCLE_POINTER_AUDIT third:
```
LIFECYCLE_POINTER_AUDIT:

Enumerate every pointer reference of the form "per LIFECYCLE_PROTOCOL Transition N"
or "LIFECYCLE_PROTOCOL Transition N incoming/outgoing" across all role instruction
blocks in this prompt (ROLE 1 Phase -1, ROLE 2 Phase 0, ROLE 1 Phase 0-CA-1,
ROLE 3 Phases 1-5, ROLE 4 Phase 6, ROLE 5 Phase 7).

For each pointer reference found:

  ROLE              | POINTER_TEXT                                  | TARGET_TRANSITION | RESOLVED: YES|NO | FINDING
  ------------------|-----------------------------------------------|-------------------|------------------|--------
  [role name/phase] | [exact pointer text from role instructions]   | Transition N      | YES|NO           |

  Rules:
    - RESOLVED: YES if Transition N appears as a labeled entry in LIFECYCLE_PROTOCOL
      (Transitions 1–5 are the labeled entries in this prompt)
    - RESOLVED: NO → FINDING: PHASE_6A_FINDING: DANGLING_LIFECYCLE_POINTER[ROLE, Transition N]
    - A pointer citing a transition number outside the declared range is DANGLING
      regardless of intent

LIFECYCLE_POINTER_AUDIT_STATUS: CLEAN (all [N] pointers resolved) |
                                 FINDINGS_PRESENT[list of DANGLING_LIFECYCLE_POINTER findings]
```

Then emit gate assertion:
```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED
  PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category
  — PASS|FAIL
```

Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B — Severity Co-Residency Audit**
Per FOUND defect: SEVERITY_CLASS present + INVARIANT_CITE present. Structured table.
CONFIRMED_ABSENT rows are EXEMPT.

**Phase 6-C — Entanglement Consistency Audit**
Verify Phase 3-E map against Phase 1 turn-level evidence.

**Phase 6-D — Topic Aggregate Consistency Audit**
Cross-check Phase 1-T CONFORMANCE_ROLLUP vs DEVIATES count per topic in Phase 1.
TOPIC_ROLLUP_MISMATCH finding for discrepancies.

**Phase 6-E — Session Timeline Consistency Audit**
Replay Phase 1-S; compare reconstructed SESSION_STATE vs Phase 1 SESSION_STATE column.
TIMELINE_STATE_MISMATCH finding for discrepancies.

**Phase 6-F — Fix Viability Audit**
Per EXECUTION_HALT: CONV_VIOLATIONS_INTRODUCED, CONV_VIOLATIONS_DETAIL,
VIABILITY: VIABLE|SIDE_EFFECTS_FOUND, CHAIN_REPAIR_COMPLETE.

**Phase 6-G — Chain Integrity Audit**
Per CHAIN-NN: CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL.

**Phase 6-H — Combined Plan / Path / Status Quo Audit**
*Plan:* EXECUTION_HALT_IN_PLAN, CHAIN_REPAIR_IN_SCOPE, DEPENDENCY_ORDER_VALID,
PLAN_INTEGRITY_AUDIT, DEPENDENCY_CYCLE_CHECK, PLAN_TIER_OVERRIDE_PRESENT,
OVERRIDE_TIER_HONORED.
*Path:* per-turn PREDICTION_MATCH_REPORTED vs PREDICTION_MATCH_AUDITED,
PATH_ADHERENCE_RATIO_VERIFIED, CRITICAL_PATH_ESCALATION_VERIFIED.
*Status quo:* per-defect DETECTION_METHOD_REPORTED vs DETECTION_METHOD_AUDITED,
AUTOMATIC_CLASSIFICATION_VERIFIED, STATUS_QUO_COVERAGE_AUDIT.

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per LIFECYCLE_PROTOCOL Transition 5 incoming.

For each FOUND defect, one PLAN_ITEM:
```
PLAN_ID: RP-NN
DEFECT_REF: [Phase 2 DEFECT_ID]
SEVERITY_CLASS: P0|P1|P2|P3
SCOPE: [topics/transitions/session variables]
DEPENDENCY_ON: [RP-NN list]
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG
TIER_RATIONALE: [rule applied]
CHAIN_REPAIR_ITEMS: [CONV-NN list; empty if none]
UNBLOCKED_BY: [observable confirmation]
```
Close: PLAN_SUMMARY: PLAN_ITEM_COUNT, IMMEDIATE_COUNT, NEXT_SPRINT_COUNT,
BACKLOG_COUNT, DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND.

---

## V-02 — Axis W: Sweep Scope Citation in Gate Field

**Variation axis:** Output format — the WRONG_SCHEMA_RESIDUAL_SWEEP gate field is extended
from a status toggle to a status-plus-manifest-citation format. The field value names
every FIELD|VALUE-annotated declaration from Phase 0-CA-1 that was included in the
residual sweep, making the gate assertion traceable to specific manifest rows rather than
an uncited CONFIRMED toggle. The lifecycle protocol is inline within role instructions
(no dedicated LIFECYCLE_PROTOCOL section; C-70 and C-73 are unaddressed). No
LIFECYCLE_POINTER_AUDIT. The parenthetical gate field uses the simple CONFIRMED toggle
(C-71 present, C-74 not introduced).

**Hypothesis:** R17 V-02 achieved C-69 PASS by embedding WRONG_SCHEMA_RESIDUAL_SWEEP as
the first field in CONTRACT_AUDIT_GATE_HONORED, with format `CLEAN before Phase 1:
CONFIRMED|NOT_CONFIRMED`. The CONFIRMED toggle asserts that the sweep ran and was clean,
but does not name which declarations were checked — a verifier cannot confirm coverage
from the gate field alone without cross-referencing the standalone WRONG_SCHEMA_RESIDUAL_
CHECK table. C-72 requires the gate field to carry an explicit scope citation: when no
WRONG_SCHEMA rows existed, `CLEAN (no WRONG_SCHEMA rows; sweep scope: Deviation Budget
[0-A-8], Constraint Chain Budget [0-A-9], Turn Prediction Contract [0-A-10], Status Quo
Method [0-A-11])`. The citation makes the gate self-describing: a reader knows precisely
what was in scope without navigating to Phase 0-CA-1. C-73 (pointer audit) and C-74
(declaration citation in parenthetical) are not introduced in this variation.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is an explicit bidirectional protocol event.
Silent fallthrough between roles is a structural violation. Each role issues an outgoing
handoff token; its successor opens with a matching acknowledgment.

**Lifecycle protocol transitions:**
1. Phase -1 close: `HANDOFF_TO: TOPOLOGY ARCHITECT` / open: `"Received PRE_FLIGHT_MANIFEST."`
2. Phase 0 close: `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1` / open: `"Received Phase 0 from Topology Architect."`
3. Phase 0-CA-1 close: `GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER` / open: `"Received GATE_STATUS: [value]. Proceeding|Blocked."`
4. Phase 5 close: `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR` / open: `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."`
5. Phase 6-A close: `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER` / open: `"Received AUDITOR_CERTIFICATION: COMPLETE."`

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10,
0-A-11) use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema
contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. The Topology Architect may not begin Phase 0-D-0 until this manifest
exists. [Same manifest structure as V-01 with SCHEMA_TYPE column and PENDING statuses.]

Close with: **HANDOFF_TO: TOPOLOGY ARCHITECT**

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST."**

[Phase 0-D-0 Column Schema Registry through Phase 0-A-11 Status Quo Method — identical
structure and instructions to V-01.]

Close with: **HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect."**

Update manifest with COMPLETE|MISSING|WRONG_SCHEMA statuses. WRONG_SCHEMA applies to
FIELD|VALUE-annotated rows where the declaration is present but uses prose or non-FIELD|
VALUE format. Both WRONG_SCHEMA and MISSING block Phase 1.

[Resolved manifest identical to V-01.]

Emit Phase 0-CA-1 output with mandatory row-count parentheticals per
DECLARATION_SCHEMA_COMPLETE verdict. [Phase 0-CA-1 block identical to V-01.]

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE
FAIL, any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

Close with: **GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
GATE_STATUS: FAIL blocks Phase 1.

[Phases 1-S through 5-F — identical structure and instructions to V-01.]

Close with: **DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**
The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Run WRONG_SCHEMA_RESIDUAL_CHECK first. [Identical table structure to V-01.]

Run PARENTHETICAL_PRESENCE_VERIFICATION second. [Identical table structure to V-01.]

Then emit gate assertion. The WRONG_SCHEMA_RESIDUAL_SWEEP field is the first gate
assertion and carries an explicit scope citation naming every FIELD|VALUE-annotated
declaration checked. When the sweep found no WRONG_SCHEMA rows, the field reads:
`CLEAN (no WRONG_SCHEMA rows; sweep scope: [declaration names from Phase 0-CA-1])`.
When rows existed and were all resolved: `CLEAN ([N] row[s] resolved; sweep scope:
[declaration names])`. When unresolved: `FINDINGS_PRESENT (sweep scope: [names])`.
A gate that asserts CONFIRMED without the scope citation does not satisfy C-72.

```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows; sweep scope:
    Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9],
    Turn Prediction Contract [0-A-10], Status Quo Method [0-A-11])
    before Phase 1: CONFIRMED|NOT_CONFIRMED
  PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category
  — PASS|FAIL
```

Close Phase 6-A with: **AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER**

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

[Identical PLAN_ITEM structure and PLAN_SUMMARY close to V-01.]

---

## V-03 — Axis X: Parenthetical Declaration Citation in Gate Field

**Variation axis:** Phrasing register — formal CONSTRAINT/MUST/PROHIBITED language frames
the parenthetical gate field as a declaration-traceability requirement, not a status toggle.
The PARENTHETICAL_VERIFICATION gate field carries an explicit citation of each verified
declaration and its confirmed row count, making the gate assertion traceable to the CA
output in Phase 0-CA-1. The lifecycle protocol is inline with CONSTRAINT framing (no
dedicated LIFECYCLE_PROTOCOL section; C-70 and C-73 unaddressed). No LIFECYCLE_POINTER_
AUDIT. The sweep gate field uses the simple CONFIRMED toggle (C-69 present, C-72 not
introduced). The parenthetical gate field is the only new addition.

**Hypothesis:** R17 V-03 achieved C-71 PASS by embedding `PARENTHETICAL_VERIFICATION:
PASS before Phase 1: CONFIRMED|NOT_CONFIRMED` as the second gate field. The toggle asserts
that all DECLARATION_SCHEMA_COMPLETE verdicts carried row-count parentheticals, but does
not name which declarations were verified or what row counts were confirmed — a verifier
must navigate to the standalone PARENTHETICAL_PRESENCE_VERIFICATION table to determine
coverage. C-74 requires the gate field to carry declaration names and their confirmed row
counts inline: `PARENTHETICAL_VERIFICATION: PASS; declarations verified: DEVIATION_BUDGET:
[N] rows CONFIRMED, CONV_CHAIN_BUDGET: [N] rows CONFIRMED, TURN_PREDICTION_CONTRACT: [N]
rows CONFIRMED, STATUS_QUO_METHOD: [N] rows CONFIRMED before Phase 1: CONFIRMED`. The
citation makes the gate self-describing. C-72 (scope citation in sweep field) and C-73
(pointer audit) are not introduced. Formal CONSTRAINT language reinforces that the
declaration citation is a structural obligation, not a quality observation.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is a declared structural constraint. Crossing
a role boundary without emitting the outgoing token AND without the successor opening with
the matching acknowledgment is a LIFECYCLE_CONSTRAINT_VIOLATION. Silent fallthrough is
PROHIBITED.

**Lifecycle protocol constraints:**
1. CONSTRAINT: Phase -1 MUST close with `HANDOFF_TO: TOPOLOGY ARCHITECT`.
   CONSTRAINT: Topology Architect MUST open with `"Received PRE_FLIGHT_MANIFEST."` before
   authoring Phase 0-D-0.
2. CONSTRAINT: Phase 0 MUST close with `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`.
   CONSTRAINT: Contract Auditor MUST open with `"Received Phase 0 from Topology
   Architect."` before Phase 0-CA-1.
3. CONSTRAINT: Phase 0-CA-1 MUST close with `GATE_STATUS: [value] issued. HANDOFF_TO:
   DEVELOPER`. CONSTRAINT: Developer MUST open with `"Received GATE_STATUS: [value].
   Proceeding|Blocked."` before Phase 1.
4. CONSTRAINT: Developer MUST close with `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO:
   AUDITOR`. CONSTRAINT: Auditor MUST open with `"Received DEVELOPER_CERTIFICATION:
   COMPLETE. Beginning independent audit."` before Phase 6.
5. CONSTRAINT: Auditor MUST close Phase 6-A with `AUDITOR_CERTIFICATION: COMPLETE.
   HANDOFF_TO: REPORT PRODUCER`. CONSTRAINT: Report Producer MUST open with `"Received
   AUDITOR_CERTIFICATION: COMPLETE."` before Phase 7.

Violation of any CONSTRAINT above is a LIFECYCLE_CONSTRAINT_VIOLATION finding. Both the
outgoing token and the incoming acknowledgment are REQUIRED; neither alone satisfies the
constraint.

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10,
0-A-11) MUST use FIELD|VALUE table rows. Prose descriptions are PROHIBITED. Prose in a
FIELD|VALUE-annotated declaration is STATUS: WRONG_SCHEMA in Phase 0-CA-1 and blocks
Phase 1.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. CONSTRAINT: Topology Architect is PROHIBITED from authoring Phase 0-D-0
until this manifest exists. [Same manifest structure as V-01.]

Close per lifecycle protocol constraint 1.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per lifecycle protocol constraint 1. [Phase 0-D-0 through Phase 0-A-11 — identical
structure and instructions to V-01.] Close per lifecycle protocol constraint 2.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per lifecycle protocol constraint 2. Update manifest with COMPLETE|MISSING|
WRONG_SCHEMA statuses. WRONG_SCHEMA is a CONSTRAINT VIOLATION: presence of a declaration
in prose format when FIELD|VALUE is REQUIRED. Emit Phase 0-CA-1 output with mandatory
row-count parentheticals per DECLARATION_SCHEMA_COMPLETE verdict. [Identical to V-01.]

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE
FAIL, any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.
A GATE_STATUS: PASS assertion without all parentheticals present is a CONSTRAINT
VIOLATION — the parenthetical contract is a REQUIRED structural element, not optional
documentation.

Close per lifecycle protocol constraint 3.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per lifecycle protocol constraint 3. GATE_STATUS: FAIL is PROHIBITED from being
ignored; any Phase 1 content following a received FAIL is an unauthorized execution
finding. [Phases 1-S through 5-F — identical to V-01.] Close per lifecycle protocol
constraint 4.

---

### ROLE 4 — AUDITOR: Phase 6

Open per lifecycle protocol constraint 4. The Auditor MUST NOT modify Developer rows.
All discrepancies are audit findings. Failure to record a discrepancy as a finding is
itself an audit finding.

**Phase 6-A — Gate and Protocol Verification**

Run WRONG_SCHEMA_RESIDUAL_CHECK first. [Identical table structure to V-01.]

Run PARENTHETICAL_PRESENCE_VERIFICATION second. [Identical table structure to V-01.]

Then emit gate assertion. The PARENTHETICAL_VERIFICATION field is the second gate
assertion and MUST carry an explicit declaration citation with confirmed row counts.
CONSTRAINT: A gate field that asserts CONFIRMED without naming the verified declarations
and their row counts does not satisfy C-74. The declaration citation makes the gate
traceable to the Phase 0-CA-1 output without cross-referencing the standalone
PARENTHETICAL_PRESENCE_VERIFICATION table.

```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED
  PARENTHETICAL_VERIFICATION: PASS; declarations verified:
    DEVIATION_BUDGET: [N] rows CONFIRMED,
    CONV_CHAIN_BUDGET: [N] rows CONFIRMED,
    TURN_PREDICTION_CONTRACT: [N] rows CONFIRMED,
    STATUS_QUO_METHOD: [N] rows CONFIRMED
    before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category
  — PASS|FAIL
```

CONSTRAINT: PARENTHETICAL_VERIFICATION: FAIL forces CONTRACT_AUDIT_GATE_HONORED: FAIL.
A gate asserting PASS while the parenthetical field reads NOT_CONFIRMED is a
contradictory gate assertion — a structural finding independent of simulation quality.

Close Phase 6-A per lifecycle protocol constraint 5.

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per lifecycle protocol constraint 5. [Identical PLAN_ITEM structure and PLAN_SUMMARY
close to V-01.]

---

## V-04 — Axes V+W: Pointer Audit + Sweep Scope Citation

**Variation axis:** Lifecycle emphasis + Output format combined — Phase 6-A carries both
the LIFECYCLE_POINTER_AUDIT (Axis V) and the sweep scope citation in the gate field (Axis
W). The LIFECYCLE_PROTOCOL section with SOLE_AUTHORITY is present as the C-70 prerequisite
for C-73. Role instructions use pointer-only references. The gate sweep field names every
FIELD|VALUE-annotated declaration in scope. The parenthetical gate field uses the simple
CONFIRMED toggle (C-71 present, C-74 not introduced). Targets C-73 + C-72 simultaneously.

**Hypothesis:** V-01 established that the LIFECYCLE_POINTER_AUDIT in Phase 6-A closes the
reference-resolution gap that C-70 alone left open. V-02 established that the sweep scope
citation in the gate field closes the gate-traceability gap that C-69 alone left open.
Each axis independently addressed one gap; V-04 tests whether combining both mechanics in
a single variation produces any interference. The two axes operate on different Phase 6-A
blocks — the LIFECYCLE_POINTER_AUDIT runs as the third block, before the gate; the scope
citation lives inside the gate's first field. They do not share state. Combination should
be additive: C-73 PASS + C-72 PASS with no structural collision. C-74 is left unaddressed
to isolate the combined V+W effect.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this
section. Role instructions reference transitions by section name and transition number
only. A HANDOFF_TO or Received string appearing in any role instruction block is a
lifecycle single-source violation.

```
Transition 1 — Phase -1 issuer → Topology Architect
  Outgoing:  HANDOFF_TO: TOPOLOGY ARCHITECT
  Incoming:  "Received PRE_FLIGHT_MANIFEST."

Transition 2 — Topology Architect → Contract Auditor
  Outgoing:  HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1
  Incoming:  "Received Phase 0 from Topology Architect."

Transition 3 — Contract Auditor → Developer
  Outgoing:  GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER
  Incoming:  "Received GATE_STATUS: [value]. Proceeding|Blocked."

Transition 4 — Developer → Auditor
  Outgoing:  DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR
  Incoming:  "Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."

Transition 5 — Auditor → Report Producer
  Outgoing:  AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER
  Incoming:  "Received AUDITOR_CERTIFICATION: COMPLETE."
```

A role that begins authoring without the incoming acknowledgment declared in this section
is a lifecycle gap finding, regardless of whether the outgoing token was present.

---

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10,
0-A-11) use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema
contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1 outgoing. [Same manifest structure as
V-01.] Close per LIFECYCLE_PROTOCOL Transition 1 outgoing.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per LIFECYCLE_PROTOCOL Transition 1 incoming. [Phase 0-D-0 through Phase 0-A-11 —
identical structure and instructions to V-01.] Close per LIFECYCLE_PROTOCOL Transition 2
outgoing.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per LIFECYCLE_PROTOCOL Transition 2 incoming. Update manifest with COMPLETE|MISSING|
WRONG_SCHEMA statuses. Emit Phase 0-CA-1 output with mandatory row-count parentheticals.
[Identical to V-01.] Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 3 incoming. GATE_STATUS: FAIL blocks Phase 1.
[Phases 1-S through 5-F — identical to V-01.] Close per LIFECYCLE_PROTOCOL Transition 4
outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Run WRONG_SCHEMA_RESIDUAL_CHECK first. [Identical table structure to V-01.]

Run PARENTHETICAL_PRESENCE_VERIFICATION second. [Identical table structure to V-01.]

Run LIFECYCLE_POINTER_AUDIT third:
```
LIFECYCLE_POINTER_AUDIT:

Enumerate every pointer reference of the form "per LIFECYCLE_PROTOCOL Transition N"
or "LIFECYCLE_PROTOCOL Transition N incoming/outgoing" across all role instruction
blocks in this prompt (ROLE 1 Phase -1, ROLE 2 Phase 0, ROLE 1 Phase 0-CA-1,
ROLE 3 Phases 1-5, ROLE 4 Phase 6, ROLE 5 Phase 7).

For each pointer reference found:

  ROLE              | POINTER_TEXT                                  | TARGET_TRANSITION | RESOLVED: YES|NO | FINDING
  ------------------|-----------------------------------------------|-------------------|------------------|--------
  [role name/phase] | [exact pointer text from role instructions]   | Transition N      | YES|NO           |

  Rules:
    - RESOLVED: YES if Transition N appears as a labeled entry in LIFECYCLE_PROTOCOL
    - RESOLVED: NO → FINDING: PHASE_6A_FINDING: DANGLING_LIFECYCLE_POINTER[ROLE, Transition N]

LIFECYCLE_POINTER_AUDIT_STATUS: CLEAN (all [N] pointers resolved) |
                                 FINDINGS_PRESENT[list of DANGLING_LIFECYCLE_POINTER findings]
```

Then emit gate assertion. The WRONG_SCHEMA_RESIDUAL_SWEEP field carries an explicit
scope citation (Axis W). The parenthetical field uses the simple CONFIRMED toggle.

```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows; sweep scope:
    Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9],
    Turn Prediction Contract [0-A-10], Status Quo Method [0-A-11])
    before Phase 1: CONFIRMED|NOT_CONFIRMED
  PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category
  — PASS|FAIL
```

Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per LIFECYCLE_PROTOCOL Transition 5 incoming. [Identical to V-01.]

---

## V-05 — Axes V+W+X: Full R18 Combination

**Variation axis:** Role sequence + Lifecycle emphasis + Output format + Phrasing register
combined — all three new axes are active simultaneously. The LIFECYCLE_PROTOCOL section
with SOLE_AUTHORITY is present (C-70). Role instructions use pointer-only references.
Phase 6-A carries the LIFECYCLE_POINTER_AUDIT (Axis V, C-73 target). The gate sweep field
names every FIELD|VALUE-annotated declaration in its scope citation (Axis W, C-72 target).
The gate parenthetical field names each verified declaration with its confirmed row count
(Axis X, C-74 target). All three new criteria can be satisfied simultaneously in a single
trace.

**Hypothesis:** V-01 through V-04 each isolate one or two of the new axes to confirm each
criterion is independently achievable and to check that they do not interfere. V-05 tests
the full R18 combination: LIFECYCLE_POINTER_AUDIT (Phase 6-A third block) + sweep scope
citation (gate first field) + parenthetical declaration citation (gate second field). Each
axis operates on a structurally distinct location — the audit table, the first gate field,
the second gate field — with no shared state, so combination should be strictly additive.
The expected result is C-73 PASS + C-72 PASS + C-74 PASS in a single trace, without any
criterion undermining another. This is the R18 full-combination benchmark variation.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this
section. Role instructions reference transitions by section name and transition number
only. A HANDOFF_TO or Received string appearing in any role instruction block is a
lifecycle single-source violation.

```
Transition 1 — Phase -1 issuer → Topology Architect
  Outgoing:  HANDOFF_TO: TOPOLOGY ARCHITECT
  Incoming:  "Received PRE_FLIGHT_MANIFEST."

Transition 2 — Topology Architect → Contract Auditor
  Outgoing:  HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1
  Incoming:  "Received Phase 0 from Topology Architect."

Transition 3 — Contract Auditor → Developer
  Outgoing:  GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER
  Incoming:  "Received GATE_STATUS: [value]. Proceeding|Blocked."

Transition 4 — Developer → Auditor
  Outgoing:  DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR
  Incoming:  "Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."

Transition 5 — Auditor → Report Producer
  Outgoing:  AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER
  Incoming:  "Received AUDITOR_CERTIFICATION: COMPLETE."
```

A role that begins authoring without the incoming acknowledgment declared in this section
is a lifecycle gap finding, regardless of whether the outgoing token was present.

---

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10,
0-A-11) use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema
contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1 outgoing. [Same manifest structure as
V-01.] Close per LIFECYCLE_PROTOCOL Transition 1 outgoing.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per LIFECYCLE_PROTOCOL Transition 1 incoming. [Phase 0-D-0 through Phase 0-A-11 —
identical structure and instructions to V-01.] Close per LIFECYCLE_PROTOCOL Transition 2
outgoing.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per LIFECYCLE_PROTOCOL Transition 2 incoming. Update manifest with COMPLETE|MISSING|
WRONG_SCHEMA statuses. Emit Phase 0-CA-1 output with mandatory row-count parentheticals.
[Identical to V-01.] Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 3 incoming. GATE_STATUS: FAIL blocks Phase 1.
[Phases 1-S through 5-F — identical to V-01.] Close per LIFECYCLE_PROTOCOL Transition 4
outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Run WRONG_SCHEMA_RESIDUAL_CHECK first:
```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO → FINDING: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows in Phase 0-CA-1) |
                              CLEAN (all WRONG_SCHEMA rows resolved) |
                              FINDINGS_PRESENT[list of unresolved declarations]
```

Run PARENTHETICAL_PRESENCE_VERIFICATION second:
```
PARENTHETICAL_PRESENCE_VERIFICATION:

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |

  PARENTHETICAL_PRESENT: YES iff CA output shows "(count N rows: [breakdown])" inline
  with the verdict. NO → FINDING: PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL[DECLARATION]

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical: list]
```

Run LIFECYCLE_POINTER_AUDIT third:
```
LIFECYCLE_POINTER_AUDIT:

Enumerate every pointer reference of the form "per LIFECYCLE_PROTOCOL Transition N"
or "LIFECYCLE_PROTOCOL Transition N incoming/outgoing" across all role instruction
blocks in this prompt (ROLE 1 Phase -1, ROLE 2 Phase 0, ROLE 1 Phase 0-CA-1,
ROLE 3 Phases 1-5, ROLE 4 Phase 6, ROLE 5 Phase 7).

For each pointer reference found:

  ROLE              | POINTER_TEXT                                  | TARGET_TRANSITION | RESOLVED: YES|NO | FINDING
  ------------------|-----------------------------------------------|-------------------|------------------|--------
  [role name/phase] | [exact pointer text from role instructions]   | Transition N      | YES|NO           |

  Rules:
    - RESOLVED: YES if Transition N appears as a labeled entry in LIFECYCLE_PROTOCOL
    - RESOLVED: NO → FINDING: PHASE_6A_FINDING: DANGLING_LIFECYCLE_POINTER[ROLE, Transition N]
    - A pointer citing a transition number outside the declared range is DANGLING regardless
      of intent

LIFECYCLE_POINTER_AUDIT_STATUS: CLEAN (all [N] pointers resolved) |
                                 FINDINGS_PRESENT[list of DANGLING_LIFECYCLE_POINTER findings]
```

Then emit gate assertion. The sweep field carries scope citation (Axis W). The
parenthetical field carries declaration citation with confirmed row counts (Axis X).
Both citations make the gate self-describing: a verifier can confirm full coverage without
navigating to Phase 0-CA-1 or to the standalone Phase 6-A tables.

```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows; sweep scope:
    Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9],
    Turn Prediction Contract [0-A-10], Status Quo Method [0-A-11])
    before Phase 1: CONFIRMED|NOT_CONFIRMED
  PARENTHETICAL_VERIFICATION: PASS; declarations verified:
    DEVIATION_BUDGET: [N] rows CONFIRMED,
    CONV_CHAIN_BUDGET: [N] rows CONFIRMED,
    TURN_PREDICTION_CONTRACT: [N] rows CONFIRMED,
    STATUS_QUO_METHOD: [N] rows CONFIRMED
    before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category
  — PASS|FAIL
```

The sweep scope citation and parenthetical declaration citation operate independently:
a NOT_CONFIRMED on the sweep field does not affect the parenthetical field, and vice
versa. Both fields must read CONFIRMED for CONTRACT_AUDIT_GATE_HONORED: PASS.

Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per LIFECYCLE_PROTOCOL Transition 5 incoming. [Identical to V-01.]
