Written to `simulations/quest/variations/rhythm-behavior-variations-R15-2026-03-17.md`.

---

## R15 Summary

**Strategy**: Close the last untested position-type x register cell, then probe mixed-register and cross-type dual placements. All 5 predicted 36/36.

| V | Axis | Key move |
|---|------|----------|
| V-01 | Lifecycle emphasis | Baseline reconfirmation at new denominator 36/36 |
| V-02 | Register | Descriptive register + inter-section peer slot -- **first test of this combination** |
| V-03 | Register + lifecycle | Mixed register N=2: descriptive at position 1, imperative at position 2 |
| V-04 | Register + lifecycle | Mixed register N=2: imperative at position 1, descriptive at position 2 |
| V-05 | Register + lifecycle | Cross-type dual: section body (descriptive, pos 1) + inter-section peer slot (descriptive) |

---

### Open questions for R15

| Question | V | Hypothesis |
|----------|---|-----------|
| Does descriptive register at the inter-section peer slot satisfy C-22? | V-02 | YES -- C-34 register invariance + C-23 isolation primacy |
| Does C-38 cover the cross-register case (descriptive first, imperative subsequent)? | V-03 | YES -- C-38 states "any subsequent qualifying placement is inert"; register of subsequent not restricted |
| Does C-33 + C-34 cover imperative first + descriptive subsequent? | V-04 | YES -- C-33 inertness + C-34 register invariance; second placement inert regardless of register |
| Does inertness extend across position types (section body + inter-section peer slot)? | V-05 | YES -- general first-qualifying-occurrence principle; position type does not affect inertness |

---

### New criteria predicted from R15

- **C-44** (format, R15): Descriptive Register in Inter-Section Peer Slot Is a Qualifying Position for C-22 -- V-02
- **C-45** (format, R15): Mixed-Register Dual Section-Body (Descriptive First, Imperative Subsequent) Composes Without Interaction -- V-03
- **C-46** (format, R15): Mixed-Register Dual Section-Body (Imperative First, Descriptive Subsequent) Composes Without Interaction -- V-04
- **C-47** (format, R15): Cross-Type Dual Placement (Section Body + Inter-Section Peer Slot, Descriptive) Composes Without Interaction -- V-05

v16 denominator would be **40**.

---

### Design rationale

R14 closed every N-count (1--6) in both registers, and every named section body individually and in combination. The one remaining untested cell in the position-type x register matrix was **descriptive register + inter-section peer slot** -- the canonical C-22 position had only been tested in imperative. V-02 closes that cell.

V-03 and V-04 are the first mixed-register dual section-body tests. All prior multi-body tests used uniform register. C-38 predicts V-03 passes (descriptive-first inertness covers any subsequent register). C-33+C-34 predict V-04 passes (imperative-first inertness + register invariance). These are the reverse complements of each other.

V-05 breaks the same-position-type constraint: all prior multi-placement tests used placements from the same class (all section bodies, or all inter-section slots). V-05 combines one section body (pos 1, descriptive) with the inter-section peer slot (descriptive), testing whether the inertness principle crosses position-type boundaries. V-02 confirms the inter-section slot works as a sole qualifying placement; V-05 tests it as a secondary (inert) placement.
ition types. C-34 (register invariance) and the underlying "first qualifying occurrence satisfies; subsequent are inert" principle predict this composes without interaction.

**Open questions for R15:**

| Question | V | Hypothesis |
|----------|---|-----------|
| Does descriptive register in the inter-section peer slot satisfy C-22? | V-02 | YES -- C-34 register invariance + C-23 isolation primacy; no proximity or label constraint |
| Does C-38 extend to the cross-register case (descriptive first, imperative subsequent)? | V-03 | YES -- C-38 states "any subsequent qualifying placement is inert"; register of subsequent is not restricted |
| Does C-33 + C-34 cover imperative first + descriptive subsequent dual section body? | V-04 | YES -- C-33 inertness + C-34 register invariance; second placement inert regardless of register |
| Does the inertness principle apply across position types (section body + inter-section peer slot)? | V-05 | YES -- general "first qualifying occurrence satisfies; subsequent are inert" principle; position type does not affect inertness |

