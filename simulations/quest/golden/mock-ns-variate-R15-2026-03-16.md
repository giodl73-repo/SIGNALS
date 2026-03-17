---
skill: quest-variate
skill_target: mock-ns
round: 15
rubric_version: 11
date: 2026-03-16
---

# mock-ns -- Round 15 Variations

Rubric: v11 (C-01 through C-34, aspirational denominator 26).

New criteria in v11 (now pass conditions):
- **C-33** -- Sub-step labeled lifecycle at S-3 and S-5: the spec lifecycle declaration
  labels S-3 to at minimum three named sub-steps (S-3.1 carry, S-3.2 compliance, S-3.3 flag)
  and S-5 to at minimum four named sub-steps (S-5.1 count, S-5.2 order, S-5.3 header,
  S-5.4 write). Sub-step identifiers become the precision vocabulary for constraint language,
  enabling C-14's blocked-step enumeration and C-16's three-op coverage by label reference.
- **C-34** -- Three-column table structure for S-0 field entries: all S-0 field entries
  appear as rows in a three-column markdown table (Field | Resolution | Downstream-Action).
  The column definitions provide a format-level guarantee that C-15, C-18, C-19, and C-20
  are satisfied for every row by structure rather than by per-entry prose crafting.

Both are mechanism criteria: they introduce structural patterns that provide format-level
compliance guarantees for existing content requirements, reducing reliance on prose crafting.
C-33 and C-34 are independent -- each can be tested alone before combining.

