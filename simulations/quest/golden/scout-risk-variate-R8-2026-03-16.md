---
skill: scout-risk
round: 8
rubric_version: v8
date: 2026-03-16
---

# Scout-Risk — Round 8 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**v8 baseline requirements** (new criteria C-26, C-27, C-28 in every variation):
- C-26: Mitigation cells must render sub-field VALUES inline as `[Type-Class: sub-field=value, ...]` — class name alone is a format violation
- C-27: Complete 6-class taxonomy defined in a standalone reference block BEFORE Phase 1 — not embedded inside any phase
- C-28: Inertia entry carries dedicated anatomy: `Inertia Condition` + `Status-quo Description` as distinct named fields, separate from the Severity/Likelihood/Mitigation structure applied to dimensional risks

**Axes selected for single-axis:**
1. **Inertia framing** — depth and richness of the dedicated inertia anatomy (beyond the C-28 minimum)
2. **Output format** — strict typed-column tables with cell-level vocabulary constraints throughout
3. **Phase structure** — explicit Phase 0 pre-read, numbered phases, three uniquely labeled repair loops

---

## V-01 — Axis: Inertia Framing

**Hypothesis**: Extending the dedicated inertia anatomy beyond the C-28 minimum — adding a `Decision Window` field that names the calendar horizon within which deferral compounds the risk — produces a richer status-quo competitor profile than R7 V-01 achieved. The status-quo framing now includes six named fields (Label, Severity, Status-quo Description, Inertia Condition, Decision Window, Mitigation). The taxonomy pre-block satisfies C-27; the sub-field inline format satisfies C-26; the two dedicated inertia fields satisfy C-28. The single-axis variation is how far the inertia framing extends beyond the minimum.

---

You are a risk analyst generating a risk register for the feature or decision below. Begin where every honest risk register must begin: with the competitor that does not appear on roadmaps, does not file for funding, and wins entirely by default.

**Feature or decision:** {{topic}}

---

### Mitigation Type Reference (Pre-phase — Read Before Writing Any Entry)

Every mitigation must be typed against one of these six classes. The taxonomy is the complete, closed set — no labels outside this list are permitted in any mitigation field.

**Mandatory mitigation format**: Every mitigation must render sub-field values inline with key=value syntax:

```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```

A mitigation reading `[Spike] — investigate` or `[Spike: conduct a study]` — without explicit key=value sub-field pairs — is incomplete.

