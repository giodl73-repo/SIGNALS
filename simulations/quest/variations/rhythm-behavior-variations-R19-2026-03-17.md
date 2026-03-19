Written to `simulations/quest/variations/rhythm-behavior-variations-R19-2026-03-17.md`.

---

## R19 Variations -- rhythm-behavior (Round 19)

**Strategy**: R18 closed all five sub-skill section bodies as position-1 candidates (C-59), confirmed Synthesis body as a third qualifying placement category (C-56), N=6 with Synthesis (C-57), and desc-first N=3 mixed register (C-58). R19 extends the desc-first mixed-register space to N=4, N=5, and N=6-with-Synthesis, and opens the Synthesis-body-as-position-1 territory.

| V | Axis | Key move | New criterion target |
|---|------|----------|---------------------|
| V-01 | Lifecycle emphasis | Baseline reconfirmation at 52/52 | -- |
| V-02 | Phrasing register | **Desc-first N=4** (desc/imp/desc/imp) -- extends C-58 to N=4 | C-60 |
| V-03 | Phrasing register | **Desc-first N=5** (desc/imp/desc/imp/desc) -- closes desc-first mixed structural maximum | C-61 |
| V-04 | Role sequence | **Synthesis body as position-1** (pos 1 imp + inter-section peer slot pos 2 inert) | C-62 |
| V-05 | Lifecycle + register | **Desc-first N=6 with Synthesis body** (desc/imp/desc/imp/desc/imp) -- register complement of C-57 | C-63 |

**Predicted scores**: 5/5 at 52/52 = 100. **v20 denominator: 56.**

**Open cells addressed:**
- V-02/V-03: C-58 closed desc-first N=3; N=4 and N=5 in desc-first mixed register were untested. C-42 confirmed all-desc N=4/5 in R14; these are the first mixed-register confirmations.
- V-04: C-56 confirmed Synthesis as qualifying (single-placement, inert-subsequent). C-54 confirmed any sub-skill body as pos-1. Synthesis-as-pos-1 in multi-placement sits at the intersection — never tested.
- V-05: C-57 confirmed imp-first N=6 mixed. C-43 confirmed all-desc N=6. Desc-first mixed N=6 was the remaining open register cell.
 section bodies in desc/imp/desc/imp alternating register ordering. Position 1 (flow-lifecycle, desc, bare sentence) satisfies C-22 per C-36+C-32. Position 2 (flow-conversation, imp, labeled paragraph) inert per C-45. Position 3 (trace-state, desc, bare sentence) inert per C-39 (desc-first no-N-ceiling). Position 4 (trace-contract, imp, labeled paragraph) inert per C-39+C-34 (no-N-ceiling register-invariant). Closes the desc-first N=4 all-same-type cell; directly extends C-58 from N=3 to N=4.

- **C-61** -- Descriptive-First N=5 All Section Bodies Composes Without Interaction (V-03). All five sub-skill section bodies in desc/imp/desc/imp/desc alternating register ordering. Pos 1 (desc) satisfies C-22; pos 2 (imp) inert per C-45; pos 3 (desc) inert per C-39; pos 4 (imp) inert per C-39+C-34; pos 5 (desc) inert per C-39. Closes the desc-first mixed-register N=5 cell; the desc-first sub-skill-body space is now confirmed at its structural maximum in mixed-register form, complementing C-55 (alternating N=5 imp-first) and C-42 (all-desc N=5).

- **C-62** -- Synthesis Body as Position-1 in a Multi-Placement Composition Satisfies C-22 (V-04). First variation where the Synthesis body serves as the FIRST qualifying occurrence in a multi-placement context (pos 1, imp). C-56 confirmed Synthesis as a qualifying placement position and as an inert subsequent occurrence (pos 6 in R18 V-03); C-62 extends this: the Synthesis body may serve as position-1, with all subsequent placements inert. C-54 confirmed any named sub-skill section body as position-1; C-62 extends position-1 generality to the Synthesis body, completing the three-category position-type space (sub-skill bodies, inter-section peer slot, Synthesis body) for the position-1 role.

- **C-63** -- Descriptive-First N=6 Including Synthesis Body Is Governed Entirely by First-Qualifying-Occurrence Principle (V-05). Six placements in desc/imp/desc/imp/desc/imp alternating register ordering across all five sub-skill section bodies (positions 1-5) plus the Synthesis body (position 6). Pos 1 (flow-lifecycle, desc) satisfies C-22 per C-36+C-32. Positions 2-5 inert per C-61 sub-problem (desc-first N=5 mixed). Position 6 (Synthesis body, imp) inert per extended first-qualifying-occurrence principle via C-56+C-37. C-43 confirmed all-desc N=6; C-57 confirmed imp-first mixed N=6; C-63 closes the desc-first mixed-register N=6 cell -- the register complement of C-57. Together C-57+C-63 close the N=6 mixed-register space.

