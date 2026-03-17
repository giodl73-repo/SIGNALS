Rubric written to `simulations/quest/rubrics/listen-adoption-rubric-2026-03-14.md`.

**Structure:**

**Essential (5) — 60 pts**
- C-01: Rogers archetype mapping — all 16 stock roles assigned to one of 5 archetypes
- C-02: Month-by-month sequence — >=3 time steps, Rogers order preserved
- C-03: Chasm identification — named + feature-specific bridging mechanism
- C-04: Interventions ranked by adoption delta — >=2, each with H/M/L or % delta
- C-05: Champion network — >=2 roles named with archetype-based rationale

**Recommended (3) — 30 pts**
- C-06: Churn risk per archetype — trigger + mitigation for >=2 archetypes
- C-07: Spread mechanism per transition — at least one feature-specific mechanism
- C-08: Structured month view — table or labeled headers, scannable

**Aspirational (2) — 10 pts**
- C-09: Sensitivity analysis — optimistic/pessimistic scenarios with named levers
- C-10: Signal readiness feedback loop — >=2 measurable adoption signals

Golden = all 5 essential pass + composite >= 80.
 / laggard). | Output contains a mapping table or list covering all 16 named roles; each role maps to exactly one of the five canonical archetype labels; no role is omitted or duplicated. |
| C-02 | correctness | essential | **Month-by-month adoption sequence** -- output includes a timeline (>=3 months) showing which archetypes / roles adopt in each period, with explicit ordering (who tries first, who follows). | At least 3 distinct time steps are present; innovators and early-adopters appear before early-majority; late-majority before laggards; no inversion of Rogers sequence. |
| C-03 | correctness | essential | **Chasm identification** -- output explicitly names the chasm between early-adopters and early-majority and states what bridging mechanism (or gap risk) applies to this feature. | The word "chasm" (or equivalent: "crossing the chasm", "adoption gap") appears; at least one concrete bridging mechanism or gap risk is stated, tied to this feature's specifics rather than generic advice. |
| C-04 | coverage    | essential | **Intervention recommendations ranked by adoption delta** -- output provides >=2 ranked interventions with an estimated adoption delta (quantified or directional: high/medium/low). | At least 2 interventions listed; each has a stated adoption delta (numeric % or H/M/L label); list is in descending delta order or explicitly marked as ranked. |
| C-05 | correctness | essential | **Champion network named** -- output identifies which roles/archetypes form the champion network (the social bridge across the chasm). | At least 2 specific roles or archetype groups are named as champions; the rationale connects their archetype position to why they can bridge into early-majority. |

---

### Recommended (raise quality)

| ID   | Category | Weight      | Criterion | Pass Condition |
|------|----------|-------------|-----------|----------------|
| C-06 | depth    | recommended | **Churn risk per archetype** -- output identifies churn risk for at least 2 archetypes, explaining what triggers churn for each. | Churn risks stated for >=2 archetypes; each risk entry names a trigger (not just "may churn") and at least one mitigation or warning signal. |
| C-07 | depth    | recommended | **Spread mechanism named per transition** -- for each archetype-to-archetype adoption transition, the output states the spread mechanism (word-of-mouth, demo, mandate, tooling integration, etc.). | Each major transition in the timeline is annotated with a spread mechanism label; generic "word of mouth" alone does not pass -- at least one transition must cite a feature-specific or role-specific mechanism. |
| C-08 | format   | recommended | **Tabular or structured month view** -- the month-by-month timeline is presented in a table, numbered list, or clearly structured format (not buried in prose). | Timeline is rendered as a table, structured list, or clearly labeled month headers; a reader can scan to any month and identify adopters without reading surrounding prose. |

---

### Aspirational (raise the bar)

| ID   | Category    | Weight       | Criterion | Pass Condition |
|------|-------------|--------------|-----------|----------------|
| C-09 | depth       | aspirational | **Sensitivity analysis on chasm width** -- output models at least 2 scenarios (optimistic / pessimistic) for chasm crossing, with different adoption velocities or champion counts. | Two named scenarios present; each scenario states a different adoption trajectory and the lever that changes it; a reader can compare the two to understand which factors most affect chasm width. |
| C-10 | correctness | aspirational | **Feedback loop into signal readiness** -- output concludes with an explicit statement of what adoption signals would indicate readiness to proceed (or not proceed) with the feature. | At least 2 measurable adoption signals stated (e.g., ">=3 early-majority teams active after month 2"); signals are concrete enough to track in a real team context. |

---

## Scoring Reference

| Outcome   | Example composite |
|-----------|------------------|
| Golden    | All 5 essential pass + C-06, C-07, C-08 pass + one aspirational = 100 |
| Pass      | All 5 essential pass + 2/3 recommended pass = 60 + 20 + 0 = 80 |
| Near-miss | All essential pass + 1/3 recommended = 60 + 10 = 70 (below threshold) |
| Fail      | Any essential fails = automatic fail regardless of composite |

---

## Notes for Evaluators

- **C-01**: "Stock roles" means the 16 named personas in the skill contract. If the output
  uses generic archetype labels without mapping specific roles, C-01 fails.
- **C-03**: Bridging mechanism must be feature-specific. Saying "find champions" without
  connecting to this feature's adoption context does not pass.
- **C-04**: "Adoption delta" may be stated as % increase in adoption rate or as H/M/L if
  the output explains what H/M/L means in context. Unranked lists fail C-04.
- **C-09**: Scenarios must differ on a named lever (not just "things go well / badly").
