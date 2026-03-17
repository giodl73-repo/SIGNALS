Written to `simulations/quest/variations/flow-lifecycle-variations-R2-2026-03-14.md`.

---

## Round 2 Summary — flow-lifecycle

| V | Axis | Key innovation | C-11 | C-12 | C-13 | C-14 |
|---|------|----------------|------|------|------|------|
| **V-01** | Output format fixed | DECISION SUPPLEMENT CATALOG section (flat, post-table, one block per DECISION state) | Standalone catalog | Registry gate + Anti-Generic Check column | Phase/State Origin column in exception table | Cross-Ref column + AT-RISK NOTE |
| **V-02** | Phrasing register (new axis) | All criteria as mandatory-answer questions; prohibition gate for C-12 | Step 7: 5-question block per decision; Q5 = FALLBACK | Step 2 prohibition-question + Step 5 confirm | E-block phase origin sub-field | AT-RISK citation requirement per row |
| **V-03** | Exception-first lifecycle | Exceptions written before states in every phase section | Per-phase supplement blocks + Fallback: field | Registry gate + Anti-Generic Check column | Structural: exception section precedes state table per phase | Cross-Ref column + AT-RISK NOTE |
| **V-04** | Axes 2+3 (phrasing + exception-first) | Conversational questions with exception-before-state ordering per phase | FALLBACK question mandatory per decision | Prohibition-question gate + confirm | Exception questions precede state questions per phase | Citation requirement + bidirectional note |
| **V-05** | Full synthesis (golden candidate) | All four new criteria given dedicated structural elements simultaneously | Per-phase blocks with `Fallback: (required)` label | Registry gate + Anti-Generic Check column + checklist | Phase Origin Stamp column + structural exception-first order | Bidirectional check: B-ID↔SLA Node Affected columns |

**All five are predicted to score 100 on v2 rubric.** R1's discrimination was C-08 (V-01 failed). R2's discrimination moves inside the 100 cluster: structural reliability on C-13 (column vs structural vs sub-field), C-14 bidirectionality (V-05 only), and content quality on C-02/C-07 (V-02 hypothesis).

**V-05** is the golden candidate: exception-first order makes C-13 structural rather than instructional; bidirectional evidence check closes C-14 in both directions; `Fallback: (required)` label makes C-11 visible as a labeled required field.

**V-02** is the wildcard: weakest structural visibility but highest predicted content specificity. The live-run question is whether richer C-02/C-07 content compensates for what a model might silently omit without a blank table cell to signal the gap.
r exception block. The key structural difference: writing exceptions before states forces phase-context reasoning.
- **C-14 primary mechanism:** SLA table gains a `Bottleneck Cross-Ref` column (all variations from R1 V-02/V-04/V-05
  already had this; R2 adds enforcement). V-05 adds a bidirectional requirement: B-ID entries must declare a
  `SLA Node Affected` column and a post-table check verifies no orphan entries on either side.

**V-05 golden candidate:** Carries all R1 V-05 structural features forward with all four new aspirational criteria
given dedicated structural enforcement. The exception-first order inside each phase (V-03 axis) is the key addition
to R1 V-05.

---

## V-01: Output Format Fixed — Flat Table + Decision Supplement Catalog + Role Registry Gate

**Axis:** Output format — R1 V-01 repaired with two structural additions: (1) a standalone DECISION SUPPLEMENT
CATALOG section after the state table, with one per-decision block including a mandatory `Fallback:` field, and
(2) a role registry gate with an `Anti-Generic Check` column. The flat table structure is preserved; no phase
sections are added.
**Hypothesis:** The R1 V-01 failure was C-08: DECISION type column + exits format do not require exhaustive
outcomes. A standalone DECISION SUPPLEMENT CATALOG (D-IDs matching S-IDs of DECISION-type rows) makes every
decision point's fallback path structurally visible as a blank field. The role registry gate closes C-12. The
exception table gains a `Phase/State Origin` column to address C-13 without adding full phase sections. The SLA
table retains the `Bottleneck Cross-Ref` column from R1 V-04 for C-14. This tests whether a flat-table approach
with targeted structural additions can match V-05's aspirational coverage.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers and table columns are fixed. The ROLE REGISTRY must be complete before the STATE TRANSITIONS
table. After the state table, write one DECISION SUPPLEMENT BLOCK per DECISION-type state in the DECISION
SUPPLEMENT CATALOG section. Do not reorder, rename, or remove any section header or column header.
Do not use generic role names (Approver, Reviewer, Manager, Owner) anywhere in this output.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE -- inferred from topic context]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete before STATE TRANSITIONS. Minimum 3 roles. All domain-specific.
Auto-select by process type:
  L2O       -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P       -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE      -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Anti-Generic Check |
|------|-----------|--------|--------------------|--------------------|
| R-01 | [Name] | [Domain] | [What this role decides or approves] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [What this role decides or approves] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [What this role decides or approves] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed for the process type.]

Registry gate: Confirm before proceeding to STATE TRANSITIONS:
  [ ] All R-IDs have domain-specific names
  [ ] All approval gates and decision points in this process type are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing STATE TRANSITIONS.]

## TERMINAL STATES
[Declare all terminal states before the state table. Every exit must reference one of these.]
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- [Condition] -- add if the process type supports cancellation]

