---
skill: quest-variate
skill_target: mock-ns
round: 8
rubric_version: 8
rubric_target: C-27, C-28
date: 2026-03-16
---

# mock-ns -- Round 8 Variations (rubric v8, C-27 + C-28 target)

Rubric: v8 (C-01 through C-28, 5 essential / 3 recommended / 20 aspirational, max 120).

New criteria in v8 (extracted from R7 scoring):

- **C-27** -- Count-strict two-sentence gate: The S-0 preamble gate consists of exactly
  two sentences and no more. Any additional sentence -- elaborative, expository, functional,
  or transitional -- causes the gate to exceed two-sentence form and fails C-27 regardless
  of whether the required sentence types (declarative + imperative) are present. The count
  is not incidental: the compact form ensures the gate cannot be misread as optional
  preamble.

- **C-28** -- Step-role declarative: The declarative identity sentence uses the step as
  its grammatical subject asserting its defining function in the pipeline. A declarative
  sentence where the grammatical subject is an output artifact ("The TOPICS.md status
  line is..."), a sequence position ("The first output is..."), or an abstraction derived
  from the step ("This step's function is...") fails C-28 regardless of sentence position
  or whether C-25's structural requirements appear otherwise satisfied.

R7 evidence sources:

- R7 V-05 (C-27 + C-28 pass): "This step emits first. Write the TOPICS.md status line
  before any other work begins." -- sole variate to pass both; step as nominative subject,
  exactly two sentences.
- R7 V-03 (C-27 fail): "This step emits first. Its single obligation before advancing is
  to report TOPICS.md status. Write the TOPICS.md status line before any other work
  begins." -- elaborative sentence inserted between declarative and imperative; count = 3.
- R7 V-04 (C-28 fail): "The first observable output of this step is the TOPICS.md status
  line." -- artifact as subject ("first observable output"); step appears only as oblique
  modifier.

Variation axes for R8 (three single-axis + one new-dimension + one convergent):

1. **Passive-voice declarative** -- artifact as nominative subject via passive construction;
   isolated C-28 failure with C-27 intact.
2. **Possessive-nominal subject** -- step demoted to genitive modifier; head noun is an
   abstraction ("defining action"); isolated C-28 boundary distinct from V-01's
   artifact-subject form.
3. **Post-imperative enforcement sentence** -- third sentence added after the imperative
   as enforcement rationale (not elaboration between the pair); C-27 fails on count
   regardless of sentence content or position within the gate.
4. **Compound-predicate declarative** -- step as nominative subject with compound predicate
   merging emit primacy and tier-resolve obligations; new dimension: tests whether
   dual-obligation declarative reveals an excellence pattern or a new restriction.
5. **Convergent: symmetric gate-verb pair** -- preamble imperative and terminal gate share
   "begin/begins" as action verb, forming a semantic enforcement mirror; potential new
   excellence signal for C-29.

---

## V-01 -- Passive-Voice Declarative

**Axis:** Grammatical voice of declarative sentence (passive vs active)

**Hypothesis:** A passive-voice declarative places an output artifact in the nominative
subject position: "The TOPICS.md status line is the first output of this step." The step
itself appears only as an oblique modifier ("of this step"), not as the grammatical subject
asserting its pipeline role. This produces a distinct C-28 failure from R7 V-04's
output-sequence form ("The first observable output of this step is X") -- here the passive
construction makes the artifact the agent while the step is demoted to a prepositional
phrase. C-27 PASS (exactly 2 sentences). C-25 PASS on type-coverage reading (declarative +
imperative both present in correct order). C-28 FAIL: grammatical subject is an artifact,
not the step.

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}      (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3       (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- TOPICS.MD EMIT

The TOPICS.md status line is the first output of this step. Write this line before any
other operation begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                               |
  |-----------|-----------|----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)    |

Carry the resolved tier into S-2 and S-3 before any further action.

Do not begin S-1 until the TOPICS.md status line above is emitted.

CONSTRAINT -- operations prohibited during this step:
  No lookup of skill categories.
  No skill-id resolution or namespace-to-skill mapping.
  No mock content generation of any kind.
  No artifact body construction or section assembly.
  No artifact path assembly or file output.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill     | Constraint                                               |
  |-----------|-------------------|----------------------------------------------------------|
  | scout     | scout-feasibility |                                                          |
  | draft     | draft-spec        |                                                          |
  | review    | review-design     |                                                          |
  | flow      | flow-resilience   |                                                          |
  | trace     | trace-request     |                                                          |
  | prove     | prove-hypothesis  |                                                          |
  | listen    | listen-support    |                                                          |
  | program   | program-plan      |                                                          |
  | topic     | topic-plan        | topic-status EXCLUDED -- meta-structural, never default  |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

  Unrecognized skill-id: emit error naming the skill-id and direct user to registry.
  Do not assign a fallback category.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step.

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                              |
  |----------------|--------------------------------------------------|-------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                           |

  Compliance override (applied last, overrides all rows above):
    If compliance tags present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Emit the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill:    {skill-id from S-1}
  Topic:    {topic}
  Category: {CATEGORY from S-2}
  Date:     {today's date}
  Status:   MOCK (awaiting review)
  Flag:     {FLAG from S-3 -- verbatim copy, not rederived}

All six fields are present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning as the first section before any body content,
separated from the header and body with --- delimiters:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace-*, scout-feasibility, listen-*).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially accurate or partially fabricated. Review for plausibility before
    accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the skill's expected structure:
  - All required section headings for the selected skill
  - Required tables or lists in expected positions
  - Gate or verdict line where the real skill produces one
  - Enforcement mechanisms in expected positions

A reader familiar with the real skill must identify which skill was mocked from structure
alone, without reading the header. Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

Emit as the final line of output:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate a thin
namespace.

---

## V-02 -- Possessive-Nominal Subject

**Axis:** Grammatical subject type -- step as possessive-genitive modifier vs nominative
subject

**Hypothesis:** "This step's defining action is to emit first" places "This step" in
genitive/possessive position. The head noun of the subject phrase is "defining action",
not "step". C-28 requires the step as grammatical subject asserting its defining function.
In this construction the step is a modifier ("this step's"), not the agent -- the
nominative subject is "defining action", an abstraction derived from the step. This differs
from V-01 (where an output artifact is subject) and from R7 V-04 (where an output-sequence
position is subject); here the subject is a nominal derivation of the step's own role.
The sentence is declarative, present-tense, and role-asserting in intent -- it correctly
conveys the step's obligation -- but the grammatical structure fails C-28's requirement
that the step itself be the agent. C-28 FAIL. C-27 PASS (exactly 2 sentences).

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}      (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3       (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- TOPICS.MD EMIT

This step's defining action is to emit first. Write the TOPICS.md status line before any
other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                               |
  |-----------|-----------|----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)    |

Carry the resolved tier into S-2 and S-3 before any further action.

Do not begin S-1 until the TOPICS.md status line above is emitted.

CONSTRAINT -- operations prohibited during this step:
  No lookup of skill categories.
  No skill-id resolution or namespace-to-skill mapping.
  No mock content generation of any kind.
  No artifact body construction or section assembly.
  No artifact path assembly or file output.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill     | Constraint                                               |
  |-----------|-------------------|----------------------------------------------------------|
  | scout     | scout-feasibility |                                                          |
  | draft     | draft-spec        |                                                          |
  | review    | review-design     |                                                          |
  | flow      | flow-resilience   |                                                          |
  | trace     | trace-request     |                                                          |
  | prove     | prove-hypothesis  |                                                          |
  | listen    | listen-support    |                                                          |
  | program   | program-plan      |                                                          |
  | topic     | topic-plan        | topic-status EXCLUDED -- meta-structural, never default  |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

  Unrecognized skill-id: emit error naming the skill-id and direct user to registry.
  Do not assign a fallback category.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step.

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                              |
  |----------------|--------------------------------------------------|-------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                           |

  Compliance override (applied last, overrides all rows above):
    If compliance tags present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Emit the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill:    {skill-id from S-1}
  Topic:    {topic}
  Category: {CATEGORY from S-2}
  Date:     {today's date}
  Status:   MOCK (awaiting review)
  Flag:     {FLAG from S-3 -- verbatim copy, not rederived}

All six fields are present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning as the first section before any body content,
separated from the header and body with --- delimiters:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace-*, scout-feasibility, listen-*).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially accurate or partially fabricated. Review for plausibility before
    accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the skill's expected structure:
  - All required section headings for the selected skill
  - Required tables or lists in expected positions
  - Gate or verdict line where the real skill produces one
  - Enforcement mechanisms in expected positions

A reader familiar with the real skill must identify which skill was mocked from structure
alone, without reading the header. Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

Emit as the final line of output:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate a thin
namespace.

---

## V-03 -- Post-Imperative Enforcement Sentence

**Axis:** Gate count -- third sentence added after the imperative as enforcement rationale

**Hypothesis:** R7 V-03 added an elaborative sentence between the declarative and
imperative (count = 3; fails C-27). This variate adds the third sentence after the
imperative and makes it enforcement rationale: "No other step may begin before this
emission completes." The sentence is not expository -- it directly enforces the gate. The
hypothesis tests whether C-27's count-strict requirement applies regardless of (a) where
in the gate the third sentence appears and (b) whether the third sentence carries
functional enforcement value rather than elaboration. Expected result: C-27 fails on count
(3 sentences) regardless of sentence content or placement relative to the required pair.
C-28 PASS ("This step emits first" has step as nominative subject). This demonstrates that
C-27 is content-agnostic: any sentence beyond the declarative+imperative pair fails the
criterion, regardless of the third sentence's purpose.

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}      (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3       (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- TOPICS.MD EMIT

This step emits first. Write the TOPICS.md status line before any other work begins.
No other step may begin before this emission completes.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                               |
  |-----------|-----------|----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)    |

Carry the resolved tier into S-2 and S-3 before any further action.

Do not begin S-1 until the TOPICS.md status line above is emitted.

CONSTRAINT -- operations prohibited during this step:
  No lookup of skill categories.
  No skill-id resolution or namespace-to-skill mapping.
  No mock content generation of any kind.
  No artifact body construction or section assembly.
  No artifact path assembly or file output.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill     | Constraint                                               |
  |-----------|-------------------|----------------------------------------------------------|
  | scout     | scout-feasibility |                                                          |
  | draft     | draft-spec        |                                                          |
  | review    | review-design     |                                                          |
  | flow      | flow-resilience   |                                                          |
  | trace     | trace-request     |                                                          |
  | prove     | prove-hypothesis  |                                                          |
  | listen    | listen-support    |                                                          |
  | program   | program-plan      |                                                          |
  | topic     | topic-plan        | topic-status EXCLUDED -- meta-structural, never default  |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

  Unrecognized skill-id: emit error naming the skill-id and direct user to registry.
  Do not assign a fallback category.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step.

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                              |
  |----------------|--------------------------------------------------|-------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                           |

  Compliance override (applied last, overrides all rows above):
    If compliance tags present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Emit the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill:    {skill-id from S-1}
  Topic:    {topic}
  Category: {CATEGORY from S-2}
  Date:     {today's date}
  Status:   MOCK (awaiting review)
  Flag:     {FLAG from S-3 -- verbatim copy, not rederived}

All six fields are present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning as the first section before any body content,
separated from the header and body with --- delimiters:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace-*, scout-feasibility, listen-*).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially accurate or partially fabricated. Review for plausibility before
    accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the skill's expected structure:
  - All required section headings for the selected skill
  - Required tables or lists in expected positions
  - Gate or verdict line where the real skill produces one
  - Enforcement mechanisms in expected positions

A reader familiar with the real skill must identify which skill was mocked from structure
alone, without reading the header. Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

Emit as the final line of output:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate a thin
namespace.

---

## V-04 -- Compound-Predicate Declarative

**Axis:** Predicate structure of declarative sentence -- simple vs compound predicate

**Hypothesis:** "This step emits first and resolves the tier variable" uses "This step"
as nominative subject (C-28 PASS) with a compound predicate that merges two pipeline
obligations: emit primacy and tier resolution. Exactly 2 sentences (C-27 PASS). This is
new territory: the declarative no longer asserts a single role but bundles two simultaneous
obligations. The hypothesis tests whether a compound-predicate declarative creates a new
excellence signal (denser information per sentence, tier-carry partially satisfied in the
preamble) or reveals a new restriction: the declarative should assert only the step's
emission identity and compound predicates that bundle additional pipeline contracts dilute
the identity assertion. If V-04 scores 120/120, the compound form is acceptable. If it
reveals a scoring gap, a candidate C-29 emerges: the declarative sentence asserts emit
primacy as a single-predicate statement -- compound predicates that merge downstream
contracts into the gate sentence fail the identity-assertion requirement.

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}      (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3       (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- TOPICS.MD EMIT

This step emits first and resolves the tier variable. Write the TOPICS.md status line
before any other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                               |
  |-----------|-----------|----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)    |

Carry the resolved tier into S-2 and S-3 before any further action.

Do not begin S-1 until the TOPICS.md status line above is emitted.

CONSTRAINT -- operations prohibited during this step:
  No lookup of skill categories.
  No skill-id resolution or namespace-to-skill mapping.
  No mock content generation of any kind.
  No artifact body construction or section assembly.
  No artifact path assembly or file output.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill     | Constraint                                               |
  |-----------|-------------------|----------------------------------------------------------|
  | scout     | scout-feasibility |                                                          |
  | draft     | draft-spec        |                                                          |
  | review    | review-design     |                                                          |
  | flow      | flow-resilience   |                                                          |
  | trace     | trace-request     |                                                          |
  | prove     | prove-hypothesis  |                                                          |
  | listen    | listen-support    |                                                          |
  | program   | program-plan      |                                                          |
  | topic     | topic-plan        | topic-status EXCLUDED -- meta-structural, never default  |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

  Unrecognized skill-id: emit error naming the skill-id and direct user to registry.
  Do not assign a fallback category.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step.

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                              |
  |----------------|--------------------------------------------------|-------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                           |

  Compliance override (applied last, overrides all rows above):
    If compliance tags present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Emit the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill:    {skill-id from S-1}
  Topic:    {topic}
  Category: {CATEGORY from S-2}
  Date:     {today's date}
  Status:   MOCK (awaiting review)
  Flag:     {FLAG from S-3 -- verbatim copy, not rederived}

All six fields are present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning as the first section before any body content,
separated from the header and body with --- delimiters:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace-*, scout-feasibility, listen-*).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially accurate or partially fabricated. Review for plausibility before
    accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the skill's expected structure:
  - All required section headings for the selected skill
  - Required tables or lists in expected positions
  - Gate or verdict line where the real skill produces one
  - Enforcement mechanisms in expected positions

A reader familiar with the real skill must identify which skill was mocked from structure
alone, without reading the header. Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

Emit as the final line of output:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate a thin
namespace.

---

## V-05 -- Convergent: Symmetric Gate-Verb Pair

**Axes (combined):** Single-predicate declarative + preamble-terminal gate vocabulary
alignment

**Hypothesis:** R7 V-05's imperative uses "before any other work begins" (scope-framed:
"work" is an undefined unit). This variate changes the imperative to "before any other
step begins" (pipeline-framed: "step" is the unit of the execution model). This creates
a new excellence signal: the preamble imperative ("before any other step begins") and the
terminal gate ("Do not begin S-1 until the TOPICS.md status line is written") both use
"begin" as the action verb -- a semantic enforcement mirror. A reader can audit the gate
pair by vocabulary alone: both positions use the same word to name the prohibited action.
The declarative remains minimal and single-predicate ("This step emits first") -- no
compound obligations merged in. Together: a self-contained declarative asserting exactly
one role + an imperative framed in pipeline units + a terminal gate that echoes the
imperative's verb. Potential C-29: preamble imperative and terminal gate share the action
verb, making the enforcement pair auditable by vocabulary alignment.

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}
  --skill    {skill-id}      (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3       (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- TOPICS.MD EMIT

This step emits first. Write the TOPICS.md status line before any other step begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                               |
  |-----------|-----------|----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)    |

Carry the resolved tier into S-2 and S-3 before any further action.

Do not begin S-1 until the TOPICS.md status line above is written.

CONSTRAINT -- operations prohibited during this step:
  No lookup of skill categories.
  No skill-id resolution or namespace-to-skill mapping.
  No mock content generation of any kind.
  No artifact body construction or section assembly.
  No artifact path assembly or file output.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill     | Constraint                                               |
  |-----------|-------------------|----------------------------------------------------------|
  | scout     | scout-feasibility |                                                          |
  | draft     | draft-spec        |                                                          |
  | review    | review-design     |                                                          |
  | flow      | flow-resilience   |                                                          |
  | trace     | trace-request     |                                                          |
  | prove     | prove-hypothesis  |                                                          |
  | listen    | listen-support    |                                                          |
  | program   | program-plan      |                                                          |
  | topic     | topic-plan        | topic-status EXCLUDED -- meta-structural, never default  |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

  Unrecognized skill-id: emit error naming the skill-id and direct user to registry.
  Do not assign a fallback category.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step.

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                              |
  |----------------|--------------------------------------------------|-------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                           |

  Compliance override (applied last, overrides all rows above):
    If compliance tags present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Emit the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill:    {skill-id from S-1}
  Topic:    {topic}
  Category: {CATEGORY from S-2}
  Date:     {today's date}
  Status:   MOCK (awaiting review)
  Flag:     {FLAG from S-3 -- verbatim copy, not rederived}

All six fields are present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning as the first section before any body content,
separated from the header and body with --- delimiters:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace-*, scout-feasibility, listen-*).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially accurate or partially fabricated. Review for plausibility before
    accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the skill's expected structure:
  - All required section headings for the selected skill
  - Required tables or lists in expected positions
  - Gate or verdict line where the real skill produces one
  - Enforcement mechanisms in expected positions

A reader familiar with the real skill must identify which skill was mocked from structure
alone, without reading the header. Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

Emit as the final line of output:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate a thin
namespace.

---

## Predicted R8 scores under rubric v8 (max 120)

| Variate | C-27 | C-28 | Predicted score | Prediction rationale |
|---------|------|------|-----------------|----------------------|
| V-05 (Convergent: Symmetric Gate-Verb Pair) | PASS | PASS | 120/120 | "This step emits first" -- step as nominative subject, exactly 2 sentences; new signal not yet in rubric |
| V-04 (Compound-Predicate Declarative) | PASS | PASS | 120/120 | "This step" retained as nominative subject; compound predicate does not alter grammatical subject |
| V-01 (Passive-Voice Declarative) | PASS | FAIL | 118/120 | "The TOPICS.md status line is the first output of this step" -- artifact as nominative subject; step is oblique |
| V-02 (Possessive-Nominal Subject) | PASS | FAIL | 118/120 | "This step's defining action" -- head noun "defining action", not "step"; step demoted to genitive modifier |
| V-03 (Post-Imperative Enforcement Sentence) | FAIL | PASS | 118/120 | "This step emits first" passes C-28; third sentence after imperative ("No other step may begin...") fails C-27 count-strict |

**V-04 note:** V-04 is predicted to score 120/120 under v8. If confirmed, R9 faces the
question: does compound-predicate emit-plus-tier in the declarative represent a neutral
form (same score) or does it open a new restriction -- the declarative should assert emit
primacy as a single-predicate statement, and merging in downstream pipeline contracts
dilutes the identity assertion? If V-04 scores higher than R7 V-05 in any sub-analysis,
a candidate C-29 emerges on the excellence side. If scorers penalize the compound form,
C-29 emerges on the restriction side: declarative is single-predicate, emit-primacy only.

**V-03 note:** V-03 confirms C-27 is position-agnostic and content-agnostic: the third
sentence fails C-27 whether it appears between the pair (R7 V-03 elaboration form) or
after the pair (R8 V-03 enforcement form). Count = 3 fails in both cases.

**V-01 vs V-02 distinction:** V-01 is an artifact-subject failure (passive voice makes
artifact nominative: "The TOPICS.md status line is the first output"). V-02 is a
possessive-nominal failure (step becomes genitive modifier, "defining action" is
nominative: "This step's defining action is to emit first"). These are two independent
C-28 failure modes: artifact-primacy and nominal-derivation. V-01 is closest to R7 V-04
("first observable output"); V-02 is a new boundary not previously tested.

**Candidate C-29 from V-05 (symmetric gate-verb):** If scoring confirms that V-05's
preamble imperative ("before any other step begins") and terminal gate ("Do not begin
S-1") share "begin" as action verb, a potential criterion emerges:
  Candidate C-29 text: "The imperative sentence in the S-0 preamble gate and the S-0
  terminal gate use the same action verb, creating a semantic enforcement mirror that
  allows the two gate positions to be verified as a matched pair from vocabulary alone."
  The pipeline-unit framing ("step" vs "work") is a secondary signal: "step" names the
  architectural unit; "work" names an undefined scope. If this also scores as an
  excellence pattern, a second candidate emerges from V-05.
