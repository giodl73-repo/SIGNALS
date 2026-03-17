---
skill: quest-variate
skill_target: mock-ns
round: 19
rubric_version: 15
date: 2026-03-16
---

# mock-ns -- Round 19 Variations

Rubric: v15 (C-01 through C-44, aspirational denominator 36).

New criteria in v15 (now pass conditions):
- **C-42** -- S-5.0 halt-on-MISMATCH gate: LIFECYCLE enumeration includes halt clause AND
  S-5.0 execution block includes conditional stop scoped to single-step fields only.
- **C-43** -- S-5.0 formal verification check table: expected strings declared in tabular
  structure with Field / Expected CONSTRAINT string / Expected Downstream-Action string columns;
  S-5.0 procedure references the table as the verification specification.
- **C-44** -- PROPAGATION table Scope column: dedicated fifth column classifying each row as
  single-step / multi-step / N/A; column values drive S-5.0 branching logic; topic row carries
  Scope=multi-step as a structural attribute, not a parenthetical in column 2.

R18 V-05 achieves full convergence on C-01 through C-44. R19 baseline: R18 V-05. All R19
variates inherit C-01 through C-44 and probe C-45+.

Three new excellence axes observed in R18 V-05's structural envelope:

1. **P-0 cross-reference protocol** (C-45 probe): In R18 V-05, the relationship between S-3's
   FLAG declaration and S-4's FLAG consumption is implicit: S-3.3 emits "FLAG resolved: {flag}"
   and S-4 uses "{flag from S-3.3}" in the header template. There is no structural token that
   binds the declaration site to the consumption site. Adding a P-0 step with a cross-reference
   table -- pairing token [S-3:CS] at the FLAG declaration with [S-4:FC] at the FLAG
   consumption -- makes the binding explicit, auditable, and navigable. A reader can verify the
   cross-site relationship by inspecting the table; an executor can confirm they are at the
   right step before processing a token row. Without P-0, the two-site FLAG contract exists
   only as a prose convention; with P-0, it is a named structural artifact.

2. **S-3 FLAG immutability chain** (C-46 probe): R18 V-05 states "FLAG is now resolved" as a
   single sentence after S-3.3. This sentence conveys intent but provides no structural
   protection layers. A FLAG immutability chain table -- with rows for Scope, Path classes,
   Affirmative closure, No-exemption, Failure consequence, and Guarantee-break -- makes each
   protection layer individually inspectable and names the failure mode of each violation. The
   table is not redundant with the single sentence: the sentence states the rule; the table
   states the rule's enforcement architecture. The distinction matters because a reader who
   understands only the sentence must infer the failure modes; a reader who sees the table
   knows them by name.

3. **S-4 header assembly FLAG copy prohibition** (C-47 probe): In R18 V-05, the HEADER BLOCK
   section of S-4 specifies "Flag: {flag from S-3.3}" as one of six header fields. The
   "{flag from S-3.3}" notation implies copy-not-rederive but does not prohibit rederivation.
   Adding an explicit FLAG prohibition rule as the first instruction of header assembly --
   "First rule: Copy FLAG from S-3.3 verbatim. Do not rederive it. This rule governs all
   header field population." -- closes the gap. The prohibition rule is load-bearing: it is
   the instruction that gives the "{flag from S-3.3}" notation its enforcement weight.

