# Quest Variations — flow-conversation — Round 19 (v18 rubric)

**Date:** 2026-03-15 | **Rubric version:** v18 | **Max score:** 250

---

## Variation Axes Selected

All 5 variations carry the full v18 baseline: C-01 through C-74. Each is designed to
surface one or both of the two new criteria C-75 and C-76.

**New axes for R19 (targeting C-75 and C-76):**

- **Axis Y — Gate self-description completeness (C-75 target)**: CONTRACT_AUDIT_GATE_HONORED
  carries both citation axes simultaneously — the sweep-scope citation (Axis W, C-72) naming
  which FIELD|VALUE declarations were in scope for the WRONG_SCHEMA sweep, AND the parenthetical
  declaration citation (Axis X, C-74) naming each verified declaration with its confirmed row
  count. The gate is explicitly framed as a "complete standalone audit summary": a verifier
  reading only the gate can confirm both format compliance (sweep scope) and row-count
  completeness (parenthetical counts) without navigating to any standalone Phase 6-A table or
  Phase 0-CA-1 output. C-72 alone or C-74 alone does not satisfy C-75; both citation axes must
  be present in the gate simultaneously.

- **Axis Z — Single-source closure (C-76 target)**: Beyond having a dedicated LIFECYCLE_PROTOCOL
  section (C-66) with SOLE_AUTHORITY and pointer-only role instructions (C-70), Phase 6-A gains
  a LIFECYCLE_POINTER_AUDIT (C-73) that enumerates every "per LIFECYCLE_PROTOCOL Transition N"
  pointer reference across all role instruction blocks and verifies each resolves to a labeled
  entry. Together, C-70 (declaration layer: every transition declared exactly once) and C-73
  (reference layer: every pointer resolves) form the closed single-source enforcement system that
  C-76 requires. A trace satisfying C-70 but missing the C-73 LIFECYCLE_POINTER_AUDIT has
  declaration-level discipline but reference-level leakage; such a trace does not satisfy C-76.

**Single-axis (3):** Z, Y, phrasing register

- **Axis Z** — LIFECYCLE_PROTOCOL section with SOLE_AUTHORITY + pointer-only role instructions
  + LIFECYCLE_POINTER_AUDIT = C-76 closed system; gate uses simple sweep toggle (C-69, no scope
  citation) and simple parenthetical toggle (C-71, no declaration citation); C-75 not introduced
- **Axis Y** — Gate carries both sweep-scope citation AND parenthetical declaration citation
  simultaneously; lifecycle inline (no dedicated section; C-70/C-73/C-76 unaddressed); no
  LIFECYCLE_POINTER_AUDIT; only the gate format changes → C-75
- **Phrasing register** — Formal CONSTRAINT/MUST/PROHIBITED language throughout; lifecycle
  inline with CONSTRAINT framing; gate uses simple toggles (no scope citation, no declaration
  citation); neither C-75 nor C-76 introduced; control variation

**Combined (2):**

- **Axes Z + Y** — LIFECYCLE_PROTOCOL section + LIFECYCLE_POINTER_AUDIT + both citation axes
  in gate simultaneously; targets C-76 + C-75
- **Axes Z + Y + phrasing register** — Full R19 combination; all three axes; C-76 + C-75 +
  CONSTRAINT language throughout

---

## V-01 — Axis Z: Single-Source Closure (C-76 Target)

**Variation axis:** Lifecycle emphasis — the LIFECYCLE_PROTOCOL section is the sole
authoritative location for all role transition tokens, with SOLE_AUTHORITY declared at the
top. Role instruction blocks contain no inline HANDOFF_TO or Received strings; they reference
transitions by section name and number only (pointer-only, satisfying C-70). Phase 6-A gains
a LIFECYCLE_POINTER_AUDIT (C-73) that enumerates every pointer reference of the form "per
LIFECYCLE_PROTOCOL Transition N" across all role instruction blocks and verifies each cited
transition number resolves to a labeled entry in the LIFECYCLE_PROTOCOL section. Together C-70
(declaration layer) and C-73 (reference layer) form the closed single-source enforcement system
required by C-76. The gate uses the simple sweep toggle (C-69, no scope citation) and the simple
parenthetical toggle (C-71, no declaration citation). C-75 is not introduced in this variation.

