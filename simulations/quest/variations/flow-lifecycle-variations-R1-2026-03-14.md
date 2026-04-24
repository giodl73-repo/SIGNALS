Written to `simulations/quest/variations/flow-lifecycle-variations-R1-2026-03-14.md`.

---

## Round 1 Summary — flow-lifecycle

| V | Axis | C-01/C-05 mechanism | C-03 mechanism | Predicted ceiling |
|---|------|---------------------|----------------|-------------------|
| **V-01** | Output format (state table) | Pre-printed columns: Entry Condition, Exits, Type | Owner (R-ID) column | Essential pass; recommended via pre-printed sections |
| **V-02** | Role sequence (roles first) | State sub-fields inside walkthrough | Registry gate + R-ID reference at every decision point | Essential pass; C-03 strongest single-axis guarantee |
| **V-03** | Lifecycle emphasis (phase sections) | Phase boundary declarations + state blocks per phase | Domain roles in PROCESS PROFILE + phase Owner | Essential pass; C-02 traces more process-specific |
| **V-04** | Axes 1+2 | Table columns + sub-fields | Registry gate + Owner column in table | Strong essential + recommended coverage |
| **V-05** | Full synthesis | Table columns per phase section | Registry gate + phase owner + table column (3 surfaces) | **Golden candidate** — all criteria structurally covered |

**Key design decisions:**

- **C-01 primary surface:** Table columns (V-01 axis) — a blank `Entry Condition` cell is visible omission; the same omission in prose is invisible. V-03 tests whether phase boundary declarations are sufficient without columns.
- **C-03 primary surface:** Role registry gate (V-02 axis) — forces domain-specific names before any state is written. Generic names are caught at the gate, not discovered after the fact.
- **C-04 structural lock:** All five variations pre-print `BOTTLENECK B-01/B-02` and `MISSING G-01` blocks with cause + downstream impact sub-fields. Stating findings without causal explanation leaves a blank labeled field — structurally visible.
- **C-09/C-10 coverage:** All five variations include pre-printed CROSS-PROCESS INTERACTIONS and SLA ANALYSIS sections. C-10 requires minimum 3 annotated nodes; the table has 3 pre-printed rows to make count enforcement visible.

**V-05 vs V-04 open question for live runs:** Does the phase-section framing produce more process-specific exception traces (C-02) and edge cases (C-07), or does V-04's flatter structure produce equivalent output with less template overhead?
se.
**Hypothesis:** Pre-printed table columns make C-01 (entry condition + labeled exits per state)
and C-08 (decision point with owner role) structurally unavoidable. A blank cell in a pre-printed
table is visible omission; the same omission in prose is invisible. The exception, bottleneck,
edge case, and SLA sections are also pre-printed to push toward aspirational criteria.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers and table columns are fixed.
Do not reorder, rename, or remove any section header or column header.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE -- inferred from topic context]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support -- inferred from process type]

## TERMINAL STATES
[Declare all terminal states before writing any state in the transition table.
Every branch in the table below must reach one of these states.]
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[Add CANCEL: [Name] or additional terminal states as appropriate for the process type.]

## STATE TRANSITIONS
[Every state appears as exactly one row. All columns required -- do not leave any cell blank.
Exits format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]". Multiple exits
separated by semicolons. State type must be one of: NORMAL / DECISION / FORK / JOIN / TERMINAL.]

| S-ID | State Name | Entry Condition | Owner Role | Exits (condition -> next) | Type |
|------|------------|-----------------|------------|---------------------------|------|
| S-01 | [Name] | [What must be true to enter this state] | [Domain role name] | [cond] -> S-02; [cond] -> TERMINAL:[name] | NORMAL |
| S-02 | [Name] | [What must be true to enter this state] | [Domain role name] | [cond] -> S-03; [cond] -> S-04 | DECISION |
[Continue until all states are represented, including all terminal states as final rows.]

[Terminal state rows:]
| S-T1 | [SUCCESS state name] | [Entry condition] | -- | -- | TERMINAL |
| S-T2 | [FAILURE state name] | [Entry condition] | -- | -- | TERMINAL |

## PARALLEL PATHS
[Model any concurrent work streams. Required if the process has concurrent branches.
Fork state: the state where the path splits. Join state: where branches re-converge.]
Fork at: S-[ID] ([State Name])
  Branch A: S-[ID] -> S-[ID] -> ... -> S-[JOIN-ID]
  Branch B: S-[ID] -> S-[ID] -> ... -> S-[JOIN-ID]
