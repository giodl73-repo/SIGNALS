# Quest Variations — flow-conversation — Round 11 (v10 rubric)

**Date:** 2026-03-15 | **Rubric version:** v10 | **Max score:** 156

---

## Variation Axes Selected

**Single-axis (3):**
- **Axis A — Lifecycle emphasis (P0 execution halt gate)**: Phase 2 P0 findings pause
  execution; the Developer must emit a MINIMUM_VIABLE_FIX block per P0 defect before
  proceeding to Phase 3. Phase 6 adds a FIX_VIABILITY_AUDIT.
- **Axis B — Output format (constraint chain propagation)**: Each CONV-NN in Phase 0-D-4
  declares a PROPAGATION list of downstream constraints that depend on its POST_VALUE.
  Phase 1 adds a CHAIN_EFFECTS column. Phase 6 adds a CHAIN_INTEGRITY_AUDIT.
- **Axis C — Inertia framing (pre-committed deviation budget)**: Developer declares a
  DEVIATION_BUDGET table in Phase 0-D before tracing. Phase 5 reports BUDGET_UTILIZATION.
  A BUDGET_EXCEEDED finding is emitted before coverage ratios.

**Combined (2):**
- **Axes A + B**: P0 execution halt gate combined with constraint chain proof. Each
  EXECUTION_HALT block extends to a CHAIN_BREAK_TRACE citing the causal upstream CONV-NN
  and the turn where the chain first diverged.
- **Axes B + C**: Constraint chain budget — DEVIATION_BUDGET declared at chain level
  (per CONV_CHAIN, not per severity). CHAIN_BUDGET_EXCEEDED becomes the 8th structural
  finding class.

---

## V-01 — Axis A: P0 Execution Halt Gate (Single-Axis)

**Hypothesis:** When Phase 2 finds a P0 defect, the artifact should pause and produce a
minimum viable fix recommendation before recording reproduction steps. Teams reading
flow-conversation artifacts need actionable remediation at the P0 tier, not a complete
defect catalog with fixes buried at the end. Forcing an EXECUTION_HALT block immediately
after each P0 classification changes the document contract: it is now an active
remediation prescription rather than a passive defect list. The Phase 6-F FIX_VIABILITY_AUDIT
closes the loop by verifying that each recommended fix would not introduce new CONV-NN
violations — surfacing fix side-effects before implementation begins.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

The Topology Architect produces the signed topology contract. All downstream roles
are bound to it; none may modify it.

**Phase 0-A-1: Topic Inventory**
```
TOPIC_ID | NAME | TRIGGER_PHRASES | ENTRY_CONDITION
         | EXIT_NODES | SLOT_FILLING: YES|NO
         | SESSION_VARS_WRITTEN | SESSION_VARS_READ
```
First encounter of an undeclared topic in any downstream phase is a CONTRACT_GAP finding.

**Phase 0-A-2: REACHABILITY_MAP**
```
ENTRY_TOPIC: TOPIC-NN
REACHABLE:   [TOPIC-NN, ...]
ORPHANED:    [TOPIC-NN, ...]
```
Orphaned topics are ORPHAN defects (fifth structural defect class).

**Phase 0-A-3: TRANSITION_MAP**
```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN
         | condition: <text> | REQUIRED|OPTIONAL
```
Unexercised REQUIRED edges are orphaned-edge defects with UNRECOVERABLE[missing edge].

**Phase 0-A-4: Vocabulary Gate**

Permitted: topic, trigger phrase, condition, fallback topic, escalation, session variable,
slot, entity, adaptive card, Power Automate flow, escalation node.
Prohibited: intent, utterance class, NLU model, chatbot, dialog node, bot flow.

`VOCABULARY_GATE: SIGNED`

**Phase 0-A-5: SLOT_PATH_MAP**

For every topic with SLOT_FILLING: YES:
```
SLOT_PATH-NN     | TOPIC_ID | SLOTS_REQUIRED | CANONICAL_TURNS: N
                 | path_type: CANONICAL
SLOT_PATH-NN-SC1 | TOPIC_ID | SLOTS_SKIPPED: [slot_1]
                 | path_type: SHORT_CIRCUIT | trigger_condition: <text>
```
Unexercised canonical SLOT_PATH-NN is a SLOT_GAP defect (sixth structural defect class).

**Phase 0-A-6: Session Variable Registry**
```
VAR_ID | TYPE | INITIAL_VALUE | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL
```
Variables appearing in Phase 1 SESSION_STATE must be registered here.

**Phase 0-A-7: Topology Invariants**
```
INVARIANT-TOPO-NN: <statement> | FALSIFICATION: <condition>
INVARIANT-SV-NN:   <statement> | FALSIFICATION: <condition>
CONV-NN:           <statement> | FALSIFICATION: <condition>
                   | MUTATION_SEMANTICS: ADDITIVE|BOOLEAN|STRING_APPEND|CONDITIONAL
                   | PROPAGATION: [CONV-NN, ...] (downstream constraints that depend on this constraint's POST_VALUE; empty list if terminal)
```
Every DEVIATES verdict and every Phase 2 defect must cite at least one registered ID.
Every CONV-NN in CONSTRAINT_VERDICTS (Phase 1) must appear here.

**Phase 0-A-8: SESSION_VARIABLE_TIMELINE_CONTRACT**
```
VAR_ID | FIRST_WRITTEN_TOPIC: TOPIC-NN
       | AUTHORIZED_REWRITERS: [TOPIC-NN, ...] (topics permitted to write beyond FIRST_WRITTEN_TOPIC)
       | CLEARED_BY: TOPIC-NN|NEVER
       | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```
All variables in Phase 0-A-6 must appear here. AUTHORIZED_REWRITERS must each appear in
Phase 0-A-1; a rewriter referencing an undeclared topic is a CONTRACT_GAP finding.
A write from a topic absent from both FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS
is an OFF_CONTRACT_WRITE anomaly. Contract sealed at Phase 0-A close.

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

The Contract Auditor's sole scope is SESSION_VARIABLE_TIMELINE_CONTRACT completeness
before trace execution begins. The Auditor does not modify the contract; it verifies it.

**Phase 0-CA-1: Contract Completeness Gate**

Compute VARS_IN_TOPOLOGY: union of all SESSION_VARS_WRITTEN and SESSION_VARS_READ across
all topics in Phase 0-A-1.

