Rubric written to `simulations/quest/rubrics/discover-causal-rubric-2026-03-17.md`.

**Structure:**

- **5 essential criteria (C-01 to C-05):** causal pathway stated, falsification condition present, inertia check performed, claim is scoped/testable, AMEND directive produced. All must pass.
- **3 recommended (R-01 to R-03):** context-specific evidence, alternative causes/confounders named, mechanism chain decomposed into 2+ hops.
- **2 aspirational (A-01 to A-02):** mechanism strength qualified, inertia baseline quantified/bounded.

The inertia check (C-03) is essential because the skill description calls it "the most commonly skipped eval." The AMEND block (C-05) is essential because without it the skill produces diagnosis but no actionable output — the whole point of the skill is to fix the hypothesis.
s | Output names at least one observable condition that, if true, would disprove the mechanism. "We can't know" or no falsification statement fails. |
| C-03 | **Inertia check performed** | essential | coverage | Output explicitly asks and answers: does doing nothing (or the status quo) also produce Y? If the check is omitted entirely, criterion fails. |
| C-04 | **Causal claim is scoped/testable** | essential | correctness | The output narrows the original claim to a specific context, population, or condition under which the mechanism is expected to hold. A claim that is unfalsifiable by scope ("always causes") fails. |
| C-05 | **AMEND directive produced** | essential | behavior | Output ends with a concrete AMEND block that addresses at least two of: narrow the causal claim, add mechanism pathway, add falsification condition. A missing or empty AMEND fails. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| R-01 | **Context-specific mechanism evidence** | recommended | depth | Output cites at least one piece of evidence (prior result, analogous feature, domain knowledge) that the mechanism has operated or failed in this specific context -- not just in theory. |
| R-02 | **Alternative causes or confounders named** | recommended | coverage | Output identifies at least one alternative explanation for Y that does not involve X, or one confounder that could produce the appearance of X->Y without a true causal link. |
| R-03 | **Mechanism chain has at least two hops** | recommended | depth | The causal pathway is decomposed into at least two intermediate steps (X -> A -> Y), making the mechanism checkable at each hop rather than opaque. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| A-01 | **Mechanism strength qualified** | aspirational | depth | Output assigns a directional confidence to the mechanism (strong/moderate/weak, or equivalent) with a brief rationale -- not just presence/absence. |
| A-02 | **Inertia baseline quantified or bounded** | aspirational | depth | The inertia check produces an estimate or bound on the baseline Y rate without X (e.g., "Y already occurs in ~30% of cases without this feature"), enabling a meaningful comparison. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

---

## Failure Modes to Watch

- **Correlation dressed as causation** -- output restates "X correlates with Y" and calls it a mechanism (fails C-01)
- **Unfalsifiable claim** -- output says the mechanism "always holds" or cannot be tested (fails C-02, C-04)
- **Inertia blind spot** -- the most common skip; output assumes Y only comes from X (fails C-03)
- **AMEND as echo** -- AMEND block just repeats the original hypothesis without narrowing (fails C-05)
- **Generic evidence** -- R-01 fails when evidence cited is domain-generic ("studies show X helps") rather than context-specific
