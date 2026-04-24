---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-15
version: 3
round: R2
changes: Added C-14 (calibration pair lifecycle position), C-15 (sub-step output sequencing), C-16 (multi-level gate architecture), C-17 (audit role separation), C-18 (audit trail captures reasoning) from R2 excellence signals ES-1 through ES-5
---

# Rubric: quest-rubric (v3)

Evaluates output from the `quest-rubric` skill, which produces a scoring rubric for a named
Signal skill. The rubric must function as a working objective function: each criterion must be
independently checkable, the tiers must follow the structural contract, and the essential
criteria must be grounded in the target skill's actual non-negotiable behaviors — not generic
quality observations that would apply to any output.

**v2 additions**: Three aspirational criteria extracted from R1 excellence signals — the inertia
test (V-05), the concrete discrimination example (V-04), and phase-gate enforcement (V-01).

**v3 additions**: Five aspirational criteria extracted from R2 excellence signals — calibration
pair lifecycle position (ES-2/V-03), sub-step output sequencing (ES-1/V-03), multi-level gate
architecture (ES-3/V-03), audit role separation (ES-4/V-05), and audit trail captures reasoning
(ES-5/V-05).

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
| C-14 | **Calibration pair produced at point of drafting** — The calibration pair required by C-12 is written while the pass condition is being drafted, not retrospectively after all criteria are sealed. Retrospective calibration pairs lose context and risk being rationalized from the final condition rather than derived alongside it. | behavior | aspirational | The rubric's workflow positions the calibration pair as a step immediately following pass-condition drafting for each criterion, before the criterion row is sealed. A workflow that permits all calibration pairs to be written at the end, after all criteria rows are finalized, does not pass. The ordering must be: draft pass condition → write calibration pair → seal criterion — not: draft all pass conditions → seal all criteria → write all calibration pairs. |
| C-15 | **Sub-step output sequencing makes omission detectable** — When the rubric requires checking mechanisms (inertia test, calibration pair), each mechanism's output appears as an independent artifact in the output stream before the criterion is recorded in the summary table. A builder who skips a check produces a table row with no preceding artifact — a structural gap detectable by inspection, not a quality judgment. | behavior | aspirational | For each mandatory check step (e.g., inertia test, calibration pair), the rubric's instructions require that step's output to appear in the output before the criterion is entered into the table (not embedded in the table cell or omitted silently). A rubric where all checking can be done mentally with only the final table as output does not satisfy this criterion. Pass if a reviewer scanning the output would see a detectable structural gap — not just a short table cell — wherever a required check was skipped. |
| C-16 | **Multi-level gate architecture** — The rubric enforces gating at two distinct granularities: a phase gate ensuring criterion-building begins from a sufficient structural foundation, and at least one per-criterion gate ensuring each criterion is complete before the next begins. A single gate at either level alone cannot enforce both structural completeness and per-criterion integrity simultaneously. | behavior | aspirational | The rubric contains at least two gates at different granularities: (1) one phase-level gate that blocks entry to criterion-writing until a structural precondition is met (e.g., minimum failure modes enumerated, minimum categories identified), and (2) at least one per-criterion gate that blocks finalization of an individual criterion until its required sub-steps are complete. A rubric with only a phase gate or only per-criterion gates does not pass. Both gates must use explicit blocking language with checkable conditions. |
| C-17 | **Audit role or phase separation** — The rubric's workflow separates the criterion-authoring concern (achieving coverage: do the criteria address the right behaviors?) from the criterion-auditing concern (achieving specificity: are the pass conditions discriminating?). When both concerns are handled in a single step, competing cognitive demands reduce the quality of each. Separation makes both the drafts and the audits independently reviewable. | depth | aspirational | The rubric either (a) designates distinct roles for authoring and auditing criteria (e.g., Author and Challenger), each producing its own output artifacts, or (b) structures the workflow into a drafting phase that produces criterion drafts and a separate review phase that produces a structured audit of those drafts. A rubric where a single step simultaneously writes each criterion and evaluates its specificity does not satisfy this criterion. The drafts and the audit must be separately readable in the output. |
| C-18 | **Audit trail captures reasoning, not only verdicts** — The audit phase produces a structured artifact (table or equivalent) recording not just whether each pass condition passed the inertia test, but which specific skill-contract element made it discriminating. Future rubric maintainers can read why each condition survived, enabling targeted revision without re-running the full evaluation. | depth | aspirational | The rubric requires the audit artifact to include a field capturing the discriminating element for each condition that passes the inertia test — e.g., a column named "Skill-Specific Element" or "Discriminating Anchor" that names the count, field, pattern, or enumeration that ties the condition to the target skill's contract. A rubric that requires only pass/fail verdicts from the audit, with no reasoning field, does not satisfy this criterion. Pass if a rubric maintainer reading the audit table could identify what to preserve if the pass condition were rewritten. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

**Note**: aspirational denominator is now 10 (C-09 through C-18).

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
- [ ] C-14: Calibration pair is written immediately after pass-condition drafting, not retrospectively
- [ ] C-15: Each mandatory check step emits an independent output artifact before the criterion is sealed — skipping leaves a detectable gap
- [ ] C-16: Two gate levels present — one phase gate and at least one per-criterion gate
- [ ] C-17: Authoring phase and auditing phase are separated, producing independently readable outputs
- [ ] C-18: Audit artifact captures the discriminating element for each condition, not only pass/fail verdicts
