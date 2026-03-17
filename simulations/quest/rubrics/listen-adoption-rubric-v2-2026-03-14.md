Written to `simulations/quest/rubrics/listen-adoption-rubric-v2-2026-03-14.md`.

---

**What changed from v1:**

Two new aspirational criteria extracted from R1 excellence signals:

**C-11 — Named inertia per archetype** (5 pts, from V-04)
V-04's laggard-first/inertia framing sharpened C-03, C-04, *and* C-05 simultaneously — not by adding a new section but by naming specific status-quo friction per archetype. This is distinct from C-03 (chasm bridging) because it operates pre-chasm, one archetype at a time. Pass requires feature-specific inertia for >=3 archetypes; generic "may resist change" fails.

**C-12 — No orphan or conditional sections** (5 pts, from V-05)
V-05 scored 100 entirely because GATE checkpoints made every section mandatory. V-01 leaked 2 pts on C-09 from a single "if confident" qualifier. C-12 generalises the pattern to the *output* level: if all 10 criterion-mapped sections are present and unconditional, C-12 passes regardless of which prompt variation produced the output.

**Max composite**: 100 → 110. Golden threshold (80) unchanged.
| Output contains a mapping table or list covering all 16 named roles; each role maps to exactly one of the five canonical archetype labels; no role is omitted or duplicated. |
| C-02 | correctness | essential (12) | **Month-by-month adoption sequence** -- output includes a timeline (>=3 months) showing which archetypes / roles adopt in each period, with explicit ordering (who tries first, who follows). | At least 3 distinct time steps are present; innovators and early-adopters appear before early-majority; late-majority before laggards; no inversion of Rogers sequence. |
| C-03 | correctness | essential (12) | **Chasm identification** -- output explicitly names the chasm between early-adopters and early-majority and states what bridging mechanism (or gap risk) applies to this feature. | The word "chasm" (or equivalent: "crossing the chasm", "adoption gap") appears; at least one concrete bridging mechanism or gap risk is stated, tied to this feature's specifics rather than generic advice. |
| C-04 | coverage | essential (12) | **Intervention recommendations ranked by adoption delta** -- output provides >=2 ranked interventions with an estimated adoption delta (quantified or directional: high/medium/low). | At least 2 interventions listed; each has a stated adoption delta (numeric % or H/M/L label); list is in descending delta order or explicitly marked as ranked. |
| C-05 | correctness | essential (12) | **Champion network named** -- output identifies which roles/archetypes form the champion network (the social bridge across the chasm). | At least 2 specific roles or archetype groups are named as champions; the rationale connects their archetype position to why they can bridge into early-majority. |

---

### Recommended (raise quality)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-06 | depth | recommended (10) | **Churn risk per archetype** -- output identifies churn risk for at least 2 archetypes, explaining what triggers churn for each. | Churn risks stated for >=2 archetypes; each risk entry names a trigger (not just "may churn") and at least one mitigation or warning signal. |
| C-07 | depth | recommended (10) | **Spread mechanism named per transition** -- for each archetype-to-archetype adoption transition, the output states the spread mechanism (word-of-mouth, demo, mandate, tooling integration, etc.). | Each major transition in the timeline is annotated with a spread mechanism label; generic "word of mouth" alone does not pass -- at least one transition must cite a feature-specific or role-specific mechanism. |
| C-08 | format | recommended (10) | **Tabular or structured month view** -- the month-by-month timeline is presented in a table, numbered list, or clearly structured format (not buried in prose). | Timeline is rendered as a table, structured list, or clearly labeled month headers; a reader can scan to any month and identify adopters without reading surrounding prose. |

---

### Aspirational (raise the bar)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-09 | depth | aspirational (5) | **Sensitivity analysis on chasm width** -- output models at least 2 scenarios (optimistic / pessimistic) for chasm crossing, with different adoption velocities or champion counts. | Two named scenarios present; each scenario states a different adoption trajectory and the lever that changes it; a reader can compare the two to understand which factors most affect chasm width. |
| C-10 | correctness | aspirational (5) | **Feedback loop into signal readiness** -- output concludes with an explicit statement of what adoption signals would indicate readiness to proceed (or not proceed) with the feature. | At least 2 measurable adoption signals stated (e.g., ">=3 early-majority teams active after month 2"); signals are concrete enough to track in a real team context. |
| C-11 | depth | aspirational (5) | **Named inertia per archetype** -- output identifies the specific status-quo friction that each archetype must overcome, not generic "resistance to change." Distinct from C-03 bridging: inertia is per-archetype, not just at the chasm. | At least 3 archetypes have a named, feature-specific inertia statement (e.g., "early-majority: existing script library satisfies 80% of use cases today" not "may resist new tooling"); generic labels fail. |
| C-12 | format | aspirational (5) | **No orphan or conditional sections** -- every criterion-mapped section is present and unconditional; no section is qualified with "if applicable," "if confident," "optional," or an equivalent hedge. | All 10 criteria (C-01 through C-10) have a corresponding output section that is explicitly present; output contains no conditional hedges on section inclusion; evaluator can locate evidence for each criterion without searching prose. |

---

## Scoring Reference

| Outcome | Example composite |
|---------|-------------------|
| Perfect | All 5 essential + all 3 recommended + all 4 aspirational = 110 |
| Golden | All 5 essential pass + composite >= 80 (e.g., 60 + 30 + 0 = 90) |
| Pass | All 5 essential pass + 2/3 recommended = 60 + 20 = 80 |
| Near-miss | All essential pass + 1/3 recommended = 60 + 10 = 70 (below threshold) |
| Fail | Any essential fails = automatic fail regardless of composite |

---

## Notes for Evaluators

- **C-01**: "Stock roles" means the 16 named personas in the skill contract. If the output uses generic archetype labels without mapping specific roles, C-01 fails.
- **C-03**: Bridging mechanism must be feature-specific. Saying "find champions" without connecting to this feature's adoption context does not pass.
- **C-04**: "Adoption delta" may be stated as % increase in adoption rate or as H/M/L if the output explains what H/M/L means in context. Unranked lists fail C-04.
- **C-09**: Scenarios must differ on a named lever (not just "things go well / badly").
- **C-11**: Inertia is per-archetype and pre-chasm, not the same as C-03's chasm bridging mechanism. A good C-11 names what each archetype is already doing that the feature must displace. If the output only names chasm-level friction (one statement for the EA->EM gap), C-11 fails even if C-03 passes.
- **C-12**: Phrases that fail C-12: "if you have enough data, include sensitivity analysis," "optional: signal readiness section," "Step 7 (if confident)." An output that structurally includes every section -- even briefly -- passes C-12. An output that omits any criterion-mapped section or marks it optional fails.

---

## R1 Excellence Signals (source for C-11, C-12)

**C-11 source -- V-04 inertia framing**: The inertia-first variation named status-quo friction per archetype before discussing adoption. Scorecard noted this "forces bridging to explicitly fight named status-quo friction; improves C-03 specificity." The pattern generalised: any output that names archetype-level inertia produces sharper interventions (C-04) and more grounded champion rationale (C-05), even without the inertia-first prompt structure.

**C-12 source -- V-05 GATE checkpoint pattern**: V-05 scored 100/100 by mapping every rubric criterion to a mandatory, named output section with no conditional qualifiers. Scorecard noted: "GATE checkpoint pattern eliminates orphan criteria." V-01 lost 2 pts on C-09 because its Step 7 was qualified "if confident -- model can skip." C-12 rewards outputs that structurally include all sections unconditionally, regardless of prompt design.
