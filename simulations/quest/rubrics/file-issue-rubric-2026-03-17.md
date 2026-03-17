Rubric written to `simulations/quest/rubrics/file-issue-rubric-v1-2026-03-17.md`.

**Summary of criteria:**

**Essential (4)** — all must pass for golden:
- **C-01** All four required fields captured (skill, expected, actual, severity)
- **C-02** Severity uses valid enum: `crash` / `wrong-output` / `missing-feature` / `improvement`
- **C-03** GitHub issue format present (title + labeled body sections)
- **C-04** Local artifact written to `simulations/feedback/`

**Recommended (3):**
- **C-05** Actionable title — names skill + symptom, not generic
- **C-06** Reproducibility context — enough for a maintainer to act
- **C-07** Repo open offer presented to user

**Aspirational (2):**
- **C-08** Severity-appropriate framing (crash = urgent, improvement = constructive)
- **C-09** Enriching context (version, chain, topic, related artifacts)

Golden threshold: all 4 essential pass + composite >= 80.