**Predicted scores under v15 rubric** (aspirational denominator = 36):

| Variation | C-41 | C-42 | C-43 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| V-01 | PASS (N=1 inter-section slot; trivial) | PASS (N=1; no descriptive section body) | PASS (N=1; no descriptive N=6) | **100** | YES |
| V-02 | PASS (N=1; no section body; trivial) | PASS (N=1; no N=4/5 descriptive section body) | PASS (N=1; trivial) | **100** | YES |
| V-03 | PASS (N=2 bodies; N=6 ceiling criterion trivially inapplicable) | PASS (N=2; N=4/5 descriptive criteria trivially inapplicable) | PASS (N=2; trivial) | **100** | YES |
| V-04 | PASS (N=2 bodies; trivial) | PASS (N=2; trivial) | PASS (N=2; trivial) | **100** | YES |
| V-05 | PASS (N=2 total, cross-type; trivial) | PASS (N=1 section body; trivial) | PASS (N=1 section body + 1 inter-section slot; trivial) | **100** | YES |

---

## V-01 -- Production Baseline at 36/36 (Lifecycle Emphasis, Reconfirmation)

**Axis**: Lifecycle emphasis -- identical to R14 V-01 (= R13 V-01 = R12 V-01 = R11 V-01 = R10
V-01 = R9 V-05): minimal form, labeled paragraph `**Axis-Header Rule**: Each gate header names
its axis.` in the confirmed inter-section peer slot between Synthesis and Consolidated Findings,
flanked by `---` dividers. Single placement. All elements in imperative register.

**Hypothesis**: R14 V-01 scored 33/33 under v14. Under v15 the three new criteria (C-41,
C-42, C-43) encode R14 findings directly:
- C-41 passes: no N=6 section-body composition; rule is at inter-section peer slot. C-41 fires
  only on placements that include the Synthesis body as a 6th section-body position -- trivially
  inapplicable.
- C-42 passes: no descriptive N=4 or N=5 section-body composition. C-42 fires on
  descriptive register at N=4 and N=5 sub-skill body counts -- trivially inapplicable.
- C-43 passes: no descriptive + N=6 composition. C-43 fires on the absolute structural maximum
  in descriptive register -- trivially inapplicable.
Expected: 36/36 = 100, golden.

**Novelty verification**: Exact re-run of R14 V-01. Purpose is denominator transition
verification (33->36) under v15. Not structurally new; new only as reconfirmation at v15.

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
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases: INIT (preconditions and partial-init failures),
NOMINAL (component handoffs and silent failures), DEGRADED (error states and recovery),
TEARDOWN (cleanup and handoff completeness).

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

**Axis-Header Rule**: Each gate header names its axis.

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort the findings table by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: one concrete next step naming the exact spec section, boundary, or component
a developer must address before writing the first line of implementation code.

Three gates before closing. One axis per gate. Do not merge.

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

---

## V-02 -- Descriptive Register + Inter-Section Peer Slot (Register, Single Axis)

**Axis**: Phrasing register -- the entire prompt is written in descriptive register AND the
axis-header rule is placed in the canonical inter-section peer slot (between Synthesis and
Consolidated Findings, flanked by `---` dividers) as a bare standalone descriptive sentence:
"Each closing confirmation gate header names its axis." No rule appears in any named section
body. Single placement only.

**Hypothesis**: C-34 states that all aspirational criteria are structure-sensitive, not
register-sensitive: descriptive phrasing that preserves all required structural elements
scores identically to imperative phrasing. C-23 states that the qualifying condition for
C-22 is physical isolation from gate bodies and example blocks -- not the presence of a named
label prefix. The inter-section peer slot is a confirmed qualifying position (R6-R8, C-24) in
imperative register; C-34 extends this to descriptive register without modification. The bare
standalone descriptive sentence, flanked by `---` dividers and separated from surrounding
content by blank lines, satisfies C-22's isolation requirement per C-23. First test of
descriptive register at the inter-section peer slot. Expected: 36/36 = 100, golden.

**Novelty verification**: All prior inter-section peer slot tests (R6-R8) used imperative
register. All descriptive-register tests (R12-R14) used named section bodies. The intersection
(descriptive + inter-section peer slot) has never been tested. Genuinely new: first confirmation
that C-34 register invariance extends to the inter-section peer slot position.

