# Quest Variations — flow-conversation — Round 12 (v11 rubric)

**Date:** 2026-03-15 | **Rubric version:** v11 | **Max score:** 184

---

## Variation Axes Selected

All 5 variations carry the full v11 baseline: C-01 through C-48. The baseline
includes mutation-first authoring, AUTHORIZED_REWRITERS, Contract Auditor gate
(COVERAGE_DELTA + CHAIN_BUDGET_DELTA), EXECUTION_HALT blocks with CHAIN_BREAK_TRACE
and CHAIN_REPAIR, PROPAGATION + CHAIN_ID in invariant register, CHAIN_EFFECTS column,
DEVIATION_BUDGET, CHAIN_BUDGET, CHAIN_BUDGET_EXCEEDED as 8th structural finding class,
Phase 6-F Fix Viability Audit, and Phase 6-G Chain Integrity Audit.

**Single-axis (3):**

- **Axis D — Lifecycle emphasis (Remediation Planner role)**: A 5th role
  (REMEDIATION PLANNER) is added after AUDITOR certification. The Planner reads all
  EXECUTION_HALT blocks and Phase 3-E ENTANGLEMENT_MAP, then produces a topologically
  sorted REMEDIATION_PLAN: one PLAN_ITEM per FOUND defect, sequenced by
  DEPENDENCY_CHAIN (ENABLES relationships from entanglement), tiered by severity
  (IMMEDIATE / NEXT_SPRINT / BACKLOG). Phase 6-H PLAN_INTEGRITY_AUDIT verifies every
  EXECUTION_HALT block is represented and every CHAIN_REPAIR CONV-NN appears in scope.

- **Axis E — Output format (Turn Prediction Contract)**: The Topology Architect
  pre-declares a TURN_PREDICTION_CONTRACT (Phase 0-A-10): one HAPPY_PATH and up to 3
  ALT_PATHs, each a PREDICTED_TURN_SEQUENCE of TOPIC_IDs with a PATH_CRITICALITY
  (CRITICAL / IMPORTANT / INFORMATIONAL). Phase 1 gains a PREDICTION_MATCH column
  (ON_PATH[PATH_ID] | DEVIATION[PATH_ID, expected, actual] | OFF_ALL_PATHS).
  PREDICTION_DEVIATION is the 9th structural defect class. PATH_ADHERENCE_RATIO is
  the 5th coverage ratio. CRITICAL_PATH deviations auto-elevate to P1 minimum severity.
  Phase 6-H PATH_ADHERENCE_AUDIT verifies PREDICTION_MATCH verdicts against the contract.

