Reading the scorecard carefully to extract the new patterns before writing.

Three new excellence signals in R2 not yet captured as criteria:

1. **Kill barrier temporal persistence test** (V-07): Kill barrier is not just identified at T=0 — it is explicitly qualified to persist at T=0 AND remain unresolved at T=18mo. Integrates C-04 with C-10 into a new test.

2. **Labeled causal chain sub-parts** (V-10): Four labeled parts (what the barrier is / why it persists / what the intervention targets / why that lever works) that structurally prevent "what" vs "why" conflation — the gap that left V-09 at PARTIAL on C-13.

3. **Mitigation confirmation signal** (V-07's C-13 evidence): Beyond explaining *why* the mitigation works (C-13), the output specifies a future-dated observable condition that would confirm the intervention is working. No existing criterion captures this forward anchor.

---

```markdown
# Rubric -- validate-inertia v3

**Version:** v3
**Updated:** 2026-03-17
**Change from v2:** Added three new aspirational criteria (C-14, C-15, C-16) extracted from Round 2
excellence signals.

---

## Structure Summary

- **5 essential (C-01--C-05):** per-persona mapping, quantified switching cost, per-persona inertia
  scores, kill-barrier callout, aggregate risk verdict
- **3 recommended (C-06--C-08):** workaround satisfaction, habit lock-in + social proof coverage,
  mitigation path for the kill barrier
- **8 aspirational (C-09--C-16):** scoring methodology transparency, time-dependent inertia
  trajectory, status-quo competitor framing, named social proof threshold, mitigation tied to
  structural root cause, kill barrier temporal persistence test, causal chain with labeled
  structural sub-parts, mitigation confirmation signal

Scoring: Essential = 10 pts each (50 total), Recommended = 10 pts each (30 total), Aspirational =
10 pts each (80 total) = **160 pts max**.

---

## Essential Criteria (all must pass)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Per-persona inertia mapping** | correctness | Output identifies two or more named user personas and maps each to one or more inertia factors. Generic "users" without persona differentiation fails. |
| C-02 | **Quantified switching cost** | correctness | At least one persona has a switching cost expressed as a measurable value -- time, money, effort rating (1-10), or steps. Qualitative-only ("it's hard") fails. |
| C-03 | **Per-persona inertia score** | correctness | Each mapped persona has an explicit inertia score (numeric or Low/Medium/High/Critical). A single blanket score for all personas fails. |
| C-04 | **Kill-barrier identification** | depth | Output identifies exactly one adoption killer -- the single factor most likely to block adoption even if all other inertia is resolved. Must be labeled distinctly. |
| C-05 | **Overall adoption inertia risk** | correctness | Output produces an aggregate risk verdict with a sentence of rationale tying it back to the per-persona scores. |

---

## Recommended Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Current workaround satisfaction assessed** | coverage | For at least one persona, output describes how satisfied they are with their current workaround and why that satisfaction creates inertia. |
| C-07 | **Habit lock-in and social proof addressed** | coverage | Output addresses habit lock-in AND social proof for at least one persona each. Missing both fails; covering one partially passes. |
| C-08 | **Mitigation path per critical barrier** | depth | For the kill barrier in C-04, output proposes at least one concrete mitigation that could reduce or eliminate that barrier. |

---

## Aspirational Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Inertia score methodology explained** | behavior | Output briefly explains how inertia scores were derived -- what factors were weighted and why. A single sentence per dimension suffices. |
| C-10 | **Adoption timeline sensitivity** | depth | Output includes at least one time-dependent statement on how inertia evolves (e.g., "after 6 months of workaround use, lock-in doubles"). |
| C-11 | **Status-quo framed as named competitor** | depth | For the kill barrier in C-04, output names the dimension on which the current solution *wins* and explains why that competitive advantage is durable -- not just "people are used to it" but what property of the current solution makes it structurally hard to displace. |
| C-12 | **Named social proof threshold** | coverage | For at least one persona where social proof is a factor, output specifies the adoption threshold as a concrete condition or count (e.g., "needs 2+ teammates before committing," "will adopt solo if manager mandates it"). Binary Y/N without a named threshold fails. |
| C-13 | **Mitigation tied to structural root cause** | depth | The mitigation from C-08 explicitly explains *why* the intervention neutralizes the structural reason the barrier exists -- not just what to do, but why that lever addresses the specific root cause named in C-04. Addressing a symptom rather than the stated structural cause fails. |
| C-14 | **Kill barrier tested against temporal persistence** | depth | The kill barrier identified in C-04 is explicitly qualified against a temporal horizon -- output states that the barrier persists at T=0 AND remains unresolved at the longest time horizon considered (e.g., T=18mo). A kill barrier identified only as a current-state snapshot without temporal qualification fails. |
| C-15 | **Causal chain with labeled structural sub-parts** | depth | For the kill barrier, output provides a causal chain with explicitly labeled, distinct sub-parts covering: (1) what the barrier is, (2) why it structurally persists, (3) what the intervention targets, and (4) why that lever resolves the structural root cause. An analysis that merges any two sub-parts into a single statement, or that provides fewer than four labeled parts, fails. |
| C-16 | **Mitigation confirmation signal specified** | depth | The kill barrier mitigation from C-08 includes a named leading indicator or observable condition at a future time point (e.g., "at T=6mo, [X behavior] would confirm the barrier is reducing") that would confirm the intervention is working. A mitigation without a forward-looking confirmation condition fails. |

---

## Notes

- A rubric pass requires all 5 essential criteria to pass individually.
- Aspirational criteria may receive PARTIAL (5 pts) for genuine attempts that fall short of the
  full pass condition.
- C-11 is distinct from C-04: C-04 identifies the kill barrier; C-11 reframes that barrier as a
  competitive-displacement problem with a named winning dimension.
- C-13 sharpens C-08: C-08 requires a concrete mitigation; C-13 requires the mitigation to be
  causally linked to the root cause stated in C-04.
- C-14 extends C-04 and C-10: C-04 requires identification; C-10 requires time-dependent
  statements; C-14 requires the kill barrier specifically to be validated across the full temporal
  horizon, not just mentioned in passing.
- C-15 sharpens C-13: C-13 requires causal linkage; C-15 requires that linkage to be expressed
  as four explicitly labeled sub-parts so "what" and "why" cannot be conflated. C-15 is the
  structural closure for C-13 that prevented V-09 from passing at full credit.
- C-16 extends C-13: C-13 explains why the mitigation works; C-16 requires a forward-dated
  observable condition that would confirm it is working. Together they form the complete
  mitigation chain: mechanism + confirmation signal.

---

## v3 Change Log

| Criterion | Change | Source |
|-----------|--------|--------|
| C-14 | New aspirational | V-07 kill barrier qualification: "must persist at T=0 AND remain unresolved at T=18mo" -- temporal persistence test not captured by C-04 (identification only) or C-10 (general time-dependency) |
| C-15 | New aspirational | V-10 four-part causal chain: labeled sub-parts structurally prevent "what" vs. "why" conflation; root cause of V-09 C-13 PARTIAL where general mitigation field could not enforce causal separation |
| C-16 | New aspirational | V-07 C-13 evidence: "explain why this lever addresses the structural reason the barrier persists at T=0 and what evidence at T=6mo would confirm the mitigation is working" -- confirmation signal as a distinct requirement beyond C-13's causal explanation |
| Scoring max | 130 -> 160 | Three new aspirational criteria at 10 pts each |
```
