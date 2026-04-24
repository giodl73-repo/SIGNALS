**rhythm-behavior R12 variations written** to `simulations/quest/variations/rhythm-behavior-variations-R12-2026-03-17.md`.

---

## R12 Summary

**Strategy**: C-32 empirical gap closure + C-33 extension + C-34 composition. All 5 variations predicted 100 (27/27).

| V | Axis | Key move |
|---|------|----------|
| V-01 | Lifecycle emphasis | R11 V-01 production form -- reconfirmation at 27/27 |
| V-02 | Lifecycle emphasis | Rule in **flow-conversation body** (C-32 empirical: unlisted body at position 2) |
| V-03 | Lifecycle emphasis | Rule in **trace-contract body** (C-32 empirical: unlisted body at position 4) |
| V-04 | Phrasing register + lifecycle | **Descriptive register + section body** (C-34 + C-31 composition -- first time combined) |
| V-05 | Lifecycle emphasis | **Triple section-body placement** (C-33 extension: N=3 across positions 1, 3, 5) |

**Design rationale for each move:**

- **V-02/V-03** close the actual gap in C-32's enumeration. C-32 claims "all four named section bodies" but lists only flow-lifecycle, trace-state, trace-permissions, Synthesis. flow-conversation (position 2) and trace-contract (position 4) appear in the sub-skill sequence without individual confirmation. Both have identical structural properties to confirmed bodies. V-02 and V-03 test C-32's assertion empirically.

- **V-04** is the first composition of C-34 (register-invariance, confirmed R11 V-05) with C-31 (section-body placement, confirmed R11 V-02/V-03). R11 kept these separate. The descriptive rule text -- "The closing confirmation gates are each labeled with a header that names the axis they check." -- is a standalone declarative sentence in a qualifying position. C-23 says isolation decides; C-34 says register doesn't decide. Together: pass.

- **V-05** tests whether C-33's "no criterion penalizes multiple qualifying placements" has an implicit N=2 ceiling. It doesn't: three bodies (positions 1, 3, 5), all individually confirmed, first satisfies C-22, second and third inert. Extends R11 V-04 (dual body) one step.
rmed and are not listed in C-32's enumeration. C-32 asserts these are covered -- V-02
  and V-03 test that assertion empirically. Both bodies share the identical structural pattern
  as the confirmed bodies: section header, instructional content, null-result instruction
  ("If none: say so explicitly."), standalone labeled paragraph, closing ---. If both score
  27/27, the flow-conversation and trace-contract bodies are empirically confirmed, closing
  any remaining uncertainty about C-32's "all" claim.

- **V-04 is the first C-34 + C-31 composition test.** R11 V-05 confirmed descriptive register
  in the inter-section peer slot. R11 V-02/V-03/R10 V-04 confirmed section bodies with
  imperative register. V-04 combines both: the entire prompt is in descriptive register (V-05
  style from R11) AND the Axis-Header Rule appears in a named section body (flow-conversation)
  rather than the inter-section slot. The rule text in descriptive form: "The closing
  confirmation gates are each labeled with a header that names the axis they check." C-22
  requires a standalone declarative sentence -- the descriptive form satisfies this. C-26/C-31
  confirm section bodies are qualifying. C-34 confirms register-invariance. All three are
  independently confirmed; V-04 tests their composition.

- **V-05 tests whether C-33's inertness rule extends beyond N=2.** R11 V-04 confirmed dual
  section-body placement: first satisfies C-22, second is inert. C-33 says "no criterion
  penalizes multiple qualifying placements" without bounding N. V-05 places the rule in three
  section bodies simultaneously (flow-lifecycle, trace-state, trace-permissions -- positions
  1, 3, 5). The first satisfies C-22; the second and third are inert. No criterion imposes
  a ceiling on qualifying placements.

**Open questions for R12:**

| Question | V | Hypothesis |
|----------|---|-----------|
| Does C-32's closure extend to flow-conversation body (not in C-32's enumeration)? | V-02 | YES -- C-31 says "all named section bodies"; flow-conversation qualifies structurally |
| Does C-32's closure extend to trace-contract body (not in C-32's enumeration)? | V-03 | YES -- structural parallel to all confirmed positions |
| Does descriptive register compose cleanly with section-body placement? | V-04 | YES -- C-34 and C-31 are independent criteria with no stated interaction |
| Does C-33's inertness rule extend to triple (N=3) section-body placement? | V-05 | YES -- "no criterion penalizes multiple qualifying placements" has no N ceiling |

