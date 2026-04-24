---
skill: quest-variate
skill_target: mock-ns
round: 2
rubric_version: 2
date: 2026-03-16
---

# mock-ns -- Round 2 Variations

Rubric: v2 (C-01 through C-13 -- 5 essential / 3 recommended / 5 aspirational).

R1 baseline: V-03/V-04/V-05 scored 100 on rubric v1 (C-01 through C-10). All passed
C-09 (topic-plan exclusion) and C-10 (default pass, no compliance tags). Under rubric
v2's new aspirational criteria, the R1 top scorers should pass C-11 (FLAG rule covers
5 cases, names trace-*, scout-feasibility, listen-* explicitly) and C-12 (S-0 step
resolves tier before S-1). The open gap is C-13: R1 V-03 had no error guard; R1 V-04
and V-05 had "emit an error and stop" but did not name the skill-id or direct to the
registry. C-13 pass condition requires: error names the unrecognized skill-id AND directs
the user to the registry. All five R2 variations target C-13.

Single-axis variations: V-01, V-02, V-03.
Two-axis combinations: V-04.
Convergent (all axes): V-05.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | C-13 minimal error block | Adding the minimum C-13-compliant error (name the skill-id + registry pointer) to the R1-V-05 foundation produces the first C-13 pass without disturbing any other criterion. |
| V-02 | C-11 wildcard notation in FLAG table | Replacing the R1-V-05 full skill list in the FLAG table with wildcard notation (`trace-*`, `listen-*`) alongside explicit `scout-feasibility` passes C-11 with fewer words and less surface area for list-completion errors. |
| V-03 | C-12 explicit prohibition block | Adding an explicit CONSTRAINT block that names the prohibited computations (skill selection, category lookup, flag computation) satisfies C-12 under adversarial conditions -- beyond what step-ordering alone provides. |
| V-04 | C-12 explicit prohibition + C-13 full error block (two-axis) | Combining the ordering CONSTRAINT from V-03 with a full error block from V-01 in a conversational register tests whether register affects C-11/C-12/C-13 reliability when both are present. |
| V-05 | Convergent (all three new criteria, all prior criteria) | R1-V-05 foundation + C-13 full error block + C-11 wildcard notation + C-12 explicit prohibition anchor. Predicts 100 on all 13 criteria. |

---

## V-01 -- C-13 Minimal Error Block

**Axis**: C-13 -- minimal compliant error block in category lookup step.
**Hypothesis**: R1-V-05 passed all criteria except C-13 (brief "emit an error and stop"
did not name the skill-id or direct to registry). Adding two required elements -- naming
the skill-id and pointing to the registry -- satisfies C-13 without changing anything
else. All other criteria carry forward from R1-V-05.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

Read TOPICS.md. Emit a dedicated line:

  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

If the topic is registered, extract its tier and compliance tags.
If not registered, use tier=1 and compliance tags=none.
If --tier was given on the command line, it takes precedence over TOPICS.md.
Carry the resolved tier and compliance tags into steps S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it as-is and skip the table below.
Otherwise look up the namespace in this table to find the default skill:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                   |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,      |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,       |
  |                | draft-proposal, draft-pitch, review-design, review-code,        |
  |                | trace-request, trace-component, trace-contract, trace-state,    |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, |
  |                | flow-trigger, flow-integration, program-plan                    |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,               |
  |                | listen-feedback, listen-support, listen-adoption                |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,          |
  |                | review-users                                                    |

If the skill-id is not found in any row, emit the following error and stop:

  ERROR: Unrecognized skill-id: "{skill-id}"
  "{skill-id}" is not in the mock-ns category registry.
  Check the registry at simulations/mock/ or verify the skill-id spelling.

Do not assign a fallback category. Do not continue past this step if an error was emitted.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG from CATEGORY and tier (tier was resolved in S-0).
Evaluate the first matching row:

  | Category       | Tier | Skill condition                                        | Flag value                                                        |
  |----------------|------|--------------------------------------------------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | not a critical skill                                   | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | 1    | critical skill (trace-*, scout-feasibility, listen-*)  | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | 2+   | critical skill (trace-*, scout-feasibility, listen-*)  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any  | any                                                    | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any  | any                                                    | REVIEW-FOR-PLAUSIBILITY                                           |

Critical skills for rows 2 and 3:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility,
  listen-support, listen-feedback, listen-adoption

Compliance override (applied after the table, overrides all rows):
  If compliance tags are present in TOPICS.md AND skill is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Carry it verbatim into S-4. Do not recompute or modify it.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact structure:

