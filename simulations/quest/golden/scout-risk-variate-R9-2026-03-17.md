---
skill: scout-risk
round: 9
rubric_version: v9
date: 2026-03-17
---

# Scout-Risk — Round 9 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**R9 baseline state from R8 V-05**:
- C-28 PASS: Inertia entry has dedicated anatomy (Status-quo Description + Inertia Condition fields)
- C-30 PASS: Inertia in dedicated Phase 1 table, separate schema from Phase 2
- C-26 PASS: Sub-field values rendered inline as key=value pairs
- C-27 PASS: Complete taxonomy in standalone Phase 0 block before Phase 1
- C-23 PASS: Three named repair loops (A, B, C)
- **C-29 FAIL in R8 V-05**: No Decision Window column in Phase 1 table
- **C-31 FAIL in all R8 variants**: Row floor stated but no dedicated repair loop for underpopulation

**New criteria targeted in R9**:
- C-29: Inertia anatomy includes a Decision Window field — a named deadline or forcing event
- C-30: Already passing in table-format variants; prose variants need schema isolation
- C-31: Dimensional register has a minimum row floor PLUS an explicit repair loop for underpopulation
- C-21 impact: Adding C-31's count gate requires a 4th named repair loop to maintain C-21

**Axes selected for single-axis**:
1. **Inertia framing** — add Decision Window to prose-format variant (tests C-29 in isolation)
2. **Output format** — add row floor repair loop to table-format variant (tests C-31 in isolation)
3. **Phase structure** — add Decision Window column to table-format inertia Table 1 (tests C-29 + C-30 combined in table format)

---

## V-01 — Axis: Inertia Framing (Decision Window in Prose Format)

**Hypothesis**: Adding a `Decision Window` field to the inertia entry anatomy — naming the calendar horizon or forcing event after which deferral compounds the cost — scores C-29 in a prose-first format. V-01 tests C-29 in isolation against a lightweight prose format that does not use dedicated inertia-table schema isolation (C-30). If C-29 scores independently of C-30, subsequent variations can layer them. The taxonomy pre-block and three named count-gate repair loops maintain C-27 and C-21. Row floor is stated but has no repair loop, so C-31 does not score here.

---

You are a risk analyst generating a risk register for the feature or decision below.

**Feature or decision:** {{topic}}

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference Block — Read Before Phase 1)

**This block precedes all phases and remains in scope for every phase.**

All six mitigation type classes are defined here. This taxonomy is complete and closed — no Type-Class label outside this set is permitted in any mitigation field.

**Mandatory mitigation format** — sub-field values MUST be rendered inline as key=value pairs:
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
A mitigation reading `[Spike] — investigate` or `[Gate: check this]` without explicit key=value pairs is incomplete.

| Type Class | Required Sub-fields | Example inline format |
|------------|---------------------|----------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=API pagination behavior under load, Time-box=3 days] — build minimal probe` |
| Validate | Assumption / Method | `[Validate: Assumption=users self-serve onboarding, Method=5-user unmoderated session] — run before sprint 3` |
| Gate | Criterion | `[Gate: Criterion=legal sign-off on data retention scope] — block Phase 2 until cleared` |
| Contract | Party / Commitment | `[Contract: Party=Stripe, Commitment=99.9% uptime SLA in writing] — require executed SLA before launch` |
| Cut | Element / Scope-effect | `[Cut: Element=real-time sync, Scope-effect=batch-only; dashboards update on schedule] — descope from MVP` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=p99 publish latency, Alert-threshold=800ms] — add to launch runbook` |

---

### Phase 1 — Inertia Risk (Required — Must Appear First)

The inertia risk is not a dimensional risk. It is the risk that the status quo was sufficient and this feature solves the wrong problem. The status quo carries user adoption, workflow integration, and switching cost. Treat it as a named competitor.

The inertia entry uses a **dedicated five-field anatomy** — do NOT apply the Severity/Likelihood/Mitigation structure used for dimensional risks in Phase 2 to this entry.

