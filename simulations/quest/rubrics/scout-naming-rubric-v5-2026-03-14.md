Looking at the four new patterns from R4:
1. **Anchor rubric tier descriptions** (V-01, V-04, V-05) → C-17
2. **Phase exit condition checklists** (V-02, V-05) → C-18
3. **Generation-time displacement floor** (V-03, V-04, V-05) → C-19
4. **--validate branch diagnostics** (V-05) → C-20

---

# scout-naming Rubric — v5

## What changed from v4 to v5

**Four new aspirational criteria** extracted from R4 patterns:

**C-17 — Anchor Rubric Tier Descriptions** (`depth`)
SETUP declares per-role integer-band tier labels (e.g., 1-3 = weak / 4-6 = adequate / 7-9 = strong / 10 = exceptional) for at least two role dimensions. SCORE assigns tier labels alongside raw integers. DECIDE sub-part (1) references the tier, completing the chain SETUP → SCORE → DECIDE. Makes scoring interpretation output-verifiable by tier label rather than integer judgment alone. V-01, V-04, V-05 pass; V-02, V-03 fail (integers without declared tier anchors).

**C-18 — Phase Exit Condition Checklists** (`behavior`)
At least two phase closings include an explicit `[ ]` checklist of exit conditions. C-03 (collision check) and C-11 (generation-time enforcement) must appear as checklist preconditions — a phase may not close until those items clear. Converts C-03 and C-11 from evaluator-inferred to checklist-enforced. V-02, V-05 pass; V-01, V-03, V-04 fail (no exit checklists).

**C-19 — Generation-time Displacement Floor** (`behavior`)
Status-quo pre-scored in SETUP as a benchmark row using the role weight matrix. At GENERATE, candidates scoring below the status-quo on a declared key dimension are marked `[BELOW-SQ: <dimension>]` and excluded before SCORE. Fraction of candidates beating the status-quo reported at DECIDE. Adds `[below SQ threshold]` as a fourth disqualification class and makes incumbency strength a measurable metric. V-03, V-04, V-05 pass; V-01, V-02 fail (no status-quo benchmark row).

**C-20 — --validate Branch Diagnostics** (`behavior`)
When `--validate` flag is present, output includes a branch that evaluates each C-09 sub-condition individually (row pinned / Validation Summary present / delta notation present / flag recognized), reports PASS/FAIL per sub-condition, and names blocking requirements by category. Independent of full C-09 compliance — clearing C-20 with partial C-09 coverage is valid if diagnostics are explicit. V-05 passes; V-01–V-04 fail (no `--validate` handling).

**Scoring impact**:
- Denominator: 8 → 12 aspirationals
- Max achievable (no C-09): 11/12 × 10 = **9.17** → max score **99.17**
- R4 variations retroactively under v5: V-05 **99.17** (C-17 + C-18 + C-19 + C-20); V-04 **97.50** (C-17 + C-19); V-01 **96.67** (C-17 only); V-02 **96.67** (C-18 only); V-03 **96.67** (C-19 only)

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
| C-15 | Labeled Sub-part Record | aspirational | depth |
| C-16 | Gate 3 Binary Status Flags | aspirational | behavior |
| C-17 | Anchor Rubric Tier Descriptions | **aspirational** | depth |
| C-18 | Phase Exit Condition Checklists | **aspirational** | behavior |
| C-19 | Generation-time Displacement Floor | **aspirational** | behavior |
| C-20 | --validate Branch Diagnostics | **aspirational** | behavior |

**Score ceiling**: 95/100 until C-09 is implemented. Max achievable: 99.17 (clears all except C-09).

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

*(See C-14 for the aspirational prose bar, C-15 for the aspirational structural bar, and C-17 for the aspirational tier-label bar on this criterion.)*

---

### C-05 — Constraint Parsed + Applied

**Pass condition**: If a constraint is present in the input, the output explicitly acknowledges it and applies it. No candidates that violate the constraint appear in the scoring matrix without a disqualification label.

---

## Recommended Criteria

### C-06 — Disqualification Logic Labeled

**Pass condition**: Disqualified candidates carry an explicit label identifying the disqualification class (e.g., `[DISQ: constraint]`, `[DISQ: low Strategy]`, `[DISQ: collision]`). A DISQUALIFIED SUMMARY with tally by class appears in the output.

---

### C-07 — Runner-Up + Fallback Rationale

**Pass condition**: A RUNNER-UP candidate is named with its composite score and at least one sentence of fallback rationale explaining when or why it is preferred over the top pick.

---

### C-08 — Findings Register (SF-NN)

**Pass condition**: Output includes a Findings Register table with SF-NN entries. At minimum one entry addresses anchor calibration or status-quo gap or vocabulary coverage. Entries follow SF-NN numbering.

