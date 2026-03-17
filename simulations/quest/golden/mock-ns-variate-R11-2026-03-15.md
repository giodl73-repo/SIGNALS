---
skill: quest-variate
skill_target: mock-ns
round: 11
rubric_version: 10
date: 2026-03-15
---

# mock-ns -- Round 11 Variations

Rubric: v10 (C-01 through C-31, aspirational denominator 23).

New criteria in v10 (now pass conditions):
- **C-29** -- Bidirectional navigation anchor: A-1 Failure consequence row carries an explicit
  self-identification marker naming S-3 as the source of the cross-reference. 4/5 R10 variants
  demonstrated this (V-01, V-02, V-04, V-05). V-03 (forward-only) passed C-28 but failed C-29.
- **C-30** -- Bracket token notation at both sites: `[A-1:FC]` in the forward direction and
  `[S-3:CS]` in the backward direction. V-02 and V-05 demonstrated this. Reduces navigation
  cost from prose parsing to token matching.
- **C-31** -- Pre-chain protocol preamble: a dedicated orientation block before all prohibition
  rows names every token pair, states what each resolves to, and maps the complete bidirectional
  link structure before any row is read. V-05 uniquely demonstrated this.

R10 converged on C-29 through C-31 in a 4/5 / 2/5 / 1/5 pass pattern respectively. C-31 is
the current convergence bottleneck -- only V-05 satisfied it, and V-05's preamble was a prose
block embedded mid-step inside S-3 (after the computation cases, before the chain). R11's
question is structural: given that a pre-chain preamble is now required, which preamble form
produces the most robust adherence?

Three dimensions of the preamble are tested:
- **Position** -- where in the prompt the preamble sits (V-01: top of S-3; V-02/V-03: same as
  R10 V-05; V-04/V-05: promoted to a numbered step before S-1)
