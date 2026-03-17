---
skill: quest-variate
skill_target: mock-ns
round: 13
rubric_version: 13
rubric_target: C-36, C-37
date: 2026-03-16
---

# mock-ns -- Round 13 Variations (rubric v13, C-36/C-37 targets)

Rubric: v13 (C-01 through C-37, 5 essential / 3 recommended / 29 aspirational, max 138).

New criteria in v13 (extracted from R12 scoring):

- **C-36** -- Ordering-predicate displacement: the step is the main-clause subject, but the main
  predicate is an ordering verb (`runs`, `executes`, `precedes`), and the emission is demoted to a
  restrictive relative clause ("S-0, which emits the TOPICS.md status line first, runs before all
  other steps"). Step as main-clause subject is necessary but not sufficient -- emission must be
  the main predicate. Failure chain: C-25, C-28, C-36 (-6 pts).

- **C-37** -- Possessive-NP action-abstraction subject with gerundive emission complement: the
  subject NP is formed as `[step]'s [action noun]` ("This step's first action"), with the gerundive
  emission as predicate complement ("is emitting..."). The step is demoted to possessor in the
  subject NP. C-34 does NOT fire (gerundive is predicate complement, not subject). Failure chain:
  C-25, C-28, C-29, C-30, C-37 (-10 pts).

Confirmed positive baseline for R13 (all score 138/138 under v13):
  "Before any other step begins, this step emits the TOPICS.md status line."   -- R12 V-02
  "This step is the first to emit the TOPICS.md status line."                  -- R12 V-04
  "This step emits the TOPICS.md status line before any other step produces output." -- R12 V-05

Open questions from R12/v13 to investigate in R13:

| Question | Structure to probe | C-36/C-37 relevance |
|----------|-------------------|---------------------|
| Q1: Does it-cleft fail C-28 or C-36? | "It is this step that first emits..." | Step is focused NP, not main-clause subject; emission in relative clause |
| Q2: Does wh-pseudo-cleft fail C-25/C-28/C-29? | "What this step does first is emit..." | Step inside subject wh-clause; "It" substitution resolves to wh-nominal |
| Q3: Does role-sequence change affect declarative criteria? | S-0 merged into S-1; S-2+S-3 combined | Structural, not phrasing axis |
| Q4: Does compound-sentence form pass? | "This step runs first; it emits the TOPICS.md status line." | Split: ordering in first conjunct, emission as main predicate in second |
| Q5: Does expletive-subject form fail distinctly? | "There is this step, which emits..." | Expletive subject + relative clause |

Axes selected for R13:
  Axis A -- Phrasing (it-cleft): V-01
  Axis B -- Phrasing (wh-pseudo-cleft): V-02
  Axis C -- Phrasing (compound-sentence split): V-03
  Combined A+B+C not applicable -- axes are mutually exclusive phrasing alternatives;
    instead, V-04 combines confirmed-positive phrasing with role-sequence restructuring,
    and V-05 combines confirmed-positive phrasing with output-format axis.

---

## V-01 -- Single-axis: Phrasing (it-cleft)

**Variation axis**: Phrasing register -- it-cleft construction for S-0 declarative.

**Hypothesis**: "It is this step that first emits the TOPICS.md status line." focuses the step via
it-cleft. The main-clause subject is the expletive `It`; `this step` is the cleft constituent; the
emission verb `emits` is inside the relative clause `that first emits...`. Expected to fail C-25
(step is not nominative subject head -- it is focused NP in cleft complement) and C-28 (emission
verb confined to relative clause). C-36 may not fire (step is not the main-clause subject -- `It`
is). This is structurally distinct from C-36 and C-37; may motivate a C-38 candidate for
it-cleft-with-relative-clause emission.

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
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC];
P-0 table, row 3 = [P-0:ABD].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (use the pre-filled table block at the
             current use site; fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-0 -- STATUS EMISSION

It is this step that first emits the TOPICS.md status line.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context, including paths that do    |
  |                         | not pass through prior steps in normal order                         |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-3:CS]                       |
  | Step       | S-3                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | This rule is first in this step -- it applies before any other       |
  |                         | instruction                                                          |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step -- named or unnamed -- is governed    |
  |                         | by this rule                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [A-1:FC]                       |
  | Step       | A-1                            |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

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

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
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

