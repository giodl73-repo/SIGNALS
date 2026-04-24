---
skill: quest-variate
skill_target: mock-ns
round: 15
rubric_version: 14
date: 2026-03-15
---

# mock-ns -- Round 15 Variations

Rubric: v14 (C-01 through C-40, aspirational denominator 32).

New criteria in v14 (now pass conditions):
- **C-38** -- Hard-stop gate language: "DO NOT WRITE THE ROW until both phases pass" is
  categorically different from "Confirmation is a prerequisite." Prerequisite framing is an
  ordering constraint; hard-stop is an execution block. Required at all three locations:
  preamble gate definition (P-0), S-3 echo, A-1 echo. All three must carry the hard-stop
  form for a PASS; any location carrying only prerequisite framing fails C-38.
- **C-39** -- Anti-bypass closing statement: a closing note in P-0 names the specific bypass
  being prevented (visual recognition without semantic read) and asserts it as a protocol
  failure. The statement must (a) name the bypass action explicitly, (b) assert it does not
  satisfy the protocol, and (c) distinguish it from Phase 2 completion.
- **C-40** -- Confirmation record output obligation: Phase 2 is not satisfied by a silent
  internal assertion. The executor must emit a confirmation record -- observable output that
  is auditable. The use-site pre-filled template (V-05 aspirational form) seeds the
  maximum: "Phase 1 confirmed: [token] located at P-0 row N. Phase 2 confirmed:
  Step=[X], Row type=[Y]; match=PASS."

R14 converged on C-36/C-37. No variation in R14 simultaneously achieved all three of
C-38, C-39, and C-40 in full form. R15 explores five distinct forms targeting these three
new criteria, varying:
- Where and how the hard-stop language appears (C-38)
- How the anti-bypass statement is positioned (C-39)
- Whether Phase 2 produces an emitted record vs. a silent assertion (C-40)

Three dimensions are tested:
- **Hard-stop register** -- verbatim "DO NOT WRITE THE ROW until both phases pass" at all
  three locations (V-01), vs. sub-section boundary "STOP" form (V-02)
- **Anti-bypass positioning** -- C-39 statement as P-0 closing line (V-01/V-02), vs.
  C-39 as P-0 opening preamble before protocol definition (V-04)
- **Phase 2 output obligation** -- silent assertion (V-01/V-02/V-04) vs. emitted record
  template at use sites (V-03), vs. full convergence with all three (V-05)

Each variation is a **complete, runnable skill body prompt** -- not a diff.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (verbatim hard-stop at all three locations; C-38 only) | The exact phrase "DO NOT WRITE THE ROW until both phases pass" placed at P-0 gate definition AND S-3 echo AND A-1 echo achieves C-38 by repetition. Hypothesis: verbatim repetition at all three sites is the minimum reliable form -- an executor reading the phrase three times at the relevant moments cannot treat Phase 2 as optional without explicitly bypassing a repeated explicit block. Does not add C-39 or C-40; tests C-38 in isolation. |
| V-02 | Lifecycle emphasis (phase sub-sections with explicit stop boundaries in P-0; C-39 closing anti-bypass) | V-01 places hard-stop at all three locations as inline text. V-02 restructures P-0 Phase 1 and Phase 2 as named sub-sections, each with an independent header, and places a dedicated "STOP" line as the closing of Phase 2. C-39 anti-bypass closing statement appears after the STOP line. Hypothesis: sub-section structure makes the two phases visually non-collapsible -- an executor cannot scan past Phase 2 without encountering the STOP header. The anti-bypass closing names the failure mode immediately after the gate, reinforcing that locate-only is insufficient. |
| V-03 | Output format (C-40 confirmation record as pre-filled emit template at both use sites) | V-01 and V-02 achieve C-38 but leave Phase 2 as an internal assertion. V-03 upgrades the S-3 and A-1 use-site echoes to include a pre-filled emit template: the executor must emit a confirmation record with named fields. P-0 defines Phase 2 as "read cells AND emit record." Hypothesis: an emitted record (C-40) converts Phase 2 from a silent check to an auditable output -- an executor who skips Phase 2 cannot produce the record, making the bypass detectable rather than silent. Does not add C-39; tests C-40 in isolation. |
| V-04 | Role sequence + inertia framing (C-39 anti-bypass statement as P-0 opening preamble, before protocol definition) | V-02 places the anti-bypass statement after the STOP line (closing position). V-04 moves it to the opening of P-0 -- before the abbreviation key, before the token table, before any phase definition. The bypass is named first: "Recognizing a token in this table without reading the Step and Row type cells is a locate-only operation. An executor who performs only Phase 1 has not satisfied this protocol." Then the protocol is defined. Hypothesis: leading with the bypass name activates a rejection frame before the protocol is encountered -- an executor who reads the opening knows what failure looks like before learning the success path, reducing the risk of collapsing the two phases during fast execution. |
| V-05 | Full convergence (C-38 hard-stop at all three locations + C-39 anti-bypass + C-40 emit record; seeds v15 maximum) | Combines V-01's hard-stop register, V-02's STOP sub-section structure, V-04's opening anti-bypass preamble, and V-03's pre-filled emit template at both use sites. P-0: opens with named bypass (C-39), defines phases as sub-sections with STOP boundary, closes Phase 2 with hard-stop and emit-record obligation (C-38 + C-40). S-3 echo: hard-stop + pre-filled template. A-1 echo: hard-stop + pre-filled template. This is the aspirational maximum for v15: every gate, every echo, every confirmation is both a hard block and an emitted observable record. |

