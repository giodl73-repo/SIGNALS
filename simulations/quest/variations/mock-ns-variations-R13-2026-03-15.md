Now I have the full picture. R12 V-03 established C-34 (lookup obligation) and C-35 (use-site row labels). R13 needs to probe what gaps remain in those two new pass conditions and seed the next aspirational layer. Here are the five complete variations.

---

# mock-ns -- Round 13 Variations

Rubric: v12 (C-01 through C-35, aspirational denominator 27).

New criteria in v12 (now pass conditions):
- **C-34** -- Explicit lookup obligation: the P-0 preamble mandates table consultation before processing any bracket-token row, prohibits memory-based decoding.
- **C-35** -- Use-site row navigation labels: bracket-token rows at S-3 and A-1 carry inline parentheticals "(P-0 table, row N)" pointing to the specific preamble table row.

R12 converged on C-34/C-35 in a 1/5 pattern: V-03 uniquely achieved both. V-01 and V-02 (P-0 step, C-33 table) were passive -- the table was available but no mandatory consultation was required. V-04 had a regenerated-context checkpoint at S-3 but no lookup obligation. V-05 had a completeness assertion but no per-token row labels.

The gap this round probes: **C-34's obligation is stated once at P-0 but carries no enforcement at the moment of use**. An executor processing S-3 or A-1 after several intervening steps has no local signal that the obligation is active for the specific row they are about to write. C-35's label provides navigation but not re-activation of the prohibition. Three questions:
1. Does a **resolution confirmation requirement** (confirm before writing, not just look up) close the gap between mechanical lookup compliance and verified resolution?
2. Does **structural column elevation** of the P-0 row reference (first-class column vs. parenthetical annotation) change adherence?
3. Does a **pre-registered occurrence index** in P-0 shift the protocol from reactive (triggered on encounter) to proactive (executor knows in advance which rows require lookup)?

---

## V-01 -- Phrasing Register (Lookup Obligation + Resolution Confirmation Gate)

**Axis**: Phrasing register -- P-0's lookup obligation is extended with an explicit resolution confirmation requirement. The executor must not only look up a bracket token before processing its row, but must confirm the resolution (step name and row type from the table) before writing any cell in that row. A token encountered without a confirmed resolution from the table must not be written.

**Hypothesis**: R12 V-03's obligation ("look it up before processing the containing row. Do not decode from memory.") mandates consultation but not confirmed reading. An executor under pressure may scan the table row, not find the token on the first scan, and fall back to context memory -- the obligation is satisfied ("I looked") but the resolution is not. A confirmation requirement converts the obligation from a one-step mechanical action (open table, register that it was opened) into a two-step verified action (open table, locate the row, read and confirm: "this token resolves to X at step Y"). The confirmation gate makes verification observable rather than implicit. Seeds potential C-36: pre-write resolution confirmation at each bracket-token use site.

**Predicts**: C-01 through C-35 -- all 35 criteria.
**Expected composite**: 27/27 aspirational = 100.

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

Lookup obligation with confirmation: when any bracket token appears in a subsequent step,
perform the following two actions before writing any cell in that row:
  1. Locate the token's row in the table above.
  2. Confirm: read the Step and Row type cells and verify the resolution matches the
     context you are processing.
