---
skill: quest-variate
skill_target: mock-ns
round: 21
rubric_version: 20
date: 2026-03-16
invoked_as: Round 7
---

# mock-ns -- Round 21 Variations

> **Note on round numbering**: This skill was invoked with "(Round 7)" but the session already
> contains scorecards through R20 and rubric v20. These are Round 21 variations targeting
> 100 under v20 (C-01--C-51) and probing new C-52+ patterns.

Rubric: v20 (C-01 through C-51, 5 essential / 3 recommended / 43 aspirational).
Scoring formula: `(E/5 x 60) + (R/3 x 30) + (A/43 x 10)`

R20 baseline: R20 V-05 -- full convergence on C-48 (S-4 Priority row modal form),
C-49 ([P-0:ABD] bracket token at both chain Anti-bypass echo rows), C-50 (All-governed
non-sequential path coverage), C-51 (All-governed "named or unnamed"). All C-01--C-51 pass.

R21 target: all five variates score 100 under v20. Goal: identify excellence patterns
for C-52, C-53, C-54 in v21.

Three new axes selected for single-axis isolation in R21:

1. **S-3 Immutability Chain: No-exemption modal promotion** (C-52 probe): C-48 converted
   the S-4 prohibition chain Priority row from a positional claim ("This rule is first in
   this step") to a modal impossibility claim ("No instruction in this step can precede
   this rule"). The S-3 immutability chain No-exemption row currently says "No path is
   exempt" -- a declarative claim. The same modal promotion applies: "No path CAN be
   exempt from this guarantee" forecloses special-case arguments that C-48's rationale
   identifies as the interpretation gap. The S-4 and S-3 chains now share the same
   anti-exemption precision vocabulary.

2. **S-4 Prohibition Chain: No-exemption modal promotion** (C-53 probe): C-48 made the
   S-4 Priority row modal. The S-4 No-exemption row currently says "No instruction in this
   step is exempt" -- also a declarative claim. Applying the same modal form: "No
   instruction in this step CAN be exempt from this rule" closes the "my instruction is
   special" interpretation gap at the No-exemption row, just as C-48 closed the "my step
   has a different ordering" gap at the Priority row. C-52 and C-53 target different chains
   (S-3 vs S-4) but apply the same pattern (modal impossibility on No-exemption row).

3. **P-0 ABD Halt-on-Violation** (C-54 probe): The P-0 confirmation record requires
   Match=PASS or Match=FAIL. When Match=FAIL, the spec declares a protocol failure but
   specifies no halt mechanism. C-42 established that S-5.0 MISMATCH halts execution.
   The same halt-on-failure pattern applied to ABD violations: if confirmation record
   Match=FAIL at any token site, emit `> ABD VIOLATION: [token-name] at [step] --
   execution halted` and stop. This converts the ABD from a declaration with observable
   failure to a declaration with enforced failure -- the same structural move C-42 made
   for propagation verification.

---

## Variation Index

| Variate | Axis | Single or combined |
|---------|------|--------------------|
| V-01 | S-3 No-exemption modal promotion | Single (C-52 probe) |
| V-02 | S-4 No-exemption modal promotion | Single (C-53 probe) |
| V-03 | P-0 ABD halt-on-violation | Single (C-54 probe) |
| V-04 | S-3 + S-4 No-exemption modal promotion | Combined (C-52 + C-53) |
| V-05 | Full convergence -- all three axes | Combined (C-52 + C-53 + C-54) |

---

## V-01 -- S-3 Immutability Chain: No-Exemption Modal Promotion

**Axis**: C-52 probe (single). Changes the S-3 FLAG immutability chain No-exemption row
from "No path is exempt" (declarative) to "No path CAN be exempt from this guarantee"
(modal impossibility). All other elements unchanged from R20 V-05.

**Hypothesis**: C-48 showed that the Priority row's declarative form ("This rule is first
in this step") left open the interpretation that a path-specific ordering could place
another instruction first -- modal form ("No instruction CAN precede") closed that gap.
The S-3 No-exemption row has the same structure: "No path is exempt" is a declarative
claim that leaves open the interpretation that a special-case path might be argued as
exempt. "No path CAN be exempt from this guarantee" forecloses that interpretation using
the same modal-impossibility vocabulary C-48 established at S-4. The S-3 and S-4 chains
share the No-exemption concept; they should share the same precision form.

**Predicts**: C-01--C-51 all pass. New C-52 probe active.
**Expected composite**: 100.

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
  P-0  Cross-reference protocol -- establish bracket tokens and anti-bypass declaration
  S-0  Read TOPICS.md and emit
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation
    S-3.1  carry -- re-emit S-0 values at point of S-3 consumption
    S-3.2  compliance -- detect compliance signal before flag runs
    S-3.3  flag -- compute FLAG with path discriminator and emit
       Note: S-3.1 must emit before S-3.2 begins; S-3.2 must emit before S-3.3 begins.
       Sub-step identifiers S-3.1, S-3.2, S-3.3 are the precision vocabulary for all
       constraint references to flag computation operations.
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
  The sub-step identifiers below are active at three structural locations. Column 1 names
  the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose role as
  parenthetical gloss. Column 2 names the exact Field value from the S-0 table whose
  Downstream-Action anchors to this sub-step -- must match S-0 table Field column exactly,
  no suffix or qualifier. Column 3 names the execution emit that fires at this sub-step.
  Column 4 (Scope) classifies each input-field row: single-step fields receive MATCH/MISMATCH
  verification at S-5.0; multi-step fields receive MULTI-STEP-ACKNOWLEDGED. The topic field
  is exempt from sub-step anchoring; its Scope=multi-step row is included to confirm
  exemption-by-design, not omission-by-oversight.

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                         | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                   | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags               | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                          | S-3.3 flag resolved emit    | single-step  |
  | S-5.0           | N/A (finalization)                                       | N/A                           | PROPAGATION verified emit   | N/A          |
  | S-5.1           | N/A (finalization)                                       | N/A                           | manifest count emit         | N/A          |
  | S-5.2           | N/A (finalization)                                       | N/A                           | section ordering emit       | N/A          |
  | S-5.3           | N/A (finalization)                                       | N/A                           | header reconciliation emit  | N/A          |
  | S-5.4           | N/A (finalization)                                       | N/A                           | artifact written emit       | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and S-4 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step        | Row type                    | Paired token | Direction                     |
  |------------|-------------|-----------------------------|--------------|-------------------------------|
  | [S-3:CS]   | S-3         | Cross-site reference row    | [S-4:FC]     | forward --> names S-4         |
  | [S-4:FC]   | S-4 (header)| Failure consequence row     | [S-3:CS]     | <-- backward, names S-3       |
  | [P-0:ABD]  | P-0         | Anti-bypass declaration     | (self)       | definition point              |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above. P-0 table, row 1 = [S-3:CS]; P-0 table, row 2 = [S-4:FC];
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
    DO NOT WRITE THE ROW until Steps 2a through 2d are complete and the record is emitted.

An executor who recognizes a token without performing Phase 2 has not satisfied this
protocol. Locate-only is a protocol failure.

Do not re-establish this protocol in later steps. Every bracket token in this run is
interpreted and confirmed per this table.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                    | Downstream-Action                                                                        |
  |-----------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                 |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                   |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                 |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins          |

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up namespace default:

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

Find the selected skill in exactly one row:

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

If skill not found in any row: emit error and stop.

Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY
  Emit as the first action of S-3 (before S-3.2 begins):
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit after S-3.1 carry, before S-3.3 flag:
    > Compliance check: {DETECTED [signal: {signal-id}] | NOT-DETECTED}

  S-3.3 -- FLAG
  Compute flag from category, tier, and critical-skill status:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support, listen-feedback,
  listen-adoption.

  Path: BASE if no refinement or override; TIER-REFINEMENT if critical at tier >= 2;
  COMPLIANCE-OVERRIDE if S-3.2 detected a compliance signal.

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context -- no path is exempt        |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path CAN be exempt from this guarantee                            |
  | Failure consequence     | If any path modifies FLAG after this point, S-4 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps       |
  | before writing this row | 2a-2d): read Step=S-3 + Row type=Cross-site reference row; assert   |
  | (P-0 table, row 1)      | match; emit confirmation record from pre-filled table below          |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and Row  |
  | [P-0:ABD]               | type cells, or without performing Phase 2, is a protocol failure.    |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC]  |
  |                         | -- the Failure consequence row in S-4 header assembly (that row      |
  |                         | identifies itself as this row's mutual target)                        |

Confirmation record for this row -- pre-filled table block:

**Executor: fill the Match field only. All other fields are pre-filled.**

  | Field      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-3:CS]                       |
  | Step       | S-3                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

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

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | No instruction in this step can precede this rule                    |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | All-governed            | All instructions in this step, named or unnamed, are subject to      |
  |                         | this rule, including paths that do not pass through prior steps in   |
  |                         | normal order                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table, row 2. Phase 2 (Steps       |
  | before writing this row | 2a-2d): read Step=S-4 (header) + Row type=Failure consequence row;  |
  | (P-0 table, row 2)      | assert match; emit confirmation record from pre-filled table below   |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading the Step and Row  |
  | [P-0:ABD]               | type cells, or without performing Phase 2, is a protocol failure.    |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS -- Cross-site reference row in S-3]         |
  |                         | Re-deriving FLAG here produces a category mismatch invisible to      |
  |                         | downstream tooling that silently corrupts the artifact's trust tier; |
  |                         | the corruption is undetectable without manual header inspection       |

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
  Before S-5.1, verify each input-field row in the PROPAGATION table (rows where Scope is
  single-step or multi-step; exclude Scope=N/A finalization rows). Apply the Scope-driven
  verification rule:
    - Scope=multi-step: confirm the field's Downstream-Action entry acknowledges multi-step
      scope explicitly ("no single sub-step anchor" or equivalent);
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
```

---

## V-02 -- S-4 Prohibition Chain: No-Exemption Modal Promotion

**Axis**: C-53 probe (single). Changes the S-4 FLAG prohibition chain No-exemption row
from "No instruction in this step is exempt" (declarative) to "No instruction in this
step CAN be exempt from this rule" (modal impossibility). All other elements unchanged
from R20 V-05.

**Hypothesis**: C-48 converted S-4's Priority row from positional to modal. The Priority
and No-exemption rows address different enforcement gaps at the same consumption site:
Priority governs ordering (which instruction runs first); No-exemption governs scope
(which instructions are within the rule's reach). V-01 applied modal promotion to S-3's
No-exemption row. V-02 applies the same promotion to S-4's No-exemption row. Together
(in V-04), both No-exemption rows across both chains are at modal precision, matching
the Priority row's modal form that C-48 established at S-4.

**Predicts**: C-01--C-51 all pass. New C-53 probe active.
**Expected composite**: 100.

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
  P-0  Cross-reference protocol -- establish bracket tokens and anti-bypass declaration
  S-0  Read TOPICS.md and emit
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation
    S-3.1  carry -- re-emit S-0 values at point of S-3 consumption
    S-3.2  compliance -- detect compliance signal before flag runs
    S-3.3  flag -- compute FLAG with path discriminator and emit
       Note: S-3.1 must emit before S-3.2 begins; S-3.2 must emit before S-3.3 begins.
       Sub-step identifiers S-3.1, S-3.2, S-3.3 are the precision vocabulary for all
       constraint references to flag computation operations.
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
  The sub-step identifiers below are active at three structural locations. Column 1 names
  the sub-step as it must appear in the S-0 CONSTRAINT block. Column 2 names the exact
  Field value from the S-0 table whose Downstream-Action anchors to this sub-step.
  Column 3 names the execution emit. Column 4 (Scope) classifies each input-field row.

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                         | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                   | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags               | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                          | S-3.3 flag resolved emit    | single-step  |
  | S-5.0           | N/A (finalization)                                       | N/A                           | PROPAGATION verified emit   | N/A          |
  | S-5.1           | N/A (finalization)                                       | N/A                           | manifest count emit         | N/A          |
  | S-5.2           | N/A (finalization)                                       | N/A                           | section ordering emit       | N/A          |
  | S-5.3           | N/A (finalization)                                       | N/A                           | header reconciliation emit  | N/A          |
  | S-5.4           | N/A (finalization)                                       | N/A                           | artifact written emit       | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and S-4 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step        | Row type                    | Paired token | Direction                     |
  |------------|-------------|-----------------------------|--------------|-------------------------------|
  | [S-3:CS]   | S-3         | Cross-site reference row    | [S-4:FC]     | forward --> names S-4         |
  | [S-4:FC]   | S-4 (header)| Failure consequence row     | [S-3:CS]     | <-- backward, names S-3       |
  | [P-0:ABD]  | P-0         | Anti-bypass declaration     | (self)       | definition point              |

Lookup obligation: before processing any row containing a bracket token, look up the
token in the table above.

Lookup protocol -- two phases, required before writing any bracket-token row:

  Phase 1 -- Locate: find the row in the table above by matching the token name.

  Phase 2 -- Confirm (four steps, in order):
    Step 2a: Read the Step cell.
    Step 2b: Read the Row type cell.
    Step 2c: Assert that the step name matches the step you are currently writing
             and that the row type name matches the role of this row in the chain.
    Step 2d: Emit confirmation record (pre-filled at use site; fill Match field only):
               Token: {pre-filled} | Step: {pre-filled} | Row type: {pre-filled} | Match: PASS|FAIL
    DO NOT WRITE THE ROW until Steps 2a-2d are complete and the record is emitted.

Locate-only is a protocol failure.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                    | Downstream-Action                                                                        |
  |-----------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                 |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                   |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                 |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins          |

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up namespace default:

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

Find the selected skill in exactly one row:

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

If skill not found in any row: emit error and stop.

Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1 -- CARRY
  Emit as the first action of S-3 (before S-3.2 begins):
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit after S-3.1 carry, before S-3.3 flag:
    > Compliance check: {DETECTED [signal: {signal-id}] | NOT-DETECTED}

  S-3.3 -- FLAG
  Compute flag from category, tier, and critical-skill status:

    | Category       | Tier | Skill condition | Flag value                                                    |
    |----------------|------|-----------------|---------------------------------------------------------------|
    | HIGH-STRUCTURE | any  | not critical    | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 1    | critical        | none (structural coverage reliable)                           |
    | HIGH-STRUCTURE | 2+   | critical        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
    | EVIDENCE-HEAVY | any  | any             | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
    | MIXED          | any  | any             | REVIEW-FOR-PLAUSIBILITY                                       |

  Critical skills: trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support, listen-feedback,
  listen-adoption.

  Path: BASE if no refinement or override; TIER-REFINEMENT if critical at tier >= 2;
  COMPLIANCE-OVERRIDE if S-3.2 detected a compliance signal.

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context -- no path is exempt        |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value         |
  |                         | emitted here                                                         |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, S-4 will inherit a       |
  |                         | corrupted value that cannot be distinguished from a correctly-        |
  |                         | computed one                                                         |
  | Guarantee-break         | This violation breaks the closure guarantee stated in the            |
  |                         | Affirmative closure row above                                        |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps       |
  | before writing this row | 2a-2d): read Step=S-3 + Row type=Cross-site reference row; assert   |
  | (P-0 table, row 1)      | match; emit confirmation record (Step 2d). DO NOT WRITE THE ROW     |
  |                         | until Steps 2a-2d are complete and the record is emitted.            |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row type |
  | [P-0:ABD]               | cells, or without performing Phase 2, is a protocol failure.         |
  | Cross-site ref [S-3:CS] | The failure produces the same silent category mismatch at [S-4:FC]  |

Confirmation record -- pre-filled:

  | Field      | Value                    |  | Token: [S-3:CS] | Step: S-3 | Row type: Cross-site reference row | Match: ___ |

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

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | No instruction in this step can precede this rule                    |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | All-governed            | All instructions in this step, named or unnamed, are subject to      |
  |                         | this rule, including paths that do not pass through prior steps in   |
  |                         | normal order                                                         |
  | No-exemption            | No instruction in this step CAN be exempt from this rule             |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table, row 2. Phase 2 (Steps       |
  | before writing this row | 2a-2d): read Step=S-4 (header) + Row type=Failure consequence row;  |
  | (P-0 table, row 2)      | assert match; emit confirmation record (Step 2d). DO NOT WRITE THE  |
  |                         | ROW until Steps 2a-2d are complete and the record is emitted.        |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without reading Step and Row type |
  | [P-0:ABD]               | cells, or without performing Phase 2, is a protocol failure.         |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS] Re-deriving FLAG here produces a category  |
  |                         | mismatch invisible to downstream tooling                             |

Confirmation record -- pre-filled:

  | Token: [S-4:FC] | Step: S-4 (header) | Row type: Failure consequence row | Match: ___ |

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
  enforcement mechanisms present. Use {topic} as subject.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION
  Before S-5.1, verify each input-field row in the PROPAGATION table. Apply the
  Scope-driven verification rule:
    - Scope=multi-step: emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions in the verification check table;
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
    Emit: > PROPAGATION MISMATCH: run halted
    Stop. Do not execute S-5.1 through S-5.4.

  S-5.1 -- COUNT
  Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit: > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit: > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 -- P-0 ABD Halt-on-Violation

**Axis**: C-54 probe (single). Adds an ABD violation halt mechanism to the P-0 protocol.
When a confirmation record at any token site returns Match=FAIL, the executor emits
`> ABD VIOLATION: [token-name] at [step] -- execution halted` and stops immediately.
All other elements unchanged from R20 V-05.

**Hypothesis**: C-42 established that S-5.0 propagation MISMATCH halts execution --
detecting a mismatch without stopping is weaker than detecting and stopping. The same
argument applies to the ABD: the P-0 confirmation record currently requires Match=PASS
or Match=FAIL, but FAIL produces no halt. An executor who writes Match=FAIL in the
confirmation record and continues processing has violated the ABD, but the spec provides
no mechanism to surface that violation as an execution failure. Adding a halt-on-FAIL
mechanism at each confirmation record site converts the ABD from a declarative protocol
to an enforced protocol -- the same structural move C-42 made for propagation verification.

**Predicts**: C-01--C-51 all pass. New C-54 probe active.
**Expected composite**: 100.

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
  P-0  Cross-reference protocol -- establish bracket tokens and anti-bypass declaration
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

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                         | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                   | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags               | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                          | S-3.3 flag resolved emit    | single-step  |
  | S-5.0           | N/A (finalization)                                       | N/A                           | PROPAGATION verified emit   | N/A          |
  | S-5.1           | N/A (finalization)                                       | N/A                           | manifest count emit         | N/A          |
  | S-5.2           | N/A (finalization)                                       | N/A                           | section ordering emit       | N/A          |
  | S-5.3           | N/A (finalization)                                       | N/A                           | header reconciliation emit  | N/A          |
  | S-5.4           | N/A (finalization)                                       | N/A                           | artifact written emit       | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): An executor who processes a bracket token without reading
the Step and Row type cells has performed only Phase 1. An executor who performs Phase 1
without performing Phase 2 violates this protocol. Locate-only is a protocol failure.
Anti-bypass echo rows at S-3 and S-4 echo this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row
    :ABD = Anti-bypass declaration

  | Token      | Step        | Row type                    | Paired token | Direction                     |
  |------------|-------------|-----------------------------|--------------|-------------------------------|
  | [S-3:CS]   | S-3         | Cross-site reference row    | [S-4:FC]     | forward --> names S-4         |
  | [S-4:FC]   | S-4 (header)| Failure consequence row     | [S-3:CS]     | <-- backward, names S-3       |
  | [P-0:ABD]  | P-0         | Anti-bypass declaration     | (self)       | definition point              |

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
               Token: {pre-filled} | Step: {pre-filled} | Row type: {pre-filled} | Match: PASS|FAIL
    DO NOT WRITE THE ROW until Steps 2a-2d are complete and the record is emitted.

Halt-on-violation: If the Match field in any confirmation record is FAIL:
  Emit: > ABD VIOLATION: [token-name] at [step] -- execution halted
  Stop immediately. Do not write the row. Do not proceed to any subsequent step.
  A FAIL Match record means the step identity or row type did not match the P-0 table;
  continuing execution would process a token row without confirmed step ownership, which
  is the exact failure the ABD exists to prevent.

Locate-only is a protocol failure.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                    | Downstream-Action                                                                        |
  |-----------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                 |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                   |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                 |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins          |

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up namespace default:

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

Find the selected skill in exactly one row:

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

If skill not found in any row: emit error and stop.

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

  Critical skills: trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support, listen-feedback,
  listen-adoption.

  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE

  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

FLAG immutability chain:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context -- no path is exempt        |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value here    |
  | No-exemption            | No path is exempt                                                    |
  | Failure consequence     | If any path modifies FLAG after this point, S-4 inherits a corrupted |
  |                         | value that cannot be distinguished from a correctly-computed one     |
  | Guarantee-break         | This violation breaks the Affirmative closure guarantee              |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-3:CS] in P-0 table, row 1. Phase 2 (Steps       |
  | before writing this row | 2a-2d): assert step match; emit confirmation record. DO NOT WRITE   |
  | (P-0 table, row 1)      | THE ROW until Steps 2a-2d are complete. If Match=FAIL: ABD VIOLATION|
  |                         | -- emit halt emit and stop before writing this row.                  |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without Phase 2 is a failure.     |
  | [P-0:ABD]               |                                                                      |
  | Cross-site ref [S-3:CS] | Failure produces silent mismatch at [S-4:FC]                         |

Confirmation record for [S-3:CS] -- pre-filled:

  | Token: [S-3:CS] | Step: S-3 | Row type: Cross-site reference row | Match: ___ |

  If Match = FAIL:
    Emit: > ABD VIOLATION: [S-3:CS] at S-3 -- execution halted
    Stop. Do not write the Cross-site ref [S-3:CS] row. Do not proceed to S-4.

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

FLAG prohibition chain:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | No instruction in this step can precede this rule                    |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | All-governed            | All instructions in this step, named or unnamed, are subject to      |
  |                         | this rule, including paths that do not pass through prior steps in   |
  |                         | normal order                                                         |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table, row 2. Phase 2 (Steps       |
  | before writing this row | 2a-2d): assert step match; emit confirmation record. DO NOT WRITE   |
  | (P-0 table, row 2)      | THE ROW until Steps 2a-2d complete. If Match=FAIL: ABD VIOLATION    |
  |                         | -- emit halt emit and stop.                                          |
  | Anti-bypass echo        | Per [P-0:ABD]: processing this row without Phase 2 is a failure.     |
  | [P-0:ABD]               |                                                                      |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS] Re-deriving FLAG produces silent mismatch  |

Confirmation record for [S-4:FC] -- pre-filled:

  | Token: [S-4:FC] | Step: S-4 (header) | Row type: Failure consequence row | Match: ___ |

  If Match = FAIL:
    Emit: > ABD VIOLATION: [S-4:FC] at S-4 (header) -- execution halted
    Stop. Do not write the Failure conseq [S-4:FC] row. Do not write the artifact.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3 -- copied verbatim, not rederived}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE -> NOTE: HIGH-STRUCTURE mock. Structure reliable. Content synthetic.
  EVIDENCE-HEAVY -> WARNING: EVIDENCE-HEAVY mock. Content evidentially fabricated.
  MIXED -> CAUTION: MIXED mock. Tables reliable. Claims may be partially fabricated.

Emit: > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning): Generate {skill-id} golden structure content.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- PROPAGATION VERIFICATION

  Verification check table (single-step fields):

  | Field           | Expected CONSTRAINT string              | Expected Downstream-Action string  |
  |-----------------|-----------------------------------------|------------------------------------|
  | tier-source     | contains "S-3.1 (carry)"                | contains "Consumed at S-3.1"       |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2"       |
  | tier            | contains "S-3.3 (flag computation)"     | contains "Consumed at S-3.3"       |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH|MISMATCH] | compliance-tags [MATCH|MISMATCH] | tier [MATCH|MISMATCH]

  If any single-step MISMATCH: emit > PROPAGATION MISMATCH: run halted. Stop.

  S-5.1: Emit: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE}
  S-5.2: Emit: > Section ordering: {IN-ORDER | REORDERED}
  S-5.3: Emit: > Header: Category={CATEGORY} [S-2: MATCH|MISMATCH] | Flag={flag} [S-3: MATCH|MISMATCH]
  S-5.4: Write last artifact line: Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
         Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-04 -- Symmetric No-Exemption Modal Promotion (S-3 + S-4)

**Axes**: C-52 + C-53 (two-axis combination). Both the S-3 immutability chain
No-exemption row ("No path CAN be exempt from this guarantee") and the S-4 prohibition
chain No-exemption row ("No instruction in this step CAN be exempt from this rule") are
promoted to modal form. All other elements unchanged from R20 V-05.

**Hypothesis**: V-01 and V-02 probe independent axes at independent steps. Combining
them tests whether both No-exemption rows can simultaneously carry modal precision without
structural conflict. They cannot conflict: S-3 and S-4 are separate steps with independent
chain tables; the No-exemption rows in each chain govern their respective scopes (S-3:
paths through S-4; S-4: instructions in header assembly). Together they achieve symmetric
modal precision across the two chain tables: every declarative claim in both chains that
has an analogous modal form now uses modal form.

**Predicts**: C-01--C-51 all pass. C-52 + C-53 probes both active.
**Expected composite**: 100.

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
  P-0  Cross-reference protocol -- establish bracket tokens and anti-bypass declaration
  S-0  Read TOPICS.md and emit
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation (S-3.1 carry, S-3.2 compliance, S-3.3 flag)
  S-4  Artifact generation
  S-5  Finalization (S-5.0 propagation, S-5.1 count, S-5.2 order, S-5.3 header, S-5.4 write)
     Note: S-5.0 halts on any single-step MISMATCH before S-5.1 runs.

SUB-STEP LABEL PROPAGATION:

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                         | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                   | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags               | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                          | S-3.3 flag resolved emit    | single-step  |
  | S-5.0-S-5.4     | N/A (finalization)                                       | N/A                           | (per sub-step)              | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

  Abbreviation key: :CS = Cross-site reference row | :FC = Failure consequence row | :ABD = Anti-bypass declaration

  | Token      | Step        | Row type                    | Paired token | Direction               |
  |------------|-------------|-----------------------------|--------------|-------------------------|
  | [S-3:CS]   | S-3         | Cross-site reference row    | [S-4:FC]     | forward --> names S-4   |
  | [S-4:FC]   | S-4 (header)| Failure consequence row     | [S-3:CS]     | <-- backward, names S-3 |
  | [P-0:ABD]  | P-0         | Anti-bypass declaration     | (self)       | definition point        |

Anti-bypass declaration (ABD): Phase 1 (locate) without Phase 2 (confirm) is a protocol failure.
Lookup protocol: Phase 1 = locate token in table. Phase 2 = Steps 2a-2d: read Step, read Row type,
assert match, emit pre-filled confirmation record. DO NOT WRITE ROW until record is emitted.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Emit: > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
        tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                  | Downstream-Action                                                            |
  |-----------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                   | Consumed across all steps; no single sub-step anchor                         |
  | tier            | TOPICS.md entry; 1 if not found; --tier if provided                         | Consumed at S-3.3                                                            |
  | compliance-tags | TOPICS.md entry; none if not found                                          | Consumed at S-3.2                                                            |
  | tier-source     | TOPICS.md | default-1 | --tier-override                                    | Consumed at S-3.1                                                            |

---

STEP S-1 -- SKILL SELECTION

Namespace defaults: scout=scout-feasibility | draft=draft-spec | review=review-design |
  flow=flow-resilience | trace=trace-request | prove=prove-hypothesis |
  listen=listen-support | program=program-plan | topic=topic-plan (NEVER topic-status)

Emit: > Generating mock for {namespace}/{skill-id} [source: --skill arg | default for {namespace}]

---

STEP S-2 -- CATEGORY LOOKUP

  | Category       | Member skills (abbreviated)                                        |
  |----------------|--------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-*, draft-*, review-design, review-code, trace-*, flow-*,     |
  |                | program-plan (see full list in R19 V-01 baseline)                  |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                  |
  |                | listen-feedback, listen-support, listen-adoption                   |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers, review-users |

If skill not found: emit error and stop.
Emit: > CATEGORY assigned: {CATEGORY} [skill: {skill-id}]

---

STEP S-3 -- FLAG COMPUTATION

  S-3.1: Emit > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}
  S-3.2: Emit > Compliance check: {DETECTED [signal: {id}] | NOT-DETECTED}
  S-3.3: Compute flag from category/tier/critical status.
  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE
  Emit: > FLAG resolved: {flag} [path: {PATH}]

FLAG immutability chain:

  | Protection layer        | Rule                                                                |
  |-------------------------|---------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                    |
  | Path classes            | Not in any step, branch, fallback, regeneration, or execution context|
  | Affirmative closure     | Every path reaching S-4 carries the FLAG value emitted here         |
  | No-exemption            | No path CAN be exempt from this guarantee                           |
  | Failure consequence     | Modification after this point produces undetectable corruption at S-4|
  | Guarantee-break         | Any violation breaks the Affirmative closure guarantee              |
  | CONFIRMATION REQUIRED   | P-0 Phase 1+2 at [S-3:CS]. If Match=FAIL: confirm, do not proceed. |
  | Anti-bypass echo [P-0:ABD] | Per [P-0:ABD]: Phase 2 required. Locate-only is a failure.       |
  | Cross-site ref [S-3:CS] | Consumes at [S-4:FC] in S-4 header assembly                         |

  Confirmation record: Token=[S-3:CS] | Step=S-3 | Row type=Cross-site reference row | Match=___

---

STEP S-4 -- ARTIFACT GENERATION

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Pre-generation manifest: Emit > Pre-generation manifest: 3 sections, 0 structures, 1 gate/verdict
Emit: > Manifest committed: 3 sections | 0 structures | 1 gate/verdict

FLAG prohibition chain:

  | Protection layer        | Rule                                                                |
  |-------------------------|---------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                    |
  | Priority                | No instruction in this step can precede this rule                   |
  | Anti-displacement       | Before any field, lookup, formatting, or other instruction           |
  | All-governed            | All instructions, named or unnamed, including non-sequential paths   |
  | No-exemption            | No instruction in this step CAN be exempt from this rule            |
  | CONFIRMATION REQUIRED   | P-0 Phase 1+2 at [S-4:FC]. If Match=FAIL: halt.                    |
  | Anti-bypass echo [P-0:ABD] | Per [P-0:ABD]: Phase 2 required. Locate-only is a failure.       |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS] Rederivation = silent mismatch            |

  Confirmation record: Token=[S-4:FC] | Step=S-4 (header) | Row type=Failure consequence row | Match=___

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id} | Topic: {topic} | Category: {CATEGORY from S-2}
  Date: {date} | Status: MOCK (awaiting review) | Flag: {flag from S-3 -- verbatim}

Emit: > Section: MOCK ARTIFACT header block [generated]

Fidelity warning (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED -- per CATEGORY).
Emit: > Section: Fidelity warning [generated]

Mock body following {skill-id} golden structure.
Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

  S-5.0 -- Verify PROPAGATION table. Check table:
  | tier-source | contains "S-3.1 (carry)" | contains "Consumed at S-3.1" |
  | compliance-tags | contains "S-3.2 (compliance detection)" | contains "Consumed at S-3.2" |
  | tier | contains "S-3.3 (flag computation)" | contains "Consumed at S-3.3" |
  Emit PROPAGATION verified. Halt on any single-step MISMATCH.

  S-5.1: > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE}
  S-5.2: > Section ordering: {IN-ORDER | REORDERED}
  S-5.3: > Header: Category={CATEGORY} [S-2: MATCH|MISMATCH] | Flag={flag} [S-3: MATCH|MISMATCH]
  S-5.4: Write Next: line. Emit > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 -- Full Convergence (All Three New Axes)

**Axes**: C-52 + C-53 + C-54. S-3 No-exemption modal ("No path CAN be exempt from this
guarantee"), S-4 No-exemption modal ("No instruction CAN be exempt from this rule"), and
P-0 halt-on-ABD-violation at both token sites.

**Hypothesis**: All three axes address distinct enforcement gaps at distinct structural
locations:
- C-52: S-3 immutability chain declarative-to-modal at No-exemption row
- C-53: S-4 prohibition chain declarative-to-modal at No-exemption row
- C-54: P-0 confirmation record FAIL result triggers halt-on-violation at both token sites
Together they extend the modal-impossibility pattern (introduced at S-4 Priority by C-48)
to No-exemption rows in both chains, and extend the halt-on-failure pattern (introduced
at S-5.0 by C-42) to the ABD enforcement mechanism at P-0. The full enforcement
architecture has no declarative-only claims remaining at the No-exemption level, and
no detected failures that proceed without halt.

**Predicts**: C-01--C-51 all pass. C-52, C-53, and C-54 probes all active.
**Expected composite**: 100.

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
  P-0  Cross-reference protocol -- bracket tokens, anti-bypass declaration, halt-on-violation
  S-0  Read TOPICS.md and emit
  S-1  Skill selection
  S-2  Category lookup
  S-3  Flag computation
    S-3.1  carry | S-3.2  compliance | S-3.3  flag
  S-4  Artifact generation
  S-5  Finalization
    S-5.0  propagation (halt on MISMATCH) | S-5.1  count | S-5.2  order
    S-5.3  header | S-5.4  write

SUB-STEP LABEL PROPAGATION:

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match) | Execution emit              | Scope        |
  |-----------------|----------------------------------------------------------|-------------------------------|-----------------------------|--------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic                         | N/A -- used throughout      | multi-step   |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                   | S-3.1 carry emit            | single-step  |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags               | S-3.2 compliance check emit | single-step  |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                          | S-3.3 flag resolved emit    | single-step  |
  | S-5.0-S-5.4     | N/A (finalization)                                       | N/A                           | (per sub-step)              | N/A          |

---

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

Anti-bypass declaration (ABD): Phase 1 (locate) without Phase 2 (confirm) is a protocol
failure. Locate-only is a protocol failure. Anti-bypass echo rows at S-3 and S-4 echo
this declaration at each bracket-token row.

  Abbreviation key:
    :CS = Cross-site reference row | :FC = Failure consequence row | :ABD = Anti-bypass declaration

  | Token      | Step        | Row type                    | Paired token | Direction               |
  |------------|-------------|-----------------------------|--------------|-------------------------|
  | [S-3:CS]   | S-3         | Cross-site reference row    | [S-4:FC]     | forward --> names S-4   |
  | [S-4:FC]   | S-4 (header)| Failure consequence row     | [S-3:CS]     | <-- backward, names S-3 |
  | [P-0:ABD]  | P-0         | Anti-bypass declaration     | (self)       | definition point        |

Lookup protocol -- two phases, required before writing any bracket-token row:
  Phase 1 -- Locate: find the row in the table above by matching the token name.
  Phase 2 -- Confirm (Steps 2a-2d): read Step, read Row type, assert match, emit
             pre-filled confirmation record. DO NOT WRITE THE ROW until 2a-2d complete.

Halt-on-violation: If any confirmation record Match = FAIL:
  Emit: > ABD VIOLATION: [token-name] at [step] -- execution halted
  Stop immediately. Do not write the row. Do not continue execution.
  A FAIL Match means step identity or row type mismatched the P-0 table.
  Proceeding would process a token row without confirmed step ownership.

Do not re-establish this protocol in later steps.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Emit as the first observable output:
  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

  | Field           | Resolution                                                                    | Downstream-Action                                                                        |
  |-----------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                 |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                   |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                 |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins          |

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

If skill not found in any row: emit error and stop.
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

  Critical skills: trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support, listen-feedback,
  listen-adoption.

  Path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE
  Emit: > FLAG resolved: {flag} [path: BASE | TIER-REFINEMENT | COMPLIANCE-OVERRIDE]

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | Scope                   | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes            | Not in any step, conditional branch, fallback path, regeneration     |
  |                         | sequence, or any other execution context -- no path is exempt        |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value here    |
  | No-exemption            | No path CAN be exempt from this guarantee                            |
  | Failure consequence     | Modification produces undetectable corrupted value at S-4            |
  | Guarantee-break         | Any violation breaks the Affirmative closure guarantee               |
  | CONFIRMATION REQUIRED   | Phase 1+2 for [S-3:CS]. If Match=FAIL: emit ABD VIOLATION, halt.   |
  | before writing this row | DO NOT WRITE THE ROW until Phase 2 complete and record emitted.      |
  | Anti-bypass echo        | Per [P-0:ABD]: Phase 2 required. Locate-only is a protocol failure.  |
  | [P-0:ABD]               |                                                                      |
  | Cross-site ref [S-3:CS] | Consumes at [S-4:FC] in S-4 header assembly                          |

Confirmation record for [S-3:CS] -- pre-filled:

  | Token      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-3:CS]                       |
  | Step       | S-3                            |
  | Row type   | Cross-site reference row       |
  | Match      | _______________                |

  If Match = FAIL:
    Emit: > ABD VIOLATION: [S-3:CS] at S-3 -- execution halted
    Stop. Do not write the Cross-site ref [S-3:CS] row. Do not proceed to S-4.

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

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | No instruction in this step can precede this rule                    |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | All-governed            | All instructions in this step, named or unnamed, are subject to      |
  |                         | this rule, including paths that do not pass through prior steps in   |
  |                         | normal order                                                         |
  | No-exemption            | No instruction in this step CAN be exempt from this rule             |
  | CONFIRMATION REQUIRED   | Phase 1+2 for [S-4:FC]. If Match=FAIL: emit ABD VIOLATION, halt.   |
  | before writing this row | DO NOT WRITE THE ROW until Phase 2 complete and record emitted.      |
  | Anti-bypass echo        | Per [P-0:ABD]: Phase 2 required. Locate-only is a protocol failure.  |
  | [P-0:ABD]               |                                                                      |
  | Failure conseq [S-4:FC] | [Mutual target of S-3:CS] Rederivation produces silent mismatch      |

Confirmation record for [S-4:FC] -- pre-filled:

  | Token      | Value                          |
  |------------|--------------------------------|
  | Token      | [S-4:FC]                       |
  | Step       | S-4 (header)                   |
  | Row type   | Failure consequence row        |
  | Match      | _______________                |

  If Match = FAIL:
    Emit: > ABD VIOLATION: [S-4:FC] at S-4 (header) -- execution halted
    Stop. Do not write the Failure conseq [S-4:FC] row. Do not write the artifact.

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
    evidentially fabricated. A real {skill-id} run is required before any evidence-based
    decision.

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
  Verify each input-field row in the PROPAGATION table. Apply Scope-driven rule:
    - Scope=multi-step: emit MULTI-STEP-ACKNOWLEDGED.
    - Scope=single-step: check both conditions below; MATCH or MISMATCH.

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
  Emit: > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit: > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## Scoring Prediction Summary

| Variate | Axis | New probe | Predicted C-01..C-51 | Predicted composite |
|---------|------|-----------|----------------------|---------------------|
| V-01 | S-3 No-exemption modal promotion | C-52 | 51/51 PASS | 100 |
| V-02 | S-4 No-exemption modal promotion | C-53 | 51/51 PASS | 100 |
| V-03 | P-0 ABD halt-on-violation | C-54 | 51/51 PASS | 100 |
| V-04 | S-3 + S-4 No-exemption modal | C-52 + C-53 | 51/51 PASS | 100 |
| V-05 | Full convergence | C-52 + C-53 + C-54 | 51/51 PASS | 100 |

**Interaction analysis**:
- V-01 modifies only the S-3 immutability chain No-exemption row. No impact on S-4 or P-0.
- V-02 modifies only the S-4 prohibition chain No-exemption row. No impact on S-3 or P-0.
- V-03 adds a halt clause to the P-0 confirmation record protocol at both token sites.
  This is additive -- it adds behavior when Match=FAIL but does not modify the Match=PASS path.
- V-04 combines V-01 + V-02. Independent steps, no interaction.
- V-05 combines all three. No conflicts: the three modifications are in different structural
  sections (S-3 chain, S-4 chain, P-0 protocol) with no shared state.

**Architecture note for V-05**: The spec now has three halt mechanisms:
1. S-5.0: PROPAGATION MISMATCH halts execution (C-42 -- established in R16/R17)
2. P-0 [S-3:CS]: ABD VIOLATION halts execution (C-54 probe)
3. P-0 [S-4:FC]: ABD VIOLATION halts execution (C-54 probe)
All three are detect-and-halt, not detect-and-continue. This makes every critical failure
mode in the FLAG contract an execution-stopping event rather than an observable-but-ignorable
one. The spec converges on a single design principle: observable failures that are not halted
are not actually enforced.

**V-next for Round 22**: With C-52, C-53, C-54 probed, Round 22 candidates include:
- S-3 Path-classes row modal promotion: "Not in any step... CAN be exempt" -- extending modal
  form from No-exemption to the closely related Path-classes row
- P-0 ABD violation reporting granularity: does the ABD VIOLATION emit include the specific
  Step cell value that mismatched, not just the token name and step?
- S-5.0 verification check table: symmetry with halt mechanism -- does the check table
  declare what happens on MATCH as well as what constitutes MISMATCH?
