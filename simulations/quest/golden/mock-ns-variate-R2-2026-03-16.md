---
skill: quest-variate
skill_target: mock-ns
round: 2
rubric_version: 2
date: 2026-03-16
---

# mock-ns -- Round 2 Variations

Rubric: v2 (C-01 through C-12, 5 essential / 3 recommended / 4 aspirational).

New criteria in v2 (extracted from R1 excellence evidence in V-03 and V-04):
- **C-11** -- TOPICS.md emit is the first observable output line, preceding all
  computation (skill selection, category resolution, flag derivation). A prompt
  specifying "before doing anything else / before any other computation" consistently
  produces this ordering. C-10 requires the emit exists; C-11 requires it appears first.
- **C-12** -- Emit uses the exact three-field format:
  `> TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}`
  All three fields must be present. Single-field emits fail this criterion.

R1 V-03 and V-04 both achieved C-11 and C-12 (100/100). R1 V-01 and V-02 had no
TOPICS.md setup at all and failed C-10/C-11/C-12. R2 isolates: (a) whether the
ordering constraint can be weakened (step label without prohibition) while still
producing C-11; (b) whether format can be expressed as example-then-instruction
rather than copy-exact and still pass C-12; (c) whether explicit prohibition outperforms
positive ordering for C-11; (d) whether conversational register maintains C-11/C-12
when step-zero is explicitly anchored. Then convergent.

Three axes selected for single-axis isolation:

1. **Lifecycle emphasis (ordering constraint strength)** -- labeled step-zero without
   explicit prohibition language. Tests whether positional numbering alone produces C-11,
   or whether "before any computation" text is the load-bearing signal.
2. **Output format (emit format precision)** -- verbatim copy instruction vs. template.
   Tests whether "copy this exact line" outperforms placeholder-template for C-12.
3. **Phrasing register (prohibition framing)** -- negative constraint ("do not compute
   X before emitting Y") vs. positive ordering ("emit Y, then proceed to X"). Tests
   whether prohibition framing is the dominant signal for C-11.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (step-zero label, no prohibition) | Labeling TOPICS.md as "STEP S-0" before S-1, with a bracketed note "(run before any other step)", is sufficient to produce C-11 without requiring explicit "before any computation" prohibition text. C-12 is seeded by including the three-field template. Predicts C-11 probable, C-12 probable, C-09 probable. |
| V-02 | Output format (verbatim copy instruction for emit format) | Expressing the emit as a "copy this exact line verbatim" instruction (not a template) is the minimum signal for C-12. The verbatim instruction removes placeholder ambiguity and forces all three fields. Also carries a step-zero label for C-11. Predicts C-11 C-12 C-09 C-10 all pass. |
| V-03 | Phrasing register (explicit prohibition framing) | An explicit negative constraint -- "Do not perform skill selection, category lookup, or flag computation until after the TOPICS.md emit line is written" -- is the strongest signal for C-11, stronger than a positive ordering instruction. Tests whether prohibition is required or merely sufficient. Predicts C-11 C-12 C-09 C-10 all pass. |
| V-04 | Lifecycle emphasis + phrasing register (conversational + step-zero, two-axis) | A conversational, imperative-light register can still produce C-11 and C-12 when "the very first thing you do" framing is used and the emit format is shown as a complete example line. Two-axis test -- if scores match V-03, formal step machinery is not required for C-11/C-12. |
| V-05 | Convergent (all axes combined) | Table-centric lookups (category registry + default-skill table) + step-zero label + explicit prohibition + verbatim copy instruction for emit format + tier-conditional flag for C-09 + fidelity warnings for C-07 + next-step line for C-08. Predicts all 12 criteria pass (100/100). |

---

## V-01 -- Lifecycle Emphasis (Step-Zero Label, No Prohibition)

**Axis**: Lifecycle emphasis -- TOPICS.md is labeled "STEP S-0" and bracketed as "(run
before any other step)" without any explicit prohibition against computing before it.
**Hypothesis**: Positional step numbering (S-0 appearing before S-1) combined with a
parenthetical reminder is sufficient to produce C-11. Explicit prohibition language
("do not compute X before Y") is stronger but may not be necessary when the step
sequencing is unambiguous. C-12 is seeded via the three-field template in S-0's emit
instruction. C-09 is seeded via tier-conditional flag refinement in S-3.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 (probable)
C-12 (probable).
**Expected composite**: ~97.5--100 (C-11 uncertain without prohibition; C-12 probable
with template).

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

STEP S-0 -- READ TOPICS.md   (run before any other step)

Read TOPICS.md and emit a dedicated status line for this topic:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

If the topic is registered, read its tier and compliance tags from the file.
If not registered, default tier to 1 and compliance tags to none.
If --tier was provided on the command line, it overrides the TOPICS.md tier.
Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise use the representative default for the namespace:

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