```
This is `rhythm-behavior` running for topic: {{topic}}.

The output is a single continuous simulation findings report written to
`simulations/campaign/{{topic}}-simulate-{{date}}.md`. The entire report is
produced as one document from start to finish, without any promise of continuation.

The report proceeds through these sections in sequence: flow-lifecycle,
flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS,
Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified. The specific
spec section that is silent or unclear is named in the finding.

**contract-violation** -- a divergence in assumptions between caller and callee at a
named boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- the 3-slot format is used for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."

The findings table is opened before flow-lifecycle begins. Rows are appended as each
finding is discovered. The Blast Radius Rationale column is populated for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

The flow-lifecycle section traces `{{topic}}` through its full operational lifecycle
across four phases: INIT (preconditions and partial-init failures), NOMINAL (component
handoffs and silent failures), DEGRADED (error states and recovery), and TEARDOWN
(cleanup and handoff completeness).

Findings are appended to the table as they are discovered (Sub-Skill = flow-lifecycle,
finding type classified, blast radius assigned). Any phase that produces no findings is
noted as such.

---

### flow-conversation

The flow-conversation section examines the conversation and intent flow for `{{topic}}`:
intent routing paths, response contracts, graph transitions, fallback branches, session
state tracking, and timeout handling. Anything the spec leaves unclear, or where caller
and callee assumptions would diverge, is recorded as a finding.

Findings are appended as discovered (Sub-Skill = flow-conversation). If this section
produces no findings, that is stated explicitly.

---

### trace-state

The trace-state section constructs the complete state model for `{{topic}}`: spec-defined
states, valid transitions, reachability from the initial state, and unauthorized state
crossings (classified as contract-violation by default).

Findings are appended as discovered (Sub-Skill = trace-state). If this section produces
no findings, that is stated explicitly.

---

### trace-contract

The trace-contract section examines every API and service boundary: pre/postcondition
symmetry, data invariants, and migration contracts. Any location where callee behavior
differs from what callers expect is recorded as a finding.

Findings are appended as discovered (Sub-Skill = trace-contract). If this section produces
no findings, that is stated explicitly.

---

### trace-permissions

The trace-permissions section traces the permission model: role authorization rules,
field-level security, team membership effects, sharing rules, and escalation paths.
Anything the spec omits, or where access control assumptions diverge, is recorded
as a finding.

Findings are appended as discovered (Sub-Skill = trace-permissions). If this section
produces no findings, that is stated explicitly.

---

### Synthesis

The Synthesis section reviews all findings collectively. For patterns that span two or
more sub-skills:
- The contributing sub-skills are named (at least two) along with each contributor's
  blast radius
- The compounding effect is described
- The CROSS-SKILL blast radius is >= max(contributing sub-skills); no downgrade from
  the highest contributor is permitted
- The rationale uses the 3-slot format plus provenance: "Inherited [LEVEL] from
  [sub-skill-X] ([F-ID])"
- The finding is labeled "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- The finding is inserted into the findings table with Sub-Skill = CROSS-SKILL

If no cross-skill patterns are present: "Synthesis: no cross-sub-skill patterns found."

---

Each closing confirmation gate header names its axis.

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

The findings table is sorted by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: a concrete next step naming the exact spec section, boundary, or component
a developer must address before writing any implementation code.

Three confirmation gates follow, one axis per gate, not merged.

**Coverage Axis Gate**: Confirms that at least one spec-gap finding and at least one
contract-violation finding are present in the report. If either category is absent,
add the missing finding before proceeding to the Format Axis Gate.

**Format Axis Gate**: Confirms that every Blast Radius Rationale cell uses the 3-slot
format with all three slots named. Any cell that does not conform is rewritten using
the [LEVEL] / [boundary] / [caller/component] / [effect] structure before proceeding
to the Inheritance Axis Gate.

**Inheritance Axis Gate**: Confirms that every CROSS-SKILL blast radius is >= max of
the contributing sub-skills, and that the rationale carries "Inherited [LEVEL] from
[sub-skill-X] ([F-ID])". Any finding that fails this check has its CROSS-SKILL blast
radius and provenance annotation corrected before closing.

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

## V-03 -- Mixed Register N=2: Descriptive at Position 1, Imperative at Position 2 (Register + Lifecycle)

**Axis**: Phrasing register + lifecycle emphasis -- the overall prompt is in imperative register
(identical to V-01 baseline structure) with the axis-header rule placed in TWO named section
bodies at DIFFERENT registers: (1) end of flow-lifecycle body (position 1) as a descriptive
sentence: "The closing confirmation gates are each labeled with a header that names the axis
they check." and (2) end of flow-conversation body (position 2) as an imperative labeled
paragraph: `**Axis-Header Rule**: Each gate header names its axis.` No rule appears at
positions 3-6 or the inter-section peer slot.

**Hypothesis**: The flow-lifecycle body placement (descriptive, position 1) is the first
qualifying occurrence and satisfies C-22 per C-36 (descriptive register + section-body
placement compose without interaction). The flow-conversation body placement (imperative,
position 2) is the second qualifying occurrence and is inert. C-38 states: "When the first
qualifying named section-body placement satisfies C-22 in descriptive register, any subsequent
qualifying placement is inert in exactly the same way it is inert in imperative register." The
"any subsequent qualifying placement" clause covers subsequent placements in ANY register,
including imperative. R13 V-02 confirmed C-38 with both placements descriptive; V-03 tests
whether the subsequent placement being IMPERATIVE is absorbed identically. Expected: 36/36
= 100, golden.

**Novelty verification**: All prior mixed-body tests used uniform register across all
placements (all imperative in R11-R13 N>1 tests; all descriptive in R12-R14 descriptive
tests). No prior round has placed the axis-header rule in two section bodies using DIFFERENT
registers. V-03 is the first test of cross-register dual section-body placement with
descriptive first and imperative subsequent. Genuinely new.

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
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases: INIT (preconditions and partial-init failures),
NOMINAL (component handoffs and silent failures), DEGRADED (error states and recovery),
TEARDOWN (cleanup and handoff completeness).

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

The closing confirmation gates are each labeled with a header that names the axis they check.

---

### flow-conversation

Walk the conversation and intent flow for `{{topic}}`: intent routing paths, response
contracts, graph transitions, fallback branches, session state tracking, timeout handling.
Note anything the spec leaves unclear or where caller and callee would disagree.

Add each finding immediately (Sub-Skill = flow-conversation, classify, assign blast radius).
If none: say so explicitly.

**Axis-Header Rule**: Each gate header names its axis.

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
a developer must address before writing the first line of implementation code.

Three gates before closing. One axis per gate. Do not merge.

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

---

## V-04 -- Mixed Register N=2: Imperative at Position 1, Descriptive at Position 2 (Register + Lifecycle)

**Axis**: Phrasing register + lifecycle emphasis -- the overall prompt is in imperative register
(identical to V-01 baseline structure) with the axis-header rule placed in TWO named section
bodies at DIFFERENT registers: (1) end of flow-lifecycle body (position 1) as an imperative
labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` and (2) end of
flow-conversation body (position 2) as a descriptive sentence: "The closing confirmation gates
are each labeled with a header that names the axis they check." No rule appears at positions
3-6 or the inter-section peer slot. This is the reverse complement of V-03.

