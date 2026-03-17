# Quest Variations — flow-conversation — Round 15 (v14 rubric)

**Date:** 2026-03-15 | **Rubric version:** v14 | **Max score:** 228

---

## Variation Axes Selected

All 5 variations carry the full v14 baseline: C-01 through C-62, plus the three
new criteria C-63 through C-65 each variation is explicitly designed to surface.
The baseline includes: PRE_FLIGHT_MANIFEST as Phase -1, COLUMN_SCHEMA_REGISTRY as
Phase 0-D-0 first artifact, universal FIELD|VALUE Phase 0-A declarations, all prior
handoff token language from R14 V-05 (GATE_STATUS, DEVELOPER_CERTIFICATION,
AUDITOR_CERTIFICATION tokens), nine defect classes, EXECUTION_HALT with CHAIN_BREAK_TRACE,
STATUS_QUO_SIMULATION (Phase 4-SQ), STATUS_QUO_COVERAGE (Phase 5-F), and REMEDIATION
PLANNER (Phase 7).

**New axes for R15 (targeting C-63, C-64, C-65):**

- **Axis L — Full lifecycle protocol closure (C-63 target)**: Tighten all 5 role
  boundary transitions to exact bidirectional HANDOFF_TO/Received token language.
  AUDITOR closes Phase 6-A specifically (not Phase 6 as a whole) with
  `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`. REMEDIATION PLANNER
  opens Phase 7 with exact token `"Received AUDITOR_CERTIFICATION: COMPLETE."`. Silent
  fallthrough at any boundary is a structural violation.

- **Axis M — Schema-typed manifest rows (C-64 target)**: PRE_FLIGHT_MANIFEST gains a
  SCHEMA_TYPE column. Rows for Phase 0-A-8/9/10/11 carry `SCHEMA_TYPE: FIELD|VALUE`.
  STATUS resolves to COMPLETE | MISSING | WRONG_SCHEMA. WRONG_SCHEMA applies when the
  declaration exists but uses prose or a non-FIELD|VALUE table format. MISSING applies
  only when the declaration is absent entirely. The manifest is the enforcement origin
  for schema type; the rubric is not.

- **Axis N — Row-count CA verification (C-65 target)**: DECLARATION_SCHEMA_COMPLETE
  in Phase 0-CA-1 carries parenthetical row counts for each of the four C-62-applicable
  declarations: `DECLARATION_NAME: PASS|FAIL (count N rows: [named breakdown])`.
  A FAIL with named missing fields is more informative than a binary FAIL. A PASS without
  a count does not satisfy C-65.

**Single-axis (3):** L, M, N

- **Axis L — Lifecycle protocol**: all 5 HANDOFF_TO/Received transitions locked
- **Axis M — Schema-typed manifest**: SCHEMA_TYPE column + WRONG_SCHEMA detection
- **Axis N — Row-count verification**: parenthetical row counts in CA output

**Combined (2):**

- **Axes L+M — Lifecycle + schema-typed manifest**: handoff protocol + manifest schema-type enforcement
- **Axes L+M+N — Full R15 combination**: all three axes + complete baseline

---

## V-01 — Axis L: Full Lifecycle Protocol Closure

**Variation axis:** Lifecycle emphasis — every role transition is an explicit bidirectional
protocol event. All 5 HANDOFF_TO/Received pairs locked; Phase 6-A closes with
`AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`; Phase 7 opens with
`"Received AUDITOR_CERTIFICATION: COMPLETE."`.

**Hypothesis:** R14 V-05 already locked most boundaries, but left two gaps: the Auditor
closed Phase 6 as a whole (not Phase 6-A specifically), and the Remediation Planner
opened with `"Received AUDITOR_CERTIFICATION."` without the `: COMPLETE` token suffix.
C-63 requires that the incoming acknowledgment cites the exact outgoing token. Making
Phase 6-A the specific close point forces the Auditor to commit at the gate boundary
rather than at the end of all Phase 6 sub-phases, and forces the RP to mirror the exact
token string. This eliminates the remaining two implicit adjacencies.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is an explicit bidirectional protocol event.
Silent fallthrough at any boundary is a structural violation. Each role issues an outgoing
handoff token and its successor opens with a matching incoming acknowledgment.

**Lifecycle protocol — 5 required transitions:**

```
Boundary 1: Phase -1 closes  → HANDOFF_TO: TOPOLOGY ARCHITECT
Boundary 2: Phase 0 closes   → HANDOFF_TO: CONTRACT AUDITOR
Boundary 3: Phase 0-CA-1     → GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER
Boundary 4: Phase 5 closes   → DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR
Boundary 5: Phase 6-A closes → AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER
```

Each outgoing token must be acknowledged by the receiving role before that role authors
any content. The acknowledgment cites the exact token string.

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** All structured Phase 0 declarations use FIELD|VALUE table
rows. Prose field descriptions do not satisfy the schema contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. The Topology Architect may not begin Phase 0-D-0 until this manifest
exists.

```
PRE_FLIGHT_MANIFEST (Phase -1):

REQUIRED_DECLARATION                          | PHASE_REF  | STATUS
----------------------------------------------|------------|--------
COLUMN_SCHEMA_REGISTRY                        | 0-D-0      | PENDING
Topic Registry                                | 0-D-1      | PENDING
Vocabulary Gate                               | 0-D-2      | PENDING
Session Variable Registry                     | 0-D-3      | PENDING
Invariant Register                            | 0-D-4      | PENDING
Transition Map                                | 0-D-5      | PENDING
Session Variable Timeline Contract            | 0-A-6      | PENDING
Invariant Chain Declaration                   | 0-A-7      | PENDING
Deviation Budget [FIELD|VALUE required]       | 0-A-8      | PENDING
Constraint Chain Budget [FIELD|VALUE required]| 0-A-9      | PENDING
Turn Prediction Contract [FIELD|VALUE required]| 0-A-10    | PENDING
Status Quo Method [FIELD|VALUE required]      | 0-A-11     | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
HANDOFF_TO: TOPOLOGY ARCHITECT
```

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST. Beginning Phase 0-D-0 authoring."**

**Phase 0-D-0 — Column Schema Registry (first artifact)**

Declare every column that will appear in the Phase 1 turn table.

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
Sign: VOCABULARY_GATE_SIGNED: YES.

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

