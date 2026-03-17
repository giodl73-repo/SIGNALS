---
skill: flow-lifecycle
round: 4
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v4-2026-03-15.md
---

# flow-lifecycle -- Round 4 Variations

Round 4 targets the two new v4 aspirational criteria, both traced to V-05 (combined axis)
from R3:
- **C-18** Schema-Inline Anti-Pattern Placement -- anti-pattern negation rules ("does not count,"
  "Mandatory," "is a fail") embedded inside schema section headers or cell definitions, not
  collected in a preamble; point-of-use enforcement adjacent to the element constrained
- **C-19** Artifact-Level Production Gate -- explicit pre-write gate blocks final artifact
  output until all verification scans show CLOSED status; distinct from C-13 (criterion
  ordering) by operating at the artifact completion boundary

**R3 learning applied to R4 design:**
- R3 V-05 locked C-18 via negations inside Phase Delta header ("Mandatory. Replacing with prose
  is a fail.") and "does not count" rules inside Entry/Exit Contract cells. V-01 through V-04
  collected negations in preamble and failed C-18. The test: does a reader see the rule at the
  cell they are filling, without scrolling?
- R3 V-05 locked C-19 via Scan Table A (per-state T-ID or OPEN) + Scan Table B
  (per-exception T-ID or OPEN) + closing gate: "artifact may not be written until Scan Summary
  shows status CLOSED." C-14 is a per-path structural confirmation; C-19 is an artifact-level
  output block -- they can both pass or fail independently.
- R4 primary risk: anti-patterns placed in a dedicated "Anti-Pattern Rules" section header
  rather than inside the schema block for the element they constrain. That is preamble by
  another name and fails C-18.
- R4 secondary risk: verification steps described as narrative ("verify all paths reach a
  terminal") without a named scan artifact and CLOSED status condition. That fails C-19
  specifically because there is no named artifact to show CLOSED.

Single-axis: V-01 (output format: table-header inline enforcement), V-02 (role sequence:
role-registry inline enforcement), V-03 (phrasing register: imperative with point-of-use
negations).
Combined: V-04 (role sequence + output format: inline anti-patterns in two schema locations),
V-05 (role sequence + output format + scan tables + artifact gate: full C-18/C-19 lock).

---

## V-01 -- Output Format Axis

**Variation axis:** Output format. Every structural section uses a table schema. Anti-pattern
negation rules are embedded inline within table column headers adjacent to the element they
constrain -- not in a preamble or dedicated warning block. A two-table terminal scan
(per-state + per-exception) with an explicit CLOSED status gate blocks final artifact output.

**Hypothesis:** C-18 fails when negation rules are collected in a preamble because they are
read once and invisible during authoring. Placing "does not count" / "is a fail" language
inside the column header keeps the constraint visible at the exact cell being filled -- a
reader authoring the Entry Trigger cell sees "then X happens is a fail" without leaving that
row. C-19 fails when verification is advisory narrative; a scan table with a named CLOSED
status requirement makes skipping structurally visible -- a blank or OPEN cell in the Scan
Summary is a concrete fail signal, not an inference.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

---

**LIFECYCLE PHASES**

Identify all phases before tracing any states.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|-----------|--------------|---------------------|--------------|------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Rules: minimum 4 phases; each aggregates >=2 states (a 1:1 phase-to-state mapping does not
count); at least one At-Risk Threshold cell carries a named causal bottleneck.

---

**ROLE REGISTRY**

| R-ID | Role Name [Mandatory. Generic labels such as "Approver," "Owner," "Manager," or "Finance team" do not count. Name the function: the person at a real desk doing a specific thing -- e.g., "Senior Credit Analyst," "AP Clerk," "Revenue Accountant."] | Phases Active | Decision Authority [Mandatory. "Owns approvals" does not count. Name the decision type and measurable threshold, e.g., "PO approval up to $50K."] |
|------|------|------|------|
| R-01 | | | |
| R-02 | | | |
| R-03 | | | |

Minimum 3 roles. Every decision gate, exception handler, and escalation path cites an R-ID
from this table.

---

**FOR EACH PHASE -- repeat this block for every Ph-ID:**

---

**PHASE ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Entry Condition [Mandatory. "After Phase N completes" does not count -- name the specific event or artifact state that triggers entry.] | Prior Phase (Ph-ID or INITIAL) | Objects Entering | SLA Clock Start | Exception Pre-Check |
|------|------|------|------|------|
| | | | | |

---

**STATE TABLE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Owner (R-ID) | Entry Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event that causes entry into this state.] | Exit Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event that causes the state to change.] | Exception Exit (E-ID or "none") |
|------|-----------|-------------|------|------|------|
| | | | | | |