- **Format** -- prose vs. table (V-02: token resolution table replaces V-05's prose preamble)
- **Register** -- declarative/protocol vs. conversational/explanatory (V-03)

V-04 and V-05 combine axes into a P-0 step. V-05 additionally seeds the v11 aspirational:
whether defining the token abbreviation system (`:CS` = Cross-site reference row, `:FC` =
Failure consequence row) as explicit named vocabulary in the protocol step produces measurably
stronger chain adherence than treating the abbreviations as contextually self-evident.

Each variation is a **complete, runnable skill body prompt** -- not a diff.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (preamble at top of S-3, before computation cases) | R10 V-05 places the preamble between the computation cases and the immutability chain. An executor processing S-3 encounters FLAG computation logic before the cross-reference protocol is established. V-01 moves the preamble to the very top of S-3 -- the first statement of the step -- so protocol context is present before any computation begins. The executor carries the token map through the computation cases and into the chain. Tests whether pre-computation placement produces stronger C-31 adherence than V-05's post-computation placement. |
| V-02 | Output format (preamble as token resolution table) | R10 V-05's preamble is prose. Prose requires sequential parsing to extract token-resolution information; a structured table makes each token independently scannable. V-02 replaces the prose preamble with a two-part table: an abbreviation key (`:CS` / `:FC`) and a resolution table (Token / Resolves to / Paired token / Direction). Same structural position as V-05 (after computation cases, before chain). Tests whether tabular resolution enables faster token orientation than prose description at identical preamble position. |
| V-03 | Phrasing register (conversational/explanatory framing) | R10 V-05 uses declarative protocol language ("S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual navigation anchors... Both directions are active. An executor entering at either site reaches the other without inference"). V-03 uses an explanatory register that names the purpose: if you arrive at A-1 without S-3 in active context, `[A-1:FC]` at A-1 confirms this is the row S-3's cross-site reference named -- you do not need to re-read S-3. Same position as V-05. Tests whether purpose-first framing produces stronger adherence than protocol-declaration framing for an identical preamble position. |
| V-04 | Combined: role sequence (preamble as numbered step P-0) + output format (abbreviation glossary table) | The cross-reference protocol is promoted from an embedded block within S-3 to a first-class numbered step (P-0 -- CROSS-REFERENCE PROTOCOL) before S-1. P-0 defines the token abbreviation system and enumerates all active token pairs before any execution begins. Every subsequent bracket token in the run is pre-explained before the first step runs. Tests whether step-level protocol elevation -- the executor carries the token map from the very start of the run rather than first encountering it mid-S-3 -- produces stronger C-31 adherence than embedded preamble. Full convergence target: all 31 criteria. |
| V-05 | Full convergence: P-0 + abbreviation glossary table + resolution table + explanatory framing | V-04's P-0 step extended with a two-part structure: an abbreviation table (`:CS` / `:FC` defined as named row-type vocabulary) followed by a token resolution table with Direction cells, plus a brief explanatory sentence. Seeds v11 aspirational: whether explicitly defining abbreviation meaning at P-0 -- making every bracket token in the run self-documenting from the glossary -- produces measurably stronger chain adherence than treating `:CS` and `:FC` as contextually-inferred abbreviations. Full convergence target: all 31 criteria. |

---

## V-01 -- Lifecycle Emphasis (Preamble at Top of S-3)

**Axis**: Lifecycle emphasis -- the cross-reference protocol preamble is the first statement
of S-3, before the FLAG computation cases. In R10 V-05, the preamble appears after the Cases
block and before the chain. V-01 moves it before the Cases block: an executor who opens S-3
sees the token map before they see any computation logic.
**Hypothesis**: An executor entering S-3 in a regenerated context encounters the computation
cases first in V-05's form, potentially processing them before registering the preamble that
follows. Moving the preamble to the top of S-3 ensures the protocol context is active before
any computation -- the executor associates the bracket tokens with the chain rows they will
encounter, rather than encountering the tokens in the chain before the preamble orients them.
All other structure matches R10 V-05 exactly.
**Predicts**: C-01 through C-31 -- all 31 criteria.
**Expected composite**: 23/23 aspirational = 100.

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

Cross-reference protocol: S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual navigation
anchors. [S-3:CS] names [A-1:FC] as its forward target. [A-1:FC] names [S-3:CS]
as its backward source. Both directions are active. An executor entering at either
anchor reaches the other without inference. This protocol is established here --
at the top of this step, before any computation or chain row -- and governs the
remainder of this run.

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
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                       |

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

## V-02 -- Output Format (Preamble as Token Resolution Table)

**Axis**: Output format -- the cross-reference protocol preamble is a structured table rather
than prose. Same structural position as R10 V-05 (after computation cases, before the chain).
The table has two parts: an abbreviation key defining `:CS` and `:FC`, and a resolution table
mapping each token to its step, row type, paired token, and direction.
**Hypothesis**: R10 V-05's prose preamble ("S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual
navigation anchors. S-3 Cross-site reference row names A-1 Failure consequence row by step and
row label. A-1 Failure consequence row names S-3 Cross-site reference row by step and row
label. Both directions are active.") requires sequential reading to extract the token-resolution
map. A table enables O(1) lookup: an executor who wants to know what [S-3:CS] resolves to
reads one row, not a paragraph. The abbreviation key additionally makes `:CS` and `:FC` named
terms rather than opaque suffixes -- an executor who encounters `[A-1:FC]` in the chain can
immediately decode it as "Failure consequence row" without parsing surrounding prose. Tests
whether tabular preamble format reduces token misidentification relative to prose description
at the same structural position.
**Predicts**: C-01 through C-31 -- all 31 criteria.
**Expected composite**: 23/23 aspirational = 100.

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

Cross-reference protocol: token resolution table.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction            |
  |----------|------|---------------------------|--------------|----------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1|
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names  |
  |          |      |                           |              | S-3 as source        |

Both anchors are active. An executor entering at either token finds its pair by
reading the Direction cell. No prior traversal required.

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
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                       |

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

## V-03 -- Phrasing Register (Conversational/Explanatory Framing)

**Axis**: Phrasing register -- the cross-reference protocol preamble uses conversational,
purpose-first language instead of R10 V-05's declarative protocol language. Same structural
position (after computation cases, before chain). The preamble explains why the anchors exist
rather than stating that they exist.
**Hypothesis**: R10 V-05's preamble is a protocol declaration: "S-3 [S-3:CS] and A-1 [A-1:FC]
carry mutual navigation anchors... Both directions are active. An executor entering at either
site reaches the other without inference." This form states the mechanism without explaining
its purpose. An executor processing the preamble under cognitive load may register that a
protocol exists without understanding why it matters. V-03 names the scenario the protocol
solves: if A-1 is regenerated without S-3 in active context, [A-1:FC] at A-1 tells the
executor that a corresponding cross-site reference exists at [S-3:CS] in S-3 -- the link is
discoverable from A-1 alone. Similarly, [S-3:CS] at S-3 names where to look at A-1 without
re-scanning the document. Tests whether purpose-first framing produces stronger adherence than
mechanism-declaration framing for the same preamble position.
**Predicts**: C-01 through C-31 -- all 31 criteria.
**Expected composite**: 23/23 aspirational = 100.

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

Two rows in this run carry bracket anchors that point to each other. Here is why
they exist and what to do with them:

  [S-3:CS] appears in S-3's Cross-site reference row below. When you encounter it,
  it means: go to the Failure consequence row in step A-1 -- that is where the
  downstream effect of a FLAG violation manifests. You do not need to re-read the
  rest of S-3 to know where to look.

  [A-1:FC] appears in A-1's Failure consequence row. When you encounter it, it
  confirms: this is the row that S-3's Cross-site reference pointed to. If you
  arrive at A-1 in a regenerated context without S-3 in memory, the [A-1:FC]
  marker tells you the link exists and where its source is. You do not need to
  re-read S-3 to confirm the cross-reference is still active.

Enter from either anchor and you reach the other. No prior traversal is needed.

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
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                       |

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

## V-04 -- Combined: P-0 as Numbered Step + Token Abbreviation Glossary

**Axes**: Role sequence (preamble promoted to first-class numbered step P-0 before S-1) +
output format (token abbreviation glossary table defining `:CS` and `:FC` as named row-type
vocabulary). The cross-reference protocol is no longer embedded within S-3 -- it is a
distinct execution step that precedes all other steps and establishes the token map before
any setup, category, or computation work begins. S-3 and A-1 carry the bracket tokens as
before but require no embedded preamble of their own.
**Hypothesis**: In R10 V-05, the preamble is encountered by an executor who is already
mid-S-3, after processing the computation cases. The executor encounters the protocol context
only when they reach that block within S-3. An executor who skips directly to A-1 (or who
enters S-3 after a context compaction) may not re-read the preamble before processing the
chain. Promoting the protocol to P-0 -- a numbered step before S-1 -- ensures the token map
is established at the earliest possible execution point. The executor has encountered the
protocol before setup, category determination, or flag computation begin. Additionally, a
formal abbreviation glossary (`:CS` = Cross-site reference row, `:FC` = Failure consequence
row) names the suffix system as defined vocabulary: an executor who later encounters
`[A-1:FC]` in the chain can decode `:FC` as "Failure consequence row" from the P-0 glossary
without parsing surrounding text. Tests whether step-level protocol elevation plus explicit
abbreviation definitions produce stronger C-31 adherence than an embedded mid-S-3 preamble.
**Predicts**: C-01 through C-31 -- all 31 criteria.
**Expected composite**: 23/23 aspirational = 100.

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

  Active token pairs:
    [S-3:CS] -- Step S-3, Cross-site reference row  -->  references [A-1:FC]
    [A-1:FC] -- Step A-1, Failure consequence row   <--  references [S-3:CS]

Protocol guarantee: [S-3:CS] names [A-1:FC] as its forward target. [A-1:FC] names
[S-3:CS] as its backward source. Both directions are active. An executor entering
at either anchor reaches the other without inference or prior traversal.

Do not re-establish this protocol in later steps. Every bracket token in this run
is interpreted per this table.

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
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                       |

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

## V-05 -- Full Convergence: P-0 + Abbreviation Glossary Table + Resolution Table + Explanatory Framing

**Axes**: Role sequence (P-0 as numbered step) + output format (two-part structured table) +
phrasing register (explanatory framing for each token's bidirectionality role). V-05 extends
V-04 with a two-table P-0 structure: an abbreviation glossary table (`:CS` / `:FC` defined as
formal named vocabulary) followed by a full token resolution table (Token / Resolves to /
Paired token / Direction), plus a one-sentence explanatory note per direction.
**Hypothesis**: V-04's P-0 defines the abbreviation key and the token pairs in list form, which
requires an executor to mentally assemble the complete picture (what `:FC` means, which step
A-1 is, what the direction of [A-1:FC] is) by reading across multiple list items. V-05 makes
the full picture visible at a glance: the abbreviation table defines the suffix vocabulary; the
resolution table maps every token to its complete description in a single scannable row; the
explanatory sentences name the specific scenario each direction handles (context-loss at A-1,
navigation from S-3). An executor entering this protocol at any point has the complete chain
map in front of them without assembly.
Seeds v11 aspirational: whether a two-part P-0 (abbreviation glossary + resolution table) with
explicit purpose statements per direction produces measurably stronger chain adherence than a
single-table P-0 (V-04) -- specifically, whether the abbreviation glossary as named vocabulary
reduces token misidentification in later chain rows by making `:CS` and `:FC` defined terms
rather than contextually-inferred abbreviations.
**Predicts**: C-01 through C-31 -- all 31 criteria.
**Expected composite**: 23/23 aspirational = 100.

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

Token notation: bracket tokens encode step and row type. Row-type abbreviations are
defined here as named vocabulary for this run.

  Abbreviation glossary:

    | Abbreviation | Row type                  | Where it appears            |
    |--------------|---------------------------|-----------------------------|
    | :CS          | Cross-site reference row  | S-3 immutability chain      |
    | :FC          | Failure consequence row   | A-1 prohibition chain       |

  Token resolution table:

    | Token    | Resolves to                                    | Paired with | Direction                          |
    |----------|------------------------------------------------|-------------|------------------------------------|
    | [S-3:CS] | S-3 Compute Flag, Cross-site reference row     | [A-1:FC]    | forward --> names A-1 as target    |
    | [A-1:FC] | A-1 Assemble Header, Failure consequence row  | [S-3:CS]    | <-- backward, names S-3 as source  |

  [S-3:CS] exists so that an executor processing S-3's chain knows where to find the
  downstream failure consequence -- the Failure consequence row in step A-1.

  [A-1:FC] exists so that an executor arriving at A-1 in a regenerated context --
  without S-3 in active memory -- knows that a cross-site reference at [S-3:CS] names
  this row as its target. The link is discoverable from A-1 alone.

Both directions are active. Do not re-establish this protocol in later steps.

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
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                         | identifies itself as this row's mutual target)                       |

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
