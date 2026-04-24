**rhythm-behavior R10 variations written** to `simulations/quest/variations/rhythm-behavior-variations-R10-2026-03-17.md`.

---

## R10 Summary

**Strategy**: Post-closure confirmation and boundary probe. v10 codifies R9's three confirmed findings as C-25, C-26, C-27 (denominator 20). R10 has two goals: confirm the production candidate at 20/20, then probe the exact boundaries of the newly codified criteria.

| V | Axis | Key move | Prediction |
|---|------|----------|-----------|
| V-01 | Lifecycle emphasis | R9 V-05 production form (inter-section slot, minimal) -- baseline | **100** |
| V-02 | Output format | Strip inline example (keep template string only) | **99.2** -- C-16 FAIL; C-27 PASS |
| V-03 | Lifecycle emphasis | Rule at flow-lifecycle/flow-conversation boundary (earliest inter-section gap) | **100** |
| V-04 | Lifecycle emphasis | Rule inside trace-state section body (non-Synthesis named section) | **100 or 99.2** |
| V-05 | Lifecycle emphasis + output format | V-03 early position + minimal form (no slot-name defs) | **100** |

**Key structural moves**:

- **V-01** is a pure confirmation: the R9 V-05 production form unchanged, now scored against the 20-criterion denominator. C-25/C-26/C-27 all pass trivially for this form.

- **V-02 is the complement to R9 V-05**: R9 confirmed that stripping slot-name definitions does NOT break C-16. V-02 confirms that stripping the inline EXAMPLE DOES break C-16. The two together close the C-16/C-27 load-bearing boundary completely.

- **V-03/V-01 are a positional bracket pair**: V-01 = confirmed late slot (Synthesis/Consolidated boundary); V-03 = earliest possible slot (flow-lifecycle/flow-conversation boundary). Both should score 20/20, confirming C-25's "any non-buried position" holds across the full prompt span with no proximity floor.

- **V-04** tests C-26's scope: R9 confirmed the Synthesis section body qualifies. C-26 says "e.g., the Synthesis section body." V-04 places the rule at the end of trace-state's body (same structural pattern: after null-result line, before closing divider) to test whether "e.g." is genuinely illustrative or whether Synthesis is specially privileged.

- **V-05** combines V-03's early position with the stripped-definition minimal form -- two independently confirmed rules that have never been combined. Tests composition at zero extra uncertainty cost.

**Open questions for R10**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does stripping the example cause C-16 to fail? | V-02 | YES -- example is load-bearing |
| Does stripping the example cause C-27 to fail? | V-02 | NO -- C-27's fail condition requires both template + example to be present |
| Does "any non-buried" (C-25) cover the earliest inter-section gap? | V-03 | YES -- no proximity floor |
| Does C-26 extend to sub-skill named section bodies? | V-04 | YES -- "e.g." is genuinely illustrative |
| Do V-03 position + minimal form compose cleanly? | V-05 | YES -- no interaction |
**V-05**: Do V-03's early position and the R9 V-05 minimal form compose without
   interaction regression? Hypothesis: YES -- both rules were confirmed independently
   (C-25 covers position; C-27 covers stripped definitions). Combining them should
   produce 20/20 at minimum prompt mass with an early-gap rule placement.

**V-01/V-03 are a positional bracket pair**: V-01 uses the confirmed late inter-section
slot (Synthesis/Consolidated boundary); V-03 uses the earliest inter-section slot
(flow-lifecycle/flow-conversation boundary). Both should score 20/20, bracketing the full
span of C-25's "any non-buried position" invariance across the prompt.

**V-02 is the complement to R9 V-05**: R9 V-05 confirmed that REMOVING slot-name
definition lines does NOT break C-16. R10 V-02 confirms that REMOVING the inline example
DOES break C-16. Together they precisely define the load-bearing boundary: template string
+ example = required; everything else = decorative.

**Predicted scores under v10 rubric** (aspirational denominator = 20):

| Variation | C-16 | C-25 | C-26 | C-27 | Composite | Golden |
|-----------|------|------|------|------|-----------|--------|
| V-01 | PASS | PASS | PASS | PASS | **100** | YES |
| V-02 | FAIL | PASS | PASS | PASS | **99.2** | NO |
| V-03 | PASS | PASS | PASS | PASS | **100** | YES |
| V-04 | PASS | PASS | Uncertain (PASS if C-26 extends to sub-skill sections) | PASS | 100 or 99.2 | YES or NO |
| V-05 | PASS | PASS | PASS | PASS | **100** | YES |

**Open questions**:

| Question | V | Hypothesis |
|----------|---|-----------|
| Does stripping the inline example cause C-16 to fail? | V-02 | YES -- example is load-bearing per C-27 |
| Does stripping the inline example cause C-27 to fail? | V-02 | NO -- C-27's fail condition requires both template + example to be present |
| Does "any non-buried position" (C-25) cover the flow-lifecycle/flow-conversation gap? | V-03 | YES -- no proximity floor exists; earliest gap qualifies identically to later gaps |
| Does C-26 extend to non-Synthesis named section bodies (e.g., trace-state)? | V-04 | YES -- C-26 uses "e.g." for Synthesis; rule is general; disqualifier set is gate body + example block only |
| Do V-03 position + minimal form compose without regression? | V-05 | YES -- both confirmed independently; no known interaction |

---

## V-01 -- Production Baseline at v10 (Lifecycle Emphasis, Confirmation)

