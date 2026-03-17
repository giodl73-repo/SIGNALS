---

## flow-trigger Variations R1 -- Summary

**5 variations, 4 axes:**

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Output format (table-per-trigger) | Pre-printed columns make C-01/C-02/C-03/C-05/C-06 structurally unavoidable |
| **V-02** | Role sequence (enumeration before pathology) | Separating catalog from analysis prevents conflation and post-hoc enumeration |
| **V-03** | Lifecycle emphasis (scenario boundary first) | Anchoring C-07 before enumeration prevents ambiguous trigger attribution |
| **V-04** | Phrasing register (conversational debug mode) | Debug-session framing produces more concrete I/O for C-03 |
| **V-05** | Combined: role sequence + table + storm quantification | All critical surfaces pre-printed; storm budget section closes C-09 |

---

### Key design decisions

**C-09 is the differentiating criterion.** Storm quantification (cascade depth + API budget impact) is the aspirational criterion most likely to fail in R1 -- no prior variation demands it by structure. V-05 adds an explicit `STORM BUDGET` section with a pre-printed template (depth, API requests, platform limit, % budget consumed, run duration). V-01 through V-04 rely on the model volunteering this analysis.

**V-01 vs V-02 is the interesting competition.** The table format (V-01) and the two-pass role separation (V-02) both improve C-01 enumeration completeness -- one by column enforcement, one by preventing the model from shortcutting enumeration through early pathology detection. V-05 combines them.

**V-04 is the conversational baseline.** It trades the formal template overhead for grounded specificity -- a useful signal for whether register alone can drive C-03 (inputs/outputs) without structural enforcement.

**Golden candidate: V-05.** Two-pass separation + pre-printed table + storm budget section covers all 9 criteria structurally, with no omission path for the criteria that free-form prompts typically miss (C-06 condition evaluation, C-09 storm quantification).
 a row in a pre-printed table with fixed columns; pathology detection is a separate required section below the table
**Hypothesis**: Pre-printed column headers (firing order, sync/async, inputs, outputs, side effects, gate conditions) make C-01 through C-06 structurally unavoidable. The model cannot produce a well-formed table row without filling in all six columns. A model that would omit side effects in prose will not leave the "Side Effects" column blank in a table.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

---

## SCENARIO

Triggering change: {signal}
Environment: [State the Dataverse environment, solution layer, and table name. If not provided, infer from topic context and note "inferred."]

---

## STEP 1: TRIGGER CATALOG

List every automation registered against this table or event. Include: Power Automate cloud flows (automated, instant, scheduled), Dataverse plug-ins (pre-operation and post-operation), Business Rules, and Copilot Studio triggers if applicable.

For each trigger found, fill in one row of the table below. Do not leave any column blank. If a value is "none" or "N/A", write it explicitly.

| # | Trigger Name | Type | Sync / Async | Gate Condition | Inputs | Outputs | Side Effects |
|---|--------------|------|--------------|----------------|--------|---------|--------------|
| 1 | [name] | Flow / Plug-in / Business Rule / Copilot | Sync / Async | [filter condition or scope that determines whether it fires] | [fields read, record state consumed] | [fields written, messages sent, records created] | [downstream effects: field writes that could trigger another automation, emails, queue messages] |
| 2 | ... | ... | ... | ... | ... | ... | ... |

[Add rows until all triggers are listed. Every trigger that fires for the stated change must appear. Every trigger that is registered but does NOT fire must also appear, with Gate Condition explaining why it is filtered out.]

