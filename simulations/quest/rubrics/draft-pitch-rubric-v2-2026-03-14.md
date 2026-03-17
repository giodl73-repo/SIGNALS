Here is the complete updated rubric:

---

# Rubric: draft-pitch — v2

**Change from v1**: Added C-10, C-11, C-12 from R1 excellence signals. Aspirational denominator updated from 2 to 5.

---

## Essential Criteria (60% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | All three versions present | coverage | Three labeled sections: exec, dev, maker. All non-empty. |
| C-02 | Each version has all four elements | coverage | Hook, What, Why, CTA present in all three versions (12 elements total). |
| C-03 | Exec version is outcome-first with ROI framing | correctness | Business outcome (cost, risk, productivity) before any feature or technology mention. |
| C-04 | Anti-positioning section present | coverage | Explicit "what we are NOT" section ruling out at least one adjacent category. Absence = hard fail. |

---

## Recommended Criteria (30% weight)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | Dev version shows the tool, not the business case | depth | Concrete interaction -- command, artifact, or workflow step. Reader can answer "what would I actually type?" |
| C-06 | Maker version is jargon-free | depth | No unexplained acronyms, namespace names, or internal terminology. |
| C-07 | Prior signals consulted | behavior | Pitch reflects framing from available scout/positioning signals. Waived if none exist. |

---

## Aspirational Criteria (10% weight)

**Existing:**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | Proof points are specific and traceable | depth | At least two proof points cite a named source or artifact path. Vague claims fail. |
| C-09 | Competitive framing names inertia as primary competitor | depth | "Doing nothing" / "the meeting that never happened" is named as the real competition. |

**New — from R1 excellence signals:**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-10 | Exec self-check is embedded at generation time | process | Skill instructs the model to write the exec opening, test it against C-03, and rewrite *before* continuing. A post-draft checklist does not pass. |
| C-11 | Positioning answers are locked in writing before prose begins | process | Strategy questions (competitor, ruling-out statement, signal framing) produce explicit written outputs before any version is drafted. An ambient preamble does not pass. |
| C-12 | Default fallback values provided for missing signals | resilience | Skill supplies explicit defaults per signal-dependent field so C-09 passes unconditionally even with no prior scout artifacts. |

---

## Composite Score Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

Golden threshold: all 4 essential pass AND composite >= 80.

---

**Key design note on C-10/C-11/C-12**: These are *process/resilience* criteria — they score the skill design, not the output content. V-05 reached 100 by using all three structural patterns. A skill that produces correct output by luck (ambient context, strong model inference) does not pass these. The distinction: enforcement vs. suggestion.
oment the exec opening is written -- not as a post-draft review step. Evidence: the skill instructs the model to write the first sentence, test it, and rewrite before continuing. A post-draft checklist does not pass. |
| C-11 | **Positioning answers are locked in writing before prose begins** | process | Strategy questions (primary competitor, ruling-out statement, signal framing) are answered as explicit written outputs before any pitch version is drafted. Locked answers are citable inputs to the PM pass. An ambient preamble or inline instruction does not pass. |
| C-12 | **Default fallback values provided for missing signals** | resilience | The skill supplies an explicit default for each signal-dependent field (e.g., Primary Competitor = "teams doing nothing / the review that never happened"). A run with no prior scout artifacts still produces a correct C-09 answer unconditionally. |

---

## Composite Score Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | All essential + >= 80 | Ship it |
| Pass | All essential + 70-79 | Usable, recommended gaps noted |
| Conditional | All essential + < 70 | Needs recommended work before use |
| Fail | Any essential fails | Do not use -- structural gap |

---

## Scoring Notes

- C-01 and C-02 are evaluated structurally -- check for presence, not quality
- C-03 is evaluated by reading the first 3 sentences of the exec version; if they describe features, it fails
- C-04 fails if the section is absent; a weak anti-positioning still passes (quality handled by C-08/C-09)
- C-07 is waived if the run has no prior signals or no scout-positioning artifact exists
- C-09 is the highest-value aspirational criterion; it signals the skill has internalized the positioning insight, not just applied a template
- C-10, C-11, C-12 are process/resilience criteria -- they score the skill design, not the output content. A skill that produces correct output by luck (not by structure) does not pass these
- C-10 and C-11 together reflect the V-05 finding: structural enforcement at generation time outperforms post-draft review
- C-12 reflects the cold-start safety finding: explicit defaults eliminate conditional passes on C-09

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric -- 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10 (embedded self-check), C-11 (positioning lockdown), C-12 (default fallbacks) from R1 excellence signals. Aspirational denominator updated from 2 to 5. |
