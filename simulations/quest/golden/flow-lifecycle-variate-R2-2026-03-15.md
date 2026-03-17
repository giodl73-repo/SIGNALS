---
skill: flow-lifecycle
round: 2
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v21-2026-03-15.md
---

# flow-lifecycle -- Round 2 Variations

Single-axis: V-01 (lifecycle emphasis: C-11/C-12/C-13 full lock), V-02 (inertia framing: SLA-enriched dual trace), V-03 (role sequence: handoff-anchored SLA).
Combined: V-04 (lifecycle emphasis + inertia framing: surgical C-13 layer), V-05 (phrasing register fixed + lifecycle emphasis).

**R1 learning applied to R2 design:**
- V-02 R1 scored 100/100 under v20; projects to 110/115 under v21 (C-13 not attempted). V-01 R2 adds VARIANT DECLARATION + C-11 breach verdict field + C-12 exception SLA impact to lock 115/115.
- V-03/V-05 R1 shared C-08 scope failure: "as-is artifacts" framing excluded stable-state lifecycle gaps. Fixed in V-02 R2 via explicit two-category edge case section.
- V-04 R1 failed C-01 (no S-ID enforcement) and C-04 (edge cases asked, not missing steps). Both fixed in V-05 R2 via STATE LEDGER pre-step and split gap/edge-case questions.
- C-13 single-state exemption: a trace without variant framing earns C-13 by explicit declaration. Applied in V-01 R2, V-03 R2.

---

## V-01 -- Lifecycle Emphasis Axis: Full Aspirational Lock

**Variation axis:** Lifecycle emphasis -- extends V-02 R1's SLA-first architecture with three structural additions that target the new v21 aspirational criteria: (1) VARIANT DECLARATION block at the top for C-13 single-state exemption, (2) Breach Verdict as a required distinct field in each Phase Exit Gate for C-11, (3) SLA impact as a required field in every exception flow for C-12.

**Hypothesis:** V-02 R1 achieved 100/100 under v20 because its SLA-first architecture structurally enforces C-10. C-11 and C-12 are extensions of the same architecture, not new concepts. Adding three targeted fields (VARIANT DECLARATION, Breach Verdict, SLA impact on exceptions) costs minimal prompt complexity while locking all five aspirational criteria. C-13 is earned via the single-state exemption: declaring no variant applies requires naming a reason, which is costless to produce. Target: 115/115 with no structural regression from V-02 R1.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**VARIANT DECLARATION**

Before tracing any states, declare the simulation scope.

| Field | Value |
|-------|-------|
| Lifecycle | [name of the process being simulated] |
| Variant framing | single-state trace -- no as-is/to-be distinction |
| Reason | [why no variant comparison applies -- e.g., "process is net-new with no prior manual equivalent," "scope is restricted to the target system configuration," "prompt names a single operational state"] |

This block is required. A missing or blank Variant Declaration is a structural fail.

---

**LIFECYCLE PHASES**

Identify all phases before tracing any states. A phase is a named cluster of states with a discrete completion condition. Every state traced belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Entry Trigger | SLA Envelope (expected) |
|-------|-----------|---------|--------------|------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

SLA Envelope = the elapsed-time window within which this phase is expected to complete under normal conditions (e.g., "same business day", "2-5 business days", "within 30 calendar days of period open").

---

**FOR EACH PHASE -- repeat this block for every Ph-ID:**

---

**PHASE ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | [Ph-ID or INITIAL] |
| Roles active | [domain-qualified role names -- "Finance team" and "Management" are not domain-qualified] |
| Objects entering | [named artifacts or records] |
| Exception pre-check | [conditions that block entry and route to exception before phase work begins] |
| SLA clock start | [event that starts the timing clock for this phase] |

**STATE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Exit Owner (domain role) | Exception Exit |
|------|------------|-----------------|-----------------|--------------------------|---------------|
| | | | | | |

State naming rule: names must be unambiguous identifiers (e.g., "PO Pending Approval" not "the approval stage"). A step described in prose without an S-ID does not count toward the 6-state minimum.

**DECISION POINTS -- [Ph-ID: Phase Name]**

For each fork within this phase:

```
Decision:  [the question being resolved]
Owner:     [domain-qualified role -- named function, not department label]
Branch A:  [transition label + target S-ID or Ph-ID]
Branch B:  [transition label + target S-ID or Ph-ID]
Fallback:  [path if decision cannot be resolved -- timeout, escalation rule, or terminal]
```

A decision point that names the condition but omits the owner role is a partial pass (0.5). All three elements required for full credit.

**PHASE EXIT GATE -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition | [S-ID or Ph-ID] |
| Failure transition | [T-ID or exception name] |
| Primary blocker | [role, resource, or condition most commonly delaying exit] |
| SLA at-risk threshold | [elapsed time at which this phase is considered at-risk -- e.g., "> 3 business days"] |
| Breach verdict | [Y / N -- does the simulated scenario exceed the at-risk threshold for this phase?] |
| Breach cause | [required if Breach verdict = Y: the specific condition in this scenario causing breach -- must reference a named step, role dependency, or system constraint from the state trace] |

