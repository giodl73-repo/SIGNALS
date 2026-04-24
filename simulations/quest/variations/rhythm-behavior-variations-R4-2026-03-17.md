Written to `simulations/quest/variations/rhythm-behavior-variations-R4-2026-03-17.md`.

---

## rhythm-behavior -- Round 4 Variations

**C-18 gap diagnosis**: R3 V-05's closing confirmation lists all three quality gates but fires a correction loop only for Gate 1 (coverage). Gates 2 (format) and 3 (inheritance) have no explicit correction instruction. C-18 requires each gate to trigger a correction loop on failure.

| # | Axis | Key Change | C-18 Target |
|---|------|-----------|-------------|
| **V-01** | Output format | Three numbered labeled gate blocks, each self-contained with header + condition + correction loop | C-18 via structural separation |
| **V-02** | Output format (compact) | Gates 2+3 merged into one compound structural gate; **tests the boundary**: does a compound loop satisfy "each triggers a correction loop"? | Expected C-18 FAIL -- confirms the boundary |
| **V-03** | Phrasing register | Flat checklist retained; each gate uses distinct repair verb: `add` (coverage), `rewrite` (format), `fix` (inheritance) | C-18 via imperative verb differentiation |
| **V-04** | Combo: format + register | V-01 labeled gates + V-03 repair verbs at full verbosity | C-18 via structure + verb precision |
| **V-05** | Combo + minimal footprint | V-04 compressed; all three loops and verbs preserved at minimum mass | C-18 + production candidate |

**Key hypotheses**:

- **V-01**: A flat checklist with one trailing correction clause is syntactically ambiguous about which items it covers. Labeled blocks make each loop unambiguous — the model cannot read Gate 2 as "confirm only."
- **V-02**: Deliberately tests whether a compound Gate 2+3 loop satisfies C-18's "each triggers a correction loop." Expected to fail C-18 because merging the format and inheritance axes into one gate collapses them — two gates is not three.
- **V-03**: "Find" is wrong for format violations (the finding exists; the cell needs rewriting) and inheritance violations (the level needs recalculation). Correct repair verbs reduce model ambiguity about what the correction produces.
- **V-04**: Structure (V-01) and verb precision (V-03) are orthogonal — both eliminated simultaneously without interference.
- **V-05**: V-04 at minimal prompt mass. If it matches V-04 on all 18 criteria, it's the deployment recommendation.

**Predicted scores under v4 rubric** (aspirational denominator = 11):

| V | C-16 | C-17 | C-18 | Composite |
|---|------|------|------|-----------|
| V-01 | PASS | PASS | PASS | **100** |
| V-02 | PASS | PASS | **FAIL** | 99 |
| V-03 | PASS | PASS | PASS | **100** |
| V-04 | PASS | PASS | PASS | **100** |
| V-05 | PASS | PASS | PASS | **100** |

V-02 is the deliberate boundary probe: if it actually passes C-18, the compound gate interpretation is valid and it becomes an even simpler production form. If it fails as predicted, the three-gates-must-be-three-loops interpretation is confirmed and V-05 is the recommendation.
sity isolates whether either axis is load-bearing.

- **V-05**: Both improvements from V-04 survive at minimal prompt mass. If V-05 matches V-04 on all 18 criteria, it is the deployment recommendation.

**Predicted scores** (v4 rubric, aspirational denominator = 11):

| Variation | C-16 | C-17 | C-18 | Predicted Composite |
|-----------|------|------|------|---------------------|
| V-01 | PASS | PASS | PASS | 100 |
| V-02 | PASS | PASS | DEPENDS on C-18 compound interpretation | 99 or 100 |
| V-03 | PASS | PASS | PASS | 100 |
| V-04 | PASS | PASS | PASS | 100 |
| V-05 | PASS | PASS | PASS | 100 |

**Open questions:**

