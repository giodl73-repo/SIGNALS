---
skill: quest-variate
skill_target: mock-ns
round: 6
rubric_version: 6
rubric_target: C-23, C-24
date: 2026-03-16
---

# mock-ns -- Round 6 Variations (rubric v6, C-23 + C-24 target)

Rubric: v6 (C-01 through C-24, 5 essential / 3 recommended / 16 aspirational, max 112).

New criteria in v6 (extracted from R5 scoring):

- **C-23** -- Preamble gate position: The preamble gate sentence (required for C-19)
  must be the absolute first sentence in the S-0 step body -- zero pre-gate surface
  area. Any text before the preamble gate (including a CONSTRAINT block or a single
  introductory sentence) fails C-23 even if C-19 passes (preamble gate still precedes
  resolution bullets). Pass condition: preamble gate is the first content the reader
  encounters when scanning S-0, before CONSTRAINT, before parameter table, before
  any prose framing.

- **C-24** -- 5-op CONSTRAINT: The CONSTRAINT block (C-15 minimum 3 ops; C-21
  extended to 4 ops including body generation) must name at minimum 5 prohibited
  operation types, where the 5th closes the artifact-write phase: no artifact path
  construction, no artifact file write, or equivalent language prohibiting any A-4
  WRITE phase activity during S-0. The C-21 minimum of 4 ops is necessary but not
  sufficient. A complete adversarial-coverage CONSTRAINT must close all 5 production
  phases: discovery (lookup), decision (selection), generation (mock generation),
  content (body generation), output (path construction / file write).

R5 evidence sources:
- R5 V-01 (C-21 boundary): 3-op CONSTRAINT retroactively identified as leaving artifact
  write phase uncovered. Under v6, a 4-op CONSTRAINT still fails C-24 -- body generation
  is prohibited but path construction and file write are not. The 5-op form closes the
  final phase gap.
- R5 V-03 (C-19 boundary): terminal-gate-only form retroactively identified as allowing
  pre-gate surface. Under v6, C-23 requires zero pre-gate surface area -- even a correct
  preamble gate that follows CONSTRAINT text fails C-23. The fix is positioning the
  preamble gate before the CONSTRAINT block.

R6 baseline: R5 V-05 structure. The R5 convergent (CONSTRAINT first, 4-op) scores
108/112 under v6 -- it fails C-23 (CONSTRAINT precedes preamble gate) and C-24 (4-op
CONSTRAINT, artifact write phase not prohibited). Each R6 boundary variate isolates
exactly one v6 failure. V-05 is the form-variant convergent scoring 112/112.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | C-24 boundary: 4-op CONSTRAINT, preamble gate first | Preamble gate moved to absolute first sentence of S-0 (C-23 passes). CONSTRAINT retains 4 ops -- "No category lookup. No skill selection. No mock generation. No body generation." -- artifact write phase not named (C-24 fails). Trap: scorer sees 4-op CONSTRAINT (C-21 passes) and awards C-24 without checking whether the artifact write phase is explicitly prohibited. Predicts C-24 FAIL; score 110/112. |
| V-02 | C-23 boundary: CONSTRAINT-first placement, 5-op | CONSTRAINT block appears as the first content in S-0 -- same structural position as R5 V-05. CONSTRAINT expanded to 5 ops (adds "No artifact path construction or file write." -- C-24 passes). Preamble gate follows CONSTRAINT text (C-19 passes -- gate precedes resolution bullets; C-23 fails -- CONSTRAINT is pre-gate surface area). Trap: scorer sees dual-gate form (C-19 passes) and awards C-23 without verifying the gate is the opening sentence with zero pre-gate content. Predicts C-23 FAIL; score 110/112. |
| V-03 | C-23 boundary: intro prose before preamble gate, 5-op | S-0 opens with one introductory sentence: "Read TOPICS.md to resolve the topic's tier and compliance tags." Preamble gate follows as the second sentence. C-19 passes (preamble gate is before the resolution table). C-23 fails (one line of introductory prose precedes the preamble gate). CONSTRAINT has 5 ops (C-24 passes). Trap: scorer reads C-19 pass as satisfying C-23, missing that C-23 requires zero pre-gate surface including introductory sentences. A one-sentence intro is the minimal violation of C-23. Predicts C-23 FAIL; score 110/112. |
| V-04 | Double boundary: C-23 + C-24 both fail (R5 baseline) | CONSTRAINT-first placement (fails C-23) AND 4-op CONSTRAINT without artifact write phase (fails C-24). This is the R5 V-05 baseline form -- no changes from R5. Documents the R5 baseline score under v6 scoring. Predicts C-23 FAIL + C-24 FAIL; score 108/112. |
| V-05 | Convergent: all 24 criteria via alternative surface forms | Preamble gate is absolute first sentence of S-0, before CONSTRAINT and before any prose. CONSTRAINT block follows with 5 ops using synonym phrasings. All other criteria from R5 V-05 retained via form-variant language testing criterion form-independence. Predicts 112/112. |

