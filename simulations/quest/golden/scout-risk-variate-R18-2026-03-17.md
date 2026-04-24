---
skill: scout-risk
round: 18
rubric_version: v17
date: 2026-03-17
---

# Scout-Risk — Round 18 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

---

## Context and Baseline Analysis

**R17 V-05 scored 180/180 on v17 rubric** — the first round where the baseline already satisfies all criteria including the three new ones. R18 is therefore exploratory: the variations probe structural escalations that are *not yet required* by v17 but may crystallize into v18 criteria.

**R17 V-05 Phase 0c state (baseline):**

```
This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a
closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to
every violation diagnosis in every phase. Every prohibition site in this prompt cites this block by
its full name: Phase 0c Violation Taxonomy. Four violation classes.

[table]

This taxonomy is closed. No violation category outside this list may be named at any prohibition site.
```

- C-51: PASS — two syntactically independent sentences, closure first, prohibition second
- C-52: PASS — parity declaration present in Phase 0c opening ("equal structural weight to Phase 0")
- C-53: PASS — "Every prohibition site in this prompt cites this block by its full name: Phase 0c Violation Taxonomy"

**Five prohibition sites in R17 V-05:**
1. Opening sentence: "a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy)"
2. Phase 0 rewrite gate: "format violations (Phase 0c Violation Taxonomy). Rewrite before advancing."
3. Phase 2 HIGH boundary: "is a format violation (Phase 0c Violation Taxonomy)"
4. Phase 2a repair loop: "Quality violation (Phase 0c Violation Taxonomy)"
5. Phase 3 severity columns: "format violations (Phase 0c Violation Taxonomy)"

**R18 escalation axes:**

| Axis | Pattern | Hypothesis for v18 criterion |
|------|---------|------------------------------|
| C-51 sentence ordering | Does canonical order (closure-then-prohibition) matter, or is reversal (prohibition-then-closure) equivalent? | If reversed form fails C-51, v18 may add C-54: closure sentence must precede prohibition sentence |
| C-52 bi-directional parity | Phase 0 currently has no symmetric parity declaration pointing back to Phase 0c. Add one. | If one-sided parity is weaker, v18 may add C-55: Phase 0 must also carry a parity sentence naming Phase 0c |
| C-53 count-bounded citation | "Every prohibition site" is an unbounded assertion. Replace with "Five prohibition sites" — a counted, verifiable claim. | v18 may add C-56: citation coverage must be declared as a concrete count, not an unbounded universal |

**Score predictions on v17 rubric:**

| Variation | C-51 | C-52 | C-53 | v17 Score | Delta |
|-----------|------|------|------|-----------|-------|
| Baseline (R17 V-05) | PASS | PASS | PASS | 180/180 | — |
| V-01 | PARTIAL | PASS | PASS | 178/180 | -2 |
| V-02 | PASS | PASS | PASS | 180/180 | 0 |
| V-03 | PASS | PASS | PASS | 180/180 | 0 |
| V-04 | PASS | PASS | PASS | 180/180 | 0 |
| V-05 | PASS | PASS | PASS | 180/180 | 0 |

V-01 is the negative control: reversal should cause C-51 PARTIAL (confirming ordering is enforced). V-02 through V-05 are positive explorations: they score identically to baseline on v17 but introduce structural patterns that probe where v18 criteria can grow.

**Axes selected:**
1. **C-51 ordering reversal** — prohibition sentence before closure sentence (negative isolation)
2. **C-52 bi-directional parity** — Phase 0 adds symmetric parity declaration naming Phase 0c
3. **C-53 count-bounded citation** — "Every prohibition site" replaced with "Five prohibition sites"
4. Combination: V-02 + V-03 (bi-directional parity + count-bounded citation)
5. Full combination: V-02 + V-03 + Phase 0c explicit ordering declaration (makes sentence order a stated rule, not a convention)

---

## V-01 — Single axis: C-51 sentence ordering — prohibition sentence before closure sentence (negative isolation)

**Hypothesis**: C-51 requires the closure declaration to consist of two syntactically independent sentences, but does it enforce a canonical order? V-01 reverses the sentence pair in Phase 0c from (closure, prohibition) to (prohibition, closure): "No violation category outside this list may be named at any prohibition site. This taxonomy is closed." Both sentences are present and syntactically independent. If C-51 passes regardless of order, V-01 scores 180/180, suggesting ordering is not part of C-51's pass condition. If C-51 requires closure-first, V-01 scores 178/180 (PARTIAL), providing evidence for a v18 criterion requiring canonical sentence order. All other structure is identical to R17 V-05.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy). All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy activation), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

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
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations (Phase 0c Violation Taxonomy). Rewrite before advancing.

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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Every prohibition site in this prompt cites this block by its full name: Phase 0c Violation Taxonomy. Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

No violation category outside this list may be named at any prohibition site. This taxonomy is closed.

Advance to Phase 1.

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

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0c Violation Taxonomy).**

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

→ **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

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

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are format violations (Phase 0c Violation Taxonomy). Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-02 — Single axis: C-52 bi-directional parity — Phase 0 carries a symmetric parity declaration naming Phase 0c