---
---
---

## V-02 -- Single-axis: Phrasing (wh-pseudo-cleft)

**Variation axis**: Phrasing register -- wh-pseudo-cleft construction for S-0 declarative.

**Hypothesis**: "What this step does first is emit the TOPICS.md status line." uses a
wh-pseudo-cleft. The subject is the wh-clause nominalization "What this step does first"; the main
verb is equative "is"; the predicate complement is the bare infinitival "emit the TOPICS.md status
line". The step appears inside the subject wh-clause, not as the nominative head. Expected to fail
C-25 (step embedded in wh-subject clause, not nominative head) and C-28 (emission verb in predicate
complement, not main predicate with step as subject). C-29 substitution: "It is emit the TOPICS.md
status line" where It = "What this step does first" (a wh-nominalization, not the step) -- C-29
fails. Structurally distinct from C-36 and C-37; may motivate a C-38 candidate for
wh-pseudo-cleft displacement.

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
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC];
P-0 table, row 3 = [P-0:ABD].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (use the pre-filled table block at the
             current use site; fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-0 -- STATUS EMISSION

What this step does first is emit the TOPICS.md status line.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context, including paths that do    |
  |                         | not pass through prior steps in normal order                         |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-3:CS]                       |
  | Step       | S-3                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | This rule is first in this step -- it applies before any other       |
  |                         | instruction                                                          |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step -- named or unnamed -- is governed    |
  |                         | by this rule                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [A-1:FC]                       |
  | Step       | A-1                            |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

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

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
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

---
---
---

## V-03 -- Single-axis: Phrasing (compound-sentence split)

**Variation axis**: Phrasing register -- compound-sentence split for S-0 declarative.

**Hypothesis**: "This step runs first; it emits the TOPICS.md status line." splits the ordering
claim and the emission claim into two independent conjuncts joined by semicolon. The first conjunct
("This step runs first") places the step as main-clause subject with an ordering predicate -- this
fires C-36 in isolation if treated as the sole declarative sentence. However, the second conjunct
("it emits the TOPICS.md status line") places the step's pronoun as the main-clause nominative
subject of the emission verb in the main predicate. The question is whether C-25 and C-28 require
a SINGLE declarative sentence to satisfy both conditions, or whether a compound sentence where the
second conjunct carries the emission in its own main predicate satisfies the criteria.
If compound-sentence split fails C-36 (the first conjunct independently fires it), R13 establishes
that the entire sentence must have emission as the SOLE main predicate -- not one of multiple
coordinated predicates where an ordering predicate precedes.

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
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC];
P-0 table, row 3 = [P-0:ABD].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (use the pre-filled table block at the
             current use site; fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-0 -- STATUS EMISSION

This step runs first; it emits the TOPICS.md status line.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context, including paths that do    |
  |                         | not pass through prior steps in normal order                         |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-3:CS]                       |
  | Step       | S-3                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | This rule is first in this step -- it applies before any other       |
  |                         | instruction                                                          |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step -- named or unnamed -- is governed    |
  |                         | by this rule                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [A-1:FC]                       |
  | Step       | A-1                            |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

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

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
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

---
---
---

## V-04 -- Combined: Confirmed-positive phrasing + role-sequence restructuring

**Variation axis A**: Phrasing register -- confirmed-positive temporal-subordinate from R12 V-02.
**Variation axis B**: Role sequence -- S-2 (category) and S-3 (flag) merged into a single
  CLASSIFY step; S-0 emission step kept as standalone.

**Hypothesis**: Merging CLASSIFY (S-2 + S-3) into a single step reduces the cognitive gap between
category assignment and flag derivation, eliminating the "compute category, then separately compute
flag" context switch. The confirmed-positive phrasing in S-0 ("Before any other step begins, this
step emits...") provides the 138/138 emission declaration. The structural question is whether the
merged CLASSIFY step preserves the FLAG immutability guarantee -- the cross-reference chain (S-3:CS
-> A-1:FC) must still bind to the merged step.

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

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at CL-1 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token       | Step | Row type                    | Paired token | Direction                     |
  |-------------|------|-----------------------------|--------------|-------------------------------|
  | [CL-1:CS]   | CL-1 | Cross-site reference row    | [A-1:FC]     | forward --> names A-1         |
  | [A-1:FC]    | A-1  | Failure consequence row     | [CL-1:CS]    | <-- backward, names CL-1      |
  | [P-0:ABD]   | P-0  | Anti-bypass declaration     | (self)       | definition point              |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [CL-1:CS]; P-0 table, row 2 = [A-1:FC];
