---
skill: quest-variate
skill_target: mock-ns
round: 19
rubric_version: 18
rubric_target: new axes -- phrasing register (C-31), output format (C-22), lifecycle emphasis (structural)
date: 2026-03-17
---

# mock-ns -- Round 19 Variations (rubric v18, new axis exploration)

Rubric: v18 (C-01 through C-47, 5 essential / 3 recommended / 39 aspirational, max 158).

R18 confirmed scores (CONSTRAINT-form axes, all reproduced):

| Variation | Fails | Score |
|-----------|-------|-------|
| V-01 (step-IDs-only) | C-15, C-21, C-24, C-44, C-46 | 148/158 |
| V-02 (trailing-group) | C-44, C-46 | 154/158 |
| V-03 (collapsed S-3, per-ID) | C-45, C-21, C-24 | 152/158 |
| V-04 (em-dash per-ID) | -- | 158/158 |
| V-05 (golden parenthetical) | -- | 158/158 |

R18 CONSTRAINT-form axes are exhausted. R19 explores three new independent axes:

| Axis | Label | Rubric target |
|------|-------|---------------|
| A | Phrasing register | C-31 (deontic "must" form in S-0 declarative closing sentence) |
| B | Output format | C-22 (HS-critical rows merged -- structural row separation absent) |
| C | Lifecycle emphasis | structural only -- phase-grouped lifecycle with state annotations |

All R19 variations use the golden parenthetical CONSTRAINT form:
"Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written."
C-44/C-45/C-46/C-47 pass in all five variations.

Variation axes:

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register (axis A): deontic closing sentence | C-31 FAIL; C-25/C-28 PASS (kept "Before any other step begins, this step emits..." as first declarative); expected 156/158 |
| V-02 | Output format (axis B): 4-row FLAG table, HS-critical-tier-1 merged into catch-all | C-22 FAIL; C-11 PASS (5 cases functionally present); expected 156/158 |
| V-03 | Lifecycle emphasis (axis C): phase-grouped lifecycle with entry/exit state annotations | All criteria PASS; S-0 content unchanged; expected 158/158 |
| V-04 | Combination A+B: deontic closing + collapsed FLAG table | C-31 FAIL + C-22 FAIL; expected 154/158 |
| V-05 | Combination A+B+C at golden: "Only this step..." + 5-row table + phase-grouped lifecycle | All criteria PASS; expected 158/158 |

---

## V-01

**Axis: Phrasing register -- deontic modal "must" replaces closing declarative in S-0**
**Hypothesis: C-31 FAIL (deontic obligation form: "This step must emit..."). C-25/C-28 PASS (first declarative "Before any other step begins, this step emits..." satisfies nominative-subject form; C-31 fires independently per v10 discriminator). C-44/C-45/C-46/C-47 PASS (golden parenthetical CONSTRAINT). Expected score: 156/158.**

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

  | Field           | Resolution                                                                  | Downstream-Action                                                                 |
  |-----------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                              |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                            | Consumed at S-3.3 (flag computation)                                              |
  | compliance-tags | TOPICS.md if found; none if not                                             | Consumed at S-3.2 (compliance detection)                                          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override       | Consumed at S-3.1; re-emitted as carry record before S-3.2 begins                |

This step must emit the TOPICS.md status line before any other step begins.

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

**Axis: Output format -- 4-row FLAG table, HS-critical-tier-1 collapsed into catch-all row**
**Hypothesis: C-22 FAIL (HS-critical-tier-1 not present as a separate row; merged into HIGH-STRUCTURE | any | any catch-all -- the v5 discriminator canonical collapse). C-11 PASS (5 cases functionally covered: HS-non-critical covered by row 1; HS-critical-tier-2+ has its own row; EVIDENCE-HEAVY and MIXED each have rows; HS-critical-tier-1 flag value 'none (structural coverage reliable)' visible as the row-1 value). C-44/C-45/C-46/C-47 PASS (golden parenthetical CONSTRAINT). Expected score: 156/158.**

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

  | Field           | Resolution                                                                  | Downstream-Action                                                                 |
  |-----------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                              |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                            | Consumed at S-3.3 (flag computation)                                              |
  | compliance-tags | TOPICS.md if found; none if not                                             | Consumed at S-3.2 (compliance detection)                                          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override       | Consumed at S-3.1; re-emitted as carry record before S-3.2 begins                |

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
    | HIGH-STRUCTURE | any  | any             | none (structural coverage reliable)                           |
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

