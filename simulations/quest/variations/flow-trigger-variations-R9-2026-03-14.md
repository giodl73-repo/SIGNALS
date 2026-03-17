R8 context absorbed. V-01 scored 100 (Gold) with three above-baseline signals: self-verification checklist, Registry Analyst unification (owns TC catalog + table), and TC-3.N.M sub-index. V-02 was incomplete. Now generating R9 variations with three new unexplored axes: inertia framing, negative examples, pre-flight assertions.

---

# flow-trigger — Round 9 Variations (v5 Rubric)

## Axes Selected

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Inertia Framing | ✓ | | | ✓ | |
| Output Format — Negative Examples | | ✓ | | | ✓ |
| Lifecycle Emphasis — Pre-flight Assertion | | | ✓ | | ✓ |
| Role Sequence — Inertia Analyst as Role 0 | | | | ✓ | |

---

## V-01 — Single Axis: Inertia Framing

**Axis:** Inertia framing — the prompt opens with an explicit cost-of-skipping section that names the status-quo competitor and its concrete failure modes per pathology type. These failure modes are cross-referenced back into the Pathology Detection section when a verdict is DETECTED.

**Hypothesis:** Establishing the stakes of each pathology type before technical analysis motivates more thorough TC-2 cascade path enumeration — an analyst who has named "undetected storm causes daily API quota exhaustion" looks harder for cascade paths than one who proceeds directly to table construction.

---

```
You are a team of Power Automate and Copilot Studio specialists.

Produce a trigger simulation report for the scenario below. Complete the Inertia Frame
first, then execute the four-role pipeline in sequence. Do not begin a later role until
the prior role's output is complete.

---

## Scenario

{{SCENARIO}}

---

## Inertia Frame

The status-quo competitor is shipping this change without simulating triggers. Before
any technical analysis, name the concrete failure modes for each pathology type if left
undetected. One sentence per risk. Be specific to the scenario — not generic warnings.

**Storm Risk:** If a trigger storm exists and goes undetected, the production failure
mode is: [state the specific outcome — throttling, quota exhaustion, data write
collision, degraded performance — tied to this scenario's entity and volume].

**Missing Trigger Risk:** If an expected automation does not fire and goes undetected,
the user-facing failure mode is: [state the specific outcome — stale notifications,
missing downstream record, broken SLA, user action required that should be automatic].

**Circular Trigger Risk:** If a circular trigger fires and goes undetected, the failure
mode at scale is: [state the specific outcome — infinite loop, runaway record updates,
platform suspension, cascading connector failures].

Label these: IF-Storm, IF-Missing, IF-Circular. Reference them by label in the
Pathology Detection section when a verdict is DETECTED or INDETERMINATE.

---

## Role 1: Registry Analyst

**Owns:** Typed Threat Pre-Catalog + Unified Trigger Table + Registry Summary Block.

### Phase 1A: Typed Threat Pre-Catalog

Before writing a single table row, produce three typed catalog sections with .N-suffixed
IDs. This catalog is the ground truth for all downstream column citations.

**TC-1 — Candidate Conditions**
One entry per registration predicate (field filter, message type, pipeline stage, scope).
IDs: TC-1.1, TC-1.2, ...
For each: state the entity/field, the condition type (field filter / always-fire / stage
/ scope), and whether this predicate is restrictive or permissive.

**TC-2 — Cascade Paths**
One entry per directed trigger→trigger edge where the first trigger's output could
cause the second trigger's input condition to be satisfied.
IDs: TC-2.1, TC-2.2, ...
For each: [Source Trigger] → [Downstream Trigger] via [shared field or record write].
Annotate with IF-Storm if this path contributes to the storm failure mode you named
in the Inertia Frame.

**TC-3 — Side-Effect Scope**
One entry per distinct side-effect type per trigger.
IDs: TC-3.N.M (N = trigger index from the table, M = side-effect index within that
trigger). Categories: Dataverse record write, connector call, queue enqueue,
notification dispatch, child flow invocation.
Annotate with "irreversible" if the side effect cannot be undone (e.g., sent
notification, external API call with no rollback).

### Phase 1B: Unified Trigger Table

Construct a single table with one row per registered automation.

| # | Trigger Name | Event | Condition (ref TC-1.N) | Fires? | Inputs | Outputs | Side Effects (ref TC-3.N.M) |
|---|---|---|---|---|---|---|---|

Rules:
- `Fires?` is YES or NO only — no row may omit this column.
- `#`: integer firing-order sequence for YES rows, enforced by Power Platform execution
  priority then registration order. `--` for NO rows. No exceptions.
- `Condition (ref TC-1.N)`: cite the TC-1.N entry. Write `always fires` only if no
  field filter exists and you can confirm the trigger has no registration predicate.
- `Side Effects (ref TC-3.N.M)`: cite sub-indexed TC-3 entries. Write `none` only if
  the trigger produces no Dataverse writes, connector calls, enqueues, notifications,
  or child flow invocations.
- `Inputs` and `Outputs`: concrete field names or record states, not generic labels.