**Predicted scores under v12 rubric** (aspirational denominator = 27):

| Variation | C-32 | C-33 | C-34 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| V-01 | PASS (no section body; trivial) | PASS (single placement) | PASS (imperative passes) | **100** | YES |
| V-02 | PASS (flow-conversation within closed set) | PASS (single body) | PASS | **100** | YES |
| V-03 | PASS (trace-contract within closed set) | PASS (single body) | PASS | **100** | YES |
| V-04 | PASS | PASS (single body) | PASS (descriptive + section body) | **100** | YES |
| V-05 | PASS | PASS (triple: first satisfies, second/third inert) | PASS | **100** | YES |

---

## V-01 -- Production Baseline at 27/27 (Lifecycle Emphasis, Reconfirmation)

**Axis**: Lifecycle emphasis -- identical to R11 V-01 (= R10 V-01 = R9 V-05): minimal form,
labeled paragraph `**Axis-Header Rule**: Each gate header names its axis.` in the confirmed
inter-section peer slot between Synthesis and Consolidated Findings, flanked by `---` dividers.
Slot-name definition lines absent. Inline example retained. No other changes.

**Hypothesis**: R11 V-01 scored 24/24 under v11. Under v12 the three new criteria encode
R11 findings directly:
- C-32 passes: no named section body is used; trivial pass.
- C-33 passes: single inter-section placement; no dual or triple body; trivial pass.
- C-34 passes: imperative register throughout; register-invariance means imperative still passes.
Expected: 27/27 = 100, golden.

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
a developer must address before writing implementation code.

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

## V-02 -- Flow-Conversation Body Probe (Lifecycle Emphasis, C-32 Unlisted Body at Position 2)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph at the END of the flow-conversation section body, immediately after the null-result
instruction ("If none: say so explicitly.") and before the closing `---` divider.
flow-conversation is position 2 of the sub-skill sequence and was NOT individually listed in
C-32's enumeration of confirmed bodies (which names only flow-lifecycle, trace-state,
trace-permissions, and Synthesis). No rule appears in any inter-section slot or any other
section body. All other elements identical to V-01.

**Hypothesis**: C-32 asserts that "all named section bodies" are confirmed and that "no named
section body remains unconfirmed." Yet flow-conversation is not in C-32's explicit list. C-31
says the non-disqualifying scope extends to "all named section bodies" -- flow-conversation
has identical structural properties to all confirmed bodies: section header, instructional
content, null-result instruction ("If none: say so explicitly."), standalone labeled paragraph,
closing ---. The disqualifier set is strictly gate body + example block; flow-conversation
body is neither. C-25 governs: "any non-buried position." If V-02 = 100, flow-conversation
body is empirically confirmed, removing any residual uncertainty about C-32's "all" claim
for this position. Expected: 27/27 = 100, golden.

**Novelty verification**: R11 confirmed flow-lifecycle (V-02, pos 1), trace-state (R10 V-04,
pos 3), trace-permissions (R11 V-03, pos 5), Synthesis. flow-conversation (pos 2) has never
been individually tested. Genuinely new.

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
a developer must address before writing implementation code.

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

## V-03 -- Trace-Contract Body Probe (Lifecycle Emphasis, C-32 Unlisted Body at Position 4)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph at the END of the trace-contract section body, immediately after the null-result
instruction ("If none: say so explicitly.") and before the closing `---` divider.
trace-contract is position 4 of the sub-skill sequence -- the second body absent from C-32's
confirmed list. No rule appears in any inter-section slot or any other section body. All
other elements identical to V-01.

