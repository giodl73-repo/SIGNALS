Now I have complete context for what R1-R4 explored. Let me generate Round 2 variations that build on R4 V-05 convergence and test genuinely new axes: compliance override reinstatement, body generation specificity, and depth parameter integration.

---

# mock-ns -- Round 2 Variations

**Rubric**: v4 (C-01 through C-16, carried from R4 convergence).

**R4 convergence summary**: R4 V-05 combined all confirmed excellence signals -- 4-op CONSTRAINT, per-field downstream-action bullets (C-15), three-op exhaustive CONSTRAINT (C-16), table-centric lookups (S-1/S-2), flag computation table with tier-conditional rows (C-09). This is the current best prompt.

**Round 2 question**: Are there dimensions R4 never tested? Three candidates:
1. The original T3 compliance override (scout-compliance / trace-permissions + tags -> REAL-REQUIRED) was silently dropped from R1 onward.
2. The body generation step is specified only by "follow the golden pattern" -- edge-case skills (prove-hypothesis, review-customers) may fail C-03 at higher rates than prototype skills.
3. The `depth` parameter (quick / standard / deep) exists in the T3 header but has never been wired into any variation.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Compliance override reinstatement | Reinstating the compliance override as a named last-check row in the flag computation table is the carrier for any future C-17 criterion (compliance-sensitive flag). Predicts C-01--C-16 pass; surfaces C-17 if added to rubric. |
| V-02 | Body generation specificity by structural category | Per-category minimal structure hints in S-4 -- naming required element types without prescribing content -- improve C-03 pass rates for edge-case skills (MIXED, EVIDENCE-HEAVY) without breaking HIGH-STRUCTURE fidelity. |
| V-03 | Depth parameter integration | Wiring `--depth` as a first-class input (quick/standard/deep) and routing body generation length through a depth table does not break existing criteria but separates body scope from structural fidelity -- a clean single-axis isolation test. |
| V-04 | Compliance override + body generation specificity (two-axis) | V-01 + V-02 combined: compliance override in S-3 and per-category structure hints in S-4 coexist without conflict. Both signals reinforce without canceling. Predicts C-01--C-16 pass + compliance-sensitive path covered. |
| V-05 | Convergent: R4 heritage + compliance override + body specificity + depth routing | R4 V-05 foundation + V-01 (compliance override) + V-02 (per-category body hints) + V-03 (depth routing). First prompt with all four signal families present simultaneously. Predicts all criteria reliably pass across all skill/tier/compliance combinations. |

---

## V-01 -- Compliance Override Reinstatement

**Axis**: Compliance override -- the original T3 spec included a last-check override in S-3: if compliance tags are present in TOPICS.md AND the skill is `scout-compliance` or `trace-permissions`, FLAG = REAL-REQUIRED (compliance-sensitive), regardless of category or tier. This override was dropped in R1 and never reinstated.
**Hypothesis**: Reinstating the compliance override as an explicit last row in the flag computation table prevents silent category mismatch for compliance-sensitive skills. No existing R4 criteria require it, but it is the structural carrier for a future C-17. Does not change the path for non-compliance skills; predicts C-01--C-16 unchanged.
**Predicts**: C-01--C-16 pass | C-17 (if added) PASS.
**Expected composite**: 100 (same as R4 V-05 for existing criteria; compliance-sensitive path now covered).

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

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
body generation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present -- existence (found/not found), tier classification,
and compliance tags. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Carry resolved compliance tags into S-3 for compliance override check.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute Flag from this table (apply rows in order; use the first match):

  | Priority | Category       | Tier | Skill condition  | Flag value                                                      |
  |----------|----------------|------|------------------|-----------------------------------------------------------------|
  | 1 (last) | any            | any  | scout-compliance or trace-permissions AND compliance tags present | REAL-REQUIRED (compliance-sensitive)                 |
  | 2        | HIGH-STRUCTURE | 2+   | critical skill   | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | 3        | HIGH-STRUCTURE | 1    | critical skill   | none (structural coverage reliable)                             |
  | 4        | HIGH-STRUCTURE | any  | non-critical     | none (structural coverage reliable)                             |
  | 5        | EVIDENCE-HEAVY | any  | any              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | 6        | MIXED          | any  | any              | REVIEW-FOR-PLAUSIBILITY                                         |

