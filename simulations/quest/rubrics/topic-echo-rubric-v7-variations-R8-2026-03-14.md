
# Variations: `topic:echo` — Round 8

**Rubric:** v7 (max 100) | **Date:** 2026-03-14

---

## Design Context

R7 differentiating evidence: V-04 scored 100/100 against v7 and demonstrated both new criteria
informally — V-04's composability manifest stated causal direction per pair ("NGT prerequisite
for Check B," "structural portability prerequisite for coupled authority") and V-04's gate
rationale named round provenance ("Check B: introduced in V-05(R4) as the primary mechanism").
These behaviors emerged from the V-05(R6) baseline design, not from structural requirements in
the prompt. R8 makes them structural requirements and tests failure cases.

Two new aspirational criteria added in v7:

- **C-21** — Composability manifest causal depth (1 pt, unproven): each pair inspection in the
  manifest articulates the directional causal mechanism of reinforcement — not just "A and B
  reinforce" but "A is a prerequisite for B" or "A establishes the property that B enforces."
- **C-22** — Gate provenance traceability (1 pt, unproven): for each gate satisfying C-20, the
  gate rationale names the specific variation and round of introduction — e.g., "introduced in
  V-05(R4)" — making the motivation claim verifiable from history rather than asserted.

**R7 V-04 against v8 scoring (inheriting 100/100):** V-04(R7) demonstrates C-21 behavior
(causal direction present in pair inspections) and C-22 behavior (round provenance named in
gate rationale). It was not designed to satisfy these criteria explicitly. R8 needs five
variations that isolate and combine these structural requirements to confirm them as proven.

**Predicted score map:**

| Variant | C-19 | C-20 | C-21 | C-22 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | FAIL | 100       |
| V-02    | FAIL | PASS | N/A  | PASS | 100       |
| V-03    | PASS | PASS | FAIL | PASS | 100       |
| V-04    | PASS | PASS | PASS | PASS | 100       |
| V-05    | PASS | PASS | PASS | FAIL | 100       |

All five score 100: the R7 baselines already exceed the 18-pt aspirational budget cap before
C-21 and C-22 are considered. Architectural differentiation lies in which new criteria each
variation satisfies.

**Axis selection:**

Single-axis (V-01, V-02, V-03):
- V-01 — C-21 axis: explicit causal direction template in manifest; gate rationale without provenance
- V-02 — C-22 axis: gate provenance field isolated from manifest (no manifest, C-19 FAIL)
- V-03 — C-21 failure: conclusion-only manifest (verdict without mechanism); gate provenance present

Combined (V-04, V-05):
- V-04 — compound maximum: causal direction template + full provenance (C-21 + C-22 both pass)
- V-05 — C-22 boundary: causal direction template + round-only provenance (C-22 failure case)

---

## V-01 — Single-axis: Causal Direction Template (C-21 structural enforcement)

**Axis:** Composability manifest pair inspection format — each pair inspection requires explicit
causal archetype selection and mechanism fill-in; conclusion-only assessments fail the template.

**Hypothesis:** Enforcing causal direction as a structural requirement in the manifest (rather
than leaving it as an incidental output of careful reasoning) earns C-21 PASS. Gate rationale
carries criterion attribution and structural removal test (C-20 PASS) but no round provenance,
isolating C-21 as the single new axis. C-22 FAIL because no provenance is named.

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
  Each surprise must fail: "A passive, attentive team tracking this feature would have found
  this through normal observation." Items that survive passive observation are not echoes.
  The "Why passive observation missed this" field names the specific mechanism.

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

