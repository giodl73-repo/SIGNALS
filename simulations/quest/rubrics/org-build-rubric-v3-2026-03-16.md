The agent pulled patterns from a different context. I'll work directly from the scorecard text provided.

Scanning the evidence cells across all variants for patterns that go beyond C-09 through C-13:

**C-14 candidate — phase gate named output variables with input contracts** (V-03, V-04):
- V-03 C-04: "Gate output records ROLE-FILE-COUNT"
- V-03 C-08/C-12: "Input contract: consumes VERDICT from Phase 1 gate"
- V-04 C-08/C-11/C-12: T1-PRESSURE, T1-VERDICT, T3-CATEGORIES-SET as typed outputs consumed downstream

**C-15 candidate — bidirectional verdict guard** (V-02, V-03, V-04):
- V-02 C-13: "FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts."
- V-03/V-04 C-13: "Both is an error. **Neither is an error.**" — C-13 only requires the "both" direction

**C-16 candidate — mitigation cells contain actions, not format guidance** (V-02):
- V-02 C-10: "FORBIDDEN: descriptive format guidance in Mitigation cells"
- Distinct from C-10 which governs "Why It Applies Here" cells

**C-17 candidate — IA scope verbatim enforcement** (V-01, V-02, V-04):
- V-01 C-11: "The scope field is derived, not composed" + "exact text from IA-SCOPE-TEMPLATE-APPLIED"
- V-02 C-11: "FORBIDDEN: writing the inertia-advocate scope field with any text other than the template"
- V-04 C-11: "Not paraphrased. Not adapted. The template text, verbatim."
- C-11 says "derived, not composed" but doesn't block paraphrase

**C-18 candidate — explicit FORBIDDEN exclusion sets per verdict path** (V-02):
- V-02 C-12: "IF CAN-OPERATE-FLAT → FORBIDDEN cat-1/cat-4; IF STRUCTURE-WARRANTED → FORBIDDEN cat-2/cat-3"
- C-12 requires correct derivation; this adds the negative constraint as a separate enforcement surface

All five are distinct from existing criteria. Here is the complete rubric v3:

---

```markdown
---
skill: quest-rubric
skill_target: org-build
date: 2026-03-16
version: 3
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

## Aspirational Criteria (10)

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

## Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)
```

**Golden threshold**: all 5 essential pass + composite >= 80.
```

---

Five new aspirational criteria added (C-14 through C-18):

| # | Pattern | Source variants |
|---|---------|----------------|
| C-14 | Phase gate named output variables + input contracts | V-03, V-04 |
| C-15 | Bidirectional verdict guard ("neither" also error) | V-02, V-03, V-04 |
| C-16 | Mitigation cells: actions not format guidance | V-02 |
| C-17 | IA scope verbatim — paraphrase fails | V-01, V-02, V-04 |
| C-18 | Explicit FORBIDDEN exclusion sets per verdict path | V-02 |

Formula denominator updated from `/5` to `/10` to reflect the expanded aspirational tier.