---

## V-01 -- Phrasing Register (Verbatim Hard-Stop at All Three Locations)

**Axis**: Phrasing register -- the C-38 hard-stop phrase "DO NOT WRITE THE ROW until both
phases pass" appears verbatim at all three required locations: (1) the P-0 gate definition
closing line, (2) the S-3 bracket-token echo row, (3) the A-1 bracket-token echo row.
C-39 anti-bypass and C-40 confirmation record are not added. Tests C-38 in isolation.
**Hypothesis**: Verbatim repetition of the hard-stop phrase at all three locations produces
C-38 more reliably than prerequisite framing (R14 V-01) or use-site-only blocker language
(R14 V-02). The phrase functions as a literal execution gate -- an executor who reads it
three times at the three relevant moments cannot treat Phase 2 as advisory without
explicitly overriding a repeated block. Single-axis isolation allows clean attribution: if
C-38 fails, it is not masked by the presence or absence of C-39/C-40.
**Predicts**: C-01 through C-38 -- 30 criteria (C-39 and C-40 not targeted).
**Expected composite**: 30/32 aspirational = 93.8.

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

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain.

  DO NOT WRITE THE ROW until both phases pass.

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table;  |
  | before writing this row | Phase 2: read Step=S-3 + Row type=Cross-site reference row;         |
  | (P-0 table, row 1)      | assert match. DO NOT WRITE THE ROW until both phases pass.          |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at           |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row       |
  |                         | identifies itself as this row's mutual target)                      |

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table;  |
  | before writing this row | Phase 2: read Step=A-1 + Row type=Failure consequence row;          |
  | (P-0 table, row 2)      | assert match. DO NOT WRITE THE ROW until both phases pass.          |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]        |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to     |
  |                         | downstream tooling that silently corrupts the artifact's trust tier;|
  |                         | the corruption is undetectable without manual header inspection      |

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

## V-02 -- Lifecycle Emphasis (Phase Sub-Sections with STOP Boundary; C-39 Anti-Bypass Closing)

**Axis**: Lifecycle emphasis -- P-0 restructures the two-phase gate as named sub-sections
with explicit headers ("Phase 1 -- Locate" / "Phase 2 -- Confirm"). Phase 2 closes with a
dedicated STOP line. The C-39 anti-bypass closing statement follows the STOP line,
immediately after the gate. Use-site echoes at S-3 and A-1 carry the same sub-section
structure in compact form, each ending with the hard-stop.
**Hypothesis**: V-01 places hard-stop as an inline closing phrase. V-02 tests whether
sub-section visual structure makes the gate physically non-collapsible -- each phase
occupies a labeled section that cannot be absorbed into a single scan pass. The STOP line
is a visual anchor that forces re-entry into Phase 2 awareness. The C-39 anti-bypass
statement following STOP names the specific failure mode at the moment of maximum gate
salience, immediately after the hard-stop reinforces it. Combined effect: the bypass is
both visually blocked and explicitly named at the same location.
**Predicts**: C-01 through C-39 -- 31 criteria (C-40 not targeted).
**Expected composite**: 31/32 aspirational = 96.9.

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

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate
    Find the row in the table above by matching the token name.

  Phase 2 -- Confirm
    Read the Step cell. Read the Row type cell.
    Assert: the step name matches the step you are currently writing.
    Assert: the row type name matches the role of this row in the chain.
    STOP. DO NOT WRITE THE ROW until both phases pass.

  An executor who recognizes a token without performing Phase 2 has not satisfied
  this protocol. Locate-only is a Phase 1 result; it does not satisfy the gate.

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
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table.                              |
  | before writing this row | Phase 2: read Step=S-3 + Row type=Cross-site reference row;         |
  | (P-0 table, row 1)      | assert match. STOP. DO NOT WRITE THE ROW until both phases pass.    |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at           |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row       |
  |                         | identifies itself as this row's mutual target)                      |

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
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table.                              |
  | before writing this row | Phase 2: read Step=A-1 + Row type=Failure consequence row;          |
  | (P-0 table, row 2)      | assert match. STOP. DO NOT WRITE THE ROW until both phases pass.    |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]        |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to     |
  |                         | downstream tooling that silently corrupts the artifact's trust tier;|
  |                         | the corruption is undetectable without manual header inspection      |

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

