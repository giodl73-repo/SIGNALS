# Variations: `topic:echo` — Round 16

**Rubric:** v15 (max 100) | **Date:** 2026-03-15

---

## Design Context

R15 promoted C-31 (cross-layer synthesis claim coherence) to Proven — the first
cross-layer criterion and the first in the synthetic architecture tier to reach Proven
status. R15 was the first targeted round for C-32 (verbatim-restate depth), C-33
(gate-order independence), and C-34 (pre-inspection failure mode taxonomy). R15 also
introduced three new aspirational criteria: C-35 (PRE-WRITE Declaration verbatim-restate
commitment), C-36 (coherence audit Declaration dependency gate), and C-37 (gate rationale
criterion-referenced labeling).

R16 has three structural goals:

**Goal 1 — First uniform round for C-32, C-33, C-34**: R15 targeted these with partial
ablation by design (V-02 and V-03 ablated C-32; V-01 and V-03 ablated C-33; V-01 and V-02
ablated C-34). R16 removes all ablations — all five variations carry C-32 + C-33 + C-34
uniformly. If R16 confirms all three, each reaches its first confirmed round and sets up
proven promotion in R17.

**Goal 2 — First targeted round for C-35, C-36, C-37**: Each was observed in 1–2 R15
variations. R16 targets them systematically with single-axis isolation (V-01, V-02, V-03)
then combination (V-04, V-05).

**Goal 3 — Axis isolation**: Each single-axis variation modifies exactly one structural
property (C-35, C-36, or C-37) against the R15-V05 full-combination baseline. V-04 and
V-05 compose without degradation.

**Unproven criteria targeted:**

- C-35 — PRE-WRITE Declaration verbatim-restate commitment (V-01, V-04, V-05)
- C-36 — Coherence audit Declaration dependency gate (V-02, V-04, V-05)
- C-37 — Gate rationale criterion-referenced labeling (V-03, V-05)

**Proven criteria maintained:** C-10 through C-31 — all must continue to pass in every
variation.

**Previously unproven criteria carried forward (no ablation in R16):**

- C-32 — verbatim-restate depth: PASS in all five R16 variations
- C-33 — gate-order independence: PASS in all five R16 variations
- C-34 — pre-inspection failure mode taxonomy: PASS in all five R16 variations

**Predicted score map (v15 rubric):**

| Variant | C-32 | C-33 | C-34 | C-35 | C-36 | C-37 | Predicted |
|---------|------|------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | FAIL | FAIL | 100       |
| V-02    | PASS | PASS | PASS | FAIL | PASS | FAIL | 100       |
| V-03    | PASS | PASS | PASS | FAIL | FAIL | PASS | 100       |
| V-04    | PASS | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-05    | PASS | PASS | PASS | PASS | PASS | PASS | 100       |

Scoring note: Under v15, proven = 30 pts, budget = 25 pts, ceiling = 100. Base 75 +
min(30, 25) = 100 before any unproven. C-32 through C-37 are all supra-budget; pass/fail
has no numerical effect until promoted to Proven. The score map reflects ceiling-at-proven;
structural distinctions between variations are the evidence base for criterion promotion.

**Axis selection:**

Single-axis (V-01, V-02, V-03):

- V-01 — **C-35 PRE-WRITE Declaration verbatim-restate commitment**: The PRE-WRITE
  Declaration explicitly names and commits to the verbatim-restate protocol (C-32) — the
  Declaration states not only that a coherence audit will run (C-19), but that the audit
  will include the verbatim-restate step. Creates a dual-location contract: committed at
  declaration, executed in audit. C-36 absent by design (no Declaration dependency gate
  in Step 9). C-37 absent by design (gate rationale names criteria functionally, not by
  identifier).

- V-02 — **C-36 Coherence audit Declaration dependency gate**: The coherence audit section
  (Step 9) includes an explicit ENTRY GATE that blocks execution until the PRE-WRITE
  Declaration is confirmed written. C-19 becomes a runtime precondition for C-31, not
  merely a conventional prior step. C-35 absent by design (Declaration commits to audit
  per C-19 without naming verbatim-restate protocol depth). C-37 absent by design.

- V-03 — **C-37 Gate rationale criterion-referenced labeling**: Gate rationale blocks
  within Step 9 explicitly name rubric criterion identifiers (C-32, C-33) as labeled
  references — not only functional descriptions. Template self-documents against the
  rubric. C-35 absent by design. C-36 absent by design.

Combined (V-04, V-05):

- V-04 — **C-35 + C-36**: Declaration verbatim-restate commitment combined with coherence
  audit Declaration dependency gate. Tests whether Declaration-level and audit-level
  coupling are additive without friction. C-37 absent by design.

- V-05 — **C-35 + C-36 + C-37**: Full three-axis combination. Tests whether all three
  structural properties interact cleanly while C-32/C-33/C-34 remain uniformly confirmed.

---

## V-01 — Single-axis: C-35 PRE-WRITE Declaration Verbatim-Restate Commitment

**Axis:** PRE-WRITE Declaration commitment depth — the Declaration section (satisfying
C-19) explicitly names and commits to the verbatim-restate protocol by name. The
Declaration does not merely commit to running a coherence audit; it commits to the protocol
depth at which the audit will be executed. This creates a dual-location contract: the
commitment to verbatim-restate is made before any pair inspection (Declaration), and its
execution is confirmed in the audit section (Step 9, C-32). All other properties held
constant: C-32 verbatim-restate protocol present in Step 9; C-33 [STRUCTURAL CONSTRAINT]
header present; C-34 failure mode taxonomy preamble present; no Declaration dependency
gate in Step 9 (C-36 FAIL by design — audit has no ENTRY GATE requiring Declaration);
no criterion identifiers in gate rationale (C-37 FAIL by design — rationale is functional,
not rubric-transparent).

