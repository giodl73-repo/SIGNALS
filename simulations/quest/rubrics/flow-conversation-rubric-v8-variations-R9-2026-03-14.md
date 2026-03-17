# Quest Variations — flow-conversation — Round 9 (v8 rubric)

**Date:** 2026-03-14 | **Rubric version:** v8 | **Max score:** 116

---

## Variation Axes Selected

**Single-axis (3):**
- **Axis A — Role sequence**: introduce a Topology Architect role that runs before
  Developer, producing a signed topology contract both Developer and Auditor are
  bound to.
- **Axis B — Lifecycle emphasis**: add a Phase 0-D-7 SLOT_PATH_MAP as a third
  pre-computation artifact orthogonal to REACHABILITY_MAP (C-19) and
  TRANSITION_MAP (C-22), covering entity/slot-fill paths within slot-filling
  topics.
- **Axis C — Output format**: introduce a Phase 4-R REMEDIATION_SEQUENCE table
  that orders defect fixes by causal dependency derived from the C-23
  ENTANGLEMENT_MAP.

**Combined (2):**
- **Axes A + B**: Topology Architect produces SLOT_PATH_MAP + REACHABILITY_MAP
  as a unified topology artifact; Developer and Auditor share the same declared
  contract source.
- **Axes C + phrasing register**: Phase 4-R REMEDIATION_SEQUENCE with
  conversational imperative register (second-person "you" directives, annotated
  rationale blocks, decision callouts) rather than the formal structured-field
  style of prior rounds.

---

## V-01 — Axis A: Topology Architect Role (Single-Axis)

**Hypothesis:** Inserting a Topology Architect role before the Developer produces
a signed topology contract that both Developer trace and Auditor audit are
downstream of, preventing the Developer from implicitly constructing topology
while tracing and preventing the Auditor from having to infer graph structure
from execution evidence.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic
graph. Three roles operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **DEVELOPER** → **AUDITOR**

No role may begin until the preceding role's output section is complete and
carries its closing `[ROLE_COMPLETE: <ROLE_NAME>]` marker.

---

### TOPOLOGY ARCHITECT PHASE — Phase 0-A

The Topology Architect operates first. It has no access to any conversation
trace. Its output is a signed topology contract that all subsequent roles are
bound to.

**Phase 0-A-1: Topic Inventory**

Declare every topic in the Copilot Studio bot. For each:

```
TOPIC_ID: TOPIC-NN
NAME: <topic name>
TRIGGER_PHRASES: [phrase_1, phrase_2, ...]
ENTRY_CONDITION: <condition or NONE>
EXIT_NODES: [exit_1, exit_2, ...]
SLOT_FILLING: YES | NO
SESSION_VARS_WRITTEN: [var_1, var_2, ...]
SESSION_VARS_READ: [var_1, var_2, ...]
```

**Phase 0-A-2: REACHABILITY_MAP**

```
ENTRY_TOPIC: TOPIC-NN
REACHABLE: [TOPIC-NN, ...]
ORPHANED: [TOPIC-NN, ...]  (defined but unreachable from entry)
```

**Phase 0-A-3: TRANSITION_MAP**

Declare every edge in the conversation graph:

```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN | condition: <condition> | REQUIRED | OPTIONAL
```

**Phase 0-A-4: SLOT_PATH_MAP**

For every topic with `SLOT_FILLING: YES`, declare the canonical slot-fill path
and all known short-circuit variants:

```
SLOT_PATH-NN | topic: TOPIC-NN | slots: [slot_1, slot_2, ...] | canonical_turns: N
SLOT_PATH-NN-SC1 | type: SHORT_CIRCUIT | skipped_slots: [slot_1] | condition: <user provides slot upfront>
SLOT_PATH-NN-SC2 | type: SHORT_CIRCUIT | skipped_slots: [slot_1, slot_2] | condition: <user provides all upfront>
```

**Phase 0-A-5: SEVERITY_CLASS_MAP**

```
P0 | CRITICAL      | session corruption or unescapable loop
P1 | HIGH          | user reaches dead end with no fallback
P2 | MEDIUM        | suboptimal path but recoverable in <= 3 turns
P3 | LOW           | cosmetic or redundant transition
EXEMPT | CONFIRMED_ABSENT | no severity applies
```

**Phase 0-A-6: Topology Invariants**

Pre-commit named topology invariants:

```
INVARIANT-TOPO-NN: <statement>   (e.g., "every topic has at least one exit node")
INVARIANT-SV-NN:   <statement>   (e.g., "session variable X is cleared on any topic exit")
```

`[ROLE_COMPLETE: TOPOLOGY_ARCHITECT]`

---

### DEVELOPER PHASE — Phases 0-D through 4

The Developer is bound to the Topology Architect's contract. It may not add,
remove, or rename any topology element declared in Phase 0-A. If the Developer
discovers a topology element absent from Phase 0-A, it must raise a
`CONTRACT_GAP` flag before the trace begins.

**Phase 0-D: Domain Binding**

```
CS_VOCABULARY_BINDING: [topic, trigger phrase, condition, fallback topic, escalation,
                        session variable, slot, entity, adaptive card, Power Automate flow]
PROHIBITED_TERMS: [intent, utterance class, NLU model, chatbot, bot flow, dialog node]
CONTRACT_SOURCE: Phase 0-A
CONTRACT_GAPS: [TOPIC-NN added | TRANS-NN added | NONE]
```

