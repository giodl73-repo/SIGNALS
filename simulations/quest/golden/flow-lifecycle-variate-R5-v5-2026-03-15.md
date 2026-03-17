---
skill: flow-lifecycle
round: 5
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v5-2026-03-15.md
---

# flow-lifecycle -- Round 5 Variations

Round 5 targets the three new v5 aspirational criteria, extracted from R4 V-03 and V-04
excellence signals:

- **C-20** Per-Step Sequential Gate Coverage -- sequential gates at >=3 distinct section
  boundaries distributed across the full schema; at minimum, gates guard role registry
  completion, phase table completion, and artifact production; each gate names the section
  it locks and the section it unlocks
- **C-21** Exception Flow Handling Role -- every named exception flow assigns a handling
  owner via a domain-qualified R-ID; exception catalog includes an owner/handler field,
  not just trigger + divergence + recovery
- **C-22** Production Gate Failure Declaration -- the production gate (C-19) contains an
  explicit inline failure mode declaration naming the consequence of violation ("is a
  structural fail," "must be discarded")

**R4 learning applied to R5 design:**
- R4 V-03 passed C-20 incidentally through imperative step-numbered structure: gates at
  "Do not proceed to Step 2 until Step 1 is complete," "You must complete this table before
  proceeding to Step 3," "Do not proceed to Step 4 until phase table is complete." V-01 and
  V-02 had zero or one gate -- C-13 cannot distinguish them, but C-20 can.
- R4 V-03 and V-04 passed C-21 through exception flow "Owner:" field and exception catalog
  "handling owner" column. V-01 and V-02 exception catalogs had trigger/divergence/recovery
  but no ownership assignment; they passed C-02 but failed C-21.
- R4 V-03 passed C-22 with "A Scan Summary that is OPEN when the artifact is written is a
  structural fail." V-01 and V-02 gates stated the condition ("may not be written until
  CLOSED") but did not name the failure consequence. The gate exists in all three (C-19
  passes); only V-03 names the consequence (C-22 passes).
- R5 primary risk for C-20: gates concentrated at one boundary only -- a single pre-write
  gate satisfies C-13 and C-19 but not C-20, which requires >=3 distinct boundaries. Gate
  count alone does not satisfy C-20; they must be distributed (role registry, phase table,
  artifact production -- not three gates all at the end).
- R5 primary risk for C-21: exception flows that name the phase owner or SLA owner as
  implicit handler. Phase owner != exception handler; the exception catalog must carry a
  Handler (R-ID) field explicitly, not a field that happens to contain a role.
