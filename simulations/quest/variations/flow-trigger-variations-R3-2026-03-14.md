Here are the 5 R3 variations:

---

## Summary

| ID | Axis | Primary Target | Predicted Score |
|----|------|---------------|-----------------|
| **V-01** | Output format — `REGISTRY.M` named variable code-fence | C-12 | ~98 (C-13 FAIL) |
| **V-02** | Lifecycle emphasis — BUDGET STEP A sub-table before STEP B | C-13 | ~98 (C-12 FAIL) |
| **V-03** | Role sequence — Registry / Budget / Pathology analysts | C-04 depth | ~96 (C-12/C-13 RISK) |
| **V-04** | Combined: output format + lifecycle emphasis | C-12 + C-13 co-satisfied | 100 |
| **V-05** | Combined: all four axes (R3 golden) | All 13 criteria structurally enforced | 100 |

---

**Key structural innovations:**

**C-12 fix (V-01, V-04, V-05):** R2 V-04 had a registry code block but downstream sections re-derived M in prose. R3 introduces named variable identifiers — `REGISTRY.M`, `REGISTRY.N`, `REGISTRY.SideEffectAutomations` — with mandatory downstream reference syntax. If the budget gate says `REGISTRY.M = ___ [from §2b code block — do not derive independently]`, any inconsistency is structurally detectable.

**C-13 fix (V-02, V-04, V-05):** R2's "Show calculation basis" was a prose template hint. R3 introduces BUDGET STEP A (per-automation sub-table, one row per automation in `REGISTRY.SideEffectAutomations`, row count = REGISTRY.M) which must complete before BUDGET STEP B (aggregate derived from STEP A rows). Aggregate totals are never asserted — they are derived.

**C-12 + C-13 cross-reference (V-04, V-05):** `REGISTRY.SideEffectAutomations` names the side-effect automations; STEP A row count must equal `REGISTRY.M`. This links the code block to the budget arithmetic — discrepancies between the two are verifiable.
ng the per-automation breakdown a separate named
  sub-table (BUDGET STEP A) that must be completed before the aggregate (BUDGET STEP B) is written.

- **C-12 + C-13 cross-reference**: `REGISTRY.SideEffectAutomations` names the automations with
  side effects; BUDGET STEP A must have exactly one row per name. Row count = REGISTRY.M. This
  creates a machine-verifiable cross-reference between C-12 and C-13 outputs.

- **V-03 is the structural risk**: Specialist-role handoff improves C-04 and C-06 depth but does
  not mandate the code-fence format (C-12) or the two-step budget lifecycle (C-13). Tests whether
  role clarity produces incidental coverage of the new criteria.

- **Golden candidates: V-04 and V-05.** V-04 is the minimal mechanism proof (C-12+C-13 without
  threat-lead complexity). V-05 adds threat-first Phase 1 from R2 V-05 for maximum C-04/C-05 depth.

---

## V-01 — Single Axis: Output Format (Registry Code Block as Named Variable System)

**Axis**: Output format — the registry summary is a strict code-fence with canonical named
identifiers (`REGISTRY.M`, `REGISTRY.N`, `REGISTRY.NonFiring`, `REGISTRY.SideEffectAutomations`);
every downstream section that uses these counts references them by name from the code block; the
budget gate section opens by reading `REGISTRY.M` explicitly rather than re-deriving from the table.

**Hypothesis**: R2 V-04 placed a registry summary code block after the table but did not require
downstream sections to reference its values by identifier. A model can write `M = 4` in the code
block and later write `Gate: M = 4 (counted from table)` in the budget section — making the two M
values independently derived rather than structurally linked. By requiring the budget gate to state
`REGISTRY.M = [value from §2b code block]`, any inconsistency between the code block and downstream
usage is structurally detectable. This tests C-12 in isolation without adding C-13's per-automation
sub-table.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

Follow this exact sequence. Each section feeds the next by named variable reference. Do not reorder.

---

## SECTION 1 — SCENARIO

| Field | Value |
|-------|-------|
| Table | [Dataverse entity schema name] |
| Change type | [field update / record create / delete / status change / custom event] |
| Field changed | [schema name — e.g., cr123_statuscode] |
| Old value | [prior state or "N/A — create/delete event"] |
| New value | [new state or "N/A — create/delete event"] |
| Solution layer | [Default / Managed / Unmanaged — or "inferred: SOURCE"] |
| Environment | [Dev / Test / UAT / Production — or "inferred"] |
| License tier | [per-user premium / per-flow / pay-as-you-go — or "assumed: TIER"] |

---

## SECTION 2 — UNIFIED TRIGGER REGISTRY

This section produces two outputs: (a) the trigger table and (b) the registry summary code block.
Both are required. The code block is the canonical variable source for all downstream sections.
Supplemental trigger lists are prohibited anywhere in the output.

### 2a — Trigger Table

Include every automation registered for this entity and event — firing AND non-firing — in one table.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

Column enforcement:
- **Fires?**: `YES` or `NO`. Every registered automation appears as exactly one row. No row may
  omit this column.
- **#**: Integer firing-sequence for YES rows (1, 2, 3…). `--` for NO rows.
- **Type**: `Cloud Flow` / `Dataverse Plugin` / `Business Rule` / `Copilot Studio Topic` / `Other`
- **Condition Expression**: required for all rows.
  - YES unconditional: `"No trigger filter — always fires on [event type] for [entity]"`
  - YES conditional: OData expression that evaluated true (e.g., `cr123_priority eq 2`)
  - NO rows: exact expression that evaluated false; `N/A` is not acceptable
