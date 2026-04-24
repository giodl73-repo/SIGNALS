---
skill: scout-risk
round: 16
rubric_version: v15
date: 2026-03-17
---

# Scout-Risk — Round 16 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

---

## Context and Baseline Analysis

**R15 V-05 scored 162/162 on the v14 rubric**, passing C-01 through C-44 cleanly. The v15 rubric adds three new aspirational criteria. Two of them (C-46, C-47) were already structurally satisfied by R15 V-05 — they formalize patterns already present in that golden. Only C-45 represents an unmet gap.

| New Criterion | v15 Status in R15 V-05 | Evidence |
|---------------|------------------------|----------|
| C-45 | **FAIL** | Phase 2 names "format violation" inline with no pre-declared taxonomy block backing the vocabulary |
| C-46 | PASS (already) | Phase 2b carries `"(which Phase 1b guarantees)"` — names the upstream phase responsible |
| C-47 | PASS (already) | Phase 0b names two extension mechanisms: "adds columns" + "defines its own row anatomy" |

**R16 Baseline state** (= R15 V-05 on v15 rubric): C-01–C-44 PASS, C-46 PASS, C-47 PASS, C-45 FAIL. Score: 166/168.

All five R16 variations target C-45 only. The variation axes explore: (a) WHERE the taxonomy block is positioned, (b) how COMPLETELY it enumerates violation types across the full prompt, and (c) whether per-site back-references to the taxonomy are added.

**Violation types audit of R15 V-05 baseline** — four distinct violation names appear across the prompt:
- `format violation` — Phase 0 (mitigation cell constraint), Phase 2 (HIGH-row prohibition)
- `quality violation` — Phase 2a Repair Loop B
- row-count deficit — Phase 2 Repair Loop A (implicit violation)
- type-diversity deficit — Phase 2b Repair Loop C (implicit violation)
- interdependency-count deficit — Phase 4 Repair Loop D (implicit violation)

C-45 requires all violation type labels be drawn from a pre-defined taxonomy block declared before all generation phases, closing the violation vocabulary.

**Score predictions on v15 rubric:**

| Variation | C-45 | Score | Delta |
|-----------|------|-------|-------|
| Baseline (R15 V-05) | FAIL | 166/168 | — |
| V-01 | PASS | 168/168 | +2 |
| V-02 | PASS | 168/168 | +2 |
| V-03 | PASS | 168/168 | +2 |
| V-04 | PASS | 168/168 | +2 |
| V-05 | PASS | 168/168 | +2 |

**Axes selected:**
1. **Output format** — violation taxonomy as a sub-section appended to Phase 0 (table format, compact), vs. standalone block with prominent closure declaration (V-01/V-02)
2. **Lifecycle emphasis** — taxonomy co-located inside existing Phase 0 vs. declared as a separate pre-phase block (Phase 0c) with the same structural weight as Phase 0 itself
3. **Phrasing register** — taxonomy block introduces labels that violation sites inherit silently vs. each violation site carries an explicit parenthetical taxonomy citation

---

## V-01 — Single axis: Output format — Violation taxonomy as sub-section of Phase 0 (compact table)

**Hypothesis**: C-45 requires a pre-declared block but does not require a dedicated phase or elaborate framing — a sub-section appended to Phase 0 satisfies the structural requirement if it enumerates violation types in a closed table and declares the vocabulary complete. V-01 appends a "Violation Type Reference" sub-section to Phase 0, using the same table format as the mitigation taxonomy but occupying a smaller footprint. Three violation types are declared (Format, Quality, Count-Deficit), covering all named infraction sites in the prompt. The existing Phase 2 "format violation" and Phase 2a "quality violation" labels become valid references into this taxonomy rather than ad hoc names. No per-site annotations are added — the taxonomy is declared once and implicitly governs all sites. Axes V-02 (standalone block) and V-03 (per-site references) are not applied.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. This phase is the only precondition phase. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration. Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output before any other content:

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Taxonomy Reference (Pre-phase — Global Scope — Read Before Phase 0b)

#### Part A: Mitigation Type Taxonomy

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|--------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

#### Part B: Violation Type Reference

Apply this reference to all infraction labels used in any phase or repair loop. Vocabulary is complete and closed. Three classes only. No violation labels outside this set are permitted.

