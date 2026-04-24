---
skill: quest-variate
skill_target: mock-ns
round: 17
rubric_version: 17
rubric_target: C-44 (per-step-ID op-type co-location), C-45 (S-3 sub-step granularity)
date: 2026-03-17
---

# mock-ns -- Round 17 Variations (rubric v17, C-44/C-45 targets)

Rubric: v17 (C-01 through C-45, 5 essential / 3 recommended / 37 aspirational, max 154).

New criteria in v17 (extracted from R16 scoring):

- **C-44** -- CONSTRAINT per-step-ID operation-type co-location: each step ID named in the
  CONSTRAINT must be paired inline with its operation-type annotation as an adjacent parenthetical
  or equivalent co-located form. Fails when types are absent (step-IDs-only) OR when types are
  named in a trailing group rather than per-ID inline. C-15/C-21/C-24 test count; C-44 tests form.

- **C-45** -- CONSTRAINT S-3 sub-step granularity: when the prohibited step set includes S-3
  sub-operations, each sub-step (S-3.1, S-3.2, S-3.3) must appear as a separately enumerated entry.
  A collapsed "S-3" reference fails C-45 regardless of whether annotations are present.

R16 confirmed scores under v17:
  R16 V-01 (step-IDs-only CONSTRAINT): 142/154 -- fails C-15, C-21, C-24, C-44 (-8 pts)
  R16 V-02--V-05 (per-ID annotated + lifecycle): 154/154 -- all pass

Open questions from R16/v17 to investigate in R17:

| Question | Structure to probe | C-44/C-45 relevance |
|----------|--------------------|---------------------|
| Q-01 | CONSTRAINT step-IDs-only (no annotations anywhere) | Canonical C-44 failure; also fires C-15/C-21/C-24 |
| Q-02 | CONSTRAINT trailing-group: types named in separate sentence, not per-ID inline | C-44 fires independently even when C-15/C-21/C-24 pass (types present but not co-located) |
| Q-03 | CONSTRAINT S-3 collapsed: per-ID annotations for S-1/S-2 but S-3 as single entry | C-45 fails; C-21/C-24 also fail (only 3 types); C-44 passes for named IDs |
| Q-04 | CONSTRAINT em-dash co-location: "S-3.1 -- carry" instead of "S-3.1 (carry)" | Does C-44's "adjacent parenthetical or equivalent co-located form" admit em-dash? |
| Q-05 | Combined: golden CONSTRAINT + prose S-1/S-2 + declarative phrasing | Full integration axes orthogonal to CONSTRAINT criteria; 154/154 confirmed |

Variation axes:

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | CONSTRAINT form: step-IDs-only | C-44 FAIL, C-15 FAIL, C-21 FAIL, C-24 FAIL; C-45 PASS; score 142/154 |
| V-02 | CONSTRAINT annotation placement: trailing group | C-44 FAIL (types not per-ID inline); C-15/C-21/C-24 PASS (5 types present); C-45 PASS; score 152/154 |
| V-03 | CONSTRAINT S-3 granularity: collapsed | C-45 FAIL; C-21 FAIL; C-24 FAIL; C-44 PASS (per-ID for 3 IDs); score 148/154 |
| V-04 | CONSTRAINT annotation punctuation: em-dash co-location | C-44 PASS (em-dash = equivalent co-located form); C-45 PASS; score 154/154 |
| V-05 | Combined: golden CONSTRAINT + prose S-1/S-2 format + declarative phrasing register | 154/154 -- confirms axes independent of CONSTRAINT criteria |

---

## V-01

**Axis: CONSTRAINT form -- step-IDs-only (no per-ID operation-type annotations)**
**Hypothesis: C-44 FAIL (step IDs present, zero per-ID annotations). C-15/C-21/C-24 co-fail (0 operation types named). C-45 PASS (S-3.1, S-3.2, S-3.3 separately enumerated). Expected score: 142/154.**

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
  | S-3.1          | S-3.1                                          | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2                                          | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3                                          | tier                    | S-3.3 flag resolved emit    | single-step |
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

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                | Downstream-Action                                      |
  |-----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                                 | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                          | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                           | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override     | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

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
  | tier-source     | contains "S-3.1"                        | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2"                        | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3"                        | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    The step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3): > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-02

**Axis: CONSTRAINT annotation placement -- operation types in trailing group sentence, not per-ID inline**
**Hypothesis: C-44 FAIL (types present but not co-located per-ID; trailing group ≠ adjacent parenthetical). C-15/C-21/C-24 PASS (5 operation types present in CONSTRAINT block). C-45 PASS (S-3.1, S-3.2, S-3.3 separately enumerated). Expected score: 152/154.**

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
  | S-3.1          | S-3.1                                          | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2                                          | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3                                          | tier                    | S-3.3 flag resolved emit    | single-step |
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

CONSTRAINT: Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is
written. Operations blocked: skill selection, category lookup, carry, compliance detection,
flag computation.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                | Downstream-Action                                      |
  |-----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                                 | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                          | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                           | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override     | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

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
  | tier-source     | contains "S-3.1"                        | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2"                        | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3"                        | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    The step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3): > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-03

