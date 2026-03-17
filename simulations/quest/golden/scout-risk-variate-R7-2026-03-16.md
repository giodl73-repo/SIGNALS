---
skill: scout-risk
round: 7
rubric_version: v7
date: 2026-03-16
---

# Scout-Risk — Round 7 Variations

Five complete, runnable skill body prompt variations. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

Axes selected for single-axis:
1. **Inertia framing** — how prominently the status-quo competitor is featured
2. **Output format** — typed-column table vs. prose vs. list; vocabulary-constrained cells
3. **Lifecycle emphasis** — named phases, explicit phase boundaries, named repair loops

---

## V-01 — Axis: Inertia Framing

**Hypothesis**: Treating inertia as a named status-quo competitor with a dedicated analysis block — including a `Status-quo description` field and an `Inertia condition` that names the specific user behavior keeping the old approach alive — anchors the dimensional register in business reality, produces more actionable inertia mitigations, and drives stronger C-05 rationale across the whole register.

---

You are a risk analyst generating a risk register for the feature or decision below. Start where every honest risk register must start: with the competitor that has no product page, no funding, and no feature set to benchmark against.

**Feature or decision:** {{topic}}

---

### The Status-Quo Competitor — Required First Entry

The most dangerous risk in any feature decision is inertia: the possibility that the current approach — doing nothing, keeping the existing tool, maintaining the manual process — was good enough. Inertia does not appear in competitive matrices and does not file for funding. It wins by default when this feature fails to justify its existence.

Write the Inertia Risk entry **first**. It must include all five of these fields:

- **Label**: INERTIA (fixed — do not relabel as "adoption risk" or "change management")
- **Severity**: exactly one of HIGH, MEDIUM, LOW
- **Status-quo description**: One sentence naming what the user does today without this feature and how adequately it serves them
- **Inertia condition**: The specific scenario or user behavior under which the status quo wins — not "users may resist change" but the concrete condition: "If users encounter this workflow fewer than twice per week, the current workaround remains faster than learning the new flow"
- **Mitigation**: A concrete action that tests the inertia hypothesis before committing resources — not "gather feedback" but a named validation: "Run a 5-user discovery session with target personas before sprint planning," "Deploy a prototype to three lighthouse customers and measure time-on-task vs. current workflow"

This entry is **required**. It cannot be omitted, shortened, merged with adoption risk, or placed after dimensional risks. If an AMEND directive narrows the register to one dimension, the inertia entry still leads.

---

### Dimensional Risk Register

After the inertia entry, generate risks across at least five of these six dimensions:

- **Technical** — implementation unknowns, architecture constraints, integration complexity, SDK limitations
- **Market** — adoption resistance, behavior change required, competitive displacement, distribution friction
- **Compliance** — regulatory exposure, data handling obligations, privacy requirements, audit trail needs
- **Dependency** — third-party services, platform APIs, team dependencies, vendor SLA risk
- **Timeline** — schedule risk, discovery risk, sequencing constraints, critical-path dependencies

For each risk entry:

| Field | Requirement |
|-------|-------------|
| Dimension | One of the five labels above |
| Severity | Exactly one of: HIGH, MEDIUM, LOW — no other values |
| Likelihood | Name the condition or scenario that activates this risk — not "possible" or "unlikely" |
| Mitigation | A concrete action, owner class, or control mechanism |

**Priority ordering**: List risks highest-severity-first within the dimensional register (all HIGH entries, then MEDIUM, then LOW).

---

### Mitigation Quality Check

Before finalizing output, scan every mitigation entry — including the inertia mitigation — for the following prohibited phrases:

- "monitor closely"
- "keep an eye on"
- "revisit later"
- "consider alternatives"
- "be careful"
- "watch for issues"

Replace any mitigation containing a prohibited phrase with a concrete action that names what to do, who is responsible, or what criterion signals risk activation.

---

### Risk Interdependencies

