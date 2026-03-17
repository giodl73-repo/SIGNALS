---
skill: quest-variate
skill_target: mock-ns
round: 18
rubric_version: 14
date: 2026-03-16
---

# mock-ns -- Round 18 Variations

Rubric: v14 (C-01 through C-41, aspirational denominator 33).

New criteria in v14 (now pass conditions):
- **C-39** -- PROPAGATION lifecycle closure: S-5.0 verification gate present; emits per-field
  MATCH/MISMATCH for each sub-step-anchored binding; exempt field emits MULTI-STEP-ACKNOWLEDGED.
- **C-40** -- PROPAGATION table completeness: topic row present with explicit multi-step scope
  annotation; field-count parity with S-0 table.
- **C-41** -- Exact field names in PROPAGATION table column 2: values match S-0 table Field
  column verbatim; column header declares exact-match intent.

R17's best performer (V-05) achieves full convergence on all 41 criteria. R18 baseline:
R17 V-05. All R18 variates inherit C-01 through C-41 and probe C-42+.

Three new axes identified in R17 V-05's S-5.0 PROPAGATION VERIFICATION block:

1. **S-5.0 as a halt gate, not just an observational emit** (C-42 probe): The S-5.0 step
   emits MATCH/MISMATCH verdicts but specifies no behavioral consequence for MISMATCH. A
   MISMATCH verdict indicates the PROPAGATION table's declared binding is inconsistent with
   actual CONSTRAINT block text or a Downstream-Action entry -- a structural error that should
   prevent artifact writing. Without halt behavior, the verification emit is observational
   only: it produces an audit record but does not prevent a structurally inconsistent artifact
   from being written. Adding halt-on-MISMATCH ("if any anchored field returns MISMATCH: emit
   halt error and stop; S-5.1 through S-5.4 do not execute") makes S-5.0 a hard quality gate.
   The MULTI-STEP-ACKNOWLEDGED verdict for topic does not trigger the halt condition; only
   MISMATCH on anchored single-step fields triggers it.

2. **S-5.0 verification criteria as a formal check table** (C-43 probe): The S-5.0
   verification instructions currently specify per-field checks as a prose bullet list that
   mixes structural specification (which strings to match) with procedural instruction (how
   to check). A formal verification check table -- with columns "Field", "Expected CONSTRAINT
   string", and "Expected Downstream-Action string" -- separates specification from procedure,
   makes the expected match strings formally declared rather than inline in prose, and enables
   the S-5.0 emit to be a direct pass/fail against each declared row. The formal check table
   is to S-5.0 what the S-0 input table is to S-0: a structured declaration of what the step
   verifies. It also creates a cross-reference between the PROPAGATION manifest (which declares
   bindings) and the verification check table (which declares the evidence of those bindings).

3. **PROPAGATION table scope column** (C-44 probe): Scope type is currently embedded as a
   column 2 parenthetical ("topic (multi-step; no sub-step anchor)") rather than as a
   dedicated structural column. A "Scope" column with values "single-step" | "multi-step"
   makes scope a first-class attribute. This has a downstream effect on S-5.0: the scope
   column explicitly drives the verification rule -- "for each row, if Scope=single-step:
   MATCH/MISMATCH; if Scope=multi-step: MULTI-STEP-ACKNOWLEDGED" -- making the verification
   logic table-driven rather than hardcoded in prose. A table-driven rule is more auditable
   and structurally consistent with the PROPAGATION manifest's own role as a declaration.

R18 isolates S-5.0 halt-on-MISMATCH (V-01), isolates formal verification check table
(V-02), isolates scope column (V-03), combines halt gate + formal check table (V-04),
and achieves full convergence (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (C-42 -- S-5.0 halt-on-MISMATCH gate) | S-5.0 emits verdicts but has no enforcement consequence. A halt instruction makes it a genuine quality gate: if any anchored field returns MISMATCH, execution stops and S-5.1 through S-5.4 do not run. Without halt, C-39 produces an audit record; with halt, C-39 produces a verified gate that prevents writing a structurally inconsistent artifact. |
| V-02 | Output format (C-43 -- S-5.0 formal verification check table) | The prose bullet list at S-5.0 mixes specification (which strings to match) with procedure (how to check). A formal two-column check table -- "Field | Expected CONSTRAINT string | Expected Downstream-Action string" -- separates declaration from procedure, makes the verification criteria auditable by inspection, and parallels the S-0 input table's role as a structured declaration. The PROPAGATION manifest declares bindings; the verification check table declares the expected evidence of those bindings. |
| V-03 | Output format (C-44 -- PROPAGATION table scope column) | Scope type embedded as a parenthetical in column 2 is a structural encoding that requires inference to extract. A dedicated "Scope" column (single-step \| multi-step) makes scope a first-class attribute and enables the S-5.0 verification rule to be stated as: "read Scope column; single-step → MATCH/MISMATCH; multi-step → MULTI-STEP-ACKNOWLEDGED." The verification logic becomes table-driven, not hardcoded. |
| V-04 | Combined: Lifecycle + Output format (halt gate + formal check table) | V-01's halt-on-MISMATCH + V-02's formal verification check table. The formal table drives which fields are checked; the halt instruction fires if any row fails. Tests whether C-42 and C-43 are jointly satisfiable and whether the formal table makes the halt condition more precisely bounded (halt only on rows that return MISMATCH, not on MULTI-STEP-ACKNOWLEDGED). |
| V-05 | Convergent: Lifecycle + Output format x2 (all three axes combined) | Full structural convergence: halt gate + formal check table + scope column. The scope column classifies each row; the formal check table provides criteria for single-step fields; the halt gate enforces quality for failed single-step checks. The MULTI-STEP-ACKNOWLEDGED path is derived from the scope column, not hardcoded in prose. All three axes interact: scope drives check type, formal table supplies expected strings for single-step fields, halt gate enforces the result. |

---

## V-01 -- Lifecycle Emphasis: S-5.0 Halt-on-MISMATCH (C-42 single axis)

**Axis**: Lifecycle emphasis -- a halt-on-MISMATCH instruction is added to S-5.0. If any
anchored field (tier-source, compliance-tags, tier) returns MISMATCH, S-5.0 emits a halt
error and execution stops; S-5.1 through S-5.4 do not execute. The LIFECYCLE block S-5.0
description is updated to reflect halt behavior. MULTI-STEP-ACKNOWLEDGED for topic does not
trigger the halt. All other elements unchanged from R17 V-05.
**Hypothesis**: S-5.0 currently makes PROPAGATION accuracy observable but has no enforcement
consequence -- subsequent S-5 steps run regardless of verdict. A MISMATCH indicates a
declared binding is inconsistent with actual structural content: the PROPAGATION table claims
"tier-source Downstream-Action entry contains 'Consumed at S-3.1'" but the actual entry does
not. Allowing artifact writing to proceed after detecting this inconsistency makes S-5.0 an
audit log, not a gate. A halt-on-MISMATCH instruction closes this gap: the verification step
enforces consistency before writing.
**Predicts**: C-01 through C-41 pass (full R17 V-05 baseline) | C-42 probe (halt-on-MISMATCH
makes S-5.0 a hard gate). C-43, C-44 not targeted.
**Expected composite**: 41/41 aspirational baseline + C-42 candidate signal.

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
       before the preceding sub-step's emit is written. If S-5.0 detects any MISMATCH,
       execution stops and S-5.1 through S-5.4 do not execute.

SUB-STEP LABEL PROPAGATION:
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names the exact Field value from the S-0 table
  whose Downstream-Action anchors to this sub-step -- must match S-0 table Field column
  exactly. Column 3 names the execution emit that fires at this sub-step. The topic field
  is exempt from sub-step anchoring (multi-step scope); its row is included to confirm
  exemption-by-design rather than omission-by-oversight.

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match)               | Execution emit              |
  |-----------------|----------------------------------------------------------|---------------------------------------------|-----------------------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic (multi-step; no sub-step anchor)      | N/A -- used throughout      |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                                 | S-3.1 carry emit            |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags                             | S-3.2 compliance check emit |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                                        | S-3.3 flag resolved emit    |
  | S-5.0           | N/A (finalization)                                       | N/A                                         | PROPAGATION verified emit   |
  | S-5.1           | N/A (finalization)                                       | N/A                                         | manifest count emit         |
  | S-5.2           | N/A (finalization)                                       | N/A                                         | section ordering emit       |
  | S-5.3           | N/A (finalization)                                       | N/A                                         | header reconciliation emit  |
  | S-5.4           | N/A (finalization)                                       | N/A                                         | artifact written emit       |

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

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

HEADER BLOCK (first content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3.3}

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
  Before S-5.1, verify each PROPAGATION table binding against actual entries. Use exact
  field names from the S-0 table Field column. The topic field is multi-step scope:
  acknowledge rather than verify (no sub-step anchor to match).
    - topic: confirm Downstream-Action entry acknowledges multi-step scope explicitly
      ("no single sub-step anchor" or equivalent)
    - tier-source (S-3.1): confirm CONSTRAINT block contains "S-3.1 (carry)" AND
      tier-source Downstream-Action entry contains "Consumed at S-3.1"
    - compliance-tags (S-3.2): confirm CONSTRAINT block contains "S-3.2 (compliance
      detection)" AND compliance-tags Downstream-Action entry contains "Consumed at S-3.2"
    - tier (S-3.3): confirm CONSTRAINT block contains "S-3.3 (flag computation)" AND
      tier Downstream-Action entry contains "Consumed at S-3.3"

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any anchored field (tier-source, compliance-tags, tier) returns MISMATCH:
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

