---
skill: quest-variate
skill_target: mock-ns
round: 5
rubric_version: 5
date: 2026-03-15
---

# mock-ns — Round 5 Variations

Rubric: v5 (C-01 through C-20, aspirational denominator 12).

New criteria in v5:
- **C-18** — Named path class enumeration at the compute site
- **C-19** — Anti-displacement closure at the consumption site
- **C-20** — Failure-consequence framing at the consumption site

Each variation is a **complete, runnable skill body prompt**. Single-axis variation
first (V-01 through V-04), then full convergence (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (formal/imperative, structured anti-displacement) | C-18 + C-19 without C-20 is sufficient to close the displacement gap. Named competitors + declarative closure anchors the rule without requiring a consequence statement. |
| V-02 | Inertia framing (path classes as the primary protection structure) | C-18 at the compute site is the highest-leverage single intervention. Conditional/fallback re-entry is the most common corruption path; naming it explicitly is more effective than downstream closure rules. |
| V-03 | Lifecycle emphasis (consequence framing at the right lifecycle position) | C-20 without C-19 breaks the inertia. Making the failure cost visible at the consumption site is more effective than naming competing instructions, because consequence visibility is the real pressure-response mechanism. |
| V-04 | Output format (table-structured baseline, C-16+C-17 only) | R3 high-water mark is sufficient. Run-scoped declaration + first-position placement together prevent FLAG corruption without additional specificity. |
| V-05 | Role sequence (convergent — all protection layers simultaneously) | C-18 + C-19 + C-20 are mutually reinforcing. Each layer closes a distinct gap; none is redundant. Full convergence is the only variant that scores 100 on aspirational. |

---

## V-01 — Anti-Displacement Closure

**Axis**: Phrasing register — formal/imperative with structured anti-displacement rules.
**Hypothesis**: Named competitor instructions + declarative closure (C-19) + path class
enumeration (C-18) close the displacement gap without a consequence statement (no C-20).
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19. Missing: C-20.
**Expected composite**: ~98.3 (11/12 aspirational, assuming C-09 and C-10 pass).

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

  | Namespace | Default skill       | Exclusion note                                      |
  |-----------|---------------------|-----------------------------------------------------|
  | scout     | scout-feasibility   | —                                                   |
  | draft     | draft-spec          | —                                                   |
  | review    | review-design       | —                                                   |
  | flow      | flow-resilience     | —                                                   |
  | trace     | trace-request       | —                                                   |
  | prove     | prove-hypothesis    | —                                                   |
  | listen    | listen-support      | —                                                   |
  | program   | program-plan        | —                                                   |
  | topic     | topic-plan          | Do NOT use topic-status (excluded — meta-structural)|

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 — DETERMINE CATEGORY

Look up the selected skill in the category registry:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

Assign CATEGORY = the matching value for the selected skill. No other value is valid.

---

STEP S-3 — COMPUTE FLAG

This step computes FLAG. FLAG is a named variable. It is computed exactly once, here.
FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order.

Compute FLAG from CATEGORY:
  - HIGH-STRUCTURE → FLAG = "none (structural coverage reliable)"
    Exception: if the skill is in a critical namespace (trace-*, scout-feasibility,
    or any listen-*) AND tier >= 2, then:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"
  - EVIDENCE-HEAVY → FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"
  - MIXED         → FLAG = "REVIEW-FOR-PLAUSIBILITY"
  - If compliance tags are present in TOPICS.md AND the skill is scout-compliance or
    trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)" regardless of category.

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 — ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.
This rule is first — it applies before any field is listed, before any category
lookup, before any formatting instruction in this step. No instruction in A-1
precedes this rule.

Assemble the MOCK ARTIFACT header block:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 — copied verbatim, not rederived}

The header appears immediately after any frontmatter. It precedes all body content.

---

STEP A-2 — FIDELITY WARNING

Write the category-appropriate fidelity warning as the first section of the
artifact body, separated from the header and body by --- delimiters.

  If EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made
    from this namespace.

  If MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data, research
    findings) may be partially accurate or partially fabricated. Review for plausibility
    before accepting coverage.

  If HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

---

STEP A-3 — GENERATE ARTIFACT BODY

Generate the mock artifact body following the golden rubric structure for the
selected skill. The output must include:
  - All required section headings for the skill
  - Required tables or lists in the correct positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in expected positions

A reader familiar with the real skill must be able to identify which skill was
mocked. Generic prose without skill-specific structure fails.

---

STEP A-4 — WRITE ARTIFACT

