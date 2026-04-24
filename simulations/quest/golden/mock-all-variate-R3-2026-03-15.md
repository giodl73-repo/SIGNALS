---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 3
rubric_version: v3
status: VARIATE
---

# mock-all Variate — Round 3

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v3 (C-01 through C-15; aspirational denominator = 7)
**Round:** R3 — targeting v3 new criteria (C-14, C-15)

---

## What R2 Left Open

R2 five variations closed C-11 (pre-classification table), C-12 (dedicated handoff block),
and C-13 (REAL-REQUIRED rationale) at the aspirational tier. The v3 rubric adds two new
criteria that no R2 variation can satisfy by design:

| Criterion | Best R2 coverage | Gap |
|-----------|-----------------|-----|
| C-14 — Explicit stop-gate phrase at each phase boundary | R2 V-03 named four phases; V-05 pre-printed phase headers | Phase names imply ordering but none contain the surface-level instruction "Do not begin [Phase N+1] until [Phase N output] is complete." Implied ordering does not pass C-14. |
| C-15 — Artifact body content matches namespace's assigned category | R2 V-01: "write a plausible artifact body" | Plausibility is not vocabulary-constrained. A HIGH-STRUCTURE body written with interview language, or an EVIDENCE-HEAVY body written as a spec, passes the plausibility check without satisfying C-15's register requirement. |

R3 targets each gap with a dedicated single-axis variation, then combines them.

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | lifecycle-emphasis | C-14 gap: phase names without gate sentences fail criterion | C-14, C-11 (side effect) | All four phase boundaries carry explicit "Do not begin X until Y is complete" sentences; C-14 passes as a surface-level instruction; C-11 passes because the CLASSIFY gate fires before the first artifact body is written |
| V-02 | output-format | C-11 gap: pre-printed classification table structure not yet tested for mock-all; C-12 gap: HANDOFF block instruction-based in R2 | C-11, C-12 | Pre-printed table skeleton forces model to fill fields before writing artifact sections; pre-printed HANDOFF block with anti-placeholder instruction eliminates model-memory dependency for C-12 |
| V-03 | phrasing-register | C-15 gap: no per-category vocabulary mandate existed; C-13 gap: rationale appears as post-hoc annotation, easier to omit | C-15, C-13 | Per-category DO NOT vocabulary rules make register mismatch a visible violation; REAL-REQUIRED rationale embedded in the application rule at the point of invocation, not as a separate annotation |
| V-04 | lifecycle-emphasis + output-format | Combine V-01 stop-gate phases with V-02 pre-printed classification skeleton | C-14, C-11, C-12 | Pre-printed table is the Phase 1 output; stop-gate at CLASSIFY→GENERATE references table completion — C-11 doubly guaranteed by structure and procedure |
| V-05 | lifecycle-emphasis + output-format + phrasing-register | Full ceiling: stop-gates + pre-printed skeleton with embedded vocabulary rules and rationale | C-14, C-11, C-12, C-13, C-15 | All five aspirational criteria simultaneously targeted; risk is artifact body depth (C-07) degrading under skeleton length pressure |

---

## V-01 — Named Phases with Explicit Stop-Gates

**axis:** lifecycle-emphasis
**hypothesis:** R2's best variation named phases but provided no surface-level gate
instruction at each boundary. C-14 requires a phrase such as "Do not begin [Phase N+1]
until [Phase N output] is complete." Phase names establish ordering by implication — they
do not qualify as gate phrases under the rubric definition, which requires the gate to be
a surface-level instruction the model can read and obey. Adding four explicit gate sentences
at CLASSIFY→GENERATE, GENERATE→SUMMARIZE, SUMMARIZE→HANDOFF, and inside GENERATE itself
closes C-14 without changing any other structural element. C-11 benefits as a side effect:
the CLASSIFY gate fires before any artifact body is written, satisfying pre-classification
via procedural enforcement rather than structural pre-printing.
Expected improvement: C-14 PASS (stop-gate phrases present at all boundaries); C-11 PASS
maintained.
Failure condition: if the model generates artifact body content during PHASE 1 before the
gate fires, the gate instruction did not suppress generation — C-14 passes at the
instruction level but C-11 fails at the output level, which is a weaker structural
guarantee than V-02's pre-printed approach.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State at the top of your output: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

