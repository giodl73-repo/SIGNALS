## campaign-behavior — Quest Variations R2

Written to `simulations/quest/variations/campaign-behavior-variations-R2-2026-03-17.md`.

### Axis map

| Variation | Single/Combo | Axis | Hypothesis |
|-----------|-------------|------|------------|
| **V-01** | single | System topology census pre-execution | Enumerating components + shared state before sub-skills run creates a system-specific blast radius anchor (C-11) |
| **V-02** | single | Full typed schemas, all 5 sub-skills | Vocabulary-matched column schemas for every sub-skill satisfies C-12 at full coverage — V-04 from R1 only hit 4 of 5 |
| **V-03** | single | Post-execution blast radius calibration | CALIBRATION BLOCK after phases but before ranking forces grounding in actual findings, not predicted topology |
| **V-04** | combo | V-01 + V-02 (census + typed schemas) | Two strongest structural innovations together — blast radius anchored AND schemas purpose-built per sub-skill |
| **V-05** | combo | Census + typed schemas + phase gates + co-located severity/blast-radius | Structurally enforces all 13 rubric criteria; no criterion requires model inference |

### What the R2 variations target

**Why R1 variations don't fully pass v2:**
- **C-11** (blast radius operationalized): All R1 variations used generic definitions ("how broadly a failure propagates") — none named {{topic}}'s actual components or shared state
- **C-12** (typed schemas): Only V-04 had typed schemas; V-02/V-05 used uniform or prose templates
- **C-13** (severity × blast radius co-located): V-02/V-04/V-05 had both fields, but V-05 was the only one with an explicit "these are distinct" anti-conflation instruction

**Key design decisions in R2:**
1. V-01/V-04/V-05 introduce a topology census as STEP 0 — the census output becomes the blast radius vocabulary used in all finding rows
2. V-02/V-04/V-05 give each sub-skill its own schema — trace-contract gets Producer/Consumer/Expected/Actual, trace-state gets State/Preconditions/Trigger/Postcondition, flow-lifecycle gets Phase/Entry/Exit/Exception-handler, flow-conversation gets Node/Outbound-paths/Dead-end/Loop
3. V-03 uses a different C-11 strategy: calibrate blast radius *after* findings exist, not before, so grounding is evidence-driven rather than speculative
4. V-05 adds an explicit anti-merge instruction: "Do not merge [severity and blast radius] into a single 'impact' field" — directly prevents the C-13 failure mode
� Single axis: System topology census (C-11 target)

**Hypothesis:** Enumerating {{topic}}'s specific components, shared state surfaces, and
downstream callers as a mandatory STEP 0 — before any sub-skill runs — produces a
system-specific blast radius anchor that a cold reviewer can use to verify finding ranks.
Generic blast radius language ("how broadly a failure propagates") fails C-11 because it
carries no verifiable system reference. A census-derived anchor names actual components.