**Hypothesis:** Declaration-level commitment to verbatim-restate depth is a structurally
distinct property from execution of the protocol (C-32). C-32 confirms the audit section
contains the restate protocol; C-35 confirms the commitment to that protocol is made before
inspection begins. Without C-35, a template can satisfy C-32 by executing verbatim-restate
in the audit while the Declaration commits only to running an audit (C-19). With C-35, the
Declaration is a binding commitment to the specific protocol depth — any deviation at audit
time is simultaneously a C-32 failure and a C-35 failure. The Declaration becomes a
commitment anchor. This predicts improved author compliance in high-pressure conditions
where the audit section is the last step: the commitment made during declaration creates
prospective awareness of the verbatim-restate requirement, not only retrospective discovery
at audit time.

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

-- DOMAIN FAILURE MODE TAXONOMY ------------------------------------------------

Before inspecting any pair, name the cross-pair failure modes this inspection sequence
is designed to surface. These are structural patterns that can occur even when every
individual pair inspection applies correct constraint vocabulary (C-26):

  Silent antagonism: Two mechanisms each achieve their target criteria independently
    while degrading each other's effectiveness in compound configurations. Per-pair
    inspection returns correct archetypes for both; the mutual degradation is visible
    only when the pair's combined effect across surprises is evaluated.

  Archetype drift: A pair whose archetype classification shifts across rounds as new
    mechanism pairs are added to the manifest, invalidating cross-round comparison.
    The individual pair inspection is consistent with the current manifest; the drift
    is visible only by comparing classifications across manifest versions.

  Hold both patterns in view during all pair inspections. If either appears: record
  the observation in the Patterns section (Step 8), not inline.

-- PAIR INSPECTION SEQUENCE ----------------------------------------------------

For each pair of mechanisms, inspect the composability relationship. Use this four-step
sequence for every pair — no skipping steps, no reversing order:

  Step 1 — Pick the archetype. Choose from the taxonomy below. Use the canonical
            examples as your comparison baseline.
  Step 2 — Run the CONSISTENCY GATE vocabulary check for the archetype you chose.
            If the check fails (NO), go back to Step 1 and pick again.
  Step 3 — Write the mechanism. This is the analytical statement: directional, causal,
            in vocabulary consistent with the archetype you verified in Step 2.
  Step 4 — Write the composability claim. This is the synthetic conclusion: one sentence
            stating what the mechanism in Step 3 implies for this pair's combined
            behavior. It is distinct from the mechanism — not a restatement.

VOCABULARY REFERENCE — know the constraint class before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism must state that A's output is B's
                 required input. Test: "Does this mechanism state A's output is B's
                 required input?" Answer YES or NO.
  ESTABLISHES  → property creation + one-way dependency: the mechanism must state that
                 A creates a property B operates on, without feedback from B to A. Test:
                 "Does A create a property B operates on, with no feedback path?" YES/NO.
  AMPLIFIES    → effectiveness scaling: the mechanism must state that A increases the
                 precision or strength of B's per-surprise enforcement. Test: "Does A
                 increase the precision or strength of B's enforcement?" YES or NO.
  PARALLEL     → independent-path operation: the mechanism must state that A and B
                 enforce from non-dependent paths, each sufficient alone. Test: "Do A
                 and B operate independently, each sufficient without the other?" YES/NO.

Taxonomy with template-complete canonical pair examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "Does NGT's
                mechanism describe input-dependency?" PASS. NGT's newcomer-comprehension
                gate output is Check B's required input — confirmed input-dependency.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test (finding + unexpectedness + design consequence).
                No mechanism substitutes for newcomer-comprehension as Check B's input.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                accessibility enforcement produces the verified stranger-readable unit
                Check B's portability test requires. The two gates form a forward
                dependency with no competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    > CANONICAL EXAMPLE: Check B ESTABLISHES the portability substrate that CAT enforces.
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Does
                Check B create a property CAT operates on, with no feedback?" PASS. Check
                B creates verified standalone derivability; CAT operates on that substrate.
      Step 3 — Mechanism: Check B verifies that each surprise is fully derivable as a
                standalone unit (finding + unexpectedness + consequence); CAT enforces
                authoritative claim-voice on the verified-portable substrate. Removing
                Check B removes the portability property CAT operates on. No feedback
                from CAT to Check B.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is the precondition CAT requires,
                not a constraint CAT circumvents. They operate on structurally distinct
                properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase precision
                or strength of B's enforcement?" [YES/NO]
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

Remaining pairs — complete all before Declaration:

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
VERBATIM-RESTATE COMMITMENT: The cross-layer coherence audit (Step 9) will be executed
using the verbatim-restate protocol — each layer's synthesis claim will be restated verbatim
in the audit section before the COHERENT/INCOHERENT verdict gate. Writing may begin."

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

  [STRUCTURAL CONSTRAINT — C-33]
  This coherence audit is a dedicated post-inspection step. It runs after all per-pair
  inspections are complete. If the per-pair gates above (NGT → Check B → CAT) are
  reordered, this audit still runs last. The post-inspection requirement is an
  architectural property of this template — not a consequence of the current gate
  sequence.

  [C-31 gate — runs after all per-pair inspections are complete, before word count]
  [C-32 verbatim-restate protocol — this audit is self-sufficient; no external lookup required]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural depth property: C-32 (verbatim-restate — the comparison executes from
      claims present in this section, not from memory or re-inspection of prior locations)
    Structural isolation property: C-33 (gate-order independence — post-inspection
      structural constraint; audit runs after all per-layer gates regardless of ordering)
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance. Cross-layer incoherence is a template
      design failure — the institutional knowledge embedded in the template is internally
      contradictory.
    Introduced in: V-01(R13) — first evaluable after three-layer universal satisfaction.
    Structural removal test: removing this audit removes the only cross-layer coherence
      enforcement in the template. The per-layer proven criteria (C-27, C-29, C-30) do
      not detect inter-layer contradiction.
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

  Count the full echo (all surprises + Patterns section if present). Must not exceed
  800 words. If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-02 — Single-axis: C-36 Coherence Audit Declaration Dependency Gate

