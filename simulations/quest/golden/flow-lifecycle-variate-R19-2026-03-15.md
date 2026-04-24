---
skill: flow-lifecycle
round: 3-session (file: R19)
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v22-2026-03-15.md
---

# flow-lifecycle -- Round 3 Variations (Rubric v22)

**Context:** R3 of the current rubric iteration series. Rubric v22 adds two new aspirational criteria
extracted from R2 excellence signals:
- **C-14** Edge Case SLA Risk Attribution (each C-08 edge case carries an SLA risk field with phase,
  magnitude, and breach-vs-delay classification)
- **C-15** Exception Coverage Completeness Audit (explicit per-phase audit of exception handler
  presence; phases with no handler named; full-coverage declaration required if all phases covered)

**R2 learning applied to R3 design:**
- R2 V-01 locked 115/115 (rubric v21) using VARIANT DECLARATION + Phase Exit Gate breach verdict
  field + SLA impact on every exception flow. That architecture is preserved as the base layer.
- C-14 requires SLA risk on edge cases: same field strictness as C-10 and C-12 -- quantitative or
  directional, not "may affect timing."
- C-15 requires a coverage audit section: listing phases is not enough -- gap consequence must be
  named, or full coverage must be explicitly declared.
- R3 primary risk: an output that earns C-08 (edge cases listed) and C-02 (exceptions traced) but
  fails C-14 (no SLA risk on edge cases) and C-15 (no coverage audit). The variations below address
  this structurally.

Single-axis: V-01 (output format: required-column enforcement), V-02 (lifecycle emphasis: full
125-point lock), V-03 (role sequence: coverage-audited handoff).
Combined: V-04 (output format + lifecycle emphasis), V-05 (phrasing register + inertia framing).

---

## V-01 -- Output Format Axis

**Variation axis:** Output format -- every exception and edge case entry is a row in a structured
table with required columns that include SLA risk (C-14) and exception coverage (C-15). Tables
cannot be selectively populated; a blank cell in a required column is a structural fail. The
exception coverage audit is a required table at the end of the exception catalog, not a free-form
section.

**Hypothesis:** C-14 and C-15 fail in unconstrained prompts because the author produces rich
exception and edge case prose, then never returns to add SLA risk or coverage audit fields. Imposing
a fixed table schema forces the author to fill every cell at authoring time, not as an afterthought.
A missing SLA risk cell is visible in a table; a missing SLA risk paragraph in prose is invisible.
The coverage audit table (one row per phase, `Exception Coverage` column) makes C-15 structural:
the phase with no exception handler produces an empty coverage cell that cannot be overlooked.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process
named in the signal.

---

**LIFECYCLE PHASES**

Identify all phases before tracing any states. A phase is a named cluster of states with a
discrete completion condition.

| Ph-ID | Phase Name | Purpose | Entry Trigger | SLA Envelope |
|-------|-----------|---------|--------------|--------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

SLA Envelope = the elapsed-time window within which this phase is expected to complete under
normal conditions (e.g., "same business day", "2-5 business days").

---

**ROLE REGISTRY**

| R-ID | Role Name (domain-qualified) | Phases Active | Primary Responsibility |
|------|------------------------------|--------------|------------------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Domain-qualified means a named function: "Credit Analyst," "AP Clerk," "Revenue Accountant."
"Finance team" or "Management" do not qualify.

---

**FOR EACH PHASE -- repeat for every Ph-ID:**

---

**STATE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Owner (R-ID) | Entry Condition | Exit Transition | Exception Exit |
|------|------------|-------------|-----------------|-----------------|---------------|
| | | | | | |

State naming rule: names must be unambiguous identifiers (e.g., "PO Pending Approval," not
"the approval stage"). A state described in prose without an S-ID does not count toward the
6-state minimum.

**DECISION POINTS -- [Ph-ID: Phase Name]**

| D-ID | Decision Question | Owner (R-ID) | Branch A (label + target) | Branch B (label + target) | Fallback |
|------|------------------|-------------|--------------------------|--------------------------|---------|
| | | | | | |

All three elements (question, owner, outcome branches) are required per row. A decision point
with a blank owner cell is a partial pass (0.5).

---

*Repeat STATE TRACE and DECISION POINTS for each phase.*

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|-------------------|----------------|
| | | | | | |

If the lifecycle is entirely sequential, state that explicitly and propose one parallelization
opportunity, naming the roles and states it would involve.

---

**EXCEPTION CATALOG**