R14 (presumed) seeded both mechanisms. R15 isolates C-34 (V-01), isolates C-33 (V-02),
combines both with prose constraint language (V-03), combines with sub-step identifiers as
constraint vocabulary (V-04), and achieves full structural convergence with explicit
column-definition compliance statements (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Output format (three-column S-0 table) | C-34 single-axis: replacing S-0 enriched bullets with a three-column table enforces C-15/C-18/C-19/C-20 by column definition. C-33 absent (S-3/S-5 flat). Predicts C-01 through C-32, C-34. |
| V-02 | Lifecycle emphasis (sub-step labeled S-3 and S-5) | C-33 single-axis: LIFECYCLE declaration with S-3.1/S-3.2/S-3.3 and S-5.1/S-5.2/S-5.3/S-5.4 satisfies C-33. S-0 keeps enriched bullets. C-34 absent. Predicts C-01 through C-33. |
| V-03 | Combined output format + lifecycle emphasis | C-33 + C-34 together. Three-column S-0 table AND sub-step labels. Constraint language still uses prose names ("skill selection", "category lookup", "flag computation"). Tests independent satisfaction before precision vocabulary is added. Predicts C-01 through C-34. |
| V-04 | Phrasing register (sub-step identifiers as constraint vocabulary) | C-33 precision deployment: S-0 CONSTRAINT references blocked sub-steps by identifier ("S-3.1 carry, S-3.2 compliance, S-3.3 flag"). C-14 enumeration and C-16 three-op coverage achieved by label reference. Also includes C-34 table. Predicts C-01 through C-34 with highest C-14/C-16 precision. |
| V-05 | Convergent (column-definition compliance guarantee + full sub-step precision) | Full structural convergence. C-34 table column headers explicitly named as the compliance enforcement mechanism for C-15/C-18/C-19/C-20. C-33 sub-step identifiers used as precision vocabulary throughout all constraint references. All 34 criteria targeted with structural guarantees. |

---

## V-01 -- Output Format: Three-Column S-0 Table (C-34 single axis)

**Axis**: Output format -- all S-0 field entries appear as rows in a three-column markdown
table (Field | Resolution | Downstream-Action) instead of enriched dash-bullet entries.
**Hypothesis**: The three-column table structure provides a format-level guarantee for
C-15 (per-field downstream action), C-18 (self-contained entries), C-19 (explicit
self-sufficient form), and C-20 (uniform coverage) via column definitions rather than
per-entry prose crafting. C-34 passes. C-33 absent -- S-3 and S-5 remain flat without
sub-step labels.
**Predicts**: C-01 through C-32 | C-34 | C-33 miss.
**Expected composite**: 33/34 aspirational.

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

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection (S-1), category lookup (S-2), or flag
computation (S-3) until this step's emit line is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

Record all S-0 field values in this table before proceeding:

  | Field           | Resolution                                                                    | Downstream-Action                                                           |
  |-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
  | topic           | Value from input argument                                                     | Subject for all steps; used in artifact path, header, and body              |
  | tier            | TOPICS.md entry if found; 1 if not found; --tier value if flag provided       | Carried to S-3 for tier-conditional flag refinement                         |
  | compliance-tags | TOPICS.md entry if found; none if not found                                   | Carried to S-3; triggers COMPLIANCE-OVERRIDE path if tag present            |
  | tier-source     | TOPICS.md if found and no override; default-1 if not found; --tier-override   | Included in S-0 emit; re-emitted in S-3 carry record                        |

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

Emit S-0 carry record (before any computation):
  > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

Emit compliance signal detection:
  > Compliance check: {DETECTED [signal: {signal-id}] | NOT-DETECTED}

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

Path: BASE if HIGH-STRUCTURE non-critical or EVIDENCE-HEAVY/MIXED with no compliance signal.
TIER-REFINEMENT if HIGH-STRUCTURE critical at tier >= 2.
COMPLIANCE-OVERRIDE if compliance signal DETECTED.

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

Generate artifact content:

HEADER BLOCK (first content in artifact):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

Emit: > Section: MOCK ARTIFACT header block [generated]

FIDELITY WARNING (immediately after header):

  HIGH-STRUCTURE ->
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY ->
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made.

  MIXED ->
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims
    may be partially accurate or partially fabricated. Review for plausibility.

Emit: > Section: Fidelity warning [generated]

MOCK BODY (after fidelity warning):

  Generate mock content following the exact golden structural pattern of {skill-id}:
  correct section headings, required tables and lists, gate or verdict line in expected
  position, enforcement mechanisms present. Use {topic} as subject throughout.
  A reader familiar with {skill-id} must identify the skill from the body alone.

Emit: > Section: Mock body ({skill-id} golden structure) [generated]

---

STEP S-5 -- FINALIZE

Emit count assertion:
  > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

Emit ordering assertion:
  > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

Emit header reconciliation:
  > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

Write as the last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 -- Lifecycle Emphasis: Sub-Step Labeled S-3 and S-5 (C-33 single axis)

**Axis**: Lifecycle emphasis -- an explicit LIFECYCLE declaration at the start of the spec
labels S-3 to three named sub-steps (S-3.1 carry, S-3.2 compliance, S-3.3 flag) and S-5
to four named sub-steps (S-5.1 count, S-5.2 order, S-5.3 header, S-5.4 write). Sub-step
headers appear in both the declaration and the execution sections.
**Hypothesis**: The lifecycle declaration with sub-step identifiers satisfies C-33
structurally. The sub-steps also make C-30 (carry at S-3 entry), C-28 (compliance before
flag), C-27/C-32/C-26 (within-S-5 ordering) achievable by label reference. S-0 field
entries remain enriched bullets (not a three-column table) -- C-34 is absent. Constraint
language names steps by prose role rather than sub-step identifier.
**Predicts**: C-01 through C-33 | C-34 miss.
**Expected composite**: 33/34 aspirational.

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
  S-4  Artifact generation
  S-5  Finalization
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection (S-1), category lookup (S-2), or flag
computation (S-3) until this step's emit line is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

Field entries (carried into S-3):
  - topic: {value from input} | from input argument | carried as subject to all steps;
    used in artifact path, header, and body
  - tier: {value} | TOPICS.md entry if found; 1 if not found; --tier if flag provided |
    carried to S-3.3 for tier-conditional flag refinement
  - compliance-tags: {value} | TOPICS.md entry if found; none if not found |
    carried to S-3.2 for COMPLIANCE-OVERRIDE path check
  - tier-source: {value} | TOPICS.md if found/no override; default-1 if not found;
    --tier-override if --tier flag provided | included in S-0 emit; re-emitted at S-3.1

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
  Emit (before any computation within S-3):
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit:
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
  Emit: > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit: > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 -- Combined: C-33 + C-34 (Both Mechanisms, Prose Constraint Language)

**Axis**: Combined output format + lifecycle emphasis -- the three-column S-0 table (C-34)
AND the LIFECYCLE declaration with sub-step labels (C-33). Constraint language continues
to use prose step names ("skill selection", "category lookup", "flag computation") without
sub-step identifier precision. Tests independent structural satisfaction of both criteria
before sub-step labels are deployed as constraint vocabulary.
**Hypothesis**: Both C-33 and C-34 pass from structure alone. C-14 and C-16 satisfy at
the existing prose level (naming 3 blocked steps, naming select/lookup/flag ops). The
sub-step identifiers in S-3 and S-5 are active as execution labels but not yet referenced
in the S-0 CONSTRAINT block. V-04 will close this by using sub-step labels in constraints.
**Predicts**: C-01 through C-34 (all 34 criteria).
**Expected composite**: 34/34 aspirational = 100.

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
  S-4  Artifact generation
  S-5  Finalization
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection (S-1), category lookup (S-2), or flag
computation (S-3) until this step's emit line is written to the conversation.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

Record all S-0 field values in this table before proceeding:

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
  Emit (before any computation within S-3):
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit:
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
  Emit: > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit: > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-04 -- Phrasing Register: Sub-Step Identifiers as Constraint Vocabulary

**Axis**: Phrasing register -- sub-step labels defined in the LIFECYCLE declaration are
deployed as precision vocabulary in the S-0 CONSTRAINT block. The constraint names blocked
sub-steps by identifier ("S-3.1 carry, S-3.2 compliance, S-3.3 flag") rather than by prose
role ("flag computation"). C-14 enumeration and C-16 three-op coverage are achieved by
label reference rather than by inline prose enumeration. Three-column S-0 table also present.
**Hypothesis**: Using sub-step identifiers in constraint language elevates C-14 precision
(5 blocked steps named by sub-step identifier vs 3 prose names) and C-16 coverage
("select=S-1, lookup=S-2, flag=S-3.3" by label). C-33 and C-34 both pass. The constraint
block demonstrates that sub-step labels provide marginal value beyond V-03 specifically
for C-14 and C-16 accuracy.
**Predicts**: C-01 through C-34, with highest C-14/C-16 compliance precision.
**Expected composite**: 34/34 aspirational = 100.

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
  S-4  Artifact generation
  S-5  Finalization
    S-5.1  count -- manifest completeness assertion
    S-5.2  order -- section ordering assertion
    S-5.3  header -- header field reconciliation vs S-2 and S-3 audit values
    S-5.4  write -- artifact written emit and next-step line

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry),
S-3.2 (compliance), or S-3.3 (flag) until this step's emit line is written to the
conversation. Primary operations select (S-1), lookup (S-2), and flag (S-3.3) are all
blocked until S-0 completes.

