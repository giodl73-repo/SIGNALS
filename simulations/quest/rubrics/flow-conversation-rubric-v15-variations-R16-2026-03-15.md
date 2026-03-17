# Quest Variations — flow-conversation — Round 16 (v15 rubric)

**Date:** 2026-03-15 | **Rubric version:** v15 | **Max score:** 234

---

## Variation Axes Selected

All 5 variations carry the full v15 baseline: C-01 through C-65, plus the three
new criteria C-66 through C-68 each variation is explicitly designed to surface.
The baseline includes: PRE_FLIGHT_MANIFEST as Phase -1 with SCHEMA_TYPE column and
WRONG_SCHEMA status (C-64), COLUMN_SCHEMA_REGISTRY as Phase 0-D-0 first artifact (C-61),
universal FIELD|VALUE Phase 0-A declarations, all 5 HANDOFF_TO/Received lifecycle tokens
(C-63), CA row-count parentheticals (C-65), nine defect classes, EXECUTION_HALT with
CHAIN_BREAK_TRACE, STATUS_QUO_SIMULATION (Phase 4-SQ), STATUS_QUO_COVERAGE (Phase 5-F),
DECLARATION_SCHEMA_COMPLETE with parenthetical row counts, and REMEDIATION PLANNER (Phase 7).

**New axes for R16 (targeting C-66, C-67, C-68):**

- **Axis P — Protocol Section Artifact (C-66 target)**: Extract the lifecycle protocol
  from inline role instructions into a first-class dedicated named section that appears
  before any role definitions begin. The section opens with "Silent fallthrough is a
  structural violation" as its first declaration, then lists all 5 transitions as labeled
  HANDOFF_TO outgoing / Received incoming pairs. This makes the contract declarative and
  machine-verifiable rather than emergent from reading through role instruction prose.
  C-66 requires: dedicated section (not inline), structural violation declaration at top,
  all 5 transitions as labeled pairs within that section.

- **Axis Q — WRONG_SCHEMA Enforcement Chain (C-67 target)**: Add an explicit
  WRONG_SCHEMA_RESIDUAL_CHECK sub-phase to Phase 6-A that enumerates every manifest row
  from Phase 0-CA-1 that carried STATUS: WRONG_SCHEMA, verifies whether each was corrected
  before Phase 1 execution, and flags any unresolved entry as a named Phase 6-A finding.
  This closes the enforcement loop: manifest-time detection (Phase 0-CA-1) → audit-time
  residual verification (Phase 6-A). A WRONG_SCHEMA row not corrected becomes
  PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED rather than an incidental observation.

- **Axis R — Parenthetical Verification (C-68 target)**: Add a
  PARENTHETICAL_PRESENCE_VERIFICATION sub-phase to Phase 6-A that checks each
  DECLARATION_SCHEMA_COMPLETE entry from Phase 0-CA-1 for the presence of its row-count
  parenthetical. Absence of a parenthetical triggers PHASE_6A_FINDING:
  MISSING_ROW_COUNT_PARENTHETICAL — a structural defect, not a quality gap. This creates
  audit coverage for C-65 compliance rather than relying on CA self-enforcement.

**Single-axis (3):** P, Q, R

- **Axis P — Protocol section artifact**: dedicated LIFECYCLE_PROTOCOL section, structural
  violation declaration first, all 5 transitions as labeled pairs
- **Axis Q — WRONG_SCHEMA enforcement chain**: Phase 6-A WRONG_SCHEMA_RESIDUAL_CHECK table,
  unresolved entries become Phase 6-A findings
- **Axis R — Parenthetical verification**: Phase 6-A PARENTHETICAL_PRESENCE_VERIFICATION
  table, absent row count = Phase 6-A finding

**Combined (2):**

- **Axes P+Q — Protocol section + WRONG_SCHEMA chain**: dedicated section + audit-time
  WRONG_SCHEMA sweep; targets C-66 + C-67
- **Axes P+Q+R — Full R16 combination**: all three axes; C-68 parenthetical check is
  structurally linked to the WRONG_SCHEMA sweep as a unified Phase 0-CA-1 output audit

---

## V-01 — Axis P: Protocol Section Artifact

**Variation axis:** Lifecycle emphasis — the lifecycle protocol is extracted from role
instruction prose and issued as a dedicated named section (`## LIFECYCLE_PROTOCOL`) that
precedes all role definitions. "Silent fallthrough is a structural violation" is the first
statement in the section. All 5 transitions are declared as labeled HANDOFF_TO + Received
pairs within a fenced block in that section. Role instructions reference the protocol
rather than re-declare it.

