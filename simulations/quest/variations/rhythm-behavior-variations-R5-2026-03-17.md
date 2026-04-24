Written to `simulations/quest/variations/rhythm-behavior-variations-R5-2026-03-17.md`.

---

## rhythm-behavior R5 Variations Summary

**Two new criteria to satisfy (C-19/C-20, aspirational denominator 11 -> 13)**:
- C-19: One axis per gate — a compound gate covering two axes collapses to one
- C-20: Axis-named repair verb — each gate must carry "add" / "rewrite" / "fix" (not a generic verb)

**Variation table**:

| V | Axis | Change | Prediction |
|---|------|--------|-----------|
| V-01 | Output format | Gate headers renamed: "Coverage Axis", "Format Axis", "Inheritance Axis" | 100 |
| V-02 | Phrasing register (boundary probe) | All three gates use "correct" instead of add/rewrite/fix | **C-20 FAIL** — 99.2 |
| V-03 | Phrasing register | Explicit anti-merge rule prepended: "One axis per gate. Do not merge." | 100 |
| V-04 | Combo: format + register | V-01 axis-labeled headers + V-03 anti-merge rule, full verbosity | 100 |
| V-05 | Combo + minimal footprint | V-04 at minimum mass | 100 |

**V-02 is the boundary probe**: confirms whether C-20's "axis-named" requirement means distinct verbs per axis or only independent conditionality per gate. Predicted FAIL: "correct" provides no axis differentiation signal, so the model has no structural cue distinguishing a missing-finding correction from a rationale-cell rewrite.

**Key open question confirmed by V-01 vs V-03**: Axis labeling in headers (structural) vs. explicit anti-merge rule (declarative) — are they independently load-bearing or does one subsume the other? V-04 tests the combo; if V-04 = V-01 = V-03 = 100, either mechanism suffices alone. If one drops below 100, the other carries the weight.
em to "Coverage Axis", "Format Axis", "Inheritance Axis" makes the one-axis-per-gate constraint visible in the label itself, giving the model a structural cue that no two headers can name the same axis.
- **V-02**: "Correct" is a generic repair verb that doesn't name which axis it targets. C-20 requires that the repair verb identify the specific axis so the model has an independent structural cue per gate. Expected to FAIL C-20 because "correct" provides no axis differentiation -- all three gates look identical to the model at the repair instruction level.
- **V-03**: The one-axis-per-gate constraint is implied by having three separate labeled gates in R4 V-05, but is never stated as a rule. An explicit preamble ("One axis per gate. Do not merge.") prevents a model from collapsing Gates 2+3 under ambiguous topics where format and inheritance violations co-occur.
- **V-04**: Axis labeling (V-01) and explicit anti-merge rule (V-03) target C-19 from different angles: V-01 encodes the constraint in the structure, V-03 states it as an instruction. They are orthogonal -- combining them eliminates both ambiguity vectors simultaneously.
- **V-05**: V-04 at minimal prompt mass. If V-05 matches V-04 on all 20 criteria, the additional words in V-04 are noise and V-05 is the deployment recommendation.

**Predicted scores under v5 rubric** (aspirational denominator = 13):

| Variation | C-19 | C-20 | Composite | Golden |
|-----------|------|------|-----------|--------|
| V-01 | PASS | PASS | **100** | YES |
| V-02 | PASS | **FAIL** | 99.2 | YES |
| V-03 | PASS | PASS | **100** | YES |
| V-04 | PASS | PASS | **100** | YES |
| V-05 | PASS | PASS | **100** | YES |

V-02 is the deliberate boundary probe: if it passes C-20, a generic repair verb satisfies axis-naming and the specificity requirement is about independence of conditionality only. If it fails as predicted, distinct repair verbs are a load-bearing mechanism.

