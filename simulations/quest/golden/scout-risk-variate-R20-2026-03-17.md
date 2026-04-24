---
skill: scout-risk
round: 20
rubric_version: v19
date: 2026-03-17
---

# Scout-Risk — Round 20 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

---

## Context and Baseline Analysis

**R19 V-05 scored 188/188 on v19 rubric** — the full-combination form satisfying both new v19 criteria
(C-56 and C-57). R20 is exploratory: the variations probe structural escalations not yet required by
v19 but which may crystallize into v20 criteria.

**R19 V-05 Phase 0 state (baseline):**

```
This taxonomy is closed. No type-class label outside this set may be used in any Mitigation cell.
```

"This set" is an implicit reference — it requires a reader to scan upward to locate which set it
describes. The set is the Phase 0 table, but the closure sentence does not name the source block.

**R19 V-05 Phase 0b state (baseline):**

```
This schema is complete and closed. Advance to Phase 0c.
```

Phase 0b closes with a state sentence plus a routing instruction. It carries no use-site constraint
sentence. The global ordering rule in Phase 0c says "This rule applies to Phase 0 and Phase 0c
closures" — Phase 0b is not named in the scope of that rule.

**R19 V-05 Phase 0c ordering meta-rule (baseline):**

```
All taxonomy closure declarations in this prompt consist of two sentences in canonical sequence:
state sentence first ("This taxonomy is closed."), use-site constraint sentence second. This rule
applies to Phase 0 and Phase 0c closures. Reversing this order at any closure site is a schema
violation (Phase 0c Violation Taxonomy).
```

The ordering rule is declared *inside* Phase 0c — one of the two phases it governs. It is applied
globally but its location is nested within a single reference block.

**R19 V-05 Phase 0c closure (baseline):**

```
This taxonomy is closed. No violation category outside this list may be named at any prohibition site.
```

"This list" refers to the Phase 0c table implicitly — the closure names no source block.

**R20 escalation axes:**

| Axis | Pattern | Hypothesis for v20 criterion |
|------|---------|------------------------------|
| Global rule location | Ordering rule lives inside Phase 0c but governs Phase 0 and Phase 0c — is the rule truly global if embedded in one of its governed blocks? | v20 may require the rule to be hoisted to a position outside all reference blocks — a true structural preamble rather than a rule-within-governed-block |
| Phase 0b closure gap | Phase 0b ends with state-only closure ("complete and closed") with no use-site constraint sentence, and is excluded from the global ordering rule scope | v20 may extend C-57 to require Phase 0b coverage: all three pre-phase blocks (Phase 0, Phase 0b, Phase 0c) carry 2-sentence closures and all three are named in the ordering rule |
| Self-naming closures | Both Phase 0 and Phase 0c closures use "this set"/"this list" (implicit reference) rather than naming the source block | v20 may require closures to reference their source block by full name — auditability without scanning, analogous to how prohibition sites were escalated from count to enumeration in v19 |

**Score predictions on v19 rubric:**

| Variation | C-56 | C-57 | v19 Score | Delta |
|-----------|------|------|-----------|-------|
| Baseline (R19 V-05) | PASS | PASS | 188/188 | — |
| V-01 | PASS | PASS or BETTER | 188/188 | 0 |
| V-02 | PASS | PASS | 188/188 | 0 |
| V-03 | PASS | PASS | 188/188 | 0 |
| V-04 | PASS | PASS | 188/188 | 0 |
| V-05 | PASS | PASS | 188/188 | 0 |

All variations maintain v19 score. V-01 may clarify whether C-57's "global scope" requires
out-of-block placement (if so, baseline was PARTIAL and V-01 is the first full PASS). V-02
probes whether Phase 0b's closure gap is a deficiency under C-57's "naming all closure
instances." V-03 probes whether implicit ("this set") vs. explicit ("Phase 0 Mitigation Type
Taxonomy") closure referencing is penalized under a future criterion.

**Axes selected:**
1. **Global rule hoisting** — extract ordering rule from Phase 0c body, place in dedicated block
   between Phase 0a and Phase 0 (negative isolation for rule location)
2. **Phase 0b scope extension** — add Phase 0b to ordering rule scope AND reform Phase 0b closure
   to 2-sentence canonical form
3. **Self-naming closure sentences** — replace "this set"/"this list" in Phase 0 and Phase 0c
   closures with explicit source block names
