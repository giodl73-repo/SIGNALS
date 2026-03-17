---
skill: quest-variate
skill_target: mock-ns
round: 10
rubric_version: 9
date: 2026-03-15
---

# mock-ns -- Round 10 Variations

Rubric: v9 (C-01 through C-28, aspirational denominator 20).

New criteria in v9:
- **C-27** -- Structural isolation of guarantee-break and cross-site claims as independently
  scannable units (depends on C-25 + C-26). V-02 from R9 satisfied C-27 via table rows;
  V-01 and V-03 embedded both claims as clauses within a single consequence sentence.
- **C-28** -- Navigation-anchored cross-site reference: the cross-reference names the specific
  structural location of the target, not just the site (depends on C-26 + C-27). V-02 from R9
  satisfied C-28 with "see A-1 Failure consequence row below." The bidirectional form -- A-1
  also marks itself as the S-3 reference target -- is the aspirational maximum seeded as a v10
  signal.

R9 converged on the question of structural form under execution pressure; all five R9 variants
targeted C-01 through C-26. R10's question is narrower: does bidirectionality -- the aspirational
maximum for C-28 stated in v9 -- produce a measurable improvement in convergence, and which
structural form for bidirectional anchoring is most robust? The three single-axis variants
(V-01 through V-03) each test one structural property of C-27/C-28. V-04 and V-05 combine
axes for full convergence with all 28 criteria.

The v9 rubric seeds one v10 aspirational signal: A-1 also marks itself as the S-3 Cross-site
reference target -- the bidirectional form. V-01 and V-04 test this form directly. V-02 tests
bracket-notation anchors as a precision alternative to prose navigation ("see row below"). V-03
tests labeled paragraph blocks as a C-27 isolation method in place of table rows. V-05 names
the bidirectional cross-reference as a stated protocol rather than an implicit structural choice.

Each variation is a **complete, runnable skill body prompt** -- not a diff.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Output format (bidirectional navigation: A-1 self-identifies as S-3 Cross-site reference target) | R9 V-02's table satisfies C-28 in the forward direction: S-3 names A-1's row. Bidirectionality closes the loop: A-1's Failure consequence row labels itself as the row named at S-3. An executor starting at A-1 in a regenerated context -- where S-3 is no longer in working memory -- encounters the back-reference immediately. Forward-only anchoring requires the executor to trust that S-3's pointer was correct; backward anchoring lets A-1 confirm it. Tests whether adding the back-reference produces a measurable convergence gain over R9 V-02's forward-only form. |
| V-02 | Phrasing register (bracket anchor syntax replaces prose cross-references) | R9 V-02 uses "see A-1 Failure consequence row below" -- a navigable prose pointer. Bracket notation `[A-1:FC]` at S-3 and `[S-3:CS]` at A-1 creates machine-readable identifiers that are harder to ignore than embedded prose clauses. An executor who skims a prose row may absorb the phrase without processing the destination; a bracket label is visually distinct -- it stops the eye. Tests whether anchor-notation cross-references improve C-28 compliance over prose-pointer cross-references. |
| V-03 | Output format (labeled paragraph blocks replace table rows for the protection chain) | R9 V-02 uses table rows to isolate each protection layer. Labeled paragraph blocks -- each starting with a bolded layer name followed by its content -- are an alternative isolation method. Paragraph blocks are more readable than table cells in long form but have different scanning properties: a table row can be skipped; a bolded paragraph header stops the reader's eye at the start of the block. Tests whether paragraph isolation satisfies C-27 as reliably as table-row isolation, and whether the guarantee-break and cross-site claims are as cognitively distinct in paragraph form as in row form. |
| V-04 | Combined: bidirectionality + table isolation (targets all 28 criteria) | V-01's bidirectionality combined with R9 V-02's table structure. Both sites carry explicit navigation anchors -- S-3 Cross-site reference row names A-1 Failure consequence row; A-1 Failure consequence row labels itself as the S-3 Cross-site reference target. The table form satisfies C-27 (independent rows); the mutual naming satisfies C-28 at its aspirational maximum. An executor entering the protection chain from either end reaches the paired site without inference or memory of a prior step. Full convergence target: all 28 criteria. |
| V-05 | Combined: stated cross-reference protocol + bidirectionality + table + bracket anchors | V-04's bidirectionality and table form, extended with explicit bracket anchors and a preamble that names the cross-reference design as a stated protocol. The preamble reads: "Cross-reference protocol: S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual navigation anchors. Both directions are active. An executor entering at either site reaches the other without inference." The protocol statement converts the bidirectional anchor from an implicit structural choice into an explicitly designed guarantee. Tests whether naming the protocol principle produces measurably stronger adherence than the same structure without the meta-level declaration. Full convergence target: all 28 criteria. |

