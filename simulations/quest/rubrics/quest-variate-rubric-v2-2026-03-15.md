v2 written. Here's the complete updated rubric:

---

```markdown
---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 2
---

# Rubric: quest-variate
```

**Structure summary — v2:**

- **5 essential** (C-01–C-05): unchanged from v1
- **3 recommended** (C-06–C-08): unchanged from v1
- **5 aspirational** (C-09–C-13): C-09 and C-10 carried over; three new:

| ID | New Criterion | Source Signal |
|----|---------------|---------------|
| C-11 | **Explicit failure condition on every hypothesis** | E-1: "if X does not improve, the mechanism is refuted" — enables clean negative results, not just confirmation |
| C-12 | **Evaluation order guidance** | E-2: post-variation ranking table by cost, independence, and dependency — supports a multi-run experimental plan |
| C-13 | **Hypothesis tension note pre-combination** | E-3: names axis-pair conflict *and predicts the dominant variable* before the combination roadmap — prevents confounded R2 results |

**Scoring formula updated:** aspirational denominator changes from `/2` to `/5` (total weight stays at 10 points). A perfect R1 output now scores 100 under v2 (5/5 aspirational), same as under v1.

**Key distinction — C-13 vs C-10:** C-10 requires noting a tension anywhere in the set. C-13 requires naming a specific pairing, predicting which axis dominates, and placing that prediction *before* the combination roadmap. A set can pass C-10 and fail C-13.
than N is a fail; extra unlabeled content does not substitute for missing labeled variations. |
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
| C-11 | **Explicit failure condition on every hypothesis** | depth | aspirational | Every hypothesis includes a stated failure condition: a specific, observable outcome that would refute the mechanism if it occurred (e.g., "if V-03 does not improve X, the mechanism is refuted"). Enables a negative experimental result to be recovered cleanly rather than explained away. |
| C-12 | **Evaluation order guidance** | depth | aspirational | After the variation bodies, the output includes a ranking or table ordering the variations by evaluation priority — incorporating cost, independence from other variations, and dependency relationships — to support a multi-run experimental plan. |
| C-13 | **Hypothesis tension note pre-combination** | depth | aspirational | At least one axis-pair conflict is explicitly named *before* the combination roadmap, with a prediction of which variable will dominate the outcome if the combination is run. Prevents a confounded round-2 result by forcing a phase-priority choice before the combination is designed. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
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
- C-11 distinguishes a hypothesis set that can return a clean negative result from one that can only confirm. A variation with no failure condition can always be explained away post-hoc.
- C-13 is stricter than C-10: C-10 requires noting a tension somewhere in the set; C-13 requires predicting which variable dominates and placing that prediction *before* the combination roadmap.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-15 | Added C-11, C-12, C-13 from R1 excellence signals; updated aspirational denominator from 2 to 5 |