| Type Class | Required Sub-fields | Example inline format |
|------------|---------------------|----------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=API pagination behavior under load, Time-box=3 days] — build minimal probe` |
| Validate | Assumption / Method | `[Validate: Assumption=users will self-serve onboarding, Method=5-user unmoderated session] — run before sprint 3` |
| Gate | Criterion | `[Gate: Criterion=legal sign-off on data retention scope] — block Phase 2 until cleared` |
| Contract | Party / Commitment | `[Contract: Party=Stripe, Commitment=99.9% uptime SLA in writing] — require executed SLA before launch dependency` |
| Cut | Element / Scope effect | `[Cut: Element=real-time sync, Scope-effect=batch-only mode; dashboards update on schedule not on event] — descope from MVP` |
| Instrument | Metric / Alert threshold | `[Instrument: Metric=p99 publish latency, Alert-threshold=800ms] — add to launch runbook and on-call rotation` |

---

### Section 1 — Status-Quo Competitor Profile (Required — Must Appear First)

The inertia risk is not a dimensional risk. It is the risk that the status quo — the current workaround, the existing tool, the manual process — was sufficient, and this feature solves the wrong problem at the wrong moment. The status quo has adoption, workflow integration, and switching cost on its side. Treat it as a named competitor.

Write the Inertia Risk entry using the **dedicated six-field anatomy** below. Do NOT apply the standard Severity/Likelihood/Mitigation structure to this entry.

| Field | Content |
|-------|---------|
| **Label** | INERTIA (fixed — do not relabel as "adoption risk" or "change management risk") |
| **Severity** | Exactly one of: HIGH \| MEDIUM \| LOW |
| **Status-quo Description** | One sentence: what the user does today without this feature, and how adequately the current approach serves them. Names the concrete behavior or tool the status quo preserves. |
| **Inertia Condition** | The specific scenario or user behavior in which the status quo wins: "IF [named triggering condition], THEN the status quo remains preferable." Not a generic observation — a named condition. |
| **Decision Window** | The time horizon within which the inertia risk compounds — the point at which deferring this decision is itself a decision. Names a concrete calendar marker, milestone, or trigger event. |
| **Mitigation** | `[Type-Class: sub-field=value, ...]` — a concrete action that tests the inertia hypothesis before committing resources |

**This entry is mandatory.** Do not omit it, shorten it, merge it with adoption risk, or place it after dimensional risks. If an AMEND directive narrows dimensional scope, the inertia entry still leads with full six-field anatomy.

---

### Section 2 — Dimensional Risk Register

After the inertia entry, generate risks across at least four of these five dimensions:

- **Technical** — implementation unknowns, architecture constraints, integration complexity, SDK limitations
- **Market** — adoption resistance, behavior change required, competitive displacement, distribution friction
- **Compliance** — regulatory exposure, data handling obligations, privacy requirements, audit trail needs
- **Dependency** — third-party services, platform APIs, team dependencies, vendor SLA risk
- **Timeline** — schedule risk, discovery risk, sequencing constraints, critical-path dependencies

For each dimensional risk entry:

```
**[Dimension] — [Risk title]**
- Severity: HIGH | MEDIUM | LOW
- Likelihood: IF [named triggering condition], THEN this risk activates
- Mitigation: [Type-Class: sub-field=value, ...] — concrete action
```

**Severity rule**: Exactly one of {HIGH, MEDIUM, LOW}. No numeric scales, no invented labels.

**Likelihood rule**: Every likelihood must use IF-THEN form — "IF [named condition], THEN this risk activates." Bare probability labels ("high", "possible", "likely") are not permitted.

**Mitigation rule**: Every mitigation must render sub-field key=value pairs as specified in the reference above. The following phrases are prohibited — if any appear, replace before proceeding:
1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"

**Priority ordering**: List all HIGH entries, then MEDIUM, then LOW. The inertia entry from Section 1 remains first regardless.

---

### Section 3 — Risk Interdependencies

After the dimensional register, write a dedicated **Risk Interdependencies** section.

Identify at least three pairs of risks (from Section 1 and Section 2) that compound each other. For each pair, state the severity transition:

> IF [Risk A] activates, [Risk B] escalates from [FROM severity] to [TO severity]

- FROM: the current severity of Risk B *before* Risk A activates — exactly one of {HIGH, MEDIUM, LOW}
- TO: the escalated severity of Risk B *when* Risk A activates — exactly one of {HIGH, MEDIUM, LOW}

If you cannot identify three distinct compound-risk pairs, return to Section 2 and refine the risk entries until the register supports at least three natural interdependencies.

---

### Section 4 — Type Diversity Check

After writing all entries, count the distinct Type-Class labels used across Sections 1 and 2.

**Minimum**: 3 distinct Type-Class labels from the 6-class reference taxonomy.

If fewer than 3 distinct labels are present, return to Section 2 and revise mitigations to increase type diversity before finalizing output. Close with:

> **Type distribution**: Spike (N), Validate (N), Gate (N), Contract (N), Cut (N), Instrument (N)

---

### AMEND Behavior

If an AMEND directive is present (e.g., "focus on compliance risks only," "treat MEDIUM as HIGH"):

- Apply directive to Section 2 dimensional scope or severity thresholds
- Retain Section 1 with full six-field anatomy regardless of scope
- Retain IF-THEN likelihood form for all remaining entries
- Retain Section 3 interdependency section for the narrowed register
- Retain Section 4 type diversity check

---

## V-02 — Axis: Output Format (Typed-Column Tables + Cell-Level Vocabulary Constraints)

**Hypothesis**: Rendering the entire register as typed-column tables — where Dimension, Severity, Type-Class, From-Severity, and To-Severity each carry explicit cell-level vocabulary constraints — makes format violations mechanically detectable without prose interpretation. The inertia table uses a dedicated column schema (satisfying C-28): a `Status-quo Description` column and an `Inertia Condition` column replace the generic `Likelihood` column used for dimensional risks. Sub-field key=value pairs in Mitigation cells satisfy C-26. The taxonomy reference block before any table satisfies C-27. The single-axis variation is whether strict tables with typed columns outperform prose lists for format compliance.

---

You are a risk analyst. Produce a structured risk register in the exact typed-column table format specified. Every column constraint is enforced — a cell value outside the stated vocabulary is a **format violation**.

**Feature or decision:** {{topic}}

---

### Mitigation Type Taxonomy (Complete Pre-phase Reference — Precedes All Tables)

All six mitigation type classes are defined here before any risk table is produced. This taxonomy is complete and closed — no Type-Class values outside this set are permitted in any cell.

**Mandatory Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
A Mitigation cell containing `[Spike]` alone, or `[Spike: investigate]` without explicit key=value pairs, is a **format violation**.

| Type Class | Required Sub-fields | Inline Cell Format |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | `[Spike: Unknown=<named gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | `[Validate: Assumption=<belief>, Method=<test method>] — action` |
| Gate | Criterion | `[Gate: Criterion=<named condition>] — action` |
| Contract | Party / Commitment | `[Contract: Party=<counterparty>, Commitment=<obligation>] — action` |
| Cut | Element / Scope effect | `[Cut: Element=<scope item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert threshold | `[Instrument: Metric=<measurable>, Alert-threshold=<trigger value>] — action` |

---

### Table 1 — Inertia Risk (Required — Dedicated Column Schema)

Produce a single-row table. This table uses a column schema distinct from Table 2 — the `Status-quo Description` and `Inertia Condition` columns replace the generic `Likelihood` column used in Table 2.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Status-quo Description | Names what the user does today without this feature and how adequately it serves them |
| Inertia Condition | IF [named status-quo scenario], THEN inertia risk activates — not a bare observation; IF-THEN form required |
| Mitigation | `[Type-Class: sub-field=value, ...]` — tests the inertia hypothesis before committing resources |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Severity: vocabulary-constrained — any other value is a format violation
- Inertia Condition: IF-THEN form required — "users may resist change" fails; a named condition with IF-THEN phrasing passes
- Mitigation: sub-field key=value pairs must appear — class name without values is a format violation
- Type-Class: vocabulary-constrained — any other value is a format violation
- This table is required. An AMEND directive does not remove it.

---

### Table 2 — Dimensional Risk Register

Produce a table with at least seven rows covering at least five of: Technical, Market, Compliance, Dependency, Timeline.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | **Must use IF-THEN form**: IF [named condition], THEN [this risk activates] — bare labels ("possible", "likely") are format violations |
| Mitigation | `[Type-Class: sub-field=value, ...]` — concrete action |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Dimension: exactly one vocabulary value — "Technical/Dependency" is a format violation
- Severity: exactly one of {HIGH, MEDIUM, LOW} — numeric scores, compound labels, invented values are violations
- Likelihood: IF-THEN form required in every row — bare probability labels fail
- Mitigation: sub-field key=value pairs required — class name alone is a violation
- Type-Class: exactly one of the six closed taxonomy labels
- Row order: HIGH rows first, then MEDIUM, then LOW

**Mitigation quality gate**: Before finalizing Table 2, scan every Mitigation cell for prohibited phrases: "monitor closely" | "keep an eye on" | "revisit later" | "consider alternatives" | "be careful" | "watch for" | "ensure adequate". Replace any occurrence with a typed concrete action with sub-field values.

**Type diversity gate**: Count distinct Type-Class values across Table 1 and Table 2. If fewer than 3 distinct values appear, revise Table 2 Mitigation and Type-Class cells before proceeding.

---

### Table 3 — Risk Interdependencies

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Table 1 or Table 2 |
| To-Risk-ID | Risk-ID from Table 1 or Table 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity |

Column rules:
- From-Severity = current severity of To-Risk *before* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- To-Severity = escalated severity of To-Risk *when* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- Both columns are vocabulary-constrained at the cell level — prose labels, compound entries, absent values are format violations
- Produce at least 3 rows

**Count gate**: If Table 3 has fewer than 3 rows, revise Table 2 and regenerate Table 3 until the row count reaches 3.

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Table 2 dimensional scope or severity thresholds
- Table 1 (inertia) retained unchanged with dedicated column schema
- All column vocabulary constraints remain in force
- Type diversity gate and interdependency count gate remain active

---

## V-03 — Axis: Phase Structure (Lifecycle Emphasis)

**Hypothesis**: An explicit Phase 0 reference block — positioned before Phase 1 and clearly labeled as a pre-phase document — is the structural enforcement mechanism for C-27. Naming every repair loop with a unique label (Repair Loop A, B, C) makes the total loop count trivially verifiable (C-23) and each loop independently addressable. Isolating the type diversity audit in its own dedicated Phase 2b (distinct from Phase 2) prevents the audit from being merged into generation (C-25). The single-axis variation is the granularity and explicitness of phase delineation.

---

You are a risk analyst. Execute the phases below in sequence. Complete each phase before advancing. Repair loops are self-correcting — execute the repair instruction, then re-execute the named phase.

**Feature or decision:** {{topic}}

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference Block)

**This is a pre-phase document. Read it before executing Phase 1.**

Every mitigation in this register must be typed against one of these six classes. The taxonomy is the complete, closed set. No Type-Class labels outside this list are permitted.

Every mitigation must render sub-field values inline with key=value syntax:
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
A mitigation reading `[Gate] — hold` or `[Spike: investigate something]` without explicit key=value pairs is incomplete.

| Type Class | Required Sub-fields | Example |
|------------|---------------------|---------|
| Spike | Unknown / Time-box | `[Spike: Unknown=third-party webhook reliability, Time-box=2 days] — build probe before committing` |
| Validate | Assumption / Method | `[Validate: Assumption=power users tolerate 3-step flow, Method=moderated test with 6 users] — complete before beta` |
| Gate | Criterion | `[Gate: Criterion=security review sign-off for PII scope] — block release branch until cleared` |
| Contract | Party / Commitment | `[Contract: Party=Auth0, Commitment=documented token rotation SLA] — require before dependency is locked` |
| Cut | Element / Scope effect | `[Cut: Element=bulk export endpoint, Scope-effect=API surface reduced; third-party integrations need manual workaround] — descope and log` |
| Instrument | Metric / Alert threshold | `[Instrument: Metric=error rate on POST /publish, Alert-threshold=2% over 5min window] — configure before canary` |

---

### Phase 1 — Generate Inertia Risk (Required)

The inertia risk is the first entry in every register. It is not a dimensional risk — it is the risk that the status quo was sufficient and this feature was unnecessary. The inertia entry uses a **dedicated anatomy**; the standard Severity/Likelihood/Mitigation structure used in Phase 2 is NOT applied to this entry.

**Inertia Anatomy:**

| Field | Rule |
|-------|------|
| **Label** | INERTIA (fixed) |
| **Severity** | Exactly one of: HIGH \| MEDIUM \| LOW |
| **Status-quo Description** | Names what the user does today without this feature and how adequately the current approach serves them |
| **Inertia Condition** | IF [specific named scenario or user behavior], THEN the status quo remains preferable — IF-THEN form required |
| **Mitigation** | `[Type-Class: sub-field=value, ...]` — tests the inertia hypothesis before committing resources |

This entry is required. No AMEND directive removes it. It appears before Phase 2 output in all registers.

After completing this entry, proceed to Phase 2.

---

### Phase 2 — Generate Dimensional Risk Register

Generate at least seven risks covering at least five of: Technical, Market, Compliance, Dependency, Timeline.

For each risk, use this anatomy:

```
**[Dimension] — [Risk title]**
- Severity: HIGH | MEDIUM | LOW (exactly one)
- Likelihood: IF [named condition], THEN [this risk activates]
- Mitigation: [Type-Class: sub-field=value, ...] — concrete action
```

- Severity: drawn exclusively from {HIGH, MEDIUM, LOW}
- Likelihood: IF-THEN form required in every entry — bare labels are not permitted
- Mitigation: typed with sub-field key=value pairs from Phase 0 taxonomy
- Row order: HIGH entries first, then MEDIUM, then LOW

After drafting all entries, proceed to Phase 2a.

---

### Phase 2a — Mitigation Quality Gate

Scan all Mitigation fields from Phase 1 and Phase 2 for the following enumerated prohibited phrases:

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

### Phase 2b — Mitigation Type Diversity Audit (Standalone Audit Step)

This phase is a standalone audit step. **Do not merge Phase 2b into Phase 2 or Phase 2a.**

Count the distinct Type-Class names used across Phase 1 and Phase 2 entries.

Minimum required: **3 distinct Type-Class labels** from the Phase 0 taxonomy.

If fewer than 3 distinct labels are present:

→ **Repair Loop B**: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM severity entries to minimize register disruption — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

**Phase 2b terminates** when the distinct Type-Class count is 3 or greater.

---

### Phase 3 — Risk Interdependency Analysis

After Phase 2b terminates, write a dedicated **Risk Interdependencies** section.

Identify compound-risk pairs: risks from Phase 1 or Phase 2 where activation of one escalates the severity of another. For each pair:

- Name both risks (dimension + short descriptor, or "Inertia" for the Phase 1 entry)
- State the severity transition: IF [Risk A] activates, [Risk B] escalates from [FROM] to [TO]
- FROM and TO must each be exactly one of {HIGH, MEDIUM, LOW}

Produce at least 3 pairs.

---

### Phase 4 — Interdependency Count Gate

Count the compound-risk pairs listed in Phase 3.

Minimum required: **3 named pairs**.

If fewer than 3 pairs are present:

→ **Repair Loop C**: Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Phase 3 lists at least 3 named pairs.

---

### Phase 5 — Final Output Assembly

Produce the complete register in this order:

1. **Inertia Risk** (Phase 1 output — with Status-quo Description and Inertia Condition fields)
2. **Dimensional Risk Register** (Phase 2 output — HIGH first, with Type-Class for each entry)
3. **Risk Interdependencies** (Phase 3 output — with FROM/TO severity labels for each pair)

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Phase 2 dimensional scope or severity thresholds
- Phase 1 (inertia) is retained with full dedicated anatomy regardless of scope
- Phase 2b (type diversity audit) and Repair Loop B remain active
- Phase 4 (count gate) and Repair Loop C remain active
- All three repair loops (A, B, C) remain active in a narrowed register

---

## V-04 — Combination: V-01 + V-03 (Rich Inertia Profile + Named Phases)

**Hypothesis**: Combining the richest inertia framing (six-field anatomy with Decision Window, treating the status quo as a named competitor) with fully named lifecycle phases and three explicitly labeled repair loops addresses two previously uncorrelated failure modes simultaneously: insufficient inertia structural differentiation (C-28) and ambiguous repair loop count (C-23). The brainstorm-first role sequence — listing candidate risk titles before expanding anatomy — also reduces the chance of shallow dimensional coverage by surveying the risk landscape before committing to entry structure.

---

You are a risk analyst. Execute the phases in sequence. Complete each phase before advancing. Repair loops are self-healing — execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Phase 0 — Mitigation Type Taxonomy (Pre-phase Reference — Read Before Phase 1)

All six mitigation type classes are defined here. This taxonomy is the complete, closed set. No Type-Class labels outside this list are permitted in any mitigation field.

Every mitigation must render sub-field values inline with key=value syntax:
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```

| Type Class | Required Sub-fields | Sub-field Semantics |
|------------|---------------------|---------------------|
| Spike | Unknown / Time-box | Unknown = the named knowledge gap; Time-box = max investigation duration before a decision is forced |
| Validate | Assumption / Method | Assumption = the named belief being tested; Method = the named test procedure |
| Gate | Criterion | Criterion = the named condition that must be satisfied before proceeding |
| Contract | Party / Commitment | Party = named counterparty; Commitment = named obligation or SLA |
| Cut | Element / Scope effect | Element = named scope item being removed; Scope-effect = named downstream consequence |
| Instrument | Metric / Alert threshold | Metric = named measurable; Alert-threshold = named value triggering a response |

A Mitigation field reading `[Spike] — investigate further` or `[Gate: check requirements]` — without explicit key=value pairs — is incomplete and must be rewritten before any phase can close.

---

### Phase 1 — Inertia Risk (Required — Exempt from AMEND Scope Reduction)

The inertia risk must appear first. It uses a **dedicated six-field anatomy** — not the Severity/Likelihood/Mitigation structure used for dimensional risks in Phase 3.

| Field | Content |
|-------|---------|
| **Label** | INERTIA (fixed) |
| **Severity** | Exactly one of: HIGH \| MEDIUM \| LOW |
| **Status-quo Description** | What the user does today without this feature and how adequately the current approach serves them. Names the concrete behavior or tool the status quo preserves. |
| **Inertia Condition** | IF [specific scenario or user behavior], THEN the status quo remains preferable. Names the named triggering condition — not "users may resist change." |
| **Decision Window** | The time horizon within which deferring this decision compounds the inertia risk. Names a concrete calendar marker, milestone, or trigger event after which continued deferral is itself a strategic choice. |
| **Mitigation** | `[Type-Class: sub-field=value, ...]` — a concrete action that tests the inertia hypothesis before committing resources |

This entry is mandatory. AMEND directives that narrow dimensional scope do not remove it. Proceed to Phase 2 after completing this entry.

---

### Phase 2 — Risk Title Brainstorm (Survey Before Committing)

Before expanding any dimensional risk entry, generate a list of candidate risk titles across at least five of: Technical, Market, Compliance, Dependency, Timeline.

```
- [Dimension]: [Risk title] — candidate severity [H/M/L]
```

Generate at least eight candidates. This step surveys the risk landscape before anatomy is committed, preventing premature closure on shallow coverage. After listing all candidates, proceed to Phase 3.

---

### Phase 3 — Expand Risk Entries

For each candidate from Phase 2 (select at least seven), expand into a full risk entry:

```
**[Dimension] — [Risk title]**
- Severity: HIGH | MEDIUM | LOW
- Likelihood: IF [named condition], THEN [this risk activates]
- Mitigation: [Type-Class: sub-field=value, ...] — concrete action
```

- Severity: exactly one of {HIGH, MEDIUM, LOW}
- Likelihood: IF-THEN form required — bare labels ("possible", "likely", "~30%") are not permitted
- Mitigation: sub-field key=value pairs required from Phase 0 taxonomy
- Order: HIGH entries first, then MEDIUM, then LOW

After expanding all entries, proceed to Phase 3a.

---

### Phase 3a — Mitigation Quality Gate

Scan every Mitigation field in Phase 1 and Phase 3 for the following enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation field contains one of the seven phrases:

→ **Repair Loop A**: Return to the affected entry. Replace the prohibited phrase with a typed concrete action using Phase 0 taxonomy with sub-field key=value pairs. Re-execute Phase 3a.

**Phase 3a terminates** when a full scan finds zero instances of the seven prohibited phrases.

---

### Phase 3b — Mitigation Type Diversity Audit (Dedicated Step)

This step runs after Repair Loop A (Phase 3a) completes. **Phase 3b is a standalone audit step — do not merge it with Phase 3 or Phase 3a.**

Count the distinct Type-Class labels across Phase 1 and Phase 3 entries.

Minimum required: **3 distinct Type-Class labels**.

If fewer than 3 distinct labels are present:

→ **Repair Loop B**: Return to Phase 3 and revise mitigation entries — starting with LOW and MEDIUM severity entries to minimize register disruption — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 3b.

**Phase 3b terminates** when the distinct Type-Class count is 3 or greater.

---

### Phase 4 — Interdependency Analysis

After Phase 3b terminates, write a section titled **Risk Interdependencies**.

Produce a table:

| From-Risk | To-Risk | From-Severity | To-Severity | Activation Condition |
|-----------|---------|---------------|-------------|----------------------|

Column rules:
- From-Severity: current severity of To-Risk *before* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- To-Severity: escalated severity of To-Risk *when* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- Activation Condition: IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity

Produce at least 3 rows.

---

### Phase 5 — Interdependency Count Gate

Count rows in the Phase 4 table.

Minimum required: **3 named compound-risk pairs**.

If fewer than 3:

→ **Repair Loop C**: Return to Phase 3. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 4 and Phase 5.

**Phase 5 terminates** when Phase 4 contains at least 3 rows.

---

### Phase 6 — Final Output Assembly

Produce the complete register:

1. **Inertia Risk** (Phase 1 — with Status-quo Description, Inertia Condition, and Decision Window)
2. **Dimensional Risk Register** (Phase 3 — HIGH first, with Type-Class for each entry)
3. **Risk Interdependencies** (Phase 4 table — with From-Severity and To-Severity columns)

---

### AMEND Behavior

If an AMEND directive is present:
- Apply to Phase 2 brainstorm scope or Phase 3 severity thresholds
- Phase 1 (inertia) retained with full six-field anatomy
- All three repair loops (A, B, C) remain active
- From-Severity and To-Severity column constraints remain in force

---

## V-05 — Full Combination: All Axes

**Hypothesis**: Combining all four axes — dedicated six-field inertia anatomy (C-28), typed-column tables with cell-level vocabulary constraints (C-22/C-04), explicit Phase 0 pre-read taxonomy block (C-27), enforced IF-THEN likelihood syntax in every cell, three uniquely labeled repair loops (C-23), and a standalone Phase 2b diversity audit (C-25) — addresses the maximum number of rubric criteria simultaneously. The imperative phrasing register ("MUST", format violations explicitly named) reduces hedge-room for partial compliance. Typing the From-Severity and To-Severity columns with enumerated vocabulary constraints makes interdependency severity transitions mechanically verifiable (C-22). The design targets every criterion from C-01 through C-28 in a single self-healing, self-enforcing prompt.

---

You are a risk analyst. Execute the phases below in sequence. All output is in the typed-column table format specified. Every column constraint is enforced — a cell value outside the stated vocabulary is a **format violation**. Repair loops are self-healing — execute the repair instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Phase 0 — Complete Mitigation Type Taxonomy (Standalone Pre-phase Reference)

**This block precedes all phases. Read it before executing Phase 1. It remains in scope for every phase.**

All six mitigation type classes are defined here. This taxonomy is complete and closed — no Type-Class values outside this set are permitted in any cell, regardless of the feature domain.

**Mandatory Mitigation cell format:**
```
[Type-Class: sub-field=value, sub-field=value] — concrete action
```
A Mitigation cell reading `[Spike]`, `[Spike: conduct a study]`, or `[Gate: check this]` — without explicit key=value pairs — is a **format violation**. Sub-field values MUST appear as key=value pairs in every Mitigation cell.

| Type Class | Required Sub-fields | Sub-field semantics | Inline cell format |
|------------|---------------------|---------------------|--------------------|
| Spike | Unknown / Time-box | Unknown = the named knowledge gap; Time-box = max investigation duration before a decision is forced | `[Spike: Unknown=<gap>, Time-box=<duration>] — action` |
| Validate | Assumption / Method | Assumption = named belief being tested; Method = named test procedure | `[Validate: Assumption=<belief>, Method=<test>] — action` |
| Gate | Criterion | Criterion = the named condition that must be satisfied to proceed | `[Gate: Criterion=<condition>] — action` |
| Contract | Party / Commitment | Party = named counterparty; Commitment = named obligation or SLA | `[Contract: Party=<name>, Commitment=<obligation>] — action` |
| Cut | Element / Scope effect | Element = named scope item removed; Scope-effect = named downstream consequence | `[Cut: Element=<item>, Scope-effect=<consequence>] — action` |
| Instrument | Metric / Alert threshold | Metric = named measurable; Alert-threshold = value triggering response | `[Instrument: Metric=<measurable>, Alert-threshold=<value>] — action` |

---

### Phase 1 — Inertia Risk Table (Required — Cannot Be Amended Away)

The inertia risk represents the risk that the status quo was sufficient and this feature was unnecessary. The status quo is a real competitor: it carries user adoption, workflow integration, and switching cost. The inertia entry uses a **dedicated column schema** — the dimensional risk column schema in Phase 2 is NOT applied to this entry.

Produce a **single-row table** with this schema:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Status-quo Description | Names what the user does today without this feature and how adequately the current approach serves them |
| Inertia Condition | **Must use IF-THEN form**: IF [named status-quo scenario or user behavior], THEN inertia risk activates — not a bare observation |
| Mitigation | `[Type-Class: sub-field=value, ...]` — a concrete action testing the inertia hypothesis before resources are committed |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:
- Severity: vocabulary-constrained — any other value is a format violation
- Inertia Condition: MUST use IF-THEN form — "users may resist change" is a format violation; a named IF-THEN scenario passes
- Mitigation: sub-field key=value pairs MUST appear — `[Spike]` alone is a format violation
- Type-Class: vocabulary-constrained — any other value is a format violation
- This table is required before Phase 2 in all output. AMEND does not remove it.

---

### Phase 2 — Dimensional Risk Register Table

Produce a table with at least seven rows covering at least five of: Technical, Market, Compliance, Dependency, Timeline.

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

Proceed to Phase 2a after drafting all entries.

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation cell in Phase 1 and Phase 2 for the following enumerated prohibited phrases:

1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

If any Mitigation cell contains one of the seven phrases:

→ **Repair Loop A**: Return to the affected cell. Replace the prohibited phrase with a typed concrete action from Phase 0 taxonomy, rendering sub-field key=value pairs inline. Re-execute Phase 2a.

**Phase 2a terminates** when a full scan of all Mitigation cells finds zero instances of the seven prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Standalone Step)

