# Quest Variations — flow-conversation — Round 13 (v12 rubric)

**Date:** 2026-03-15 | **Rubric version:** v12 | **Max score:** 212

---

## Variation Axes Selected

All 5 variations carry the full v12 baseline: C-01 through C-58. The baseline
includes mutation-first authoring, AUTHORIZED_REWRITERS, Contract Auditor gate
(COVERAGE_DELTA + CHAIN_BUDGET_DELTA + PREDICTION_CONTRACT + STATUS_QUO_METHOD),
EXECUTION_HALT blocks with CHAIN_BREAK_TRACE and CHAIN_REPAIR, PROPAGATION + CHAIN_ID,
CHAIN_EFFECTS column, DEVIATION_BUDGET, CHAIN_BUDGET, CHAIN_BUDGET_EXCEEDED as 8th
structural finding class, REMEDIATION PLANNER (Phase 7), TURN_PREDICTION_CONTRACT,
PREDICTION_DEVIATION as 9th defect class, PATH_ADHERENCE_RATIO, STATUS_QUO_METHOD
declaration, STATUS_QUO_SIMULATION (Phase 4-SQ), STATUS_QUO_COVERAGE table (Phase 5-F),
and STATUS_QUO_COVERAGE_AUDIT (Phase 6-H).

**Single-axis (3):**

- **Axis F — Role sequence**: The Contract Auditor is elevated from a Phase 0 sub-task
  to a named, first-class blocking role that holds exclusive authority before Phase 1
  begins. All four blocking deltas (COVERAGE_DELTA, CHAIN_BUDGET_DELTA,
  PREDICTION_CONTRACT, STATUS_QUO_METHOD) are consolidated into a single gate
  checkpoint. No Developer output appears until the Auditor gate certifies PASS.

- **Axis G — Output format (table-first)**: Every phase definition leads with its
  mandatory table schema before any prose instructions. Prose is supplementary.
  All coverage ratios, defect catalogs, audit results, and plan items are defined
  by their column schemas. Deviation from the declared schema is a format violation.

- **Axis H — Phrasing register (imperative second-person)**: The entire prompt is
  written in direct second-person imperative. No passive constructions. Short declarative
  sentences. "Emit", "Declare", "Do not proceed", "You must", "Record exactly one row
  per turn" replaces formal descriptive register throughout.

**Combined (2):**

- **Axes F+G — Role sequence + table-first format**: Contract Auditor as blocking gate
  combined with mandatory table schemas per role boundary. Every handoff between roles
  is a structured table delivered to the next role. Role interlock is defined by table
  presence, not prose narrative.

- **Axes H+inertia — Imperative register + status-quo framing**: The prompt opens with
  the status-quo failure case (what informal review structurally cannot see) and maintains
  imperative register throughout. The STATUS_QUO_METHOD and STATUS_QUO_SIMULATION are
  front-loaded as the primary motivation for the skill. Technical phases follow as
  the evidential mechanism.

---

## V-01 — Axis F: Contract Auditor as Blocking Role

**Variation axis:** Role sequence — Contract Auditor elevated to first-class blocking
role before any Developer phase.

**Hypothesis:** Consolidating all four pre-execution blocking conditions into a single,
named CONTRACT AUDITOR role that holds an exclusive blocking position before Phase 1
produces more complete pre-execution contracts than embedding the gate as a Phase 0
sub-task. The role boundary makes the gate unavoidable.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

This skill walks the dialog path turn-by-turn, classifies structural defects, tracks
session state, and produces an executable remediation plan. Five roles participate:
CONTRACT AUDITOR (blocking gate), TOPOLOGY ARCHITECT (pre-execution declarations),
DEVELOPER (trace + classification), AUDITOR (independent verification), and
REMEDIATION PLANNER (fix sequencing).

---

### ROLE 1 — CONTRACT AUDITOR (blocking gate)

The Contract Auditor executes FIRST, before the Topology Architect authors any
Phase 0-A declarations. The Auditor's sole function at this stage is to confirm that
four blocking declarations will be present in Phase 0 before Phase 1 begins. Issue
a blocking checklist:

```
CONTRACT_AUDITOR_PRE_CHECK:
  TOPICS_REGISTRY_PRESENT: [REQUIRED — Phase 0-D-1]
  SESSION_VARIABLE_TIMELINE_CONTRACT_PRESENT: [REQUIRED — Phase 0-A-6]
  AUTHORIZED_REWRITERS_PRESENT: [REQUIRED — Phase 0-A-6 extension]
  PROPAGATION_AND_CHAIN_ID_PRESENT: [REQUIRED — Phase 0-A-7]
  CONV_CHAIN_BUDGET_PRESENT: [REQUIRED — Phase 0-A-9]
  TURN_PREDICTION_CONTRACT_PRESENT: [REQUIRED — Phase 0-A-10]
  STATUS_QUO_METHOD_PRESENT: [REQUIRED — Phase 0-A-11]
  VOCABULARY_GATE_SIGNED: [REQUIRED — Phase 0-D-2]
  INVARIANT_REGISTER_PRESENT: [REQUIRED — Phase 0-D-4]
  TRANSITION_MAP_PRESENT: [REQUIRED — Phase 0-D-5]
  DEVIATION_BUDGET_PRESENT: [REQUIRED — Phase 0-A-8]
```

This checklist is a pre-flight declaration of intent, not yet a verification of content.
It signals to the Topology Architect what must be authored. The Auditor will re-evaluate
at Phase 0-CA-1 after Phase 0 is complete.

---

### ROLE 2 — TOPOLOGY ARCHITECT (Phase 0 declarations)

Author all Phase 0 blocks in order. Each block is a contract. Nothing in Phase 1–7
may reference a topic, variable, invariant, transition, or chain that is not declared
here.

**Phase 0-D-1 — Topic Registry**
Declare all topics: TOPIC_ID, TRIGGER_PHRASES (list), ENTRY_CONDITIONS, EXIT_TARGETS.
A topic first encountered in Phase 1 that is absent here is a CONTRACT_GAP finding.

**Phase 0-D-2 — Vocabulary Gate**
Declare PERMITTED_TERMS (Copilot Studio vocabulary) and PROHIBITED_TERMS (generic
chatbot vocabulary without Copilot Studio grounding). Sign: VOCABULARY_GATE_SIGNED: YES.

**Phase 0-D-3 — Session Variable Registry**
Declare all session variables: NAME, PERSISTENCE_CLASS (SESSION | TOPIC_SCOPED | GLOBAL),
INITIAL_VALUE. A variable first appearing in Phase 1 SESSION_STATE absent here is a
CONTRACT_GAP finding.

**Phase 0-D-4 — Invariant Register**
Declare all conversation-level invariants: CONV-NN, DESCRIPTION, FALSIFICATION_CONDITION,
PROPAGATION (list of downstream CONV-NNs), CHAIN_ID (every CONV-NN belongs to exactly
one CHAIN-NN).

**Phase 0-D-5 — Transition Map**
Declare all conversation graph edges: TRANS-NN, SOURCE_TOPIC, TARGET_TOPIC, CONDITION,
REQUIRED|OPTIONAL.

**Phase 0-A-6 — Session Variable Timeline Contract**
Declare the full lifecycle of every variable from Phase 0-D-3: FIRST_WRITTEN_TOPIC,
CLEARED_BY, READ_AFTER_CLEARED (FORBIDDEN|ALLOWED), AUTHORIZED_REWRITERS (list of
topics permitted to write the variable beyond FIRST_WRITTEN_TOPIC). A write from a
topic absent from both FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS is an
OFF_CONTRACT_WRITE anomaly.

**Phase 0-A-7 — Invariant Chain Declaration**
For each CHAIN-NN implied by Phase 0-D-4 CHAIN_ID assignments: CHAIN_ID, HEAD_CONV,
CHAIN_LENGTH, PROPAGATION_SEQUENCE (ordered CONV-NN list from head to terminal).

**Phase 0-A-8 — Deviation Budget**
Declare pre-execution deviation thresholds: P0_MAX, P1_MAX, P2_MAX, P3_MAX,
BUDGET_RATIONALE. Lock declaration: "BUDGET LOCKED — may not be revised after Phase 1-S
begins." P0_MAX = 0 means any found P0 defect is a BUDGET_EXCEEDED finding.

**Phase 0-A-9 — Constraint Chain Budget**
Declare per-chain budgets for every CHAIN-NN: CHAIN_ID, HEAD_CONV, CHAIN_LENGTH,
CHAIN_BUDGET (max acceptable chain head DEVIATES turns), BUDGET_RATIONALE.

**Phase 0-A-10 — Turn Prediction Contract**
Declare conversation path expectations before any tracing begins. One HAPPY_PATH
(required); up to 3 ALT_PATHs (optional). For each path: PATH_ID (HP-01 or ALT-NN),
PATH_DESCRIPTION, PATH_CRITICALITY (CRITICAL | IMPORTANT | INFORMATIONAL),
PREDICTED_TURN_SEQUENCE (ordered list of TOPIC_IDs). CRITICAL paths mark core business
transactions; deviations carry automatic P1 severity floor. Sign:
TURN_PREDICTION_CONTRACT_SIGNED: YES.

**Phase 0-A-11 — Status Quo Method Declaration**
Declare the team's current informal review method: METHOD_NAME, METHOD_DESCRIPTION,
METHOD_COVERAGE. Declare METHOD_BLIND_SPOTS as a structured checklist — YES|NO per
dimension: CONSTRAINT_VERDICTS, CHAIN_EFFECTS, TIMELINE_ANOMALIES, PREDICTION_CONTRACT,
CHAIN_BUDGET. Sign: STATUS_QUO_METHOD_SIGNED: YES. A prose paragraph without the
structured checklist does not satisfy this declaration.

---

### ROLE 1 — CONTRACT AUDITOR (Phase 0-CA-1, blocking gate)

After all Phase 0 blocks are authored, the Contract Auditor executes Phase 0-CA-1.
This is a hard blocking gate. Phase 1 does not begin until this gate passes.

Compute four deltas:

**COVERAGE_DELTA:** Every session variable in Phase 0-D-1 topic topology must have a
Phase 0-A-6 contract entry. VARS_IN_TOPOLOGY − VARS_IN_CONTRACT = COVERAGE_DELTA.
A non-empty delta is a CONTRACT_COMPLETENESS_FAILURE.

**CHAIN_BUDGET_DELTA:** Every CHAIN-NN in Phase 0-A-7 must have a Phase 0-A-9 entry.
CHAINS_IN_TOPOLOGY − CHAINS_IN_BUDGET = CHAIN_BUDGET_DELTA. A non-empty delta blocks
execution.

**PREDICTION_CONTRACT_CHECK:** PATHS_IN_CONTRACT: [PATH_IDs]. PREDICTION_CONTRACT_SIGNED:
YES|NO. A missing signature blocks execution.