- **Axis F — Phrasing register (Imperative second-person)**: Identical v11 structure
  rewritten entirely in imperative second-person ("You will declare...", "Emit an
  EXECUTION_HALT block...", "For each turn, output..."). No structural changes.
  Hypothesis: directive register reduces hedging, forces sequential step completion,
  and creates unambiguous phase-gate checkpoints.

**Combined (2):**

- **Axes D + E**: Remediation Planner + Turn Prediction Contract combined. The
  REMEDIATION_PLAN incorporates PREDICTION_DEVIATION defects alongside EXECUTION_HALT
  blocks. CRITICAL_PATH deviations that trigger EXECUTION_HALT conditions carry
  PLAN_TIER: IMMEDIATE regardless of base severity. Phase 6-H merges Plan Integrity
  Audit and Path Adherence Audit into a single structured phase.

- **Axes E + inertia extension (STATUS_QUO_SIMULATION)**: Turn Prediction Contract
  combined with a STATUS_QUO_SIMULATION parallel trace. After Phase 4, the Developer
  re-runs the same scenario using only the declared informal review method
  (STATUS_QUO_METHOD declared in Phase 0). The parallel trace is abbreviated: no
  CONSTRAINT_VERDICTS, no CHAIN_EFFECTS, no PREDICTION_MATCH. Phase 5 includes a
  STATUS_QUO_COVERAGE table: what the informal trace found vs. what simulation found.
  PREDICTION_DEVIATION defects are automatically FOUND_BY_SIMULATION_ONLY (informal
  review cannot detect path-contract violations). Phase 6-H audits STATUS_QUO_COVERAGE
  completeness.

---

## V-01 — Axis D: Remediation Planner Role (Single-Axis)

**Hypothesis:** A flow-conversation artifact ends at Auditor certification — the
team still has to manually prioritize and sequence the fixes. Adding a REMEDIATION
PLANNER role converts the defect catalog into an executable work plan. The Planner
reads the entanglement map (which defects enable others), the EXECUTION_HALT
CHAIN_REPAIR lists (which constraints must be re-evaluated), and severity tiers
to produce a topologically sorted REMEDIATION_PLAN. A fix that unlocks downstream
fixes must appear first; P0 items occupy an IMMEDIATE tier. Phase 6-H verifies
plan completeness: every EXECUTION_HALT block must have a plan item, and every
CHAIN_REPAIR CONV-NN must be in scope.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Five roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR** → **REMEDIATION PLANNER**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

Produce all pre-execution artifacts in order. Sign each sub-artifact with
`[ARTIFACT_COMPLETE: 0-A-N]` before proceeding to the next.

**Phase 0-A-1: Topic Inventory**
Declare all topics:
`TOPIC_ID | TRIGGER_PHRASES | ENTRY_CONDITIONS | EXIT_TARGETS | REACHABLE: YES|NO`
Every topic referenced in Phase 1 must appear here. First reference to an undeclared
topic is a CONTRACT_GAP finding.

**Phase 0-A-2: Topic Reachability Map**
Declare which topics are reachable from which via natural conversation flow.
Orphaned topics (declared but unreachable) are flagged as ORPHAN candidates.

**Phase 0-A-3: Transition Map**
Declare all conversation graph edges:
`TRANS-NN | SOURCE_TOPIC | TARGET_TOPIC | CONDITION | REQUIRED|OPTIONAL`
Phase 5 reports transitions_exercised / total_declared.
Unexercised REQUIRED transitions are orphaned-edge defects.

**Phase 0-A-4: Vocabulary Gate**
Declare PERMITTED_TERMS (Copilot Studio vocabulary: topics, trigger phrases, conditions,
fallback topics, escalation, session variables) and PROHIBITED_TERMS (generic chatbot
terms without Copilot Studio grounding). Sign with VOCABULARY_GATE: SIGNED.
Phase 1 trace entries must contain no PROHIBITED_TERMS.

**Phase 0-A-5: Slot Path Map**
For each slot-filling topic, declare:
`SLOT_PATH_ID | TOPIC_ID | SLOT_SEQUENCE | REQUIRED_SLOTS | OPTIONAL_SLOTS | SHORT_CIRCUIT_CONDITIONS`

**Phase 0-A-6: Session Variable Registry**
Declare all session variables:
`VAR_ID | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL | INITIAL_VALUE`
First appearance of an unregistered variable in Phase 1 SESSION_STATE is a CONTRACT_GAP.

**Phase 0-A-7: Invariant Register**
Declare all conversation-level invariants. Each entry:
```
CONV-NN:
  DESCRIPTION: <what must hold>
  FALSIFICATION: <observable condition that disproves it>
  MUTATION_SEMANTICS: ADDITIVE|BOOLEAN|STRING_APPEND|CONDITIONAL
  PROPAGATION: [CONV-NN, ...] (downstream constraints that depend on this constraint's POST_VALUE; empty if terminal)
  CHAIN_ID: CHAIN-NN (every CONV-NN belongs to exactly one chain)
```
Chain head = first CONV-NN in chain with no inbound PROPAGATION.
When the chain head DEVIATES on any turn, downstream nodes enter CHAIN_SUSPENDED status
for that turn. CHAIN_SUSPENDED is not a DEVIATES verdict.
A chain is BROKEN if its head DEVIATES on any turn without recovering before trace end.

**Phase 0-A-8: Session Variable Timeline Contract**
For each variable in Phase 0-A-6:
```
VAR_ID:
  FIRST_WRITTEN_TOPIC: <TOPIC_ID>
  AUTHORIZED_REWRITERS: [TOPIC_ID, ...] (topics permitted to write beyond first-written)
  CLEARED_BY: <TOPIC_ID or NONE>
  READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```
A WRITE from a topic absent from both FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS
is an OFF_CONTRACT_WRITE anomaly.

**Phase 0-A-9: Constraint Chain Budget**
Declare per-chain budget for every CHAIN-NN from Phase 0-A-7:
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | CHAIN_BUDGET (max acceptable HEAD DEVIATES turns) | BUDGET_RATIONALE
```
CHAIN_BUDGET = 0 means any chain head DEVIATES turn is a CHAIN_BUDGET_EXCEEDED finding.
Budget applies only to the chain head; suspended downstream constraints are not counted.

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

Verify SESSION_VARIABLE_TIMELINE_CONTRACT completeness and chain budget coverage
before Developer begins Phase 1. This role may not be performed by the Topology
Architect or Developer.

```
VARS_IN_TOPOLOGY: [VAR_ID, ...] (from Phase 0-A-6)
VARS_IN_CONTRACT: [VAR_ID, ...] (from Phase 0-A-8)
COVERAGE_DELTA: [missing VAR_IDs] (must be empty to proceed)

CHAINS_IN_TOPOLOGY: [CHAIN-NN, ...] (from Phase 0-A-7)
CHAINS_IN_BUDGET: [CHAIN-NN, ...] (from Phase 0-A-9)
CHAIN_BUDGET_DELTA: [missing CHAIN-NNs] (must be empty to proceed)

AUTHORIZED_REWRITER_CHECK: For each AUTHORIZED_REWRITER in Phase 0-A-8, verify
  it appears in Phase 0-A-1. Flag any rewriter referencing an undeclared topic as CONTRACT_GAP.

CONTRACT_AUDIT: PASS | BLOCKED[COVERAGE_DELTA non-empty | CHAIN_BUDGET_DELTA non-empty | CONTRACT_GAP list]
```

Phase 1 execution may not begin until CONTRACT_AUDIT: PASS.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1–6

**DEVIATION_BUDGET** (declare before Phase 1-S; LOCKED — may not be revised after Phase 1-S begins):
```
P0_MAX: <integer>
P1_MAX: <integer>
P2_MAX: <integer>
P3_MAX: <integer>
BUDGET_RATIONALE: <why these thresholds are appropriate>
```

---

**Phase 1-S: Session Timeline (Mutation Log)**
Author Phase 1-S BEFORE Phase 1. SESSION_STATE in Phase 1 is derived by replaying
Phase 1-S mutations in turn order; it is not independently authored.

For every turn and every non-null session variable, record:
`TURN_ID | VAR_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | PRE_VALUE | POST_VALUE | CONTRACT_MATCH: YES|NO | TIMELINE_ANOMALY: NONE|READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ | ANOMALY_TYPE`

---

**Phase 1: Turn-by-Turn Trace**
For every turn, record a row in the turn table:

`TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE (derived from Phase 1-S replay; cite Phase 1-S entry) | CONFORMANCE: CONFORMS|DEVIATES[CONV-NN] | CONSTRAINT_VERDICTS (CONV-NN: CONFORMS|DEVIATES|CHAIN_SUSPENDED[chain head: CONV-NN broke at TURN_ID]) | CHAIN_EFFECTS (CONV-NN → [CONV-NN-downstream: ACTIVATED|SUSPENDED, ...]; N/A if no downstream propagation)`

For mutation invariants in CONSTRAINT_VERDICTS, include inline arithmetic evidence:
`CONV-NN: PRE=<value> MUTATION=<operation> POST=<value> CHECK: PRE+MUTATION=POST | CONV_NN_EVIDENCE_CLASS: CONDITIONAL[branch condition]`

No turn may lack CONFORMANCE or CONSTRAINT_VERDICTS. DEVIATES entries cite the violated
CONV-NN by its registered ID. CHAIN_SUSPENDED cites the chain head and first-deviate turn.

---

**Phase 1-T: Topic Aggregate** (additive to Phase 1; does not replace it)

For each topic visited:
`TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ | DEFECT_CITATIONS[DEFECT_CLASS, TURN_ID] | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP: <DEVIATES count> / <total turns on this topic>`

---

**Phase 2: Defect Classification**

Classify every defect found. Eight structural defect classes:
`DEAD_END | INFINITE_LOOP | INTENT_COLLISION | MISSING_FALLBACK | ORPHAN | SLOT_GAP | TIMELINE_ANOMALY | CHAIN_BUDGET_EXCEEDED`

For each finding:
`DEFECT_ID | DEFECT_CLASS | TOPIC_ID | TURN_ID | SEVERITY_CLASS: P0|P1|P2|P3 | INVARIANT_CITE: CONV-NN | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_ID]|MASKED_BY[DEFECT_ID] | RECOVERY: RECOVERABLE[min_turns, target_state]|UNRECOVERABLE[reason]`

CHAIN_BUDGET_EXCEEDED findings carry additional fields:
`FINDING_CLASS: CHAIN_BUDGET_EXCEEDED | CHAIN_ID | HEAD_CONV | BUDGET | ACTUAL | OVER_BY | FIRST_EXCEED_TURN | SUSPENDED_CONVS | IMPLICATION`
CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY by definition.
CHAIN_BUDGET_EXCEEDED findings are EXEMPT from Phase 6-B co-residency audit but must
appear in SIMULATION_DELTA.

**P0 EXECUTION HALT GATE**: Immediately after classifying each FOUND P0 defect, before
proceeding to classify lower-severity defects, emit:
```
EXECUTION_HALT
  HALT_TRIGGER: <DEFECT_CLASS> at <TOPIC_ID|TURN_ID>
  ROOT_CAUSE: <one-sentence causal statement>
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN: CHAIN-NN
    CHAIN_HEAD_CONV: CONV-NN
    FIRST_DEVIATE_TURN: TURN_ID
    SUSPENDED_CONVS: [CONV-NN, ...]
    BREAK_TO_DEFECT_PATH: <narrative: how chain break caused or enabled the P0 defect>
  MVF_RECOMMENDATION: <minimum viable fix>
  MVF_SCOPE: <topics/transitions/session variables the fix touches>
  CHAIN_REPAIR: [CONV-NN, ...] (chain head + all SUSPENDED_CONVS in BROKEN_CHAIN)
  UNBLOCKED_BY: <observable state change confirming fix was applied>
```
A trace with no FOUND P0 defects satisfies the P0 gate vacuously.

---

**Phase 3: Defect Reproduction**
For each FOUND defect:
- Minimal reproduction: exact utterance sequence that triggers the defect
- Observable failure mode

**Phase 3-E: Entanglement Map**
`DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_ID]|MASKED_BY[DEFECT_ID]`
MASKED_BY defects carry conditional recovery verdicts.

---

**Phase 4: Fallback and Escalation**

4-A. Trace at least one fallback path to completion: trigger, fallback node, agent
response, recovery or exit.

4-B. Trace at least one escalation path to human agent (or equivalent terminal handoff):
trigger condition, handoff node name, session state at handoff, agent receipt confirmation.
Escalation is CONFIRMED ABSENT only if no escalation topic appears in Phase 0-A-1.

4-C. For any FOUND INTENT_COLLISION: propose a disambiguation strategy (entity enrichment,
condition ordering, or trigger phrase refactor) with rationale.

---

**Phase 5: Coverage and Quality Gate**

**Phase 5-A: Deviation Budget Utilization**
```
DEVIATION_BUDGET_UTILIZATION
  SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET|EXCEEDED
  P0 | <P0_MAX> | <count> | ...
  P1 | ...
  P2 | ...
  P3 | ...
  OVERALL_BUDGET_STATUS: WITHIN_BUDGET | EXCEEDED[violated classes]
```
If OVERALL_BUDGET_STATUS: EXCEEDED, emit before coverage ratios:
```
BUDGET_EXCEEDED_FINDING
  VIOLATED_CLASSES: [...]
  OVER_BY: <class: actual - max, ...>
  IMPLICATION: <one sentence on readiness>
