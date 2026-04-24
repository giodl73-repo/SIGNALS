
# Variations: `topic:echo` — Round 9

**Rubric:** v8 (max 100) | **Date:** 2026-03-15

---

## Design Context

R8 differentiating evidence: V-01(R8) demonstrated C-23 (archetype classification — template
requires archetype selection from finite taxonomy before mechanism fill-in; mechanism consistent
with selected archetype). V-04(R8) and V-05(R8) demonstrated the C-23 FAIL boundary: causal
direction stated without archetype selection field satisfies C-21 but not C-23. R8 also
confirmed C-22 as proven (all five R8 variations pass; C-22 now carries 2 pts in base).

Two unproven criteria in v8:

- **C-21** — Composability manifest causal depth (1 pt, unproven): each pair inspection
  articulates the directional causal mechanism — not just "A and B reinforce" but "A's
  output is B's required input" or "A establishes the property that B enforces."
- **C-23** — Composability manifest archetype classification (1 pt, unproven): each pair
  inspection classifies the causal relationship using a named archetype from the finite
  taxonomy (PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL) before stating the mechanism.

**R8 V-01 against v8 scoring (inheriting 100/100):** V-01(R8) demonstrates both C-21 and
C-23. It was designed to target C-21 and incidentally demonstrated C-23 as a new quality
dimension. R9 needs five variations that isolate and combine these structural requirements
to confirm both as proven.

**Predicted score map:**

| Variant | C-19 | C-20 | C-21 | C-22 | C-23 | Predicted |
|---------|------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | FAIL | PASS | 100       |
| V-02    | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-03    | PASS | PASS | FAIL | PASS | FAIL | 100       |
| V-04    | PASS | PASS | PASS | PASS | PASS | 100       |
| V-05    | PASS | PASS | PASS | PASS | PASS | 100       |

All five score 100: R8 baselines already exceed the aspirational budget cap before C-21
and C-23 are factored. Architectural differentiation lies in which new criteria each
variation satisfies.

**Axis selection:**

Single-axis (V-01, V-02, V-03):
- V-01 — C-23 isolation: full archetype taxonomy with internal consistency check; gate
  rationale without provenance (C-22 FAIL confirms C-23 is orthogonal to C-22)
- V-02 — C-21 pass / C-23 fail: causal direction in manifest (free-form mechanism field,
  no archetype taxonomy); full gate provenance isolating C-23 as the missing dimension
- V-03 — C-21 failure: verdict+achievement manifest (what each pair achieves, not why
  A causes B); full gate provenance confirms C-21/C-23 as the failure axis

Combined (V-04, V-05):
- V-04 — compound maximum: full archetype taxonomy + internal consistency + gate provenance
  (C-21 + C-22 + C-23 all pass)
- V-05 — distribution audit extension: extends V-04 with post-inspection archetype
  distribution summary (reveals macro enforcement pipeline structure)

---

## V-01 — Single-axis: Archetype Classification (C-23 structural enforcement, C-22 absent)

**Axis:** Composability manifest pair inspection format — template requires archetype
selection from finite taxonomy before mechanism fill-in, plus explicit consistency check
instruction. Gate rationale carries criterion attribution and structural removal test (C-20
PASS) but no round provenance, isolating C-23 as the single new axis. C-22 FAIL because no
"Introduced in" field in gate rationale.

**Hypothesis:** Archetype classification (C-23) requires two structural elements that C-21
alone does not: (1) archetype selection from a finite, named set preceding the mechanism
statement, and (2) a consistency check instruction establishing that the mechanism must be
verifiable against the selected archetype. Neither element is present in a free-form causal
direction template. C-22 FAIL isolates C-23 as the differentiating axis; C-21 PASS is
inherited from the archetype template (mechanism field still present and directional).

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

REQUIRED BEFORE Step 1. Complete all pair inspections and declare before any candidate
selection begins. Do not write surprises until the final declaration is recorded.

Active enforcement mechanisms (11 total):
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs enumerated)
  5.  Counterfactual gate — Rule 1 ("Why passive observation missed this" field)
  6.  NGT — Newcomer Gate Test (C-08 gate, runs per surprise before Check B)
  7.  Check B — Portability Test (C-14 gate, runs per surprise after NGT)
  8.  CAT — Coupled Authority Test (C-16 gate, runs per surprise after Check B)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