| Violation Class | When It Applies |
|-----------------|-----------------|
| Format Violation | A cell value outside the declared vocabulary for that field, or a mitigation cell not conforming to the required Type-Class key=value format |
| Quality Violation | A mitigation cell containing a prohibited phrase from the Phase 2a scan list |
| Count-Deficit Violation | A phase output containing fewer rows than the stated minimum for that phase |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels are violations. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

**Forward-Reference Coverage Declaration:** This schema is consumed by three generation phases: Phase 1 (uses the Table 1 Schema Extension declared above), Phase 1b (uses the Table 2 Row Schema base for HIGH-seed rows), and Phase 2 (uses the Table 2 Row Schema base for expansion rows). Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**

This schema is complete and closed. Advance to Phase 1.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of any AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register using the Table 2 Row Schema from Phase 0b.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

**Phase 1b completion gate:** Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it before advancing. Do not proceed to Phase 2 with a gap.

Phase 2 inherits these seeded rows and expands around them. Phase 2b confirms the per-dimension HIGH coverage guaranteed here.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Rows)

**Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b.** All active dimensions must be represented. HIGH rows from Phase 1b are already present — do not duplicate them. Add rows until the total Table 2 row count (Phase 1b seeds + Phase 2 additions) reaches **7 rows minimum**.

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation.**

Use the Table 2 Row Schema from Phase 0b. No columns beyond the Phase 0b field list. No field omissions.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies** using the schema below:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Named activation event — IF [From-Risk activates by its stated condition]; this is a dedicated column, not embedded in severity cells |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-02 — Single axis: Lifecycle emphasis — Violation taxonomy as standalone Phase 0c block (parallel structural weight to Phase 0)

**Hypothesis**: C-45 is satisfied by any pre-declared taxonomy block, but the structural strength of the declaration differs when the taxonomy occupies a dedicated phase block vs. a sub-section. V-02 tests whether giving the violation taxonomy the same structural prominence as Phase 0 (dedicated phase header, explicit "complete and closed" declaration, four violation classes covering all infraction sites including repair loop labels) yields a cleaner, more independently legible C-45 pass than V-01's compact sub-section approach. Phase 0 remains the mitigation-only taxonomy; Phase 0c is the dedicated violation type taxonomy. This tests the lifecycle emphasis axis: is the violation taxonomy an appendix to the mitigation taxonomy, or a peer pre-phase reference? All other phases are identical to R15 V-05. No per-site back-references added (V-03 axis not applied).

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. This phase is the only precondition phase. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration. Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output before any other content:

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|--------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels are violations. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

**Forward-Reference Coverage Declaration:** This schema is consumed by three generation phases: Phase 1 (uses the Table 1 Schema Extension declared above), Phase 1b (uses the Table 2 Row Schema base for HIGH-seed rows), and Phase 2 (uses the Table 2 Row Schema base for expansion rows). Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**

This schema is complete and closed. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to all infraction labels used in any phase header, phase body, or repair loop. Taxonomy is complete and closed. Four classes only. No violation labels outside this set are permitted anywhere in this prompt.

| Violation Class | Applies When |
|-----------------|--------------|
| **Format Violation** | A cell value falls outside the declared vocabulary for that column, or a mitigation cell does not conform to the required `[Type-Class: key=value] — action` format |
| **Quality Violation** | A mitigation cell contains one of the prohibited phrases listed in Phase 2a |
| **Count-Deficit Violation** | A phase output contains fewer rows than the minimum stated for that phase |
| **Sequence Violation** | A generation phase begins before its declared precondition phase is complete |

No violation class outside this set is used anywhere. Repair loops that name a violation type draw exclusively from this taxonomy.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of any AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register using the Table 2 Row Schema from Phase 0b.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

**Phase 1b completion gate:** Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it before advancing. Do not proceed to Phase 2 with a gap.

Phase 2 inherits these seeded rows and expands around them. Phase 2b confirms the per-dimension HIGH coverage guaranteed here.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Rows)

**Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b.** All active dimensions must be represented. HIGH rows from Phase 1b are already present — do not duplicate them. Add rows until the total Table 2 row count (Phase 1b seeds + Phase 2 additions) reaches **7 rows minimum**.

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation.**

