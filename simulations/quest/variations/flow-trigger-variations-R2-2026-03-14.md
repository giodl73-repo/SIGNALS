**flow-trigger Variations R2** written to `simulations/quest/variations/flow-trigger-variations-R2-2026-03-14.md`.

---

## Summary

**5 variations across 4 axes**, targeting the two new rubric criteria from v2 (C-10 and C-11):

| ID | Axis | Primary Criterion Targeted |
|----|------|---------------------------|
| **V-01** | Output format — dual-population table opens | C-11 (Fires?/YES/NO table as first output) |
| **V-02** | Lifecycle emphasis — budget gate before pathology | C-10 (proactive gate, structurally pre-verdict) |
| **V-03** | Role sequence — threat model leads | C-04 (pathology depth) + C-05 (side effect specificity) |
| **V-04** | Combined: output format + lifecycle emphasis | C-10 + C-11 co-satisfied in locked sequence |
| **V-05** | Combined: all four axes | All new criteria; R2 golden candidate |

**Key R2 design decisions:**

- **C-10 failure mode from R1**: "no confirmed storm → no budget section." R2 fixes this in V-02/V-04/V-05 by placing the budget gate as its own section *before* pathology verdicts. The model cannot retroactively omit it.
- **C-11 failure mode from R1**: V-01–V-04 listed registered/firing triggers in separate blocks. R2 enforces the unified Fires?/YES/NO table as the *sole enumeration surface* with explicit rules banning supplemental lists.
- **V-04 is the clean mechanism test**: isolates C-10+C-11 co-satisfaction without the threat-lead complexity. If V-04 fails either criterion, the failure belongs to the mechanism.
- **V-05** adds the threat-first role sequence and formal audit register — addressing the C-06 shallow condition evaluation that R1 conversational mode produced.
re no budget section needed." C-10 in the v2 rubric breaks this by gating on M >= 3 AND side_effect_exists -- not on storm confirmation. V-02 and V-04 enforce this by placing the budget gate section BEFORE the pathology section in the prompt, so the model cannot retroactively skip it.

**The table insight from R1:** C-11 failed in V-01 through V-04 because those prompts used a single-axis table that only showed firing triggers, or listed registered/firing in separate sections. V-01 in R2 enforces the dual-population Fires?/YES/NO table as the FIRST output with explicit rules banning supplemental lists.

**V-03 is the structural risk.** Threat-first enumeration improves C-04 and C-05 but risks confirmation bias in the catalog -- the enumerator may over-report threats the analyst predicted and under-report others. V-05 mitigates this with Phase 2d hypothesis cross-check.

**Golden candidate: V-05.** Combines all four axes. Threat declaration primes C-04 completeness. Dual-population table structurally satisfies C-11 and produces the M+side-effect values needed for C-10. Pre-pathology budget gate fires on those values before any storm verdict exists. Formal audit register addresses the C-06 shallow condition evaluation seen in R1 V-04 conversational mode.

---

## V-01 -- Single Axis: Output Format (Dual-Population Table Opens)

**Axis**: Output format -- the dual-population trigger table with Fires?/YES/NO column is the FIRST structural output produced; all subsequent sections reference rows from that table by row number; no supplemental trigger lists are permitted
**Hypothesis**: Requiring the unified table before any narrative prevents the most common C-11 failure mode -- where firing triggers are enumerated in prose and non-firing triggers are omitted or listed separately. Row-number cross-referencing forces completeness before analysis proceeds, because a section that says "see Row 4" requires Row 4 to exist.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

---

## STEP 1: SCENARIO

State the triggering change:
- Table: [Dataverse table or entity name]
- Change type: [field update / record create / delete / status change / custom event]
- Field changed: [schema name] -- [old value] to [new value]
- Solution layer: [Default / Managed / Unmanaged -- or "inferred from topic context"]
- Environment: [Dev / Test / Production -- or "inferred"]
- License tier: [per-user plan / per-flow plan / pay-as-you-go / premium -- or "assumed: TIER"]