**Hypothesis:** R15 V-05 achieved C-63 through role instructions that contained the
HANDOFF_TO/Received language, but the protocol remained emergent — a reader had to traverse
all role sections to reconstruct the full contract. C-66 requires the protocol to be a
first-class artifact: a named section that is machine-verifiable on its own, before any
role instructions are read. Making the protocol section the first structural element of
the prompt — with the violation declaration at top — satisfies C-66 while leaving
C-67 and C-68 unaddressed.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

Every role transition is a declared protocol event. The outgoing role MUST emit the token
below before its successor begins. The incoming role MUST open with the matching
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

A role that begins authoring without the incoming acknowledgment cited above is a
lifecycle gap finding, regardless of whether the outgoing token was present.

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

Close with LIFECYCLE_PROTOCOL Transition 1 token: **HANDOFF_TO: TOPOLOGY ARCHITECT**

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per Transition 2 incoming: **"Received PRE_FLIGHT_MANIFEST."**

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
Every variable from Phase 0-D-3 must have a row.

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

Close per Transition 2 outgoing: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per Transition 3 incoming: **"Received Phase 0 from Topology Architect."**

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

Then emit Phase 0-CA-1 output:
```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list — VARS_IN_TOPOLOGY not in VARS_IN_CONTRACT]
  CHAIN_BUDGET_DELTA: [empty or list — CHAINS_IN_TOPOLOGY not in CHAINS_IN_BUDGET]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET:         PASS|FAIL (count N rows: [named breakdown, e.g. "5 rows: P0/P1/P2/P3 + RATIONALE"])
    CONV_CHAIN_BUDGET:        PASS|FAIL (count N rows: [N rows: 5 fields per chain × M chains])
    TURN_PREDICTION_CONTRACT: PASS|FAIL (count N rows: [4 rows per path × M paths + 1 signed row])
    STATUS_QUO_METHOD:        PASS|FAIL (count N rows: [9 rows: 3 metadata + 5 BLIND + SIGNED])
  PREDICTION_CONTRACT_SIGNED:    YES|NO
  STATUS_QUO_METHOD_SIGNED:      YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any manifest row MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, any delta non-empty, or any signature NO.

Close per Transition 3 outgoing: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per Transition 4 incoming: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
GATE_STATUS: FAIL blocks Phase 1. Any Phase 1 content following a received FAIL is an
unauthorized execution finding.

**Phase 1-S — Session Variable Mutation Log (author BEFORE Phase 1)**
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE cells in Phase 1 are derived by replaying Phase 1-S in turn order.
Each SESSION_STATE cell cites its Phase 1-S source row.

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
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION,
CONTRACT_GAP.

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

Close per Transition 4 outgoing:
**"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open per Transition 5 incoming:
**"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

The Auditor never modifies Developer rows. All discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**
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

Close Phase 6-A with Transition 5 outgoing:
**"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

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

Open per Transition 5 incoming from Auditor:
**"Received AUDITOR_CERTIFICATION: COMPLETE."**

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

## V-02 — Axis Q: WRONG_SCHEMA Enforcement Chain

**Variation axis:** Role sequence — Phase 6-A opens with a WRONG_SCHEMA_RESIDUAL_CHECK
table before any other verification. The table enumerates every manifest row from
Phase 0-CA-1 that carried STATUS: WRONG_SCHEMA, verifies resolution, and flags
unresolved entries as named Phase 6-A findings. The lifecycle protocol remains inline
within role instructions (no dedicated section).

**Hypothesis:** R15 introduced WRONG_SCHEMA as a manifest status that blocks Phase 1
execution. But Phase 6-A in R15 only verifies that the gate was honored — it does not
explicitly sweep for WRONG_SCHEMA residuals that might have been incorrectly marked
COMPLETE or bypassed. C-67 requires Phase 6-A to serve as the audit-time closure for
manifest-time WRONG_SCHEMA detection. By making WRONG_SCHEMA_RESIDUAL_CHECK the first
Phase 6-A item — before gate verification — unresolved WRONG_SCHEMA entries become
findable Phase 6-A defects rather than implicit gate-honored artifacts.

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
HANDOFF_TO: TOPOLOGY ARCHITECT
```

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST."**

[Phase 0-D-0 through Phase 0-A-11 — same as V-01 above.]

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect."**