- **Sync/Async**: `Sync` (pre-commit) / `Async` (post-commit) for YES rows; `--` for NO rows
- **Inputs**: YES rows: concrete values (field schema name, OData token, record ID pattern);
  `--` for NO rows
- **Outputs**: YES rows: concrete state changes (field written, entity created, endpoint called,
  message type); `--` for NO rows
- **Side Effects**: YES rows: specific external state changes (target table schema name, recipient
  role, API hostname, audit log name) or `none`; `--` for NO rows

### 2b — Registry Summary Code Block

Write this code block immediately after the table. This is the canonical variable declaration.
All downstream sections reference M, N, and automation names from this block — not from the table.

```registry
REGISTRY.M                      = [count of YES rows where Side Effects != "none"]
REGISTRY.N                      = [count of all YES rows — total firing triggers]
REGISTRY.NonFiring              = [count of NO rows]
REGISTRY.SideEffectAutomations  = [comma-separated YES-row names with Side Effects != "none", or "none"]
```

---

## SECTION 3 — BUDGET GATE (runs before pathology — mandatory)

Gate condition: `REGISTRY.M >= 3`

Read REGISTRY.M from §2b. Do not recount from the trigger table.

```gate
REGISTRY.M  = ___  [value from §2b — do not derive independently]
Gate MET    = YES / NO
```

**If gate NOT MET:**

> Budget gate NOT triggered: REGISTRY.M = [§2b value] (fewer than 3 side-effect automations fire).

Proceed to Section 4.

**If gate MET** — complete the budget table. "Unknown" is not acceptable; state estimation
assumptions in one sentence below the table.

| Budget Metric | Estimate | Calculation Basis |
|---------------|----------|-------------------|
| Side-effect trigger count M | [REGISTRY.M from §2b] | §2b code block |
| Total firing triggers N | [REGISTRY.N from §2b] | §2b code block |
| Estimated API requests per occurrence | [integer or range] | [per-automation: Flow A = X, Plugin B = Y; total = X+Y+…] |
| Power Platform daily request limit | [limit] | License tier from §1 |
| Budget consumed per occurrence (%) | [(requests/limit)×100] | Arithmetic above |
| Estimated run duration — sync path | [estimate] | Sync YES rows from §2a |
| Estimated run duration — async path | [estimate] | Longest async path from §2a |

Estimation assumptions: [one sentence]

---

## SECTION 4 — PATHOLOGY DETECTION

Reference automations by name from §2a. This section runs after §3.

| Pathology | Verdict | Evidence | Remediation |
|-----------|---------|----------|-------------|
| **Trigger Storm** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Missing Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Circular Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |

Evidence for PRESENT/RISK: full cascade trace — "[Automation A] output [field X = value] →
[Automation B] fires on condition [field X changed] → [B] output creates [entity Y] →
[Automation C] fires on [entity Y create]…"

Evidence for ABSENT: name the specific guard present — not "no issues found."

Remediation for PRESENT/RISK:
- PA: `Add trigger condition to [Flow Name]: @not(equals(triggerOutputs()?['body/FIELDNAME'], VALUE))`
- Plugin: `if (context.Depth > 1) return;` at entry of [PluginClass.OnExecute]
- Copilot Studio: condition node `[System.Activity.Name] is not equal to "Automated"` in [TopicName]

---

## SECTION 5 — SUMMARY

