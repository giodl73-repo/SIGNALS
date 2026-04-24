Rubric written to `simulations/quest/rubrics/quest-golden-rubric-2026-03-14.md`.

**Structure summary:**

**Essential (5 criteria, 60 pts)** — the loop must actually run:
- C-01: Full 4-phase loop executed (generate → score → identify → propose)
- C-02: Per-criterion pass/fail shown for every variation (not just composite)
- C-03: Both convergence conditions checked (trial + plateau), not just one
- C-04: Golden prompt body written to artifact path
- C-05: Final rubric persisted to artifact path

**Recommended (3 criteria, 30 pts)** — the quest produces signal, not just a winner:
- C-06: Excellence pattern named as a reusable principle (QU2), not an instance
- C-07: New rubric criterion has all 5 fields (QU3)
- C-08: Plateau declaration cites the two specific rounds with no new patterns

**Aspirational (2 criteria, 10 pts)** — the variations do useful work:
- C-09: Score spread exists each round (at least one variation scores lower — otherwise nothing was learned)
- C-10: Each pattern is tagged skill-specific vs. transferable

The key design decision: C-03 splits dual convergence into two auditable gates, since the most likely failure is declaring golden after trial convergence but before plateau is confirmed. Six failure modes cover the typical ways the loop short-circuits without producing a usable result.
t plateaued). Declaring convergence when only one condition holds is a hard fail. |
| C-04 | Golden prompt artifact written | essential | behavior | The converged prompt body is written to the skill artifact path (`simulations/quest/golden/{skill}-golden-{date}.md`). An artifact that contains only metadata or a summary without the prompt body is a hard fail. |
| C-05 | Final rubric artifact written | essential | behavior | The final rubric (with all criteria accumulated across rounds) is written to a rubric artifact path. A run that scores but never persists the rubric is a hard fail. |

### Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Excellence pattern named and abstracted (QU2) | recommended | depth | For each round where a variation outperforms others, the run explicitly names what structural property caused the score difference -- not just which variation won. The pattern must be stated as a reusable principle (e.g., "section-first placement forces calibration before rating") not an instance description (e.g., "V-03 passed"). |
| C-07 | Rubric criterion proposed with full fields (QU3) | recommended | correctness | Each new rubric criterion proposed includes all five required fields: ID, text, weight, category, and a clear pass condition. A proposal missing any field does not pass. |
| C-08 | Plateau detection with round count | recommended | behavior | When declaring quest plateau, the run explicitly states which two consecutive rounds produced no new excellence patterns, naming them (e.g., "Round 3 and Round 4: no new patterns found"). A plateau declaration without citing the round evidence does not pass. |

### Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Score separation across variations | aspirational | depth | Variations are designed or selected so that at least one scores lower than the rest in each round, producing an informative spread rather than all-pass or all-fail. A round where all variations produce identical composite scores does not pass -- no signal was extracted from the spread. |
| C-10 | Pattern generalizability stated | aspirational | coverage | Each extracted excellence pattern is explicitly tagged as either skill-specific (applies only to this skill) or transferable (applies to a class of skills). Patterns without a scope statement do not pass. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| QG-01 | C-03 | Run declares convergence after all variations pass the rubric but does not check the 2-round plateau condition -- quest may still have undiscovered excellence patterns |
| QG-02 | C-02 | Run reports "all pass" or a single composite score without showing which criterion each variation passed or failed -- scoring is unauditable |
| QG-03 | C-06 | Run notes V-03 won round 3 but states no reusable principle -- the pattern is buried in the scorecard, not extracted |
| QG-04 | C-04 | Run identifies the golden prompt body in prose but never writes the artifact -- next skill invocation cannot load it |
| QG-05 | C-07 | Run proposes "add a section-ordering criterion" but omits a clear pass condition -- criterion cannot be scored in the next round |
| QG-06 | C-01 | Run generates variations and picks a winner by inspection, skipping the score-then-identify-then-propose loop -- rubric never evolves |
