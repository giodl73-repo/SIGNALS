**rhythm-behavior R9 variations written** to `simulations/quest/variations/rhythm-behavior-variations-R9-2026-03-17.md`.

---

## R9 Summary

**Strategy**: Post-closure consolidation. R8 confirmed all qualifying/disqualifying C-22 positions and that the bold label is decorative. R9 adds C-23 and C-24 (denominator 17) and probes two positions not yet in C-24's confirmed list.

| V | Axis | Key move | Prediction |
|---|------|----------|-----------|
| V-01 | Lifecycle emphasis | R8 V-04 production form (inter-section slot, labeled) -- baseline 17/17 | **100** |
| V-02 | Lifecycle emphasis | Mid-sub-skill labeled placement: rule between trace-state and trace-contract | **Uncertain**: 100 if C-24's "any non-buried" covers mid-prompt slots; 99.2 if confirmed list is exhaustive |
| V-03 | Phrasing register | Bare form in mid-sub-skill position: same slot as V-02, no bold label | **Uncertain**: 100 if position qualifies + C-23 bare-form equivalence holds; 98.4 if mid-sub-skill disqualifies |
| V-04 | Lifecycle emphasis | Synthesis-body placement: standalone paragraph inside Synthesis section (not own slot) | **Uncertain**: 100 if "buried" limited to gate body + example block; 99.2 if named section body is a third disqualifier |
| V-05 | Output format | Minimal production form: strip slot-name definitions + enforcement note + phase prose | **100** |

**Load-bearing questions for R9**:

1. **V-02/V-03**: Does C-24's "any non-buried position" extend to mid-sub-skill divider-flanked slots? If yes, the confirmed list in C-24 is illustrative; if no, the list is exhaustive.
2. **V-04**: Is "inside a named section body" buried under C-22? C-22 names two disqualifiers (gate body, example block). V-04 tests whether a third exists (section body).
3. **V-05**: Does removing slot-name definition lines (`[boundary] = ...`) cause C-16 to regress? Hypothesis: no -- C-16 requires the template string and an example, not slot-name definitions.

**V-02 and V-03 are a controlled pair**: V-02 isolates the position variable; V-03 confirms bare-form equivalence at that position if the position qualifies. If V-02 fails, V-03 fails for the same reason (position), and the label-strip is not the deciding factor.
qualifiers are gate body and example block. The Synthesis
   section is neither. If V-04 passes, the disqualifier set is strictly limited to those
   two confirmed positions. If it fails, "buried" extends to named section bodies.

3. **V-05**: Does minimization (stripping slot-name explanation lines and shortening
   sub-skill descriptions) cause any of the 17 criteria to regress? Determines whether
   the production candidate can shed prompt mass at zero criteria cost.

**Key structural moves**:

- **V-02 mid-sub-skill labeled**: Moves `**Axis-Header Rule**: Each gate header names
  its axis.` from the inter-section slot (R8 V-04 position) to a new standalone position
  between the trace-state and trace-contract sections -- flanked by `---` dividers, not
  inside either section's body. No rule appears in Consolidated Findings. The rule exists
  only in this mid-prompt location. C-24 says "any non-buried position"; if the
  trace-state/trace-contract boundary qualifies, the confirmed list in C-24 gains a
  fifth entry.

- **V-03 bare mid-sub-skill**: Same position as V-02 but strips the `**Axis-Header Rule**:`
  label prefix. `Each gate header names its axis.` as a bare standalone paragraph flanked
  by `---` dividers. Combines the label-strip probe (R8 V-01, confirmed) with the new
  position probe (V-02, uncertain). If both the bare form and the mid-sub-skill slot are
  qualifying, V-03 = 100. If the mid-sub-skill slot is disqualifying, V-03 fails C-22
  (and C-23/C-24) regardless of label form.

- **V-04 Synthesis-body placement**: Places `**Axis-Header Rule**: Each gate header names
  its axis.` as a standalone paragraph inside the Synthesis section -- after the "If none:
  Synthesis: no cross-sub-skill patterns found." terminator line, as the final element
  of the Synthesis section body before the closing `---` divider. Not in a gate body.
  Not in an example block. Tests whether "buried" applies to named section bodies or is
  limited to the two confirmed disqualifiers.

