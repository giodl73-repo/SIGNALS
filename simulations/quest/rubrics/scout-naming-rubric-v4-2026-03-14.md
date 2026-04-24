Done. Here's the v4 summary:

---

## What changed from v3 to v4

**Two new aspirational criteria** extracted from Round 3:

**C-15 — Labeled Sub-part Record** (`depth`)
The TOP PICK block uses explicitly labeled lines `(1) Dimensions: [...] / (2) vs. Status-quo: [...] / (3) Vocabulary: [...]` instead of prose. Upgrades C-14 from instruction-inferred to output-verifiable — a missing sub-part is an absent line, not an omitted clause. V-03/V-04/V-05 pass; V-01/V-02 fail (they use inline prose).

**C-16 — Gate 3 Binary Status Flags** (`behavior`)
Gate 3 (SCORE/DECIDE boundary) carries binary status flags confirming cross-phase dependencies exist before DECIDE runs: `Status-quo benchmarked: yes/no`, `Collisions checked: top 3`. Extends C-13's count pattern — gates now have two mechanisms: counters (cardinality) and flags (cross-phase consistency). V-03/V-04/V-05 pass; V-01/V-02 fail (no Gate 3 line).

**Scoring impact**:
- Denominator: 6 → 8
- Max achievable (no C-09): 98.3 → **98.75**
- R3 golden prompts (V-03/V-04/V-05) retroactively score **98.75** under v4; V-01/V-02 score **96.25** (clear C-14 in prose but miss C-15 and C-16)
s (did a required prior step complete).

---

## Criterion Table

| ID | Text | Tier | Category |
|----|------|------|----------|
| C-01 | Candidate Volume (10-15) | essential | correctness |
| C-02 | Five-Role Scoring Matrix + declared weights | essential | correctness |
| C-03 | Collision Check (namespace + external) | essential | coverage |
| C-04 | Top Pick Named + Justified | essential | correctness |
| C-05 | Constraint Parsed + Applied | essential | behavior |
| C-06 | Disqualification Logic labeled | recommended | correctness |
| C-07 | Runner-Up + Fallback Rationale | recommended | depth |
| C-08 | Findings Register (SF-NN) | recommended | depth |
| C-09 | `--validate` flag pins row 1 + Validation Summary | aspirational | behavior |
| C-10 | Domain Vocabulary Extraction logged | aspirational | depth |
| C-11 | Generation-time Constraint Enforcement | aspirational | behavior |
| C-12 | Phase-structured Output | aspirational | behavior |
| C-13 | Gate Confirmation Count | aspirational | behavior |
| C-14 | 3-part DECIDE Rationale | aspirational | depth |
| C-15 | Labeled Sub-part Record | **aspirational** | depth |
| C-16 | Gate 3 Binary Status Flags | **aspirational** | behavior |

**Score ceiling**: 95/100 until C-09 is implemented. Max achievable: 98.75 (clears all except C-09).

---

## Essential Criteria

### C-01 — Candidate Volume (10-15)

**Pass condition**: Output contains between 10 and 15 candidate names in the GENERATE phase. Fewer than 10 fails; more than 15 fails.

---

### C-02 — Five-Role Scoring Matrix + Declared Weights

**Pass condition**: Scoring matrix has exactly five role columns (PM, Strategy, GTM, UX, Design). Role weights are declared before the matrix and sum to 100%. Composite score formula is stated explicitly.

---

### C-03 — Collision Check (namespace + external)

**Pass condition**: Top candidates checked against both internal namespace and external registries (npm/PyPI and/or brand search). Both collision classes reported. Minimum top 3 candidates checked.

---

### C-04 — Top Pick Named + Justified

**Pass condition**: Top pick identified with score value and >= 1 sentence of rationale that references at least one scoring dimension (PM, Strategy, GTM, UX, or Design).

*(See C-14 for the aspirational prose bar and C-15 for the aspirational structural bar on this criterion.)*

---

### C-05 — Constraint Parsed + Applied

**Pass condition**: If a constraint is present in the input, the output explicitly acknowledges it and applies it. No candidates that violate the constraint appear in the scoring matrix without a disqualification label.

---

## Recommended Criteria

### C-06 — Disqualification Logic Labeled