**Axis: Lifecycle emphasis -- phase-grouped LIFECYCLE block with entry/exit state annotations per step**
**Hypothesis: All criteria PASS. Phase grouping and state annotations are additive -- no existing step content removed, no S-0 closing sentence displaced, no FLAG table structural change. Lifecycle expansion is purely organizational. C-44/C-45/C-46/C-47 PASS (golden parenthetical CONSTRAINT). C-22 PASS (5-row golden FLAG table). C-31 PASS ("Only this step emits..." golden declarative closing). Expected score: 158/158.**

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

  Phase 1 -- Protocol and topic resolution
    P-0  Cross-reference protocol (token registration + anti-bypass declaration)
         Entry: no bracket tokens defined; no anti-bypass declaration
         Exit:  [S-3:CS], [S-4:FC], [P-0:ABD] registered; two-phase lookup protocol documented
    S-0  Read TOPICS.md (emit status line)
         Entry: topic + namespace + optional flags; TOPICS.md unread; tier unresolved
         Exit:  TOPICS.md status line emitted; tier resolved; compliance-tags resolved; tier-source resolved

  Phase 2 -- Skill and category resolution
    S-1  Skill selection
         Entry: namespace; optional --skill arg
         Exit:  skill-id resolved; generating-mock emit written
    S-2  Category lookup
         Entry: skill-id from S-1
         Exit:  CATEGORY assigned (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED); category emit written

  Phase 3 -- Flag computation
    S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
         Entry: tier, compliance-tags, tier-source from S-0; CATEGORY from S-2
         Exit:  FLAG resolved and locked; S-3.1/S-3.2/S-3.3 emits written; immutability chain closed

  Phase 4 -- Artifact generation and finalization
    S-4  Artifact generation (header | fidelity warning | mock body)
         Entry: skill-id, topic, CATEGORY, FLAG, tier
         Exit:  MOCK ARTIFACT header written; fidelity warning written; mock body written
    S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)
         Entry: completed artifact sections from S-4
         Exit:  propagation verified; manifest counted; artifact written to path; next-step line last

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

  | Field           | Resolution                                                                  | Downstream-Action                                                                 |
  |-----------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                              |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                            | Consumed at S-3.3 (flag computation)                                              |
  | compliance-tags | TOPICS.md if found; none if not                                             | Consumed at S-3.2 (compliance detection)                                          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override       | Consumed at S-3.1; re-emitted as carry record before S-3.2 begins                |

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

**Axis: Combination A+B -- deontic closing sentence (axis A) + 4-row collapsed FLAG table (axis B)**
**Hypothesis: C-31 FAIL (deontic closing) + C-22 FAIL (HS-critical-tier-1 collapsed into catch-all). C-25/C-28 PASS (first declarative "Before any other step begins, this step emits..." satisfies nominative-subject form). C-11 PASS (4-row table functionally covers all 5 cases). C-44/C-45/C-46/C-47 PASS (golden parenthetical CONSTRAINT). Expected score: 154/158.**

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

  | Field           | Resolution                                                                  | Downstream-Action                                                                 |
  |-----------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                              |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                            | Consumed at S-3.3 (flag computation)                                              |
  | compliance-tags | TOPICS.md if found; none if not                                             | Consumed at S-3.2 (compliance detection)                                          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override       | Consumed at S-3.1; re-emitted as carry record before S-3.2 begins                |

This step must emit the TOPICS.md status line before any other step begins.

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
    | HIGH-STRUCTURE | any  | any             | none (structural coverage reliable)                           |
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

