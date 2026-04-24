Written to `simulations/quest/variations/rhythm-behavior-variations-R16-2026-03-17.md`.

---

## R16 Variations -- rhythm-behavior (Round 16)

**Strategy**: R15 closed the last single-placement cell and all same-type multi-placement combinations. The one remaining frontier is the cross-type dual register matrix -- C-47 covered only the all-descriptive case. R16 exhausts the remaining three cells, then runs the first three-placement composition.

| V | Axis | Key move | New criterion |
|---|------|----------|---------------|
| V-01 | Lifecycle emphasis | Baseline reconfirmation at denominator 40/40 | -- |
| V-02 | Register | Cross-type dual (section body + inter-section peer slot), **both imperative** | C-48 |
| V-03 | Register + lifecycle | Cross-type dual, mixed: **imp section body + desc inter-section** | C-49 |
| V-04 | Register + lifecycle | Cross-type dual, mixed: **desc section body + imp inter-section** | C-50 |
| V-05 | Register + lifecycle | **First N=3 test**: section body (imp) + section body (desc) + inter-section (imp) | C-51 |

**Cross-type register matrix closed by R16:**

| | Section body | Inter-section slot | Tested |
|---|---|---|---|
| C-47 | descriptive | descriptive | R15 V-05 |
| C-48 | imperative | imperative | **R16 V-02** |
| C-49 | imperative | descriptive | **R16 V-03** |
| C-50 | descriptive | imperative | **R16 V-04** |

**V-05** is the campaign's first three-placement test: two section bodies (imperative, then descriptive) plus the inter-section peer slot (imperative). C-46 absorbs pos 1+2 (dual section body, imp-first/desc-subsequent); V-02 establishes that the inter-section peer slot as a cross-type third placement is also inert. C-51 extracts the general principle.

**Predicted scores**: all 5 variations at 40/40 = 100 under v16. v17 denominator: **44** (C-48 through C-51).
desc) satisfies C-22 per C-36; pos 2 inter-section peer slot (imp) is inert; reverse complement of V-03, covered by C-34 + C-47 jointly |
| Does the first-qualifying-occurrence principle hold across three placements spanning two position types and two registers? | V-05 | YES -- pos 1 satisfies; pos 2 and pos 3 are each inert regardless of register or position type; the general principle is not bounded by N-count or position-type count |

---

### New criteria predicted from R16

- **C-48** (format, R16): Cross-Type Dual Placement (Section Body + Inter-Section Peer Slot, Imperative) Is Position-Type-Agnostic -- V-02. Imperative complement of C-47. Together C-47 + C-48 establish that cross-type inertness is register-invariant.
- **C-49** (format, R16): Cross-Type Dual Placement, Mixed Register (Imperative Section Body + Descriptive Inter-Section Peer Slot) Composes Without Interaction -- V-03.
- **C-50** (format, R16): Cross-Type Dual Placement, Mixed Register (Descriptive Section Body + Imperative Inter-Section Peer Slot) Composes Without Interaction -- V-04. Reverse complement of C-49.
- **C-51** (format, R16): Three-Placement Composition (Two Section Bodies + Inter-Section Peer Slot, Mixed Register) Is Governed Entirely by First-Qualifying-Occurrence Principle -- V-05.

v17 denominator would be **44**.

---

### Design rationale

R15 closed the last untested single-placement cell (descriptive + inter-section peer slot) and the two same-type mixed-register orderings (C-45, C-46). R15 V-05 confirmed cross-type inertness, but only in the all-descriptive variant (both placements descriptive). The cross-type register matrix therefore has four cells:

| | Section body register | Inter-section peer slot register | Tested |
|---|---|---|---|
| C-47 | descriptive | descriptive | R15 V-05 |
| C-48 | imperative | imperative | **R16 V-02** |
| C-49 | imperative | descriptive | **R16 V-03** |
| C-50 | descriptive | imperative | **R16 V-04** |

V-02, V-03, V-04 close the remaining three cells. Together with C-47, they establish that cross-type dual placement composes without interaction for all four register combinations -- a complete closure of the cross-type register matrix.