**Pass condition**: Any disqualified candidate carries a label stating the disqualification reason (e.g., `[DISQ: low Strategy]`, `[DISQ: constraint]`). Structural rules (e.g., score floor on core dimensions) are stated explicitly; disqualification is not left to evaluator judgment.

---

### C-07 — Runner-Up + Fallback Rationale

**Pass condition**: Second-place candidate named with its composite score and >= 1 sentence explaining why it is the fallback choice.

---

### C-08 — Findings Register (SF-NN)

**Pass condition**: Output includes a FINDINGS REGISTER section with >= 1 SF-NN entry. Each entry has an ID, description, and severity (P1/P2/P3).

---

## Aspirational Criteria

### C-09 — `--validate` Flag Pins Row 1 + Validation Summary

`--validate` mode re-runs the scoring matrix against the stored top pick from a prior run. Row 1 is locked; output contains a Validation Summary section comparing current scores to prior scores.

**Pass condition**: `--validate` flag recognized and handled. Row 1 pinned. Validation Summary present with delta notation.

**Origin**: Design requirement. Unimplementable until skill infrastructure exists. Blocks score ceiling at 95.

---

### C-10 — Domain Vocabulary Extraction Logged

Vocabulary terms extracted from source files are surfaced as a named list before candidates are generated.

**Pass condition**: Output contains `Domain vocabulary: [term1, term2, ...]` with 5-10 terms and a named source file. Vocabulary must precede the GENERATE phase or appear in a SETUP phase.

**Origin**: Round 1, V-05.

---

### C-11 — Generation-time Constraint Enforcement

Constraints are enforced during candidate generation (GENERATE phase), not only during post-hoc filtering. Candidates that violate a constraint never enter the scoring matrix.

**Pass condition**: Output explicitly marks constraint evaluation as occurring before or during generation. Scoring matrix contains no candidates that would have required post-hoc disqualification for constraint violation.

**Note**: C-11 without C-13 means compliance is inferred from absence of violating candidates, not confirmed by a counter. C-13 is the verification mechanism for C-11.

**Origin**: Round 1, V-05.

---

### C-12 — Phase-structured Output

Output is organized into explicit named phases — at minimum GENERATE, SCORE, DECIDE — with no cross-phase bleed.

**Pass condition**: At least three named phase headers present. No scoring rows appear under GENERATE; no new candidate names introduced under SCORE or DECIDE.

**Note**: Phase structure is the structural prerequisite for C-11 — you cannot confirm generation-time enforcement without a visible GENERATE phase boundary. Numbered phase separators (e.g., `--- PHASE 2: GENERATE ---`) are the stronger form; unlabeled section titles satisfy the pass condition but not the aspirational ideal.

**Origin**: Round 1, V-05.

---

### C-13 — Gate Confirmation Count

A gate counter line appears at the close of the GENERATE phase confirming how many candidates were generated, how many were pre-disqualified, and how many advance to SCORE.

**Pass condition**: Output contains a line of the form `Generated: N. Pre-disqualified: N. Advancing: N.` (or equivalent three-value summary) at the GENERATE/SCORE boundary. The advancing count must equal the candidates that appear in the scoring matrix.

**Why this matters**: C-11 requires generation-time constraint enforcement but does not require the model to prove it happened. A gate counter makes C-11 output-verifiable — the evaluator can confirm compliance from the count, not from absence of violating candidates. Without C-13, C-11 is instruction-inferred; with C-13, C-11 is output-verified.

*(See C-16 for the aspirational extension of this pattern to Gate 3.)*

**Origin**: Round 2. V-03, V-04, V-05 demonstrated this mechanism. V-01 and V-02 passed C-11 without C-13 (compliance inferred).

---

### C-14 — 3-part DECIDE Rationale

The top-pick rationale in the DECIDE phase contains all three of: (1) reference to >= 2 scoring dimensions by name, (2) explicit comparison to the status-quo name or nearest competitor, (3) connection to >= 1 domain vocabulary term extracted in SETUP.

**Pass condition**: DECIDE section contains all three elements. "It scored highest" alone fails. A rationale that references dimensions but omits status-quo comparison fails. A rationale that references dimensions and status-quo but omits vocabulary connection fails.

