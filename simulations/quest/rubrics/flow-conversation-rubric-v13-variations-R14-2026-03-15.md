# Quest Variations — flow-conversation — Round 14 (v13 rubric)

**Date:** 2026-03-15 | **Rubric version:** v13 | **Max score:** 222

---

## Variation Axes Selected

All 5 variations carry the full v13 baseline: C-01 through C-62. The baseline
includes mutation-first authoring, AUTHORIZED_REWRITERS, Contract Auditor gate
(COVERAGE_DELTA + CHAIN_BUDGET_DELTA + PREDICTION_CONTRACT + STATUS_QUO_METHOD),
EXECUTION_HALT blocks with CHAIN_BREAK_TRACE and CHAIN_REPAIR, PROPAGATION + CHAIN_ID,
CHAIN_EFFECTS column, DEVIATION_BUDGET, CHAIN_BUDGET, CHAIN_BUDGET_EXCEEDED as 8th
structural finding class, REMEDIATION PLANNER (Phase 7), TURN_PREDICTION_CONTRACT,
PREDICTION_DEVIATION as 9th defect class, PATH_ADHERENCE_RATIO, STATUS_QUO_METHOD
declaration, STATUS_QUO_SIMULATION (Phase 4-SQ), STATUS_QUO_COVERAGE table (Phase 5-F),
STATUS_QUO_COVERAGE_AUDIT (Phase 6-H), and all four new v13 criteria (C-59 through C-62).

**Single-axis (3):**

- **Axis I — Pre-flight manifest as Phase -1**: The CONTRACT AUDITOR emits a
  PRE_FLIGHT_MANIFEST (REQUIRED_DECLARATION | PHASE_REF | STATUS: PENDING) as the
  very first output of the simulation — before the TOPOLOGY ARCHITECT has authored a
  single Phase 0-A line. The manifest is numbered Phase -1 to make temporal priority
  unambiguous. At Phase 0-CA-1 the Auditor updates each row to COMPLETE|MISSING and
  emits GATE_STATUS: PASS|FAIL as a declared handoff token. The TOPOLOGY ARCHITECT
  may not begin Phase 0-A-1 until the manifest exists; DEVELOPER may not begin Phase 1
  until GATE_STATUS: PASS is received and explicitly acknowledged.

- **Axis J — Column schema as Phase 0-D-0 (first artifact)**: The TOPOLOGY ARCHITECT's
  first Phase 0 output is Phase 0-D-0 COLUMN_SCHEMA_REGISTRY — a COLUMN_NAME | FORMAT
  | ALLOWED_VALUES | REQUIRED_WHEN table declaring every column that will appear in the
  Phase 1 turn table. Phase 0-D-1 (topic registry) follows. The Contract Auditor
  verifies COLUMN_SCHEMA_COMPLETE: PASS|FAIL as its first sub-check in Phase 0-CA-1.
  A column appearing in Phase 1 without a Phase 0-D-0 row is a CONTRACT_GAP finding;
  a column declared in Phase 0-D-0 but missing from a Phase 1 turn row is a
  CONTRACT_GAP finding.

- **Axis K — Universal FIELD|VALUE Phase 0 language**: Every multi-field structured
  Phase 0-A declaration is encoded as a FIELD|VALUE table with no prose equivalents.
  Applicable declarations: STATUS_QUO_METHOD (each METHOD_BLIND_SPOTS dimension as
  a FIELD|YES|NO row), TURN_PREDICTION_CONTRACT (each PATH_ID as a FIELD|VALUE row
  block), DEVIATION_BUDGET (each SEVERITY|MAX row), CONV_CHAIN_BUDGET (each
  CHAIN_ID|BUDGET row). Prose descriptions of these fields are not schema rows and
  do not satisfy the declaration; the Contract Auditor verifies
  DECLARATION_SCHEMA_COMPLETE: PASS|FAIL for each C-62-applicable declaration.

**Combined (2):**

- **Axes I+J — Manifest-first + column schema as first artifact**: Phase -1
  PRE_FLIGHT_MANIFEST combined with Phase 0-D-0 COLUMN_SCHEMA_REGISTRY. The manifest
  lists the column schema registry as a required artifact; the topology architect must
  satisfy both before Phase 0-CA-1 updates the manifest. Handoff tokens carry the
  column schema gate result alongside COVERAGE_DELTA and other blocking conditions.

- **Axes I+J+K — Manifest + column schema + universal FIELD|VALUE + lifecycle
  emphasis**: All three axes combined with explicit handoff token language at every
  role boundary. Every role transition is a protocol event, not implicit adjacency:
  manifest → PENDING; phase 0-CA-1 → GATE_STATUS; developer opens phase 1 →
  "Received GATE_STATUS: [value]. Proceeding|Blocked."; developer closes phase 5 →
  DEVELOPER_CERTIFICATION: COMPLETE; auditor opens phase 6-A → "Received
  DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."

---

## V-01 — Axis I: Pre-Flight Manifest as Phase -1

**Variation axis:** Role sequence — PRE_FLIGHT_MANIFEST as a structurally prior
Phase -1, emitted by CONTRACT AUDITOR before any Topology Architect authoring.

**Hypothesis:** Numbering the manifest as Phase -1 makes temporal priority a hard
structural constraint rather than a prose instruction. The Topology Architect cannot
begin Phase 0-A-1 until Phase -1 exists; every Phase 0 artifact is authored against
a pending checklist. At Phase 0-CA-1 the manifest transitions from PENDING to
COMPLETE|MISSING, making the handoff token (GATE_STATUS) a downstream artifact of
the manifest rather than an independent assertion.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate: CONTRACT AUDITOR (Phase -1 + Phase 0-CA-1), TOPOLOGY ARCHITECT
(Phase 0-A), DEVELOPER (Phases 1–5), AUDITOR (Phase 6), REMEDIATION PLANNER (Phase 7).

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute Phase -1 before the Topology Architect authors any declaration. Emit the
PRE_FLIGHT_MANIFEST table:

```
PRE_FLIGHT_MANIFEST:

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
Deviation Budget                              | 0-A-8      | PENDING
Constraint Chain Budget                       | 0-A-9      | PENDING
Turn Prediction Contract                      | 0-A-10     | PENDING
Status Quo Method Declaration                 | 0-A-11     | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING — Topology Architect may now begin Phase 0-A authoring.
```

The Topology Architect authors all Phase 0-A sections against this manifest. The manifest
is the authoring checklist, not a post-hoc summary.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0-D and Phase 0-A declarations

Author all Phase 0 blocks in order. Every topic, variable, invariant, transition, chain,
and contract authored here is the pre-execution commitment; Phase 1–7 may not reference
anything undeclared.