**Phase 1: Turn-by-Turn Trace**

Walk the conversation turn-by-turn. For each turn, emit a row:

```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE | CONFORMANCE
```

- `SLOT_PATH_ID`: cite the relevant SLOT_PATH-NN from Phase 0-A-4 if this turn
  is within a slot-filling sequence; `N/A` otherwise.
- `TRANSITION_ID`: cite the relevant TRANS-NN from Phase 0-A-3.
- `SESSION_STATE`: show active variable values at end of turn.
- `CONFORMANCE`: `CONFORMS` | `DEVIATES[reason]`

**Phase 1-T: Topic Aggregate** (additive to Phase 1)

For each topic visited, emit one aggregate row:

```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

**Phase 1-S: Slot-Fill Path Coverage**

For each SLOT_PATH-NN declared in Phase 0-A-4, report:

```
SLOT_PATH_ID | STATUS: EXERCISED | UNEXERCISED | PARTIAL
             | TURNS_EXERCISED | SHORT_CIRCUIT_TRIGGERED: YES | NO | N/A
```

An unexercised canonical slot-fill path is a `SLOT_GAP` defect — a sixth
structural defect class at slot-graph level, distinct from ORPHAN (graph level)
and orphaned edge (transition level).

**Phase 2: Defect Classification**

For each defect class — DEAD_END, INFINITE_LOOP, INTENT_COLLISION,
MISSING_FALLBACK, ORPHAN, SLOT_GAP — emit a row:

```
DEFECT_CLASS | VERDICT: FOUND | CONFIRMED_ABSENT
             | EXAMPLE (if FOUND) | INVARIANT_CITE (CONFIRMED_ABSENT requires cite)
             | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
```

`CONFIRMED_ABSENT` rows: `SEVERITY_CLASS = EXEMPT`.
`FOUND` rows: `SEVERITY_CLASS` ∈ {P0, P1, P2, P3}; must coexist with
`INVARIANT_CITE`.

`RECOVERY`:
- `FOUND` rows: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` or
  `UNRECOVERABLE[reason]`
- `CONFIRMED_ABSENT`: `EXEMPT`

`ENTANGLEMENT_VERDICT`: `ISOLATED` | `ENABLES[DEFECT_CLASS]` |
`MASKED_BY[DEFECT_CLASS]`. For `MASKED_BY` defects, recovery becomes
conditional: `RECOVERABLE[min_turns=N, target=TOPIC-NN,
requires_fix=DEFECT_CLASS]`.

**Phase 3: Defect Reproduction**

For each `FOUND` defect, provide the minimal utterance sequence that triggers
it and the observable failure mode.

**Phase 3-E: ENTANGLEMENT_MAP**

Emit the full causal graph across FOUND defects:

```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B | REMEDIATION_ORDER
```

Where `REMEDIATION_ORDER` is the fix sequence number derived from causal
dependency (fix the `ENABLES` source before fixing the downstream effect).

**Phase 4: Fallback Chain Coverage**

Trace at least one fallback path to completion: no topic match → fallback topic
triggered → escalation or graceful exit. Show the full chain.

**Phase 4-R: REMEDIATION_SEQUENCE**

Using the ENTANGLEMENT_MAP from Phase 3-E, emit an ordered remediation table:

```
FIX_ORDER | DEFECT_CLASS | DEFECT_INSTANCE | BLOCKING_FIXES | UNBLOCKED_BY_FIX
```

`BLOCKING_FIXES`: list of fix orders that must complete before this row can be
addressed. `UNBLOCKED_BY_FIX`: which downstream defects become addressable once
this fix ships. A defect with no BLOCKING_FIXES and ISOLATED entanglement has
fix order 1. Fixes that ENABLE downstream defects must complete in topological
order.

**Phase 5: Coverage Metrics**

```
TOPIC_COVERAGE:       reachable_visited / total_reachable  (from Phase 0-A-2)
TRANSITION_COVERAGE:  transitions_exercised / total_declared (from Phase 0-A-3)
SLOT_PATH_COVERAGE:   slot_paths_exercised / total_declared  (from Phase 1-S)
```

Report all three as independent, orthogonal coverage signals.

**Phase 6: Adversarial Turn Injection**

Inject at least one: unexpected topic switch during slot-fill, out-of-scope
utterance mid-flow, or session timeout simulation. Show agent response and state
delta. Record the TRANSITION_ID and SLOT_PATH_ID exercised (if any).

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR PHASE — Phase 6-A through 6-D

The Auditor operates on the completed Developer output and the Topology Architect
contract. It does not revise; it audits.

**Phase 6-A: Coverage Audit**

Verify that all three coverage ratios in Phase 5 are consistent with the
declared topology artifacts in Phase 0-A.

```
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:  PASS | FAIL[discrepancy]
```

**Phase 6-B: Severity Co-Residency Audit**

For each `FOUND` defect row, verify that `SEVERITY_CLASS` and `INVARIANT_CITE`
coexist. Neither column may carry a value without the other. `CONFIRMED_ABSENT`
rows must carry `SEVERITY_CLASS = EXEMPT`.

