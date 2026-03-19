Written to `simulations/quest/variations/rhythm-behavior-variations-R3-2026-03-17.md`.

---

## rhythm-behavior -- Round 3 Variations

**Context**: All 15 v3 criteria are already structurally saturated by R2 V-04 (SYNTHESIS step covers C-13, Rationale column covers C-14, CROSS-SKILL table label covers C-15). R3 has no new pass/fail targets -- it probes **quality dimensions within passing criteria**.

| # | Axis | Key Change | Targets |
|---|------|-----------|---------|
| **V-01** | Rationale format mandate | 3-slot required format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]` | C-08/C-14 quality |
| **V-02** | CROSS-SKILL blast radius inheritance | SYNTHESIS gets explicit inheritance rule: CROSS-SKILL blast radius = max(contributors); documented in rationale | C-09/C-15 quality |
| **V-03** | Minimal surface area | Per-section rationale reminders removed; enforcement at table column + closing confirmation only | Simplification |
| **V-04** | Combo: format + inheritance | V-01 + V-02 at full verbosity | Both quality axes |
| **V-05** | Combo: format + inheritance + minimal | V-01 + V-02 in V-03's footprint | Quality + simplification |

**Key hypotheses:**

- **V-01**: Open "one sentence" instruction allows vague rationales that technically pass C-08 without being auditable. The 3-slot format forces a model to name a specific boundary, a specific caller, and a specific effect -- three separate evidentiary claims, not one generic phrase.

- **V-02**: R2 V-04's "assign a blast radius reflecting the combined scope" is underconstrained -- a model can assign CROSS-SKILL NARROW even when contributors were MEDIUM and WIDE. The explicit `max()` rule with a no-downgrade constraint closes this quality gap without restricting valid upward scope expansion.

- **V-03**: R2 V-04 carries 5 redundant per-section "populate Blast Radius Rationale" instructions after the column mandate already provides structural enforcement. If V-03 scores equally, they're noise. If lower, they're load-bearing.

- **V-05**: Optimal production candidate -- both quality upgrades in minimal footprint. If it matches V-04's quality output, it is the deployment recommendation.
eferred. If it scores higher, full verbosity is load-bearing.

- **V-05** is the primary candidate for v3 golden: it carries the quality upgrades from V-01/V-02
  in the smallest structural footprint. If all 15 criteria pass, it is the production candidate.

**Predicted scores** (v3 rubric, aspirational denominator = 8):

| Variation | C-13 | C-14 | C-15 | C-08 quality | C-09 quality | Predicted Score |
|-----------|------|------|------|-------------|-------------|-----------------|
| V-01 | PASS | PASS | PASS | higher | baseline | 100 |
| V-02 | PASS | PASS | PASS | baseline | higher | 100 |
| V-03 | PASS | PASS | PASS | baseline | baseline | 100 |
| V-04 | PASS | PASS | PASS | higher | higher | 100 |
| V-05 | PASS | PASS | PASS | higher | higher | 100 |

All five predicted golden. R3 differentiates on rationale quality (auditable, specific vs
passable-but-vague) rather than pass/fail. The open questions are quality questions.

**Open questions:**

| Question | V | Hypothesis |
|----------|---|-----------|
| Does a 3-slot rationale format produce noticeably more specific rationales than open instruction? | V-01, V-04, V-05 | YES -- 3 named slots force boundary + caller + effect to be named separately; open instruction allows vague restatements |
| Does the inheritance rule prevent CROSS-SKILL NARROW when contributors are WIDE/MEDIUM? | V-02, V-04, V-05 | YES -- explicit max() rule with no-downgrade constraint eliminates scope underassignment |
| Are per-section rationale reminders load-bearing or redundant? | V-03 | Likely redundant -- column pressure is the structural mechanism; per-section text adds noise, not enforcement |
| Does combining format mandate + inheritance produce the best rationale quality overall? | V-04, V-05 | YES -- both quality axes are independent; combo captures both without interference |
| Does V-05 (full quality in minimal form) match V-04 in scoring? | V-05 vs V-04 | YES -- simplification preserves all structural mechanisms |

---

## V-01 -- Rationale Format Mandate

**Axis**: C-08/C-14 quality -- Blast Radius Rationale upgraded from open one-sentence instruction
to a 3-slot required format specifying boundary, propagation target, and effect.
**Hypothesis**: The open "one sentence naming the specific flows, contracts, or permission
boundaries affected" instruction in R2 V-04 allows vague rationales that technically satisfy C-08
(something is written) without being auditable (the boundary and caller are not specifically named).
A 3-slot format -- `[LEVEL] because [boundary] propagates to [caller/component], [effect]` -- forces
three separate named elements into every rationale cell. A model cannot fill the format with a
generic phrase like "because multiple downstream callers are affected"; it must name the boundary
(e.g., `session-sequence-number contract`) and the caller (e.g., `flow-conversation routing
and trace-contract pre-check`). This raises rationale quality from passable to auditable without
changing any pass/fail criterion.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue -- the full report must appear in this response.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

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

**Blast Radius Rationale** -- for each finding, write one sentence using this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: name the exact API boundary, state variable, or contract clause -- not a generic
    description like "the session layer" but the specific named boundary (e.g.,
    `session-sequence-number contract`, `role-assignment pre-condition`)
  - [caller/component]: name the specific downstream caller or component affected -- not "multiple
    callers" or "downstream components" but the named ones (e.g., `flow-conversation routing,
    trace-contract pre-check`)
  - [effect]: one phrase describing the runtime consequence (e.g., "producing stale-state errors
    at both", "blocking all subsequent state transitions")
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation routing
  and trace-contract pre-check, producing stale-state errors at both."
  Do not use the format as a template to fill with generic placeholders -- every slot must be
  specific to this finding.

Use this findings table. Open it before flow-lifecycle and append rows throughout.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

Blast Radius Rationale is required for every row. Do not leave it blank.

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
classify it as a spec-gap or contract-violation, assign a blast radius, and populate
Blast Radius Rationale using the required format.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation), classify it, assign
a blast radius, and populate Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default. Add each finding to
the table (Sub-Skill = trace-state), classify it, assign a blast radius, and populate
Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract), classify it, assign a blast radius, and
populate Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions), classify it, assign a blast radius, and populate
Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together -- a
finding whose root cause or propagation path spans two or more sub-skills.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two)
- Describe the relationship or compounding effect
- Assign a blast radius reflecting the combined scope
- Write a Blast Radius Rationale using the required format, naming the full affected scope
  across both sub-skills -- the [boundary] and [caller/component] slots must identify cross-skill
  elements, not single-sub-skill elements
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no cross-sub-skill patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

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
- Every finding has a Sub-Skill attribution, a Blast Radius, and a Blast Radius Rationale
- Every Blast Radius Rationale uses the "[LEVEL] because [boundary] propagates to
  [caller/component], [effect]" format with named boundary and named caller/component

If either category (spec-gap or contract-violation) is missing, go back and find at least
one before closing the report.

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| CROSS-SKILL | | |
| TOTAL | | |
```