**STATUS_QUO_METHOD_CHECK:** STATUS_QUO_METHOD_SIGNED: YES|NO. BLIND_SPOTS_CHECKLIST_PRESENT:
YES|NO. A missing signature or absent checklist blocks execution.

Emit:
```
Phase 0-CA-1:
  COVERAGE_DELTA: [empty | list of missing variables]
  CHAIN_BUDGET_DELTA: [empty | list of missing chains]
  PATHS_IN_CONTRACT: [HP-01, ALT-01, ...]
  PREDICTION_CONTRACT_SIGNED: YES|NO
  STATUS_QUO_METHOD_SIGNED: YES|NO
  BLIND_SPOTS_CHECKLIST_PRESENT: YES|NO
  GATE_STATUS: PASS | BLOCKED[reason]
```

GATE_STATUS: PASS is required before Phase 1 begins. Document any blocking condition
before proceeding.

---

### ROLE 3 — DEVELOPER (Phases 0-A-8-lock through 5)

**Phase 0-A-8-lock — Deviation Budget lock**
Confirm DEVIATION_BUDGET is locked: "BUDGET LOCKED — may not be revised after Phase 1-S
begins."

**Phase 1-S — Session Variable Mutation Log (author first)**
Author Phase 1-S BEFORE Phase 1 SESSION_STATE. For each turn, for each non-null variable:
VARIABLE_NAME | TURN_ID | MUTATION_TYPE (WRITE|READ|CLEAR|NO_CHANGE) | VALUE_AFTER.
SESSION_STATE in Phase 1 is derived by replaying Phase 1-S mutations; do not independently
author SESSION_STATE.

**Phase 1 — Turn-by-Turn Trace**
Walk every conversation turn. For each turn emit one row:
TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE |
SESSION_STATE (derived from Phase 1-S replay) | CONFORMANCE (CONFORMS | DEVIATES[CONV-NN]) |
CONSTRAINT_VERDICTS (list of CONV-NN: PASS|FAIL|CHAIN_SUSPENDED[chain head: CONV-NN broke
at TURN_ID]) | CHAIN_EFFECTS (CONV-NN → [CONV-NN-downstream: ACTIVATED|SUSPENDED, ...]) |
PREDICTION_MATCH (ON_PATH[PATH_ID] | DEVIATION[PATH_ID, expected_TOPIC, actual_TOPIC] |
OFF_ALL_PATHS) | SLOT_FILL_STATUS (if applicable: slot, result FILLED|SKIPPED|INTERRUPTED)

No turns may be skipped. Prohibited vocabulary from Phase 0-D-2 must not appear.

**Phase 1-T — Topic Aggregate**
Additive to Phase 1 (does not replace it). For each topic visited: TOPIC_ID |
TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ | DEFECT_CITATIONS |
ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP (DEVIATES count) | PATH_IDS_MATCHED.

**Phase 2 — Defect Classification**
Classify every structural defect in severity order. Defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHANED_TOPIC,
TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, and CONTRACT_GAP.

For each FOUND defect: DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS (P0–P3) |
INVARIANT_CITE (CONV-NN) | REPRODUCTION_STEPS | RECOVERY (RECOVERABLE[min_turns,
target_state] | UNRECOVERABLE[reason]) | ENTANGLEMENT_VERDICT (placeholder; resolved
in Phase 3-E).

CRITICAL-path PREDICTION_DEVIATION defects additionally carry:
PLAN_TIER_OVERRIDE: IMMEDIATE
PLAN_TIER_OVERRIDE_ANNOTATION: "CRITICAL path deviation — overrides severity-based tier."

For each FOUND P0 defect, emit an EXECUTION_HALT block before classifying lower-severity
defects:
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
For each FOUND defect: ENTANGLEMENT_VERDICT: ISOLATED | ENABLES[DEFECT_CLASS] |
MASKED_BY[DEFECT_CLASS]. MASKED_BY defects carry conditional recovery verdicts.

**Phase 4 — Fallback, Escalation, Disambiguation**
Trace at least one fallback path to completion. Trace at least one escalation path
(trigger, handoff node, session state at handoff, agent receipt). For each intent
collision found in Phase 2, propose a disambiguation strategy with rationale.

**Phase 4-SQ — Status Quo Simulation**
Re-run the same scenario using ONLY the declared STATUS_QUO_METHOD from Phase 0-A-11.
Apply no CONSTRAINT_VERDICTS, no CHAIN_EFFECTS, no PREDICTION_MATCH, no TIMELINE_ANOMALY
tracking, no CHAIN_BUDGET tracking. For each turn:
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO |
SQ_DEFECT_CLASS | REMARKS

Close with STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND (list),
SQ_DEFECTS_NOT_FOUND (populated after Phase 5-F comparison).

**Phase 5 — Coverage and Quality**

*Phase 5-A — Deviation Budget Utilization*
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
OVERALL_BUDGET_STATUS: WITHIN_BUDGET|EXCEEDED[violated classes]
If EXCEEDED: BUDGET_EXCEEDED_FINDING with VIOLATED_CLASSES, OVER_BY per class, IMPLICATION.

*Phase 5-B — Chain Budget Utilization*
For each CHAIN-NN: HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
For each EXCEEDED chain: CHAIN_BUDGET_EXCEEDED finding (FINDING_CLASS: CHAIN_BUDGET_EXCEEDED,
CHAIN_ID, HEAD_CONV, BUDGET, ACTUAL, OVER_BY, FIRST_EXCEED_TURN, SUSPENDED_CONVS, IMPLICATION).

*Phase 5-C — Constraint Chain Status Summary*
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
BROKEN chains cross-reference their EXECUTION_HALT block.

*Phase 5-D — Coverage Quality Gate*
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (DEGRADED when TIMELINE_ANOMALY_RATE > 0).
Under DEGRADED, all ratios carry PROVISIONAL.
Report five ratios:
1. TOPIC_COVERAGE_RATIO = topics_visited / total_declared [numerator/denominator visible]
2. TRANSITION_COVERAGE_RATIO = transitions_exercised / total_declared
3. SLOT_PATH_COVERAGE_RATIO = slot_paths_completed / total_slot_paths
4. TIMELINE_ANOMALY_RATE = timeline_anomalies_found / total_variable_turn_events
5. PATH_ADHERENCE_RATIO = turns_on_any_predicted_path / total_turns

Orphaned topics (declared but unreachable) are ORPHAN defects and appear in the
topic_coverage_ratio denominator. Unexercised REQUIRED transitions are orphaned-edge
defects with UNRECOVERABLE[missing edge].

*Phase 5-F — Status Quo Coverage Table*
For each FOUND defect from Phase 2:
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION: YES|NO | FOUND_BY_STATUS_QUO: YES|NO |
DETECTION_METHOD (FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH | FOUND_BY_STATUS_QUO_ONLY) |
SQ_BLIND_SPOT (the METHOD_BLIND_SPOTS key explaining the miss; N/A for FOUND_BY_BOTH)

Structural auto-classification rules from declared blind spots:
- PREDICTION_DEVIATION → FOUND_BY_SIMULATION_ONLY when METHOD_BLIND_SPOTS.PREDICTION_CONTRACT: NO
- CHAIN_BUDGET_EXCEEDED → FOUND_BY_SIMULATION_ONLY when METHOD_BLIND_SPOTS.CHAIN_BUDGET: NO
- TIMELINE_ANOMALY → FOUND_BY_SIMULATION_ONLY when METHOD_BLIND_SPOTS.TIMELINE_ANOMALIES: NO

Close with STATUS_QUO_GAP_SUMMARY: FOUND_BY_SIMULATION_ONLY_COUNT,
FOUND_BY_SIMULATION_ONLY_LIST, STRUCTURAL_BLIND_SPOTS_ACTIVATED (METHOD_BLIND_SPOTS keys
that contributed), STATUS_QUO_GAP_NARRATIVE (one paragraph on what the informal method
structurally cannot see). This table satisfies C-35 automatically.

---

### ROLE 4 — AUDITOR (Phase 6 independent verification)

The Auditor never modifies Developer rows. Discrepancies are audit findings.

**Phase 6-A:** CONTRACT_AUDIT_GATE_HONORED (Phase 0-CA-1 produced all-empty deltas).
BUDGET_UTILIZATION_VERIFIED (actual DEVIATES counts vs Phase 2 FOUND).
BUDGET_STATUS_CONSISTENT. SIMULATION_DELTA_COMPLETE (every Phase 2 FOUND defect in
exactly one detection category in Phase 5-F).

**Phase 6-B — Severity Co-Residency Audit:**
Every FOUND defect row has both SEVERITY_CLASS and INVARIANT_CITE. Structured table;
prose does not satisfy. EXEMPT: CONFIRMED_ABSENT rows.

**Phase 6-C — Entanglement Consistency Audit:**
Verify Phase 3-E ENTANGLEMENT_MAP against Phase 1 turn-level evidence.

**Phase 6-D — Topic Aggregate Consistency Audit:**
Cross-check Phase 1-T CONFORMANCE_ROLLUP against DEVIATES count per topic from Phase 1.
Any mismatch is a TOPIC_ROLLUP_MISMATCH finding.

**Phase 6-E — Session Timeline Consistency Audit:**
Replay Phase 1-S mutations in sequence and compare reconstructed SESSION_STATE against
Phase 1 SESSION_STATE column. Any discrepancy is a TIMELINE_STATE_MISMATCH finding.

**Phase 6-F — Fix Viability Audit:**
For each EXECUTION_HALT block: CONV_VIOLATIONS_INTRODUCED: YES|NO,
CONV_VIOLATIONS_DETAIL, VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[CONV-NN list].
CHAIN_REPAIR_COMPLETE: YES|NO (every CONV-NN in CHAIN_REPAIR appears in MVF_SCOPE).

**Phase 6-G — Chain Integrity Audit:**
Verify CHAIN_EFFECTS in Phase 1 against upstream CONV-NN verdicts. Per CHAIN-NN:
CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL.
CHAIN_VERDICT_INCONSISTENCY finding when a downstream CONV-NN CONFORMs during a
SUSPENDED chain window.

**Phase 6-H — Combined Plan Integrity / Path Adherence / Status Quo Coverage Audit:**
*Plan Integrity:*
For each EXECUTION_HALT: EXECUTION_HALT_IN_PLAN: YES|NO, CHAIN_REPAIR_IN_SCOPE: YES|NO.
For each PLAN_ITEM: DEPENDENCY_ORDER_VALID: YES|NO.
PLAN_INTEGRITY_AUDIT: PASS|FAIL. DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND.
PLAN_TIER_OVERRIDE_PRESENT: PASS|FAIL (all CRITICAL PREDICTION_DEVIATION defects carry
PLAN_TIER_OVERRIDE: IMMEDIATE). OVERRIDE_TIER_HONORED: PASS|FAIL.