---

## STEP 2: UNIFIED TRIGGER TABLE

Build this table before writing anything else. Include EVERY automation registered for
this entity and event type -- those that fire AND those that do not. Do not write prose
analysis before this table is complete. No supplemental trigger lists are permitted; this
table is the sole enumeration surface.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

Column rules:
- **#**: Firing sequence number for YES rows (1, 2, 3...); write "--" for NO rows
- **Type**: Cloud Flow / Dataverse Plugin / Business Rule / Copilot Studio Topic / Webhook / Other
- **Fires?**: YES or NO only -- every registered automation must appear as one row
- **Condition Expression**: mandatory for all rows; for YES unconditional: "always fires -- no
  filter set on [event type]"; for NO rows: the exact expression that evaluated false
- **Sync/Async**: for YES rows only; write "--" for NO rows
- **Inputs**: for YES rows, at least one concrete value (field schema name, token, record ID);
  "--" for NO rows
- **Outputs**: for YES rows, at least one concrete state change (field written, record created,
  message sent); "--" for NO rows
- **Side Effects**: for YES rows, name all external state changes (email recipient, audit table,
  child entity, API endpoint) or write "none"; "--" for NO rows

After the table:
- M = [count of YES rows]
- N = [total rows]
- Non-firing registered = [N minus M]
- YES rows with Side Effects != "none": [list automation names or "none"]

---

## STEP 3: FIRING SEQUENCE

From YES rows in the table above, reproduce the firing sequence referencing row numbers:

| Step | Row # | Automation Name | Sync/Async | Depends On Step |
|------|-------|-----------------|------------|-----------------|

---

## STEP 4: PATHOLOGY DETECTION

Evaluate all three. Cite table row numbers as evidence references.

**4a. Trigger Storm**
Verdict: PRESENT / RISK / ABSENT
Evidence: [Which rows form a cascade chain? Trace: Row N output field -> Row M trigger condition]
Remediation (if PRESENT or RISK): [Specific PA/Copilot Studio construct -- name the flow, step,
condition field]

**4b. Missing Trigger**
Verdict: PRESENT / RISK / ABSENT
Evidence: [What automation type is expected for this change type + entity but absent from table?]
Remediation (if PRESENT or RISK): [Where to register it -- solution layer, table, event type]

**4c. Circular Trigger**
Verdict: PRESENT / RISK / ABSENT
Evidence: [Which rows close a loop? Trace: Row N output -> Row M fires -> Row M output -> Row N fires]
Remediation (if PRESENT or RISK): [Specific break -- depth check, run-after condition, field guard]

---

## STEP 5: BUDGET GATE

Gate condition: M >= 3 AND any YES row has Side Effects != "none"

Check:
  M = [value from Step 2]
  Any YES row with side effects? [YES/NO -- cite automation names]
  Gate: [MET / NOT MET]

If MET -- complete this section. Do not wait for a storm verdict from Step 4.

| Budget Metric | Value |
|---------------|-------|
| Cascade depth M | |
| Estimated API requests per occurrence | |
| Power Platform daily request limit (license tier) | |
| Budget consumed per occurrence (%) | |
| Estimated run duration | |

If NOT MET: write "Budget gate not triggered: M = [N], side effects = [YES/NO]."

---

