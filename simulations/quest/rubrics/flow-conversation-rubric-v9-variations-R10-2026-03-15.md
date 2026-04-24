# Quest Variations — flow-conversation — Round 10 (v9 rubric)

**Date:** 2026-03-15 | **Rubric version:** v9 | **Max score:** 136

---

## Variation Axes Selected

**Single-axis (3):**
- **Axis A — Output format (mutation-first authoring)**: Phase 1-S SESSION_TIMELINE is
  authored before Phase 1. SESSION_STATE in Phase 1 is derived from Phase 1-S replay,
  not independently populated. This eliminates the consistency gap Phase 6-E was designed
  to catch after the fact.
- **Axis B — Inertia framing**: Each Phase 2 defect row carries a STATUS_QUO_GAP field
  declaring what an informal flow review would fail to detect. Phase 5 adds a
  SIMULATION_DELTA block listing findings invisible to status-quo review.
- **Axis C — Output format (timeline-headline coverage)**: Phase 5 is restructured to
  report TIMELINE_ANOMALY_RATE first as a quality gate (CLEAN | DEGRADED). Coverage
  ratios below the gate are CONFIRMED when CLEAN and PROVISIONAL when DEGRADED.

**Combined (2):**
- **Axes A + Role sequence**: Contract Auditor gate — a fourth role (CONTRACT AUDITOR)
  inserted between Topology Architect and Developer verifies SESSION_VARIABLE_TIMELINE_CONTRACT
  completeness before any Phase 1 tracing begins. Developer may not start Phase 1 until
  CONTRACT_AUDIT: PASS.
- **Axes B + Phrasing register**: Inertia framing combined with constraint-satisfaction
  register — Phase 0-D declares named conversation constraints (CONV-NN), Phase 1 carries
  inline CONSTRAINT_VERDICTS, and STATUS_QUO_GAP annotations explain why each constraint
  cannot be verified by informal review.

---

## V-01 — Axis A: Mutation-First Tracing (Single-Axis)

**Hypothesis:** Inverting the authoring order so Phase 1-S SESSION_TIMELINE is populated
before Phase 1 SESSION_STATE eliminates the failure mode where a developer populates
SESSION_STATE directly and then writes Phase 1-S post-hoc to match. If SESSION_STATE
must be reconstructed from Phase 1-S replay, the developer cannot introduce session
state values that lack a corresponding mutation event. This turns the C-29 audit from a
retroactive discrepancy-finder into a structural impossibility.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Two roles operate in strict phase-gate order:

**DEVELOPER** → **AUDITOR**

The Auditor may not begin until `[ROLE_COMPLETE: DEVELOPER]` is present.

---

### DEVELOPER — Phases 0 through 6

**Phase 0-D: Pre-Execution Contract**

Complete all declarations before any trace output.

**0-D-1 Topic Registry**

For each topic:
```
TOPIC_ID | NAME | TRIGGER_PHRASES | ENTRY_CONDITION
         | EXIT_NODES | SLOT_FILLING: YES|NO
         | SESSION_VARS_WRITTEN | SESSION_VARS_READ
```
First encounter of an undeclared topic in Phase 1 is a CONTRACT_GAP finding.

**0-D-2 Vocabulary Gate**

Permitted: topic, trigger phrase, condition, fallback topic, escalation, session
variable, slot, entity, adaptive card, Power Automate flow, escalation node.
Prohibited: intent, utterance class, NLU model, chatbot, dialog node, bot flow.

`VOCABULARY_GATE: SIGNED`

**0-D-3 Session Variable Registry**
```
VAR_ID | TYPE | INITIAL_VALUE | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL
```

**0-D-4 Topology Invariants**

Declare all conversation-level invariants before tracing:
```
INVARIANT-TOPO-NN: <statement> | FALSIFICATION: <condition>
INVARIANT-SV-NN:   <statement> | FALSIFICATION: <condition>
```
Every DEVIATES verdict and every Phase 2 defect must cite at least one INVARIANT-ID.

**0-D-5 TRANSITION_MAP**
```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN
         | condition: <text> | REQUIRED|OPTIONAL
```
Unexercised REQUIRED edges are orphaned-edge defects; recovery verdict
`UNRECOVERABLE[missing edge]`.

**0-D-6 REACHABILITY_MAP**
```
ENTRY_TOPIC: TOPIC-NN
REACHABLE:   [TOPIC-NN, ...]
ORPHANED:    [TOPIC-NN, ...]
```
Orphaned topics are ORPHAN defects (fifth structural defect class).

**0-D-7 SLOT_PATH_MAP**

For every topic with SLOT_FILLING: YES:
```
SLOT_PATH-NN     | TOPIC_ID | SLOTS_REQUIRED | CANONICAL_TURNS: N
                 | path_type: CANONICAL
SLOT_PATH-NN-SC1 | TOPIC_ID | SLOTS_SKIPPED: [slot_1]
                 | path_type: SHORT_CIRCUIT | trigger_condition: <text>
```
Unexercised canonical SLOT_PATH-NN is a SLOT_GAP defect (sixth structural defect class).

**0-D-8 SESSION_VARIABLE_TIMELINE_CONTRACT**

For every variable in 0-D-3:
```
VAR_ID | FIRST_WRITTEN_TOPIC: TOPIC-NN
       | CLEARED_BY: TOPIC-NN|NEVER
       | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```
All variables in 0-D-3 must appear here. This contract is sealed at Phase 0 close.
Auditor phases may not grant retroactive dispensation for undeclared lifecycle events.

`PHASE_0_CONTRACT: SEALED`

---

**Phase 1-S: SESSION_TIMELINE** ← *author this before Phase 1*

