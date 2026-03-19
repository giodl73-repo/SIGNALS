Written to `simulations/quest/variations/rhythm-behavior-variations-R2-2026-03-17.md`.

---

## rhythm-behavior -- Round 2 Variations

**Base**: R1 V-05 (highest robustness, C-10/C-11/C-12 already embedded).
**R2 targets**: C-08 and C-09 -- both failed all 5 R1 variations, never targeted.

| # | Axis | Key Change | Targets |
|---|------|-----------|---------|
| **V-01** | C-08 via structural column | `Blast Radius Rationale` column added to findings table; required for every row | C-08 |
| **V-02** | C-08 via inline annotation | `Why WIDE/MEDIUM/NARROW:` annotation mandated at point of blast radius assignment in each sub-skill section | C-08 (different mechanism) |
| **V-03** | C-09 via SYNTHESIS step | Dedicated SYNTHESIS section after all five sub-skill sections; explicit cross-sub-skill pattern search before consolidation | C-09 |
| **V-04** | Combo C-08 + C-09 | Rationale column + SYNTHESIS step | C-08 + C-09 |
| **V-05** | Combo C-08 + C-09 + reinforced C-12 | Rationale column + SYNTHESIS + explicit at-discovery mandate per section | C-08 + C-09 + C-12 |

**Key design decisions:**

- **V-01 vs V-02** isolates the C-08 mechanism: column (structural, cell omission is visible) vs annotation (prose, closer to context, could be silently skipped). The rubric requires "every finding includes a one-sentence rationale naming the affected scope" -- both forms satisfy the letter, but column is harder to violate.

- **V-03** decouples C-09 from C-08. If V-03 passes C-09 without rationale columns, C-09 is purely an instruction gap. If it fails, cross-sub-skill synthesis may need the richer rationale context that V-04 provides.

- **V-04** is the primary golden candidate: two minimal structural additions, no noise, maximum coverage of the two failing criteria.

- **V-05** tests whether the explicit "apply at point of discovery" mandate per section header improves rationale quality over V-04, at the cost of verbosity. Likely marginal given the pre-opened table already embeds the pattern.

**Predicted scores** (v2 rubric, aspirational denominator = 5):

| Variation | C-08 | C-09 | C-10 | C-11 | C-12 | Predicted Score |
|-----------|------|------|------|------|------|-----------------|
| V-01 | PASS | FAIL | PASS | PASS | PASS | 3/5 asp → ~96 |
| V-02 | LIKELY | FAIL | PASS | PASS | PASS | 3/5 asp → ~96 |
| V-03 | FAIL | PASS | PASS | PASS | PASS | 3/5 asp → ~96 |
| V-04 | PASS | PASS | PASS | PASS | PASS | 5/5 asp → **100** |
| V-05 | PASS | PASS | PASS | PASS | PASS | 5/5 asp → **100** |
ine "Why WIDE/MEDIUM/NARROW:" annotation unlock C-08? | V-02 | LIKELY -- but annotation may be dropped in dense output |
| Does a standalone SYNTHESIS section unlock C-09? | V-03, V-04, V-05 | YES -- named step makes cross-sub-skill search explicit |
| Does C-09 require C-08 to first exist? | V-03 | NO -- testing decoupling |
| Does reinforced C-12 wording in V-05 add measurable value over V-04? | V-05 | MARGINAL -- V-04's pre-opened table already embeds at-discovery attribution |

---

## V-01 -- C-08 via Structural Rationale Column

**Axis**: C-08 only -- blast radius justification added as a dedicated table column.
**Hypothesis**: A `Blast Radius Rationale` column in the findings table forces a one-sentence
scope justification into every row by structural pressure. The model cannot populate the row
without filling the column. The column is more reliable than a prose mandate because it makes
omission visible as an empty cell rather than a missing sentence in running text.

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

**Blast Radius Rationale** -- for each finding, write one sentence naming the specific flows,
contracts, or permission boundaries affected. This is not a restatement of the WIDE/MEDIUM/
NARROW level -- it is the evidence for why that level was assigned.
  Example: "WIDE because all callers of the session-state boundary inherit the corrupted
  sequence number, blocking flow-conversation and trace-contract simultaneously."

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
classify it as a spec-gap or contract-violation, assign a blast radius, and write one
sentence in Blast Radius Rationale naming the affected scope.

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
| TOTAL | | |
```

---

## V-02 -- C-08 via Inline Annotation

**Axis**: C-08 only -- blast radius justification embedded as a mandatory annotation at the
point of blast radius assignment in each sub-skill section, rather than a separate column.
**Hypothesis**: An inline "Why WIDE/MEDIUM/NARROW:" annotation written at the moment of
discovery is closer to the finding's narrative context and may produce richer, more specific
rationale than a table cell. The trade-off: prose annotation can be skipped silently, while
a column cell cannot. This variation tests whether inline placement yields better rationale
quality even at some risk of omission.

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

**For every blast radius assignment** in any section, immediately follow it with a
"Why [LEVEL]:" annotation on the same line or the next line. The annotation must name the
specific flows, contracts, or permission boundaries affected -- not restate the level
definition. One sentence is sufficient.
  Format: "Why WIDE: all session-state readers inherit the stale sequence, breaking both
  flow-conversation routing and trace-contract pre-condition checks."
  Format: "Why NARROW: error is caught inside the intent-router component before any
  downstream boundary is reached."

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
classify it as a spec-gap or contract-violation, assign a blast radius, and write the
"Why [LEVEL]:" annotation immediately after the blast radius assignment.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation), classify it, assign
a blast radius, and write the "Why [LEVEL]:" annotation.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default. Add each finding to
the table (Sub-Skill = trace-state), classify it, assign a blast radius, and write the
"Why [LEVEL]:" annotation.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract), classify it, assign a blast radius, and
write the "Why [LEVEL]:" annotation.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions), classify it, assign a blast radius, and write the
"Why [LEVEL]:" annotation.

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
- Every finding has a Sub-Skill attribution, a Blast Radius, and a "Why [LEVEL]:" annotation

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
| TOTAL | | |
```