Minimum 6 states total across all phases.

---

**DECISION TABLE -- [Ph-ID: Phase Name]**

| D-ID | Decision Condition [Mandatory. Qualitative conditions such as "large amount" or "needs review" do not count -- state a measurable threshold: dollar amount, day count, retry limit, or policy code.] | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback [Mandatory. A blank Fallback is a structural fail -- name the holding state or escalation path for: owner unavailable, system down, or configuration missing.] |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PHASE EXIT GATE -- [Ph-ID: Phase Name]**

| Exit Condition | Success Transition | Failure Transition (T-ID or exception) | SLA At-Risk Threshold | Scenario Breach (Y/N) | Breach Cause (if Y: traceable to S-ID or E-ID) |
|---------------|-------------------|----------------------------------------|-----------------------|----------------------|------------------------------------------------|
| | | | | | |

---

*Repeat entry contract + state table + decision table + exit gate for each phase.*

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state explicitly with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact [Mandatory. "May cause delays" does not count -- name the phase SLA, the magnitude (e.g., "+3 business days"), and whether this is a breach or a delay.] |
|------|--------------|---------------|------------------|----------------|-------------------------------------|------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

---

**EDGE CASE TABLE**

Minimum 2 edge cases distinct from the exception catalog.

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason (why the lifecycle has no handler) | Consequence |
|-------|--------------|---------|-----------------------------------------------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

Minimum 2 bottlenecks with cause and downstream impact. Minimum 1 gap naming the missing step
and the consequence of its absence.

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

For every S-ID in the state tables, confirm it either continues to a named state or appears
in a terminal's Reached From column.

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

For every E-ID in the exception catalog, confirm the recovery or terminal is named.

| E-ID | Exception Name | Recovery S-ID (or first in sequence) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Artifact may not be written until Scan Summary shows status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Phases > Role Registry > Per-Phase Blocks (entry contract + state table +
decision table + exit gate) > Parallel Path Table > Exception Catalog > Edge Case Table >
Bottleneck and Gap Table > Cross-Lifecycle Dependency > Terminal Declaration > Scan Table A >
Scan Table B > Scan Summary.

No required column may be left blank. Decision Fallback column must be populated on every row.
SLA Impact in exception catalog must name phase SLA, magnitude, and breach-or-delay
classification. Scan Summary must show CLOSED before artifact is written.

---

## V-02 -- Role Sequence Axis

**Variation axis:** Role sequence. Domain-qualified roles are the first artifact produced,
before any phase, state, or decision is named. The role registry schema header carries the
generic-label anti-pattern inline: the Role Name column header contains the negation rule
adjacent to the cell where a generic label would appear. A named terminal verification scan
with explicit CLOSED gate blocks artifact output.

**Hypothesis:** C-11 requires role-first anchoring; C-18 requires inline anti-pattern placement
adjacent to the constrained element. Embedding the generic-label rule inside the Role Name
column header satisfies both from a single structural decision. A separate "Anti-Pattern
Rules" section satisfies neither: it is preamble-by-another-name for C-18, and it precedes
rather than anchors the role content for C-11. The handoff-sequence structure naturally
organizes all downstream content by role, making orphan roles and uncited decision owners
structurally visible rather than narratively described.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Domain-qualified roles are the first artifact. Everything in this document -- phases, states,
decisions, exceptions, terminals -- references a Role ID from the registry below. No R-ID may
be cited that does not appear in this table.

---

**ROLE REGISTRY**

| R-ID | Role Name [Mandatory. Generic labels such as "Approver," "Owner," "Manager," or "Finance team" do not count -- is a fail. Use the named function: the person at a specific desk doing a specific task, e.g., "Senior Credit Analyst," "AP Clerk," "Revenue Accountant," "Procurement Category Manager."] | Functional Area | First Touch Point in Lifecycle | Decision Authority | SLA Accountable? |
|------|------|------|------|------|------|
| R-01 | | | | | Y / N |
| R-02 | | | | | Y / N |
| R-03 | | | | | Y / N |

Minimum 3 roles. At least one Y per phase in SLA Accountable.

**Do not proceed to phases until the Role Registry is complete.**

---

**PHASE TABLE**

