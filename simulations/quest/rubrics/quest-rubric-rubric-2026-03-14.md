Written to `simulations/quest/rubrics/quest-rubric-rubric-2026-03-14.md`.

**Design rationale:**

The five essential criteria form a complete "is this rubric usable?" gate:
- **C-01** — structural completeness (all fields present)
- **C-02** — weight distribution in spec (3-5 / 2-3 / 1-2)
- **C-03** — the scoring formula is correct and stated
- **C-04** — criteria are actually about the skill, not generic quality
- **C-05** — pass conditions are binary, not subjective

The trickiest one to get right in practice is **C-04** — the most common failure mode for rubric generation is producing criteria like "output is well-structured" that could apply to any skill. A rubric for `quest-rubric` should talk about weight counts, formula presence, and skill-specific criteria — not generic document quality.

**C-09** (calibration) is deliberately aspirational because it requires a human reviewer to run a thought experiment; it can't be checked mechanically until we have real golden/poor output pairs to compare.
on contains all five fields, with no field left blank or missing. |
| C-02 | **Weight distribution is within spec** — The rubric contains 3–5 essential criteria, 2–3 recommended criteria, and 1–2 aspirational criteria. | essential | correctness | Count of essential in [3,5]; count of recommended in [2,3]; count of aspirational in [1,2]. |
| C-03 | **Composite score formula and golden threshold are stated correctly** — The rubric declares the composite formula (60/30/10 split) and the golden threshold (all essential pass + composite >= 80). | essential | correctness | Formula present with weights 60, 30, 10 for essential/recommended/aspirational bands; threshold stated as >= 80 with the all-essential-pass precondition. |
| C-04 | **Criteria are skill-specific** — Essential criteria test the actual non-negotiable behaviors of the target skill, not generic document quality (no criteria like "is well-written" or "is complete"). | essential | correctness | At least 3 of the essential criteria name specific behaviors, outputs, or structural properties unique to the target skill; none are purely generic quality signals. |
| C-05 | **Pass conditions are binary and testable** — Every pass condition can be evaluated as pass/fail without subjective judgment; each uses observable signals (counts, presence/absence, specific patterns, measurable thresholds). | essential | behavior | All pass conditions use verifiable criteria; none require subjective assessment ("good", "sufficient", "appropriate" without a measurable anchor). |

---

## Recommended Criteria

These improve rubric usability. A rubric without them is acceptable but weaker.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Criteria ordered by weight tier** — Essential criteria appear before recommended, recommended before aspirational. Each tier is clearly separated and labeled. | recommended | format | Sections appear in order: essential → recommended → aspirational, with distinct headers or table sections per tier. |
| C-07 | **Categories drawn from the allowed set** — Every criterion's category is one of the five canonical values: correctness, depth, format, coverage, behavior. No invented categories. | recommended | correctness | All category fields contain only: correctness, depth, format, coverage, or behavior. |
| C-08 | **Essential criteria cover distinct failure modes** — No two essential criteria test the same behavior; together they catch at least four distinct ways an output can fail to be useful. | recommended | coverage | No two essential criteria have overlapping pass conditions; reviewers can identify at least four distinct failure modes caught by the essential set. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Rubric is calibrated** — A reviewer using this rubric can correctly classify a mediocre output (scores < 80) and an excellent output (scores >= 80) without ambiguity. At least one essential criterion would catch a real failure in a poor output. | aspirational | depth | Reviewer can produce a concrete example of a poor output that fails >= 1 essential criterion, and a strong output that passes all essential and >= 2 recommended criteria. |
| C-10 | **Evolution hook present** — The rubric acknowledges it should grow as quest-golden discovers excellence patterns; frontmatter includes a `version` field and/or the document includes a note about how the rubric should be updated over time. | aspirational | behavior | Frontmatter has `version` field populated; OR document contains a section/note describing how the rubric should evolve as golden outputs are discovered. |

---

## Notes

This rubric is version 1. It should grow as `/quest:golden` runs against `/quest:rubric` outputs and surfaces excellence patterns not yet captured here. Likely additions:
- Criterion for ID sequential ordering (C-01, C-02... with no gaps)
- Criterion for frontmatter completeness (skill, skill_target, date, version all present)
- Criterion for rubric self-applicability (can the rubric score itself?)