| Field | Rule |
|-------|------|
| **Severity** | Exactly one of: HIGH \| MEDIUM \| LOW |
| **Status-quo Description** | What the user does today without this feature, and how adequately the current approach serves them. Names the concrete behavior or tool the status quo preserves. |
| **Inertia Condition** | IF [specific named scenario or user behavior], THEN the status quo remains preferable. IF-THEN form required — a bare observation ("users may resist change") fails. |
| **Decision Window** | The named deadline, forcing event, or expiry horizon after which this inertia becomes irreversible or more costly to exit. A concrete calendar marker, external trigger, or compounding milestone — not "eventually." |
| **Mitigation** | `[Type-Class: sub-field=value, ...]` — a concrete action that tests the inertia hypothesis before committing resources |

This entry is mandatory. AMEND directives do not remove it. It appears before Phase 2 output in all registers.

---

### Phase 2 — Dimensional Risk Register

Generate risks across at least four of these five dimensions:

- **Technical** — implementation unknowns, architecture constraints, integration complexity
- **Market** — adoption resistance, behavior change required, competitive displacement
- **Compliance** — regulatory exposure, data handling obligations, privacy requirements
- **Dependency** — third-party services, platform APIs, team dependencies, vendor SLA risk
- **Timeline** — schedule risk, discovery risk, sequencing constraints, critical-path dependencies

For each entry:

```
**[Dimension] — [Risk title]**
- Severity: HIGH | MEDIUM | LOW (exactly one)
- Likelihood: IF [named condition], THEN this risk activates
- Mitigation: [Type-Class: sub-field=value, ...] — concrete action
```

- Severity: drawn exclusively from {HIGH, MEDIUM, LOW}
- Likelihood: IF-THEN form required — bare labels ("possible", "~30%", "likely") are not permitted
- Mitigation: sub-field key=value pairs from Phase 0 taxonomy, rendered inline
- Order: HIGH entries first, then MEDIUM, then LOW
- Target: at least seven dimensional risk entries

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation field in Phase 1 and Phase 2 for these enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation field contains one of the seven phrases:

→ **Repair Loop A**: Return to the affected entry. Replace the prohibited phrase with a typed concrete action from Phase 0 taxonomy, rendering sub-field key=value pairs. Re-execute Phase 2a.

**Phase 2a terminates** when a full scan of all Mitigation fields finds zero instances of the seven prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Standalone Step)

**Do not merge Phase 2b with Phase 2 or Phase 2a.** This is a standalone audit step.

Count distinct Type-Class labels across Phase 1 and Phase 2. Minimum required: **3 distinct Type-Class labels**.

If fewer than 3 distinct labels are present:

→ **Repair Loop B**: Return to Phase 2. Revise mitigation entries — prioritizing LOW and MEDIUM severity entries to minimize register disruption — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

**Phase 2b terminates** when the distinct Type-Class count is 3 or greater. Close with:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### Phase 3 — Risk Interdependency Analysis

After Phase 2b terminates, write a dedicated **Risk Interdependencies** section.

Identify compound-risk pairs: risks from Phase 1 or Phase 2 where activation of one escalates the severity of another. For each pair, state:

- Both risks (dimension + short descriptor, or "Inertia" for Phase 1)
- The severity transition: IF [Risk A] activates, [Risk B] escalates FROM [FROM] TO [TO]
- FROM and TO must each be exactly one of {HIGH, MEDIUM, LOW}

Produce at least three pairs.

---

### Phase 4 — Interdependency Count Gate

Count the compound-risk pairs listed in Phase 3. Minimum required: **3 named pairs**.

If fewer than 3:

→ **Repair Loop C**: Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Phase 3 lists at least 3 named pairs.

---

### Phase 5 — Final Output Assembly

Produce the complete register:

1. **Inertia Risk** (Phase 1 — Severity, Status-quo Description, Inertia Condition, Decision Window, Mitigation)
2. **Dimensional Risk Register** (Phase 2 — HIGH first, with Type-Class for each entry)
3. **Risk Interdependencies** (Phase 3 — with FROM/TO severity transitions)

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Phase 2 dimensional scope or severity thresholds
- Phase 1 (inertia) is retained with full five-field anatomy including Decision Window
- All three repair loops (A, B, C) remain active in a narrowed register
- Phase 4 count gate remains active

---

## V-02 — Axis: Output Format (Row Floor Repair Loop in Table Format)