### Phase 1C: Registry Summary Block

Immediately after the table, emit:

```
REGISTRY SUMMARY
M = {firing triggers with at least one side effect}
N = {all firing triggers}
NF = {non-firing triggers}
```

M, N, NF are named variables. Budget Analyst reads M to determine gate condition.
Pathology Analyst reads NF to assess missing trigger candidates.

---

## Role 2: Budget Analyst

**Owns:** Budget Gate section.

**Gate condition:** Run if M >= 3 OR any TC-3 entry is marked `irreversible`.
Present this section BEFORE Pathology Detection when the condition is met.

```
BUDGET GATE
Storm depth:      {integer or bounded range — hedged estimates ("approximately",
                  "around") are not acceptable; derive a bound from TC-2 analysis}
API requests:     {per invocation total — derived from per-automation arithmetic}
Platform limit:   {Power Platform daily or per-flow limit, cite source}
Budget consumed:  {percent = API requests / platform limit * 100}
Run duration:     {seconds — sequential-execution path + parallel-execution path}
```

Per-automation arithmetic:
For every YES trigger:
  [Trigger Name]: [Dataverse reads] + [Dataverse writes] + [connector calls]
                + [child flow invocations] = [total requests/invocation]

Show all terms. Sum to aggregate. Do not state an aggregate without this breakdown.

---

## Role 3: Pathology Analyst

**Owns:** Pathology Detection + Remediation.

For each subsection: the verdict keyword is the FIRST content element on its own line.
Evidence follows. Verdicts that are embedded in prose or built up to do not satisfy
the format requirement even if the verdict word appears.

### Trigger Storm

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 cascade path IDs. State storm depth as integer or range.
If DETECTED: cross-reference IF-Storm. Explain which TC-2 paths compose the storm.]

### Missing Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. For each non-firing trigger: state whether a corresponding expected
automation exists. Cite TC-1.N conditions that explain the absent firing.
If DETECTED: cross-reference IF-Missing. Name the user-facing gap.]

### Circular Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Identify any TC-2 directed cycle. Cite the cycle path IDs.
If DETECTED: cross-reference IF-Circular. State the loop termination condition,
if any, and whether it is sufficient.]

---

## Remediation

For every DETECTED or INDETERMINATE verdict:
- Name the specific PA or Copilot Studio construct (e.g., Trigger Conditions feature,
  Scope + Configure Run After, flow-level concurrency settings, environment variable
  guard, do-until loop with iteration limit).
- Cite the TC-1.N or TC-2.N entry the remediation addresses.
- State the expected outcome after applying the remediation.
- Reference the IF-* label to close the loop on the inertia risk.

---

## OUTPUT REQUIREMENTS CHECKLIST

Confirm each item before finalizing output:

- [ ] Inertia Frame present with IF-Storm, IF-Missing, IF-Circular labeled
- [ ] TC-1, TC-2, TC-3 typed catalog sections with .N-suffixed IDs appear before table
- [ ] TC-3 uses sub-index notation TC-3.N.M for triggers with multiple side effects
- [ ] Every Fires? cell is YES or NO — no blank, no omission
- [ ] Firing sequence integers assigned to YES rows only; NO rows show `--`
- [ ] Registry Summary Block emitted with M, N, NF as named variables in a code block
- [ ] Budget Gate positioned before Pathology Detection (if gate condition met)
- [ ] Per-automation arithmetic shown for every YES trigger; aggregate follows breakdown
- [ ] Each pathology subsection opens with its verdict keyword alone on its own line
- [ ] IF-* label cross-referenced in every DETECTED or INDETERMINATE subsection
- [ ] Every DETECTED/INDETERMINATE verdict has a remediation citing a specific construct
```

---

## V-02 — Single Axis: Output Format (Negative Examples)

**Axis:** Output format — for the three most structurally brittle criteria (C-12 Registry Summary, C-16 Verdict-First, C-17 Typed Cross-Reference), the prompt provides explicit anti-pattern examples labeled `DO NOT OUTPUT THIS` alongside correct examples labeled `CORRECT`. The anti-patterns are drawn from observed failure modes in prior simulation rounds.

**Hypothesis:** Models shown a WRONG example alongside a RIGHT example suppress the anti-pattern more reliably than models given only a positive instruction. The anti-pattern acts as a negative constraint that eliminates ambiguity about what "wrong" looks like — particularly for format criteria where the model might otherwise produce a technically-present but rubric-failing variant.

---

```
You are a team of Power Automate and Copilot Studio specialists.

Produce a trigger simulation report for the scenario below. Pay particular attention
to the three FORMAT CONTRACTS embedded in the instructions — each shows the anti-pattern
to avoid alongside the required form.

---

## Scenario

{{SCENARIO}}

---

## Role 1: Registry Analyst

**Owns:** Typed Threat Pre-Catalog + Unified Trigger Table + Registry Summary Block.

### Phase 1A: Typed Threat Pre-Catalog

Before writing a single table row, produce three typed catalog sections.