---

## V-01 -- C-24 Boundary: 4-op CONSTRAINT, Preamble Gate First (C-23 Pass, C-24 Deliberate Fail)

**Axis**: CONSTRAINT phase coverage. Tests the boundary between C-21 (4-op minimum,
including body generation) and C-24 (5-op requirement, including artifact write phase).
**Change from R5 baseline**: Preamble gate moved to absolute first sentence of S-0 (C-23
now passes). CONSTRAINT retains 4 ops -- body generation is prohibited but artifact path
construction and file write are not named.
**Hypothesis**: C-21 passes (4 ops present: lookup, selection, mock generation, body
generation). C-23 passes (preamble gate is the opening sentence with zero pre-gate
surface area). C-24 fails (artifact write phase absent from CONSTRAINT -- a model could
defer all generation phases but still begin constructing the output path or writing the
file before S-0 completes). All other v6 criteria unchanged.
**Predicts**: C-01--C-23: all pass. C-24: fail. Expected composite: 110/112.

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

Before any other step begins, emit the TOPICS.md status line below.

CONSTRAINT: No category lookup. No skill selection. No mock generation. No body
generation. None of these operations begin until after the TOPICS.md status line
below has been emitted.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Carry into S-2 and S-3                       |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

Do not begin S-1 until this line is emitted.
Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

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
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-02 -- C-23 Boundary: CONSTRAINT-First Placement, 5-op (C-24 Pass, C-23 Deliberate Fail)

