---
skill: quest-variate
skill_target: mock-ns
round: 16
rubric_version: 16
rubric_target: C-42 (step-scope displacement), C-43 (lifecycle-annotation replacement)
date: 2026-03-17
---

# mock-ns -- Round 16 Variations (rubric v16, C-42/C-43 targets)

Rubric: v16 (C-01 through C-43, 5 essential / 3 recommended / 35 aspirational, max 150).

New criteria in v16 (extracted from R15 scoring):

- **C-42** -- C-28 step-scope displacement: emission sentence with correct nominative-subject form
  but displaced into S-1 (S-0 absent or merged) fails C-28 and fires C-42. Grammatical form
  is necessary but not sufficient; step scope is independently required.

- **C-43** -- C-32 lifecycle-annotation closing-position displacement: lifecycle exit-state
  annotation that REPLACES the terminal sentence of S-0 causes C-32 to fail and C-43 to fire.
  Annotation that FOLLOWS the terminal sentence (supplementation) passes both C-32 and C-43.

R15 confirmed scores under v16:
  R15 V-01 (decision table, no S-0): 118/150 -- fails C-12, C-13, C-15..C-28/C-32 (S-0 dependent), C-42
  R15 V-02 (lifecycle annotations, supplementation): 150/150 -- all pass
  R15 V-02 (lifecycle annotations, replacement): 148/150 -- fails C-32, C-43

Open questions from R15/v16 to investigate in R16:

| Question | Structure to probe | C-42/C-43 relevance |
|----------|--------------------|---------------------|
| Q-01 | Phrasing register: declarative vs imperative in non-S-0 steps | Does phrasing affect C-28 score when S-0 is present and correctly scoped? |
| Q-02 | S-0 with explicit CONSTRAINT gate blocking downstream steps | Does an explicit gate sentence strengthen C-42 scoring without introducing displacement? |
| Q-03 | S-1/S-2 as inline prose instead of lookup tables | Does format reduction outside the chain tables reduce any structural criterion? |
| Q-04 | S-3 sub-steps as explicit numbered sequence with in-order constraint | Does explicit ordering in S-3 affect C-33 (carry-emit ordering) or any criterion? |
| Q-05 | Combined: declarative phrasing + explicit S-0 gate + prose S-1/S-2 | Full integration -- can 150/150 be achieved with significantly reduced table density? |

Variation axes:

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register (declarative form) | Declarative step descriptions preserve all structural criteria; no score change |
| V-02 | Lifecycle emphasis (explicit S-0 gate + supplementation annotation) | Explicit CONSTRAINT gate strengthens C-42 pass and supplementation annotation confirms C-43 pass at 150/150 |
| V-03 | Output format (prose S-1/S-2 lookup) | Replacing default-skill and category tables with inline prose does not affect any structural criterion |
| V-04 | Role sequence (S-3 sub-steps as numbered sequence with explicit in-order constraint) | Numbered S-3 sequence strengthens C-33 without affecting C-42/C-43 |
| V-05 | Combined (V-01 declarative + V-02 S-0 gate + V-03 prose format) | Full integration produces more readable prompt at 150/150 |

---

## V-01

**Axis: Phrasing register (declarative form replacing imperative "Emit:" instructions)**
**Hypothesis: Declarative step descriptions ("The step emits..." vs "Emit:") preserve all structural criteria identically. Expected score: 150/150.**

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

LIFECYCLE
  P-0  Cross-reference protocol (token registration + anti-bypass declaration)
  S-0  Read TOPICS.md (emit status line)
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
  S-4  Artifact generation (header | fidelity warning | mock body)
  S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)

  S-3 note: sub-steps execute in order; each emits before the next begins.
  S-5 note: sub-steps execute in sequence. S-5.0 MISMATCH halts execution.

SUB-STEP LABEL PROPAGATION:

  | Sub-step       | CONSTRAINT reference (ID-primary)              | S-0 table Field (exact) | Execution emit              | Scope       |
  |----------------|------------------------------------------------|-------------------------|-----------------------------|-------------|
  | topic (exempt) | N/A -- multi-step scope; no CONSTRAINT ref     | topic                   | N/A -- used throughout      | multi-step  |
  | S-3.1          | S-3.1 (carry)                                  | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2 (compliance detection)                   | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3 (flag computation)                       | tier                    | S-3.3 flag resolved emit    | single-step |
  | S-5.0-S-5.4    | N/A (finalization)                             | N/A                     | (per sub-step)              | N/A         |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. All tokens defined here.