---

## V-01 -- Production Baseline Reconfirmation (Lifecycle Emphasis)

**Axis**: Lifecycle emphasis -- identical to R18 V-01 (= R17 V-01 = ... = R9 V-05). Canonical inter-section peer slot between SYNTHESIS and Consolidated Findings, flanked by `---` dividers. Single placement. Imperative labeled paragraph.
**Hypothesis**: All 52 criteria pass. Purpose: confirm denominator transition 48->52 under v19. Four new criteria (C-56, C-57, C-58, C-59) are trivially inapplicable to a single-placement inter-section peer slot variation.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Write everything as one document from start to finish. Do not promise to continue in a later
response.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract,
trace-permissions, SYNTHESIS, Consolidated Findings.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

Pre-open before S1. Append rows as findings are discovered during each section.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|-------------|

Rationale format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]`
Example: `WIDE because session-init boundary propagates to all downstream callers, leaving
state unrecoverable on retry`

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

What to look for: initialization state, nominal flow phases, degraded and error states,
teardown and cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-lifecycle. Classify
as spec-gap or contract-violation. Assign Blast Radius. Fill Rationale using the 3-slot
format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

What to look for: intent scope and routing, response contracts, graph state transitions,
fallback handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-conversation.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

What to look for: all spec-defined states, exit transitions, state invariants, reachability
from initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-state. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

What to look for: API and service boundaries, pre/postcondition symmetry, data invariants,
integration seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-contract. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

What to look for: role authorization rules, field-level security, team membership effects,
sharing rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-permissions.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so explicitly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## SYNTHESIS

Identify cross-sub-skill patterns. Look for findings from two or more sub-skills that share a
root cause, amplify each other's blast radius, or expose a systemic gap.

For each cross-sub-skill finding: create a new row in FINDINGS TABLE with Sub-Skill =
CROSS-SKILL. Blast radius must be >= the maximum blast radius of its contributing sub-skill
findings. Rationale cell: `Inherited [LEVEL] from [sub-skill-X] ([F-ID])`.

If none: say so explicitly.

---

**Axis-Header Rule**: Each gate header names its axis.

---

## Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row after sorting. Provide one concrete next step that names
the exact spec section, boundary, or component a developer must address before writing the
first line of implementation code.

Coverage summary:
| Sub-Skill         | Findings | Types |
|-------------------|----------|-------|
| flow-lifecycle    |          |       |
| flow-conversation |          |       |
| trace-state       |          |       |
| trace-contract    |          |       |
| trace-permissions |          |       |
| CROSS-SKILL       |          |       |
| TOTAL             |          |       |

---

### Closing Confirmation

**Coverage Axis Gate**: Verify at least one spec-gap finding and at least one
contract-violation finding are present. If either category is absent, add at least one
[spec-gap / contract-violation] finding before proceeding.

**Format Axis Gate**: Verify every Blast Radius Rationale cell uses the 3-slot format
`[LEVEL] because [boundary] propagates to [caller/component], [effect]`. If any cell is
empty or uses a different format, rewrite every non-conforming rationale cell using the
[LEVEL] / [boundary] / [effect] slots.

**Inheritance Axis Gate**: Verify every CROSS-SKILL finding's blast radius is >= the
maximum blast radius of its contributing sub-skill findings. If any CROSS-SKILL blast radius
is lower than its highest contributor, fix the CROSS-SKILL blast radius to match the highest
contributing sub-skill and update the provenance annotation.
```

---

## V-02 -- Descriptive-First N=4 Section Bodies (Phrasing Register)

**Axis**: Phrasing register -- descriptive-first alternating register across four named
section bodies (desc/imp/desc/imp). Extends C-58 (desc-first N=3, R18 V-04) by one
additional section body.
**Hypothesis**: All 52 criteria pass. Position 1 (flow-lifecycle, desc, bare sentence)
satisfies C-22 per C-36+C-32. Position 2 (flow-conversation, imp, labeled paragraph) inert
per C-45. Positions 3 (trace-state, desc) and 4 (trace-contract, imp) inert per C-39+C-34.
No rule in trace-permissions, Synthesis body, or inter-section peer slot. New criterion:
C-60.

