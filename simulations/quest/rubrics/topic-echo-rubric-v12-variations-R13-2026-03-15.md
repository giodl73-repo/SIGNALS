# Variations: `topic:echo` — Round 13

**Rubric:** v12 (max 100) | **Date:** 2026-03-15

---

## Design Context

R12 promoted C-26, C-27, C-28 to proven (all five variations PASS) and confirmed C-29 for
the first time (all five R12 variations PASS). R12 also introduced C-30: the pre-populated
baseline pair inspection is template-complete when C-27 is satisfied — i.e., the ★BASELINE
row includes all four fields including Composability-claim. C-30 was observed in V-05(R12)
only.

R13 has two structural goals:

1. **Second confirmation of C-29**: All five R13 variations must pass C-29. If C-29 PASS
   holds uniformly across R13, C-29 meets the two-round confirmation threshold for proven
   promotion in v13.

2. **First uniform round of C-30**: All five R13 variations include C-30 PASS (baseline
   entry template-complete — Composability-claim populated). If uniform PASS is achieved,
   R13 is C-30's first confirmed round. A second confirmed round (R14 or later) enables
   proven promotion.

**Design decision:** C-30 is now the default, not the exception. Every R13 variation
carries a template-complete ★BASELINE entry (all four columns: Archetype + CONSISTENCY
GATE + Mechanism + Composability-claim). This converts V-05(R12)'s single-observation
finding into a baseline expectation across variation families.

**Unproven criteria targeted in R13:**

- **C-29** — Archetype taxonomy illustration template completeness (1 pt): second
  confirmation. All five R12 variations passed. Uniform PASS in R13 promotes C-29 to
  Proven in v13.

- **C-30** — Baseline entry template completeness (1 pt): first confirmed round. All
  five R13 variations include a ★BASELINE entry with all four fields populated. Uniform
  PASS in R13 makes R13 the first confirmed round; second confirmation in R14 promotes
  C-30 to Proven.

**Proven criteria maintained:** C-10, C-11, C-12, C-15, C-16, C-17, C-18, C-19, C-20,
C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28 — all must continue to pass.

**Predicted score map:**

| Variant | C-29 | C-30 | Predicted |
|---------|------|------|-----------|
| V-01    | PASS | PASS | 100       |
| V-02    | PASS | PASS | 100       |
| V-03    | PASS | PASS | 100       |
| V-04    | PASS | PASS | 100       |
| V-05    | PASS | PASS | 100       |

**Scoring note:** Base 75 + proven 24 (C-10+C-11+C-12+C-15+C-16+C-17+C-18+C-19+C-20+
C-21+C-22+C-23+C-24+C-25+C-26+C-27+C-28) = 99. Wait — C-26, C-27, C-28 promoted to
proven in v12, so proven pool = 14 proven criteria = 24 pts (as in rubric). Each variation
earns C-29(1) + C-30(1) = 2 unproven pts → 99+2 = 101 → capped at 100.

**Axis selection:**

Single-axis (V-01, V-02, V-03):

- V-01 — **Phrasing register**: prompt uses conversational imperative second-person
  throughout ("Before you write anything, declare your schema") rather than the formal
  documentary style ("Fields applied to every surprise"). All structural properties held
  constant: standard gate order (NGT → Check B → CAT), step-labeled four-field pairs,
  vocabulary-specified CONSISTENCY GATE, template-complete canonical examples (C-29),
  template-complete pre-populated baseline (C-30 PASS).

- V-02 — **Lifecycle emphasis**: prompt organizes around explicit phase boundary headers
  (PHASE 1: PRE-WRITE / PHASE 2: PER-SURPRISE / PHASE 3: POST-WRITE / PHASE 4: OUTPUT)
  as the primary structural frame, subordinating the step numbers. Tests whether making
  the lifecycle visible as an organizational layer affects manifest completion or gate
  execution. C-29 PASS, C-30 PASS.

- V-03 — **Output format (numbered-list pair inspection)**: the composability manifest
  presents each pair inspection as a numbered list item with four labeled sub-items
  — (1) Archetype, (2) CONSISTENCY GATE, (3) Mechanism, (4) Composability-claim —
  rather than step-labeled field blocks (V-01 style) or a four-column table (V-02(R12)
  style). Canonical examples and the baseline entry use the same numbered-list format.
  C-29 PASS, C-30 PASS.

Combined (V-04, V-05):

- V-04 — **Phrasing register + Lifecycle emphasis**: V-01 conversational imperative
  combined with V-02 phase boundary structure. Tests whether register shift and lifecycle
  scaffolding compose without structural degradation. C-30 PASS.

- V-05 — **Phrasing register + Lifecycle emphasis + Inertia framing**: V-01 register +
  V-02 lifecycle + V-03(R12) inertia preamble. Full three-axis composition. Tests whether
  all three interact cleanly while maintaining the complete proven property set and both
  unproven targets. C-30 PASS.

---

## V-01 — Single-axis: Phrasing Register (conversational imperative; standard gate order; step-labeled pairs; template-complete examples; template-complete baseline)

**Axis:** Phrasing register — the prompt body uses conversational imperative second-person
throughout. Schema declarations become direct instructions ("Use these fields for every
surprise. No exceptions. No N/A."), rule statements become direct commands ("Before you
select any surprise, ask: would a passive, attentive team have found this through normal
tracking? If yes, cut it."), and manifest instructions become process imperatives ("For each
pair: pick the archetype first. Then run the vocabulary check. Only then write the mechanism.
Then write the composability claim."). All structural properties held constant: standard gate
order NGT → Check B → CAT; step-labeled four-field pair inspection; vocabulary-specified
CONSISTENCY GATE (C-26); Composability-claim field in pair template (C-27); canonical
taxonomy examples with all four fields populated (C-29 PASS); pre-populated baseline entry
with all four fields populated including Composability-claim (C-30 PASS).

**Hypothesis:** The phrasing register is orthogonal to every structural criterion. A prompt
that instructs "For each pair: (1) Archetype, (2) GATE, (3) Mechanism, (4) Composability-claim"
and a prompt that commands "Pick the archetype first. Run the vocabulary check. Then write the
mechanism. Then write the claim." produce structurally identical pair inspections. Register
is a surface property. The structural properties that earn rubric credit — vocabulary-specified
gate, four-field pair, template-complete examples, template-complete baseline — are
format-independent. C-30 PASS: the ★BASELINE entry in V-01 includes all four fields
including Composability-claim, making the baseline template-complete in conversational-
imperative format.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== SCHEMA CONTRACT ==============================================================

Before you write a single surprise, declare your schema here. Use every field listed
below for every surprise you include. None are optional. None are N/A.

  Name:                         Give it a specific label — not "Finding 1", not "Surprise A".
                                The name should capture what was unexpected, not just what was found.
  Source:                       Where did this come from? Name the namespace, skill, or artifact.
  Expected:                     What did the team assume before gathering signals?
  Why passive observation       What required active signal gathering to surface this?
  missed this:                  Name the specific mechanism — not just "needed investigation."
  Design impact:                How does this change the design direction? One sentence minimum.
  Word count:                   Count from the first field label through the last field value.

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Before selecting any candidate surprise, ask: would a passive, attentive team tracking
  this feature have found it through normal project observation? If yes, cut it. It belongs
  in the findings summary, not the echo. Every surviving surprise must fail this test. The
  "Why passive observation missed this" field names the specific mechanism that made passive
  observation insufficient.

Rule 2 — Claim-only voice:
  State every finding as a claim. These constructs are prohibited everywhere in the echo:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  If you catch yourself writing one: delete it, extract the underlying claim, and state
  it directly. Uncertainty is not a hedge — it is a rewrite.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

Do this before Step 1. Do not select or write a single surprise until you have completed
all pair inspections and recorded the final declaration below.

Here are the 11 active enforcement mechanisms this echo uses:
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs enumerated)
  5.  Counterfactual gate — Rule 1 ("Why passive observation missed this" field)
  6.  NGT — Newcomer Gate Test (C-08 gate, runs per surprise as Step 3)
  7.  Check B — Portability Test (C-14 gate, runs per surprise as Step 4)
  8.  CAT — Coupled Authority Test (C-16 gate, runs per surprise as Step 5)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