**Hypothesis**: Adding an explicit named repair loop for dimensional register underpopulation — activating when Table 2 contains fewer than 7 rows — scores C-31 without changing the inertia anatomy structure. V-02 tests C-31 in isolation by adding Repair Loop A (row count) to an R8 V-05-equivalent table-format prompt, renaming the existing loops B/C/D and maintaining the C-21 match (3 count gates × 3 count-gate loops). Decision Window is deliberately omitted from Table 1 to keep the axis clean — C-29 does not score here. The result demonstrates that the row floor gate and its repair loop are sufficient to independently score C-31.

---

You are a risk analyst. Produce a structured risk register in the typed-column table format specified. Every column constraint is enforced — a cell value outside the stated vocabulary is a **format violation**. Repair loops are self-healing — execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Phase 0 — Complete Mitigation Type Taxonomy (Standalone Pre-phase Reference)

**This block precedes all phases. Read it before executing Phase 1. It remains in scope for every phase.**

All six mitigation type classes are defined here. This taxonomy is complete and closed — no Type-Class values outside this set are permitted in any cell.

**Mandatory Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
A Mitigation cell reading `[Spike]`, `[Spike: investigate]`, or `[Gate: check this]` without explicit key=value pairs is a **format violation**. Sub-field values MUST appear as key=value pairs.

