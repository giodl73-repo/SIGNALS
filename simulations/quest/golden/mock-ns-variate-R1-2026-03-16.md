---
skill: quest-variate
skill_target: mock-ns
round: 1
rubric_version: 1
date: 2026-03-16
---

# mock-ns -- Round 1 Variations

Rubric: v1 (C-01 through C-10, 5 essential / 3 recommended / 2 aspirational).

This is the first variate round. Rubric is new; no prior run history. Single-axis
variation first (V-01 through V-03), then a two-axis combination (V-04), then
full convergence (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (conversational, descriptive) | A readable, conversational register with labeled phases hits all essential + recommended criteria without requiring heavy structural machinery. The rubric at v1 does not penalize register; C-09/C-10 may not pass due to lighter tier/TOPICS instructions. |
| V-02 | Output format (table-centric lookups) | Embedding the category registry and default skill table as explicit lookup tables (not prose lists) reduces mismatch on C-02 (category correctness) and C-06 (default skill selection). |
| V-03 | Lifecycle emphasis (setup-first, TOPICS.md as anchor) | Making TOPICS.md consultation a named, emit-bearing first step (before skill selection) surfaces C-10 and wires tier into the flag computation path for C-09. |
| V-04 | Phrasing register + lifecycle emphasis (conversational register + TOPICS.md anchor) | Combining the readability of V-01 with the explicit TOPICS.md setup of V-03 allows C-10 to pass while keeping the prompt approachable. Two-axis test. |
| V-05 | Convergent (all axes) | Table-centric lookups (V-02) + TOPICS.md-first setup (V-03) + tier-conditional flag refinement (C-09) + explicit fidelity warnings (C-07) + correct path + next-step line. Predicts all 10 criteria passing. |

---

## V-01 -- Phrasing Register (Conversational)

**Axis**: Phrasing register -- conversational, descriptive, imperative-light.
**Hypothesis**: A readable register with clear section headers and prose instructions
produces correct essential outputs (header block, category, body structure, flag, path)
and recommended outputs (default skill, fidelity warning, next-step line). C-09 and C-10
may miss due to lighter tier-conditional and TOPICS.md instruction weight.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | (C-09 uncertain) (C-10 miss).
**Expected composite**: ~86 (5/5 essential, 3/3 recommended, 0-1/2 aspirational).

---

```
You are running /mock:ns for Signal.

This skill generates a mock artifact for a single namespace. It is single-pass --
no confirmation prompts, no iterative refinement. You receive a topic and a namespace,
produce the mock artifact, and write it to disk.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional, default: 1)

---

Phase 1 -- Pick the skill

If --skill was provided, use it. Otherwise use the representative skill for the namespace:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan  (never topic-status -- that is meta-structural and excluded)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic})...

---

Phase 2 -- Assign the category

Every skill belongs to exactly one of three categories. Look up the selected skill:

  HIGH-STRUCTURE
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY
    prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED
    scout-competitors, prove-hypothesis, review-customers, review-users

If the skill is not in this list, emit an error and stop.

---

Phase 3 -- Write the artifact

The artifact goes to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open the artifact with the MOCK ARTIFACT header block. All six fields are required,
in this order:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {see below}

Choose the Flag value based on the category:

  HIGH-STRUCTURE  ->  Flag: none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  Flag: REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  Flag: REVIEW-FOR-PLAUSIBILITY

After the header, add the category-appropriate fidelity warning before the body content:

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

After the fidelity warning, generate the mock body. The body must follow the exact
structural pattern of the selected skill -- correct section headings, required tables
or lists, gate or verdict line where the skill produces one, enforcement mechanisms
in the expected positions. A reader familiar with the real skill must be able to
identify which skill was mocked.

Use {topic} as the subject throughout the body content.

---

Phase 4 -- Finalize

After writing the artifact body, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

End with this exact line (replace placeholders):
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 -- Output Format (Table-Centric Lookups)

**Axis**: Output format -- all lookup logic expressed as explicit tables, not prose.
**Hypothesis**: Table-structured category registry and default-skill table make C-02
(category correctness) and C-06 (default skill selection) less error-prone. The LLM
matches rows rather than scanning prose. C-05 (path) and C-01 (header) are templated
explicitly. C-07 (fidelity warning) and C-08 (next-step) are deferred to a final step.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | (C-09/C-10 miss -- no
tier-conditional or TOPICS emit instructions).
**Expected composite**: ~86 (5/5 essential, 3/3 recommended, 0/2 aspirational).

---

```
You are running /mock:ns for Signal. Single-pass. No prompts.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional, default: 1)

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise consult this table:

  | Namespace | Default skill     | Notes                              |
  |-----------|-------------------|------------------------------------|
  | scout     | scout-feasibility |                                    |
  | draft     | draft-spec        |                                    |
  | review    | review-design     |                                    |
  | flow      | flow-resilience   |                                    |
  | trace     | trace-request     |                                    |
  | prove     | prove-hypothesis  |                                    |
  | listen    | listen-support    |                                    |
  | program   | program-plan      |                                    |
  | topic     | topic-plan        | topic-status excluded (meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Skills                                                          |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,      |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,       |
  |                | draft-proposal, draft-pitch, review-design, review-code,        |
  |                | trace-request, trace-component, trace-contract, trace-state,    |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, |
  |                | flow-trigger, flow-integration, program-plan                    |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,               |
  |                | listen-feedback, listen-support, listen-adoption                |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,          |
  |                | review-users                                                    |

The Category value for the MOCK ARTIFACT header is the matched row label.

---

STEP S-3 -- FLAG COMPUTATION

Compute the Flag value from the category:

  | Category       | Flag value                                                  |
  |----------------|-------------------------------------------------------------|
  | HIGH-STRUCTURE | none (structural coverage reliable)                         |
  | EVIDENCE-HEAVY | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)|
  | MIXED          | REVIEW-FOR-PLAUSIBILITY                                     |