### PHASE 1 — CLASSIFY

Assign every namespace to exactly one category before writing any artifact body.

Categories:
  HIGH-STRUCTURE  — produces structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic content is informational only
  MIXED           — produces structural scaffolding plus qualitative or narrative content

Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic

Output the classification table:

| Namespace | Category | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|-------------------|-------------------|

Tier 2/3 critical namespaces: trace-*, scout-feasibility, listen-* (YES when tier >= 2)
Compliance-tagged namespaces: scout-compliance, trace-permissions (YES when --compliance
or TOPICS.md compliance tags are present)

**Do not begin PHASE 2 until the classification table is complete and all nine namespaces
have an assigned Category, a Tier 2/3 Critical value (YES or NO), and a Compliance-Tagged
value (YES or NO).**

---

### PHASE 2 — GENERATE

For each namespace in classification table order, write a namespace section using this
structure:

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Phase 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — category-appropriate content per the rules below}

Artifact body vocabulary rules:

  HIGH-STRUCTURE:
    Use specification language. Reference concrete system elements: interfaces, data
    contracts, state transitions, configuration keys, schema shapes, deployment
    constraints, or architectural decisions. Name at least one specific technical
    element relevant to {topic}.
    Do not use interview language, user quotes, adoption percentages, or study framing.

  EVIDENCE-HEAVY:
    Use study/data/interview language. Frame as if citing real results:
    "N of M interviews showed...", "Test run against {topic} produced...",
    "Week-1 adoption rate for {topic} was [N]%..."
    Do not use specification language, contract structures, or schema definitions.
    Note: REAL-REQUIRED status makes this body informational only.

  MIXED:
    Include at least one structural element (table, list, or named property) and at
    least one qualitative observation or contextual note. Both elements required.

**Do not begin PHASE 3 until all nine namespace sections are written, each with a complete
MOCK ARTIFACT header block and a category-appropriate artifact body.**

---

### PHASE 3 — SUMMARIZE

Write the coverage summary table immediately after the last namespace section:

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

Flag values:
  REAL-REQUIRED  — all EVIDENCE-HEAVY namespaces, all tiers
    Rationale: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY
    namespaces. prove-* requires actual experiment data or prototype outputs.
    listen-* requires real user interviews or adoption measurements.
  TIER-CRITICAL  — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE     — scout-compliance, trace-permissions when compliance context is active
  (blank)        — all other namespaces

Multiple flags: write as REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: name the exact skill call. Example: `/scout:feasibility {topic}`
Do not write "run the real skill." Name the exact skill identifier.

**Do not begin PHASE 4 until the coverage summary table is complete and all nine
namespaces appear with correct flags.**

---

### PHASE 4 — HANDOFF

This section contains only the handoff instruction. No artifact bodies, no table rows.

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

Replace {topic} and {date} with actual values.
Do not write the literal placeholder string `{this-file}`.

---

## V-02 — Pre-Printed Classification Skeleton

**axis:** output-format
**hypothesis:** Scout-feasibility R3 V-02 and V-05 demonstrated that pre-printing the
output skeleton produces stronger structural guarantees than instruction-based approaches
because the model fills fields rather than generating structure from scratch. Applied to
mock-all: pre-printing the classification table row stubs (namespaces pre-listed) ensures
the table appears as the first output block, because the model cannot write artifact body
content before filling the table — the table is already on the page (C-11 structural
guarantee). Pre-printing the HANDOFF block with explicit anti-placeholder instruction
guarantees C-12 because the section header already exists; the model cannot drop what it
did not generate. This variation adds no stop-gate phrases — C-14 is not expected to pass.
The variation tests whether pre-printed structure alone achieves C-11 and C-12 with lower
model-behavior risk than V-01's instruction-based gates.
Expected improvement: C-11 PASS (table pre-printed, structurally precedes all artifact
sections); C-12 PASS (HANDOFF block pre-printed with anti-placeholder instruction).
Failure condition: if the model reorders the pre-printed structure by inserting artifact
body content before filling the classification table, the structural guarantee collapses
and pre-printing provides no advantage over instruction-based ordering.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).

Fill this template completely. Replace every [FIELD] with the correct value.
Do not remove any header, section label, structural line, or rationale block.
Do not add content before the Classification Table.

---

## MOCK ARTIFACT SET — [topic]