Two sentences: REGISTRY.N of (REGISTRY.N + REGISTRY.NonFiring) registered automations fired;
budget gate result (REGISTRY.M); pathology verdicts. One recommended action if any verdict is
PRESENT or RISK.

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: `skill`, `topic`, `date`, `REGISTRY.M`, `REGISTRY.N`, `REGISTRY.NonFiring`,
`budget_gate_fired` (boolean), `pathologies_found` (list), `license_tier`.
```

---

## V-02 — Single Axis: Lifecycle Emphasis (Per-Automation Calculation as Explicit Phase)

**Axis**: Lifecycle emphasis — the budget section has two mandatory, sequenced sub-steps: BUDGET
STEP A produces a per-automation breakdown sub-table with one row per side-effect automation and
columns for each action category; BUDGET STEP B derives the aggregate total from STEP A's row
totals. STEP B must not begin before STEP A is complete. The aggregate total is never asserted
directly — it is always the arithmetic sum of STEP A rows.

**Hypothesis**: R2 V-02 appended "Show calculation basis: Flow A calls N Dataverse actions + M
connector actions = X requests" as a prose template after the budget table. A model can write a
plausible aggregate total without producing per-automation rows if the template is treated as
optional. By splitting the budget section into two explicitly named sequential steps — STEP A
(sub-table, one row per automation) then STEP B (aggregate derived from STEP A) — the model is
structurally blocked from writing STEP B until STEP A exists. If STEP A rows are incomplete, the
STEP B totals are verifiably wrong against the rows.

**Note**: This variation does NOT use the strict registry code block with named variable identifiers
(C-12). The registry summary uses an informal prose format — identical to R2 V-02. This tests the
C-13 mechanism in isolation.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

Execute these sections in order. Do not skip a section. Do not reorder.

---

## SECTION 1 — SCENARIO DECLARATION

State precisely:
- Table: [entity schema name]
- Event: [field update / record create / delete / status change / custom event]
- Field: [schema name] — [old value] to [new value]
- Solution layer: [Default / Managed / Unmanaged — or "inferred from: SOURCE"]
- Environment: [Dev / Test / Production — or "inferred"]
- License tier: [plan — or "assumed: TIER; basis: REASON"]

---

## SECTION 2 — TRIGGER REGISTRY

Enumerate every automation registered for this entity and event. Include both firing and non-firing.
One table only — no supplemental trigger lists anywhere in the output.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

- **Fires?**: `YES` or `NO`. Every registered automation must appear; no row may omit this column.
- **#**: Firing sequence integer for YES rows. `--` for NO rows.
- **Condition Expression**: required for all rows. "No filter — always fires on [event type]" is
  valid for unconditional YES. NO rows: state the expression that evaluated false; `N/A` is not
  acceptable.
- **Sync/Async**: for YES rows only; `--` for NO.
- **Inputs/Outputs**: concrete values for YES rows; `--` for NO.
- **Side Effects**: external state changes for YES rows (with specifics: table name, role, API
  hostname) or `none`; `--` for NO.

Registry summary (write after table):

  M (YES rows with Side Effects != "none") = ___
  N (total YES rows)                       = ___
  Non-firing (NO rows)                     = ___
  Automations with side effects: [comma-separated names, or "none"]

---

## SECTION 3 — BUDGET GATE (runs before pathology — mandatory)

Gate condition: M >= 3 (from registry summary above)

Check:
  M        = ___ [from registry summary]
  Gate MET = YES / NO

**If NOT MET:** write "Budget gate: NOT TRIGGERED — M = [value]." Proceed to Section 4.

**If MET** — complete BUDGET STEP A before BUDGET STEP B. Both are required. Do not write STEP B
aggregate totals before STEP A rows are complete.

**BUDGET STEP A — Per-Automation Breakdown**

One row for each automation listed in "Automations with side effects" from Section 2.

| Automation Name | Dataverse Reads | Dataverse Writes | Connector Calls | Notification Sends | Other Actions | Total per Invocation |
|-----------------|-----------------|------------------|-----------------|-------------------|---------------|----------------------|
| [name] | [count] | [count] | [count] | [count] | [count] | [row sum] |
| … | | | | | | |

Estimation rules:
- Minimum plausible integer count per cell under normal execution (no error branches).
- "Unknown" is not acceptable — estimate and state your basis below the table.
- Total per Invocation = arithmetic sum of all cells in that row.

Estimation assumptions: [one sentence]

**BUDGET STEP B — Aggregate Summary** (derived from STEP A — do not assert without STEP A)

| Budget Metric | Value | Derivation |
|---------------|-------|------------|
| Total API requests per occurrence | [sum of all STEP A "Total per Invocation" values] | Σ STEP A rows |
| Power Platform daily request limit | [limit] | License tier from Section 1 |
| Budget consumed per occurrence (%) | [(requests ÷ limit) × 100] | STEP B arithmetic |
| Cascade depth N | [N from registry summary] | All firing triggers |
| Estimated sync chain duration | [estimate] | Sync YES rows in Section 2 |
| Estimated async chain duration | [estimate] | Longest async path |
| Budget risk level | `LOW` (<1%) / `MEDIUM` (1–10%) / `HIGH` (>10%) | Per budget consumed |

---

## SECTION 4 — PATHOLOGY DETECTION

Evaluate all three. Reference automations by name from Section 2.

**4a. Trigger Storm**
Verdict: `PRESENT` / `RISK` / `ABSENT`
Evidence: [cascade trace by automation name and field path, or confirmation of separation]
Remediation (PRESENT/RISK only): [exact PA/Dataverse construct — name flow, step, expression]

**4b. Missing Trigger**
Verdict: `PRESENT` / `RISK` / `ABSENT`
Evidence: [expected type and unguarded logic, or confirmation of coverage]
Remediation (PRESENT/RISK only): [registration target — solution layer, entity, event, type]

**4c. Circular Trigger**
Verdict: `PRESENT` / `RISK` / `ABSENT`
Evidence: [loop trace, or specific guard mechanism preventing re-entry]
Remediation (PRESENT/RISK only): [plugin depth check, OldValue guard, or trigger condition filter]

---

## SECTION 5 — SUMMARY

Two sentences: N of (N+NonFiring) registered automations fired; budget gate result (M); pathology
verdicts. One action item if any verdict is PRESENT or RISK.

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: `skill`, `topic`, `date`, `M`, `N`, `budget_gate_fired` (boolean),
`pathologies_found` (list), `storm_depth` (integer or "N/A").
```

---

## V-03 — Single Axis: Role Sequence (Three Specialist Analysts)

**Axis**: Role sequence — three distinct specialist analysts execute sequentially with a formal
handoff: (1) Registry Analyst enumerates all triggers and produces the complete catalog; (2) Budget
Analyst receives the catalog as read-only input and produces the budget gate and calculation;
(3) Pathology Analyst receives both catalog and budget data and produces verdicts and remediation.
Each analyst operates only within their domain.

**Hypothesis**: A single-role prompt allows enumeration and budget calculation to be merged into
one pass, enabling a model to assert budget totals without referencing catalog entries. Splitting
Budget Analyst as a separate role that treats the catalog as a read-only input forces the budget
section to explicitly cite which automations are being counted. Role specialization also pressures
the Pathology Analyst to name specific catalog entries as evidence rather than writing generic
verdicts. This tests whether role separation produces incidental C-12/C-13 coverage.

**Note**: This variation does not explicitly mandate the registry code block code-fence format
(C-12) or the two-step STEP A/STEP B budget lifecycle (C-13). Both may appear based on the Budget
Analyst's format choices.