**Open questions**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does axis-labeled gate header enforce C-19 better than a function-named header? | V-01, V-04 | YES -- "Coverage Axis" makes the one-axis constraint visible in the label; "Coverage" alone does not |
| Does a generic repair verb ("correct") fail C-20 when axis-named verbs would pass? | V-02 | YES -- "correct" provides no axis differentiation; the model has no structural cue to fire distinct repairs |
| Does an explicit anti-merge rule prevent axis collapse under ambiguous topics? | V-03, V-04 | YES -- "One axis per gate. Do not merge." closes the gap where two-axis violations might tempt a compound correction |
| Do axis labeling and anti-merge rule independently add value, or does one subsume the other? | V-04 vs V-01/V-03 | ORTHOGONAL -- labeling encodes constraint structurally; the rule states it declaratively; both are non-redundant |
| Does V-05 match V-04 on all 20 criteria at minimal footprint? | V-05 vs V-04 | YES -- axis labels and anti-merge rule survive compression |

---

## V-01 -- Axis-Labeled Gate Headers (Output Format)

**Axis**: Output format -- closing gate headers renamed from function-names ("Coverage", "Format", "Inheritance") to axis-names ("Coverage Axis", "Format Axis", "Inheritance Axis"). Gate conditions and repair verbs (add/rewrite/fix) are unchanged from R4 V-05.
**Hypothesis**: R4 V-05's gate headers name the function but not the axis. The word "Axis" in the header makes the one-axis-per-gate constraint structurally visible: two headers cannot both say "Format Axis," so the model cannot collapse them. C-19 and C-20 are satisfied by labeling without any change to the gate logic.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state,
trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified; name the
spec section that is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a named
boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- 3-slot format required for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  [boundary] = named API boundary, state variable, or contract clause.
  [caller/component] = specific downstream caller or component.
  [effect] = runtime consequence.
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  All three slots must be specific -- no generic phrases.

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before starting? What breaks if initialization is
partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off and
what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery
look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

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

Check every API and service boundary: pre/postcondition symmetry, data invariants,
migration contracts. Note anywhere callee behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access
control assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings together. For patterns spanning two or more sub-skills:
- Name contributing sub-skills (at least two) and each contributor's blast radius
- Describe the compounding effect
- CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted
- Rationale: 3-slot format + provenance: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])"
- Label: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add to findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete next step naming the exact spec section, boundary, or component
a developer must address before writing implementation code.

Three gates before closing:

**Gate 1 -- Coverage Axis**: at least one spec-gap and one contract-violation present?
If either is missing, **add** one before Gate 2.

**Gate 2 -- Format Axis**: every Blast Radius Rationale uses 3-slot format with all slots
specifically named?
If any cell violates format or uses generic placeholders, **rewrite** before Gate 3.

**Gate 3 -- Inheritance Axis**: every CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
If any CROSS-SKILL finding violates the floor or lacks annotation, **fix** before closing.

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

## V-02 -- Shared Repair Verb Probe (Phrasing Register, Boundary Probe)

**Axis**: Phrasing register -- all three closing gates use the same generic repair verb ("correct") instead of axis-specific verbs (add/rewrite/fix). Gate headers are axis-labeled (from V-01) and each gate covers one axis. Tests whether C-20 requires distinct repair verbs or only independent conditionality.
**Hypothesis**: C-20 requires that each gate carry a repair verb that "names its specific axis" -- giving the model a structural cue to fire independently. The word "correct" does not name an axis: it says nothing about whether the model must insert a new row, rewrite an existing cell, or recalculate a blast radius level. Expected to FAIL C-20 because verb genericity removes the axis-identification signal even when each gate is otherwise structurally independent.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state,
trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified; name the
spec section that is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a named
boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- 3-slot format required for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  [boundary] = named API boundary, state variable, or contract clause.
  [caller/component] = specific downstream caller or component.
  [effect] = runtime consequence.
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  All three slots must be specific -- no generic phrases.

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before starting? What breaks if initialization is
partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off and
what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery
look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

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

