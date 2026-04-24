
# Variations: `topic:echo` — Round 10

**Rubric:** v9 (max 100) | **Date:** 2026-03-15

---

## Design Context

R9 demonstrated C-24 and C-25 from a single variation (V-01). Both remain unproven — proven
status requires demonstration across two or more rounds. R10 provides five variations designed
to isolate C-24 and C-25 as independently achievable quality dimensions, establish their
mutual failure boundary, and confirm the full chain in compound variations.

**Unproven criteria targeted in R10:**

- **C-24** — Archetype-mechanism consistency verification (1 pt): manifest template includes
  a discrete named verification step that instructs the author to actively confirm
  archetype-mechanism consistency before the pair inspection is finalized. A parenthetical
  reminder embedded in a field label does not satisfy this; a named step with an explicit
  instruction does.
- **C-25** — Archetype taxonomy illustration (1 pt): manifest template provides at least one
  concrete canonical pair example for each archetype used, giving authors a comparison
  baseline for classification decisions. Abstract taxonomy definition alone does not satisfy
  this; named pair instances with archetype label and one-sentence mechanism do.

**Predicted score map:**

| Variant | C-21 | C-22 | C-23 | C-24 | C-25 | Predicted |
|---------|------|------|------|------|------|-----------|
| V-01    | PASS | FAIL | PASS | PASS | FAIL | 100       |
| V-02    | PASS | FAIL | PASS | FAIL | PASS | 100       |
| V-03    | PASS | PASS | PASS | FAIL | FAIL | 100       |
| V-04    | PASS | PASS | PASS | PASS | PASS | 100       |
| V-05    | PASS | PASS | PASS | PASS | PASS | 100       |

**Scoring note:** C-22 FAIL (−2 pts from proven 20) in V-01/V-02 is offset by 3 unproven
points each (C-21+C-23+C-24 and C-21+C-23+C-25 respectively), reaching the 21-pt budget cap.
V-03 (C-22 PASS, proven=20) + 2 unproven (C-21+C-23) = 22 → capped 21 → 79+21=100. V-04/V-05
earn 4+ unproven pts against 21-pt cap → 100 regardless.

**Axis selection:**

Single-axis (V-01, V-02, V-03):
- V-01 — Phrasing register: formal/technical imperative language names the consistency check
  as "CONSISTENCY GATE" — a discrete named step with explicit instruction. Taxonomy defined
  abstractly only. C-24 PASS, C-25 FAIL. C-22 FAIL isolates C-24 as the single new axis.
- V-02 — Output format: pair inspection template embeds concrete EXAMPLE blocks inside the
  template structure. Consistency is noted as a parenthetical field annotation, not a named
  step. C-25 PASS, C-24 FAIL. C-22 FAIL isolates C-25 as the single new axis.
- V-03 — Role sequence: pair inspection uses three-field sequence (Archetype → Mechanism →
  Composability-claim). Archetype precedes mechanism (C-23 PASS), mechanism is directional
  (C-21 PASS), no verification step between fields (C-24 FAIL), no concrete examples
  (C-25 FAIL). C-22 PASS confirms C-24/C-25 failure is orthogonal to provenance.

Combined (V-04, V-05):
- V-04 — Phrasing register + output format: formal CONSISTENCY GATE + concrete canonical
  examples + gate provenance. Full manifest precision chain (C-21+C-22+C-23+C-24+C-25 PASS).
- V-05 — Lifecycle emphasis + inertia framing: V-04 baseline extended with post-inspection
  archetype distribution audit and opening inertia context. Potential C-26 signal: distribution
  audit surfaces macro-structural enforcement pipeline properties not visible per-pair.

---

## V-01 — Single-axis: Phrasing Register (formal CONSISTENCY GATE; no concrete examples)

**Axis:** Phrasing register — formal/technical imperative language. The composability manifest
names the consistency check as a discrete numbered step ("CONSISTENCY GATE") with an explicit
verification instruction. Taxonomy is defined abstractly (four archetypes, definitions only —
no concrete pair examples). Gate rationale carries criterion + primary motivation + structural
removal test (C-20 PASS) but no "Introduced in:" provenance field (C-22 FAIL). C-22 FAIL
isolates C-24 as the single differentiating unproven axis.

