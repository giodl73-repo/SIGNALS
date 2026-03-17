Good. R14 exhausted phrasing-register variants of the TOPICS.md emission ordering sentence — V-03 (focus-particle) and V-05 (temporal-clause) both scored 146/146. R15 should now test structural axes while carrying the proven V-03 phrasing forward. Let me write the five complete variations.

---

# mock-ns — Round 15 Variations (rubric v15, 2026-03-17)

**Rubric**: v15 (C-01–C-41, max 146)
**Phrasing baseline carried forward**: R14 V-03 focus-particle ("Only this step emits…") — 146/146 under v15.
**R15 axis targets**: role sequence, output format, lifecycle emphasis, and two combinations. All single-axis variations first.

**Context**: R14 fully explored the phrasing-register axis for the TOPICS.md emission ordering sentence. V-03 and V-05 both converged at 146/146 under v15. R15 pivots to structural axes — the FLAG computation path, step ordering, and phase boundary explicitness — to test whether structural changes open new failure modes or reinforce 146/146.

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format — decision table for CATEGORY/FLAG | Collapsing prose case logic into one lookup table removes the multi-step derivation chain that creates FLAG mutation risk |
| V-02 | Lifecycle emphasis — explicit entry/exit state per step | Named state contracts at each step boundary prevent step-skip and FLAG inheritance failures |
| V-03 | Role sequence — FLAG-first (inputs only), TOPICS.md second | Pre-computing FLAG from namespace+tier before any content read eliminates all content-phase mutation paths |
| V-04 | Combination: V-01 + V-02 (table + lifecycle gates) | Decision table + phase contracts should yield the strongest structural guarantee against both derivation and mutation errors |
| V-05 | Combination: V-03 + V-01 (FLAG-first + table) | Front-loading FLAG via table lookup should maximize immutability surface without adding verbosity from V-02's state declarations |

---

## V-01 — Single axis: Output format (decision table replaces prose case logic)

**Axis**: Output format — replace S-2 (prose category) and S-3 (prose FLAG cases) with a single consolidated CATEGORY-FLAG lookup table. One table row per combination. Executor does one lookup; no conditional branching in prose.

**Hypothesis**: The current skill uses two sequential prose derivations (S-2 assigns CATEGORY, S-3 applies case logic to get FLAG). A single lookup table removes the sequential dependency and the surface area where FLAG could be re-derived. Executor reads one row, extracts both values, proceeds.