At least one exception per lifecycle phase. Every row must populate all columns.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Deviation from Normal | Recovery (S-ID or T-ID) | SLA Impact |
|------|--------------|---------------|------------------|-----------------------|------------------------|-----------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |
| ... | | | | | | |

SLA Impact column: state the timing consequence explicitly -- "adds 3+ days to PO approval phase;
triggers breach threshold." "May cause delays" does not qualify.

---

**EXCEPTION COVERAGE AUDIT** *(required -- C-15)*

One row per lifecycle phase. Phases with no exception handler listed in the catalog above are
gaps; name the risk consequence.

| Ph-ID | Phase Name | Exception Coverage | Handler E-IDs | Gap Risk (if uncovered) |
|-------|-----------|-------------------|--------------|------------------------|
| PH-01 | | covered / gap | | |
| PH-02 | | covered / gap | | |
| ... | | | | |

If every phase is covered, the final row must read: **"Full coverage declared. All [N] phases
have at least one exception handler."** Do not leave this table blank.

---

**EDGE CASE TABLE** *(required -- C-08 + C-14)*

At least 2 edge cases distinct from the exception flows above. Every row must populate all
columns including `SLA Risk`.

| EC-ID | Phase (Ph-ID) | Edge Case Name | Trigger Condition | Why Lifecycle Has No Handler | Risk / Consequence | SLA Risk |
|-------|--------------|---------------|------------------|-----------------------------|--------------------|---------|
| EC-01 | | | | | | |
| EC-02 | | | | | | |
| ... | | | | | | |

SLA Risk column: name the specific phase SLA or timing envelope at risk, the expected magnitude
of impact, and whether this is a breach-level consequence or a delay.
Example: `"Puts Day-3 PO approval SLA at risk; concurrent volume peak likely causes breach."`
"May affect timing" does not qualify.

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Reached From (S-IDs + E-IDs) |
|------|--------------|------|------------|------------------------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | |
| ... | | | | |

Terminal gate: every S-ID in the state traces and every E-ID in the exception catalog must
either continue to another state or appear in "Reached From." Blank IDs are open paths and
a structural fail.

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

At least 2 bottlenecks with cause, and at least 1 process gap (a step the described lifecycle
omits but that real-world execution requires).

---

**CROSS-LIFECYCLE DEPENDENCY TABLE** *(raise score)*

| Adjacent Lifecycle | Direction | Handoff Trigger | Artifact Passed | Coupling State | SLA Dependency |
|-------------------|-----------|----------------|----------------|---------------|---------------|
| | sends / receives | | | | |

---

**VARIANT DECLARATION** *(required for C-13)*

| Field | Value |
|-------|-------|
| Variant framing | single-state trace / as-is + to-be dual trace |
| Reason | [if single-state: why no variant comparison applies] |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Phases > Role Registry > Phase State Traces and Decision Points >
Parallel Path Table > Exception Catalog > Exception Coverage Audit > Edge Case Table >
Terminal Declaration > Bottleneck and Gap Table > Cross-Lifecycle Dependency Table >
Variant Declaration.

Every table must be fully populated. Blank cells in required columns are structural fails.
The Exception Coverage Audit must account for every phase. The Edge Case SLA Risk column
must name a specific phase SLA and magnitude. Every path must reach a declared T-ID.

---

## V-02 -- Lifecycle Emphasis Axis: Full 125-Point Lock

**Variation axis:** Lifecycle emphasis -- extends R2 V-01's SLA-first architecture (which
targeted 115/115 under v21) with two targeted structural additions for the v22 aspirational
criteria: (1) Edge Case SLA Risk field required in every edge case template entry for C-14,
(2) EXCEPTION COVERAGE AUDIT section added as a required block immediately after the
exception catalog for C-15. Everything from R2 V-01 is preserved; the two additions are
surgical.

**Hypothesis:** R2 V-01 achieved 115/115 by adding three targeted fields (VARIANT DECLARATION,
Breach Verdict, SLA impact on exceptions) to V-02 R1's proven phase architecture. The same
pattern applies to v22: C-14 and C-15 are structural extensions of what already works (edge
case enumeration + exception catalog). Two more targeted fields -- edge case SLA risk and
coverage audit block -- should lock 125/125 without structural regression.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

---

**VARIANT DECLARATION**

Before tracing any states, declare the simulation scope.