Pair inspection — CAUSAL DIRECTION REQUIRED for each pair:

  For each pair, select one causal archetype and fill in the mechanism:

  Causal archetypes:
    PREREQUISITE   — "A is a prerequisite for B": A's output is B's required input;
                     B cannot run effectively without A passing first
    ESTABLISHES    — "A establishes the property that B enforces": A creates the
                     condition; B verifies that condition holds per surprise
    AMPLIFIES      — "A amplifies B's enforcement per surprise": A strengthens B's
                     check in each application; B works better because A ran first
    PARALLEL       — "A and B target the same sub-property from complementary angles":
                     neither is a prerequisite; both independently enforce the same
                     property with no mutual degradation

  Required pairs (inspect all; add any pair where conflict is possible):

  Schema manifest + Stranger-reader commitment:
    Archetype: [select one]
    Mechanism: [fill in — e.g., "Schema manifest ESTABLISHES the property that
                Stranger-reader commitment enforces: each declared field must be
                comprehensible without project context; Stranger-reader commitment
                verifies that property holds per surprise"]

  Rule 1 + Rule 2:
    Archetype: [select one]
    Mechanism: [fill in]

  Rule 1 (counterfactual gate) + NGT:
    Archetype: [select one]
    Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Archetype: [select one]
    Mechanism: [fill in]

  NGT + Check B:
    Archetype: [select one]
    Mechanism: [fill in — e.g., "NGT is a PREREQUISITE for Check B: NGT's newcomer-
                comprehension gate is a required input for Check B's portability test;
                a surprise that fails NGT (stranger cannot understand it) cannot pass
                Check B's stranger-reader extraction test"]

  Check B + CAT:
    Archetype: [select one]
    Mechanism: [fill in — e.g., "Check B ESTABLISHES the property that CAT enforces:
                Check B's structural portability verification is a prerequisite for
                CAT's coupled authority test — CAT tests portability with authoritative
                voice; the portability half is satisfied by Check B passing first"]

  CAT + Rule 2:
    Archetype: [select one]
    Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Archetype: [select one]
    Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Archetype: [select one]
    Mechanism: [fill in]

  Rule 1 + Check B:
    Archetype: [select one]
    Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Archetype: [select one]
    Mechanism: [fill in]

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected with causal direction
  confirmed. All mechanisms reinforce each other toward the single stranger-reader target.
  No mechanism pair found to be in conflict. Writing may begin."

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
    Criterion enforced: C-08 (per-surprise newcomer accessibility).
    Primary motivation: NGT exists to enforce C-08 per surprise. If C-20 were removed
    from rubric evaluation, NGT would still exist: C-08 requires that each surprise be
    independently accessible to a newcomer, and NGT is the primary enforcement mechanism
    for that requirement.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior exposure to this project understand this finding without
    consulting source signals or the rest of the echo?
    If no: rewrite before continuing to Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability).
    Primary motivation: Check B exists to enforce C-14 per surprise. If C-20 were removed
    from rubric evaluation, Check B would still exist: C-14 requires that each surprise
    stand alone as a self-contained institutional claim, and Check B is the primary
    enforcement mechanism for that requirement.

  For each surprise individually:
    Extract this surprise as a standalone block.
    A reader who has never seen this project reads only this block.
    Can they derive: (1) the finding, (2) why it was unexpected, (3) the design consequence?
    If any component is missing or requires external context: rewrite before continuing to CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling).
    Primary motivation: CAT exists to enforce C-16 per surprise. If C-20 were removed from
    rubric evaluation, CAT would still exist: C-16 requires that each surprise individually
    pass both the stranger-reader test and the no-hedging test as a coupled unit, and CAT
    is the primary enforcement mechanism for that requirement.

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

## V-02 — Single-axis: Gate Provenance Annotation (C-22 structural enforcement)

**Axis:** Gate rationale format — each gate rationale carries an explicit provenance field
naming the specific variation and round of introduction. No composability manifest present
(C-19 FAIL), isolating C-22 as the single new axis.

**Hypothesis:** C-22 can be earned independently of C-21 — the provenance field in each gate's
design rationale is an orthogonal documentation requirement that does not require a manifest.
C-19 FAIL + C-22 PASS confirms that C-22, like C-20, does not imply C-19. The provenance
field converts the structural removal test from an assertion to a historically verifiable fact
(e.g., "introduced in V-05(R4)" predates C-18 as a rubric criterion, confirming criterion-
enforcement motivation by timeline).

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 9.

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
  Each surprise must fail: "A passive, attentive team would have found this through normal
  observation." The "Why passive observation missed this" field names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited: may suggest / appears to indicate / seems like / could mean /
              it is possible that / might be / could indicate / it seems
  Every schema field is a direct statement.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic.
  List every candidate finding not expected before gathering signals.
  Apply Rule 1 (counterfactual filter) and C-01 filter (no expected findings dressed as
  surprises). Minimum 3 candidates required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six schema fields per candidate.
  Check A — per-item 120-word cap. Extract claim if exceeded.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — runs per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT exists to enforce C-08 per surprise. This motivation is
      independent of rubric gating requirements: C-08 requires newcomer-accessible
      surprises regardless of how enforcement is documented. Removing C-20 from
      evaluation does not remove the motivation for NGT.
    Structural removal test: if C-20 were removed from the rubric, NGT still exists
      because C-08 requires per-surprise accessibility enforcement and NGT is the
      primary mechanism for it.
    Introduced in: V-03(R6) — first variation in this skill's lineage to install a
      named discrete C-08 gate as a per-surprise step. V-03(R6) added NGT to the
      V-05(R5) baseline, completing the 3/3 gate set for C-18.

  For each surprise individually:
    Can a new-hire with no prior project exposure understand this without consulting
    source signals? If no: rewrite before continuing.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise. This motivation
      is independent of rubric gating requirements: C-14 requires each surprise to
      stand alone as a self-contained institutional claim.
    Structural removal test: if C-20 were removed from the rubric, Check B still
      exists because C-14 requires per-surprise portability enforcement and Check B
      is the primary mechanism for it.
    Introduced in: V-05(R4) — first variation to install a named per-surprise
      portability test as a discrete gate step. V-05(R4) was the first variation to
      add Check B ("a reader who has never seen this project reads only this section")
      as an explicitly named per-surprise step, predating C-18 as a rubric criterion.

  For each surprise individually:
    Extract as standalone block. Can reader derive: (1) finding, (2) why unexpected,
    (3) design consequence? If any missing or context-dependent: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise. This motivation is
      independent of rubric gating requirements: C-16 requires each surprise to pass
      both stranger-reader and no-hedging tests as a coupled unit.
    Structural removal test: if C-20 were removed from the rubric, CAT still exists
      because C-16 requires per-surprise coupled enforcement and CAT is the primary
      mechanism for it.
    Introduced in: V-05(R5) — first variation to install a named coupled authority
      test as a discrete per-surprise gate. V-05(R5) added CAT to the V-05(R4)
      baseline (which had Check B but no coupling gate), predating C-18 as a rubric
      criterion.

  For each surprise individually:
    (1) No prohibited constructs from Rule 2.
    (2) Accessible to a stranger without project context.
    Both required. If either fails: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Name field across all surprises: every label specific and descriptive. No generic labels.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  All six fields populated across all surprises. No N/A, blank, or placeholder.

== STEP 8 — PATTERNS + FINAL CHECK =============================================

  Patterns: if any two surprises share a root cause, write Patterns section. Else omit.
  Word count: full echo ≤800 words total. Cut if exceeded.

== STEP 9 — WRITE ARTIFACT =====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: Conclusion-Only Manifest (C-21 failure case)

**Axis:** Composability manifest pair inspection depth — each pair inspection produces a
verdict (reinforcing / non-conflicting) and a one-sentence rationale about the outcome, but
does not state the directional causal mechanism. The manifest template does not include a
causal archetype field.

**Hypothesis:** A composability manifest that inspects each pair and records relationship
verdicts satisfies C-19 (pair inspection occurs, mutual reinforcement declared pre-write)
but fails C-21 (causal direction not stated, inspections are conclusion-assertions not
causal mechanisms). Structurally parallel to the V-03 R7 finding: enumeration satisfies
the naming requirement but not the inspection requirement; here, verdict-inspection satisfies
C-19's inspection requirement but not C-21's causal depth requirement. Gate rationale carries
full provenance (inherited from V-04(R7) lineage), so C-22 PASS.

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
  Design impact:                [one sentence minimum — how this changes design direction]
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
  3.  Word discipline — Check A (120-word cap)
  4.  Anti-hedging — Rule 2 (8 prohibited constructs)
  5.  Counterfactual gate — Rule 1
  6.  NGT — Newcomer Gate Test (C-08 gate)
  7.  Check B — Portability Test (C-14 gate)
  8.  CAT — Coupled Authority Test (C-16 gate)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

Pair inspection — for each pair, assess and record:

  Verdict options: reinforcing | non-conflicting | conflicting (resolve before writing)
  For each verdict, write one sentence explaining the relationship outcome.

  Schema manifest + Stranger-reader commitment:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence — what relationship exists between these mechanisms]

  Rule 1 + Rule 2:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Rule 1 + NGT:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Word discipline + Anti-hedging:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  NGT + Check B:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence — e.g., "NGT and Check B both test stranger-reader
                comprehension at different levels and reinforce each other"]

  Check B + CAT:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence — e.g., "Check B and CAT both require stranger-accessible
                output and reinforce toward the same portability target"]

  CAT + Rule 2:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Schema manifest + Label parity audit:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Label parity audit + Field completion scan:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Rule 1 + Check B:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Stranger-reader commitment + CAT:
    Verdict: [reinforcing / non-conflicting / conflicting]
    Rationale: [one sentence]

  Declaration: "All 11 active mechanisms inspected. [N] pairs reinforcing, [M] non-conflicting,
  0 conflicting. All mechanisms reinforce each other toward the single stranger-reader target.
  Writing may begin."

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**. Read all signals. List candidates not expected before
  gathering signals. Apply Rule 1 + C-01 filter. Minimum 3 required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six schema fields per candidate. Check A: 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT enforces C-08 per surprise. Independent of C-18: removing
      gating requirements from evaluation does not change C-08's per-surprise accessibility
      requirement. NGT is the primary mechanism for that requirement.
    Structural removal test: remove C-20 from the rubric. NGT still exists because C-08
      requires per-surprise newcomer accessibility enforcement.
    Introduced in: V-03(R6) — first variation in this skill's lineage to install NGT as a
      named per-surprise C-08 gate, predating C-18 as a rubric criterion (introduced v6).

  For each surprise: new-hire comprehension without project context. If fails: rewrite.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise portability)
    Primary motivation: Check B enforces C-14 per surprise. Independent of C-18.
    Structural removal test: remove C-20 from the rubric. Check B still exists because
      C-14 requires per-surprise portability enforcement.
    Introduced in: V-05(R4) — first variation to install Check B as a named per-surprise
      portability gate, predating C-18 as a rubric criterion.

  For each surprise: extract standalone. Derive finding, unexpectedness, consequence.
  If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT enforces C-16 per surprise. Independent of C-18.
    Structural removal test: remove C-20 from the rubric. CAT still exists because C-16
      requires per-surprise coupled enforcement.
    Introduced in: V-05(R5) — first variation to install CAT as a named per-surprise
      C-16 gate, predating C-18 as a rubric criterion.

  For each surprise: (1) no prohibited constructs; (2) stranger-accessible. Both required.

