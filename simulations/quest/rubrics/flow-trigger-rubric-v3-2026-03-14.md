---

# flow-trigger Rubric — v3

**Two new aspirational criteria** extracted from R2 scorecard "Excellence Signals from V-04 and V-05" (signals 3 and 4 — signals 1 and 2 were already C-10/C-11 in v2):

**C-12 — Registry Summary Code Block** *(format)*
Both 100-scoring variations place a code-fence immediately after the trigger table declaring `M`, `N`, and `Non-firing` as explicit downstream-referenceable variables. Without it, the budget gate (C-10) must guess or implicitly count M from the table — making the C-10/C-11 structural guarantee incomplete. A variation can pass C-11 and still fail C-12 if its budget gate doesn't read from a declared variable.

**C-13 — Per-Automation Calculation Basis** *(depth)*
C-09 checks anti-hedge enforcement and a final budget number. C-13 checks whether the arithmetic is shown per-automation (`Flow A calls N Dataverse actions + M connector actions = X requests`). Aggregate totals are assertions; per-automation breakdowns are verifiable. V-02 introduced the template; V-04/V-05 made it a structural requirement with "Show calculation basis."

**Scoring formula update**: aspirational denominator changes from `/4` to `/6`; max aspirational contribution stays at 10 points; composite ceiling unchanged at 100. Step size per criterion: 2.5 → ~1.67.
| depth | Each trigger has at least one concrete input and one concrete output |
| C-04 | **Pathology Detection** | coverage | All three pathology types addressed — flagged with evidence or confirmed absent |

## Recommended Criteria (30%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Side Effects** | depth | At least one side effect per trigger that has one; clean triggers noted |
| C-06 | **Condition Evaluation** | correctness | Gate conditions stated per trigger; "always fires" claims justified |
| C-07 | **Scenario Boundary** | format | Triggering change unambiguous; environment/solution layer named |

## Aspirational Criteria (10%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Remediation Recommendations** | behavior | Every flagged pathology has an actionable remediation referencing specific PA/Copilot Studio constructs |
| C-09 | **Trigger Storm Quantification** | depth | Storm depth as a number or range; budget impact in PP request limits or run duration; hedged estimates fail |
| C-10 | **Proactive Budget Gate** *(new — R1 V-05)* | behavior | Budget section (storm depth, API requests, platform limit, budget consumed, run duration) present whenever M >= 3 AND any side effect exists — structured as a numbered section before pathology detection; does not wait for a confirmed storm verdict |
| C-11 | **Dual-Population Table** *(new — R1 V-05)* | format | Single unified table with `Fires? YES/NO` per row, including explicit per-row enforcement rule ("YES or NO only — no row may omit this column"); separate registered/firing lists do not satisfy this criterion |
| C-12 | **Registry Summary Code Block** *(new — R2 V-04/V-05)* | format | A structured code-fence or fixed-format block immediately following the trigger table declares M (firing triggers with side effects), N (all firing triggers), and Non-firing counts as explicit downstream-referenceable variables; implicit counts derived by row-counting the table do not satisfy this criterion |
| C-13 | **Per-Automation Calculation Basis** *(new — R2 V-04/V-05)* | depth | Budget section includes per-automation arithmetic showing additive action count components (e.g., "Flow A calls N Dataverse actions + M connector actions = X requests per invocation"); aggregate totals without per-automation intermediate arithmetic do not satisfy this criterion |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 4 essential pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Output is trustworthy and production-useful |
| Silver | 60-79 or 1 essential miss | Useful but requires human verification |
| Bronze | 40-59 | Partial signal; major gaps present |
| Fail | < 40 or 2+ essential miss | Not usable; regenerate |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10 (Proactive Budget Gate) and C-11 (Dual-Population Table) from R1 V-05 excellence signals; aspirational pool expanded from 2 to 4; scoring denominator updated |
| v3 | 2026-03-14 | Added C-12 (Registry Summary Code Block) and C-13 (Per-Automation Calculation Basis) from R2 V-04/V-05 excellence signals 3 and 4; aspirational pool expanded from 4 to 6; scoring denominator updated |

---

**Key changes from v2:**

- **C-12** captures the registry summary code block pattern from V-04 and V-05. Both 100-scoring variations place a structured code-fence immediately after the dual-population table declaring M, N, and Non-firing counts as explicit values. This creates downstream-referenceable variables that the budget gate section (C-10) reads from — preventing M from being implicit or inconsistently derived. Without C-12, a variation can satisfy C-11 (table present) but still produce a budget gate that guesses M rather than reads it from a declared value.

- **C-13** captures the per-automation calculation basis pattern from V-02, V-04, and V-05. C-09 requires anti-hedge enforcement ("unknown is not acceptable") and a final budget number. C-13 goes further: the budget section must show the additive arithmetic per automation, not just the aggregate. This converts C-09 from a structural presence check into a content quality check — intermediate arithmetic is verifiable; asserted totals are not. V-04/V-05 both require "Show calculation basis" with per-automation component breakdown.

- **Scoring denominator** for aspirational updated from `/4` to `/6`; aspirational max contribution stays at 10 points, so the composite ceiling is unchanged at 100. Step size per aspirational criterion changes from 2.5 to ~1.67.
