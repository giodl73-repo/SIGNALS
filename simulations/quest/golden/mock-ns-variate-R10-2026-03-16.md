---
skill: quest-variate
skill_target: mock-ns
round: 10
rubric_version: 10
rubric_target: C-31, C-32
date: 2026-03-16
---

# mock-ns -- Round 10 Variations (rubric v10, C-31 + C-32 target)

Rubric: v10 (C-01 through C-32, 5 essential / 3 recommended / 24 aspirational, max 128).

New criteria in v10 (extracted from R9 scoring):

- **C-31** -- Indicative-mood test: The declarative sentence in the two-sentence gate must
  use indicative present tense, not deontic/modal-obligation form. "This step must emit
  first" fails because "must" prescribes a behavioral norm rather than asserting the
  step's structural role; the sentence is a requirement-imposition, not a role-declaration.
  Deontic form simultaneously fails C-25 (prescribes, does not assert role) and C-28
  (modal-obligation is not indicative role-assertion). One modal word triggers three
  criterion failures.

- **C-32** -- Structural-independence test: C-18 (explicit handoff, any position) and C-20
  (standalone terminal sentence, closing position) are independent requirements that cannot
  be satisfied by the same sentence when that sentence is the gate opener. A compound-
  predicate opening declarative encoding tier-carry satisfies C-18 but not C-20; C-20
  requires a separate standalone sentence in terminal position of S-0, after the resolution
  logic. When C-20 fails from this structural choice, C-32 co-fails.

R9 evidence sources:

- R9 V-01 (128/128): "S-0 is the emit step." -- identity predicate, indicative, step as
  direct nominative subject. C-31 PASS (no modal). C-32 PASS (standalone terminal sentence
  present and independent). Confirmed 128/128 under v10.
- R9 V-02 (122/128): "This step must emit first." -- deontic modal. C-25 FAIL + C-28 FAIL
  + C-31 FAIL from single word "must." Three criteria, one cause. Confirmed C-31 boundary.
- R9 V-03 (124/128): "This step emits first and carries tier into S-2 and S-3." (no
  terminal sentence) -- C-20 FAIL + C-32 FAIL. The compound declarative opener satisfies
  C-18 but the standalone terminal sentence was removed; C-20 and C-32 co-fail.
- R9 V-04 (124/128): "S-0 is the emit step and carries tier into S-2 and S-3." (no
  terminal sentence) -- same structural failure as V-03: C-20 + C-32 co-fail.
- R9 V-05 (128/128): "This step emits first and carries tier into S-2 and S-3." + standalone
  terminal sentence -- dual-register form: compound opener satisfies C-18; terminal sentence
  satisfies C-20 independently; C-32 PASS.

Confirmed baseline for R10 (any of: R9 V-01 form, R9 V-05 form):
  -- Identity predicate: "S-0 is the emit step."
  -- Action form: "This step emits first [and carries tier into S-2 and S-3]."
  -- Both with standalone terminal: "Carry the resolved tier into S-2 and S-3 before any
     further action."

Unexplored territory entering R10:

With C-31 confirmed (deontic "must" / "shall" / "should" are failure modes), and C-32
confirmed (compound-opener cannot collapse C-18+C-20 into one sentence), the remaining
unexplored declarative failure modes center on:

1. SYNTACTIC VOICE: passive construction ("is emitted by this step") -- step as by-agent
   rather than grammatical subject; tests C-28/C-30 boundary (C-30 targets active voice
   specifically; passive may pass C-30 while failing C-28).

