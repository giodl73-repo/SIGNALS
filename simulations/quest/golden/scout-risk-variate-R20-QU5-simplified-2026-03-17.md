---
skill: scout-risk
round: 20
variant: QU5-simplified
rubric_version: v20
date: 2026-03-17
---

# Scout-Risk — QU5 Simplified Prompt (V-05 Minimal Form)

## Simplification Report

**Baseline**: V-05 (R20) — 188/188 on v19, candidate v20 baseline.
**Goal**: Shortest form that still passes all essential rubric criteria.
**Method**: Remove sentences doing no work — meta-commentary, redundant restatements,
orientation-only forward references, and explanatory elaborations of already-stated constraints.

### What Was Removed and Why

| # | Location | Removed | Words | Reason |
|---|----------|---------|-------|--------|
| 1 | AMEND check | Phase list with function labels ("Phase 0 (taxonomy activation), Phase 0b (schema declaration), ...Phase 4 (count gate) are role-activating phases") → compressed to "all subsequent phases (Phase 0 through Phase 4)" | 37 | Phase names are sufficient; function labels are orientation text, not constraints |
| 2 | Phase 0a body | "Phase 0a is mandatory when an AMEND directive is present." | 12 | Covered by AMEND check preamble ("execute Phase 0a first") |
| 3 | Phase 0a body | "This phase is the only precondition phase." | 9 | Covered by heading "Role-Activation Gate" |
| 4 | Phase 0a body | "No table is seeded, no role activates, no register phase begins until this phase produces and confirms the AMEND Scope Declaration." | 23 | Covered by AMEND check preamble ("do not begin until Phase 0a produces and confirms") |
| 5 | Phase 0a closing | "Phase 0a is complete." | 5 | Trivial state announcement; "Confirmed scope is locked" does the work |
| 6 | Phase 0 intro | "This block is a pre-phase reference block of equal structural weight to Phase 0c — both declare a closed vocabulary before any generation phase executes." | 28 | Pure meta-commentary; no constraint or instruction |
| 7 | Phase 0 intro | "Taxonomy is complete and closed." | 5 | Redundant with the canonical closure sentence at block end |
| 8 | Phase 0b intro | "No row in Table 1 (Phase 1) or Table 2 (Phase 1b and Phase 2) is written before this phase completes." | 22 | Redundant with the preceding "Declare the row schema before any row is populated" |
| 9 | Phase 0b FRCD | Parenthetical schema descriptions: "(uses the Table 1 Schema Extension declared above)", "(uses the Table 2 Row Schema base for HIGH-seed rows)", "(uses the Table 2 Row Schema base for expansion rows)" | 29 | Phase names alone identify scope; verbose descriptions are orientation |
| 10 | Phase 0b FRCD | "Each of these phases references this schema by name." | 9 | Descriptive, not constraining; the prohibition at end is the operative sentence |
| 11 | Phase 0c intro | "This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes." | 28 | Pure meta-commentary; no constraint or instruction |
| 12 | Phase 0c intro | "identified by phase location:" | 4 | Parenthetical label for the numbered list; numbers already identify location |
| 13 | Phase 1 | "No new columns. No omitted fields." | 6 | Fully covered by Phase 0b declaration and schema reference |
| 14 | Phase 1b | "Before any MEDIUM or LOW rows exist," | 7 | Temporal ordering established by phase sequence; Phase 2 adds MEDIUM/LOW after Phase 1b |
| 15 | Phase 1b | "Phase 2 inherits these seeded rows and expands around them. Phase 2b confirms the per-dimension HIGH coverage guaranteed here." | 21 | Orientation-only forward references; both target phases describe their own behavior |
| 16 | Phase 2a | Table scope enumeration "in Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows" → "in all tables" | 15 | "All Mitigation cells" is comprehensive; enumeration adds length not precision |
| 17 | Phase 2b | Count scope enumeration "across Table 1 (Phase 1), Table 2 Phase 1b rows, and Table 2 Phase 2 rows" → "across all tables" | 12 | Same as Phase 2a: "all tables" is sufficient |
| 18 | Phase 2b | "(which Phase 1b guarantees)" | 4 | Parenthetical explanation; parenthetical removed, claim remains in prior sentence |
| 19 | Phase 2b | "A deficit here means the register has type monoculture, not a HIGH coverage gap." | 15 | Explanation of the distinction; the prohibition ("Do not revise Phase 1b entries") is what enforces it |
| 20 | Phase 2b | "Phase 2b terminates when count reaches 3 or greater." | 9 | Implied by "If fewer than 3: Repair Loop C" — loop exits when condition is no longer true |
| 21 | Phase 3 | "Trigger Condition is a discrete named field, not embedded in severity cells." | 12 | Redundant with the column definition: "this is a dedicated column, not embedded in severity cells" |
| 22 | Phase 4 | "Phase 4 terminates when Phase 3 contains at least 3 rows." | 12 | Implied by repair loop structure; loop exits when count ≥ 3 |
| 23 | Phase 5 | "(Phase 0a — if present; includes Active Dimensions and Suppressed Dimensions)" → "(Phase 0a — omit if no AMEND directive)" | 8 | Trim to routing instruction only; field names visible from Phase 0a |
| 24 | Phase 5 | "(Phase 1b seeds + Phase 2 additions, HIGH rows first, all columns vocabulary-constrained)" → "(HIGH rows first)" | 11 | Phase 2 instructions already establish ordering and schema; reminder kept minimal |
| 25 | Phase 5 | "(Trigger Condition + From-Severity + To-Severity columns)" | 8 | Phase 3 already defines the schema; no need to repeat column names in assembly step |

