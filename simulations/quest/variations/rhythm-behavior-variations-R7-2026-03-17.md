Written to `simulations/quest/variations/rhythm-behavior-variations-R7-2026-03-17.md`.

---

## R7 Variations Summary

**New criterion**: C-22 -- Explicit Axis-Header Preamble Rule (denominator 14 -> 15).

**Base**: R6 V-05 (22/22 under v6, already has "Each gate header names its axis." in preamble chain).

**Strategy**: Two boundary probes that should fail C-22, one phrasing verbosity test, two combos testing the strongest standalone form.

| V | Axis | Key move | Prediction |
|---|------|----------|-----------|
| V-01 | Phrasing register (burial probe) | Rule appended to Coverage Axis Gate body | C-22 FAIL -- 99.2 |
| V-02 | Output format (example probe) | Rule as parenthetical inside rationale example block | C-22 FAIL -- 99.2 |
| V-03 | Phrasing register (verbosity) | Extended form: "Every closing confirmation gate header must explicitly name its quality axis." | 100 |
| V-04 | Combo: dedicated paragraph + stripped headers | **Axis-Header Rule**: paragraph isolated by blank lines | 100 |
| V-05 | Combo: dedicated paragraph + full positional headers | V-04 rule + "Gate N -- Coverage Axis Gate" prefix | 100 |

**Production candidate**: V-04 -- the dedicated `**Axis-Header Rule**: Each gate header names its axis.` paragraph is the maximally standalone C-22 form at minimal prompt mass. V-05 is the verbosity reference; if V-04 = V-05 on all 22 criteria, the positional prefix remains decorative for the third consecutive round.
x | 100 |

**Key structural moves**:

- **V-01 burial probe**: Moves "Each gate header names its axis." from the preamble chain into the body of Coverage Axis Gate. Tests whether C-22's "not buried in a gate body" disqualifier is location-specific. If V-01 fails C-22 while R6 V-05 passes, preamble-chain position vs. gate-body position is load-bearing.
- **V-02 example probe**: Embeds the rule as a parenthetical immediately following the 3-slot rationale example text. Tests whether C-22's "not inlined within an example" disqualifier fires for a parenthetical appended to an example. The rule is structurally within the example block (same indentation), not an independent sentence.
- **V-03 verbosity test**: Replaces the compressed "Each gate header names its axis." with the extended form "Every closing confirmation gate header must explicitly name its quality axis." Same standalone sentence, more explicit modal and scope. Tests whether phrasing within the standalone form affects C-22 or any prior criteria.
- **V-04 dedicated paragraph**: Isolates the rule as a visually independent paragraph with a bold label: "**Axis-Header Rule**: Each gate header names its axis." Separated from surrounding instructions by blank lines. Tests whether labeled-paragraph form is a stronger C-22 encoding than the preamble-chain form.
- **V-05 dedicated paragraph + full headers**: V-04's dedicated rule paragraph combined with the full "Gate N -- Coverage Axis Gate" header form from R6 V-01/V-04. Tests whether maximum-explicitness combination (dedicated rule label + positional + axis-gate header) outperforms V-04 on any criterion. Confirms positional prefix still decorative under v7 rubric.

**Production candidate prediction**: V-04 -- dedicated **Axis-Header Rule** paragraph with stripped axis-gate headers, maximum structural independence for C-22 at minimal prompt mass.

**Open questions**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does the rule buried in a gate body fail C-22? | V-01 | YES -- "not buried in a gate body" is a disqualifying location |
| Does the rule inlined in an example block fail C-22? | V-02 | YES -- parenthetical within an example block is not a standalone independent instruction |
| Does a verbose extended sentence satisfy C-22 identically to the compressed form? | V-03 | YES -- C-22 tests standalone presence, not phrasing; no criteria difference |
| Does a dedicated labeled paragraph form pass C-22 more robustly than preamble-chain? | V-04 | YES -- visual and structural isolation maximum; most independently readable |
| Does combining dedicated rule paragraph with full positional headers improve over V-04? | V-05 vs V-04 | NO -- positional prefix confirmed decorative in R6; V-04 and V-05 should score identically |

**Predicted scores under v7 rubric** (aspirational denominator = 15):

| Variation | C-22 | Composite | Golden |
|-----------|------|-----------|--------|
| V-01 | **FAIL** | 99.2 | YES (all essential+recommended pass) |
| V-02 | **FAIL** | 99.2 | YES |
| V-03 | PASS | **100** | YES |
| V-04 | PASS | **100** | YES |
| V-05 | PASS | **100** | YES |