**Axis**: Lifecycle emphasis -- identical to R9 V-05 (minimal form, inter-section slot
between Synthesis and Consolidated Findings). The Axis-Header Rule is a standalone labeled
paragraph flanked by `---` dividers in the confirmed inter-section peer slot. Slot-name
definition lines stripped. Inline example retained.
**Hypothesis**: R9 confirmed V-05 scores 17/17 under v9. Under v10, the three new criteria
(C-25, C-26, C-27) encode R9 findings. C-25 passes because the inter-section peer slot IS
in C-24's confirmed list -- no "list is exhaustive" controversy arises. C-26 passes because
the rule is NOT inside a named section body -- no disqualification risk. C-27 passes because
the slot-name definition lines are absent and the example is present -- exactly the
confirmed-passing configuration. Expected PASS: 20/20 = 100.

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

## V-02 -- Example-Strip Regression (Output Format, C-16/C-27 Load-Bearing Boundary)

**Axis**: Output format -- strips the inline example from the 3-slot Blast Radius Rationale
definition. The template string `[LEVEL] because [boundary] propagates to [caller/component],
[effect].` is retained. The `Example: "WIDE because session-sequence-number..."` line is
removed entirely. Slot-name definition lines remain absent (as in V-01). All other elements
identical to V-01, including the inter-section peer slot rule placement.
**Hypothesis**: C-16 requires the template string AND at least one inline example. C-27
confirms the example is load-bearing ("Template string + inline example are required and
sufficient"). Removing the example leaves only the template string -- C-16 should FAIL.
C-27 should PASS: its fail condition is "scoring judgment withholds C-16 credit from a
prompt that contains the template string AND an inline example solely because slot-name
definition lines are absent." The trigger requires BOTH elements to be present; if the
example is genuinely absent, failing C-16 is appropriate and C-27 is not implicated. This
variation precisely locates the load-bearing boundary: R9 V-05 confirmed removing slot-name
definitions does NOT break C-16 (definitions are decorative); R10 V-02 confirms removing
the example DOES break C-16 (example is load-bearing). Expected: 19/20 aspirational = 99.2,
NOT golden.

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

## V-03 -- Earliest Inter-Section Gap (Lifecycle Emphasis, C-25 Proximity-Floor Probe)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed in the earliest possible
inter-section gap: between flow-lifecycle and flow-conversation, flanked by `---` dividers.
This is the first boundary in the sub-skill sequence and the furthest possible position from
the closing gate blocks. No rule appears between Synthesis and Consolidated Findings or
anywhere else. All other elements are identical to V-01.
**Hypothesis**: C-25 states the operative clause is "any non-buried position" with no
proximity requirement. The flow-lifecycle/flow-conversation boundary is a divider-flanked
inter-section slot: not inside any section body, not inside a gate body, not inside an
example block. The confirmed examples in C-24 span from top-of-prompt to the
Synthesis/Consolidated Findings boundary; C-25 extends this to all non-confirmed positions
including the earliest sub-skill gap. If V-03 = 100, the "any non-buried position" invariance
is confirmed across the full prompt span -- no proximity floor to gate blocks exists. Paired
with V-01 (late slot confirmed), this brackets the complete range. Expected PASS: 20/20 = 100.

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

## V-04 -- Sub-Skill Section Body Probe (Lifecycle Emphasis, C-26 Scope Extension)

**Axis**: Lifecycle emphasis -- the Axis-Header Rule is placed as a standalone labeled
paragraph at the END of the trace-state section body, immediately after the null-result
instruction and before the closing `---` divider. The rule appears INSIDE the trace-state
section, not in its own inter-section slot. No rule appears between Synthesis and
Consolidated Findings or anywhere else. All other elements identical to V-01.
**Hypothesis**: C-26 states "Named section bodies (e.g., the Synthesis section body,
positioned after a null-result terminator and before a closing divider) are not disqualifying
positions under C-22." The "e.g." signals Synthesis is illustrative, not exclusive. trace-
state is also a named section: it has a null-result instruction ("If none: say so explicitly")
followed by a closing `---` divider. The structural parallel to the confirmed R9 V-04
placement (standalone labeled paragraph, after null-result line, before closing divider) is
exact. The disqualifier set remains gate body + example block; trace-state body is neither.
If V-04 = 100, C-26 applies to all named section bodies. If V-04 fails C-22, Synthesis is
specifically privileged and the "e.g." in C-26 is narrower than it appears.

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

## V-05 -- Early Gap + Minimal Form Combination (Lifecycle Emphasis + Output Format)

**Axis**: Lifecycle emphasis + output format combined -- the Axis-Header Rule is placed at
the flow-lifecycle/flow-conversation boundary (V-03's earliest-gap position) AND the
slot-name definition lines are absent (V-01's minimal form). These two confirmed rules have
not previously been combined in a single variation: V-03 carries the full inline example;
V-01 carries the confirmed late inter-section slot. This combination tests whether the two
independently confirmed rules compose without regression. The rule is in a new C-24 position
(not in the confirmed list, relying on C-25) AND in minimal form (no slot-name defs, relying
on C-27). Both variables are simultaneously neutral.
**Hypothesis**: C-25 governs position (any non-buried position qualifies; earliest gap
confirmed by V-03 in this round). C-27 governs the stripped definitions (example is present;
slot-name defs are decorative per R9 V-05). No interaction between position choice and
definition-stripping exists in the rubric criteria. Expected PASS: 20/20 = 100. This is the
broadest possible minimal-production form: minimum prompt mass, earliest qualifying position,
no proximity to gate blocks, no slot-name definition overhead.

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