Check every API and service boundary: pre/postcondition symmetry, data invariants,
migration contracts. Note anywhere callee behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access
control assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings together. For patterns spanning two or more sub-skills:
- Name contributing sub-skills (at least two) and each contributor's blast radius
- Describe the compounding effect
- CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted
- Rationale: 3-slot format + provenance: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])"
- Label: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add to findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete next step naming the exact spec section, boundary, or component
a developer must address before writing implementation code.

Three gates before closing:

**Gate 1 -- Coverage Axis**: at least one spec-gap and one contract-violation present?
If either is missing, **correct** the report before Gate 2.

**Gate 2 -- Format Axis**: every Blast Radius Rationale uses 3-slot format with all slots
specifically named?
If any cell violates format or uses generic placeholders, **correct** before Gate 3.

**Gate 3 -- Inheritance Axis**: every CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
If any CROSS-SKILL finding violates the floor or lacks annotation, **correct** before closing.

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

## V-03 -- Explicit One-Axis Rule Statement (Phrasing Register)

**Axis**: Phrasing register -- an explicit anti-merge rule is prepended to the closing confirmation: "Each gate covers exactly one quality axis. Do not merge axes." Gate headers and repair verbs (add/rewrite/fix) are unchanged from R4 V-05.
**Hypothesis**: R4 V-05 implies the one-axis-per-gate constraint by having three labeled gates, but never states it. A model running the skill on an ambiguous topic where format violations and inheritance violations co-occur might be tempted to address both under one correction pass. The explicit rule closes that gap: "Do not merge axes" is an unambiguous instruction that each correction loop must stay within its own axis boundary.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state,
trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified; name the
spec section that is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a named
boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- 3-slot format required for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  [boundary] = named API boundary, state variable, or contract clause.
  [caller/component] = specific downstream caller or component.
  [effect] = runtime consequence.
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  All three slots must be specific -- no generic phrases.

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before starting? What breaks if initialization is
partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off and
what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery
look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

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

Check every API and service boundary: pre/postcondition symmetry, data invariants,
migration contracts. Note anywhere callee behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access
control assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings together. For patterns spanning two or more sub-skills:
- Name contributing sub-skills (at least two) and each contributor's blast radius
- Describe the compounding effect
- CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted
- Rationale: 3-slot format + provenance: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])"
- Label: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add to findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete next step naming the exact spec section, boundary, or component
a developer must address before writing implementation code.

Three gates before closing. Each gate covers exactly one quality axis. Do not merge axes.

**Gate 1 -- Coverage**: at least one spec-gap and one contract-violation present?
If either is missing, **add** one before Gate 2.

**Gate 2 -- Format**: every Blast Radius Rationale uses 3-slot format with all slots
specifically named?
If any cell violates format or uses generic placeholders, **rewrite** before Gate 3.

**Gate 3 -- Inheritance**: every CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
If any CROSS-SKILL finding violates the floor or lacks annotation, **fix** before closing.

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

## V-04 -- Combo: Axis-Labeled Headers + Explicit Anti-Merge Rule

**Axis**: Output format (V-01 axis-labeled headers) + phrasing register (V-03 explicit anti-merge rule) at full verbosity.
**Hypothesis**: V-01 encodes the one-axis constraint structurally (each header says "Axis"), V-03 states it declaratively ("Do not merge axes"). These are orthogonal mechanisms: V-01 targets the model's structural reading of the gate layout, V-03 targets the model's instruction following at correction time. Combining them eliminates both ambiguity vectors. Full verbosity isolates whether either mechanism adds independent value or whether one subsumes the other.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state,
trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified; name the
spec section that is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a named
boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- 3-slot format required for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  [boundary] = named API boundary, state variable, or contract clause.
  [caller/component] = specific downstream caller or component.
  [effect] = runtime consequence.
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  All three slots must be specific -- no generic phrases.

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before starting? What breaks if initialization is
partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off and
what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery
look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

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

