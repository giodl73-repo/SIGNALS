# Variations: `topic:echo` — Round 15

**Rubric:** v14 (max 100) | **Date:** 2026-03-15

---

## Design Context

R14 was the first confirmed round for C-31 (cross-layer synthesis claim coherence). All five
R14 variations passed C-31 uniformly — the composability manifest's three synthetic layers
(live inspection C-27, canonical illustration C-29, pre-populated baseline C-30) carry
mutually consistent synthesis claims for shared mechanism pairs. Second confirmation in R15
promotes C-31 to Proven.

R14 also identified three new aspirational criteria, each from a single-variation observation:

- **C-32** — Coherence audit verbatim-restate depth (R14/V-01 canonical reference)
- **C-33** — Coherence audit gate-order independence by structural isolation (R14/V-02)
- **C-34** — Pre-inspection domain failure mode taxonomy (R14/V-03)

R15 has three structural goals:

**Goal 1 — Second confirmation of C-31**: All five R15 variations must pass C-31. Combined
with R14's first confirmation, the two-round threshold is met. C-31 promotes to Proven in v15.

**Goal 2 — First targeted round for C-32, C-33, C-34**: R14 confirmed each in a single
variation. R15 is the first round that targets them systematically across variation families.
Design decision: C-32 (verbatim-restate depth) is the default coherence audit implementation
for R15 single-axis variations V-01 through V-03 — except V-02 and V-03, which explicitly
ablate it by design to test C-33 and C-34 in isolation. V-04 and V-05 combine.

**Goal 3 — Axis isolation**: Each single-axis variation modifies exactly one structural
property against the R14 canonical baseline. Combined variations compose without degradation.

**Unproven criteria targeted:**

- C-32 — Coherence audit verbatim-restate depth (V-01, V-04, V-05)
- C-33 — Coherence audit gate-order independence (V-02, V-04, V-05)
- C-34 — Pre-inspection domain failure mode taxonomy (V-03, V-05)

**Proven criteria maintained:** C-10 through C-30 — all must continue to pass in every
variation.

**Predicted score map (v14 rubric):**

| Variant | C-31 | C-32 | C-33 | C-34 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | FAIL | FAIL | 100       |
| V-02    | PASS | FAIL | PASS | FAIL | 100       |
| V-03    | PASS | FAIL | FAIL | PASS | 100       |
| V-04    | PASS | PASS | PASS | FAIL | 100       |
| V-05    | PASS | PASS | PASS | PASS | 100       |

Scoring note: Under v14, proven = 29 pts, budget = 25 pts, ceiling = 100. Base 75 + min(29, 25)
= 100 before any unproven. All four unproven targets (C-31, C-32, C-33, C-34) are supra-budget;
pass/fail on these does not change the numerical score until v15 promotes C-31 to proven and
updates the budget. The score map reflects ceiling-at-proven; the structural distinctions
between variations are the evidence base for criterion promotion, not score differentiation.

**Axis selection:**

Single-axis (V-01, V-02, V-03):

- V-01 — **C-32 verbatim-restate depth**: Coherence audit includes explicit verbatim-restate
  protocol — author directed to restate each layer's synthesis claim verbatim, named with its
  layer identifier, in the audit section before the verdict gate. Makes the audit self-sufficient.
  All other properties constant: standard gate order NGT → Check B → CAT; vocabulary-specified
  CONSISTENCY GATE (C-26); Composability-claim field in every pair (C-27); template-complete
  canonical examples (C-29 PASS); template-complete baseline (C-30 PASS); no explicit structural
  isolation declaration (C-33 FAIL by design).

- V-02 — **C-33 explicit gate-order independence**: Coherence audit section has an explicit
  post-inspection structural constraint header and a manifest-completion entry gate that declares
  the audit's post-inspection positioning as an architectural property — not emergent from the
  current gate ordering. No verbatim-restate instruction (C-32 FAIL by design). Standard gate
  order NGT → Check B → CAT.

- V-03 — **C-34 pre-inspection failure mode taxonomy**: Preamble block before pair inspections
  names "silent antagonism" and "archetype drift" as cross-pair failure mode patterns — mechanism
  types detectable only across the inspection set. No verbatim-restate (C-32 FAIL by design), no
  explicit isolation (C-33 FAIL by design). Standard coherence audit (C-31 PASS).

Combined (V-04, V-05):