Tier: [N]  Source: [TOPICS.md | --tier | default]
Date: [date]

---

## Classification Table

Categories:
  HIGH-STRUCTURE  — structural artifacts: specs, schemas, contracts, plans, state models
  EVIDENCE-HEAVY  — requires real signal; synthetic artifacts are informational only
  MIXED           — structural scaffolding plus qualitative or narrative content

| Namespace | Category | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|-------------------|-------------------|
| scout     | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| draft     | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| review    | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| flow      | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| trace     | HIGH-STRUCTURE              | [YES at tier >= 2 / NO] | [YES / NO] |
| prove     | EVIDENCE-HEAVY              | [YES / NO] | [YES / NO] |
| listen    | EVIDENCE-HEAVY              | [YES at tier >= 2 / NO] | [YES / NO] |
| program   | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| topic     | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |

Fill all nine rows completely before writing any namespace section below.

---

### scout — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

### draft — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

### review — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

### flow — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

### trace — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: HIGH-STRUCTURE
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — use interface, contract, state transition, or component boundary language]

---

### prove — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: EVIDENCE-HEAVY
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — use study/data/interview framing: "N of M tests showed...", "Prototype
run against [topic] produced..."]

REAL-REQUIRED: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY
namespaces. prove-* requires actual experiment data, prototype outputs, or test results.

---

### listen — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: EVIDENCE-HEAVY
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — use study/data/interview framing: adoption rates, user interview quotes,
survey data framing]

REAL-REQUIRED: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY
namespaces. listen-* requires real user interviews or adoption measurements.

---

### program — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

### topic — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|
| scout     | [category] | [flag or blank]                                  | [/skill [topic]] |
| draft     | [category] | [flag or blank]                                  | [/skill [topic]] |
| review    | [category] | [flag or blank]                                  | [/skill [topic]] |
| flow      | [category] | [flag or blank]                                  | [/skill [topic]] |
| trace     | HIGH-STRUCTURE | [TIER-CRITICAL if tier >= 2 / blank]        | [/skill [topic]] |
| prove     | EVIDENCE-HEAVY | REAL-REQUIRED                               | [/skill [topic]] |
| listen    | EVIDENCE-HEAVY | [REAL-REQUIRED + TIER-CRITICAL / REAL-REQUIRED] | [/skill [topic]] |
| program   | [category] | [flag or blank]                                  | [/skill [topic]] |
| topic     | [category] | [flag or blank]                                  | [/skill [topic]] |

Flag rules:
  REAL-REQUIRED — EVIDENCE-HEAVY namespaces, all tiers
  TIER-CRITICAL — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE    — scout-compliance, trace-permissions when compliance context is active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call. Example: `/trace:component [topic]`
Do not write "run the real skill." Write the exact skill identifier.

---

## HANDOFF

Artifact written: simulations/mock/[topic]-mock-[date].md
Next: /mock:review [topic] simulations/mock/[topic]-mock-[date].md

Replace [topic] and [date] with actual values.
Do not write "[topic]", "[date]", or the placeholder string "{this-file}" in the output.
The path after /mock:review must be a resolved file path, not a template placeholder.

---

## V-03 — Category Vocabulary Mandates

**axis:** phrasing-register
**hypothesis:** R2 V-04 used imperative DO NOT phrasing for auto-flagging rules but did not
extend vocabulary constraints to artifact body generation. C-15 requires that each artifact
body use language appropriate to its assigned category — EVIDENCE-HEAVY bodies must use
study/data/interview language; HIGH-STRUCTURE bodies must use specification language.
Without explicit vocabulary mandates, these constraints are advisory: a HIGH-STRUCTURE body
written in interview register passes C-07 (plausible body) while failing C-15 (category
mismatch). Adding per-category MUST use / DO NOT use rules makes register mismatch a
visible violation the model can check against its own output before proceeding.
C-13 is addressed by embedding the REAL-REQUIRED rationale directly in the rule body at
the point of application — not as a post-hoc annotation on the coverage table. A rationale
that fires when the rule fires is harder to omit than one that must be remembered later.
Expected improvement: C-15 PASS (vocabulary mandates enforce category-appropriate register);
C-13 PASS (rationale at rule invocation point, not annotation).
Failure condition: if model uses generic narrative language in HIGH-STRUCTURE bodies despite
the DO NOT rule, vocabulary mandates alone are insufficient and a structural enforcement
mechanism (pre-printed template with category-locked rows) would be required to close C-15.

