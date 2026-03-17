Done. Here is the complete v3 rubric:

---

**`simulations/quest/rubrics/quest-rubric-rubric-v3-2026-03-14.md`**

**What changed from v2:**

Three new aspirational criteria from R2 excellence signals:

| ID | Signal | What it tests |
|----|--------|---------------|
| C-14 | design-rationale-first | Design rationale section appears **before** the first criteria table -- position makes inertia framing causally prior to construction, not retrospective |
| C-15 | stacked-self-application-plus-rejection-log | Design rationale contains both a named criterion ID (poor-output thought experiment) AND a rejected generic criterion in the same section -- both slots populated simultaneously |
| C-16 | amend-as-three-gate-check | Amend/revision step contains three distinct explicit questions: generic-vs-specific, binary-pass-condition testability, redundant-failure-mode overlap; N/A if skill has no revision phase |

Also added:
- **N/A handling rule** in Scoring: structurally inapplicable criteria excluded from both numerator and denominator
- **Self-application slot** in Notes (C-15 requirement): names C-04 as the failure-point criterion for a poor output; describes a strong output that passes all essential and recommended
- **Rejection log** updated with a third entry ("criteria are high quality" -- circular, no testable signal)
- **v4 candidates** section updated

**Self-scoring projection (v3 against itself):**
- C-14 PASS (design rationale block precedes the Essential table)
- C-15 PASS (rejection log + C-04 poor-output example in same Notes section)
- C-16 N/A (no amend step; excluded from denominator)
IL if the skill design does not include a revision phase.

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
| C-14 | **Design rationale precedes criteria tables** -- The design rationale section (or equivalent intent block) appears in the output document before the first criteria table. Position is not cosmetic: when inertia framing and failure-mode enumeration are written before the criteria exist, they constrain construction rather than rationalizing it after the fact. V-04 and V-05 had identical content; only V-05 satisfied the positional gate. | aspirational | format | Design rationale section (or equivalent block describing dominant failure mode, rejected criteria, or construction intent) appears before the first Essential criteria table in the document; no criteria table appears above the design rationale text. |
| C-15 | **Self-application and rejection log co-present in design rationale** -- The design rationale contains both (1) a self-application result naming at least one essential criterion ID that a concrete poor output would fail, and (2) at least one named rejected generic criterion. Both slots are populated in the same section with zero mutual interference. V-05 was the only R2 variation to achieve both simultaneously. | aspirational | depth | Design rationale section contains: (1) at least one essential criterion ID cited as the failure point for a described poor output, AND (2) at least one explicitly rejected generic criterion named by its text; both items present in the same design rationale section, not distributed to separate appendices or notes. |
| C-16 | **Amend step covers all three primary criterion failure modes as distinct gates** -- The rubric prompt's amend or revision step addresses all three primary ways a criterion can fail: (1) the criterion text is generic rather than skill-specific, (2) the pass condition is not binary and testable, (3) the criterion duplicates a failure mode already caught by another criterion. Each failure mode is a distinct explicit question, not bundled into freeform editorial guidance. | aspirational | behavior | Amend or revision checklist contains three distinct questions explicitly addressing: (1) generic-vs-specific content, (2) binary-pass-condition testability, (3) redundant-failure-mode overlap; all three present and distinct; none merged into a single open-ended revision prompt. N/A if the skill design includes no revision phase. |

---

## Scoring

**Composite formula**: (essential_pass_count / essential_total) * 60 + (recommended_pass_count / recommended_total) * 30 + (aspirational_pass_count / aspirational_total) * 10

**Golden threshold**: all essential criteria pass AND composite score >= 80.

PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

N/A on a criterion excludes it from both numerator and denominator for that band.

---

## Notes

This rubric is version 3. Changes from v2:

- Added C-14 (design-rationale-first): positional requirement that design rationale precedes criteria tables; R2 showed V-04 and V-05 had identical content but only V-05 satisfied the positional gate -- the structural property was the decisive discriminator.
- Added C-15 (stacked-self-application-plus-rejection-log): requires both C-09 evidence (named criterion ID + poor output) and C-13 evidence (rejected generic criterion) to co-exist in the same design rationale section; V-05 was the only R2 variation to achieve both simultaneously.
- Added C-16 (amend-as-three-gate-check): requires the amend/revision step to cover all three primary criterion failure modes as distinct questions, converting revision from freeform editorial to structured validation gate.
- Added N/A handling rule to Scoring section for structurally inapplicable criteria.

Rejected generic criteria (specificity filter log):
- "output is well-structured" -- rejected; tests document aesthetics, not rubric correctness
- "is clear and complete" -- rejected; subjective with no measurable anchor
- "criteria are high quality" -- rejected; circular; provides no testable signal

Self-application against this rubric (C-15 slot):
- Poor output: a rubric whose Essential criteria are "criteria are well-written", "rubric is complete", "output is useful" -- fails C-04 (no skill-specific behaviors named); C-04 is the failure-point criterion.
- Strong output: a rubric with 4 essential criteria naming specific output structures, binary pass conditions throughout, and a design rationale paragraph before the first table -- passes all essential and all recommended.

Candidates for v4:
- Criterion for frontmatter completeness (skill, skill_target, date, version all present and populated)
- Criterion for criterion ID sequential ordering (C-01, C-02... with no gaps or reuse)
- Refinement of C-16 to sharpen the N/A boundary (when is "no revision phase" a design decision vs. an omission?)

This rubric should continue to grow as /quest:golden runs against /quest:rubric outputs and new excellence signals are extracted from scorecards.
