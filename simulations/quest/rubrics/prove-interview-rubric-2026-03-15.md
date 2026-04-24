Written to `simulations/quest/rubrics/prove-interview-rubric-2026-03-15.md`.

---

**Rubric summary: prove-interview v1**

**5 essential (C-01..C-05)**:
- C-01 — Persona identity declared (correctness)
- C-02 — Prior knowledge scoped (correctness)
- C-03 — Answers in persona voice (behavior)
- C-04 — Evidence explicitly extracted (coverage)
- C-05 — Surprising or confirming moment labeled (depth)

**3 recommended (C-06..C-08)**:
- C-06 — Questions probe declared concerns, with follow-up (depth)
- C-07 — Multiple distinct personas (coverage)
- C-08 — Evidence signal-typed with label taxonomy (behavior)

**2 aspirational (C-09..C-10)**:
- C-09 — Cross-interview synthesis (N/A when N=1)
- C-10 — Simulation fidelity annotated

The hardest essential is **C-03** (persona voice) — it's the criterion that separates grounded simulation from generic AI output. **C-08** (signal-typed evidence) is the recommended criterion with the most downstream value: typed evidence flows directly into the `/topic:` namespace without re-interpretation.
us or role-free subjects fail. |
| C-02 | **Prior knowledge scoped** | correctness | essential | Each subject's prior knowledge and blind spots are stated before answers are given -- what they know, what they don't know, what they care about. A subject with no prior knowledge section fails. |
| C-03 | **Answers in persona voice** | behavior | essential | Answers are written in the declared persona's distinct voice -- vocabulary, concerns, and framing match the role. Answers that could belong to any persona (generic AI output) fail. |
| C-04 | **Evidence explicitly extracted** | coverage | essential | At least one concrete evidence item (insight, concern, requirement, contradiction, or signal) is explicitly extracted per subject -- not left implicit in the dialogue. Evidence listed only inside the transcript without a dedicated extraction phase or section fails. |
| C-05 | **Surprising or confirming moment labeled** | depth | essential | Each subject includes at least one moment labeled SURPRISING or CONFIRMING, tied to an expectation or prior assumption. Unlabeled interesting moments do not count. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Questions probe declared concerns** | depth | recommended | Questions are anchored to the subject's declared role and prior knowledge -- they probe role-specific concerns, not generic topics. At least one follow-up question appears in response to a prior answer within the same interview. |
| C-07 | **Multiple distinct personas** | coverage | recommended | At least two subjects are present with meaningfully different roles, knowledge levels, or priorities -- not minor variations of the same profile. A single subject or near-identical subjects fail. |
| C-08 | **Evidence signal-typed** | behavior | recommended | Each extracted evidence item carries a signal type label (e.g., adoption risk, feasibility concern, requirement gap, scope signal, constraint) making its downstream use in the topic narrative explicit. Unlabeled evidence items fail. |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-interview synthesis** | depth | aspirational | After all interviews, a synthesis section aggregates findings across subjects -- naming patterns, contradictions, or convergences and connecting individual evidence items into a composite signal. (N/A when N=1 subject.) |
| C-10 | **Simulation fidelity annotated** | behavior | aspirational | The output includes a brief meta-note distinguishing grounded claims (based on documented persona knowledge or domain context) from constructed plausibility, naming at least one specific basis. Helps the reader calibrate trust per section. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Passing essential, weak on recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite |

---

## Notes

- A "persona" here is a simulated human stakeholder or customer -- not a UI persona or product feature walkthrough. C-03 requires answers to reflect the simulated human's perspective, concerns, and blind spots.
- C-05 (surprising/confirming moment) requires an explicit label. The criterion is testing whether the output distinguishes expected from unexpected -- not just whether interesting content is present.
- C-08 (signal-typed evidence) is the bridge to the topic namespace: typed evidence can be consumed by `/topic:` skills directly.
- C-09 is N/A for single-subject runs; exclude from the aspirational denominator to avoid penalizing intentionally focused interviews.
