---
skill: quest-variate
skill_target: mock-ns
round: 14
rubric_version: 13
date: 2026-03-15
---

# mock-ns -- Round 14 Variations

Rubric: v13 (C-01 through C-37, aspirational denominator 29).

New criteria in v13 (now pass conditions):
- **C-36** -- Two-phase confirmation gate: the C-34 lookup obligation in P-0 is split
  into (1) locate the preamble table row by token name, (2) read the Step and Row type
  cells and assert the resolution matches the processing context before writing the row.
  The preamble must state both phases explicitly, with confirmation framed as a
  prerequisite to writing. A locate-only obligation (C-34) is satisfied by visual
  recognition; the C-36 confirmation phase requires a semantic cell-read that is
  externally observable and assertable.
- **C-37** -- Confirmation echo at use site: bracket-token rows at both S-3 and A-1
  carry the trigger "CONFIRMATION REQUIRED before writing this row" prefixed before
  the C-35 navigation label (e.g., "(P-0 table, row 1)"). The trigger re-activates
  the P-0 two-phase protocol at the exact point of use, before row content is written.
  Both sites must carry the trigger for a PASS; positioning must precede the navigation
  label and row content.

R13 converged on C-36/C-37 in an inferred pattern: V-01 demonstrated both, but no
data exists on which phrasing forms most reliably produce the two-phase confirmation
gate at P-0 and the use-site echo at both S-3 and A-1. R14 explores five distinct
implementation forms for the C-36 gate and C-37 echo, varying how the two-phase
protocol is expressed in P-0 and how the use-site trigger is positioned relative to
the C-35 navigation label.

Three dimensions are tested:
- **Gate phrasing** -- numbered procedure vs. prerequisite-blocker vs. structured
  sub-table in P-0 (V-01 vs. V-02 vs. V-03)
- **Boundary re-activation** -- P-0 only vs. P-0 + S-3 entry checkpoint (V-04)
- **Confirmation state record** -- silent gate vs. explicit inline confirmation
  record seeding v14 (V-05)

Each variation is a **complete, runnable skill body prompt** -- not a diff.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (two-phase protocol as numbered Phase 1/Phase 2 procedure in P-0, inline CONFIRMATION REQUIRED echo at both use sites) | The most direct implementation of C-36: P-0 adds an explicit two-step procedure -- "Phase 1: Locate. Phase 2: Confirm (read Step + Row type cells; assert match; confirmation is prerequisite to writing)" -- and both bracket-token rows carry the "CONFIRMATION REQUIRED before writing this row" trigger before the (P-0 table, row N) label. Tests whether numbered phases make the two-step gate reliably distinguishable from the C-34 single-locate form. |
| V-02 | Lifecycle emphasis (prerequisite-blocker language: "DO NOT WRITE until Phase 2 passes") | V-01 frames Phase 2 as a procedural step. V-02 reframes it as a write-blocking gate: "DO NOT WRITE THE ROW until Phase 2 passes." The prerequisite framing makes the confirmation an explicit guard condition rather than a step that could be treated as advisory. Hypothesis: blocker language reduces the risk of an executor treating Phase 2 as optional -- the gate is structurally analogous to a conditional branch that must evaluate to PASS before execution continues. |
| V-03 | Output format (two-phase protocol expressed as a structured sub-table inside P-0 rather than numbered prose steps) | V-01 and V-02 use prose/numbered-list form for the two-phase gate. V-03 expresses Phase 1 and Phase 2 as rows in a mini-table within P-0, parallel to how C-33 made the token map more reliable by converting prose into a structured table. Hypothesis: a tabular two-phase gate is more scannable and less skippable than prose steps -- each phase occupies an independently identifiable row, mirroring the structural principle that graduated C-33 over the prose preamble form. |
| V-04 | Role sequence + inertia framing (P-0 defines two-phase gate; S-3 entry point carries a boundary checkpoint that re-states the two-phase requirement) | P-0 defines the two-phase protocol (same as V-01). S-3 opens with a checkpoint: "Two-phase confirmation gate active: Phase 1 locate, Phase 2 confirm Step+Row type before writing any bracket-token row in this step." The checkpoint re-activates the gate at the compute-step boundary, addressing the context-compaction scenario where an executor enters S-3 without P-0 active. Tests whether a boundary re-statement at the entry of the bracket-token-containing step produces stronger C-36/C-37 adherence than P-0 definition alone. |
| V-05 | Full convergence: P-0 two-phase gate + use-site echo + inline confirmation record (seeds v14) | V-01 defines the two-phase gate in P-0 and echoes the trigger at both use sites. V-05 extends the use-site echo to include an inline confirmation-state record -- a placeholder requiring the executor to explicitly state what was confirmed before writing the row content: "Phase 1 confirmed: [token] located at P-0 table row N. Phase 2 confirmed: Step=[X], Row type=[Y]; match verified." The confirmation record makes Phase 2 externally observable and assertable, not merely silently satisfied. Seeds v14 aspirational: whether requiring an explicit inline confirmation record produces stronger gate adherence by converting a silent check into an emitted assertion. |