| Field | Value |
|-------|-------|
| Lifecycle | [name of the process being simulated] |
| Variant framing | single-state trace -- no as-is/to-be distinction |
| Reason | [why no variant comparison applies -- e.g., "process is net-new," "scope is restricted to the target system configuration," "prompt names a single operational state"] |

This block is required. A missing or blank Variant Declaration is a structural fail.

---

**LIFECYCLE PHASES**

Identify all phases before tracing any states. Every state belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Entry Trigger | SLA Envelope (expected) |
|-------|-----------|---------|--------------|------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

SLA Envelope = the elapsed-time window within which this phase is expected to complete under
normal conditions.

---

**FOR EACH PHASE -- repeat this entire block for every Ph-ID:**

---

**PHASE ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | [Ph-ID or INITIAL] |
| Roles active | [domain-qualified role names -- "Finance team" is not domain-qualified] |
| Objects entering | [named artifacts or records] |
| Exception pre-check | [conditions that block entry and route to exception before work begins] |
| SLA clock start | [event that starts the timing clock for this phase] |

**STATE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Exit Owner (domain role) | Exception Exit |
|------|------------|-----------------|-----------------|--------------------------|---------------|
| | | | | | |

State naming rule: names must be unambiguous identifiers (e.g., "PO Pending Approval" not
"the approval stage"). Steps described in prose without an S-ID do not count.

**DECISION POINTS -- [Ph-ID: Phase Name]**

```
Decision:  [the question being resolved]
Owner:     [domain-qualified role -- named function, not department label]
Branch A:  [transition label + target S-ID or Ph-ID]
Branch B:  [transition label + target S-ID or Ph-ID]
Fallback:  [path if decision cannot be resolved -- timeout, escalation, or terminal]
```

All three elements (question, owner, branches) required. A missing owner is a partial pass (0.5).

**PHASE EXIT GATE -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition | [S-ID or Ph-ID] |
| Failure transition | [T-ID or exception name] |
| Primary blocker | [role, resource, or condition that most commonly delays exit] |
| SLA at-risk threshold | [elapsed time at which this phase is considered at-risk] |
| Scenario breach | [Y / N -- does the simulated scenario exceed the at-risk threshold?] |
| Breach verdict | [if Y: the specific cause of breach in this scenario, traceable to a state or exception above] |
| Exception coverage status | [covered / gap -- are all foreseeable exceptions handled in this phase? If gap: name the unhandled class] |

---

*Repeat PHASE ENTRY CONTRACT + STATE TRACE + DECISION POINTS + PHASE EXIT GATE for each phase.*

---

**BOTTLENECK SYNTHESIS**

Review all Phase Exit Gates where Scenario breach = Y. For each breached gate:

| B-ID | Phase (Ph-ID) | At-Risk Threshold Breached | Root Cause | Downstream Cascade |
|------|--------------|---------------------------|------------|-------------------|
| B-01 | | | | |
| B-02 | | | | |

If no phase breaches, identify the two most vulnerable phases under peak load or exception
conditions and explain why.

Additionally, name at least 1 process gap -- a step that real-world execution requires but
the described lifecycle omits.

---

**PARALLEL PATH ANALYSIS**

```
Fork state:      [S-ID or Ph-ID where concurrent execution begins]
Branch A:        [activity + owner role]
Branch B:        [activity + owner role]
Join condition:  [what must be true before threads merge]
Time saving:     [estimated elapsed time saved vs. sequential execution]
Merge owner:     [domain-qualified role]
```

If the lifecycle is sequential, state that explicitly and identify one parallelization
opportunity, naming roles and states.

---

**EXCEPTION FLOW CATALOG**

At least one exception per lifecycle phase. Each must be process-specific.

```
Exception:     [name]
Phase:         [Ph-ID]
Trigger:       [specific condition]
Deviation:     [how this diverges from the normal phase sequence]
SLA impact:    [timing consequence -- "adds N days to phase; triggers/does-not-trigger breach
                threshold." Quantitative or directional required. "May cause delays" does not
                qualify.]
Recovery:      [T-ID or recovery S-ID]
```

---

**EXCEPTION COVERAGE COMPLETENESS AUDIT** *(required -- C-15)*

After cataloging all exception flows above, audit every phase for coverage completeness.

| Ph-ID | Phase Name | Exception Coverage | Exceptions Traced | Gap Risk (if uncovered) |
|-------|-----------|-------------------|------------------|------------------------|
| PH-01 | | covered / gap | [exception names] | |
| PH-02 | | covered / gap | [exception names] | |
| ... | | | | |