**Phase 0-D-0 — Column Schema Registry**
Declare every column that will appear in the Phase 1 turn table.
```
COLUMN_NAME          | FORMAT                                    | ALLOWED_VALUES                                      | REQUIRED_WHEN
---------------------|-------------------------------------------|-----------------------------------------------------|--------------------
TURN_ID              | T-NN                                      | T-01, T-02, ...                                     | Every turn
USER_UTTERANCE       | free text                                 | any                                                 | Every turn
TOPIC_MATCHED        | TOPIC_ID from Phase 0-D-1                 | declared topics or CONTRACT_GAP                     | Every turn
NODES_EXECUTED       | comma-separated node names                | any                                                 | Every turn
AGENT_RESPONSE       | free text                                 | any                                                 | Every turn
TRANSITION_TARGET    | TOPIC_ID or TERMINAL                      | declared topics, TERMINAL, FALLBACK                 | Every turn
SESSION_STATE        | derived from Phase 1-S replay             | variable=value pairs                                | Every turn
CONFORMANCE          | CONFORMS or DEVIATES[CONV-NN]             | CONFORMS, DEVIATES[CONV-NN]                         | Every turn
CONSTRAINT_VERDICTS  | CONV-NN: PASS|FAIL|CHAIN_SUSPENDED list   | registered CONV-NNs only                            | Every turn
CHAIN_EFFECTS        | CONV-NN → [downstream: ACTIVATED|SUSPENDED] | per Phase 0-A-7 propagation                       | Every turn
PREDICTION_MATCH     | ON_PATH[PATH_ID] | DEVIATION[...] | OFF_ALL_PATHS | per Phase 0-A-10 contract                    | Every turn
SLOT_FILL_STATUS     | slot=FILLED|SKIPPED|INTERRUPTED           | FILLED, SKIPPED, INTERRUPTED                        | Slot-fill turns only
```

**Phase 0-D-1 — Topic Registry**
```
TOPIC_ID | TRIGGER_PHRASES | ENTRY_CONDITIONS | EXIT_TARGETS
```
A topic first encountered in Phase 1 that is absent here is a CONTRACT_GAP finding.

**Phase 0-D-2 — Vocabulary Gate**
```
TERM | CLASS: PERMITTED|PROHIBITED | RATIONALE
```
Sign: VOCABULARY_GATE_SIGNED: YES. Prohibited terms must not appear in Phase 1 trace
entries. Developer signs gate at Phase 0-D-2 close.

**Phase 0-D-3 — Session Variable Registry**
```
NAME | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL | INITIAL_VALUE
```

**Phase 0-D-4 — Invariant Register**
```
CONV-NN | DESCRIPTION | FALSIFICATION_CONDITION | PROPAGATION (downstream CONV-NNs) | CHAIN_ID
```

**Phase 0-D-5 — Transition Map**
```
TRANS-NN | SOURCE_TOPIC | TARGET_TOPIC | CONDITION | REQUIRED|OPTIONAL
```

**Phase 0-A-6 — Session Variable Timeline Contract**
```
VARIABLE | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED | AUTHORIZED_REWRITERS
```
Every variable from Phase 0-D-3 must have a row. A write from a topic absent from both
FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS is an OFF_CONTRACT_WRITE anomaly.

**Phase 0-A-7 — Invariant Chain Declaration**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | PROPAGATION_SEQUENCE (ordered CONV-NN list)
```

**Phase 0-A-8 — Deviation Budget**
```
SEVERITY | MAX_DEVIATES_ALLOWED | BUDGET_RATIONALE
```
Lock declaration: "BUDGET LOCKED — may not be revised after Phase 1-S begins."
P0_MAX = 0 means any FOUND P0 defect is a BUDGET_EXCEEDED finding.

**Phase 0-A-9 — Constraint Chain Budget**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | CHAIN_BUDGET | BUDGET_RATIONALE
```
Every CHAIN-NN from Phase 0-A-7 must have a row.

**Phase 0-A-10 — Turn Prediction Contract**
```
PATH_ID | PATH_DESCRIPTION | PATH_CRITICALITY: CRITICAL|IMPORTANT|INFORMATIONAL | PREDICTED_TURN_SEQUENCE
```
One HP-01 row required; up to 3 ALT-NN rows. Sign: TURN_PREDICTION_CONTRACT_SIGNED: YES.
CRITICAL paths mark core business transactions; PREDICTION_DEVIATION on a CRITICAL path
auto-elevates to P1 minimum severity.

**Phase 0-A-11 — Status Quo Method Declaration**
```
FIELD                    | VALUE
-------------------------|------------------------------------------------------
METHOD_NAME              | [short label]
METHOD_DESCRIPTION       | [one paragraph]
METHOD_COVERAGE          | [what artifacts/paths the method naturally checks]
BLIND_CONSTRAINT_VERDICTS| YES|NO  (does the method check per-invariant verdicts?)
BLIND_CHAIN_EFFECTS      | YES|NO  (does the method trace constraint propagation?)
BLIND_TIMELINE_ANOMALIES | YES|NO  (does the method check variable lifecycle ordering?)
BLIND_PREDICTION_CONTRACT| YES|NO  (does the method check against declared paths?)
BLIND_CHAIN_BUDGET       | YES|NO  (does the method check per-chain deviation thresholds?)
```
Sign: STATUS_QUO_METHOD_SIGNED: YES.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1 (Manifest resolution + gate)

Update the PRE_FLIGHT_MANIFEST to COMPLETE|MISSING for each row. Then compute all
blocking deltas:

```
PRE_FLIGHT_MANIFEST (updated):

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
Deviation Budget                              | 0-A-8      | COMPLETE|MISSING
Constraint Chain Budget                       | 0-A-9      | COMPLETE|MISSING
Turn Prediction Contract                      | 0-A-10     | COMPLETE|MISSING
Status Quo Method Declaration                 | 0-A-11     | COMPLETE|MISSING

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL  (FAIL if any STATUS = MISSING)
```

Then compute:
- COVERAGE_DELTA: VARS_IN_TOPOLOGY − VARS_IN_CONTRACT (non-empty = CONTRACT_COMPLETENESS_FAILURE)
- CHAIN_BUDGET_DELTA: CHAINS_IN_TOPOLOGY − CHAINS_IN_BUDGET (non-empty blocks execution)
- COLUMN_SCHEMA_COMPLETE: PASS|FAIL (every Phase 1 column has a Phase 0-D-0 row)
- DECLARATION_SCHEMA_COMPLETE: PASS|FAIL (each C-62-applicable declaration uses FIELD|VALUE rows)
- PREDICTION_CONTRACT_SIGNED: YES|NO
- STATUS_QUO_METHOD_SIGNED: YES|NO