```
Run campaign-behavior for: {{topic}}

STEP 0 — TOPOLOGY CENSUS (complete before running any sub-skill)

Before simulating anything, enumerate the architecture of {{topic}}:

1. Components — list every distinct service, store, agent, queue, or API involved
2. Shared state surfaces — list every resource two or more components read or write
   (database tables, event streams, caches, global config flags)
3. Downstream callers — list every component or user path that depends on
   {{topic}} being correct
4. User-visible surfaces — list observable outputs where a defect would be visible
   (API responses, UI states, notifications, events)

BLAST RADIUS ANCHOR — derived from the census above:
A finding has WIDE blast radius if it affects two or more components from the list
above, or corrupts a shared state surface from the list above.
A finding has NARROW blast radius if it is contained to one component with no
shared-state writes and no downstream callers affected.

When stating blast radius in ranked findings, name the specific component or shared
state surface from this census. Do not use generic language.

---

Now run all five sub-skills. Do not skip any.

Execution order:
1. flow-lifecycle
2. flow-conversation
3. trace-state
4. trace-contract
5. trace-permissions

flow-lifecycle
Simulate the full business lifecycle for {{topic}}.
Walk each phase: creation, active transitions, terminal states, exception paths.
For each transition: entry condition, exit condition, exception handler.
Flag: missing entry condition, missing exit condition, missing exception handler,
unreachable terminal state.

flow-conversation
Walk the multi-turn agent conversation graph for {{topic}}.
For each node: list outbound paths.
Flag: dead ends (no valid exit), loops (node revisited without progress),
missing handoff definitions (agent passes control to undefined destination).

trace-state
Hand-compile the state machine for {{topic}}.
For each state: preconditions, transition trigger, postcondition, system invariants.
Flag: unguarded transitions (trigger with no precondition guard), dead states
(valid entry, no valid exit), invariant violations.

trace-contract
At every component boundary relevant to {{topic}}:
State what the producer promises. State what the consumer expects.
Flag any mismatch: type, cardinality, nullability, timing, ordering.
Label each mismatch with the specific components involved.

trace-permissions
Walk every RBAC role that touches {{topic}}.
For each role: list permitted actions, denied actions.
Flag: privilege escalation paths, over-broad grants, missing deny rules
on sensitive operations.

---

CONSOLIDATE

Write ONE report. Not five.

Rank all findings by blast radius — use the STEP 0 census-anchored definition.
For each blast radius assessment, name which component or shared state surface
from the census is affected. Do not restate the generic definition.

For each finding:
- [sub-skill source]
- What the finding is
- Blast radius: WIDE / MEDIUM / NARROW — [name specific component or shared state
  from STEP 0 census]
- Severity at the epicenter: HIGH / MED / LOW
- What must change to resolve it

Flag any finding corroborated by two or more sub-skills as SYSTEMIC.
Systemic findings rank above isolated findings of equal blast radius.

Spec gaps: Conditions the simulation exposed that the spec does not address.
Write "none detected" if clean.

Contract violations: Producer/consumer mismatches found during simulation.
Write "none detected" if clean.

Verdict: go / conditional-go / no-go
One sentence — name the highest-blast-radius finding (with component name from census)
or state none found.
```

---

## V-02 — Single axis: Full typed schemas, all 5 sub-skills (C-12 target)

**Hypothesis:** Providing vocabulary-appropriate column schemas for ALL five sub-skills
forces each sub-skill's findings into columns that match its specific signal type.
R1 V-04 used typed schemas for 4 of 5 sub-skills (flow-conversation used a generic
template). Full coverage prevents any sub-skill from falling back to mismatched columns
and satisfies C-12 at maximum degree.