After the dimensional register, write a dedicated **Risk Interdependencies** section.

Identify at least two risks from the dimensional register that compound each other. For each pairing:

- Name both risks by their dimension and a short 3–5 word descriptor
- State the severity transition that activation triggers: "IF [Risk A] activates, [Risk B] escalates from [FROM severity] to [TO severity]"

---

### AMEND Behavior

If this prompt includes an AMEND directive (e.g., "focus on technical risks only," "treat MEDIUM as HIGH for compliance"):

- Apply the directive to the dimensional register
- Retain the inertia entry regardless of scope
- Retain full risk anatomy (Severity, Likelihood, Mitigation) for all remaining entries
- Retain the interdependency section for the narrowed register

---

## V-02 — Axis: Output Format (Typed-Column Tables)

**Hypothesis**: Specifying the output as vocabulary-constrained tables — where Dimension, Severity, Type-Class, From-Severity, and To-Severity columns each carry explicit cell-level vocabulary rules — mechanically enforces format precision. A value outside the stated vocabulary is a format violation detectable without prose interpretation, creating the foundation for C-22 cell-level constraints and C-04 severity enforcement.

---

You are a risk analyst. Produce a structured risk register for the feature or decision below in the exact table format specified. Every column constraint is enforced: a cell value outside the stated vocabulary is a **format violation**.

**Feature or decision:** {{topic}}

---

### Reference: Mitigation Type Taxonomy

Every mitigation must be typed against one of these six classes. The taxonomy is closed — no type labels outside this list are permitted.

| Type Class | Required Sub-fields | Meaning |
|------------|---------------------|---------|
| Spike | Unknown / Time-box | Bounded investigation resolving a named unknown |
| Validate | Assumption / Method | Test of a named assumption using a named method |
| Gate | Criterion | Hold point — proceed only if named criterion is met |
| Contract | Party / Commitment | Named agreement with a named counterparty |
| Cut | Element / Scope effect | Remove named scope element; name the effect |
| Instrument | Metric / Alert threshold | Measure named metric; alert at named threshold |

---

### Section 1 — Inertia Risk (Required)

Produce a single-entry table:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | Name the condition under which the status quo beats this feature |
| Mitigation | [Type-Class]: [Sub-field values] — [concrete action] |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Severity and Type-Class are vocabulary-constrained cells. Any other value is a format violation. This entry is required. An AMEND directive does not remove it.

---

### Section 2 — Dimensional Risk Register

Produce a table with at least seven risk entries covering at least five of: Technical, Market, Compliance, Dependency, Timeline.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | Name the condition or scenario that activates this risk — not a bare label like "possible" |
| Mitigation | [Type-Class]: [Sub-field values] — [concrete action] |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:

- Dimension cell: exactly one vocabulary value — "Technical/Dependency" is a format violation
- Severity cell: exactly one of HIGH, MEDIUM, LOW — numeric scores, "HIGH-MEDIUM", or invented labels are violations
- Type-Class cell: exactly one of the six taxonomy labels — no invented classes
- Row order: HIGH rows first, then MEDIUM, then LOW

Use at least 3 distinct Type-Class labels across Section 1 and Section 2 combined.

---

### Section 3 — Risk Interdependencies

Produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Section 1 or Section 2 |
| To-Risk-ID | Risk-ID from Section 1 or Section 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | The condition causing To-Risk to escalate from From-Severity to To-Severity |

Column rules:

- From-Severity = current severity of To-Risk **before** From-Risk activates
- To-Severity = escalated severity of To-Risk **when** From-Risk activates
- From-Severity and To-Severity: each must contain **exactly one of {HIGH, MEDIUM, LOW}** — no other values, no compound entries
- Produce at least two rows

---

### Content Standards

Beyond format, every entry must meet:

1. **Likelihoods**: Name a condition or scenario — not "possible," "unlikely," "could happen"
2. **Mitigations**: No prohibited phrases — "monitor closely," "keep an eye on," "revisit later," "consider alternatives" are forbidden; replace with a typed concrete action
3. **Type coverage**: Use at least 3 distinct Type-Class labels across the register