```

**Phase 5-B: Constraint Chain Budget Utilization**
```
CHAIN_BUDGET_UTILIZATION
  CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET|EXCEEDED
```
For each chain exceeding budget, emit a CHAIN_BUDGET_EXCEEDED finding per Phase 2 format.

**Phase 5-C: Coverage Quality Gate**
Declare COVERAGE_QUALITY_GATE: CLEAN | DEGRADED as the headline before coverage ratios.
DEGRADED when TIMELINE_ANOMALY_RATE > 0. All four ratios carry PROVISIONAL designation
under DEGRADED. A PROVISIONAL ratio carries an explicit acknowledgment that temporal
ordering defects exist.

**Phase 5-D: Coverage Ratios**
1. `topic_coverage_ratio` = topics_visited / total_declared (from Phase 0-A-1)
2. `transition_coverage_ratio` = transitions_exercised / total_declared (from Phase 0-A-3)
3. `slot_path_coverage_ratio` = slot_paths_traced / total_declared (from Phase 0-A-5)
4. `TIMELINE_ANOMALY_RATE` = timeline_anomalies / total_variable_turn_events (from Phase 1-S)

Report as fractions with numerator and denominator visible.

**Phase 5-E: Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```
BROKEN chains that map to P0 EXECUTION_HALT blocks must cross-reference the EXECUTION_HALT.

**Phase 5-F: Simulation Delta**
For each FOUND defect, assign:
`FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH`
`STATUS_QUO_GAP` = count and list of FOUND_BY_SIMULATION_ONLY defects.
CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY by definition.
Every Phase 2 FOUND defect must appear in exactly one detection-method category.

---

**Phase 6: Adversarial Turn Injection**
Inject at least one adversarial utterance mid-conversation (off-topic, ambiguous, or
contradictory). Record: INJECTION_TURN_ID, INJECTION_UTTERANCE, SYSTEM_RESPONSE,
DEFECT_TRIGGERED: YES|NO, RECOVERY_PATH (traced to completion).

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-H

**Phase 6-A: Coverage Audit**
```
CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL (Phase 0-CA-1 produced empty COVERAGE_DELTA and CHAIN_BUDGET_DELTA)
QUALITY_GATE_VERIFIED: PASS|FAIL (COVERAGE_QUALITY_GATE headline present before ratios)
TOPIC_COVERAGE_VERIFIED: PASS|FAIL[cite]
TRANSITION_COVERAGE_VERIFIED: PASS|FAIL[cite]
SLOT_PATH_COVERAGE_VERIFIED: PASS|FAIL[cite]
TIMELINE_ANOMALY_RATE_VERIFIED: PASS|FAIL[cite]
BUDGET_UTILIZATION_VERIFIED: PASS|FAIL (actual DEVIATES counts vs Phase 2 FOUND per severity)
BUDGET_STATUS_CONSISTENT: PASS|FAIL (EXCEEDED/WITHIN_BUDGET verdict matches audited counts)
SIMULATION_DELTA_COMPLETE: PASS|FAIL (every Phase 2 FOUND defect in exactly one category; CHAIN_BUDGET_EXCEEDED present)
AUDITOR_CERTIFICATION: PASS|FAIL
```
CONTRACT_AUDIT_GATE_HONORED must be the first entry; AUDITOR_CERTIFICATION must be the last.

**Phase 6-B: Severity Co-Residency Audit**
For each FOUND defect row (excluding CHAIN_BUDGET_EXCEEDED, which is EXEMPT):
Verify both SEVERITY_CLASS and INVARIANT_CITE are present. Produce structured table:
`DEFECT_ID | SEVERITY_CLASS_PRESENT: YES|NO | INVARIANT_CITE_PRESENT: YES|NO | AUDIT: PASS|FAIL`

**Phase 6-C: Entanglement Consistency Audit**
Verify Phase 3-E ENTANGLEMENT_MAP consistency against Phase 1 turn-level evidence.
`DEFECT_ID | ENTANGLEMENT_VERDICT_REPORTED | ENTANGLEMENT_VERDICT_AUDITED | CONSISTENT: PASS|FAIL[cite]`

**Phase 6-D: Topic Aggregate Consistency Audit**
Cross-check Phase 1-T conformance_rollup against Phase 1 DEVIATES counts per topic.
`TOPIC_ID | ROLLUP_REPORTED | DEVIATES_AUDITED | CONSISTENT: PASS|FAIL[TOPIC_ROLLUP_MISMATCH]`

**Phase 6-E: Session Timeline Consistency Audit**
Replay Phase 1-S mutations in sequence. Compare reconstructed SESSION_STATE against
Phase 1 SESSION_STATE at every turn.
`TURN_ID | RECONSTRUCTED_STATE | REPORTED_STATE | CONSISTENT: PASS|FAIL[TIMELINE_STATE_MISMATCH]`

**Phase 6-F: Fix Viability Audit**
For each EXECUTION_HALT block in Phase 2:
```
HALT_TRIGGER | MVF_RECOMMENDATION | CONV_VIOLATIONS_INTRODUCED: YES|NO | CONV_VIOLATIONS_DETAIL
             | CHAIN_REPAIR_COMPLETE: YES|NO (every CONV-NN in CHAIN_REPAIR appears in MVF_SCOPE)
             | VIABILITY: VIABLE | SIDE_EFFECTS_FOUND[CONV-NN list]
```
VIABLE requires CONV_VIOLATIONS_INTRODUCED: NO and CHAIN_REPAIR_COMPLETE: YES.

**Phase 6-G: Chain Integrity Audit**
Verify all CHAIN_EFFECTS declared in Phase 1 against upstream CONV-NN verdicts.
Rules: (1) ACTIVATED edge must correspond to upstream CONFORMS; (2) SUSPENDED edge must
correspond to upstream DEVIATES or CHAIN_SUSPENDED; (3) downstream CONFORMS during
SUSPENDED window is CHAIN_VERDICT_INCONSISTENCY.
`CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL[cite]`

**Phase 6-H: Plan Integrity Audit** *(new in V-01)*
After Remediation Planner completes Phase 7, verify:
```
For each EXECUTION_HALT block in Phase 2:
  EXECUTION_HALT_IN_PLAN: YES|NO (corresponding PLAN_ITEM exists in Phase 7)
  CHAIN_REPAIR_IN_SCOPE: YES|NO (every CONV-NN from CHAIN_REPAIR appears in PLAN_ITEM SCOPE)

For each PLAN_ITEM in Phase 7:
  DEPENDENCY_ORDER_VALID: YES|NO (PLAN_ITEM does not precede any item in its DEPENDENCY_ON list)

PLAN_INTEGRITY_AUDIT: PASS | FAIL[cite]
DEPENDENCY_CYCLE_CHECK: PASS | CYCLE_FOUND[RP-NN cycle description]
```

`[ROLE_COMPLETE: AUDITOR]`

---

### REMEDIATION PLANNER — Phase 7 *(new in V-01)*

Read all EXECUTION_HALT blocks (Phase 2) and Phase 3-E ENTANGLEMENT_MAP.
Produce REMEDIATION_PLAN: one PLAN_ITEM per FOUND defect, topologically sorted.

For each defect, declare:
```
PLAN_ID: RP-NN
DEFECT_REF: <Phase 2 DEFECT_ID>
SEVERITY_CLASS: <P0|P1|P2|P3>
SCOPE: <topics/transitions/session variables; use MVF_SCOPE from EXECUTION_HALT if available>
DEPENDENCY_ON: [RP-NN, ...] (items that must execute before this one; derived from ENABLES in Phase 3-E)
PLAN_TIER: IMMEDIATE (P0) | NEXT_SPRINT (P1) | BACKLOG (P2/P3)
TIER_RATIONALE: <why this tier>
CHAIN_REPAIR_ITEMS: [CONV-NN, ...] (from EXECUTION_HALT CHAIN_REPAIR field; empty if no halt)
UNBLOCKED_BY: <observable confirmation this fix is applied>
```

