---
skill: quest-variate
skill_target: mock-ns
round: 16
rubric_version: 12
date: 2026-03-16
---

# mock-ns -- Round 16 Variations

Rubric: v12 (C-01 through C-36, aspirational denominator 28).

New criteria in v12 (now pass conditions):
- **C-35** -- Sub-step label reference constraint language: every blocked-step reference
  in the S-0 CONSTRAINT block uses the C-33 sub-step identifier as syntactic primary,
  with any prose role name appearing only as a subsequent gloss. "S-3.1 (carry)" passes;
  "carry (S-3.1)" fails; "flag computation (S-3)" fails even if C-33 is satisfied.
- **C-36** -- Sub-step identifier precision in C-34 table Downstream-Action column:
  every Downstream-Action entry identifies its consumption point by C-33 sub-step
  identifier. Step-level references ("carried to S-3") fail C-36 even when C-34 and
  C-15 are satisfied. Requires C-33 and C-34 as preconditions.

R15's best performer (V-05) introduced C-33 sub-step labels + C-34 three-column table +
column-definition guarantee. Two C-35/C-36 gaps survive into R16:

Gap 1 (C-35): V-04/V-05 CONSTRAINT has a prose-primary second sentence:
  "Primary operations select (S-1), lookup (S-2), and flag (S-3.3) are all blocked..."
  -- the prose roles ("select", "lookup", "flag") are syntactic primary; step labels
  are parenthetical. This inverts the C-35 requirement.

Gap 2 (C-36): The `topic` row Downstream-Action reads "Subject for all steps; used in
  artifact path, header, and body" -- no sub-step anchor named. The three remaining rows
  already reference sub-steps (S-3.1, S-3.2, S-3.3) but use the verb "carried to" rather
  than "consumed at", leaving the precision implicit rather than explicit.