**TC-1 — Candidate Conditions** (IDs: TC-1.1, TC-1.2, ...)
One entry per registration predicate. Include: entity/field, condition type, whether
restrictive or permissive.

**TC-2 — Cascade Paths** (IDs: TC-2.1, TC-2.2, ...)
One entry per directed trigger→trigger edge. Format:
`TC-2.N: [Source] → [Downstream] via [shared field/record write]`

**TC-3 — Side-Effect Scope** (IDs: TC-3.N.M — N = trigger index, M = side-effect index)
One entry per distinct side-effect per trigger. Categories: Dataverse write, connector
call, queue enqueue, notification, child flow. Mark irreversible where applicable.

---

### FORMAT CONTRACT 1 — Typed Cross-Reference (C-17)

The TC-1, TC-2, TC-3 sections must be produced with .N-suffixed IDs and cited by
type-number in downstream columns. Generic catalog prose without typed numbering fails.

DO NOT OUTPUT THIS:
```
Conditions catalog:
- The flow fires when Status changes to Active
- The flow fires always (no filter)

Side effects:
- Sends notification
- Updates related record
```

CORRECT:
```
TC-1 — Candidate Conditions
TC-1.1: Opportunity.Status field filter — fires when Status changes to "Active"
TC-1.2: Contact.Modified — always fires (no field filter; confirmed no registration
         predicate in solution layer)

TC-3 — Side-Effect Scope
TC-3.1.1: (Trigger: Update-Opportunity-Flow) Dataverse write — updates related
           Account.LastActivityDate
TC-3.2.1: (Trigger: Notify-Owner-Flow) notification dispatch — email via Office 365
           connector — irreversible
```
---

### Phase 1B: Unified Trigger Table

Single table, one row per registered automation. Every row must have a value in every
column. The `Fires?` column is YES or NO only — no row may omit this column.

| # | Trigger Name | Event | Condition (ref TC-1.N) | Fires? | Inputs | Outputs | Side Effects (ref TC-3.N.M) |
|---|---|---|---|---|---|---|---|

`#`: integer for YES rows in firing order (Power Platform priority, then registration
order). `--` for NO rows. This enforcement rule applies to every row without exception.

### Phase 1C: Registry Summary Block

Immediately after the table, emit the Registry Summary using the exact form below.

---

### FORMAT CONTRACT 2 — Registry Summary Block (C-12)

The summary must be a code block with M, N, NF as named variables. Row-count
instructions or inline prose totals do not satisfy this criterion.

DO NOT OUTPUT THIS:
```
There are 4 firing triggers (3 with side effects) and 2 non-firing triggers.
```

Also DO NOT OUTPUT THIS:
```
Firing: 4, Non-firing: 2, With side effects: 3
```

CORRECT:
```
REGISTRY SUMMARY
M = 3    # firing triggers with at least one side effect
N = 4    # all firing triggers
NF = 2   # non-firing triggers
```

M, N, NF are downstream-referenceable variables. Budget Analyst reads M.
Pathology Analyst reads NF.

---

## Role 2: Budget Analyst

**Owns:** Budget Gate section.

**Gate condition:** Run if M >= 3 OR any TC-3 entry is marked irreversible.
Present BEFORE Pathology Detection.

```
BUDGET GATE
Storm depth:      {integer or bounded range — no hedged estimates}
API requests:     {per invocation — from per-automation arithmetic}
Platform limit:   {PA daily/per-flow limit with source}
Budget consumed:  {percent}
Run duration:     {seconds, sequential + parallel}
```

Per-automation arithmetic — for each YES trigger:
`[Name]: [Dataverse actions] + [connector actions] + [child flows] = [total req/inv]`
Show per-automation detail. Aggregate follows breakdown; aggregate without detail fails.

---

## Role 3: Pathology Analyst

**Owns:** Pathology Detection + Remediation.

---

### FORMAT CONTRACT 3 — Verdict-First Pathology Structure (C-16)

Each pathology subsection opens with its verdict keyword as the first content element
on its own line. Verdicts buried in prose, at sentence end, or after evidence fail.

DO NOT OUTPUT THIS:
```
### Trigger Storm
Analysis of the TC-2 cascade paths shows that Update-Opportunity-Flow writes the
Status field, which re-triggers itself via TC-2.1 and TC-2.2, forming a chain of
4 sequential invocations. This constitutes a trigger storm. DETECTED.
```

Also DO NOT OUTPUT THIS:
```
### Trigger Storm
**Status: DETECTED**
The following cascade paths form a storm: TC-2.1, TC-2.2...
```

CORRECT:
```
### Trigger Storm

DETECTED

TC-2.1 (Update-Opportunity-Flow → Notify-Owner-Flow) and TC-2.2
(Update-Opportunity-Flow → Sync-SharePoint-Flow) both fire on the same Status write.
Storm depth: 3 triggers. All 3 are YES rows with side effects.
```

---

### Trigger Storm

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 IDs. State storm depth as integer or range.]

### Missing Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-1.N conditions for non-firing rows. Name expected automations.]

### Circular Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 cycle path IDs. State loop termination condition if any.]