For each pair of mechanisms, inspect the composability relationship. Use this four-step
sequence for every pair — no skipping steps, no reversing order:

  Step 1 — Pick the archetype. Choose from the taxonomy below. Use the canonical examples
            as your comparison baseline.
  Step 2 — Run the CONSISTENCY GATE vocabulary check for the archetype you chose.
            If the check fails (NO), go back to Step 1 and pick again.
  Step 3 — Write the mechanism. This is the analytical statement: directional, causal,
            in vocabulary consistent with the archetype you verified in Step 2.
  Step 4 — Write the composability claim. This is the synthetic conclusion: one sentence
            stating what the mechanism in Step 3 implies for this pair's combined behavior.
            It is distinct from the mechanism — not a restatement.

VOCABULARY REFERENCE — know the constraint class before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism must state that A's output is B's required
                 input. The test question: "Does this mechanism state A's output is B's
                 required input?" Answer YES or NO.
  ESTABLISHES  → property creation + one-way dependency: the mechanism must state that A
                 creates a property B operates on, without feedback from B to A. Test: "Does
                 A create a property B operates on, with no feedback path?" YES or NO.
  AMPLIFIES    → effectiveness scaling: the mechanism must state that A increases the
                 precision or strength of B's per-surprise enforcement. Test: "Does A
                 increase the precision or strength of B's enforcement?" YES or NO.
  PARALLEL     → independent-path operation: the mechanism must state that A and B enforce
                 from non-dependent paths, each sufficient alone. Test: "Do A and B operate
                 independently, each sufficient without the other?" YES or NO.