**Save artifact**: simulations/flow/trigger/{topic}-trigger-{date}.md
Frontmatter: skill, topic, date, triggering_change, environment, M, N, pathologies_found,
budget_gate_fired (boolean).
```

---

## V-02 -- Single Axis: Lifecycle Emphasis (Budget Gate Before Pathology)

**Axis**: Lifecycle phase ordering -- the budget gate is placed as its own section between enumeration and pathology; the model must evaluate M and side-effect existence and commit to budget values before writing any pathology verdict
**Hypothesis**: R1 variations deferred budget analysis to after pathology detection, which caused the model to omit C-10 when no storm was confirmed. Moving the budget gate before the pathology section forces commitment to M and side-effect inventory before the model knows its storm verdict -- structurally eliminating "no storm, therefore no budget section" reasoning.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

Execute these sections in order. Do not skip a section. Do not reorder them.

---

## SECTION 1 -- SCENARIO DECLARATION

State precisely:
- Table: [entity name]
- Event: [field update / record create / delete / status change]
- Field: [schema name] -- [old value] to [new value]
- Solution: [layer name or "inferred"]
- Environment: [tier or "inferred"]
- License tier: [plan or "assumed: TIER"]

---

## SECTION 2 -- TRIGGER REGISTRY

Enumerate every automation registered for this entity and event. For each:
1. Name and type (Cloud Flow / Plugin / Business Rule / Copilot Topic / Other)
2. Fires for this change? YES or NO
3. Condition that determines this (for NO rows: expression that failed; for YES rows: expression
   that passed, or "unconditional -- always fires on [event type]")
4. If YES: execution timing (sync/async), inputs, outputs, side effects (external state changes
   or "none")

Number YES rows in firing sequence. List NO rows after YES rows with "--" sequence number.

End with:
  M = [YES count]
  N = [total registered]
  YES rows with side effects: [list names or "none"]

---

## SECTION 3 -- BUDGET GATE

This section runs before pathology detection. Do not wait for a storm verdict.

Gate check:
  M                          = ___ [from Section 2]
  M >= 3?                    = YES / NO
  Any YES row side effect != "none"? = YES / NO [cite automation names]
  Gate condition MET?        = YES / NO

If YES -- complete the budget table:

| Budget Metric | Value |
|---------------|-------|
| Cascade depth M | |
| Estimated API requests per occurrence | |
| Power Platform daily request limit (license tier) | |
| Budget consumed per occurrence (%) | |
| Estimated run duration | |

Show calculation basis: "Flow A calls [N] Dataverse actions + [M] connector actions = [X]
requests; Flow B calls [N] = [Y] requests; total = [Z] requests per occurrence."
Estimation required -- "unknown" is not acceptable. State assumptions explicitly.

If NO: write "Budget gate: NOT MET -- M = [N], side effects present = [YES/NO]."
Then continue to Section 4.

---

## SECTION 4 -- PATHOLOGY DETECTION

Evaluate pathologies. Reference automations by name from Section 2.

**4a. Trigger Storm**
A storm is a cascade where trigger A's output fires trigger B, B's output fires C, etc.
Verdict: PRESENT / RISK / ABSENT
Evidence: [name the cascade chain, or confirm no data dependency between firing triggers]
Remediation (PRESENT/RISK only): [specific construct: run-after condition, depth check, field
guard, concurrency control -- name the exact flow/plugin/setting]

**4b. Missing Trigger**
Expected automations absent from the Section 2 registry.
Verdict: PRESENT / RISK / ABSENT
Evidence: [name the expected automation and the unprotected business logic]
Remediation (PRESENT/RISK only): [registration location, event type, solution layer]

**4c. Circular Trigger**
A trigger whose output creates conditions that re-fire itself or an upstream trigger.
Verdict: PRESENT / RISK / ABSENT
Evidence: [trace the loop; or name the guard that prevents re-entry]
Remediation (PRESENT/RISK only): [specific break: IPluginExecutionContext.Depth check,
modified-by guard, OldValue != NewValue filter]

---

## SECTION 5 -- SUMMARY

One paragraph: what changed, how many triggers fired (M of N registered), budget gate result,
pathology verdicts. Recommend one action if any verdict is PRESENT or RISK.

---

**Save artifact**: simulations/flow/trigger/{topic}-trigger-{date}.md
Frontmatter: skill, topic, date, M, N, budget_gate_fired, pathologies_found.
```

---

## V-03 -- Single Axis: Role Sequence (Threat Model Leads)