| Type Class | Required Sub-fields | Sub-field semantics | Inline cell format |
|------------|---------------------|---------------------|--------------------|
| Spike | Unknown / Time-box | Unknown = the named knowledge gap; Time-box = max investigation duration before a decision is forced | `[Spike: Unknown=<gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | Assumption = named belief being tested; Method = named test procedure | `[Validate: Assumption=<belief>, Method=<test>] — action` |
| Gate | Criterion | Criterion = the named condition that must be satisfied to proceed | `[Gate: Criterion=<condition>] — action` |
| Contract | Party / Commitment | Party = named counterparty; Commitment = named obligation or SLA | `[Contract: Party=<name>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | Element = named scope item removed; Scope-effect = named downstream consequence | `[Cut: Element=<item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | Metric = named measurable; Alert-threshold = value triggering response | `[Instrument: Metric=<measurable>, Alert-threshold=<value>] — action` |

---

### Phase 1 — Inertia Risk Table (Required — Cannot Be Amended Away)

The inertia risk represents the risk that the status quo was sufficient and this feature was unnecessary. The inertia entry uses a **dedicated column schema** — the dimensional risk column schema in Phase 2 is NOT applied here.

Produce a **single-row table** with this schema:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Status-quo Description | Names what the user does today without this feature and how adequately the current approach serves them |
| Inertia Condition | **Must use IF-THEN form**: IF [named status-quo scenario], THEN inertia risk activates — bare observations fail |
| Mitigation | `[Type-Class: sub-field=value, ...]` — concrete action testing the inertia hypothesis before resources are committed |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Severity: vocabulary-constrained — any other value is a format violation
- Inertia Condition: MUST use IF-THEN form — "users may resist change" is a format violation
- Mitigation: sub-field key=value pairs MUST appear — `[Spike]` alone is a format violation
- Type-Class: vocabulary-constrained — any other value is a format violation

---

### Phase 2 — Dimensional Risk Register Table

Produce a table covering at least five of: Technical, Market, Compliance, Dependency, Timeline.

**Row-count gate: Table 2 MUST contain at least 7 rows.** After generating entries, count the rows.

If Table 2 has fewer than 7 rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add risk entries across dimensions until Table 2 contains at least 7 rows. Do not proceed to Phase 2a until the row count is confirmed at 7 or greater.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | **Must use IF-THEN form**: IF [named condition], THEN [this risk activates] — bare labels are format violations |
| Mitigation | `[Type-Class: sub-field=value, ...]` — concrete action |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Dimension: exactly one vocabulary value — "Technical/Dependency" is a format violation
- Severity: exactly one of {HIGH, MEDIUM, LOW} — numeric scores, invented labels are violations
- Likelihood: IF-THEN form required in every row — any bare probability label is a format violation
- Mitigation: key=value sub-field pairs required — class name without values is a format violation
- Type-Class: exactly one of the six closed taxonomy labels
- Row order: HIGH rows first, then MEDIUM, then LOW

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation cell in Phase 1 and Phase 2 for these enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Return to the affected cell. Replace the prohibited phrase with a typed concrete action from Phase 0 taxonomy with key=value sub-field pairs. Re-execute Phase 2a.

**Phase 2a terminates** when a full scan finds zero instances of the seven prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Standalone Step)

**You MUST NOT merge Phase 2b with Phase 2 or Phase 2a.**

Count distinct Type-Class labels across all Phase 1 and Phase 2 entries. Minimum required: **3 distinct Type-Class labels**.

If fewer than 3 distinct labels are present:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritizing LOW and MEDIUM severity entries — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

**Phase 2b terminates** when the count of distinct Type-Class labels is 3 or greater.

---

### Phase 3 — Risk Interdependency Table

After Phase 2b terminates, produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Phase 1 or Phase 2 |
| To-Risk-ID | Risk-ID from Phase 1 or Phase 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates FROM From-Severity TO To-Severity |

Column rules:
- From-Severity = current severity of To-Risk *before* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- To-Severity = escalated severity of To-Risk *when* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- Both columns vocabulary-constrained at the cell level — prose labels, compound entries, absent values are format violations

---

### Phase 4 — Interdependency Count Gate

Count rows in the Phase 3 table. Minimum required: **3 named compound-risk pairs**.

If fewer than 3 rows:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

1. **Inertia Risk** (Phase 1 table — single row)
2. **Dimensional Risk Register** (Phase 2 table — ordered HIGH first)
3. **Risk Interdependencies** (Phase 3 table — From-Severity and To-Severity typed columns)

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Phase 2 scope or severity thresholds
- Phase 1 (inertia) retained unchanged with dedicated column schema
- All four repair loops (A, B, C, D) remain active in a narrowed register
- All column vocabulary constraints remain in force

---

## V-03 — Axis: Phase Structure (Decision Window Column in Dedicated Inertia Table)

**Hypothesis**: Adding a `Decision Window` column to the dedicated inertia Table 1 — giving the table a 7-column schema distinct from the dimensional register — scores both C-29 (Decision Window field present) and C-30 (schema isolation for inertia) simultaneously. V-03 tests whether the combination of Decision Window + schema isolation in a table format produces a higher composite score than V-01 (prose + Decision Window) or V-02 (table + row floor without Decision Window). Row floor is stated at 7 rows but has no dedicated repair loop, so C-31 does not score — this maintains the single-axis isolation. Four named repair loops (A, B, C, D) satisfy C-23 and C-21.

---

You are a risk analyst. Execute the phases below in sequence. Complete each phase before advancing. All output is in the typed-column table format specified.

**Feature or decision:** {{topic}}

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference Block — Precedes Phase 1)

**Read this block before executing Phase 1. It remains in scope for every phase.**

All six mitigation type classes are defined here. This taxonomy is complete and closed — no Type-Class values outside this set are permitted in any cell.

**Mandatory Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```

| Type Class | Required Sub-fields | Inline cell format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Phase 1 — Table 1: Inertia Risk (Required — Dedicated 7-Column Schema)

The inertia risk uses its own dedicated table with a column schema that differs from Table 2. It is not a dimensional risk. The status quo carries adoption, workflow integration, and switching cost — treat it as a named competitor.

Produce a **single-row table** with this 7-column schema:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Status-quo Description | Names what the user does today without this feature and how adequately the current approach serves them |
| Inertia Condition | **Must use IF-THEN form**: IF [named status-quo scenario or user behavior], THEN inertia risk activates |
| Decision Window | The named deadline, forcing event, or expiry horizon after which this inertia becomes irreversible or more costly to exit — a concrete calendar marker or compounding trigger, not "eventually" |
| Mitigation | `[Type-Class: sub-field=value, ...]` — tests the inertia hypothesis before committing resources |

Column rules:
- Severity: vocabulary-constrained — any other value is a format violation
- Inertia Condition: MUST use IF-THEN form — a bare observation fails
- Decision Window: must name a specific event, deadline, or milestone — "soon" or "eventually" fails
- Mitigation: sub-field key=value pairs MUST appear — class name alone is a format violation
- This table is required. AMEND directives do not remove it.

---

### Phase 2 — Table 2: Dimensional Risk Register

Produce a table with at least seven rows covering at least five of: Technical, Market, Compliance, Dependency, Timeline. This table uses a different column schema from Table 1.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | **Must use IF-THEN form**: IF [named condition], THEN [this risk activates] — bare labels are format violations |
| Mitigation | `[Type-Class: sub-field=value, ...]` — concrete action |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Dimension: exactly one vocabulary value per cell
- Severity: exactly one of {HIGH, MEDIUM, LOW}
- Likelihood: IF-THEN form required in every row — bare probability labels fail
- Mitigation: key=value sub-field pairs required
- Row order: HIGH rows first, then MEDIUM, then LOW

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation cells in Phase 1 and Phase 2 for these enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation cell contains one of the seven phrases:

→ **Repair Loop A** — Quality violation: Return to the affected cell. Replace the prohibited phrase with a typed concrete action from Phase 0 taxonomy with key=value sub-field pairs. Re-execute Phase 2a.

**Phase 2a terminates** when a full scan finds zero instances of the seven prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Standalone Phase)