---

## Aspirational Criteria

### C-09 — `--validate` flag pins row 1 + Validation Summary

**Pass condition**: When `--validate` flag is present, all four sub-conditions pass: (1) top pick from prior run is pinned to Row 1 of the SCORE matrix, (2) a Validation Summary section is present, (3) delta notation from the prior run's stored scores is shown, (4) the flag is recognized and handled in the output. All four required.

*(Infrastructure note: sub-conditions 3 and 4 require prior-run score storage outside the prompt. C-20 captures partial diagnostic progress toward this criterion.)*

---

### C-10 — Domain Vocabulary Extraction logged

**Pass condition**: SETUP phase extracts 5-10 domain vocabulary terms from the source file or invocation context. Vocabulary list is logged with source name. Gate 1 confirmation includes vocabulary count and source.

---

### C-11 — Generation-time Constraint Enforcement

**Pass condition**: Constraint enforcement occurs at GENERATE time, not as a post-hoc filter. Candidates violating the constraint are labeled `[DISQ: constraint]` at the point of generation and are not carried forward to SCORE unmarked.

---

### C-12 — Phase-structured Output

**Pass condition**: Output uses explicit phase separators (e.g., `--- PHASE 1: SETUP ---` through `--- PHASE 4: DECIDE ---`). All four phases present and numbered.

---

### C-13 — Gate Confirmation Count

**Pass condition**: Gate 2 (GENERATE/SCORE boundary) reports a three-value counter: candidates generated, pre-disqualified by constraint, advancing to SCORE.

---

### C-14 — 3-part DECIDE Rationale

**Pass condition**: DECIDE section includes three rationale sub-parts: (1) at least two scoring dimensions with integers and specific reasoning, (2) comparison to status-quo on specific dimensions, (3) vocabulary term connection. All three parts must be substantively populated.

---

### C-15 — Labeled Sub-part Record

**Pass condition**: The TOP PICK block uses explicitly labeled distinct lines for each sub-part: `(1) Dimensions: [...]`, `(2) vs. Status-quo: [...]`, `(3) Vocabulary: [...]`. A missing sub-part is an absent line, not an omitted clause within prose.

---

### C-16 — Gate 3 Binary Status Flags

**Pass condition**: Gate 3 (SCORE/DECIDE boundary) carries binary status flags in addition to a count: `Status-quo benchmarked: yes/no` and `Collisions checked: top 3`. Both flags must be present.

---

### C-17 — Anchor Rubric Tier Descriptions

**Pass condition**: SETUP phase declares per-role integer-band tier labels (e.g., `1-3 = weak / 4-6 = adequate / 7-9 = strong / 10 = exceptional`) for at least two role dimensions. SCORE phase assigns tier labels alongside raw integers (e.g., `Strategy: 8 — strong`). DECIDE sub-part (1) references the declared anchor tier, completing the auditable chain SETUP declares → SCORE assigns → DECIDE cites.

*(Relationship to C-14 and C-15: C-17 requires tier labels from the declared rubric to appear in DECIDE sub-part (1). A variation can clear C-14 and C-15 without C-17 if rationale uses integers alone.)*

---

### C-18 — Phase Exit Condition Checklists

**Pass condition**: At least two phase closings include an explicit `[ ]` checklist of exit conditions that must be satisfied before the phase closes. C-03 (collision check) and C-11 (generation-time enforcement) must each appear as checklist items in their respective phases — converting them from evaluator-inferred observations to checklist-enforced preconditions that block phase close if absent.

---

### C-19 — Generation-time Displacement Floor

**Pass condition**: All three sub-conditions present: (1) status-quo product pre-scored in SETUP as a named benchmark row using the declared role weight matrix, (2) candidates scoring below the status-quo on a declared key dimension marked `[BELOW-SQ: <dimension>]` at GENERATE and excluded before SCORE, (3) fraction of candidates beating the status-quo reported at DECIDE. `[below SQ threshold]` functions as a fourth disqualification class alongside constraint, collision, and score floor.

---

### C-20 — --validate Branch Diagnostics

**Pass condition**: When `--validate` flag is present, the output includes a branch that: (1) evaluates each of the four C-09 sub-conditions individually, (2) reports PASS/FAIL per sub-condition, (3) names blocking requirements by category (e.g., row-position conflict, infrastructure gap). Clearing C-20 with partial C-09 compliance is valid provided diagnostics are explicit and complete.

*(Relationship to C-09: C-20 measures diagnostic quality of `--validate` handling. C-09 requires full compliance. A variation can clear C-20 without clearing C-09 — V-05 R4 demonstrates this: 2/4 C-09 sub-conditions pass, C-20 passes.)*
