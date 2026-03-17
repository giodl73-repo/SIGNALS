---
skill: flow-lifecycle
round: 1
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v1-2026-03-15.md
---

# flow-lifecycle -- Round 1 Variations

Single-axis: V-01 (role sequence), V-02 (lifecycle emphasis / SLA-first), V-03 (inertia framing).
Combined: V-04 (phrasing register + lifecycle emphasis), V-05 (role sequence + inertia framing).

---

## V-01 -- Role Sequence Axis

**Variation axis:** Role sequence -- roles introduced in handoff order, each anchored to its first-touch point in the lifecycle.

**Hypothesis:** Forcing role introduction to follow handoff sequence means the role list doubles as a draft process skeleton. Any role named out of handoff order signals a gap or a concurrent path. C-08 (domain-specific role assignment) passes by construction because the author must anchor each role to the step where they first receive the document. Phantom roles (introduced but never assigned a state) surface as orphan rows in the handoff table.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**HANDOFF SEQUENCE -- ROLE INTRODUCTION**

Before tracing any state, introduce roles in the order they first receive or act on the process object. A role entry is valid only when its first-touch point is named. Do not list roles by seniority, department hierarchy, or alphabetical order -- list them by when they first handle the object.

| Seq | First-Touch Point | Role Name (domain-qualified) | R-ID | Handoff Received From | Handoff Passes To |
|-----|-------------------|------------------------------|------|-----------------------|-------------------|
| 1 | | | R-01 | ORIGIN | |
| 2 | | | R-02 | R-01 | |
| ... | | | | | |

Rules:
- Role Name must be domain-qualified. "Approver" is not a role name. "Credit Analyst" is.
- First-Touch Point names the state or event where this role enters. A role with no named first-touch point is a gap, not a role.
- Handoff Received From names the prior R-ID or "ORIGIN" for the first actor.
- Handoff Passes To names the next R-ID or "TERMINAL" for the last actor on a path.

**HANDOFF GATE: Every R-ID cited in any later stage must appear in this table. A decision point that cites an unnamed actor is a fail. A handoff that skips a sequence number without explanation is a gap.**

---

**STAGE 1 -- STATE TRACE IN HANDOFF ORDER**

Trace states in the order the process object moves through the handoff sequence. For each state:

| S-ID | State Name | Owner (R-ID) | Entry Condition | Exit Condition | Exits (labeled) |
|------|------------|-------------|-----------------|----------------|-----------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Orphan check: Every R-ID from the handoff table must own at least one S-ID. An R-ID with no state is a phantom role.**

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

If the decision involves a handoff to a role not yet in the sequence (an out-of-order touch), flag this as a concurrency note and explain the join condition.

---

**STAGE 3 -- PARALLEL PATHS**

Identify at least one point where two or more process threads run concurrently. For each parallel fork:

```
Fork state:      [S-ID where concurrent execution begins]
Branch A:        [thread label -- what runs here, who owns it (R-ID)]
Branch B:        [thread label -- what runs here, who owns it (R-ID)]
Join condition:  [what must be true before both branches merge]
Join owner:      [R-ID who validates the merge -- cite handoff sequence number]
Downstream:      [S-ID that follows the join]
```

If the process is entirely sequential, state that and propose one parallelization that would reduce elapsed time, naming the roles and states affected.

---

**STAGE 4 -- EXCEPTION FLOWS**

Trace at least one exception per lifecycle phase. Each exception must be specific to this process -- not a generic system error.

For each exception:

```
Exception:   [name]
Origin:      [S-ID where the exception arises]
Owner:       [R-ID -- the role who detects or handles this exception]
Trigger:     [specific condition, expressed in domain terms]
Deviation:   [how this diverges from the happy-path trace]
Recovery:    [recovery state (S-ID) or terminal failure state (T-ID) reached]
```

---

**STAGE 5 -- TERMINAL DECLARATION**

List all terminal states. Every branch traced in Stages 1-4 must reach one of these terminals.

| T-ID | Terminal Name | Type | Last Owner (R-ID) | Reached From (S-IDs) |
|------|--------------|------|------------------|----------------------|
| T-01 | | success / failure / cancel | | |
| T-02 | | | | |
| ... | | | | |

**Terminal gate: After filling this table, scan every S-ID and every exception recovery state. Any ID not listed in "Reached From" and not continuing to another state is an open path and a fail.**

---

