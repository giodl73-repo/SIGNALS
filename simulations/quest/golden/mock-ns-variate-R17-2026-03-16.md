---
skill: quest-variate
skill_target: mock-ns
round: 17
rubric_version: 13
date: 2026-03-16
---

# mock-ns -- Round 17 Variations

Rubric: v13 (C-01 through C-38, aspirational denominator 30).

New criteria in v13 (now pass conditions):
- **C-37** -- Sub-step propagation manifest at LIFECYCLE level: a PROPAGATION section is
  present at the LIFECYCLE level that (a) maps each C-33 sub-step identifier (at minimum
  S-3.1, S-3.2, S-3.3) to its structural target locations, and (b) is accurate -- every
  declared binding is reflected in the actual CONSTRAINT block text and Downstream-Action
  column entries. A PROPAGATION table whose bindings are inconsistent with actual entries
  fails C-37 even when the table structure is formally present.
- **C-38** -- "Consumed at" consumption-event verb form in Downstream-Action column: every
  Downstream-Action entry for a field with a single sub-step consumption point uses a
  consumption-event verb ("Consumed at," "Used at," "Applied at," "Evaluated at") as the
  primary verb phrase. Transport verbs ("Carried to," "Forwarded to," "Passed to") fail
  C-38. The multi-step exempt field (topic) is exempt when its entry explicitly
  acknowledges the multi-step scope ("Consumed across all steps; no single sub-step anchor").

R16's best performer (V-05) introduced: ID-primary CONSTRAINT (C-35), "Consumed at" verb
form in Downstream-Action (C-36/C-38), PROPAGATION table with accurate bindings (C-37),
plus the column-definition guarantee from R15-V-05. R16 V-05 achieves full convergence on
all 38 criteria.

R17 baseline: R16 V-05. All R17 variates inherit C-01 through C-38 and probe C-39+.

Three new axes identified in R16 V-05's PROPAGATION section:

1. **PROPAGATION lifecycle closure** (C-39 probe): The PROPAGATION table declares bindings
   but is never verified against actual entries within the run. C-26 verifies header fields
   at S-5.3; C-27 verifies section count at S-5.1. The PROPAGATION table has no analogous
   close-out. A PROPAGATION verification emit at S-5 entry -- comparing declared PROPAGATION
   bindings against actual CONSTRAINT block text and Downstream-Action entries -- would make
   C-37 accuracy observable as a runtime assertion, not just a structural claim. Candidate:
   new S-5.0 sub-step before COUNT.