Anti-bypass declaration (ABD): An executor who processes a bracket token without
performing Phase 2 (Steps 2a through 2d) has not satisfied this protocol.
Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo this
declaration. [P-0:ABD] is registered as its own definition point -- encountering
[P-0:ABD] at an echo site requires Phase 1 lookup on [P-0:ABD] before processing.

  Abbreviation key: :CS = Cross-site reference row | :FC = Failure consequence row
                    :ABD = Anti-bypass declaration

  | Token     | Step | Row type                 | Paired token | Direction                |
  |-----------|------|--------------------------|--------------|--------------------------|
  | [S-3:CS]  | S-3  | Cross-site reference row | [S-4:FC]     | forward --> names S-4    |
  | [S-4:FC]  | S-4  | Failure consequence row  | [S-3:CS]     | <-- backward, names S-3  |
  | [P-0:ABD] | P-0  | Anti-bypass declaration  | (self)       | definition point         |

Lookup protocol -- two phases, both required before writing any bracket-token row:

  Phase 1 -- Locate: find the row by token name in the table above.
  Phase 2 -- Confirm:
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step; row type matches current row role.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match only).
             DO NOT WRITE THE ROW until Steps 2a-2d are complete.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written.

This step emits the TOPICS.md status line before any other step produces output.

The step reads TOPICS.md and writes:
  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
      tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                        | Downstream-Action                                      |
  |-----------------|-------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                         | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                  | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                   | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

Only this step emits the TOPICS.md status line.

---

STEP S-1 -- SKILL SELECTION

  | Namespace | Default skill     | Exclusion note                                 |
  |-----------|-------------------|------------------------------------------------|
  | scout     | scout-feasibility |                                                |
  | draft     | draft-spec        |                                                |
  | review    | review-design     |                                                |
  | flow      | flow-resilience   |                                                |
  | trace     | trace-request     |                                                |
  | prove     | prove-hypothesis  |                                                |
  | listen    | listen-support    |                                                |
  | program   | program-plan      |                                                |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

The step emits:
  > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills                                                                       |
  |----------------|-------------------------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,            |
  |                | scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,            |
  |                | review-design, review-code, trace-request, trace-component, trace-contract,         |
  |                | trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,       |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,      |
  |                | flow-integration, program-plan                                                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, |
  |                | listen-adoption                                                                     |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers, review-users                 |

The step emits:
  > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY:
  The step emits:
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE:
  The step emits:
    > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}

  S-3.3 -- FLAG:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-*, scout-feasibility, listen-support, listen-feedback, listen-adoption.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE.

  The step emits:
    > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                         |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration      |
  |                         | sequence -- no execution context is exempt                               |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value emitted here|
  | No-exemption            | No path is exempt from this closure requirement                          |
  | Failure consequence     | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's   |
  |                         | trust tier that is invisible to downstream tooling -- undetectable        |
  |                         | without manual header inspection                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in Affirmative closure |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match; emit         |
  | (P-0 table, row 1)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC] --   |
  |                         | the Failure consequence row in S-4 header assembly (that row identifies  |
  |                         | itself as this row's mutual target)                                      |

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

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest (emit before writing any artifact content):

  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line

The step emits:
  > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                         |
  | Priority                | No instruction in this step can precede this rule.                       |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any       |
  |                         | formatting instruction, or any other instruction in this step            |
  | All-governed            | All instructions in this step, named or unnamed, are subject to this     |
  |                         | rule, including paths that do not pass through prior steps in normal     |
  |                         | order                                                                    |
  | No-exemption            | No instruction in this step is exempt                                    |
  | Guarantee-break         | This violation breaks the FLAG closure guarantee stated in S-3's         |
  |                         | Affirmative closure row -- the corruption is undetectable without        |
  |                         | manual header inspection                                                 |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-4 + Row type=Failure consequence row; assert match; emit          |
  | (P-0 table, row 2)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]             |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to          |
  |                         | downstream tooling that silently corrupts the artifact's trust tier      |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-4:FC]                       |
  | Step       | S-4 (header)                   |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

The step emits:
  > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
    be partially accurate or partially fabricated. Review for plausibility.

The step emits:
  > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate content following the exact golden structural pattern of {skill-id}: correct
  section headings, required tables and lists, gate or verdict line in expected position,
  enforcement mechanisms present. Use {topic} as subject. A reader familiar with {skill-id}
  must identify the skill from the body alone.