Update manifest. WRONG_SCHEMA applies to rows annotated SCHEMA_TYPE: FIELD|VALUE where
the declaration exists but uses prose or a non-FIELD|VALUE table format. MISSING applies
only when the declaration is absent entirely. Both WRONG_SCHEMA and MISSING block Phase 1.

```
PRE_FLIGHT_MANIFEST (resolved):

REQUIRED_DECLARATION                           | PHASE_REF | SCHEMA_TYPE   | STATUS
-----------------------------------------------|-----------|---------------|---------------------------
[same rows as Phase -1 manifest, resolved to COMPLETE|MISSING|WRONG_SCHEMA]
```

Then emit:
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

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

[Same as V-01 — all phases 1-S through 5-F with Developer certification close.]

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

**Phase 6-A — Gate, WRONG_SCHEMA Residual, and Protocol Verification**

The Auditor opens Phase 6-A with the WRONG_SCHEMA residual sweep BEFORE gate verification.
This sweep is the enforcement closure for manifest-time WRONG_SCHEMA detection.

```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if the declaration was corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO if the declaration remained in wrong format; this is an unresolved WRONG_SCHEMA residual
    - FINDING: when RESOLVED: NO → PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN (no WRONG_SCHEMA rows in Phase 0-CA-1) |
                              CLEAN (all WRONG_SCHEMA rows resolved) |
                              FINDINGS_PRESENT[list of unresolved declarations]
```

If WRONG_SCHEMA_RESIDUAL_SWEEP shows FINDINGS_PRESENT, each unresolved declaration
becomes a Phase 6-A audit finding before any other verification proceeds.

Then continue:
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
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

Close Phase 6-A: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

