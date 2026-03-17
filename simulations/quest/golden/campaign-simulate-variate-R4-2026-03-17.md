---
skill: campaign-simulate
round: 4
date: 2026-03-17
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-simulate-rubric-v3-2026-03-17.md
---

# campaign-simulate -- Round 4 Variations

Round 3 V-05 achieves 100/100 on rubric v3. Round 4 explores three new axes that have not
been tested in any prior round. The goal is to surface excellence patterns that could warrant
a rubric v4 upgrade, and to test whether the same structural compliance can be reached by
different mechanisms.

**New axes this round:**

- **Axis A: Topic Entity Manifest** -- Before any sub-skill fires, the topic is decomposed into
  five typed entity lists (one per sub-skill). Each sub-skill receives its pre-extracted
  traversal targets instead of re-reading the raw topic. Converts sub-skill setup from
  "infer what to trace" to "trace these specific entities."
- **Axis B: Finding Type Pre-Assignment** -- Like C-14 pre-assigns System Boundary vocabulary,
  declare a fixed Type vocabulary map per sub-skill before execution. Type classification
  becomes a copy operation from a named set, not a model judgment call.
- **Axis C: Remediation Template Contract** -- Every Remediation cell must follow the
  three-field template: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`. Free-text remediation
  produces vague entries; the template enforces actionability by construction.

**Variation axes this round:**

Single-axis: V-01 (entity manifest), V-02 (type pre-assignment), V-03 (remediation template).
Combined: V-04 (entity manifest + type pre-assignment), V-05 (entity manifest + type
pre-assignment + remediation template, carrying full R3 V-05 architecture forward).

---

## V-01 -- Topic Entity Manifest Axis

**Variation axis:** Role sequence / lifecycle emphasis -- before any sub-skill fires, the
campaign produces a Topic Entity Manifest that decomposes the topic into five typed entity
lists. Each sub-skill reads its own entity list rather than re-interpreting the raw topic
spec. The entity list is the traversal target; the sub-skill walks the list, not the prose.

**Hypothesis:** Re-reading a spec five times at sub-skill setup introduces interpretation
variance: each sub-skill may model different states, different contract surfaces, or different
role sets from the same prose. Pre-extracting entities in one pass eliminates this variance.
A trace-state sub-skill that walks a pre-enumerated state list covers every state; one that
infers the state machine may miss implicit states. C-01 compliance (all five sub-skills
execute on distinct findings) improves when each sub-skill has an explicit, non-overlapping
entity scope. A new excellence pattern emerges: entity manifest completeness as a pre-execution
quality gate, verifiable before a single sub-skill runs.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Before any sub-skill executes, produce
a Topic Entity Manifest that extracts the traversal targets for each sub-skill. Sub-skills
receive their entity list and walk it -- they do not re-derive scope from the raw topic.

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. Each list is the complete traversal scope
for its owning sub-skill.

**Entity List 1 -- trace-state targets**

List every distinct state the system can be in. For each state: name it and note whether
it is an entry state, interior state, exit state, or error state.

| State Name | Type (entry / interior / exit / error) | Description |
|------------|---------------------------------------|-------------|
|            |                                       |             |

**Entity List 2 -- trace-contract targets**

List every contract boundary: the interfaces where a caller passes control or data to a
callee. For each boundary: name the interface, the caller, and the callee.

| Boundary Name | Caller | Callee |
|---------------|--------|--------|
|               |        |        |

**Entity List 3 -- trace-permissions targets**

List every role in the RBAC model. For each role: name it and list the actions it is
expected to be able to perform per the spec.

| Role | Expected Actions |
|------|-----------------|
|      |                  |

**Entity List 4 -- flow-lifecycle targets**

List every lifecycle phase. For each phase: name it, name its entry condition, and name
its exit condition.

| Phase | Entry Condition | Exit Condition |
|-------|----------------|---------------|
|       |                |               |

**Entity List 5 -- flow-conversation targets**

List every conversation entry point: the distinct user intents or system events that start
a conversation path. For each entry point: name it and note whether it is a primary or
edge path.

| Entry Point | Path Type (primary / edge) |
|-------------|---------------------------|
|             |                           |

**Manifest completeness gate**: Before sub-skills run, verify that no entity list is empty.
An empty list means the topic spec is underspecified for that sub-skill -- flag it and either
supplement from inference or record as a pre-simulation spec gap.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1)
2. trace-contract      (walks Entity List 2)
3. trace-permissions   (walks Entity List 3)
4. flow-lifecycle      (walks Entity List 4)
5. flow-conversation   (walks Entity List 5)

---

**SUB-SKILL 1: trace-state**

Walk Entity List 1. For each state: write every transition in and out of it, write its
precondition and postcondition, and find:

- States with no exit transition (caller enters, cannot proceed)
- Transitions that can fire before their precondition is met
- Invariants named in the spec that are not enforced at the state boundary
- States that are in the list but unreachable from the initial state

For each finding:

```
F-ID:          [F-01, F-02, ...]
Sub-skill:     trace-state
Type:          state-anomaly
System Boundary: state machine
Spec location: [specific section or state name from Entity List 1]
Summary:       [one sentence naming the specific state or transition]
Severity:      [CRITICAL / HIGH / MEDIUM / LOW]
Blast radius:  [system-wide / cross-skill / component-wide / isolated]
Remediation:   [specific action at a named location]
Trace Link:    N/A -- trace sub-skill
```

---

**SUB-SKILL 2: trace-contract**

Walk Entity List 2. For each boundary: state the caller's expectation of what the callee
returns, state what the callee actually returns per the spec, and flag any mismatch.

Look especially for: undocumented edge case behaviors, implicit assumptions not stated in
the spec, and boundaries where the caller and callee use different success definitions.

For each finding: [same schema, sub-skill = trace-contract, type = contract-violation or
spec-gap, System Boundary = "contract surface"]

---

**SUB-SKILL 3: trace-permissions**

Walk Entity List 3. For each role, trace the full permission path: what the spec says the
role can do, what the spec says it cannot do, and whether those boundaries are enforced.
Find:

- Privilege escalation routes (a role reaches a resource it should not via an unguarded path)
- Missing denials (an action attempted by a role the spec does not address)
- Cross-role conflicts enabling race conditions or data leaks

For each finding: [same schema, sub-skill = trace-permissions, type = permission-gap,
System Boundary = "permission check"]

---

**SUB-SKILL 4: flow-lifecycle**

Walk Entity List 4. For each phase: verify the entry condition is specified, the exit
condition is specified, and the exception path from the phase is specified. Find:

- Phases with no recovery path if the exit condition is not met
- Transitions between phases that have no defined precondition in the spec
- Terminal states that can be reached without being declared as terminal

For each finding: [same schema, sub-skill = flow-lifecycle, type = lifecycle-gap or
flow-gap, System Boundary = "lifecycle phase", Trace Link = F-ID of any related trace
finding or "none"]

---

**SUB-SKILL 5: flow-conversation**

Walk Entity List 5. For each entry point, simulate the conversation path through the graph.
Find:

- Dead ends: a state with no valid next action
- Loops: a path that returns to a prior state without resolution
- Ambiguous transitions: the spec does not define the next state given the current state and input

For each finding: [same schema, sub-skill = flow-conversation, System Boundary =
"conversation state", Trace Link populated or "none"]

---

**UNIFIED FINDINGS REPORT**

Collect all findings from all five sub-skills. Rank by blast radius (system-wide first),
then severity within each tier. Assign final sequential F-IDs if resequencing occurred.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|
|      |      |           |                |      |              |         |          |             |           |             |

For all system-wide and cross-skill findings: add blast radius rationale naming the
downstream flows, components, or contracts affected.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Entity List Rows Used |
|-----------|--------|-------------|----------------------|
| trace-state | executed / no findings | | |
| trace-contract | executed / no findings | | |
| trace-permissions | executed / no findings | | |
| flow-lifecycle | executed / no findings | | |
| flow-conversation | executed / no findings | | |

---

**TEST SCENARIO BASELINE**

For each CRITICAL or HIGH finding, derive a named test scenario:

| Scenario | F-ID | What to Exercise | Acceptance Condition |
|----------|------|-----------------|---------------------|
|          |      |                 |                     |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Topic Entity Manifest > Manifest Completeness Gate > per-sub-skill
execution (each walking its entity list) > Unified Findings Report (ranked) > Execution Log
(with entity list row counts) > Test Scenario Baseline.

---

## V-02 -- Finding Type Pre-Assignment Axis

**Variation axis:** Output format -- the Type column vocabulary is pre-assigned per sub-skill
before any sub-skill runs. The prompt declares a fixed type map. Type classification is a
copy operation from a named set, not a model judgment call. This is the parallel of C-14's
System Boundary vocabulary pre-assignment applied to the Type column.

**Hypothesis:** C-14 closed the system-boundary judgment gap by making boundary labels a
mechanical copy from a five-label vocabulary. The Type column has the same vulnerability:
free-text type labels allow inconsistent or meaningless values ("issue", "problem", "gap")
that obscure finding categorization. Pre-assigning a type vocabulary per sub-skill makes
type classification verifiable: a finding from trace-permissions must have one of the
permission-type labels. This closes an analogous gap to C-14 and could surface a new
criterion C-19 in a future rubric. The risk: a narrow type vocabulary may not capture a
genuine finding -- the prompt must allow "spec-gap" as a cross-cutting escape type.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute all five sub-skills in order.
Before any sub-skill runs, the Type vocabulary map below is in effect. Every finding uses
exactly one type value from its sub-skill's assigned list. A type value not in the
sub-skill's list is a finding error.

---

**TYPE VOCABULARY MAP**

This map is pre-assigned. Do not invent new type labels.

| Sub-Skill | Allowed Type Values |
|-----------|---------------------|
| trace-state | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

**Cross-cutting rule**: `spec-gap` is available to all sub-skills as an escape hatch for
findings that do not fit any other type in the sub-skill's list. When `spec-gap` is used,
the Summary must explain what is underspecified and why no more specific type applies.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**EXECUTION SEQUENCE**

1. flow-lifecycle
2. flow-conversation
3. trace-state
4. trace-contract
5. trace-permissions

---

**SUB-SKILL 1: flow-lifecycle**

Trace the business process lifecycle for {{topic}}. Walk every phase, every transition,
every exception path. Find missing exit states, undefined phase contracts, exception
recovery gaps, undeclared terminal states.

For each finding:

```
F-ID:            [F-01, F-02, ...]
Sub-skill:       flow-lifecycle
Type:            [choose from: lifecycle-gap / missing-exit-state / undefined-phase-contract / recovery-gap / spec-gap]
System Boundary: lifecycle phase
Spec location:   [specific section or phase name]
Summary:         [one sentence naming the specific phase or transition]
Severity:        [CRITICAL / HIGH / MEDIUM / LOW]
Blast radius:    [system-wide / cross-skill / component-wide / isolated]
Trace Link:      N/A -- pre-trace execution
Remediation:     [specific action at a named location]
```

---

**SUB-SKILL 2: flow-conversation**

Simulate the multi-turn conversation graph for {{topic}}. Walk major and edge paths.
Find dead ends, loops, ambiguous transitions.

For each finding:

```
F-ID:            [continues from above]
Sub-skill:       flow-conversation
Type:            [choose from: dead-end / loop-risk / ambiguous-transition / spec-gap]
System Boundary: conversation state
[remaining fields same schema]
```

---

**SUB-SKILL 3: trace-state**

Hand-compile the state machine for {{topic}}. Write every state, every transition, every
precondition and postcondition. Find exit-less states, early-firing transitions, unenforced
invariants, and unreachable states.

For each finding:

```
F-ID:            [continues]
Sub-skill:       trace-state
Type:            [choose from: state-anomaly / unreachable-state / invariant-violation / transition-guard-missing / spec-gap]
System Boundary: state machine
[remaining fields same schema]
```

---

**SUB-SKILL 4: trace-contract**

Identify the three most important contract boundaries for {{topic}}. For each: state caller
expectation, callee behavior per spec, and any divergence. Find undocumented edge case
behaviors at interfaces.

For each finding:

```
F-ID:            [continues]
Sub-skill:       trace-contract
Type:            [choose from: contract-violation / undocumented-behavior / caller-callee-mismatch / spec-gap]
System Boundary: contract surface
[remaining fields same schema]
```

---

**SUB-SKILL 5: trace-permissions**

Walk the RBAC model. Trace each role through the permission path. Find privilege escalation
routes, missing denials, and cross-role conflicts.

For each finding:

```
F-ID:            [continues]
Sub-skill:       trace-permissions
Type:            [choose from: privilege-escalation / missing-denial / cross-role-conflict / spec-gap]
System Boundary: permission check
[remaining fields same schema]
```

---

**TYPE VOCABULARY VERIFICATION**

Before synthesis, verify every finding's Type value is in its sub-skill's allowed list.

| Sub-Skill | Finding IDs | Type Values Used | All in Vocabulary? |
|-----------|-------------|-----------------|-------------------|
| flow-lifecycle | | | YES / NO |
| flow-conversation | | | YES / NO |
| trace-state | | | YES / NO |
| trace-contract | | | YES / NO |
| trace-permissions | | | YES / NO |

If any sub-skill shows NO: identify the non-conforming findings and either reclassify using
an allowed type or reclassify as `spec-gap` with explanation in Summary.

---

**UNIFIED FINDINGS REPORT**

Collect all findings. Rank by blast radius (system-wide first) then severity within tier.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|
|      |      |           |                |      |              |         |          |             |           |             |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Type Values Used |
|-----------|--------|-------------|-----------------|
| flow-lifecycle | executed / no findings | | |
| flow-conversation | executed / no findings | | |
| trace-state | executed / no findings | | |
| trace-contract | executed / no findings | | |
| trace-permissions | executed / no findings | | |

---

**TEST SCENARIO BASELINE**

| Scenario | F-ID | Type | What to Exercise | Acceptance Condition |
|----------|------|------|-----------------|---------------------|
|          |      |      |                 |                     |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Type Vocabulary Map (header) > per-sub-skill execution (each
citing type values from the map) > Type Vocabulary Verification > Unified Findings Report
(ranked) > Execution Log > Test Scenario Baseline.

---

## V-03 -- Remediation Template Contract Axis

**Variation axis:** Phrasing register / output format -- every Remediation cell must follow
a three-field template: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`. Free-text remediation
fields produce vague entries that tell the reader what is wrong without telling them what
to do. The template enforces three-field specificity and makes vague remediations structurally
visible as template violations. The pre-output verification gate (C-17) explicitly includes
a remediation template compliance check.