Emit:
```
Phase 0-CA-1:
  PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  DECLARATION_SCHEMA_COMPLETE: PASS|FAIL
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

A non-empty MISSING count, non-empty COVERAGE_DELTA, non-empty CHAIN_BUDGET_DELTA,
COLUMN_SCHEMA_COMPLETE: FAIL, DECLARATION_SCHEMA_COMPLETE: FAIL, or any missing
signature produces GATE_STATUS: FAIL, which blocks Phase 1.

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open Phase 1 with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
A FAIL gate status blocks Phase 1; any Phase 1 content following a received
GATE_STATUS: FAIL is an unauthorized execution finding.

**Phase 1-S — Session Variable Mutation Log (author before Phase 1)**
Author Phase 1-S BEFORE Phase 1 SESSION_STATE. For each turn, for each non-null variable:
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE in Phase 1 is derived by replaying Phase 1-S mutations in turn order.
Each SESSION_STATE cell cites its Phase 1-S source entry. Do not independently author
SESSION_STATE.

**Phase 1 — Turn-by-Turn Trace**
Emit one row per turn using the schema from Phase 0-D-0. No turns may be skipped or
collapsed. Prohibited vocabulary from Phase 0-D-2 must not appear. CHAIN_SUSPENDED
verdicts in CONSTRAINT_VERDICTS cite the chain head:
`CONV-NN: CHAIN_SUSPENDED [chain head: CONV-NN broke at TURN_ID]`.

**Phase 1-T — Topic Aggregate (additive)**
```
TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ |
DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP | PATH_IDS_MATCHED
```

**Phase 2 — Defect Classification**
Classify in severity order. Nine defect classes: DEAD_END, INFINITE_LOOP,
INTENT_COLLISION, MISSING_FALLBACK, ORPHANED_TOPIC, TIMELINE_ANOMALY,
CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP.

For each FOUND defect:
```
DEFECT_ID | DEFECT_CLASS | LOCATION (topic/turn) | SEVERITY_CLASS: P0|P1|P2|P3 |
INVARIANT_CITE (CONV-NN) | REPRODUCTION_STEPS | RECOVERY (RECOVERABLE[min_turns, target_state]
| UNRECOVERABLE[reason]) | ENTANGLEMENT_VERDICT (placeholder for Phase 3-E)
```

CRITICAL-path PREDICTION_DEVIATION defects additionally carry:
`PLAN_TIER_OVERRIDE: IMMEDIATE` with annotation "CRITICAL path deviation — overrides
severity-based tier."

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
MASKED_BY defects carry conditional recovery verdicts: RECOVERABLE[min_turns,
target_state, requires_fix=DEFECT_CLASS].

**Phase 4 — Fallback, Escalation, Disambiguation**
Inject at least one adversarial utterance mid-conversation (Phase 6 also verifies this).
Trace at least one fallback path to completion. Trace at least one escalation path:
trigger condition, handoff node, session state at handoff, agent receipt confirmation.
For each intent collision found in Phase 2, propose a disambiguation strategy with
rationale (entity enrichment, condition ordering, or trigger phrase refactor).

**Phase 4-SQ — Status Quo Simulation**
Re-run the same scenario using ONLY the declared STATUS_QUO_METHOD from Phase 0-A-11.
Apply no CONSTRAINT_VERDICTS, no CHAIN_EFFECTS, no PREDICTION_MATCH, no TIMELINE_ANOMALY
tracking, no CHAIN_BUDGET tracking.
```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO |
SQ_DEFECT_CLASS | REMARKS
```
Close with STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND (list),
SQ_DEFECTS_NOT_FOUND (populated after Phase 5-F comparison).

**Phase 5 — Coverage and Quality**

*Phase 5-A — Deviation Budget Utilization*
```
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
```
OVERALL_BUDGET_STATUS: WITHIN_BUDGET|EXCEEDED[violated classes].
If EXCEEDED: BUDGET_EXCEEDED_FINDING with VIOLATED_CLASSES, OVER_BY per class, IMPLICATION.

*Phase 5-B — Chain Budget Utilization*
```
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
```
For each EXCEEDED chain: CHAIN_BUDGET_EXCEEDED finding (8th structural finding class).
CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY in SIMULATION_DELTA by
definition.

*Phase 5-C — Constraint Chain Status Summary*
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```
BROKEN chains cross-reference their EXECUTION_HALT block.

*Phase 5-D — Coverage Quality Gate*
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (DEGRADED when TIMELINE_ANOMALY_RATE > 0).
Under DEGRADED, all ratios carry PROVISIONAL. Report five ratios:
1. TOPIC_COVERAGE_RATIO = topics_visited / total_declared [numerator/denominator visible]
2. TRANSITION_COVERAGE_RATIO = transitions_exercised / total_declared
3. SLOT_PATH_COVERAGE_RATIO = slot_paths_completed / total_slot_paths
4. TIMELINE_ANOMALY_RATE = timeline_anomalies_found / total_variable_turn_events
5. PATH_ADHERENCE_RATIO = turns_on_any_predicted_path / total_turns

Orphaned topics are ORPHAN defects and appear in the denominator.

