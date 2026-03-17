---
skill: scout-risk
round: 13
rubric_version: v12
date: 2026-03-17
---

# Scout-Risk — Round 13 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**R12 baseline state from R11 V-05 (142/142 on v11 rubric)**:
- C-01 through C-34: All passing — full typed-column three-table structure, named repair loops A/B/C/D, Decision Window, row floor (>=7), complete taxonomy in Phase 0, Phase 2b as standalone diversity audit, Phase 0a as structured AMEND header
- **C-35 PARTIAL in R11 V-05**: Phase 0a exists as an isolated sub-phase before Phase 0 and Phase 1, but the prompt does not explicitly state that Phase 0a is a "role-activation gate" — i.e., it does not name Phase 0, Phase 1, Phase 2, Phase 3 as role-activating phases that are all blocked until Phase 0a confirms scope. The constraint is structurally implied by sequencing, not explicitly stated as a precondition contract.
- **C-36 FAIL in all R11 variants**: No HIGH-seed step exists. The diversity audit (Phase 2b) operates retrospectively — it discovers per-dimension HIGH coverage gaps after expansion rather than confirming a seeded guarantee. The HIGH-first row ordering in Phase 2 is a sort constraint, not a seed constraint.
- **C-37 FAIL in all R11 variants**: The Table 2 column schema is defined inline within Phase 2, not as a named pre-population field list declared before any row (including the inertia row in Phase 1) is written. The Phase 0b slot is empty; C-27 (taxonomy pre-declared in Phase 0) is satisfied but the row anatomy schema is not pre-declared as a standalone block.

**R13 targets**:
- C-35: Strengthen Phase 0a as an explicit role-activation gate — name every subsequent phase as a role-activating phase and state Phase 0a as their common closed precondition
- C-36: Add Phase 1b HIGH-Seed Step immediately after Phase 1 (inertia) and before Phase 2 (expansion) — seeds one HIGH row per active dimension before any MEDIUM or LOW rows exist
- C-37: Add Phase 0b Risk Register Schema Declaration between Phase 0 (taxonomy) and Phase 1 (inertia) — declares all Table 2 column names as a named field list with inertia-specific extensions for Table 1, making both tables draw from one pre-population schema

**Score expectation against v12 rubric**:
- R11 V-05 baseline: ~142/148 (C-35 PARTIAL, C-36 FAIL, C-37 FAIL)
- V-01 target: C-35 PASS; C-36, C-37 unchanged (~144/148)
- V-02 target: C-36 PASS; C-35, C-37 unchanged (~144/148)
- V-03 target: C-37 PASS; C-35, C-36 unchanged (~144/148)
- V-04 target: C-35 + C-36 PASS; C-37 unchanged (~146/148)
- V-05 target: C-35 + C-36 + C-37 all PASS (148/148)

**Axes selected**:
1. **Lifecycle emphasis** — Phase 0a phrasing as explicit role-activation gate (C-35 isolation test)
2. **Role sequence** — HIGH-seed sub-phase placement between Phase 1 and Phase 2 (C-36 isolation test)
3. **Output format** — Risk register schema pre-declared as a named Phase 0b field list (C-37 isolation test)
4. Combination: Lifecycle emphasis + Role sequence (C-35 + C-36)
5. Full combination: Lifecycle emphasis + Role sequence + Output format (C-35 + C-36 + C-37)

---

## V-01 — Single axis: Lifecycle emphasis — Phase 0a as explicit role-activation gate (C-35)

**Hypothesis**: The C-35 gap in R11 V-05 is a phrasing gap, not a structural one. Phase 0a already precedes Phase 0 and all register phases, but the prompt never explicitly states that Phase 0, Phase 1, Phase 2, Phase 3, and Phase 4 are "role-activating phases" blocked until Phase 0a confirms. Adding an explicit precondition contract — naming every downstream phase as blocked and Phase 0a as their shared closed precondition — satisfies C-35 without restructuring any phase. V-01 tests this minimal addition in isolation: all other structure is identical to R11 V-05.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 1 (inertia registration), Phase 2 (register build), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. This phase is the only precondition phase. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration below. Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output. Output it before any other content.

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to every Mitigation cell in every phase.

Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Dedicated Schema — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table with the 7-column schema below. This table appears in all output regardless of AMEND directive.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 |
| Dimension | INERTIA |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | IF-THEN form required: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

---