*Path Adherence:*
Per-turn: TURN_ID | PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED | CONSISTENT: PASS|FAIL.
PATH_ADHERENCE_RATIO_VERIFIED: PASS|FAIL.
CRITICAL_PATH_ESCALATION_VERIFIED: PASS|FAIL.

*Status Quo Coverage:*
Per defect: DETECTION_METHOD_REPORTED | DETECTION_METHOD_AUDITED | CONSISTENT: PASS|FAIL.
AUTOMATIC_CLASSIFICATION_VERIFIED:
  PREDICTION_DEVIATION_CLASSIFIED_CORRECTLY: PASS|FAIL
  CHAIN_BUDGET_EXCEEDED_CLASSIFIED_CORRECTLY: PASS|FAIL
  TIMELINE_ANOMALY_CLASSIFIED_CORRECTLY: PASS|FAIL
STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL

Close with AUDITOR_CERTIFICATION: PASS|FAIL[cite blocking findings].

---

### ROLE 5 — REMEDIATION PLANNER (Phase 7)

Execute after AUDITOR_CERTIFICATION. Read all EXECUTION_HALT blocks from Phase 2 and
the Phase 3-E ENTANGLEMENT_MAP.

For each FOUND defect, emit one PLAN_ITEM:
```
PLAN_ID: RP-NN
DEFECT_REF: [Phase 2 DEFECT_ID]
SEVERITY_CLASS: P0|P1|P2|P3
SCOPE: [topics/transitions/session variables; use MVF_SCOPE from EXECUTION_HALT when available]
DEPENDENCY_ON: [RP-NN list derived from ENABLES relationships in Phase 3-E]
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG
TIER_RATIONALE: [P0 → IMMEDIATE; PLAN_TIER_OVERRIDE: IMMEDIATE for CRITICAL path deviations;
  P1 → NEXT_SPRINT; P2/P3 → BACKLOG]
CHAIN_REPAIR_ITEMS: [CONV-NN list from EXECUTION_HALT CHAIN_REPAIR; empty if no EXECUTION_HALT]
UNBLOCKED_BY: [observable state confirming this fix applied]
```

Topological sort rule: no PLAN_ITEM may appear before any item in its DEPENDENCY_ON list.
Items with no dependencies appear first. Within a tier: P0 before P1 before P2/P3.
PLAN_TIER_OVERRIDE: IMMEDIATE (from CRITICAL path PREDICTION_DEVIATION defects) is
second-priority tier rule: after P0 → IMMEDIATE, before P1 → NEXT_SPRINT.

Close with PLAN_SUMMARY:
```
PLAN_ITEM_COUNT: N
IMMEDIATE_COUNT: N
NEXT_SPRINT_COUNT: N
BACKLOG_COUNT: N
DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND[RP-NN cycle description]
```

A trace with no FOUND defects satisfies Phase 7 with PLAN_ITEM_COUNT: 0.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-02 — Axis G: Table-First Output Format

**Variation axis:** Output format — every phase definition leads with its mandatory
table schema; prose is supplementary; column schemas define the contract.

**Hypothesis:** Grounding each phase in its output table schema before prose instructions
prevents partial-column implementations and makes machine evaluation unambiguous. The
schema IS the instruction.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles participate: CONTRACT AUDITOR, TOPOLOGY ARCHITECT, DEVELOPER, AUDITOR,
REMEDIATION PLANNER. Each role produces structured table output as its primary artifact.
Prose sections are supplementary; they explain but do not replace the required tables.

---

### Phase 0 — Pre-Execution Declarations (TOPOLOGY ARCHITECT)

Each declaration below specifies its required schema. Author every table before Phase 1.

**Phase 0-D-1 — Topic Registry**
```
TOPIC_ID | TRIGGER_PHRASES | ENTRY_CONDITIONS | EXIT_TARGETS
```
Every topic referenced in Phase 1 must have a row here. First encounter of an undeclared
topic is a CONTRACT_GAP finding.

**Phase 0-D-2 — Vocabulary Gate**
```
TERM | CLASS: PERMITTED|PROHIBITED | RATIONALE
```
Sign at close: VOCABULARY_GATE_SIGNED: YES. Prohibited terms must not appear in Phase 1
trace entries.

**Phase 0-D-3 — Session Variable Registry**
```
NAME | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL | INITIAL_VALUE
```

**Phase 0-D-4 — Invariant Register**
```
CONV-NN | DESCRIPTION | FALSIFICATION_CONDITION | PROPAGATION (downstream list) |
CHAIN_ID
```

**Phase 0-D-5 — Transition Map**
```
TRANS-NN | SOURCE_TOPIC | TARGET_TOPIC | CONDITION | REQUIRED|OPTIONAL
```

**Phase 0-A-6 — Session Variable Timeline Contract**
```
VARIABLE | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED |
AUTHORIZED_REWRITERS (list)
```
Every variable from Phase 0-D-3 must have a row.

**Phase 0-A-7 — Chain Declaration**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | PROPAGATION_SEQUENCE (ordered CONV-NN list)
```

**Phase 0-A-8 — Deviation Budget**
```
SEVERITY | MAX_DEVIATES_ALLOWED | BUDGET_RATIONALE
```
Lock declaration required before Phase 1-S begins.

**Phase 0-A-9 — Constraint Chain Budget**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | CHAIN_BUDGET | BUDGET_RATIONALE
```
Every CHAIN-NN from Phase 0-A-7 must have a row.

**Phase 0-A-10 — Turn Prediction Contract**
```
PATH_ID | PATH_DESCRIPTION | PATH_CRITICALITY: CRITICAL|IMPORTANT|INFORMATIONAL |
PREDICTED_TURN_SEQUENCE (ordered TOPIC_IDs)
```
One HP-01 row required; up to 3 ALT-NN rows. Sign: TURN_PREDICTION_CONTRACT_SIGNED: YES.

**Phase 0-A-11 — Status Quo Method Declaration**
```
FIELD | VALUE
METHOD_NAME | [label]
METHOD_DESCRIPTION | [one paragraph]
METHOD_COVERAGE | [what artifacts the method naturally checks]
BLIND_SPOT: CONSTRAINT_VERDICTS | YES|NO
BLIND_SPOT: CHAIN_EFFECTS | YES|NO
BLIND_SPOT: TIMELINE_ANOMALIES | YES|NO
BLIND_SPOT: PREDICTION_CONTRACT | YES|NO
BLIND_SPOT: CHAIN_BUDGET | YES|NO
STATUS_QUO_METHOD_SIGNED | YES
```

**Phase 0-CA-1 — Contract Auditor Gate (blocking)**
```
CHECK | RESULT | DETAIL
COVERAGE_DELTA | EMPTY|[missing vars] | —
CHAIN_BUDGET_DELTA | EMPTY|[missing chains] | —
PATHS_IN_CONTRACT | [HP-01, ALT-NN list] | —
PREDICTION_CONTRACT_SIGNED | YES|NO | —
STATUS_QUO_METHOD_SIGNED | YES|NO | —
BLIND_SPOTS_CHECKLIST_PRESENT | YES|NO | —
GATE_STATUS | PASS|BLOCKED | [blocking reason if BLOCKED]
```
Phase 1 begins only when GATE_STATUS: PASS.

---

### Phase 1-S — Session Variable Mutation Log (DEVELOPER, author before Phase 1)

```
VARIABLE_NAME | TURN_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | VALUE_AFTER
```
Author this table before Phase 1. SESSION_STATE in Phase 1 is derived by replaying
these entries in turn order, not independently authored.

---

### Phase 1 — Turn-by-Turn Trace (DEVELOPER)

```
TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE |
SESSION_STATE | CONFORMANCE: CONFORMS|DEVIATES[CONV-NN] |
CONSTRAINT_VERDICTS: CONV-NN→PASS|FAIL|CHAIN_SUSPENDED[...] |
CHAIN_EFFECTS: CONV-NN→[downstream: ACTIVATED|SUSPENDED] |
PREDICTION_MATCH: ON_PATH[PATH_ID]|DEVIATION[PATH_ID,expected,actual]|OFF_ALL_PATHS |
SLOT_FILL: slot→FILLED|SKIPPED|INTERRUPTED (if applicable)
```
Every turn gets a row. No turns skipped. No turns collapsed into summaries.

---

### Phase 1-T — Topic Aggregate (DEVELOPER, additive)

```
TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ |
DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP |
PATH_IDS_MATCHED
```

---

### Phase 2 — Defect Classification (DEVELOPER)

Classify defects in severity order. For each FOUND defect:

```
DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS |
INVARIANT_CITE | REPRODUCTION_STEPS |
RECOVERY: RECOVERABLE[min_turns,target_state]|UNRECOVERABLE[reason] |
ENTANGLEMENT_VERDICT | PLAN_TIER_OVERRIDE (CRITICAL PREDICTION_DEVIATION only)
```

Defect classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHANED_TOPIC, TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION,
CONTRACT_GAP.

CRITICAL-path PREDICTION_DEVIATION defects carry SEVERITY_CLASS: P1 minimum
and PLAN_TIER_OVERRIDE: IMMEDIATE.

For each FOUND P0 defect, emit EXECUTION_HALT before lower-severity defects:

```
EXECUTION_HALT:
  HALT_TRIGGER | ROOT_CAUSE | MVF_RECOMMENDATION | MVF_SCOPE | UNBLOCKED_BY
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN | CHAIN_HEAD_CONV | FIRST_DEVIATE_TURN | SUSPENDED_CONVS |
    BREAK_TO_DEFECT_PATH
  CHAIN_REPAIR: [CONV-NN list]
```

---

### Phase 3-E — Entanglement Map (DEVELOPER)

```
DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[class]|MASKED_BY[class] |
CONDITIONAL_RECOVERY (MASKED_BY defects only)
```

---

### Phase 4 — Fallback, Escalation, Disambiguation (DEVELOPER)

Trace one fallback path to completion (full chain, not first node only).
Trace one escalation path: trigger condition, handoff node, SESSION_STATE at handoff,
agent receipt confirmation.
For each intent collision from Phase 2: propose disambiguation strategy with rationale.

---

### Phase 4-SQ — Status Quo Simulation (DEVELOPER)

Re-run scenario using declared STATUS_QUO_METHOD only. No constraint verdicts, chain
effects, prediction match, timeline anomaly tracking, or chain budget tracking.

```
TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY |
SQ_DEFECT_FOUND: YES|NO | SQ_DEFECT_CLASS | REMARKS
```

```
STATUS_QUO_FINDINGS:
  TOTAL_TURNS: N
  SQ_DEFECTS_FOUND: [class: description, ...]
  SQ_DEFECTS_NOT_FOUND: [populated in Phase 5-F after comparison to Phase 2]
```