Note: Breach verdict and SLA at-risk threshold are distinct. The threshold is a label; the verdict is an active judgment against the scenario being simulated. Both are required. A threshold without a verdict is a partial pass on C-11.

If Breach verdict = N, confirm the phase is still within threshold and note whether it would breach under peak conditions.

---

*Repeat PHASE ENTRY CONTRACT + STATE TRACE + DECISION POINTS + PHASE EXIT GATE for every Ph-ID.*

---

**PARALLEL PATH ANALYSIS**

Identify at least one point where concurrent activities reduce lifecycle elapsed time. For each:

```
Fork state:      [S-ID or Ph-ID where concurrent execution begins]
Branch A:        [activity + owner role (domain-qualified)]
Branch B:        [activity + owner role (domain-qualified)]
Join condition:  [what must be true before both branches merge]
Time saving:     [estimated elapsed time saved vs sequential execution]
Merge owner:     [domain-qualified role who validates the join]
```

If the process is entirely sequential, state that explicitly and explain why. Explicit absence declaration earns C-06 recommended credit. Silence does not.

---

**EXCEPTION FLOW CATALOG**

At least one exception per lifecycle phase. Each exception must be process-specific -- not a generic system error.

For each exception:

```
Exception:     [name]
Phase:         [Ph-ID where the exception arises]
Trigger:       [specific condition in domain terms]
Deviation:     [how this diverges from the normal phase sequence]
SLA impact:    [how this exception affects phase SLA compliance -- must be quantitative or
                directional, e.g.:
                  "adds 3+ days to PO approval phase; triggers breach of PH-02 threshold"
                  "resets phase clock; cascades 5+ day delay into PH-03"
                "may cause delays" does not satisfy this field]
Recovery:      [T-ID if terminal, or S-ID if the exception recovers to a lifecycle state]
```

SLA impact is required on every exception flow. The field must name the timing consequence and identify downstream phase cascade where applicable.

---

**EDGE CASE CATALOG**

At least 3 edge cases distinct from the exception flows above. Edge cases are design gaps -- scenarios logically reachable but absent from the lifecycle trace.

```
Edge case:        [name]
Phase:            [Ph-ID where this scenario could arise]
Trigger:          [condition that produces this scenario]
Why unhandled:    [what the current lifecycle lacks -- missing step, decision rule, or state]
SLA risk:         [effect on phase timing -- quantitative or directional]
Correct handling: [what the process should do]
```

Do not reuse scenarios from EXCEPTION FLOW CATALOG. Exception flows are reachable paths in the current design. Edge cases are gaps -- scenarios the process has no path for.

---

**BOTTLENECK SYNTHESIS**

Review every Phase Exit Gate where Breach verdict = Y. For each breached gate:

| B-ID | Phase (Ph-ID) | At-Risk Threshold | Breach Cause | Downstream Cascade |
|------|--------------|-------------------|-------------|-------------------|
| B-01 | | | | |
| B-02 | | | | |

If no phase has Breach verdict = Y in the simulated scenario, identify the two phases most vulnerable to breach under peak load or exception conditions and explain why. Minimum 2 bottleneck entries regardless.

Additionally, identify at least 1 process gap:

| G-ID | Phase | Missing Step | Real-World Requirement | Risk |
|------|-------|-------------|----------------------|------|
| G-01 | | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Reached From (S-IDs / E-IDs) |
|------|--------------|------|-------------|------------------------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | |
| ... | | | | |

Terminal gate: every S-ID in every state trace and every Recovery field in every exception flow must either continue to another S-ID or appear in "Reached From." Unlisted IDs are open paths and a structural fail.

Minimum: 1 success terminal and 1 failure or cancel terminal.

---

**CROSS-PROCESS HANDOFF**

| Handoff trigger | Recipient process | Fields passed | Acceptance condition | SLA dependency |
|-----------------|------------------|---------------|---------------------|---------------|
| | | | | |

SLA dependency: state whether a delay in this lifecycle breaches a timing obligation in the adjacent process.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Variant Declaration > Lifecycle Phases > Per-Phase Blocks (entry contract, state trace, decisions, exit gate) > Parallel Path Analysis > Exception Flow Catalog > Edge Case Catalog > Bottleneck Synthesis > Terminal Declaration > Cross-Process Handoff.

Pre-write checklist:
- [ ] Variant Declaration present and completed with reason field
- [ ] Every phase has SLA Envelope, at-risk threshold, Breach verdict (Y/N), and Breach cause (if Y)
- [ ] Every exception flow has SLA impact with quantitative or directional timing consequence
- [ ] Every S-ID and exception Recovery state reaches a declared T-ID
- [ ] All decision points name a domain-qualified owner role
- [ ] EDGE CASE CATALOG scenarios are not present in EXCEPTION FLOW CATALOG

---

## V-02 -- Inertia Framing Axis: SLA-Enriched Dual Trace