**Phase 0-A-8 — Deviation Budget (FIELD|VALUE rows)**
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
FIELD                   | VALUE
------------------------|--------------------------------
PATH_ID                 | HP-01 | ALT-NN
PATH_DESCRIPTION        | [scenario narrative]
PATH_CRITICALITY        | CRITICAL|IMPORTANT|INFORMATIONAL
PREDICTED_TURN_SEQUENCE | [ordered TOPIC_ID list]
```
```
FIELD                           | VALUE
--------------------------------|------
TURN_PREDICTION_CONTRACT_SIGNED | YES
```
CRITICAL paths: PREDICTION_DEVIATION auto-elevates to P1 minimum severity.

**Phase 0-A-11 — Status Quo Method Declaration (FIELD|VALUE rows)**
```
FIELD                    | VALUE
-------------------------|----------------------------------------------------------
METHOD_NAME              | [short label]
METHOD_DESCRIPTION       | [one paragraph]
METHOD_COVERAGE          | [what the method checks]
BLIND_CONSTRAINT_VERDICTS| YES|NO
BLIND_CHAIN_EFFECTS      | YES|NO
BLIND_TIMELINE_ANOMALIES | YES|NO
BLIND_PREDICTION_CONTRACT| YES|NO
BLIND_CHAIN_BUDGET       | YES|NO
STATUS_QUO_METHOD_SIGNED | YES
```

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect. Resolving PRE_FLIGHT_MANIFEST."**

Update manifest to COMPLETE|MISSING for each row. Then compute all blocking checks:

```
PRE_FLIGHT_MANIFEST (resolved):

REQUIRED_DECLARATION                          | PHASE_REF  | STATUS
----------------------------------------------|------------|------------------------
COLUMN_SCHEMA_REGISTRY                        | 0-D-0      | COMPLETE|MISSING
Topic Registry                                | 0-D-1      | COMPLETE|MISSING
Vocabulary Gate                               | 0-D-2      | COMPLETE|MISSING
Session Variable Registry                     | 0-D-3      | COMPLETE|MISSING
Invariant Register                            | 0-D-4      | COMPLETE|MISSING
Transition Map                                | 0-D-5      | COMPLETE|MISSING
Session Variable Timeline Contract            | 0-A-6      | COMPLETE|MISSING
Invariant Chain Declaration                   | 0-A-7      | COMPLETE|MISSING
Deviation Budget [FIELD|VALUE required]       | 0-A-8      | COMPLETE|MISSING
Constraint Chain Budget [FIELD|VALUE required]| 0-A-9      | COMPLETE|MISSING
Turn Prediction Contract [FIELD|VALUE required]| 0-A-10    | COMPLETE|MISSING
Status Quo Method [FIELD|VALUE required]      | 0-A-11     | COMPLETE|MISSING

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
```

Then emit:
```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET: PASS|FAIL
    CONV_CHAIN_BUDGET: PASS|FAIL
    TURN_PREDICTION_CONTRACT: PASS|FAIL
    STATUS_QUO_METHOD: PASS|FAIL
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any manifest row MISSING, any DECLARATION_SCHEMA check fails,
COVERAGE_DELTA non-empty, CHAIN_BUDGET_DELTA non-empty, or any signature is NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
GATE_STATUS: FAIL blocks Phase 1. Any Phase 1 content following a received FAIL
is an unauthorized execution finding.

**Phase 1-S — Session Variable Mutation Log (author BEFORE Phase 1)**
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE cells in Phase 1 are derived by replaying Phase 1-S in turn order.
Each SESSION_STATE cell cites its Phase 1-S source row.

**Phase 1 — Turn-by-Turn Trace**
One row per turn; all columns from Phase 0-D-0. No turns skipped or collapsed.
No prohibited vocabulary. Inject at least one adversarial utterance; record injection
TURN_ID, system response, defect triggered (if any), recovery path.

**Phase 1-T — Topic Aggregate (additive)**
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
INVARIANT_CITE (CONV-NN) | REPRODUCTION_STEPS | RECOVERY (RECOVERABLE[min_turns,
target_state] | UNRECOVERABLE[reason]) | ENTANGLEMENT_VERDICT
```
CRITICAL-path PREDICTION_DEVIATION: add PLAN_TIER_OVERRIDE: IMMEDIATE.

For each FOUND P0 defect, emit before classifying lower-severity defects:
```
EXECUTION_HALT:
  HALT_TRIGGER: [defect class and topic/turn location]
  ROOT_CAUSE: [one-sentence causal statement]
  MVF_RECOMMENDATION: [smallest change eliminating the P0 condition]
  MVF_SCOPE: [topics/transitions/session variables the fix touches]
  UNBLOCKED_BY: [observable state change confirming fix applied]
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN: [CHAIN-NN]
    CHAIN_HEAD_CONV: [CONV-NN]
    FIRST_DEVIATE_TURN: [TURN_ID]
    SUSPENDED_CONVS: [list]
    BREAK_TO_DEFECT_PATH: [narrative]
  CHAIN_REPAIR: [CONV-NNs to re-evaluate after fix]
```

**Phase 3-E — Entanglement Map**
```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_CLASS]|MASKED_BY[DEFECT_CLASS]
```
MASKED_BY: conditional recovery RECOVERABLE[min_turns, target_state, requires_fix=DEFECT_CLASS].

**Phase 4 — Fallback, Escalation, Disambiguation**
Trace at least one fallback path to completion. Trace at least one escalation: trigger
condition, handoff node, session state at handoff, agent receipt confirmation. For each
intent collision: disambiguation strategy (entity enrichment, condition ordering, or
trigger phrase refactor) with rationale.

**Phase 4-SQ — Status Quo Simulation**
Re-run using ONLY STATUS_QUO_METHOD from Phase 0-A-11. No CONSTRAINT_VERDICTS,
CHAIN_EFFECTS, PREDICTION_MATCH, TIMELINE_ANOMALY, or CHAIN_BUDGET tracking.
```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO |
SQ_DEFECT_CLASS | REMARKS
```
Close with STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND (list),
SQ_DEFECTS_NOT_FOUND (populated after Phase 5-F comparison).

**Phase 5-A — Deviation Budget Utilization**
```
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
```
OVERALL_BUDGET_STATUS: WITHIN_BUDGET|EXCEEDED. If EXCEEDED: BUDGET_EXCEEDED_FINDING
with VIOLATED_CLASSES, OVER_BY per class, IMPLICATION.

**Phase 5-B — Chain Budget Utilization**
```
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
```
For each EXCEEDED chain: CHAIN_BUDGET_EXCEEDED finding (8th structural class).

**Phase 5-C — Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```
BROKEN chains cross-reference their EXECUTION_HALT block.

**Phase 5-D — Coverage Quality Gate + Five Ratios**
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (DEGRADED when TIMELINE_ANOMALY_RATE > 0).
Five ratios (PROVISIONAL under DEGRADED):
1. TOPIC_COVERAGE_RATIO = topics_visited / total_declared
2. TRANSITION_COVERAGE_RATIO = transitions_exercised / total_declared
3. SLOT_PATH_COVERAGE_RATIO = slot_paths_completed / total_slot_paths
4. TIMELINE_ANOMALY_RATE = timeline_anomalies_found / total_variable_turn_events
5. PATH_ADHERENCE_RATIO = turns_on_any_predicted_path / total_turns

