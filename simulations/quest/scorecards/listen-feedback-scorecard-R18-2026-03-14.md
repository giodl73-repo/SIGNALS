# listen-feedback Round 18 Scorecard — Rubric v16

## Scoring Structure

| Tier | Criteria | Pts Each | Max |
|------|----------|----------|-----|
| Essential (C-01–C-05) | 5 | 15 | 75 |
| Recommended (R-01–R-03) | 3 | 5 | 15 |
| Aspirational (A-01–A-29) | 29 | 5 | 145 |
| **Total** | | | **235** |

---

## Essential Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | 12 persona cards present | PASS | PASS | PASS | PASS | PASS |
| C-02 | NPS score + justification per card | PASS | PASS | PASS | PASS | PASS |
| C-03 | Severity-labeled feedback per card | PASS | PASS | PASS | PASS | PASS |
| C-04 | Aggregate NPS computed + threshold applied | PASS | PASS | PASS | PASS | PASS |
| C-05 | Cross-persona theme matrix present | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 75/75 — all variations.** No variation modifies the baseline persona card, aggregate, or theme matrix protocol.

---

## Recommended Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| R-01 | Blocking issues escalated | PASS | PASS | PASS | PASS | PASS |
| R-02 | PM and UX roles included | PASS | PASS | PASS | PASS | PASS |
| R-03 | Theme matrix severity annotation | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 15/15 — all variations.**

---

## Aspirational Criteria — A-01 through A-26

All baseline criteria preserved from R17. No variation removes, conflicts with, or weakens any prior aspirational criterion. Group-pass notation:

| Range | Score | Evidence |
|-------|-------|----------|
| A-01–A-26 (26 criteria) | PASS × 26 = 130 pts | Baseline preserved; variation changes are additive only |

---

## Differentiating Criteria — A-27, A-28, A-29

### A-27 — Failure Mode Annotation

Pass condition: the protocol names the failure mode prevented by each structural constraint.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **PARTIAL** (3 pts) | Baseline A-27 application satisfied for other constraints; the new CI formula requirement is stated as a structural two-part format rule but the failure mode for omitting the formula is not named. The constraint is verifiable but its rationale is not present. |
| V-02 | **PARTIAL** (3 pts) | Template gap is a visible enforcement mechanism but carries no failure mode annotation. A reader filling the template cannot distinguish "why is the parenthetical required" from "this is optional commentary." |
| V-03 | **PARTIAL** (3 pts) | Derivation phase makes formula structurally prior (D.1 precedes D.4) but the phase instructions do not name the failure mode prevented by requiring D.1. Phase enforcement is mechanical, not epistemic. |
| V-04 | **PARTIAL** (3 pts) | Dual enforcement (V-01 format + V-03 derivation) plus aggregate manifest extension to A6. Positional verifiability ("count to 9 for cards, A6 for aggregate") is noted, but the CI formula requirement has no failure mode annotation. A-27 is satisfied at the structural level, not the epistemic level. |
| V-05 | **PASS** (5 pts) | Step S.1 explicitly names the failure mode: *"Without the formula parenthetical (±1.96·[SD_value]/√12) alongside the interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method."* This is the A-27 pass condition: structural constraint plus named failure mode. Directly parallel to A-25 (UX-before-PM with epistemic rationale). |

---

### A-28 — Directional Sensitivity Separation

| Variation | Score | Evidence |
|-----------|-------|----------|
| All (V-01–V-05) | **PASS** (5 pts) | Baseline preserved; no variation modifies sensitivity analysis structure. |

---

### A-29 — CI/Variance Annotation Includes Computation Formula