---

## V-02 -- CROSS-SKILL Blast Radius Inheritance

**Axis**: C-09/C-15 quality -- SYNTHESIS section adds an explicit blast radius inheritance rule
that constrains CROSS-SKILL findings to assign the higher of the contributing sub-skills'
blast radii, with the inheritance documented in the rationale.
**Hypothesis**: In R2, SYNTHESIS section instructions say "assign a blast radius reflecting the
combined scope" -- this is correct but underconstrained. A model assigning CROSS-SKILL blast
radius independently (not relative to contributors) can produce a CROSS-SKILL NARROW finding
whose contributing sub-skills were MEDIUM and WIDE, which is a scope underassignment error.
An explicit inheritance rule -- CROSS-SKILL blast radius >= max(contributing sub-skills) -- with
a no-downgrade constraint prevents this without restricting valid upward scope expansion when
the combination genuinely opens new scope. The rationale must document which sub-skill the
level was inherited from, making the derivation auditable.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue -- the full report must appear in this response.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

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

**Blast Radius Rationale** -- for each finding, write one sentence naming the specific flows,
contracts, or permission boundaries affected. Not a restatement of the level definition --
the evidence for why that level was assigned.
  Example: "WIDE because all downstream callers of the session boundary inherit the
  corrupted sequence number before any error surface is reached."