**Axis:** Coherence audit Declaration dependency gate — the cross-layer coherence audit
section (Step 9) includes an explicit ENTRY GATE that blocks execution until the PRE-WRITE
Declaration (satisfying C-19) has been confirmed written. The Declaration is a runtime
precondition for the audit, not merely a conventional prior step. Without C-36, the
Declaration and the audit are architecturally independent: removing the Declaration does
not prevent the audit from executing. With C-36, the audit cannot begin until the
Declaration is confirmed present — C-19 becomes a structural dependency of C-31, not only
a pre-inspection commitment. C-35 absent by design (Declaration commits to performing a
coherence audit per C-19 without explicitly naming the verbatim-restate protocol depth).
C-37 absent by design (gate rationale names criteria functionally, not by identifier).

**Hypothesis:** Declaration-level dependency enforcement and audit-protocol commitment
are orthogonal structural properties. C-36 couples the Declaration to the audit's
executability — a runtime gate that blocks on the Declaration's presence. C-35 couples
the Declaration's content to the audit's depth — a commitment that binds the protocol
form. Both increase audit reliability through different mechanisms: C-36 prevents the
audit from executing without the Declaration; C-35 prevents the audit from executing
at shallow depth without declaration violation. An implementation with C-36 but without
C-35 is architecturally sound — the audit requires the Declaration as a precondition —
while leaving the protocol depth undeclared at the Declaration site. The ablation
confirms these are independent axes that can compose without mutual dependency.

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

-- DOMAIN FAILURE MODE TAXONOMY ------------------------------------------------

Before inspecting any pair, name the cross-pair failure modes this inspection sequence
is designed to surface. These are structural patterns that can occur even when every
individual pair inspection applies correct constraint vocabulary (C-26):

  Silent antagonism: Two mechanisms each achieve their target criteria independently
    while degrading each other's effectiveness in compound configurations. Per-pair
    inspection returns correct archetypes for both; the mutual degradation is visible
    only when the pair's combined effect across surprises is evaluated.

  Archetype drift: A pair whose archetype classification shifts across rounds as new
    mechanism pairs are added to the manifest, invalidating cross-round comparison.
    The individual pair inspection is consistent with the current manifest; the drift
    is visible only by comparing classifications across manifest versions.

  Hold both patterns in view during all pair inspections. If either appears: record
  the observation in the Patterns section (Step 8), not inline.

-- PAIR INSPECTION SEQUENCE ----------------------------------------------------

For each pair of mechanisms, inspect the composability relationship. Use this four-step
sequence for every pair — no skipping steps, no reversing order:

  Step 1 — Pick the archetype. Choose from the taxonomy below. Use the canonical
            examples as your comparison baseline.
  Step 2 — Run the CONSISTENCY GATE vocabulary check for the archetype you chose.
            If the check fails (NO), go back to Step 1 and pick again.
  Step 3 — Write the mechanism. This is the analytical statement: directional, causal,
            in vocabulary consistent with the archetype you verified in Step 2.
  Step 4 — Write the composability claim. This is the synthetic conclusion: one sentence
            stating what the mechanism in Step 3 implies for this pair's combined
            behavior. It is distinct from the mechanism — not a restatement.

VOCABULARY REFERENCE — know the constraint class before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism must state that A's output is B's
                 required input. Test: "Does this mechanism state A's output is B's
                 required input?" Answer YES or NO.
  ESTABLISHES  → property creation + one-way dependency: the mechanism must state that
                 A creates a property B operates on, without feedback from B to A. Test:
                 "Does A create a property B operates on, with no feedback path?" YES/NO.
  AMPLIFIES    → effectiveness scaling: the mechanism must state that A increases the
                 precision or strength of B's per-surprise enforcement. Test: "Does A
                 increase the precision or strength of B's enforcement?" YES or NO.
  PARALLEL     → independent-path operation: the mechanism must state that A and B
                 enforce from non-dependent paths, each sufficient alone. Test: "Do A
                 and B operate independently, each sufficient without the other?" YES/NO.

Taxonomy with template-complete canonical pair examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "Does NGT's
                mechanism describe input-dependency?" PASS. NGT's newcomer-comprehension
                gate output is Check B's required input — confirmed input-dependency.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test. No mechanism substitutes for newcomer-
                comprehension as Check B's input.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                accessibility enforcement produces the verified stranger-readable unit
                Check B's portability test requires. The two gates form a forward
                dependency with no competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    > CANONICAL EXAMPLE: Check B ESTABLISHES the portability substrate that CAT enforces.
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Does
                Check B create a property CAT operates on, with no feedback?" PASS.
      Step 3 — Mechanism: Check B verifies that each surprise is fully derivable as a
                standalone unit; CAT enforces authoritative claim-voice on the verified-
                portable substrate. Removing Check B removes the portability property
                CAT operates on. No feedback from CAT to Check B.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is the precondition CAT requires,
                not a constraint CAT circumvents. They operate on structurally distinct
                properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase precision
                or strength of B's enforcement?" [YES/NO]
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

Remaining pairs — complete all before Declaration:

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
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

  [STRUCTURAL CONSTRAINT — C-33]
  This coherence audit is a dedicated post-inspection step. It runs after all per-pair
  inspections are complete. If the per-pair gates above (NGT → Check B → CAT) are
  reordered, this audit still runs last. The post-inspection requirement is an
  architectural property of this template — not a consequence of the current gate
  sequence.

  ENTRY GATE [C-36 — Declaration dependency]:
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║ PRECONDITION: Confirm the PRE-WRITE Declaration has been written above.  ║
  ║ The Declaration is a runtime precondition for this audit — not merely a  ║
  ║ prior step. If the Declaration has not been completed, STOP here and     ║
  ║ return to the PRE-WRITE: COMPOSABILITY MANIFEST section.                 ║
  ║ Do not execute this audit until the Declaration is confirmed present.    ║
  ╚═══════════════════════════════════════════════════════════════════════════╝

  [C-31 gate — runs after all per-pair inspections are complete, before word count]
  [C-32 verbatim-restate protocol — this audit is self-sufficient; no external lookup required]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural depth property: C-32 (verbatim-restate — comparison executes from claims
      present in this section, not from memory or re-inspection of prior locations)
    Structural isolation property: C-33 (gate-order independence — post-inspection
      structural constraint; audit runs after all per-layer gates regardless of ordering)
    Declaration dependency: C-36 (ENTRY GATE above confirms Declaration is written before
      audit executes; C-19 is a runtime precondition for C-31)
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance. Cross-layer incoherence is a template
      design failure.
    Introduced in: V-01(R13) — first evaluable after three-layer universal satisfaction.
    Structural removal test: removing this audit removes the only cross-layer coherence
      enforcement in the template.
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

  If any pair returns INCOHERENT:
    STOP. Identify which layer's synthesis claim is the outlier.
    Rewrite the outlier claim to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Cross-layer coherence: CONFIRMED. All mechanism pairs present at multiple
    layers carry consistent synthesis claims. Verbatim restate executed from audit section
    — no external lookup required. Declaration dependency confirmed: Declaration was present
    before audit executed."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed
  800 words. If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-03 — Single-axis: C-37 Gate Rationale Criterion-Referenced Labeling