- V-04 — **C-32 + C-33**: Verbatim-restate protocol combined with explicit post-inspection
  structural isolation. Tests whether the two structural properties are additive without friction.
  No failure mode preamble (C-34 FAIL by design).

- V-05 — **C-32 + C-33 + C-34**: Full three-axis combination. Tests whether all three interact
  cleanly while maintaining the complete proven property set.

---

## V-01 — Single-axis: C-32 Verbatim-Restate Depth

**Axis:** Coherence audit verbatim-restate depth — the cross-layer coherence audit includes a
verbatim-restate protocol that directs the author to restate each of the three layers' synthesis
claims verbatim, named with their layer identifiers, in the audit section before the
COHERENT/INCOHERENT verdict gate. All structural properties held constant: standard gate order
(NGT → Check B → CAT); vocabulary-specified CONSISTENCY GATE (C-26); Composability-claim field
in every pair inspection (C-27); template-complete canonical examples (C-29 PASS);
template-complete pre-populated baseline (C-30 PASS); no explicit structural isolation
declaration (C-33 FAIL by design — isolation is positional, not architecturally declared).

**Hypothesis:** Verbatim-restate depth is orthogonal to all properties that determine C-31
pass/fail. C-31 requires an audit section, three named layers, a verdict gate, and a blocking
instruction — all present here regardless of restate depth. C-32 adds a self-sufficiency
property: an audit that instructs the author to restate each layer's claim verbatim is
document-local — the comparison executes from claims present in the audit section without
requiring the author to retrieve or recall claims from their original locations. This predicts
a lower failure rate under attention or token pressure relative to a compressed directive audit.
The verbatim-restate protocol is a purely additive structural property with no interaction
surface against any proven criterion.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 11.

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
  found this through normal observation." Items that survive passive observation belong in
  the findings summary, not the echo. Apply Rule 1 as a filter at Step 1, not an
  annotation. The "Why passive observation missed this" field names the specific mechanism
  that made passive observation insufficient.

Rule 2 — Claim-only voice:
  State every finding as a direct claim. These constructs are prohibited everywhere:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Uncertainty is not a hedge — it is a rewrite. Delete the hedge. Extract the claim.
  State it directly.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

Commit before writing. Do not select or write a single surprise until you have completed
all pair inspections below and recorded the Declaration. This is a pre-write commitment,
not an optional review.

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
                 input. Test: "Does this mechanism state A's output is B's required input?"
                 Answer YES or NO.
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

  NGT + Check B:
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

== STEP 9 — CROSS-LAYER COHERENCE AUDIT ========================================

  [C-31 gate — runs after all per-pair inspections are complete, before word count]
  [C-32 verbatim-restate protocol — this audit is self-sufficient; no external lookup required]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural depth property: C-32 (verbatim-restate — the comparison executes from
      claims present in this section, not from memory or re-inspection of prior locations)
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance. Cross-layer incoherence is a template
      design failure — the institutional knowledge embedded in the template is internally
      contradictory.
    Scope: runs once, across the full inspection set. Not per-pair; post-manifest.

  VERBATIM-RESTATE PROTOCOL:
  For each mechanism pair that appears at more than one layer, restate the synthesis claim
  from each present layer verbatim in this audit section — named with its layer identifier —
  before issuing the COHERENT/INCOHERENT verdict. Do not paraphrase. Do not summarize.
  Restate the exact text of each Step 4 claim as written at its original layer.

  This protocol makes the audit self-sufficient. An author or reviewer executing the
  comparison does so from claims present in this section — no re-inspection of the manifest,
  canonical examples, or baseline entry required.

  For each mechanism pair present at two or more layers, run this audit block:

    Pair: [mechanism A + mechanism B]
      BASELINE LAYER (C-30) — synthesis claim
        (restate verbatim from ★BASELINE Step 4):
        "[paste the exact text of the Composability-claim from the ★BASELINE entry above]"

      ILLUSTRATION LAYER (C-29) — synthesis claim
        (restate verbatim from canonical taxonomy example Step 4):
        "[paste the exact text of the Composability-claim from the CANONICAL EXAMPLE above]"

      LIVE INSPECTION LAYER (C-27) — synthesis claim
        (restate verbatim from your pair inspection Step 4):
        "[paste the exact text of the Composability-claim you wrote in the manifest above]"

      Verdict: COHERENT / INCOHERENT
      (COHERENT: all present layers agree on archetype, directional relationship, and
       compatible mechanism framing.
       INCOHERENT: any present layer contradicts another on archetype or directional
       relationship — same pair, different structural conclusion.)

  If any pair returns INCOHERENT:
    STOP. Do not proceed to Step 10.
    Identify which layer's synthesis claim is the outlier.
    Rewrite the outlier claim to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Cross-layer coherence: CONFIRMED. All mechanism pairs present at multiple
    layers carry consistent synthesis claims. Verbatim restate executed from audit section
    — no external lookup required."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed 800 words.
  If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-02 — Single-axis: C-33 Explicit Gate-Order Independence