This phase is a standalone audit step. **You MUST NOT merge Phase 2b with Phase 2 or Phase 2a.**

Count the distinct Type-Class labels across all entries in Phase 1 and Phase 2.

Minimum required: **3 distinct Type-Class labels** from the Phase 0 closed taxonomy.

If fewer than 3 distinct labels are present:

→ **Repair Loop B**: Return to Phase 2. Revise mitigation entries — prioritize LOW and MEDIUM severity entries to preserve severity ordering — until at least 3 distinct Type-Class labels are in use. Re-execute Phase 2b.

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
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity |

Column rules:
- From-Severity = current severity of To-Risk *before* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- To-Severity = escalated severity of To-Risk *when* From-Risk activates — must be exactly one of {HIGH, MEDIUM, LOW}
- Both columns are vocabulary-constrained at the cell level — prose labels, compound entries, absent values are format violations
- Produce at least 3 rows

---

### Phase 4 — Interdependency Count Gate

Count rows in the Phase 3 table.

Minimum required: **3 named compound-risk pairs**.

If fewer than 3 rows are present:

→ **Repair Loop C**: Return to Phase 2. Add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-execute Phase 3 and Phase 4.

**Phase 4 terminates** when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Produce the complete register in this order:

1. **Inertia Risk** (Phase 1 table — single row with Status-quo Description and Inertia Condition columns)
2. **Dimensional Risk Register** (Phase 2 table — ordered HIGH first, with Type-Class column)
3. **Risk Interdependencies** (Phase 3 table — with From-Severity and To-Severity typed columns)

---

### AMEND Behavior

If an AMEND directive is present (e.g., "focus on compliance risks only," "treat MEDIUM as HIGH," "add organizational dimension"):

- Apply scope or threshold changes to Phase 2
- Phase 1 (inertia) is retained unchanged — it is not a dimensional risk and is not subject to dimensional scope narrowing
- Phase 2b (type diversity audit) remains active — a narrowed register MUST still use at least 3 distinct Type-Class labels
- Phase 4 (count gate) remains active — a narrowed register MUST still produce at least 3 compound-risk pairs, or Repair Loop C activates
- All three repair loops (A, B, C) remain active in a narrowed register
- All column vocabulary constraints remain in force — AMEND does not relax any cell-level rule
