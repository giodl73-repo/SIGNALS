Rubric written to `simulations/quest/rubrics/validate-inertia-rubric-2026-03-17.md`.

**Structure:**

- **5 essential** (60 pts): per-persona inertia analysis, quantified switching cost, kill barrier named, workaround satisfaction assessed, per-persona inertia score present
- **3 recommended** (30 pts): habit lock-in, social proof requirement, learning curve quantified
- **2 aspirational** (10 pts): overall risk rating with mitigation, inertia asymmetry (structural vs. behavioral)

**Key design decisions:**
- C-03 (kill barrier) is the hardest to pass — requires explicit labeling and feature-specificity, not generic risk language
- C-05 enforces the score artifact as a discrete value on a consistent scale — narrative-only outputs fail
- C-10 (aspirational) distinguishes permanent lost TAM from delayed adoption, which is the sophisticated insight this skill should eventually produce
grounded ("a senior dev who owns the current Makefile won't give up control of the build step"). |
| C-02 | **Switching cost quantified** | correctness | essential | At least one switching cost is expressed in concrete units: time (hours/days to migrate), money (license delta, tooling cost), effort (number of steps, files to touch), or risk (rollback complexity). Vague language ("high cost", "some effort") does not pass. |
| C-03 | **Kill barrier named** | correctness | essential | Output explicitly names the single barrier most likely to block adoption entirely -- labeled as such (e.g., "kill barrier", "adoption stopper", "the one thing that would prevent adoption"). Must be specific to this feature, not a generic observation. |
| C-04 | **Workaround satisfaction assessed** | correctness | essential | Output evaluates how well the current workaround already solves the problem for at least one persona -- including what the workaround is and why it feels "good enough" to that persona. |
| C-05 | **Per-persona inertia score present** | format | essential | Each analyzed persona receives a discrete inertia score on a consistent scale (e.g., 1-5, Low/Medium/High/Critical, or 0-10). All scores must use the same scale and appear in the output. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Habit lock-in addressed** | depth | recommended | Output goes beyond cost analysis to identify a behavioral or habitual pattern (muscle memory, workflow ritual, team convention) that would cause the persona to revert even after initial adoption. Must be persona-specific, not generic. |
| C-07 | **Social proof requirement mapped** | depth | recommended | Output identifies what social proof threshold a skeptical persona would need before adopting -- e.g., "needs to see 3 teammates use it first", "requires a public case study from a similar team", "won't move until their tech lead endorses it". |
| C-08 | **Learning curve quantified** | depth | recommended | At least one persona's learning curve is expressed in concrete terms: ramp time estimate, number of new concepts to internalize, or comparison to something the persona already knows ("similar to learning X, which took Y"). |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Overall risk rating with mitigation** | depth | aspirational | Output synthesizes per-persona scores into an overall adoption inertia risk level (Low/Medium/High/Critical) AND proposes at least one specific mitigation per barrier identified -- actionable enough to include in a launch plan. |
| C-10 | **Inertia asymmetry identified** | correctness | aspirational | Output distinguishes between personas for whom inertia is structural (will not adopt without product changes) vs. behavioral (can be overcome with onboarding/framing), and calls out which personas represent permanent lost TAM vs. delayed adoption. |

---

## Scoring Reference

| Score Range | Interpretation |
|-------------|----------------|
| 100 | All criteria pass -- exemplary output |
| 80-99 | Golden threshold met -- output is useful and publishable |
| 60-79 | Essential pass but recommended gaps -- usable, needs improvement |
| < 60 | One or more essential criteria fail -- output is not useful |

## Reviewer Notes

- C-01 and C-03 are the two criteria most commonly failed by shallow outputs. If both fail, the output is a generic risk list, not an inertia analysis.
- C-02 passes if at least one cost is quantified; not all costs need numbers.
- C-05 fails if personas receive narrative assessments with no discrete score -- the score is the primary artifact.
- C-09 mitigation must target the kill barrier named in C-03; restating the barrier as a recommendation does not pass.
- C-10 is strictly aspirational: structural vs. behavioral inertia is a sophisticated distinction that requires domain knowledge about the persona's org context.