Introduce phases in the order roles hand off the process object.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | SLA Owner (R-ID) | Risk Flag |
|-------|-----------|--------------|---------------------|--------------|-----------------|----------|
| PH-01 | | | | | | NORMAL / AT-RISK |
| PH-02 | | | | | | |
| PH-03 | | | | | | |
| PH-04 | | | | | | |

Minimum 4 phases. Each aggregates >=2 states. At least one AT-RISK flag with named causal
bottleneck.

---

**STATE TRACE** *(in handoff order)*

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| S-01 | | | | | | | NORMAL / AT-RISK |
| S-02 | | | | | | | |

Minimum 6 states. Every R-ID cited here must exist in the Role Registry.

---

**DECISION POINTS**

For each decision gate:

```
Decision: [the question resolved at this fork]
Owner: [R-ID from Role Registry -- a decision point with no owner R-ID does not count toward the 3-decision minimum]
Condition (threshold): [measurable threshold -- e.g., "Invoice total >= $50,000" or "Days since submission > 5"; qualitative conditions do not count]
Branch A (condition met): --> [S-ID or T-ID]
Branch B (condition not met): --> [S-ID or T-ID]
Fallback (owner unavailable / system down / config missing): --> [holding state S-ID or escalation R-ID and path]
```

Minimum 3 decision points.

---

**PARALLEL PATHS**

If parallel paths exist:

```
Fork: [S-ID]
Branch A: [activity + R-ID]
Branch B: [activity + R-ID]
Join condition: [what must be true before merge]
Join owner: [R-ID]
Downstream: [S-ID after merge]
```

If sequential: state explicitly with rationale. Propose one parallelization opportunity.

---

**EXCEPTION FLOWS**

Minimum 3 exceptions spanning at least 2 distinct phases.

```
Exception: [name] (E-ID: E-0X)
Phase: [Ph-ID]
Triggering condition: [specific -- not "system error" but the named failure mode]
Divergence state: [S-ID where normal path exits]
Handling owner: [R-ID who detects or responds]
Deviation: [which normal steps are skipped or replaced]
Recovery: [S-ID or ordered sequence] or Terminal: [T-ID]
```

---

**EDGE CASES**

Minimum 2 edge cases distinct from exception flows.

```
Edge case: [name] (EC-ID: EC-0X)
Phase: [Ph-ID]
Scenario: [what condition produces this path]
Gap reason: [what lifecycle assumption breaks here]
Consequence: [specific operational impact -- not "errors may occur"]
```

---

**BOTTLENECKS AND GAPS**

```
Bottleneck: [name] (B-ID: B-0X)
Phase: [Ph-ID] | Owner most accountable: [R-ID]
Cause: [domain-specific -- name the constraint]
Downstream impact: [which state or phase is directly affected]
```

```
Process gap: [name] (G-ID: G-0X)
Missing step: [what the lifecycle omits]
Why required: [what real-world execution cannot complete without this]
Consequence of absence: [specific failure]
```

Minimum 2 bottlenecks, minimum 1 process gap.

---

**CROSS-LIFECYCLE HANDOFF**

Minimum 1 handoff.

```
Handoff: [name]
Direction: [outbound / inbound]
Partner lifecycle: [name]
Coupling state: [S-ID or Ph-ID]
What passes: [artifact, record, or status event]
Coupling risk: [downstream failure if handoff is late or malformed]
```

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | Reached From (S-IDs, E-IDs) |
|------|--------------|----------------------------------|------------------------------|
| T-01 | | | |
| T-02 | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**TERMINAL VERIFICATION SCAN**

| Path | Last Node (S-ID or E-ID) | Terminal (T-ID) | Status (CLOSED / OPEN) |
|------|--------------------------|----------------|----------------------|
| Happy path | | | |
| Exception E-01 | | | |
| Exception E-02 | | | |
| Exception E-03 | | | |
| [all additional traced paths] | | | |

**Scan Summary: [OPEN / CLOSED]**

**Artifact may not be written until Scan Summary shows status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Trace > Decision Points > Parallel Paths >
Exception Flows > Edge Cases > Bottlenecks and Gaps > Cross-Lifecycle Handoff > Terminal
Declaration > Terminal Verification Scan.

All R-IDs cited in the body trace back to the Role Registry. Every decision Fallback names
a state or escalation path. Scan Summary is CLOSED before the artifact is written.

---

## V-03 -- Phrasing Register Axis