Rules:
- Every phase from the LIFECYCLE PHASES table must appear as a row.
- "Gap" phases must name the risk consequence of having no exception handler: what failure mode
  is invisible, what recovery path is absent, what downstream impact is undetected.
- If every phase is covered, the last row must explicitly declare: "Full coverage -- all [N]
  phases have at least one exception handler." Silence does not earn this criterion.

---

**EDGE CASE CATALOG** *(required -- C-08 + C-14)*

At least 2 edge cases distinct from the exception flows above.

```
Edge case:     [name]
Phase:         [Ph-ID]
Trigger:       [condition that produces this path]
Gap:           [why the current lifecycle has no step for this scenario]
Consequence:   [the risk or impact if this case fires unhandled]
SLA risk:      [which phase SLA or timing envelope is at risk; expected magnitude; breach-level
                consequence or delay. Must name a specific threshold -- "may affect timing" does
                not qualify. Example: "Puts Day-3 PO approval SLA at risk; likely breach if
                concurrent with month-end volume peak."]
```

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Reached From |
|------|--------------|------|------------|-------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | |
| ... | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY** *(raise score)*

```
Adjacent lifecycle:    [name]
Direction:             [this lifecycle sends to / receives from]
Handoff trigger:       [what event initiates the handoff]
Coupling state:        [the state or artifact at which the handoff occurs]
SLA dependency:        [does the adjacent lifecycle's timing affect this one's SLA?]
```

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Variant Declaration > Lifecycle Phases > Phases (entry contract + state trace +
decisions + exit gate per phase) > Bottleneck Synthesis > Parallel Path Analysis > Exception
Flow Catalog > Exception Coverage Completeness Audit > Edge Case Catalog > Terminal
Declaration > Cross-Lifecycle Dependency.

Every phase exit gate must include a Scenario breach answer (Y/N) with a Breach verdict
(if Y) and an Exception coverage status (covered/gap). Every edge case must include a
populated SLA risk field naming a specific threshold. The coverage audit must account for
every phase. Every path must reach a declared T-ID.

---

## V-03 -- Role Sequence Axis: Coverage-Audited Handoff

**Variation axis:** Role sequence -- roles introduced in handoff order as in R1 V-01 and
R2 V-03, extended with two additions targeting v22: (1) each edge case in Stage 6 carries
a required SLA risk field (C-14), (2) a per-phase Exception Coverage Audit table appears
as Stage 5.5 between the exception flow catalog and the edge case catalog (C-15). The
handoff-ordered structure naturally organizes exceptions and edge cases by role ownership,
making coverage gaps visible as handoff points with no exception-owning role.

**Hypothesis:** The handoff sequence structure that proved effective in R1 and R2 is already
phase-organized. Adding a coverage audit as a required stage between exception flows and edge
cases means the author reviews exception coverage while the per-phase structure is still
visible. Edge cases, which appear immediately after, naturally inherit the SLA risk field
from the timing machinery already established by the handoff SLA annotations. C-13 is
earned via the single-state exemption declaration in the PROCESS CONTEXT block.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

---

**PROCESS CONTEXT**

```
Lifecycle:       [name of process, e.g., Purchase-to-Pay]
Variant framing: [single-state trace OR as-is/to-be dual trace]
Reason:          [if single-state: why no variant comparison applies]
Scope:           [which document types or sub-processes are in scope]
```

---

**HANDOFF SEQUENCE -- ROLE INTRODUCTION**

Introduce roles in the order they first receive or act on the process object. A role entry
is valid only when its first-touch point is named.

| Seq | First-Touch Point | R-ID | Role Name (domain-qualified) | Handoff Received From | Handoff Passes To | SLA Owner? |
|-----|-------------------|------|------------------------------|----------------------|-------------------|-----------|
| 1 | | R-01 | | ORIGIN | | Y / N |
| 2 | | R-02 | | R-01 | | Y / N |
| ... | | | | | | |

SLA Owner: mark Y for roles who are accountable for a phase or step completing within its
SLA envelope. At least one role per phase must be marked Y.

**HANDOFF GATE: Every R-ID cited in any later stage must appear in this table with a named
first-touch point. A decision point citing an unnamed actor is a fail. A handoff that skips
a sequence number without explanation is a gap.**

---

**STAGE 1 -- STATE TRACE IN HANDOFF ORDER**

| S-ID | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits (labeled) | Phase (Ph-ID) |
|------|------------|-------------|-----------------|----------------|-----------------|--------------|
| S-01 | | | | | | |
| S-02 | | | | | | |
| ... | | | | | | |