**Phase 5-F — Status Quo Coverage Table**
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION | FOUND_BY_STATUS_QUO |
DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY|FOUND_BY_BOTH|FOUND_BY_STATUS_QUO_ONLY |
SQ_BLIND_SPOT
```
Auto-classification: PREDICTION_DEVIATION → FOUND_BY_SIMULATION_ONLY when
BLIND_PREDICTION_CONTRACT: YES; CHAIN_BUDGET_EXCEEDED when BLIND_CHAIN_BUDGET: YES;
TIMELINE_ANOMALY when BLIND_TIMELINE_ANOMALIES: YES.
Close with STATUS_QUO_GAP_SUMMARY.

Close Phase 5 with: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

The Auditor never modifies Developer rows. Discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Verify and emit:
- CONTRACT_AUDIT_GATE_HONORED: PRE_FLIGHT_MANIFEST_STATUS was PASS, COLUMN_SCHEMA_COMPLETE
  was PASS, DECLARATION_SCHEMA_COMPLETE was PASS for all four declarations, all deltas
  empty, all signatures present — all confirmed before Phase 1. PASS|FAIL.
- BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
- BUDGET_STATUS_CONSISTENT: PASS|FAIL
- SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category.

Close Phase 6-A with:
**"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

(Note: AUDITOR_CERTIFICATION for the overall audit is emitted at Phase 6-A close. The
sub-phases 6-B through 6-H findings feed Phase 7. If any sub-phase yields a blocking
finding, include it in the AUDITOR_CERTIFICATION citation: `AUDITOR_CERTIFICATION:
FAIL[cite blocking findings]. HANDOFF_TO: REPORT PRODUCER.`)

**Phase 6-B — Severity Co-Residency Audit**
Every FOUND defect row has both SEVERITY_CLASS and INVARIANT_CITE. Structured table;
prose does not satisfy. EXEMPT: CONFIRMED_ABSENT rows.

**Phase 6-C — Entanglement Consistency Audit**
Verify Phase 3-E ENTANGLEMENT_MAP against Phase 1 turn-level evidence.

**Phase 6-D — Topic Aggregate Consistency Audit**
Cross-check Phase 1-T CONFORMANCE_ROLLUP against DEVIATES count per topic in Phase 1.
TOPIC_ROLLUP_MISMATCH finding for any discrepancy.

**Phase 6-E — Session Timeline Consistency Audit**
Replay Phase 1-S mutations; compare reconstructed SESSION_STATE against Phase 1
SESSION_STATE column. TIMELINE_STATE_MISMATCH finding for any discrepancy.

**Phase 6-F — Fix Viability Audit**
Per EXECUTION_HALT: CONV_VIOLATIONS_INTRODUCED, CONV_VIOLATIONS_DETAIL,
VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[CONV-NN list], CHAIN_REPAIR_COMPLETE.

**Phase 6-G — Chain Integrity Audit**
Per CHAIN-NN: CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL.
CHAIN_VERDICT_INCONSISTENCY when downstream CONV-NN CONFORMs during a SUSPENDED window.

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

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE. Constructing REMEDIATION_PLAN."**

Read all EXECUTION_HALT blocks (Phase 2) and Phase 3-E ENTANGLEMENT_MAP.

For each FOUND defect, one PLAN_ITEM:
```
PLAN_ID: RP-NN
DEFECT_REF: [Phase 2 DEFECT_ID]
SEVERITY_CLASS: P0|P1|P2|P3
SCOPE: [topics/transitions/session variables]
DEPENDENCY_ON: [RP-NN list from ENABLES in Phase 3-E]
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG
TIER_RATIONALE: [P0→IMMEDIATE; PLAN_TIER_OVERRIDE for CRITICAL deviations; P1→NEXT_SPRINT; P2/P3→BACKLOG]
CHAIN_REPAIR_ITEMS: [CONV-NN list from EXECUTION_HALT CHAIN_REPAIR; empty if none]
UNBLOCKED_BY: [observable state confirming fix applied]
```

Topological sort: no PLAN_ITEM before any item in its DEPENDENCY_ON list.
PLAN_TIER_OVERRIDE: IMMEDIATE is second-priority after P0, before P1.

Close with:
```
PLAN_SUMMARY:
  PLAN_ITEM_COUNT: N
  IMMEDIATE_COUNT: N
  NEXT_SPRINT_COUNT: N
  BACKLOG_COUNT: N
  DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND[RP-NN cycle]
```
A trace with no FOUND defects satisfies Phase 7 with PLAN_ITEM_COUNT: 0.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-02 — Axis M: Schema-Typed Manifest Rows

**Variation axis:** Output format — PRE_FLIGHT_MANIFEST gains a SCHEMA_TYPE column.
Rows for Phase 0-A-8/9/10/11 declare `SCHEMA_TYPE: FIELD|VALUE`. At Phase 0-CA-1,
STATUS resolves to COMPLETE | MISSING | WRONG_SCHEMA. The manifest is the enforcement
origin; the rubric is not.

**Hypothesis:** R14 V-05 annotated manifest rows with `[FIELD|VALUE required]` in the
REQUIRED_DECLARATION label — an inline prose hint, not a structural field. C-64 requires
that SCHEMA_TYPE be a separate column with a machine-readable value, so that WRONG_SCHEMA
(declaration present but wrong format) becomes a distinct status from MISSING (declaration
absent). This distinction matters because WRONG_SCHEMA is a richer finding: the topology
architect produced something, but in the wrong encoding. A single SCHEMA_TYPE column
delivers this detection without changing any Phase 0-A authoring contract.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate: CONTRACT AUDITOR (Phase -1 + Phase 0-CA-1), TOPOLOGY ARCHITECT
(Phase 0), DEVELOPER (Phases 1–5), AUDITOR (Phase 6), REMEDIATION PLANNER (Phase 7).

**Universal format constraint:** All structured Phase 0 declarations with multiple fields
use FIELD|VALUE table rows. Prose field descriptions do not satisfy the schema contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. The Topology Architect may not begin Phase 0-D-0 until this manifest
exists.

The manifest carries a SCHEMA_TYPE column for rows where a specific encoding format is
contractually required. A declaration that is present but uses the wrong format resolves
to WRONG_SCHEMA at Phase 0-CA-1, not MISSING.

```
PRE_FLIGHT_MANIFEST (Phase -1):

