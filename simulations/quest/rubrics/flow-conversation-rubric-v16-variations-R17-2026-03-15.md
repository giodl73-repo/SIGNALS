# Quest Variations — flow-conversation — Round 17 (v16 rubric)

**Date:** 2026-03-15 | **Rubric version:** v16 | **Max score:** 240

---

## Variation Axes Selected

All 5 variations carry the full v16 baseline: C-01 through C-68, plus the three new
criteria C-69 through C-71 each variation is explicitly designed to surface.
The baseline includes: all v15 criteria, LIFECYCLE_PROTOCOL dedicated section (C-66),
WRONG_SCHEMA_RESIDUAL_CHECK in Phase 6-A (C-67), PARENTHETICAL_PRESENCE_VERIFICATION in
Phase 6-A (C-68), plus all prior structural elements through C-65.

**New axes for R17 (targeting C-69, C-70, C-71):**

- **Axis S — Lifecycle single-source (C-70 target)**: Extract every HANDOFF_TO token
  and Received acknowledgment string OUT of role instruction prose and deposit them
  exclusively in the LIFECYCLE_PROTOCOL section. Role instructions reference transitions
  by section name and transition number only. The LIFECYCLE_PROTOCOL section opens with
  a SOLE_AUTHORITY declaration that explicitly forbids re-declaration elsewhere. A
  HANDOFF_TO token appearing in any role instruction block is a structural violation —
  the single source of truth is the protocol section, not the role instruction.
  C-70 requires: (a) LIFECYCLE_PROTOCOL named section with SOLE_AUTHORITY declaration
  present, (b) no HANDOFF_TO or Received string in any role instruction block, (c) role
  instructions reference transitions as "per LIFECYCLE_PROTOCOL Transition N."

- **Axis T — Gate sweep precondition (C-69 target)**: The WRONG_SCHEMA_RESIDUAL_CHECK
  standalone table in Phase 6-A generates WRONG_SCHEMA_RESIDUAL_SWEEP status. That
  status is then consumed as a structural FIRST FIELD in CONTRACT_AUDIT_GATE_HONORED —
  not a parallel block the gate can ignore. The gate reads: `WRONG_SCHEMA_RESIDUAL_SWEEP:
  CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED` as its first assertion, before
  PRE_FLIGHT_MANIFEST_STATUS. A gate that asserts HONORED without first confirming the
  sweep is an incomplete gate assertion — the enforcement chain runs from Phase 0-CA-1
  detection through Phase 6-A sweep through gate assertion.
  C-69 requires C-67 PASS. Scoring: sweep result is a named field WITHIN
  CONTRACT_AUDIT_GATE_HONORED AND appears as the first field in the gate block.

- **Axis U — Gate parenthetical precondition (C-71 target)**: The
  PARENTHETICAL_PRESENCE_VERIFICATION standalone table generates PARENTHETICAL_VERIFICATION
  status. That status is then consumed as a structural field in CONTRACT_AUDIT_GATE_HONORED,
  parallel to the sweep field (Axis T). The gate reads: `PARENTHETICAL_VERIFICATION: PASS
  before Phase 1: CONFIRMED|NOT_CONFIRMED` as its second assertion, before
  PRE_FLIGHT_MANIFEST_STATUS. A gate without this field has not verified C-65 compliance
  as a gate precondition — verification coverage from C-68 propagates into gate integrity.
  C-71 requires C-68 PASS. Scoring: parenthetical status is a named field WITHIN
  CONTRACT_AUDIT_GATE_HONORED AND appears sequentially after the sweep field (Axis T order).

**Single-axis (3):** S, T, U

- **Axis S — Lifecycle single-source**: SOLE_AUTHORITY declaration in section; no
  HANDOFF_TO or Received strings in role instruction prose; pointer-only references
- **Axis T — Gate sweep precondition**: WRONG_SCHEMA_RESIDUAL_SWEEP as first gate field;
  sweep result is consumed by the gate, not ignored by it
- **Axis U — Gate parenthetical precondition**: PARENTHETICAL_VERIFICATION as second gate
  field; parenthetical result propagates into gate assertion

**Combined (2):**

- **Axes S+T — Single-source lifecycle + sweep gate precondition**: SOLE_AUTHORITY section
  + pointer-only roles + sweep as gate first field; targets C-70 + C-69
- **Axes S+T+U — Full R17 combination**: all three axes; C-70 + C-69 + C-71 simultaneously

---

## V-01 — Axis S: Lifecycle Single-Source

**Variation axis:** Lifecycle emphasis — the LIFECYCLE_PROTOCOL section is upgraded with a
SOLE_AUTHORITY declaration that explicitly forbids HANDOFF_TO token and Received
acknowledgment strings from appearing anywhere outside this section. Every role instruction
drops its inline token values and references the protocol section by name and transition
number only: "per LIFECYCLE_PROTOCOL Transition N." The section is the single verifiable
source of the full transition contract.