---

### Phase 5 — Coverage and Quality (DEVELOPER)

**Phase 5-A — Deviation Budget Utilization**
```
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
```
OVERALL_BUDGET_STATUS: WITHIN_BUDGET|EXCEEDED[violated classes].
If EXCEEDED, emit BUDGET_EXCEEDED_FINDING: VIOLATED_CLASSES | OVER_BY | IMPLICATION.

**Phase 5-B — Chain Budget Utilization**
```
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT |
STATUS: WITHIN_BUDGET|EXCEEDED
```
For each EXCEEDED chain, emit CHAIN_BUDGET_EXCEEDED finding with:
CHAIN_ID | HEAD_CONV | BUDGET | ACTUAL | OVER_BY | FIRST_EXCEED_TURN |
SUSPENDED_CONVS | IMPLICATION.

**Phase 5-C — Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN |
EXECUTION_HALT_REF (if BROKEN and C-38 present)
```

**Phase 5-D — Coverage Quality Gate then Ratios**
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED. Then:
```
RATIO | VALUE (fraction) | STATUS
TOPIC_COVERAGE_RATIO | N/M | CLEAN|PROVISIONAL
TRANSITION_COVERAGE_RATIO | N/M | CLEAN|PROVISIONAL
SLOT_PATH_COVERAGE_RATIO | N/M | CLEAN|PROVISIONAL
TIMELINE_ANOMALY_RATE | N/M | —
PATH_ADHERENCE_RATIO | N/M | CLEAN|PROVISIONAL
```
Numerator and denominator visible in every fraction.

**Phase 5-F — Status Quo Coverage Table**
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION: YES|NO |
FOUND_BY_STATUS_QUO: YES|NO |
DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY|FOUND_BY_BOTH|FOUND_BY_STATUS_QUO_ONLY |
SQ_BLIND_SPOT: [METHOD_BLIND_SPOTS key | N/A]
```
Auto-classification: apply structural rules from declared METHOD_BLIND_SPOTS.
```
STATUS_QUO_GAP_SUMMARY:
  FOUND_BY_SIMULATION_ONLY_COUNT: N
  FOUND_BY_SIMULATION_ONLY_LIST: [DEFECT_IDs]
  STRUCTURAL_BLIND_SPOTS_ACTIVATED: [METHOD_BLIND_SPOTS keys]
  STATUS_QUO_GAP_NARRATIVE: [one paragraph]
```

---

### Phase 6 — Independent Verification (AUDITOR)

**Phase 6-A:**
```
CHECK | RESULT | DETAIL
CONTRACT_AUDIT_GATE_HONORED | PASS|FAIL | —
BUDGET_UTILIZATION_VERIFIED | PASS|FAIL | —
BUDGET_STATUS_CONSISTENT | PASS|FAIL | —
SIMULATION_DELTA_COMPLETE | PASS|FAIL | [uncategorized defects if FAIL]
```

**Phase 6-B — Severity Co-Residency Audit:**
```
DEFECT_ID | SEVERITY_CLASS_PRESENT: YES|NO | INVARIANT_CITE_PRESENT: YES|NO |
VERDICT: PASS|FAIL | EXEMPT: YES|NO
```

**Phase 6-C — Entanglement Consistency Audit:**
```
DEFECT_ID | ENTANGLEMENT_REPORTED | ENTANGLEMENT_AUDITED | CONSISTENT: PASS|FAIL
```

**Phase 6-D — Topic Aggregate Consistency Audit:**
```
TOPIC_ID | CONFORMANCE_ROLLUP_REPORTED | DEVIATES_COUNT_AUDITED |
CONSISTENT: PASS|FAIL | FINDING (if FAIL: TOPIC_ROLLUP_MISMATCH)
```

**Phase 6-E — Session Timeline Consistency Audit:**
```
TURN_ID | SESSION_STATE_REPORTED | SESSION_STATE_RECONSTRUCTED |
CONSISTENT: PASS|FAIL | FINDING (if FAIL: TIMELINE_STATE_MISMATCH)
```

**Phase 6-F — Fix Viability Audit:**
```
EXECUTION_HALT_REF | CONV_VIOLATIONS_INTRODUCED: YES|NO |
CONV_VIOLATIONS_DETAIL | CHAIN_REPAIR_COMPLETE: YES|NO |
VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[CONV-NNs]
```

**Phase 6-G — Chain Integrity Audit:**
```
CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL |
FINDING (if FAIL: CHAIN_VERDICT_INCONSISTENCY)
```

**Phase 6-H — Combined Plan/Path/SQ Coverage Audit:**
```
EXECUTION_HALT_REF | EXECUTION_HALT_IN_PLAN: YES|NO |
CHAIN_REPAIR_IN_SCOPE: YES|NO
```
```
PLAN_ID | DEPENDENCY_ORDER_VALID: YES|NO
```
PLAN_INTEGRITY_AUDIT: PASS|FAIL. DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND.
PLAN_TIER_OVERRIDE_PRESENT: PASS|FAIL. OVERRIDE_TIER_HONORED: PASS|FAIL.
```
TURN_ID | PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED | CONSISTENT: PASS|FAIL
```
PATH_ADHERENCE_RATIO_VERIFIED: PASS|FAIL. CRITICAL_PATH_ESCALATION_VERIFIED: PASS|FAIL.
```
DEFECT_ID | DETECTION_METHOD_REPORTED | DETECTION_METHOD_AUDITED | CONSISTENT: PASS|FAIL
```
AUTOMATIC_CLASSIFICATION_VERIFIED:
  PREDICTION_DEVIATION: PASS|FAIL
  CHAIN_BUDGET_EXCEEDED: PASS|FAIL
  TIMELINE_ANOMALY: PASS|FAIL
STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL

AUDITOR_CERTIFICATION: PASS|FAIL[cite]

---

### Phase 7 — Remediation Plan (REMEDIATION PLANNER)

Execute after AUDITOR_CERTIFICATION.

```
PLAN_ID | DEFECT_REF | SEVERITY_CLASS | SCOPE | DEPENDENCY_ON |
PLAN_TIER: IMMEDIATE|NEXT_SPRINT|BACKLOG | TIER_RATIONALE |
CHAIN_REPAIR_ITEMS | UNBLOCKED_BY
```

Topological sort: no item precedes its DEPENDENCY_ON items. Items with no dependencies
first. P0 before P1 before P2/P3 within a tier. PLAN_TIER_OVERRIDE: IMMEDIATE
(second-priority after P0 → IMMEDIATE, before P1 → NEXT_SPRINT).

```
PLAN_SUMMARY:
  PLAN_ITEM_COUNT: N
  IMMEDIATE_COUNT: N
  NEXT_SPRINT_COUNT: N
  BACKLOG_COUNT: N
  DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND
```

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-03 — Axis H: Imperative Second-Person Register

**Variation axis:** Phrasing register — direct second-person imperative throughout;
no passive constructions; short sentences; explicit prohibition gates.

**Hypothesis:** Imperative register with explicit "do not proceed" gates reduces
interpretive latitude and over-completion better than formal descriptive register.
Shorter sentences make individual requirements harder to miss.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

Five roles execute in order: CONTRACT AUDITOR, TOPOLOGY ARCHITECT, DEVELOPER, AUDITOR,
REMEDIATION PLANNER. Do not begin a phase until the previous phase is complete.

---

### CONTRACT AUDITOR — Pre-check

Issue a pre-flight checklist before the Topology Architect begins. List the ten required
Phase 0 declarations. State which are present and which are missing. Do not begin Phase 0
until you know what to author.

---

### TOPOLOGY ARCHITECT — Phase 0

Author these Phase 0 declarations in order. Do not skip any. Do not begin Phase 1-S
until Phase 0-CA-1 passes.

**Phase 0-D-1.** List every topic: TOPIC_ID, TRIGGER_PHRASES, ENTRY_CONDITIONS, EXIT_TARGETS.
Do not reference a topic in Phase 1 that you have not declared here.

**Phase 0-D-2.** List permitted Copilot Studio terms and prohibited generic chatbot terms.
Sign VOCABULARY_GATE_SIGNED: YES. Do not use prohibited terms in Phase 1.

**Phase 0-D-3.** List every session variable: NAME, PERSISTENCE_CLASS, INITIAL_VALUE.
Do not reference a variable in Phase 1 SESSION_STATE that you have not declared here.

**Phase 0-D-4.** List every invariant: CONV-NN, DESCRIPTION, FALSIFICATION_CONDITION,
PROPAGATION (downstream CONV-NNs), CHAIN_ID. Assign every CONV-NN to exactly one chain.

**Phase 0-D-5.** List every graph edge: TRANS-NN, SOURCE_TOPIC, TARGET_TOPIC, CONDITION,
REQUIRED|OPTIONAL.

**Phase 0-A-6.** For every variable in Phase 0-D-3, declare: FIRST_WRITTEN_TOPIC,
CLEARED_BY, READ_AFTER_CLEARED (FORBIDDEN|ALLOWED), AUTHORIZED_REWRITERS. Do not
write a variable from a topic absent from both FIRST_WRITTEN_TOPIC and
AUTHORIZED_REWRITERS; that is an OFF_CONTRACT_WRITE anomaly.

**Phase 0-A-7.** For every CHAIN_ID you used in Phase 0-D-4, declare: CHAIN_ID,
HEAD_CONV, CHAIN_LENGTH, PROPAGATION_SEQUENCE.

**Phase 0-A-8.** Declare your deviation budget: P0_MAX, P1_MAX, P2_MAX, P3_MAX,
BUDGET_RATIONALE. Write "BUDGET LOCKED — may not be revised after Phase 1-S begins."
Do not change these numbers after you have seen Phase 1 output.

**Phase 0-A-9.** For every chain in Phase 0-A-7, declare: CHAIN_ID, HEAD_CONV,
CHAIN_LENGTH, CHAIN_BUDGET, BUDGET_RATIONALE. Do not leave any chain without a budget.

**Phase 0-A-10.** Declare your turn prediction contract. Write one HAPPY_PATH (required)
and up to three ALT_PATHs. For each: PATH_ID, PATH_DESCRIPTION,
PATH_CRITICALITY (CRITICAL|IMPORTANT|INFORMATIONAL), PREDICTED_TURN_SEQUENCE.
Sign TURN_PREDICTION_CONTRACT_SIGNED: YES. Do not begin Phase 1 without this signature.

**Phase 0-A-11.** Declare the team's current informal review method. Write METHOD_NAME,
METHOD_DESCRIPTION, METHOD_COVERAGE. Then fill in METHOD_BLIND_SPOTS with YES|NO for
each: CONSTRAINT_VERDICTS, CHAIN_EFFECTS, TIMELINE_ANOMALIES, PREDICTION_CONTRACT,
CHAIN_BUDGET. Write each YES|NO explicitly. Do not substitute a prose description for
the structured checklist. Sign STATUS_QUO_METHOD_SIGNED: YES.

