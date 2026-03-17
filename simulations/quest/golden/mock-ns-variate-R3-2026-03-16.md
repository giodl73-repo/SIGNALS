---
skill: quest-variate
skill_target: mock-ns
round: 3
rubric_version: 3
date: 2026-03-16
---

# mock-ns -- Round 3 Variations

Rubric: v3 (C-01 through C-16, 5 essential / 3 recommended / 8 aspirational).

New criteria in v3 (extracted from R2 V-05 excellence evidence):
- **C-14** -- Assembly expressed as discrete named steps A-1 through A-5
- **C-15** -- CONSTRAINT block names prohibited S-0 operations by type (no category
  lookup, no skill selection, no mock generation)
- **C-16** -- Wildcard patterns `trace-*`, `listen-*` appear in FLAG table condition
  column cell, not only in footnotes

R2 V-05 was promoted to T3 SKILL.md. Audit against v3 reveals three open gaps:

- **C-12 gap**: T3 merges TOPICS.md read into S-1 alongside skill selection. The C-12
  pass condition requires TOPICS.md to complete in its own step *before* S-1 skill
  selection begins. Same-step does not satisfy the criterion.
- **C-15 gap**: T3 has no dedicated S-0 with a CONSTRAINT block naming prohibited
  operations by functional type. S-3 has a FLAG immutability chain, but S-0 prohibition
  language is absent.
- **C-16 gap**: T3's S-3 uses case-prose for FLAG computation. Wildcards `trace-*` and
  `listen-*` appear in Case 1 prose text but not inside a FLAG table condition column
  cell. C-16 requires the wildcard to appear in the cell itself.

C-14 is satisfied by T3 SKILL.md: steps A-1 through A-5 (ASSEMBLE HEADER, FIDELITY
WARNING, GENERATE ARTIFACT BODY, WRITE ARTIFACT, NEXT-STEP LINE) are present and
labeled.

R3 isolates: (a) whether a FLAG table with wildcard patterns directly in the Condition
column satisfies C-16 independently; (b) whether S-0 separation with a CONSTRAINT naming
op types by name satisfies C-15 (and incidentally fixes C-12); (c) whether S-0/S-1
separation without P-0 machinery is sufficient for C-12 alone; (d) whether C-15 and C-16
stack without interference; then convergent.

Three axes selected for single-axis isolation:

1. **FLAG table condition column (C-16)** -- Replace S-3 case prose with a lookup table
   whose Condition column cells contain `trace-*` and `listen-*` wildcards directly.
   Tests whether moving the wildcard from prose body to table condition cell is the
   load-bearing signal for C-16. Everything else from T3 SKILL.md is preserved.
2. **S-0 CONSTRAINT with named type prohibitions (C-15 + C-12)** -- Add S-0 as a
   dedicated TOPICS.md step before S-1, with a CONSTRAINT block naming: "No category
   lookup. No skill selection. No mock generation." Tests whether naming prohibited
   operations by functional type (not by step order) satisfies C-15, and whether the
   step separation incidentally satisfies C-12.
3. **Clean S-0 separation, no P-0 protocol (C-12 isolation)** -- Strip the cross-
   reference token machinery (P-0) and present S-0 as a dedicated TOPICS.md step with
   plain ordering language. Tests whether C-12 is satisfied by step-label separation
   alone, without the CONSTRAINT prohibition or P-0 overhead.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | FLAG table condition column (C-16) | A FLAG computation table whose Condition column cells contain `trace-*` and `listen-*` wildcards directly -- not in a footnote or prose expansion below -- is the minimal sufficient signal for C-16. C-12 and C-15 are not addressed (S-1 still merges TOPICS.md + skill selection; no S-0 CONSTRAINT with named types). Predicts C-14 pass, C-15 fail, C-16 pass, C-12 fail. |