The step emits:
  > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, verify each input-field row in the PROPAGATION table. Apply Scope-driven rule:
    - Scope=multi-step: confirm Downstream-Action acknowledges multi-step scope explicitly;
      emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions in the verification check table below;
      emit MATCH if both pass, MISMATCH if either fails.

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    The step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  The step emits:
    > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  The step emits (after S-5.1, before S-5.3):
    > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  The step emits (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  The step emits:
    > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-02

**Axis: Lifecycle emphasis -- S-0 with explicit CONSTRAINT gate + supplementation annotation following terminal sentence**
**Hypothesis: Explicit CONSTRAINT gate in S-0 strengthens C-42 pass; supplementation annotation (following terminal sentence) confirms C-43 supplementation = pass. Expected score: 150/150.**

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

LIFECYCLE
  P-0  Cross-reference protocol (token registration + anti-bypass declaration)
  S-0  Read TOPICS.md (emit status line)
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
  S-4  Artifact generation (header | fidelity warning | mock body)
  S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)

  S-3 note: sub-steps execute in order; each emits before the next begins.
  S-5 note: sub-steps execute in sequence. S-5.0 MISMATCH halts execution.

SUB-STEP LABEL PROPAGATION:

  | Sub-step       | CONSTRAINT reference (ID-primary)              | S-0 table Field (exact) | Execution emit              | Scope       |
  |----------------|------------------------------------------------|-------------------------|-----------------------------|-------------|
  | topic (exempt) | N/A -- multi-step scope; no CONSTRAINT ref     | topic                   | N/A -- used throughout      | multi-step  |
  | S-3.1          | S-3.1 (carry)                                  | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2 (compliance detection)                   | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3 (flag computation)                       | tier                    | S-3.3 flag resolved emit    | single-step |
  | S-5.0-S-5.4    | N/A (finalization)                             | N/A                     | (per sub-step)              | N/A         |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. All tokens defined here.

Anti-bypass declaration (ABD): An executor who processes a bracket token without
performing Phase 2 (Steps 2a through 2d) has not satisfied this protocol.
Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo this
declaration. [P-0:ABD] is registered as its own definition point -- encountering
[P-0:ABD] at an echo site requires Phase 1 lookup on [P-0:ABD] before processing.

  Abbreviation key: :CS = Cross-site reference row | :FC = Failure consequence row
                    :ABD = Anti-bypass declaration

  | Token     | Step | Row type                 | Paired token | Direction                |
  |-----------|------|--------------------------|--------------|--------------------------|
  | [S-3:CS]  | S-3  | Cross-site reference row | [S-4:FC]     | forward --> names S-4    |
  | [S-4:FC]  | S-4  | Failure consequence row  | [S-3:CS]     | <-- backward, names S-3  |
  | [P-0:ABD] | P-0  | Anti-bypass declaration  | (self)       | definition point         |

Lookup protocol -- two phases, both required before writing any bracket-token row:

  Phase 1 -- Locate: find the row by token name in the table above.
  Phase 2 -- Confirm:
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step; row type matches current row role.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match only).
             DO NOT WRITE THE ROW until Steps 2a-2d are complete.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                        | Downstream-Action                                      |
  |-----------------|-------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                         | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                  | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                   | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

Only this step emits the TOPICS.md status line.
[S-0 lifecycle exit: all four field values resolved; downstream steps may proceed]

---

STEP S-1 -- SKILL SELECTION

  | Namespace | Default skill     | Exclusion note                                 |
  |-----------|-------------------|------------------------------------------------|
  | scout     | scout-feasibility |                                                |
  | draft     | draft-spec        |                                                |
  | review    | review-design     |                                                |
  | flow      | flow-resilience   |                                                |
  | trace     | trace-request     |                                                |
  | prove     | prove-hypothesis  |                                                |
  | listen    | listen-support    |                                                |
  | program   | program-plan      |                                                |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills                                                                       |
  |----------------|-------------------------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,            |
  |                | scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,            |
  |                | review-design, review-code, trace-request, trace-component, trace-contract,         |
  |                | trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,       |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,      |
  |                | flow-integration, program-plan                                                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, |
  |                | listen-adoption                                                                     |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers, review-users                 |

Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY: Emit: > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}
  S-3.2 -- COMPLIANCE: Emit: > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}
  S-3.3 -- FLAG:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-*, scout-feasibility, listen-support, listen-feedback, listen-adoption.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE.

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                         |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration      |
  |                         | sequence -- no execution context is exempt                               |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value emitted here|
  | No-exemption            | No path is exempt from this closure requirement                          |
  | Failure consequence     | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's   |
  |                         | trust tier that is invisible to downstream tooling -- undetectable        |
  |                         | without manual header inspection                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in Affirmative closure |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match; emit         |
  | (P-0 table, row 1)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC] --   |
  |                         | the Failure consequence row in S-4 header assembly (that row identifies  |
  |                         | itself as this row's mutual target)                                      |

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

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest (emit before writing any artifact content):

  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line

Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                         |
  | Priority                | No instruction in this step can precede this rule.                       |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any       |
  |                         | formatting instruction, or any other instruction in this step            |
  | All-governed            | All instructions in this step, named or unnamed, are subject to this     |
  |                         | rule, including paths that do not pass through prior steps in normal     |
  |                         | order                                                                    |
  | No-exemption            | No instruction in this step is exempt                                    |
  | Guarantee-break         | This violation breaks the FLAG closure guarantee stated in S-3's         |
  |                         | Affirmative closure row -- the corruption is undetectable without        |
  |                         | manual header inspection                                                 |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-4 + Row type=Failure consequence row; assert match; emit          |
  | (P-0 table, row 2)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]             |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to          |
  |                         | downstream tooling that silently corrupts the artifact's trust tier      |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-4:FC]                       |
  | Step       | S-4 (header)                   |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
    be partially accurate or partially fabricated. Review for plausibility.