**Authoring rule**: Populate Phase 1-S before filling the SESSION_STATE column in
Phase 1. The SESSION_STATE column in Phase 1 is derived by replaying Phase 1-S
mutations in turn order through the current TURN_ID. Do not independently author
SESSION_STATE; reconstruct it from Phase 1-S.

For every turn in which any session variable is active, mutated, or cleared:
```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONTRACT_MATCH: CONFORMS|VIOLATES[reason]
        | TIMELINE_ANOMALY: YES|NO | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

TIMELINE_ANOMALY: YES when:
- READ after CLEARED_BY has fired and READ_AFTER_CLEARED = FORBIDDEN → READ_AFTER_CLEAR
- WRITE in a TOPIC_ID not declared as FIRST_WRITTEN_TOPIC and no contract override → OFF_CONTRACT_WRITE
- READ where most recent prior mutation was CLEAR with no intervening WRITE → STALE_READ

Each TIMELINE_ANOMALY: YES row generates a TIMELINE_ANOMALY defect entry in Phase 2.

---

**Phase 1: Turn-by-Turn Trace**

For each turn:
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | INVARIANT_CONFORMANCE | CONFORMANCE
```

- `SESSION_STATE`: derived from Phase 1-S replay through this TURN_ID. Must not
  contradict any POST_VALUE recorded in Phase 1-S for this turn.
- `SLOT_PATH_ID`: cite SLOT_PATH-NN from 0-D-7 when inside a slot-fill sequence; N/A otherwise.
- `TRANSITION_ID`: cite TRANS-NN from 0-D-5.
- `INVARIANT_CONFORMANCE`: HOLDS | VIOLATED[INVARIANT-ID]
- `CONFORMANCE`: CONFORMS | DEVIATES[INVARIANT-ID]

No turns may be skipped. No topics may be referenced absent from 0-D-1.

**Phase 1-T: Topic Aggregate** (additive to Phase 1, not replacing it)

One row per topic visited:
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```
CONFORMANCE_ROLLUP must match the DEVIATES count for this topic in Phase 1.
A CONFORMS rollup for a topic with at least one DEVIATES turn is a
TOPIC_ROLLUP_MISMATCH (flagged in Phase 6-D).

---

**Phase 2: Defect Classification**

Classify all seven defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE (if FOUND; for TIMELINE_ANOMALY cite VAR_ID and TURN_ID from Phase 1-S)
             | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
```

Typing rules (hard constraints):
- CONFIRMED_ABSENT: `SEVERITY_CLASS = EXEMPT`. INVARIANT_CITE required.
- FOUND: `SEVERITY_CLASS` ∈ {P0, P1, P2, P3}. INVARIANT_CITE required. Both columns must coexist.
- RECOVERY for FOUND: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` | `UNRECOVERABLE[reason]`
- MASKED_BY: `RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`
- ENTANGLEMENT_VERDICT: `ISOLATED` | `ENABLES[DEFECT_CLASS]` | `MASKED_BY[DEFECT_CLASS]`

Severity: P0 (session corruption/unescapable loop), P1 (dead end, no fallback),
P2 (suboptimal, recoverable ≤ 3 turns), P3 (cosmetic).

**Phase 3: Defect Reproduction**

For each FOUND defect: minimal utterance sequence that triggers it + observable failure mode.

**Phase 3-E: ENTANGLEMENT_MAP**
```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION: UPSTREAM|DOWNSTREAM
```

**Phase 4: Fallback Chain + Escalation + Disambiguation**

Trace at least one fallback path to completion: no topic match → fallback topic →
escalation or graceful exit. Show every node. Record TRANSITION_IDs.

Trace at least one escalation path: trigger condition, handoff node name, SESSION_STATE
at handoff, agent receipt confirmation. Escalation is CONFIRMED_ABSENT only if no
escalation topic was declared in 0-D-1.

If INTENT_COLLISION was FOUND in Phase 2, propose a disambiguation strategy (entity
enrichment, condition ordering, trigger phrase refactor) with rationale.

**Phase 5: Coverage Metrics**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events  (from Phase 1-S)
TOPIC_COVERAGE:        reachable_visited / total_reachable            (from 0-D-6)
TRANSITION_COVERAGE:   transitions_exercised / total_declared         (from 0-D-5)
SLOT_PATH_COVERAGE:    slot_paths_exercised / total_declared          (from 0-D-7)
```
Report all four as fractions with numerator and denominator visible. ORPHAN topics
included in TOPIC_COVERAGE denominator. TIMELINE_ANOMALY_RATE > 0 is a quality signal
independent of the other three ratios; a trace may achieve 100% on the first three
while TIMELINE_ANOMALY_RATE > 0.

**Phase 6: Adversarial Turn Injection**

Inject at least one adversarial utterance: off-topic, ambiguous, or contradictory
mid-conversation. Record TURN_ID, topic match or miss, TRANSITION_ID, SLOT_PATH_ID
(if a slot-fill was interrupted). Emit Phase 1-S entries for adversarial turns. Trace
recovery to completion.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-E

The Auditor operates on completed Developer output. It does not revise; it audits.
Auditor findings may not retroactively alter Developer rows.

**Phase 6-A: Coverage Audit**

Verify all four coverage ratios against declared topology:
```
TIMELINE_ANOMALY_RATE_VERIFIED:   PASS | FAIL[discrepancy — cite Phase 1-S total event count]
TOPIC_COVERAGE_VERIFIED:          PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED:     PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
```