**Axis:** Coherence audit gate-order independence via explicit structural isolation — the
cross-layer coherence audit section has a structural constraint header that declares its
post-inspection positioning as an architectural property, and a manifest-completion entry gate
that blocks execution until all pair inspections and the Declaration are confirmed complete.
The isolation is explicit: it does not depend on the current NGT → Check B → CAT gate order
to be enforced — any reordering of the per-pair gates leaves the audit structurally last. No
verbatim-restate instruction (C-32 FAIL by design — the audit uses locator references, not
inline restatement). All other properties constant: standard gate order NGT → Check B → CAT;
vocabulary-specified CONSISTENCY GATE (C-26); Composability-claim field in every pair (C-27);
template-complete canonical examples (C-29 PASS); template-complete baseline (C-30 PASS).

**Hypothesis:** Gate-order independence is a distinct structural property from coherence audit
presence (C-31) and from verbatim-restate depth (C-32). A coherence audit whose post-inspection
positioning is declared architecturally — via header constraint and entry gate — cannot be
interleaved with per-pair gates regardless of how the preceding gate sequence is ordered. An
audit whose post-inspection positioning is implicit (emergent from current gate numbering)
could legitimately be moved between per-pair steps in a gate-reordered variation and still
satisfy C-31. Explicit structural isolation forecloses that failure mode. The entry gate is
the enforcement mechanism: if the manifest Declaration has not been written, the audit does
not execute. Structural isolation is independent of verbatim-restate depth — both axes
increase audit reliability through different mechanisms.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 11.

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
  found this through normal observation." Items that survive passive observation belong in
  the findings summary, not the echo. Apply Rule 1 as a filter at Step 1, not an
  annotation. The "Why passive observation missed this" field names the specific mechanism
  that made passive observation insufficient.

Rule 2 — Claim-only voice:
  State every finding as a direct claim. These constructs are prohibited everywhere:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Uncertainty is not a hedge — it is a rewrite. Delete the hedge. Extract the claim.
  State it directly.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

Commit before writing. Do not select or write a single surprise until you have completed
all pair inspections below and recorded the Declaration. This is a pre-write commitment,
not an optional review.

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
                 input. Test: "Does this mechanism state A's output is B's required input?"
                 Answer YES or NO.
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

  NGT + Check B:
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

== STEP 9 — POST-INSPECTION COHERENCE AUDIT =====================================

  [STRUCTURAL CONSTRAINT — C-33: This section is architecturally post-inspection. It runs
   only after all per-pair gate sequences in the Composability Manifest are complete. This
   is a template design property, not a convention of the current gate ordering: if the
   per-pair gates (NGT → Check B → CAT) are reordered, this audit still runs last. Any
   gate reordering that embeds this audit within a per-pair step violates this structural
   constraint.]

  [ENTRY GATE: Before executing any part of this audit, confirm:
   (a) All pair inspections in the Composability Manifest are complete — every pair has
       Step 1 through Step 4 populated.
   (b) The Declaration at the end of the Composability Manifest has been written.
   If either condition is not met: return to the Composability Manifest and satisfy it
   before entering this section. Partial inspection at the time of this audit is a
   structural violation regardless of gate ordering.]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural isolation property: C-33 (gate-order independence — post-inspection
      positioning is explicitly declared as an architectural constraint, not emergent
      from the current gate sequence; the ENTRY GATE enforces this regardless of how
      preceding per-pair gates are ordered)
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance. Cross-layer incoherence is a template
      design failure.
    Scope: runs once, across the full inspection set. Not per-pair; post-manifest.

  For each mechanism pair that appears at more than one layer:
    Identify the mechanism pair.
    Locate the synthesis claim at each present layer:
      BASELINE layer: the Composability-claim in the ★BASELINE entry (Step 4 above)
      ILLUSTRATION layer: the Composability-claim in the canonical taxonomy example (Step 4)
      LIVE INSPECTION layer: the Composability-claim in your pair inspection (Step 4)
    Compare: do all present layers agree on archetype, directional relationship, and
      mechanism framing?
      COHERENT: the claims at all present layers are mutually consistent.
      INCOHERENT: any layer contradicts another on archetype or directional relationship.

  If any pair is INCOHERENT:
    STOP. Do not proceed to Step 10.
    Rewrite the incoherent claim(s) to restore cross-layer agreement.
    Re-run this audit for the affected pair before proceeding.

  If all pairs are COHERENT:
    Write: "Post-inspection coherence: CONFIRMED. ENTRY GATE satisfied — all pair
    inspections complete before audit execution. All mechanism pairs present at multiple
    layers carry consistent synthesis claims."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed 800 words.
  If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: C-34 Pre-Inspection Domain Failure Mode Taxonomy