| Question | V | Hypothesis |
|----------|---|-----------|
| Does a labeled gate block make each correction loop unambiguous? | V-01, V-04 | YES -- label + condition + correction in one block is syntactically unambiguous vs trailing catch-all |
| Does a compound gate covering Gates 2+3 satisfy C-18's "each triggers a correction loop"? | V-02 | NO -- C-18 defines three axes; a compound gate collapses them into one, which misses the "each" requirement |
| Do repair verb differences (add/rewrite/fix) change model behavior relative to a generic "go back"? | V-03, V-04, V-05 | YES -- "rewrite" directs the model to transform an existing cell; "fix" directs recalculation; "add" directs insertion; generic "go back" is ambiguous about the repair target |
| Does V-05 match V-04 on all 18 criteria at minimal footprint? | V-05 vs V-04 | YES -- structural mechanisms survive compression |

---

## V-01 -- Labeled Gate Blocks (Output Format)

**Axis**: Output format -- closing confirmation restructured from a flat checklist with one trailing correction clause into three labeled gate blocks, each self-contained with a header, a condition, and a dedicated correction loop.
**Hypothesis**: A flat checklist followed by "If either category is missing, go back..." is syntactically ambiguous: "either category" refers only to gate 1 items, and the model has no structural cue that gates 2 and 3 also have correction loops. Numbered labeled blocks make each gate's correction instruction unambiguous -- the model cannot read gate 2 as "confirm only, no correction required."

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

---

### What to look for

A **spec-gap** is a requirement that is missing, ambiguous, or underspecified. When you
find one, say which section of the spec is silent or unclear.

A **contract-violation** is a case where a caller and a callee have divergent assumptions
at a boundary. When you find one, name the boundary.

**Blast radius** describes propagation scope if the problem ships unaddressed:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- for each finding, use this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: the named API boundary, state variable, or contract clause (e.g.,
    `session-sequence-number contract`)
  - [caller/component]: the specific downstream caller or component (e.g.,
    `flow-conversation routing, trace-contract pre-check`)
  - [effect]: the runtime consequence (e.g., `producing stale-state errors at both`)
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  Do not use generic phrases -- every slot must name a specific element from this topic.

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

For each issue, add a row to the findings table (Sub-Skill = flow-lifecycle), classify it
as a spec-gap or contract-violation, and assign a blast radius.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow intent routing paths,
response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation).

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace valid
transitions, check reachability from the initial state, and look for unauthorized crossings.
An unauthorized crossing is a contract-violation by default. Add each finding to the table
(Sub-Skill = trace-state).

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract).

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions).

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each contributor
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: CROSS-SKILL blast radius >= max(contributing sub-skills).
  No downgrade from the highest contributor is permitted. If the combination opens scope
  not reached by any single contributor, assign the next higher level.
- Write a Blast Radius Rationale in 3-slot format, appending a provenance annotation:
  "[LEVEL] because [cross-skill boundary] propagates to [cross-skill callers/components],
  [effect]. Inherited [LEVEL] from [sub-skill-X] ([F-ID])."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

The first finding in the sorted list gets one concrete, specific next step that a developer
can execute before writing the first line of implementation code. Name the exact spec
section, boundary, or component -- not a generic directive.

Before you close, run the following three gates in order. Each gate has its own correction
instruction -- do not skip a gate and do not combine corrections.

**Gate 1 -- Coverage**
Does the report contain at least one spec-gap and at least one contract-violation?
If either category is absent, go back and find at least one before continuing to Gate 2.

**Gate 2 -- Rationale Format**
Does every Blast Radius Rationale cell use the "[LEVEL] because [boundary] propagates to
[caller/component], [effect]" format, with all three slots filled by named, specific elements?
If any cell is missing a slot, uses a generic placeholder, or is blank, rewrite those cells
before continuing to Gate 3.

**Gate 3 -- Inheritance Compliance**
Does every CROSS-SKILL finding's blast radius equal or exceed the highest contributor's
blast radius? Does every CROSS-SKILL rationale include "Inherited [LEVEL] from [sub-skill-X]
([F-ID])"?
If any CROSS-SKILL finding violates the floor or lacks the provenance annotation, fix it
before closing.

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