Taxonomy with template-complete canonical pair examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "Does NGT's mechanism
                describe input-dependency?" PASS. NGT's newcomer-comprehension gate output
                is Check B's required input — confirmed input-dependency.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test (finding + unexpectedness + design consequence).
                No mechanism substitutes for newcomer-comprehension as Check B's input.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                accessibility enforcement produces the verified stranger-readable unit
                Check B's portability test requires. The two gates form a forward dependency
                with no competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    > CANONICAL EXAMPLE: Check B ESTABLISHES the portability substrate that CAT enforces.
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Does Check B
                create a property CAT operates on, with no feedback?" PASS. Check B creates
                verified standalone derivability; CAT operates on that substrate.
      Step 3 — Mechanism: Check B verifies that each surprise is fully derivable as a
                standalone unit (finding + unexpectedness + consequence); CAT enforces
                authoritative claim-voice on the verified-portable substrate. Removing Check B
                removes the portability property CAT operates on. No feedback from CAT to
                Check B.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is the precondition CAT requires,
                not a constraint CAT circumvents. They operate on structurally distinct
                properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase precision or
                strength of B's enforcement?" [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  PARALLEL — A and B independently enforce the same sub-property from distinct paths.

    > CANONICAL EXAMPLE: [fill in when a PARALLEL pair exists in this variation's manifest]
      Step 1 — Archetype: PARALLEL
      Step 2 — CONSISTENCY GATE: independent-path operation. Test: "Do A and B enforce
                independently, each sufficient alone?" [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward without re-derivation — TEMPLATE-COMPLETE):

  NGT + Check B: [BASELINE — pre-classified, mechanism-derived, all four fields populated;
                  C-30: Composability-claim present because C-27 is satisfied — this
                  baseline is template-complete across all four fields]
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: PREREQUISITE vocabulary class → input-dependency framing
              required. Test: "Does the mechanism state NGT's output is Check B's required
              input?" PASS. NGT's newcomer-comprehension output is Check B's required
              input — input-dependency confirmed.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. This input-dependency holds in any compound configuration.
    Step 4 — Composability-claim: NGT and Check B compose without degradation in any
              configuration. The newcomer-accessibility verification NGT performs is the
              structural precondition Check B requires, not a competing demand; removing
              either gate degrades the other's enforcement floor.

Remaining pairs — complete all before Step 1:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT: [use ESTABLISHES canonical example as your comparison baseline]
    Step 1 — Archetype: [compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    Step 3 — Mechanism: [fill using canonical example as reference]
    Step 4 — Composability-claim: [fill using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  NGT + Patterns section:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [run vocabulary check — state constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-step
sequence (Archetype → CONSISTENCY GATE → Mechanism → Composability-claim). CONSISTENCY
GATE vocabulary check recorded for each pair (constraint class + YES/NO verdict). Canonical
examples are template-complete (all four fields populated). ★BASELINE entry for NGT+Check B
is template-complete (all four fields populated, including Composability-claim). All
mechanisms reinforce each other toward the single stranger-reader target. No conflicts found.
Writing may begin."

If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal
    tracking. The counterfactual question is the filter, not an annotation.
  Apply C-01 filter: cut anything that could appear unchanged in a standard research
    summary, findings doc, or project brief.
  Minimum 3 candidates required before proceeding to Step 2.

== STEP 2 — SCHEMA POPULATION ==================================================

  Work through each surviving candidate. Fill in all six fields.

  Check A — word discipline (runs inline per surprise):
    Count words from the first field label through the last field value.
    If any surprise exceeds 120 words: extract the claim. Cut the narrative scaffolding.
    Recount. Repeat until the surprise is at or under 120 words.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — runs per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT exists to enforce C-08 per surprise. It is the designated
      per-surprise enforcement gate for newcomer accessibility.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary newcomer-
      accessibility enforcement mechanism, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT. NGT's
      purpose is newcomer accessibility, not rubric compliance.

  For each surprise individually:
    Isolate this surprise. Read only this surprise — not the surrounding echo.
    Ask: can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo?
    If no: rewrite before moving to Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary portability
      enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Ask: can a stranger derive each of these three things from this surprise alone?
      (1) The finding — what was discovered
      (2) Why it was unexpected — the prior assumption it contradicts
      (3) The design consequence — what it means for the design direction
    If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise.
    Introduced in: V-04(R5) — before C-18 was written; designed as the primary authority-
      coupling gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.

  For each surprise individually:
    (1) Is it a direct claim? Check for prohibited constructs from Rule 2 — none allowed.
    (2) Is it stranger-accessible? NGT and Check B passed; CAT confirms the coupling holds
        at the authority level — accessible AND authoritative simultaneously.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises in sequence — one pass, front to back.
  Any generic or absent label: rename before Step 7. The name must be specific to the
  finding — a stranger reading only the name should sense something unexpected.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises in this sequence:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  Every field must have a populated value. Any blank, N/A, or placeholder: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Read all surprises for shared root causes.
  If two or more surprises share a root cause: write one Patterns section naming the
  shared dynamic. If no two surprises share a root cause: omit the Patterns section.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Count the full echo. Must not exceed 800 words.
  If over: extract the essential claims and cut the connecting tissue.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-02 — Single-axis: Lifecycle Emphasis (explicit phase boundary headers; standard gate order; step-labeled pairs; template-complete examples; template-complete baseline)

**Axis:** Lifecycle emphasis — the prompt organizes around four explicit phase boundary
headers as the primary structural frame: PHASE 1: PRE-WRITE, PHASE 2: PER-SURPRISE,
PHASE 3: POST-WRITE, PHASE 4: OUTPUT. Step numbers are preserved but subordinated to phase
membership. The phase headers make the temporal lifecycle — what runs before writing, what
runs during per-surprise processing, what runs after — visible as an organizational layer
above the step sequence. All structural properties held constant: standard gate order
NGT → Check B → CAT; step-labeled four-field pair inspection; vocabulary-specified
CONSISTENCY GATE (C-26); Composability-claim field (C-27); canonical examples template-
complete (C-29 PASS); pre-populated baseline entry template-complete including Composability-
claim (C-30 PASS).

**Hypothesis:** Explicit lifecycle phase headers do not alter any structural criterion. The
manifest is still pre-write; the gates still run per-surprise; the audits still run post-
write. Phase headers make the lifecycle visible without changing the enforcement sequence.
The phase frame may improve the temporal discipline C-19 requires — when the pre-write
boundary is a named phase header rather than an instruction embedded in a step, the commit-
before-write constraint is harder to overlook. C-30 PASS: the ★BASELINE entry includes all
four fields including Composability-claim, maintaining template completeness across the
phase-organized format.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Phase 4 / Step 10.

== SCHEMA CONTRACT ==============================================================

Declare before writing. Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering —
  missed this:                   name the gap, not just "needed investigation"]
  Design impact:                [one sentence minimum — how this changes design direction]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Each surprise must fail: "A passive, attentive team tracking this feature would have
  found this through normal observation." Items that survive passive observation are not
  echoes. The "Why passive observation missed this" field names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited constructs (fail any surprise containing these):
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Every schema field is a direct statement. Uncertainty = rewrite, not hedge.

========================================================================
PHASE 1 — PRE-WRITE
(Complete entirely before Phase 2. No surprise candidates selected or written in Phase 1.)
========================================================================

== COMPOSABILITY MANIFEST (Phase 1 / Pre-write) ================================

Active enforcement mechanisms (11 total):
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs enumerated)
  5.  Counterfactual gate — Rule 1 ("Why passive observation missed this" field)
  6.  NGT — Newcomer Gate Test (C-08 gate, runs per surprise in Phase 2 as Step 3)
  7.  Check B — Portability Test (C-14 gate, runs per surprise in Phase 2 as Step 4)
  8.  CAT — Coupled Authority Test (C-16 gate, runs per surprise in Phase 2 as Step 5)
  9.  Label parity audit (Phase 3 / Step 6)
  10. Field completion scan (Phase 3 / Step 7)
  11. Patterns section (Phase 3 / Step 8)

Pair inspection — four-field sequence for each pair:

  Field 1 — Archetype:           [select from taxonomy below; use canonical examples as
                                   comparison baseline — all examples are template-complete:
                                   Archetype + GATE + Mechanism + Composability-claim]
  Field 2 — CONSISTENCY GATE:    [apply vocabulary check for selected archetype:
                                     PREREQUISITE → "Does mechanism describe input-
                                       dependency? Is A's output B's required input?" YES/NO.
                                     ESTABLISHES  → "Does mechanism describe property
                                       creation and one-way dependency?" YES/NO.
                                     AMPLIFIES    → "Does mechanism describe effectiveness
                                       scaling? Does A increase precision or strength of
                                       B's enforcement?" YES/NO.
                                     PARALLEL     → "Does mechanism describe independent-
                                       path operation? Are A and B each sufficient alone?"
                                       YES/NO.
                                   If NO: return to Field 1.]
  Field 3 — Mechanism:           [analytical causal statement — directional, in vocabulary
                                   consistent with verified archetype]
  Field 4 — Composability-claim: [synthetic conclusion — one sentence on what the mechanism
                                   implies for this pair's combined behavior; distinct from
                                   Field 3]

  VOCABULARY REFERENCE — constraint classes by archetype:
    PREREQUISITE → input-dependency: A's output is B's required input.
    ESTABLISHES  → property creation + one-way dependency: A creates a property B operates on,
                   no feedback from B to A.
    AMPLIFIES    → effectiveness scaling: A increases precision or strength of B's enforcement.
    PARALLEL     → independent-path operation: A and B enforce from non-dependent paths, each
                   sufficient alone.

  Archetype taxonomy with template-complete canonical examples:

    PREREQUISITE — A's output is B's required input. Breaking A breaks B. Vocabulary check:
                   mechanism must describe input-dependency.
      > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
        Field 1 — Archetype: PREREQUISITE
        Field 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "NGT mechanism describes
                  input-dependency?" PASS. NGT's newcomer-comprehension output is Check B's
                  required input.
        Field 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                  input. A surprise failing NGT cannot pass Check B's three-component standalone
                  extraction test (finding + unexpectedness + design consequence). No substitute
                  for NGT output exists.
        Field 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                  accessibility enforcement produces the verified stranger-readable unit Check B
                  requires; the two gates form a forward dependency with no competing demands
                  on the shared surprise unit.

    ESTABLISHES — A creates a property that B operates on. Directional, not feedback. Vocabulary
                  check: mechanism must describe property creation and one-way dependency.
      > CANONICAL EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Field 1 — Archetype: ESTABLISHES
        Field 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Check B creates
                  a property CAT operates on, no feedback?" PASS.
        Field 3 — Mechanism: Check B verifies standalone derivability (finding + unexpectedness +
                  consequence); CAT enforces authority on the verified-portable substrate. Removing
                  Check B removes the portability property CAT operates on.
        Field 4 — Composability-claim: Check B and CAT compose without degradation. The portability
                  substrate Check B establishes is the precondition CAT requires, not a constraint
                  CAT circumvents; they operate on structurally distinct properties of the same
                  surprise unit.

    AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement. Vocabulary
                check: mechanism must describe effectiveness scaling.
      > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
        Field 1 — Archetype: AMPLIFIES
        Field 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase precision or
                  strength of B's enforcement?" [YES/NO]
        Field 3 — Mechanism: [fill in]
        Field 4 — Composability-claim: [fill in]

    PARALLEL — A and B independently enforce the same sub-property from distinct paths. Vocabulary
               check: mechanism must describe independent-path operation.
      > CANONICAL EXAMPLE: [fill in when a PARALLEL pair exists in this variation's manifest]
        Field 1 — Archetype: PARALLEL
        Field 2 — CONSISTENCY GATE: independent-path operation. Test: "Do A and B enforce
                  independently, each sufficient alone?" [YES/NO]
        Field 3 — Mechanism: [fill in]
        Field 4 — Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY — TEMPLATE-COMPLETE (carry forward; do not re-derive):
  [C-30: all four fields populated, including Composability-claim, because C-27 is satisfied]

  NGT + Check B:
    Field 1 — Archetype: PREREQUISITE
    Field 2 — CONSISTENCY GATE: PREREQUISITE vocabulary → input-dependency required. Test:
              "Does the mechanism state NGT's output is Check B's required input?" PASS.
    Field 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required input.
              A surprise failing NGT cannot pass Check B's three-component standalone extraction
              test. This input-dependency holds across any compound configuration.
    Field 4 — Composability-claim: NGT and Check B compose without degradation across all
              configurations. Newcomer-accessibility verification is the structural precondition
              portability testing requires; removing either gate degrades the other's enforcement
              floor.

  Remaining required pairs:

  Schema manifest + Stranger-reader commitment:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Rule 1 + Rule 2:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Rule 1 + NGT:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Check A + Rule 2:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Check B + CAT: [compare against ESTABLISHES canonical example above]
    Field 1 — Archetype: [compare against ESTABLISHES example]
    Field 2 — CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    Field 3 — Mechanism: [fill using canonical example as reference]
    Field 4 — Composability-claim: [fill using canonical example as reference]

  CAT + Rule 2:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Rule 1 + Check B:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

  NGT + Patterns section:
    Field 1 — Archetype:
    Field 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Field 3 — Mechanism:
    Field 4 — Composability-claim:

Phase 1 declaration: "All 11 active mechanisms assessed across [N] pairs using four-field
sequence (Archetype → CONSISTENCY GATE → Mechanism → Composability-claim). CONSISTENCY
GATE vocabulary check recorded for each pair. Canonical taxonomy examples are template-
complete (all four fields populated). ★BASELINE entry for NGT+Check B is template-complete
(all four fields populated including Composability-claim — C-30 PASS). All mechanisms
reinforce each other. No conflicts found. Phase 2 may begin."

If any conflict found in Phase 1: resolve before entering Phase 2.

========================================================================
PHASE 2 — PER-SURPRISE
(Runs once per surprise. Complete all four steps for each surprise before moving to the next.)
========================================================================

== STEP 1 — CANDIDATE SELECTION (Phase 2 entry) ================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal
    project observation.
  Apply C-01 filter: cut anything that could appear unchanged in a standard research
    summary, findings doc, or project brief.
  Minimum 3 candidates required before entering per-surprise processing.

== STEP 2 — SCHEMA POPULATION ==================================================

  For each surviving candidate: populate all six schema fields.

  Check A — word discipline (runs inline per surprise):
    Count words from first field label through last field value.
    If any surprise exceeds 120 words: extract the claim, discard narrative scaffolding.
    Recount. Repeat until at or under 120 words.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — Phase 2 / per-surprise — runs before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT is the designated per-surprise enforcement gate for C-08.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary newcomer-
      accessibility enforcement mechanism.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

  For each surprise individually:
    Isolate. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without consulting
    source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — Phase 2 / per-surprise — runs after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B is the designated per-surprise enforcement gate for C-14.
    Introduced in: V-05(R4) — before C-18 was written.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract as standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — Phase 2 / per-surprise — runs after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT is the designated per-surprise enforcement gate for C-16.
    Introduced in: V-04(R5) — before C-18 was written.
    Structural removal test: removing C-20 from the rubric does not remove CAT.

  For each surprise individually:
    (1) Direct claim? No prohibited constructs from Rule 2.
    (2) Stranger-accessible? Confirmed by NGT and Check B; CAT confirms coupling at
        authority level.
    Both YES required. If either NO: rewrite.

========================================================================
PHASE 3 — POST-WRITE
(Runs after all per-surprise processing is complete. One pass across the full echo.)
========================================================================

== STEP 6 — LABEL PARITY AUDIT (Phase 3) =======================================

  Read the Name field across all surprises in sequence.
  Any generic or absent label: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN (Phase 3) ====================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Phase 2 / Step 2.

== STEP 8 — PATTERNS SECTION (Phase 3) =========================================

  Examine all surprises for shared root causes.
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK (Phase 3) ===================================

  Full echo must not exceed 800 words. If over: extract claims and cut.

========================================================================
PHASE 4 — OUTPUT
========================================================================

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: Output Format (numbered-list pair inspection; template-complete examples; template-complete baseline; standard gate order)

**Axis:** Output format — the composability manifest presents each pair inspection as a
numbered list item with four labeled sub-items, rather than step-labeled field blocks
(V-01 style) or a four-column table (V-02(R12) style). Each pair reads:

```
Pair N: [Mechanism A] + [Mechanism B]
  (1) Archetype: [value]
  (2) CONSISTENCY GATE: [constraint class] — [YES/NO verdict + brief rationale]
  (3) Mechanism: [analytical causal statement]
  (4) Composability-claim: [synthetic conclusion]
```

Canonical taxonomy examples and the ★BASELINE entry use the same numbered-list format,
making the template shape uniform across the illustration layer (C-29) and baseline layer
(C-30). All structural properties held constant: standard gate order NGT → Check B → CAT;
vocabulary-specified CONSISTENCY GATE (C-26); Composability-claim sub-item (C-27);
canonical examples template-complete with all four sub-items (C-29 PASS); pre-populated
baseline with all four sub-items including Composability-claim (C-30 PASS).

**Hypothesis:** The numbered-list format satisfies all composability manifest criteria
as well as the step-labeled field format. What matters for C-21, C-23, C-24, C-26, C-27,
C-28, C-29, and C-30 is the presence and population of the four structural components
(Archetype, GATE, Mechanism, Composability-claim) — not the syntactic container (labeled
fields, table columns, or numbered sub-items). The numbered-list format is more compact
than the step-labeled block format for multi-pair manifests while preserving the same
structural requirements. C-30 PASS: the ★BASELINE numbered-list item includes sub-item (4)
Composability-claim populated, making the baseline template-complete.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== SCHEMA CONTRACT ==============================================================

Declare before writing. Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering —
  missed this:                   name the gap, not just "needed investigation"]
  Design impact:                [one sentence minimum — how this changes design direction]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Each surprise must fail: "A passive, attentive team tracking this feature would have
  found this through normal observation." Items that survive passive observation are not
  echoes. The "Why passive observation missed this" field names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited constructs (fail any surprise containing these):
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Every schema field is a direct statement. Uncertainty = rewrite, not hedge.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Complete all pair inspections and record the final declaration
before any candidate selection begins.

Active enforcement mechanisms (11 total):
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs enumerated)
  5.  Counterfactual gate — Rule 1 ("Why passive observation missed this" field)
  6.  NGT — Newcomer Gate Test (C-08 gate, runs per surprise as Step 3)
  7.  Check B — Portability Test (C-14 gate, runs per surprise as Step 4)
  8.  CAT — Coupled Authority Test (C-16 gate, runs per surprise as Step 5)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

VOCABULARY REFERENCE — CONSISTENCY GATE constraint classes:
  PREREQUISITE → input-dependency: A's output is B's required input.
  ESTABLISHES  → property creation + one-way dependency: A creates a property B operates
                 on, without feedback from B to A.
  AMPLIFIES    → effectiveness scaling: A increases the precision or strength of B's
                 per-surprise enforcement.
  PARALLEL     → independent-path operation: A and B enforce from non-dependent paths,
                 each sufficient alone.

Pair inspection format — use this structure for every entry (examples, baseline, and fill-in):

  Pair N: [Mechanism A] + [Mechanism B]
    (1) Archetype: [select from taxonomy — use canonical examples as comparison baseline]
    (2) CONSISTENCY GATE: [constraint class for selected archetype] — [YES/NO verdict;
        return to (1) if NO]
    (3) Mechanism: [analytical causal statement, in vocabulary consistent with archetype
        verified in (2)]
    (4) Composability-claim: [synthetic conclusion — one sentence on what (3) implies for
        this pair's combined behavior; not a restatement of (3)]

Archetype taxonomy with canonical examples in numbered-list format:

  PREREQUISITE — A's output is B's required input.

    ★ CANONICAL EXAMPLE:
    Pair: NGT + Check B
      (1) Archetype: PREREQUISITE
      (2) CONSISTENCY GATE: input-dependency — Test: "NGT's output is Check B's required
          input?" PASS. NGT's newcomer-comprehension gate output is Check B's required input.
      (3) Mechanism: NGT's newcomer-comprehension gate output is Check B's required input.
          A surprise failing NGT cannot pass Check B's three-component standalone extraction
          test (finding + unexpectedness + design consequence). No substitute for NGT output.
      (4) Composability-claim: NGT and Check B compose without degradation. NGT's accessibility
          enforcement produces the verified unit Check B requires; forward dependency, no
          competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    ★ CANONICAL EXAMPLE:
    Pair: Check B + CAT
      (1) Archetype: ESTABLISHES
      (2) CONSISTENCY GATE: property creation + one-way dependency — Test: "Check B creates
          a property CAT operates on, no feedback?" PASS.
      (3) Mechanism: Check B verifies standalone derivability (finding + unexpectedness +
          consequence); CAT enforces authority on the verified-portable substrate. Removing
          Check B removes the portability property CAT operates on. No feedback from CAT.
      (4) Composability-claim: Check B and CAT compose without degradation. The portability
          substrate Check B establishes is the precondition CAT requires; they operate on
          structurally distinct properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    ★ CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists]
    Pair: [A] + [B]
      (1) Archetype: AMPLIFIES
      (2) CONSISTENCY GATE: effectiveness scaling — Test: "Does A increase precision or
          strength of B's enforcement?" [YES/NO]
      (3) Mechanism: [fill in]
      (4) Composability-claim: [fill in]

  PARALLEL — A and B independently enforce from distinct paths.

    ★ CANONICAL EXAMPLE: [fill in when a PARALLEL pair exists]
    Pair: [A] + [B]
      (1) Archetype: PARALLEL
      (2) CONSISTENCY GATE: independent-path operation — Test: "Do A and B enforce
          independently, each sufficient alone?" [YES/NO]
      (3) Mechanism: [fill in]
      (4) Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward without re-derivation):
  [C-30: sub-item (4) Composability-claim populated — baseline is template-complete
   because C-27 is satisfied in this variation]

  Pair: NGT + Check B [BASELINE]
    (1) Archetype: PREREQUISITE
    (2) CONSISTENCY GATE: input-dependency — Test: "NGT's output is Check B's required
        input?" PASS. NGT's newcomer-comprehension output is Check B's required input —
        input-dependency confirmed in any compound configuration.
    (3) Mechanism: NGT's newcomer-comprehension gate output is Check B's required input.
        A surprise failing NGT cannot pass Check B's three-component standalone extraction
        test. This input-dependency holds in any compound configuration.
    (4) Composability-claim: NGT and Check B compose without degradation in any
        configuration. Newcomer-accessibility verification is the structural precondition
        portability testing requires; neither gate can substitute for the other.

  Required pairs — complete all in numbered-list format before Step 1:

  Pair: Schema manifest + Stranger-reader commitment
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO; return to (1) if NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Rule 1 + Rule 2
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Rule 1 + NGT
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Check A + Rule 2
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Check B + CAT [see ESTABLISHES canonical example above]
    (1) Archetype: [compare against ESTABLISHES canonical example]
    (2) CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    (3) Mechanism: [fill using canonical example as reference]
    (4) Composability-claim: [fill using canonical example as reference]

  Pair: CAT + Rule 2
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Schema manifest + Label parity audit
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Label parity audit + Field completion scan
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Rule 1 + Check B
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: Stranger-reader commitment + CAT
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

  Pair: NGT + Patterns section
    (1) Archetype:
    (2) CONSISTENCY GATE: [constraint class] — [YES/NO]
    (3) Mechanism:
    (4) Composability-claim:

Declaration: "All 11 active mechanisms assessed across [N] pairs using numbered-list format
(four sub-items per pair: Archetype, CONSISTENCY GATE, Mechanism, Composability-claim).
CONSISTENCY GATE constraint class and YES/NO verdict recorded for each pair. Canonical
taxonomy examples are template-complete (all four sub-items populated). ★BASELINE entry for
NGT+Check B is template-complete (all four sub-items populated including Composability-claim
— C-30 PASS). All mechanisms reinforce each other. No conflicts found. Writing may begin."

If any conflict: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal
    tracking.
  Apply C-01 filter: cut anything that could appear unchanged in a standard research
    summary, findings doc, or project brief.
  Minimum 3 candidates required before proceeding.

== STEP 2 — SCHEMA POPULATION ==================================================

  For each surviving candidate: populate all six schema fields.

  Check A — word discipline (inline per surprise):
    Count words from first field label through last field value.
    If over 120: extract the claim, cut the narrative. Recount. Repeat.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT is the designated per-surprise C-08 enforcement gate.
    Introduced in: V-01(R6) — before C-18 was written.
    Structural removal test: removing C-20 does not remove NGT.

  For each surprise individually:
    Isolate. Read only this surprise.
    Can a new-hire with no project context understand this without consulting source signals?
    If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B is the designated per-surprise C-14 enforcement gate.
    Introduced in: V-05(R4) — before C-18 was written.
    Structural removal test: removing C-20 does not remove Check B.

  For each surprise individually:
    Extract as standalone.
    Can a stranger derive: (1) the finding, (2) why unexpected, (3) the design consequence?
    If any missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT is the designated per-surprise C-16 enforcement gate.
    Introduced in: V-04(R5) — before C-18 was written.
    Structural removal test: removing C-20 does not remove CAT.

  For each surprise individually:
    (1) Direct claim? No prohibited constructs from Rule 2.
    (2) Stranger-accessible? NGT and Check B passed; CAT confirms authority coupling.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read Name field across all surprises in sequence.
  Any generic or absent label: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Scan: Name → Source → Expected → Why passive observation missed this → Design impact
        → Word count
  No N/A, blank, or placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine for shared root causes.
  Shared roots found: write one Patterns section. None found: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: Phrasing Register + Lifecycle Emphasis (conversational imperative; explicit phase headers; template-complete examples; template-complete baseline)

