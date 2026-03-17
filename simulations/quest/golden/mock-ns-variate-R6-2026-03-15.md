---
skill: quest-variate
skill_target: mock-ns
round: 6
rubric_version: 6
date: 2026-03-15
---

# mock-ns — Round 6 Variations

Rubric: v6 (C-01 through C-22, aspirational denominator 14).

New criteria in v6:
- **C-21** — No-exemption affirmative closure at the compute site (depends on C-18)
- **C-22** — Catch-all instruction clause in the anti-displacement closure (depends on C-19)

R5 V-05 already carried C-21 language ("Every execution path that reaches A-1 carries the
FLAG value emitted here. No path is exempt.") but lacked C-22. R6 closes both gaps.

Each variation is a **complete, runnable skill body prompt**. Single-axis variation
first (V-01 through V-03), then combined axes (V-04, V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (C-22 only, formal/imperative catch-all at consumption site) | C-22 closes the residual anti-displacement gap in V-01 from R5. Naming only three canonical instruction types left the closure open to unrecognized types; adding "or any other instruction in this step" makes it exhaustive by construction. C-21 at the compute site is unnecessary because C-18 + catch-all path clause already achieves practical exhaustiveness there. |
| V-02 | Inertia framing (C-21 only, affirmative closure as primary compute-site protection) | C-21 is the higher-leverage criterion. The affirmative closure converts the prohibition from an enumeration (which can be read as illustrative) to a positive assertion of exhaustiveness. Compute-site exhaustiveness prevents FLAG corruption before header assembly begins; consumption-side catch-all (C-22) adds language complexity for a failure that C-21 already forecloses. |
| V-03 | Lifecycle emphasis (R5 high-water baseline, neither C-21 nor C-22) | R5 full convergence (C-01 through C-20) is already sufficient. C-18 + catch-all path clause at the compute site and C-19 three-type anti-displacement closure at the consumption site together achieve practical exhaustiveness. Adding C-21 and C-22 introduces verbose assertions over gaps that are operationally negligible. |
| V-04 | Role sequence + output format (both C-21 and C-22, table-structured) | C-21 and C-22 are independent structural completions -- C-21 closes the compute-site exhaustiveness gap; C-22 closes the consumption-site instruction-type gap. Table-structuring the anti-displacement clause (C-22) makes the catch-all visually undeniable rather than a tail clause a reader might skip. |
| V-05 | Full convergence (all 22 criteria, prose emphasis) | C-21 and C-22 are mutually reinforcing with all prior layers. C-21 forecloses the "enumeration-as-illustrative" reading at the compute site; C-22 forecloses the "unnamed-instruction-type" loophole at the consumption site. Neither is redundant. Full convergence is the only variant that predicts 100 on v6 aspirational. |

---

## V-01 — Consumption-Side Catch-All

**Axis**: Phrasing register — formal/imperative. Adds C-22 (catch-all instruction clause
at consumption site). Intentionally omits C-21 (no affirmative closure at compute site).
**Hypothesis**: C-22 closes the gap V-01 from R5 left open at A-1. The anti-displacement
closure named three canonical instruction types (C-19) but a future or unrecognized
instruction type could still displace the FLAG prohibition. Adding "or any other instruction
in this step" makes the coverage exhaustive by construction, without requiring an affirmative
closure assertion at the compute site.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-22. Missing: C-21.
**Expected composite**: 13/14 aspirational = ~99.3

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required — scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional — default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional — default: 1)

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

---

STEP S-1 — SETUP

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
  | topic     | topic-plan          | topic-status is EXCLUDED — meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 — DETERMINE CATEGORY

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

STEP S-3 — COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order.

Compute FLAG from CATEGORY and tier:

  Case 1 — CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 — CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 — CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 — CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override — check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 — ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first — it applies before any field is listed, before any category
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
  Flag: {FLAG from S-3 — copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 — FIDELITY WARNING

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

STEP A-3 — GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 — WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 — NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-02 — Compute-Site Affirmative Closure

**Axis**: Inertia framing — affirmative closure as primary compute-site protection.
Adds C-21 (positive-obligation statement + no-exemption statement at compute site).
Intentionally omits C-22 (no catch-all for instruction types at consumption site).
**Hypothesis**: C-21 is the stronger criterion for Round 6. An enumeration of path
classes — even one with a catch-all clause ("or any other execution context") — can
still be read as illustrative. The affirmative closure converts the prohibition from
a list to a positive assertion: exhaustiveness is a stated fact, not inferred from
the list's length. Compute-site exhaustiveness prevents FLAG corruption before header
assembly begins; by the time execution reaches A-1 the FLAG is already a settled fact.
C-22 (instruction-type catch-all) adds verbosity at the consumption site for a failure
mode that C-21 already forecloses upstream.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21. Missing: C-22.
**Expected composite**: 13/14 aspirational = ~99.3

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required — scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional — default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional — default: 1)

Single-pass. No prompts.

---

STEP S-1 — SETUP

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
  | topic     | topic-plan          | topic-status is EXCLUDED — meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 — DETERMINE CATEGORY

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

STEP S-3 — COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt.

Compute FLAG from CATEGORY and tier:

  Case 1 — CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 — CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 — CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 — CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override — check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 — ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first — it applies before any field is listed, before any category
lookup, before any formatting instruction in this step. No instruction in A-1
precedes this rule.
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
  Flag: {FLAG from S-3 — copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 — FIDELITY WARNING

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

STEP A-3 — GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 — WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 — NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-03 — R5 High-Water Baseline (Lifecycle Emphasis)

**Axis**: Lifecycle emphasis — explicit compute/assembly phase boundaries. Neither C-21
nor C-22 is present. Maximally concise within each phase. Serves as the R6 control.
**Hypothesis**: R5 full convergence (C-01 through C-20) is already sufficient. The compute
phase protection (C-16 + C-18 with catch-all path clause) and assembly phase protection
(C-17 + C-19 three-type anti-displacement + C-20 consequence) together achieve practical
exhaustiveness. C-21 and C-22 assert exhaustiveness in language but do not close
operationally distinct failure modes beyond what C-18 and C-19 already cover. The
lifecycle phase labeling makes each boundary explicit without adding new prohibition text.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20. Missing: C-21, C-22.
**Expected composite**: 12/14 aspirational = ~98.6

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

== COMPUTE PHASE ==

S-1. SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Determine the skill to mock.
  If --skill is specified, use it.
  Otherwise, apply the namespace default:

  Namespace defaults:
    scout    -> scout-feasibility
    draft    -> draft-spec
    review   -> review-design
    flow     -> flow-resilience
    trace    -> trace-request
    prove    -> prove-hypothesis
    listen   -> listen-support
    program  -> program-plan
    topic    -> topic-plan
               (topic-status is excluded as meta-structural; never use it as
                the mock-ns default, even if it appears first alphabetically)

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

FLAG is a named variable computed in this step, before any header assembly.

FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order.

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
  or trace-permissions, any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not modify FLAG after this step.

== END COMPUTE PHASE ==

---

== ASSEMBLY PHASE ==

A-1. ASSEMBLE HEADER

RULE 1 — Do not compute a new FLAG value here. Copy FLAG from S-3 exactly as
emitted.
This rule is first — it applies before any field is listed, before any category
lookup, before any formatting instruction in this step. No instruction in A-1
precedes this rule.
Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
to downstream tooling and silently corrupts the artifact's trust tier. The failure
cannot be caught by automated review because the header category and flag fields
are not cross-checked by any downstream process other than mock-review, which may
not run before the artifact is consumed.

Build the header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 — do not rederive}

Place immediately after frontmatter, before all body content.

---

A-2. FIDELITY WARNING

Write the fidelity warning as the lead section of the artifact body, before mock
content, delimited by ---:

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

== END ASSEMBLY PHASE ==
```

---

## V-04 — Table-Structured Both (C-21 + C-22, Role Sequence + Output Format)

**Axis**: Role sequence + output format (combination). Both C-21 and C-22 present.
Table-structured procedure with a dedicated anti-displacement table for C-22. C-21
affirmative closure appears as a named row following the FLAG computation table.
**Hypothesis**: C-21 and C-22 are independent closures for distinct structural gaps.
Table-structuring the anti-displacement rule at A-1 (C-22) makes the instruction-type
catch-all visually undeniable: a reader who skips prose may still process a table row
labeled "ANY OTHER INSTRUCTION -- NO." The affirmative closure at S-3 (C-21) gains
strength when placed as an explicit named assertion following the FLAG computation table
rather than embedded in a prohibition run-on sentence. Role sequence: the no-exemption
statement is the final stand-alone line of S-3, not a tail clause -- visual separation
reinforces its status as an assertion, not an afterthought.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22.
**Expected composite**: 14/14 aspirational = 100

---

```
You are running /mock:ns for Signal.

INPUTS

| Input     | Value                                                                    |
|-----------|--------------------------------------------------------------------------|
| Topic     | {topic} (required)                                                       |
| Namespace | {namespace} (required): scout | draft | review | flow | trace | prove |  |
|           | listen | program | topic                                              |
| --skill   | {skill-id} (optional -- default: representative skill)                   |
| --tier    | 1 | 2 | 3 (optional -- default: 1)                                    |

Single-pass. No prompts.

---

PROCEDURE

S-1  SETUP
     Read TOPICS.md. Emit:
       > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

     Select the skill:

     | Namespace | Default           | Exclusion constraint                             |
     |-----------|-------------------|--------------------------------------------------|
     | scout     | scout-feasibility |                                                  |
     | draft     | draft-spec        |                                                  |
     | review    | review-design     |                                                  |
     | flow      | flow-resilience   |                                                  |
     | trace     | trace-request     |                                                  |
     | prove     | prove-hypothesis  |                                                  |
     | listen    | listen-support    |                                                  |
     | program   | program-plan      |                                                  |
     | topic     | topic-plan        | Do NOT use topic-status (meta-structural, excl.) |

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
     Compute FLAG as a named variable, exactly once, before header assembly.

     | CATEGORY        | Tier / skill condition               | FLAG value                                                     |
     |-----------------|--------------------------------------|----------------------------------------------------------------|
     | HIGH-STRUCTURE  | critical (trace-*, scout-feas., list.)| "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"|
     |                 | + tier >= 2                          |                                                                |
     | HIGH-STRUCTURE  | all other cases                      | "none (structural coverage reliable)"                          |
     | EVIDENCE-HEAVY  | --                                   | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)" |
     | MIXED           | --                                   | "REVIEW-FOR-PLAUSIBILITY"                                      |
     | Compliance      | scout-compliance or trace-permissions| "REAL-REQUIRED (compliance-sensitive)"                         |
     | override        | any tier, any category               |                                                                |

     Prohibition: FLAG MUST NOT be recomputed anywhere in this run -- not in any step,
     any conditional branch, any fallback path, any regeneration sequence, or any other
     execution context, including paths that bypass normal step order.

     Affirmative closure: Every execution path that reaches A-1 carries the FLAG value
     computed in this step.
     No path is exempt.