## V-02 -- Compound Structural Gate (Output Format, Compact)

**Axis**: Output format (compact) -- Gates 2 and 3 merged into one "structural quality" compound gate with a single correction loop. Gate 1 (coverage) keeps its own correction loop. Tests whether a two-gate closing confirmation satisfies C-18's "each triggers a correction loop on failure."
**Hypothesis**: C-18 defines three independent quality axes. Merging Gates 2 and 3 into one compound gate yields two gates total, not three. A compound gate covering "all structural rules" cannot satisfy "each [of three gates] triggers a correction loop" because it collapses the format axis and the inheritance axis into one check. This variation exists to confirm the failure prediction: V-02 is expected to fail C-18 if C-18 requires strictly independent loops per axis, and to pass if C-18 accepts a compound loop as covering both.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

---

### What to look for

A **spec-gap** is a requirement that is missing, ambiguous, or underspecified. When you
find one, say which section of the spec is silent or unclear.

A **contract-violation** is a case where a caller and a callee have divergent assumptions
at a boundary. When you find one, name the boundary.

**Blast radius** describes propagation scope if the problem ships unaddressed:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- for each finding, use this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: the named API boundary, state variable, or contract clause
  - [caller/component]: the specific downstream caller or component
  - [effect]: the runtime consequence
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."

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

For each issue, add a row to the findings table (Sub-Skill = flow-lifecycle), classify it
as a spec-gap or contract-violation, and assign a blast radius.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow intent routing paths,
response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation).

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace valid
transitions, check reachability from the initial state, and look for unauthorized crossings.
An unauthorized crossing is a contract-violation by default. Add each finding to the table
(Sub-Skill = trace-state).

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract).

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions).

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each contributor
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: CROSS-SKILL blast radius >= max(contributing sub-skills).
  No downgrade from the highest contributor is permitted.
- Write a Blast Radius Rationale using the 3-slot format with provenance annotation:
  "[LEVEL] because [cross-skill boundary] propagates to [callers/components], [effect].
  Inherited [LEVEL] from [sub-skill-X] ([F-ID])."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

The first finding in the sorted list gets one concrete, specific next step that a developer
can execute before writing the first line of implementation code. Name the exact spec
section, boundary, or component -- not a generic directive.

Before you close, run this two-gate check:

**Gate 1 -- Coverage**
Does the report contain at least one spec-gap and at least one contract-violation?
If either is absent, go back and find at least one before continuing.

**Gate 2 -- Structural Quality** (format + inheritance, checked together)
(a) Does every Blast Radius Rationale use the "[LEVEL] because [boundary] propagates to
[caller/component], [effect]" format with all three slots specifically named?
(b) Does every CROSS-SKILL finding's blast radius equal or exceed the highest contributor's
blast radius, with "Inherited [LEVEL] from [sub-skill-X] ([F-ID])" in the rationale?
If (a) or (b) fails, fix all non-conforming entries before closing.

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

## V-03 -- Repair Verb Differentiation (Phrasing Register)

**Axis**: Phrasing register -- each closing gate uses the repair verb that matches its required action: `add` for missing findings (coverage), `rewrite` for non-conforming rationale cells (format), `fix` for blast radius miscalculation (inheritance). The flat checklist structure from R3 V-05 is retained; only the correction instructions change.
**Hypothesis**: R3 V-05 fires "go back and find at least one" for the coverage correction loop. This verb ("find") is correct for coverage: the model must locate a finding it missed. But "find" is wrong for format violations (the finding exists; the rationale cell needs to be rewritten) and for inheritance violations (the blast radius level needs to be recalculated). Using `rewrite` and `fix` as distinct repair verbs gives the model unambiguous instructions about what the correction produces. This reduces the risk of a model "finding" an additional finding instead of rewriting an existing rationale.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

---

### What to look for

A **spec-gap** is a requirement that is missing, ambiguous, or underspecified. When you
find one, say which section of the spec is silent or unclear.