Emit: > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate content following the exact golden structural pattern of {skill-id}: correct
  section headings, required tables and lists, gate or verdict line in expected position,
  enforcement mechanisms present. Use {topic} as subject. A reader familiar with {skill-id}
  must identify the skill from the body alone.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, verify each input-field row in the PROPAGATION table. Apply Scope-driven rule:
    - Scope=multi-step: confirm Downstream-Action acknowledges multi-step scope explicitly;
      emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions in the verification check table below;
      emit MATCH if both pass, MISMATCH if either fails.

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    Emit: > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
             Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3):
    > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-03

**Axis: Output format -- prose substitution for S-1 and S-2 lookup tables**
**Hypothesis: Replacing the default-skill table (S-1) and category membership table (S-2) with inline prose descriptions reduces table density without affecting any structural criterion. Expected score: 150/150.**

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

LIFECYCLE
  P-0  Cross-reference protocol (token registration + anti-bypass declaration)
  S-0  Read TOPICS.md (emit status line)
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
  S-4  Artifact generation (header | fidelity warning | mock body)
  S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)

  S-3 note: sub-steps execute in order; each emits before the next begins.
  S-5 note: sub-steps execute in sequence. S-5.0 MISMATCH halts execution.

SUB-STEP LABEL PROPAGATION:

  | Sub-step       | CONSTRAINT reference (ID-primary)              | S-0 table Field (exact) | Execution emit              | Scope       |
  |----------------|------------------------------------------------|-------------------------|-----------------------------|-------------|
  | topic (exempt) | N/A -- multi-step scope; no CONSTRAINT ref     | topic                   | N/A -- used throughout      | multi-step  |
  | S-3.1          | S-3.1 (carry)                                  | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2 (compliance detection)                   | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3 (flag computation)                       | tier                    | S-3.3 flag resolved emit    | single-step |
  | S-5.0-S-5.4    | N/A (finalization)                             | N/A                     | (per sub-step)              | N/A         |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. All tokens defined here.

Anti-bypass declaration (ABD): An executor who processes a bracket token without
performing Phase 2 (Steps 2a through 2d) has not satisfied this protocol.
Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo this
declaration. [P-0:ABD] is registered as its own definition point -- encountering
[P-0:ABD] at an echo site requires Phase 1 lookup on [P-0:ABD] before processing.

  Abbreviation key: :CS = Cross-site reference row | :FC = Failure consequence row
                    :ABD = Anti-bypass declaration

  | Token     | Step | Row type                 | Paired token | Direction                |
  |-----------|------|--------------------------|--------------|--------------------------|
  | [S-3:CS]  | S-3  | Cross-site reference row | [S-4:FC]     | forward --> names S-4    |
  | [S-4:FC]  | S-4  | Failure consequence row  | [S-3:CS]     | <-- backward, names S-3  |
  | [P-0:ABD] | P-0  | Anti-bypass declaration  | (self)       | definition point         |

Lookup protocol -- two phases, both required before writing any bracket-token row:

  Phase 1 -- Locate: find the row by token name in the table above.
  Phase 2 -- Confirm:
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step; row type matches current row role.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match only).
             DO NOT WRITE THE ROW until Steps 2a-2d are complete.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                        | Downstream-Action                                      |
  |-----------------|-------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                         | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                  | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                   | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

Only this step emits the TOPICS.md status line.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use that skill-id. Otherwise use the namespace default:
scout -> scout-feasibility | draft -> draft-spec | review -> review-design |
flow -> flow-resilience | trace -> trace-request | prove -> prove-hypothesis |
listen -> listen-support | program -> program-plan | topic -> topic-plan.
topic-status is permanently excluded (meta-structural; never default for any namespace).

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

Assign CATEGORY from the skill-id selected in S-1:

HIGH-STRUCTURE includes: scout-feasibility, scout-stakeholders, scout-requirements,
scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
review-design, review-code, trace-request, trace-component, trace-contract, trace-state,
trace-skill, trace-migration, trace-deployment, flow-resilience, flow-dataflow,
flow-conversation, flow-lifecycle, flow-throttle, flow-trigger, flow-integration, program-plan.