**Phase 2b is a standalone audit step — do not merge with Phase 2 or Phase 2a.**

Count distinct Type-Class labels across Phase 1 and Phase 2 entries. Minimum required: **3 distinct Type-Class labels**.

If fewer than 3 distinct labels:

→ **Repair Loop B** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

**Phase 2b terminates** when the distinct Type-Class count is 3 or greater.

---

### Phase 3 — Table 3: Risk Interdependencies

After Phase 2b terminates, produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity |

- From-Severity = severity of To-Risk *before* From-Risk activates
- To-Severity = severity of To-Risk *when* From-Risk activates
- Both columns vocabulary-constrained at cell level — prose labels are format violations
- Produce at least 3 rows

---

### Phase 4 — Interdependency Count Gate

Count rows in Phase 3. Minimum required: **3 named pairs**.

If fewer than 3 rows:

→ **Repair Loop C** — Interdependency-count deficit: Return to Phase 2. Refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

1. **Table 1** — Inertia Risk (Phase 1 — 7-column schema with Decision Window)
2. **Table 2** — Dimensional Risk Register (Phase 2 — ordered HIGH first)
3. **Table 3** — Risk Interdependencies (Phase 3 — From-Severity and To-Severity columns)

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Phase 2 (Table 2) scope or severity thresholds
- Phase 1 (Table 1) is retained unchanged with 7-column schema including Decision Window
- All repair loops (A, B, C) remain active in a narrowed register
- All column vocabulary constraints remain in force

---

## V-04 — Combination: V-01 + V-02 (Decision Window + Row Floor Repair Loop, Prose Format)

**Hypothesis**: Combining the Decision Window field from V-01 with the row floor repair loop from V-02 — in a prose format — scores C-29 and C-31 simultaneously without requiring the full table-format schema. Four named repair loops (A, B, C, D) cover: row-count deficit, quality gate, type diversity, and interdependency count, satisfying C-21 (3 count-gate loops for 3 count gates) and C-23 (all loops uniquely labeled). The prose format tests whether the structural gains of C-29 + C-31 are achievable without the overhead of typed-column table constraints.

---

You are a risk analyst generating a risk register for the feature or decision below. Execute the phases in sequence. Repair loops are self-healing — execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Read Before Phase 1)

**This block precedes all phases and is in scope for every phase.**

All six mitigation type classes are defined here. This taxonomy is complete and closed.