== STEP 6–9 — AUDIT + WRITE ====================================================

  Step 6 — Label parity audit: all Name fields specific and descriptive.
  Step 7 — Field completion scan: all six fields populated, no N/A.
  Step 8 — Patterns + word count: Patterns if shared root cause; full echo ≤800 words.
  Step 9 — Write to simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: Causal Direction Template + Gate Provenance (compound maximum)

**Axis:** Both C-21 and C-22 targeted by explicit structural requirements — causal direction
template in manifest pair inspections AND provenance field in every gate rationale.

**Hypothesis:** V-04 is the compound maximum: the first variation in the topic-echo lineage
designed to satisfy C-21 and C-22 simultaneously as structural requirements (not incidental
behaviors). C-21 PASS + C-22 PASS. This mirrors V-04(R7)'s role in the prior round: the
compound maximum variation that earns both new unproven criteria.

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

REQUIRED BEFORE Step 1. Complete all pair inspections with causal direction and declare
before any candidate selection begins.

Active enforcement mechanisms (11 total):
  1.  Schema manifest
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

Pair inspection — CAUSAL DIRECTION REQUIRED:

  For each pair: select archetype, state mechanism.

  Archetypes:
    PREREQUISITE — A's output is B's required input; B cannot run without A passing
    ESTABLISHES  — A creates the condition; B verifies it per surprise
    AMPLIFIES    — A strengthens B's enforcement in each application
    PARALLEL     — both target the same sub-property independently, no mutual degradation

  Schema manifest + Stranger-reader commitment:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + Rule 2:
    Archetype: [select]
    Mechanism: [fill in]

  Rule 1 + NGT:
    Archetype: [select]
    Mechanism: [fill in]

  Word discipline + Anti-hedging:
    Archetype: [select]
    Mechanism: [fill in]

  NGT + Check B:
    Archetype: PREREQUISITE
    Mechanism: "NGT is a prerequisite for Check B: NGT's newcomer-comprehension gate
    produces a verified stranger-readable surprise; Check B's portability test requires
    that input — a surprise that fails NGT (stranger cannot understand it without context)
    cannot pass Check B's three-component standalone extraction test."

  Check B + CAT:
    Archetype: ESTABLISHES
    Mechanism: "Check B establishes the structural portability property that CAT enforces:
    Check B verifies that a surprise can be extracted and understood in full; CAT then
    enforces that the extracted unit is stated with authoritative claim-voice. Portability
    (Check B) is a prerequisite sub-property of coupled-authority portability (CAT)."

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

  Declaration: "All 11 active mechanisms assessed with causal direction confirmed per pair.
  All mechanisms reinforce each other toward the single stranger-reader target. No conflicts
  found. Writing may begin."

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**. Read all signals.
  List candidates not expected before gathering signals. Apply Rule 1 + C-01 filter.
  Minimum 3 candidates required.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six fields per candidate. Check A: 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT exists to enforce C-08 per surprise. Criterion-enforcement
      is the primary motivation: C-08 requires newcomer accessibility for every surprise
      individually, and NGT is the designated per-surprise gate for it.
    Structural removal test: removing C-20 from the rubric does not remove NGT —
      C-08 still requires per-surprise newcomer accessibility enforcement.
    Introduced in: V-03(R6) — first variation to add NGT as a named discrete C-08
      per-surprise gate. V-03(R6) was scored in Round 6, predating C-18 as a rubric
      criterion (C-18 introduced in rubric v6 as a new unproven criterion at R5/R6
      boundary). NGT's criterion-enforcement motivation predates the gating requirement.

  For each surprise: new-hire comprehension without project context. If fails: rewrite.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise. The portability
      requirement — each surprise must stand alone as a self-contained institutional
      claim — motivated Check B's introduction.
    Structural removal test: removing C-20 from the rubric does not remove Check B —
      C-14 still requires per-surprise portability enforcement.
    Introduced in: V-05(R4) — first variation to install Check B as a named per-surprise
      portability gate. V-05(R4) predates C-18 as a rubric criterion by two rounds;
      Check B's portability enforcement motivation is documented prior to any gating
      requirement existing in the rubric.

  For each surprise: extract standalone. Derive finding, unexpectedness, consequence.
  If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise. The coupled requirement
      — each surprise must be both stranger-accessible and claim-voiced as a unit —
      motivated CAT's introduction.
    Structural removal test: removing C-20 from the rubric does not remove CAT —
      C-16 still requires per-surprise coupled enforcement.
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