**Hypothesis:** R16 V-01, V-04, V-05 achieved C-66 by extracting the lifecycle protocol
into a dedicated named section with "Silent fallthrough is a structural violation" at the
top and all 5 transitions as labeled pairs. However, those variations ALSO included the
actual HANDOFF_TO and Received strings inline in role instruction blocks (e.g., "Close with
LIFECYCLE_PROTOCOL Transition 1 token: **HANDOFF_TO: TOPOLOGY ARCHITECT**"). C-70 identifies
this as a single-source violation: two locations now carry authoritative transition tokens —
the dedicated section AND the role instruction prose. Removing the inline token values and
replacing them with section-pointer references (e.g., "Close per LIFECYCLE_PROTOCOL
Transition 1 outgoing.") enforces single-source-of-truth. A reader — or a verifier — can
locate the full contract in exactly one place. C-69 and C-71 are unaddressed by this axis;
Phase 6-A uses the standalone-block structure from V-04 R16 for C-67 and C-68.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this section.
Role instructions reference transitions by section name and transition number only. A
HANDOFF_TO or Received string appearing in any role instruction block is a lifecycle
single-source violation.

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

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1. The Topology Architect may not begin
Phase 0-D-0 until this manifest exists.

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

Open per LIFECYCLE_PROTOCOL Transition 2 incoming.

**Phase 0-D-0 — Column Schema Registry (first artifact)**

| COLUMN_NAME         | FORMAT                                    | ALLOWED_VALUES                                                        | REQUIRED_WHEN       |
|---------------------|-------------------------------------------|-----------------------------------------------------------------------|---------------------|
| TURN_ID             | T-NN                                      | T-01, T-02, ...                                                       | Every turn          |
| USER_UTTERANCE      | free text                                 | any                                                                   | Every turn          |
| TOPIC_MATCHED       | TOPIC_ID                                  | declared topics, CONTRACT_GAP                                         | Every turn          |
| NODES_EXECUTED      | comma-separated                           | any                                                                   | Every turn          |
| AGENT_RESPONSE      | free text                                 | any                                                                   | Every turn          |
| TRANSITION_TARGET   | TOPIC_ID or terminal                      | declared topics, TERMINAL, FALLBACK                                   | Every turn          |
| SESSION_STATE       | replayed from Phase 1-S                   | variable=value pairs                                                  | Every turn          |
| CONFORMANCE         | verdict                                   | CONFORMS, DEVIATES[CONV-NN]                                           | Every turn          |
| CONSTRAINT_VERDICTS | CONV-NN evaluation list                   | PASS, FAIL, CHAIN_SUSPENDED[chain head: CONV-NN broke at TURN_ID]     | Every turn          |
| CHAIN_EFFECTS       | propagation effects                       | CONV-NN → [CONV-NN: ACTIVATED\|SUSPENDED, ...]                        | Every turn          |
| PREDICTION_MATCH    | path match                                | ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual], OFF_ALL_PATHS | Every turn          |
| SLOT_FILL_STATUS    | slot=RESULT                               | FILLED, SKIPPED, INTERRUPTED                                          | Slot-fill turns     |

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
-------------|----------------------------------------
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
HP-01 required; up to 3 ALT-NN:
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

Open per LIFECYCLE_PROTOCOL Transition 3 incoming.

Update manifest. STATUS values: COMPLETE (present and correct format) | MISSING (absent
entirely) | WRONG_SCHEMA (present but uses prose or non-required table format). WRONG_SCHEMA
applies only to rows annotated SCHEMA_TYPE: FIELD|VALUE. Then compute all blocking checks.

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

WRONG_SCHEMA counts as non-COMPLETE. A WRONG_SCHEMA row blocks Phase 1 alongside MISSING rows.

Then emit Phase 0-CA-1 output. Row-count parentheticals are mandatory for each
DECLARATION_SCHEMA_COMPLETE verdict:

```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list — VARS_IN_TOPOLOGY not in VARS_IN_CONTRACT]
  CHAIN_BUDGET_DELTA: [empty or list — CHAINS_IN_TOPOLOGY not in CHAINS_IN_BUDGET]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET:         PASS|FAIL (count N rows: [named breakdown, e.g. "5 rows: P0/P1/P2/P3 + RATIONALE"])
    CONV_CHAIN_BUDGET:        PASS|FAIL (count N rows: [5 fields per chain × M chains])
    TURN_PREDICTION_CONTRACT: PASS|FAIL (count N rows: [4 rows per path × M paths + 1 signed row])
    STATUS_QUO_METHOD:        PASS|FAIL (count N rows: [9 rows: 3 metadata + 5 BLIND + SIGNED])
  PREDICTION_CONTRACT_SIGNED:    YES|NO
  STATUS_QUO_METHOD_SIGNED:      YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
GATE_STATUS: FAIL blocks Phase 1. Any Phase 1 content following a received FAIL is an
unauthorized execution finding.

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

Open per LIFECYCLE_PROTOCOL Transition 5 incoming.

The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if the declaration was corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO if the declaration remained in wrong format; this is an unresolved residual
    - FINDING when RESOLVED: NO: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows in Phase 0-CA-1) |
                              CLEAN (all WRONG_SCHEMA rows resolved) |
                              FINDINGS_PRESENT[list of unresolved declarations]
```

```
PARENTHETICAL_PRESENCE_VERIFICATION:

For each DECLARATION_SCHEMA_COMPLETE entry in Phase 0-CA-1:

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES; — if NO] | [see rule]
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |

  PARENTHETICAL_PRESENT: YES iff CA output shows "(count N rows: [breakdown])" inline
  with the PASS|FAIL verdict for that declaration.
  PARENTHETICAL_PRESENT: NO → FINDING: PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL
  [DECLARATION] — structural defect, not a quality observation.

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical: list]
```

```
CONTRACT_AUDIT_GATE_HONORED:
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

Open per LIFECYCLE_PROTOCOL Transition 5 incoming from Auditor.

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

## V-02 — Axis T: Gate Sweep Precondition

**Variation axis:** Output format — the WRONG_SCHEMA_RESIDUAL_CHECK standalone table runs
first in Phase 6-A (satisfying C-67). Its WRONG_SCHEMA_RESIDUAL_SWEEP result is then
consumed as the FIRST FIELD in CONTRACT_AUDIT_GATE_HONORED — not a parallel block the gate
can ignore. The gate cannot assert HONORED without a CONFIRMED sweep field. The lifecycle
protocol remains inline within role instructions (no dedicated LIFECYCLE_PROTOCOL section,
so C-70 is unaddressed).

**Hypothesis:** R16 V-02 and V-04 achieved C-67 by placing WRONG_SCHEMA_RESIDUAL_CHECK as
a standalone block before the gate assertion. However, the gate block itself did not
reference the sweep result — a gate-honored assertion could be issued without consuming the
sweep outcome. C-69 requires the gate to carry the sweep result as a named field. The
distinguishing structural move is: the gate OPENS with
`WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED` as its first
assertion, making sweep confirmation a precondition of gate passage. A gate that asserts
CONTRACT_AUDIT_GATE_HONORED: PASS while that field reads NOT_CONFIRMED is a contradictory
assertion — the sweep result is structurally embedded, not adjacent. C-70 and C-71 are
unaddressed in this variation.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is an explicit bidirectional protocol event.
Silent fallthrough between roles is a structural violation. Each role issues an outgoing
handoff token and its successor opens with a matching acknowledgment.

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

Execute FIRST. The Topology Architect may not begin Phase 0-D-0 until this manifest exists.

[Same manifest as V-01 — with SCHEMA_TYPE column, PENDING statuses.]

Close with: **HANDOFF_TO: TOPOLOGY ARCHITECT**

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST."**

[Phase 0-D-0 through Phase 0-A-11 — same as V-01.]

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect."**

Update manifest. WRONG_SCHEMA applies to FIELD|VALUE-annotated rows where declaration exists
but uses prose or non-FIELD|VALUE format. Both WRONG_SCHEMA and MISSING block Phase 1.

[Resolved manifest as V-01 — COMPLETE|MISSING|WRONG_SCHEMA statuses.]

Emit Phase 0-CA-1 output with mandatory row-count parentheticals per DECLARATION_SCHEMA_COMPLETE verdict.

[Phase 0-CA-1 block as V-01 — all fields including parentheticals.]

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
GATE_STATUS: FAIL blocks Phase 1.

[All phases 1-S through 5-F — same as V-01.]

Close with: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

The Auditor opens Phase 6-A with the WRONG_SCHEMA residual sweep. The sweep result is
then the first field consumed by the gate assertion. A gate asserting HONORED without a
CONFIRMED sweep field is a structurally incomplete assertion.

```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if declaration corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO if declaration remained in wrong format — unresolved residual
    - FINDING when RESOLVED: NO: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows) |
                              CLEAN (all resolved) |
                              FINDINGS_PRESENT[unresolved declarations]