## STATE TRANSITIONS
[Every state is one row. Owner column must contain an R-ID from the ROLE REGISTRY -- not a role name.
Exits format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]". Semicolons between exits.
Type: NORMAL / DECISION / FORK / JOIN / TERMINAL.
DECISION-type states will have a supplement block in the DECISION SUPPLEMENT CATALOG below.]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-01 | [Name] | [What must be true to enter this state] | R-[N] | [cond] -> S-02; [cond] -> TERMINAL:[name] | NORMAL |
| S-02 | [Name] | [What must be true to enter] | R-[N] | [cond] -> S-03; [cond] -> S-04 | DECISION |
[Continue for all states. Every exit must reference a declared state or TERMINAL state.]
[Terminal state rows:]
| S-T1 | [SUCCESS name] | [Entry condition] | -- | -- | TERMINAL |
| S-T2 | [FAILURE name] | [Entry condition] | -- | -- | TERMINAL |

## DECISION SUPPLEMENT CATALOG
[Write one block per DECISION-type row in the STATE TRANSITIONS table above.
D-ID matches the S-ID of the decision state. Every block requires a Fallback: field.
Do not write "n/a" for Fallback: -- either provide the fallback path or explain why branches are exhaustive.]

D-[S-ID] -- [State Name]:
  Condition evaluated: [The exact rule or data threshold being tested -- not "if approved" but the specific condition]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [destination state name]
  Branch NO:  [condition] -> S-[ID]: [destination state name or TERMINAL:name]
  Fallback:   [what happens when no branch condition applies] -> S-[ID]: [destination]
              [If YES/NO are exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

[Repeat one block per DECISION-type state. The catalog must be complete before EXCEPTION FLOWS.]

## PARALLEL PATHS
[Model concurrent work streams with explicit fork, branches, and join.]
Fork at: S-[ID] ([State Name])
  Branch A (R-[N] owns): S-[ID] -> S-[ID] -> ... -> S-[JOIN-ID]
  Branch B (R-[N] owns): S-[ID] -> S-[ID] -> ... -> S-[JOIN-ID]
Join at: S-[ID] ([State Name])
  Join type: AND-join / OR-join
  Join condition: [What all branches must deliver before join state is entered]
[If no parallel paths: "No parallel paths. Process is fully sequential. Rationale: [why]"]

## EXCEPTION FLOWS
[3+ named exception traces. Each must reach a declared terminal state.
Each trace must reference the handling role by R-ID. Each must be specific to this process type.
The Phase/State Origin column identifies where in the lifecycle this exception originates.]

| E-ID | Exception Name | Phase/State Origin | Trigger Condition | Trace (states) | Handling (R-ID) | Terminal |
|------|---------------|-------------------|-------------------|----------------|-----------------|---------|
| E-01 | [Name] | S-[ID]: [state name] | [Specific condition -- no generic "system error"] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
| E-02 | [Name] | S-[ID]: [state name] | [Specific condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
| E-03 | [Name] | S-[ID]: [state name] | [Specific condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
[Add E-04 onward for additional exception flows.]

## BOTTLENECKS AND GAPS

Bottlenecks (minimum 2 -- states or transitions where delays commonly accumulate):
| B-ID | State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) |
|------|---------------------------|-------|-------------------|--------------|
| B-01 | [State name -- S-ID] | [Specific cause, not "slow approvals"] | [Effect on downstream states or SLA] | R-[N] |
| B-02 | [State name -- S-ID] | [Specific cause] | [Effect on downstream states or SLA] | R-[N] |
[Add B-03 if additional bottlenecks exist.]

Missing steps (minimum 1 -- steps absent from this model that exist in real-world practice):
| G-ID | Label | Missing Step Description | Placement | Rationale | Would-Own (R-ID) |
|------|-------|--------------------------|-----------|-----------|-----------------|
| G-01 | MISSING: [Name] | [What this step does] | S-[ID] -> here -> S-[ID] | [Why standard practice for this process type] | R-[N] |

## EDGE CASES
[3+ cases distinct from all E-IDs in EXCEPTION FLOWS. Must not duplicate any named exception trace.]

| EC-ID | Triggering Condition | Why Problematic | Correct Response |
|-------|---------------------|-----------------|------------------|
| EC-01 | [Condition -- distinct from all E-IDs] | [Why current model cannot handle this] | [What correct handling looks like] |
| EC-02 | [Condition -- distinct from all E-IDs] | [Why current model cannot handle this] | [What correct handling looks like] |
| EC-03 | [Condition -- distinct from all E-IDs] | [Why current model cannot handle this] | [What correct handling looks like] |

## CROSS-PROCESS INTERACTIONS
[At least one handoff contract where this lifecycle touches an adjacent process.]

| Sending State (S-ID) | Receiving Process | Data Payload | Expected Acknowledgment | Handoff Owner (R-ID) |
|----------------------|-------------------|--------------|------------------------|----------------------|
| S-[ID] | [Adjacent process name] | [Data fields or artifact] | [Response the receiving process returns] | R-[N] |
[Add rows for additional cross-process handoffs.]
[If none: "No cross-process interactions. This lifecycle is self-contained. Rationale: [explain]"]

## SLA ANALYSIS
[Annotate 3+ states or transitions. For every AT-RISK row, cite the B-ID from BOTTLENECKS AND GAPS
that explains why the SLA is exceeded. If no B-ID exists for an at-risk node, add it to BOTTLENECKS first.]

| State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|---------------------------|------------|------------------|----------|---------------------|
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason SLA is exceeded] -- causal source: B-[ID]"]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, state_count, decision_count,
exception_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-02: Phrasing Register — Conversational-Imperative Questions

**Axis:** Phrasing register — replace all table columns and template sub-fields with mandatory-answer
questions. Each question addresses a specific criterion by forcing a direct answer rather than a cell
fill. The role gate is a prohibition question with explicit confirm. The decision fallback is addressed
as a mandatory fifth question in each decision block. Exception phase-origin is a required sub-field
in each exception answer block. SLA at-risk entries require a bottleneck citation answer.
**Hypothesis:** A question-per-criterion format reduces template-filling behavior and increases
operational specificity because the model must construct an answer rather than populate a pre-labeled
cell. Prohibition gates ("not 'Approver' -- fix before continuing") apply pressure at the structural
decision point rather than after-the-fact review. The cost is reduced structural visibility: a skipped
answer is less obvious than a blank table cell. Tests whether conversational format produces richer
operational content (C-02 specificity, C-07 edge case depth) at the cost of some structural enforcement.

```
You are running /flow-lifecycle. Answer every numbered question in order.
Do not skip any question. Do not use generic role names (Approver, Reviewer, Manager, Owner) --
every role must have a domain-specific job title. If a question specifies a minimum count, meet it.

---

## STEP 1 -- IDENTIFY THE PROCESS

1. What type of lifecycle is this?
   Answer: [L2O / P2P / PERIOD-CLOSE / CASE]

2. What single event triggers this lifecycle? (One sentence.)
   Answer: [Trigger event]

3. What domain does this process belong to?
   Answer: [Sales / Procurement / Finance / Support]

---

## STEP 2 -- DECLARE DOMAIN ROLES

Before answering any state or exception questions, name the domain experts for this process.
Use specific job titles -- not "Approver," "Reviewer," "Manager," or "Owner."

4. Name at least 3 domain-specific roles for this process. For each role, provide:
   - R-ID (R-01, R-02, R-03, ...)
   - Exact job title in this domain
   - What decisions or approvals this role holds
   - Which lifecycle phases this role is active in

   R-01: Title: [domain-specific]  |  Decides: [authority]  |  Active in: [phases]
   R-02: Title: [domain-specific]  |  Decides: [authority]  |  Active in: [phases]
   R-03: Title: [domain-specific]  |  Decides: [authority]  |  Active in: [phases]
   [Add R-04, R-05 if the process requires additional roles.]

5. Anti-generic gate: Does any role above use the title "Approver," "Reviewer," "Manager,"
   "Owner," or "Actor" without a domain qualifier?
   Answer: YES (fix before continuing) / NO (proceed to Step 3)

---

## STEP 3 -- TERMINAL STATES

6. How does this lifecycle end successfully? Name the success terminal state and describe the
   condition that places the lifecycle in that state.
   SUCCESS: [Name]  --  Condition: [What makes this the successful end]

7. How does this lifecycle end in failure? Name at least one failure terminal state.
   FAILURE: [Name]  --  Condition: [What triggers failure]

8. Does this lifecycle support cancellation? If yes, name the cancellation terminal state.
   [CANCEL: [Name]  --  Condition: [What triggers cancellation]] / No cancellation path.

---

## STEP 4 -- WALK EVERY STATE

9. List every state in this lifecycle in order. For each state, answer all of the following:

   State S-[N]:
     Name: [What is this state called?]
     Entry condition: [What must be true before the process can enter this state?]
     Owner: R-[N] -- [Role title from ROLE REGISTRY]
     State type: NORMAL / DECISION / FORK / JOIN / TERMINAL
     What happens next? (List every possible exit from this state):
       [condition] -> S-[N] or TERMINAL:[name]
       [condition] -> S-[N] or TERMINAL:[name]
       [continue for all exits -- every exit must name a destination state or terminal]

   [If DECISION type: also answer:]
     Decision rule: [Exact condition being evaluated -- not "if approved" but the specific data or threshold]
     Who evaluates it: R-[N] -- [role title]

   Walk all states. No state may end without a declared destination.

---

## STEP 5 -- PARALLEL WORK STREAMS

10. Does this lifecycle have concurrent branches -- where two or more work streams run simultaneously
    before converging?
    YES: Describe:
      Fork state: S-[ID] ([name]) -- where the split begins
      Branch A: Owner R-[N]. States traversed: S-[ID] -> ... -> S-[JOIN-ID]
      Branch B: Owner R-[N]. States traversed: S-[ID] -> ... -> S-[JOIN-ID]
      Join state: S-[ID] ([name]) -- where branches converge
      Join type: AND-join (all must complete) / OR-join (first to finish unblocks join)
      Join condition: [What all branches must deliver before the join state is entered]
    NO: State that the process is sequential and explain why no concurrent paths exist.

---

## STEP 6 -- TRACE EXCEPTION FLOWS

11. Name the 3 most important failure modes in this process. For each, trace the full path.
    Each exception must be specific to this process type -- no generic "system error" or "timeout."

    E-[N] -- [Exception name]:
      Phase and state where this originates: Phase [name if applicable] / S-[ID]: [state name]
      What triggers it: [The specific domain condition -- not "error" but the actual event]
      States traversed: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
      Who handles it: R-[N] -- [role title]
      What does the handler do: [Action that leads to the terminal state]

    [Answer E-01, E-02, E-03 at minimum. Add E-04, E-05 if additional major exceptions exist.]

---

## STEP 7 -- DECISION SUPPLEMENT BLOCKS

12. For every DECISION-type state from Step 4, answer these five questions:

    Decision D-[S-ID] -- [state name]:
      Q1: What exact rule or data value is evaluated? (No vague conditions like "if valid.")
      Q2: Who evaluates it? R-[N] -- [role title]
      Q3: Branch YES -- if the condition is met: what happens? -> S-[N] or TERMINAL:[name]
      Q4: Branch NO -- if the condition is not met: what happens? -> S-[N] or TERMINAL:[name]
      Q5: FALLBACK -- if neither Q3 nor Q4 applies (ambiguous input, missing field, edge data):
          what happens and who routes it? -> S-[N] -- [handler and action]
          [If YES/NO are truly exhaustive: explain why no unhandled input is possible.]

    [Complete one block per DECISION state. No decision may have an unanswered Q5.]

---

## STEP 8 -- BOTTLENECKS AND GAPS

13. Where do delays accumulate most in this process? Name at least 2 bottlenecks.

    Bottleneck B-01:
      Where: [State name or transition -- S-ID]
      Why delays accumulate: [Specific mechanism -- not "slow approvals" but the actual domain cause]
      What blocks downstream: [Effect on subsequent states, dependent roles, or SLA]
      Owner of the delay source: R-[N] -- [role title]

    Bottleneck B-02:
      Where: [State name or transition -- S-ID]
      Why: [Specific mechanism]
      Downstream effect: [What gets blocked]
      Owner: R-[N]

    [Add B-03 if a third major bottleneck exists.]

14. What step is missing from this model that exists in real-world practice for this process type?
    Name at least 1.

    MISSING G-01: [Step name]
      Where it belongs: Between S-[ID] ([state name]) and S-[ID] ([state name])
      What it does: [Description of the step]
      Why it belongs in practice: [Domain rationale -- why real processes include this]
      Who would own it: R-[N] -- [role title]

---

## STEP 9 -- EDGE CASES

15. Name 3 scenarios that fall outside both the happy path and the exception flows above.
    Each must be a specific operational condition not duplicating any E-ID from Step 6.

    EC-01:
      Condition: [Specific trigger -- distinct from all E-IDs]
      Why problematic: [What the current model cannot handle]
      Correct response: [What the process should do]

    EC-02:
      Condition: [Distinct from E-IDs and EC-01]
      Why problematic: [What breaks]
      Correct response: [What should happen]

    EC-03:
      Condition: [Distinct from E-IDs, EC-01, EC-02]
      Why problematic: [What breaks]
      Correct response: [What should happen]

---

## STEP 10 -- CROSS-PROCESS INTERACTIONS

16. Where does this lifecycle hand off data or control to an adjacent process?
    Describe at least one inter-process handoff.

    Sending state: S-[ID] ([state name])
    Receiving process: [Adjacent process name -- e.g., GL Posting, Billing, Inventory Management]
    Data sent: [Fields or artifact handed off]
    Expected acknowledgment: [What the receiving process returns to confirm receipt]
    Who owns the handoff: R-[N] -- [role title]

    [Add additional handoffs if multiple inter-process touchpoints exist.]
    [If none: "No cross-process handoffs. This lifecycle is self-contained. Reason: [explain]"]

---

## STEP 11 -- SLA AND TIMING RISK

17. For at least 3 states or transitions, provide the SLA target and typical duration.
    For every at-risk entry, cite the bottleneck B-ID from Step 8 that explains the delay.

    | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Reference |
    |---------------------------|------------|------------------|----------|----------------------|
    | [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | [If YES: B-[ID] -- [bottleneck name]] |
    | [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | [If YES: B-[ID] -- [bottleneck name]] |
    | [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | [If YES: B-[ID] -- [bottleneck name]] |

    For every AT-RISK row with no B-ID cited: go to Step 8 and add a bottleneck entry first,
    then cite it here. An at-risk SLA entry without a bottleneck cross-reference is incomplete.

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, state_count, decision_count,
exception_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-03: Lifecycle Emphasis — Exception-First Phase Sections

**Axis:** Lifecycle emphasis — within each phase section, EXCEPTION TRACES are written before STATE
DETAILS. This order is structurally enforced: the exception table appears as the first content block
inside each phase section, before the state table and decision supplement blocks. Exceptions must be
specific to the conditions of the current phase because the phase context is the only available frame
when they are written.
**Hypothesis:** Writing exceptions before states forces phase-specific failure-mode reasoning before
the happy path is traced. C-13 compliance is structural: exceptions are generated inside a phase
section, so their phase origin is the phase section header itself -- no separate annotation needed.
This approach also reduces generic exception risk (C-02) because the model's generation scope is
bounded by the phase when exceptions are written. The full role registry gate (C-12) is retained
from R1 V-05. Per-phase decision supplement blocks (C-11) are retained from R1 V-05. SLA table
gains the `Bottleneck Cross-Ref` column for C-14. Tests whether exception-first ordering is a
sufficient C-13 mechanism without requiring a separate `Phase Origin` column.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, table columns, and sub-field labels are fixed.
ORDERING RULE: within each phase section, write EXCEPTION TRACES before STATE DETAILS.
This order is required -- do not swap it.
The ROLE REGISTRY must be complete before any phase section is written.
Every DECISION-type state requires a DECISION SUPPLEMENT BLOCK with a Fallback: field.
Do not use generic role names (Approver, Reviewer, Manager, Owner) anywhere in this output.
Do not reorder, rename, or remove any section header, column header, or template fragment.

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

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [What this role decides] | [Phases] | Not "Approver"/"Manager" |
| R-02 | [Name] | [Domain] | [What this role decides] | [Phases] | Not "Approver"/"Manager" |
| R-03 | [Name] | [Domain] | [What this role decides] | [Phases] | Not "Approver"/"Manager" |
[Add R-04, R-05 as needed.]

Registry gate: Process type [TYPE].
  [ ] All R-IDs have domain-specific names
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
[Declared before phase sections. All exception traces and phase exits must reach one of these.]
SUCCESS: [Name] -- [Condition]
FAILURE: [Name] -- [Condition]
[CANCEL: [Name] -- [Condition] -- add if applicable]

## PHASE MAP
[Declare all phases before writing phase sections. Every phase here must have a section below.]

| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [What starts this phase] | R-[N] | [What ends it] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Downstream Handoff for the last phase must reference a TERMINAL state.]

---

[For every phase declared in the PHASE MAP, write a section following this exact template.
ORDERING WITHIN EACH PHASE: Exception Traces -> States -> Decision Supplement Blocks -> Parallel Paths.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### Exception Traces for This Phase
[Write exception traces BEFORE the state table.
These exceptions originate in this phase -- their phase context is implied by the section header.
Generate failure modes that are specific to what happens in this phase.
At least one exception per phase where realistic.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.
Generic exceptions (system error, connection timeout) that could appear in any phase are not acceptable.]

| E-ID | Exception Name | Trigger State (S-ID) | Trigger Condition | Trace | Handling (R-ID) | Terminal |
|------|---------------|---------------------|-------------------|-------|-----------------|---------|
| E-[N] | [Name] | S-[ID] | [Phase-specific condition for this phase's work] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
[Add rows for additional exceptions originating in this phase.]

### States in This Phase

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks
[One block per DECISION-type state in the States table above.
Write "No DECISION-type states in this phase." if none.
Fallback: field is required for every block. Do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback:   [what happens when no branch condition applies] -> S-[ID]: [destination]
              [If branches are exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

[Repeat one block per DECISION-type state in this phase.]

### Parallel Work Streams in This Phase
[If this phase has concurrent branches:]
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase name or TERMINAL:name]

---

[Repeat the PHASE section for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS
[Source from phase sections above. Reference phase name and S-ID.]

Bottlenecks (minimum 2):
| B-ID | Phase: State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) |
|------|-----------------------------------|-------|-------------------|--------------|
| B-01 | [Phase: state/transition] | [Specific cause] | [Effect on downstream] | R-[N] |
| B-02 | [Phase: state/transition] | [Specific cause] | [Effect on downstream] | R-[N] |
[Add B-03 if additional bottlenecks exist.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What this step does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases distinct from all E-IDs written in any phase section. Cite the phase where each occurs.]

| EC-ID | Phase | Triggering Condition | Why Problematic | Correct Response |
|-------|-------|---------------------|-----------------|------------------|
| EC-01 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-02 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-03 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff. If none: "No cross-process interactions. Self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. For every AT-RISK row, cite the B-ID from BOTTLENECKS AND GAPS.
If an AT-RISK entry has no corresponding B-ID: add the bottleneck first, then reference it here.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [reason] -- causal source: B-[ID]"]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-04: Phrasing Register + Exception-First (Axes 2+3)

**Axes:** Phrasing register (V-02) + Exception-first lifecycle emphasis (V-03)
**Hypothesis:** Combining conversational questions with exception-first phase ordering tests whether
the two axes are mutually reinforcing or competing. The V-02 axis produces richer operational content
through active reasoning questions; the V-03 axis produces phase-specific exception traces by
constraining generation scope to the current phase. Together they may produce the highest C-02
specificity of any variation. The tradeoff: conversational format reduces blank-cell visibility
for C-01 and C-05 compared to table-column variations. Tests whether content quality improves
enough to compensate for reduced structural enforcement. C-11 is addressed through the mandatory
FALLBACK question in each decision block. C-12 through the prohibition-question gate in Part 1.
C-13 through exception questions preceding state questions per phase. C-14 through the explicit
bottleneck citation requirement in the SLA table.

```
You are running /flow-lifecycle. Answer every labeled question in order.
For each lifecycle phase, answer the exception questions BEFORE the state questions.
This order is required -- do not swap exception and state sections within a phase.
Do not use generic role names. Do not skip any labeled question.

---

## PART 1 -- PROCESS AND ROLES

Q1: What type of lifecycle is this?
    Answer: [L2O / P2P / PERIOD-CLOSE / CASE]

Q2: What single event triggers this lifecycle? (One sentence.)
    Answer: [Trigger event]

Q3: What domain?
    Answer: [Sales / Procurement / Finance / Support]

ROLE REGISTRY -- complete before any phase questions:

Q4: Who are the domain experts for this process? Name at least 3 roles using specific job titles.
    Use the actual title from this domain -- not "Approver," "Reviewer," "Manager," or "Owner."

    R-01: Title: [domain-specific]  |  Decides: [authority]  |  Active in: [phases]
    R-02: Title: [domain-specific]  |  Decides: [authority]  |  Active in: [phases]
    R-03: Title: [domain-specific]  |  Decides: [authority]  |  Active in: [phases]
    [Add R-04, R-05 if the process requires more roles.]

Q5: Anti-generic check: does any R-ID above use a generic title (Approver, Reviewer, Manager,
    Owner, Actor)?
    Answer: YES (fix before continuing) / NO (proceed to Q6)

TERMINAL STATES:

Q6: How does this lifecycle end successfully?
    SUCCESS: [Name]  --  Condition: [Entry condition for success]

Q7: How does it end in failure?
    FAILURE: [Name]  --  Condition: [Entry condition for failure]

Q8: Is cancellation possible?
    [CANCEL: [Name]  --  Condition: [What triggers cancellation]] / No cancellation path.

---

## PART 2 -- PHASE MAP

Q9: What are the named phases of this lifecycle? List them with their entry triggers, owners,
    exit conditions, and downstream handoffs.

    | Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
    |-------|--------------|--------------|----------------|--------------------|
    | [Name] | [What starts it] | R-[N] | [What ends it] | [Artifact or TERMINAL:name] |
    [Minimum 3 phases. Last phase must hand off to a TERMINAL state.]

---

## PART 3 -- PHASE DETAIL (answer for every phase)

For each phase, answer exception questions FIRST, then state questions.

---

### PHASE: [PHASE NAME]

Context: [Entry trigger] / Owner: R-[N] / Exit: [condition] / Handoff: [artifact or TERMINAL]

#### Exception Questions for This Phase

Q-EX-[N]a: What named failure modes originate specifically in this phase?
Think about what data conditions, role failures, timing events, or system states in THIS PHASE
cause the lifecycle to deviate. Generate at least one exception specific to this phase's work.

For each exception originating in this phase:

E-[N] -- [Exception name]:
  Phase origin: PHASE:[this phase name]
  What triggers it (phase-specific condition, not generic): [Condition]
  Which states does the trace pass through: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Who handles it: R-[N] -- [role title]
  What does the handler do to reach the terminal: [Action]

[Write at least one exception per phase where realistic.]
[Write "No plausible exceptions in this phase -- reason: [explain why]" only if genuinely true.]

#### State Questions for This Phase

Q-ST-[N]b: Now trace the states for this phase. For each state:

S-[ID]: [State Name]
  Entry condition: [What must be true before this state is entered?]
  Owner: R-[N] -- [Role title from ROLE REGISTRY]
  Type: NORMAL / DECISION / FORK / JOIN / TERMINAL
  What can happen next? (List every possible exit):
    [condition] -> S-[ID] or TERMINAL:[name]
    [condition] -> S-[ID] or TERMINAL:[name]

  [If DECISION type: also answer:]
  What exact rule or data value is evaluated? [Specific condition]
  Who evaluates it? R-[N] -- [role title]
  If the condition is met (Branch YES): -> S-[ID] / TERMINAL:[name]
  If the condition is not met (Branch NO): -> S-[ID] / TERMINAL:[name]
  FALLBACK -- if neither YES nor NO applies (ambiguous input, missing data, edge case):
    -> S-[ID] -- [who routes it and what they do]
    [If YES/NO are truly exhaustive: explain why no unhandled input is possible.]

[Trace all states in this phase.]

#### Parallel Work in This Phase

Q-PL-[N]c: Does this phase have concurrent branches?
  YES: Fork at S-[ID]. Branch A (R-[N]): [states]. Branch B (R-[N]): [states].
       Join at S-[ID]. Join type: AND/OR. Join condition: [what all branches must deliver].
  NO: "Sequential phase."

How does this phase end?
  [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat PART 3 phase block for every phase in PART 2]

---

## PART 4 -- BOTTLENECKS AND GAPS

Q10: Where do delays accumulate most? Name at least 2 bottlenecks.

Bottleneck B-01:
  Where: [State name -- S-ID, from which phase?]
  Why delays accumulate: [Specific mechanism in this domain]
  What blocks downstream: [Effect on subsequent states or SLA]
  Owner of delay source: R-[N] -- [role title]

Bottleneck B-02:
  Where: [State name -- S-ID]
  Why: [Specific mechanism]
  Downstream effect: [What gets blocked]
  Owner: R-[N]

[Add B-03 if a third significant bottleneck exists.]

Q11: What step is missing from this model that exists in real-world practice?
Name at least 1.

MISSING G-01: [Step name]
  Where it belongs: Between S-[ID] ([name]) and S-[ID] ([name]) in Phase: [name]
  What it does: [Description]
  Why it belongs in practice: [Domain rationale]
  Who would own it: R-[N] -- [role title]

---

## PART 5 -- EDGE CASES

Q12: Name 3 scenarios outside both the happy path and the exception flows above.
Do not duplicate any E-ID. For each, identify the phase where it would surface.

EC-01 (Phase: [name]):
  Condition: [What triggers this -- distinct from all E-IDs]
  Why problematic: [What the current model cannot handle]
  Correct response: [What should happen]

EC-02 (Phase: [name]):
  Condition: [Distinct from E-IDs and EC-01]
  Why problematic: [What breaks]
  Correct response: [What should happen]

EC-03 (Phase: [name]):
  Condition: [Distinct from all prior]
  Why problematic: [What breaks]
  Correct response: [What should happen]

---

## PART 6 -- CROSS-PROCESS INTERACTIONS

Q13: Where does this lifecycle hand off to an adjacent process?
Describe at least one inter-process handoff.

  Sending state: S-[ID] ([name]) in Phase: [name]
  Receiving process: [Adjacent process name]
  Data sent: [Fields or artifact]
  Expected acknowledgment: [What comes back from the receiving process]
  Who owns the handoff: R-[N] -- [role title]

[Add additional handoffs if they exist.]
[If none: "Self-contained. No cross-process handoffs. Reason: [explain]"]

---

## PART 7 -- SLA AND TIMING RISK

Q14: For at least 3 states or transitions, provide the SLA target and typical duration.
For every at-risk entry, cite the B-ID from Part 4 that explains the delay.

| State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Reference |
|---------------------------|------------|------------------|----------|----------------------|
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | [If YES: B-[ID] -- [bottleneck name]] |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | [If YES: B-[ID] -- [bottleneck name]] |
| [Name -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | [If YES: B-[ID] -- [bottleneck name]] |

For every AT-RISK row with no B-ID: go to Part 4 and add a bottleneck entry first.
SLA at-risk entries without bottleneck cross-references are incomplete.

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-05: Full Synthesis — Registry Gate + Exception-First Phase Sections + Decision Supplement Blocks + Bidirectional SLA-Bottleneck Chain

**Axes:** Role registry gate (R1 V-02 axis) + Exception-first phase sections (V-03 axis) + Decision
supplement blocks per phase (R1 V-03/V-05 axis) + Bidirectional SLA-to-bottleneck evidence chain (new)
**Hypothesis:** Maximum structural coverage for all 14 criteria. Four targeted additions over R1 V-05:
(1) exception traces are written before state tables within each phase section, making C-13 structural
rather than instructional; (2) the role registry gains an `Anti-Generic Check` column that makes the
generic-name prohibition visible per row, not just at the gate header; (3) every decision supplement
block gains an explicit `Fallback: (required)` label, making C-11 pass conditions visible as a labeled
required field; (4) the bottleneck table gains a `SLA Node Affected` column, and the SLA analysis
section includes a bidirectional check block that verifies no orphan entries on either side, closing
the C-14 evidence chain in both directions. Golden candidate for Round 2.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, table columns, and sub-field labels are fixed.
ORDERING RULE: within each phase section, Exception Traces appear BEFORE States.
The ROLE REGISTRY must be complete before any phase section is written.
Every Owner cell must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Every DECISION-type state must have a DECISION SUPPLEMENT BLOCK with a labeled Fallback: (required) field.
Every AT-RISK SLA row must cite a B-ID; every B-ID in BOTTLENECKS must name its SLA Node Affected.
Do not reorder, rename, or remove any section header, column header, or template fragment.

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

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions this role makes] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions this role makes] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions this role makes] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate: Process type [TYPE].
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
[Declared before phase sections. All exception traces and phase exit conditions must reach one of these.]
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- [Condition] -- add if the process type supports cancellation]

