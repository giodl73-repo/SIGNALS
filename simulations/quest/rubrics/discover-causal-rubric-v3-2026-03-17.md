Looking at the R2 scorecard, I need to identify which patterns produced full passes on criteria where other variations only got PARTIALs, and what new output dimensions those patterns reveal.

Key signals from R2:
- **V-04** uniquely passed C-10 (5/5) via an explicit "may not proceed" gate + verbatim scope declaration. Others got 3–4/5 with ordering instructions alone.
- **V-03** uniquely passed C-12 (5/5) by requiring WHEN TO OBSERVE as a third named required field. Others got 3/5 with only WHAT + HOW.
- **V-02** scored 4/5 on C-10 via a required written MARGINAL SCOPE artifact before mechanism tracing — a distinct approach from V-04's gate architecture.
- **C-09** failed across all four variations — no variation required quantification, confirming this remains an unsolved aspirational gap.

New output criteria emerging from R2:

1. **C-14** — Written scope declaration as a named artifact before mechanism tracing (from V-02/V-04 patterns)
2. **C-15** — WHEN TO OBSERVE present in each falsification condition (from V-03 pattern)
3. **C-16** — Marginal contribution dimensioned across multiple named axes (from V-02's table structure)

---

# /discover-causal Rubric — v3

**Skill:** `/discover-causal`
**Version:** v3 (upgraded from v2 based on R2 excellence signals — 2026-03-17)
**Max score:** 135 (Essential 60 + Recommended 30 + Aspirational 45)

---

## Changelog: v2 → v3

- Aspirational band expanded from 30 pts (6 criteria) to 45 pts (9 criteria).
- Three new aspirational criteria added from R2 excellence signals:
  - C-14: Written scope declaration produced as a named artifact before mechanism tracing
  - C-15: WHEN TO OBSERVE specified in each falsification condition
  - C-16: Marginal contribution dimensioned across multiple named axes
- Scoring Notes updated to reflect C-14–C-16 and their relationship to prior criteria.
- Essential and Recommended bands unchanged.

### R2 Signal Summary

V-04 uniquely passed C-10 (5/5) via an explicit "may not proceed" gate tied to a verbatim scope declaration block; three other variations achieved only PARTIAL (3–4/5) despite strong ordering instructions. V-03 uniquely passed C-12 (5/5) by requiring WHEN TO OBSERVE as a required named field alongside WHAT and HOW; three others scored PARTIAL. V-02 approached C-10 differently — a required written MARGINAL SCOPE artifact — scoring 4/5 without a hard gate. C-09 (effect size) failed across all four variations; no variation has yet required quantification. C-14–C-16 extract the patterns that distinguished full passes from partials.

---

## Structure Summary

- **4 Essential (C-01..C-04)** — pathway, falsification, inertia check, AMEND. Failing any means the output skipped the actual work.
- **3 Recommended (C-05..C-07)** — evidence, confounders, testability. Separates solid from minimal.
- **9 Aspirational (C-08..C-16)** — depth, quantification, ordering discipline, inertia-aware amendment, operationalized falsification, explicit compliance, scope artifact, falsification timing, marginal dimensioning. For mature analyses and structurally rigorous outputs.

The inertia check (C-03) is marked essential because the skill description calls it "the most commonly skipped eval" — making it a soft criterion would defeat the point.

---

## Essential Criteria (weight: 60 pts total — 15 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Mechanism pathway traced** | depth | Output names a causal pathway from X to Y with at least one intermediate step. A bare assertion of correlation ("X causes Y") fails. The pathway must name the process, not just assert the link. |
| C-02 | **Falsification condition present** | correctness | Output names at least one observable condition that would prove the mechanism wrong (e.g., "if Y occurs even when X is absent, the mechanism is broken"). Vague hedges like "it might not work" do not count. |
| C-03 | **Inertia check performed** | correctness | Output explicitly asks and answers whether doing nothing (no feature, no X) would also produce Y. Must resolve the check — not just acknowledge it exists. |
| C-04 | **AMEND section produced** | behavior | Output concludes with an AMEND block that narrows the causal claim, adds the mechanism pathway, or adds a falsification condition. AMEND must change the hypothesis, not just restate it. |

---

## Recommended Criteria (weight: 30 pts total — 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Evidence cited** | coverage | Output references at least one piece of supporting evidence — data, research, analogous feature, or domain pattern — showing the mechanism has held in a comparable context. If no evidence exists, the output says so explicitly. |
| C-06 | **Confounders identified** | depth | Output names at least one alternative explanation or confounding variable that could produce Y without X, independent of the inertia check. |
| C-07 | **Narrowed claim is more testable** | correctness | The AMEND version of the hypothesis is more specific and falsifiable than the original. A reviewer reading both should agree the amended version is easier to prove wrong. |

---

## Aspirational Criteria (weight: 45 pts total — 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Multi-step causal chain traced** | depth | Mechanism pathway traces through at least two intermediate variables (X → M1 → M2 → Y), showing propagation of effect rather than a single-hop claim. |
| C-09 | **Effect size or probability estimated** | depth | Output provides a rough quantification of the causal link — effect size, likelihood range, or order-of-magnitude estimate — grounded in cited evidence or mechanism logic. |
| C-10 | **Inertia resolved before mechanism trace is constructed** | ordering | The inertia check is performed and resolved before the mechanism pathway is traced. An output that builds the full mechanism and then adds an inertia caveat retroactively does not pass — the caveat is not the same as scoping the trace before building it. |
| C-11 | **AMEND accounts for X's marginal contribution over inertia** | correctness | When the inertia check resolves as Partial or Yes, the AMEND section explicitly states what X contributes beyond what inertia already produces (speed, reliability, cost, completeness, or equivalent dimension). An AMEND that does not address a Partial inertia finding is still a broken hypothesis. |
| C-12 | **Falsification conditions include a How-to-Observe test** | correctness | Each falsification condition names a specific observable — what would be measured, tracked, or observed to confirm the mechanism is broken. A falsification condition with no operationalization ("it might not work", "results could differ") does not pass. |
| C-13 | **Section compliance explicitly surfaced** | behavior | Output explicitly names the status of each major section (pathway, inertia, AMEND) — either confirming completion or naming the specific gap. A silently underspecified output is indistinguishable from a compliant one on casual read; naming the gap is the minimal pass. |
| C-14 | **Written scope declaration produced before mechanism tracing** | ordering | Before any mechanism steps appear, the output contains an explicit written statement naming what Y is being traced and what Y excludes — the marginal scope. This statement must appear as a distinct, findable artifact (e.g., a labeled declaration block or a named scope commitment line), not as scope-setting prose embedded within the mechanism trace itself. An output that resolves inertia and immediately begins tracing without a written scope commitment fails even if ordering is correct. |
| C-15 | **WHEN TO OBSERVE specified in falsification conditions** | correctness | Each falsification condition specifies when the observation would be made — at what stage of deployment, within what time window, or under what test protocol. C-12 requires HOW TO OBSERVE; C-15 requires a timing or test-context specification in addition. A falsification condition that names what to measure and how to measure it but gives no indication of when fails. |
| C-16 | **Marginal contribution dimensioned across multiple named axes** | depth | When the inertia check resolves as Partial or Yes, the AMEND section presents marginal contribution across at least two distinct named dimensions (e.g., speed + reliability, cost + completeness, latency + coverage). A single-axis statement ("X is faster than inertia") does not pass. C-11 requires marginal contribution to be stated; C-16 requires it to be multi-dimensional. |

---

## Scoring Notes

- C-01 and C-02 are the minimum for any useful causal analysis. Failing either means the output has not done the work the skill requires.
- C-03 is the most commonly skipped check — its presence is essential even if the answer is "no, inertia does not produce Y."
- C-04 enforces the AMEND behavior. An output that diagnoses but does not amend is incomplete.
- C-05 through C-07 distinguish a solid output from a minimal one.
- C-08 and C-09 are for mature, well-evidenced causal analyses. Absence does not penalize early-stage work.
- C-10 penalizes a specific structural failure: building the mechanism over the wrong Y. Retroactive inertia caveats pass C-03 but fail C-10.
- C-11 closes the gap left by outputs that resolve C-03 but then ignore the Partial/Yes finding in the AMEND. C-03 and C-11 together enforce the full inertia discipline.
- C-12 upgrades falsification from assertion to operationalization. C-02 requires a falsification condition; C-12 requires that condition to be testable.
- C-13 rewards outputs that self-audit rather than silently underspecify. Gate-architecture outputs (PATHWAY GATE, INERTIA GATE, AMEND GATE) typically pass; prose outputs that omit a section without flagging it fail.
- C-14 distinguishes commitment from ordering. C-10 verifies that inertia precedes mechanism; C-14 verifies that a written scope artifact exists as a checkpoint between inertia resolution and mechanism tracing. An output can satisfy C-10 (correct ordering) and fail C-14 (no written scope statement). R2 signal: V-04 passed C-10 with an explicit "may not proceed" gate tied to a verbatim scope declaration; V-02 nearly passed (4/5) with a required MARGINAL SCOPE artifact; three other variations stayed at PARTIAL despite strong ordering instructions.
- C-15 adds the timing dimension to falsification. C-12 requires WHAT and HOW; C-15 requires WHEN. A complete falsification condition specifies the observable result (WHAT), the measurement or detection method (HOW), and the stage or window in which the test should be run (WHEN). R2 signal: V-03 uniquely passed C-12 by requiring all three as named required fields; variations with only two fields scored PARTIAL.
- C-16 penalizes single-axis marginal framing. C-11 requires marginal contribution to be present; C-16 requires it to be substantive — covering at least two named dimensions so that the AMEND is not trivially bypassed by a one-line assertion. R2 signal: V-02's marginal contribution table requiring multiple explicit dimensions produced the clearest AMEND outputs of the round.
