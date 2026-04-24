Now I have the full context. The T3 SKILL.md was promoted from R2 V-05, and R3 targets three open gaps: C-12 (TOPICS.md merged with skill selection), C-15 (no S-0 CONSTRAINT naming prohibited ops by type), C-16 (wildcards in case prose, not in FLAG table Condition cells). Generating the 5 complete variations now.

---

# mock-ns -- Round 3 Variations

Rubric: v3 (C-01 through C-16, 5 essential / 3 recommended / 8 aspirational).

New criteria in v3 (extracted from R2 V-05 excellence evidence):
- **C-14** -- Assembly expressed as discrete named steps A-1 through A-5
- **C-15** -- CONSTRAINT block names prohibited S-0 operations by type (no category lookup, no skill selection, no mock generation)
- **C-16** -- Wildcard patterns `trace-*`, `listen-*` appear in FLAG table condition column cell, not only in footnotes

T3 SKILL.md (promoted from R2 V-05) has three open gaps against v3:

- **C-12 gap**: S-1 reads TOPICS.md and does skill selection in the same step. C-12 requires TOPICS.md to complete before S-1 skill selection begins.
- **C-15 gap**: No dedicated S-0 with a CONSTRAINT block naming prohibited operations by functional type.
- **C-16 gap**: S-3 uses case-prose. Wildcards `trace-*` and `listen-*` appear in Case 1 prose body, not inside a Condition column cell of a FLAG table.

C-14 is satisfied by T3: steps A-1 through A-5 (ASSEMBLE HEADER, FIDELITY WARNING, GENERATE ARTIFACT BODY, WRITE ARTIFACT, NEXT-STEP LINE) are present and labeled.

R3 isolates: (a) FLAG table with wildcards in Condition column satisfies C-16 independently; (b) S-0 separation with CONSTRAINT naming op types by name satisfies C-15 and incidentally C-12; (c) plain S-0 separation without P-0 machinery satisfies C-12 alone; (d) C-15 and C-16 stack without interference; then convergent.

Three axes selected for single-axis isolation:
1. **FLAG table condition column (C-16)** -- Replace S-3 case prose with a table whose Condition cells contain `trace-*` and `listen-*` directly.
2. **S-0 CONSTRAINT with named type prohibitions (C-15 + C-12)** -- Add S-0 as a dedicated TOPICS.md step before S-1, with CONSTRAINT block naming forbidden operations by type.
3. **Clean S-0 separation, no P-0 (C-12 isolation)** -- S-0 as plain TOPICS.md step with ordering language only; strip no machinery, add no CONSTRAINT.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | FLAG table condition column (C-16 single axis) | A FLAG computation table whose Condition column cells contain `trace-*` and `listen-*` as match expressions directly -- not in footnotes or prose below -- is the minimal sufficient signal for C-16. S-1 still merges TOPICS.md with skill selection; no S-0 CONSTRAINT. Predicts: C-12 fail, C-14 pass, C-15 fail, C-16 pass. |
| V-02 | S-0 CONSTRAINT with named prohibitions (C-15 + C-12) | A dedicated S-0 step whose CONSTRAINT block names prohibited operations by functional type ("No category lookup. No skill selection. No mock generation.") satisfies C-15. The S-0/S-1 separation incidentally satisfies C-12. S-3 stays as case prose (C-16 not addressed). Predicts: C-12 pass, C-14 pass, C-15 pass, C-16 fail. |
| V-03 | Clean S-0 separation, no P-0 (C-12 isolation) | Stripping P-0 and presenting S-0 as a plain dedicated TOPICS.md step with ordering language satisfies C-12 via step-label separation alone. Tests whether P-0 is necessary for C-12 or whether the step boundary is the load-bearing signal. C-15 and C-16 not addressed. Predicts: C-12 pass, C-14 pass, C-15 fail, C-16 fail. |
| V-04 | S-0 CONSTRAINT + FLAG wildcard table (C-15 + C-16, two-axis) | Combining S-0 CONSTRAINT with named prohibitions (V-02 axis) and FLAG wildcard table (V-01 axis) satisfies C-15, C-16, and C-12 without interference. C-14 maintained (A-1...A-5). Tests whether the two axes are additive. Predicts: C-12 pass, C-14 pass, C-15 pass, C-16 pass. |
| V-05 | Convergent (all three axes) | P-0 cross-reference protocol + S-0 CONSTRAINT naming prohibited ops by functional type + S-1 skill selection only + S-3 FLAG table with `trace-*`, `listen-*` in Condition column + A-1 through A-5 assembly. Closes all three T3 gaps. All 16 criteria predicted to pass. |

