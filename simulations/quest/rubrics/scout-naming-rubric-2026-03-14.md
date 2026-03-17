Written to `simulations/quest/rubrics/scout-naming-rubric-2026-03-14.md`.

**10 criteria, 3 tiers:**

| ID | Text | Tier | Category |
|----|------|------|----------|
| C-01 | Candidate Volume (10-15) | essential | correctness |
| C-02 | Five-Role Scoring Matrix + weights | essential | correctness |
| C-03 | Collision Check (namespace + external) | essential | coverage |
| C-04 | Top Pick Named + Justified | essential | correctness |
| C-05 | Constraint Parsed + Applied | essential | behavior |
| C-06 | Disqualification Logic labeled | recommended | correctness |
| C-07 | Runner-Up + Fallback Rationale | recommended | depth |
| C-08 | Findings Register (SF-NN) | recommended | depth |
| C-09 | `--validate` flag pins row 1 + Validation Summary | aspirational | behavior |
| C-10 | Domain Vocabulary Extraction logged | aspirational | depth |

The `--validate` design gap from SF-01 in the trace became C-09 (aspirational) — the skill doesn't support it yet, so it's the bar to clear once essentials are stable.
egy -- and a weighted composite is shown. Weights must match or approximate: PM 25%, Strategy 25%, GTM 20%, UX 20%, Design 10%.
- **Pass condition**: Scoring table present with all 5 role columns plus a weighted/composite column. Declared weights sum to 100%. No role omitted.

---

### C-03 -- Collision Check Performed

- **Weight**: essential
- **Category**: coverage
- **Text**: Output performs at least two classes of collision check: (1) internal namespace collision against known plugin namespaces, and (2) external collision against package registries or notable brand/domain overlap.
- **Pass condition**: Both collision classes explicitly mentioned with at least one concrete result (hit or clear) for the top candidate.

---

### C-04 -- Top Pick Named and Justified

- **Weight**: essential
- **Category**: correctness
- **Text**: Output names exactly one top pick, states its composite score, and gives a rationale grounded in the scoring dimensions (not just "it scored highest").
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

---

### C-10 -- Domain Vocabulary Extraction Logged

- **Weight**: aspirational
- **Category**: depth
- **Text**: Output surfaces the domain vocabulary it extracted from CLAUDE.md or plugin-plan.md as a setup step, showing which terms seeded or influenced candidate generation.
- **Pass condition**: At least 5 domain vocabulary terms listed in a setup or extraction step, with an explicit note that they came from a named source file.

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

**Composite score**: ___
**Golden**: [ ] All essential pass AND composite >= 80