```
You are running /flow:trigger for topic: {topic}.

This simulation runs in three analyst passes. Each analyst operates only within their role.
Do not merge passes. Do not let one analyst produce another analyst's outputs.

---

## ANALYST 1 — REGISTRY ANALYST

**Role**: Power Automate / Dataverse Enumeration Specialist. Your only job is to produce a complete
trigger catalog for the given change event. Do not evaluate pathologies. Do not calculate budget.
Produce the catalog that downstream analysts use.

**Triggering change**: {signal}

### 1a — Scenario Record

- Entity schema name: ___
- Change event: [field update / record create / delete / status change / custom event]
- Field schema name (field update only): ___ — old value: ___ — new value: ___
- Solution layer: [or "inferred: SOURCE"]
- Environment: [or "inferred"]
- License tier: [or "assumed: TIER; basis: REASON"]

### 1b — Unified Trigger Table

Every automation registered for this entity and change event — firing AND non-firing — in one table.
No supplemental trigger lists.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

- **Fires?**: `YES` or `NO`. Every registered automation has exactly one row; no row may omit this.
- **#**: Integer for YES rows (firing execution order). `--` for NO rows.
- **Type**: `Cloud Flow` / `Dataverse Plugin` / `Business Rule` / `Copilot Studio Topic` / `Other`
- **Condition Expression**: required for all rows. Unconditional YES: "Always fires — no filter on
  [event type]." NO rows: exact failed expression; `N/A` is not acceptable.
- **Sync/Async**: `Sync` / `Async` for YES rows; `--` for NO
- **Inputs**: concrete schema-name values for YES rows; `--` for NO
- **Outputs**: concrete state changes for YES rows; `--` for NO
- **Side Effects**: named external state changes for YES rows (with specifics), or `none`; `--` for NO

### 1c — Catalog Summary

Write immediately after the table:
- Firing (YES) count: ___
- Non-firing (NO) count: ___
- YES rows with Side Effects != "none": ___ [list names or "none"]
- Sync YES rows: ___ / Async YES rows: ___

End Analyst 1: "Trigger catalog complete. Handing off to Budget Analyst."

---

## ANALYST 2 — BUDGET ANALYST

**Role**: Power Platform Capacity Architect. You receive the Analyst 1 catalog. Your job is to
evaluate the budget gate and, if triggered, calculate the platform cost of the cascade. You do not
re-enumerate triggers. You do not evaluate pathologies. Reference the Analyst 1 catalog by name.

**Input**: Analyst 1 catalog summary — M (YES rows with side effects), N (total YES), license tier.

### 2a — Gate Check

Gate condition: M >= 3

  M (from Analyst 1 summary)  = ___
  Gate condition MET          = YES / NO

If NOT MET: "Budget gate: NOT TRIGGERED — M = [value]. No budget analysis required."
End Analyst 2. Hand off to Analyst 3.

### 2b — Per-Automation Action Count (required if gate MET)

One row for each automation named in Analyst 1's "YES rows with Side Effects != none":

| Automation Name | Dataverse Reads | Dataverse Writes | Connector Calls | Sends | Other | Total per Invocation |
|-----------------|-----------------|------------------|-----------------|-------|-------|----------------------|
| [name from Analyst 1] | [count] | [count] | [count] | [count] | [count] | [row sum] |
| … | | | | | | |

Estimation rules: minimum plausible count per cell; "Unknown" is not acceptable. State estimation
basis in one sentence below the table.

### 2c — Budget Summary (derived from §2b — do not assert totals without §2b)

| Budget Metric | Value | Derivation |
|---------------|-------|------------|
| Side-effect triggers M | [from Analyst 1] | Analyst 1 catalog summary |
| Total API requests per occurrence | [sum of §2b "Total per Invocation" column] | Σ §2b rows |
| PP daily request limit | [limit] | License tier from Analyst 1 scenario |
| Budget consumed per occurrence (%) | [(requests/limit)×100] | §2c arithmetic |
| Total cascade depth N | [N from Analyst 1] | Analyst 1 catalog summary |
| Sync chain duration | [estimate] | Analyst 1 sync rows |
| Async chain duration | [estimate] | Analyst 1 async rows |
| Budget risk level | `LOW` / `MEDIUM` / `HIGH` | <1% / 1–10% / >10% |

End Analyst 2: "Budget analysis complete. Handing off to Pathology Analyst."

---

## ANALYST 3 — PATHOLOGY ANALYST

**Role**: Power Platform Architect. You receive the Analyst 1 catalog and Analyst 2 budget data.
Evaluate all three pathology types. Reference Analyst 1's catalog entries by name as evidence.

### 3a — Pathology Verdicts

| Pathology | Verdict | Evidence | Remediation |
|-----------|---------|----------|-------------|
| **Trigger Storm** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Missing Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Circular Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |

Evidence for PRESENT/RISK: full cascade trace using Analyst 1 automation names and data paths —
"[Name] output [field=X] → [Name B] fires on [field X changed] → [B] output creates [entity] →
[Name C] fires on [entity create]…"

Evidence for ABSENT: name the specific guard in the current configuration — not "no issues found."

Remediation for PRESENT/RISK:
- PA: `Add trigger condition to [Flow Name]: @not(equals(triggerOutputs()?['body/FIELDNAME'], VALUE))`
- Plugin: `if (context.Depth > 1) return;` in [PluginClass.OnExecute]
- Copilot Studio: `[System.Activity.Name] is not equal to "Automated"` condition in [TopicName]

### 3b — Summary

Two sentences: N of (N+NonFiring) fired; budget gate result from Analyst 2; pathology verdicts.
One recommended action if any verdict is PRESENT or RISK.

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: `skill`, `topic`, `date`, `M`, `N`, `budget_gate_fired` (boolean),
`pathologies_found` (list), `analysts` (["Registry","Budget","Pathology"]).
```

