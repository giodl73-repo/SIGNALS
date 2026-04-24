Quest-golden finalized.

**Artifacts on disk:**

| File | Status |
|------|--------|
| `simulations/quest/golden/quest-golden-golden-2026-03-14.md` | Written (was empty) |
| `simulations/quest/scorecards/quest-golden-scorecard-R4-2026-03-14.md` | Already complete |
| `simulations/quest/rubrics/quest-golden-rubric-v3-2026-03-14.md` | Already on disk (v3 final) |

**Golden prompt**: V-01 (minimal structure, 634 words after simplification, 100/100 composite, all 13 criteria pass).

**Rubric trajectory**: v1 (10 criteria) -> v2 (C-11 added, R1) -> v3 (C-12, C-13 added, R2). Stable at v3 across R3+R4.

**3 transferable patterns extracted:**
- E-1: Causal spread-design statement belongs in the generation step, not only the convergence gate
- R2-P1: Generation-phase active instruction required — post-hoc RANK row is not a substitute
- R2-P2: Causal explanation and competitive framing are non-substitutes; causal is mandatory
riation must vary only one axis.
Round 2+: combine axes that produced signal in earlier rounds.

Spread-design rule: if all variations produce identical composite scores, the round
generates no new excellence patterns and does not advance plateau detection. Design
variations to diverge on at least one criterion.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

STEP 2 -- SCORE EACH VARIATION

For each variation, score every criterion (criterion-by-criterion -- not just composite).
Per criterion:
  Result: PASS | PARTIAL | FAIL
  Evidence: [text present or absent]

Produce a summary score matrix (compute composite using rubric formula):

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| C-01      | E  |      |      |      |      |      |
...
| COMPOSITE |    |      |      |      |      |      |
| RANK      |    |      |      |      |      |      |

DO NOT proceed to Step 3 until you have criterion-by-criterion scores for all 5 variations.

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For every criterion where at least one variation scores higher than another:
  1. Name the structural property that caused the difference.
     Write it as a reusable principle -- not which variation won but what design
     choice caused the difference.
  2. Tag its scope: skill-specific | transferable
  3. State the mechanism: the specific prompt property present in passing variations
     and absent from failing ones.

List any criterion all variations fail:
  Diagnosis: rubric-gap | skill-gap

If no variation outperforms any other on any criterion, state:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

DO NOT proceed to Step 4 until all patterns are named and scoped.

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each excellence pattern from Step 3, propose a rubric criterion with all five fields:
  ID:             C-[NN]
  Text:           [criterion description, one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

CONVERGENCE -- CHECK BOTH GATES INDEPENDENTLY

GATE 1 (TRIAL): Do all variations in this round pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED

GATE 2 (PLATEAU): Did Step 3 in this round AND in the immediately preceding round
  both find zero new excellence patterns?
  Name both rounds explicitly (e.g., "Round 3 and Round 4: no new patterns found").
  State: QUEST PLATEAUED or QUEST NOT PLATEAUED

DO NOT declare golden unless both gates are satisfied simultaneously.

WRITE GOLDEN ARTIFACTS (on dual convergence only)

1. Select the highest-composite-scoring variation from this round.
   If tied, select the variation with minimal structure (fewest operator constraints).
2. Write it verbatim -- the full prompt body -- to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Include frontmatter (skill, date, rounds, rubric_final, score, status).
   Body: the complete, runnable prompt text. DO NOT write only a summary.
3. Write the final accumulated rubric (all criteria across all rounds) to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
4. State both artifact paths.
```

---

## What Made It Golden

**3 accumulated excellence patterns drove the v1 -> v3 rubric evolution:**

**E-1 (Round 1 -> C-11, aspirational)**: Prompts that explicitly state *why* uniform-score rounds stall plateau detection produce spread-design incentives that instruction-only approaches lack. The causal statement ("rounds where all variations produce identical composite scores generate no new excellence patterns and do not advance plateau detection") belongs in the generation phase, not only in the convergence gate. Scope: transferable.

**R2-P1 (Round 2 -> C-12, aspirational)**: The generation step must contain an *active* spread-design instruction -- an explicit instruction that causes the operator to produce divergent variations. A post-hoc RANK row in the score matrix is not a substitute. Visibility of spread after it exists does not cause divergent variation design. Scope: transferable.

**R2-P2 (Round 2 -> C-13, aspirational)**: The causal explanation for stalled plateau detection cannot be substituted by competitive framing alone. Competitive framing (champion-defense, inertia) and causal explanation address the same problem through distinct mechanisms; only the causal explanation satisfies C-11. Both may coexist but the causal statement is mandatory. Scope: transferable.

**What the minimal structure adds over a naive implementation:**

1. The spread-design rule is in the *generation* step -- not just the convergence gate. This ensures the operator acts on it before variations are written, not after scoring reveals the problem.
2. The causal statement is explicit ("does not advance plateau detection") -- not implicit in a RANK row or implied by a tie-breaking rule.
3. The DO NOT gates at each step boundary prevent skipping -- the loop is not advisory.
4. Step 3 fallback language is prescribed verbatim -- operators know exactly what to write when no spread exists, removing ambiguity about whether an all-pass round is a failure or a confirmation.

---

## Final Rubric Criteria Summary (v3)

| ID | Weight | Category | Text |
|----|--------|----------|------|
| C-01 | essential | behavior | Full 4-phase loop executed (generate, score, identify, propose) |
| C-02 | essential | behavior | Per-criterion pass/fail shown for every variation |
| C-03 | essential | behavior | Both convergence conditions checked (TRIAL + PLATEAU) |
| C-04 | essential | behavior | Golden prompt artifact written (full body, not summary) |
| C-05 | essential | behavior | Final rubric artifact written (all criteria accumulated) |
| C-06 | recommended | depth | Excellence pattern named and abstracted as reusable principle |
| C-07 | recommended | correctness | Rubric criterion proposed with all 5 fields (ID, text, weight, category, pass condition) |
| C-08 | recommended | behavior | Plateau detection cites both rounds explicitly by name |
| C-09 | aspirational | depth | Score separation across variations (at least one variation scores lower) |
| C-10 | aspirational | coverage | Pattern generalizability stated (skill-specific or transferable) |
| C-11 | aspirational | structure | Prompt explains why uninformative rounds stall plateau detection |
| C-12 | aspirational | structure | Generation phase contains active spread-design instruction |
| C-13 | aspirational | structure | Causal explanation not substituted by competitive framing alone |

**Scoring formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)`
**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Quest Summary

| Round | Variations | Top Score | New Patterns | Gate 1 | Gate 2 |
|-------|-----------|-----------|--------------|--------|--------|
| R1 | 5 | 90 | 1 (E-1 -> C-11) | NOT CONVERGED | NOT PLATEAUED |
| R2 | 5 | 100 | 2 (R2-P1 -> C-12, R2-P2 -> C-13) | CONVERGED | NOT PLATEAUED |
| R3 | 5 | 100 | 0 | CONVERGED | NOT PLATEAUED |
| R4 | 5 | 100 | 0 | CONVERGED | PLATEAUED |

**Dual convergence at R4. Golden written. Rubric final at v3.**
