Written to `simulations/quest/variations/flow-lifecycle-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — flow-lifecycle

### Axis selection

Three single-axis variations, each isolating one new R3 criterion:

| V | Axis | New criterion targeted | C-15 | C-16 | C-17 |
|---|------|----------------------|------|------|------|
| **V-01** | Output format | C-17 — constructed-answer blocks replace exception + edge-case table rows | FAIL | FAIL | PASS |
| **V-02** | Lifecycle emphasis | C-15 — explicit SECTION A/B labels per phase make exception-first a named first-class structural constraint | PASS | FAIL | FAIL |
| **V-03** | Inertia framing | C-16 — bottleneck entries become per-item answer blocks with mandatory `SLA Nodes Affected:` + `Evidence:` fields | borderline | PASS | FAIL |
| **V-04** | Axes 1+2 combined | C-15 + C-17 — named sections + constructed-answer exceptions | PASS | FAIL | PASS |
| **V-05** | Full synthesis (golden) | C-15 + C-16 + C-17 simultaneously, on V-05 R2 base | PASS | PASS | PASS |

### Key design decisions

**Why "Inertia framing" for C-16:** No listed axis maps cleanly to bidirectional bottleneck-SLA linkage. Inertia framing — making the existing process's cost (bottlenecks + SLA violations) the analytical centrepiece — is the closest fit. The B-NN answer blocks with `SLA Nodes Affected:` and `Evidence:` fields reframe bottlenecks as the primary causal document, not a lookup table.

**C-17 hypothesis carried forward from R2 V-02:** The R2 wildcard was never live-run. V-01, V-04, V-05 all use constructed-answer exception blocks, so R3 gets three chances to test whether answer synthesis improves C-02/C-07 content quality over cell-fill.

**V-05 golden candidate:** Adds three targeted substitutions to V-05 R2 — (1) SECTION A/B labels per phase, (2) B-NN answer blocks, (3) exception/edge-case answer blocks — without disturbing any of the 14 existing structural mechanisms. Predicted score: 100/100 on v3 rubric.

**Predicted score spread** against v3 rubric: V-01/V-02/V-03 ≈ 97.8, V-04 ≈ 98.9, V-05 = 100. Discrimination lives in whether C-15/C-16/C-17 pass or fail in each variation.
does explicit section naming alone enforce structural priority without changing exception format?). V-03 tests C-16 in isolation (does elevating the bottleneck-SLA chain to a primary analytical frame improve bidirectional coverage without complicating other sections?).

**Discrimination:** All five variations are designed to pass C-01 through C-14. The new discrimination cluster is C-15/C-16/C-17. V-01 passes only C-17. V-02 passes only C-15. V-03 passes only C-16. V-04 passes C-15 + C-17. V-05 passes all three plus carries the full V-05 R2 structural base.

**V-05 golden candidate:** Builds on V-05 R2 (exception-first ordering + registry gate + per-phase decision supplement blocks + bidirectional SLA-bottleneck). R3 additions: (1) SECTION A/B labels make C-15 pass via explicit naming, not just ordering; (2) bottleneck entries use answer blocks with `SLA Nodes Affected:` labeled field, closing C-16; (3) exception flows and edge cases are replaced with constructed-answer blocks, closing C-17. The base bidirectional check block from R2 V-05 is retained and reinforced by the new B-NN sub-field structure.

---

## V-01: Output Format -- Constructed-Answer Blocks for Exceptions and Edge Cases

**Axis:** Output format -- replace exception flows and edge cases table rows with per-item
constructed-answer blocks using labeled sub-fields. All other structure from V-05 R2 is preserved:
registry gate, flat state table (not per-phase), decision supplement catalog, bidirectional SLA check
is absent (no phase sections, so B-NN carries no SLA Node column), exception flows remain post-table.
**Hypothesis:** Constructed-answer blocks make incomplete exception entries structurally visible as
unanswered labeled fields, not sparse cells. A blank `Trigger:` sub-field in an answer block is
qualitatively different from an empty table cell -- the label declares what is missing. This tests
whether C-17's format requirement can be satisfied without the phase-section architecture of V-03/V-05
R2. The cost: C-15 fails (answer blocks are post-table, not structurally first per phase) and C-16
fails (no `SLA Node Affected` in bottleneck table). Expected to score 100 on C-01 through C-14 and
pass C-17 but fail C-15 and C-16.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before the STATE TRANSITIONS table.
Every Owner cell must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Every DECISION-type state must have a DECISION SUPPLEMENT BLOCK in the DECISION SUPPLEMENT CATALOG.
Exception flows and edge cases must be written as per-item answer blocks, not table rows.
Every blank sub-field in an exception or edge-case answer block is a visible incomplete answer.
Do not reorder, rename, or remove any section header, column header, or answer block field.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before STATE TRANSITIONS. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Anti-Generic Check |
|------|-----------|--------|--------------------|--------------------|
| R-01 | [Name] | [Domain] | [What this role decides] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [What this role decides] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [What this role decides] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing STATE TRANSITIONS.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## STATE TRANSITIONS
[Every state is one row. Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or
"[condition] -> TERMINAL:[name]". Semicolons between exits.
Type: NORMAL / DECISION / FORK / JOIN / TERMINAL.
DECISION-type states have supplement blocks in the DECISION SUPPLEMENT CATALOG below.]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-01 | [Name] | [Entry condition] | R-[N] | [cond] -> S-02; [cond] -> TERMINAL:[name] | NORMAL |
| S-02 | [Name] | [Entry condition] | R-[N] | [cond] -> S-03; [cond] -> S-04 | DECISION |
[Continue for all states.]
| S-T1 | [SUCCESS name] | [Entry condition] | -- | -- | TERMINAL |
| S-T2 | [FAILURE name] | [Entry condition] | -- | -- | TERMINAL |

## DECISION SUPPLEMENT CATALOG
[One block per DECISION-type state. D-ID matches the S-ID. Fallback: (required) must be filled.]

D-[S-ID] -- [State Name]:
  Condition evaluated: [Exact rule -- not "if approved" but the specific threshold or test]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

[Repeat for every DECISION-type state. Catalog must be complete before EXCEPTION FLOWS.]

## PARALLEL PATHS
Fork at: S-[ID] ([State Name])
  Branch A (R-[N] owns): S-[ID] -> ... -> S-[JOIN]
  Branch B (R-[N] owns): S-[ID] -> ... -> S-[JOIN]
Join at: S-[ID] ([State Name])
  Join type: AND-join / OR-join
  Join condition: [What all branches must deliver]
[If none: "No parallel paths. Process is fully sequential. Rationale: [why]"]

## EXCEPTION FLOWS
[3+ named exception flows. Each must be specific to this process type -- no generic system errors.
Write each as a per-item answer block with all labeled sub-fields filled.
A blank sub-field is a visible incomplete answer -- do not leave any sub-field empty.]

E-01 -- [Exception Name]:
  Phase origin: [The state or process area where this exception originates -- cite S-ID]
  Trigger: [Specific condition that causes this exception -- process-specific, not generic]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

E-02 -- [Exception Name]:
  Phase origin: [S-ID and state name]
  Trigger: [Specific condition]
  Trace: S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

E-03 -- [Exception Name]:
  Phase origin: [S-ID and state name]
  Trigger: [Specific condition]
  Trace: S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add E-04 onward as needed. Every E-block must have all five sub-fields answered.]

## BOTTLENECKS AND GAPS
Bottlenecks (minimum 2):
| B-ID | State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) |
|------|---------------------------|-------|-------------------|--------------|
| B-01 | [State name -- S-ID] | [Specific cause] | [Effect on downstream] | R-[N] |
| B-02 | [State name -- S-ID] | [Specific cause] | [Effect on downstream] | R-[N] |

Missing steps (minimum 1):
| G-ID | Label | Missing Step Description | Placement | Rationale | Would-Own (R-ID) |
|------|-------|--------------------------|-----------|-----------|-----------------|
| G-01 | MISSING: [Name] | [What this step does] | S-[ID] -> here -> S-[ID] | [Why standard for this process] | R-[N] |

## EDGE CASES
[3+ cases distinct from all E-IDs above.
Write each as a per-item answer block with all labeled sub-fields filled.
A blank sub-field is a visible incomplete answer -- do not leave any sub-field empty.]

EC-01 -- [Edge Case Name]:
  Trigger: [Condition that surfaces this case -- distinct from every E-ID trigger]
  Why problematic: [Why the current model cannot handle this correctly]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Trigger: [Condition -- distinct from every E-ID trigger]
  Why problematic: [Explanation]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Trigger: [Condition -- distinct from every E-ID trigger]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. Every EC-block must have all three sub-fields answered.]

## CROSS-PROCESS INTERACTIONS
| Sending State (S-ID) | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-------------------|--------------|------------------------|----------------------|
| S-[ID] | [Process name] | [Data fields] | [Response] | R-[N] |
[If none: "No cross-process interactions. Self-contained. Rationale: [explain]"]

## SLA ANALYSIS
| State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|---------------------------|------------|------------------|----------|---------------------|
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append: "AT-RISK NOTE: [reason typical exceeds SLA] -- causal source: B-[ID]"]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, state_count, decision_count,
exception_count, edge_case_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-02: Lifecycle Emphasis -- Named SECTION A/B Per-Phase Exception-First Ordering

**Axis:** Lifecycle emphasis -- enforce structural position of exception sections by naming them
as numbered sub-sections (SECTION A -- EXCEPTIONS, SECTION B -- STATES) within each phase block.
The section labels are not just ordering hints; they are declared output elements with their own
headers that precede the state table. Each phase is organized as a labeled two-section unit;
exceptions are always the first declared section. Exception content remains in table format. The
rest of the structure follows V-03 R2: registry gate, per-phase decision supplement blocks,
per-phase SLA, bidirectional SLA note (but no SLA Node Affected column in B-NN table).
**Hypothesis:** Explicit section naming ("SECTION A -- EXCEPTIONS IN THIS PHASE") communicates
structural primacy more clearly than ordering-instruction prose. A model following the template
cannot write SECTION B before SECTION A without violating a labeled section header sequence. The
cost: exception content stays in table cells (C-17 fails), and B-NN entries do not declare SLA
Node Affected (C-16 fails). Expected to pass C-01 through C-14 and C-15, but fail C-16 and C-17.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and field labels are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
Do not reorder, rename, or remove any section header or sub-section label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: always write SECTION A before SECTION B.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always first in every phase block.
Write failure modes specific to the work done in this phase before any state detail is visible.
Generic exceptions (system error, network timeout) that could appear in any phase are not acceptable.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

| E-ID | Exception Name | Trigger State (S-ID) | Trigger Condition | Trace | Handling (R-ID) | Terminal |
|------|---------------|---------------------|-------------------|-------|-----------------|---------|
| E-[N] | [Name] | S-[ID]: [state name in this phase] | [Phase-specific condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
[Add rows for additional exceptions specific to this phase.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state above.
Write "No DECISION-type states in this phase." if none. Fallback: (required) must be filled.]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or threshold -- process and phase specific]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS
Bottlenecks (minimum 2):
| B-ID | Phase: State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) |
|------|-----------------------------------|-------|-------------------|--------------|
| B-01 | [Phase: state] | [Specific cause] | [Downstream effect] | R-[N] |
| B-02 | [Phase: state] | [Specific cause] | [Downstream effect] | R-[N] |

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any E-ID from any phase above. Cite originating phase.]
| EC-ID | Phase | Triggering Condition | Why Problematic | Correct Response |
|-------|-------|---------------------|-----------------|------------------|
| EC-01 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-02 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-03 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |

## CROSS-PROCESS INTERACTIONS
| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process] | [Data] | [Acknowledgment] | R-[N] |
[If none: "No cross-process interactions. Self-contained. Rationale: [explain]"]

## SLA ANALYSIS
| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append: "AT-RISK NOTE: [reason] -- causal source: B-[ID]"]

Bidirectional check note: for each AT-RISK row, confirm the cited B-ID exists in BOTTLENECKS.
For each B-ID in BOTTLENECKS, confirm at least one AT-RISK row in SLA ANALYSIS cites it.

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-03: Inertia Framing -- Bottleneck-SLA Chain as Analytical Centrepiece (C-16)

**Axis:** Inertia framing -- the existing process's failure modes and SLA violations are the
analytical centrepiece. Bottleneck entries use per-item answer blocks (not table rows) with a
mandatory `SLA Nodes Affected:` labeled field and a mandatory `Evidence:` field that names the
SLA ANALYSIS rows that cite this bottleneck. The SLA table retains the `Bottleneck Cross-Ref`
column from V-05 R2. A post-table bidirectional check block closes the chain explicitly.
The rest of the structure is V-03 R2: per-phase sections, exception-first ordering within phases
(structural, not named sections), registry gate. Exception and edge-case content remain in tables.
**Hypothesis:** Elevating the bottleneck-SLA chain to a primary analytical construct -- making
each bottleneck an answer block with a required `SLA Nodes Affected:` field -- closes C-16 more
reliably than adding a column to a table, because a blank answer field is structurally visible
as unanswered, while an empty table cell can be overlooked. The cost: exception sections are
still tables (C-17 fails); SECTION A/B naming is absent (C-15 borderline -- ordering is structural
but not named). Expected to pass C-01 through C-14 and C-16, borderline on C-15, fail C-17.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, table columns, and answer block sub-fields are fixed.
ORDERING RULE: within each phase section, Exception Traces appear BEFORE States.
The ROLE REGISTRY must be complete before any phase section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Bottleneck entries are answer blocks, not table rows. Every bottleneck must name its SLA Nodes Affected.
Every AT-RISK SLA row must cite a B-ID; every B-ID must have a matching SLA entry (bidirectional chain).
Do not reorder, rename, or remove any section header, column header, or answer block field.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any phase section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one phase section for every phase in the PHASE MAP.
ORDERING WITHIN EACH PHASE: Exception Traces -> States -> Decision Supplement Blocks -> Parallel Paths.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### Exception Traces for This Phase
[Write BEFORE the States table. Phase context scopes failure modes.
Generic exceptions (system error, network timeout) are not acceptable.
Write "No plausible exceptions -- rationale: [explain]" only if genuinely inapplicable.]

| E-ID | Exception Name | Trigger State (S-ID) | Trigger Condition | Trace | Handling (R-ID) | Terminal |
|------|---------------|---------------------|-------------------|-------|-----------------|---------|
| E-[N] | [Name] | S-[ID]: [state name] | [Phase-specific condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |

### States
| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |

### Decision Supplement Blocks
[One block per DECISION-type state. Fallback: (required) must be filled.]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule -- process and phase specific]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch fires] -> S-[ID]: [destination]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [states] | Branch B (R-[N]): [states] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE section for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottlenecks are written as per-item answer blocks.
Each block has a mandatory `SLA Nodes Affected:` field naming the state(s) in SLA ANALYSIS
that this bottleneck causes to go AT-RISK.
The `SLA Nodes Affected:` answer must reference states that appear in the SLA ANALYSIS section below.
A blank `SLA Nodes Affected:` field is a visible incomplete answer -- do not leave it empty.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition (S-ID): [Phase name: state name -- S-ID]
  Cause: [Specific cause -- not "slow approvals" but the operational reason]
  Downstream impact: [Effect on states or timeline downstream of this bottleneck]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) whose SLA entry in SLA ANALYSIS will show AT-RISK due to this bottleneck]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition (S-ID): [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]

[Add B-03 onward as needed. Every B-block must have all five fields answered.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any E-ID from any phase above. Cite originating phase.]
| EC-ID | Phase | Triggering Condition | Why Problematic | Correct Response |
|-------|-------|---------------------|-----------------|------------------|
| EC-01 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-02 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-03 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |

## CROSS-PROCESS INTERACTIONS
| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process] | [Data] | [Acknowledgment] | R-[N] |
[If none: "No cross-process interactions. Self-contained. Rationale: [explain]"]

## SLA ANALYSIS
[3+ nodes. Every AT-RISK row must cite a B-ID. Every B-ID's SLA Nodes Affected must appear here.
The bidirectional chain is closed when: every AT-RISK row has a B-ID AND every B-ID names a
state that appears in this table as AT-RISK.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append: "AT-RISK NOTE: [reason] -- causal source: B-[ID]"]

Bidirectional evidence check:
  Forward (SLA -> B): Every AT-RISK row cites a B-ID? [YES: all closed | NO: add missing B-IDs]
  Backward (B -> SLA): Every B-ID's SLA Nodes Affected appears in this table as AT-RISK?
                        [YES: chain closed | NO: add SLA row or update B-block SLA Nodes Affected]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-04: Axes 1+2 -- Named Exception-First Sections + Constructed-Answer Exception Blocks

**Axes:** Lifecycle emphasis (named SECTION A/B ordering) + Output format (constructed-answer
blocks for exceptions and edge cases). Combines V-02's explicit section labeling with V-01's
constructed-answer format for exception and edge-case content. The bottleneck section retains
table rows (no B-NN SLA Node Affected field), so C-16 is one-directional only.
**Hypothesis:** Structural section naming (C-15) and constructed-answer exception blocks (C-17)
are additive: the former encodes phase-scoped generation as architecture, the latter makes every
incomplete exception entry visible as an unanswered labeled sub-field. Together they address the
two most actionable R3 gaps -- structural position and content completeness -- without requiring
the bidirectional bottleneck restructuring of V-03. Expected to pass C-01 through C-14, C-15,
C-17, but fail C-16 (no `SLA Node Affected` in B-NN entries, one-directional chain only).

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Every blank sub-field in an exception or edge-case answer block is a visible incomplete answer.
Do not reorder, rename, or remove any section header, sub-section label, or answer block field.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always first in every phase block.
Write failure modes specific to this phase before any state detail.
Generic exceptions (system error, network timeout) are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state declared in SECTION B of this phase]
  Trigger: [Phase-specific condition -- not generic]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state above.
Write "No DECISION-type states in this phase." if none. Fallback: (required) must be filled.]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule -- process and phase specific]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch fires] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [states] | Branch B (R-[N]): [states] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS
Bottlenecks (minimum 2):
| B-ID | Phase: State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) |
|------|-----------------------------------|-------|-------------------|--------------|
| B-01 | [Phase: state] | [Specific cause] | [Downstream effect] | R-[N] |
| B-02 | [Phase: state] | [Specific cause] | [Downstream effect] | R-[N] |

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- distinct from all E-IDs in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly]
  Correct response: [What correct handling looks like]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process] | [Data] | [Acknowledgment] | R-[N] |
[If none: "No cross-process interactions. Self-contained. Rationale: [explain]"]

## SLA ANALYSIS
| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append: "AT-RISK NOTE: [reason] -- causal source: B-[ID]"]

Bidirectional note: for each AT-RISK row, confirm B-ID exists in BOTTLENECKS. For each B-ID in
BOTTLENECKS, confirm at least one AT-RISK row cites it. Correct any orphan entries.

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-05: Full Synthesis -- Named Sections + B-NN Answer Blocks + Constructed-Answer Exceptions

**Axes:** All three: Lifecycle emphasis (SECTION A/B named ordering, C-15) + Inertia framing
(B-NN answer blocks with SLA Nodes Affected, C-16) + Output format (constructed-answer blocks for
exceptions and edge cases, C-17). Full structural base from V-05 R2: registry gate with Anti-Generic
Check column, per-phase decision supplement blocks with Fallback: (required) label, per-phase
parallel paths, cross-process interaction table, bidirectional SLA check block.
**Hypothesis:** All three R3 criteria can be satisfied simultaneously without structural conflict:
SECTION A/B labeling (C-15) and constructed-answer exception blocks (C-17) are co-located per phase;
B-NN answer blocks (C-16) are in the post-phase BOTTLENECKS section. The full V-05 R2 structure
is preserved; R3 adds three targeted substitutions: (1) phase section labels for exception/state
ordering, (2) bottleneck entry format change from table to answer blocks, (3) exception/edge-case
format change from table to answer blocks. Golden candidate for Round 3.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with a mandatory SLA Nodes Affected: field.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
Do not reorder, rename, or remove any section header, sub-section label, column header, or field label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in SECTION B of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in SECTION B.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) is a required field -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- process and phase specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottleneck entries are per-item answer blocks.
The SLA Nodes Affected: field is required -- it names the state(s) in SLA ANALYSIS that this
bottleneck causes to go AT-RISK. The state names must appear in the SLA ANALYSIS section below.
A blank SLA Nodes Affected: field is a visible incomplete answer -- do not leave it empty.
The Evidence: field names the SLA ANALYSIS AT-RISK rows that cite this B-ID, closing the
reverse direction of the bidirectional chain.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [AT-RISK entries that list "causal source: B-01" in SLA ANALYSIS]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [AT-RISK entries that cite this B-ID]

[Add B-03 onward as needed. All six fields required per block.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace (E-ID) from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- must be distinct from every E-ID trigger in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly -- specific to this process]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation -- specific to this process]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. Bidirectional chain rules:
  Forward (SLA -> B): every AT-RISK row must cite a B-ID from BOTTLENECKS.
  Backward (B -> SLA): every B-ID's SLA Nodes Affected field must name a state appearing here as AT-RISK.
  No orphan at-risk entries (AT-RISK without a B-ID).
  No orphan bottleneck IDs (B-ID without an AT-RISK SLA row citing it).]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

Bidirectional evidence check:
  Forward (SLA -> B):  Every AT-RISK row cites a B-ID? [YES: closed | NO: list uncited AT-RISK rows]
  Backward (B -> SLA): Every B-ID's SLA Nodes Affected appears here as AT-RISK?
                        [YES: chain closed | NO: list B-IDs without matching AT-RISK rows]
  Chain status: CLOSED (all forward + backward links verified) / OPEN (list unresolved links)

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## Round 3 Design Notes

### Variation axis selection rationale

Three single-axis variations, each targeting one new R3 criterion in isolation:
- **Output format -- C-17 first** (V-01): Replace exception flows and edge-case table rows with
  per-item constructed-answer blocks. Flat state table structure preserved from V-01 R2 (no phase
  sections). Tests whether C-17 can be satisfied without phase-section architecture. Exception
  sections remain post-table (C-15 fails) and B-NN table has no SLA Node column (C-16 fails).
- **Lifecycle emphasis -- C-15 first** (V-02): Named SECTION A/B labels per phase make exception-first
  ordering a first-class structural constraint, not just an ordering instruction. Builds on V-03 R2
  phase-section structure. Exception content stays in tables (C-17 fails), B-NN table unchanged
  (C-16 fails). Tests whether section naming alone is sufficient for C-15 without answer blocks.
- **Inertia framing -- C-16 first** (V-03): Bottleneck entries become per-item answer blocks with
  a mandatory `SLA Nodes Affected:` field plus an `Evidence:` field. Builds on V-03 R2 exception-first
  ordering (C-15 borderline -- structural but unnamed sections). Exception content stays in tables
  (C-17 fails). Tests whether B-NN answer blocks close C-16 independently of exception format.

Two combined variations:
- **Axes 1+2** (V-04): Named SECTION A/B ordering (C-15) + constructed-answer exception blocks (C-17).
  B-NN table unchanged (C-16 one-directional, fails). Tests whether the two format/structure axes
  together produce the expected additive improvement.
- **Full synthesis** (V-05): All three new criteria targeted simultaneously, on the V-05 R2 baseline.
  Golden candidate for Round 3.

Inertia framing is mapped to the bottleneck-SLA chain prominence because the "status quo process" is
best expressed through its bottlenecks and SLA violations -- the analytical framing that shows what
the current process costs. No rubric criterion directly rewards process-contrast framing of alternatives.

Role sequence was not selected: no R3 criterion is discriminated by role ordering.

### Predicted R3 scores against v3 rubric

| Variation | C-01..C-14 | C-15 | C-16 | C-17 | Asp pass | Score |
|-----------|-----------|------|------|------|---------|-------|
| V-01 | All PASS | FAIL | FAIL | PASS | 7/9 | 60+30+(7/9*10) ~97.8 |
| V-02 | All PASS | PASS | FAIL | FAIL | 7/9 | 60+30+(7/9*10) ~97.8 |
| V-03 | All PASS | borderline | PASS | FAIL | 7/9 (C-15 borderline) | ~97.8 |
| V-04 | All PASS | PASS | FAIL | PASS | 8/9 | 60+30+(8/9*10) ~98.9 |
| V-05 | All PASS | PASS | PASS | PASS | 9/9 | 60+30+10 = **100** |

C-15 note on V-03: exception-first ordering is structural (within-phase ordering rule preserved from
R2 V-03) but the sections are unnamed (no SECTION A/B labels). The pass condition requires exceptions
as "first-class output elements" before state tables per phase. Structural ordering satisfies the
spirit; the absence of explicit section labels leaves ambiguity about whether an unlabeled exception
table that precedes a state table counts as a "first-class output element." Scored as borderline:
likely pass in practice, but structurally weaker than V-02/V-04/V-05.

C-16 note on V-04: bidirectional note in SLA ANALYSIS is present (from V-05 R2 inheritance) but the
B-NN entries do not declare `SLA Nodes Affected:`. The C-16 pass condition specifically requires B-NN
entries to include SLA node references. One-directional chain only.

### Excellence signals to watch in live runs

1. **C-17 content quality hypothesis (from R2 V-02 wildcard):** Does constructed-answer format for
   exception blocks (V-01, V-04, V-05) produce more operationally specific C-02/C-07 content than
   table rows? This was the unresolved R2 wildcard -- R3 tests it across three variations.
2. **C-15 naming vs ordering:** Does explicit SECTION A/B labeling (V-02, V-04, V-05) produce
   stronger structural compliance than unnamed exception-first ordering (V-03)? The question is
   whether a section label changes generation behavior beyond what ordering-rule prose already achieves.
3. **C-16 answer block vs column:** Does the B-NN `SLA Nodes Affected:` answer block (V-03, V-05)
   close the backward chain more reliably than V-05 R2's `SLA Node Affected` table column? The
   hypothesis is that a blank answer sub-field is more visible than an empty table cell.
4. **V-05 synthesis cost:** Does adding three structural changes simultaneously introduce any
   generation-time conflict? Specifically: does the SECTION A answer-block format for exceptions
   conflict with the structured Phase map ordering when the model must match E-IDs from SECTION A
   to state S-IDs that are only visible in SECTION B (written after)?