## V-03 -- Output Format (C-40 Confirmation Record as Pre-Filled Emit Template)

**Axis**: Output format -- P-0 defines Phase 2 as requiring an emitted confirmation record,
not merely a silent assertion. S-3 and A-1 use-site echoes each include a pre-filled
template that the executor must emit before writing the row. The template has named fields:
Phase 1 confirmed: [token] located at P-0 row N. Phase 2 confirmed: Step=[X], Row
type=[Y]; match=PASS. C-39 anti-bypass is not added. C-38 hard-stop is present at all
three locations.
**Hypothesis**: Silent Phase 2 (C-36/C-37 as in R14) is internally satisfied but externally
unverifiable. An executor who reads the Step and Row type cells silently passes Phase 2
without leaving a trace. A pre-filled emit template converts Phase 2 from an assertion to
an observable record -- an executor who skips Phase 2 cannot produce the correct field
values in the record, making the bypass detectable. The template also forces a momentary
pause (filling in the fields) that prevents collapse of Phase 1 and Phase 2 into a single
fast-scan. This tests C-40 in isolation while maintaining C-38 at all three locations.
**Predicts**: C-01 through C-38, C-40 -- 31 criteria (C-39 not targeted).
**Expected composite**: 31/32 aspirational = 96.9.

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

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain. Emit confirmation record:
               Phase 1 confirmed: {token} located at P-0 row {N}.
               Phase 2 confirmed: Step={step}, Row type={row-type}; match=PASS.
             DO NOT WRITE THE ROW until both phases pass and the record is emitted.

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table;  |
  | before writing this row | Phase 2: read Step=S-3 + Row type=Cross-site reference row; assert  |
  | (P-0 table, row 1)      | match; emit record: "Phase 1 confirmed: [S-3:CS] at P-0 row 1.     |
  |                         | Phase 2 confirmed: Step=S-3, Row type=Cross-site reference row;     |
  |                         | match=PASS." DO NOT WRITE THE ROW until both phases pass.           |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at           |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row       |
  |                         | identifies itself as this row's mutual target)                      |

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table;  |
  | before writing this row | Phase 2: read Step=A-1 + Row type=Failure consequence row; assert   |
  | (P-0 table, row 2)      | match; emit record: "Phase 1 confirmed: [A-1:FC] at P-0 row 2.     |
  |                         | Phase 2 confirmed: Step=A-1, Row type=Failure consequence row;      |
  |                         | match=PASS." DO NOT WRITE THE ROW until both phases pass.           |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]        |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to     |
  |                         | downstream tooling that silently corrupts the artifact's trust tier;|
  |                         | the corruption is undetectable without manual header inspection      |

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

## V-04 -- Role Sequence + Inertia Framing (C-39 Anti-Bypass as P-0 Opening Preamble)

**Axis**: Role sequence + inertia framing -- P-0 opens with the C-39 anti-bypass statement
before the abbreviation key, before the token table, before any phase definition. The
bypass is named first: "Recognizing a token without reading the Step and Row type cells
is a locate-only operation. An executor who performs only Phase 1 has not satisfied this
protocol." The phases are then defined, and Phase 2 closes with the hard-stop. Use-site
echoes carry the hard-stop form.
**Hypothesis**: V-02 places the anti-bypass statement after the gate (closing position) --
the failure mode is named after the success path is defined. V-04 inverts this: the failure
mode is named before the protocol, creating a rejection frame before the executor encounters
the phases. An executor who reads the opening knows that fast-scan locate-only is a named
failure; they then read the protocol as the correct alternative. Inertia framing: the
status-quo path (visual recognition) is called out at the top before the executor can
adopt it. This tests whether the anti-bypass statement is more effective as a precondition
frame (opening) than as a consequence note (closing).
**Predicts**: C-01 through C-39 -- 31 criteria (C-40 not targeted).
**Expected composite**: 31/32 aspirational = 96.9.

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

