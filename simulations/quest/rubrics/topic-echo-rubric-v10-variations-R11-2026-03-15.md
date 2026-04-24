
# Variations: `topic:echo` — Round 11

**Rubric:** v10 (max 100) | **Date:** 2026-03-15

---

## Design Context

R10 promoted C-21 and C-23 to proven and revealed three new structural patterns: C-26
(constraint vocabulary in CONSISTENCY GATE), C-27 (synthesis claim separation in pair
inspection), and C-28 (pre-populated baseline pair inspection). R10 demonstrated C-24 in
V-01/V-04/V-05 and C-25 in V-02/V-04/V-05. Both C-24 and C-25 have been demonstrated across
two rounds (C-24: R9 V-01, R10 V-01/V-04/V-05; C-25: R9 V-01, R10 V-02/V-04/V-05).

R11 provides five variations designed to:
1. Demonstrate C-24 and C-25 uniformly across all five variations — enabling proven promotion
   in v11.
2. Isolate C-26, C-27, and C-28 as independently achievable single-axis dimensions (one per
   single-axis variation).
3. Confirm joint stability of C-26+C-27 (V-04) and all three together (V-05).

**Unproven criteria targeted in R11:**

- **C-24** — Archetype-mechanism consistency verification (1 pt): manifest template includes a
  discrete named gate instructing active archetype-mechanism consistency check before mechanism
  is stated. A parenthetical field annotation does not satisfy this; a named step does.
  Demonstrated in R9 V-01 and R10 V-01/V-04/V-05.

- **C-25** — Archetype taxonomy illustration (1 pt): manifest template provides at least one
  concrete canonical pair example per archetype used. Abstract taxonomy definition alone does
  not satisfy; named pair instances with archetype label and mechanism do.
  Demonstrated in R9 V-01 and R10 V-02/V-04/V-05.

- **C-26** — Archetype constraint vocabulary specification (1 pt): CONSISTENCY GATE names the
  specific constraint class for each archetype — input-dependency (PREREQUISITE), property
  creation (ESTABLISHES), effectiveness scaling (AMPLIFIES), independent paths (PARALLEL) —
  making the verification instruction a binary vocabulary check rather than an author-judgment
  call. First demonstrated in R10 V-01/V-04.

- **C-27** — Composability manifest synthesis claim separation (1 pt): pair inspection uses a
  Mechanism field for the analytical causal description and a distinct Composability-claim
  field for the synthetic composability assertion. Each field is independently evaluable.
  First demonstrated in R10 V-03.

- **C-28** — Manifest pre-populated baseline pair inspection (1 pt): manifest template embeds
  at least one fully pre-completed pair entry (archetype + mechanism + gate result all
  pre-filled) as a carry-forward baseline. Structurally distinct from C-25's illustrative
  EXAMPLE blocks, which require the author to classify from scratch.
  First demonstrated in R10 V-04/V-05.

**Predicted score map:**

| Variant | C-22 | C-24 | C-25 | C-26 | C-27 | C-28 | Predicted |
|---------|------|------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | FAIL | FAIL | 100       |
| V-02    | PASS | PASS | PASS | FAIL | PASS | FAIL | 100       |
| V-03    | PASS | PASS | PASS | FAIL | FAIL | PASS | 100       |
| V-04    | PASS | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-05    | PASS | PASS | PASS | PASS | PASS | PASS | 100       |

**Scoring note:** Base 77 + proven 22 = 99. Each variation earns C-24(1) + C-25(1) + at least
one of C-26/C-27/C-28(1) = 3 unproven → 99+3 = 102 → capped 100. Differentiating dimension:
which of C-26/C-27/C-28 pass. Uniform PASS of C-24 and C-25 across all five — combined with
R9 and R10 evidence across two prior rounds — enables proven promotion in v11.

**Axis selection:**

Single-axis (V-01, V-02, V-03):
- V-01 — Phrasing register: CONSISTENCY GATE names vocabulary constraint class per archetype
  (PREREQUISITE → input-dependency, ESTABLISHES → property creation, AMPLIFIES → effectiveness
  scaling, PARALLEL → independent paths). Two-field pair output: Archetype + Mechanism.
  C-26 PASS, C-27 FAIL (no Composability-claim field), C-28 FAIL (no pre-populated entry).
  C-26 is the single differentiating new axis.