2. PREDICTIVE FUTURE ("will emit"): "will" is not listed in C-31's deontic enumeration
   (must/shall/should/is required to); the C-31 test ("replace modal with simple present;
   does it transform from norm to fact?") is ambiguous for predictive "will." Tests whether
   C-31 catches predictive future or treats it as indicative-equivalent.

3. GERUNDIVE-SUBJECT ("Emitting first is..."): gerund phrase in nominative subject position.
   Step is absent from subject NP; appears only as genitive modifier in predicate. New C-29
   failure mode distinct from R8 V-02's possessive-nominal "This step's defining action is..."

4. REVERSED SENTENCE ORDER (imperative first): "Write the TOPICS.md status line before any
   other work begins. S-0 is the emit step." Tests whether C-25's numbered structure
   "(1) declarative, (2) imperative" implies ordering constraint, or merely requires both
   types to be present.

5. CLEFT EXTRAPOSITION ("It is this step that..."): dummy expletive subject "It" with
   focused NP "this step." Tests C-28/C-29 boundary: the step appears as focused
   constituent but "It" is the formal grammatical subject; C-29 substitution test fails
   because "It" refers to an abstract proposition, not to the step directly.

Variation axes for R10 (three single-axis + two probing new structural modes):

1. **Passive-voice declarative** (V-01) -- "The TOPICS.md status line is emitted first by
   this step." Step as passive by-agent, artifact as nominative subject. C-28: step is not
   grammatical subject -- FAIL. C-30: artifact in nominative position -- but C-30 specifies
   "in active voice"; passive clause may PASS C-30 on a strict reading.

2. **Predictive-future modal ("will")** (V-02) -- "This step will emit first." "Will" not
   in C-31's deontic list. C-31 test: replace "will" with simple present -- "This step
   emits first" -- is the transformation from norm to fact? For predictive "will," the
   transformation yields a fact, suggesting the original may be predictive-indicative rather
   than deontic. Key discrimination: does C-31 treat "will" as deontic or indicative?

3. **Gerundive-nominative declarative** (V-03) -- "Emitting first is this step's defining
   action." Gerund phrase "Emitting first" as grammatical subject; "this step" as genitive
   modifier in predicate. New C-29 failure mode distinct from possessive-nominal. C-28:
   step not as agent of its own emission action -- FAIL. C-29: step not as direct nominative
   head of subject NP -- FAIL.

4. **Reversed sentence order** (V-04) -- Imperative sentence first, then declarative:
   "Write the TOPICS.md status line before any other work begins. S-0 is the emit step."
   Tests whether C-25's numbered structure "(1) declarative, (2) imperative" requires this
   ordering, or accepts both sentence types in any order.

5. **Cleft-extraposition declarative** (V-05) -- "It is this step that emits first."
   Dummy expletive "It" as formal grammatical subject; "this step" as focused NP in
   extraposition. C-29 substitution test: replace subject NP with "It" -- refers to the
   abstract proposition, not to the step itself. C-28: step is not grammatical subject
   of the main clause.

---

## V-01 -- Passive-Voice Declarative

**Axis:** Voice -- passive ("is emitted by this step") vs active ("emits first")

**Hypothesis:** "The TOPICS.md status line is emitted first by this step" places the
artifact (TOPICS.md status line) as the nominative grammatical subject; the step appears
as the oblique by-agent ("by this step"). C-28 requires "the step as grammatical subject
of its own emission action" -- the step is not the grammatical subject here (it is the
passive agent), so C-28 FAILS. C-30 requires "the declarative sentence must not promote
an output artifact to nominative subject position in active voice" -- the criterion
explicitly qualifies "in active voice." The passive construction places the artifact in
nominative subject position but uses passive, not active, voice. On a strict reading of
C-30's "active voice" qualifier, C-30 PASSES. C-29: the grammatical subject NP head is
"status line" (the artifact), not the step -- FAIL. C-25: the sentence asserts an
output-position claim ("artifact is emitted first by step"), not a role-declaration about
the step's nature in the pipeline -- C-25 may also FAIL on role-assertion grounds.

Predicted score: C-25 FAIL (-2), C-28 FAIL (-2), C-29 FAIL (-2). C-30 PASS (passive, not
active). C-31 PASS (indicative passive, no modal). Score: 122/128. Alternate prediction if
C-25 passes on content grounds: 124/128 (C-28 FAIL + C-29 FAIL only).

The key discriminator: does C-30's "in active voice" qualifier create a gap that passive
constructions escape? If yes, passive artifact-as-subject becomes a rubric blind spot --
the artifact is in nominative position but C-30 does not fire, and only C-28/C-29 catch
the failure.

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