REQUIRED_DECLARATION           | PHASE_REF | SCHEMA_TYPE  | STATUS
-------------------------------|-----------|--------------|--------
COLUMN_SCHEMA_REGISTRY         | 0-D-0     | —            | PENDING
Topic Registry                 | 0-D-1     | —            | PENDING
Vocabulary Gate                | 0-D-2     | —            | PENDING
Session Variable Registry      | 0-D-3     | —            | PENDING
Invariant Register             | 0-D-4     | —            | PENDING
Transition Map                 | 0-D-5     | —            | PENDING
Session Variable Timeline      | 0-A-6     | —            | PENDING
Invariant Chain Declaration    | 0-A-7     | —            | PENDING
Deviation Budget               | 0-A-8     | FIELD|VALUE  | PENDING
Constraint Chain Budget        | 0-A-9     | FIELD|VALUE  | PENDING
Turn Prediction Contract       | 0-A-10    | FIELD|VALUE  | PENDING
Status Quo Method Declaration  | 0-A-11    | FIELD|VALUE  | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
HANDOFF_TO: TOPOLOGY ARCHITECT
```

SCHEMA_TYPE: — rows: presence is sufficient; format is not contractually enforced by
the manifest. SCHEMA_TYPE: FIELD|VALUE rows: presence is necessary but not sufficient;
the declaration must use FIELD|VALUE table rows. If the declaration exists but uses prose
or a non-FIELD|VALUE format, STATUS resolves to WRONG_SCHEMA at Phase 0-CA-1.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST. Beginning Phase 0-D-0 authoring."**

**Phase 0-D-0 — Column Schema Registry (first artifact)**

Declare every column that will appear in the Phase 1 turn table.

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
Sign: VOCABULARY_GATE_SIGNED: YES.

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

**Phase 0-A-8 — Deviation Budget (FIELD|VALUE rows — manifest SCHEMA_TYPE: FIELD|VALUE)**
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
A prose paragraph describing budget thresholds results in STATUS: WRONG_SCHEMA at
Phase 0-CA-1 manifest resolution.

**Phase 0-A-9 — Constraint Chain Budget (FIELD|VALUE block per chain — SCHEMA_TYPE: FIELD|VALUE)**

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

**Phase 0-A-10 — Turn Prediction Contract (FIELD|VALUE block per path — SCHEMA_TYPE: FIELD|VALUE)**

HP-01 required; up to 3 ALT-NN:
```
FIELD                   | VALUE
------------------------|--------------------------------
PATH_ID                 | HP-01 | ALT-NN
PATH_DESCRIPTION        | [scenario narrative]
PATH_CRITICALITY        | CRITICAL|IMPORTANT|INFORMATIONAL
PREDICTED_TURN_SEQUENCE | [ordered TOPIC_ID list]
```
```
FIELD                           | VALUE
--------------------------------|------
TURN_PREDICTION_CONTRACT_SIGNED | YES
```

**Phase 0-A-11 — Status Quo Method Declaration (FIELD|VALUE rows — SCHEMA_TYPE: FIELD|VALUE)**
```
FIELD                    | VALUE
-------------------------|----------------------------------------------------------
METHOD_NAME              | [short label]
METHOD_DESCRIPTION       | [one paragraph]
METHOD_COVERAGE          | [what the method checks]
BLIND_CONSTRAINT_VERDICTS| YES|NO
BLIND_CHAIN_EFFECTS      | YES|NO
BLIND_TIMELINE_ANOMALIES | YES|NO
BLIND_PREDICTION_CONTRACT| YES|NO
BLIND_CHAIN_BUDGET       | YES|NO
STATUS_QUO_METHOD_SIGNED | YES
```

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect. Resolving PRE_FLIGHT_MANIFEST."**

Update manifest to COMPLETE | MISSING | WRONG_SCHEMA for each row. WRONG_SCHEMA applies
to SCHEMA_TYPE: FIELD|VALUE rows where the declaration is present but not in FIELD|VALUE
table format. MISSING applies only when the declaration is entirely absent.

```
PRE_FLIGHT_MANIFEST (resolved):

REQUIRED_DECLARATION           | PHASE_REF | SCHEMA_TYPE  | STATUS
-------------------------------|-----------|--------------|-------------------------
COLUMN_SCHEMA_REGISTRY         | 0-D-0     | —            | COMPLETE|MISSING
Topic Registry                 | 0-D-1     | —            | COMPLETE|MISSING
Vocabulary Gate                | 0-D-2     | —            | COMPLETE|MISSING
Session Variable Registry      | 0-D-3     | —            | COMPLETE|MISSING
Invariant Register             | 0-D-4     | —            | COMPLETE|MISSING
Transition Map                 | 0-D-5     | —            | COMPLETE|MISSING
Session Variable Timeline      | 0-A-6     | —            | COMPLETE|MISSING
Invariant Chain Declaration    | 0-A-7     | —            | COMPLETE|MISSING
Deviation Budget               | 0-A-8     | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Constraint Chain Budget        | 0-A-9     | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Turn Prediction Contract       | 0-A-10    | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Status Quo Method Declaration  | 0-A-11    | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL  (FAIL if any STATUS = MISSING or WRONG_SCHEMA)
```

Then emit:
```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET: PASS|FAIL
    CONV_CHAIN_BUDGET: PASS|FAIL
    TURN_PREDICTION_CONTRACT: PASS|FAIL
    STATUS_QUO_METHOD: PASS|FAIL
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any STATUS = MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, COVERAGE_DELTA non-empty, CHAIN_BUDGET_DELTA
non-empty, or any signature NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**

*(All phases identical to V-01: Phase 1-S, Phase 1, Phase 1-T, Phase 2 with EXECUTION_HALT
for P0 defects, Phase 3-E, Phase 4, Phase 4-SQ, Phase 5-A through 5-F.)*

Close Phase 5 with: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

Phase 6-A: CONTRACT_AUDIT_GATE_HONORED additionally verifies that no manifest row carried
WRONG_SCHEMA (any WRONG_SCHEMA row before Phase 1 is a protocol violation).

*(Phases 6-B through 6-H identical to V-01.)*

Close Phase 6-A with: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE. Constructing REMEDIATION_PLAN."**

*(PLAN_ITEMs and PLAN_SUMMARY identical to V-01.)*

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-03 — Axis N: Row-Count CA Verification

**Variation axis:** Output format — DECLARATION_SCHEMA_COMPLETE in Phase 0-CA-1 carries
parenthetical row counts for each of the four C-62-applicable declarations:
`DECLARATION_NAME: PASS|FAIL (count N rows: [named breakdown])`.

**Hypothesis:** R14 V-05 added a row count only for STATUS_QUO_METHOD: `(count 9 rows: 3
metadata + 5 BLIND + SIGNED)`. C-65 requires the same parenthetical for all four
declarations, with named field breakdowns. A binary PASS|FAIL without a count is
structurally ambiguous: the model may have checked for presence only, not completeness.
Requiring a count and naming the expected fields in the breakdown turns CA verification
into a self-documenting audit trail. A FAIL entry that names missing fields is more
actionable than one that does not. This axis adds the row-count format to all four entries
without changing the Phase 0-A authoring contract.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate: CONTRACT AUDITOR (Phase -1 + Phase 0-CA-1), TOPOLOGY ARCHITECT
(Phase 0), DEVELOPER (Phases 1–5), AUDITOR (Phase 6), REMEDIATION PLANNER (Phase 7).

**Universal format constraint:** All structured Phase 0 declarations use FIELD|VALUE table
rows. Prose field descriptions do not satisfy the schema contract.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST.