**Variation axis:** Inertia framing -- V-03 R1 repaired and extended. Three fixes applied: (1) SLA Envelope added to LIFECYCLE PHASES table and Breach Verdict added to Phase Exit Gate (C-10/C-11 unlocked); (2) SLA impact field added to exception catalog (C-12 unlocked); (3) EDGE CASE CATALOG restructured into two explicit categories -- transition-period artifacts AND stable-state lifecycle gaps -- closing the C-08 scope failure from R1.

**Hypothesis:** V-03 R1 scored 90 under v20 with C-10 fail and C-08 partial. Under v21 it would score 90/115 (C-10/C-11/C-12 fail, C-13 pass). The SLA additions are additive over V-03 R1's proven inertia structure; the C-08 fix recaptures the recommended partial. C-13 is native to the as-is/to-be bottleneck trajectory table. With all four SLA aspirational criteria structurally enforced, target is 115/115.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

This simulation runs a dual trace: the as-is process (how the organization currently executes this lifecycle) and the to-be process (the target state -- system-supported or redesigned). For each lifecycle phase, trace both states and identify where the transition will encounter resistance.

---

**PROCESS IDENTITY**

```
Lifecycle:      [name of process]
As-is context:  [how this process runs today -- tool, medium, key manual steps]
To-be context:  [the target state -- system, automation, integration]
Scope:          [which document types or sub-processes are in scope]
```

---

**ROLE REGISTRY**

| R-ID | Role Name (domain-qualified) | As-Is Activity | To-Be Activity | Change Type |
|------|------------------------------|----------------|----------------|-------------|
| R-01 | | | | eliminated / reduced / unchanged / new |
| R-02 | | | | |
| ... | | | | |

Change types:
- **eliminated**: role's manual step is automated away
- **reduced**: role still owns the step but workload shrinks
- **unchanged**: no change between as-is and to-be
- **new**: role introduced by the to-be process

Generic role names ("Finance team," "Operations," "Management") are not domain-qualified and fail C-05.

---

**LIFECYCLE PHASES**

| Ph-ID | Phase Name | As-Is Mechanism | To-Be Mechanism | Inertia Risk (H/M/L) | SLA Envelope (expected) |
|-------|-----------|-----------------|-----------------|---------------------|------------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

Inertia Risk: H = deeply embedded as-is (workarounds, undocumented steps, role identity tied to the task). M = significant change but role survives. L = transition is mostly additive.
SLA Envelope = expected elapsed time for this phase to complete under normal conditions.

---

**FOR EACH PHASE -- repeat this block for every Ph-ID:**

---

**AS-IS TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Owner (R-ID) | Manual Step? |
|------|------------|-----------------|-----------------|-------------|--------------|
| | | | | | Y / N |

As-is exception flows for this phase (at least 1):

```
As-is exception:    [name]
Trigger:            [specific condition in domain terms]
Current workaround: [how the process currently handles this -- often manual, undocumented]
Terminal:           [success / failure / rework loop]
```

**TO-BE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Owner (R-ID) | Automated? |
|------|------------|-----------------|-----------------|-------------|------------|
| | | | | | Y / N |

To-be exception flows for this phase (at least 1):

```
To-be exception:    [name]
Trigger:            [specific condition]
Handling:           [how the target system handles this]
SLA impact:         [timing consequence -- quantitative or directional:
                     e.g., "adds 3+ days; triggers breach of PH-02 threshold"
                     "may cause delays" does not satisfy this field]
Terminal:           [success / failure / exception queue / recovery S-ID]
```

**PHASE EXIT GATE -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition (to-be) | |
| Success transition | [S-ID or Ph-ID] |
| Failure transition | [T-ID or exception name] |
| Primary blocker (to-be) | [role, resource, or system dependency] |
| SLA at-risk threshold | [elapsed time at which this phase is at-risk in the to-be process] |
| Breach verdict | [Y / N -- does the simulated scenario exceed the at-risk threshold?] |
| Breach cause | [required if Y: specific condition in this scenario causing breach] |

**INERTIA POINT -- [Ph-ID: Phase Name]**

```
Inertia risk:       [H / M / L]
Source of inertia:  [what makes the as-is hard to displace -- workaround, role identity,
                     undocumented logic, exception volume, integration dependency]
Transition risk:    [what breaks or degrades during the switchover period]
Mitigation:         [what must be true in the to-be design to reduce resistance]
```

---

*Repeat AS-IS TRACE + TO-BE TRACE + PHASE EXIT GATE + INERTIA POINT for every Ph-ID.*

---

**PARALLEL PATHS**

For each concurrent execution path, note whether parallelism exists in as-is, to-be, or both:

```
Fork state:      [S-ID]
As-is parallel:  [Y / N -- does as-is run these concurrently?]
To-be parallel:  [Y / N -- does to-be run these concurrently?]
Branch A:        [activity + owner (R-ID)]
Branch B:        [activity + owner (R-ID)]
Join condition:  [what must be true before threads merge]
Inertia note:    [if to-be introduces parallelism that as-is runs sequentially, name the resistance]
```

