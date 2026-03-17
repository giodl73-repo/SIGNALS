Reading the two patterns from the JSON:

1. **constraint-completeness-seal** — C-19 (uniform register) + C-20 (systematic gates) together produce a closed constraint system. The compound property is not testable by either criterion individually: you must verify that every typed binding has a MUST/FORBIDDEN governing it in the consuming phase.

2. **pre-print skeleton** — a filled-in output template with named placeholder slots keyed to gate variables constrains output *shape*, not just output *content*. No current criterion captures this.

These become C-21 and C-22. Formula denominator moves from 12 to 14.

---

```markdown
---
skill: quest-rubric
skill_target: org-build
date: 2026-03-16
version: 5
---

# Scoring Rubric — org-build

## Essential Criteria (5)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-01** | org-chart.md present with ASCII hierarchy | correctness | File exists and contains an ASCII box/line diagram with min 2 org levels. Flat name list fails. |
| **C-02** | All five role fields present in every .craft/roles/ file | correctness | Every role file contains `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Any missing field fails. |
| **C-03** | inertia-advocate role always present | correctness | A role file with `inertia` or `advocate` in name/title exists under `.craft/roles/`. Absence fails unconditionally. |
| **C-04** | Role count within depth range | coverage | Standard: 20-30 files. Deep: 50+. Below lower bound fails. Exceeding upper bound by >20% without deep flag also fails. |
| **C-05** | Headcount by area table present | format | org-chart.md has table with `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates` columns. Table without Decides/Escalates fails. |

## Recommended Criteria (3)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-06** | Role files grouped by area subdirectories | format | `.craft/roles/` has min 2 area subdirs. All roles flat with no grouping fails. |
| **C-07** | Operating rhythm table and committee charters complete | depth | Rhythm table with 3+ distinct rows (ROB + shiproom + governance) AND a charter per governance meeting with all 5 fields including Quorum as `N of M` fraction. |
| **C-08** | Inertia assessment reaches VERDICT with FLAT-CASE-PRESSURE rating | depth | org-chart.md contains `FLAT-CASE-PRESSURE:` with a closed-set rating and a `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` verdict. Generic prose without rated verdict fails. |

## Aspirational Criteria (14)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-09** | Org Evolution Roadmap with typed triggers | depth | 2+ rows: Row 1 is headcount threshold, Row 2 is different category. Two headcount thresholds fails. |
| **C-10** | Anti-Pattern Watch uses cat-N typed citations | correctness | 2+ rows where every "Why It Applies Here" cell opens with `[element name] (cat-N) —` syntax. Plain prose fails. Descriptive format guidance without imperative MUST fails. |
| **C-11** | Phase-gate with cross-artifact coherence: IA scope references FLAT-CASE-PRESSURE rating | depth | inertia-advocate `scope` field is derived from the FLAT-CASE-PRESSURE rating via pre-written templates (one per rating level). Generic scope text not tied to rated verdict fails. |
| **C-12** | Anti-pattern categories derived from structural design choice | depth | Anti-pattern category selection is explicitly tied to the design decision: flat org produces cat-3/cat-2; deep hierarchy produces cat-1/cat-4. Category choices independent of structure fail. |
| **C-13** | Single-verdict guard uses explicit error framing | correctness | C-08 verdict block contains explicit error framing — e.g., "Only one verdict. Both is an error." Permissive phrasing ("choose one", "pick either") fails. |
| **C-14** | Phase gates produce named typed output variables consumed by downstream input contracts | depth | At least one phase gate records a named typed output variable (e.g., T1-VERDICT, T1-PRESSURE) and at least one downstream phase declares an explicit input contract referencing that variable by name. Gate output that is implicit or unnamed fails. Downstream phase with no input contract declaration fails. |
| **C-15** | Verdict guard is bidirectional — "neither" is also an explicit error | correctness | C-08 verdict block explicitly names both failure modes: "Both is an error" AND "Neither is an error." A guard that covers only the "both" direction fails. Symmetric FORBIDDEN framing ("FORBIDDEN: writing both. FORBIDDEN: omitting both.") satisfies this criterion. |
| **C-16** | Anti-pattern Mitigation cells contain remediation actions, not format guidance | correctness | Every Mitigation cell in the Anti-Pattern Watch table contains a specific remediation action. Cells containing descriptive format instructions or column-structure guidance instead of actions fail. |
| **C-17** | IA scope template applied verbatim — paraphrase fails | correctness | The inertia-advocate `scope` field contains the exact text of the applicable rating-keyed template. Paraphrase, adaptation, or any deviation from the template text fails. "Derived, not composed" is necessary but not sufficient; verbatim copy is required. |
| **C-18** | Category exclusion sets are explicitly FORBIDDEN per verdict path | depth | The anti-pattern derivation block states not only which categories are required per verdict but also which are forbidden: CAN-OPERATE-FLAT forbids cat-1/cat-4; STRUCTURE-WARRANTED forbids cat-2/cat-3. Stating the correct path without forbidding the wrong path fails. |
| **C-19** | Imperative register used uniformly across all phase instructions | correctness | Every constraint statement in every phase uses MUST or FORBIDDEN. Advisory language ("should", "prefer", "typically", "consider") in any constraint context fails. C-10 requires MUST in one section; this criterion requires that register across the entire output. |
| **C-20** | All phase gates declare typed outputs and all dependent phases declare input contracts | depth | Every phase gate in the output declares named typed output variables. Every phase that consumes a prior gate's output declares an explicit input contract naming that variable. C-14 requires at least one such pair; this criterion requires systematic coverage. Any gate with implicit or unnamed output fails. Any consuming phase with no input contract declaration fails. |
| **C-21** | Constraint-completeness seal: every typed gate variable is governed by MUST/FORBIDDEN in its consuming phase | depth | For every named typed output variable declared at a phase gate, the downstream input contract that consumes it is governed by MUST or FORBIDDEN — not advisory language. C-19 requires uniform register across all phases; C-20 requires systematic gate coverage; this criterion requires the two properties to intersect: each typed variable binding must be simultaneously named (C-20) and imperatively constrained (C-19). A typed binding consumed with "should reference" or "typically uses" fails. Advisory language anywhere in an input contract that governs a named gate variable fails. |
| **C-22** | Pre-print skeleton with named placeholder slots keyed to gate variables | format | The output contains a filled template skeleton for at least one artifact, showing its shape with explicit named placeholder slots (e.g., `{{T1-VERDICT}}`, `[FLAT-CASE-PRESSURE-RATING]`) that correspond directly to typed output variables declared at phase gates. A typed variable declaration with no corresponding template slot fails. A skeleton with unnamed or untyped slots (e.g., `[VALUE]`, `___`) fails. Template shape must be derivable from gate variable names alone — a reader who knows only the gate outputs must be able to fill in every slot without ambiguity. |

## Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 10)
```
```

---

Two criteria added:

- **C-21** captures the *intersection* of C-19 and C-20 — it fails when a named typed variable exists but its consuming constraint is advisory. Neither parent criterion catches this gap alone.
- **C-22** captures the pre-print skeleton signal — a template with named placeholder slots keyed to gate variables constrains output shape independently of typing or register. A model that satisfies C-20 fully can still fail C-22 if it never renders a filled skeleton.

Formula denominator is now 14; aspirational weight per criterion drops from 0.833 to 0.714 points each.