A **contract-violation** is a case where a caller and a callee have divergent assumptions
at a boundary. When you find one, name the boundary.

**Blast radius** describes propagation scope if the problem ships unaddressed:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- for each finding, use this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: the named API boundary, state variable, or contract clause
  - [caller/component]: the specific downstream caller or component
  - [effect]: the runtime consequence
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  Do not use generic phrases -- every slot must name a specific element from this topic.

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

For each issue, add a row to the findings table (Sub-Skill = flow-lifecycle), classify it
as a spec-gap or contract-violation, and assign a blast radius.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow intent routing paths,
response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation).

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace valid
transitions, check reachability from the initial state, and look for unauthorized crossings.
An unauthorized crossing is a contract-violation by default. Add each finding to the table
(Sub-Skill = trace-state).

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract).

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions).

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each contributor
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: CROSS-SKILL blast radius >= max(contributing sub-skills).
  No downgrade from the highest contributor is permitted.
- Write a Blast Radius Rationale using the 3-slot format with provenance annotation:
  "[LEVEL] because [cross-skill boundary] propagates to [callers/components], [effect].
  Inherited [LEVEL] from [sub-skill-X] ([F-ID])."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

The first finding in the sorted list gets one concrete, specific next step that a developer
can execute before writing the first line of implementation code. Name the exact spec
section, boundary, or component -- not a generic directive.

Before you close, confirm all three:

- At least one finding is a spec-gap and at least one is a contract-violation.
  If either category is missing, **add** at least one before continuing.

- Every Blast Radius Rationale cell uses the "[LEVEL] because [boundary] propagates to
  [caller/component], [effect]" format with all three slots specifically named.
  If any cell fails this format, **rewrite** those cells before continuing.

- Every CROSS-SKILL finding's blast radius is >= the highest contributing sub-skill's
  blast radius, and its rationale includes "Inherited [LEVEL] from [sub-skill-X] ([F-ID])".
  If any CROSS-SKILL finding violates the floor or lacks the annotation, **fix** it before
  closing.

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

## V-04 -- Combo: Labeled Gates + Repair Verb Differentiation

**Axis**: Output format (V-01 labeled blocks) + phrasing register (V-03 repair verbs) at full verbosity.
**Hypothesis**: V-01 provides structural clarity (each gate is an unambiguous self-contained block) and V-03 provides verb precision (each correction instruction names the right repair action). These are orthogonal: V-01 targets model attention (does it see three separate loops?), V-03 targets model behavior (does it know what to produce?). Combining them eliminates both ambiguity vectors. Full verbosity isolates whether either axis adds independent value or whether one suffices.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Output: a single continuous simulation findings report saved as
`simulations/campaign/{{topic}}-simulate-{{date}}.md`.

Write everything as one document from start to finish. Do not promise to continue.

The report runs five simulation sections in this exact order:
  flow-lifecycle, then flow-conversation, then trace-state, then trace-contract,
  then trace-permissions, then a SYNTHESIS section, then a consolidated findings section.

---

### What to look for

A **spec-gap** is a requirement that is missing, ambiguous, or underspecified. When you
find one, say which section of the spec is silent or unclear.

A **contract-violation** is a case where a caller and a callee have divergent assumptions
at a boundary. When you find one, name the boundary.

**Blast radius** describes propagation scope if the problem ships unaddressed:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- for each finding, use this exact format:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  - [boundary]: the named API boundary, state variable, or contract clause (e.g.,
    `session-sequence-number contract`)
  - [caller/component]: the specific downstream caller or component (e.g.,
    `flow-conversation routing, trace-contract pre-check`)
  - [effect]: the runtime consequence (e.g., `producing stale-state errors at both`)
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."
  Do not use generic phrases -- every slot must name a specific element from this topic.

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

For each issue, add a row to the findings table (Sub-Skill = flow-lifecycle), classify it
as a spec-gap or contract-violation, and assign a blast radius.

If you find nothing in a phase, say so briefly (e.g., "INIT: no findings").

---

### flow-conversation

