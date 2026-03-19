Written to `simulations/quest/variations/rhythm-behavior-variations-R1-2026-03-17.md`.

---

## rhythm-behavior -- Round 1 Variations

5 complete, runnable skill body prompts generated.

| # | Axis | Key change | Targets |
|---|------|-----------|---------|
| **V-01** | Output format | Findings table with Blast Radius + Finding Type columns; consolidated section sorts and labels the table | C-03, C-04 structural |
| **V-02** | Phrasing register | Descriptive/conversational guidance; section headers as natural language; implicit structure | C-02 adherence hypothesis |
| **V-03** | Lifecycle emphasis | flow-lifecycle decomposes into 4 named phases: INIT / NOMINAL / DEGRADED / TEARDOWN | Finding richness in S1 |
| **V-04** | Combo V-01 + V-03 | Table format + phase prompts | C-03/C-04 + richer S1 |
| **V-05** | Combo V-01 + V-02 + V-03 | All three -- tests if conversational register softens table discipline | Maximum coverage |

**Round 1 design decisions:**

- All 5 variations include the sequence declaration preamble (C-01 is not varied -- it's a structural invariant).
- V-02 uses a pre-opened findings table with a "keep adding rows throughout" instruction rather than a formal PRE-COMMIT directive -- tests whether the lighter framing holds.
- The key open question: **does the Blast Radius column in the findings table satisfy C-03**, or does the rubric require a separate ranked list? If the scorer requires a standalone numbered list, V-01/V-04/V-05 fail C-03 and the next round should add an explicit ranked list section.
- V-05 is the maximum-coverage candidate and the most likely golden if the conversational register doesn't erode table discipline.
able discipline. | All three single-axis changes combined. |

**Open questions for scoring:**

| Question | Variations | Predicted |
|----------|-----------|-----------|
| Does a Blast Radius column in the findings table satisfy C-03 without a separate ranked list? | V-01, V-04, V-05 | YES -- column provides explicit ranking signal per finding |
| Does "spec-gap" / "contract-violation" as a Type column satisfy C-04 distinguishability? | V-01, V-04, V-05 | YES |
| Does conversational register risk losing the sequence declaration (C-01)? | V-02, V-05 | NO -- declaration appears as explicit preamble in all variations |
| Does per-phase S1 prompting risk producing a multi-section S1 that violates C-02 continuity? | V-03, V-04, V-05 | NO -- phases are sub-bullets within the single S1 section |
| Does explicit null-result instruction ("if no findings, state: No findings") satisfy C-07? | All | YES |

---

## V-01 -- Structured Findings Table

**Axis**: Output format -- findings table with explicit Blast Radius and Finding Type columns.
**Hypothesis**: A table with a Blast Radius column (WIDE / MEDIUM / NARROW) and a Type column
(spec-gap / contract-violation) forces C-03 (explicit ranking) and C-04 (category
distinguishability) to be satisfied structurally. The consolidated FINDINGS section sorts the
same table by Blast Radius descending, making rank order unambiguous. Per-finding Sub-Skill
attribution in the table satisfies C-05 without extra instruction.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Produce one unified simulation findings report. Do not split into separate outputs.
Do not defer or stub any section.

Declared execution sequence:
  S1 flow-lifecycle -> S2 flow-conversation -> S3 trace-state ->
  S4 trace-contract -> S5 trace-permissions -> FINDINGS

Execute sections in declared order. Do not reorder.

---

## DEFINITIONS

Blast Radius -- scope of downstream impact if a finding is not addressed before implementation:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

Pre-commit before S1. Append rows as findings are discovered in each section.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Impact | Remediation |
|------|-----------|----------|--------------|--------------|--------|-------------|

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

Examine: initialization state, nominal flow phases, degraded or error states, teardown and
cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = flow-lifecycle).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S1 flow-lifecycle: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

Examine: intent scope and routing, response contracts, graph state transitions, fallback
handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = flow-conversation).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S2 flow-conversation: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

Examine: all spec-defined states, exit transitions, state invariants, reachability from
initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-state).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S3 trace-state: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

Examine: API and service boundaries, pre/postcondition symmetry, data invariants, integration
seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-contract).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S4 trace-contract: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

Examine: role authorization rules, field-level security, team membership effects, sharing
rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-permissions).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S5 trace-permissions: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## FINDINGS

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last). Reproduce the sorted table here.

Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row (highest blast radius). Provide one specific, actionable
next step that can be executed before implementation begins. The action must name the exact
spec section, boundary, or component to address -- not a generic "investigate further."

