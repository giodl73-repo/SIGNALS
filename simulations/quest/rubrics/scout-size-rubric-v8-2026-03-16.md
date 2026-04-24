Reading the R7 scorecard carefully. Two distinct patterns emerge:

1. **V-03 passes C-20 but the caveat flags a new frontier** — role-separated production solves the basis/gap conflation, but "role-switching overhead may create new failure modes... if role boundaries introduce ambiguity about which role owns other fields." The fix for C-20 applies only to the constrained pair; every other field is implicitly unassigned. A two-phase design that separates only the relational pair while leaving remaining fields unchartered creates ownership gaps that can produce drift in either phase.

2. **The Phase 2 non-access clause names a structural property, not a content category** — C-20's passing condition requires "an explicit non-overlap charter stated in the second role's instructions." The caveat implies a stronger form: a charter that prohibits re-using "what the analyst confirmed" in the abstract is weaker than one that names the specific confirmed content category (e.g., "do not cite the API contract as your gap if the Sizing Analyst confirmed it"). A named prohibition is falsifiable at the role level without cross-referencing the basis output; a structural rule requires that cross-reference to detect violation.

---

```markdown
# Scout-Size Rubric — v8

**Skill**: scout-size
**Version**: v8 (updated from v7 — added C-23, C-24 from R7 excellence signals)
**Date**: 2026-03-16

---

## Purpose

This rubric scores the output of the `scout-size` skill against 24 criteria grouped
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
| C-21 | **Inline failure examples provide both WRONG and CORRECT instances** | depth | C-17 requires inline failure examples adjacent to the constrained field. A complete failure example includes both a named WRONG instance (showing the specific violation and why it fails) and a CORRECT instance (showing what passes). A CORRECT-only example reinforces the success pattern but does not activate failure detection — the model cannot recognize its own drift by comparing against success alone. A WRONG-only example names the error but leaves no exit path toward compliance. An abstract structural pattern — e.g., "if your gap says 'X is not confirmed' and the basis says 'X is established,' you have violated your charter" — partially satisfies C-17 by naming the shape of the failure but fails C-21 because it substitutes a schema description for a concrete named instance. A prompt passes C-21 when every C-17-scoped failure example supplies both a concrete named WRONG instance and a concrete named CORRECT instance in the same inline block. |
| C-22 | **Relational constraints are co-encoded in the dependent field's definition** | depth | When a constraint governs a relationship between two fields — e.g., "the destination tier must differ from the currently assigned tier," or "the gap must address a different dimension than the basis" — the constraint belongs in the dependent field's column header or field label, not in a separate rules section or prose bullet. Encoding the relational rule in the dependent field means the constraint is active at the moment the model produces that field's value; a prose bullet in a rules section can be bypassed if the model fills the field before consulting the rules. A column header like "Destination Tier [must differ from current tier: fill with LOW / MEDIUM / HIGH / XL]" satisfies both C-13 (value format) and C-16 (relational rule) at the point of production. A prompt passes C-22 when every field-to-field relational constraint — at minimum, the sensitivity destination tier (C-16) and the confidence gap (C-15) — is co-encoded in the dependent field's label or definition rather than stated only in a separate rules section. |
| C-23 | **Role charters assign explicit ownership of all output fields, not just the constrained pair** | depth | When role-separated production (C-20) is used to govern the basis/gap pair, the role charters must also specify which role produces every remaining output field. A design that separates only the constrained pair while leaving other fields unassigned creates implicit ownership: each phase may fill unchartered fields opportunistically, or leave them to the other phase, generating either duplication or gaps. Role-switching overhead is justified only if charter coverage eliminates, rather than introduces, ownership ambiguity. A prompt passes C-23 when every output field appears in exactly one role's charter as a named production responsibility, and the other role's charter explicitly excludes it or is silent by design through an enumerated field list — not by omission. |
| C-24 | **Phase 2 non-access clause names the prohibited content category, not only the structural property** | depth | In two-phase designs (C-20), the Phase 2 role's non-overlap charter is stronger when it names the specific category of Phase 1 confirmed content that is prohibited from the gap — e.g., "do not cite the API contract status as your gap if the Sizing Analyst confirmed it in Phase 1" — rather than stating only the structural property it enforces ("address a different dimension"). A named prohibition is falsifiable at the role level: a reader can check the Phase 2 output against the named prohibited category without cross-referencing Phase 1. A structural-property-only prohibition requires that cross-reference and allows a model to comply with the letter of the charter while violating its intent if it frames a negation of Phase 1 content as a "different dimension." A prompt passes C-24 when the Phase 2 charter's non-access clause names the content category it prohibits — at minimum, the class of items the Sizing Analyst is expected to confirm — not only the relational rule. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Patterns to Watch (v8 additions in bold)

- **Plan creep** — violates C-05. Most likely failure mode.
- **Role boundary drift** — violates C-23. Two-phase designs that separate the constrained pair but leave other fields unchartered allow each phase to fill unassigned fields opportunistically. Explicit field enumeration per role is the fix.
- **Structural-property non-access** — violates C-24. A Phase 2 charter that prohibits re-using "what was confirmed" in the abstract still requires cross-referencing Phase 1 output to detect violations. Naming the prohibited content category makes the charter self-contained and the violation observable without cross-reference.
```