```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS | FAIL
```

**Phase 6-C: Entanglement Consistency Audit**

Verify that each `ENTANGLEMENT_VERDICT` in the defect table is consistent with
turn-level evidence in Phase 1. A `MASKED_BY` verdict that is not supported by
a specific turn sequence is a Phase 6-C failure.

```
DEFECT | ENTANGLEMENT_VERDICT | TURN_EVIDENCE | CONSISTENCY: PASS | FAIL[cite]
```

**Phase 6-D: Remediation Sequence Audit**

Verify that the REMEDIATION_SEQUENCE in Phase 4-R forms a valid topological
order: no defect appears at a fix order N where a defect it depends on appears
at fix order > N.

```
REMEDIATION_SEQUENCE_VALID: PASS | FAIL[cycle or ordering violation]
```

**Phase 6-E: Prohibited Vocabulary Verification**

Scan all Developer output phases. Confirm that no prohibited term from Phase 0-D
appears in any Developer section.

```
PROHIBITED_TERM_SCAN: CLEAN | VIOLATION[term, phase, turn]
```

`[ROLE_COMPLETE: AUDITOR]`

---

## V-02 — Axis B: Slot-Path Coverage Map (Single-Axis)

**Hypothesis:** Adding a Phase 0-D-7 SLOT_PATH_MAP as a third orthogonal
pre-computation artifact (alongside REACHABILITY_MAP and TRANSITION_MAP) exposes
an unexercised slot-fill path as a structural defect class (SLOT_GAP) invisible
to topic-level and edge-level coverage. Short-circuit slot paths — where the
user provides all required entities upfront — are a distinct coverage gap from
canonical sequential fill.

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic
graph. Two roles operate in strict phase-gate order:

**DEVELOPER** → **AUDITOR**

The Auditor may not begin until `[ROLE_COMPLETE: DEVELOPER]` is present.

---

### DEVELOPER — Phases 0-D through 6

**Phase 0-D: Domain Pre-Contract**

Declare before any trace output:

**0-D-1 Topic Inventory** — for each topic: TOPIC_ID, trigger phrases,
slot-filling status, session variables written/read.

**0-D-2 CS Vocabulary Binding** — permitted terms: topic, trigger phrase,
condition, fallback topic, escalation, session variable, slot, entity, Power
Automate flow. Prohibited: intent, chatbot, NLU model, dialog node.

**0-D-3 Session Variable Registry** — for each variable: VAR_ID, type, initial
value, persistence class (SESSION | TOPIC_SCOPED | GLOBAL).

**0-D-4 REACHABILITY_MAP**

```
ENTRY_TOPIC: TOPIC-NN
REACHABLE:   [TOPIC-NN, ...]
ORPHANED:    [TOPIC-NN, ...]
```

Orphaned topics are ORPHAN defects — a fifth structural defect class.

**0-D-5 TRANSITION_MAP**

Declare every edge:

```
TRANS-NN | source: TOPIC-NN | target: TOPIC-NN | condition: <text> | REQUIRED | OPTIONAL
```

**0-D-6 SEVERITY_CLASS_MAP + Topology Invariants**

Severity classes: P0 (session corruption / unescapable loop), P1 (dead end, no
fallback), P2 (suboptimal but recoverable ≤ 3 turns), P3 (cosmetic), EXEMPT
(CONFIRMED_ABSENT rows).

Named invariants: `INVARIANT-TOPO-NN`, `INVARIANT-SV-NN`.

**0-D-7 SLOT_PATH_MAP** ← *new in V-02*

For every topic with slot-filling, declare all slot paths:

```
SLOT_PATH-NN     | topic: TOPIC-NN | slots_required: [slot_1, slot_2, ...]
                 | canonical_turns: N | path_type: CANONICAL
SLOT_PATH-NN-SC1 | topic: TOPIC-NN | slots_skipped: [slot_1]
                 | canonical_turns: N-1 | path_type: SHORT_CIRCUIT
                 | trigger_condition: <user provides slot_1 upfront>
```

An unexercised canonical SLOT_PATH-NN is a `SLOT_GAP` defect — a **sixth
structural defect class** at slot-graph level, distinct from:
- ORPHAN (topic graph level, C-19)
- orphaned edge (transition level, C-22)

**Phase 1: Turn-by-Turn Trace**

Table columns:

```
TURN | USER_UTTERANCE | TOPIC_MATCHED | SLOT_PATH_ID | NODES_EXECUTED
     | AGENT_RESPONSE | TRANSITION_ID | SESSION_STATE | INVARIANT_CONFORMANCE
     | CONFORMANCE
```

- `SLOT_PATH_ID`: cite SLOT_PATH-NN from Phase 0-D-7 when inside a slot-fill
  sequence; `N/A` otherwise.
- `TRANSITION_ID`: cite TRANS-NN from Phase 0-D-5.
- `INVARIANT_CONFORMANCE`: `HOLDS` | `VIOLATED[INVARIANT-ID]`.
- `CONFORMANCE`: `CONFORMS` | `DEVIATES[reason]`.

**Phase 1-T: Topic Aggregate** (additive)

One row per topic visited:

```
TOPIC_ID | TURNS_VISITED | SESSION_VARS_SET | SESSION_VARS_READ
         | DEFECT_CITATIONS | ADVERSARIAL_COUNT | CONFORMANCE_ROLLUP
```

**Phase 1-S: Slot-Path Coverage** ← *new in V-02*

One row per declared SLOT_PATH-NN:

```
SLOT_PATH_ID | TOPIC_ID | STATUS: EXERCISED | UNEXERCISED | PARTIAL
             | TURNS_EXERCISED | SHORT_CIRCUIT_HIT: YES | NO | N/A
             | DEFECT_VERDICT: SLOT_GAP | NONE
```

**Phase 2: Defect Classification**

Six classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHAN, SLOT_GAP.

For each:

```
DEFECT_CLASS | VERDICT: FOUND | CONFIRMED_ABSENT
             | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS | RECOVERY
             | ENTANGLEMENT_VERDICT
```

Typing rules:
- `CONFIRMED_ABSENT`: `SEVERITY_CLASS = EXEMPT`; `INVARIANT_CITE` required.
- `FOUND`: `SEVERITY_CLASS` ∈ {P0, P1, P2, P3}; `INVARIANT_CITE` required
  (coexistence enforced in Phase 6-B).
- `RECOVERY` for `FOUND`: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` or
  `UNRECOVERABLE[reason]`.
- `ENTANGLEMENT_VERDICT`: `ISOLATED` | `ENABLES[DEFECT_CLASS]` |
  `MASKED_BY[DEFECT_CLASS]`.

**Phase 3: Reproduction Steps**

For each FOUND defect: minimal utterance sequence + observable failure mode.

**Phase 3-E: ENTANGLEMENT_MAP**

```
DEFECT_A | ENTANGLEMENT_VERDICT | DEFECT_B
```

For `MASKED_BY` defects: recovery becomes
`RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`.

**Phase 4: Fallback Chain**

Trace at least one fallback path to completion: no match → fallback topic →
escalation or graceful exit. Show full chain with TRANSITION_IDs.

**Phase 5: Coverage Metrics**

```
TOPIC_COVERAGE:      reachable_visited / total_reachable   (denominator from Phase 0-D-4)
TRANSITION_COVERAGE: transitions_exercised / total_declared (denominator from Phase 0-D-5)
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared  (denominator from Phase 0-D-7)
```

Three independent, orthogonal coverage signals.

**Phase 6: Adversarial Injection**

At least one: topic switch during slot fill, out-of-scope utterance, session
timeout. Show state delta. Record SLOT_PATH_ID if slot-fill was interrupted.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phase 6-A through 6-C

**Phase 6-A: Coverage Audit**

Verify all three coverage ratios against declared topology:

```
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[discrepancy]
SLOT_PATH_COVERAGE_VERIFIED:  PASS | FAIL[discrepancy]
```

Report slot-path denominator consistency: `slot_paths_exercised` must count
only paths with STATUS = EXERCISED in Phase 1-S.

**Phase 6-B: Severity Co-Residency Audit**

```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS | FAIL
```

Every FOUND row: both columns populated. Every CONFIRMED_ABSENT row:
SEVERITY_CLASS = EXEMPT.

**Phase 6-C: Entanglement Consistency Audit**

```
DEFECT | ENTANGLEMENT_VERDICT | TURN_EVIDENCE | CONSISTENCY: PASS | FAIL[cite]
```

A `MASKED_BY` verdict without supporting turn-level evidence is a Phase 6-C
failure.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-03 — Axis C: Remediation Sequence Table (Single-Axis)

**Hypothesis:** A Phase 4-R REMEDIATION_SEQUENCE table that derives fix order
from the C-23 ENTANGLEMENT_MAP provides actionable output that the current rubric
does not require: not just "which defects exist and how they relate" but "in what
order must a developer fix them to avoid testing a masked fix before its
dependency is resolved."

---

You are simulating a multi-turn Copilot Studio agent conversation through a topic
graph. Two roles operate in strict sequence:

**DEVELOPER** → **AUDITOR**

Do not begin the AUDITOR section until `[ROLE_COMPLETE: DEVELOPER]` is present.

---

### DEVELOPER — Phases 0-D through 6

**Phase 0-D: Pre-Declarations** (all of these before any trace)

**0-D-1** Topic inventory: TOPIC_ID, name, trigger phrases, slot-filling flag,
session variables written/read.

**0-D-2** CS vocabulary binding. Permitted: topic, trigger phrase, condition,
fallback topic, escalation, session variable, slot, entity, adaptive card,
Power Automate flow, escalation node. Prohibited: intent, utterance class,
NLU model, chatbot, dialog node, bot skill.

**0-D-3** Session variable registry: VAR_ID, type, initial value, persistence
class (SESSION | TOPIC_SCOPED | GLOBAL).

**0-D-4** REACHABILITY_MAP: entry topic, reachable set, orphaned topics. Orphaned
topics are ORPHAN defects.

**0-D-5** TRANSITION_MAP (`TRANS-NN | source | target | condition | REQUIRED |
OPTIONAL`). Unexercised REQUIRED edges are orphaned-edge defects.

**0-D-6** SEVERITY_CLASS_MAP (P0–P3, EXEMPT) + named topology invariants
(`INVARIANT-TOPO-NN`, `INVARIANT-SV-NN`).

**Phase 1: Turn Trace**

One row per turn:

```
TURN | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE
     | TRANSITION_ID | SESSION_STATE | INVARIANT_CONFORMANCE | CONFORMANCE