Join at: S-[ID] ([State Name])
  Join type: AND-join / OR-join
  Join condition: [What all branches must deliver before the join state is entered]
[If no parallel paths exist: write "No parallel paths. Process is fully sequential."]

## EXCEPTION FLOWS
[3+ named exception traces required. Each must start from a trigger state and reach a terminal.
Exception flows are distinct from edge cases: they are named failure scenarios with a traced path.]

| E-ID | Exception Name | Trigger State | Trigger Condition | Trace (states) | Terminal Reached |
|------|---------------|---------------|-------------------|----------------|-----------------|
| E-01 | [Name] | S-[ID] | [What condition triggers departure from happy path] | S-[ID] -> S-[ID] -> ... | TERMINAL:[name] |
| E-02 | [Name] | S-[ID] | [What condition triggers departure from happy path] | S-[ID] -> S-[ID] -> ... | TERMINAL:[name] |
| E-03 | [Name] | S-[ID] | [What condition triggers departure from happy path] | S-[ID] -> S-[ID] -> ... | TERMINAL:[name] |
[Add rows for additional exception flows. Each row must reach a declared terminal state.]

## BOTTLENECKS AND GAPS

Bottlenecks (minimum 2 required -- states or transitions where delays commonly accumulate):
| B-ID | State or Transition | Cause | Downstream Impact |
|------|---------------------|-------|-------------------|
| B-01 | [State name or S-ID -> S-ID] | [Why delays accumulate here -- specific mechanism] | [Effect on subsequent states or SLA] |
| B-02 | [State name or S-ID -> S-ID] | [Why delays accumulate here -- specific mechanism] | [Effect on subsequent states or SLA] |
[Add B-03, B-04 if additional bottlenecks exist.]

Missing steps (minimum 1 required -- steps absent from this model that exist in practice):
| G-ID | Label | Missing Step Description | Rationale |
|------|-------|--------------------------|-----------|
| G-01 | MISSING: [Step Name] | [What this step does] | [Why it belongs in real-world practice for this process type] |
[Add G-02 if additional gaps exist.]

## EDGE CASES
[3+ edge cases required. Must not duplicate named exception flows above.
Each edge case is a scenario that falls outside both the happy path and the named exceptions.]

| EC-ID | Triggering Condition | Why Problematic | Correct Response |
|-------|---------------------|-----------------|------------------|
| EC-01 | [Specific condition that creates the case] | [Why the current model cannot handle this correctly] | [What handling should look like] |
| EC-02 | [Specific condition that creates the case] | [Why the current model cannot handle this correctly] | [What handling should look like] |
| EC-03 | [Specific condition that creates the case] | [Why the current model cannot handle this correctly] | [What handling should look like] |

## CROSS-PROCESS INTERACTIONS
[Identify at least one point where this lifecycle touches an adjacent process.
If none exist, write "No cross-process interactions. Rationale: [why this is a self-contained lifecycle]".]

| Sending State | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner |
|---------------|-------------------|--------------|------------------------|---------------|
| S-[ID] | [Adjacent process name] | [Fields or artifact sent] | [What the receiving process returns] | [Role name] |
[Add rows for additional cross-process handoffs.]

## SLA ANALYSIS
[Attach timing annotations to 3+ states or transitions. Flag any node where typical exceeds SLA.]