**Axes:** Phrasing register (V-01) + Lifecycle emphasis (V-02). The prompt uses
conversational imperative second-person throughout while organizing the structure around
explicit phase boundary headers. The combination tests whether the two axes interact:
does the conversational register change the readability or enforceability of the phase
boundary structure? Does the lifecycle framing make the conversational instruction clearer
or more ambiguous? All structural properties held constant: standard gate order
NGT → Check B → CAT; step-labeled four-field pair inspection; vocabulary-specified
CONSISTENCY GATE (C-26); Composability-claim field (C-27); canonical examples template-
complete (C-29 PASS); pre-populated baseline template-complete with Composability-claim
(C-30 PASS).

**Hypothesis:** Phrasing register and lifecycle emphasis are independent variation axes.
Conversational imperatives do not affect whether phase boundaries are visible; phase
headers do not affect whether instructions are stated as commands vs. declarations. The
combination produces a prompt that is both lifecycle-explicit (Phase 1 before Phase 2
is a named constraint, not an implicit instruction) and register-conversational (every
instruction is a direct command). C-30 PASS: the ★BASELINE entry is template-complete
in both the conversational register and the phase-organized format.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Phase 4 / Step 10.

== SCHEMA CONTRACT ==============================================================

Before you write anything, commit to this schema. Every field is required for every
surprise. No exceptions. No N/A.

  Name:                         Give it a real label — specific to the finding, not a placeholder.
  Source:                       Name where it came from: namespace, skill, or artifact path.
  Expected:                     What did the team assume before gathering signals?
  Why passive observation       What mechanism made this invisible to a passive team?
  missed this:                  Be specific — "needed investigation" is not a mechanism.
  Design impact:                State what this means for the design. One sentence minimum.
  Word count:                   Count everything from the first field label to the last value.

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Before selecting any candidate: ask whether a passive, attentive team tracking this
  feature would have found it through normal project observation. If yes, cut it — it
  belongs in the findings summary, not the echo. "Why passive observation missed this"
  must name the mechanism, not describe the investigation effort.