If the process is entirely sequential, declare it explicitly. Explicit declaration earns C-06 credit.

---

**EXCEPTION CATALOG -- AS-IS VS TO-BE**

| E-ID | Exception | As-Is Handling | To-Be Handling | SLA Impact (to-be) | Coverage Risk |
|------|-----------|---------------|----------------|-------------------|---------------|
| E-01 | | | | | covered / gap / regression |
| E-02 | | | | | |
| E-03 | | | | | |

SLA Impact (to-be): must state timing consequence (days, threshold breach, downstream cascade) -- not just note that an impact exists.

Coverage Risk:
- **covered**: to-be addresses the exception at least as well as as-is
- **gap**: to-be does not address this exception at all
- **regression**: as-is handled this; to-be removes the handling without substitute

---

**EDGE CASE CATALOG**

Name edge cases in two explicit categories. Both are required.

**Category A -- Transition-period artifacts (at least 2):**
Edge cases that exist only because of the as-is process or that emerge during the switchover period.

```
Edge case:          [name]
Origin:             [as-is artifact / transition period / both]
Trigger:            [condition]
Impact:             [why this is problematic in transition or in to-be]
Correct handling:   [what the to-be design must address]
```

**Category B -- Stable-state lifecycle gaps (at least 1):**
Edge cases that exist in the to-be process as designed, independent of transition -- scenarios logically reachable but absent from the to-be trace.

```
Edge case:          [name]
Phase:              [Ph-ID where this occurs in the to-be trace]
Trigger:            [condition that produces this path in the to-be state]
Why unhandled:      [what the to-be design lacks -- the missing step or decision rule]
Risk:               [consequence if the to-be process encounters this case]
Correct handling:   [what should be added to the to-be design]
```

---

**BOTTLENECK SYNTHESIS -- TRAJECTORY**

For each bottleneck, track it across the as-is/to-be transition with three required fields:

| B-ID | Phase | As-Is Bottleneck | Status in To-Be | New Location (if shifted) | Net Change |
|------|-------|-----------------|-----------------|--------------------------|-----------|
| B-01 | | | eliminated / shifted / residual | | better / worse / shifted |
| B-02 | | | | | |

Status: **eliminated** = does not exist in to-be. **shifted** = moves to a different step or phase (new location required). **residual** = persists unchanged.

Net Change must assess whether the process is faster, slower, or unchanged overall. A trajectory entry without the net-change assessment is a partial pass on C-13.

---

**TERMINAL STATES**

| T-ID | Terminal Name | As-Is Reachable | To-Be Reachable | Type | SLA Outcome |
|------|--------------|-----------------|-----------------|------|-------------|
| T-01 | | Y / N | Y / N | success / failure / cancel | on-time / breached / N/A |
| ... | | | | | |

Note any terminal in as-is unreachable in to-be (regression) and any terminal in to-be not present in as-is (new handling).

---

**CROSS-PROCESS DEPENDENCIES -- INERTIA AMPLIFIED**

```
Adjacent process:   [name]
As-is coupling:     [how processes interact today -- often informal or file-based]
To-be coupling:     [designed integration -- event, API, batch]
SLA dependency:     [whether this lifecycle's SLA breach cascades into the adjacent process]
Inertia risk:       [what resists the coupling change]
```

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Process Identity > Role Registry > Lifecycle Phases > Per-Phase Blocks (as-is trace, to-be trace, exit gate, inertia point) > Parallel Paths > Exception Catalog > Edge Case Catalog (A + B) > Bottleneck Synthesis Trajectory > Terminal States > Cross-Process Dependencies.

Pre-write checklist:
- [ ] Every phase has SLA Envelope, breach verdict, and (if Y) breach cause
- [ ] Every to-be exception has SLA impact with quantitative or directional timing
- [ ] Edge Case Catalog contains both transition-period artifacts (Category A) AND stable-state gaps (Category B)
- [ ] Every bottleneck has all three trajectory fields: as-is status, to-be status, net change
- [ ] Every path reaches a declared T-ID

---

## V-03 -- Role Sequence Axis: Handoff-Anchored SLA

**Variation axis:** Role sequence -- V-01 R1 repaired and extended. Three changes: (1) C-08 EDGE CASE section fully defined with body instructions and a two-part scope requirement (C-01 R1 had a truncated section header only); (2) SLA Clock column added to the HANDOFF SEQUENCE table -- timing is role-anchored, not phase-anchored; (3) SLA impact field added to exception flows (C-12). C-13 earned via PROCESS CONTEXT variant declaration.

**Hypothesis:** Anchoring timing to the handoff sequence rather than to phases creates a different analytical lens: the bottleneck is named by identifying which role holds the object longest, not by which phase runs over. This may produce more actionable diagnoses because the role who causes breach is explicitly named in the handoff table rather than inferred from phase aggregation. Target: all essential + recommended structurally enforced; C-09/C-10/C-11/C-12/C-13 all reachable.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**PROCESS CONTEXT**