```
You are running the campaign-behavior simulation for: {{topic}}

Run five sub-skills in trace-first sequence. This order is intentional: structural
contracts are verified before behavioral flows are walked, so lifecycle and conversation
simulation have a defined contract baseline to check against.

Execution sequence:
1. trace-contract
2. trace-permissions
3. trace-state
4. flow-lifecycle
5. flow-conversation

Mark "none detected" explicitly when a sub-skill finds no issues.
Do not skip any section.

---

### 1. trace-contract

Compare expected vs actual at every component boundary for {{topic}}.

| ID | Producer | Consumer | Expected | Actual | Mismatch-type | Severity |
|----|----------|----------|----------|--------|---------------|----------|

Mismatch types: SCHEMA / NULLABILITY / CARDINALITY / ORDERING / TIMING
If clean: one row — "no contract violations detected".

---

### 2. trace-permissions

Walk every RBAC role for {{topic}}.

| ID | Role | Permitted actions | Denied actions | Escalation path? | Over-broad grant? | Flag |
|----|------|-------------------|----------------|------------------|-------------------|------|

If clean: one row — "no permission issues detected".

---

### 3. trace-state

Hand-compile the state machine for {{topic}}.

| ID | State | Preconditions | Trigger | Postcondition | Invariants | Flag |
|----|-------|---------------|---------|---------------|------------|------|

Flags: UNGUARDED (trigger with no precondition guard) / DEAD (no valid exit) /
INVARIANT-VIOLATION (postcondition contradicts a system invariant)
If clean: one row — "no state issues detected".

---

### 4. flow-lifecycle

Simulate the full business lifecycle for {{topic}}.

| ID | Phase | Entry-condition | Exit-condition | Exception-handler | Flag |
|----|-------|----------------|----------------|-------------------|------|

Flags: NO-ENTRY / NO-EXIT / NO-HANDLER / UNREACHABLE
If clean: one row — "no lifecycle issues detected".

---

### 5. flow-conversation

Walk the agent conversation graph for {{topic}}.

| ID | Node | Outbound-paths | Dead-end? | Loop? | Handoff-defined? | Flag |
|----|------|----------------|-----------|-------|------------------|------|

If clean: one row — "no conversation issues detected".

---

### Campaign Summary

| Metric | Value |
|--------|-------|
| Sub-skills run | 5 of 5 |
| Total findings | N |
| Spec gaps | N |
| Contract violations | N |
| Cross-skill findings | N |
| Readiness verdict | go / conditional-go / no-go |

---

### Ranked Findings (blast radius order, highest first)

Blast radius = how broadly a failure propagates. A finding that corrupts shared state
or breaks a contract consumed by multiple callers has wider blast radius than one
contained to a single isolated path.

| Rank | ID | Sub-skill | Finding | Blast-radius | Severity | Remediation |
|------|----|-----------|---------|--------------|----------|-------------|

Blast-radius: WIDE / MEDIUM / NARROW
Severity: HIGH / MED / LOW (at the failure epicenter, independent of propagation scope)
These are distinct dimensions — a finding can be low-severity but wide-blast.

---

### Spec Gaps

Conditions the simulation exposed that the spec does not address.
Write "none detected" if the spec covered every case.

---

### Contract Violations

Mismatches between component promises. Write "none detected" if clean.

---

### Cross-skill Findings

Findings that appeared in two or more sub-skills — label each SYSTEMIC and name
the contributing sub-skills. Systemic findings rank above isolated findings of
equal blast radius.
Write "none" if no overlap.

---

### Implementation Readiness Verdict

**Verdict:** go / conditional-go / no-go
**Rationale:** [one sentence — cite the highest-blast-radius finding or state none found]
```

---

## V-03 — Single axis: Post-execution blast radius calibration (C-11 alternative)

**Hypothesis:** Rather than an upfront census that predicts system topology, a mandatory
CALIBRATION BLOCK placed after all sub-skills — but before synthesis — forces the model
to identify which shared state and boundaries the *actual findings* touched. Post-hoc
calibration is evidence-based: the model grounds blast radius in findings that exist,
not in components that might matter.