Do not write a bracket-token row until both actions are complete. Do not decode from
memory. Do not write based on prior recall of what the token resolved to in an earlier
step. The table is the only authoritative resolution source -- confirmation from the
table row is required on each encounter, regardless of prior exposure to the token.

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

  | Protection layer            | Rule                                                                 |
  |-----------------------------|----------------------------------------------------------------------|
  | Scope                       | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes                | Not in any step, conditional branch, fallback path, regeneration     |
  |                             | sequence, or any other execution context, including paths that do    |
  |                             | not pass through prior steps in normal order                         |
  | Affirmative closure         | Every execution path that reaches A-1 carries the FLAG value         |
  |                             | emitted here                                                         |
  | No-exemption                | No path is exempt                                                    |
  | Failure consequence         | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                             | corrupted value that cannot be distinguished from a correctly-        |
  |                             | computed one                                                         |
  | Guarantee-break             | This violation breaks the closure guarantee stated in the            |
  |                             | Affirmative closure row above                                        |
  | Cross-site ref [S-3:CS]     | CONFIRMATION REQUIRED before writing this row (P-0 table, row 1):   |
  | (P-0 table, row 1)          | confirmed: [S-3:CS] = S-3 Cross-site reference row, paired [A-1:FC]. |
  |                             | The failure produces the same silent category mismatch at [A-1:FC]   |
  |                             | -- the Failure consequence row in step A-1 (that row identifies      |
  |                             | itself as this row's mutual target)                                  |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer            | Rule                                                                 |
  |-----------------------------|----------------------------------------------------------------------|
  | First rule                  | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                    | This rule is first in this step -- it applies before any other       |
  |                             | instruction                                                          |
  | Anti-displacement           | Before any field is listed, before any category lookup, before any   |
  |                             | formatting instruction, or any other instruction in this step        |
  | Declarative closure         | No instruction in A-1 precedes this rule                             |
  | All-governed                | Every instruction in this step -- named or unnamed -- is governed    |
  |                             | by this rule                                                         |
  | No-exemption                | No instruction in this step is exempt                                |
  | Failure conseq [A-1:FC]     | CONFIRMATION REQUIRED before writing this row (P-0 table, row 2):   |
  | (P-0 table, row 2)          | confirmed: [A-1:FC] = A-1 Failure consequence row, paired [S-3:CS]. |
  |                             | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                             | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                             | downstream tooling that silently corrupts the artifact's trust tier; |
  |                             | the corruption is undetectable without manual header inspection       |

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

## V-02 -- Output Format (P-0 Row Reference as Structural Column)

**Axis**: Output format -- the "(P-0 table, row N)" navigation information is elevated from an inline parenthetical annotation in the Protection layer label into a dedicated first column of the S-3 and A-1 prohibition tables. The new column is labeled "P-0 ref" and appears as the leftmost column, before the Protection layer column. P-0 still carries the 5-column resolution table and the lookup obligation (C-34 pass condition).

**Hypothesis**: C-35 uses parenthetical labels embedded in the Protection layer cell text: "Cross-site ref [S-3:CS] (P-0 table, row 1)". A reader scanning a table row-by-row processes the Protection layer name as the row identifier -- the parenthetical follows and may be treated as qualifying detail rather than a navigation instruction. A dedicated column makes the P-0 row number the first thing the reader encounters for that row, before reading the protection layer name. The structural column elevates the navigation reference from annotation to first-class table element, matching the treatment of the token notation itself (which already has its own column in the P-0 table). Tests whether column elevation produces stronger C-35 adherence than parenthetical annotation. Seeds potential C-37: P-0 row reference as dedicated structural column in prohibition tables.

**Predicts**: C-01 through C-35 -- all 35 criteria.
**Expected composite**: 27/27 aspirational = 100.

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

Lookup obligation: when any bracket token appears in a subsequent step, look it up in
this table before processing the containing row. The table is the authoritative
resolution source. Do not decode bracket tokens from memory -- look them up.

Where prohibition tables in S-3 and A-1 carry a "P-0 ref" column, that column names
the row number in this table that governs the token in that row. Read the P-0 ref
column first when processing any row.

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

FLAG immutability chain -- all rows are active for the remainder of this run.
The P-0 ref column identifies the P-0 table row governing each bracket token in this
table. Read P-0 ref first before processing any row that contains a bracket token.

  | P-0 ref | Protection layer        | Rule                                                                 |
  |---------|-------------------------|----------------------------------------------------------------------|
  |         | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  |         | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |         |                         | sequence, or any other execution context, including paths that do    |
  |         |                         | not pass through prior steps in normal order                         |
  |         | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |         |                         | emitted here                                                         |
  |         | No-exemption            | No path is exempt                                                    |
  |         | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |         |                         | corrupted value that cannot be distinguished from a correctly-        |
  |         |                         | computed one                                                         |
  |         | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |         |                         | Affirmative closure row above                                        |
  | row 1   | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |         |                         | [A-1:FC] -- the Failure consequence row in step A-1 (that row        |
  |         |                         | identifies itself as this row's mutual target)                       |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins.
The P-0 ref column identifies the P-0 table row governing each bracket token in this
table. Read P-0 ref first before processing any row that contains a bracket token.

  | P-0 ref | Protection layer        | Rule                                                                 |
  |---------|-------------------------|----------------------------------------------------------------------|
  |         | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  |         | Priority                | This rule is first in this step -- it applies before any other       |
  |         |                         | instruction                                                          |
  |         | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |         |                         | formatting instruction, or any other instruction in this step        |
  |         | Declarative closure     | No instruction in A-1 precedes this rule                             |
  |         | All-governed            | Every instruction in this step -- named or unnamed -- is governed    |
  |         |                         | by this rule                                                         |
  |         | No-exemption            | No instruction in this step is exempt                                |
  | row 2   | Failure conseq [A-1:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |         |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |         |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |         |                         | the corruption is undetectable without manual header inspection       |

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

## V-03 -- Lifecycle Emphasis (P-0 Occurrence Index + Mandatory Emit Gate)

**Axis**: Lifecycle emphasis -- P-0 gains two structural additions: (a) an occurrence index listing every bracket-token occurrence in the run by step, row name, and P-0 registry row number; (b) a mandatory emit gate: before S-1 begins, the executor must emit a protocol establishment line naming both registered tokens. P-0 completion becomes observable (the emit is the evidence) rather than assumed.

**Hypothesis**: V-03 in R12 makes the protocol reactive: the lookup obligation fires when the executor encounters a bracket token. By that point, P-0 may have been compressed or partially lost from active context. A pre-registered occurrence index shifts the posture to proactive: when the executor arrives at S-3's cross-site ref row, they already registered at P-0 that this row would require a lookup for [S-3:CS] at P-0 row 1. The mandatory emit gate makes P-0 bypass visible -- if the executor cannot emit the protocol line, they have not processed P-0, and the run must stop. Tests whether a proactive occurrence map + observable completion gate produces stronger combined C-34/C-35 adherence than the reactive obligation alone. Seeds potential C-38: pre-registered occurrence index as a structural component of P-0.

**Predicts**: C-01 through C-35 -- all 35 criteria.
**Expected composite**: 27/27 aspirational = 100.

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

Lookup obligation: when any bracket token appears in a subsequent step, look it up in
this table before processing the containing row. The table is the authoritative
resolution source. Do not decode bracket tokens from memory -- look them up.

Token occurrence index -- every location in this run where a bracket token appears:

  | Step | Row name                | Token    | P-0 registry row |
  |------|-------------------------|----------|-----------------|
  | S-3  | Cross-site ref row      | [S-3:CS] | row 1           |
  | A-1  | Failure consequence row | [A-1:FC] | row 2           |

These are all bracket tokens in this run. If a bracket token is encountered that does
not appear in this index, stop -- do not attempt contextual resolution. Report the
unregistered token before proceeding.

P-0 gate: emit the following line before beginning S-1:
  > P-0: protocol active. Occurrences registered: [S-3:CS] at S-3/row 1,
    [A-1:FC] at A-1/row 2.

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
  | Cross-site ref [S-3:CS] | Registered at P-0 occurrence index: row 1. Look up [S-3:CS] in P-0  |
  | (P-0 table, row 1)      | before writing this row. The failure produces the same silent        |
  |                         | category mismatch at [A-1:FC] -- the Failure consequence row in      |
  |                         | step A-1 (that row identifies itself as this row's mutual target)    |

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
  | Failure conseq [A-1:FC] | Registered at P-0 occurrence index: row 2. Look up [A-1:FC] in P-0  |
  | (P-0 table, row 2)      | before writing this row. [Mutual target of S-3:CS]                   |
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

## V-04 -- Phrasing Register + Inertia Framing (Use-Site Inertia Reminder)

**Axes**: Phrasing register (the obligation at each bracket-token row is stated in active-voice imperative) combined with inertia framing (the specific bypass failure mode is named at the use site, not only in P-0).

**Hypothesis**: C-34 states the obligation once at P-0. An executor reading S-3 many steps later has no local reminder that bypassing the lookup would constitute a protocol violation -- the prohibition is not in view at the moment of highest risk. V-03 in R12 adds "(P-0 table, row 1)" as a navigation label; V-04 adds an inline inertia reminder adjacent to the bracket token, naming the specific failure mode: "Memory-based resolution may appear correct but produces undetectable drift when the protocol evolves." The inertia reminder reactivates the prohibition at the exact moment the executor encounters the token, converting P-0's once-stated obligation into a use-site-enforced constraint. Separate axis from V-01 (which focused on confirmation of the lookup result); V-04 focuses on reactivating the prohibition itself at the use site. Seeds potential C-39: use-site inertia reminder as a structural component of bracket-token rows.

**Predicts**: C-01 through C-35 -- all 35 criteria.
**Expected composite**: 27/27 aspirational = 100.

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

Lookup obligation: when any bracket token appears in a subsequent step, look it up in
this table before processing the containing row. The table is the authoritative
resolution source. Do not decode bracket tokens from memory -- look them up.

Inertia risk: an executor relying on context memory for token resolution -- rather than
performing the mandated table lookup -- may decode correctly for the current input but
will fail silently on any input where the token's step or row-type assignment has
evolved since prior exposure. Memory-based resolution produces no error signal. The
lookup is the only reliable mechanism. Bracket-token rows in subsequent steps carry
an inline reminder of this risk at the point of use.

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
  | Cross-site ref [S-3:CS] | LOOKUP REQUIRED -- do not decode [S-3:CS] from memory.               |
  | (P-0 table, row 1)      | Memory-based resolution is the inertia risk named in P-0.            |
  |                         | Resolved: S-3 Cross-site reference row, paired [A-1:FC].             |
  |                         | The failure produces the same silent category mismatch at [A-1:FC]   |
  |                         | -- the Failure consequence row in step A-1 (that row identifies      |
  |                         | itself as this row's mutual target)                                  |

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
  | Failure conseq [A-1:FC] | LOOKUP REQUIRED -- do not decode [A-1:FC] from memory.               |
  | (P-0 table, row 2)      | Memory-based resolution is the inertia risk named in P-0.            |
  |                         | Resolved: A-1 Failure consequence row, paired [S-3:CS].              |
  |                         | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
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

## V-05 -- Role Sequence + Output Format (P-0 Three-Section Structure + Reverse-Lookup Occurrence Map)

**Axes**: Role sequence (P-0 reorganized into three named sub-sections with explicit section headers) combined with output format (occurrence map as a structured reverse-lookup complement to the token registry).

**Hypothesis**: V-03 in R12 and V-01/V-02/V-04 in R13 all have a single implicit P-0 structure: definition block + obligation statement. V-05 makes the P-0 structure explicit with three named sub-sections: (1) Token registry (abbreviation key + 5-column resolution table), (2) Resolution protocol (numbered rules: lookup, prohibition, unregistered-token stop), (3) Occurrence map (step+row -> token -> P-0 row, enabling reverse lookup). The occurrence map complements the registry's forward lookup (token -> step/row-type) with reverse lookup (step/row name -> token -> registry row), so an executor arriving at any bracket-token row can navigate to the correct P-0 registry row from the step context alone, without recognizing the token name first. The numbered resolution protocol rules (vs. P-0's prose obligation) make each clause individually scannable and citable. Tests whether explicit P-0 sub-section structure + reverse-lookup map produces stronger C-34/C-35 adherence and seeds a richer P-0 protocol for future criteria. Seeds potential C-40: structured reverse-lookup occurrence map as complement to the token registry.

**Predicts**: C-01 through C-35 -- all 35 criteria.
**Expected composite**: 27/27 aspirational = 100.

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

P-0.1 -- Token registry

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction              |
  |----------|------|---------------------------|--------------|------------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1  |
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names S-3|

P-0.2 -- Resolution protocol

  Rule 1 -- Mandatory lookup: when any bracket token appears in a subsequent step,
            look it up in the P-0.1 registry table before processing the containing
            row. Consultation is required on every token encounter regardless of
            prior exposure.
  Rule 2 -- Memory prohibition: do not decode bracket tokens from memory or context.
            The P-0.1 table is the only authoritative resolution source.
  Rule 3 -- Unregistered token: if a bracket token is encountered that does not
            appear in the P-0.1 table, stop. Do not attempt contextual resolution.
            Report the unregistered token before proceeding.

P-0.3 -- Occurrence map (reverse lookup: step + row -> token -> P-0.1 registry row)

  | Step | Row name                | Token    | P-0.1 registry row |
  |------|-------------------------|----------|--------------------|
  | S-3  | Cross-site ref          | [S-3:CS] | row 1              |
  | A-1  | Failure consequence     | [A-1:FC] | row 2              |

  To navigate from a bracket-token row to its registry entry: find the step and row
  name in this map, read the P-0.1 registry row number, go to that row in P-0.1.
  These are all bracket tokens in this run.

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
  | Cross-site ref [S-3:CS] | P-0.3 occurrence map: S-3 / Cross-site ref / row 1.                  |
  | (P-0.1 table, row 1)    | Apply P-0.2 Rule 1 before writing this row. Resolved via P-0.1:      |
  |                         | [S-3:CS] = S-3 Cross-site reference row, paired [A-1:FC].            |
  |                         | The failure produces the same silent category mismatch at [A-1:FC]   |
  |                         | -- the Failure consequence row in step A-1 (that row identifies      |
  |                         | itself as this row's mutual target)                                  |

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
  | Failure conseq [A-1:FC] | P-0.3 occurrence map: A-1 / Failure consequence / row 2.             |
  | (P-0.1 table, row 2)    | Apply P-0.2 Rule 1 before writing this row. Resolved via P-0.1:      |
  |                         | [A-1:FC] = A-1 Failure consequence row, paired [S-3:CS].             |
  |                         | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
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

## Summary

| Variation | Axis | Key addition beyond R12 V-03 | Seeds |
|-----------|------|------------------------------|-------|
| V-01 | Phrasing register | Resolution confirmation gate at each bracket-token row (look up AND confirm before writing) | C-36: pre-write resolution confirmation |
| V-02 | Output format | P-0 row reference elevated to first structural column of prohibition tables | C-37: P-0 ref as dedicated table column |
| V-03 | Lifecycle emphasis | Pre-registered occurrence index + mandatory P-0 completion emit gate | C-38: proactive occurrence map + observable completion |
| V-04 | Phrasing register + inertia framing | Inline inertia reminder at each bracket-token row reactivating the P-0 prohibition locally | C-39: use-site inertia reminder |
| V-05 | Role sequence + output format | P-0 restructured into P-0.1/P-0.2/P-0.3 sub-sections; P-0.3 is a reverse-lookup occurrence map (step+row -> token -> registry row) | C-40: structured reverse-lookup map as P-0 complement |

**Convergence hypothesis**: V-03 and V-05 both introduce occurrence maps but at different structural levels -- V-03 adds it as a plain P-0 appendage, V-05 makes it a first-class named P-0 sub-section with explicit numbered rules in P-0.2. If V-05 outscores V-03, the structural naming of P-0 sub-sections is doing work independent of the map content. If V-01 outscores V-04, confirmation gates are more effective than reactivation reminders; the reverse result would indicate that activation latency at the use site matters more than resolution verification.