**Orphan check: Every R-ID from the handoff table must own at least one S-ID. An R-ID
with no state is a phantom role.**

---

**STAGE 2 -- DECISION AND FORK POINTS**

For each decision point in the lifecycle:

```
Decision: [question being resolved at this fork]
Owner:    [R-ID from the handoff table]
Seq:      [handoff sequence number of the decision owner]
Branch A: [transition label and target S-ID if condition is met]
Branch B: [transition label and target S-ID if condition fails]
Fallback: [what happens if the decision cannot be made -- timeout, escalation, or terminal]
```

A decision point that names the condition but omits the owner R-ID is a partial pass (0.5).

---

**STAGE 3 -- PARALLEL PATHS**

```
Fork state:      [S-ID where concurrent execution begins]
Branch A:        [thread label -- activity + R-ID]
Branch B:        [thread label -- activity + R-ID]
Join condition:  [what must be true before branches merge]
Join owner:      [R-ID who validates the merge]
Downstream:      [S-ID that follows the join]
```

If the process is entirely sequential, state that explicitly and propose one parallelization
that would reduce elapsed time, naming the roles and states affected.

---

**STAGE 4 -- EXCEPTION FLOWS**

At least one exception per lifecycle phase. Each exception must be specific to this process.

```
Exception:   [name]
Phase:       [Ph-ID]
Origin:      [S-ID where the exception arises]
Owner:       [R-ID -- the role who detects or handles this exception]
Trigger:     [specific condition, in domain terms]
Deviation:   [how this diverges from the happy-path trace]
SLA impact:  [timing consequence -- quantitative or directional required, e.g., "adds 2+ days
              to approval phase; puts 5-day SLA at risk of breach."]
Recovery:    [recovery state (S-ID) or terminal failure state (T-ID)]
```

---

**STAGE 5 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | Last Owner (R-ID) | Reached From (S-IDs) |
|------|--------------|------|------------------|----------------------|
| T-01 | | success / failure / cancel | | |
| T-02 | | | | |
| ... | | | | |

**Terminal gate: After filling this table, scan every S-ID and every exception recovery state.
Any ID not listed in "Reached From" and not continuing to another state is an open path and
a fail.**

---

**STAGE 5.5 -- EXCEPTION COVERAGE AUDIT** *(required -- C-15)*

After completing exception flows, audit every lifecycle phase for coverage completeness.
A phase is covered if at least one exception in Stage 4 fires from that phase.

| Ph-ID | Phase Name | Coverage | Exception Owner (R-ID) | Exception Names | Gap Risk (if uncovered) |
|-------|-----------|---------|----------------------|----------------|------------------------|
| PH-01 | | covered / gap | | | |
| PH-02 | | covered / gap | | | |
| ... | | | | | |

Rules:
- "Gap" phases must name what failure mode is invisible and what the downstream risk is.
- If all phases are covered, the row labeled "COVERAGE VERDICT" must read: "Full coverage --
  all [N] phases have at least one exception handler." Silence does not earn this criterion.

---

**STAGE 6 -- BOTTLENECK, GAP, AND EDGE CASE ANALYSIS**

**Bottleneck and gap identification:**

Review the handoff sequence table. Any role who appears in only one state, or whose
Handoff Passes To field points to a terminal, is a bottleneck candidate.

| B-ID | Type | Name | Phase (Ph-ID) | Cause (domain-specific) | Downstream Impact |
|------|------|------|--------------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

**Edge case catalog (C-08 + C-14):**

At least 2 edge cases distinct from the exception flows in Stage 4.

```
Edge case:      [name]
Phase:          [Ph-ID]
Handoff point:  [R-ID or sequence number where this occurs]
Trigger:        [condition that produces this path]
Gap:            [why the handoff sequence has no step for this scenario]
Consequence:    [the risk if this fires unhandled]
SLA risk:       [which phase SLA or timing envelope is at risk; expected magnitude; whether
                 breach-level or delay. Must name a specific threshold.
                 Example: "Puts PH-02 5-day approval SLA at risk; breach likely if dispute
                 resolution cycle exceeds 2 days."]
```

---

**STAGE 7 -- SLA AND TIMING SUMMARY** *(raise score)*

For each phase where the SLA owner (from handoff table) is accountable:

| Ph-ID | Phase Name | SLA Envelope | At-Risk Threshold | Scenario Breach (Y/N) | Breach Cause |
|-------|-----------|-------------|------------------|----------------------|-------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