**Phase 6-B: Severity Co-Residency Audit**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS|FAIL
```
Every FOUND row: both columns populated. Every CONFIRMED_ABSENT row: EXEMPT.

**Phase 6-C: Entanglement Consistency Audit**
```
DEFECT | ENTANGLEMENT_VERDICT | SUPPORTING_TURN | CONSISTENCY: PASS|FAIL[cite]
```
A MASKED_BY or ENABLES claim without supporting Phase 1 turn evidence is a Phase 6-C failure.

**Phase 6-D: Topic Aggregate Consistency Audit**

Cross-check Phase 1-T conformance_rollup against Phase 1 DEVIATES count per topic:
```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS|FAIL
TOPIC_ROLLUP_MISMATCH_COUNT: N
```
This is the mandatory gate for C-24. C-24 cannot achieve full credit without PASS here.

**Phase 6-E: Session Timeline Consistency Audit**

Replay Phase 1-S mutations in turn sequence. Reconstruct SESSION_STATE per turn.
Compare against Phase 1 SESSION_STATE:
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```
Any Phase 1-S TIMELINE_ANOMALY: YES row not cited in a Phase 2 TIMELINE_ANOMALY
defect row is a Phase 6-E finding.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-02 — Axis B: Inertia Framing (Single-Axis)

**Hypothesis:** Annotating every Phase 2 defect row with STATUS_QUO_GAP — what an
informal review process (whiteboard walkthrough, manual test, config code review)
would fail to detect — makes the simulation artifact self-justifying and forces the
developer to articulate why each finding is a structured-simulation finding rather
than something routine review catches. The inertia competitor is the team that says
"we already reviewed this flow." The Phase 5 SIMULATION_DELTA block names findings
that are structurally invisible to status-quo methods, making the detection value
explicit rather than implied.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Two roles operate in strict phase-gate order:

**DEVELOPER** → **AUDITOR**

The Auditor may not begin until `[ROLE_COMPLETE: DEVELOPER]` is present.

---

### DEVELOPER — Phases 0 through 6

**Phase 0-D: Pre-Execution Contract**

**0-D-0 Status-Quo Baseline** ← *new in V-02*

Declare what review method the team currently uses in place of structured conversation
simulation:
```
STATUS_QUO_METHOD: <e.g., manual walkthrough, whiteboard diagram, developer test>
KNOWN_GAPS:        <what the team acknowledges it does not currently check>
```
This declaration is the inertia reference point. Every defect finding in Phase 2 will
be evaluated against it.

**0-D-1 Topic Registry**
```
TOPIC_ID | NAME | TRIGGER_PHRASES | ENTRY_CONDITION
         | EXIT_NODES | SLOT_FILLING: YES|NO
         | SESSION_VARS_WRITTEN | SESSION_VARS_READ
```

**0-D-2 Vocabulary Gate**

Permitted: topic, trigger phrase, condition, fallback topic, escalation, session
variable, slot, entity, adaptive card, Power Automate flow.
Prohibited: intent, utterance class, NLU model, chatbot, dialog node.

`VOCABULARY_GATE: SIGNED`

**0-D-3 Session Variable Registry**
```
VAR_ID | TYPE | INITIAL_VALUE | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL
```

**0-D-4 Topology Invariants**
```
INVARIANT-TOPO-NN: <statement> | FALSIFICATION: <condition>
INVARIANT-SV-NN:   <statement> | FALSIFICATION: <condition>
```

**0-D-5 TRANSITION_MAP**
```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN
         | condition: <text> | REQUIRED|OPTIONAL
```

**0-D-6 REACHABILITY_MAP**
```
ENTRY_TOPIC: TOPIC-NN
REACHABLE:   [TOPIC-NN, ...]
ORPHANED:    [TOPIC-NN, ...]
```

**0-D-7 SLOT_PATH_MAP**

For every topic with SLOT_FILLING: YES, declare canonical and short-circuit paths.

**0-D-8 SESSION_VARIABLE_TIMELINE_CONTRACT**

For every variable in 0-D-3:
```
VAR_ID | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```

`PHASE_0_CONTRACT: SEALED`

---

**Phase 1: Turn-by-Turn Trace**
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | INVARIANT_CONFORMANCE | CONFORMANCE
```

**Phase 1-T: Topic Aggregate** (additive to Phase 1)
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

**Phase 1-S: SESSION_TIMELINE** (additive to Phase 1 and Phase 1-T)
```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONTRACT_MATCH: CONFORMS|VIOLATES[reason]
        | TIMELINE_ANOMALY: YES|NO | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

---

**Phase 2: Defect Classification** ← *STATUS_QUO_GAP column added*

Classify all seven defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY
             | ENTANGLEMENT_VERDICT
             | STATUS_QUO_GAP: <what the STATUS_QUO_METHOD in 0-D-0 would miss>
