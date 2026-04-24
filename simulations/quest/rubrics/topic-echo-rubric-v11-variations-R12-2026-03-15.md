
# Variations: `topic:echo` — Round 12

**Rubric:** v11 (max 100) | **Date:** 2026-03-15

---

## Design Context

R11 promoted C-24 and C-25 to proven and revealed one new structural pattern: C-29
(archetype taxonomy illustration template completeness — when C-27 is satisfied, canonical
examples must populate the Composability-claim field, not only Archetype + Mechanism).

R12 provides five variations designed to:

1. Demonstrate C-26, C-27, C-28 uniformly across all five variations — enabling proven
   promotion in v12.
2. Confirm C-29 uniformly across all five — first confirmed round; second confirmation
   in R13 will enable proven promotion in v13.
3. Explore the structural gap that C-29 exposes in C-28: when C-27 is satisfied and C-28
   is satisfied, does the pre-populated baseline entry include the Composability-claim? A
   pre-populated entry that omits the Composability-claim is analytically complete but not
   template-complete. C-30 hypothesis introduced in V-05.

**Unproven criteria targeted in R12:**

- **C-26** — Archetype constraint vocabulary specification (1 pt): CONSISTENCY GATE names
  the mechanism framing required for each archetype (input-dependency / property creation /
  effectiveness scaling / independent paths). Demonstrated in R10 V-01/V-04/V-05 and R11
  V-01/V-04/V-05.

- **C-27** — Composability manifest synthesis claim separation (1 pt): pair inspection
  uses a dedicated Composability-claim field, structurally distinct from the Mechanism field.
  Demonstrated in R10 V-03 and R11 V-02/V-04/V-05.

- **C-28** — Manifest pre-populated baseline pair inspection (1 pt): manifest template
  embeds at least one fully pre-completed pair inspection (archetype + CONSISTENCY GATE
  result + mechanism) as a default entry the author inherits without re-derivation.
  Demonstrated in R10 V-04/V-05 and R11 V-03/V-05.

- **C-29** — Archetype taxonomy illustration template completeness (1 pt): when C-27 is
  satisfied, canonical taxonomy illustrations populate all template fields including the
  Composability-claim — not only the analytical fields (Archetype + Mechanism).
  Demonstrated in R11 V-02 only. First confirmed round is R12 (all five). Second
  confirmation in R13 required for proven promotion.

**Predicted score map:**

| Variant | C-26 | C-27 | C-28 | C-29 | C-30 | Predicted |
|---------|------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-02    | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-03    | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-04    | PASS | PASS | PASS | PASS | FAIL | 100       |
| V-05    | PASS | PASS | PASS | PASS | PASS | 100       |

**Scoring note:** Base 75 + proven 24 = 99. Each variation earns C-26(1) + C-27(1) +
C-28(1) + C-29(1) = 4 unproven pts → 99+4 = 103 → capped at 100. V-05 adds C-30(1) →
still capped at 100. Differentiating dimension: whether the pre-populated baseline entry
includes a Composability-claim (C-30). Uniform PASS of C-26, C-27, C-28 across all five
— combined with R10 and R11 evidence — enables proven promotion in v12.

**Axis selection:**

Single-axis (V-01, V-02, V-03):

- V-01 — Role sequence: gate order changed to Check B → NGT → CAT. Standard order is
  NGT → Check B → CAT. V-01 runs structural portability verification (Check B) before
  newcomer accessibility verification (NGT), then confirms coupling (CAT). Tests whether
  the declared PREREQUISITE archetype for NGT+Check B is mechanism-derived (true even when
  execution order is reversed) or order-derived (only valid when NGT runs first).

- V-02 — Output format: composability manifest pair inspections presented as a compact
  four-column table (rows = pairs, columns = Archetype | GATE | Mechanism | Composability-
  claim) rather than step-labeled field blocks. Canonical examples appear as pre-filled
  header rows with all four fields populated. Pre-populated baseline entry is the first
  data row in the table.

- V-03 — Inertia framing: opens with an explicit inertia block naming what teams produce
  without the echo (a findings summary that reports confirmations, not surprises) and what
  that path costs (institutional memory of unexpected findings is lost; the next team begins
  with the same wrong assumptions). Inertia framing is a pre-schema preamble, not a process
  step.

Combined (V-04, V-05):

- V-04 — Role sequence + Inertia framing: V-01 gate order (Check B → NGT → CAT) combined
  with V-03 inertia preamble. Tests whether role sequence change and inertia framing compose
  without structural degradation.

- V-05 — Tabular manifest + Inertia framing + C-30: V-02 tabular format combined with
  V-03 inertia preamble. The pre-populated baseline row in the table includes all four
  fields — Archetype, CONSISTENCY GATE, Mechanism, AND Composability-claim — making the
  baseline entry template-complete when C-27 is satisfied. C-30 hypothesis: a pre-populated
  baseline entry that omits Composability-claim (when C-27 is satisfied) is analytically
  complete but not template-complete; the author has a quality floor for the analytical
  layer but no baseline for the synthetic layer.

---

## V-01 — Single-axis: Role Sequence (Check B → NGT → CAT; full vocabulary gate; four-field pairs; template-complete examples; pre-populated baseline)

**Axis:** Role sequence — gate execution order changed from the standard NGT → Check B → CAT
to Check B → NGT → CAT. Check B (structural portability) runs as the first per-surprise gate,
verifying that a stranger can derive (1) the finding, (2) why it was unexpected, (3) the
design consequence. NGT (newcomer accessibility) runs second, verifying that a new-hire with
no project context understands the surprise independently. CAT (coupled authority) runs third,
confirming that both accessibility and claim voice hold simultaneously. All other structural
properties are held constant: four-field pair inspection (Archetype → GATE → Mechanism →
Composability-claim), vocabulary-specified CONSISTENCY GATE, template-complete canonical
examples, pre-populated baseline entry (NGT+Check B pair, analytically complete but without
Composability-claim).