---

STEP S-4 -- ARTIFACT CONSTRUCTION

Write the artifact to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Structure:

1. MOCK ARTIFACT header block (required, immediately first):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id}
   Topic: {topic}
   Category: {category from S-2}
   Date: {date}
   Status: MOCK (awaiting review)
   Flag: {flag from S-3}

2. Fidelity warning (required, immediately after header):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
     reliable. Content is synthetically generated but structurally representative.
     Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces.

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
     evidentially fabricated. Do not draw conclusions about {topic} from this output.
     A real {skill-id} run is required before any evidence-based decision.

   MIXED:
     CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims
     may be partially fabricated. Review for plausibility.

3. Mock body (required, after fidelity warning):

   Follow the golden structural pattern of {skill-id} exactly:
   - Use the correct section headings for that skill
   - Include required tables, lists, and gate/verdict lines
   - Place enforcement mechanisms in their expected positions
   - A reader familiar with {skill-id} must recognize the structure
   Content uses {topic} as subject. All values are synthetic but structurally
   representative.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Final line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 -- Lifecycle Emphasis (Setup-First, TOPICS.md as Anchor)

**Axis**: Lifecycle emphasis -- TOPICS.md consultation is the first named step with its
own dedicated emit line; tier is read from TOPICS.md before any other computation.
**Hypothesis**: Making TOPICS.md a first-class setup step with a required emit line
surfaces C-10 (TOPICS.md consultation evidence). Piping the tier from TOPICS.md into
the flag computation path enables C-09 (tier-conditional flag for critical namespaces).
Both aspirational criteria depend on the tier being visible before S-3 runs.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10.
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

Before anything else, read TOPICS.md. Emit a dedicated line on the result:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

If the topic is found, read its tier classification and compliance tags.
If not found, default tier to 1 and compliance tags to none.
If --tier was provided on the command line, it overrides the TOPICS.md tier.

Carry the resolved tier into all downstream steps.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise use the representative skill:

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

---

STEP S-3 -- FLAG COMPUTATION

Base flag by category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement for HIGH-STRUCTURE only:
  If the category is HIGH-STRUCTURE AND the skill is one of:
    trace-request, trace-component, trace-contract, trace-state, trace-skill,
    trace-migration, trace-deployment, scout-feasibility, listen-support,
    listen-feedback, listen-adoption
  AND tier >= 2:
    Override flag to: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)
  If tier == 1 for those same skills, use the standard flag.

EVIDENCE-HEAVY and MIXED flags are not affected by tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open the file with the MOCK ARTIFACT header block. All fields required, in this order:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

Immediately after the header, write the category-appropriate fidelity warning:

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility,
    listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED ->
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data, research
    findings) may be partially accurate or partially fabricated. Review for
    plausibility before accepting coverage.

After the fidelity warning, generate the mock body following the exact golden structure
of {skill-id}: correct section headings, required tables or lists, gate or verdict line
in the expected position, enforcement mechanisms present. Use {topic} as the subject.
A reader familiar with {skill-id} must be able to identify the skill from the body alone.

---

STEP S-5 -- FINALIZE

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-04 -- Phrasing Register + Lifecycle Emphasis (Two-Axis)