**Hypothesis:** The most common failure mode in remediation fields is incomplete specificity:
entries like "fix the spec", "clarify the contract", "add documentation" name a domain but
not an action. These pass a no-blank-cell check but fail a usefulness check -- a developer
reading the finding cannot act without further investigation. A mandatory template converts
the remediation field from a comment into an actionable work item. The template also
surfaces spec gaps: if a finding's remediation cannot be templated (no target, no location,
no spec), the finding is not yet actionable and must be flagged as a research item. The
risk is over-rigid templates that produce awkward phrasings -- the verb list below should
allow escape for findings that genuinely require investigation rather than a spec change.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Execute all five sub-skills in order.
Every finding's Remediation field must follow the template below. A remediation entry that
does not fit the template is a finding error, not a format preference.

---

**REMEDIATION TEMPLATE**

Every Remediation cell must be one of:

1. **Action template**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
   - VERB: Add / Remove / Change / Enforce / Specify / Split / Merge / Guard / Document
   - TARGET: the specific thing being acted on (a field, transition, role check, phase boundary)
   - AT: the specific location (spec section number, interface name, state name, code boundary)
   - TO: the specification of what it should be after the action

   *Example*: `Add postcondition check AT Signal.submit() boundary TO enforce that status == "pending"
   before state transitions as specified in section 3.2.1`

