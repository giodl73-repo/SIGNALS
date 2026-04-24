---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 1
---

# Rubric: quest-variate

Evaluates output from the `quest-variate` skill, which generates N distinct prompt variations of a skill body. Each variation must be a complete, runnable skill body — not a diff — with a labeled axis and hypothesis.

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Complete skill bodies** | correctness | essential | Every variation is a fully self-contained, runnable skill body. No variation is expressed as a diff, patch, delta, or "same as above except…" fragment. |
| C-02 | **Label + axis + hypothesis on every variation** | format | essential | Each variation carries a V-NN label, names its variation axis (one of: role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity), and states a testable hypothesis about the effect of that axis choice. |
| C-03 | **Single-axis isolation** | correctness | essential | Each variation changes exactly one axis relative to a stable baseline. No variation introduces two or more simultaneous axis changes (combinations are only allowed after single-axis passes are complete). |
| C-04 | **N variations produced** | coverage | essential | The output contains exactly N variations (default N=5, or the N specified in the prompt). Fewer than N is a fail; extra unlabeled content does not substitute for missing labeled variations. |
| C-05 | **Genuine distinctness** | correctness | essential | No two variations are superficially equivalent (e.g., minor synonym substitution that does not actually change the axis). Each variation must be distinguishable by its axis choice in a way that would produce observably different model behavior. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Axis spread across the full axis vocabulary** | coverage | recommended | The N variations cover at least 3 distinct axes from the axis vocabulary (role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity). Not all variations on the same axis. |
| C-07 | **Hypotheses are falsifiable** | depth | recommended | Every hypothesis is specific enough to be testable: it predicts a directional outcome (e.g., "V-03 will produce more granular scoring because…"), not a vague preference ("this might be better"). |
| C-08 | **Baseline is explicit or inferable** | format | recommended | The output either states the baseline skill body once up front, or makes the stable baseline clearly inferable from the variation set so a reviewer can reason about what changed. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Combination roadmap appended** | depth | aspirational | After the single-axis variations, the output includes a brief combination matrix or table identifying the most promising axis pairings for a follow-up pass, with rationale. |
| C-10 | **Hypothesis tension surfaced** | depth | aspirational | At least one variation explicitly notes a trade-off or tension between axes (e.g., "increasing scoring granularity in V-04 conflicts with the concise output format in V-02"), demonstrating awareness of interaction effects. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Ship-ready variation set |
| Silver | >= 65, all essential pass | Usable with minor gaps |
| Bronze | >= 50, >= 4 essential pass | Needs revision before use |
| Fail | any essential fails | Not usable |

---

## Evaluator Notes

- C-01 is the hardest essential to fake: spot-check by asking "could I paste V-02 directly into a skill file and run it?" If the answer is no, C-01 fails.
- C-03 failures are common when a skill body is complex — authors tend to "fix" two things at once. One axis change per variation is a strict constraint.
- C-07 distinguishes a variation set that can drive a real experiment from one that is decorative.
