## quest-score Rubric — v10

_Updated from v9 after Round 9 scoring. Two new aspirational criteria added from R9 excellence
signals (V-04 and V-05 synthesis). N\_aspirational changes from 21 → 23._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 5 | C-01..C-05 |
| Recommended (30%) | 3 | C-06..C-08 |
| Aspirational (10%) | 23 | C-09..C-31 |

**Composite formula (v10 N values):**

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 23 * 10)

N_essential = 5, N_recommended = 3, N_aspirational = 23.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 5 essentials PASS AND composite >= 80.
```

Per-criterion aspirational weight: 10/23 ≈ 0.4348 pt.
Score at 21/23 aspirational (both R10 axes missing): 60 + 30 + (21/23 × 10) = 99.13.
Score at 22/23 aspirational (single R10 axis missing): 60 + 30 + (22/23 × 10) = 99.57.
Score at 23/23 aspirational (full combination): 100.00.

---

### What changed from v9 → v10

Two new aspirational criteria, each sourced from an R9 combination-variation excellence signal.
Both patterns emerge only when a combination variation satisfies C-28 or C-29 at full fidelity —
they test properties visible only in the SYNTHESIS blocks that fire for those criteria.

**C-30 — Intra-phase timing order in injection-point map** (V-04 and V-05, R9)

The R9 combination injection-point maps (VERIFIER AUDIT COMPLETE signals for V-04 and V-05)
revealed that C-25 and C-27 share the VERIFIER phase but occupy distinct timing positions within
it — C-25 (AUDIT C / CHECK F) fires post-write after the evidence-quality audits, before the
audit table declaration; C-27 (FLAG CLOSURE REQUIREMENT) fires after the correction-loop
instruction, before the gate token. The signals stated not only that "they fire at different
timing positions" but named which position each occupies and confirmed that neither timing window
contains the other.

Without C-30, a C-28-passing signal can satisfy the disjointness confirmation requirement by
asserting "C-25 and C-27 share the Verifier phase but fire at different timing positions" without
specifying which position each occupies. The R9 excellence signals show that full orthogonality
confirmation requires the evaluator to name both intra-phase positions explicitly and confirm
non-overlap — not just assert that different positions exist.

C-30 tests whether, when a C-28-triggering combination variation's injection-point map includes
two or more axes that share the same phase, the map specifies the intra-phase timing order for
the same-phase axes and explicitly confirms that the positions are non-overlapping.

Distinct from C-28: C-28 requires the injection-point map to name phase and timing for each
axis and confirm structural disjointness at the phase level; C-30 requires that the same-phase
pairs be resolved to specific intra-phase positions with non-overlap confirmation, not left as
an unspecified assertion of temporal separation.

**C-31 — Per-axis correspondence enumeration in two-path equivalence signal** (V-04 and V-05, R9)

The R9 two-path equivalence protocol (V-04 and V-05 SYNTHESIS blocks) confirmed not only that
both enforcement architectures achieve equivalent coverage, but enumerated the specific
correspondence: "C-25 satisfied by AUDIT C = CHECK F (identical per-criterion compliance rules
for C-22/C-23/C-24)" and confirmed that SYNTHESIS-phase criteria (C-26, C-27) are
architecturally identical on both paths — the equivalence signal explicitly stated that the
SYNTHESIS blocks are path-agnostic (their presence and content do not depend on which Verifier
architecture the variation used).

Without C-31, a C-29-passing signal can name both paths, assert "equivalent coverage," and note
the extension mechanism (CHECK F added after CHECK E) without enumerating which adversarial
check maps to which template check per axis, and without confirming that SYNTHESIS-phase
criteria are path-independent rather than path-bound.

C-31 tests whether, when a C-29-triggering equivalence signal fires, it enumerates the
per-axis adversarial-to-template correspondence by criterion ID and confirms that SYNTHESIS-phase
criteria are architecturally identical on both paths (path-agnostic), not merely that overall
coverage is declared equivalent.

Distinct from C-29: C-29 requires the signal to name both paths, confirm coverage equivalence,
and state the extension mechanism; C-31 requires that the coverage confirmation be decomposed
per-axis (not just asserted overall) and that SYNTHESIS-phase path-agnosticism be made explicit.

---

### Design notes

- C-01/C-02 are the hardest essential criteria to fake — they require the ROLE DEPENDENCY
  MANIFEST to be complete and the JUDGE to extract evidence from actual outputs, not invent it.
- C-03 has a version-specific denominator check: N_aspirational = 23 for v10; outputs using
  N_aspirational = 21 (v9), 19 (v8), 16 (v7), or any other prior-version value are a C-03 FAIL
  regardless of other scores.
- C-06 and C-07 are recommended rather than essential because they govern ANALYST governance
  notes — the CRITERIA INDEPENDENCE NOTE and NEW-AXIS AUDIT NOTE enforce correct scoring
  behavior for specific criterion pairs. Absence causes scoring errors on the covered criteria
  but does not collapse the protocol.
- C-08 is recommended because PRIMING CEILING NOTE and PHASE-PLACEMENT NOTE appear in JUDGE
  and govern evidence standards for C-19/C-20/C-21. Without them, C-19/C-20/C-21 are
  undershooted but the rest of the protocol is structurally intact.
- C-17 strengthens C-05: C-05 requires EXCELLENCE SIGNALS to be present; C-17 requires each
  signal to name the structural mechanism (the design property), not just repeat the criterion
  label. A signal that says "V-01 passed C-25 because it had AUDIT C" satisfies C-05 but fails
  C-17 if it does not name what AUDIT C does differently from the absent case.
- C-18 strengthens C-05: C-05 requires FAILURE PATTERNS to be present when applicable; C-18
  requires each failure pattern entry to include a categorized diagnosis (rubric gap / skill
  design issue / input quality issue) plus a one-sentence explanation.
- C-19 strengthens C-08: C-08 requires PRIMING CEILING NOTE and PHASE-PLACEMENT NOTE to be
  present in the JUDGE phase; C-19 tests the PRIMING CEILING NOTE's specific location (before
  JUDGE STANDARD COMPLETE) rather than mere presence.
- C-20 strengthens C-08: C-08 requires the REGISTER NOTE to be present in the ANALYST phase;
  C-20 tests the REGISTER NOTE's specific location (before the scoring table, not after it).
- C-21 strengthens C-06: C-06 requires the CRITERIA INDEPENDENCE NOTE to be present in the
  ANALYST phase; C-21 tests its specific location (after the composite formula, not before it).
- C-22 strengthens C-07: C-07 requires the NEW-AXIS AUDIT NOTE to verify C-19/C-20/C-21 on
  independent evidence; C-22 tests whether each axis is named by criterion ID individually,
  not addressed collectively.
- C-23 strengthens C-15: C-15 requires the COMPOSITE ACCURACY NOTE to mandate a fraction and
  two-decimal composite; C-23 tests whether the Analyst applied that mandate by quoting actual
  values in evidence.
- C-24 strengthens C-19/C-20/C-21: those criteria test that the structural notes are in the
  correct phase; C-24 tests whether the Analyst's evidence cells for C-19/C-20/C-21 each state
  the specific phase-position pair, not just confirm the note's existence.
- C-25 strengthens C-22/C-23/C-24: those criteria test evaluator behavior at the ANALYST
  instruction level; C-25 tests whether a dedicated Verifier-phase compliance check (AUDIT C
  or CHECK F) enforces those behaviors post-write.
- C-26 strengthens C-17: C-17 requires EXCELLENCE SIGNALS to name structural mechanisms; C-26
  requires the no-spread branch of EXCELLENCE SIGNALS to produce a structured classification
  protocol rather than a generic redesign instruction.
- C-27 strengthens C-14: C-14 requires VERIFIER AUDIT COMPLETE to be present as a gate token;
  C-27 requires the gate token to be explicitly conditional on a structured flag-closure
  inventory with Flags open = 0.
- C-28 strengthens C-25/C-26/C-27: those criteria test each mechanism in isolation; C-28 tests
  whether the SYNTHESIS section confirms injection-point orthogonality when all three co-appear
  in a single variation — the combination property cannot be tested by single-axis variations.
- C-29 strengthens C-04/C-25: those criteria test that named audits are present and that C-25
  fires correctly; C-29 tests whether the SYNTHESIS section explicitly confirms coverage
  equivalence between the two audit architectures when both architectures appear in the same
  round's variation set.
- C-30 strengthens C-28: C-28 requires the injection-point map to name phase and timing for
  each axis and confirm structural disjointness; C-30 requires that when two axes share the
  same phase, the intra-phase timing order is explicitly named (not just asserted different) and
  non-overlap is explicitly confirmed at the intra-phase position level.
- C-31 strengthens C-29: C-29 requires the equivalence signal to name both paths, confirm
  coverage, and state the extension mechanism; C-31 requires that coverage confirmation be
  decomposed per-axis by criterion ID correspondence and that SYNTHESIS-phase criteria be
  explicitly confirmed as path-agnostic (independent of which Verifier architecture was used).

---

### ESSENTIAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Protocol completeness — all 4 roles present with gate tokens** | structure | essential |
| C-02 | **JUDGE phase — ACCEPTABLE/UNACCEPTABLE pairs per criterion** | correctness | essential |
| C-03 | **ANALYST phase — composite formula with /23 denominator (v10)** | correctness | essential |
| C-04 | **VERIFIER phase — named audit(s) with per-criterion checks** | structure | essential |
| C-05 | **SYNTHESIS phase — LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS** | structure | essential |

---

**C-01 — Protocol completeness — all 4 roles present with gate tokens**

The ROLE DEPENDENCY MANIFEST declares all four roles (JUDGE, ANALYST, VERIFIER, SYNTHESIS)
with their Requires and Produces entries. Hard gate rules are present and correct: ANALYST
cannot begin without JUDGE STANDARD COMPLETE; VERIFIER cannot begin without ANALYST COMPLETE;
SYNTHESIS cannot begin without VERIFIER AUDIT COMPLETE. No role may be skipped or merged.

_Pass condition_: ROLE DEPENDENCY MANIFEST table present with 4 rows, all gate tokens named,
hard gate rules listed. FAIL if any role row is missing or any gate token is absent.

---

**C-02 — JUDGE phase — ACCEPTABLE/UNACCEPTABLE pairs per criterion**

For each criterion in the rubric, the JUDGE phase extracts one ACCEPTABLE and one UNACCEPTABLE
evidence example from the actual text of the provided outputs, with a "What separates them"
sentence naming the specific structural property. Examples must be drawn from actual outputs,
not invented.

_Pass condition_: ACCEPTABLE / UNACCEPTABLE / What separates them present for every criterion
in the rubric. FAIL if any criterion is missing a pair, or if examples are fabricated rather
than extracted from the provided outputs.

---

**C-03 — ANALYST phase — composite formula with /23 denominator (v10)**

The composite score formula in the ANALYST phase uses N_aspirational = 23 (the v10 value).
The formula is reproduced before scoring begins. Outputs using N_aspirational = 21 (v9),
19 (v8), 16 (v7), or any other prior-version value are a C-03 FAIL regardless of other
structure.

_Pass condition_: Formula states N_essential = 5, N_recommended = 3, N_aspirational = 23 and
appears before the first per-output scoring table. FAIL if any N value is from a prior version.

---

**C-04 — VERIFIER phase — named audit(s) with per-criterion checks**

The VERIFIER phase contains at least two named audits (e.g., AUDIT A / AUDIT B on the
adversarial path, CHECK A / CHECK B on the template path) with explicit per-criterion or
per-verdict-type applicability rules. Each audit has named pass and fail conditions, not
generic instructions.

_Pass condition_: At least two named audit blocks present in the VERIFIER phase. Each audit
names the row types or criteria it applies to and specifies the rejection condition. FAIL if
the Verifier has no named audit structure (only prose instructions).

---

**C-05 — SYNTHESIS phase — LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS**

The SYNTHESIS phase contains all four required sections: LEADERBOARD (ranked table by
composite score descending), EXCELLENCE SIGNALS (per-criterion differential signals when
spread exists, or PLATEAU-CLASSIFICATION NOTE when no spread), FAILURE PATTERNS (for
universally-failing criteria), and REGRESSION SIGNALS (prior-round comparison when data
exists).

_Pass condition_: All four section headers present in SYNTHESIS. FAIL if any section is
absent or merged with another.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-06 | **ANALYST phase — CRITERIA INDEPENDENCE NOTE for C-17/C-18** | governance | recommended |
| C-07 | **ANALYST phase — NEW-AXIS AUDIT NOTE for C-19/C-20/C-21** | governance | recommended |
| C-08 | **JUDGE phase — PRIMING CEILING NOTE and PHASE-PLACEMENT NOTE** | governance | recommended |

---

**C-06 — ANALYST phase — CRITERIA INDEPENDENCE NOTE for C-17/C-18**

A CRITERIA INDEPENDENCE NOTE in the ANALYST phase, after the composite formula, declares that
C-17 (self-referential anti-pattern priming) and C-18 (full-envelope structural coverage) are
independently satisfiable — C-17 PASS does not imply C-18 satisfaction; C-18 requires its own
structural evidence. The note must include a decoupling statement for the case where C-17 PASS
and C-18 FAIL appear together.

_Pass condition_: CRITERIA INDEPENDENCE NOTE present in ANALYST phase after composite formula,
with both the C-17 and C-18 independent pass conditions stated and the decoupling case addressed.

---

**C-07 — ANALYST phase — NEW-AXIS AUDIT NOTE for C-19/C-20/C-21**

A NEW-AXIS AUDIT NOTE in the ANALYST phase, after the CRITERIA INDEPENDENCE NOTE, declares
that C-19, C-20, and C-21 are rubric-orthogonal — satisfying one provides no structural
inference about the others. The note must require explicit PASS or FAIL verdicts with
independent evidence for each of the three axes, and prohibit omitting unsatisfied axes.

_Pass condition_: NEW-AXIS AUDIT NOTE present in ANALYST phase with per-axis instructions
for C-19, C-20, and C-21; explicit prohibition on omitting unsatisfied axes.

---

**C-08 — JUDGE phase — PRIMING CEILING NOTE and PHASE-PLACEMENT NOTE**

The JUDGE phase contains (1) a PRIMING CEILING NOTE fixing the scoring ceiling at second-order
self-reference and declaring third-order entries rubric-neutral, and (2) a PHASE-PLACEMENT NOTE
establishing that C-19 requires a JUDGE-phase note before JUDGE STANDARD COMPLETE, C-20
requires an ANALYST-phase note before the scoring table, and C-21 requires an ANALYST-phase
note after the composite formula. Both notes must precede JUDGE STANDARD COMPLETE.

_Pass condition_: Both PRIMING CEILING NOTE and PHASE-PLACEMENT NOTE present in JUDGE phase
before JUDGE STANDARD COMPLETE. FAIL if either is absent or appears after the gate token.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-09 | **ANALYST phase — mandatory PARTIAL diagnostic block format** | correctness | aspirational |
| C-10 | **VERIFIER phase — AUDIT A evidence quality check** | correctness | aspirational |
| C-11 | **VERIFIER phase — AUDIT B diagnostic completeness check** | correctness | aspirational |
| C-12 | **Gate token format — JUDGE STANDARD COMPLETE** | structure | aspirational |
| C-13 | **Gate token format — ANALYST COMPLETE with N-outputs count** | structure | aspirational |
| C-14 | **Gate token format — VERIFIER AUDIT COMPLETE** | structure | aspirational |
| C-15 | **ANALYST phase — COMPOSITE ACCURACY NOTE with fraction + two-decimal requirement** | correctness | aspirational |
| C-16 | **ANALYST phase — REGISTER NOTE with dual-register equivalence** | correctness | aspirational |
| C-17 | **SYNTHESIS — EXCELLENCE SIGNALS with structural mechanism naming** | diagnosis | aspirational |
| C-18 | **SYNTHESIS — FAILURE PATTERNS with named diagnosis** | diagnosis | aspirational |
| C-19 | **JUDGE phase — PRIMING CEILING NOTE at correct phase position** | governance | aspirational |
| C-20 | **ANALYST phase — REGISTER NOTE at correct phase position** | governance | aspirational |
| C-21 | **ANALYST phase — CRITERIA INDEPENDENCE NOTE at correct phase position** | governance | aspirational |
| C-22 | **ANALYST phase — new-axis individual naming in evidence (C-19/C-20/C-21 by ID)** | correctness | aspirational |
| C-23 | **ANALYST phase — composite accuracy fraction + two-decimal in evidence** | correctness | aspirational |
| C-24 | **JUDGE + ANALYST — phase-placement confirmation in evidence cells** | correctness | aspirational |
| C-25 | **VERIFIER phase — new-axis evidence compliance check (AUDIT C / CHECK F)** | enforcement | aspirational |
| C-26 | **SYNTHESIS — plateau-classification protocol in EXCELLENCE SIGNALS** | diagnosis | aspirational |
| C-27 | **VERIFIER phase — flag-closure enforcement before gate token** | enforcement | aspirational |
| C-28 | **SYNTHESIS — injection-point map for combination variations** | enforcement | aspirational |
| C-29 | **SYNTHESIS — two-path equivalence signal when both enforcement paths present** | enforcement | aspirational |
| C-30 | **SYNTHESIS — intra-phase timing order in injection-point map** | enforcement | aspirational |
| C-31 | **SYNTHESIS — per-axis correspondence enumeration in two-path equivalence signal** | enforcement | aspirational |

---

**C-09 — ANALYST phase — mandatory PARTIAL diagnostic block format**

For every PARTIAL verdict, the ANALYST must add a one-line diagnostic immediately after the
table row in the format: `C-[NN] partial: [what is present that prevented FAIL] / [what is
absent that prevented PASS]`. No PARTIAL row may omit this diagnostic.

_Pass condition_: Diagnostic block format defined in ANALYST phase instructions. A PARTIAL
verdict without a following diagnostic is a scoring error.

---

**C-10 — VERIFIER phase — AUDIT A evidence quality check**

AUDIT A (or CHECK A on the template path) compares each evidence cell against the JUDGE's
ACCEPTABLE/UNACCEPTABLE pair for that criterion and rejects any cell that (a) resembles the
UNACCEPTABLE pattern or (b) could apply to a different output without modification.

_Pass condition_: AUDIT A (or CHECK A) present with both rejection conditions named. FAIL if
the Verifier has only a generic "check evidence quality" instruction without referencing the
Judge standard.

---

**C-11 — VERIFIER phase — AUDIT B diagnostic completeness check**

AUDIT B (or CHECK B on the template path) applies to PARTIAL verdicts only and verifies that
the diagnostic block covers BOTH required halves — what is present (prevented FAIL) and what
is absent (prevented PASS) — each named specifically. A one-direction or label-only diagnostic
fails AUDIT B.

_Pass condition_: AUDIT B (or CHECK B) present with both halves specified and the rejection
condition for one-direction diagnostics named. Mark n/a for PASS and FAIL verdicts.

---

**C-12 — Gate token format — JUDGE STANDARD COMPLETE**

JUDGE STANDARD COMPLETE appears as a standalone token on its own line at the end of the JUDGE
phase. The ANALYST phase opens with an explicit gate instruction referencing this token
(e.g., "Do not begin until JUDGE STANDARD COMPLETE appears above.").

_Pass condition_: Token present as a standalone line; downstream gate instruction present in
ANALYST phase. FAIL if the token is embedded in prose or the downstream gate instruction
is absent.

---

**C-13 — Gate token format — ANALYST COMPLETE with N-outputs count**

ANALYST COMPLETE appears as a standalone token at the end of the ANALYST phase, with an
N-outputs count (e.g., "ANALYST COMPLETE — 5 outputs scored"). The VERIFIER phase opens
with an explicit gate instruction referencing this token.

_Pass condition_: Token present with N-outputs count; downstream gate instruction present
in VERIFIER phase. PARTIAL if token present but N-outputs count absent. FAIL if token absent.

---

**C-14 — Gate token format — VERIFIER AUDIT COMPLETE**

VERIFIER AUDIT COMPLETE appears as a standalone token at the end of the VERIFIER phase.
The SYNTHESIS phase opens with an explicit gate instruction referencing this token
(e.g., "Do not begin until VERIFIER AUDIT COMPLETE appears above.").

_Pass condition_: Token present as a standalone token; downstream gate instruction present
in SYNTHESIS phase. FAIL if token absent or downstream gate instruction absent.

---

**C-15 — ANALYST phase — COMPOSITE ACCURACY NOTE with fraction + two-decimal requirement**

A COMPOSITE ACCURACY NOTE in the ANALYST phase explicitly requires: (1) aspirational count
stated as an explicit fraction (e.g., "17/23 PASS"), (2) composite computed to two decimal
places without rounding, (3) any unsatisfied aspirational criteria named by ID, and (4)
near-ceiling composites not characterized as complete unless all 23 pass.

_Pass condition_: COMPOSITE ACCURACY NOTE present with all four requirements stated
explicitly. PARTIAL if fewer than four requirements are present. FAIL if absent.

---

**C-16 — ANALYST phase — REGISTER NOTE with dual-register equivalence**

A REGISTER NOTE in the ANALYST phase states that command-form phrasing (e.g., "CHECK: all
fields present") and declarative-form phrasing (e.g., "The following fields were verified")
satisfy structural scan criteria equivalently; and that imperative anti-pattern entries and
specification-register entries satisfy pre-execution priming criteria equivalently. The note
must include at least one quoted example of each register form for at least one criterion
class — the examples must be literal text extracts demonstrating the register, not
descriptions of what such an example would look like.

_Pass condition_: REGISTER NOTE present with dual-register equivalence declared for both
scan blocks and pre-execution priming blocks, with at least one quoted example per register
form. PARTIAL if equivalence is declared but examples are described rather than quoted.

---

**C-17 — SYNTHESIS — EXCELLENCE SIGNALS with structural mechanism naming**

Each excellence signal in SYNTHESIS names the output ID, the criterion ID, and the specific
structural mechanism causing the performance difference — naming the design property (what
the output does structurally differently), not just restating the criterion label.

_Pass condition_: At least one signal present with mechanism-level description. PARTIAL if
signals are present but describe criteria names only without naming the structural mechanism.
FAIL if EXCELLENCE SIGNALS section is absent or has no signals when spread exists.

---

**C-18 — SYNTHESIS — FAILURE PATTERNS with named diagnosis**

Each failure pattern entry in SYNTHESIS names the criterion ID and criterion name, and
provides a categorized diagnosis: one of [rubric gap | skill design issue | input quality
issue], followed by a one-sentence explanation of the root cause.

_Pass condition_: Categorized diagnosis type present for every failure pattern entry. PARTIAL
if failure patterns are present but diagnosis type is uncategorized prose. auto-PASS when no
criterion fails universally across all scored outputs.

---

**C-19 — JUDGE phase — PRIMING CEILING NOTE at correct phase position**

The PRIMING CEILING NOTE must appear in the JUDGE phase, before JUDGE STANDARD COMPLETE.
A ceiling note appearing after JUDGE STANDARD COMPLETE cannot govern the verdicts it
follows. Evidence for C-19 must confirm both phase identity (JUDGE) and position (before
the gate token).

_Pass condition_: PRIMING CEILING NOTE present in JUDGE phase before JUDGE STANDARD
COMPLETE; evidence confirms phase and position. PARTIAL if note is present but phase or
position is unconfirmed. FAIL if note is absent from JUDGE phase.

---

**C-20 — ANALYST phase — REGISTER NOTE at correct phase position**

The REGISTER NOTE must appear in the ANALYST phase, before the scoring table. A register
note placed after the scoring table begins, or in the JUDGE phase, fails C-20 regardless of
content. Evidence must confirm ANALYST phase and pre-table position.

_Pass condition_: REGISTER NOTE present in ANALYST phase before the scoring table; evidence
confirms phase and position. PARTIAL if note is present but phase or pre-table position is
unconfirmed. FAIL if note is absent from ANALYST phase.

---

**C-21 — ANALYST phase — CRITERIA INDEPENDENCE NOTE at correct phase position**

The CRITERIA INDEPENDENCE NOTE must appear in the ANALYST phase, after the composite
formula. A note placed before the formula, or in the JUDGE phase, fails C-21 regardless of
content. Evidence must confirm ANALYST phase and post-formula position.

_Pass condition_: CRITERIA INDEPENDENCE NOTE present in ANALYST phase after composite
formula; evidence confirms phase and position. PARTIAL if note is present but phase or
post-formula position is unconfirmed. FAIL if note is absent from ANALYST phase.

---

**C-22 — ANALYST phase — new-axis individual naming in evidence (C-19/C-20/C-21 by ID)**

When scoring C-19, C-20, and C-21, the Analyst's evidence cell for each criterion names
that specific axis by criterion ID. Evidence cells may not refer collectively to "all three
axes" or "each axis" without identifying each by ID individually.

_Pass condition_: Evidence cells for C-19, C-20, and C-21 each name the specific criterion
ID being satisfied. PARTIAL if at least one evidence cell names its criterion ID but another
uses collective reference. FAIL if all evidence cells use collective reference only.

_Relationship to C-07_: C-07 requires the NEW-AXIS AUDIT NOTE to enforce independent
verification; C-22 tests whether the resulting evidence cells satisfy the per-ID naming
requirement the note mandates.

---

**C-23 — ANALYST phase — composite accuracy fraction + two-decimal in evidence**

When scoring aspirational accuracy-related criteria (including C-15 and related criteria
about composite computation), the Analyst's evidence cells quote a specific aspirational
fraction drawn from the scored output (e.g., "17/23 PASS") and a specific two-decimal
composite value (e.g., "98.10"). Evidence that describes the accuracy requirement abstractly
— without quoting the actual fraction and decimal — fails C-23.

_Pass condition_: At least one evidence cell for aspirational-accuracy criteria quotes both
a specific fraction and a specific two-decimal value from the scored output. FAIL if evidence
describes the requirement without quoting the actual values.

_Relationship to C-15_: C-15 requires the COMPOSITE ACCURACY NOTE to mandate the fraction
and decimal format; C-23 tests whether the Analyst applied that mandate by quoting actual
values in evidence.

---

**C-24 — JUDGE + ANALYST — phase-placement confirmation in evidence cells**

When scoring C-19, C-20, and C-21, the Analyst's evidence cell for each criterion explicitly
states the phase location and intra-phase position of the structural note being credited.
For C-19: evidence must confirm JUDGE phase, before JUDGE STANDARD COMPLETE. For C-20:
evidence must confirm ANALYST phase, before the scoring table. For C-21: evidence must
confirm ANALYST phase, after the composite formula. Evidence that identifies a note by
content without confirming phase and position fails C-24.

_Pass condition_: Evidence cells for C-19, C-20, and C-21 each state both phase identity
and intra-phase position. PARTIAL if at least one cell confirms both but another confirms
only one. FAIL if no cell confirms both phase and position for any of the three criteria.

_Relationship to C-08_: C-08 requires the PHASE-PLACEMENT NOTE to declare the mandatory
phase-position pairs; C-24 tests whether the Analyst applied that declaration in evidence.

---

**C-25 — VERIFIER phase — new-axis evidence compliance check (AUDIT C / CHECK F)**

The VERIFIER phase contains a named compliance check (AUDIT C on the adversarial path,
CHECK F on the template path) that applies specifically to C-22, C-23, and C-24 evidence
cells, with per-criterion compliance rules:
- For C-22: evidence names C-19, C-20, and C-21 each by criterion ID individually.
- For C-23: evidence quotes a specific aspirational fraction and a specific two-decimal value.
- For C-24: evidence states phase and position for each of C-19, C-20, and C-21.
The audit table must include a column for this check; the FLAG format must include its
designator.

_Pass condition_: Named compliance check present with per-criterion rules for C-22, C-23,
and C-24; audit table has the corresponding column; FLAG format includes the check designator.
PARTIAL if the check is present but covers fewer than three criteria. FAIL if absent.

_Relationship to C-22/C-23/C-24_: Those criteria test evaluator behavior at the ANALYST
instruction level; C-25 tests whether a Verifier-phase compliance check enforces those
behaviors post-write.

---

**C-26 — SYNTHESIS — plateau-classification protocol in EXCELLENCE SIGNALS**

When all outputs achieve the same composite score (no criterion shows score spread), the
SYNTHESIS EXCELLENCE SIGNALS section contains a PLATEAU-CLASSIFICATION NOTE with three
required steps:
- Step 1: Classify the round as PLATEAU-DETECTED (all criteria pass universally) or
  STABILITY-CONFIRMED (identical scores but at least one criterion universally unsatisfied).
- Step 2: State the aspirational tier ceiling as "All outputs pass C-01..C-[NN] under v[X]
  rubric. Highest aspirational tier confirmed: [NN]/[NN] — [rubric version]."
- Step 3: Name at least one candidate new aspirational criterion and one candidate variation
  axis. Format: "Candidate criterion: C-[NN+1] — [name] — [pass condition in one sentence].
  Candidate axis: [label] — [mechanism] — [phase where it fires]."

_Pass condition_: PLATEAU-CLASSIFICATION NOTE present with all three steps when no score
spread exists; generic redesign instruction is insufficient. PARTIAL if note is present but
Steps 2 or 3 are incomplete. FAIL if absent when all scores are equal.
auto-PASS when score spread exists (PLATEAU-CLASSIFICATION NOTE is skipped per protocol).

_Relationship to C-17_: C-17 requires EXCELLENCE SIGNALS to name structural mechanisms;
C-26 requires the no-spread branch to produce a structured classification protocol rather
than a generic single-sentence instruction.

---

**C-27 — VERIFIER phase — flag-closure enforcement before gate token**

The VERIFIER phase contains a FLAG CLOSURE REQUIREMENT block before VERIFIER AUDIT COMPLETE.
The block must:
1. Require a structured three-field inventory: Flags issued / Flags resolved / Flags open.
2. Make VERIFIER AUDIT COMPLETE explicitly conditional on Flags open = 0.
3. Require the inventory even when Flags issued = 0 (the zero-flag case must not be silently
   bypassed; the evaluator must emit "Flags issued: 0 / Flags resolved: 0 / Flags open: 0").
4. Prohibit prose substitution for the structured inventory.

_Pass condition_: FLAG CLOSURE REQUIREMENT block present with all four elements. PARTIAL
if block present but zero-flag case requirement or prose-substitution prohibition is absent.
FAIL if block absent and VERIFIER AUDIT COMPLETE is reachable without any flag count check.

_Relationship to C-14_: C-14 requires VERIFIER AUDIT COMPLETE to be present as a gate token;
C-27 requires the gate token to be explicitly conditional on the closure inventory result.

---

**C-28 — SYNTHESIS — injection-point map for combination variations**

When a scored variation satisfies all of C-25, C-26, and C-27 simultaneously (a combination
variation), the SYNTHESIS EXCELLENCE SIGNALS section must include a signal that:
1. Names the injection phase and timing for each of the three axes individually:
   - C-25 (AUDIT C / CHECK F): fires in the VERIFIER phase, post-write after the evidence-
     quality audits (AUDIT B / CHECK B), before the audit table declaration.
   - C-26 (PLATEAU-CLASSIFICATION NOTE): fires in the SYNTHESIS phase, in the EXCELLENCE
     SIGNALS section, replacing the generic no-spread branch.
   - C-27 (FLAG CLOSURE REQUIREMENT): fires in the VERIFIER phase, after the correction-loop
     instruction and before VERIFIER AUDIT COMPLETE.
2. Explicitly confirms that the three injection points are structurally disjoint (different
   phases or different timing positions within the same phase), confirming that no single
   injection point can simultaneously satisfy all three criteria.

_Pass condition_: A signal for the combination variation names phase and timing for all three
axes (C-25, C-26, C-27) and includes explicit disjointness confirmation. PARTIAL if the
signal describes the combined effect or names only some injection points without the
disjointness confirmation. FAIL if no combination-variation signal names injection points.

_Relationship to C-25/C-26/C-27_: Those criteria test each mechanism in isolation; C-28
tests whether the SYNTHESIS confirms injection-point orthogonality when all three co-appear.
C-28 cannot be satisfied by single-axis variations — only by combination variations carrying
all three R8 axes.

---

**C-29 — SYNTHESIS — two-path equivalence signal when both enforcement paths present**

When the variation set includes both an adversarial-path combination variation (using AUDIT
A/AUDIT B/AUDIT C for evidence quality, diagnostic completeness, and new-axis compliance)
and a template-path combination variation (using CHECK A through CHECK F for the same
coverage), the SYNTHESIS EXCELLENCE SIGNALS section must include a signal that:
1. Names both enforcement architectures explicitly (adversarial path and template path).
2. Confirms that both paths achieve equivalent aspirational coverage for the evaluator-
   behavior axes tested in this round (currently C-25 via AUDIT C / CHECK F, with
   equivalent coverage of C-22/C-23/C-24 enforcement).
3. Notes the structural mechanism by which the template path extends (e.g., "CHECK F
   added after CHECK E in the existing chain, without restructuring the audit table").

_Pass condition_: A signal naming both enforcement paths with explicit coverage-equivalence
confirmation and mechanism-of-extension note. PARTIAL if equivalence is stated but one of
the two paths is not named, or if the mechanism of extension is absent. FAIL if no signal
addresses two-path equivalence when both combination path types appear in the variation set.

_Relationship to C-04/C-25_: C-04 tests that named audits are present (satisfied by either
path); C-25 tests that new-axis evidence compliance fires correctly (satisfied by either
path); C-29 tests whether the SYNTHESIS confirms that both architectural paths provide
equivalent coverage — a property that is not visible from scoring either path alone.

---

**C-30 — SYNTHESIS — intra-phase timing order in injection-point map**

When C-28 fires and the injection-point map includes two or more axes that share the same
phase (specifically, C-25 and C-27 both appear in the VERIFIER phase), the signal must:
1. State the intra-phase timing order for each same-phase axis pair — naming which fires
   earlier in the phase and what structural event separates their timing positions:
   - C-25 (AUDIT C / CHECK F): fires post-write, after the evidence-quality audits (AUDIT B /
     CHECK B), before the audit table declaration.
   - C-27 (FLAG CLOSURE REQUIREMENT): fires after the correction-loop instruction, before
     the VERIFIER AUDIT COMPLETE gate token.
2. Explicitly confirm that the intra-phase positions are non-overlapping — neither timing
   window contains the other (C-27 cannot fire "inside" C-25's timing window and vice versa).

Without C-30, a C-28-passing signal may satisfy the disjointness requirement by asserting
that same-phase axes "fire at different timing positions" without specifying which position
each occupies, leaving the evaluator unable to verify the non-overlap claim independently.

_Pass condition_: When C-28 fires and at least two axes share the same phase, the injection-
point map specifies the intra-phase timing order for all same-phase axis pairs and explicitly
confirms non-overlap at the position level. PARTIAL if timing order is specified but non-
overlap confirmation is absent. FAIL if same-phase axes are mentioned without any intra-phase
timing order specification.
auto-PASS when the C-28 trigger does not fire, or when no two of C-25/C-26/C-27 share the
same phase (i.e., all three axes are in different phases).

_Relationship to C-28_: C-28 requires the injection-point map to name phase and timing for
each axis and confirm structural disjointness; C-30 requires that when two axes share the
same phase, the disjointness confirmation resolves to named intra-phase positions with
explicit non-overlap rather than an asserted-but-unspecified timing separation.

---

**C-31 — SYNTHESIS — per-axis correspondence enumeration in two-path equivalence signal**

When C-29 fires, the two-path equivalence signal must:
1. Enumerate the specific adversarial-to-template-path correspondence by criterion ID for
   each covered axis (e.g., "C-25 satisfied by AUDIT C = CHECK F: identical per-criterion
   compliance rules for C-22/C-23/C-24") — not merely assert that overall coverage is
   equivalent.
2. Confirm that SYNTHESIS-phase criteria (specifically C-26 and C-27) are architecturally
   identical on both paths — i.e., the SYNTHESIS blocks for these criteria are path-agnostic
   and do not depend on which Verifier enforcement architecture the variation used.

Without C-31, a C-29-passing signal may name both paths and assert "equivalent coverage"
without mapping each adversarial check to its template-path counterpart by axis, and without
confirming that SYNTHESIS-phase criteria such as C-26 and C-27 are unaffected by the choice
of Verifier architecture.

_Pass condition_: When C-29 fires, the equivalence signal enumerates per-axis correspondence
between adversarial checks and template checks (by criterion ID) and explicitly confirms that
SYNTHESIS-phase criteria are architecturally identical on both paths. PARTIAL if per-axis
correspondence is enumerated but SYNTHESIS-phase path-agnosticism is not confirmed, or if
path-agnosticism is confirmed but per-axis correspondence is absent. FAIL if neither property
is present.
auto-PASS when C-29 auto-PASSes (variation set does not include both adversarial-path and
template-path combination variations).

_Relationship to C-29_: C-29 requires the equivalence signal to name both paths, confirm
coverage equivalence, and state the template-path extension mechanism; C-31 requires that
coverage confirmation be decomposed per-axis by criterion ID correspondence and that SYNTHESIS-
phase criteria be explicitly confirmed as path-agnostic — a property that neither C-29's
coverage assertion nor the extension mechanism statement alone can establish.

---

### Criterion roster with mechanism-level diagnostic questions (v10)

| ID | Name | Tier | Auto-PASS | Diagnostic Question |
|----|------|------|-----------|---------------------|
| C-01 | Protocol completeness — all 4 roles with gate tokens | E | none | Can you identify all four role rows in the ROLE DEPENDENCY MANIFEST (JUDGE, ANALYST, VERIFIER, SYNTHESIS), each with a Produces entry, and confirm that all three hard gate rules are stated? A manifest with three rows, or gate rules present in prose without the manifest table, fails C-01. |
| C-02 | JUDGE — ACCEPTABLE/UNACCEPTABLE pairs per criterion | E | none | Does the JUDGE phase contain a C-[NN] / ACCEPTABLE / UNACCEPTABLE / What separates them block for every criterion in the rubric, and are the examples extracted from actual outputs rather than invented? A JUDGE that covers only the differentiating criteria and not the baseline criteria fails C-02. |
| C-03 | ANALYST — composite formula /23 denominator (v10) | E | none | Does the ANALYST formula use N_aspirational = 23? A formula using N_aspirational = 21 (v9) is a C-03 FAIL regardless of other structure. Can you re-derive the composite from the 31 verdict values using N_essential=5, N_recommended=3, N_aspirational=23 within +/-0.01 rounding tolerance? |
| C-04 | VERIFIER — named audits with per-criterion checks | E | none | Does the VERIFIER phase contain at least two named audits (AUDIT A / AUDIT B or CHECK A / CHECK B) with explicit per-criterion or per-verdict-type applicability rules? A Verifier with only prose correction instructions and no named audit structure fails C-04. |
| C-05 | SYNTHESIS — all four required sections | E | none | Does the SYNTHESIS phase contain all four section headers: LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, and REGRESSION SIGNALS? A SYNTHESIS missing any one section fails C-05. |
| C-06 | ANALYST — CRITERIA INDEPENDENCE NOTE for C-17/C-18 | R | none | Does the ANALYST phase contain a CRITERIA INDEPENDENCE NOTE, positioned after the composite formula, that declares C-17 and C-18 independently satisfiable and includes a decoupling statement for the C-17 PASS + C-18 FAIL case? A note present but positioned before the formula fails C-06. |
| C-07 | ANALYST — NEW-AXIS AUDIT NOTE for C-19/C-20/C-21 | R | none | Does the ANALYST phase contain a NEW-AXIS AUDIT NOTE that requires explicit PASS or FAIL verdicts with independent evidence for each of C-19, C-20, and C-21, and prohibits omitting unsatisfied axes? A note that only declares orthogonality without requiring explicit verdicts fails C-07. |
| C-08 | JUDGE — PRIMING CEILING NOTE and PHASE-PLACEMENT NOTE | R | none | Does the JUDGE phase contain both PRIMING CEILING NOTE (second-order ceiling, third-order rubric-neutral) and PHASE-PLACEMENT NOTE (phase-position pairs for C-19/C-20/C-21), both before JUDGE STANDARD COMPLETE? A JUDGE missing either note fails C-08. |
| C-09 | ANALYST — mandatory PARTIAL diagnostic block format | A | none | Does the ANALYST phase define the C-[NN] partial: [prevented FAIL] / [prevented PASS] format and require it for every PARTIAL verdict? An ANALYST that accepts PARTIAL verdicts without a defined diagnostic format fails C-09. |
| C-10 | VERIFIER — AUDIT A evidence quality vs. Judge standard | A | none | Does AUDIT A (or CHECK A) reference the Judge's ACCEPTABLE/UNACCEPTABLE pair as the comparison standard, and name both rejection conditions: (a) resembles UNACCEPTABLE, and (b) could apply to a different output unchanged? An AUDIT A with only one rejection condition fails C-10. |
| C-11 | VERIFIER — AUDIT B diagnostic completeness for PARTIAL | A | none | Does AUDIT B (or CHECK B) apply to PARTIAL verdicts only, verify both halves of the diagnostic (prevented FAIL + prevented PASS), and fail one-direction or label-only diagnostics? An AUDIT B that checks only that a diagnostic exists without checking both halves fails C-11. |
| C-12 | Gate token — JUDGE STANDARD COMPLETE | A | none | Does JUDGE STANDARD COMPLETE appear as a standalone token on its own line, and does the ANALYST phase open with a gate instruction referencing it? A token embedded in a sentence, or a missing downstream gate instruction, fails C-12. |
| C-13 | Gate token — ANALYST COMPLETE with N-outputs count | A | none | Does ANALYST COMPLETE appear with an N-outputs count (e.g., "5 outputs scored"), and does the VERIFIER phase open with a gate instruction referencing it? PARTIAL if token present but N-outputs count absent. |
| C-14 | Gate token — VERIFIER AUDIT COMPLETE | A | none | Does VERIFIER AUDIT COMPLETE appear as a standalone token, and does the SYNTHESIS phase open with a gate instruction referencing it? A token present but SYNTHESIS gate instruction absent fails C-14. |
| C-15 | ANALYST — COMPOSITE ACCURACY NOTE fraction + two-decimal | A | none | Does the COMPOSITE ACCURACY NOTE explicitly state all four requirements: (1) aspirational fraction format, (2) two decimal places, (3) named missing criteria by ID, (4) no near-ceiling as complete? PARTIAL if fewer than four requirements are stated. |
| C-16 | ANALYST — REGISTER NOTE dual-register equivalence | A | none | Does the REGISTER NOTE provide quoted examples of both command-form and declarative-form for at least one criterion class (scan blocks) and both imperative and specification register for at least one criterion class (pre-execution priming)? A REGISTER NOTE with equivalence declared but examples described rather than quoted fails C-16 PARTIAL. A REGISTER NOTE with only declarative-form examples fails C-16. |
| C-17 | SYNTHESIS — EXCELLENCE SIGNALS mechanism naming | A | none | Does each excellence signal name the structural mechanism (the design property) rather than only the criterion label? A signal that says "V-01 passed C-25 because it had AUDIT C" without stating what AUDIT C does differently from the absent case fails C-17 for that signal. PARTIAL if some signals name mechanisms but others do not. |
| C-18 | SYNTHESIS — FAILURE PATTERNS named diagnosis | A | auto-PASS when no universal failures | Does each failure pattern entry include a categorized diagnosis type (rubric gap / skill design issue / input quality issue) followed by a one-sentence explanation? A failure pattern without a categorized diagnosis type fails C-18. |
| C-19 | JUDGE — PRIMING CEILING NOTE at correct phase position | A | none | Does the PRIMING CEILING NOTE appear in the JUDGE phase before JUDGE STANDARD COMPLETE, and does the evidence confirm both phase identity and position? Evidence that states "PRIMING CEILING NOTE present" without confirming JUDGE phase and pre-gate-token position fails C-19. |
| C-20 | ANALYST — REGISTER NOTE at correct phase position | A | none | Does the REGISTER NOTE appear in the ANALYST phase before the scoring table, and does the evidence confirm both ANALYST phase and pre-table position? A REGISTER NOTE in the JUDGE phase, or after the scoring table begins, fails C-20. |
| C-21 | ANALYST — CRITERIA INDEPENDENCE NOTE at correct phase position | A | none | Does the CRITERIA INDEPENDENCE NOTE appear in the ANALYST phase after the composite formula, and does the evidence confirm both ANALYST phase and post-formula position? A note before the formula, or in the JUDGE phase, fails C-21. |
| C-22 | ANALYST — new-axis individual naming by criterion ID | A | none | Do the evidence cells for C-19, C-20, and C-21 each name the specific criterion ID being satisfied — not "all three axes" collectively? PARTIAL if at least one cell names its ID but another uses collective reference. FAIL if all cells use collective reference only. |
| C-23 | ANALYST — composite accuracy fraction + two-decimal in evidence | A | none | Does at least one evidence cell for aspirational-accuracy criteria quote both a specific fraction (e.g., "17/23 PASS") and a specific two-decimal composite value (e.g., "98.10") drawn from the scored output? Evidence that describes the requirement abstractly without quoting actual values fails C-23. |
| C-24 | JUDGE + ANALYST — phase-placement confirmation in evidence cells | A | none | Do the evidence cells for C-19, C-20, and C-21 each state both phase identity and intra-phase position? Evidence that confirms note content without naming phase and position fails C-24 for that cell. PARTIAL if some cells confirm both but at least one does not. |
| C-25 | VERIFIER — new-axis evidence compliance (AUDIT C / CHECK F) | A | none | Does the VERIFIER phase contain a named compliance check (AUDIT C or CHECK F) targeting C-22, C-23, and C-24 evidence cells, with per-criterion compliance rules for all three? The audit table must include the corresponding column; the FLAG format must include its designator. PARTIAL if the check covers fewer than three of the target criteria. |
| C-26 | SYNTHESIS — plateau-classification protocol | A | auto-PASS when score spread exists | When no score spread exists, does SYNTHESIS EXCELLENCE SIGNALS contain a PLATEAU-CLASSIFICATION NOTE with Step 1 (PLATEAU-DETECTED / STABILITY-CONFIRMED), Step 2 (aspirational tier ceiling with rubric version), and Step 3 (named candidate criterion in structured format + named candidate axis)? A generic redesign instruction without these three steps fails C-26. PARTIAL if Step 1 and Step 2 are present but Step 3 omits the structured format. |
| C-27 | VERIFIER — flag-closure enforcement | A | none | Does the VERIFIER phase contain a FLAG CLOSURE REQUIREMENT with three-field inventory (issued/resolved/open), explicit Flags open = 0 condition on VERIFIER AUDIT COMPLETE, zero-flag case requirement, and prose-substitution prohibition? PARTIAL if block is present but zero-flag case requirement or prose-substitution prohibition is absent. |
| C-28 | SYNTHESIS — injection-point map for combination variations | A | auto-PASS when no combination variation satisfies all of C-25+C-26+C-27 | When a variation satisfies all of C-25, C-26, and C-27: does the SYNTHESIS excellence signal for that variation name the injection phase and timing for each of the three axes individually, and explicitly confirm their structural disjointness? A signal describing the combined effect without naming individual injection points fails C-28. PARTIAL if injection points are named but disjointness is not explicitly confirmed. |
| C-29 | SYNTHESIS — two-path equivalence signal | A | auto-PASS when variation set does not include both an adversarial-path and a template-path combination variation | When both an adversarial-path (AUDIT A/B/C) combination variation and a template-path (CHECK A through CHECK F) combination variation are present: does SYNTHESIS include a signal naming both paths, confirming equivalent coverage, and noting the mechanism of template-path extension? PARTIAL if equivalence is stated but one path is unnamed or the extension mechanism is absent. |
| C-30 | SYNTHESIS — intra-phase timing order in injection-point map | A | auto-PASS when C-28 does not fire, or when no two of C-25/C-26/C-27 share the same phase | When C-28 fires and at least two axes share the same phase: does the injection-point map specify the intra-phase timing order for all same-phase axis pairs and explicitly confirm that their positions are non-overlapping? PARTIAL if timing order is given but non-overlap confirmation is absent. FAIL if same-phase axes are mentioned without intra-phase timing order specification. |
| C-31 | SYNTHESIS — per-axis correspondence enumeration in two-path equivalence signal | A | auto-PASS when C-29 auto-PASSes | When C-29 fires: does the equivalence signal enumerate the per-axis adversarial-to-template correspondence by criterion ID (e.g., "C-25: AUDIT C = CHECK F") and explicitly confirm that SYNTHESIS-phase criteria (C-26, C-27) are architecturally identical on both paths? PARTIAL if per-axis correspondence is present but SYNTHESIS-phase path-agnosticism is unconfirmed, or vice versa. FAIL if neither property is present. |
