# flow-trigger — Round 3 Scorecard

## Rubric Version: v3 | Variations: V-01 through V-05

---

## Criterion-by-Criterion Evaluation

### C-01 — Unified Trigger Table *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 2a mandates single table with YES/NO column, explicit `NO row` prohibition on omission |
| V-02 | PASS | Same trigger table structure retained; axis change is budget-only |
| V-03 | PASS | Registry Analyst role produces the same table; specialist role enforces it if anything more strictly |
| V-04 | PASS | Inherits V-01 trigger table; no regression |
| V-05 | PASS | Inherits V-04; threat-first Phase 1 pre-populates table rows from identified threats |

---

### C-02 — Trigger Inputs/Outputs *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Inputs: "concrete values (field schema name, OData token, record ID pattern)"; Outputs: "concrete state changes (field written, entity created, endpoint called)" |
| V-02 | PASS | Same column requirements inherited |
| V-03 | PASS | Registry Analyst role has explicit accountability for Inputs/Outputs columns |
| V-04 | PASS | Inherited from V-01 table spec |
| V-05 | PASS | Phase 1 threat surface drives richer output population before table is written |

---

### C-03 — Firing Sequence *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | `#` column: "Integer firing-sequence for YES rows (1, 2, 3…). `--` for NO rows" — explicit enforcement |
| V-02 | PASS | Identical column enforcement retained |
| V-03 | PASS | Registry Analyst owns the `#` column; role accountability increases compliance |
| V-04 | PASS | Inherited |
| V-05 | PASS | Inherited |

---

### C-04 — Pathology Detection *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 4 table covers all three types with PRESENT/RISK/ABSENT verdicts and cascade trace format |
| V-02 | PASS | Same pathology section; axis change is budget-only |
| V-03 | PASS+ | Pathology Analyst role adds dedicated accountability; role handoff forces fresh-eyes review of C-04 |
| V-04 | PASS | Inherited pathology section; REGISTRY cross-reference enables stronger circular trigger detection |
| V-05 | PASS+ | Threat-first Phase 1 pre-catalogs threat surface; pathology section can reference named threats rather than discovering them mid-table |

---

### C-05 — Side Effects *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Side Effects column: "specific external state changes (target table schema name, recipient role, API hostname, audit log name) or `none`" |
| V-02 | PASS | Inherited; STEP A sub-table maps side-effect automations, reinforcing explicit accounting |
| V-03 | PASS | Registry Analyst role has side effects as named accountability |
| V-04 | PASS | `REGISTRY.SideEffectAutomations` makes side-effect list a first-class named variable — strongest enforcement |
| V-05 | PASS | Inherited from V-04 plus threat-first Phase 1 surfaces side effects early |

---

### C-06 — Condition Evaluation *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Condition Expression column: unconditional format, OData expression format, NO-row exact-expression requirement; `N/A` prohibited |
| V-02 | PASS | Same condition enforcement |
| V-03 | PASS | Budget Analyst role reviews conditions against budget gate inputs — secondary depth check |
| V-04 | PASS | Inherited |
| V-05 | PASS | Inherited |

---

### C-07 — Scenario Boundary *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 1 table: Change type, Field changed, Old/New value, Solution layer, Environment all required |
| V-02 | PASS | Same scenario table |
| V-03 | PASS | Same scenario table; Registry Analyst references it before building the trigger table |
| V-04 | PASS | Inherited |
| V-05 | PASS | Inherited |

---

### C-08 — Remediation Recommendations *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 4 remediation column with specific PA/Copilot Studio syntax templates (`Add trigger condition to [Flow Name]: @not(equals(…))`, `if (context.Depth > 1) return;`, condition node syntax) |
| V-02 | PASS | Same remediation column |
| V-03 | PASS | Pathology Analyst role explicitly owns remediation; specialist accountability sharpens specificity |
| V-04 | PASS | Inherited; REGISTRY names enable "Add trigger condition to [REGISTRY.SideEffectAutomations[i]]" precision |
| V-05 | PASS | Same as V-04 plus threat-first Phase 1 pre-identifies likely pathology type, enabling earlier remediation framing |

---

### C-09 — Trigger Storm Quantification *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Budget table includes "Estimated API requests per occurrence" and "Budget consumed per occurrence (%)"; "Unknown is not acceptable" anti-hedge enforced |
| V-02 | PASS | BUDGET STEP B derives aggregate from STEP A rows — quantification is structurally enforced, not hinted |
| V-03 | PASS | Budget Analyst role owns quantification; however no mandatory two-step lifecycle means enforcement is role-dependent not structural |
| V-04 | PASS | STEP A + STEP B two-phase lifecycle; anti-hedge plus derived aggregate |
| V-05 | PASS | Same as V-04 |

---

### C-10 — Proactive Budget Gate *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 3 before Section 4; gate condition `REGISTRY.M >= 3`; budget table required when gate met; gate fires proactively regardless of storm verdict |
| V-02 | PASS | Same gate position and condition; STEP A ensures gate has per-automation data to read |
| V-03 | PASS | Budget Analyst role runs budget before pathology; structural sequence maintained |
| V-04 | PASS | Gate reads `REGISTRY.M` from §2b code block by explicit variable reference |
| V-05 | PASS | Same as V-04 |

---

### C-11 — Dual-Population Table *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Single unified table with YES/NO enforcement; "Supplemental trigger lists are prohibited anywhere in the output" |
| V-02 | PASS | Same table spec |
| V-03 | PASS | Registry Analyst role enforces single table; separate list prohibition inherited |
| V-04 | PASS | Inherited |
| V-05 | PASS | Inherited |

---