```

STATUS_QUO_GAP rules:
- FOUND rows: explain the specific property of this defect that makes it invisible to
  the declared STATUS_QUO_METHOD. Reference the method by name.
- CONFIRMED_ABSENT rows: state "NOT_APPLICABLE — absence confirmed through [invariant
  cite]; status-quo method would reach the same conclusion because [reason]."

Typing rules:
- CONFIRMED_ABSENT: SEVERITY_CLASS = EXEMPT. INVARIANT_CITE required.
- FOUND: SEVERITY_CLASS ∈ {P0, P1, P2, P3}. INVARIANT_CITE required (both coexist).
- RECOVERY: RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]
- MASKED_BY: RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]
- ENTANGLEMENT_VERDICT: ISOLATED | ENABLES[DEFECT_CLASS] | MASKED_BY[DEFECT_CLASS]

**Phase 3: Defect Reproduction**

For each FOUND defect: minimal utterance sequence + observable failure mode.

**Phase 3-E: ENTANGLEMENT_MAP**
```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION: UPSTREAM|DOWNSTREAM
```

**Phase 4: Fallback Chain + Escalation + Disambiguation**

Trace at least one fallback path to completion. Trace at least one escalation path
(trigger condition, handoff node, SESSION_STATE at handoff, agent receipt confirmation).
ESCALATION is CONFIRMED_ABSENT only if no escalation topic exists in 0-D-1.

For any FOUND INTENT_COLLISION: propose disambiguation strategy with rationale.

**Phase 5: Coverage Metrics + Simulation Delta** ← *SIMULATION_DELTA new in V-02*

```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
TOPIC_COVERAGE:        reachable_visited / total_reachable
TRANSITION_COVERAGE:   transitions_exercised / total_declared
SLOT_PATH_COVERAGE:    slot_paths_exercised / total_declared
```

**SIMULATION_DELTA** ← enumerate findings invisible to STATUS_QUO_METHOD:

For each FOUND defect where STATUS_QUO_GAP identifies a detection gap, emit one row:
```
DEFECT_CLASS | WHY_INVISIBLE_TO_STATUS_QUO | DETECTION_METHOD: <what in Phase 0-D-N or Phase 1-S surfaced it>
```

SIMULATION_DELTA is empty if every FOUND defect would also have been caught by the
declared STATUS_QUO_METHOD. If SIMULATION_DELTA is empty, the Developer must justify
the claim with reference to the specific property of each defect class checked.

**Phase 6: Adversarial Turn Injection**

At least one adversarial scenario. Show TURN_ID, TRANSITION_ID, state delta,
Phase 1-S entries for adversarial turns, and recovery trace.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-E

**Phase 6-A: Coverage Audit**
```
TIMELINE_ANOMALY_RATE_VERIFIED:   PASS | FAIL[discrepancy]
TOPIC_COVERAGE_VERIFIED:          PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED:     PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
```

Verify SIMULATION_DELTA completeness: every FOUND defect with STATUS_QUO_GAP citing a
detection gap must appear in SIMULATION_DELTA.
```
SIMULATION_DELTA_COMPLETE: PASS | FAIL[missing defect class]
```

**Phase 6-B: Severity Co-Residency Audit**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS|FAIL
```

**Phase 6-C: Entanglement Consistency Audit**
```
DEFECT | ENTANGLEMENT_VERDICT | SUPPORTING_TURN | CONSISTENCY: PASS|FAIL[cite]
```

**Phase 6-D: Topic Aggregate Consistency Audit**
```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS|FAIL
TOPIC_ROLLUP_MISMATCH_COUNT: N
```
Mandatory gate for C-24.

**Phase 6-E: Session Timeline Consistency Audit**
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```
Any TIMELINE_ANOMALY: YES row in Phase 1-S not cited in Phase 2 is a Phase 6-E finding.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-03 — Axis C: Timeline-Headline Coverage (Single-Axis)

**Hypothesis:** Reporting TIMELINE_ANOMALY_RATE first in Phase 5 as a quality gate
(CLEAN | DEGRADED) and marking downstream coverage ratios PROVISIONAL when DEGRADED
forces the developer to treat temporal state correctness as the primary quality signal.
If timeline anomalies are present, conversation paths may have followed incorrect
branches — making topic, transition, and slot-path coverage counts potentially
misleading. The gate makes this dependency explicit. A developer who achieves high
TOPIC_COVERAGE but has TIMELINE_ANOMALY_RATE > 0 must acknowledge the provisional
nature of their coverage claims before reporting them.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Two roles operate in strict phase-gate order:

**DEVELOPER** → **AUDITOR**

The Auditor may not begin until `[ROLE_COMPLETE: DEVELOPER]` is present.

---

### DEVELOPER — Phases 0 through 6

**Phase 0-D: Pre-Execution Contract**

**0-D-1** Topic Registry: TOPIC_ID, trigger phrases, entry condition, exit nodes,
SLOT_FILLING flag, session vars written/read.

**0-D-2** Vocabulary Gate. Permitted: topic, trigger phrase, condition, fallback topic,
escalation, session variable, slot, entity, adaptive card, Power Automate flow.
Prohibited: intent, utterance class, NLU model, chatbot, dialog node.
`VOCABULARY_GATE: SIGNED`

**0-D-3** Session Variable Registry: VAR_ID, type, initial value, persistence class.

**0-D-4** Topology Invariants: INVARIANT-TOPO-NN and INVARIANT-SV-NN with falsification
conditions. Every DEVIATES verdict and every Phase 2 defect must cite at least one.

**0-D-5** TRANSITION_MAP: TRANS-NN | source | target | condition | REQUIRED|OPTIONAL.
Unexercised REQUIRED edges are orphaned-edge defects.

**0-D-6** REACHABILITY_MAP: ENTRY_TOPIC, REACHABLE list, ORPHANED list.
Orphaned topics are ORPHAN defects.

**0-D-7** SLOT_PATH_MAP: canonical and short-circuit paths for every slot-filling topic.
Unexercised canonical paths are SLOT_GAP defects.

**0-D-8** SESSION_VARIABLE_TIMELINE_CONTRACT: for every variable in 0-D-3:
FIRST_WRITTEN_TOPIC, CLEARED_BY, READ_AFTER_CLEARED: FORBIDDEN|ALLOWED.
Contract sealed at Phase 0 close.

`PHASE_0_CONTRACT: SEALED`

---

**Phase 1: Turn-by-Turn Trace**
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | INVARIANT_CONFORMANCE | CONFORMANCE
```

**Phase 1-T: Topic Aggregate** (additive to Phase 1)
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

**Phase 1-S: SESSION_TIMELINE** (additive to Phase 1 and Phase 1-T)
```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONTRACT_MATCH: CONFORMS|VIOLATES[reason]
        | TIMELINE_ANOMALY: YES|NO | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

---

**Phase 2: Defect Classification**

Classify all seven defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
```