2. **Research item template (for findings not yet actionable)**:
   `INVESTIGATE [specific question] BEFORE specifying remediation`

   *Example*: `INVESTIGATE whether concurrent submission is intended behavior BEFORE
   specifying remediation for the missing lock guard`

A remediation of "fix the spec", "clarify", "add validation", or any entry without a named
target and location = template violation.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**EXECUTION SEQUENCE**

1. flow-lifecycle
2. flow-conversation
3. trace-state
4. trace-contract
5. trace-permissions

---

**SUB-SKILL 1: flow-lifecycle**

Trace the business process lifecycle for {{topic}}. Walk every phase, every transition,
every exception path. Find missing exit states, undefined phase contracts, exception recovery
gaps.

For each finding:

```
F-ID:            [F-01, F-02, ...]
Sub-skill:       flow-lifecycle
Type:            [spec-gap / lifecycle-gap / flow-gap / contract-violation]
System Boundary: lifecycle phase
Spec location:   [specific section or phase name -- not "the spec"]
Summary:         [one sentence]
Severity:        [CRITICAL / HIGH / MEDIUM / LOW]
Blast radius:    [system-wide / cross-skill / component-wide / isolated]
Trace Link:      N/A -- pre-trace execution
Remediation:     [VERB TARGET AT LOCATION TO SPEC] or [INVESTIGATE question BEFORE specifying]
```