**Variation axis:** Phrasing register -- imperative and directive throughout. Section
definitions issue commands ("Name exactly," "You must," "Do not use"). Anti-pattern negation
rules appear inline at each field definition, not in a preamble or dedicated rules block.
The output command is a conditional directive: "Do not write the artifact until status is
CLOSED."

**Hypothesis:** Descriptive prompts ("include roles with domain context") leave gap space
the author fills with minimal specificity. Imperative prompts with inline negation
("Name the function: AP Clerk. Finance team is a fail") close the gap at authoring time,
not at review time. Inline negation at the field definition achieves C-18 because the
constraint is adjacent to the constrained cell -- the author cannot fill the Entry Trigger
cell without the "then X happens is a fail" instruction in view. The directive output gate
achieves C-19 by framing non-compliance as a structural violation that produces an invalid
artifact, not as an advisory reminder.

---

You are a business-process simulation expert. Simulate the complete lifecycle of the document
or process named in the signal. Follow these steps in order. Do not proceed to a step until
the prior step is fully complete.

---

**Step 1. Declare the lifecycle.**

State: (a) lifecycle type, (b) specific scenario, (c) single-state or as-is/to-be framing,
(d) if single-state: why no variant comparison applies.

Do not proceed to Step 2 until Step 1 is complete.

---

**Step 2. Establish domain-qualified roles.**

You must name at least 3 roles. For each, use this table:

| R-ID | Role Title [You must name the specific function at a real desk. "Finance team," "Approver," and "Management" are fails -- do not use them. Use: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | When They First Enter | What They Decide or Act On |
|------|------|------|------|------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

You must complete this table before proceeding to Step 3. Every R-ID cited in later steps
must appear here.

---

**Step 3. Identify phases.**

You must name at least 4 phases.

| Ph-ID | Phase Name | Entry Trigger [You must name the specific event -- not "after the prior phase ends."] | Completion Condition [You must name what "done" looks like -- not "when everything is complete."] | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Each phase must aggregate at least 2 states. A 1:1 phase-to-state mapping does not count.
You must flag at least one phase AT-RISK and name the bottleneck causing the risk.

Do not proceed to Step 4 until the phase table is complete.

---

**Step 4. Trace states.**

You must produce at least 6 states total across all phases.

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) [You must cite an R-ID from Step 2. A blank or uncited owner is a fail.] | Entry Trigger [You must name the actor or system event. "Then X happens" is a fail.] | Exit Trigger [You must name the actor or system event. "Then X happens" is a fail.] | SLA Window | Risk |
|------|-----------|-------------|------|------|------|------|------|
| | | | | | | | NORMAL / AT-RISK |

---

**Step 5. Name decision points.**

You must name at least 3. Use this format for each:

```
Decision: [name the question resolved here]
Owner: [R-ID from Step 2 -- you must cite a valid R-ID]
Condition: [name the measurable threshold -- dollar amount, day count, retry limit.
  "Needs review" and "large amount" are fails -- do not use them.]
Branch A (condition met): --> [S-ID]
Branch B (condition not met): --> [S-ID]
Fallback [You must name what happens when the decision cannot be made. A blank Fallback
  is a structural fail. Cover: owner unavailable, system down, configuration missing.]:
  --> [holding state S-ID or escalation R-ID and next action]
```

---

**Step 6. Identify parallel paths.**

If parallel paths exist, name each path, its join condition, and the join owner R-ID.
If sequential, state that explicitly with rationale. Propose one parallelization opportunity
naming the roles and states.

---

**Step 7. Trace exception flows.**

You must trace at least 3 exceptions spanning at least 2 distinct phases.

```
Exception: [name it precisely -- not "system error" but the specific failure mode]
Phase: [Ph-ID]
Trigger: [the specific condition in domain terms]
Divergence: [S-ID where normal flow exits]
Owner: [R-ID who detects or handles this -- must be from Step 2]
Deviation: [which steps are skipped or replaced]
Recovery: [ordered S-IDs] OR Terminal: [T-ID]
```

---

**Step 8. Enumerate edge cases.**

You must name at least 2 edge cases distinct from Step 7.

```
Edge case: [name it]
Phase: [Ph-ID]
Scenario: [what happens and under what condition]
Gap reason: [what lifecycle assumption this violates]
Consequence: [specific operational impact -- "errors may occur" is not an answer]
```

---

**Step 9. Identify bottlenecks and process gaps.**

You must name at least 2 bottlenecks and at least 1 process gap.