**Hypothesis**: The flow-lifecycle body placement (imperative, position 1) is the first
qualifying occurrence and satisfies C-22 per C-33 (dual section-body placement with first
satisfying C-22 per confirmed R11 V-02 single-section-body pass). The flow-conversation body
placement (descriptive, position 2) is the second qualifying occurrence and is inert. C-33
covers dual named section-body placement with both in imperative; C-34 states criteria are
structure-sensitive, not register-sensitive. Together: if the second placement were imperative,
C-33 would make it inert; C-34 extends this to descriptive register without modification. The
second occurrence in descriptive is structurally inert regardless of its register. Expected:
36/36 = 100, golden.

**Novelty verification**: V-03 is the only prior mixed-register dual-body test, and uses
descriptive first. V-04 uses imperative first -- the reverse. No prior round has placed the
rule in two section bodies with the first imperative and the subsequent descriptive. Genuinely
new: first test of C-33 + C-34 composition with reverse register ordering (imperative first,
descriptive subsequent).

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
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."

Open this table before flow-lifecycle. Append rows as findings are discovered.
Blast Radius Rationale is required for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

Walk `{{topic}}` through four phases: INIT (preconditions and partial-init failures),
NOMINAL (component handoffs and silent failures), DEGRADED (error states and recovery),
TEARDOWN (cleanup and handoff completeness).