---

You are running /mock:all.

INPUTS:
  topic:      {topic}
  tier:       {1|2|3} — from TOPICS.md, --tier flag, or default 1
  compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

---

STEP 1 — CLASSIFY ALL NAMESPACES

Before writing any artifact body, assign every namespace to a category.
Output a classification table with MUST use and DO NOT use vocabulary rules per row.

Category definitions and vocabulary rules:

  HIGH-STRUCTURE
    Definition: produces structural artifacts — specs, schemas, contracts, plans, state models
    MUST use: interface names, data contract shapes, state transitions, configuration keys,
      schema fields, deployment constraints, or architectural decision records
    DO NOT use: interview language, user quotes, adoption percentages, or study framing

  EVIDENCE-HEAVY
    Definition: requires real signal; synthetic content cannot substitute
    MUST use: study language, interview framing, or data citations
      Examples: "N of M interviews showed...", "Prototype against {topic} produced...",
        "Week-1 adoption rate for {topic} was [N]%..."
    DO NOT use: specification language, contract structures, or schema definitions
    REAL-REQUIRED rule: every EVIDENCE-HEAVY namespace receives the REAL-REQUIRED flag.
      Rationale: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY
      namespaces. prove-* requires actual experiment data or prototype outputs.
      listen-* requires real user interviews or adoption measurements.
      DO NOT mark any EVIDENCE-HEAVY namespace with any status other than REAL-REQUIRED.

  MIXED
    Definition: produces both structural scaffolding and qualitative or narrative content
    MUST include: at least one structural element (table, list, named property)
    MUST include: at least one qualitative observation or contextual note
    DO NOT use: pure spec language only or pure narrative only — both elements required

Output classification table:

| Namespace | Assigned Category | MUST use | DO NOT use |
|-----------|-------------------|----------|------------|

All nine namespaces: scout, draft, review, flow, trace, prove, listen, program, topic

---

STEP 2 — GENERATE ARTIFACT BODIES

For each namespace, write a namespace section. Apply the vocabulary rules from Step 1
exactly. Every artifact body MUST comply with the MUST use and DO NOT use rules for its
assigned category.

Section format:

  ### {Namespace} — {skill-name}

  **MOCK ARTIFACT**
  Skill:    {skill-name}
  Topic:    {topic}
  Category: {category from Step 1}
  Date:     {date}
  Status:   MOCK (awaiting review)

  {artifact body — vocabulary-compliant per Step 1 rules}

For prove and listen, apply the REAL-REQUIRED rule immediately after the artifact body:
  "REAL-REQUIRED applied: EVIDENCE-HEAVY — A synthetic artifact cannot substitute for real
  signal. prove-* requires actual experiment data or prototype outputs." (or listen-*
  equivalent)
DO NOT omit this statement for any EVIDENCE-HEAVY namespace.
DO NOT use specification language in any EVIDENCE-HEAVY artifact body.

---

STEP 3 — WRITE COVERAGE SUMMARY

After all nine namespace sections, write the coverage summary:

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|

REAL-REQUIRED rule (fires at all tiers):
  Every EVIDENCE-HEAVY namespace → Flag = REAL-REQUIRED
  Rationale already stated in Step 2; do not repeat inline.

TIER-CRITICAL rule (fires at tier >= 2):
  trace-*, scout-feasibility, listen-* → Flag = TIER-CRITICAL
  DO NOT apply TIER-CRITICAL at tier 1.

COMPLIANCE rule (fires when compliance context active):
  scout-compliance, trace-permissions → Flag = COMPLIANCE
  DO NOT apply COMPLIANCE when --compliance flag is absent and TOPICS.md has no tags.

