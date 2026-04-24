---
skill: quest-variate
skill_target: mock-ns
round: 4
rubric_version: 4
date: 2026-03-16
---

# mock-ns -- Round 4 Variations

Rubric: v4 (C-01 through C-16, 5 essential / 3 recommended / 8 aspirational).

New criteria in v4 (extracted from R3 differential analysis):
- **C-15** -- Per-field resolution guidance: beyond naming the three emit fields (C-13),
  the spec tells the executor what to do with each resolved value downstream. V-02 R3
  passed because resolution bullets reinforced downstream action per field (notably:
  tier carries into S-3 for flag computation; compliance tags are emit-only). V-03 R3
  failed despite having the same C-13 bullets -- the bullets described how to fill the
  emit template but not what the resolved values drive in later steps.
- **C-16** -- Exhaustive three-op enumeration: the blocking constraint names all three
  primary operations (skill selection, category lookup, and flag computation). V-03 R3
  passed ("skill selection, category lookup, and flag computation are all blocked").
  V-02 R3 failed ("skill selection or category lookup" -- only two ops, flag computation
  left unguarded).

R3 reference scores under v4:
- V-03 (passive blocked-until, 3 ops): C-15 FAIL, C-16 PASS -- 7/8 aspirational = 98.75
- V-02 (CONSTRAINT 2 ops, downstream-action bullets): C-15 PASS, C-16 FAIL -- 7/8 = 98.75
- V-01 (annotated template, no downstream actions): C-15 FAIL, C-16 FAIL -- 4.5/8 = 95.6

R4 target: combine V-02's per-field downstream-action bullets (C-15) with V-03's
three-op exhaustive enumeration (C-16) in a single prompt. Three single-axis tests
isolate the two axes and a third alternative C-15 form (tabular resolution); then
two-axis combination; then convergent with full belt-and-suspenders.

Three axes selected for single-axis isolation:

1. **Lifecycle emphasis (C-15: downstream-action bullets, 2-op CONSTRAINT)**
   Per-field resolution bullets that name downstream actions (existence drives default
   behavior; tier carries to S-3 for flag; compliance tags are emit-only). CONSTRAINT
   names only 2 ops to isolate C-15 while deliberately failing C-16.