Pair inspection — ARCHETYPE CLASSIFICATION REQUIRED:

  For each pair:
    Step 1: Select archetype from the finite taxonomy below (must precede mechanism)
    Step 2: State mechanism in terms consistent with the selected archetype

  Taxonomy (finite — select exactly one per pair):
    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. In any novel
                    compound configuration, this ordering constraint holds: inserting a
                    mechanism between A and B that transforms A's output into something
                    B cannot consume breaks the enforcement path.
    ESTABLISHES   — A creates a property that B operates on. Directional but not input-
                    dependent: B's behavior depends on A's property holding, but A does
                    not consume B's output. Removing A removes the property B verifies.
    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    B operates without A but produces weaker enforcement. In compound
                    configurations, the amplification relationship holds independently
                    of other mechanisms in the chain.
    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Each can satisfy the criterion alone. No mutual dependency; neither
                    is a prerequisite for the other. In novel compound configurations,
                    the parallel relationship persists: adding mechanisms does not convert
                    this pair to PREREQUISITE or AMPLIFIES.

  Consistency check: every mechanism statement must be verifiable against its selected
  archetype. A PREREQUISITE archetype whose stated mechanism describes mutual amplification
  fails internal consistency — the classification is self-contradicting. An evaluator
  reading [archetype + mechanism] can verify consistency without inspecting the full manifest.

  Required pairs (inspect all; add any pair where conflict is possible):

  Schema manifest + Stranger-reader commitment:
    Archetype: [PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL]
    Mechanism: [state mechanism consistent with selected archetype]

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + NGT:
    Archetype: [select]
    Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Archetype: [select]
    Mechanism: [fill in]

  NGT + Check B:
    Archetype: PREREQUISITE
    Mechanism example: "NGT is a PREREQUISITE for Check B: NGT's newcomer-comprehension
    gate output (a verified stranger-readable surprise) is Check B's required input; a
    surprise failing NGT cannot pass Check B's three-component standalone extraction test.
    This ordering holds in any compound configuration: no mechanism inserted between NGT
    and Check B can substitute for newcomer-comprehension verification."

  Check B + CAT:
    Archetype: ESTABLISHES
    Mechanism example: "Check B ESTABLISHES the structural portability property that CAT
    enforces: Check B verifies that a surprise is fully derivable as a standalone unit
    (finding + unexpectedness + consequence); CAT then enforces that this verified-portable
    unit is stated with authoritative claim-voice. The portability property (Check B's output)
    is the substrate for CAT's authority-coupling test; removing Check B removes the property
    CAT verifies."

  CAT + Rule 2:
    Archetype: [select]
    Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Archetype: [select]
    Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + Check B:
    Archetype: [select]
    Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Archetype: [select]
    Mechanism: [fill in]

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected with archetype
  classification and mechanism statements consistent with selected archetypes. All
  mechanisms reinforce each other toward the single stranger-reader target. No conflicts
  found. Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal tracking.
  Apply C-01 filter: cut anything that could appear unchanged in a standard research summary,
    findings doc, or project brief.
  Minimum 3 candidates required before proceeding to Step 2.

== STEP 2 — SCHEMA POPULATION ==================================================

  For each surviving candidate: populate all six schema fields.

  Check A — word discipline (runs inline per surprise):
    Count words from first field label through last field value.
    If any surprise exceeds 120 words: extract the claim, discard narrative scaffolding.
    Recount. Repeat until ≤120 words.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — runs per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT exists to enforce C-08 per surprise. C-08 requires each
      surprise to be independently accessible to a newcomer; NGT is the designated
      per-surprise enforcement mechanism for this requirement. This motivation is
      independent of rubric gating requirements: C-08's accessibility demand exists
      regardless of how enforcement is documented.
    Structural removal test: removing C-20 from the rubric does not remove NGT.
      C-08 still requires per-surprise newcomer accessibility enforcement, and NGT
      is still the primary mechanism for that requirement.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise. C-14 requires each
      surprise to stand alone as a self-contained institutional claim; Check B is the
      designated per-surprise enforcement mechanism for that requirement.
    Structural removal test: removing C-20 from the rubric does not remove Check B.
      C-14 still requires per-surprise portability enforcement, and Check B is still
      the primary mechanism for that requirement.

  For each surprise individually:
    Extract this surprise as a standalone block.
    A reader who has never seen this project reads only this block.
    Can they derive: (1) the finding, (2) why it was unexpected, (3) the design consequence?
    If any component is missing or requires external context: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise. C-16 requires each
      surprise to pass both the stranger-reader test and the no-hedging test as a
      coupled unit; CAT is the designated per-surprise enforcement mechanism for that
      requirement.
    Structural removal test: removing C-20 from the rubric does not remove CAT.
      C-16 still requires per-surprise coupled enforcement, and CAT is still the
      primary mechanism for that requirement.

  For each surprise individually:
    (1) Is this surprise stated as a direct claim? (No prohibited constructs from Rule 2.)
    (2) Is this surprise accessible to a stranger without project context? (NGT and Check B
        must have already passed; CAT confirms the coupling holds at authoritative-voice level.)
    Both must be YES. If either is NO: rewrite before continuing.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises in sequence.
  Every Name field must be: present, specific, and descriptive of its content.
  Failing labels: "Finding N", "Surprise A", any generic category header.
  Any generic or absent label: rename before continuing to Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises in sequence:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  Every field must contain substantive content. No N/A, no blank, no placeholder text.
  Any gap: return to Step 2 for that surprise.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  If any two surprises share a root cause: write one Patterns section after all surprises.
    Name the shared dynamic explicitly. One sentence per pattern. Do not redescribe the
    individual surprises.
  If no shared roots: omit the Patterns section.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Count all words in the full echo: schema fields, labels, patterns section, all content.
  If total exceeds 800 words: extract and cut. The echo is a claim document, not a narrative.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-02 — Single-axis: Causal Direction Without Archetype (C-21 PASS, C-23 FAIL)

**Axis:** Composability manifest pair inspection format — template requires directional
causal mechanism per pair (free-form mechanism field) but no archetype taxonomy field.
Gate rationale carries full provenance (C-22 PASS), isolating C-23 as the single failing
dimension.

**Hypothesis:** Free-form causal direction ("A is a prerequisite for B: [mechanism]")
satisfies C-21's requirement that the directional causal mechanism be stated, but does not
satisfy C-23's requirement for archetype selection from a finite taxonomy before the
mechanism. The distinction is classification vs description: C-21 requires a directional
description; C-23 requires a taxonomic classification that makes the relationship type
finite, auditable, and internally verifiable. Free-form mechanisms can express the same
content as archetype+mechanism pairs but without the predictive constraint class the
archetype name encodes. C-22 PASS via gate provenance confirms that C-23 is orthogonal
to C-22 — gate design integrity and archetype classification are independent quality axes.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== SCHEMA CONTRACT ==============================================================

Declare before writing. Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering]
  missed this:
  Design impact:                [one sentence minimum — how this changes design direction]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Passive-team test. "Why passive observation missed this" names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited: may suggest / appears to indicate / seems like / could mean /
              it is possible that / might be / could indicate / it seems
  Every schema field is a direct statement.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Complete all pair inspections with causal direction and declare