*Phase 5-F — Status Quo Coverage Table*
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION | FOUND_BY_STATUS_QUO |
DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY|FOUND_BY_BOTH|FOUND_BY_STATUS_QUO_ONLY |
SQ_BLIND_SPOT
```
Auto-classification: PREDICTION_DEVIATION → FOUND_BY_SIMULATION_ONLY when
BLIND_PREDICTION_CONTRACT: NO; CHAIN_BUDGET_EXCEEDED when BLIND_CHAIN_BUDGET: NO;
TIMELINE_ANOMALY when BLIND_TIMELINE_ANOMALIES: NO.

Close with STATUS_QUO_GAP_SUMMARY: FOUND_BY_SIMULATION_ONLY_COUNT,
FOUND_BY_SIMULATION_ONLY_LIST, STRUCTURAL_BLIND_SPOTS_ACTIVATED,
STATUS_QUO_GAP_NARRATIVE (one paragraph on what the informal method cannot see).

Close Phase 5 with: **DEVELOPER_CERTIFICATION: COMPLETE**

---

### ROLE 4 — AUDITOR: Phase 6 independent verification

Open Phase 6-A with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent
audit."** The Auditor never modifies Developer rows; discrepancies are audit findings.

**Phase 6-A:** CONTRACT_AUDIT_GATE_HONORED (PRE_FLIGHT_MANIFEST_STATUS: PASS and all
deltas empty before Phase 1). BUDGET_UTILIZATION_VERIFIED. BUDGET_STATUS_CONSISTENT.
SIMULATION_DELTA_COMPLETE (every Phase 2 FOUND defect in exactly one detection category).

**Phase 6-B — Severity Co-Residency Audit:**
Every FOUND defect row has both SEVERITY_CLASS and INVARIANT_CITE. Structured table;
prose does not satisfy. EXEMPT: CONFIRMED_ABSENT rows.

**Phase 6-C — Entanglement Consistency Audit:**
Verify Phase 3-E ENTANGLEMENT_MAP against Phase 1 turn-level evidence.

**Phase 6-D — Topic Aggregate Consistency Audit:**
Cross-check Phase 1-T CONFORMANCE_ROLLUP against DEVIATES count per topic from Phase 1.
TOPIC_ROLLUP_MISMATCH finding for any discrepancy.

**Phase 6-E — Session Timeline Consistency Audit:**
Replay Phase 1-S mutations in sequence; compare reconstructed SESSION_STATE against
Phase 1 SESSION_STATE column. TIMELINE_STATE_MISMATCH finding for any discrepancy.

**Phase 6-F — Fix Viability Audit:**
For each EXECUTION_HALT block: CONV_VIOLATIONS_INTRODUCED: YES|NO,
CONV_VIOLATIONS_DETAIL, VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[CONV-NN list].
CHAIN_REPAIR_COMPLETE: YES|NO.

**Phase 6-G — Chain Integrity Audit:**
Per CHAIN-NN: CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL.
CHAIN_VERDICT_INCONSISTENCY when a downstream CONV-NN CONFORMs during a SUSPENDED window.

**Phase 6-H — Combined Plan Integrity / Path Adherence / Status Quo Coverage Audit:**

*Plan Integrity:* EXECUTION_HALT_IN_PLAN: YES|NO; CHAIN_REPAIR_IN_SCOPE: YES|NO per
EXECUTION_HALT. DEPENDENCY_ORDER_VALID: YES|NO per PLAN_ITEM. PLAN_INTEGRITY_AUDIT:
PASS|FAIL. DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND. PLAN_TIER_OVERRIDE_PRESENT:
PASS|FAIL. OVERRIDE_TIER_HONORED: PASS|FAIL.

*Path Adherence:* Per-turn: PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED |
CONSISTENT: PASS|FAIL. PATH_ADHERENCE_RATIO_VERIFIED: PASS|FAIL.
CRITICAL_PATH_ESCALATION_VERIFIED: PASS|FAIL.

*Status Quo Coverage:* Per defect: DETECTION_METHOD_REPORTED | DETECTION_METHOD_AUDITED
| CONSISTENT: PASS|FAIL. AUTOMATIC_CLASSIFICATION_VERIFIED (PREDICTION_DEVIATION,
CHAIN_BUDGET_EXCEEDED, TIMELINE_ANOMALY each: PASS|FAIL).
STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL.

Close with AUDITOR_CERTIFICATION: PASS|FAIL[cite blocking findings].

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Execute after AUDITOR_CERTIFICATION. Read all EXECUTION_HALT blocks (Phase 2) and the
Phase 3-E ENTANGLEMENT_MAP.

For each FOUND defect emit one PLAN_ITEM:
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

## V-02 — Axis J: Column Schema as Phase 0-D-0 (First Artifact)

**Variation axis:** Output format — COLUMN_SCHEMA_REGISTRY is the first Phase 0 artifact,
sequenced before the topic registry, committing to the Phase 1 table structure before
any content declarations begin.

**Hypothesis:** When the column schema declaration precedes the topic registry, the
Contract Auditor can gate on COLUMN_SCHEMA_COMPLETE as its first check — before evaluating
any content contract. A column that appears in Phase 1 without a Phase 0-D-0 row is
structurally unenforceable; placing the column schema first makes every derived column a
first-class pre-execution commitment rather than an implied byproduct of phase instructions.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate: CONTRACT AUDITOR (Phase 0-CA-1), TOPOLOGY ARCHITECT (Phase 0),
DEVELOPER (Phases 1–5), AUDITOR (Phase 6), REMEDIATION PLANNER (Phase 7).

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0 declarations

Author all Phase 0 blocks. The COLUMN_SCHEMA_REGISTRY (Phase 0-D-0) is the first artifact.
Nothing in Phase 1 may reference a column not declared here.

**Phase 0-D-0 — Column Schema Registry (FIRST ARTIFACT)**

Declare every column that will appear in the Phase 1 turn table before authoring any
other Phase 0 block. The schema row format:
```
COLUMN_NAME | FORMAT | ALLOWED_VALUES | REQUIRED_WHEN
```

Required column declarations (extend as needed for any additional non-core columns):

| COLUMN_NAME         | FORMAT                                          | ALLOWED_VALUES                                                     | REQUIRED_WHEN       |
|---------------------|-------------------------------------------------|--------------------------------------------------------------------|---------------------|
| TURN_ID             | T-NN                                            | T-01, T-02, ...                                                    | Every turn          |
| USER_UTTERANCE      | free text                                       | any                                                                | Every turn          |
| TOPIC_MATCHED       | TOPIC_ID                                        | declared Phase 0-D-1 topics, or CONTRACT_GAP                       | Every turn          |
| NODES_EXECUTED      | comma-separated                                 | any node names                                                     | Every turn          |
| AGENT_RESPONSE      | free text                                       | any                                                                | Every turn          |
| TRANSITION_TARGET   | TOPIC_ID or terminal state                      | declared topics, TERMINAL, FALLBACK                                | Every turn          |
| SESSION_STATE       | derived from Phase 1-S replay                   | variable=value pairs                                               | Every turn          |
| CONFORMANCE         | CONFORMS or DEVIATES[CONV-NN]                   | CONFORMS, DEVIATES[CONV-NN]                                        | Every turn          |
| CONSTRAINT_VERDICTS | list of CONV-NN evaluations                     | PASS, FAIL, CHAIN_SUSPENDED[chain head: CONV-NN broke at TURN_ID]  | Every turn          |
| CHAIN_EFFECTS       | CONV-NN → [downstream: ACTIVATED\|SUSPENDED]   | per Phase 0-A-7 propagation structure                              | Every turn          |
| PREDICTION_MATCH    | ON_PATH, DEVIATION, or OFF_ALL_PATHS            | ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual], OFF_ALL_PATHS | Every turn       |
| SLOT_FILL_STATUS    | slot=RESULT                                     | FILLED, SKIPPED, INTERRUPTED                                       | Slot-fill turns only|

The Contract Auditor verifies COLUMN_SCHEMA_COMPLETE: PASS|FAIL at Phase 0-CA-1.
A column appearing in Phase 1 without a Phase 0-D-0 row is a CONTRACT_GAP finding.
A Phase 1 turn row missing a schema-declared REQUIRED_WHEN: Every turn column is a
CONTRACT_GAP finding.

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

**Phase 0-A-8 — Deviation Budget**
```
SEVERITY | MAX_DEVIATES_ALLOWED | BUDGET_RATIONALE
```
Lock: "BUDGET LOCKED — may not be revised after Phase 1-S begins."

**Phase 0-A-9 — Constraint Chain Budget**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | CHAIN_BUDGET | BUDGET_RATIONALE
```