| V-02 | S-0 CONSTRAINT with named prohibitions (C-15 + C-12) | A dedicated S-0 step whose CONSTRAINT block names prohibited operations by functional type ("No category lookup. No skill selection. No mock generation.") satisfies C-15. The S-0/S-1 step separation also incidentally satisfies C-12. FLAG stays as case prose (no wildcard table). C-16 not addressed. Predicts C-12 pass, C-14 pass, C-15 pass, C-16 fail. |
| V-03 | Clean S-0 separation, no P-0 (C-12 isolation) | Stripping P-0 cross-reference machinery and presenting S-0 as a dedicated TOPICS.md step with plain ordering language satisfies C-12 via step-label separation alone. Tests whether P-0 is necessary for C-12 or whether the step boundary alone is the load-bearing signal. C-15 and C-16 not addressed. Predicts C-12 pass, C-14 pass, C-15 fail, C-16 fail. |
| V-04 | S-0 CONSTRAINT + FLAG wildcard table (C-15 + C-16, two-axis) | Combining the S-0 CONSTRAINT with named prohibitions (V-02) and the FLAG wildcard table (V-01) satisfies C-15, C-16, and C-12 simultaneously without interference. C-14 maintained (A-1...A-5). Tests stacking: both axes should be additive. Predicts C-12 pass, C-14 pass, C-15 pass, C-16 pass. |
| V-05 | Convergent (all axes) | P-0 cross-reference protocol + S-0 CONSTRAINT naming prohibited ops by functional type + S-1 skill selection only + S-3 FLAG table with `trace-*`, `listen-*` in Condition column + A-1 through A-5 assembly. Closes all three T3 gaps. All 16 criteria predicted to pass. |

---

## V-01 -- FLAG Table Condition Column (C-16)

**Axis**: FLAG table condition column -- S-3 flag computation replaced with a lookup
table whose Condition column cells contain `trace-*` and `listen-*` wildcards directly
in the match expression.
**Hypothesis**: C-16 requires the wildcard patterns to appear in the Condition column
cell itself, not in a footnote or prose expansion below the table. Expressing the
critical-skill condition as "skill matches `trace-*`" and "skill matches `listen-*`"
directly inside the table cells is the minimal change that satisfies C-16. The P-0
cross-reference protocol and A-1...A-5 assembly steps are preserved from T3 SKILL.md.
S-1 still merges TOPICS.md with skill selection -- C-12 is not addressed. No S-0
CONSTRAINT with named op types -- C-15 is not addressed.
**Predicts**: C-01 through C-11 pass | C-12 fail | C-13 pass | C-14 pass | C-15 fail |
C-16 pass.
**Expected composite**: ~14 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

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
             current use site; fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill       | Exclusion constraint                                       |
  |-----------|---------------------|------------------------------------------------------------|
  | scout     | scout-feasibility   |                                                            |
  | draft     | draft-spec          |                                                            |
  | review    | review-design       |                                                            |
  | flow      | flow-resilience     |                                                            |
  | trace     | trace-request       |                                                            |
  | prove     | prove-hypothesis    |                                                            |
  | listen    | listen-support      |                                                            |
  | program   | program-plan        |                                                            |
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

Compute FLAG from CATEGORY, tier, and skill-id using this lookup table.
Evaluate conditions top-to-bottom; use the flag from the first matching row:

  | Condition                                                              | Flag                                                              |
  |------------------------------------------------------------------------|-------------------------------------------------------------------|
  | CATEGORY = HIGH-STRUCTURE, skill matches trace-*, tier >= 2            | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE, skill = scout-feasibility, tier >= 2        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE, skill matches listen-*, tier >= 2           | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                            | none (structural coverage reliable)                               |
  | CATEGORY = EVIDENCE-HEAVY                                              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | CATEGORY = MIXED                                                       | REVIEW-FOR-PLAUSIBILITY                                           |