| State or Transition | SLA Target | Typical Duration | At-Risk? | Risk Reason |
|--------------------|------------|------------------|----------|-------------|
| [Name] | [N hrs / N days] | [N hrs / N days] | YES / NO | [If YES: why typical exceeds target] |
| [Name] | [N hrs / N days] | [N hrs / N days] | YES / NO | [If YES: why typical exceeds target] |
| [Name] | [N hrs / N days] | [N hrs / N days] | YES / NO | [If YES: why typical exceeds target] |
[Add rows as needed. AT-RISK nodes should cross-reference bottleneck entries where applicable.]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, state_count, terminal_states, exception_count,
bottleneck_count, gap_count, parallel_paths, cross_process_count, sla_node_count.
```

---

## V-02: Role Registry Declared Before States

**Axis:** Role sequence -- the ROLE REGISTRY is a named, pre-printed section that must be
completed before any state is traced. Every decision point and approval gate in the walkthrough
must reference a role by R-ID from the registry. Role names are process-specific (no generic
"Approver" or "Reviewer" labels allowed; violators are caught by the validation gate).
**Hypothesis:** Forcing role declaration before state tracing prevents the most common C-03
failure mode: generic role names appearing at decision points because the model defaulted to
placeholders mid-flow. The registry validation gate is an explicit check that surfaces the
failure structurally. When roles are established first, they become a controlled vocabulary
that all downstream sections must use -- this also improves C-08 (decision point explicitness)
because the role is never ambiguous at the point of assignment.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers are fixed. The ROLE REGISTRY must be complete before any state is traced.
Every decision point must reference a role by R-ID from the registry.
Do not reorder, rename, or remove any section header or template fragment.
Do not use generic role names (Approver, Reviewer, Manager) -- all roles must be domain-specific.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE -- inferred from topic context]
Trigger event: [What initiates this lifecycle?]

## ROLE REGISTRY
[Complete this section fully before writing any state, decision point, or exception flow.
Auto-select roles matching the process type:
  L2O       -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P       -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE      -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel
Add or replace roles based on the specific topic context. Minimum 3 roles required.]

| R-ID | Role Name | Domain | Decision Authority | Active Phases |
|------|-----------|--------|--------------------|---------------|
| R-01 | [Domain-specific name] | [Domain] | [What this role approves or decides] | [Which lifecycle phases] |
| R-02 | [Domain-specific name] | [Domain] | [What this role approves or decides] | [Which lifecycle phases] |
| R-03 | [Domain-specific name] | [Domain] | [What this role approves or decides] | [Which lifecycle phases] |
[Add R-04, R-05 as needed for the process type.]

Role validation: Process type is [PROCESS TYPE]. Each approval gate and decision point
below must be owned by one of the roles above. Confirm: [List each R-ID and the gate or
decision it owns. If any decision point has no owner from this registry, flag it here.]

## TERMINAL STATES
[Declare all terminal states. Every state walkthrough path must reach one of these.]
SUCCESS: [Name] -- [Condition]
FAILURE: [Name] -- [Condition]
[CANCEL: [Name] -- [Condition] -- add if the process type supports cancellation]

## STATE WALKTHROUGH
[Walk every state grouped by lifecycle phase. For each state write all sub-fields.
Owner must reference an R-ID from the ROLE REGISTRY. Decision points must list every outcome branch.]

### Phase: [Phase Name]

S-[ID]: [State Name]
  Entry condition: [What must be true before this state is entered]
  Owner: [R-ID] -- [Role Name]
  Exits:
    [condition] -> S-[ID]: [next state name]
    [condition] -> S-[ID]: [next state name or TERMINAL:name]
  Type: NORMAL / DECISION / FORK / JOIN / TERMINAL

[If this state is a DECISION, add:]
  Decision rule: [The specific rule or threshold being evaluated]
  Fallback branch: [condition] -> S-[ID] (required if no explicit else branch exists)

[Repeat for every state in this phase. Separate phases with a sub-header.]

### Phase: [Next Phase Name]
[Continue pattern...]

## PARALLEL PATHS
[If the process has concurrent work streams, model fork and join explicitly.]
Fork at: S-[ID] ([State Name])
  Branch A ([R-ID] owns): S-[ID] -> S-[ID] -> ...
  Branch B ([R-ID] owns): S-[ID] -> S-[ID] -> ...
Join at: S-[ID] ([State Name])
  Join type: AND-join / OR-join
  Join condition: [What all branches must complete before join fires]
[If fully sequential: "No parallel paths. Process is sequential end-to-end."]

## EXCEPTION FLOWS
[3+ named exception traces required. Each must reach a terminal state.
Each exception must reference the handling role by R-ID.]

E-01 [Exception Name]:
  Trigger: S-[ID] ([State Name]) when [condition]
  Trace: S-[ID] -> S-[ID] -> TERMINAL:[name]
  Handling role: [R-ID] -- [Role Name]
  Resolution: [What the role does to reach the terminal state]

E-02 [Exception Name]:
  Trigger: S-[ID] ([State Name]) when [condition]
  Trace: S-[ID] -> S-[ID] -> TERMINAL:[name]
  Handling role: [R-ID] -- [Role Name]
  Resolution: [What the role does to reach the terminal state]

E-03 [Exception Name]:
  Trigger: S-[ID] ([State Name]) when [condition]
  Trace: S-[ID] -> S-[ID] -> TERMINAL:[name]
  Handling role: [R-ID] -- [Role Name]
  Resolution: [What the role does to reach the terminal state]

[Add E-04, E-05 for additional exception flows.]

## BOTTLENECKS AND GAPS

BOTTLENECK B-01: [State or transition name]
  Cause: [Why delays accumulate -- specific mechanism, not generic "slow process"]
  Downstream impact: [Effect on subsequent states, SLA, or dependent roles]
  Owner role: [R-ID] -- role whose action is the delay source

BOTTLENECK B-02: [State or transition name]
  Cause: [Why delays accumulate -- specific mechanism]
  Downstream impact: [Effect on subsequent states, SLA, or dependent roles]
  Owner role: [R-ID]

MISSING G-01: [Step Name]
  Where it belongs: Between S-[ID] ([name]) and S-[ID] ([name])
  Rationale: [Why this step is standard practice for this process type and is absent here]
  Would be owned by: [R-ID]

## EDGE CASES
[3+ edge cases distinct from named exception flows above.]

EC-01: [Triggering condition -- must not duplicate E-01 through E-03]
  Why problematic: [Impact on flow or data integrity]
  Correct response: [What handling should produce]

EC-02: [Triggering condition]
  Why problematic: [Impact on flow or data integrity]
  Correct response: [What handling should produce]

EC-03: [Triggering condition]
  Why problematic: [Impact on flow or data integrity]
  Correct response: [What handling should produce]

## CROSS-PROCESS INTERACTIONS
Sending state: S-[ID] ([State Name])
Receiving process: [Adjacent process name -- e.g., GL posting, Inventory Management, Billing]
Data payload: [Fields or artifact sent across the process boundary]
Expected acknowledgment: [What the adjacent process returns]
Handoff owner: [R-ID] -- [Role Name]
[Add additional handoff entries if multiple cross-process interactions exist.]
[If none: "No cross-process interactions identified. All data flows are internal to this lifecycle."]

## SLA ANALYSIS
[Annotate 3+ states/transitions with timing expectations. Cross-reference bottlenecks.]

| State or Transition | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|--------------------|------------|------------------|----------|---------------------|
| [Name] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: add "AT-RISK NOTE: [reason typical exceeds SLA target]" below the row.]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, state_count, phase_count,
exception_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-03: Lifecycle Emphasis — Named Phase Sections with Explicit Boundaries

**Axis:** Lifecycle emphasis -- each lifecycle phase gets its own named section with three
mandatory boundary declarations: entry trigger (what starts this phase), exit condition
(what ends it), and downstream handoff (what artifact or data passes to the next phase).
States, decision points, and exception flows are organized inside the phase they belong to
rather than in a single flat table.
**Hypothesis:** Phase-section structure forces the model to reason about the lifecycle as
a sequence of bounded units rather than a flat list of states. This increases the probability
that C-01 (entry conditions) is satisfied at the phase level even when individual state
entries are incomplete, and that C-05 (terminal states) is satisfied because each phase
must declare its exit condition. Phase sections also create natural homes for phase-specific
exception flows, which may improve C-02 exception trace specificity compared to a flat
exception table.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers are fixed. Each lifecycle phase is an explicit named section with
declared entry, exit, and handoff. Do not reorder, rename, or remove any section header
or sub-field label.

---

## PROCESS PROFILE
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [What initiates this lifecycle?]
Domain roles (auto-selected from process type): [Comma-separated list of domain-specific role names]
Terminal states:
  SUCCESS: [Name] -- [Condition]
  FAILURE: [Name] -- [Condition]
  [CANCEL: [Name] -- add if applicable]

## PHASE MAP
[Declare all phases before writing phase detail sections.
Every phase in this table must have a corresponding detail section below.]

| Phase | Entry Trigger | Owner Role | Exit Condition | Downstream Handoff |
|-------|--------------|------------|----------------|--------------------|
| [Name] | [What starts this phase] | [Role] | [What ends it] | [Artifact or data passed forward, or TERMINAL:name] |
[Add rows for every phase. Minimum 3 phases expected for a realistic lifecycle.]

---

[For every phase declared in the PHASE MAP, write a detail section using the template below.
The phase name in the section header must match exactly the name in the PHASE MAP.]

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP -- the exact condition or event that starts this phase]
Owner: [Role name -- domain-specific, matching PROCESS PROFILE]
Exit condition: [The condition that marks this phase complete]
Downstream handoff: [Artifact or data delivered to next phase or adjacent process]

States in this phase:
  S-[ID]: [State Name]
    Entry condition: [What must be true before this state is entered]
    Owner: [Role]
    Exits:
      [condition] -> S-[ID]
      [condition] -> S-[ID] (or TERMINAL:[name])
    [If DECISION state:] Decision rule: [specific rule evaluated] | Fallback: [condition] -> S-[ID]

  [Repeat for every state in this phase]

Decision points in this phase:
  [For each DECISION-type state, restate the branch conditions and their owners explicitly:]
  D-[ID] ([State Name]):
    Condition: [Rule evaluated]
    Owner: [Role]
    Branch YES: [condition] -> S-[ID]
    Branch NO:  [condition] -> S-[ID]
    Fallback:   [condition] -> S-[ID] (required if not exhaustively covered above)

Parallel work streams in this phase:
  [If this phase has concurrent branches:]
  Fork: S-[ID] -> Branch A: [state list] | Branch B: [state list] -> Join: S-[ID]
  Join type: AND-join / OR-join
  Join condition: [What all branches must deliver before the join fires]
  [If none: "Sequential -- no concurrent branches in this phase."]

Exception traces originating in this phase (at least one per phase where realistic):
  E-[ID] [Name]:
    Trigger: S-[ID] when [condition]
    Trace: S-[ID] -> S-[ID] -> TERMINAL:[name]
    Handling: [Role and action]

[Repeat the PHASE section for every phase declared in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Source bottlenecks and gaps from the phase walkthrough above. Reference phase and state.]

BOTTLENECK B-01: [Phase: State or transition]
  Cause: [Why delays accumulate -- specific to this process type]
  Downstream impact: [Effect on the next phase or dependent processes]

BOTTLENECK B-02: [Phase: State or transition]
  Cause: [Why delays accumulate]
  Downstream impact: [Effect on the next phase or dependent processes]

[Add B-03 if additional bottlenecks were identified in the phase walkthrough.]

MISSING G-01: [Step Name]
  Phase where it belongs: [Phase name]
  Placement: Between [state name] and [state name]
  Rationale: [Why this step is standard for this process type and is absent from this model]

## EDGE CASES
[3+ cases distinct from exception flows. Must not duplicate any E-ID traced in phase sections.]

EC-01: [Triggering condition]
  Why problematic: [Impact on phase boundaries or data integrity]
  Correct response: [What the correct handling looks like]

EC-02: [Triggering condition]
  Why problematic: [Impact on phase boundaries or data integrity]
  Correct response: [What the correct handling looks like]

EC-03: [Triggering condition]
  Why problematic: [Impact on phase boundaries or data integrity]
  Correct response: [What the correct handling looks like]

## CROSS-PROCESS INTERACTIONS
[Identify where this lifecycle's phase handoffs touch adjacent processes.]
Sending phase/state: [Phase: S-ID]
Receiving process: [Adjacent process name]
Data payload: [Fields or artifact]
Expected acknowledgment: [Response from receiving process]
Sending role: [Role name]
[Add additional rows if multiple inter-process handoffs exist.]
[If none: "No cross-process interactions. All phase handoffs are internal."]

## SLA ANALYSIS
[Attach timing data to 3+ phase-level transitions or states. Cross-reference phases.]

| Phase | State or Transition | SLA Target | Typical Duration | At-Risk? |
|-------|---------------------|------------|------------------|----------|
| [Phase] | [State/transition] | [N hrs/days] | [N hrs/days] | YES / NO |
| [Phase] | [State/transition] | [N hrs/days] | [N hrs/days] | YES / NO |
| [Phase] | [State/transition] | [N hrs/days] | [N hrs/days] | YES / NO |
[AT-RISK rows: add note below the row -- "AT-RISK: [reason] -- cross-ref B-[ID] if a bottleneck was identified."]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, phase_count, state_count, exception_count,
bottleneck_count, gap_count, parallel_phases, terminal_states, cross_process_count, sla_node_count.
```