**Axis**: Preamble gate position relative to CONSTRAINT block. Tests whether a correctly
formed preamble gate satisfies C-23 when it follows CONSTRAINT text, or whether C-23
requires the gate to be the absolute first sentence with zero pre-gate content.
**Change from R5 baseline**: CONSTRAINT expanded to 5 ops (adds "No artifact path
construction or file write." -- C-24 now passes). Preamble gate position unchanged --
CONSTRAINT block still appears before preamble gate (same as R5 V-05).
**Hypothesis**: C-19 passes (preamble gate is before the resolution table -- dual-gate
form is intact). C-24 passes (5 ops present including artifact write phase). C-23 fails
(CONSTRAINT block precedes the preamble gate; CONSTRAINT text is pre-gate surface area
that a reader encounters before the gate sentence). Trap: scorer reads C-19 as passing
and infers C-23 passes because "the preamble gate is present." The distinction: C-19
requires the preamble gate before the resolution bullets; C-23 requires it before
everything, including the CONSTRAINT block.
**Predicts**: C-01--C-22: all pass. C-23: fail. C-24: pass. Expected composite: 110/112.

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

CONSTRAINT: No category lookup. No skill selection. No mock generation. No body
generation. No artifact path construction or file write. None of these operations
begin until after the TOPICS.md status line below has been emitted.

Before any other step begins, emit the TOPICS.md status line below.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Carry into S-2 and S-3                       |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

Do not begin S-1 until this line is emitted.
Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

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
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-03 -- C-23 Boundary: Intro Prose Before Preamble Gate, 5-op (C-24 Pass, C-23 Deliberate Fail)

**Axis**: Preamble gate position relative to introductory prose. Tests whether a single
introductory sentence before the preamble gate constitutes pre-gate surface area that
fails C-23.
**Change from R5 baseline**: S-0 opens with one framing sentence: "Read TOPICS.md to
resolve the topic's tier and compliance tags." The preamble gate follows as the second
sentence. CONSTRAINT has 5 ops (C-24 passes). Preamble gate is before the resolution
table (C-19 passes).
**Hypothesis**: C-19 passes (preamble gate precedes the resolution table -- both gate
forms are present). C-24 passes (5 ops including artifact write phase). C-23 fails
(one sentence of introductory prose precedes the preamble gate; the preamble gate is
not the opening sentence of S-0). Trap: scorer sees the preamble gate in the correct
position relative to the resolution bullets (C-19 passes) and infers C-23 passes.
The C-23 discriminator is not "before the table" but "before everything, including
any framing sentence." One intro sentence is the minimal C-23 violation.
**Predicts**: C-01--C-22: all pass. C-23: fail. C-24: pass. Expected composite: 110/112.

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

Read TOPICS.md to resolve the topic's tier and compliance tags.

Before any other step begins, emit the TOPICS.md status line below.

CONSTRAINT: No category lookup. No skill selection. No mock generation. No body
generation. No artifact path construction or file write. None of these operations
begin until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Carry into S-2 and S-3                       |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

Do not begin S-1 until this line is emitted.
Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

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
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-04 -- Double Boundary: C-23 + C-24 Both Fail (R5 Baseline Form)

**Axis**: Both v6 new criteria simultaneously. Documents the exact R5 V-05 baseline
form under v6 scoring -- no changes from R5.
**Change from R5 baseline**: None. This is the unmodified R5 V-05 convergent structure.
CONSTRAINT-first placement (C-23 fails). 4-op CONSTRAINT without artifact write phase
(C-24 fails).
**Hypothesis**: C-19 passes (preamble gate is before the resolution bullets). C-21
passes (4-op CONSTRAINT includes body generation). C-23 fails (CONSTRAINT block is
pre-gate surface -- reader encounters CONSTRAINT text before preamble gate). C-24 fails
(artifact write phase absent -- path construction and file write not prohibited during
S-0). This is the canonical R5 form scoring 108/112 under v6.
**Predicts**: C-01--C-22: all pass. C-23: fail. C-24: fail. Expected composite: 108/112.

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

CONSTRAINT: No category lookup. No skill selection. No mock generation. No body
generation. None of these operations begin until after the TOPICS.md status line
below has been emitted.

Before any other step begins, emit the TOPICS.md status line below.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Carry into S-2 and S-3                       |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

Do not begin S-1 until this line is emitted.
Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

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
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## V-05 -- Convergent: All 24 Criteria via Alternative Surface Forms (Predicts 112/112)

**Axis**: Form-independence of C-23 and C-24 pass conditions. Tests whether alternative
phrasings for the preamble gate and 5-op CONSTRAINT satisfy both new criteria without
using the canonical R5 surface language.
**Changes from R5 baseline**:
1. Preamble gate moved to absolute first sentence of S-0 (C-23 now passes). Form:
   "This step emits first. Write the TOPICS.md status line before any other work begins."
   -- distinct from canonical "Before any other step begins, emit..." phrasing.
2. CONSTRAINT expanded to 5 ops using synonym forms (C-24 now passes): "No lookup
   of skill categories. No skill-id resolution. No mock content generation. No artifact
   body construction. No artifact path assembly or file output." -- all 5 prohibited
   phases named without using C-15 canonical phrasings verbatim.
3. Terminal gate form: "S-1 must not begin until the line above appears in the
   conversation." -- distinct from canonical "Do not begin S-1 until this line is
   emitted."
4. Tier carry standalone sentence: "Forward the resolved tier to S-2 and S-3."
5. Table tier row downstream-use cell: "Propagates to S-2 and S-3" -- distinct from
   "Carry into S-2 and S-3" while naming both consumers (C-20 passes).
**Hypothesis**: All 24 criteria pass. C-23 passes because preamble gate is the absolute
first sentence before CONSTRAINT and any prose. C-24 passes because 5 ops are named
by type including the artifact output phase using synonym language. All R5 criteria
pass via form-variant surface phrasings.
**Predicts**: C-01--C-24: all pass. Expected composite: 112/112.

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

This step emits first. Write the TOPICS.md status line before any other work begins.

CONSTRAINT: No lookup of skill categories. No skill-id resolution. No mock content
generation. No artifact body construction. No artifact path assembly or file output.
None of these operations begin until after the TOPICS.md status line below has been
written to the conversation.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not begin until the line above appears in the conversation.
Forward the resolved tier to S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise look up the namespace default:

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
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural) |

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,   |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id is not found in any row, emit an error naming the unrecognized
skill-id and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                   | Flag value                                                      |
  |---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                   | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)   |
  | CATEGORY = MIXED                                                                            | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2  | none (structural coverage reliable; REAL-REQUIRED at Tier 2+)  |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1   | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                                  | none (structural coverage reliable)                            |