## PHASE MAP
[Declare all phases before writing phase detail sections. Every phase here must have a section below.]

| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Downstream Handoff for the last phase must reference a TERMINAL state.]

---

[For every phase in the PHASE MAP, write a section using the template below.
ORDERING WITHIN EACH PHASE: Exception Traces -> States -> Decision Supplement Blocks -> Parallel Paths.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### Exception Traces for This Phase
[Write these BEFORE the state table. Generate failure modes specific to the work done in this phase.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
At least one exception per phase where realistic.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.
Generic exceptions (system error, network timeout) that could appear in any phase are not acceptable.
Each E-ID must include a Phase Origin Stamp matching this phase.]

| E-ID | Exception Name | Phase Origin Stamp | Trigger State (S-ID) | Trigger Condition | Trace | Handling (R-ID) | Terminal |
|------|---------------|-------------------|---------------------|-------------------|-------|-----------------|---------|
| E-[N] | [Name] | PHASE:[this phase name] | S-[ID] | [Phase-specific condition] | S-[ID] -> ... | R-[N] | TERMINAL:[name] |
[Add rows for additional exceptions specific to this phase.]

### States
| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for every state in this phase. DECISION-type states have supplement blocks below.
Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks
[One block per DECISION-type state in the States table above.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) field must be filled for every block -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- must be specific to this process and phase]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If branches are exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