```

Then emit the parenthetical verification table:

[PARENTHETICAL_PRESENCE_VERIFICATION table as V-01 — with FINDING for absent parentheticals.]

Then emit gate verification with WRONG_SCHEMA_RESIDUAL_SWEEP as the first embedded field:

```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

The WRONG_SCHEMA_RESIDUAL_SWEEP field is a gate precondition: its status is CONFIRMED by
cross-referencing the WRONG_SCHEMA_RESIDUAL_CHECK table above. A sweep result of
FINDINGS_PRESENT forces NOT_CONFIRMED on this field and FAIL on CONTRACT_AUDIT_GATE_HONORED.

Close Phase 6-A: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

**Phase 6-B through 6-H:** [Same as V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

[Same as V-01 — PLAN_ITEM per defect, PLAN_SUMMARY close.]

---

## V-03 — Axis U: Gate Parenthetical Precondition

**Variation axis:** Phrasing register — formal imperative constraint language is used
throughout to frame the PARENTHETICAL_PRESENCE_VERIFICATION result as a gate precondition.
The PARENTHETICAL_VERIFICATION status appears as a named field in CONTRACT_AUDIT_GATE_HONORED
immediately after WRONG_SCHEMA_RESIDUAL_SWEEP. The vocabulary shifts to CONSTRAINT/VIOLATION/
PROHIBITED to signal structural obligations. The lifecycle protocol remains inline within
role instructions (no dedicated LIFECYCLE_PROTOCOL section, C-70 unaddressed). No
WRONG_SCHEMA_RESIDUAL_SWEEP in gate (C-69 unaddressed); WRONG_SCHEMA_RESIDUAL_CHECK runs as
standalone block only.

**Hypothesis:** R16 V-03 achieved C-68 by placing PARENTHETICAL_PRESENCE_VERIFICATION as
a standalone Phase 6-A table. However, the gate assertion did not carry the parenthetical
result as a field — a gate-honored assertion could be issued without confirming parenthetical
compliance. C-71 requires the gate to carry `PARENTHETICAL_VERIFICATION: PASS before Phase 1:
CONFIRMED|NOT_CONFIRMED` as a named field. This variation uses imperative constraint language
("CONSTRAINT VIOLATION", "MUST", "PROHIBITED") to make the obligation explicit: a gate that
asserts HONORED while PARENTHETICAL_VERIFICATION reads NOT_CONFIRMED is a structural defect.
Axis U is isolated here — C-70 (no inline redeclarations) and C-69 (sweep as gate first
field) are not addressed.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is a declared structural constraint. Crossing a
role boundary WITHOUT emitting the outgoing handoff token AND without the successor opening
with the matching acknowledgment is a LIFECYCLE_CONSTRAINT_VIOLATION. Silent fallthrough is
PROHIBITED.

**Lifecycle protocol constraints:**
1. CONSTRAINT: Phase -1 MUST close with `HANDOFF_TO: TOPOLOGY ARCHITECT`.
   CONSTRAINT: Topology Architect MUST open with `"Received PRE_FLIGHT_MANIFEST."` before authoring Phase 0-D-0.
2. CONSTRAINT: Phase 0 MUST close with `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`.
   CONSTRAINT: Contract Auditor MUST open with `"Received Phase 0 from Topology Architect."` before Phase 0-CA-1.
3. CONSTRAINT: Phase 0-CA-1 MUST close with `GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER`.
   CONSTRAINT: Developer MUST open with `"Received GATE_STATUS: [value]. Proceeding|Blocked."` before Phase 1.
4. CONSTRAINT: Developer MUST close with `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR`.
   CONSTRAINT: Auditor MUST open with `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` before Phase 6.
5. CONSTRAINT: Auditor MUST close Phase 6-A with `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`.
   CONSTRAINT: Report Producer MUST open with `"Received AUDITOR_CERTIFICATION: COMPLETE."` before Phase 7.

Violation of any CONSTRAINT above generates a LIFECYCLE_CONSTRAINT_VIOLATION finding,
regardless of whether partial tokens were present. Both the outgoing and incoming tokens
are REQUIRED; neither alone satisfies the constraint.

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10,
0-A-11) MUST use FIELD|VALUE table rows. Prose descriptions are PROHIBITED. Prose in a
FIELD|VALUE-annotated declaration is STATUS: WRONG_SCHEMA in Phase 0-CA-1 and blocks Phase 1.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. Constraint: Topology Architect MUST NOT author Phase 0-D-0 before this
manifest exists. Non-existence of this manifest is a CONTRACT_SETUP_VIOLATION.