**Axis: CONSTRAINT S-3 granularity -- S-3 collapsed to single entry "S-3 (flag computation)"**
**Hypothesis: C-45 FAIL (S-3 not enumerated as S-3.1/S-3.2/S-3.3). C-21 FAIL (only 3 operation types < 4). C-24 FAIL (3 < 5). C-44 PASS (each named ID has adjacent parenthetical). C-15 PASS (3 >= 3). Expected score: 148/154.**

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
  | S-3.1          | S-3 (flag computation) [collapsed]             | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3 (flag computation) [collapsed]             | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3 (flag computation) [collapsed]             | tier                    | S-3.3 flag resolved emit    | single-step |
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

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), or S-3 (flag
computation) until this step's emit is written.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                | Downstream-Action                                      |
  |-----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                                 | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                          | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                           | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override     | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

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

  | Field           | Expected CONSTRAINT string                  | Expected Downstream-Action string  |
  |-----------------|---------------------------------------------|------------------------------------|
  | tier-source     | contains "S-3 (flag computation)"           | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3 (flag computation)"           | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3 (flag computation)"           | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    The step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3): > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-04

**Axis: CONSTRAINT annotation punctuation -- em-dash co-location ("S-3.1 -- carry") instead of parenthetical ("S-3.1 (carry)")**
**Hypothesis: C-44 PASS -- em-dash satisfies "equivalent co-located form"; each step ID paired with its operation-type annotation inline. C-45 PASS (S-3.1, S-3.2, S-3.3 separately enumerated). C-15/C-21/C-24 PASS (5 operation types present). Expected score: 154/154.**

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
  | S-3.1          | S-3.1 -- carry                                 | tier-source             | S-3.1 carry emit            | single-step |
  | S-3.2          | S-3.2 -- compliance detection                  | compliance-tags         | S-3.2 compliance check emit | single-step |
  | S-3.3          | S-3.3 -- flag computation                      | tier                    | S-3.3 flag resolved emit    | single-step |
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

CONSTRAINT: Do not perform S-1 -- skill selection, S-2 -- category lookup, S-3.1 -- carry,
S-3.2 -- compliance detection, or S-3.3 -- flag computation until this step's emit is written.

Before any other step begins, this step emits the TOPICS.md status line.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                | Downstream-Action                                      |
  |-----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                                 | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                          | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                           | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override     | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

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

  | Field           | Expected CONSTRAINT string                  | Expected Downstream-Action string  |
  |-----------------|---------------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 -- carry"                   | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 -- compliance detection"    | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 -- flag computation"        | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH:
    The step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit (after S-5.1, before S-5.3): > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit (after S-5.2, before S-5.4):
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

## V-05

**Axis: Combined -- golden CONSTRAINT (per-ID parenthetical + S-3 sub-steps) + prose format for S-1/S-2 + declarative phrasing register throughout**
**Hypothesis: 154/154 -- all CONSTRAINT criteria pass; prose/declarative axes are orthogonal to C-44/C-45. Confirms that output format and phrasing register do not affect CONSTRAINT correctness.**

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

The step reads TOPICS.md and emits:
  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
      tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                | Downstream-Action                                      |
  |-----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
  | topic           | Value from input argument                                                 | Consumed across all steps; no single sub-step anchor   |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                          | Consumed at S-3.3 (flag computation)                   |
  | compliance-tags | TOPICS.md if found; none if not                                           | Consumed at S-3.2 (compliance detection)               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override     | Consumed at S-3.1; re-emitted as carry record before S-3.2 |

Only this step emits the TOPICS.md status line.

---

STEP S-1 -- SKILL SELECTION

The default skill for each namespace is: scout -> scout-feasibility, draft -> draft-spec,
review -> review-design, flow -> flow-resilience, trace -> trace-request,
prove -> prove-hypothesis, listen -> listen-support, program -> program-plan,
topic -> topic-plan (topic-status is NEVER selected -- excluded as meta-structural).

If --skill is provided, the step uses that skill-id instead of the namespace default.

The step emits:
  > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

The CATEGORY for each skill is one of: HIGH-STRUCTURE, EVIDENCE-HEAVY, or MIXED.

HIGH-STRUCTURE skills: scout-feasibility, scout-stakeholders, scout-requirements,
scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
review-design, review-code, trace-request, trace-component, trace-contract, trace-state,
trace-skill, trace-migration, trace-deployment, flow-resilience, flow-dataflow,
flow-conversation, flow-lifecycle, flow-throttle, flow-trigger, flow-integration,
program-plan.

EVIDENCE-HEAVY skills: prove-websearch, prove-interview, prove-prototype,
listen-feedback, listen-support, listen-adoption.

MIXED skills: scout-competitors, prove-hypothesis, review-customers, review-users.

The step emits:
  > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY:
  The step re-emits S-0 field values as a carry record before S-3.2 begins:
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE:
  The step checks for compliance tags from S-0 and emits:
    > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}

  S-3.3 -- FLAG:
  The step resolves FLAG from CATEGORY, tier, and compliance-override path:

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

  The step generates content following the exact golden structural pattern of {skill-id}:
  correct section headings, required tables and lists, gate or verdict line in expected
  position, enforcement mechanisms present. The step uses {topic} as subject throughout.
  A reader familiar with {skill-id} must identify the skill from the body alone.

The step emits:
  > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, the step verifies each input-field row in the PROPAGATION table.
  Scope=multi-step fields: the step confirms Downstream-Action acknowledges multi-step
  scope explicitly and emits MULTI-STEP-ACKNOWLEDGED. Scope=single-step fields: the
  step checks both conditions in the verification table and emits MATCH if both pass,
  MISMATCH if either fails.

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  The step emits:
    > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
        [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field returns MISMATCH, the step emits:
      > PROPAGATION MISMATCH: run halted -- repair CONSTRAINT block or
          Downstream-Action entries before continuing
  and stops. S-5.1 through S-5.4 do not execute.

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
  The step writes as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  The step emits:
    > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