A-1  HEADER ASSEMBLY
     The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.

     Anti-displacement — this rule precedes all of the following without exception:

     | Instruction type              | May precede this rule? |
     |-------------------------------|------------------------|
     | Field listing                 | NO                     |
     | Category lookup               | NO                     |
     | Formatting instructions       | NO                     |
     | Any other instruction in A-1  | NO                     |

     No instruction in A-1 precedes this rule.
     Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible
     to downstream tooling and silently corrupts the artifact's trust tier.

     [MOCK ARTIFACT -- NOT VERIFIED]
     Skill: {skill-id}
     Topic: {topic}
     Category: {CATEGORY}
     Date: {today's date}
     Status: MOCK (awaiting review)
     Flag: {FLAG from S-3}

A-2  FIDELITY WARNING
     Write as the lead section of the artifact body (before mock content, after ---):

     | CATEGORY       | Warning type | Required content                                            |
     |----------------|--------------|-------------------------------------------------------------|
     | EVIDENCE-HEAVY | WARNING      | Content fabricated; real run required before any decision   |
     | MIXED          | CAUTION      | Structural reliable; specific claims may be partially wrong |
     | HIGH-STRUCTURE | NOTE         | Structure reliable; Tier 1 adequate; REAL-REQUIRED at       |
     |                |              | Tier 2+ for critical namespaces                             |

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

## V-05 — Full R6 Convergence

**Axis**: Full convergence — all 22 criteria simultaneously, prose emphasis. Both C-21
and C-22 present, with each positioned to maximize the density of its structural signal.
**Hypothesis**: C-21 and C-22 are mutually reinforcing layers that close distinct gaps.
C-21 forecloses the "enumeration-as-illustrative" reading at the compute site — even a
path-class catch-all can be read as a list of examples; the affirmative closure asserts
exhaustiveness as a positive fact and states explicitly that no path is exempt. C-22
forecloses the "unnamed-instruction-type" loophole at the consumption site — an executor
encountering a new instruction type not in the named list may not recognize it as subject
to the anti-displacement prohibition; the catch-all eliminates this by making coverage
exhaustive by construction. Neither layer is redundant: C-21 defends the compute site
against interpretive slippage; C-22 defends the consumption site against future revision
pressure. Full convergence is the only variant that predicts 100 on the v6 aspirational
criteria.
**Predicts**: All 22 criteria — C-01 through C-22.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}         (required)
  Namespace: {namespace}     (required — scout | draft | review | flow | trace |
                              prove | listen | program | topic)
  --skill    {skill-id}      (optional)
  --tier     1 | 2 | 3       (default: 1)