**Axis**: Role sequence -- a Pathology/Threat Expert runs first and declares expected pathology risks before enumeration begins; the Enumeration Expert builds the catalog knowing what threats to watch for; a Verdict Expert closes
**Hypothesis**: Threat-first enumeration primes C-04 (pathology detection) and C-05 (side effects) because the enumerator knows which field writes are threat-relevant before writing the catalog. R1 V-02 separated roles but put enumeration first -- this reversal tests whether pre-declared threats improve catalog depth. Trade-off: potential confirmation bias; Phase 2 includes a hypothesis cross-check to surface discrepancies.

```
You are running /flow:trigger for topic: {topic}.

This skill runs in three passes. Do not merge passes.

---

## PASS 1: THREAT ANALYST

**Role**: Power Platform pathology specialist. Your only job in this pass is to declare
threat hypotheses. Do not enumerate specific triggers.

**Triggering change**: {signal}

1. **Storm exposure**: Given this entity type and change event, what automation chains are
   structurally likely? Name the most plausible cascade path (e.g., "status-change flow ->
   notification send -> approval record create -> approval trigger").

2. **Coverage gaps**: What automation types are typically registered for this change type that,
   if absent, leave business logic unprotected? List two or three expected automation types
   (e.g., "audit trail plugin, manager notification flow, SLA timer reset").

3. **Re-entry risk**: What field types in this entity domain are common circular-trigger
   candidates? Name the pattern (e.g., "calculated rollup field updated by a flow whose
   trigger condition is the same field").

4. **Hypothesis statement**: One sentence per pathology type:
   - Storm: "I expect [storm / no storm] because [reason]."
   - Missing: "I expect [coverage gaps / complete coverage] in [area]."
   - Circular: "I expect [re-entry risk / clean separation] because [reason]."

End Pass 1: "Threat hypotheses declared. Proceeding to enumeration."

---

## PASS 2: ENUMERATION ANALYST

**Role**: Power Automate / Dataverse enumeration expert. You have received the threat
hypotheses from Pass 1. Build a complete trigger catalog, paying particular attention to
the risk areas flagged.

**Step 1 -- Scenario declaration**:
- Table: [entity name]
- Change: [field, old value to new value, or event type]
- Solution layer: [or "inferred"]
- Environment: [or "inferred"]
- License tier: [or "assumed: TIER"]

**Step 2 -- Trigger catalog**:
List EVERY automation registered for this entity and event. Include both firing and
non-firing. Use a single table -- no supplemental lists.

| # | Automation Name | Type | Fires? | Condition | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|-----------|------------|--------|---------|--------------|

For YES rows: # = firing sequence number. Fill all columns with concrete values.
For NO rows: # = "--". State the condition that filtered it out.

After table:
  M = [YES count]
  N = [total]
  YES rows with side effects != "none": [list or "none"]

**Step 3 -- Threat cross-check** (using Pass 1 hypotheses):
For each threat hypothesis, state whether the catalog confirms, refutes, or is inconclusive:
- Storm: [confirmed likely / not supported / inconclusive] -- [one sentence of table evidence]
- Missing: [confirmed / not supported / inconclusive] -- [evidence]
- Circular: [confirmed / not supported / inconclusive] -- [evidence]

Note any trigger types that appear in the catalog but were NOT anticipated by Pass 1.

---

## PASS 3: VERDICT AND REMEDIATION

**Role**: Power Platform architect. Using the catalog and threat cross-check, produce
final verdicts and the budget gate.

**Pathology verdicts**:

| Pathology | Verdict | Key Evidence (row numbers) | Remediation |
|-----------|---------|---------------------------|-------------|
| Trigger Storm | PRESENT / RISK / ABSENT | | |
| Missing Trigger | PRESENT / RISK / ABSENT | | |
| Circular Trigger | PRESENT / RISK / ABSENT | | |

Remediation column: specific construct only -- name the flow, the step, the condition
expression, or the plugin registration setting.

**Budget gate** (evaluate before writing recommendations):
  M = [from Pass 2]. Side effects present = [YES/NO].
  Gate (M >= 3 AND side effects exist): [MET / NOT MET]

If MET -- budget section:
| Budget Metric | Value |
|---------------|-------|
| Cascade depth M | |
| Estimated API requests per occurrence | |
| Power Platform daily request limit | |
| Budget consumed per occurrence (%) | |
| Estimated run duration | |

**Confidence note**: For any verdict where the Pass 1 hypothesis was confirmed, note
confidence = HIGH. For verdicts that contradicted the hypothesis, note what changed
from expectation.

---

**Save artifact**: simulations/flow/trigger/{topic}-trigger-{date}.md
Frontmatter: skill, topic, date, M, N, threats_predicted, threats_confirmed,
budget_gate_fired, pathologies_found.
```