**Why this matters**: C-04 (essential) requires only one dimension reference. C-14 converts the top-pick justification into a mandatory competitive argument — the status-quo requirement forces the model to position the recommendation against a concrete alternative, which is the actual decision the team needs to make. The vocabulary connection confirms the pick is grounded in the product's own language.

*(See C-15 for the aspirational structural form of this criterion.)*

**Origin**: Round 2, V-05 (full 3-part). V-03 and V-01 reached 2-part. V-02 met only the essential bar.

---

### C-15 — Labeled Sub-part Record

The TOP PICK block in DECIDE presents the 3-part rationale as explicitly labeled sub-part lines — `(1) Dimensions: [...]`, `(2) vs. Status-quo: [...]`, `(3) Vocabulary: [...]` — rather than as running prose.

**Pass condition**: All three C-14 elements appear as distinct, named sub-part lines under the TOP PICK heading. Each sub-part label is present and each line is non-empty. A missing sub-part label (even if the content is present in prose) fails.

**Why this matters**: C-14 in prose form requires the evaluator to read and parse the rationale to confirm all three elements are present — a missing element is an omitted clause, detectable only by interpretation. C-15 in record form makes each element a visible structural slot: a missing sub-part is an absent line, not an ambiguous omission. The labeled record is the output-verifiable form; prose is instruction-inferred. This principle generalizes: any criterion requiring multiple distinct elements in the same output block should prefer the labeled record form over inline instructions.

**Relationship to C-14**: C-15 is a structural upgrade of C-14. A prompt that passes C-15 always passes C-14. A prompt that passes C-14 in prose form does not pass C-15.

**Origin**: Round 3. V-03, V-04, V-05 demonstrated labeled sub-part records. V-01 and V-02 used inline prose (C-14 pass, C-15 fail). Labeled record structure identified as the compliance driver for multi-part output requirements.

---

### C-16 — Gate 3 Binary Status Flags

A gate summary line appears at the close of the SCORE phase (Gate 3) that includes at least one binary status flag confirming that a required prior-phase artifact exists before DECIDE proceeds.

**Pass condition**: Output contains a Gate 3 line that includes at minimum: surviving candidate count AND at least one binary flag of the form `[artifact]: yes/no` (e.g., `Status-quo benchmarked: yes`, `Collisions checked: top 3`). The flag must refer to an artifact produced in an earlier phase; it cannot be satisfied by referring only to SCORE-phase results.

**Why this matters**: C-13 confirms what happened within the GENERATE phase (count of advancing candidates). C-16 extends the gate pattern to the SCORE/DECIDE boundary: before DECIDE executes, the model must confirm that cross-phase dependencies are satisfied. `Status-quo benchmarked: yes/no` confirms the SETUP-phase artifact required by C-14(2) exists. `Collisions checked: top 3` confirms the C-03 artifact covers the surviving candidates. Gates can carry both counters (how many advanced) and flags (did a required prior step complete) — C-16 establishes the flag half of this contract.

**Relationship to C-13**: C-13 is the count mechanism at Gate 2. C-16 is the flag mechanism at Gate 3. Together they form a full gate protocol: count confirms cardinality; flags confirm cross-phase consistency.

**Origin**: Round 3. V-03, V-04, V-05 demonstrated Gate 3 with binary status flags. V-01 and V-02 had no Gate 3 line. Pattern identified as a generalization of the Gate 2 count — gates as a general cross-phase verification mechanism, not a single-use counter.

---

## Scoring Formula (updated)

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/8 * 10)   <- denominator bumped from 6 to 8
```

The denominator change means the aspirational weight per criterion drops from 1.67 pts to 1.25 pts. Maximum aspirational contribution stays at 10 pts.

**Score examples**:

| Aspirational cleared | Score |
|----------------------|-------|
| All 8 (requires C-09) | 100.0 |
| C-10 + C-11 + C-12 + C-13 + C-14 + C-15 + C-16 (no C-09) | 98.75 |
| C-10 + C-11 + C-12 + C-13 + C-14 + C-15 (no C-09, no C-16) | 97.5 |
| C-10 + C-11 + C-12 + C-13 + C-14 (no C-09, no C-15, no C-16) | 96.25 |
| C-10 + C-11 + C-12 + C-13 only | 95.0 |
| C-11 + C-12 + C-13 only | 93.75 |
| C-11 + C-12 only | 92.5 |
| None | 90.0 |