- R5 primary risk for C-22: advisory language ("should be CLOSED," "confirm CLOSED before
  writing") states a condition without naming a consequence. C-22 requires the gate to
  declare what happens if violated, not just what status is required.

Single-axis: V-01 (Output Format: gate saturation at three boundaries, C-20 target),
V-02 (Role Sequence: exception ownership column, C-21 target),
V-03 (Phrasing Register: gate failure declaration, C-22 target).
Combined: V-04 (Output Format + Role Sequence: gates + exception ownership, C-20 + C-21),
V-05 (all three new axes + C-18/C-19 carry-through: full C-20/C-21/C-22 lock).

---

## V-01 -- Output Format Axis: Gate Saturation at Three Boundaries

**Variation axis:** Output format. Sequential "do not proceed" gates appear at exactly 3
distinct section boundaries, distributed across the full schema: (1) after Role Registry
-- blocks entry to PHASE TABLE; (2) after PHASE TABLE -- blocks entry to STATE TABLE;
(3) at artifact production -- blocks final write. Each gate explicitly names the section
it locks and the section it unlocks. The exception catalog carries trigger, divergence
phase, and recovery path only -- no Handler column (C-21 absent). The production gate
states the CLOSED requirement without naming a failure consequence (C-22 absent).

**Hypothesis:** C-20 requires gates at >=3 distinct boundaries. A schema with a single
pre-write gate satisfies C-13 (one gate) and C-19 (artifact-level gate) but fails C-20
because the gate is concentrated at one boundary. Distributing three named gates across
the schema creates a per-step handshake: the author cannot start phases before completing
roles, cannot trace states before completing phases, and cannot write the artifact without
closing the scan. This structural distribution is what C-20 counts. C-21 (exception
ownership) and C-22 (failure declaration) are absent to isolate the gate-count axis.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal.

---

**ROLE REGISTRY**

Declare domain-qualified roles before anything else. Generic labels (User, Approver, Owner,
Finance team, Management) are fails -- they do not count toward the 3-role minimum.

| R-ID | Role Name (domain-qualified -- e.g., "Senior Credit Analyst," "AP Clerk," "Revenue Accountant") | Functional Area | Decision Authority (measurable threshold) | SLA Accountable |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles.

**Gate 1 [Role Registry -> Phase Table]. Do not proceed to PHASE TABLE until Role Registry
is complete and every role has a domain-qualified title.**

---

**PHASE TABLE**

Identify all phases before tracing any states.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|-----------|--------------|---------------------|--------------|------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases. Each must aggregate >=2 states -- a 1:1 phase-to-state mapping does not
count. At least one At-Risk Threshold must name a causal bottleneck.

**Gate 2 [Phase Table -> State Table]. Do not proceed to STATE TABLE until Phase Table is
complete and every phase has a named entry trigger and completion condition.**

---

**STATE TABLE**

Minimum 6 states total across all phases.

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| | | | | | | | NORMAL / AT-RISK |

Every R-ID cited here must exist in the Role Registry.

---

**DECISION TABLE**

Minimum 3 decision points.

| D-ID | Decision Condition (measurable threshold -- "large amount" does not count) | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback (owner unavailable / system down / config missing) |
|------|------|------|------|------|------|
| | | | | | |

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state explicitly with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact (name phase SLA, magnitude, breach-or-delay) |
|------|--------------|---------------|------------------|----------------|-------------------------------------|------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

---

**EDGE CASE TABLE**

Minimum 2 edge cases distinct from exception catalog.

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

Minimum 2 bottlenecks (cause + impact). Minimum 1 gap (missing step + consequence).

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate 3 [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

---

## V-02 -- Role Sequence Axis: Exception Ownership Column

**Variation axis:** Role sequence + output format. Domain-qualified roles are the first
artifact produced. The exception catalog includes a mandatory Handler (R-ID) column that
assigns exception ownership to a domain-qualified role from the registry. The column header
carries the inline mandatory rule adjacent to the cell where ownership would be left blank.
Sequential gates: only one exists (before the final artifact write) -- C-20 is absent.
Production gate exists but contains no failure declaration (C-22 absent).

**Hypothesis:** C-21 requires every exception flow to assign a handling owner. The gap in
R4 V-01 and V-02 was that exception catalogs named trigger, divergence, and recovery
without assigning ownership. Adding a Handler (R-ID) column with inline mandatory
enforcement closes this gap structurally: the author cannot complete the exception row
without naming an owner. The column header placement makes the rule visible at the exact
cell being filled (C-18 compatible). C-20 (gate saturation at three boundaries) is absent
-- only one gate at artifact production -- to isolate the ownership axis. A single gate
is sufficient for C-13 but not C-20.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal.

Domain-qualified roles are the first artifact. No phase, state, or decision may reference
a role that does not appear in the Role Registry below.

---

**ROLE REGISTRY**

| R-ID | Role Name [Mandatory. "Approver," "Owner," "Manager," and "Finance team" are fails -- do not use them. Name the specific function: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | First Touch Point | Decision Authority | Exception Handler |
|------|------|------|------|------|------|
| R-01 | | | | | Y / N |
| R-02 | | | | | Y / N |
| R-03 | | | | | Y / N |

Minimum 3 roles. Mark at least one role as Y in Exception Handler.

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | SLA Owner (R-ID) | Risk Flag |
|-------|-----------|--------------|---------------------|--------------|-----------------|----------|
| PH-01 | | | | | | NORMAL / AT-RISK |
| PH-02 | | | | | | |
| PH-03 | | | | | | |
| PH-04 | | | | | | |

Minimum 4 phases. Each aggregates >=2 states. At least one AT-RISK flag with named causal
bottleneck.

---

**STATE TRACE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states. Every R-ID cited must exist in the Role Registry.

---

**DECISION POINTS**

Minimum 3 decision points. For each:

```
Decision: [name the question resolved here]
Owner: [R-ID from Role Registry]
Condition: [measurable threshold -- dollar amount, day count, retry limit; qualitative conditions do not count]
Branch A (condition met): --> [S-ID]
Branch B (condition not met): --> [S-ID]
Fallback (owner unavailable / system down / config missing): --> [holding state or escalation path]
```

---

**PARALLEL PATHS**

If parallel paths exist: name each path, join condition, and join owner (R-ID).
If sequential: state explicitly with rationale. Propose one parallelization opportunity
naming roles and states.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Handler (R-ID) [Mandatory. Every exception must be owned by a domain-qualified role from the Role Registry. Blank Handler is a fail -- it means the exception has no accountable owner.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact |
|------|--------------|---------------|------------------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause | Downstream Impact |
|------|------|--------------|------|-------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

---

**CROSS-LIFECYCLE HANDOFF**

Minimum 1 handoff.

```
Partner: [lifecycle name]
Direction: [outbound / inbound]
Coupling state: [S-ID or Ph-ID]
What passes: [artifact or record]
Coupling risk: [what fails if this handoff is late or malformed]
```

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | Reached From (S-IDs, E-IDs) |
|------|--------------|----------------------------------|------------------------------|
| T-01 | | | |
| T-02 | | | |

---

**TERMINAL VERIFICATION SCAN**

| Path | Last Node (S-ID or E-ID) | Terminal (T-ID) | Status (CLOSED / OPEN) |
|------|--------------------------|----------------|----------------------|
| Happy path | | | |
| Exception E-01 | | | |
| Exception E-02 | | | |
| Exception E-03 | | | |

**Scan Summary: [OPEN / CLOSED]**

**Artifact may not be written until Scan Summary shows status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Trace > Decision Points > Parallel Paths >
Exception Catalog > Edge Cases > Bottlenecks and Gaps > Cross-Lifecycle Handoff >
Terminal Declaration > Terminal Verification Scan.

---

## V-03 -- Phrasing Register Axis: Gate Failure Declaration

**Variation axis:** Phrasing register. The production gate contains an explicit failure mode
declaration inline within the gate sentence itself -- naming the consequence of violating
the gate. The format is step-numbered imperative throughout (R4 V-03 register, which proved
effective for C-19). Sequential gates: only the final step gate (production gate) -- C-20
is absent (only 1 gate, satisfies C-13 and C-19 but not C-20's >=3 boundary requirement).
Exception flows in step prose format include an Owner field, but it is a prose label ("Owner:
[R-ID]"), not a required table column with inline mandatory enforcement (C-21 marginal --
ownership is present in template but not column-enforced).

**Hypothesis:** C-22 is the difference between "artifact may not be written until CLOSED"
(condition only) and "artifact may not be written until CLOSED -- writing with an OPEN Scan
Summary is a structural fail and the output must be discarded" (condition + named
consequence). The consequence declaration changes the cognitive force: an author who sees
"is a structural fail" treats the gate as a hard stop, not an advisory. C-20 and column-
enforced C-21 are absent to isolate the phrasing axis. The question this variation answers:
does a failure declaration in the gate text change output quality when gate saturation and
column enforcement are not present?

---

You are a business-process simulation expert. Simulate the complete lifecycle of the
document or process named in the signal. Follow these steps in order.

---

**Step 1. Declare the lifecycle.**

State: (a) lifecycle type, (b) specific business scenario, (c) whether you are modeling a
single-state or as-is/to-be variant and why.

---

**Step 2. Establish domain-qualified roles.**

Name at least 3 roles. For each:

| R-ID | Role Title [Name the specific function at a real desk. Generic labels (User, Approver, Manager, Finance team) are fails.] | Functional Area | First Entry Point | Decision Authority |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Every decision gate, exception trace, and escalation in later steps must cite an R-ID
from this table.

---

**Step 3. Identify phases.**

Name at least 4 phases. Each must aggregate >=2 states.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Flag at least one phase AT-RISK with the causal bottleneck named.

---

**Step 4. Trace states.**

Name at least 6 states total.

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| | | | | | | | NORMAL / AT-RISK |

---

**Step 5. Name decision points.**

Name at least 3. For each:

```
Decision: [the question resolved at this fork]
Owner: [R-ID from Step 2]
Condition: [measurable threshold -- dollar amount, day count, retry limit; "needs review" is a fail]
Branch A (condition met): --> [S-ID]
Branch B (condition not met): --> [S-ID]
Fallback (owner unavailable / system down / config missing): --> [holding state or escalation path]
```

---

**Step 6. Identify parallel paths.**

If parallel paths exist: name each, join condition, join owner R-ID.
If sequential: state with rationale and propose one parallelization opportunity.

---

**Step 7. Trace exception flows.**

Name at least 3 exceptions spanning at least 2 distinct phases.

```
Exception: [name the specific failure mode -- not "system error"]
Phase: [Ph-ID]
Trigger: [specific condition in domain terms]
Divergence: [S-ID where normal flow exits]
Owner: [R-ID who detects or handles this]
Deviation: [which normal steps are skipped or replaced]
Recovery: [ordered S-IDs] OR Terminal: [T-ID]
```

---

**Step 8. Enumerate edge cases.**

Name at least 2, distinct from Step 7.

```
Edge case: [name]
Phase: [Ph-ID]
Scenario: [what happens and under what condition]
Gap reason: [what lifecycle assumption breaks here]
Consequence: [specific operational impact]
```

---

**Step 9. Identify bottlenecks and process gaps.**

At least 2 bottlenecks and 1 process gap.

```
Bottleneck: [name] | Phase: [Ph-ID] | Owner: [R-ID]
Cause: [domain-specific -- not "resource constraints"]
Downstream impact: [state or phase affected]
```

```
Process gap: [name]
Missing step: [what the lifecycle omits]
Consequence: [what breaks when this step is absent]
```

---

**Step 10. Note cross-lifecycle dependencies.**

At least 1 connection to a partner lifecycle.

```
Partner: [lifecycle name]
Direction: [outbound / inbound]
Coupling state: [S-ID or Ph-ID]
What passes: [artifact or record]
Coupling risk: [downstream failure if handoff is late]
```

---

**Step 11. Declare terminal states.**

At least 1 SUCCESS and 1 FAILURE.

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | Reached From (S-IDs, E-IDs) |
|------|--------------|----------------------------------|------------------------------|
| T-01 | | | |
| T-02 | | | |

---

**Step 12. Run the terminal verification scan.**

For every traced path, confirm it reaches a named terminal.

| Path | Last Node (S-ID or E-ID) | Terminal (T-ID) | Status (CLOSED / OPEN) |
|------|--------------------------|----------------|----------------------|
| Happy path | | | |
| Exception E-01 | | | |
| Exception E-02 | | | |
| Exception E-03 | | | |
| [all additional paths] | | | |

**Scan Summary: [OPEN / CLOSED]**

**Do not write the artifact until Scan Summary shows status CLOSED. Writing the artifact
when Scan Summary is OPEN is a structural fail -- the output is an incomplete lifecycle
trace where at least one path has no named terminal, and it must be discarded.**

---

**Step 13. Write the artifact.**

Only after Step 12 Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Sections: Lifecycle Context > Role Registry > Phase Table > State Trace > Decision Points >
Parallel Paths > Exception Flows > Edge Cases > Bottlenecks and Gaps > Cross-Lifecycle
Dependencies > Terminal Declaration > Terminal Verification Scan.

Pre-write checklist:
- Every R-ID cited in the body traces back to Step 2
- Every Entry/Exit Trigger names an actor or system event
- Every Decision Fallback is populated
- Scan Summary is CLOSED

---

## V-04 -- Combined: Gate Saturation + Exception Ownership (C-20 + C-21)

**Variation axes combined:**
1. Output format (gate saturation) -- sequential gates at >=4 distinct section boundaries:
   (1) role registry -> phase table; (2) phase table -> state table; (3) exception catalog
   -> terminals; (4) scan summary -> artifact; each gate names section locked and section
   unlocked
2. Role sequence (exception ownership) -- exception catalog includes mandatory Handler
   (R-ID) column; exception ownership is enforced as a table field with inline rule; a gate
   after the exception catalog blocks forward progress until every handler cell is populated

**Hypothesis:** V-01 achieves C-20 (3 gates distributed across boundaries) without
exception ownership -- C-21 fails. V-02 achieves C-21 (handler column in exception catalog)
without gate saturation -- C-20 fails. Combining them creates mutual enforcement: the gate
before the exception section cannot be satisfied until every exception handler is named;
the gate after the exception section enforces that the Handler column is complete before
the author moves to terminals. The combination may produce more consistent C-21 compliance
than a handler column alone, because the gate creates a hard stop -- the author cannot
proceed without completing the handler field. C-22 (failure declaration) is absent in the
production gate to isolate the C-20 + C-21 combination from the phrasing axis.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal.

---

**ROLE REGISTRY**

Domain-qualified roles are established first. Generic labels (Approver, Owner, Manager,
Finance team) do not count toward the minimum.

| R-ID | Role Name [Mandatory. Name the specific function at a real desk. Generic labels are fails.] | Functional Area | Decision Authority (measurable threshold) | Exception Handler |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles. Mark at least one as Exception Handler Y.

**Gate 1 [Role Registry -> Phase Table]. Do not proceed to PHASE TABLE until Role Registry
is complete, every role has a domain-qualified title, and at least one exception handler
is marked Y.**

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger [name the specific event -- "after prior phase ends" does not count] | Completion Condition [name what "done" looks like -- "when complete" does not count] | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases, each aggregating >=2 states. At least one At-Risk Threshold carries a
named causal bottleneck.

**Gate 2 [Phase Table -> State Table]. Do not proceed to STATE TABLE until Phase Table is
complete and every phase has a named entry trigger, completion condition, and SLA envelope.**

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states. Every R-ID cited must exist in the Role Registry.

---

**DECISION TABLE**

| D-ID | Decision Condition (measurable threshold) | Owner (R-ID) | Branch A (condition met) | Branch B (condition not met) | Fallback (owner unavailable / system down / config missing) |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points. Every Fallback cell must be populated.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Handler (R-ID) [Mandatory. Cite a domain-qualified R-ID from the Role Registry. Blank is a fail -- an exception without a named handler has no accountable owner.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact (phase SLA + magnitude + breach-or-delay) |
|------|--------------|---------------|------------------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Gate 3 [Exception Catalog -> Terminals]. Do not proceed to TERMINAL DECLARATION until
every exception row has a Handler (R-ID) populated. An exception without an owner is a
structural gap.**

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State | SLA Dependency |
|-------------------|-----------|----------------|----------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate 4 [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

---

## V-05 -- Full Lock: C-20 + C-21 + C-22 + C-18/C-19 Carry-Through

**Variation axes combined:**
1. Output format (gate saturation) -- sequential gates at >=4 distinct section boundaries
   (role registry, phase table, exception catalog, artifact production); each gate names
   section locked and section unlocked; satisfies C-20 and C-13
2. Role sequence (exception ownership) -- exception catalog Handler (R-ID) column with
   inline mandatory enforcement in column header; gate after exception catalog enforces
   completion; satisfies C-21
3. Phrasing register (failure declaration) -- production gate contains inline failure
   consequence declaration naming what happens if the gate is violated; satisfies C-22
4. C-18 carry-through -- anti-pattern negation rules embedded inside schema column headers
   at point of use, not collected in preamble; >=2 inline negation locations
5. C-19 carry-through -- two-table scan (per-state + per-exception) with explicit CLOSED
   status condition; the gate operates at artifact completion

**Hypothesis:** R4 V-03 achieved C-18, C-19, C-20, C-21, and C-22 incidentally through
imperative step-numbered structure. V-05 in R5 is the explicit reference implementation:
each criterion is addressed by a named structural decision, not an emergent property of
the format. C-20 is addressed by four named gates at four boundaries. C-21 is addressed by
a mandatory Handler column and a gate that enforces its completion. C-22 is addressed by
a gate sentence that names the violation consequence. C-18 is addressed by negation rules
embedded in column headers at the constrained cell. C-19 is addressed by two scan tables
and a CLOSED status condition on the production gate. V-05 answers: what does a prompt
look like when every criterion from C-18 through C-22 is deliberately designed in?

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every section in order. Each gate must be
satisfied before the next section opens.

---

**ROLE REGISTRY**

Domain-qualified roles must be established before any phase, state, decision, or exception
is named. No R-ID may be cited in any later section that does not appear here.

| R-ID | Role Name [Mandatory. "Approver," "Owner," "Manager," and "Finance team" are fails -- do not use them. Name the function at a specific desk: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | Decision Authority [Mandatory. "Owns approvals" does not count -- name the decision type and measurable threshold: "PO approval up to $50K," "Invoice exception hold <=3 business days."] | Exception Handler |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles. At least one marked Exception Handler Y.

**Gate 1 [Role Registry -> Phase Table]. Do not proceed to PHASE TABLE until Role Registry
is complete: every role has a domain-qualified title, a measurable decision authority, and
the exception handler column is populated. An incomplete Role Registry is a structural fail
-- phases written before roles are anchored produce uncitable R-IDs downstream.**

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger [Mandatory. "After prior phase ends" does not count -- name the specific event or artifact state that triggers entry.] | Completion Condition [Mandatory. "When everything is done" does not count -- name what "done" looks like in observable terms.] | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases. Each aggregates >=2 states -- a 1:1 phase-to-state mapping does not
count. At least one At-Risk Threshold names a causal bottleneck.

**Gate 2 [Phase Table -> State Table]. Do not proceed to STATE TABLE until Phase Table is
complete: every phase has a named entry trigger, completion condition, SLA envelope, and
at least one AT-RISK phase is marked with a causal bottleneck. Writing states before
phases are fully defined produces states that cannot be correctly phase-attributed.**

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) [Mandatory. Cite an R-ID from the Role Registry. Blank owner is a fail -- every state must have an accountable role.] | Entry Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event causing entry.] | Exit Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event causing exit.] | SLA Window | Risk |
|------|-----------|-------------|------|------|------|------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states total across all phases.

---

**DECISION TABLE**

| D-ID | Decision Condition [Mandatory. "Large amount" and "needs review" do not count -- state a measurable threshold: dollar amount, day count, retry limit, or policy code.] | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback [Mandatory. Blank is a structural fail -- name the holding state or escalation path for: owner unavailable, system down, configuration missing.] |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale. Propose one parallelization opportunity naming roles
and states.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition [Mandatory. "System error" and "data issue" do not count -- name the specific failure mode in domain terms.] | Divergence S-ID | Handler (R-ID) [Mandatory. Every exception must be owned by a domain-qualified role from the Role Registry. Blank is a fail -- it means no role is accountable for recovery.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact [Mandatory. "May cause delays" does not count -- name the phase SLA, magnitude (e.g., "+3 business days"), and whether this is a breach or a delay.] |
|------|--------------|---------------|------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Gate 3 [Exception Catalog -> Terminals]. Do not proceed to TERMINAL DECLARATION until
every exception row has a Handler (R-ID) populated. An exception without a named handler
is a structural fail -- it produces an exception path with no accountable owner, which is
a process gap, not an edge case.**

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason (why no handler exists) | Consequence |
|-------|--------------|---------|-----------------------------------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific -- "resource constraints" does not count) | Downstream Impact |
|------|------|--------------|------|----------------------------------------------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

Minimum 2 bottlenecks (cause + downstream impact). Minimum 1 gap (missing step +
consequence of absence).

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

For every S-ID in the State Table, confirm it continues to a named state or appears in a
terminal's Reached From column.

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

For every E-ID in the Exception Catalog, confirm the recovery path or terminal is named.

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate 4 [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED. Writing the artifact when Scan Summary is OPEN is a structural fail -- it
produces an incomplete lifecycle trace where at least one path has no named terminal, and
that artifact must be discarded.**

---

**OUTPUT**

Only after Gate 4 is satisfied (Scan Summary CLOSED): write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

Pre-write checklist (confirm before writing):
- Every R-ID cited in the document traces back to the Role Registry
- Every Entry/Exit Trigger in State Table names an actor or system event (not "then X happens")
- Every Decision Fallback cell is populated
- Every Exception Handler cell carries a domain-qualified R-ID
- Scan Summary Overall Status is CLOSED