**STAGE 6 -- BOTTLENECK AND GAP ANALYSIS**

Review the handoff sequence table. Any role who appears in only one state, or whose Handoff Passes To field points to a terminal, is a potential bottleneck candidate.

| B-ID | Type | Name | Cause (domain-specific) | Downstream Impact |
|------|------|------|------------------------|-------------------|
| B-01 | bottleneck | | | |
| B-02 | bottleneck | | | |
| G-01 | gap | | | |

Additionally: identify at least 2 edge cases -- valid paths the handoff sequence does not account for. For each, name the trigger, the gap in the handoff table, and the correct response.

---

**STAGE 7 -- CROSS-PROCESS HANDOFF (raise score)**

If this process passes the object to an adjacent process at any terminal:

| Terminal (T-ID) | Recipient Process | Handoff Trigger | Fields Passed | Acceptance Condition |
|----------------|------------------|-----------------|---------------|---------------------|
| | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

The artifact must contain the Handoff Sequence table, all seven stages in order, and the terminal gate verification. Every R-ID cited in any stage must exist in the handoff table. Every path must reach a declared T-ID.

---

## V-02 -- Lifecycle Emphasis Axis

**Variation axis:** Lifecycle emphasis -- SLA envelopes are first-class per phase, not an optional supplement. Every phase entry contract includes an SLA clock start and every phase exit gate includes an at-risk threshold with a scenario breach answer.

**Hypothesis:** Making timing a required field per phase surfaces bottlenecks (C-07) structurally. When the author must state expected duration at phase entry and at-risk threshold at phase exit, bottleneck identification is not a separate creative step -- it follows mechanically from phases whose time-box is breached in the simulated scenario.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**LIFECYCLE PHASES**

Identify all lifecycle phases before tracing any states. A phase is a named cluster of states with a discrete completion condition. Every state that will be traced belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Entry Trigger | SLA Envelope (expected) |
|-------|-----------|---------|--------------|------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

SLA Envelope = the elapsed-time window within which this phase is expected to complete under normal conditions (e.g., "same business day", "2-5 business days", "within 30 calendar days of period open").

---

**FOR EACH PHASE:**

---

**PHASE ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | [Ph-ID or INITIAL] |
| Roles active | [domain-qualified role names] |
| Objects entering | [named artifacts or records] |
| Exception pre-check | [conditions that would block entry and route to exception] |
| SLA clock start | [what event starts the clock for this phase] |

**STATE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Exit Owner (domain role) | Exception Exit |
|------|------------|-----------------|-----------------|--------------------------|---------------|
| | | | | | |

**DECISION POINTS -- [Ph-ID: Phase Name]**

For each fork within this phase:

```
Decision:  [condition being resolved]
Owner:     [domain-qualified role]
Branch A:  [label + target S-ID or Ph-ID]
Branch B:  [label + target S-ID or Ph-ID]
Fallback:  [path if decision cannot be resolved]
```

**PHASE EXIT GATE -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition | [S-ID or Ph-ID] |
| Failure transition | [T-ID or exception name] |
| Primary blocker | [role, resource, or condition that most commonly delays exit] |
| SLA at-risk threshold | [elapsed time at which this phase is considered at-risk] |
| Scenario breach | [Y / N -- does the simulated scenario exceed the at-risk threshold?] |
| Breach cause | [if Y: what causes the breach in this scenario] |

---

*Repeat PHASE ENTRY CONTRACT + STATE TRACE + DECISION POINTS + PHASE EXIT GATE for each phase listed in LIFECYCLE PHASES.*

---

**BOTTLENECK SYNTHESIS**

After completing all phases, review each exit gate where Scenario breach = Y. For each breached gate:

| B-ID | Phase (Ph-ID) | At-Risk Threshold Breached | Root Cause | Downstream Cascade |
|------|--------------|---------------------------|------------|-------------------|
| B-01 | | | | |
| B-02 | | | | |

If no phase breaches the at-risk threshold in the simulated scenario, identify the two phases most vulnerable to breach under peak load or exception conditions, and explain why.

---

**PARALLEL PATH ANALYSIS**

Identify at least one point where concurrent activities reduce lifecycle elapsed time. For each:

```
Fork state:      [S-ID or Ph-ID where concurrent execution begins]
Branch A:        [activity + owner role]
Branch B:        [activity + owner role]
Join condition:  [what must be true before threads merge]
Time saving:     [estimated elapsed time saved vs sequential execution]
Merge owner:     [domain-qualified role]
```

