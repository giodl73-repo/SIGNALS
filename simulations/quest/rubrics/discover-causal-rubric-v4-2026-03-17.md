Here is the complete updated rubric:

---

# /discover-causal Rubric — v4

**Skill:** `/discover-causal`
**Version:** v4 (upgraded from v3 based on R3 excellence signals — 2026-03-17)
**Max score:** 150 (Essential 60 + Recommended 30 + Aspirational 60)

---

## Changelog: v3 -> v4

- Aspirational band expanded from 45 pts (9 criteria) to 60 pts (12 criteria).
- Three new aspirational criteria added from R3 excellence signals:
  - C-17: AUTHORIZED SCOPE field enumerates a hypothesis-revision routing path as a named third legal value
  - C-18: MARGINAL CONTRIBUTION axes presented as labeled, independent slots rather than collapsed prose
  - C-19: Incomplete structured entries explicitly disqualified and not counted toward minimums
- Scoring Notes updated to reflect C-17-C-19 and their relationship to prior criteria.
- Essential and Recommended bands unchanged.

### R3 Signal Summary

V-02 uniquely passed C-14 (5/5) by producing AUTHORIZED SCOPE as a named required field with three explicit legal values: "full mechanism," "marginal contribution only -- dimensions: [list]," or "hypothesis requires revision before proceeding." V-01 got PARTIAL because a gate existed but scope was embedded as an instruction to Phase 2, not a named artifact field with enumerated outcomes. V-02 uniquely passed C-16 (5/5) by requiring MARGINAL CONTRIBUTION as a multi-line block with labeled dimension slots ("dimension 1, dimension 2, dimension 3 if applicable") rather than V-01's single-line singular-dimension field. V-02 also surfaced a row-validity enforcement pattern: "a row with an empty cell does not count toward the minimum" -- converting WHEN TO OBSERVE from a style preference into a structural gate on falsification completeness. C-09 (effect size) failed across all three variations; the gap remains unsolved through R3. C-17-C-19 extract the patterns that distinguish structural enforcement from structural suggestion.

---

## Structure Summary

- **4 Essential (C-01..C-04)** -- pathway, falsification, inertia check, AMEND. Failing any means the output skipped the actual work.
- **3 Recommended (C-05..C-07)** -- evidence, confounders, testability. Separates solid from minimal.
- **12 Aspirational (C-08..C-19)** -- depth, quantification, ordering discipline, inertia-aware amendment, operationalized falsification, explicit compliance, scope artifact, falsification timing, marginal dimensioning, scope routing, labeled dimension slots, entry disqualification. For mature analyses and structurally rigorous outputs.

---

## Essential Criteria (weight: 60 pts total -- 15 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Mechanism pathway traced** | depth | Output names a causal pathway from X to Y with at least one intermediate step. A bare assertion of correlation ("X causes Y") fails. The pathway must name the process, not just assert the link. |
| C-02 | **Falsification condition present** | correctness | Output names at least one observable condition that would prove the mechanism wrong. Vague hedges do not count. |
| C-03 | **Inertia check performed** | correctness | Output explicitly asks and answers whether doing nothing would also produce Y. Must resolve the check -- not just acknowledge it exists. |
| C-04 | **AMEND section produced** | behavior | Output concludes with an AMEND block that changes the hypothesis -- not just restates it. |

---

## Recommended Criteria (weight: 30 pts total -- 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Evidence cited** | coverage | At least one piece of supporting evidence, or an explicit statement that none exists. |
| C-06 | **Confounders identified** | depth | At least one alternative explanation independent of the inertia check. |
| C-07 | **Narrowed claim is more testable** | correctness | AMEND version is more specific and falsifiable than the original. |

---