Use the Table 2 Row Schema from Phase 0b. No columns beyond the Phase 0b field list. No field omissions.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies** using the schema below:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Named activation event — IF [From-Risk activates by its stated condition]; this is a dedicated column, not embedded in severity cells |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-03 — Single axis: Phrasing register — Per-site taxonomy citations (every violation site references the Phase 0 taxonomy by class name)

**Hypothesis**: C-45 requires violation labels to be "drawn from" a pre-declared taxonomy — but a taxonomy block alone satisfies this only if the connection between the block and its usage sites is legible. V-03 tests whether the addition of explicit parenthetical citations at each violation site ("Format Violation per Phase 0 taxonomy") strengthens the pass evidence independently of where the taxonomy block is placed. V-03 places the taxonomy in Phase 0 (compact sub-section, same structure as V-01 Part B) AND adds parenthetical taxonomy citations at all four infraction sites: Phase 2 (format violation), Phase 2a Repair Loop B (quality violation), Phase 2 Repair Loop A (count-deficit violation), and Phase 4 Repair Loop D (count-deficit violation). The taxonomy block itself is identical to V-01. The axis under test is the phrasing register at violation sites — implicit vs. explicit taxonomy reference.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. This phase is the only precondition phase. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration. Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output before any other content:

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Taxonomy Reference (Pre-phase — Global Scope — Read Before Phase 0b)

#### Part A: Mitigation Type Taxonomy

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|--------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

#### Part B: Violation Type Reference

Apply this reference to all infraction labels used in any phase or repair loop. Vocabulary is complete and closed. Three classes only. No violation labels outside this set are permitted.

| Violation Class | When It Applies |
|-----------------|-----------------|
| Format Violation | A cell value outside the declared vocabulary for that field, or a mitigation cell not conforming to the required Type-Class key=value format |
| Quality Violation | A mitigation cell containing a prohibited phrase from the Phase 2a scan list |
| Count-Deficit Violation | A phase output containing fewer rows than the stated minimum for that phase |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels are violations. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

**Forward-Reference Coverage Declaration:** This schema is consumed by three generation phases: Phase 1 (uses the Table 1 Schema Extension declared above), Phase 1b (uses the Table 2 Row Schema base for HIGH-seed rows), and Phase 2 (uses the Table 2 Row Schema base for expansion rows). Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**

This schema is complete and closed. Advance to Phase 1.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of any AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register using the Table 2 Row Schema from Phase 0b.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

**Phase 1b completion gate:** Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it before advancing. Do not proceed to Phase 2 with a gap.

Phase 2 inherits these seeded rows and expands around them. Phase 2b confirms the per-dimension HIGH coverage guaranteed here.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Rows)

**Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b.** All active dimensions must be represented. HIGH rows from Phase 1b are already present — do not duplicate them. Add rows until the total Table 2 row count (Phase 1b seeds + Phase 2 additions) reaches **7 rows minimum**.

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0 taxonomy).**