**Hypothesis:** C-24 requires a discrete named verification step in the manifest template;
abstract taxonomy definition plus a parenthetical reminder do not satisfy it. The formal
register produces a maximally explicit CONSISTENCY GATE that is identifiable as a template
action distinct from the archetype selection field and mechanism field. C-25 FAIL confirms
that concrete examples are not required for C-24 to pass — the verification step functions
on abstract definitions alone.

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

Pair inspection — ARCHETYPE CLASSIFICATION WITH CONSISTENCY GATE:

  For each pair, in this sequence:
    Step 1: Select archetype from the finite taxonomy below (must precede mechanism).
    Step 2: CONSISTENCY GATE — Before stating the mechanism, apply this check:
              "Does my intended mechanism statement satisfy the constraint class of the
               selected archetype?" If yes: proceed to Step 3. If no: return to Step 1
               with a corrected archetype or corrected mechanism framing.
    Step 3: State the mechanism in terms consistent with the verified archetype.

  Taxonomy (abstract definitions — select exactly one per pair):
    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. In any
                    novel compound configuration, inserting a mechanism between A and B
                    that transforms A's output into something B cannot consume breaks
                    the enforcement path. Mechanism framing must describe input-dependency.
    ESTABLISHES   — A creates a property that B operates on. Directional but not
                    feedback-dependent: B's behavior depends on A's property holding,
                    but A does not consume B's output. Removing A removes the property
                    B verifies. Mechanism framing must describe property creation and
                    one-way dependency.
    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    B operates without A but produces weaker enforcement. In compound
                    configurations, the amplification relationship holds independently of
                    other mechanisms in the chain. Mechanism framing must describe
                    effectiveness scaling.
    PARALLEL      — A and B independently enforce the same sub-property from distinct
                    paths. Each can satisfy the criterion alone. No mutual dependency;
                    neither is a prerequisite for the other. Mechanism framing must
                    describe independent path operation.

  Required pairs (inspect all; add any pair where conflict is possible):

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype: [PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL]
    Step 2 — CONSISTENCY GATE: [confirm mechanism framing will satisfy archetype above]
    Step 3 — Mechanism: [state mechanism consistent with verified archetype]

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 + NGT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  NGT + Check B:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Check B + CAT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  CAT + Rule 2:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 + Check B:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected. For each pair,
  CONSISTENCY GATE confirmed archetype-mechanism alignment before mechanism was finalized.
  All mechanisms reinforce each other toward the single stranger-reader target. No conflicts
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

## V-02 — Single-axis: Output Format (embedded EXAMPLE blocks; parenthetical consistency)

**Axis:** Output format — the composability manifest pair inspection template is restructured to
embed concrete EXAMPLE blocks directly in the template body, one per archetype used, immediately
following the blank pair entries. Consistency check is rendered as a parenthetical annotation
on the Archetype field label: "(mechanism below must be consistent with selected archetype)".
This is a field-level reminder, not a discrete named step. C-25 PASS (concrete examples
present), C-24 FAIL (no named gate — parenthetical implies consistency but does not instruct
the author to verify it as a discrete action). C-22 FAIL (no gate provenance) isolates C-25
as the single differentiating unproven axis.

**Hypothesis:** C-25 can be demonstrated independently of C-24: concrete canonical pair
examples embedded in the manifest template satisfy C-25's comparison-baseline requirement
without requiring a discrete verification step. C-24 requires a NAMED STEP that instructs
the author to perform a consistency check as an explicit action — a parenthetical annotation
on the archetype field label does not constitute a discrete step.

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