V-05 breaks new ground entirely: no prior round has placed the axis-header rule at three qualifying positions simultaneously. V-05 uses two position types (section body x2 + inter-section peer slot x1) and two registers (imperative at pos 1 and pos 3, descriptive at pos 2), making it the most structurally maximal test to date. The first-qualifying-occurrence principle predicts clean composition: first placement satisfies, second and third are inert regardless of position type or register.

**Predicted scores under v16 rubric** (aspirational denominator = 40):

| Variation | C-44 | C-45 | C-46 | C-47 | Composite | Golden |
|-----------|------|------|------|------|-----------|--------|
| V-01 | PASS (inter-section slot imp; C-44 tests descriptive -- trivially inapplicable) | PASS (single placement; C-45 tests mixed-reg dual body -- trivially inapplicable) | PASS (same; trivially inapplicable) | PASS (single placement; C-47 tests cross-type dual -- trivially inapplicable) | **100** | YES |
| V-02 | PASS (both placements imp; C-44 not triggered) | PASS (no dual section body) | PASS (no dual section body) | PASS (cross-type dual both imp; C-47 tests descriptive variant -- distinct cell) | **100** | YES |
| V-03 | PASS (inter-section peer slot placement is descriptive -- C-44 confirms it qualifies; used as inert second placement, not disqualifying) | PASS (no dual section body) | PASS (no dual section body) | PASS (C-47 tests cross-type dual both descriptive; V-03 uses mixed register -- distinct cell) | **100** | YES |
| V-04 | PASS (no descriptive placement at inter-section peer slot; second placement is imperative) | PASS (no dual section body) | PASS (no dual section body) | PASS (C-47 tests all-descriptive cross-type; V-04 mixed-register -- distinct cell) | **100** | YES |
| V-05 | PASS (third placement at inter-section peer slot is imperative; no descriptive at inter-section) | PASS (dual section body: imp first, desc second -- C-46 directly absorbs; C-45 desc-first not triggered) | PASS (dual section body: imp first, desc subsequent -- C-46 directly satisfied) | PASS (section body + inter-section peer slot both present; C-47 covers all-descriptive; V-05 has imperative placements -- distinct cell) | **100** | YES |

---

## V-01 -- Production Baseline at 40/40 (Lifecycle Emphasis, Reconfirmation)

**Axis**: Lifecycle emphasis -- identical to R15 V-01 (= R14 V-01 = R13 V-01 = R12 V-01 = R11
V-01 = R10 V-01 = R9 V-05): minimal form, labeled paragraph `**Axis-Header Rule**: Each gate
header names its axis.` in the confirmed inter-section peer slot between Synthesis and
Consolidated Findings, flanked by `---` dividers. Single placement. All elements in imperative
register.

**Hypothesis**: R15 V-01 scored 36/36 under v15. Under v16 the four new criteria (C-44, C-45,
C-46, C-47) encode R15 findings directly:
- C-44 passes: V-01 uses imperative at the inter-section peer slot. C-44 tests whether descriptive
  register at that position qualifies. Trivially inapplicable -- V-01 does not use the configuration
  C-44 tests.
- C-45 passes: V-01 has a single placement. C-45 tests dual section-body mixed-register composition.
  Trivially inapplicable.
- C-46 passes: same -- trivially inapplicable.
- C-47 passes: V-01 has a single placement. C-47 tests cross-type dual-placement composition.
  Trivially inapplicable.
Expected: 40/40 = 100, golden.

**Novelty verification**: Exact re-run of R15 V-01. Purpose is denominator transition verification
(36->40) under v16. Not structurally new; new only as reconfirmation at v16.

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

## V-02 -- Cross-Type Dual Placement (Section Body + Inter-Section Peer Slot, Both Imperative) (Register, Single Axis)