Use this findings table. Open it before flow-lifecycle and append rows throughout.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

Blast Radius Rationale is required for every row. Do not leave it blank.

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
classify it as a spec-gap or contract-violation, assign a blast radius, and populate
Blast Radius Rationale with one sentence naming the affected scope.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation), classify it, assign
a blast radius, and populate Blast Radius Rationale.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default. Add each finding to
the table (Sub-Skill = trace-state), classify it, assign a blast radius, and populate
Blast Radius Rationale.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract), classify it, assign a blast radius, and
populate Blast Radius Rationale.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions), classify it, assign a blast radius, and populate
Blast Radius Rationale.

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together -- a
finding whose root cause or propagation path spans two or more sub-skills.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: Assign CROSS-SKILL blast radius as the HIGHER of the
  contributing sub-skills' blast radii. Do not assign CROSS-SKILL a blast radius lower than
  the highest contributor. If the combination opens scope not reached by any single contributor,
  assign the next higher level and explain what additional scope the interaction opens.
- Write a Blast Radius Rationale in this form: "Inherited [LEVEL] from [sub-skill-X]
  ([F-ID]) because [cross-skill-mechanism]; combined scope [matches/exceeds the single contributor
  because explanation]."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no cross-sub-skill patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

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
- Every finding has a Sub-Skill attribution, a Blast Radius, and a Blast Radius Rationale
- Every CROSS-SKILL finding's blast radius is >= the highest contributing sub-skill's blast radius

If either category (spec-gap or contract-violation) is missing, go back and find at least
one before closing the report.

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| CROSS-SKILL | | |
| TOTAL | | |
```

---

## V-03 -- Minimal Surface Area

**Axis**: Simplification -- R2 V-04 carries 5 redundant per-section "populate Blast Radius
Rationale" instructions (one per sub-skill section) in addition to the table column mandate and
the closing confirmation. This variation removes all per-section rationale reminders and
concentrates enforcement at two sites: the table column mandate and the closing confirmation.
**Hypothesis**: The column structural pressure (empty cell is visible omission) and the closing
confirmation (active correction loop) are the two load-bearing enforcement sites for C-08/C-14.
Per-section "populate Blast Radius Rationale" reminders repeat information the table column
already communicates. Removing them reduces prompt mass by approximately 30%, lowering the risk
of the model attending to contradictory or redundant instructions across reinforcement layers.
If V-03 scores identically to V-04, per-section repetition was noise. If V-03 scores lower,
per-section reinforcement was contributing to C-08 quality.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue.

Sections in this exact order:
  flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions,
  SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified. Name which spec
section is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a boundary.
Name the boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale**: one sentence naming the specific flows, contracts, or permission
boundaries affected by this finding. Evidence for the level, not a restatement of it.

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before it can start? What breaks if initialization
is partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off to each
other and what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify type, assign blast radius).
Say "PHASE: no findings" if a phase is clean.

---

### flow-conversation

Walk the conversation and intent flow for `{{topic}}`: intent routing paths, response
contracts, graph transitions, fallback branches, session state tracking, timeout handling.
Note anything the spec leaves unclear or where caller and callee would disagree.

Add each finding immediately (Sub-Skill = flow-conversation, classify, assign blast radius).
If none: say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`: spec-defined states, valid transitions,
reachability from initial state, unauthorized crossings (contract-violation by default).

Add each finding immediately (Sub-Skill = trace-state, classify, assign blast radius).
If none: say so explicitly.

---