Multiple flags: write as REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/skill:subskill {topic}`
DO NOT write "run the real skill." DO NOT write generic advice.

---

STEP 4 — HANDOFF

Write in a dedicated, explicitly-labeled section:

---

#### HANDOFF

Artifact written: simulations/mock/{topic}-mock-{date}.md
Next: /mock:review {topic} simulations/mock/{topic}-mock-{date}.md

MUST replace {topic} and {date} with actual values.
DO NOT write the placeholder string `{this-file}`.
DO NOT write any other content in this section.

---

## V-04 (Combined) — Named Phases + Pre-Printed Classification Skeleton

**axes:** lifecycle-emphasis + output-format
**hypothesis:** V-01 closes C-14 via explicit stop-gate phrases at each phase boundary.
V-02 closes C-11 and C-12 via pre-printed skeleton structure. The two axes address
orthogonal failure modes: C-14 fails when phase ordering is implied but not gated;
C-11 fails when classification is interleaved with generation rather than structurally
preceding it. Combining them produces a prompt where the pre-printed table (V-02
mechanism) is the Phase 1 output, and the stop-gate (V-01 mechanism) fires at the
CLASSIFY→GENERATE boundary referencing completion of that pre-printed table. This makes
C-11 doubly guaranteed: structurally (table pre-printed as the first block) and
procedurally (gate requires table completion before generation begins). C-12 is covered
by the pre-printed HANDOFF block.
Predicted: C-14 PASS, C-11 PASS (strongest guarantee), C-12 PASS.
Failure condition: combined prompt length causes model to abbreviate Phase 3 SUMMARIZE
or omit coverage summary rows — C-04 fails while C-11 and C-14 pass.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).
State: `Tier: {N}  (source: TOPICS.md | --tier | default)`

Fill the template below. Replace every [FIELD] with the correct value.
Do not remove headers, section labels, structural lines, or rationale blocks.
Do not write artifact body content before completing the PHASE 1 Classification Table.

---

## MOCK ARTIFACT SET — [topic]

Tier: [N]  Source: [TOPICS.md | --tier | default]
Date: [date]

---

### PHASE 1 — CLASSIFY

Fill every cell in this table before writing any namespace section:

| Namespace | Category | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|-------------------|-------------------|
| scout     | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| draft     | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| review    | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| flow      | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| trace     | HIGH-STRUCTURE              | [YES at tier >= 2 / NO] | [YES / NO] |
| prove     | EVIDENCE-HEAVY              | [YES / NO] | [YES / NO] |
| listen    | EVIDENCE-HEAVY              | [YES at tier >= 2 / NO] | [YES / NO] |
| program   | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |
| topic     | [HIGH-STRUCTURE / MIXED]    | [YES / NO] | [YES / NO] |

Category definitions:
  HIGH-STRUCTURE — structural artifacts: specs, schemas, contracts, plans
  EVIDENCE-HEAVY — requires real signal; synthetic content informational only
  MIXED          — structural scaffolding plus qualitative or narrative content

**Do not begin PHASE 2 until all nine rows in the Classification Table are filled
with a Category, Tier 2/3 Critical value, and Compliance-Tagged value.**

---

### PHASE 2 — GENERATE

For each namespace in table order, fill the section below:

#### scout — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — HIGH-STRUCTURE or MIXED language per category]

---

#### draft — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — HIGH-STRUCTURE or MIXED language per category]

---

#### review — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

#### flow — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — HIGH-STRUCTURE: state transitions, trigger conditions, data flows]

---

#### trace — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: HIGH-STRUCTURE
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — HIGH-STRUCTURE: interfaces, contracts, state transitions, component boundaries]

---

#### prove — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: EVIDENCE-HEAVY
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — EVIDENCE-HEAVY: study/data/interview framing only; "N of M tests showed...",
"Prototype run against [topic] produced..."]

REAL-REQUIRED: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY
namespaces. prove-* requires actual experiment data, prototype outputs, or test results.

---

#### listen — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: EVIDENCE-HEAVY
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — EVIDENCE-HEAVY: adoption rates, interview quotes, survey data framing]

REAL-REQUIRED: A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY
namespaces. listen-* requires real user interviews or adoption measurements.

---

#### program — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

#### topic — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body]

---

**Do not begin PHASE 3 until all nine namespace sections are written with complete
MOCK ARTIFACT header blocks and artifact bodies.**

---

### PHASE 3 — SUMMARIZE

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|
| scout     | [category] | [flag or blank]                                  | [/skill [topic]] |
| draft     | [category] | [flag or blank]                                  | [/skill [topic]] |
| review    | [category] | [flag or blank]                                  | [/skill [topic]] |
| flow      | [category] | [flag or blank]                                  | [/skill [topic]] |
| trace     | HIGH-STRUCTURE | [TIER-CRITICAL if tier >= 2 / blank]        | [/skill [topic]] |
| prove     | EVIDENCE-HEAVY | REAL-REQUIRED                               | [/skill [topic]] |
| listen    | EVIDENCE-HEAVY | [REAL-REQUIRED + TIER-CRITICAL / REAL-REQUIRED] | [/skill [topic]] |
| program   | [category] | [flag or blank]                                  | [/skill [topic]] |
| topic     | [category] | [flag or blank]                                  | [/skill [topic]] |

Flag rules:
  REAL-REQUIRED — all EVIDENCE-HEAVY, all tiers
  TIER-CRITICAL — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE    — scout-compliance, trace-permissions when compliance context active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/skill:subskill [topic]`