```
depth: standard

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
Anti-bypass echo rows at S-2 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-2:CS]   | S-2  | Cross-site reference row    | [A-1:FC]     | forward --> names A-1        |
  | [A-1:FC]   | A-1  | Failure consequence row     | [S-2:CS]     | <-- backward, names S-2      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-2:CS]; P-0 table, row 2 = [A-1:FC];
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

Read TOPICS.md. Only this step emits the TOPICS.md status line; no subsequent step
repeats this emission. Emit:
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

STEP S-2 -- CATEGORY AND FLAG LOOKUP

CATEGORY and FLAG are assigned in a single lookup. Find the row matching your
(namespace/skill-id, tier, compliance) combination. Read CATEGORY and FLAG from
that row. Do not derive either value by any other means.

  | Skill                                                   | Tier | Compliance tag? | CATEGORY       | FLAG                                                         |
  |---------------------------------------------------------|------|-----------------|----------------|--------------------------------------------------------------|
  | scout-feasibility, any trace-*, any listen-*            | 2+   | no              | HIGH-STRUCTURE | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)|
  | scout-feasibility, any trace-*, any listen-*            | 1    | no              | HIGH-STRUCTURE | none (structural coverage reliable)                          |
  | scout-feasibility, any trace-*, any listen-*            | any  | yes             | HIGH-STRUCTURE | REAL-REQUIRED (compliance-sensitive)                         |
  | scout-stakeholders, scout-requirements, scout-naming,   | any  | no              | HIGH-STRUCTURE | none (structural coverage reliable)                          |
  | scout-compliance, scout-market, draft-spec,             |      |                 |                |                                                              |
  | draft-proposal, draft-pitch, review-design,             |      |                 |                |                                                              |
  | review-code, trace-skill, flow-resilience,              |      |                 |                |                                                              |
  | flow-dataflow, flow-conversation, flow-lifecycle,       |      |                 |                |                                                              |
  | flow-throttle, flow-trigger, flow-integration,          |      |                 |                |                                                              |
  | program-plan                                            |      |                 |                |                                                              |
  | scout-compliance, trace-permissions                     | any  | yes             | HIGH-STRUCTURE | REAL-REQUIRED (compliance-sensitive)                         |
  | prove-websearch, prove-interview, prove-prototype,      | any  | no              | EVIDENCE-HEAVY | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed) |
  | listen-feedback, listen-support, listen-adoption        |      |                 |                |                                                              |
  | scout-competitors, prove-hypothesis,                    | any  | no              | MIXED          | REVIEW-FOR-PLAUSIBILITY                                      |
  | review-customers, review-users                          |      |                 |                |                                                              |

CATEGORY and FLAG are now fixed. They are named variables. Do not recompute or
modify them anywhere in this run.

FLAG immutability: CATEGORY and FLAG were assigned in this step. They carry forward
unchanged to A-1. Any re-derivation in a later step corrupts the artifact trust tier.

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | assigned here                                                        |
  | No-exemption            | No path is exempt                                                    |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-2:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-2 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below.         |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Cross-site ref [S-2:CS] | The failure produces the same silent category mismatch at            |
  |                         | [A-1:FC] -- the Failure consequence row in step A-1                  |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-2:CS]                       |
  | Step       | S-2                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

CATEGORY and FLAG are now resolved. Do not re-evaluate or modify them.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-2 verbatim. Do not rederive it.                     |
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
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below.         |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Failure conseq [A-1:FC] | [Mutual target of S-2:CS -- Cross-site reference row in S-2]         |
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
  Flag: {FLAG from S-2 -- copied verbatim, not rederived}

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

## V-02 — Single axis: Lifecycle emphasis (explicit entry/exit state contracts)

**Axis**: Lifecycle emphasis — each step begins with an ENTRY STATE declaration (what named variables must exist before this step runs) and ends with an EXIT STATE declaration (what named variables are now resolved). Steps are explicit state-machine transitions.

**Hypothesis**: The current skill relies on prose flow between steps. Adding named state contracts at each boundary makes the FLAG handoff from S-3 → A-1 explicit as a state-machine assertion, not just an instruction. This should prevent step-skip failures and make the immutability chain structurally verifiable.

```
depth: standard

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

Locate-only is a protocol failure. Do not re-establish this protocol in later steps.

  EXIT STATE (P-0): token table established, lookup protocol defined, ABD active.

---

STEP S-1 -- SETUP

  ENTRY STATE: inputs resolved ({topic}, {namespace}, {skill-id} or default, {tier}).
  TOPICS.md not yet read. SKILL-ID not yet selected.

Read TOPICS.md. Only this step emits the TOPICS.md status line; no subsequent step
repeats this emission. Emit:
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

  EXIT STATE (S-1): SKILL-ID resolved. TOPICS.md read. Compliance tags known.
  CATEGORY = unset. FLAG = unset.

---

STEP S-2 -- DETERMINE CATEGORY

  ENTRY STATE: SKILL-ID resolved. Compliance tags known. CATEGORY = unset. FLAG = unset.

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

  EXIT STATE (S-2): CATEGORY assigned (one of HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED).
  FLAG = unset.

---

STEP S-3 -- COMPUTE FLAG

  ENTRY STATE: CATEGORY assigned. Compliance tags known. FLAG = unset.
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
  |                         | sequence, or any other execution context                             |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                         | corrupted value                                                      |
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

  EXIT STATE (S-3): FLAG assigned and immutable. CATEGORY assigned and immutable.
  Both values carry forward verbatim to A-1. No step between S-3 and A-1 may read,
  write, or branch on FLAG for any purpose other than verbatim copy.

---

STEP A-1 -- ASSEMBLE HEADER

  ENTRY STATE: FLAG = value from S-3 (verbatim). CATEGORY = value from S-2 (verbatim).
  Both values are treated as read-only in this step.

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | This rule is first in this step -- before any other instruction      |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record from pre-filled table below.         |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol         |
  |                         | failure.                                                             |
  | Failure conseq [A-1:FC] | [Mutual target of S-3:CS]                                            |
  |                         | Re-deriving FLAG here silently corrupts the artifact's trust tier    |

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

  EXIT STATE (A-1): header block written with verbatim FLAG. CATEGORY used for fidelity
  warning selection in A-2.

---

STEP A-2 -- FIDELITY WARNING

  ENTRY STATE: header block complete. CATEGORY known (from S-2, read-only).

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

  EXIT STATE (A-2): fidelity warning written.