4. Combination: V-01 + V-02 (hoisted rule + Phase 0b scope and closure)
5. Full combination: V-01 + V-02 + V-03 (hoisted rule + Phase 0b + self-naming all closures)

---

## V-01 — Single axis: Global rule hoisting — ordering rule extracted from Phase 0c body and placed in a dedicated pre-Phase-0 global block

**Hypothesis**: R19 V-05 satisfies C-57 by declaring the ordering rule inside Phase 0c: "All taxonomy
closure declarations in this prompt consist of two sentences in canonical sequence... This rule applies
to Phase 0 and Phase 0c closures." This placement is structurally anomalous: the rule governs Phase 0
(which precedes Phase 0c) but is declared after Phase 0 has already appeared. A reader encountering
Phase 0's closure before reaching Phase 0c's body has not yet seen the rule that governs it. V-01
hoists the ordering rule to a standalone block placed *between Phase 0a and Phase 0*, so the rule
is declared before either governed block executes. If C-57 requires the rule to be "at global scope"
meaning outside any reference block it governs, V-01 is the first true satisfier; baseline is PARTIAL.
If C-57 is satisfied by the rule's semantic scope regardless of physical location, V-01 scores
identically to baseline. All other structure is identical to R19 V-05 — Phase 0b coverage is still
excluded, closures still use implicit references.

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

### Closure Ordering Rule — Global (Declared Before Phase 0 Activates — Applies to All Reference Block Closures)

All taxonomy closure declarations in this prompt consist of two sentences in canonical sequence: state sentence first ("This taxonomy is closed." or equivalent), use-site constraint sentence second. This rule applies to Phase 0 and Phase 0c closures. Reversing this order at any closure site is a schema violation (Phase 0c Violation Taxonomy).

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

This taxonomy is closed. No type-class label outside this set may be used in any Mitigation cell.

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, ... | All Table 2 rows |
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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, identified by phase location: (1) prompt opening sentence — "a cell value outside the stated vocabulary is a format violation"; (2) Phase 0 Mitigation format note — cells not in key=value form "are format violations"; (3) Phase 2 HIGH boundary — "Adding a HIGH-severity row here is a format violation"; (4) Phase 2a repair loop — "Quality violation"; (5) Phase 3 severity columns — "prose, blank, or compound values are format violations". Four violation classes.

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

-> **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

-> **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

-> **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

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

-> **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

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

## V-02 — Single axis: Phase 0b scope extension — ordering rule scope widened to Phase 0b and Phase 0b closure reformed to 2-sentence canonical form

**Hypothesis**: R19 V-05 declares a global ordering rule: "This rule applies to Phase 0 and Phase 0c
closures." Phase 0b also carries a closure sentence ("This schema is complete and closed.") but it is
excluded from the rule's named scope. Under C-57, the rule must "name all closure instances." If Phase
0b's "This schema is complete and closed." qualifies as a closure instance, then the rule's scope is
incomplete and C-57 is PARTIAL in R19 V-05. V-02 extends the scope to "Phase 0, Phase 0b, and Phase
0c closures" AND reforms Phase 0b's closure from state-only ("This schema is complete and closed.
Advance to Phase 0c.") to the canonical 2-sentence pattern: state sentence + use-site constraint
sentence. This creates symmetric closure structure across all three pre-phase reference blocks. All
other content is identical to R19 V-05 — the ordering rule remains inside Phase 0c body, closures
still use implicit references ("this set"/"this list").

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

This taxonomy is closed. No type-class label outside this set may be used in any Mitigation cell.

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, ... | All Table 2 rows |
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

This schema is complete and closed. No field, column, or constraint outside this declaration may be applied to any table in this register. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, identified by phase location: (1) prompt opening sentence — "a cell value outside the stated vocabulary is a format violation"; (2) Phase 0 Mitigation format note — cells not in key=value form "are format violations"; (3) Phase 2 HIGH boundary — "Adding a HIGH-severity row here is a format violation"; (4) Phase 2a repair loop — "Quality violation"; (5) Phase 3 severity columns — "prose, blank, or compound values are format violations". Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

All taxonomy closure declarations in this prompt consist of two sentences in canonical sequence: state sentence first ("This taxonomy is closed." or equivalent), use-site constraint sentence second. This rule applies to Phase 0, Phase 0b, and Phase 0c closures. Reversing this order at any closure site is a schema violation (Phase 0c Violation Taxonomy).

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