---

## V-04 -- Combined: Output Format + Lifecycle Emphasis

**Axes combined**: (1) Dual-population Fires?/YES/NO table as first structural output (C-11); (2) budget gate evaluates immediately after table, before any pathology section (C-10)
**Hypothesis**: C-10 and C-11 are co-dependent -- C-11 produces the M count and side-effect inventory that C-10 needs. Combining them in a locked sequence (table -> budget gate -> pathology) means C-10 can never be skipped because it has no storm verdict to wait for; it runs on gate condition immediately after the table values are available. This is the minimal combination to co-satisfy both new rubric criteria.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

Follow this exact sequence. Each section feeds the next. Do not reorder.

---

## SECTION 1 -- SCENARIO

| Field | Value |
|-------|-------|
| Table | [entity name] |
| Change type | [field update / create / delete / status change / custom event] |
| Field changed | [schema name] |
| Old value | [prior state or "N/A"] |
| New value | [new state or "N/A"] |
| Solution layer | [Default / Managed / Unmanaged -- or "inferred: SOURCE"] |
| Environment | [Dev / Test / Production -- or "inferred"] |
| License tier | [per-user / per-flow / pay-as-you-go / premium -- or "assumed: TIER"] |

---

## SECTION 2 -- UNIFIED TRIGGER REGISTRY

This table is the single source of truth for all downstream sections.

Include every automation registered for this entity and event -- those that fire AND those
that do not. This is the only place triggers are enumerated. Supplemental lists are not
permitted.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

Column enforcement:
- **Fires?**: YES or NO. No row may omit this column. No trigger may be omitted from the table.
- **#**: Firing sequence number for YES rows (execution order). "--" for NO rows.
- **Condition Expression**: non-empty for all rows. "No filter -- always fires on [event type]"
  is valid for unconditional YES rows. State the failed expression for NO rows.
- **Sync/Async**: for YES rows only; "--" for NO.
- **Inputs/Outputs**: for YES rows, concrete values. For NO rows: "--".
- **Side Effects**: for YES rows, name all external state changes or write "none". "--" for NO.

Registry summary (write after table):
```
M (Fires? = YES) = ___
N (total rows)   = ___
Non-firing       = ___
YES rows with Side Effects != "none": ___ [list automation names or "none"]
```

---

## SECTION 3 -- BUDGET GATE (runs before pathology -- mandatory)

This section uses values from Section 2. It does not wait for a storm verdict.

Gate condition: M >= 3 AND at least one YES row has Side Effects != "none"

```
M                     = ___ [from registry summary]
Side effects present  = ___ YES/NO [cite row automation names]
Gate condition MET    = ___ YES/NO
```

**If gate MET:**

| Budget Metric | Estimate | Calculation Basis |
|---------------|----------|-------------------|
| Cascade depth M | | row count from Section 2 |
| API requests per occurrence | | [sum per-automation: Dataverse calls + connector calls + sends] |
| Power Platform daily request limit | | [state license tier and its daily limit] |
| Budget consumed per occurrence (%) | | (requests / daily limit) x 100 |
| Estimated run duration | | [sync chain duration + async chain duration] |

Show calculation basis. "Unknown" is not acceptable -- estimate with stated assumptions.

**If gate NOT met:**

> Budget gate NOT triggered: M = [N], side effects = [YES/NO with count]. No budget section
> required.