Bottleneck format:
```
Name: [name] | Phase: [Ph-ID] | Owner most accountable: [R-ID]
Cause: [domain-specific -- not "resource constraints" but the named constraint]
Downstream impact: [which state or phase is affected and how]
```

Gap format:
```
Missing step: [name what is absent]
Why required: [what real-world execution needs this step to do]
Consequence: [what breaks when this step is missing]
```

---

**Step 10. Note cross-lifecycle dependencies.**

Name at least 1 connection to a partner lifecycle.

```
Partner: [lifecycle name]
Direction: [outbound from this lifecycle / inbound trigger from partner]
Coupling state: [S-ID or Ph-ID in this lifecycle]
What passes: [the artifact or record]
Coupling risk: [what fails if this handoff is late or malformed]
```

---

**Step 11. Declare terminal states.**

You must include at least 1 SUCCESS and at least 1 FAILURE terminal.

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | Reached From (S-IDs, E-IDs) |
|------|--------------|----------------------------------|------------------------------|
| T-01 | | | |
| T-02 | | | |

---

**Step 12. Run the terminal verification scan. Do not skip this step.**

For every path traced, verify it reaches a named terminal.

| Path | Last Node (S-ID or E-ID) | Terminal (T-ID) | Status (CLOSED / OPEN) |
|------|--------------------------|----------------|----------------------|
| Happy path | | | |
| Exception E-01 | | | |
| Exception E-02 | | | |
| Exception E-03 | | | |
| [all additional paths] | | | |

**Scan Summary: [OPEN / CLOSED]**

**Do not write the artifact until every row shows CLOSED and Scan Summary is CLOSED.**
A Scan Summary that is OPEN when the artifact is written is a structural fail.

---

**Step 13. Write the artifact.**

Only after Step 12 Scan Summary is CLOSED: produce the lifecycle artifact at
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Sections in order: Lifecycle Context > Role Registry > Phase Table > State Trace > Decision
Points > Parallel Paths > Exception Flows > Edge Cases > Bottlenecks and Gaps >
Cross-Lifecycle Dependencies > Terminal Declaration > Terminal Verification Scan.

Pre-write checklist (confirm before writing):
- Every R-ID cited in the body traces back to Step 2
- Every Entry/Exit Trigger names an actor or system event
- Every Decision Fallback is populated
- Scan Summary is CLOSED

---

## V-04 -- Combined: Role Sequence + Output Format

**Variation axes combined:**
1. Role sequence -- domain-qualified roles established before any phase or state; role registry
   schema header carries the generic-label anti-pattern inline (C-11 + first C-18 location)
2. Output format -- table-dominant throughout; state table carries a second inline anti-pattern
   in the Entry/Exit Trigger column headers (second C-18 location); two-table scan (per-state +
   per-exception) with explicit CLOSED gate achieves C-19

**Hypothesis:** V-02 achieves C-18 via the role registry header alone -- one inline negation
location. V-01 achieves C-18 via state and decision table headers -- two inline negation
locations. Combining them places inline enforcement in two schema locations (role registry +
state table), exceeding the >=2 C-18 threshold with structural redundancy. A reader authoring
the Role Name cell sees the generic-label rule; a reader authoring the Entry Trigger cell sees
the "then X happens" rule -- neither rule requires scrolling back to a preamble. The scan
tables (V-01's pattern) achieve C-19. Together these axes cover C-11, C-18, and C-19 without
Phase Delta blocks.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Domain-qualified roles are the first artifact produced. No phase, state, or decision may be
named before the Role Registry is complete.

---

**ROLE REGISTRY**

| R-ID | Role Name [Mandatory. Generic labels such as "Approver," "Owner," "Manager," or "Finance team" do not count -- is a fail. Name the specific function: "AP Clerk," "Senior Credit Analyst," "Revenue Accountant," "Procurement Category Manager."] | Functional Area | First Touch Point | Decision Authority [Mandatory. "Reviews and approves" does not count. State the decision type and threshold, e.g., "Approves invoices up to $50K; routes above to VP Finance."] | SLA Accountable? |
|------|------|------|------|------|------|
| R-01 | | | | | Y / N |
| R-02 | | | | | Y / N |
| R-03 | | | | | Y / N |

Minimum 3 roles. At least one SLA Accountable = Y per phase. No R-ID may be cited downstream
that does not appear here.

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold | SLA Owner (R-ID) |
|-------|-----------|--------------|---------------------|--------------|------------------|-----------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |
| PH-04 | | | | | | |

Minimum 4 phases. Each aggregates >=2 states. At least one At-Risk entry with named bottleneck.

---

**STATE TABLE** *(all phases, in handoff order)*

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event that causes entry into this state.] | Exit Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event.] | SLA Window | Risk |
|------|-----------|-------------|-------------|------|------|------|------|
| S-01 | | | | | | | NORMAL / AT-RISK |
| S-02 | | | | | | | |