before any candidate selection begins.

Active enforcement mechanisms (11 total):
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs)
  5.  Counterfactual gate — Rule 1
  6.  NGT — Newcomer Gate Test (C-08 gate)
  7.  Check B — Portability Test (C-14 gate)
  8.  CAT — Coupled Authority Test (C-16 gate)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

Pair inspection — CAUSAL DIRECTION REQUIRED:

  For each pair, state the directional causal mechanism of reinforcement. The mechanism
  statement must be specific enough that an external evaluator could predict the pair's
  behavior in a novel mechanism combination containing both mechanisms.

  Acceptable causal direction forms:
    "A is a prerequisite for B: [A's output is B's required input — state specific output
     and input]"
    "A establishes the property that B enforces: [A creates condition X; B verifies X
     holds per surprise]"
    "A amplifies B's enforcement per surprise: [A's act increases precision of B's check
     in this specific way]"
    "A and B are parallel paths: [both independently enforce sub-property X from distinct
     routes — describe how each reaches the same property independently]"

  Required pairs:

  Schema manifest + Stranger-reader commitment:
    Direction: [state mechanism — A's directional causal relationship to B]

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Direction: [fill in]

  Rule 1 + NGT:
    Direction: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Direction: [fill in]

  NGT + Check B:
    Direction: "NGT is a prerequisite for Check B: NGT's newcomer-comprehension gate
    output (a verified stranger-readable surprise) is Check B's required input; a
    surprise that fails NGT cannot pass Check B's three-component standalone extraction
    test (the stranger-accessible precondition for Check B is already broken)."

  Check B + CAT:
    Direction: "Check B establishes the portability property that CAT enforces: Check B
    verifies structural portability (finding + unexpectedness + consequence derivable
    standalone); CAT verifies that the verified-portable unit is stated with authoritative
    claim-voice. The portability sub-property is Check B's output and CAT's required
    substrate."

  CAT + Rule 2:
    Direction: [fill in]

  Schema manifest + Label parity audit:
    Direction: [fill in]

  Label parity audit + Field completion scan:
    Direction: [fill in]

  Rule 1 + Check B:
    Direction: [fill in]

  Stranger-reader commitment + CAT:
    Direction: [fill in]

  Declaration: "All 11 active mechanisms assessed with causal direction confirmed per pair.
  All mechanisms reinforce each other toward the single stranger-reader target. No conflicts
  found. Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate not expected before gathering signals.
  Apply Rule 1 + C-01 filter. Minimum 3 candidates required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six schema fields per candidate.
  Check A — word discipline (inline per surprise): 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — runs per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT enforces C-08 per surprise. C-08's per-surprise accessibility
      requirement exists independently of how enforcement is documented; NGT is the
      designated enforcement mechanism.
    Structural removal test: removing C-20 from the rubric does not remove NGT — C-08
      still requires per-surprise newcomer accessibility enforcement.
    Introduced in: V-03(R6) — first variation in this skill's lineage to install NGT
      as a named discrete per-surprise C-08 gate. V-03(R6) was designed in Round 6,
      predating C-18 as a rubric criterion (C-18 introduced in rubric v6 at the R5/R6
      boundary). NGT's criterion-enforcement motivation predates the gating requirement.

  For each surprise individually:
    Can a new-hire with no prior project exposure understand this without consulting
    source signals? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B enforces C-14 per surprise. C-14's per-surprise
      portability requirement exists independently of how enforcement is documented.
    Structural removal test: removing C-20 from the rubric does not remove Check B —
      C-14 still requires per-surprise portability enforcement.
    Introduced in: V-05(R4) — first variation to install Check B as a named per-surprise
      portability gate. V-05(R4) predates C-18 as a rubric criterion by two rounds;
      Check B's portability enforcement motivation is documented prior to any gating
      requirement existing in the rubric.

  For each surprise individually:
    Extract as standalone block. Can reader derive: (1) finding, (2) why unexpected,
    (3) design consequence? If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT enforces C-16 per surprise. C-16's coupled requirement
      exists independently of how enforcement is documented.
    Structural removal test: removing C-20 from the rubric does not remove CAT —
      C-16 still requires per-surprise coupled enforcement.
    Introduced in: V-05(R5) — first variation to install CAT as a named per-surprise
      C-16 gate. V-05(R5) predates C-18 as a rubric criterion by one round; CAT's
      coupling enforcement motivation predates the gating requirement.

  For each surprise individually:
    (1) No prohibited constructs from Rule 2.
    (2) Accessible to a stranger without project context.
    Both required. If either fails: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Name field across all surprises: every label specific and descriptive. No generic labels.
  Rename any "Finding N", "Surprise A", or category-header labels before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  All six fields populated across all surprises. No N/A, blank, or placeholder.
  Any gap: return to Step 2 for that surprise.

== STEP 8 — PATTERNS + FINAL CHECK =============================================

  Patterns: if any two surprises share a root cause, write Patterns section naming the
    shared dynamic. Else omit.
  Word count: full echo ≤800 words. Extract and cut if exceeded.

== STEP 9 — WRITE ARTIFACT =====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: Achievement-Only Manifest (C-21 FAIL, C-23 FAIL)

**Axis:** Composability manifest pair inspection depth — each pair inspection records a
verdict (reinforcing / non-conflicting / conflicting) and a one-sentence achievement
describing what the mechanism combination produces toward the writing goal. The achievement
field describes the output quality the pair enforces together — not the directional causal
mechanism of their interaction. Gate rationale carries full provenance (C-22 PASS).

**Hypothesis:** A composability manifest that inspects each pair and records verdict +
achievement satisfies C-19 (pair inspection completed, mutual reinforcement declared pre-
write) but fails C-21 (causal direction not stated — achievement descriptions answer "what
does this pair achieve?" not "why does A cause B's required input?"). Achievement statements
are forward-looking output claims; causal mechanisms are backward-looking explanatory claims.
The structural test: "NGT and Check B together produce a newcomer-accessible portable
surprise" (achievement) vs "NGT's newcomer-comprehension gate output is Check B's required
input" (mechanism). Both inspect the pair; only the mechanism statement satisfies C-21.
C-23 FAIL follows from C-21 FAIL — archetype classification requires that a causal direction
be stated at all.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== SCHEMA CONTRACT ==============================================================

Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering]
  missed this:
  Design impact:                [one sentence minimum]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Passive-team test. "Why passive observation missed this" names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited: may suggest / appears to indicate / seems like / could mean /
              it is possible that / might be / could indicate / it seems

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Record all pair assessments and declare before writing begins.

Active enforcement mechanisms (11 total):
  1.  Schema manifest
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs)
  5.  Counterfactual gate — Rule 1
  6.  NGT — Newcomer Gate Test (C-08 gate)
  7.  Check B — Portability Test (C-14 gate)
  8.  CAT — Coupled Authority Test (C-16 gate)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