### Phase 2 — Table 2: Dimensional Risk Register (Minimum 7 Rows)

Produce a table covering all five dimensions: Technical, Market, Compliance, Dependency, Timeline. Apply AMEND scope from Phase 0a if present.

Count rows after generating. Minimum required: **7 rows**.

If fewer than 7 rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add entries until row count reaches 7. Re-confirm before Phase 2a.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates — bare labels are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument |

Row order: HIGH first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Phase 1 and Phase 2 for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge)

Count distinct Type-Class labels across Phase 1 and Phase 2. Minimum required: **3 distinct labels**.

If fewer than 3:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Activation event as a dedicated column — IF [From-Risk activates by its named condition]; this field is separate from From-Severity and To-Severity |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field — not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (7-column schema with Decision Window)
3. **Table 2** — Dimensional Risk Register (HIGH rows first; all columns vocabulary-constrained)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b

---

## V-02 — Single axis: Role sequence — HIGH-seed sub-phase within Phase 1 (C-36)

**Hypothesis**: C-36 requires a named HIGH-seed step that produces one HIGH row per active dimension before any expansion rows are added. The gap in R11 V-05 is not a phrasing gap — it is a structural absence. Phase 2 currently sorts rows HIGH-first but does not require HIGH rows to be seeded before MEDIUM/LOW rows are written. A new Phase 1b, placed immediately after Phase 1 (inertia) and before Phase 2 (expansion), seeds the HIGH foundation as its sole output. Phase 2 then expands around the seeded rows. Phase 2b diversity audit shifts from gap-discovery mode to seed-confirmation mode. V-02 tests this structural insertion in isolation — the AMEND section and all other phases are identical to R11 V-05.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a. Otherwise, begin at Phase 0.**

---

### Phase 0a — AMEND Resolution Phase (Execute When AMEND Directive Is Present)

Produce the **AMEND Scope Declaration** as this phase's sole output. Output it before any other content.

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to every Mitigation cell in every phase.

Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Dedicated Schema — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table with the 7-column schema below. This table appears in all output regardless of AMEND directive.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 |
| Dimension | INERTIA |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | IF-THEN form required: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row using the Table 2 column schema below. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

Phase 1b completes when: every active dimension has exactly one HIGH-severity row. Count active dimensions. Count HIGH rows. They must match. If any active dimension lacks a HIGH row, add it now — do not advance to Phase 2 with a gap.

Phase 2 inherits these seeded rows and expands around them. Phase 2b diversity audit confirms the per-dimension HIGH coverage guaranteed here — it does not discover gaps; it confirms a structural fact established in this step.

---

### Phase 2 — Table 2: Dimensional Risk Register (Minimum 7 Rows — Expands Phase 1b Seeds)

Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b. All five dimensions must be represented (subject to AMEND). HIGH rows from Phase 1b are already present — do not duplicate them. Add rows until the total Table 2 row count (Phase 1b seeds + Phase 2 additions) reaches **7 rows minimum**.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … (continue sequence from Phase 1b) |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates — bare labels are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument |

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Phase 1, Phase 1b, and Phase 2 for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge)

Count distinct Type-Class labels across Phase 1, Phase 1b, and Phase 2. Minimum required: **3 distinct labels**.

Note: Phase 1b seeded HIGH-severity rows across all active dimensions. This audit confirms the type distribution of the complete register — it does not repair per-dimension HIGH coverage (which Phase 1b guarantees). If fewer than 3 distinct Type-Class labels are found, the gap is in type diversity, not HIGH coverage.

If fewer than 3:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1, Phase 1b, or Table 2 |
| To-Risk-ID | Risk-ID from Table 1, Phase 1b, or Table 2 |
| Trigger Condition | Activation event as a dedicated column — IF [From-Risk activates by its named condition]; this field is separate from From-Severity and To-Severity |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field — not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (7-column schema with Decision Window)
3. **Table 2** — Dimensional Risk Register (Phase 1b seeds + Phase 2 additions, HIGH rows first, all columns vocabulary-constrained)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b

---

## V-03 — Single axis: Output format — Risk register schema pre-declared as Phase 0b (C-37)