Firing order note: The row number (#) represents the firing sequence. Renumber rows if the execution order differs from the catalog order. Synchronous triggers fire before the database transaction commits; list them first within their execution scope. Asynchronous triggers fire after commit; list them after.

---

## STEP 2: PATHOLOGY SCAN

Review the catalog above and answer each of the three pathology questions. Do not skip a question. If a pathology is absent, explicitly confirm it with evidence.

**Trigger Storm**
Does any single field change or event cause more than 3 triggers to fire in sequence, or cause a trigger to re-enter the same automation? State: PRESENT or ABSENT.
If PRESENT: list the cascade chain (Trigger A -> Trigger B -> Trigger C...) and count the total triggers in the chain.
If ABSENT: state which condition or scope setting prevents it.

**Missing Triggers**
Given the triggering change ({signal}), are there automations that should logically fire but are not registered or are filtered out unexpectedly? State: PRESENT or ABSENT.
If PRESENT: name each missing trigger and explain what business logic is unprotected as a result.
If ABSENT: confirm the registered triggers cover the expected automation surface.

**Circular Triggers**
Does any trigger write a field or record that would cause another trigger (or itself) to fire again, creating a loop? State: PRESENT or ABSENT.
If PRESENT: describe the loop (Trigger A writes Field X -> Trigger B fires on Field X -> Trigger B writes Field Y -> Trigger A fires on Field Y).
If ABSENT: identify the condition or design pattern that breaks the potential loop.

---

## STEP 3: REMEDIATION (if pathologies found)

For each pathology marked PRESENT in Step 2, write one remediation entry:

- [Pathology type]: [Trigger(s) involved]
  Fix: [Concrete remediation using a specific Power Automate or Copilot Studio construct -- e.g., "Add a condition checking OldValue != NewValue before the flow body", "Set the plug-in execution scope to Parent:False to prevent re-entry", "Register a throttle using the concurrency control setting on the cloud flow."]
  Platform reference: [Power Automate condition / Plug-in IPluginExecutionContext.Depth / Copilot Studio topic condition / other]

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: skill, topic, date, triggering_change, environment, trigger_count, pathologies_found (list), storm_depth (if applicable).
```

---

## V-02 -- Single Axis: Role Sequence (Enumeration Before Pathology)

**Axis**: Role sequence -- Pass 1 is an Enumeration Analyst who catalogs every trigger; Pass 2 is a Pathology Analyst who receives the catalog and analyzes it for storm, missing, and circular patterns. The two passes do not merge.
**Hypothesis**: When enumeration and pathology detection are the same pass, models frequently use pathology detection as a shortcut -- they identify one storm and stop enumerating. Separating the passes forces the Enumeration Analyst to produce a complete catalog before any pathology reasoning begins. Expected to improve C-01 completeness and C-04 accuracy.

```
You are running /flow:trigger for topic: {topic}.

This skill executes two sequential passes. Do not merge the passes. Complete Pass 1 fully before starting Pass 2.

---

## PASS 1: ENUMERATION ANALYST

**Role**: You are an Enumeration Analyst with expertise in Power Automate and Dataverse. Your only job in this pass is to catalog every automation registered for this table and event. You are not analyzing for pathologies yet.

**Triggering change**: {signal}

**Instructions**:

1. State the scenario boundary:
   - Table: [Dataverse table or entity name]
   - Change type: [field change / record create / record delete / status change / other]
   - Field changed: [field name, old value -> new value, or "N/A if event-based"]
   - Environment / solution: [state or note "inferred from topic"]

2. Enumerate every automation registered against this table and event. For each one:
   - Name and type (cloud flow / plug-in / business rule / Copilot trigger / other)
   - Execution timing: synchronous (pre-commit) or asynchronous (post-commit)
   - Gate condition: the filter, scope, or condition that determines whether it fires for this specific change
   - Fires for this change? YES / NO (and if NO, state which gate condition filters it out)

3. For each trigger that fires (YES), detail:
   - Inputs: what data does it read? (triggering record fields, context data, related records)
   - Outputs: what does it produce? (field writes, record creates, emails, queue messages, HTTP calls)
   - Side effects: does any output write a field or record that could itself trigger another automation?

4. Number the triggers in firing sequence. Sync triggers first (ordered by plug-in execution pipeline stage if relevant), then async.

5. At the end of Pass 1, write: "Pass 1 complete. Catalog contains [N] registered triggers, [M] fire for this change."

---

## PASS 2: PATHOLOGY ANALYST

**Role**: You are a Pathology Analyst. You have received the catalog from Pass 1. Your job is to analyze it for the three trigger pathology types. Do not add new triggers to the catalog. If you find a trigger was omitted in Pass 1, note the gap separately.

**Using the catalog from Pass 1, answer each of the following:**

### Storm Analysis
Review the firing sequence. Does any single change cause a trigger to fire that writes a field, which causes a second trigger to fire, and so on in a cascade?
- State: STORM DETECTED or NO STORM
- If STORM DETECTED: write the full cascade chain. Count total triggers in the chain. Estimate execution budget impact (number of Power Platform API requests consumed, or approximate run duration if determinable).
- If NO STORM: identify the architectural reason (scope condition, missing listener, idempotent writes) that prevents it.

### Missing Trigger Analysis
Based on the triggering change ({signal}), what automations would a developer reasonably expect to fire that are absent from the catalog?
- State: MISSING TRIGGERS FOUND or CATALOG COMPLETE
- If MISSING TRIGGERS FOUND: name each expected-but-absent automation and describe what business logic is exposed as a result.
- If CATALOG COMPLETE: confirm why the catalog covers the expected automation surface.

### Circular Trigger Analysis
Does any trigger in the catalog write a field or create a record that would re-trigger another automation already in the catalog (or the same trigger again)?
- State: CIRCULAR TRIGGER FOUND or NO CIRCULAR TRIGGER
- If CIRCULAR TRIGGER FOUND: trace the loop step by step. Identify where the cycle closes.
- If NO CIRCULAR TRIGGER: identify the condition, depth-check, or design pattern that prevents re-entry.

### Remediation (for each pathology found)
For each pathology marked DETECTED or FOUND:
- Pathology: [type]
- Affected triggers: [names from catalog]
- Remediation: [specific Power Automate / Copilot Studio construct or Dataverse plug-in pattern]
- Implementation note: [where in the platform to apply it]

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: skill, topic, date, triggering_change, trigger_count_registered, trigger_count_fired, pathologies_found (list), storm_depth (if applicable).
```

---

## V-03 -- Single Axis: Lifecycle Emphasis (Scenario Boundary First, Heavy Setup)

**Axis**: Lifecycle emphasis -- the prompt opens with a mandatory SCENARIO DECLARATION section that must be fully specified before enumeration begins; the scenario declaration gates all downstream analysis
**Hypothesis**: Anchoring C-07 (scenario boundary) before any trigger enumeration prevents the most common failure mode: triggers attributed to the wrong field change or wrong environment. A declared scenario also forces the model to distinguish "triggers registered for this table" from "triggers that fire for this specific change" -- a distinction C-01 requires but free-form prompts collapse.

```
You are running /flow:trigger for topic: {topic}.

Your role: Power Automate / Copilot Studio domain expert.

Do not begin trigger enumeration until the SCENARIO DECLARATION section is complete.

---

## SECTION 1: SCENARIO DECLARATION

Complete all fields before proceeding. Every field is required. If a value must be inferred, state the source of the inference.

```
Table:              [Dataverse table or entity name]
Solution layer:     [Managed / Unmanaged / Default solution -- or "inferred from: SOURCE"]
Environment:        [Development / Test / Production -- or "inferred from: SOURCE"]
Change type:        [Record Create / Record Update / Record Delete / Status Change / Custom event]
Field changed:      [Field schema name -- or "N/A" if event-based]
Old value:          [Previous field value -- or "N/A"]
New value:          [New field value -- or "N/A"]
Triggered by:      [User action / System process / Another automation -- infer if not stated]
```

Scenario confirmation: "Simulating: [Field] changed from [OldValue] to [NewValue] on [Table] in [Environment]."

Do not proceed past this line until the scenario confirmation is written.

---

## SECTION 2: TRIGGER REGISTRY

List every automation registered against this table, regardless of whether it fires for the declared scenario. This is the full registry.

For each registered trigger:
- Name and type
- Registered event (create / update / delete / specific field / all fields)
- Fires for declared scenario: YES or NO
- If NO: state the gate condition that filters it out

At the end: "Registry complete: [N] triggers registered, [M] fire for the declared scenario."

---

## SECTION 3: FIRING SEQUENCE

For the M triggers that fire, list them in execution order.

For each trigger, write one block:

```
[#]. [Trigger Name] ([Type]) -- [SYNC | ASYNC]
Gate condition: [What condition was evaluated and passed to allow this trigger to fire]
Inputs: [Fields read, record state consumed, context data]
Outputs: [Fields written, records created, messages sent, HTTP calls made]
Side effects: [Any output that writes data capable of triggering another automation -- or "None"]
```

Number the blocks in firing sequence. Synchronous triggers appear before asynchronous. Within sync, order by plug-in pipeline stage (Pre-Validation -> Pre-Operation -> Post-Operation) if applicable.

---

## SECTION 4: PATHOLOGY ANALYSIS

Address all three pathology types. Do not skip one. "ABSENT" is a valid answer only if accompanied by evidence.

**4a. Trigger Storm**
A trigger storm occurs when one change causes a cascade of triggers, each writing data that fires the next.
Assessment: [STORM DETECTED | ABSENT]
Evidence: [Trace the cascade if detected, or name the design feature that prevents it if absent]

**4b. Missing Triggers**
A missing trigger is one that a developer would expect to fire for the declared scenario but is absent from the registry.
Assessment: [MISSING TRIGGERS FOUND | CATALOG COMPLETE]
Evidence: [Name each missing trigger and the unprotected business logic, or confirm the registry is complete]

**4c. Circular Triggers**
A circular trigger occurs when a trigger's output writes a field or record that causes another trigger (or itself) to fire again.
Assessment: [CIRCULAR TRIGGER FOUND | ABSENT]
Evidence: [Trace the loop if found, or name the break condition if absent]

---

## SECTION 5: REMEDIATION

For each pathology found in Section 4, write one entry:

Pathology: [Storm | Missing | Circular]
Triggers involved: [names]
Recommended fix: [specific Power Automate condition / Dataverse plug-in depth check / Copilot Studio topic condition / throttle setting]
Where to apply: [exact location in the platform: flow condition node / plug-in registration / solution layer]

If no pathologies were found: write "No pathologies detected. No remediation required."

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: skill, topic, date, table, environment, field_changed, old_value, new_value, trigger_count_registered, trigger_count_fired, pathologies_found (list).
```

---

## V-04 -- Single Axis: Phrasing Register (Conversational Debug Mode)

**Axis**: Phrasing register -- second-person, conversational, debug-session framing; the model is "tracing what just happened" rather than "enumerating a catalog as a domain expert"
**Hypothesis**: Debug-session framing produces more concrete inputs/outputs (C-03) because the model simulates an actual investigation rather than an academic enumeration. The register lowers the barrier to specificity -- "what did this flow actually read?" is a more grounded question than "state the inputs for this trigger." Trade-off: the informal register may produce shallower condition evaluation (C-06) and may underweight async triggers, which are less visible in a debug session mental model.

```
You are debugging a trigger trace for: {topic}.

The change that happened: {signal}

Walk through exactly what fires. You're an engineer who has the Power Platform admin center open, the solution explorer visible, and the plug-in trace log in a second tab. Tell me what you see.

---

**First: set the scene.**

What table did the change happen on? What field changed, from what to what? What environment are you looking at? If anything is unclear, state your assumption and keep moving.

---

**Now walk the trigger sequence.**

Start with whatever fires first. For each thing that fires:

- What is it? (Cloud flow, plug-in, business rule, Copilot topic -- name it)
- Does it run before the database commits, or after? (Sync or async)
- What condition did it check before firing? Did it pass? Why?
- What did it read from the record? What did it write, send, or create?
- Did anything it wrote or created set off something else?

Number each item. Keep them in the order they actually execute.

Once you've worked through everything that fires, go back and note anything that was registered but didn't fire -- and why it got skipped.

---

**Now look for trouble.**

Three things to check:

1. **Too many fires**: Did one field change set off a chain? How long did the chain get? If the chain is longer than 3 steps, name every step and count them.

2. **Missing automations**: Is there something that should have fired for this change but didn't? What's not covered that you'd expect to be covered?

3. **Loops**: Does anything that fired write a field that would cause another trigger to fire on it -- possibly looping back to something earlier in the sequence?

For each one: tell me if it's a problem or not, and show your work.

---

**If you found a problem: tell me how to fix it.**

For each issue you flagged above, give me one concrete fix. Not "add a condition" -- tell me which condition, on which flow or plug-in, checking which field or context value. Name the exact Power Automate node or Dataverse registration setting where the fix goes.

---

**Wrap up.**

One paragraph: what fired, in what order, any problems found, and whether the automation surface for this change is healthy or needs attention.

---

**Save your trace to**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Include in the frontmatter: skill, topic, date, triggering_change, trigger_count_fired, pathologies_found (list), environment (stated or inferred).
```

---

## V-05 -- Combined: Role Sequence + Table Format + Storm Quantification

**Axes**: Role sequence (enumeration-first, two passes) + output format (pre-printed table) + explicit storm budget section (quantification emphasized)
**Hypothesis**: Maximum coverage across all 9 criteria. The enumeration pass guarantees C-01 completeness and C-07 scenario anchoring. The table format guarantees C-02/C-03/C-05/C-06 by structural enforcement. The dedicated STORM BUDGET section forces C-09 and makes C-08 remediations concrete by anchoring them to platform limits. This is the golden candidate for R1.

```
You are running /flow:trigger for topic: {topic}.

This skill executes in two passes with a fixed output format. Follow the structure exactly.

---

## PASS 1: ENUMERATION

**Role**: Enumeration Analyst -- Power Automate / Dataverse / Copilot Studio domain expert.

**Step 1 -- Scenario declaration** (required before enumeration begins):

```
Table:          [Dataverse table / entity name]
Environment:    [Dev / Test / Prod -- or "inferred from: SOURCE"]
Solution:       [Solution name or layer]
Change type:    [field update / record create / record delete / status change]
Field changed:  [schema name -- or "N/A"]
Old value:      [prior value -- or "N/A"]
New value:      [new value -- or "N/A"]
```

**Step 2 -- Trigger catalog table**:

Fill every cell. "None" and "N/A" are valid -- blank is not.

| # | Trigger Name | Type | Fires? | Sync / Async | Gate Condition (why it fires or skips) | Inputs (fields / context read) | Outputs (fields written / records created / messages sent) | Side Effects (outputs that could trigger another automation) |
|---|--------------|------|--------|--------------|----------------------------------------|-------------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| 1 | [name] | Flow / Plug-in / Business Rule / Copilot / Other | YES / NO | Sync / Async / N/A | [condition evaluated; state why it passes or fails for this change] | [list fields and context data read] | [list all writes, creates, sends] | [any output that writes data capable of re-triggering -- or "None"] |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... |

[Add rows until all registered triggers are listed -- both those that fire (YES) and those filtered out (NO).]

Firing sequence: rows with YES are numbered in execution order. Sync rows appear before Async rows. Renumber if needed.

Pass 1 summary: "Catalog complete: [N] triggers registered, [M] fire for this change."

---

## PASS 2: PATHOLOGY ANALYST

**Role**: Pathology Analyst. You have the catalog from Pass 1. Analyze it. Do not add triggers. If you find a gap in the catalog, flag it separately as a catalog error.

---

### 2a. Trigger Storm Analysis

A storm is a cascade where Trigger A fires and writes data, causing Trigger B to fire, which writes data, causing Trigger C to fire, and so on.

Storm assessment: [STORM DETECTED | NO STORM]

If STORM DETECTED:
- Cascade chain: [Trigger A (output: Field X) -> Trigger B (reads Field X, output: Record Y) -> Trigger C (fires on Record Y)...]
- Storm depth: [N triggers in the cascade]
- Budget estimate: [Estimate Power Platform API requests consumed by the cascade, OR approximate total execution duration. Reference: Power Platform daily request limits by license tier, or per-flow run duration cap of 30 days.]
- Remediation: [Specific fix -- e.g., "Add OldValue != NewValue condition to Trigger B's filter, breaking the write-re-trigger loop. Apply in: Power Automate flow condition node immediately after the trigger step."]

If NO STORM:
- Prevention mechanism: [What architectural decision or condition prevents cascade -- e.g., "Trigger B is scoped to record creates only; the update from Trigger A does not fire a create event."]

---

### 2b. Missing Trigger Analysis

Given the declared change ({signal}), what automation would a developer reasonably expect to find registered but is absent from the catalog?

Missing trigger assessment: [MISSING TRIGGERS FOUND | CATALOG COMPLETE]

If MISSING TRIGGERS FOUND:
For each missing trigger:
- Expected automation: [description of what should exist]
- Business logic exposed: [what consequence or workflow is unprotected without it]
- Remediation: [where to register it -- solution layer, table registration, trigger event type]

If CATALOG COMPLETE:
- Confirmation: [state why the registered triggers cover the expected automation surface for this change]

---

### 2c. Circular Trigger Analysis

A circular trigger occurs when a trigger writes a field or creates a record that causes another trigger to fire on it -- closing a loop back to a trigger already in the sequence.

Circular assessment: [CIRCULAR TRIGGER FOUND | NO CIRCULAR TRIGGER]

If CIRCULAR TRIGGER FOUND:
- Loop trace: [Trigger A writes Field X -> Trigger B fires (registered on Field X) -> Trigger B writes Field Y -> Trigger A fires (registered on Field Y) -> loop closes]
- Loop closure point: [where in the sequence the cycle re-enters]
- Remediation: [specific break -- e.g., "Add IPluginExecutionContext.Depth > 1 check at the start of Trigger A's plug-in code to prevent re-entrant execution." OR "Add a condition to Trigger B checking that the triggering record's modified_by is not the system service account used by Trigger A."]

If NO CIRCULAR TRIGGER:
- Break condition: [what prevents re-entry -- scope setting, depth check, field guard, idempotent write pattern]

---

### 2d. Storm Budget Section (complete if storm detected OR if storm risk is elevated)

Complete this section if: a storm was detected, OR if [M] (triggers that fire) >= 3 and any trigger has a side effect that writes a field.

```
Storm depth:         [N triggers in cascade -- or "N/A"]
API requests (est):  [N requests for the cascade, computed as: sum of actions per trigger in cascade]
Platform limit:      [State the relevant daily limit for the license tier assumed, e.g., "10,000 API requests/day per user (Microsoft 365 license)"]
Budget consumed:     [N requests / daily limit = X% of daily budget per occurrence]
Run duration (est):  [Estimate total wall-clock time for cascade if async; note if any step could approach the 30-day flow timeout]
Risk level:          [LOW / MEDIUM / HIGH -- with justification]
```

---

**Save artifact**: `simulations/flow/trigger/{topic}-trigger-{date}.md`
Frontmatter: skill, topic, date, table, environment, field_changed, old_value, new_value, trigger_count_registered, trigger_count_fired, pathologies_found (list), storm_depth (number or "N/A"), storm_api_requests (number or "N/A").
```

---

## Round 1 Design Notes

### Variation axis coverage

| Axis | Variations | Single-axis | Combined |
|------|-----------|-------------|---------|
| Output format (table vs prose) | V-01, V-05 | V-01 | V-05 |
| Role sequence | V-02, V-05 | V-02 | V-05 |
| Lifecycle emphasis | V-03, V-05 | V-03 | V-05 |
| Phrasing register | V-04 | V-04 | V-05 (formal) |
| Storm quantification emphasis | V-05 | -- | V-05 |

### Predicted failure modes per variation

| V | Most likely C to miss | Reason |
|---|----------------------|----|
| V-01 | C-09 (storm quantification) | Table format covers structural criteria; no explicit budget section |
| V-02 | C-06 (condition evaluation) | Two-role separation improves C-01 and C-04 but condition column not pre-printed |
| V-03 | C-09 (storm quantification) | Heavy lifecycle emphasis covers setup and enumeration; budget section absent |
| V-04 | C-06 (condition evaluation) | Conversational register may produce concrete I/O but shallow condition coverage |
| V-05 | None predicted | All surfaces pre-printed; storm budget section added to close C-09 |

### C-09 is the differentiating criterion

C-09 (storm quantification: cascade depth, API request budget impact) is the aspirational criterion most likely to fail in R1 prompts that do not explicitly require it. V-05's dedicated STORM BUDGET section is the structural guarantee. V-01 through V-04 rely on the model volunteering this analysis.

### Golden candidate

**V-05** is the direct R1 synthesis target:
- Scenario declaration gates enumeration (C-07)
- Pre-printed table enforces C-01/C-02/C-03/C-05/C-06 structurally
- Two-pass separation prevents enumeration shortcutting (C-01/C-04)
- Explicit storm budget section targets C-09
- Remediation blocks per pathology target C-08

**V-01** and **V-02** are the strongest single-axis candidates. The open research question: does the pre-printed table (V-01) or the two-pass role separation (V-02) more reliably produce a complete trigger catalog? These are mutually reinforcing, which is why V-05 combines them.