Pair inspection — for each pair, assess and record:

  Verdict: [reinforcing / non-conflicting / conflicting]
    reinforcing    — together these mechanisms produce stronger output than either alone
    non-conflicting — mechanisms operate on different properties without interfering
    conflicting    — one mechanism undermines the other (must resolve before writing)

  Achievement: [one sentence — what quality property does this mechanism combination enforce
                in the finished echo?]

  Schema manifest + Stranger-reader commitment:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Achievement: [what this combination enforces in the echo]

  Rule 1 + Rule 2:
    Verdict: [...]
    Achievement: [...]

  Rule 1 + NGT:
    Verdict: [...]
    Achievement: [...]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Verdict: [...]
    Achievement: [...]

  NGT + Check B:
    Verdict: reinforcing
    Achievement example: "NGT and Check B together enforce that each surprise is both
    newcomer-comprehensible and fully self-contained as a standalone institutional claim."

  Check B + CAT:
    Verdict: reinforcing
    Achievement example: "Check B and CAT together enforce that each surprise is portable
    in structure and authoritative in voice — structurally self-contained and claim-stated."

  CAT + Rule 2:
    Verdict: [...]
    Achievement: [...]

  Schema manifest + Label parity audit:
    Verdict: [...]
    Achievement: [...]

  Label parity audit + Field completion scan:
    Verdict: [...]
    Achievement: [...]

  Rule 1 + Check B:
    Verdict: [...]
    Achievement: [...]

  Stranger-reader commitment + CAT:
    Verdict: [...]
    Achievement: [...]

  Declaration: "All 11 active mechanisms inspected. [N] pairs reinforcing, [M] non-conflicting,
  0 conflicting. All mechanisms reinforce each other toward the stranger-reader target.
  Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**. Read all signals. List candidates not expected before
  gathering signals. Apply Rule 1 + C-01 filter. Minimum 3 required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six schema fields per candidate. Check A: 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT enforces C-08 per surprise. This motivation is independent
      of rubric gating requirements: C-08's accessibility demand exists regardless of
      how enforcement is documented. NGT is the primary mechanism for that demand.
    Structural removal test: removing C-20 from the rubric does not remove NGT. C-08
      still requires per-surprise newcomer accessibility enforcement.
    Introduced in: V-03(R6) — first variation to install NGT as a named discrete
      per-surprise C-08 gate. V-03(R6) predates C-18 as a rubric criterion (C-18
      introduced at the R5/R6 boundary). NGT's criterion-enforcement motivation
      predates the gating requirement.

  For each surprise: new-hire comprehension without project context. If fails: rewrite.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B enforces C-14 per surprise. Independent of C-18.
    Structural removal test: removing C-20 does not remove Check B — C-14 still
      requires per-surprise portability enforcement.
    Introduced in: V-05(R4) — first variation to install Check B as a named per-surprise
      portability gate, predating C-18 as a rubric criterion by two rounds.

  For each surprise: extract standalone. Derive (1) finding, (2) unexpectedness,
  (3) consequence. If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT enforces C-16 per surprise. Independent of C-18.
    Structural removal test: removing C-20 does not remove CAT — C-16 still requires
      per-surprise coupled enforcement.
    Introduced in: V-05(R5) — first variation to install CAT as a named per-surprise
      C-16 gate, predating C-18 as a rubric criterion by one round.

  For each surprise: (1) no prohibited constructs; (2) stranger-accessible. Both required.

