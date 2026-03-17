---
skill: quest-variate
skill_target: mock-ns
round: 4
rubric_version: 4
rubric_target: C-17, C-18
date: 2026-03-16
---

# mock-ns -- Round 4 Variations (rubric v4, C-17 + C-18 target)

Rubric: v4 (C-01 through C-18, 5 essential / 3 recommended / 10 aspirational).

New criteria in v4 (extracted from R3 differential analysis):

- **C-17** -- S-0 advancement gate sentence: within the S-0 step body, a sentence
  explicitly names S-1 (or equivalent next step) and states that it must not begin
  until the TOPICS.md status line has been emitted. Pass condition: "Do not begin
  S-1 until this line is emitted," "Before any other step begins, emit the TOPICS.md
  status line," or any phrasing that names the prohibited next step and makes the emit
  line a required precondition. CONSTRAINT block alone does not satisfy this criterion.

- **C-18** -- S-0 tier-carry handoff with named consumers: S-0 includes an explicit
  handoff sentence that (a) names the tier value as the carried artifact and (b) names
  at least two downstream steps by label that will consume it. Pass condition: "Carry
  the resolved tier into S-2 and S-3" or equivalent. "Carry the resolved tier forward"
  without naming consumers does not satisfy.

R3 evidence sources:
- R3 V-03 (clean S-0 separation) had the distinguishing signal: "Do not begin S-1 until
  this line is emitted" -- the sentence that names S-1 and enforces the gate (C-17).
- R3 V-02 and V-03 both had "Carry the resolved tier into S-2 and S-3" as part of their
  S-0 tier carry -- naming two downstream consumers (C-18).

R4 baseline: R3 V-04 structure augmented with C-15 (CONSTRAINT naming 3 op types) and
C-16 (FLAG table with trace-*, listen-* in condition column). Base passes C-01--C-16.
All R4 variations share the same S-1 through A-5 structure. Only S-0 varies across
V-01, V-02, V-03. V-04 combines; V-05 is convergent with enhanced lookups throughout.

Three axes selected for single-axis isolation:

1. **Lifecycle emphasis (C-17: terminal gate sentence, single-consumer carry)**
   "Do not begin S-1 until this line is emitted." placed as terminal sentence after
   resolution bullets. Carry names only S-3 ("Carry resolved tier into S-3") to
   deliberately fail C-18 for clean isolation.

2. **Role sequence (C-18: named-consumer terminal carry, no gate sentence)**
   Terminal carry sentence names S-2 and S-3 explicitly. CONSTRAINT provides ordering
   but no standalone gate sentence names S-1. Tests C-18 in isolation.

3. **Phrasing register (C-17 form test: CONSTRAINT-embedded S-1 name, no consumers)**
   CONSTRAINT block is rewritten to name S-1 as a step rather than naming operations:
   "Do not begin S-1, S-2, or S-3 until after the TOPICS.md status line has been
   emitted." Tests whether naming S-1 inside the CONSTRAINT satisfies C-17, or whether
   a standalone sentence outside the CONSTRAINT block is required.

---

## Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (C-17 terminal gate, C-18 deliberate fail) | Gate sentence "Do not begin S-1 until this line is emitted." placed as terminal statement after resolution bullets satisfies C-17. Tier carry names only S-3 ("into S-3 for flag computation") -- one consumer, not two -- deliberately fails C-18 for clean C-17 isolation. Predicts C-17 PASS, C-18 FAIL. Expected score: 18 criteria, 1 aspirational fail (C-18) = 96. |
| V-02 | Role sequence (C-18 named-consumer terminal carry, C-17 deliberate fail) | Terminal carry sentence "Carry the resolved tier into S-2 and S-3." names two downstream steps as consumers, satisfying C-18. No standalone gate sentence naming S-1 -- CONSTRAINT provides ordering but only names operations. C-17 requires a sentence naming S-1 specifically; CONSTRAINT alone does not suffice. Predicts C-17 FAIL, C-18 PASS. Expected score: 96. |
| V-03 | Phrasing register (C-17 CONSTRAINT-embedded S-1 name, C-18 deliberate fail) | CONSTRAINT block rewritten to name steps rather than operations: "Do not begin S-1, S-2, or S-3 until after the TOPICS.md status line has been emitted." Tests whether C-17 passes when S-1 is named inside the CONSTRAINT, or whether a standalone sentence outside the CONSTRAINT is required. No consumers named -- C-18 deliberate fail. Predicts C-17 uncertain (constraint form under test), C-18 FAIL. |
| V-04 | Lifecycle emphasis + role sequence (C-17 + C-18 combined, the v4 target) | Combines V-01's terminal gate sentence ("Do not begin S-1 until this line is emitted.") with V-02's named-consumer tier carry ("Carry the resolved tier into S-2 and S-3."). C-15 CONSTRAINT names 3 op types; C-16 FLAG table has trace-*, listen-* in condition column. Satisfies both C-17 and C-18 simultaneously in S-0 without structural changes elsewhere. Predicts C-01--C-18 all pass. Expected score: 100. |
| V-05 | Convergent (all excellence signals at maximum strength) | Belt-and-suspenders: (1) dual gate form -- "Before any other step begins" pre-step sentence PLUS "Do not begin S-1 until this line is emitted" named-S-1 sentence (C-17 redundant pass); (2) named-consumer carry in tabular resolution downstream-use column ("Carry into S-2 and S-3") PLUS standalone terminal carry sentence (C-18 redundant pass); (3) 4-op CONSTRAINT including body generation; (4) tabular S-1 namespace defaults; (5) tabular S-2 category lookup; (6) FLAG table with tier-conditional rows and trace-*, listen-* in condition column. Combines every confirmed excellence signal from R1 through R4 with full C-17+C-18 targeting. Predicts C-01--C-18 all reliably pass. Expected score: 100. |

---

## V-01 -- Lifecycle Emphasis: C-17 via Terminal Gate Sentence (C-18 Deliberate Fail)

**Axis**: Lifecycle emphasis -- gate sentence "Do not begin S-1 until this line is
emitted." is the terminal statement of S-0, placed after the resolution bullets. Tier
carry bullet names only S-3 ("Carry resolved tier into S-3 for flag computation") --
one downstream consumer, deliberately failing C-18 for clean C-17 isolation.
**Hypothesis**: The terminal gate sentence naming S-1 is the minimal form that satisfies
C-17. Placement after the resolution bullets rather than before them should not affect
the pass condition. The single-consumer carry confirms C-18 requires two named consumers
and that naming one is insufficient.
**Predicts**: C-17 PASS | C-18 FAIL | C-01--C-16 pass | Expected composite: 96.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: No skill selection. No category lookup. No mock generation.
None of these operations begin until after the TOPICS.md status line has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

Do not begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign CATEGORY for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any group, emit an error naming the unrecognized
skill-id and stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                               | Flag value                                                      |
  |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                               | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | CATEGORY = MIXED                                                                        | REVIEW-FOR-PLAUSIBILITY                                         |
  | CATEGORY = HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                                             | none (structural coverage reliable)                             |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it.

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

Write the fidelity warning immediately after the header, separated by ---. Choose by CATEGORY:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or partially
    fabricated. Review for plausibility before accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden structural pattern of {skill-id}:
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures in expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms present (role cards, numeric rubric, scoring ranges)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative

A reader familiar with the real {skill-id} output must be able to identify the
skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-02 -- Role Sequence: C-18 via Named-Consumer Terminal Carry (C-17 Deliberate Fail)

**Axis**: Role sequence -- the tier resolution bullet contains only the value-resolution
rule (no downstream action clause), but a terminal sentence after the bullets states
"Carry the resolved tier into S-2 and S-3." This places the named-consumer carry as a
standalone sentence outside the resolution bullets, naming S-2 and S-3 explicitly.
No standalone gate sentence names S-1 -- the CONSTRAINT provides ordering but its
prohibition statement names operations ("skill selection, category lookup") not steps.
**Hypothesis**: "Carry the resolved tier into S-2 and S-3." satisfies C-18 as a terminal
sentence regardless of position in S-0. CONSTRAINT-only ordering does not satisfy C-17
because C-17 requires a sentence naming S-1 specifically, not just the operations that
S-1 encompasses. The isolation confirms that the carrier of C-18 is the two-consumer
naming, independent of gate presence.
**Predicts**: C-17 FAIL | C-18 PASS | C-01--C-16 pass | Expected composite: 96.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: No skill selection. No category lookup. No mock generation.
None of these operations begin until after the TOPICS.md status line has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