Compute VARS_IN_CONTRACT: all VAR_IDs in Phase 0-A-8.

```
VARS_IN_TOPOLOGY: [VAR_ID, ...]
VARS_IN_CONTRACT: [VAR_ID, ...]
COVERAGE_DELTA:   [VAR_IDs in TOPOLOGY but not CONTRACT] (empty = PASS)
CONTRACT_AUDIT: PASS | BLOCKED[COVERAGE_DELTA non-empty — CONTRACT_COMPLETENESS_FAILURE]
```

If CONTRACT_AUDIT: BLOCKED, the Developer's first output must be a CONTRACT_REMEDIATION
section addressing every VAR_ID in COVERAGE_DELTA. Developer may not proceed to Phase 1-S
until CONTRACT_AUDIT: PASS.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1 through 5

**Status-Quo Baseline**
```
STATUS_QUO_METHOD: <e.g., manual walkthrough, whiteboard diagram, developer test>
KNOWN_GAPS:        <what the team acknowledges it does not currently check>
```

---

**Phase 1-S: SESSION_TIMELINE** ← *author this before Phase 1*

**Authoring rule**: Populate Phase 1-S before filling the SESSION_STATE column in Phase 1.
SESSION_STATE in Phase 1 is derived by replaying Phase 1-S mutations in turn order through
the current TURN_ID. Do not independently author SESSION_STATE; reconstruct it from Phase 1-S.
Each SESSION_STATE cell must cite the Phase 1-S entry from which it was reconstructed.

For every turn in which any session variable is active, mutated, or cleared:
```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONTRACT_MATCH: CONFORMS|VIOLATES[reason]
        | TIMELINE_ANOMALY: YES|NO
        | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

TIMELINE_ANOMALY: YES when:
- READ after CLEARED_BY has fired and READ_AFTER_CLEARED = FORBIDDEN → READ_AFTER_CLEAR
- WRITE from a topic absent from FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS → OFF_CONTRACT_WRITE
- READ where most recent prior mutation was CLEAR with no intervening WRITE → STALE_READ

Each TIMELINE_ANOMALY: YES row generates a TIMELINE_ANOMALY defect entry in Phase 2.

---

**Phase 1: Turn-by-Turn Trace**

For each turn:
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | CONFORMANCE | CONSTRAINT_VERDICTS
```

- `SESSION_STATE`: derived from Phase 1-S replay through this TURN_ID. Cite the Phase 1-S
  entry: e.g., `{var: "X", from: Phase1S-T3-VAR_X}`.
- `SLOT_PATH_ID`: cite SLOT_PATH-NN from Phase 0-A-5; N/A outside slot-fill sequences.
- `TRANSITION_ID`: cite TRANS-NN from Phase 0-A-3.
- `CONFORMANCE`: CONFORMS | DEVIATES[INVARIANT-ID]
- `CONSTRAINT_VERDICTS`: comma-separated list of `CONV-NN: CONFORMS|DEVIATES` evaluated
  against this turn. Every CONV-NN cited must appear in Phase 0-A-7. A CONV-NN referencing
  an unregistered invariant is a CONTRACT_GAP finding. A DEVIATES[CONV-NN] in
  CONSTRAINT_VERDICTS that contradicts CONFORMS in CONFORMANCE is a VERDICT_MISMATCH
  finding for the Auditor.

For CONV-NN invariants with MUTATION_SEMANTICS ≠ CONDITIONAL, include arithmetic evidence
inline in CONSTRAINT_VERDICTS:
```
CONV-NN: CONFORMS [PRE=<v>, MUTATION=<op>, POST=<v>, CHECK: PRE+MUTATION=POST]
CONV-NN: DEVIATES [PRE=<v>, MUTATION=<op>, POST=<v>, CHECK: PRE+MUTATION≠POST — violation]
```
For CONDITIONAL semantics: `CONV-NN: CONFORMS [BRANCH: <condition>, PATH: <taken>]`

No turns may be skipped. No topics may be referenced absent from Phase 0-A-1.

**Phase 1-T: Topic Aggregate** (additive to Phase 1, not replacing it)

One row per topic visited:
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```
CONFORMANCE_ROLLUP must match the DEVIATES count for this topic in Phase 1.
A CONFORMS rollup for a topic with at least one DEVIATES turn is a TOPIC_ROLLUP_MISMATCH.

---

**Phase 2: Defect Classification**

Classify all seven defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE (if FOUND; for TIMELINE_ANOMALY cite VAR_ID and TURN_ID from Phase 1-S)
             | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
             | STATUS_QUO_GAP: <what STATUS_QUO_METHOD would miss>
```

Typing rules:
- CONFIRMED_ABSENT: `SEVERITY_CLASS = EXEMPT`. INVARIANT_CITE required.
- FOUND: `SEVERITY_CLASS` ∈ {P0, P1, P2, P3}. INVARIANT_CITE required. Both columns must coexist.
- RECOVERY for FOUND: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` | `UNRECOVERABLE[reason]`
- MASKED_BY: `RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`
- ENTANGLEMENT_VERDICT: `ISOLATED` | `ENABLES[DEFECT_CLASS]` | `MASKED_BY[DEFECT_CLASS]`

Severity: P0 (session corruption/unescapable loop), P1 (dead end, no fallback),
P2 (suboptimal, recoverable ≤ 3 turns), P3 (cosmetic).

**P0 EXECUTION HALT GATE** ← *new in V-01*

After classifying each FOUND defect, before proceeding to the next defect class:

If `SEVERITY_CLASS = P0`, emit an EXECUTION_HALT block immediately:
```
EXECUTION_HALT
  HALT_TRIGGER:       <DEFECT_CLASS> at <TOPIC_ID|TURN_ID>
  ROOT_CAUSE:         <one-sentence causal statement>
  MVF_RECOMMENDATION: <minimum viable fix — the smallest change that eliminates the P0 condition>
  MVF_SCOPE:          <which topics/transitions/session variables the fix touches>
  UNBLOCKED_BY:       <the observable state change that confirms the fix was applied>