[Same manifest as V-01 — with SCHEMA_TYPE column, PENDING statuses, HANDOFF_TO close.]

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open: **"Received PRE_FLIGHT_MANIFEST."** (REQUIRED — absence is LIFECYCLE_CONSTRAINT_VIOLATION)

[Phase 0-D-0 through Phase 0-A-11 — same as V-01.]

Close: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**
(REQUIRED — absence is LIFECYCLE_CONSTRAINT_VIOLATION)

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open: **"Received Phase 0 from Topology Architect."** (REQUIRED)

[Resolved manifest and Phase 0-CA-1 output block — same as V-01, including WRONG_SCHEMA
statuses and mandatory row-count parentheticals.]

Close: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."** (REQUIRED)

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open: **"Received GATE_STATUS: [value]. Proceeding|Blocked."** (REQUIRED)
CONSTRAINT: GATE_STATUS: FAIL PROHIBITS Phase 1 authoring. Phase 1 content following a
received FAIL is an UNAUTHORIZED_EXECUTION_VIOLATION.

[All phases 1-S through 5-F — same as V-01.]

Close: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."** (REQUIRED)

---

### ROLE 4 — AUDITOR: Phase 6

Open: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."** (REQUIRED)

CONSTRAINT: The Auditor MUST NOT modify Developer rows. All discrepancies MUST be expressed
as audit findings.

**Phase 6-A — Gate and Protocol Verification**