```
PRE_FLIGHT_MANIFEST (Phase -1):

REQUIRED_DECLARATION                          | PHASE_REF  | STATUS
----------------------------------------------|------------|--------
COLUMN_SCHEMA_REGISTRY                        | 0-D-0      | PENDING
Topic Registry                                | 0-D-1      | PENDING
Vocabulary Gate                               | 0-D-2      | PENDING
Session Variable Registry                     | 0-D-3      | PENDING
Invariant Register                            | 0-D-4      | PENDING
Transition Map                                | 0-D-5      | PENDING
Session Variable Timeline Contract            | 0-A-6      | PENDING
Invariant Chain Declaration                   | 0-A-7      | PENDING
Deviation Budget [FIELD|VALUE required]       | 0-A-8      | PENDING
Constraint Chain Budget [FIELD|VALUE required]| 0-A-9      | PENDING
Turn Prediction Contract [FIELD|VALUE required]| 0-A-10    | PENDING
Status Quo Method [FIELD|VALUE required]      | 0-A-11     | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
HANDOFF_TO: TOPOLOGY ARCHITECT
```

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST. Beginning Phase 0-D-0 authoring."**

*(Phase 0-D-0 through Phase 0-A-11 identical to V-01, including FIELD|VALUE format for
Phase 0-A-8/9/10/11.)*

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect. Resolving PRE_FLIGHT_MANIFEST."**

Update manifest rows to COMPLETE|MISSING. Then emit the full gate output. For each
C-62-applicable declaration, count actual FIELD|VALUE rows and name the expected fields
in the breakdown. A PASS entry without a row count does not satisfy the verification
contract. A FAIL entry must name which rows are missing.

```
PRE_FLIGHT_MANIFEST (resolved):
[update STATUS to COMPLETE|MISSING for each row — identical schema to Phase -1]
PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
```

```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET: PASS|FAIL (count N rows: P0_MAX, P1_MAX, P2_MAX, P3_MAX, RATIONALE, BUDGET_LOCK — expected 6)
    CONV_CHAIN_BUDGET: PASS|FAIL (count N rows per chain: CHAIN_ID, HEAD_CONV, CHAIN_LENGTH, CHAIN_BUDGET, RATIONALE — expected 5 per CHAIN-NN; [K] chains declared)
    TURN_PREDICTION_CONTRACT: PASS|FAIL (count N rows: [PATH_ID blocks: PATH_ID, PATH_DESCRIPTION, PATH_CRITICALITY, PREDICTED_TURN_SEQUENCE per path] + TURN_PREDICTION_CONTRACT_SIGNED — expected 4K+1 where K = path count)
    STATUS_QUO_METHOD: PASS|FAIL (count N rows: METHOD_NAME, METHOD_DESCRIPTION, METHOD_COVERAGE, BLIND_CONSTRAINT_VERDICTS, BLIND_CHAIN_EFFECTS, BLIND_TIMELINE_ANOMALIES, BLIND_PREDICTION_CONTRACT, BLIND_CHAIN_BUDGET, STATUS_QUO_METHOD_SIGNED — expected 9)
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

FAIL format for incomplete declarations:
`DECLARATION_NAME: FAIL (count N rows: found [list of found field names]; missing [list of absent field names])`

GATE_STATUS: FAIL if: any manifest row MISSING, COLUMN_SCHEMA_COMPLETE FAIL, any
DECLARATION_SCHEMA_COMPLETE FAIL, COVERAGE_DELTA non-empty, CHAIN_BUDGET_DELTA non-empty,
or any signature NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**

*(All phases identical to V-01.)*

Close Phase 5 with: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

Phase 6-A CONTRACT_AUDIT_GATE_HONORED additionally verifies that DECLARATION_SCHEMA_COMPLETE
entries included parenthetical row counts (absence of counts is itself a finding).

*(Phases 6-A through 6-H identical to V-01.)*

Close Phase 6-A with: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE. Constructing REMEDIATION_PLAN."**

*(PLAN_ITEMs and PLAN_SUMMARY identical to V-01.)*

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-04 — Axes L+M: Full Lifecycle Protocol + Schema-Typed Manifest

**Variation axes:** Lifecycle emphasis (Axis L) + Schema-typed manifest rows (Axis M).

**Hypothesis:** C-63 and C-64 target different layers of the same protocol spine: C-63
targets the transition tokens (what passes between roles), C-64 targets the manifest
schema (what the manifest knows about encoding contracts). Combining them means the
manifest itself carries the declaration type that drives WRONG_SCHEMA detection, and
every role transition that crosses a manifest-tracked boundary is explicitly acknowledged.
The combined prompt eliminates two independent ambiguity zones: a simulation that passes
C-63 without C-64 may still silently accept a prose-formatted Phase 0-A-8 declaration;
one that passes C-64 without C-63 may still have an implicit RP-start that doesn't cite
the Auditor's exact token.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is an explicit bidirectional protocol event.
Silent fallthrough is a structural violation.

**Lifecycle protocol — 5 required transitions:**
```
Boundary 1: Phase -1 closes  → HANDOFF_TO: TOPOLOGY ARCHITECT
Boundary 2: Phase 0 closes   → HANDOFF_TO: CONTRACT AUDITOR
Boundary 3: Phase 0-CA-1     → GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER
Boundary 4: Phase 5 closes   → DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR
Boundary 5: Phase 6-A closes → AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER
```

**Schema-type manifest enforcement:** PRE_FLIGHT_MANIFEST rows for Phase 0-A-8/9/10/11
carry `SCHEMA_TYPE: FIELD|VALUE`. At Phase 0-CA-1, these rows may resolve to COMPLETE,
MISSING, or WRONG_SCHEMA. The manifest is the enforcement origin for schema type.

**Universal format constraint:** All structured Phase 0 declarations use FIELD|VALUE
table rows. Prose field descriptions are structurally invisible.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. Topology Architect may not begin until manifest exists.

```
PRE_FLIGHT_MANIFEST (Phase -1):

REQUIRED_DECLARATION           | PHASE_REF | SCHEMA_TYPE  | STATUS
-------------------------------|-----------|--------------|--------
COLUMN_SCHEMA_REGISTRY         | 0-D-0     | —            | PENDING
Topic Registry                 | 0-D-1     | —            | PENDING
Vocabulary Gate                | 0-D-2     | —            | PENDING
Session Variable Registry      | 0-D-3     | —            | PENDING
Invariant Register             | 0-D-4     | —            | PENDING
Transition Map                 | 0-D-5     | —            | PENDING
Session Variable Timeline      | 0-A-6     | —            | PENDING
Invariant Chain Declaration    | 0-A-7     | —            | PENDING
Deviation Budget               | 0-A-8     | FIELD|VALUE  | PENDING
Constraint Chain Budget        | 0-A-9     | FIELD|VALUE  | PENDING
Turn Prediction Contract       | 0-A-10    | FIELD|VALUE  | PENDING
Status Quo Method Declaration  | 0-A-11    | FIELD|VALUE  | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
HANDOFF_TO: TOPOLOGY ARCHITECT
```

SCHEMA_TYPE: FIELD|VALUE rows: if declaration is present but not in FIELD|VALUE format,
STATUS resolves to WRONG_SCHEMA. MISSING is reserved for absent declarations only.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST. Beginning Phase 0-D-0 authoring."**

*(Phase 0-D-0 through Phase 0-A-11 identical to V-01, including FIELD|VALUE format for
Phase 0-A-8/9/10/11.)*

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect. Resolving PRE_FLIGHT_MANIFEST."**

Update manifest to COMPLETE | MISSING | WRONG_SCHEMA:

```
PRE_FLIGHT_MANIFEST (resolved):