- V-02 — Output format: pair inspection uses four-field sequence (Archetype → CONSISTENCY
  GATE → Mechanism → Composability-claim). Gate present but vocabulary-free: instructs
  "confirm mechanism matches selected archetype" without naming constraint classes (C-26 FAIL).
  Composability-claim is a distinct synthetic field separate from analytical Mechanism.
  C-27 PASS, C-26 FAIL, C-28 FAIL. C-27 is the single differentiating new axis.

- V-03 — Lifecycle emphasis: pair inspection template carries a fully pre-completed NGT+Check B
  baseline entry (all fields pre-filled: archetype, gate confirmation, and mechanism). Gate
  present but vocabulary-free (C-26 FAIL). Three-field output: Archetype + Gate + Mechanism,
  no Composability-claim (C-27 FAIL). C-28 PASS, C-26 FAIL, C-27 FAIL. C-28 is the single
  differentiating new axis.

Combined (V-04, V-05):
- V-04 — Phrasing register + output format: vocabulary-specified CONSISTENCY GATE (C-26) +
  four-field pair sequence with Composability-claim (C-27). No pre-populated baseline
  (C-28 FAIL). Confirms C-26 and C-27 are jointly achievable without requiring C-28.

- V-05 — Lifecycle emphasis + inertia framing: V-04 baseline extended with a pre-populated
  four-field baseline entry for NGT+Check B (C-28 PASS) and an opening inertia context block.
  All three new criteria simultaneously present. Inertia framing converts the document-level
  counterfactual context into an explicit pre-write commitment.

---

## V-01 — Single-axis: Phrasing Register (vocabulary-specified CONSISTENCY GATE; two-field pairs; no Composability-claim; no pre-populated entry)

**Axis:** Phrasing register — the CONSISTENCY GATE names a specific vocabulary constraint
class for each archetype. Instead of instructing "verify mechanism is consistent with the
selected archetype" (impressionistic), the gate provides the binary vocabulary test for
each archetype: PREREQUISITE → input-dependency, ESTABLISHES → property creation and one-way
dependency, AMPLIFIES → effectiveness scaling, PARALLEL → independent-path operation. Each
archetype maps to a named constraint class; the gate verdict is vocabulary-driven, not
author-judgment-driven. Pair output uses two fields (Archetype + Mechanism; no
Composability-claim). Taxonomy includes concrete canonical examples (C-25 PASS). Gate
provenance for all three per-surprise gates (C-22 PASS). No pre-populated baseline (C-28 FAIL).

**Hypothesis:** C-26 requires only vocabulary specification in the gate instruction and can
pass without a Composability-claim third field (C-27 FAIL) or a pre-populated baseline entry
(C-28 FAIL). The constraint vocabulary is a property of the gate's instruction text, not of
the pair inspection's field structure. Naming the constraint class converts C-24's verification
step from an author-judgment call to a binary vocabulary check, making the gate testable.

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