The Auditor MUST complete the WRONG_SCHEMA residual check and the PARENTHETICAL_PRESENCE
verification BEFORE asserting CONTRACT_AUDIT_GATE_HONORED. Both verification results are
REQUIRED fields in the gate assertion; their absence makes the gate assertion structurally
INCOMPLETE.

```
WRONG_SCHEMA_RESIDUAL_CHECK:

CONSTRAINT: Every manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1 MUST be
enumerated below. Omission of a WRONG_SCHEMA row from this table is an AUDIT_COVERAGE_VIOLATION.

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  CONSTRAINT: RESOLVED: NO → FINDING: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]
  — this finding is MANDATORY; the Auditor MUST NOT omit it.

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows) |
                              CLEAN (all resolved) |
                              FINDINGS_PRESENT[unresolved declarations]
```

```
PARENTHETICAL_PRESENCE_VERIFICATION:

CONSTRAINT: Every DECLARATION_SCHEMA_COMPLETE entry in Phase 0-CA-1 MUST be checked for
parenthetical presence. Omission of a declaration row from this table is an
AUDIT_COVERAGE_VIOLATION.

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES; — if NO] | [see rule]
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |

  CONSTRAINT: PARENTHETICAL_PRESENT: NO → FINDING: PHASE_6A_FINDING:
  MISSING_ROW_COUNT_PARENTHETICAL[DECLARATION] — MANDATORY structural defect finding.
  A CA verdict of PASS without a parenthetical does NOT satisfy C-65; the Auditor MUST
  flag the omission regardless of declaration content correctness.

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical: list]
```

Gate assertion with PARENTHETICAL_VERIFICATION as a structural required field:

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
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

CONSTRAINT: CONTRACT_AUDIT_GATE_HONORED without both WRONG_SCHEMA_RESIDUAL_SWEEP and
PARENTHETICAL_VERIFICATION fields present and CONFIRMED is an INCOMPLETE_GATE_ASSERTION
— the gate is structurally defective regardless of the PASS|FAIL verdict on other fields.

Close Phase 6-A: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