---

### CONTRACT AUDITOR — Phase 0-CA-1 (blocking gate)

Do this before Phase 1 begins. Do not let Phase 1 start until GATE_STATUS: PASS.

Compute COVERAGE_DELTA: count variables in Phase 0-D-1 topology missing from Phase 0-A-6.
Compute CHAIN_BUDGET_DELTA: count chains in Phase 0-A-7 missing from Phase 0-A-9.
Check PREDICTION_CONTRACT_SIGNED: YES|NO.
Check STATUS_QUO_METHOD_SIGNED: YES|NO.
Check BLIND_SPOTS_CHECKLIST_PRESENT: YES|NO.

Emit GATE_STATUS: PASS only when all deltas are empty and all signatures are YES.
Emit GATE_STATUS: BLOCKED and name the blocking condition otherwise.

---

### DEVELOPER — Phase 1-S (author before Phase 1)

Author the mutation log before you write Phase 1. For every turn, for every non-null
session variable, record: VARIABLE_NAME, TURN_ID, MUTATION_TYPE (WRITE|READ|CLEAR|
NO_CHANGE), VALUE_AFTER. Derive Phase 1 SESSION_STATE by replaying these entries.
Do not independently author SESSION_STATE.

---

### DEVELOPER — Phase 1 (turn-by-turn trace)

Walk every turn. Emit one row per turn. Do not skip turns. Do not collapse turns into
summaries.

Each row must carry all of these columns:
TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE |
SESSION_STATE | CONFORMANCE | CONSTRAINT_VERDICTS | CHAIN_EFFECTS | PREDICTION_MATCH |
SLOT_FILL (if applicable)

Fill CONFORMANCE: CONFORMS or DEVIATES[CONV-NN]. Cite the CONV-NN by its registered ID.
Fill CONSTRAINT_VERDICTS: list every CONV-NN evaluated, with PASS|FAIL|CHAIN_SUSPENDED.
Fill CHAIN_EFFECTS: for each CONV-NN with downstream propagation, list
CONV-NN → [downstream: ACTIVATED|SUSPENDED].
Fill PREDICTION_MATCH: ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual],
or OFF_ALL_PATHS.
Do not use prohibited terms from Phase 0-D-2.

---

### DEVELOPER — Phase 1-T (topic aggregate, additive)

Write one row per topic visited. Do not replace Phase 1 with this table. Add it after
Phase 1. Include: TOPIC_ID, TURNS_VISITED, SESSION_VARIABLES_SET, SESSION_VARIABLES_READ,
DEFECT_CITATIONS, ADVERSARIAL_INJECTION_COUNT, CONFORMANCE_ROLLUP, PATH_IDS_MATCHED.

---

### DEVELOPER — Phase 2 (defect classification)

Classify every defect you found. Use these nine classes: DEAD_END, INFINITE_LOOP,
INTENT_COLLISION, MISSING_FALLBACK, ORPHANED_TOPIC, TIMELINE_ANOMALY,
CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP.

For each FOUND defect write: DEFECT_ID, DEFECT_CLASS, LOCATION, SEVERITY_CLASS,
INVARIANT_CITE, REPRODUCTION_STEPS, RECOVERY, ENTANGLEMENT_VERDICT.

Do not leave any defect without both SEVERITY_CLASS and INVARIANT_CITE.
Do not leave ENTANGLEMENT_VERDICT blank; set it to ISOLATED, ENABLES[class], or
MASKED_BY[class].

When you find a CRITICAL-path PREDICTION_DEVIATION defect: set SEVERITY_CLASS to P1
minimum even if you think the inherent severity is lower. Add
PLAN_TIER_OVERRIDE: IMMEDIATE and PLAN_TIER_OVERRIDE_ANNOTATION:
"CRITICAL path deviation — overrides severity-based tier."

When you find a P0 defect: emit EXECUTION_HALT before you classify anything lower.
Write: HALT_TRIGGER, ROOT_CAUSE (one sentence), MVF_RECOMMENDATION, MVF_SCOPE,
UNBLOCKED_BY. Then write CHAIN_BREAK_TRACE: BROKEN_CHAIN, CHAIN_HEAD_CONV,
FIRST_DEVIATE_TURN, SUSPENDED_CONVS, BREAK_TO_DEFECT_PATH. Then write CHAIN_REPAIR:
list every CONV-NN that must be re-evaluated after the fix.

---

### DEVELOPER — Phase 3-E (entanglement map)

Assign every FOUND defect an ENTANGLEMENT_VERDICT. Do not leave any FOUND defect
without one. MASKED_BY defects must have conditional recovery verdicts in Phase 2.

---

### DEVELOPER — Phase 4 (fallback, escalation, disambiguation)

Trace one fallback path to completion. Show every node in the chain. Do not stop at
the first fallback node.

Trace one escalation path. Show: trigger condition, handoff node name, SESSION_STATE
at handoff, and agent receipt confirmation. If no escalation topic is declared in
Phase 0-D-1, write ESCALATION: CONFIRMED_ABSENT.

For each intent collision from Phase 2: propose a disambiguation strategy and explain
why it works.

Inject at least one adversarial utterance mid-conversation. Record: TURN_ID, utterance,
system response, any defect triggered, recovery path to completion.

---

### DEVELOPER — Phase 4-SQ (status quo simulation)

Re-run the same conversation using only the METHOD described in Phase 0-A-11.
Do not apply CONSTRAINT_VERDICTS. Do not apply CHAIN_EFFECTS. Do not track
PREDICTION_MATCH. Do not track TIMELINE_ANOMALIES. Do not track CHAIN_BUDGET.
Apply only the capabilities of the declared informal method.

For each turn write: TURN_ID, TOPIC_MATCHED, AGENT_RESPONSE_SUMMARY,
SQ_DEFECT_FOUND (YES|NO), SQ_DEFECT_CLASS (if found), REMARKS.

Close with STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND list,
SQ_DEFECTS_NOT_FOUND (fill this after you complete Phase 5-F).

---

### DEVELOPER — Phase 5 (coverage and quality)

**Phase 5-A.** Report deviation budget utilization. For each severity class: BUDGET,
ACTUAL_DEVIATES, STATUS. State OVERALL_BUDGET_STATUS. If EXCEEDED, emit
BUDGET_EXCEEDED_FINDING: VIOLATED_CLASSES, OVER_BY, IMPLICATION.

**Phase 5-B.** Report chain budget utilization. For each chain: CHAIN_BUDGET,
HEAD_DEVIATES_COUNT, STATUS. If a chain EXCEEDED, emit a CHAIN_BUDGET_EXCEEDED finding.
Include: CHAIN_ID, HEAD_CONV, BUDGET, ACTUAL, OVER_BY, FIRST_EXCEED_TURN,
SUSPENDED_CONVS, IMPLICATION.

**Phase 5-C.** Summarize constraint chain status. One row per chain: CHAIN_ID,
HEAD_CONV, CHAIN_LENGTH, TURNS_SUSPENDED, FINAL_STATUS (INTACT|BROKEN).
Cross-reference BROKEN chains to their EXECUTION_HALT block.

**Phase 5-D.** Write COVERAGE_QUALITY_GATE: CLEAN or DEGRADED before you write any
ratio. DEGRADED if TIMELINE_ANOMALY_RATE > 0. Under DEGRADED, mark every ratio
PROVISIONAL. Then write all five ratios with numerator and denominator visible:
TOPIC_COVERAGE_RATIO, TRANSITION_COVERAGE_RATIO, SLOT_PATH_COVERAGE_RATIO,
TIMELINE_ANOMALY_RATE, PATH_ADHERENCE_RATIO. Do not omit the COVERAGE_QUALITY_GATE
headline.

**Phase 5-F.** Build the STATUS_QUO_COVERAGE table. For each FOUND defect from Phase 2,
write one row: DEFECT_ID, DEFECT_CLASS, FOUND_BY_SIMULATION, FOUND_BY_STATUS_QUO,
DETECTION_METHOD, SQ_BLIND_SPOT.

Apply auto-classification rules from your METHOD_BLIND_SPOTS declaration:
- PREDICTION_DEVIATION: FOUND_BY_SIMULATION_ONLY when PREDICTION_CONTRACT: NO
- CHAIN_BUDGET_EXCEEDED: FOUND_BY_SIMULATION_ONLY when CHAIN_BUDGET: NO
- TIMELINE_ANOMALY: FOUND_BY_SIMULATION_ONLY when TIMELINE_ANOMALIES: NO

Write STATUS_QUO_GAP_SUMMARY: FOUND_BY_SIMULATION_ONLY_COUNT,
FOUND_BY_SIMULATION_ONLY_LIST, STRUCTURAL_BLIND_SPOTS_ACTIVATED,
STATUS_QUO_GAP_NARRATIVE (one paragraph). Return to Phase 4-SQ and fill in
SQ_DEFECTS_NOT_FOUND now that you have this table.

---

### AUDITOR — Phase 6 (independent verification)

Do not modify any Developer rows. Record discrepancies as findings.

**Phase 6-A.** Verify: CONTRACT_AUDIT_GATE_HONORED, BUDGET_UTILIZATION_VERIFIED,
BUDGET_STATUS_CONSISTENT, SIMULATION_DELTA_COMPLETE. Mark PASS or FAIL for each.

**Phase 6-B.** Check every FOUND defect row for SEVERITY_CLASS and INVARIANT_CITE.
Both must be present. Produce a table. Mark each row PASS or FAIL. EXEMPT rows
are CONFIRMED_ABSENT only.

**Phase 6-C.** Verify Phase 3-E ENTANGLEMENT_MAP against Phase 1 evidence.

**Phase 6-D.** Cross-check Phase 1-T CONFORMANCE_ROLLUP against Phase 1 DEVIATES count
per topic. Mark any mismatch TOPIC_ROLLUP_MISMATCH.

**Phase 6-E.** Replay Phase 1-S mutations. Compare reconstructed SESSION_STATE to Phase 1
SESSION_STATE at every turn. Mark any discrepancy TIMELINE_STATE_MISMATCH.

**Phase 6-F.** For each EXECUTION_HALT block: verify CONV_VIOLATIONS_INTRODUCED and
CHAIN_REPAIR_COMPLETE. Mark VIABLE or SIDE_EFFECTS_FOUND.

**Phase 6-G.** For each chain: verify CHAIN_EFFECTS in Phase 1 against upstream CONV-NN
verdicts. Mark any CONFORMS verdict during a SUSPENDED chain window as
CHAIN_VERDICT_INCONSISTENCY.