Note: Priority 1 (compliance override) is checked last in the table but takes precedence
over all other rows -- if the compliance condition is met, use that flag regardless of
category or tier.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

---- HEADER BLOCK (required; must be first content in the file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header, no content between) ----

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
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP S-5 -- FINALIZE

After writing the artifact, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-02 -- Body Generation Specificity by Structural Category

**Axis**: Body generation specification -- the current R4 V-05 body instruction is category-agnostic ("follow the golden structural pattern"). This variation adds per-category minimal structure contracts: named required element types per category without prescribing content. The hypothesis is that executor ambiguity on MIXED and EVIDENCE-HEAVY body structure (no tables, no gate lines) is the primary source of C-03 failures for less-common skills.
**Hypothesis**: Naming 3-4 required element types per category in the body generation instruction reduces C-03 failure rate for edge-case skills (prove-hypothesis as MIXED, listen-support as EVIDENCE-HEAVY) without over-constraining HIGH-STRUCTURE output. The CONSTRAINT and table structures carry forward unchanged from R4 V-05.
**Predicts**: C-01--C-16 pass | C-03 PASS at higher rate for MIXED and EVIDENCE-HEAVY skills.
**Expected composite**: 100 (improved reliability on C-03 across skill types).

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

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
body generation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present -- existence (found/not found), tier classification,
and compliance tags. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute Flag from this table:

  | Category       | Tier | Skill condition  | Flag value                                                      |
  |----------------|------|------------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | non-critical     | none (structural coverage reliable)                             |
  | HIGH-STRUCTURE | 1    | critical         | none (structural coverage reliable)                             |
  | HIGH-STRUCTURE | 2+   | critical         | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | EVIDENCE-HEAVY | any  | any              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | MIXED          | any  | any              | REVIEW-FOR-PLAUSIBILITY                                         |

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

---- HEADER BLOCK (required; must be first content in the file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header, no content between) ----

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

  Generate mock content following the exact golden structural pattern of {skill-id}.
  The body must satisfy all structural requirements for the matched category:

  HIGH-STRUCTURE body contract:
    - Correct section headings in the order the real skill uses them
    - At least one enforcement table or scoring structure where the skill has one
    - A gate or verdict line in its expected structural position
    - Phase or boundary markers where the skill uses them
    - All values are synthetic but shapes are identical to real output

  EVIDENCE-HEAVY body contract:
    - Section headings for each evidence or data-collection dimension the skill covers
    - Named data slots (quotes, sources, personas, tickets) with placeholder values
    - A confidence or summary statement where the skill produces one
    - No invented conclusions -- data slots must be structurally present but clearly synthetic

  MIXED body contract:
    - Structural elements (tables, scoring, verdicts) generated with full fidelity
    - Research or evidence claims clearly marked synthetic (e.g., "[synthetic]")
    - A verdict or recommendation line in its expected position
    - Cross-persona or multi-source comparison structure if the skill uses one

  In all cases: use {topic} as the subject. A reader familiar with the real {skill-id}
  output must be able to identify the skill from the body alone, without reading the header.

---

STEP S-5 -- FINALIZE

After writing the artifact, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-03 -- Depth Parameter Integration

