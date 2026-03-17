Done. Here is the complete updated rubric:

---

# quest-variate Rubric — v2

**Skill:** `quest-variate`
**Version:** v2 (updated from R1 scorecard — 2026-03-14)
**Scoring model:** Essential (60) + Recommended (30) + Aspirational (10)

---

## Design Decisions

- **4 essential criteria** (not 5) — the skill has one core invariant per property: completeness, labeling, single-axis isolation, and count. A 5th would overlap.
- **C-01 (complete runnable bodies)** is the hardest fail mode in practice — models routinely emit diffs or partial bodies when asked to "vary" something.
- **C-03 (single-axis isolation)** enforces the scientific discipline the skill description calls out explicitly: single-axis passes before combinations.
- **C-07 (axis coverage breadth)** is recommended, not essential — with N=5 you can't hit all 6 axes, so 4-of-6 is a reasonable floor.
- **C-08/C-09** are aspirational because they only apply in specific N > 6 or baseline-anchored scenarios — penalizing their absence in a default N=5 run would be unfair.
- **C-10/C-11/C-12** are new aspirational criteria added from R1 excellence signals — V-04's phase-gate design surfaced two structural patterns that distinguish good variations from excellent ones.
- **Failure modes section** names the 5 most likely failure patterns by criterion, which makes scoring faster and more consistent across runs.

---

## Criteria

### Essential (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Complete runnable bodies** | completeness | essential | Each variation is a complete, standalone skill body. No diffs, no "same as above", no references to other variations. The body can be dropped into a skill file and run without modification. |
| C-02 | **Inline axis and hypothesis labels** | labeling | essential | Each variation includes an inline `**Axis:**` field, `**Hypothesis:**` field, and variation ID (`## V-01`). All three fields are present and non-empty. |
| C-03 | **Single-axis isolation** | correctness | essential | Each variation changes exactly one axis relative to a baseline. Variations that co-vary two or more axes without being labeled as combination passes fail. |
| C-04 | **N variations produced** | coverage | essential | Output contains exactly N complete variations. Default N=5 when not specified. |

### Recommended (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Testable hypotheses** | depth | recommended | Each hypothesis is falsifiable — predicts a specific, observable difference in model behavior or output quality. Generic descriptions do not pass. |
| C-06 | **Non-trivial variation** | depth | recommended | Each variation demonstrates a genuinely different design choice a practitioner would consciously select. Surface phrasing changes do not qualify. |
| C-07 | **Axis coverage breadth** | coverage | recommended | At least 4 of the 6 defined axes are represented across all N variations. |

### Aspirational (10 points total)

| ID | Criterion | Category | Source | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Combination pass labeled and deferred** | behavior | v1 | If N > 6, combination passes appear after all single-axis variations and name both axes. |
| C-09 | **Baseline variation included** | behavior | v1 | One variation (typically V-01) serves as the canonical baseline so subsequent variations are anchored to a known point. |
| C-10 | **Stop conditions encode constraint structurally** | behavior | R1/V-04 | The skill body uses explicit stop conditions or phase gates to enforce single-axis isolation mechanically — not as advisory instructions. A halt-and-rewrite trigger is present: the structure itself prevents axis drift rather than warning against it. |
| C-11 | **Hypothesis committed before generation begins** | behavior | R1/V-04 | The skill body requires axis and hypothesis to be declared in a phase prior to generating the variation body. Generation does not begin until the hypothesis is locked. Prevents lazy axis selection driven by what is easy to generate. |
| C-12 | **Explicit rewrite trigger** | behavior | R1/V-04 | The skill body specifies a named rewrite trigger condition (e.g., "if multi-axis drift detected, discard variation and regenerate") rather than a warning or advisory note. The trigger is checkable before the next phase begins. |

---

## Scoring

```
Composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)
```

| Threshold | Meaning |
|-----------|---------|
| All essential pass + composite >= 80 | Golden -- meets quality bar |
| All essential pass + composite < 80 | Acceptable -- essential correct, recommended gaps |
| Any essential fail | Reject -- output is not usable |

---

## Failure Modes

1. **Diff leak** — body contains "same as above" or diff notation instead of full content (fails C-01)
2. **Missing hypothesis** — label and axis present but hypothesis is a restatement of the axis name (fails C-02)
3. **Axis drift** — variation modifies two dimensions simultaneously, unlabeled as combination (fails C-03)
4. **Count mismatch** — output delivers 4 or 6 variations when 5 were requested (fails C-04)
5. **Trivial delta** — variation changes surface phrasing only, not the design choice the axis represents (fails C-06)

---

**Key changes from v1:**

- Added C-10, C-11, C-12 as new aspirational criteria from R1 excellence signals
- Scoring denominator for aspirational updated from `/2` to `/5` (now 5 aspirational criteria)
- Added `Source` column to aspirational table to track origin (v1 vs R1/V-04)
- Design decisions updated to document the R1-sourced additions
eets quality bar |
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