2. **Phrasing register (C-16: three-op CONSTRAINT, standard bullets)**
   CONSTRAINT names all three primary ops ("skill selection, category lookup, or flag
   computation") in active imperative form. Resolution bullets use the standard form
   (no downstream-action reinforcement) to isolate C-16.

3. **Output format (C-15 alternative: tabular resolution, C-16 also present)**
   Per-field resolution guidance expressed as a three-column table (Field | Resolved
   value | Downstream use) rather than bullet list. Uses 3-op passive blocked-until
   for C-16. Tests whether tabular format satisfies C-15 as an alternative to bullets.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (C-15: downstream-action bullets, 2-op CONSTRAINT) | Per-field bullets stating downstream actions (tier -> S-3, tags -> emit-only) satisfy C-15. 2-op CONSTRAINT deliberately fails C-16 for clean isolation. Predicts C-15 PASS, C-16 FAIL. |
| V-02 | Phrasing register (C-16: three-op CONSTRAINT, standard bullets) | CONSTRAINT naming "skill selection, category lookup, or flag computation" satisfies C-16 exhaustive enumeration in active imperative form. Standard resolution bullets (no downstream-action reinforcement) may or may not pass C-15 -- isolates C-16. Predicts C-15 uncertain, C-16 PASS. |
| V-03 | Output format (C-15 tabular resolution, C-16 via passive blocked-until) | Per-field resolution expressed as a 3-column table (Field / Resolved value / Downstream use) satisfies C-15 via a third form -- neither bullet list nor inline annotation. Passive blocked-until carries C-16 (3 ops). If C-15 passes tabular, the mechanism is downstream-use column presence, not bullet phrasing. |
| V-04 | Lifecycle emphasis + phrasing register (C-15 + C-16 combined, the v4 target) | Combining V-01's per-field downstream-action bullets (C-15) with V-02's three-op CONSTRAINT enumeration (C-16) satisfies both simultaneously. This is the prompt structure the v4 rubric designated as V-next. Predicts all 16 criteria pass. |
| V-05 | Convergent (all axes at maximum strength) | Belt-and-suspenders: annotated template + C-13 enumeration sentence + per-field downstream-action bullets (C-15) + 4-op CONSTRAINT (C-16 plus body generation) + table-centric lookups for S-1/S-2 + flag computation table with tier-conditional rows. Combines every confirmed excellence signal from R1 through R4. Predicts all 16 criteria reliably pass. |

---

## V-01 -- Lifecycle Emphasis: C-15 via Downstream-Action Bullets (2-Op CONSTRAINT)

**Axis**: Lifecycle emphasis -- per-field resolution bullets that name what each
resolved value drives in downstream steps. CONSTRAINT names only 2 ops (skill
selection and category lookup) to deliberately fail C-16 and cleanly isolate C-15.
**Hypothesis**: When each emit field has a dedicated action bullet -- existence drives
default-assignment behavior; tier is explicitly carried into S-3 for flag computation;
compliance tags are emit-only with no flag effect -- the prompt satisfies C-15. The
2-op CONSTRAINT isolates this from C-16 so the two criteria can be scored independently.
**Predicts**: C-01--C-14 pass | C-15 PASS | C-16 FAIL.
**Expected composite**: ~98.75 (7/8 aspirational -- same band as R3 V-02 under v4).

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection or category lookup until after
the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign the category for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill appears in no group, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Base flag by category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement (HIGH-STRUCTURE, critical skills only):
  Critical skills: trace-request, trace-component, trace-contract, trace-state,
    trace-skill, trace-migration, trace-deployment, scout-feasibility,
    listen-support, listen-feedback, listen-adoption
  Condition: category = HIGH-STRUCTURE AND skill is critical AND tier >= 2
  Refined flag: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

EVIDENCE-HEAVY and MIXED flags are unaffected by tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write the artifact in this exact sequence:

1. MOCK ARTIFACT header block (first, before any other content):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id}
   Topic: {topic}
   Category: {category from S-2}
   Date: {date}
   Status: MOCK (awaiting review)
   Flag: {flag from S-3}

2. Fidelity warning (immediately after header, no content between):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
     mechanisms are reliable. Content is synthetically generated but structurally
     representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
     Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
     correct but evidentially fabricated. Do not use this output to draw conclusions
     about {topic}. The sections are right; the contents are invented. A real
     {skill-id} run is required before any evidence-based decision can be made.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
     mechanisms) are reliable. Specific claims may be partially accurate or partially
     fabricated. Review for plausibility before accepting coverage.

3. Mock body (after fidelity warning):

   Follow the golden structure of {skill-id}: correct section headings, required
   tables or lists, gate or verdict line in its expected position, enforcement
   mechanisms present. Use {topic} as subject. The body must be recognizable to
   anyone familiar with the real {skill-id} output, without reading the header.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 -- Phrasing Register: C-16 via Three-Op CONSTRAINT (Standard Resolution Bullets)

**Axis**: Phrasing register -- the CONSTRAINT names all three primary operations in
active imperative form ("skill selection, category lookup, or flag computation").
Resolution bullets use the standard form inherited from R3: field-naming with value
rules, a single carryover instruction, but no per-field downstream-action reinforcement.
**Hypothesis**: Naming all three primary operations in the CONSTRAINT satisfies C-16
in active imperative form. The standard resolution bullets may pass C-15 at some rate
(the rubric noted V-02 R3 passed C-15 despite having similar structure), but this
variation isolates C-16 by ensuring C-15 is not specifically enhanced beyond baseline.
**Predicts**: C-01--C-14 pass | C-15 uncertain (no enhancement) | C-16 PASS.
**Expected composite**: ~98.75 (7/8 aspirational if C-15 follows baseline failure rate).

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, or flag computation
until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Resolution:
  - "found" if the topic appears in TOPICS.md; "not found" if absent
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign the category for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill appears in no group, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Base flag by category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement (HIGH-STRUCTURE, critical skills only):
  Critical skills: trace-request, trace-component, trace-contract, trace-state,
    trace-skill, trace-migration, trace-deployment, scout-feasibility,
    listen-support, listen-feedback, listen-adoption
  Condition: category = HIGH-STRUCTURE AND skill is critical AND tier >= 2
  Refined flag: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

