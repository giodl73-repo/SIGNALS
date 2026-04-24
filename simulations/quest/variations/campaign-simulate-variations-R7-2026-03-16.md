Written to `simulations/quest/golden/campaign-simulate-variate-R7-2026-03-16.md`.

---

## Round 7 Variations — Summary

**Context**: R6 V-04 and V-05 both scored 100/100 under v6. Two new criteria extracted (C-24, C-25) raise the raw max to 114.

**Under v7**: R6 V-05 without C-24/C-25 = 110/114 = **96.5 normalized**. To reach 100: both must pass.

---

### Variation Axes

| Variation | Axis | Hypothesis | New Criteria Targeted |
|-----------|------|-----------|----------------------|
| **V-01** | Output format — compliance checklist uses sub-claim architecture for multi-part rows (`fired/partial/not-fired` per sub-claim; partial verdict names failing sub-claim) | C-24 passes by construction; T-1 ANNEX from R6 V-05 preserved | C-24 |
| **V-02** | Output format — per-scope Disposition column (`elevated/withheld-T1/withheld-rule`) is primary T-1 record; T-1 ANNEX is summary-only aggregator | C-25 passes by construction; compliance checklist uses R6 format without sub-claim decomposition | C-25 |
| **V-03** | Lifecycle emphasis — Disposition column promoted to declared structural constraint in the axis table (column schema named as observable, not just described); column absence = structural axis failure | C-25 passes by construction via structural commitment; tests schema-enforcement vs instruction-enforcement | C-25 (alternative) |
| **V-04** | Combined — V-01 + V-02 axes on R6 V-05 base | Both C-24 and C-25 pass; all prior C-01--C-23 mechanisms present | C-24 + C-25 |
| **V-05** | Full integration — sub-claim compliance architecture + per-scope Disposition as declared structural commitment + T-1 ANNEX explicitly characterized as summary-only + structural violation warnings for binary multi-part verdicts | All pass; adds explicit structural violation language to prevent silent degradation | C-24 + C-25 + hardening |

---

**Key design decisions in V-05** (the aspirational best):

1. **Structural axis declaration row 5** names the Disposition column schema verbatim: `Obs #, What was noticed, Disposition [elevated/withheld-T1/withheld-rule], T-1 reason, Filter rule` — making column omission a declaration mismatch, not a formatting preference.

2. **T-1 ANNEX** is explicitly labeled "summary aggregator only — must cite per-scope records." A T-1 ANNEX naming a withheld-T1 observation absent from any per-scope table is called out as a structural violation.

3. **Compliance checklist** opens with an explicit sub-claim architecture rule: "Binary PASS for a multi-part row is a structural violation of this checklist." This is the strongest formulation of C-24 — the violation is named before any row is filled.