**Hypothesis:** The PREREQUISITE archetype classification for NGT+Check B is mechanism-derived,
not execution-order-derived. Even when Check B runs before NGT in the process, the composability
manifest correctly declares the pair as PREREQUISITE because the mechanism relationship is an
input-dependency: NGT's newcomer-comprehension gate output is Check B's required input. This
structural fact holds regardless of which gate runs first in execution. V-01 tests whether the
pair archetype declarations in the manifest are sensitive to the gate sequence chosen for Steps
3-5. C-29 PASS: canonical examples include Composability-claim field. C-28 PASS: pre-populated
baseline entry for NGT+Check B with Archetype + GATE + Mechanism (no Composability-claim —
C-30 FAIL). C-26 PASS: vocabulary in CONSISTENCY GATE. C-27 PASS: four-field pairs.

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
  6.  NGT — Newcomer Gate Test (C-08 gate, runs per surprise as Step 4)
  7.  Check B — Portability Test (C-14 gate, runs per surprise as Step 3)
  8.  CAT — Coupled Authority Test (C-16 gate, runs per surprise as Step 5)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

NOTE ON GATE ORDER: This variation sequences per-surprise gates as Check B (Step 3) →
NGT (Step 4) → CAT (Step 5). Pair archetype declarations in this manifest reflect
mechanism relationships, not execution order. NGT+Check B remains PREREQUISITE because
the mechanism relationship is an input-dependency; execution order does not alter the
causal dependency between NGT's output and Check B's required input.