```
Run campaign-behavior for: {{topic}}

Five sub-skills. Phase gates ensure completeness. After all phases complete, a
calibration block derives system-specific blast radius definitions before ranking.

---

PHASE 1 — ENTER: flow-lifecycle

Walk the full business lifecycle of {{topic}} from creation to all terminal states.
Include every exception path.

For each phase transition: entry condition, exit condition, exception handler.
Flag: missing entry conditions, missing exit conditions, missing exception handlers,
unreachable terminal states.

EXIT CRITERIA: Every phase transition accounted for. Every exception path handled
or flagged. Write "phase 1 complete — [N findings / clean]".

---

PHASE 2 — ENTER: flow-conversation

Walk the multi-turn agent conversation graph for {{topic}}.
Map every node and its outbound edges.
Flag: dead ends (node with no valid outbound path), loops (node revisited without
forward progress), missing handoff definitions.

EXIT CRITERIA: Full graph traversal complete. Write "phase 2 complete — [N findings / clean]".

---

PHASE 3 — ENTER: trace-state

Hand-compile the state machine for {{topic}}.
For each state: preconditions, transition trigger, postcondition, system invariants.
Flag: unguarded transitions, dead states, invariant violations.

EXIT CRITERIA: Every reachable state traced. Write "phase 3 complete — [N findings / clean]".

---

PHASE 4 — ENTER: trace-contract

At every component boundary: state what the producer promises and what the consumer
expects. Compare. Flag every mismatch by type (schema, nullability, ordering,
cardinality, timing).

EXIT CRITERIA: Every boundary crossed. Write "phase 4 complete — [N findings / clean]".

---

PHASE 5 — ENTER: trace-permissions

Walk every RBAC role that touches {{topic}}. For each role: permitted actions,
denied actions. Flag: privilege escalation paths, over-broad grants, missing deny
rules on sensitive operations.

EXIT CRITERIA: Every role walked. Write "phase 5 complete — [N findings / clean]".

---

CALIBRATION BLOCK — complete this before ranking (do not skip)

Based on the findings from all five phases, identify the following for {{topic}}:

1. Shared state surfaces — what state did multiple findings touch?
   Name each resource (e.g., event stream X, table Y, cache Z).
2. High-fan-out boundaries — which component boundaries appeared in the most findings?
   Which contracts are consumed by more than one caller?
3. User-visible surfaces — which findings, if real defects, would surface to end users?

Now define blast radius for THIS campaign using the above:
- WIDE = a defect affecting [name the shared state or boundary from item 1 or 2 above],
  propagating to [N downstream callers or user-visible surface from item 3]
- MEDIUM = breaks one contract boundary with limited downstream propagation
- NARROW = contained to one isolated path, no shared-state writes, no visible surface impact

Use these calibrated definitions in the ranked findings. Name the specific shared state
or boundary when assigning blast radius. Do not revert to generic language.

---

CONSOLIDATE

Write ONE report. Synthesize across all five phases.

Rank all findings by blast radius (wide first) using the calibrated definitions above.

For each finding:
- [phase/sub-skill source]
- What the finding is
- Blast radius: WIDE / MEDIUM / NARROW — name the specific shared state or boundary
  from the calibration block
- Severity at the epicenter: HIGH / MED / LOW
- What must change to resolve it

Identify any finding that appeared in two or more phases. Call it SYSTEMIC.
Systemic findings rank above isolated findings of equal blast radius.

SPEC GAPS: List every condition exposed by simulation that the spec does not cover.
Write "none detected" if clean.

CONTRACT VIOLATIONS: List every producer/consumer mismatch.
Write "none detected" if clean.

VERDICT: go / conditional-go / no-go
One sentence — name the highest-blast-radius finding (with calibrated component
or state name) or state none found.
```

---

## V-04 — Combination: System topology census + Full typed schemas (C-11 + C-12)

**Hypothesis:** Combining the pre-execution topology census (V-01 axis) with
vocabulary-appropriate typed schemas for all five sub-skills (V-02 axis) ensures
two things simultaneously: blast radius is anchored to named system components before
any finding is generated, and per-sub-skill findings are captured in columns that match
the specific signal type of each sub-skill.