## V-02 -- Output Format: S-5.0 Formal Verification Check Table (C-43 single axis)

**Axis**: Output format -- the S-5.0 verification instructions replace the prose bullet list
with a formal verification check table (columns: Field, Expected CONSTRAINT string, Expected
Downstream-Action string). The table specifies the exact match strings for each single-step
field. The S-5.0 check procedure is stated as a rule against the table rows rather than
embedded in prose. No halt-on-MISMATCH; no scope column. All other elements unchanged from
R17 V-05.
**Hypothesis**: The prose bullet list at S-5.0 conflates what to verify (the expected strings)
with how to verify (check CONSTRAINT block and Downstream-Action). A formal check table
separates specification from procedure and makes the expected strings auditable by inspection:
a reader can cross-reference "Expected CONSTRAINT string: S-3.1 (carry)" directly against the
CONSTRAINT block text without inferring it from prose. The formal table is the structural
complement to the PROPAGATION manifest: the manifest declares "tier-source Downstream-Action
is 'Consumed at S-3.1'"; the verification table declares "the expected evidence is the string
'Consumed at S-3.1' in that entry." Together they form a closed declaration-plus-evidence pair.
**Predicts**: C-01 through C-41 pass (full R17 V-05 baseline) | C-43 probe (formal check
table replaces prose bullet list at S-5.0). C-42, C-44 not targeted.
**Expected composite**: 41/41 aspirational baseline + C-43 candidate signal.

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
    S-5.0  propagation -- verify PROPAGATION table bindings against actual entries
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line
       Note: S-5.0 through S-5.4 execute in sequence. No S-5 sub-step may begin
       before the preceding sub-step's emit is written.

