Two new excellence patterns surface from the scorecard:

**Pattern A — Accountability-addressed recommendation** (from C-01 analysis): V-04/V-05 PASS because they name a decision-maker with time constraint and accountability ("10 minutes and must decide"). V-01/V-02/V-03 PARTIAL because recommendation floats without reader orientation. The output property: recommendation is framed as a decision for a named role, not as a finding.

**Pattern B — Pattern block self-sufficiency** (from C-10 analysis): V-04 is called "strongest mechanism — both structural independence and sequencing enforced." C-10 already requires a discrete labeled claim; the new bar is that the block is self-contained — readable without the surrounding narrative. The output property: no forward/backward references inside the pattern block.

Here is the complete rubric v3:

---

# Quest Rubric — `topic-story` v3

## Essential Criteria

Output is not usable if any essential criterion fails.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Bottom Line Up Front** | correctness | essential | The recommendation or verdict appears in the opening paragraph or first named section — not buried at the end. A story that builds to a conclusion fails. A story where the first substantive sentence is hedging or context-setting fails. |
| C-02 | **Labeled sections present** | format | essential | The story contains the five named beats: *What we set out to understand / What the signals revealed / What the signals say together / What remains uncertain / The recommendation*. Any beat missing or renamed beyond recognition fails. |
| C-03 | **Cross-signal synthesis present** | correctness | essential | Beat 3 states a claim that references what two or more signals show *together* that no single signal shows alone. A sentence that could be derived from reading any single artifact fails. Restating artifact summaries side by side fails. |
| C-04 | **Pattern, not summary** | depth | essential | The synthesis claim names a relationship, tension, or gap across signals — not a collection of findings. A sentence equivalent to "Signal A said X and Signal B said Y" fails. The pattern must name a synthetic claim (e.g., "users want X but the technical cost is Y — the gap is the risk"). Restating individual findings side by side fails. |

---

## Recommended Criteria

Output is meaningfully better when these pass.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Signal coverage is grounded** | coverage | recommended | At least three distinct signal namespaces or artifact types are referenced to show what evidence base the story draws from. Not exhaustive enumeration — enough to make the synthesis credible. Fewer than three identifiable signal sources fails. |
| C-06 | **Uncertainty is specific** | depth | recommended | The "what remains uncertain" section names at least one specific open question that, if resolved, would change the recommendation. Generic hedges such as "more research may be needed" without naming what research or what it would change fail. |
| C-07 | **Recommendation proportionality** | correctness | recommended | The recommendation weight is consistent with the evidence described. Strong positive signals → proceed; mixed → pause; conflicting → pivot; weak or negative → abandon. A proceed recommendation following a story of conflicts and gaps fails; an abandon recommendation following a story of strong positive signals fails. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Narrative arc** | behavior | aspirational | The story has a discernible arc: intent (what we set out to learn), evidence building (signals adding up), resolution (recommendation). A reader unfamiliar with the topic can follow the reasoning from intent to recommendation without consulting the underlying signals. A flat list of findings with a tacked-on recommendation fails. |
| C-09 | **Delta surfacing** | depth | aspirational | At least one explicit "we expected X but found Y" or equivalent contrastive statement appears. The story calls out where the signals surprised or contradicted initial assumptions. Absence of any contrastive or discovery framing fails. Discovery language that requires inference from surrounding context — rather than a stated contrast — fails. |
| C-10 | **Pre-composition pattern artifact** | depth | aspirational | The cross-signal pattern is stated as a discrete, labeled claim that stands independently of the narrative prose — a named sentence or block (e.g., "The pattern: ...") that could be read without the surrounding story. The pattern must not exist only as an inference embedded in flowing text. This signals the pattern was identified analytically before writing, not arrived at during composition. Absence of a discrete pattern statement fails. |
| C-11 | **Pattern-to-recommendation traceability** | correctness | aspirational | The recommendation is visibly derived from the named cross-signal pattern. The story contains an explicit logical bridge: the pattern is cited as the stated reason for the recommendation verb chosen. A reader can identify the sentence or passage where the pattern produces the recommendation. Recommendation and pattern that are both present but not explicitly connected fail. |
| C-12 | **Decision-cost annotated uncertainty** | depth | aspirational | Each uncertainty item explicitly states what resolving it would change about the recommendation: whether the verb would shift and in which direction (e.g., "if X resolves to Y, this moves from pause to proceed"). General "this matters for the decision" framing without a stated direction fails. Uncertainty items with no decision-cost annotation fail. |
| C-13 | **Accountability-addressed recommendation** | correctness | aspirational | The recommendation beat names or clearly addresses the decision context — who is making the decision and under what constraint. A recommendation stated as a finding ("the signals suggest X") rather than a decision ("a team lead deciding Y should Z") fails. A recommendation with no named or implied decision-maker role fails. |
| C-14 | **Pattern block self-sufficiency** | depth | aspirational | The pre-composition pattern block (C-10) is self-contained: it conveys the full cross-signal claim without requiring the surrounding narrative to be read. Forward references ("as shown below"), backward references ("the above signals"), or incomplete claims that resolve only in the prose around the block all fail. |

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
| Any essential fails | Not useful — do not use output |
| All essential pass, composite < 80 | Partial — useful with caveats |
| All essential pass, composite >= 80 | Golden — meets standard |
| All criteria pass, composite = 100 | Exemplary |

---

## Criterion Weights Summary

| ID | Category | Weight |
|----|----------|--------|
| C-01 | correctness | essential |
| C-02 | format | essential |
| C-03 | correctness | essential |
| C-04 | depth | essential |
| C-05 | coverage | recommended |
| C-06 | depth | recommended |
| C-07 | correctness | recommended |
| C-08 | behavior | aspirational |
| C-09 | depth | aspirational |
| C-10 | depth | aspirational |
| C-11 | correctness | aspirational |
| C-12 | depth | aspirational |
| C-13 | correctness | aspirational |
| C-14 | depth | aspirational |

---

**v3 change notes**: Added C-13 and C-14. N_aspirational increases from 5 to 7. C-13 sourced from V-04/V-05 PASS / V-01–V-03 PARTIAL split on C-01: the differentiating mechanism is audience-accountability framing that positions the recommendation as a decision rather than a finding. C-14 sourced from V-04 "strongest mechanism" note on C-10: structural independence (labeled block) and sequencing enforcement are necessary but not sufficient — the block must also be self-contained, requiring no reference to the surrounding prose to convey the full claim. Re-score Round 2 against v3 before promoting any variation to golden.
