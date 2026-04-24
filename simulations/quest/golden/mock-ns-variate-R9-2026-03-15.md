---
skill: quest-variate
skill_target: mock-ns
round: 9
rubric_version: 8
date: 2026-03-15
---

# mock-ns -- Round 9 Variations

Rubric: v8 (C-01 through C-26, aspirational denominator 18).

No new criteria in R9. Rubric v8 is complete.

R8 V-04 (table-structured S-3, minimal form) and V-05 (prose, full emphasis) both achieved
full convergence at 100. The compute-site chain is six layers (C-14, C-16, C-18, C-21, C-23,
C-25, C-26) and the consumption-site chain is five layers (C-14, C-17, C-19, C-20, C-22, C-24).

R9 shifts the question from "which criteria to add" to "which structural form is most robust
under execution pressure." All five variants target full convergence on v8. The discriminant
is not coverage -- it is whether structural choices (register, format, ordering, step
topology, auditability) change how reliably an executor follows the six-layer compute chain
and five-layer consumption chain.

The three single-axis variants (V-01 through V-03) each test one structural property.
V-03 is the exception: consequence-first ordering at S-3 is structurally incompatible with
C-25 (guarantee-break framing requires the C-21 affirmative closure to be stated before the
consequence, so the phrase "the guarantee stated above is broken" has a referent), making
V-03 a deliberate test of whether consequence-first framing is worth the C-25 loss.
V-04 and V-05 combine axes for full convergence.

Each variation is a **complete, runnable skill body prompt** -- not a diff.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (first-person "you" address throughout) | Personalized executor framing -- "You MUST NOT recompute FLAG" vs "FLAG MUST NOT be recomputed" -- creates a tighter binding between the instruction and the executor's attention. The prohibition is no longer a system-level rule the executor observes; it is a direct command addressed to the specific executor running this step. Under pressure, first-person commands are harder to mentally background than third-person prohibitions. All 26 criteria carry identical content but in "you will" register throughout. |
| V-02 | Output format (tabular prohibition blocks at both sites) | Tables are processed row-by-row and cannot be skimmed the way prose paragraphs can. The six compute-site protection layers and five consumption-site protection layers expressed as labeled-row tables force each layer into an explicit cell -- an executor cannot read past the GUARANTEE-BREAK or CROSS-SITE rows without encountering them as distinct entries. Prose paragraphs allow the final clauses to blend into the body; tables surface each clause as an individually scannable item. |
| V-03 | Inertia framing (consequence-before-prohibition at S-3) | Leading S-3 with the failure consequence before stating the prohibition gives an executor under pressure the cost of violation as the first thing they read. Current order: state prohibition, then consequence -- an executor who skims the first sentence gets the rule. Inverted order: state consequence, then prohibition -- an executor who skims the first sentence gets the cost. The inverted order makes the "why not" visible before the "do not." Trade-off: C-25 (guarantee-break framing) is structurally incompatible with consequence-first ordering -- "the guarantee stated above is broken" cannot reference a guarantee not yet stated. C-25 is intentionally absent in V-03. Isolates whether C-25's causal bridge is the load-bearing mechanism, or whether the consequence's visibility (position and content) is what matters. |
| V-04 | Role sequence + Lifecycle emphasis (merged CLASSIFY-AND-FLAG step + procedure overview) | Merging S-2 (category) and S-3 (flag) into a single CLASSIFY-AND-FLAG step eliminates the inter-step gap where CATEGORY exists as a resolved variable but FLAG does not yet exist. During that gap, the pressure to rederive FLAG at A-1 is highest because FLAG has not yet been explicitly named as a resolved variable. Collapsing both assignments into one step ensures that CATEGORY and FLAG resolve simultaneously, removing the gap. The procedure overview at the top of the prompt gives the executor a structural map before any instruction is processed, reducing the chance that later steps are treated as lower priority. |
| V-05 | Full convergence + explicit protection chain audit at S-3 close | All 26 criteria in standard prose form, with S-3 ending in a numbered six-layer protection chain summary that names each layer by criterion and confirms it has been stated. The audit makes the compute-site chain structure explicit and navigable: an executor who reads the summary after completing S-3 can verify that all six layers are active before proceeding to A-1. Without the audit, the six layers are embedded in a prose paragraph that a subsequent executor (or a regenerated context) must parse to confirm completeness. The audit converts the chain from implicit to explicit at the point of FLAG resolution. |