SUB-STEP LABEL PROPAGATION:
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names the exact Field value from the S-0 table
  whose Downstream-Action anchors to this sub-step -- must match S-0 table Field column
  exactly. Column 3 names the execution emit that fires at this sub-step. The topic field
  is exempt from sub-step anchoring (multi-step scope); its row is included to confirm
  exemption-by-design rather than omission-by-oversight.

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match)               | Execution emit              |
  |-----------------|----------------------------------------------------------|---------------------------------------------|-----------------------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic (multi-step; no sub-step anchor)      | N/A -- used throughout      |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                                 | S-3.1 carry emit            |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags                             | S-3.2 compliance check emit |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                                        | S-3.3 flag resolved emit    |
  | S-5.0           | N/A (finalization)                                       | N/A                                         | PROPAGATION verified emit   |
  | S-5.1           | N/A (finalization)                                       | N/A                                         | manifest count emit         |
  | S-5.2           | N/A (finalization)                                       | N/A                                         | section ordering emit       |
  | S-5.3           | N/A (finalization)                                       | N/A                                         | header reconciliation emit  |
  | S-5.4           | N/A (finalization)                                       | N/A                                         | artifact written emit       |

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

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

HEADER BLOCK (first content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3.3}

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
  Before S-5.1, check each row of the verification check table below against actual entries.
  For each single-step field: confirm both string conditions are present; emit MATCH if both
  pass, MISMATCH if either fails. For topic: confirm Downstream-Action entry acknowledges
  multi-step scope explicitly ("no single sub-step anchor" or equivalent); emit
  MULTI-STEP-ACKNOWLEDGED.

  Verification check table:

  | Field           | Expected CONSTRAINT string       | Expected Downstream-Action string                   |
  |-----------------|----------------------------------|-----------------------------------------------------|
  | topic           | N/A (multi-step scope)           | contains "no single sub-step anchor" or equivalent  |
  | tier-source     | contains "S-3.1 (carry)"         | contains "Consumed at S-3.1"                        |
  | compliance-tags | contains "S-3.2 (compliance      | contains "Consumed at S-3.2"                        |
  |                 |   detection)"                    |                                                     |
  | tier            | contains "S-3.3 (flag            | contains "Consumed at S-3.3"                        |
  |                 |   computation)"                  |                                                     |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

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