```
You are running the campaign-behavior simulation for: {{topic}}

STEP 0 — TOPOLOGY CENSUS (required before any sub-skill runs)

Enumerate the architecture of {{topic}}:

Components: [list every distinct service, store, agent, queue, or API involved]

Shared state surfaces: [list every resource two or more components read or write —
tables, streams, caches, config flags]

Downstream callers: [list every component or user path that depends on
{{topic}} being correct]

User-visible surfaces: [list observable outputs where a defect would be visible —
API responses, UI states, notifications, events]

Contract boundaries: [list every producer/consumer interface boundary]

BLAST RADIUS ANCHOR — derived from the census:
WIDE = affects a shared state surface or a contract boundary with N>1 callers from above.
NARROW = contained to one component with no shared-state writes, no downstream callers.
Name components and state surfaces from the census when stating blast radius.
Do not use generic language.

---

Run five sub-skills in trace-first sequence.

Execution sequence:
1. trace-contract
2. trace-permissions
3. trace-state
4. flow-lifecycle
5. flow-conversation

Mark "none detected" explicitly when a sub-skill produces no findings.

---

### 1. trace-contract

| ID | Producer | Consumer | Expected | Actual | Mismatch-type | Severity |
|----|----------|----------|----------|--------|---------------|----------|

Mismatch types: SCHEMA / NULLABILITY / CARDINALITY / ORDERING / TIMING
If clean: "no contract violations detected".

---

### 2. trace-permissions

| ID | Role | Permitted actions | Denied actions | Escalation path | Over-broad grant? | Flag |
|----|------|-------------------|----------------|-----------------|-------------------|------|

If clean: "no permission issues detected".

---

### 3. trace-state

| ID | State | Preconditions | Trigger | Postcondition | Invariants | Flag |
|----|-------|---------------|---------|---------------|------------|------|

Flags: UNGUARDED / DEAD / INVARIANT-VIOLATION
If clean: "no state issues detected".

---

### 4. flow-lifecycle

| ID | Phase | Entry-condition | Exit-condition | Exception-handler | Flag |
|----|-------|----------------|----------------|-------------------|------|

Flags: NO-ENTRY / NO-EXIT / NO-HANDLER / UNREACHABLE
If clean: "no lifecycle issues detected".

---

### 5. flow-conversation

| ID | Node | Outbound-paths | Dead-end? | Loop? | Handoff-defined? | Flag |
|----|------|----------------|-----------|-------|------------------|------|

If clean: "no conversation issues detected".

---

### Campaign Summary

| Metric | Value |
|--------|-------|
| Sub-skills run | 5 of 5 |
| Total findings | N |
| Spec gaps | N |
| Contract violations | N |
| Cross-skill findings | N |

---

### Ranked Findings (blast radius order)

Use the STEP 0 census-anchored definition. Name specific components and shared
state surfaces from the census when assigning blast radius — not generic terms.

| Rank | ID | Sub-skill | Finding | Blast-radius | Severity | Remediation |
|------|----|-----------|---------|--------------|----------|-------------|

Blast-radius: WIDE / MEDIUM / NARROW + [component or state surface from census]
Severity: HIGH / MED / LOW — intensity at the failure epicenter, independent of scope
These are orthogonal dimensions — co-locate both on every finding row.

---

### Spec Gaps

Conditions the simulation exposed that the spec does not address.
Write "none detected" if clean.

---

### Contract Violations

Mismatches between component promises. Write "none detected" if clean.

---

### Cross-skill Findings

Findings corroborated by two or more sub-skills — label each SYSTEMIC and name
the contributing sub-skills. Systemic findings rank above isolated findings of
equal blast radius.
Write "none" if no overlap.

---

### Implementation Readiness Verdict

**Verdict:** go / conditional-go / no-go
**Rationale:** [one sentence — cite the highest-blast-radius finding by component name
from census, or state none found]
```

---

## V-05 — Combination: Topology census + Typed schemas + Phase gates + Co-located severity/blast-radius

**Hypothesis:** Combining all four structural innovations — system topology census for
C-11 grounding, typed schemas for C-12 coverage, phase gates for C-01 completeness,
and explicit co-location of severity and blast radius for C-13 — produces a prompt
that structurally enforces all 13 rubric criteria without relying on the model to
infer any of them.