---

## V-01 -- FLAG Table Condition Column (C-16)

**Axis**: FLAG table condition column -- S-3 flag computation replaced with a lookup table whose Condition column cells contain `trace-*` and `listen-*` wildcards as match expressions.
**Hypothesis**: C-16 requires the wildcard patterns in the Condition cell itself, not in footnote or prose below. Expressing critical-skill conditions as "skill matches `trace-*`" and "skill matches `listen-*`" inside table cells is the minimal change that satisfies C-16. P-0 and A-1...A-5 are preserved from T3. S-1 still merges TOPICS.md with skill selection -- C-12 not addressed. No S-0 CONSTRAINT -- C-15 not addressed.
**Predicts**: C-01 through C-11 pass | C-12 fail | C-13 pass | C-14 pass | C-15 fail | C-16 pass.
**Expected composite**: ~14 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
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
    Step 2c: Assert step name matches the step you are currently writing
             and row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (fill Match field only):
               Token: {token-name -- pre-filled}
               Step: {step-name -- pre-filled}
               Row type: {row-type-name -- pre-filled}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

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

If the skill is not in any group, emit an error naming the unrecognized skill-id and
the available registry, then stop.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

Evaluate the rows in order. Use the first matching Condition. Stop at first match.

  | Condition                                                              | FLAG value                                                    |
  |------------------------------------------------------------------------|---------------------------------------------------------------|
  | CATEGORY = HIGH-STRUCTURE AND skill matches `trace-*` AND tier >= 2   | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)" |
  | CATEGORY = HIGH-STRUCTURE AND skill = scout-feasibility AND tier >= 2  | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)" |
  | CATEGORY = HIGH-STRUCTURE AND skill matches `listen-*` AND tier >= 2   | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)" |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                            | "none (structural coverage reliable)"                         |
  | CATEGORY = EVIDENCE-HEAVY                                              | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)" |
  | CATEGORY = MIXED                                                       | "REVIEW-FOR-PLAUSIBILITY"                                     |

Compliance override -- applied after table lookup, regardless of case above:
  If compliance tags are present in TOPICS.md AND skill is scout-compliance or
  trace-permissions (any tier, any category):
  FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability: FLAG MUST NOT be recomputed anywhere in this run. Every execution
path that reaches A-1 carries the FLAG value emitted here.

CONFIRMATION REQUIRED before writing the cross-site reference row:

  Phase 1: locate [S-3:CS] in P-0 table, row 1.
  Phase 2 (Steps 2a-2d): read Step=S-3 + Row type=Cross-site reference row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [S-3:CS]                 |
  | Step       | S-3                      |
  | Row type   | Cross-site reference row |
  | Match      | _______________          |

Cross-site reference [S-3:CS]: Failure to copy FLAG verbatim at A-1 produces a
category mismatch at [A-1:FC] that is invisible to downstream tooling.

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

First rule: Copy FLAG from S-3 verbatim. Do not rederive it.

CONFIRMATION REQUIRED before writing the failure consequence row:

  Phase 1: locate [A-1:FC] in P-0 table, row 2.
  Phase 2 (Steps 2a-2d): read Step=A-1 + Row type=Failure consequence row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [A-1:FC]                 |
  | Step       | A-1                      |
  | Row type   | Failure consequence row  |
  | Match      | _______________          |

Failure consequence [A-1:FC]: Re-deriving FLAG here produces a category mismatch
invisible to downstream tooling. [Mutual target of S-3:CS]

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

All six fields present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section after the header. Separate from header
and from body with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    (competitor names, market data, research findings) may be partially fabricated.
    Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
Body must include:
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

## V-02 -- S-0 CONSTRAINT with Named Prohibitions (C-15 + C-12)