**Phase 0-A-10 — Turn Prediction Contract**
```
PATH_ID | PATH_DESCRIPTION | PATH_CRITICALITY | PREDICTED_TURN_SEQUENCE
```
Sign: TURN_PREDICTION_CONTRACT_SIGNED: YES.

**Phase 0-A-11 — Status Quo Method Declaration**
```
FIELD                    | VALUE
-------------------------|----------------------------------------------------------
METHOD_NAME              | [label]
METHOD_DESCRIPTION       | [paragraph]
METHOD_COVERAGE          | [artifacts/paths the method checks]
BLIND_CONSTRAINT_VERDICTS| YES|NO
BLIND_CHAIN_EFFECTS      | YES|NO
BLIND_TIMELINE_ANOMALIES | YES|NO
BLIND_PREDICTION_CONTRACT| YES|NO
BLIND_CHAIN_BUDGET       | YES|NO
```
Sign: STATUS_QUO_METHOD_SIGNED: YES.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

Verify in this order:
1. COLUMN_SCHEMA_COMPLETE: PASS|FAIL (every Phase 1 column has a Phase 0-D-0 row with all four fields)
2. COVERAGE_DELTA: VARS_IN_TOPOLOGY − VARS_IN_CONTRACT (non-empty = CONTRACT_COMPLETENESS_FAILURE)
3. CHAIN_BUDGET_DELTA: CHAINS_IN_TOPOLOGY − CHAINS_IN_BUDGET
4. DECLARATION_SCHEMA_COMPLETE per C-62-applicable declaration:
   - STATUS_QUO_METHOD: PASS|FAIL (each METHOD_BLIND_SPOTS dimension is a FIELD|VALUE row)
   - TURN_PREDICTION_CONTRACT: PASS|FAIL
   - DEVIATION_BUDGET: PASS|FAIL
   - CONV_CHAIN_BUDGET: PASS|FAIL
5. PREDICTION_CONTRACT_SIGNED: YES|NO
6. STATUS_QUO_METHOD_SIGNED: YES|NO

Emit:
```
Phase 0-CA-1:
  COLUMN_SCHEMA_COMPLETE: PASS|FAIL
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  DECLARATION_SCHEMA_COMPLETE:
    STATUS_QUO_METHOD: PASS|FAIL
    TURN_PREDICTION_CONTRACT: PASS|FAIL
    DEVIATION_BUDGET: PASS|FAIL
    CONV_CHAIN_BUDGET: PASS|FAIL
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

CONTRACT_AUDIT_GATE_HONORED requires COLUMN_SCHEMA_COMPLETE: PASS alongside all other
empty-delta conditions.

---

### ROLE 3 — DEVELOPER: Phases 1–5

**Phase 1-S — Session Variable Mutation Log (author first)**
Author before Phase 1 SESSION_STATE. Each SESSION_STATE cell cites its Phase 1-S source.
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```

**Phase 1 — Turn-by-Turn Trace**
Emit one row per turn using the schema from Phase 0-D-0. No turns skipped. No prohibited
vocabulary. Adversarial utterance injected at least once: record TURN_ID, system response,
defect triggered (if any), and recovery path to completion.

**Phase 1-T — Topic Aggregate (additive to Phase 1)**
```
TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ |
DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP | PATH_IDS_MATCHED
```

**Phase 2 — Defect Classification**
Nine defect classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION,
CONTRACT_GAP.

For each FOUND defect: DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS | INVARIANT_CITE
| REPRODUCTION_STEPS | RECOVERY | ENTANGLEMENT_VERDICT.

CRITICAL-path PREDICTION_DEVIATION: PLAN_TIER_OVERRIDE: IMMEDIATE.

P0 defects: emit EXECUTION_HALT block (HALT_TRIGGER, ROOT_CAUSE, MVF_RECOMMENDATION,
MVF_SCOPE, UNBLOCKED_BY, CHAIN_BREAK_TRACE, CHAIN_REPAIR) before classifying
lower-severity defects.

**Phase 3-E — Entanglement Map**
```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_CLASS]|MASKED_BY[DEFECT_CLASS]
```

**Phase 4** — Fallback trace, escalation trace, disambiguation proposals.

**Phase 4-SQ — Status Quo Simulation** — Abbreviated trace using STATUS_QUO_METHOD only.

**Phase 5** — Deviation Budget Utilization (5-A), Chain Budget Utilization (5-B),
Constraint Chain Status Summary (5-C), Coverage Quality Gate + five ratios (5-D),
Status Quo Coverage Table (5-F). Close with DEVELOPER_CERTIFICATION: COMPLETE.

---

### ROLE 4 — AUDITOR: Phase 6

Phases 6-A through 6-H as specified in V-01. Opens with "Received DEVELOPER_CERTIFICATION:
COMPLETE. Beginning independent audit." Phase 6-A additionally verifies
COLUMN_SCHEMA_COMPLETE: PASS was present in Phase 0-CA-1.

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Topologically sorted PLAN_ITEMs after AUDITOR_CERTIFICATION. PLAN_SUMMARY closes Phase 7.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-03 — Axis K: Universal FIELD|VALUE Phase 0 Language

**Variation axis:** Phrasing register — every multi-field Phase 0-A declaration uses
FIELD|VALUE table rows exclusively; prose declarations of structured fields are
prohibited.

**Hypothesis:** Making FIELD|VALUE the universal language for Phase 0 declarations
eliminates the ambiguity between "field described in prose" and "field declared as a
schema row." The Contract Auditor can verify DECLARATION_SCHEMA_COMPLETE by counting
rows rather than parsing prose, making missing fields structurally visible. This targets
C-62 at maximum enforcement depth without requiring a pre-flight manifest.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles: CONTRACT AUDITOR (Phase 0-CA-1), TOPOLOGY ARCHITECT (Phase 0), DEVELOPER
(Phases 1–5), AUDITOR (Phase 6), REMEDIATION PLANNER (Phase 7).

**Protocol constraint:** All structured Phase 0 declarations must use FIELD|VALUE table
rows. A declaration expressed as prose does not satisfy the schema contract, even if all
field values are present in the prose. The Contract Auditor counts rows, not prose
sentences.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0 declarations

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
NAME | PERSISTENCE_CLASS | INITIAL_VALUE
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