---

## V-03 -- C-09 via SYNTHESIS Step

**Axis**: C-09 only -- a dedicated SYNTHESIS section inserted between the five sub-skill
sections and the consolidated findings. The SYNTHESIS step instructs an explicit cross-
sub-skill pattern search before consolidation begins.
**Hypothesis**: C-09 fails when there is no explicit instruction to look for cross-sub-skill
patterns. Adding a named SYNTHESIS step -- positioned after all five sections have run, but
before the final FINDINGS consolidation -- gives the model a moment to compare findings
across sections and identify compounding risks. Placement after all five sections maximizes
the evidence available for cross-skill pattern detection.

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
disagree. Add each finding to the table (Sub-Skill = flow-conversation), classify it, and
assign a blast radius.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default. Add each finding to
the table (Sub-Skill = trace-state), classify it, and assign a blast radius.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract), classify it, and assign a blast radius.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions), classify it, and assign a blast radius.

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
- Every finding has a Sub-Skill attribution and a Blast Radius

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

## V-04 -- Combo: Rationale Column + SYNTHESIS Step

**Axis**: V-01 (C-08 via structural column) + V-03 (C-09 via SYNTHESIS step).
**Hypothesis**: The Blast Radius Rationale column (V-01) unlocks C-08 mechanically -- every
row must have a rationale cell. The SYNTHESIS step (V-03) unlocks C-09 explicitly -- the
model is given a named moment to search for cross-sub-skill patterns. Together they target
both failing aspirationals in a single prompt. This is the primary golden candidate for R2:
two separate structural additions, each minimal, each targeting one criterion.

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
- Name the contributing sub-skills (at least two)
- Describe the relationship or compounding effect
- Assign a blast radius reflecting the combined scope
- Write a Blast Radius Rationale sentence naming the full affected scope across both sub-skills
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

## V-05 -- Combo: Rationale Column + SYNTHESIS + Reinforced At-Discovery Attribution

**Axis**: V-04 (C-08 + C-09) plus explicit at-discovery attribution mandate in each sub-skill
section header, reinforcing C-12 beyond what the pre-opened table already provides.
**Hypothesis**: V-04 inherits C-12 from the R1 V-05 base (pre-opened table + append-throughout
instruction). V-05 tests whether an explicit sentence in each section -- "apply Sub-Skill,
Finding Type, Blast Radius, and Blast Radius Rationale at the point of discovery" -- improves
rationale completeness in the Rationale column. Risk is prompt verbosity; benefit is zero
ambiguity about when attribution applies.

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
  Example: "WIDE because the corrupted session state propagates to all callers of the
  flow-conversation routing boundary before any component surfaces an error."

**Attribution rule**: Apply Sub-Skill, Finding Type, Blast Radius, and Blast Radius Rationale
at the moment of discovery -- inside the sub-skill section where the finding first appears.
Do not defer classification to the consolidated section. The consolidation step is mechanical:
it reproduces the table; it does not reclassify.

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

For each issue in any phase: immediately apply Sub-Skill = flow-lifecycle, classify as
spec-gap or contract-violation, assign Blast Radius, and write Blast Radius Rationale before
moving to the next finding. Add the row to the findings table at the point of discovery.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow the intent routing
paths, response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree.

For each issue: immediately apply Sub-Skill = flow-conversation, classify as spec-gap or
contract-violation, assign Blast Radius, and write Blast Radius Rationale. Add the row to
the findings table at the point of discovery.

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace
valid transitions, check reachability from the initial state, and look for unauthorized
crossings. An unauthorized crossing is a contract-violation by default.

For each issue: immediately apply Sub-Skill = trace-state, classify as spec-gap or
contract-violation, assign Blast Radius, and write Blast Radius Rationale. Add the row to
the findings table at the point of discovery.

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect.

For each issue: immediately apply Sub-Skill = trace-contract, classify as spec-gap or
contract-violation, assign Blast Radius, and write Blast Radius Rationale. Add the row to
the findings table at the point of discovery.

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge.

For each issue: immediately apply Sub-Skill = trace-permissions, classify as spec-gap or
contract-violation, assign Blast Radius, and write Blast Radius Rationale. Add the row to
the findings table at the point of discovery.

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together -- a
finding whose root cause or propagation path spans two or more sub-skills.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two)
- Describe the relationship or compounding effect
- Apply the attribution rule: Sub-Skill = CROSS-SKILL, Finding Type, Blast Radius, and
  Blast Radius Rationale at point of synthesis -- name the full affected scope across both
  contributing sub-skills
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table

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
- Every Blast Radius Rationale names a specific flow, contract, or permission boundary

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

## Version History

| Version | Date | Changes |
|---------|------|---------|
| R1 | 2026-03-17 | Initial 5 variations (V-01 through V-05). All scored 90. C-08 and C-09 not targeted. |
| R2 | 2026-03-17 | All 5 variations target C-08 and/or C-09. Base: R1 V-05. Single-axis: V-01 (C-08 column), V-02 (C-08 annotation), V-03 (C-09 synthesis). Combos: V-04 (C-08+C-09), V-05 (C-08+C-09+reinforced C-12). |