**Axis**: Depth parameter -- the original T3 SKILL.md header has `depth: standard` with a `# quick | standard | deep` routing comment. No prior variation surfaces `--depth` as a first-class input or routes body generation scope through it. This variation adds `--depth` to INPUTS and routes body generation length through a depth table: quick (5+ sections minimum, breadth only), standard (full structural coverage, default), deep (adversarial edge cases present in body content alongside standard structure).
**Hypothesis**: Surfacing depth as a named input and routing it explicitly does not break any C-01--C-16 criterion (depth affects body scope, not header, flag, path, or fidelity warning). It is a clean single-axis test. If a future C-18 criterion for depth-appropriate body scope is added, this variation is the carrier.
**Predicts**: C-01--C-16 pass (unchanged) | C-18 (if added) PASS.
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
  --depth    quick | standard | deep (optional -- default: standard)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
body generation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present -- existence (found/not found), tier classification,
and compliance tags. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

Resolve depth: use --depth value if provided; otherwise default to standard.
Carry resolved depth into S-4 for body scope routing.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      -> flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier}, depth: {depth})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute Flag from this table:

  | Category       | Tier | Skill condition  | Flag value                                                      |
  |----------------|------|------------------|-----------------------------------------------------------------|
  | HIGH-STRUCTURE | any  | non-critical     | none (structural coverage reliable)                             |
  | HIGH-STRUCTURE | 1    | critical         | none (structural coverage reliable)                             |
  | HIGH-STRUCTURE | 2+   | critical         | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | EVIDENCE-HEAVY | any  | any              | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | MIXED          | any  | any              | REVIEW-FOR-PLAUSIBILITY                                         |

Flag is unaffected by depth.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

---- HEADER BLOCK (required; must be first content in the file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header, no content between) ----

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

  Generate mock content following the exact golden structural pattern of {skill-id}.
  Body scope is routed by depth:

  | Depth    | Body scope                                                                  |
  |----------|-----------------------------------------------------------------------------|
  | quick    | Minimum viable structure: 5+ sections, primary tables only, no edge cases   |
  | standard | Full structural coverage: all sections, all required tables, standard gate  |
  | deep     | Full standard coverage PLUS: adversarial edge cases present as named rows,  |
  |          | failure paths in gate/verdict, boundary conditions in enforcement tables    |

  In all cases:
  - Correct section headings for {skill-id}
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place
  - Use {topic} as subject throughout
  - All values synthetic but structurally representative
  A reader familiar with the real {skill-id} output must identify the skill from
  the body alone, without reading the header block.

---

STEP S-5 -- FINALIZE

After writing the artifact, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-04 -- Compliance Override + Body Generation Specificity (Two-Axis)

**Axis**: Two-axis combination: V-01's compliance override reinstated in S-3 (last-check priority row) plus V-02's per-category body generation contracts in S-4.
**Hypothesis**: Both signals coexist without conflict -- the compliance override is in S-3 (does not affect body spec), and per-category body hints are in S-4 (do not affect flag computation). Together they close the two most likely failure modes not covered by R4 V-05: (1) compliance-sensitive skills receiving wrong flag, (2) MIXED/EVIDENCE-HEAVY skills generating unrecognizable body structure. Combined prediction matches or exceeds R4 V-05.
**Predicts**: C-01--C-16 pass | C-03 improved for edge-case skills | C-17 (compliance) PASS if added.
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

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
body generation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present -- existence (found/not found), tier classification,
and compliance tags. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Carry resolved compliance tags into S-3 for compliance override check.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compliance-sensitive skills:
  scout-compliance, trace-permissions

Compute Flag. Apply rows in order; stop at the first match:

  | Priority | Condition                                                         | Flag value                                                      |
  |----------|--------------------------------------------------------------------|----------------------------------------------------------------|
  | 1        | Skill is compliance-sensitive AND compliance tags present           | REAL-REQUIRED (compliance-sensitive)                           |
  | 2        | Category=HIGH-STRUCTURE AND skill is critical AND tier >= 2        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | 3        | Category=HIGH-STRUCTURE AND skill is critical AND tier = 1         | none (structural coverage reliable)                            |
  | 4        | Category=HIGH-STRUCTURE AND skill is non-critical                  | none (structural coverage reliable)                            |
  | 5        | Category=EVIDENCE-HEAVY                                            | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | 6        | Category=MIXED                                                     | REVIEW-FOR-PLAUSIBILITY                                        |

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