[Repeat one block per DECISION-type state in this phase.]

### Parallel Work Streams in This Phase
[If this phase has concurrent branches:]
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase name or TERMINAL:name]

---

[Repeat the PHASE section for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS
[Source from phase sections above. Every B-ID must name its SLA Node Affected for the C-14 bidirectional chain.]

Bottlenecks (minimum 2):
| B-ID | Phase: State or Transition (S-ID) | Cause | Downstream Impact | Owner (R-ID) | SLA Node Affected |
|------|-----------------------------------|-------|-------------------|--------------|-------------------|
| B-01 | [Phase: state/transition] | [Specific cause] | [Effect on downstream] | R-[N] | [State name whose SLA this bottleneck impacts -- must appear in SLA ANALYSIS below] |
| B-02 | [Phase: state/transition] | [Specific cause] | [Effect on downstream] | R-[N] | [State name whose SLA this bottleneck impacts] |
[Add B-03 if additional bottlenecks exist.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What this step does] | [Why standard practice for this process type] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace from any phase section above.
Each edge case must cite the phase where it would surface.]

| EC-ID | Phase | Triggering Condition | Why Problematic | Correct Response |
|-------|-------|---------------------|-----------------|------------------|
| EC-01 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-02 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |
| EC-03 | [Phase] | [Condition -- distinct from all E-IDs] | [Problem] | [Handling] |

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. BIDIRECTIONAL EVIDENCE CHAIN RULE:
  Forward link: every AT-RISK row must cite a B-ID from BOTTLENECKS AND GAPS.
  Backward link: every B-ID in BOTTLENECKS AND GAPS must have a matching entry in this table
  (the SLA Node Affected column in BOTTLENECKS points to the row here).
  No orphan at-risk entries. No orphan bottleneck IDs.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [reason typical exceeds SLA] -- causal source: B-[ID]"]