---- HEADER BLOCK (required; first content in file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

---- FIDELITY WARNING (required; immediately after header) ----

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility,
    listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated.
    Review for plausibility before accepting coverage.

---- MOCK BODY (required; after fidelity warning) ----

  Generate mock content following the exact golden structural pattern of {skill-id}:
  - Use the correct section headings for {skill-id}
  - Include all required tables, lists, and scoring structures in expected positions
  - Place the gate or verdict line in its expected structural position
  - Enforce any category-specific output rules (role card format, numeric rubric, etc.)
  - Use {topic} as the subject throughout
  A reader familiar with the real {skill-id} output must be able to identify the skill
  from the body alone without reading the header.

---

STEP S-5 -- FINALIZE

After the artifact is written, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (in that case, mock-review already controls the next step).
```

---

## V-02 -- C-11 Wildcard Notation in FLAG Table

**Axis**: C-11 -- wildcard notation (`trace-*`, `listen-*`) in FLAG rule replaces full
skill enumeration in the critical skill condition column.
**Hypothesis**: C-11 requires the FLAG rule to "name critical skill namespaces explicitly
as `trace-*`, `scout-feasibility`, and `listen-*`." Wildcard notation is the most direct
way to satisfy this wording and eliminates the risk of list-completion errors (missing
one trace-* or listen-* skill from a full enumeration). Combined with C-13 minimal error
block, predicts 100.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

Read TOPICS.md. Emit a dedicated line:

  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Resolution:
  - Topic found in TOPICS.md: use its tier and compliance tags.
  - Topic not found: tier=1, compliance tags=none.
  - --tier given on command line: overrides TOPICS.md tier.

Carry the resolved tier and compliance tags into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise use the representative skill for the namespace:

  scout -> scout-feasibility  |  draft   -> draft-spec       |  review -> review-design
  flow  -> flow-resilience    |  trace   -> trace-request    |  prove  -> prove-hypothesis
  listen -> listen-support    |  program -> program-plan
  topic -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row:

  | Category       | Member skills                                                   |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,      |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,       |
  |                | draft-proposal, draft-pitch, review-design, review-code,        |
  |                | trace-request, trace-component, trace-contract, trace-state,    |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, |
  |                | flow-trigger, flow-integration, program-plan                    |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,               |
  |                | listen-feedback, listen-support, listen-adoption                |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,          |
  |                | review-users                                                    |

If the skill-id does not appear in any row:
  Emit: ERROR: Unrecognized skill-id: "{skill-id}" -- not in category registry.
        Check simulations/mock/ for the current registry or verify the skill-id spelling.
  Stop. Do not proceed.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG using this 5-case table. Evaluate CATEGORY, tier (from S-0), and whether
the skill matches the critical-namespace pattern:

  | Case | Category       | Tier | Skill matches critical pattern?    | Flag value                                                        |
  |------|----------------|------|------------------------------------|-------------------------------------------------------------------|
  | 1    | HIGH-STRUCTURE | any  | No (not trace-*, scout-feasibility,| none (structural coverage reliable)                               |
  |      |                |      |  or listen-*)                      |                                                                   |
  | 2    | HIGH-STRUCTURE | 1    | Yes (trace-*, scout-feasibility,   | none (structural coverage reliable)                               |
  |      |                |      |  or listen-*)                      |                                                                   |
  | 3    | HIGH-STRUCTURE | 2+   | Yes (trace-*, scout-feasibility,   | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  |      |                |      |  or listen-*)                      |                                                                   |
  | 4    | EVIDENCE-HEAVY | any  | any                                | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | 5    | MIXED          | any  | any                                | REVIEW-FOR-PLAUSIBILITY                                           |

  Critical namespace pattern expansion:
    trace-*         = trace-request, trace-component, trace-contract, trace-state,
                      trace-skill, trace-migration, trace-deployment
    scout-feasibility (exact name, no wildcard)
    listen-*        = listen-support, listen-feedback, listen-adoption

  Compliance override (applied after, regardless of case):
    If compliance tags present AND skill is scout-compliance or trace-permissions:
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Copy verbatim into S-4. Do not recompute.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Structure:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3}

---

{fidelity warning -- select the block that matches CATEGORY}

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific
    claims (competitor names, market data, research findings) may be partially
    fabricated. Review for plausibility before accepting coverage.

---

{mock body -- golden structural pattern of {skill-id}}

  All required section headings. Required tables, lists, and scoring structures in
  expected positions. Gate or verdict line where the real skill produces one.
  Enforcement mechanisms present. Use {topic} as subject throughout.
  A reader familiar with {skill-id} must identify the skill from the body alone
  without reading the header.

---

STEP S-5 -- FINALIZE

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-03 -- C-12 Explicit Prohibition Block

**Axis**: C-12 -- an explicit CONSTRAINT block in S-0 that names the specific computations
prohibited until after the TOPICS.md emit line.
**Hypothesis**: R1 top scorers satisfied C-12 through structural step ordering (S-0 before
S-1). The v2 rubric's pass condition warns against prompts that read TOPICS.md "within the
same step as skill selection." An explicit CONSTRAINT block naming the prohibited
computations (skill selection, category lookup, flag computation) creates a stronger signal
that C-12 fires even under prompt compression or interleaving. Combined with a C-13
compliant error block, predicts 100.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or any
other step in this run until after the status line below has been emitted. The tier value
resolved in this step is the only valid tier for this run.

Read TOPICS.md. Emit:

  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Resolution rules:
  - Topic found: use its tier and compliance tags.
  - Topic not found: tier=1, compliance tags=none.
  - --tier given: overrides TOPICS.md tier.

S-0 is complete when this line has been written. Carry resolved tier and compliance tags
into all downstream steps.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it and skip the table.
Otherwise use the namespace default:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row:

  | Category       | Member skills                                                   |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,      |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,       |
  |                | draft-proposal, draft-pitch, review-design, review-code,        |
  |                | trace-request, trace-component, trace-contract, trace-state,    |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, |
  |                | flow-trigger, flow-integration, program-plan                    |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,               |
  |                | listen-feedback, listen-support, listen-adoption                |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,          |
  |                | review-users                                                    |

UNKNOWN SKILL GUARD:
If the skill-id is not found in any row above, emit this error block and stop:

  ERROR: Unrecognized skill-id: "{skill-id}"
  This skill-id is not in the mock-ns category registry. No CATEGORY can be assigned
  and no mock can be generated.
  To resolve: check the skill-id spelling, or consult the registry at
  simulations/mock/ to see which skill-ids are registered.

Do not proceed past this step if an error was emitted.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG from CATEGORY and tier. Apply the first row that matches:

  | Category       | Tier | Skill condition                                        | Flag value                                                        |
  |----------------|------|--------------------------------------------------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | not critical (not trace-*, not scout-feasibility,      | none (structural coverage reliable)                               |
  |                |      |  not listen-*)                                         |                                                                   |
  | HIGH-STRUCTURE | 1    | critical: trace-*, scout-feasibility, listen-*         | none (structural coverage reliable)                               |
  | HIGH-STRUCTURE | 2+   | critical: trace-*, scout-feasibility, listen-*         | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  | EVIDENCE-HEAVY | any  | any                                                    | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | MIXED          | any  | any                                                    | REVIEW-FOR-PLAUSIBILITY                                           |

  Expansion of critical-namespace patterns:
    trace-*           = trace-request, trace-component, trace-contract, trace-state,
                        trace-skill, trace-migration, trace-deployment
    scout-feasibility = scout-feasibility (exact)
    listen-*          = listen-support, listen-feedback, listen-adoption

  Compliance override (checked last, overrides all rows above):
    If TOPICS.md compliance tags present AND skill is scout-compliance or
    trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is resolved. Carry verbatim into S-4. Do not recompute.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim copy, not rederived}

---

{fidelity warning for CATEGORY}

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not draw conclusions about {topic}.
    The sections are right; the contents are invented. A real {skill-id} run is
    required before any evidence-based decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or partially
    fabricated. Review for plausibility before accepting coverage.

---

{mock body}

Follow the exact golden structural pattern of {skill-id}. Include all required section
headings, required tables and scoring structures, gate or verdict line in its expected
position, enforcement mechanisms where the skill places them. Use {topic} as subject.
A reader familiar with {skill-id} must identify the skill from the body alone without
reading the header.

---

STEP S-5 -- FINALIZE

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-04 -- Conversational Register + C-12 Prohibition + C-13 Full Error Block (Two-Axis)

**Axis**: Conversational register (R1-V-04) combined with explicit ordering prohibition
(V-03) and full C-13 error block (V-01). Two-axis test: does conversational phrasing
maintain C-11/C-12/C-13 reliability when both are fully satisfied in prose rather than
step-labeled format?
**Hypothesis**: R1 confirmed that conversational register achieves C-06 and C-09 parity
with formal prompts. This variation tests whether "the very first thing you do -- before
selecting a skill, before assigning a category, before computing a flag" produces the
same C-12 reliability as a CONSTRAINT block. If yes, register is confirmed as
non-load-bearing for all v2 criteria.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Your job is to produce one mock artifact for a single namespace. One pass. No prompts.
Read TOPICS.md first. Pick the skill. Assign category. Compute the flag. Write the
artifact. Emit the next-step line. Done.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if given)

---

The very first thing you do -- before selecting a skill, before assigning a category,
before computing a flag, before writing any part of the artifact -- is read TOPICS.md
and emit this line:

  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

If the topic is registered in TOPICS.md, use its tier and note any compliance tags.
If not registered, use tier 1 and no compliance tags.
If --tier was given on the command line, that value wins over TOPICS.md.
Keep the resolved tier for all steps that follow.

---

Next, pick the skill. If --skill was given, use it. Otherwise use the namespace default:

  scout -> scout-feasibility    |  draft   -> draft-spec       |  review -> review-design
  flow  -> flow-resilience      |  trace   -> trace-request    |  prove  -> prove-hypothesis
  listen -> listen-support      |  program -> program-plan
  topic -> topic-plan   (never topic-status -- meta-structural and excluded)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

Now assign the category. Every skill belongs to exactly one of three groups:

  HIGH-STRUCTURE (structure is the substance; mock fidelity is high):
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY (evidence is the value; contents are fabricated in a mock):
    prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED (partly structural, partly evidential):
    scout-competitors, prove-hypothesis, review-customers, review-users

If the skill is not in any group, emit an error that names the unrecognized skill-id
and directs the user to the registry at simulations/mock/, then stop immediately.
Do not assign a fallback category or continue producing the artifact.

---

Now compute the Flag. There are five cases -- take the first one that matches:

  1. Category = HIGH-STRUCTURE, skill is NOT in trace-*, scout-feasibility, or listen-*:
     Flag = "none (structural coverage reliable)"

  2. Category = HIGH-STRUCTURE, skill IS in trace-*, scout-feasibility, or listen-*,
     tier = 1:
     Flag = "none (structural coverage reliable)"

  3. Category = HIGH-STRUCTURE, skill IS in trace-*, scout-feasibility, or listen-*,
     tier >= 2:
     Flag = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  4. Category = EVIDENCE-HEAVY:
     Flag = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  5. Category = MIXED:
     Flag = "REVIEW-FOR-PLAUSIBILITY"

  Where:
    trace-*         covers trace-request, trace-component, trace-contract, trace-state,
                    trace-skill, trace-migration, trace-deployment
    scout-feasibility is the exact skill name (no wildcard)
    listen-*        covers listen-support, listen-feedback, listen-adoption

  Compliance override (applied after the five cases):
    If TOPICS.md has compliance tags AND the skill is scout-compliance or trace-permissions,
    replace the Flag with "REAL-REQUIRED (compliance-sensitive)".

---

Now write the artifact to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open with the MOCK ARTIFACT header block -- all six fields, in this exact order:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {value computed above}

Right after the header, include the fidelity warning for the category:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
    reliable. Content is synthetically generated but structurally representative.
    Adequate for Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not draw conclusions about {topic}.
    A real {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims
    (competitor names, market data, research findings) may be partially fabricated.
    Review for plausibility before accepting coverage.

After the fidelity warning, generate the mock body. Follow the exact golden structure
of {skill-id}: correct section headings, required tables or lists, gate or verdict line
where expected, enforcement mechanisms in place. Use {topic} as the subject throughout.
Anyone familiar with the real {skill-id} output should be able to identify the skill
from the body alone without reading the header.

---

When done, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Make the last line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

(Omit only when called from within a mock-review session to regenerate a thin namespace.)
```

---

## V-05 -- Convergent (All Three v2 Criteria + All Prior Criteria)

**Axis**: R1-V-05 foundation + C-13 full error block (named skill-id + registry pointer) +
C-11 wildcard notation in 5-row FLAG table + C-12 explicit prohibition anchor in S-0.
**Hypothesis**: R1-V-05 scored 100 on rubric v1 (passing C-09 and C-10 as aspirational).
Under rubric v2, R1-V-05 likely fails only C-13 (its error-stop did not name the skill-id
or point to the registry). Adding the three targeted elements produces the first v2-clean
100: explicit C-12 prohibition (belt-and-suspenders with S-0 step ordering), wildcard
notation for C-11 clarity, and a full C-13 error block. All R1-V-05 criterion passes carry
forward unchanged.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Read inputs, resolve defaults, write artifact, emit next-step.

INPUTS
  Topic:     {topic}                (required)
  Namespace: {namespace}            (required: scout | draft | review | flow | trace |
                                     prove | listen | program | topic)
  --skill    {skill-id}             (optional)
  --tier     1 | 2 | 3              (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category assignment, flag computation, or
any other step in this run until after the TOPICS.md status line below is written.

Read TOPICS.md. Emit:

  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Field resolution -- all three fields are required; do not omit any:
  - Existence: "found" if topic is registered in TOPICS.md, otherwise "not found"
  - Tier: read from TOPICS.md if found; default to 1 if not found;
           override with --tier if provided on the command line
  - Compliance tags: read from TOPICS.md if found; "none" if not found or no tags present

Carry resolved tier and compliance tags into steps S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it as-is and skip the table below.
Otherwise look up the namespace in this table to find the default skill:

  | Namespace | Default skill     | Exclusion note                                |
  |-----------|-------------------|-----------------------------------------------|
  | scout     | scout-feasibility |                                               |
  | draft     | draft-spec        |                                               |
  | review    | review-design     |                                               |
  | flow      | flow-resilience   |                                               |
  | trace     | trace-request     |                                               |
  | prove     | prove-hypothesis  |                                               |
  | listen    | listen-support    |                                               |
  | program   | program-plan      |                                               |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                   |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,      |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,       |
  |                | draft-proposal, draft-pitch, review-design, review-code,        |
  |                | trace-request, trace-component, trace-contract, trace-state,    |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, |
  |                | flow-trigger, flow-integration, program-plan                    |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,               |
  |                | listen-feedback, listen-support, listen-adoption                |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,          |
  |                | review-users                                                    |

UNKNOWN SKILL GUARD:
If the skill-id does not appear in any row, emit the following error block and stop:

  ERROR: Unrecognized skill-id: "{skill-id}"
  "{skill-id}" is not in the mock-ns category registry. No CATEGORY can be assigned
  and no mock can be generated for an unregistered skill.
  Check the skill-id spelling and confirm it belongs to one of the 9 Signal namespaces.
  Consult the registry at simulations/mock/ to see which skill-ids are registered.

Do not assign a fallback category. Do not continue past this guard.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG using this complete 5-case table. Evaluate CATEGORY, tier (from S-0),
and whether the skill matches the critical-namespace pattern:

  | Case | Category       | Tier | Skill matches critical pattern?           | Flag value                                                        |
  |------|----------------|------|-------------------------------------------|-------------------------------------------------------------------|
  | 1    | HIGH-STRUCTURE | any  | No -- not trace-*, not scout-feasibility, | none (structural coverage reliable)                               |
  |      |                |      |  not listen-*                             |                                                                   |
  | 2    | HIGH-STRUCTURE | 1    | Yes -- trace-*, scout-feasibility,        | none (structural coverage reliable)                               |
  |      |                |      |  or listen-*                              |                                                                   |
  | 3    | HIGH-STRUCTURE | 2+   | Yes -- trace-*, scout-feasibility,        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)    |
  |      |                |      |  or listen-*                              |                                                                   |
  | 4    | EVIDENCE-HEAVY | any  | any                                       | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)      |
  | 5    | MIXED          | any  | any                                       | REVIEW-FOR-PLAUSIBILITY                                           |

  Critical-namespace pattern expansion:
    trace-*           = trace-request, trace-component, trace-contract, trace-state,
                        trace-skill, trace-migration, trace-deployment
    scout-feasibility = scout-feasibility (exact name, no wildcard)
    listen-*          = listen-support, listen-feedback, listen-adoption

  Compliance override (applied after the table, overrides any case):
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Carry it verbatim into A-1. Do not recompute or modify it.

---

STEP A-1 -- ASSEMBLE HEADER

Copy FLAG from S-3 verbatim. Do not rederive it.

Write the artifact to: simulations/mock/{topic}-{namespace}-mock-{date}.md

HEADER BLOCK (required; must be first content in file after any frontmatter):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, before any mock content.
Separate from the header and from the body with --- delimiters.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility,
    listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated.
    Review for plausibility before accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate mock content following the exact golden structural pattern of {skill-id}:
  - Use the correct section headings for {skill-id}
  - Include all required tables, lists, and scoring structures in expected positions
  - Place the gate or verdict line in its expected structural position
  - Enforce any category-specific output rules (role card format, numeric rubric, etc.)
  - Use {topic} as the subject throughout; all values synthetic but structurally
    representative
  A reader familiar with the real {skill-id} output must be able to identify the skill
  from the body alone without reading the header.

---

STEP A-4 -- WRITE ARTIFACT

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit only if this run was called from within a mock-review session to
regenerate a thin namespace (mock-review already controls the next step in that context).
```