Minimum 6 states. Every Owner R-ID traces to the Role Registry.

---

**DECISION TABLE**

| D-ID | Decision Question | Owner (R-ID) | Condition [Mandatory. Name a measurable threshold: dollar amount, day count, retry count. "Needs review" does not count.] | Branch A (met: S-ID) | Branch B (not met: S-ID) | Fallback [Mandatory. Name holding state or escalation path for: owner unavailable, system down, config missing. A blank Fallback does not count.] |
|------|------------------|-------------|------|------|------|------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

---

**PHASE EXIT GATE TABLE**

| Ph-ID | Phase Name | Exit Condition | Success Transition | Failure Transition (T-ID) | SLA Breach Threshold | Scenario Breach (Y/N) | Breach Cause (if Y) |
|-------|-----------|---------------|-------------------|--------------------------|---------------------|----------------------|---------------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |
| PH-04 | | | | | | | |

At least one Y breach verdict with cause traceable to a named S-ID or bottleneck.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: declare explicitly with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Handling Owner (R-ID) | Deviation from Normal Flow | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact [Mandatory. "May cause delays" does not count -- name the phase SLA, the magnitude, and breach vs. delay classification.] |
|------|--------------|---------------|------------------|----------------|----------------------|---------------------------|-------------------------------------|------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

---

**EDGE CASE TABLE**

Minimum 2 edge cases distinct from the exception catalog.

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK TABLE**

| B-ID | Phase (Ph-ID) | Name | Cause | Downstream Impact |
|------|--------------|------|-------|------------------|
| B-01 | | | | |
| B-02 | | | | |

**PROCESS GAP TABLE**

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Consequence of Absence |
|------|--------------|-------------|--------------|----------------------|
| G-01 | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY TABLE**

| Adjacent Lifecycle | Direction | Coupling State (S-ID or Ph-ID) | What Passes | SLA Dependency |
|-------------------|-----------|-------------------------------|------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION TABLE**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID (or first in sequence) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A | | | |
| Scan Table B | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Artifact may not be written until Scan Summary shows status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Phase Exit Gate Table >
Parallel Path Table > Exception Catalog > Edge Case Table > Bottleneck Table > Process Gap
Table > Cross-Lifecycle Dependency > Terminal Declaration > Scan Table A > Scan Table B >
Scan Summary.

No required column may be left blank. Every R-ID cited in any table traces to the Role
Registry. Every Decision Fallback is populated. Every Exception SLA Impact names a specific
phase, magnitude, and breach-or-delay classification. Scan Summary is CLOSED before artifact
is written.

---

## V-05 -- Combined: Role Sequence + Schema-Inline Anti-Patterns + Scan Tables + Artifact Gate

**Variation axes combined:**
1. Role sequence -- domain-qualified roles anchor all downstream content; role registry schema
   header carries inline anti-pattern at the Role Name column (C-11, first C-18 location)
2. Output format -- per-phase Phase Delta blocks; state table header carries a second inline
   anti-pattern at the Entry/Exit Trigger columns (second C-18 location); decision table
   Condition column carries a third inline anti-pattern for quantification (C-17 + C-18)
3. Lifecycle emphasis -- per-phase Phase Delta blocks (entry contract, exit gate, SLA envelope,
   breach verdict) provide the phase structure required for C-16; phases declared before states
4. Artifact-level production gate -- Scan Table A (per-state T-ID or OPEN) + Scan Table B
   (per-exception T-ID or OPEN) + closing gate: "artifact may not be written until Scan
   Summary shows status CLOSED" -- the exact language pattern that achieves C-19

**Hypothesis:** C-18 requires >=2 inline negation rules inside schema definitions, not in
preamble. This variation embeds "does not count" / "is a fail" / "Mandatory" in three schema
locations (role registry header, state table trigger columns, decision condition column) --
each adjacent to the cell being constrained, visible without scrolling. The Phase Delta
pattern achieves C-16 by making phases first-class structural units. Scan Table A + B provide
C-14's per-path confirmation. The "artifact may not be written until Scan Summary shows status
CLOSED" gate achieves C-19 by blocking artifact completion -- distinct from C-13's
criterion-to-criterion ordering because it operates on the artifact output boundary itself.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