The TOPICS.md status line is emitted first by this step. Write the TOPICS.md status line
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

## V-02 -- Predictive-Future Modal ("will")

**Axis:** Modal type -- predictive future ("will emit") vs deontic obligation ("must emit")
vs indicative fact ("emits first")

**Hypothesis:** "This step will emit first" uses "will" as a future modal. C-31's enumerated
deontic list is: "must," "shall," "should," "is required to." "Will" is absent from this
list. The C-31 discrimination test: "replace the modal with simple present indicative -- if
this transforms the sentence from a norm ('must emit' = 'the step is required to emit') to
a statement of fact ('emits' = 'the step emits'), the original was deontic." For "will emit":
replacement yields "This step emits first" -- a statement of fact. For "must emit": the same
replacement also yields "This step emits first." The substitution test produces the same
outcome for both predictive "will" and deontic "must"; it does not discriminate between them.

The key question: is "will" in "This step will emit first" deontic (obligation) or predictive
(temporal assertion about future state)? "Will" in English is primarily predictive-future; it
does not carry strong deontic loading in present-context statements about step behavior. The
sentence reads as a factual prediction: this step is going to emit first. Not as an
obligation: this step is required to emit first.

C-25 requires "a declarative identity sentence asserting the step's emit primacy as a
statement of the step's ROLE." "This step will emit first" asserts the step's future behavior;
this is a role-assertion about what the step does, expressed in predictive form. C-28: "This
step" is the grammatical subject; "will emit first" is the predicate (step as agent of
emission). C-29: "This step" is the direct nominative head. C-30: no artifact in subject
position. C-31: "will" is not in the deontic list.

Predicted score (predictive-indicative reading): 128/128. All criteria PASS.
Alternate prediction (deontic reading of "will"): C-25 FAIL + C-28 FAIL + C-31 FAIL = 122/128.
This variation is a genuine boundary test. The outcome will either (a) confirm that "will" is
outside C-31's scope and 128/128 is achievable with predictive future, or (b) require a
rubric note clarifying that "will" must also be avoided when asserting step role.

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

This step will emit first. Write the TOPICS.md status line before any other work begins.

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

## V-03 -- Gerundive-Nominative Declarative

**Axis:** Subject form -- gerundive phrase as nominative ("Emitting first is...") vs direct
step reference ("This step emits first" / "S-0 is the emit step")

**Hypothesis:** "Emitting first is this step's defining action" places a gerund phrase
("Emitting first") as the grammatical subject. "This step" appears only as the genitive
modifier within the predicate noun phrase ("this step's defining action"). C-29 requires
"the step as direct nominative head of the subject noun phrase." The subject NP head is
"Emitting" (a gerundive nominalization), not "this step." FAIL C-29. C-29 substitution
test: replace the subject NP with "It" -- "It is this step's defining action" -- "It"
refers to the gerundive action (emitting first), not to the step itself. FAIL.

This is a new gerundive-subject failure mode distinct from R8 V-02's possessive-nominal
form ("This step's defining action is to emit first"). In R8 V-02: the nominalization
"defining action" is the subject and "This step" is a possessive modifier of the subject.
In V-03 here: the gerundive action "Emitting first" is the subject and "this step" has
moved to the predicate as a possessive modifier of "defining action." Both constructions
demote the step, but through different syntactic paths -- both should fail C-29.

C-28 requires "the step as grammatical subject of its own emission action." The gerundive
"Emitting first" is the subject and "is" is the copula; the step does not appear as the
agent performing emission in subject position. FAIL C-28.

C-25: the sentence does assert a role relationship -- emitting first is identified as this
step's defining action. The role-assertion content is present, but the step is syntactically
demoted from subject. C-25 may pass on a content-reading (role assertion is present
somewhere in the sentence) while C-28 and C-29 fail on grammatical-structure tests.

C-30 PASS: no output artifact (like TOPICS.md status line) in subject position -- the
gerundive "Emitting first" is an action, not an artifact. C-31 PASS: copula "is" is
indicative, no modal of obligation.

