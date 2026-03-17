---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 2
prior_version: quest-rubric-variate-R1-2026-03-15.md
---

# Rubric: quest-variate (v2)

Evaluates output from the `quest-variate` skill, which generates N distinct prompt variations
of a skill body. Each variation must be complete and runnable, vary along exactly one axis,
and carry a labeled hypothesis.

**v2 changes**: Added C-11 through C-14 from Round 1 excellence signals. Updated scoring
formula to account for 4 additional aspirational criteria. No essential or recommended
criteria changed.

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
| C-11 | **Hypothesis negation clause** — Each hypothesis includes an explicit failure condition stating what outcome would disprove the prediction, not just what it predicts. | depth | aspirational | At least one hypothesis in the set contains a "if [criterion] does NOT change..." or equivalent negation clause that makes the failure mode concrete and detectable. Scoring considers the weakest hypothesis; a set where every hypothesis has a negation clause is a full pass. |
| C-12 | **Anchor variation designation** — One variation in the set is explicitly named as the structural anchor for all combination runs, with a rationale grounded in structural impact and isolation quality. | behavior | aspirational | A single variation is designated "combination anchor" (or equivalent) and the designation is justified by reference to the axis's structural centrality — not merely listed as a candidate. Presence of a rationale distinguishes this from C-09's combination candidates list. |
| C-13 | **Register-level isolation** — Across all non-phrasing-register variations, the instructional voice register (terse vs. verbose, directive vs. exploratory) is consistent. Phrasing drift is detectable when a non-phrasing variation reads noticeably differently in tone from the others. | correctness | aspirational | A side-by-side comparison of any two non-phrasing-register variations reveals no detectable shift in instructional register. Terse phrasing in one and verbose in another is a fail unless phrasing-register is the declared axis for one of them. |
| C-14 | **Output-contract axis coherence** — When a variation introduces a new structural element (role, phase, framing), the output contract evolves to include fields that capture the artifact of that element, and those new fields are directly attributable to the variation's declared axis. | format | aspirational | New header fields or label fields present in a variation can be traced to the declared axis. Generic additions with no axis connection are a fail. Variations whose axis does not introduce new structural elements are exempt. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

Partial credit on essential criteria (e.g., C-04 PARTIAL) counts as 0.5 toward the
essential numerator. Aspirational partial credit counts as 0.5 toward the aspirational
numerator.

**Golden threshold**: all 5 essential criteria pass (no partials) AND composite >= 80.

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
- [ ] C-11: At least one hypothesis includes an explicit negation/failure clause
- [ ] C-12: One variation explicitly designated as combination anchor with structural rationale
- [ ] C-13: No register-level drift across non-phrasing-register variations
- [ ] C-14: New output-contract fields in structural variations are axis-attributable

---

## Criterion Genealogy

| Criterion | Source | Round introduced |
|-----------|--------|-----------------|
| C-01 | Design (completeness is hardest essential to miss) | v1 |
| C-02 | Design (count and label format) | v1 |
| C-03 | Design (axis declaration) | v1 |
| C-04 | Design (single-axis isolation — theoretical core) | v1 |
| C-05 | Design (axis diversity — prevents degenerate output) | v1 |
| C-06 | Design (axis breadth) | v1 |
| C-07 | Design (hypothesis specificity — distinguishes testable from trivial) | v1 |
| C-08 | Design (structural fidelity) | v1 |
| C-09 | Design (combination readiness) | v1 |
| C-10 | Design (evaluation order) | v1 |
| C-11 | R1 excellence: V-04 hypothesis named as "Best in set" for including explicit failure condition | v2 |
| C-12 | R1 excellence: V-04 named as "combination anchor" — distinct from C-09's candidate list | v2 |
| C-13 | R1 excellence: V-03 C-04 PARTIAL flagged register-level bleed despite structural isolation holding | v2 |
| C-14 | R1 excellence: V-05 added axis-attributable fields (champion-stance, challenger-stance) to output contract | v2 |
