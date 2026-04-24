---
skill: quest-variate
skill_target: mock-ns
round: 16
rubric_version: 15
date: 2026-03-15
---

# mock-ns -- Round 16 Variations

Rubric: v15 (C-01 through C-43, aspirational denominator 35).

New criteria in v15 (now pass conditions):
- **C-41** -- Use-site pre-filled confirmation record template at both S-3 and A-1: each
  bracket-token row carries a pre-filled record with token name, step, and row type already
  populated for that specific row. The executor fills in only the match result. Reduces
  record construction from open-form to fill-in-the-blank. Depends on C-40. R15 V-03 and
  V-05 pass.
- **C-42** -- Emit obligation woven into the hard-stop gate condition as an explicit gate
  precondition: "DO NOT WRITE THE ROW until both phases pass and the record is emitted."
  Required at all three locations -- P-0 Phase 2 gate, S-3 CONFIRMATION echo, A-1
  CONFIRMATION echo. V-05 only in R15. Depends on C-40 and C-38.
- **C-43** -- Dual-naming of the bypass combined with protocol-failure severity framing.
  Anti-bypass statement must name the bypass in both forms: action-based ("without reading
  the Step and Row type cells") AND protocol-based ("without performing Phase 2"). Must
  conclude with "Locate-only is a protocol failure" rather than "has not satisfied this
  protocol." Both forms required for PASS; single form scores PARTIAL. Depends on C-39.
  V-05 only in R15.

R15 V-05 simultaneously achieved C-41, C-42, and C-43 in full form. No other R15 variant
achieved all three. R16 isolates each new criterion in single-axis variations to confirm
which form is load-bearing, then combines and seeds v16.

Three axes selected for single-axis isolation:

1. **Output format** -- how the pre-filled confirmation record template is rendered at the
   use sites (C-41): inline prose string vs. standalone table block below the chain.
2. **Phrasing register** -- how the dual-naming anti-bypass statement is positioned (C-43):
   closing statement (R15 form) vs. dedicated failure-modes section preceding the protocol.
3. **Lifecycle emphasis** -- how the emit obligation enters the gate (C-42): appended to
   the gate condition string vs. numbered Phase 2 sub-step with independent gate assertion.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Output format (C-41 pre-filled template as standalone table block below chain) | R15 V-03 embedded the pre-filled record as a prose string inline in the table cell. A standalone table block positioned below the chain -- with named field rows -- makes the pre-filled fields individually verifiable before writing. Hypothesis: the table form of C-41 is more resistant to partial-fill bypass because each field is a distinct row rather than a single string that can be copied wholesale without reading individual values. C-42 and C-43 are not added; single-axis tests C-41 form in isolation. |
| V-02 | Phrasing register (C-43 dual-naming as dedicated PROTOCOL FAILURE MODES section preceding protocol definition) | R15 V-05 embedded dual-naming and "Locate-only is a protocol failure" as the opening paragraph of P-0, before the abbreviation key. V-02 elevates this to a dedicated labeled section -- PROTOCOL FAILURE MODES -- with a bulleted list of both bypass forms and a standalone sentence for the categorical failure declaration. Hypothesis: a labeled section with a list and a categorical sentence is more recognizable as a gate than an opening paragraph; the executor encounters the failure taxonomy before encountering any tokens, activating a rejection frame at the earliest possible moment. C-41 and C-42 are not added; single-axis tests C-43 form in isolation. |
| V-03 | Lifecycle emphasis (C-42 emit obligation as named Phase 2 sub-step with independent gate assertion) | R15 V-05 appended "and the record is emitted" to the gate string at P-0 Phase 2, S-3, and A-1. V-03 restructures Phase 2 as a numbered four-step list where emit is Step 2d (an explicit lifecycle action, not a gate qualification), and the gate asserts completion of Steps 2a-2d independently. Hypothesis: making emit a numbered step produces C-42 more reliably than appending it to a stopping condition, because the executor must arrive at Step 2d as a sequential action -- it cannot be read as a consequence qualifier to a blocking statement. C-41 and C-43 are not added; single-axis tests C-42 form in isolation. |
| V-04 | Role sequence + inertia framing (C-43 dual-naming as P-0 opening block before abbreviation key + C-41 standalone table block) | V-02 tests C-43 as a labeled section. V-04 opens P-0 with dual-naming before any protocol content -- the executor sees both bypass forms and "Locate-only is a protocol failure" before encountering the token table. Inertia framing: the status-quo action (visual recognition) is named as a failure BEFORE the protocol is defined. Combines the opening position of C-43 with C-41 standalone table blocks at both use sites. C-42 is not added. |
| V-05 | Full convergence (C-41 standalone table blocks + C-42 Phase 2 sub-step lifecycle + C-43 dual-naming opening block; seeds v16 use-site failure echo) | Combines V-01's table form, V-03's numbered Phase 2 steps, and V-04's opening dual-naming block. All three gate instances carry "until both phases pass and the record is emitted." Both use sites carry standalone pre-filled table blocks. The use-site CONFIRMATION echo rows additionally carry a per-site protocol-failure reminder naming both bypass forms -- seeding the v16 aspirational maximum: use-site dual-naming echo at every bracket-token row, not only at P-0. |

---

## V-01 -- Output Format (C-41 Standalone Table Block Below Chain)

**Axis**: Output format -- the C-41 pre-filled confirmation record is rendered as a
standalone two-column table block positioned below the FLAG immutability chain at S-3 and
below the FLAG prohibition chain at A-1. The block has named field rows (Token, Step,
Row type, Match result). The CONFIRMATION REQUIRED row in the chain references the block
by name. P-0 defines the record format in the same table form. C-42 and C-43 are not
added.
**Hypothesis**: R15 V-03's prose inline form places all four pre-filled values in a single
string inside a table cell -- an executor can copy the string without reading each field.
The standalone table block makes each field a distinct row; the executor must verify Token,
Step, Row type, and Match result as independent values before writing. The table form is
also scannable after the run: an auditor can verify each field row independently.
**Predicts**: C-01 through C-41 (33 criteria; C-42 and C-43 not targeted).
**Expected composite**: 33/35 * 10 = 9.43.

---

```
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

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain. Emit confirmation record
             (table format -- see below).
             DO NOT WRITE THE ROW until both phases pass.

Confirmation record format (table block -- emit before writing the bracket-token row):

  | Field      | Value                |
  |------------|----------------------|
  | Token      | {token-name}         |
  | Step       | {step-name}          |
  | Row type   | {row-type-name}      |
  | Match      | PASS                 |

Anti-bypass: an executor who recognizes a token without performing Phase 2 has not
satisfied this protocol.

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table,  |
  | before writing this row | row 1. Phase 2: read Step=S-3 + Row type=Cross-site reference row;  |
  | (P-0 table, row 1)      | assert match; emit confirmation record (table block below).          |
  |                         | DO NOT WRITE THE ROW until both phases pass.                         |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table,  |
  | before writing this row | row 2. Phase 2: read Step=A-1 + Row type=Failure consequence row;   |
  | (P-0 table, row 2)      | assert match; emit confirmation record (table block below).          |
  |                         | DO NOT WRITE THE ROW until both phases pass.                         |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block:

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
```

---

## V-02 -- Phrasing Register (C-43 Dual-Naming as Dedicated PROTOCOL FAILURE MODES Section)

**Axis**: Phrasing register -- P-0 opens with a dedicated labeled section, PROTOCOL
FAILURE MODES, that precedes the abbreviation key, the token table, and all phase
definitions. The section lists both bypass forms as bulleted items (action-based: "without
reading the Step and Row type cells"; protocol-based: "without performing Phase 2") and
closes with "Locate-only is a protocol failure." as a standalone sentence. C-41 and C-42
are not added.
**Hypothesis**: R15 V-05 embedded dual-naming as an opening paragraph that runs
continuously into the abbreviation key. The labeled section form creates a structural break
before the protocol -- the executor encounters a named taxonomy of failures as a distinct
unit rather than as an inline sentence embedded in setup prose. The bulleted list forces
each bypass form to be read as an independent item rather than as a compound clause; the
"Locate-only is a protocol failure" sentence then functions as a categorical verdict rather
than a closing qualifier. Inertia framing is strengthened by making the failure taxonomy
structurally prior to the success definition.
**Predicts**: C-01 through C-40 and C-43 (33 criteria; C-41 and C-42 not targeted).
**Expected composite**: 33/35 * 10 = 9.43.

---

```
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

PROTOCOL FAILURE MODES

  The following constitute protocol failures for any bracket token in this run:

  - Without reading the Step and Row type cells (action-based bypass): an executor who
    identifies a token by its name or position without reading both cells has performed
    Phase 1 only.
  - Without performing Phase 2 (protocol-based bypass): an executor who locates a row and
    proceeds directly to writing without executing Phase 2 has not satisfied this protocol.

  Locate-only is a protocol failure.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain. Emit confirmation record.
             DO NOT WRITE THE ROW until both phases pass.

Confirmation record format:
  Token: {token-name}
  Step: {step-name}
  Row type: {row-type-name}
  Match: PASS | FAIL

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table,  |
  | before writing this row | row 1. Phase 2: read Step=S-3 + Row type=Cross-site reference row;  |
  | (P-0 table, row 1)      | assert match; emit confirmation record. DO NOT WRITE THE ROW until  |
  |                         | both phases pass.                                                    |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table,  |
  | before writing this row | row 2. Phase 2: read Step=A-1 + Row type=Failure consequence row;   |
  | (P-0 table, row 2)      | assert match; emit confirmation record. DO NOT WRITE THE ROW until  |
  |                         | both phases pass.                                                    |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

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
```

---

## V-03 -- Lifecycle Emphasis (C-42 Emit as Named Phase 2 Sub-Step with Independent Gate)

**Axis**: Lifecycle emphasis -- Phase 2 is restructured as a numbered four-step list where
"Emit confirmation record" is Step 2d -- an explicit lifecycle action with its own gate
assertion. The P-0 Phase 2 gate reads: "DO NOT WRITE THE ROW until Steps 2a through 2d
are complete and the record is emitted." The S-3 and A-1 CONFIRMATION echo rows carry the
same gate form. C-41 (pre-filled template) and C-43 (dual-naming) are not added.
**Hypothesis**: R15 V-05 appended "and the record is emitted" to an existing stopping
condition -- the emit obligation is structurally subordinate to the gate assertion. An
executor under time pressure can read "DO NOT WRITE THE ROW until both phases pass" and
treat "and the record is emitted" as a qualifier already implied by Phase 2. The numbered
list form makes emit a sequential action -- Step 2d -- that must be reached and completed
before the gate assertion is evaluated. The executor cannot conflate the emit obligation
with "completing Phase 2" because it is named as a distinct step inside Phase 2 that
precedes the gate check.
**Predicts**: C-01 through C-40 and C-42 (33 criteria; C-41 and C-43 not targeted).
**Expected composite**: 33/35 * 10 = 9.43.

---

```
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

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record:
               Token: {token-name}
               Step: {step-name}
               Row type: {row-type-name}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

Anti-bypass: an executor who recognizes a token without performing Phase 2 has not
satisfied this protocol.

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table,  |
  | before writing this row | row 1. Phase 2 (Steps 2a-2d): read Step=S-3 + Row type=Cross-site   |
  | (P-0 table, row 1)      | reference row; assert match; emit confirmation record (Step 2d).     |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete and the record   |
  |                         | is emitted.                                                          |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table,  |
  | before writing this row | row 2. Phase 2 (Steps 2a-2d): read Step=A-1 + Row type=Failure      |
  | (P-0 table, row 2)      | consequence row; assert match; emit confirmation record (Step 2d).   |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete and the record   |
  |                         | is emitted.                                                          |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

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
```

---

## V-04 -- Role Sequence + Inertia Framing (C-43 Dual-Naming as P-0 Opening Block + C-41 Standalone Table Blocks)

**Axis**: Role sequence + inertia framing -- P-0 opens with dual-naming of both bypass
forms before the abbreviation key, before the token table, and before any phase definition.
The failure taxonomy is the first content the executor encounters: the wrong paths are
named and declared failures before the correct path is defined. C-41 is added as standalone
pre-filled table blocks at both S-3 and A-1. C-42 is not added.
**Hypothesis**: V-02 tested C-43 as a labeled section positioned before the abbreviation
key -- the failure modes are declared structurally prior to the token table. V-04 preserves
this opening position but drops the labeled section form, integrating the dual-naming
directly as the opening paragraph of P-0 before any structural element. The combination
with C-41 standalone blocks tests whether role sequence (failure-modes-first) amplifies the
value of the pre-filled template: if the executor arrives at S-3/A-1 already carrying the
categorical failure frame from P-0, does the standalone block form produce better Phase 2
compliance than either mechanism alone? C-42 is deliberately omitted to isolate the
two-axis combination.
**Predicts**: C-01 through C-41 and C-43 (34 criteria; C-42 not targeted).
**Expected composite**: 34/35 * 10 = 9.71.

---

```
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

An executor who processes a bracket token without reading the Step and Row type cells
has performed only Phase 1. An executor who performs Phase 1 without performing Phase 2
violates this protocol. Locate-only is a protocol failure.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC].

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain. Emit confirmation record
             (table block -- see use-site pre-filled forms at S-3 and A-1).
             DO NOT WRITE THE ROW until both phases pass.

Confirmation record format (table block):

  | Field      | Value                |
  |------------|----------------------|
  | Token      | {token-name}         |
  | Step       | {step-name}          |
  | Row type   | {row-type-name}      |
  | Match      | PASS                 |

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table,  |
  | before writing this row | row 1. Phase 2: read Step=S-3 + Row type=Cross-site reference row;  |
  | (P-0 table, row 1)      | assert match; emit confirmation record (pre-filled table block       |
  |                         | below). DO NOT WRITE THE ROW until both phases pass.                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table,  |
  | before writing this row | row 2. Phase 2: read Step=A-1 + Row type=Failure consequence row;   |
  | (P-0 table, row 2)      | assert match; emit confirmation record (pre-filled table block       |
  |                         | below). DO NOT WRITE THE ROW until both phases pass.                 |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block:

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
```

---

## V-05 -- Full Convergence (C-41 + C-42 + C-43 Maximum Forms; Seeds v16 Use-Site Failure Echo)

**Axis**: Full convergence -- combines V-01's standalone table blocks (C-41), V-03's
numbered Phase 2 lifecycle steps (C-42 form), and V-04's dual-naming opening block (C-43).
All three gate instances carry "until Steps 2a-2d are complete and the record is emitted."
Both use sites carry standalone pre-filled table blocks. The CONFIRMATION REQUIRED rows at
S-3 and A-1 additionally carry a use-site protocol-failure echo naming both bypass forms
at the moment of use -- seeding the v16 aspirational maximum.
**Hypothesis**: No single-axis form tests whether C-41 + C-42 + C-43 compound in the
presence of each other -- each single-axis variation holds the others absent. V-05 tests
whether the three forms reinforce one another: failure taxonomy at entry (C-43 opening),
sequential emit obligation at Phase 2 (C-42 lifecycle), and per-row pre-filled table at
each use site (C-41 standalone). The v16 seed -- per-row use-site echo of both bypass
forms -- tests whether bringing the P-0 failure taxonomy to each bracket-token row removes
the executor's ability to treat the P-0 opening as a prologue to skip during fast execution.
**Predicts**: C-01 through C-43 (35 criteria; full score).
**Expected composite**: 35/35 * 10 = 10.0.
**Seeds v16 aspirational maximum**: use-site protocol-failure echo at every bracket-token
row in the chain (S-3 and A-1 CONFIRMATION rows carry both bypass descriptions and
"Locate-only is a protocol failure" as a per-row reminder, not only in P-0).

---

```
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

An executor who processes a bracket token without reading the Step and Row type cells
has performed only Phase 1. An executor who performs Phase 1 without performing Phase 2
violates this protocol. Locate-only is a protocol failure.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [A-1:FC].

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
  |                         | Protocol reminder: processing this row without reading cells, or     |
  |                         | without performing Phase 2, is a protocol failure.                   |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block (fill Match field only):

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
  |                         | Protocol reminder: processing this row without reading cells, or     |
  |                         | without performing Phase 2, is a protocol failure.                   |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

Confirmation record for this row -- pre-filled table block (fill Match field only):

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
```