**Phase 6-H.** Run three sub-audits:
1. Plan integrity: verify every EXECUTION_HALT has a PLAN_ITEM; verify CHAIN_REPAIR
   coverage; verify topological order; check for dependency cycles; verify
   PLAN_TIER_OVERRIDE_PRESENT and OVERRIDE_TIER_HONORED.
2. Path adherence: verify every PREDICTION_MATCH verdict per turn against the contract;
   verify PATH_ADHERENCE_RATIO; verify CRITICAL_PATH_ESCALATION (P1 minimum on all
   CRITICAL deviations).
3. Status quo coverage: verify DETECTION_METHOD per defect; verify
   AUTOMATIC_CLASSIFICATION for PREDICTION_DEVIATION, CHAIN_BUDGET_EXCEEDED,
   TIMELINE_ANOMALY. Mark STATUS_QUO_COVERAGE_AUDIT: PASS or FAIL.

Close with AUDITOR_CERTIFICATION: PASS or FAIL. List every blocking finding if FAIL.

---

### REMEDIATION PLANNER — Phase 7

Do not begin until AUDITOR_CERTIFICATION is written. Read Phase 2 EXECUTION_HALT blocks
and Phase 3-E ENTANGLEMENT_MAP.

Write one PLAN_ITEM per FOUND defect. For each: PLAN_ID (RP-NN), DEFECT_REF,
SEVERITY_CLASS, SCOPE, DEPENDENCY_ON, PLAN_TIER, TIER_RATIONALE, CHAIN_REPAIR_ITEMS,
UNBLOCKED_BY.

Tier rules in priority order:
1. P0 → IMMEDIATE
2. PLAN_TIER_OVERRIDE: IMMEDIATE (CRITICAL path PREDICTION_DEVIATION) → IMMEDIATE
3. P1 → NEXT_SPRINT
4. P2/P3 → BACKLOG

Do not place any item before its DEPENDENCY_ON items. Place items with no dependencies
first. Within a tier, place P0 before P1 before P2/P3.

Close with PLAN_SUMMARY: PLAN_ITEM_COUNT, IMMEDIATE_COUNT, NEXT_SPRINT_COUNT,
BACKLOG_COUNT, DEPENDENCY_CYCLE_CHECK.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-04 — Axes F+G: Role Sequence + Table-First Format

**Variation axes:** Role sequence (Contract Auditor as hard blocking role) combined
with table-first output format (every role handoff is a structured table).

**Hypothesis:** Making every role boundary a structured table handoff — the Contract
Auditor passes a gate table to the Developer, the Developer passes a defect catalog
table to the Planner — produces artifacts that are more machine-verifiable and harder
to partially satisfy than prose-described phases.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

This skill uses five roles. Each role receives a structured input table from the
previous role and produces a structured output table as its primary artifact. The
role handoff IS the table. Prose is supplementary.

---

### ROLE 1 — CONTRACT AUDITOR (Phase 0-CA-0: pre-flight)

Before any Phase 0 declarations are authored, the Contract Auditor issues this gate
table to the Topology Architect:

```
REQUIRED_DECLARATION | PHASE_REF | STATUS: PENDING
Topic Registry | Phase 0-D-1 | PENDING
Vocabulary Gate | Phase 0-D-2 | PENDING
Session Variable Registry | Phase 0-D-3 | PENDING
Invariant Register | Phase 0-D-4 | PENDING
Transition Map | Phase 0-D-5 | PENDING
Session Variable Timeline Contract | Phase 0-A-6 | PENDING
Chain Declaration | Phase 0-A-7 | PENDING
Deviation Budget | Phase 0-A-8 | PENDING
Constraint Chain Budget | Phase 0-A-9 | PENDING
Turn Prediction Contract | Phase 0-A-10 | PENDING
Status Quo Method | Phase 0-A-11 | PENDING
```

The Topology Architect authors all declarations against this manifest. The Contract
Auditor then evaluates Phase 0-CA-1.

---

### ROLE 2 — TOPOLOGY ARCHITECT (Phase 0 declarations)

Author each declaration as a table. The table schema is the specification.

**Phase 0-D-1:**
`TOPIC_ID | TRIGGER_PHRASES | ENTRY_CONDITIONS | EXIT_TARGETS`

**Phase 0-D-2:**
`TERM | CLASS: PERMITTED|PROHIBITED | RATIONALE`
Sign: VOCABULARY_GATE_SIGNED: YES

**Phase 0-D-3:**
`NAME | PERSISTENCE_CLASS | INITIAL_VALUE`

**Phase 0-D-4:**
`CONV-NN | DESCRIPTION | FALSIFICATION_CONDITION | PROPAGATION | CHAIN_ID`

**Phase 0-D-5:**
`TRANS-NN | SOURCE_TOPIC | TARGET_TOPIC | CONDITION | REQUIRED|OPTIONAL`

**Phase 0-A-6:**
`VARIABLE | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED | AUTHORIZED_REWRITERS`

**Phase 0-A-7:**
`CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | PROPAGATION_SEQUENCE`

**Phase 0-A-8:**
`SEVERITY | MAX_DEVIATES_ALLOWED | BUDGET_RATIONALE`
Lock: "BUDGET LOCKED — may not be revised after Phase 1-S begins."

**Phase 0-A-9:**
`CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | CHAIN_BUDGET | BUDGET_RATIONALE`

**Phase 0-A-10:**
`PATH_ID | PATH_DESCRIPTION | PATH_CRITICALITY | PREDICTED_TURN_SEQUENCE`
Sign: TURN_PREDICTION_CONTRACT_SIGNED: YES

**Phase 0-A-11:**
```
FIELD | VALUE
METHOD_NAME | [label]
METHOD_DESCRIPTION | [paragraph]
METHOD_COVERAGE | [what the method checks]
BLIND_SPOT: CONSTRAINT_VERDICTS | YES|NO
BLIND_SPOT: CHAIN_EFFECTS | YES|NO
BLIND_SPOT: TIMELINE_ANOMALIES | YES|NO
BLIND_SPOT: PREDICTION_CONTRACT | YES|NO
BLIND_SPOT: CHAIN_BUDGET | YES|NO
STATUS_QUO_METHOD_SIGNED | YES
```

---

### ROLE 1 — CONTRACT AUDITOR (Phase 0-CA-1: blocking gate)

Evaluate the Topology Architect's output. Update the pre-flight manifest:

```
REQUIRED_DECLARATION | PHASE_REF | STATUS: COMPLETE|MISSING | DELTA_ITEM
Topic Registry | Phase 0-D-1 | — | —
...
```

Then compute the four blocking conditions:

```
BLOCKING_CHECK | RESULT | DETAIL
COVERAGE_DELTA | EMPTY|[missing vars] | vars in 0-D-1 topology missing from 0-A-6
CHAIN_BUDGET_DELTA | EMPTY|[missing chains] | chains in 0-A-7 missing from 0-A-9
PREDICTION_CONTRACT_SIGNED | YES|NO | —
STATUS_QUO_METHOD_SIGNED + CHECKLIST | YES|NO | —
GATE_STATUS | PASS|BLOCKED | [reason if BLOCKED]
```

Hand GATE_STATUS: PASS to the Developer before Phase 1-S begins.

---

### ROLE 3 — DEVELOPER (Phases 1-S through 5)

Receive GATE_STATUS: PASS from the Contract Auditor. Do not begin without it.

**Phase 1-S — Mutation Log (author first):**
`VARIABLE_NAME | TURN_ID | MUTATION_TYPE | VALUE_AFTER`

**Phase 1 — Turn Trace:**
`TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE | SESSION_STATE | CONFORMANCE | CONSTRAINT_VERDICTS | CHAIN_EFFECTS | PREDICTION_MATCH | SLOT_FILL`

SESSION_STATE derived from Phase 1-S replay. Every turn gets a row.

**Phase 1-T — Topic Aggregate (additive):**
`TOPIC_ID | TURNS_VISITED | SESSION_VARIABLES_SET | SESSION_VARIABLES_READ | DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP | PATH_IDS_MATCHED`

**Phase 2 — Defect Catalog:**
`DEFECT_ID | DEFECT_CLASS | LOCATION | SEVERITY_CLASS | INVARIANT_CITE | REPRODUCTION_STEPS | RECOVERY | ENTANGLEMENT_VERDICT | PLAN_TIER_OVERRIDE`

For P0 defects: emit EXECUTION_HALT block (HALT_TRIGGER | ROOT_CAUSE | MVF_RECOMMENDATION | MVF_SCOPE | UNBLOCKED_BY | CHAIN_BREAK_TRACE | CHAIN_REPAIR) before lower-severity defects.

CRITICAL PREDICTION_DEVIATION defects carry SEVERITY_CLASS: P1 minimum and
PLAN_TIER_OVERRIDE: IMMEDIATE.

**Phase 3-E — Entanglement Map:**
`DEFECT_ID | ENTANGLEMENT_VERDICT | CONDITIONAL_RECOVERY`

**Phase 4 — Fallback/Escalation/Disambiguation:**
Trace one complete fallback chain. Trace one complete escalation path. Propose
disambiguation for each intent collision. Inject one adversarial turn; trace recovery.

**Phase 4-SQ — Status Quo Simulation:**
`TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND | SQ_DEFECT_CLASS | REMARKS`
Close: `STATUS_QUO_FINDINGS: TOTAL_TURNS | SQ_DEFECTS_FOUND | SQ_DEFECTS_NOT_FOUND`

**Phase 5-A — Deviation Budget Utilization:**
`SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS`
OVERALL_BUDGET_STATUS. BUDGET_EXCEEDED_FINDING if EXCEEDED.

**Phase 5-B — Chain Budget Utilization:**
`CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS`
CHAIN_BUDGET_EXCEEDED findings for exceeded chains.

**Phase 5-C — Chain Status Summary:**
`CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS | EXECUTION_HALT_REF`

**Phase 5-D — Coverage Quality Gate + Ratios:**
COVERAGE_QUALITY_GATE: CLEAN|DEGRADED.
`RATIO | FRACTION (N/M) | STATUS: CLEAN|PROVISIONAL`
Five ratios: TOPIC_COVERAGE, TRANSITION_COVERAGE, SLOT_PATH_COVERAGE,
TIMELINE_ANOMALY_RATE, PATH_ADHERENCE_RATIO.

**Phase 5-F — Status Quo Coverage Table:**
`DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION | FOUND_BY_STATUS_QUO | DETECTION_METHOD | SQ_BLIND_SPOT`
Auto-classify from declared METHOD_BLIND_SPOTS. Close: STATUS_QUO_GAP_SUMMARY table
(FOUND_BY_SIMULATION_ONLY_COUNT | FOUND_BY_SIMULATION_ONLY_LIST |
STRUCTURAL_BLIND_SPOTS_ACTIVATED | STATUS_QUO_GAP_NARRATIVE).