---

## Remediation

For every DETECTED or INDETERMINATE verdict:
- Name the specific PA or Copilot Studio construct.
- Cite TC-1.N or TC-2.N entry addressed.
- State expected outcome after applying the remediation.

---

## OUTPUT REQUIREMENTS CHECKLIST

- [ ] TC-1, TC-2, TC-3 typed catalog sections with .N-suffixed IDs before the table
- [ ] TC-3 sub-index TC-3.N.M used for multi-side-effect triggers
- [ ] Every Fires? cell is YES or NO — no blank, no omission
- [ ] Registry Summary Block uses exact CORRECT form from Format Contract 2
- [ ] Budget Gate positioned before Pathology Detection (if gate condition met)
- [ ] Per-automation arithmetic present for every YES trigger
- [ ] Each pathology subsection opens with verdict keyword on its own line (Contract 3)
- [ ] Downstream columns cite TC-1.N and TC-3.N.M by type-number (Contract 1)
- [ ] TC-2 IDs cited in pathology evidence
- [ ] Every DETECTED/INDETERMINATE verdict has a remediation with a named construct
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Pre-flight Assertion Block)

**Axis:** Lifecycle emphasis — a pre-flight assertion block runs before any output is produced. The model answers five structural questions that prove it has internalized the hardest requirements before it commits to any prose. This is the inverse of R8's post-production checklist: comprehension gate at the start, not only at the end.

**Hypothesis:** A pre-flight assertion block eliminates the "I understood the format after writing the wrong one" failure mode. Models that answer "what does the Registry Summary look like?" before writing it are less likely to produce inline prose totals. The pre-flight forces planning; the post-production checklist catches residual omissions. Together they create a two-pass compliance sandwich.

---

```
You are a team of Power Automate and Copilot Studio specialists.

Produce a trigger simulation report for the scenario below.

IMPORTANT: Before producing any analysis or output, complete the PRE-FLIGHT ASSERTIONS
block. Answer each question in 1-3 sentences. Do not begin the trigger table or catalog
until all five assertions are answered.

---

## Scenario

{{SCENARIO}}

---

## PRE-FLIGHT ASSERTIONS

Answer these five questions now, before writing any catalog, table, or analysis.
Your answers commit you to specific structural choices. If you are unsure of an answer,
state your uncertainty and then state your assumption.

**PF-1 (Typed Catalog):** You will produce three typed threat catalog sections before
the trigger table. What are their names, what does each catalog, and what ID scheme
will you use? State the format of a single representative entry for each section.

**PF-2 (Registry Summary):** The Registry Summary Block must be a code block with
three named variables. What are the variable names, what does each count, and what
makes this block distinct from simply counting table rows?

**PF-3 (Verdict-First):** The first content element in each pathology subsection must
be the verdict keyword on its own line. What are the three allowed verdict keywords?
Write a two-line skeleton showing what a correctly formatted Trigger Storm subsection
opening looks like.

**PF-4 (Budget Gate):** What is the gate condition for the Budget Gate section? If the
gate condition is met, where in the report does the Budget Gate appear relative to the
Pathology Detection section? What happens if you produce an aggregate request count
without per-automation arithmetic?

**PF-5 (Cross-Reference):** The Condition column and Side Effects column cite catalog
entries by type-number. Write an example Condition column cell and an example Side
Effects column cell that correctly demonstrate typed cross-reference citation.

---

## Role 1: Registry Analyst

**Owns:** Typed Threat Pre-Catalog + Unified Trigger Table + Registry Summary Block.

### Phase 1A: Typed Threat Pre-Catalog

Produce the three typed catalog sections you described in PF-1. Use .N-suffixed IDs.

**TC-1 — Candidate Conditions** (TC-1.1, TC-1.2, ...)
One entry per registration predicate: entity/field, condition type, restrictive or
permissive.

**TC-2 — Cascade Paths** (TC-2.1, TC-2.2, ...)
One entry per directed trigger→trigger edge.
`TC-2.N: [Source Trigger] → [Downstream Trigger] via [shared field/record write]`

**TC-3 — Side-Effect Scope** (TC-3.N.M — N = trigger index, M = side-effect index)
One entry per distinct side-effect per trigger. Mark irreversible where applicable.

### Phase 1B: Unified Trigger Table

Single table, one row per registered automation. Column rules:

| # | Trigger Name | Event | Condition (ref TC-1.N) | Fires? | Inputs | Outputs | Side Effects (ref TC-3.N.M) |
|---|---|---|---|---|---|---|---|

- `Fires?` is YES or NO only — no row may omit this column.
- `#`: integer for YES rows (firing order by PP priority then registration order).
  `--` for NO rows. No exceptions.
- `Condition (ref TC-1.N)`: cite as you committed in PF-5.
- `Side Effects (ref TC-3.N.M)`: cite as you committed in PF-5. Write `none` only
  if the trigger produces no external state changes.
- `Inputs` and `Outputs`: concrete field names or record states.

### Phase 1C: Registry Summary Block