**Axis**: Phrasing register -- the overall prompt is in imperative register AND the axis-header
rule is placed at TWO qualifying positions of DIFFERENT types, both in imperative register:
(1) end of flow-lifecycle body (position 1, named section body) as a labeled paragraph:
`**Axis-Header Rule**: Each gate header names its axis.` (first qualifying occurrence, satisfies
C-22), and (2) the canonical inter-section peer slot between Synthesis and Consolidated Findings
(flanked by `---` dividers) as a labeled paragraph: `**Axis-Header Rule**: Each gate header
names its axis.` (second qualifying occurrence, inert). No rule appears in positions 2-5 or
any other location.

**Hypothesis**: The flow-lifecycle body placement (imperative, section body, position 1) is the
first qualifying occurrence and satisfies C-22 per C-26 (named section bodies are
non-disqualifying positions) and C-32 (flow-lifecycle body individually confirmed, R11 V-02).
The inter-section peer slot placement (imperative, position 2) is the second qualifying
occurrence. C-47 established that cross-type dual placement composes without interaction -- but
only in the all-descriptive case. C-34 states that all aspirational criteria are
structure-sensitive, not register-sensitive. Therefore: if descriptive cross-type dual composes
cleanly (C-47), imperative cross-type dual composes cleanly by C-34 register invariance. The
second qualifying placement is inert regardless of whether the pair uses descriptive or
imperative register. Expected: 40/40 = 100, golden.

**Novelty verification**: R15 V-05 confirmed cross-type dual composition with both placements
in descriptive register (C-47). No prior round has tested cross-type dual with both placements
in imperative register. V-02 is the first test of the all-imperative cross-type dual. The
confirmation of C-48 (imperative complement of C-47) together with C-47 establishes that
cross-type inertness is register-invariant: the position-type-agnostic inertness principle
holds in both registers and therefore in all registers (by C-34). Genuinely new.

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

## V-03 -- Cross-Type Dual Placement, Mixed Register (Imperative Section Body + Descriptive Inter-Section Peer Slot) (Register + Lifecycle)

