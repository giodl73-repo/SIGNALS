---
skill: quest-variate
skill_target: mock-ns
round: 11
rubric_version: 11
rubric_target: C-33, C-34
date: 2026-03-16
---

# mock-ns -- Round 11 Variations (rubric v11, C-33 + C-34 target)

Rubric: v11 (C-01 through C-34, 5 essential / 3 recommended / 26 aspirational, max 132).

New criteria in v11 (extracted from R10 scoring):

- **C-33** -- Passive artifact-as-subject: The declarative sentence must not place an
  output artifact as grammatical subject in a passive construction. "The TOPICS.md status
  line is emitted first by this step" places the artifact as passive grammatical subject;
  the step appears only as the by-agent. C-30's "in active voice" qualifier does not fire
  on passive constructions; C-33 closes that gap. Four-criterion failure chain: C-25,
  C-28, C-29, C-33.

- **C-34** -- Gerundive-as-subject: The declarative sentence must not promote a gerundive
  action-nominalization to grammatical subject position. "Emitting first is this step's
  defining action" promotes the gerundive "Emitting first" to nominative subject; the step
  is relegated to predicate-possessive "this step's." C-28 and C-29 catch this
  independently; C-34 names it as a distinct fifth declarative failure mode. Three-
  criterion failure chain: C-28, C-29, C-34.

R10 evidence sources (retroactive v11 scores):

- R10 V-01 (120/132): "The TOPICS.md status line is emitted first by this step." Passive
  artifact-as-subject. C-33 fires; C-25, C-28, C-29 co-fail.
- R10 V-02 (132/132): "This step will emit first." Predictive future, step as direct
  nominative. C-33 PASS (not passive), C-34 PASS (no gerundive subject).
- R10 V-03 (126/132): "Emitting first is this step's defining action." Gerundive subject.
  C-34 fires; C-28, C-29 co-fail.
- R10 V-04 (130/132): Reversed order. Only C-25 fails (ordering violation). C-33 PASS,
  C-34 PASS.
- R10 V-05 (124/132): Cleft extraposition. C-28, C-29 fail; C-33 PASS, C-34 PASS.

Confirmed baseline for R11 (any of):
  "This step will emit first."            -- R10 champion (132/132 under v11)
  "S-0 is the emit step."                 -- R9 champion (132/132 under v11)
  "This step emits first."                -- R8 champion form (132/132 under v11)

Open questions from R10/v11 to investigate in R11:

| Question | Target variation |
|----------|-----------------|
| Does C-33 fire for ACTIVE artifact-as-subject, or is C-33 passive-only? | V-01 |
| Do C-28/C-29 fail for wh-cleft with step as embedded agent? | V-02 |
| Does C-34 fire for infinitival subject, or only for gerundive? | V-03 |
| Does C-29 fail when step identifier appears as appositive (not NP head)? | V-04 |
| Can a transitive-object construction achieve 132/132 with explicit artifact naming? | V-05 |

Variation axes for R11 (three single-axis + two combined):

1. **Active artifact-as-subject** (V-01) -- "TOPICS.md is the first artifact this step
   emits"; active-voice artifact nominative; confirms C-33 passive-only scope vs C-30

2. **Wh-cleft with embedded step** (V-02) -- "What S-0 emits first is the TOPICS.md
   status line"; step is logical agent inside a nominalized free relative clause; tests
   C-28/C-29 syntactic-surface threshold; C-34 boundary (wh-nominalization vs gerundive)

3. **Infinitival subject** (V-03) -- "To emit the TOPICS.md status line first is this
   step's role"; infinitival action-nominalization as subject; tests C-34 scope:
   gerundive-specific vs action-nominalization-general

4. **Appositional step identifier** (V-04) -- "The emit step, S-0, runs before all other
   steps produce any output"; common-noun NP head with step identifier as appositive;
   tests C-29's direct-nominative-head requirement

5. **Transitive-object confirmed positive** (V-05) -- "S-0 emits the TOPICS.md status
   line before any other output"; step as direct nominative subject, artifact as
   transitive direct object; predicted 132/132