---

STEP A-3 -- GENERATE ARTIFACT BODY

  ENTRY STATE: header complete, fidelity warning written. SKILL-ID known (from S-1).

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

  EXIT STATE (A-3): mock body complete. Artifact ready to write.

---

STEP A-4 -- WRITE ARTIFACT

  ENTRY STATE: complete artifact in memory (header + warning + body).

Write the complete artifact to:
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

## V-03 — Single axis: Role sequence (FLAG-first, inputs-only pre-computation)

**Axis**: Role sequence — invert step order so CATEGORY and FLAG are computed in Step 1 from the inputs alone ({namespace}, {tier}), before TOPICS.md is read. TOPICS.md read happens in Step 2 and can only trigger the compliance override (a narrow, named exception path). Content generation follows in Steps 3–5.

**Hypothesis**: In the baseline skill, FLAG is computed in S-3 (step 3) after TOPICS.md has been read and the skill selected. There is a 2-step window (S-1 to S-3) during which the executor holds intermediate state that could be contaminated. By computing CATEGORY and FLAG at Step 1 from pure inputs, the FLAG is immutable before any content-processing begins. The compliance override is an explicit, narrow amendment path — not a re-derivation.

```
depth: standard

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
Anti-bypass echo rows at S-1 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-1:CS]   | S-1  | Cross-site reference row    | [A-1:FC]     | forward --> names A-1        |
  | [A-1:FC]   | A-1  | Failure consequence row     | [S-1:CS]     | <-- backward, names S-1      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above.

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step and row type matches role of this row.
    Step 2d: Emit confirmation record (fill Match field only):
               Token: {token-name -- pre-filled at use site}
               Step: {step-name -- pre-filled at use site}
               Row type: {row-type-name -- pre-filled at use site}
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete.

Locate-only is a protocol failure. Do not re-establish this protocol in later steps.

---

STEP S-1 -- DETERMINE CATEGORY AND FLAG (inputs only)

CATEGORY and FLAG are computed here, before reading TOPICS.md, from the inputs
{namespace/skill-id} and {tier} alone.

Step S-1 runs first. Only this step resolves CATEGORY and FLAG; no subsequent step
re-derives either value. The compliance override (below) is a named amendment path,
not a re-derivation.

Assign CATEGORY:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

Assign FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

CATEGORY and FLAG are now assigned. Carry them forward to A-1 verbatim.

FLAG immutability chain:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, or other context |
  | Affirmative closure     | Every execution path that reaches A-1 carries the FLAG value here    |
  | No-exemption            | No path is exempt                                                    |
  | Compliance override     | The named exception path in S-2 AMENDS FLAG by one defined rule;    |
  |                         | it does not re-derive it from CATEGORY + tier                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-1:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-1 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below.         |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and      |
  | [P-0:ABD]               | Row type cells, or without performing Phase 2, is a protocol failure.|
  | Cross-site ref [S-1:CS] | Failure produces silent category mismatch at [A-1:FC]                |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-1:CS]                       |
  | Step       | S-1                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

CATEGORY and FLAG are resolved. They do not change unless S-2 compliance override
fires, in which case only FLAG changes by the single defined amendment rule.

---

STEP S-2 -- SETUP (read TOPICS.md; apply compliance override if triggered)

Read TOPICS.md. Only this step emits the TOPICS.md status line; no subsequent step
repeats this emission. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Compliance override (applies only if both conditions are true):
  Condition A: compliance tags are present in TOPICS.md
  Condition B: skill is scout-compliance or trace-permissions

  If both conditions are true:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"
  Otherwise: FLAG is unchanged from S-1.

This is the only permitted FLAG amendment after S-1. It is a single-rule named path,
not a re-derivation from CATEGORY + tier.

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

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-1 (as possibly amended in S-2) verbatim.           |
  |                         | Do not rederive it.                                                  |
  | Priority                | This rule is first -- before any other instruction in this step      |
  | Anti-displacement       | Before any field, before any category lookup, before any formatting  |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert match; |
  | (P-0 table, row 2)      | emit confirmation record. DO NOT WRITE until Steps 2a-2d complete.  |
  | Anti-bypass echo        | Per [P-0:ABD]: locate-only is a protocol failure.                    |
  | [P-0:ABD]               |                                                                      |
  | Failure conseq [A-1:FC] | [Mutual target of S-1:CS]                                            |
  |                         | Re-deriving FLAG here silently corrupts the artifact's trust tier    |

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
  Skill: {skill-id from S-2}
  Topic: {topic}
  Category: {CATEGORY from S-1}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-1, as possibly amended in S-2 -- copied verbatim, not rederived}

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

## V-04 — Combined: Output format + Lifecycle emphasis (decision table + phase state contracts)

**Axes**: V-01 (decision table for CATEGORY/FLAG) + V-02 (explicit ENTRY/EXIT STATE per step).

**Hypothesis**: The table removes conditional prose logic (reducing derivation error surface) and the state contracts make the FLAG handoff visually auditable as a machine transition rather than a prose instruction chain. Together they address two independent failure modes: derivation errors (V-01) and step-skip/mutation errors (V-02). The combination should reinforce 146/146 if each axis independently passes, or surface a new interaction failure mode if they don't.

```
depth: standard

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
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
Anti-bypass echo rows at S-2 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-2:CS]   | S-2  | Cross-site reference row    | [A-1:FC]     | forward --> names A-1        |
  | [A-1:FC]   | A-1  | Failure consequence row     | [S-2:CS]     | <-- backward, names S-2      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above.

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name and row type match the current context.
    Step 2d: Emit confirmation record (fill Match field only):
               Token / Step / Row type: pre-filled at use site
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a-2d complete and record is emitted.