EVIDENCE-HEAVY includes: prove-websearch, prove-interview, prove-prototype,
listen-feedback, listen-support, listen-adoption.

MIXED includes: scout-competitors, prove-hypothesis, review-customers, review-users.

Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY: Emit: > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}
  S-3.2 -- COMPLIANCE: Emit: > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}
  S-3.3 -- FLAG:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-*, scout-feasibility, listen-support, listen-feedback, listen-adoption.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE.

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                         |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration      |
  |                         | sequence -- no execution context is exempt                               |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value emitted here|
  | No-exemption            | No path is exempt from this closure requirement                          |
  | Failure consequence     | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's   |
  |                         | trust tier that is invisible to downstream tooling -- undetectable        |
  |                         | without manual header inspection                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in Affirmative closure |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match; emit         |
  | (P-0 table, row 1)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC] --   |
  |                         | the Failure consequence row in S-4 header assembly (that row identifies  |
  |                         | itself as this row's mutual target)                                      |

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

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest (emit before writing any artifact content):

  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line

Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                         |
  | Priority                | No instruction in this step can precede this rule.                       |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any       |
  |                         | formatting instruction, or any other instruction in this step            |
  | All-governed            | All instructions in this step, named or unnamed, are subject to this     |
  |                         | rule, including paths that do not pass through prior steps in normal     |
  |                         | order                                                                    |
  | No-exemption            | No instruction in this step is exempt                                    |
  | Guarantee-break         | This violation breaks the FLAG closure guarantee stated in S-3's         |
  |                         | Affirmative closure row -- the corruption is undetectable without        |
  |                         | manual header inspection                                                 |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-4 + Row type=Failure consequence row; assert match; emit          |
  | (P-0 table, row 2)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]             |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to          |
  |                         | downstream tooling that silently corrupts the artifact's trust tier      |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-4:FC]                       |
  | Step       | S-4 (header)                   |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
    be partially accurate or partially fabricated. Review for plausibility.

Emit: > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate content following the exact golden structural pattern of {skill-id}: correct
  section headings, required tables and lists, gate or verdict line in expected position,
  enforcement mechanisms present. Use {topic} as subject. A reader familiar with {skill-id}
  must identify the skill from the body alone.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, verify each input-field row in the PROPAGATION table. Apply Scope-driven rule:
    - Scope=multi-step: confirm Downstream-Action acknowledges multi-step scope explicitly;
      emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions in the verification check table below;
      emit MATCH if both pass, MISMATCH if either fails.

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    Emit: > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
             Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3):
    > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-04

**Axis: Role sequence -- S-3 sub-steps as explicit numbered sequence with in-order constraint**
**Hypothesis: Converting S-3 sub-steps from dash-notation to an explicit numbered sequence with "do not proceed to the next until the current emit is written" reinforces C-33 (carry-emit ordering) without affecting C-42/C-43. Expected score: 150/150.**

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

LIFECYCLE
  P-0  Cross-reference protocol (token registration + anti-bypass declaration)
  S-0  Read TOPICS.md (emit status line)
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
  S-4  Artifact generation (header | fidelity warning | mock body)
  S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)

  S-3 note: sub-steps execute in order; each emits before the next begins.
  S-5 note: sub-steps execute in sequence. S-5.0 MISMATCH halts execution.

SUB-STEP LABEL PROPAGATION:

  | Sub-step       | CONSTRAINT reference (ID-primary)              | S-0 table Field (exact) | Execution emit              | Scope       |
  |----------------|------------------------------------------------|-------------------------|-----------------------------|-------------|
  | topic (exempt) | N/A -- multi-step scope; no CONSTRAINT ref     | topic                   | N/A -- used throughout      | multi-step  |
  | S-3.1          | S-3.1 (carry)                                  | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2 (compliance detection)                   | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3 (flag computation)                       | tier                    | S-3.3 flag resolved emit    | single-step |
  | S-5.0-S-5.4    | N/A (finalization)                             | N/A                     | (per sub-step)              | N/A         |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. All tokens defined here.

Anti-bypass declaration (ABD): An executor who processes a bracket token without
performing Phase 2 (Steps 2a through 2d) has not satisfied this protocol.
Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo this
declaration. [P-0:ABD] is registered as its own definition point -- encountering
[P-0:ABD] at an echo site requires Phase 1 lookup on [P-0:ABD] before processing.

  Abbreviation key: :CS = Cross-site reference row | :FC = Failure consequence row
                    :ABD = Anti-bypass declaration

  | Token     | Step | Row type                 | Paired token | Direction                |
  |-----------|------|--------------------------|--------------|--------------------------|
  | [S-3:CS]  | S-3  | Cross-site reference row | [S-4:FC]     | forward --> names S-4    |
  | [S-4:FC]  | S-4  | Failure consequence row  | [S-3:CS]     | <-- backward, names S-3  |
  | [P-0:ABD] | P-0  | Anti-bypass declaration  | (self)       | definition point         |