== STEP 6–9 — AUDIT + WRITE ====================================================

  Step 6 — Label parity audit: all Name fields specific and descriptive. No generic labels.
  Step 7 — Field completion scan: all six fields populated, no N/A or placeholder.
  Step 8 — Patterns: if shared root cause across surprises, write Patterns section.
           Word count: full echo ≤800 words. Cut if exceeded.
  Step 9 — Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: Archetype Classification + Gate Provenance (compound maximum)

**Axis:** Both C-21 and C-23 targeted by explicit structural requirements — full archetype
taxonomy with internal consistency check in manifest pair inspections AND full round
provenance in every gate rationale. C-22 PASS is inherited from V-04(R8) baseline.

**Hypothesis:** V-04 is the compound maximum for v8: the first variation in the topic-echo
lineage designed to satisfy C-21, C-22, and C-23 simultaneously as structural requirements.
C-23 PASS requires the manifest template to: (1) define the finite archetype taxonomy before
pair inspections begin, (2) require archetype selection as a field preceding mechanism fill-in,
and (3) include a consistency check instruction. V-04 inherits C-22 from V-04(R8)'s gate
rationale provenance pattern ("Introduced in: V-XX(RN)"). The three new criteria are
structurally independent: archetype classification (C-23) operates in the manifest;
causal depth (C-21) is a quality dimension within mechanism statements; gate provenance
(C-22) operates in the gate rationale sections. All three can pass simultaneously without
structural tension.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== SCHEMA CONTRACT ==============================================================

Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering]
  missed this:
  Design impact:                [one sentence minimum]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Passive-team test per surprise. "Why passive observation missed this" names the mechanism.

