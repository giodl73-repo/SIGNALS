Here is the complete updated rubric:

---

# Scout-Size Rubric — v2

**Skill**: scout-size
**Version**: v2 (updated from v1 — added C-11, C-12 from R1 excellence signals)
**Date**: 2026-03-16

---

## Purpose

This rubric scores the output of the `scout-size` skill against 12 criteria grouped into three tiers: Essential (must pass), Recommended (output is better with these), and Aspirational (raise the bar). A scorecard runner evaluates each criterion as PASS, PARTIAL, or FAIL and computes a composite score.

---

## Criteria

### Essential (60 pts total — must all pass to reach golden)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Surface area enumerated** | completeness | Output names each integration point individually and provides a total count (e.g., "API endpoint, auth hook, event bus subscription — 3 integration points"). A general description without named points and a count fails. |
| C-02 | **Complexity tier on-scale** | correctness | Output assigns exactly one of: LOW / MEDIUM / HIGH / XL — this vocabulary, nothing else. "MODERATE", "3/5", or "complex" all fail. The vocabulary is load-bearing; downstream skills parse it. |
| C-03 | **Inertia check present** | completeness | Output explicitly compares building the feature against the cost of maintaining the current workaround (or absence of the feature). The comparison must name what the workaround is and give a directional cost judgment (cheaper / comparable / more expensive). Omitting the check entirely fails; a one-liner that names the workaround and cost direction passes. |
| C-04 | **Confidence level stated with basis** | correctness | Output states a confidence level (HIGH / MEDIUM / LOW, or a percentage band) and identifies what drives that confidence — e.g., "MEDIUM — surface area is clear but integration behavior with the legacy auth layer is unverified." A bare "confidence: HIGH" with no basis fails. |
| C-05 | **Signal boundary respected** | behavior | Output does NOT contain task breakdowns, sprint assignments, owner names, or milestone dates. It is a sizing signal, not a plan. Presence of any assigned task ("Sprint 1: implement X") fails this criterion. |

### Recommended (30 pts total — output is better with these)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Team-size signal names specialist types** | depth | Output identifies the specialist disciplines needed (e.g., "1 backend, 1 platform, 0.5 PM") not just a headcount. "3 engineers" alone fails; "1 backend engineer, 1 frontend engineer, 0.5 PM" passes. |
| C-07 | **Timeline signal given as sprint range** | depth | Output gives a sprint range estimate (e.g., "3-5 sprints") — not a calendar date, not a single fixed number. A range communicates uncertainty appropriately; a point estimate or calendar date fails. |
| C-08 | **Primary complexity driver identified** | depth | Output names the one or two factors that most drive the complexity tier rating. Generic justification ("it's complex") fails. |

### Aspirational (10 pts total — raise the bar)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Sensitivity: what changes the tier** | depth | Output states at least one condition that would push the complexity tier up and one that would push it down. The conditions must be **tier-specific** — sprint-range sensitivity does not satisfy this criterion. |
| C-10 | **Confidence calibration: what would change it** | depth | Output states what information or investigation result would materially raise or lower the stated confidence level. |
| C-11 | **Confidence gap named** | depth | Output explicitly names the specific thing that is NOT yet known or verified — the primary source of residual uncertainty — distinct from the basis of what IS known. For example: "gap: webhook delivery contract with the legacy auth layer is unverified." C-04 requires naming what supports the confidence rating; C-11 requires naming what limits it. Outputs that state only the positive basis without identifying the specific unknown fall short. |
| C-12 | **Sensitivity framed as single named conditions** | depth | Each sensitivity direction (tier up, tier down) is stated as one specific, named condition — not a list of factors or a vague hedge. "Several factors could push the tier up" fails; "tier rises to XL if offline sync is required" passes. This is a refinement of C-09: C-09 requires tier up/down conditions; C-12 requires each to be a single named condition with a direct tier consequence stated. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Patterns to Watch (v2 additions in bold)

- **Plan creep** — violates C-05. Most likely failure mode.
- **Tier without scale** — "MODERATE" / numeric scores fail C-02.
- **Silent inertia** — workaround mentioned without cost direction fails C-03.
- **Bare confidence** — label without basis fails C-04.
- **Dimension-mismatch sensitivity** — sprint-range sensitivity instead of tier sensitivity fails C-09. V-03's near-miss in R1.
- **Basis without gap** — confidence basis present but specific unknown omitted fails C-11.
- **Vague sensitivity** — "several factors could push this higher" instead of one named condition fails C-12.

---

**Two new excellence patterns extracted from R1:**

- **C-11** comes from V-02 TABLE 4's `Gap` column, V-03 STEP 5's "the gap", and V-04 Q6's "What is unverified?" — three independent variants converged on naming the specific unknown that limits confidence. That convergence across the best outputs makes it a real signal.

- **C-12** comes from V-04's "What SINGLE condition would push this tier one step up / one step down?" framing. The single-condition constraint eliminates the hedge ("several things could raise this") that makes sensitivity non-actionable. V-03 showed the failure mode: it provided sensitivity on the wrong dimension (sprint range instead of tier) — which C-09 didn't clearly exclude. C-12 tightens both the dimension requirement and the precision requirement.
s that focus entirely on the new build and mention the workaround
  only in passing ("users currently use a spreadsheet") fail C-03. The check requires a
  cost comparison, not just a name.
- **Bare confidence**: stating "confidence: HIGH" with no basis is common. C-04 requires
  a reason -- the basis is what makes the confidence actionable.
- **Dimension-mismatch sensitivity**: outputs that provide sprint-range sensitivity (sprint
  count goes up/down given conditions) instead of tier sensitivity (LOW/MEDIUM/HIGH/XL moves
  given conditions) satisfy the instinct behind C-09 but fail the criterion. The tier is
  the load-bearing signal; sprint ranges are a recommended output, not the sensitivity axis.
  This was V-03's near-miss in R1.
- **Basis without gap**: outputs that fully justify their confidence rating (C-04) but omit
  what is specifically unverified fail C-11. The gap is what makes the confidence rating
  actionable -- it tells the team exactly what to investigate next.
- **Vague sensitivity**: sensitivity stated as "several factors could push this higher" fails
  C-12. Each direction requires a named single condition with the resulting tier stated.

---

## v2 Change Log

| Change | Reason |
|--------|--------|
| Added C-11: Confidence gap named | R1 scorecard: V-02 TABLE 4 "Gap" column, V-03 STEP 5 "the gap", V-04 Q6 "What is unverified?" -- all three high-scoring variants independently named the specific unknown that limits confidence. This pattern was absent from v1 and appeared consistently across the best outputs. |
| Added C-12: Single-condition sensitivity framing | R1 scorecard: V-04's "What single condition would push this tier one step up / one step down?" produced sharper, more actionable sensitivity than V-02 (no tier sensitivity) or V-03 (wrong dimension). The single-condition constraint forces precision that a list of factors avoids. |
| Added dimension-mismatch to failure patterns | R1 scorecard: V-03 provided sprint-range sensitivity instead of tier sensitivity -- a near-miss that v1's C-09 text did not clearly exclude. New failure pattern makes the distinction explicit. |
| Added basis-without-gap to failure patterns | Counterpart to the C-11 addition -- names the most likely way C-11 fails. |
| Added vague-sensitivity to failure patterns | Counterpart to the C-12 addition -- names the most likely way C-12 fails. |
| Updated scoring formula: aspirational_pass / 4 | Aspirational tier now has 4 criteria instead of 2; formula denominator updated accordingly. Each aspirational criterion is worth 2.5 pts. |
| Updated score table | Reflects 4-criterion aspirational tier. |