Hand Phase 2 Defect Catalog and Phase 3-E Entanglement Map to REMEDIATION PLANNER.
Hand Phase 5 output to AUDITOR.

---

### ROLE 4 — AUDITOR (Phase 6: independent verification)

Receive Developer output. Produce one verification table per sub-phase. Do not modify
Developer rows.

**Phase 6-A:**
`CHECK | RESULT: PASS|FAIL | DETAIL`
(CONTRACT_AUDIT_GATE_HONORED, BUDGET_UTILIZATION_VERIFIED, BUDGET_STATUS_CONSISTENT,
SIMULATION_DELTA_COMPLETE)

**Phase 6-B:**
`DEFECT_ID | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | VERDICT | EXEMPT`

**Phase 6-C:**
`DEFECT_ID | ENTANGLEMENT_REPORTED | ENTANGLEMENT_AUDITED | CONSISTENT`

**Phase 6-D:**
`TOPIC_ID | CONFORMANCE_ROLLUP_REPORTED | DEVIATES_COUNT_AUDITED | CONSISTENT`

**Phase 6-E:**
`TURN_ID | SESSION_STATE_REPORTED | SESSION_STATE_RECONSTRUCTED | CONSISTENT`

**Phase 6-F:**
`EXECUTION_HALT_REF | CONV_VIOLATIONS_INTRODUCED | CONV_VIOLATIONS_DETAIL | CHAIN_REPAIR_COMPLETE | VIABILITY`

**Phase 6-G:**
`CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT`

**Phase 6-H (combined):**
Plan: `EXECUTION_HALT_REF | EXECUTION_HALT_IN_PLAN | CHAIN_REPAIR_IN_SCOPE`
Plan: `PLAN_ID | DEPENDENCY_ORDER_VALID`
PLAN_INTEGRITY_AUDIT: PASS|FAIL. DEPENDENCY_CYCLE_CHECK. PLAN_TIER_OVERRIDE_PRESENT.
OVERRIDE_TIER_HONORED.

Path: `TURN_ID | PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED | CONSISTENT`
PATH_ADHERENCE_RATIO_VERIFIED. CRITICAL_PATH_ESCALATION_VERIFIED.

SQ: `DEFECT_ID | DETECTION_METHOD_REPORTED | DETECTION_METHOD_AUDITED | CONSISTENT`
AUTOMATIC_CLASSIFICATION_VERIFIED (three classes). STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL.

AUDITOR_CERTIFICATION: PASS|FAIL[cite].

---

### ROLE 5 — REMEDIATION PLANNER (Phase 7)

Receive Phase 2 Defect Catalog and Phase 3-E Entanglement Map. Wait for
AUDITOR_CERTIFICATION before producing the plan.

Produce one PLAN_ITEM per FOUND defect:
`PLAN_ID | DEFECT_REF | SEVERITY_CLASS | SCOPE | DEPENDENCY_ON | PLAN_TIER | TIER_RATIONALE | CHAIN_REPAIR_ITEMS | UNBLOCKED_BY`

Tier priority: P0 → IMMEDIATE; PLAN_TIER_OVERRIDE: IMMEDIATE (CRITICAL deviations) → IMMEDIATE;
P1 → NEXT_SPRINT; P2/P3 → BACKLOG.
Topological sort: no item before its DEPENDENCY_ON items.

```
PLAN_SUMMARY:
PLAN_ITEM_COUNT | IMMEDIATE_COUNT | NEXT_SPRINT_COUNT | BACKLOG_COUNT | DEPENDENCY_CYCLE_CHECK
```

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-05 — Axes H + Inertia: Imperative Register + Status-Quo Framing

**Variation axes:** Phrasing register (imperative second-person) combined with inertia
framing (status-quo failure case as opening motivation, STATUS_QUO_SIMULATION
front-loaded as the evidential core).

**Hypothesis:** Opening with the concrete failure case of informal review — naming what
it structurally cannot see — and maintaining imperative register throughout produces
stronger adoption motivation alongside technical rigor. The status-quo gap is the
reason to run this skill; making it visible first shapes how every subsequent phase
is read.

---

You are simulating a multi-turn Copilot Studio conversation flow for the topic: **{topic}**.

**Why this skill exists:** Your team's current informal review method has structural
blind spots. It catches what is visually obvious in a walk-through. It does not check
whether every conversation invariant holds at every turn. It does not trace how a
violated constraint suspends downstream logic. It does not verify that session variables
are written by authorized topics only. It does not compare the actual conversation path
to a pre-declared expected path. It does not count how many times a constraint chain
head deviates before the conversation ends. This skill makes those gaps structural and
visible, not asserted.

The STATUS_QUO_METHOD declaration (Phase 0-A-11) and the STATUS_QUO_SIMULATION
(Phase 4-SQ) are the mechanism: you declare what your informal method does, run it
in parallel, and prove which defects it misses and why.

Five roles execute in order: CONTRACT AUDITOR, TOPOLOGY ARCHITECT, DEVELOPER, AUDITOR,
REMEDIATION PLANNER.

---

### Phase 0-A-11 — Declare the Status Quo Method (TOPOLOGY ARCHITECT, do this first)

Declare this before any other Phase 0 declaration. It frames why everything else matters.

Write METHOD_NAME: a short label for the team's current informal review practice.
Write METHOD_DESCRIPTION: one paragraph describing what your team does today — manual
walk-through, reading the topic graph, desk review, whatever it is.
Write METHOD_COVERAGE: list what this method naturally checks.
Then fill in METHOD_BLIND_SPOTS with YES or NO for each dimension:
  CONSTRAINT_VERDICTS — does the method check per-invariant verdicts for every turn?
  CHAIN_EFFECTS — does the method trace how a violated constraint suspends downstream logic?
  TIMELINE_ANOMALIES — does the method check variable write/read/clear ordering?
  PREDICTION_CONTRACT — does the method compare actual path to a declared expected path?
  CHAIN_BUDGET — does the method count how many turns a constraint chain head deviates?

Write each YES or NO explicitly. Do not write a prose paragraph instead of the checklist.
Sign STATUS_QUO_METHOD_SIGNED: YES.

These YES|NO answers drive the automatic defect classification in Phase 5-F. Every NO
becomes a structural blind spot that maps directly to at least one defect class that only
this skill can catch.

---

### Phase 0 — Remaining Pre-Execution Declarations (TOPOLOGY ARCHITECT)

Now author the remaining Phase 0 declarations. Each is a pre-execution commitment.
Nothing you reference in Phase 1–7 may be absent here.

**Phase 0-D-1 — Topic Registry:** TOPIC_ID, TRIGGER_PHRASES, ENTRY_CONDITIONS, EXIT_TARGETS.
**Phase 0-D-2 — Vocabulary Gate:** permitted Copilot Studio terms, prohibited generic terms.
  Sign VOCABULARY_GATE_SIGNED: YES.
**Phase 0-D-3 — Session Variable Registry:** NAME, PERSISTENCE_CLASS, INITIAL_VALUE.
**Phase 0-D-4 — Invariant Register:** CONV-NN, DESCRIPTION, FALSIFICATION_CONDITION,
  PROPAGATION (downstream CONV-NNs), CHAIN_ID. Every CONV-NN belongs to exactly one chain.
**Phase 0-D-5 — Transition Map:** TRANS-NN, SOURCE_TOPIC, TARGET_TOPIC, CONDITION, REQUIRED|OPTIONAL.
**Phase 0-A-6 — Session Variable Timeline Contract:** VARIABLE, FIRST_WRITTEN_TOPIC,
  CLEARED_BY, READ_AFTER_CLEARED (FORBIDDEN|ALLOWED), AUTHORIZED_REWRITERS. Every
  variable from Phase 0-D-3 gets a row. A write from an unauthorized topic is an
  OFF_CONTRACT_WRITE anomaly.
**Phase 0-A-7 — Chain Declaration:** CHAIN_ID, HEAD_CONV, CHAIN_LENGTH,
  PROPAGATION_SEQUENCE for every CHAIN_ID used in Phase 0-D-4.
**Phase 0-A-8 — Deviation Budget:** P0_MAX, P1_MAX, P2_MAX, P3_MAX, BUDGET_RATIONALE.
  Write "BUDGET LOCKED" before Phase 1-S begins. Do not change these after seeing results.
**Phase 0-A-9 — Constraint Chain Budget:** CHAIN_ID, HEAD_CONV, CHAIN_LENGTH,
  CHAIN_BUDGET, BUDGET_RATIONALE for every chain.
**Phase 0-A-10 — Turn Prediction Contract:** One HAPPY_PATH (required) and up to three
  ALT_PATHs. For each: PATH_ID, PATH_DESCRIPTION, PATH_CRITICALITY
  (CRITICAL|IMPORTANT|INFORMATIONAL), PREDICTED_TURN_SEQUENCE (ordered TOPIC_IDs).
  CRITICAL paths declare core business transactions; any deviation from them auto-elevates
  to P1 severity. Sign TURN_PREDICTION_CONTRACT_SIGNED: YES.

---

### CONTRACT AUDITOR — Phase 0-CA-1 (blocking gate)

Compute four blocking conditions. Do not begin Phase 1 until all pass.

COVERAGE_DELTA: variables in Phase 0-D-1 topology missing from Phase 0-A-6.
CHAIN_BUDGET_DELTA: chains in Phase 0-A-7 missing from Phase 0-A-9.
PREDICTION_CONTRACT check: PREDICTION_CONTRACT_SIGNED: YES|NO.
STATUS_QUO_METHOD check: STATUS_QUO_METHOD_SIGNED: YES|NO and
BLIND_SPOTS_CHECKLIST_PRESENT: YES|NO.

Emit GATE_STATUS: PASS when all deltas are empty and all signatures are YES.
Emit GATE_STATUS: BLOCKED and name the condition otherwise.

---

### DEVELOPER — Phase 1-S (mutation log, author before Phase 1)

Author the mutation log first. Do not write Phase 1 SESSION_STATE independently.
For every turn and every non-null variable: VARIABLE_NAME, TURN_ID,
MUTATION_TYPE (WRITE|READ|CLEAR|NO_CHANGE), VALUE_AFTER.
Derive SESSION_STATE by replaying these entries in order.

---

### DEVELOPER — Phase 1 (turn trace)

Walk every turn. One row per turn. Do not skip. Do not summarize groups of turns.
Every row: TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED |
AGENT_RESPONSE | SESSION_STATE | CONFORMANCE | CONSTRAINT_VERDICTS | CHAIN_EFFECTS |
PREDICTION_MATCH | SLOT_FILL.