```

The Developer emits one EXECUTION_HALT block per P0 defect found, in the order the P0
defects are classified. Classification of lower-severity defects continues after all P0
EXECUTION_HALT blocks are emitted. This is a documentation ordering requirement, not a
trace-execution stop.

---

**Phase 3: Defect Reproduction**

For each FOUND defect: minimal utterance sequence that triggers it + observable failure mode.

**Phase 3-E: ENTANGLEMENT_MAP**
```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION: UPSTREAM|DOWNSTREAM
```
A MASKED_BY or ENABLES claim without supporting Phase 1 turn evidence is invalid.

---

**Phase 4: Fallback Chain + Escalation + Disambiguation**

Trace at least one fallback path to completion: no topic match → fallback topic →
escalation or graceful exit. Show every node. Record TRANSITION_IDs.

Trace at least one escalation path: trigger condition, handoff node name, SESSION_STATE
at handoff, agent receipt confirmation. Escalation is CONFIRMED_ABSENT only if no
escalation topic was declared in Phase 0-A-1.

If INTENT_COLLISION was FOUND in Phase 2, propose a disambiguation strategy (entity
enrichment, condition ordering, trigger phrase refactor) with rationale.

---

**Phase 5: Coverage Metrics + Simulation Delta**

**5-A: Temporal Quality Gate**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events  (from Phase 1-S)
COVERAGE_QUALITY_GATE: CLEAN (anomalies_found = 0) | DEGRADED (anomalies_found > 0)
```
If DEGRADED: all ratios in 5-B carry PROVISIONAL designation. Emit DEGRADED_COVERAGE_NOTE
citing anomaly types, affected topics, and affected transitions.

**5-B: Coverage Ratios**
```
STATUS: CONFIRMED (CLEAN) | PROVISIONAL (DEGRADED)
TOPIC_COVERAGE:      reachable_visited / total_reachable       (from Phase 0-A-2)
TRANSITION_COVERAGE: transitions_exercised / total_declared     (from Phase 0-A-3)
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared      (from Phase 0-A-5)
```
ORPHAN topics included in TOPIC_COVERAGE denominator.

**5-C: SIMULATION_DELTA**

For each FOUND defect from Phase 2:
```
DEFECT_CLASS | DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH
             | STATUS_QUO_GAP_SUMMARY: <why STATUS_QUO_METHOD would miss or catch this>
```
Every Phase 2 FOUND defect must appear in exactly one category. Uncategorized defects
are a SIMULATION_DELTA audit finding.

**Phase 6: Adversarial Turn Injection**

Inject at least one adversarial utterance mid-conversation (off-topic, ambiguous, or
contradictory). Record: TURN_ID, topic match or miss, TRANSITION_ID, SLOT_PATH_ID if a
slot-fill was interrupted. Emit Phase 1-S entries for adversarial turns. Trace recovery
to completion. Include CONSTRAINT_VERDICTS for adversarial turns with arithmetic evidence
where applicable.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-F

The Auditor operates on completed Developer output. It does not revise; it audits.
Auditor findings may not retroactively alter Developer rows.

**Phase 6-A: Coverage Audit + Gate Verification**
```
CONTRACT_AUDIT_GATE_HONORED: PASS | FAIL[Phase 0-CA-1 delta was non-empty or Developer bypassed gate]
QUALITY_GATE_VERIFIED:            PASS | FAIL[anomaly count mismatch vs Phase 1-S]
COVERAGE_STATUS_APPROPRIATE:      PASS | FAIL[PROVISIONAL missing when DEGRADED, or vice versa]
TOPIC_COVERAGE_VERIFIED:          PASS | FAIL[discrepancy — cite denominator source]
TRANSITION_COVERAGE_VERIFIED:     PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
SIMULATION_DELTA_COMPLETE:        PASS | FAIL[uncategorized defect class]
```
CONTRACT_AUDIT_GATE_HONORED: PASS requires Phase 0-CA-1 delta to have been empty before
Phase 1-S began. This must be the final entry in Phase 6-A.

**Phase 6-B: Severity Co-Residency Audit**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS|FAIL
```
Every FOUND row: both columns populated. Every CONFIRMED_ABSENT row: EXEMPT. Structured
table required; prose note does not satisfy.

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

Replay Phase 1-S mutations in turn sequence. Reconstruct SESSION_STATE per turn.
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```
Under mutation-first authoring, CONSISTENT: FAIL is a structural authoring error, not a
discrepancy between two independently-authored tables. Any Phase 1-S TIMELINE_ANOMALY: YES
row not cited in a Phase 2 TIMELINE_ANOMALY defect is a Phase 6-E finding.

**Phase 6-F: Fix Viability Audit** ← *new in V-01*

For each EXECUTION_HALT block emitted in Phase 2, verify:
```
HALT_TRIGGER | MVF_RECOMMENDATION | CONV_VIOLATIONS_INTRODUCED: YES|NO
             | CONV_VIOLATIONS_DETAIL: [CONV-NN affected by fix]
             | VIABILITY: VIABLE | SIDE_EFFECTS_FOUND[CONV-NN list]
```
A VIABLE verdict requires: (a) the fix addresses HALT_TRIGGER, and (b) CONV_VIOLATIONS_INTRODUCED: NO.
If the fix introduces new CONV-NN violations (e.g., changes a session variable in a way
that breaks a downstream constraint), emit SIDE_EFFECTS_FOUND with the affected CONV-NN list.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-02 — Axis B: Constraint Chain Propagation (Single-Axis)

**Hypothesis:** Per-turn CONV-NN verdicts (C-36) are binary and turn-local. When a
session variable mutation satisfies CONV-01 at turn 3, and CONV-05 at turn 7 depends on
the same variable's value, the connection between these constraints is invisible unless
explicitly declared. Chaining constraints across turns — each CONV-NN declares which
downstream constraints depend on its POST_VALUE — transforms per-turn binary verdicts into
a compositional proof system. A chain failure surfaces the causal root at the upstream
constraint rather than at the symptom turn. The Phase 6-F CHAIN_INTEGRITY_AUDIT verifies
that every declared propagation edge fired when its upstream constraint held, and did not
fire when its upstream constraint failed.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

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

**Phase 0-A-3: TRANSITION_MAP**
```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN
         | condition: <text> | REQUIRED|OPTIONAL
```

**Phase 0-A-4: Vocabulary Gate**

Permitted: topic, trigger phrase, condition, fallback topic, escalation, session variable,
slot, entity, adaptive card, Power Automate flow, escalation node.
Prohibited: intent, utterance class, NLU model, chatbot, dialog node, bot flow.