Bidirectional evidence check:
  For each AT-RISK row: B-[ID] cited? [YES: chain closed | NO: add B-ID to BOTTLENECKS first]
  For each B-ID in BOTTLENECKS: SLA Node Affected appears in this table? [YES: chain closed | NO: add SLA row]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## Round 2 Design Notes

### Variation axis selection rationale

Three single-axis variations:
- **Output format fixed** (V-01): R1 V-01 repaired with Decision Supplement Catalog (C-11) and role
  registry gate (C-12). Flat table preserved. Tests whether targeted structural additions to the
  R1 V-01 design close the aspirational gap without phase sections.
- **Phrasing register** (V-02): New axis not tested in R1. Conversational question format replaces
  table columns and template sub-fields. Tests whether active-answer questions produce richer
  operational content (C-02, C-07) while still satisfying structural criteria through prohibition
  gates and mandatory-answer sub-questions.
- **Lifecycle emphasis -- exception-first** (V-03): Intensification of R1 V-03. Exception traces
  appear before state tables within each phase. Makes C-13 structural (phase-section header is the
  phase origin stamp) rather than instructional. Combines with R1 V-02's registry gate for C-12.

Phrasing register and inertia framing were not combined in R1. R2 tests phrasing register as a
primary single-axis variation. Inertia framing remains unexamined; not selected for R2 because
no rubric criterion directly rewards process-contrast framing.

