Rubric written to `simulations/quest/rubrics/validate-inertia-rubric-2026-03-17.md`.

**Structure summary:**

- **5 essential (C-01–C-05):** per-persona mapping, quantified switching cost, per-persona inertia scores, kill-barrier callout, aggregate risk verdict — the four hard deliverables the skill description promises
- **3 recommended (C-06–C-08):** workaround satisfaction, habit lock-in + social proof coverage, mitigation path for the kill barrier
- **2 aspirational (C-09–C-10):** scoring methodology transparency, time-dependent inertia trajectory

The kill-barrier criterion (C-04) is essential because the AMEND clause treats it as the primary sharpening move — a rubric that let it slide optional would miss the point of the skill.
user personas and maps each to one or more inertia factors (workaround satisfaction, switching cost, habit lock-in, social proof, learning curve). Generic "users" without persona differentiation fails. |
| C-02 | **Quantified switching cost** | correctness | At least one persona has a switching cost expressed as a measurable value — time (hours/days), money, effort rating (e.g., 1-10), or steps required. Qualitative-only descriptions ("it's hard") fail. |
| C-03 | **Per-persona inertia score** | correctness | Each mapped persona has an explicit inertia score or risk level (numeric or Low/Medium/High/Critical). Score must be distinct per persona — a single blanket score for all personas fails. |
| C-04 | **Kill-barrier identification** | depth | Output identifies exactly one barrier called out as the adoption killer — the single factor most likely to block adoption even if all other inertia is resolved. Must be labeled or emphasized distinctly (e.g., "critical barrier", "adoption killer"). |
| C-05 | **Overall adoption inertia risk** | correctness | Output produces an aggregate inertia risk verdict (Low/Medium/High/Critical or equivalent scale) with a sentence of rationale tying it back to the per-persona scores. |

---

## Recommended Criteria (output is better with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Current workaround satisfaction assessed** | coverage | For at least one persona, output explicitly describes how satisfied they are with their current workaround and why that satisfaction creates inertia. "They have no workaround" is valid if explained. |
| C-07 | **Habit lock-in and social proof addressed** | coverage | Output addresses habit lock-in (behavioral/muscle memory resistance) AND social proof requirements (whether adoption depends on seeing peers adopt first) for at least one persona each. Missing both fails; covering one partially passes. |
| C-08 | **Mitigation path per critical barrier** | depth | For the kill barrier identified in C-04, output proposes at least one concrete mitigation (feature change, onboarding tweak, migration tool, pricing lever, etc.) that could reduce or eliminate that barrier. |

---

## Aspirational Criteria (raise the bar)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Inertia score methodology explained** | behavior | Output briefly explains how inertia scores were derived -- what factors were weighted and why -- so a reviewer can sanity-check or recalibrate the scoring. A single sentence per dimension suffices; absent any explanation fails. |
| C-10 | **Adoption timeline sensitivity** | depth | Output estimates how inertia evolves over time: does switching cost decrease as the ecosystem matures, or does habit lock-in compound? Must include at least one time-dependent statement (e.g., "after 6 months of workaround use, lock-in doubles"). |

---

## Notes

- A rubric pass requires **all 5 essential criteria** to pass individually.
- Partial credit within a criterion is not applied -- each criterion is binary (pass/fail).
- If the skill output focuses on a single persona (AMEND mode), C-01 and C-03 pass with one persona provided it is named and specific.
- Quantification in C-02 may use relative scales (e.g., "3x more steps than current workflow") when absolute values are not estimable.
