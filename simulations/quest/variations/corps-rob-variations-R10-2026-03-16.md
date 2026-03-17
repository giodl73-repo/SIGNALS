Written to `simulations/quest/golden/corps-rob-variate-R10-2026-03-16.md`.

---

## Variate R10 -- corps-rob

5 complete variations targeting the four new v10 criteria (C-32 through C-35) as primary-axis targets rather than byproducts.

### Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Carry-forward structural blocks (RULE CARRY-FORWARD, VIOLATION-12) | V-01, V-04, V-05 | C-06, C-32 |
| Named rule glossary preamble (all rules front-loaded, headers cite by name) | V-02, V-04, V-05 | C-30, C-31 |
| Synthesis affirmative identity (RULE SYNTHESIS + required subsections, VIOLATION-13) | V-03, V-05 | C-09, C-10, C-33 |
| C-34 disambiguation annotation in glossary | V-04, V-05 | C-34 |
| C-35 audit table additive-not-replacement constraint (RULE AUDIT-TABLE, VIOLATION-14) | V-05 | C-35 |

---

### V-01 -- Carry-Forward Structural Axis
**Single axis.** RULE CARRY-FORWARD as primary cross-stage coherence mechanism. Mandatory per-stage CARRY FORWARD blocks before findings (not Inherits: notation). CARRY: NONE zero-state. VIOLATION-12 creates a **fourth C-24 enforcement loop**. Default order, single IB-01. Hypothesis: does structural carry-block discipline produce richer C-06 compliance than scattered inline notation?

### V-02 -- Named Rule Glossary Preamble
**Single axis.** All format rules declared in a RUN-LEVEL RULE GLOSSARY before any stage output. Post-stage sections cite rules by glossary name (`[RULE X applies]`), never redeclare inline. Extends C-30 from a single schema to the full rule set. Default order, single IB-01. Hypothesis: does a complete rule glossary eliminate re-declaration noise while preserving full criterion coverage and producing richer C-31 header citations?

### V-03 -- Synthesis Affirmative Identity
**Single axis.** RULE SYNTHESIS declares SYNTHESIS as a **positive artifact** with five enumerated required subsections (BLOCKERS, CROSS-CUTTING THEMES SUMMARY, RESIDUAL OPEN ITEMS, DUAL-DIRECTION CHECK, INERTIA PRESSURE SUMMARY) — not merely "not an audit section." Absence of any required subsection is a SYNTHESIS FORMAT ERROR. VIOLATION-13. Dual IB-01+IB-02. Default order. Hypothesis: does an affirmative synthesis contract produce richer C-09/C-10 content than a negation alone?

### V-04 -- Carry-Forward + Rule Glossary (Combination)
**Combination of V-01 + V-02.** Adds the **C-34 disambiguation annotation** in the glossary: RULE CONDITIONAL-ITEM annotated `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]` at rule-declaration time. Default order, single IB-01. Tests: does a glossary-level disambiguation prevent conflation before either construct is applied?

### V-05 -- Full R10 Stack
**Full combination.** Risk-lead order + dual IB-01+IB-02 + rule glossary preamble + per-stage CARRY FORWARD blocks + RULE SYNTHESIS affirmative identity + C-34 disambiguation + RULE AUDIT-TABLE additive constraint (VIOLATION-14). Four C-24 enforcement loops. Taxonomy extends to VIOLATION-14. Target: **225/225**.

**Retroactive predicted scores under v10:**

| Variation | Predicted Score | Key gains |
|-----------|----------------|-----------|
| V-01 | ~195 | C-32 via VIOLATION-12; C-06 deeper; C-33 from RULE SYNTHESIS |
| V-02 | ~190 | C-30/C-31 via glossary; C-32/C-33 from glossary entries |
| V-03 | ~200 | C-33 affirmative + dual IB; C-09/C-10 richer |
| V-04 | ~210 | V-01+V-02 + C-34 disambiguation |
| V-05 | 225 | All four v10 criteria + four enforcement loops |