---

## V-01 -- Phrasing Register ("You" Address Throughout)

**Axis**: Phrasing register -- first-person executor address replaces third-person system
language throughout. "You MUST NOT recompute FLAG" in place of "FLAG MUST NOT be recomputed."
"Your first instruction in this step" in place of "The first rule of this step." "No other
instruction in A-1 precedes this one" in place of "No instruction in A-1 precedes this rule."
**Hypothesis**: First-person address creates personal accountability at the critical prohibition
steps. A third-person rule ("FLAG MUST NOT be recomputed") is a system property the executor
reads and may mentally file as background. A first-person command ("You MUST NOT recompute
FLAG") assigns the obligation to the specific executor running the step, making the prohibition
harder to deprioritize under pressure. The content of all 26 criteria is unchanged; only the
register changes.
**Predicts**: All 26 criteria -- C-01 through C-26.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

You will execute this skill in a single pass. You will not prompt the user. You will
write one artifact and emit one next-step line.

---

STEP S-1 -- SETUP

You will read TOPICS.md. You will emit a dedicated line for the TOPICS.md result:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

You will select the skill to mock:
  - If --skill is provided, use it.
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

You will emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- DETERMINE CATEGORY

You will assign CATEGORY for the selected skill. Look up the skill in this table:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,
    flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

CATEGORY is now assigned. You will not modify it.

---

STEP S-3 -- COMPUTE FLAG

You will compute FLAG exactly once in this step. FLAG is a named variable.

You MUST NOT recompute FLAG anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value you emit here. No path is exempt. If you
allow any path to modify FLAG after this point, the guarantee stated above is broken:
A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed
one, producing the same silent category mismatch described at the consumption site.

You will compute FLAG from CATEGORY and tier:

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

FLAG is now resolved. You will not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Your first instruction in this step: copy FLAG from S-3 verbatim. Do not rederive it.
This is your first instruction -- it applies before you list any field, before any
category lookup, before any formatting instruction, or any other instruction you carry
out in this step. No other instruction in A-1 precedes this one. Every instruction you
follow in this step -- named or unnamed -- is governed by this instruction. No
instruction in this step is exempt.
Inertia risk: if you rederive FLAG here, you will produce a category mismatch that is
invisible to downstream tooling and will silently corrupt the artifact's trust tier.
The artifact will carry an incorrect Flag field, downstream mock-review will flag the
wrong namespaces as REAL-REQUIRED, and the corruption will be undetectable without
manual header inspection.

You will assemble the header block:

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

You will write the fidelity warning as the first section of the artifact body. You will
position it before any mock content. Separate from the header and from the body with ---
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

You will generate the mock body following the golden rubric structure for the selected
skill. The body must include:
  - All required section headings for the skill
  - Required tables or lists in the expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms in the expected positions

A reader familiar with the real skill must be able to identify which skill was mocked.
Generic prose without skill-specific structure fails.

---

STEP A-4 -- WRITE ARTIFACT

You will write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

You will emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact is:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-02 -- Output Format (Tabular Prohibition Blocks)

**Axis**: Output format -- both the compute-site and consumption-site prohibition blocks
expressed as labeled-row tables rather than prose paragraphs. Each protection layer occupies
a dedicated row. The six compute-site layers (scope, path classes, affirmative closure,
no-exemption, failure consequence, guarantee-break, cross-site) and the five consumption-site
layers (first rule, anti-displacement, declarative closure, all-governed/no-exempt,
consequence) are individually addressable entries.
**Hypothesis**: Prose prohibition paragraphs can be read with variable depth -- an executor
under pressure may process the first clause ("FLAG MUST NOT be recomputed anywhere in this
run") and skim the remainder. A table enforces row-level attention: each row is a discrete
visual unit that the executor must explicitly pass over. The GUARANTEE-BREAK and CROSS-SITE
rows are visually isolated at the bottom of the S-3 table rather than embedded at the end of
a long sentence, making them harder to skip. The same isolation applies to the CONSEQUENCE
row at A-1.
**Predicts**: All 26 criteria -- C-01 through C-26.
**Expected composite**: 100.

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
  - Otherwise use the representative default:

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

FLAG immutability chain -- all rows are active for the remainder of this run:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | Scope                 | FLAG MUST NOT be recomputed anywhere in this run                     |
  | Path classes          | Not in any step, conditional branch, fallback path, regeneration     |
  |                       | sequence, or any other execution context, including paths that do    |
  |                       | not pass through prior steps in normal order                         |
  | Affirmative closure   | Every execution path that reaches A-1 carries the FLAG value         |
  |                       | emitted here                                                         |
  | No-exemption          | No path is exempt                                                    |
  | Failure consequence   | If any path modifies FLAG after this point, A-1 will inherit a       |
  |                       | corrupted value that cannot be distinguished from a correctly-        |
  |                       | computed one                                                         |
  | Guarantee-break       | This violation breaks the closure guarantee stated in the            |
  |                       | Affirmative closure row above                                        |
  | Cross-site reference  | The failure produces the same silent category mismatch described      |
  |                       | at the consumption site (see A-1 Failure consequence row below)      |

FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

FLAG prohibition chain -- all rows govern this step before any construction begins:

  | Protection layer      | Rule                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | First rule            | Copy FLAG from S-3 verbatim. Do not rederive it.                     |
  | Priority              | This rule is first in this step -- it applies before any other       |
  |                       | instruction                                                          |
  | Anti-displacement     | Before any field is listed, before any category lookup, before any   |
  |                       | formatting instruction, or any other instruction in this step        |
  | Declarative closure   | No instruction in A-1 precedes this rule                             |
  | All-governed          | Every instruction in this step -- named or unnamed -- is governed    |
  |                       | by this rule                                                         |
  | No-exemption          | No instruction in this step is exempt                                |
  | Failure consequence   | Re-deriving FLAG here produces a category mismatch invisible to       |
  |                       | downstream tooling that silently corrupts the artifact's trust tier; |
  |                       | the corruption is undetectable without manual header inspection       |

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

## V-03 -- Inertia Framing (Consequence-Before-Prohibition at S-3)

**Axis**: Inertia framing -- the failure consequence is stated as the opening of S-3 before
the prohibition, inverting the current order. Current order: state the prohibition, then
the affirmative closure, then the consequence. Inverted order: state the consequence first
(naming the failure mode and cross-site reference), then the prohibition, then the affirmative
closure. At A-1, order is unchanged.
**Hypothesis**: An executor under pressure who reads only the first sentence of the S-3
prohibition block currently reads the rule ("FLAG MUST NOT be recomputed"). In consequence-
first ordering, the same executor reads the cost ("A-1 will inherit a corrupted value
indistinguishable from a correctly-computed one"). The cost creates a stronger cognitive
anchor than the rule: a rule can be mentally filed as "noted, moving on"; a named failure
consequence creates a concrete image of what goes wrong that is harder to dismiss. The
consequence-first form also surfaces the C-26 cross-site reference (the mirrored failure at
A-1) at the front of the block rather than at the end of a long sentence.
**Note on C-25**: Consequence-before-prohibition ordering is structurally incompatible with
C-25. C-25 requires the consequence statement to frame the violation as "breaking the
guarantee stated above" -- a backward reference that requires C-21's affirmative closure to
be stated before the consequence. In inverted ordering, the affirmative closure is stated
after the consequence, so "the guarantee stated above is broken" has no referent. C-25 is
intentionally absent in V-03. This variant is a direct test of whether C-25's logical bridge
is the load-bearing mechanism, or whether consequence visibility (position and content) is
what matters. C-26 is retained: the cross-site reference ("same silent category mismatch
described at the consumption site") does not depend on ordering.
**Predicts**: C-01 C-02 C-03 C-04 C-05 | C-06 C-07 C-08 | C-09 C-10 C-11 C-12 C-13
C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24 C-26. Missing: C-25.
**Expected composite**: 17/18 aspirational = ~99.4

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
  - Otherwise use the representative default:

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

FLAG is a named variable computed in this step.

FAILURE CONSEQUENCE: If any execution path reaches A-1 carrying a FLAG value that
differs from the one emitted here, A-1 will inherit a corrupted value that cannot
be distinguished from a correctly-computed one -- producing the same silent category
mismatch described at the consumption site. The failure is invisible to downstream
tooling and undetectable without manual header inspection.

To prevent this: FLAG MUST NOT be recomputed anywhere in this run -- not in any step,
any conditional branch, any fallback path, any regeneration sequence, or any other
execution context, including paths that do not pass through prior steps in normal order.

Every execution path that reaches A-1 carries the FLAG value emitted here. No path is
exempt.

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

## V-04 -- Role Sequence + Lifecycle Emphasis (Merged CLASSIFY-AND-FLAG + Procedure Overview)

**Axis**: Role sequence + lifecycle emphasis -- S-2 (category assignment) and S-3 (flag
computation) merged into a single CLASSIFY-AND-FLAG step; a procedure overview table added
at the top of the prompt before any steps begin.
**Hypothesis**: The inter-step gap between S-2 and S-3 is the point of highest FLAG
rederivation risk: CATEGORY exists as a resolved variable, but FLAG has not yet been
explicitly named. An executor who reaches A-1 via a regenerated context after S-2 but before
S-3 may derive FLAG inline at A-1 from CATEGORY, satisfying C-03 (category correct) while
violating C-11/C-14 (FLAG must be pre-computed). Merging both assignments into one step
ensures that CATEGORY and FLAG resolve simultaneously -- there is no state where CATEGORY
is known but FLAG is not. The procedure overview makes the step topology visible before any
instruction is processed, helping the executor understand that S-2 is the single resolution
point for both values and that A-1 is a strict consumer.
**Predicts**: All 26 criteria -- C-01 through C-26.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

PROCEDURE OVERVIEW

  | Step | Name                | Role                                                    |
  |------|---------------------|---------------------------------------------------------|
  | S-1  | Setup               | Read TOPICS.md, select skill, emit progress line        |
  | S-2  | Classify and Flag   | Assign CATEGORY and compute FLAG -- both final here     |
  | A-1  | Header              | Assemble artifact header; copy FLAG from S-2 verbatim  |
  | A-2  | Fidelity Warning    | Write category-appropriate warning as lead section      |
  | A-3  | Artifact Body       | Generate mock body per golden rubric structure          |
  | A-4  | Write               | Write complete artifact to path                         |
  | A-5  | Next Step           | Emit next-step line as final artifact line              |

Single-pass. No prompts. S-2 is the only step where CATEGORY and FLAG are assigned.
A-1 copies FLAG from S-2 verbatim -- it does not compute, derive, or verify FLAG.

---

STEP S-1 -- SETUP

Read TOPICS.md. Emit a dedicated line:
  > TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}

Select the skill to mock:
  - If --skill is provided, use it.
  - Otherwise use the representative default:

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

STEP S-2 -- CLASSIFY AND FLAG

This step assigns CATEGORY and computes FLAG as a named variable. Both values are
final after this step. Neither is modified anywhere in this run after S-2 closes.

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

CATEGORY is assigned. Do not modify it.

Compute FLAG as a named variable from CATEGORY and tier:

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

FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional
branch, any fallback path, any regeneration sequence, or any other execution context,
including paths that do not pass through prior steps in normal order. Every execution
path that reaches A-1 carries the FLAG value emitted here. No path is exempt. If any
path modifies FLAG after this point, the guarantee stated above is broken: A-1 will
inherit a corrupted value that cannot be distinguished from a correctly-computed one,
producing the same silent category mismatch described at the consumption site.

Both CATEGORY and FLAG are now resolved. Do not re-evaluate or modify either value
anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

The first rule of this step is: copy FLAG from S-2 verbatim. Do not rederive it.
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
  Flag: {FLAG from S-2 -- copied verbatim, not rederived}

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

## V-05 -- Full Convergence + Protection Chain Audit

**Axis**: Role sequence -- all 26 criteria in standard prose form, with S-3 closing with an
explicit numbered six-layer protection chain summary that names each criterion by layer label
and confirms it has been stated in the step above.
**Hypothesis**: The six-layer compute-site chain (C-14, C-16, C-18, C-21, C-23, C-25, C-26)
is embedded in a single prose paragraph in all prior R8 variants. An executor or regenerated
context that processes the paragraph sequentially may complete the chain; an executor that
skims it may miss C-25 (guarantee-break framing) or C-26 (cross-site reference) because
both appear at the end of the same sentence. The protection chain audit at the close of S-3
converts the chain from implicit to explicit: each layer is a numbered entry with its label,
and the final line "FLAG is now resolved with all six protection layers active" is an
auditable closure statement. A subsequent executor who reads the audit line before A-1 has
a six-point checklist against which to verify that the compute-site chain is complete. This
mirrors the role that the A-1 prohibition block plays for the consumption site -- it makes
the layered structure visible at the point of FLAG resolution rather than requiring the
executor to parse the prose paragraph to confirm completeness.
**Predicts**: All 26 criteria -- C-01 through C-26.
**Expected composite**: 100.

---

```
You are running /mock:ns for Signal.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required -- scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative skill per namespace)
  --tier     1 | 2 | 3        (optional -- default: 1)

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

Protection chain established at this step -- all six layers are active for the
remainder of this run:

  [1] Scope (C-16): FLAG MUST NOT be recomputed anywhere in this run -- not in any
      subsequent step, not via any conditional branch, not via any fallback path, not
      via any regeneration sequence, not via any other execution context
  [2] Path classes (C-18): prohibition covers conditional branches, fallback paths,
      regeneration sequences, and all other execution contexts, including paths that
      do not pass through prior steps in normal order
  [3] Affirmative closure (C-21): every execution path that reaches A-1 carries the
      FLAG value emitted here; no path is exempt
  [4] Failure consequence (C-23): any modification after this point produces a
      corrupted value at A-1 that is indistinguishable from a correctly-computed one
  [5] Guarantee-break framing (C-25): such modification breaks the closure
      commitment stated in layer [3] above
  [6] Cross-site reference (C-26): the failure produces the same silent category
      mismatch described at the consumption site in A-1

FLAG is now resolved with all six protection layers active. Do not re-evaluate or
modify it anywhere in this run.

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

| Variant | Axis | Structural change | C-25 | C-26 | Expected composite |
|---------|------|------------------|------|------|-------------------|
| V-01 | Phrasing register ("you" address) | All imperatives personalized to executor | pass | pass | 100 |
| V-02 | Output format (tabular prohibition blocks) | S-3 and A-1 prohibition as labeled-row tables | pass | pass | 100 |
| V-03 | Inertia framing (consequence-first at S-3) | Failure consequence precedes prohibition; C-25 structurally absent | FAIL | pass | ~99.4 |
| V-04 | Role sequence + lifecycle emphasis (merged S-2/S-3, phase map) | CLASSIFY-AND-FLAG step; procedure overview table | pass | pass | 100 |
| V-05 | Full convergence + protection chain audit | Six-layer numbered summary at S-3 close | pass | pass | 100 |

**Key discriminants**:
- V-01 vs V-02: Tests whether personalization (register) or tabular isolation (format) more
  reliably prevents C-25/C-26 from being skipped. Both predict 100 but through different
  mechanisms -- V-01 by direct executor address, V-02 by structural row isolation.
- V-03 vs V-01/V-02/V-04/V-05: The critical isolation test. If real runs show V-03 producing
  equivalent execution quality to the full-convergence variants despite missing C-25, this
  would suggest C-25's guarantee-break framing is redundant when the consequence is
  front-loaded. If V-03 underperforms, C-25's causal bridge is confirmed as load-bearing --
  the backward reference to the affirmative closure commitment adds something that consequence
  visibility alone does not provide.
- V-04 vs V-05: Tests whether merging S-2/S-3 (topology change) or adding an explicit audit
  at S-3 close (audit trail) is the more reliable structural reinforcement. V-04 changes
  when FLAG resolves; V-05 changes how the resolution is confirmed.
- V-01/V-02/V-04/V-05 vs R8 V-05: All four R9 full-convergence variants carry identical
  criteria coverage to R8 V-05. If any R9 variant scores differently from R8 V-05 on real
  runs, the difference is attributable entirely to the structural change tested -- register,
  format, step topology, or audit trail.
- The primary empirical question for R9: Is the six-layer compute-site chain more reliably
  executed when it is phrased in first person (V-01), structured as a table (V-02), merged
  with CATEGORY into one step (V-04), or followed by an explicit numbered audit (V-05)?
  R8 showed that the chain's content (C-25 + C-26) was stable across minimal and prose
  forms. R9 tests whether the chain's form changes execution reliability.