Locate-only is a protocol failure. Do not re-establish this protocol in later steps.

  EXIT STATE (P-0): token table active. Lookup protocol defined. ABD in effect.

---

STEP S-1 -- SETUP

  ENTRY STATE: inputs resolved. TOPICS.md not read. SKILL-ID unresolved.
  CATEGORY = unset. FLAG = unset.

Read TOPICS.md. Only this step emits the TOPICS.md status line; no subsequent step
repeats this emission. Emit:
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

  EXIT STATE (S-1): SKILL-ID resolved. Compliance tags known.
  CATEGORY = unset. FLAG = unset.

---

STEP S-2 -- CATEGORY AND FLAG LOOKUP (single table, one row)

  ENTRY STATE: SKILL-ID resolved. Compliance tags known. CATEGORY = unset. FLAG = unset.

Find the single row in the table below that matches ({skill-id}, {tier}, compliance).
Read CATEGORY and FLAG from that row. These are your named variables. Do not derive
either value by any other means.

  | Skill pattern                                           | Tier | Compliance? | CATEGORY       | FLAG                                                          |
  |---------------------------------------------------------|------|-------------|----------------|---------------------------------------------------------------|
  | scout-feasibility, trace-*, listen-*                    | 2+   | no          | HIGH-STRUCTURE | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | scout-feasibility, trace-*, listen-*                    | 1    | no          | HIGH-STRUCTURE | none (structural coverage reliable)                           |
  | scout-compliance, trace-permissions                     | any  | yes         | HIGH-STRUCTURE | REAL-REQUIRED (compliance-sensitive)                          |
  | scout-stakeholders, scout-requirements, scout-naming,   | any  | no          | HIGH-STRUCTURE | none (structural coverage reliable)                           |
  |   scout-compliance, scout-market, draft-spec,           |      |             |                |                                                               |
  |   draft-proposal, draft-pitch, review-design,           |      |             |                |                                                               |
  |   review-code, trace-skill, flow-resilience,            |      |             |                |                                                               |
  |   flow-dataflow, flow-conversation, flow-lifecycle,     |      |             |                |                                                               |
  |   flow-throttle, flow-trigger, flow-integration,        |      |             |                |                                                               |
  |   program-plan                                          |      |             |                |                                                               |
  | prove-websearch, prove-interview, prove-prototype,      | any  | no          | EVIDENCE-HEAVY | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  |   listen-feedback, listen-support, listen-adoption      |      |             |                |                                                               |
  | scout-competitors, prove-hypothesis,                    | any  | no          | MIXED          | REVIEW-FOR-PLAUSIBILITY                                       |
  |   review-customers, review-users                        |      |             |                |                                                               |

CATEGORY and FLAG are now fixed. They are named variables. Do not recompute them.

