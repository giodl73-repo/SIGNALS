---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 3
prior_version: quest-rubric-variate-R2-2026-03-15.md
---

# Rubric: quest-variate (v3)

Evaluates output from the `quest-variate` skill, which generates N distinct prompt variations
of a skill body. Each variation must be complete and runnable, vary along exactly one axis,
and carry a labeled hypothesis.

**v3 changes**: Added C-14 through C-18 from Round 2 excellence signals. No essential or
recommended criteria changed. Aspirational denominator updated from /5 to /10.

---

## Criteria

### Essential (must all pass — without these the output is not useful)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Runnable completeness** | correctness | essential | Every variation is a full, standalone skill body. Each V-NN block can be copied into a skill file and executed without referencing any other variation. No "same as V-01 except…" constructs. All declared steps and sections are written out in full — not placeholders, not ellipses. |
| C-02 | **Count and labeling** | format | essential | Output contains exactly the requested N variations (default 5 when N is unspecified), labeled V-01 through V-0N in sequence with no gaps. Fewer than N is a fail; extra unlabeled content does not substitute for missing labeled variations. |
| C-03 | **Axis declaration** | format | essential | Every V-NN header or preamble includes an `axis:` field naming one of the defined axes, and a `hypothesis:` field stating the expected behavioral effect. Both fields must be present and non-empty. |
| C-04 | **Single-axis isolation** | correctness | essential | Each variation changes exactly one axis relative to a shared baseline. Reading two variations side-by-side, the structural difference maps to exactly one named axis. Changes that bleed across axes are a fail. Exception: variations explicitly labeled as combination passes. |
| C-05 | **Genuine distinctness** | correctness | essential | No two variations are superficially equivalent (e.g., minor synonym substitution that does not actually change the axis). Each variation must be distinguishable by its axis choice in a way that would produce observably different model behavior. |

---

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Axis spread across the full axis vocabulary** | coverage | recommended | The N variations cover at least 3 distinct axes from the axis vocabulary (role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity). Not all variations on the same axis. |
| C-07 | **Hypotheses are falsifiable** | depth | recommended | Every hypothesis is specific enough to be testable: it predicts a directional outcome (e.g., "V-03 will produce more granular scoring because…"), not a vague preference ("this might be better"). |
| C-08 | **Baseline is explicit or inferable** | format | recommended | The output either states the baseline skill body once up front, or makes the stable baseline clearly inferable from the variation set so a reviewer can reason about what changed. |

---

### Aspirational (raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Combination roadmap appended** | depth | aspirational | After the single-axis variations, the output includes a brief combination matrix or table identifying the most promising axis pairings for a follow-up pass, with rationale. |
| C-10 | **Hypothesis tension surfaced** | depth | aspirational | At least one variation explicitly notes a trade-off or tension between axes (e.g., "increasing scoring granularity in V-04 conflicts with the concise output format in V-02"), demonstrating awareness of interaction effects. |
| C-11 | **Explicit failure condition on every hypothesis** | depth | aspirational | Every hypothesis includes a stated failure condition: a specific, observable outcome that would refute the mechanism if it occurred (e.g., "if V-03 does not improve X, the mechanism is refuted"). Enables a negative experimental result to be recovered cleanly rather than explained away. |
| C-12 | **Evaluation order guidance** | depth | aspirational | After the variation bodies, the output includes a ranking or table ordering the variations by evaluation priority — incorporating cost, independence from other variations, and dependency relationships — to support a multi-run experimental plan. |
| C-13 | **Hypothesis tension note pre-combination** | depth | aspirational | At least one axis-pair conflict is explicitly named *before* the combination roadmap, with a prediction of which variable will dominate the outcome if the combination is run. Prevents a confounded round-2 result by forcing a phase-priority choice before the combination is designed. |
| C-14 | **Criterion-targeted axis selection** | depth | aspirational | At least one variation names the specific rubric criterion its declared axis is designed to improve. The mechanism connecting the axis to the criterion must be explicit (e.g., "annotated-rationale constraints cause mechanism-citing hypotheses, improving C-07 pass rates"). Naming an outcome-level effect without connecting it to a criterion ID does not pass. |
| C-15 | **Inline generation loop gate** | correctness | aspirational | At least one variation embeds a self-check gate *inside* the variation-generation loop — fired after each variation body, before advancing to the next — with an explicit "fix before advancing" or equivalent instruction. A gate that appears only as a post-generation review step does not pass. The gate must name which criteria it is checking. |
| C-16 | **Per-axis pole declaration before generation** | format | aspirational | Before any variation body is generated, the output includes a structured declaration of the current (baseline) pole for every axis in the axis vocabulary. A champion table or equivalent qualifies; a single "the baseline skill body is [X]" reference does not — each axis must have its current pole named individually. Directly enables C-04 isolation checks by making the stable element visible per axis. |
| C-17 | **Pre-generation axis lock** | correctness | aspirational | Combination passes (or any variation where axis isolation is a risk) include an explicit instruction declaring axis assignments immutable once the generation phase begins ("do not revise axis assignments after Phase N begins" or equivalent). Converts C-04 single-axis isolation from an intention to an enforced protocol constraint. Only evaluated for combination passes; single-axis-only outputs pass by default. |
| C-18 | **Single-axis comparison denominator in combination failure conditions** | depth | aspirational | Combination pass failure conditions name the most relevant single-axis variation as the comparison baseline rather than the bare unvaried skill (e.g., "if the combination does not exceed V-01 alone…" rather than "if the outcome does not improve…"). The named variation must be the one that most directly tests the dominant axis of the combination. Only evaluated for combination passes; single-axis-only outputs pass by default. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Ship-ready variation set |
| Silver | >= 65, all essential pass | Usable with minor gaps |
| Bronze | >= 50, >= 4 essential pass | Needs revision before use |
| Fail | any essential fails | Not usable |

