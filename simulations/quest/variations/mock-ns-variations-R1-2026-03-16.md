Now I have everything I need. Here are 5 complete, runnable prompt variations for **mock-ns**, targeting rubric v1 (C-01 through C-10).

---

# mock-ns — Round 1 Variations

**Rubric**: v1 (C-01 through C-10: 5 essential / 3 recommended / 2 aspirational)

**Round**: 1 — first variate pass. Single-axis for V-01 through V-03, one two-axis combination (V-04), full convergence (V-05).

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (conversational, descriptive) | A readable, prose-driven register with labeled phases covers C-01 through C-08. The lighter instruction weight predicts misses on C-09 (topic-status exclusion) and C-10 (compliance override) because neither is named as a case. |
| V-02 | Output format (table-centric lookups) | Encoding category assignment and flag computation as explicit lookup tables (not prose lists) reduces category/flag mismatch. C-02 and C-03 pass by row-match rather than scanning. C-09 passes if the exclusion constraint appears as a table note. C-10 predicts miss: compliance override is not naturally expressed as a table row in a minimal design. |
| V-03 | Lifecycle emphasis (TOPICS.md-first, compliance override as named case) | Promoting TOPICS.md consultation to the first named step with a dedicated emit line, and making the compliance override an explicit, named override case that runs last, directly targets C-06, C-09, and C-10. Hypothesis: all 10 criteria pass when setup is anchored to TOPICS.md and the compliance path is named. |
| V-04 | Phrasing register + lifecycle emphasis (conversational register + TOPICS.md anchor) | V-01's readable prose register combined with V-03's TOPICS.md-first setup and named compliance override. Predicts C-10 and C-09 passing without requiring table machinery. Two-axis test: can the conversational tone survive the structural precision required by C-09/C-10? |
| V-05 | Convergent (table format + TOPICS.md lifecycle + compliance + tier-conditional flag) | Full convergence: V-02 tables + V-03 lifecycle emphasis + explicit tier-conditional flag for HIGH-STRUCTURE critical skills (C-03 tier case) + compliance override named last in flag computation. Every criterion has a structural home. Predicts all 10 passing. |

---

## V-01 — Phrasing Register (Conversational)

**Axis**: Phrasing register — conversational, descriptive, imperative-light.
**Hypothesis**: A readable, phase-labeled format reaches C-01 through C-08 without heavy structural machinery. C-09 and C-10 likely miss: topic-status exclusion and compliance override are not named explicitly.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 uncertain / C-10 miss.
**Expected composite**: ~86.

---

```
You are running /mock:ns for Signal.

This skill creates a synthetic mock artifact for a single namespace. It is
single-pass -- no prompts, no back-and-forth. You receive a topic and a
namespace, produce one artifact, write it to disk, and stop.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove |
                            listen | program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional, default: 1)

---

Phase 1 -- Read context

Read TOPICS.md. Emit a status line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

---

Phase 2 -- Choose the skill

If --skill was provided, use it. Otherwise select the representative skill
for the namespace:

  scout   -> scout-feasibility      draft   -> draft-spec
  review  -> review-design          flow    -> flow-resilience
  trace   -> trace-request          prove   -> prove-hypothesis
  listen  -> listen-support         program -> program-plan
  topic   -> topic-plan

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

Phase 3 -- Assign the category

Find the selected skill in this registry. Every skill belongs to exactly one
category:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now determined for this run. Do not change it.

---

Phase 4 -- Compute the flag

Choose the Flag value based on the category:

  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

---

Phase 5 -- Write the artifact

Write the file to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Start with the header block (immediately first, before any body content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from Phase 3}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from Phase 4}

After the header, add the category-appropriate fidelity warning, separated by ---:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or
    partially fabricated. Review for plausibility before accepting coverage.

After the fidelity warning, generate the mock body. Follow the exact structural
pattern of the selected skill:
  - Use the correct section headings for that skill
  - Include required tables or scored lists in their expected positions
  - Include a gate or verdict line where the real skill produces one
  - Place enforcement mechanisms in their expected positions
  - A reader familiar with the real skill must recognize which skill was mocked

Use {topic} as the subject throughout the body content.

---

Phase 6 -- Finalize

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-02 — Output Format (Table-Centric Lookups)

**Axis**: Output format — all lookup and decision logic expressed as tables.
**Hypothesis**: Row-match tables for skill selection, category registry, and flag computation reduce mismatch errors on C-02 and C-03. The topic exclusion note in the skill-selection table surfaces C-09. C-10 predicts miss: compliance override is not a natural table row in this minimal form.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 pass / C-10 miss.
**Expected composite**: ~93.

---

```
You are running /mock:ns for Signal. Single-pass. No prompts.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove |
                            listen | program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional, default: 1)

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

