---
skill: quest-variate
skill_target: mock-ns
round: 7
rubric_version: 7
rubric_target: C-25, C-26
date: 2026-03-16
---

# mock-ns -- Round 7 Variations (rubric v7, C-25 + C-26 target)

Rubric: v7 (C-01 through C-26, 5 essential / 3 recommended / 18 aspirational, max 116).

New criteria in v7 (extracted from R6 scoring):

- **C-25** -- Two-sentence gate form: The S-0 preamble gate (required for C-23) must
  consist of two sentences in this order: (1) a declarative identity sentence asserting
  the step's emit primacy as a statement of ROLE -- "This step emits first" or equivalent;
  then (2) an imperative emit instruction -- "Write the TOPICS.md status line before any
  other work begins." A single-sentence imperative passes C-23 but fails C-25. The order
  is specified: declarative first, imperative second.

- **C-26** -- Synonym CONSTRAINT vocabulary: Every op-type prohibition in the CONSTRAINT
  block must use vocabulary that is semantically equivalent to but lexically distinct from
  the canonical op-type label. All five prohibitions must use synonym forms. Even one
  canonical phrase in the CONSTRAINT block fails C-26, regardless of how many synonym
  forms are present.

R6 evidence sources:
- R6 V-05 (C-25 + C-26 pass): "This step emits first. Write the TOPICS.md status line
  before any other work begins." + "No lookup of skill categories. No skill-id resolution.
  No mock content generation. No artifact body construction. No artifact path assembly or
  file output." -- sole variate to pass both.
- R6 V-01 (C-25 fail): Single-sentence gate "Before any other step begins, emit the
  TOPICS.md status line below." passes C-23 (zero pre-gate surface) but fails C-25
  (missing declarative identity sentence).
