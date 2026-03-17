---
name: signal-mock-ns
description: Mock artifact for a single namespace with category annotation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
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

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line:
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