**Hypothesis**: C-32 claims closure across all named section bodies, listing four. trace-contract
(position 4 of 5) has never been individually tested. Its structural pattern is identical to
all confirmed bodies and to flow-conversation (V-02): section header, instructional content,
null-result instruction ("If none: say so explicitly."), standalone labeled paragraph, closing
---. The same C-25/C-26/C-31 reasoning applies: "any non-buried position," disqualifiers are
strictly gate body + example block, section body is neither. Together with V-02, a 27/27
score here closes the only remaining individual-confirmation gaps in C-32's "all" claim.
Expected: 27/27 = 100, golden.

**Novelty verification**: trace-contract (pos 4) has never been individually tested. This
is the fifth and final sub-skill body to receive individual confirmation (after flow-lifecycle,
flow-conversation (V-02 this round), trace-state, trace-permissions). Genuinely new.

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

**Axis-Header Rule**: Each gate header names its axis.

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

## V-04 -- Descriptive Register + Section Body (Phrasing Register + Lifecycle, C-34 + C-31 Composition)

**Axis**: Phrasing register + lifecycle emphasis -- the entire prompt is written in
descriptive/explanatory register (identical strategy to R11 V-05) AND the Axis-Header Rule
is placed inside a named section body (flow-conversation body) rather than the inter-section
peer slot. The rule appears in descriptive form: "The closing confirmation gates are each
labeled with a header that names the axis they check." All structural requirements are
preserved verbatim: three axis-labeled gate headers (Coverage Axis Gate / Format Axis Gate /
Inheritance Axis Gate), three independent correction loops, 3-slot template + inline example,
pre-opened findings table with rationale column, at-discovery row appending.

**Hypothesis**: C-34 (register-invariance) and C-26/C-31 (section body is qualifying) are
independent criteria with no stated interaction. C-22 requires "a concise standalone declarative
sentence" -- the descriptive rule "The closing confirmation gates are each labeled with a header
that names the axis they check." is a standalone declarative sentence placed in a qualifying
position (flow-conversation body). C-23 confirms isolation is the deciding factor, not label
presence. C-34 confirms register is not a deciding factor. Together: descriptive rule + section
body = qualifying for C-22. All remaining criteria check structural elements (table columns,
gate count, axis labels in headers, template + example) that are register-independent.
Expected: 27/27 = 100, golden.

**Novelty verification**: R11 V-05 = descriptive register + inter-section peer slot. R11 V-02
= section body + imperative. V-04 = descriptive register + section body. Never tested before.

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

The closing confirmation gates are each labeled with a header that names the axis they check.

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

## V-05 -- Triple Named Section-Body Placement (Lifecycle Emphasis, C-33 Extension to N=3)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph inside THREE named section bodies simultaneously: at the end of the flow-lifecycle
body (after "If a phase has no findings, say so briefly.", before closing ---), at the end
of the trace-state body (after "If none: say so explicitly.", before closing ---), and at
the end of the trace-permissions body (after "If none: say so explicitly.", before closing
---). No rule appears in any inter-section slot. All other elements identical to V-01.

**Hypothesis**: C-33 states "two qualifying named section-body placements satisfy C-22 at
the first occurrence; the second is redundant but inert. No criterion penalizes multiple
qualifying placements." The rule is stated without an N-ceiling: "multiple qualifying
placements" has no stated upper bound. Three placements follow the same logic: the first
satisfies C-22, the second and third are inert. R8 V-05 confirmed dual inter-section slots;
R11 V-04 confirmed dual section bodies (N=2). V-05 extends the pattern to N=3 across three
section bodies spanning the full sub-skill range (positions 1, 3, 5). The three chosen bodies
include two from C-32's confirmed list (flow-lifecycle, trace-permissions) plus trace-state
(also confirmed) -- all individually validated, so no unconfirmed variable is introduced.
Expected: 27/27 = 100, golden.

**Novelty verification**: R8 V-05 = dual inter-section slots. R11 V-04 = dual section bodies.
V-05 = triple section bodies (N=3). No three-body placement exists in R1-R11 run history.

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

---

### trace-state

Build the complete state model for `{{topic}}`: spec-defined states, valid transitions,
reachability from initial state, unauthorized crossings (contract-violation by default).

Add each finding immediately (Sub-Skill = trace-state, classify, assign blast radius).
If none: say so explicitly.

**Axis-Header Rule**: Each gate header names its axis.

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

**Axis-Header Rule**: Each gate header names its axis.

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