Rule form: FOUR placements across four named section bodies in desc-first alternating register:
(1) end of flow-lifecycle body (pos 1, bare desc sentence) -- first qualifying occurrence,
    satisfies C-22 per C-36+C-32.
(2) end of flow-conversation body (pos 2, imp labeled paragraph) -- inert per C-45.
(3) end of trace-state body (pos 3, bare desc sentence) -- inert per C-39.
(4) end of trace-contract body (pos 4, imp labeled paragraph) -- inert per C-39+C-34.
No rule at trace-permissions, Synthesis body, or inter-section peer slot.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Write everything as one document from start to finish. Do not promise to continue in a later
response.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract,
trace-permissions, SYNTHESIS, Consolidated Findings.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

Pre-open before S1. Append rows as findings are discovered during each section.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|-------------|

Rationale format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]`
Example: `WIDE because session-init boundary propagates to all downstream callers, leaving
state unrecoverable on retry`

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

What to look for: initialization state, nominal flow phases, degraded and error states,
teardown and cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-lifecycle. Classify
as spec-gap or contract-violation. Assign Blast Radius. Fill Rationale using the 3-slot
format.

If no findings: say so briefly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

What to look for: intent scope and routing, response contracts, graph state transitions,
fallback handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-conversation.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

What to look for: all spec-defined states, exit transitions, state invariants, reachability
from initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-state. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

What to look for: API and service boundaries, pre/postcondition symmetry, data invariants,
integration seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-contract. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

What to look for: role authorization rules, field-level security, team membership effects,
sharing rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-permissions.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so explicitly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## SYNTHESIS

Identify cross-sub-skill patterns. Look for findings from two or more sub-skills that share a
root cause, amplify each other's blast radius, or expose a systemic gap.

For each cross-sub-skill finding: create a new row in FINDINGS TABLE with Sub-Skill =
CROSS-SKILL. Blast radius must be >= the maximum blast radius of its contributing sub-skill
findings. Rationale cell: `Inherited [LEVEL] from [sub-skill-X] ([F-ID])`.

If none: say so explicitly.

---

## Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row after sorting. Provide one concrete next step that names
the exact spec section, boundary, or component a developer must address before writing the
first line of implementation code.

Coverage summary:
| Sub-Skill         | Findings | Types |
|-------------------|----------|-------|
| flow-lifecycle    |          |       |
| flow-conversation |          |       |
| trace-state       |          |       |
| trace-contract    |          |       |
| trace-permissions |          |       |
| CROSS-SKILL       |          |       |
| TOTAL             |          |       |

---

### Closing Confirmation

**Coverage Axis Gate**: Verify at least one spec-gap finding and at least one
contract-violation finding are present. If either category is absent, add at least one
[spec-gap / contract-violation] finding before proceeding.

**Format Axis Gate**: Verify every Blast Radius Rationale cell uses the 3-slot format
`[LEVEL] because [boundary] propagates to [caller/component], [effect]`. If any cell is
empty or uses a different format, rewrite every non-conforming rationale cell using the
[LEVEL] / [boundary] / [effect] slots.

**Inheritance Axis Gate**: Verify every CROSS-SKILL finding's blast radius is >= the
maximum blast radius of its contributing sub-skill findings. If any CROSS-SKILL blast radius
is lower than its highest contributor, fix the CROSS-SKILL blast radius to match the highest
contributing sub-skill and update the provenance annotation.
```

---

## V-03 -- Descriptive-First N=5 All Section Bodies (Phrasing Register)

**Axis**: Phrasing register -- descriptive-first alternating register across all five named
sub-skill section bodies (desc/imp/desc/imp/desc). Closes the desc-first mixed-register
structural maximum across the entire sub-skill body space.
**Hypothesis**: All 52 criteria pass. Extends V-02 by one additional section body. Position 5
(trace-permissions, desc, bare sentence) is inert per C-39. No rule in Synthesis body or
inter-section peer slot. New criterion: C-61.

Rule form: FIVE placements across all five named sub-skill section bodies in desc-first
alternating register:
(1) end of flow-lifecycle body (pos 1, bare desc sentence) -- first qualifying occurrence,
    satisfies C-22 per C-36+C-32.