-> **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

-> **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

-> **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

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

-> **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

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

## V-03 — Single axis: Self-naming closure sentences — "this set"/"this list" replaced with block-name references in Phase 0 and Phase 0c closures

**Hypothesis**: Phase 0's closure reads "No type-class label outside *this set* may be used in any
Mitigation cell." Phase 0c's closure reads "No violation category outside *this list* may be named
at any prohibition site." Both use implicit deictic references ("this set," "this list") that require
a reader to scan upward to identify the named set. This is analogous to the count-vs-enumeration
escalation that produced C-56: a count requires scanning to verify; an enumeration does not. Similarly,
"this set" requires scanning to locate; a named reference does not. V-03 replaces both implicit
references with explicit source block names: Phase 0's closure becomes "No type-class label outside
the Phase 0 Mitigation Type Taxonomy may be used in any Mitigation cell." Phase 0c's closure becomes
"No violation category outside the Phase 0c Violation Taxonomy may be named at any prohibition site."
A named closure is self-contained — its source block is verifiable by block title without scanning.
If v20 requires named-block closures, implicit "this set"/"this list" would be insufficient. All other
content is identical to R19 V-05 — the ordering rule remains inside Phase 0c, Phase 0b is unchanged.

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

This taxonomy is closed. No type-class label outside the Phase 0 Mitigation Type Taxonomy may be used in any Mitigation cell.

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, ... | All Table 2 rows |
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

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, identified by phase location: (1) prompt opening sentence — "a cell value outside the stated vocabulary is a format violation"; (2) Phase 0 Mitigation format note — cells not in key=value form "are format violations"; (3) Phase 2 HIGH boundary — "Adding a HIGH-severity row here is a format violation"; (4) Phase 2a repair loop — "Quality violation"; (5) Phase 3 severity columns — "prose, blank, or compound values are format violations". Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

All taxonomy closure declarations in this prompt consist of two sentences in canonical sequence: state sentence first ("This taxonomy is closed."), use-site constraint sentence second. This rule applies to Phase 0 and Phase 0c closures. Reversing this order at any closure site is a schema violation (Phase 0c Violation Taxonomy).

This taxonomy is closed. No violation category outside the Phase 0c Violation Taxonomy may be named at any prohibition site.

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

-> **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

-> **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

-> **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

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

-> **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

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

## V-04 — Combination: Global rule hoisting + Phase 0b scope extension (V-01 + V-02)

**Hypothesis**: V-01 isolates whether hoisting improves C-57; V-02 isolates whether Phase 0b scope
extension improves C-57. V-04 combines both: the ordering rule is hoisted to a standalone block
between Phase 0a and Phase 0, AND its scope covers all three pre-phase blocks: Phase 0, Phase 0b,
and Phase 0c. Phase 0b's closure is reformed to the 2-sentence canonical pattern. This is structurally
the strongest formulation of the ordering rule short of also adding self-naming closures: the rule
is positioned before any governed block executes, names every closure instance, and every named
instance follows the declared pattern. If v20 requires both hoisting AND Phase 0b coverage, V-04
is the minimum satisfier. V-03's self-naming is not applied — closures still use "this set"/"this list."

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

### Closure Ordering Rule — Global (Declared Before Phase 0 Activates — Applies to All Reference Block Closures)

All taxonomy closure declarations in this prompt consist of two sentences in canonical sequence: state sentence first ("This taxonomy is closed." or equivalent), use-site constraint sentence second. This rule applies to Phase 0, Phase 0b, and Phase 0c closures. Reversing this order at any closure site is a schema violation (Phase 0c Violation Taxonomy).

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

This taxonomy is closed. No type-class label outside this set may be used in any Mitigation cell.

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, ... | All Table 2 rows |
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

This schema is complete and closed. No field, column, or constraint outside this declaration may be applied to any table in this register. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, identified by phase location: (1) prompt opening sentence — "a cell value outside the stated vocabulary is a format violation"; (2) Phase 0 Mitigation format note — cells not in key=value form "are format violations"; (3) Phase 2 HIGH boundary — "Adding a HIGH-severity row here is a format violation"; (4) Phase 2a repair loop — "Quality violation"; (5) Phase 3 severity columns — "prose, blank, or compound values are format violations". Four violation classes.

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