```

**Phase 1-T: Topic Aggregate**

One row per topic visited: TOPIC_ID, turns visited, session vars set/read, defect
citations, adversarial count, conformance rollup.

**Phase 2: Defect Classification**

Classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK, ORPHAN.
For each:

```
DEFECT_CLASS | VERDICT | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS
             | RECOVERY | ENTANGLEMENT_VERDICT
```

Typing constraints:
- `CONFIRMED_ABSENT`: SEVERITY_CLASS = EXEMPT; INVARIANT_CITE required.
- `FOUND`: SEVERITY_CLASS ∈ {P0, P1, P2, P3}; INVARIANT_CITE required.
- RECOVERY: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` or
  `UNRECOVERABLE[reason]` for FOUND; EXEMPT for CONFIRMED_ABSENT.
- For MASKED_BY defects: `RECOVERABLE[..., requires_fix=DEFECT_CLASS]`.

**Phase 3: Reproduction Steps**

For each FOUND defect: exact utterance sequence + observable failure mode.

**Phase 3-E: ENTANGLEMENT_MAP**

Full causal graph across FOUND defects:

```
DEFECT_ID | ENTANGLEMENT_VERDICT | RELATED_DEFECT_ID | CAUSAL_DIRECTION
```

`CAUSAL_DIRECTION`: UPSTREAM (this defect causes) | DOWNSTREAM (this defect
is caused by).

**Phase 4: Fallback Chain**

Trace at least one fallback path to completion. Show every node in the chain.

**Phase 4-R: REMEDIATION_SEQUENCE** ← *new in V-03*

Derive a fix order from the ENTANGLEMENT_MAP. Rules:

1. An ISOLATED defect has no blocking dependency.
2. A defect that ENABLES another defect must be fixed *after* the downstream
   defect is known (it contributes to it), but *before* its own downstream
   effects can be fully verified.
3. A MASKED_BY defect cannot be confirmed or reproduced until its masking
   defect is fixed first.

Emit the sequence as a table:

```
FIX_ORDER | DEFECT_CLASS | SEVERITY | DEPENDS_ON_FIX_ORDERS
          | UNBLOCKS_FIX_ORDERS | RATIONALE
```

`DEPENDS_ON_FIX_ORDERS`: fix orders that must complete before this can begin.
`UNBLOCKS_FIX_ORDERS`: fix orders that become actionable once this ships.
`RATIONALE`: one sentence citing the entanglement relationship.

**Structural rules for Phase 4-R:**
- No circular dependencies permitted. If a cycle exists, flag it as a
  `REMEDIATION_CYCLE` defect and escalate to P0.
- Every FOUND defect must appear in exactly one FIX_ORDER row.
- CONFIRMED_ABSENT defects are excluded.

**Phase 5: Coverage Metrics**

```
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
REMEDIATION_DEPTH:   defects_with_dependency / total_found  (entanglement density)
```

`REMEDIATION_DEPTH` is the fraction of FOUND defects that have at least one
blocking or unblocking dependency — a measure of how tangled the defect graph is.

**Phase 6: Adversarial Injection**

At least one adversarial scenario. Show topic match, state delta, TRANSITION_ID
exercised.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phase 6-A through 6-D

**Phase 6-A: Coverage Audit**

```
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[discrepancy]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[discrepancy]
```

**Phase 6-B: Severity Co-Residency Audit**

```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS | FAIL
```

**Phase 6-C: Entanglement Consistency Audit**

```
DEFECT | ENTANGLEMENT_VERDICT | TURN_EVIDENCE | CONSISTENCY: PASS | FAIL[cite]
```

**Phase 6-D: Remediation Sequence Audit** ← *new in V-03*

Verify Phase 4-R forms a valid topological order.

```
TOPOLOGICAL_ORDER_VALID: PASS | FAIL[cycle or ordering violation]
REMEDIATION_CYCLE_DETECTED: YES[description] | NO
ALL_FOUND_DEFECTS_COVERED: PASS | FAIL[missing DEFECT_CLASS]
RATIONALE_PRESENT_FOR_ALL: PASS | FAIL[FIX_ORDER with empty rationale]
```

A `FAIL` on `TOPOLOGICAL_ORDER_VALID` means a MASKED_BY defect appears at a
lower fix order than the defect masking it — the plan would have a developer
attempt to fix an effect before its cause.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-04 — Axes A + B: Topology Architect + Session Timeline (Combined)

**Hypothesis:** Combining the Topology Architect role (V-01) with a Phase 1-S
SESSION_TIMELINE — a turn-indexed log of state mutations additive to the Phase
1-T topic aggregate — surfaces temporal ordering bugs invisible to both topic
and edge coverage: a session variable written in turn 3 that is read in turn 2
of a repeat visit is a timeline anomaly, not a defect classifiable as any of
the five standard classes.

---

You are simulating a multi-turn Copilot Studio agent conversation. Three roles
operate in strict phase-gate order:

**TOPOLOGY ARCHITECT** → **DEVELOPER** → **AUDITOR**

---

### TOPOLOGY ARCHITECT — Phase 0-A

The Topology Architect produces the signed topology contract. The Developer and
Auditor are both downstream consumers; neither may modify the contract.

**Phase 0-A-1: Topic Inventory** (TOPIC_ID, trigger phrases, slot-filling flag,
session vars written/read)

**Phase 0-A-2: REACHABILITY_MAP** (entry topic, reachable set, orphaned topics)

**Phase 0-A-3: TRANSITION_MAP** (`TRANS-NN | source | target | condition |
REQUIRED | OPTIONAL`)

**Phase 0-A-4: SLOT_PATH_MAP** (canonical and short-circuit paths per
slot-filling topic; see V-02 Phase 0-A-4 structure)

**Phase 0-A-5: SEVERITY_CLASS_MAP** (P0–P3, EXEMPT)

**Phase 0-A-6: Session Variable Timeline Contract** ← *new in V-04*

For each session variable, declare the expected lifecycle:

```
VAR_ID | FIRST_WRITTEN_TOPIC: TOPIC-NN | PERSISTS_ACROSS_TOPICS: YES | NO
       | CLEARED_BY: TOPIC-NN | NEVER | READ_AFTER_CLEARED: FORBIDDEN | ALLOWED
```

`READ_AFTER_CLEARED: FORBIDDEN` creates a named invariant: any turn that reads
VAR_ID after it has been cleared is a `TIMELINE_ANOMALY` — a seventh structural
defect class at state-ordering level.

**Phase 0-A-7: Topology Invariants** (`INVARIANT-TOPO-NN`, `INVARIANT-SV-NN`)

`[ROLE_COMPLETE: TOPOLOGY_ARCHITECT]`

---

### DEVELOPER — Phases 0-D through 6

**Phase 0-D: Domain Binding**

```
CS_VOCABULARY_BINDING: [topic, trigger phrase, condition, fallback topic,
                        escalation, session variable, slot, entity,
                        Power Automate flow]
PROHIBITED_TERMS: [intent, chatbot, NLU model, dialog node]
CONTRACT_SOURCE: Phase 0-A
CONTRACT_GAPS: [NONE | item description]
```

**Phase 1: Turn Trace**

```
TURN | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE
     | TRANSITION_ID | SESSION_STATE | INVARIANT_CONFORMANCE | CONFORMANCE
```

**Phase 1-T: Topic Aggregate** (additive to Phase 1)

One row per topic: TOPIC_ID, turns visited, session vars set/read, defect
citations, adversarial count, conformance rollup.

**Phase 1-S: SESSION_TIMELINE** ← *new in V-04*

A turn-indexed log of every session variable mutation, strictly additive to
Phase 1 and Phase 1-T. Do not remove session state columns from Phase 1.

```
TURN | VAR_ID | MUTATION: WRITE | READ | CLEAR | NO_CHANGE
     | PRE_VALUE | POST_VALUE | TOPIC_ID | TIMELINE_ANOMALY: YES | NO
```

`TIMELINE_ANOMALY: YES` when:
- A variable is READ after being CLEARED, and the contract declares
  `READ_AFTER_CLEARED: FORBIDDEN` for that variable.
- A variable is WRITTEN in a turn whose TOPIC_ID is not the declared
  `FIRST_WRITTEN_TOPIC` and no contract override exists.

Each `TIMELINE_ANOMALY: YES` row generates a `TIMELINE_ANOMALY` defect finding
in Phase 2.

**Phase 2: Defect Classification**

Seven classes: DEAD_END, INFINITE_LOOP, INTENT_COLLISION, MISSING_FALLBACK,
ORPHAN, SLOT_GAP, TIMELINE_ANOMALY.

Standard row structure:

```
DEFECT_CLASS | VERDICT | EXAMPLE | INVARIANT_CITE | SEVERITY_CLASS
             | RECOVERY | ENTANGLEMENT_VERDICT
```

TIMELINE_ANOMALY defects cite the `VAR_ID` and the TURN from Phase 1-S as the
EXAMPLE field.

**Phase 3: Reproduction Steps + Phase 3-E: ENTANGLEMENT_MAP**

(Same structure as V-01 Phase 3 and Phase 3-E.)

**Phase 4: Fallback Chain**

(Same structure as previous variations.)

**Phase 5: Coverage Metrics**

```
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
SLOT_PATH_COVERAGE:  slot_paths_exercised / total_declared
TIMELINE_ANOMALY_RATE: anomalies_found / total_state_mutations
```

`TIMELINE_ANOMALY_RATE` is a quality signal, not a pass/fail threshold.

**Phase 6: Adversarial Injection**

At least one scenario. Show SESSION_TIMELINE entries for the adversarial turns.

`[ROLE_COMPLETE: DEVELOPER]`

---

### AUDITOR — Phase 6-A through 6-E

**Phase 6-A: Coverage Audit**

```
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL
SLOT_PATH_COVERAGE_VERIFIED:  PASS | FAIL
```

**Phase 6-B: Severity Co-Residency Audit**

(Standard structure: SEVERITY_CLASS + INVARIANT_CITE coexistence per FOUND row.)

