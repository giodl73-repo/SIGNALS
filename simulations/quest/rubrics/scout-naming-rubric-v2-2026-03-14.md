Here is the complete updated rubric:

---

# Scout Naming Rubric — v2

**Version**: v2
**Updated**: 2026-03-14
**Changes from v1**: Added C-11 (Generation-time Constraint Enforcement) and C-12 (Phase-structured Output) as aspirational criteria, extracted from Round 1 excellence signals. V-05 (Combined, 95) demonstrated both mechanisms. Score ceiling remains 95 until C-09 (`--validate`) is implemented.

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
| C-11 | Generation-time Constraint Enforcement | **aspirational** | behavior |
| C-12 | Phase-structured Output | **aspirational** | behavior |

**Score ceiling**: 95/100 until C-09 is implemented.

---

## Essential Criteria

*(C-01 through C-05 unchanged)*

---

## Recommended Criteria

*(C-06 through C-08 unchanged)*

---

## Aspirational Criteria (new in v2)

### C-11 -- Generation-time Constraint Enforcement

Constraints are enforced during candidate generation (GENERATE phase), not only during post-hoc filtering. Candidates that violate a constraint never enter the scoring matrix.

**Pass condition**: Output explicitly marks constraint evaluation as occurring before or during generation. Scoring matrix contains no candidates that would have required post-hoc disqualification for constraint violation.

**Origin**: Round 1, V-05. Post-hoc filtering (C-05/C-06) satisfies the essential bar; generation-time enforcement is the higher bar — it eliminates false-positive score inflation from candidates that score well across roles but violate a constraint.

---

### C-12 -- Phase-structured Output

Output is organized into explicit named phases — at minimum GENERATE, SCORE, DECIDE — with no cross-phase bleed.

**Pass condition**: At least three named phase headers present. No scoring rows appear under GENERATE; no new candidate names introduced under SCORE or DECIDE.

**Origin**: Round 1, V-05. Phase structure is also the structural prerequisite for C-11 — you cannot confirm generation-time enforcement without a visible GENERATE phase boundary.

---