**Phase 6-B through 6-H:** [Same as V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open: **"Received AUDITOR_CERTIFICATION: COMPLETE."** (REQUIRED)

[Same as V-01 — PLAN_ITEM per defect, PLAN_SUMMARY close.]

---

## V-04 — Axes S+T: Lifecycle Single-Source + Gate Sweep Precondition

**Variation axes:** Lifecycle emphasis (Axis S) + Output format (Axis T). The LIFECYCLE_PROTOCOL
section carries a SOLE_AUTHORITY declaration forbidding inline token re-declaration (targeting
C-70). Role instructions reference transitions by section name and number only. Phase 6-A
opens with the WRONG_SCHEMA_RESIDUAL_CHECK standalone table; its result is consumed as the
FIRST FIELD in CONTRACT_AUDIT_GATE_HONORED (targeting C-69). PARENTHETICAL_VERIFICATION
is a standalone Phase 6-A table only — it is NOT embedded in the gate assertion (C-71
unaddressed in this combination).

**Hypothesis:** Axes S and T are mechanically independent — the single-source lifecycle
rule operates on the prompt structure prior to Phase 1, and the sweep-as-gate-precondition
rule operates on Phase 6-A structure. Their combination should satisfy C-70 and C-69
simultaneously. Axis U (C-71) would require additionally embedding PARENTHETICAL_VERIFICATION
as a gate field; without it, the parenthetical check remains a standalone Phase 6-A table
that the gate does not reference. V-05 adds Axis U.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this section.
Role instructions reference transitions by section name and transition number only. A
HANDOFF_TO or Received string appearing in any role instruction block is a lifecycle
single-source violation — the contract exists in exactly one location.

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

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1. The Topology Architect may not begin
Phase 0-D-0 until this manifest exists.

[Same manifest as V-01 — with SCHEMA_TYPE column, PENDING statuses.]

Close per LIFECYCLE_PROTOCOL Transition 1 outgoing.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per LIFECYCLE_PROTOCOL Transition 2 incoming.

[Phase 0-D-0 through Phase 0-A-11 — same as V-01.]

Close per LIFECYCLE_PROTOCOL Transition 2 outgoing.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per LIFECYCLE_PROTOCOL Transition 3 incoming.

[Resolved manifest and Phase 0-CA-1 output block — same as V-01, including WRONG_SCHEMA
statuses and mandatory row-count parentheticals.]

Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
GATE_STATUS: FAIL blocks Phase 1.

[All phases 1-S through 5-F — same as V-01.]

Close per LIFECYCLE_PROTOCOL Transition 4 outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

Open per LIFECYCLE_PROTOCOL Transition 5 incoming.

The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Phase 6-A opens with the WRONG_SCHEMA residual sweep. The sweep result is then consumed
as the first field in the gate assertion — not a parallel block the gate can ignore.

```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if declaration corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO if declaration remained in wrong format — unresolved residual
    - FINDING when RESOLVED: NO: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows) |
                              CLEAN (all resolved) |
                              FINDINGS_PRESENT[unresolved declarations]
```

```
PARENTHETICAL_PRESENCE_VERIFICATION:

For each DECLARATION_SCHEMA_COMPLETE entry in Phase 0-CA-1:

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |

  PARENTHETICAL_PRESENT: NO → FINDING: PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL
  [DECLARATION] — structural defect, not a quality gap.

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical: list]
```

Gate verification with WRONG_SCHEMA_RESIDUAL_SWEEP as first embedded precondition field:

```
CONTRACT_AUDIT_GATE_HONORED:
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

The WRONG_SCHEMA_RESIDUAL_SWEEP field is populated by cross-referencing the
WRONG_SCHEMA_RESIDUAL_CHECK table. A sweep result of FINDINGS_PRESENT forces NOT_CONFIRMED
and FAIL on CONTRACT_AUDIT_GATE_HONORED. The PARENTHETICAL_VERIFICATION result does not
appear in the gate assertion — it is a standalone Phase 6-A finding only.

Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B through 6-H:** [Same as V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per LIFECYCLE_PROTOCOL Transition 5 incoming from Auditor.

[Same as V-01 — PLAN_ITEM per defect, PLAN_SUMMARY close.]

---

## V-05 — Axes S+T+U: Full R17 Combination

**Variation axes:** Lifecycle emphasis (Axis S) + Output format (Axis T) + Phrasing register
(Axis U). All three new criteria targeted: C-70 (SOLE_AUTHORITY lifecycle section, no inline
redeclarations), C-69 (WRONG_SCHEMA_RESIDUAL_SWEEP as gate first field), C-71 (PARENTHETICAL_VERIFICATION
as gate second field). The three axes are mutually reinforcing: the LIFECYCLE_PROTOCOL
section is the structural contract for role boundaries; the gate assertion is the structural
contract for Phase 0 compliance; both contracts enforce single-source-of-truth — the section
is the only place to find transition tokens, and the gate is the only place to find combined
Phase 0 compliance status.

**Hypothesis:** V-04 satisfies C-70 and C-69 but not C-71. Adding Axis U embeds
PARENTHETICAL_VERIFICATION as the second gate field, immediately following
WRONG_SCHEMA_RESIDUAL_SWEEP. The two gate precondition fields form a logical pair: the first
checks declaration format compliance (schema type), the second checks declaration completeness
(row count accountability). Together they constitute the full Phase 0-CA-1 output audit
summary inside the gate assertion. A gate without both fields has not verified the complete
Phase 0-CA-1 output contract. V-05 should satisfy all three new criteria simultaneously.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this section.
Role instructions reference transitions by section name and transition number only. A
HANDOFF_TO or Received string appearing in any role instruction block is a lifecycle
single-source violation — the contract exists in exactly one location, and this is it.

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

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1. The Topology Architect may not begin
Phase 0-D-0 until this manifest exists.

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

Open per LIFECYCLE_PROTOCOL Transition 2 incoming.

**Phase 0-D-0 — Column Schema Registry (first artifact)**

| COLUMN_NAME         | FORMAT                                    | ALLOWED_VALUES                                                        | REQUIRED_WHEN       |
|---------------------|-------------------------------------------|-----------------------------------------------------------------------|---------------------|
| TURN_ID             | T-NN                                      | T-01, T-02, ...                                                       | Every turn          |
| USER_UTTERANCE      | free text                                 | any                                                                   | Every turn          |
| TOPIC_MATCHED       | TOPIC_ID                                  | declared topics, CONTRACT_GAP                                         | Every turn          |
| NODES_EXECUTED      | comma-separated                           | any                                                                   | Every turn          |
| AGENT_RESPONSE      | free text                                 | any                                                                   | Every turn          |
| TRANSITION_TARGET   | TOPIC_ID or terminal                      | declared topics, TERMINAL, FALLBACK                                   | Every turn          |
| SESSION_STATE       | replayed from Phase 1-S                   | variable=value pairs                                                  | Every turn          |
| CONFORMANCE         | verdict                                   | CONFORMS, DEVIATES[CONV-NN]                                           | Every turn          |
| CONSTRAINT_VERDICTS | CONV-NN evaluation list                   | PASS, FAIL, CHAIN_SUSPENDED[chain head: CONV-NN broke at TURN_ID]     | Every turn          |
| CHAIN_EFFECTS       | propagation effects                       | CONV-NN → [CONV-NN: ACTIVATED\|SUSPENDED, ...]                        | Every turn          |
| PREDICTION_MATCH    | path match                                | ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual], OFF_ALL_PATHS | Every turn          |
| SLOT_FILL_STATUS    | slot=RESULT                               | FILLED, SKIPPED, INTERRUPTED                                          | Slot-fill turns     |

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
-------------|----------------------------------------
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
HP-01 required; up to 3 ALT-NN:
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

Open per LIFECYCLE_PROTOCOL Transition 3 incoming.

Update manifest. STATUS values: COMPLETE | MISSING | WRONG_SCHEMA (for FIELD|VALUE-annotated
rows where declaration exists but uses prose or non-FIELD|VALUE format). Both MISSING and
WRONG_SCHEMA block Phase 1.

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

Emit Phase 0-CA-1 output. Row-count parentheticals are mandatory for each
DECLARATION_SCHEMA_COMPLETE verdict; a PASS without a parenthetical does not satisfy C-65:

```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET:         PASS|FAIL (count N rows: [e.g. "5 rows: P0/P1/P2/P3 + RATIONALE"])
    CONV_CHAIN_BUDGET:        PASS|FAIL (count N rows: [5 fields per chain × M chains])
    TURN_PREDICTION_CONTRACT: PASS|FAIL (count N rows: [4 rows per path × M paths + 1 signed row])
    STATUS_QUO_METHOD:        PASS|FAIL (count N rows: [9 rows: 3 metadata + 5 BLIND + SIGNED])
  PREDICTION_CONTRACT_SIGNED:    YES|NO
  STATUS_QUO_METHOD_SIGNED:      YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
GATE_STATUS: FAIL blocks Phase 1.

**Phase 1-S — Session Variable Mutation Log (author BEFORE Phase 1)**
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE cells in Phase 1 are derived by replaying Phase 1-S in turn order.

**Phase 1 — Turn-by-Turn Trace**
One row per turn; all columns from Phase 0-D-0. No turns skipped or collapsed.
Inject at least one adversarial utterance; record injection TURN_ID, response, defect,
recovery path.

**Phase 1-T — Topic Aggregate (additive)**
```
TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ |
DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP | PATH_IDS_MATCHED
```

**Phase 2 — Defect Classification**
Nine defect classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP.

Per FOUND defect:
```
DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS: P0|P1|P2|P3 | INVARIANT_CITE |
REPRODUCTION_STEPS | RECOVERY | ENTANGLEMENT_VERDICT |
[PLAN_TIER_OVERRIDE: IMMEDIATE — CRITICAL deviations only]
```

Per FOUND P0 defect, before classifying lower-severity:
```
EXECUTION_HALT:
  HALT_TRIGGER | ROOT_CAUSE | MVF_RECOMMENDATION | MVF_SCOPE | UNBLOCKED_BY
  CHAIN_BREAK_TRACE: BROKEN_CHAIN | CHAIN_HEAD_CONV | FIRST_DEVIATE_TURN |
                     SUSPENDED_CONVS | BREAK_TO_DEFECT_PATH
  CHAIN_REPAIR: [CONV-NN list]
```

**Phase 3-E — Entanglement Map**
```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_CLASS]|MASKED_BY[DEFECT_CLASS]
```

**Phase 4 — Fallback, Escalation, Disambiguation**
One fallback to completion. One escalation full chain. Intent collisions: disambiguation
strategy with rationale.

**Phase 4-SQ — Status Quo Simulation**
```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO |
SQ_DEFECT_CLASS | REMARKS
```
STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND, SQ_DEFECTS_NOT_FOUND.

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
1. TOPIC_COVERAGE_RATIO
2. TRANSITION_COVERAGE_RATIO
3. SLOT_PATH_COVERAGE_RATIO
4. TIMELINE_ANOMALY_RATE
5. PATH_ADHERENCE_RATIO

**Phase 5-F — Status Quo Coverage Table**
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION | FOUND_BY_STATUS_QUO |
DETECTION_METHOD | SQ_BLIND_SPOT
```
Auto-classification rules apply. Close with STATUS_QUO_GAP_SUMMARY.

Close per LIFECYCLE_PROTOCOL Transition 4 outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

Open per LIFECYCLE_PROTOCOL Transition 5 incoming.

The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate Verification + Phase 0-CA-1 Output Audit**

Phase 6-A is structured in three sequential blocks. The results of Blocks 1 and 2 are
consumed as the first two fields of Block 3's gate assertion. A gate asserting
CONTRACT_AUDIT_GATE_HONORED: PASS without CONFIRMED status in both Block 1 and Block 2
fields is a structurally incomplete gate assertion.

**Block 1 — WRONG_SCHEMA Residual Check** (enforcement closure for C-64/C-67 chain)

```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row carrying STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  RESOLVED: YES if declaration corrected to FIELD|VALUE format before Phase 1 began.
  RESOLVED: NO if declaration remained in wrong format — this is an unresolved residual.
  FINDING when RESOLVED: NO: PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows) |
                              CLEAN (all resolved) |
                              FINDINGS_PRESENT[unresolved declarations]