Rule 2 — Claim-only voice:
  Prohibited: may suggest / appears to indicate / seems like / could mean /
              it is possible that / might be / could indicate / it seems

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Complete all pair inspections with archetype classification
and mechanism statements. Declare before candidate selection begins.

Active enforcement mechanisms (11 total):
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs enumerated)
  5.  Counterfactual gate — Rule 1
  6.  NGT — Newcomer Gate Test (C-08 gate)
  7.  Check B — Portability Test (C-14 gate)
  8.  CAT — Coupled Authority Test (C-16 gate)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

Pair inspection — ARCHETYPE CLASSIFICATION REQUIRED:

  For each pair:
    Step 1: Select archetype from finite taxonomy (must precede mechanism statement)
    Step 2: State mechanism in terms consistent with the selected archetype

  Taxonomy (finite — exactly one per pair):
    PREREQUISITE  — A's output is B's required input. Breaking A breaks B in any
                    compound configuration. Ordering constraint is non-negotiable.
    ESTABLISHES   — A creates a property that B operates on. Directional, not input-
                    dependent. Removing A removes the property B enforces.
    AMPLIFIES     — A increases precision or strength of B's per-surprise enforcement.
                    B operates without A but with reduced effectiveness.
    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    No mutual dependency; neither is prerequisite for the other.

  Consistency check: mechanism must be verifiable against selected archetype. A PREREQUISITE
  archetype whose mechanism describes independent operation fails its own classification.

  Required pairs:

  Schema manifest + Stranger-reader commitment:
    Archetype: [select]
    Mechanism: [fill in — consistent with archetype]

  Rule 1 + Rule 2:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + NGT:
    Archetype: [select]
    Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Archetype: [select]
    Mechanism: [fill in]

  NGT + Check B:
    Archetype: PREREQUISITE
    Mechanism: "NGT is a PREREQUISITE for Check B: NGT's newcomer-comprehension gate
    output is Check B's required input; a surprise that fails NGT (stranger cannot
    understand it without project context) cannot pass Check B's three-component
    standalone extraction test. This constraint holds in any novel compound configuration:
    newcomer-comprehension verification must precede portability testing."

  Check B + CAT:
    Archetype: ESTABLISHES
    Mechanism: "Check B ESTABLISHES the structural portability property that CAT enforces:
    Check B verifies that a surprise is derivable standalone (finding + unexpectedness +
    consequence); CAT enforces that the verified-portable unit is authoritative in voice.
    Check B's property (structural portability) is the substrate for CAT's coupling test;
    removing Check B removes the property CAT verifies."

  CAT + Rule 2:
    Archetype: [select]
    Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Archetype: [select]
    Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + Check B:
    Archetype: [select]
    Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Archetype: [select]
    Mechanism: [fill in]

  Declaration: "All 11 active mechanisms assessed with archetype classification and mechanism
  statements consistent with selected archetypes. All mechanisms reinforce each other toward
  the single stranger-reader target. No conflicts found. Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**. Read all signals. List candidates not expected before
  gathering signals. Apply Rule 1 + C-01 filter. Minimum 3 required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six schema fields per candidate. Check A: 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT enforces C-08 per surprise. C-08's per-surprise accessibility
      requirement exists independently of how enforcement is documented; NGT is the
      designated enforcement mechanism for that requirement.
    Structural removal test: removing C-20 from the rubric does not remove NGT. C-08
      still requires per-surprise newcomer accessibility enforcement.
    Introduced in: V-03(R6) — first variation in this skill's lineage to install NGT
      as a named discrete per-surprise C-08 gate. V-03(R6) predates C-18 as a rubric
      criterion (C-18 introduced at the R5/R6 boundary). The timeline confirms that
      NGT's criterion-enforcement motivation predates any gating requirement.

  For each surprise: new-hire comprehension without project context. If fails: rewrite.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B enforces C-14 per surprise. C-14 requires each surprise
      to stand alone as a self-contained institutional claim; Check B is the primary
      mechanism for that requirement.
    Structural removal test: removing C-20 does not remove Check B — C-14 still requires
      per-surprise portability enforcement.
    Introduced in: V-05(R4) — first variation to install Check B as a named per-surprise
      portability gate. V-05(R4) predates C-18 as a rubric criterion by two rounds;
      Check B's portability enforcement motivation is documented prior to any gating
      requirement in the rubric.

  For each surprise: extract standalone. Derive (1) finding, (2) unexpectedness,
  (3) consequence. If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT enforces C-16 per surprise. C-16 requires each surprise to
      pass both the stranger-reader test and the no-hedging test as a coupled unit;
      CAT is the primary per-surprise enforcement mechanism for that requirement.
    Structural removal test: removing C-20 does not remove CAT — C-16 still requires
      per-surprise coupled enforcement.
    Introduced in: V-05(R5) — first variation to install CAT as a named per-surprise
      C-16 gate. V-05(R5) predates C-18 as a rubric criterion by one round; CAT's
      coupling enforcement motivation is documented prior to the gating requirement.

  For each surprise: (1) no prohibited constructs; (2) stranger-accessible. Both required.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Name field across all surprises: every label specific and descriptive. No generic labels.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  All six fields populated across all surprises. No N/A, blank, or placeholder.