P-0 table, row 3 = [P-0:ABD].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (use the pre-filled table block at the
             current use site; fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-0 -- STATUS EMISSION

Before any other step begins, this step emits the TOPICS.md status line.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

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

STEP CL-1 -- CLASSIFY (CATEGORY + FLAG)

This step assigns CATEGORY and derives FLAG in a single pass. Both are named variables.
CATEGORY is assigned first. FLAG is derived second. Neither is modified after this step.

**Part A -- Assign CATEGORY**

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned.

**Part B -- Compute FLAG**

FLAG is computed exactly once. It is a named variable.

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context, including paths that do    |
  |                         | not pass through prior steps in normal order                         |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [CL-1:CS] in P-0 table, row 1. Phase 2 (Steps 2a- |
  | before writing this row | 2d): read Step=CL-1 + Row type=Cross-site reference row; assert    |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below         |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete     |
  |                         | and the record is emitted.                                          |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Cross-site ref [CL-1:CS]| The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [CL-1:CS]                      |
  | Step       | CL-1                           |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

CATEGORY and FLAG are now resolved. Do not re-evaluate or modify either anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from CL-1 verbatim. Do not rederive it.                    |
  | Priority                | This rule is first in this step -- it applies before any other       |
  |                         | instruction                                                          |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step -- named or unnamed -- is governed    |
  |                         | by this rule                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Failure conseq [A-1:FC] | [Mutual target of CL-1:CS -- Cross-site reference row in CL-1]       |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [A-1:FC]                       |
  | Step       | A-1                            |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from CL-1}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from CL-1 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
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

---
---
---

## V-05 -- Combined: Confirmed-positive phrasing + role-sequence restructuring + output-format

**Variation axis A**: Phrasing register -- "This step emits the TOPICS.md status line before any
  other step produces output." (R12 V-05 champion, trailing-adverbial form, 138/138 under v13).
**Variation axis B**: Role sequence -- S-2 and S-3 merged into CL-1 (same as V-04).
**Variation axis C**: Output format -- step-overview table added at top of skill body, listing
  all steps with purpose and expected output; FLAG immutability chain presented as a two-row
  summary at CL-1 entry rather than the full six-row table (full table is replaced by a compact
  single-paragraph declaration; the cross-reference protocol in P-0 still governs).

**Hypothesis**: The step-overview table (Axis C) makes the execution contract explicit at the
top -- an evaluator reading the skill body can verify the correct step order and expected output
before reaching each step. The compact FLAG immutability declaration at CL-1 tests whether a
shorter immutability block (less structural overhead) maintains the same cross-reference guarantee
or whether the full table is required to pass the immutability criteria.

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

STEP OVERVIEW

  | Step | Purpose                         | Expected output                              |
  |------|---------------------------------|----------------------------------------------|
  | P-0  | Cross-reference protocol        | Token table + lookup obligation              |
  | S-0  | Status emission                 | TOPICS.md status line (first output)         |
  | S-1  | Setup -- skill selection        | Generating mock line                         |
  | CL-1 | Classify -- category + flag     | CATEGORY assigned; FLAG resolved once        |
  | A-1  | Assemble header                 | 6-field MOCK ARTIFACT header block           |
  | A-2  | Fidelity warning                | Category-matched warning section             |
  | A-3  | Artifact body                   | Full skill-specific mock body                |
  | A-4  | Write artifact                  | File written; path emitted                   |
  | A-5  | Next-step line                  | /mock:review call at end of artifact         |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at CL-1 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token       | Step | Row type                    | Paired token | Direction                     |
  |-------------|------|-----------------------------|--------------|-------------------------------|
  | [CL-1:CS]   | CL-1 | Cross-site reference row    | [A-1:FC]     | forward --> names A-1         |
  | [A-1:FC]    | A-1  | Failure consequence row     | [CL-1:CS]    | <-- backward, names CL-1      |
  | [P-0:ABD]   | P-0  | Anti-bypass declaration     | (self)       | definition point              |

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record:
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

---

STEP S-0 -- STATUS EMISSION

