Reading the scorecard carefully before writing.

Two systematic gaps emerge from Round 4:

1. **C-11 PARTIAL in all three variants** — every variant has the pattern and the verb, but none require the explicit connective sentence in the recommendation beat: *"[the named pattern] is why this verb was chosen."* The bridge is always implied, never stated.

2. **C-15 PARTIAL in V-03, but C-15 PASSES in V-01/V-02** — the distinction is structural. V-03's "write this before writing the narrative" is instructional framing only. V-01's Part 1/Part 2 split and V-02's named block with placement validation rules are structural proofs. The excellence signal: structural placement is the only enforceable proof of pre-composition.

New criteria:
- **C-17 — Explicit pattern-to-recommendation bridge**: closes the C-11 gap
- **C-18 — Structural pre-composition gate**: formalizes what separates V-01/V-02 from V-03 on C-15

---

# Quest Rubric — `topic-story` v5

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
| C-15 | **Delta pre-composition** | depth | aspirational | The contrastive discovery ("we expected X but found Y") is identified as a discrete analytic step before narrative prose begins — not arrived at during composition or appended as a closing observation. Parallel to C-10: the delta must exist as a named pre-writing output, not emerge organically from the writing. A delta statement that could have been written without prior comparative analysis fails. Absence of any evidence that the contrast was surfaced analytically before the story was composed fails. |
| C-16 | **Evidence-verb self-certification** | correctness | aspirational | The recommendation beat includes an explicit evidence posture statement — a sentence that names the overall signal posture (e.g., strong positive, mixed, conflicting, weak) and cites it as the direct basis for the verb chosen. A recommendation that states the verb without naming the posture that produced it fails. The posture statement must appear in the recommendation beat itself, not be inferred from the synthesis section. |
| C-17 | **Explicit pattern-to-recommendation bridge** | correctness | aspirational | The recommendation beat contains a sentence that names the cross-signal pattern by reference and identifies it as the stated reason for the verb chosen — not merely that both the pattern and the verb appear in the story. The bridge must be explicit: "Because [the named pattern], the recommendation is [verb]" or equivalent. A story where the pattern and the recommendation verb are present but connected only by implication or inference fails. The bridge sentence must appear in the recommendation beat, not in Beat 3. |
| C-18 | **Structural pre-composition gate** | depth | aspirational | Proof that analytic artifacts (pattern, delta) were produced before narrative writing is established by structural placement, not by instruction. A named Part 1 / Part 2 separator, a formally labeled block with a placement rule, or an equivalent structural device is required. Instructional language alone ("write the delta before writing the story") does not satisfy this criterion — the structure must make it verifiable. An output where pre-composition cannot be confirmed from structure alone fails. |

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
| C-15 | depth | aspirational |
| C-16 | correctness | aspirational |
| C-17 | correctness | aspirational |
| C-18 | depth | aspirational |

---

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial: C-01–C-09 |
| v2 | Added C-10 (pre-composition pattern artifact) |
| v3 | Added C-11–C-14 (traceability, decision-cost, accountability, self-sufficiency) |
| v4 | Added C-15 (delta pre-composition), C-16 (evidence-verb self-certification) |
| v5 | Added C-17 (explicit pattern-to-recommendation bridge) — closes C-11 PARTIAL gap universal across R4 variants; Added C-18 (structural pre-composition gate) — formalizes the V-01/V-02 vs V-03 split on C-15: instruction is not proof, structure is |
