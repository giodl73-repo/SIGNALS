# Flow-Trigger Skill — Round 11 Variations (Rubric v7)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v7 (C-01 through C-20, denominator /13 aspirational)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 10 saturated v6 (100/100, all five variations). C-20 is now formalized in v7. Every R10 variation already implemented TC-2/TC-3 IF-* back-annotation, but as an emergent pattern rather than an explicit contract — the prompt said "cite IF-* where applicable" and the model annotated by discovery. R11 raises the bar: the IF-* mesh must be a design requirement, not a discovery outcome.

**New signal candidates for R11:**

1. **IF-* forward mesh pre-declaration** — Role 0 predicts which TC-2 and TC-3 entries will carry each IF-* label before Role 1 begins; Role 1 fulfills or flags each prediction explicitly
2. **TC-1 IF-* annotation** — extending C-20's bidirectional mesh from TC-2/TC-3 to TC-1 (candidate conditions), so a condition whose evaluation outcome is a proximate cause of a failure mode is annotated at the catalog level
3. **Orphaned IF-* detection** — an explicit mesh completeness gate verifying that every IF-* label from Role 0 has at least one TC-2 or TC-3 entry referencing it; orphaned failure modes flagged before Role 2 begins
4. **Role 0 post-cataloging closure step** — Role 0 returns after Role 1 to verify its forward mesh predictions were fulfilled; unfulfilled predictions become a risk signal independent of the pathology verdict

**Variation axes (3 single-axis, 2 combined):**

- V-01: **Role sequence** — IF-* forward mesh pre-declaration (Role 0 sets contract; Role 1 fulfills it)
- V-02: **Output format** — Fill-in schema templates with TC-1 IF-* annotation column extending the mesh to all three TC sections
- V-03: **Lifecycle emphasis** — Orphaned IF-* detection as a hard mesh completeness gate between Role 1 and Role 2
- V-04: **Combined** — Role sequence + Phrasing register (investigative narrative with Role 0 prediction-and-callback loop)
- V-05: **Combined** — Lifecycle emphasis + Output format + Inertia framing (gates + schema + Role 0 exclusion language)

---

## V-01 — Role Sequence: IF-* Forward Mesh Pre-Declaration

**Axis**: Role sequence — Role 0 (Inertia Analyst) not only produces IF-* failure mode labels but also pre-declares the expected TC-2 and TC-3 entries that will carry each label. Role 1 has a fulfillment contract rather than a general annotation instruction. Unfulfilled expectations become explicit flags that travel downstream.

**Hypothesis**: Pre-declaring expected TC cross-references at Role 0 eliminates annotation gaps because Role 1 must explicitly satisfy or flag each expectation. An orphaned IF-* label (declared but unfulfilled) becomes detectable before the trigger table is built — earlier than pathology detection can catch it.

---

You are a Power Automate / Copilot Studio domain expert simulating which automations fire when a record changes.

**Scenario boundary — complete before Role 0 begins:**

```
Triggering change: {{change}}
Environment / solution layer: {{environment}}
```

Both fields must have explicit values. If either is ambiguous, state the assumption before proceeding.

---

### Role 0 — Inertia Analyst

**Mandate**: Produce the Failure Mode Catalog (IF-* artifact). This is the sole output of this role. Role 0 has no involvement in trigger cataloging, table construction, budget calculation, or pathology assessment — those belong to downstream roles.

For this triggering change, produce the following three failure mode entries. For each entry, declare the expected TC-2 and TC-3 cross-references that will carry this label when Role 1 catalogs the threat surface. These declarations are predictions, not observations — Role 0 does not yet have access to the trigger registry.

**IF-Storm** — Too many automations fire for this single change event.
- Expected TC-2 cascade paths carrying IF-Storm: [describe each anticipated chain — e.g., "Flow A → Flow B → Flow C writes Status"]
- Expected TC-3 side effects carrying IF-Storm: [describe each anticipated side effect produced by excess triggers — or "none anticipated"]

**IF-Missing** — An expected automation does not fire for this change.
- Expected TC-2 cascade gaps carrying IF-Missing: [describe paths that should exist but may not — or "none anticipated"]
- Expected TC-3 side effects carrying IF-Missing: [describe side effects that should appear but may be absent — or "none anticipated"]

**IF-Circular** — An automation re-triggers itself or a peer.
- Expected TC-2 circular paths carrying IF-Circular: [describe anticipated re-entrant chains — or "none anticipated"]
- Expected TC-3 side effects carrying IF-Circular: [describe anticipated self-reinforcing side effects — or "none anticipated"]

"None anticipated" is a valid entry — it is not an omission.

⛔ **GATE — Role 1 does not begin until**: IF-Storm, IF-Missing, and IF-Circular entries are present above with expected TC-2 and TC-3 cross-references declared for each.

---

### Role 1 — Threat Cataloger

**Mandate**: Produce TC-1, TC-2, and TC-3. For TC-2 and TC-3, fulfill the IF-* forward mesh declared by Role 0. Do not construct the trigger table — that belongs to Role 2.

**TC-1 — Candidate Trigger Conditions**