---

STEP S-2 -- SKILL SELECTION

If --skill is provided, use it. Otherwise look up namespace in this table:

  | Namespace | Default skill     | Constraint                                   |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | topic-status is EXCLUDED (meta-structural)   |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-3 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Included skills                                                 |
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

CATEGORY = matched row label. Do not modify CATEGORY after this step.

---

STEP S-4 -- FLAG COMPUTATION

Look up CATEGORY in this table:

  | Category       | Flag value                                                      |
  |----------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | none (structural coverage reliable)                             |
  | EVIDENCE-HEAVY | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | MIXED          | REVIEW-FOR-PLAUSIBILITY                                         |

FLAG = matched row value. Do not modify FLAG after this step.

---

STEP S-5 -- ARTIFACT CONSTRUCTION

Write to: simulations/mock/{topic}-{namespace}-mock-{date}.md

1. MOCK ARTIFACT header block (first, before all body content):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id from S-2}
   Topic: {topic}
   Category: {CATEGORY from S-3}
   Date: {today's date}
   Status: MOCK (awaiting review)
   Flag: {FLAG from S-4}

2. Fidelity warning (immediately after header, separated by ---):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
     reliable. Content is synthetically generated but structurally representative.
     Adequate for Tier 1 structural planning. REAL-REQUIRED at Tier 2+ for critical
     namespaces (trace-*, scout-feasibility, listen-*).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
     evidentially fabricated. Do not draw conclusions about {topic} from this output.
     A real {skill-id} run is required before any evidence-based decision.

   MIXED:
     CAUTION: This is a MIXED mock. Tables and gates are reliable. Specific claims
     may be partially fabricated. Review for plausibility.

3. Mock body (after fidelity warning):

   Follow the structural pattern of {skill-id} exactly:
   - Correct section headings for that skill
   - Required tables, scored lists, and gate/verdict lines in expected positions
   - Enforcement mechanisms in their expected positions
   - A reader familiar with {skill-id} must recognize the structure from headings alone
   Content uses {topic} as subject. All values are synthetic.

---

STEP S-6 -- COMPLETION

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

Final line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-03 — Lifecycle Emphasis (TOPICS.md-First + Named Compliance Override)

**Axis**: Lifecycle emphasis — TOPICS.md consultation is the structural anchor of the entire run; compliance override is an explicit, named final case in flag computation.
**Hypothesis**: Making TOPICS.md a named first step with dedicated emit wires C-06. Naming the compliance override as a distinct case that runs after all other flag cases wires C-10. Naming the topic-status exclusion as a constraint in skill selection wires C-09. Predicts all 10 criteria passing.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 all pass.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

---

STEP S-1 -- SETUP: READ TOPICS.md

Read TOPICS.md. This step runs before all others. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Record tier and compliance tags. They are used in S-3 flag computation.
Do not proceed until this emit line is written.

---

STEP S-2 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the default skill:

  | Namespace | Default skill       | Exclusion constraint                              |
  |-----------|---------------------|---------------------------------------------------|
  | scout     | scout-feasibility   |                                                   |
  | draft     | draft-spec          |                                                   |
  | review    | review-design       |                                                   |
  | flow      | flow-resilience     |                                                   |
  | trace     | trace-request       |                                                   |
  | prove     | prove-hypothesis    |                                                   |
  | listen    | listen-support      |                                                   |
  | program   | program-plan        |                                                   |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural,      |
  |           |                     | never a default skill                             |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-3 -- CATEGORY AND FLAG

Assign CATEGORY for the selected skill:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

Compute FLAG from CATEGORY and tier using these cases in order:

  Case A -- HIGH-STRUCTURE, critical skill (trace-*, scout-feasibility, listen-*),
            tier >= 2:
    FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  Case B -- HIGH-STRUCTURE (all other cases):
    FLAG = "none (structural coverage reliable)"

  Case C -- EVIDENCE-HEAVY:
    FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  Case D -- MIXED:
    FLAG = "REVIEW-FOR-PLAUSIBILITY"

  Compliance override (apply last, overrides any case above):
    If compliance tags are present AND selected skill is scout-compliance or
    trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is resolved after this step. Do not recompute it.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block (immediately first in the artifact, before all body content):

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-2}
  Topic: {topic}
  Category: {CATEGORY from S-3}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- copy verbatim, do not rederive}

All six fields are required. No field may be blank.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---:

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
    Tier 2+ for critical namespaces (trace-*, scout-feasibility, listen-*).

---