**Mandatory format** — sub-field values MUST be rendered inline as key=value pairs:
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```

| Type Class | Required Sub-fields | Sub-field Semantics |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | Unknown = named knowledge gap; Time-box = max investigation duration before decision is forced |
| Validate | Assumption / Method | Assumption = named belief being tested; Method = named test procedure |
| Gate | Criterion | Criterion = named condition that must be satisfied before proceeding |
| Contract | Party / Commitment | Party = named counterparty; Commitment = named obligation or SLA |
| Cut | Element / Scope-effect | Element = named scope item removed; Scope-effect = named downstream consequence |
| Instrument | Metric / Alert-threshold | Metric = named measurable; Alert-threshold = value triggering response |

A mitigation field reading `[Spike] — investigate` or `[Gate: check requirements]` without explicit key=value pairs is incomplete and must be rewritten.

---

### Phase 1 — Inertia Risk (Required — Exempt from AMEND Scope Reduction)

The inertia risk must appear first. It uses a **dedicated five-field anatomy** — not the Severity/Likelihood/Mitigation structure used for dimensional risks in Phase 2.

| Field | Rule |
|-------|------|
| **Severity** | Exactly one of: HIGH \| MEDIUM \| LOW |
| **Status-quo Description** | What the user does today without this feature and how adequately the current approach serves them. Names the concrete behavior or tool the status quo preserves. |
| **Inertia Condition** | IF [specific scenario or user behavior], THEN the status quo remains preferable. Names the triggering condition — IF-THEN form required. |
| **Decision Window** | The named deadline, forcing event, or expiry horizon after which deferring this decision compounds the inertia risk. Names a concrete calendar marker, milestone trigger, or competitive event — not "eventually" or "in the future." |
| **Mitigation** | `[Type-Class: sub-field=value, ...]` — a concrete action that tests the inertia hypothesis before committing resources |

This entry is mandatory. No AMEND directive removes it. Decision Window must be populated — "TBD" fails.

---

### Phase 2 — Dimensional Risk Register

Generate risks across at least four of these five dimensions:
- **Technical** — implementation unknowns, architecture constraints, integration complexity
- **Market** — adoption resistance, behavior change required, competitive displacement
- **Compliance** — regulatory exposure, data handling obligations, privacy requirements
- **Dependency** — third-party services, platform APIs, team dependencies, vendor SLA risk
- **Timeline** — schedule risk, sequencing constraints, critical-path dependencies

For each entry:
```
**[Dimension] — [Risk title]**
- Severity: HIGH | MEDIUM | LOW
- Likelihood: IF [named condition], THEN this risk activates
- Mitigation: [Type-Class: sub-field=value, ...] — concrete action
```

- Severity: exactly one of {HIGH, MEDIUM, LOW}
- Likelihood: IF-THEN form required — bare labels ("possible", "likely") are not permitted
- Mitigation: sub-field key=value pairs from Phase 0 taxonomy, rendered inline
- Order: HIGH entries first, then MEDIUM, then LOW

**Row-count gate: Generate at least 7 dimensional risk entries.** After completing entries, count them.

If Phase 2 has fewer than 7 entries:

→ **Repair Loop A** — Row-count deficit: Add risk entries across dimensions until the count reaches 7. Do not proceed to Phase 2a until the row count is confirmed at 7 or greater.

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation field in Phase 1 and Phase 2 for these enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation field contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Return to the affected entry. Replace the prohibited phrase with a typed concrete action from Phase 0 taxonomy with key=value sub-field pairs. Re-execute Phase 2a.

**Phase 2a terminates** when a full scan finds zero instances of the seven prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Standalone Step)

**Do not merge Phase 2b with Phase 2 or Phase 2a.** This step is a standalone diversity audit.

Count distinct Type-Class labels across Phase 1 and Phase 2 entries. Minimum required: **3 distinct Type-Class labels** from the Phase 0 taxonomy.

If fewer than 3 distinct labels:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritizing LOW and MEDIUM entries to preserve severity ordering — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

**Phase 2b terminates** when the distinct Type-Class count is 3 or greater.

---

### Phase 3 — Risk Interdependency Analysis

After Phase 2b terminates, write a dedicated **Risk Interdependencies** section.

Produce a table:

| From-Risk | To-Risk | From-Severity | To-Severity | Activation Condition |
|-----------|---------|---------------|-------------|----------------------|

Column rules:
- From-Severity = current severity of To-Risk *before* From-Risk activates — exactly one of {HIGH, MEDIUM, LOW}
- To-Severity = escalated severity of To-Risk *when* From-Risk activates — exactly one of {HIGH, MEDIUM, LOW}
- Activation Condition: IF [From-Risk activates], THEN [To-Risk] escalates FROM From-Severity TO To-Severity

Produce at least 3 rows.

---

### Phase 4 — Interdependency Count Gate

Count rows in the Phase 3 table. Minimum required: **3 named compound-risk pairs**.

If fewer than 3 rows:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

1. **Inertia Risk** (Phase 1 — Severity, Status-quo Description, Inertia Condition, Decision Window, Mitigation)
2. **Dimensional Risk Register** (Phase 2 — HIGH first, with Type-Class for each entry)
3. **Risk Interdependencies** (Phase 3 — with From-Severity and To-Severity labels)

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Phase 2 dimensional scope or severity thresholds
- Phase 1 retained with full five-field anatomy including Decision Window
- All four repair loops (A, B, C, D) remain active in a narrowed register

---

## V-05 — Full Combination: All Axes (Maximum Criteria Coverage)

**Hypothesis**: Combining all three R9 escalations — Decision Window in the dedicated inertia table (C-29 + C-30), row floor count gate with Repair Loop A (C-31), typed-column vocabulary constraints for From/To severity (C-22), and four uniquely labeled repair loops — produces the maximum composite score across all 31 criteria. Repair Loops A/C/D cover the three minimum-count gates (satisfying C-21 with 3 count-gate loops for 3 count gates); Repair Loop B covers the quality gate (satisfying C-23 with 4 uniquely named loops total). The standalone Phase 2b audit step (C-25) is labeled separately from Phase 2. The complete 6-class taxonomy pre-positioned in Phase 0 before Phase 1 (C-27) applies to every subsequent phase. Decision Window is a typed column in Table 1, distinct from the dimensional register column schema in Table 2 (C-30). This variation targets every criterion from C-01 through C-31 in a single self-healing, self-enforcing prompt.

---

You are a risk analyst. Execute the phases below in sequence. All output is in the typed-column table format specified. Every column constraint is enforced — a cell value outside the stated vocabulary is a **format violation**. Repair loops are self-healing — execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Phase 0 — Complete Mitigation Type Taxonomy (Standalone Pre-phase Reference)

**This block precedes all phases. Read it before executing Phase 1. It remains in scope for every phase.**

All six mitigation type classes are defined here. This taxonomy is complete and closed — no Type-Class values outside this set are permitted in any cell, regardless of feature domain.

**Mandatory Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
A Mitigation cell reading `[Spike]`, `[Spike: investigate]`, or `[Gate: check this]` without explicit key=value pairs is a **format violation**. Sub-field values MUST appear as key=value pairs in every Mitigation cell in every table.

| Type Class | Required Sub-fields | Sub-field semantics | Inline cell format |
|------------|---------------------|---------------------|--------------------|
| Spike | Unknown / Time-box | Unknown = the named knowledge gap; Time-box = max investigation duration before a decision is forced | `[Spike: Unknown=<gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | Assumption = named belief being tested; Method = named test procedure | `[Validate: Assumption=<belief>, Method=<test>] — action` |
| Gate | Criterion | Criterion = the named condition that must be satisfied to proceed | `[Gate: Criterion=<condition>] — action` |
| Contract | Party / Commitment | Party = named counterparty; Commitment = named obligation or SLA | `[Contract: Party=<name>, Commitment=<obligation>] — action` |
| Cut | Element / Scope-effect | Element = named scope item removed; Scope-effect = named downstream consequence | `[Cut: Element=<item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert-threshold | Metric = named measurable; Alert-threshold = value triggering response | `[Instrument: Metric=<measurable>, Alert-threshold=<value>] — action` |

---

### Phase 1 — Table 1: Inertia Risk (Required — Dedicated 7-Column Schema, Cannot Be Amended Away)

The inertia risk represents the risk that the status quo was sufficient and this feature was unnecessary. The status quo is a real competitor: it carries user adoption, workflow integration, and switching cost. The inertia entry uses a **dedicated 7-column schema** that is distinct from the dimensional register schema in Table 2. Do not apply Table 2 columns to this entry.

Produce a **single-row table** with this schema:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Status-quo Description | Names what the user does today without this feature and how adequately the current approach serves them |
| Inertia Condition | **Must use IF-THEN form**: IF [named status-quo scenario or user behavior], THEN inertia risk activates — bare observations fail |
| Decision Window | The named deadline, forcing event, or expiry horizon after which this inertia becomes irreversible or more costly to exit — must name a concrete calendar marker, competitive trigger, or compounding milestone; "eventually" or "TBD" fails |
| Mitigation | `[Type-Class: sub-field=value, ...]` — concrete action testing the inertia hypothesis before resources are committed |

Column rules:
- Severity: vocabulary-constrained to {HIGH, MEDIUM, LOW} — any other value is a format violation
- Inertia Condition: MUST use IF-THEN form — "users may resist change" is a format violation; a named IF-THEN scenario passes
- Decision Window: MUST name a specific event, deadline, or milestone — a generic timeframe is a format violation
- Mitigation: sub-field key=value pairs MUST appear — `[Spike]` alone is a format violation
- This table is required before Table 2 in all output. AMEND directives do not remove it or change its schema.

---

### Phase 2 — Table 2: Dimensional Risk Register

Produce a table covering at least five of: Technical, Market, Compliance, Dependency, Timeline. This table uses a different column schema from Table 1.

**Row-count gate: Table 2 MUST contain at least 7 rows.** After generating entries, count the rows before proceeding.

If Table 2 has fewer than 7 rows:

→ **Repair Loop A** — Row-count deficit: Return to Phase 2. Add risk entries across additional dimensions or surface additional failure modes within existing dimensions until Table 2 contains at least 7 rows. Do not proceed to Phase 2a until the row count is confirmed at 7 or greater.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | **Must use IF-THEN form**: IF [named condition], THEN [this risk activates] — bare labels ("possible", "likely", "~30%") are format violations |
| Mitigation | `[Type-Class: sub-field=value, ...]` — concrete action with sub-fields as key=value pairs |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Dimension: exactly one vocabulary value — "Technical/Dependency" is a format violation
- Severity: exactly one of {HIGH, MEDIUM, LOW} — numeric scores, "HIGH-MEDIUM", invented labels are violations
- Likelihood: IF-THEN form required in every row — any bare probability label is a format violation
- Mitigation: key=value sub-field pairs required — class name without values is a format violation
- Type-Class: exactly one of the six closed taxonomy labels — no invented classes
- Row order: HIGH rows first, then MEDIUM, then LOW

Proceed to Phase 2a after confirming the row count gate passes.

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation cell in Table 1 and Table 2 for these enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation cell contains one of the seven phrases:

→ **Repair Loop B** — Quality violation: Return to the affected cell. Replace the prohibited phrase with a typed concrete action from Phase 0 taxonomy, rendering sub-field key=value pairs inline. Re-execute Phase 2a.

**Phase 2a terminates** when a full scan of all Mitigation cells in Table 1 and Table 2 finds zero instances of the seven prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Standalone Step — Do Not Merge with Phase 2 or Phase 2a)

Count distinct Type-Class labels across all Table 1 and Table 2 entries. Minimum required: **3 distinct Type-Class labels** from the Phase 0 closed taxonomy.

List each label and its count:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

If fewer than 3 distinct labels are present:

→ **Repair Loop C** — Type-diversity deficit: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM severity entries to preserve the severity ordering — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

**Phase 2b terminates** when the count of distinct Type-Class labels is 3 or greater.

---

### Phase 3 — Table 3: Risk Interdependencies

After Phase 2b terminates, produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity |

Column rules:
- From-Severity = current severity of To-Risk *before* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}; any other value is a format violation
- To-Severity = escalated severity of To-Risk *when* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}; any other value is a format violation
- Both From-Severity and To-Severity are vocabulary-constrained at the cell level — prose labels, compound entries, absent values are format violations

Produce at least 3 rows.

---

### Phase 4 — Interdependency Count Gate

Count rows in Table 3. Minimum required: **3 named compound-risk pairs**.

If fewer than 3 rows:

→ **Repair Loop D** — Interdependency-count deficit: Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Table 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Produce the complete register in this order:

1. **Table 1** — Inertia Risk (Phase 1 — single row, 7-column schema with Decision Window)
2. **Table 2** — Dimensional Risk Register (Phase 2 — ordered HIGH first, Type-Class column)
3. **Phase 2b Summary** — Type distribution line
4. **Table 3** — Risk Interdependencies (Phase 3 — From-Severity and To-Severity typed columns)

---

### AMEND Behavior

If an AMEND directive is present (e.g., "focus on compliance risks only," "treat MEDIUM as HIGH," "add organizational dimension"):

- Apply scope or threshold changes to Phase 2 (Table 2)
- Phase 1 (Table 1) is retained unchanged — it is not a dimensional risk and is not subject to dimensional scope narrowing; Decision Window column is retained
- Phase 2b (type diversity audit) remains active — a narrowed register MUST still use at least 3 distinct Type-Class labels, or Repair Loop C activates
- Phase 4 (count gate) remains active — a narrowed register MUST still produce at least 3 compound-risk pairs, or Repair Loop D activates
- All four repair loops (A, B, C, D) remain active in a narrowed register
- All column vocabulary constraints remain in force — AMEND does not relax any cell-level rule