**Axis**: S-0 separation with typed prohibitions -- a dedicated S-0 step reads TOPICS.md only, with a CONSTRAINT block naming forbidden operation types by name rather than by step reference. S-3 retains case prose (C-16 not addressed).
**Hypothesis**: C-15 requires the CONSTRAINT to name prohibited operations by *functional type*, not just by step order ("after S-0, before S-1"). Naming "No category lookup. No skill selection. No mock generation." makes the constraint self-enforcing regardless of where those operations appear. The S-0/S-1 boundary incidentally satisfies C-12 as a structural consequence of separation.
**Predicts**: C-01 through C-11 pass | C-12 pass | C-13 pass | C-14 pass | C-15 pass | C-16 fail.
**Expected composite**: ~15 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
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

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches the step you are currently writing
             and row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (fill Match field only):
               Token: {token-name -- pre-filled}
               Step: {step-name -- pre-filled}
               Row type: {row-type-name -- pre-filled}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete.

---

STEP S-0 -- READ TOPICS.md

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

CONSTRAINT: S-0 performs this read and emit only.
  No category lookup.
  No skill selection.
  No mock generation.

S-0 is complete when the emit line above is written. S-1 begins after S-0 is complete.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock using the values established in S-0:
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

If the skill is not in any group, emit an error naming the unrecognized skill-id and
the available registry, then stop.

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

FLAG immutability: FLAG MUST NOT be recomputed anywhere in this run. Every execution
path that reaches A-1 carries the FLAG value emitted here.

CONFIRMATION REQUIRED before writing the cross-site reference row:

  Phase 1: locate [S-3:CS] in P-0 table, row 1.
  Phase 2 (Steps 2a-2d): read Step=S-3 + Row type=Cross-site reference row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [S-3:CS]                 |
  | Step       | S-3                      |
  | Row type   | Cross-site reference row |
  | Match      | _______________          |

Cross-site reference [S-3:CS]: Failure to copy FLAG verbatim at A-1 produces a
category mismatch at [A-1:FC] invisible to downstream tooling.

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

First rule: Copy FLAG from S-3 verbatim. Do not rederive it.

CONFIRMATION REQUIRED before writing the failure consequence row:

  Phase 1: locate [A-1:FC] in P-0 table, row 2.
  Phase 2 (Steps 2a-2d): read Step=A-1 + Row type=Failure consequence row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [A-1:FC]                 |
  | Step       | A-1                      |
  | Row type   | Failure consequence row  |
  | Match      | _______________          |

Failure consequence [A-1:FC]: Re-deriving FLAG here corrupts the artifact's trust tier
silently. [Mutual target of S-3:CS]

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

All six fields present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section after the header. Separate with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+
    for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
Body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.

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

Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-03 -- Clean S-0 Separation, No P-0 (C-12 isolation)

**Axis**: Phrasing register -- P-0 cross-reference token machinery is removed entirely. S-0 is a plain dedicated TOPICS.md step using ordering language ("S-0 is complete before S-1 begins"). No bracket tokens. No confirmation records. No CONSTRAINT block. Tests whether the step-label boundary alone carries C-12.
**Hypothesis**: C-12 is satisfied by the structural fact that TOPICS.md reading occurs in a labeled step before skill selection occurs in a separate labeled step. The P-0 protocol was designed to protect the FLAG cross-site contract, not to satisfy C-12. If C-12 passes with plain ordering language and no P-0, then P-0 is not load-bearing for C-12.
**Predicts**: C-01 through C-11 pass | C-12 pass | C-13 pass | C-14 pass | C-15 fail | C-16 fail.
**Expected composite**: ~14 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

S-0 is complete when the emit line above is written.
S-1 begins only after S-0 is complete.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock using values from S-0:
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

If the skill is not in any group, emit an error naming the unrecognized skill-id and
the available registry, then stop.

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

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

All six fields present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section after the header. Separate with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+
    for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
Body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.

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

Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-04 -- S-0 CONSTRAINT + FLAG Wildcard Table (C-15 + C-16, two-axis)

