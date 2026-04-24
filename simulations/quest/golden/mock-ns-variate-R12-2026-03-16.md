---
skill: quest-variate
skill_target: mock-ns
round: 12
rubric_version: 12
rubric_target: C-35
date: 2026-03-16
---

# mock-ns -- Round 12 Variations (rubric v12, C-35 target)

Rubric: v12 (C-01 through C-35, 5 essential / 3 recommended / 27 aspirational, max 134).

New criterion in v12 (extracted from R11 V-01 scoring):

- **C-35** -- Relative-clause-agent displacement: The declarative sentence must not place the
  step as the agent of a restrictive relative clause while the artifact occupies the main-clause
  nominative subject position. "TOPICS.md is the first artifact this step emits" has "TOPICS.md"
  as main-clause subject and "this step" as agent inside "this step emits" (relative clause).
  The step is grammatically active in the subordinate clause; C-35 requires it to be
  grammatically active in the MAIN clause as nominative subject.
  Failure chain: C-25, C-28, C-29, C-30, C-35 (-10 pts). C-33 passes (active voice, not passive).

R11 evidence sources (retroactive v12 scores):

- R11 V-01 (124/134): "TOPICS.md is the first artifact this step emits." Active artifact-as-subject
  + relative-clause-agent step. C-25, C-28, C-29, C-30, C-35 all fail; C-33 PASS.
- R11 V-02 (predicted 128-130/134): Wh-cleft with embedded step. [Retroactive scoring pending.]
- R11 V-05 (predicted 134/134): Transitive-object confirmed positive. [Retroactive scoring pending.]

Confirmed baseline for R12 (any of):
  "This step emits first."               -- R10 champion (134/134 under v12)
  "S-0 is the emit step."               -- R9 champion (134/134 under v12)
  "This step emits the TOPICS.md        -- R11 V-05 form
   status line before any other output."

Open questions from R11/v12 to investigate in R12:

| Question | Target variation |
|----------|-----------------|
| Does C-28 fail when step is main-clause subject but emission is confined to a relative clause? | V-01 |
| Does fronted adverbial clause ("Before...") displace step from main-clause subject? | V-02 |
| Does possessive-subject form ("This step's first action is...") fail C-29? | V-03 |
| Does "This step is the first to emit..." (infinitival complement) pass C-28? | V-04 |
| Can transitive-object form with explicit artifact + ordering contrast achieve 134/134? | V-05 |

Variation axes for R12 (three single-axis + two combined):

1. **Relative-clause emission with step as main-clause subject** (V-01) -- "S-0, which emits
   the TOPICS.md status line first, runs before all other steps"; step is main-clause subject
   but emission action is confined to a non-restrictive relative clause; tests C-28's
   "grammatical subject of its own emission action" requirement -- does the emission need to
   be in the main predicate?

2. **Fronted adverbial clause** (V-02) -- "Before any other step begins, this step emits the
   TOPICS.md status line"; temporal adverbial fronting; step is main-clause subject + emission
   is main predicate; tests whether fronted subordinate clause triggers any criterion

3. **Possessive-subject nominalization** (V-03) -- "This step's first action is emitting the
   TOPICS.md status line"; possessive NP "this step's first action" as main-clause subject;
   step demoted to possessor; tests C-29 (substitution: "It" refers to "first action", not
   step), C-28 (step not grammatical subject of emission), C-35 (step not main-clause nominative)

4. **Equative with infinitival complement** (V-04) -- "This step is the first to emit the
   TOPICS.md status line"; step as main-clause subject of equative copula; emission in
   infinitival complement; tests C-28 boundary: does step-as-subject-of-"is" satisfy "step
   as grammatical subject of its own emission action"?

5. **Confirmed positive: transitive-object with explicit artifact + ordering contrast** (V-05) --
   "This step emits the TOPICS.md status line before any other step produces output"; step
   as main-clause nominative, emission as main predicate, artifact as direct object, explicit
   ordering contrast in subordinate clause; predicted 134/134

---

## V-01 -- Relative-clause emission with step as main-clause subject