Add each finding immediately (Sub-Skill = flow-lifecycle, classify, assign blast radius).
If a phase has no findings, say so briefly.

**Axis-Header Rule**: Each gate header names its axis.

---

### flow-conversation

Walk the conversation and intent flow for `{{topic}}`: intent routing paths, response
contracts, graph transitions, fallback branches, session state tracking, timeout handling.
Note anything the spec leaves unclear or where caller and callee would disagree.

Add each finding immediately (Sub-Skill = flow-conversation, classify, assign blast radius).
If none: say so explicitly.

The closing confirmation gates are each labeled with a header that names the axis they check.

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
a developer must address before writing the first line of implementation code.

Three gates before closing. One axis per gate. Do not merge.

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

---

## V-05 -- Cross-Type Dual Placement: Section Body (Descriptive) + Inter-Section Peer Slot (Descriptive) (Register + Lifecycle)

**Axis**: Phrasing register + lifecycle emphasis -- the entire prompt is in descriptive
register AND the axis-header rule is placed at TWO qualifying positions of DIFFERENT types:
(1) end of flow-lifecycle body (position 1, named section body) as a descriptive sentence:
"The closing confirmation gates are each labeled with a header that names the axis they check."
(first qualifying occurrence, satisfies C-22 per C-36), and (2) the canonical inter-section
peer slot between Synthesis and Consolidated Findings (flanked by `---` dividers) as a
descriptive bare sentence: "Each closing confirmation gate header names its axis." (second
qualifying occurrence, inert). No rule appears at positions 2-6 other than the inter-section
peer slot.

**Hypothesis**: The flow-lifecycle body placement (descriptive, section body, position 1) is
the first qualifying occurrence and satisfies C-22 per C-36 (descriptive + section body
confirmed). The inter-section peer slot placement (descriptive, inter-section peer slot) is
the second qualifying occurrence and is inert. C-33 covers dual named SECTION-BODY placements;
the inter-section peer slot is not a named section body. The governing principle -- "first
qualifying occurrence satisfies C-22; all subsequent qualifying occurrences are inert" -- is
general and extends to any qualifying position regardless of type. C-24 confirms any non-buried
position is qualifying; the inertness rule for additional qualifying placements extends
across position types. V-02 (this round) confirms that descriptive register at the
inter-section peer slot satisfies C-22 as a FIRST qualifying occurrence; V-05 tests it
as a SECOND qualifying occurrence (inert). Expected: 36/36 = 100, golden.

**Novelty verification**: All prior multi-placement tests used placements of the SAME position
type (all section bodies, or all inter-section slots). V-05 is the first test combining
placements of DIFFERENT position types (section body + inter-section peer slot) in a single
prompt. No prior round has tested whether the inertness principle extends across position types.
Genuinely new: first cross-type dual placement composition.