Compliance override (check last, applied regardless of table result above):
  If compliance tags are present in TOPICS.md AND skill is scout-compliance or
  trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context                             |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated above             |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below.         |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1                  |

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
  | Priority                | This rule is first in this step -- applies before any other          |
  |                         | instruction                                                          |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below.         |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells is a protocol failure.                                |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS] Re-deriving FLAG here silently corrupts    |
  |                         | the artifact's trust tier; the corruption is undetectable without    |
  |                         | manual header inspection.                                            |

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
```

---

## V-02 -- S-0 CONSTRAINT with Named Type Prohibitions (C-15 + C-12)

**Axis**: Dedicated S-0 step with CONSTRAINT block naming prohibited operations by
functional type. S-1 becomes skill-selection only. FLAG computation stays as case prose.
**Hypothesis**: C-15 requires the CONSTRAINT block to name prohibited operations *by
functional type*, not by step order. The rubric's parenthetical supplies the exact
type names: "no category lookup, no skill selection, no mock generation." Writing
"CONSTRAINT: No category lookup. No skill selection. No mock generation." directly in
S-0 satisfies C-15. The S-0/S-1 separation also incidentally satisfies C-12 (tier
resolved before skill selection begins). C-16 not addressed -- S-3 case prose remains;
wildcards appear in prose, not in a table Condition column cell.
**Predicts**: C-01 through C-12 pass | C-13 pass | C-14 pass | C-15 pass | C-16 fail.
**Expected composite**: ~15 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

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
    Step 2d: Emit confirmation record (fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

Locate-only is a protocol failure.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: No category lookup. No skill selection. No mock generation.
None of these operations may begin until the TOPICS.md emit line below is written.

Read TOPICS.md. Emit this exact line (all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Resolution rules:
  - existence: "found" if topic is registered in TOPICS.md; "not found" if absent
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided
  - compliance tags: tag list from TOPICS.md; "none" if absent or unregistered

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill       | Exclusion constraint                                       |
  |-----------|---------------------|------------------------------------------------------------|
  | scout     | scout-feasibility   |                                                            |
  | draft     | draft-spec          |                                                            |
  | review    | review-design       |                                                            |
  | flow      | flow-resilience     |                                                            |
  | trace     | trace-request       |                                                            |
  | prove     | prove-hypothesis    |                                                            |
  | listen    | listen-support      |                                                            |
  | program   | program-plan        |                                                            |
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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration  |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated above             |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record below. DO NOT WRITE until complete.  |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row type |
  | [P-0:ABD]               | cells, or without performing Phase 2, is a protocol failure.         |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [A-1:FC]  |

Confirmation record:

**Executor: fill the Match field only.**

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
  | Priority                | Applies before any other instruction in this step                    |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record below.                               |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row type |
  | [P-0:ABD]               | cells is a protocol failure.                                         |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS] Re-deriving FLAG here silently corrupts    |
  |                         | the artifact's trust tier.                                           |

Confirmation record:

**Executor: fill the Match field only.**

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

All six fields present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning immediately after the header, before any
mock content. Separate with --- delimiters.

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

A reader familiar with the real skill must be able to identify which skill was mocked
from the body alone, without reading the header.

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

## V-03 -- Clean S-0 Separation, No P-0 Protocol (C-12 Isolation)

**Axis**: P-0 cross-reference machinery stripped. S-0 is a dedicated TOPICS.md step
with plain ordering language ("before any other step begins"). S-1 is skill selection
only. A-1 through A-5 assembly steps preserved as clean labeled sections.
**Hypothesis**: C-12 requires that TOPICS.md tier is resolved in a step that precedes
S-1 skill selection. The pass condition says step-labeled separation with an explicit
tier-carry handoff sentence satisfies C-12 -- a CONSTRAINT block is not required. If
this variation passes C-12, step-label separation alone is the load-bearing signal and
P-0 is not necessary. If it underperforms V-02, the CONSTRAINT block in S-0 is
contributing to C-12 compliance beyond the step label. C-15 not addressed (no named-
type CONSTRAINT). C-16 not addressed (case prose in S-3).
**Predicts**: C-01 through C-12 pass | C-13 pass | C-14 pass | C-15 fail | C-16 fail.
**Expected composite**: ~14 of 16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

Before any other step begins, read TOPICS.md. Emit this exact line (all three fields
required -- do not omit any):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Resolution rules:
  - existence: "found" if topic is registered in TOPICS.md; "not found" if absent
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided
  - compliance tags: tag list from TOPICS.md; "none" if absent or unregistered

Carry the resolved tier into S-2 and S-3. Do not begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill       | Exclusion constraint                                       |
  |-----------|---------------------|------------------------------------------------------------|
  | scout     | scout-feasibility   |                                                            |
  | draft     | draft-spec          |                                                            |
  | review    | review-design       |                                                            |
  | flow      | flow-resilience     |                                                            |
  | trace     | trace-request       |                                                            |
  | prove     | prove-hypothesis    |                                                            |
  | listen    | listen-support      |                                                            |
  | program   | program-plan        |                                                            |
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

FLAG is computed exactly once in this step and must not be recomputed or modified
anywhere in this run.

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

FLAG is now resolved. Copy it verbatim into A-1. Do not rederive it.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it from CATEGORY or tier.

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

Write the category-matched fidelity warning immediately after the header, before any
mock content. Separate with --- delimiters.

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

A reader familiar with the real skill must be able to identify which skill was mocked
from the body alone, without reading the header.

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

## V-04 -- S-0 CONSTRAINT + FLAG Wildcard Table (C-15 + C-16, Two-Axis)

**Axis**: S-0 with named-type CONSTRAINT (V-02 axis) combined with FLAG table using
wildcard conditions in the Condition column (V-01 axis). Two-axis combination test.
**Hypothesis**: C-15 and C-16 are independent: the S-0 CONSTRAINT addresses how the
step gate is expressed; the FLAG table addresses how critical-skill conditions are
encoded. Combining both satisfies both criteria without interference. C-12 also passes
as a side effect of S-0/S-1 separation. C-14 is maintained (A-1...A-5). The P-0
cross-reference protocol is preserved for FLAG immutability robustness. If this
variation matches V-02 + V-01 independently on their target criteria, the axes stack
additively and all four open gaps (C-12, C-15, C-16, and the implied C-14 clean-up)
are closed by one prompt.
**Predicts**: C-01 through C-16 all pass.
**Expected composite**: 16/16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

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
    Step 2d: Emit confirmation record (fill in the Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is
    emitted.

Locate-only is a protocol failure.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: No category lookup. No skill selection. No mock generation.
None of these operations may begin until the TOPICS.md emit line below is written.

Read TOPICS.md. Emit this exact line (all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Resolution rules:
  - existence: "found" if topic is registered in TOPICS.md; "not found" if absent
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided
  - compliance tags: tag list from TOPICS.md; "none" if absent or unregistered

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

  | Namespace | Default skill       | Exclusion constraint                                       |
  |-----------|---------------------|------------------------------------------------------------|
  | scout     | scout-feasibility   |                                                            |
  | draft     | draft-spec          |                                                            |
  | review    | review-design       |                                                            |
  | flow      | flow-resilience     |                                                            |
  | trace     | trace-request       |                                                            |
  | prove     | prove-hypothesis    |                                                            |
  | listen    | listen-support      |                                                            |
  | program   | program-plan        |                                                            |
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

Compute FLAG from CATEGORY, tier, and skill-id using this lookup table.
Evaluate conditions top-to-bottom; use the flag from the first matching row:

  | Condition                                                              | Flag                                                              |
  |------------------------------------------------------------------------|-------------------------------------------------------------------|
  | CATEGORY = HIGH-STRUCTURE, skill matches trace-*, tier >= 2            | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE, skill = scout-feasibility, tier >= 2        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE, skill matches listen-*, tier >= 2           | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                            | none (structural coverage reliable)                               |
  | CATEGORY = EVIDENCE-HEAVY                                              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | CATEGORY = MIXED                                                       | REVIEW-FOR-PLAUSIBILITY                                           |

Compliance override (check last, applied regardless of table result above):
  If compliance tags are present in TOPICS.md AND skill is scout-compliance or
  trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration  |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated above             |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record below. DO NOT WRITE until complete.  |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row type |
  | [P-0:ABD]               | cells, or without performing Phase 2, is a protocol failure.         |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [A-1:FC]  |

Confirmation record:

**Executor: fill the Match field only.**

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
  | Priority                | Applies before any other instruction in this step                    |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record below.                               |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row type |
  | [P-0:ABD]               | cells is a protocol failure.                                         |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS] Re-deriving FLAG here silently corrupts    |
  |                         | the artifact's trust tier.                                           |

Confirmation record:

**Executor: fill the Match field only.**

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

All six fields present. Header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the category-matched fidelity warning immediately after the header, before any
mock content. Separate with --- delimiters.

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

A reader familiar with the real skill must be able to identify which skill was mocked
from the body alone, without reading the header.

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

## V-05 -- Convergent (All Axes)

**Axis**: P-0 cross-reference protocol + S-0 CONSTRAINT naming prohibited ops by
functional type + S-1 skill selection only + S-2 category as two-column table +
S-3 FLAG table with `trace-*`, `listen-*` in Condition column + A-1 through A-5
assembly.
**Hypothesis**: Combining all three axes in the same prompt satisfies C-12 (S-0 before
S-1), C-15 (CONSTRAINT with named op types at S-0), and C-16 (wildcard conditions in
FLAG table Condition cell) simultaneously. The three changes are architecturally
independent -- each targets a different section (S-0, S-3) and a different behavioral
property (step gate, operation prohibition, condition encoding). P-0 is retained for
FLAG immutability robustness. The S-2 category table is included for C-02/C-13
robustness (reduces skill-id mismatch risk).

The key claim: S-0 CONSTRAINT must name operations by *functional type* ("No category
lookup. No skill selection. No mock generation."), not by step reference. The FLAG
table must place `trace-*` and `listen-*` in the Condition column cells, not in a
footnote. These two changes, combined with the inherited A-1...A-5 assembly steps and
S-0/S-1 separation, close all three open gaps in T3 SKILL.md.
**Predicts**: C-01 through C-16 all pass.
**Expected composite**: 16/16 criteria pass.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

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
token in the table above. P-0 table, row 1 = [S-3:CS]; row 2 = [A-1:FC]; row 3 =
[P-0:ABD].

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

CONSTRAINT: No category lookup. No skill selection. No mock generation.
None of these operations may begin until the TOPICS.md emit line below is written.

Read TOPICS.md. Emit this exact text (all three fields required -- do not omit any):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill       | Exclusion constraint                                       |
  |-----------|---------------------|------------------------------------------------------------|
  | scout     | scout-feasibility   |                                                            |
  | draft     | draft-spec          |                                                            |
  | review    | review-design       |                                                            |
  | flow      | flow-resilience     |                                                            |
  | trace     | trace-request       |                                                            |
  | prove     | prove-hypothesis    |                                                            |
  | listen    | listen-support      |                                                            |
  | program   | program-plan        |                                                            |
  | topic     | topic-plan          | NEVER topic-status (excluded: meta-structural)             |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                         |
  |----------------|-----------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,            |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,             |
  |                | draft-proposal, draft-pitch, review-design, review-code,              |
  |                | trace-request, trace-component, trace-contract, trace-state,          |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,      |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,       |
  |                | flow-trigger, flow-integration, program-plan                          |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                     |
  |                | listen-feedback, listen-support, listen-adoption                      |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers, review-users   |

If the skill is not in any row, emit an error naming the unrecognized skill-id and
the available registry, then stop.

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

Compute FLAG from CATEGORY, tier, and skill-id using this lookup table.
Evaluate conditions top-to-bottom; use the flag from the first matching row:

  | Condition                                                              | Flag                                                              |
  |------------------------------------------------------------------------|-------------------------------------------------------------------|
  | CATEGORY = HIGH-STRUCTURE, skill matches trace-*, tier >= 2            | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE, skill = scout-feasibility, tier >= 2        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE, skill matches listen-*, tier >= 2           | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                            | none (structural coverage reliable)                               |
  | CATEGORY = EVIDENCE-HEAVY                                              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | CATEGORY = MIXED                                                       | REVIEW-FOR-PLAUSIBILITY                                           |

Compliance override (check last, applied regardless of table result above):
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
  | Guarantee-break         | This violation breaks the closure guarantee stated above             |
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
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the exact golden structural pattern of the selected
skill. The body must include:
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative

A reader familiar with the real {skill-id} output must be able to identify the skill
from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace (mock-review controls the next step in that context).
```