**Total removed**: ~371 words
**Original word count**: ~1,765 words
**Simplified word count**: ~1,394 words
**Reduction**: ~21%

### Criteria Verification

| Criterion | Still passes? | Notes |
|-----------|--------------|-------|
| C-58: Ordering rule before Phase 0 | YES | Closure Ordering Rule block retained between Phase 0a and Phase 0 |
| C-59: Scope covers Phase 0, 0b, 0c | YES | "This rule applies to Phase 0, Phase 0b, and Phase 0c closures" retained verbatim |
| C-60: Closures self-name source blocks | YES | All three closures retain full block names (Phase 0 Mitigation Type Taxonomy / Phase 0b Risk Register Schema / Phase 0c Violation Taxonomy) |
| C-56: Five prohibition sites enumerated | YES | Full enumeration in Phase 0c retained verbatim |
| C-57: Ordering rule global scope, all instances named | YES | Rule is in dedicated block before Phase 0; names all three blocks |
| Format vocabulary (severity, dimension, type-class) | YES | All vocabulary constraints retained in schema tables |
| IF-THEN likelihood | YES | Retained in Phase 0b schema |
| Inertia risk 7-field schema | YES | Phase 0b Table 1 Extension unchanged |
| Phase 1b HIGH-seed + completion gate | YES | Retained fully |
| Phase 2 row minimum (7) | YES | Retained |
| Phase 2a quality gate (7 phrases) | YES | Retained; "full scan" termination condition retained |
| Phase 2b type diversity (3 distinct) | YES | Retained; "do not revise Phase 1b" retained |
| Phase 3 interdependencies (3 rows) | YES | Retained |
| Phase 4 count gate | YES | Repair loop retained; implied termination is sufficient |
| AMEND handling | YES | Phase 0a body and AMEND check retained; gate semantics preserved |

---

## Simplified Prompt Body

---

You are a risk analyst. Execute each phase below in strict sequence. Every phase is mandatory. Every column constraint is enforced — a cell value outside the stated vocabulary is a format violation (Phase 0c Violation Taxonomy). All repair loops are self-healing: execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

**AMEND check: If an AMEND directive accompanies this topic, execute Phase 0a first. Phase 0a is a closed precondition — all subsequent phases (Phase 0 through Phase 4) do not begin until Phase 0a produces and confirms the AMEND Scope Declaration. If no AMEND directive is present, skip Phase 0a and begin at Phase 0.**

---

### Phase 0a — AMEND Resolution (Role-Activation Gate — Completes Before Any Role Activates)

Every subsequent phase inherits the confirmed scope from this output.

Produce the **AMEND Scope Declaration** as this phase's sole output before any other content:

| Field | Constraint |
|-------|------------|
| **Active Dimensions** | Name every dimension retained for Table 2. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |
| **Suppressed Dimensions** | Name every dimension excluded from Table 2 by this AMEND directive. Each value must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values permitted. |

Completeness constraint: Every member of {Technical, Market, Compliance, Dependency, Timeline} appears in exactly one field. No omissions. No duplicates. No values outside this set in either field.

