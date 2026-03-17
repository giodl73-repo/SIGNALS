**Rubric v2 written.** Three new aspirational criteria added:

---

**C-10 — Pre-composition pattern artifact** (`depth`, aspirational)
Sourced from: V-01/V-04 both PASS C-04 via a *written deliverable* step; V-02 only gets PARTIAL because "find the pattern" is a mental step.
Pass condition: the cross-signal pattern is stated as a discrete, labeled claim (e.g., "The pattern: ...") that stands independently of the narrative prose — not only as an embedded inference within flowing text.

**C-11 — Pattern-to-recommendation traceability** (`correctness`, aspirational)
Sourced from: V-03's consistency check ("if the pattern does not justify the Bottom Line, revise one of them") — no other variation has this backward pressure.
Pass condition: an explicit logical bridge exists — the pattern is cited as the stated reason for the recommendation verb. C-03 + C-04 both present is not sufficient; the connection must be named.

**C-12 — Decision-cost annotated uncertainty** (`depth`, aspirational)
Sourced from: V-03's C-06 instruction — "what does it cost the recommendation? If an answer would change the Bottom Line, say so explicitly" — beyond just "name what is unknown."
Pass condition: each uncertainty item states which direction the recommendation verb would shift if resolved. "This matters for the decision" without a stated direction fails.

---

**Scoring impact** — N_aspirational goes from 2 to 5. The aspirational pool (10 pts) is now harder to fully capture: V-01/V-04 at composite 90 would score differently against v2 (C-10 likely PASS, C-11 PARTIAL, C-12 FAIL = 3/5 aspirational = 6 pts vs prior 5 pts on 2/2). Recommend re-scoring Round 1 against v2 in the next scorecard.
hetic claim (e.g., "users want X but the technical cost is Y -- the gap is the risk"). Restating individual findings side by side fails. |

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
| C-10 | **Pre-composition pattern artifact** | depth | aspirational | The cross-signal pattern is stated as a discrete, labeled claim that stands independently of the narrative prose -- a named sentence or block (e.g., "The pattern: ...") that could be read without the surrounding story. The pattern must not exist only as an inference embedded in flowing text. This signals the pattern was identified analytically before writing, not arrived at during composition. Absence of a discrete pattern statement fails. |
| C-11 | **Pattern-to-recommendation traceability** | correctness | aspirational | The recommendation is visibly derived from the named cross-signal pattern. The story contains an explicit logical bridge: the pattern is cited as the stated reason for the recommendation verb chosen. A reader can identify the sentence or passage where the pattern produces the recommendation. Recommendation and pattern that are both present but not explicitly connected fail. |
| C-12 | **Decision-cost annotated uncertainty** | depth | aspirational | Each uncertainty item explicitly states what resolving it would change about the recommendation: whether the verb would shift and in which direction (e.g., "if X resolves to Y, this moves from pause to proceed"). General "this matters for the decision" framing without a stated direction fails. Uncertainty items with no decision-cost annotation fail. |

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
| C-10 | aspirational | depth |
| C-11 | aspirational | correctness |
| C-12 | aspirational | depth |

---

## Scoring Notes

- **C-01 vs C-05**: C-01 is about *how* signals are used (synthesis vs enumeration). C-05 is about *how many* are referenced. A story can reference many signals enumeratively (fails C-01) or synthesize few deeply (passes C-01, may fail C-05).
- **C-03 and C-07 interact**: C-03 requires the recommendation exists; C-07 requires it is proportional. Score each independently.
- **C-04 is the hardest essential**: Evaluators should ask "could this pattern claim appear in any single signal?" If yes, it is not a cross-signal synthesis and fails.
- **C-10 vs C-04**: C-04 checks that the cross-signal claim exists and is synthetic. C-10 checks that it is stated as a discrete, labeled artifact rather than embedded prose. An output can pass C-04 (the claim is present and genuinely synthetic) while failing C-10 (the claim is woven into a paragraph with no discrete identity).
- **C-11 vs C-03 + C-04**: C-03 requires the recommendation exists; C-04 requires the pattern exists. C-11 requires the two are explicitly connected by a stated logical bridge. All three can be present while C-11 fails if the connection is implicit.
- **C-12 vs C-06**: C-06 requires each uncertainty names a question that, if resolved, would change the recommendation. C-12 requires it also states the *direction* of that change (which verb it shifts to). An output can pass C-06 (change implied) while failing C-12 (direction not stated).

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-15 | Added C-10, C-11, C-12 from Round 1 excellence signals: pre-composition pattern artifact, pattern-to-recommendation traceability, decision-cost annotated uncertainty |
