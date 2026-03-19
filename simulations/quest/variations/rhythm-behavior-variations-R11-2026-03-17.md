**rhythm-behavior R11 variations written** to `simulations/quest/variations/rhythm-behavior-variations-R11-2026-03-17.md`.

---

## R11 Summary

**Strategy**: C-31 extension coverage + phrasing register probe. Two goals: (1) confirm production candidate at 24/24 under the expanded rubric, (2) probe C-31's "all named section bodies" claim against the two extreme bodies, test dual body composition, and break new ground with phrasing register.

| V | Axis | Key move | Prediction |
|---|------|----------|-----------|
| V-01 | Lifecycle emphasis | R10 V-01 production form -- reconfirmation at 24/24 | **100** |
| V-02 | Lifecycle emphasis | Rule in flow-lifecycle body (earliest named section body, C-31 extension) | **100** |
| V-03 | Lifecycle emphasis | Rule in trace-permissions body (last named section body before Synthesis) | **100** |
| V-04 | Lifecycle emphasis | Rule in flow-lifecycle body + trace-state body simultaneously (dual body, no inter-section slot) | **100** |
| V-05 | Phrasing register | Full descriptive/explanatory register throughout; all structural requirements preserved | **100** |

---

**Key structural moves:**

- **V-01** is pure confirmation: R10 V-01 unchanged against 24 criteria. C-28/C-29/C-30/C-31 all pass trivially for the inter-section slot form.

- **V-02/V-03 are the C-31 extremal bracket pair.** R10 V-04 confirmed trace-state body (position 3). V-02 = flow-lifecycle (position 1, most distant from Synthesis); V-03 = trace-permissions (position 5, immediately before Synthesis). Together with R10 V-04 and R9 V-04 (Synthesis body), this closes the C-31 "all named section bodies" claim across all five sub-skill sections.

- **V-04** tests dual body placement: two section bodies, no inter-section slot. Genuinely new -- R8 V-05 tested dual inter-section slots, R10 V-04 tested a single body. Tests C-31 composition and whether redundant qualifying placements are inert.

- **V-05** is the first phrasing register probe at the 24-criterion denominator. Imperative directives rewritten as declarative descriptions. Gate headers and structural requirements preserved verbatim. The design note from R10 is applied: novelty verified before writing -- no prior round has tested phrasing register at current rubric depth.

**Open questions for R11:**

| Question | V | Hypothesis |
|----------|---|-----------|
| Does C-31 extend to flow-lifecycle body? | V-02 | YES |
| Does C-31 extend to trace-permissions body? | V-03 | YES |
| Do two section-body placements compose cleanly? | V-04 | YES |
| Is phrasing register irrelevant to all 24 criteria? | V-05 | YES |
body. V-04 is genuinely new: two section bodies, no
  inter-section slot. Tests whether two qualifying body positions compose without
  interference and whether C-22 handles redundant qualifying placements cleanly.

- **V-05** is the first phrasing register test at the 24-criterion denominator. All
  imperative instruction sentences are rewritten in descriptive/explanatory register
  (declarative descriptions of what each section does rather than directives to the model).
  All structural requirements preserved verbatim. Tests whether criteria are register-
  invariant.

**Open questions for R11**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does C-31 extend to flow-lifecycle body (earliest sub-skill section)? | V-02 | YES -- C-31 says "all named section bodies"; flow-lifecycle has null-result line + closing --- |
| Does C-31 extend to trace-permissions body (last sub-skill section before Synthesis)? | V-03 | YES -- structural parallel to trace-state body confirmed in R10 |
| Does dual body placement (two section bodies, no inter-section slot) work? | V-04 | YES -- no rubric criterion penalizes redundant qualifying placements |
| Is phrasing register (descriptive vs. imperative) irrelevant to criteria scoring? | V-05 | YES -- all criteria check structural properties, not register |

**Predicted scores under v11 rubric** (aspirational denominator = 24):

| Variation | C-16 | C-22 | C-25 | C-26 | C-27 | C-28 | C-29 | C-30 | C-31 | Composite | Golden |
|-----------|------|------|------|------|------|------|------|------|------|-----------|--------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | YES |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (if C-31 extends) | **100** | YES |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (if C-31 extends) | **100** | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | YES |

---

## V-01 -- Production Baseline at 24/24 (Lifecycle Emphasis, Reconfirmation)

**Axis**: Lifecycle emphasis -- identical to R10 V-01 (= R9 V-05): minimal form, labeled
paragraph `**Axis-Header Rule**: Each gate header names its axis.` in the confirmed inter-
section peer slot between Synthesis and Consolidated Findings, flanked by `---` dividers.
Slot-name definition lines absent. Inline example retained. No other changes.

**Hypothesis**: R10 V-01 scored 20/20 under v10. Under v11 the four new criteria encode
R10 findings directly:
- C-28 passes: inline example IS present -- scorer correctly recognizes it as required.
- C-29 passes: example IS present; C-27 correctly applies to this form; C-29's protection
  against invoking C-27 to shield a genuinely MISSING example is not triggered.
- C-30 passes: rule is in the confirmed late inter-section slot; positional invariance
  holds from earliest to latest; this position is well within the invariant range.
- C-31 passes: rule is NOT in any section body -- C-31's non-disqualifying expansion is
  not triggered; trivial pass.
Expected: 24/24 = 100, golden.

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

## V-02 -- Flow-Lifecycle Body Probe (Lifecycle Emphasis, C-31 Earliest Body Extension)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph at the END of the flow-lifecycle section body, immediately after the null-result
instruction ("If a phase has no findings, say so briefly.") and before the closing `---`
divider. flow-lifecycle is the EARLIEST named section body in the sub-skill sequence --
the most distant possible body placement from the gate blocks. No rule appears in any
inter-section slot or any other section body. All other elements identical to V-01.