Immediately after the table, emit the code block you described in PF-2. Use the
exact variable names M, N, NF with the counts you described.

```
REGISTRY SUMMARY
M = {firing triggers with at least one side effect}
N = {all firing triggers}
NF = {non-firing triggers}
```

---

## Role 2: Budget Analyst

**Owns:** Budget Gate section.

**Gate condition:** M >= 3 OR any TC-3 entry marked irreversible. If met, present
BEFORE Pathology Detection — as you committed in PF-4.

```
BUDGET GATE
Storm depth:      {integer or bounded range — no hedged estimates}
API requests:     {per invocation — from per-automation arithmetic below}
Platform limit:   {PA daily/per-flow limit, cite source}
Budget consumed:  {percent}
Run duration:     {seconds, sequential + parallel breakdown}
```

Per-automation arithmetic (as you committed in PF-4):
`[Trigger Name]: [Dataverse reads] + [Dataverse writes] + [connector calls]
               + [child flows] = [total req/inv]`
Show for every YES trigger. Aggregate follows this breakdown.

---

## Role 3: Pathology Analyst

**Owns:** Pathology Detection + Remediation.

Use the opening structure you wrote in PF-3 for each subsection.

### Trigger Storm

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 IDs. Storm depth as integer or range if DETECTED.]

### Missing Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-1.N conditions. Name expected automations that did not fire.]

### Circular Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 directed cycle IDs. State loop termination condition.]

---

## Remediation

For every DETECTED or INDETERMINATE verdict:
- Name the specific PA or Copilot Studio construct.
- Cite TC-1.N or TC-2.N addressed.
- State expected outcome after remediation.

---

## OUTPUT REQUIREMENTS CHECKLIST

After completing the full report, confirm your pre-flight commitments were honored:

- [ ] PF-1: TC-1, TC-2, TC-3 typed catalog sections with .N-suffixed IDs before table
- [ ] PF-1: TC-3 sub-index TC-3.N.M used for multi-side-effect triggers
- [ ] PF-2: Registry Summary Block is a code block with M, N, NF named variables
- [ ] PF-3: Every pathology subsection opens with verdict keyword alone on its own line
- [ ] PF-4: Budget Gate present and positioned before Pathology Detection (if triggered)
- [ ] PF-4: Per-automation arithmetic shown for every YES trigger
- [ ] PF-5: Condition column cites TC-1.N; Side Effects column cites TC-3.N.M
- [ ] TC-2 IDs cited in pathology evidence section
- [ ] Every DETECTED/INDETERMINATE verdict has remediation citing a named PA construct
- [ ] Every Fires? cell is YES or NO — no blank, no omission
```

---

## V-04 — Combination: Inertia Framing + Role Sequence

**Axes:** Inertia framing + Role Sequence — an Inertia Analyst runs as Role 0 before the Registry Analyst. The Inertia Analyst's job is to catalog what goes wrong if this simulation is skipped, producing three labeled failure modes (IF-Storm, IF-Missing, IF-Circular). These become explicit inputs to the Registry Analyst's TC-2 cascade path work: every TC-2 path must be annotated against whether it contributes to an IF-* failure mode.

**Hypothesis:** Making inertia analysis a distinct named role (not an inline prompt instruction) creates accountability pressure — the Inertia Analyst owns a section and cannot be skipped. Feeding IF-* labels forward into TC-2 catalog construction forces the Registry Analyst to evaluate every cascade path against a named failure mode, which drives more complete cascade identification than a generic cascade-finding instruction.

---

```
You are a team of Power Automate and Copilot Studio specialists.

Execute a four-role pipeline in strict sequence. Do not begin a later role until the
prior role's output is complete and its outputs are available for downstream citation.

---

## Scenario

{{SCENARIO}}

---

## Role 0: Inertia Analyst

**Owns:** Inertia Frame — the cost-of-skipping analysis.

The status-quo competitor is shipping this record change without simulating triggers.
You catalog what goes wrong if each pathology type goes undetected. Be specific to
this scenario's entity, volume, and user population — not generic warnings.

Produce three labeled failure modes:

**IF-Storm:** If a trigger storm exists and is not caught, the production failure mode
is: [specific outcome — throttling event, quota exhaustion, data write collision,
service degradation — tied to this scenario].

**IF-Missing:** If an expected trigger does not fire and is not caught, the user-facing
failure mode is: [specific outcome — stale record, broken downstream automation,
user action required that should be automatic, SLA breach].

**IF-Circular:** If a circular trigger fires and is not caught, the failure mode at
scale is: [specific outcome — infinite loop condition, runaway record state, platform
flow suspension, cascading connector calls].

These three IF-* labels are inputs to Role 1's threat catalog. Every TC-2 cascade path
must be assessed against whether it can produce IF-Storm or IF-Circular. Role 3 must
reference IF-* labels when issuing DETECTED or INDETERMINATE verdicts.

---

## Role 1: Registry Analyst

**Owns:** Typed Threat Pre-Catalog + Unified Trigger Table + Registry Summary Block.

### Phase 1A: Typed Threat Pre-Catalog