---

## V-01 -- Active artifact-as-subject

**Axis:** C-30 vs C-33 scope: active-voice artifact nominative (C-30 detector) vs passive
artifact nominative (C-33 detector). Confirms the two criteria are non-overlapping.
**Hypothesis:** C-30 fires (artifact in active nominative), C-28 fails (step not
grammatical subject), C-25 fails (assertion about artifact property, not step role).
C-33 does NOT fire (active voice, not passive). Expected score: 124/132.

```
---
name: mock-ns
description: Mock artifact for a single namespace with category annotation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- EMIT TOPICS.MD STATUS LINE

TOPICS.md is the first artifact this step emits.
Write the status line before any other output begins.

Read TOPICS.md now. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Carry the resolved tier value into S-1. Do not re-read TOPICS.md in any later step.

Do not begin S-1 until the TOPICS.md status line is written.

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-3:CS]   | S-3  | Cross-site reference row    | [A-1:FC]     | forward --> names A-1        |
  | [A-1:FC]   | A-1  | Failure consequence row     | [S-3:CS]     | <-- backward, names S-3      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above.

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (use the pre-filled table block at the
             current use site; fill in the Match field only).
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

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

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability chain:

  | Protection layer        | Rule                                                      |
  |-------------------------|-----------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run          |
  | Affirmative closure     | Every execution path that reaches A-1 carries this value  |
  | No-exemption            | No path is exempt                                         |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1.             |
  | before writing this row | Phase 2 (Steps 2a-2d): assert match; emit record.         |
  | (P-0 table, row 1)      | DO NOT WRITE until Steps 2a-2d complete.                  |
  | Cross-site ref [S-3:CS] | Failure produces silent mismatch at [A-1:FC].             |

Confirmation record:
  | Token    | [S-3:CS]                   |
  | Step     | S-3                        |
  | Row type | Cross-site reference row   |
  | Match    | _______________            |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain:

  | Protection layer        | Rule                                                      |
  |-------------------------|-----------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.          |
  | Priority                | Applies before any other instruction in this step         |
  | No-exemption            | No instruction in this step is exempt                     |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2.             |
  | before writing this row | Phase 2 (Steps 2a-2d): assert match; emit record.         |
  | (P-0 table, row 2)      | DO NOT WRITE until Steps 2a-2d complete.                  |
  | Failure conseq [A-1:FC] | Re-deriving FLAG silently corrupts the artifact trust tier.|

Confirmation record:
  | Token    | [A-1:FC]                   |
  | Step     | A-1                        |
  | Row type | Failure consequence row    |
  | Match    | _______________            |

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body, before any mock
content, separated from header and body with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific
    claims may be partially accurate or partially fabricated. Review for
    plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

**V-01 gate analysis:**

Sentence 1: "TOPICS.md is the first artifact this step emits."
- Subject: "TOPICS.md" (artifact as active nominative)
- Construction: active-voice copular with relative-clause predicate nominal
- C-25: Sentence asserts a property of the artifact (being first), not the step's role.
  The step appears only inside the relative clause "this step emits" -- as agent of the
  embedded verb, not as main-clause subject. Not a step role-assertion. FAIL.
- C-28: Grammatical subject is "TOPICS.md." Step appears as embedded agent. FAIL.
- C-29: Substitution -- replace "TOPICS.md" with "It" -> "It is the first artifact this
  step emits." "It" refers to the artifact. Step is not nominative head. FAIL.
- C-30: Artifact in nominative position in active voice. FAIL.
- C-33: Active-voice construction. C-33 targets passive constructions specifically. PASS.
  This is the key test: C-33 does NOT fire for active-voice artifact nominative.
- C-34: No gerundive subject. PASS.

**Score: 132 - 2(C-25) - 2(C-28) - 2(C-29) - 2(C-30) = 124/132. C-33 PASS.**

Key finding: C-30 and C-33 are non-overlapping detectors. C-30 fires for active artifact
nominative; C-33 fires for passive artifact nominative. The same displacement pattern
(artifact usurps subject position) triggers different criteria depending on voice. A
perfect complement: no active-artifact form escapes C-30, no passive-artifact form escapes
C-33.

---

## V-02 -- Wh-cleft with embedded step

**Axis:** Wh-cleft construction; step as logical agent inside nominalized free relative
clause; artifact as predicate nominal (not subject). Tests C-28/C-29 syntactic-surface
threshold and C-34 boundary (wh-nominalization vs gerundive).
**Hypothesis:** C-28 fails (wh-clause is grammatical subject, not S-0). C-29 fails
(NP head is "What", not S-0). C-25 passes (content is a role-assertion, C-25 is content-
based). C-30 passes (artifact is predicate nominal, not active nominative). C-33 passes
(not passive). C-34 is an open question (wh-nominalization is not gerundive morphologically).
Expected score: 128/132 (if C-34 is gerundive-specific) or 126/132 (if C-34 fires).

```
---
name: mock-ns
description: Mock artifact for a single namespace with category annotation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- EMIT TOPICS.MD STATUS LINE