---

## V-04 — Combined: Output Format + Lifecycle Emphasis (C-12 + C-13 Co-Satisfaction)

**Axes combined**: (1) registry summary code block with named variables `REGISTRY.M`,
`REGISTRY.N`, `REGISTRY.NonFiring`, `REGISTRY.SideEffectAutomations` as downstream-referenceable
identifiers (C-12); (2) BUDGET STEP A per-automation breakdown sub-table required before BUDGET
STEP B aggregate, with row count validated against `REGISTRY.M` (C-13); the budget gate reads
`REGISTRY.M` by name from the code block.

**Hypothesis**: C-12 and C-13 are structurally co-dependent: the registry code block names the
side-effect automations in `REGISTRY.SideEffectAutomations`, and BUDGET STEP A must have exactly
one row per named automation. This creates a verifiable cross-reference — if `REGISTRY.M = 4` and
`REGISTRY.SideEffectAutomations` lists four names, STEP A must have exactly four rows. Any
discrepancy between the code block and the breakdown is structurally detectable. This is the
minimal combination that co-satisfies C-12 and C-13 without the threat-lead complexity of V-05.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

Follow this exact sequence. Each section feeds the next by named variable reference. Do not reorder.

---

## SECTION 1 — SCENARIO

| Field | Value |
|-------|-------|
| Table | [Dataverse entity schema name] |
| Change type | [field update / record create / delete / status change / custom event] |
| Field changed | [schema name — e.g., cr123_statuscode] |
| Old value | [prior state or "N/A — create/delete"] |
| New value | [new state or "N/A — create/delete"] |
| Solution layer | [Default / Managed / Unmanaged — or "inferred: SOURCE"] |
| Environment | [Dev / Test / UAT / Production — or "inferred"] |
| License tier | [per-user premium / per-flow / pay-as-you-go — or "assumed: TIER"] |

---

## SECTION 2 — UNIFIED TRIGGER REGISTRY

This section produces two outputs: (a) the trigger table and (b) the registry summary code block.
Both are required. The code block is the canonical variable source. Downstream sections reference
REGISTRY.M, REGISTRY.N, and automation names from the code block — not from the table.
Supplemental trigger lists are prohibited.

### 2a — Trigger Table

Every automation registered for this entity and event — firing AND non-firing — in one table.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

Column enforcement:
- **Fires?**: `YES` or `NO`. Every registered automation appears as exactly one row. No row may
  omit this column.
- **#**: Integer firing-sequence for YES rows. `--` for NO rows.
- **Type**: `Cloud Flow` / `Dataverse Plugin` / `Business Rule` / `Copilot Studio Topic` / `Other`
- **Condition Expression**: required for all rows.
  - YES unconditional: `"No trigger filter — always fires on [event type] for [entity]"`
  - YES conditional: OData expression that evaluated true
  - NO rows: exact expression that evaluated false; `N/A` is not acceptable
- **Sync/Async**: `Sync` / `Async` for YES rows; `--` for NO
- **Inputs**: concrete values for YES rows (field schema name, OData token, record ID pattern);
  `--` for NO
- **Outputs**: concrete state changes for YES rows (field written, entity created, endpoint,
  message type); `--` for NO
- **Side Effects**: specific external state changes for YES rows (table schema name, recipient role,
  API hostname, audit log name) or `none`; `--` for NO

### 2b — Registry Summary Code Block

Write immediately after the table. This code block is the single source of truth for trigger counts.

```registry
REGISTRY.M                      = [count of YES rows where Side Effects != "none"]
REGISTRY.N                      = [count of all YES rows — total firing triggers]
REGISTRY.NonFiring              = [count of NO rows]
REGISTRY.SideEffectAutomations  = [comma-separated YES-row names with Side Effects != "none", or "none"]
```

---

## SECTION 3 — BUDGET GATE (runs before pathology — mandatory)

Gate condition: `REGISTRY.M >= 3`

Read REGISTRY.M from §2b. Do not recount from the trigger table.

```gate
REGISTRY.M  = ___  [from §2b code block — do not derive independently]
Gate MET    = YES / NO
```

**If gate NOT MET:**

> Budget gate NOT triggered: REGISTRY.M = [§2b value]. No budget section required.

Proceed to Section 4.

**If gate MET** — execute BUDGET STEP A before BUDGET STEP B. Both are required.

**BUDGET STEP A — Per-Automation Breakdown**

One row for each automation in `REGISTRY.SideEffectAutomations` from §2b. Row count must equal
`REGISTRY.M`.

| Automation Name | Dataverse Reads | Dataverse Writes | Connector Calls | Notification Sends | Other Actions | Total per Invocation |
|-----------------|-----------------|------------------|-----------------|-------------------|---------------|----------------------|
| [name from REGISTRY.SideEffectAutomations] | [count] | [count] | [count] | [count] | [count] | [row sum] |
| … | | | | | | |

Estimation rules:
- Minimum plausible integer count per cell under normal execution. "Unknown" is not acceptable.
- Total per Invocation = arithmetic sum of all cells in that row. Do not assert a total without
  filling the addend cells.

Estimation assumptions: [one sentence]

**BUDGET STEP B — Aggregate Summary** (derived from STEP A — do not assert totals without STEP A)