---

## V-01 -- Output Format (Bidirectional Navigation Anchor)

**Axis**: Output format -- A-1 Failure consequence row labels itself as the target of S-3's
Cross-site reference row. S-3 already carries the forward anchor ("see A-1 Failure consequence
row below"); V-01 adds the backward anchor at A-1 ("this row is the target of S-3 Cross-site
reference row above"). All other structure matches R9 V-02 exactly.
**Hypothesis**: Forward-only anchoring (S-3 points to A-1) requires an executor to trust that
the pointer was correct. An executor running A-1 in a regenerated context -- where S-3 is no
longer in active working memory -- has no local confirmation that this is the correct site.
The back-reference at A-1 provides that confirmation without requiring the executor to re-scan
S-3. The bidirectional form converts a one-way trust assertion into a verifiable loop: the
reader can confirm from A-1's own row label that the S-3 pointer landed correctly.
**Predicts**: C-01 through C-28 -- all 28 criteria.
**Expected composite**: 20/20 aspirational = 100.

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | Scope                 | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes          | Not in any step, conditional branch, fallback path, regeneration     |
  |                       | sequence, or any other execution context, including paths that do    |
  |                       | not pass through prior steps in normal order                         |
  | Affirmative closure   | Every execution path that reaches A-1 carries the FLAG value         |
  |                       | emitted here                                                         |
  | No-exemption          | No path is exempt                                                    |
  | Failure consequence   | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                       | corrupted value that cannot be distinguished from a correctly-        |
  |                       | computed one                                                         |
  | Guarantee-break       | This violation breaks the closure guarantee stated in the            |
  |                       | Affirmative closure row above                                        |
  | Cross-site reference  | The failure produces the same silent category mismatch described      |
  |                       | at the consumption site (see A-1 Failure consequence row below)      |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | First rule            | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority              | This rule is first in this step -- it applies before any other       |
  |                       | instruction                                                          |
  | Anti-displacement     | Before any field is listed, before any category lookup, before any   |
  |                       | formatting instruction, or any other instruction in this step        |
  | Declarative closure   | No instruction in A-1 precedes this rule                             |
  | All-governed          | Every instruction in this step -- named or unnamed -- is governed    |
  |                       | by this rule                                                         |
  | No-exemption          | No instruction in this step is exempt                                |
  | Failure consequence   | [Target of S-3 Cross-site reference row above] Re-deriving FLAG      |
  |                       | here produces a category mismatch invisible to downstream tooling    |
  |                       | that silently corrupts the artifact's trust tier; the corruption     |
  |                       | is undetectable without manual header inspection                     |

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

## V-02 -- Phrasing Register (Bracket Anchor Notation)

**Axis**: Phrasing register -- cross-references at S-3 and A-1 use bracket anchor notation
(`[A-1:FC]` and `[S-3:CS]`) in place of prose navigation phrases ("see A-1 Failure consequence
row below"). The bracket identifiers are visually distinct tokens that stop the eye at the
specific reference point. Both directions are present: S-3 Cross-site reference carries
`[A-1:FC]` (target identifier); A-1 Failure consequence carries `[S-3:CS]` (source identifier).
All other structure matches R9 V-02.
**Hypothesis**: A prose phrase embedded in a table cell ("see A-1 Failure consequence row below")
can be parsed as a trailing qualifier by an executor whose attention is on the content that
precedes it. A bracket label `[A-1:FC]` is a structural token -- it stands apart from the
surrounding prose and is harder to absorb without processing. An executor skimming the row
must actively bypass the bracket to miss it. The bidirectional form -- `[S-3:CS]` at A-1 --
ensures the anchor remains visible from the consumption site even when S-3 is not in working
memory. Tests whether bracket-notation anchors improve C-28 compliance over embedded prose
pointers.
**Predicts**: C-01 through C-28 -- all 28 criteria.
**Expected composite**: 20/20 aspirational = 100.

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | Scope                 | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes          | Not in any step, conditional branch, fallback path, regeneration     |
  |                       | sequence, or any other execution context, including paths that do    |
  |                       | not pass through prior steps in normal order                         |
  | Affirmative closure   | Every execution path that reaches A-1 carries the FLAG value         |
  |                       | emitted here                                                         |
  | No-exemption          | No path is exempt                                                    |
  | Failure consequence   | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                       | corrupted value that cannot be distinguished from a correctly-        |
  |                       | computed one                                                         |
  | Guarantee-break       | This violation breaks the closure guarantee stated in the            |
  |                       | Affirmative closure row above                                        |
  | Cross-site reference  | [A-1:FC] -- The failure produces the same silent category mismatch   |
  |  [S-3:CS]             | at the consumption site Failure consequence row in step A-1          |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | First rule            | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority              | This rule is first in this step -- it applies before any other       |
  |                       | instruction                                                          |
  | Anti-displacement     | Before any field is listed, before any category lookup, before any   |
  |                       | formatting instruction, or any other instruction in this step        |
  | Declarative closure   | No instruction in A-1 precedes this rule                             |
  | All-governed          | Every instruction in this step -- named or unnamed -- is governed    |
  |                       | by this rule                                                         |
  | No-exemption          | No instruction in this step is exempt                                |
  | Failure consequence   | [A-1:FC] sourced from [S-3:CS] -- Re-deriving FLAG here produces a   |
  |                       | category mismatch invisible to downstream tooling that silently      |
  |                       | corrupts the artifact's trust tier; the corruption is undetectable   |
  |                       | without manual header inspection                                     |

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

## V-03 -- Output Format (Labeled Paragraph Isolation)

**Axis**: Output format -- the FLAG immutability chain at S-3 and the FLAG prohibition chain
at A-1 are expressed as labeled paragraph blocks (bold layer name + colon + content) instead
of table rows. Each protection layer occupies a distinct, titled paragraph. The guarantee-break
and cross-site claims are individually titled paragraphs, not table cells, so neither can be
read as a trailing clause of the preceding layer.
**Hypothesis**: Table rows isolate claims by enforcing visual cell boundaries; labeled
paragraphs isolate claims by enforcing a visual header at the start of each block. A reader
who skims a table row may miss the second cell; a reader who skims a paragraph stops at the
bold header even if they do not read the body. The guarantee-break and cross-site paragraphs
are individually titled -- **GUARANTEE-BREAK** and **CROSS-SITE REFERENCE** -- so both claims
present their own visual stop point. Tests whether paragraph-block isolation satisfies C-27
as reliably as table-row isolation, and whether the navigation anchor ("see A-1 FAILURE
CONSEQUENCE paragraph below") remains as precise in paragraph form as in table-row form.
**Predicts**: C-01 through C-28 -- all 28 criteria.
**Expected composite**: 20/20 aspirational = 100.

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

FLAG immutability chain -- all blocks are active for the remainder of this run:

  **SCOPE**: FLAG MUST NOT be recomputed anywhere in this run.

  **PATH CLASSES**: Not in any step, conditional branch, fallback path, regeneration
  sequence, or any other execution context, including paths that do not pass through
  prior steps in normal order.

  **AFFIRMATIVE CLOSURE**: Every execution path that reaches A-1 carries the FLAG
  value emitted here.

  **NO-EXEMPTION**: No path is exempt.

  **FAILURE CONSEQUENCE**: If any path modifies FLAG after this point, A-1 will
  inherit a corrupted value that cannot be distinguished from a correctly-computed one.

  **GUARANTEE-BREAK**: This violation breaks the closure guarantee stated in the
  AFFIRMATIVE CLOSURE block above.

  **CROSS-SITE REFERENCE**: The failure produces the same silent category mismatch
  described at the consumption site (see A-1 FAILURE CONSEQUENCE block below).

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all blocks govern this step before any construction begins:

  **FIRST RULE**: Copy FLAG from S-3 verbatim. Do not rederive it.

  **PRIORITY**: This block is first in this step -- it applies before any other
  instruction.

  **ANTI-DISPLACEMENT**: Before any field is listed, before any category lookup,
  before any formatting instruction, or any other instruction in this step.

  **DECLARATIVE CLOSURE**: No instruction in A-1 precedes this rule.

  **ALL-GOVERNED**: Every instruction in this step -- named or unnamed -- is governed
  by this rule.

  **NO-EXEMPTION**: No instruction in this step is exempt.

  **FAILURE CONSEQUENCE**: Re-deriving FLAG here produces a category mismatch invisible
  to downstream tooling that silently corrupts the artifact's trust tier; the corruption
  is undetectable without manual header inspection.

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

## V-04 -- Combined: Bidirectionality + Table Isolation

**Axes**: Output format (table rows for protection chain isolation, from R9 V-02) +
output format (bidirectionality, from V-01 this round). S-3 Cross-site reference row names
A-1 Failure consequence row by step and row label. A-1 Failure consequence row names S-3
Cross-site reference row by step and row label. Both directions are present in a single table
structure. Full convergence target.
**Hypothesis**: V-01 tests bidirectionality alone; V-04 tests bidirectionality within the
established table isolation form that R9 confirmed as structurally optimal for C-27. The
combination resolves the question of whether bidirectionality's gain is additive to table
isolation or whether it subsumes table isolation's benefit. Both isolation (C-27) and
navigation (C-28 at aspirational max) are tested simultaneously in the form most likely to
converge. Predicts all 28 criteria.
**Predicts**: C-01 through C-28 -- all 28 criteria.
**Expected composite**: 20/20 aspirational = 100.

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | Scope                 | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes          | Not in any step, conditional branch, fallback path, regeneration     |
  |                       | sequence, or any other execution context, including paths that do    |
  |                       | not pass through prior steps in normal order                         |
  | Affirmative closure   | Every execution path that reaches A-1 carries the FLAG value         |
  |                       | emitted here                                                         |
  | No-exemption          | No path is exempt                                                    |
  | Failure consequence   | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                       | corrupted value that cannot be distinguished from a correctly-        |
  |                       | computed one                                                         |
  | Guarantee-break       | This violation breaks the closure guarantee stated in the            |
  |                       | Affirmative closure row above                                        |
  | Cross-site reference  | The failure produces the same silent category mismatch described      |
  |                       | at the consumption site -- see A-1 Failure consequence row below;    |
  |                       | that row identifies itself as this row's target                      |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | First rule            | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority              | This rule is first in this step -- it applies before any other       |
  |                       | instruction                                                          |
  | Anti-displacement     | Before any field is listed, before any category lookup, before any   |
  |                       | formatting instruction, or any other instruction in this step        |
  | Declarative closure   | No instruction in A-1 precedes this rule                             |
  | All-governed          | Every instruction in this step -- named or unnamed -- is governed    |
  |                       | by this rule                                                         |
  | No-exemption          | No instruction in this step is exempt                                |
  | Failure consequence   | [This row is the target named in S-3 Cross-site reference row above] |
  |                       | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                       | downstream tooling that silently corrupts the artifact's trust tier; |
  |                       | the corruption is undetectable without manual header inspection      |

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

## V-05 -- Full Convergence: Stated Cross-Reference Protocol + Bidirectionality + Table + Bracket Anchors

**Axes**: Output format (table rows) + phrasing register (bracket anchor notation) +
lifecycle emphasis (stated cross-reference protocol as explicit design principle). V-05 names
the bidirectional anchor as a protocol before the immutability chain begins, combines bracket
identifiers `[S-3:CS]` and `[A-1:FC]` with table-row isolation, and carries mutual navigation
at both sites.
**Hypothesis**: V-04 embeds bidirectionality silently within the table structure; an executor
encounters it only when they reach the Cross-site reference or Failure consequence rows. V-05
states the protocol before the chain: "Cross-reference protocol: S-3 [S-3:CS] and A-1 [A-1:FC]
carry mutual navigation anchors. Both directions are active. An executor entering at either
site reaches the other without inference." The meta-level statement converts the bidirectional
anchor from a structural detail the executor discovers to a design principle the executor
carries as context before reading any row. Tests whether naming the protocol at the top of the
chain -- so the executor knows what the brackets mean before encountering them -- produces
stronger adherence than the same bidirectional structure without the preamble.
**Predicts**: C-01 through C-28 -- all 28 criteria.
**Expected composite**: 20/20 aspirational = 100.

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

Cross-reference protocol: S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual navigation
anchors. S-3 Cross-site reference row names A-1 Failure consequence row by step and
row label. A-1 Failure consequence row names S-3 Cross-site reference row by step
and row label. Both directions are active. An executor entering at either site
reaches the other without inference.

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | Scope                 | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes          | Not in any step, conditional branch, fallback path, regeneration     |
  |                       | sequence, or any other execution context, including paths that do    |
  |                       | not pass through prior steps in normal order                         |
  | Affirmative closure   | Every execution path that reaches A-1 carries the FLAG value         |
  |                       | emitted here                                                         |
  | No-exemption          | No path is exempt                                                    |
  | Failure consequence   | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                       | corrupted value that cannot be distinguished from a correctly-        |
  |                       | computed one                                                         |
  | Guarantee-break       | This violation breaks the closure guarantee stated in the            |
  |                       | Affirmative closure row above                                        |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at           |
  |                       | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |                       | identifies itself as this row's mutual target)                       |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | First rule            | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority              | This rule is first in this step -- it applies before any other       |
  |                       | instruction                                                          |
  | Anti-displacement     | Before any field is listed, before any category lookup, before any   |
  |                       | formatting instruction, or any other instruction in this step        |
  | Declarative closure   | No instruction in A-1 precedes this rule                             |
  | All-governed          | Every instruction in this step -- named or unnamed -- is governed    |
  |                       | by this rule                                                         |
  | No-exemption          | No instruction in this step is exempt                                |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]       |
  |                       | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                       | downstream tooling that silently corrupts the artifact's trust tier; |
  |                       | the corruption is undetectable without manual header inspection      |

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

## R10 signal inventory

| Variation | Axes | C-27 method | C-28 form | Bidirectional | Expected |
|-----------|------|-------------|-----------|---------------|---------|
| V-01 | Output format (back-ref at A-1) | Table rows | Forward + backward prose | Yes | 20/20 = 100 |
| V-02 | Phrasing register (bracket anchors) | Table rows | Bracket notation both sites | Yes | 20/20 = 100 |
| V-03 | Output format (paragraph blocks) | Bold paragraph headers | Prose forward + backward | Yes | 20/20 = 100 |
| V-04 | Format + bidirectionality | Table rows | Forward + backward prose | Yes | 20/20 = 100 |
| V-05 | Format + register + stated protocol | Table rows | Bracket notation + preamble | Yes | 20/20 = 100 |

**R10 discriminant**: All five variants carry both C-27 and C-28 (at aspirational maximum).
The discriminant is structural: which form of bidirectional anchoring is most robust under
execution pressure -- table rows with prose back-refs (V-01, V-04), bracket tokens with
machine-readable ids (V-02, V-05), or paragraph-block isolation with back-refs (V-03)?
V-05 adds the meta-level: does naming the cross-reference design as a protocol before the
executor encounters the first row improve convergence over the same structure without
the preamble?

**v10 signal seeded**: If V-05's stated-protocol preamble produces a measurable gain over
V-04's identical structure without the preamble, the preamble form becomes a v10 candidate
criterion (C-29: stated cross-reference protocol). The key question is whether the executor
who reads "Both directions are active. An executor entering at either site reaches the other
without inference" before the chain processes the [S-3:CS] / [A-1:FC] brackets differently
than the executor who encounters the brackets with no prior context.