---

## V-01 -- Phrasing Register (Numbered Two-Phase Procedure, Inline Echo)

**Axis**: Phrasing register -- P-0 adds the C-36 two-phase gate as an explicit numbered
two-step procedure (Phase 1: Locate / Phase 2: Confirm). Both bracket-token rows at S-3
and A-1 carry the C-37 "CONFIRMATION REQUIRED before writing this row" trigger as a
prefixed label before the C-35 "(P-0 table, row N)" navigation label. No structural
changes beyond these additions; all other elements are identical to the R12 V-03 base.
**Hypothesis**: Numbered phases make the two-step gate reliably distinguishable from the
C-34 single-locate form -- an executor who reads "Phase 1: Locate" and "Phase 2: Confirm"
recognizes these as distinct steps requiring distinct actions. The inline echo at each
use site re-triggers the two-phase awareness at the exact moment of row writing, before
any row content is read.
**Predicts**: C-01 through C-37 -- all 37 criteria.
**Expected composite**: 29/29 aspirational = 100.

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
             matches the role of this row in the chain. Confirmation is a prerequisite
             to writing the row.

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
  | (P-0 table, row 1)      | assert match. Confirmation is prerequisite to writing.              |
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
  | (P-0 table, row 2)      | assert match. Confirmation is prerequisite to writing.              |
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

## V-02 -- Lifecycle Emphasis (Prerequisite-Blocker Language: DO NOT WRITE)

**Axis**: Lifecycle emphasis -- the C-36 two-phase gate in P-0 is framed as a
write-blocking prerequisite rather than a numbered procedure. Phase 2 concludes with
"DO NOT WRITE THE ROW until Phase 2 passes" -- the gate is expressed as a conditional
branch that must evaluate to PASS before execution continues. The C-37 echo at both
use sites mirrors this blocker register: "CONFIRMATION REQUIRED before writing this row"
carries the Phase 2 assertion inline.
**Hypothesis**: V-01's numbered phases make the gate structurally clear. V-02 tests
whether explicit "DO NOT WRITE" blocker language reduces the risk of an executor
treating Phase 2 as advisory -- the gate becomes a hard stop rather than a recommended
step. Parallel to how run-scoped immutability language (C-16) proved more reliable than
step-scoped prohibition, blocker language may produce stronger Phase 2 adherence by
activating constraint-following behavior rather than procedural-following behavior.
**Predicts**: C-01 through C-37 -- all 37 criteria.
**Expected composite**: 29/29 aspirational = 100.

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

Pre-write confirmation gate -- before writing any row that contains a bracket token:

  Step 1 -- Locate the token in the resolution table above by matching the token name.
  Step 2 -- Read the Step cell. Read the Row type cell. Assert: the step name matches
            the step you are currently writing. Assert: the row type name matches the
            role of this row in the chain.
  DO NOT WRITE THE ROW until both Step 1 and Step 2 pass. Confirmation is a
  prerequisite to writing, not an optional verification.