---

**EXCEPTION FLOW CATALOG**

At least one exception per lifecycle phase. Each must be process-specific.

```
Exception:     [name]
Phase:         [Ph-ID]
Trigger:       [specific condition]
Deviation:     [how this diverges from the normal phase sequence]
SLA impact:    [how this exception affects phase SLA compliance]
Recovery:      [T-ID or recovery S-ID]
```

---

**EDGE CASE CATALOG**

At least 3 edge cases distinct from the exception flows. For each:

```
Edge case:        [name]
Phase:            [Ph-ID]
Trigger:          [condition that produces this path]
SLA risk:         [does this edge case put the phase SLA at risk? why?]
Correct handling: [what the process should do]
```

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Reached From |
|------|--------------|------|-------------|-------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | |
| ... | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)**

| Handoff trigger | Recipient process | Fields passed | Acceptance condition | SLA dependency |
|-----------------|------------------|---------------|---------------------|---------------|
| | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Phases > Phases (each with entry contract, state trace, decisions, exit gate) > Bottleneck Synthesis > Parallel Path Analysis > Exception Flow Catalog > Edge Case Catalog > Terminal Declaration.

Every phase must have an SLA envelope, an at-risk threshold, and a scenario breach answer. Every path must reach a declared T-ID.

---

## V-03 -- Inertia Framing Axis

**Variation axis:** Inertia framing -- the status-quo process (manual, paper-based, legacy system, or "how it's done today") is named as an explicit comparator at each phase. The simulation runs a dual trace: as-is and to-be. Inertia points -- where the as-is resists displacement -- are required structural elements, not optional commentary.

**Hypothesis:** Requiring an as-is trace produces more realistic bottleneck and gap findings (C-07, C-09) because practitioners know exactly where the status-quo works well enough that automation will be resisted. Edge cases that exist only because of legacy workarounds become visible. The inertia comparison strengthens cross-lifecycle dependencies (C-10) because legacy processes often have informal couplings that to-be designs break.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

This simulation runs a dual trace: the as-is process (how the organization currently executes this lifecycle) and the to-be process (the target state, typically the automated or system-supported version). For each lifecycle phase, trace both states and identify where the transition from as-is to to-be will encounter resistance.

---

**PROCESS IDENTITY**

```
Lifecycle:      [name of process, e.g., Purchase-to-Pay]
As-is context:  [how this process is executed today -- tool, medium, manual steps]
To-be context:  [the target state -- system, automation, integration]
Scope:          [which document types or sub-processes are in scope]
```

---

**ROLE REGISTRY**

Declare all roles. For each role, note whether their work changes between as-is and to-be, and how.

| R-ID | Role Name (domain-qualified) | As-Is Activity | To-Be Activity | Change Type |
|------|------------------------------|----------------|----------------|-------------|
| R-01 | | | | eliminated / reduced / unchanged / new |
| R-02 | | | | |
| ... | | | | |

Change types:
- **eliminated**: role's manual step is automated away
- **reduced**: role still owns the step but workload shrinks
- **unchanged**: no change for this role between as-is and to-be
- **new**: role is introduced by the to-be process (e.g., exception manager, data steward)

---

**LIFECYCLE PHASES**

| Ph-ID | Phase Name | As-Is Mechanism | To-Be Mechanism | Inertia Risk (H/M/L) |
|-------|-----------|-----------------|-----------------|---------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

Inertia Risk: H = as-is mechanism is deeply embedded (manual workarounds, undocumented steps, role identity tied to the task). M = change is significant but the role survives. L = transition is mostly additive.

---

**FOR EACH PHASE -- DUAL TRACE**

---

**AS-IS TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Owner (R-ID) | Manual Step? |
|------|------------|-----------------|-----------------|-------------|--------------|
| | | | | | Y / N |

As-is exception flows for this phase:

```
As-is exception:    [name]
Trigger:            [condition]
Current workaround: [how the process currently handles this -- often manual, undocumented]
Terminal:           [success / failure / rework loop]
```

**TO-BE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Owner (R-ID) | Automated? |
|------|------------|-----------------|-----------------|-------------|------------|
| | | | | | Y / N |

To-be exception flows for this phase:

```
To-be exception:    [name]
Trigger:            [condition]
Handling:           [how the target system handles this]
Terminal:           [success / failure / exception queue]
```