What S-0 emits first is the TOPICS.md status line.
Write it before any other output begins.

Read TOPICS.md now. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Carry the resolved tier value into S-1. Do not re-read TOPICS.md in any later step.

Do not begin S-1 until the TOPICS.md status line is written.

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

[identical to V-01 P-0 through A-5]
```

*(Full steps P-0 through A-5 identical to V-01; each variation is complete and runnable.)*

**V-02 gate analysis:**

Sentence 1: "What S-0 emits first is the TOPICS.md status line."
- Construction: wh-cleft (pseudo-cleft). Subject = "What S-0 emits first" (free relative
  clause). Predicate = "is the TOPICS.md status line" (copular + predicate nominal).
- C-25: Content reading -- the sentence asserts what S-0's first output is, identifying
  S-0 as the first emitter. This is a declarative role-assertion in cleft form. C-25 is
  content-based (confirmed by R9 V-01: identity-predicate cleft passed C-25 on content).
  PASS.
- C-28: Main-clause grammatical subject is "What S-0 emits first" (nominalized free
  relative). S-0 appears inside the relative clause as the agent of "emits first" -- it is
  the logical agent but not the main-clause grammatical subject. C-28 is a syntactic-
  surface test (confirmed R10 V-05 cleft analysis). FAIL.
- C-29: Substitution -- replace "What S-0 emits first" with "It" -> "It is the TOPICS.md
  status line." "It" refers to the action-content (the thing first emitted), not to S-0.
  S-0 is not the direct nominative head. FAIL.
- C-30: "TOPICS.md status line" is the predicate nominal (postcopular position), not the
  subject. C-30's "nominative position" = subject position. PASS.
- C-33: Active-voice wh-cleft, not a passive construction. PASS.
- C-34: KEY QUESTION. "What S-0 emits first" is a nominalized free relative clause, not
  a gerundive ("-ing" nominalization). The subject contains an action (emits) but the
  nominalizer is the wh-word "What," not a gerundive morpheme. C-34 is defined as
  "gerundive-as-subject" with source example "Emitting first is this step's defining
  action." If C-34 is gerundive-morpheme-specific, it does NOT fire here. If C-34 is
  action-nominalization-general, it may fire. The rubric text "gerundive-as-subject"
  implies morpheme specificity; wh-clefts use a different nominalization mechanism.
  Predicted: PASS (C-34 is gerundive-specific).

**Score: 132 - 2(C-28) - 2(C-29) = 128/132 if C-34 PASS; 126/132 if C-34 fires.**

Key finding: if score is 128/132, C-34 is confirmed gerundive-specific. If 126/132, the
rubric requires a discriminator note distinguishing gerundive-specific and nominalization-
general scope, or a new criterion for wh-nominalization displacement.

---

## V-03 -- Infinitival subject (C-34 boundary)

**Axis:** C-34 scope: gerundive-specific vs action-nominalization-general; infinitival
subject as minimal morphological contrast to gerundive.
**Hypothesis:** "To emit first" is an infinitival action-nominalization; "Emitting first"
is a gerundive action-nominalization. Both displace the step from subject position. C-34
names the gerundive case explicitly. If C-34 is gerundive-specific, infinitival form
produces C-28 + C-29 failures only (128/132). If C-34 is nominalization-general, it
co-fires (126/132). A new C-35 criterion may be warranted if 128/132.

```
---
name: mock-ns
description: Mock artifact for a single namespace with category annotation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- EMIT TOPICS.MD STATUS LINE