Lookup protocol -- two phases, both required before writing any bracket-token row:

  Phase 1 -- Locate: find the row by token name in the table above.
  Phase 2 -- Confirm:
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step; row type matches current row role.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match only).
             DO NOT WRITE THE ROW until Steps 2a-2d are complete.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                        | Downstream-Action                                      |
  |-----------------|-------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                         | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                  | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                   | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

Only this step emits the TOPICS.md status line.

---

STEP S-1 -- SKILL SELECTION

  | Namespace | Default skill     | Exclusion note                                 |
  |-----------|-------------------|------------------------------------------------|
  | scout     | scout-feasibility |                                                |
  | draft     | draft-spec        |                                                |
  | review    | review-design     |                                                |
  | flow      | flow-resilience   |                                                |
  | trace     | trace-request     |                                                |
  | prove     | prove-hypothesis  |                                                |
  | listen    | listen-support    |                                                |
  | program   | program-plan      |                                                |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills                                                                       |
  |----------------|-------------------------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,            |
  |                | scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,            |
  |                | review-design, review-code, trace-request, trace-component, trace-contract,         |
  |                | trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,       |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,      |
  |                | flow-integration, program-plan                                                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, |
  |                | listen-adoption                                                                     |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers, review-users                 |

Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

Sequence: S-3.1 runs first. S-3.2 runs only after S-3.1's emit is written. S-3.3 runs only
after S-3.2's emit is written. No sub-step may begin before its predecessor's emit is complete.

  1. S-3.1 -- CARRY
     Emit: > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}
     Do not proceed to S-3.2 until this emit is written.

  2. S-3.2 -- COMPLIANCE
     Check for compliance-sensitive skills (scout-compliance, trace-permissions) AND
     compliance tags in TOPICS.md. If both present: FLAG = "REAL-REQUIRED (compliance-sensitive)".
     Emit: > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}
     Do not proceed to S-3.3 until this emit is written.

  3. S-3.3 -- FLAG
     Apply the flag matrix below. Compliance override from S-3.2 takes final precedence.

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-*, scout-feasibility, listen-support, listen-feedback, listen-adoption.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE.

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                         |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration      |
  |                         | sequence -- no execution context is exempt                               |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value emitted here|
  | No-exemption            | No path is exempt from this closure requirement                          |
  | Failure consequence     | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's   |
  |                         | trust tier that is invisible to downstream tooling -- undetectable        |
  |                         | without manual header inspection                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in Affirmative closure |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match; emit         |
  | (P-0 table, row 1)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC] --   |
  |                         | the Failure consequence row in S-4 header assembly (that row identifies  |
  |                         | itself as this row's mutual target)                                      |

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

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest (emit before writing any artifact content):

  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line

Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                         |
  | Priority                | No instruction in this step can precede this rule.                       |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any       |
  |                         | formatting instruction, or any other instruction in this step            |
  | All-governed            | All instructions in this step, named or unnamed, are subject to this     |
  |                         | rule, including paths that do not pass through prior steps in normal     |
  |                         | order                                                                    |
  | No-exemption            | No instruction in this step is exempt                                    |
  | Guarantee-break         | This violation breaks the FLAG closure guarantee stated in S-3's         |
  |                         | Affirmative closure row -- the corruption is undetectable without        |
  |                         | manual header inspection                                                 |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-4 + Row type=Failure consequence row; assert match; emit          |
  | (P-0 table, row 2)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]             |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to          |
  |                         | downstream tooling that silently corrupts the artifact's trust tier      |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-4:FC]                       |
  | Step       | S-4 (header)                   |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
    be partially accurate or partially fabricated. Review for plausibility.

Emit: > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate content following the exact golden structural pattern of {skill-id}: correct
  section headings, required tables and lists, gate or verdict line in expected position,
  enforcement mechanisms present. Use {topic} as subject. A reader familiar with {skill-id}
  must identify the skill from the body alone.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, verify each input-field row in the PROPAGATION table. Apply Scope-driven rule:
    - Scope=multi-step: confirm Downstream-Action acknowledges multi-step scope explicitly;
      emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions in the verification check table below;
      emit MATCH if both pass, MISMATCH if either fails.

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    Emit: > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
             Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3):
    > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-05

**Axis: Combined -- declarative phrasing (V-01) + explicit S-0 CONSTRAINT gate with supplementation annotation (V-02) + prose S-1/S-2 format (V-03)**
**Hypothesis: All three single-axis changes compose without conflict. The resulting prompt is more readable, maintains all structural criteria at 150/150, and the supplementation annotation explicitly activates the C-43 pass path. Expected score: 150/150.**