**INERTIA POINT -- [Ph-ID: Phase Name]**

```
Inertia risk:       [H / M / L from the phase table]
Source of inertia:  [what makes the as-is hard to displace -- workaround, role identity,
                     undocumented logic, exception volume, integration dependency]
Transition risk:    [what breaks or degrades during the switchover period]
Mitigation:         [what must be true in the to-be design to reduce resistance]
```

---

*Repeat AS-IS TRACE + TO-BE TRACE + INERTIA POINT for each phase.*

---

**PARALLEL PATHS**

For each parallel execution path, note whether the parallelism exists in as-is, to-be, or both:

```
Fork state:      [S-ID]
As-is parallel:  [Y / N -- does as-is run these concurrently?]
To-be parallel:  [Y / N -- does to-be run these concurrently?]
Branch A:        [activity + owner]
Branch B:        [activity + owner]
Join condition:  [what must be true to merge]
Inertia note:    [if to-be introduces parallelism that as-is runs sequentially, name the resistance]
```

---

**EXCEPTION CATALOG -- AS-IS VS TO-BE**

For each significant exception, compare how as-is and to-be handle it:

| E-ID | Exception | As-Is Handling | To-Be Handling | Coverage Risk |
|------|-----------|---------------|----------------|---------------|
| E-01 | | | | covered / gap / regression |
| E-02 | | | | |
| E-03 | | | | |

Coverage Risk:
- **covered**: to-be addresses the exception at least as well as as-is
- **gap**: to-be does not address this exception at all
- **regression**: as-is handled this exception; to-be removes the handling without a substitute

---

**EDGE CASES EXPOSED BY TRANSITION**

At least 3 edge cases that exist only because of the as-is process or that emerge during the transition period:

```
Edge case:          [name]
Origin:             [as-is artifact / transition period / both]
Trigger:            [condition]
Impact:             [why this is problematic in the transition or in to-be]
Correct handling:   [what the to-be design must address]
```

---

**TERMINAL STATES**

| T-ID | Terminal Name | As-Is Reachable | To-Be Reachable | Type |
|------|--------------|-----------------|-----------------|------|
| T-01 | | Y / N | Y / N | success / failure / cancel |
| ... | | | | |

Note any terminal in the as-is that is unreachable in the to-be (regression), and any terminal in the to-be that does not exist in the as-is (new handling).

---

**CROSS-PROCESS DEPENDENCIES -- INERTIA AMPLIFIED**

For each dependency on an adjacent process, compare coupling in as-is vs to-be:

```
Adjacent process:   [name]
As-is coupling:     [how the processes interact today -- often informal or file-based]
To-be coupling:     [how the integration is designed -- event, API, batch]
Inertia risk:       [what resists the coupling change -- data format, timing, ownership]
```

---

**BOTTLENECK SYNTHESIS**

| B-ID | Phase | As-Is Bottleneck | Eliminated in To-Be? | To-Be Bottleneck (if any) | Net Change |
|------|-------|-----------------|---------------------|--------------------------|-----------|
| B-01 | | | Y / N | | better / worse / shifted |
| B-02 | | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Process Identity > Role Registry > Lifecycle Phases > Phase Dual Traces (as-is + to-be + inertia point per phase) > Parallel Paths > Exception Catalog > Edge Cases > Terminal States > Cross-Process Dependencies > Bottleneck Synthesis.

Every phase must have both an as-is trace and a to-be trace. Every inertia point must have a risk level, a source, and a mitigation. Every path must reach a declared T-ID.

---

## V-04 -- Combined (Phrasing Register + Lifecycle Emphasis)

**Variation axes combined:**
1. Phrasing register -- conversational and scenario-led; the prompt narrates as a guided walkthrough
2. Lifecycle emphasis -- SLA envelopes embedded per phase as required fields, not optional annotations

**Hypothesis:** A conversational register lowers the structural barrier to surfacing bottlenecks and edge cases (C-07, C-09) naturally while the embedded SLA requirement prevents the narrative from drifting away from timing accountability. The combination produces richer prose findings without sacrificing the measurable time-based evidence that makes bottleneck diagnoses defensible against rubric scoring.

---

You are a seasoned domain expert who has worked this process long enough to know exactly where it slows down, where it breaks, and what nobody documented. Walk through the full lifecycle of the process described in the signal.

---

**Who's involved, and when do they show up?**

