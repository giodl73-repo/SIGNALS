Rubric written to `simulations/quest/rubrics/prove-hypothesis-rubric-2026-03-14.md`.

**Structure:**
- **5 essential** (C-01 through C-05): claim, falsification conditions, numeric confidence, experiment list, no goalpost movement
- **3 recommended** (C-06 through C-08): prior signals note, confirmation conditions, evidence-backed confidence rationale
- **2 aspirational** (C-09, C-10): experiment-to-falsification mapping, risk-ranked order

**Design decisions:**
- C-05 (no goalpost movement) isn't in the trace findings but is the behavioral guarantee that makes the whole skill meaningful — added it as essential
- The three trace findings (SF-01, SF-02, SF-03) map cleanly to C-06, C-03, and C-07
- Failure modes call out the three violations that make an output unsalvageable regardless of partial credit
d false. Conditions must be testable (observable outcome, not opinion). |
| C-03 | **Confidence level (0-100)** | correctness | essential | Output states a numeric confidence value 0-100 with a brief rationale. Missing, qualitative-only ("medium"), or unexplained numbers fail. |
| C-04 | **Experiment list** | coverage | essential | Output lists two or more named experiments tied to proving or falsifying the claim. Generic "run tests" fails; named prove sub-skills (prove:interview, prove:prototype, etc.) pass. |
| C-05 | **No goalpost movement** | behavior | essential | Hypothesis is declared before any evidence is discussed. Output must not adjust the claim or falsification conditions in response to findings already presented in the same artifact. |

---

## Recommended Criteria (30 pts total -- output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Prior signals note** | behavior | recommended | Output explicitly states whether prior prove artifacts exist for this topic ("No prior investigation signals found" or lists what was loaded). Silence on this point fails. |
| C-07 | **Confirmation conditions** | depth | recommended | Output includes a "what would confirm this" section alongside the falsification conditions. At minimum one positive confirmation criterion is stated. |
| C-08 | **Confidence rationale references prior evidence** | depth | recommended | The confidence rationale cites at least one concrete prior signal, trace finding, or known friction point -- not just intuition. Pure intuition rationale fails. |

---

## Aspirational Criteria (10 pts total -- raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Experiment-to-falsification mapping** | depth | aspirational | Each experiment is explicitly mapped to one or more falsification conditions it will test. A table or inline annotation is acceptable. |
| C-10 | **Risk-ranked experiment order** | format | aspirational | Experiments are ordered by their likelihood of falsifying the hypothesis (highest-risk experiment first), with rationale. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 2) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Modes (auto-fail regardless of score)

- Claim is adjusted after evidence is introduced in the same artifact (violates C-05)
- No numeric confidence value present (violates C-03)
- Fewer than two named experiments (violates C-04)

---

## Rubric Notes

Derived from trace artifact `plugin-prove-hypothesis-2026-03-14.md`.
Findings SF-01, SF-02, SF-03 drove C-06, C-03, and C-07 respectively.
C-05 (no goalpost movement) was not surfaced as a finding but is the core behavioral
guarantee of the skill -- omitting it would make the rubric trivially passable.