Walk through the conversation and intent flow for `{{topic}}`. Follow intent routing paths,
response contracts, graph transitions, fallback branches, session state tracking, and
timeout handling. Note anything the spec leaves unclear or where caller and callee would
disagree. Add each finding to the table (Sub-Skill = flow-conversation).

If you find no issues, say so explicitly.

---

### trace-state

Build the complete state model for `{{topic}}`. List every spec-defined state, trace valid
transitions, check reachability from the initial state, and look for unauthorized crossings.
An unauthorized crossing is a contract-violation by default. Add each finding to the table
(Sub-Skill = trace-state).

If you find no issues, say so explicitly.

---

### trace-contract

Check the behavioral contracts for `{{topic}}`. Examine every API or service boundary,
verify that pre and postconditions are symmetric, check data invariants and migration
contracts. Note anywhere the callee's behavior differs from what callers expect. Add each
finding to the table (Sub-Skill = trace-contract).

If you find no issues, say so explicitly.

---

### trace-permissions

Trace the permission model for `{{topic}}`. Check role authorization rules, field-level
security, team membership effects, sharing rules, and escalation paths. Note anything the
spec omits or where access control assumptions diverge. Add each finding to the table
(Sub-Skill = trace-permissions).

If you find no issues, say so explicitly.

---

### Synthesis

Review all findings across the five sub-skills together. Look for patterns or compounding
risks that only become visible when results from multiple sub-skills are read together.

For each cross-sub-skill pattern found:
- Name the contributing sub-skills (at least two) and the blast radius of each contributor
- Describe the relationship or compounding effect
- **Blast Radius Inheritance Rule**: CROSS-SKILL blast radius >= max(contributing sub-skills).
  No downgrade from the highest contributor is permitted. If the combination opens scope
  not reached by any single contributor, assign the next higher level and explain why.
- Write a Blast Radius Rationale in 3-slot format with provenance annotation:
  "[LEVEL] because [cross-skill boundary] propagates to [cross-skill callers/components],
  [effect]. Inherited [LEVEL] from [sub-skill-X] ([F-ID])."
- Label it: "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- Add it to the findings table with Sub-Skill = CROSS-SKILL

If no patterns exist, state: "Synthesis: no cross-sub-skill patterns found."

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last) and reproduce it here.
Label the sort: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

The first finding in the sorted list gets one concrete, specific next step that a developer
can execute before writing the first line of implementation code. Name the exact spec
section, boundary, or component -- not a generic directive.

Before you close, run the following three gates in order. Each has its own repair
instruction. Do not combine or skip.

**Gate 1 -- Coverage**
Does the report contain at least one finding classified as a spec-gap and at least one
classified as a contract-violation?
If either category is absent, **add** at least one finding of that type before Gate 2.

**Gate 2 -- Rationale Format**
Does every Blast Radius Rationale cell use the "[LEVEL] because [boundary] propagates to
[caller/component], [effect]" format, with [boundary], [caller/component], and [effect]
each filled by a named, specific element (not a generic phrase)?
If any cell violates the format or leaves a slot generic, **rewrite** those cells before
Gate 3.

**Gate 3 -- Inheritance Compliance**
Does every CROSS-SKILL finding's blast radius equal or exceed the highest contributor's
blast radius? Does every CROSS-SKILL rationale include the provenance annotation
"Inherited [LEVEL] from [sub-skill-X] ([F-ID])"?
If any CROSS-SKILL finding violates the floor or lacks the annotation, **fix** the blast
radius and rationale before closing.

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

## V-05 -- Combo: Labeled Gates + Repair Verb Differentiation + Minimal Footprint

**Axis**: Output format (V-01) + phrasing register (V-03) + minimal surface area. V-04 content in the fewest words that preserve all three independent correction loops with their distinct repair verbs.
**Hypothesis**: V-04's full verbosity is the reference form. V-05 is the compression test. If V-05 matches V-04 on all 18 criteria, the additional words in V-04 are noise. If V-05 drops any criterion, the omitted words were load-bearing. V-05 is the production candidate.

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
