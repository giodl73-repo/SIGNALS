---
skill: quest-variate
skill_target: mock-ns
round: 9
rubric_version: 9
rubric_target: C-29, C-30
date: 2026-03-16
---

# mock-ns -- Round 9 Variations (rubric v9, C-29 + C-30 target)

Rubric: v9 (C-01 through C-30, 5 essential / 3 recommended / 22 aspirational, max 124).

New criteria in v9 (extracted from R8 scoring):

- **C-29** -- Nominative-subject test: The declarative sentence must have the step as
  direct nominative head of the subject noun phrase. Possessive-nominal constructions
  fail ("This step's defining action is to emit first") -- the nominalization "defining
  action" is the grammatical subject; "This step" occupies genitive modifier position.
  Substitution test: replace the subject noun phrase with "It" -- if "It" refers to an
  abstraction derived from the step, the step is not the grammatical subject.

- **C-30** -- Artifact-subject prohibition: The declarative sentence must not promote
  an output artifact to nominative subject position in active voice. "The TOPICS.md
  status line is the first output of this step" fails -- the artifact is nominative
  subject; the step appears only as oblique modifier "of this step." Distinct from
  C-28's output-sequence-subject form and C-29's possessive-nominal form.

R8 evidence sources:

- R8 V-04 (C-27 + C-28 + C-29 + C-30 PASS, 124/124): "This step emits first and
  resolves the tier variable. Write the TOPICS.md status line before any other work
  begins." Step is direct nominative subject; compound predicate keeps step as agent
  of both predicates.
- R8 V-05 (C-27 + C-28 + C-29 + C-30 PASS, 124/124): Symmetric gate-verb pair -- also
  direct nominative action form.
- R8 V-01 (C-30 FAIL, 122/124): "The TOPICS.md status line is the first output of this
  step." Artifact as nominative subject in active voice.
- R8 V-02 (C-29 FAIL, 122/124): "This step's defining action is to emit first."
  Possessive-nominal subject; step demoted to genitive modifier.
- R8 V-03 (C-27 FAIL, 122/124): Three-sentence gate (enforcement sentence added after
  imperative; count = 3 regardless of sentence utility).

Confirmed baseline for R9 (any of: R8 V-04 form, R8 V-05 form):
  "This step emits first [and resolves the tier variable]."
  "Write the TOPICS.md status line before any other work begins."

Variation axes for R9 (three single-axis + two combined):

1. **Predicative-identity declarative** (V-01) -- "S-0 is the emit step." vs action
   form "This step emits first." C-25 explicitly lists "S-0 is the emit step" as an
   equivalent form. Tests: does the identity-predicate form satisfy C-28/C-29/C-30
   when a step label ("S-0") occupies nominative position?

2. **Modal-obligation declarative** (V-02) -- "This step must emit first." vs
   indicative "This step emits first." C-25 requires "a declarative identity sentence
   asserting the step's emit primacy as a statement of the step's ROLE" and "present-
   tense declaration." Tests whether a modal-obligation sentence declares role identity
   or imposes an obligation (potential C-25/C-28 failure mode: mood-sensitive).

3. **Tier-carry compound predicate with named consumers** (V-03) -- "This step emits
   first and carries tier into S-2 and S-3." Unlike R8 V-04's "resolves the tier
   variable" (no consumer labels), this compound directly names S-2 and S-3. Tests:
   (a) does C-18 accept the declarative opening sentence as the "explicit handoff
   sentence" when the standalone terminal sentence is removed? (b) does C-20's
   "standalone terminal sentence" require a separate prose sentence independent of
   the declarative, making C-20 position-sensitive?

4. **Two-axis: V-01 identity + V-03 tier-carry consumers** (V-04) -- "S-0 is the
   emit step and carries tier into S-2 and S-3." Identity compound with consumer
   labels. Tests whether identity-predicate compound satisfies C-18 and C-28
   simultaneously, and repeats the C-20 terminal-position test in identity form.

5. **Synthesis: V-03 compound + full C-18/C-20 dual-register coverage** (V-05) --
   Retains the tier-carry compound in the declarative (satisfying C-18 via declarative)
   AND the standalone terminal sentence (satisfying C-20 dual-register requirement).
   Maximum redundancy; predicted 124/124.

---

## V-01 -- Predicative-Identity Declarative

**Axis:** Declarative sentence form -- identity-predicate ("S-0 is the emit step") vs
action-predicate ("This step emits first")

**Hypothesis:** C-25 pass condition explicitly includes "S-0 is the emit step" as an
equivalent declarative form alongside "This step emits first." The step label "S-0"
serves as direct nominative subject; "is the emit step" is an identity predicate that
names the step's structural role in the pipeline. C-28 PASS: step as grammatical subject
asserting its defining function (role identity, not output-position claim). C-29 PASS:
"S-0" is a direct step-label nominative -- it refers to the step itself, not to an
abstraction derived from it; the substitution test ("It emits first" would refer to S-0,
not an abstraction). C-30 PASS: no artifact in subject position. C-27 PASS: exactly two
sentences. Predicted: 124/124.

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