```
Run campaign-behavior for: {{topic}}

---

STEP 0 — TOPOLOGY CENSUS (complete before any sub-skill runs)

Map the system structure of {{topic}}:

1. Components — list every service, store, agent, queue, or API
2. Shared state surfaces — list every resource with multiple readers or writers
3. Downstream callers — list every component or path that depends on {{topic}}
4. User-visible surfaces — list observable outputs (API, UI, events, notifications)
5. Contract boundaries — list every producer/consumer interface

BLAST RADIUS DEFINITION FOR THIS CAMPAIGN:
- WIDE: a defect affecting a shared state surface [item 2] or a boundary with
  N>1 callers [item 3], potentially cascading to a user-visible surface [item 4]
- MEDIUM: a defect breaking one contract boundary [item 5] with limited downstream
  propagation
- NARROW: a defect confined to one component [item 1] with no shared-state writes

Use component names and state surface names from this census in all blast radius
assessments. Do not use generic language in the ranked findings.

---

PHASE 1 — ENTER: trace-contract

At every contract boundary [item 5 from census]: compare producer promise vs
consumer expectation. Flag every mismatch.

| ID | Producer | Consumer | Expected | Actual | Mismatch-type | Severity |
|----|----------|----------|----------|--------|---------------|----------|

Mismatch types: SCHEMA / NULLABILITY / CARDINALITY / ORDERING / TIMING
If clean: "no contract violations — phase 1 clean".

EXIT CRITERIA: Every boundary from the census crossed. Write "phase 1 complete".

---

PHASE 2 — ENTER: trace-permissions

Walk every RBAC role that touches {{topic}}.

| ID | Role | Permitted | Denied | Escalation path | Over-broad grant? | Flag |
|----|------|-----------|--------|-----------------|-------------------|------|

If clean: "no permission issues — phase 2 clean".

EXIT CRITERIA: Every role walked. Write "phase 2 complete".

---

PHASE 3 — ENTER: trace-state

Hand-compile the state machine for {{topic}}.

| ID | State | Preconditions | Trigger | Postcondition | Invariants | Flag |
|----|-------|---------------|---------|---------------|------------|------|

Flags: UNGUARDED / DEAD / INVARIANT-VIOLATION
If clean: "no state issues — phase 3 clean".

EXIT CRITERIA: Every reachable state traced. Write "phase 3 complete".

---

PHASE 4 — ENTER: flow-lifecycle

Simulate the full business lifecycle for {{topic}}.

| ID | Phase | Entry-condition | Exit-condition | Exception-handler | Flag |
|----|-------|----------------|----------------|-------------------|------|

Flags: NO-ENTRY / NO-EXIT / NO-HANDLER / UNREACHABLE
If clean: "no lifecycle issues — phase 4 clean".

EXIT CRITERIA: Every phase transition and exception path accounted for.
Write "phase 4 complete".

---

PHASE 5 — ENTER: flow-conversation

Walk the agent conversation graph for {{topic}}.

| ID | Node | Outbound-paths | Dead-end? | Loop? | Handoff-defined? | Flag |
|----|------|----------------|-----------|-------|------------------|------|

If clean: "no conversation issues — phase 5 clean".

EXIT CRITERIA: Full graph traversal complete. Write "phase 5 complete".

---

CONSOLIDATE — do not skip this step

Write ONE report. Synthesize across all five phases.

Rank all findings by blast radius using the STEP 0 definition.
Name the specific component or shared state surface from the census when stating
blast radius. Each finding row must carry BOTH blast radius AND severity as
distinct, non-merged fields.

| Rank | ID | Phase | Finding | Blast-radius | Severity | Remediation |
|------|----|-------|---------|--------------|----------|-------------|

Blast-radius: WIDE / MEDIUM / NARROW + [name component or state surface from census]
Severity: HIGH / MED / LOW — intensity at the failure epicenter, not propagation scope
These are orthogonal. Do not merge them into a single "impact" field.

Identify findings appearing in two or more phases. Label SYSTEMIC.
Systemic findings rank above isolated findings of equal blast radius.

SPEC GAPS: Conditions the simulation exposed that the spec does not address.
Write "none detected" if clean.

CONTRACT VIOLATIONS: Producer/consumer mismatches. Write "none detected" if clean.

CROSS-SKILL FINDINGS:

| Finding | Contributing phases | Label |
|---------|--------------------|----|

Write "none" if no multi-phase overlap.

VERDICT: go / conditional-go / no-go
One sentence — name the highest-blast-radius finding by component name from census,
or state no blocking findings were detected.
```