- R6 V-02/V-03 (C-26 fail): 5-op CONSTRAINT using canonical phrases ("No category lookup.
  No skill selection. No mock generation. No body generation. No artifact path construction
  or file write.") passes C-24 but fails C-26.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | C-25 order boundary: imperative-first two-sentence gate | Gate uses two sentences in reversed order: imperative first, declarative second. Tests whether C-25 requires the specific declarative-then-imperative order or just the presence of both sentences. C-23 passes (gate content is still S-0 opening). C-25 predicted FAIL. Score: 114/116. |
| V-02 | C-26 partial boundary: 4/5 synonymized, 1 canonical retained | CONSTRAINT synonymizes 4 op types but retains the canonical C-24 phrase for op type 5 (artifact write): "No artifact path construction or file write." C-25 passes (R6 V-05 gate form). C-26 predicted FAIL (one canonical phrase disqualifies). Score: 114/116. |
| V-03 | C-25 three-sentence boundary: enriched declarative (2 declarative + 1 imperative) | S-0 opens with three sentences: identity assertion, elaboration, imperative. Tests whether "consists of two sentences" in C-25 means exactly two or at least two with both types present. C-25 result uncertain: 114/116 if exactly-two required; 116/116 if at-least-two. |
| V-04 | C-25 output-primacy boundary: output named first, not step role | Gate opens: "The first observable output of this step is the TOPICS.md status line. Write it before any other work begins." Two sentences present, declarative first -- but declarative asserts output ordering, not step role. C-25 requires step-role assertion. Predicted FAIL. Score: 114/116. |
| V-05 | Convergent: all 26 criteria, CONSTRAINT with deepened synonym vocabulary | Two-sentence gate retained from R6 V-05. CONSTRAINT synonyms deepened to share zero lexemes with canonical phrases. Tests that extreme paraphrase satisfies C-26 without proximity bound. Predicts 116/116. |

---

## V-01 -- C-25 Order Boundary: Imperative-First Two-Sentence Gate (C-25 Deliberate Fail)

**Axis**: Two-sentence gate sentence order. Tests whether C-25 requires the declarative
sentence to precede the imperative, or whether just having both sentences present suffices.
**Change from R6 V-05**: Gate sentences transposed -- imperative appears first ("Write
the TOPICS.md status line before any other work begins."), declarative appears second
("This step emits first."). No other changes.
**Hypothesis**: C-23 passes (gate-type content is the absolute first content of S-0 --
zero non-gate surface area even with sentences transposed). C-25 fails -- the pass
condition specifies: "(1) a declarative identity sentence... and (2) an imperative
instruction" with the numbered ordering prescriptive; declarative must precede imperative.
The trap: scorer sees both sentences present and awards C-25 without checking order.
Both sentences being present is necessary but not sufficient -- the declarative must
establish identity before the imperative directs action.
**Predicts**: C-01--C-24: all pass. C-25: fail. C-26: pass. Expected composite: 114/116.

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

Write the TOPICS.md status line before any other work begins. This step emits first.

CONSTRAINT: No lookup of skill categories. No skill-id resolution. No mock content
generation. No artifact body construction. No artifact path assembly or file output.
None of these operations begin until after the TOPICS.md status line below has been
written to the conversation.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not begin until the line above appears in the conversation.
Forward the resolved tier to S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id is not found in any row, emit an error naming the unrecognized
skill-id and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (evaluated after table match, regardless of row result):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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

---

STEP A-3 -- GENERATE ARTIFACT BODY

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

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-02 -- C-26 Partial Boundary: 4/5 Synonymized, 1 Canonical Retained (C-26 Deliberate Fail)

**Axis**: Synonym coverage completeness. Tests C-26's "even one op-type in canonical
phrase form" rule -- whether a CONSTRAINT with 4/5 synonym forms and 1 canonical phrase
satisfies or fails C-26.
**Change from R6 V-05**: CONSTRAINT retains synonym vocabulary for op types 1-4 but reverts
op type 5 (artifact write phase) to the canonical C-24 phrase: "No artifact path
construction or file write." Two-sentence gate unchanged (C-25 passes).
**Hypothesis**: C-24 passes (5 ops named). C-25 passes (R6 V-05 declarative-first gate
retained). C-26 fails -- "No artifact path construction or file write" is the canonical
phrase from the C-24 definition; it is not a synonym form. C-26 is all-or-nothing: every
prohibition must use distinct vocabulary. The trap: scorer sees 4/5 synonym forms and
awards partial credit, or reads "most prohibitions use synonyms" as satisfying C-26.
**Predicts**: C-01--C-25: all pass. C-26: fail. Expected composite: 114/116.

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

This step emits first. Write the TOPICS.md status line before any other work begins.

CONSTRAINT: No lookup of skill categories. No skill-id resolution. No mock content
generation. No artifact body construction. No artifact path construction or file write.
None of these operations begin until after the TOPICS.md status line below has been
written to the conversation.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not begin until the line above appears in the conversation.
Forward the resolved tier to S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id is not found in any row, emit an error naming the unrecognized
skill-id and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (evaluated after table match, regardless of row result):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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

---

STEP A-3 -- GENERATE ARTIFACT BODY

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

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-03 -- C-25 Three-Sentence Boundary: Enriched Declarative (2 Declarative + 1 Imperative)

**Axis**: C-25 sentence-count interpretation. Tests whether "consists of two sentences"
in the C-25 pass condition means exactly two sentences, or at least two sentences with
both required types (declarative identity + imperative) present.
**Change from R6 V-05**: Gate expanded from two sentences to three -- an elaboration
sentence is inserted between the identity assertion and the imperative: "This step emits
first. Its single obligation before advancing is to report TOPICS.md status. Write the
TOPICS.md status line before any other work begins."
**Hypothesis**: C-23 passes (first sentence is still pure identity/gate content -- zero
pre-gate surface area). C-25 result is uncertain -- the rubric says "consists of two
sentences: (1) declarative... and (2) imperative" which could be exactly-two (fail: three
sentences present) or type-specification (pass: both required types present; additional
declarative doesn't violate either type requirement). This variate surfaces the C-25
sentence-count interpretation boundary. A fail here warrants a rubric clarification note
in v8 ("exactly two sentences"); a pass confirms C-25 is type-based rather than
count-based. The CONSTRAINT is unchanged from R6 V-05 synonym form (C-26 passes).
**Predicts**: C-01--C-24: all pass. C-26: pass. C-25: uncertain.
If exactly-two required: 114/116. If at-least-two-with-both-types: 116/116.

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

This step emits first. Its single obligation before advancing is to report TOPICS.md
status. Write the TOPICS.md status line before any other work begins.

CONSTRAINT: No lookup of skill categories. No skill-id resolution. No mock content
generation. No artifact body construction. No artifact path assembly or file output.
None of these operations begin until after the TOPICS.md status line below has been
written to the conversation.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not begin until the line above appears in the conversation.
Forward the resolved tier to S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id is not found in any row, emit an error naming the unrecognized
skill-id and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (evaluated after table match, regardless of row result):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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

---

STEP A-3 -- GENERATE ARTIFACT BODY

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

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-04 -- C-25 Output-Primacy Boundary: Output Named First, Not Step Role (C-25 Deliberate Fail)

**Axis**: C-25 declarative identity type. Tests whether a declarative sentence asserting
OUTPUT primacy ("the first observable output of this step is X") satisfies C-25's
requirement for a declaration of the step's ROLE ("This step emits first" -- asserting
what the step IS, not just what it produces first).
**Change from R6 V-05**: Gate sentences rewritten to output-primacy form: "The first
observable output of this step is the TOPICS.md status line. Write it before any other
work begins." Two sentences present, declarative first -- but the declarative frames
output ordering rather than step identity. CONSTRAINT unchanged (C-26 passes).
**Hypothesis**: C-23 passes (first sentence is still gate-type content at S-0 opening --
zero pre-gate surface area). C-25 fails -- the pass condition specifies "a declarative
identity sentence asserting the step's emit primacy as a statement of the step's ROLE."
Output-primacy framing ("the first observable output is X") is a claim about output
sequence, not about the step's functional identity. The distinction: identity declaration
("This step emits first" -- what the step IS) vs output-ordering declaration ("the first
output is X" -- what comes out first). The trap: scorer sees two sentences with declarative
+ imperative pattern and awards C-25 without examining whether the declarative asserts
step role vs output position.
**Predicts**: C-01--C-24: all pass. C-25: fail. C-26: pass. Expected composite: 114/116.

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

The first observable output of this step is the TOPICS.md status line. Write it before
any other work begins.

CONSTRAINT: No lookup of skill categories. No skill-id resolution. No mock content
generation. No artifact body construction. No artifact path assembly or file output.
None of these operations begin until after the TOPICS.md status line below has been
written to the conversation.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not begin until the line above appears in the conversation.
Forward the resolved tier to S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id is not found in any row, emit an error naming the unrecognized
skill-id and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (evaluated after table match, regardless of row result):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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

---

STEP A-3 -- GENERATE ARTIFACT BODY

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

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-05 -- Convergent: All 26 Criteria, CONSTRAINT with Deepened Synonym Vocabulary (Predicts 116/116)

**Axis**: C-26 synonym depth tolerance. Tests whether CONSTRAINT synonyms that share
zero lexemes with canonical op-type phrases still satisfy C-26, or whether an implicit
proximity bound exists that disqualifies extremely remote paraphrase.
**Changes from R6 V-05**:
1. CONSTRAINT synonyms replaced with deeper paraphrase sharing no lexemes with canonical
   phrases: "No classification of skill registries. No routing of input identifiers to
   skill records. No synthesis of simulated content. No composition of artifact sections.
   No filesystem path formation or file emission."
   - Canonical: "No category lookup" -> "No classification of skill registries"
   - Canonical: "No skill selection" -> "No routing of input identifiers to skill records"
   - Canonical: "No mock generation" -> "No synthesis of simulated content"
   - Canonical: "No body generation" -> "No composition of artifact sections"
   - Canonical: "No artifact path assembly or file output" -> "No filesystem path formation
     or file emission"
   Zero shared content words between any canonical phrase and its replacement.
2. Two-sentence gate retained verbatim from R6 V-05 (C-25 passes).
3. All other steps unchanged from R6 V-05.
**Hypothesis**: C-26 passes -- the criterion specifies "semantically equivalent to but
lexically distinct from the canonical op-type label" with no proximity bound. Deep
synonymization satisfies lexical distinctness at the maximum degree; semantic equivalence
is preserved because each phrase names the same prohibited operation concept. If this
variate fails C-26 (scorer argues the synonyms are "too abstract to verify"), that reveals
a C-27 discriminator (synonym proximity bound) worth extracting into rubric v8.
**Predicts**: C-01--C-26: all pass. Expected composite: 116/116.

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

This step emits first. Write the TOPICS.md status line before any other work begins.

CONSTRAINT: No classification of skill registries. No routing of input identifiers to
skill records. No synthesis of simulated content. No composition of artifact sections.
No filesystem path formation or file emission. None of these actions begin until after
the TOPICS.md status line below appears in the conversation.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not begin until the line above appears in the conversation.
Forward the resolved tier to S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id is not found in any row, emit an error naming the unrecognized
skill-id and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (evaluated after table match, regardless of row result):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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

---

STEP A-3 -- GENERATE ARTIFACT BODY

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

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## R7 Variation Summary

| Variate | Single-axis change | C-25 pred | C-26 pred | Score pred |
|---------|--------------------|-----------|-----------|------------|
| V-01 | Gate sentences transposed: imperative first, declarative second | FAIL | PASS | 114/116 |
| V-02 | CONSTRAINT: 4/5 synonymized, op-5 canonical form retained | PASS | FAIL | 114/116 |
| V-03 | Gate: 3 sentences (declarative + elaboration + imperative) | UNCERTAIN | PASS | 114 or 116 |
| V-04 | Gate declarative frames output-primacy, not step role | FAIL | PASS | 114/116 |
| V-05 | CONSTRAINT with deepened synonyms (zero shared lexemes with canonical) | PASS | PASS | 116/116 |

**New traps documented:**
- "Reversed two-sentence gate satisfies C-23, misses C-25" (V-01): Both sentences present
  at S-0 opening, imperative precedes declarative. C-25 specifies declarative-first order --
  presence of both sentences necessary but not sufficient.
- "4/5 synonymization satisfies C-24, misses C-26" (V-02): Four op types paraphrased,
  one retained in canonical form. C-26's all-or-nothing requirement fires on the single
  canonical phrase regardless of synonym coverage elsewhere.
- "Three-sentence gate tests C-25 count interpretation" (V-03): Open question surfaced for
  rubric clarification. If V-03 fails C-25, the v8 rubric should add "exactly two sentences";
  if it passes, no change -- C-25 is type-based not count-based.
- "Output-primacy declarative fails step-role identity" (V-04): Two sentences, declarative
  first -- but declares output ordering rather than step identity. C-25 requires the
  declarative to assert what the step IS, not what it outputs first.
- "Deep synonymization still satisfies C-26" (V-05): Tests whether C-26 has an implicit
  proximity bound. If V-05 fails, a new C-27 on synonym proximity would be extracted.