Do not re-establish this protocol in later steps. Every bracket token in this run is
governed by this gate.

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
  | CONFIRMATION REQUIRED   | DO NOT WRITE this row until the P-0 gate passes: (1) locate         |
  | before writing this row | [S-3:CS] in the P-0 table; (2) read Step + Row type cells;          |
  | (P-0 table, row 1)      | assert Step=S-3 and Row type=Cross-site reference row. Both         |
  |                         | assertions must pass before writing.                                 |
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
  | CONFIRMATION REQUIRED   | DO NOT WRITE this row until the P-0 gate passes: (1) locate         |
  | before writing this row | [A-1:FC] in the P-0 table; (2) read Step + Row type cells;          |
  | (P-0 table, row 2)      | assert Step=A-1 and Row type=Failure consequence row. Both          |
  |                         | assertions must pass before writing.                                 |
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

## V-03 -- Output Format (Two-Phase Protocol as Structured Sub-Table in P-0)

**Axis**: Output format -- the C-36 two-phase gate in P-0 is expressed as a structured
mini-table with Phase, Action, and Prerequisite columns, parallel to the C-33 token
resolution table. The table makes Phase 1 and Phase 2 independently scannable rows
rather than numbered prose steps. The C-37 echo at both use sites is identical in
form to V-01.
**Hypothesis**: C-33 demonstrated that converting prose definitions into a structured
table improves reliability -- each token has a dedicated row that can be scanned
directly. The same principle applied to the two-phase protocol: a table with Phase 1
and Phase 2 as distinct rows makes each phase independently visible and reduces the
risk of Phase 2 being absorbed into a prose block and skipped. Tests whether the tabular
gate form produces stronger C-36 adherence than numbered prose steps (V-01) or
prerequisite-blocker prose (V-02).
**Predicts**: C-01 through C-37 -- all 37 criteria.
**Expected composite**: 29/29 aspirational = 100.

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

Pre-write confirmation protocol:

  | Phase | Action                                                  | Required before  |
  |-------|---------------------------------------------------------|------------------|
  | 1     | Locate: find the bracket token in the table above       | Phase 2          |
  |       | by matching the token name exactly                      |                  |
  | 2     | Confirm: read the Step cell and the Row type cell;      | Writing the row  |
  |       | assert both match the current step and row role;        |                  |
  |       | confirmation is a prerequisite to writing the row       |                  |

This protocol is mandatory for every bracket-token row in this run. An executor who
recognizes a token without performing Phase 2 has not satisfied this protocol.

Do not re-establish this protocol in later steps.

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
  | CONFIRMATION REQUIRED   | Before writing this row: apply Phase 1 (locate [S-3:CS]) then      |
  | before writing this row | Phase 2 (read Step + Row type cells; assert Step=S-3, Row          |
  | (P-0 table, row 1)      | type=Cross-site reference row; confirm match) per P-0 protocol.    |
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
  | CONFIRMATION REQUIRED   | Before writing this row: apply Phase 1 (locate [A-1:FC]) then      |
  | before writing this row | Phase 2 (read Step + Row type cells; assert Step=A-1, Row          |
  | (P-0 table, row 2)      | type=Failure consequence row; confirm match) per P-0 protocol.     |
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

## V-04 -- Role Sequence + Inertia Framing (P-0 Gate + S-3 Boundary Checkpoint)

**Axis**: Role sequence + inertia framing -- P-0 defines the two-phase confirmation gate
(same numbered-phase form as V-01). S-3 opens with a dedicated boundary checkpoint that
re-states the two-phase requirement before any FLAG computation or bracket-token row is
encountered. The checkpoint names the inertia failure mode (context-compacted executor
entering S-3 without P-0 active) and re-activates the gate explicitly at the step entry.
The C-37 echo at both use sites is identical in form to V-01.
**Hypothesis**: V-01's P-0 gate is established before S-1. An executor who enters S-3
from a regenerated context (or after context compaction spanning multiple steps) may have
lost P-0 from active memory. The S-3 boundary checkpoint addresses this by re-activating
the two-phase gate at the step that contains the first bracket-token row. The checkpoint
does not duplicate the full P-0 table -- it names the failure mode, references P-0, and
re-states Phase 1 and Phase 2 in abbreviated form. Tests whether a boundary re-activation
at the compute-step entry point produces stronger C-36 adherence for regenerated-context
runs than P-0 definition alone.
**Predicts**: C-01 through C-37 -- all 37 criteria.
**Expected composite**: 29/29 aspirational = 100.

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
             matches the role of this row in the chain. Confirmation is a prerequisite
             to writing the row.