Pair inspection — ARCHETYPE CLASSIFICATION WITH VOCABULARY-SPECIFIED CONSISTENCY GATE:

  For each pair, in this sequence:
    Step 1: Select archetype from the taxonomy below (use canonical examples as
            comparison baseline — see EXAMPLES embedded in each archetype definition).
    Step 2: CONSISTENCY GATE — Apply the vocabulary check for the selected archetype:
              PREREQUISITE → "Does my mechanism describe input-dependency?
                              Does it state that A's output is B's required input?"
              ESTABLISHES  → "Does my mechanism describe property creation and one-way
                              dependency? Does it state that A creates a property B
                              operates on, without feedback from B to A?"
              AMPLIFIES    → "Does my mechanism describe effectiveness scaling?
                              Does it state that A increases the precision or strength
                              of B's per-surprise enforcement?"
              PARALLEL     → "Does my mechanism describe independent-path operation?
                              Does it state that A and B enforce from non-dependent
                              paths, each sufficient alone?"
            If NO for the selected vocabulary check: return to Step 1.
    Step 3: State mechanism in terms that satisfy the verified vocabulary constraint.

  Taxonomy with canonical pair examples (select exactly one per pair):

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. Vocabulary
                    check: mechanism must describe input-dependency.
      > EXAMPLE: NGT is a PREREQUISITE for Check B. NGT's newcomer-comprehension output
        is Check B's required input; a surprise that fails NGT cannot pass Check B's
        three-component standalone extraction test (finding + unexpectedness + consequence).
        Input-dependency confirmed: no mechanism inserted between NGT and Check B
        substitutes for newcomer-comprehension verification.

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
                    Vocabulary check: mechanism must describe property creation and
                    one-way dependency.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Check B verifies standalone derivability; CAT enforces authority-coupling on the
        verified-portable substrate. Removing Check B removes the portability property CAT
        verifies. Property creation and one-way dependency confirmed.

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    B operates without A but produces weaker enforcement. Vocabulary check:
                    mechanism must describe effectiveness scaling.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Neither is a prerequisite for the other. Vocabulary check: mechanism must
                    describe independent-path operation.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]

  Required pairs (inspect all; add any pair where conflict is possible):

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check for selected archetype — state
              constraint class and YES/NO verdict]
    Step 3 — Mechanism: [fill in]

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Rule 1 + NGT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  NGT + Check B:
    Step 1 — Archetype: [select — compare against PREREQUISITE example above]
    Step 2 — CONSISTENCY GATE: [input-dependency vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in using canonical example as reference]

  Check B + CAT:
    Step 1 — Archetype: [select — compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [property creation/one-way dependency vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Schema manifest + Label parity audit:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Label parity audit + Field completion scan:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Rule 1 + Check B:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Stranger-reader commitment + CAT:
    Step 1 — Archetype: [select]
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected. For each pair,
  CONSISTENCY GATE applied vocabulary check for selected archetype; constraint class
  confirmed (input-dependency / property creation / effectiveness scaling / independent
  paths) before mechanism was stated. All mechanisms reinforce each other toward the single
  stranger-reader target. No conflicts found. Writing may begin."

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
      per-surprise enforcement mechanism for that requirement.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.
      C-08 still requires per-surprise newcomer accessibility enforcement.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise. C-14 requires each
      surprise to stand alone as a self-contained institutional claim.
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
    Primary motivation: CAT exists to enforce C-16 per surprise. C-16 requires each
      surprise to pass both the stranger-reader test and the no-hedging test as a
      coupled unit; CAT is the designated per-surprise enforcement mechanism.
    Introduced in: V-04(R5) — before C-18 was written; designed as the primary
      authority-coupling gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.
      C-16 still requires per-surprise coupled enforcement.

  For each surprise individually:
    (1) Is this surprise stated as a direct claim? (No prohibited constructs from Rule 2.)
    (2) Is this surprise accessible to a stranger without project context? (NGT and Check B
        must have already passed; CAT confirms coupling holds at authoritative-voice level.)
    Both must be YES. If either is NO: rewrite before continuing.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises in sequence.
  Failing labels: "Finding N", "Surprise A", any generic category header.
  Any generic or absent label: rename before continuing to Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises in sequence:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  Every field must contain substantive content. No N/A, no blank, no placeholder text.
  Any gap: return to Step 2 for that surprise.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  If any two share a root cause: write one Patterns section. Name the shared dynamic
  explicitly. One sentence per pattern. Do not redescribe individual surprises.
  If no shared roots: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Count all words in the full echo.
  If total exceeds 800 words: extract and cut. The echo is a claim document, not a narrative.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-02 — Single-axis: Output Format (four-field pairs with Composability-claim; no vocabulary in gate; no pre-populated entry)

**Axis:** Output format — pair inspection uses a four-field sequence: Archetype → CONSISTENCY
GATE → Mechanism → Composability-claim. The Mechanism field carries the analytical causal
description ("what is the causal relationship between A and B?"). The Composability-claim
field carries the synthetic composability assertion ("what does that relationship imply for
their combined behavior?"). These are semantically distinct fields, each independently
evaluable. The CONSISTENCY GATE is present as a discrete named step (C-24 PASS) but carries
no vocabulary specification — it instructs "confirm mechanism matches selected archetype"
without naming constraint classes (C-26 FAIL). Taxonomy includes canonical examples (C-25
PASS). Gate provenance for all three gates (C-22 PASS). No pre-populated baseline (C-28 FAIL).

**Hypothesis:** C-27 requires field-level separation of the analytical mechanism description
from the synthetic composability claim and can pass without vocabulary specification in the
gate (C-26 FAIL) or a pre-populated baseline entry (C-28 FAIL). The separation is a property
of the pair inspection's field structure, not of the gate's instruction text. A merged field
hides the analytical/synthetic distinction; a two-field structure exposes it: a causal
mechanism can be accurately described while its composability conclusion is incorrectly drawn,
and the separation makes the inconsistency visible.

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

Pair inspection — FOUR-FIELD SEQUENCE: ARCHETYPE → GATE → MECHANISM → COMPOSABILITY-CLAIM:

  For each pair:
    Step 1 — Archetype:           [select from taxonomy below; archetype must precede
                                   mechanism — use canonical examples as comparison baseline]
    Step 2 — CONSISTENCY GATE:    [before stating mechanism, confirm: does your intended
                                   mechanism statement match the selected archetype? If
                                   not: return to Step 1 with corrected archetype or framing]
    Step 3 — Mechanism:           [analytical causal statement — name the directional
                                   mechanism by which A's output, property, or effect
                                   enables or amplifies B's function; not just "reinforce"]
    Step 4 — Composability-claim: [synthetic conclusion — one sentence stating what the
                                   causal mechanism in Step 3 implies for this pair's
                                   composability; distinct from the mechanism description]

  The Mechanism field (Step 3) answers: "What is the causal relationship between A and B?"
  The Composability-claim field (Step 4) answers: "What does that relationship imply for
  their combined composability?" Complete each field independently — do not merge them.

  Taxonomy with canonical pair examples (select exactly one per pair):

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
      > EXAMPLE: NGT is a PREREQUISITE for Check B.
        Mechanism: "NGT's newcomer-comprehension output is Check B's required input; a
          surprise failing NGT cannot pass Check B's three-component standalone extraction
          test. No mechanism between NGT and Check B substitutes for newcomer-comprehension
          verification."
        Composability-claim: "NGT and Check B compose without degradation: NGT's
          accessibility enforcement produces the verified stranger-readable unit that Check B's
          portability test requires, creating a forward dependency without competing demands."

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Mechanism: "Check B verifies that a surprise is fully derivable as a standalone unit
          (finding + unexpectedness + consequence); CAT enforces that this verified-portable
          unit is stated with authoritative claim-voice. Removing Check B removes the
          portability substrate CAT operates on."
        Composability-claim: "Check B and CAT compose without degradation: the portability
          substrate Check B establishes is the precondition CAT requires, not a constraint
          CAT circumvents."

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]
        Mechanism: [...]
        Composability-claim: [...]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]
        Mechanism: [...]
        Composability-claim: [...]

  Required pairs:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  NGT + Check B:
    Step 1 — Archetype: [see PREREQUISITE example above]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in using canonical example as reference]
    Step 4 — Composability-claim: [fill in using canonical example as reference]

  Check B + CAT:
    Step 1 — Archetype: [see ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in using canonical example as reference]
    Step 4 — Composability-claim: [fill in using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-field
  format (Archetype → Gate → Mechanism → Composability-claim). Mechanism and Composability-
  claim fields completed separately for each pair — analytical description and synthetic
  assertion independently evaluable. All mechanisms reinforce each other toward the single
  stranger-reader target. No conflicts found. Writing may begin."

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
    Primary motivation: NGT exists to enforce C-08 per surprise; NGT is the designated
      per-surprise enforcement mechanism for that requirement.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise.
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
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: Lifecycle Emphasis (pre-populated baseline entry; no vocabulary; no Composability-claim)

**Axis:** Lifecycle emphasis — the composability manifest template carries a fully
pre-completed baseline pair inspection for NGT+Check B. All three fields are pre-filled:
archetype selected (PREREQUISITE), gate confirmation recorded ("input-dependency — PASS"),
and mechanism stated in full. This entry is a carry-forward institutional asset: the author
inherits a verified, quality-floor inspection and does not re-derive it. Remaining pairs use
blank templates. The CONSISTENCY GATE is present as a discrete named step (C-24 PASS) but
without vocabulary specification — it instructs "confirm consistency" without naming constraint
classes (C-26 FAIL). Three-field pair output: Archetype + Gate + Mechanism; no Composability-
claim (C-27 FAIL). Canonical examples in taxonomy (C-25 PASS). Gate provenance (C-22 PASS).

**Hypothesis:** C-28 requires at least one fully pre-completed pair entry (archetype + gate
result + mechanism all pre-filled) and can pass without vocabulary specification in the gate
(C-26 FAIL) or a Composability-claim field (C-27 FAIL). The pre-population is a manifest
template property — it concerns what is present before the author writes, not how the gate
tests consistency or whether the pair inspection outputs a synthesis claim. The structural
value of C-28 is the quality floor it establishes: the manifest contains at least one entry
that demonstrably satisfies C-21 and C-23 criteria independent of author effort in this round.

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

Pair inspection — ARCHETYPE CLASSIFICATION WITH CONSISTENCY GATE AND PRE-POPULATED BASELINE:

  For each pair, in this sequence:
    Step 1: Select archetype from the taxonomy below (use canonical examples as
            comparison baseline — see EXAMPLES embedded in each archetype definition).
    Step 2: CONSISTENCY GATE — Before stating mechanism, confirm: does your intended
            mechanism statement match the selected archetype? If not: return to Step 1.
    Step 3: State mechanism consistent with the verified archetype.

  PRE-POPULATED BASELINE ENTRY (carry forward — do not re-derive):

  NGT + Check B: [BASELINE — pre-classified and verified; inherited by this manifest]
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: mechanism describes input-dependency — PASS.
              NGT's newcomer-comprehension output is Check B's required input.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise that fails NGT cannot pass Check B's three-component
              standalone extraction test (finding + unexpectedness + design consequence).
              This input-dependency holds in any compound configuration: no mechanism
              inserted between NGT and Check B substitutes for newcomer-comprehension
              verification.

  Use the baseline entry above as the within-manifest quality standard for all subsequent
  pair inspections. Each subsequent inspection should meet or exceed the baseline's level
  of specificity in the mechanism field.

  Taxonomy with canonical pair examples (select exactly one per pair):

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
      > EXAMPLE: see pre-populated baseline entry above (NGT + Check B).

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Check B verifies standalone derivability; CAT enforces authority-coupling on the
        verified-portable substrate. Removing Check B removes the portability property CAT
        verifies.

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]

  Remaining required pairs (baseline NGT+Check B entry already complete above):

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

  Check B + CAT:
    Step 1 — Archetype: [see ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [confirm]
    Step 3 — Mechanism: [fill in using canonical example as reference]

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

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected. Pre-populated
  baseline (NGT+Check B, PREREQUISITE, input-dependency) carried forward as quality
  standard. CONSISTENCY GATE confirmed archetype-mechanism alignment at each step.
  All mechanisms reinforce each other toward the single stranger-reader target.
  No conflicts found. Writing may begin."

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise.
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
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: Phrasing Register + Output Format (vocabulary gate + Composability-claim; no pre-populated entry)

**Axes:** Phrasing register + output format. The vocabulary-specified CONSISTENCY GATE from
V-01 (C-26 PASS) combined with the four-field pair inspection structure from V-02, where the
Composability-claim field is a distinct synthetic assertion separate from the Mechanism field
(C-27 PASS). Canonical examples in taxonomy (C-25 PASS). Gate provenance (C-22 PASS). No
pre-populated baseline entry (C-28 FAIL). This is the full C-26+C-27 compound without C-28.

**Hypothesis:** C-26 and C-27 are jointly stable without requiring C-28. The vocabulary
specification is a property of the gate instruction; the Composability-claim is a property
of the pair inspection's field structure; the pre-populated baseline entry is a property of
the manifest template's pre-written content. All three are orthogonal. V-04 confirms that
embedding vocabulary in the gate (C-26) and adding a Composability-claim field (C-27) do not
create structural friction with each other: the gate tests vocabulary-consistency before the
Mechanism field is stated, and the Composability-claim field operates on top of the verified
Mechanism field, creating a four-step chain: Archetype → Vocabulary-Gate → Mechanism →
Composability-claim.

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

Pair inspection — VOCABULARY-GATED FOUR-FIELD SEQUENCE:
  Archetype → Vocabulary-Gate → Mechanism → Composability-claim

  For each pair:
    Step 1 — Archetype:           [select from taxonomy below; use canonical examples as
                                   comparison baseline; archetype must precede mechanism]
    Step 2 — CONSISTENCY GATE:    [apply vocabulary check for the selected archetype:
                                   PREREQUISITE → input-dependency: "Does mechanism state
                                     A's output is B's required input?"
                                   ESTABLISHES  → property creation: "Does mechanism state
                                     A creates a property that B operates on, without
                                     feedback from B to A?"
                                   AMPLIFIES    → effectiveness scaling: "Does mechanism
                                     state A increases the precision or strength of B's
                                     per-surprise enforcement?"
                                   PARALLEL     → independent paths: "Does mechanism state
                                     A and B enforce from non-dependent paths, each
                                     sufficient alone?"
                                   If NO for the selected vocabulary check: return to Step 1]
    Step 3 — Mechanism:           [analytical causal statement satisfying the verified
                                   vocabulary constraint — name the directional mechanism]
    Step 4 — Composability-claim: [synthetic conclusion — one sentence on what the causal
                                   mechanism in Step 3 implies for this pair's composability]

  The Mechanism field (Step 3) and Composability-claim field (Step 4) are semantically
  distinct. Step 3 is an analytical description of a mechanism property. Step 4 is a
  synthetic assertion about what that mechanism means for the pair's combined behavior.
  Complete each field independently — do not merge them into Step 3.

  Taxonomy with canonical pair examples (select exactly one per pair):

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
                    Vocabulary check: mechanism must describe input-dependency.
      > EXAMPLE: NGT is a PREREQUISITE for Check B.
        Mechanism: "NGT's newcomer-comprehension output is Check B's required input; a
          surprise failing NGT cannot pass Check B's three-component standalone extraction
          test. No mechanism between NGT and Check B substitutes for newcomer-comprehension
          verification."
        Composability-claim: "NGT and Check B compose without degradation: NGT's
          accessibility enforcement produces the verified input Check B requires, creating
          a forward dependency without competing demands."

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
                    Vocabulary check: mechanism must describe property creation and one-way
                    dependency.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Mechanism: "Check B verifies standalone derivability (finding + unexpectedness +
          consequence); CAT enforces authority-coupling on that verified-portable substrate.
          Removing Check B removes the portability property CAT verifies."
        Composability-claim: "Check B and CAT compose without degradation: the portability
          substrate Check B establishes is the precondition CAT requires, not a constraint
          it circumvents."

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    Vocabulary check: mechanism must describe effectiveness scaling.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]
        Mechanism: [...]
        Composability-claim: [...]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Vocabulary check: mechanism must describe independent-path operation.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]
        Mechanism: [...]
        Composability-claim: [...]

  Required pairs:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  NGT + Check B:
    Step 1 — Archetype: [see PREREQUISITE example above]
    Step 2 — CONSISTENCY GATE: [input-dependency vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in using canonical example as reference]
    Step 4 — Composability-claim: [fill in using canonical example as reference]

  Check B + CAT:
    Step 1 — Archetype: [see ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [property creation vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]
    Step 4 — Composability-claim: [fill in]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-field
  vocabulary-gated format. CONSISTENCY GATE applied vocabulary check (input-dependency /
  property creation / effectiveness scaling / independent paths) for each selected archetype
  before mechanism was stated. Mechanism and Composability-claim fields completed separately
  for each pair. All mechanisms reinforce each other toward the single stranger-reader target.
  No conflicts found. Writing may begin."

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise.
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
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: Lifecycle Emphasis + Inertia Framing (all three new criteria + inertia context)

**Axes:** Lifecycle emphasis + inertia framing. V-04 baseline extended in two dimensions:
(1) Lifecycle emphasis — the manifest template carries a fully pre-populated four-field
baseline entry for NGT+Check B (all fields pre-filled: archetype, vocabulary-gate result,
mechanism, and composability-claim). This inherits the C-26+C-27 chain from V-04 and adds
C-28's pre-population property: the NGT+Check B baseline entry is a completed four-field
inspection, not a blank template row.
(2) Inertia framing — an INERTIA CONTEXT block before the schema contract records, before
any writing begins, what a passive team would have concluded without active signal gathering
and what active investigation produced that passive observation could not. This converts the
document-level counterfactual gate (C-10) from an implied constraint into an explicit
pre-write commitment.

All structural criteria from V-04 (C-24, C-25, C-26, C-27) are preserved.

**Hypothesis:** C-28 is achievable alongside C-26 and C-27 simultaneously. The pre-populated
four-field baseline entry (C-28) extends the V-04 template without degrading either the
vocabulary gate (C-26) or the Composability-claim separation (C-27): the pre-populated entry
demonstrates all four fields completed at quality-floor level, serving as both a carry-forward
institutional asset and a within-manifest quality standard for subsequent inspections. Inertia
framing sets a document-level context that reinforces Rule 1's per-surprise counterfactual
gate without creating structural friction with any mechanism in the chain.

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
Record it here; do not write it to the artifact.

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

Pair inspection — VOCABULARY-GATED FOUR-FIELD SEQUENCE WITH PRE-POPULATED BASELINE:
  Archetype → Vocabulary-Gate → Mechanism → Composability-claim

  For each pair:
    Step 1 — Archetype:           [select from taxonomy below; use canonical examples as
                                   comparison baseline; archetype must precede mechanism]
    Step 2 — CONSISTENCY GATE:    [apply vocabulary check for the selected archetype:
                                   PREREQUISITE → input-dependency: "Does mechanism state
                                     A's output is B's required input?"
                                   ESTABLISHES  → property creation: "Does mechanism state
                                     A creates a property that B operates on, without
                                     feedback from B to A?"
                                   AMPLIFIES    → effectiveness scaling: "Does mechanism
                                     state A increases the precision or strength of B's
                                     per-surprise enforcement?"
                                   PARALLEL     → independent paths: "Does mechanism state
                                     A and B enforce from non-dependent paths, each
                                     sufficient alone?"
                                   If NO for the selected vocabulary check: return to Step 1]
    Step 3 — Mechanism:           [analytical causal statement satisfying the verified
                                   vocabulary constraint]
    Step 4 — Composability-claim: [synthetic conclusion — one sentence on what the causal
                                   mechanism implies for this pair's composability]

  PRE-POPULATED BASELINE ENTRY (carry forward — do not re-derive):

  NGT + Check B: [BASELINE — all four fields pre-completed; inherited by this manifest]
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: PREREQUISITE → input-dependency check: "Does mechanism state
              NGT's output is Check B's required input?" YES — PASS.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise that fails NGT cannot pass Check B's three-component
              standalone extraction test (finding + unexpectedness + design consequence).
              This input-dependency holds in any compound configuration: no mechanism
              inserted between NGT and Check B substitutes for newcomer-comprehension
              verification.
    Step 4 — Composability-claim: NGT and Check B compose without degradation: NGT's
              accessibility enforcement produces the verified stranger-readable unit that
              Check B's portability test requires, creating a forward dependency without
              competing demands on the author.

  Use the baseline entry above as the within-manifest quality standard for all subsequent
  pair inspections. Each subsequent inspection should match the baseline's specificity in
  Steps 3 and 4.

  Taxonomy with canonical pair examples (select exactly one per pair):

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B.
                    Vocabulary check: mechanism must describe input-dependency.
      > EXAMPLE: see pre-populated baseline entry (NGT + Check B) above.

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
                    Vocabulary check: mechanism must describe property creation and one-way
                    dependency.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Mechanism: "Check B verifies standalone derivability; CAT enforces authority-coupling
          on the verified-portable substrate. Removing Check B removes the property CAT
          verifies."
        Composability-claim: "Check B and CAT compose without degradation: the portability
          substrate Check B establishes is the precondition CAT requires, not a constraint
          it circumvents."

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    Vocabulary check: mechanism must describe effectiveness scaling.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]
        Mechanism: [...]
        Composability-claim: [...]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Vocabulary check: mechanism must describe independent-path operation.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]
        Mechanism: [...]
        Composability-claim: [...]

  Remaining required pairs (baseline NGT+Check B entry already complete above):

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT:
    Step 1 — Archetype: [see ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [property creation vocabulary check — YES/NO]
    Step 3 — Mechanism: [fill in]
    Step 4 — Composability-claim: [fill in]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE:
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using vocabulary-
  gated four-field format. Pre-populated baseline (NGT+Check B, PREREQUISITE, input-
  dependency, four fields complete) carried forward as quality standard. CONSISTENCY GATE
  applied vocabulary check for each selected archetype before mechanism was stated. Mechanism
  and Composability-claim fields completed separately for each pair. All mechanisms reinforce
  each other toward the single stranger-reader target. No conflicts found. Writing may begin."

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before Check B.

== STEP 4 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step after NGT, before CAT]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after Check B]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise.
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
  If any share a root cause: write one Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```