---

You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

LIFECYCLE
  P-0  Cross-reference protocol (token registration + anti-bypass declaration)
  S-0  Read TOPICS.md (emit status line)
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
  S-4  Artifact generation (header | fidelity warning | mock body)
  S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)

  S-3 note: sub-steps execute in order; each emits before the next begins.
  S-5 note: sub-steps execute in sequence. S-5.0 MISMATCH halts execution.

SUB-STEP LABEL PROPAGATION:

  | Sub-step       | CONSTRAINT reference (ID-primary)              | S-0 table Field (exact) | Execution emit              | Scope       |
  |----------------|------------------------------------------------|-------------------------|-----------------------------|-------------|
  | topic (exempt) | N/A -- multi-step scope; no CONSTRAINT ref     | topic                   | N/A -- used throughout      | multi-step  |
  | S-3.1          | S-3.1 (carry)                                  | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2 (compliance detection)                   | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3 (flag computation)                       | tier                    | S-3.3 flag resolved emit    | single-step |
  | S-5.0-S-5.4    | N/A (finalization)                             | N/A                     | (per sub-step)              | N/A         |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. All tokens defined here.

Anti-bypass declaration (ABD): An executor who processes a bracket token without
performing Phase 2 (Steps 2a through 2d) has not satisfied this protocol.
Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo this
declaration. [P-0:ABD] is registered as its own definition point -- encountering
[P-0:ABD] at an echo site requires Phase 1 lookup on [P-0:ABD] before processing.

  Abbreviation key: :CS = Cross-site reference row | :FC = Failure consequence row
                    :ABD = Anti-bypass declaration

  | Token     | Step | Row type                 | Paired token | Direction                |
  |-----------|------|--------------------------|--------------|--------------------------|
  | [S-3:CS]  | S-3  | Cross-site reference row | [S-4:FC]     | forward --> names S-4    |
  | [S-4:FC]  | S-4  | Failure consequence row  | [S-3:CS]     | <-- backward, names S-3  |
  | [P-0:ABD] | P-0  | Anti-bypass declaration  | (self)       | definition point         |

Lookup protocol -- two phases, both required before writing any bracket-token row:

  Phase 1 -- Locate: find the row by token name in the table above.
  Phase 2 -- Confirm:
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert step name matches current step; row type matches current row role.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match only).
             DO NOT WRITE THE ROW until Steps 2a-2d are complete.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.

This step emits the TOPICS.md status line before any other step produces output.

The step reads TOPICS.md and writes:
  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
      tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                        | Downstream-Action                                      |
  |-----------------|-------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                         | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                  | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                   | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

Only this step emits the TOPICS.md status line.
[S-0 lifecycle exit: all four field values resolved; S-1 through S-3.3 may proceed]

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use that skill-id. Otherwise use the namespace default:
scout -> scout-feasibility | draft -> draft-spec | review -> review-design |
flow -> flow-resilience | trace -> trace-request | prove -> prove-hypothesis |
listen -> listen-support | program -> program-plan | topic -> topic-plan.
topic-status is permanently excluded (meta-structural; never default for any namespace).

The step emits:
  > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

Assign CATEGORY from the skill-id selected in S-1:

HIGH-STRUCTURE includes: scout-feasibility, scout-stakeholders, scout-requirements,
scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
review-design, review-code, trace-request, trace-component, trace-contract, trace-state,
trace-skill, trace-migration, trace-deployment, flow-resilience, flow-dataflow,
flow-conversation, flow-lifecycle, flow-throttle, flow-trigger, flow-integration, program-plan.

EVIDENCE-HEAVY includes: prove-websearch, prove-interview, prove-prototype,
listen-feedback, listen-support, listen-adoption.

MIXED includes: scout-competitors, prove-hypothesis, review-customers, review-users.