The inertia entry (Table 1) is not subject to AMEND scope reduction. It does not appear in either field.

Confirmed scope is locked. Advance to Phase 0.

---

### Closure Ordering Rule — Global (Declared Before Phase 0 Activates — Applies to All Reference Block Closures)

All taxonomy and schema closure declarations in this prompt consist of two sentences in canonical sequence: state sentence first ("This taxonomy is closed." or "This schema is complete and closed."), use-site constraint sentence second. This rule applies to Phase 0, Phase 0b, and Phase 0c closures. Reversing this order at any closure site is a schema violation (Phase 0c Violation Taxonomy).

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 0b. Apply it to every Mitigation cell in every phase. Six classes only. No labels outside this set are permitted anywhere.

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

Declare the row schema before any row is populated. Every row in every table draws from this field list. No columns are added during Phase 1, Phase 1b, or Phase 2.

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

**Forward-Reference Coverage Declaration:** This schema is consumed by three generation phases: Phase 1, Phase 1b, and Phase 2. **No generation phase outside this list adds columns or defines its own row anatomy.**

This schema is complete and closed. No field, column, or constraint outside the Phase 0b Risk Register Schema may be applied to any table in this register. Advance to Phase 0c.

---

### Phase 0c — Violation Type Taxonomy (Pre-phase Reference — Global Scope)

Read this block before Phase 1. Apply it to every violation diagnosis in every phase. Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, (1) prompt opening sentence — "a cell value outside the stated vocabulary is a format violation"; (2) Phase 0 Mitigation format note — cells not in key=value form "are format violations"; (3) Phase 2 HIGH boundary — "Adding a HIGH-severity row here is a format violation"; (4) Phase 2a repair loop — "Quality violation"; (5) Phase 3 severity columns — "prose, blank, or compound values are format violations". Four violation classes.

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

Populate each field per Phase 0b constraints.

---

### Phase 1b — HIGH-Seed Step (Seed ONE HIGH Row Per Active Dimension — Completes Before Phase 2)

Seed the HIGH foundation of the register using the Table 2 Row Schema from Phase 0b.

For each active dimension in scope — all five (Technical, Market, Compliance, Dependency, Timeline) unless AMEND restricts the set — produce exactly one HIGH-severity row. Write only HIGH rows here. Do not write any MEDIUM or LOW rows in this step.

**Phase 1b completion gate:** Count active dimensions. Count HIGH rows produced here. They must match. If any active dimension lacks a HIGH row, add it before advancing. Do not proceed to Phase 2 with a gap.

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

Scan all Mitigation cells in all tables for these prohibited phrases:

1. "monitor closely" / 2. "keep an eye on" / 3. "revisit later" / 4. "consider alternatives" / 5. "be careful" / 6. "watch for" / 7. "ensure adequate"

If any cell contains one of the seven phrases:

-> **Repair Loop B** — Quality violation (Phase 0c Violation Taxonomy): Replace the prohibited phrase in the affected cell with a typed concrete action from the Phase 0 taxonomy. Key=value sub-field pairs required. Re-execute Phase 2a.

Phase 2a terminates when zero instances of all seven phrases are found in a full scan.

---

### Phase 2b — Type Diversity Audit (Standalone Phase — Do Not Merge with Any Other Step)

Count distinct Type-Class labels across all tables. Minimum required: **3 distinct labels**.

**This audit does not repair per-dimension HIGH coverage — its scope is type-class distribution only. Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**

If fewer than 3 distinct Type-Class labels:

-> **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM rows — until 3 distinct Type-Class labels are present. Re-execute Phase 2b.

Record:

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

From-Severity and To-Severity are each vocabulary-constrained to {HIGH, MEDIUM, LOW} — prose, blank, or compound values are format violations (Phase 0c Violation Taxonomy).

---

### Phase 4 — Interdependency Count Gate (Minimum 3 Rows)

Count rows in Phase 3. Minimum required: **3**.

If fewer than 3:

-> **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or decompose risk entries until the register supports 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

---

### Phase 5 — Final Output Assembly

Output in this order:

1. **AMEND Scope Declaration** (Phase 0a — omit if no AMEND directive)
2. **Table 1** — Inertia Risk (7-column schema with Decision Window)
3. **Table 2** — Dimensional Risk Register (HIGH rows first)
4. **Table 3** — Risk Interdependencies
5. **Type distribution** record from Phase 2b