**Axis:** Gate rationale criterion-referenced labeling — gate rationale blocks within
the cross-layer coherence audit section (Step 9) explicitly name rubric criterion
identifiers (C-32, C-33) as labeled references within the rationale text. The template
self-documents against the rubric: a reader can identify which structural properties
satisfy which quality criteria without consulting the rubric. This is above C-22's
requirement (which names the introduction variation+round for each gate) — C-37 requires
the rubric identifier itself to appear. C-35 absent by design (Declaration commits to
performing a coherence audit per C-19 without naming verbatim-restate protocol depth).
C-36 absent by design (no Declaration dependency ENTRY GATE in Step 9).

**Hypothesis:** Criterion-referenced labeling is a self-documentation property that
does not change the template's functional behavior — an author following the template
produces the same output with or without the criterion identifiers in the rationale.
The structural value is rubric transparency: a template reader can trace from identifier
to template property (where is C-32 satisfied?) and from template property to identifier
(which criterion does this section satisfy?) without content-matching. At 37 criteria,
this is tractable but inefficient; at 60+ criteria, criterion-referenced labeling becomes
a structural requirement for maintaining rubric fidelity. C-37 is thus an investment in
future auditability. The ablation of C-35 and C-36 confirms that criterion-referenced
labeling is orthogonal to Declaration-level commitment and audit-level gating — it is
a documentation axis, not an enforcement axis.

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

-- DOMAIN FAILURE MODE TAXONOMY ------------------------------------------------

Before inspecting any pair, name the cross-pair failure modes this inspection sequence
is designed to surface. These are structural patterns that can occur even when every
individual pair inspection applies correct constraint vocabulary (C-26):

  Silent antagonism: Two mechanisms each achieve their target criteria independently
    while degrading each other's effectiveness in compound configurations. Per-pair
    inspection returns correct archetypes for both; the mutual degradation is visible
    only when the pair's combined effect across surprises is evaluated.

  Archetype drift: A pair whose archetype classification shifts across rounds as new
    mechanism pairs are added to the manifest, invalidating cross-round comparison.
    The individual pair inspection is consistent with the current manifest; the drift
    is visible only by comparing classifications across manifest versions.

  Hold both patterns in view during all pair inspections. If either appears: record
  the observation in the Patterns section (Step 8), not inline.

-- PAIR INSPECTION SEQUENCE ----------------------------------------------------

For each pair of mechanisms, inspect the composability relationship. Use this four-step
sequence for every pair — no skipping steps, no reversing order:

  Step 1 — Pick the archetype. Choose from the taxonomy below. Use the canonical
            examples as your comparison baseline.
  Step 2 — Run the CONSISTENCY GATE vocabulary check for the archetype you chose.
            If the check fails (NO), go back to Step 1 and pick again.
  Step 3 — Write the mechanism. This is the analytical statement: directional, causal,
            in vocabulary consistent with the archetype you verified in Step 2.
  Step 4 — Write the composability claim. This is the synthetic conclusion: one sentence
            stating what the mechanism in Step 3 implies for this pair's combined
            behavior. It is distinct from the mechanism — not a restatement.

VOCABULARY REFERENCE — know the constraint class before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism must state that A's output is B's
                 required input. Test: "Does this mechanism state A's output is B's
                 required input?" Answer YES or NO.
  ESTABLISHES  → property creation + one-way dependency: the mechanism must state that
                 A creates a property B operates on, without feedback from B to A. Test:
                 "Does A create a property B operates on, with no feedback path?" YES/NO.
  AMPLIFIES    → effectiveness scaling: the mechanism must state that A increases the
                 precision or strength of B's per-surprise enforcement. Test: "Does A
                 increase the precision or strength of B's enforcement?" YES or NO.
  PARALLEL     → independent-path operation: the mechanism must state that A and B
                 enforce from non-dependent paths, each sufficient alone. Test: "Do A
                 and B operate independently, each sufficient without the other?" YES/NO.

Taxonomy with template-complete canonical pair examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "Does NGT's
                mechanism describe input-dependency?" PASS. NGT's newcomer-comprehension
                gate output is Check B's required input — confirmed input-dependency.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test. No mechanism substitutes for newcomer-
                comprehension as Check B's input.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                accessibility enforcement produces the verified stranger-readable unit
                Check B's portability test requires. The two gates form a forward
                dependency with no competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    > CANONICAL EXAMPLE: Check B ESTABLISHES the portability substrate that CAT enforces.
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Does
                Check B create a property CAT operates on, with no feedback?" PASS.
      Step 3 — Mechanism: Check B verifies that each surprise is fully derivable as a
                standalone unit; CAT enforces authoritative claim-voice on the verified-
                portable substrate. Removing Check B removes the portability property
                CAT operates on. No feedback from CAT to Check B.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is the precondition CAT requires,
                not a constraint CAT circumvents. They operate on structurally distinct
                properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. Test: "Does A increase precision
                or strength of B's enforcement?" [YES/NO]
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