**Axis**: Conversational register (V-01) combined with TOPICS.md-first setup (V-03).
**Hypothesis**: A conversational, readable prompt can still surface C-10 (TOPICS.md
emit) and C-09 (tier-conditional flag) if the setup phase is explicitly sequenced before
skill selection and the tier-conditional rule is stated plainly in prose rather than
as a formal override block. Two-axis test -- if this matches V-03 scores, prose
instructions are sufficient for tier-conditional handling.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Your job is to produce one mock artifact for a single namespace. Do it in one pass.
No prompts, no clarification requests. Write the artifact. Emit the next-step line. Done.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}   (optional -- if missing, you'll pick the representative skill)
  --tier     1 | 2 | 3    (optional -- default: read from TOPICS.md, else 1)

---

First, read TOPICS.md. Emit exactly this line before doing anything else:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

If the topic is registered, read its tier and compliance tags. If not, use tier 1 and
no compliance tags. If the user passed --tier, that value wins over TOPICS.md.

---

Next, decide which skill to mock:

- If --skill was given, use it directly.
- If not, use the namespace default:
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

Now assign the category. Every skill belongs to one of these three groups:

  HIGH-STRUCTURE -- the structure is the substance; mock fidelity is high:
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY -- value is in the data collected; structure right but content fabricated:
    prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED -- partly structural, partly evidential:
    scout-competitors, prove-hypothesis, review-customers, review-users

---

Now compute the Flag:

  If HIGH-STRUCTURE:
    Standard flag: "none (structural coverage reliable)"
    But if the skill is from trace-*, scout-feasibility, or listen-* and tier >= 2:
      Use: "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  If EVIDENCE-HEAVY:
    Flag: "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  If MIXED:
    Flag: "REVIEW-FOR-PLAUSIBILITY"

---

Now write the artifact to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open with the MOCK ARTIFACT header block -- all six fields, in this exact order:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {value computed above}

Right after the header, include the fidelity warning for the category:

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

After the fidelity warning, generate the mock body. Follow the exact golden structure
of {skill-id}: right section headings, required tables or lists, gate or verdict line
where expected, enforcement mechanisms in place. Use {topic} as the subject. The body
should be recognizable to anyone familiar with the real {skill-id} output.

---

When done, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

And make the last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 -- Convergent (All Axes)

**Axis**: Table-centric lookups (V-02) + TOPICS.md-first setup (V-03) + explicit
tier-conditional flag refinement + fidelity warnings by category + correct path + next-step.
**Hypothesis**: Combining structured table lookups for category/default-skill (reduces
mismatch risk on C-02/C-06), explicit TOPICS.md setup step with dedicated emit (C-10),
tier-conditional flag logic with named critical skills (C-09), category-exact fidelity
warnings (C-07), correct path template (C-05), and next-step invocation line (C-08)
produces a prompt where all 10 criteria pass.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10.
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

Read TOPICS.md now. Emit a dedicated line:

  > TOPICS.md: {found | not found}, tier: {tier-from-file | 1 (default)},
    compliance tags: {tags | none}

If the topic is registered, extract its tier and compliance tags.
If not registered, use tier=1 and compliance tags=none.
If --tier was given on the command line, it takes precedence over TOPICS.md.
Carry the resolved tier into steps S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it as-is and skip the table below.
Otherwise look up the namespace in this table to find the default skill:

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

  | Category       | Member skills                                                   |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,      |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,       |
  |                | draft-proposal, draft-pitch, review-design, review-code,        |
  |                | trace-request, trace-component, trace-contract, trace-state,    |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, |
  |                | flow-trigger, flow-integration, program-plan                    |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,               |
  |                | listen-feedback, listen-support, listen-adoption                |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,          |
  |                | review-users                                                    |

Record the matched category. If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Compute Flag from category and tier:

  | Category       | Tier | Skill condition                                    | Flag value                                                            |
  |----------------|------|----------------------------------------------------|-----------------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | not a critical skill                               | none (structural coverage reliable)                                   |
  | HIGH-STRUCTURE | 1    | critical skill (trace-*, scout-feasibility, listen-*) | none (structural coverage reliable)                                |
  | HIGH-STRUCTURE | 2+   | critical skill (trace-*, scout-feasibility, listen-*) | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)      |
  | EVIDENCE-HEAVY | any  | any                                                | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)          |
  | MIXED          | any  | any                                                | REVIEW-FOR-PLAUSIBILITY                                               |

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write the artifact in this exact structure:

---- HEADER BLOCK (required; must be first content after any frontmatter) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header block) ----

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
  - Use the correct section headings for {skill-id}
  - Include all required tables, lists, and scoring structures
  - Place the gate or verdict line in its expected structural position
  - Enforce any category-specific output rules (role card format, numeric rubric, etc.)
  - Use {topic} as the subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the skill
  from the body alone without reading the header.

---

STEP S-5 -- FINALIZE

After the artifact is written, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (in that case, mock-review already controls the next step).
```