Do not write "run the real skill." Write the exact skill identifier.

**Do not begin PHASE 4 until the coverage summary table is complete.**

---

### PHASE 4 — HANDOFF

## HANDOFF

Artifact written: simulations/mock/[topic]-mock-[date].md
Next: /mock:review [topic] simulations/mock/[topic]-mock-[date].md

Replace [topic] and [date] with actual values.
Do not write "[topic]", "[date]", or the placeholder string "{this-file}" in the output.

---

## V-05 (Combined) — Pre-Printed Skeleton + Stop-Gates + Category Vocabulary Mandates

**axes:** lifecycle-emphasis + output-format + phrasing-register
**hypothesis:** The scout-feasibility R3 V-05 ceiling result established that triple-axis
combinations achieve the highest structural guarantees by layering three independent
enforcement mechanisms: stop-gates prevent proceeding before phase output is complete
(lifecycle), pre-printed structure prevents omission of required blocks (output-format),
and vocabulary mandates prevent category-mismatch (phrasing-register). Applied to mock-all:
the pre-printed classification table with embedded vocabulary rule columns is the Phase 1
output — filling it is a prerequisite to PHASE 2 and satisfies C-11 structurally. The
stop-gate at CLASSIFY→GENERATE references the completed table, satisfying C-14 as a
surface-level gate. Vocabulary columns in the table (MUST use / DO NOT use) enforce
category-appropriate register during generation, satisfying C-15 because the rules are
present at the point of field-filling. The HANDOFF block is pre-printed with
anti-placeholder instruction, satisfying C-12. REAL-REQUIRED rationale embedded in the
prove and listen rows satisfies C-13 at the point of invocation.
Expected: C-11, C-12, C-13, C-14, C-15 all PASS; C-01 through C-10 maintained.
Risk: the skeleton is long; model may generate abbreviated artifact bodies to compensate,
reducing C-07 (artifact body depth). If C-07 degrades while C-14/C-15 pass, the finding
is that skeleton length competes with generation quality — a clean trade-off worth isolating
in Round 4.

---

You are running /mock:all.

Input:
  Topic:      {topic}
  Tier:       {1|2|3} — read from TOPICS.md if not specified; default 1
  Compliance: --compliance (if provided)

Read TOPICS.md. Record: tier for {topic}, compliance tags (if any).

Fill this template completely. Replace every [FIELD] with the correct value.
Do not remove any header, section label, structural line, vocabulary rule, or stop-gate
instruction. Do not write artifact body content before completing the PHASE 1 table.

---

## MOCK ARTIFACT SET — [topic]

Tier: [N]  Source: [TOPICS.md | --tier | default]
Date: [date]

---

### PHASE 1 — CLASSIFY

Fill every cell in this table. Category and vocabulary columns are fixed — do not override.