REQUIRE:
  - At least one finding classified spec-gap
  - At least one finding classified contract-violation
  - All findings carry a Sub-Skill attribution
  - Blast Radius column populated for every finding
  - Top finding has a concrete next step

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| TOTAL | | |
```

---

## V-02 -- Conversational Register

**Axis**: Phrasing register -- descriptive and natural-language guidance throughout.
**Hypothesis**: Replacing imperative EXIT GATE directives with natural-language framing
reduces template-following overhead and produces a more readable unified output. The
sequence declaration and finding type definitions remain explicit; the section descriptions
shift to describe *what the output should contain* rather than *what commands to execute*.
This may improve C-02 (unified report) compliance by reducing the cognitive pressure to
produce separate structured outputs.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue -- the full report must appear in this response.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a consolidated findings section.

---

### What to look for

A **spec-gap** is a requirement that is missing, ambiguous, or underspecified in the target
spec. When you find one, say which section of the spec is silent or unclear.

A **contract-violation** is a case where a caller and a callee have divergent assumptions at
a boundary. When you find one, name the boundary.

**Blast radius** describes how widely a problem propagates if you ship it unaddressed:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, but shared state not reached
- NARROW -- failure stays inside one component

---

### flow-lifecycle

Walk through the complete lifecycle of `{{topic}}` as a business process -- from first
initialization through normal operation, into error or degraded states, through teardown, and
across integration handoffs. Note anything the spec leaves unclear or where two components
would behave inconsistently with each other. Assign a blast radius to each issue and say
whether it is a spec-gap or a contract-violation.

If you find no issues, say so explicitly.

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Assign a blast radius to each issue and classify it.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
every valid transition, check reachability from the initial state, and look for unauthorized
state crossings. An unauthorized crossing is a contract-violation by default. Assign a blast
radius to each issue you find.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note any place where the callee's behavior differs from what callers expect.
Assign a blast radius to each issue and classify it.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Assign a blast radius and classify
each issue.

If you find no issues, say so explicitly.

---

### Consolidated Findings

List every finding from the five sections above, grouped first by blast radius (WIDE issues
first, NARROW issues last). For each finding, say which sub-skill surfaced it and whether
it is a spec-gap or a contract-violation.

The highest blast-radius finding gets one concrete, specific next step -- the exact action
a developer should take before writing the first line of implementation code.

Confirm that your list contains at least one spec-gap and at least one contract-violation.
If it does not, revisit the sections above.

Coverage summary: for each of the five sub-skills, how many findings did it produce?
```

---

## V-03 -- Lifecycle Emphasis

**Axis**: Lifecycle emphasis -- flow-lifecycle section receives explicit phase prompts
(INIT / NOMINAL / DEGRADED / TEARDOWN). Other sections unchanged.
**Hypothesis**: Naming the four lifecycle phases as simulation targets in S1 yields more
findings per phase and makes the flow-lifecycle boundary clearer relative to flow-conversation
(S2). Richer S1 output increases the probability of surfacing WIDE-blast spec-gaps from the
lifecycle domain, which are the most common high-blast findings in orchestration scenarios.
The extra specificity does not risk C-02 because all phases remain subsections of a single S1
section.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Produce one unified simulation findings report. Do not split into separate outputs.
Do not defer or stub any section.

Declared execution sequence:
  S1 flow-lifecycle -> S2 flow-conversation -> S3 trace-state ->
  S4 trace-contract -> S5 trace-permissions -> FINDINGS

Execute sections in declared order. Do not reorder.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           missing, ambiguous, or underspecified requirement -- cite spec section
  contract-violation: caller/callee assumption divergence at a named boundary

---

## FINDINGS TABLE

Pre-commit before S1. Append rows throughout.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Impact | Remediation |
|------|-----------|----------|--------------|--------------|--------|-------------|

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}` across four phases. For each
phase, examine the concerns listed. Add findings to FINDINGS TABLE as they are discovered.

**INIT phase** -- What state does `{{topic}}` require to be initialized? What pre-conditions
must hold? What happens if initialization is partial or interrupted?

**NOMINAL phase** -- What is the expected flow through normal operation? What boundaries are
crossed between components? Where could a nominal flow silently diverge from spec?

**DEGRADED phase** -- What states does `{{topic}}` enter under error conditions? Are degraded
states fully specified? What recovery paths exist and are they complete?

**TEARDOWN phase** -- How does `{{topic}}` terminate or hand off? What cleanup is required?
Are integration handoffs to other components fully specified?

Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings in a phase: state "INIT: no findings." (or the relevant phase name).

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

Examine: intent scope and routing, response contracts, graph state transitions, fallback
handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = flow-conversation).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S2 flow-conversation: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

Examine: all spec-defined states, exit transitions, state invariants, reachability from
initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-state).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S3 trace-state: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

Examine: API and service boundaries, pre/postcondition symmetry, data invariants, integration
seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-contract).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S4 trace-contract: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

Examine: role authorization rules, field-level security, team membership effects, sharing
rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-permissions).
Classify each finding as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S5 trace-permissions: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## FINDINGS

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last). Reproduce sorted table here.
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row. Provide one specific, actionable next step executable
before implementation begins. Name the exact spec section, boundary, or component to address.

REQUIRE:
  - At least one finding classified spec-gap
  - At least one finding classified contract-violation
  - All findings carry Sub-Skill attribution
  - Blast Radius column populated for every finding
  - Top finding has a concrete next step

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| TOTAL | | |
```

---