This step emits the TOPICS.md status line before any other step produces output.

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

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

STEP CL-1 -- CLASSIFY (CATEGORY + FLAG)

This step assigns CATEGORY and derives FLAG. Both are named variables resolved once here.

**Part A -- Assign CATEGORY**

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

**Part B -- Compute FLAG**

FLAG is computed exactly once. It is a named variable.

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

FLAG immutability: FLAG MUST NOT be recomputed or modified anywhere in this run.
Every execution path that reaches A-1 carries the FLAG value emitted here. No path
is exempt. Recomputing FLAG at A-1 silently corrupts the artifact's trust tier in a
way that cannot be detected without manual header inspection.

CONFIRMATION REQUIRED before writing the cross-site reference row below.
Phase 1: locate [CL-1:CS] in P-0 table, row 1.
Phase 2 (Steps 2a-2d): read Step=CL-1 + Row type=Cross-site reference row;
assert match; emit confirmation record (Step 2d). DO NOT WRITE THE ROW until
Steps 2a-2d are complete and the record is emitted.

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [CL-1:CS]                      |
  | Step       | CL-1                           |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

The failure consequence at [A-1:FC] is: re-deriving FLAG at A-1 produces a silent
category mismatch undetectable without manual inspection. Do not rederive FLAG.

CATEGORY and FLAG are now resolved. Do not re-evaluate or modify either anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

First rule (before all other instructions): copy FLAG from CL-1 verbatim. Do not
rederive it. This rule governs every instruction in this step. No instruction is exempt.

CONFIRMATION REQUIRED before writing the failure consequence row below.
Phase 1: locate [A-1:FC] in P-0 table, row 2.
Phase 2 (Steps 2a-2d): read Step=A-1 + Row type=Failure consequence row;
assert match; emit confirmation record. DO NOT WRITE THE ROW until
Steps 2a-2d are complete and the record is emitted.

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [A-1:FC]                       |
  | Step       | A-1                            |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from CL-1}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from CL-1 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
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

---

## Summary Table

| Variation | Axis | S-0 declarative sentence | Predicted C-36 | Predicted C-37 | Predicted total |
|-----------|------|--------------------------|----------------|----------------|-----------------|
| V-01 | Phrasing (it-cleft) | "It is this step that first emits the TOPICS.md status line." | PASS (step not main-clause subject) | PASS | ~128-132/138 (C-25, C-28 likely fail -- new territory) |
| V-02 | Phrasing (wh-pseudo-cleft) | "What this step does first is emit the TOPICS.md status line." | PASS | PASS | ~128-132/138 (C-25, C-28, C-29 likely fail) |
| V-03 | Phrasing (compound-split) | "This step runs first; it emits the TOPICS.md status line." | boundary | PASS | ~132-136/138 (C-36 boundary: first conjunct has ordering predicate) |
| V-04 | Confirmed-positive + role-sequence | "Before any other step begins, this step emits the TOPICS.md status line." | PASS | PASS | 138/138 (subject to CL-1 immutability chain holding) |
| V-05 | Confirmed-positive + role-sequence + step-overview table | "This step emits the TOPICS.md status line before any other step produces output." | PASS | PASS | 138/138 (tests compact immutability block -- may fail immutability criteria) |

Open questions for R13 scoring:

- **Q1 (it-cleft)**: Does "It is this step that..." fail C-25 (step not nominative head), C-28
  (emission in relative clause), and potentially introduce a C-38 candidate for
  expletive-subject cleft-with-relative-clause emission?

- **Q2 (wh-pseudo-cleft)**: Does "What this step does first is emit..." fail C-25, C-28, C-29
  (substitution "It" = wh-nominalization, not the step)? Does the equative form pass C-34
  (emission verb `emit` is predicate complement, not subject -- C-34 should not fire)?

- **Q3 (compound-split)**: Does "This step runs first; it emits..." fire C-36 on the first
  conjunct, or does C-36 require a single declarative sentence? If the second conjunct's emission
  in main-predicate position rescues C-28, a new discriminator note to C-36 is warranted.

- **Q4 (compact immutability in V-05)**: Does reducing the full FLAG immutability six-row table
  to a two-paragraph prose declaration preserve passing scores on immutability criteria? If it
  fails, this identifies which criteria require the table form specifically.