At least 1 breach = Y verdict must appear with a cause traceable to a specific bottleneck
or exception in the trace.

---

**STAGE 8 -- CROSS-PROCESS HANDOFF** *(raise score)*

| Terminal (T-ID) | Recipient Process | Handoff Trigger | Fields Passed | Acceptance Condition |
|----------------|------------------|-----------------|---------------|---------------------|
| | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Process Context > Handoff Sequence > Stage 1 (State Trace) > Stage 2 (Decisions)
> Stage 3 (Parallel Paths) > Stage 4 (Exception Flows) > Stage 5 (Terminal Declaration) >
Stage 5.5 (Exception Coverage Audit) > Stage 6 (Bottleneck + Gap + Edge Cases) > Stage 7
(SLA Summary) > Stage 8 (Cross-Process Handoff).

Every R-ID in the handoff table must own at least one state. Every edge case must include a
populated SLA risk field. The coverage audit must account for every phase. Every path must
reach a declared T-ID.

---

## V-04 -- Combined (Output Format + Lifecycle Emphasis)

**Variation axes combined:**
1. Output format -- strict table schema throughout; required columns for SLA risk and exception
   coverage make C-14 and C-15 structurally enforced
2. Lifecycle emphasis -- SLA-first per-phase architecture with entry contracts, exit gates,
   breach verdicts, and phase-organized exception coverage

**Hypothesis:** The two axes compound: the lifecycle emphasis architecture provides the SLA
machinery (phase envelopes, at-risk thresholds, breach verdicts) that C-14 SLA risk fields
refer back to. The output format enforces completeness: every required column must be
populated before the author can consider the section done. The combination means the SLA
risk in an edge case entry is not a free-form narrative judgment but a reference to a specific
phase envelope already established in the lifecycle phases table -- precise, cross-referenceable,
and machine-checkable.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

---

**VARIANT DECLARATION** *(required)*

| Field | Value |
|-------|-------|
| Lifecycle | |
| Variant framing | single-state trace -- no as-is/to-be distinction |
| Reason | [why no variant comparison applies] |

---

**LIFECYCLE PHASES**

| Ph-ID | Phase Name | Purpose | Entry Trigger | SLA Envelope | At-Risk Threshold |
|-------|-----------|---------|--------------|--------------|------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

At-Risk Threshold = the elapsed time at which this phase is considered at-risk of breaching
its SLA. This column is referenced by edge case SLA risk fields below.

---

**ROLE REGISTRY**

| R-ID | Role Name (domain-qualified) | Phases Active | Exception Owner? |
|------|------------------------------|--------------|-----------------|
| R-01 | | | Y / N |
| R-02 | | | Y / N |
| ... | | | |

Exception Owner = Y if this role detects or handles at least one exception in this lifecycle.
At least one role per phase must be an exception owner.

---

**FOR EACH PHASE:**

---

**PHASE ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | [Ph-ID or INITIAL] |
| Roles active (R-IDs) | |
| Objects entering | |
| Exception pre-check | |
| SLA clock start | |

**STATE TABLE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Owner (R-ID) | Entry Condition | Exit Transition | Exception Exit |
|------|------------|-------------|-----------------|-----------------|---------------|
| | | | | | |

**DECISION TABLE -- [Ph-ID: Phase Name]**

| D-ID | Decision Question | Owner (R-ID) | Branch A (label + S-ID) | Branch B (label + S-ID) | Fallback |
|------|------------------|-------------|------------------------|------------------------|---------|
| | | | | | |

**EXCEPTION TABLE -- [Ph-ID: Phase Name]**

| E-ID | Exception Name | Trigger Condition | Deviation | SLA Impact | Recovery (S-ID or T-ID) |
|------|---------------|------------------|-----------|-----------|------------------------|
| | | | | | |

SLA Impact: quantitative or directional required. Reference the At-Risk Threshold from the
Lifecycle Phases table where applicable.

**PHASE EXIT GATE -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition | |
| Failure transition | |
| Primary blocker | |
| Scenario breach | Y / N |
| Breach verdict | [if Y: specific cause traceable to a state or exception in this phase] |
| Exception coverage | covered / gap |
| Coverage gap detail | [if gap: what exception class is unhandled and what is the consequence] |

---

*Repeat PHASE ENTRY CONTRACT + STATE TABLE + DECISION TABLE + EXCEPTION TABLE + PHASE EXIT
GATE for each phase.*

---