CONFORMANCE: CONFORMS or DEVIATES[CONV-NN]. Cite registered IDs only.
CONSTRAINT_VERDICTS: every CONV-NN evaluated this turn, marked PASS|FAIL|CHAIN_SUSPENDED.
CHAIN_EFFECTS: for each CONV-NN with propagation, list downstream ACTIVATED or SUSPENDED.
PREDICTION_MATCH: ON_PATH[PATH_ID], DEVIATION[PATH_ID, expected, actual], or OFF_ALL_PATHS.
Do not use prohibited vocabulary.

---

### DEVELOPER — Phase 1-T (topic aggregate, additive to Phase 1)

One row per topic: TOPIC_ID, TURNS_VISITED, SESSION_VARIABLES_SET, SESSION_VARIABLES_READ,
DEFECT_CITATIONS, ADVERSARIAL_INJECTION_COUNT, CONFORMANCE_ROLLUP, PATH_IDS_MATCHED.

---

### DEVELOPER — Phase 2 (defect classification)

Classify every defect in severity order (P0 first). Nine defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHANED_TOPIC,
TIMELINE_ANOMALY, CHAIN_BUDGET_EXCEEDED, PREDICTION_DEVIATION, CONTRACT_GAP.

Each FOUND defect: DEFECT_ID, DEFECT_CLASS, LOCATION, SEVERITY_CLASS, INVARIANT_CITE,
REPRODUCTION_STEPS, RECOVERY, ENTANGLEMENT_VERDICT.

When you find a CRITICAL-path PREDICTION_DEVIATION: set SEVERITY_CLASS to P1 minimum.
Add PLAN_TIER_OVERRIDE: IMMEDIATE. This defect enters the remediation plan at IMMEDIATE
tier regardless of severity — a broken critical path is adoption-blocking.

When you find a P0 defect: emit EXECUTION_HALT before classifying lower-severity defects.
Write HALT_TRIGGER, ROOT_CAUSE (one sentence), MVF_RECOMMENDATION, MVF_SCOPE,
UNBLOCKED_BY. Then CHAIN_BREAK_TRACE (BROKEN_CHAIN, CHAIN_HEAD_CONV,
FIRST_DEVIATE_TURN, SUSPENDED_CONVS, BREAK_TO_DEFECT_PATH). Then CHAIN_REPAIR
(CONV-NNs to re-evaluate after fix).

---

### DEVELOPER — Phase 3-E (entanglement map)

Assign every FOUND defect: ENTANGLEMENT_VERDICT (ISOLATED | ENABLES[class] |
MASKED_BY[class]). MASKED_BY defects carry conditional recovery verdicts in Phase 2.

---

### DEVELOPER — Phase 4 (fallback, escalation, disambiguation)

Trace one fallback path to completion. Show the full chain.
Trace one escalation path: trigger condition, handoff node, SESSION_STATE at handoff,
agent receipt confirmation.
Propose a disambiguation strategy for each intent collision.
Inject one adversarial utterance. Record TURN_ID, utterance, response, defect triggered
(if any), recovery path.

---

### DEVELOPER — Phase 4-SQ (status quo simulation)

This is the heart of the adoption case. Re-run the same scenario using ONLY the
STATUS_QUO_METHOD you declared in Phase 0-A-11. Pretend you cannot see constraint
verdicts, chain effects, prediction matching, timeline anomalies, or chain budgets.
Apply only the informal method.

For each turn: TURN_ID, TOPIC_MATCHED, AGENT_RESPONSE_SUMMARY,
SQ_DEFECT_FOUND (YES|NO), SQ_DEFECT_CLASS (if found), REMARKS.

Write STATUS_QUO_FINDINGS: TOTAL_TURNS, SQ_DEFECTS_FOUND (list),
SQ_DEFECTS_NOT_FOUND (fill after Phase 5-F).

The defects in SQ_DEFECTS_NOT_FOUND are the defects your team currently ships without
knowing. Phase 5-F makes them explicit.

---

### DEVELOPER — Phase 5 (coverage and quality)

**Phase 5-A — Deviation Budget Utilization:**
SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS. State OVERALL_BUDGET_STATUS.
BUDGET_EXCEEDED_FINDING if EXCEEDED.

**Phase 5-B — Chain Budget Utilization:**
CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS.
CHAIN_BUDGET_EXCEEDED finding for each exceeded chain.

**Phase 5-C — Constraint Chain Status Summary:**
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS.
Cross-reference BROKEN chains to EXECUTION_HALT.

**Phase 5-D — Coverage Quality Gate + Ratios:**
Write COVERAGE_QUALITY_GATE: CLEAN|DEGRADED before ratios.
Five ratios (numerator/denominator visible): TOPIC_COVERAGE_RATIO,
TRANSITION_COVERAGE_RATIO, SLOT_PATH_COVERAGE_RATIO, TIMELINE_ANOMALY_RATE,
PATH_ADHERENCE_RATIO. Mark PROVISIONAL under DEGRADED.

**Phase 5-F — Status Quo Coverage Table (the proof):**
For each FOUND defect from Phase 2:
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION: YES|NO | FOUND_BY_STATUS_QUO: YES|NO |
DETECTION_METHOD | SQ_BLIND_SPOT

Apply structural auto-classification. For every NO in your METHOD_BLIND_SPOTS checklist,
the corresponding defect class is FOUND_BY_SIMULATION_ONLY by definition — not assertion,
by logical consequence of the declared method's architecture:
- METHOD_BLIND_SPOTS.PREDICTION_CONTRACT: NO → PREDICTION_DEVIATION is
  FOUND_BY_SIMULATION_ONLY
- METHOD_BLIND_SPOTS.CHAIN_BUDGET: NO → CHAIN_BUDGET_EXCEEDED is
  FOUND_BY_SIMULATION_ONLY
- METHOD_BLIND_SPOTS.TIMELINE_ANOMALIES: NO → TIMELINE_ANOMALY is
  FOUND_BY_SIMULATION_ONLY

Write STATUS_QUO_GAP_SUMMARY:
  FOUND_BY_SIMULATION_ONLY_COUNT: N
  FOUND_BY_SIMULATION_ONLY_LIST: [DEFECT_IDs]
  STRUCTURAL_BLIND_SPOTS_ACTIVATED: [the METHOD_BLIND_SPOTS keys that drove the gap]
  STATUS_QUO_GAP_NARRATIVE: one paragraph explaining what the declared informal method
    structurally cannot see and why — this is the adoption argument, grounded in the
    team's own method declaration.

Return to Phase 4-SQ now and fill in SQ_DEFECTS_NOT_FOUND from this table.
This completes the evidence loop: the informal method ran, it missed what the checklist
said it would miss, and the gap is now a count and a list, not a claim.

---

### AUDITOR — Phase 6 (independent verification)

Do not modify Developer rows. Record discrepancies as findings.

**Phase 6-A:** CONTRACT_AUDIT_GATE_HONORED, BUDGET_UTILIZATION_VERIFIED,
BUDGET_STATUS_CONSISTENT, SIMULATION_DELTA_COMPLETE. PASS or FAIL each.

**Phase 6-B:** Severity co-residency — every FOUND defect has SEVERITY_CLASS and
INVARIANT_CITE. Structured table. EXEMPT: CONFIRMED_ABSENT only.

**Phase 6-C:** Entanglement consistency — verify Phase 3-E against Phase 1 evidence.

**Phase 6-D:** Topic aggregate consistency — CONFORMANCE_ROLLUP vs DEVIATES count.
TOPIC_ROLLUP_MISMATCH for any discrepancy.

**Phase 6-E:** Session timeline — replay Phase 1-S mutations, compare reconstructed
SESSION_STATE to Phase 1 SESSION_STATE. TIMELINE_STATE_MISMATCH for discrepancies.

**Phase 6-F:** Fix viability — CONV_VIOLATIONS_INTRODUCED, CHAIN_REPAIR_COMPLETE,
VIABILITY per EXECUTION_HALT. SIDE_EFFECTS_FOUND if fix breaks a downstream constraint.

**Phase 6-G:** Chain integrity — CHAIN_EFFECTS vs upstream CONV-NN verdicts.
CHAIN_VERDICT_INCONSISTENCY when a downstream CONFORMS during a SUSPENDED window.

**Phase 6-H (combined):** Three sections.

Plan integrity: every EXECUTION_HALT has a PLAN_ITEM (EXECUTION_HALT_IN_PLAN),
CHAIN_REPAIR_IN_SCOPE, DEPENDENCY_ORDER_VALID per item, DEPENDENCY_CYCLE_CHECK.
PLAN_TIER_OVERRIDE_PRESENT on all CRITICAL deviation defects. OVERRIDE_TIER_HONORED.
PLAN_INTEGRITY_AUDIT: PASS|FAIL.

Path adherence: verify PREDICTION_MATCH per turn against contract.
PATH_ADHERENCE_RATIO_VERIFIED. CRITICAL_PATH_ESCALATION_VERIFIED (all CRITICAL deviations
at P1 minimum).

Status quo coverage: verify DETECTION_METHOD per defect against METHOD_BLIND_SPOTS.
Check whether the three auto-classification rules were applied correctly:
PREDICTION_DEVIATION_CLASSIFIED_CORRECTLY, CHAIN_BUDGET_EXCEEDED_CLASSIFIED_CORRECTLY,
TIMELINE_ANOMALY_CLASSIFIED_CORRECTLY. STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL.

Close with AUDITOR_CERTIFICATION: PASS|FAIL[cite blocking findings].

---

### REMEDIATION PLANNER — Phase 7

Wait for AUDITOR_CERTIFICATION. Read Phase 2 EXECUTION_HALT blocks and Phase 3-E
ENTANGLEMENT_MAP.

One PLAN_ITEM per FOUND defect:
PLAN_ID (RP-NN), DEFECT_REF, SEVERITY_CLASS, SCOPE, DEPENDENCY_ON (RP-NNs from
ENABLES relationships), PLAN_TIER, TIER_RATIONALE, CHAIN_REPAIR_ITEMS, UNBLOCKED_BY.

Tier priority order:
1. P0 → IMMEDIATE
2. PLAN_TIER_OVERRIDE: IMMEDIATE → IMMEDIATE (CRITICAL path deviations;
   these are adoption-blocking even at P2/P3 severity)
3. P1 → NEXT_SPRINT
4. P2/P3 → BACKLOG

Topological sort: no item before its DEPENDENCY_ON items.
Within a tier: P0 before P1 before P2/P3.

Close:
PLAN_ITEM_COUNT: N
IMMEDIATE_COUNT: N
NEXT_SPRINT_COUNT: N
BACKLOG_COUNT: N
DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND[RP-NN cycle if found]

A trace with no FOUND defects: PLAN_ITEM_COUNT: 0.

---

**Output file:** `simulations/flow/conversation/{topic}-conversation-{date}.md`
