Rubric written to `simulations/quest/rubrics/quest-variate-rubric-2026-03-14.md`.

**Design decisions:**

- **4 essential criteria** (not 5) — the skill has one core invariant per property: completeness, labeling, single-axis isolation, and count. A 5th would overlap.
- **C-01 (complete runnable bodies)** is the hardest fail mode in practice — models routinely emit diffs or partial bodies when asked to "vary" something.
- **C-03 (single-axis isolation)** enforces the scientific discipline the skill description calls out explicitly: single-axis passes before combinations.
- **C-07 (axis coverage breadth)** is recommended, not essential — with N=5 you can't hit all 6 axes, so 4-of-6 is a reasonable floor.
- **C-08/C-09** are aspirational because they only apply in specific N > 6 or baseline-anchored scenarios — penalizing their absence in a default N=5 run would be unfair.
- **Failure modes section** names the 5 most likely failure patterns by criterion, which makes scoring faster and more consistent across runs.
choice. All three fields are present and non-empty. |
| C-03 | **Single-axis isolation** | correctness | essential | Each variation changes exactly one axis relative to a baseline. A reviewer can identify the single dimension that differs. Variations that co-vary two or more axes without being labeled as combination passes fail this criterion. |
| C-04 | **N variations produced** | coverage | essential | Output contains exactly N complete variations. Default N=5 when not specified. If N is specified by the caller, the output matches that count. |

### Recommended (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Testable hypotheses** | depth | recommended | Each hypothesis is falsifiable -- it predicts a specific, observable difference in model behavior or output quality (e.g., "shorter role sequence reduces token overhead without losing precision"). Generic descriptions ("this uses a different format") do not pass. |
| C-06 | **Non-trivial variation** | depth | recommended | Variations are meaningfully distinct. Changing a single word or toggling one boolean does not constitute an axis variation. Each variation demonstrates a genuinely different design choice that a practitioner would consciously select. |
| C-07 | **Axis coverage breadth** | coverage | recommended | Across all N variations, at least 4 of the 6 defined axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity) are represented at least once. |

### Aspirational (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Combination pass labeled and deferred** | behavior | aspirational | If N > 6, at least one variation is explicitly labeled as a combination pass (multi-axis) and appears after all single-axis variations. The label names both axes being combined. Single-axis passes are not intermixed with combination passes. |
| C-09 | **Baseline variation included** | behavior | aspirational | One variation (typically V-01) serves as the canonical baseline -- it matches the current skill body or a well-understood reference implementation -- so subsequent variations are anchored to a known point rather than to each other. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
```

| Threshold | Meaning |
|-----------|---------|
| All essential pass + composite >= 80 | Golden -- meets quality bar |
| All essential pass + composite < 80 | Acceptable -- essential correct, recommended gaps |
| Any essential fail | Reject -- output is not usable |

---

## Failure Modes

These are the most common ways `quest-variate` outputs fail:

1. **Diff leak** -- variation body contains "same as above" or diff notation instead of full content (fails C-01)
2. **Missing hypothesis** -- label and axis present but hypothesis omitted or is a restatement of the axis name (fails C-02)
3. **Axis drift** -- variation modifies two dimensions simultaneously and is not labeled as a combination (fails C-03)
4. **Count mismatch** -- output delivers 4 or 6 variations when 5 were requested (fails C-04)
5. **Trivial delta** -- variation changes surface phrasing only, not the design choice the axis represents (fails C-06)