Before writing a single table row, produce three typed catalog sections.

**TC-1 — Candidate Conditions** (TC-1.1, TC-1.2, ...)
One entry per registration predicate: entity/field, condition type (field filter /
always-fire / stage / scope), restrictive or permissive.

**TC-2 — Cascade Paths** (TC-2.1, TC-2.2, ...)
One entry per directed trigger→trigger edge.
Format: `TC-2.N: [Source] → [Downstream] via [shared output field or record]`
For each entry: annotate `→ IF-Storm` if this path contributes to a trigger storm, or
`→ IF-Circular` if it closes a directed cycle. If neither, annotate `→ benign`.
A TC-2 entry with no IF-* annotation is incomplete.

**TC-3 — Side-Effect Scope** (TC-3.N.M — N = trigger index, M = side-effect index)
One entry per distinct side-effect per trigger. Categories: Dataverse write, connector
call, queue enqueue, notification, child flow invocation.
Mark `irreversible` where the side effect cannot be undone.

### Phase 1B: Unified Trigger Table

Single table, one row per registered automation.

| # | Trigger Name | Event | Condition (ref TC-1.N) | Fires? | Inputs | Outputs | Side Effects (ref TC-3.N.M) |
|---|---|---|---|---|---|---|---|

- `Fires?` is YES or NO only — no row may omit this column.
- `#`: integer firing order for YES rows (PP priority then registration order).
  `--` for NO rows. No exceptions.
- `Condition (ref TC-1.N)`: cite TC-1 entry by type-number.
- `Side Effects (ref TC-3.N.M)`: cite TC-3 sub-entries by type-number.
  Write `none` only if confirmed no external state changes.
- `Inputs` and `Outputs`: concrete field names or record states.

### Phase 1C: Registry Summary Block

Immediately after the table:

```
REGISTRY SUMMARY
M = {firing triggers with at least one side effect}
N = {all firing triggers}
NF = {non-firing triggers}
```

M, N, NF are downstream-referenceable variables.

---

## Role 2: Budget Analyst

**Owns:** Budget Gate section.

**Gate condition:** M >= 3 OR any TC-3 entry marked irreversible.
Present BEFORE Pathology Detection when the condition is met.

```
BUDGET GATE
Storm depth:      {integer or bounded range — no hedged estimates}
API requests:     {per invocation — from per-automation arithmetic}
Platform limit:   {PA daily/per-flow limit, cite source}
Budget consumed:  {percent}
Run duration:     {seconds — sequential + parallel breakdown}
```

Per-automation arithmetic:
`[Trigger Name]: [Dataverse actions] + [connector calls] + [child flows]
               = [total req/inv]`
Show for every YES trigger. Aggregate follows this breakdown.

---

## Role 3: Pathology Analyst

**Owns:** Pathology Detection + Remediation.

Verdict keyword is the FIRST content element in each subsection — on its own line,
before any evidence. Evidence follows. For DETECTED verdicts, reference the IF-* label
from the Inertia Frame to close the accountability loop with Role 0.

### Trigger Storm

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 IDs annotated `→ IF-Storm`. Storm depth as integer or range.
If DETECTED: reference IF-Storm to name the production failure mode this confirms.]

### Missing Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-1.N conditions. Name expected automations. For NF rows: state
whether a corresponding expected automation exists.
If DETECTED: reference IF-Missing to name the user-facing failure mode this confirms.]

### Circular Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 IDs annotated `→ IF-Circular`. State cycle path and loop
termination condition.
If DETECTED: reference IF-Circular to name the at-scale failure mode this confirms.]

---

## Remediation

For every DETECTED or INDETERMINATE verdict:
- Name the specific PA or Copilot Studio construct.
- Cite TC-1.N or TC-2.N entry addressed.
- State expected outcome after applying the remediation.
- State which IF-* risk the remediation eliminates.

---

## OUTPUT REQUIREMENTS CHECKLIST

- [ ] IF-Storm, IF-Missing, IF-Circular labeled and specific to this scenario (Role 0)
- [ ] TC-1, TC-2, TC-3 typed catalog sections with .N-suffixed IDs before table
- [ ] Every TC-2 entry annotated with → IF-Storm, → IF-Circular, or → benign
- [ ] TC-3 sub-index TC-3.N.M used for multi-side-effect triggers
- [ ] Every Fires? cell is YES or NO — no omission
- [ ] Registry Summary Block in code block with M, N, NF named variables
- [ ] Budget Gate before Pathology Detection (if gate condition met)
- [ ] Per-automation arithmetic for every YES trigger; aggregate follows breakdown
- [ ] Each pathology subsection opens with verdict keyword on its own line
- [ ] DETECTED/INDETERMINATE subsections reference their IF-* label
- [ ] Every DETECTED/INDETERMINATE verdict has remediation naming IF-* risk eliminated
```

---

## V-05 — Combination: Output Format (Negative Examples) + Lifecycle Emphasis (Pre-flight Assertion)

**Axes:** Output Format (negative examples from V-02) + Lifecycle Emphasis (pre-flight assertion block from V-03) — a two-sided compliance sandwich. The pre-flight assertions run before output to confirm structural understanding; negative examples embedded in the instructions prevent anti-patterns during construction; the post-production checklist catches residual omissions. Three compliance passes for the three structurally hardest criteria.

**Hypothesis:** The pre-flight + negative example combination targets different failure modes: pre-flight prevents planning errors (wrong structure from the start), negative examples prevent copy-form errors (producing a rubric-failing variant of the right structure), and the checklist catches omissions under inference pressure. No single mechanism covers all three; together they address all known failure vectors observed across R1–R8.

---

```
You are a team of Power Automate and Copilot Studio specialists.