To emit the TOPICS.md status line first is this step's role.
Write it before any other output begins.

Read TOPICS.md now. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Carry the resolved tier value into S-1. Do not re-read TOPICS.md in any later step.

Do not begin S-1 until the TOPICS.md status line is written.

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

[identical to V-01 P-0 through A-5]
```

*(Full steps P-0 through A-5 identical to V-01.)*

**V-03 gate analysis:**

Sentence 1: "To emit the TOPICS.md status line first is this step's role."
- Construction: infinitival subject. Subject = "To emit the TOPICS.md status line first"
  (infinitive clause). Predicate = "is this step's role" (copular + genitive-possessive
  predicate nominal).
- C-25: Content: the sentence explicitly identifies the step's role (emitting first). This
  is a declarative role-assertion. PASS on content grounds.
- C-28: Grammatical subject is "To emit the TOPICS.md status line first" (infinitive
  clause). The step appears only as genitive modifier "this step's" inside the predicate.
  The step is not the grammatical subject performing the action -- the infinitive clause is.
  FAIL.
- C-29: Substitution -- replace "To emit the TOPICS.md status line first" with "It" ->
  "It is this step's role." "It" refers to the infinitive action (emitting), not to the
  step. FAIL.
- C-30: "TOPICS.md status line" is inside the infinitive clause as the object of "emit,"
  not the main-clause subject. PASS.
- C-33: Not a passive construction. PASS.
- C-34: KEY DISCRIMINATOR. C-34 names "gerundive-as-subject" with source example
  "Emitting first is this step's defining action." The infinitive "To emit first" is a
  distinct morphological form from the gerundive "Emitting first." Both are action-
  nominalizations; both displace the step to genitive-predicate. Two possible outcomes:
    - C-34 PASS (gerundive-specific): Score 128/132. If so, a new C-35 may be warranted
      to name the infinitival-subject displacement pattern explicitly, or a rubric note
      extending C-34's scope.
    - C-34 FAIL (nominalization-general): Score 126/132. If so, C-34's description should
      be updated to read "action-nominalization-as-subject" with both gerundive and
      infinitival forms as named examples.

**Score: 128/132 (C-34 gerundive-specific) or 126/132 (C-34 nominalization-general).**

---

## V-04 -- Appositional step identifier (combined axis: C-29 + C-28)

**Axis:** C-29 identifier-strict vs referential; appositional step name "S-0" as
non-head constituent of subject NP.
**Hypothesis:** "The emit step, S-0" -- NP head is "step" (common noun modified by "emit"
as pre-nominal adjective); "S-0" is an appositive renaming constituent, not the NP head.
C-29 substitution test: "It runs before all other steps produce any output" -- "It" refers
to the emit step, which IS S-0. The referent is the step. C-28: the subject (emit step)
is performing the action (running first). Expected: C-29 is the ambiguous criterion; C-28
likely passes. Score: 130/132 (C-29 identifier-strict) or 132/132 (C-29 referential).

```
---
name: mock-ns
description: Mock artifact for a single namespace with category annotation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- EMIT TOPICS.MD STATUS LINE

The emit step, S-0, runs before all other steps produce any output.
Write the TOPICS.md status line now.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Carry the resolved tier value into S-1. Do not re-read TOPICS.md in any later step.

Do not begin S-1 until the TOPICS.md status line is written.

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