Pair inspection — FOUR-FIELD SEQUENCE WITH VOCABULARY-SPECIFIED CONSISTENCY GATE:

  For each pair, in this sequence:
    Step 1 — Archetype:           [select from taxonomy below; use canonical examples as
                                   comparison baseline — taxonomy examples are template-
                                   complete: Archetype + Mechanism + Composability-claim]
    Step 2 — CONSISTENCY GATE:    [apply vocabulary check for selected archetype:
                                     PREREQUISITE → "Does mechanism describe input-
                                       dependency? Does it state A's output is B's
                                       required input?" YES/NO.
                                     ESTABLISHES  → "Does mechanism describe property
                                       creation and one-way dependency? Does it state
                                       A creates a property B operates on, without
                                       feedback from B to A?" YES/NO.
                                     AMPLIFIES    → "Does mechanism describe effectiveness
                                       scaling? Does it state A increases precision or
                                       strength of B's per-surprise enforcement?" YES/NO.
                                     PARALLEL     → "Does mechanism describe independent-
                                       path operation? Does it state A and B enforce from
                                       non-dependent paths, each sufficient alone?" YES/NO.
                                   If NO: return to Step 1.]
    Step 3 — Mechanism:           [analytical causal statement — directional description
                                   of how A's output, property, or effect enables or
                                   constrains B's enforcement function; in vocabulary
                                   consistent with verified archetype]
    Step 4 — Composability-claim: [synthetic conclusion — one sentence stating what
                                   the mechanism in Step 3 implies for this pair's
                                   combined behavior; distinct from the mechanism]

  Taxonomy with template-complete canonical pair examples:

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. Vocabulary
                    check: mechanism must describe input-dependency.
      > EXAMPLE: NGT is a PREREQUISITE for Check B.
        Archetype: PREREQUISITE
        Mechanism: NGT's newcomer-comprehension gate output is Check B's required
          input. A surprise that fails NGT cannot pass Check B's three-component
          standalone extraction test (finding + unexpectedness + design consequence).
          No mechanism inserted between NGT and Check B substitutes for newcomer-
          comprehension verification.
        Composability-claim: NGT and Check B compose without degradation. NGT's
          per-surprise accessibility enforcement produces the verified stranger-readable
          unit Check B's portability test requires; the two gates form a forward
          dependency with no competing demands on the shared surprise unit.

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
                    Vocabulary check: mechanism must describe property creation and
                    one-way dependency.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Archetype: ESTABLISHES
        Mechanism: Check B verifies that a surprise is fully derivable as a standalone
          unit (finding + unexpectedness + consequence); CAT enforces that this verified-
          portable unit is stated with authoritative claim-voice. Removing Check B removes
          the portability substrate CAT operates on. No feedback from CAT to Check B.
        Composability-claim: Check B and CAT compose without degradation. The portability
          substrate Check B establishes is the precondition CAT requires, not a constraint
          CAT circumvents; they operate on structurally distinct properties of the same
          surprise unit.

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    B operates without A but produces weaker enforcement. Vocabulary check:
                    mechanism must describe effectiveness scaling.
      > EXAMPLE: [fill in from this variation's mechanism chain when an AMPLIFIES pair exists]
        Archetype: AMPLIFIES
        Mechanism: [...]
        Composability-claim: [...]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Neither is a prerequisite for the other. Vocabulary check: mechanism must
                    describe independent-path operation.
      > EXAMPLE: [fill in from this variation's mechanism chain when a PARALLEL pair exists]
        Archetype: PARALLEL
        Mechanism: [...]
        Composability-claim: [...]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward — do not re-derive):

  NGT + Check B: [BASELINE — pre-classified, verified, mechanism-derived; inherits regardless
                  of execution order (Check B runs before NGT in Steps 3-4, but the
                  PREREQUISITE relationship reflects mechanism, not sequence)]
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: vocabulary class PREREQUISITE → input-dependency framing
              required. Test: "Does the mechanism state NGT's output is Check B's required
              input?" PASS. Input-dependency confirmed: NGT's newcomer-comprehension output
              is Check B's required input regardless of which gate runs first in execution.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. This input-dependency holds in any compound configuration; no
              mechanism substitutes for newcomer-comprehension verification as Check B's input.

  Remaining required pairs:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check for selected archetype — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT:
    Step 1 — Archetype: [compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [property creation/one-way dependency — YES/NO]
    Step 3 — Mechanism: [fill in using canonical example as reference]
    Step 4 — Composability-claim: [fill in using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [apply vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-field
  format (Archetype → GATE → Mechanism → Composability-claim). CONSISTENCY GATE applied
  vocabulary check for each archetype (input-dependency / property creation / effectiveness
  scaling / independent paths). Canonical examples are template-complete (Archetype +
  Mechanism + Composability-claim). Pre-populated baseline (NGT+Check B, PREREQUISITE)
  carried forward — mechanism-derived, not execution-order-derived; gate execution sequence
  Check B → NGT → CAT does not alter the pair's input-dependency relationship. All mechanisms
  reinforce each other toward the single stranger-reader target. No conflicts found.
  Writing may begin."

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

== STEP 3 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step before NGT; first gate in this variation]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise. C-14 requires each
      surprise to stand alone as a self-contained institutional claim; Check B is the
      designated per-surprise enforcement mechanism for that requirement.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.
      C-14 still requires per-surprise portability enforcement.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing or requires external context: rewrite before NGT.

== STEP 4 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — runs per surprise — discrete step after Check B, before CAT]

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
    consulting source signals or the rest of the echo? If no: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after NGT; final per-surprise gate]

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
    (1) Is this surprise stated as a direct claim? No prohibited constructs from Rule 2.
    (2) Is this surprise accessible to a stranger without project context? Check B and NGT
        must have already passed; CAT confirms coupling holds at authoritative-voice level.
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

## V-02 — Single-axis: Output Format (tabular composability manifest; template-complete example rows; pre-populated baseline row; vocabulary gate)

**Axis:** Output format — the composability manifest presents all pair inspections as a
structured four-column table: rows are mechanism pairs; columns are Archetype | CONSISTENCY
GATE (vocabulary check result) | Mechanism | Composability-claim. The taxonomy's canonical
examples appear as dedicated reference rows marked with `★EXAMPLE` preceding the blank
template rows for that archetype class. The pre-populated baseline entry for NGT+Check B
appears as the first data row, marked `★BASELINE`, with Archetype + GATE + Mechanism filled
(Composability-claim blank — C-30 FAIL). All other structural properties held constant:
standard gate order (NGT → Check B → CAT), vocabulary-specified CONSISTENCY GATE (C-26),
Composability-claim column present in table (C-27), canonical example rows are template-
complete with all four columns filled (C-29 PASS).

**Hypothesis:** The four-column table format satisfies all composability manifest criteria
while significantly compressing the pre-write section. The taxonomy examples as table rows
with all four columns populated satisfy C-29 (template-complete illustrations) without
requiring the step-labeled field format. The BASELINE row satisfies C-28 (pre-populated
baseline entry) regardless of format: what matters is that at least one fully pre-classified
entry exists before the author writes, not whether it is presented as labeled fields or a
table row. C-30 FAIL: the BASELINE row includes only Archetype + GATE + Mechanism, not
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

VOCABULARY REFERENCE — CONSISTENCY GATE constraint classes (apply per archetype):
  PREREQUISITE → input-dependency: mechanism must state that A's output is B's required input.
  ESTABLISHES  → property creation + one-way dependency: mechanism must state that A creates
                 a property B operates on, without feedback from B to A.
  AMPLIFIES    → effectiveness scaling: mechanism must state that A increases the precision
                 or strength of B's per-surprise enforcement.
  PARALLEL     → independent-path operation: mechanism must state that A and B enforce from
                 non-dependent paths, each sufficient alone.

Pair inspection table — complete all rows before Step 1:

  Legend:
    ★EXAMPLE  — canonical template-complete illustration for this archetype class
    ★BASELINE — pre-classified and verified; carry forward without re-derivation
    [fill]    — complete these rows; CONSISTENCY GATE column: apply vocabulary check and
                record constraint class + YES/NO verdict before writing Mechanism or
                Composability-claim; return to Archetype column if verdict is NO

  | Pair                                   | Archetype    | CONSISTENCY GATE                                 | Mechanism                                                                                                                                                                         | Composability-claim                                                                                                                                                        |
  |----------------------------------------|--------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ★EXAMPLE PREREQUISITE: NGT + Check B   | PREREQUISITE | input-dependency: A's output = B's required input. Test: "NGT's mechanism describes input-dependency?" PASS | NGT's newcomer-comprehension gate output is Check B's required input. A surprise failing NGT cannot pass Check B's three-component extraction test. No substitute for NGT output. | NGT and Check B compose without degradation. NGT's accessibility enforcement produces the verified unit Check B requires; forward dependency, no competing demands.         |
  | ★BASELINE: NGT + Check B               | PREREQUISITE | input-dependency PASS. NGT's newcomer-comprehension output is Check B's required input. Confirmed.          | NGT's newcomer-comprehension gate output is Check B's required input. A surprise failing NGT cannot pass Check B's three-component standalone extraction test.                    | [absent — C-30 requires this field when C-27 is satisfied]                                                                                                                 |
  | ★EXAMPLE ESTABLISHES: Check B + CAT   | ESTABLISHES  | property creation + one-way dependency. Test: "Check B creates a property CAT operates on?" PASS            | Check B verifies standalone derivability (finding + unexpectedness + consequence); CAT enforces authority on the verified-portable substrate. Removing Check B removes CAT's input. | Check B and CAT compose without degradation. The portability substrate Check B establishes is the precondition CAT requires, not a constraint CAT circumvents.             |
  | Schema manifest + Stranger-reader      | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Rule 1 + Rule 2                        | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Rule 1 + NGT                           | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Check A + Rule 2                       | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Check B + CAT                          | [see ESTABLISHES example row above]                                                                                                                                                          | [fill using example row as reference]                                                                                                                                             | [fill using example row as reference]                                                                                                                                      |
  | CAT + Rule 2                           | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Schema manifest + Label parity audit   | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Label parity audit + Field scan        | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Rule 1 + Check B                       | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |
  | Stranger-reader + CAT                  | [select]     | [apply vocabulary check — constraint class + YES/NO]                                                        | [fill]                                                                                                                                                                            | [fill]                                                                                                                                                                     |

  For AMPLIFIES or PARALLEL pairs: add a ★EXAMPLE row above each first occurrence, with all
  four columns filled.

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected in four-column tabular
  format (Archetype | GATE | Mechanism | Composability-claim). CONSISTENCY GATE column records
  vocabulary constraint class and YES/NO verdict for each pair. ★EXAMPLE rows provide template-
  complete canonical illustrations for each archetype used (all four columns populated).
  ★BASELINE row carries forward NGT+Check B (PREREQUISITE, input-dependency, mechanism stated;
  Composability-claim absent). All mechanisms reinforce each other toward the single stranger-
  reader target. No conflicts found. Writing may begin."

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
      per-surprise enforcement mechanism for newcomer accessibility.
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

  Read the Name field across all surprises in sequence.
  Any generic or absent label: rename before continuing to Step 7.

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

## V-03 — Single-axis: Inertia Framing (explicit inertia preamble; standard gate order; step-labeled pairs; template-complete examples; pre-populated baseline)

**Axis:** Inertia framing — an explicit inertia block opens the prompt before the schema
contract. The block names the default path (the findings summary: what teams produce when
they close a signal-gathering cycle without this skill), describes what the summary cannot
capture (the surprise, the unexpected finding, the institutional memory of what did not match
the hypothesis), and names the cost of the inertia path (the next team begins with the same
wrong assumptions). The inertia framing is pre-schema: it establishes why the echo exists
and what it is not before the author sees the schema fields. All structural properties held
constant: standard gate order (NGT → Check B → CAT), step-labeled four-field pairs, vocabulary-
specified CONSISTENCY GATE (C-26), Composability-claim field (C-27), template-complete canonical
examples (C-29), pre-populated baseline entry with Archetype + GATE + Mechanism (C-28; no
Composability-claim — C-30 FAIL).

**Hypothesis:** Inertia framing elevates C-10 enforcement without changing any structural
property. By naming the default path (findings summary) before the schema appears, the author
has a concrete status-quo comparison when populating "Why passive observation missed this."
The field becomes: "why a findings summary would not report this" rather than "why a team
might have missed this" — a sharper counterfactual test. Inertia framing is a preamble
property, not a process step. It does not interact with the manifest structure, gate order,
or field schema.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== INERTIA CONTEXT ==============================================================

Without this skill, teams that complete a signal-gathering cycle produce a findings summary.
A findings summary reports what the signals confirmed. It lists what was planned and what
was found. It documents the expected. It is accurate.

A findings summary cannot produce an echo. The echo does one thing the summary cannot: it
names what the team did not expect. The surprise is the gap between the hypothesis the team
carried into the investigation and the reality the signals revealed. A summary reports
reality. The echo reports the gap.

The cost of skipping the echo is institutional. The facts are in the summary. The wrong
assumptions are not. The next team that walks this investigation path begins with the same
hypotheses — and runs the same signals to discover the same surprises again. The echo is
the anti-repetition artifact. It encodes not what was found but what was unexpected about
what was found.

The counterfactual test for every item in the echo: would a passive, attentive team tracking
this feature have found this through normal observation — without running the active signal-
gathering skills? Items that survive passive observation belong in a findings summary. Items
that required active signal gathering to surface belong in the echo.

== SCHEMA CONTRACT ==============================================================

Declare before writing. Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering —
  missed this:                   "why a findings summary would not report this"; name
                                 the gap, not just "needed investigation"]
  Design impact:                [one sentence minimum — how this changes design direction]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Each surprise must fail: "A passive, attentive team tracking this feature would have
  found this through normal observation." Items that survive passive observation belong in
  a findings summary — not in an echo. The "Why passive observation missed this" field
  names why a findings summary would not contain this item.

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