Use the Table 2 Row Schema from Phase 0b. No columns beyond the Phase 0b field list. No field omissions.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Count-deficit violation (Phase 0 taxonomy): Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation (Phase 0 taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies** using the schema below:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Named activation event — IF [From-Risk activates by its stated condition]; this is a dedicated column, not embedded in severity cells |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field, not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Count-deficit violation (Phase 0 taxonomy): Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

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

## V-04 — Combination: Output format + Lifecycle emphasis (V-01 table format + V-02 standalone block)

**Hypothesis**: V-01 (compact sub-section in Phase 0) and V-02 (standalone Phase 0c block) each pass C-45 through different structural paths. V-04 tests whether combining both properties — a standalone block with its own phase header AND a comprehensive four-class enumeration with explicit closure — produces a stronger C-45 pass than either V-01 or V-02 in isolation. The combination is non-redundant: V-01's contribution is the compact integration with the mitigation taxonomy; V-02's contribution is the structural independence and four-class comprehensiveness. V-04 takes V-02's standalone Phase 0c approach and ensures it carries the explicit four-class count closure declaration ("Four classes only. No violation labels outside this set are permitted."). No per-site annotations (V-03 axis not applied).

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. This phase is the only precondition phase. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration. Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output before any other content:

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|--------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels are violations. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

**Forward-Reference Coverage Declaration:** This schema is consumed by three generation phases: Phase 1 (uses the Table 1 Schema Extension declared above), Phase 1b (uses the Table 2 Row Schema base for HIGH-seed rows), and Phase 2 (uses the Table 2 Row Schema base for expansion rows). Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**

This schema is complete and closed. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to all infraction labels used in any phase header, phase body, or repair loop. Taxonomy is complete and closed. **Four classes only. No violation labels outside this set are permitted anywhere.**

| Violation Class | Applies When |
|-----------------|--------------|
| **Format Violation** | A cell value falls outside the declared vocabulary for that column, or a mitigation cell does not conform to the required `[Type-Class: key=value] — action` format |
| **Quality Violation** | A mitigation cell contains one of the prohibited phrases listed in Phase 2a |
| **Count-Deficit Violation** | A phase output contains fewer rows than the minimum stated for that phase |
| **Sequence Violation** | A generation phase begins before its declared precondition phase is complete |

All repair loops draw violation class labels exclusively from this taxonomy. No infraction is named outside this set.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of any AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register using the Table 2 Row Schema from Phase 0b.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

**Phase 1b completion gate:** Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it before advancing. Do not proceed to Phase 2 with a gap.

Phase 2 inherits these seeded rows and expands around them. Phase 2b confirms the per-dimension HIGH coverage guaranteed here.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Rows)

**Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b.** All active dimensions must be represented. HIGH rows from Phase 1b are already present — do not duplicate them. Add rows until the total Table 2 row count (Phase 1b seeds + Phase 2 additions) reaches **7 rows minimum**.

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation.**

Use the Table 2 Row Schema from Phase 0b. No columns beyond the Phase 0b field list. No field omissions.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies** using the schema below:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Named activation event — IF [From-Risk activates by its stated condition]; this is a dedicated column, not embedded in severity cells |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-05 — Full combination: Lifecycle emphasis + Phrasing register (standalone Phase 0c taxonomy + per-site taxonomy citations at all violation sites)

**Hypothesis**: V-02 (standalone Phase 0c) provides the strongest structural declaration for C-45 — the violation taxonomy has its own phase header and closure statement parallel to Phase 0. V-03 (per-site taxonomy citations) ensures each violation site explicitly draws from the taxonomy by name, making the connection scannable at both source (taxonomy) and usage (violation site). The combination makes C-45 evidence two-directionally verifiable: (a) the taxonomy block pre-declares all violation types before any generation phase; (b) every violation site carries a citation confirming it draws from that block. The two axes are non-interfering: Phase 0c is not changed by V-03's per-site annotations, and the annotations do not require Phase 0c to exist (they would work with V-01's sub-section equally). V-05 applies V-02's standalone Phase 0c (four classes, explicit closure) and V-03's parenthetical taxonomy citations at all four infraction sites. This is the expected 168/168 golden for R16.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation. All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Phase 0a is mandatory when an AMEND directive is present. This phase is the only precondition phase. No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration. Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output before any other content:

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Phase 0a is complete. Confirmed scope is locked. Advance to Phase 0.

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations. Rewrite before advancing.

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|--------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, … | All Table 2 rows |
| Dimension | Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values. | All rows |
| Severity | Exactly one of: HIGH \| MEDIUM \| LOW. No other values. | All rows |
| Likelihood | IF-THEN form: IF [named condition], THEN this risk activates. Bare labels are violations. | All rows |
| Mitigation | `[Type-Class: sub-field=value, sub-field=value] — concrete action`. Drawn from Phase 0 taxonomy. | All rows |
| Type-Class | Exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument. No other values. | All rows |

**Table 1 Schema Extension — Inertia Entry (Extends Base Schema with Named Substitutions):**

The inertia entry (INERTIA-01) draws from the base schema above with the following named field substitutions. Likelihood is replaced by three inertia-specific fields; all other base fields are inherited unchanged.