== STEP 8 — PATTERNS + FINAL CHECK =============================================

  Patterns: if any two surprises share a root cause, write Patterns section. Else omit.
  Word count: full echo ≤800 words. Cut if exceeded.

== STEP 9 — WRITE ARTIFACT =====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: Archetype Distribution Audit (C-23 macro-structure extension)

**Axis:** Extends V-04 with a post-inspection archetype distribution summary — after all
pair inspections, tally the archetype selections and interpret the manifest's macro
structural shape. Tests whether aggregate archetype distribution reveals enforcement
pipeline properties that are invisible at the pair level. All four of C-19, C-20, C-21,
C-22, C-23 pass; the distribution audit is a potential new quality signal.

**Hypothesis:** Archetype classification at the pair level (C-23) is necessary but not
sufficient to reveal macro-properties of the enforcement pipeline. A manifest where all
pairs are PREREQUISITE indicates a strictly ordered pipeline — any mechanism removal breaks
all downstream mechanisms. A manifest mixing PREREQUISITE and PARALLEL archetypes indicates
a mechanism set with both ordered dependencies and independent enforcement paths. These
structural properties are only visible after all pair inspections are complete and the
archetype distribution is tallied. V-05 makes the distribution explicit as a required
post-inspection step, before the declaration. If this macro-structural characterization
consistently surfaces a new quality dimension, it is a candidate for a new unproven
criterion in v9.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== SCHEMA CONTRACT ==============================================================

Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering]
  missed this:
  Design impact:                [one sentence minimum]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Passive-team test per surprise. "Why passive observation missed this" names the mechanism.

Rule 2 — Claim-only voice:
  Prohibited: may suggest / appears to indicate / seems like / could mean /
              it is possible that / might be / could indicate / it seems

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Complete all pair inspections with archetype classification,
compile distribution summary, and declare before candidate selection begins.

Active enforcement mechanisms (11 total):
  1.  Schema manifest (pre-write field declaration)
  2.  Stranger-reader commitment
  3.  Word discipline — Check A (120-word per-item cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs enumerated)
  5.  Counterfactual gate — Rule 1
  6.  NGT — Newcomer Gate Test (C-08 gate)
  7.  Check B — Portability Test (C-14 gate)
  8.  CAT — Coupled Authority Test (C-16 gate)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