FLAG immutability chain:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Affirmative closure     | Every path reaching A-1 carries the FLAG value assigned here         |
  | No-exemption            | No path is exempt                                                    |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-2:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-2 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record. DO NOT WRITE until complete.        |
  | Anti-bypass echo        | Per [P-0:ABD]: locate-only is a protocol failure.                    |
  | [P-0:ABD]               |                                                                      |
  | Cross-site ref [S-2:CS] | Failure produces silent category mismatch at [A-1:FC]                |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-2:CS]                       |
  | Step       | S-2                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

  EXIT STATE (S-2): CATEGORY = {value}. FLAG = {value}. Both immutable.
  Carry both forward verbatim to A-1. Do not re-evaluate.

---

STEP A-1 -- ASSEMBLE HEADER

  ENTRY STATE: CATEGORY = {value from S-2, verbatim}. FLAG = {value from S-2, verbatim}.
  Both values are read-only in this step.

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-2 verbatim. Do not rederive it.                     |
  | Priority                | First rule -- before any other instruction in this step              |
  | Anti-displacement       | Before any field, lookup, formatting, or other instruction           |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert match; |
  | (P-0 table, row 2)      | emit confirmation record. DO NOT WRITE until complete.               |
  | Anti-bypass echo        | Per [P-0:ABD]: locate-only is a protocol failure.                    |
  | [P-0:ABD]               |                                                                      |
  | Failure conseq [A-1:FC] | [Mutual target of S-2:CS]                                            |
  |                         | Re-deriving FLAG silently corrupts the artifact's trust tier         |

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
  Flag: {FLAG from S-2 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

  EXIT STATE (A-1): header written. FLAG consumed verbatim. Proceed to A-2.

---

STEP A-2 -- FIDELITY WARNING

  ENTRY STATE: header complete. CATEGORY known (read-only from S-2).

Write the fidelity warning as the first section of the artifact body, before any mock
content, separated from header and body with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
    reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1.

  EXIT STATE (A-2): fidelity warning written.

---

STEP A-3 -- GENERATE ARTIFACT BODY

  ENTRY STATE: header and fidelity warning complete. SKILL-ID known.

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

Generic prose without skill-specific structure fails.

  EXIT STATE (A-3): artifact body complete. Ready to write.

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

## V-05 — Combined: Role sequence + Output format (FLAG-first + decision table)

**Axes**: V-03 (compute FLAG from inputs in Step 1 before TOPICS.md read) + V-01 (decision table for CATEGORY/FLAG, one lookup row).

**Hypothesis**: Combining FLAG-first ordering with a lookup table yields maximum immutability surface with minimum cognitive load. The executor does one table lookup in Step 1, locks two values, reads TOPICS.md in Step 2 only for the narrow compliance amendment path, then assembles. No prose case logic, no sequential derivation steps, no content-phase FLAG exposure. This is the tightest possible execution path for FLAG correctness.

```
depth: standard

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
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
Anti-bypass echo rows at S-1 and A-1 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-1:CS]   | S-1  | Cross-site reference row    | [A-1:FC]     | forward --> names A-1        |
  | [A-1:FC]   | A-1  | Failure consequence row     | [S-1:CS]     | <-- backward, names S-1      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above.

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name and row type match current context.
    Step 2d: Emit confirmation record (fill Match field only):
               Token / Step / Row type: pre-filled at use site
               Match: PASS | FAIL
    DO NOT WRITE THE ROW until Steps 2a-2d complete and record is emitted.

Locate-only is a protocol failure. Do not re-establish this protocol in later steps.

---

STEP S-1 -- CATEGORY AND FLAG LOOKUP (from inputs, before TOPICS.md)

CATEGORY and FLAG are locked here, from {namespace/skill-id} and {tier} alone,
before TOPICS.md is read. Find the matching row in the table below. Read CATEGORY
and FLAG. These are your named variables for this run.

Only this step resolves CATEGORY and FLAG from inputs; no subsequent step re-derives
either value. Step S-2 may amend FLAG by one named rule only (compliance override).

  | Skill pattern                                           | Tier | Compliance? | CATEGORY       | FLAG                                                          |
  |---------------------------------------------------------|------|-------------|----------------|---------------------------------------------------------------|
  | scout-feasibility, trace-*, listen-*                    | 2+   | (see S-2)   | HIGH-STRUCTURE | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | scout-feasibility, trace-*, listen-*                    | 1    | (see S-2)   | HIGH-STRUCTURE | none (structural coverage reliable)                           |
  | scout-stakeholders, scout-requirements, scout-naming,   | any  | (see S-2)   | HIGH-STRUCTURE | none (structural coverage reliable)                           |
  |   scout-compliance, scout-market, draft-spec,           |      |             |                |                                                               |
  |   draft-proposal, draft-pitch, review-design,           |      |             |                |                                                               |
  |   review-code, trace-skill, flow-resilience,            |      |             |                |                                                               |
  |   flow-dataflow, flow-conversation, flow-lifecycle,     |      |             |                |                                                               |
  |   flow-throttle, flow-trigger, flow-integration,        |      |             |                |                                                               |
  |   program-plan                                          |      |             |                |                                                               |
  | prove-websearch, prove-interview, prove-prototype,      | any  | (see S-2)   | EVIDENCE-HEAVY | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  |   listen-feedback, listen-support, listen-adoption      |      |             |                |                                                               |
  | scout-competitors, prove-hypothesis,                    | any  | (see S-2)   | MIXED          | REVIEW-FOR-PLAUSIBILITY                                       |
  |   review-customers, review-users                        |      |             |                |                                                               |

CATEGORY and FLAG are now fixed. They are named variables.

FLAG immutability chain:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, branch, fallback, or other execution context        |
  | Affirmative closure     | Every path reaching A-1 carries the FLAG value assigned here         |
  | No-exemption            | No path is exempt                                                    |
  | Compliance override     | S-2 may amend FLAG by one defined rule; amendment is not re-derivation|
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-1:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-1 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record. DO NOT WRITE until complete.        |
  | Anti-bypass echo        | Per [P-0:ABD]: locate-only is a protocol failure.                    |
  | [P-0:ABD]               |                                                                      |
  | Cross-site ref [S-1:CS] | Failure produces silent category mismatch at [A-1:FC]                |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-1:CS]                       |
  | Step       | S-1                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

CATEGORY and FLAG are resolved. Carry forward to A-1 verbatim.

---

STEP S-2 -- SETUP (read TOPICS.md; apply compliance override if triggered; select skill)

Read TOPICS.md. Only this step emits the TOPICS.md status line; no subsequent step
repeats this emission. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Compliance override (the only permitted FLAG amendment after S-1):
  If compliance tags are present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"
  Otherwise: FLAG is unchanged from S-1. Do not re-examine or re-derive it.

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

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-1 (as possibly amended in S-2) verbatim.           |
  |                         | Do not rederive it.                                                  |
  | Priority                | First -- before any other instruction in this step                   |
  | Anti-displacement       | Before any field, lookup, formatting, or other instruction           |
  | Declarative closure     | No instruction in A-1 precedes this rule                             |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [A-1:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=A-1 + Row type=Failure consequence row; assert match; |
  | (P-0 table, row 2)      | emit confirmation record. DO NOT WRITE until complete.               |
  | Anti-bypass echo        | Per [P-0:ABD]: locate-only is a protocol failure.                    |
  | [P-0:ABD]               |                                                                      |
  | Failure conseq [A-1:FC] | [Mutual target of S-1:CS]                                            |
  |                         | Re-deriving FLAG silently corrupts the artifact's trust tier         |

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
  Skill: {skill-id from S-2}
  Topic: {topic}
  Category: {CATEGORY from S-1}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-1, as possibly amended in S-2 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body, before any mock
content, separated from header and body with --- delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific claims
    may be partially fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
    reliable. Content is synthetically generated but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for
    critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

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

## Round 15 summary

| Variation | Axis | Key structural change | C-40/C-41 exposure |
|-----------|------|-----------------------|--------------------|
| V-01 | Output format | S-2+S-3 → single lookup table | None — focus-particle emission line preserved |
| V-02 | Lifecycle emphasis | ENTRY/EXIT STATE declarations at every step | None — focus-particle emission line preserved |
| V-03 | Role sequence | FLAG-first (S-1), TOPICS.md second (S-2) | None — focus-particle emission line in S-2 |
| V-04 | V-01 + V-02 | Table + phase state contracts | None |
| V-05 | V-03 + V-01 | FLAG-first + table | None |

**Token table note**: V-01, V-04 rename the cross-reference tokens from [S-3:CS]/[A-1:FC] to [S-2:CS]/[A-1:FC] because FLAG is resolved in S-2 (not S-3) when using the consolidated table. V-03 and V-05 rename them to [S-1:CS]/[A-1:FC] because FLAG is resolved in S-1 (FLAG-first). Rubric evaluators should verify token table step labels match the actual resolution step in each variation.

**Write path**: `simulations/quest/golden/mock-ns-variate-R15-2026-03-17.md`
