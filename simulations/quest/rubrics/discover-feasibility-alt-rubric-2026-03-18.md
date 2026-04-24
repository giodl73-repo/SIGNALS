Written to `simulations/quest/rubrics/discover-feasibility-alt-rubric-2026-03-18.md`.

**Summary of the rubric:**

- **5 essential** (C-01 through C-05): INFERENCE GATE fields, VERDICT score/label consistency, ARCHITECT traffic-light + RED Blockers, 4 inertia surfaces, focus woven not appended. All confirmed stable at 100.0 through R7 of the prior session.
- **3 recommended** (C-06 through C-08): Amendment traceability, focus influence on base analysis, STRATEGY BUILD-VS-BUY coverage. Also confirmed stable.
- **2 aspirational** (C-09, C-10): Focus propagation to 2+ downstream sections (confirmed in R7), STRATEGY-before-ARCHITECT structural guarantee (promoted from R7 excellence signals, pending empirical validation this session).

**Scoring**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`. Golden = all 5 essential PASS (no PARTIAL) + composite >= 80.
excellence signals and is pending empirical validation in this session.

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | INFERENCE GATE has all required fields | completeness | essential | Feature, Team, and Timeline are all present and non-empty in the INFERENCE GATE section before any analysis begins. Focus is optional; its absence does not fail C-01. |
| C-02 | VERDICT has score + label consistent with range, prerequisites iff FEASIBLE WITH CAVEATS + RED | correctness | essential | VERDICT contains a numeric score (0-100) and a label (NOT FEASIBLE, FEASIBLE WITH CAVEATS, or FEASIBLE) both present. Label is consistent with score range: <50 = NOT FEASIBLE, 50-74 = FEASIBLE WITH CAVEATS, >=75 = FEASIBLE. Prerequisites listed iff label is FEASIBLE WITH CAVEATS and at least one RED component exists. |
| C-03 | ARCHITECT table has traffic-light ratings with RED Blockers | correctness | essential | Every component row in the ARCHITECT table carries GREEN, YELLOW, or RED. Every RED-rated component has a corresponding RED Blockers entry with all three sub-fields: blocker statement, Lift condition, and Do-nothing cost. "No RED components." is acceptable iff no RED rows exist. |
| C-04 | Inertia surfaces in all four required locations | coverage | essential | All four inertia surfaces present: (1) INERTIA: STATUS QUO section with Baseline sentence, (2) Do-nothing cost column in ARCHITECT table with a value on every row, (3) "Not building this means:" line in VERDICT, (4) "Inertia saved:" line on every amendment in AMENDMENTS. Any surface omitted fails this criterion. |
| C-05 | When focus is active, focus content is woven into existing sections | behavior | essential | If a focus value is provided (compliance, stakeholders, requirements, naming, size, or other), the focus-specific content appears integrated within the relevant existing sections -- not appended as a new standalone section after AMENDMENTS. Fails if focus content is additive-only (appended block). Passes automatically (N/A) if no focus is active. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | AMENDMENTS are traceable to RED or YELLOW components | depth | recommended | Every amendment names the specific component it addresses, states the color transition, and includes a score-delta estimate. Amendments not tied to a rated component, or missing the color transition, fail this criterion. |
| C-07 | Focus integration visibly influences the base analysis | depth | recommended | When focus is active, the focus content demonstrably changes the base analysis -- not just accompanies it. Passes automatically (N/A) if no focus is active. |
| C-08 | STRATEGY: BUILD-VS-BUY covers at least half of components | coverage | recommended | At least 50% of the components listed in the ARCHITECT table carry an explicit Build / Buy / Use existing recommendation in the STRATEGY section. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | Focus constraint propagates to 2+ downstream sections | coverage | aspirational | When focus is active, the focus-introduced constraint must appear in at least two distinct downstream sections (e.g., ARCHITECT, INERTIA, VERDICT, AMENDMENTS). Presence in only one section fails C-09. Passes N/A if no focus is active. |
| C-10 | STRATEGY section precedes ARCHITECT table to structurally guarantee C-08 coverage | behavior | aspirational | The STRATEGY section appears before the ARCHITECT table in the output, converting C-08 from an output-checked instruction into a by-construction property -- every ARCHITECT component row has a prior STRATEGY entry because STRATEGY was already written at evaluation time. A response where ARCHITECT precedes STRATEGY fails C-10 even if C-08 passes independently. Passes N/A if the output contains no STRATEGY section. |

---

## Scoring

```
Composite = (essential_pass    / 5  * 60)
          + (recommended_pass  / 3  * 30)
          + (aspirational_pass / 2  * 10)
```

PARTIAL scores count as 0.5 for the formula. PARTIAL on any essential criterion fails the Golden threshold regardless of composite score.

**Golden threshold**: all 5 essential criteria pass (no PARTIALs) AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential (no PARTIAL) + >= 80 | Ship-ready; alt version validates the unified hypothesis |
| Passing | all essential (PARTIAL allowed) + 60-79 | Usable, recommended gaps noted |
| Failing | any essential fails or PARTIAL | Not useful as a feasibility artifact |

---

## Evaluation Notes

- **C-05 is the diagnostic criterion for the A/B test**: the entire point of the alt version is that focus is woven in, not appended. Score C-05 strictly -- a new section added after AMENDMENTS is a structural failure even if the content is correct.
- **C-07 and C-05 are complementary**: C-05 checks structure (where focus content lives), C-07 checks effect (whether it changed the analysis). An output can pass C-05 (focus is woven in) but fail C-07 (the base sections are unchanged). The alt version wins the A/B test only if both pass.
- **C-04 partial pattern**: the Do-nothing cost column in the ARCHITECT table is the most frequently omitted inertia surface. Score each row independently -- one blank cell in a multi-row table is a PARTIAL.
- **C-09 is a propagation test, not a presence test**: identify the constraint introduced by focus, then trace it forward. If it does not recur in a second section, score FAIL.
- **C-10 is a section-ordering test**: verify STRATEGY section heading appears before ARCHITECT section heading. A correct ARCHITECT table that happens to precede STRATEGY still fails C-10. Do not infer ordering from content quality.
- **N/A handling**: C-05, C-07, and C-09 pass as N/A when no focus is active. C-10 passes N/A if the output contains no STRATEGY section.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-18 | New session. Carries forward C-01 through C-08 (all confirmed PASS 100.0 in 2026-03-17 R7). Aspirational pool trimmed to C-09 (confirmed) + C-10 (STRATEGY-before-ARCHITECT, from R7 excellence signals; pending empirical validation). Aspirational denominator /2. |