---

**SCOPE DECLARATION** *(required first block)*

| Field | Value |
|-------|-------|
| Lifecycle | [name, e.g., "Procure-to-Pay," "Lead-to-Order," "Period Close," "Case Lifecycle"] |
| Scenario | [company type, scale, industry context] |
| Variant framing | single-state trace -- no as-is/to-be distinction |
| Reason | [why no variant comparison applies] |

This block is Mandatory. A missing Scope Declaration is a fail.

---

**ROLE REGISTRY** *(complete before any phase or state)*

| R-ID | Role Name [Mandatory. "Approver," "Owner," "Manager," "Finance team," "Operations" do not count -- is a fail. Name the specific function at a real desk: "AP Clerk," "Senior Credit Analyst," "Revenue Accountant," "Procurement Category Manager," "Case Resolution Specialist."] | Functional Area | First Touch Point | Decision Authority [Mandatory. "Reviews and approves" does not count. State the decision type and measurable threshold, e.g., "Invoice approval up to $50K; routes >=50K to VP Finance."] | SLA Accountable? |
|------|------|------|------|------|------|
| R-01 | | | | | Y / N |
| R-02 | | | | | Y / N |
| R-03 | | | | | Y / N |

Minimum 3 roles. At least one SLA Accountable = Y per phase. No downstream R-ID citation is
valid unless it appears in this table.

**Do not proceed to phases until the Role Registry is complete.**

---

**LIFECYCLE PHASE TABLE** *(complete before any state trace)*

| Ph-ID | Phase Name | Entry Trigger [Mandatory. "After Phase N" does not count -- name the specific event or artifact state.] | Completion Condition [Mandatory. "When everything is done" does not count -- name the verification event or record state.] | SLA Envelope | At-Risk Threshold | SLA Owner (R-ID) |
|-------|-----------|------|------|------|------|------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |
| PH-04 | | | | | | |

Minimum 4 phases. Each aggregates >=2 states -- a 1:1 phase-to-state mapping does not count.
At least one At-Risk Threshold carries a named causal bottleneck.

**Do not proceed to Phase Delta blocks until the Phase Table is complete.**

---

**PHASE DELTA -- [Ph-ID: Phase Name]**

*Repeat this entire block for every Ph-ID.*

---

**ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition [Mandatory. "Previous phase complete" is a fail -- name the specific triggering event.] | |
| Prior phase (Ph-ID or INITIAL) | |
| Objects entering (named artifacts or records) | |
| Roles active (R-IDs) | |
| Exception pre-check | |
| SLA clock start | |

---

**STATE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Owner (R-ID) | Entry Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event. Describing the action in prose without naming a specific actor or event does not count toward the 6-state minimum.] | Exit Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event.] | Exception Exit (E-ID or "none") | SLA Window | Risk |
|------|-----------|-------------|------|------|------|------|------|
| | | | | | | | NORMAL / AT-RISK |

---

**DECISION POINTS -- [Ph-ID: Phase Name]**

```
Decision: [question resolved at this fork]
Owner: [R-ID from Role Registry -- a decision point with no cited R-ID does not count toward the 3-decision minimum]
Condition [Mandatory. Name a measurable threshold: dollar amount, day count, retry count,
  policy code. Qualitative conditions such as "large value" or "requires attention" do not
  count -- is a fail.]:
  Branch A (threshold met): --> [S-ID or T-ID]
  Branch B (not met): --> [S-ID or T-ID]
Fallback [Mandatory. "Escalate" alone does not count -- name the holding state (S-ID) or
  the escalation role (R-ID) and the path they take. Covers: owner unavailable, system down,
  configuration missing. A blank Fallback is a fail.]:
  --> [holding state S-ID] or [escalation R-ID and next action]
```

---

**EXIT GATE -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition (S-ID or Ph-ID) | |
| Failure transition (T-ID or exception E-ID) | |
| Primary blocker | |
| SLA at-risk threshold (from Phase Table) | |
| Scenario breach (Y / N) | |
| Breach verdict [if Y: specific cause traceable to a named S-ID or E-ID above] | |

---

*Repeat ENTRY CONTRACT + STATE TRACE + DECISION POINTS + EXIT GATE for each phase.*

---

**PARALLEL PATH BLOCK**