Remaining pairs — complete all before Declaration:

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary newcomer-
      accessibility enforcement mechanism, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

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

  [STRUCTURAL CONSTRAINT — C-33]
  This coherence audit is a dedicated post-inspection step. It runs after all per-pair
  inspections are complete. If the per-pair gates above (NGT → Check B → CAT) are
  reordered, this audit still runs last. The post-inspection requirement is an
  architectural property of this template — not a consequence of the current gate
  sequence.

  [C-31 gate — runs after all per-pair inspections are complete, before word count]
  [C-32 verbatim-restate protocol — this audit is self-sufficient; no external lookup required]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural depth property satisfied — C-32: verbatim-restate depth. The comparison
      executes from claims present in this section; no re-inspection of prior locations
      required. An audit without the verbatim-restate instruction is C-32 FAIL even if
      the verdict gate names all three layers.
    Structural isolation property satisfied — C-33: gate-order independence. The
      [STRUCTURAL CONSTRAINT] header above declares the post-inspection requirement as
      an architectural property. If per-pair gates are reordered, this audit still runs
      last. An audit whose post-inspection positioning is positional (emergent from
      current numbering) but not declared is C-33 FAIL.
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance. Cross-layer incoherence is a template
      design failure.
    Introduced in: V-01(R13) — first evaluable after three-layer universal satisfaction.
    Structural removal test: removing this audit removes the only cross-layer coherence
      enforcement in the template.
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

  If any pair returns INCOHERENT:
    STOP. Identify which layer's synthesis claim is the outlier.
    Rewrite the outlier claim to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Cross-layer coherence: CONFIRMED. All mechanism pairs present at multiple
    layers carry consistent synthesis claims. Verbatim restate executed from audit section
    — no external lookup required."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed
  800 words. If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: C-35 + C-36

**Axis:** Declaration verbatim-restate commitment (C-35) combined with coherence audit
Declaration dependency gate (C-36). Tests whether Declaration-level commitment and
audit-level enforcement coupling are additive without structural friction. V-01 established
C-35 in isolation; V-02 established C-36 in isolation. V-04 confirms they compose: the
Declaration commits to verbatim-restate protocol depth (C-35), and the audit's ENTRY GATE
confirms the Declaration is present before executing (C-36). This creates a bidirectional
contract: the Declaration binds the protocol form forward; the audit ENTRY GATE requires
the Declaration backward. C-37 absent by design (gate rationale functional, not criterion-
referenced).

**Hypothesis:** C-35 and C-36 are structurally complementary without being redundant.
C-35 operates at the Declaration site: the commitment binds the author to verbatim-restate
depth before any pair inspection. C-36 operates at the audit site: the ENTRY GATE blocks
audit execution if the Declaration is absent. Neither implies the other — C-35 without C-36
allows an audit without checking Declaration presence; C-36 without C-35 requires the
Declaration without naming the protocol depth it should commit to. Together they form a
complete contract: present (C-36) and content-specified (C-35). The combination predicts
that the Declaration's commitment text (C-35) and the audit's ENTRY GATE (C-36) do not
interact with the verbatim-restate protocol execution (C-32) or the structural isolation
header (C-33) — all four properties operate at different structural positions.

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

-- DOMAIN FAILURE MODE TAXONOMY ------------------------------------------------

Before inspecting any pair, name the cross-pair failure modes this inspection sequence
is designed to surface. These are structural patterns that can occur even when every
individual pair inspection applies correct constraint vocabulary (C-26):

  Silent antagonism: Two mechanisms each achieve their target criteria independently
    while degrading each other's effectiveness in compound configurations. Per-pair
    inspection returns correct archetypes for both; the mutual degradation is visible
    only when the pair's combined effect across surprises is evaluated.

  Archetype drift: A pair whose archetype classification shifts across rounds as new
    mechanism pairs are added to the manifest, invalidating cross-round comparison.
    The individual pair inspection is consistent with the current manifest; the drift
    is visible only by comparing classifications across manifest versions.

  Hold both patterns in view during all pair inspections. If either appears: record
  the observation in the Patterns section (Step 8), not inline.

-- PAIR INSPECTION SEQUENCE ----------------------------------------------------

For each pair of mechanisms, inspect the composability relationship. Use this four-step
sequence for every pair — no skipping steps, no reversing order:

  Step 1 — Pick the archetype. Choose from the taxonomy below. Use the canonical
            examples as your comparison baseline.
  Step 2 — Run the CONSISTENCY GATE vocabulary check for the archetype you chose.
            If the check fails (NO), go back to Step 1 and pick again.
  Step 3 — Write the mechanism. This is the analytical statement: directional, causal,
            in vocabulary consistent with the archetype you verified in Step 2.
  Step 4 — Write the composability claim. This is the synthetic conclusion: one sentence
            stating what the mechanism in Step 3 implies for this pair's combined
            behavior. It is distinct from the mechanism — not a restatement.

VOCABULARY REFERENCE — know the constraint class before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism must state that A's output is B's
                 required input. Test: "Does this mechanism state A's output is B's
                 required input?" Answer YES or NO.
  ESTABLISHES  → property creation + one-way dependency: the mechanism must state that
                 A creates a property B operates on, without feedback from B to A. Test:
                 "Does A create a property B operates on, with no feedback path?" YES/NO.
  AMPLIFIES    → effectiveness scaling: the mechanism must state that A increases the
                 precision or strength of B's per-surprise enforcement. Test: "Does A
                 increase the precision or strength of B's enforcement?" YES or NO.
  PARALLEL     → independent-path operation: the mechanism must state that A and B
                 enforce from non-dependent paths, each sufficient alone. Test: "Do A
                 and B operate independently, each sufficient without the other?" YES/NO.