Tell me every person who touches this process. Give each one a real job title -- not "approver" or "user" but the specific role in this domain (e.g., the Revenue Accountant who closes the period, the Sales Admin who enters the order). For each role, tell me when they first enter the process and what decision or action belongs to them.

---

**What are the phases, and how long should each one take?**

Before walking the process step by step, name the phases. A phase is a meaningful chunk of the lifecycle with a clear beginning and a clear "done" condition.

For each phase, answer:
- What is this phase trying to accomplish?
- What triggers it (what just happened in the prior phase)?
- How long does this normally take from entry to exit?
- What makes a phase take longer than it should -- what's the most common reason it stalls?

I need a real answer for each of these. "It depends" is not an answer. Give me the number and the reason.

---

**Walk me through the process, phase by phase**

For each phase:

*Opening:* Tell me how this phase starts. What just happened that put the process here? What does the process object look like when it arrives?

*Normal path:* Walk me through what happens step by step. At every decision point, tell me: what's the question, who answers it, what happens if the answer is yes, what happens if the answer is no, and what happens if no one answers at all?

*Parallel work:* If two things happen simultaneously in this phase, walk me through both threads and tell me what the process is waiting for before it can continue past the fork.

*Phase completion:* What has to be true for this phase to be finished? Who signs off? What document or record change makes it official?

*Timing pressure:* What is the normal SLA for this phase? What's the at-risk threshold -- when does this phase being late start causing visible problems? Does the scenario you're tracing breach that threshold? If yes, say why.

*Exception exits:* What can go wrong in this phase that sends the process off the normal path? For each: what triggers it, how does it diverge, and where does it land?

---

**The cases nobody wrote a rule for**

Every process has edge cases -- valid but rare situations that nobody planned for. After walking all the phases, name at least 3. For each one, explain what triggers it, why it causes problems, and what the process should do when it happens.

---

**Where does time go?**

Now that you've walked the whole process, call out the 2 or 3 places where elapsed time is the real risk. For each:
- Which phase and which step?
- What is the normal SLA?
- What backs up behind it when it slips?
- In the scenario you traced, did this step breach its threshold?

---

**How does it end?**

List every way this process can terminate. For each terminal state, say whether it's a success, a failure, or a cancellation. Every path you walked above must land on one of these.

---

**Connections to other processes**

If this process hands off to another process -- or if another process must complete before this one can proceed -- describe that connection. What triggers the handoff, what information moves, and what does the receiving process need to see before it accepts?

---

**Write the artifact**

Produce the lifecycle artifact at `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

The artifact should read like a professional process analysis: organized, specific, and useful to someone who has to implement, debug, or improve this process. Every role must have a domain-qualified name. Every phase must have an SLA envelope (expected duration) and an at-risk threshold with a scenario breach answer. Every path must reach a named terminal. Every decision point must name the owner.

---

## V-05 -- Combined (Role Sequence + Inertia Framing)

**Variation axes combined:**
1. Role sequence -- roles introduced in handoff order, each anchored to a first-touch point
2. Inertia framing -- as-is process named as an explicit comparator at each handoff point

**Hypothesis:** Combining handoff-ordered role introduction with as-is/to-be comparison addresses two common failure modes simultaneously. Generic role names (C-08 fail) are blocked by the handoff gate requiring a first-touch point for every role. Edge cases that exist only because of legacy workarounds (C-09) surface naturally when the author traces both the as-is and to-be behavior at each handoff point. Exception flows become more realistic because the as-is column forces the author to name the informal handling that practitioners already know about.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

This simulation runs in two layers: the handoff sequence (who touches the document and in what order) and the inertia delta (what changes between the as-is process and the to-be process at each handoff point).

---

**PROCESS CONTEXT**

```
Lifecycle:       [name of process]
As-is context:   [how this process runs today -- tool, medium, manual steps]
To-be context:   [target state -- system, automation, integration]
```

---

**HANDOFF SEQUENCE WITH INERTIA DELTA**

Introduce roles in the order they first touch the process object. For each role, name the as-is work and the to-be work at their handoff point.

| Seq | First-Touch Point | R-ID | Role Name (domain-qualified) | As-Is Work | To-Be Work | Change Type |
|-----|-------------------|------|------------------------------|------------|------------|-------------|
| 1 | | R-01 | | | | |
| 2 | | R-02 | | | | |
| ... | | | | | | |

Change types: **eliminated** / **reduced** / **unchanged** / **new**

**HANDOFF GATE: Every R-ID cited anywhere in the simulation must appear in this table with a named first-touch point. An R-ID with no first-touch point is an undeclared actor and a scoring fail. The to-be work cell may not be blank -- if the role has no to-be work, mark it "eliminated" and explain below.**

---

**STATE TRACE -- TO-BE LIFECYCLE**

Trace the to-be lifecycle states in handoff sequence order. For each state:

| S-ID | State Name | Owner (R-ID) | Entry Condition | Exit Transition | Exception Exit |
|------|------------|-------------|-----------------|-----------------|----------------|
| S-01 | | R-01 | | | |
| S-02 | | R-02 | | | |
| ... | | | | | |

For each state where Change Type is **eliminated** or **reduced** (from the handoff table), add an inline inertia note:

> *Inertia note [S-ID]: In the as-is process, [role R-XX] performed [specific manual step] at this point. The to-be design eliminates or reduces this step. Transition risk: [what breaks or degrades if the manual step is retired without a complete substitute].*

---

**DECISION AND FORK POINTS**

For each decision point in the lifecycle:

```
Decision:      [condition being resolved]
Handoff seq:   [sequence number of the decision owner]
Owner:         [R-ID]
Branch A:      [label + target S-ID]
Branch B:      [label + target S-ID]
Fallback:      [path if decision cannot be resolved]
As-is delta:   [how this decision was made in the as-is process -- informal rule, manual
                review, email chain, system flag -- and whether the to-be design handles
                it the same way or differently]
