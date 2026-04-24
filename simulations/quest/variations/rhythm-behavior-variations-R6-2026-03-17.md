Written to `simulations/quest/variations/rhythm-behavior-variations-R6-2026-03-17.md`.

---

## rhythm-behavior R6 Variations Summary

**New criterion**: C-21 — Axis-Labeled Gate Header Encoding (aspirational denominator 13 → 14). Pass requires the axis word in the gate header itself; positional labels ("Gate 1") fail.

**Critical observation**: R5 V-05 headers are `Gate 1 -- Coverage Axis` — the axis word IS already in the header. R5 V-05 likely already passes C-21. R6 must probe the boundary and find the strongest form.

**Variation table**:

| V | Axis | Change from R5 V-05 | Prediction |
|---|------|---------------------|-----------|
| V-01 | Output format | Append "Gate" suffix: "Gate 1 -- Coverage Axis Gate" | 100 |
| V-02 | Phrasing register (boundary probe) | Positional-only headers "Gate 1/2/3"; axis in body only | **C-21 FAIL** — 99.2 |
| V-03 | Output format (stripped) | Drop positional prefix: "**Coverage Axis Gate**" as sole header; forward refs use gate names | 100 |
| V-04 | Combo: explicit rule + V-01 | V-01 + preamble "Each gate header must name its quality axis." | 100 |
| V-05 | Combo + minimal footprint | V-03 headers (axis-only) + compressed explicit rule "Each gate header names its axis." | 100 |

**Key structural moves**:

- **V-01 vs V-05**: V-01 keeps "Gate N --" prefix for navigability; V-05 drops it entirely and uses axis-gate names as forward references. If V-05 matches V-01 on all 21 criteria, the positional prefix is decorative.
- **V-02 boundary probe**: Confirms C-21's header-location requirement. If "Gate 1" with axis in the body fails but "Coverage Axis Gate" passes, the header-vs-body distinction is load-bearing.
- **V-03 positional-stripped form**: Forward references change from "before Gate 2" to "before Format Axis Gate" — tests whether gate sequencing can be encoded by name reference alone.
- **V-04/V-05 combo**: Adds explicit declarative rule to structural encoding, same orthogonal pattern as R5 used for C-19. V-05 is the compression test and R6 production candidate if confirmed.

**Production candidate prediction**: V-05 — axis-gate headers at minimal footprint, explicit rule preserved.
 the
maximally explicit C-21 form. The positional prefix is retained for gate sequencing.

**V-02 logic**: "Gate 1" with axis in the body (e.g., "spec-gap present? -- coverage axis")
moves the axis label one level down. C-21 requires the axis label in the header. Expected
FAIL: the header contains no axis word, only a position number.

**V-03 logic**: Drop "Gate N --" entirely; use just "**Coverage Axis Gate**" as the header.
If C-18 (three gates, each axis independent) and C-19 (one axis per gate) are satisfied by
axis label + repair verb alone, the numbered prefix adds no criteria value and V-03 is the
minimal axis-gate form.

**V-04 logic**: Structural encoding (axis word in header) and declarative encoding (explicit
rule "Each gate header must name its quality axis.") target C-21 from orthogonal angles --
same mechanism V-03/V-04 used in R5 for C-19. Combining them closes both ambiguity vectors.

**V-05 logic**: V-03 stripped headers survive compression test. If V-05 matches V-04 on all
21 criteria, the explicit preamble rule is noise. If V-05 drops C-21, the explicit rule is
load-bearing even when the header format is correct.

**Predicted scores under v6 rubric** (aspirational denominator = 14):

| Variation | C-21 | Composite | Golden |
|-----------|------|-----------|--------|
| V-01 | PASS | **100** | YES |
| V-02 | **FAIL** | 99.2 | YES |
| V-03 | PASS | **100** | YES |
| V-04 | PASS | **100** | YES |
| V-05 | PASS | **100** | YES |

V-02 is the deliberate boundary probe: if it passes C-21, moving the axis label into the
gate body satisfies the header requirement and the location distinction is not load-bearing.
If it fails as predicted, the header location is independently necessary -- the axis word
in the body does not substitute for the axis word in the header.

**Open questions**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does "Coverage Axis Gate" (axis + role in header) satisfy C-21 more robustly than "Coverage Axis" alone? | V-01 | YES -- axis+role encoding is maximally self-describing; two headers cannot share a name |
| Does a positional-only header ("Gate 1") with axis in the body fail C-21? | V-02 | YES -- C-21 is location-specific; axis must appear in the header, not the body |
| Does stripping the positional prefix ("**Coverage Axis Gate**" alone) preserve all 21 criteria? | V-03 | YES -- axis label carries C-21; numbered prefix carries navigability only |
| Do structural encoding (header format) and declarative encoding (explicit rule) independently satisfy C-21, or does one subsume the other? | V-04 vs V-01/V-03 | ORTHOGONAL -- but both may be sufficient alone; combo adds redundancy, not new criteria coverage |
| Does V-05 match V-04 on all 21 criteria at minimal footprint? | V-05 vs V-04 | YES -- axis-gate headers survive compression; explicit rule is noise if headers already encode the constraint |

---

## V-01 -- Full Axis-Gate Header Naming (Output Format)

**Axis**: Output format -- gate headers upgraded from "Gate N -- Coverage Axis" to
"Gate N -- Coverage Axis Gate". The word "Gate" is added to the axis label, making each
header a self-contained descriptor of its axis and role.
**Hypothesis**: R5 V-05 headers ("Gate 1 -- Coverage Axis") already satisfy C-21 because
the axis word appears in the header. V-01 strengthens the encoding: "Coverage Axis Gate"
makes the header a complete self-description (axis = Coverage, role = Gate). Two headers
cannot both say "Coverage Axis Gate," making C-19's one-axis-per-gate constraint structurally
visible at maximum resolution. All other elements are unchanged from R5 V-05.

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