Topological sort rule: no PLAN_ITEM may appear before any PLAN_ITEM in its DEPENDENCY_ON
list. Items with no dependencies come first. Within a tier, P0 items precede P1 precede P2/P3.

After all PLAN_ITEMs, emit:
```
PLAN_SUMMARY
  PLAN_ITEM_COUNT: <total>
  IMMEDIATE_COUNT: <P0 items>
  NEXT_SPRINT_COUNT: <P1 items>
  BACKLOG_COUNT: <P2/P3 items>
  DEPENDENCY_CYCLE_CHECK: PASS | CYCLE_FOUND[RP-NN cycle]
```

`[ROLE_COMPLETE: REMEDIATION PLANNER]`

---

## V-02 — Axis E: Turn Prediction Contract (Single-Axis)

**Hypothesis:** Pre-declaring expected conversation paths before tracing transforms
the Topology Architect from a graph documenter into a path predictor. Deviations from
the predicted path surface not just which topic was wrong but which path contract was
broken and how critical that path is. PATH_ADHERENCE_RATIO as a 5th coverage metric
adds a prediction-vs-reality dimension that per-turn CONFORMANCE cannot capture alone:
a trace can achieve 100% CONFORMANCE (all invariants held turn-by-turn) while severely
deviating from all declared paths. CRITICAL_PATH deviations auto-elevate severity,
making the artifact self-escalating for the most important flow sequences.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

**Phase 0-A-1 through 0-A-9**: Identical to V-01 (Topic Inventory, Reachability Map,
Transition Map, Vocabulary Gate, Slot Path Map, Session Variable Registry, Invariant
Register with PROPAGATION+CHAIN_ID, Session Variable Timeline Contract with
AUTHORIZED_REWRITERS, Constraint Chain Budget).

**Phase 0-A-10: Turn Prediction Contract** *(new in V-02)*
Declare the expected conversation paths before tracing. One HAPPY_PATH is required;
up to 3 ALT_PATHs are optional.

For each path:
```
PATH_ID: HP-01 | ALT-NN
PATH_DESCRIPTION: <brief narrative of this conversation scenario>
PATH_CRITICALITY: CRITICAL | IMPORTANT | INFORMATIONAL
PREDICTED_TURN_SEQUENCE:
  TURN_NN: TOPIC_ID (with any SLOT_PATH_ID or expected TRANSITION_ID)
  ...
```

PATH_CRITICALITY rules:
- CRITICAL: core happy path or paths covering required business transactions
- IMPORTANT: named alternative paths (error recovery, disambiguation)
- INFORMATIONAL: exploratory or edge-case paths

A PREDICTION_DEVIATION on a CRITICAL path is automatically elevated to P1 minimum
severity, regardless of the defect's inherent severity classification.

TURN_PREDICTION_CONTRACT must be signed before Phase 1 begins.
`TURN_PREDICTION_CONTRACT_SIGNED: YES`

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

Identical to V-01, plus:
```
PATHS_IN_CONTRACT: [PATH_ID, ...] (from Phase 0-A-10)
PREDICTION_CONTRACT_SIGNED: YES|NO
```
CONTRACT_AUDIT: PASS requires TURN_PREDICTION_CONTRACT_SIGNED: YES.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1–6

**DEVIATION_BUDGET**: Declare before Phase 1-S. LOCKED.
`P0_MAX | P1_MAX | P2_MAX | P3_MAX | BUDGET_RATIONALE`

**Phase 1-S**: SESSION_TIMELINE mutation log (identical to V-01, authored before Phase 1).

**Phase 1: Turn-by-Turn Trace**
All columns from V-01, plus one new column:

`... | PREDICTION_MATCH: ON_PATH[PATH_ID] | DEVIATION[PATH_ID, expected_TOPIC_ID, actual_TOPIC_ID] | OFF_ALL_PATHS`

Rules:
- ON_PATH[PATH_ID]: this turn matches the PREDICTED_TURN_SEQUENCE of PATH_ID at the
  corresponding sequence position.
- DEVIATION[PATH_ID, expected, actual]: the trace visited a different topic than the
  contract predicted at this sequence position.
- OFF_ALL_PATHS: the turn does not correspond to any declared PATH_ID sequence position.

A turn may be ON_PATH for one path and OFF_ALL_PATHS for others simultaneously;
record the most specific match.

**Phase 1-T**: Topic aggregate (identical to V-01), plus:
`PATH_IDS_MATCHED: [HP-01, ALT-NN, ...] (paths this topic appeared on as ON_PATH)`

**Phase 2: Defect Classification**

Nine structural defect classes:
`DEAD_END | INFINITE_LOOP | INTENT_COLLISION | MISSING_FALLBACK | ORPHAN | SLOT_GAP | TIMELINE_ANOMALY | CHAIN_BUDGET_EXCEEDED | PREDICTION_DEVIATION`

**PREDICTION_DEVIATION** defect format:
```
DEFECT_ID | DEFECT_CLASS: PREDICTION_DEVIATION
DEVIATION_TURN: TURN_ID
PATH_ID: <which path contract was violated>
EXPECTED_TOPIC: <TOPIC_ID from PREDICTED_TURN_SEQUENCE>
ACTUAL_TOPIC: <TOPIC_ID observed in trace>
PATH_CRITICALITY: CRITICAL|IMPORTANT|INFORMATIONAL (inherited from Phase 0-A-10)
SEVERITY_CLASS: P0|P1|P2|P3 (CRITICAL paths auto-elevate to P1 minimum)
INVARIANT_CITE: CONV-NN (cite the constraint most related to this path deviation)
DEVIATION_IMPACT: CRITICAL_PATH_BROKEN | ALT_PATH_DEVIATION | OFF_ALL_PATHS
RECOVERY: RECOVERABLE[min_turns, target_path_state] | UNRECOVERABLE[reason]
ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_ID]|MASKED_BY[DEFECT_ID]
```

P0 EXECUTION HALT GATE, CHAIN_BREAK_TRACE, CHAIN_REPAIR: identical to V-01.

**Phases 3–4**: Identical to V-01.

**Phase 5: Coverage and Quality Gate**

**Phase 5-A**: Deviation Budget Utilization (identical to V-01).
**Phase 5-B**: Constraint Chain Budget Utilization (identical to V-01).
**Phase 5-C**: Coverage Quality Gate (CLEAN | DEGRADED, identical to V-01).
**Phase 5-D**: Coverage Ratios — report 5 ratios:
1. topic_coverage_ratio
2. transition_coverage_ratio
3. slot_path_coverage_ratio
4. TIMELINE_ANOMALY_RATE
5. **PATH_ADHERENCE_RATIO** = turns_on_any_predicted_path / total_turns *(new in V-02)*

PATH_ADHERENCE_RATIO notes: OFF_ALL_PATHS turns do not appear in the numerator.
Under COVERAGE_QUALITY_GATE: DEGRADED, PATH_ADHERENCE_RATIO also carries PROVISIONAL.

**Phase 5-E**: Constraint Chain Status Summary (identical to V-01).
**Phase 5-F**: Simulation Delta (identical to V-01; PREDICTION_DEVIATION defects are
FOUND_BY_SIMULATION_ONLY if informal review method does not consult TURN_PREDICTION_CONTRACT).

**Phase 6: Adversarial Turn Injection** (identical to V-01).

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-H

**Phases 6-A through 6-G**: Identical to V-01.

**Phase 6-H: Path Adherence Audit** *(new in V-02)*
Verify PREDICTION_MATCH verdicts against Phase 0-A-10 TURN_PREDICTION_CONTRACT.

For each turn carrying PREDICTION_MATCH:
```
TURN_ID | PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED | CONSISTENT: PASS|FAIL[PATH_AUDIT_MISMATCH]
```
Audit rules:
1. ON_PATH[PATH_ID]: verify the turn's TOPIC_MATCHED appears in PATH_ID's
   PREDICTED_TURN_SEQUENCE at the corresponding sequence position.