Typing rules: CONFIRMED_ABSENT → SEVERITY_CLASS = EXEMPT + INVARIANT_CITE required.
FOUND → SEVERITY_CLASS ∈ {P0, P1, P2, P3} + INVARIANT_CITE required (both coexist).
RECOVERY: RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason].
MASKED_BY: RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS].

**Phase 3: Defect Reproduction + Phase 3-E: ENTANGLEMENT_MAP**

Phase 3: For each FOUND defect — minimal utterance sequence + observable failure mode.

Phase 3-E:
```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION: UPSTREAM|DOWNSTREAM
```

**Phase 4: Fallback Chain + Escalation + Disambiguation**

Trace at least one fallback path to completion with full node chain and TRANSITION_IDs.
Trace at least one escalation path (trigger, handoff node, SESSION_STATE at handoff,
agent receipt confirmation). Escalation CONFIRMED_ABSENT only if no escalation topic
in 0-D-1. For FOUND INTENT_COLLISION: propose disambiguation strategy with rationale.

**Phase 5: Coverage Metrics** ← *restructured with quality gate*

**5-A: Temporal Quality Gate**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
COVERAGE_QUALITY_GATE: CLEAN (anomalies_found = 0) | DEGRADED (anomalies_found > 0)
```

If DEGRADED: emit DEGRADED_COVERAGE_NOTE explaining which coverage ratios may be
misleading and why. Specify: which TIMELINE_ANOMALY types were found, which topics
were visited during anomalous turns, and which transitions were exercised during
those turns. Ratios reported in 5-B are marked PROVISIONAL until anomalies are resolved.

```
DEGRADED_COVERAGE_NOTE: <anomaly types> affected topic visits in [TOPIC-NN, ...],
transitions [TRANS-NN, ...]. Coverage ratios below are PROVISIONAL pending resolution.
```

**5-B: Coverage Ratios**
```
STATUS: CONFIRMED (gate = CLEAN) | PROVISIONAL (gate = DEGRADED)

TOPIC_COVERAGE:      reachable_visited / total_reachable          (denominator from 0-D-6)
TRANSITION_COVERAGE: transitions_exercised / total_declared        (denominator from 0-D-5)
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared         (denominator from 0-D-7)
```

Report all three with numerator and denominator visible. ORPHAN topics in denominator.

**Phase 6: Adversarial Turn Injection**

At least one adversarial scenario. Show TURN_ID, TRANSITION_ID, state delta, Phase 1-S
entries for adversarial turns, recovery trace.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-E

**Phase 6-A: Coverage Audit**

Verify the quality gate verdict first:
```
QUALITY_GATE_VERIFIED: PASS | FAIL[anomaly count mismatch vs Phase 1-S]
COVERAGE_STATUS_APPROPRIATE: PASS | FAIL[ratios marked CONFIRMED when DEGRADED, or vice versa]
```

Then verify ratio denominators:
```
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:  PASS | FAIL[discrepancy]
```

If DEGRADED_COVERAGE_NOTE was required but absent, flag as Phase 6-A finding.

**Phase 6-B: Severity Co-Residency Audit**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS|FAIL
```

**Phase 6-C: Entanglement Consistency Audit**
```
DEFECT | ENTANGLEMENT_VERDICT | SUPPORTING_TURN | CONSISTENCY: PASS|FAIL[cite]
```

**Phase 6-D: Topic Aggregate Consistency Audit**
```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS|FAIL
TOPIC_ROLLUP_MISMATCH_COUNT: N
```
Mandatory gate for C-24.

**Phase 6-E: Session Timeline Consistency Audit**

Replay Phase 1-S mutations per turn. Compare reconstructed SESSION_STATE against Phase 1:
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```
Any TIMELINE_ANOMALY: YES row in Phase 1-S not cited in Phase 2 is a Phase 6-E finding.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-04 — Axes A + Role Sequence: Contract Auditor Gate (Combined)

**Hypothesis:** Inserting a CONTRACT AUDITOR role between the Topology Architect and
Developer — whose sole function is to verify SESSION_VARIABLE_TIMELINE_CONTRACT
completeness and internal consistency before any Phase 1 tracing begins — makes C-25 a
hard pre-execution gate rather than a documentation requirement. The failure mode in
prior rounds: underdeclared contracts discovered only in Phase 6-E, after all trace
work was complete. A Contract Auditor gate eliminates retroactive contract-gap
rationalization and combines with mutation-first tracing (V-01 axis) to ensure that
both the pre-execution commitment and the trace evidence are structurally sound before
any SESSION_STATE is authored.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

The Topology Architect produces the signed topology contract. All downstream roles are
bound to it; none may modify it.

**Phase 0-A-1: Topic Inventory**
```
TOPIC_ID | NAME | TRIGGER_PHRASES | ENTRY_CONDITION
         | EXIT_NODES | SLOT_FILLING: YES|NO
         | SESSION_VARS_WRITTEN | SESSION_VARS_READ
```

**Phase 0-A-2: REACHABILITY_MAP**
```
ENTRY_TOPIC: TOPIC-NN
REACHABLE:   [TOPIC-NN, ...]
ORPHANED:    [TOPIC-NN, ...]
```
Orphaned topics are ORPHAN defects.

**Phase 0-A-3: TRANSITION_MAP**
```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN
         | condition: <text> | REQUIRED|OPTIONAL