---

## V-04: State Table + Role Registry First (Axes 1+2)

**Axes:** Output format (V-01 table structure) + Role sequence (V-02 roles-first gate)
**Hypothesis:** The role registry (V-02 axis) establishes a named, validated role set that
all table rows must reference. The state table (V-01 axis) provides a column-per-criterion
structure that prevents silent omission of entry conditions, exits, and role assignments.
Together they create two mutually reinforcing guarantees: the registry ensures domain-specific
role names appear, and the table ensures those role names appear in every state row.
C-03 fails only if a role in the state table does not appear in the registry; that mismatch
is structurally visible. C-01 and C-08 fail only if a table cell is blank; that is equally
visible. Tests whether dual-surface structural enforcement outperforms either axis alone.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers and table columns are fixed. The ROLE REGISTRY must be complete before
the STATE TRANSITIONS table is written. Every Owner cell in the state table must contain
an R-ID from the ROLE REGISTRY -- no generic role names allowed.
Do not reorder, rename, or remove any section header, column header, or template fragment.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [What initiates this lifecycle?]

## ROLE REGISTRY
[Complete before writing STATE TRANSITIONS. Minimum 3 roles. All domain-specific.
Auto-select from process type:
  L2O       -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P       -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor
  CASE      -> Support Agent, Case Manager, Ops Lead, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority |
|------|-----------|--------|--------------------|
| R-01 | [Domain-specific name] | [Domain] | [What this role approves or decides] |
| R-02 | [Domain-specific name] | [Domain] | [What this role approves or decides] |
| R-03 | [Domain-specific name] | [Domain] | [What this role approves or decides] |
[Add R-04, R-05 as needed.]

Registry gate: Confirm each of the following before proceeding to STATE TRANSITIONS:
  [ ] All R-IDs have domain-specific names (no "Approver", "Reviewer", "Manager")
  [ ] All approval gates in this process type have a named role in this registry
  [ ] Minimum 3 roles registered

## TERMINAL STATES
SUCCESS: [Name] -- [Condition]
FAILURE: [Name] -- [Condition]
[CANCEL: [Name] -- [Condition] if applicable]

## STATE TRANSITIONS
[Every state is one row. Owner must be an R-ID from the ROLE REGISTRY above -- not a role name.
Exits format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]". Multiple exits
separated by semicolons. Type: NORMAL / DECISION / FORK / JOIN / TERMINAL.]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-01 | [Name] | [Entry condition -- specific, not generic] | R-[N] | [cond] -> S-02; [cond] -> TERMINAL:[name] | NORMAL |
| S-02 | [Name] | [Entry condition] | R-[N] | [cond] -> S-03; [cond] -> S-04 | DECISION |
[Continue for all states.]
[Terminal state rows -- Owner column: "--":]
| S-T1 | [SUCCESS name] | [Entry condition] | -- | -- | TERMINAL |
| S-T2 | [FAILURE name] | [Entry condition] | -- | -- | TERMINAL |