`VOCABULARY_GATE: SIGNED`

**Phase 0-A-5: SLOT_PATH_MAP**
```
SLOT_PATH-NN     | TOPIC_ID | SLOTS_REQUIRED | CANONICAL_TURNS: N | path_type: CANONICAL
SLOT_PATH-NN-SC1 | TOPIC_ID | SLOTS_SKIPPED: [slot_1] | path_type: SHORT_CIRCUIT | trigger_condition: <text>
```

**Phase 0-A-6: Session Variable Registry**
```
VAR_ID | TYPE | INITIAL_VALUE | PERSISTENCE_CLASS: SESSION|TOPIC_SCOPED|GLOBAL
```

**Phase 0-A-7: Topology Invariants + Constraint Chain Declaration** ← *new in V-02*
```
INVARIANT-TOPO-NN: <statement> | FALSIFICATION: <condition>
INVARIANT-SV-NN:   <statement> | FALSIFICATION: <condition>
CONV-NN:           <statement> | FALSIFICATION: <condition>
                   | MUTATION_SEMANTICS: ADDITIVE|BOOLEAN|STRING_APPEND|CONDITIONAL
                   | PROPAGATION: [CONV-NN, ...] — downstream constraints whose evaluation
                     depends on this constraint's POST_VALUE being CONFORMS.
                   | CHAIN_ID: CHAIN-NN (assign every CONV-NN to exactly one chain;
                     terminal constraints have PROPAGATION: [] but still carry CHAIN_ID)
```

**Constraint chain rules:**
- Every CONV-NN belongs to exactly one CHAIN-NN.
- A chain is a directed acyclic sequence of CONV-NN nodes connected by PROPAGATION edges.
- The first CONV-NN in a chain (no inbound PROPAGATION) is the chain head.
- A chain is BROKEN if the chain head DEVIATES; subsequent nodes in a broken chain are
  CHAIN_SUSPENDED (their verdicts cannot be trusted because the upstream precondition failed).
- CHAIN_SUSPENDED is not a DEVIATES verdict; it is a suspended evaluation.

**Phase 0-A-8: SESSION_VARIABLE_TIMELINE_CONTRACT**
```
VAR_ID | FIRST_WRITTEN_TOPIC: TOPIC-NN
       | AUTHORIZED_REWRITERS: [TOPIC-NN, ...]
       | CLEARED_BY: TOPIC-NN|NEVER
       | READ_AFTER_CLEARED: FORBIDDEN|ALLOWED
```

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

**Phase 0-CA-1: Contract Completeness Gate**
```
VARS_IN_TOPOLOGY: [VAR_ID, ...]
VARS_IN_CONTRACT: [VAR_ID, ...]
COVERAGE_DELTA:   [missing VAR_IDs]
CONTRACT_AUDIT: PASS | BLOCKED[COVERAGE_DELTA non-empty]
```

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1 through 5

**Status-Quo Baseline**
```
STATUS_QUO_METHOD: <current review method>
KNOWN_GAPS:        <what the team acknowledges it does not check>
```

---

**Phase 1-S: SESSION_TIMELINE** ← *author this before Phase 1*

**Authoring rule**: Phase 1-S before Phase 1 SESSION_STATE. SESSION_STATE derived from
Phase 1-S replay; each cell cites its Phase 1-S source entry.

```
TURN_ID | VAR_ID | MUTATION: WRITE|READ|CLEAR|NO_CHANGE
        | PRE_VALUE | POST_VALUE | TOPIC_ID
        | CONTRACT_MATCH: CONFORMS|VIOLATES[reason]
        | TIMELINE_ANOMALY: YES|NO | ANOMALY_TYPE: READ_AFTER_CLEAR|OFF_CONTRACT_WRITE|STALE_READ|NONE
```

---

**Phase 1: Turn-by-Turn Trace**

```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | CONFORMANCE | CONSTRAINT_VERDICTS | CHAIN_EFFECTS
```

- `CONFORMANCE`: CONFORMS | DEVIATES[INVARIANT-ID]
- `CONSTRAINT_VERDICTS`: for each CONV-NN evaluated this turn:
  - For MUTATION_SEMANTICS ≠ CONDITIONAL:
    `CONV-NN: CONFORMS [PRE=<v>, MUTATION=<op>, POST=<v>, CHECK: PRE+MUTATION=POST]`
    `CONV-NN: DEVIATES [PRE=<v>, MUTATION=<op>, POST=<v>, CHECK: PRE+MUTATION≠POST — violation]`
  - For CONDITIONAL: `CONV-NN: CONFORMS [BRANCH: <cond>, PATH: <taken>]`
  - If upstream chain head DEVIATES in this or a prior turn and POST_VALUE not restored:
    `CONV-NN: CHAIN_SUSPENDED [chain head: CONV-NN broke at TURN_ID]`
- `CHAIN_EFFECTS` ← *new in V-02*: for each CONV-NN evaluated this turn, list downstream
  propagation effects:
  ```
  CHAIN_EFFECTS: CONV-NN → [CONV-NN-downstream-1: ACTIVATED|SUSPENDED, ...]
  ```
  ACTIVATED: upstream CONFORMS, downstream evaluation is enabled for subsequent turns.
  SUSPENDED: upstream DEVIATES, downstream evaluation is suspended until upstream recovers.

**Phase 1-T: Topic Aggregate** (additive to Phase 1)
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

---

**Phase 2: Defect Classification**

Classify all seven defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
             | STATUS_QUO_GAP: <what STATUS_QUO_METHOD would miss>
```

Typing rules:
- CONFIRMED_ABSENT: SEVERITY_CLASS = EXEMPT. INVARIANT_CITE required.
- FOUND: SEVERITY_CLASS ∈ {P0, P1, P2, P3}. INVARIANT_CITE required.
- RECOVERY: RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]
- MASKED_BY: RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]
- ENTANGLEMENT_VERDICT: ISOLATED | ENABLES[DEFECT_CLASS] | MASKED_BY[DEFECT_CLASS]

---

**Phase 3: Defect Reproduction + Phase 3-E: ENTANGLEMENT_MAP**

Phase 3: minimal utterance sequence + observable failure mode per FOUND defect.

Phase 3-E:
```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | CAUSAL_DIRECTION: UPSTREAM|DOWNSTREAM
```

---

**Phase 4: Fallback Chain + Escalation + Disambiguation**

Trace at least one fallback path to completion. Trace at least one escalation path.
For FOUND INTENT_COLLISION: propose disambiguation strategy with rationale.

---

**Phase 5: Coverage Metrics + Simulation Delta**

**5-A: Temporal Quality Gate**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
COVERAGE_QUALITY_GATE: CLEAN | DEGRADED
```
If DEGRADED: emit DEGRADED_COVERAGE_NOTE and mark 5-B ratios PROVISIONAL.