## V-03 -- Output Format: PROPAGATION Table Scope Column (C-44 single axis)

**Axis**: Output format -- a fifth "Scope" column (values: single-step | multi-step | N/A)
is added to the PROPAGATION table. The topic row's column 2 entry is simplified from
"topic (multi-step; no sub-step anchor)" to just "topic" since scope is now carried in the
dedicated column. The S-5.0 verification step references the Scope column to determine
check type: single-step rows get MATCH/MISMATCH; multi-step rows get MULTI-STEP-ACKNOWLEDGED.
No halt-on-MISMATCH; no formal check table. All other elements unchanged from R17 V-05.
**Hypothesis**: Embedding scope as a column 2 parenthetical makes scope an implicit attribute
that requires parsing the parenthetical to extract. A dedicated Scope column makes scope
a first-class structural attribute: it can be read at a glance, it enables a rule-based
description of the S-5.0 logic ("read Scope column; apply corresponding verification type"),
and it removes scope annotation from the exact-name field in column 2 -- allowing column 2
to carry only the exact field name with no suffix. This is the same discipline C-41 applies
to column 2 naming: exact field names without decorators. The parenthetical scope annotation
in V-05's "topic (multi-step; no sub-step anchor)" is a C-41 borderline case: the field name
is exact, but a parenthetical qualifier follows. Moving scope to a dedicated column achieves
full separation of concerns in the PROPAGATION table structure.
**Predicts**: C-01 through C-41 pass (full R17 V-05 baseline) | C-44 probe (Scope column
makes scope a first-class structural attribute, drives S-5.0 rule table-derivable).
C-42, C-43 not targeted.
**Expected composite**: 41/41 aspirational baseline + C-44 candidate signal.

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
    S-5.0  propagation -- verify PROPAGATION table bindings against actual entries
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line
       Note: S-5.0 through S-5.4 execute in sequence. No S-5 sub-step may begin
       before the preceding sub-step's emit is written.