The step emits:
  > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY:
  The step emits:
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE:
  The step emits:
    > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}

  S-3.3 -- FLAG:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-*, scout-feasibility, listen-support, listen-feedback, listen-adoption.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE.

  The step emits:
    > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                         |
  | Path classes            | Not in any step, conditional branch, fallback path, or regeneration      |
  |                         | sequence -- no execution context is exempt                               |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value emitted here|
  | No-exemption            | No path is exempt from this closure requirement                          |
  | Failure consequence     | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's   |
  |                         | trust tier that is invisible to downstream tooling -- undetectable        |
  |                         | without manual header inspection                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in Affirmative closure |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-3 + Row type=Cross-site reference row; assert match; emit         |
  | (P-0 table, row 1)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC] --   |
  |                         | the Failure consequence row in S-4 header assembly (that row identifies  |
  |                         | itself as this row's mutual target)                                      |

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

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest (emit before writing any artifact content):

  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line

The step emits:
  > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                     |
  |-------------------------|--------------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                         |
  | Priority                | No instruction in this step can precede this rule.                       |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any       |
  |                         | formatting instruction, or any other instruction in this step            |
  | All-governed            | All instructions in this step, named or unnamed, are subject to this     |
  |                         | rule, including paths that do not pass through prior steps in normal     |
  |                         | order                                                                    |
  | No-exemption            | No instruction in this step is exempt                                    |
  | Guarantee-break         | This violation breaks the FLAG closure guarantee stated in S-3's         |
  |                         | Affirmative closure row -- the corruption is undetectable without        |
  |                         | manual header inspection                                                 |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table. Phase 2 (Steps 2a-2d): read      |
  | before writing this row | Step=S-4 + Row type=Failure consequence row; assert match; emit          |
  | (P-0 table, row 2)      | confirmation record (Step 2d). DO NOT WRITE THE ROW until complete.      |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without performing Phase 2 (Steps     |
  | [P-0:ABD]:              | 2a-2d) has not satisfied this protocol. Locate-only is a protocol        |
  |                         | failure.                                                                 |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]             |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to          |
  |                         | downstream tooling that silently corrupts the artifact's trust tier      |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-4:FC]                       |
  | Step       | S-4 (header)                   |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

The step emits:
  > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement mechanisms
    are reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use this output to draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims may
    be partially accurate or partially fabricated. Review for plausibility.

The step emits:
  > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate content following the exact golden structural pattern of {skill-id}: correct
  section headings, required tables and lists, gate or verdict line in expected position,
  enforcement mechanisms present. Use {topic} as subject. A reader familiar with {skill-id}
  must identify the skill from the body alone.

The step emits:
  > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, verify each input-field row in the PROPAGATION table. Apply Scope-driven rule:
    - Scope=multi-step: confirm Downstream-Action acknowledges multi-step scope explicitly;
      emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions in the verification check table below;
      emit MATCH if both pass, MISMATCH if either fails.

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    The step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  The step emits:
    > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  The step emits (after S-5.1, before S-5.3):
    > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  The step emits (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  The step emits:
    > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## Variation Summary

| Variation | Primary axis | Secondary axes | Key structural change | C-42 risk | C-43 risk | Predicted score |
|-----------|-------------|----------------|----------------------|-----------|-----------|-----------------|
| V-01 | Phrasing register (declarative) | -- | "Emit:" -> "The step emits:" throughout | None (S-0 present, nominative-subject sentence preserved) | None (terminal sentence unchanged) | 150/150 |
| V-02 | Lifecycle emphasis | -- | Explicit CONSTRAINT gate in S-0 + supplementation annotation follows terminal sentence | None (S-0 discrete, emission sentence in S-0 scope) | None (supplementation: annotation follows, does not replace terminal sentence) | 150/150 |
| V-03 | Output format (prose S-1/S-2) | -- | Default-skill table and category table replaced with inline prose descriptions | None (S-0 unchanged; emission sentence scoped to S-0) | None (S-0 terminal sentence unchanged) | 150/150 |
| V-04 | Role sequence (numbered S-3 sequence) | -- | S-3 sub-steps as 1-2-3 numbered list with explicit "do not proceed until emit written" | None | None | 150/150 |
| V-05 | Combined | V-01 + V-02 + V-03 | Declarative phrasing + explicit S-0 CONSTRAINT gate + supplementation annotation + prose S-1/S-2 | None (CONSTRAINT gate explicitly prevents S-1 from starting before S-0 emit) | None (supplementation annotation explicitly activates C-43 pass path) | 150/150 |

### C-42 compliance across all variations

All five variations maintain S-0 as a discrete step with the nominative-subject emission
sentence scoped to S-0. No variation collapses S-0 into S-1. The emission sentence appears
in S-0 in all five, satisfying the step-scope boundary requirement for C-42.

### C-43 compliance across all variations

V-01, V-03, V-04: Terminal sentence "Only this step emits the TOPICS.md status line." present
as discrete prose; no lifecycle annotation near it -- C-43 trivially passes.

V-02 and V-05: Supplementation annotation "[S-0 lifecycle exit: all four field values resolved;
downstream steps may proceed]" appears AFTER the terminal sentence. The terminal sentence is
still present as discrete prose. C-43 passes via supplementation path.

### Open question from R16

Q-01 answered: Declarative phrasing ("The step emits:") is syntactically neutral relative to
C-28 -- the nominative-subject emission sentence is not an "Emit:" instruction; it is a
structural sentence in the step body. Changing "Emit:" to "The step emits:" in procedural
instructions does not affect C-28, which scores the structural sentence, not the procedural
emit instructions.