---

## SECTION 4 -- PATHOLOGY DETECTION

Reference Section 2 rows by # or name.

| Pathology | Verdict | Evidence | Remediation |
|-----------|---------|----------|-------------|
| **Trigger Storm** | PRESENT / RISK / ABSENT | | |
| **Missing Trigger** | PRESENT / RISK / ABSENT | | |
| **Circular Trigger** | PRESENT / RISK / ABSENT | | |

For each PRESENT or RISK verdict:
- **Evidence**: specific row numbers and data path (e.g., Row 2 output field X -> Row 4 fires on
  field X -> Row 4 output creates child record -> Row 1 fires on child record create)
- **Remediation**: exact construct (flow condition node, plugin depth check, Copilot topic
  condition, concurrency limit setting, trigger filter expression)

For each ABSENT verdict:
- State the architectural reason (not "no issues found")

---

## SECTION 5 -- SUMMARY

Two sentences: what fired, any pathology found, budget gate result. One recommendation if
any verdict is PRESENT or RISK.

---

**Save artifact**: simulations/flow/trigger/{topic}-trigger-{date}.md
Frontmatter: skill, topic, date, M, N, budget_gate_fired (boolean), pathologies_found (list),
storm_depth (number or "N/A").
```

---

## V-05 -- Combined: All Four Axes (R2 Golden Candidate)

**Axes combined**: (1) Dual-population table as sole enumeration surface (C-11); (2) budget gate before pathology (C-10); (3) threat analyst leads (C-04 depth); (4) formal audit-report register (versus R1 V-04 conversational mode which weakened C-06)
**Hypothesis**: R2 golden candidate. Threat declaration primes C-04 completeness before the table is built. The dual-population table structurally satisfies C-11 and produces M+side-effect values. The pre-pathology budget gate fires on those values before any storm confirmation, structurally satisfying C-10. Formal audit register addresses the shallow C-06 condition evaluation produced by the conversational register in R1 V-04. Phase 2d hypothesis cross-check mitigates the confirmation bias risk introduced by threat-first enumeration.

```
You are running /flow:trigger for topic: {topic}.

This simulation runs in four phases. Follow phase boundaries exactly. Do not merge phases.

---

## PHASE 1 -- THREAT DECLARATION

**Role**: Power Platform Pathology Specialist

Before any enumeration, state your prior expectations for this scenario.

**Triggering change**: {signal}

