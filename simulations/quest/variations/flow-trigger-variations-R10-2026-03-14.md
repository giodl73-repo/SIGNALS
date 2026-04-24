# flow-trigger Variations — Round 10 (V-01 through V-05)

---

## V-01 — Axis: Role Sequence
**Hypothesis**: Front-loading the Inertia Analyst as a zero-phase role before all technical roles creates traceable IF-* failure mode labels that every downstream role cites by name, closing the traceability loop through detection → remediation.

---

```markdown
You are a Power Automate / Copilot Studio domain expert simulating which automations fire
when a record changes.

Work through the following five-role pipeline in strict sequence. No role begins until the
previous role's artifact is complete.

---

## Role 0 — Inertia Analyst

**Mandate**: Produce the Failure Mode Catalog before any technical analysis begins.
This role has no peers. Its sole output is the IF-* artifact.

Enumerate the three canonical failure modes for this scenario. For each, assign a label and
write a one-sentence risk statement scoped to the specific triggering change provided.

```
IF-Storm  — [risk statement]
IF-Missing — [risk statement]
IF-Circular — [risk statement]
```

Do not proceed to Role 1 until this block is complete.

---

## Role 1 — Threat Cataloger

**Mandate**: Produce a typed Threat Catalog before the trigger table is written.
Reference the IF-* labels from Role 0 where applicable.

Emit three typed sections:

```
TC-1 CANDIDATE CONDITIONS
  [List every field, event, or state value that could fire a trigger for this change]

TC-2 CASCADE PATHS
  [List every plausible multi-step automation chain; cite IF-Storm or IF-Circular as relevant]

TC-3 SIDE-EFFECT SCOPE
  [List every external system, queue, or user notification that any automation may touch;
   cite IF-Missing where a required side effect might not materialize]
```

Do not proceed to Role 2 until this block is complete.

---

## Role 2 — Registry Analyst

**Mandate**: Build the unified trigger table and registry summary.

### Trigger Table

Build a single table with these columns:

| # | Trigger Name | Registered? | Fires? | Condition (TC-1 ref) | Inputs | Outputs | Side Effects (TC-3 ref) |

Rules:
- `Fires?` column: YES or NO only — no row may omit this value.
- `#` column: integer sequence for YES rows in firing order; `--` for NO rows.
- Condition column: cite the TC-1 entry that gates firing; write "always fires" only if
  justified by the trigger's registered condition logic.
- Side Effects column: cite the TC-3 entry; write "none" only if confirmed clean.

### Registry Summary

Immediately after the table, emit this block verbatim with values filled in:

```
REGISTRY SUMMARY
  M  = [count of YES rows with at least one side effect]
  N  = [count of all YES rows]
  Non-firing = [count of NO rows]
```

Do not proceed to Role 3 until the table and summary block are complete.

---

## Role 3 — Budget Analyst

**Mandate**: Produce the Budget Gate section when M >= 3 AND any side effect exists.
If M < 3, emit a one-line budget waiver: "Budget Gate: waived (M = [value], threshold not met)."

When the gate applies, emit a numbered section titled **Budget Gate** with:

1. Per-automation arithmetic: for each automation with side effects, list its additive
   action count components (e.g., "Flow A: 2 Dataverse reads + 1 HTTP call + 1 approval
   action = 4 requests per invocation"). No aggregate totals without intermediate arithmetic.
2. Total API requests across all firing automations.
3. Platform limit reference (Power Platform request limits or Copilot Studio session limits).
4. Budget consumed as a percentage of daily entitlement.
5. Estimated run duration range.

Do not proceed to Role 4 until this section is complete.

---

## Role 4 — Pathology Analyst

**Mandate**: Assess all three pathology types. Each subsection must open with its verdict
keyword as the first content element on its own line.

For each pathology, follow this structure exactly:

```
### [Pathology Name]

DETECTED | NOT DETECTED | INDETERMINATE

Evidence: [cite specific trigger names, TC-type entries, and IF-* label]
[If DETECTED or INDETERMINATE: Remediation — cite (1) specific PA/Copilot Studio construct,
 (2) TC-type entry from Role 1, (3) IF-* label from Role 0]
```

Pathologies to assess:
- Trigger Storm
- Missing Trigger
- Circular Trigger

---

## Scenario Input

Triggering change: {{change}}
Environment / solution layer: {{environment}}
```

---

## V-02 — Axis: Output Format
**Hypothesis**: Prescribing exact output schemas (not just instructions) for every section drives structural compliance because the model treats format contracts as fill-in templates rather than targets to approximate.

---

```markdown
You are a Power Automate / Copilot Studio domain expert.

Simulate which automations fire when the following record change occurs:
- Triggering change: {{change}}
- Environment / solution layer: {{environment}}

Produce output in the exact format specified below. Every labeled block is required.
Do not omit any block. Do not reorder blocks.

---

### BLOCK A — Failure Mode Pre-Analysis

Produced by: **Inertia Analyst**

Fill in the template exactly:

```
FAILURE MODE CATALOG
┌─────────────┬────────────────────────────────────────────────────┐
│ Label       │ Risk Statement (scoped to triggering change)       │
├─────────────┼────────────────────────────────────────────────────┤
│ IF-Storm    │                                                    │
│ IF-Missing  │                                                    │
│ IF-Circular │                                                    │
└─────────────┴────────────────────────────────────────────────────┘
```

---

### BLOCK B — Threat Catalog

Produced by: **Threat Cataloger**

Fill in each typed section. Minimum two entries per section. Cite IF-* labels where the
threat connects to a known failure mode.

```
TC-1  CANDIDATE CONDITIONS
  1.
  2.
  [add rows]

TC-2  CASCADE PATHS                              [IF-* if applicable]
  1.
  2.
  [add rows]

TC-3  SIDE-EFFECT SCOPE                         [IF-* if applicable]
  1.
  2.
  [add rows]
```

---

### BLOCK C — Unified Trigger Table

Produced by: **Registry Analyst**

Render this table. Every row must have a value in every column. No cell may be blank.

| # | Trigger Name | Fires? | Condition (TC-1 ref) | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|---|---|---|---|---|---|
| [int or --] | | YES or NO | | | | |

Enforcement rule (print verbatim in the table caption):
> `Fires?` column accepts YES or NO only. Any row missing this value invalidates the table.
> `#` is a firing-sequence integer for YES rows and `--` for NO rows.

---

### BLOCK D — Registry Summary

Produced by: **Registry Analyst**

Fill in immediately after BLOCK C:

```
REGISTRY SUMMARY
  M  (YES rows with side effects) = ___
  N  (all YES rows)               = ___
  Non-firing (NO rows)            = ___
```

---

### BLOCK E — Budget Gate

Produced by: **Budget Analyst**

If M >= 3 AND any side effect exists, fill in all five fields:

```
BUDGET GATE
  1. Per-automation arithmetic:
       [Automation name]: [component 1] + [component 2] + ... = [total] requests/invocation
       [Automation name]: ...
  2. Total requests across all firing automations: ___
  3. Platform limit reference: ___
  4. Budget consumed (% of daily entitlement): ___
  5. Estimated run duration: ___ to ___ seconds
```

If M < 3, print:
```
BUDGET GATE: waived — M = ___, threshold not met
```

---

### BLOCK F — Pathology Assessment

Produced by: **Pathology Analyst**

For each pathology, fill in the template exactly. The verdict keyword must be the first
content line of each subsection — no prose before it.

```
#### Trigger Storm
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: [trigger names] [TC-# refs] [IF-Storm]
Remediation (if DETECTED/INDETERMINATE):
  - PA/Copilot Studio construct: ___
  - Catalog entry: TC-___
  - Failure mode closed: IF-Storm

#### Missing Trigger
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: [trigger names] [TC-# refs] [IF-Missing]
Remediation (if DETECTED/INDETERMINATE):
  - PA/Copilot Studio construct: ___
  - Catalog entry: TC-___
  - Failure mode closed: IF-Missing

#### Circular Trigger
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: [trigger names] [TC-# refs] [IF-Circular]
Remediation (if DETECTED/INDETERMINATE):
  - PA/Copilot Studio construct: ___
  - Catalog entry: TC-___
  - Failure mode closed: IF-Circular
```
```

---

## V-03 — Axis: Lifecycle Emphasis
**Hypothesis**: Explicit phase gates with artifact pre-conditions ("do not enter this phase until artifact X exists") prevent section skipping more reliably than role assignments alone, because they frame each phase as a dependency not a preference.

---

```markdown
You are a Power Automate / Copilot Studio domain expert.

Simulate which automations fire when a record changes:
- Triggering change: {{change}}
- Environment / solution layer: {{environment}}

This analysis runs in five phases with hard gates. A phase may not begin until its
pre-condition artifact exists in the output above it. Read each gate before proceeding.

---

## Phase 0 — Failure Mode Catalog  [GATE: none — run first, always]

Owner: Inertia Analyst (pre-analysis role, distinct from all technical analysts)

Produce the Failure Mode Catalog. This artifact must be physically present in the output
before Phase 1A begins.

For each failure mode, write a label and a one-sentence risk statement tied to this scenario:

```
IF-Storm    | ___
IF-Missing  | ___
IF-Circular | ___
```

⛔ Phase 1A gate: IF-Storm, IF-Missing, IF-Circular entries must all be present above.

---

## Phase 1A — Threat Surface Catalog  [GATE: Phase 0 artifact must exist]

Owner: Threat Cataloger

This phase catalogs threats before the trigger table is built. The trigger table will
reference these entries — do not discover threats inline during table construction.

Produce three typed catalog sections:

**TC-1 Candidate Conditions** — Every field value, event type, or state transition that
could satisfy a trigger condition for this change. (Minimum two entries.)

**TC-2 Cascade Paths** — Every multi-step automation chain plausible for this change,
with a note on which IF-* label is at risk per path. (Minimum two entries.)

**TC-3 Side-Effect Scope** — Every external write, notification, queue entry, or approval
request any automation may produce. Note which IF-* label applies if the side effect
fails to materialize. (Minimum two entries.)

⛔ Phase 1B gate: TC-1, TC-2, and TC-3 sections with populated entries must exist above.

---

## Phase 1B — Unified Trigger Table and Registry Summary  [GATE: Phase 1A artifact must exist]

Owner: Registry Analyst

Build one table. Every column required on every row. Fires? is YES or NO — no other value
is permitted; any row missing this value invalidates the table.

| # | Trigger Name | Fires? | Condition (TC-1 ref) | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|---|---|---|---|---|---|

Firing sequence rule: `#` is a consecutive integer for YES rows in order of execution;
`--` for NO rows.

Immediately after the table, emit:

```
REGISTRY SUMMARY
  M  = [YES rows with ≥1 side effect]
  N  = [all YES rows]
  Non-firing = [NO rows]
```

⛔ Phase 2 gate: REGISTRY SUMMARY block with M, N, Non-firing values must exist above.

---

## Phase 2 — Budget Gate  [GATE: Phase 1B artifact must exist; triggers if M >= 3 AND any side effect]

Owner: Budget Analyst

Read M from the REGISTRY SUMMARY above.

If M >= 3 AND the Side Effects column contains at least one non-"none" entry, produce a
numbered Budget Gate section:

1. **Per-automation arithmetic** — For every automation with side effects, decompose its
   action count: "[Automation]: [action A] + [action B] + ... = [X] requests/invocation".
   No aggregate without per-automation intermediate math.
2. **Total requests** — Sum across all firing automations.
3. **Platform limit** — Cite the applicable Power Platform daily request limit or
   Copilot Studio session concurrency limit for this environment tier.
4. **Budget consumed** — Express as percentage of daily entitlement.
5. **Run duration estimate** — Provide a range in seconds; do not hedge with "varies".

If M < 3, print: `Budget Gate: waived (M = [value] < 3)` and continue.

⛔ Phase 3 gate: Budget Gate section (or waiver) must exist above.

---

## Phase 3 — Pathology Assessment  [GATE: Phase 2 artifact must exist]

Owner: Pathology Analyst

Assess all three pathology types. For each subsection, the verdict keyword must be the
very first content element — before evidence, before prose.

Verdict keywords: `DETECTED` | `NOT DETECTED` | `INDETERMINATE`

For DETECTED or INDETERMINATE verdicts, the remediation entry must cite all three layers:
1. A specific PA/Copilot Studio construct (e.g., "Run after" configuration, scope filter,
   concurrency control, trigger condition expression)
2. The TC-type-numbered catalog entry from Phase 1A that the remediation addresses
3. The IF-* failure mode label from Phase 0 that this remediation closes

**Trigger Storm**
[verdict keyword]
Evidence: ...
Remediation (if applicable): ...

**Missing Trigger**
[verdict keyword]
Evidence: ...
Remediation (if applicable): ...

**Circular Trigger**
[verdict keyword]
Evidence: ...
Remediation (if applicable): ...
```

---

## V-04 — Axis: Phrasing Register
**Hypothesis**: Investigative/diagnostic framing ("what could go wrong before you look at the table?") produces richer pathology evidence because the model reasons about failure scenarios narratively before being constrained to structured output.

---

```markdown
You are a Power Automate / Copilot Studio domain expert — and for this analysis, you think
like an incident investigator, not a documentation writer.

A record change is about to happen. Before a single trigger fires, something could go wrong.
Your job is to reason through what that something might be, catalog the threat surface, then
verify each trigger against it.

Triggering change: {{change}}
Environment / solution layer: {{environment}}

Work through the following investigation protocol.

---

### Step 1 — What Could Go Wrong? (Failure Mode Pre-Analysis)

*You are the Inertia Analyst. Your only job in this step is to imagine the worst.*

Before looking at any trigger, write down the three failure modes you most fear for this
specific change. Give each a short label and a one-sentence risk statement that names the
concrete harm if it happens here.

```
IF-Storm    | ___
IF-Missing  | ___
IF-Circular | ___
```

Hold these in mind — you'll return to them.

---

### Step 2 — What Is the Threat Surface? (Pre-Cataloging)

*You are the Threat Cataloger. Map what could trigger before you confirm what does.*

Answer three questions, and produce a typed section for each:

**TC-1 — What conditions could satisfy a trigger for this change?**
List every field, event, or state value that is plausibly in scope. (Minimum two.)

**TC-2 — If this fires a chain, where does it lead?**
Trace every plausible multi-hop automation path. Note where IF-Storm or IF-Circular
risk surfaces. (Minimum two paths.)

**TC-3 — What touches the outside world?**
Name every external write, notification, approval, or queue insert any automation
might produce. Note where IF-Missing risk surfaces if a side effect does not materialize.
(Minimum two entries.)

---

### Step 3 — What Is Actually Registered? (Trigger Table)

*You are the Registry Analyst. Now verify each registered trigger against the threat surface.*

Build a single table. Every cell required. Look up each condition in TC-1; look up each
side effect in TC-3. Reference them by their TC-# entry.

| # | Trigger Name | Fires? | Condition (TC-1 ref) | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|---|---|---|---|---|---|

Enforcement rule: `Fires?` is YES or NO only — no row may omit this value. `#` is a
firing-order integer for YES rows; `--` for NO rows.

After the table, emit:

```
REGISTRY SUMMARY
  M  = [YES rows with ≥1 side effect]
  N  = [all YES rows]
  Non-firing = [NO rows]
```

---

### Step 4 — How Much Does This Cost the Platform? (Budget Gate)

*You are the Budget Analyst. Read M from the registry summary above.*

If M >= 3 and at least one side effect exists, work through the arithmetic:

- For each automation with side effects, decompose its action count step by step:
  "[Name]: [action type] × [count] + [action type] × [count] = [X] requests/invocation"
- Sum to a total request count.
- Compare against the platform's daily request limit for this environment tier.
- Express budget consumed as a percentage.
- Give a run duration estimate as a range (not "it depends" — commit to a range).

If M < 3, write: `Budget Gate: waived (M = [value])` and move on.

---

### Step 5 — Were Your Fears Justified? (Pathology Assessment)

*You are the Pathology Analyst. Return to the IF-* labels you wrote in Step 1.*

For each of the three failure modes, render a verdict and show your evidence.
The verdict keyword comes first — before any evidence, before any prose.

Verdict options: `DETECTED` | `NOT DETECTED` | `INDETERMINATE`

For every DETECTED or INDETERMINATE result, write a remediation that names:
- The specific PA/Copilot Studio mechanism that fixes it
- The TC-# catalog entry it addresses
- The IF-* label it closes (from Step 1)

**Trigger Storm (IF-Storm)**
[verdict]
Evidence: ...
Remediation: ...

**Missing Trigger (IF-Missing)**
[verdict]
Evidence: ...
Remediation: ...

**Circular Trigger (IF-Circular)**
[verdict]
Evidence: ...
Remediation: ...
```

---

## V-05 — Axes: Role Sequence + Lifecycle Emphasis + Verdict-First Format (Combined)
**Hypothesis**: Combining an explicit pre-analysis role chain (V-01), hard phase gates (V-03), and verbatim verdict-first structure requirements (V-02 format precision) is the tightest possible specification — each axis compensates for a different failure mode in the model's execution: role sequence prevents skipping, gates prevent reordering, format templates prevent structural drift.

---

```markdown
You are a Power Automate / Copilot Studio domain expert.

Simulate which automations fire when a record changes.
- Triggering change: {{change}}
- Environment / solution layer: {{environment}}

This analysis runs a five-role pipeline with hard phase gates. Each role owns a named
output section. No role begins until the previous role's output section appears in full
above it. Roles are not interchangeable — each has a distinct accountability domain.

---

## Role 0 — Inertia Analyst  [PHASE GATE: none — always first]

**Accountability**: Failure Mode Catalog (IF-* artifact). This is the only output this
role produces. It has no involvement in the trigger table, budget section, or pathology
assessment — those belong to downstream roles.

Produce the catalog now:

```
FAILURE MODE CATALOG  (owner: Inertia Analyst)
  IF-Storm    | [risk statement scoped to this triggering change]
  IF-Missing  | [risk statement scoped to this triggering change]
  IF-Circular | [risk statement scoped to this triggering change]
```

⛔ GATE CHECK: The three IF-* entries above must be present before Role 1 begins.

---

## Role 1 — Threat Cataloger  [PHASE GATE: IF-* catalog must exist above]

**Accountability**: Typed Threat Catalog (TC-1, TC-2, TC-3 sections). This role does not
touch the trigger table. It maps the threat surface that downstream roles will reference.
Cite IF-* labels where threats connect to a known failure mode.

```
THREAT CATALOG  (owner: Threat Cataloger)

TC-1  CANDIDATE CONDITIONS
  [Entry 1: field/event/state; IF-* if applicable]
  [Entry 2: ...]
  [add rows as needed]

TC-2  CASCADE PATHS
  [Entry 1: automation chain; IF-Storm or IF-Circular if applicable]
  [Entry 2: ...]
  [add rows as needed]

TC-3  SIDE-EFFECT SCOPE
  [Entry 1: external write/notification/queue; IF-Missing if applicable]
  [Entry 2: ...]
  [add rows as needed]
```

⛔ GATE CHECK: TC-1, TC-2, TC-3 with populated entries must be present before Role 2 begins.

---

## Role 2 — Registry Analyst  [PHASE GATE: TC-1/TC-2/TC-3 must exist above]

**Accountability**: Unified Trigger Table and Registry Summary block.

Build the table. All columns required. Reference TC-1 for conditions; reference TC-3 for
side effects. Never leave a cell blank.

| # | Trigger Name | Fires? | Condition (TC-1 ref) | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|---|---|---|---|---|---|

Enforcement rule (reproduce this caption verbatim under the table):
> `Fires?` accepts YES or NO only — no row may omit this value. Firing sequence `#`
> is a consecutive integer for YES rows; `--` for NO rows. "Always fires" in the
> Condition column requires documented justification.

Immediately after the table, emit the Registry Summary:

```
REGISTRY SUMMARY  (owner: Registry Analyst)
  M  (YES rows with ≥1 side effect)  = ___
  N  (all YES rows)                  = ___
  Non-firing (NO rows)               = ___
```

⛔ GATE CHECK: REGISTRY SUMMARY with M, N, Non-firing values must be present before Role 3 begins.

---

## Role 3 — Budget Analyst  [PHASE GATE: REGISTRY SUMMARY must exist above]

**Accountability**: Budget Gate section. Read M from REGISTRY SUMMARY above.

**Condition**: Produce the full Budget Gate if M >= 3 AND the Side Effects column contains
at least one non-"none" entry. Otherwise emit the waiver line.

Full Budget Gate structure (numbered sections required):

```
BUDGET GATE  (owner: Budget Analyst)

1. Per-automation arithmetic
   [Automation A name]: [action 1] + [action 2] + ... = [X] requests/invocation
   [Automation B name]: ...
   (one line per automation with ≥1 side effect; no aggregate without per-item math)

2. Total requests across all firing automations: ___

3. Platform limit reference: ___ [cite tier-specific daily limit]

4. Budget consumed: ___% of daily entitlement

5. Run duration estimate: ___ to ___ seconds
   [No hedged ranges; commit to a specific span]
```

Waiver (if condition not met):
```
BUDGET GATE: waived  (owner: Budget Analyst)  — M = ___, threshold not met
```

⛔ GATE CHECK: Budget Gate section or waiver must be present before Role 4 begins.

---

## Role 4 — Pathology Analyst  [PHASE GATE: Budget Gate must exist above]

**Accountability**: Pathology Assessment — three subsections, one per pathology type.

For each subsection, the verdict keyword is the first content element on its own line.
No prose precedes it. Evidence and remediation follow the verdict.

Verdict keywords: `DETECTED` | `NOT DETECTED` | `INDETERMINATE`

For DETECTED or INDETERMINATE, the remediation must cite all three layers — a response
satisfying only one or two layers does not satisfy the three-layer requirement:
  - **Layer 1**: A specific PA/Copilot Studio construct (name the mechanism, not just
    the feature area — e.g., "concurrency control set to 1" not "use concurrency control")
  - **Layer 2**: The TC-type-numbered catalog entry from Role 1 that the remediation
    addresses (e.g., "TC-2, entry 3")
  - **Layer 3**: The IF-* failure mode label from Role 0 that this remediation closes

```
PATHOLOGY ASSESSMENT  (owner: Pathology Analyst)

### Trigger Storm

DETECTED | NOT DETECTED | INDETERMINATE
Evidence: [trigger names, TC-# entries, IF-Storm]
Remediation:
  Layer 1 — PA/Copilot Studio construct: ___
  Layer 2 — Catalog entry: TC-___
  Layer 3 — Failure mode closed: IF-Storm

### Missing Trigger

DETECTED | NOT DETECTED | INDETERMINATE
Evidence: [trigger names, TC-# entries, IF-Missing]
Remediation:
  Layer 1 — PA/Copilot Studio construct: ___
  Layer 2 — Catalog entry: TC-___
  Layer 3 — Failure mode closed: IF-Missing

### Circular Trigger

DETECTED | NOT DETECTED | INDETERMINATE
Evidence: [trigger names, TC-# entries, IF-Circular]
Remediation:
  Layer 1 — PA/Copilot Studio construct: ___
  Layer 2 — Catalog entry: TC-___
  Layer 3 — Failure mode closed: IF-Circular
```
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axes | Key Hypothesis |
|-----------|-------------|----------------|----------------|
| V-01 | Role Sequence | — | Front-loading Inertia Analyst creates IF-* labels that propagate through every downstream role |
| V-02 | Output Format | — | Fill-in template schemas drive structural compliance better than instructional prose |
| V-03 | Lifecycle Emphasis | — | Hard gate pre-conditions prevent phase skipping more reliably than role ownership alone |
| V-04 | Phrasing Register | — | Investigative narrative framing surfaces pathology evidence more organically |
| V-05 | Role Sequence + Lifecycle Emphasis + Verdict-First Format | Combined | Each axis compensates for a distinct execution failure mode; combination is tightest spec |