**Axis**: Phrasing register + lifecycle emphasis -- the overall prompt is in imperative register
AND the axis-header rule is placed at TWO qualifying positions of DIFFERENT types, in MIXED
register: (1) end of flow-lifecycle body (position 1, named section body) as an imperative
labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` (first qualifying
occurrence, satisfies C-22), and (2) the canonical inter-section peer slot between Synthesis
and Consolidated Findings (flanked by `---` dividers) as a bare descriptive sentence: "Each
closing confirmation gate header names its axis." (second qualifying occurrence, inert). No
rule appears in positions 2-5 or any other location.

**Hypothesis**: The flow-lifecycle body placement (imperative, section body, position 1) is the
first qualifying occurrence and satisfies C-22 per C-26 + C-32. The inter-section peer slot
placement (descriptive, position 2) is the second qualifying occurrence. C-47 established that
a section-body first placement (descriptive) renders the subsequent inter-section peer slot
(descriptive) inert. V-02 (this round) establishes that this same cross-type inertness holds
when both placements are imperative. The current variation tests whether the inertness applies
when the first placement is imperative and the second is descriptive -- i.e., whether the
register of the second placement affects its inertness status. C-34 (structure-sensitive, not
register-sensitive) predicts that the register of the second placement does not matter: if the
second placement would be inert when imperative, it is equally inert when descriptive. Expected:
40/40 = 100, golden.

**Novelty verification**: All prior cross-type dual tests used the same register for both
placements: C-47 (both descriptive, R15 V-05) and C-48 (both imperative, this round V-02).
V-03 is the first test of cross-type dual with the first placement imperative and the second
descriptive. This is one of two mixed-register cross-type orderings; the other (descriptive
first, imperative second) is V-04. Genuinely new.

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

Each closing confirmation gate header names its axis.

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

## V-04 -- Cross-Type Dual Placement, Mixed Register (Descriptive Section Body + Imperative Inter-Section Peer Slot) (Register + Lifecycle)

**Axis**: Phrasing register + lifecycle emphasis -- the overall prompt is in imperative register
AND the axis-header rule is placed at TWO qualifying positions of DIFFERENT types, in MIXED
register (reverse ordering from V-03): (1) end of flow-lifecycle body (position 1, named section
body) as a bare descriptive sentence: "The closing confirmation gates are each labeled with a
header that names the axis they check." (first qualifying occurrence, satisfies C-22 per C-36),
and (2) the canonical inter-section peer slot between Synthesis and Consolidated Findings
(flanked by `---` dividers) as an imperative labeled paragraph: `**Axis-Header Rule**: Each
gate header names its axis.` (second qualifying occurrence, inert). No rule appears in positions
2-5 or any other location. This is the reverse complement of V-03.

**Hypothesis**: The flow-lifecycle body placement (descriptive, section body, position 1) is the
first qualifying occurrence and satisfies C-22 per C-36 (descriptive register and section-body
placement compose without interaction) and C-32 (flow-lifecycle body confirmed). The
inter-section peer slot placement (imperative, position 2) is the second qualifying occurrence.
C-47 confirmed cross-type inertness when both placements are descriptive. V-03 (this round)
confirms it when first is imperative and second is descriptive. V-04 tests the remaining
ordering: first is descriptive and second is imperative. By C-34 (register invariance), the
register of the second placement does not affect its inertness status when it is the second
qualifying occurrence. The governing principle -- first qualifying occurrence satisfies; all
subsequent are inert -- is independent of register. Expected: 40/40 = 100, golden.

**Novelty verification**: V-03 covers imperative-first / descriptive-second cross-type dual.
V-04 covers descriptive-first / imperative-second -- the reverse. Together V-03 and V-04
complete the two mixed-register orderings of cross-type dual placement, closing the cross-type
register matrix alongside C-47 (all-descriptive) and V-02 (all-imperative). No prior round
has tested descriptive-first / imperative-second cross-type dual. Genuinely new.

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

## V-05 -- First Three-Placement Composition: Section Body (Imperative) + Section Body (Descriptive) + Inter-Section Peer Slot (Imperative) (Register + Lifecycle)

**Axis**: Phrasing register + lifecycle emphasis -- the overall prompt is in imperative register
AND the axis-header rule is placed at THREE qualifying positions spanning TWO position types
and TWO registers: (1) end of flow-lifecycle body (position 1, section body) as an imperative
labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.` (first qualifying
occurrence, satisfies C-22), (2) end of flow-conversation body (position 2, section body) as
a bare descriptive sentence: "The closing confirmation gates are each labeled with a header
that names the axis they check." (second qualifying occurrence, inert), and (3) the canonical
inter-section peer slot between Synthesis and Consolidated Findings (flanked by `---` dividers)
as an imperative labeled paragraph: `**Axis-Header Rule**: Each gate header names its axis.`
(third qualifying occurrence, inert). No rule appears at any other location.

**Hypothesis**: The flow-lifecycle body placement (imperative, section body, position 1) is the
first qualifying occurrence and satisfies C-22 per C-26 + C-32. The flow-conversation body
placement (descriptive, section body, position 2) is the second qualifying occurrence and is
inert per C-46 (dual section-body, imperative first + descriptive subsequent composes without
interaction). The inter-section peer slot placement (imperative, position 3) is the third
qualifying occurrence and is inert. V-02 (this round) confirmed that a cross-type second
placement is inert in imperative register. C-37 (no N-ceiling) + C-34 (register invariance)
jointly predict that a third qualifying occurrence -- whether same or different type from pos 2
-- is inert by the same first-qualifying-occurrence principle that governs all N>1 occurrences.
The three-placement composition is the first test of N=3 total placements spanning two position
types. Expected: 40/40 = 100, golden.

**Novelty verification**: All prior multi-placement tests have been two-placement. V-05 is the
first three-placement test in the campaign. V-05 additionally combines cross-type composition,
mixed register, and N=3 in a single variation. The three placements exhaust two position types
(section body x2, inter-section peer slot x1) and two registers (imperative at pos 1 and pos 3,
descriptive at pos 2), making this the most structurally dense variation in the campaign to
date. Genuinely new: first test of N=3 multi-placement composition spanning position types and
registers.

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