[identical to V-01 P-0 through A-5]
```

*(Full steps P-0 through A-5 identical to V-01.)*

**V-04 gate analysis:**

Sentence 1: "The emit step, S-0, runs before all other steps produce any output."
- Construction: NP subject with parenthetical appositive. Subject NP = "The emit step,
  S-0" (head: "step," determiner: "The," pre-nominal adjective: "emit," appositive: "S-0").
  Predicate = "runs before all other steps produce any output."
- C-25: Declarative, step in subject position, role-assertion (temporal ordering). PASS.
- C-28: The NP "The emit step, S-0" is the grammatical subject and is performing the
  action "runs before all other steps." The referent is S-0 (via apposition). C-28 tests
  whether the step is the grammatical subject performing the emission action. The subject
  performs the running-first action -- which IS the emission role. PASS.
- C-29: KEY DISCRIMINATOR. Substitution -- replace "The emit step, S-0" with "It" ->
  "It runs before all other steps produce any output." C-29's substitution test asks:
  does "It" refer to an abstraction derived from the step, or to the step itself? "It"
  refers to the emit step (= S-0 directly via apposition). The referent is the step,
  not an abstraction derived from it. However, the NP HEAD is "step" (a common noun),
  not "S-0" (the identifier). C-29 was introduced (R8/R9) to catch possessive-nominal
  displacement ("This step's defining action" -- step demoted to genitive). The appositive
  construction does not demote the step to genitive; "S-0" appears in the same NP as the
  head. Two readings:
    - FAIL (identifier-strict): C-29 requires the step identifier to be the direct NP
      head. "step" is the head; "S-0" is merely an appositive. Score: 130/132.
    - PASS (referential): The subject NP unambiguously refers to S-0 (the appositive
      makes the identity explicit); the substitution test "It" refers to S-0 directly.
      Score: 132/132.
  The rubric's history favors the stricter reading (each criterion was introduced to close
  a specific gap). The appositive is a new construction not seen in prior rounds; both
  interpretations are defensible without a rubric note.
- C-30: "TOPICS.md status line" does not appear in the gate sentence. PASS.
- C-33: Not passive. PASS.
- C-34: No gerundive subject. PASS.

**Score: 130/132 (C-29 identifier-strict) or 132/132 (C-29 referential).**

Key finding: if 130/132, a rubric discriminator note for C-29 is warranted clarifying
that appositional step identifiers are not sufficient -- the identifier must be the
direct NP head. If 132/132, C-29 is confirmed referential and the identifier-head
pattern is confirmed as best-practice but not strictly required.

---

## V-05 -- Transitive-object confirmed positive

**Axis:** Constructive confirmation -- step as direct nominative subject, artifact as
transitive direct object. C-30 and C-33 simultaneously satisfied by placing artifact in
object position (not subject position, not passive subject position). Predicted 132/132.
**Hypothesis:** The transitive-object construction is the canonical safe pattern for
gates that name the artifact explicitly: subject = step identifier, verb = transitive
emission verb, object = artifact name. This satisfies C-30 (no active nominative artifact)
and C-33 (no passive nominative artifact) with the same move.

```
---
name: mock-ns
description: Mock artifact for a single namespace with category annotation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-0 -- EMIT TOPICS.MD STATUS LINE

S-0 emits the TOPICS.md status line before any other output.
Write it now.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Carry the resolved tier value into S-1. Do not re-read TOPICS.md in any later step.

Do not begin S-1 until the TOPICS.md status line is written.

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-3:CS]   | S-3  | Cross-site reference row    | [A-1:FC]     | forward --> names A-1        |
  | [A-1:FC]   | A-1  | Failure consequence row     | [S-3:CS]     | <-- backward, names S-3      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above.

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name and row type match current context.
    Step 2d: Emit confirmation record (fill in Match field only).
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

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

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability chain:

  | Protection layer        | Rule                                                      |
  |-------------------------|-----------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run          |
  | Affirmative closure     | Every execution path that reaches A-1 carries this value  |
  | No-exemption            | No path is exempt                                         |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1.             |
  | before writing this row | Phase 2 (Steps 2a-2d): assert match; emit record.         |
  | (P-0 table, row 1)      | DO NOT WRITE until Steps 2a-2d complete.                  |
  | Cross-site ref [S-3:CS] | Failure produces silent mismatch at [A-1:FC].             |