### trace-contract

Check every API and service boundary: pre/postcondition symmetry, data invariants, migration
contracts. Note anywhere the callee's behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access control
assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for compounding risks that only
become visible when results from multiple sub-skills are read together.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two)
- Describe the relationship or compounding effect
- Assign a blast radius reflecting the combined scope
- Write a Blast Radius Rationale sentence naming the full cross-skill scope
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete, specific next step a developer can execute before writing any
implementation code. Name the exact spec section, boundary, or component -- not a generic
directive.

Before you finish, confirm:
- At least one finding is a spec-gap
- At least one finding is a contract-violation
- Every finding has Sub-Skill attribution, Blast Radius, and Blast Radius Rationale

If either category is missing, go back and find at least one before closing the report.

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| CROSS-SKILL | | |
| TOTAL | | |
```

---

## V-04 -- Combo: Format Mandate + Inheritance Rule

**Axis**: V-01 (C-08/C-14 quality via 3-slot rationale format) + V-02 (C-09/C-15 quality via
CROSS-SKILL inheritance rule). Full R2 V-04 verbosity retained.
**Hypothesis**: The 3-slot format mandate (V-01) ensures per-finding rationales name boundary,
caller, and effect specifically. The inheritance rule (V-02) ensures CROSS-SKILL blast radii
are correctly scoped relative to contributors. The two axes are orthogonal -- V-01 applies to
all five sub-skill findings; V-02 applies only to SYNTHESIS findings. Combining them upgrades
both quality dimensions simultaneously. This is the primary quality candidate for R3: two
independent quality additions, each targeting a different finding category, no structural
interaction risk.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue -- the full report must appear in this response.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

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

**Blast Radius Rationale** -- for each finding, write one sentence using this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: name the exact API boundary, state variable, or contract clause (not a generic
    description -- e.g., `session-sequence-number contract`, `role-assignment pre-condition`)
  - [caller/component]: name the specific downstream caller or component affected (not "multiple
    callers" -- e.g., `flow-conversation routing, trace-contract pre-check`)
  - [effect]: one phrase for the runtime consequence (e.g., "producing stale-state errors at
    both", "blocking all subsequent state transitions")
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation routing
  and trace-contract pre-check, producing stale-state errors at both."

Use this findings table. Open it before flow-lifecycle and append rows throughout.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

Blast Radius Rationale is required for every row. Do not leave it blank.

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
classify it as a spec-gap or contract-violation, assign a blast radius, and populate
Blast Radius Rationale using the required format.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation), classify it, assign
a blast radius, and populate Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default. Add each finding to
the table (Sub-Skill = trace-state), classify it, assign a blast radius, and populate
Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract), classify it, assign a blast radius, and
populate Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions), classify it, assign a blast radius, and populate
Blast Radius Rationale using the required format.

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together -- a
finding whose root cause or propagation path spans two or more sub-skills.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each contributor
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: Assign CROSS-SKILL blast radius as the HIGHER of the
  contributing sub-skills' blast radii. Do not assign a lower level than the highest contributor.
  If the combination opens scope not present in any single contributor, assign the next higher
  level and explain what new scope the interaction opens.
- Write a Blast Radius Rationale using the required format: "[LEVEL] because [boundary] propagates
  to [caller/component], [effect]" -- where [boundary] and [caller/component] span both contributing
  sub-skills. Append: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no cross-sub-skill patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

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
- Every finding has a Sub-Skill attribution, a Blast Radius, and a Blast Radius Rationale
- Every Blast Radius Rationale uses the "[LEVEL] because [boundary] propagates to
  [caller/component], [effect]" format with specific named boundary and caller/component
- Every CROSS-SKILL finding's blast radius is >= the highest contributing sub-skill's blast radius

If either category (spec-gap or contract-violation) is missing, go back and find at least
one before closing the report.

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| CROSS-SKILL | | |
| TOTAL | | |
```

---

## V-05 -- Combo: Format Mandate + Inheritance Rule + Minimal Surface Area