---

## V-01 -- Rule Buried in Coverage Axis Gate Body (Phrasing Register, Burial Probe)

**Axis**: Phrasing register -- "Each gate header names its axis." is removed from the preamble chain and appended to the body of the Coverage Axis Gate block. Every other element is identical to R6 V-05.
**Hypothesis**: C-22 requires the rule to appear as an independent instruction, explicitly disqualifying burial in a gate body. Moving the sentence into the gate's body text -- between the gate's question and its correction loop -- puts it in the gate block, not a standalone preamble. Expected FAIL C-22: the sentence is embedded in the gate block's instruction flow, not independently readable as a structural rule.

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

**Coverage Axis Gate**: spec-gap present? contract-violation present? Each gate header
names its axis.
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

## V-02 -- Rule Inlined in Rationale Example (Output Format, Example Probe)

**Axis**: Output format -- "Each gate header names its axis." is removed from the preamble chain and inserted as a parenthetical immediately following the 3-slot rationale example, within the indented example block. All other elements are identical to R6 V-05.
**Hypothesis**: C-22 disqualifies rules "inlined within an example." The parenthetical "(Gate headers name their axis.)" appears at the same indentation level as the example text -- structurally within the example block, not a standalone instruction. A model reading the block treats it as a footnote on the example, not a governing rule. Expected FAIL C-22: the rule is not independently readable as a structural instruction; its placement inside the example block makes it a commentary annotation, not a preamble rule.

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
  (Gate headers name their axis.)
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

## V-03 -- Extended Standalone Sentence Form (Phrasing Register)

**Axis**: Phrasing register -- the compressed "Each gate header names its axis." is replaced with the extended form "Every closing confirmation gate header must explicitly name its quality axis." The rule remains in the preamble chain position (last sentence of the "Three gates before closing..." line). All other elements are identical to R6 V-05.
**Hypothesis**: C-22 tests standalone presence, not phrasing. The extended sentence is still a standalone declarative sentence -- not buried, not inlined. Modal "must," scope qualifier "closing confirmation," and adjective "quality" add no criteria coverage; this was confirmed in R6 between V-04 and V-05 phrasing forms, both scoring 100. Expected 100: no criteria change from R6 V-05. Confirms the compressed form is sufficient and the extended form adds no value at the cost of extra prompt mass.

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

Three gates before closing. One axis per gate. Do not merge. Every closing confirmation
gate header must explicitly name its quality axis.

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

## V-04 -- Dedicated Axis-Header Rule Paragraph + Stripped Headers (Combo)

**Axis**: Output format (dedicated rule paragraph with bold label) + phrasing register
(compressed sentence form from R6 V-05). The rule is isolated as its own paragraph:
"**Axis-Header Rule**: Each gate header names its axis." separated from the surrounding
instruction lines by blank lines before and after. Headers remain stripped axis-gate form
("**Coverage Axis Gate**"). This is the minimal-mass production candidate.
**Hypothesis**: The dedicated labeled paragraph is the strongest standalone form for C-22 --
visually and structurally independent, unambiguously not buried and not inlined. The
"**Axis-Header Rule**:" label makes the rule purpose self-evident without reading the gate
blocks. If V-04 scores 100 and V-01/V-02 fail, the dedicated-paragraph form is the
maximally robust C-22 encoding at minimal prompt mass. R7 production candidate.

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

**Axis-Header Rule**: Each gate header names its axis.

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

## V-05 -- Dedicated Axis-Header Rule Paragraph + Full Positional Headers (Combo)

**Axis**: Output format (V-04 dedicated rule paragraph) + positional prefix retained
("Gate N -- Coverage Axis Gate" from R6 V-01/V-04). Tests whether the maximum-explicitness
combination -- labeled dedicated rule paragraph + positional + axis-gate headers -- scores
identically to V-04 (dedicated rule + stripped headers). The positional prefix was confirmed
decorative in R6 (R6 V-03 = R6 V-01 on all 21 criteria). If V-05 matches V-04 on all 22
criteria, the positional prefix remains decorative under the v7 rubric and V-04 is the
minimal form. V-05 is the verbosity reference.
**Hypothesis**: 100 -- identical to V-04 on all criteria. The positional prefix adds no
criteria coverage under any of the 22 criteria. If confirmed, V-04 is the R7 production
candidate at minimum prompt mass.

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

**Axis-Header Rule**: Each gate header names its axis.

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