STEP A-3 -- MOCK BODY

Generate the artifact body following the structural pattern of the selected skill:
  - All required section headings for that skill
  - Required tables or lists in their expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in their expected positions

A reader familiar with the real skill must be able to identify which skill was mocked
from the section headings and tables alone. Generic prose without skill-specific
structure fails.

Use {topic} as the subject throughout. All values are synthetic.

---

STEP A-4 -- WRITE AND CLOSE

Write the complete artifact to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to
regenerate a thin namespace.
```

---

## V-04 — Phrasing Register + Lifecycle Emphasis (Conversational + TOPICS.md Anchor)

**Axis**: Two-axis — V-01's conversational register + V-03's TOPICS.md-first lifecycle and named compliance override.
**Hypothesis**: Readable prose tone survives structural precision when TOPICS.md consultation and compliance override are given explicit, named homes. The register keeps instructions human-scannable while the structural hooks ensure C-09 and C-10 pass.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 all pass.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

This skill generates a single mock artifact for one namespace. It is
single-pass -- no prompts, no iterations. Read context, choose a skill,
assign category and flag, write the artifact, done.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove |
                            listen | program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional, default: 1)

---

Phase 1 -- Read context first

Before anything else, read TOPICS.md. Emit this line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Note any compliance tags and the tier -- they affect the flag value in Phase 3.

---

Phase 2 -- Choose the skill

If --skill was provided, use it. Otherwise pick the representative default
for the namespace. One constraint: for the topic namespace, the default is
always topic-plan. topic-status is excluded -- it is meta-structural and
is never the default.

  scout     -> scout-feasibility     draft   -> draft-spec
  review    -> review-design         flow    -> flow-resilience
  trace     -> trace-request         prove   -> prove-hypothesis
  listen    -> listen-support        program -> program-plan
  topic     -> topic-plan  (never topic-status)

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

Phase 3 -- Assign category, then compute flag

Assign the CATEGORY for the chosen skill:

  HIGH-STRUCTURE skills produce reliable structure but synthetic content:
    scout-feasibility, scout-stakeholders, scout-requirements, scout-naming,
    scout-compliance, scout-market, draft-spec, draft-proposal, draft-pitch,
    review-design, review-code, trace-request, trace-component, trace-contract,
    trace-state, trace-skill, trace-migration, trace-deployment, flow-resilience,
    flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle, flow-trigger,
    flow-integration, program-plan

  EVIDENCE-HEAVY skills require a real run before evidence-based decisions:
    prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED skills produce reliable structure but claims need plausibility review:
    scout-competitors, prove-hypothesis, review-customers, review-users

Now compute FLAG from CATEGORY, using this logic in order:

  1. HIGH-STRUCTURE, AND the skill is a critical one (trace-*, scout-feasibility,
     or listen-*), AND tier is 2 or 3:
       FLAG = "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"

  2. HIGH-STRUCTURE in all other cases:
       FLAG = "none (structural coverage reliable)"

  3. EVIDENCE-HEAVY:
       FLAG = "REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)"

  4. MIXED:
       FLAG = "REVIEW-FOR-PLAUSIBILITY"

  5. Compliance override -- check this last, regardless of category or tier:
     If compliance tags are present in TOPICS.md AND the selected skill is
     scout-compliance or trace-permissions:
       FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is set. Do not change it.

---

Phase 4 -- Write the artifact

Write to: simulations/mock/{topic}-{namespace}-mock-{date}.md

Open with the MOCK ARTIFACT header. All six fields are required:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {CATEGORY from Phase 3}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from Phase 3}

After the header (separated by ---), write the fidelity warning:

  For HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace-*, scout-feasibility, listen-*).

  For EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. A real {skill-id} run is required before any evidence-based
    decision can be made from this namespace.

  For MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or
    partially fabricated. Review for plausibility before accepting coverage.

After the fidelity warning, generate the mock body. It must follow the exact
structural pattern of the selected skill -- correct section headings, required
tables or scored lists in expected positions, gate or verdict line where the
real skill produces one, enforcement mechanisms in expected positions. A reader
familiar with the real skill must recognize which skill was mocked from the
headings and tables alone.

Use {topic} as subject throughout. All content is synthetic.

---

Phase 5 -- Finalize

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

End the artifact with:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## V-05 — Convergent (Tables + TOPICS.md Lifecycle + Tier-Conditional Flag + Compliance Override)

**Axis**: Full convergence — V-02 table-centric lookups + V-03 lifecycle emphasis with TOPICS.md as structural anchor + explicit tier-conditional flag case for HIGH-STRUCTURE critical skills + compliance override as a named terminal case.
**Hypothesis**: Every criterion has an unambiguous structural home. C-01: header template. C-02: S-3 category table. C-03: S-4 flag table with tier branch and compliance override. C-04: A-2 fidelity warning. C-05: A-3 body instructions. C-06: S-1 emit. C-07: A-4 path and emit. C-08: A-4 next-step. C-09: S-2 exclusion constraint. C-10: S-4 compliance override case. All 10 pass.
**Predicts**: All 10 criteria pass. Composite: 100.

---

```
You are running /mock:ns for Signal.