| Field Name | Schema Relation | Cell Constraint |
|------------|-----------------|-----------------|
| Risk-ID | Inherited, fixed value | INERTIA-01 |
| Dimension | Inherited, fixed value | INERTIA |
| Severity | Inherited | Exactly one of: HIGH \| MEDIUM \| LOW |
| Status-quo Description | Substitution for Likelihood (1 of 3) | Name the concrete behavior or tool the status quo preserves and how adequately it serves current users |
| Inertia Condition | Substitution for Likelihood (2 of 3) | IF-THEN form: IF [named scenario or user behavior], THEN inertia risk activates — bare observations are violations |
| Decision Window | Extension (3 of 3) | Name the concrete deadline, forcing event, or milestone after which this inertia becomes harder to exit — "eventually" and "TBD" are violations |
| Mitigation | Inherited | `[Type-Class: sub-field=value, sub-field=value] — concrete action` testing the inertia hypothesis |

**Forward-Reference Coverage Declaration:** This schema is consumed by three generation phases: Phase 1 (uses the Table 1 Schema Extension declared above), Phase 1b (uses the Table 2 Row Schema base for HIGH-seed rows), and Phase 2 (uses the Table 2 Row Schema base for expansion rows). Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**

This schema is complete and closed. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to all infraction labels used in any phase header, phase body, or repair loop. Taxonomy is complete and closed. **Four classes only. No violation labels outside this set are permitted anywhere in this prompt.**

| Violation Class | Applies When |
|-----------------|--------------|
| **Format Violation** | A cell value falls outside the declared vocabulary for that column, or a mitigation cell does not conform to the required `[Type-Class: key=value] — action` format |
| **Quality Violation** | A mitigation cell contains one of the prohibited phrases listed in Phase 2a |
| **Count-Deficit Violation** | A phase output contains fewer rows than the minimum stated for that phase |
| **Sequence Violation** | A generation phase begins before its declared precondition phase is complete |

All repair loops draw violation class labels exclusively from this taxonomy. No infraction is named outside this set.

---

### Phase 1 — Table 1: Inertia Risk (Mandatory — Schema from Phase 0b — Never Suppressed)

The inertia risk is the risk that the status quo was sufficient and this feature was unnecessary. Produce a single-row table using the Table 1 Schema Extension declared in Phase 0b (7 fields). This table appears in all output regardless of any AMEND directive.

Populate each field per Phase 0b constraints. No new columns. No omitted fields.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Before any MEDIUM or LOW rows exist, seed the HIGH foundation of the register using the Table 2 Row Schema from Phase 0b.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

**Phase 1b completion gate:** Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it before advancing. Do not proceed to Phase 2 with a gap.

Phase 2 inherits these seeded rows and expands around them. Phase 2b confirms the per-dimension HIGH coverage guaranteed here.

---

### Phase 2 — Table 2: Dimensional Risk Register (Schema from Phase 0b — Minimum 7 Rows)

**Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b.** All active dimensions must be represented. HIGH rows from Phase 1b are already present — do not duplicate them. Add rows until the total Table 2 row count (Phase 1b seeds + Phase 2 additions) reaches **7 rows minimum**.

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0c taxonomy).**

Use the Table 2 Row Schema from Phase 0b. No columns beyond the Phase 0b field list. No field omissions.

Count total rows (Phase 1b seeds + Phase 2 additions). Minimum required: **7 rows**.

If fewer than 7 total rows:

→ **Repair Loop A** — Count-deficit violation (Phase 0c taxonomy): Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation (Phase 0c taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Phase 2b terminates when count reaches 3 or greater. Record:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Table 3: Risk Interdependencies (Minimum 3 Rows)

Produce a table titled **Risk Interdependencies** using the schema below:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| Trigger Condition | Named activation event — IF [From-Risk activates by its stated condition]; this is a dedicated column, not embedded in severity cells |
| From-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *before* From-Risk fires |
| To-Severity | Exactly one of: HIGH \| MEDIUM \| LOW — severity of To-Risk *when* From-Risk fires |

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are violations. Trigger Condition is a discrete named field, not embedded in severity cells.

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

→ **Repair Loop D** — Count-deficit violation (Phase 0c taxonomy): Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (7-column schema with Decision Window)
3. **Table 2** — Dimensional Risk Register (Phase 1b seeds + Phase 2 additions, HIGH rows first, all columns vocabulary-constrained)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b