**Hypothesis:** R18 V-05 achieved C-73 PASS by adding LIFECYCLE_POINTER_AUDIT to Phase 6-A
and achieved C-70 PASS by making the LIFECYCLE_PROTOCOL section SOLE_AUTHORITY. However, R18
did not explicitly name C-76 — the property that C-70 and C-73 together form a *closed*
enforcement system where the declaration layer and reference layer are both sealed. A trace
satisfying C-70 but missing C-73 has a correct single source but cannot guarantee all pointers
to it resolve; a trace with C-73 but without C-70's SOLE_AUTHORITY declaration can have
LIFECYCLE_POINTER_AUDIT pass while unauthorized re-declarations exist outside the audited scope.
C-76 is satisfied only when both layers are verified closed. This variation introduces explicit
"closed single-source enforcement system" language to make the C-76 dependency visible to the
model, and positions the LIFECYCLE_POINTER_AUDIT as the mandatory closure mechanism for the
reference layer — not an optional audit enhancement.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

**SOLE_AUTHORITY:** This section is the sole authoritative location for all role transition
tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this section.
Role instructions reference transitions by section name and transition number only. A HANDOFF_TO
or Received string appearing in any role instruction block is a lifecycle single-source violation.
Together this section (declaration layer) and the Phase 6-A LIFECYCLE_POINTER_AUDIT (reference
layer) form the closed single-source enforcement system: the declaration layer ensures every
transition is declared exactly once; the reference layer ensures every pointer to that layer
resolves. Neither layer alone closes the system.

Every role transition is a declared protocol event. The outgoing role MUST emit the token
declared below before its successor begins. The incoming role MUST open with the matching
acknowledgment before authoring any content. Implicit phase adjacency does not satisfy this
contract.

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
0-A-11) use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema contract.

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
    DEVIATION_BUDGET:         PASS|FAIL (count N rows: [breakdown])
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

Run LIFECYCLE_POINTER_AUDIT third. This audit closes the reference layer of the
single-source enforcement system: C-70 ensures no inline re-declarations exist outside
the LIFECYCLE_PROTOCOL section (declaration layer); this audit ensures every pointer
into that section resolves (reference layer). Together they satisfy C-76.
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

## V-02 — Axis Y: Gate Self-Description Completeness (C-75 Target)

**Variation axis:** Output format — CONTRACT_AUDIT_GATE_HONORED is reformatted so that both
citation axes are present simultaneously in the gate block. The WRONG_SCHEMA_RESIDUAL_SWEEP
field carries an explicit scope citation naming every FIELD|VALUE-annotated declaration checked
(Axis W, C-72). The PARENTHETICAL_VERIFICATION field carries an explicit citation of each
verified declaration with its confirmed row count (Axis X, C-74). Together these form a
complete standalone audit summary: a verifier reading only the gate can confirm both format
compliance (which declarations were in scope for the sweep) and row-count completeness (which
declarations were parenthetically verified and at what counts) without navigating to any
standalone Phase 6-A table or Phase 0-CA-1 output. The lifecycle is inline within role
instructions (no dedicated LIFECYCLE_PROTOCOL section; C-70, C-73, and C-76 are unaddressed).
The only structural change from the v18 baseline is the gate format.

**Hypothesis:** R18 V-02 achieved C-72 PASS (sweep-scope citation in gate) and R18 V-03
achieved C-74 PASS (parenthetical declaration citation in gate), but neither R18 variation
carried both simultaneously — V-02 had the sweep citation but simple parenthetical toggle;
V-03 had the declaration citation but simple sweep toggle. C-75 requires both C-72 and C-74
simultaneously in the same gate. This variation introduces the combined format for the first
time: the sweep field names its scope AND the parenthetical field names its declarations and
row counts in the same CONTRACT_AUDIT_GATE_HONORED block. A gate satisfying C-72 alone or
C-74 alone cannot satisfy C-75; the dual presence is the minimum condition. C-76 is not
introduced; lifecycle is inline.

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
0-A-11) use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. The Topology Architect may not begin Phase 0-D-0 until this manifest exists.