SINGLE-PASS. NO PROMPTS. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line before any other output:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Record: tier, compliance tags. Both are inputs to STEP S-4.

---

STEP S-2 -- SKILL SELECTION

If --skill is provided, use it. Otherwise consult this table:

  | Namespace | Default skill       | Exclusion constraint                              |
  |-----------|---------------------|---------------------------------------------------|
  | scout     | scout-feasibility   |                                                   |
  | draft     | draft-spec          |                                                   |
  | review    | review-design       |                                                   |
  | flow      | flow-resilience     |                                                   |
  | trace     | trace-request       |                                                   |
  | prove     | prove-hypothesis    |                                                   |
  | listen    | listen-support      |                                                   |
  | program   | program-plan        |                                                   |
  | topic     | topic-plan          | topic-status is EXCLUDED -- meta-structural,      |
  |           |                     | never a default skill                             |

Emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-3 -- CATEGORY ASSIGNMENT

Find the selected skill in exactly one row of this table:

  | Category       | Included skills                                                 |
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

CATEGORY = matched row label. Do not modify CATEGORY after this step.

---

STEP S-4 -- FLAG COMPUTATION

Evaluate the following cases in order. The first matching case sets FLAG.
Apply the compliance override last, after all cases, regardless of which
case fired.

  | Case | Condition                                                      | FLAG value                                                   |
  |------|----------------------------------------------------------------|--------------------------------------------------------------|
  | A    | HIGH-STRUCTURE AND skill is trace-*, scout-feasibility, or    | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)|
  |      | any listen-* AND tier >= 2                                     |                                                              |
  | B    | HIGH-STRUCTURE (all other)                                     | none (structural coverage reliable)                          |
  | C    | EVIDENCE-HEAVY                                                 | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed) |
  | D    | MIXED                                                          | REVIEW-FOR-PLAUSIBILITY                                      |

  Compliance override (runs after Cases A through D):
    If compliance tags are present in TOPICS.md AND skill is scout-compliance
    or trace-permissions (any tier, any category):
    FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is resolved. Do not recompute it anywhere in this run.

---

STEP A-1 -- HEADER BLOCK

Write the header block first in the artifact, before any body content:

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-2}
  Topic: {topic}
  Category: {CATEGORY from S-3}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-4 -- copy verbatim, do not rederive}

All six fields are required. No field may be blank.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---,
before any body content. Select by CATEGORY:

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
    Tier 2+ for critical namespaces (trace-*, scout-feasibility, listen-*).

---

STEP A-3 -- ARTIFACT BODY

Generate the mock body following the structural pattern of the selected skill.
The body must include:
  - All required section headings for the skill
  - Required tables or scored lists in their expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in their expected positions

A reader familiar with the real skill must be able to identify which skill was
mocked from the section headings and tables alone. Generic prose without
skill-specific structure fails this criterion.

Use {topic} as the subject throughout. All values are synthetic.

---

STEP A-4 -- WRITE AND CLOSE

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit: > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to
regenerate a thin namespace.
```

---

## Summary Table

| Variation | Primary axis | Secondary axis | C-01–C-05 | C-06–C-08 | C-09 | C-10 | Expected composite |
|-----------|-------------|----------------|-----------|-----------|------|------|--------------------|
| V-01 | Phrasing register (conversational) | — | pass | pass | uncertain | miss | ~86 |
| V-02 | Output format (table-centric) | — | pass | pass | pass | miss | ~93 |
| V-03 | Lifecycle emphasis (TOPICS.md-first + compliance) | — | pass | pass | pass | pass | 100 |
| V-04 | Phrasing register (conversational) | Lifecycle emphasis | pass | pass | pass | pass | 100 |
| V-05 | Output format (tables) | Lifecycle + compliance | pass | pass | pass | pass | 100 |

**Single-axis findings to test**:
- V-01 vs V-02: does table format alone improve C-02/C-03 accuracy versus prose?
- V-03 alone vs V-04: can compliance override survive in conversational register?
- V-02 vs V-05: does adding TOPICS.md lifecycle to table format push C-10 over the line?