**Hypothesis**: C-31 states C-26 extends to all named section bodies. R10 V-04 confirmed
trace-state (position 3 of 5). V-02 tests the opposite extreme: flow-lifecycle is the
first section in the prompt, before any other sub-skill runs. The structural pattern is
identical to trace-state (R10 V-04) and Synthesis (R9 V-04): standalone labeled paragraph,
after null-result instruction, before closing `---` divider. The null-result form for
flow-lifecycle ("If a phase has no findings, say so briefly.") differs in wording from
other sections ("If none: say so explicitly.") but is functionally equivalent as a null-
result terminator -- the structural property that matters is the presence of a null-result
line before the closing divider, not the exact wording. The disqualifier set remains
strictly gate body + example block; flow-lifecycle body is neither. C-25 governs: "any
non-buried position" with no proximity floor. If V-02 = 100, C-31's "all named section
bodies" includes flow-lifecycle at the earliest position. Expected: 24/24 = 100, golden.

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

## V-03 -- Trace-Permissions Body Probe (Lifecycle Emphasis, C-31 Latest Pre-Synthesis Body)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph at the END of the trace-permissions section body, immediately after the null-
result instruction ("If none: say so explicitly.") and before the closing `---` divider.
trace-permissions is the LAST named section body before Synthesis -- immediately preceding
the Synthesis section. No rule appears in any inter-section slot or any other section body.
All other elements identical to V-01.

**Hypothesis**: C-31 states C-26 extends to all named section bodies. R10 V-04 confirmed
trace-state (position 3 of 5). V-03 tests position 5 of 5 -- the closest sub-skill body
to Synthesis. The structural pattern is identical to the confirmed positions: standalone
labeled paragraph, after null-result instruction ("If none: say so explicitly."), before
closing `---` divider. trace-permissions qualifies under C-31's extended class. If V-03
= 100, the confirmed range for named section bodies now spans from flow-lifecycle (V-02 =
position 1, earliest) through trace-permissions (V-03 = position 5, latest pre-Synthesis),
with trace-state (R10 V-04 = position 3) and Synthesis (R9 V-04) already confirmed. This
closes C-31's "all named section bodies" claim across all positions without exception.
Expected: 24/24 = 100, golden.

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

---

## V-04 -- Dual Section-Body Placement (Lifecycle Emphasis, C-31 Composition)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph inside TWO named section bodies simultaneously: at the end of the flow-lifecycle
body (after null-result, before closing `---`) and at the end of the trace-state body
(after null-result, before closing `---`). No rule appears in any inter-section slot.
All other elements identical to V-01.

**Hypothesis**: C-31 confirms named section bodies are qualifying positions; C-25 confirms
"any non-buried position." Two qualifying positions in the same prompt compose without
interference -- no rubric criterion penalizes redundant qualifying placements. C-22
requires at least one standalone declarative sentence in a qualifying position; having two
satisfies this without surplus risk. R8 V-05 confirmed dual inter-section slots. R10 V-04
tested a single body. V-04 is a new configuration: two section bodies, no inter-section
slot. C-22 passes at the first qualifying position (flow-lifecycle body); the second
(trace-state body) is redundant but inert. Expected: 24/24 = 100, golden.

**Novelty verification**: R8 V-05 = dual inter-section slots. R10 V-04 = single body
(trace-state). R11 V-04 = two section bodies, no inter-section slot. Configuration is
genuinely new.

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

## V-05 -- Descriptive Register (Phrasing Register, Structural-Invariance Probe)

**Axis**: Phrasing register -- all imperative instruction sentences are rewritten in
descriptive/explanatory register. Directives ("Walk {{topic}} through...", "Add each
finding immediately...") become declarative descriptions of what each section produces
("The flow-lifecycle section traces {{topic}} through...", "Findings are appended to the
table as they are discovered..."). Gate bodies use explanatory language ("Confirms that...
If either is absent, the missing finding is added...") rather than imperative conditionals
("Missing: add one..."). All structural requirements are preserved verbatim: axis-labeled
gate headers (Coverage Axis Gate / Format Axis Gate / Inheritance Axis Gate), three-gate
structure with independent correction loops, template + example in the 3-slot definition,
pre-opened findings table with rationale column, at-discovery row appending. Axis-Header
Rule placement is identical to V-01 (inter-section peer slot between Synthesis and
Consolidated Findings).

**Hypothesis**: All 24 rubric criteria check structural properties of the prompt (presence
of template + example, gate header labels containing axis names, gate count, independent
correction loops per gate, table pre-opening, rationale column pre-declared, etc.) rather
than the register of the instruction language. A descriptive register that preserves all
structural elements scores identically to the imperative form. Key risk point at C-20
(Axis-Named Repair Verb): the descriptive gate bodies use "add the missing finding"
(coverage axis), "rewritten using the three-slot format" (format axis), and "corrected to
match the highest contributing sub-skill" (inheritance axis) -- all name the axis target
explicitly without generic directives. Expected: 24/24 = 100, golden. If any criterion
fails, the failure isolates the structural property that is register-sensitive.

**Novelty verification**: No phrasing register test exists in the R1-R11 run history at
the current rubric depth. This is a genuinely new axis. The prior axis coverage is: role
sequence (R1-R2), output format (R1-R5), lifecycle emphasis (R3-R10). Phrasing register
has not been explored.

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

**Axis-Header Rule**: Each gate header names its axis.

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