---

## Predicted scorecard

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 header fields | pass | pass | pass | pass | pass |
| C-02 category correct | pass | pass | pass | pass | pass |
| C-03 flag correct | pass | pass | pass | pass | pass |
| C-04 fidelity warning | pass | pass | pass | pass | pass |
| C-05 skill-specific body | pass | pass | pass | pass | pass |
| C-06 setup emit lines | pass | pass | pass | pass | pass |
| C-07 write path + confirm | pass | pass | pass | pass | pass |
| C-08 next-step line | pass | pass | pass | pass | pass |
| C-09 topic exclusion | pass | pass | pass | pass | pass |
| C-10 compliance override | pass | pass | pass | pass | pass |
| C-11 FLAG covers all 5 cases | pass | pass | pass | pass | pass |
| C-12 S-0 before S-1 | fail | pass | pass | pass | pass |
| C-13 error on unknown skill | pass | pass | pass | pass | pass |
| C-14 A-1 through A-5 steps | pass | pass | pass | pass | pass |
| C-15 CONSTRAINT names op types | fail | pass | fail | pass | pass |
| C-16 wildcards in condition cell | pass | fail | fail | pass | pass |
| **Predicted pass count** | **14/16** | **15/16** | **14/16** | **16/16** | **16/16** |

Key discriminations this round:
- V-01 vs V-02: isolates C-16 (FLAG table cell) vs C-15 (CONSTRAINT naming) independently
- V-01 vs V-03: C-16 isolated vs C-12; both fail C-15 but differ on C-12 and C-16
- V-02 vs V-03: whether CONSTRAINT at S-0 adds to C-12 beyond step-label separation alone
- V-04: two-axis stacking check -- if both single-axis pass their targets, V-04 passes all
- V-05: full convergent -- closes all three T3 gaps (C-12, C-15, C-16) in one prompt