**5-A-2: Constraint Chain Status Summary** ← *new in V-02*
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```
A chain is BROKEN if its head DEVIATES on any turn and never recovers before the trace ends.
A chain is INTACT if its head CONFORMS on all turns, or recovers before the trace ends.

**5-B: Coverage Ratios**
```
STATUS: CONFIRMED | PROVISIONAL
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared
```

**5-C: SIMULATION_DELTA**
```
DEFECT_CLASS | DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH
             | STATUS_QUO_GAP_SUMMARY
```

**Phase 6: Adversarial Turn Injection**

Inject at least one adversarial turn. Include CHAIN_EFFECTS for adversarial turns.
Trace recovery. Record Phase 1-S entries.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-F

**Phase 6-A: Coverage Audit + Gate Verification**
```
CONTRACT_AUDIT_GATE_HONORED:  PASS | FAIL[developer bypassed gate]
QUALITY_GATE_VERIFIED:        PASS | FAIL[anomaly count mismatch]
COVERAGE_STATUS_APPROPRIATE:  PASS | FAIL
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:  PASS | FAIL[discrepancy]
SIMULATION_DELTA_COMPLETE:    PASS | FAIL[uncategorized defect]
```
CONTRACT_AUDIT_GATE_HONORED must be the final entry.

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

**Phase 6-E: Session Timeline Consistency Audit**
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```

**Phase 6-F: Chain Integrity Audit** ← *new in V-02*

For each CHAIN-NN declared in Phase 0-A-7:
```
CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL[cite]
```
Verify:
1. Every ACTIVATED propagation edge in Phase 1 CHAIN_EFFECTS corresponds to an upstream
   CONV-NN: CONFORMS verdict in the same or prior turn.
2. Every SUSPENDED propagation edge corresponds to an upstream CONV-NN: DEVIATES or
   CHAIN_SUSPENDED verdict.
3. No downstream CONV-NN carries a CONFORMS verdict during a SUSPENDED chain window.
   A downstream CONFORMS during a SUSPENDED window is a CHAIN_VERDICT_INCONSISTENCY finding.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-03 — Axis C: Pre-committed Deviation Budget (Single-Axis)

**Hypothesis:** Declaring a DEVIATION_BUDGET before tracing begins makes the quality bar
explicit and verifiable — the same way test coverage thresholds are declared before
tests run. Teams that commit to "zero P0 defects" in the artifact's Phase 0 pre-execution
contract are held to that commitment in Phase 5 via BUDGET_UTILIZATION. A BUDGET_EXCEEDED
finding is emitted as a gate before coverage ratios are reported, giving it the same
prominence as TIMELINE_ANOMALY_RATE. The Auditor verifies BUDGET_UTILIZATION accuracy
in Phase 6-A. This axis targets inertia framing: when a team reviewing the artifact sees
that the budget was exceeded, the artifact self-justifies its existence — the team's own
pre-committed bar was not met.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

**Phase 0-A-1 through Phase 0-A-8**: identical to V-01 Phase 0-A-1 through Phase 0-A-8.

*(Produce: topic inventory, reachability map, transition map, vocabulary gate, slot path
map, session variable registry, topology invariants with CONV-NN/PROPAGATION, and session
variable timeline contract with AUTHORIZED_REWRITERS. CONV-NN invariants carry
MUTATION_SEMANTICS. Contract sealed at Phase 0-A close.)*

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

*(Identical to V-01 Phase 0-CA-1. Produce VARS_IN_TOPOLOGY vs VARS_IN_CONTRACT delta.
CONTRACT_AUDIT: PASS required before Developer begins.)*

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1 through 5

**Status-Quo Baseline**
```
STATUS_QUO_METHOD: <current review method>
KNOWN_GAPS:        <what the team does not currently check>
```

**DEVIATION_BUDGET Declaration** ← *new in V-03*

Declare maximum acceptable DEVIATES-turn counts before Phase 1-S begins. These are
pre-execution commitments; they may not be revised after Phase 1 is authored.
```
DEVIATION_BUDGET
  P0_MAX: <integer, typically 0>
  P1_MAX: <integer>
  P2_MAX: <integer>
  P3_MAX: <integer>
  BUDGET_RATIONALE: <why these thresholds are appropriate for this flow>
```
P0_MAX = 0 means any P0 defect is a BUDGET_EXCEEDED finding.

---

**Phase 1-S: SESSION_TIMELINE** ← *author before Phase 1*

*(Identical structure to V-01 Phase 1-S. Mutation-first authoring. SESSION_STATE derived
from Phase 1-S replay. Each SESSION_STATE cell cites its Phase 1-S source entry.)*

---

**Phase 1: Turn-by-Turn Trace**
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | CONFORMANCE | CONSTRAINT_VERDICTS
```

`CONFORMANCE`: CONFORMS | DEVIATES[INVARIANT-ID]

`CONSTRAINT_VERDICTS`: comma-separated CONV-NN evaluations for this turn.
- For MUTATION_SEMANTICS ≠ CONDITIONAL: include `[PRE=<v>, MUTATION=<op>, POST=<v>, CHECK: PRE+MUTATION=POST]`
- For CONDITIONAL: include `[BRANCH: <cond>, PATH: <taken>]`

**Phase 1-T: Topic Aggregate** (additive)
```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

---

**Phase 2: Defect Classification**

Classify all seven defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
             | STATUS_QUO_GAP
