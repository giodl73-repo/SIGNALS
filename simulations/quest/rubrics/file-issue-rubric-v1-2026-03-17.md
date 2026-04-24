---
skill: quest-rubric
skill_target: file-issue
date: 2026-03-17
version: 1
---

# Scoring Rubric — `file-issue`

**Skill**: Report a Signal skill issue, unexpected behavior, or improvement idea.
**Purpose**: Captures structured issue data, formats it as a GitHub issue, and logs it locally.

---

## Essential Criteria (60% of score — all must pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Four required fields captured** | correctness | essential | Output contains all four required fields: (1) which skill ran, (2) what was expected, (3) what actually happened, (4) severity level. Missing any field is a fail. |
| C-02 | **Severity uses valid enum** | correctness | essential | Severity is exactly one of: `crash`, `wrong-output`, `missing-feature`, `improvement`. Any other value or omission is a fail. |
| C-03 | **GitHub issue format present** | format | essential | Output includes a GitHub-style issue with a title line and a body containing at least two labeled sections (e.g., **Expected**, **Actual**, **Severity**, **Steps to reproduce**). |
| C-04 | **Local log artifact written to simulations/feedback/** | behavior | essential | Skill writes or clearly specifies an artifact path under `simulations/feedback/`. Path must be non-ambiguous (includes skill name and date or slug). |

---

## Recommended Criteria (30% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Actionable, specific issue title** | format | recommended | The GitHub issue title names the specific skill and the specific problem — not generic phrases like "Bug report" or "Issue with skill". Pass: title contains skill name + symptom or behavior. |
| C-06 | **Sufficient reproducibility context** | depth | recommended | Body includes enough detail for a maintainer to reproduce or understand the issue: what input was given, what the environment was, or what sequence of events led to the problem. A one-sentence description alone is a fail. |
| C-07 | **Repo open offer presented** | behavior | recommended | Skill explicitly offers to open the issue at the Signal repo (e.g., asks the user if they want to open it, or provides a `gh issue create` command). |

---

## Aspirational Criteria (10% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Severity-appropriate framing** | depth | aspirational | Tone and urgency match severity: `crash` uses urgent language and asks for immediate reproduction steps; `improvement` uses constructive, proposal-oriented framing. A `crash` filed with casual improvement language or vice versa is a fail. |
| C-09 | **Skill context enrichment** | coverage | aspirational | Issue body includes at least one enriching context item beyond the four required fields: skill version or date, related skills in the invocation chain, topic name, or a reference to an existing rubric or golden artifact. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

### Score bands

| Composite | Verdict |
|-----------|---------|
| >= 80, all essential pass | Golden |
| >= 60, all essential pass | Acceptable |
| Any essential fail | Not acceptable (regardless of composite) |
| < 60 | Not acceptable |

---

## Rationale

- **C-01/C-02** are the core contract of the skill — capturing the right fields in the right vocabulary. Without them the issue is incomplete or unsortable by severity.
- **C-03** ensures the output is actually usable as a GitHub issue, not just a prose description.
- **C-04** closes the loop on local logging, which is an explicit part of the skill's stated purpose.
- **C-05** prevents noise in the issue tracker — vague titles are unfiled in practice.
- **C-06** distinguishes a useful bug report from a throwaway complaint.
- **C-07** verifies the skill follows through on its "offers to open" promise.
- **C-08/C-09** reflect maturity: a skill that calibrates tone to severity and enriches context produces issues that actually get fixed.