REQUIRED_DECLARATION           | PHASE_REF | SCHEMA_TYPE  | STATUS
-------------------------------|-----------|--------------|-------------------------
COLUMN_SCHEMA_REGISTRY         | 0-D-0     | —            | COMPLETE|MISSING
Topic Registry                 | 0-D-1     | —            | COMPLETE|MISSING
Vocabulary Gate                | 0-D-2     | —            | COMPLETE|MISSING
Session Variable Registry      | 0-D-3     | —            | COMPLETE|MISSING
Invariant Register             | 0-D-4     | —            | COMPLETE|MISSING
Transition Map                 | 0-D-5     | —            | COMPLETE|MISSING
Session Variable Timeline      | 0-A-6     | —            | COMPLETE|MISSING
Invariant Chain Declaration    | 0-A-7     | —            | COMPLETE|MISSING
Deviation Budget               | 0-A-8     | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Constraint Chain Budget        | 0-A-9     | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Turn Prediction Contract       | 0-A-10    | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Status Quo Method Declaration  | 0-A-11    | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL  (FAIL if any STATUS = MISSING or WRONG_SCHEMA)
```

Then emit gate output:
```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET: PASS|FAIL
    CONV_CHAIN_BUDGET: PASS|FAIL
    TURN_PREDICTION_CONTRACT: PASS|FAIL
    STATUS_QUO_METHOD: PASS|FAIL
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any STATUS = MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, COVERAGE_DELTA non-empty, CHAIN_BUDGET_DELTA
non-empty, or any signature NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**

*(All phases identical to V-01.)*

Close Phase 5 with: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

Phase 6-A CONTRACT_AUDIT_GATE_HONORED verifies: PRE_FLIGHT_MANIFEST_STATUS was PASS
(no MISSING or WRONG_SCHEMA), COLUMN_SCHEMA_COMPLETE was PASS, DECLARATION_SCHEMA_COMPLETE
was PASS for all four declarations, all deltas empty, all signatures present — all
confirmed before Phase 1.

*(Phases 6-B through 6-H identical to V-01.)*

Close Phase 6-A with: **"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE. Constructing REMEDIATION_PLAN."**

*(PLAN_ITEMs and PLAN_SUMMARY identical to V-01.)*

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-05 — Axes L+M+N: Full Lifecycle + Schema-Typed Manifest + Row-Count Verification

**Variation axes:** Lifecycle protocol closure (Axis L) + Schema-typed manifest rows
(Axis M) + Row-count CA verification (Axis N) + full R14 baseline.

**Hypothesis:** C-63, C-64, and C-65 form three interlocking layers over the same
protocol structure. C-63 governs what crosses role boundaries. C-64 governs what the
manifest knows about encoding contracts for Phase 0-A declarations. C-65 governs how
deeply the Contract Auditor verifies those encoding contracts at gate time. A simulation
that passes C-63+C-64 but not C-65 still has an under-specified CA verification step
where row counts can be omitted. Combining all three layers produces a prompt where: no
role boundary is implicit (C-63), no schema-type declaration can be wrong-formatted
without a distinct manifest status (C-64), and no CA verification entry can omit its
row count (C-65). The prior three ambiguity zones are structurally closed.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is an explicit bidirectional protocol event.
Silent fallthrough is a structural violation. Each role issues an outgoing handoff token
and its successor opens with the exact matching incoming acknowledgment.

**Lifecycle protocol — 5 required transitions:**
```
Boundary 1: Phase -1 closes  → HANDOFF_TO: TOPOLOGY ARCHITECT
             TA opens        → "Received PRE_FLIGHT_MANIFEST."
Boundary 2: Phase 0 closes   → HANDOFF_TO: CONTRACT AUDITOR
             CA opens 0-CA-1 → "Received Phase 0 from Topology Architect."
Boundary 3: Phase 0-CA-1     → GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER
             Dev opens       → "Received GATE_STATUS: [value]. Proceeding|Blocked."
Boundary 4: Phase 5 closes   → DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR
             Aud opens       → "Received DEVELOPER_CERTIFICATION: COMPLETE."
Boundary 5: Phase 6-A closes → AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER
             RP opens        → "Received AUDITOR_CERTIFICATION: COMPLETE."
```

**Schema-type manifest enforcement:** PRE_FLIGHT_MANIFEST carries a SCHEMA_TYPE column
for rows 0-A-8/9/10/11. STATUS resolves to COMPLETE | MISSING | WRONG_SCHEMA. The
manifest is the enforcement origin; WRONG_SCHEMA is distinct from MISSING.

**Row-count CA verification:** DECLARATION_SCHEMA_COMPLETE entries carry parenthetical
row counts with named breakdowns. A PASS without a count does not satisfy the verification
contract. A FAIL must name absent fields.

**Universal format constraint:** All structured Phase 0 declarations use FIELD|VALUE table
rows. Prose field descriptions are structurally invisible.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. Topology Architect may not begin Phase 0-D-0 until manifest exists.

```
PRE_FLIGHT_MANIFEST (Phase -1):

REQUIRED_DECLARATION           | PHASE_REF | SCHEMA_TYPE  | STATUS
-------------------------------|-----------|--------------|--------
COLUMN_SCHEMA_REGISTRY         | 0-D-0     | —            | PENDING
Topic Registry                 | 0-D-1     | —            | PENDING
Vocabulary Gate                | 0-D-2     | —            | PENDING
Session Variable Registry      | 0-D-3     | —            | PENDING
Invariant Register             | 0-D-4     | —            | PENDING
Transition Map                 | 0-D-5     | —            | PENDING
Session Variable Timeline      | 0-A-6     | —            | PENDING
Invariant Chain Declaration    | 0-A-7     | —            | PENDING
Deviation Budget               | 0-A-8     | FIELD|VALUE  | PENDING
Constraint Chain Budget        | 0-A-9     | FIELD|VALUE  | PENDING
Turn Prediction Contract       | 0-A-10    | FIELD|VALUE  | PENDING
Status Quo Method Declaration  | 0-A-11    | FIELD|VALUE  | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
HANDOFF_TO: TOPOLOGY ARCHITECT
```

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0