Pair inspection — ARCHETYPE CLASSIFICATION WITH CANONICAL EXAMPLES:

  Template (fill in for each required pair):

    Pair: [Mechanism A] + [Mechanism B]
    Archetype: [PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL]
               (mechanism below must be consistent with selected archetype)
    Mechanism: [directional causal statement of reinforcement]

  Taxonomy:
    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.

  Canonical examples (reference when classifying pairs):

    EXAMPLE — NGT + Check B:
      Archetype: PREREQUISITE
      Mechanism: "NGT's newcomer-comprehension output is Check B's required input. A surprise
      that fails NGT cannot pass Check B's three-component standalone extraction test. This
      input-dependency holds in any compound configuration: no mechanism inserted between NGT
      and Check B substitutes for newcomer-comprehension verification."

    EXAMPLE — Check B + CAT:
      Archetype: ESTABLISHES
      Mechanism: "Check B establishes the structural portability property that CAT enforces.
      Check B verifies that a surprise is fully derivable as a standalone unit (finding +
      unexpectedness + consequence); CAT then enforces that this verified-portable unit is
      stated with authoritative claim-voice. Removing Check B removes the substrate CAT
      operates on."

  Required pairs (use template above; compare against EXAMPLE blocks when classifying):

  Schema manifest + Stranger-reader commitment:
    Archetype: [select — compare against EXAMPLE taxonomy above if PREREQUISITE or ESTABLISHES]
    Mechanism: [fill in]

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
    Archetype: [see EXAMPLE above]
    Mechanism: [see EXAMPLE above — fill in using canonical as reference]

  Check B + CAT:
    Archetype: [see EXAMPLE above]
    Mechanism: [see EXAMPLE above — fill in using canonical as reference]

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

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using archetype
  classification with canonical examples as comparison baseline. All mechanisms reinforce
  each other toward the single stranger-reader target. No conflicts found. Writing may begin."

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
      independent of rubric gating requirements.
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
      C-14 still requires per-surprise portability enforcement.

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
      coupled unit; CAT is the designated per-surprise enforcement mechanism.
    Structural removal test: removing C-20 from the rubric does not remove CAT.
      C-16 still requires per-surprise coupled enforcement.

  For each surprise individually:
    (1) Is this surprise stated as a direct claim? (No prohibited constructs from Rule 2.)
    (2) Is this surprise accessible to a stranger without project context?
    Both must be YES. If either is NO: rewrite before continuing.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises in sequence.
  Failing labels: "Finding N", "Surprise A", any generic category header.
  Any generic or absent label: rename before continuing.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises in sequence:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  Every field must contain substantive content. No N/A, no blank, no placeholder text.
  Any gap: return to Step 2 for that surprise.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  If any two surprises share a root cause: write one Patterns section after all surprises.
  If no shared roots: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Total echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: Role Sequence (three-field pair format; gate provenance; no verification or examples)

**Axis:** Role sequence — the composability manifest pair inspection uses a three-field
sequential format: Archetype → Mechanism → Composability-claim. The sequence places archetype
selection before mechanism (C-23 PASS), mechanism is directional (C-21 PASS), and a
composability-claim field follows. However, there is no discrete verification step between
the archetype field and the mechanism field (C-24 FAIL), and the taxonomy is defined abstractly
without concrete pair examples (C-25 FAIL). Gate rationale includes "Introduced in: V-XX(RY)"
provenance for all three gates (C-22 PASS).

**Hypothesis:** Even with archetype preceding mechanism in the pair inspection sequence, the
absence of a discrete instruction to verify archetype-mechanism consistency means C-24 FAILs.
The field ordering does not substitute for a named verification action. C-24 FAIL with C-22
PASS and C-23 PASS establishes that the three-field sequence is structurally insufficient for
C-24: field order is not a verification gate.

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
  found this through normal observation." The "Why passive observation missed this" field
  names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited constructs:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Every schema field is a direct statement.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Complete all pair inspections and declare before any candidate
selection begins.

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