**Phase 6-C: Entanglement Consistency Audit**

(Standard structure: ENTANGLEMENT_VERDICT vs turn-level evidence.)

**Phase 6-D: Topic Aggregate Consistency Audit**

Verify Phase 1-T conformance rollup is consistent with Phase 1 CONFORMANCE
column. A CONFORMS rollup for a topic that contains at least one DEVIATES turn
is an audit failure.

```
TOPIC_ID | PHASE_1_DEVIATES_COUNT | PHASE_1T_ROLLUP | CONSISTENT: PASS | FAIL
```

**Phase 6-E: Session Timeline Consistency Audit** ← *new in V-04*

Verify that the SESSION_TIMELINE in Phase 1-S is consistent with Phase 1
SESSION_STATE column at every turn.

```
TURN | PHASE_1_SESSION_STATE | PHASE_1S_COMPUTED_STATE | CONSISTENT: PASS | FAIL
TIMELINE_ANOMALY_CONFIRMED: PASS | FAIL[cite VAR_ID, TURN]
```

A `TIMELINE_ANOMALY: YES` row in Phase 1-S that is not cited in a Phase 2
defect row is a Phase 6-E finding.

`[ROLE_COMPLETE: AUDITOR]`

---

## V-05 — Axes C + Phrasing Register: Remediation Sequence, Conversational Register (Combined)

**Hypothesis:** The formal structured-field style of prior rounds aids machine
parseability but can reduce human readability for the remediation output — the
section of the artifact most likely to be acted on by a developer. V-05 tests
whether a conversational, second-person imperative register for Phase 4-R
produces a more readable remediation plan while still satisfying the structural
typing constraints required by C-13 and C-15.

---

You are a Copilot Studio domain expert running a full conversation-flow simulation.
Walk through the multi-turn dialog, surface every structural defect, and produce
an ordered fix plan a developer can act on immediately.

Work in two stages: **Developer** then **Auditor**. Don't start the Auditor
section until the Developer section ends with `[ROLE_COMPLETE: DEVELOPER]`.

---

### Developer

Before you write a single trace turn, lock down the topology. Do this in order:

**Step 1 — Map your topics.** List every topic: its ID, its trigger phrases, any
session variables it reads or writes, and whether it does slot-filling. Use this
vocabulary throughout and nowhere else: *topic, trigger phrase, condition,
fallback topic, escalation, session variable, slot, entity, Power Automate flow*.
If you catch yourself writing *intent*, *chatbot*, or *NLU model*, stop and
rewrite.

**Step 2 — Draw the reachability map.** Pick the entry topic. Walk every
transition path and list every topic reachable from entry. Any topic you defined
but can't reach from entry is an orphan — that's already a defect, and you
haven't written a single trace turn yet.

```
ENTRY: TOPIC-NN
REACHABLE:  [TOPIC-NN, ...]
ORPHANED:   [TOPIC-NN, ...]
```

**Step 3 — Declare every transition edge.** Number them TRANS-01, TRANS-02, and
so on. For each, say where it starts, where it ends, what condition triggers it,
and whether it's required or optional.

```
TRANS-NN | from: TOPIC-NN | to: TOPIC-NN | condition: <text> | REQUIRED | OPTIONAL
```

A required edge you never exercise is an orphaned edge — same severity as an
orphaned topic.

**Step 4 — Assign severity buckets.** You'll need these when classifying defects:

- P0: session corruption or a loop the user can never escape
- P1: user hits a dead end with no fallback
- P2: bad path but user recovers in three turns or fewer
- P3: minor, cosmetic
- EXEMPT: a defect class you've confirmed is absent (not a real defect, no
  severity)

**Step 5 — Name your invariants.** Write down two or three topology guarantees
you're betting on: "every topic has at least one exit node," "session variable
X is always cleared on topic exit." Label them INVARIANT-TOPO-01, INVARIANT-SV-01
and so on. You'll use these IDs to justify your absence claims later.

**Step 6 — Trace the conversation turn by turn.** For each turn, fill in this
row — no skipping columns:

```
TURN | USER_UTTERANCE | TOPIC_MATCHED | NODES_EXECUTED | AGENT_RESPONSE
     | TRANSITION_ID | SESSION_STATE | INVARIANT_CONFORMANCE | CONFORMANCE
```

`INVARIANT_CONFORMANCE`: HOLDS or VIOLATED[which invariant].
`CONFORMANCE`: CONFORMS or DEVIATES[why].

**Step 7 — Add the topic aggregate.** One row per topic you visited — additive to
the trace, not a replacement:

```
TOPIC_ID | TURNS | VARS_SET | VARS_READ | DEFECT_CITATIONS
         | ADVERSARIAL_TURNS | CONFORMANCE_ROLLUP
```

**Step 8 — Classify every defect type.** Go through these six classes one by one.
For each: did you find it or confirm it absent?

DEAD_END | INFINITE_LOOP | INTENT_COLLISION | MISSING_FALLBACK | ORPHAN |
(any orphaned transition edge you found in Step 3)

Fill in a row for each:

```
DEFECT_CLASS | FOUND | CONFIRMED_ABSENT
             | EXAMPLE (if FOUND) | INVARIANT_CITE (required for CONFIRMED_ABSENT)
             | SEVERITY_CLASS | RECOVERY | ENTANGLEMENT_VERDICT
```