**Hypothesis**: C-37 requires the row anatomy schema (column field list) for the risk register to be declared as a named pre-population block before any row — including the inertia row (Table 1) — is written. R11 V-05 declares the mitigation type taxonomy in Phase 0 (satisfying C-27) but defines Table 2 column constraints inline within Phase 2. The inertia table (Phase 1) defines its own 7-column schema inline as well. There is no single pre-population schema declaration that both tables draw from. Adding Phase 0b between Phase 0 (taxonomy) and Phase 1 (inertia) as a named "Risk Register Schema Declaration" — which pre-declares all Table 2 columns and names the inertia-specific extensions as named substitutions to that schema — satisfies C-37. Table 1 and Table 2 both explicitly reference Phase 0b's schema, making field parity a structural precondition rather than a retrospective consistency check. All other phases are identical to R11 V-05.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a. Otherwise, begin at Phase 0.**

---

### Phase 0a — AMEND Resolution Phase (Execute When AMEND Directive Is Present)

Produce the **AMEND Scope Declaration** as this phase's sole output. Output it before any other content.

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase.

Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1 or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|-----------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels (high, low, possible) are violations. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Field count: 7 (base schema 6 fields + 1 extension). Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (field 1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (field 2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (field 3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

This schema is complete and closed. Advance to Phase 1.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Rows)

Produce a table using the Table 2 Row Schema declared in Phase 0b. Cover all five dimensions: Technical, Market, Compliance, Dependency, Timeline. Apply AMEND scope from Phase 0a if present.

No columns beyond the Phase 0b field list. No field omissions.

Count rows after generating. Minimum required: **7 rows**.

If fewer than 7 rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add entries until row count reaches 7. Re-confirm before Phase 2a.

Row order: HIGH first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Phase 1 and Phase 2 for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge)

Count distinct Type-Class labels across Phase 1 and Phase 2. Minimum required: **3 distinct labels**.

If fewer than 3:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Activation event as a dedicated column — IF [From-Risk activates by its named condition]; this field is separate from From-Severity and To-Severity |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field — not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (Phase 0b schema — 7 fields with Decision Window)
3. **Table 2** — Dimensional Risk Register (Phase 0b schema — HIGH rows first; all columns vocabulary-constrained)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b

---

## V-04 — Combination: Lifecycle emphasis + Role sequence (C-35 + C-36)

**Hypothesis**: C-35 and C-36 address two structural gaps that compound: Phase 0a not explicitly named as a role-activation gate (C-35) and no HIGH-seed step before expansion (C-36). V-04 combines V-01's explicit role-activation gate language with V-02's Phase 1b HIGH-seed step. The combination hypothesis: when Phase 0a is an explicit precondition for role activation AND Phase 1b guarantees per-dimension HIGH coverage before expansion, the two structural patterns reinforce each other — scope confirmation (Phase 0a) feeds directly into the seed dimensions (Phase 1b seeding only active dimensions), making Phase 1b's seed step intrinsically AMEND-aware without additional wiring. C-37 (schema pre-declaration) is not added here — V-04 isolates the C-35+C-36 interaction.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration below. Every subsequent phase — Phase 0 through Phase 4 — inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output. Output it before any other content.

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to every Mitigation cell in every phase.

Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Dedicated Schema — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table with the 7-column schema below. This table appears in all output regardless of AMEND directive.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 |
| Dimension | INERTIA |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | IF-THEN form required: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register. This step uses the confirmed active dimensions from Phase 0a (or all five if no AMEND directive is present).

For each active dimension, produce exactly one HIGH-severity row in the Table 2 column schema below. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

Phase 1b completes when: every active dimension has exactly one HIGH-severity row. Count active dimensions. Count HIGH rows seeded here. They must match. If any active dimension lacks a HIGH row, add it now — do not advance to Phase 2 with a gap.

Phase 2 expands around these seeded rows. Phase 2b diversity audit confirms the per-dimension HIGH coverage established here — it does not discover gaps in HIGH coverage; it confirms a structural fact.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … (starting from D-01) |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline |
| Severity | HIGH only in this step — no MEDIUM or LOW rows written here |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates — bare labels are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument |

---

### Phase 2 — Table 2: Dimensional Risk Register (Minimum 7 Total Rows — Expands Phase 1b Seeds)

Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b. The dimensional register is the union of Phase 1b seeds + Phase 2 additions. Do not duplicate Phase 1b rows. Apply AMEND scope from Phase 0a if present.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 total rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries until total count reaches 7. Re-confirm before Phase 2a.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-NN (continue numbering from Phase 1b) |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates — bare labels are violations |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action` |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument |

Final row order across Phase 1b + Phase 2: HIGH first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Phase 1, Phase 1b, and Phase 2 for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge)

Count distinct Type-Class labels across Phase 1, Phase 1b, and Phase 2. Minimum required: **3 distinct labels**.

Note: Phase 1b seeded HIGH rows across all active dimensions. This audit confirms type distribution across the complete register. If fewer than 3 distinct labels are found, the deficit is in type diversity — not in per-dimension HIGH coverage, which Phase 1b guarantees.

If fewer than 3:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1, Phase 1b, or Phase 2 |
| To-Risk-ID | Risk-ID from Table 1, Phase 1b, or Phase 2 |
| Trigger Condition | Activation event as a dedicated column — IF [From-Risk activates by its named condition]; this field is separate from From-Severity and To-Severity |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field — not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (7-column schema with Decision Window)
3. **Table 2** — Dimensional Risk Register (Phase 1b seeds + Phase 2 additions, HIGH rows first, all columns vocabulary-constrained)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b

---

## V-05 — Combination: Lifecycle emphasis + Role sequence + Output format (C-35 + C-36 + C-37)

**Hypothesis**: All three new criteria require upstream structural additions that are mutually compatible. Phase 0a as a role-activation gate (C-35) confirms scope before any role fires. Phase 0b as a schema pre-declaration (C-37) declares the row anatomy before any row is written. Phase 1b as a HIGH-seed step (C-36) seeds the HIGH foundation before any expansion row is added. These three preconditions form a clean sequence: scope confirmed → schema declared → HIGH seeds placed → expansion begins. Each precondition is a closed output: Phase 0a produces the AMEND Scope Declaration; Phase 0b produces the Risk Register Schema; Phase 1b produces one HIGH row per active dimension. Every downstream phase inherits all three closed outputs. The combination hypothesis: the three preconditions compose without conflict — Phase 0a scope feeds Phase 1b seed dimensions; Phase 0b schema feeds Phase 1 and Phase 2 row format; Phase 1b seeds feed Phase 2 expansion and Phase 2b confirmation. V-05 targets 148/148 by adding all three structural preconditions to the R11 V-05 baseline in the order that makes each one a clean closed output for all downstream phases.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. No table is seeded, no role activates, no schema is declared, no register phase begins until this phase produces and confirms the AMEND Scope Declaration below. Every subsequent phase — Phase 0 through Phase 4 — inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output. Output it before any other content.

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase.

Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. This is the second and final pre-population phase. No row in Table 1 (Phase 1), Phase 1b (HIGH-seed), or Table 2 (Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|-----------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels forbidden. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Field count: 7. Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (field 1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (field 2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (field 3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

This schema is complete and closed. No fields added in any downstream phase. Advance to Phase 1.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register. This step uses the confirmed active dimensions from Phase 0a (or all five if no AMEND is present) and the Table 2 Row Schema from Phase 0b.

For each active dimension, produce exactly one HIGH-severity row using the Phase 0b base schema. Write only HIGH rows here. No MEDIUM or LOW rows in this step.

Phase 1b completes when: every active dimension has exactly one HIGH-severity row. Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it now — do not advance to Phase 2 with a gap.

Phase 2 expands around these seeded rows. Phase 2b confirms per-dimension HIGH coverage as a structural fact established here — it does not discover gaps.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Total Rows)

Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b. The dimensional register is the union of Phase 1b seeds + Phase 2 additions. Do not duplicate Phase 1b rows. Apply AMEND scope from Phase 0a if present. Use the Table 2 Row Schema from Phase 0b — no additional columns.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 total rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Phase 1, Phase 1b, and Phase 2 for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge)

Count distinct Type-Class labels across Phase 1, Phase 1b, and Phase 2. Minimum required: **3 distinct labels**.

Note: Phase 1b guarantees one HIGH row per active dimension. This audit confirms the type-class distribution of the complete register. A deficit here means type monoculture — not a HIGH coverage gap.

If fewer than 3:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1, Phase 1b, or Phase 2 |
| To-Risk-ID | Risk-ID from Table 1, Phase 1b, or Phase 2 |
| Trigger Condition | Activation event as a dedicated column — IF [From-Risk activates by its named condition]; this field is separate from From-Severity and To-Severity |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field — not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (Phase 0b Table 1 Schema Extension — 7 fields with Decision Window)
3. **Table 2** — Dimensional Risk Register (Phase 0b base schema — Phase 1b seeds + Phase 2 additions, HIGH rows first)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b