Open with: **"Received PRE_FLIGHT_MANIFEST. Beginning Phase 0-D-0 authoring."**

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
Sign: VOCABULARY_GATE_SIGNED: YES.

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

**Phase 0-A-8 — Deviation Budget (FIELD|VALUE rows; manifest SCHEMA_TYPE: FIELD|VALUE)**
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

**Phase 0-A-9 — Constraint Chain Budget (FIELD|VALUE block per chain; SCHEMA_TYPE: FIELD|VALUE)**

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

**Phase 0-A-10 — Turn Prediction Contract (FIELD|VALUE block per path; SCHEMA_TYPE: FIELD|VALUE)**

HP-01 required; up to 3 ALT-NN:
```
FIELD                   | VALUE
------------------------|--------------------------------
PATH_ID                 | HP-01 | ALT-NN
PATH_DESCRIPTION        | [scenario narrative]
PATH_CRITICALITY        | CRITICAL|IMPORTANT|INFORMATIONAL
PREDICTED_TURN_SEQUENCE | [ordered TOPIC_ID list]
```
```
FIELD                           | VALUE
--------------------------------|------
TURN_PREDICTION_CONTRACT_SIGNED | YES
```
CRITICAL paths: PREDICTION_DEVIATION auto-elevates to P1 minimum severity.

**Phase 0-A-11 — Status Quo Method Declaration (FIELD|VALUE rows; SCHEMA_TYPE: FIELD|VALUE)**
```
FIELD                    | VALUE
-------------------------|----------------------------------------------------------
METHOD_NAME              | [short label]
METHOD_DESCRIPTION       | [one paragraph]
METHOD_COVERAGE          | [what the method checks]
BLIND_CONSTRAINT_VERDICTS| YES|NO
BLIND_CHAIN_EFFECTS      | YES|NO
BLIND_TIMELINE_ANOMALIES | YES|NO
BLIND_PREDICTION_CONTRACT| YES|NO
BLIND_CHAIN_BUDGET       | YES|NO
STATUS_QUO_METHOD_SIGNED | YES
```

Close with: **"Phase 0 authoring complete. HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1."**

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Open with: **"Received Phase 0 from Topology Architect. Resolving PRE_FLIGHT_MANIFEST."**

Update manifest to COMPLETE | MISSING | WRONG_SCHEMA. WRONG_SCHEMA applies to
SCHEMA_TYPE: FIELD|VALUE rows where the declaration is present but not in FIELD|VALUE
format. MISSING is reserved for absent declarations.

```
PRE_FLIGHT_MANIFEST (resolved):

REQUIRED_DECLARATION           | PHASE_REF | SCHEMA_TYPE  | STATUS
-------------------------------|-----------|--------------|-------------------------
COLUMN_SCHEMA_REGISTRY         | 0-D-0     | —            | COMPLETE|MISSING
Topic Registry                 | 0-D-1     | —            | COMPLETE|MISSING
Vocabulary Gate                | 0-D-2     | —            | COMPLETE|MISSING
Session Variable Registry      | 0-D-3     | —            | COMPLETE|MISSING
Invariant Register             | 0-D-4     | —            | COMPLETE|MISSING
Transition Map                 | 0-D-5     | —            | COMPLETE|MISSING
Session Variable Timeline      | 0-A-6     | —            | COMPLETE|MISSING
Invariant Chain Declaration    | 0-A-7     | —            | COMPLETE|MISSING
Deviation Budget               | 0-A-8     | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Constraint Chain Budget        | 0-A-9     | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Turn Prediction Contract       | 0-A-10    | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA
Status Quo Method Declaration  | 0-A-11    | FIELD|VALUE  | COMPLETE|MISSING|WRONG_SCHEMA

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL  (FAIL if any STATUS = MISSING or WRONG_SCHEMA)
```

Then emit gate output with full row-count parentheticals for all four C-62 declarations:

```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET: PASS|FAIL (count N rows: P0_MAX, P1_MAX, P2_MAX, P3_MAX, RATIONALE, BUDGET_LOCK — expected 6)
    CONV_CHAIN_BUDGET: PASS|FAIL (count N rows per chain: CHAIN_ID, HEAD_CONV, CHAIN_LENGTH, CHAIN_BUDGET, RATIONALE — expected 5 per CHAIN-NN; [K] chains declared)
    TURN_PREDICTION_CONTRACT: PASS|FAIL (count N rows: [PATH_ID, PATH_DESCRIPTION, PATH_CRITICALITY, PREDICTED_TURN_SEQUENCE per path] + TURN_PREDICTION_CONTRACT_SIGNED — expected 4K+1 where K = path count)
    STATUS_QUO_METHOD: PASS|FAIL (count N rows: METHOD_NAME, METHOD_DESCRIPTION, METHOD_COVERAGE, BLIND_CONSTRAINT_VERDICTS, BLIND_CHAIN_EFFECTS, BLIND_TIMELINE_ANOMALIES, BLIND_PREDICTION_CONTRACT, BLIND_CHAIN_BUDGET, STATUS_QUO_METHOD_SIGNED — expected 9)
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

FAIL format: `DECLARATION_NAME: FAIL (count N rows: found [named found fields]; missing [named absent fields])`

GATE_STATUS: FAIL if: any STATUS = MISSING or WRONG_SCHEMA, COLUMN_SCHEMA_COMPLETE FAIL,
any DECLARATION_SCHEMA_COMPLETE FAIL, COVERAGE_DELTA non-empty, CHAIN_BUDGET_DELTA
non-empty, or any signature NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
GATE_STATUS: FAIL blocks Phase 1. Phase 1 content following received FAIL is an
unauthorized execution finding.

**Phase 1-S — Session Variable Mutation Log (author BEFORE Phase 1)**
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE cells in Phase 1 are derived by replaying Phase 1-S. Each cell cites
its Phase 1-S source row.

**Phase 1 — Turn-by-Turn Trace**
One row per turn; all columns from Phase 0-D-0. No turns skipped. No prohibited
vocabulary. Inject at least one adversarial utterance; record TURN_ID, response,
defect triggered (if any), recovery.

**Phase 1-T — Topic Aggregate (additive)**
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
DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS | INVARIANT_CITE |
REPRODUCTION_STEPS | RECOVERY | ENTANGLEMENT_VERDICT
```
CRITICAL-path PREDICTION_DEVIATION: add PLAN_TIER_OVERRIDE: IMMEDIATE.

For each FOUND P0 defect, emit before classifying lower-severity defects:
```
EXECUTION_HALT:
  HALT_TRIGGER: [defect class and location]
  ROOT_CAUSE: [one-sentence causal statement]
  MVF_RECOMMENDATION: [smallest fix eliminating P0 condition]
  MVF_SCOPE: [topics/transitions/session variables]
  UNBLOCKED_BY: [observable state confirming fix applied]
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN: [CHAIN-NN]
    CHAIN_HEAD_CONV: [CONV-NN]
    FIRST_DEVIATE_TURN: [TURN_ID]
    SUSPENDED_CONVS: [list]
    BREAK_TO_DEFECT_PATH: [narrative]
  CHAIN_REPAIR: [CONV-NNs to re-evaluate after fix]
```

