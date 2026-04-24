Rubric written to `simulations/quest/rubrics/discover-causal-rubric-2026-03-17.md`.

**Design decisions:**

- **5 essential criteria** covering the four explicit skill outputs (pathway, falsification, inertia check, AMEND narrowing) plus the evidence-in-context assessment that's easy to skip
- **C-03 (inertia check) as essential** — the skill description calls this "the most commonly skipped eval," so it must be mandatory, not optional
- **C-04 separates AMEND presence from C-08 AMEND quality** — existence of the amendment is essential; actionability is recommended, since a rubric that fails on vague amendments would be too strict for early rounds
- **Falsification framing in C-02** is intentionally strict: "metric didn't move" is not a mechanism falsification — it must describe what a *broken mechanism* looks like (e.g., users see the feature but behavior doesn't change at the expected step)
- **C-09/C-10 aspirational** — evidence grading and multi-pathway analysis are genuinely harder and not needed for the rubric to be useful on first runs
describe what a broken mechanism would look like). |
| C-03 | **Inertia check performed** | coverage | essential | Response directly asks and answers whether doing nothing (no feature, status quo) would also produce outcome Y. Must not omit this check or treat it as optional. |
| C-04 | **Causal claim narrowed in AMEND** | behavior | essential | Output includes an AMEND section that produces a revised, narrower version of the original causal claim -- more precise scope, conditions, or population than the input hypothesis. Restating the original does not pass. |
| C-05 | **Context evidence assessed** | correctness | essential | Response evaluates whether evidence that the mechanism holds exists in the feature's specific context (team, product, users). "We don't have evidence yet" is a valid answer; silence is not. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Mechanism pathway is testable** | depth | recommended | The described pathway is specific enough that a team could design an observation or test to confirm or deny it. Vague pathways ("X leads to better outcomes") do not pass; named measurable steps do. |
| C-07 | **At least one confounder or alternative cause identified** | depth | recommended | Response names at least one plausible alternative explanation for Y that does not involve X, or a confounding variable that could create the appearance of X causing Y. |
| C-08 | **AMEND output is actionable** | behavior | recommended | The narrowed claim in AMEND is concrete enough to act on -- includes a bounded scope (user segment, condition, timeframe) or a mechanism qualifier. Generic narrowings ("add more evidence") do not pass. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Evidence quality rated** | depth | aspirational | Response distinguishes between evidence types (anecdotal, observed correlation, controlled measurement) and rates the current strength of causal evidence, not just its presence or absence. |
| C-10 | **Multiple causal pathways considered** | depth | aspirational | Response identifies more than one possible causal pathway from X to Y and notes whether they are complementary, competing, or independently falsifiable. |

---

## Scoring Guide

| Range | Interpretation |
|-------|---------------|
| All essential pass + >= 80 | Golden -- meets bar for production use |
| All essential pass + 70-79 | Acceptable -- useful but shallow on recommended |
| Any essential fail | Below bar -- output is unreliable regardless of score |
| < 70 | Below bar |

## Common Failure Modes

- **C-01 fail**: Output confirms the claim ("yes, X causes Y") without tracing the mechanism
- **C-02 fail**: Falsification is stated as a metric threshold ("if retention doesn't go up") rather than a mechanism break
- **C-03 fail**: Inertia check skipped entirely -- most common failure per skill description
- **C-04 fail**: AMEND section restates the original hypothesis or broadens instead of narrows
- **C-05 fail**: Evidence section is generic ("studies show...") without reference to the team's actual context
