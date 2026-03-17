Done. Here is the complete updated rubric:

---

```
simulations/quest/rubrics/quest-rubric-rubric-v2-2026-03-14.md
```

**What changed from v1:**

Three new aspirational criteria, each mapping directly to one Round 1 excellence signal:

| ID | Signal source | What it tests |
|----|---------------|---------------|
| C-11 | Inertia framing | Design rationale names the dominant failure mode *before* any criteria table |
| C-12 | Closed-world gates | No bare subjective qualifier in any pass condition without a count/threshold anchor; "no other values" closure enforced |
| C-13 | Rejection log | At least one generic criterion named as explicitly rejected -- proves the specificity filter ran, not just that it was intended |

C-07's pass condition was also tightened with "no other values" closure language (the V-05 pattern that turns an allowlist into a closed world).

A **Scoring** section was added making the PARTIAL-on-essential rule explicit (0.5 for score math, but does not satisfy the all-essential-pass gate).

**Self-scoring projection for this v2 rubric against itself:**
- C-11 PASS (design rationale opens with the failure mode statement)
- C-12 PASS (pass conditions use counts, presence/absence, pattern anchors throughout)
- C-13 PASS (notes section names "output is well-structured" / "is clear and complete" as the rejected generic criteria)
mechanically until real golden/poor output pairs exist.

**C-11 through C-13** are new in v2, extracted from Round 1 excellence signals. They test whether a rubric exhibits the structural properties that distinguish V-05 (97.5) from V-03 (92.5): inertia framing, closed-world pass-condition gates, and a rejection log proving the specificity filter ran.

---

## Essential Criteria

These must all pass. A rubric that fails any essential criterion is not usable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | **All five required fields are present** -- Each criterion row contains: ID, Text, Weight, Category, and Pass Condition. No field is left blank or missing. | essential | format | Every row in every criteria table contains all five fields with no field left blank or missing. |
| C-02 | **Weight distribution is within spec** -- The rubric contains 3-5 essential criteria, 2-3 recommended criteria, and 1-2 aspirational criteria. | essential | correctness | Count of essential in [3,5]; count of recommended in [2,3]; count of aspirational in [1,2]. |
| C-03 | **Composite score formula and golden threshold are stated correctly** -- The rubric declares the composite formula (60/30/10 split) and the golden threshold (all essential pass + composite >= 80). | essential | correctness | Formula present with weights 60, 30, 10 for essential/recommended/aspirational bands; threshold stated as >= 80 with the all-essential-pass precondition. |
| C-04 | **Criteria are skill-specific** -- Essential criteria test the actual non-negotiable behaviors of the target skill, not generic document quality (no criteria like "is well-written" or "is complete"). | essential | correctness | At least 3 of the essential criteria name specific behaviors, outputs, or structural properties unique to the target skill; none are purely generic quality signals. |
| C-05 | **Pass conditions are binary and testable** -- Every pass condition can be evaluated as pass/fail without subjective judgment; each uses observable signals (counts, presence/absence, specific patterns, measurable thresholds). | essential | behavior | All pass conditions use verifiable criteria; none require subjective assessment ("good", "sufficient", "appropriate" without a measurable anchor). |

---

## Recommended Criteria

These improve rubric usability. A rubric without them is acceptable but weaker.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Criteria ordered by weight tier** -- Essential criteria appear before recommended, recommended before aspirational. Each tier is clearly separated and labeled. | recommended | format | Sections appear in order: essential -> recommended -> aspirational, with distinct headers or table sections per tier. |
| C-07 | **Categories drawn from the allowed set** -- Every criterion category is one of the five canonical values: correctness, depth, format, coverage, behavior. No invented categories. | recommended | correctness | All category fields contain only: correctness, depth, format, coverage, or behavior; no other values. |
| C-08 | **Essential criteria cover distinct failure modes** -- No two essential criteria test the same behavior; together they catch at least four distinct ways an output can fail to be useful. | recommended | coverage | No two essential criteria have overlapping pass conditions; reviewers can identify at least four distinct failure modes caught by the essential set. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Rubric is calibrated** -- A reviewer using this rubric can correctly classify a mediocre output (scores < 80) and an excellent output (scores >= 80) without ambiguity. At least one essential criterion would catch a real failure in a poor output. | aspirational | depth | Reviewer can produce a concrete example of a poor output that fails >= 1 essential criterion, and a strong output that passes all essential and >= 2 recommended criteria. |
| C-10 | **Evolution hook present** -- The rubric acknowledges it should grow as quest-golden discovers excellence patterns; frontmatter includes a version field and the document includes a note about how the rubric should be updated over time. | aspirational | behavior | Frontmatter has version field populated; OR document contains a section/note describing how the rubric should evolve as golden outputs are discovered. |
| C-11 | **Inertia framing in design rationale** -- The rubric design rationale names the dominant failure mode for the target skill before listing any criteria. Naming the enemy first anchors every subsequent review decision as a persistent filter rather than a per-criterion afterthought. | aspirational | depth | Design rationale contains an explicit statement of the most common or most dangerous failure mode for the target skill; this statement appears before the first criteria table. |
| C-12 | **Pass conditions use closed-world gates** -- Each pass condition is phrased as a binary gate with explicit unacceptable-signal anchors. Subjective terms ("good", "sufficient", "appropriate", "thorough", "complete") do not appear in pass conditions without a measurable anchor alongside them. | aspirational | behavior | No pass condition contains a bare subjective qualifier without a count, threshold, or presence/absence anchor; OR the rubric explicitly lists banned subjective terms and at least 3 pass conditions demonstrate the pattern ("X is present" / "count >= N" / "none of Y"). |
| C-13 | **Rejection log proves the specificity filter ran** -- The design rationale or notes section names at least one generic criterion that was considered and rejected, with the rejection stated explicitly. Proving the filter ran is stronger than asserting the intent to run it. | aspirational | depth | Design rationale or notes section contains at least one named example of a rejected generic criterion (e.g., "output is well-structured", "is clear and complete") stated as explicitly rejected, not merely implied. |

---

## Scoring

**Composite formula**: (essential_pass_count / essential_total) * 60 + (recommended_pass_count / recommended_total) * 30 + (aspirational_pass_count / aspirational_total) * 10

**Golden threshold**: all essential criteria pass AND composite score >= 80.

PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

---

## Notes

This rubric is version 2. Changes from v1:
- Added C-11 (inertia framing), C-12 (closed-world gates), C-13 (rejection log) as aspirational criteria, extracted from Round 1 excellence signals (V-05 patterns).
- Strengthened C-07 pass condition with "no other values" closure language.
- Added explicit Scoring section with PARTIAL handling rule.

It should continue to grow as /quest:golden runs against /quest:rubric outputs. Candidates for v3:
- Criterion for ID sequential ordering (C-01, C-02... with no gaps)
- Criterion for frontmatter completeness (skill, skill_target, date, version all present)
- Criterion for rubric self-applicability (can the rubric score itself?)