SUB-STEP LABEL PROPAGATION:
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names the exact Field value from the S-0 table
  whose Downstream-Action anchors to this sub-step -- must match S-0 table Field column
  exactly, no suffix. Column 3 names the execution emit that fires at this sub-step.
  Column 4 (Scope) classifies each input-field row as single-step or multi-step; the
  Scope value drives the S-5.0 verification type for that row.

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

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

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

HEADER BLOCK (first content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3.3}

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
  Before S-5.1, verify each PROPAGATION table row where Scope is single-step or multi-step
  (exclude Scope=N/A finalization rows). Use the Scope column to determine verification type:
    - Scope=single-step: confirm (a) CONSTRAINT block contains the CONSTRAINT reference ID
      and (b) the field's Downstream-Action entry contains "Consumed at {sub-step-id}";
      emit MATCH if both pass, MISMATCH if either fails.
    - Scope=multi-step: confirm the field's Downstream-Action entry acknowledges multi-step
      scope explicitly ("no single sub-step anchor" or equivalent);
      emit MULTI-STEP-ACKNOWLEDGED.

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

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

## V-04 -- Combined: Lifecycle + Output Format (Halt Gate + Formal Check Table)

**Axis**: Combined V-01 (halt-on-MISMATCH) and V-02 (formal verification check table).
No scope column (single-axis purity on C-44 preserved). The formal check table provides
the specification of what to verify; the halt instruction fires if any single-step row
returns MISMATCH. The interaction: the formal table makes the halt condition precisely
bounded -- halt fires only when a declared table row produces MISMATCH, not on the topic
MULTI-STEP-ACKNOWLEDGED path. The formal table and the halt gate are structurally
complementary: the table declares the pass/fail criteria; the halt gate enforces the result.
**Hypothesis**: C-42 (halt gate) and C-43 (formal check table) are structurally independent
but operationally coupled: the formal table provides the specification that the halt gate
enforces. A formal table without a halt gate is a specification without enforcement; a halt
gate without a formal table is enforcement without a clear pass/fail specification. Together
they close the S-5.0 quality loop: the table declares what "MATCH" means; the gate enforces
that a MISMATCH blocks artifact writing.
**Predicts**: C-01 through C-41 pass | C-42 + C-43 probes satisfied | C-44 not targeted.
**Expected composite**: 41/41 aspirational baseline + C-42 and C-43 candidate signals.

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
       before the preceding sub-step's emit is written. If S-5.0 detects any MISMATCH,
       execution stops and S-5.1 through S-5.4 do not execute.

SUB-STEP LABEL PROPAGATION:
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names the exact Field value from the S-0 table
  whose Downstream-Action anchors to this sub-step -- must match S-0 table Field column
  exactly. Column 3 names the execution emit that fires at this sub-step. The topic field
  is exempt from sub-step anchoring (multi-step scope); its row is included to confirm
  exemption-by-design rather than omission-by-oversight.

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | S-0 table Field (exact match)               | Execution emit              |
  |-----------------|----------------------------------------------------------|---------------------------------------------|-----------------------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic (multi-step; no sub-step anchor)      | N/A -- used throughout      |
  | S-3.1           | S-3.1 (carry)                                            | tier-source                                 | S-3.1 carry emit            |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags                             | S-3.2 compliance check emit |
  | S-3.3           | S-3.3 (flag computation)                                 | tier                                        | S-3.3 flag resolved emit    |
  | S-5.0           | N/A (finalization)                                       | N/A                                         | PROPAGATION verified emit   |
  | S-5.1           | N/A (finalization)                                       | N/A                                         | manifest count emit         |
  | S-5.2           | N/A (finalization)                                       | N/A                                         | section ordering emit       |
  | S-5.3           | N/A (finalization)                                       | N/A                                         | header reconciliation emit  |
  | S-5.4           | N/A (finalization)                                       | N/A                                         | artifact written emit       |

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

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