2. DEVIATION: verify the expected and actual TOPIC_IDs match the contract and trace.
3. OFF_ALL_PATHS: verify no declared path has this TOPIC_ID at this sequence position.

```
PATH_ADHERENCE_RATIO_VERIFIED: PASS|FAIL[mismatch count]
CRITICAL_PATH_ESCALATION_VERIFIED: PASS|FAIL (CRITICAL deviations carry P1 minimum severity)
PATH_ADHERENCE_AUDIT: PASS|FAIL
```

`[ROLE_COMPLETE: AUDITOR]`

---

## V-03 — Axis F: Imperative Second-Person Register (Single-Axis)

**Hypothesis:** The v11 baseline written in third-person descriptive ("The Developer
produces...", "The Auditor verifies...") allows the executing model to treat each
instruction as a description of a desired state rather than a mandatory step. Rewriting
in imperative second-person ("Produce...", "Verify...", "You must emit...") makes each
instruction a direct command with an unambiguous completion criterion. The hypothesis
is that imperative register reduces prompt hedging (phrases like "should include" become
"must include"), eliminates ambiguity about which role is currently executing, and
creates cleaner phase-gate checkpoints — resulting in more complete phase execution
without structural changes to the artifact.

---

Simulate a multi-turn Copilot Studio agent conversation through a topic graph.
Execute four roles in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

Do not begin any role until the preceding role's section carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### AS TOPOLOGY ARCHITECT — Phase 0-A

Produce all pre-execution artifacts in order. After each sub-artifact, write
`[ARTIFACT_COMPLETE: 0-A-N]` before producing the next.

**Phase 0-A-1: Topic Inventory**
Declare every topic the trace will reference. For each topic, write:
`TOPIC_ID | TRIGGER_PHRASES | ENTRY_CONDITIONS | EXIT_TARGETS | REACHABLE: YES|NO`
You must declare all topics before Phase 1 begins. Any topic appearing in Phase 1
that is not in this inventory is a CONTRACT_GAP finding — record it immediately.

**Phase 0-A-2: Reachability Map**
Map which topics are reachable from which topics via natural conversation flow.
Flag any declared topic with no inbound path as an ORPHAN candidate.

**Phase 0-A-3: Transition Map**
Declare every conversation graph edge:
`TRANS-NN | SOURCE_TOPIC | TARGET_TOPIC | CONDITION | REQUIRED|OPTIONAL`
You must declare all transitions before Phase 1 begins. Unexercised REQUIRED
transitions become orphaned-edge defects in Phase 5.

**Phase 0-A-4: Vocabulary Gate**
Declare PERMITTED_TERMS (Copilot Studio vocabulary) and PROHIBITED_TERMS (generic
chatbot terms). Sign the gate: `VOCABULARY_GATE: SIGNED`. In Phase 1, write no
PROHIBITED_TERMS in any trace entry.

**Phase 0-A-5: Slot Path Map**
For each slot-filling topic, declare:
`SLOT_PATH_ID | TOPIC_ID | SLOT_SEQUENCE | REQUIRED_SLOTS | OPTIONAL_SLOTS | SHORT_CIRCUIT_CONDITIONS`

**Phase 0-A-6: Session Variable Registry**
Declare every session variable before Phase 1:
`VAR_ID | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL | INITIAL_VALUE`
If Phase 1 references an unregistered variable, record it as a CONTRACT_GAP immediately.

**Phase 0-A-7: Invariant Register**
For every conversation-level invariant, write:
```
CONV-NN:
  DESCRIPTION: <what must hold>
  FALSIFICATION: <observable condition that disproves it>
  MUTATION_SEMANTICS: ADDITIVE|BOOLEAN|STRING_APPEND|CONDITIONAL
  PROPAGATION: [CONV-NN, ...] (empty if terminal)
  CHAIN_ID: CHAIN-NN
```
Identify the chain head for each CHAIN-NN (the CONV-NN with no inbound PROPAGATION).
When a chain head DEVIATES, mark all downstream nodes CHAIN_SUSPENDED for that turn.
Mark a chain BROKEN if its head DEVIATES on any turn without recovering before the trace ends.

**Phase 0-A-8: Session Variable Timeline Contract**
For every variable in Phase 0-A-6, write:
```
VAR_ID:
  FIRST_WRITTEN_TOPIC: <TOPIC_ID>
  AUTHORIZED_REWRITERS: [TOPIC_ID, ...]
  CLEARED_BY: <TOPIC_ID or NONE>
  READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```
Any write from a topic absent from both FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS
is an OFF_CONTRACT_WRITE anomaly.

**Phase 0-A-9: Constraint Chain Budget**
For every CHAIN-NN from Phase 0-A-7, write:
`CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | CHAIN_BUDGET | BUDGET_RATIONALE`
Set CHAIN_BUDGET = 0 for chains where any head deviation is unacceptable.
Count only chain head DEVIATES turns against the budget; do not count CHAIN_SUSPENDED turns.

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### AS CONTRACT AUDITOR — Phase 0-CA-1

You are a separate agent from the Topology Architect and Developer. Your scope is
pre-execution contract completeness only.

Perform these checks:
```
1. List VARS_IN_TOPOLOGY (from Phase 0-A-6) and VARS_IN_CONTRACT (from Phase 0-A-8).
   Compute COVERAGE_DELTA = VARS_IN_TOPOLOGY minus VARS_IN_CONTRACT.
   If non-empty, block execution.

2. List CHAINS_IN_TOPOLOGY (from Phase 0-A-7) and CHAINS_IN_BUDGET (from Phase 0-A-9).
   Compute CHAIN_BUDGET_DELTA = CHAINS_IN_TOPOLOGY minus CHAINS_IN_BUDGET.
   If non-empty, block execution.

3. For each AUTHORIZED_REWRITER in Phase 0-A-8: verify it appears in Phase 0-A-1.
   If not, record CONTRACT_GAP[rewriter TOPIC_ID not in topology].

4. Write: CONTRACT_AUDIT: PASS | BLOCKED[reason]
```

Do not allow Phase 1 to begin until you write CONTRACT_AUDIT: PASS.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### AS DEVELOPER — Phases 1–6

Before Phase 1-S, declare and lock your DEVIATION_BUDGET:
```
DEVIATION_BUDGET (LOCKED — you may not revise this after Phase 1-S begins)
  P0_MAX: <integer>
  P1_MAX: <integer>
  P2_MAX: <integer>
  P3_MAX: <integer>
  BUDGET_RATIONALE: <why these thresholds>
```

**Phase 1-S: Session Timeline**
Write Phase 1-S BEFORE Phase 1. You must not independently author SESSION_STATE in
Phase 1 — derive it entirely by replaying Phase 1-S mutations in turn order.

For every turn and every non-null session variable, write:
`TURN_ID | VAR_ID | MUTATION_TYPE: WRITE|READ|CLEAR|NO_CHANGE | PRE_VALUE | POST_VALUE | CONTRACT_MATCH: YES|NO | TIMELINE_ANOMALY: NONE|READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ | ANOMALY_TYPE`

**Phase 1: Turn-by-Turn Trace**
For every conversation turn, write one row:
`TURN_ID | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE (cite Phase 1-S entry) | CONFORMANCE: CONFORMS|DEVIATES[CONV-NN] | CONSTRAINT_VERDICTS | CHAIN_EFFECTS`

For CONSTRAINT_VERDICTS on mutation invariants, include:
`CONV-NN: PRE=<value> MUTATION=<op> POST=<value> CHECK: <arithmetic confirmation> | CONV_NN_EVIDENCE_CLASS: CONDITIONAL[branch condition]`

Do not leave any turn without both CONFORMANCE and CONSTRAINT_VERDICTS.
For DEVIATES, cite the CONV-NN. For CHAIN_SUSPENDED, cite the chain head and the turn
where it first deviated.

For CHAIN_EFFECTS, write:
`CONV-NN → [CONV-NN-downstream: ACTIVATED|SUSPENDED, ...]`
Write N/A if this CONV-NN has no downstream propagation.

**Phase 1-T: Topic Aggregate**
Write Phase 1-T after Phase 1. Do not replace Phase 1 with it — both must be present.
For each visited topic:
`TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ | DEFECT_CITATIONS | ADVERSARIAL_INJECTION_COUNT | CONFORMANCE_ROLLUP`

**Phase 2: Defect Classification**
Classify every defect. Use exactly these eight defect classes:
`DEAD_END | INFINITE_LOOP | INTENT_COLLISION | MISSING_FALLBACK | ORPHAN | SLOT_GAP | TIMELINE_ANOMALY | CHAIN_BUDGET_EXCEEDED`

For each finding, write:
`DEFECT_ID | DEFECT_CLASS | TOPIC_ID | TURN_ID | SEVERITY_CLASS | INVARIANT_CITE | ENTANGLEMENT_VERDICT | RECOVERY`

For CHAIN_BUDGET_EXCEEDED, also write:
`CHAIN_ID | HEAD_CONV | BUDGET | ACTUAL | OVER_BY | FIRST_EXCEED_TURN | SUSPENDED_CONVS | IMPLICATION`
These findings are FOUND_BY_SIMULATION_ONLY and EXEMPT from Phase 6-B co-residency audit.

Immediately after classifying each P0 defect, before proceeding to lower-severity defects,
you must emit an EXECUTION_HALT block:
```
EXECUTION_HALT
  HALT_TRIGGER: <DEFECT_CLASS> at <TOPIC_ID|TURN_ID>
  ROOT_CAUSE: <one sentence>
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN: CHAIN-NN
    CHAIN_HEAD_CONV: CONV-NN
    FIRST_DEVIATE_TURN: TURN_ID
    SUSPENDED_CONVS: [CONV-NN, ...]
    BREAK_TO_DEFECT_PATH: <how the chain break caused or enabled this P0>
  MVF_RECOMMENDATION: <minimum viable fix>
  MVF_SCOPE: <topics/transitions/variables touched>
  CHAIN_REPAIR: [CONV-NN, ...] (chain head + all SUSPENDED_CONVS)
  UNBLOCKED_BY: <observable confirmation of fix>
```
If there are no P0 defects, this gate is satisfied vacuously.

**Phase 3: Defect Reproduction**
For each FOUND defect: write the minimal utterance sequence that triggers it and
the observable failure mode.

**Phase 3-E: Entanglement Map**
For every FOUND defect: `DEFECT_ID | ENTANGLEMENT_VERDICT: ISOLATED|ENABLES[DEFECT_ID]|MASKED_BY[DEFECT_ID]`

**Phase 4: Fallback, Escalation, Disambiguation**
4-A. Trace one fallback path to completion.
4-B. Trace one escalation path (or write CONFIRMED ABSENT if no escalation topic declared).
4-C. For any INTENT_COLLISION found: propose a specific disambiguation strategy with rationale.

**Phase 5: Coverage and Quality Gate**

5-A. Write DEVIATION_BUDGET_UTILIZATION table. If exceeded, emit BUDGET_EXCEEDED_FINDING
before coverage ratios.

5-B. Write CHAIN_BUDGET_UTILIZATION table. For each chain exceeding budget, emit
CHAIN_BUDGET_EXCEEDED finding per Phase 2 format.

5-C. Declare COVERAGE_QUALITY_GATE: CLEAN | DEGRADED as the headline before coverage ratios.
Mark all ratios PROVISIONAL if DEGRADED.

5-D. Report four coverage ratios as fractions (numerator/denominator visible):
topic_coverage_ratio, transition_coverage_ratio, slot_path_coverage_ratio, TIMELINE_ANOMALY_RATE.

5-E. Write CONSTRAINT CHAIN STATUS SUMMARY table:
`CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN`
Cross-reference BROKEN chains to their EXECUTION_HALT blocks.

5-F. Write SIMULATION_DELTA: assign each FOUND defect to FOUND_BY_SIMULATION_ONLY or FOUND_BY_BOTH.

**Phase 6: Adversarial Turn Injection**
Inject one adversarial utterance. Record: INJECTION_TURN_ID, utterance, system response,
DEFECT_TRIGGERED, recovery path.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AS AUDITOR — Phases 6-A through 6-G

You are structurally independent of the Developer. Your findings may not alter Developer
rows; record discrepancies as audit findings.

**Phase 6-A:** Write a CONTRACT_AUDIT_GATE_HONORED field first, then verify each
coverage signal, then write AUDITOR_CERTIFICATION last:
```
CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL
QUALITY_GATE_VERIFIED: PASS|FAIL
TOPIC_COVERAGE_VERIFIED: PASS|FAIL[cite]
TRANSITION_COVERAGE_VERIFIED: PASS|FAIL[cite]
SLOT_PATH_COVERAGE_VERIFIED: PASS|FAIL[cite]
TIMELINE_ANOMALY_RATE_VERIFIED: PASS|FAIL[cite]
BUDGET_UTILIZATION_VERIFIED: PASS|FAIL
BUDGET_STATUS_CONSISTENT: PASS|FAIL
SIMULATION_DELTA_COMPLETE: PASS|FAIL
AUDITOR_CERTIFICATION: PASS|FAIL
```

**Phase 6-B:** Produce a structured co-residency audit table (excluding CHAIN_BUDGET_EXCEEDED):
`DEFECT_ID | SEVERITY_CLASS_PRESENT: YES|NO | INVARIANT_CITE_PRESENT: YES|NO | AUDIT: PASS|FAIL`

**Phase 6-C:** Verify Phase 3-E ENTANGLEMENT_MAP against Phase 1 turn-level evidence.
`DEFECT_ID | ENTANGLEMENT_VERDICT_REPORTED | AUDITED | CONSISTENT: PASS|FAIL[cite]`

**Phase 6-D:** Cross-check Phase 1-T conformance_rollup against Phase 1 DEVIATES counts per topic.
`TOPIC_ID | ROLLUP_REPORTED | DEVIATES_AUDITED | CONSISTENT: PASS|FAIL[TOPIC_ROLLUP_MISMATCH]`

**Phase 6-E:** Replay Phase 1-S mutations and compare reconstructed SESSION_STATE to Phase 1.
`TURN_ID | RECONSTRUCTED_STATE | REPORTED_STATE | CONSISTENT: PASS|FAIL[TIMELINE_STATE_MISMATCH]`

**Phase 6-F:** For each EXECUTION_HALT block, verify fix viability:
`HALT_TRIGGER | MVF_RECOMMENDATION | CONV_VIOLATIONS_INTRODUCED: YES|NO | CHAIN_REPAIR_COMPLETE: YES|NO | VIABILITY: VIABLE|SIDE_EFFECTS_FOUND[CONV-NN list]`

**Phase 6-G:** Verify all CHAIN_EFFECTS against upstream verdicts:
`CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL[CHAIN_VERDICT_INCONSISTENCY if downstream CONFORMS during SUSPENDED window]`

`[ROLE_COMPLETE: AUDITOR]`

---

## V-04 — Axes D + E: Remediation Planner + Turn Prediction Contract (Combined)

**Hypothesis:** Combining the Remediation Planner (Axis D) with the Turn Prediction
Contract (Axis E) creates a closed-loop artifact. Predicted-path deviations are not
just defects to classify — they inform the remediation plan's priority tier.
CRITICAL_PATH deviation defects automatically enter PLAN_TIER: IMMEDIATE in the
REMEDIATION_PLAN regardless of severity classification. This closes the gap between
the prediction contract (what we expected) and the remediation plan (what we do about
it): critical path breaks receive the same urgency tier as P0 defects without waiting
for manual severity adjudication. The Phase 6-H combined audit verifies both plan
integrity and path adherence in a single Auditor phase.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Five roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR** → **REMEDIATION PLANNER**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

**Phases 0-A-1 through 0-A-9**: Identical to V-01 (complete topic graph, transition map,
vocabulary gate, slot paths, variable registry, invariants with PROPAGATION+CHAIN_ID,
timeline contract with AUTHORIZED_REWRITERS, chain budgets).

**Phase 0-A-10: Turn Prediction Contract** *(from V-02)*
Declare HAPPY_PATH (required) and up to 3 ALT_PATHs. For each:
```
PATH_ID: HP-01 | ALT-NN
PATH_DESCRIPTION: <scenario narrative>
PATH_CRITICALITY: CRITICAL | IMPORTANT | INFORMATIONAL
PREDICTED_TURN_SEQUENCE:
  TURN_NN: TOPIC_ID
  ...
```
CRITICAL path deviations auto-elevate to P1 minimum severity AND to PLAN_TIER: IMMEDIATE
in Phase 7 (regardless of severity class).
Sign: `TURN_PREDICTION_CONTRACT_SIGNED: YES`

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

All checks from V-01, plus:
```
PATHS_IN_CONTRACT: [PATH_ID, ...]
TURN_PREDICTION_CONTRACT_SIGNED: YES|NO
```
CONTRACT_AUDIT: PASS requires both COVERAGE_DELTA = empty AND CHAIN_BUDGET_DELTA = empty
AND TURN_PREDICTION_CONTRACT_SIGNED: YES.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1–6

**DEVIATION_BUDGET**: Declare before Phase 1-S. LOCKED.
`P0_MAX | P1_MAX | P2_MAX | P3_MAX | BUDGET_RATIONALE`

**Phase 1-S**: SESSION_TIMELINE mutation log (authored before Phase 1; identical to V-01).

**Phase 1: Turn-by-Turn Trace**
All columns from V-01, plus PREDICTION_MATCH from V-02:
`... | PREDICTION_MATCH: ON_PATH[PATH_ID] | DEVIATION[PATH_ID, expected, actual] | OFF_ALL_PATHS`

**Phase 1-T**: Identical to V-02 (includes PATH_IDS_MATCHED column).

**Phase 2: Defect Classification**

Nine structural defect classes (eight from V-01 + PREDICTION_DEVIATION from V-02):
`DEAD_END | INFINITE_LOOP | INTENT_COLLISION | MISSING_FALLBACK | ORPHAN | SLOT_GAP | TIMELINE_ANOMALY | CHAIN_BUDGET_EXCEEDED | PREDICTION_DEVIATION`

PREDICTION_DEVIATION format: identical to V-02 (includes DEVIATION_IMPACT, PATH_CRITICALITY,
auto-elevation rule for CRITICAL paths).

P0 EXECUTION HALT GATE with CHAIN_BREAK_TRACE and CHAIN_REPAIR: identical to V-01.

Note: CRITICAL path PREDICTION_DEVIATION defects carry an additional field in Phase 2:
`PLAN_TIER_OVERRIDE: IMMEDIATE (CRITICAL path deviation — overrides severity-based tier)`
This override is respected by the Remediation Planner in Phase 7.

**Phases 3–4**: Identical to V-01.

**Phase 5: Coverage and Quality Gate**

5-A: Deviation Budget Utilization (identical to V-01).
5-B: Constraint Chain Budget Utilization (identical to V-01).
5-C: Coverage Quality Gate: CLEAN | DEGRADED (identical to V-01).
5-D: Five coverage ratios (identical to V-02 — includes PATH_ADHERENCE_RATIO as 5th).
5-E: Constraint Chain Status Summary (identical to V-01).
5-F: Simulation Delta (PREDICTION_DEVIATION defects from CRITICAL paths are
FOUND_BY_SIMULATION_ONLY where the informal review method cannot consult the contract).

**Phase 6: Adversarial Turn Injection** (identical to V-01).

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-H

**Phases 6-A through 6-G**: Identical to V-01.

**Phase 6-H: Combined Plan Integrity and Path Adherence Audit** *(merged from D+E)*

Part 1 — Path Adherence Audit (from V-02 Phase 6-H):
```
For each turn with PREDICTION_MATCH:
  TURN_ID | PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED | CONSISTENT: PASS|FAIL
PATH_ADHERENCE_RATIO_VERIFIED: PASS|FAIL[mismatch count]
CRITICAL_PATH_ESCALATION_VERIFIED: PASS|FAIL (CRITICAL deviations at P1 minimum)
PLAN_TIER_OVERRIDE_PRESENT: PASS|FAIL (PLAN_TIER_OVERRIDE field on all CRITICAL deviation defects)
```

Part 2 — Plan Integrity Audit (from V-01 Phase 6-H):
```
For each EXECUTION_HALT block and each PLAN_TIER_OVERRIDE defect:
  ITEM_IN_PLAN: YES|NO
  CHAIN_REPAIR_IN_SCOPE: YES|NO (if EXECUTION_HALT)
  OVERRIDE_TIER_HONORED: YES|NO (PLAN_TIER_OVERRIDE: IMMEDIATE defects in IMMEDIATE tier)
For each PLAN_ITEM:
  DEPENDENCY_ORDER_VALID: YES|NO
PLAN_INTEGRITY_AUDIT: PASS|FAIL[cite]
DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND[cycle]
```

`[ROLE_COMPLETE: AUDITOR]`

---

### REMEDIATION PLANNER — Phase 7

Read all EXECUTION_HALT blocks, Phase 3-E ENTANGLEMENT_MAP, and Phase 2 PLAN_TIER_OVERRIDE
fields. Produce REMEDIATION_PLAN.

For each defect, declare:
```
PLAN_ID: RP-NN
DEFECT_REF: <Phase 2 DEFECT_ID>
SEVERITY_CLASS: <P0|P1|P2|P3>
SCOPE: <topics/transitions/session variables>
DEPENDENCY_ON: [RP-NN, ...] (from Phase 3-E ENABLES relationships)
PLAN_TIER: IMMEDIATE | NEXT_SPRINT | BACKLOG
TIER_RATIONALE: <severity-based tier or PLAN_TIER_OVERRIDE explanation>
CHAIN_REPAIR_ITEMS: [CONV-NN, ...] (from EXECUTION_HALT CHAIN_REPAIR; empty if no halt)
UNBLOCKED_BY: <observable confirmation>
```

Tier assignment rules (in priority order):
1. P0 defects → IMMEDIATE
2. PLAN_TIER_OVERRIDE: IMMEDIATE present (CRITICAL path deviation) → IMMEDIATE
3. P1 defects → NEXT_SPRINT
4. P2/P3 defects → BACKLOG

Topological sort: no PLAN_ITEM precedes any item in its DEPENDENCY_ON list.

Emit PLAN_SUMMARY after all PLAN_ITEMs:
`PLAN_ITEM_COUNT | IMMEDIATE_COUNT | NEXT_SPRINT_COUNT | BACKLOG_COUNT | DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND`

`[ROLE_COMPLETE: REMEDIATION PLANNER]`

---

## V-05 — Axes E + Inertia Extension: Turn Prediction Contract + STATUS_QUO_SIMULATION (Combined)

**Hypothesis:** The SIMULATION_DELTA section (C-35) categorizes defects as
FOUND_BY_SIMULATION_ONLY or FOUND_BY_BOTH, but the categorization is asserted rather
than demonstrated. A STATUS_QUO_SIMULATION — a parallel abbreviated trace using only
the team's declared informal review method — makes the gap concrete and undeniable:
the team's own method, run on the same scenario, produces a visible subset of the
findings. When combined with the Turn Prediction Contract (Axis E), PREDICTION_DEVIATION
defects are automatically FOUND_BY_SIMULATION_ONLY with a structural proof: informal
review does not consult path contracts, so path deviations are invisible to it by
construction. The STATUS_QUO_COVERAGE table makes this proof explicit and quantified.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

**Phases 0-A-1 through 0-A-9**: Identical to V-01.

**Phase 0-A-10: Turn Prediction Contract** *(from V-02)*
Identical to V-02 Phase 0-A-10 (HAPPY_PATH + up to 3 ALT_PATHs, PATH_CRITICALITY,
PREDICTED_TURN_SEQUENCE, TURN_PREDICTION_CONTRACT_SIGNED: YES).

**Phase 0-A-11: Status Quo Method Declaration** *(new in V-05)*
Declare the team's current informal review method before Phase 1 begins. This declaration
is used to construct the STATUS_QUO_SIMULATION in Phase 4-SQ.

```
STATUS_QUO_METHOD:
  METHOD_NAME: <e.g., "Manual topic-by-topic walkthrough", "Trigger phrase spot-check">
  METHOD_DESCRIPTION: <one paragraph describing what the team currently does>
  METHOD_COVERAGE: <what artifacts/paths the method naturally checks>
  METHOD_BLIND_SPOTS: <what the method structurally cannot check>
    - CONSTRAINT_VERDICTS: <YES|NO — does the method check per-invariant verdicts?>
    - CHAIN_EFFECTS: <YES|NO — does the method trace constraint propagation?>
    - TIMELINE_ANOMALIES: <YES|NO — does the method check variable lifecycle ordering?>
    - PREDICTION_CONTRACT: <YES|NO — does the method check against declared expected paths?>
    - CHAIN_BUDGET: <YES|NO — does the method check per-chain deviation thresholds?>
STATUS_QUO_METHOD_SIGNED: YES
```

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

All checks from V-01, plus:
```
PATHS_IN_CONTRACT: [PATH_ID, ...] (from Phase 0-A-10)
STATUS_QUO_METHOD_SIGNED: YES|NO
TURN_PREDICTION_CONTRACT_SIGNED: YES|NO
```
CONTRACT_AUDIT: PASS requires all deltas empty, STATUS_QUO_METHOD_SIGNED: YES,
and TURN_PREDICTION_CONTRACT_SIGNED: YES.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1–6

**DEVIATION_BUDGET**: Declare before Phase 1-S. LOCKED.
`P0_MAX | P1_MAX | P2_MAX | P3_MAX | BUDGET_RATIONALE`

**Phase 1-S**: SESSION_TIMELINE mutation log (authored before Phase 1; identical to V-01).

**Phase 1: Turn-by-Turn Trace**
All columns from V-01, plus PREDICTION_MATCH from V-02:
`... | PREDICTION_MATCH: ON_PATH[PATH_ID] | DEVIATION[PATH_ID, expected, actual] | OFF_ALL_PATHS`

**Phase 1-T**: Identical to V-02 (includes PATH_IDS_MATCHED).

**Phase 2: Defect Classification**
Nine structural defect classes (eight from V-01 + PREDICTION_DEVIATION from V-02).
PREDICTION_DEVIATION format identical to V-02.
P0 EXECUTION HALT GATE with CHAIN_BREAK_TRACE and CHAIN_REPAIR: identical to V-01.

**Phase 3**: Defect reproduction + Phase 3-E ENTANGLEMENT_MAP (identical to V-01).

**Phase 4**: Fallback, escalation, disambiguation (identical to V-01).

**Phase 4-SQ: Status Quo Simulation** *(new in V-05)*
Re-run the same conversation scenario using ONLY the declared STATUS_QUO_METHOD from
Phase 0-A-11. This is an abbreviated trace:
- No CONSTRAINT_VERDICTS
- No CHAIN_EFFECTS
- No PREDICTION_MATCH (the informal method does not consult path contracts)
- No TIMELINE_ANOMALY tracking
- No CHAIN_BUDGET tracking

For each turn in the status-quo trace, write:
`TURN_ID | TOPIC_MATCHED | AGENT_RESPONSE_SUMMARY | SQ_DEFECT_FOUND: YES|NO | SQ_DEFECT_CLASS (if found) | REMARKS`

After the abbreviated trace, write STATUS_QUO_FINDINGS:
```
STATUS_QUO_FINDINGS:
  TOTAL_TURNS: <count>
  SQ_DEFECTS_FOUND: [DEFECT_CLASS: description, ...]
  SQ_DEFECTS_NOT_FOUND: (determined after comparing to Phase 2 FOUND defects)
```

**Phase 5: Coverage and Quality Gate**

5-A: Deviation Budget Utilization (identical to V-01).
5-B: Constraint Chain Budget Utilization (identical to V-01).
5-C: Coverage Quality Gate: CLEAN | DEGRADED (identical to V-01).
5-D: Five coverage ratios (identical to V-02 — includes PATH_ADHERENCE_RATIO as 5th).
5-E: Constraint Chain Status Summary (identical to V-01).

**Phase 5-F: Status Quo Coverage Table** *(extended from C-35 in V-05)*
Instead of a simple SIMULATION_DELTA categorization, produce a STATUS_QUO_COVERAGE table.

For each FOUND defect from Phase 2:
```
DEFECT_ID | DEFECT_CLASS | FOUND_BY_SIMULATION | FOUND_BY_STATUS_QUO | DETECTION_METHOD
           | SQ_BLIND_SPOT (which METHOD_BLIND_SPOT explains why STATUS_QUO missed it, if applicable)
```

DETECTION_METHOD values:
- FOUND_BY_SIMULATION_ONLY: simulation found it; STATUS_QUO_SIMULATION did not
- FOUND_BY_BOTH: both methods found it
- FOUND_BY_STATUS_QUO_ONLY: STATUS_QUO found it but simulation did not (unexpected; flag as anomaly)

Structural rules for automatic classification:
- PREDICTION_DEVIATION defects are FOUND_BY_SIMULATION_ONLY if STATUS_QUO METHOD_BLIND_SPOTS.PREDICTION_CONTRACT: NO (method does not check path contracts)
- CHAIN_BUDGET_EXCEEDED defects are FOUND_BY_SIMULATION_ONLY if METHOD_BLIND_SPOTS.CHAIN_BUDGET: NO
- TIMELINE_ANOMALY defects are FOUND_BY_SIMULATION_ONLY if METHOD_BLIND_SPOTS.TIMELINE_ANOMALIES: NO

After the table, emit:
```
STATUS_QUO_GAP_SUMMARY:
  FOUND_BY_SIMULATION_ONLY_COUNT: <count>
  FOUND_BY_SIMULATION_ONLY_LIST: [DEFECT_ID, ...]
  STRUCTURAL_BLIND_SPOTS_ACTIVATED: [METHOD_BLIND_SPOT keys that contributed, ...]
  STATUS_QUO_GAP_NARRATIVE: <one paragraph explaining what manual review structurally cannot see>
```

**Phase 6: Adversarial Turn Injection** (identical to V-01).

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-H

**Phases 6-A through 6-G**: Identical to V-01. Phase 6-A SIMULATION_DELTA_COMPLETE
verification now covers STATUS_QUO_COVERAGE table completeness (every Phase 2 FOUND
defect appears in exactly one DETECTION_METHOD category).

**Phase 6-H: Status Quo Coverage and Path Adherence Audit** *(new in V-05)*

Part 1 — Status Quo Coverage Audit:
```
For each FOUND defect in Phase 2:
  DEFECT_ID | DETECTION_METHOD_REPORTED | DETECTION_METHOD_AUDITED | CONSISTENT: PASS|FAIL
  (Audit: does the SQ_BLIND_SPOT cited match the Method's declared METHOD_BLIND_SPOTS?)

AUTOMATIC_CLASSIFICATION_VERIFIED:
  PREDICTION_DEVIATION_CLASSIFIED_CORRECTLY: PASS|FAIL
  CHAIN_BUDGET_EXCEEDED_CLASSIFIED_CORRECTLY: PASS|FAIL
  TIMELINE_ANOMALY_CLASSIFIED_CORRECTLY: PASS|FAIL

STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL
```

Part 2 — Path Adherence Audit (from V-02 Phase 6-H):
```
For each turn with PREDICTION_MATCH:
  TURN_ID | PREDICTION_MATCH_REPORTED | PREDICTION_MATCH_AUDITED | CONSISTENT: PASS|FAIL
PATH_ADHERENCE_RATIO_VERIFIED: PASS|FAIL[mismatch count]
CRITICAL_PATH_ESCALATION_VERIFIED: PASS|FAIL
PATH_ADHERENCE_AUDIT: PASS|FAIL
```

`[ROLE_COMPLETE: AUDITOR]`