```

**Phase 0-A-4: SLOT_PATH_MAP**

For every SLOT_FILLING: YES topic, declare canonical and short-circuit paths:
```
SLOT_PATH-NN     | TOPIC_ID | SLOTS_REQUIRED | CANONICAL_TURNS: N | path_type: CANONICAL
SLOT_PATH-NN-SC1 | TOPIC_ID | SLOTS_SKIPPED | path_type: SHORT_CIRCUIT | trigger_condition: <text>
```

**Phase 0-A-5: SEVERITY_CLASS_MAP**
```
P0 | CRITICAL      — session corruption or unescapable loop
P1 | HIGH          — dead end with no fallback
P2 | MEDIUM        — suboptimal but recoverable <= 3 turns
P3 | LOW           — cosmetic or redundant
EXEMPT             — CONFIRMED_ABSENT rows
```

**Phase 0-A-6: SESSION_VARIABLE_TIMELINE_CONTRACT**

For every session variable the bot may write or read:
```
VAR_ID | FIRST_WRITTEN_TOPIC: TOPIC-NN
       | CLEARED_BY: TOPIC-NN|NEVER
       | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
       | AUTHORIZED_REWRITERS: [TOPIC-NN, ...] | NONE
```
`AUTHORIZED_REWRITERS`: topics other than FIRST_WRITTEN_TOPIC that may WRITE this
variable without generating an OFF_CONTRACT_WRITE anomaly. Empty if only
FIRST_WRITTEN_TOPIC may write.

**Phase 0-A-7: Topology Invariants**
```
INVARIANT-TOPO-NN: <statement> | FALSIFICATION: <condition>
INVARIANT-SV-NN:   <statement> | FALSIFICATION: <condition>
```

`[ROLE_COMPLETE: TOPOLOGY_ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA ← *new role in V-04*

The Contract Auditor has one job: verify that Phase 0-A-6 SESSION_VARIABLE_TIMELINE_CONTRACT
is complete and internally consistent before the Developer begins tracing. The Developer
may not begin Phase 1 until CONTRACT_AUDIT: PASS.

**Phase 0-CA-1: Coverage Check**

Every variable present in Phase 0-A-1 SESSION_VARS_WRITTEN or SESSION_VARS_READ across
all topics must have an entry in Phase 0-A-6. Missing entries are COVERAGE_GAPS.
```
VARS_IN_TOPOLOGY:   [VAR_ID, ...]  (union of all SESSION_VARS_WRITTEN + SESSION_VARS_READ across all topics)
VARS_IN_CONTRACT:   [VAR_ID, ...]  (from Phase 0-A-6)
COVERAGE_GAPS:      [VAR_ID, ...] | NONE
```

**Phase 0-CA-2: Lifecycle Consistency Check**

For each variable in Phase 0-A-6, verify internal consistency:
```
VAR_ID | CLEARED_BY_REACHABLE: PASS|FAIL[TOPIC-NN unreachable per 0-A-2]
       | AUTHORIZED_REWRITERS_REACHABLE: PASS|FAIL[TOPIC-NN unreachable per 0-A-2]
       | FIRST_WRITTEN_REACHABLE: PASS|FAIL[TOPIC-NN unreachable per 0-A-2]
       | LIFECYCLE_CONSISTENT: PASS|FAIL[reason]
```

**Phase 0-CA-3: Contract Audit Verdict**
```
CONTRACT_AUDIT: PASS | BLOCKED[reason: COVERAGE_GAP|LIFECYCLE_INCONSISTENCY|UNREACHABLE_TOPIC]
```

If CONTRACT_AUDIT: BLOCKED, the Developer's first output must be a CONTRACT_REMEDIATION
section resolving all BLOCKED findings before any Phase 1 turn is traced.

`[ROLE_COMPLETE: CONTRACT_AUDITOR]`

---

### DEVELOPER — Phases 0-D through 6

The Developer is bound to the Topology Architect's contract and the Contract Auditor's
verdict. It may not add, remove, or rename any topology element from Phase 0-A. Any
topology element discovered absent from Phase 0-A must be raised as a CONTRACT_GAP flag.

**Phase 0-D: Domain Binding**
```
CS_VOCABULARY_BINDING: [topic, trigger phrase, condition, fallback topic, escalation,
                        session variable, slot, entity, Power Automate flow]
PROHIBITED_TERMS:       [intent, chatbot, NLU model, dialog node]
CONTRACT_SOURCE:        Phase 0-A
CONTRACT_AUDIT_CITED:   PASS  (must match Phase 0-CA-3 verdict)
CONTRACT_GAPS:          [NONE | item description]
```

**Phase 1-S: SESSION_TIMELINE** ← *author before Phase 1 SESSION_STATE*

Populate Phase 1-S first. Phase 1 SESSION_STATE is derived from Phase 1-S replay.
```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONTRACT_MATCH: CONFORMS|VIOLATES[reason]
        | TIMELINE_ANOMALY: YES|NO
        | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

AUTHORIZED_REWRITERS from Phase 0-A-6 are recognized: a WRITE in an authorized
re-writer topic is not an OFF_CONTRACT_WRITE.

**Phase 1: Turn-by-Turn Trace**
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | INVARIANT_CONFORMANCE | CONFORMANCE
```
SESSION_STATE derived from Phase 1-S replay. TRANSITION_ID and SLOT_PATH_ID cite
Phase 0-A-3 and Phase 0-A-4 entries respectively.

**Phase 1-T: Topic Aggregate** (additive to Phase 1)
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

**Phase 2: Defect Classification**

Seven defect classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
```

Typing rules identical to V-01. For TIMELINE_ANOMALY, cite VAR_ID, TURN_ID, and
ANOMALY_TYPE from Phase 1-S. Note whether the anomaly was detected because a variable
lacked AUTHORIZED_REWRITERS coverage (OFF_CONTRACT_WRITE would have been permitted
had the Architect declared the re-writer).

**Phase 3: Defect Reproduction + Phase 3-E: ENTANGLEMENT_MAP**

Phase 3: minimal utterance sequence per FOUND defect + observable failure mode.
Phase 3-E: DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION.

**Phase 4: Fallback Chain + Escalation + Disambiguation**

Trace at least one fallback path to completion. Trace at least one escalation path in
full. For FOUND INTENT_COLLISION: disambiguation strategy with rationale.

**Phase 5: Coverage Metrics**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
TOPIC_COVERAGE:        reachable_visited / total_reachable            (from 0-A-2)
TRANSITION_COVERAGE:   transitions_exercised / total_declared         (from 0-A-3)
SLOT_PATH_COVERAGE:    slot_paths_exercised / total_declared          (from 0-A-4)
```

**Phase 6: Adversarial Turn Injection**

At least one adversarial scenario. Show Phase 1-S entries for adversarial turns.
Record TRANSITION_ID and SLOT_PATH_ID if applicable. Trace recovery.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-E

**Phase 6-A: Coverage Audit**
```
TIMELINE_ANOMALY_RATE_VERIFIED:   PASS | FAIL[discrepancy]
TOPIC_COVERAGE_VERIFIED:          PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED:     PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
CONTRACT_AUDIT_GATE_HONORED:      PASS | FAIL[Developer began Phase 1 without CONTRACT_AUDIT: PASS]
```

**Phase 6-B: Severity Co-Residency Audit**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS|FAIL
```

**Phase 6-C: Entanglement Consistency Audit**
```
DEFECT | ENTANGLEMENT_VERDICT | SUPPORTING_TURN | CONSISTENCY: PASS|FAIL[cite]
```

**Phase 6-D: Topic Aggregate Consistency Audit**
```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS|FAIL
TOPIC_ROLLUP_MISMATCH_COUNT: N
```
Mandatory gate for C-24.

**Phase 6-E: Session Timeline Consistency Audit**

Replay Phase 1-S mutations. Reconstruct SESSION_STATE per turn. Compare against Phase 1:
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```
Any TIMELINE_ANOMALY: YES not cited in Phase 2 is a Phase 6-E finding.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-05 — Axes B + Phrasing Register: Constraint-Satisfaction with Inertia Annotations (Combined)

**Hypothesis:** Expressing the simulation as a constraint set — where Phase 0-D declares
named conversation contracts (CONV-NN), Phase 1 carries inline CONSTRAINT_VERDICTS, and
each constraint carries a STATUS_QUO_DETECTABILITY annotation — embeds anomaly detection
logic structurally into the trace format. Inertia framing (V-02 axis) explains why each
constraint cannot be verified by informal review; constraint-satisfaction register makes
the explanation load-bearing rather than decorative. An Auditor verifying constraint
verdicts is verifying that the developer correctly evaluated each CONV-NN at each turn —
a machine-checkable property — rather than re-evaluating defects from scratch.

---

You are a Copilot Studio domain expert running a full conversation-flow simulation.
Your output is a constraint-verified trace: you declare conversation contracts first,
evaluate each contract at every turn, then audit your own evaluations.

Work in two stages: **Developer** then **Auditor**. The Auditor does not begin until
`[ROLE_COMPLETE: DEVELOPER]` is present.

---

### Developer

Before tracing a single turn, lock down two things: the topology and the constraint set.

**Step 1 — Declare your topics.**

List every topic in the bot. For each: TOPIC_ID, trigger phrases, slot-filling flag,
session variables written and read. Use only these terms throughout: *topic, trigger
phrase, condition, fallback topic, escalation, session variable, slot, entity,
adaptive card, Power Automate flow*. Write *intent*, *chatbot*, or *NLU model* and
you must stop and rewrite. Sign the gate: `VOCABULARY_GATE: SIGNED`.

**Step 2 — Map reachability and transitions.**

Pick the entry topic. Walk every edge. List reachable topics and orphaned topics
(orphans are already ORPHAN defects — log them now, before the trace). Number every
edge TRANS-01 onward: source, target, condition, REQUIRED or OPTIONAL. Unexercised
REQUIRED edges are orphaned-edge defects.

**Step 3 — Declare session variables and the timeline contract.**

For each variable: VAR_ID, type, initial value, persistence class. Then, for every
variable, declare the expected lifecycle:
```
VAR_ID | FIRST_WRITTEN_TOPIC | CLEARED_BY | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```
This contract is sealed here. You cannot amend it in Phase 6.

**Step 4 — Declare slot paths.**

For every slot-filling topic, declare the canonical fill path and any short-circuit
variants. Unexercised canonical paths are SLOT_GAP defects.

**Step 5 — Name your conversation constraints.** ← *constraint-satisfaction register, new in V-05*

Before tracing, declare the invariants the trace must satisfy as named constraints:
```
CONV-NN: <property that holds for all turns>
         STATUS_QUO_DETECTABILITY: DETECTABLE|NOT_DETECTABLE
         DETECTION_REASON: <why informal review would or would not catch a violation>
```

Required minimum constraints (you may add more):
- CONV-01: For all turns T, SESSION_STATE[T] equals the state computed by replaying
  Phase 1-S mutations through turn T.
  STATUS_QUO_DETECTABILITY: NOT_DETECTABLE (informal review sees state snapshots, not mutation sequences)
- CONV-02: For all FOUND defects D, SEVERITY_CLASS ∈ {P0,P1,P2,P3} and INVARIANT_CITE ≠ NULL coexist.
- CONV-03: For all CONFIRMED_ABSENT defects D, SEVERITY_CLASS = EXEMPT.
- CONV-04: No turn references a TOPIC_ID absent from the declared topic registry.
- CONV-05: No session variable read occurs after its CLEARED_BY event when READ_AFTER_CLEARED = FORBIDDEN.
  STATUS_QUO_DETECTABILITY: NOT_DETECTABLE (lifecycle violations require temporal ordering of mutations — invisible in flow diagrams or manual walkthroughs that examine single-turn state)
- CONV-06: Every DEVIATES turn cites a registered INVARIANT-ID.

Additional constraints for your specific topic graph are encouraged. Each must include
STATUS_QUO_DETECTABILITY with a one-sentence reason.

**Step 6 — Status-quo baseline.**

Declare what informal method the team currently uses:
```
STATUS_QUO_METHOD: <e.g., manual walkthrough, diagram review, developer testing>
```
You will use this in SIMULATION_DELTA in Step 13.

**Step 7 — Trace the conversation turn by turn.**

For each turn, fill in every column — no skipping:
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | INVARIANT_CONFORMANCE | CONFORMANCE
     | CONSTRAINT_VERDICTS: CONV-NN=PASS|FAIL[...], CONV-NN=PASS|FAIL[...]
```

`CONSTRAINT_VERDICTS`: evaluate every applicable CONV-NN at this turn. A FAIL cites
the constraint ID and the condition that falsified it. CONV-01 is applicable at every
turn with a non-null session variable. CONV-04 is applicable at every turn. Others
apply as their scope dictates.

**Step 8 — Add the session timeline.** (additive to Phase 7's turn table)

For every turn where a session variable is active:
```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONV_01_EVIDENCE: PRE+MUTATION=POST? PASS|FAIL
        | TIMELINE_ANOMALY: YES|NO | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

`CONV_01_EVIDENCE` shows the arithmetic: the mutation applied to PRE_VALUE should yield
POST_VALUE. This is the per-row evidence for CONV-01 in Step 7.

**Step 9 — Add the topic aggregate.** (additive to the turn table)

One row per topic visited:
```
TOPIC_ID | TURNS | VARS_SET | VARS_READ | DEFECT_CITATIONS
         | ADVERSARIAL_TURNS | CONFORMANCE_ROLLUP
```

**Step 10 — Classify every defect type.** Seven classes: DEAD_END, INFINITE_LOOP,
INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
             | CONV_VIOLATIONS: [CONV-NN, ...] | NONE
```

`CONV_VIOLATIONS`: list every CONV-NN whose verdict was FAIL in at least one turn row
where this defect class contributed to the failure.

Typing rules: CONFIRMED_ABSENT → SEVERITY_CLASS = EXEMPT + INVARIANT_CITE.
FOUND → SEVERITY_CLASS ∈ {P0,P1,P2,P3} + INVARIANT_CITE (both coexist).
RECOVERY: RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason].
MASKED_BY: RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS].

**Step 11 — Write reproduction steps.** For each FOUND defect: exact utterance
sequence that triggers it, observable failure mode, and which CONV-NN was violated.

**Step 12 — Map the entanglement.**
```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION: UPSTREAM|DOWNSTREAM
```

**Step 13 — Report coverage and simulation delta.**

```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
TOPIC_COVERAGE:        reachable_visited / total_reachable
TRANSITION_COVERAGE:   transitions_exercised / total_declared
SLOT_PATH_COVERAGE:    slot_paths_exercised / total_declared

CONSTRAINT_VIOLATION_SUMMARY:
  CONV-NN | VIOLATIONS: N | TURNS_AFFECTED: [T, ...]
```

**SIMULATION_DELTA**: for each FOUND defect whose CONV-NN has
STATUS_QUO_DETECTABILITY = NOT_DETECTABLE, emit:
```
DEFECT_CLASS | CONV_VIOLATED | WHY_NOT_DETECTABLE_BY_STATUS_QUO
```

If every FOUND defect is DETECTABLE by the declared STATUS_QUO_METHOD, write
`SIMULATION_DELTA: EMPTY — all findings within reach of status-quo method` and
justify each claim.

**Step 14 — Trace the fallback chain.** No-match → fallback topic → escalation or
graceful exit. Show every node and TRANSITION_ID. Trace escalation in full. For
FOUND INTENT_COLLISION: propose disambiguation strategy.

**Step 15 — Inject an adversarial turn.** Off-topic, ambiguous, or mid-slot-fill topic
switch. Show TRANSITION_ID, state delta, Phase 1-S entries, CONSTRAINT_VERDICTS for
adversarial turns. Trace recovery.

`[ROLE_COMPLETE: DEVELOPER]`

---

### Auditor

Four verification tasks. Do not revise Developer output — audit it.

**Audit 1 — Constraint verdict consistency.**

For each CONV-NN declared in Step 5, verify that FAIL verdicts in the turn table
are internally consistent with the constraint's falsification condition. A PASS verdict
at turn T for CONV-01 where Phase 1-S shows a discrepancy at turn T is a contradiction.
```
CONV-NN | TOTAL_TURNS_EVALUATED | FAIL_VERDICTS | CONSISTENCY: PASS|FAIL[cite turn]
```

**Audit 2 — Coverage audit.**
```
TIMELINE_ANOMALY_RATE_VERIFIED:   PASS | FAIL[discrepancy]
TOPIC_COVERAGE_VERIFIED:          PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED:     PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
SIMULATION_DELTA_COMPLETE:        PASS | FAIL[FOUND defect with NOT_DETECTABLE missing from delta]
```

**Audit 3 — Severity co-residency.**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CONV_VIOLATIONS_PRESENT
       | CO_RESIDENCY: PASS|FAIL
```
CONV_VIOLATIONS must be present for FOUND rows and absent or NONE for CONFIRMED_ABSENT rows.

**Audit 4 — Topic aggregate and timeline consistency.**

Topic aggregate (mandatory gate for C-24):
```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS|FAIL
TOPIC_ROLLUP_MISMATCH_COUNT: N
```

Session timeline consistency:
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```
Any TIMELINE_ANOMALY: YES in Phase 1-S not cited in a TIMELINE_ANOMALY defect row
is a finding here.

`[ROLE_COMPLETE: AUDITOR]`

---

*End of Round 10 variations.*