**Axis:** C-28 boundary: step is main-clause nominative subject, but emission action is
confined to a non-restrictive relative clause; main predicate is an ordering/completion verb.
**Hypothesis:** C-35 PASSES (step is main-clause nominative, not a relative-clause agent).
C-28 FAILS (emission action is in the relative clause, not the main predicate; "grammatical
subject of its own emission action" requires the emission to be the main predicate, not an
embedded attribute). C-25: borderline -- sentence declares the step runs first, which is a
role-assertion, so C-25 may pass. If C-28 fails, C-29 is independent (substitution test).
Expected score: 130/134 (C-28 fails) or lower if C-25 also triggered.

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

S-0, which emits the TOPICS.md status line first, runs before all other steps.
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

Sentence 1: "S-0, which emits the TOPICS.md status line first, runs before all other steps."
- Main-clause subject: "S-0" (the step -- nominative)
- Main-clause predicate: "runs before all other steps" (NOT an emission action -- ordering/motion verb)
- Relative clause: "which emits the TOPICS.md status line first" (modifies S-0; emission confined here)

- C-25: The sentence declares S-0's role (it runs first, before other steps). This is a step
  role-assertion. PASS -- content-based test satisfied.
- C-28: "Grammatical subject of its own emission action" -- S-0 is the grammatical subject,
  but the emission action is "emits" in the relative clause, not the main predicate. The main
  predicate is "runs." Question: does "grammatical subject of its own emission action" require
  the emission to be the MAIN predicate? If yes: FAIL. If the relative clause counts: PASS.
- C-29: Substitution -- "It, which emits first, runs before all other steps." "It" = S-0.
  Step is nominative head. PASS (if C-28 passes) or partially satisfied regardless.
- C-30: Artifact is in direct-object position inside the relative clause, not in active
  nominative position at main-clause level. PASS.
- C-33: Active voice. PASS.
- C-34: No gerundive subject. PASS.
- C-35: Step is main-clause nominative. PASS (C-35 specifically requires main-clause subject;
  S-0 satisfies this). C-35 is the key differentiator from R11 V-01.

**Predicted score: 130/134 (C-28 fails) or 134/134 (C-28 passes if relative-clause emission counts).**

Key question for R12: Does C-28 require emission in the MAIN predicate, or is relative-clause
emission sufficient? V-01 isolates this question. The answer determines whether C-35 is
sufficient for full C-28 recovery or whether C-28 has a stricter main-predicate requirement
independent of C-35.

---

## V-02 -- Fronted adverbial clause

**Axis:** Fronted subordinate temporal clause; step is unambiguous main-clause subject with
emission as main predicate. Establishes that fronted adverbials do not trigger any criterion.
**Hypothesis:** All 35 criteria pass. This is a confirmed-positive form -- identical to the
R10 champion structure except fronted adverbial is added. Expected score: 134/134.

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

Before any other step begins, this step emits the TOPICS.md status line.
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

**V-02 gate analysis:**

Sentence 1: "Before any other step begins, this step emits the TOPICS.md status line."
- Fronted adverbial clause: "Before any other step begins" (temporal subordinate clause)
- Main-clause subject: "this step" (the step -- nominative)
- Main-clause predicate: "emits" (emission action -- direct)
- Direct object: "the TOPICS.md status line"

- C-25: Declarative sentence is first. Step is declared as the emitter (role-assertion). PASS.
- C-28: "This step" is grammatical subject of its own emission action "emits." PASS.
- C-29: Substitution -- "Before any other step begins, it emits the TOPICS.md status line."
  "It" = "this step." Step is nominative head. PASS.
- C-30: Artifact is direct object, not active nominative. PASS.
- C-33: Active voice. PASS.
- C-34: No gerundive subject. PASS.
- C-35: "This step" is main-clause nominative subject. PASS.

Fronted adverbial clause ("Before any other step begins") is a subordinate clause, but it
modifies the main clause -- it does not displace the main-clause subject. No criterion
targets fronted adverbials. The sentence structure is clean across all 35 criteria.

**Predicted score: 134/134.**

---

## V-03 -- Possessive-subject nominalization

**Axis:** C-29 and C-28 boundary: "this step's first action" as main-clause subject; step
demoted to possessor inside the NP. Tests whether C-29's substitution test fires when the
step is possessor (not nominative head) and C-35 fires when the possessive NP head is a
nominalized action, not the step itself.
**Hypothesis:** C-28 FAILS (step is possessor, not grammatical subject of emission). C-29
FAILS (substitution "It is emitting the TOPICS.md status line" -- "It" = "this step's first
action", not the step). C-35 FAILS (step is not main-clause nominative -- possessive NP head
"first action" is). Expected score: 124/134 (C-28, C-29, C-35 fail; -6 aspirational pts and
impact on C-25 depending on content-based ruling).

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