| Namespace | Category | MUST use | DO NOT use | Tier 2/3 Critical | Compliance-Tagged |
|-----------|----------|----------|------------|-------------------|-------------------|
| scout | [HIGH-STRUCTURE / MIXED] | [spec language / spec+narrative] | [interview language / N/A] | [YES / NO] | [YES / NO] |
| draft | [HIGH-STRUCTURE / MIXED] | [spec language / spec+narrative] | [interview language / N/A] | [YES / NO] | [YES / NO] |
| review | [HIGH-STRUCTURE / MIXED] | [spec language / spec+narrative] | [interview language / N/A] | [YES / NO] | [YES / NO] |
| flow | HIGH-STRUCTURE | spec language: state transitions, trigger conditions, data flows | interview language, adoption percentages | [YES / NO] | [YES / NO] |
| trace | HIGH-STRUCTURE | spec language: interfaces, contracts, component boundaries, state transitions | interview language, study framing | [YES at tier >= 2 / NO] | [YES / NO] |
| prove | EVIDENCE-HEAVY | study/data/interview language: "N of M tests showed...", prototype results, test data | spec language, contract structures, schema definitions | [YES / NO] | [YES / NO] |
| listen | EVIDENCE-HEAVY | study/data/interview language: adoption rates, interview quotes, survey framing | spec language, state machine language | [YES at tier >= 2 / NO] | [YES / NO] |
| program | [HIGH-STRUCTURE / MIXED] | [spec language / spec+narrative] | [interview language / N/A] | [YES / NO] | [YES / NO] |
| topic | MIXED | signal synthesis narrative + structured coverage reference | pure spec language | [YES / NO] | [YES / NO] |

REAL-REQUIRED rule (embedded here, applied during PHASE 2):
  prove and listen are EVIDENCE-HEAVY. A synthetic artifact cannot substitute for real
  signal in EVIDENCE-HEAVY namespaces. prove-* requires actual experiment data or
  prototype outputs. listen-* requires real user interviews or adoption measurements.
  DO NOT assign any flag other than REAL-REQUIRED to EVIDENCE-HEAVY namespaces.

**Do not begin PHASE 2 until every cell in the Classification Table is filled and all nine
namespaces have an assigned category, vocabulary rules, Tier 2/3 Critical value, and
Compliance-Tagged value.**

---

### PHASE 2 — GENERATE

For each namespace, fill the section below. Apply the MUST use and DO NOT use rules from
the PHASE 1 table row. Every artifact body must comply with both vocabulary rules.

#### scout — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — apply MUST use / DO NOT use from scout table row]

---

#### draft — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — apply MUST use / DO NOT use from draft table row]

---

#### review — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — apply MUST use / DO NOT use from review table row]

---

#### flow — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: HIGH-STRUCTURE
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — HIGH-STRUCTURE: state transitions, trigger conditions, data flows;
DO NOT use interview language or adoption percentages]

---

#### trace — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: HIGH-STRUCTURE
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — HIGH-STRUCTURE: interfaces, contracts, component boundaries;
DO NOT use interview language or study framing]

---

#### prove — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: EVIDENCE-HEAVY
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — EVIDENCE-HEAVY: study/data/interview language only;
DO NOT use spec language, contract structures, or schema definitions]

REAL-REQUIRED — EVIDENCE-HEAVY: A synthetic artifact cannot substitute for real signal.
prove-* requires actual experiment data or prototype outputs.

---

#### listen — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: EVIDENCE-HEAVY
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — EVIDENCE-HEAVY: adoption rates, interview quotes, survey data framing;
DO NOT use spec language or state machine language]

REAL-REQUIRED — EVIDENCE-HEAVY: A synthetic artifact cannot substitute for real signal.
listen-* requires real user interviews or adoption measurements.

---

#### program — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: [from table]
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — apply MUST use / DO NOT use from program table row]

---

#### topic — [skill-name]

**MOCK ARTIFACT**
Skill:    [skill-name]
Topic:    [topic]
Category: MIXED
Date:     [date]
Status:   MOCK (awaiting review)

[artifact body — MIXED: signal synthesis narrative plus structured coverage reference;
MUST include at least one structural element and one qualitative observation;
DO NOT use pure spec language]

---

**Do not begin PHASE 3 until all nine namespace sections are filled with complete
MOCK ARTIFACT header blocks and vocabulary-compliant artifact bodies.**

---

### PHASE 3 — SUMMARIZE

## Coverage Summary

| Namespace | Category | Flag | Recommended Next Step |
|-----------|----------|------|-----------------------|
| scout     | [category] | [flag or blank]                                  | [/skill [topic]] |
| draft     | [category] | [flag or blank]                                  | [/skill [topic]] |
| review    | [category] | [flag or blank]                                  | [/skill [topic]] |
| flow      | HIGH-STRUCTURE | [flag or blank]                             | [/skill [topic]] |
| trace     | HIGH-STRUCTURE | [TIER-CRITICAL if tier >= 2 / blank]        | [/skill [topic]] |
| prove     | EVIDENCE-HEAVY | REAL-REQUIRED                               | [/skill [topic]] |
| listen    | EVIDENCE-HEAVY | [REAL-REQUIRED + TIER-CRITICAL / REAL-REQUIRED] | [/skill [topic]] |
| program   | [category] | [flag or blank]                                  | [/skill [topic]] |
| topic     | MIXED      | [flag or blank]                                  | [/skill [topic]] |