```
Lifecycle:         [name of process]
Variant framing:   [single-state trace -- no as-is/to-be distinction]
Reason:            [why no variant comparison applies -- process is net-new / scope excludes
                    prior state / prompt names a single operational configuration]
```

Variant framing is required. A missing or blank entry is a structural fail.

---

**HANDOFF SEQUENCE -- ROLE INTRODUCTION**

Introduce roles in the order they first receive or act on the process object. A role entry is valid only when its first-touch point is named.

| Seq | First-Touch Point | R-ID | Role Name (domain-qualified) | SLA Clock | Handoff From | Handoff To |
|-----|-------------------|------|------------------------------|-----------|--------------|------------|
| 1 | | R-01 | | [expected time this role holds the object] | ORIGIN | |
| 2 | | R-02 | | | R-01 | |
| ... | | | | | | |

Rules:
- Role Name must be domain-qualified. "Approver" is not a role. "Credit Analyst" is.
- First-Touch Point = the state or event where this role enters. No named first-touch = gap, not a role.
- SLA Clock = expected elapsed time from when this role receives the object to when they pass it on. If the role owns a phase boundary, note the at-risk threshold.
- Handoff From = prior R-ID (or ORIGIN). Handoff To = next R-ID (or TERMINAL).

**HANDOFF GATE: Every R-ID cited in any later section must appear in this table. A decision point citing an unnamed actor is a fail. An R-ID with no SLA Clock is a timing gap.**

---

**STAGE 1 -- STATE TRACE IN HANDOFF ORDER**

| S-ID | State Name | Owner (R-ID) | Entry Condition | Exit Condition | SLA at-risk? | Exits (labeled) |
|------|------------|-------------|-----------------|----------------|-------------|-----------------|
| S-01 | | | | | Y / N | |
| S-02 | | | | | | |
| ... | | | | | | |

State naming rule: names must be unambiguous identifiers ("PO Pending Approval" not "the approval stage"). Prose without an S-ID does not count toward the 6-state minimum.

SLA at-risk: flag Y for states where the SLA Clock from the HANDOFF SEQUENCE most commonly runs over. For each Y, add a brief note in Exits naming the cause.

**Orphan check: every R-ID from the handoff table must own at least one S-ID. An R-ID with no owned state is a phantom role.**

---

**STAGE 2 -- DECISION AND FORK POINTS**

```
Decision:      [the question being resolved]
Owner:         [R-ID from the handoff table]
Seq:           [handoff sequence number of the decision owner]
Branch A:      [transition label + target S-ID]
Branch B:      [transition label + target S-ID]
Fallback:      [path if decision cannot be made -- timeout, escalation, or terminal]
```

A decision that names the condition but omits the owner role is a partial pass (0.5).

If the decision involves a role not yet in the handoff sequence, flag it as a concurrency note and explain the join condition.

---

**STAGE 3 -- PARALLEL PATHS**

For each parallel fork:

```
Fork state:      [S-ID where concurrent execution begins]
Branch A:        [thread label + owner (R-ID)]
Branch B:        [thread label + owner (R-ID)]
Join condition:  [what must be true before threads merge]
Join owner:      [R-ID who validates the merge]
Downstream:      [S-ID following the join]
Time saving:     [estimated time saved vs sequential]
```

If the process is entirely sequential, declare it explicitly and propose one parallelization that would reduce elapsed time, naming the roles and states affected. Explicit declaration earns C-06 credit.

---

**STAGE 4 -- EXCEPTION FLOWS**

At least one exception per lifecycle phase.

```
Exception:     [name]
Origin:        [S-ID where the exception arises]
Owner:         [R-ID -- role who detects or handles this exception]
Trigger:       [specific condition in domain terms]
Deviation:     [how this diverges from the happy-path trace]
SLA impact:    [timing consequence on the owning role's SLA Clock and any downstream roles --
                quantitative or directional:
                  "resets R-03 clock; delays STAGE 5 entry by 3+ days"
                  "may cause delays" does not satisfy this field]
Recovery:      [recovery S-ID or terminal T-ID]
```

---

**STAGE 5 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Last Owner (R-ID) | Reached From (S-IDs / E-IDs) |
|------|--------------|------|-------------|-------------------|------------------------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | | |
| ... | | | | | |

**Terminal gate: every S-ID in Stage 1 and every Recovery state in Stage 4 must either continue to another S-ID or appear in "Reached From." Unlisted IDs are open paths and a fail.**

---

**STAGE 6 -- BOTTLENECK AND GAP ANALYSIS**

Roles with a long SLA Clock relative to upstream and downstream peers are bottleneck candidates. Any role whose Handoff To points directly to TERMINAL without an intermediate state is a potential gap.

| B-ID | Type | Name | Seq (R-ID) | Cause (domain-specific) | Downstream Impact |
|------|------|------|-----------|------------------------|-------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

Bottleneck cause must be domain-specific (e.g., "Credit Analyst queue: single approver for all orders > $50K"). "Slow" is not a cause.