---- HEADER BLOCK (required; must be first content in the file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header, no content between) ----

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

  Generate mock content following the exact golden structural pattern of {skill-id}.
  The body must satisfy the structural requirements for the matched category:

  HIGH-STRUCTURE body contract:
    - Correct section headings in the order the real skill uses them
    - At least one enforcement table or scoring structure where the skill has one
    - A gate or verdict line in its expected structural position
    - Phase or boundary markers where the skill uses them
    - All values synthetic; shapes identical to real output

  EVIDENCE-HEAVY body contract:
    - Section headings for each evidence or data-collection dimension the skill covers
    - Named data slots (quotes, sources, personas, tickets) with placeholder values
    - A confidence or summary statement where the skill produces one
    - Data slots present and clearly synthetic -- no invented conclusions

  MIXED body contract:
    - Structural elements (tables, scoring, verdicts) generated with full fidelity
    - Research or evidence claims marked synthetic (e.g., "[synthetic]")
    - A verdict or recommendation line in its expected position
    - Cross-persona or multi-source comparison structure if the skill uses one

  In all cases: use {topic} as the subject. A reader familiar with the real {skill-id}
  output must identify the skill from the body alone, without reading the header.

---

STEP S-5 -- FINALIZE

After writing the artifact, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-05 -- Convergent: R4 Heritage + Compliance Override + Body Specificity + Depth Routing

**Axis**: All confirmed excellence signals at maximum strength: R4 V-05 foundation (4-op CONSTRAINT, per-field downstream-action bullets C-15, three-op exhaustive enumeration C-16, table-centric lookups S-1/S-2, flag computation table with tier-conditional rows C-09) PLUS V-01 compliance override (C-17 carrier) PLUS V-02 per-category body contracts (C-03 hardening) PLUS V-03 depth routing (C-18 carrier). This is the first prompt that integrates all four Round 2 signal families alongside the complete R4 heritage.
**Hypothesis**: Each new signal (compliance override, body contracts, depth routing) occupies a distinct step and instruction domain -- none conflicts with an R4 signal. The compliance override is a last-row in S-3 that does not touch S-4; per-category body contracts strengthen C-03 at S-4 without affecting S-0--S-3; depth routing at S-0 and S-4 does not touch the header, flag, or path. All 16 existing criteria pass; new criteria are surfaced if added to the rubric.
**Predicts**: C-01--C-16 reliably pass | C-17 (compliance-sensitive) PASS | C-18 (depth-appropriate scope) PASS.
**Expected composite**: 100 across all criteria including future additions.

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
  --depth    quick | standard | deep (optional -- default: standard)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, flag computation, or
body generation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present -- existence (found/not found), tier classification,
and compliance tags. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Carry resolved compliance tags into S-3 for compliance override check.

Resolve depth: use --depth if provided; otherwise default to standard.
Carry resolved depth into S-4 for body scope routing.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier}, depth: {depth})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                    |
  |----------------|------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,       |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,        |
  |                | draft-proposal, draft-pitch, review-design, review-code,         |
  |                | trace-request, trace-component, trace-contract, trace-state,     |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience, |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                     |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                |
  |                | listen-feedback, listen-support, listen-adoption                 |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,           |
  |                | review-users                                                     |

If the skill is not in any row, emit an error and stop.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills (eligible for tier-conditional refinement):
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compliance-sensitive skills (eligible for compliance override):
  scout-compliance, trace-permissions