Confirmation record:
  | Token    | [S-3:CS]                   |
  | Step     | S-3                        |
  | Row type | Cross-site reference row   |
  | Match    | _______________            |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain:

  | Protection layer        | Rule                                                      |
  |-------------------------|-----------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.          |
  | Priority                | Applies before any other instruction in this step         |
  | No-exemption            | No instruction in this step is exempt                     |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2.             |
  | before writing this row | Phase 2 (Steps 2a-2d): assert match; emit record.         |
  | (P-0 table, row 2)      | DO NOT WRITE until Steps 2a-2d complete.                  |
  | Failure conseq [A-1:FC] | Re-deriving FLAG silently corrupts the artifact trust tier.|

Confirmation record:
  | Token    | [A-1:FC]                   |
  | Step     | A-1                        |
  | Row type | Failure consequence row    |
  | Match    | _______________            |

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body, before any mock
content, separated from header and body with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific
    claims may be partially accurate or partially fabricated. Review for
    plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

**V-05 gate analysis:**

Sentence 1: "S-0 emits the TOPICS.md status line before any other output."
- Construction: simple transitive declarative. Subject = "S-0" (step identifier as direct
  NP head). Verb = "emits" (transitive). Direct object = "the TOPICS.md status line."
  Temporal adjunct = "before any other output."
- C-25: "S-0" is the subject; sentence asserts S-0's role as first emitter. Declarative
  form. PASS.
- C-28: "S-0" is the grammatical subject performing the emission action. PASS.
- C-29: Substitution -- replace "S-0" with "It" -> "It emits the TOPICS.md status line
  before any other output." "It" refers directly to S-0. PASS.
- C-30: "TOPICS.md status line" is the direct object (not nominative position in active
  voice). PASS.
- C-31: "emits" is simple present indicative. No deontic modal. PASS.
- C-32: C-18 handoff and C-20 terminal are independent sentences downstream. PASS.
- C-33: Not a passive construction. Artifact is in object position. PASS.
- C-34: No gerundive subject. "S-0" is the grammatical subject. PASS.

**Score: 132/132.**

Structural principle confirmed: placing the artifact as transitive direct object is the
canonical safe form for gates that name the artifact explicitly. Subject = step identifier
(satisfies C-28, C-29). Object = artifact name (satisfies C-30 and C-33 simultaneously,
since neither active-nominative nor passive-nominative applies). Verb = active transitive
emission verb (satisfies C-31, avoids nominalization that would trigger C-34).

---

## Predicted Ranking

| Rank | Var | Gate declarative | Predicted | Failures |
|------|-----|-----------------|-----------|---------|
| 1 | V-05 | "S-0 emits the TOPICS.md status line before any other output." | **132/132** | none |
| 2 | V-04 (referential) | "The emit step, S-0, runs before all other steps produce any output." | **132/132** | none |
| 2 | V-04 (identifier-strict) | same | **130/132** | C-29 |
| 3 | V-02 (C-34 gerundive-specific) | "What S-0 emits first is the TOPICS.md status line." | **128/132** | C-28, C-29 |
| 3 | V-03 (C-34 gerundive-specific) | "To emit the TOPICS.md status line first is this step's role." | **128/132** | C-28, C-29 |
| 3 | V-03 (C-34 nominalization-general) | same | **126/132** | C-28, C-29, C-34 |
| 4 | V-02 (C-34 fires) | "What S-0 emits first is the TOPICS.md status line." | **126/132** | C-28, C-29, C-34 |
| 5 | V-01 | "TOPICS.md is the first artifact this step emits." | **124/132** | C-25, C-28, C-29, C-30 |

