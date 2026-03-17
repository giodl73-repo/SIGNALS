Reading the R13 scorecard for V-02 excellence signals not captured by C-01 through C-35.

Three new signals from V-02:

1. **Narrative-ledger closed-world constraint** — V-02 adds "Do not introduce new findings not in the LEDGER." C-34 requires the ledger be exhaustive; this new signal closes the other direction: the narrative may only draw from the ledger. Bidirectional closure.

2. **Pre-composition blocks as first-class output sections** — V-02 surfaces BLOCK D, BLOCK P, BLOCK B, LEDGER as named document sections in Part 1, not just internal steps. C-10/C-15 require pre-composition to occur; this requires it to be *visible* in the final artifact, making it auditable without inference.

3. **BLOCK B verbatim restatement in Beat 5** — V-02 requires BLOCK B to appear *verbatim* in Beat 5, not paraphrased. C-17 requires an explicit bridge; this closes interpretive drift between the analytical bridge and its narrative expression.

---

# Quest Rubric — `topic-story` v13

**Version:** v13
**Source rounds:** R1–R13
**Rubric version history:**
- v12 → v13: +3 aspirational criteria (C-36, C-37, C-38); N_aspirational 28 → 31
- v11 → v12: +3 aspirational criteria (C-33, C-34, C-35); N_aspirational 25 → 28
- v10 → v11: +3 aspirational criteria (C-30, C-31, C-32); N_aspirational 22 → 25
- v9 → v10: +2 aspirational criteria (C-28, C-29); N_aspirational 20 → 22

**What changed from v12 to v13:**

| | v12 | v13 |
|--|-----|-----|
| Version | v12 | v13 |
| Source rounds | R1–R12 | R1–R13 |
| Aspirational count | 28 | 31 |
| Total criteria | 35 | 38 |
| Composite formula denominator | 28 | 31 |

**Three new aspirational criteria from R13 (V-02 excellence signals):**

| C | Name | Axis | Category |
|---|------|------|----------|
| C-36 | Narrative-ledger closed-world constraint | V-02 | correctness |
| C-37 | Pre-composition blocks as first-class output sections | V-02 | depth |
| C-38 | BLOCK B verbatim restatement in Beat 5 | V-02 | correctness |

---

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
| C-18–C-32 | *(criteria defined in rounds R1–R11 — definitions carried forward from v11)* | — | aspirational | — |
| C-33 | **VERDICT narrative-explanatory enforcement statement** | correctness | aspirational | The VERDICT line is accompanied immediately by a co-located statement that prohibits narrative construction toward the verdict: e.g., "The narrative explains this verdict. It does not build toward it." A VERDICT that appears as a format instruction without a self-enforcing prohibition fails. The prohibition must be co-located with the VERDICT, not separated into a preamble or appendix. |
| C-34 | **Ledger exhaustiveness constraint** | coverage | aspirational | The LEDGER carries an explicit statement that every artifact must appear — both a positive requirement ("no artifact may be omitted") and a named failure condition ("a LEDGER that represents a selection rather than the full set fails"). A LEDGER that is exhaustive in practice but carries no self-enforcing exhaustiveness language fails. The constraint must be stated, not implied by the ledger format alone. |
| C-35 | **Delta block citation in Beat 5** | correctness | aspirational | Beat 5 cites BLOCK D by name with an inline summary clause that states the analytic function of the delta for the evidence posture — e.g., "The delta — [one-clause summary of BLOCK D] — is the signal that most defines this posture." A Beat 5 that names the posture and verb without citing the delta block that produced them fails. The citation must name BLOCK D explicitly, not refer to it obliquely or by inference. |
| C-36 | **Narrative-ledger closed-world constraint** | correctness | aspirational | The narrative beats may only cite artifacts and findings that appear in the LEDGER. No new evidence, signals, or conclusions enter the prose that were not pre-declared in the ledger. A narrative that introduces an artifact reference, dataset, or finding not present in the LEDGER fails. This criterion is the complement of C-34: C-34 requires the ledger to contain all artifacts; C-36 requires the narrative to draw only from the ledger. Both directions must close. A prompt that enforces ledger exhaustiveness without enforcing narrative boundedness satisfies C-34 but fails C-36. |
| C-37 | **Pre-composition blocks as first-class output sections** | depth | aspirational | BLOCK D, BLOCK P, BLOCK B, and LEDGER appear as named, labeled sections in the final output document — visible to the reader as discrete artifacts, not absorbed into narrative prose or retained only as internal reasoning steps. A story where the pre-composition work is present in the prose but not surfaced as distinct labeled sections fails. Making the blocks visible as output sections allows a reader to audit the analytical pre-work directly without inferring it from the narrative. A two-part document structure (analytical blocks in Part 1; narrative in Part 2) satisfies this criterion; an approach where the blocks are process instructions only does not. |
| C-38 | **BLOCK B verbatim restatement in Beat 5** | correctness | aspirational | The bridge sentence (BLOCK B) appears verbatim in Beat 5 — not paraphrased, summarized, or reworded. Beat 5 must contain the exact text of BLOCK B as written in the pre-composition block. A Beat 5 that references the pattern and the recommendation verb without using BLOCK B's exact language fails. Verbatim restatement closes the audit trail from pre-composition bridge to narrative recommendation: any divergence between what the bridge said analytically and what the recommendation beat says creates an undetectable interpretive shift. C-17 requires an explicit bridge; C-38 requires that bridge to be carried forward without transformation. |

---

## Composite Score Formula

```
composite = (aspirational_passes / 31) × 100
```

Denominator is 31 (all aspirational criteria, C-18 through C-32 included when rubric text is available for scoring). When criteria are unverifiable due to missing rubric text, report visible-only composite with an explicit adjustment note and upper/lower bounds.