**Axis:** Pre-inspection failure mode taxonomy — a preamble block before the composability
manifest pair inspections names two cross-pair domain failure modes: "silent antagonism" and
"archetype drift." These are mechanism types that manifest across multiple pair inspections
and cannot be detected by per-archetype vocabulary checks alone. The preamble primes
prospective recognition before any pair inspection begins. No verbatim-restate (C-32 FAIL by
design), no explicit structural isolation declaration (C-33 FAIL by design). Standard coherence
audit section (C-31 PASS). All other properties constant: standard gate order NGT → Check B →
CAT; vocabulary-specified CONSISTENCY GATE (C-26); Composability-claim in every pair (C-27);
template-complete canonical examples (C-29 PASS); template-complete baseline (C-30 PASS).

**Hypothesis:** Pre-inspection failure mode taxonomy increases analytical depth on C-21
(mechanism field precision) and C-17 (composability rigor) without structural friction against
C-26 (per-archetype vocabulary specification) or C-29/C-30 (template completeness). The two
failure modes operate at the cross-pair scope — they require the author to inspect pairs in
relation to each other, not within a single archetype's constraint class. Pre-naming them
shifts discovery from post-inspection evaluation (the author notices a pattern only after
writing all pairs) to pre-inspection priming (the author enters with named patterns to look
for). C-34 is independent of C-26: C-26 prevents per-archetype vocabulary violations within
a single pair inspection; C-34 names structural patterns visible only across the full
inspection set.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 11.

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
  found this through normal observation." Items that survive passive observation belong in
  the findings summary, not the echo. Apply Rule 1 as a filter at Step 1, not an
  annotation. The "Why passive observation missed this" field names the specific mechanism
  that made passive observation insufficient.

Rule 2 — Claim-only voice:
  State every finding as a direct claim. These constructs are prohibited everywhere:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Uncertainty is not a hedge — it is a rewrite. Delete the hedge. Extract the claim.
  State it directly.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

Commit before writing. Do not select or write a single surprise until you have completed
all pair inspections below and recorded the Declaration. This is a pre-write commitment,
not an optional review.

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

DOMAIN FAILURE MODE TAXONOMY (read before beginning pair inspections):

Two cross-pair failure mechanisms are named here to prime prospective recognition. They
manifest across multiple pair inspections — not within a single archetype's constraint
class. Per-archetype vocabulary correctness (CONSISTENCY GATE) does not prevent them;
detecting them requires comparing mechanism statements across the full inspection set.

  1. Silent antagonism — Two mechanisms each satisfy their individual target criteria
     in isolation while degrading each other's enforcement effectiveness in compound
     configurations. Observable signature: each pair inspection passes all vocabulary
     checks and produces a valid mechanism statement, but reading mechanism statements
     across inspection pairs reveals that one mechanism's per-surprise enforcement
     narrows the operational scope available for another mechanism's enforcement when
     both run simultaneously on the same surprise. The antagonism is invisible within
     a single pair inspection; it appears only when the full manifest is compared
     horizontally across pairs.

  2. Archetype drift — A pair's archetype classification becomes inconsistent with its
     mechanism statement as new pairs are added to the inspection set. The mechanism
     statement for the pair may remain accurate and vocabulary-compliant (CONSISTENCY
     GATE passes), but the archetype assigned in an earlier classification round no
     longer accurately represents the structural relationship when the pair is viewed
     alongside the full manifest. Observable signature: a pair classified under one
     archetype whose mechanism, read in the context of the full set, reveals an
     ordering or dependency that the original archetype does not capture. Archetype
     drift invalidates cross-round comparison for the affected pair.