### Criterion structural guarantees by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (entry + exits) | Table columns | Mandatory entry condition + exits questions per state | Table columns per phase | Mandatory questions per state | Table columns per phase |
| C-02 (3+ exceptions) | Exception table with Phase/State Origin column | E-block with phase origin sub-field | Exception table per phase (before states) | E-blocks per phase (before state questions) | Exception table per phase with Phase Origin Stamp column |
| C-03 (domain roles) | Registry gate + Anti-Generic Check column | Prohibition-question gate + confirm step | Registry gate + Anti-Generic Check column | Prohibition-question gate + confirm step | Registry gate + Anti-Generic Check column + Owner column |
| C-04 (bottlenecks + MISSING) | Pre-printed tables | B-block + MISSING block per step | Phase-sourced tables | Phase-sourced B/MISSING answers | Phase-sourced tables with B-ID↔SLA linkage |
| C-05 (terminal states) | Declared upfront; exit format enforces TERMINAL refs | Q6/Q7/Q8 answer blocks; exits must reference declared terminals | Declared upfront; phase end declaration | Q6-Q8 blocks; phase-end questions | Declared upfront; phase end declaration per section |
| C-06 (parallel paths) | Pre-printed section | Q10 parallel work question | Per-phase parallel section | Per-phase parallel question | Per-phase parallel section |
| C-07 (edge cases) | Pre-printed 3-row table | Q15 three-block answers | Phase-cited 3-row table | Phase-cited answers | Phase-cited 3-row table |
| C-08 (decision explicitness) | Supplement Catalog with Fallback: field | Q-DECISION sub-questions + mandatory FALLBACK | Per-phase supplement blocks with Fallback: | Decision FALLBACK question per state | Per-phase supplement blocks with Fallback: (required) label |
| C-09 (cross-process) | Pre-printed 5-column table | Q16 handoff answer block | Pre-printed section | Part 6 handoff answer | Pre-printed section |
| C-10 (SLA analysis) | Pre-printed 3-row table + Cross-Ref column | Q17 table + citation requirement | Phase-tagged table + Cross-Ref column | Part 7 table + citation requirement | Phase-tagged table + Cross-Ref column |
| C-11 (decision supplement block) | Standalone DECISION SUPPLEMENT CATALOG; one block per DECISION state | Step 7 mandatory 5-question block per decision; Q5 = FALLBACK | Per-phase DECISION SUPPLEMENT BLOCKS with Fallback: field | FALLBACK question in phase exception/state section | Per-phase blocks with Fallback: (required) label |
| C-12 (role registry gate) | Registry table + Anti-Generic Check column + gate checklist | Step 2 prohibition questions + Step 5 confirm gate | Registry table + Anti-Generic Check column + gate checklist | Part 1 prohibition questions + Q5 confirm | Registry table + Anti-Generic Check column + gate checklist |
| C-13 (phase-scoped exceptions) | Phase/State Origin column in flat exception table | Phase origin stamp sub-field per E-block | Exception table per phase section (structural) | Exception questions before state questions per phase | Exception table per phase with Phase Origin Stamp column (structural) |
| C-14 (SLA-to-bottleneck chain) | Bottleneck Cross-Ref column + AT-RISK NOTE citing B-ID | Q17 AT-RISK citation requirement; orphan-check note | Bottleneck Cross-Ref column + AT-RISK NOTE | Part 7 citation requirement; bidirectional note | Bidirectional check: B-ID↔SLA Node Affected columns; post-table check block |