**Axis**: Combined S-0 CONSTRAINT with named type prohibitions (V-02 axis) and FLAG table with wildcards in Condition column cells (V-01 axis). Tests whether the two axes stack additively.
**Hypothesis**: C-15 and C-16 address different structural sites (S-0 CONSTRAINT and S-3 FLAG table respectively). There is no dependency between them; combining both axes should satisfy C-15 and C-16 simultaneously without interference. The S-0/S-1 boundary also satisfies C-12 as a structural consequence. P-0 is retained. A-1...A-5 maintained for C-14.
**Predicts**: C-01 through C-16 pass. All four targeted criteria pass; no interference.
**Expected composite**: 16 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
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

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches the step you are currently writing
             and row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (fill Match field only):
               Token: {token-name -- pre-filled}
               Step: {step-name -- pre-filled}
               Row type: {row-type-name -- pre-filled}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete.

---

STEP S-0 -- READ TOPICS.md

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

CONSTRAINT: S-0 performs this read and emit only.
  No category lookup.
  No skill selection.
  No mock generation.

S-0 is complete when the emit line above is written. S-1 begins after S-0 is complete.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock using values from S-0:
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

If the skill is not in any group, emit an error naming the unrecognized skill-id and
the available registry, then stop.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

Evaluate the rows in order. Use the first matching Condition. Stop at first match.

  | Condition                                                              | FLAG value                                                    |
  |------------------------------------------------------------------------|---------------------------------------------------------------|
  | CATEGORY = HIGH-STRUCTURE AND skill matches `trace-*` AND tier >= 2   | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)" |
  | CATEGORY = HIGH-STRUCTURE AND skill = scout-feasibility AND tier >= 2  | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)" |
  | CATEGORY = HIGH-STRUCTURE AND skill matches `listen-*` AND tier >= 2   | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)" |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                            | "none (structural coverage reliable)"                         |
  | CATEGORY = EVIDENCE-HEAVY                                              | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)" |
  | CATEGORY = MIXED                                                       | "REVIEW-FOR-PLAUSIBILITY"                                     |

Compliance override -- applied after table lookup, regardless of row matched above:
  If compliance tags are present in TOPICS.md AND skill is scout-compliance or
  trace-permissions (any tier, any category):
  FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability: FLAG MUST NOT be recomputed anywhere in this run.

CONFIRMATION REQUIRED before writing the cross-site reference row:

  Phase 1: locate [S-3:CS] in P-0 table, row 1.
  Phase 2 (Steps 2a-2d): read Step=S-3 + Row type=Cross-site reference row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [S-3:CS]                 |
  | Step       | S-3                      |
  | Row type   | Cross-site reference row |
  | Match      | _______________          |

Cross-site reference [S-3:CS]: Failure to copy FLAG verbatim at A-1 produces a
category mismatch at [A-1:FC] invisible to downstream tooling.

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

First rule: Copy FLAG from S-3 verbatim. Do not rederive it.

CONFIRMATION REQUIRED before writing the failure consequence row:

  Phase 1: locate [A-1:FC] in P-0 table, row 2.
  Phase 2 (Steps 2a-2d): read Step=A-1 + Row type=Failure consequence row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [A-1:FC]                 |
  | Step       | A-1                      |
  | Row type   | Failure consequence row  |
  | Match      | _______________          |

Failure consequence [A-1:FC]: Re-deriving FLAG corrupts the artifact's trust tier
silently. [Mutual target of S-3:CS]

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

All six fields present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section after the header. Separate with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. A real {skill-id} run is required before
    any evidence-based decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are reliable.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
Body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.

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

Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-05 -- Convergent (all three axes)

**Axis**: Full convergence -- P-0 cross-reference protocol + S-0 CONSTRAINT naming prohibited ops by functional type + S-1 skill selection only + S-3 FLAG table with `trace-*` and `listen-*` in Condition column cells + A-1 through A-5 assembly.
**Hypothesis**: The three gaps are independent: C-12/C-15 live at the S-0/S-1 boundary; C-16 lives at S-3. Adding all three fixes simultaneously is non-interfering. The three axes are additive: S-0 CONSTRAINT names what S-0 cannot do (satisfying C-15, and the boundary satisfies C-12 structurally); the FLAG table moves wildcards from case-prose bodies into Condition cells (satisfying C-16); P-0 and A-1...A-5 were already present (C-14). All 16 criteria predicted to pass.
**Predicts**: C-01 through C-16 all pass.
**Expected composite**: 16 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

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

STEP S-0 -- READ TOPICS.md

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