This step's first action is emitting the TOPICS.md status line.
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

**V-03 gate analysis:**

Sentence 1: "This step's first action is emitting the TOPICS.md status line."
- Main-clause subject: "This step's first action" (possessive NP; head = "action", possessor = "this step")
- Main-clause predicate: "is emitting" (copular + gerundive predicate nominal)

- C-25: The sentence declares what the step's first action is. Content-based: does asserting
  a property of the step's action constitute a step role-assertion? Borderline. C-25 may
  FAIL if "this step" must be the NP head of the declarative subject, not just a possessor.
- C-28: "This step" is the possessor inside the NP, not the grammatical subject. The
  grammatical subject is "This step's first action." The step is not the grammatical subject
  of its own emission action. FAIL.
- C-29: Substitution -- "It is emitting the TOPICS.md status line." "It" = "this step's
  first action" (the NP head), not "this step." Step is not the nominative referent. FAIL.
- C-30: Artifact is predicate nominal (inside gerundive), not active nominative. PASS.
- C-33: Active voice. PASS.
- C-34: "Emitting the TOPICS.md status line" is the predicate nominative (complement of
  copula), not the sentence subject. C-34 fires when a gerundive is in SUBJECT position.
  Here it is in predicate position. PASS.
- C-35: "This step" is possessor inside subject NP, not the main-clause nominative head.
  FAIL (C-35 requires step as main-clause nominative; "this step's first action" as subject
  places a nominalized action, not the step, in nominative position).

This is a new pattern: possessive-possessor displacement. The step is present in the NP
but as possessor, not nominative head. C-35 fires (step not main-clause nominative).
C-28 fires independently (step not grammatical subject of emission). C-34 does NOT fire
(gerundive is predicate, not subject). This is a distinct failure pattern from C-34.

**Predicted score: 124/134 (C-28, C-29, C-35 fail; C-25 borderline; C-34 PASS).**

If C-25 also fails: 122/134. A new potential criterion may be warranted: possessive-subject
displacement as a named sixth failure mode distinct from C-35.

---

## V-04 -- Equative with infinitival complement

**Axis:** C-28 boundary: step as main-clause subject of copula "is"; emission in infinitival
complement "to emit." Tests whether C-28's "grammatical subject of its own emission action"
requires the step to be the subject of an active-voice emission verb, or whether being the
subject of an equative that CHARACTERIZES the step by its emission role satisfies C-28.
**Hypothesis:** C-35 PASSES (step is main-clause nominative). C-28 is the open question:
"This step is the first to emit" -- step is subject of "is", not of "emit." The emission
appears in the infinitival complement. If C-28 requires direct-subject-of-emission: FAIL.
If subject-of-equative-characterizing-emission satisfies it: PASS.
Expected score: 134/134 (if C-28 passes) or 132/134 (if C-28 fails).

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

This step is the first to emit the TOPICS.md status line.
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

**V-04 gate analysis:**

Sentence 1: "This step is the first to emit the TOPICS.md status line."
- Main-clause subject: "This step" (the step -- nominative)
- Main-clause predicate: "is the first to emit the TOPICS.md status line" (equative copula
  with infinitival complement)

- C-25: Declarative sentence declares the step's role as first emitter. PASS.
- C-28: "This step" is grammatical subject. The emission is in the infinitival complement
  "to emit the TOPICS.md status line." The step does not have "emit" as its direct main
  predicate; the main predicate is "is." Open question: does C-28's "grammatical subject
  of its own emission action" require the emission verb to be the main predicate?
  - If strict reading (must be subject of active emission verb): FAIL
  - If equative characterization suffices (step is identified by its emission role): PASS
- C-29: Substitution -- "It is the first to emit the TOPICS.md status line." "It" = "this step."
  Step is nominative head. PASS.
- C-30: Artifact is inside the infinitival complement, not active nominative. PASS.
- C-33: Active construction. PASS.
- C-34: No gerundive subject. PASS.
- C-35: "This step" is main-clause nominative. PASS.