**Hypothesis**: C-52 requires Phase 0c to declare "equal structural weight to Phase 0." This is a one-sided declaration: Phase 0c points to Phase 0, but Phase 0 carries no corresponding sentence. V-02 adds a symmetric parity declaration to Phase 0's opening: "This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes." Phase 0c retains its existing parity sentence unchanged. The result is bi-directional parity: the relationship is declarable and verifiable by reading either block in isolation, without consulting the other. This may become a v18 criterion (C-55): Phase 0 must carry a symmetric parity declaration naming Phase 0c. V-02 does not change Phase 0c, the closure sentences, or the citation format — all other structure is identical to R17 V-05.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy). All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy activation), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

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

This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations (Phase 0c Violation Taxonomy). Rewrite before advancing.

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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Every prohibition site in this prompt cites this block by its full name: Phase 0c Violation Taxonomy. Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

This taxonomy is closed. No violation category outside this list may be named at any prohibition site.

Advance to Phase 1.

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

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0c Violation Taxonomy).**

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

→ **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

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

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are format violations (Phase 0c Violation Taxonomy). Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-03 — Single axis: C-53 count-bounded citation — "Every prohibition site" replaced with exact count declaration

**Hypothesis**: C-53 requires per-site citations to use the fully-qualified block heading string. The current declaration "Every prohibition site in this prompt cites this block by its full name: Phase 0c Violation Taxonomy" is an unbounded universal assertion — it cannot be falsified by local inspection alone without finding all prohibition sites. V-03 replaces this with a counted declaration: "Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy." A reader can now verify coverage by counting citations found (5 expected) rather than asserting all-sites compliance without a bound. If this pattern produces a v18 criterion (C-56), it would require the coverage declaration to name a concrete count rather than an unbounded "every." All other structure is identical to R17 V-05.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy). All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy activation), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

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
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations (Phase 0c Violation Taxonomy). Rewrite before advancing.

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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy. Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

This taxonomy is closed. No violation category outside this list may be named at any prohibition site.

Advance to Phase 1.

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

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0c Violation Taxonomy).**

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

→ **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

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

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are format violations (Phase 0c Violation Taxonomy). Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-04 — Combination: C-52 bi-directional parity + C-53 count-bounded citation (V-02 + V-03)

**Hypothesis**: V-02 and V-03 are independent improvements — Phase 0 parity sentence and Phase 0c count declaration have no structural dependency. V-04 applies both simultaneously to test whether they interact: does a reviewer who finds the count (5) match the found citations, and also confirm parity from either block, have a qualitatively stronger auditability guarantee than either property alone? The combination tests a pattern where both blocks are self-describing and the coverage claim is falsifiable by count. If this combination is scored distinctly from its parts, it suggests a v18 compound criterion. All other structure is identical to R17 V-05 except Phase 0 (adds parity sentence) and Phase 0c (count declaration replaces "every").

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy). All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy activation), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

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

This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations (Phase 0c Violation Taxonomy). Rewrite before advancing.

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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy. Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

This taxonomy is closed. No violation category outside this list may be named at any prohibition site.

Advance to Phase 1.

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

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0c Violation Taxonomy).**

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

→ **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

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

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are format violations (Phase 0c Violation Taxonomy). Trigger Condition is a discrete named field, not embedded in severity cells.

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

## V-05 — Full combination: C-51 canonical ordering declared + C-52 bi-directional parity + C-53 count-bounded citation + explicit sentence order rule in Phase 0c

**Hypothesis**: V-05 applies all three new axes and adds one further escalation: makes the canonical sentence order (closure-then-prohibition) an *explicitly stated rule* within Phase 0c rather than an implicit convention. The V-01 isolation test probed whether C-51 enforces ordering; V-05 assumes the answer is yes and encodes it. Phase 0c closure section becomes: "The taxonomy closure consists of two sentences in canonical sequence. The state sentence comes first: 'This taxonomy is closed.' The use-site constraint sentence comes second: 'No violation category outside this list may be named at any prohibition site.' Reversing this order is a schema violation." Combined with bi-directional parity (V-02) and count-bounded citation (V-03), V-05 represents the maximum structural auditability form. This pattern — making implicit ordering explicit as a named rule — may become a v18 criterion (C-54). Expected: 180/180 on v17; new patterns position V-05 as the v18 baseline source.

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy). All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — Phase 0 (taxonomy activation), Phase 0b (schema declaration), Phase 0c (violation taxonomy activation), Phase 1 (inertia registration), Phase 1b (HIGH-seed), Phase 2 (register build), Phase 2a (quality gate), Phase 2b (diversity audit), Phase 3 (interdependency build), and Phase 4 (count gate) are role-activating phases that do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

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

This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Taxonomy is complete and closed. Six classes only. No labels outside this set are permitted anywhere.

**Required Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
Cells reading `[Spike]`, `[Gate: check this]`, or any form without explicit key=value pairs are format violations (Phase 0c Violation Taxonomy). Rewrite before advancing.

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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy. Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

The taxonomy closure consists of two sentences in canonical sequence. The state sentence comes first: "This taxonomy is closed." The use-site constraint sentence comes second: "No violation category outside this list may be named at any prohibition site." Reversing this order is a schema violation (Phase 0c Violation Taxonomy).

This taxonomy is closed. No violation category outside this list may be named at any prohibition site.

Advance to Phase 1.

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

**Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. Adding a HIGH-severity row here is a format violation (Phase 0c Violation Taxonomy).**

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

→ **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

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

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are format violations (Phase 0c Violation Taxonomy). Trigger Condition is a discrete named field, not embedded in severity cells.

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