R16 isolates C-35 fix (V-01), isolates C-36 upgrade (V-02), isolates propagation
declaration (V-03), combines C-35+C-36 (V-04), and achieves full convergence (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (C-35 -- single-sentence ID-primary CONSTRAINT) | Removing the prose-primary second sentence from V-04/V-05's CONSTRAINT block closes C-35 by ensuring every blocked-step reference uses sub-step ID as syntactic primary throughout. A single imperative sentence with ID-first references suffices; no second sentence is needed to restate the block. |
| V-02 | Output format (C-36 -- explicit "consumed at S-X.X" downstream anchors) | Upgrading every Downstream-Action entry to use the "consumed at S-X.X" verb form -- including a `topic` entry that explicitly names its multi-step consumption scope -- closes C-36 by making the sub-step consumption point present by verb in every row, not by implication from the sub-step number alone. |
| V-03 | Lifecycle emphasis (explicit SUB-STEP LABEL PROPAGATION declaration) | Appending a PROPAGATION table to the LIFECYCLE block maps each sub-step label to its three structural target locations (CONSTRAINT reference, table Downstream-Action field, execution emit), making C-35 and C-36 satisfaction checkable at the declaration point without reading the full spec body. |
| V-04 | Combined: C-35 + C-36 (phrasing register + output format) | V-01's single-sentence ID-primary CONSTRAINT + V-02's "consumed at S-X.X" Downstream-Action table together, without a propagation declaration overhead. Tests whether the two structural fixes are sufficient without a mapping declaration. |
| V-05 | Convergent: C-35 + C-36 + propagation declaration + column-definition guarantee | Full structural convergence: V-01 CONSTRAINT + V-02 Downstream-Action + V-03 PROPAGATION declaration + R15-V-05 column-definition compliance guarantee. All 36 criteria targeted by structure rather than by per-entry prose crafting. |

---

## V-01 -- Phrasing Register: Single-Sentence ID-Primary CONSTRAINT (C-35 single axis)

**Axis**: Phrasing register -- the S-0 CONSTRAINT block is reduced to a single imperative
sentence in which every blocked-step reference uses the C-33 sub-step identifier as
syntactic primary, with any prose role appearing as a parenthetical gloss on the label.
The prose-primary second sentence from V-04/V-05 ("Primary operations select (S-1)...
are all blocked") is eliminated.
**Hypothesis**: C-35 requires every constraint reference to use sub-step ID as primary
anchor. V-04/V-05's second sentence inverts this for S-1, S-2, and S-3.3. Removing it
leaves a single sentence that is uniformly ID-primary. C-35 passes cleanly. C-34
column-definition guarantee is retained from R15-V-05. C-36 is not targeted -- topic
row Downstream-Action remains without explicit sub-step anchor; other rows retain the
"Carried to S-X.X" form rather than "Consumed at S-X.X".
**Predicts**: C-01 through C-34 | C-35 pass | C-36 miss (topic row unanchored).
**Expected composite**: 35/36 aspirational.

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

  | Field           | Resolution                                                                    | Downstream-Action                                                           |
  |-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Subject for all steps; used in artifact path, header, and body              |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Carried to S-3.3 for tier-conditional flag refinement                       |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Carried to S-3.2; triggers COMPLIANCE-OVERRIDE path if tag present          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Included in S-0 emit; re-emitted in S-3.1 carry record                      |

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

## V-02 -- Output Format: Explicit "Consumed at S-X.X" Downstream Anchors (C-36 single axis)

**Axis**: Output format -- every Downstream-Action column entry in the S-0 table uses an
explicit "consumed at S-X.X" or "consumed across..." verb form. The `topic` row is
upgraded to acknowledge its multi-step consumption scope explicitly. The three rows that
already had sub-step references are upgraded from "Carried to S-X.X" (implicit anchor)
to "Consumed at S-X.X" (explicit verb). CONSTRAINT block retains the V-05 prose-primary
second sentence -- C-35 miss is intentional for single-axis isolation.
**Hypothesis**: C-36 requires the Downstream-Action column to identify each field's
consumption point by C-33 sub-step identifier. The V-05 form passes for tier,
compliance-tags, and tier-source by implication. The topic row has no sub-step anchor.
Upgrading to "consumed at S-X.X" makes the anchor explicit by verb, closes the gap for
topic, and strengthens precision for the other three fields.
**Predicts**: C-01 through C-34 | C-35 miss | C-36 pass.
**Expected composite**: 35/36 aspirational.

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

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance), or S-3.3 (flag) until this step's emit line is written to the
conversation. Primary operations select (S-1), lookup (S-2), and flag (S-3.3) are all
blocked until S-0 completes.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

  | Field           | Resolution                                                                    | Downstream-Action                                                                       |
  |-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                  |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins         |

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

## V-03 -- Lifecycle Emphasis: Explicit Sub-Step Label Propagation Declaration (single axis)

**Axis**: Lifecycle emphasis -- a SUB-STEP LABEL PROPAGATION table is appended to the
LIFECYCLE block, mapping each C-33 sub-step identifier to its three structural target
locations: (1) how it appears in the S-0 CONSTRAINT block, (2) which S-0 table row's
Downstream-Action field anchors to it, (3) which execution emit fires at it. CONSTRAINT
block and table Downstream-Action are unchanged from R15-V-05 (single-axis isolation:
C-35 miss, C-36 partial intentional).
**Hypothesis**: The PROPAGATION table is a readability and awareness mechanism, not a
compliance mechanism. It makes the C-33->C-35->C-36 propagation chain checkable at
declaration time. It does not itself close C-35 (CONSTRAINT is unchanged) or C-36 (topic
row unanchored). Its structural value is in making the gap visible -- an executor who
reads the PROPAGATION table and then reads the CONSTRAINT block will observe the
mismatch between column 1 ("CONSTRAINT reference (ID-primary)") and the actual second
sentence's prose-primary form.
**Predicts**: C-01 through C-34 | C-35 miss | C-36 partial (three rows have sub-step
refs, topic row still unanchored).
**Expected composite**: 34/36 aspirational.

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
  Each C-33 sub-step identifier below is active at three structural locations. Column 1
  shows how the sub-step must appear in the S-0 CONSTRAINT block (ID-primary form).
  Column 2 shows which S-0 table Downstream-Action field anchors to this sub-step.
  Column 3 shows which execution emit fires at this sub-step.

  | Sub-step | CONSTRAINT reference (ID-primary) | Table Downstream-Action field | Execution emit              |
  |----------|-----------------------------------|-------------------------------|-----------------------------|
  | S-3.1    | S-3.1 (carry)                     | tier-source row               | S-3.1 carry emit            |
  | S-3.2    | S-3.2 (compliance detection)      | compliance-tags row           | S-3.2 compliance check emit |
  | S-3.3    | S-3.3 (flag computation)          | tier row                      | S-3.3 flag resolved emit    |
  | S-5.1    | N/A (finalization)                | N/A                           | manifest count emit         |
  | S-5.2    | N/A (finalization)                | N/A                           | section ordering emit       |
  | S-5.3    | N/A (finalization)                | N/A                           | header reconciliation emit  |
  | S-5.4    | N/A (finalization)                | N/A                           | artifact written emit       |

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance), or S-3.3 (flag) until this step's emit line is written to the
conversation. Primary operations select (S-1), lookup (S-2), and flag (S-3.3) are all
blocked until S-0 completes.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

The three column definitions below enforce field name, resolution method, and downstream
action for every row by structure. A row is complete if and only if all three columns are
populated. This table satisfies the self-contained entry requirement for all four fields
without per-entry inspection.

  | Field           | Resolution                                                                    | Downstream-Action                                                           |
  |-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Subject for all steps; used in artifact path, header, and body              |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Carried to S-3.3 for tier-conditional flag refinement                       |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Carried to S-3.2; triggers COMPLIANCE-OVERRIDE path if tag present          |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Included in S-0 emit; re-emitted in S-3.1 carry record                      |

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