1. **Storm exposure**: Given this entity type and change event, what automation chains are
   structurally likely? Name the most plausible cascade path (e.g., "status-change flow ->
   notification flow -> approval record create -> approval trigger chain").

2. **Coverage gaps**: What automation types are typically registered for this change type
   that, if absent, represent a business logic gap? List two or three expected types (e.g.,
   "audit trail plugin, manager notification flow, SLA recalculation trigger").

3. **Re-entry risk**: What field types in this entity domain are common circular-trigger
   candidates? Name the pattern (e.g., "calculated rollup field updated by a flow whose
   trigger condition is the same rollup field").

4. **Hypothesis statement**:
   - Storm: "I expect [storm / no storm] because [one sentence]."
   - Missing: "I expect [coverage gaps / complete coverage] in [area]."
   - Circular: "I expect [re-entry risk / clean separation] because [one sentence]."

End Phase 1: "Threat hypotheses declared. Proceeding to enumeration."

---

## PHASE 2 -- UNIFIED TRIGGER REGISTRY

**Role**: Power Automate / Dataverse Enumeration Expert

**2a. Scenario block** (complete before table):
```
Entity/Table:       ___
Change type:        ___
Field changed:      ___ [schema name]
Old value:          ___
New value:          ___
Solution layer:     ___ [or "inferred from: SOURCE"]
Environment:        ___ [or "inferred"]
License tier:       ___ [or "assumed: TIER -- basis: REASON"]
```

**2b. Dual-population trigger table**

List every automation registered for this entity and event -- firing AND non-firing -- in
one table. This table is the sole enumeration surface. No supplemental trigger lists.

| # | Automation Name | Type | Fires? | Condition Expression | Sync/Async | Inputs | Outputs | Side Effects |
|---|-----------------|------|--------|---------------------|------------|--------|---------|--------------|

Column enforcement:
- **Fires?**: YES or NO. Every registered automation must appear as exactly one row.
- **#**: Integer sequence for YES rows (execution order). "--" for NO rows.
- **Type**: Cloud Flow / Dataverse Plugin / Business Rule / Copilot Studio Topic / Custom
  Connector / Other
- **Condition Expression**: mandatory for all rows. "Always fires -- no filter set on [event
  type]" is valid. State the failed expression for NO rows. Do not write "N/A."
- **Sync/Async**: YES rows only. Pre-commit = Sync. Post-commit = Async. "--" for NO rows.
- **Inputs**: YES rows: concrete values (field schema name, OData value, token name). "--" for NO.
- **Outputs**: YES rows: concrete state changes (field schema name written, entity name created,
  message type sent, API endpoint called). "--" for NO.
- **Side Effects**: YES rows: external state changes with specifics (email recipient role, audit
  table schema name, child entity schema name, API hostname) or "none". "--" for NO.

**2c. Registry summary**:
```
M (Fires? = YES)                     = ___
N (total rows)                       = ___
Non-firing registered                = ___
YES rows with Side Effects != "none" = ___ [list automation names or "none"]
```

**2d. Hypothesis cross-check** (against Phase 1 declarations):
- Storm hypothesis: [confirmed likely / not supported / inconclusive] -- [one sentence from table]
- Coverage gap hypothesis: [confirmed / not supported / inconclusive] -- [one sentence]
- Re-entry hypothesis: [confirmed / not supported / inconclusive] -- [one sentence]
- Unexpected findings: [trigger types in the catalog not anticipated by Phase 1, or "none"]

---

## PHASE 3 -- BUDGET GATE

**Role**: Power Platform Capacity Analyst

This phase runs before pathology verdicts. Gate condition does not require a confirmed storm.

```
Gate check:
  M                           = ___ [Phase 2 registry summary]
  M >= 3?                     = YES / NO
  Any Side Effects != "none"? = YES / NO [name automations from Phase 2c]
  Gate MET?                   = YES / NO
```

**If gate MET** -- complete the budget table:

| Budget Metric | Value | Calculation Basis |
|---------------|-------|-------------------|
| Cascade depth M | | count of YES rows |
| API requests per occurrence | | [sum: per-automation action counts from Phase 2 Outputs/Side Effects] |
| Power Platform daily request limit | | license tier: ___ -- limit: ___ requests/day |
| Budget consumed per occurrence (%) | | (requests / limit) x 100 |
| Estimated run duration -- sync chain | | [sum of sync step durations] |
| Estimated run duration -- async chain | | [longest async path duration] |
| Budget risk level | LOW / MEDIUM / HIGH | [LOW < 1%, MEDIUM 1-10%, HIGH > 10% per occurrence] |

Estimation rule: where exact action counts are unknown, state the minimum plausible count
and reason from there. Do not write "unknown" -- estimate and declare confidence level.

**If gate NOT MET:**
> Budget gate: NOT TRIGGERED
> M = [N] (< 3, or M = [N] with no side effects identified)
> No budget section required for this simulation.

---

## PHASE 4 -- PATHOLOGY VERDICTS AND REMEDIATION

**Role**: Power Platform Architect

Using the trigger table from Phase 2 and budget data from Phase 3:

| Pathology | Verdict | Evidence | Remediation |
|-----------|---------|----------|-------------|
| Trigger Storm | PRESENT / RISK / ABSENT | | |
| Missing Trigger | PRESENT / RISK / ABSENT | | |
| Circular Trigger | PRESENT / RISK / ABSENT | | |

**Evidence column**: cite Phase 2 row # and data path. For storm: trace the full cascade
(e.g., "Row 3 output: Status = Approved -> Row 5 trigger condition: Status changed -> Row 5
output: Owner reassignment -> Row 2 trigger condition: Owner changed -> loop closes at Row 2").

**Remediation column**: reference exact construct with specifics:
- Power Automate: "add trigger condition '@not(equals(triggerOutputs()?['body/FIELDNAME'], VALUE))'
  to [Flow Name]" / "set concurrency control to 1 on [Flow Name]"
- Dataverse Plugin: "check context.Depth > 1 at plugin entry in [Plugin Class Name]; return
  early if depth exceeded" / "add PreImages check: if old value == new value, skip processing"
- Copilot Studio: "add condition node '[System.Activity.Name] is not equal to Automated' before
  topic [Topic Name] trigger fires"
- For ABSENT verdicts: state the specific guard mechanism present in the current configuration
  -- not "no issues detected"

**Phase 1 hypothesis reconciliation**: For each Phase 1 hypothesis, state confirmed or refuted
and what the discrepancy reveals (e.g., "Storm hypothesis confirmed -- cascade path matched
prediction; additional async branch found that was not anticipated").

---

**Save artifact**: simulations/flow/trigger/{topic}-trigger-{date}.md
Frontmatter: skill, topic, date, entity, environment, field_changed, M, N,
budget_gate_fired (boolean), storm_depth (integer or "N/A"), pathologies_found
(list: storm/missing/circular), hypothesis_accuracy (phase1_matches/3).
```

---

## Round 2 Design Notes

### Variation axis coverage

| Axis | R1 approach | R2 approach | Change |
|------|------------|-------------|--------|
| Output format | Single-axis table (V-01): columns per trigger | Dual-population Fires?/YES/NO (V-01, V-04, V-05) | Table now includes non-firing triggers explicitly |
| Role sequence | Enumeration-first two-pass (V-02) | Threat-first three-pass (V-03, V-05) | Roles reversed; threat declaration primes enumeration |
| Lifecycle emphasis | Scenario boundary gates enumeration (V-03) | Budget gate runs before pathology (V-02, V-04, V-05) | Phase ordering enforces C-10 before C-04 |
| Phrasing register | Conversational debug (V-04) | Formal audit report (V-05) | Addresses C-06 weakness from R1 V-04 |
| Storm quantification | Dedicated STORM BUDGET section (V-05 only) | Budget gate section in all variations | C-10 normalized across all R2 variations |

### Predicted C-10 / C-11 pass rates

| V | C-10 (Budget Gate) | C-11 (Dual-Population Table) |
|---|-------------------|------------------------------|
| V-01 | RISK -- gate present but after pathology | PASS -- table is first output |
| V-02 | PASS -- gate section is structurally before pathology | RISK -- table format not enforced |
| V-03 | RISK -- gate present in Pass 3 but verdict-adjacent | RISK -- table present but no Fires?/YES/NO enforcement |
| V-04 | PASS -- Section 3 runs before Section 4 by structure | PASS -- dual-population table enforced |
| V-05 | PASS -- Phase 3 structurally precedes Phase 4 | PASS -- dual-population table is sole enumeration surface |

### C-09 inheritance from R1

V-05 R1 closed C-09 (storm quantification). All R2 variations inherit the budget section template
from R1 V-05. C-09 is no longer the differentiating criterion -- C-10 and C-11 are.

### Golden candidate

**V-05** is the R2 synthesis target:
- Threat declaration primes C-04 completeness and C-05 side-effect specificity
- Dual-population table structurally satisfies C-11 and produces M+side-effect values
- Pre-pathology budget gate structurally satisfies C-10 without storm confirmation dependency
- Formal audit register addresses C-06 shallow condition evaluation from R1 V-04

**V-04** is the strongest single-principle combination candidate: it isolates the C-10/C-11
co-satisfaction mechanism cleanly, without the threat-first complexity of V-05. If V-04 fails
C-10 or C-11, the failure is attributable to the mechanism itself, not to the threat-lead phase.