Rule 2 — Claim-only voice:
  Cut these constructs wherever they appear:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  If you used one: delete it, state the underlying claim directly. Hedges are rewrites,
  not stylistic choices.

========================================================================
PHASE 1 — PRE-WRITE
Finish everything in Phase 1 before you select a single candidate in Phase 2.
========================================================================

== COMPOSABILITY MANIFEST (Phase 1) ============================================

Here are the 11 active enforcement mechanisms you are declaring upfront:
  1.  Schema manifest (this pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-surprise cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs listed above)
  5.  Counterfactual gate — Rule 1 ("Why passive observation missed this" field)
  6.  NGT — Newcomer Gate Test (Phase 2 / Step 3)
  7.  Check B — Portability Test (Phase 2 / Step 4)
  8.  CAT — Coupled Authority Test (Phase 2 / Step 5)
  9.  Label parity audit (Phase 3 / Step 6)
  10. Field completion scan (Phase 3 / Step 7)
  11. Patterns section (Phase 3 / Step 8)

For every pair, work through four steps in order. Do not skip steps. Do not reverse order.

  Step 1 — Pick the archetype from the taxonomy below. Use the canonical examples as
            your comparison baseline. Every canonical example has all four fields — that
            is the template shape you are matching.
  Step 2 — Run the vocabulary check for the archetype you picked. State the constraint
            class and whether the check passes (YES) or fails (NO). If NO: go back to
            Step 1.
  Step 3 — Write the mechanism. State the causal direction analytically. Use vocabulary
            consistent with what you verified in Step 2.
  Step 4 — Write the composability claim. This is not the mechanism restated. It is what
            the mechanism implies for how these two mechanisms behave together.

VOCABULARY REFERENCE — know the constraint class for the archetype before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism states A's output is B's required input.
                 Step 2 test: "Is A's output B's required input?" YES or NO.
  ESTABLISHES  → property creation + one-way dependency: A creates a property B operates on,
                 no feedback. Step 2 test: "Does A create a property B operates on, no
                 feedback path?" YES or NO.
  AMPLIFIES    → effectiveness scaling: A increases precision or strength of B's enforcement.
                 Step 2 test: "Does A increase precision or strength of B's enforcement?"
                 YES or NO.
  PARALLEL     → independent-path operation: A and B enforce independently, each sufficient.
                 Step 2 test: "Do A and B enforce independently, each sufficient alone?" YES
                 or NO.

