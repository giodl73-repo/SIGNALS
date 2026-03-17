Written to `simulations/quest/rubrics/prove-interview-rubric-v2-2026-03-14.md`.

---

**What changed from v1:**

Two new aspirational criteria extracted from the V-03 (Role Sequence / Disposition-Ordered) golden signal, the highest-scoring R1 variation at 94/110:

**C-11 — Disposition arc structured** (5 pts)
Captures V-03's structural insight that champion/neutral/skeptic ordering isn't just persona diversity (C-08) — it creates an evidence arc where the *relationship* between dispositions is itself signal. Convergence despite skepticism = strong signal. Skeptic confirming champion without role-grounded resistance = red flag. This is a different thing from C-08's "meaningfully different roles" check.

**C-12 — Critical contradiction named** (5 pts)
Captures V-03's six-dimension synthesis vs. the generic "note contradictions" in C-09. The distinction: listing contradictions passes C-09; *ranking* them and explaining the evidential weight of the most significant one passes C-12. C-09 and C-12 are now a ladder — C-09 is the floor, C-12 is the ceiling.

**Point accounting:** Aspirational section goes from 10 pts to 20 pts, total ceiling from 100 to 110. Golden threshold stays at 80 — still reachable without any aspirational points, so the gate isn't inflated.
m the V-03 (Role Sequence / Disposition-Ordered) excellence signal in Round 1.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Persona identity declared** | correctness | essential | Each interview subject has an explicit role, title, or identity stated before the interview begins. Anonymous or role-free subjects fail. |
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

## Aspirational Criteria (20 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-interview synthesis** | depth | aspirational | After all interviews, the output includes a synthesis section noting patterns, contradictions, or convergences across subjects -- connecting the individual evidence items into a composite signal. |
| C-10 | **Evidence confidence rated** | depth | aspirational | Each extracted evidence item carries an explicit confidence or signal-strength marker (e.g., strong/weak, high/low, confirmed/suspected) with a one-line rationale. |
| C-11 | **Disposition arc structured** | depth | aspirational | Personas include at least one explicit advocate (champion or supporter) and at least one explicit skeptic (critic or resistant voice). The synthesis addresses whether agreement or contradiction between dispositions was the dominant arc signal -- convergence despite skepticism is strong signal; skeptic confirming champion without role-grounded resistance is a red flag. |
| C-12 | **Critical contradiction named** | depth | aspirational | The synthesis section does not merely list contradictions -- it identifies and names the single most significant contradiction between interview subjects and explains its evidential weight (what it confirms, undermines, or leaves unresolved). A synthesis that enumerates contradictions without ranking them fails this criterion. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Passing essential, weak recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite score |

Note: composite ceiling is 110 in v2 (20 aspirational pts). Golden threshold is still 80 -- achievable without any aspirational points.

---

## Partial Credit Reference

| Band | PASS | PARTIAL | FAIL |
|------|------|---------|------|
| Essential (12 pts each) | 12 | 8 | 0 |
| Recommended (10 pts each) | 10 | 3-7 | 0 |
| Aspirational (5 pts each) | 5 | 2-3 | 0 |

---

## Notes

- A "persona" in this skill is a simulated human, not a UI persona. The distinction matters for C-03: the answer must reflect the simulated human's perspective, not a product feature walkthrough.
- C-05 (grounded) is the hardest criterion to satisfy automatically. Evidence of grounding: the answer references the persona's industry, role-specific constraints, or documented concerns. Evidence of failure: the answer is universally applicable platitudes with no role-specific color. A Skeptic whose resistance is "change is hard" fails C-05 regardless of persona labeling.
- C-09 synthesis is only gradable when N >= 2 interview subjects exist. For single-subject interviews, C-09 is scored N/A (excluded from aspirational denominator).
- C-11 is only gradable when N >= 2 interview subjects exist with declared stances. If no disposition labels are present, score C-11 based on whether a structural advocate/skeptic contrast is present in the roles themselves (e.g., sponsor vs. end-user resistance). For single-subject runs, C-11 is N/A.
- C-12 requires the synthesis to explicitly rank contradictions, not merely enumerate them. A synthesis that says "Subject A said X; Subject B said Y" without evaluating which contradiction matters more fails C-12 even if C-09 passes.
- C-11 and C-12 were added in v2 based on the V-03 (Role Sequence / Disposition-Ordered) golden signal in Round 1 scoring. V-03 achieved 94/110 composite -- the highest score of any R1 variation -- driven by its structured disposition arc and six-dimension synthesis including an explicit "Critical contradiction" field.