-> **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

-> **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

-> **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

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

-> **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

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

## V-05 — Full combination: Global rule hoisting + Phase 0b scope extension + self-naming closures (V-01 + V-02 + V-03)

**Hypothesis**: V-05 applies all three positive axes simultaneously. The global ordering rule is hoisted
to a pre-Phase-0 block (V-01), its scope covers Phase 0, Phase 0b, and Phase 0c (V-02), Phase 0b's
closure is reformed to the canonical 2-sentence pattern (V-02), and all three closures name their
source block explicitly (V-03). The combined structure achieves maximum structural self-documentation:
(a) the ordering rule is declared before any governed block executes; (b) every pre-phase reference
block is named in the rule's scope; (c) every closure sentence identifies its source by block name
rather than implicit reference; (d) every closure instance follows the declared canonical sequence.
A reviewer can verify all structural invariants without scanning the full prompt: the global rule block
is the single audit entry point, each named block's closure is verifiable by block title. Expected
188/188 on v19. This is the candidate v20 baseline.

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

### Closure Ordering Rule — Global (Declared Before Phase 0 Activates — Applies to All Reference Block Closures)

All taxonomy and schema closure declarations in this prompt consist of two sentences in canonical sequence: state sentence first ("This taxonomy is closed." or "This schema is complete and closed."), use-site constraint sentence second. This rule applies to Phase 0, Phase 0b, and Phase 0c closures. Reversing this order at any closure site is a schema violation (Phase 0c Violation Taxonomy).

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

This taxonomy is closed. No type-class label outside the Phase 0 Mitigation Type Taxonomy may be used in any Mitigation cell.

---

### Phase 0b — Risk Register Schema Declaration (Pre-Population Field List — Governs All Tables)

Declare the row schema before any row is populated. No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

**Table 2 Row Schema — Dimensional Risk (Base Schema):**

| Field Name | Cell Constraint | Applies To |
|------------|-----------------|------------|
| Risk-ID | Sequential identifier: D-01, D-02, ... | All Table 2 rows |
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

This schema is complete and closed. No field, column, or constraint outside the Phase 0b Risk Register Schema may be applied to any table in this register. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes. Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, identified by phase location: (1) prompt opening sentence — "a cell value outside the stated vocabulary is a format violation"; (2) Phase 0 Mitigation format note — cells not in key=value form "are format violations"; (3) Phase 2 HIGH boundary — "Adding a HIGH-severity row here is a format violation"; (4) Phase 2a repair loop — "Quality violation"; (5) Phase 3 severity columns — "prose, blank, or compound values are format violations". Four violation classes.

| Violation Class | Trigger Condition | Example in This Register |
|-----------------|-------------------|-----------------------------|
| Format | Cell value deviates from a stated vocabulary constraint (severity, dimension, type-class, or other field vocabulary) | Severity cell contains "Critical" instead of HIGH / MEDIUM / LOW |
| Schema | Row anatomy deviates from the Phase 0b field list — extra column added or required field omitted | "Notes" column added to Table 2 outside Phase 0b declaration |
| Boundary | Content violates a declared phase boundary constraint | HIGH-severity row added in Phase 2; Phase 1b entry revised during a Phase 2b repair loop |
| Quality | Prohibited phrase found in a Mitigation cell — vague language not replaced by a typed concrete action | "monitor closely" present in a Mitigation cell after Phase 2a scan |

This taxonomy is closed. No violation category outside the Phase 0c Violation Taxonomy may be named at any prohibition site.

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

-> **Repair Loop A** — Row-count deficit: Return to Phase 2. Add MEDIUM or LOW entries for under-populated dimensions until total count reaches 7. Re-confirm before Phase 2a.

Final row order across Phase 1b + Phase 2: HIGH rows first, MEDIUM second, LOW third.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

-> **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

-> **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

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

-> **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)
2. **Table 1** — Inertia Risk (7-column schema with Decision Window)
3. **Table 2** — Dimensional Risk Register (Phase 1b seeds + Phase 2 additions, HIGH rows first, all columns vocabulary-constrained)
4. **Table 3** — Risk Interdependencies (Trigger Condition + From-Severity + To-Severity columns)
5. **Type distribution** record from Phase 2b
