---
skill: quest-rubric
skill_target: prove-interview
date: 2026-03-15
version: 1
---

# prove-interview Rubric — v1

## Skill Summary

Simulate stakeholder or customer interviews using persona-driven methodology. For each interview subject: their role, their prior knowledge, questions asked, answers given (in the persona's voice), surprising moments, evidence extracted. The interview is a simulation — not real — but grounded in the persona's documented knowledge and concerns.

---

## Essential Criteria (60 points total, 4 criteria × 15 pts each)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Persona identity declared** | correctness | essential | Each interview subject has an explicit role or title stated before any questions are posed. An artifact that opens with questions before establishing who is being interviewed fails. Anonymous or role-free subjects fail. |
| C-02 | **Answers in persona voice** | behavior | essential | Answers read as coming from the declared persona — vocabulary, framing, and concerns match the stated role. Generic answers that could belong to any persona regardless of role fail. |
| C-03 | **Evidence explicitly extracted** | coverage | essential | At least one concrete evidence item (insight, concern, requirement, contradiction, or signal) is explicitly extracted per interview subject — not left implicit in the dialogue. An artifact with transcript only and no extraction phase fails. |
| C-04 | **Surprising or confirming moment documented** | depth | essential | At least one interview subject produces a moment labeled or called out as unexpected, surprising, or as explicit confirmation or contradiction of a prior expectation. An artifact with no epistemic marking of interview outcomes fails. |

---

## Recommended Criteria (30 points total, 3 criteria × 10 pts each)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Prior knowledge scoped per subject** | correctness | recommended | Each subject's prior knowledge, background context, or what they care about is stated before their answers are given — not inferred from their answers. A persona whose knowledge scope is discovered only through their answers does not pass. |
| C-06 | **Questions probe declared concerns** | depth | recommended | At least one question per subject directly addresses a concern or domain declared in the persona setup (C-01 or C-05). Questions that are fully generic and make no contact with the specific persona profile do not pass. |
| C-07 | **Multiple distinct personas interviewed** | coverage | recommended | The simulation includes at least two interview subjects with meaningfully different roles, knowledge levels, or concerns — not minor variations of the same profile. A second subject who echoes the first without adding distinct perspective does not satisfy coverage. |

---

## Aspirational Criteria (10 points total, 2 criteria × 5 pts each)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Cross-persona synthesis present** | depth | aspirational | After all interviews, the output includes a synthesis section identifying patterns, contradictions, or tensions across subjects and connecting individual evidence items into a composite signal. A synthesis that merely lists the per-subject findings without connecting them fails. Gradable only when N >= 2 subjects; scored N/A for single-subject runs. |
| C-09 | **Evidence tagged by signal type** | format | aspirational | Each extracted evidence item carries an explicit signal category annotation (e.g., `[risk]`, `[preference]`, `[constraint]`, `[validation]`, `[invalidation]`). Annotations must be present on the extracted items — not inferred by a reader from prose. Enables downstream `/topic:` namespace to aggregate evidence by type. |

---

## Scoring Reference

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
```

| Result | Meaning |
|--------|---------|
| All C-01..C-04 pass + composite >= 80 | Golden — meets threshold |
| All C-01..C-04 pass + composite < 80 | Essential passing, weak recommended/aspirational |
| Any C-01..C-04 fail | Below threshold regardless of composite score |

---

## Notes

- "Persona" in this skill is a simulated human stakeholder or customer, not a UI/UX persona archetype. C-02 fails if answers sound like a product feature explanation rather than a human's perspective on a problem.
- C-04 is the minimum epistemic bar: the simulation must surface something the team didn't already know or explicitly confirm/deny. A transcript that produces no signal distinction from a feature document fails.
- C-08 is N/A for single-subject runs. When N=1, aspirational denominator is 1 (C-09 only); max aspirational contribution is 10 pts.
- Grounding (answers referencing the persona's plausible domain knowledge) is captured by C-02 — answers must match the declared role. Invented facts outside the persona's stated knowledge domain constitute a C-02 failure.