```

---

**PARALLEL PATHS**

For each concurrent execution path:

```
Fork state:       [S-ID]
Branch A:         [activity + R-ID]
Branch B:         [activity + R-ID]
Join condition:   [what must be true to merge]
As-is parallel:   [did the as-is process run these concurrently? if not, what made it
                   sequential and what inertia exists against introducing parallelism?]
```

---

**EXCEPTION FLOWS -- AS-IS WORKAROUNDS SURFACED**

For each significant exception, declare how as-is handled it (often an informal workaround) and how to-be handles it:

| E-ID | Exception | Trigger | As-Is Workaround | To-Be Handling | Coverage Risk |
|------|-----------|---------|-----------------|----------------|---------------|
| E-01 | | | | | covered / gap / regression |
| E-02 | | | | | |
| E-03 | | | | | |

Coverage Risk:
- **covered**: to-be addresses the exception at least as well as as-is
- **gap**: to-be does not address this exception at all
- **regression**: as-is handled this exception; to-be removes the handling without a substitute

---

**EDGE CASES FROM AS-IS ARTIFACTS**

At least 3 edge cases that exist because of the as-is process or that emerge during the transition period:

```
Edge case:          [name]
Handoff point:      [R-ID or sequence number where this occurs]
As-is origin:       [what as-is behavior or workaround creates this edge case]
To-be exposure:     [how the to-be design is vulnerable to this case]
Correct response:   [what the to-be design must do]
```

---

**TERMINAL STATES**

| T-ID | Terminal Name | Type | Reached From |
|------|--------------|------|-------------|
| T-01 | | success / failure / cancel | |
| ... | | | |

**Terminal gate: Every S-ID in the state trace and every E-ID in the exception table must either continue to another state or appear in "Reached From." Unlisted IDs are open paths and a fail.**

---

**BOTTLENECK SYNTHESIS**

For each handoff sequence point where Change Type is **eliminated** or **reduced**, confirm whether the bottleneck moves, shrinks, or shifts:

| B-ID | Handoff Seq | As-Is Bottleneck | Eliminated in To-Be? | Residual or Shifted Bottleneck |
|------|------------|-----------------|---------------------|-------------------------------|
| B-01 | | | Y / N | |
| B-02 | | | Y / N | |

Identify at least 1 gap -- a step that should exist in the to-be process but is absent.

---

**CROSS-PROCESS HANDOFF**

| Adjacent process | As-Is coupling | To-Be coupling | Inertia risk |
|-----------------|---------------|----------------|-------------|
| | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Process Context > Handoff Sequence (with inertia delta) > State Trace (with inline inertia notes) > Decision Points > Parallel Paths > Exception Flows > Edge Cases > Terminal States > Bottleneck Synthesis > Cross-Process Handoff.

Every R-ID must appear in the handoff table with a named first-touch point. Every exception must have a Coverage Risk assessment. Every path must reach a declared T-ID.