---

## Quick Checklist (for manual scoring)

- [ ] C-01: Every variation is a complete, standalone, runnable skill body
- [ ] C-02: Exactly N variations, labeled V-01 through V-0N with no gaps
- [ ] C-03: Each variation has `axis:` and `hypothesis:` fields, both non-empty
- [ ] C-04: Each variation changes exactly one axis (combination passes labeled explicitly)
- [ ] C-05: No two variations are superficially equivalent
- [ ] C-06: At least 3 distinct axes from the axis vocabulary represented
- [ ] C-07: Every hypothesis predicts a directional, testable outcome
- [ ] C-08: Baseline stated explicitly or clearly inferable from the variation set
- [ ] C-09: Combination roadmap present with axis-pair rationale
- [ ] C-10: At least one hypothesis surfaces an axis tension or trade-off
- [ ] C-11: Every hypothesis includes an explicit failure condition
- [ ] C-12: Evaluation order table or ranking provided
- [ ] C-13: Axis-pair tension named before combination roadmap, with dominance prediction
- [ ] C-14: At least one variation names the rubric criterion ID its axis targets
- [ ] C-15: At least one variation has a self-check gate inside the generation loop
- [ ] C-16: Per-axis baseline pole declared before any variation body is generated
- [ ] C-17: Combination passes include an explicit pre-generation axis lock instruction
- [ ] C-18: Combination failure conditions name a single-axis variation as comparison denominator

---

## Evaluator Notes

- C-01 is the hardest essential to fake: spot-check by asking "could I paste V-02 directly into a skill file and run it?" If no, C-01 fails.
- C-04 failures are common when a skill body is complex — authors tend to fix two things at once. One axis change per variation is a strict constraint.
- **C-14 vs C-07**: C-07 requires a falsifiable hypothesis. C-14 requires that the axis was *chosen* to target a specific rubric criterion, with the mechanism stated. A variation can pass C-07 and fail C-14 if the axis-to-criterion connection is never made explicit.
- **C-15 vs C-08**: C-08 checks whether a baseline is present. C-15 checks whether a correctness gate fires inside the loop. They are independent — a variation can pass C-08 and fail C-15.
- **C-16 vs C-08**: C-08 passes if the baseline is "inferable." C-16 requires a structured per-axis declaration of current poles before generation begins. A set can pass C-08 and fail C-16.
- **C-17 and C-18**: Only evaluated for outputs that include at least one combination pass. If all variations are single-axis, both criteria are vacuously true and score as full passes.

---

## Criterion Genealogy

| Criterion | Source | Round introduced |
|-----------|--------|-----------------|
| C-01 | Design | v1 |
| C-02 | Design | v1 |
| C-03 | Design | v1 |
| C-04 | Design (single-axis isolation — theoretical core) | v1 |
| C-05 | Design (genuine distinctness — prevents synonym-swap degenerate output) | v1 |
| C-06 | Design | v1 |
| C-07 | Design (falsifiability distinguishes testable from trivial hypotheses) | v1 |
| C-08 | Design | v1 |
| C-09 | Design | v1 |
| C-10 | Design | v1 |
| C-11 | R1 excellence: explicit failure condition enables clean negative results | v2 |
| C-12 | R1 excellence: evaluation order guidance supports multi-run experimental plans | v2 |
| C-13 | R1 excellence: pre-combination tension note with dominance prediction prevents confounded R2 | v2 |
| C-14 | R2 excellence: V-01 axis chosen to target C-07 pass rates — "annotated-rationale constraints cause mechanism-citing hypotheses" — first criterion-targeted axis in the set | v3 |
| C-15 | R2 excellence: V-02 self-score gate fires after each body while context is active — "strongest C-01 targeting mechanism in the set" — gate-inside-loop pattern | v3 |
| C-16 | R2 excellence: V-03 champion table declared per-axis before generation — "converts baseline from inferable to explicitly declared per axis" — strongest C-08 in the set | v3 |
| C-17 | R2 excellence: V-04 PLAN-phase immutability — "most operationally specific axis-isolation mechanism in the set" — axis lock enforced as protocol constraint | v3 |
| C-18 | R2 excellence: V-04 and V-05 combination failure conditions named single-axis comparison denominator (V-01, V-03) rather than bare baseline — compound comparison rigor | v3 |
