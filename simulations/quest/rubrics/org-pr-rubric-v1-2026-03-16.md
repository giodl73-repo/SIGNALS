---
skill: quest-rubric
skill_target: org-pr
date: 2026-03-16
version: 1
---

# Scoring Rubric — org-pr

**Skill**: org-pr
**Purpose**: Run a PR through the full org. Each relevant role reviews the diff from their
perspective; output includes per-role findings with P1/P2/P3 severity, consensus analysis,
and a go/no-go recommendation.

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total)

Pass all five or the output is not useful.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Multi-role coverage** — at least two roles from the defined role set (architect, security, testing, compliance, performance, UX) produce findings. | coverage | Output contains 2+ labeled reviewer sections, each from a named role in the defined set. Sections must contain at least one finding. |
| C-02 | **P1/P2/P3 severity on every finding** — every finding carries a severity tag; no finding is left unclassified. | correctness | Every finding line or block includes a P1, P2, or P3 tag. Zero untagged findings. If no findings: reviewer section states "No findings" explicitly. |
| C-03 | **File-based role selection rationale** — the skill explains why each selected role was included based on what changed in the diff. | correctness | Each reviewer section (or a selection manifest before the sections) identifies which changed files or areas triggered that role's inclusion. A role selected without rationale fails this criterion. |
| C-04 | **Explicit go/no-go recommendation** — output closes with a clear go or no-go verdict, not a list of findings left for the reader to interpret. | correctness | Output contains a labeled "Go / No-Go" or "Recommendation" block with a single-word verdict (Go or No-Go) and a one-sentence basis. Verdict must be derivable from the findings — not contradicted by them. |
| C-05 | **Per-role structure** — each reviewer's section is clearly labeled with the role name and visually separated so findings can be attributed without ambiguity. | format | Each reviewer section opens with a heading or label containing the role name. Findings from different roles cannot be parsed as belonging to the same section. |

---

## Recommended Criteria (weight: 30 pts total)

Output is better with these. Not required for a useful result, but expected in mature skill runs.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Consensus analysis** — cross-role themes and conflicts are surfaced explicitly, not left for the reader to discover. | depth | Output includes a cross-role section (or equivalent summary block) that names: (a) any finding raised by two or more roles independently (convergence signal), and (b) any pair of roles with incompatible assessments of the same surface (conflict signal). If neither exists, the section states "No convergence or conflicts detected." |
| C-07 | **P1 blocks go** — the go/no-go formula is consistent: any open P1 finding produces a no-go verdict. | correctness | If one or more P1 findings appear anywhere in the output, the overall verdict is No-Go. A Go verdict with an unresolved P1 finding anywhere in the output is a formula violation and fails this criterion. |
| C-08 | **Actionable findings** — findings name the specific file, function, area, or code pattern that triggered the concern, not generic observations. | depth | At least 80% of findings include a specific locator: file name, line range, component name, or named code pattern. Findings that say only "there may be a security risk" without a locator do not satisfy this criterion. |

---

## Aspirational Criteria (weight: 10 pts total)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Author-blind perspective** — findings read as if reviewers had no access to the author's intent; no charitable interpretation of ambiguous patterns. | depth | At least one finding per active reviewer section challenges an assumption embedded in the diff rather than its stated behavior. Findings that only confirm what the diff intended to do do not satisfy this criterion for that section. |
| C-10 | **Non-obvious issue surfaced** — the output includes at least one finding the author is unlikely to have self-identified: a cross-cutting concern, a latent interaction, or an omission not visible from the changed files alone. | coverage | Output contains at least one finding labeled or classified as a cross-cutting concern, an omission, or an out-of-diff interaction risk. The finding must be traceable to a role perspective not replicated by the author's own discipline. |

---

## Criterion Reference Table

| ID | Text (short) | Weight | Category |
|----|-------------|--------|----------|
| C-01 | Multi-role coverage (2+ roles produce findings) | essential | coverage |
| C-02 | P1/P2/P3 on every finding | essential | correctness |
| C-03 | File-based role selection rationale | essential | correctness |
| C-04 | Explicit go/no-go recommendation | essential | correctness |
| C-05 | Per-role labeled structure | essential | format |
| C-06 | Consensus analysis (convergence + conflicts) | recommended | depth |
| C-07 | P1 blocks go (formula consistency) | recommended | correctness |
| C-08 | Actionable findings with locators | recommended | depth |
| C-09 | Author-blind challenge perspective | aspirational | depth |
| C-10 | Non-obvious cross-cutting issue surfaced | aspirational | coverage |

---

## Scoring Worksheet

```
Essential (N=5):   C-01[_] C-02[_] C-03[_] C-04[_] C-05[_]
  essential_pass = __ / 5
  essential_pts  = essential_pass / 5 * 60 = __

Recommended (N=3): C-06[_] C-07[_] C-08[_]
  recommended_pass = __ / 3
  recommended_pts  = recommended_pass / 3 * 30 = __

Aspirational (N=2): C-09[_] C-10[_]
  aspirational_pass = __ / 2
  aspirational_pts  = aspirational_pass / 2 * 10 = __

Composite = essential_pts + recommended_pts + aspirational_pts = __

Golden = all essential pass AND composite >= 80? [YES / NO]
```