Predicted: C-28 FAIL (-2), C-29 FAIL (-2). Score: 124/128 (if C-25 passes on content
grounds) or 122/128 (if C-25 also fails because the step is demoted from agent position).

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

Emitting first is this step's defining action. Write the TOPICS.md status line before any
other work begins.

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

## V-04 -- Reversed Sentence Order (Imperative First)

**Axis:** Internal gate sentence order -- imperative first, declarative second vs (C-25
standard) declarative first, imperative second

**Hypothesis:** "Write the TOPICS.md status line before any other work begins. S-0 is the
emit step." places the imperative instruction first and the declarative identity sentence
second -- the reverse of C-25's numbered structure. C-25 pass condition: "(1) a declarative
identity sentence asserting the step's emit primacy... and (2) an imperative instruction
naming what must be emitted and when... Both sentences must be present at S-0 opening."

The "(1)" and "(2)" numbering implies ordering: declarative must be sentence 1, imperative
must be sentence 2. In V-04, sentence 1 is the imperative and sentence 2 is the declarative.
If C-25 requires this specific ordering, the reversed form FAILS C-25 even though both
required sentence types are present.

C-23 says the "preamble gate" appears as "the absolute first sentence in the S-0 step body."
C-23's discriminator note: "V-01 (R6) uses single-imperative form at S-0 opening -- passes
C-23, fails C-25." This demonstrates that C-23 is satisfied by ANY sentence as the gate
opener (it requires the gate construct to be first in S-0, not that the declarative must
be the opening sentence within the gate). In V-04: C-23 PASS (the gate construct occupies
the S-0 opening; no pre-gate surface area). C-25: ordering violated -- imperative before
declarative. FAIL C-25 if ordering is required. PASS C-25 if ordering is type-only.

C-27 PASS: count-strict exactly 2 sentences -- still 2 in reversed order.
C-28: the declarative sentence IS "S-0 is the emit step" -- identity predicate, step as
grammatical subject. PASS on the declarative sentence form itself.
C-29 PASS: "S-0" is the direct nominative head of the declarative's subject NP.
C-30 PASS: no artifact in subject position. C-31 PASS: indicative copula, no modal.

Predicted: C-25 FAIL (-2) if ordering is enforced. Score: 126/128.
Alternate prediction if C-25 is type-only (not order-sensitive): 128/128.

The outcome resolves whether C-25's "(1)...(2)..." structure is a strict ordering
requirement or merely a structural description of the two types that must be present.
If ordering is not enforced, a reversed gate is a valid passing form and the rubric needs
a clarification note.

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

Write the TOPICS.md status line before any other work begins. S-0 is the emit step.

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

## V-05 -- Cleft-Extraposition Declarative

**Axis:** Subject form -- cleft extraposition ("It is this step that...") vs direct
nominative ("This step emits first" / "S-0 is the emit step")

**Hypothesis:** "It is this step that emits first" is a cleft sentence. In cleft structure:
"It" is the dummy expletive (formal grammatical subject of the main clause), "is" is the
copula, "this step" is the focused NP (extraposed subject), and "that emits first" is the
relative clause identifying the referent. "This step" is not the grammatical subject of
the main clause -- "It" holds that position.

C-29 substitution test: "replace the subject noun phrase with 'It.'" The subject NP is
already "It." The test asks whether "It" refers to the step itself or to an abstraction.
In the cleft, "It" is an expletive (dummy pronoun) that refers forward to the entire
proposition "this step that emits first" -- it does not refer to the step directly.
FAIL C-29.

C-28: "the step as grammatical subject of its own emission action." "This step" is the
subject of "emits first" in the relative clause ("that emits first"), so the step IS the
logical agent of the emission within the embedded clause. But the main clause subject is
"It" (expletive). C-28 requires the step as grammatical subject at the sentence level, not
only at the embedded clause level. FAIL C-28 on a strict grammatical-subject reading.

Alternate C-28 reading: if "grammatical subject" is interpreted as the logical subject
(the agent of the emission predicate), then "this step" is the logical subject of
"emits first" in the relative clause. PASS C-28 on a semantic-subject interpretation.
The outcome depends on whether C-28 is read syntactically (surface subject of main
clause) or semantically (logical agent of emission).