**Phase 0-A-7 — Invariant Chain Declaration**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | PROPAGATION_SEQUENCE
```

**Phase 0-A-8 — Deviation Budget (FIELD|VALUE format required)**

Express as a FIELD|VALUE table. Each severity threshold is a distinct row:
```
FIELD        | VALUE
-------------|------------------------------
P0_MAX       | [integer — 0 means any P0 is BUDGET_EXCEEDED]
P1_MAX       | [integer]
P2_MAX       | [integer]
P3_MAX       | [integer]
BUDGET_LOCK  | BUDGET LOCKED — may not be revised after Phase 1-S begins
RATIONALE    | [one sentence]
```
A prose paragraph describing thresholds does not satisfy C-62 for this declaration.

**Phase 0-A-9 — Constraint Chain Budget (FIELD|VALUE format required)**

Each CHAIN-NN is a distinct block of rows:
```
FIELD          | VALUE
---------------|------------------------------
CHAIN_ID       | CHAIN-NN
HEAD_CONV      | CONV-NN
CHAIN_LENGTH   | [integer]
CHAIN_BUDGET   | [max acceptable chain head DEVIATES turns]
RATIONALE      | [one sentence]
```
Repeat this block for each CHAIN-NN. Every CHAIN-NN from Phase 0-A-7 must have a block.

**Phase 0-A-10 — Turn Prediction Contract (FIELD|VALUE format required)**

One HAPPY_PATH block required; up to 3 ALT_PATH blocks:
```
FIELD                    | VALUE
-------------------------|------------------------------
PATH_ID                  | HP-01
PATH_DESCRIPTION         | [scenario narrative]
PATH_CRITICALITY         | CRITICAL|IMPORTANT|INFORMATIONAL
PREDICTED_TURN_SEQUENCE  | [ordered TOPIC_ID list]
```
Sign row:
```
FIELD                            | VALUE
---------------------------------|------
TURN_PREDICTION_CONTRACT_SIGNED  | YES
```
CRITICAL paths: PREDICTION_DEVIATION auto-elevates to P1 minimum.

**Phase 0-A-11 — Status Quo Method Declaration (FIELD|VALUE format required)**

Each field and each METHOD_BLIND_SPOTS dimension is a separate row:
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
A METHOD_BLIND_SPOTS dimension expressed as prose (e.g., "the method does not check
chain effects") does not constitute a schema row and does not satisfy C-62 for that
dimension.

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1

For each C-62-applicable declaration, verify FIELD|VALUE completeness — count rows, not
prose:

```
Phase 0-CA-1:
  DECLARATION_SCHEMA_COMPLETE:
    DEVIATION_BUDGET: PASS|FAIL  (5 required rows: P0_MAX, P1_MAX, P2_MAX, P3_MAX, RATIONALE)
    CONV_CHAIN_BUDGET: PASS|FAIL  (5 rows per CHAIN-NN: CHAIN_ID, HEAD_CONV, CHAIN_LENGTH, CHAIN_BUDGET, RATIONALE)
    TURN_PREDICTION_CONTRACT: PASS|FAIL  (4 rows per path: PATH_ID, PATH_DESCRIPTION, PATH_CRITICALITY, PREDICTED_TURN_SEQUENCE)
    STATUS_QUO_METHOD: PASS|FAIL  (9 rows: 3 metadata + 5 BLIND dimensions + SIGNED)
  COVERAGE_DELTA: [empty or list]
  CHAIN_BUDGET_DELTA: [empty or list]
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  COLUMN_SCHEMA_COMPLETE: N/A (no Phase 0-D-0 in this variation; column schema derived from phase instructions)
  GATE_STATUS: PASS|FAIL
```

Any FAIL in DECLARATION_SCHEMA_COMPLETE, non-empty delta, or missing signature produces
GATE_STATUS: FAIL.

---

### ROLE 3 — DEVELOPER: Phases 1–5

All phases as specified in V-01, with FIELD|VALUE tables for Phase 0 declarations as
the source of truth. Phase 1 turn table columns as documented in phase instructions.
Close Phase 5 with DEVELOPER_CERTIFICATION: COMPLETE.

---

### ROLE 4 — AUDITOR: Phase 6

As specified in V-01. Opens with "Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning
independent audit." Phase 6-A CONTRACT_AUDIT_GATE_HONORED additionally verifies that
DECLARATION_SCHEMA_COMPLETE: PASS for all four C-62-applicable declarations.

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

As specified in V-01.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-04 — Axes I+J: Pre-Flight Manifest + Column Schema as First Artifact

**Variation axes:** Role sequence (Axis I) + Output format (Axis J) — PRE_FLIGHT_MANIFEST
as Phase -1 combined with COLUMN_SCHEMA_REGISTRY as the first Phase 0 artifact.

**Hypothesis:** The manifest lists the column schema registry as a required artifact
(STATUS: PENDING at Phase -1). The Topology Architect must satisfy Phase 0-D-0 before
any other Phase 0 block. At Phase 0-CA-1, the Contract Auditor updates the manifest
to COMPLETE|MISSING and verifies COLUMN_SCHEMA_COMPLETE as its first gate check
(before COVERAGE_DELTA). This binds role-sequence interlock (C-59/C-60) with
schema-first enforcement (C-61) into a single structural protocol.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles: CONTRACT AUDITOR (Phase -1 + Phase 0-CA-1), TOPOLOGY ARCHITECT (Phase 0),
DEVELOPER (Phases 1–5), AUDITOR (Phase 6), REMEDIATION PLANNER (Phase 7).

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute Phase -1 before the Topology Architect authors any Phase 0 content.

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
Deviation Budget                              | 0-A-8      | PENDING
Constraint Chain Budget                       | 0-A-9      | PENDING
Turn Prediction Contract                      | 0-A-10     | PENDING
Status Quo Method Declaration                 | 0-A-11     | PENDING

PRE_FLIGHT_MANIFEST_STATUS: PENDING
```

The COLUMN_SCHEMA_REGISTRY row is listed first in the manifest, signaling that it is
the first artifact the Topology Architect must produce.

---

### ROLE 2 — TOPOLOGY ARCHITECT: Phase 0 declarations

Author Phase 0-D-0 FIRST, then proceed in order. Every other phase must reference only
columns declared in Phase 0-D-0.

**Phase 0-D-0 — Column Schema Registry (satisfies manifest row 1)**

```
COLUMN_NAME          | FORMAT                                    | ALLOWED_VALUES                                                        | REQUIRED_WHEN
---------------------|-------------------------------------------|-----------------------------------------------------------------------|--------------------
TURN_ID              | T-NN                                      | T-01, T-02, ...                                                       | Every turn
USER_UTTERANCE       | free text                                 | any                                                                   | Every turn
TOPIC_MATCHED        | TOPIC_ID                                  | declared topics or CONTRACT_GAP                                       | Every turn
NODES_EXECUTED       | comma-separated node names                | any                                                                   | Every turn
AGENT_RESPONSE       | free text                                 | any                                                                   | Every turn
TRANSITION_TARGET    | TOPIC_ID or terminal state                | declared topics, TERMINAL, FALLBACK                                   | Every turn
SESSION_STATE        | derived from Phase 1-S replay             | variable=value pairs                                                  | Every turn
CONFORMANCE          | verdict                                   | CONFORMS, DEVIATES[CONV-NN]                                           | Every turn
CONSTRAINT_VERDICTS  | list of CONV-NN evaluations               | PASS, FAIL, CHAIN_SUSPENDED[chain head: CONV-NN broke at TURN_ID]     | Every turn
CHAIN_EFFECTS        | propagation effects                       | CONV-NN → [CONV-NN: ACTIVATED\|SUSPENDED, ...]                        | Every turn
PREDICTION_MATCH     | path match result                         | ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual], OFF_ALL_PATHS | Every turn
SLOT_FILL_STATUS     | slot=RESULT                               | FILLED, SKIPPED, INTERRUPTED                                          | Slot-fill turns only
```

