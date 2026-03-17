Here is the complete updated rubric:

---

# flow-trigger Rubric — v2

**Skill**: `flow:trigger`
**Version**: v2 (updated from R1 scorecard — 2026-03-14)
**Changelog**: Added C-10 (Proactive Budget Gate) and C-11 (Dual-Population Table) from V-05 excellence signals.

---

## Structure

- **4 Essential (C-01–C-04):** trigger enumeration, firing order with sync/async, inputs/outputs per trigger, and explicit pathology detection (storm / missing / circular)
- **3 Recommended (C-05–C-07):** side effects, condition evaluation gates, scenario boundary declaration
- **4 Aspirational (C-08–C-11):** remediation recommendations per pathology, trigger storm quantification, proactive budget gate, dual-population table

**Scoring:** `(essential/4 * 60) + (recommended/3 * 30) + (aspirational/4 * 10)` — golden at all essential pass + composite >= 80.

---

## Essential Criteria (60% of composite score)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Trigger Enumeration** | coverage | Every trigger that fires is present; no firing trigger omitted |
| C-02 | **Firing Order** | correctness | Numbered sequence provided; sync/async explicit per trigger |
| C-03 | **Inputs and Outputs** | depth | Each trigger has at least one concrete input and one concrete output |
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
| C-10 | **Proactive Budget Gate** *(new — V-05)* | behavior | Budget section (storm depth, API requests, platform limit, budget consumed, run duration) present whenever M >= 3 AND any side effect exists — does not wait for a confirmed storm verdict |
| C-11 | **Dual-Population Table** *(new — V-05)* | format | Single unified table with `Fires? YES/NO` per row; separate registered/firing lists do not satisfy this criterion |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 4 essential pass AND composite >= 80.

---

**Key changes from v1:**

- **C-10** captures V-05's proactive-budget-trigger pattern. V-01–V-04 all failed C-09 because they waited for a confirmed storm — C-10 closes that gap structurally by tying the budget gate to `M >= 3 AND side_effect_exists`.
- **C-11** captures V-05's dual-population-table pattern. All single-axis variations used separate registered/firing lists, which left enumeration completeness partially model-dependent. A single table with a `Fires?` column makes omission structurally harder.
- **Scoring denominator** for aspirational updated from `/2` to `/4`; aspirational max contribution stays at 10 points, so the composite ceiling is unchanged at 100.
flagged pathology has at least one actionable remediation; remediations reference specific Power Automate / Copilot Studio constructs |
| C-09 | **Trigger Storm Quantification** — If a trigger storm is present or at risk, the depth of the cascade is estimated (how many triggers fire in sequence, approximate execution budget consumed) | depth | Storm depth is expressed as a number or bounded range; budget impact is framed in terms of Power Platform request limits or run duration; hedged or omitted estimates do not pass |
| C-10 | **Proactive Budget Gate** — Budget analysis is triggered proactively when cascade depth M >= 3 AND any side effect exists, regardless of whether a confirmed storm has been declared; the output does not wait for an explicit storm verdict to produce budget estimates | behavior | A budget section (storm depth, API requests, platform limit, budget consumed, run duration) is present whenever M >= 3 and at least one side effect is identified; absence of a confirmed storm verdict is not a valid reason to omit the section |
| C-11 | **Dual-Population Table** — A single enumeration table covers both registered-but-not-firing and firing triggers using a Fires? YES/NO column, preventing the inconsistent registry/firing split where models may enumerate only firing triggers and omit non-firing ones | format | One unified table is present with an explicit fires/does-not-fire distinction per row; separate enumeration lists for registered vs. firing triggers do not satisfy this criterion |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

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
| v1 | 2026-03-14 | Initial rubric -- 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10 (Proactive Budget Gate) and C-11 (Dual-Population Table) from R1 V-05 excellence signals; aspirational pool expanded from 2 to 4; scoring denominator updated |