---

## Open Questions R11 Will Resolve

| Question | Resolution mechanism | Rubric consequence |
|----------|---------------------|--------------------|
| Is C-33 passive-only? | V-01: C-33 PASS (predicted), C-30 FAIL -- confirms non-overlapping scope | Rubric note: C-30 = active detector, C-33 = passive detector, same failure class |
| Does C-34 cover wh-nominalization? | V-02 score: 128 vs 126 -- C-34 PASS confirms gerundive-specific | If 126: extend C-34 description to "action-nominalization-as-subject" |
| Does C-34 cover infinitival subjects? | V-03 score: 128 vs 126 -- C-34 PASS confirms gerundive-specific | If 128: C-35 candidate for infinitival-subject displacement |
| Is C-29 identifier-strict or referential? | V-04 score: 130 vs 132 -- C-29 FAIL confirms identifier-strict | Rubric note: direct NP head must be the step identifier, not a common-noun referent with appositive |
| Is transitive-object form the canonical safe gate pattern? | V-05 score: 132/132 -- confirms the pattern | Design rule: artifact in object position satisfies C-30 + C-33 in one move |

---

```json
{
  "round": 11,
  "rubric_version": 11,
  "rubric_target": ["C-33", "C-34"],
  "max_score": 132,
  "variations": [
    {
      "id": "V-01",
      "axis": "Active artifact-as-subject (C-30 vs C-33 scope confirmation)",
      "gate_declarative": "TOPICS.md is the first artifact this step emits.",
      "predicted_score": 124,
      "predicted_failures": ["C-25", "C-28", "C-29", "C-30"],
      "c33_fires": false,
      "c34_fires": false,
      "key_hypothesis": "C-33 is passive-only; C-30 detects active-voice artifact-as-subject; the two criteria are non-overlapping"
    },
    {
      "id": "V-02",
      "axis": "Wh-cleft with embedded step (C-28/C-29 threshold + C-34 boundary)",
      "gate_declarative": "What S-0 emits first is the TOPICS.md status line.",
      "predicted_score_lower": 126,
      "predicted_score_upper": 128,
      "predicted_failures_certain": ["C-28", "C-29"],
      "predicted_failures_ambiguous": ["C-34"],
      "c33_fires": false,
      "key_hypothesis": "C-34 is gerundive-specific (score 128); wh-nominalization is not gerundive"
    },
    {
      "id": "V-03",
      "axis": "Infinitival subject (C-34 gerundive-specific vs nominalization-general boundary)",
      "gate_declarative": "To emit the TOPICS.md status line first is this step's role.",
      "predicted_score_lower": 126,
      "predicted_score_upper": 128,
      "predicted_failures_certain": ["C-28", "C-29"],
      "predicted_failures_ambiguous": ["C-34"],
      "c33_fires": false,
      "key_hypothesis": "If 128: C-34 gerundive-specific; C-35 candidate for infinitival case. If 126: C-34 covers all action-nominalizations"
    },
    {
      "id": "V-04",
      "axis": "Appositional step identifier (C-29 identifier-strict vs referential boundary)",
      "gate_declarative": "The emit step, S-0, runs before all other steps produce any output.",
      "predicted_score_lower": 130,
      "predicted_score_upper": 132,
      "predicted_failures_ambiguous": ["C-29"],
      "c33_fires": false,
      "c34_fires": false,
      "key_hypothesis": "C-29 identifier-strict: score 130. C-29 referential: score 132"
    },
    {
      "id": "V-05",
      "axis": "Transitive-object confirmed positive (artifact in direct-object position)",
      "gate_declarative": "S-0 emits the TOPICS.md status line before any other output.",
      "predicted_score": 132,
      "predicted_failures": [],
      "c33_fires": false,
      "c34_fires": false,
      "key_hypothesis": "Artifact in object position satisfies C-30 and C-33 simultaneously; transitive-object is the canonical safe gate form for explicit-artifact naming"
    }
  ]
}
```