CONSTRAINT: S-0 performs this read and emit only.
  No category lookup.
  No skill selection.
  No mock generation.

S-0 is complete when the emit line above is written. S-1 begins only after S-0 is complete.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock using values established in S-0:
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

If the skill is not in any group, emit an error naming the unrecognized skill-id and
the available registry, then stop.

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

Evaluate the rows in order. Use the first matching Condition. Stop at first match.

  | Condition                                                              | FLAG value                                                       |
  |------------------------------------------------------------------------|------------------------------------------------------------------|
  | CATEGORY = HIGH-STRUCTURE AND skill matches `trace-*` AND tier >= 2   | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"  |
  | CATEGORY = HIGH-STRUCTURE AND skill = scout-feasibility AND tier >= 2  | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"  |
  | CATEGORY = HIGH-STRUCTURE AND skill matches `listen-*` AND tier >= 2   | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"  |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                            | "none (structural coverage reliable)"                            |
  | CATEGORY = EVIDENCE-HEAVY                                              | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"   |
  | CATEGORY = MIXED                                                       | "REVIEW-FOR-PLAUSIBILITY"                                        |

Compliance override -- applied after table lookup, regardless of row matched above:
  If compliance tags are present in TOPICS.md AND skill is scout-compliance or
  trace-permissions (any tier, any category):
  FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                  |
  |-------------------------|-----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                      |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration      |
  |                         | sequence, or any other execution context                              |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value          |
  |                         | emitted here                                                          |
  | No-exemption            | No path is exempt                                                     |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a        |
  |                         | corrupted value indistinguishable from a correctly-computed one        |
  | Guarantee-break         | This violation breaks the closure guarantee stated above               |

CONFIRMATION REQUIRED before writing the cross-site reference row:

  Phase 1: locate [S-3:CS] in P-0 table, row 1.
  Phase 2 (Steps 2a-2d): read Step=S-3 + Row type=Cross-site reference row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [S-3:CS]                 |
  | Step       | S-3                      |
  | Row type   | Cross-site reference row |
  | Match      | _______________          |

Cross-site reference [S-3:CS]: The failure produces a silent category mismatch at
[A-1:FC] -- the Failure consequence row in step A-1 (that row identifies itself as
this row's mutual target).

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                  |
  |-------------------------|-----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                      |
  | Priority                | This rule is first -- it applies before any other instruction          |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any    |
  |                         | formatting instruction, or any other instruction in this step         |
  | No-exemption            | No instruction in this step is exempt                                 |

CONFIRMATION REQUIRED before writing the failure consequence row:

  Phase 1: locate [A-1:FC] in P-0 table, row 2.
  Phase 2 (Steps 2a-2d): read Step=A-1 + Row type=Failure consequence row;
  assert match; emit confirmation record (fill Match only):

  | Field      | Value                    |
  |------------|--------------------------|
  | Token      | [A-1:FC]                 |
  | Step       | A-1                      |
  | Row type   | Failure consequence row  |
  | Match      | _______________          |

Failure consequence [A-1:FC]: [Mutual target of S-3:CS -- Cross-site reference row in S-3]
Re-deriving FLAG here produces a category mismatch invisible to downstream tooling that
silently corrupts the artifact's trust tier.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

All six fields present. The header appears immediately after any frontmatter.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Separate from
header and from body with --- delimiters.

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

| Variation | Axis | C-12 | C-14 | C-15 | C-16 | Predicted score |
|-----------|------|------|------|------|------|-----------------|
| V-01 | FLAG table Condition column | fail | pass | fail | **pass** | ~14/16 |
| V-02 | S-0 CONSTRAINT named prohibitions | **pass** | pass | **pass** | fail | ~15/16 |
| V-03 | Plain S-0 separation, no P-0 | **pass** | pass | fail | fail | ~14/16 |
| V-04 | S-0 CONSTRAINT + FLAG wildcard table | **pass** | pass | **pass** | **pass** | **16/16** |
| V-05 | Convergent (all axes + immutability chain) | **pass** | pass | **pass** | **pass** | **16/16** |

V-04 and V-05 are both predicted to pass all 16. The structural difference is V-05 adds the FLAG immutability chain table in S-3 and the FLAG prohibition chain table in A-1 -- which are likely the seeds of C-17+ criteria in v4.