2. **PROPAGATION table completeness: multi-step exempt field coverage** (C-40 probe): The
   PROPAGATION table covers the three sub-step-anchored fields (tier, compliance-tags,
   tier-source). The multi-step exempt field (topic) has no PROPAGATION row. The C-38
   exemption for topic is acknowledged in the Downstream-Action column ("no single sub-step
   anchor") but is not reflected in the PROPAGATION table -- making the table an incomplete
   manifest of all input fields. A dedicated topic row with a "multi-step scope" annotation
   would make the table cover all four input fields and distinguish exemption-by-design
   from omission-by-oversight.

3. **PROPAGATION entry naming precision: exact field names** (C-41 probe): The PROPAGATION
   table "Table Downstream-Action field" column currently uses descriptive names ("tier row",
   "compliance-tags row", "tier-source row") rather than the exact field names from the S-0
   table ("tier", "compliance-tags", "tier-source"). Exact field names make the cross-
   reference unambiguous and enable mechanical verification without name-matching heuristics.
   The descriptor "row" adds no information and introduces a naming variant.

R17 isolates PROPAGATION lifecycle closure (V-01), isolates multi-step exempt field
coverage (V-02), isolates exact field names (V-03), combines lifecycle + naming (V-04),
and achieves full convergence (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (C-39 -- PROPAGATION verification gate at S-5.0) | Adding S-5.0 as a PROPAGATION verification sub-step before S-5.1 COUNT closes the C-37 lifecycle by making the declared table bindings observable as a runtime accuracy assertion rather than a structural claim. This mirrors the C-26 header reconciliation and C-27 section count patterns at the same S-5 phase. A PROPAGATION table whose accuracy is verified at S-5.0 is structurally identical to an unverified one but auditably closed. |
| V-02 | Output format (C-40 -- topic row in PROPAGATION table with multi-step scope annotation) | Omitting the topic field from the PROPAGATION table makes the table an incomplete manifest of input fields. Adding an explicit topic row with "multi-step scope (no sub-step anchor)" annotation distinguishes exemption-by-design from omission-by-oversight, and makes the table a complete four-field manifest matching the four-field S-0 input table. The PROPAGATION table covering all input fields achieves field-count parity with the S-0 table. |
| V-03 | Phrasing register (C-41 -- exact field names in PROPAGATION table) | Using exact field names ("tier-source", "compliance-tags", "tier") rather than descriptive names ("tier-source row", "compliance-tags row", "tier row") in the PROPAGATION table's "Table Downstream-Action field" column makes each declared binding unambiguous and mechanically verifiable against the S-0 table's Field column. Descriptive names introduce a naming variant that requires human matching; exact names allow direct column comparison. |
| V-04 | Combined: Lifecycle + Phrasing (PROPAGATION verification gate + exact field names) | V-01's S-5.0 PROPAGATION verification gate + V-03's exact field names together, without the topic-row addition. Tests whether C-39 and C-41 are structurally independent and can be satisfied simultaneously. The verification emit at S-5.0 names fields by exact field name, making the verification assertion consistent with the PROPAGATION table's naming precision. |
| V-05 | Convergent: Lifecycle + Output format + Phrasing (all three axes combined) | Full structural convergence: V-01 S-5.0 PROPAGATION verification + V-02 topic row with multi-step scope + V-03 exact field names. The S-5.0 verification handles the topic row by emitting a MULTI-STEP-ACKNOWLEDGED annotation for it (no MATCH/MISMATCH possible for a multi-step scope field). All four input fields covered in PROPAGATION table; all bindings use exact names; lifecycle closure present at S-5.0. |

---

## V-01 -- Lifecycle Emphasis: PROPAGATION Verification Gate at S-5.0 (C-39 single axis)

**Axis**: Lifecycle emphasis -- a new S-5.0 PROPAGATION VERIFICATION sub-step is added at
the start of S-5 finalization, before the existing S-5.1 COUNT sub-step. The S-5.0 emit
cross-checks each PROPAGATION table binding against the actual CONSTRAINT block text and
Downstream-Action column entries, producing a per-binding MATCH or MISMATCH verdict. The
PROPAGATION table content and all other elements are unchanged from R16 V-05.
**Hypothesis**: C-37 requires PROPAGATION accuracy but does not make accuracy observable
as a runtime event -- it is a structural claim verifiable only by cross-section inspection.
S-5.0 introduces a PROPAGATION close-out that mirrors C-26 (header reconciliation) and
C-27 (manifest count verification) at the same finalization phase, making C-37 accuracy
observable as a dedicated emit. A PROPAGATION table with a corresponding S-5.0 close-out
achieves full lifecycle closure: declared at the LIFECYCLE level, executed across S-3 and
S-0, verified at S-5.0 entry.
**Predicts**: C-01 through C-38 pass (full R16 V-05 baseline) | C-39 probe (S-5.0
PROPAGATION verification emit introduces a lifecycle close-out not present in R16 V-05).
**Expected composite**: 38/38 aspirational baseline + C-39 candidate signal.

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
  role as parenthetical gloss. Column 2 names which S-0 table Downstream-Action field
  anchors to this sub-step. Column 3 names the execution emit that fires at this sub-step.

  | Sub-step | CONSTRAINT reference (ID-primary) | Table Downstream-Action field | Execution emit              |
  |----------|------------------------------------|-------------------------------|-----------------------------|
  | S-3.1    | S-3.1 (carry)                      | tier-source row               | S-3.1 carry emit            |
  | S-3.2    | S-3.2 (compliance detection)       | compliance-tags row           | S-3.2 compliance check emit |
  | S-3.3    | S-3.3 (flag computation)           | tier row                      | S-3.3 flag resolved emit    |
  | S-5.0    | N/A (finalization)                 | N/A                           | PROPAGATION verified emit   |
  | S-5.1    | N/A (finalization)                 | N/A                           | manifest count emit         |
  | S-5.2    | N/A (finalization)                 | N/A                           | section ordering emit       |
  | S-5.3    | N/A (finalization)                 | N/A                           | header reconciliation emit  |
  | S-5.4    | N/A (finalization)                 | N/A                           | artifact written emit       |

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
  Before S-5.1, verify each PROPAGATION table binding against actual entries:
    - For S-3.1: confirm CONSTRAINT block contains "S-3.1 (carry)" AND tier-source
      Downstream-Action entry contains "Consumed at S-3.1"
    - For S-3.2: confirm CONSTRAINT block contains "S-3.2 (compliance detection)" AND
      compliance-tags Downstream-Action entry contains "Consumed at S-3.2"
    - For S-3.3: confirm CONSTRAINT block contains "S-3.3 (flag computation)" AND
      tier Downstream-Action entry contains "Consumed at S-3.3"

  Emit: > PROPAGATION verified: S-3.1 [MATCH | MISMATCH] | S-3.2 [MATCH | MISMATCH] |
           S-3.3 [MATCH | MISMATCH]

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

## V-02 -- Output Format: Topic Row in PROPAGATION Table (C-40 single axis)

**Axis**: Output format -- the PROPAGATION table gains an explicit row for the topic field,
annotated as "multi-step scope (no sub-step anchor)." The table now covers all four S-0
input fields (topic, tier, compliance-tags, tier-source) rather than only the three
sub-step-anchored fields. The topic row's CONSTRAINT and Downstream-Action entries are
annotated as "N/A (multi-step scope)" and "all steps (no single sub-step anchor)"
respectively. No S-5.0 verification sub-step is added (single-axis isolation).
**Hypothesis**: The PROPAGATION table omitting topic is an incomplete manifest: it covers
three of four input fields. The topic row represents a design decision (multi-step scope
exemption) that should be explicit in the PROPAGATION table rather than implied by
absence. An explicit "multi-step scope" annotation in the PROPAGATION table distinguishes
intentional exemption from oversight, and makes the table a complete four-field manifest
with field-count parity to the S-0 input table. A complete PROPAGATION table leaves no
input field unaccounted for at the LIFECYCLE declaration level.
**Predicts**: C-01 through C-38 pass (full R16 V-05 baseline) | C-40 probe (topic row in
PROPAGATION table introduces complete four-field coverage not present in R16 V-05).
**Expected composite**: 38/38 aspirational baseline + C-40 candidate signal.

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
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line
       Note: S-5.1 through S-5.4 execute in sequence. No S-5 sub-step may begin
       before the preceding sub-step's emit is written.

SUB-STEP LABEL PROPAGATION:
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names which S-0 table Downstream-Action field
  anchors to this sub-step. Column 3 names the execution emit that fires at this sub-step.
  The topic field has multi-step scope and is exempt from sub-step anchoring: its row is
  included below to confirm exemption-by-design, not omission-by-oversight.

  | Sub-step        | CONSTRAINT reference (ID-primary)                        | Table Downstream-Action field               | Execution emit              |
  |-----------------|----------------------------------------------------------|---------------------------------------------|-----------------------------|
  | topic (exempt)  | N/A -- multi-step scope; no CONSTRAINT reference         | topic row (multi-step; no sub-step anchor)  | N/A -- used throughout      |
  | S-3.1           | S-3.1 (carry)                                            | tier-source row                             | S-3.1 carry emit            |
  | S-3.2           | S-3.2 (compliance detection)                             | compliance-tags row                         | S-3.2 compliance check emit |
  | S-3.3           | S-3.3 (flag computation)                                 | tier row                                    | S-3.3 flag resolved emit    |
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

## V-03 -- Phrasing Register: Exact Field Names in PROPAGATION Table (C-41 single axis)

**Axis**: Phrasing register -- the PROPAGATION table's "Table Downstream-Action field"
column uses exact field names from the S-0 table ("tier-source", "compliance-tags", "tier")
rather than descriptive names with "row" suffix ("tier-source row", "compliance-tags row",
"tier row"). No topic row added; no S-5.0 verification sub-step. All other elements
unchanged from R16 V-05.
**Hypothesis**: The "row" suffix in PROPAGATION table column 2 entries is a naming variant
that introduces a gap between the PROPAGATION declaration and the S-0 table's Field
column values. A reader cross-referencing "tier-source row" against the S-0 table must
perform a name-matching step ("tier-source row" = the row whose Field is "tier-source").
Using the exact field name ("tier-source") creates a direct column-value reference,
enabling mechanical verification: the PROPAGATION table column 2 value must equal the
S-0 table Field column value exactly. This is the same naming precision that C-35 requires
for CONSTRAINT block references -- every structural reference to a defined entity uses
the entity's canonical name, not a descriptive variant.
**Predicts**: C-01 through C-38 pass (full R16 V-05 baseline) | C-41 probe (exact field
names in PROPAGATION table column 2, enabling mechanical cross-reference to S-0 table).
**Expected composite**: 38/38 aspirational baseline + C-41 candidate signal.

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
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line
       Note: S-5.1 through S-5.4 execute in sequence. No S-5 sub-step may begin
       before the preceding sub-step's emit is written.

SUB-STEP LABEL PROPAGATION:
  The C-33 sub-step identifiers below are active at three structural locations. Column 1
  names the sub-step as it must appear in the S-0 CONSTRAINT block -- ID-primary, prose
  role as parenthetical gloss. Column 2 names the exact Field value from the S-0 table
  whose Downstream-Action anchors to this sub-step -- this value must match the S-0 table
  Field column exactly. Column 3 names the execution emit that fires at this sub-step.

  | Sub-step | CONSTRAINT reference (ID-primary) | S-0 table Field (exact match) | Execution emit              |
  |----------|------------------------------------|-------------------------------|-----------------------------|
  | S-3.1    | S-3.1 (carry)                      | tier-source                   | S-3.1 carry emit            |
  | S-3.2    | S-3.2 (compliance detection)       | compliance-tags               | S-3.2 compliance check emit |
  | S-3.3    | S-3.3 (flag computation)           | tier                          | S-3.3 flag resolved emit    |
  | S-5.1    | N/A (finalization)                 | N/A                           | manifest count emit         |
  | S-5.2    | N/A (finalization)                 | N/A                           | section ordering emit       |
  | S-5.3    | N/A (finalization)                 | N/A                           | header reconciliation emit  |
  | S-5.4    | N/A (finalization)                 | N/A                           | artifact written emit       |

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

## V-04 -- Combined: Lifecycle + Phrasing (PROPAGATION Verification Gate + Exact Field Names)

**Axis**: Combined V-01 (lifecycle emphasis: S-5.0 PROPAGATION verification sub-step) and
V-03 (phrasing register: exact field names in PROPAGATION table column 2). No topic row
added (single-axis purity on C-40 preserved). The S-5.0 verification emit uses exact field
names in its MATCH/MISMATCH assertions, achieving naming consistency across the PROPAGATION
table and its close-out emit.
**Hypothesis**: C-39 (PROPAGATION lifecycle closure) and C-41 (exact field name precision)
are structurally independent. V-01 adds runtime observability to C-37 accuracy; V-03 adds
naming precision to C-37's structural declaration. Together they address both the audit
chain (C-39) and the cross-reference precision (C-41) dimensions of the PROPAGATION
section without introducing the topic-row coverage question (C-40). The S-5.0 emit
names fields by their exact S-0 table Field values ("tier-source", "compliance-tags",
"tier") rather than by sub-step label alone, making the verification assertion itself a
cross-reference demonstration: S-5.0 emits "tier-source: MATCH" not "S-3.1 field: MATCH".
**Predicts**: C-01 through C-38 pass | C-39 + C-41 probes satisfied | C-40 not targeted.
**Expected composite**: 38/38 aspirational baseline + C-39 and C-41 candidate signals.

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
  whose Downstream-Action anchors to this sub-step -- this value must match the S-0 table
  Field column exactly. Column 3 names the execution emit that fires at this sub-step.

  | Sub-step | CONSTRAINT reference (ID-primary) | S-0 table Field (exact match) | Execution emit              |
  |----------|------------------------------------|-------------------------------|-----------------------------|
  | S-3.1    | S-3.1 (carry)                      | tier-source                   | S-3.1 carry emit            |
  | S-3.2    | S-3.2 (compliance detection)       | compliance-tags               | S-3.2 compliance check emit |
  | S-3.3    | S-3.3 (flag computation)           | tier                          | S-3.3 flag resolved emit    |
  | S-5.0    | N/A (finalization)                 | N/A                           | PROPAGATION verified emit   |
  | S-5.1    | N/A (finalization)                 | N/A                           | manifest count emit         |
  | S-5.2    | N/A (finalization)                 | N/A                           | section ordering emit       |
  | S-5.3    | N/A (finalization)                 | N/A                           | header reconciliation emit  |
  | S-5.4    | N/A (finalization)                 | N/A                           | artifact written emit       |

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
  field names from the S-0 table Field column in the verification emit:
    - For tier-source (S-3.1): confirm CONSTRAINT block contains "S-3.1 (carry)" AND
      tier-source Downstream-Action entry contains "Consumed at S-3.1"
    - For compliance-tags (S-3.2): confirm CONSTRAINT block contains "S-3.2 (compliance
      detection)" AND compliance-tags Downstream-Action entry contains "Consumed at S-3.2"
    - For tier (S-3.3): confirm CONSTRAINT block contains "S-3.3 (flag computation)" AND
      tier Downstream-Action entry contains "Consumed at S-3.3"

  Emit: > PROPAGATION verified: tier-source [MATCH | MISMATCH] | compliance-tags
           [MATCH | MISMATCH] | tier [MATCH | MISMATCH]

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

## V-05 -- Convergent: Lifecycle + Output Format + Phrasing (All Three Axes Combined)

**Axis**: All three axes combined. V-01's S-5.0 PROPAGATION verification gate closes the
C-37 lifecycle. V-02's topic row in the PROPAGATION table makes the table a complete four-
field manifest. V-03's exact field names in PROPAGATION column 2 enable mechanical cross-
reference. The S-5.0 verification handles topic by emitting MULTI-STEP-ACKNOWLEDGED (no
MATCH/MISMATCH check is meaningful for a field with no sub-step anchor). The S-5.0 emit
covers all four input fields: three with MATCH/MISMATCH + one with MULTI-STEP-ACKNOWLEDGED.
**Hypothesis**: Full C-39/C-40/C-41 convergence. The PROPAGATION table is complete (all
four input fields; topic row present), named precisely (exact field names), and lifecycle-
closed (S-5.0 verifies each binding including the topic exemption). The PROPAGATION section
at the LIFECYCLE level becomes a self-contained structural manifest: complete field coverage,
exact naming, and a close-out that makes its accuracy claims observable as runtime events.
The maximal precision state for a PROPAGATION section is: (a) all consuming fields covered
(C-40), (b) column 2 uses exact field names (C-41), (c) S-5.0 verifies each binding with a
field-named emit (C-39), (d) the topic row acknowledges multi-step scope explicitly rather
than being absent (C-40), and (e) all four input fields are accounted for in the S-5.0 emit.
**Predicts**: C-01 through C-38 pass | C-39 + C-40 + C-41 all probed. Tests whether the
three new axes are jointly satisfiable and whether any new excellence pattern emerges at
the maximal precision state.
**Expected composite**: 38/38 aspirational baseline + C-39, C-40, C-41 candidate signals.

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