## V-05 — Combined: Causal Direction + Round-Only Provenance (C-22 boundary case)

**Axis:** Gate provenance specificity — causal direction template present in manifest (C-21
axis from V-01 inherited), but gate provenance uses round-level reference only ("introduced
in Round 4") without naming the specific variation ("V-05(R4)").

**Hypothesis:** Round-level provenance fails C-22 because the reference does not enable an
evaluator to verify whether the gate predates or postdates C-18 as a rubric criterion.
"Introduced in Round 4" identifies a time range but not a specific variation or position
within that round's evaluation sequence. C-22's pass condition requires that the reference
be "accurate — verifiable against the variation's history — and must enable an evaluator to
determine whether the gate predates or postdates the C-18 rubric criterion." A round reference
is too coarse: multiple variations per round may have different gate architectures, and C-18
was introduced across the R5/R6 boundary, making R5/R6 round references ambiguous. C-21 PASS,
C-22 FAIL.

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
  Passive-team test. "Why passive observation missed this" names the mechanism.

Rule 2 — Claim-only voice:
  Prohibited: may suggest / appears to indicate / seems like / could mean /
              it is possible that / might be / could indicate / it seems

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1.

Active enforcement mechanisms (11 total):
  1–11: [Schema manifest, Stranger-reader commitment, Check A, Rule 2, Rule 1,
         NGT, Check B, CAT, Label parity audit, Field completion scan, Patterns]

Pair inspection — CAUSAL DIRECTION REQUIRED:

  Archetypes: PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL (select one per pair).
  For each pair: archetype + mechanism statement (specific enough to predict behavior
  in unseen configurations).

  NGT + Check B:
    Archetype: PREREQUISITE
    Mechanism: "NGT is a prerequisite for Check B: newcomer-comprehension gate output
    is Check B's required input; a surprise failing NGT cannot pass Check B's three-
    component extraction test."

  Check B + CAT:
    Archetype: ESTABLISHES
    Mechanism: "Check B establishes the portability property CAT enforces: structural
    portability (Check B) is a required sub-property of coupled-authority portability
    (CAT); the portability dimension of CAT's coupling test is satisfied by Check B."

  [remaining 9 pairs: select archetype + fill mechanism]

  Declaration: "All 11 active mechanisms assessed. Causal direction confirmed per pair.
  All mechanisms reinforce. No conflicts. Writing may begin."

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**. Read all signals. Apply Rule 1 + C-01 filter. Min 3.

== STEP 2 — SCHEMA POPULATION ==================================================

  Populate all six fields per candidate. Check A: 120-word per-item cap.

== STEP 3 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — per surprise — discrete step before Check B]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT enforces C-08 per surprise. Motivation is criterion-
      enforcement: C-08 requires newcomer accessibility per surprise; NGT is the
      primary mechanism for it.
    Structural removal test: removing C-20 from rubric does not remove NGT — C-08
      still requires per-surprise newcomer accessibility enforcement.
    Introduced in: Round 6 — added as the primary C-08 per-surprise gate when the
      variation lineage required named newcomer accessibility enforcement.

  For each surprise: new-hire comprehension without project context. If fails: rewrite.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise portability)
    Primary motivation: Check B enforces C-14 per surprise. Motivation is criterion-
      enforcement: C-14 requires per-surprise portability; Check B is the primary gate.
    Structural removal test: removing C-20 from rubric does not remove Check B —
      C-14 still requires per-surprise portability enforcement.
    Introduced in: Round 4 — added as the primary C-14 per-surprise portability gate
      when the variation lineage first required explicit portability enforcement per
      surprise.

  For each surprise: extract standalone. Derive finding, unexpectedness, consequence.
  If any missing: rewrite.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT enforces C-16 per surprise. Motivation is criterion-
      enforcement: C-16 requires coupled newcomer-accessibility and authoritative-voice
      enforcement per surprise; CAT is the primary gate for it.
    Structural removal test: removing C-20 from rubric does not remove CAT — C-16
      still requires per-surprise coupled enforcement.
    Introduced in: Round 5 — added as the primary C-16 per-surprise coupling gate
      when the variation lineage first required explicit claim-authority coupling
      enforcement per surprise.

  For each surprise: (1) no prohibited constructs; (2) stranger-accessible. Both required.