Additionally, at least 2 edge cases -- valid scenarios the handoff sequence does not account for. These must be stable-state lifecycle gaps (not exception flows):

```
Edge case:          [name]
Trigger:            [condition that produces this scenario]
Handoff gap:        [which R-ID sequence step has no defined handling]
Why unhandled:      [what the lifecycle design lacks -- the missing step, rule, or state]
SLA risk:           [effect on the owning role's SLA Clock if this case occurs]
Correct response:   [what the lifecycle should do]
```

---

**STAGE 7 -- CROSS-PROCESS HANDOFF**

| Terminal (T-ID) | Adjacent Process | Direction | Handoff Trigger | Fields Passed | SLA Dependency |
|----------------|-----------------|-----------|-----------------|---------------|---------------|
| | | sends-to / receives-from | | | |

SLA Dependency: whether a delay in this lifecycle breaches a downstream or upstream timing obligation.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Process Context (with Variant Declaration) > Handoff Sequence > Stage 1 (State Trace) > Stage 2 (Decisions) > Stage 3 (Parallel Paths) > Stage 4 (Exceptions) > Stage 5 (Terminals) > Stage 6 (Bottlenecks and Edge Cases) > Stage 7 (Cross-Process Handoff).

Pre-write checklist:
- [ ] Variant Declaration present with reason field completed
- [ ] Every R-ID has a named First-Touch Point and SLA Clock
- [ ] Every R-ID cited in any stage appears in the handoff table
- [ ] Every exception flow has SLA impact with quantitative or directional timing
- [ ] Stage 6 edge cases are distinct from Stage 4 exception flows
- [ ] Every path reaches a declared T-ID

---

## V-04 -- Combined (Lifecycle Emphasis + Inertia Framing): Surgical C-13 Layer

**Variation axes combined:**
1. Lifecycle emphasis -- V-02 R1's SLA-first per-phase architecture (proven 100/100 under v20)
2. Inertia framing -- limited to the BOTTLENECK SYNTHESIS section only; no full dual-trace overhead

**Hypothesis:** V-02 R1 scored 100/100 under v20 and projects to 110/115 under v21 (C-13 not earned because no variant framing). Full dual-trace (V-03 R1 / V-02 R2) doubles output length. The minimum required for C-13 is a BOTTLENECK SYNTHESIS with three-field trajectory entries (as-is status, to-be status, net change). Injecting variant framing only at the PROCESS CONTEXT and BOTTLENECK SYNTHESIS sections earns C-13 without restructuring the core phase-loop. With C-11 breach verdict and C-12 exception SLA impact also added, the combination targets 115/115 at lower output complexity than full dual-trace.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

---

**PROCESS CONTEXT**

```
Lifecycle:         [name of process]
Current state:     [brief description of how this process runs today -- tool, medium, manual steps]
Target state:      [the system or automation target, if any -- or "same as current" if no migration in scope]
Variant framing:   [single-variant trace (current state only) /
                    dual-variant trace (current state compared to target state)]
```

If Variant framing = single-variant, BOTTLENECK SYNTHESIS uses the single-variant form.
If Variant framing = dual-variant, BOTTLENECK SYNTHESIS uses the trajectory form.

---

**LIFECYCLE PHASES**

| Ph-ID | Phase Name | Purpose | Entry Trigger | SLA Envelope (expected) |
|-------|-----------|---------|--------------|------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**FOR EACH PHASE -- repeat this block for every Ph-ID:**

---