The key discriminator for R12 is whether C-28 fires on equative constructions where the
step is identified by its emission role but the emission appears in an infinitival
complement. V-04 is the cleanest isolation of this question.

**Predicted score: 134/134 (if C-28 passes on equative form) or 132/134 (if C-28 fails).**

If C-28 fails on V-04, a new criterion may be warranted for equative-infinitival displacement
(the step is characterized by its emission but the emission verb is not the main predicate).

---

## V-05 -- Confirmed positive: transitive-object + explicit artifact + ordering contrast

**Axis:** Combined: step as main-clause nominative, emission as main predicate, artifact as
transitive direct object, explicit ordering contrast in subordinate clause. This is the
strongest confirmed-positive form based on all prior rounds. Predicted 134/134.
**Hypothesis:** All 35 criteria pass. Step is unambiguous main-clause subject of an active
emission verb; artifact is direct object; "before any other step produces output" explicitly
names the ordering contrast without displacing the step from subject position.

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

This step emits the TOPICS.md status line before any other step produces output.
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

Sentence 1: "This step emits the TOPICS.md status line before any other step produces output."
- Main-clause subject: "This step" (the step -- nominative)
- Main-clause predicate: "emits" (emission action -- direct, active voice)
- Direct object: "the TOPICS.md status line"
- Subordinate clause: "before any other step produces output" (temporal adverbial -- does not
  displace step from subject position)

- C-25: Declarative sentence is first. Step declares its role as the emitter. PASS.
- C-28: "This step" is grammatical subject of its own emission action "emits." PASS.
- C-29: Substitution -- "It emits the TOPICS.md status line before any other step produces
  output." "It" = "this step." Step is nominative head. PASS.
- C-30: Artifact is direct object of "emits," not active nominative subject. PASS.
- C-33: Active voice. PASS.
- C-34: No gerundive subject. PASS.
- C-35: "This step" is main-clause nominative subject, not a relative-clause agent. PASS.

The subordinate clause "before any other step produces output" adds an explicit ordering
contrast but is a temporal adverbial subordinate clause -- it does not participate in any
of the displacement failure modes (C-25 through C-35). V-02 confirmed fronted adverbials
pass; V-05 confirms trailing adverbial subordinate clauses also pass.

**Predicted score: 134/134.**

---

## Summary Table

| Variate | Declarative sentence | Primary axis | Predicted score | Key criteria at risk |
|---------|---------------------|--------------|-----------------|----------------------|
| V-01 | "S-0, which emits the TOPICS.md status line first, runs before all other steps." | C-28: emission in relative clause (not main predicate) | 130/134 | C-28 (FAIL), C-35 (PASS) |
| V-02 | "Before any other step begins, this step emits the TOPICS.md status line." | Fronted adverbial: no displacement | 134/134 | All pass |
| V-03 | "This step's first action is emitting the TOPICS.md status line." | C-29/C-35: possessive-subject displacement | 124/134 | C-28, C-29, C-35 (all FAIL) |
| V-04 | "This step is the first to emit the TOPICS.md status line." | C-28: equative + infinitival complement | 132/134 or 134/134 | C-28 (open question) |
| V-05 | "This step emits the TOPICS.md status line before any other step produces output." | Confirmed positive: transitive-object + ordering contrast | 134/134 | All pass |

**Key questions this round resolves:**

1. **C-28 main-predicate requirement** (V-01, V-04): Does C-28 require the emission action to
   be the main predicate, or does subject position alone satisfy it? V-01 has emission in a
   non-restrictive relative clause; V-04 has emission in an infinitival complement. Both have
   the step as main-clause subject. If both fail C-28 despite step-as-main-subject, C-28 has
   a "main-predicate-emission" requirement that C-35's main-clause-subject requirement does
   not cover. A new criterion naming this gap would be warranted.

2. **Possessive-subject displacement as a new named failure mode** (V-03): "This step's first
   action" places the step as possessor, not nominative. C-35 fires (step not main-clause
   nominative). C-28 fires independently (step not grammatical subject of emission). This is
   a new structural pattern not previously named; if V-03 scores as predicted, C-36 may be
   warranted for possessive-subject displacement.

3. **Fronted/trailing adverbials confirmed safe** (V-02, V-05): Confirms that temporal
   adverbial subordinate clauses -- whether fronted or trailing -- do not trigger any criterion.
   Provides clean baselines for the open-question variates.