Carry the resolved tier into S-2 and S-3.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign CATEGORY for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any group, emit an error naming the unrecognized
skill-id and stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                               | Flag value                                                      |
  |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                               | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | CATEGORY = MIXED                                                                        | REVIEW-FOR-PLAUSIBILITY                                         |
  | CATEGORY = HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                                             | none (structural coverage reliable)                             |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it.

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

Write the fidelity warning immediately after the header, separated by ---. Choose by CATEGORY:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or partially
    fabricated. Review for plausibility before accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden structural pattern of {skill-id}:
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures in expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms present (role cards, numeric rubric, scoring ranges)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative

A reader familiar with the real {skill-id} output must be able to identify the
skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-03 -- Phrasing Register: C-17 Form Test via CONSTRAINT-Embedded S-1 Name (C-18 Deliberate Fail)

**Axis**: Phrasing register -- the CONSTRAINT block is rewritten to name steps by label
rather than operations by type: "Do not begin S-1, S-2, or S-3 until after the
TOPICS.md status line below has been emitted." The sentence naming S-1 appears inside
the CONSTRAINT block rather than as a standalone terminal sentence outside it. No
consumers named in the carry -- "Carry resolved tier forward" deliberately fails C-18.
**Hypothesis**: C-17 requires "within the S-0 step body, a sentence explicitly names S-1
and states it must not begin until the TOPICS.md status line is emitted." The CONSTRAINT
is within the S-0 step body. If C-17 is a content requirement (S-1 must be named, emit
must be the precondition), the CONSTRAINT-embedded form passes. If C-17 is also a form
requirement (standalone sentence outside the CONSTRAINT block), this form fails. This is
the discriminating test: form-agnostic vs form-specific pass condition.
**Predicts**: C-17 uncertain (form under test) | C-18 FAIL | C-01--C-16 pass.
If C-17 passes: expected composite 96. If C-17 fails: 94.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not begin S-1, S-2, or S-3 until after the TOPICS.md status line
below has been emitted. No category lookup. No mock generation.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier forward.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign CATEGORY for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any group, emit an error naming the unrecognized
skill-id and stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                               | Flag value                                                      |
  |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                               | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | CATEGORY = MIXED                                                                        | REVIEW-FOR-PLAUSIBILITY                                         |
  | CATEGORY = HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                                             | none (structural coverage reliable)                             |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it.

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

Write the fidelity warning immediately after the header, separated by ---. Choose by CATEGORY:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or partially
    fabricated. Review for plausibility before accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden structural pattern of {skill-id}:
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures in expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms present (role cards, numeric rubric, scoring ranges)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative

A reader familiar with the real {skill-id} output must be able to identify the
skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-04 -- Lifecycle Emphasis + Role Sequence: C-17 + C-18 Combined (The v4 Target)

**Axis**: Two-axis combination: (1) V-01's terminal gate sentence ("Do not begin S-1
until this line is emitted.") satisfying C-17, and (2) V-02's named-consumer carry
("Carry the resolved tier into S-2 and S-3.") satisfying C-18. The two sentences are
both present in S-0 as separate lines -- gate sentence as the terminal statement, carry
sentence embedded in the tier resolution bullet action clause.
**Hypothesis**: C-17 and C-18 are additive -- satisfying both simultaneously requires
only two sentence additions to the base S-0 structure, with no interaction effects.
The CONSTRAINT names 3 op types (C-15), the FLAG table has trace-*/listen-* in the
condition column (C-16), and the A-step assembly labels cover C-14. This is the prompt
the v4 rubric designates as the target -- the minimal change from V-01 that also
satisfies C-18.
**Predicts**: C-01--C-18 all pass. Expected composite: 100.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write the artifact and emit the next-step line.