```

Typing rules as in V-01.

---

**Phase 3: Defect Reproduction + Phase 3-E: ENTANGLEMENT_MAP**

*(Same structure as V-01.)*

---

**Phase 4: Fallback Chain + Escalation + Disambiguation**

*(Same structure as V-01.)*

---

**Phase 5: Coverage Metrics + Budget Utilization + Simulation Delta**

**5-A: DEVIATION_BUDGET Utilization** ← *new in V-03, placed before quality gate*

Count actual DEVIATES turns per severity class from Phase 2 FOUND defects:
```
DEVIATION_BUDGET_UTILIZATION
  SEVERITY | BUDGET | ACTUAL_DEVIATES | STATUS: WITHIN_BUDGET | EXCEEDED
  P0       | <P0_MAX> | <count>       | WITHIN_BUDGET | EXCEEDED
  P1       | <P1_MAX> | <count>       | WITHIN_BUDGET | EXCEEDED
  P2       | <P2_MAX> | <count>       | WITHIN_BUDGET | EXCEEDED
  P3       | <P3_MAX> | <count>       | WITHIN_BUDGET | EXCEEDED
  OVERALL_BUDGET_STATUS: WITHIN_BUDGET | EXCEEDED[P0, P1, ...]
```

If OVERALL_BUDGET_STATUS: EXCEEDED, emit a BUDGET_EXCEEDED finding before 5-B:
```
BUDGET_EXCEEDED_FINDING
  VIOLATED_CLASSES: [P0, ...]
  OVER_BY:          P0: <actual - max>, ...
  IMPLICATION:      <one sentence on what this means for flow readiness>
```

**5-B: Temporal Quality Gate**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
COVERAGE_QUALITY_GATE: CLEAN | DEGRADED
```
If DEGRADED: all 5-C ratios carry PROVISIONAL designation.

**5-C: Coverage Ratios**
```
STATUS: CONFIRMED | PROVISIONAL
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared
```

**5-D: SIMULATION_DELTA**
```
DEFECT_CLASS | DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH | STATUS_QUO_GAP_SUMMARY
```

**Phase 6: Adversarial Turn Injection**

*(Same structure as V-01. Include CONSTRAINT_VERDICTS with arithmetic evidence.)*

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-F

**Phase 6-A: Coverage Audit + Gate Verification**
```
CONTRACT_AUDIT_GATE_HONORED:  PASS | FAIL
BUDGET_UTILIZATION_VERIFIED:  PASS | FAIL[actual DEVIATES count mismatch vs Phase 2 FOUND defects]
  P0_VERIFIED: <budget> vs <audited actual>
  P1_VERIFIED: <budget> vs <audited actual>
  P2_VERIFIED: <budget> vs <audited actual>
  P3_VERIFIED: <budget> vs <audited actual>
BUDGET_STATUS_CONSISTENT:     PASS | FAIL[EXCEEDED claimed but actual within budget, or vice versa]
QUALITY_GATE_VERIFIED:        PASS | FAIL[anomaly count mismatch]
COVERAGE_STATUS_APPROPRIATE:  PASS | FAIL
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:  PASS | FAIL[discrepancy]
SIMULATION_DELTA_COMPLETE:    PASS | FAIL[uncategorized defect]
```
CONTRACT_AUDIT_GATE_HONORED must be the final entry.

**Phase 6-B through 6-E**: identical to V-01 Phases 6-B through 6-E.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-04 — Axes A + B: P0 Halt Gate + Constraint Chain Proof (Combined)

**Hypothesis:** A P0 defect is most actionable when its causal path through the constraint
graph is visible. Knowing that a P0 DEAD_END exists is useful; knowing which CONV_CHAIN
was BROKEN before the dead end materialized — and at which turn the chain first diverged —
is prescriptive. Combining the P0 EXECUTION_HALT gate (Axis A) with constraint chain
propagation (Axis B) forces each EXECUTION_HALT block to include a CHAIN_BREAK_TRACE:
the causal upstream CONV-NN, the turn where the chain head first DEVIATES, and which
downstream constraints were CHAIN_SUSPENDED as a consequence. The MVF_RECOMMENDATION
must also specify a CHAIN_REPAIR: which constraints need re-evaluation after the fix.
This turns a defect halt into a complete causal remediation prescription.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

**Phase 0-A-1 through Phase 0-A-8**: Produce all artifacts as in V-02.

Key requirement: every CONV-NN in Phase 0-A-7 carries CHAIN_ID, PROPAGATION list, and
MUTATION_SEMANTICS. PROPAGATION edges are the causal graph used by EXECUTION_HALT
CHAIN_BREAK_TRACE in Phase 2.

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

*(Identical to V-01/V-02. CONTRACT_AUDIT: PASS required before Developer begins.)*

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1 through 5

**Status-Quo Baseline**
```
STATUS_QUO_METHOD: <current review method>
KNOWN_GAPS:        <what the team does not currently check>
```

---

**Phase 1-S: SESSION_TIMELINE** ← *author before Phase 1*

*(Mutation-first. SESSION_STATE derived from replay. Each cell cites its Phase 1-S source.)*

---

**Phase 1: Turn-by-Turn Trace**
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | CONFORMANCE | CONSTRAINT_VERDICTS | CHAIN_EFFECTS
```

`CONSTRAINT_VERDICTS` with arithmetic evidence (CONV-NN: CONFORMS/DEVIATES/CHAIN_SUSPENDED
+ PRE/MUTATION/POST/CHECK for non-CONDITIONAL semantics).

`CHAIN_EFFECTS`: for each CONV-NN evaluated, list downstream ACTIVATED or SUSPENDED effects.

**Phase 1-T**: additive topic aggregate as in prior variations.

---

**Phase 2: Defect Classification + P0 Execution Halt Gate with Chain Break Trace**

Classify all seven defect classes with full columns (INVARIANT_CITE, SEVERITY_CLASS,
RECOVERY, ENTANGLEMENT_VERDICT, STATUS_QUO_GAP).

**P0 EXECUTION HALT GATE with CHAIN_BREAK_TRACE** ← *combined axis A + B*

After classifying each FOUND P0 defect, immediately emit:
```
EXECUTION_HALT
  HALT_TRIGGER:       <DEFECT_CLASS> at <TOPIC_ID|TURN_ID>
  ROOT_CAUSE:         <one-sentence causal statement>
  CHAIN_BREAK_TRACE:
    BROKEN_CHAIN:     CHAIN-NN
    CHAIN_HEAD_CONV:  CONV-NN
    FIRST_DEVIATE_TURN: TURN_ID (earliest turn where chain head DEVIATES)
    SUSPENDED_CONVS:  [CONV-NN, ...] (downstream constraints suspended by the break)
    BREAK_TO_DEFECT_PATH: <narrative: how the chain break caused or enabled the P0 defect>
  MVF_RECOMMENDATION: <minimum viable fix>
  MVF_SCOPE:          <which topics/transitions/session variables the fix touches>
  CHAIN_REPAIR:       [CONV-NN, ...] (constraints that must be re-evaluated after fix —
                       typically: chain head + all SUSPENDED_CONVS in BROKEN_CHAIN)
  UNBLOCKED_BY:       <observable state change confirming fix was applied>