**Phase 0-D-1 through 0-D-5 and 0-A-6 through 0-A-11** — as specified in V-02,
including FIELD|VALUE table format for Phase 0-A-8 (Deviation Budget),
Phase 0-A-9 (Chain Budget), Phase 0-A-10 (Turn Prediction Contract), and
Phase 0-A-11 (Status Quo Method Declaration).

---

### ROLE 1 — CONTRACT AUDITOR: Phase 0-CA-1 (Manifest resolution + full gate)

Update the PRE_FLIGHT_MANIFEST and run all blocking checks:

```
PRE_FLIGHT_MANIFEST (updated):

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
Deviation Budget                              | 0-A-8      | COMPLETE|MISSING
Constraint Chain Budget                       | 0-A-9      | COMPLETE|MISSING
Turn Prediction Contract                      | 0-A-10     | COMPLETE|MISSING
Status Quo Method Declaration                 | 0-A-11     | COMPLETE|MISSING

PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL
```

Compute:
- COLUMN_SCHEMA_COMPLETE: PASS|FAIL (Phase 0-D-0 row for every Phase 1 column)
- COVERAGE_DELTA: VARS_IN_TOPOLOGY − VARS_IN_CONTRACT
- CHAIN_BUDGET_DELTA: CHAINS_IN_TOPOLOGY − CHAINS_IN_BUDGET
- DECLARATION_SCHEMA_COMPLETE: PASS|FAIL for each of the four C-62 declarations
- PREDICTION_CONTRACT_SIGNED: YES|NO
- STATUS_QUO_METHOD_SIGNED: YES|NO

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

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**

All phases as specified in V-01. Close Phase 5 with DEVELOPER_CERTIFICATION: COMPLETE.

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

Phase 6-A CONTRACT_AUDIT_GATE_HONORED verifies: PRE_FLIGHT_MANIFEST_STATUS: PASS,
COLUMN_SCHEMA_COMPLETE: PASS, all deltas empty, all signatures present.

All other Phase 6 sub-phases as specified in V-01.

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

As specified in V-01.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-05 — Axes I+J+K: Manifest + Column Schema + Universal FIELD|VALUE + Lifecycle Emphasis

**Variation axes:** Role sequence (Axis I) + Output format (Axis J) + Universal FIELD|VALUE
language (Axis K) + lifecycle emphasis on explicit handoff tokens at every role boundary.

**Hypothesis:** Combining all three single axes produces a prompt where: (1) no Phase 0
artifact can be silently omitted (manifest), (2) no Phase 1 column can be silently omitted
(column schema first), (3) no Phase 0 structured field can be silently omitted (FIELD|VALUE
universal language), and (4) no role boundary can be crossed without an explicit handoff
token (lifecycle emphasis). The four new v13 criteria (C-59 through C-62) become structural
outcomes of the prompt format, not aspirational additions.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate. Every role boundary is an explicit protocol event — roles do not
implicitly continue from adjacent phases. Each role issues and receives declared handoff
tokens. Silent fallthrough is a structural violation.

**Roles:**
- CONTRACT AUDITOR — Phase -1 (PRE_FLIGHT_MANIFEST), Phase 0-CA-1 (gate)
- TOPOLOGY ARCHITECT — Phase 0-D-0 through Phase 0-A-11
- DEVELOPER — Phases 1–5
- AUDITOR — Phase 6
- REMEDIATION PLANNER — Phase 7

**Universal format constraint:** Every structured Phase 0 declaration with multiple fields
uses FIELD|VALUE table rows. No prose field descriptions. No numbered lists as field
substitutes. A field expressed in prose is structurally invisible to the Contract Auditor
and does not satisfy the declaration schema.

---

### ROLE 1 — CONTRACT AUDITOR: Phase -1 (Pre-Flight Manifest)

Execute FIRST. The Topology Architect may not begin Phase 0-D-0 until this manifest exists.

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

Open with: **"Received PRE_FLIGHT_MANIFEST. Authoring Phase 0-D-0 through 0-A-11 against
pending manifest."**

**Phase 0-D-0 — Column Schema Registry**

First artifact. Declare every Phase 1 column:

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

**Phase 0-D-1 through 0-D-5** — same table schemas as V-04.

**Phase 0-A-6 — Session Variable Timeline Contract**
```
VARIABLE | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED | AUTHORIZED_REWRITERS
```

**Phase 0-A-7 — Invariant Chain Declaration**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | PROPAGATION_SEQUENCE
```

**Phase 0-A-8 — Deviation Budget (FIELD|VALUE rows)**
```
FIELD        | VALUE
-------------|---------------------------------------
P0_MAX       | [0 = any P0 is BUDGET_EXCEEDED]
P1_MAX       | [integer]
P2_MAX       | [integer]
P3_MAX       | [integer]
RATIONALE    | [one sentence]
BUDGET_LOCK  | BUDGET LOCKED — may not be revised after Phase 1-S begins
```

**Phase 0-A-9 — Constraint Chain Budget (FIELD|VALUE rows per chain)**

One block per CHAIN-NN from Phase 0-A-7:
```
FIELD          | VALUE
---------------|-------------------------------
CHAIN_ID       | CHAIN-NN
HEAD_CONV      | CONV-NN
CHAIN_LENGTH   | [integer]
CHAIN_BUDGET   | [max chain-head DEVIATES turns]
RATIONALE      | [one sentence]
```

**Phase 0-A-10 — Turn Prediction Contract (FIELD|VALUE rows per path)**

One block per path (HP-01 required; up to 3 ALT-NN):
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

Update manifest, then run all gate checks:

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
```

Then:
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
    STATUS_QUO_METHOD: PASS|FAIL  (count 9 rows: 3 metadata + 5 BLIND + SIGNED)
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  GATE_STATUS: PASS|FAIL
```

GATE_STATUS: FAIL if: any manifest row is MISSING, any DECLARATION_SCHEMA check fails,
COVERAGE_DELTA non-empty, CHAIN_BUDGET_DELTA non-empty, or any signature is NO.

Close with: **"GATE_STATUS: [value] issued. HANDOFF_TO: DEVELOPER."**

---

### ROLE 3 — DEVELOPER: Phases 1–5

Open with: **"Received GATE_STATUS: [value]. Proceeding|Blocked."**
FAIL: halt; document blocking condition; do not author Phase 1.

**Phase 1-S — Session Variable Mutation Log (author BEFORE Phase 1)**
```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
SESSION_STATE cells in Phase 1 are derived by replaying Phase 1-S in turn order.
Each SESSION_STATE cell cites its Phase 1-S source row.

