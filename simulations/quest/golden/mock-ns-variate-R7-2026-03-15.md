---
skill: quest-variate
skill_target: mock-ns
round: 7
rubric_version: 7
date: 2026-03-15
---

# mock-ns -- Round 7 Variations

Rubric: v7 (C-01 through C-24, aspirational denominator 16).

New criteria in v7:
- **C-23** -- Failure-consequence statement at the compute site (depends on C-21)
- **C-24** -- No-instruction-exempt affirmative closure at the consumption site (depends on C-22)

R6 V-05 carried C-21 ("Every execution path that reaches A-1 carries the FLAG value emitted
here. No path is exempt.") and C-22 ("or any other instruction in this step"). R7 closes the
remaining two asymmetries: C-23 mirrors C-20 at the compute site; C-24 mirrors C-21 at the
consumption side.

Each variation is a **complete, runnable skill body prompt**. Single-axis variation first
(V-01 through V-03), then combined axes (V-04, V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Inertia framing (C-23 only, compute-site consequence as primary addition) | C-23 is the higher-leverage R7 criterion. The affirmative closure at S-3 (C-21) asserts that every path carries the FLAG value and no path is exempt -- but it leaves the executor to infer why a violation would be serious. Naming the contamination mechanism and its downstream consequence makes the guarantee credible at the moment it is stated. C-24 at the consumption side is redundant because C-21 already forecloses the compute-path corruption that C-24 guards against downstream. |
| V-02 | Phrasing register (C-24 only, consumption-side affirmative as primary addition) | C-24 is the higher-leverage R7 criterion. The catch-all at A-1 (C-22) covers instruction types by exclusion -- "or any other instruction in this step" is a negative bound. C-24 converts that negative bound to a positive assertion of coverage. A positive-coverage statement is epistemically stronger: the executor cannot read "or any other" as limited to the semantic category of the three named types. C-23 at the compute site adds consequence language the executor can infer from C-20 at A-1, where the downstream mismatch is already named. |
| V-03 | Lifecycle emphasis (R6 baseline -- neither C-23 nor C-24) | R6 full convergence (C-01 through C-22) is sufficient. C-21 at the compute site converts the path-class enumeration to a positive assertion of exhaustiveness; C-22 extends the anti-displacement closure to cover unnamed instruction types. C-23 and C-24 add consequence and affirmative language over gaps that are operationally foreclosed by the upstream guarantees already in place. Baseline for scoring regression comparison. |
| V-04 | Output format + role sequence (C-23 minimal + C-24 full, table-structured) | C-23 and C-24 are independent structural completions. C-23 minimal form (single-sentence consequence) is sufficient to pass the criterion without importing the full C-20 verbosity pattern at the compute site. C-24 full form is necessary at the consumption side because the positive-coverage affirmative has no upstream analogue to compress against. Table-structuring S-3 clarifies the Flag-case decision without adding length to the prohibition block. |
| V-05 | Full convergence (all 24 criteria, prose emphasis) | C-23 and C-24 are mutually reinforcing with all prior layers. C-23 makes the consequence visible at the site where corruption originates; C-24 forecloses the residual "semantic-category" ambiguity at the consumption site. Neither is redundant. Full convergence is the only variant that predicts 100 on v7 aspirational. |

---

## V-01 -- Compute-Site Consequence (C-23 only)

**Axis**: Inertia framing -- failure-consequence statement added at the compute site only.
C-24 intentionally absent.
**Hypothesis**: C-23 is the stronger R7 addition. The affirmative closure (C-21) tells the
executor that every path carries FLAG and no path is exempt, but an executor under pressure
may deprioritize an unexplained positive-obligation statement. Naming the contamination
mechanism -- "A-1 will inherit a corrupted value indistinguishable from a correctly-computed
one" -- makes the cost of violation visible at the moment the guarantee is stated, not three
steps later at A-1. C-24 is not needed because C-21 already forecloses compute-path corruption
before A-1 is reached.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23. Missing: C-24.
**Expected composite**: 15/16 aspirational = ~99.4

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative skill for the namespace:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, the guarantee stated above is broken: A-1 will
inherit a corrupted value that cannot be distinguished from a correctly-computed one,
producing the same silent category mismatch described at the consumption site.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-02 -- Consumption-Side Affirmative (C-24 only)

**Axis**: Phrasing register -- no-instruction-exempt affirmative closure added at the
consumption site only. C-23 intentionally absent.
**Hypothesis**: C-24 is the stronger R7 addition. The catch-all clause at A-1 (C-22)
covers unnamed instruction types by negative inclusion -- "or any other instruction in
this step" asserts that nothing outside the three named types escapes the prohibition,
but the coverage is stated as an extension of the list, not as a positive fact. An
executor can read "or any other" as limited to instructions of the same semantic category
as the three canonical types. C-24 closes this residual ambiguity by asserting coverage
positively: "Every instruction in this step -- named or unnamed -- is governed by this
rule. No instruction in this step is exempt." C-23 at the compute site adds consequence
language that is already inferable from C-20 at A-1, where the downstream mismatch is
named explicitly.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-24. Missing: C-23.
**Expected composite**: 15/16 aspirational = ~99.4

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

Single-pass. No prompts.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock. If --skill is provided, use it. Otherwise use the
representative default:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule. Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-03 -- R6 Baseline (neither C-23 nor C-24)

**Axis**: Lifecycle emphasis -- R6 full convergence as regression baseline. No new R7
criteria introduced.
**Hypothesis**: R6 full convergence (C-01 through C-22) is already sufficient. C-21's
affirmative closure makes compute-site exhaustiveness a positive fact; C-22's catch-all
makes consumption-site instruction coverage exhaustive by construction. C-23 and C-24
add consequence language and positive-coverage affirmatives that the executor can already
infer from the upstream guarantees in place. Adding them introduces verbosity without
closing a gap that is operationally significant.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22. Missing: C-23, C-24.
**Expected composite**: 14/16 aspirational = ~98.8

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove |
                            listen | program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (default: 1)

Execute in one pass. No prompts. Write artifact. Done.

---

S-1. SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Determine the skill to mock.
  If --skill is specified, use it.
  Otherwise, apply the namespace default:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

S-2. CATEGORY

Look up the skill in the category table:

  HIGH-STRUCTURE
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY
    prove-websearch, prove-interview, prove-prototype, listen-feedback,
    listen-support, listen-adoption

  MIXED
    scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY = the value from this table. No other value is valid.

---

S-3. COMPUTE FLAG

FLAG is a named variable computed in this step. Compute it once.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt.

  CATEGORY = HIGH-STRUCTURE, critical namespace (trace-*, scout-feasibility,
             listen-*), tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"
  CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"
  CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"
  CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"
  Compliance override (compliance tags in TOPICS.md AND skill is scout-compliance
  or trace-permissions):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not modify FLAG after this step.

---

A-1. ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Build the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- do not rederive}

Place immediately after frontmatter, before all body content.

---

A-2. FIDELITY WARNING

Write the fidelity warning as the lead section of the artifact body, before mock
content, delimited by ---:

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Structure is correct; content is
    fabricated. Do not use for conclusions about {topic}. Real {skill-id} run
    required before evidence-based decisions.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable. Specific
    claims may be fabricated. Review for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
    reliable. Content is synthetically generated. Adequate for structural planning
    at Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

---

A-3. ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
All required sections, tables, gates, and enforcement mechanisms must be present in
the expected positions. Generic prose fails.

---

A-4. WRITE

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md
Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

A-5. NEXT STEP

Final artifact line:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit if regenerating from within a mock-review session.
```

---

## V-04 -- C-23 Minimal + C-24 Full (table-structured)

**Axis**: Output format + role sequence -- C-23 in minimal single-sentence form paired
with C-24 in full form. Table-structured S-3 flag-case decision.
**Hypothesis**: C-23 and C-24 are independent structural completions that do not require
the same elaboration level to satisfy their pass conditions. C-23 requires only that the
consequence be named (contamination mechanism + downstream effect); a single sentence is
sufficient. C-24 requires the full two-component form (positive-coverage statement +
no-exemption statement) with no minimal shortcut. Table-structuring the flag-case decision
in S-3 reduces cognitive overhead at the decision node without shortening the prohibition
block that follows it. The minimal C-23 form tests whether consequence visibility requires
extended elaboration or whether precision is enough.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24.
**Expected composite**: 100 (all 24 criteria).

---

```
You are running /mock:ns for Signal.

INPUTS

| Input     | Value                                                                      |
|-----------|----------------------------------------------------------------------------|
| Topic     | {topic} (required)                                                         |
| Namespace | {namespace} (required): scout | draft | review | flow | trace | prove |    |
|           | listen | program | topic                                                |
| --skill   | {skill-id} (optional -- default: representative skill)                     |
| --tier    | 1 | 2 | 3 (optional -- default: 1)                                    |

Single-pass. No prompts.

---

PROCEDURE

S-1  SETUP
     Read TOPICS.md. Emit:
       > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

     Select the skill:

     | Namespace | Default skill       | Exclusion constraint                                      |
     |-----------|---------------------|-----------------------------------------------------------|
     | scout     | scout-feasibility   |                                                           |
     | draft     | draft-spec          |                                                           |
     | review    | review-design       |                                                           |
     | flow      | flow-resilience     |                                                           |
     | trace     | trace-request       |                                                           |
     | prove     | prove-hypothesis    |                                                           |
     | listen    | listen-support      |                                                           |
     | program   | program-plan        |                                                           |
     | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

     Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

S-2  CATEGORY
     Assign CATEGORY:
       HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
         scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
         draft-pitch, review-design, review-code, trace-request, trace-component,
         trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
         flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
         flow-throttle, flow-trigger, flow-integration, program-plan
       EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
         listen-feedback, listen-support, listen-adoption
       MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

S-3  COMPUTE FLAG
     Compute FLAG as a named variable before header assembly.

     | CATEGORY                         | FLAG value                                                     |
     |----------------------------------|----------------------------------------------------------------|
     | HIGH-STRUCTURE (critical + T2+)  | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"|
     | HIGH-STRUCTURE (all other)       | "none (structural coverage reliable)"                          |
     | EVIDENCE-HEAVY                   | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)" |
     | MIXED                            | "REVIEW-FOR-PLAUSIBILITY"                                      |
     | Compliance override (any cat.)   | "REAL-REQUIRED (compliance-sensitive)"                         |

     Critical namespaces: trace-*, scout-feasibility, listen-*. Compliance override applies
     when compliance tags are present in TOPICS.md AND skill is scout-compliance or
     trace-permissions; override takes precedence over all other cases.

     FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
     branch, any fallback path, any regeneration sequence, or any other execution context,
     including paths that do not pass through prior steps in normal order. Every execution
     path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
     path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot
     be distinguished from a correctly-computed one.

     FLAG is resolved. Do not re-evaluate or modify it anywhere in this run.