(2) end of flow-conversation body (pos 2, imp labeled paragraph) -- inert per C-45.
(3) end of trace-state body (pos 3, bare desc sentence) -- inert per C-39.
(4) end of trace-contract body (pos 4, imp labeled paragraph) -- inert per C-39+C-34.
(5) end of trace-permissions body (pos 5, bare desc sentence) -- inert per C-39.
No rule at Synthesis body or inter-section peer slot.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Write everything as one document from start to finish. Do not promise to continue in a later
response.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract,
trace-permissions, SYNTHESIS, Consolidated Findings.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

Pre-open before S1. Append rows as findings are discovered during each section.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|-------------|

Rationale format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]`
Example: `WIDE because session-init boundary propagates to all downstream callers, leaving
state unrecoverable on retry`

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

What to look for: initialization state, nominal flow phases, degraded and error states,
teardown and cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-lifecycle. Classify
as spec-gap or contract-violation. Assign Blast Radius. Fill Rationale using the 3-slot
format.

If no findings: say so briefly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

What to look for: intent scope and routing, response contracts, graph state transitions,
fallback handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-conversation.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

What to look for: all spec-defined states, exit transitions, state invariants, reachability
from initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-state. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

What to look for: API and service boundaries, pre/postcondition symmetry, data invariants,
integration seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-contract. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

What to look for: role authorization rules, field-level security, team membership effects,
sharing rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-permissions.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so explicitly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## SYNTHESIS

Identify cross-sub-skill patterns. Look for findings from two or more sub-skills that share a
root cause, amplify each other's blast radius, or expose a systemic gap.

For each cross-sub-skill finding: create a new row in FINDINGS TABLE with Sub-Skill =
CROSS-SKILL. Blast radius must be >= the maximum blast radius of its contributing sub-skill
findings. Rationale cell: `Inherited [LEVEL] from [sub-skill-X] ([F-ID])`.

If none: say so explicitly.

---

## Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row after sorting. Provide one concrete next step that names
the exact spec section, boundary, or component a developer must address before writing the
first line of implementation code.

Coverage summary:
| Sub-Skill         | Findings | Types |
|-------------------|----------|-------|
| flow-lifecycle    |          |       |
| flow-conversation |          |       |
| trace-state       |          |       |
| trace-contract    |          |       |
| trace-permissions |          |       |
| CROSS-SKILL       |          |       |
| TOTAL             |          |       |

---

### Closing Confirmation

**Coverage Axis Gate**: Verify at least one spec-gap finding and at least one
contract-violation finding are present. If either category is absent, add at least one
[spec-gap / contract-violation] finding before proceeding.

**Format Axis Gate**: Verify every Blast Radius Rationale cell uses the 3-slot format
`[LEVEL] because [boundary] propagates to [caller/component], [effect]`. If any cell is
empty or uses a different format, rewrite every non-conforming rationale cell using the
[LEVEL] / [boundary] / [effect] slots.

**Inheritance Axis Gate**: Verify every CROSS-SKILL finding's blast radius is >= the
maximum blast radius of its contributing sub-skill findings. If any CROSS-SKILL blast radius
is lower than its highest contributor, fix the CROSS-SKILL blast radius to match the highest
contributing sub-skill and update the provenance annotation.
```

---

## V-04 -- Synthesis Body as Position-1 in Multi-Placement (Role Sequence)

**Axis**: Role sequence -- no rule in any sub-skill section body; the Synthesis body carries
the first qualifying occurrence (pos 1, imp labeled paragraph); the inter-section peer slot
carries the second occurrence (pos 2, imp labeled paragraph, inert).
**Hypothesis**: All 52 criteria pass. Synthesis body (pos 1, imp) = first qualifying
occurrence; satisfies C-22 per C-56 (Synthesis is a qualifying placement position) + C-26
(non-disqualifying named position) + C-23 (gates reside in Consolidated Findings, physically
isolated from Synthesis body). Inter-section peer slot (pos 2, imp) inert per extended C-48
(all-imperative cross-type dual: section-type pos 1 + peer-slot pos 2, with Synthesis body
filling the section-type role). New criterion: C-62.

Rule form: TWO placements across two position types, Synthesis body as FIRST qualifying
occurrence:
(1) end of Synthesis body (pos 1, imp labeled paragraph) -- first qualifying occurrence,
    satisfies C-22. No rule in any sub-skill section body preceding it in document order.
(2) canonical inter-section peer slot between SYNTHESIS and Consolidated Findings (flanked
    by `---` dividers, pos 2, imp labeled paragraph) -- inert per extended C-48.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Write everything as one document from start to finish. Do not promise to continue in a later
