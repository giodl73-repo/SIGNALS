The scorecard data I need is all in the prompt. Three new excellence patterns from Round 7:

1. **V-03 C-08**: "Beat 1 declares hypothesis as falsifiable claim, providing inertia baseline" — the *form* of the hypothesis matters; a vague intent statement has no reference point for the delta.
2. **V-01 C-09**: "Anti-stagnation check" — S0 = S3 is a pattern failure; the delta must show substantive mutation, not confirmation.
3. **V-02 C-07**: "Contradicting a RESOLVED verdict requires explicit reasoning" — prior-verdict override must be named, not silent.

---

# Quest Rubric — `topic-story` v7

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
| C-19 | **Non-substitution constraint** | correctness | aspirational | The story explicitly states that an artifact produced in an earlier stage or section does not satisfy the requirement for its placement in a later stage or section. Each required placement must be independently satisfied — prior-stage presence is not credit. A prompt or template that allows the bridge sentence produced in the analysis block to serve as the bridge sentence required in the recommendation beat fails. The non-substitution rule must be stated explicitly for each placement requirement where early production could otherwise imply late satisfaction. |
| C-20 | **Multi-stage consistency enforcement** | correctness | aspirational | Critical claims — evidence posture, pattern statement, recommendation verb — appear at multiple designated positions in the output such that inconsistency between stages is self-revealing without requiring the reader to manually compare sections. A single-point certification (posture named once, in one place) fails. The required redundancy is structural: each critical claim must appear at a minimum of two named positions whose pairing is visible in the output. An output where a claim could change between an early stage and the recommendation beat without contradiction being structurally visible fails. |
| C-21 | **Falsifiable hypothesis as inertia baseline** | depth | aspirational | The initial hypothesis (Beat 1 / "What we set out to understand") is stated as a falsifiable claim — a specific proposition that the signals can confirm, refute, or modify. A vague intent statement ("we set out to understand X") fails; the hypothesis must be a claim that could be proven wrong ("we believed X" / "our hypothesis: X holds"). This creates the measurable inertia baseline against which the S0→S3 delta is computed — without a falsifiable starting position, the delta has no reference point and C-09's contrast collapses into a description rather than a measurement. |
| C-22 | **Anti-stagnation constraint** | depth | aspirational | The S0→S3 delta shows substantive mutation: the evolved hypothesis differs from the initial in a way that affects the recommendation's direction or confidence level. An output must demonstrate — not merely assert — how the signals shifted, strengthened, or undermined the initial hypothesis in a named way. A delta that amounts to "the signals confirmed what we already believed" without naming how confidence changed fails. S0 = S3 is a pattern failure regardless of how it is framed. The anti-stagnation check is not satisfied by a contrastive statement that could have been written before the signals were read. Depends on C-21: C-22 cannot pass if C-21 fails. |
| C-23 | **Prior-verdict override discipline** | correctness | aspirational | If a prior beat or stage produces a verdict — an adjudicated signal stance, a RESOLVED conflict determination, or an intermediate recommendation — the recommendation beat cannot contradict it without an explicit, named override reason. Silent contradiction fails: a recommendation verb inconsistent with a prior-stage verdict is a correctness error, not a stylistic choice. The override sentence must identify which verdict is being superseded and state the reason the final recommendation departs from it. A recommendation that is merely consistent with prior verdicts requires no additional action; this criterion applies only where a contradiction exists. |

---

## Scoring Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Where N_essential = 4, N_recommended = 3, N_aspirational = 16.

**Golden threshold**: all essential criteria pass AND composite >= 80.

### Score Bands

| Score | Interpretation |
|-------|----------------|
| Any essential fails | Not useful — do not use output |

---

**Changes from v6 to v7:**

| | v6 | v7 |
|---|---|---|
| N_aspirational | 13 | 16 |
| New criteria | — | C-21, C-22, C-23 |
| Source round | — | R7 |

**New aspirational criteria:**

- **C-21 — Falsifiable hypothesis as inertia baseline**: Beat 1 hypothesis must be a falsifiable claim, not a vague intent statement. Source: V-03 C-08 evidence ("Beat 1 declares hypothesis as falsifiable claim, providing inertia baseline"). Without a falsifiable starting position, C-09's delta has no reference point.

- **C-22 — Anti-stagnation constraint**: S0→S3 delta must show substantive mutation — S0 = S3 is a pattern failure. Source: V-01 C-09 evidence ("Anti-stagnation check"). Extends C-09's contrastive discovery requirement by demanding the contrast be genuine and not merely cosmetic. Depends on C-21.

- **C-23 — Prior-verdict override discipline**: A recommendation that contradicts a prior-stage verdict (RESOLVED conflict, adjudicated stance) without explicit named override reasoning fails. Source: V-02 C-07 evidence ("Contradicting a RESOLVED verdict requires explicit reasoning"). Closes the silent-contradiction gap not addressed by C-07, C-11, or C-17.