Pair inspection — three-field sequence (archetype → mechanism → composability-claim):

  For each pair:
    Archetype:            [select from: PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL]
    Mechanism:            [directional causal statement — not just "reinforce"; name how
                           A's output, property, or effect enables or amplifies B's function]
    Composability-claim:  [one sentence — why this pair reinforces without mutual degradation]

  Taxonomy (select exactly one per pair):
    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.

  Required pairs (inspect all; add any pair where conflict is possible):

  Schema manifest + Stranger-reader commitment:
    Archetype:
    Mechanism:
    Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Archetype:
    Mechanism:
    Composability-claim:

  Rule 1 + NGT:
    Archetype:
    Mechanism:
    Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Archetype:
    Mechanism:
    Composability-claim:

  NGT + Check B:
    Archetype:
    Mechanism:
    Composability-claim:

  Check B + CAT:
    Archetype:
    Mechanism:
    Composability-claim:

  CAT + Rule 2:
    Archetype:
    Mechanism:
    Composability-claim:

  Schema manifest + Label parity audit:
    Archetype:
    Mechanism:
    Composability-claim:

  Label parity audit + Field completion scan:
    Archetype:
    Mechanism:
    Composability-claim:

  Rule 1 + Check B:
    Archetype:
    Mechanism:
    Composability-claim:

  Stranger-reader commitment + CAT:
    Archetype:
    Mechanism:
    Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected with archetype
  classification and directional mechanism statements. All mechanisms reinforce each other
  toward the single stranger-reader target. No conflicts found. Writing may begin."

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
      per-surprise enforcement mechanism. This motivation is independent of rubric
      gating requirements.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.
      C-08 still requires per-surprise enforcement, and NGT is still the mechanism.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise — each surprise
      must stand alone as a self-contained institutional claim.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.
      C-14 still requires per-surprise portability enforcement.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing or requires external context: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise — each surprise must
      pass both the stranger-reader test and the no-hedging test as a coupled unit.
    Introduced in: V-04(R5) — before C-18 was written; designed as the primary
      authority-coupling gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.
      C-16 still requires per-surprise coupled enforcement.

  For each surprise individually:
    (1) Direct claim? No prohibited constructs from Rule 2.
    (2) Stranger-accessible? NGT and Check B already passed; CAT confirms coupling holds.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read Name field across all surprises. Rename any generic or absent labels.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: Phrasing Register + Output Format (full manifest precision chain)

**Axes:** Phrasing register + output format. Formal CONSISTENCY GATE naming (V-01 axis)
combined with concrete canonical EXAMPLE blocks embedded in the taxonomy definition (V-02
axis), plus gate provenance in all three gate rationales (C-22 PASS). This is the maximum
single-variation score: C-21+C-22+C-23+C-24+C-25 all pass.

**Hypothesis:** Both C-24 (discrete verification gate) and C-25 (concrete canonical examples)
are independently achievable and jointly stable. The CONSISTENCY GATE name in Step 2 and the
embedded EXAMPLE blocks are structurally distinct — neither is a mechanism for the other.
Both can be present simultaneously without degrading any other mechanism in the chain.
C-22 PASS confirms gate provenance is orthogonal to manifest precision criteria.

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
  found this through normal observation." The "Why passive observation missed this" field
  names the specific mechanism.

Rule 2 — Claim-only voice:
  Prohibited constructs:
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