Enter all pair inspections below with these patterns named. Recognition is prospective,
not retrospective: you are primed to recognize silent antagonism and archetype drift
before any individual pair inspection begins.

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
                 input. Test: "Does this mechanism state A's output is B's required input?"
                 Answer YES or NO.
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

  NGT + Check B:
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
is template-complete (all four fields populated, including Composability-claim). Silent
antagonism and archetype drift reviewed across the full inspection set — no instances
detected. All mechanisms reinforce each other toward the single stranger-reader target.
No conflicts found. Writing may begin."

If any conflict found (including silent antagonism or archetype drift): resolve before
proceeding.

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

== STEP 9 — CROSS-LAYER COHERENCE AUDIT ========================================

  [C-31 gate — runs after all per-pair inspections are complete, before word count]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance. Cross-layer incoherence is a template
      design failure.
    Scope: runs once, across the full inspection set. Not per-pair; post-manifest.

  For each mechanism pair that appears at more than one layer:
    Identify the mechanism pair.
    Locate the synthesis claim at each present layer:
      BASELINE layer: the Composability-claim in the ★BASELINE entry (Step 4 above)
      ILLUSTRATION layer: the Composability-claim in the canonical taxonomy example (Step 4)
      LIVE INSPECTION layer: the Composability-claim in your pair inspection (Step 4)
    Compare: do all present layers agree on archetype, directional relationship, and
      mechanism framing?
      COHERENT: the claims at all present layers are mutually consistent.
      INCOHERENT: any layer contradicts another on archetype or directional relationship.

  If any pair is INCOHERENT:
    STOP. Do not proceed to Step 10.
    Rewrite the incoherent claim(s) to restore cross-layer agreement before proceeding.

  If all pairs are COHERENT:
    Write: "Cross-layer coherence: CONFIRMED."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed 800 words.
  If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: C-32 Verbatim-Restate + C-33 Explicit Gate-Order Independence

**Axes:** Verbatim-restate depth (C-32) combined with explicit post-inspection structural
isolation (C-33). Tests whether the two coherence audit structural properties are additive
without friction: the verbatim-restate protocol requires the author to populate the audit
section with claim text from all three layers; the explicit structural isolation requires the
audit section to be preceded by an entry gate that blocks execution until all manifest
inspections are complete. Both requirements apply to the same section, creating a double
structural demand on the coherence audit. No failure mode preamble (C-34 FAIL by design).
Standard gate order NGT → Check B → CAT; all proven criteria maintained.

**Hypothesis:** The verbatim-restate protocol (C-32) and the explicit post-inspection
structural constraint (C-33) operate on different properties of the same audit section —
content depth vs. execution ordering — and impose no competing demands. C-32 specifies how
the synthesis claims are represented in the audit section (verbatim, with layer identifiers);
C-33 specifies when the audit section executes (only after manifest Declaration is written).
These are structurally parallel constraints, not sequential or conflicting ones. The combined
section is the canonical reference for a coherence audit that is simultaneously self-sufficient
(C-32) and architecturally post-inspection (C-33). The combination predicts no degradation in
any proven criterion.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 11.

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
  found this through normal observation." Items that survive passive observation belong in
  the findings summary, not the echo. Apply Rule 1 as a filter at Step 1, not an
  annotation. The "Why passive observation missed this" field names the specific mechanism
  that made passive observation insufficient.

Rule 2 — Claim-only voice:
  State every finding as a direct claim. These constructs are prohibited everywhere:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Uncertainty is not a hedge — it is a rewrite. Delete the hedge. Extract the claim.
  State it directly.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

Commit before writing. Do not select or write a single surprise until you have completed
all pair inspections below and recorded the Declaration. This is a pre-write commitment,
not an optional review.

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
                 input. Test: "Does this mechanism state A's output is B's required input?"
                 Answer YES or NO.
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

  NGT + Check B:
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