If parallel paths exist:

```
Fork state: [S-ID]
Branch A: [activity + R-ID]
Branch B: [activity + R-ID]
Join condition: [what must be true before merge]
Join owner: [R-ID]
Downstream: [S-ID after merge]
```

If sequential: state explicitly with rationale. Propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 distinct phases.

```
Exception: [name] (E-ID: E-0X)
Phase: [Ph-ID]
Triggering condition: [specific condition in domain terms -- not "system error"]
Divergence state: [S-ID where normal path exits]
Handling owner: [R-ID from Role Registry]
Deviation: [which normal steps are skipped or replaced]
Recovery: [ordered S-IDs] or Terminal: [T-ID]
```

---

**EDGE CASE CATALOG**

Minimum 2 edge cases distinct from the exception catalog.

```
Edge case: [name] (EC-ID: EC-0X)
Phase: [Ph-ID]
Scenario: [what condition produces this path]
Gap reason: [what lifecycle design assumption this violates]
Consequence: [specific operational impact -- not "errors may occur"]
```

---

**BOTTLENECK AND GAP REGISTER**

Minimum 2 bottlenecks (cause + downstream impact), minimum 1 process gap.

```
Bottleneck: [name] (B-ID: B-0X)
Phase: [Ph-ID] | Owner most accountable: [R-ID]
Cause: [domain-specific -- name the constraint, not "capacity issues"]
Downstream impact: [which phase or state is directly degraded]
```

```
Process gap: [name] (G-ID: G-0X)
Missing step: [what the lifecycle omits]
Why required: [what real-world execution cannot complete without this]
Consequence of absence: [specific failure when this step is missing]
```

---

**CROSS-LIFECYCLE DEPENDENCY**

Minimum 1 handoff.

```
Handoff: [name]
Direction: [outbound from this lifecycle / inbound trigger from partner]
Partner lifecycle: [name]
Coupling state: [S-ID or Ph-ID in this lifecycle]
What passes: [artifact, record, or status event]
Coupling risk: [downstream failure if handoff is late or malformed]
```

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome (on-time / breached / N/A) | Reached From (S-IDs, E-IDs) |
|------|--------------|----------------------------------|----------------------------------------|------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE. Every terminal must have at least one Reached From entry.

---

**SCAN TABLE A -- Per-State Path Verification**

For every S-ID in the state traces above, confirm it either continues to a named state or
appears in a terminal's Reached From column. Status is CLOSED when one of these is confirmed;
OPEN when neither is confirmed.

| S-ID | State Name | Phase (Ph-ID) | Continues To (S-ID) or Terminal (T-ID) | Status (CLOSED / OPEN) |
|------|-----------|-------------|----------------------------------------|----------------------|
| | | | | |

---

**SCAN TABLE B -- Per-Exception Path Verification**

For every E-ID in the exception catalog, confirm the recovery path leads to a named state or
terminal. Status is CLOSED when confirmed; OPEN when the path is unresolved.

| E-ID | Exception Name | Phase (Ph-ID) | Recovery S-ID (or first in sequence) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------|-------------------------------------------------------|----------------------|
| | | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (per-state) | | | |
| Scan Table B (per-exception) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Artifact may not be written until Scan Summary shows status CLOSED across all rows in Scan
Table A and Scan Table B.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Scope Declaration > Role Registry > Lifecycle Phase Table > Phase Delta blocks
(entry contract + state trace + decision points + exit gate, one set per phase) > Parallel
Path Block > Exception Catalog > Edge Case Catalog > Bottleneck and Gap Register >
Cross-Lifecycle Dependency > Terminal Declaration > Scan Table A > Scan Table B >
Scan Summary.

Pre-write verification checklist (all must be confirmed before writing):
- [ ] Role Registry complete: all R-IDs have domain-qualified titles; no generic labels
- [ ] Phase Delta blocks complete: entry contract, state trace, decisions, exit gate per phase
- [ ] State traces: all Entry/Exit Triggers name an actor or system event; no "then X happens"
- [ ] Decision points: all Conditions name measurable thresholds; all Fallbacks populated
- [ ] Exception catalog: all E-IDs have handling owner R-ID and named recovery or terminal
- [ ] Terminals: >=1 SUCCESS, >=1 FAILURE; all Reached From cells populated
- [ ] Scan Table A: all rows CLOSED
- [ ] Scan Table B: all rows CLOSED
- [ ] Scan Summary: Overall Status = CLOSED