```
This is `rhythm-behavior` running for topic: {{topic}}.

The output is a single continuous simulation findings report written to
`simulations/campaign/{{topic}}-simulate-{{date}}.md`. The entire report is
produced as one document from start to finish, without any promise of continuation.

The report proceeds through these sections in sequence: flow-lifecycle,
flow-conversation, trace-state, trace-contract, trace-permissions, SYNTHESIS,
Consolidated Findings.

---

### What to look for

**spec-gap** -- a requirement that is missing, ambiguous, or underspecified. The specific
spec section that is silent or unclear is named in the finding.

**contract-violation** -- a divergence in assumptions between caller and callee at a
named boundary.

**Blast radius**:
- WIDE -- corrupts shared state or breaks multiple downstream callers
- MEDIUM -- two or more components affected, shared state not reached
- NARROW -- failure stays inside one component

**Blast Radius Rationale** -- the 3-slot format is used for every finding:
  "[LEVEL] because [boundary] propagates to [caller/component], [effect]."
  Example: "WIDE because session-sequence-number contract propagates to flow-conversation
  routing and trace-contract pre-check, producing stale-state errors at both."

The findings table is opened before flow-lifecycle begins. Rows are appended as each
finding is discovered. The Blast Radius Rationale column is populated for every row.

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Impact | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|--------|-------------|

---

### flow-lifecycle

The flow-lifecycle section traces `{{topic}}` through its full operational lifecycle
across four phases: INIT (preconditions and partial-init failures), NOMINAL (component
handoffs and silent failures), DEGRADED (error states and recovery), and TEARDOWN
(cleanup and handoff completeness).

Findings are appended to the table as they are discovered (Sub-Skill = flow-lifecycle,
finding type classified, blast radius assigned). Any phase that produces no findings is
noted as such.

The closing confirmation gates are each labeled with a header that names the axis they check.

---

### flow-conversation

The flow-conversation section examines the conversation and intent flow for `{{topic}}`:
intent routing paths, response contracts, graph transitions, fallback branches, session
state tracking, and timeout handling. Anything the spec leaves unclear, or where caller
and callee assumptions would diverge, is recorded as a finding.

Findings are appended as discovered (Sub-Skill = flow-conversation). If this section
produces no findings, that is stated explicitly.

---

### trace-state

The trace-state section constructs the complete state model for `{{topic}}`: spec-defined
states, valid transitions, reachability from the initial state, and unauthorized state
crossings (classified as contract-violation by default).

Findings are appended as discovered (Sub-Skill = trace-state). If this section produces
no findings, that is stated explicitly.

---

### trace-contract

The trace-contract section examines every API and service boundary: pre/postcondition
symmetry, data invariants, and migration contracts. Any location where callee behavior
differs from what callers expect is recorded as a finding.

Findings are appended as discovered (Sub-Skill = trace-contract). If this section produces
no findings, that is stated explicitly.

---

### trace-permissions

The trace-permissions section traces the permission model: role authorization rules,
field-level security, team membership effects, sharing rules, and escalation paths.
Anything the spec omits, or where access control assumptions diverge, is recorded
as a finding.

Findings are appended as discovered (Sub-Skill = trace-permissions). If this section
produces no findings, that is stated explicitly.

---

### Synthesis

The Synthesis section reviews all findings collectively. For patterns that span two or
more sub-skills:
- The contributing sub-skills are named (at least two) along with each contributor's
  blast radius
- The compounding effect is described
- The CROSS-SKILL blast radius is >= max(contributing sub-skills); no downgrade from
  the highest contributor is permitted
- The rationale uses the 3-slot format plus provenance: "Inherited [LEVEL] from
  [sub-skill-X] ([F-ID])"
- The finding is labeled "CROSS-SKILL: [sub-skill-A + sub-skill-B]"
- The finding is inserted into the findings table with Sub-Skill = CROSS-SKILL

If no cross-skill patterns are present: "Synthesis: no cross-sub-skill patterns found."

---

Each closing confirmation gate header names its axis.

---

### Consolidated Findings

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

The findings table is sorted by blast radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

Top finding: a concrete next step naming the exact spec section, boundary, or component
a developer must address before writing any implementation code.

Three confirmation gates follow, one axis per gate, not merged.

**Coverage Axis Gate**: Confirms that at least one spec-gap finding and at least one
contract-violation finding are present in the report. If either category is absent,
add the missing finding before proceeding to the Format Axis Gate.

**Format Axis Gate**: Confirms that every Blast Radius Rationale cell uses the 3-slot
format with all three slots named. Any cell that does not conform is rewritten using
the [LEVEL] / [boundary] / [caller/component] / [effect] structure before proceeding
to the Inheritance Axis Gate.

**Inheritance Axis Gate**: Confirms that every CROSS-SKILL blast radius is >= max of
the contributing sub-skills, and that the rationale carries "Inherited [LEVEL] from
[sub-skill-X] ([F-ID])". Any finding that fails this check has its CROSS-SKILL blast
radius and provenance annotation corrected before closing.

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