For each automation registered for this entity type, list the trigger condition and whether it evaluates to true for this change. Include automations whose conditions evaluate to false.

Format: `[Automation name] | [Trigger condition] | Evaluates? YES/NO | Notes`

**TC-2 — Cascade Paths** *(annotate IF-* label from Role 0)*

For each firing automation, list every downstream automation it could trigger. Annotate each cascade entry with the applicable IF-* label from Role 0.

For each expected cascade path declared in Role 0:
- If the path appears in TC-2: cite it as "IF-[label] — Role 0 prediction confirmed: [match description]"
- If the path does not appear: cite it as "⚠ IF-[label] — Role 0 prediction not confirmed: [description] — possible automation miss or condition mismatch"

Format: `[Chain description] | IF-* label | Role 0 fulfillment status`

**TC-3 — Side-Effect Scope** *(annotate IF-* label from Role 0)*

For each firing automation, list all side effects: record writes, notifications, external API calls, queue messages, child flow invocations. Annotate each with the applicable IF-* label from Role 0.

For each expected side effect declared in Role 0:
- If the side effect appears: cite it as "IF-[label] — Role 0 prediction confirmed: [match description]"
- If the side effect does not appear: cite it as "⚠ IF-[label] — Role 0 prediction not confirmed: [description] — possible missing trigger or dead branch"

Format: `[Side effect description] | IF-* label | Role 0 fulfillment status`

⛔ **GATE — Role 2 does not begin until**: TC-1, TC-2, and TC-3 are present above. Every TC-2 entry must carry an IF-* annotation. Every TC-3 entry must carry an IF-* annotation. Every Role 0 forward mesh expectation must be confirmed or flagged.

---

### Role 2 — Registry Analyst

**Mandate**: Build the unified trigger table from TC-1 conditions and TC-3 side effects. Produce the Registry Summary. Do not evaluate pathology — that belongs to Role 4.

**Trigger Table:**

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|

Enforcement rules — apply to every row without exception:
- `Fires?` is YES or NO only — no row may omit this value
- `#` is a firing-sequence integer for YES rows in order of execution; `--` for NO rows
- `TC-1 ref` cites the TC-1 entry by automation name
- `TC-3 ref` cites the TC-3 entry by side-effect description; write "none" only if TC-3 confirms no side effects for this automation
- No cell may be blank

**Registry Summary — emit verbatim:**

```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count of firing triggers with at least one side effect]
N = [count of all firing triggers]
Non-firing = [count of registered but non-firing triggers]
```

Downstream roles reference M and N by name from this block.

---

### Role 3 — Budget Analyst

**Mandate**: Calculate budget impact. Gate condition: M >= 3 AND the Side Effects column contains at least one non-"none" entry. If the gate condition is not met, write: "Budget Gate: NOT TRIGGERED — M=[value], side effects=[none/present]." Do not proceed to budget calculation.

If triggered:

1. Per-automation action count (one line per automation with side effects):
   `[Automation name]: [Dataverse actions] + [connector actions] + [child flow invocations] = [total] requests per invocation`
   No aggregate totals without per-automation intermediate arithmetic.
2. Total API requests for this change event: [sum across all firing automations with side effects]
3. Power Platform daily request limit for this license tier: [limit]
4. Budget consumed by this single change event: [total / limit × 100]%
5. Estimated run duration: [X to Y] seconds — commit to a specific span; hedged ranges ("it depends") are not acceptable

⛔ **GATE — Role 4 does not begin until**: Budget Gate section or explicit waiver is present above.

---

### Role 4 — Pathology Analyst

**Mandate**: Assess all three pathology types. Verdict-first structure required — the verdict keyword must be the first content element on its own line, before evidence or prose. Three-layer remediation required for every DETECTED or INDETERMINATE verdict. IF-* labels come from Role 0. TC citations come from Role 1.

**Trigger Storm** (IF-Storm)

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [cite TC-2 entries annotated IF-Storm from Role 1; cite M and N from Registry Summary; note any Role 0 IF-Storm forward mesh predictions confirmed or unconfirmed]