Taxonomy with template-complete canonical pair examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "Does NGT's
                mechanism describe input-dependency?" PASS. NGT's newcomer-comprehension
                gate output is Check B's required input — confirmed input-dependency.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test. No mechanism substitutes for newcomer-
                comprehension as Check B's input.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                accessibility enforcement produces the verified stranger-readable unit
                Check B's portability test requires. The two gates form a forward
                dependency with no competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    > CANONICAL EXAMPLE: Check B ESTABLISHES the portability substrate that CAT enforces.
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Does
                Check B create a property CAT operates on, with no feedback?" PASS.
      Step 3 — Mechanism: Check B verifies that each surprise is fully derivable as a
                standalone unit; CAT enforces authoritative claim-voice on the verified-
                portable substrate. Removing Check B removes the portability property
                CAT operates on. No feedback from CAT to Check B.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is the precondition CAT requires,
                not a constraint CAT circumvents. They operate on structurally distinct
                properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  PARALLEL — A and B independently enforce the same sub-property from distinct paths.

    > CANONICAL EXAMPLE: [fill in when a PARALLEL pair exists in this variation's manifest]
      Step 1 — Archetype: PARALLEL
      Step 2 — CONSISTENCY GATE: independent-path operation. [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward without re-derivation — TEMPLATE-COMPLETE):

  NGT + Check B:
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: PREREQUISITE vocabulary class → input-dependency framing
              required. Test: "Does the mechanism state NGT's output is Check B's required
              input?" PASS. Input-dependency confirmed.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. This input-dependency holds in any compound configuration.
    Step 4 — Composability-claim: NGT and Check B compose without degradation in any
              configuration. The newcomer-accessibility verification NGT performs is the
              structural precondition Check B requires, not a competing demand; removing
              either gate degrades the other's enforcement floor.

Remaining pairs — complete all before Declaration:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT:
    Step 1 — Archetype: [compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    Step 3 — Mechanism: [fill using canonical example as reference]
    Step 4 — Composability-claim: [fill using canonical example as reference]

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

Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-step
sequence (Archetype → CONSISTENCY GATE → Mechanism → Composability-claim). CONSISTENCY
GATE vocabulary check recorded for each pair (constraint class + YES/NO verdict). Canonical
examples are template-complete (all four fields populated). ★BASELINE entry for NGT+Check B
is template-complete (all four fields populated, including Composability-claim). All
mechanisms reinforce each other toward the single stranger-reader target. No conflicts found.
VERBATIM-RESTATE COMMITMENT: The cross-layer coherence audit (Step 9) will be executed
using the verbatim-restate protocol — each layer's synthesis claim will be restated verbatim
in the audit section before the COHERENT/INCOHERENT verdict gate. Writing may begin."

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — before C-18 was written; not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

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
    Introduced in: V-05(R4) — not installed to satisfy a rubric gap.
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
    Introduced in: V-04(R5) — not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.

  For each surprise individually:
    (1) Is it a direct claim? Check for prohibited constructs from Rule 2 — none allowed.
    (2) Is it stranger-accessible? CAT confirms the coupling holds at the authority level.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises in sequence — one pass, front to back.
  Any generic or absent label: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises in this sequence:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  Every field must have a populated value. Any blank, N/A, or placeholder: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Read all surprises for shared root causes.
  If two or more surprises share a root cause: write one Patterns section naming the
  shared dynamic. If no two surprises share a root cause: omit the Patterns section.

== STEP 9 — CROSS-LAYER COHERENCE AUDIT ========================================

  [STRUCTURAL CONSTRAINT — C-33]
  This coherence audit is a dedicated post-inspection step. It runs after all per-pair
  inspections are complete. If the per-pair gates above (NGT → Check B → CAT) are
  reordered, this audit still runs last. The post-inspection requirement is an
  architectural property of this template — not a consequence of the current gate
  sequence.

  ENTRY GATE [C-36 — Declaration dependency]:
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║ PRECONDITION: Confirm the PRE-WRITE Declaration has been written above.  ║
  ║ The Declaration is a runtime precondition for this audit — not merely a  ║
  ║ prior step. If the Declaration has not been completed, STOP here and     ║
  ║ return to the PRE-WRITE: COMPOSABILITY MANIFEST section.                 ║
  ║ Do not execute this audit until the Declaration is confirmed present.    ║
  ╚═══════════════════════════════════════════════════════════════════════════╝

  [C-31 gate — runs after all per-pair inspections are complete, before word count]
  [C-32 verbatim-restate protocol — this audit is self-sufficient; no external lookup required]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural depth property: C-32 (verbatim-restate — comparison executes from claims
      present in this section)
    Structural isolation property: C-33 (gate-order independence — post-inspection
      structural constraint declared above)
    Declaration dependency: C-36 (ENTRY GATE confirms Declaration present before audit
      executes; C-19 is a runtime precondition for C-31)
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance.
    Introduced in: V-01(R13).
    Structural removal test: removing this audit removes the only cross-layer coherence
      enforcement in the template.
    Scope: runs once, across the full inspection set. Not per-pair; post-manifest.

  VERBATIM-RESTATE PROTOCOL:
  For each mechanism pair that appears at more than one layer, restate the synthesis claim
  from each present layer verbatim in this audit section — named with its layer identifier —
  before issuing the COHERENT/INCOHERENT verdict. Do not paraphrase. Do not summarize.
  Restate the exact text of each Step 4 claim as written at its original layer.

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

  If any pair returns INCOHERENT:
    STOP. Identify the outlier layer. Rewrite to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Cross-layer coherence: CONFIRMED. All mechanism pairs present at multiple
    layers carry consistent synthesis claims. Verbatim restate executed from audit section
    — no external lookup required. Declaration dependency confirmed."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed
  800 words. If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: C-35 + C-36 + C-37

**Axis:** Full three-criterion combination — PRE-WRITE Declaration verbatim-restate
commitment (C-35), coherence audit Declaration dependency gate (C-36), and gate rationale
criterion-referenced labeling (C-37) — combined with the R15-V05 baseline (C-32 + C-33
+ C-34). Tests whether all six structural properties (C-32 through C-37) are mutually
additive in a single variation. V-05 is the canonical reference implementation for R16:
if all six unproven criteria pass together, V-05 becomes the basis for R17's single-axis
isolation of any newly emerging criteria.

**Hypothesis:** The three new properties (C-35, C-36, C-37) occupy distinct structural
positions that do not interact with each other or with the three previously confirmed
properties (C-32, C-33, C-34): C-35 extends the Declaration text; C-36 adds an ENTRY GATE
to Step 9; C-37 adds criterion identifiers to the gate rationale within Step 9. The
criterion-referenced labels in C-37 explicitly name C-32 and C-33 as identifier references,
which is additive relative to C-35's Declaration commitment and C-36's ENTRY GATE — C-37
documents the structural properties C-32 and C-33 provide, but does not depend on C-35 or
C-36 to function. The six-way combination has no predicted interaction surface because the
six criteria operate at different template positions: Declaration content (C-35), audit
entry condition (C-36), audit rationale labeling (C-37), audit protocol depth (C-32),
audit positioning declaration (C-33), pre-inspection preamble (C-34).

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

-- DOMAIN FAILURE MODE TAXONOMY ------------------------------------------------

Before inspecting any pair, name the cross-pair failure modes this inspection sequence
is designed to surface. These are structural patterns that can occur even when every
individual pair inspection applies correct constraint vocabulary (C-26):

  Silent antagonism: Two mechanisms each achieve their target criteria independently
    while degrading each other's effectiveness in compound configurations. Per-pair
    inspection returns correct archetypes for both; the mutual degradation is visible
    only when the pair's combined effect across surprises is evaluated.

  Archetype drift: A pair whose archetype classification shifts across rounds as new
    mechanism pairs are added to the manifest, invalidating cross-round comparison.
    The individual pair inspection is consistent with the current manifest; the drift
    is visible only by comparing classifications across manifest versions.

  Hold both patterns in view during all pair inspections. If either appears: record
  the observation in the Patterns section (Step 8), not inline.

-- PAIR INSPECTION SEQUENCE ----------------------------------------------------

For each pair of mechanisms, inspect the composability relationship. Use this four-step
sequence for every pair — no skipping steps, no reversing order:

  Step 1 — Pick the archetype. Choose from the taxonomy below. Use the canonical
            examples as your comparison baseline.
  Step 2 — Run the CONSISTENCY GATE vocabulary check for the archetype you chose.
            If the check fails (NO), go back to Step 1 and pick again.
  Step 3 — Write the mechanism. This is the analytical statement: directional, causal,
            in vocabulary consistent with the archetype you verified in Step 2.
  Step 4 — Write the composability claim. This is the synthetic conclusion: one sentence
            stating what the mechanism in Step 3 implies for this pair's combined
            behavior. It is distinct from the mechanism — not a restatement.

VOCABULARY REFERENCE — know the constraint class before you run Step 2:

  PREREQUISITE → input-dependency: the mechanism must state that A's output is B's
                 required input. Test: "Does this mechanism state A's output is B's
                 required input?" Answer YES or NO.
  ESTABLISHES  → property creation + one-way dependency: the mechanism must state that
                 A creates a property B operates on, without feedback from B to A. Test:
                 "Does A create a property B operates on, with no feedback path?" YES/NO.
  AMPLIFIES    → effectiveness scaling: the mechanism must state that A increases the
                 precision or strength of B's per-surprise enforcement. Test: "Does A
                 increase the precision or strength of B's enforcement?" YES or NO.
  PARALLEL     → independent-path operation: the mechanism must state that A and B
                 enforce from non-dependent paths, each sufficient alone. Test: "Do A
                 and B operate independently, each sufficient without the other?" YES/NO.

Taxonomy with template-complete canonical pair examples:

  PREREQUISITE — A's output is B's required input. Breaking A breaks B.

    > CANONICAL EXAMPLE: NGT is a PREREQUISITE for Check B.
      Step 1 — Archetype: PREREQUISITE
      Step 2 — CONSISTENCY GATE: input-dependency vocabulary. Test: "Does NGT's
                mechanism describe input-dependency?" PASS. NGT's newcomer-comprehension
                gate output is Check B's required input — confirmed input-dependency.
      Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
                input. A surprise that fails NGT cannot pass Check B's three-component
                standalone extraction test. No mechanism substitutes for newcomer-
                comprehension as Check B's input.
      Step 4 — Composability-claim: NGT and Check B compose without degradation. NGT's
                accessibility enforcement produces the verified stranger-readable unit
                Check B's portability test requires. The two gates form a forward
                dependency with no competing demands on the shared surprise unit.

  ESTABLISHES — A creates a property that B operates on. Directional, not feedback.

    > CANONICAL EXAMPLE: Check B ESTABLISHES the portability substrate that CAT enforces.
      Step 1 — Archetype: ESTABLISHES
      Step 2 — CONSISTENCY GATE: property creation + one-way dependency. Test: "Does
                Check B create a property CAT operates on, with no feedback?" PASS.
      Step 3 — Mechanism: Check B verifies that each surprise is fully derivable as a
                standalone unit; CAT enforces authoritative claim-voice on the verified-
                portable substrate. No feedback from CAT to Check B.
      Step 4 — Composability-claim: Check B and CAT compose without degradation. The
                portability substrate Check B establishes is the precondition CAT requires,
                not a constraint CAT circumvents. They operate on structurally distinct
                properties of the same surprise unit.

  AMPLIFIES — A increases the precision or strength of B's per-surprise enforcement.

    > CANONICAL EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation's manifest]
      Step 1 — Archetype: AMPLIFIES
      Step 2 — CONSISTENCY GATE: effectiveness scaling. [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  PARALLEL — A and B independently enforce the same sub-property from distinct paths.

    > CANONICAL EXAMPLE: [fill in when a PARALLEL pair exists in this variation's manifest]
      Step 1 — Archetype: PARALLEL
      Step 2 — CONSISTENCY GATE: independent-path operation. [YES/NO]
      Step 3 — Mechanism: [fill in]
      Step 4 — Composability-claim: [fill in]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward without re-derivation — TEMPLATE-COMPLETE):

  NGT + Check B:
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: PREREQUISITE vocabulary class → input-dependency framing
              required. Test: "Does the mechanism state NGT's output is Check B's required
              input?" PASS. Input-dependency confirmed.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. This input-dependency holds in any compound configuration.
    Step 4 — Composability-claim: NGT and Check B compose without degradation in any
              configuration. The newcomer-accessibility verification NGT performs is the
              structural precondition Check B requires, not a competing demand; removing
              either gate degrades the other's enforcement floor.

Remaining pairs — complete all before Declaration:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT:
    Step 1 — Archetype: [compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: property creation + one-way dependency — YES/NO
    Step 3 — Mechanism: [fill using canonical example as reference]
    Step 4 — Composability-claim: [fill using canonical example as reference]

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

Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-step
sequence (Archetype → CONSISTENCY GATE → Mechanism → Composability-claim). CONSISTENCY
GATE vocabulary check recorded for each pair (constraint class + YES/NO verdict). Canonical
examples are template-complete (all four fields populated). ★BASELINE entry for NGT+Check B
is template-complete (all four fields populated, including Composability-claim). All
mechanisms reinforce each other toward the single stranger-reader target. No conflicts found.
VERBATIM-RESTATE COMMITMENT: The cross-layer coherence audit (Step 9) will be executed
using the verbatim-restate protocol — each layer's synthesis claim will be restated verbatim
in the audit section before the COHERENT/INCOHERENT verdict gate. Writing may begin."

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
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

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
    Introduced in: V-05(R4) — not installed to satisfy a rubric gap.
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
    Introduced in: V-04(R5) — not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.

  For each surprise individually:
    (1) Is it a direct claim? Check for prohibited constructs from Rule 2 — none allowed.
    (2) Is it stranger-accessible? CAT confirms the coupling holds at the authority level.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises in sequence — one pass, front to back.
  Any generic or absent label: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises in this sequence:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  Every field must have a populated value. Any blank, N/A, or placeholder: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Read all surprises for shared root causes.
  If two or more surprises share a root cause: write one Patterns section naming the
  shared dynamic. If no two surprises share a root cause: omit the Patterns section.

== STEP 9 — CROSS-LAYER COHERENCE AUDIT ========================================

  [STRUCTURAL CONSTRAINT — C-33]
  This coherence audit is a dedicated post-inspection step. It runs after all per-pair
  inspections are complete. If the per-pair gates above (NGT → Check B → CAT) are
  reordered, this audit still runs last. The post-inspection requirement is an
  architectural property of this template — not a consequence of the current gate
  sequence.

  ENTRY GATE [C-36 — Declaration dependency]:
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║ PRECONDITION: Confirm the PRE-WRITE Declaration has been written above.  ║
  ║ The Declaration is a runtime precondition for this audit — not merely a  ║
  ║ prior step. If the Declaration has not been completed, STOP here and     ║
  ║ return to the PRE-WRITE: COMPOSABILITY MANIFEST section.                 ║
  ║ Do not execute this audit until the Declaration is confirmed present.    ║
  ╚═══════════════════════════════════════════════════════════════════════════╝

  [C-31 gate — runs after all per-pair inspections are complete, before word count]
  [C-32 verbatim-restate protocol — this audit is self-sufficient; no external lookup required]

  Gate design rationale:
    Criterion enforced: C-31 (cross-layer synthesis claim coherence)
    Structural depth property satisfied — C-32: verbatim-restate depth. The comparison
      executes from claims present in this section; no re-inspection of prior locations
      required. An audit without the verbatim-restate instruction is C-32 FAIL even if
      the verdict gate names all three layers.
    Structural isolation property satisfied — C-33: gate-order independence. The
      [STRUCTURAL CONSTRAINT] header above declares the post-inspection requirement as
      an architectural property. If per-pair gates are reordered, this audit still runs
      last. An audit whose post-inspection positioning is positional but not declared is
      C-33 FAIL.
    Declaration dependency — C-36: the ENTRY GATE above confirms the Declaration is
      written before this audit executes. C-19 is a runtime precondition for C-31.
    Primary motivation: when C-27, C-29, and C-30 simultaneously pass, the synthesis
      claims at each layer must agree in substance.
    Introduced in: V-01(R13) — first evaluable after three-layer universal satisfaction.
    Structural removal test: removing this audit removes the only cross-layer coherence
      enforcement in the template.
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

  If any pair returns INCOHERENT:
    STOP. Identify the outlier layer. Rewrite to restore cross-layer agreement.
    Re-run this audit block for the affected pair before proceeding.

  If all pairs return COHERENT:
    Write: "Cross-layer coherence: CONFIRMED. All mechanism pairs present at multiple
    layers carry consistent synthesis claims. Verbatim restate executed from audit section
    — no external lookup required. Declaration dependency confirmed: Declaration was present
    before audit executed. Criterion-referenced properties confirmed: C-32 verbatim-restate
    depth executed; C-33 gate-order independence structurally declared."
    Continue to Step 10.

== STEP 10 — WORD COUNT FINAL CHECK ============================================

  Count the full echo (all surprises + Patterns section if present). Must not exceed
  800 words. If over: extract the essential claims and cut the connecting tissue.

== STEP 11 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## Summary of R16 Variation Design Decisions

**Why no ablations in R16:**
R15's ablation design (some variations intentionally failing C-32/C-33/C-34) served the
purpose of single-axis isolation in the first targeted round. R16's purpose is first uniform
confirmation of C-32/C-33/C-34 — ablation would prevent the two-round threshold from being
met. All five R16 variations carry C-32 + C-33 + C-34 without exception.

**Why C-37 targets the gate rationale, not a new section:**
C-37 is a documentation property layered onto the existing gate rationale block required by
C-22. It does not add a new structural section; it adds identifier labels to an existing
required block. This makes C-37 the lowest-friction of the three new criteria — it is an
annotation on an existing required element rather than a new structural requirement.

**Why C-35 and C-36 are structurally complementary but not redundant:**
C-35 binds the Declaration's content (it must commit to verbatim-restate depth). C-36 binds
the audit's executability (it must confirm the Declaration's presence). V-04's combination
test confirms: C-35 without C-36 allows the audit to execute even if the Declaration were
somehow absent; C-36 without C-35 requires the Declaration's presence without specifying
its content. Together they close both gaps.

**R17 setup:**
If R16 confirms C-32/C-33/C-34 uniformly (first confirmed round for each) and C-35/C-36/C-37
first-targeted, R17 will be structured as:
- Goal 1: Second confirmed round for C-32, C-33, C-34 → promotes all three to Proven
- Goal 2: Second targeted round for C-35, C-36, C-37
- The proven total increases from 30 to 33 pts; budget remains 25 pts; ceiling remains 100
