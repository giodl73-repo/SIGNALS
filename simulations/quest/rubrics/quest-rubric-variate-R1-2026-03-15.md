---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 1
---

# Rubric: quest-variate

Evaluates output from the `quest-variate` skill, which generates N distinct prompt variations
of a skill body. Each variation must be complete and runnable, vary along exactly one axis,
and carry a labeled hypothesis.

---

## Criteria

### Essential (must all pass — without these the output is not useful)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Completeness** — Every variation is a full, standalone skill body, not a diff or patch against a base. | correctness | essential | Each V-NN block can be copied into a skill file and executed without referencing any other variation. No "same as V-01 except..." constructs. |
| C-02 | **Count** — Output contains exactly N variations (default 5 when N is unspecified), labeled V-01 through V-0N in sequence. | correctness | essential | Variation count matches the requested N. Labels are sequential with no gaps. |
| C-03 | **Axis declaration** — Each variation declares its variation axis and a hypothesis, both present and non-empty. | format | essential | Every V-NN header or preamble includes an `axis:` field naming one of the six defined axes, and a `hypothesis:` field stating the expected behavioral effect. |
| C-04 | **Single-axis isolation** — Each variation changes exactly one axis relative to a shared baseline. No variation combines multiple axis changes unless the run is explicitly a combination pass. | correctness | essential | Reading two variations side-by-side, the structural difference maps to exactly one named axis. Changes that bleed across axes are a fail. |
| C-05 | **Axis diversity** — No two variations share the same axis (unless N > 6, in which case repeats are allowed only if the hypothesis tests a different setting of the same axis). | coverage | essential | For N <= 6, all variation axes are distinct. |

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Axis breadth** — Variations collectively sample at least four of the six defined axes: role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity. | coverage | recommended | Count distinct axes present across all variations. Pass if >= 4 of the 6 canonical axes are represented. |
| C-07 | **Hypothesis specificity** — Each hypothesis is falsifiable and names the observable behavioral outcome (not just "will be different"). | depth | recommended | Hypothesis states a concrete prediction: what the evaluator should see change in output, how to detect it, or what scoring dimension it affects. "Output will be more concise" passes; "will vary" fails. |
| C-08 | **Structural fidelity** — Each variation preserves the structural skeleton of a valid Signal skill body (frontmatter, description, steps/body, output contract). | correctness | recommended | All required skill sections are present in every variation even when their content changes. Missing sections in any variation is a fail. |

### Aspirational (raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Combination readiness** — Output includes a brief note (or appendix) identifying which axis pairs are high-priority candidates for combination runs and why. | depth | aspirational | At least one combination recommendation is present with a stated rationale referencing the hypotheses from the single-axis variations. |
| C-10 | **Evaluation order guidance** — Output suggests a sequencing for which variations to evaluate first to maximize learning per run (e.g., cheapest axis to test, most structurally impactful). | behavior | aspirational | An explicit ordering or priority tier is present, with a rationale connecting to axis cost or hypothesis independence. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready output |
| Acceptable | all essential + 70-79 | Minor gaps, usable with review |
| Marginal | all essential + < 70 | Structural gaps, iterate before use |
| Fail | any essential fails | Not usable regardless of total score |

---

## Quick Checklist (for manual scoring)

- [ ] C-01: Every variation is a complete, standalone skill body
- [ ] C-02: Exactly N variations, labeled V-01 through V-0N
- [ ] C-03: Each variation has `axis:` and `hypothesis:` fields
- [ ] C-04: Each variation changes exactly one axis
- [ ] C-05: No two variations share the same axis (for N <= 6)
- [ ] C-06: At least 4 of 6 canonical axes represented
- [ ] C-07: Each hypothesis names a concrete, observable behavioral outcome
- [ ] C-08: All variations preserve required skill body structure
- [ ] C-09: Combination candidates identified with rationale
- [ ] C-10: Evaluation order or priority tier provided