| Budget Metric | Value | Derivation |
|---------------|-------|------------|
| Side-effect triggers M | [REGISTRY.M] | §2b code block |
| Total firing triggers N | [REGISTRY.N] | §2b code block |
| Total API requests per occurrence | [sum of all STEP A "Total per Invocation"] | Σ STEP A rows |
| Power Platform daily request limit | [limit] | License tier from §1 |
| Budget consumed per occurrence (%) | [(requests ÷ limit) × 100] | STEP B arithmetic |
| Estimated run duration — sync path | [estimate] | Sync YES rows from §2a |
| Estimated run duration — async path | [estimate] | Longest async path from §2a |
| Budget risk level | `LOW` (<1%) / `MEDIUM` (1–10%) / `HIGH` (>10%) | Per budget consumed |

---

## SECTION 4 — PATHOLOGY DETECTION

Reference §2a automations by name. This section runs after §3.

| Pathology | Verdict | Evidence | Remediation |
|-----------|---------|----------|-------------|
| **Trigger Storm** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Missing Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Circular Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |

Evidence for PRESENT/RISK: cascade trace by name and data path — "[Automation A] output:
[field X = VALUE] → [Automation B] fires on [field X changed] → [B] output: creates [entity Y] →
[Automation C] fires on [entity Y create]…"

Evidence for ABSENT: name the specific architectural guard — not "no issues found."

Remediation for PRESENT/RISK:
- PA: `Add trigger condition to [Flow Name]: @not(equals(triggerOutputs()?['body/FIELDNAME'], VALUE))`
- Plugin: `if (context.Depth > 1) return;` at entry of [PluginClass.OnExecute]
- Copilot Studio: condition node `[System.Activity.Name] is not equal to "Automated"` in [TopicName]

---

## SECTION 5 — SUMMARY

Two sentences: REGISTRY.N of (REGISTRY.N + REGISTRY.NonFiring) registered automations fired;
budget gate result (REGISTRY.M); pathology verdicts. One recommended action if any verdict is
PRESENT or RISK.

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: `skill`, `topic`, `date`, `REGISTRY.M`, `REGISTRY.N`, `REGISTRY.NonFiring`,
`budget_gate_fired` (boolean), `pathologies_found` (list), `budget_risk_level`.
```

---

## V-05 — Combined: All Four Axes (R3 Golden Candidate)

**Axes combined**: (1) threat-first role sequence — Phase 1 declares expected storm chains,
coverage gaps, and re-entry risks before enumeration; (2) dual-population table as sole
enumeration surface with explicit YES/NO enforcement (C-11, inherited from R2); (3) registry
summary code block with named variable identifiers and hypothesis cross-check (C-12); (4) BUDGET
STEP A per-automation sub-table with REGISTRY.M row-count validation before STEP B aggregate
(C-13); (5) pre-positioned budget gate reads REGISTRY.M from code block before pathology (C-10).

**Hypothesis**: R3 golden candidate. Threat declaration primes C-04 completeness and C-05
side-effect specificity before enumeration begins. The dual-population table satisfies C-11 and
populates `REGISTRY.SideEffectAutomations` in the code block. The registry code block makes
`REGISTRY.M` a named variable that the budget gate reads by identifier (C-12), preventing
independent re-derivation. BUDGET STEP A rows are validated against `REGISTRY.SideEffectAutomations`,
creating a self-verifying cross-reference between C-12 and C-13. The hypothesis cross-check in
§2d surfaces catalog entries the threat declaration did not anticipate, mitigating confirmation bias.

```
You are running /flow:trigger for topic: {topic}.

This simulation runs in four phases. Follow phase boundaries exactly. Do not merge phases.

---

## PHASE 1 — THREAT DECLARATION

**Role**: Power Platform Pathology Specialist

Before any enumeration, declare structural hypotheses about this scenario. Do not enumerate
specific triggers. Declare what types of automations and pathologies are likely.

**Triggering change**: {signal}