[Pre-Flight Manifest table identical to V-01 with SCHEMA_TYPE column and PENDING statuses.]

Close with: **HANDOFF_TO: TOPOLOGY ARCHITECT**

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST."**

[Phase 0-D-0 through Phase 0-A-11 — identical structure and instructions to V-01.]

Close with: **HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect."**

Update manifest with COMPLETE|MISSING|WRONG_SCHEMA statuses. WRONG_SCHEMA blocks Phase 1
alongside MISSING.

[Resolved manifest and Phase 0-CA-1 output with row-count parentheticals — identical to V-01.]

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

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

Then emit gate assertion. The CONTRACT_AUDIT_GATE_HONORED block is a complete standalone
audit summary. Both citation axes are present simultaneously: the sweep field names its
scope (which declarations were checked), and the parenthetical field names each verified
declaration with its confirmed row count. A verifier reading only this block can confirm
format compliance and row-count completeness without navigating to Phase 6-A tables or
Phase 0-CA-1 output.

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

Close Phase 6-A with: **AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER**

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

[Identical PLAN_ITEM structure and PLAN_SUMMARY close to V-01.]

---

## V-03 — Phrasing Register: Formal CONSTRAINT Language (Control)

**Variation axis:** Phrasing register — formal CONSTRAINT/MUST/PROHIBITED language frames
every role boundary and every schema requirement as an enforceable constraint, not a
recommendation. The lifecycle protocol is inline with CONSTRAINT phrasing (no dedicated
LIFECYCLE_PROTOCOL section; C-70 and C-73 are unaddressed; C-76 not satisfied). The gate
uses the simple sweep toggle (C-69, no scope citation) and the simple parenthetical toggle
(C-71, no declaration citation); C-75 not satisfied. This is a control variation: neither new
R19 criterion is introduced. The phrasing register change is the sole axis.

**Hypothesis:** Explicit CONSTRAINT/MUST/PROHIBITED framing in role instructions may improve
adherence to the nine-defect class inventory, FIELD|VALUE schema discipline, and gate structure
without introducing any new criteria. If the CONSTRAINT register achieves comparable essential
and recommended criterion scores to V-01 and V-02, it confirms that phrasing register is an
independent axis from the lifecycle-emphasis and output-format axes: all three can be combined
in V-05 without confounding.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

**STRUCTURAL CONSTRAINT:** Five roles participate. Crossing a role boundary without emitting
the outgoing token AND without the successor opening with the matching acknowledgment is a
LIFECYCLE_CONSTRAINT_VIOLATION. Silent fallthrough is PROHIBITED.

**Lifecycle protocol constraints:**
1. CONSTRAINT: Phase -1 MUST close with `HANDOFF_TO: TOPOLOGY ARCHITECT`.
   CONSTRAINT: Topology Architect MUST open with `"Received PRE_FLIGHT_MANIFEST."` before
   authoring Phase 0-D-0.
2. CONSTRAINT: Phase 0 MUST close with `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`.
   CONSTRAINT: Contract Auditor MUST open with `"Received Phase 0 from Topology Architect."`
   before Phase 0-CA-1.
3. CONSTRAINT: Phase 0-CA-1 MUST close with `GATE_STATUS: [value] issued. HANDOFF_TO:
   DEVELOPER`. CONSTRAINT: Developer MUST open with `"Received GATE_STATUS: [value].
   Proceeding|Blocked."` before Phase 1. GATE_STATUS: FAIL is PROHIBITED from executing Phase 1.