response.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract,
trace-permissions, SYNTHESIS, Consolidated Findings.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

Pre-open before S1. Append rows as findings are discovered during each section.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|-------------|

Rationale format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]`
Example: `WIDE because session-init boundary propagates to all downstream callers, leaving
state unrecoverable on retry`

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

What to look for: initialization state, nominal flow phases, degraded and error states,
teardown and cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-lifecycle. Classify
as spec-gap or contract-violation. Assign Blast Radius. Fill Rationale using the 3-slot
format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

What to look for: intent scope and routing, response contracts, graph state transitions,
fallback handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-conversation.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

What to look for: all spec-defined states, exit transitions, state invariants, reachability
from initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-state. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

What to look for: API and service boundaries, pre/postcondition symmetry, data invariants,
integration seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-contract. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

What to look for: role authorization rules, field-level security, team membership effects,
sharing rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-permissions.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so explicitly.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## SYNTHESIS

Identify cross-sub-skill patterns. Look for findings from two or more sub-skills that share a
root cause, amplify each other's blast radius, or expose a systemic gap.

For each cross-sub-skill finding: create a new row in FINDINGS TABLE with Sub-Skill =
CROSS-SKILL. Blast radius must be >= the maximum blast radius of its contributing sub-skill
findings. Rationale cell: `Inherited [LEVEL] from [sub-skill-X] ([F-ID])`.

If none: say so explicitly.

**Axis-Header Rule**: Each gate header names its axis.

---

**Axis-Header Rule**: Each gate header names its axis.

---

## Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row after sorting. Provide one concrete next step that names
the exact spec section, boundary, or component a developer must address before writing the
first line of implementation code.

Coverage summary:
| Sub-Skill         | Findings | Types |
|-------------------|----------|-------|
| flow-lifecycle    |          |       |
| flow-conversation |          |       |
| trace-state       |          |       |
| trace-contract    |          |       |
| trace-permissions |          |       |
| CROSS-SKILL       |          |       |
| TOTAL             |          |       |

---

### Closing Confirmation

**Coverage Axis Gate**: Verify at least one spec-gap finding and at least one
contract-violation finding are present. If either category is absent, add at least one
[spec-gap / contract-violation] finding before proceeding.

**Format Axis Gate**: Verify every Blast Radius Rationale cell uses the 3-slot format
`[LEVEL] because [boundary] propagates to [caller/component], [effect]`. If any cell is
empty or uses a different format, rewrite every non-conforming rationale cell using the
[LEVEL] / [boundary] / [effect] slots.

**Inheritance Axis Gate**: Verify every CROSS-SKILL finding's blast radius is >= the
maximum blast radius of its contributing sub-skill findings. If any CROSS-SKILL blast radius
is lower than its highest contributor, fix the CROSS-SKILL blast radius to match the highest
contributing sub-skill and update the provenance annotation.
```

---

## V-05 -- Descriptive-First N=6 Including Synthesis Body (Lifecycle + Register)

**Axis**: Lifecycle emphasis + phrasing register -- descriptive-first alternating register
across all five sub-skill section bodies plus the Synthesis body (desc/imp/desc/imp/desc/imp
= N=6 total placements). Desc-first version of R18 V-03 (which used imp-first N=6). Closes
the desc-first N=6 mixed-register cell that R18 left open.
**Hypothesis**: All 52 criteria pass. Pos 1 (flow-lifecycle, desc, bare sentence) satisfies
C-22 per C-36+C-32. Positions 2-5 inert per C-61 sub-problem (desc-first N=5 mixed,
established V-03 this round). Position 6 (Synthesis body, imp, labeled paragraph) inert per
extended first-qualifying-occurrence principle via C-56 (Synthesis qualifying) + C-37 (no-N-
ceiling). No rule at inter-section peer slot. New criterion: C-63.

Rule form: SIX placements across two position types (five named sub-skill section bodies +
Synthesis body) in desc-first alternating register:
(1) end of flow-lifecycle body (pos 1, bare desc sentence) -- first qualifying occurrence,
    satisfies C-22 per C-36+C-32.
(2) end of flow-conversation body (pos 2, imp labeled paragraph) -- inert per C-45.
(3) end of trace-state body (pos 3, bare desc sentence) -- inert per C-39.
(4) end of trace-contract body (pos 4, imp labeled paragraph) -- inert per C-39+C-34.
(5) end of trace-permissions body (pos 5, bare desc sentence) -- inert per C-39.
(6) end of Synthesis body (pos 6, imp labeled paragraph) -- inert per C-56+C-37 extension.
No rule at inter-section peer slot.