## Scoring Formula (updated)

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/4 * 10)   ← denominator bumped from 2 to 4
```

The denominator change means the aspirational weight per criterion drops from 5 pts to 2.5 pts. Maximum aspirational contribution stays at 10 pts. A variation that clears C-10 + C-11 + C-12 (but not C-09) scores: `60 + 30 + (3/4 * 10) = 97.5`.
 just "it scored highest").
- **Pass condition**: Top pick identified with score value and >= 1 sentence of rationale that references at least one scoring dimension (PM, Strategy, GTM, UX, or Design).

---

### C-05 -- Constraint Parsed and Applied

- **Weight**: essential
- **Category**: behavior
- **Text**: Any constraint passed in the invocation is acknowledged and visibly applied -- either by filtering candidates that violate it or by noting which candidates satisfy/violate it.
- **Pass condition**: Constraint mentioned explicitly in setup or filtering step. At least one candidate decision (include, disqualify, or note) references the constraint.

---

## Recommended Criteria

### C-06 -- Disqualification Logic

- **Weight**: recommended
- **Category**: correctness
- **Text**: Candidates eliminated for any reason are labeled "disqualified" with a specific cause (namespace collision, constraint violation, brand conflict, etc.) rather than silently omitted.
- **Pass condition**: At least one candidate is explicitly disqualified with a labeled reason. Disqualified candidates may remain in the matrix with a flag or be listed separately -- either form passes.

---

### C-07 -- Runner-Up with Fallback Rationale

- **Weight**: recommended
- **Category**: depth
- **Text**: A runner-up (second-best available candidate) is named with a brief rationale explaining why it is a viable fallback if the top pick is unavailable.
- **Pass condition**: Runner-up named, score stated, and at least one fallback rationale sentence present.

---

### C-08 -- Findings Register

- **Weight**: recommended
- **Category**: depth
- **Text**: Output concludes with a findings register in SF-NN format identifying design gaps, re-weighting opportunities, or constraint relaxations surfaced during scoring.
- **Pass condition**: Findings table or list present with at least one SF-NN entry. Each entry has an ID, description, and severity (P1/P2/P3 or equivalent).

---

## Aspirational Criteria

### C-09 -- --validate Flag Behavior

- **Weight**: aspirational
- **Category**: behavior
- **Text**: When invoked with `--validate <name>`, the named candidate is pinned at row 1 of the matrix regardless of its score, and a "Validation Summary" block appears immediately after the matrix summarizing whether the named choice is defensible given alternatives.
- **Pass condition**: `--validate` path produces: (1) named candidate at row 1, (2) a Validation Summary block with a clear verdict (validated / not recommended / conditional).

**Status**: Design gap -- skill does not yet support `--validate`. No variation can clear this criterion until the flag is implemented.

---

### C-10 -- Domain Vocabulary Extraction Logged

- **Weight**: aspirational
- **Category**: depth
- **Text**: Output surfaces the domain vocabulary it extracted from CLAUDE.md or plugin-plan.md as a setup step, showing which terms seeded or influenced candidate generation.
- **Pass condition**: At least 5 domain vocabulary terms listed in a setup or extraction step, with an explicit note that they came from a named source file.

---

### C-11 -- Generation-time Constraint Enforcement

- **Weight**: aspirational
- **Category**: behavior
- **Text**: Constraints are enforced during candidate generation (GENERATE phase), not only during post-hoc filtering. Candidates that violate a constraint never enter the scoring matrix -- they are excluded before scoring, not disqualified afterward.
- **Pass condition**: Output explicitly marks constraint evaluation as occurring before or during generation (e.g., a GENERATE phase step that excludes violating candidates). Scoring matrix contains no candidates that would have required post-hoc disqualification for constraint violation.

**Origin**: Round 1, V-05 (Combined, 95). Generation-time enforcement eliminates a class of false-positive score inflation: a candidate that scores well across roles but violates a constraint can inflate the matrix even if later disqualified. Excluding it at generation time prevents contamination. Post-hoc filtering (C-05/C-06) satisfies the essential bar; generation-time enforcement is the higher bar.

---

### C-12 -- Phase-structured Output

- **Weight**: aspirational
- **Category**: behavior
- **Text**: Output is organized into explicit named phases -- at minimum GENERATE, SCORE, and DECIDE -- with clear phase headers. Each phase contains only the work appropriate to that phase; no scoring logic appears in the generation phase and no new candidates appear in the scoring phase.
- **Pass condition**: At least three named phase headers present. Cross-phase bleed is absent: no scoring rows appear under GENERATE, no new candidate names introduced under SCORE or DECIDE.

**Origin**: Round 1, V-05 (Combined, 95). Phase headers enforce the separation between candidate generation, scoring, and decision. Without them, prompts that combine generation and scoring in a single instruction allow phase-bleed: scores get applied before the full candidate set is established, or constraints get re-evaluated mid-score rather than at generation time. Phase structure is also the structural prerequisite that makes C-11 verifiable -- you cannot confirm generation-time enforcement without a visible GENERATE phase boundary.

---

## Scoring Formula

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/4 * 10)
```

**Golden threshold**: All essential pass AND composite >= 80.

**Current score ceiling**: 95/100 (C-09 unimplementable until `--validate` skill flag exists).

---

## Scoring Summary Template

| Criterion | Tier | Pass? |
|-----------|------|-------|
| C-01 Candidate Volume | essential | |
| C-02 Five-Role Scoring Matrix | essential | |
| C-03 Collision Check | essential | |
| C-04 Top Pick Named + Justified | essential | |
| C-05 Constraint Parsed + Applied | essential | |
| C-06 Disqualification Logic | recommended | |
| C-07 Runner-Up + Fallback Rationale | recommended | |
| C-08 Findings Register | recommended | |
| C-09 --validate Flag Behavior | aspirational | |
| C-10 Domain Vocabulary Extraction | aspirational | |
| C-11 Generation-time Constraint Enforcement | aspirational | |
| C-12 Phase-structured Output | aspirational | |

**Composite score**: ___
**Golden**: [ ] All essential pass AND composite >= 80