Assign the category for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill is not in any group, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Base flag by category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement for HIGH-STRUCTURE critical namespaces only:
  If category is HIGH-STRUCTURE AND skill is one of:
    trace-request, trace-component, trace-contract, trace-state, trace-skill,
    trace-migration, trace-deployment, scout-feasibility, listen-support,
    listen-feedback, listen-adoption
  AND tier >= 2:
    Override flag to: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

EVIDENCE-HEAVY and MIXED flags are not modified by tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write the artifact in this exact structure:

1. MOCK ARTIFACT header block (must appear first, before any body content):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id}
   Topic: {topic}
   Category: {category from S-2}
   Date: {date}
   Status: MOCK (awaiting review)
   Flag: {flag from S-3}

2. Fidelity warning (immediately after header block):

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

   Follow the exact golden structure of {skill-id}: correct section headings,
   required tables or lists, gate or verdict line in the expected position,
   enforcement mechanisms present. Use {topic} as the subject throughout.
   A reader familiar with {skill-id} must be able to identify the skill from the
   body alone without reading the header.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 -- Output Format (Verbatim Copy Instruction for Emit Format)

**Axis**: Output format -- the TOPICS.md emit format is expressed as a verbatim
copy instruction ("emit this exact text") rather than a template with placeholders.
**Hypothesis**: A "copy this exact line" instruction removes placeholder-substitution
ambiguity and forces the executor to produce all three fields (found/not found, tier,
compliance tags), because the example line itself contains all three. Template
instructions leave open whether the LLM will collapse the format to a single field
if it infers the other two are "obvious." C-12 tests for all three fields; verbatim
instruction is the minimal change that reliably prevents single-field collapse.
Step-zero is established via "before doing anything else" text for C-11.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12.
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

Before doing anything else, read TOPICS.md. Then emit this exact text (fill in values,
keep all three fields -- do not omit tier or compliance tags even if they are default):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields are required in this emit line:
  - "found" if the topic appears in TOPICS.md; "not found" if absent
  - tier: the value from TOPICS.md, or 1 if not registered, or the --tier override
  - compliance tags: the tag list from TOPICS.md, or "none" if absent or unregistered

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it directly. Otherwise use the representative default:

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

Find the selected skill in exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill is not listed, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Base flag from category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement (HIGH-STRUCTURE critical skills only):
  Critical skills: trace-request, trace-component, trace-contract, trace-state,
    trace-skill, trace-migration, trace-deployment, scout-feasibility,
    listen-support, listen-feedback, listen-adoption
  If category is HIGH-STRUCTURE AND skill is critical AND tier >= 2:
    Override flag to: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open with the MOCK ARTIFACT header block. All six fields required, in this order:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

Immediately after the header, write the category-appropriate fidelity warning:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

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

After the fidelity warning, generate the mock body following the exact golden
structure of {skill-id}: correct section headings, required tables or lists, gate
or verdict line in its expected position, enforcement mechanisms in place.
Use {topic} as the subject. A reader familiar with {skill-id} must recognize the
body structure without reading the header.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 -- Phrasing Register (Explicit Prohibition Framing)

**Axis**: Phrasing register -- the TOPICS.md step carries an explicit negative constraint:
the executor is told not to perform any other computation until after the emit line is
written. Prohibition framing rather than positive ordering.
**Hypothesis**: Positive instructions ("emit first, then proceed") leave open the
possibility that the executor interleaves the TOPICS.md read with other setup steps.
A negative constraint ("do not select a skill, do not assign a category, do not compute
a flag until the TOPICS.md line is written") closes that interpretation explicitly.
This is the strongest formulation for C-11. If V-01 (label-only) fails C-11 and V-03
passes, prohibition is the load-bearing signal. If both pass, prohibition is sufficient
but not necessary.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12.
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

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
any other step until after you have emitted the TOPICS.md status line below.

Read TOPICS.md. Emit:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Resolution rules:
  - "found": topic appears in TOPICS.md. Read its tier and compliance tags.
  - "not found": topic absent. Default tier = 1, compliance tags = none.
  - --tier override: if provided, replaces the TOPICS.md tier value.

All three fields (existence, tier, compliance tags) must appear in the emit line.
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

## V-04 -- Lifecycle Emphasis + Phrasing Register (Conversational + Step-Zero, Two-Axis)

**Axis**: Conversational register (imperative-light, descriptive flow) combined with
a "the very first thing" framing for TOPICS.md. Two-axis test against V-03 (prohibition,
formal) and V-01 (step-zero label, formal).
**Hypothesis**: A conversational register can reliably produce C-11 when the first-step
framing is explicit ("the very first thing you do") and the emit format is shown as a
complete example line in the text. Friendly phrasing does not trade off against C-11
or C-12 -- what matters is the ordering anchor, not the register. If this matches V-03
scores, formal prohibition machinery is unnecessary for C-11 compliance.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Your job is simple: produce one mock artifact for a single namespace in one pass.
No prompts, no questions, no back-and-forth. Read the inputs, do the work, write
the artifact, and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}   (optional -- if missing, you pick the representative skill)
  --tier     1 | 2 | 3    (optional -- default: read from TOPICS.md, else 1)