C-25: the cleft construction is an identity assertion ("the thing that emits first is this
step"). It does assert the step's role as the emitter. C-25 PASS on content grounds.

C-30 PASS: no output artifact (like TOPICS.md status line) in nominative position.
C-31 PASS: copula "is" is indicative, no modal of obligation. C-27 PASS: exactly 2
sentences.

Predicted: C-29 FAIL (-2). C-28 uncertain: FAIL on syntactic reading (-2) or PASS on
semantic reading. Score: 124/128 (strict: C-28 + C-29 fail) or 126/128 (semantic: C-29
fail only).

The outcome determines whether C-28's "grammatical subject" test is syntactic-surface
or semantic-logical. If syntactic-surface only: cleft form fails C-28 + C-29. If semantic:
cleft form only fails C-29. A rubric note distinguishing these two readings may be needed.

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

It is this step that emits first. Write the TOPICS.md status line before any other work
begins.

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

## Predicted Score Summary

| Variation | Gate Declarative                                              | Key Axis                | Predicted Failures             | Predicted Score |
|-----------|---------------------------------------------------------------|-------------------------|--------------------------------|-----------------|
| V-01      | The TOPICS.md status line is emitted first by this step.      | Passive voice           | C-25?, C-28, C-29              | 122-124/128     |
| V-02      | This step will emit first.                                    | Predictive future "will" | None OR C-25 + C-28 + C-31    | 122 or 128/128  |
| V-03      | Emitting first is this step's defining action.                | Gerundive-nominative    | C-28, C-29                     | 122-124/128     |
| V-04      | Write the TOPICS.md status line ... S-0 is the emit step.     | Reversed sentence order | C-25 (ordering)                | 126/128         |
| V-05      | It is this step that emits first.                             | Cleft extraposition     | C-29, C-28?                    | 124-126/128     |

Key open questions resolved by scoring:

1. **V-01 -- passive gap in C-30**: Does C-30's "in active voice" qualifier create a gap
   that passive constructions escape? If yes, passive artifact-as-subject becomes a rubric
   blind spot -- the artifact is in nominative position but C-30 does not fire. Only
   C-28/C-29 catch the failure. A rubric C-30 note may be needed: "active voice is the
   primary form; passive constructions placing an artifact as subject fail C-28 directly
   and need not additionally fail C-30."

2. **V-02 -- predictive "will" vs deontic list**: Is "will" deontic or predictive-indicative
   under C-31? The deontic list does not include "will." If C-31 is list-strict, V-02 passes
   128/128; if C-31's substitution test treats predictive "will" as obligation-equivalent,
   V-02 fails C-25 + C-28 + C-31. A rubric note either way: either add "will" to the safe
   list (indicative-equivalent) or add it to the deontic list.

3. **V-03 -- C-25 content vs syntax split**: Does C-25 pass when role-assertion content is
   present but the step is syntactically demoted to genitive modifier? The rubric's C-25/C-28
   split (C-25 = content check, C-28 = syntax check) suggests C-25 can pass independently.
   If gerundive-subject passes C-25 on content grounds, V-03 scores 124; if C-25 also
   requires the step as subject, V-03 scores 122.

4. **V-04 -- C-25 ordering vs type-only**: Does C-25's numbered structure "(1) declarative,
   (2) imperative" enforce sentence ordering, or just require both types? If ordering is
   required: V-04 fails C-25 = 126/128. If type-only: V-04 passes C-25 = 128/128 and
   reversed-order is a valid gate form. Rubric should clarify.

5. **V-05 -- C-28 syntactic vs semantic subject**: Does C-28's "grammatical subject" mean
   the surface syntactic subject of the main clause ("It" in the cleft) or the logical
   agent of the emission predicate ("this step" in the relative clause)? If syntactic:
   cleft fails C-28 + C-29 = 124/128. If semantic: cleft fails C-29 only = 126/128. Rubric
   may need a C-28 note explicitly ruling on cleft constructions.