## V-04 -- Combined: C-35 + C-36 (Phrasing Register + Output Format)

**Axis**: Combined V-01 (phrasing register) and V-02 (output format). CONSTRAINT block
uses a single ID-primary sentence with no prose-primary reversal. Downstream-Action
column uses "consumed at S-X.X" verb form for all four entries, with `topic` explicitly
annotated as multi-step with no single sub-step anchor. PROPAGATION declaration absent
(tests whether the two structural fixes suffice without declaration overhead).
**Hypothesis**: C-35 and C-36 are structurally independent. V-01's CONSTRAINT fix closes
C-35; V-02's Downstream-Action upgrade closes C-36. Combined, they target all 36
criteria. The column-definition guarantee preamble is retained from R15-V-05. No
PROPAGATION table.
**Predicts**: C-01 through C-36 (all 36 criteria).
**Expected composite**: 36/36 aspirational = 100.

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

  | Field           | Resolution                                                                    | Downstream-Action                                                                       |
  |-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                  |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins         |

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

## V-05 -- Convergent: C-35 + C-36 + Propagation Declaration + Column-Definition Guarantee

**Axis**: All three axes combined with R15-V-05's column-definition guarantee. V-01's
single-sentence ID-primary CONSTRAINT closes C-35. V-02's "consumed at S-X.X"
Downstream-Action closes C-36. V-03's SUB-STEP LABEL PROPAGATION table makes the
C-33->C-35->C-36 propagation chain checkable at declaration time. The R15-V-05
column-definition compliance guarantee statement is retained.
**Hypothesis**: Full structural convergence across all 36 criteria. C-33 defines sub-step
labels; C-35 is closed by single-sentence CONSTRAINT; C-36 is closed by "consumed at
S-X.X" verb form and explicit topic anchor; the PROPAGATION table makes the propagation
chain a first-class spec-level assertion rather than an implicit structural consequence.
The PROPAGATION table's "CONSTRAINT reference (ID-primary)" column heading also serves
as an in-spec reminder that column 1 form is the required C-35 form, making the
constraint block's correct form checkable by comparing the PROPAGATION table against
the CONSTRAINT block text.
**Predicts**: C-01 through C-36 (all 36 criteria), with C-35 and C-36 guaranteed by
structure at all three propagation locations.
**Expected composite**: 36/36 aspirational = 100.

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

  | Sub-step | CONSTRAINT reference (ID-primary) | Table Downstream-Action field | Execution emit              |
  |----------|------------------------------------|-------------------------------|-----------------------------|
  | S-3.1    | S-3.1 (carry)                      | tier-source row               | S-3.1 carry emit            |
  | S-3.2    | S-3.2 (compliance detection)       | compliance-tags row           | S-3.2 compliance check emit |
  | S-3.3    | S-3.3 (flag computation)           | tier row                      | S-3.3 flag resolved emit    |
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

  | Field           | Resolution                                                                    | Downstream-Action                                                                       |
  |-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Consumed across all steps as artifact subject; no single sub-step anchor                |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Consumed at S-3.3 for tier-conditional flag refinement                                  |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Consumed at S-3.2 for COMPLIANCE-OVERRIDE path detection                                |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Consumed at S-3.1; re-emitted as part of S-3.1 carry record before S-3.2 begins         |

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

## Scorecard prediction (v12 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-32 | pass | pass | pass | pass | pass |
| C-33 (sub-step lifecycle labels) | pass | pass | pass | pass | pass |
| C-34 (three-column S-0 table) | pass | pass | pass | pass | pass |
| C-35 (ID-primary constraint language) | **pass** | miss | miss | **pass** | **pass** |
| C-36 (sub-step anchors in Downstream-Action) | miss | **pass** | partial | **pass** | **pass** |
| **Predicted composite (aspirational)** | 35/36 | 35/36 | 34/36 | **36/36** | **36/36** |

**Gap analysis:**

- V-01: C-36 miss -- topic row has no sub-step anchor; verb form is "Carried to" not
  "Consumed at". C-35 closes cleanly by removing the prose-primary second sentence.
- V-02: C-35 miss -- CONSTRAINT second sentence retains "Primary operations select (S-1)..."
  prose-primary form. C-36 closes via "consumed at S-X.X" and explicit topic annotation.
- V-03: C-35 miss (CONSTRAINT unchanged from R15-V-05); C-36 partial (three sub-step
  refs present as "Carried to S-X.X", topic still unanchored). PROPAGATION table creates
  awareness of where gaps are but does not structurally close them.
- V-04: Both close. The two single-axis fixes are structurally independent and combine
  without interference. No propagation overhead.
- V-05: Both close plus PROPAGATION table makes the chain a first-class spec assertion.
  If execution-trace quality is scored, V-05 may edge ahead of V-04.

**Expected leaderboard:** V-04 = V-05 > V-01 = V-02 > V-03.