### C-12 — Registry Summary Code Block *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | Section 2b: mandatory code-fence with `REGISTRY.M`, `REGISTRY.N`, `REGISTRY.NonFiring`, `REGISTRY.SideEffectAutomations`; budget gate explicitly reads from §2b: `REGISTRY.M = ___ [value from §2b — do not derive independently]` — downstream reference syntax enforced |
| V-02 | **FAIL** | No registry code-fence required; STEP A sub-table carries per-automation data but M, N, NonFiring are not declared as named variables in a separate code block; budget gate derives M from STEP A rows rather than reading from a declared variable |
| V-03 | **FAIL** | Role sequence does not mandate code-fence format; Registry Analyst role may produce a summary but no structural requirement for the `registry` code-fence or canonical variable identifiers |
| V-04 | **PASS** | Inherits V-01's registry code block; adds `REGISTRY.SideEffectAutomations` as the named list that BUDGET STEP A iterates — creates machine-verifiable cross-reference |
| V-05 | **PASS** | Inherited from V-04; threat-first Phase 1 may pre-populate REGISTRY counts before the table is written |

---

### C-13 — Per-Automation Calculation Basis *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Budget table Calculation Basis column hints `[per-automation: Flow A = X, Plugin B = Y; total = X+Y+…]` but this is a template placeholder in a single cell — not a mandatory sub-table with one row per automation. Aggregate total can still be asserted without intermediate arithmetic being structurally required |
| V-02 | **PASS** | BUDGET STEP A mandatory sub-table: one row per side-effect automation, columns for each action category; BUDGET STEP B derives aggregate from STEP A row totals — two-phase lifecycle enforced; aggregate cannot be asserted before STEP A completes |
| V-03 | **FAIL** | Budget Analyst role owns the estimate but no mandatory two-step lifecycle; per-automation breakdown may appear but is not structurally enforced |
| V-04 | **PASS** | Inherits V-02 STEP A + STEP B lifecycle; STEP A row count must equal `REGISTRY.M`, creating structural linkage to C-12 code block |
| V-05 | **PASS** | Same as V-04 |

---

## Score Summary

```
composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
```

| ID | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Essential | Rec | Asp | Composite | Band |
|----|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|-----|-----|-----------|------|
| V-01 | P | P | P | P | P | P | P | P | P | P | P | **P** | **F** | 4/4 | 3/3 | 5/6 | **98.3** | Gold |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | **F** | **P** | 4/4 | 3/3 | 5/6 | **98.3** | Gold |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | **F** | **F** | 4/4 | 3/3 | 4/6 | **96.7** | Gold |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | 4/4 | 3/3 | 6/6 | **100** | Gold |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | 4/4 | 3/3 | 6/6 | **100** | Gold |

---

## Ranking

| Rank | ID | Score | C-12 | C-13 | Notes |
|------|----|-------|------|------|-------|
| 1 | **V-05** | 100 | PASS | PASS | All four axes — C-12 named variable system + C-13 two-phase lifecycle + threat-first Phase 1 + specialist roles; structurally enforces all 13 criteria |
| 1 | **V-04** | 100 | PASS | PASS | Minimal two-axis proof; C-12 + C-13 cross-reference via `REGISTRY.SideEffectAutomations → STEP A row count = REGISTRY.M` |
| 3 | **V-01** | 98.3 | PASS | FAIL | C-12 fully solved; C-13 hint only — Calculation Basis column template does not mandate two-step lifecycle |
| 3 | **V-02** | 98.3 | FAIL | PASS | C-13 fully solved via mandatory STEP A; C-12 absent — M, N, NonFiring not declared as named variables in code-fence |
| 5 | **V-03** | 96.7 | FAIL | FAIL | Role sequence improves C-04/C-05 depth; neither format innovation enforced structurally |

---

## Excellence Signals from V-04 and V-05

### Signal 1 — Named Variable Cross-Reference Prevents Independent Re-Derivation (C-12 → C-10 linkage)

R2 placed a registry code block but allowed downstream sections to re-derive M from the table. R3 V-01/V-04/V-05 introduce mandatory reference syntax: `REGISTRY.M = ___ [value from §2b — do not derive independently]`. Any inconsistency between the code block and the budget gate is now structurally detectable — the two M values cannot silently diverge because the budget gate is prohibited from counting independently.

### Signal 2 — REGISTRY.SideEffectAutomations as Iteration Contract (C-12 → C-13 linkage)

V-04 and V-05 add `REGISTRY.SideEffectAutomations` as a named list in the code block. BUDGET STEP A must have exactly one row per name in that list, and `row count = REGISTRY.M`. This creates a machine-verifiable cross-reference: if STEP A has 3 rows but REGISTRY.M = 4, the discrepancy is immediately visible. R2 had the code block and the sub-table but no explicit linkage between them.

### Signal 3 — Two-Phase Budget Lifecycle Makes Aggregate a Derived Value, Not an Assertion (C-13)

R2's "Show calculation basis" was a prose template hint inside a single table cell. V-02/V-04/V-05 make STEP B structurally dependent on STEP A: the aggregate total cannot be written until STEP A is complete. This converts the budget estimate from an asserted number into a derived number — every digit is verifiable by row-checking STEP A. Assertions are trust; derivations are evidence.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named variable reference syntax prohibits downstream re-derivation of M — budget gate must cite §2b code block identifier, not re-count the table", "REGISTRY.SideEffectAutomations list in code block creates iteration contract for BUDGET STEP A — row count must equal REGISTRY.M, making C-12 and C-13 machine-verifiably linked", "Two-phase budget lifecycle (STEP A per-automation sub-table → STEP B aggregate derived from STEP A) converts aggregate totals from assertions into derived values"]}
```
