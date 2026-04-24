---
skill: quest-variate
skill_target: mock-ns
round: 5
rubric_version: 5
rubric_target: C-19, C-20, C-21, C-22
date: 2026-03-16
---

# mock-ns -- Round 5 Variations (rubric v5, C-19 + C-20 + C-21 + C-22 target)

Rubric: v5 (C-01 through C-22, 5 essential / 3 recommended / 14 aspirational, max 108).

New criteria in v5 (extracted from R4 V-05 retroactive scoring):

- **C-19** -- Dual-gate form: S-0 must contain BOTH a preamble gate (placed before the
  resolution bullets, stating the emit requirement as the step's first action) AND a
  terminal gate (placed after the resolution bullets, naming S-1 and forbidding early
  advancement). A step with only one gate form satisfies C-17 but fails C-19. Pass
  condition: preamble in the form "Before any other step begins, emit the TOPICS.md
  status line" PLUS terminal in the form "Do not begin S-1 until this line is emitted."

- **C-20** -- Tier-carry dual register: The tier-carry contract must appear in two
  independent registers: (1) the tier row's downstream-use column in the structured
  resolution table must explicitly name "S-2 and S-3" as consumers; (2) a standalone
  terminal sentence in S-0 prose must name both consumers. Either alone passes C-18;
  both together are required for C-20. Generic table cell descriptions (e.g., "Used in
  flag computation") without naming the consumers fail C-20 even if the standalone
  sentence passes C-18.

- **C-21** -- 4-op CONSTRAINT: The CONSTRAINT block (already required for C-15) must
  name at minimum 4 prohibited operation types: no category lookup, no skill selection,
  no mock generation, AND no body generation. The C-15 minimum of 3 ops is necessary
  but not sufficient. Body generation must appear explicitly as a 4th prohibition. A
  CONSTRAINT with only 3 ops passes C-15 but fails C-21.

- **C-22** -- 5-row FLAG table: The FLAG computation table must contain a dedicated row
  for HIGH-STRUCTURE critical skills at tier=1 (flag: none) as a structurally separate
  row from the HIGH-STRUCTURE non-critical catch-all row, even though both produce
  "none". C-11 allows functional collapse (rubric explicitly permits cases 1+2 merged);
  C-22 requires explicit row separation for documentation clarity. The tier=1 critical
  row must name the critical namespaces (C-16 consistent).

R4 evidence sources:
- R4 V-05 (convergent) retroactively scored 108/108 under v5 -- it already contained
  all four constructs: dual preamble+terminal gate, dual table+prose tier carry, 4-op
  CONSTRAINT including body generation, and 5-row FLAG table with tier=1 separated.
- R4 V-04 (C-17+C-18 combined target) retroactively scored 100/108 -- it had the
  correct gate and carry from V-04 but only a 3-op CONSTRAINT (no body generation) and
  a 4-row FLAG table (tier=1 critical collapsed into the non-critical catch-all).

R5 baseline: R4 V-05 structure. Each of V-01 through V-04 isolates exactly one v5
criterion failure. V-05 is the form-variant convergent -- achieves 108/108 via surface
language distinct from R4 V-05, testing criterion form-independence.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | C-21 boundary: 3-op CONSTRAINT | CONSTRAINT names 3 ops (no body generation). C-15 passes (3 ops named by type). C-21 fails (body generation not prohibited, leaving a gap where artifact content could begin before S-0 completes). All other v5 criteria pass unchanged. Predicts C-21 FAIL; score 106/108. |
| V-02 | C-22 boundary: 4-row FLAG table | FLAG table has 4 rows -- HS-critical-tier=1 collapsed into HS-non-critical catch-all ("HIGH-STRUCTURE, all other conditions"). C-11 passes (5 cases functionally covered; rubric permits collapse). C-22 fails (tier=1 critical not a distinct row). Trap: scorer awards C-22 because C-11 passes, missing that C-22 requires structural separation beyond functional coverage. Predicts C-22 FAIL; score 106/108. |
| V-03 | C-19 boundary: terminal gate only | Preamble gate removed ("Before any other step begins..."). Terminal gate retained ("Do not begin S-1 until this line is emitted."). C-17 passes (terminal gate names S-1). C-19 fails (no preamble gate present). Trap: scorer awards C-19 because C-17 passes, missing the two-gate requirement. Predicts C-19 FAIL; score 106/108. |
| V-04 | C-20 boundary: table column without named consumers | Tier row downstream-use column reads "Used in S-3 flag computation" (no consumers named). Standalone terminal sentence reads "Carry the resolved tier into S-2 and S-3." (consumers named). C-18 passes (standalone sentence names S-2+S-3). C-20 fails (table column omits consumer names; dual-register requirement unmet). Trap: scorer awards C-20 because C-18 passes and table column is present, missing that C-20 requires BOTH registers to name the consumers. Predicts C-20 FAIL; score 106/108. |
| V-05 | Convergent: all 22 criteria via alternative surface forms | R4 V-05 criteria achieved via distinct phrasings, testing form-independence. Preamble gate: "This step executes first. Emit the TOPICS.md status line below before any other step begins." Terminal gate: "S-1 must not start until that line has been written." Table carry: "Propagates to S-2 and S-3." Standalone carry: "Carry the resolved tier forward to S-2 and S-3." CONSTRAINT: 4 ops using synonyms. FLAG: same 5 rows. All 22 criteria pass via form-variant language. Predicts 108/108. |

---

## V-01 -- C-21 Boundary: 3-op CONSTRAINT (C-19 + C-20 + C-22 Pass, C-21 Deliberate Fail)

**Axis**: CONSTRAINT op-count. Tests the boundary between C-15 (3-op minimum) and C-21
(4-op requirement including body generation).
**Change from baseline**: CONSTRAINT reads "No skill selection. No category lookup. No
mock generation." -- exactly 3 ops. "No body generation." is absent.
**Hypothesis**: C-15 passes (3 ops present, named by type). C-21 fails (body generation
not prohibited, leaving a gap where a model could begin generating artifact content during
S-0 before category and skill are resolved). All other v5 criteria are unchanged: C-19
(dual gate), C-20 (dual-register carry), C-22 (5-row FLAG) all pass because their
constructs are untouched.
**Predicts**: C-01--C-20: all pass. C-21: fail. C-22: pass. Expected composite: 106/108.

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

CONSTRAINT: No skill selection. No category lookup. No mock generation. None of
these operations begin until after the TOPICS.md status line below has been emitted.

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

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                  | Flag value                                                     |
  |--------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                  | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  | CATEGORY = MIXED                                                                           | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1  | none (structural coverage reliable)                           |
  | HIGH-STRUCTURE, all other skills, any tier                                                 | none (structural coverage reliable)                           |

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

## V-02 -- C-22 Boundary: 4-row FLAG Table (C-19 + C-20 + C-21 Pass, C-22 Deliberate Fail)

**Axis**: FLAG table row structure. Tests whether the HS-critical-tier=1 case must appear
as a distinct table row, or whether functional coverage via a catch-all row is sufficient.
**Change from baseline**: FLAG table has 4 rows. The HS-critical-tier=1 row is removed;
the catch-all row reads "HIGH-STRUCTURE, all other conditions" -- covering non-critical
skills at any tier AND critical skills at tier=1 in a single row.
**Hypothesis**: C-11 passes (all 5 cases are functionally covered -- the rubric explicitly
states "Cases 1 and 2 may be collapsed into a single row when they share the same flag
value"). C-16 passes (the tier>=2 critical row still names trace-*, listen-* in its
condition cell). C-22 fails (HS-critical-tier=1 has no dedicated row; the explicit
separation required by C-22 is absent). Trap pattern: a scorer might see that C-11 passes
and 5 cases are handled, and award C-22 without checking for row-level separation.
**Predicts**: C-01--C-21: all pass. C-22: fail. Expected composite: 106/108.

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

CONSTRAINT: No skill selection. No category lookup. No mock generation. No body
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

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                  | Flag value                                                     |
  |--------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                  | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  | CATEGORY = MIXED                                                                           | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | HIGH-STRUCTURE, all other conditions                                                       | none (structural coverage reliable)                           |

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

## V-03 -- C-19 Boundary: Terminal Gate Only (C-20 + C-21 + C-22 Pass, C-19 Deliberate Fail)

**Axis**: Gate count in S-0. Tests whether a single terminal gate form satisfies C-19, or
whether C-19 strictly requires both preamble and terminal forms.
**Change from baseline**: "Before any other step begins, emit the TOPICS.md status line
below." is removed from S-0. Only the terminal gate "Do not begin S-1 until this line is
emitted." remains after the resolution bullets.
**Hypothesis**: C-17 passes (the terminal gate sentence names S-1 and makes the emit line
a required precondition -- satisfies the content requirement of C-17). C-19 fails (the
preamble gate is absent; C-19 requires both entry-position and exit-position gate forms).
Trap pattern: a scorer might award C-19 because C-17 passes, reasoning that "a gate is
present." The rubric explicitly says "A step with only one gate form satisfies C-17 but
not C-19." The preamble gate's function is to re-state the constraint at the entry of the
step, before the resolution bullets, so that a reader scanning the step knows the emit
requirement before encountering the resolution logic.
**Predicts**: C-01--C-18: all pass. C-19: fail. C-20--C-22: all pass.
Expected composite: 106/108.

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

CONSTRAINT: No skill selection. No category lookup. No mock generation. No body
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

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                  | Flag value                                                     |
  |--------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                  | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  | CATEGORY = MIXED                                                                           | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1  | none (structural coverage reliable)                           |
  | HIGH-STRUCTURE, all other skills, any tier                                                 | none (structural coverage reliable)                           |

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

## V-04 -- C-20 Trap: Table Column Without Named Consumers (C-19 + C-21 + C-22 Pass, C-18/C-20 Deliberate Probe)

**Axis**: Tier-carry register completeness. Tests whether the C-20 table-column requirement
is specifically that the downstream-use cell names S-2 and S-3, not merely that it
references tier's downstream use in some form.
**Change from baseline**: The tier row downstream-use column reads "Used in S-3 flag
computation" -- present and informative, but does not name S-2 or S-3 as consumer labels.
The standalone terminal sentence "Carry the resolved tier into S-2 and S-3." is unchanged.
**Hypothesis**: C-18 passes (standalone sentence names S-2 and S-3 as consumers --
satisfies the handoff contract). C-20 fails (the table column describes what tier is used
for but does not name the consumers by label; C-20 requires BOTH registers to contain the
named-consumer form). Trap pattern: a scorer might note that C-18 passes, a table column
is present, and the standalone sentence names consumers -- and award C-20 on the basis that
"the carry is covered." The rubric requires the table cell specifically to state "Carry into
S-2 and S-3" or equivalent naming both consumers, not a generic description of tier's role.
**Predicts**: C-01--C-19: all pass. C-20: fail. C-21--C-22: all pass.
Expected composite: 106/108.

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

CONSTRAINT: No skill selection. No category lookup. No mock generation. No body
generation. None of these operations begin until after the TOPICS.md status line
below has been emitted.

Before any other step begins, emit the TOPICS.md status line below.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                                   |
  |-----------------|----------------------------------------------------------|--------------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none                |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Used in S-3 flag computation                     |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation         |

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

If the skill-id does not appear in any row, emit an error that names the unrecognized
skill-id and points to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                                  | Flag value                                                     |
  |--------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                  | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  | CATEGORY = MIXED                                                                           | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1  | none (structural coverage reliable)                           |
  | HIGH-STRUCTURE, all other skills, any tier                                                 | none (structural coverage reliable)                           |

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

## V-05 -- Convergent (All 22 Criteria via Alternative Surface Forms)

**Axis**: Form-independence test. All four v5 criteria achieved via surface language
distinct from R4 V-05, demonstrating that the criteria are content-based and not
locked to specific phrasing.
**v5 signals by construct**:
- C-19 (dual gate): Preamble reads "This step executes first. Emit the TOPICS.md status
  line below before any other step begins." Terminal reads "S-1 must not start until the
  line above has been written." Both gates present; neither uses R4 V-05 wording.
- C-20 (dual-register carry): Table downstream-use column reads "Propagates to S-2 and
  S-3" (names both consumers). Standalone sentence reads "Carry the resolved tier forward
  to S-2 and S-3." (names both consumers). Both registers present; different surface forms.
- C-21 (4-op CONSTRAINT): "No skill lookup. No category classification. No mock
  generation. No artifact content production." -- 4 ops, synonymic phrasing, body
  generation covered by "artifact content production."
- C-22 (5-row FLAG): Same 5-row structure as R4 V-05. Condition cells use alternative
  wording in rows 4 and 5; tier=1 critical row remains explicit and separate.
**Hypothesis**: All 22 criteria pass via form-variant language. This confirms the rubric
criteria are content-based (what is said) not form-based (the exact words used). Any
implementation that provides the semantic content of each criterion should score the same
as R4 V-05 regardless of phrasing. Expected composite: 108/108.
**Predicts**: C-01--C-22 all pass. Expected score: 108/108.

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

CONSTRAINT: No skill lookup. No category classification. No mock generation. No
artifact content production. None of these operations begin until after the TOPICS.md
status line below has been written.

This step executes first. Emit the TOPICS.md status line below before any other step
begins.

Read TOPICS.md. Emit this exact line (fill in all three fields):

  > TOPICS.md: {existence: found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields must be present. Resolve each field and apply its downstream action:

  | Field           | Resolved value                                           | Downstream use                               |
  |-----------------|----------------------------------------------------------|----------------------------------------------|
  | existence       | "found" if topic in TOPICS.md; "not found" if absent     | If "not found": tier=1, tags=none            |
  | tier            | TOPICS.md value; 1 if unregistered; --tier if provided   | Propagates to S-2 and S-3                    |
  | compliance tags | Tag list from TOPICS.md; "none" if absent/unregistered   | Emit only; no effect on flag computation     |

S-1 must not start until the line above has been written.
Carry the resolved tier forward to S-2 and S-3.

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

If the skill-id is not found in any row, emit an error naming the unrecognized skill-id
and pointing to the registry. Stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Critical skills for tier-conditional refinement:
  trace-request, trace-component, trace-contract, trace-state, trace-skill,
  trace-migration, trace-deployment, scout-feasibility, listen-support,
  listen-feedback, listen-adoption

Compute FLAG from this table (evaluate top to bottom; first matching row wins):

  | Condition                                                                                  | Flag value                                                     |
  |--------------------------------------------------------------------------------------------|----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                                  | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)  |
  | CATEGORY = MIXED                                                                           | REVIEW-FOR-PLAUSIBILITY                                        |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1  | none (structural coverage reliable)                           |
  | HIGH-STRUCTURE, non-critical skills, any tier                                             | none (structural coverage reliable)                           |

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

## Predicted scoring summary

| Variate | C-19 | C-20 | C-21 | C-22 | Score |
|---------|------|------|------|------|-------|
| V-01    | pass | pass | FAIL | pass | 106   |
| V-02    | pass | pass | pass | FAIL | 106   |
| V-03    | FAIL | pass | pass | pass | 106   |
| V-04    | pass | FAIL | pass | pass | 106   |
| V-05    | pass | pass | pass | pass | 108   |

## New failure traps from R5

| Failure | Criterion | Description |
|---------|-----------|-------------|
| 3-op CONSTRAINT omits body generation | C-21 | CONSTRAINT passes C-15 (3 op types named) but fails C-21 because "body generation" or "artifact content production" is not listed as a 4th prohibited type. Model may begin generating artifact content during S-0 before category/skill are resolved. |
| HS-critical-tier=1 collapsed into catch-all | C-22 | 4-row FLAG table passes C-11 (functional coverage; rubric permits collapse) but fails C-22 because the tier=1 critical case has no dedicated row. The tier=1 case is documented only implicitly via catch-all coverage. |
| Preamble gate absent | C-19 | S-0 has a terminal gate naming S-1 (C-17 passes) but no preamble gate before the resolution bullets. A reader must scan past the resolution logic before encountering any gate language. C-19 requires both entry-position and exit-position coverage. |
| Table column describes use without naming consumers | C-20 | Table downstream-use cell says "Used in S-3 flag computation" or similar. Standalone sentence names S-2 and S-3. C-18 passes (standalone names consumers). C-20 fails (table cell must also name the consumers -- generic description of tier's use is not a named-consumer carry). |