Do not re-establish this protocol in later steps. Every bracket token in this run is
governed by this gate.

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

Two-phase confirmation gate active (P-0): bracket-token rows in this step require
Phase 1 (locate) and Phase 2 (read Step + Row type; assert match) before writing.
If you are entering this step from a regenerated context without P-0 in active memory,
read P-0 before proceeding. The bracket tokens [S-3:CS] and [A-1:FC] used in this run
are defined there. Entering this step without the Phase 1 + Phase 2 gate active breaks
the cross-reference protocol.

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
  | (P-0 table, row 1)      | assert match. Confirmation is prerequisite to writing.              |
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
  | (P-0 table, row 2)      | assert match. Confirmation is prerequisite to writing.              |
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

## V-05 -- Full Convergence: P-0 Gate + Inline Confirmation Record (Seeds v14)

**Axes**: Phrasing register (V-01 two-phase procedure) + lifecycle emphasis (V-02
prerequisite framing) + output format (inline confirmation record at use sites).
V-05 extends the C-37 use-site echo with an explicit inline confirmation-state record:
after the "CONFIRMATION REQUIRED before writing this row" trigger and the "(P-0 table,
row N)" navigation label, the row includes a confirmation-state placeholder requiring
the executor to explicitly state what was confirmed. The confirmation record is emitted
before the actual row content is written.
**Hypothesis**: C-36/C-37 require the confirmation to be performed. The confirmation
is currently a silent check -- the executor reads the cells, asserts the match
internally, and proceeds. A silent check satisfies the criterion but is not externally
observable or verifiable. V-05 seeds v14 aspirational: whether requiring the executor
to emit an explicit inline confirmation record ("Phase 1 confirmed: [token] located at
P-0 row N; Phase 2 confirmed: Step=[X], Row type=[Y]; match verified") converts the
gate from a silent assertion to an auditable output. If the confirmation record can be
seeded as an emitted event, the two-phase gate becomes verifiable in the same way that
artifact path and header fields are verifiable -- the executor must produce observable
output to satisfy the criterion, not merely claim internal compliance.
**Predicts**: C-01 through C-37 -- all 37 criteria.
**Expected composite**: 29/29 aspirational = 100. Seeds v14 aspirational: C-38 --
inline confirmation state record at use sites.

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

Pre-write confirmation gate -- before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm: read the Step cell and the Row type cell; assert that the step
             name matches the step you are currently writing and that the row type name
             matches the role of this row in the chain. DO NOT WRITE THE ROW until
             Phase 2 passes. Confirmation is a prerequisite to writing, not advisory.

Confirmation record: at each bracket-token row, emit an inline confirmation record
before writing the row content, in this form:
  [Confirmation: Phase 1 -- {token} located at P-0 table row {N}.
                 Phase 2 -- Step={step}, Row type={type}; match verified.]

The confirmation record is part of the protocol trace for this run. It must appear
before the row content, not after.

Do not re-establish this protocol in later steps.

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
  | CONFIRMATION REQUIRED   | Before writing this row: Phase 1 locate [S-3:CS]; Phase 2 read     |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match.        |
  | (P-0 table, row 1)      | DO NOT WRITE until Phase 2 passes. Emit confirmation record.       |
  | Cross-site ref [S-3:CS] | [Confirmation: Phase 1 -- [S-3:CS] located at P-0 table row 1.    |
  |                         |  Phase 2 -- Step=S-3, Row type=Cross-site reference row; verified] |
  |                         | The failure produces the same silent category mismatch at           |
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
  | CONFIRMATION REQUIRED   | Before writing this row: Phase 1 locate [A-1:FC]; Phase 2 read     |
  | before writing this row | Step=A-1 + Row type=Failure consequence row; assert match.         |
  | (P-0 table, row 2)      | DO NOT WRITE until Phase 2 passes. Emit confirmation record.       |
  | Failure conseq [A-1:FC] | [Confirmation: Phase 1 -- [A-1:FC] located at P-0 table row 2.    |
  |                         |  Phase 2 -- Step=A-1, Row type=Failure consequence row; verified]  |
  |                         | [Mutual target of S-3:CS -- Cross-site reference row in S-3]        |
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