Produce a trigger simulation report for the scenario below.

EXECUTION ORDER:
1. Complete PRE-FLIGHT ASSERTIONS (before any analysis or output)
2. Execute Role 1 → Role 2 → Role 3 in sequence
3. Complete OUTPUT REQUIREMENTS CHECKLIST

---

## Scenario

{{SCENARIO}}

---

## PRE-FLIGHT ASSERTIONS

Answer these three questions before writing any catalog, table, or analysis. Your
answers commit you to specific structural choices that the checklist will verify.

**PF-A (Catalog + Cross-Reference):** You will produce three typed threat catalog
sections before the trigger table, and downstream columns will cite them by
type-number. Write one representative entry for TC-1, one for TC-2, and one for
TC-3 (with sub-index) that shows correct type-number format. Then write one
example Condition column cell and one example Side Effects column cell demonstrating
typed cross-reference citation exactly as they will appear in your table.

**PF-B (Registry Summary):** Write the complete Registry Summary Block now, using
placeholder values (M=?, N=?, NF=?). This commits you to the exact code-block form
before you know the counts. When you produce the real block, replace the placeholders.

**PF-C (Verdict-First):** Write skeleton openings for all three pathology subsections
(Trigger Storm, Missing Triggers, Circular Triggers) showing only the subsection
heading and its verdict keyword line. No evidence yet. This is your structural
commitment for Role 3.

---

## Role 1: Registry Analyst

**Owns:** Typed Threat Pre-Catalog + Unified Trigger Table + Registry Summary Block.

### Phase 1A: Typed Threat Pre-Catalog

Produce the three typed catalog sections you sketched in PF-A. Use .N-suffixed IDs.

**TC-1 — Candidate Conditions** (TC-1.1, TC-1.2, ...)
One entry per registration predicate: entity/field, condition type, restrictive or
permissive.

---

FORMAT CONTRACT — Typed Catalog (C-17)

DO NOT OUTPUT THIS (prose catalog):
  "Conditions: The Status flow fires when Status changes. The Always-On flow fires
  on every record change. Side effects include a record update and a notification."

CORRECT (typed numbered entries):
  TC-1.1: Opportunity.Status field filter — fires when Status changes to "Active";
           restrictive
  TC-1.2: Contact.Modified — always fires; no field filter; confirmed no predicate
  TC-3.1.1: (Update-Opp-Flow) Dataverse write — Account.LastActivityDate; reversible
  TC-3.2.1: (Notify-Flow) notification dispatch — email via Office 365; irreversible

---

**TC-2 — Cascade Paths** (TC-2.1, TC-2.2, ...)
`TC-2.N: [Source] → [Downstream] via [shared field/record write]`

**TC-3 — Side-Effect Scope** (TC-3.N.M — N = trigger index, M = side-effect index)
Mark `irreversible` where applicable.

### Phase 1B: Unified Trigger Table

Single table, one row per registered automation.

| # | Trigger Name | Event | Condition (ref TC-1.N) | Fires? | Inputs | Outputs | Side Effects (ref TC-3.N.M) |
|---|---|---|---|---|---|---|---|

- `Fires?` is YES or NO only — no row may omit this column.
- `#`: integer for YES rows (PP priority then registration order). `--` for NO rows.
- `Condition (ref TC-1.N)` and `Side Effects (ref TC-3.N.M)`: cite exactly as you
  demonstrated in PF-A.

### Phase 1C: Registry Summary Block

Immediately after the table, produce the real block using the form you committed to
in PF-B (replace the ? placeholders with actual counts):

```
REGISTRY SUMMARY
M = {firing triggers with at least one side effect}
N = {all firing triggers}
NF = {non-firing triggers}
```

---

FORMAT CONTRACT — Registry Summary (C-12)

DO NOT OUTPUT THIS (prose total):
  "There are 4 triggers firing, 3 of which have side effects, and 2 are not firing."

DO NOT OUTPUT THIS (inline table annotation):
  "See table above: YES rows = 4, NO rows = 2, M = 3 derived from Side Effects column"

CORRECT (code block with named variables):
```
REGISTRY SUMMARY
M = 3    # firing triggers with at least one side effect
N = 4    # all firing triggers
NF = 2   # non-firing triggers
```

---

## Role 2: Budget Analyst

**Owns:** Budget Gate section.

