---
skill: quest-rubric
skill_target: topic-story
date: 2026-03-15
version: 1
---

# Scoring Rubric: topic-story

Evaluates the editorial narrative that synthesizes all signals into a coherent story for a topic.
The output must be an authored interpretation, not a signal enumeration.

---

## Essential Criteria

All essential criteria must pass. Failure on any one makes the output not useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Synthesis, not summary** | correctness | essential | No dominant pattern of "Signal X found Y" enumeration. Signals are referenced only to support interpretive claims. The text makes claims that draw on multiple signals simultaneously. A reader cannot tell the output was assembled by reading signals in order. |
| C-02 | **All five structural elements present** | format | essential | The following are each identifiable as distinct sections or clearly addressed paragraphs: (1) what we set out to understand, (2) what each signal revealed (key finding), (3) what the signals say together (the pattern), (4) what remains uncertain, (5) the recommendation. Absence of any one fails. |
| C-03 | **Explicit, grounded recommendation** | correctness | essential | One of the four verbs -- proceed / pause / pivot / abandon -- appears as the recommendation with a rationale tied to specific signals or the pattern identified. A vague "it depends" or missing recommendation fails. |
| C-04 | **Cross-signal pattern identified** | depth | essential | The "signals say together" section makes a claim that could not be derived from any single signal alone. The pattern must be named or stated as a synthetic claim (e.g., "users want X but the technical cost is Y -- the gap is the risk"). Restating individual findings side by side fails. |

---

## Recommended Criteria

Output is meaningfully better when these pass.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Signal coverage is grounded** | coverage | recommended | At least three distinct signal namespaces or artifact types are referenced to show what evidence base the story draws from. Not exhaustive enumeration -- enough to make the synthesis credible. Fewer than three identifiable signal sources fails. |
| C-06 | **Uncertainty is specific** | depth | recommended | The "what remains uncertain" section names at least one specific open question that, if resolved, would change the recommendation. Generic hedges such as "more research may be needed" without naming what research or what it would change fail. |
| C-07 | **Recommendation proportionality** | correctness | recommended | The recommendation weight is consistent with the evidence described. Strong positive signals -> proceed; mixed -> pause; conflicting -> pivot; weak or negative -> abandon. A proceed recommendation following a story of conflicts and gaps fails; an abandon recommendation following a story of strong positive signals fails. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Narrative arc** | behavior | aspirational | The story has a discernible arc: intent (what we set out to learn), evidence building (signals adding up), resolution (recommendation). A reader unfamiliar with the topic can follow the reasoning from intent to recommendation without consulting the underlying signals. A flat list of findings with a tacked-on recommendation fails. |
| C-09 | **Delta surfacing** | depth | aspirational | At least one explicit "we expected X but found Y" or equivalent contrastive statement appears. The story calls out where the signals surprised or contradicted initial assumptions. Absence of any contrastive or discovery framing fails. |

---

## Scoring Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

### Score Bands

| Score | Interpretation |
|-------|----------------|
| Any essential fails | Not useful -- do not use output |
| All essential pass, composite < 80 | Partial -- useful with caveats |
| All essential pass, composite >= 80 | Golden -- meets standard |
| All criteria pass, composite = 100 | Exemplary |

---

## Criterion Weights Summary

| ID | Weight | Category |
|----|--------|----------|
| C-01 | essential | correctness |
| C-02 | essential | format |
| C-03 | essential | correctness |
| C-04 | essential | depth |
| C-05 | recommended | coverage |
| C-06 | recommended | depth |
| C-07 | recommended | correctness |
| C-08 | aspirational | behavior |
| C-09 | aspirational | depth |

---

## Scoring Notes

- **C-01 vs C-05**: C-01 is about *how* signals are used (synthesis vs enumeration). C-05 is about *how many* are referenced. A story can reference many signals enumeratively (fails C-01) or synthesize few deeply (passes C-01, may fail C-05).
- **C-03 and C-07 interact**: C-03 requires the recommendation exists; C-07 requires it is proportional. Score each independently.
- **C-04 is the hardest essential**: Evaluators should ask "could this pattern claim appear in any single signal?" If yes, it is not a cross-signal synthesis and fails.