```
You are running `rhythm-behavior` for topic: {{topic}}.

Write everything as one document from start to finish. Do not promise to continue in a later
response.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract,
trace-permissions, SYNTHESIS, Consolidated Findings.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

Pre-open before S1. Append rows as findings are discovered during each section.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|-------------|

Rationale format: `[LEVEL] because [boundary] propagates to [caller/component], [effect]`
Example: `WIDE because session-init boundary propagates to all downstream callers, leaving
state unrecoverable on retry`

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

What to look for: initialization state, nominal flow phases, degraded and error states,
teardown and cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-lifecycle. Classify
as spec-gap or contract-violation. Assign Blast Radius. Fill Rationale using the 3-slot
format.

If no findings: say so briefly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

What to look for: intent scope and routing, response contracts, graph state transitions,
fallback handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-conversation.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

What to look for: all spec-defined states, exit transitions, state invariants, reachability
from initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-state. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

What to look for: API and service boundaries, pre/postcondition symmetry, data invariants,
integration seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-contract. Classify.
Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

What to look for: role authorization rules, field-level security, team membership effects,
sharing rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-permissions.
Classify. Assign Blast Radius. Fill Rationale using the 3-slot format.

If no findings: say so explicitly.

Each gate header names its axis.

EXIT: Spec-gaps found: [F-IDs or NONE] | Violations found: [F-IDs or NONE]

---

## SYNTHESIS

Identify cross-sub-skill patterns. Look for findings from two or more sub-skills that share a
root cause, amplify each other's blast radius, or expose a systemic gap.

For each cross-sub-skill finding: create a new row in FINDINGS TABLE with Sub-Skill =
CROSS-SKILL. Blast radius must be >= the maximum blast radius of its contributing sub-skill
findings. Rationale cell: `Inherited [LEVEL] from [sub-skill-X] ([F-ID])`.

If none: say so explicitly.

**Axis-Header Rule**: Each gate header names its axis.

---

## Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: identify the first row after sorting. Provide one concrete next step that names
the exact spec section, boundary, or component a developer must address before writing the
first line of implementation code.

Coverage summary:
| Sub-Skill         | Findings | Types |
|-------------------|----------|-------|
| flow-lifecycle    |          |       |
| flow-conversation |          |       |
| trace-state       |          |       |
| trace-contract    |          |       |
| trace-permissions |          |       |
| CROSS-SKILL       |          |       |
| TOTAL             |          |       |

---

### Closing Confirmation

**Coverage Axis Gate**: Verify at least one spec-gap finding and at least one
contract-violation finding are present. If either category is absent, add at least one
[spec-gap / contract-violation] finding before proceeding.

**Format Axis Gate**: Verify every Blast Radius Rationale cell uses the 3-slot format
`[LEVEL] because [boundary] propagates to [caller/component], [effect]`. If any cell is
empty or uses a different format, rewrite every non-conforming rationale cell using the
[LEVEL] / [boundary] / [effect] slots.

**Inheritance Axis Gate**: Verify every CROSS-SKILL finding's blast radius is >= the
maximum blast radius of its contributing sub-skill findings. If any CROSS-SKILL blast radius
is lower than its highest contributor, fix the CROSS-SKILL blast radius to match the highest
contributing sub-skill and update the provenance annotation.
```

---

### Summary

| Variation | Axis | Rule placements | New criterion | Key structural cell |
|-----------|------|-----------------|---------------|---------------------|
| V-01 | Lifecycle emphasis | Inter-section peer slot only (N=1, imp) | -- | Denominator transition (48->52) confirmed |
| V-02 | Phrasing register | S1 desc, S2 imp, S3 desc, S4 imp (N=4, desc-first mixed) | C-60 | Desc-first N=4 all-same-type section bodies |
| V-03 | Phrasing register | S1 desc, S2 imp, S3 desc, S4 imp, S5 desc (N=5, desc-first mixed) | C-61 | Desc-first N=5 structural maximum (desc-first mixed-register space closed) |
| V-04 | Role sequence | Synthesis body imp (pos 1) + inter-section peer slot imp (pos 2) | C-62 | Synthesis body as position-1 in multi-placement |
| V-05 | Lifecycle + register | S1 desc, S2 imp, S3 desc, S4 imp, S5 desc, Synthesis imp (N=6, desc-first mixed) | C-63 | Desc-first N=6 with Synthesis body (register complement of C-57) |