Pair inspection — ARCHETYPE CLASSIFICATION REQUIRED:

  For each pair:
    Step 1: Select archetype from finite taxonomy (must precede mechanism statement)
    Step 2: State mechanism in terms consistent with selected archetype

  Taxonomy (finite — exactly one per pair):
    PREREQUISITE  — A's output is B's required input. Strict ordering: breaking A breaks B
                    in any compound configuration.
    ESTABLISHES   — A creates a property that B operates on. Directional, not input-
                    dependent: removing A removes the property B enforces.
    AMPLIFIES     — A increases precision or strength of B's per-surprise enforcement.
                    B operates without A but with reduced effectiveness.
    PARALLEL      — A and B independently enforce the same sub-property. No mutual
                    dependency; both can satisfy the criterion alone.

  Consistency check: mechanism must be verifiable against selected archetype. A PREREQUISITE
  archetype describing independent parallel operation fails its own classification.

  Required pairs:

  Schema manifest + Stranger-reader commitment:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + Rule 2:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + NGT:
    Archetype: [select]
    Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Archetype: [select]
    Mechanism: [fill in]

  NGT + Check B:
    Archetype: PREREQUISITE
    Mechanism: "NGT is a PREREQUISITE for Check B: NGT's newcomer-comprehension output
    is Check B's required input; a surprise failing NGT cannot pass Check B's three-
    component standalone extraction test."

  Check B + CAT:
    Archetype: ESTABLISHES
    Mechanism: "Check B ESTABLISHES the portability property CAT enforces: structural
    portability (Check B's output) is the substrate for CAT's coupling test; removing
    Check B removes the property CAT verifies."

  CAT + Rule 2:
    Archetype: [select]
    Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Archetype: [select]
    Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + Check B:
    Archetype: [select]
    Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Archetype: [select]
    Mechanism: [fill in]

  Archetype distribution summary (complete after all pair inspections):

    Tally archetype selections across all 11 pairs:
      PREREQUISITE: [count] pairs
      ESTABLISHES:  [count] pairs
      AMPLIFIES:    [count] pairs
      PARALLEL:     [count] pairs

    Interpret distribution:
      All-PREREQUISITE → strictly ordered enforcement pipeline; any mechanism removal
        propagates downstream breakage
      PREREQUISITE + PARALLEL mix → ordered core with independent enforcement paths;
        the parallel mechanisms could be removed without breaking ordered mechanisms
      ESTABLISHES majority → property-creation dominant; the manifest is a chain of
        A-creates-property-B-enforces relationships
      Any AMPLIFIES → mechanisms with strengthening dependencies; the AMPLIFIES
        mechanisms add quality above the enforcement floor

    Write one sentence characterizing this manifest's structural shape:
      [e.g., "This manifest is PREREQUISITE-dominant ([N]/11 pairs), indicating a
      strictly ordered enforcement pipeline from schema declaration through authority
      coupling; the [M] ESTABLISHES relationships reflect property-creation stages
      where an upstream mechanism's output becomes the substrate for the next."]

  Declaration: "All 11 active mechanisms assessed with archetype classification,
  mechanism statements, and distribution summary. [Distribution characterization sentence].
  All mechanisms reinforce each other toward the stranger-reader target. No conflicts found.
  Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**. Read all signals. List candidates not expected before
  gathering signals. Apply Rule 1 + C-01 filter. Minimum 3 required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six schema fields per candidate. Check A: 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT enforces C-08 per surprise. This motivation is independent
      of rubric gating requirements; C-08's demand exists regardless of documentation.
    Structural removal test: removing C-20 does not remove NGT — C-08 still requires
      per-surprise newcomer accessibility enforcement.
    Introduced in: V-03(R6) — first variation to install NGT as a named discrete
      per-surprise C-08 gate, predating C-18 as a rubric criterion (C-18 introduced
      at the R5/R6 boundary). Criterion-enforcement motivation predates gating requirement.

  For each surprise: new-hire comprehension without project context. If fails: rewrite.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B enforces C-14 per surprise. Independent of C-18.
    Structural removal test: removing C-20 does not remove Check B — C-14 still requires
      per-surprise portability enforcement.
    Introduced in: V-05(R4) — first variation to install Check B as a named per-surprise
      portability gate, predating C-18 as a rubric criterion by two rounds. Check B's
      portability enforcement motivation is documented prior to any gating requirement.

  For each surprise: extract standalone. Derive (1) finding, (2) unexpectedness,
  (3) consequence. If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT enforces C-16 per surprise. Independent of C-18.
    Structural removal test: removing C-20 does not remove CAT — C-16 still requires
      per-surprise coupled enforcement.
    Introduced in: V-05(R5) — first variation to install CAT as a named per-surprise
      C-16 gate, predating C-18 as a rubric criterion by one round. CAT's coupling
      enforcement motivation is documented prior to the gating requirement.

  For each surprise: (1) no prohibited constructs; (2) stranger-accessible. Both required.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Name field across all surprises: every label specific and descriptive. No generic labels.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  All six fields populated across all surprises. No N/A, blank, or placeholder.

== STEP 8 — PATTERNS + FINAL CHECK =============================================

  Patterns: if any two surprises share a root cause, write Patterns section. Else omit.
  Word count: full echo ≤800 words. Cut if exceeded.

== STEP 9 — WRITE ARTIFACT =====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## Scoring Notes

**C-21 status after R9:** Demonstrated in R8 (V-01, V-04, V-05) and confirmed in R9
(V-01, V-02, V-04, V-05). Criterion is proven across two rounds. Promotion to 2 pts
(proven) candidate for v9 rubric.

**C-23 status after R9:** Demonstrated in R8 (V-01) and confirmed in R9 (V-01, V-04,
V-05). Criterion is proven across two rounds. Promotion to 2 pts (proven) candidate
for v9 rubric.

**C-23 FAIL boundary confirmed:** V-02 (causal direction without archetype field) and
V-03 (achievement-only manifest) each provide a distinct C-23 FAIL case, reinforcing
the boundary established in R8.

**New potential criterion from V-05:** Archetype distribution summary — if the
distribution characterization in V-05 consistently produces a macro-structural insight
not derivable from pair-level inspections alone, this is a candidate for C-24 (unproven,
1 pt) in v9: "Composability manifest archetype distribution characterization."

**Structural chain:** The precision dimension of the composability manifest is now
complete across four quality levels:
- **C-19**: pairs inspected, mutual reinforcement declared (pre-write commitment)
- **C-21**: each pair states directional causal mechanism (explanatory depth)
- **C-23**: each mechanism classified by finite archetype (predictive constraint class)
- **C-24 (candidate)**: archetype distribution characterized (macro pipeline structure)
