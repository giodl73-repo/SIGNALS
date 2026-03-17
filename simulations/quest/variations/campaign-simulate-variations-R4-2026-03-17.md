Written to `simulations/quest/golden/campaign-simulate-variate-R4-2026-03-17.md`.

---

# campaign-simulate -- Round 4 Variations

**Diagnosis**: R3 V-05 is 100/100 on rubric v3. Three judgment surfaces remain that R3 did not mechanize:

1. **Sub-skill scope definition** -- each sub-skill re-reads the raw topic and infers what to traverse (variance risk)
2. **Type column classification** -- free text; no vocabulary constraint (parallel gap to C-14)
3. **Remediation specificity** -- style guidance only; "fix the spec" passes a no-blank-cell check

---

## Axes

**Axis A: Topic Entity Manifest (V-01)** -- Phase 0 produces five typed entity lists (one per sub-skill) before any sub-skill fires. Sub-skills walk the list; they don't re-derive scope from prose. Converts "infer what to trace" into "trace these specific entities." Hypothesis: eliminates interpretation variance, surfaces higher-quality findings per entity, and creates a manifest completeness gate verifiable before execution begins.

**Axis B: Finding Type Pre-Assignment (V-02)** -- Declares a fixed Type vocabulary map per sub-skill (e.g., trace-permissions → [`privilege-escalation`, `missing-denial`, `cross-role-conflict`, `spec-gap`]). Type classification becomes a copy operation from a named set. Parallel to how C-14 closed the System Boundary judgment gap. Hypothesis: surfaces new excellence pattern C-19 in a future rubric -- type vocabulary conformance verifiable by inspection.

**Axis C: Remediation Template Contract (V-03)** -- Every Remediation cell must follow `[VERB] [TARGET] AT [LOCATION] TO [SPEC]` or `INVESTIGATE [question] BEFORE specifying`. "Fix the spec" is a named template violation. The C-17 verification gate explicitly checks template compliance. Hypothesis: converts remediation from a comment into an actionable work item; also surfaces findings that are not yet actionable (research items) as a separate visible category.

---

## Variations

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | Entity Manifest (single-axis) | Scope pre-extraction eliminates interpretation variance; manifest completeness gate is a new pre-execution quality check |
| **V-02** | Type Pre-Assignment (single-axis) | Type vocabulary map closes the Type column judgment gap; conformance is verifiable by inspection (candidate C-19) |
| **V-03** | Remediation Template (single-axis) | Template enforces three-field specificity; surfaces non-actionable findings as research items rather than vague prose |
| **V-04** | Entity Manifest + Type Pre-Assignment | Closes two judgment gaps simultaneously; model allocates attention to finding substance rather than scope and label selection |
| **V-05** | Entity Manifest + Type Pre-Assignment + Remediation Template + full R3 V-05 architecture | Maximum-structure Round 4 variant; every column has a mechanical compliance path; no cell requires model judgment for form compliance |

---

**V-05 column compliance map** (all 10 columns, fully mechanical):

| Column | Mechanical Path |
|--------|----------------|
| F-ID | Sequential counter |
| Sub-Skill | Fixed set of 5 |
| System Boundary | C-14 vocabulary copy |
| Type | New type map copy |
| Spec Location | Named section required (not "the spec") |
| Summary | One sentence (content judgment -- intentionally retained) |
| Severity | 4-value enum |
| Blast Radius | 4-value enum |
| Trace Link | F-ID from brief or "none" (never blank) |
| Remediation | Template action form or research form |
