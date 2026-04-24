```
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

  If Category MISMATCH or Flag MISMATCH:
    Emit: > HEADER MISMATCH: run halted -- Category or Flag value in artifact header does
             not match S-2 or S-3 audit value; repair header before S-5.4
    Stop. Do not execute S-5.4.

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-04 — Combined: S-3 Modal + S-4 First Rule Enumeration (V-01 + V-02)

**Axes**: S-3 Affirmative closure modal upgrade AND S-4 First rule bypass-vector enumeration.  
**Hypothesis**: C-52 and C-53 are independent axes — modal impossibility at the declaration site and enumerated prohibition at the consumption site. Together they close both ends of the FLAG cross-site contract without a structural gap: the S-3 chain asserts it is impossible for FLAG to differ at consumption; the S-4 First rule names every mechanism by which rederivation might be attempted.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

LIFECYCLE:
  P-0  Cross-reference protocol -- register bracket tokens; establish two-phase lookup obligation
  S-0  Read TOPICS.md and emit
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation
    S-3.1  carry -- re-emit S-0 values at point of S-3 consumption
    S-3.2  compliance -- detect compliance signal before flag runs
    S-3.3  flag -- compute FLAG with path discriminator and emit
       Note: S-3.1 must emit before S-3.2 begins; S-3.2 must emit before S-3.3 begins.
  S-4  Artifact generation
  S-5  Finalization
    S-5.0  propagation -- verify PROPAGATION table bindings; halt if any MISMATCH detected
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line
       Note: S-5.0 through S-5.4 execute in sequence. No S-5 sub-step may begin
       before the preceding sub-step's emit is written. If S-5.0 detects any MISMATCH
       in a single-step field, execution stops and S-5.1 through S-5.4 do not execute.

SUB-STEP LABEL PROPAGATION:

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                   | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source             | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags         | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                    | S-3.3 flag resolved emit    | single-step  |
  | S-5.0           | N/A (finalization)                                       | N/A                     | PROPAGATION verified emit   | N/A          |
  | S-5.1           | N/A (finalization)                                       | N/A                     | manifest count emit         | N/A          |
  | S-5.2           | N/A (finalization)                                       | N/A                     | section ordering emit       | N/A          |
  | S-5.3           | N/A (finalization)                                       | N/A                     | header reconciliation emit  | N/A          |
  | S-5.4           | N/A (finalization)                                       | N/A                     | artifact written emit       | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and S-4 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row  |  :FC = Failure consequence row  |  :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-3:CS]   | S-3  | Cross-site reference row    | [S-4:FC]     | forward --> names S-4        |
  | [S-4:FC]   | S-4  | Failure consequence row     | [S-3:CS]     | <-- backward, names S-3      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; row 2 = [S-4:FC]; row 3 = [P-0:ABD].

Lookup protocol -- two phases, required before writing any bracket-token row:
  Phase 1 -- Locate: find the row by matching token name.
  Phase 2 -- Confirm (Steps 2a-2d): read Step cell; read Row type cell; assert match;
    emit confirmation record (pre-filled at use site, fill Match field only).
    DO NOT WRITE THE ROW until Steps 2a-2d are complete and the record is emitted.

Locate-only is a protocol failure. Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                  | Downstream-Action                                                                      |
  |-----------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps as artifact subject; no single sub-step anchor               |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided     | Consumed at S-3.3 for tier-conditional flag refinement                                 |
  | compliance-tags | TOPICS.md entry if found; none if not found                                 | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins       |

---

STEP S-1 -- SKILL SELECTION

  | Namespace | Default skill     | Exclusion note                                  |
  |-----------|-------------------|-------------------------------------------------|
  | scout     | scout-feasibility |                                                 |
  | draft     | draft-spec        |                                                 |
  | review    | review-design     |                                                 |
  | flow      | flow-resilience   |                                                 |
  | trace     | trace-request     |                                                 |
  | prove     | prove-hypothesis  |                                                 |
  | listen    | listen-support    |                                                 |
  | program   | program-plan      |                                                 |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)  |

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If skill not found: emit error and stop.
Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY
  Emit: > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit: > Compliance check: {DETECTED [signal: {signal-id}] | NOT-DETECTED}

  S-3.3 -- FLAG

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical: trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support, listen-feedback,
  listen-adoption.

  Path: BASE | TIER-REFINEMENT (critical at tier >= 2) | COMPLIANCE-OVERRIDE (S-3.2 detected)
  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain -- all rows active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context, including paths that do    |
  |                         | not pass through prior steps in normal order                         |
  | Affirmative closure     | No execution path that reaches S-4 can carry a FLAG value other      |
  |                         | than the one emitted here                                            |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, S-4 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the impossibility guarantee stated in the       |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record (fill Match field only).             |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                 |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row      |
  | [P-0:ABD]               | type cells, or without performing Phase 2, is a protocol failure.   |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC]  |

  Confirmation record: Token=[S-3:CS] | Step=S-3 | Row type=Cross-site reference row | Match=___

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest:
  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line
Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any header field is written:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it by any means:        |
  |                         | recomputation from category and tier, inference from skill-id,       |
  |                         | derivation from an intermediary variable, default-table lookup,      |
  |                         | or any other mechanism.                                              |
  | Priority                | No instruction in this step can precede this rule                    |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in S-4 precedes this rule                             |
  | All-governed            | Every instruction in this step, named or unnamed, is governed by     |
  |                         | this rule, including paths that do not pass through prior steps in   |
  |                         | normal order                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-4 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record (fill Match field only).             |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                 |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row      |
  | [P-0:ABD]               | type cells, or without performing Phase 2, is a protocol failure.   |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS] Re-deriving FLAG here produces a category  |
  |                         | mismatch invisible to downstream tooling; undetectable without       |
  |                         | manual header inspection                                             |

  Confirmation record: Token=[S-4:FC] | Step=S-4 | Row type=Failure consequence row | Match=___

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING:
  HIGH-STRUCTURE -> NOTE: HIGH-STRUCTURE mock. Structure reliable. Content synthetic.
    Adequate Tier 1. REAL-REQUIRED Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
  EVIDENCE-HEAVY -> WARNING: EVIDENCE-HEAVY mock. Evidence fabricated. Real {skill-id} run required.
  MIXED -> CAUTION: MIXED mock. Tables/gates reliable. Claims may be partially fabricated.
Emit: > Section: Fidelity warning [generated]

MOCK BODY:
  Generate content following exact golden structural pattern of {skill-id}: correct section
  headings, required tables/lists, gate or verdict in expected position, enforcement mechanisms
  present. A reader familiar with {skill-id} must identify the skill from the body alone.
Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Scope-driven rule: Scope=multi-step -> emit MULTI-STEP-ACKNOWLEDGED;
  Scope=single-step -> check verification check table; emit MATCH or MISMATCH.

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source [MATCH|MISMATCH]
           | compliance-tags [MATCH|MISMATCH] | tier [MATCH|MISMATCH]
  If any single-step MISMATCH: emit halt error. Stop. S-5.1-S-5.4 do not execute.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit: > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit: > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as last line of artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 — Convergent: All Three Axes (V-01 + V-02 + V-03)

**Axes**: S-3 modal Affirmative closure + S-4 First rule bypass-vector enumeration + S-5.3 halt gate.  
**Hypothesis**: The three axes address three distinct sites in the FLAG lifecycle. V-01 makes the declaration site (S-3) state impossibility rather than policy. V-02 makes the consumption site (S-4) close every named bypass vector. V-03 makes the post-write verification step (S-5.3) consistent with S-5.0's halt-on-MISMATCH semantics. A specification where all three hold has no site in the FLAG lifecycle that admits interpretation gaps or permits a corrupted artifact to be written.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

LIFECYCLE:
  P-0  Cross-reference protocol -- register bracket tokens; establish two-phase lookup obligation
  S-0  Read TOPICS.md and emit
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation
    S-3.1  carry -- re-emit S-0 values at point of S-3 consumption
    S-3.2  compliance -- detect compliance signal before flag runs
    S-3.3  flag -- compute FLAG with path discriminator and emit
       Note: S-3.1 must emit before S-3.2 begins; S-3.2 must emit before S-3.3 begins.
  S-4  Artifact generation
  S-5  Finalization
    S-5.0  propagation -- verify PROPAGATION table bindings; halt if any MISMATCH detected
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values;
           halt if Category MISMATCH or Flag MISMATCH
    S-5.4  write -- artifact written emit and next-step line
       Note: S-5.0 through S-5.4 execute in sequence. If S-5.0 detects any single-step
       MISMATCH, execution stops; S-5.1-S-5.4 do not execute. If S-5.3 detects a
       Category or Flag MISMATCH, execution stops; S-5.4 does not execute.

SUB-STEP LABEL PROPAGATION:

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                   | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source             | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags         | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                    | S-3.3 flag resolved emit    | single-step  |
  | S-5.0           | N/A (finalization)                                       | N/A                     | PROPAGATION verified emit   | N/A          |
  | S-5.1           | N/A (finalization)                                       | N/A                     | manifest count emit         | N/A          |
  | S-5.2           | N/A (finalization)                                       | N/A                     | section ordering emit       | N/A          |
  | S-5.3           | N/A (finalization)                                       | N/A                     | header reconciliation emit  | N/A          |
  | S-5.4           | N/A (finalization)                                       | N/A                     | artifact written emit       | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and S-4 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row  |  :FC = Failure consequence row  |  :ABD = Anti-bypass declaration

  | Token      | Step | Row type                    | Paired token | Direction                    |
  |------------|------|-----------------------------|--------------|------------------------------|
  | [S-3:CS]   | S-3  | Cross-site reference row    | [S-4:FC]     | forward --> names S-4        |
  | [S-4:FC]   | S-4  | Failure consequence row     | [S-3:CS]     | <-- backward, names S-3      |
  | [P-0:ABD]  | P-0  | Anti-bypass declaration     | (self)       | definition point             |

Lookup obligation: P-0 table, row 1 = [S-3:CS]; row 2 = [S-4:FC]; row 3 = [P-0:ABD].
Before processing any bracket-token row: Phase 1 (locate) then Phase 2 (confirm Steps 2a-2d,
emit confirmation record, fill Match field only). DO NOT WRITE the row until record is emitted.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                  | Downstream-Action                                                                      |
  |-----------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps as artifact subject; no single sub-step anchor               |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided     | Consumed at S-3.3 for tier-conditional flag refinement                                 |
  | compliance-tags | TOPICS.md entry if found; none if not found                                 | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                               |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins       |

---

STEP S-1 -- SKILL SELECTION

  | Namespace | Default skill     | Exclusion note                                  |
  |-----------|-------------------|-------------------------------------------------|
  | scout     | scout-feasibility |                                                 |
  | draft     | draft-spec        |                                                 |
  | review    | review-design     |                                                 |
  | flow      | flow-resilience   |                                                 |
  | trace     | trace-request     |                                                 |
  | prove     | prove-hypothesis  |                                                 |
  | listen    | listen-support    |                                                 |
  | program   | program-plan      |                                                 |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)  |

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If skill not found: emit error and stop.
Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY
  Emit: > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit: > Compliance check: {DETECTED [signal: {signal-id}] | NOT-DETECTED}

  S-3.3 -- FLAG

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical: trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support, listen-feedback,
  listen-adoption.

  Path: BASE | TIER-REFINEMENT (critical at tier >= 2) | COMPLIANCE-OVERRIDE (S-3.2 detected)
  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG immutability chain -- all rows active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context, including paths that do    |
  |                         | not pass through prior steps in normal order                         |
  | Affirmative closure     | No execution path that reaches S-4 can carry a FLAG value other      |
  |                         | than the one emitted here                                            |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, S-4 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the impossibility guarantee stated in the       |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-3 + Row type=Cross-site reference row; assert      |
  | (P-0 table, row 1)      | match; emit confirmation record (fill Match field only).             |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                 |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row      |
  | [P-0:ABD]               | type cells, or without performing Phase 2, is a protocol failure.   |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC]  |

  Confirmation record: Token=[S-3:CS] | Step=S-3 | Row type=Cross-site reference row | Match=___

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest:
  > Pre-generation manifest:
  > - Section: MOCK ARTIFACT header block
  > - Section: Fidelity warning ({CATEGORY}-appropriate)
  > - Section: Mock body ({skill-id} golden structure)
  > - Gate/verdict: Next-step invocation line
Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

HEADER BLOCK:

FLAG prohibition chain -- all rows govern this step before any header field is written:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it by any means:        |
  |                         | recomputation from category and tier, inference from skill-id,       |
  |                         | derivation from an intermediary variable, default-table lookup,      |
  |                         | or any other mechanism.                                              |
  | Priority                | No instruction in this step can precede this rule                    |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | Declarative closure     | No instruction in S-4 precedes this rule                             |
  | All-governed            | Every instruction in this step, named or unnamed, is governed by     |
  |                         | this rule, including paths that do not pass through prior steps in   |
  |                         | normal order                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table, row 2. Phase 2 (Steps 2a-   |
  | before writing this row | 2d): read Step=S-4 + Row type=Failure consequence row; assert        |
  | (P-0 table, row 2)      | match; emit confirmation record (fill Match field only).             |
  |                         | DO NOT WRITE THE ROW until Steps 2a-2d are complete.                 |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row      |
  | [P-0:ABD]               | type cells, or without performing Phase 2, is a protocol failure.   |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS] Re-deriving FLAG here produces a category  |
  |                         | mismatch invisible to downstream tooling; undetectable without       |
  |                         | manual header inspection                                             |

  Confirmation record: Token=[S-4:FC] | Step=S-4 | Row type=Failure consequence row | Match=___

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING:
  HIGH-STRUCTURE -> NOTE: HIGH-STRUCTURE mock. Structure reliable. Content synthetic.
    Adequate Tier 1. REAL-REQUIRED Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
  EVIDENCE-HEAVY -> WARNING: EVIDENCE-HEAVY mock. Evidence fabricated. Real {skill-id} run required.
  MIXED -> CAUTION: MIXED mock. Tables/gates reliable. Claims may be partially fabricated.
Emit: > Section: Fidelity warning [generated]

MOCK BODY:
  Generate content following exact golden structural pattern of {skill-id}: correct section
  headings, required tables/lists, gate or verdict in expected position, enforcement mechanisms
  present. A reader familiar with {skill-id} must identify the skill from the body alone.
Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Scope-driven rule: Scope=multi-step -> emit MULTI-STEP-ACKNOWLEDGED;
  Scope=single-step -> check verification check table; emit MATCH or MISMATCH.

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source [MATCH|MISMATCH]
           | compliance-tags [MATCH|MISMATCH] | tier [MATCH|MISMATCH]
  If any single-step MISMATCH: emit halt error. Stop. S-5.1-S-5.4 do not execute.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit: > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit: > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  If Category MISMATCH or Flag MISMATCH:
    Emit: > HEADER MISMATCH: run halted -- Category or Flag value in artifact header does
             not match S-2 or S-3 audit value; repair header before S-5.4
    Stop. Do not execute S-5.4.

  S-5.4 -- WRITE
  Write as last line of artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## Round 4 Summary

| Variate | Axis | New probe | Expected vs baseline |
|---------|------|-----------|----------------------|
| V-01 | S-3 Affirmative closure modal | C-52 | C-01-C-51 PASS + C-52 |
| V-02 | S-4 First rule bypass vectors | C-53 | C-01-C-51 PASS + C-53 |
| V-03 | S-5.3 halt gate | C-54 | C-01-C-51 PASS + C-54 |
| V-04 | V-01 + V-02 | C-52 + C-53 | C-01-C-51 PASS + C-52 + C-53 |
| V-05 | V-01 + V-02 + V-03 | C-52 + C-53 + C-54 | C-01-C-51 PASS + C-52 + C-53 + C-54 |

**Independence check**: All three axes are structurally independent — they touch different rows (S-3 Affirmative closure, S-4 First rule, S-5.3 halt block) with no shared text. V-01 through V-03 each isolate one axis cleanly. V-05 is the convergence candidate if all three probes pass.