S-0 is the emit step. Write the TOPICS.md status line before any other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                                |
  |-----------|-----------|-----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)     |

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

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                           |
  |----------------|--------------------------------------------------|-------|----------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                        |

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

Write the category-matched fidelity warning before any body content,
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

## V-02 -- Modal-Obligation Declarative

**Axis:** Declarative sentence mood -- modal-obligation ("must emit") vs indicative
action ("emits first")

**Hypothesis:** "This step must emit first" places the step as direct nominative subject
("This step") with a modal predicate ("must emit first"). C-29 PASS: "This step" is
direct nominative, not a nominalization. C-30 PASS: no artifact in subject position.
C-27 PASS: exactly two sentences. The discriminator is C-25/C-28: C-25 requires "a
declarative identity sentence asserting the step's emit primacy as a statement of the
step's ROLE" with "present-tense declaration that names the step's defining function."
C-28 requires the step as grammatical subject "asserting its defining function in the
pipeline." The question: does "must emit" ASSERT the step's function (declarative reading)
or COMMAND it (deontic reading)? If the modal "must" converts the sentence from a
description of what S-0 IS into a prescription of what S-0 SHOULD DO, then C-28 fails
(the sentence imposes obligation rather than declares identity). The prediction: C-25/C-28
FAIL -- "must emit" is mood-obligation, not role-declaration; C-25 requires a declarative
that identifies the step's role, and a modal imposes a norm rather than declaring a fact
about the step's nature. Predicted: 120/124 (fail C-25 at -2, fail C-28 at -2).

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

This step must emit first. Write the TOPICS.md status line before any other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                                |
  |-----------|-----------|-----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)     |

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

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                           |
  |----------------|--------------------------------------------------|-------|----------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                        |

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

Write the category-matched fidelity warning before any body content,
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

## V-03 -- Tier-Carry Compound Predicate with Named Consumers (No Terminal Sentence)

**Axis:** Compound predicate content names downstream consumers; standalone terminal
tier-carry sentence removed; C-18/C-20 position-sensitivity tested

**Hypothesis:** "This step emits first and carries tier into S-2 and S-3" places the
step as direct nominative subject with a compound predicate. The first conjunct ("emits
first") satisfies the emit-primacy requirement of C-25/C-28/C-29/C-30. The second
conjunct ("carries tier into S-2 and S-3") names the tier as carried artifact and names
both downstream consumers by step label -- satisfying C-18's requirement for an explicit
handoff sentence. C-28/C-29/C-30 all PASS (same subject-position reasoning as R8 V-04's
compound predicate). C-27 PASS: exactly two sentences in gate. C-18 question: the
declarative sentence IS "an explicit handoff sentence naming tier and two downstream
steps" -- does C-18 care that this sentence is the opening declarative rather than a
terminal prose sentence? C-20 question: C-20 requires the tier-carry to appear "as a
standalone terminal sentence in S-0 prose naming both consumers." The opening declarative
is not terminal. With the standalone sentence removed, C-20 may fail. The design
deliberately omits "Carry the resolved tier into S-2 and S-3 before any further action"
to test this boundary. Predicted: 122/124 (C-20 FAIL at -2) if C-20 is position-
sensitive; 124/124 if C-20 accepts the declarative compound as the standalone sentence.

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

This step emits first and carries tier into S-2 and S-3. Write the TOPICS.md status line
before any other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                                |
  |-----------|-----------|-----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)     |

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

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                           |
  |----------------|--------------------------------------------------|-------|----------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                        |

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

Write the category-matched fidelity warning before any body content,
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

## V-04 -- Two-Axis: Identity Declarative + Tier-Carry Consumers (No Terminal Sentence)

**Axes:** V-01 (predicative-identity declarative) + V-03 (tier-carry with named
consumers; standalone terminal sentence removed)

**Hypothesis:** "S-0 is the emit step and carries tier into S-2 and S-3" is an identity
compound predicate where the first conjunct asserts the step's role ("is the emit step")
and the second conjunct names the tier handoff with consumers. C-28: the step label "S-0"
is grammatical subject asserting its pipeline role via identity predicate -- PASS. C-29:
"S-0" is direct nominative step-label -- PASS. C-30: no artifact in subject position --
PASS. C-27: exactly two sentences -- PASS. C-18 question: same as V-03 -- the declarative
compound names tier and consumers; does C-18 accept it as the "explicit handoff sentence"?
The identity form ("is the emit step and carries tier...") may satisfy C-18 even when it
doesn't use an action verb for the tier-carry specifically: "S-0 carries tier into S-2
and S-3" is a clear carry statement in the compound. C-20 question: same as V-03 -- no
standalone terminal sentence; tests whether C-20 passes in identity form the same as in
action form. Predicted: 122/124 (same C-20 boundary as V-03) if C-20 is position-
sensitive. If C-18 also fails in identity form (the "is" predicate is not an "explicit
handoff" by some readings), then 120/124 (two failures).

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

S-0 is the emit step and carries tier into S-2 and S-3. Write the TOPICS.md status line
before any other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                                |
  |-----------|-----------|-----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)     |

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

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                           |
  |----------------|--------------------------------------------------|-------|----------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                        |

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