**EXCEPTION COVERAGE AUDIT** *(required -- C-15)*

Consolidate coverage status across all phases. Every phase from the Lifecycle Phases table
must appear.

| Ph-ID | Phase Name | Coverage | Exception E-IDs | Gap Consequence |
|-------|-----------|---------|----------------|----------------|
| PH-01 | | covered / gap | | |
| PH-02 | | covered / gap | | |
| ... | | | | |

If every phase is covered, append: **"Full coverage -- all [N] phases have exception
handlers. No unhandled phase gaps identified."**

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Time Saving | Join Owner (R-ID) |
|-----------|---------------------------|---------------------------|---------------|------------|------------------|
| | | | | | |

If sequential, state so and propose one parallelization opportunity.

---

**EDGE CASE TABLE** *(required -- C-08 + C-14)*

At least 2 edge cases distinct from per-phase exception tables above.

| EC-ID | Phase (Ph-ID) | Edge Case Name | Trigger | Why No Handler Exists | Consequence | SLA Risk |
|-------|--------------|---------------|---------|----------------------|------------|---------|
| EC-01 | | | | | | |
| EC-02 | | | | | | |
| ... | | | | | | |

SLA Risk column schema:
- Which phase SLA or At-Risk Threshold (from Lifecycle Phases table) is at risk
- Magnitude: expected additional elapsed time
- Classification: breach-level consequence OR delay

Leave no SLA Risk cell blank. "May affect timing" does not qualify.

---

**BOTTLENECK TABLE**

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link (Ph-ID) |
|------|--------------|----------------|-------|------------------|---------------------|
| B-01 | | | | | |
| B-02 | | | | | |

At least 2 bottlenecks with cause. Breach Link names the phase whose exit gate Scenario
breach = Y and that this bottleneck contributes to.

**GAP TABLE**

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|---------------|
| G-01 | | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Reached From (S-IDs + E-IDs) |
|------|--------------|------|------------|------------------------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | |
| ... | | | | |

Terminal gate: every S-ID and E-ID must either continue to another state or appear in
"Reached From."

---

**CROSS-LIFECYCLE DEPENDENCY TABLE** *(raise score)*

| Adjacent Lifecycle | Direction | Coupling State (S-ID or Ph-ID) | Artifact Passed | SLA Dependency |
|-------------------|-----------|-------------------------------|----------------|---------------|
| | sends to / receives from | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Variant Declaration > Lifecycle Phases > Role Registry > Phases (entry contract +
state table + decision table + exception table + exit gate per phase) > Exception Coverage
Audit > Parallel Path Table > Edge Case Table > Bottleneck Table > Gap Table > Terminal
Declaration > Cross-Lifecycle Dependency Table.

No table cell in a required column may be left blank. The SLA Risk column in the Edge Case
Table must reference a specific threshold from the Lifecycle Phases table. The Exception
Coverage Audit must account for every phase. Every path must reach a declared T-ID.

---

## V-05 -- Combined (Phrasing Register + Inertia Framing)

**Variation axes combined:**
1. Phrasing register -- conversational and scenario-led; the prompt asks questions rather than
   issuing structural commands, lowering the authoring barrier while still requiring specific
   answers
2. Inertia framing -- the as-is process is named as a comparator; C-13 is earned through the
   dual trace, not the exemption path

**Hypothesis:** The conversational + inertia combination from R1 V-04 proved effective at
generating rich exception and edge case content by framing the prompt as an expert practitioner
walkthrough. For R3, the two new criteria (C-14 and C-15) are embedded as explicit "before
you move on" checkpoint questions after the exception catalog and edge case sections. The
inertia framing (as-is/to-be dual trace) provides C-13 coverage structurally, and the
as-is process naturally surfaces edge cases that arise from legacy workarounds -- making
C-14's SLA risk attribution more concrete because the SLA breach scenario is traceable to
a known as-is gap rather than a hypothetical.

---

You are a seasoned domain expert who has worked this process long enough to know exactly
where it slows down, where it breaks, and what nobody documented. Walk through the full
lifecycle of the process described in the signal.

This walkthrough runs two layers: how the process works today (as-is) and how it should
work in the target state (to-be). At each stage you will be asked to compare both.

---

**Who's involved, and when do they show up?**

Tell me every person who touches this process. Give each a real job title for this specific
domain -- not "approver" but the named function (the Credit Analyst who checks the customer's
credit limit, the AP Clerk who matches the invoice to the PO, the Revenue Accountant who
reconciles and closes). For each role:
- When do they first enter the process?
- What is their primary action or decision?
- Does their role change between as-is and to-be? If so, how?