== STEP 9 — POST-INSPECTION COHERENCE AUDIT (VERBATIM-RESTATE) =================

  [STRUCTURAL CONSTRAINT — C-33: This section is architecturally post-inspection. It runs
   only after all per-pair gate sequences in the Composability Manifest are complete. This
   is a template design property, not a convention of the current gate ordering: if the
   per-pair gates (NGT → Check B → CAT) are reordered, this audit still runs last. Any
   reordering that embeds this audit within a per-pair step violates this constraint.]

  [ENTRY GATE: Before executing any part of this audit, confirm:
   (a) All pair inspections in the Composability Manifest are complete — every pair has
       Step 1 through Step 4 populated.
   (b) The Declaration at the end of the Composability Manifest has been written.
   If either condition is not met: return to the Composability Manifest and satisfy it
   before entering this section. Partial inspection at the time of this audit is a
   structural violation regardless of gate ordering.]

  Gate design rationale:
    Criteria enforced: C-31 (cross-layer synthesis claim coherence) + C-32 (verbatim-
      restate depth) + C-33 (gate-order independence by explicit structural isolation)
    C-32 property: the verbatim-restate protocol makes this audit self-sufficient — the
      comparison executes from claims present in this section, no re-inspection required
    C-33 property: the STRUCTURAL CONSTRAINT header and ENTRY GATE declare post-inspection
      positioning architecturally — not as a convention of the current gate ordering
    Primary motivation: three-layer synthesis claim coherence; cross-layer incoherence is
      a template design failure.
    Scope: runs once, across the full inspection set. Not per-pair; post-manifest.

  VERBATIM-RESTATE PROTOCOL:
  For each mechanism pair that appears at more than one layer, restate the synthesis claim
  from each present layer verbatim in this audit section — named with its layer identifier —
  before issuing the COHERENT/INCOHERENT verdict. Do not paraphrase. Do not summarize.
  Restate the exact text of each Step 4 claim as written at its original layer.

  This protocol makes the audit self-sufficient. An author or reviewer executing the
  comparison does so from claims present in this section — no re-inspection of the manifest,
  canonical examples, or baseline entry required.

  For each mechanism pair present at two or more layers, run this audit block:

    Pair: [mechanism A + mechanism B]
      BASELINE LAYER (C-30) — synthesis claim
        (restate verbatim from ★BASELINE Step 4):
        "[paste the exact text of the Composability-claim from the ★BASELINE entry above]"

      ILLUSTRATION LAYER (C-29) — synthesis claim
        (restate verbatim from canonical taxonomy example Step 4):
        "[paste the exact text of the Composability-claim from the CANONICAL EXAMPLE above]"

      LIVE INSPECTION LAYER (C-27) — synthesis claim
        (restate verbatim from your pair inspection Step 4):
        "[paste the exact text of the Composability-claim you wrote in the manifest above]"

      Verdict: COHERENT / INCOHERENT
      (COHERENT: all present layers agree on archetype, directional relationship, and
       compatible mechanism framing.
       INCOHERENT: any present layer contradicts another on archetype or directional
       relationship — same pair, different structural conclusion.)

  If any pair returns INCOHERENT:
    STOP. Do not proceed to Step 10.
    Identify which layer's synthesis claim is the outlier.
    Rewrite the outlier claim to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Post-inspection coherence: CONFIRMED. ENTRY GATE satisfied — all pair
    inspections complete before audit execution. Verbatim restate executed — audit is
    self-sufficient. All mechanism pairs present at multiple layers carry consistent
    synthesis claims."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed 800 words.
  If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: C-32 + C-33 + C-34 (Full Three-Axis)

**Axes:** Verbatim-restate depth (C-32) + explicit gate-order independence (C-33) +
pre-inspection failure mode taxonomy (C-34). All three new aspirational criteria targeted
simultaneously. Tests whether the three axes are fully additive: C-34's preamble block
operates at the manifest scope (pre-pair-inspection), C-32 and C-33 operate at the audit
scope (post-manifest). They modify different sections and impose no overlapping structural
demands. The combination is the reference implementation for a variation that carries all
three properties.