Decision point supplement: For every DECISION-type row in the table above, write:
  D-[S-ID]: Condition: [rule] | Fallback branch: [condition] -> S-[ID]
[This ensures every decision has an exhaustive outcome set, satisfying C-08 fallback requirement.]

## PARALLEL PATHS
Fork at: S-[ID] ([State Name])
  Branch A (R-[N] owns): S-[ID] -> S-[ID] -> S-[JOIN-ID]
  Branch B (R-[N] owns): S-[ID] -> S-[ID] -> S-[JOIN-ID]
Join at: S-[ID] ([State Name])
  Join type: AND-join / OR-join
  Join condition: [What all branches must deliver before join state is entered]
[If no parallel paths: "No parallel paths. Process is sequential."]

## EXCEPTION FLOWS
[3+ named exception traces. Each references handling role by R-ID. Each reaches a terminal state.]

| E-ID | Exception Name | Trigger: S-ID | Trigger Condition | Trace | Handling: R-ID | Terminal |
|------|---------------|---------------|-------------------|-------|----------------|---------|
| E-01 | [Name] | S-[ID] | [Condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
| E-02 | [Name] | S-[ID] | [Condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
| E-03 | [Name] | S-[ID] | [Condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
[Add rows for additional exceptions.]

## BOTTLENECKS AND GAPS

Bottlenecks (minimum 2):
| B-ID | State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) |
|------|---------------------------|-------|-------------------|--------------|
| B-01 | [State name -- S-ID] | [Specific cause] | [Downstream effect] | R-[N] |
| B-02 | [State name -- S-ID] | [Specific cause] | [Downstream effect] | R-[N] |

Missing steps (minimum 1):
| G-ID | Label | Missing Step | Placement | Rationale | Would-Own (R-ID) |
|------|-------|--------------|-----------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Description] | S-[ID] -> here -> S-[ID] | [Why it belongs] | R-[N] |

## EDGE CASES
[3+ cases, non-overlapping with E-01 through exception table.]
| EC-ID | Triggering Condition | Why Problematic | Correct Response |
|-------|---------------------|-----------------|------------------|
| EC-01 | [Condition] | [Problem] | [Handling] |
| EC-02 | [Condition] | [Problem] | [Handling] |
| EC-03 | [Condition] | [Problem] | [Handling] |

## CROSS-PROCESS INTERACTIONS
| Sending State (S-ID) | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|----------------------|-------------------|--------------|------------------------|--------------|
| S-[ID] | [Process name] | [Data fields] | [Response expected] | R-[N] |
[If none: "No cross-process interactions identified."]

## SLA ANALYSIS
| State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Cross-Ref |
|---------------------------|------------|------------------|----------|-----------|
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: add "AT-RISK NOTE: [specific reason SLA is exceeded in practice]" below the row.]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, state_count, exception_count,
bottleneck_count, gap_count, parallel_paths, terminal_states, cross_process_count,
sla_node_count, at_risk_count.
```

---

## V-05: Full Synthesis (All Three Axes)

**Axes:** State table format (V-01) + Role registry first (V-02) + Phase sections (V-03)
**Hypothesis:** Maximum structural coverage. The role registry establishes the controlled
role vocabulary before any state is traced. Phase sections force explicit phase boundary
declarations (entry trigger, exit condition, handoff). The state transition table inside
each phase section provides column-level enforcement of entry conditions and labeled exits.
No surface where a criterion can be satisfied is left to model discretion: C-01 is enforced
by table columns within each phase section; C-03 is enforced by the registry gate and the
Owner column; C-05 is enforced by terminal state declarations at both process level and
per phase-exit; C-06 is enforced by a pre-printed PARALLEL PATHS section inside each phase;
C-08 is enforced by the decision point supplement block inside each phase. This is the
direct synthesis target for Round 1 and the candidate for golden evaluation.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, table columns, and sub-field labels are fixed.
The ROLE REGISTRY must be complete before any phase section is written.
Every Owner cell in state tables must be an R-ID from the ROLE REGISTRY.
Do not reorder, rename, or remove any section header, column header, or template fragment.
Do not use generic role names (Approver, Reviewer, Manager) anywhere in this output.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any phase section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O       -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P       -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE      -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases |
|------|-----------|--------|--------------------|---------------|
| R-01 | [Domain-specific name] | [Domain] | [Decisions this role makes] | [Phases] |
| R-02 | [Domain-specific name] | [Domain] | [Decisions this role makes] | [Phases] |
| R-03 | [Domain-specific name] | [Domain] | [Decisions this role makes] | [Phases] |
[Add R-04, R-05 as needed.]

Registry gate: Process type [TYPE]. All approval gates and decision points must be owned
by an R-ID from this registry. Violations are flagged in the relevant phase section.

## TERMINAL STATES
[Declared before phase sections. All phase-exit conditions must resolve to one of these.]
SUCCESS: [Name] -- [Condition that ends the lifecycle in the successful state]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- [Condition] -- add if the process type supports cancellation]

## PHASE MAP
[Declare all phases before writing phase detail sections. Every phase here must have a section below.]
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Downstream Handoff for the last phase must reference a TERMINAL state.]

---

[For every phase in the PHASE MAP, write a detail section using the template below.
Phase name must match PHASE MAP exactly.]

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP -- the condition that ends this phase]
Downstream handoff: [Artifact or data passed forward, or TERMINAL:name]

States:
| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for every state in this phase. Terminal states use "--" in Owner and Exits.]

Decision point supplement (one block per DECISION-type state in this phase):
  D-[S-ID] ([State Name]):
    Condition evaluated: [Specific rule or data threshold]
    Owner: R-[N] -- [Role Name]
    Branch YES: [condition] -> S-[ID]
    Branch NO:  [condition] -> S-[ID]
    Fallback:   [condition] -> S-[ID] (required if above branches are not exhaustive)

Parallel work streams in this phase:
  [If concurrent branches exist in this phase:]
  Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
  Join type: AND-join / OR-join
  Join condition: [What all branches must deliver before join fires]
  [If none: "Sequential -- no concurrent branches in this phase."]

Exception traces from this phase:
  E-[ID] [Name]: Trigger: S-[ID] when [condition] -> [Trace: S-ID -> S-ID] -> TERMINAL:[name]
    Handling: R-[N] -- [Role] -- [Action taken]
  [At least one exception trace per phase where realistic. Label "None plausible" only if genuinely inapplicable.]

Phase end: [Condition] -> [Next phase name or TERMINAL:name]

---

[Repeat PHASE section for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Source from phase walkthroughs above. Reference phase and S-ID.]

Bottlenecks (minimum 2):
| B-ID | Phase: State or Transition | Cause | Downstream Impact | Owner (R-ID) |
|------|---------------------------|-------|-------------------|--------------|
| B-01 | [Phase: state/transition] | [Specific cause, not generic] | [Downstream effect] | R-[N] |
| B-02 | [Phase: state/transition] | [Specific cause] | [Downstream effect] | R-[N] |
[Add B-03 if additional bottlenecks were identified.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What this step does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace from phase sections.]
| EC-ID | Triggering Condition | Why Problematic | Correct Response |
|-------|---------------------|-----------------|------------------|
| EC-01 | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-02 | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-03 | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.]
| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment expected] | R-[N] |
[Add rows for additional cross-process handoffs. If none: "No cross-process interactions. Lifecycle is self-contained."]

## SLA ANALYSIS
[3+ nodes annotated. Cross-reference bottlenecks where timing exceeds SLA.]
| Phase | State or Transition | SLA Target | Typical Duration | At-Risk? | Cross-Ref |
|-------|---------------------|------------|------------------|----------|-----------|
| [Phase] | [State/transition -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State/transition -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State/transition -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row -- "AT-RISK NOTE: [why typical exceeds SLA -- reference bottleneck if applicable]"]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## Round 1 Design Notes

### Variation axis selection rationale

Three single-axis variations were selected from the five available axes:
- **Output format** (V-01): Highest leverage for C-01 and C-08 -- table columns make omission
  structurally visible in a way prose cannot.
- **Role sequence** (V-02): Directly targets C-03's most common failure mode (generic role names)
  without changing state representation format. Tests whether role-first ordering alone closes C-03.
- **Lifecycle emphasis** (V-03): Tests whether phase sections carry C-01 and C-05 via boundary
  declarations even without table columns. Also creates natural containers for C-02 exception traces.

Phrasing register and inertia framing were not selected as primary single-axis variations for R1.
Phrasing register affects output quality but not criterion pass/fail structurally. Inertia framing
is a secondary concern for flow-lifecycle (no explicit C-15 equivalent in v1 rubric).

### Criterion structural guarantees by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (entry + exits) | Table columns | State sub-fields | Phase boundary + state blocks | Table columns + sub-fields | Table columns per phase |
| C-02 (3+ exceptions) | Exception table | Exception blocks with R-ID | Exception per phase | Exception table with R-ID | Exception per phase with R-ID |
| C-03 (domain roles) | Role column in table | Registry gate + R-ID ref | Role list in profile | Registry gate + table column | Registry gate + phase owner + table column |
| C-04 (bottlenecks + MISSING) | Pre-printed BOTTLENECKS/MISSING sections | Pre-printed blocks | Pre-printed B-ID/G-ID sections | Pre-printed table + G-ID | Phase-sourced + consolidated table |
| C-05 (terminal states) | TERMINAL STATES declared upfront | TERMINAL STATES declared upfront | TERMINAL STATES + phase exit conditions | Both declarations | All three surfaces |
| C-06 (parallel paths) | Pre-printed section | Pre-printed section | Per-phase parallel section | Pre-printed section | Per-phase parallel section |
| C-07 (edge cases) | Pre-printed 3-row table | Pre-printed 3-block section | Pre-printed 3-block section | Pre-printed 3-row table | Pre-printed 3-row table |
| C-08 (decision explicitness) | Type column + exits format | DECISION state annotation | Decision point supplement block | Type column + supplement | Per-phase supplement |
| C-09 (cross-process) | Pre-printed section | Pre-printed section | Pre-printed section | Pre-printed table | Pre-printed table |
| C-10 (SLA analysis) | Pre-printed 3-row table | Pre-printed 3-row table | Pre-printed phase-tagged table | Pre-printed table + cross-ref | Pre-printed table + cross-ref |

### Predicted differentiation

All five variations are designed to pass all 5 essential criteria. The within-essential
differentiation is on depth and completeness of recommended/aspirational criteria:

| Dimension | Strongest | Why |
|-----------|----------|-----|
| C-03 structural guarantee | V-05 > V-04 > V-02 | Three surfaces (registry + phase owner + table column) |
| C-01 completeness | V-01/V-04/V-05 | Table column makes entry condition per state mandatory |
| C-02 specificity | V-03/V-05 | Phase-contained exceptions are more likely to be process-specific |
| C-08 exhaustiveness | V-05 > V-04 | Per-phase supplement with fallback requirement |
| Output overhead | V-01 < V-05 | V-01 is flat table; V-05 is phased + table + registry |

### V-golden candidate

**V-05** is the direct synthesis target for Round 1:
- Role registry gate prevents C-03 generic-name failure
- Phase sections carry C-01 and C-05 at the boundary level
- Table columns within phase sections carry C-01 at the state level
- Per-phase decision point supplement carries C-08 exhaustively
- All aspirational sections (C-09, C-10) pre-printed with minimum-count enforcement
- Cross-reference columns in SLA table link C-10 findings to C-04 bottlenecks

**V-04** is the closest structural competitor: it closes C-03 and C-01 via two surfaces
(registry + table) without the overhead of phase sections. Key question for live runs:
does V-05's phase-section framing produce meaningfully more process-specific exception
traces (C-02) and edge cases (C-07) compared to V-04's flat table approach?