4. CONSTRAINT: Developer MUST close with `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO:
   AUDITOR`. CONSTRAINT: Auditor MUST open with `"Received DEVELOPER_CERTIFICATION: COMPLETE.
   Beginning independent audit."` before Phase 6.
5. CONSTRAINT: Auditor MUST close Phase 6-A with `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO:
   REPORT PRODUCER`. CONSTRAINT: Report Producer MUST open with `"Received AUDITOR_CERTIFICATION:
   COMPLETE."` before Phase 7.

**SCHEMA CONSTRAINT:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10, 0-A-11) MUST
use FIELD|VALUE table rows. Prose field descriptions are PROHIBITED and do not satisfy the schema
contract. A declaration present in prose format carries STATUS: WRONG_SCHEMA, which blocks Phase 1.

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

CONSTRAINT: Execute FIRST. No Topology Architect authoring is PERMITTED before this manifest
exists.

[Pre-Flight Manifest table identical to V-01 with SCHEMA_TYPE column and PENDING statuses.]

CONSTRAINT: Close with `HANDOFF_TO: TOPOLOGY ARCHITECT`.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

CONSTRAINT: Open with `"Received PRE_FLIGHT_MANIFEST."` before any Phase 0-D-0 authoring.

[Phase 0-D-0 through Phase 0-A-11 — identical structure to V-01. FIELD|VALUE format is a
CONSTRAINT, not a recommendation.]

CONSTRAINT: Close with `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

CONSTRAINT: Open with `"Received Phase 0 from Topology Architect."` before auditing.

Update manifest. STATUS values: COMPLETE | MISSING | WRONG_SCHEMA. WRONG_SCHEMA status is
PROHIBITED from proceeding to Phase 1 alongside MISSING status.

[Resolved manifest and Phase 0-CA-1 output with mandatory row-count parentheticals — identical
to V-01.]

GATE_STATUS: FAIL if any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

CONSTRAINT: Close with `GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER`.

---

### ROLE 3 — DEVELOPER: Phases 1–5

CONSTRAINT: Open with `"Received GATE_STATUS: [value]. Proceeding|Blocked."`. GATE_STATUS:
FAIL is PROHIBITED from executing Phase 1; any Phase 1 content following a received FAIL
is an unauthorized execution finding.

[Phases 1-S through 5-F — identical structure and instructions to V-01. CONSTRAINT: Phase 1-S
MUST be authored before Phase 1. SESSION_STATE derivation from Phase 1-S replay is REQUIRED.]

Nine defect classes are REQUIRED: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP.
Each class MUST be either FOUND (with example) or CONFIRMED_ABSENT (with scope statement).

CONSTRAINT: Close with `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR`.

---

### ROLE 4 — AUDITOR: Phase 6

CONSTRAINT: Open with `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent
audit."`. The Auditor is PROHIBITED from modifying Developer rows. All discrepancies MUST
be recorded as audit findings.

**Phase 6-A — Gate and Protocol Verification**

CONSTRAINT: Run WRONG_SCHEMA_RESIDUAL_CHECK before emitting gate assertion.
[Identical table structure to V-01.]

CONSTRAINT: Run PARENTHETICAL_PRESENCE_VERIFICATION before emitting gate assertion.
[Identical table structure to V-01.]

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

CONSTRAINT: Close Phase 6-A with `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`.

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

CONSTRAINT: Open with `"Received AUDITOR_CERTIFICATION: COMPLETE."`.

[Identical PLAN_ITEM structure and PLAN_SUMMARY close to V-01.]

---

## V-04 — Axes Z + Y: Single-Source Closure + Gate Self-Description (C-76 + C-75)

**Variation axes:** Lifecycle emphasis + Output format — V-01's LIFECYCLE_PROTOCOL dedicated
section (Axis Z: SOLE_AUTHORITY + pointer-only role instructions + LIFECYCLE_POINTER_AUDIT)
is combined with V-02's self-describing gate format (Axis Y: both sweep-scope citation and
parenthetical declaration citation simultaneously in CONTRACT_AUDIT_GATE_HONORED). This
variation targets both C-76 and C-75 in a single artifact.

