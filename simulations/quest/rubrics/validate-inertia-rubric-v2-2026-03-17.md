Done. Here's a summary of what changed in v2:

**Two new aspirational criteria extracted from Round 1:**

| ID | Source | Pattern |
|----|--------|---------|
| C-11 | V-05 | Kill barrier stated as hypothesis *before* persona analysis. V-05 was the only variant to score full aspirational on C-03 — because Phase 1 makes it structurally impossible to bury or derive the barrier post-hoc from persona aggregation. |
| C-12 | V-03 | Status-quo framed as a competitor, forcing "why they chose it" reasoning. V-03 scored "PASS — strongest of all variants" on C-04 specifically because it asked *why the persona adopted the incumbent*, not just what they currently use. |

**Point redistribution:** Aspirational tier stays at 10 pts. C-09 and C-10 drop from 5 to 3 pts each; C-11 and C-12 get 2 pts each.

**Also fixed:** C-01's pass condition was truncated in v1 (the file started mid-paragraph). v2 includes the full rubric from header to footer.
sonas, each with a role and a role-grounded reason why they would resist adoption (e.g., "Maya -- senior backend engineer who owns the deployment pipeline, won't cede build control"). Generic statements not tied to a specific persona fail. |
| C-02 | **Switching cost quantified** | correctness | essential | At least one switching cost is expressed in concrete units: time (hours/days to migrate), money (license delta, tooling cost), effort (number of steps, files to touch), or risk (rollback complexity). Vague language ("high cost", "some effort") does not pass. |
| C-03 | **Kill barrier named** | correctness | essential | Output explicitly names the single barrier most likely to block adoption entirely -- labeled as such (e.g., "kill barrier", "adoption stopper", "the one thing that would prevent adoption"). Must be specific to this feature, not a generic observation. |
| C-04 | **Workaround satisfaction assessed** | correctness | essential | Output evaluates how well the current workaround already solves the problem for at least one persona -- including what the workaround is and why it feels "good enough" to that persona. |
| C-05 | **Per-persona inertia score present** | format | essential | Each analyzed persona receives a discrete inertia score on a consistent scale (e.g., 1-5, Low/Medium/High/Critical, or 0-10). All scores must use the same scale and appear in the output. |

*Each essential criterion is worth 12 pts. Failure of any essential criterion renders the output not useful regardless of other scores.*

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Habit lock-in addressed** | depth | recommended | Output goes beyond cost analysis to identify a behavioral or habitual pattern (muscle memory, workflow ritual, team convention) that would cause the persona to revert even after initial adoption. Must be persona-specific, not generic. |
| C-07 | **Social proof requirement mapped** | depth | recommended | Output identifies what social proof threshold a skeptical persona would need before adopting -- e.g., "needs to see 3 teammates use it first", "requires a public case study from a similar team", "won't move until their tech lead endorses it". |
| C-08 | **Learning curve quantified** | depth | recommended | At least one persona's learning curve is expressed in concrete terms: ramp time estimate, number of new concepts to internalize, or comparison to something the persona already knows ("similar to learning X, which took Y"). |

*Each recommended criterion is worth 10 pts.*

---

## Aspirational Criteria (10 pts total)

*Aspirational criteria reward structural sophistication. Partial credit is common; full pass is rare. Point weights redistributed in v2 to accommodate C-11 and C-12.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Overall risk rating with mitigation** | depth | aspirational | Output synthesizes per-persona scores into an overall adoption inertia risk level (Low/Medium/High/Critical) AND proposes at least one specific mitigation per barrier identified -- actionable enough to include in a launch plan. Mitigation must target the kill barrier named in C-03; restating the barrier as a recommendation does not pass. | 3 pts |
| C-10 | **Inertia asymmetry identified** | correctness | aspirational | Output distinguishes between personas for whom inertia is structural (will not adopt without product changes) vs. behavioral (can be overcome with onboarding/framing), and calls out which personas represent permanent lost TAM vs. delayed adoption. | 3 pts |
| C-11 | **Kill barrier hypothesized before persona analysis** | structure | aspirational | Kill barrier is stated as an explicit hypothesis in the first section of the output, before any per-persona analysis begins. The hypothesis must be feature-specific (not derived from persona aggregation). This structural sequencing prevents the kill barrier from being buried, genericized, or synthesized post-hoc. | 2 pts |
| C-12 | **Status-quo treated as competitor** | depth | aspirational | Output reasons about why at least one persona *chose* or *stays with* the incumbent/workaround -- not just what it is, but why they selected it. Uses framing such as "they adopted X because...", "X won this persona because...", or "the reason they haven't switched is..." that captures an adoption decision, not merely current state. | 2 pts |

---

## Scoring Reference

| Score Range | Interpretation |
|-------------|----------------|
| 100 | All criteria pass -- exemplary output |
| 80-99 | Golden threshold met -- output is useful and publishable |
| 60-79 | Essential pass but recommended gaps -- usable, needs improvement |
| < 60 | One or more essential criteria fail -- output is not useful |

---

## Reviewer Notes

- C-01 and C-03 are the two criteria most commonly failed by shallow outputs. If both fail, the output is a generic risk list, not an inertia analysis.
- C-02 passes if at least one cost is quantified; not all costs need numbers.
- C-05 fails if personas receive narrative assessments with no discrete score -- the score is the primary artifact.
- C-09 mitigation must target the kill barrier named in C-03; restating the barrier as a recommendation does not pass.
- C-10 is strictly aspirational: structural vs. behavioral inertia is a sophisticated distinction that requires domain knowledge about the persona's org context.
- C-11 is achievable only when the output is structured as a two-phase analysis (barrier hypothesis → persona analysis). Single-phase outputs that derive the kill barrier at the end fail this criterion even if C-03 passes.
- C-12 is strengthened by competitor framing at the prompt level (e.g., "treat the current workaround as a competitor"). Outputs that merely describe what a persona uses without reasoning about the adoption decision do not pass.

---

## Version Notes

**v2 changes (2026-03-17):**
- Added C-11: Kill barrier sequenced first -- extracted from V-05 excellence signal (Phase 1 hypothesis before persona analysis produced the strongest C-03 results across all variants)
- Added C-12: Status-quo as competitor -- extracted from V-03 excellence signal (competitor framing produced the strongest C-04 results across all variants, including "why they chose it" reasoning)
- Redistributed aspirational point weights: C-09=3, C-10=3, C-11=2, C-12=2 (total aspirational tier unchanged at 10 pts)
- Completed C-01 pass condition (was truncated in v1)
