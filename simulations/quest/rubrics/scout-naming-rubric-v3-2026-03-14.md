Reading the two captured patterns from the scorecard JSON:

1. **Gate confirmation count** → C-13 (makes C-11 output-verifiable, not instruction-inferred)
2. **3-part DECIDE rationale** → C-14 (dimensions + status-quo + vocab; can't be satisfied by "it scored highest")

---

# Scout Naming Rubric — v3

**Version**: v3
**Updated**: 2026-03-14
**Changes from v2**: Added C-13 (Gate Confirmation Count) and C-14 (3-part DECIDE Rationale) as aspirational criteria, extracted from Round 2 excellence patterns. Aspirational denominator bumped from 4 to 6. Score ceiling remains 95 until C-09 (`--validate`) is implemented. Max achievable without C-09: 98.3 (5/6 × 10 = 8.3 aspirational).

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
| C-13 | Gate Confirmation Count | **aspirational** | behavior |
| C-14 | 3-part DECIDE Rationale | **aspirational** | depth |

**Score ceiling**: 95/100 until C-09 is implemented. Max achievable: 98.3 (clears all except C-09).

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

**Pass condition**: Top pick identified with score value and ≥ 1 sentence of rationale that references at least one scoring dimension (PM, Strategy, GTM, UX, or Design).

*(See C-14 for the aspirational bar on this criterion.)*

---

### C-05 — Constraint Parsed + Applied

**Pass condition**: If a constraint is present in the input, the output explicitly acknowledges it and applies it. No candidates that violate the constraint appear in the scoring matrix without a disqualification label.

---

## Recommended Criteria

### C-06 — Disqualification Logic Labeled

**Pass condition**: Any disqualified candidate carries a label stating the disqualification reason (e.g., `[DISQ: low Strategy]`, `[DISQ: constraint]`). Structural rules (e.g., score floor on core dimensions) are stated explicitly; disqualification is not left to evaluator judgment.

---

### C-07 — Runner-Up + Fallback Rationale

**Pass condition**: Second-place candidate named with its composite score and ≥ 1 sentence explaining why it is the fallback choice.

---

### C-08 — Findings Register (SF-NN)

**Pass condition**: Output includes a FINDINGS REGISTER section with ≥ 1 SF-NN entry. Each entry has an ID, description, and severity (P1/P2/P3).

---

## Aspirational Criteria

### C-09 — `--validate` Flag Pins Row 1 + Validation Summary

`--validate` mode re-runs the scoring matrix against the stored top pick from a prior run. Row 1 is locked; output contains a Validation Summary section comparing current scores to prior scores.

**Pass condition**: `--validate` flag recognized and handled. Row 1 pinned. Validation Summary present with delta notation.

**Origin**: Design requirement. Unimplementable until skill infrastructure exists. Blocks score ceiling at 95.

---

### C-10 — Domain Vocabulary Extraction Logged

Vocabulary terms extracted from source files are surfaced as a named list before candidates are generated.

**Pass condition**: Output contains `Domain vocabulary: [term1, term2, ...]` with 5–10 terms and a named source file. Vocabulary must precede the GENERATE phase or appear in a SETUP phase.

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

**Origin**: Round 2. V-03, V-04, V-05 demonstrated this mechanism. V-01 and V-02 passed C-11 without C-13 (compliance inferred). Gate confirmation is the strongest C-11 enforcement mechanism available in text prompts.

---

### C-14 — 3-part DECIDE Rationale

The top-pick rationale in the DECIDE phase contains all three of: (1) reference to ≥ 2 scoring dimensions by name, (2) explicit comparison to the status-quo name or nearest competitor, (3) connection to ≥ 1 domain vocabulary term extracted in SETUP.

**Pass condition**: DECIDE section contains all three elements. "It scored highest" alone fails. A rationale that references dimensions but omits status-quo comparison fails. A rationale that references dimensions and status-quo but omits vocabulary connection fails.

**Why this matters**: C-04 (essential) requires only one dimension reference. C-14 converts the top-pick justification into a mandatory competitive argument — the status-quo requirement forces the model to position the recommendation against a concrete alternative, which is the actual decision the team needs to make. The vocabulary connection confirms the pick is grounded in the product's own language.

**Origin**: Round 2, V-05 (full 3-part). V-03 and V-01 reached 2-part (dimensions + vocab, no status-quo). V-02 met only the 1-dimension essential bar.

---

## Scoring Formula (updated)

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/6 * 10)   ← denominator bumped from 4 to 6
```

The denominator change means the aspirational weight per criterion drops from 2.5 pts to 1.67 pts. Maximum aspirational contribution stays at 10 pts.

**Score examples**:

| Aspirational cleared | Score |
|----------------------|-------|
| All 6 (requires C-09) | 100.0 |
| C-10 + C-11 + C-12 + C-13 + C-14 (no C-09) | 98.3 |
| C-10 + C-11 + C-12 + C-13 (no C-09, no C-14) | 96.7 |
| C-11 + C-12 + C-13 only | 95.0 |
| C-11 + C-12 only (R1 ceiling) | 93.3 |
| None | 90.0 |