Pair inspection — FOUR-FIELD SEQUENCE WITH VOCABULARY-SPECIFIED CONSISTENCY GATE:

  For each pair, in this sequence:
    Step 1 — Archetype:           [select from taxonomy below; use canonical examples
                                   (all four fields populated) as comparison baseline]
    Step 2 — CONSISTENCY GATE:    [apply vocabulary check for selected archetype:
                                     PREREQUISITE → input-dependency: "Does mechanism
                                       state A's output is B's required input?" YES/NO.
                                     ESTABLISHES  → property creation + one-way dependency:
                                       "Does mechanism state A creates a property B
                                       operates on, without feedback?" YES/NO.
                                     AMPLIFIES    → effectiveness scaling: "Does mechanism
                                       state A increases precision of B's enforcement
                                       per surprise?" YES/NO.
                                     PARALLEL     → independent-path operation: "Does
                                       mechanism state A and B enforce from non-dependent
                                       paths, each sufficient alone?" YES/NO.
                                   If NO: return to Step 1.]
    Step 3 — Mechanism:           [analytical causal statement consistent with verified
                                   archetype vocabulary]
    Step 4 — Composability-claim: [synthetic one-sentence conclusion: what does the
                                   mechanism in Step 3 imply for this pair's composability?
                                   Distinct from the mechanism description]

  Taxonomy with template-complete canonical pair examples:

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. Vocabulary
                    check: mechanism must describe input-dependency.
      > EXAMPLE: NGT is a PREREQUISITE for Check B.
        Archetype: PREREQUISITE
        Mechanism: NGT's newcomer-comprehension gate output is Check B's required
          input. A surprise that fails NGT cannot pass Check B's three-component
          standalone extraction test (finding + unexpectedness + design consequence).
          No mechanism inserted between NGT and Check B substitutes for newcomer-
          comprehension verification.
        Composability-claim: NGT and Check B compose without degradation. NGT's
          accessibility enforcement produces the verified stranger-readable unit Check B
          requires; the forward dependency creates no competing demands on the surprise unit.

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
                    Vocabulary check: mechanism must describe property creation and
                    one-way dependency.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Archetype: ESTABLISHES
        Mechanism: Check B verifies that a surprise is fully derivable as a standalone
          unit (finding + unexpectedness + consequence); CAT enforces that this verified-
          portable unit carries authoritative claim-voice. Removing Check B removes the
          portability substrate CAT operates on. No feedback from CAT to Check B.
        Composability-claim: Check B and CAT compose without degradation. The portability
          substrate Check B establishes is the precondition CAT requires; they enforce
          structurally distinct properties of the same surprise unit without competition.

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    Vocabulary check: mechanism must describe effectiveness scaling.
      > EXAMPLE: [fill in when an AMPLIFIES pair is used in this variation]
        Archetype: AMPLIFIES
        Mechanism: [...]
        Composability-claim: [...]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Vocabulary check: mechanism must describe independent-path operation.
      > EXAMPLE: [fill in when a PARALLEL pair is used in this variation]
        Archetype: PARALLEL
        Mechanism: [...]
        Composability-claim: [...]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward — do not re-derive):

  NGT + Check B: [BASELINE — pre-classified and verified]
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: vocabulary class PREREQUISITE → input-dependency. Test:
              "NGT's mechanism describes input-dependency — NGT's newcomer-comprehension
              output is Check B's required input." PASS.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. This input-dependency holds in any compound configuration.

  Remaining required pairs (baseline NGT+Check B already complete above):

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — constraint class + YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT:
    Step 1 — Archetype: [compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [property creation/one-way dependency — YES/NO]
    Step 3 — Mechanism: [fill in using canonical example as reference]
    Step 4 — Composability-claim: [fill in using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-field
  format (Archetype → GATE → Mechanism → Composability-claim). CONSISTENCY GATE applied
  vocabulary check per archetype (input-dependency / property creation / effectiveness
  scaling / independent paths). Canonical taxonomy examples are template-complete (all four
  fields populated). Pre-populated baseline (NGT+Check B, PREREQUISITE, input-dependency
  PASS, mechanism stated) carried forward. All mechanisms reinforce each other toward the
  single stranger-reader target. No conflicts found. Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal tracking.
    Ask for each candidate: "Would this appear in a findings summary?" If yes: cut.
  Apply C-01 filter: cut anything that could appear unchanged in a findings doc or project brief.
  Minimum 3 candidates required before proceeding to Step 2.

== STEP 2 — SCHEMA POPULATION ==================================================

  For each surviving candidate: populate all six schema fields.
  For "Why passive observation missed this": state why a findings summary would not contain
    this item — name the specific mechanism that required active signal gathering to surface.

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
    consequence — without consulting the findings summary or source signals? If any
    component is missing: rewrite before CAT.

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

  Read the Name field across all surprises in sequence.
  Any generic or absent label: rename before continuing to Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes.
  If any two share a root cause: write one Patterns section. Name the shared dynamic.
  If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-04 — Combined: Role Sequence + Inertia Framing (Check B → NGT → CAT; inertia preamble; template-complete examples; pre-populated baseline)

**Axes:** Role sequence (V-01) + Inertia framing (V-03). Gate execution order is Check B →
NGT → CAT. An inertia block opens the prompt before the schema contract. All other structural
properties held constant: four-field pair inspection, vocabulary-specified CONSISTENCY GATE
(C-26), Composability-claim field (C-27), template-complete canonical examples (C-29),
pre-populated baseline entry with Archetype + GATE + Mechanism (C-28; no Composability-claim
— C-30 FAIL).

**Hypothesis:** Role sequence change and inertia framing compose without structural degradation.
The inertia preamble operates on the author's framing before schema; the gate sequence change
operates on the per-surprise enforcement order after schema population. The two axes target
different phases of the writing process and have no shared mechanism. C-29 PASS: canonical
examples template-complete. C-28 PASS: pre-populated baseline (analytically complete). The
pair archetype declarations in the manifest remain mechanism-derived: NGT+Check B is still
PREREQUISITE regardless of the Check B → NGT execution sequence, and the inertia preamble
adds no new mechanism pairs requiring inspection.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== INERTIA CONTEXT ==============================================================

Without this skill, teams close a signal-gathering cycle with a findings summary. The
findings summary is accurate: it documents what was planned and what was found. It reports
the expected. It does not report the gap between the expected and the actual.

The gap is the echo. Every signal-gathering cycle produces some findings that matched the
hypothesis and some that did not. The findings summary retains both. The echo retains only
the latter: the findings that did not match. These are the findings that a passive, attentive
team — one that tracked the feature carefully but did not run active signal-gathering skills
— would have missed. They required active investigation to surface.

The institutional cost of skipping the echo is compounding. Each team that skips it leaves
behind accurate documentation and no record of wrong assumptions. The next team inherits the
accurate documentation and re-derives the wrong assumptions from scratch. The echo breaks
this cycle by encoding not what was confirmed but what was unexpected.

Every item in this echo must fail the passive-observation test: would a team tracking this
feature through normal project observation have found this? Items that survive belong in the
findings summary. Items that required active signal-gathering to surface belong here.

== SCHEMA CONTRACT ==============================================================

Declare before writing. Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering —
  missed this:                   "why a findings summary would not contain this item";
                                 name the mechanism, not just "needed investigation"]
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
  6.  NGT — Newcomer Gate Test (C-08 gate, runs per surprise as Step 4)
  7.  Check B — Portability Test (C-14 gate, runs per surprise as Step 3)
  8.  CAT — Coupled Authority Test (C-16 gate, runs per surprise as Step 5)
  9.  Label parity audit
  10. Field completion scan
  11. Patterns section

NOTE ON GATE ORDER: Gate execution order in Steps 3-5 is Check B → NGT → CAT. Pair
archetype declarations reflect mechanism relationships, not execution order. NGT+Check B
remains PREREQUISITE: the mechanism relationship is an input-dependency regardless of
which gate runs first.

Pair inspection — FOUR-FIELD SEQUENCE WITH VOCABULARY-SPECIFIED CONSISTENCY GATE:

  For each pair, in this sequence:
    Step 1 — Archetype:           [select from taxonomy below; canonical examples are
                                   template-complete — all four fields populated]
    Step 2 — CONSISTENCY GATE:    [apply vocabulary check for selected archetype:
                                     PREREQUISITE → "Does mechanism describe input-
                                       dependency? A's output = B's required input?" YES/NO.
                                     ESTABLISHES  → "Does mechanism describe property
                                       creation + one-way dependency?" YES/NO.
                                     AMPLIFIES    → "Does mechanism describe effectiveness
                                       scaling? A increases B's enforcement precision
                                       per surprise?" YES/NO.
                                     PARALLEL     → "Does mechanism describe independent-
                                       path operation? A and B enforce non-dependently,
                                       each sufficient alone?" YES/NO.
                                   If NO: return to Step 1.]
    Step 3 — Mechanism:           [analytical causal statement in vocabulary consistent
                                   with verified archetype]
    Step 4 — Composability-claim: [synthetic one-sentence assertion: what the mechanism
                                   implies for this pair's combined behavior; distinct
                                   from the mechanism description]

  Taxonomy with template-complete canonical pair examples:

    PREREQUISITE  — A's output is B's required input. Breaking A breaks B. Vocabulary
                    check: mechanism must describe input-dependency.
      > EXAMPLE: NGT is a PREREQUISITE for Check B.
        Archetype: PREREQUISITE
        Mechanism: NGT's newcomer-comprehension gate output is Check B's required
          input. A surprise failing NGT cannot pass Check B's three-component standalone
          extraction test (finding + unexpectedness + design consequence). No mechanism
          substitutes for newcomer-comprehension verification as Check B's input.
        Composability-claim: NGT and Check B compose without degradation. NGT's
          per-surprise accessibility enforcement produces the verified stranger-readable
          unit Check B requires; the forward dependency creates no competing demands
          on the surprise unit.

    ESTABLISHES   — A creates a property that B operates on. Directional, not feedback.
                    Vocabulary check: mechanism must describe property creation and
                    one-way dependency.
      > EXAMPLE: Check B ESTABLISHES the structural portability property that CAT enforces.
        Archetype: ESTABLISHES
        Mechanism: Check B verifies standalone derivability (finding + unexpectedness +
          consequence); CAT enforces that this verified-portable unit carries authoritative
          claim-voice. Removing Check B removes the portability substrate CAT operates on.
          No feedback from CAT to Check B.
        Composability-claim: Check B and CAT compose without degradation. The portability
          substrate Check B establishes is the precondition CAT requires; they enforce
          structurally distinct properties of the same surprise unit without competition.

    AMPLIFIES     — A increases the precision or strength of B's per-surprise enforcement.
                    Vocabulary check: mechanism must describe effectiveness scaling.
      > EXAMPLE: [fill in when an AMPLIFIES pair exists in this variation]
        Archetype: AMPLIFIES
        Mechanism: [...]
        Composability-claim: [...]

    PARALLEL      — A and B independently enforce the same sub-property from distinct paths.
                    Vocabulary check: mechanism must describe independent-path operation.
      > EXAMPLE: [fill in when a PARALLEL pair exists in this variation]
        Archetype: PARALLEL
        Mechanism: [...]
        Composability-claim: [...]

  ★ PRE-POPULATED BASELINE ENTRY (carry forward — mechanism-derived; execution order does
    not affect archetype classification):

  NGT + Check B: [BASELINE]
    Step 1 — Archetype: PREREQUISITE
    Step 2 — CONSISTENCY GATE: vocabulary class PREREQUISITE → input-dependency. Test:
              "Mechanism describes input-dependency: NGT's newcomer-comprehension output is
              Check B's required input." PASS. Confirmed: this relationship holds regardless
              of whether Check B executes before NGT in Steps 3-4.
    Step 3 — Mechanism: NGT's newcomer-comprehension gate output is Check B's required
              input. A surprise failing NGT cannot pass Check B's three-component standalone
              extraction test. Input-dependency holds in any compound configuration.

  Remaining required pairs:

  Schema manifest + Stranger-reader commitment:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 (counterfactual gate) + Rule 2 (claim-only voice):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + NGT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Word discipline (Check A) + Anti-hedging (Rule 2):
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Check B + CAT:
    Step 1 — Archetype: [compare against ESTABLISHES example above]
    Step 2 — CONSISTENCY GATE: [property creation/one-way dependency — YES/NO]
    Step 3 — Mechanism: [fill using canonical example as reference]
    Step 4 — Composability-claim: [fill using canonical example as reference]

  CAT + Rule 2:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Schema manifest + Label parity audit:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Label parity audit + Field completion scan:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Rule 1 + Check B:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Stranger-reader commitment + CAT:
    Step 1 — Archetype:
    Step 2 — CONSISTENCY GATE: [vocabulary check — YES/NO]
    Step 3 — Mechanism:
    Step 4 — Composability-claim:

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected using four-field
  format (Archetype → GATE → Mechanism → Composability-claim). CONSISTENCY GATE applied
  vocabulary check for each archetype. Canonical taxonomy examples are template-complete
  (all four fields populated). Pre-populated baseline (NGT+Check B, PREREQUISITE,
  input-dependency PASS, mechanism stated) carried forward — mechanism-derived, not
  execution-order-derived; gate sequence Check B → NGT → CAT does not alter pair
  classification. All mechanisms reinforce toward the single stranger-reader target.
  No conflicts found. Writing may begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal
    tracking. Ask: "Would a findings summary contain this?"
  Apply C-01 filter: cut anything that could appear unchanged in a standard research summary,
    findings doc, or project brief.
  Minimum 3 candidates required before proceeding to Step 2.

== STEP 2 — SCHEMA POPULATION ==================================================

  For each surviving candidate: populate all six schema fields.

  Check A — word discipline (runs inline per surprise):
    Count words from first field label through last field value.
    If any surprise exceeds 120 words: extract the claim, discard narrative scaffolding.
    Recount. Repeat until ≤120 words.

== STEP 3 — CHECK B (Portability Test) =========================================

  [C-14 gate — runs per surprise — discrete step before NGT; first gate in this variation]

  Gate design rationale:
    Criterion enforced: C-14 (per-surprise surprise portability)
    Primary motivation: Check B exists to enforce C-14 per surprise.
    Introduced in: V-05(R4) — before C-18 was written; designed as the primary
      portability enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove Check B.

  For each surprise individually:
    Extract this surprise as a standalone block.
    Can a stranger derive: (1) the finding, (2) why it was unexpected, (3) the design
    consequence? If any component is missing or requires external context: rewrite before NGT.

== STEP 4 — NGT (Newcomer Gate Test) ===========================================

  [C-08 gate — runs per surprise — discrete step after Check B, before CAT]

  Gate design rationale:
    Criterion enforced: C-08 (per-surprise newcomer accessibility)
    Primary motivation: NGT exists to enforce C-08 per surprise.
    Introduced in: V-01(R6) — before C-18 was written; designed as the primary
      newcomer-accessibility enforcement gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove NGT.

  For each surprise individually:
    Isolate this surprise. Read only this surprise.
    Can a new-hire with no prior project exposure understand this finding without
    consulting source signals or the rest of the echo? If no: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =======================================

  [C-16 gate — runs per surprise — discrete step after NGT; final per-surprise gate]

  Gate design rationale:
    Criterion enforced: C-16 (per-surprise claim-authority coupling)
    Primary motivation: CAT exists to enforce C-16 per surprise.
    Introduced in: V-04(R5) — before C-18 was written; designed as the primary
      authority-coupling gate, not installed to satisfy a rubric gap.
    Structural removal test: removing C-20 from the rubric does not remove CAT.

  For each surprise individually:
    (1) Direct claim? No prohibited constructs from Rule 2.
    (2) Stranger-accessible? Check B and NGT passed; CAT confirms coupling at authority level.
    Both YES required. If either NO: rewrite.

== STEP 6 — LABEL PARITY AUDIT =================================================

  Read the Name field across all surprises. Any generic label: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes. If any: write Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## V-05 — Combined: Tabular Manifest + Inertia Framing + C-30 (pre-populated baseline entry template completeness when C-27 present)

**Axes:** Output format (V-02 tabular manifest) + Inertia framing (V-03 preamble) + C-30
exploration. The pre-populated baseline row in the manifest table includes all four columns —
Archetype, CONSISTENCY GATE, Mechanism, AND Composability-claim — making the baseline entry
template-complete when C-27 is satisfied. This is the C-30 axis.

**C-30 hypothesis:** When C-27 is satisfied (Composability-claim field present in pair
inspection template) and C-28 is satisfied (pre-populated baseline entry exists), the pre-
populated baseline entry must include a Composability-claim to be template-complete. C-28's
current pass condition requires the baseline entry to carry archetype + mechanism + (if C-24)
consistency verification result. It does not require a Composability-claim. A baseline entry
that satisfies C-28 while omitting the Composability-claim (as in V-01 through V-04) creates
a structural gap parallel to the one C-29 closes for canonical taxonomy examples: the author
has a quality floor for the analytical layer (archetype + mechanism) but no baseline for the
synthetic layer (composability assertion). A template-complete pre-populated baseline entry
provides calibration for both layers. The structural relationship: C-30 is to C-28 as C-29 is
to C-25 — synthesis separation applied to the baseline layer rather than the illustration layer.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files until Step 10.

== INERTIA CONTEXT ==============================================================

Without this skill, a team that finishes signal gathering produces a findings summary.
The findings summary is the inertia path: it is accurate, it is expected, and it reports
what the team already suspected. It does not report the gap between what the team suspected
and what the signals actually revealed.

The echo is not a better findings summary. It is a different document. The findings summary
answers "what did we find?" The echo answers "what did we not expect to find?" The two
documents are written from the same signal artifacts and share no content: every item in
a findings summary could have been predicted before the investigation; every item in an echo
could not.

The institutional cost of the inertia path compounds across teams. Findings summaries travel
well: they are consulted, cited, and referenced. Echoes are the artifacts that do not get
written — not because teams lack the findings, but because the findings summary feels
complete. The surprises remain encoded in no artifact. The next team enters the investigation
with the same prior hypotheses and discovers the same surprises again.

Every candidate in Step 1 must fail: "A passive, attentive team tracking this feature would
have found this through normal project observation." Survivors of this test belong in the
findings summary. Only failures belong in the echo.

== SCHEMA CONTRACT ==============================================================

Declare before writing. Fields applied to every surprise — all required, none N/A:

  Name:                         [descriptive label — not "Finding 1" or "Surprise A"]
  Source:                       [namespace:skill or artifact path]
  Expected:                     [what the team assumed before gathering signals]
  Why passive observation       [specific mechanism that required active signal gathering —
  missed this:                   "why this item does not appear in the findings summary";
                                 name the gap mechanism, not just "needed investigation"]
  Design impact:                [one sentence minimum — how this changes design direction]
  Word count:                   [number]

== RULES ========================================================================

Rule 1 — Counterfactual gate:
  Each surprise must fail: "A passive, attentive team tracking this feature would have
  found this through normal observation." Items that survive passive observation belong in
  a findings summary, not an echo. The "Why passive observation missed this" field names
  why this item does not appear in the findings summary.

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

VOCABULARY REFERENCE — CONSISTENCY GATE constraint classes (apply per archetype):
  PREREQUISITE → input-dependency: mechanism must state that A's output is B's required input.
  ESTABLISHES  → property creation + one-way dependency: mechanism must state A creates a
                 property B operates on, without feedback from B to A.
  AMPLIFIES    → effectiveness scaling: mechanism must state A increases the precision or
                 strength of B's per-surprise enforcement.
  PARALLEL     → independent-path operation: mechanism must state A and B enforce from
                 non-dependent paths, each sufficient alone.

Pair inspection table — complete all rows before Step 1:

  Legend:
    ★EXAMPLE  — canonical template-complete illustration (all four columns populated)
    ★BASELINE — pre-classified and verified; carry forward without re-derivation;
                ALL FOUR COLUMNS POPULATED in this variation (C-30: baseline is template-
                complete — Composability-claim present because C-27 is satisfied)
    [fill]    — complete these rows; CONSISTENCY GATE column: apply vocabulary check,
                record constraint class + YES/NO verdict before writing Mechanism or
                Composability-claim; return to Archetype if verdict is NO

  | Pair                                   | Archetype    | CONSISTENCY GATE                                                                                   | Mechanism                                                                                                                                                                              | Composability-claim                                                                                                                                                                         |
  |----------------------------------------|--------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ★EXAMPLE PREREQUISITE: NGT + Check B   | PREREQUISITE | input-dependency. "NGT mechanism describes input-dependency — NGT's output is Check B's input?" PASS | NGT's newcomer-comprehension gate output is Check B's required input. A surprise failing NGT cannot pass Check B's three-component extraction test. No substitute for NGT's output.    | NGT and Check B compose without degradation. NGT's accessibility enforcement produces the verified unit Check B requires; the forward dependency creates no competing demands.              |
  | ★BASELINE: NGT + Check B               | PREREQUISITE | input-dependency PASS. "NGT's newcomer-comprehension output is Check B's required input." Confirmed. | NGT's newcomer-comprehension gate output is Check B's required input. A surprise failing NGT cannot pass Check B's three-component standalone extraction test.                         | NGT and Check B compose without degradation. NGT's per-surprise accessibility enforcement produces the verified stranger-readable unit Check B's portability test requires; the two gates form a forward pipeline with no competing demands on the shared surprise unit. |
  | ★EXAMPLE ESTABLISHES: Check B + CAT   | ESTABLISHES  | property creation + one-way dep. "Check B creates a property CAT operates on?" PASS                 | Check B verifies standalone derivability (finding + unexpectedness + consequence); CAT enforces authority on the verified-portable substrate. Removing Check B removes CAT's input.    | Check B and CAT compose without degradation. The portability substrate Check B establishes is the precondition CAT requires; they enforce structurally distinct properties without competition. |
  | Schema manifest + Stranger-reader      | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Rule 1 + Rule 2                        | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Rule 1 + NGT                           | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Check A + Rule 2                       | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Check B + CAT                          | ESTABLISHES  | [see ESTABLISHES example row]                                                                        | [fill using example row as reference]                                                                                                                                                  | [fill using example row as reference]                                                                                                                                                       |
  | CAT + Rule 2                           | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Schema manifest + Label parity audit   | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Label parity audit + Field scan        | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Rule 1 + Check B                       | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |
  | Stranger-reader + CAT                  | [select]     | [constraint class + YES/NO]                                                                          | [fill]                                                                                                                                                                                 | [fill]                                                                                                                                                                                      |

  For AMPLIFIES or PARALLEL pairs: add ★EXAMPLE rows above each first occurrence (all
  four columns populated).

  C-30 NOTE: The ★BASELINE row includes a Composability-claim. This makes the pre-populated
  baseline entry template-complete under C-27 (Composability-claim field present in template).
  V-01 through V-04 omit the Composability-claim from the BASELINE row — their pre-populated
  entries satisfy C-28 (archetype + GATE + mechanism) but are not template-complete under C-27.
  V-05 closes this gap: the BASELINE row demonstrates what a correct Composability-claim looks
  like for a PREREQUISITE pair, calibrating the author's synthesis claims against a verified
  canonical instance rather than from abstract definition alone.

  Declaration: "All 11 active mechanisms assessed. [N] pairs inspected in four-column tabular
  format (Archetype | GATE | Mechanism | Composability-claim). CONSISTENCY GATE column records
  vocabulary constraint class and YES/NO verdict per pair. ★EXAMPLE rows are template-complete
  (all four columns populated) for each archetype used — satisfying C-29. ★BASELINE row (NGT+
  Check B, PREREQUISITE) is template-complete: all four columns populated including Composability-
  claim — satisfying C-28 and introducing C-30 (baseline is template-complete under C-27). All
  mechanisms reinforce toward the single stranger-reader target. No conflicts found. Writing may
  begin."

  If any conflict found: resolve before proceeding.

== STEP 1 — CANDIDATE SELECTION ================================================

  Glob: simulations/{topic}/**
  Read all signal artifacts for this topic across all namespaces.
  List every candidate finding that was NOT expected before gathering signals.
  Apply Rule 1: cut anything a passive, attentive team would have found through normal tracking.
    Ask: "Would a findings summary contain this?" If yes: cut.
  Apply C-01 filter: cut anything that could appear unchanged in a findings doc or project brief.
  Minimum 3 candidates required before proceeding to Step 2.

== STEP 2 — SCHEMA POPULATION ==================================================

  For each surviving candidate: populate all six schema fields.
  For "Why passive observation missed this": name why this item does not appear in the
    findings summary — state the specific mechanism that required active signal gathering.

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
    consequence — without consulting the findings summary or source signals? If any
    component is missing: rewrite before CAT.

== STEP 5 — CAT (Coupled Authority Test) =========================================

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

  Read the Name field across all surprises. Any generic label: rename before Step 7.

== STEP 7 — FIELD COMPLETION SCAN ==============================================

  Read each field across all surprises:
    Name → Source → Expected → Why passive observation missed this → Design impact → Word count
  No N/A, no blank, no placeholder. Any gap: return to Step 2.

== STEP 8 — PATTERNS SECTION ===================================================

  Examine all surprises for shared root causes. If any: write Patterns section. If none: omit.

== STEP 9 — WORD COUNT FINAL CHECK =============================================

  Full echo must not exceed 800 words. If over: extract and cut.

== STEP 10 — WRITE ARTIFACT ====================================================

  Write to: simulations/{topic}/{topic}-echo-{date}.md
```

---

## Predicted Score Map Summary

| Variant | Base | Proven | C-26 | C-27 | C-28 | C-29 | C-30 | Total | Capped |
|---------|------|--------|------|------|------|------|------|-------|--------|
| V-01    | 75   | 24     | 1    | 1    | 1    | 1    | 0    | 103   | 100    |
| V-02    | 75   | 24     | 1    | 1    | 1    | 1    | 0    | 103   | 100    |
| V-03    | 75   | 24     | 1    | 1    | 1    | 1    | 0    | 103   | 100    |
| V-04    | 75   | 24     | 1    | 1    | 1    | 1    | 0    | 103   | 100    |
| V-05    | 75   | 24     | 1    | 1    | 1    | 1    | 1    | 104   | 100    |

**Differentiating dimension:** C-30 — pre-populated baseline entry template completeness
(Composability-claim present in baseline when C-27 is satisfied). V-01 through V-04 FAIL C-30
(baseline row has Archetype + GATE + Mechanism only). V-05 PASS C-30 (baseline row has all
four fields including Composability-claim).

**Enabling conditions for v12 rubric:** If C-26, C-27, C-28 PASS uniformly across all five
R12 variations, combined with prior round evidence (R10+R11 for C-26; R10+R11 for C-27; R10+
R11 for C-28), all three meet the two-round confirmed-round threshold for Proven promotion.
C-29 first confirmed round is R12; second confirmation required in R13 for Proven promotion.
C-30 introduced in R12 V-05 only; two rounds of confirmation required.

**C-30 structural chain:**
- C-25: taxonomy illustration (Proven R10+R11)
- C-27: synthesis claim field in live pair inspection (targeting Proven R12)
- C-29: taxonomy illustrations template-complete under C-27 (targeting Proven R13)
- C-28: pre-populated baseline entry (targeting Proven R12)
- C-30: pre-populated baseline entry template-complete under C-27 — C-29's structural
  parallel applied to the baseline layer rather than the illustration layer

**Axis independence note:** V-01 tests whether pair archetype classifications are mechanism-
derived (independent of execution order) or order-derived. If C-28 PASS and C-29 PASS in
V-01 despite the reversed gate sequence, this confirms that manifest pair inspection quality
is a structural property of mechanism relationships, not a function of which gate runs first
in the process steps. V-02 and V-05 test whether tabular format is a structurally equivalent
presentation for all manifest criteria (C-19, C-21, C-23, C-24, C-25, C-26, C-27, C-28,
C-29, C-30) — format should not affect criterion satisfaction. V-03 and V-04 test whether
inertia framing composes without structural friction against the manifest criteria and gate
sequence respectively.