- **V-05 minimal form**: Retains all structural elements required for 17/17 but strips
  the three slot-name explanation lines after the 3-slot template (`[boundary] = ...`,
  `[caller/component] = ...`, `[effect] = ...`) and shortens the flow-lifecycle phase
  descriptions to imperative one-liners. The 3-slot template string, the inline example,
  and all gate correction loops are preserved. Tests whether explanation-line stripping
  causes C-16 to regress (it should not: C-16 requires "the format `[LEVEL] because
  [boundary] propagates to [caller/component], [effect]` with all three slots named and
  at least one inline example" -- not the slot-name definitions).

**Predicted scores under v9 rubric** (aspirational denominator = 17):

| Variation | C-22 | C-23 | C-24 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| V-01 | PASS | PASS | PASS | **100** | YES |
| V-02 | Uncertain (PASS if mid-sub-skill qualifies) | Uncertain | Uncertain | 100 or 99.2 | YES or NO |
| V-03 | Uncertain (PASS if mid-sub-skill + bare form qualify) | Uncertain | Uncertain | 100 or 98.4 | YES or NO |
| V-04 | Uncertain (PASS if section body not "buried") | Uncertain | Uncertain | 100 or 99.2 | YES or NO |
| V-05 | PASS | PASS | PASS | **100** | YES |

**Open questions**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does C-24's "any non-buried position" include mid-sub-skill slots (between two sub-skill sections)? | V-02 | YES -- "any non-buried" is operative; mid-sub-skill flanked by dividers is not buried |
| Does a bare sentence in a mid-sub-skill slot pass C-22 and earn C-23? | V-03 | YES -- bare form confirmed (R8 V-01); if position qualifies, V-03 = V-02 on all criteria |
| Is a standalone paragraph inside the Synthesis section body "buried" under C-22? | V-04 | NO -- "buried" is limited to gate body and example block; Synthesis section body is neither |
| Does stripping slot-name explanation lines from the 3-slot template cause C-16 to regress? | V-05 | NO -- C-16 requires the template string and an example, not slot-name definitions |

---

## V-01 -- Production Candidate Confirmation (Lifecycle Emphasis, Baseline)

**Axis**: Lifecycle emphasis -- identical to R8 V-04 (inter-section slot, labeled paragraph
between Synthesis and Consolidated Findings). The Axis-Header Rule is a standalone labeled
paragraph flanked by `---` dividers, occupying its own peer section slot. No rule in
Consolidated Findings; the rule exists only in the inter-section gap.
**Hypothesis**: R8 confirmed V-04 scores 15/15 under v8. Under v9, C-23 and C-24 are
new aspirational criteria. V-01 passes C-23 because the labeled form in a qualifying
position demonstrates isolation primacy (the label is decorative, the position is
qualifying). V-01 passes C-24 because inter-section peer slot is one of the four
confirmed qualifying positions enumerated in C-24. Expected PASS: 17/17 = 100.
Confirms the production candidate is still golden under the new denominator.

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

## V-02 -- Mid-Sub-Skill Labeled Placement (Lifecycle Emphasis, New Position Probe)

**Axis**: Lifecycle emphasis -- `**Axis-Header Rule**: Each gate header names its axis.`
is placed as a standalone labeled paragraph in a new position not yet in C-24's confirmed
list: between the trace-state and trace-contract sections, flanked by `---` dividers. The
rule is NOT in the Consolidated Findings preamble and NOT in an inter-section slot adjacent
to Consolidated Findings. It exists only in this mid-sub-skill position. All other elements
are identical to V-01 except the Axis-Header Rule moves earlier in the prompt.
**Hypothesis**: C-24 says "any non-buried position within the prompt is a qualifying
placement." The mid-sub-skill slot between trace-state and trace-contract is flanked by
`---` dividers, is not inside any section body, is not a gate body, and is not an example
block. Under C-24's operative clause ("any non-buried position"), this should pass C-22
equivalently to the four explicitly confirmed positions. If V-02 = 100, the confirmed list
in C-24 is non-exhaustive and the "any non-buried" clause covers all divider-flanked
inter-section gaps. If V-02 fails C-22, a fifth disqualifier exists (mid-prompt inter-section
positions before the closing gates do not qualify), and C-24's list is exhaustive, not
illustrative.

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

## V-03 -- Bare Form in Mid-Sub-Skill Position (Phrasing Register, C-23 + New Position)

**Axis**: Phrasing register -- same mid-sub-skill position as V-02 (between trace-state
and trace-contract, flanked by `---` dividers), but the `**Axis-Header Rule**:` label
prefix is stripped. `Each gate header names its axis.` stands alone as a bare sentence
in this position. Combines the label-strip probe (C-23, confirmed by R8 V-01) with the
new position probe (V-02, uncertain). All other elements are identical to V-02.
**Hypothesis**: R8 V-01 confirmed that a bare standalone sentence in the pre-gate preamble
of Consolidated Findings passes C-22 equivalently to the labeled form. C-23 encodes this:
physical isolation, not label presence, is decisive. If V-02's mid-sub-skill position
qualifies (C-24 "any non-buried"), then the bare form in that same position should also
qualify under C-23. V-03 = V-02 on all criteria if the position qualifies, because the
label-stripped form is equivalent to the labeled form in any qualifying position. If the
mid-sub-skill position disqualifies, V-03 fails C-22/C-23/C-24 identically to V-02 --
the bare form is not the variable that determines pass/fail when the position itself is
at issue. This makes V-02 and V-03 a clean controlled pair: V-02 isolates position; V-03
confirms bare-form equivalence at that position if position qualifies.

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

Each gate header names its axis.

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

## V-04 -- Synthesis-Body Placement (Lifecycle Emphasis, Section-Body Border Probe)

**Axis**: Lifecycle emphasis -- `**Axis-Header Rule**: Each gate header names its axis.`
is placed as the final standalone paragraph inside the Synthesis section body, immediately
after the "If none: Synthesis: no cross-sub-skill patterns found." terminator line and
before the closing `---` divider. The rule is NOT in its own inter-section slot; it is
physically inside the Synthesis section. It is separated from the nearest gate blocks by
the full Consolidated Findings preamble text. The rule is not inside a gate body and
not inside an example block.
**Hypothesis**: C-22 names two disqualifiers: gate body and example block. The Synthesis
section body is neither. C-24 says "any non-buried position." A standalone paragraph at
the end of the Synthesis section is not buried (it is visually isolated from the
surrounding content by line breaks and the `---` terminator). Expected PASS: the
Synthesis section body is not a disqualifying position. If V-04 = 100, "buried" under
C-22 is strictly limited to gate bodies and example blocks, and named section bodies
are qualifying positions. If V-04 fails C-22, a third disqualifier exists: being embedded
within any named section body, regardless of physical isolation within that section.
The distinction between "inside a section's body" and "in its own inter-section slot"
would then matter structurally.

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

## V-05 -- Minimal Production Form (Output Format, Mass-Reduction Probe)

**Axis**: Output format -- strips non-structural explanation prose while preserving
all 17 criteria. Three elements removed: (1) the three slot-name definition lines after
the 3-slot template (`[boundary] = ...`, `[caller/component] = ...`, `[effect] = ...`);
(2) the "All three slots must be specific -- no generic phrases." enforcement note after
the example; (3) the four-line expanded phase descriptions in flow-lifecycle replaced with
single-line imperatives. The 3-slot template string itself, the inline example, the null-
result instructions, the gate correction loops, the coverage summary, and the Axis-Header
Rule (inter-section slot, labeled, R8 V-04 position) are all preserved unchanged.
**Hypothesis**: C-16 requires "the format `[LEVEL] because [boundary] propagates to
[caller/component], [effect]` with all three slots named and at least one inline example."
It does not require slot-name definitions or the "no generic phrases" enforcement note.
Stripping the explanation lines and the enforcement note leaves the template string and
the example intact -- C-16 passes. C-07 requires explicit null-result statements in each
sub-skill section; the "If none: say so explicitly" / "If a phase has no findings, say
so briefly" instructions are preserved. All other criteria are structural (column presence,
gate structure, correction loops) and are unaffected by prose stripping. Expected PASS:
17/17 = 100. Confirms that the slot-name definitions and enforcement note are decorative
relative to C-16 and establishes the minimum-mass production form under v9.

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