## V-04 -- Combo: Structured Table + Lifecycle Phases

**Axis**: V-01 (output format) + V-03 (lifecycle emphasis).
**Hypothesis**: Structured table output with explicit Blast Radius and Type columns
(V-01) combined with four named lifecycle phases in flow-lifecycle (V-03) produces the
maximum density of correctly attributed findings at minimal prompt overhead. The table
handles C-03 and C-04 mechanically; the phase prompts drive finding richness in the
highest-risk simulation domain.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Produce one unified simulation findings report. Do not split into separate outputs.
Do not defer or stub any section.

Declared execution sequence:
  S1 flow-lifecycle -> S2 flow-conversation -> S3 trace-state ->
  S4 trace-contract -> S5 trace-permissions -> FINDINGS

Execute sections in declared order. Do not reorder.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           missing, ambiguous, or underspecified requirement -- cite spec section
  contract-violation: caller/callee assumption divergence at a named boundary

---

## FINDINGS TABLE

Pre-commit before S1. Append rows throughout.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Impact | Remediation |
|------|-----------|----------|--------------|--------------|--------|-------------|

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}` across four named phases.

**INIT** -- pre-conditions, initialization state, partial-init failure modes.
**NOMINAL** -- expected operational flow, component boundary crossings, silent divergence risks.
**DEGRADED** -- error and degraded states, recovery completeness, spec coverage of failure modes.
**TEARDOWN** -- termination, cleanup requirements, integration handoff completeness.

For each issue in any phase: add a row to FINDINGS TABLE (Sub-Skill = flow-lifecycle).
Classify as spec-gap or contract-violation. Assign Blast Radius.

If no findings in a phase, note it inline (e.g., "INIT: no findings").

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

Examine: intent scope and routing, response contracts, graph state transitions, fallback
handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = flow-conversation).
Classify as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S2 flow-conversation: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

Examine: all spec-defined states, exit transitions, state invariants, reachability from
initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-state).
Classify as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S3 trace-state: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

Examine: API and service boundaries, pre/postcondition symmetry, data invariants, integration
seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-contract).
Classify as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S4 trace-contract: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

Examine: role authorization rules, field-level security, team membership effects, sharing
rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE (Sub-Skill = trace-permissions).
Classify as spec-gap or contract-violation. Assign Blast Radius.

If no findings: state "S5 trace-permissions: no findings."

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## FINDINGS

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last). Reproduce sorted table here.
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row. Provide one specific, actionable next step executable
before implementation begins. Name the exact spec section, boundary, or component to address.

REQUIRE:
  - At least one finding classified spec-gap
  - At least one finding classified contract-violation
  - All findings carry Sub-Skill attribution
  - Blast Radius column populated for every finding
  - Top finding has a concrete next step

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| TOTAL | | |
```

---

## V-05 -- Combo: Structured Table + Conversational Register + Lifecycle Phases

**Axis**: V-01 (output format) + V-02 (phrasing register) + V-03 (lifecycle emphasis).
**Hypothesis**: All three single-axis improvements combined. The table format enforces C-03
and C-04 structurally; the conversational register may improve readability and unified-output
adherence; the lifecycle phases drive finding richness in the highest-risk domain. The risk
is that conversational register in the section bodies softens the table discipline -- this
combo tests whether the table's structural gravity holds even when surrounding prose is
descriptive rather than imperative.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue -- the full report must appear in this response.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a consolidated findings section.

---

### What to look for

A **spec-gap** is a requirement that is missing, ambiguous, or underspecified. When you find
one, say which section of the spec is silent or unclear.

A **contract-violation** is a case where a caller and a callee have divergent assumptions at
a boundary. When you find one, name the boundary.

**Blast radius** describes propagation scope if the problem ships unaddressed:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

Use this findings table. Open it before flow-lifecycle and append rows throughout.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Impact | Remediation |
|------|-----------|----------|--------------|--------------|--------|-------------|

---

### flow-lifecycle

Walk through the lifecycle of `{{topic}}` in four phases:

**INIT** -- What does `{{topic}}` need before it can start? What breaks if initialization
is partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off to each
other and what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

For each issue in any phase, add a row to the findings table (Sub-Skill = flow-lifecycle),
classify it as a spec-gap or contract-violation, and assign a blast radius.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table, classify it, and assign a blast radius.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default. Add each finding to
the table, classify it, and assign a blast radius.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table, classify it, and assign a blast radius.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table,
classify it, and assign a blast radius.

If you find no issues, say so explicitly.

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

The first finding in the sorted list (highest blast radius) gets one concrete, specific next
step that a developer can execute before writing the first line of implementation code. Name
the exact spec section, boundary, or component to address -- not a generic directive.

Before you finish, confirm:
- At least one finding is a spec-gap
- At least one finding is a contract-violation
- Every finding has a Sub-Skill attribution and a Blast Radius

If either category is missing, go back and find at least one before closing the report.

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| TOTAL | | |
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| R1 | 2026-03-17 | Initial variations for rhythm-behavior (fresh skill, no prior champion) |