**Hypothesis:** C-34's preamble block and C-32/C-33's coherence audit modifications are
structurally parallel — they are not in the same section, do not share execution points, and
impose no competing constraints. C-34 adds prospective pattern recognition before the manifest;
C-32 adds self-sufficiency to the post-manifest audit; C-33 adds architectural post-inspection
isolation to the same audit section. The combination is predicted to pass all 34 criteria in
v14 (C-31 PASS completing second confirmation for proven promotion; C-32, C-33, C-34 PASS as
aspirational targets). All proven criteria maintained throughout.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 11.

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
  found this through normal observation." Items that survive passive observation belong in
  the findings summary, not the echo. Apply Rule 1 as a filter at Step 1, not an
  annotation. The "Why passive observation missed this" field names the specific mechanism
  that made passive observation insufficient.

Rule 2 — Claim-only voice:
  State every finding as a direct claim. These constructs are prohibited everywhere:
    may suggest / appears to indicate / seems like / could mean /
    it is possible that / might be / could indicate / it seems
  Uncertainty is not a hedge — it is a rewrite. Delete the hedge. Extract the claim.
  State it directly.

== PRE-WRITE: COMPOSABILITY MANIFEST ============================================

Commit before writing. Do not select or write a single surprise until you have completed
all pair inspections below and recorded the Declaration. This is a pre-write commitment,
not an optional review.

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

DOMAIN FAILURE MODE TAXONOMY (read before beginning pair inspections):

Two cross-pair failure mechanisms are named here to prime prospective recognition. They
manifest across multiple pair inspections — not within a single archetype's constraint
class. Per-archetype vocabulary correctness (CONSISTENCY GATE) does not prevent them;
detecting them requires comparing mechanism statements across the full inspection set.

  1. Silent antagonism — Two mechanisms each satisfy their individual target criteria
     in isolation while degrading each other's enforcement effectiveness in compound
     configurations. Observable signature: each pair inspection passes all vocabulary
     checks and produces a valid mechanism statement, but reading mechanism statements
     across inspection pairs reveals that one mechanism's per-surprise enforcement
     narrows the operational scope available for another mechanism's enforcement when
     both run simultaneously on the same surprise. The antagonism is invisible within
     a single pair inspection; it appears only when the full manifest is compared
     horizontally across pairs.

  2. Archetype drift — A pair's archetype classification becomes inconsistent with its
     mechanism statement as new pairs are added to the inspection set. The mechanism
     statement for the pair may remain accurate and vocabulary-compliant (CONSISTENCY
     GATE passes), but the archetype assigned in an earlier classification round no
     longer accurately represents the structural relationship when the pair is viewed
     alongside the full manifest. Observable signature: a pair classified under one
     archetype whose mechanism, read in the context of the full set, reveals an
     ordering or dependency that the original archetype does not capture. Archetype
     drift invalidates cross-round comparison for the affected pair.

Enter all pair inspections below with these patterns named. Recognition is prospective,
not retrospective: you are primed to recognize silent antagonism and archetype drift
before any individual pair inspection begins.

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
                 input. Test: "Does this mechanism state A's output is B's required input?"
                 Answer YES or NO.
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

  NGT + Check B:
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
is template-complete (all four fields populated, including Composability-claim). Silent
antagonism and archetype drift reviewed across the full inspection set — no instances
detected. All mechanisms reinforce each other toward the single stranger-reader target.
No conflicts found. Writing may begin."

If any conflict found (including silent antagonism or archetype drift): resolve before
proceeding.

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