**Phase 1 — Turn-by-Turn Trace**
One row per turn; all columns from Phase 0-D-0. No turns skipped. No prohibited
vocabulary. Inject at least one adversarial utterance: record injection TURN_ID,
system response, defect triggered (if any), recovery to completion.

**Phase 1-T — Topic Aggregate (additive)**
```
TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ |
DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP | PATH_IDS_MATCHED
```

**Phase 2 — Defect Classification**
Nine defect classes. For each FOUND defect:
```
DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS | INVARIANT_CITE |
REPRODUCTION_STEPS | RECOVERY | ENTANGLEMENT_VERDICT
```
CRITICAL-path PREDICTION_DEVIATION: add PLAN_TIER_OVERRIDE: IMMEDIATE.

P0 defects: emit EXECUTION_HALT (HALT_TRIGGER, ROOT_CAUSE, MVF_RECOMMENDATION,
MVF_SCOPE, UNBLOCKED_BY, CHAIN_BREAK_TRACE with BROKEN_CHAIN/CHAIN_HEAD_CONV/
FIRST_DEVIATE_TURN/SUSPENDED_CONVS/BREAK_TO_DEFECT_PATH, CHAIN_REPAIR) before
classifying lower-severity defects.

**Phase 3-E — Entanglement Map**
```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_CLASS]|MASKED_BY[DEFECT_CLASS]
```

**Phase 4** — Fallback trace, escalation trace (trigger, handoff node, session state,
receipt), disambiguation proposals for intent collisions.

**Phase 4-SQ — Status Quo Simulation**
Using ONLY STATUS_QUO_METHOD. No CONSTRAINT_VERDICTS, CHAIN_EFFECTS, PREDICTION_MATCH,
TIMELINE_ANOMALY, or CHAIN_BUDGET.
```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO |
SQ_DEFECT_CLASS | REMARKS
```
STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND, SQ_DEFECTS_NOT_FOUND.

**Phase 5-A — Deviation Budget Utilization**
```
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
```
OVERALL_BUDGET_STATUS: WITHIN_BUDGET|EXCEEDED. If EXCEEDED: BUDGET_EXCEEDED_FINDING.

**Phase 5-B — Chain Budget Utilization**
```
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
```
CHAIN_BUDGET_EXCEEDED findings (8th structural class) for exceeded chains.

**Phase 5-C — Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```

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
DETECTION_METHOD | SQ_BLIND_SPOT
```
Auto-classification from FIELD|VALUE rows in Phase 0-A-11.
Close with STATUS_QUO_GAP_SUMMARY.

Close Phase 5 with: **DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR.**

---

### ROLE 4 — AUDITOR: Phase 6

Open with: **"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."**

The Auditor never modifies Developer rows. Discrepancies are audit findings.

**Phase 6-A:** CONTRACT_AUDIT_GATE_HONORED: PRE_FLIGHT_MANIFEST_STATUS was PASS,
COLUMN_SCHEMA_COMPLETE was PASS, DECLARATION_SCHEMA_COMPLETE was PASS for all four
declarations, all deltas empty, all signatures present — all confirmed before Phase 1.
BUDGET_UTILIZATION_VERIFIED. BUDGET_STATUS_CONSISTENT. SIMULATION_DELTA_COMPLETE.

**Phase 6-B** — Severity Co-Residency Audit (structured table; prose not sufficient).
EXEMPT: CONFIRMED_ABSENT rows.

**Phase 6-C** — Entanglement Consistency Audit (Phase 3-E vs Phase 1 evidence).

**Phase 6-D** — Topic Aggregate Consistency Audit (Phase 1-T CONFORMANCE_ROLLUP vs
Phase 1 DEVIATES counts). TOPIC_ROLLUP_MISMATCH findings.

**Phase 6-E** — Session Timeline Consistency Audit (Phase 1-S replay vs Phase 1
SESSION_STATE). TIMELINE_STATE_MISMATCH findings.

**Phase 6-F** — Fix Viability Audit (per EXECUTION_HALT: CONV_VIOLATIONS_INTRODUCED,
CONV_VIOLATIONS_DETAIL, VIABILITY, CHAIN_REPAIR_COMPLETE).

**Phase 6-G** — Chain Integrity Audit (per CHAIN-NN: CHAIN_STATUS_REPORTED vs
CHAIN_STATUS_AUDITED, CONSISTENT: PASS|FAIL; CHAIN_VERDICT_INCONSISTENCY findings).

**Phase 6-H** — Combined Plan Integrity / Path Adherence / Status Quo Coverage Audit
(PLAN_INTEGRITY_AUDIT, DEPENDENCY_CYCLE_CHECK, PLAN_TIER_OVERRIDE_PRESENT,
OVERRIDE_TIER_HONORED; PATH_ADHERENCE_RATIO_VERIFIED, CRITICAL_PATH_ESCALATION_VERIFIED;
AUTOMATIC_CLASSIFICATION_VERIFIED, STATUS_QUO_COVERAGE_AUDIT).

Close with: **AUDITOR_CERTIFICATION: PASS|FAIL[cite blocking findings].
HANDOFF_TO: REMEDIATION PLANNER.**

---

### ROLE 5 — REMEDIATION PLANNER: Phase 7

Open with: **"Received AUDITOR_CERTIFICATION. Constructing REMEDIATION_PLAN."**

For each FOUND defect, one PLAN_ITEM:
```
PLAN_ID: RP-NN
DEFECT_REF: [Phase 2 DEFECT_ID]
SEVERITY_CLASS: P0|P1|P2|P3
SCOPE: [topics/transitions/session variables; MVF_SCOPE when available]
DEPENDENCY_ON: [RP-NN list from ENABLES in Phase 3-E]
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG
TIER_RATIONALE: [P0→IMMEDIATE; PLAN_TIER_OVERRIDE for CRITICAL deviations; P1→NEXT_SPRINT; P2/P3→BACKLOG]
CHAIN_REPAIR_ITEMS: [CONV-NN list from EXECUTION_HALT CHAIN_REPAIR; empty if no P0]
UNBLOCKED_BY: [observable state confirming fix applied]
```

Sort rules: (1) no PLAN_ITEM before any item in DEPENDENCY_ON, (2) P0→IMMEDIATE before
PLAN_TIER_OVERRIDE: IMMEDIATE before P1→NEXT_SPRINT before P2/P3→BACKLOG, (3) within tier:
lower DEFECT_ID first.

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