---

**SUB-SKILL 2: flow-conversation**

Simulate the multi-turn conversation graph for {{topic}}. Walk major and edge paths.
Find dead ends, loops, ambiguous transitions.

For each finding: [same schema, sub-skill = flow-conversation, System Boundary = "conversation state"]

---

**SUB-SKILL 3: trace-state**

Hand-compile the state machine for {{topic}}. Write every state, transition, precondition,
and postcondition. Find exit-less states, early-firing transitions, unenforced invariants,
unreachable states.

For each finding: [same schema, sub-skill = trace-state, System Boundary = "state machine"]

---

**SUB-SKILL 4: trace-contract**

Identify the three most important contract boundaries for {{topic}}. State caller expectation,
callee behavior per spec, and any divergence. Find undocumented edge case behaviors.

For each finding: [same schema, sub-skill = trace-contract, System Boundary = "contract surface"]

---

**SUB-SKILL 5: trace-permissions**

Walk the RBAC model. Trace each role through the permission path. Find privilege escalation
routes, missing denials, and cross-role conflicts.

For each finding: [same schema, sub-skill = trace-permissions, System Boundary = "permission check"]

---

**REMEDIATION TEMPLATE VERIFICATION**

Before writing the unified report, verify every Remediation cell against the template.

| F-ID | Remediation Summary | Template Form | Conformant? |
|------|---------------------|--------------|-------------|
|      |                     | action / research / VIOLATION | YES / NO |

If any finding shows VIOLATION: correct the remediation before proceeding. A report with
template violations in the verification table = gate not passed.

---

**UNIFIED FINDINGS REPORT**

Collect all findings. Rank by blast radius (system-wide first) then severity within tier.

| Rank | F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|
|      |      |           |                |      |              |         |          |             |           |             |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Research Items |
|-----------|--------|-------------|----------------|
| flow-lifecycle | executed / no findings | | |
| flow-conversation | executed / no findings | | |
| trace-state | executed / no findings | | |
| trace-contract | executed / no findings | | |
| trace-permissions | executed / no findings | | |