**Gate 1 -- Coverage Axis Gate**: spec-gap present? contract-violation present?
Missing: **add** one before Gate 2.

**Gate 2 -- Format Axis Gate**: all Blast Radius Rationale cells use 3-slot format with all
slots specifically named?
Violation: **rewrite** those cells before Gate 3.

**Gate 3 -- Inheritance Axis Gate**: all CROSS-SKILL blast radius >= max(contributors), with
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

---

## V-02 -- Positional-Only Headers, Axis in Body (Phrasing Register, Boundary Probe)

**Axis**: Phrasing register -- gate headers use positional labels only ("Gate 1", "Gate 2",
"Gate 3"). The axis name is moved into the gate body as a parenthetical. Tests whether
C-21's pass condition is location-specific (header only) or content-based (axis word
anywhere in the gate block).
**Hypothesis**: C-21 requires "the axis word to appear in the header itself." The header
"Gate 1" contains no axis word -- only a position number. Moving the axis label to the body
("spec-gap present? contract-violation present? -- coverage axis") does not satisfy C-21
because the pass condition is about header encoding, not gate-block content. Expected FAIL
C-21: the positional header provides no self-enforcing constraint; two "Gate N" headers can
cover the same axis without any structural signal of collision.

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

**Gate 1**: at least one spec-gap and one contract-violation present? (coverage axis)
Missing: **add** one before Gate 2.

**Gate 2**: all Blast Radius Rationale cells use 3-slot format with all slots specifically
named? (format axis)
Violation: **rewrite** those cells before Gate 3.

**Gate 3**: all CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale? (inheritance axis)
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

---

## V-03 -- Axis-Gate Headers, Positional Prefix Stripped (Output Format)

**Axis**: Output format -- the positional prefix ("Gate N --") is stripped entirely. Each
gate header is just the axis-gate label: "**Coverage Axis Gate**", "**Format Axis Gate**",
"**Inheritance Axis Gate**". Forward references within the closing confirmation also use
gate names instead of positional numbers.
**Hypothesis**: The "Gate N --" positional prefix serves navigability but carries no rubric
criteria value. C-21 passes because the axis word is in the header. C-18 passes because
three independent gates exist. C-19 passes because no two headers can share a name. C-20
passes because repair verbs (add/rewrite/fix) are unchanged. Stripping the positional prefix
reduces prompt mass without losing any criteria. If V-03 matches V-01 on all 21 criteria,
the numbered prefix is decorative and V-03 is the minimal form of C-21 compliance.

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

**Coverage Axis Gate**: spec-gap present? contract-violation present?
Missing: **add** one before Format Axis Gate.

**Format Axis Gate**: all Blast Radius Rationale cells use 3-slot format with all slots
specifically named?
Violation: **rewrite** those cells before Inheritance Axis Gate.

**Inheritance Axis Gate**: all CROSS-SKILL blast radius >= max(contributors), with
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

---

## V-04 -- Combo: Explicit Axis-Header Rule + Full Axis-Gate Naming

**Axis**: Output format (V-01 full axis-gate naming) + phrasing register (explicit
declaration "Each gate header must name its quality axis.") at full verbosity.
**Hypothesis**: V-01 encodes C-21 structurally (axis word in header). Adding an explicit
declarative rule targets C-21 from a second angle -- same orthogonal mechanism established
in R5 for C-19 (structural headers + "Do not merge axes."). Combining them closes both
ambiguity vectors: a model that misses the header format constraint is caught by the
explicit rule; a model that ignores the rule sees the constraint enforced by the header
structure. Full verbosity isolates whether either mechanism adds independent C-21 value.

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

Three gates before closing. One axis per gate. Do not merge. Each gate header must name
its quality axis.

**Gate 1 -- Coverage Axis Gate**: at least one spec-gap and one contract-violation present?
If either is missing, **add** one before Gate 2.

**Gate 2 -- Format Axis Gate**: every Blast Radius Rationale uses 3-slot format with all
slots specifically named?
If any cell violates format or uses generic placeholders, **rewrite** before Gate 3.

**Gate 3 -- Inheritance Axis Gate**: every CROSS-SKILL blast radius >= max(contributors),
with "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
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

## V-05 -- Combo: Axis-Gate Headers + Minimal Footprint

**Axis**: Output format (V-03 positional-stripped axis-gate headers) + phrasing register
(V-04 explicit axis-header rule) at minimum prompt mass.
**Hypothesis**: V-04 is the full-verbosity reference. V-05 is the compression test. The
axis-gate header form ("**Coverage Axis Gate**" alone, no positional prefix) and the
minimal preamble ("Each gate header names its axis.") must together satisfy C-21 and all
prior criteria at the same score as V-04. If V-05 matches V-04 on all 21 criteria, the
positional prefix and expanded gate phrasing in V-04 are noise. V-05 is the R6 production
candidate if confirmed.

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

Three gates before closing. One axis per gate. Do not merge. Each gate header names its axis.

**Coverage Axis Gate**: spec-gap present? contract-violation present?
Missing: **add** one before Format Axis Gate.

**Format Axis Gate**: all Blast Radius Rationale cells use 3-slot format with all slots named?
Violation: **rewrite** those cells before Inheritance Axis Gate.

**Inheritance Axis Gate**: all CROSS-SKILL blast radius >= max(contributors), with
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in rationale?
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