Write the artifact to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 — NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit this line only if this skill was called from within a mock-review session
to regenerate a thin namespace.
```

---

## V-02 — Path Class Enumeration

**Axis**: Inertia framing — path class names as the primary protection structure at
the compute site.
**Hypothesis**: Explicit path class enumeration at S-3 (C-18) is the highest-leverage
intervention. Conditional/fallback re-entry is the most common corruption source;
naming all path classes is more effective than downstream consumption-site rules.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18. Missing: C-19, C-20.
**Expected composite**: ~97.5 (11/12 aspirational, C-18 adds the enumeration; no
anti-displacement closure or consequence statement at A-1).

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required — scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional)
  --tier     1 | 2 | 3        (optional — default: 1)

Single-pass. No prompts.

---

STEP S-1 — SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock. If --skill is provided, use it. Otherwise use the
representative default:

  | Namespace | Default skill       | Exclusion constraint                                |
  |-----------|---------------------|-----------------------------------------------------|
  | scout     | scout-feasibility   |                                                     |
  | draft     | draft-spec          |                                                     |
  | review    | review-design       |                                                     |
  | flow      | flow-resilience     |                                                     |
  | trace     | trace-request       |                                                     |
  | prove     | prove-hypothesis    |                                                     |
  | listen    | listen-support      |                                                     |
  | program   | program-plan        |                                                     |
  | topic     | topic-plan          | topic-status is excluded (meta-structural). Do NOT  |
  |           |                     | use topic-status as a mock-ns default at any tier.  |

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

---

STEP S-3 — COMPUTE FLAG

FLAG is computed here, as a named variable, before any header assembly.

FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, or any regeneration sequence. This prohibition covers every
execution path, including paths that bypass the normal step order.

Compute FLAG from CATEGORY:
  - HIGH-STRUCTURE + critical namespace (trace-*, scout-feasibility, listen-*) + tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"
  - HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"
  - EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"
  - MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"
  - Compliance override (compliance tags present AND skill is scout-compliance or
    trace-permissions, any tier):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is resolved. Do not modify it after this emit.

---

STEP A-1 — ASSEMBLE HEADER

The first rule of this step: copy FLAG from S-3 verbatim. Do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG — verbatim from S-3}

---

STEP A-2 — FIDELITY WARNING

Write the fidelity warning as the first section of the artifact body (before mock
content, separated by --- delimiters):

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Structure is correct; content is
    fabricated. Do not use to draw conclusions about {topic}. A real {skill-id}
    run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements are reliable; specific
    claims may be partially fabricated. Review for plausibility.

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
    reliable. Content is synthetically generated. Adequate for Tier 1 structural
    planning. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
    scout-feasibility, listen).

---

STEP A-3 — GENERATE ARTIFACT BODY

Generate the mock body following the golden rubric structure for the selected skill.
Include all required headings, tables, gates, and enforcement mechanisms. The output
must be skill-specific — generic prose fails.

---

STEP A-4 — WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md
Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 — NEXT-STEP LINE

Final line of artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

(Omit if called from within a mock-review session to regenerate a thin namespace.)
```

---

## V-03 — Failure-Consequence Framing

**Axis**: Lifecycle emphasis — consequence statement at the consumption site,
positioned immediately after the first-rule prohibition.
**Hypothesis**: Naming the failure mechanism (C-20) without anti-displacement closure
(C-19) is more effective than closure without consequence. Consequence visibility is
the real pressure-response mechanism; an executor who knows what goes wrong will not
rederive FLAG even without an explicit instruction inventory.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-20. Missing: C-19.
**Expected composite**: ~97.5 (11/12 aspirational — C-19 absent means no anti-
displacement closure; C-18 and C-20 present).

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

  Namespace defaults:
    scout    → scout-feasibility
    draft    → draft-spec
    review   → review-design
    flow     → flow-resilience
    trace    → trace-request
    prove    → prove-hypothesis
    listen   → listen-support
    program  → program-plan
    topic    → topic-plan
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

FLAG is a named variable computed in this step. Compute it once.

FLAG MUST NOT be recomputed anywhere in this run — not in any step, any conditional
branch, any fallback path, or any regeneration sequence. Every execution path —
including paths that enter header assembly without passing through S-3 in normal
order — is covered by this prohibition.

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

RULE 1 — Do not compute a new FLAG value here. Copy FLAG from S-3 exactly as
emitted.
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

## V-04 — First-Rule Baseline (C-16 + C-17 only)