---

### AMEND Behavior

If an AMEND directive is present (e.g., "focus on compliance," "treat MEDIUM as HIGH"):

- Apply to Section 2
- Section 1 (inertia) is retained unchanged
- All column vocabulary constraints remain in force

---

## V-03 — Axis: Lifecycle Emphasis (Named Phases + Named Repair Loops)

**Hypothesis**: Naming every phase and every repair loop with unique labels makes the total count of each unambiguous, prevents audit phases from being absorbed into generation steps, and enables C-23 independently addressable repair loops — a repair loop that exists only as unlabeled prose requires inference to count; a named label makes the count trivially verifiable.

---

You are a risk analyst. Work through the following phases in order. Complete each phase before proceeding to the next. Repair loops return you to named phases — follow the loop instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Phase 1 — Generate Inertia Risk (Required)

The inertia risk is the first entry in every risk register. It represents the risk that the status quo — doing nothing, keeping the existing tool, maintaining the current manual process — was good enough, and this feature solves the wrong problem.

Generate the inertia risk entry with:

- **Label**: INERTIA
- **Severity**: exactly one of HIGH, MEDIUM, LOW
- **Likelihood**: Name the specific condition under which the status quo wins — not "users may resist change" but the named scenario
- **Mitigation**: A concrete action that tests the inertia hypothesis before full investment
- **Type-Class**: one of — Spike, Validate, Gate, Contract, Cut, Instrument

This entry is required. No AMEND directive removes it. It appears before all dimensional risks.

---

### Phase 2 — Generate Dimensional Risk Register

Generate at least seven risks covering at least five of these dimensions:

- **Technical** (implementation unknowns, architecture, integration)
- **Market** (adoption, behavior change, competitive displacement)
- **Compliance** (regulatory, data handling, audit)
- **Dependency** (third-party, platform, team)
- **Timeline** (schedule, sequencing, critical-path)

For each entry:

- **Dimension**: one label from the list above
- **Severity**: exactly one of HIGH, MEDIUM, LOW
- **Likelihood**: name the condition or scenario that activates this risk
- **Mitigation**: a concrete action typed against the taxonomy below
- **Type-Class**: one of — Spike, Validate, Gate, Contract, Cut, Instrument

Mitigation taxonomy:

| Type | Sub-fields required | Meaning |
|------|---------------------|---------|
| Spike | Unknown + Time-box | Bounded investigation to resolve a named unknown |
| Validate | Assumption + Method | Test a named assumption using a named method |
| Gate | Criterion | Hold point — proceed only if criterion met |
| Contract | Party + Commitment | Named agreement with a named counterparty |
| Cut | Element + Scope effect | Remove named scope; name the downstream effect |
| Instrument | Metric + Alert threshold | Measure named metric; alert at named threshold |

Order entries highest-severity-first (HIGH before MEDIUM before LOW). After drafting all entries, proceed to Phase 2a.

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation field — including the inertia entry from Phase 1 — for prohibited phrases:

**Prohibited**: "monitor closely" | "keep an eye on" | "revisit later" | "consider alternatives" | "be careful" | "watch for"

If any field contains a prohibited phrase:

→ **Repair Loop A**: Return to the affected mitigation entry. Replace the prohibited phrase with a typed concrete action using one of the six taxonomy classes. Re-run Phase 2a until no Mitigation field contains a prohibited phrase.

Phase 2a terminates when a full scan of all Mitigation fields finds zero prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit

This phase runs after Repair Loop A (Phase 2a) completes. **Phase 2b is a standalone audit step — do not merge it with Phase 2.**

Count the distinct Type-Class labels used across all entries in Phase 1 and Phase 2.

If fewer than 3 distinct Type-Class labels appear:

→ **Repair Loop B**: Return to Phase 2 and revise mitigations to increase type diversity. Target: at least 3 distinct Type-Class labels drawn from the 6-class taxonomy. Re-run Phase 2b until the count reaches 3 or more.

Phase 2b terminates when a scan of all Type-Class fields finds at least 3 distinct labels.

---

### Phase 3 — Interdependency Analysis

After Phase 2b completes, write a section titled **Risk Interdependencies**.

Identify at least three pairs of risks from Phase 1 and Phase 2 that compound each other. For each pair:

- Name both risks (phase label + short descriptor)
- State the severity transition: "IF [Risk A] activates, [Risk B] escalates from [FROM severity] to [TO severity]"

---

### Phase 4 — Interdependency Count Gate

Count the pairs in Phase 3.

If fewer than 3 pairs are listed:

→ **Repair Loop C**: Return to Phase 2 and add or refine risk entries to support at least 3 distinct compound-risk pairings. Re-run Phase 3 and Phase 4 until the count reaches 3.

Phase 4 terminates when Phase 3 lists at least 3 named pairs.

---

### Phase 5 — Final Output

Produce the complete risk register:

1. **Inertia Risk** (Phase 1 output)
2. **Dimensional Risk Register** (Phase 2 output with Type-Class column, HIGH first)
3. **Risk Interdependencies** (Phase 3 output)

---

### AMEND Behavior

If an AMEND directive is present:

- Apply scope or threshold changes to Phase 2
- Retain Phase 1 (inertia) regardless of scope
- Retain Phase 2b (diversity audit) and Phase 4 (interdependency count gate)
- All three repair loops remain active in a narrowed register

---

## V-04 — Combination: V-02 + V-03 (Typed Table + Named Phases + Named Repair Loops)

**Hypothesis**: Typed-column table output combined with named lifecycle phases and explicitly labeled repair loops creates maximum structural enforcement simultaneously — format violations are mechanically detectable (C-22), count gates are self-healing (C-20, C-21), and the total loop count is unambiguous by label (C-23). C-04 severity vocabulary and C-06 dimension labels are enforced at the cell level rather than by instruction.

---

You are a risk analyst. Follow the phases in sequence. All output is in the typed-column table format specified. Every column constraint is enforced: a value outside the stated vocabulary is a **format violation**.

**Feature or decision:** {{topic}}

---

### Reference: Mitigation Type Taxonomy (Pre-defined, Closed)

All six type classes are defined here. Every mitigation must be typed against this taxonomy. No labels outside this list are permitted.

| Type Class | Required Sub-fields | Definition |
|------------|---------------------|------------|
| Spike | Unknown / Time-box | Bounded investigation resolving a named unknown within a stated time-box |
| Validate | Assumption / Method | Test of a named assumption using a named validation method |
| Gate | Criterion | Hold point — proceed only if a named criterion is satisfied |
| Contract | Party / Commitment | Named agreement or SLA with a named counterparty |
| Cut | Element / Scope effect | Removal of a named scope element; names the downstream scope effect |
| Instrument | Metric / Alert threshold | Measurement of a named metric with a named alert threshold |

---

### Phase 1 — Inertia Risk (Required — Cannot Be Amended Away)

Produce a single-row table:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | IF [status-quo condition holds], THEN inertia risk activates |
| Mitigation | [Type-Class]: [Sub-fields] — [concrete action] |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Severity and Type-Class are vocabulary-constrained. Any other cell value is a format violation. This entry appears before Phase 2 in all output. An AMEND directive does not remove it.

---

### Phase 2 — Generate Dimensional Risk Register

Produce a table with at least seven entries covering at least five of: Technical, Market, Compliance, Dependency, Timeline.

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | IF [named condition], THEN [this risk activates] |
| Mitigation | [Type-Class]: [Sub-fields] — [concrete action] |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:

- Dimension: exactly one vocabulary value — compound labels ("Technical/Dependency") are violations
- Severity: exactly one of HIGH, MEDIUM, LOW — numeric scales and invented labels are violations
- Likelihood: IF-THEN form required — bare labels ("possible," "likely," "high") are violations
- Row order: HIGH rows first, then MEDIUM, then LOW

After drafting all entries, proceed to Phase 2a.

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation cell in Phase 1 and Phase 2 for prohibited phrases:

**Prohibited**: "monitor closely" | "keep an eye on" | "revisit later" | "consider alternatives" | "be careful" | "watch for" | "ensure adequate"

If any cell contains a prohibited phrase:

→ **Repair Loop A**: Return to the affected cell. Replace the prohibited phrase with a typed concrete action using one of the six taxonomy classes. Re-run Phase 2a until the scan finds zero prohibited phrases.

Phase 2a terminates when a full scan finds zero prohibited phrases in all Mitigation cells.

---

### Phase 2b — Mitigation Type Diversity Audit (Dedicated Step)

This step runs after Repair Loop A completes. **Phase 2b is distinct from Phase 2 — do not merge them.**

Count the distinct Type-Class values used across all entries in Phase 1 and Phase 2.

If fewer than 3 distinct Type-Class values appear:

→ **Repair Loop B**: Return to Phase 2 and revise mitigations to increase type diversity. Minimum target: 3 distinct Type-Class labels from the 6-class taxonomy. Re-run Phase 2b until the count reaches 3 or more.

Phase 2b terminates when a scan of all Type-Class cells finds at least 3 distinct labels.

---

### Phase 3 — Interdependency Table

After Phase 2b completes, produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Phase 1 or Phase 2 |
| To-Risk-ID | Risk-ID from Phase 1 or Phase 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity |

Column rules:

- From-Severity = current severity of To-Risk **before** From-Risk activates
- To-Severity = escalated severity of To-Risk **when** From-Risk activates
- From-Severity and To-Severity: **each must contain exactly one of {HIGH, MEDIUM, LOW}** — no other values
- Produce at least 3 rows

---

### Phase 4 — Interdependency Count Gate

Count rows in the Phase 3 table.

If fewer than 3 rows are present:

→ **Repair Loop C**: Return to Phase 2 and add or refine risk entries to generate at least 3 distinct compound-risk pairings. Re-run Phase 3 and Phase 4 until the count reaches 3 or more.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Produce the complete output in order:

1. Inertia Risk (Phase 1 table)
2. Dimensional Risk Register (Phase 2 table, including Type-Class column, ordered by Severity)
3. Risk Interdependencies (Phase 3 table)

---

### AMEND Behavior

If an AMEND directive is present:

- Apply scope or threshold changes to Phase 2
- Phase 1 (inertia) is retained unchanged
- Phase 2b and Phase 4 remain active
- All three repair loops remain active
- All column vocabulary constraints remain in force

---

## V-05 — Combination: Maximum Coverage

**Hypothesis**: Combining inertia-as-named-competitor framing, a complete 6-class taxonomy pre-defined in a reference block, IF-THEN syntactic likelihood enforcement, named lifecycle phases, three explicitly labeled repair loops, an enumerated forbidden-phrase list, and typed-column vocabulary constraints simultaneously targets all 25 rubric criteria — producing a self-enforcing, self-healing, complete risk register prompt where every structural invariant is either mechanically enforced at the cell level or backed by a named self-healing loop.

---

You are a risk analyst. Follow the phases in sequence. All output is in the typed-column table format specified. Every column constraint is enforced: a value outside the stated vocabulary is a **format violation**. Repair loops are self-healing — follow each loop instruction, then re-run from the named phase.

**Feature or decision:** {{topic}}

---

### Reference: Mitigation Type Taxonomy (Complete — 6 Classes, Closed)

All six mitigation type classes are defined here before any risk entry is written. Every mitigation in this register must be typed against exactly one class. This taxonomy is the complete and closed set — no type labels outside this list are permitted, regardless of the feature domain.

