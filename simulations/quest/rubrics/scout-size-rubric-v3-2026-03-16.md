# Scout-Size Rubric — v3

**Skill**: scout-size
**Version**: v3 (updated from v2 — added C-13, C-14 from R2 excellence signals)
**Date**: 2026-03-16

---

## Purpose

This rubric scores the output of the `scout-size` skill against 14 criteria grouped into three tiers: Essential (must pass), Recommended (output is better with these), and Aspirational (raise the bar). A scorecard runner evaluates each criterion as PASS, PARTIAL, or FAIL and computes a composite score.

---

## Criteria

### Essential (60 pts total — must all pass to reach golden)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Surface area enumerated** | completeness | Output names each integration point individually and provides a total count (e.g., "API endpoint, auth hook, event bus subscription — 3 integration points"). A general description without named points and a count fails. |
| C-02 | **Complexity tier on-scale** | correctness | Output assigns exactly one of: LOW / MEDIUM / HIGH / XL — this vocabulary, nothing else. "MODERATE", "3/5", or "complex" all fail. The vocabulary is load-bearing; downstream skills parse it. |
| C-03 | **Inertia check present** | completeness | Output explicitly compares building the feature against the cost of maintaining the current workaround (or absence of the feature). The comparison must name what the workaround is and give a directional cost judgment (cheaper / comparable / more expensive). Omitting the check entirely fails; a one-liner that names the workaround and cost direction passes. Outputs that focus entirely on the new build and mention the workaround only in passing ("users currently use a spreadsheet") fail. |
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
| C-13 | **Sensitivity names explicit tier destination** | depth | Each sensitivity condition states the destination tier explicitly — `Tier rises to [LEVEL]` or `Tier drops to [LEVEL]`. A condition that says "tier would rise" or "this could bump the tier" without naming the target level fails. C-12 requires a single named condition; C-13 requires the destination tier to be unambiguous, not implied. The `[LEVEL]` slot must be filled with LOW / MEDIUM / HIGH / XL. |
| C-14 | **Sensitivity conditions are falsifiable** | depth | Each tier-shift condition is a verifiable scenario — one that could be confirmed or ruled out through concrete investigation (e.g., "confirm whether offline sync is required," "spike the webhook contract with the auth team"). Abstract hedges pass C-12 if they are named and singular but fail C-14 if they cannot be discovered: "if requirements change" and "if scope grows" are not conditions — they are deferrals. A condition passes C-14 when a reader can state what action would settle it. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Patterns to Watch (v3 additions in bold)

- **Plan creep** — violates C-05. Most likely failure mode.
- **Tier without scale** — "MODERATE" / numeric scores fail C-02.
- **Silent inertia** — workaround mentioned without cost direction fails C-03.
- **Bare confidence** — label without basis fails C-04.
- **Dimension-mismatch sensitivity** — sprint-range sensitivity instead of tier sensitivity fails C-09. V-03's near-miss in R1.
- **Basis without gap** — confidence basis present but specific unknown omitted fails C-11.
- **Vague sensitivity** — "several factors could push this higher" instead of one named condition fails C-12.
- **Implied tier destination** — sensitivity states direction ("tier rises") but omits the target level fails C-13. V-01's near-miss in R2: STEP 5 required "one named condition" but lacked `[LEVEL]` in its template, allowing outputs that satisfy C-12's intent while leaving the destination ambiguous.
- **Unfalsifiable condition** — named and singular condition that cannot be verified ("if scope grows") fails C-14. Passes C-12 on form; fails C-14 on substance.

---

**Two new excellence patterns extracted from R2:**

- **C-13** comes from V-01's PARTIAL on C-12: the prompt required a single named condition but its template omitted `[LEVEL]`, producing outputs where the tier destination was implied rather than stated. V-02 and V-03 both used fill-in templates that required `[LEVEL]` explicitly — and both earned PASS. The gap in V-01 is not about naming the condition; it is about naming where the condition lands. C-13 closes that gap as a separate, targeted criterion.

- **C-14** comes from V-02's "testability criterion stated" observation under C-12. V-02 listed four named failing forms and required that each condition be a scenario the team could actually investigate. A condition like "if offline sync is required" is falsifiable — it can be confirmed in a requirements conversation. A condition like "if scope grows" is not — it is a restatement of general risk. C-14 separates these: C-12 governs form (single, named, with tier consequence); C-14 governs substance (the condition must point to something discoverable).