### Predicted aspirational scores against v2 rubric

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Aspirational pts |
|-----------|------|------|------|------|------|------|-----------------|
| V-01 | PASS | PASS | PASS | PASS | PASS (column) | PASS | 6/6 = 10 |
| V-02 | PASS | PASS | PASS | PASS | PASS (sub-field) | PASS | 6/6 = 10 |
| V-03 | PASS | PASS | PASS | PASS | PASS (structural) | PASS | 6/6 = 10 |
| V-04 | PASS | PASS | PASS | PASS | PASS (structural) | PASS | 6/6 = 10 |
| V-05 | PASS | PASS | PASS | PASS | PASS (structural + column) | PASS | 6/6 = 10 |

**All five variations are designed to score 100 against the v2 rubric.** The discrimination in R2 lives
within the 100 cluster, in structural reliability differences:

| Strength | Variations | Why |
|----------|-----------|-----|
| Strongest | V-05 | Exception-first order structural; Phase Origin Stamp column; Fallback: (required) label; bidirectional B-ID↔SLA check; three C-03 surfaces |
| Strong | V-03 | Exception-first structural; registry gate; per-phase decision supplement; SLA cross-ref |
| Strong | V-01 | Supplement Catalog makes all decisions visible in one place; registry gate; SLA cross-ref |
| Moderate | V-04 | Exception-first structural via question order; all criteria covered by questions; lower blank-cell visibility |
| Moderate | V-02 | All criteria covered by mandatory questions; richest likely content; weakest structural visibility |

**V-05 open question for live runs:** Does the bidirectional SLA-bottleneck check block (requiring that
every B-ID's SLA Node Affected column matches a table row) produce a closed evidence chain without
generating orphan bottleneck entries or orphan at-risk rows? Does the `Fallback: (required)` label
produce stronger fallback coverage than `Fallback:` alone?

**V-01 vs V-03 open question:** Does grouping all decision supplement blocks in a standalone catalog
(V-01) or distributing them inside phase sections (V-03) produce more exhaustive fallback coverage?
The catalog is a single, auditable location; the per-phase blocks provide context proximity.

**V-02 content quality hypothesis:** The conversational format is predicted to produce the most
operationally specific exception traces (C-02) and edge cases (C-07) because the model constructs
answers rather than fills pre-labeled cells. Whether this content quality advantage is structurally
visible in rubric scoring is the key live-run question.