HEADER BLOCK (first content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3.3}

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
  Before S-5.1, check each row of the verification check table below against actual entries.
  For each single-step field: confirm both string conditions; emit MATCH if both pass,
  MISMATCH if either fails. For topic: confirm Downstream-Action entry acknowledges
  multi-step scope explicitly; emit MULTI-STEP-ACKNOWLEDGED.

  Verification check table:

  | Field           | Expected CONSTRAINT string       | Expected Downstream-Action string                   |
  |-----------------|----------------------------------|-----------------------------------------------------|
  | topic           | N/A (multi-step scope)           | contains "no single sub-step anchor" or equivalent  |
  | tier-source     | contains "S-3.1 (carry)"         | contains "Consumed at S-3.1"                        |
  | compliance-tags | contains "S-3.2 (compliance      | contains "Consumed at S-3.2"                        |
  |                 |   detection)"                    |                                                     |
  | tier            | contains "S-3.3 (flag            | contains "Consumed at S-3.3"                        |
  |                 |   computation)"                  |                                                     |

  Emit: > PROPAGATION verified: topic [MULTI-STEP-ACKNOWLEDGED] | tier-source
           [MATCH | MISMATCH] | compliance-tags [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

  If any single-step field (tier-source, compliance-tags, tier) returns MISMATCH:
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

## V-05 -- Convergent: Lifecycle + Output Format x2 (All Three Axes Combined)

**Axis**: All three axes combined. V-01's halt-on-MISMATCH makes S-5.0 a hard gate.
V-02's formal verification check table specifies the exact match criteria for each field.
V-03's Scope column makes scope a first-class structural attribute in the PROPAGATION table.
The three axes interact: the Scope column classifies each row (single-step / multi-step);
the formal check table covers only single-step fields; the S-5.0 procedure is stated as a
rule against both (Scope=single-step rows checked via the formal table; Scope=multi-step
rows handled by the MULTI-STEP-ACKNOWLEDGED path); the halt gate fires only when a
single-step row in the formal table returns MISMATCH.
The topic row in the PROPAGATION table no longer needs a parenthetical in column 2 because
scope is carried in the dedicated Scope column -- column 2 carries only the exact field name
"topic", consistent with C-41's naming precision requirement applied without qualification.
**Hypothesis**: Full C-42/C-43/C-44 convergence. The maximal precision state for S-5.0 is:
(a) scope column drives verification type (C-44 -- table-driven rule), (b) formal check
table declares expected strings for single-step fields (C-43 -- specification separate from
procedure), (c) halt-on-MISMATCH enforces consistency before artifact writing (C-42 -- gate
not log). The V-05 axis demonstrates that all three are jointly satisfiable and that each
strengthens the others: scope column eliminates ambiguity about which rows get MATCH/MISMATCH;
formal table eliminates ambiguity about what MATCH means; halt gate eliminates ambiguity
about the consequence of MISMATCH.
**Predicts**: C-01 through C-41 pass | C-42 + C-43 + C-44 all probed. Tests whether new
excellence patterns emerge at the maximal S-5.0 precision state.
**Expected composite**: 41/41 aspirational baseline + C-42, C-43, C-44 candidate signals.

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
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names the exact Field value from the S-0 table
  whose Downstream-Action anchors to this sub-step -- must match S-0 table Field column
  exactly, no suffix or qualifier. Column 3 names the execution emit that fires at this
  sub-step. Column 4 (Scope) classifies each input-field row: single-step fields receive
  MATCH/MISMATCH verification at S-5.0; multi-step fields receive MULTI-STEP-ACKNOWLEDGED.
  The topic field is exempt from sub-step anchoring; its Scope=multi-step row is included
  to confirm exemption-by-design, not omission-by-oversight.

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

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit line
is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

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

HEADER BLOCK (first content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3.3}

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