---

**What are the phases, and how long should each take?**

Before walking the steps, name the phases. A phase has a clear beginning, a clear "done"
condition, and someone accountable for it completing on time.

For each phase, answer:
- What is this phase trying to accomplish?
- What triggers it?
- How long does it normally take (as-is)? How long should it take (to-be)?
- Who is accountable if it runs over?
- What is the at-risk threshold -- when does running over start causing visible downstream
  problems?
- Does the process I'm tracing breach that threshold in either as-is or to-be? Say yes or no
  and explain why.

"It depends" is not an answer. Give me the number and the reason.

---

**Walk me through the process, phase by phase**

For each phase, run both layers:

*As-is:* How does this phase run today? Walk every step. At decision points: who decides,
what are the options, what happens if no one decides? At handoffs: what is passed, how is
it passed (email, system, paper), and what breaks if the handoff fails?

*To-be:* How does this phase run in the target state? What is automated? What manual steps
remain? For each step eliminated: what is the transition risk -- what breaks during the
switchover period before the automation is stable?

*Phase completion:* What has to be true for this phase to be done -- in both as-is and
to-be? Who confirms it? What record or event makes it official?

*Exception exits:* What can go wrong in this phase that sends the process off the normal
path? For each exception: what triggers it, how does it diverge, and where does it land?
How is it handled today (as-is)? How will it be handled in the target state (to-be)?

*Timing pressure:* What is the SLA for this phase? Does the scenario I'm tracing breach
the at-risk threshold? If yes, say why and say which bottleneck or exception caused the
breach.

---

**Before moving past exceptions: have I covered every phase?**

After describing the exceptions for all phases, stop and audit your exception coverage.
For each phase in your lifecycle:
- Does it have at least one exception flow?
- If not: what failure mode is invisible without an exception handler here? What happens
  downstream when that failure goes undetected?

If every phase has a handler, say so explicitly: "All [N] phases are covered; no exception
handler gaps identified."

Do not skip this audit. A lifecycle that traces rich exceptions for 3 of 5 phases without
noting the 2 uncovered phases fails C-15 on the rubric.

---

**The cases nobody wrote a rule for**

Every process has edge cases -- valid but rare situations that nobody planned for. After
walking all phases, name at least 2 that are distinct from the exception flows above
(those were documented failure paths; these are undocumented gaps).

For each edge case, answer:
- What triggers it?
- Why does the current process have no step for this? (What as-is assumption broke?)
- What goes wrong when it fires?
- Which phase SLA is at risk if this fires? How bad? Would it breach the threshold or just
  add delay? Name the specific phase and threshold you identified earlier.

This last question is required. "SLA may be affected" is not an answer. Name the phase,
name the threshold, say breach or delay.

---

**Where does time go?**

Now that you have walked the whole process, call out the 2 or 3 places where elapsed time
is the real risk. For each:
- Which phase and which step?
- What is the normal SLA and the at-risk threshold?
- What backs up behind it when it slips?
- In the scenario you traced, did this step breach its threshold in as-is? In to-be?
- Is this bottleneck eliminated, shifted, or residual in the to-be design?

---

**How does it end?**

List every way this process can terminate. For each terminal state:
- Success, failure, or cancellation?
- In as-is only, to-be only, or both?
- Which path leads here?

Every path you walked above must land on one of these named terminals.

---

**Connections to other processes**

If this process hands off to another process -- or if another process must complete before
this one can proceed -- describe the connection. What triggers the handoff? What information
moves? What does the receiving process need to see before it accepts? How does this
dependency differ between as-is and to-be?

---

**Write the artifact**

Produce the lifecycle artifact at `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

The artifact should read like a professional process analysis that an implementer, auditor,
or process owner could act on. Requirements:
- Every role must have a domain-qualified name (job function, not department).
- Every phase must have an SLA envelope, an at-risk threshold, and a scenario breach answer
  for both as-is and to-be.
- Every exception must have an SLA impact field with a quantitative or directional consequence.
- The exception coverage audit must appear as a distinct section accounting for every phase.
- Every edge case must include an SLA risk answer naming the specific phase, threshold, and
  breach-or-delay classification.
- Every bottleneck must carry an as-is / to-be trajectory (eliminated / shifted / residual)
  with a net-change assessment.
- Every path must reach a named terminal state.
- Every decision point must name the owner.