1. **Storm exposure**: What automation chain is structurally most likely for this entity type and
   change event? Name the most plausible cascade path (e.g., "status-change cloud flow →
   notification send → approval record create → approval trigger chain → owner reassignment flow").
   Identify the highest-risk cascade link.

2. **Coverage gaps**: What automation types are typically registered for this change event type
   that, if absent, leave business logic unprotected? List two or three expected types (e.g.,
   "audit trail plugin, manager notification flow, SLA timer recalculation trigger"). For each,
   name the unguarded business logic.

3. **Re-entry risk**: What field types in this entity domain are common circular-trigger candidates?
   Name the pattern (e.g., "calculated rollup field updated by a flow whose trigger condition is
   the same rollup field").

4. **Hypothesis statement** (one sentence per type):
   - Storm: "I expect [storm present / storm risk / no storm] because [one sentence]."
   - Missing: "I expect [coverage gaps in AREA / complete coverage] because [one sentence]."
   - Circular: "I expect [re-entry risk / clean separation] because [one sentence]."

End Phase 1: "Threat hypotheses declared. Proceeding to enumeration."

---

## PHASE 2 — UNIFIED TRIGGER REGISTRY

**Role**: Power Automate / Dataverse Enumeration Expert. You have the Phase 1 threat hypotheses.
Build a complete catalog, paying particular attention to risk areas flagged.

### 2a — Scenario Block

```scenario
entity_schema_name:  ___
change_event:        ___  [field_update | record_create | record_delete | status_change | custom_event]
field_schema_name:   ___  [or "N/A — not a field update"]
old_value:           ___  [or "N/A"]
new_value:           ___  [or "N/A"]
solution_layer:      ___  [Default | Managed | Unmanaged | inferred: SOURCE]
environment:         ___  [Dev | Test | UAT | Production | inferred]
license_tier:        ___  [per_user_premium | per_flow | payg | assumed: TIER — basis: REASON]
```

### 2b — Dual-Population Trigger Table

Every automation registered for this entity and event — firing AND non-firing — in one table.
This table is the sole enumeration surface. No supplemental trigger lists anywhere in the output.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

Column enforcement:
- **Fires?**: `YES` or `NO`. Every registered automation appears as exactly one row. No row may
  omit this column.
- **#**: Integer firing-sequence for YES rows (execution order). `--` for NO rows.
- **Type**: `Cloud Flow` / `Dataverse Plugin` / `Business Rule` / `Copilot Studio Topic` /
  `Custom Connector` / `Other`
- **Condition Expression**: required for all rows.
  - YES unconditional: `"No trigger filter — always fires on [event type] for [entity]"`
  - YES conditional: OData/FetchXML expression that evaluated true
  - NO rows: exact expression that evaluated false; do not write `N/A`
- **Sync/Async**: `Sync` (pre-commit) / `Async` (post-commit) for YES rows; `--` for NO rows
- **Inputs**: YES rows: concrete values (field schema name, OData value, token name, record ID
  pattern); `--` for NO rows
- **Outputs**: YES rows: concrete state changes (field schema name written, entity name created,
  API endpoint pattern, message category); `--` for NO rows
- **Side Effects**: YES rows: specific external state changes (target table schema name, recipient
  role name, API hostname, audit log schema name) or `none`; `--` for NO rows

### 2c — Registry Summary Code Block

Write immediately after the table. This block is the canonical variable declaration for all
downstream phases. Phases 3 and 4 reference these identifiers, not row counts from the table.

```registry
REGISTRY.M                      = [count of YES rows where Side Effects != "none"]
REGISTRY.N                      = [count of all YES rows — total firing triggers]
REGISTRY.NonFiring              = [count of NO rows]
REGISTRY.SideEffectAutomations  = [comma-separated YES-row names with Side Effects != "none", or "none"]
```

### 2d — Hypothesis Cross-Check (against Phase 1 declarations)

- Storm hypothesis: `[confirmed likely / not supported / inconclusive]` — [one sentence from table]
- Coverage gap hypothesis: `[confirmed / not supported / inconclusive]` — [one sentence]
- Re-entry hypothesis: `[confirmed / not supported / inconclusive]` — [one sentence]
- Unexpected findings: [trigger types in catalog not anticipated by Phase 1, or "none"]

End Phase 2: "Registry complete. REGISTRY.M = [value]. Proceeding to budget analysis."

---

## PHASE 3 — BUDGET GATE

**Role**: Power Platform Capacity Analyst

This phase runs before pathology verdicts. Gate condition does not require a confirmed storm.
Read all values from §2c registry code block — do not re-derive from the table.

```gate
REGISTRY.M  = ___  [from §2c — do not derive independently]
Gate MET    = YES / NO  [REGISTRY.M >= 3]
```

**If gate NOT MET:**

> Budget gate: NOT TRIGGERED — REGISTRY.M = [§2c value] (fewer than 3 side-effect automations fire).
> No budget section required.

Proceed to Phase 4.

**If gate MET** — execute BUDGET STEP A before BUDGET STEP B. Both are required.

**BUDGET STEP A — Per-Automation Breakdown**

One row for each automation in `REGISTRY.SideEffectAutomations`. Row count must equal `REGISTRY.M`.

| Automation Name | Dataverse Reads | Dataverse Writes | Connector Calls | Notification Sends | Other Actions | Total per Invocation |
|-----------------|-----------------|------------------|-----------------|-------------------|---------------|----------------------|
| [name from REGISTRY.SideEffectAutomations] | [count] | [count] | [count] | [count] | [count] | [row sum] |
| … | | | | | | |

Estimation rule: minimum plausible count per cell under normal execution. "Unknown" is not
acceptable — estimate and state basis below the table.

Estimation basis: [one sentence on entity relationships, flow depth, or connector type assumed]

**BUDGET STEP B — Aggregate Summary** (derived from STEP A — do not assert total without STEP A)

| Budget Metric | Value | Derivation |
|---------------|-------|------------|
| Side-effect triggers M | [REGISTRY.M] | §2c code block |
| Total firing triggers N | [REGISTRY.N] | §2c code block |
| Total API requests per occurrence | [sum of all STEP A "Total per Invocation"] | Σ STEP A rows |
| Power Platform daily request limit | [limit] | License tier from §2a |
| Budget consumed per occurrence (%) | [(requests ÷ limit) × 100] | STEP B arithmetic |
| Estimated sync chain duration | [estimate] | Sync YES rows from §2b |
| Estimated async chain duration (longest path) | [estimate] | Async YES rows from §2b |
| Budget risk level | `LOW` (<1%) / `MEDIUM` (1–10%) / `HIGH` (>10%) | Per budget consumed |

End Phase 3: "Budget complete. Gate = [MET/NOT MET]. Risk = [level or N/A]."

---

## PHASE 4 — PATHOLOGY VERDICTS AND REMEDIATION

**Role**: Power Platform Architect

Using §2b trigger table and §3 budget data, produce final verdicts. Reference §2b automations
by name. Evidence must trace specific data paths through the catalog.

| Pathology | Verdict | Evidence | Remediation |
|-----------|---------|----------|-------------|
| **Trigger Storm** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Missing Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |
| **Circular Trigger** | `PRESENT` / `RISK` / `ABSENT` | | |

**Evidence — PRESENT/RISK**: full cascade trace from §2b:
"[Automation A] output: [field schema name = VALUE] → [Automation B] fires on condition [field
changed to VALUE] → [B] output: creates [entity schema name] → [Automation C] fires on [entity
create] → loops back when…"

**Evidence — ABSENT**: name the specific guard in the current configuration:
"[Flow Name] trigger condition filters [field schema name] != [guard value]" or "[PluginClass]
checks context.Depth at entry."

**Remediation — PRESENT/RISK only**:
- PA flow: `Add trigger condition to [Flow Name]: @not(equals(triggerOutputs()?['body/FIELDNAME'], VALUE))`
  OR `Set concurrency control to 1 on [Flow Name]`
- Dataverse Plugin: `if (context.Depth > 1) return;` at top of [PluginClass.OnExecute]
  OR `if (preImage[FIELD].Equals(postImage[FIELD])) return;`
- Copilot Studio: `Condition: [System.Activity.Name] is not equal to "Automated"` before [TopicName]

**Phase 1 hypothesis reconciliation**:
- Storm: [confirmed/refuted] — [one sentence on catalog vs. prediction]
- Missing: [confirmed/refuted] — [one sentence]
- Circular: [confirmed/refuted] — [one sentence]

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: `skill`, `topic`, `date`, `entity_schema_name`, `environment`, `field_changed`,
`REGISTRY.M`, `REGISTRY.N`, `REGISTRY.NonFiring`, `budget_gate_fired` (boolean),
`budget_risk_level`, `pathologies_found` (list: storm/missing/circular),
`hypothesis_accuracy` (phase1_matches/3).
```

---

## Round 3 Design Notes

### Variation axis coverage

| Axis | R2 approach | R3 approach | Change |
|------|------------|-------------|--------|
| Output format | Registry summary in code block but values referenced in prose ("M = [value from registry]") | Named variable identifiers (`REGISTRY.M`) with mandatory downstream reference syntax (V-01, V-04, V-05) | Code block graduates from format hint to downstream-referenceable variable system; inconsistency is structurally detectable |
| Lifecycle emphasis | "Show calculation basis" column hint in budget table (V-04 R2) | BUDGET STEP A (per-automation sub-table) required before BUDGET STEP B (aggregate derived from rows) as explicit sequential lifecycle steps (V-02, V-04, V-05) | Aggregate total blocked until per-automation rows exist and are verifiable |
| Role sequence | Single-role or threat+enumerator+verdict (R2 V-03/V-05) | Three specialist analysts: Registry / Budget / Pathology — Budget Analyst treats catalog as read-only (V-03 R3) | Role separation prevents enumeration+budget merge; Budget Analyst cites catalog entries by name |
| Inertia framing | (Not a primary axis in R2) | (Not isolated as primary axis in R3 — subsumed into threat-first Phase 1 of V-05) | Threat-first framing from R2 V-05 preserved in V-05 R3 |

### Predicted per-criterion scores

| V | C-10 | C-11 | C-12 | C-13 | Predicted Composite |
|---|------|------|------|------|---------------------|
| V-01 | PASS | PASS | PASS | RISK | ~98 |
| V-02 | PASS | PASS | FAIL | PASS | ~98 |
| V-03 | PASS | PASS | RISK | RISK | ~96 |
| V-04 | PASS | PASS | PASS | PASS | 100 |
| V-05 | PASS | PASS | PASS | PASS | 100 |

### C-12 vs C-11 distinction

C-11 (R2) required: one unified table with `Fires? YES/NO` per row + explicit enforcement rule.
C-12 (R3) requires: a code-fence block immediately after the table declaring M, N, and NonFiring
as named variables that downstream sections reference by identifier.

A variation can satisfy C-11 (table present with enforcement) and fail C-12 (no code-fence, or
code-fence present but downstream sections re-derive M independently). V-01 through V-03 in R2
all satisfy C-11 but do not satisfy C-12 as defined in R3 rubric.

### C-13 vs C-09 distinction

C-09 (R1/R2) required: anti-hedge enforcement ("unknown is not acceptable") + final budget number.
C-13 (R3) requires: per-automation arithmetic in the budget section showing additive action count
components — aggregate totals without per-automation intermediate arithmetic do not satisfy this.

V-02 R2 had a calculation basis template ("Flow A calls N Dataverse actions + M connector actions
= X requests") as a prose hint. This passes C-09 (anti-hedge present) but fails C-13 (no separate
per-automation sub-table row structure). R3 V-02/V-04/V-05 make the per-automation breakdown a
structurally required sub-table, not a template hint.

### Golden candidate

**V-05** is the R3 synthesis target:
- Threat declaration (Phase 1) primes C-04 pathology completeness and C-05 side-effect specificity
- Dual-population table (§2b) satisfies C-11 and populates REGISTRY.SideEffectAutomations
- Registry code block (§2c) with named variable identifiers satisfies C-12
- Pre-positioned budget gate (Phase 3) reads REGISTRY.M by identifier, satisfying C-10
- BUDGET STEP A rows validated against REGISTRY.M row-count creates C-12/C-13 cross-reference
- Hypothesis cross-check (§2d) mitigates threat-first confirmation bias

**V-04** is the minimal mechanism proof: isolates C-12+C-13 co-satisfaction without threat-lead
complexity. If V-04 fails either new criterion, the failure belongs to the mechanism, not the
phase architecture.

```json
{"round": 3, "all_essential_pass_predicted": true, "new_patterns": ["named variable identifiers in registry code block (REGISTRY.M) with mandatory downstream reference syntax creates structurally detectable inconsistency if budget gate re-derives M independently", "BUDGET STEP A per-automation sub-table with row count validated against REGISTRY.M creates cross-reference between C-12 and C-13 — sub-table is both verifiable and self-consistent with the code block", "two-step STEP A then STEP B lifecycle sequencing blocks aggregate assertion before per-automation arithmetic exists"]}
```