A-1  HEADER
     The first rule of this step: copy FLAG from S-3 verbatim. Do not rederive it.
     This rule is first -- it applies before any field is listed, before any category
     lookup, before any formatting instruction, or any other instruction in this step.
     No instruction in A-1 precedes this rule. Every instruction in this step -- named or
     unnamed -- is governed by this rule. No instruction in this step is exempt.
     Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
     to downstream tooling and silently corrupts the artifact's trust tier. The artifact
     will carry an incorrect Flag field, downstream mock-review will flag the wrong
     namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
     header inspection.

     [MOCK ARTIFACT -- NOT VERIFIED]
     Skill: {skill-id}
     Topic: {topic}
     Category: {CATEGORY}
     Date: {today's date}
     Status: MOCK (awaiting review)
     Flag: {FLAG from S-3}

A-2  FIDELITY WARNING
     Write as the lead section of the artifact body (before mock content, after ---):

     | CATEGORY       | Block    | Required content                                       |
     |----------------|----------|--------------------------------------------------------|
     | EVIDENCE-HEAVY | WARNING  | Content fabricated; real run required                  |
     | MIXED          | CAUTION  | Structural reliable; specific claims may be wrong      |
     | HIGH-STRUCTURE | NOTE     | Structure reliable; Tier 1 adequate; REAL-REQUIRED     |
     |                |          | at Tier 2+ for critical namespaces                     |

A-3  ARTIFACT BODY
     Generate mock body following the golden rubric structure for the selected skill.
     All required sections, tables, gates, and enforcement mechanisms must be present.
     Generic prose fails.

A-4  WRITE
     Path: simulations/mock/{topic}-{namespace}-mock-{date}.md
     Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

A-5  NEXT STEP
     Final line: Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
     (Omit if called from within a mock-review session.)
```

---

## V-05 -- Full Convergence (all 24 criteria)

**Axis**: Role sequence -- convergent execution with all four R6/R7 protection layers
active simultaneously. Prose emphasis.
**Hypothesis**: C-23 and C-24 are mutually reinforcing with all prior layers. C-23 makes
the contamination consequence visible at the site where corruption originates (the compute
step), mirroring the role C-20 plays at the consumption site. C-24 converts the consumption-
site catch-all from a negative bound to a positive assertion of coverage, mirroring the role
C-21 plays at the compute site. Together they complete the structural symmetry between both
prohibition sites: each site now carries a five-level escalation chain (prohibition ->
run-scoped -> named classes/types -> affirmative closure/catch-all -> failure consequence/
no-exempt affirmative). Neither criterion is redundant; each closes a gap the others leave
open. Full convergence is the only variant that predicts 100 on v7 aspirational.
**Predicts**: All 24 criteria -- C-01 through C-24.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}         (required)
  Namespace: {namespace}     (required -- scout | draft | review | flow | trace |
                              prove | listen | program | topic)
  --skill    {skill-id}      (optional)
  --tier     1 | 2 | 3       (default: 1)

Single-pass. No prompts. One artifact. One next-step line.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line for the TOPICS.md result:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is specified: use it.
  - Otherwise, use the representative default from this table:

  | Namespace | Default skill       | Exclusion constraint                                      |
  |-----------|---------------------|-----------------------------------------------------------|
  | scout     | scout-feasibility   |                                                           |
  | draft     | draft-spec          |                                                           |
  | review    | review-design       |                                                           |
  | flow      | flow-resilience     |                                                           |
  | trace     | trace-request       |                                                           |
  | prove     | prove-hypothesis    |                                                           |
  | listen    | listen-support      |                                                           |
  | program   | program-plan        |                                                           |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. Do not modify it.

---

STEP S-3 -- COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, the guarantee stated above is broken: A-1 will
inherit a corrupted value that cannot be distinguished from a correctly-computed one,
producing the same silent category mismatch described at the consumption site.

Compute FLAG from CATEGORY and tier:

  Case 1 -- CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 -- CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 -- CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 -- CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override -- check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first -- it applies before any field is listed, before any category
lookup, before any formatting instruction, or any other instruction in this step.
No instruction in A-1 precedes this rule. Every instruction in this step -- named or
unnamed -- is governed by this rule. No instruction in this step is exempt.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The artifact
will carry an incorrect Flag field, downstream mock-review will flag the wrong
namespaces as REAL-REQUIRED, and the corruption is undetectable without manual
header inspection.

Assemble the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body. Position it
before any mock content. Separate from the header and from the body with ---
delimiters.

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or partially fabricated. Review
    for plausibility before accepting coverage.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning and coverage orientation at
    Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## Scoring prediction summary

| Variant | Axis | New criteria targeted | Denominator | Expected composite |
|---------|------|-----------------------|-------------|-------------------|
| V-01 | Inertia framing (compute-site consequence) | C-23 only | 16 | ~99.4 |
| V-02 | Phrasing register (consumption-side affirmative) | C-24 only | 16 | ~99.4 |
| V-03 | Lifecycle emphasis (R6 baseline) | none | 16 | ~98.8 |
| V-04 | Output format + role sequence (C-23 minimal + C-24 full) | C-23 + C-24 | 16 | 100 |
| V-05 | Full convergence (prose) | C-23 + C-24 | 16 | 100 |

**Key discriminants**:
- V-01 vs V-02: Isolates whether compute-site consequence (C-23) or consumption-site
  affirmative (C-24) is the stronger standalone addition.
- V-04 vs V-05: Tests whether minimal C-23 form (single-sentence consequence at S-3)
  satisfies the rubric as well as V-05's expanded form with explicit contamination
  mechanism naming. If V-04 scores 100, C-23 does not require extended elaboration.
- V-03 vs V-01/V-02: Confirms that C-23 and C-24 each add a measurable increment over
  the R6 baseline (if V-03 scores 98.8, each single-criterion addition adds ~0.3 points
  at the aspirational layer).
- V-04 vs V-03: Shows combined R7 gain over R6 baseline when both criteria are present.