== STEP 9 — POST-INSPECTION COHERENCE AUDIT (VERBATIM-RESTATE) =================

  [STRUCTURAL CONSTRAINT — C-33: This section is architecturally post-inspection. It runs
   only after all per-pair gate sequences in the Composability Manifest are complete. This
   is a template design property, not a convention of the current gate ordering: if the
   per-pair gates (NGT → Check B → CAT) are reordered, this audit still runs last. Any
   reordering that embeds this audit within a per-pair step violates this constraint.]

  [ENTRY GATE: Before executing any part of this audit, confirm:
   (a) All pair inspections in the Composability Manifest are complete — every pair has
       Step 1 through Step 4 populated.
   (b) The Declaration at the end of the Composability Manifest has been written.
   If either condition is not met: return to the Composability Manifest and satisfy it
   before entering this section. Partial inspection at the time of this audit is a
   structural violation regardless of gate ordering.]

  Gate design rationale:
    Criteria enforced: C-31 (cross-layer synthesis claim coherence) + C-32 (verbatim-
      restate depth) + C-33 (gate-order independence by explicit structural isolation)
    C-32 property: verbatim-restate protocol makes this audit self-sufficient — comparison
      executes from claims present in this section, no re-inspection required
    C-33 property: STRUCTURAL CONSTRAINT header and ENTRY GATE declare post-inspection
      positioning architecturally — independent of how preceding gates are ordered
    C-34 property: domain failure mode taxonomy (silent antagonism, archetype drift) was
      named in the pre-inspection preamble; any instances detected during pair inspection
      must be resolved before the Declaration is written — they do not enter this audit
    Primary motivation: three-layer synthesis claim coherence; cross-layer incoherence is
      a template design failure.
    Scope: runs once, across the full inspection set. Not per-pair; post-manifest.

  VERBATIM-RESTATE PROTOCOL:
  For each mechanism pair that appears at more than one layer, restate the synthesis claim
  from each present layer verbatim in this audit section — named with its layer identifier —
  before issuing the COHERENT/INCOHERENT verdict. Do not paraphrase. Do not summarize.
  Restate the exact text of each Step 4 claim as written at its original layer.

  This protocol makes the audit self-sufficient. An author or reviewer executing the
  comparison does so from claims present in this section — no re-inspection of the manifest,
  canonical examples, or baseline entry required.

  For each mechanism pair present at two or more layers, run this audit block:

    Pair: [mechanism A + mechanism B]
      BASELINE LAYER (C-30) — synthesis claim
        (restate verbatim from ★BASELINE Step 4):
        "[paste the exact text of the Composability-claim from the ★BASELINE entry above]"

      ILLUSTRATION LAYER (C-29) — synthesis claim
        (restate verbatim from canonical taxonomy example Step 4):
        "[paste the exact text of the Composability-claim from the CANONICAL EXAMPLE above]"

      LIVE INSPECTION LAYER (C-27) — synthesis claim
        (restate verbatim from your pair inspection Step 4):
        "[paste the exact text of the Composability-claim you wrote in the manifest above]"

      Verdict: COHERENT / INCOHERENT
      (COHERENT: all present layers agree on archetype, directional relationship, and
       compatible mechanism framing.
       INCOHERENT: any present layer contradicts another on archetype or directional
       relationship — same pair, different structural conclusion.)

  If any pair returns INCOHERENT:
    STOP. Do not proceed to Step 10.
    Identify which layer's synthesis claim is the outlier.
    Rewrite the outlier claim to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Post-inspection coherence: CONFIRMED. ENTRY GATE satisfied — all pair
    inspections and Declaration complete before audit execution. Verbatim restate
    executed — audit is self-sufficient. Domain failure modes (silent antagonism,
    archetype drift) resolved at manifest stage — none propagated to this audit.
    All mechanism pairs present at multiple layers carry consistent synthesis claims."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed 800 words.
  If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## Round 15 Scoring Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-31 | PASS | PASS | PASS | PASS | PASS | Second confirmation → Proven in v15 |
| C-32 | PASS | FAIL | FAIL | PASS | PASS | First targeted round (3 of 5) |
| C-33 | FAIL | PASS | FAIL | PASS | PASS | First targeted round (3 of 5) |
| C-34 | FAIL | FAIL | PASS | FAIL | PASS | First targeted round (2 of 5) |
| Proven (C-10–C-30) | PASS | PASS | PASS | PASS | PASS | All maintained |
| Score | 100 | 100 | 100 | 100 | 100 | Ceiling by proven set alone |

**C-31 promotion condition met**: All five variations PASS C-31. Combined with R14 first
confirmation, the two-round threshold is satisfied. C-31 promotes to Proven in v15.

**C-32 confirmation status after R15**: First confirmed round if all three targeted variations
(V-01, V-04, V-05) pass. Second confirmation required in R16 for proven promotion.

**C-33 confirmation status after R15**: First confirmed round if all three targeted variations
(V-02, V-04, V-05) pass. Second confirmation required in R16 for proven promotion.

**C-34 confirmation status after R15**: First confirmed round if both targeted variations
(V-03, V-05) pass. A second round with broader uniform coverage required for proven promotion.

**Predicted R16 direction**: If C-32 and C-33 each confirm uniformly (all five variations in
R16), both promote to Proven simultaneously — a potential two-criterion promotion matching the
C-26/C-27/C-28/C-30 pattern from v14. C-34's narrower initial coverage (2 of 5) may require
an additional intermediate round.