R19 isolates P-0 protocol (V-01), isolates S-3 immutability (V-02), isolates S-4 copy
prohibition (V-03), combines P-0 + S-3 immutability (V-04), and achieves full convergence
(V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (C-45 -- P-0 cross-reference protocol, minimal) | S-3 FLAG declaration and S-4 FLAG consumption are implicitly linked by prose convention only. A P-0 token table with [S-3:CS] and [S-4:FC] makes the cross-site binding explicit and auditable without requiring a full anti-bypass mechanism. Tests whether named structural tokens alone improve the FLAG contract. |
| V-02 | Output format (C-46 -- S-3 FLAG immutability chain table) | A single "FLAG is now resolved" sentence conveys intent but provides no protection-layer architecture. A six-row immutability chain table names each protection layer and its failure mode explicitly, making the enforcement architecture inspectable by row. Tests whether the table form adds structural precision beyond the sentence form. |
| V-03 | Phrasing register (C-47 -- S-4 header assembly FLAG copy prohibition) | "{flag from S-3.3}" implies copy-not-rederive but does not prohibit rederivation. An explicit first-rule prohibition -- "Copy FLAG from S-3.3 verbatim. Do not rederive it." -- as the opening instruction of header assembly closes the implicit-explicit gap. Tests whether the first-rule form is the load-bearing complement to the immutability declaration in S-3. |
| V-04 | Combined: Lifecycle + Output format (P-0 protocol + S-3 immutability) | V-01's P-0 token table + V-02's FLAG immutability chain. The cross-site tokens name the structural relationship; the immutability table enumerates the protection architecture at the declaration site. Tests whether C-45 and C-46 are jointly satisfiable and whether named tokens strengthen the immutability table (by naming the target of the cross-site reference row). |
| V-05 | Convergent: Lifecycle + Output format x2 + Phrasing (all three axes combined + anti-bypass) | Full structural convergence: P-0 with anti-bypass declaration and confirmation records + S-3 FLAG immutability chain with [S-3:CS] confirmation record + S-4 header assembly FLAG prohibition chain with [S-4:FC] confirmation record. The three axes interact: P-0 defines the tokens; S-3 immutability table carries [S-3:CS] to create the cross-site forward arc; S-4 prohibition chain carries [S-4:FC] to close the arc. Confirmation records at each token site enforce Phase 2 of the lookup protocol. |

---

## V-01 -- Lifecycle Emphasis: P-0 Cross-Reference Protocol (C-45 single axis)

**Axis**: Lifecycle emphasis -- a minimal P-0 cross-reference step is added before STEP S-0.
P-0 contains a token table pairing [S-3:CS] at S-3's FLAG declaration site with [S-4:FC] at
S-4's header assembly site. No anti-bypass mechanism. No confirmation records. The token table
makes the FLAG cross-site binding a named structural artifact rather than an implicit prose
convention. All other elements unchanged from R18 V-05.
**Hypothesis**: The FLAG contract between S-3 and S-4 is real but invisible. A minimal P-0
token table makes it navigable and auditable. A reader can verify the cross-site relationship
by token name; an executor knows before processing S-3.3 that it produces a value consumed at
[S-4:FC]. Without P-0, the binding is inferred from "{flag from S-3.3}" in the header template;
with P-0, it is declared.
**Predicts**: C-01 through C-44 pass (full R18 V-05 baseline) | C-45 probe (P-0 minimal
cross-reference). C-46, C-47 not targeted.
**Expected composite**: 36/36 aspirational baseline + C-45 candidate signal.

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
  P-0  Cross-reference protocol -- establish bracket tokens for this run
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

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Cross-site reference tokens for this run. Each token names its source step, its paired
target step, and the structural role of the row it marks.

  | Token    | Source step | Target step        | Row role                             |
  |----------|-------------|--------------------|--------------------------------------|
  | [S-3:CS] | S-3         | S-4 (header)       | Cross-site reference -- FLAG emitter |
  | [S-4:FC] | S-4 (header)| S-3                | Failure consequence -- FLAG consumer |

[S-3:CS] marks the row in S-3 that declares FLAG as complete and consumed downstream.
[S-4:FC] marks the row in S-4 header assembly that consumes FLAG from S-3.

Before processing any row marked with a bracket token: locate the token in the table
above. Confirm that the current step matches the Source step cell. Then process the row.

Do not re-establish this protocol in later steps.

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

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

  Cross-site ref [S-3:CS]: FLAG value emitted here is consumed at [S-4:FC] -- header
  assembly in S-4. Any modification to FLAG between this point and S-4 produces a
  category mismatch in the artifact's trust tier that is invisible to downstream tooling.

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

  Failure conseq [S-4:FC]: Copy FLAG from S-3.3 verbatim. Do not rederive it.
  [Mutual target of S-3:CS -- cross-site reference row in S-3]

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

---

## V-02 -- Output Format: S-3 FLAG Immutability Chain (C-46 single axis)

**Axis**: Output format -- a FLAG immutability chain table is added to S-3 after S-3.3's emit.
The table enumerates protection layers: Scope, Path classes, Affirmative closure,
No-exemption, Failure consequence, and Guarantee-break. No P-0 protocol. No S-4 prohibition.
All other elements unchanged from R18 V-05.
**Hypothesis**: "FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run."
conveys the rule but not the enforcement architecture. A six-row immutability chain table
makes each protection layer individually inspectable: a reader can verify not just that FLAG
is immutable but WHY and WHAT breaks if the rule is violated. The table form is to S-3 what
the verification check table (C-43) is to S-5.0 -- specification separated from procedure.
**Predicts**: C-01 through C-44 pass | C-46 probe (S-3 FLAG immutability chain table). C-45,
C-47 not targeted.
**Expected composite**: 36/36 aspirational baseline + C-46 candidate signal.

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

  | Protection layer    | Rule                                                                      |
  |---------------------|---------------------------------------------------------------------------|
  | Scope               | FLAG MUST NOT be recomputed anywhere in this run                          |
  | Path classes        | Not in any step, conditional branch, fallback path, or regeneration       |
  |                     | sequence -- no execution context is exempt                                |
  | Affirmative closure | Every execution path that reaches S-4 carries the FLAG value emitted here |
  | No-exemption        | No path is exempt from this closure requirement                           |
  | Failure consequence | Re-deriving FLAG at S-4 produces a category mismatch in the artifact's    |
  |                     | trust tier that is invisible to downstream tooling -- undetectable without |
  |                     | manual header inspection                                                   |
  | Guarantee-break     | This violation breaks the closure guarantee stated in Affirmative closure  |

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

---

## V-03 -- Phrasing Register: S-4 Header Assembly FLAG Copy Prohibition (C-47 single axis)

**Axis**: Phrasing register -- an explicit FLAG copy prohibition rule is added as the first
instruction of the HEADER BLOCK section in S-4. The rule states "First rule: Copy FLAG from
S-3.3 verbatim. Do not rederive it. This rule governs all header field population." The
"{flag from S-3.3}" notation in the header template is unchanged; the prohibition rule is
what gives it enforcement weight. No P-0 protocol. No S-3 immutability table. All other
elements unchanged from R18 V-05.
**Hypothesis**: "{flag from S-3.3}" is notation, not prohibition. A reader following the
notation copies the flag; an executor in a branch path might rederive it without contradiction.
The explicit first-rule prohibition closes this gap: it is not redundant with the notation --
it is the enforcement that the notation lacks. The first-rule form is the correct phrasing
because it establishes unconditional priority: no instruction in header assembly precedes it.
**Predicts**: C-01 through C-44 pass | C-47 probe (S-4 header assembly FLAG copy prohibition).
C-45, C-46 not targeted.
**Expected composite**: 36/36 aspirational baseline + C-47 candidate signal.

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

  First rule: Copy FLAG from S-3.3 verbatim. Do not rederive it.
  This rule governs all header field population. No instruction in header assembly
  precedes this rule. No path in header assembly is exempt.

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

---

## V-04 -- Combined: Lifecycle + Output Format (P-0 Protocol + S-3 Immutability Chain)

**Axis**: V-01's P-0 cross-reference token table combined with V-02's S-3 FLAG immutability
chain table. No S-4 copy prohibition. The P-0 token table establishes [S-3:CS] as the name
of the cross-site reference row at S-3, giving the immutability chain's failure-consequence
row a forward-arc target name. Together: P-0 declares the relationship exists; the
immutability chain enumerates why it matters and what breaks if violated.
**Hypothesis**: P-0 and the immutability chain are complementary: P-0 names the cross-site
target ([S-4:FC]) so a reader can navigate to the consumption site; the immutability chain
names the protection architecture so a reader can understand the enforcement. Each is useful
alone (V-01, V-02 above); together, the cross-site ref row in the immutability chain can
name [S-4:FC] by its token rather than by prose description, tightening the forward arc.
**Predicts**: C-01 through C-44 pass | C-45 + C-46 probed. C-47 not targeted.
**Expected composite**: 36/36 aspirational baseline + C-45, C-46 candidate signals.

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
  P-0  Cross-reference protocol -- establish bracket tokens for this run
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

STEP P-0 -- CROSS-REFERENCE PROTOCOL

Cross-site reference tokens for this run:

  | Token    | Source step | Target step        | Row role                             |
  |----------|-------------|--------------------|--------------------------------------|
  | [S-3:CS] | S-3         | S-4 (header)       | Cross-site reference -- FLAG emitter |
  | [S-4:FC] | S-4 (header)| S-3                | Failure consequence -- FLAG consumer |

[S-3:CS] marks the FLAG immutability declaration in S-3 as the cross-site reference source.
[S-4:FC] marks the header assembly in S-4 as the cross-site failure consequence target.

Before processing any row marked with a bracket token: locate the token in the table
above. Confirm that the current step matches the Source step cell. Then process the row.

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

  | Protection layer    | Rule                                                                      |
  |---------------------|---------------------------------------------------------------------------|
  | Scope               | FLAG MUST NOT be recomputed anywhere in this run                          |
  | Path classes        | Not in any step, conditional branch, fallback path, or regeneration       |
  |                     | sequence -- no execution context is exempt                                |
  | Affirmative closure | Every execution path that reaches S-4 carries the FLAG value emitted here |
  | No-exemption        | No path is exempt from this closure requirement                           |
  | Failure consequence | Re-deriving FLAG at [S-4:FC] produces a category mismatch in the          |
  |                     | artifact's trust tier invisible to downstream tooling                     |
  | Guarantee-break     | This violation breaks the closure guarantee stated in Affirmative closure  |
  | Cross-site ref      | [S-3:CS]: FLAG emitter (this step) -- paired with [S-4:FC] header         |
  | [S-3:CS]            | assembly; locate token in P-0 table to confirm step before writing        |

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

  Failure conseq [S-4:FC]: Copy FLAG from S-3.3 verbatim. Do not rederive it.
  [Mutual target of S-3:CS -- cross-site reference row in S-3 immutability chain]

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

---

## V-05 -- Convergent: Lifecycle + Output Format x2 + Phrasing (All Three Axes + Anti-Bypass)

**Axis**: Full structural convergence. P-0 with anti-bypass declaration (named heading
"Anti-bypass declaration (ABD):"), forward navigation pointer naming S-3 and S-4, and
two-phase lookup protocol with confirmation records. S-3 FLAG immutability chain with
[S-3:CS] confirmation record (Phase 2 required before writing the cross-site reference row).
S-4 header assembly FLAG prohibition chain with [S-4:FC] confirmation record (Phase 2
required before writing the failure consequence row). The three axes interact: P-0 defines
the ABD and the token table; S-3 immutability chain carries [S-3:CS] as a load-bearing
cross-site reference that names [S-4:FC] as its target; S-4 prohibition chain carries
[S-4:FC] as the mutual target that closes the arc. Confirmation records at both sites
enforce Phase 2 -- an executor who processes a token row without confirming step identity
violates the ABD.
**Hypothesis**: The maximal precision state for the FLAG cross-site contract is: (a) P-0
establishes named tokens with forward navigation and anti-bypass enforcement (C-45 + ABD
subaxis); (b) S-3 immutability chain uses a token to name its downstream target, and
requires Phase 2 confirmation before the cross-site reference row is written (C-46 + C-45);
(c) S-4 prohibition chain uses a token to name its origin and requires Phase 2 confirmation
before the failure consequence row is written (C-47 + C-45). The confirmation record
mechanism closes the bypass gap at both token sites: the ABD says locate-only is a failure;
the confirmation record proves Phase 2 was performed. V-05 demonstrates that C-45, C-46,
and C-47 are jointly satisfiable and that the anti-bypass mechanism strengthens all three
by adding verification at each token site.
**Predicts**: C-01 through C-44 pass | C-45 + C-46 + C-47 all probed. Tests whether new
excellence patterns emerge at the maximal cross-site contract precision state.
**Expected composite**: 36/36 aspirational baseline + C-45, C-46, C-47 candidate signals.

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
  | No-exemption            | No path is exempt                                                    |
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
  | Anti-bypass echo        | Per P-0, ABD: processing this row without reading the Step and Row   |
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

  | Protection layer        | Rule                                                                 |
  |-------------------------|----------------------------------------------------------------------|
  | First rule              | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority                | This rule is first in this step -- it applies before any other       |
  |                         | instruction                                                          |
  | Anti-displacement       | Before any field is listed, before any category lookup, before any   |
  |                         | formatting instruction, or any other instruction in this step        |
  | All-governed            | Every instruction in this step is governed by this rule              |
  | No-exemption            | No instruction in this step is exempt                                |
  | CONFIRMATION REQUIRED   | Phase 1: locate [S-4:FC] in P-0 table, row 2. Phase 2 (Steps       |
  | before writing this row | 2a-2d): read Step=S-4 (header) + Row type=Failure consequence row;  |
  | (P-0 table, row 2)      | assert match; emit confirmation record from pre-filled table below   |
  |                         | (Step 2d). DO NOT WRITE THE ROW until Steps 2a-2d are complete      |
  |                         | and the record is emitted.                                           |
  | Anti-bypass echo        | Per P-0, ABD: processing this row without reading the Step and Row   |
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

## Relationship among C-45, C-46, and C-47

C-45, C-46, and C-47 are the FLAG cross-site contract precision class, building on the
immutability foundation implied by C-42 through C-44.

Each criterion tightens a different dimension:
- **C-45** adds navigability -- the cross-site binding is a named token, not a prose
  convention; a reader can locate the declaration and consumption sites by token name.
- **C-46** adds enforcement architecture -- the protection layers at the declaration site
  are individually inspectable; each failure mode has a name.
- **C-47** adds consumption-site closure -- the prohibition at the consumption site is
  the first-priority rule, not an implied consequence of the notation.

The axes are independent at the criterion level:
- V-01 (C-45 only): tokens navigable but no immutability table, no consumption prohibition.
- V-02 (C-46 only): protection layers inspectable but no named tokens, no prohibition.
- V-03 (C-47 only): consumption-site rule explicit but no tokens, no architecture table.
- V-04 (C-45 + C-46): tokens name the arc and the table enumerates architecture; the
  cross-site ref row in the table can name [S-4:FC] -- the token gives the architecture
  table a precise forward target.
- V-05 (all three + ABD): maximal state. The Scope-column pattern from C-44 parallels the
  table-driven architecture here: just as C-44 made scope a first-class structural attribute
  driving S-5.0 logic, C-45 + C-46 + C-47 make the FLAG cross-site contract a first-class
  structural artifact driving S-3 and S-4 behavior. The anti-bypass confirmation records
  close the execution gap: declaring the protocol (C-45) without verifying it was followed
  at each token site leaves the same observational-only gap that C-42 closed for S-5.0.