**PHASE ENTRY CONTRACT -- [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | [Ph-ID or INITIAL] |
| Roles active | [domain-qualified role names] |
| Objects entering | [named artifacts or records] |
| Exception pre-check | [conditions that block entry and route to exception] |
| SLA clock start | [event that starts the timing clock] |

**STATE TRACE -- [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Exit Transition | Exit Owner (domain role) | Exception Exit |
|------|------------|-----------------|-----------------|--------------------------|---------------|
| | | | | | |

State names must be unambiguous identifiers.

**DECISION POINTS -- [Ph-ID: Phase Name]**

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
| Primary blocker | [role, resource, or condition] |
| SLA at-risk threshold | [elapsed time at which this phase is at-risk] |
| Breach verdict | [Y / N] |
| Breach cause | [required if Y: specific condition causing breach in this scenario] |

---

*Repeat PHASE ENTRY CONTRACT + STATE TRACE + DECISION POINTS + PHASE EXIT GATE for every Ph-ID.*

---

**PARALLEL PATH ANALYSIS**

```
Fork state:      [S-ID or Ph-ID]
Branch A:        [activity + owner (domain-qualified)]
Branch B:        [activity + owner (domain-qualified)]
Join condition:  [what must be true to merge]
Time saving:     [estimated savings vs sequential]
Merge owner:     [domain-qualified role]
```

If sequential, declare explicitly with reason. Explicit absence earns C-06 credit.

---

**EXCEPTION FLOW CATALOG**

At least one exception per lifecycle phase.

```
Exception:     [name]
Phase:         [Ph-ID]
Trigger:       [specific condition in domain terms]
Deviation:     [divergence from normal phase sequence]
SLA impact:    [timing consequence -- quantitative or directional:
                  "adds 3+ days to PO approval phase; triggers breach of PH-02 threshold"
                  "cascades to PH-03; resets downstream SLA clock by 5+ days"
                "may cause delays" does not satisfy this field]
Recovery:      [T-ID or recovery S-ID]
```

---

**EDGE CASE CATALOG**

At least 3 edge cases distinct from the exception flows. Edge cases are design gaps -- scenarios the lifecycle has no path for.

```
Edge case:        [name]
Phase:            [Ph-ID]
Trigger:          [condition]
Why unhandled:    [missing step or decision rule in the current design]
SLA risk:         [quantitative or directional effect on phase timing]
Correct handling: [what the process should do]
```

---

**BOTTLENECK SYNTHESIS**

Review each Phase Exit Gate where Breach verdict = Y. If no phase breaches, identify the two most vulnerable under peak conditions.

**Single-variant form** (use when Variant framing = single-variant):

| B-ID | Phase (Ph-ID) | Root Cause | Downstream Cascade | Target-State Note |
|------|--------------|------------|-------------------|------------------|
| B-01 | | | | [would this bottleneck be eliminated or shifted by the stated target state, if any?] |
| B-02 | | | | |

**Dual-variant trajectory form** (use when Variant framing = dual-variant):

| B-ID | Phase | Current-State Bottleneck | Status in Target State | New Location (if shifted) | Net Change |
|------|-------|-------------------------|----------------------|--------------------------|-----------|
| B-01 | | | eliminated / shifted / residual | | [better / worse / shifted -- overall assessment] |
| B-02 | | | | | |

Status: **eliminated** = gone in target state. **shifted** = moves to a different step or phase (new location required). **residual** = persists unchanged. Net Change must assess process speed/quality overall. A trajectory entry without the net-change assessment is a partial pass on C-13.

Additionally, at least 1 process gap:

| G-ID | Phase | Missing Step | Real-World Requirement | Risk |
|------|-------|-------------|----------------------|------|
| G-01 | | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | SLA Outcome | Reached From |
|------|--------------|------|-------------|-------------|
| T-01 | | success / failure / cancel | on-time / breached / N/A | |
| ... | | | | |

Terminal gate: every S-ID and exception Recovery state must either continue to another S-ID or appear in "Reached From."

---

**CROSS-PROCESS HANDOFF**

| Handoff trigger | Recipient process | Fields passed | Acceptance condition | SLA dependency |
|-----------------|------------------|---------------|---------------------|---------------|
| | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Process Context > Lifecycle Phases > Per-Phase Blocks > Parallel Path Analysis > Exception Flow Catalog > Edge Case Catalog > Bottleneck Synthesis (single or dual-variant per Process Context) > Terminal Declaration > Cross-Process Handoff.

Pre-write checklist:
- [ ] Process Context completed with Variant framing declared
- [ ] Every phase has SLA Envelope, breach verdict, and (if Y) breach cause
- [ ] Every exception has SLA impact with quantitative or directional timing
- [ ] Bottleneck Synthesis uses the correct form for the declared variant framing
- [ ] If dual-variant: every bottleneck has eliminated/shifted/residual + net change assessment
- [ ] Every path reaches a declared T-ID

---

## V-05 -- Combined (Phrasing Register Fixed + Lifecycle Emphasis)

**Variation axes combined:**
1. Phrasing register -- conversational, scenario-led (V-04 R1 axis)
2. Lifecycle emphasis -- SLA fields per phase as required sub-questions (V-02 R1 axis)

**V-04 R1 failure analysis (all three failures fixed in this variation):**
- C-01 partial: no S-ID enforcement; states named in prose failed the unambiguous identifier test. Fix: add STATE LEDGER pre-step requiring S-ID assignments before the walkthrough begins.
- C-04 partial: "The cases nobody wrote a rule for" asked for edge cases, not missing steps. Gap requirement unmet. Fix: split into two separate questions -- "Missing steps" and "Cases nobody wrote a rule for."
- C-06 partial: "If two things happen simultaneously" allowed silent omission when the author judged no parallelism. Fix: replace with an explicit "parallel or sequential?" declaration required per phase.

**New in V-05 R2:**
- SLA breach verdict added as a per-phase conversational sub-question (C-11)
- SLA impact added as a per-exception sub-question (C-12)
- VARIANT DECLARATION closing block for C-13 single-state exemption

**Hypothesis:** V-04 R1's conversational register produces richer domain language and more realistic bottleneck narratives than table-driven formats -- its 83/100 score was not intrinsic to the register but to three specific enforcement gaps. With four structural guardrails added (state ledger, gap question, parallel declaration, SLA impact sub-question), the register's strengths are preserved while the rubric gaps are closed. Target: all essential and recommended pass + C-09/C-10/C-11/C-12 aspirational pass + C-13 via closing declaration.

---

You are a seasoned domain expert who has worked this process long enough to know exactly where it slows down, where it breaks, and what nobody documented. Walk through the full lifecycle of the process described in the signal.

---

**Who's involved, and when do they show up?**

Tell me every person who touches this process. Give each one a real job title -- not "approver" or "user" but the specific role in this domain (e.g., the Revenue Accountant who closes the period, the Sales Admin who enters the order). For each role, tell me:
- Their job title (domain-qualified)
- When they first enter the process -- which step or event puts the document in their hands
- What decision or action belongs exclusively to them

---

**Name the states before you walk them**

Before walking the process phase by phase, produce a STATE LEDGER. This is a numbered list of every named state in the lifecycle.

For each entry:
- State identifier (e.g., S-01, S-02...)
- State name -- specific and unambiguous (e.g., "Invoice Pending 3-Way Match" not "the matching stage")
- Which role owns this state

This ledger is required. A state described later in the walkthrough that does not appear in the ledger has no named state and does not count toward coverage. Add states to the ledger as you write them; the ledger must be complete before writing the artifact.

---

**What are the phases, and how long should each one take?**

Before walking step by step, name the phases. A phase is a meaningful chunk of the lifecycle with a clear beginning and a clear "done" condition.

For each phase, answer:
- What is this phase trying to accomplish?
- What triggers it?
- How long does this normally take from entry to exit? Give a real number -- "it depends" is not an answer.
- What is the at-risk threshold -- when does being late in this phase start causing visible downstream problems?
- What is the most common reason this phase stalls?

---

**Walk me through the process, phase by phase**

For each phase:

*Opening:* How does this phase start? What just happened that put the process here?

*Normal path:* Walk through step by step. At every decision point: what is the question, who answers it (use their job title), what happens if yes, what happens if no, what happens if no one answers at all?

*Parallel or sequential?* Does anything run concurrently in this phase, or is it entirely sequential? You must declare one or the other -- silence is not an answer. If concurrent, walk both threads and state what the process waits for before continuing past the fork. If sequential, say why.

*Phase completion:* What must be true for this phase to be finished? Who signs off? What change to a document or record makes it official?

*Timing pressure:* What is the normal SLA for this phase? What is the at-risk threshold? Does the scenario you are tracing breach that threshold? If yes, state exactly what causes the breach. If no, confirm the phase is within threshold.

*Exception exits:* What can go wrong in this phase that sends the process off the normal path? For each: what triggers it, how does it diverge, what is the SLA impact in days or threshold language (not "may cause delays"), and where does it land?

---

**Missing steps**

After walking all the phases, name the steps the lifecycle design does not include but that real-world execution actually requires. At least 1. For each:
- Which phase does it belong to?
- Why does the current lifecycle design omit it?
- What breaks or gets done informally when the step is absent?

---

**The cases nobody wrote a rule for**

Name at least 2 edge cases -- valid but rare scenarios the lifecycle has no path for. These are not the exception exits from the walkthrough; those are reachable paths in the current design. Edge cases are design gaps -- situations the process was never designed to handle. For each:
- What triggers it?
- Why does the current design leave it unhandled?
- What is the risk or consequence?
- What should the process do?

---

**Where does time go?**

Now that you have walked the whole process, call out the 2 or 3 places where elapsed time is the real risk. For each:
- Which phase and which step?
- What is the normal SLA?
- What backs up behind it when it slips?
- In the scenario you traced, did this step breach its threshold?

---

**How does it end?**

List every way this process can terminate. For each terminal state, say whether it is a success, a failure, or a cancellation. Every path walked above must land on one of these.

---

**Connections to other processes**

If this process hands off to another process -- or depends on one to provide inputs -- describe that connection: what triggers the handoff, what information moves, what does the receiving process need before it accepts, and does a delay in this lifecycle breach a timing obligation in the adjacent process?

---

**Variant declaration**

Before writing the artifact, state whether this walkthrough traces a single operational state (no as-is/to-be comparison) or a dual-state comparison. If single-state, name the reason no variant comparison applies. If dual-state, note in the bottleneck analysis how each bottleneck's status differs between the two states.

---

**Write the artifact**

Produce the lifecycle artifact at `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

The artifact must contain, in order:
1. Role list with domain-qualified titles and first-touch points
2. State Ledger with S-IDs, state names, and owners
3. Phase list with SLA envelopes and at-risk thresholds
4. Phase walkthrough (normal path, parallel/sequential declaration, phase completion, timing pressure with breach verdict, exception exits with SLA impact)
5. Missing steps
6. Edge cases (distinct from exception exits)
7. Bottleneck synthesis
8. Terminal state list
9. Cross-process connections
10. Variant declaration

Every role must have a domain-qualified name. Every state in the walkthrough must match an S-ID in the State Ledger. Every phase must have an SLA envelope, an at-risk threshold, and a breach verdict for the scenario traced. Every exception exit must include an SLA impact statement in days or threshold language. Every path must reach a named terminal.