```

One EXECUTION_HALT block per P0 defect, in classification order.

---

**Phase 3: Defect Reproduction + Phase 3-E: ENTANGLEMENT_MAP**

*(Same as V-01.)*

---

**Phase 4: Fallback Chain + Escalation + Disambiguation**

*(Same as V-01. Show CHAIN_EFFECTS for fallback path turns.)*

---

**Phase 5: Coverage Metrics + Simulation Delta**

**5-A: Temporal Quality Gate**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
COVERAGE_QUALITY_GATE: CLEAN | DEGRADED
```

**5-A-2: Constraint Chain Status Summary**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```
Any BROKEN chain that corresponds to a P0 HALT_TRIGGER must be listed here with a cross-
reference to the EXECUTION_HALT block.

**5-B: Coverage Ratios**
```
STATUS: CONFIRMED | PROVISIONAL
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared
```

**5-C: SIMULATION_DELTA**
```
DEFECT_CLASS | DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH | STATUS_QUO_GAP_SUMMARY
```

**Phase 6: Adversarial Turn Injection**

*(Include CHAIN_EFFECTS. Emit Phase 1-S entries for adversarial turns.)*

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-G

**Phase 6-A through 6-E**: as in V-01.

**Phase 6-F: Fix Viability Audit** ← *from Axis A*
```
HALT_TRIGGER | MVF_RECOMMENDATION | CONV_VIOLATIONS_INTRODUCED: YES|NO
             | CHAIN_REPAIR_COMPLETE: YES|NO (all SUSPENDED_CONVS listed in CHAIN_REPAIR)
             | VIABILITY: VIABLE | SIDE_EFFECTS_FOUND[CONV-NN list]
```
CHAIN_REPAIR_COMPLETE: YES requires every CONV-NN in the CHAIN_REPAIR list to be present
in the MVF_SCOPE or CHAIN_REPAIR field.

**Phase 6-G: Chain Integrity Audit** ← *from Axis B*
```
CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL[cite]
```
Verify ACTIVATED/SUSPENDED CHAIN_EFFECTS against upstream CONV-NN verdicts. Flag any
downstream CONFORMS during a SUSPENDED window as CHAIN_VERDICT_INCONSISTENCY.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-05 — Axes B + C: Constraint Chain Budget (Combined)

**Hypothesis:** A per-severity DEVIATION_BUDGET (Axis C) pools all defects of a severity
tier, making it possible to "spend" the budget on any defect class. A per-chain budget
is more semantically precise: the team commits to a max failure count for each named
constraint chain, not for an anonymous tier. CONV-CHAIN-01 (balance invariant) may have
budget 0; CONV-CHAIN-02 (greeting acknowledgment) may have budget 2. A CHAIN_BUDGET_EXCEEDED
finding names the chain that violated its threshold, not just a severity class. This
makes the deviation budget domain-meaningful rather than generic. CHAIN_BUDGET_EXCEEDED
is introduced as the eighth structural finding class alongside the existing seven defect
classes. The Phase 6-F CHAIN_BUDGET_AUDIT closes the loop.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic graph.
Four roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **CONTRACT AUDITOR** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's section is complete and carries its
`[ROLE_COMPLETE: <ROLE>]` marker.

---

### TOPOLOGY ARCHITECT — Phase 0-A

**Phase 0-A-1 through Phase 0-A-8**: Produce all artifacts as in V-02 (topic inventory,
reachability map, transition map, vocabulary gate, slot path map, session variable registry,
topology invariants with CONV-NN/PROPAGATION/CHAIN_ID/MUTATION_SEMANTICS, timeline contract
with AUTHORIZED_REWRITERS).

**Phase 0-A-9: CONV_CHAIN_BUDGET Declaration** ← *new in V-05*

For every CHAIN-NN declared in Phase 0-A-7:
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH
         | CHAIN_BUDGET: <max acceptable DEVIATES turns for the chain head across all turns>
         | BUDGET_RATIONALE: <why this threshold is appropriate for this chain's domain semantics>
```
CHAIN_BUDGET = 0 means any DEVIATES on the chain head is a CHAIN_BUDGET_EXCEEDED finding.
CHAIN_BUDGET applies only to the chain head (CONV-NN with no inbound PROPAGATION);
suspended downstream constraints are not counted against the budget.

`[ROLE_COMPLETE: TOPOLOGY ARCHITECT]`

---

### CONTRACT AUDITOR — Phase 0-CA-1

**Phase 0-CA-1: Contract Completeness Gate + Chain Budget Registration Check** ← *extended in V-05*

```
VARS_IN_TOPOLOGY: [VAR_ID, ...]
VARS_IN_CONTRACT: [VAR_ID, ...]
COVERAGE_DELTA:   [missing VAR_IDs]
CHAINS_IN_TOPOLOGY:  [CHAIN-NN, ...] (all CHAIN_IDs assigned in Phase 0-A-7)
CHAINS_IN_BUDGET:    [CHAIN-NN, ...] (all CHAIN_IDs with budget entries in Phase 0-A-9)
CHAIN_BUDGET_DELTA:  [CHAIN_IDs in TOPOLOGY but not BUDGET] (empty = PASS)
CONTRACT_AUDIT: PASS | BLOCKED[COVERAGE_DELTA non-empty | CHAIN_BUDGET_DELTA non-empty]
```

Both deltas must be empty for CONTRACT_AUDIT: PASS.

`[ROLE_COMPLETE: CONTRACT AUDITOR]`

---

### DEVELOPER — Phases 1 through 5

**Status-Quo Baseline**
```
STATUS_QUO_METHOD: <current review method>
KNOWN_GAPS:        <what the team does not currently check>
```

---

**Phase 1-S: SESSION_TIMELINE** ← *author before Phase 1*

*(Mutation-first. SESSION_STATE derived from replay. Each cell cites its Phase 1-S source.)*