INPUTS
  Topic:     {topic}
  Namespace: {namespace}   (scout | draft | review | flow | trace | prove | listen |
                            program | topic)
  --skill    {skill-id}    (optional)
  --tier     1 | 2 | 3     (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: No skill selection. No category lookup. No mock generation.
None of these operations begin until after the TOPICS.md status line has been emitted.

Read TOPICS.md. Emit this exact line:

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

All three fields (existence, tier, compliance tags) must appear. Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-2 and S-3.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Record in emit only -- compliance tags have no direct effect on flag computation.

Do not begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is provided, use it. Otherwise select the representative default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded as meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Assign CATEGORY for the selected skill. Match to exactly one group:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any group, emit an error naming the unrecognized
skill-id and stop. Do not assign a fallback category.

---

STEP S-3 -- FLAG COMPUTATION

Compute FLAG from this table (evaluate top to bottom; use the first matching row):

  | Condition                                                                               | Flag value                                                      |
  |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                               | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | CATEGORY = MIXED                                                                        | REVIEW-FOR-PLAUSIBILITY                                         |
  | CATEGORY = HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | CATEGORY = HIGH-STRUCTURE (all other cases)                                             | none (structural coverage reliable)                             |

Compliance override (applied last, regardless of row match above):
  If TOPICS.md compliance tags are present AND skill-id is scout-compliance or
  trace-permissions: FLAG = "REAL-REQUIRED (compliance-sensitive)"

FLAG is now resolved. Do not recompute or modify it.

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

Write the fidelity warning immediately after the header, separated by ---. Choose by CATEGORY:

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. The structure, sections, and enforcement
    mechanisms are reliable. Content is synthetically generated but structurally
    representative. Adequate for structural planning at Tier 1. REAL-REQUIRED at
    Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. The content below is structurally
    correct but evidentially fabricated. Do not use this output to draw conclusions
    about {topic}. The sections are right; the contents are invented. A real
    {skill-id} run is required before any evidence-based decision can be made.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims may be partially accurate or partially
    fabricated. Review for plausibility before accepting coverage.

---

STEP A-3 -- GENERATE ARTIFACT BODY

Generate the mock body following the golden structural pattern of {skill-id}:
  - Correct section headings for {skill-id}
  - All required tables, lists, and scoring structures in expected positions
  - Gate or verdict line where the skill produces one
  - Enforcement mechanisms present (role cards, numeric rubric, scoring ranges)
  - Use {topic} as subject throughout
  - All values are synthetic but structurally representative

A reader familiar with the real {skill-id} output must be able to identify the
skill from the body alone, without reading the header block.

---

STEP A-4 -- WRITE ARTIFACT

Write the complete artifact (header + warning + body) to:
  simulations/mock/{topic}-{namespace}-mock-{date}.md

Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

---

STEP A-5 -- NEXT-STEP LINE

The final line of the artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

Omit only if this skill was called from within a mock-review session to regenerate
a thin namespace.
```

---

## V-05 -- Convergent (All Excellence Signals at Maximum Strength)

**Axis**: All confirmed excellence signals from R1 through R4 combined at maximum
strength: (1) dual gate form -- "Before any other step begins, emit the TOPICS.md
status line below" PLUS "Do not begin S-1 until this line is emitted" (belt-and-
suspenders for C-17, covering both listed equivalents); (2) named-consumer carry in
both the tabular resolution downstream-use column AND as a standalone terminal sentence
(belt-and-suspenders for C-18); (3) 4-op CONSTRAINT including body generation as a
fourth guarded operation; (4) tabular S-1 namespace defaults with exclusion column;
(5) tabular S-2 category lookup; (6) FLAG table with tier-conditional rows and
trace-*/listen-* patterns directly in condition column cells (C-16); (7) error-stop
on unrecognized skill-id with name-the-id language (C-13); (8) A-1 through A-5 labeled
assembly steps (C-14).
**Hypothesis**: No prior convergent has included all C-17 and C-18 signals alongside the
full R1/R2/R3 heritage. Belt-and-suspenders on both new criteria eliminates any
ambiguity about whether a single form is sufficient. The dual gate and dual carry add
only ~3 lines to S-0 while closing every known failure mode. All 18 criteria pass
reliably.
**Predicts**: C-01--C-18 all reliably pass. Expected composite: 100.

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

  | Condition                                                                        | Flag value                                                      |
  |----------------------------------------------------------------------------------|-----------------------------------------------------------------|
  | CATEGORY = EVIDENCE-HEAVY                                                        | REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)    |
  | CATEGORY = MIXED                                                                  | REVIEW-FOR-PLAUSIBILITY                                         |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier >= 2 | none (structural coverage reliable; REAL-REQUIRED at Tier 2+) |
  | HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-* AND tier = 1  | none (structural coverage reliable)                            |
  | HIGH-STRUCTURE, all other skills, any tier                                       | none (structural coverage reliable)                             |

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

Write the fidelity warning immediately after the header, separated by ---. Choose by CATEGORY:

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