```

**Block 2 — Parenthetical Presence Verification** (enforcement closure for C-65/C-68 chain)

```
PARENTHETICAL_PRESENCE_VERIFICATION:

For each DECLARATION_SCHEMA_COMPLETE entry in Phase 0-CA-1:

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES; — if NO] | [see rule]
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES; — if NO] |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES; — if NO] |

  PARENTHETICAL_PRESENT: YES iff CA output shows "(count N rows: [breakdown])" inline
  with the PASS|FAIL verdict for that declaration.
  PARENTHETICAL_PRESENT: NO → FINDING: PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL
  [DECLARATION] — structural defect, not a quality gap.

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical]
```

**Block 3 — Contract Audit Gate Verification**

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

WRONG_SCHEMA_RESIDUAL_SWEEP field: cross-referenced from Block 1 result. FINDINGS_PRESENT
forces NOT_CONFIRMED and FAIL.
PARENTHETICAL_VERIFICATION field: cross-referenced from Block 2 result. FAIL forces
NOT_CONFIRMED and FAIL on the gate.

Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B — Severity Co-Residency Audit**
Per FOUND defect: SEVERITY_CLASS + INVARIANT_CITE both present. Structured table.

**Phase 6-C — Entanglement Consistency Audit**
Verify Phase 3-E map against Phase 1 turn-level evidence.

**Phase 6-D — Topic Aggregate Consistency Audit**
Cross-check Phase 1-T CONFORMANCE_ROLLUP vs DEVIATES count per topic.

**Phase 6-E — Session Timeline Consistency Audit**
Replay Phase 1-S; compare reconstructed SESSION_STATE vs Phase 1 SESSION_STATE.

**Phase 6-F — Fix Viability Audit**
Per EXECUTION_HALT: CONV_VIOLATIONS_INTRODUCED, VIABILITY, CHAIN_REPAIR_COMPLETE.

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

Open per LIFECYCLE_PROTOCOL Transition 5 incoming from Auditor.

For each FOUND defect, one PLAN_ITEM:
```
PLAN_ID: RP-NN
DEFECT_REF: [Phase 2 DEFECT_ID]
SEVERITY_CLASS: P0|P1|P2|P3
SCOPE: [topics/transitions/session variables]
DEPENDENCY_ON: [RP-NN list]
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG
TIER_RATIONALE: [P0 → IMMEDIATE; PLAN_TIER_OVERRIDE for CRITICAL deviations; P1 → NEXT_SPRINT; P2/P3 → BACKLOG]
CHAIN_REPAIR_ITEMS: [CONV-NN list from EXECUTION_HALT CHAIN_REPAIR; empty if none]
UNBLOCKED_BY: [observable confirmation]
```
Close: PLAN_SUMMARY: PLAN_ITEM_COUNT, IMMEDIATE_COUNT, NEXT_SPRINT_COUNT,
BACKLOG_COUNT, DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND.

---

## Variation Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-70 (SOLE_AUTHORITY in section; no HANDOFF_TO/Received inline in role instructions) | TARGET | — | — | TARGET | TARGET |
| C-69 (WRONG_SCHEMA_RESIDUAL_SWEEP as first gate field in CONTRACT_AUDIT_GATE_HONORED) | — | TARGET | — | TARGET | TARGET |
| C-71 (PARENTHETICAL_VERIFICATION as gate field in CONTRACT_AUDIT_GATE_HONORED) | — | — | TARGET | — | TARGET |
| C-66 (dedicated LIFECYCLE_PROTOCOL section, violation declaration at top, 5 labeled pairs) | PASS | — | — | PASS | PASS |
| C-67 (Phase 6-A WRONG_SCHEMA_RESIDUAL_CHECK, unresolved = finding) | PASS | PASS | PASS | PASS | PASS |
| C-68 (Phase 6-A PARENTHETICAL_PRESENCE_VERIFICATION, absent count = finding) | PASS | PASS | PASS | PASS | PASS |
| C-63 (5 HANDOFF_TO/Received transitions, all locked) | PASS | PASS | PASS | PASS | PASS |
| C-64 (SCHEMA_TYPE in manifest, WRONG_SCHEMA status) | PASS | PASS | PASS | PASS | PASS |
| C-65 (row-count parentheticals in CA output) | PASS | PASS | PASS | PASS | PASS |

**Key structural differences:**

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| LIFECYCLE_PROTOCOL section with SOLE_AUTHORITY — no-redeclaration declaration | YES | NO | NO | YES | YES |
| Role instructions use pointer-only references ("per Transition N") — no inline tokens | YES | NO | NO | YES | YES |
| WRONG_SCHEMA_RESIDUAL_SWEEP as first field in CONTRACT_AUDIT_GATE_HONORED | NO | YES | NO | YES | YES |
| PARENTHETICAL_VERIFICATION as field in CONTRACT_AUDIT_GATE_HONORED | NO | NO | YES | NO | YES |
| Both Block 1 and Block 2 results consumed as gate precondition fields in Block 3 | NO | NO | NO | NO | YES |
| Imperative constraint language (MUST NOT, PROHIBITED, CONSTRAINT VIOLATION) | NO | NO | YES | NO | NO |
| Standalone WRONG_SCHEMA_RESIDUAL_CHECK table with finding generation | YES | YES | YES | YES | YES |
| Standalone PARENTHETICAL_PRESENCE_VERIFICATION table with finding generation | YES | YES | YES | YES | YES |