== STEP 6–9 — AUDIT + WRITE ====================================================

  Step 6 — Label parity audit: all Name fields specific and descriptive.
  Step 7 — Field completion scan: all six fields populated, no N/A.
  Step 8 — Patterns + word count: Patterns if shared root cause; ≤800 words total.
  Step 9 — Write to simulations/{topic}/{topic}-echo-{date}.md
```

---

## Structural Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-19 Pre-write composability declaration | PASS | FAIL | PASS | PASS | PASS |
| C-20 Gate design integrity | PASS | PASS | PASS | PASS | PASS |
| C-21 Composability manifest causal depth | **PASS** | N/A | **FAIL** | **PASS** | **PASS** |
| C-22 Gate provenance traceability | **FAIL** | **PASS** | **PASS** | **PASS** | **FAIL** |

**C-21 failure mode isolated in V-03:** Manifest present (C-19 PASS), pair inspection
occurs, mutual reinforcement declared — but inspection is verdict-assertion only ("NGT and
Check B reinforce each other") without causal direction. C-21 requires more than inspection
occurring; it requires the directional mechanism to be stated. The verdict-only template
satisfies C-19 and fails C-21 on the same pair-inspection content.

**C-22 failure mode isolated in V-05:** Gate rationale carries criterion attribution and
passes structural removal test (C-20 PASS) — but provenance is round-level only ("Round 4")
without variation specificity ("V-05(R4)"). C-22 cannot be satisfied by round-level reference
because the timeline verification requires knowing when within a round the gate was introduced,
not just which round. "Round 4" does not resolve which side of the C-18 introduction boundary
a gate falls on when C-18 was introduced across the R5/R6 evaluation period.

**C-22 orthogonality from C-21 isolated in V-02:** No manifest (C-19 FAIL → C-21 not
evaluable) but full round provenance in every gate rationale (C-22 PASS). Mirrors V-02(R7)'s
role confirming C-19/C-20 orthogonality: gate-level documentation requirements (C-20, C-22)
are independent from manifest-level documentation requirements (C-19, C-21).