EVIDENCE-HEAVY and MIXED flags are unaffected by tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write the artifact in this exact sequence:

1. MOCK ARTIFACT header block (first, before any other content):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id}
   Topic: {topic}
   Category: {category from S-2}
   Date: {date}
   Status: MOCK (awaiting review)
   Flag: {flag from S-3}

2. Fidelity warning (immediately after header, no content between):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
     mechanisms are reliable. Content is synthetically generated but structurally
     representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
     Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
     correct but evidentially fabricated. Do not use this output to draw conclusions
     about {topic}. The sections are right; the contents are invented. A real
     {skill-id} run is required before any evidence-based decision can be made.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
     mechanisms) are reliable. Specific claims may be partially accurate or partially
     fabricated. Review for plausibility before accepting coverage.

3. Mock body (after fidelity warning):

   Follow the golden structure of {skill-id}: correct section headings, required
   tables or lists, gate or verdict line in its expected position, enforcement
   mechanisms present. Use {topic} as subject. The body must be recognizable to
   anyone familiar with the real {skill-id} output, without reading the header.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 -- Output Format: C-15 via Tabular Resolution (Passive Blocked-Until for C-16)

**Axis**: Output format -- per-field resolution guidance expressed as a three-column
lookup table (Field | Resolved value | Downstream use) rather than a bullet list.
Uses passive blocked-until framing for C-16 (three ops: skill selection, category
lookup, flag computation). Isolates the C-15 format question.
**Hypothesis**: A table with an explicit "Downstream use" column makes per-field
resolution guidance unambiguous and auditable -- each row directly names what the
executor should do with the resolved value (existence -> drives default behavior;
tier -> carries into S-3 for flag; compliance tags -> emit only). If C-15 passes
with tabular format, the mechanism is the downstream-use specification itself,
independent of whether it is expressed as bullets or table rows.
**Predicts**: C-01--C-14 pass | C-15 PASS (tabular downstream-use column) | C-16 PASS.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

Skill selection, category lookup, and flag computation are all blocked until
the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                        |
  |-----------------|----------------------------------------------------------|---------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none     |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Carry into S-3 for flag computation   |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag          |

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign the category for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill appears in no group, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Base flag by category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement (HIGH-STRUCTURE, critical skills only):
  Critical skills: trace-request, trace-component, trace-contract, trace-state,
    trace-skill, trace-migration, trace-deployment, scout-feasibility,
    listen-support, listen-feedback, listen-adoption
  Condition: category = HIGH-STRUCTURE AND skill is critical AND tier >= 2
  Refined flag: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

EVIDENCE-HEAVY and MIXED flags are unaffected by tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write the artifact in this exact sequence:

1. MOCK ARTIFACT header block (first, before any other content):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id}
   Topic: {topic}
   Category: {category from S-2}
   Date: {date}
   Status: MOCK (awaiting review)
   Flag: {flag from S-3}

2. Fidelity warning (immediately after header, no content between):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
     mechanisms are reliable. Content is synthetically generated but structurally
     representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
     Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
     correct but evidentially fabricated. Do not use this output to draw conclusions
     about {topic}. The sections are right; the contents are invented. A real
     {skill-id} run is required before any evidence-based decision can be made.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
     mechanisms) are reliable. Specific claims may be partially accurate or partially
     fabricated. Review for plausibility before accepting coverage.

3. Mock body (after fidelity warning):

   Follow the golden structure of {skill-id}: correct section headings, required
   tables or lists, gate or verdict line in its expected position, enforcement
   mechanisms present. Use {topic} as subject. The body must be recognizable to
   anyone familiar with the real {skill-id} output, without reading the header.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-04 -- Lifecycle Emphasis + Phrasing Register: C-15 + C-16 Combined (The V4 Target)