**Phase 6-B through 6-H:** [Same as V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

[Same as V-01 — PLAN_ITEM per defect, PLAN_SUMMARY close.]

---

## V-03 — Axis R: Parenthetical Verification

**Variation axis:** Output format — Phase 6-A includes a PARENTHETICAL_PRESENCE_VERIFICATION
table after gate verification. One row per DECLARATION_SCHEMA_COMPLETE entry from
Phase 0-CA-1. PARENTHETICAL_PRESENT: YES|NO. When NO: PHASE_6A_FINDING:
MISSING_ROW_COUNT_PARENTHETICAL[DECLARATION]. The lifecycle protocol remains inline
within role instructions (no dedicated section). No WRONG_SCHEMA sweep.

**Hypothesis:** R15 established that DECLARATION_SCHEMA_COMPLETE entries must carry
row-count parentheticals (C-65). But the CA self-verifies this — Phase 6-A in R15 does
not independently check for parenthetical presence. C-68 requires absence of a row count
to be a findable Phase 6-A defect rather than a CA omission that passes audit silently.
Structuring parenthetical verification as a named Phase 6-A table with explicit
FINDING generation creates audit coverage without requiring C-67's WRONG_SCHEMA sweep.

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

**Roles and universal format constraint:** [Same as V-01.]

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

[Same as V-02 — manifest with SCHEMA_TYPE column, HANDOFF_TO: TOPOLOGY ARCHITECT.]

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

[Same as V-01 — Phase 0-D-0 through Phase 0-A-11, HANDOFF_TO: CONTRACT AUDITOR close.]

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

[Same as V-02 — resolved manifest with WRONG_SCHEMA, row-count parentheticals in
DECLARATION_SCHEMA_COMPLETE, GATE_STATUS close.]

### ROLE 3 — DEVELOPER: Phases 1–5

[Same as V-01 — all phases 1-S through 5-F with Developer certification close.]

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

**Phase 6-A — Gate, Protocol, and Parenthetical Verification**

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
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

Then emit the parenthetical verification table:

```
PARENTHETICAL_PRESENCE_VERIFICATION:

For each DECLARATION_SCHEMA_COMPLETE entry in Phase 0-CA-1:

  DECLARATION              | CA_VERDICT | PARENTHETICAL_PRESENT | ROW_COUNT_CITED | FINDING
  -------------------------|-----------|-----------------------|-----------------|--------
  DEVIATION_BUDGET         | PASS|FAIL | YES|NO                | [N if YES]      | [see below]
  CONV_CHAIN_BUDGET        | PASS|FAIL | YES|NO                | [N if YES]      |
  TURN_PREDICTION_CONTRACT | PASS|FAIL | YES|NO                | [N if YES]      |
  STATUS_QUO_METHOD        | PASS|FAIL | YES|NO                | [N if YES]      |

Rules:
  - PARENTHETICAL_PRESENT: YES iff CA output shows "(count N rows: [breakdown])" inline
    with the PASS|FAIL verdict
  - PARENTHETICAL_PRESENT: NO → FINDING: PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL
    [DECLARATION] — this is a structural defect, not a quality observation
  - A CA verdict of PASS without a parenthetical does not satisfy C-65; the Auditor must
    flag the omission regardless of whether the declaration contents were correct

PARENTHETICAL_VERIFICATION: PASS | FAIL[declarations missing parenthetical: list]
```

Close Phase 6-A: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

**Phase 6-B through 6-H:** [Same as V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

[Same as V-01.]

---

## V-04 — Axes P+Q: Protocol Section Artifact + WRONG_SCHEMA Enforcement Chain

**Variation axes:** Lifecycle emphasis (Axis P) + Role sequence (Axis Q). The LIFECYCLE_PROTOCOL
is a dedicated named section before all role definitions (targeting C-66). Phase 6-A opens
with WRONG_SCHEMA_RESIDUAL_CHECK before gate verification (targeting C-67). Phase 6-A does
NOT include a PARENTHETICAL_PRESENCE_VERIFICATION table (C-68 unaddressed).

**Hypothesis:** Axes P and Q are independent enforcement channels — the protocol section
ensures the lifecycle contract is a machine-verifiable artifact (C-66), and the WRONG_SCHEMA
residual sweep ensures manifest-time WRONG_SCHEMA detection propagates to audit-time findings
(C-67). Their combination should satisfy both C-66 and C-67 simultaneously. C-68 requires a
third explicit Phase 6-A table; without Axis R that criterion remains unsatisfied.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

Every role transition is a declared protocol event. The outgoing role MUST emit the token
below before its successor begins. The incoming role MUST open with the matching
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

A role that begins authoring without the incoming acknowledgment cited above is a
lifecycle gap finding, regardless of whether the outgoing token was present.

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

[Same manifest as V-01 — with SCHEMA_TYPE column, HANDOFF_TO: TOPOLOGY ARCHITECT close.]

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per Transition 2 incoming: **"Received PRE_FLIGHT_MANIFEST."**

[Phase 0-D-0 through Phase 0-A-11 — same as V-01.]

Close per Transition 2 outgoing:
**"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per Transition 3 incoming: **"Received Phase 0 from Topology Architect."**

[Resolved manifest with COMPLETE|MISSING|WRONG_SCHEMA, all blocking checks, row-count
parentheticals in DECLARATION_SCHEMA_COMPLETE — same as V-02.]

Close per Transition 3 outgoing:
**"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per Transition 4 incoming:
**"Received GATE_STATUS: [value]. Proceeding|Blocked."**

[All phases 1-S through 5-F — same as V-01.]

Close per Transition 4 outgoing:
**"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open per Transition 5 incoming:
**"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

**Phase 6-A — Gate, WRONG_SCHEMA Residual, and Protocol Verification**

The Auditor opens Phase 6-A with the WRONG_SCHEMA residual sweep BEFORE gate verification.

```
WRONG_SCHEMA_RESIDUAL_CHECK:

For each manifest row that carried STATUS: WRONG_SCHEMA in Phase 0-CA-1:

  DECLARATION | PHASE_REF | WRONG_SCHEMA_AT_CA | CORRECTED_BEFORE_PHASE_1 | RESOLVED: YES|NO | FINDING

  Rules:
    - RESOLVED: YES if declaration corrected to FIELD|VALUE format before Phase 1 began
    - RESOLVED: NO if declaration remained in wrong format
    - FINDING: when RESOLVED: NO → PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED[DECLARATION, PHASE_REF]

WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN | FINDINGS_PRESENT[list]
```

Then continue gate verification:
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
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

Close Phase 6-A per Transition 5 outgoing:
**"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

**Phase 6-B through 6-H:** [Same as V-01.]

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open per Transition 5 incoming: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

[Same as V-01.]

---

## V-05 — Axes P+Q+R: Full R16 Combination

**Variation axes:** Lifecycle emphasis (Axis P) + Role sequence (Axis Q) + Output format
(Axis R). All three new criteria targeted: C-66 (dedicated protocol section), C-67
(WRONG_SCHEMA residual check), C-68 (parenthetical presence verification). Axis R is
structurally linked to Axis Q: the PARENTHETICAL_PRESENCE_VERIFICATION is positioned as
the second sub-phase of the Phase 6-A output audit, forming a unified Phase 0-CA-1 output
contract verification block. This makes C-67 and C-68 co-residents of a single named audit
section, with the protocol section (C-66) preceding all role instructions as a first-class
structural artifact.

**Hypothesis:** V-04 satisfies C-66 and C-67 but not C-68. The missing element is audit
coverage for parenthetical presence. By appending PARENTHETICAL_PRESENCE_VERIFICATION
immediately after WRONG_SCHEMA_RESIDUAL_CHECK — both under a shared
`PHASE_0_CA_OUTPUT_AUDIT` heading — the two enforcement axes become mutually reinforcing:
WRONG_SCHEMA checks declaration format, parenthetical checks declaration completeness.
Together they form the complete Phase 6-A coverage of Phase 0-CA-1 output quality.
V-05 should satisfy all three new criteria simultaneously.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

## LIFECYCLE_PROTOCOL

Silent fallthrough is a structural violation.

Every role transition is a declared protocol event. The outgoing role MUST emit the token
below before its successor begins. The incoming role MUST open with the matching
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

A role that begins authoring without the incoming acknowledgment cited above is a
lifecycle gap finding, regardless of whether the outgoing token was present.

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

Close per Transition 1 outgoing: **HANDOFF_TO: TOPOLOGY ARCHITECT**

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open per Transition 2 incoming: **"Received PRE_FLIGHT_MANIFEST."**

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

Close per Transition 2 outgoing:
**"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open per Transition 3 incoming: **"Received Phase 0 from Topology Architect."**

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

Close per Transition 3 outgoing:
**"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open per Transition 4 incoming:
**"Received GATE_STATUS: [value]. Proceeding|Blocked."**
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
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION,
CONTRACT_GAP.

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

Close per Transition 4 outgoing:
**"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open per Transition 5 incoming:
**"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

**Phase 6-A — Gate Verification + Phase 0-CA-1 Output Audit**

Phase 6-A is structured in three sequential blocks:

**Block 1 — WRONG_SCHEMA Residual Check** (Axis Q: enforcement closure for C-64/C-67)

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

**Block 2 — Parenthetical Presence Verification** (Axis R: enforcement closure for C-65/C-68)

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
  PRE_FLIGHT_MANIFEST_STATUS was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  COLUMN_SCHEMA_COMPLETE was PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All DECLARATION_SCHEMA checks PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  All deltas empty before Phase 1: CONFIRMED|NOT_CONFIRMED
  All signatures present before Phase 1: CONFIRMED|NOT_CONFIRMED
  WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED
  PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED
  CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL

BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: PASS|FAIL
```

Close Phase 6-A per Transition 5 outgoing:
**"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

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

Open per Transition 5 incoming: **"Received AUDITOR_CERTIFICATION: COMPLETE."**

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
| C-66 (dedicated LIFECYCLE_PROTOCOL section, violation declaration at top, 5 labeled pairs) | TARGET | — | — | TARGET | TARGET |
| C-67 (Phase 6-A WRONG_SCHEMA_RESIDUAL_CHECK, unresolved = finding) | — | TARGET | — | TARGET | TARGET |
| C-68 (Phase 6-A PARENTHETICAL_PRESENCE_VERIFICATION, absent count = finding) | — | — | TARGET | — | TARGET |
| C-63 (5 HANDOFF_TO/Received transitions, all locked) | PASS | PASS | PASS | PASS | PASS |
| C-64 (SCHEMA_TYPE in manifest, WRONG_SCHEMA status) | PASS | PASS | PASS | PASS | PASS |
| C-65 (row-count parentheticals in CA output) | PASS | PASS | PASS | PASS | PASS |

**Key structural differences:**

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| LIFECYCLE_PROTOCOL as dedicated named section before role definitions | YES | NO | NO | YES | YES |
| "Silent fallthrough is a structural violation" at top of named section | YES | NO | NO | YES | YES |
| All 5 transitions as labeled HANDOFF_TO + Received pairs within section | YES | NO | NO | YES | YES |
| Phase 6-A WRONG_SCHEMA_RESIDUAL_CHECK table with finding generation | NO | YES | NO | YES | YES |
| Phase 6-A PARENTHETICAL_PRESENCE_VERIFICATION table with finding generation | NO | NO | YES | NO | YES |
| Both audit tables co-resident in Phase 6-A output audit block | NO | NO | NO | NO | YES |
| Phase 6-A Block 3 gate verification cites both WRONG_SCHEMA and parenthetical checks | NO | NO | NO | NO | YES |