Check every API and service boundary: pre/postcondition symmetry, data invariants,
migration contracts. Note anywhere callee behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access
control assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings together. For patterns spanning two or more sub-skills:
- Name contributing sub-skills (at least two) and each contributor's blast radius
- Describe the compounding effect
- CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted
- Rationale: 3-slot format + provenance: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])"
- Label: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add to findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete next step naming the exact spec section, boundary, or component
a developer must address before writing implementation code.

Three gates before closing. Each gate covers exactly one quality axis. Do not merge axes.

**Gate 1 -- Coverage Axis**: at least one spec-gap and one contract-violation present?
If either is missing, **add** one before Gate 2.

**Gate 2 -- Format Axis**: every Blast Radius Rationale uses 3-slot format with all slots
specifically named?
If any cell violates format or uses generic placeholders, **rewrite** before Gate 3.

**Gate 3 -- Inheritance Axis**: every CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
If any CROSS-SKILL finding violates the floor or lacks annotation, **fix** before closing.

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

## V-05 -- Combo: Axis-Labeled Headers + Explicit Anti-Merge Rule + Minimal Footprint

**Axis**: Output format (V-01) + phrasing register (V-03) + minimal surface area. V-04 content in the fewest words that preserve axis-labeled headers, the explicit anti-merge rule, and all three independent correction loops with their distinct repair verbs.
**Hypothesis**: V-04's full verbosity is the reference form. V-05 is the compression test. If V-05 matches V-04 on all 20 criteria, the additional words in V-04 are noise. If V-05 drops C-19 or C-20, the omitted words were load-bearing. V-05 is the production candidate.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state,
trace-contract, trace-permissions, SYNTHESIS, Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified; name the
spec section that is silent or unclear.

**contract-violation** -- divergent assumptions between caller and callee at a named
boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- 3-slot format required for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  [boundary] = named API boundary, state variable, or contract clause.
  [caller/component] = specific downstream caller or component.
  [effect] = runtime consequence.
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  All three slots must be specific -- no generic phrases.

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases:

**INIT** -- What does `{{topic}}` need before starting? What breaks if initialization is
partial or interrupted?

**NOMINAL** -- What does normal operation look like? Where do components hand off and
what could silently go wrong?

**DEGRADED** -- What error states exist? Are they all specified? What does recovery
look like?

**TEARDOWN** -- How does `{{topic}}` finish or hand off? Is cleanup fully specified?

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

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

Check every API and service boundary: pre/postcondition symmetry, data invariants,
migration contracts. Note anywhere callee behavior differs from what callers expect.

Add each finding immediately (Sub-Skill = trace-contract, classify, assign blast radius).
If none: say so explicitly.

---

### trace-permissions

Trace the permission model: role authorization rules, field-level security, team membership
effects, sharing rules, escalation paths. Note anything the spec omits or where access
control assumptions diverge.

Add each finding immediately (Sub-Skill = trace-permissions, classify, assign blast radius).
If none: say so explicitly.

---

### Synthesis

Review all findings together. For patterns spanning two or more sub-skills:
- Name contributing sub-skills (at least two) and each contributor's blast radius
- Describe the compounding effect
- CROSS-SKILL blast radius >= max(contributing sub-skills); no downgrade permitted
- Rationale: 3-slot format + provenance: "Inherited [LEVEL] from [sub-skill-X] ([F-ID])"
- Label: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add to findings table with Sub-Skill = CROSS-SKILL

If none: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete next step naming the exact spec section, boundary, or component
a developer must address before writing implementation code.

Three gates before closing. One axis per gate. Do not merge.

**Gate 1 -- Coverage Axis**: spec-gap present? contract-violation present?
Missing: **add** one before Gate 2.

**Gate 2 -- Format Axis**: all Blast Radius Rationale cells use 3-slot format with all
slots specifically named?
Violation: **rewrite** those cells before Gate 3.

**Gate 3 -- Inheritance Axis**: all CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
Violation: **fix** blast radius and annotation before closing.

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