**Axis**: Two-axis combination: (1) per-field downstream-action bullets from V-01
(C-15) and (2) three-op CONSTRAINT enumeration from V-02 (C-16).
**Hypothesis**: The v4 rubric identifies V-02 R3 as the C-15 carrier and V-03 R3 as
the C-16 carrier -- each holding one excellence signal the other lacks. Combining
V-01's per-field downstream-action bullets (existence drives default-assignment; tier
carries into S-3; compliance tags are emit-only) with V-02's CONSTRAINT naming all
three primary ops (skill selection, category lookup, flag computation) satisfies both
C-15 and C-16 simultaneously. This is the prompt the v4 rubric designated as V-next.
**Predicts**: C-01--C-16 all pass.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, or flag computation
until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign the category for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill appears in no group, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Base flag by category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement (HIGH-STRUCTURE, critical skills only):
  Critical skills: trace-request, trace-component, trace-contract, trace-state,
    trace-skill, trace-migration, trace-deployment, scout-feasibility,
    listen-support, listen-feedback, listen-adoption
  Condition: category = HIGH-STRUCTURE AND skill is critical AND tier >= 2
  Refined flag: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

EVIDENCE-HEAVY and MIXED flags are unaffected by tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write the artifact in this exact sequence:

1. MOCK ARTIFACT header block (first, before any other content):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id}
   Topic: {topic}
   Category: {category from S-2}
   Date: {date}
   Status: MOCK (awaiting review)
   Flag: {flag from S-3}

2. Fidelity warning (immediately after header, no content between):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
     mechanisms are reliable. Content is synthetically generated but structurally
     representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
     Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
     correct but evidentially fabricated. Do not use this output to draw conclusions
     about {topic}. The sections are right; the contents are invented. A real
     {skill-id} run is required before any evidence-based decision can be made.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
     mechanisms) are reliable. Specific claims may be partially accurate or partially
     fabricated. Review for plausibility before accepting coverage.

3. Mock body (after fidelity warning):

   Follow the golden structure of {skill-id}: correct section headings, required
   tables or lists, gate or verdict line in its expected position, enforcement
   mechanisms present. Use {topic} as subject. The body must be recognizable to
   anyone familiar with the real {skill-id} output, without reading the header.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 -- Convergent (All Excellence Signals at Maximum Strength)

**Axis**: All confirmed excellence signals from R1 through R4 combined at maximum
strength: annotated template (C-13 inline) + explicit C-13 enumeration sentence +
per-field downstream-action bullets (C-15) + 4-op CONSTRAINT (C-16 plus body
generation as fourth guarded op) + table-centric lookups for S-1 and S-2 + full
flag computation table with tier-conditional rows (C-09).
**Hypothesis**: Each signal reinforces the others without conflict. The annotated
template plus enumeration sentence is belt-and-suspenders for C-13; the downstream-
action bullets reinforce C-15 with explicit per-field guidance; the 4-op CONSTRAINT
exhaustively guards all three primary operations plus body generation for C-16 and
C-14; table lookups minimize category-mismatch risk for C-02/C-06; the flag table
makes tier-conditional computation unambiguous for C-09. No prior convergent has
combined all 16 signals; this is the first prompt with C-15+C-16 alongside the
full R1/R2/R3 heritage.
**Predicts**: C-01--C-16 all reliably pass.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
body generation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present -- existence (found/not found), tier classification,
and compliance tags. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute Flag from this table:

  | Category       | Tier | Skill condition  | Flag value                                                      |
  |----------------|------|------------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | non-critical     | none (structural coverage reliable)                             |
  | HIGH-STRUCTURE | 1    | critical         | none (structural coverage reliable)                             |
  | HIGH-STRUCTURE | 2+   | critical         | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | EVIDENCE-HEAVY | any  | any              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | MIXED          | any  | any              | REVIEW-FOR-PLAUSIBILITY                                         |

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

---- HEADER BLOCK (required; must be first content in the file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header, no content between) ----

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility,
    listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated.
    Review for plausibility before accepting coverage.

---- MOCK BODY (required; after fidelity warning) ----

  Generate mock content following the exact golden structural pattern of {skill-id}:
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP S-5 -- FINALIZE

After writing the artifact, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```