**Hypothesis:** C-76 is satisfied when the declaration layer (SOLE_AUTHORITY section, C-70)
and reference layer (LIFECYCLE_POINTER_AUDIT, C-73) are both closed. C-75 is satisfied when
the gate carries both sweep-scope citation (C-72) and parenthetical declaration citation (C-74)
simultaneously. V-04 is the first variation to target both new R19 criteria in combination.
The combination tests whether the two axes are compositionally independent: if the LIFECYCLE_
POINTER_AUDIT finding count is zero, the gate self-description should report a clean sweep
scope, and the parenthetical field should confirm its declarations — neither enforcement layer
should interfere with the other.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

[Identical to V-01: SOLE_AUTHORITY declaration, Transitions 1–5 as labeled entries,
closing rule about lifecycle gap findings.]

---

**Roles and universal format constraint:** [Identical to V-01.]

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST per LIFECYCLE_PROTOCOL Transition 1 outgoing.

[Pre-Flight Manifest table identical to V-01.]

Close per LIFECYCLE_PROTOCOL Transition 1 outgoing.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per LIFECYCLE_PROTOCOL Transition 1 incoming.

[Phase 0-D-0 through Phase 0-A-11 — identical to V-01.]

Close per LIFECYCLE_PROTOCOL Transition 2 outgoing.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per LIFECYCLE_PROTOCOL Transition 2 incoming.

[Resolved manifest and Phase 0-CA-1 output with mandatory row-count parentheticals —
identical to V-01.]

Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per LIFECYCLE_PROTOCOL Transition 3 incoming. GATE_STATUS: FAIL blocks Phase 1.

[Phases 1-S through 5-F — identical to V-01.]

Close per LIFECYCLE_PROTOCOL Transition 4 outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

Open per LIFECYCLE_PROTOCOL Transition 4 incoming.
The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Run WRONG_SCHEMA_RESIDUAL_CHECK first. [Identical to V-01.]

Run PARENTHETICAL_PRESENCE_VERIFICATION second. [Identical to V-01.]

