---
skill: quest-golden
date: 2026-03-15
source: quest-golden-variate-R5-2026-03-15.md (V-05 body)
pass: QU5 simplification
original_word_count: 728
simplified_word_count: 488
reduction_pct: 33
all_essential_still_pass: true
status: simplified
---

# quest:golden -- Find the Golden Prompt

Skill: [SKILL_NAME]
Rubric version: [VERSION] (criteria C-01 through C-[NN])
Round: [ROUND_NUMBER]

---

## SPREAD-DESIGN PHASE

Assign variation axes before writing any prompt body.

Round 1: Vary one axis per variation (single-axis isolation).
Round 2+: Combine axes that produced spread (PARTIAL or FAIL) in the prior round.
           Consult the PARTIAL AMPLIFIER TRAJECTORY TABLE before finalizing assignments.

PARTIAL AMPLIFIER TRAJECTORY TABLE:

| Round | Axis | Occurrence | Recommended Action |
|-------|------|-----------|-------------------|
| [prior round entries] | | | |

Axis-assignment plan:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | [axis] | [source signal] | [criteria target] | [predicted score] |
| V-02 | | | | |
| V-03 | | | | |
| V-04 | | | | |
| V-05 | | | | |

---

## STEP 1 -- GENERATE 5 VARIATION BODIES

Write 5 complete, runnable skill bodies (V-01 through V-05).
Label each: variation axis and hypothesis.

---

## STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion:
  Result: PASS | PARTIAL | FAIL
  Evidence: [exact text present or absent]

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| [each criterion row] | | | | | | |
| COMPOSITE | | | | | | |
| RANK | | | | | | |

Composite formula: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
PARTIAL counts as 0.5 in aspirational tier.

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For every criterion where at least one variation scores higher than another:
  1. Name the structural property (reusable principle, not just which variation won).
  2. State the mechanism: what prompt property is present in passing variations, absent
     from failing ones.
  3. Causal layer: structural | behavioral | correctness
  4. Provenance: [V-XX, R-N] -- variation and round where this property first appeared.

If no spread exists on any criterion: "No score spread found. Redesign for divergence."

Add any new PARTIAL entries to the PARTIAL AMPLIFIER TRAJECTORY TABLE, marking
Occurrence as First or Repeated.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

For each new excellence pattern, propose:
  ID:             C-[NN]
  Text:           [one-sentence criterion]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

If no new patterns this round: "No new criteria proposed this round."

---

## CONVERGENCE CHECK

GATE 1 (TRIAL): Do all 5 variations pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED
  Evidence: [list which criteria all 5 pass, or which fails]

GATE 2 (PLATEAU): Did Step 3 in THIS round AND in the IMMEDIATELY PRECEDING round
  both find zero new excellence patterns?
  Name both rounds explicitly (e.g., "Round 4 and Round 5: no new patterns found").
  State: QUEST PLATEAUED or QUEST NOT PLATEAUED

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite-scoring variation from this round.
2. Write the full prompt body verbatim to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Include frontmatter: skill, date, rounds-to-convergence, rubric_final, score, status: golden.
   Body: complete, runnable prompt text.
3. Write the final accumulated rubric (all criteria from all rounds) to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
   Every criterion must include: ID, category, text, pass condition, weight, added-in-round.
4. State both artifact paths.