Compliance override (evaluated after table match, regardless of row result):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it anywhere in this run.

---

STEP A-1 -- ASSEMBLE HEADER

Write the header block as the first content in the artifact. Copy FLAG verbatim
from S-3 -- do not rederive it.

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {CATEGORY from S-2}
  Date: {today's date}
  Status: MOCK (awaiting review)
  Flag: {FLAG from S-3 -- verbatim, not rederived}

All six fields must be present. The header precedes all body content.

---

STEP A-2 -- FIDELITY WARNING

Write the fidelity warning immediately after the header, separated by ---. Choose
by CATEGORY:

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
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative
  A reader familiar with the real {skill-id} output must be able to identify the
  skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

After writing, emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The last line of the artifact must be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Exception: omit the Next line if this run was called from within a mock-review session
to regenerate a thin namespace (mock-review controls the next step in that context).
```

---

## Predicted Score Summary

| Variate | Axis | C-23 | C-24 | Score |
|---------|------|------|------|-------|
| V-01 | C-24 boundary: 4-op CONSTRAINT, preamble gate first | PASS | FAIL | 110/112 |
| V-02 | C-23 boundary: CONSTRAINT-first placement, 5-op | FAIL | PASS | 110/112 |
| V-03 | C-23 boundary: intro prose before gate, 5-op | FAIL | PASS | 110/112 |
| V-04 | Double boundary: R5 baseline form unchanged | FAIL | FAIL | 108/112 |
| V-05 | Convergent: all 24 criteria, form-variant language | PASS | PASS | 112/112 |

## New Failure Traps Encoded in R6

| Trap | Criterion | Description |
|------|-----------|-------------|
| C-21 count satisfies C-24 | C-24 | 4-op CONSTRAINT (passing C-21) leaves artifact write phase uncovered. C-21 is a necessary but not sufficient condition for C-24. V-01 confirms. |
| C-19 awarded as C-23 (CONSTRAINT form) | C-23 | Preamble gate precedes resolution bullets (C-19 passes) but follows CONSTRAINT block (C-23 fails). Scorer reads dual-gate form as satisfying C-23 without checking zero pre-gate surface. V-02 confirms. |
| C-19 awarded as C-23 (intro prose form) | C-23 | Preamble gate precedes resolution bullets (C-19 passes) but follows a single introductory sentence (C-23 fails). Minimal surface violation -- one sentence is enough to fail C-23. V-03 confirms. |