Compute Flag. Evaluate rows in priority order; stop at the first match:

  | Priority | Condition                                                         | Flag value                                                      |
  |----------|--------------------------------------------------------------------|----------------------------------------------------------------|
  | 1        | Skill is compliance-sensitive AND compliance tags != none           | REAL-REQUIRED (compliance-sensitive)                           |
  | 2        | Category=HIGH-STRUCTURE AND skill is critical AND tier >= 2        | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | 3        | Category=HIGH-STRUCTURE AND skill is critical AND tier = 1         | none (structural coverage reliable)                            |
  | 4        | Category=HIGH-STRUCTURE AND skill is non-critical                  | none (structural coverage reliable)                            |
  | 5        | Category=EVIDENCE-HEAVY                                            | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | 6        | Category=MIXED                                                     | REVIEW-FOR-PLAUSIBILITY                                        |

Flag is not affected by depth.

---

STEP S-4 -- WRITE ARTIFACT

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

---- HEADER BLOCK (required; must be first content in the file) ----

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id}
  Topic: {topic}
  Category: {category from S-2}
  Date: {date}
  Status: MOCK (awaiting review)
  Flag: {flag from S-3}

---- FIDELITY WARNING (required; immediately after header, no content between) ----

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

  Generate mock content following the exact golden structural pattern of {skill-id}.
  Body scope is routed by depth:

  | Depth    | Scope                                                                       |
  |----------|-----------------------------------------------------------------------------|
  | quick    | Minimum viable: 5+ sections, primary tables only, no edge cases             |
  | standard | Full structural coverage: all sections, all required tables, standard gate  |
  | deep     | Standard coverage PLUS: adversarial edge cases as named rows, failure paths |
  |          | in gate/verdict, boundary conditions in enforcement tables                  |

  The body must also satisfy the structural contract for the matched category:

  HIGH-STRUCTURE:
    - Correct section headings in the order the real skill uses them
    - At least one enforcement table or scoring structure where the skill has one
    - A gate or verdict line in its expected structural position
    - Phase or boundary markers where the skill uses them

  EVIDENCE-HEAVY:
    - Section headings for each evidence or data-collection dimension the skill covers
    - Named data slots (quotes, sources, personas, tickets) with placeholder values
    - A confidence or summary statement where the skill produces one
    - No invented conclusions; data slots present and clearly synthetic

  MIXED:
    - Structural elements (tables, scoring, verdicts) at full fidelity
    - Research or evidence claims marked synthetic (e.g., "[synthetic]")
    - A verdict or recommendation line in its expected position
    - Cross-persona or multi-source comparison structure if the skill uses one

  In all cases: use {topic} as the subject. All values are synthetic but structurally
  representative. A reader familiar with the real {skill-id} output must identify the
  skill from the body alone, without reading the header block.

---

STEP S-5 -- FINALIZE

After writing the artifact, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## Round 2 Summary

| Variation | Axis | New signals introduced | Predicts |
|-----------|------|------------------------|----------|
| V-01 | Compliance override reinstatement | Compliance override (C-17 carrier) | C-01--C-16 pass; C-17 PASS if added |
| V-02 | Body generation specificity by category | Per-category body contracts (C-03 hardening) | C-01--C-16 pass; C-03 improved for MIXED/EH |
| V-03 | Depth parameter integration | Depth routing in S-0 + S-4 (C-18 carrier) | C-01--C-16 pass; C-18 PASS if added |
| V-04 | V-01 + V-02 (two-axis) | Compliance override + body contracts | C-01--C-16 pass; C-17 carrier active |
| V-05 | Convergent: R4 heritage + V-01 + V-02 + V-03 | All Round 2 signals + full R4 foundation | C-01--C-18 pass when rubric extended |

**Scoring recommendation**: Run all five against the same 3 test inputs used in R4 (standard HIGH-STRUCTURE, EVIDENCE-HEAVY, and MIXED skill mocks). Add a fourth test input: `scout-compliance` topic with compliance tags present, to activate the compliance override path. Criteria to watch: C-03 on prove-hypothesis (MIXED), C-17 on scout-compliance with tags.