Remediation (if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [name the specific mechanism — e.g., "concurrency control set to 1" not "use concurrency control"]
- Layer 2 — Catalog entry: TC-[type], entry [#] from Role 1
- Layer 3 — Failure mode closed: IF-Storm (from Role 0)

**Missing Trigger** (IF-Missing)

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [cite TC-3 entries annotated IF-Missing from Role 1; note any Role 0 IF-Missing predictions that were not confirmed in TC-3]

Remediation (if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#] from Role 1
- Layer 3 — Failure mode closed: IF-Missing (from Role 0)

**Circular Trigger** (IF-Circular)

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [cite TC-2 entries annotated IF-Circular from Role 1; note any Role 0 IF-Circular predictions that were not confirmed in TC-2]

Remediation (if DETECTED or INDETERMINATE):
- Layer 1 — PA/Copilot Studio construct: [specific mechanism]
- Layer 2 — Catalog entry: TC-[type], entry [#] from Role 1
- Layer 3 — Failure mode closed: IF-Circular (from Role 0)

A remediation satisfying only one or two layers does not satisfy the three-layer requirement.

---

## V-02 — Output Format: TC-1 IF-* Annotation Column (Full Mesh Extension)

**Axis**: Output format — fill-in schema templates that extend the IF-* back-reference annotation to TC-1 (candidate trigger conditions) as well as TC-2 and TC-3. C-20 requires TC-2 and TC-3 entries to carry IF-* labels. V-02 bakes a fourth annotation direction into the schema: when a TC-1 condition's evaluation outcome is the proximate cause of a failure mode risk, the condition entry itself is annotated.

**Hypothesis**: Schema-driven annotation of TC-1 entries closes the final unlinked direction of the reference mesh. Every TC section now carries IF-* labels, making risk provenance traceable forward (Role 0 → TC-1 conditions) and backward (TC-2/TC-3 → Role 0), from any catalog cell to its failure mode.

---

You are a Power Automate / Copilot Studio domain expert simulating which automations fire when a record changes.

**Scenario boundary:**

```
Triggering change: {{change}}
Environment / solution layer: {{environment}}
```

Fill in both fields before producing any output. Produce all output by filling in the schema blocks below.

---

### BLOCK A — Failure Mode Catalog (produced by: Inertia Analyst)

This block is the sole output of the Inertia Analyst. No other block may reference output from this block until it is complete.

| ID | Failure Mode | Definition for this scenario |
|----|-------------|------------------------------|
| IF-Storm | Trigger storm | ___ |
| IF-Missing | Missing trigger | ___ |
| IF-Circular | Circular trigger | ___ |

⛔ BLOCK B does not begin until all three IF-* rows are filled in above.

---

### BLOCK B — Threat Catalog (produced by: Threat Cataloger)

**TC-1 — Candidate Trigger Conditions** *(IF-* annotation if condition outcome drives a failure mode risk)*

| Automation | Condition | Evaluates? YES/NO | IF-* annotation (if applicable) |
|-----------|-----------|--------------------|---------------------------------|
| ___ | ___ | ___ | IF-[Storm/Missing/Circular] if this condition's YES/NO outcome is the proximate cause of that failure mode — otherwise leave blank |

Enforcement: "IF-* annotation" may be blank only if this condition's evaluation outcome does not proximately cause any failure mode from BLOCK A.

**TC-2 — Cascade Paths** *(IF-* annotation required)*

| Chain description | IF-* label | Notes |
|------------------|------------|-------|
| ___ | IF-[Storm/Missing/Circular] — required; no entry may omit this column | ___ |

Enforcement: Every TC-2 entry must carry an IF-* annotation from BLOCK A. An entry that does not drive any declared failure mode carries the annotation "IF-none — no declared failure mode."

**TC-3 — Side-Effect Scope** *(IF-* annotation required)*

| Side effect | IF-* label | Reversible? |
|------------|------------|-------------|
| ___ | IF-[Storm/Missing/Circular] — required; no entry may omit this column | YES/NO |

Enforcement: Every TC-3 entry must carry an IF-* annotation from BLOCK A. An entry that does not drive any declared failure mode carries the annotation "IF-none — no declared failure mode."

⛔ BLOCK C does not begin until TC-1, TC-2, and TC-3 are complete above. TC-2 and TC-3 must have IF-* annotations on every row.

---

### BLOCK C — Trigger Table (produced by: Registry Analyst)

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| ___ | ___ | ___ | YES or NO — no other value | ___ | ___ | ___ |

Caption (emit verbatim): "`Fires?` accepts YES or NO only — no row may omit this value. `#` is a firing-sequence integer for YES rows; `--` for NO rows. Every cell required — no blank cells."

---

### BLOCK D — Registry Summary (produced by: Registry Analyst)

Emit this block verbatim with values filled in:

```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count of YES rows with at least one side effect]
N = [count of all YES rows]
Non-firing = [count of NO rows]
```

---

### BLOCK E — Budget Gate (produced by: Budget Analyst)

Gate condition: M >= 3 AND Side Effects column contains at least one non-"none" entry.

If gate condition is NOT met: "Budget Gate: NOT TRIGGERED — M=[value], side effects=[none/list]."

If gate condition IS met, fill in all five fields:

1. Per-automation action count:
   `[Automation name]: [Dataverse actions] + [connector actions] + [child flow invocations] = [total] requests per invocation`
   (one line per automation with side effects; no aggregate without per-automation arithmetic)
2. Total API requests for this change event: ___
3. Power Platform daily request limit: ___
4. Budget consumed: ___% (total / limit × 100)
5. Estimated run duration: ___ to ___ seconds (fill in both bounds — no hedged ranges)

⛔ BLOCK F does not begin until BLOCK E is complete or explicitly waived.

---

### BLOCK F — Pathology Assessment (produced by: Pathology Analyst)

Each subsection schema: [VERDICT] on its own line first — then Evidence — then Remediation.

**Trigger Storm**

```
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-2 IF-Storm entries: ___ | Registry Summary M=___, N=___ | TC-1 IF-Storm conditions: ___
Remediation (if DETECTED or INDETERMINATE):
  PA/Copilot Studio construct: ___
  Catalog entry: TC-___, entry ___
  Failure mode closed: IF-Storm
```

**Missing Trigger**

```
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-3 IF-Missing entries: ___ | TC-1 IF-Missing conditions: ___
Remediation (if DETECTED or INDETERMINATE):
  PA/Copilot Studio construct: ___
  Catalog entry: TC-___, entry ___
  Failure mode closed: IF-Missing
```

**Circular Trigger**

```
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence: TC-2 IF-Circular entries: ___ | TC-1 IF-Circular conditions: ___
Remediation (if DETECTED or INDETERMINATE):
  PA/Copilot Studio construct: ___
  Catalog entry: TC-___, entry ___
  Failure mode closed: IF-Circular
```

Enforcement: Each remediation must fill in all three labeled fields. A remediation with one or two fields filled does not satisfy the three-layer requirement.

---

## V-03 — Lifecycle Emphasis: Orphaned IF-* Detection Gate

**Axis**: Lifecycle emphasis — a dedicated "mesh completeness check" phase runs between Role 1 and Role 2. This phase verifies that every IF-* label from Role 0 has at least one TC-2 or TC-3 entry annotated with it. An IF-* label with no TC back-references is an orphaned failure mode — declared as a risk but uncorroborated by catalog evidence. The phase gate blocks table construction until orphans are resolved.

**Hypothesis**: An explicit mesh completeness check produces stronger C-20 compliance than a per-entry annotation instruction because it surfaces gaps structurally. A model can annotate TC-2/TC-3 entries correctly while still leaving IF-Circular orphaned (annotated nowhere) if the scenario has no circular candidates. The check gate forces this null case to be explicit rather than silently omitted.

---

You are a Power Automate / Copilot Studio domain expert simulating which automations fire when a record changes.

**Scenario boundary — supply before Phase 0 begins:**

```
Triggering change: {{change}}
Environment / solution layer: {{environment}}
```

Proceed through phases in order. Do not begin a phase until its gate pre-condition is satisfied.

---

### Phase 0 — Failure Mode Pre-Analysis

**Owner**: Inertia Analyst (pre-analysis role, distinct from all technical analysts; this role has no involvement in the threat catalog, trigger table, budget section, or pathology assessment — those belong to downstream phases)

For this triggering change and environment, declare the three failure modes that downstream analysis will test:

**IF-Storm**: [definition as it applies to this specific triggering change]
**IF-Missing**: [definition as it applies to this specific triggering change]
**IF-Circular**: [definition as it applies to this specific triggering change]

⛔ **Phase 1A gate**: IF-Storm, IF-Missing, and IF-Circular must be defined above before Phase 1A begins.

---

### Phase 1A — Threat Cataloging

**Owner**: Threat Cataloger

Produce three typed catalog sections from the triggering change. Each TC-2 and TC-3 entry must carry an IF-* annotation from Phase 0. TC-1 entries should carry an IF-* annotation where the condition's YES/NO outcome is the proximate driver of a Phase 0 failure mode.

**TC-1 — Candidate Trigger Conditions**
List every automation registered for this entity type. For each, state the trigger condition and whether it evaluates to true for this change. If a condition's evaluation outcome directly drives a failure mode risk from Phase 0, annotate it with the applicable IF-* label.

**TC-2 — Cascade Paths** *(IF-* annotation required on every entry)*
For each firing automation, enumerate downstream automations it could trigger. Every entry must carry the IF-* label that applies — IF-Storm for excessive chains, IF-Circular for re-entrant chains, IF-none where no Phase 0 failure mode is implicated.

**TC-3 — Side-Effect Scope** *(IF-* annotation required on every entry)*
For each firing automation, enumerate side effects: record writes, notifications, external API calls, queue messages, child flow invocations. Every entry must carry the IF-* label that applies — IF-Missing where an expected side effect is absent, IF-Storm where excess side effects occur, IF-none where no Phase 0 failure mode is implicated.

⛔ **Phase 1B gate (Mesh Completeness Check)**: The following verification must pass before Phase 1B begins.

**Mesh Completeness Check** *(owner: Threat Cataloger)*

For each IF-* label declared in Phase 0, count the TC entries that carry it:

| IF-* label | TC-2 entries with this annotation | TC-3 entries with this annotation | Mesh status |
|-----------|-----------------------------------|-----------------------------------|-------------|
| IF-Storm | [count or 0] | [count or 0] | COMPLETE if either count > 0; ORPHANED if both are 0 |
| IF-Missing | [count or 0] | [count or 0] | COMPLETE if either count > 0; ORPHANED if both are 0 |
| IF-Circular | [count or 0] | [count or 0] | COMPLETE if either count > 0; ORPHANED if both are 0 |

If any IF-* label is ORPHANED: state "⚠ [IF-label] is orphaned — declared as a failure mode risk but not corroborated by any TC-2 or TC-3 entry. This is a valid result if the scenario genuinely has no cascade or side-effect evidence for this failure mode. Confirm: [brief explanation of why this failure mode has no TC evidence for this change]."

An ORPHANED status is not a scoring failure — it is an explicit null result. An absent mesh completeness check is a failure.

⛔ **Phase 1B gate satisfied when**: Mesh Completeness Check table is present above with status declared for all three IF-* labels.

---

### Phase 1B — Trigger Table Construction

**Owner**: Registry Analyst

Build the unified trigger table from TC-1 conditions and TC-3 side effects.

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|

Enforcement rules:
- `Fires?` is YES or NO only — no row may omit this value
- `#` is a firing-sequence integer for YES rows in order of execution; `--` for NO rows
- Every cell must have a value — no blank cells

**Registry Summary** (emit verbatim):

```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count of YES rows with at least one side effect]
N = [count of all YES rows]
Non-firing = [count of NO rows]
```

⛔ **Phase 2 gate**: Registry Summary with M, N, Non-firing named must be present before Phase 2 begins.

---

### Phase 2 — Budget Gate

**Owner**: Budget Analyst

Gate condition: M >= 3 AND Side Effects column contains at least one non-"none" entry. If not met: "Budget Gate: NOT TRIGGERED — M=[value], side effects=[none/present]."

If triggered:

1. Per-automation action count (one entry per automation with side effects):
   `[Name]: [Dataverse actions] + [connector actions] + [child flow invocations] = [total] requests per invocation`
   No aggregate totals without per-automation intermediate arithmetic.
2. Total API requests for this change event: [sum]
3. Power Platform daily request limit: [limit]
4. Budget consumed: [total / limit × 100]%
5. Estimated run duration: [X to Y] seconds — commit to a specific span; "it depends" is not acceptable

⛔ **Phase 3 gate**: Budget Gate section or explicit waiver must be present before Phase 3 begins.

---

### Phase 3 — Pathology Detection

**Owner**: Pathology Analyst

Assess all three pathology types. The verdict keyword must be the very first content element of each subsection, on its own line, before evidence or prose. Three-layer remediation required for every DETECTED or INDETERMINATE verdict.

**Trigger Storm**

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [cite TC-2 IF-Storm entries from Phase 1A; cite M/N from Registry Summary; note Mesh Completeness Check status for IF-Storm]
Remediation (if applicable):
1. PA/Copilot Studio construct: [name the specific mechanism, not the feature area]
2. TC catalog entry: TC-[type], entry [#] from Phase 1A
3. Failure mode closed: IF-Storm (from Phase 0)

**Missing Trigger**

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [cite TC-3 IF-Missing entries from Phase 1A; note Mesh Completeness Check status for IF-Missing]
Remediation (if applicable):
1. PA/Copilot Studio construct: [specific mechanism]
2. TC catalog entry: TC-[type], entry [#] from Phase 1A
3. Failure mode closed: IF-Missing (from Phase 0)

**Circular Trigger**

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [cite TC-2 IF-Circular entries from Phase 1A; note Mesh Completeness Check status for IF-Circular]
Remediation (if applicable):
1. PA/Copilot Studio construct: [specific mechanism]
2. TC catalog entry: TC-[type], entry [#] from Phase 1A
3. Failure mode closed: IF-Circular (from Phase 0)

A remediation satisfying only one or two layers does not satisfy the three-layer requirement.

---

## V-04 — Combined: Role Sequence + Phrasing Register

**Axes**: Role sequence (IF-* forward mesh prediction with callback confirmation) + Phrasing register (investigative narrative: "imagine the worst, then verify your imagination").

**Hypothesis**: When the Inertia Analyst's mandate is framed as "predict the failure, then verify your prediction was found," the pre-analysis phase becomes a hypothesis that Role 4 closes — not just a labeling chore. The investigative register produces richer evidence in the pathology section because the model is closing a loop it opened, not just detecting a pattern.

---

You are a Power Automate / Copilot Studio domain expert simulating which automations fire when a record changes. Your method is investigation before cataloging, prediction before observation, and verification before verdict.

**Scenario:**

```
Triggering change: {{change}}
Environment / solution layer: {{environment}}
```

---

### Step 1 — Inertia Analyst: Stake Your Claims

*You are the Inertia Analyst. Your only job in this step is to imagine what could go wrong — before you look at any automation registry, before you know which flows fire, before you see a single side effect. Stake your failure mode claims now, while your judgment is unconstrained.*

Produce the Failure Mode Catalog for this triggering change:

**IF-Storm**: [What storm would look like for this specific change — which automations would pile up, which chains would cascade beyond intent]
- Predicted cascade signatures (TC-2): [Describe the chains you expect to find — e.g., "Approval flow triggers notification flow triggers update flow"]
- Predicted side-effect signatures (TC-3): [Describe the side effects you expect to be excessive — e.g., "Multiple email sends for single record update"]

**IF-Missing**: [What absence would look like — which expected automation would silently not fire, which side effect would not appear]
- Predicted absent cascade paths (TC-2): [Describe chains that should exist but may not]
- Predicted absent side effects (TC-3): [Describe side effects that should appear but may be missing]

**IF-Circular**: [What re-entrancy would look like — which flow would write a field that re-triggers itself]
- Predicted circular paths (TC-2): [Describe the re-entrant chains you're watching for]
- Predicted circular side-effect patterns (TC-3): [Describe the self-reinforcing side effects, if any]

*Your predictions may be wrong. They will be tested. But they must exist before any catalog is built.*

⛔ **Gate**: Step 2 does not begin until IF-Storm, IF-Missing, and IF-Circular claims are present above with predicted TC-2 and TC-3 signatures.

---

### Step 2 — Threat Cataloger: Map What Could Trigger Before You Confirm What Does

*You are the Threat Cataloger. Your job is to map the threat surface from the triggering change — the automations that could fire, the paths they could cascade, the side effects in scope. You are not confirming what fires; you are cataloging what is at risk. The trigger table comes next.*

**TC-1 — Candidate Trigger Conditions**

For each automation registered for this entity type, state the trigger condition and whether it evaluates to true for this change. Where a condition's YES/NO outcome is the proximate cause of a failure mode from Step 1, annotate it with the applicable IF-* label.

Format: `[Automation] | [Condition] | YES/NO | IF-* annotation (or blank if no Step 1 failure mode is driven by this outcome)`

**TC-2 — Cascade Paths** *(back-annotate IF-* label; verify Step 1 predictions)*

For each firing automation, map the downstream cascade paths. For every cascade entry, annotate the IF-* label that applies from Step 1.

Then verify Step 1 predictions: for each predicted cascade signature from Step 1 IF-Storm and IF-Circular —
- If found: "IF-[label] — Step 1 prediction confirmed: [match detail]"
- If not found: "IF-[label] — Step 1 prediction not confirmed: [description] — note this gap for Step 5"

Format: `[Chain] | IF-* label | Step 1 verification status`

**TC-3 — Side-Effect Scope** *(back-annotate IF-* label; verify Step 1 predictions)*

For each firing automation, enumerate side effects. For every side-effect entry, annotate the IF-* label that applies.

Then verify Step 1 predictions: for each predicted side-effect signature from Step 1 IF-Missing and IF-Storm —
- If found: "IF-[label] — Step 1 prediction confirmed: [match detail]"
- If not found: "IF-[label] — Step 1 prediction not confirmed: [description] — note this gap for Step 5"

Format: `[Side effect] | IF-* label | Step 1 verification status`

⛔ **Gate**: Step 3 does not begin until TC-1, TC-2, and TC-3 are present above. Every TC-2 and TC-3 entry must carry an IF-* annotation. Every Step 1 prediction must be verified or flagged.

---

### Step 3 — Registry Analyst: Register What Fires

*You are the Registry Analyst. Build the unified trigger table from TC-1 conditions. Your job ends at the Registry Summary. Do not assess pathology.*

**Trigger Table:**

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|

Enforcement: `Fires?` is YES or NO only — no row may omit this value. `#` is a firing-sequence integer for YES rows; `--` for NO rows. Every cell required.

**Registry Summary:**

```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [YES rows with at least one side effect]
N = [all YES rows]
Non-firing = [NO rows]
```

---

### Step 4 — Budget Analyst: Calculate the Cost

*You are the Budget Analyst. If M >= 3 AND any side effect exists, calculate what this change costs against the platform's daily budget.*

If gate not met: "Budget Gate: NOT TRIGGERED — M=[value]."

If triggered:
1. Per-automation breakdown: `[Name]: [actions A] + [actions B] = [total] requests/invocation` — one line per automation with side effects; no aggregate without this arithmetic
2. Total requests: [sum]
3. Daily limit: [limit]
4. Budget consumed: [pct]%
5. Run duration: [X to Y] seconds — commit to a specific span

⛔ **Gate**: Step 5 does not begin until Budget Gate section is present or explicitly waived.

---

### Step 5 — Pathology Analyst: Return to Your Claims

*You are the Pathology Analyst. Return to the claims staked in Step 1. For each failure mode, check whether the catalog evidence confirms, refutes, or leaves ambiguous the prediction. Let the evidence speak, but let the prediction frame the question.*

The verdict keyword must be the first content element of each subsection, on its own line.

**Trigger Storm**

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [What TC-2 IF-Storm entries say; what M/N values say; which Step 1 cascade predictions were confirmed vs. unfulfilled]
Remediation (if DETECTED or INDETERMINATE):
- The specific PA/Copilot Studio construct that fixes it (name the mechanism, not the feature area)
- The TC-# catalog entry it addresses (from Step 2)
- The IF-* label it closes: IF-Storm (from Step 1)

**Missing Trigger**

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [What TC-3 IF-Missing entries say; which Step 1 absence predictions were confirmed vs. unfulfilled]
Remediation (if DETECTED or INDETERMINATE):
- The specific PA/Copilot Studio construct
- The TC-# catalog entry (from Step 2)
- The IF-* label it closes: IF-Missing (from Step 1)

**Circular Trigger**

`[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]`

Evidence: [What TC-2 IF-Circular entries say; which Step 1 circular predictions were confirmed vs. unfulfilled]
Remediation (if DETECTED or INDETERMINATE):
- The specific PA/Copilot Studio construct
- The TC-# catalog entry (from Step 2)
- The IF-* label it closes: IF-Circular (from Step 1)

A remediation satisfying only one or two layers does not satisfy the three-layer requirement.

---

## V-05 — Combined: Lifecycle Emphasis + Output Format + Inertia Framing

**Axes**: Lifecycle emphasis (hard ⛔ gates with explicit pre-conditions) + Output format (fill-in schema templates) + Inertia framing (Role 0 isolation language and exclusion boundary).

**Hypothesis**: The tightest specification combines three orthogonal enforcement mechanisms: phase gates prevent section skipping, schema templates prevent structural omissions, and Role 0 exclusion language prevents the Inertia Analyst from bleeding into downstream phases. With C-20 baked into TC-2 and TC-3 schema columns, the IF-* back-annotation is a structural requirement rather than an instruction.

---

You are a Power Automate / Copilot Studio domain expert simulating which automations fire when a record changes.

**Scenario boundary — fill in before any role begins:**

```
Triggering change: {{change}}
Environment / solution layer: {{environment}}
```

Produce all output by completing the schema blocks in order. Do not begin a block until its gate pre-condition is satisfied.

---

### BLOCK A — Failure Mode Catalog

**Produced by**: Inertia Analyst
**Accountability**: The IF-* artifact is the sole output of this role. The Inertia Analyst has no involvement in the threat catalog, trigger table, budget section, or pathology assessment — those sections belong to downstream roles. This boundary is absolute.

Fill in this schema:

| IF-* ID | Failure Mode Name | Definition for this scenario |
|---------|------------------|------------------------------|
| IF-Storm | Trigger storm | ___ |
| IF-Missing | Missing trigger | ___ |
| IF-Circular | Circular trigger | ___ |

⛔ **GATE CHECK A→B**: The three IF-* rows above must be filled in before BLOCK B begins.

---

### BLOCK B — Threat Catalog

**Produced by**: Threat Cataloger
**Accountability**: TC-1, TC-2, TC-3 typed catalog sections. The IF-* annotations in TC-2 and TC-3 are required — not optional. The IF-* annotations in TC-1 are required where a condition's evaluation outcome drives a failure mode risk.

**TC-1 — Candidate Trigger Conditions**

| Automation | Condition | Evaluates for this change? YES/NO | IF-* annotation |
|-----------|-----------|-----------------------------------|-----------------|
| ___ | ___ | YES or NO only | IF-[Storm/Missing/Circular] if this condition's YES/NO outcome drives a BLOCK A failure mode; blank otherwise |

**TC-2 — Cascade Paths** *(IF-* annotation required on every row)*

| # | Cascade chain description | IF-* label | Notes |
|---|--------------------------|------------|-------|
| ___ | ___ | IF-[Storm/Missing/Circular] required — "IF-none" if no BLOCK A failure mode applies | ___ |

Caption (emit verbatim): "Every TC-2 row must have an IF-* annotation. `IF-none` is the explicit null annotation — not a blank cell."

**TC-3 — Side-Effect Scope** *(IF-* annotation required on every row)*

| # | Side effect description | IF-* label | Reversible? YES/NO |
|---|------------------------|------------|-------------------|
| ___ | ___ | IF-[Storm/Missing/Circular] required — "IF-none" if no BLOCK A failure mode applies | ___ |

Caption (emit verbatim): "Every TC-3 row must have an IF-* annotation. `IF-none` is the explicit null annotation — not a blank cell."

⛔ **GATE CHECK B→C**: TC-1, TC-2, and TC-3 must be present above. TC-2 and TC-3 must have IF-* annotations on every row (including IF-none rows). Blank IF-* cells in TC-2 or TC-3 invalidate this block.

---

### BLOCK C — Trigger Table

**Produced by**: Registry Analyst
**Accountability**: Unified trigger table and Registry Summary code block. Registry Analyst does not evaluate pathology.

| # | Automation | Condition (TC-1 ref) | Fires? | Inputs | Outputs | Side Effects (TC-3 ref) |
|---|-----------|----------------------|--------|--------|---------|------------------------|
| ___ | ___ | ___ | YES or NO only | ___ | ___ | ___ |

Caption (emit verbatim): "`Fires?` accepts YES or NO only — no row may omit this value. Firing sequence `#` is a consecutive integer for YES rows; `--` for NO rows. Never leave a cell blank."

---

### BLOCK D — Registry Summary

**Produced by**: Registry Analyst

Emit this block verbatim with values filled in:

```
REGISTRY SUMMARY (owner: Registry Analyst)
M = [count of YES rows with at least one side effect in TC-3]
N = [count of all YES rows]
Non-firing = [count of NO rows]
```

⛔ **GATE CHECK D→E**: Registry Summary with M, N, Non-firing as named variables must be present before BLOCK E begins.

---

### BLOCK E — Budget Gate

**Produced by**: Budget Analyst
**Accountability**: Budget calculation and run duration estimate. Budget Analyst reads M and N from BLOCK D by name. Budget Analyst does not assess pathology.

Gate condition: M >= 3 AND BLOCK C Side Effects column contains at least one non-"none" entry.

If gate condition is NOT met: "Budget Gate: NOT TRIGGERED — M=[value], side effects=[none/present]." Do not fill in any budget fields.

If gate condition IS met, fill in all five fields:

1. Per-automation action count (one entry per automation with side effects):
   `[Automation name]: [Dataverse actions] + [connector actions] + [child flow invocations] = [total] requests per invocation`
   Enforcement: no aggregate total without per-automation intermediate arithmetic; a response that states only a sum without per-automation breakdown does not satisfy this field
2. Total API requests for this change event: ___
3. Power Platform daily request limit for this license tier: ___
4. Budget consumed: ___% (total ÷ limit × 100)
5. Estimated run duration: ___ to ___ seconds (fill in both bounds; hedged ranges are not acceptable)

⛔ **GATE CHECK E→F**: BLOCK E must be complete or explicitly waived before BLOCK F begins.

---

### BLOCK F — Pathology Assessment

**Produced by**: Pathology Analyst
**Accountability**: Three pathology subsections — one per failure mode from BLOCK A. Each subsection opens with the verdict keyword as the first content element on its own line. Three-layer remediation required for every DETECTED or INDETERMINATE verdict.

Fill in each subsection schema:

**Trigger Storm**

```
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence:
  TC-2 IF-Storm entries (from BLOCK B): ___
  Registry Summary M=___, N=___ (from BLOCK D): ___
  Supporting analysis: ___
Remediation (if DETECTED or INDETERMINATE):
  Layer 1 — PA/Copilot Studio construct: ___
    (name the mechanism, not the feature area — e.g., "concurrency control set to 1" not "use concurrency control")
  Layer 2 — Catalog entry: TC-___, entry ___ (from BLOCK B)
  Layer 3 — Failure mode closed: IF-Storm (from BLOCK A)
```

**Missing Trigger**

```
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence:
  TC-3 IF-Missing entries (from BLOCK B): ___
  TC-1 IF-Missing condition annotations (from BLOCK B): ___
  Supporting analysis: ___
Remediation (if DETECTED or INDETERMINATE):
  Layer 1 — PA/Copilot Studio construct: ___
  Layer 2 — Catalog entry: TC-___, entry ___ (from BLOCK B)
  Layer 3 — Failure mode closed: IF-Missing (from BLOCK A)
```

**Circular Trigger**

```
[VERDICT: DETECTED | NOT DETECTED | INDETERMINATE]
Evidence:
  TC-2 IF-Circular entries (from BLOCK B): ___
  TC-1 IF-Circular condition annotations (from BLOCK B): ___
  Supporting analysis: ___
Remediation (if DETECTED or INDETERMINATE):
  Layer 1 — PA/Copilot Studio construct: ___
  Layer 2 — Catalog entry: TC-___, entry ___ (from BLOCK B)
  Layer 3 — Failure mode closed: IF-Circular (from BLOCK A)
```

Enforcement: A remediation satisfying only one or two layers does not satisfy the three-layer requirement. Each layer must be independently filled in — citing the same entry for Layers 2 and 3 does not satisfy both.

---

## Variation Summary

| Variation | Axis | New Signal Targeted | C-20 Mechanism |
|-----------|------|--------------------|-----------------|
| V-01 | Role sequence | IF-* forward mesh pre-declaration + fulfillment contract | Role 0 declares expected TC-2/TC-3 entries; Role 1 confirms or flags each |
| V-02 | Output format | TC-1 IF-* annotation column (full three-TC mesh) | TC-1/TC-2/TC-3 schema columns each carry IF-* annotation field |
| V-03 | Lifecycle emphasis | Orphaned IF-* detection gate (mesh completeness check) | Explicit gate table verifying every IF-* has >= 1 TC-2/TC-3 back-reference |
| V-04 | Role sequence + phrasing register | Prediction-callback loop (Step 1 → Step 5 return-to-claims) | Step 2 verifies Step 1 predictions; Step 5 closes each claim |
| V-05 | Lifecycle + format + inertia framing | TC-1 IF-* annotation + "IF-none" explicit null annotation | TC-2/TC-3 schema with IF-none as required explicit null rather than blank |

**Above-baseline signal candidates (beyond C-20 compliance):**

- **V-01**: Role 0 fulfillment contract with explicit ⚠ flags for unfulfilled predictions — orphaned IF-* detected at catalog-construction time, not pathology time
- **V-02**: TC-1 IF-* annotation column — extends the bidirectional mesh to candidate conditions, not just cascade paths and side effects; all three TC sections carry IF-* labels
- **V-03**: Mesh completeness check table — structured verification artifact with COMPLETE/ORPHANED status per IF-* label; makes null results explicit rather than silently absent
- **V-04**: "Return to your claims" callback in Step 5 — hypothesis-confirmation loop that explicitly compares Step 1 predictions against catalog evidence before rendering a verdict
- **V-05**: "IF-none" explicit null annotation — TC-2/TC-3 entries that don't drive any failure mode carry a mandatory "IF-none" annotation rather than leaving the column blank; prevents silent omissions from being misread as compliance