---

**TEST SCENARIO BASELINE**

| Scenario | F-ID | Remediation Form | What to Exercise |
|----------|------|-----------------|-----------------|
|          |      | action / research | |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Remediation Template (header) > per-sub-skill execution (each
with templated remediations) > Remediation Template Verification (gate must pass) > Unified
Findings Report (ranked) > Execution Log > Test Scenario Baseline.

---

## V-04 -- Combined (Entity Manifest + Type Pre-Assignment)

**Variation axes combined:**
1. Output format / lifecycle emphasis -- Topic Entity Manifest decomposes the topic into
   five typed entity lists before sub-skills run (V-01 axis)
2. Output format -- Type vocabulary pre-assigned per sub-skill; classification is a
   copy operation from a named set (V-02 axis)

**Hypothesis:** The combination closes two judgment gaps simultaneously. The entity manifest
eliminates interpretation variance at sub-skill setup: each sub-skill knows exactly what
entities to traverse. The type pre-assignment eliminates classification variance at finding
output: each sub-skill knows exactly which type labels are valid. Together they constrain
the two highest-variance operations in the simulation (what to examine, how to label the
result) to mechanical operations. When both are active, the model spends its attention on
finding substance rather than scope definition and label selection. This may surface higher-
quality findings per entity traversed. The combined prompt also makes manifest completeness
and type vocabulary verification two independent quality gates that can be checked before
synthesis, reducing the chance that a weak sub-skill run is promoted into the unified report
without detection.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Phase 0 produces the Topic Entity
Manifest and the Type Vocabulary Map -- both are in effect for all sub-skills. Sub-skills
walk their entity list and label findings using only their assigned type vocabulary.

---

**TYPE VOCABULARY MAP** (pre-assigned, in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

`spec-gap` is available to all sub-skills. System Boundary values are also fixed -- copy
from this table, do not invent alternate labels.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. Sub-skills walk these lists.

**Entity List 1 -- trace-state traversal targets**

| State Name | Type (entry / interior / exit / error) | Precondition (brief) | Postcondition (brief) |
|------------|---------------------------------------|---------------------|----------------------|
|            |                                       |                     |                      |

**Entity List 2 -- trace-contract traversal targets**

| Boundary Name | Caller | Callee | Caller Expectation (brief) |
|---------------|--------|--------|---------------------------|
|               |        |        |                           |

**Entity List 3 -- trace-permissions traversal targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle traversal targets**

| Phase | Entry Condition | Exit Condition | Exception Path |
|-------|----------------|---------------|----------------|
|       |                |               |                |

**Entity List 5 -- flow-conversation traversal targets**

| Entry Point | Path Type | Expected Termination |
|-------------|-----------|---------------------|
|             |           |                     |

**Manifest completeness gate**: All five lists non-empty. Any empty list = spec gap,
logged as pre-simulation finding F-00 before sub-skills run.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH)
   -- PAUSE: verify severity budget gate, write Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads Trace Findings Brief)
5. flow-conversation   (walks Entity List 5; reads Trace Findings Brief)

---

**FINDINGS TABLE SCHEMA** (unified, all sub-skills)

All findings from all sub-skills enter this table incrementally.

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

No blank cells. If a field does not apply: "N/A -- [reason]".
System Boundary and Type must be copied from the Type Vocabulary Map above -- not inferred.

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify transitions, preconditions, postconditions.
Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add each finding as a row. System Boundary = "state machine". Type from list 1 vocabulary.
Trace Link = "N/A -- trace sub-skill."

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: verify caller expectation against callee spec behavior.
Find mismatches and undocumented edge case behaviors.

Add findings. System Boundary = "contract surface". Type from list 2 vocabulary.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, and cross-role conflicts.

Add findings. System Boundary = "permission check". Type from list 3 vocabulary.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run.

---

**TRACE FINDINGS BRIEF**

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius |
|------|-----------|------|---------|----------|-------------|
|      |           |      |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, and exception
path are fully specified. Find lifecycle gaps, missing exit states, undefined phase contracts.

Add findings. System Boundary = "lifecycle phase". Type from list 4 vocabulary.
Trace Link: scan the brief -- if any trace finding shares a root cause with this finding,
name it by F-ID. If none: "none."

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path. Find dead ends,
loops, ambiguous transitions.

Add findings. System Boundary = "conversation state". Type from list 5 vocabulary.
Same Trace Link requirement as flow-lifecycle.

---

**FINDINGS TABLE (complete)**

[Insert full table here. Verify: no blank cells, all System Boundary and Type values copied
from the Type Vocabulary Map, all Trace Links populated.]

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**RANKED FINDINGS**

Re-sort by blast radius (system-wide first) then severity. Add Rank column.

