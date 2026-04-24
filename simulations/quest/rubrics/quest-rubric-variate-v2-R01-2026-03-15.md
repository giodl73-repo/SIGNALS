---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-15
version: 2
round: R1
changes: Added C-11 (discriminating pass conditions), C-12 (calibration example), C-13 (phase-gate enforcement) from R1 excellence signals
---

# Rubric: quest-rubric (v2)

Evaluates output from the `quest-rubric` skill, which produces a scoring rubric for a named
Signal skill. The rubric must function as a working objective function: each criterion must be
independently checkable, the tiers must follow the structural contract, and the essential
criteria must be grounded in the target skill's actual non-negotiable behaviors — not generic
quality observations that would apply to any output.

**v2 additions**: Three aspirational criteria extracted from R1 excellence signals — the inertia
test (V-05), the concrete discrimination example (V-04), and phase-gate enforcement (V-01).

---

## Criteria

### Essential (must all pass — without these the output is not useful)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Field completeness** — Every criterion entry contains all five required fields: ID (C-NN), text with a bold label, weight (essential/recommended/aspirational), category (correctness/depth/format/coverage/behavior), and a pass condition. | format | essential | Count the fields present for each criterion. Pass if no criterion is missing any of the five fields. A criterion with "see above" or an empty pass condition is a fail. |
| C-02 | **Tier count compliance** — The rubric contains 3-5 essential criteria, 2-3 recommended criteria, and 1-2 aspirational criteria — no more, no fewer. | correctness | essential | Count criteria in each tier. Pass only if all three counts fall within the specified ranges. A rubric with 2 essential criteria or 4 recommended criteria fails immediately. |
| C-03 | **Essential criteria grounded in target skill** — Essential criteria cover behaviors that are specific and non-negotiable for the named target skill, not generic output-quality criteria that would apply to any skill. | correctness | essential | Read the essential criteria and ask: could these criteria be copy-pasted unchanged onto a rubric for a completely different skill? Pass if fewer than 2 of the essential criteria are purely generic (e.g., "output is well-formatted" with no connection to the skill contract). |
| C-04 | **Testable pass conditions** — Every pass condition names a specific, observable outcome that an evaluator can verify without subjective judgment. | correctness | essential | For each pass condition, ask: can two independent evaluators reach the same pass/fail verdict without discussion? Pass conditions containing only vague language ("good", "sufficient", "appropriate") with no concrete anchor are a fail. |
| C-05 | **Composite score formula and golden threshold present** — The rubric includes the composite scoring formula using the standard weights (essential 60, recommended 30, aspirational 10) and states the golden threshold condition. | format | essential | Check that the score section contains a formula matching the standard composite structure and a golden threshold statement. Missing formula or threshold is a fail. |

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Category diversity** — Criteria span at least three distinct categories across the full rubric, avoiding clustering in a single dimension. | coverage | recommended | Count distinct categories used. Pass if >= 3 of the 5 canonical categories (correctness/depth/format/coverage/behavior) appear across all criteria. |
| C-07 | **Criteria ordered by severity within tiers** — Within the essential tier, criteria are listed from most structurally critical (output unusable if this fails) to least. Same ordering principle applied to recommended and aspirational tiers. | depth | recommended | Read the essential criteria in order. If swapping C-01 and C-04 would produce a more logical triage sequence, the ordering fails. Pass if the first essential criterion represents the single highest-stakes failure mode for the target skill. |
| C-08 | **Quick checklist present** — Output includes a checklist block (markdown checkboxes) summarizing all criteria IDs and their key assertion for rapid manual scoring. | format | recommended | A checklist section exists with one checkbox line per criterion referencing its ID and a short description. Pass if all criteria IDs appear in the checklist. |

### Aspirational (raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Criteria enable iteration** — When a criterion fails, its pass condition gives enough specificity that the output author knows exactly what to fix without running the skill again to ask. Each criterion's failure mode is self-describing. | behavior | aspirational | For each criterion, ask: if this criterion failed, does the pass condition text tell the author the minimum change needed to achieve a pass? Pass if >= 80% of criteria have self-describing failure modes (not just "does not pass"). |
| C-10 | **No redundancy or contradiction** — No two criteria overlap such that passing one guarantees passing the other, and no two criteria impose logically contradictory requirements on the output. | depth | aspirational | For each pair of criteria, ask: is there a rubric output that passes one but fails the other for a non-trivial reason? If two criteria always agree, they are redundant and one should be folded in. Pass if all criteria add unique signal with no fully-overlapping pair. |
| C-11 | **Discriminating pass conditions** — Each pass condition tests a behavior that a generic rubric ("the output is clear and comprehensive") would fail to catch. Distinct from C-04 (observability): a condition can be observable but still redundant with a vague rubric if it checks only structural presence rather than skill-specific contract fulfillment. | correctness | aspirational | For each pass condition, ask the inertia test: "Could a rubric that says 'the output is clear and comprehensive' still pass this condition?" If yes for any pass condition, that condition has not been sharpened enough. Pass if every pass condition names at least one count, named field, structural pattern, or enumeration that only the target skill's contract could supply — not shared structural minimums. |
| C-12 | **Calibration example present** — The rubric includes at least one concrete positive/negative pair showing the boundary between acceptable and failing output for the most critical essential criterion. The pair must name the skill — e.g., "generic: 'output is low quality' / grounded: 'the output has no formula so quest-golden cannot compute a composite score'" — so a new evaluator can self-calibrate without a training session. | behavior | aspirational | A calibration example block exists containing one labeled generic example (shows what NOT to write) and one labeled grounded example (shows what to write) for at least one essential criterion. Both examples must reference the target skill by name or reference its output contract. Pass if a reader unfamiliar with the rubric could use the pair to correctly classify two additional borderline cases. |
| C-13 | **Phase-gate enforcement present** — The rubric's structure includes at least one hard gate that blocks forward progress until a structural requirement is verified. A gate must be explicit (e.g., "DO NOT proceed to the next step until...") and must reference a checkable condition, not an aspiration. | behavior | aspirational | A gate statement is present using explicit blocking language ("DO NOT proceed", "stop here", "must complete before advancing"). The gate condition is checkable: it names a count, a field, or a structural property, not a quality judgment. Pass if violating the gate would result in a detectably incomplete output (the gated step is one that earlier steps feed). |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Note**: aspirational denominator is now 5 (C-09 through C-13).

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric — use as objective function |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

---

## Quick Checklist (for manual scoring)

- [ ] C-01: Every criterion has all five required fields (ID, text, weight, category, pass condition)
- [ ] C-02: Exactly 3-5 essential, 2-3 recommended, 1-2 aspirational
- [ ] C-03: Essential criteria are specific to the target skill, not generic quality observations
- [ ] C-04: Every pass condition is testable by two independent evaluators without discussion
- [ ] C-05: Composite score formula and golden threshold are present
- [ ] C-06: At least 3 distinct categories represented across all criteria
- [ ] C-07: Essential criteria ordered from most to least structurally critical
- [ ] C-08: Quick checklist present with all criterion IDs
- [ ] C-09: Each failing criterion tells the author what to fix without re-running the skill
- [ ] C-10: No two criteria are redundant or contradictory
- [ ] C-11: Every pass condition fails the inertia test (a "clear and comprehensive" rubric would miss it)
- [ ] C-12: At least one concrete generic/grounded example pair present for an essential criterion
- [ ] C-13: At least one hard phase gate with explicit blocking language and a checkable condition