---

The very first thing you do -- before selecting a skill, before assigning a category,
before computing anything -- is read TOPICS.md and emit one line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

If the topic is in TOPICS.md, read its tier and compliance tags from there.
If it is not registered, use tier 1 and no compliance tags.
If the user passed --tier, that value wins.

Keep all three fields in the emit -- existence, tier, and compliance tags.
Then proceed.

---

Decide which skill to mock:

- If --skill was given, use it.
- Otherwise use the default for the namespace:
    scout -> scout-feasibility
    draft -> draft-spec
    review -> review-design
    flow -> flow-resilience
    trace -> trace-request
    prove -> prove-hypothesis
    listen -> listen-support
    program -> program-plan
    topic -> topic-plan   (never topic-status)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

Assign the category. Every skill falls into exactly one of these three groups:

  HIGH-STRUCTURE -- structure is the substance; mock fidelity is high:
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY -- value is in the evidence; structure is right but content is fabricated:
    prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED -- partly structural, partly evidential:
    scout-competitors, prove-hypothesis, review-customers, review-users

---

Compute the flag from the category and the tier you resolved above:

  HIGH-STRUCTURE (non-critical): "none (structural coverage reliable)"
  HIGH-STRUCTURE (critical skill, tier 1): "none (structural coverage reliable)"
  HIGH-STRUCTURE (critical skill, tier >= 2): "none (structural coverage reliable;
    REAL-REQUIRED at Tier 2+)"
  EVIDENCE-HEAVY: "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"
  MIXED: "REVIEW-FOR-PLAUSIBILITY"

Critical skills for the tier check:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

---

Write the artifact to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open with the MOCK ARTIFACT header block -- all six fields, in this order:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {value computed above}

Right after the header, put the fidelity warning:

  HIGH-STRUCTURE: "NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement
  mechanisms are reliable. Content is synthetically generated but structurally
  representative. Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical
  namespaces (trace, scout-feasibility, listen)."

  EVIDENCE-HEAVY: "WARNING: This is an EVIDENCE-HEAVY mock. The content below is
  structurally correct but evidentially fabricated. Do not use this output to draw
  conclusions about {topic}. A real {skill-id} run is required before any
  evidence-based decision."

  MIXED: "CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific
  claims may be partially fabricated. Review for plausibility."

After that, write the mock body. Match the golden structure of {skill-id} exactly:
right section headings, required tables or lists, gate or verdict line where expected,
enforcement mechanisms in place. Use {topic} as the subject. Anyone who knows the real
{skill-id} output should recognize the structure from the body alone.

---

When done, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

And make the last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 -- Convergent (All Axes Combined)

**Axis**: Table-centric lookups (V-02 from R1) + step-zero label + explicit prohibition
(V-03) + verbatim copy instruction for emit format (V-02) + tier-conditional flag table
(C-09) + fidelity warnings (C-07) + next-step line (C-08).
**Hypothesis**: Combining the strongest signals from each single-axis variation produces
a prompt where all 12 criteria reliably pass. The prohibition framing ensures C-11;
the verbatim copy instruction and three-field requirement ensures C-12; table-centric
lookups reduce category mismatch risk for C-02/C-06; the flag computation table with
explicit critical-skill enumeration and tier rows ensures C-09; the fidelity warning
block ensures C-07.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12.
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

CONSTRAINT: Do not perform skill selection, category assignment, flag computation,
or any other step until after the TOPICS.md emit line below is written.

Read TOPICS.md. Emit this exact text (all three fields required -- do not omit any):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                              |
  |-----------|-------------------|---------------------------------------------|
  | scout     | scout-feasibility |                                             |
  | draft     | draft-spec        |                                             |
  | review    | review-design     |                                             |
  | flow      | flow-resilience   |                                             |
  | trace     | trace-request     |                                             |
  | prove     | prove-hypothesis  |                                             |
  | listen    | listen-support    |                                             |
  | program   | program-plan      |                                             |
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

  | Category       | Tier | Skill condition  | Flag value                                                       |
  |----------------|------|------------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | non-critical     | none (structural coverage reliable)                              |
  | HIGH-STRUCTURE | 1    | critical         | none (structural coverage reliable)                              |
  | HIGH-STRUCTURE | 2+   | critical         | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)   |
  | EVIDENCE-HEAVY | any  | any              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)     |
  | MIXED          | any  | any              | REVIEW-FOR-PLAUSIBILITY                                          |

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