**Axis: Combination A+B+C at golden -- "Only this step emits..." (axis A golden) + 5-row FLAG table (axis B golden) + phase-grouped lifecycle with state annotations (axis C golden)**
**Hypothesis: All criteria PASS. A at golden: C-31 PASS ("Only this step emits..." is nominative + non-deontic). B at golden: C-22 PASS (HS-critical-tier-1 separate row). C at golden: phase grouping is supplemental, no content removed. C-44/C-45/C-46/C-47 PASS (golden parenthetical CONSTRAINT). Expected score: 158/158.**

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

  Phase 1 -- Protocol and topic resolution
    P-0  Cross-reference protocol (token registration + anti-bypass declaration)
         Entry: no bracket tokens defined; no anti-bypass declaration
         Exit:  [S-3:CS], [S-4:FC], [P-0:ABD] registered; two-phase lookup protocol documented
    S-0  Read TOPICS.md (emit status line)
         Entry: topic + namespace + optional flags; TOPICS.md unread; tier unresolved
         Exit:  TOPICS.md status line emitted; tier resolved; compliance-tags resolved; tier-source resolved

  Phase 2 -- Skill and category resolution
    S-1  Skill selection
         Entry: namespace; optional --skill arg
         Exit:  skill-id resolved; generating-mock emit written
    S-2  Category lookup
         Entry: skill-id from S-1
         Exit:  CATEGORY assigned (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED); category emit written

  Phase 3 -- Flag computation
    S-3  Flag computation (S-3.1 carry | S-3.2 compliance | S-3.3 flag)
         Entry: tier, compliance-tags, tier-source from S-0; CATEGORY from S-2
         Exit:  FLAG resolved and locked; S-3.1/S-3.2/S-3.3 emits written; immutability chain closed

  Phase 4 -- Artifact generation and finalization
    S-4  Artifact generation (header | fidelity warning | mock body)
         Entry: skill-id, topic, CATEGORY, FLAG, tier
         Exit:  MOCK ARTIFACT header written; fidelity warning written; mock body written
    S-5  Finalize (S-5.0 propagation | S-5.1 count | S-5.2 order | S-5.3 header | S-5.4 write)
         Entry: completed artifact sections from S-4
         Exit:  propagation verified; manifest counted; artifact written to path; next-step line last

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

  | Field           | Resolution                                                                  | Downstream-Action                                                                 |
  |-----------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                              |
  | tier            | TOPICS.md if found; 1 if not; --tier if provided                            | Consumed at S-3.3 (flag computation)                                              |
  | compliance-tags | TOPICS.md if found; none if not                                             | Consumed at S-3.2 (compliance detection)                                          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not; --tier-override       | Consumed at S-3.1; re-emitted as carry record before S-3.2 begins                |

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

## R19 Summary

Axes confirmed independent of CONSTRAINT form (all variations use golden parenthetical; C-44/C-45/C-46/C-47 pass throughout):

| Variation | Axis | Fails | Expected score |
|-----------|------|-------|----------------|
| V-01 | Phrasing register: deontic closing ("must emit") | C-31 | 156/158 |
| V-02 | Output format: 4-row FLAG table (HS-critical-tier-1 in catch-all) | C-22 | 156/158 |
| V-03 | Lifecycle emphasis: phase-grouped with state annotations | -- | 158/158 |
| V-04 | Combination A+B: deontic + collapsed FLAG | C-31, C-22 | 154/158 |
| V-05 | Combination A+B+C at golden: "Only..." + 5-row + phase-grouped | -- | 158/158 |

Open questions for R20:

| Question | Structure to probe | Target |
|----------|--------------------|--------|
| Q-01 | Passive closing sentence in S-0: "The TOPICS.md status line is emitted by this step" | C-33 + C-25 + C-28 + C-29 four-criterion chain |
| Q-02 | Wh-pseudo-cleft closing: "What this step does first is emit the TOPICS.md status line" | C-39 + C-25 + C-28 + C-29 chain |
| Q-03 | Prose FLAG computation covering all 5 cases inline (no table) | Whether C-11 PASS + C-22 FAIL or both fail |
| Q-04 | C-31 + C-22 + C-45 cascade (three-axis failure): deontic + collapsed FLAG + collapsed S-3 | C-31 + C-22 + C-45 + C-21 + C-24 |
| Q-05 | Phase-grouped lifecycle with annotations replacing (not supplementing) S-0 tier-carry sentence | C-32 + C-43 |