---

**Phase 1: Turn-by-Turn Trace**
```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE
     | CONFORMANCE | CONSTRAINT_VERDICTS | CHAIN_EFFECTS
```

`CONSTRAINT_VERDICTS` with CONV-NN verdicts (CONFORMS/DEVIATES/CHAIN_SUSPENDED) and
arithmetic evidence for non-CONDITIONAL MUTATION_SEMANTICS.

`CHAIN_EFFECTS`: CONV-NN → [downstream CONV-NN: ACTIVATED|SUSPENDED] per turn.

**Phase 1-T**: additive topic aggregate.

---

**Phase 2: Defect Classification**

Classify the seven standard defect classes:
DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

For each:
```
DEFECT_CLASS | VERDICT: FOUND|CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
             | STATUS_QUO_GAP
```

---

**Phase 3: Defect Reproduction + Phase 3-E: ENTANGLEMENT_MAP**

*(Same as V-01. Minimal reproduction + observable failure mode per FOUND defect.)*

---

**Phase 4: Fallback Chain + Escalation + Disambiguation**

*(Same as V-01.)*

---

**Phase 5: Coverage Metrics + Chain Budget Utilization + Simulation Delta**

**5-A: CONV_CHAIN_BUDGET Utilization** ← *new in V-05, placed before quality gate*

For each CHAIN-NN in Phase 0-A-9, count chain head DEVIATES turns from Phase 1:
```
CHAIN_BUDGET_UTILIZATION
  CHAIN_ID | HEAD_CONV | CHAIN_BUDGET | HEAD_DEVIATES_COUNT | STATUS: WITHIN_BUDGET | EXCEEDED
  ...
  OVERALL_CHAIN_BUDGET_STATUS: WITHIN_BUDGET | EXCEEDED[CHAIN-NN, ...]
```

If any chain exceeds its budget, emit a CHAIN_BUDGET_EXCEEDED finding for each:
```
CHAIN_BUDGET_EXCEEDED
  FINDING_CLASS: CHAIN_BUDGET_EXCEEDED (eighth structural finding class)
  CHAIN_ID:      CHAIN-NN
  HEAD_CONV:     CONV-NN
  BUDGET:        <declared max>
  ACTUAL:        <actual DEVIATES count>
  OVER_BY:       <actual - budget>
  FIRST_EXCEED_TURN: TURN_ID
  SUSPENDED_CONVS:   [CONV-NN, ...] (downstream constraints suspended during budget violation)
  IMPLICATION:   <domain impact — what the constraint chain violation means for flow correctness>
```

**5-B: Temporal Quality Gate**
```
TIMELINE_ANOMALY_RATE: anomalies_found / total_variable_turn_events
COVERAGE_QUALITY_GATE: CLEAN | DEGRADED
```
If DEGRADED: 5-C ratios are PROVISIONAL.

**5-C: Coverage Ratios**
```
STATUS: CONFIRMED | PROVISIONAL
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared
```

**5-D: Constraint Chain Final Status**
```
CHAIN_ID | HEAD_CONV | CHAIN_LENGTH | TURNS_SUSPENDED | FINAL_STATUS: INTACT|BROKEN
```

**5-E: SIMULATION_DELTA**
```
DEFECT_CLASS | DETECTION_METHOD: FOUND_BY_SIMULATION_ONLY | FOUND_BY_BOTH | STATUS_QUO_GAP_SUMMARY
```
CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY by definition: budget
thresholds cannot be verified by informal review.

**Phase 6: Adversarial Turn Injection**

*(Include CHAIN_EFFECTS for adversarial turns. Emit Phase 1-S entries.)*

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phases 6-A through 6-G

**Phase 6-A: Coverage Audit + Gate Verification**
```
CONTRACT_AUDIT_GATE_HONORED:   PASS | FAIL[developer bypassed gate or chain budget missing]
QUALITY_GATE_VERIFIED:         PASS | FAIL[anomaly count mismatch]
COVERAGE_STATUS_APPROPRIATE:   PASS | FAIL
TOPIC_COVERAGE_VERIFIED:       PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED:  PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:   PASS | FAIL[discrepancy]
SIMULATION_DELTA_COMPLETE:     PASS | FAIL[uncategorized defect or CHAIN_BUDGET_EXCEEDED missing]
```
CONTRACT_AUDIT_GATE_HONORED must be the final entry.

**Phase 6-B: Severity Co-Residency Audit**
```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS|FAIL
```
Note: CHAIN_BUDGET_EXCEEDED findings are structural, not severity-classed; they are EXEMPT
from co-residency audit but must appear in SIMULATION_DELTA.

**Phase 6-C: Entanglement Consistency Audit**
```
DEFECT | ENTANGLEMENT_VERDICT | SUPPORTING_TURN | CONSISTENCY: PASS|FAIL[cite]
```

**Phase 6-D: Topic Aggregate Consistency Audit**
```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS|FAIL
TOPIC_ROLLUP_MISMATCH_COUNT: N
```

**Phase 6-E: Session Timeline Consistency Audit**
```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS|FAIL
```

**Phase 6-F: Chain Budget Audit** ← *new in V-05*

For each CHAIN-NN:
```
CHAIN_ID | BUDGET | HEAD_DEVIATES_AUDITED | BUDGET_STATUS_CONSISTENT: PASS|FAIL
          | CHAIN_BUDGET_EXCEEDED_FINDING_PRESENT: YES|NO|N/A
          | CHAIN_BUDGET_AUDIT: PASS | FAIL[mismatch between audited count and reported count]
```
Verify by counting CONV-NN: DEVIATES verdicts for the chain head in Phase 1
CONSTRAINT_VERDICTS. If Developer reported WITHIN_BUDGET but Auditor count exceeds
budget, emit CHAIN_BUDGET_MISMATCH.

**Phase 6-G: Chain Integrity Audit** ← *from Axis B*
```
CHAIN_ID | CHAIN_STATUS_REPORTED | CHAIN_STATUS_AUDITED | CONSISTENT: PASS|FAIL[cite]
```
Verify ACTIVATED/SUSPENDED CHAIN_EFFECTS against upstream verdicts. Flag downstream
CONFORMS during SUSPENDED window as CHAIN_VERDICT_INCONSISTENCY.

`[ROLE_COMPLETE: AUDITOR]`