Write the category-matched fidelity warning before any body content,
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

## V-05 -- Synthesis: Tier-Carry Compound + Full C-18/C-20 Dual-Register Coverage

**Axes:** V-03 compound predicate with named consumers + standalone terminal sentence
retained to ensure C-20 dual-register (table cell + terminal prose sentence both present)

**Hypothesis:** V-03 and V-04 test whether the declarative compound alone satisfies
C-18/C-20. V-05 resolves that question by retaining all three registers simultaneously:
(1) the declarative compound "This step emits first and carries tier into S-2 and S-3"
-- satisfies C-18 via declarative sentence naming tier and consumers; (2) the tier-carry
table row with "Carry into S-2 (category) and S-3 (flag)" -- satisfies C-20's table-
column requirement; (3) the standalone terminal sentence "Carry the resolved tier into
S-2 and S-3 before any further action" -- satisfies C-20's standalone terminal sentence
requirement. All three registers encode the same obligation independently. C-20 is
satisfied with maximum redundancy regardless of whether C-20 is position-sensitive. The
preamble gate remains count-strict at exactly two sentences (the declarative and the
imperative); the standalone tier-carry sentence appears AFTER the resolution bullets, as
prose content within S-0 but not within the two-sentence gate. C-27 PASS (gate = 2
sentences). C-28/C-29/C-30 PASS (step as direct nominative with action compound).
Predicted: 124/124 -- maximum coverage synthesis.

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

This step emits first and carries tier into S-2 and S-3. Write the TOPICS.md status line
before any other work begins.

Resolve TOPICS.md:
  - If TOPICS.md exists: read tier; read compliance tags if present.
  - If TOPICS.md absent: tier = 1 (default); compliance tags = none.
  - Emit: > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Tier-carry contract:

  | Parameter | Source    | Downstream use                                |
  |-----------|-----------|-----------------------------------------------|
  | tier      | TOPICS.md | Carry into S-2 (category) and S-3 (flag)     |

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

  | CATEGORY       | Skill condition                                  | Tier  | FLAG                                                           |
  |----------------|--------------------------------------------------|-------|----------------------------------------------------------------|
  | HIGH-STRUCTURE | non-critical                                     | any   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | 1     | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE | critical (trace-*, scout-feasibility, listen-*)  | >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | EVIDENCE-HEAVY | any                                              | any   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | MIXED          | any                                              | any   | REVIEW-FOR-PLAUSIBILITY                                        |

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

Write the category-matched fidelity warning before any body content,
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

## Predicted Scores (v9 rubric, max 124)

| Variate | Declarative sentence | C-25 | C-27 | C-28 | C-29 | C-30 | C-18 | C-20 | Predicted |
|---------|---------------------|------|------|------|------|------|------|------|-----------|
| V-01 (Identity declarative) | "S-0 is the emit step." | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 124/124 |
| V-02 (Modal-obligation) | "This step must emit first." | FAIL | PASS | FAIL | PASS | PASS | PASS | PASS | 120/124 |
| V-03 (Tier-carry compound, no terminal) | "This step emits first and carries tier into S-2 and S-3." | PASS | PASS | PASS | PASS | PASS | PASS | ? | 122 or 124 |
| V-04 (Identity + tier-carry, no terminal) | "S-0 is the emit step and carries tier into S-2 and S-3." | PASS | PASS | PASS | PASS | PASS | ? | ? | 120-124 |
| V-05 (Synthesis: compound + dual-register) | "This step emits first and carries tier into S-2 and S-3." | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 124/124 |

**Three discriminators targeted:**

1. **C-25/C-28 mood-sensitivity** (V-02): Does "must emit" satisfy the declarative-role
   requirement of C-25, or does the modal convert the sentence from role-assertion to
   obligation-imposition? If C-28 is mood-sensitive, V-02 fails at -4 (C-25 + C-28 both
   fail). If C-28 accepts modal-obligation as role-assertion, V-02 scores 124/124 and a
   new permissive note is added for C-25 and C-28.

2. **C-20 terminal-position sensitivity** (V-03 vs V-05): C-20 requires tier-carry "as
   a standalone terminal sentence in S-0 prose." V-03 has the tier-carry only in the
   opening declarative compound (not terminal). V-05 has both the declarative compound
   and a separate terminal sentence. If V-03 fails C-20 and V-05 passes, "terminal" is
   confirmed position-sensitive (opening declarative does not qualify). If V-03 passes
   C-20, the declarative compound satisfies C-20 regardless of sentence position.

3. **C-18 identity-form sensitivity** (V-04): Does "S-0 is the emit step and carries
   tier into S-2 and S-3" satisfy C-18's "explicit handoff sentence"? The identity
   first conjunct followed by a carrying second conjunct may or may not constitute an
   "explicit handoff sentence" per C-18's reading. If V-04 fails C-18 where V-03 passes
   it, the identity-predicate form is the differentiator.