For all system-wide and cross-skill findings: add blast radius rationale naming affected
flows, components, or contracts.

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | | | MET / NOT MET | | |
| trace-contract | | | MET / NOT MET | | |
| trace-permissions | | | MET / NOT MET | | |
| flow-lifecycle | | | N/A | | |
| flow-conversation | | | N/A | | |

A sub-skill with no findings must add a sentinel row: Summary = "No findings detected",
Remediation = "None required -- [reason]", all other cells populated.

---

**TEST SCENARIO BASELINE**

| Scenario | F-ID | Type | Severity | What to Exercise | Acceptance Condition |
|----------|------|------|----------|-----------------|---------------------|
|          |      |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why Scope Is Wider |
|------|------------|-------|----------------------|-------------------|
|      |            |       |                      |                   |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order: Type Vocabulary Map > Severity Scale > Topic Entity Manifest >
Manifest Completeness Gate > trace sub-skill executions (each with budget status) > Severity
Budget Gate > Trace Findings Brief > flow sub-skill executions (each with trace link check) >
Findings Table (complete) > Type Vocabulary Verification > Ranked Findings > Execution Log >
Test Scenario Baseline > Cross-Skill Patterns.

---

## V-05 -- Combined (Entity Manifest + Type Pre-Assignment + Remediation Template)

**Variation axes combined:**
1. Lifecycle emphasis -- Topic Entity Manifest pre-extracts five typed entity lists (V-01 axis)
2. Output format -- Type vocabulary pre-assigned per sub-skill; copy operation (V-02 axis)
3. Phrasing register / output format -- Remediation template contract; three-field required (V-03 axis)

This variation carries the full R3 V-05 architecture forward intact (trace-first ordering,
severity budgets, unified 10-column findings table, no-blank-cell contract with N/A sentinels,
pre-assigned boundary vocabulary, universal sentinel rule, sentinel rows for clean sub-skills,
pre-output verification gate, unified schema).

**Hypothesis:** This is the maximum-structure Round 4 variant. The three new axes close the
three remaining judgment gaps that R3 V-05 left open: (1) sub-skill scope is now defined by
an entity manifest rather than re-derived from prose, (2) type classification is now a copy
operation rather than free text, (3) remediation specificity is now enforced by a named
template rather than style guidance. Combined with the full R3 V-05 architecture, every
column in every row has a mechanical compliance path: F-ID (sequential), Sub-Skill (fixed),
System Boundary (C-14 vocabulary), Type (new type vocabulary), Spec Location (named section
required), Summary (one sentence), Severity (four-value enum), Blast Radius (four-value
enum), Trace Link (F-ID or "none"), Remediation (template or research item). No column
requires model judgment -- every value can be verified as conformant or non-conformant by
inspection. This is the fully mechanical simulation campaign. The risk is that maximum
structure produces maximum compliance with minimum insight: every cell fills, every gate
passes, but the findings are thin because the model satisfied the form rather than the
substance. The severity scale definitions, the entity manifest completeness gate, and the
research-item escape in the remediation template must carry the quality floor.

---

Simulate the technical behavior of: {{topic}}

Run the full pre-implementation simulation campaign. Phase 0 produces the Topic Entity
Manifest, the Type Vocabulary Map, and the Remediation Template -- all three are in effect
for every sub-skill. Every cell in every finding row has a mechanical compliance path.

---

**SEVERITY SCALE**

- **CRITICAL**: data loss, security breach, or system unavailability if shipped
- **HIGH**: incorrect behavior, contract violation, or blocked user flow if shipped
- **MEDIUM**: degraded behavior, performance issue, or misleading output if shipped
- **LOW**: minor inconsistency, cosmetic, or documentation gap

---

**TYPE VOCABULARY MAP** (pre-assigned; in effect for all sub-skills)

| Sub-Skill | System Boundary | Allowed Type Values |
|-----------|----------------|---------------------|
| trace-state | state machine | `state-anomaly` `unreachable-state` `invariant-violation` `transition-guard-missing` `spec-gap` |
| trace-contract | contract surface | `contract-violation` `undocumented-behavior` `caller-callee-mismatch` `spec-gap` |
| trace-permissions | permission check | `privilege-escalation` `missing-denial` `cross-role-conflict` `spec-gap` |
| flow-lifecycle | lifecycle phase | `lifecycle-gap` `missing-exit-state` `undefined-phase-contract` `recovery-gap` `spec-gap` |
| flow-conversation | conversation state | `dead-end` `loop-risk` `ambiguous-transition` `spec-gap` |

System Boundary and Type must be copied from this table. Both are copy operations, not
model judgments. `spec-gap` is the escape type for any finding that does not fit the
sub-skill's specific vocabulary.

---

**REMEDIATION TEMPLATE**

Every Remediation cell must be one of:

1. **Action form**: `[VERB] [TARGET] AT [LOCATION] TO [SPEC]`
   - VERB: Add / Remove / Change / Enforce / Specify / Split / Merge / Guard / Document
   - TARGET: specific thing being acted on
   - AT: specific location (spec section, interface name, state name)
   - TO: the specification of what it should be

2. **Research form**: `INVESTIGATE [specific question] BEFORE specifying remediation`

"Fix the spec", "clarify", "add validation", or any entry without named target and location
= template violation.

---

**FINDINGS TABLE SCHEMA** (unified, 10 columns, all sub-skills)

| F-ID | Sub-Skill | System Boundary | Type | Spec Location | Summary | Severity | Blast Radius | Trace Link | Remediation |
|------|-----------|----------------|------|--------------|---------|----------|-------------|-----------|-------------|

**No-blank-cell rules:**
- Every row has all ten columns populated
- If a column does not apply: "N/A -- [reason]" -- not blank, not a dash
- System Boundary: copy from Type Vocabulary Map
- Type: copy from Type Vocabulary Map for the sub-skill
- Spec Location: specific section or boundary name -- never "the spec is unclear"
- Severity: one of the four enumerated values
- Blast Radius: system-wide / cross-skill / component-wide / isolated
- Trace Link: F-ID of related trace finding, "none", or "N/A -- trace sub-skill"
- Remediation: action form or research form per the template above

---

**PHASE 0: TOPIC ENTITY MANIFEST**

Decompose {{topic}} into five typed entity lists. These are the traversal targets for sub-skills.

**Entity List 1 -- trace-state targets**

| State Name | Type (entry / interior / exit / error) | Precondition | Postcondition |
|------------|---------------------------------------|-------------|---------------|
|            |                                       |             |               |

**Entity List 2 -- trace-contract targets**

| Boundary Name | Caller | Callee | Caller Expectation |
|---------------|--------|--------|-------------------|
|               |        |        |                   |

**Entity List 3 -- trace-permissions targets**

| Role | Permitted Actions | Denied Actions | Spec Section |
|------|------------------|----------------|-------------|
|      |                  |                |             |

**Entity List 4 -- flow-lifecycle targets**

| Phase | Entry Condition | Exit Condition | Exception Path Defined? |
|-------|----------------|---------------|------------------------|
|       |                |               |                        |

**Entity List 5 -- flow-conversation targets**

| Entry Point | Path Type (primary / edge) | Expected Termination |
|-------------|---------------------------|---------------------|
|             |                           |                     |

**Manifest completeness gate**: All five lists non-empty before any sub-skill runs. An
empty list = pre-simulation spec gap, recorded as sentinel finding F-00 in the findings
table.

---

**EXECUTION ORDER**

1. trace-state         (walks Entity List 1; severity budget: >= 1 CRITICAL or HIGH; add rows)
2. trace-contract      (walks Entity List 2; severity budget: >= 1 CRITICAL or HIGH; add rows)
3. trace-permissions   (walks Entity List 3; severity budget: >= 1 CRITICAL or HIGH; add rows)
   -- PAUSE: verify severity budget gate; write Trace Findings Brief --
4. flow-lifecycle      (walks Entity List 4; reads brief; add rows; populate Trace Link)
5. flow-conversation   (walks Entity List 5; reads brief; add rows; populate Trace Link)

---

**SUB-SKILL 1: trace-state** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 1. For each state: verify all transitions, preconditions, and postconditions.
Find: exit-less states, early-firing transitions, unenforced invariants, unreachable states.

Add each finding as a row. System Boundary = "state machine" (from map). Type from map.
Trace Link = "N/A -- trace sub-skill." Remediation in template form.

**Budget status**: [MET -- CRITICAL/HIGH F-IDs: ...] OR [NOT MET -- widened scope to: ... -- re-run findings: ...]

---

**SUB-SKILL 2: trace-contract** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 2. For each boundary: state caller expectation, callee behavior per spec,
and the divergence. Find undocumented edge case behaviors at interfaces.

Add findings. System Boundary = "contract surface". Type from map.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SUB-SKILL 3: trace-permissions** (severity budget: >= 1 CRITICAL or HIGH)

Walk Entity List 3. For each role: trace permitted and denied paths. Find escalation routes,
missing denials, and cross-role conflicts.

Add findings. System Boundary = "permission check". Type from map.

**Budget status**: [MET -- ...] OR [NOT MET -- ...]

---

**SEVERITY BUDGET GATE**

| Sub-Skill | Budget Status | CRITICAL/HIGH F-IDs |
|-----------|--------------|---------------------|
| trace-state | MET / NOT MET | |
| trace-contract | MET / NOT MET | |
| trace-permissions | MET / NOT MET | |

All three must be MET before flow sub-skills run. If any is NOT MET without rationale,
the campaign halts.

---

**TRACE FINDINGS BRIEF**

Compile all trace rows from the findings table.

| F-ID | Sub-Skill | Type | Summary | Severity | Blast Radius |
|------|-----------|------|---------|----------|-------------|
|      |           |      |         |          |             |