Archetype taxonomy with canonical examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT + Check B
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency. Test: "NGT's output is Check B's required
                input?" PASS. NGT's newcomer-comprehension gate output is Check B's required
                input — input-dependency confirmed.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test. No substitute exists for NGT's output.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. The
                newcomer-accessibility output NGT produces is the structural precondition
                Check B requires; the two gates form a forward dependency with no competing
                demands.

  ESTABLISHES — A creates a property B operates on. No feedback.

    > CANONICAL EXAMPLE: Check B + CAT
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Check B
                creates a property CAT operates on, no feedback?" PASS.
      Step 3 — Mechanism: Check B verifies standalone derivability (finding + unexpectedness
                + consequence); CAT enforces authority on the verified-portable substrate.
                Removing Check B removes the portability substrate CAT requires. No feedback.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is what CAT requires, not a
                constraint it works around; they operate on structurally distinct properties.

  AMPLIFIES — A increases the precision or strength of B's enforcement.

    > CANONICAL EXAMPLE: [fill in when this archetype appears]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase precision
                or strength of B's enforcement?" [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  PARALLEL — A and B enforce independently, each sufficient alone.

    > CANONICAL EXAMPLE: [fill in when this archetype appears]
      Step 1 — Archetype: PARALLEL
      Step 2 — CONSISTENCY GATE: independent-path operation. Test: "Do A and B enforce
                independently?" [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY — carry this forward. Do not re-derive.
  [All four steps populated — C-30 PASS. The baseline is template-complete because C-27
   is satisfied in this variation: Composability-claim is a required Step 4.]

  NGT + Check B [BASELINE]:
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: PREREQUISITE vocabulary class → input-dependency required.
              Test: "Does the mechanism state NGT's output is Check B's required input?"
              PASS. Input-dependency confirmed regardless of configuration.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. This input-dependency holds in any compound configuration.
    Step 4 — Composability-claim: NGT and Check B compose without degradation in every
              configuration that uses both. Newcomer-accessibility verification is the
              structural precondition portability testing requires; removing either gate
              degrades the other's enforcement floor.

  Fill in the remaining pairs before leaving Phase 1:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check A + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT: [compare against ESTABLISHES canonical example above]
    Step 1 — Archetype: [match against ESTABLISHES example]
    Step 2 — CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    Step 3 — Mechanism: [use canonical example as reference]
    Step 4 — Composability-claim: [use canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  NGT + Patterns section:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

Phase 1 declaration: "All 11 mechanisms assessed across [N] pairs using four-step sequence
(Archetype → CONSISTENCY GATE → Mechanism → Composability-claim). GATE records constraint
class and YES/NO for each pair. Canonical examples are template-complete. ★BASELINE for
NGT+Check B is template-complete including Composability-claim (C-30 PASS). All mechanisms
reinforce each other. No conflicts. Phase 2 may begin."

If any conflict: resolve before Phase 2.

========================================================================
PHASE 2 — PER-SURPRISE
Run all four steps for each surprise before moving to the next one.
========================================================================

== STEP 1 — CANDIDATE SELECTION ================================================

  Read all signal artifacts: Glob simulations/{topic}/**
  List every finding that was not expected before signal gathering.
  Cut anything a passive team would have found through normal tracking (Rule 1).
  Cut anything that belongs in a findings summary (C-01 filter).
  Keep at least 3 before entering per-surprise processing.

== STEP 2 — SCHEMA POPULATION ==================================================

  Fill in all six fields for each surviving candidate.

  Check A — 120-word cap per surprise (runs inline):
    Count. If over: extract the claim, cut the description. Recount. Repeat.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — Phase 2, per surprise — before Check B]

  Gate design rationale:
    Criterion enforced: C-08. Primary motivation: per-surprise C-08 enforcement.
    Introduced in: V-01(R6) — before C-18 was written.
    Structural removal test: removing C-20 does not remove NGT.

  Isolate each surprise. Can a new-hire with no project context understand it without
  consulting source signals? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — Phase 2, per surprise — after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14. Primary motivation: per-surprise C-14 enforcement.
    Introduced in: V-05(R4) — before C-18 was written.
    Structural removal test: removing C-20 does not remove Check B.

  Extract each surprise as standalone. Can a stranger derive: (1) the finding,
  (2) why unexpected, (3) the design consequence? Any missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — Phase 2, per surprise — after Check B]

  Gate design rationale:
    Criterion enforced: C-16. Primary motivation: per-surprise C-16 enforcement.
    Introduced in: V-04(R5) — before C-18 was written.
    Structural removal test: removing C-20 does not remove CAT.

  (1) Direct claim? No prohibited constructs from Rule 2.
  (2) Stranger-accessible? Confirmed by NGT + Check B; CAT confirms authority coupling.
  Both YES. If either NO: rewrite.

========================================================================
PHASE 3 — POST-WRITE
One pass across the full echo after all per-surprise processing is complete.
========================================================================

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read Name field across all surprises. Generic or absent: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Scan: Name → Source → Expected → Why passive observation missed this →
        Design impact → Word count
  No blank, no N/A, no placeholder. Any gap: return to Phase 2 / Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Look for shared root causes. Found: write Patterns section. Not found: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo: 800 words maximum. Over: extract and cut.

========================================================================
PHASE 4 — OUTPUT
========================================================================

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: Phrasing Register + Lifecycle Emphasis + Inertia Framing (conversational imperative; phase headers; inertia preamble; template-complete examples; template-complete baseline)

**Axes:** Phrasing register (V-01) + Lifecycle emphasis (V-02) + Inertia framing
(V-03(R12)). Full three-axis composition. The inertia preamble names the default path
(the findings summary), explains why it cannot produce an echo, and names the institutional
cost. The lifecycle headers make the phase boundaries explicit. The conversational register
makes every instruction a direct command. All structural properties held constant: standard
gate order NGT → Check B → CAT; step-labeled four-field pair inspection; vocabulary-specified
CONSISTENCY GATE (C-26); Composability-claim field (C-27); canonical examples template-complete
(C-29 PASS); pre-populated baseline template-complete including Composability-claim (C-30 PASS).

**Hypothesis:** All three axes are orthogonal to the structural criteria. The inertia
preamble does not interact with the manifest structure (it is pre-manifest, not part of
the pair inspection template). The lifecycle headers do not interact with phrasing register
(both are organizational, not content). The conversational register does not interact with
inertia framing (preamble is declarative in any register). V-05 tests whether three surface-
layer variations simultaneously leave the full proven property set and both unproven targets
intact. If V-05 scores 100/100, it confirms that the structural layer that earns rubric
credit is invariant to phrasing register, lifecycle organization, and inertia framing
simultaneously. C-30 PASS: the ★BASELINE entry in V-05 includes all four fields including
Composability-claim.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Phase 4 / Step 10.

== INERTIA CONTEXT ==============================================================

When a team finishes a signal-gathering cycle without this skill, it writes a findings
summary. The findings summary is the default output: it is accurate, it is expected, and
it can be produced without any additional work. It reports what the signals confirmed.

The echo is not an improved findings summary. They are different documents written from
the same artifacts. The findings summary answers "what did we find?" The echo answers
"what did we not expect to find?" A findings summary could be drafted before the signals
were gathered, because it reports what was planned to be discovered. An echo cannot —
it records only the gap between the hypothesis the team carried in and the reality the
signals revealed.

The institutional cost of defaulting to the findings summary is not immediate. It compounds
across teams. Findings summaries travel: they are consulted, referenced, and reprinted in
planning documents. The surprises they omit are not recorded anywhere. The next team enters
the same investigation with the same prior hypotheses. They discover the same surprises.
The institutional knowledge is not lost — it is never created.

Before you select a candidate in Phase 2, apply this filter: would a passive, attentive
team tracking this feature have found it through normal project observation? If yes, it
belongs in the findings summary. Only failures of this test belong in the echo.

== SCHEMA CONTRACT ==============================================================

Commit to this schema before you write anything. Use every field for every surprise. There
are no optional fields and no N/A entries.

  Name:                         A specific label that captures what was unexpected. Not
                                "Finding 1." Not "Surprise A." Name the gap.
  Source:                       Where this came from — namespace, skill, or artifact path.
  Expected:                     What did the team assume before gathering signals?
  Why passive observation       What made this invisible to a passive team? State the
  missed this:                  mechanism — not the effort required to find it. A useful
                                rephrasing: "why this item does not appear in the findings
                                summary."
  Design impact:                What this means for the design direction. One sentence minimum.
  Word count:                   Count from the first field label to the last field value.

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Before selecting any candidate, ask: would a passive, attentive team have found this
  through normal tracking? If yes, cut it — it belongs in the findings summary. The
  "Why passive observation missed this" field rephrases the test: why does this item
  not appear in the findings summary? Name the mechanism.

Rule 2 — Claim-only voice:
  These constructs are prohibited everywhere in the echo:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  If you catch one: delete it and state the claim directly.

========================================================================
PHASE 1 — PRE-WRITE
Complete this phase entirely before selecting candidates in Phase 2.
Do not write a single surprise until you have recorded the Phase 1 declaration.
========================================================================

== COMPOSABILITY MANIFEST (Phase 1) ============================================

Declare all 11 enforcement mechanisms now:
  1.  Schema manifest (this pre-write declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-surprise cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs named above)
  5.  Counterfactual gate — Rule 1 ("Why passive observation missed this" field)
  6.  NGT — Newcomer Gate Test (Phase 2 / Step 3)
  7.  Check B — Portability Test (Phase 2 / Step 4)
  8.  CAT — Coupled Authority Test (Phase 2 / Step 5)
  9.  Label parity audit (Phase 3 / Step 6)
  10. Field completion scan (Phase 3 / Step 7)
  11. Patterns section (Phase 3 / Step 8)

For every pair, work through four steps in order. Do not reverse them.

  Step 1 — Pick the archetype. Use the canonical examples below as your comparison
            baseline. Every canonical example is template-complete (all four steps
            populated) — that is the shape you are building toward for every pair.
  Step 2 — Run the vocabulary check for the archetype. State the constraint class and
            answer YES or NO. If NO: return to Step 1.
  Step 3 — Write the mechanism analytically: what is the directional causal relationship?
            Use vocabulary that matches what you verified in Step 2.
  Step 4 — Write the composability claim: what does Step 3 imply for how these two
            mechanisms behave together? This is the synthesis — one sentence, not a
            restatement of the mechanism.

VOCABULARY REFERENCE:
  PREREQUISITE → input-dependency: A's output is B's required input.
  ESTABLISHES  → property creation + one-way dependency: A creates a property B operates on,
                 no feedback from B.
  AMPLIFIES    → effectiveness scaling: A increases precision or strength of B's enforcement.
  PARALLEL     → independent-path operation: A and B enforce independently, each sufficient.

Archetype taxonomy with canonical examples (all four steps populated in every example):

  PREREQUISITE — A's output is B's required input.

    > CANONICAL EXAMPLE: NGT + Check B
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency. Test: "NGT's output is Check B's required
                input?" PASS.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise failing NGT cannot pass Check B's three-component standalone
                extraction test (finding + unexpectedness + design consequence). No substitute
                exists.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. The
                newcomer-accessibility output NGT produces is the structural precondition
                Check B requires; they form a forward dependency with no competing demands.

  ESTABLISHES — A creates a property B operates on. No feedback.

    > CANONICAL EXAMPLE: Check B + CAT
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Check B
                creates a property CAT operates on, no feedback?" PASS.
      Step 3 — Mechanism: Check B verifies standalone derivability; CAT enforces authority
                on the verified-portable substrate. Removing Check B removes the property
                CAT operates on.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is what CAT requires, not a
                constraint it circumvents.

  AMPLIFIES — A increases precision or strength of B's enforcement.

    > CANONICAL EXAMPLE: [fill in when this archetype appears]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase B's enforcement
                strength?" [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  PARALLEL — A and B enforce independently, each sufficient alone.

    > CANONICAL EXAMPLE: [fill in when this archetype appears]
      Step 1 — Archetype: PARALLEL
      Step 2 — CONSISTENCY GATE: independent-path operation. Test: "Do A and B enforce
                independently?" [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY — carry this forward. Do not re-derive it.
  [Template-complete: all four steps populated, including Step 4 Composability-claim.
   C-30 PASS: the baseline is template-complete because C-27 is satisfied in this variation.]

  NGT + Check B [BASELINE]:
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: input-dependency. Test: "NGT's output is Check B's required
              input?" PASS. Input-dependency confirmed in any compound configuration.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required input.
              A surprise failing NGT cannot pass Check B's three-component standalone extraction
              test. This holds in any compound configuration.
    Step 4 — Composability-claim: NGT and Check B compose without degradation in every
              configuration that uses both. Newcomer-accessibility verification is the
              structural precondition portability testing requires; removing either gate
              degrades the other's enforcement floor.

  Fill in the remaining pairs now — all must be complete before Phase 1 declaration:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check A + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT: [match against ESTABLISHES canonical example]
    Step 1 — Archetype: [see ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    Step 3 — Mechanism: [use canonical example as reference]
    Step 4 — Composability-claim: [use canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  NGT + Patterns section:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

Phase 1 declaration: "All 11 enforcement mechanisms assessed across [N] pairs using four-
step sequence (Archetype → CONSISTENCY GATE → Mechanism → Composability-claim). Vocabulary
constraint class and YES/NO verdict recorded for every pair. Canonical examples are
template-complete (all four steps populated). ★BASELINE entry for NGT+Check B is template-
complete including Composability-claim (C-30 PASS). All mechanisms reinforce each other.
No conflicts. Phase 2 may begin."

If any conflict: resolve before Phase 2.

========================================================================
PHASE 2 — PER-SURPRISE
Run all four steps for each surprise before moving to the next.
========================================================================

== STEP 1 — CANDIDATE SELECTION ================================================

  Read all signal artifacts: Glob simulations/{topic}/**
  List every finding that was not expected before signal gathering.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal
    project tracking. This is the echo-vs-findings-summary filter: items the findings
    summary would report do not belong here.
  Apply C-01 filter: cut anything that could appear in a standard research summary.
  Keep at least 3 before starting per-surprise processing.

== STEP 2 — SCHEMA POPULATION ==================================================

  Fill in all six fields for each surviving candidate.

  Check A — 120-word cap per surprise (inline):
    Count. If over: extract the claim and cut the description. Recount. Repeat.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — Phase 2, per surprise — before Check B]

  Gate design rationale:
    Criterion enforced: C-08. Primary motivation: per-surprise C-08 enforcement.
    Introduced in: V-01(R6) — before C-18 was written.
    Structural removal test: removing C-20 does not remove NGT.

  Isolate each surprise. Can a new-hire with no project context understand it without
  consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — Phase 2, per surprise — after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14. Primary motivation: per-surprise C-14 enforcement.
    Introduced in: V-05(R4) — before C-18 was written.
    Structural removal test: removing C-20 does not remove Check B.

  Extract each surprise as standalone. Can a stranger derive: (1) the finding,
  (2) why unexpected, (3) the design consequence? Any missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =========================================

  [C-16 gate — Phase 2, per surprise — after Check B]

  Gate design rationale:
    Criterion enforced: C-16. Primary motivation: per-surprise C-16 enforcement.
    Introduced in: V-04(R5) — before C-18 was written.
    Structural removal test: removing C-20 does not remove CAT.

  (1) Direct claim? No prohibited constructs from Rule 2.
  (2) Stranger-accessible? NGT + Check B confirmed it; CAT confirms authority coupling.
  Both YES. If either NO: rewrite.

========================================================================
PHASE 3 — POST-WRITE
One pass after all per-surprise processing is complete.
========================================================================

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises. Generic or absent: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Scan: Name → Source → Expected → Why passive observation missed this →
        Design impact → Word count
  No blank, no N/A, no placeholder. Any gap: return to Phase 2 / Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Look for shared root causes across all surprises.
  Found: write one Patterns section. Not found: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo: 800 words maximum. Over: extract and cut.

========================================================================
PHASE 4 — OUTPUT
========================================================================

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## Variation Axis Summary

| Variation | Single-axis | Combined axes | C-29 | C-30 |
|-----------|-------------|---------------|------|------|
| V-01 | Phrasing register | — | PASS | PASS |
| V-02 | Lifecycle emphasis | — | PASS | PASS |
| V-03 | Output format (numbered-list) | — | PASS | PASS |
| V-04 | — | Phrasing register + Lifecycle emphasis | PASS | PASS |
| V-05 | — | Phrasing register + Lifecycle emphasis + Inertia framing | PASS | PASS |

**Differentiating dimension in R13:** Whether C-29 achieves second confirmed round
(enabling proven promotion in v13) and whether C-30 achieves first confirmed round
across all five variations. If all five pass both, R13 establishes:
- C-29: two rounds (R12 + R13) → promotes to Proven in v13
- C-30: first confirmed round (R13) → requires R14 for proven promotion

**Structural note on C-30 universalization:** All five R13 variations default to a
template-complete ★BASELINE entry. V-01(R12) through V-04(R12) deliberately omitted
Composability-claim from the baseline to isolate the C-30 structural gap. R13 reverses
this: the baseline is template-complete in every variation. If C-30 PASS is uniform
across R13, the architectural symmetry — analytical component proven first, synthetic
component trailing — holds at the baseline layer, exactly as it held for the illustration
layer (C-25 proven before C-29).