Recognizing a token in the table below without reading the Step and Row type cells is a
locate-only operation (Phase 1 only). An executor who performs only Phase 1 has not
satisfied this protocol. Locate-only does not satisfy the confirmation gate.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain.
             DO NOT WRITE THE ROW until both phases pass.

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [S-3:CS] in P-0 table;  |
  | before writing this row | Phase 2: read Step=S-3 + Row type=Cross-site reference row;         |
  | (P-0 table, row 1)      | assert match. DO NOT WRITE THE ROW until both phases pass.          |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at           |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row       |
  |                         | identifies itself as this row's mutual target)                      |

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
  | CONFIRMATION REQUIRED   | Before writing this row -- Phase 1: locate [A-1:FC] in P-0 table;  |
  | before writing this row | Phase 2: read Step=A-1 + Row type=Failure consequence row;          |
  | (P-0 table, row 2)      | assert match. DO NOT WRITE THE ROW until both phases pass.          |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]        |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to     |
  |                         | downstream tooling that silently corrupts the artifact's trust tier;|
  |                         | the corruption is undetectable without manual header inspection      |

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

## V-05 -- Full Convergence (C-38 + C-39 + C-40; Seeds v15 Maximum)

**Axis**: Full convergence -- all three new criteria at their aspirational maximum. P-0:
opens with the C-39 anti-bypass preamble (named bypass before protocol definition); Phase 2
sub-section closes with STOP + DO NOT WRITE hard-stop (C-38 at preamble gate); defines
Phase 2 as requiring an emitted confirmation record (C-40). S-3 echo: hard-stop + pre-filled
emit template. A-1 echo: hard-stop + pre-filled emit template. This is the aspirational
maximum for v15.
**Hypothesis**: V-01 isolated C-38; V-02 combined C-38 + C-39 (closing position); V-03
isolated C-40; V-04 combined C-38 + C-39 (opening position). V-05 combines all three.
The full convergence form is the strongest gate: (1) the executor's bypass reflex is
rejected by name before they read the protocol; (2) Phase 2 is a named sub-section with
a physical STOP boundary that cannot be collapsed; (3) the confirmation record must be
emitted at the use site, making Phase 2 externally auditable. Any single bypass path
(visual recognition, skipped Phase 2, silent assertion) fails at least two independent
mechanisms. Expected to achieve 32/32, seeding the v15 denominator and the reference
form for subsequent rounds.
**Predicts**: C-01 through C-40 -- all 32 criteria.
**Expected composite**: 32/32 aspirational = 100.

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

Recognizing a token in the table below without reading the Step and Row type cells is a
locate-only operation (Phase 1 only). An executor who recognizes a token without
performing Phase 2 has not satisfied this protocol. Locate-only is a protocol failure.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate
    Find the row in the table above by matching the token name.

  Phase 2 -- Confirm
    Read the Step cell. Read the Row type cell.
    Assert: the step name matches the step you are currently writing.
    Assert: the row type name matches the role of this row in the chain.
    Emit confirmation record:
      Phase 1 confirmed: {token} located at P-0 row {N}.
      Phase 2 confirmed: Step={step}, Row type={row-type}; match=PASS.
    STOP. DO NOT WRITE THE ROW until both phases pass and the record is emitted.

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
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2: read Step=S-3 +    |
  | before writing this row | Row type=Cross-site reference row; assert match; emit record:       |
  | (P-0 table, row 1)      | "Phase 1 confirmed: [S-3:CS] at P-0 row 1. Phase 2 confirmed:      |
  |                         | Step=S-3, Row type=Cross-site reference row; match=PASS."           |
  |                         | DO NOT WRITE THE ROW until both phases pass and record is emitted.  |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at           |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row       |
  |                         | identifies itself as this row's mutual target)                      |

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
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table. Phase 2: read Step=A-1 +    |
  | before writing this row | Row type=Failure consequence row; assert match; emit record:        |
  | (P-0 table, row 2)      | "Phase 1 confirmed: [A-1:FC] at P-0 row 2. Phase 2 confirmed:      |
  |                         | Step=A-1, Row type=Failure consequence row; match=PASS."            |
  |                         | DO NOT WRITE THE ROW until both phases pass and record is emitted.  |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]        |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to     |
  |                         | downstream tooling that silently corrupts the artifact's trust tier;|
  |                         | the corruption is undetectable without manual header inspection      |

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
