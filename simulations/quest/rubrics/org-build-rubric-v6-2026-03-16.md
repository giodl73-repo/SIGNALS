Two new patterns from the scorecard JSON:

- **C-23** — phase-execution-ordering constraint: `FORBIDDEN: beginning a phase before recording all output variables of the preceding phase`
- **C-24** — record-block checkpoint: materialized named record block emitted after each phase gate before the next phase reads it

Denominator moves from 14 to 16.

```markdown
---
skill: quest-rubric
skill_target: org-build
date: 2026-03-16
version: 6
---

# Scoring Rubric — org-build

## Essential Criteria (5)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-01** | org-chart.md present with ASCII hierarchy | correctness | File exists and contains an ASCII box/line diagram with min 2 org levels. Flat name list fails. |
| **C-02** | All five role fields present in every .roles/ file | correctness | Every role file contains `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Any missing field fails. |
| **C-03** | inertia-advocate role always present | correctness | A role file with `inertia` or `advocate` in name/title exists under `.roles/`. Absence fails unconditionally. |
| **C-04** | Role count within depth range | coverage | Standard: 20-30 files. Deep: 50+. Below lower bound fails. Exceeding upper bound by >20% without deep flag also fails. |
| **C-05** | Headcount by area table present | format | org-chart.md has table with `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates` columns. Table without Decides/Escalates fails. |

## Recommended Criteria (3)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-06** | Role files grouped by area subdirectories | format | `.roles/` has min 2 area subdirs. All roles flat with no grouping fails. |
| **C-07** | Operating rhythm table and committee charters complete | depth | Rhythm table with 3+ distinct rows (ROB + shiproom + governance) AND a charter per governance meeting with all 5 fields including Quorum as `N of M` fraction. |
| **C-08** | Inertia assessment reaches VERDICT with FLAT-CASE-PRESSURE rating | depth | org-chart.md contains `FLAT-CASE-PRESSURE:` with a closed-set rating and a `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` verdict. Generic prose without rated verdict fails. |

## Aspirational Criteria (16)

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
| **C-23** | Phase-execution ordering constraint: FORBIDDEN beginning a phase before recording all preceding gate outputs | correctness | Every phase transition includes an explicit prohibition on starting the next phase before all output variables of the current phase have been recorded. Stating output contracts without a temporal ordering guard fails. A blanket "record before proceeding" instruction at the top of the prompt is insufficient — each phase boundary must carry the constraint. This operates at the process level: it governs execution order, not schema content. A prompt that defines correct gate schemas (C-20) but omits the ordering FORBIDDEN at any phase boundary fails this criterion. |
| **C-24** | Record-block checkpoint: named record block materialized after each phase gate | format | After every phase gate, the output contains a named record block — a structured text block that materializes each typed output variable by name and value (e.g., `T2-PRESSURE: ELEVATED`, `T2-VERDICT: STRUCTURE-WARRANTED`) before the next phase begins. A gate variable appearing only in a contract table fails; it must appear as an emitted record block. Record blocks serve as auditable checkpoints: they make gate boundaries observable and expose dangling outputs (variables declared but never emitted). A prompt that defines gate contracts (C-20) and ordering guards (C-23) but never requires materialized record blocks fails this criterion. |

## Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/16 * 10)
```
```

---

**C-23** closes the process-level gap C-20 and C-21 cannot see: correct schema + correct register + no ordering guard still allows a model to read T2 inputs before T1 outputs are written. The FORBIDDEN must appear at each boundary, not once at the top.

**C-24** closes the observability gap: contract tables declare what variables *should* exist; record blocks prove they *were* emitted. The R6 scorecard's T1-REPO-COUNT gap would have been caught at emission time rather than only at the schema-comparison step.

The two criteria are complementary — C-23 enforces temporal order, C-24 enforces materialization — and both are independently testable from C-20/C-21.