Flag rules:
  REAL-REQUIRED — all EVIDENCE-HEAVY, all tiers (pre-flagged in PHASE 1 table)
  TIER-CRITICAL — trace-*, scout-feasibility, listen-* at tier >= 2
  COMPLIANCE    — scout-compliance, trace-permissions when compliance context active
  Multiple flags: REAL-REQUIRED + TIER-CRITICAL

Recommended Next Step: exact skill call — `/skill:subskill [topic]`
DO NOT write "run the real skill." DO NOT write generic advice.

**Do not begin PHASE 4 until the coverage summary table is complete and all nine
namespaces appear with correct flags and recommended next steps.**

---

### PHASE 4 — HANDOFF

This section contains the handoff instruction only. Do not add artifact bodies, table
rows, or other content here.

---

## HANDOFF

Artifact written: simulations/mock/[topic]-mock-[date].md
Next: /mock:review [topic] simulations/mock/[topic]-mock-[date].md

Replace [topic] and [date] with actual values.
Do not write "[topic]", "[date]", or the placeholder string "{this-file}" in the output.
The path after /mock:review must be a fully resolved file path, not a template placeholder.

---

## Variation Map Summary

| V | Axes | What Changed | Target Criteria | Hypothesis |
|---|------|--------------|-----------------|------------|
| V-01 | lifecycle-emphasis | Four named phases each with explicit "Do not begin X until Y is complete" stop-gate sentence at every boundary | C-14, C-11 (side effect) | Stop-gate sentence at each boundary is the minimum surface-level instruction C-14 requires; phase names alone do not qualify; CLASSIFY gate fires before first artifact body as a procedural C-11 guarantee |
| V-02 | output-format | Pre-printed classification table skeleton with namespaces pre-listed + pre-printed HANDOFF block with anti-placeholder instruction | C-11, C-12 | Pre-printed table forces model to fill fields before writing artifact sections; structural guarantee stronger than instruction-based ordering; HANDOFF block cannot be dropped because it is already on the page |
| V-03 | phrasing-register | Per-category MUST use / DO NOT use vocabulary rules; REAL-REQUIRED rationale embedded in the rule at point of invocation, not as post-hoc annotation | C-15, C-13 | Category-specific vocabulary mandates make register mismatch a visible self-checkable violation; rationale at rule invocation point is harder to omit than annotation-based placement |
| V-04 | lifecycle-emphasis + output-format | Pre-printed classification table as Phase 1 output + explicit stop-gate at each phase boundary referencing the pre-printed table | C-14, C-11, C-12 | C-11 doubly guaranteed: structurally (pre-printed table precedes all artifact sections) and procedurally (stop-gate requires table completion before PHASE 2 begins) |
| V-05 | lifecycle-emphasis + output-format + phrasing-register | Full ceiling: pre-printed table with embedded vocabulary rule columns (C-15) and REAL-REQUIRED rationale rows (C-13) + stop-gates at all four boundaries (C-14) + pre-printed HANDOFF block (C-12) | C-14, C-11, C-12, C-13, C-15 | All five aspirational criteria simultaneously targeted; risk is artifact body depth (C-07) degrading under skeleton length pressure — if C-07 degrades, skeleton length vs. generation quality is the Round 4 discriminator |

**Top combination candidate for Round 4:**
V-05 achieves the widest criterion coverage and is the predicted ceiling. The open question
from V-03 (phrasing-register single-axis) is whether vocabulary DO NOT rules alone, without
skeleton structure, can hold C-15 in live model runs. If V-05 passes C-15 and V-03 does
not, the finding is that vocabulary mandates require structural anchoring to enforce (table
columns > instruction blocks). If both pass C-15, vocabulary DO NOT rules are independently
sufficient and skeleton adds no C-15 value — making Round 4 focus on C-07 depth vs.
skeleton length as the new discriminator.

Next: /mock:review mock-all simulations/quest/golden/mock-all-variate-R3-2026-03-15.md