## Aspirational Criteria (weight: 60 pts total -- 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Multi-step causal chain traced** | depth | Pathway traces through at least two intermediates (X -> M1 -> M2 -> Y). |
| C-09 | **Effect size or probability estimated** | depth | Rough quantification of the causal link grounded in evidence or mechanism logic. |
| C-10 | **Inertia resolved before mechanism trace is constructed** | ordering | Inertia check performed and resolved before the mechanism pathway is traced. Retroactive caveats do not pass. |
| C-11 | **AMEND accounts for X's marginal contribution over inertia** | correctness | When INERTIA is Partial or Yes, AMEND explicitly states what X contributes beyond inertia. |
| C-12 | **Falsification conditions include a How-to-Observe test** | correctness | Each falsification condition names a specific observable. No operationalization = fail. |
| C-13 | **Section compliance explicitly surfaced** | behavior | Output names the status of each major section -- either confirming completion or naming the specific gap. |
| C-14 | **Written scope declaration produced before mechanism tracing** | ordering | A distinct, findable scope artifact appears before any mechanism steps. Not prose embedded within the trace. |
| C-15 | **WHEN TO OBSERVE specified in falsification conditions** | correctness | Each falsification condition specifies when the observation would be made (deployment stage, time window, test protocol). C-12 requires HOW; C-15 requires WHEN in addition. |
| C-16 | **Marginal contribution dimensioned across multiple named axes** | depth | When INERTIA is Partial or Yes, AMEND covers at least two distinct named dimensions. A single-axis statement fails. |
| C-17 | **Scope declaration enumerates a hypothesis-revision routing path** | ordering | The scope declaration (C-14) names at least three legal outcomes, one of which explicitly routes back to the hypothesis before mechanism tracing begins. Binary gates (proceed/stop) and two-value fields fail. C-17 requires that artifact to offer revision as a first-class outcome. |
| C-18 | **Marginal contribution axes presented as labeled independent slots** | depth | When INERTIA is Partial or Yes, each axis appears as a separately labeled slot (e.g., "DIMENSION 1: [name] -- [claim]"), not as free-form prose. Labeled slots prevent multiple axes from collapsing into one fluent phrase. C-16 requires multiple axes; C-18 requires each to be independently labeled and verifiable. |
| C-19 | **Incomplete structured entries explicitly disqualified** | behavior | When a falsification condition or mechanism step is missing a required component, the output explicitly identifies it as non-qualifying and does not count it toward minimums. Silently counting a partial entry fails. C-12/C-15 require the components; C-19 requires the output to self-audit and name disqualifications. |

---

**New criteria rationale:**

- **C-17** upgrades C-14 from gate to decision tree. The key R3 finding: V-01 had a gate (C-10 pass) and a scope step (C-14 partial) but only binary routing. V-02 added "hypothesis requires revision before proceeding" as a third named value, turning scope declaration into an actual checkpoint with a revision path. That third value is the difference.

- **C-18** upgrades C-16 from presence to structure. Free-form prose can satisfy C-16 by mentioning two dimensions in one sentence — labeled slots cannot hide that. The R3 pass pattern from V-02 ("dimension 1, dimension 2, dimension 3 if applicable") makes each axis independently auditable.

- **C-19** converts C-12/C-15 field requirements into output-level enforcement. V-02's row-validity rule ("empty cell disqualifies the row") is what produces outputs that self-audit rather than silently count incomplete entries. C-19 closes the silent-partial-credit gap.
d + reliability, cost + completeness, latency + coverage). A single-axis statement ("X is faster than inertia") does not pass. C-11 requires marginal contribution to be stated; C-16 requires it to be multi-dimensional. |
| C-17 | **Scope declaration enumerates a hypothesis-revision routing path** | ordering | The written scope declaration (C-14) contains at least three named legal outcomes, one of which explicitly routes back to the hypothesis before any mechanism tracing begins. The revision path must be named as an outcome (e.g., "hypothesis requires revision before proceeding") -- not merely implied by a stop instruction. Binary gates (proceed/stop) and scope fields with only two values fail. C-14 requires a named scope artifact; C-17 requires that artifact to offer a revision route as a first-class outcome alongside proceed variants. |
| C-18 | **Marginal contribution axes presented as labeled independent slots** | depth | When INERTIA is Partial or Yes, each marginal contribution axis appears as a separately labeled slot (e.g., "DIMENSION 1: [name] -- [claim]", "DIMENSION 2: [name] -- [claim]") rather than as free-form prose or a combined multi-sentence statement. Labeled slots make each axis independently verifiable and prevent multiple axes from collapsing into one fluent phrase. C-16 requires multiple axes; C-18 requires each axis to be a separately labeled, independently verifiable unit. |
| C-19 | **Incomplete structured entries explicitly disqualified** | behavior | When a falsification condition or mechanism step is missing a required component (WHAT/HOW/WHEN TO OBSERVE for falsification; named process for mechanism steps), the output explicitly identifies it as non-qualifying and does not count it toward the stated minimum. Silently counting a partial entry, or silently omitting the gap without notice, fails. C-12 and C-15 require the components to be present; C-19 requires the output to self-audit by naming and disqualifying entries where components are absent. |