**Phase 3-E — Entanglement Map**
```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_CLASS]|MASKED_BY[DEFECT_CLASS]
```

**Phase 4 — Fallback, Escalation, Disambiguation**
Trace at least one fallback. Trace at least one escalation (trigger, handoff node,
session state, receipt). Per intent collision: disambiguation strategy + rationale.

**Phase 4-SQ — Status Quo Simulation**
ONLY STATUS_QUO_METHOD. No CONSTRAINT_VERDICTS, CHAIN_EFFECTS, PREDICTION_MATCH,
TIMELINE_ANOMALY, CHAIN_BUDGET tracking.
```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND | SQ_DEFECT_CLASS | REMARKS
```
STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND, SQ_DEFECTS_NOT_FOUND.

**Phase 5-A — Deviation Budget Utilization**
```
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
```
OVERALL_BUDGET_STATUS. If EXCEEDED: BUDGET_EXCEEDED_FINDING.

**Phase 5-B — Chain Budget Utilization**
```
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
```
CHAIN_BUDGET_EXCEEDED findings for exceeded chains.

**Phase 5-C — Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```

**Phase 5-D — Coverage Quality Gate + Five Ratios**
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED. Five ratios (PROVISIONAL under DEGRADED):
1. TOPIC_COVERAGE_RATIO = topics_visited / total_declared
2. TRANSITION_COVERAGE_RATIO = transitions_exercised / total_declared
3. SLOT_PATH_COVERAGE_RATIO = slot_paths_completed / total_slot_paths
4. TIMELINE_ANOMALY_RATE = timeline_anomalies_found / total_variable_turn_events
5. PATH_ADHERENCE_RATIO = turns_on_any_predicted_path / total_turns

**Phase 5-F — Status Quo Coverage Table**
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION | FOUND_BY_STATUS_QUO |
DETECTION_METHOD | SQ_BLIND_SPOT
```
Auto-classification from Phase 0-A-11 FIELD|VALUE rows.
Close with STATUS_QUO_GAP_SUMMARY.

Close Phase 5 with: **"DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR."**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

The Auditor never modifies Developer rows. Discrepancies are audit findings.

**Phase 6-A — Gate and Protocol Verification**

Verify and emit:
- CONTRACT_AUDIT_GATE_HONORED: PRE_FLIGHT_MANIFEST_STATUS was PASS (no MISSING or
  WRONG_SCHEMA), COLUMN_SCHEMA_COMPLETE was PASS, DECLARATION_SCHEMA_COMPLETE was PASS
  for all four declarations with row counts present, all deltas empty, all signatures
  present — all confirmed before Phase 1. Additionally verify that DECLARATION_SCHEMA_COMPLETE
  entries included parenthetical row counts (absence of counts is a protocol finding).
- BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
- BUDGET_STATUS_CONSISTENT: PASS|FAIL
- SIMULATION_DELTA_COMPLETE: every Phase 2 FOUND defect in exactly one detection category.

Close Phase 6-A with:
**"AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER."**

(If blocking findings: `AUDITOR_CERTIFICATION: FAIL[cite]. HANDOFF_TO: REPORT PRODUCER.`)

**Phase 6-B — Severity Co-Residency Audit**
Every FOUND defect row has both SEVERITY_CLASS and INVARIANT_CITE. Structured table.
EXEMPT: CONFIRMED_ABSENT rows.

**Phase 6-C — Entanglement Consistency Audit**
Phase 3-E ENTANGLEMENT_MAP vs Phase 1 turn-level evidence.

**Phase 6-D — Topic Aggregate Consistency Audit**
Phase 1-T CONFORMANCE_ROLLUP vs Phase 1 DEVIATES counts. TOPIC_ROLLUP_MISMATCH findings.

**Phase 6-E — Session Timeline Consistency Audit**
Phase 1-S replay vs Phase 1 SESSION_STATE. TIMELINE_STATE_MISMATCH findings.

**Phase 6-F — Fix Viability Audit**
Per EXECUTION_HALT: CONV_VIOLATIONS_INTRODUCED, CONV_VIOLATIONS_DETAIL,
VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[list], CHAIN_REPAIR_COMPLETE.

**Phase 6-G — Chain Integrity Audit**
Per CHAIN-NN: CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL.
CHAIN_VERDICT_INCONSISTENCY findings.

**Phase 6-H — Combined Plan / Path / Status Quo Audit**
*Plan:* EXECUTION_HALT_IN_PLAN, CHAIN_REPAIR_IN_SCOPE, DEPENDENCY_ORDER_VALID,
PLAN_INTEGRITY_AUDIT, DEPENDENCY_CYCLE_CHECK, PLAN_TIER_OVERRIDE_PRESENT, OVERRIDE_TIER_HONORED.
*Path:* per-turn PREDICTION_MATCH verified, PATH_ADHERENCE_RATIO_VERIFIED,
CRITICAL_PATH_ESCALATION_VERIFIED.
*Status quo:* DETECTION_METHOD verified per defect, AUTOMATIC_CLASSIFICATION_VERIFIED,
STATUS_QUO_COVERAGE_AUDIT.

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION: COMPLETE. Constructing REMEDIATION_PLAN."**

Read all EXECUTION_HALT blocks and Phase 3-E ENTANGLEMENT_MAP.

For each FOUND defect, one PLAN_ITEM:
```
PLAN_ID: RP-NN
DEFECT_REF: [Phase 2 DEFECT_ID]
SEVERITY_CLASS: P0|P1|P2|P3
SCOPE: [topics/transitions/session variables]
DEPENDENCY_ON: [RP-NN list from ENABLES in Phase 3-E]
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG
TIER_RATIONALE: [P0→IMMEDIATE; PLAN_TIER_OVERRIDE for CRITICAL deviations; P1→NEXT_SPRINT; P2/P3→BACKLOG]
CHAIN_REPAIR_ITEMS: [CONV-NN list from EXECUTION_HALT CHAIN_REPAIR; empty if none]
UNBLOCKED_BY: [observable state confirming fix applied]
```

Topological sort: no PLAN_ITEM before any item in DEPENDENCY_ON.
P0→IMMEDIATE, then PLAN_TIER_OVERRIDE: IMMEDIATE, then P1→NEXT_SPRINT, then P2/P3→BACKLOG.
Within tier: lower DEFECT_ID first.

Close with:
```
PLAN_SUMMARY:
  PLAN_ITEM_COUNT: N
  IMMEDIATE_COUNT: N
  NEXT_SPRINT_COUNT: N
  BACKLOG_COUNT: N
  DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND[RP-NN cycle]
```
A trace with no FOUND defects satisfies Phase 7 with PLAN_ITEM_COUNT: 0.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`