Pair inspection — ARCHETYPE CLASSIFICATION WITH CONSISTENCY GATE AND CANONICAL EXAMPLES:

  For each pair, in this sequence:
    Step 1: Select archetype from the taxonomy below (using canonical examples as
            comparison baseline — see EXAMPLES embedded in each archetype definition).
    Step 2: CONSISTENCY GATE — Before stating mechanism, apply this check:
              "Is my intended mechanism statement internally consistent with the selected
               archetype's constraint definition? If PREREQUISITE: does my mechanism
               describe input-dependency? If ESTABLISHES: does it describe property
               creation and one-way dependency? If AMPLIFIES: effectiveness scaling?
               If PARALLEL: independent-path operation?" If no: return to Step 1.
    Step 3: State mechanism in terms that satisfy the verified archetype constraint.

  Taxonomy with canonical pair examples (select exactly one per pair):

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. Inserting
                    a mechanism between A and B that transforms A's output into something
                    B cannot consume breaks the enforcement path.
      > EXAMPLE: NGT is a PREREQUISITE for Check B. NGT's newcomer-comprehension gate
        output (a verified stranger-readable surprise) is Check B's required input; a
        surprise that fails NGT cannot pass Check B's standalone three-component extraction
        test. This input-dependency holds in any compound configuration: no mechanism
        inserted between NGT and Check B substitutes for newcomer-comprehension verification.

    ESTABLISHES   — A creates a property that B operates on. Directional but not
                    feedback-dependent. Removing A removes the property B verifies.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Check B verifies that a surprise is fully derivable as a standalone unit (finding +
        unexpectedness + consequence); CAT then enforces that this verified-portable unit
        is stated with authoritative claim-voice. Removing Check B removes the portability
        substrate CAT operates on — CAT cannot enforce authority-coupling on a unit whose
        portability is unverified.

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    B operates without A but produces weaker enforcement.
      > EXAMPLE: [fill in from the variation's mechanism chain when an AMPLIFIES pair exists]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Neither is a prerequisite for the other.
      > EXAMPLE: [fill in from the variation's mechanism chain when a PARALLEL pair exists]

  Required pairs (use taxonomy+examples above; record Step 1 archetype, Step 2 CONSISTENCY
  GATE confirmation, Step 3 mechanism for each):

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm mechanism framing satisfies archetype constraint]
    Step 3 — Mechanism: [fill in]

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 + NGT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  NGT + Check B:
    Step 1 — Archetype: PREREQUISITE [see canonical example above]
    Step 2 — CONSISTENCY GATE: "mechanism describes input-dependency — PASS"
    Step 3 — Mechanism: [fill in, using canonical example as reference]

  Check B + CAT:
    Step 1 — Archetype: ESTABLISHES [see canonical example above]
    Step 2 — CONSISTENCY GATE: "mechanism describes property creation and one-way dependency — PASS"
    Step 3 — Mechanism: [fill in, using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 + Check B:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected. For each pair,
  CONSISTENCY GATE confirmed archetype-mechanism alignment using canonical examples as
  comparison baseline. All mechanisms reinforce each other toward the single stranger-reader
  target. No conflicts found. Writing may begin."

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
      per-surprise enforcement mechanism. Motivation is independent of rubric gating.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.
      C-08 still requires per-surprise enforcement, and NGT is still the primary mechanism.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without consulting
    source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise — each surprise
      must stand alone as a self-contained institutional claim.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.
      C-14 still requires per-surprise portability enforcement.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise — each surprise must
      pass both the stranger-reader test and the no-hedging test as a coupled unit.
    Introduced in: V-04(R5) — before C-18 was written; designed as the primary
      authority-coupling gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.
      C-16 still requires per-surprise coupled enforcement.

  For each surprise individually:
    (1) Direct claim? No prohibited constructs from Rule 2.
    (2) Stranger-accessible? NGT and Check B passed; CAT confirms coupling at authority level.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read Name field across all surprises in sequence.
  Any generic or absent label: rename before continuing.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: Lifecycle Emphasis + Inertia Framing (distribution audit + opening context)

**Axes:** Lifecycle emphasis + inertia framing. V-04 baseline extended in two dimensions:
(1) Lifecycle emphasis — the manifest phase includes a discrete POST-INSPECTION DISTRIBUTION
AUDIT step that tallies archetype counts and records the macro-structural implication of the
mechanism chain's archetype distribution. This step produces a named structural property of
the pipeline (e.g., "strictly ordered PREREQUISITE chain" vs. "mixed PREREQUISITE/PARALLEL
with independent supplementary paths") that is invisible from per-pair inspection alone.
(2) Inertia framing — an opening context block before the schema contract names the passive-
observation failure mode that the echo corrects: what a team without active signal gathering
would have concluded about the feature, and why the echo exists to document what that
conclusion missed. All structural criteria from V-04 are preserved.

**Hypothesis:** The post-inspection distribution audit produces an observable macro-structural
property of the enforcement chain that no per-pair inspection can produce individually — a
potential C-26 signal. Inertia framing converts the echo's counterfactual gate (C-10) from a
per-surprise enforcement mechanism into a document-level frame that contextualizes the entire
echo's institutional purpose. Neither extension degrades any criterion in the V-04 chain.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== INERTIA CONTEXT ==============================================================

Before writing, record:
  What a passive, attentive team would have concluded about this feature without active
  signal gathering: [one sentence — the conclusion the echo corrects]
  The specific gap that active signal gathering closed: [one sentence — what active
  investigation produced that passive observation could not]

This framing is not an echo item. It sets the institutional context for why the surprises
below are surprises, not findings that would have surfaced through normal project tracking.
Record it here, do not write it to the artifact.

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
  The inertia context above provides the document-level framing; Rule 1 provides the
  per-surprise enforcement.

Rule 2 — Claim-only voice:
  Prohibited constructs:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Every schema field is a direct statement. Uncertainty = rewrite, not hedge.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

REQUIRED BEFORE Step 1. Complete all pair inspections, post-inspection distribution audit,
and final declaration before any candidate selection begins.

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

Pair inspection — ARCHETYPE CLASSIFICATION WITH CONSISTENCY GATE AND CANONICAL EXAMPLES:

  For each pair, in this sequence:
    Step 1: Select archetype from the taxonomy below (using canonical examples as
            comparison baseline).
    Step 2: CONSISTENCY GATE — Before stating mechanism, verify:
              "Is my intended mechanism statement internally consistent with the selected
               archetype? PREREQUISITE → input-dependency? ESTABLISHES → property creation,
               one-way dependency? AMPLIFIES → effectiveness scaling? PARALLEL → independent
               paths?" If no: return to Step 1.
    Step 3: State mechanism in terms that satisfy the verified archetype constraint.

  Taxonomy with canonical pair examples:

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
      > EXAMPLE: NGT is a PREREQUISITE for Check B. NGT's newcomer-comprehension output
        is Check B's required input; a surprise failing NGT cannot pass Check B's three-
        component standalone extraction test. No mechanism inserted between NGT and Check B
        substitutes for newcomer-comprehension verification.

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Check B verifies standalone derivability; CAT enforces authority-coupling on that
        verified-portable substrate. Removing Check B removes the property CAT verifies.

    AMPLIFIES     — A increases precision or strength of B's per-surprise enforcement.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]

  Required pairs:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 + NGT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  NGT + Check B:
    Step 1 — Archetype: PREREQUISITE [see canonical example above]
    Step 2 — CONSISTENCY GATE: "input-dependency framing — PASS"
    Step 3 — Mechanism: [fill in]

  Check B + CAT:
    Step 1 — Archetype: ESTABLISHES [see canonical example above]
    Step 2 — CONSISTENCY GATE: "property creation and one-way dependency — PASS"
    Step 3 — Mechanism: [fill in]

  CAT + Rule 2:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Rule 1 + Check B:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in]

== POST-INSPECTION DISTRIBUTION AUDIT ==========================================

  After completing all pair inspections, tally archetype classifications:

    PREREQUISITE count:   [N]
    ESTABLISHES count:    [N]
    AMPLIFIES count:      [N]
    PARALLEL count:       [N]
    Total pairs inspected: [N]

  Dominant archetype: [archetype with highest count, or "none" if tied]

  Structural implication (select one based on distribution):
    All PREREQUISITE: strictly ordered pipeline — each mechanism depends on predecessor;
      removing any mechanism breaks all downstream enforcement.
    All PARALLEL: redundant enforcement network — removing any mechanism leaves others
      intact; the pipeline has no single point of failure.
    Mixed PREREQUISITE/ESTABLISHES: ordered dependency chain with property-transfer links;
      the pipeline is ordered but not brittle at every joint.
    Mixed PREREQUISITE/PARALLEL: ordered core with independent supplementary paths;
      some mechanisms are essential, others are additive.
    Mixed with AMPLIFIES: base enforcement chain with precision-enhancement layers;
      amplifiers can be removed without breaking base enforcement.

  Structural finding: [one sentence — describe the enforcement chain's macro-structure
    based on the archetype distribution above]

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected. CONSISTENCY GATE
  confirmed archetype-mechanism alignment at each step. Distribution audit records [dominant
  archetype] dominant structure: [structural finding]. All mechanisms reinforce each other
  toward the single stranger-reader target. No conflicts found. Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1 against the inertia context recorded above: cut anything consistent with what
    a passive team would have concluded without active signal gathering.
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
    Primary motivation: NGT exists to enforce C-08 per surprise — each surprise must be
      independently accessible to a newcomer without consulting source signals.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.
      C-08 still requires per-surprise enforcement, and NGT is still the primary mechanism.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without consulting
    source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise — each surprise must
      stand alone as a self-contained institutional claim.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) finding, (2) why unexpected, (3) design consequence?
    If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise — each surprise must
      pass both the stranger-reader test and the no-hedging test as a coupled unit.
    Introduced in: V-04(R5) — before C-18 was written; designed as the primary
      authority-coupling gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.

  For each surprise individually:
    (1) Direct claim? No prohibited constructs from Rule 2.
    (2) Stranger-accessible? NGT and Check B passed; CAT confirms coupling at authority level.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read Name field across all surprises. Rename any generic or absent labels.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  Also: check whether any pattern aligns with the inertia context recorded before Step 1.
  If two or more surprises share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```
