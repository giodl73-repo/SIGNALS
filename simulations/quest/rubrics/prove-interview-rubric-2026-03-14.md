Rubric written to `simulations/quest/rubrics/prove-interview-rubric-2026-03-14.md`.

**Summary:**

- **5 essential** (C-01..C-05): persona identity, prior knowledge scoped, answers in persona voice, evidence extracted, grounded not invented
- **3 recommended** (C-06..C-08): surprising moment, question quality (open + follow-up), multiple distinct personas
- **2 aspirational** (C-09..C-10): cross-interview synthesis, evidence confidence rated

The hardest essential to satisfy is **C-05 (grounded)** — it's the criterion that separates a real persona simulation from generic AI output. C-09 synthesis has a graceful N/A rule for single-subject runs to keep scoring fair.
ona identity declared** | correctness | essential | Each interview subject has an explicit role, title, or identity stated before the interview begins. Anonymous or role-free subjects fail. |
| C-02 | **Prior knowledge scoped** | correctness | essential | Each subject's prior knowledge or background context is stated (what they know, what they don't know, what they care about) before answers are given. |
| C-03 | **Answers in persona voice** | behavior | essential | Answers read as coming from the declared persona -- vocabulary, concerns, and framing match the role. Generic AI-sounding answers that could belong to any persona fail. |
| C-04 | **Evidence extracted** | coverage | essential | At least one concrete evidence item (insight, concern, requirement, contradiction, or signal) is explicitly extracted per interview subject -- not left implicit in the dialogue. |
| C-05 | **Grounded, not invented** | correctness | essential | Answers reference the persona's documented domain knowledge or plausible role-based concerns. Answers that invent facts outside the persona's plausible knowledge domain fail. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Surprising moment present** | depth | recommended | At least one interview subject produces an unexpected answer, tension, or reveal -- something the interviewer's questions did not anticipate. The moment is labeled or called out. |
| C-07 | **Question quality** | depth | recommended | Questions are open-ended and probing, not leading or yes/no. At least one follow-up question appears in response to a prior answer within a single interview. |
| C-08 | **Multiple distinct personas** | coverage | recommended | The simulation includes at least two interview subjects with meaningfully different roles, knowledge levels, or concerns -- not minor variations of the same profile. |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-interview synthesis** | depth | aspirational | After all interviews, the output includes a synthesis section noting patterns, contradictions, or convergences across subjects -- connecting the individual evidence items into a composite signal. |
| C-10 | **Evidence confidence rated** | depth | aspirational | Each extracted evidence item carries an explicit confidence or signal-strength marker (e.g., strong/weak, high/low, confirmed/suspected) with a one-line rationale. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Passing essential, weak recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite score |

## Notes

- A "persona" in this skill is a simulated human, not a UI persona. The distinction matters for C-03: the answer must reflect the simulated human's perspective, not a product feature walkthrough.
- C-05 (grounded) is the hardest criterion to satisfy automatically. Evidence of grounding: the answer references the persona's industry, role-specific constraints, or documented concerns. Evidence of failure: the answer is universally applicable platitudes with no role-specific color.
- C-09 synthesis is only gradable when N >= 2 interview subjects exist. For single-subject interviews, C-09 is scored N/A (excluded from aspirational denominator).