---

**SUB-SKILL 4: flow-lifecycle** (reads Trace Findings Brief; walks Entity List 4)

Walk Entity List 4. For each phase: verify entry condition, exit condition, and exception
path are fully specified. Find lifecycle gaps, missing exit states, undefined phase contracts,
recovery gaps.

Add findings. System Boundary = "lifecycle phase". Type from map.

For each finding's Trace Link: scan the brief -- if any trace finding shares a root cause,
same spec section, or this flow anomaly is downstream of a trace anomaly, name the trace
F-ID. If no link: "none."

At least one flow-lifecycle finding must carry a non-"none" Trace Link.

---

**SUB-SKILL 5: flow-conversation** (reads Trace Findings Brief; walks Entity List 5)

Walk Entity List 5. For each entry point: simulate the conversation path. Find dead ends,
loops, ambiguous transitions.

Add findings. System Boundary = "conversation state". Type from map.
Same Trace Link requirement: scan brief, name linked F-ID or "none."

---

**FINDINGS TABLE (complete)**

[Insert the full findings table here with all rows from all five sub-skills.]

Pre-output blank-cell verification -- check each of the following before writing:
- [ ] Zero blank cells (every cell is N/A or a value)
- [ ] All System Boundary values copied from Type Vocabulary Map
- [ ] All Type values copied from Type Vocabulary Map for their sub-skill
- [ ] All Spec Locations name a specific section or boundary
- [ ] All Trace Links populated ("none" or "N/A -- trace sub-skill" is acceptable; blank is not)
- [ ] All Severity values from the four-value enumerated set
- [ ] All Remediation entries match action form or research form template
- [ ] Sub-skills with no findings have a sentinel row (Summary = "No findings detected")

If any check fails: fill or correct before writing the table.

**Verification gate**: PASSED (all checks above clear) OR FAILED (list the failing checks).

Do not write the unified report until the verification gate shows PASSED.

---

**RANKED FINDINGS**

Re-sort the complete findings table by blast radius (system-wide first) then severity within
tier. Add Rank column at left.

For all system-wide and cross-skill findings: add blast radius rationale immediately below
naming the downstream flows, components, or contracts affected and explaining why the scope
reaches that far.

---

**TYPE VOCABULARY VERIFICATION**

| Sub-Skill | Types Used | All From Vocabulary? |
|-----------|------------|---------------------|
| trace-state | | YES / NO |
| trace-contract | | YES / NO |
| trace-permissions | | YES / NO |
| flow-lifecycle | | YES / NO |
| flow-conversation | | YES / NO |

---

**EXECUTION LOG**

| Sub-Skill | Status | Finding IDs | Budget Status | Entity List Rows | Types Used |
|-----------|--------|-------------|--------------|-----------------|------------|
| trace-state | executed / no findings | | MET / NOT MET | | |
| trace-contract | executed / no findings | | MET / NOT MET | | |
| trace-permissions | executed / no findings | | MET / NOT MET | | |
| flow-lifecycle | executed / no findings | | N/A | | |
| flow-conversation | executed / no findings | | N/A | | |

A sub-skill with "no findings" still gets a sentinel row in the findings table. Summary =
"No findings detected", Remediation = "None required -- [reason]", all other cells populated
per the no-blank-cell contract.

---

**TEST SCENARIO BASELINE**

All CRITICAL and HIGH findings produce a named test scenario. The baseline must contain at
least as many scenarios as there are CRITICAL/HIGH findings in the table.

| Scenario ID | F-ID | Type | Severity | What to Exercise | Acceptance Condition |
|-------------|------|------|----------|-----------------|---------------------|
|             |      |      |          |                 |                     |

---

**CROSS-SKILL PATTERNS**

Scan for root causes that appear across two or more sub-skills. For each compounding pattern:

| P-ID | Root Cause | F-IDs | Combined Blast Radius | Why Scope Is Wider Than Any Single Finding |
|------|------------|-------|----------------------|--------------------------------------------|
|      |            |       |                      |                                            |

---

**OUTPUT**

Write to: simulations/{{topic}}/simulate-{{date}}.md

Required sections in order:
1. Severity Scale
2. Type Vocabulary Map
3. Remediation Template
4. Findings Table Schema
5. Topic Entity Manifest
6. Manifest Completeness Gate
7. trace sub-skill executions (each with budget status)
8. Severity Budget Gate
9. Trace Findings Brief
10. flow sub-skill executions (each with trace link check)
11. Findings Table (complete, all cells populated, verification gate PASSED)
12. Ranked Findings (blast-radius sorted, top-tier rationale)
13. Type Vocabulary Verification
14. Execution Log
15. Test Scenario Baseline
16. Cross-Skill Patterns

Before writing the file: run the pre-output blank-cell verification gate. All eight checks
must clear. Report the gate result inline before the ranked findings section.