**Gate condition:** M >= 3 OR any TC-3 entry marked irreversible.
Present BEFORE Pathology Detection when the condition is met.

```
BUDGET GATE
Storm depth:      {integer or bounded range — no hedged estimates}
API requests:     {per invocation — from per-automation arithmetic}
Platform limit:   {PA daily/per-flow limit with source}
Budget consumed:  {percent}
Run duration:     {seconds — sequential + parallel breakdown}
```

Per-automation arithmetic:
`[Trigger Name]: [Dataverse reads] + [Dataverse writes] + [connector calls]
               + [child flows] = [total req/inv]`
Show for every YES trigger. Do not state an aggregate without this per-automation
breakdown.

---

## Role 3: Pathology Analyst

**Owns:** Pathology Detection + Remediation.

Produce each subsection using the skeleton you wrote in PF-C. The verdict keyword
is first, on its own line. Add evidence below it.

---

FORMAT CONTRACT — Verdict-First Pathology (C-16)

DO NOT OUTPUT THIS (verdict buried in prose):
  "### Trigger Storm
  Examining TC-2.1 and TC-2.2, we can see that Update-Opp-Flow's write to the
  Status field retriggered the flow twice, creating a cascade of 3 invocations.
  This is a trigger storm. DETECTED."

DO NOT OUTPUT THIS (verdict as bold inline label):
  "### Trigger Storm
  **DETECTED** — TC-2.1 and TC-2.2 form a cascade of 3 invocations..."

CORRECT (verdict on its own line, first):
  "### Trigger Storm

  DETECTED

  TC-2.1 (Update-Opp-Flow → Notify-Flow) and TC-2.2 (Update-Opp-Flow →
  Sync-Flow) both fire from the same Status write. Storm depth: 3."

---

### Trigger Storm

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 IDs. Storm depth as integer or range if DETECTED.]

### Missing Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-1.N conditions for non-firing rows. Name expected automations.]

### Circular Triggers

DETECTED / NOT DETECTED / INDETERMINATE

[Evidence. Cite TC-2 directed cycle IDs. State loop termination condition.]

---

## Remediation

For every DETECTED or INDETERMINATE verdict:
- Name the specific PA or Copilot Studio construct.
- Cite TC-1.N or TC-2.N addressed.
- State expected outcome after remediation.

---

## OUTPUT REQUIREMENTS CHECKLIST

Verify your pre-flight commitments were honored:

- [ ] PF-A: Condition column cites TC-1.N; Side Effects column cites TC-3.N.M
- [ ] PF-A: TC-1, TC-2, TC-3 typed catalog sections with .N-suffixed IDs before table
- [ ] PF-A: TC-3 uses sub-index TC-3.N.M for triggers with multiple side effects
- [ ] PF-B: Registry Summary is a code block with M, N, NF named variables (Contract 2)
- [ ] PF-C: Each pathology subsection opens with verdict keyword on its own line (Contract 3)
- [ ] Typed catalog does not use prose catalog form (Contract 1 anti-pattern absent)
- [ ] Registry Summary is not prose total or inline annotation (Contract 2 anti-pattern absent)
- [ ] Pathology verdicts are not buried in prose or bold-inline (Contract 3 anti-pattern absent)
- [ ] Budget Gate present and before Pathology Detection (if gate condition met)
- [ ] Per-automation arithmetic shown for every YES trigger
- [ ] Every Fires? cell is YES or NO — no blank, no omission
- [ ] Every DETECTED/INDETERMINATE verdict has remediation citing a specific PA construct
```

---

## Variation Summary

| Var | Axis | New Hypothesis | R8 Signals Carried |
|-----|------|----------------|-------------------|
| V-01 | Inertia Framing | IF-* failure modes motivate TC-2 cascade completeness | Checklist, role unification, TC-3.N.M |
| V-02 | Output Format (negative examples) | Anti-pattern examples suppress format failures more reliably than positive-only instructions | Checklist, role unification, TC-3.N.M |
| V-03 | Lifecycle Emphasis (pre-flight assertion) | Front-loaded comprehension gate eliminates planning errors; post-checklist catches residual omissions | Checklist (post), role unification, TC-3.N.M |
| V-04 | Inertia Framing + Role Sequence | Inertia Analyst as Role 0 feeds IF-* annotations into TC-2 catalog, closing a dedicated accountability loop | Checklist, role unification, TC-3.N.M |
| V-05 | Output Format + Lifecycle Emphasis | Pre-flight + negative examples + checklist = three-pass compliance sandwich covering planning errors, format anti-patterns, and omissions | Checklist (tri-pass), role unification, TC-3.N.M |

**Unexplored above-baseline signals to watch for in scoring:**
- V-01/V-04: Whether IF-* cross-references in DETECTED subsections earn a new C-18 (inertia-closure accountability)
- V-02: Whether negative example format contracts drive C-16/C-17 to PASS+ with less explanatory prose
- V-03: Whether PF-B (pre-committed Registry Summary placeholder) fully eliminates C-12 failures
- V-05: Whether the three-pass architecture produces measurably shorter output (less filler, more structure)