Run LIFECYCLE_POINTER_AUDIT third. [Identical to V-01: enumerate all "per LIFECYCLE_PROTOCOL
Transition N" pointer references, verify each resolves to Transitions 1–5, DANGLING_LIFECYCLE_
POINTER finding for unresolved. LIFECYCLE_POINTER_AUDIT closes the reference layer of the
single-source enforcement system alongside C-70's declaration layer; together they satisfy C-76.]

Then emit gate assertion. The gate is a complete standalone audit summary: both sweep-scope
citation AND parenthetical declaration citation are present simultaneously, enabling a verifier
to confirm format compliance (sweep scope) and row-count completeness (parenthetical counts)
from the gate alone without navigating to standalone tables.

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

Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B through 6-H:** [Identical to V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per LIFECYCLE_PROTOCOL Transition 5 incoming.

[Identical PLAN_ITEM structure and PLAN_SUMMARY close to V-01.]

---

## V-05 — Axes Z + Y + Phrasing Register: Full R19 Combination

**Variation axes:** Lifecycle emphasis + Output format + Phrasing register — V-04's combined
LIFECYCLE_PROTOCOL section (Axis Z) and self-describing gate (Axis Y) are overlaid with the
formal CONSTRAINT/MUST/PROHIBITED phrasing register from V-03. Every role boundary is declared
as a structural constraint. The LIFECYCLE_PROTOCOL section carries SOLE_AUTHORITY with explicit
enforcement language. The gate asserts both sweep-scope and parenthetical citations. The LIFECYCLE_
POINTER_AUDIT is required as the reference-layer closure mechanism for C-76.

**Hypothesis:** The full R19 combination tests whether CONSTRAINT framing reinforces the
single-source enforcement system described in C-76 and the gate self-description property
described in C-75. Specifically: (1) CONSTRAINT language around the SOLE_AUTHORITY declaration
should reduce unauthorized re-declarations in role instruction blocks; (2) CONSTRAINT language
in Phase 6-A LIFECYCLE_POINTER_AUDIT framing should reinforce that every pointer must resolve,
not just that the audit table must be present; (3) CONSTRAINT framing on the gate fields should
reinforce that both citation axes are structurally mandatory, not optional enhancements. If V-05
achieves both C-75 and C-76 PASS with higher frequency than V-04, the phrasing register
contributes to enforceability beyond the structural axes alone.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is PROHIBITED and constitutes a structural violation.

**SOLE_AUTHORITY CONSTRAINT:** This section is the sole authoritative location for all role
transition tokens. HANDOFF_TO and Received acknowledgment strings MUST NOT appear outside this
section. Role instructions MUST reference transitions by section name and transition number only.
A HANDOFF_TO or Received string appearing in any role instruction block is a LIFECYCLE_SINGLE_
SOURCE_VIOLATION. Together this section (declaration layer) and the Phase 6-A LIFECYCLE_POINTER_
AUDIT (reference layer) form the closed single-source enforcement system: declaration layer
ensures every transition is declared exactly once; reference layer ensures every pointer to that
layer resolves. Both layers MUST be closed for single-source enforcement to hold.

Every role transition is a declared protocol event. The outgoing role MUST emit the token below
before its successor begins. The incoming role MUST open with the matching acknowledgment before
authoring any content. Implicit phase adjacency is PROHIBITED.

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

A role that begins authoring without the incoming acknowledgment declared in this section is a
lifecycle gap finding. GATE_STATUS: FAIL is PROHIBITED from executing Phase 1.

---

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**SCHEMA CONSTRAINT:** All structured Phase 0 declarations (0-A-8, 0-A-9, 0-A-10, 0-A-11) MUST
use FIELD|VALUE table rows. Prose field descriptions are PROHIBITED. A declaration in prose format
carries STATUS: WRONG_SCHEMA and MUST block Phase 1 execution.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

CONSTRAINT: Execute FIRST per LIFECYCLE_PROTOCOL Transition 1 outgoing. Topology Architect
authoring is PROHIBITED before this manifest exists.

[Pre-Flight Manifest table identical to V-01 with SCHEMA_TYPE column and PENDING statuses.]

CONSTRAINT: Close per LIFECYCLE_PROTOCOL Transition 1 outgoing.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

CONSTRAINT: Open per LIFECYCLE_PROTOCOL Transition 1 incoming before any Phase 0-D-0 authoring.

[Phase 0-D-0 through Phase 0-A-11 — identical structure to V-01. FIELD|VALUE format is a
CONSTRAINT for all 0-A-8, 0-A-9, 0-A-10, 0-A-11 declarations.]

CONSTRAINT: Close per LIFECYCLE_PROTOCOL Transition 2 outgoing.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

CONSTRAINT: Open per LIFECYCLE_PROTOCOL Transition 2 incoming before auditing.

Update manifest. WRONG_SCHEMA is PROHIBITED from proceeding alongside MISSING.

[Resolved manifest and Phase 0-CA-1 output with mandatory row-count parentheticals —
identical to V-01.]

GATE_STATUS: FAIL if any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

CONSTRAINT: Close per LIFECYCLE_PROTOCOL Transition 3 outgoing.

---

### ROLE 3 — DEVELOPER: Phases 1–5

CONSTRAINT: Open per LIFECYCLE_PROTOCOL Transition 3 incoming. GATE_STATUS: FAIL is PROHIBITED
from executing Phase 1; any Phase 1 content following a received FAIL is an unauthorized execution
finding.

CONSTRAINT: Phase 1-S MUST be authored before Phase 1. SESSION_STATE is DERIVED by replaying
Phase 1-S mutations; independent SESSION_STATE authoring is PROHIBITED.

[Phases 1-S through 5-F — identical structure to V-01. Nine defect classes REQUIRED: DEAD_END,
INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHANED_TOPIC, TIMELINE_ANOMALY,
CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP. Each MUST be FOUND (with example)
or CONFIRMED_ABSENT (with explicit scope statement).]

CONSTRAINT: Close per LIFECYCLE_PROTOCOL Transition 4 outgoing.

---

### ROLE 4 — AUDITOR: Phase 6

CONSTRAINT: Open per LIFECYCLE_PROTOCOL Transition 4 incoming. Developer rows are PROHIBITED
from modification. All discrepancies MUST be recorded as audit findings.

**Phase 6-A — Gate and Protocol Verification**

CONSTRAINT: Run WRONG_SCHEMA_RESIDUAL_CHECK before emitting gate assertion. [Identical to V-01.]

CONSTRAINT: Run PARENTHETICAL_PRESENCE_VERIFICATION before emitting gate assertion.
[Identical to V-01.]

CONSTRAINT: Run LIFECYCLE_POINTER_AUDIT before emitting gate assertion. This audit is the
reference-layer closure mechanism for C-76: C-70's SOLE_AUTHORITY section closes the declaration
layer; this audit MUST close the reference layer. Every "per LIFECYCLE_PROTOCOL Transition N"
pointer across all role instruction blocks MUST be verified as resolving to a labeled transition.
An unresolved pointer is PROHIBITED; it earns a DANGLING_LIFECYCLE_POINTER finding. The audit
MUST NOT be omitted even when all pointers are expected to resolve — the audit table is the
closure evidence, not the SOLE_AUTHORITY section itself.
[Identical audit table structure, rules, and LIFECYCLE_POINTER_AUDIT_STATUS format to V-01.]

CONSTRAINT: Emit gate assertion as a complete standalone audit summary. Both citation axes MUST
be present simultaneously — sweep-scope citation (Axis W) and parenthetical declaration citation
(Axis X) — so that a verifier reading only the gate can confirm format compliance and row-count
completeness without navigating to standalone Phase 6-A tables or Phase 0-CA-1 output. A gate
carrying only one citation axis does not satisfy C-75.

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

CONSTRAINT: Close Phase 6-A per LIFECYCLE_PROTOCOL Transition 5 outgoing.

**Phase 6-B — Severity Co-Residency Audit**
Per FOUND defect: SEVERITY_CLASS MUST be present + INVARIANT_CITE MUST be present. Structured
table REQUIRED. CONFIRMED_ABSENT rows are EXEMPT.

**Phase 6-C — Entanglement Consistency Audit**
CONSTRAINT: Verify Phase 3-E map against Phase 1 turn-level evidence. Discrepancies are
PROHIBITED from going unreported.

**Phase 6-D — Topic Aggregate Consistency Audit**
CONSTRAINT: Cross-check Phase 1-T CONFORMANCE_ROLLUP vs DEVIATES count per topic in Phase 1.
TOPIC_ROLLUP_MISMATCH finding REQUIRED for any discrepancy.

**Phase 6-E — Session Timeline Consistency Audit**
CONSTRAINT: Replay Phase 1-S; compare reconstructed SESSION_STATE vs Phase 1 SESSION_STATE.
TIMELINE_STATE_MISMATCH finding REQUIRED for any discrepancy.

**Phase 6-F — Fix Viability Audit**
Per EXECUTION_HALT: CONV_VIOLATIONS_INTRODUCED, CONV_VIOLATIONS_DETAIL,
VIABILITY: VIABLE|SIDE_EFFECTS_FOUND, CHAIN_REPAIR_COMPLETE.

**Phase 6-G — Chain Integrity Audit**
Per CHAIN-NN: CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL.

**Phase 6-H — Combined Plan / Path / Status Quo Audit**
[Identical scope to V-01: Plan integrity, path adherence, status quo coverage audit.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

CONSTRAINT: Open per LIFECYCLE_PROTOCOL Transition 5 incoming.

[Identical PLAN_ITEM structure and PLAN_SUMMARY close to V-01.]
