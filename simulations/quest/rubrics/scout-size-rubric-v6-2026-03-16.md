Reading the scorecard carefully. Two distinct patterns emerge from R5:

1. **Gate-level placement** — V-04 proves post-generation checklists don't satisfy C-17's "active at generation time" language. This needs its own criterion because C-17's adjacency requirement doesn't preclude checklist placement — it just says "adjacent." The new criterion names the precise failure mode: the model can complete all output fields before encountering the example.

2. **Role separation as structural relational guard** — V-03's two-phase design prevents basis/gap conflation not by restating the rule but by making conflation a charter violation. C-18 covers single-field structural encoding; this covers complementary-pair constraints. Genuinely new mechanism.

```markdown
# Scout-Size Rubric — v6

**Skill**: scout-size
**Version**: v6 (updated from v5 — added C-19, C-20 from R5 excellence signals)
**Date**: 2026-03-16

---

## Purpose

This rubric scores the output of the `scout-size` skill against 20 criteria grouped
into three tiers: Essential (must pass), Recommended (output is better with these),
and Aspirational (raise the bar). A scorecard runner evaluates each criterion as
PASS, PARTIAL, or FAIL and computes a composite score.

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
| C-15 | **Confidence basis and gap are non-overlapping** | depth | The confidence basis (C-04) and the confidence gap (C-11) address different dimensions of confidence. The basis names what IS established or verified; the gap names what is NOT yet known. An output fails if the gap negates or restates the basis — e.g., "Basis: API contract is established; Gap: API contract is not yet confirmed" answers both fields from the same dimension, one positive and one negative. Genuine non-overlap means the basis and gap point to different aspects of the sizing: the basis might name what makes confidence HIGH in one area while the gap names a separate area that remains unresolved. |
| C-16 | **Sensitivity destination tier differs from current tier** | depth | Each named sensitivity condition (C-13) states a destination tier that is different from the currently assigned complexity tier. A condition mapping a tier to itself — e.g., stating "Tier rises to MEDIUM" when the current tier is already MEDIUM — is vacuous: it either means the tier will not actually change, or the sensitivity is being stated without consequence. Tier transitions must show movement. If the current tier is HIGH, a valid tier-up condition must name XL; a valid tier-down condition must name MEDIUM or LOW. Repeating the current tier in a sensitivity slot fails this criterion regardless of whether C-12, C-13, and C-14 are otherwise satisfied. |
| C-17 | **High-risk constraints carry inline failure examples** | depth | Each constraint that has a documented failure mode from prior rounds includes a concrete counter-example at the point of the constraint — not in a separate "common errors" appendix. The example must appear adjacent to the constraint it illustrates so that the output field cannot be satisfied without the failure mode being active at generation time. An abstract "this is wrong" statement without a specific named example allows output to drift into compliant-but-vacuous forms. A constraint passes C-17 when a reader can tell immediately, from the constraint alone, what a failing output looks like. Prior documented failure modes for C-11, C-15, and C-16 make those constraints the minimum scope for this requirement. |
| C-18 | **Constraints encoded as structural features where format permits** | depth | Where the output format allows (named fields, table columns, required totals), the prompt encodes constraints as schema-level features rather than relying on prose instruction alone. A column header "[HIGH or XL — must be higher than current tier]" is harder to violate than a prose note saying "the tier must go up," because violation is visible at the field level without the reader needing to cross-reference a separate rules section. Instruction-only is sufficient to pass C-12 through C-16; structural encoding raises the bar by making constraint violations observable in the output skeleton itself. A prompt passes C-18 when at least the constraints for C-13 and C-16 — the two tier-value fields — are expressed as named columns or field labels rather than prose-only rules. |
| C-19 | **Inline failure examples precede the output field they govern** | depth | A WRONG/CORRECT block satisfies C-17's generation-time requirement only if it appears within or immediately before the field definition it governs — not in a post-output checklist, gate section, or "Review Your Output" block that follows the output skeleton. The test: if a model could complete all output fields before encountering the WRONG/CORRECT block, the block is a gate, not a guard. Gates may catch failures during human review; they do not prevent generation-time drift. A prompt passes C-19 when no C-17-scoped failure example appears after the last output field it governs. A variation that places WRONG/CORRECT examples in an end-of-prompt checklist satisfies C-17's adjacency intent but fails C-19 because the examples are inactive during field production. |
| C-20 | **Complementary constraint pairs use role-separated production** | depth | Where two constraints govern a relational pair of output fields (e.g., confidence basis / confidence gap, tier-up condition / tier-down condition), encoding them as separate role charters makes conflation a charter violation rather than a rule violation. V-03's two-phase design (Sizing Analyst produces the basis in Phase 1; Risk Assessor produces the gap in Phase 2, explicitly prohibited from re-using what the analyst confirmed) prevents C-15 conflation structurally: violating the non-overlap rule requires the assessor to break their own charter, which is observable at the role level rather than only at the output level. This is a C-18-style architectural technique applied to relational constraints rather than single-field constraints. A prompt passes C-20 when at least the basis/gap pair (C-15) is produced by role-separated steps with an explicit non-overlap charter stated in the second role's instructions. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Patterns to Watch (v6 additions in bold)

- **Plan creep** — violates C-05. Most likely failure mode.
- **Tier without scale** — "MODERATE" / numeric scores fail C-02.
- **Silent inertia** — workaround mentioned without cost direction fails C-03.
- **Basis-gap conflation** — gap negates rather than extends the basis; fails C-15. Guard must include an inline counter-example (C-17). Role separation (C-20) makes conflation a charter violation.
- **Null sensitivity** — tier destination repeats current tier; fails C-16. Structural column encoding (C-18) makes this visible without prose cross-referencing.
- **Register-dependent guard collapse** — conversational or imperative prompts that omit inline failure examples and structural field labels expose C-11, C-15, and C-16 to silent failure. C-17 and C-18 close this gap.
- **Gate-level guard placement** — WRONG/CORRECT examples in a post-output checklist or "Review Your Output" section are inactive during field production; fails C-19. Guards must precede or be embedded in the field definition, not follow the full output skeleton.
- **Role structure without non-overlap charter** — two-phase prompts that assign separate roles but omit an explicit prohibition on the second role re-using the first role's output satisfy C-20's structural form but not its relational guard intent; the assessor must be chartered to address a different dimension, not merely to produce a different section.
```