Read TOPICS.md now. Emit as the first observable output:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance-tags: {tags | none},
    tier-source: {TOPICS.md | default-1 | --tier-override}

Record all S-0 field values in this table before proceeding:

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
  Emit as the first action of S-3 (before S-3.2 and S-3.3):
    > S-0 carry: tier={tier}, compliance-tags={tags}, tier-source={source}

  S-3.2 -- COMPLIANCE
  Emit after S-3.1, before S-3.3:
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

## V-05 -- Convergent: Column-Definition Compliance Guarantee + Full Sub-Step Precision

**Axis**: All mechanisms combined with explicit structural guarantee statements. The S-0
three-column table column headers are named as the compliance enforcement mechanism for
C-15/C-18/C-19/C-20, making the guarantee structural rather than implied. The S-0
CONSTRAINT uses sub-step identifiers as precision vocabulary (V-04 form). The LIFECYCLE
declaration explicitly states the enforcement relationship between C-33 (sub-step labels)
and the ordering constraints at S-3 and S-5.
**Hypothesis**: Full structural convergence. C-34's column headers are not just present
but named as the enforcement mechanism -- the preamble states "The three column definitions
below enforce field completeness for every row without per-entry inspection." C-33's
sub-step labels are used as constraint vocabulary throughout. All 34 criteria targeted
by structure rather than by prose crafting.
**Predicts**: C-01 through C-34 (all), with C-33/C-34 compliance guaranteed by column
definition and lifecycle labeling respectively, not by per-entry prose.
**Expected composite**: 34/34 aspirational = 100.

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
  Compute flag from category, tier, and critical-skill status.
  Input state: tier and compliance-tags from S-3.1 carry; compliance signal from S-3.2.

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

  Path discriminator:
    BASE             -- HIGH-STRUCTURE non-critical, or EVIDENCE-HEAVY/MIXED with no signal
    TIER-REFINEMENT  -- HIGH-STRUCTURE critical at tier >= 2
    COMPLIANCE-OVERRIDE -- compliance signal DETECTED at S-3.2

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
  Emit as first action of S-5 (before S-5.2 begins):
    > Manifest complete: 3/3 sections | {COMPLETE | INCOMPLETE [missing: {list}]}

  S-5.2 -- ORDER
  Emit after S-5.1, before S-5.3:
    > Section ordering: {IN-ORDER | REORDERED [reordered: {list}]}

  S-5.3 -- HEADER
  Emit after S-5.2, before S-5.4:
    > Header: Category={CATEGORY} [S-2: MATCH | MISMATCH] | Flag={flag} [S-3: MATCH | MISMATCH]

  S-5.4 -- WRITE
  Write as the last line of the artifact:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

  Emit after S-5.3 header reconciliation:
    > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```