---

## Scoring Notes

- C-01 and C-02 are the minimum for any useful causal analysis. Failing either means the output has not done the work the skill requires.
- C-03 is the most commonly skipped check -- its presence is essential even if the answer is "no, inertia does not produce Y."
- C-04 enforces the AMEND behavior. An output that diagnoses but does not amend is incomplete.
- C-05 through C-07 distinguish a solid output from a minimal one.
- C-08 and C-09 are for mature, well-evidenced causal analyses. Absence does not penalize early-stage work.
- C-10 penalizes a specific structural failure: building the mechanism over the wrong Y. Retroactive inertia caveats pass C-03 but fail C-10.
- C-11 closes the gap left by outputs that resolve C-03 but then ignore the Partial/Yes finding in the AMEND. C-03 and C-11 together enforce the full inertia discipline.
- C-12 upgrades falsification from assertion to operationalization. C-02 requires a falsification condition; C-12 requires that condition to be testable.
- C-13 rewards outputs that self-audit rather than silently underspecify. Gate-architecture outputs (PATHWAY GATE, INERTIA GATE, AMEND GATE) typically pass; prose outputs that omit a section without flagging it fail.
- C-14 distinguishes commitment from ordering. C-10 verifies that inertia precedes mechanism; C-14 verifies that a written scope artifact exists as a checkpoint between inertia resolution and mechanism tracing. An output can satisfy C-10 (correct ordering) and fail C-14 (no written scope statement). R3 signal: V-01 passed C-10 but got PARTIAL on C-14 because scope adjustment was embedded as an instruction to Phase 2, not a named artifact field.
- C-15 adds the timing dimension to falsification. C-12 requires WHAT and HOW; C-15 requires WHEN. A complete falsification condition specifies the observable result (WHAT), the measurement or detection method (HOW), and the stage or window in which the test should be run (WHEN). R2 signal: V-03 uniquely passed C-12 by requiring all three as named required fields; variations with only two fields scored PARTIAL.
- C-16 penalizes single-axis marginal framing. C-11 requires marginal contribution to be present; C-16 requires it to be substantive -- covering at least two named dimensions. R3 signal: V-01 scored PARTIAL because its MARGINAL CONTRIBUTION field was singular; V-02 passed by requiring a multi-line block.
- C-17 upgrades C-14 from gate to decision tree. C-14 requires a named scope artifact; C-17 requires that artifact to carry a third legal value that routes back to the hypothesis. The revision path matters because it converts scope declaration from a formality into a real checkpoint -- an output that finds INERTIA: YES must be able to route back rather than forcing a proceed-or-stop choice. R3 signal: V-02's AUTHORIZED SCOPE with three explicit values including "hypothesis requires revision before proceeding" is the canonical pass pattern.
- C-18 upgrades C-16 from presence to structure. C-16 requires multiple axes; C-18 requires each axis to be a separately labeled unit. Free-form prose can name two dimensions in one sentence and satisfy C-16 while obscuring whether they are genuinely independent claims or reframings of the same assertion. Labeled slots make that ambiguity structurally impossible. R3 signal: V-02's "dimension 1, dimension 2, dimension 3 if applicable" block is the canonical pass pattern; V-01's single-line field failed C-16 and could not have passed C-18.
- C-19 converts field requirements into output-level enforcement. C-12 and C-15 require components to be present; C-19 requires the output to announce when they are not and exclude the entry from its count. This closes the silent-partial-credit gap: an output that lists two falsification conditions where one is incomplete but unchallenged is presenting weaker evidence than it claims. R3 signal: V-02's row-validity rule ("a row with an empty cell does not count toward the minimum") is the structural mechanism that produces C-19-compliant outputs.