**Axis**: V-01 (3-slot rationale format) + V-02 (CROSS-SKILL inheritance rule) in V-03's
minimal structure (per-section rationale reminders removed; enforcement concentrated at table
column + closing confirmation).
**Hypothesis**: V-04 carries both quality upgrades but with full verbosity. If the 3-slot format
mandate is strong enough to enforce specific rationales through column pressure alone (no per-section
reminders), and the inheritance rule survives without per-sub-skill context repetition, then V-05
delivers V-04 quality at V-03 footprint. This is the primary candidate for production deployment:
minimal prompt mass, highest quality constraints, all 15 criteria satisfied. Risk: the format
mandate may need the per-section "using the required format" reminder to reliably apply in dense
output. If V-05 scores lower than V-04 on rationale quality, per-section repetition is load-bearing
for format adherence.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not break it into separate
responses. Do not promise to continue.

Sections in this exact order:
  flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions,
  SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified. Name which spec
section is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a boundary.
Name the boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- for each finding, write one sentence using this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: name the exact API boundary, state variable, or contract clause
  - [caller/component]: name the specific downstream caller or component -- not generic terms
  - [effect]: one phrase for the runtime consequence
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation routing
  and trace-contract pre-check, producing stale-state errors at both."

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before it can start? What breaks if initialization
is partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off to each
other and what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify type, assign blast radius).
Say "PHASE: no findings" if a phase is clean.

---

### flow-conversation

Walk the conversation and intent flow for `{{topic}}`: intent routing paths, response
contracts, graph transitions, fallback branches, session state tracking, timeout handling.

Add each finding immediately (Sub-Skill = flow-conversation, classify, assign blast radius).
If none: say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`: spec-defined states, valid transitions,
reachability from initial state, unauthorized crossings (contract-violation by default).

Add each finding immediately (Sub-Skill = trace-state, classify, assign blast radius).
If none: say so explicitly.

---

### trace-contract

Check every API and service boundary: pre/postcondition symmetry, data invariants, migration
contracts. Note anywhere the callee's behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access control
assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for compounding risks that only
become visible when results from multiple sub-skills are read together.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each contributor
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: Assign CROSS-SKILL blast radius as the HIGHER of the
  contributing sub-skills' blast radii. Do not assign lower than the highest contributor.
  If the combination opens new scope, assign the next higher level and explain why.
- Write a Blast Radius Rationale using the required format. Append:
  "Inherited [LEVEL] from [sub-skill-X] ([F-ID])."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete, specific next step a developer can execute before writing any
implementation code. Name the exact spec section, boundary, or component.

Before you finish, confirm:
- At least one finding is a spec-gap
- At least one finding is a contract-violation
- Every finding has Sub-Skill attribution, Blast Radius, and Blast Radius Rationale
- Every Blast Radius Rationale uses the "[LEVEL] because [boundary] propagates to
  [caller/component], [effect]" format with named boundary and named caller/component
- Every CROSS-SKILL finding's blast radius is >= the highest contributing sub-skill's blast radius

If either category is missing, go back and find at least one before closing the report.

Coverage summary:
| Sub-Skill | Findings | Types |
|-----------|---------|-------|
| flow-lifecycle | | |
| flow-conversation | | |
| trace-state | | |
| trace-contract | | |
| trace-permissions | | |
| CROSS-SKILL | | |
| TOTAL | | |
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| R1 | 2026-03-17 | Initial 5 variations (V-01 through V-05). All scored 90. C-08 and C-09 not targeted. |
| R2 | 2026-03-17 | All 5 target C-08 and/or C-09. Base: R1 V-05. V-04 (Rationale column + SYNTHESIS) scores 100. |
| R3 | 2026-03-17 | All 15 v3 criteria already saturated by R2 V-04. R3 probes quality dimensions: rationale format specificity (V-01), CROSS-SKILL blast radius inheritance (V-02), minimal surface area (V-03), and combos (V-04, V-05). |
