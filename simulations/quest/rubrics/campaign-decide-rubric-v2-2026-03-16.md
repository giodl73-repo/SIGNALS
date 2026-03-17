Rubric written to `simulations/quest/rubrics/campaign-decide-rubric-v2-2026-03-16.md`.

**What changed from v1:**

Two new aspirational criteria extracted from V-02's R1 excellence signals:

| ID | Criterion | Why it's new |
|----|-----------|-------------|
| C-11 | **Per-phase required-field schema** | V-01 passed C-06 (document structure) but scored 60. V-02 scored 100 because its per-phase table schemas forced every criterion to appear by construction. C-06 and C-11 are independent: a brief can have titled sections (C-06 pass) without per-phase required rows (C-11 fail). |
| C-12 | **Templated citation syntax** | V-02's `Because (cite by Phase): - [claim] because Phase [N], [section]` is mechanically auditable. V-01's generic "cite evidence" instruction passes C-05 but leaves citation format open. C-12 scores whether the format itself is prescribed, not just whether citations are present. |

**Scoring formula update:** aspirational denominator moves from `/2` to `/4`. Max composite stays 100. R1 re-scores: V-02 remains 100, V-01 becomes `60 + 0 + 0 = 60` (C-11/C-12 both fail), V-03 becomes `48 + 0 + 5 = 53` (C-09/C-10 pass but C-11/C-12 fail, Bronze).
defer/pivot) recommendation. Absence of a stated recommendation is an automatic fail. |
| C-02 | **Confidence level stated** | correctness | essential | Recommendation is accompanied by a stated confidence (e.g., High/Medium/Low or a numeric percentage). A recommendation without confidence is incomplete. |
| C-03 | **All six sub-skill domains represented** | coverage | essential | Output contains distinct sections or evidence blocks attributable to each of the six orchestrated skills: competitors, feasibility, market, hypothesis, web-search evidence, and synthesis. Missing any domain means the campaign is incomplete. |
| C-04 | **Inertia-first competitor framing** | correctness | essential | The competitor analysis leads with incumbent/inertia forces (status-quo cost, switching cost, or "why people don't change") before listing named rivals. The orchestration spec requires this ordering. |
| C-05 | **Evidence-to-recommendation traceability** | correctness | essential | The recommendation is visibly grounded in evidence from the brief (citations, section references, or explicit "because" statements). A recommendation that floats free of its evidence base fails. |

---

## Recommended Criteria (30 pts total — output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Structured decision brief format** | format | recommended | Output uses a consistent document structure: titled sections, a summary block, and a clear recommendation block. Prose-only dumps without section hierarchy do not pass. |
| C-07 | **Risk and counter-evidence acknowledged** | depth | recommended | Brief surfaces at least one risk, caveat, or piece of counter-evidence that could undermine the recommendation. A one-sided brief fails this criterion. |
| C-08 | **Hypothesis disposition explicit** | depth | recommended | Each hypothesis entered into prove-hypothesis has an explicit outcome (confirmed / refuted / inconclusive). Hypotheses that disappear without resolution fail this criterion. |

---

## Aspirational Criteria (10 pts total — raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Confidence calibration narrative** | depth | aspirational | Brief explains *why* confidence is rated as it is — naming the specific evidence gaps or strength factors that drove the rating, not just asserting a level. |
| C-10 | **Actionable next steps conditioned on recommendation** | behavior | aspirational | If build: output includes a concrete next step (e.g., scope spike, prototype). If no-build: output includes an exit condition or revisit trigger. Generic "further research needed" does not pass. |
| C-11 | **Per-phase required-field schema** | format | aspirational | Each evidence phase has its own structured schema with required named rows (not just an overall summary block). The brief is verifiable at the phase level. A single recommendation block with no per-phase field structure does not pass. |
| C-12 | **Templated citation syntax in recommendation** | correctness | aspirational | The recommendation's evidence citations follow a prescribed format (e.g., "because Phase [N], [section reference]"), making traceability mechanically auditable at a glance. Free-prose citations such as "as shown above" or "based on the evidence" do not pass. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Ready for golden use |
| Silver | >= 60, all essential pass | Usable, recommended gaps noted |
| Bronze | < 60 or any essential fail | Not yet fit for purpose |

---

## Evaluation Notes

- **C-04 (inertia-first)** is the most commonly missed essential criterion. Reviewers should
  check that competitor content opens with status-quo forces, not a named-player list.
- **C-05 (traceability)** should be evaluated by asking: could a reader trace each claim in
  the recommendation back to a specific evidence block? If not, fail.
- **C-08 (hypothesis disposition)** is recommended because prove-hypothesis is a core
  sub-skill; orphaned hypotheses signal a shallow synthesis pass.
- When scoring C-09, "High confidence because we found three independent sources confirming
  X" passes; "High confidence" alone does not.
- **C-11 (per-phase schema)** distinguishes a brief that is structurally enforceable from one
  that relies on the model to self-organize. V-02 hit 100 by construction; V-01 hit 60 despite
  passing all essentials because C-11/C-12 patterns were absent.
- **C-12 (templated citation)** is the difference between "evidence is present somewhere"
  (C-05 pass) and "evidence is pinnable to a specific phase and section." Score C-05 and C-12
  independently: a brief can pass C-05 with prose citations and still fail C-12.