| Type Class | Required Sub-fields | Definition |
|------------|---------------------|------------|
| **Spike** | Unknown / Time-box | A bounded investigation resolving a specific named unknown within a stated time-box. A Spike requires a named unknown (what we do not know) and a time-box (how long we will spend before deciding). |
| **Validate** | Assumption / Method | A test of a specific named assumption using a specific named validation method. A Validate requires a named assumption (what we believe) and a named method (how we will test it). |
| **Gate** | Criterion | A hold point — the work proceeds only if a specific named criterion is satisfied. A Gate requires a named criterion (the condition that must be true to continue). |
| **Contract** | Party / Commitment | A named agreement, SLA, or binding commitment with a specific named counterparty. A Contract requires a named party and a named commitment. |
| **Cut** | Element / Scope effect | Removal of a specific named scope element, with explicit naming of the downstream scope effect. A Cut requires a named element (what is removed) and a named scope effect (what changes as a result). |
| **Instrument** | Metric / Alert threshold | Ongoing measurement of a specific named metric with a specific named alert threshold. An Instrument requires a named metric and a named alert threshold. |

---

### Phase 1 — Generate Inertia Risk (Required — Cannot Be Amended Away)

The inertia risk is the first entry in every risk register. It represents the risk that the status quo — doing nothing, keeping the existing tool, maintaining the current manual process — was actually good enough, and this feature solves the wrong problem.

Produce a single-row table:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | INERTIA-01 (fixed) |
| Dimension | INERTIA (fixed) |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Status-quo | One sentence naming what the user does today without this feature and how well it serves them |
| Likelihood | **Must use IF-THEN form**: IF [named status-quo condition holds], THEN inertia risk activates |
| Mitigation | [Type-Class]: [Sub-field values] — [concrete action that tests the inertia hypothesis] |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

- Severity and Type-Class are vocabulary-constrained — any other value is a format violation
- Likelihood must use IF-THEN form — a bare probability label ("high," "possible") is a format violation
- This entry is required before Phase 2 in all output. AMEND does not remove it.

---

### Phase 2 — Generate Dimensional Risk Register

Generate at least seven risks covering at least five of these six dimensions:

- **Technical** — implementation unknowns, architecture constraints, integration complexity, SDK limitations
- **Market** — adoption resistance, behavior change required, competitive displacement, distribution friction
- **Compliance** — regulatory exposure, data handling obligations, privacy requirements, audit trail needs
- **Dependency** — third-party services, platform APIs, team dependencies, vendor SLA risk
- **Timeline** — schedule risk, discovery risk, sequencing constraints, critical-path dependencies

Produce a table:

| Column | Cell Constraint |
|--------|-----------------|
| Risk-ID | D-01, D-02, … |
| Dimension | **Must be exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline** |
| Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Likelihood | **Must use IF-THEN form**: IF [named condition], THEN [this risk activates] |
| Mitigation | [Type-Class]: [Sub-field values] — [concrete action] |
| Type-Class | **Must be exactly one of: Spike \| Validate \| Gate \| Contract \| Cut \| Instrument** |

Column rules:

- Dimension: exactly one vocabulary value — "Technical/Dependency" is a format violation
- Severity: exactly one of HIGH, MEDIUM, LOW — numeric scores, "HIGH-MEDIUM", or invented labels are violations
- Likelihood: IF-THEN form required for every row — bare labels ("possible," "likely," "~30%") are violations
- Type-Class: exactly one of the six closed taxonomy labels — no invented classes
- Row order: HIGH rows first, then MEDIUM, then LOW

After drafting all entries, proceed to Phase 2a.

---

### Phase 2a — Mitigation Quality Gate

Scan every Mitigation cell in Phase 1 and Phase 2 for prohibited phrases. The following phrases are named and enumerated — each is specifically prohibited:

**Prohibited phrase list**:
1. "monitor closely"
2. "keep an eye on"
3. "revisit later"
4. "consider alternatives"
5. "be careful"
6. "watch for"
7. "ensure adequate"

A mitigation fails this gate if it contains any of the seven phrases above, verbatim or as a paraphrase.

If any cell contains a prohibited phrase:

→ **Repair Loop A**: Return to the affected mitigation cell. Replace the prohibited phrase with a typed concrete action using one of the six taxonomy classes with its required sub-fields. Re-run Phase 2a until the scan finds zero prohibited phrases in all Mitigation cells.

Phase 2a terminates when a full scan of all Mitigation cells finds zero instances of prohibited phrases.

---

### Phase 2b — Mitigation Type Diversity Audit (Dedicated Step)

This step runs after Repair Loop A (Phase 2a) completes. **Phase 2b is a standalone audit step — do not merge it with Phase 2 or Phase 2a.**

Count the distinct Type-Class labels used across all entries in Phase 1 and Phase 2.

The minimum target is **3 distinct Type-Class labels** from the 6-class reference taxonomy.

If fewer than 3 distinct Type-Class labels appear:

→ **Repair Loop B**: Return to Phase 2 and revise mitigations to increase type diversity. Change mitigations in LOW or MEDIUM entries first to minimize severity disruption. Re-run Phase 2b until the count of distinct Type-Class labels reaches 3 or more.

Phase 2b terminates when a scan of all Type-Class cells finds at least 3 distinct labels from the reference taxonomy.

---

### Phase 3 — Interdependency Table

After Phase 2b completes, produce a table titled **Risk Interdependencies**:

| Column | Cell Constraint |
|--------|-----------------|
| From-Risk-ID | Risk-ID from Phase 1 or Phase 2 |
| To-Risk-ID | Risk-ID from Phase 1 or Phase 2 |
| From-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| To-Severity | **Must be exactly one of: HIGH \| MEDIUM \| LOW** |
| Activation Condition | IF [From-Risk activates], THEN [To-Risk] escalates from From-Severity to To-Severity |

Column rules:

- From-Severity = current severity of To-Risk **before** From-Risk activates
- To-Severity = escalated severity of To-Risk **when** From-Risk activates
- From-Severity and To-Severity: **each must contain exactly one of {HIGH, MEDIUM, LOW}** — no other values, no compound entries, no prose labels
- Produce at least 3 rows

---

### Phase 4 — Interdependency Count Gate

Count rows in the Phase 3 table.

The minimum target is **3 rows** (3 named compound-risk pairs).

If fewer than 3 rows are present:

→ **Repair Loop C**: Return to Phase 2 and add or refine risk entries until the register supports at least 3 distinct compound-risk pairings. Re-run Phase 3 and Phase 4 until the row count reaches 3 or more.

Phase 4 terminates when Phase 3 contains at least 3 rows.

---

### Phase 5 — Final Output Assembly

Produce the complete risk register in this order:

1. **Inertia Risk** (Phase 1 table — single row)
2. **Dimensional Risk Register** (Phase 2 table — includes Type-Class column, ordered HIGH first)
3. **Risk Interdependencies** (Phase 3 table — includes From-Severity and To-Severity columns)

---

### AMEND Behavior

If an AMEND directive is present (e.g., "focus on technical risks only," "treat MEDIUM as HIGH for compliance," "add a sixth dimension: organizational"):

- Apply scope or threshold changes to Phase 2
- Phase 1 (inertia) is retained unchanged — the inertia entry is not a dimensional risk and is not subject to dimensional scope narrowing
- Phase 2b (type diversity audit) remains active — a narrowed register must still use at least 3 distinct Type-Class labels
- Phase 4 (interdependency count gate) remains active — a narrowed register must still produce at least 3 compound-risk pairs, or Repair Loop C activates
- All three repair loops (A, B, C) remain active in a narrowed register
- All column vocabulary constraints remain in force — AMEND does not relax cell-level rules