**Axis**: Output format — table-structured, concise. The R3 high-water mark: run-scoped
immutability at compute site, first-rule prioritization at consumption site. No new
v5 criteria. Baseline for scoring comparison.
**Hypothesis**: C-16 + C-17 is sufficient. Run-scoped declaration and first-position
placement together prevent FLAG corruption without additional path class enumeration,
anti-displacement closure, or consequence statements.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17. Missing: C-18, C-19, C-20.
**Expected composite**: ~97.5 (10/12 aspirational — C-16 and C-17 pass; C-18 C-19 C-20
all absent).

---

```
You are running /mock:ns for Signal.

INPUTS

| Input     | Value                                                                    |
|-----------|--------------------------------------------------------------------------|
| Topic     | {topic} (required)                                                       |
| Namespace | {namespace} (required): scout | draft | review | flow | trace | prove |   |
|           | listen | program | topic                                              |
| --skill   | {skill-id} (optional — default: representative skill)                    |
| --tier    | 1 | 2 | 3 (optional — default: 1)                                    |

Single-pass. No prompts.

---

PROCEDURE

S-1  SETUP
     Read TOPICS.md. Emit:
       > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

     Select the skill:

     | Namespace | Default         | Notes                                          |
     |-----------|-----------------|------------------------------------------------|
     | scout     | scout-feasibility |                                              |
     | draft     | draft-spec      |                                                |
     | review    | review-design   |                                                |
     | flow      | flow-resilience |                                                |
     | trace     | trace-request   |                                                |
     | prove     | prove-hypothesis|                                                |
     | listen    | listen-support  |                                                |
     | program   | program-plan    |                                                |
     | topic     | topic-plan      | Do NOT use topic-status (meta-structural)      |

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

     | CATEGORY        | FLAG value                                                     |
     |-----------------|----------------------------------------------------------------|
     | HIGH-STRUCTURE  | "none (structural coverage reliable)"                          |
     | HIGH-STRUCTURE, | "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"|
     | critical + T2+  |                                                                |
     | EVIDENCE-HEAVY  | "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)" |
     | MIXED           | "REVIEW-FOR-PLAUSIBILITY"                                      |
     | Compliance over-| "REAL-REQUIRED (compliance-sensitive)"                         |
     | ride (any cat.) |                                                                |

     FLAG is resolved. Do not re-evaluate or modify it in any subsequent step of this run.

A-1  HEADER
     The first rule of this step is: copy FLAG from S-3 verbatim. Do not rederive it.

     [MOCK ARTIFACT -- NOT VERIFIED]
     Skill: {skill-id}
     Topic: {topic}
     Category: {CATEGORY}
     Date: {today's date}
     Status: MOCK (awaiting review)
     Flag: {FLAG from S-3}

A-2  FIDELITY WARNING
     Write as the lead section of the artifact body (before mock content, after ---):

     | CATEGORY       | Warning type | Required content                                  |
     |----------------|--------------|---------------------------------------------------|
     | EVIDENCE-HEAVY | WARNING      | Content fabricated; real run required             |
     | MIXED          | CAUTION      | Structural reliable; specific claims may be wrong |
     | HIGH-STRUCTURE | NOTE         | Structure reliable; Tier 1 adequate; REAL-REQUIRED|
     |                |              | at Tier 2+ for critical namespaces                |

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

## V-05 — Full Convergence (C-18 + C-19 + C-20)

**Axis**: Role sequence — convergent execution with all three protection layers active
simultaneously.
**Hypothesis**: C-18 + C-19 + C-20 are mutually reinforcing. Path class enumeration (C-18)
prevents compute-site re-entry from non-linear paths. Anti-displacement closure (C-19)
anchors the first-rule position against adjacent instructions. Consequence framing (C-20)
makes the cost of any violation explicit at the moment the instruction is processed. No
layer is redundant; each closes a gap the others leave open.
**Predicts**: All 20 criteria — C-01 through C-20.
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
| V-01 | Phrasing register (anti-displacement closure) | C-18 + C-19 | ~98.3 |
| V-02 | Inertia framing (path class enumeration) | C-18 | ~97.5 |
| V-03 | Lifecycle emphasis (failure-consequence framing) | C-18 + C-20 | ~97.5 |
| V-04 | Output format (table-structured baseline) | none (C-16+C-17 only) | ~97.5 |
| V-05 | Role sequence (full convergence) | C-18 + C-19 + C-20 | 100 |

**Key discriminant**: V-01 vs V-05 isolates the value of C-20 (consequence statement).
V-02 vs V-01 isolates the value of C-19 (anti-displacement closure vs path class
enumeration alone). V-03 vs V-01 isolates C-19 vs C-20 as the stronger individual
criterion. V-04 is the R3 baseline; its score relative to V-02/V-03 confirms whether
path class enumeration or consequence framing adds more than the R3 stack alone.