Single-pass. No prompts. One artifact. One next-step line.

---

STEP S-1 — SETUP

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
  | topic     | topic-plan          | topic-status is EXCLUDED — meta-structural, never default |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 — DETERMINE CATEGORY

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

STEP S-3 — COMPUTE FLAG

FLAG is computed exactly once in this step. It is a named variable.

FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt.

Compute FLAG from CATEGORY and tier:

  Case 1 — CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility,
            any listen-*) AND tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case 2 — CATEGORY = HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case 3 — CATEGORY = EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case 4 — CATEGORY = MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override — check last, applied regardless of case above:
    If compliance tags are present in TOPICS.md AND skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 — ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first — it applies before any field is listed, before any category
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
  Flag: {FLAG from S-3 — copied verbatim, not rederived}

The header appears immediately after any frontmatter. All six fields are present.
The header precedes all body content.

---

STEP A-2 — FIDELITY WARNING

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

STEP A-3 — GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 — WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 — NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## Scoring prediction summary

| Variant | Axis | New criteria targeted | Expected composite |
|---------|------|-----------------------|--------------------|
| V-01 | Phrasing register (catch-all at consumption site) | C-22 | ~99.3 |
| V-02 | Inertia framing (affirmative closure at compute site) | C-21 | ~99.3 |
| V-03 | Lifecycle emphasis (R5 baseline, phase labels) | none | ~98.6 |
| V-04 | Role sequence + output format (table-structured both) | C-21 + C-22 | 100 |
| V-05 | Full convergence (all 22 criteria, prose) | C-21 + C-22 | 100 |

**Key discriminants**:
- V-01 vs V-02 isolates the relative value of C-22 vs C-21 as independent closures.
- V-03 is the control: confirms whether R5 full convergence (C-01 through C-20) already
  achieves practical exhaustiveness, or whether C-21 and C-22 add measurable protection.
- V-04 vs V-05 isolates structural presentation: does table-formatting the anti-displacement
  clause (C-22) produce a higher-fidelity execution trace than prose?
- V-01 + V-02 together test the asymmetry hypothesis: is compute-site exhaustiveness
  (C-21) more operationally critical than consumption-site instruction-type coverage
  (C-22), or vice versa?