Pass condition: CI annotation explicitly states the computation formula alongside the numeric value.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **PASS** (5 pts) | Two-part labeled structure (`**Formula:** 95% CI = mean ± 1.96·(SD/√12)` + `**Computed:** SD = [X.XX]; 95% CI [lower, upper] (±1.96·[SD_value]/√12)`) makes omission of the formula line structurally detectable: a single-line CI output is visibly incomplete. Strong single-mechanism enforcement. |
| V-02 | **PARTIAL** (3 pts) | Template gap approach (`95% CI [[lower], [upper]] (±1.96·[SD_value]/√12)`) relies on the evaluator reading the parenthetical `[SD_value]` as a required fill-in rather than optional annotation. The "Required output format" instruction clarifies intent but a `> ` blockquote is advisory, not structurally mandatory. An evaluator satisficing on the format could produce `95% CI [6.2, 7.8]` and misread the template note as supplementary guidance. Weakest enforcement mechanism of the five. |
| V-03 | **PASS** (5 pts) | Derivation phase makes formula the required *input* to the CI, not a format decoration on the output. D.1 (state formula) must be completed before D.2 (compute SD), D.3 (apply), D.4 (report). Phase exit without D.1 is structurally blocked. Process-level enforcement is more fundamental than output-format enforcement: the formula is required at generation time, not only at output-inspection time. |
| V-04 | **PASS** (5 pts) | Dual enforcement: V-01 format structure (output-level) and V-03 derivation phase (process-level) are independent. Compliance is verifiable at two levels without cross-reference. Aggregate manifest explicitly extends to A6 (statistical spread as a numbered aggregate field), making the formula requirement positionally verifiable in three places: per-card count (9 fields), aggregate count (6 fields), CI block line count (2 lines). |
| V-05 | **PASS** (5 pts) | V-03 derivation phase (mechanical enforcement) plus failure mode annotation (epistemic grounding). The formula is required by phase structure AND its omission's consequence is named. This is the deepest enforcement: the evaluator cannot omit the formula without both violating a phase exit condition and suppressing a named failure mode explanation. |

---

## Composite Scores

| Variation | Essential | Recommended | A-01–A-26 | A-27 | A-28 | A-29 | **Total** |
|-----------|-----------|-------------|-----------|------|------|------|-----------|
| V-01 | 75 | 15 | 130 | 3 | 5 | 5 | **233** |
| V-02 | 75 | 15 | 130 | 3 | 5 | 3 | **231** |
| V-03 | 75 | 15 | 130 | 3 | 5 | 5 | **233** |
| V-04 | 75 | 15 | 130 | 3 | 5 | 5 | **233** |
| V-05 | 75 | 15 | 130 | 5 | 5 | 5 | **235** |

---

## Ranking

| Rank | Variation | Score | Key Differentiator |
|------|-----------|-------|--------------------|
| 1 | **V-05** | 235/235 | Only variation to fully pass A-27 by naming the CI failure mode; derivation phase + epistemic rationale closes both gaps simultaneously |
| 2 | **V-04** | 233/235 | Strongest structural enforcement (dual mechanism + A6 aggregate extension); A-27 partial because CI failure mode not named |
| 3 | **V-03** | 233/235 | Process-level enforcement (formula structurally required as phase input); stronger than format-only but A-27 partial |
| 4 | **V-01** | 233/235 | Clean output-format enforcement; detectable by line count but single mechanism, no phase-level guarantee |
| 5 | **V-02** | 231/235 | Template mechanism is advisory, not structural; weakest A-29 enforcement of the round |

*Tiebreak within 233-group: V-04 > V-03 > V-01 by enforcement depth (dual > process > format).*

---

## Excellence Signals from V-05

**Signal 1: Failure mode annotation applied to the new criterion at introduction.**
V-05 applies A-27's failure mode annotation mechanism directly to A-29, following the exact pattern that generated A-25 (UX-before-PM with epistemic rationale). Both A-25 and V-05's A-29 treatment name the failure mode prevented by the constraint: *"PM framing would anchor UX reading"* (A-25) and *"a reader cannot confirm whether ±1.96·SD/√12 or a different method was used"* (V-05). The pattern is: new structural constraints gain durable enforcement when their failure mode is named at introduction, converting arbitrary format rules into principled requirements.

**Signal 2: Dual closure — structural gap and explanation gap addressed simultaneously.**
V-03 closes the structural gap (phase cannot exit without formula). V-05 closes both: the derivation phase closes the structural gap, and the failure mode annotation closes the explanation gap. A criterion that can be omitted for process reasons AND understood to be skippable for epistemic reasons requires both closures to be maximally robust. V-04 achieves dual structural closure (two enforcement mechanisms); V-05 achieves structural closure plus epistemic closure. These are different dimensions of robustness.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["failure mode annotation applied to the new criterion at introduction: naming why a bare CI is unauditable converts A-29 from an arbitrary format constraint to a principled requirement, following the A-25 epistemic rationale pattern — every new structural constraint should arrive with its failure mode named", "dual closure targets two independent omission vectors simultaneously: V-05's derivation phase closes the structural gap (formula required as phase input) while the failure mode annotation closes the explanation gap (evaluator understands why omission matters), making the criterion robust to both mechanical oversight and principled skipping"]}
```