Typing rules — these are hard constraints, not guidelines:
- If CONFIRMED_ABSENT: `SEVERITY_CLASS = EXEMPT`. No exceptions.
- If FOUND: `SEVERITY_CLASS` must be P0, P1, P2, or P3. You cannot write
  "medium" or "low" here — use the enum.
- FOUND rows also need INVARIANT_CITE. If you don't have an invariant that
  covers it, add one in Step 5 retroactively and note the addition.
- RECOVERY for FOUND: `RECOVERABLE[min_turns=N, target=TOPIC-NN]` or
  `UNRECOVERABLE[reason]`.
- If a defect is MASKED_BY another:
  `RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`.
- ENTANGLEMENT_VERDICT: `ISOLATED` | `ENABLES[DEFECT_CLASS]` |
  `MASKED_BY[DEFECT_CLASS]`.

**Step 9 — Write the reproduction steps.** For each FOUND defect: the exact
utterance sequence that triggers it, and what the user sees when it fires.

**Step 10 — Map the entanglement.** Draw the causal graph across your FOUND
defects:

```
DEFECT_A | ENTANGLEMENT | DEFECT_B
```

If DEAD_END ENABLES INFINITE_LOOP: write it. If MISSING_FALLBACK MASKS DEAD_END:
write it. This is the input to the fix plan.

**Step 11 — Trace the fallback chain.** Pick the worst-case no-match scenario.
Walk every node from "no topic matched" to "user is either escalated or gracefully
exited." Show the whole chain, not just the first fallback node.

**Step 12 — Write the fix plan.** ← *conversational register, new in V-05*

Here's where you tell the developer exactly what to fix and in what order. Use
plain English. The structural typing is still required — but the rationale should
read like an engineer talking to another engineer, not a schema dump.

Write one block per fix, ordered so that each block's dependencies are already
resolved by the time the developer gets to it:

---

**Fix [N] — [SHORT_TITLE]**
Severity: [P0 | P1 | P2 | P3]
Depends on: [Fix N, Fix N, ... | None]
Unblocks: [Fix N, Fix N, ... | Nothing]

[Two to three sentences in plain English: what is broken, why it's broken, and
what the fix looks like. Reference the defect class and the entanglement
relationship if one exists. Example: "The MISSING_FALLBACK in TOPIC-03 is
masking a DEAD_END in TOPIC-07 — until you add the fallback exit node, you
won't be able to confirm whether the dead end is a real problem or an artifact
of the missing path."]

Structural record:
```
FIX_ORDER: N | DEFECT_CLASS: X | DEPENDS_ON: [N,...] | UNBLOCKS: [N,...]
```

---

Repeat for every FOUND defect. If no FOUND defects exist, write one block
confirming that the fix plan is empty and citing the invariants that support
each absence claim.

**Step 13 — Report coverage.** Three numbers:

```
TOPIC_COVERAGE:      reachable_visited / total_reachable
TRANSITION_COVERAGE: transitions_exercised / total_declared
```

**Step 14 — Inject an adversarial turn.** Try one of these: an out-of-scope
utterance mid-slot-fill, a topic switch the user forces at the worst possible
moment, or a session timeout. Show what happens. Note the TRANSITION_ID
exercised and whether it was already in your reachable set.

`[ROLE_COMPLETE: DEVELOPER]`

---

### Auditor

You have four jobs. Do them in order. Don't revise the Developer's output —
audit it.

**Audit 1 — Coverage verification.**

Check the two coverage ratios against the declared maps. Any denominator that
doesn't match the declared topology is wrong, not just imprecise.

```
TOPIC_COVERAGE_VERIFIED:      PASS | FAIL[what's wrong]
TRANSITION_COVERAGE_VERIFIED: PASS | FAIL[what's wrong]
```

**Audit 2 — Severity co-residency.**

Every FOUND row must have both SEVERITY_CLASS and INVARIANT_CITE. Neither column
can exist without the other. Every CONFIRMED_ABSENT row must show EXEMPT.

```
DEFECT | SEVERITY_CLASS_PRESENT | INVARIANT_CITE_PRESENT | CO_RESIDENCY: PASS | FAIL
```

**Audit 3 — Entanglement consistency.**

Every ENTANGLEMENT_VERDICT must be supported by a specific turn in the trace.
An ENABLES or MASKED_BY claim with no turn citation is a failure.

```
DEFECT | ENTANGLEMENT_VERDICT | SUPPORTING_TURN | CONSISTENT: PASS | FAIL
```

**Audit 4 — Fix plan topology.**

The fix plan must be a valid topological sort. A MASKED_BY defect appearing at
a lower fix order than the defect masking it means the plan tells the developer
to fix an effect before its cause — that's a structural failure.

```
FIX_PLAN_TOPOLOGICAL_ORDER: PASS | FAIL[which fix order has an ordering violation]
ALL_FOUND_DEFECTS_IN_PLAN:  PASS | FAIL[which FOUND defect is missing]
RATIONALE_PRESENT:          PASS | FAIL[which fix block has no plain-English rationale]
```

`[ROLE_COMPLETE: AUDITOR]`

---

*End of V-05.*
