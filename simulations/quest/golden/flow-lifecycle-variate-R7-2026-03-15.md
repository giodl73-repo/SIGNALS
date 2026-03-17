---
skill: flow-lifecycle
round: 7
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v26-2026-03-15.md
---

# flow-lifecycle -- Round 7 Variations

Round 7 carries forward the R6 V-05 baseline (160/160 under v26) and explores three structural axes that do not touch the C-19/C-20/C-21/C-22 cluster -- those criteria are already maximally satisfied by the 4-row Outcome Conditions table and the FM-A/FM-B checklist item. R7 tests whether surface-level structural changes affect author compliance while leaving all scoring-critical content requirements intact.

**R6 V-05 baseline under v26**: 160/160. C-21 PASS (4-row Outcome Conditions table names FM-A, FM-B, PM-1, PM-2). C-22 PASS (checklist item names FM-A and FM-B by label, positioned post-fill). All other criteria pass.

**R7 challenge**: Apply three structural variation axes to the v26-compliant baseline. Every variation must score 160/160 under v26. Axis changes must not degrade any C-01 through C-22 criterion. New structure must add author guidance value, not cosmetic difference only.

Single-axis variations: V-01 (Role Sequence -- lifecycle-type-driven role derivation), V-02 (Phrasing Register -- conversational imperative throughout), V-03 (Inertia Framing -- as-is process anchor before Step 1).
Combined variations: V-04 (V-01 + V-03: lifecycle context + as-is anchor, formal register), V-05 (all three axes: full maximum candidate).

---

## V-01 -- Role Sequence Axis: Lifecycle-Type-Driven Role Derivation

**Variation axis:** A **LIFECYCLE CONTEXT** block is inserted before FIELD CONTENT RULES. It maps the signal to one of four lifecycle types (L2O, P2P, Period Close, Case Lifecycle) and lists expected functional roles for that type as starting candidates. Step 1 (Domain Role Registry) becomes a confirm-and-extend step: authors validate the suggested roles, replace generic labels with implementation-specific titles, and add any roles the type table omitted. Roles enter the trace with a classification context rather than from a blank table.

**Hypothesis:** The current prompt opens with an empty R-ID table. An author who has not mentally loaded the role domain may fill it with under-specified roles (Finance team, Approver) before the state-trace pressure of Step 3 forces a correction that never gets made. Front-loading expected roles from the lifecycle type activates C-05 compliance at context-load time. The auto-selection heuristic also makes the skill description's "stock roles: domain experts auto-selected from process context" clause explicit in the prompt rather than implied by the skill header.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Begin by classifying the lifecycle type -- this determines the expected domain roles. Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**LIFECYCLE CONTEXT**

Identify the lifecycle type from the signal. Match to the closest category. The Expected Domain Roles column lists starting candidates -- not a complete list. Adjust for your implementation in Step 1.

| Lifecycle Type | Signal Indicators | Expected Domain Roles |
|---------------|-------------------|-----------------------|
| Lead-to-Order (L2O) | opportunity, quote, deal, order, customer, CRM | Account Executive, Sales Operations Analyst, Credit Analyst, Order Management Clerk, Sales Director |
| Procure-to-Pay (P2P) | purchase requisition, PO, goods receipt, invoice, payment, vendor | Procurement Officer, AP Clerk, Receiving Clerk, Controller, Budget Owner |
| Period Close | journal entry, reconciliation, accrual, ledger, period, close, consolidation | Revenue Accountant, FP&A Analyst, Accounting Manager, Controller, External Auditor |
| Case Lifecycle | case, ticket, incident, resolution, escalation, SLA, support | Case Manager, Service Desk Lead, Subject Matter Expert, Compliance Officer, Escalation Manager |
| Other | (not matched above) | Derive roles from the process description -- name the functional title, not the org unit |

```
Lifecycle type detected:    [fill in]
Expected roles identified:  [list from table above, adjusted for this implementation]
```

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Confirm and extend the roles identified in LIFECYCLE CONTEXT. Replace any generic label with the named functional title this specific process uses. Add roles the type table omitted. Every role must be tied to a decision domain.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail even if listed in the LIFECYCLE CONTEXT starting list. Every decision gate must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

Name every lifecycle phase before writing any states.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold"). "May cause delays" is a fail -- no phase, no magnitude.

---

**STEP 6 -- TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for -- distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak"). "May affect timing" is a fail -- no Ph-ID, no magnitude.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration -- complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT` is declared here: skip Tables 8a and 8b. In Step 9, every Breach Link cell receives the token `SLA-ABSENT`. Do not leave Breach Link cells blank -- carry the declaration forward.
- If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link -- Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: you have evidence and did not cite it |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: you had the token and did not use it |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" is a fail -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail -- no states named, no consequence type.

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify -- example fail: "improves audit trail" (no specific rule or dependency cited).
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a fail.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`. If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" is a fail -- no classification, no location for shifted.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] LIFECYCLE CONTEXT completed. Lifecycle type named. Expected roles identified.
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 1: All roles are domain-qualified functional titles. No generic labels.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Identified SLA evidence status. No FM-A (has evidence, used general language) or FM-B (no evidence, left blank) conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

---

## V-02 -- Phrasing Register Axis: Conversational Imperative

**Variation axis:** The formal "STEP N -- NAME" header format is replaced with a conversational imperative register. Each section opens with a direct-action sentence framing what the author must do and why, before presenting the schema. Field rules use second-person imperative. The Outcome Conditions table, SLA token vocabulary, and completion checklist are preserved structurally with the same content; only the voice changes. All table schemas and column definitions are identical to the R6 V-05 baseline.

**Hypothesis:** The formal step-header format is evaluator-legible but may create friction for an author working through the prompt interactively -- the imperative is buried after the label. A conversational register ("Before you trace any state, lock in your role vocabulary") activates the compliance intent at sentence 1 of each section rather than at sentence 2 or 3. This tests whether register affects completeness without changing content requirements. If output quality is equivalent, the formal register is preferred for its auditability; if the conversational register produces better-populated fields, it is a superior author-facing format.

---

You are a business-process simulation expert. Your job is to simulate the full lifecycle of the document or process named in the signal -- every state, every transition, every exception path, every terminal. Work through the sections below in order. Do not skip ahead. Each section tells you what to produce and what makes an entry pass or fail.

Before you open any table, read the **FIELD CONTENT RULES** block below. It tells you what qualifies and what fails for every constrained field. The rules at each section reinforce it inline. Step 8 sets up your SLA vocabulary; Step 9 uses it. These dependencies run forward -- you cannot fill Step 9 correctly without completing Step 8 first.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

---

**1. Lock in your role vocabulary first.**

Before you trace any state, name every domain role this lifecycle uses. Use the functional title the process actually uses -- not org-chart categories. You will reference these R-IDs at every decision gate; a vague role here cascades to every step that cites it.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

If you write "User", "Approver", "Admin", or "Finance team" -- that is a fail. Every decision gate must cite an R-ID.

---

**2. Name your phases before you name your states.**

You cannot trace a state without knowing which phase contains it. List every phase here. Each phase has a purpose and knows where it came from.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**3. Trace every state with its entry trigger and exit trigger.**

You need at least 6 named states. For each one: what triggered it, what happens, and how does the process leave it? Do not describe a state in prose without naming it.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision points** -- you need at least 3. For each one, name the question being decided, who decides it, every downstream branch, and the fallback if the decision cannot be made. Omitting the owner role is a partial fail.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel paths** -- identify at least one fork that runs concurrent activities before rejoining. Name the join condition: what must be true before the lifecycle resumes the main sequence. If this lifecycle genuinely has no parallel paths, say so explicitly -- silence is not a declaration.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**4. Declare how each phase ends.**

For each phase, name the exit gate. Include the SLA envelope here -- you will need it when you reach Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**5. Catalog every exception -- what derails the happy path and where it ends up.**

You need at least 3. For SLA Impact: you must name the phase (Ph-ID), the timing consequence, and whether the breach threshold fires. See FIELD CONTENT RULES.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" fails -- no phase, no magnitude.

---

**6. Name every terminal state -- success and failure.**

Every path in the trace must end somewhere named. Do not leave a branch pointing at nothing.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

You need at least one success terminal and at least one failure or cancel terminal.

---

**7. Surface the edge cases the lifecycle design ignores.**

Edge cases are scenarios that are logically reachable but absent from the lifecycle design -- they are not exceptions (Step 5) because the process has no handler for them at all. You need at least 2. For SLA Risk: name the specific phase threshold at risk and the directional consequence. See FIELD CONTENT RULES.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" fails -- no Ph-ID, no magnitude.

---

**8. Establish your SLA vocabulary before the bottleneck register.**

Step 9 requires a typed SLA reference in every Breach Link cell. You establish that evidence here. If this lifecycle has no SLA targets, declare it now so Step 9 knows to use the `SLA-ABSENT` token instead.

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**Declare your SLA status before opening any table:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT`: skip Tables 8a and 8b. Carry the token to every Breach Link cell in Step 9. Do not leave those cells blank.
- If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y with a cause traceable to a specific bottleneck or exception.

---

**9. Register every bottleneck -- what stalls the process and where it shows up in the SLA data.**

You need at least 2. The Breach Link column has exactly four valid outcomes. Identify your SLA status from Step 8, then follow the matching row:

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: you have evidence and did not cite it |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: you had the token and did not use it |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" fails -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" fails -- no states named, no consequence type.

---

**10. Name every step the lifecycle is missing.**

At least 1 gap. Use the three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent` -- vague entries fail both fields.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule), handoff precondition (name the downstream state that needs this step's output), or system dependency (name the system that fails without it). "Best practice" fails -- "improves audit trail" has no rule or dependency.
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" fails.

---

**11. Identify where this lifecycle hands off to another process.**

At least 1 cross-lifecycle dependency. Name the trigger, the receiving process, what gets passed, and what the receiver requires to accept it.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**12. Audit your exception coverage -- confirm the catalog is complete, not just populated.**

For every phase you named in Step 2, check whether you have an exception handler. Name the risk for any phase that has none. If every phase is covered, say so explicitly -- silence is not a declaration of coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**13. Track every bottleneck across the process transition.**

For each bottleneck in Step 9, show where it stands in the current process and where it ends up in the target process. See FIELD CONTENT RULES for `Net Change`. If this is a net-new process with no as-is state, declare "Single-state: [reason]" -- do not leave the trajectory blank.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" fails -- no classification, no location.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Before you write, confirm every item below:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Identified SLA evidence status. No FM-A (has evidence, used general language) or FM-B (no evidence, left blank) conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

---

## V-03 -- Inertia Framing Axis: As-Is Process Anchor

**Variation axis:** An **AS-IS ANCHOR** block is inserted before FIELD CONTENT RULES. It captures the current state of the process being simulated: how it is managed today, known pain points with named steps and failure modes, key constraints, and the inertia cost of leaving the current process unchanged. If no as-is state exists, the author declares "New Process" with a reason. Step 13 (Bottleneck Trajectory) explicitly references the AS-IS ANCHOR as the source of the as-is column rather than requiring authors to reconstruct that baseline at trajectory time.

**Hypothesis:** C-13 (Bottleneck Trajectory Analysis) requires an as-is vs. to-be comparison, but the current prompt leaves the as-is baseline implicit -- authors must construct it from the trace during Step 13, at which point form-closing pressure often produces generic entries ("manual process today") rather than named state comparisons. Front-loading the as-is anchor makes the trajectory baseline a first-class artifact: established once, at the start, referenced throughout. The "Single-state" declaration for net-new processes is also made explicit upfront rather than discovered as an afterthought at Step 13.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Begin by anchoring the as-is state of the process -- this establishes the baseline for Step 13's trajectory analysis. Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**AS-IS ANCHOR**

Before tracing the target lifecycle, establish the current process baseline. This anchor is the reference for Step 13's as-is column. Complete all fields. If this is a net-new process with no current-state equivalent, declare it explicitly.

```
Process type today:    [manual / semi-automated / legacy system / other -- name it]
Known pain points:     [2-3 named bottlenecks in the current process -- name the step and the failure mode;
                        e.g., "Manual PO approval queue: AP Clerk batches approvals weekly, 3-5 day delay"]
Key constraints:       [time, regulatory, or system constraints currently shaping the process]
Inertia cost:          [what it costs to leave the current process unchanged -- SLA exposure, error rate,
                        manual effort, compliance risk -- be specific]
```

If no as-is baseline exists: `New Process: [one sentence explaining why no current-state equivalent applies]`

A completed AS-IS ANCHOR is required before Step 13. Leaving it blank and filling trajectory fields from memory is a fail.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Before tracing any state, declare the domain-specific roles this lifecycle uses. Replace every generic label with the named functional title the process actually uses.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. Every decision gate must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

Name every lifecycle phase before writing any states.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold"). "May cause delays" is a fail -- no phase, no magnitude.

---

**STEP 6 -- TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for -- distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak"). "May affect timing" is a fail -- no Ph-ID, no magnitude.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration -- complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT` is declared here: skip Tables 8a and 8b. In Step 9, every Breach Link cell receives the token `SLA-ABSENT`. Do not leave Breach Link cells blank -- carry the declaration forward.
- If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link -- Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: you have evidence and did not cite it |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: you had the token and did not use it |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" is a fail -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail -- no states named, no consequence type.

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify -- example fail: "improves audit trail" (no specific rule or dependency cited).
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a fail.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status from the as-is baseline (AS-IS ANCHOR above) to the target state. The As-Is State column must reflect the pain points and current-process description in the AS-IS ANCHOR -- do not reconstruct the baseline here. If the AS-IS ANCHOR declared "New Process," write "Single-state: New Process" in every As-Is State cell. See FIELD CONTENT RULES for `Net Change`.

| B-ID | As-Is State (from AS-IS ANCHOR) | Target State (or "Single-state: [reason]") | Net Change |
|------|----------------------------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" is a fail -- no classification, no location for shifted.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: AS-IS Anchor > Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] AS-IS ANCHOR completed. Process type named. Pain points named with steps and failure modes. If new process, declared explicitly.
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Identified SLA evidence status. No FM-A (has evidence, used general language) or FM-B (no evidence, left blank) conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 13: As-Is State drawn from AS-IS ANCHOR. Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

---

## V-04 -- Combined: V-01 + V-03 (Lifecycle Context + As-Is Anchor, Formal Register)

**Variation axis (V-01 + V-03):** Combines the LIFECYCLE CONTEXT block from V-01 -- lifecycle type classification and expected role derivation before Step 1 -- with the AS-IS ANCHOR block from V-03 -- current process baseline before FIELD CONTENT RULES. Step 1 (Domain Role Registry) is a confirm-and-extend step derived from LIFECYCLE CONTEXT. Step 13 (Bottleneck Trajectory) draws its as-is column from the AS-IS ANCHOR rather than from author recall. Formal step-header register is preserved. FIELD CONTENT RULES, inline field rules, Outcome Conditions table, and completion checklist are identical to R6 V-05.

**Hypothesis:** V-01 addresses the role-domain loading problem (Step 1 is filled before the author has domain context loaded). V-03 addresses the trajectory-reconstruction problem (Step 13 as-is column is built from memory rather than from a named baseline). Together they bookend the two sections where implicit context requirements most often produce under-specified content. LIFECYCLE CONTEXT establishes who is in the process; AS-IS ANCHOR establishes what state the process is currently in. Neither block changes any scoring-critical content rule.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Begin by classifying the lifecycle type and anchoring the current process state. Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**LIFECYCLE CONTEXT**

Identify the lifecycle type from the signal. Match to the closest category. The Expected Domain Roles column lists starting candidates -- adjust for your implementation in Step 1.

| Lifecycle Type | Signal Indicators | Expected Domain Roles |
|---------------|-------------------|-----------------------|
| Lead-to-Order (L2O) | opportunity, quote, deal, order, customer, CRM | Account Executive, Sales Operations Analyst, Credit Analyst, Order Management Clerk, Sales Director |
| Procure-to-Pay (P2P) | purchase requisition, PO, goods receipt, invoice, payment, vendor | Procurement Officer, AP Clerk, Receiving Clerk, Controller, Budget Owner |
| Period Close | journal entry, reconciliation, accrual, ledger, period, close, consolidation | Revenue Accountant, FP&A Analyst, Accounting Manager, Controller, External Auditor |
| Case Lifecycle | case, ticket, incident, resolution, escalation, SLA, support | Case Manager, Service Desk Lead, Subject Matter Expert, Compliance Officer, Escalation Manager |
| Other | (not matched above) | Derive roles from the process description -- name the functional title, not the org unit |

```
Lifecycle type detected:    [fill in]
Expected roles identified:  [list from table above, adjusted for this implementation]
```

---

**AS-IS ANCHOR**

Establish the current process baseline before tracing the target lifecycle. This anchor is the reference for Step 13's as-is column. If this is a net-new process, declare it.

```
Process type today:    [manual / semi-automated / legacy system / other -- name it]
Known pain points:     [2-3 named bottlenecks in the current process -- name the step and the failure mode;
                        e.g., "Manual PO approval queue: AP Clerk batches approvals weekly, 3-5 day delay"]
Key constraints:       [time, regulatory, or system constraints currently shaping the process]
Inertia cost:          [what it costs to leave the current process unchanged -- be specific]
```

If no as-is baseline exists: `New Process: [one sentence explaining why no current-state equivalent applies]`

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Confirm and extend the roles identified in LIFECYCLE CONTEXT. Replace any generic label with the named functional title this specific process uses. Add roles the type table omitted. Every role must be tied to a decision domain.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail even if they appeared in the LIFECYCLE CONTEXT starting list. Every decision gate must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

Name every lifecycle phase before writing any states.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" is a fail -- no phase, no magnitude.

---

**STEP 6 -- TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for -- distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" is a fail -- no Ph-ID, no magnitude.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration -- complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT` is declared here: skip Tables 8a and 8b. In Step 9, every Breach Link cell receives the token `SLA-ABSENT`. Do not leave Breach Link cells blank -- carry the declaration forward.
- If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link -- Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: you have evidence and did not cite it |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: you had the token and did not use it |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" is a fail -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail -- no states named, no consequence type.

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify -- example fail: "improves audit trail" (no specific rule or dependency cited).
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a fail.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status from the as-is baseline (AS-IS ANCHOR above) to the target state. The As-Is State column must draw on the pain points named in the AS-IS ANCHOR. If the AS-IS ANCHOR declared "New Process," write "Single-state: New Process" in every As-Is State cell. See FIELD CONTENT RULES for `Net Change`.

| B-ID | As-Is State (from AS-IS ANCHOR) | Target State (or "Single-state: [reason]") | Net Change |
|------|----------------------------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" is a fail -- no classification, no location for shifted.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Context > AS-IS Anchor > Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] LIFECYCLE CONTEXT completed. Lifecycle type named. Expected roles identified.
- [ ] AS-IS ANCHOR completed. Process type named. Pain points named with steps and failure modes. If new process, declared explicitly.
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 1: All roles are domain-qualified functional titles. No generic labels.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Identified SLA evidence status. No FM-A (has evidence, used general language) or FM-B (no evidence, left blank) conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 13: As-Is State drawn from AS-IS ANCHOR. Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

---

## V-05 -- Full Combination: All R7 Axes + R6 V-05 Carry-Forward

**Variation axis (V-01 + V-02 + V-03 + R6 V-05 carry-forward):** Combines all three R7 axes -- LIFECYCLE CONTEXT and confirm-and-extend Role Registry (V-01), conversational imperative register throughout (V-02), AS-IS ANCHOR with Step 13 explicit reference (V-03) -- with the complete R6 V-05 carry-forward: FIELD CONTENT RULES global catalog, per-step inline field rules, 4-row Outcome Conditions table at Step 9 (FM-A, FM-B, PM-1, PM-2), and completion checklist naming FM-A and FM-B by label.

Three layers of context scaffolding: LIFECYCLE CONTEXT establishes who is in the process before any role table is opened; AS-IS ANCHOR establishes what state the process is in before any state is traced; conversational register activates each compliance intent at the first sentence of each section. The C-21/C-22 mechanisms are preserved without change.

**Hypothesis:** Each structural axis addresses a different author failure mode: (a) LIFECYCLE CONTEXT prevents role under-specification at the point of first domain contact; (b) AS-IS ANCHOR prevents trajectory reconstruction failure at Step 13; (c) conversational register reduces the activation distance between section header and compliance intent. Combined, these three scaffolds address the three most common under-specification patterns while leaving every scoring-critical content rule intact. Maximum-composite scoring target: 160/160 under v26.

---

You are a business-process simulation expert. Your job is to simulate the full lifecycle of the document or process named in the signal -- every state, every transition, every exception, every terminal. Work through the sections below in order. Do not skip ahead.

Start by classifying the lifecycle type and anchoring the current process baseline. Both inform what you write later. Once those are set, read FIELD CONTENT RULES before opening any table. Each section also includes inline field rules at the moment you need them. Step 8 sets your SLA vocabulary; Step 9 uses it. These dependencies run forward -- you cannot correctly fill Step 9 without completing Step 8 first.

---

**LIFECYCLE CONTEXT**

Classify the lifecycle type from the signal. The Expected Domain Roles column gives you starting candidates for your role vocabulary -- confirm and extend them in Section 1.

| Lifecycle Type | Signal Indicators | Expected Domain Roles |
|---------------|-------------------|-----------------------|
| Lead-to-Order (L2O) | opportunity, quote, deal, order, customer, CRM | Account Executive, Sales Operations Analyst, Credit Analyst, Order Management Clerk, Sales Director |
| Procure-to-Pay (P2P) | purchase requisition, PO, goods receipt, invoice, payment, vendor | Procurement Officer, AP Clerk, Receiving Clerk, Controller, Budget Owner |
| Period Close | journal entry, reconciliation, accrual, ledger, period, close, consolidation | Revenue Accountant, FP&A Analyst, Accounting Manager, Controller, External Auditor |
| Case Lifecycle | case, ticket, incident, resolution, escalation, SLA, support | Case Manager, Service Desk Lead, Subject Matter Expert, Compliance Officer, Escalation Manager |
| Other | (not matched above) | Derive roles from the process description -- name the functional title, not the org unit |

```
Lifecycle type detected:    [fill in]
Expected roles identified:  [list from table above, adjusted for this implementation]
```

---

**AS-IS ANCHOR**

Before you trace a single state, establish what the process looks like today. This is the source for Section 13's as-is column -- you will not reconstruct it there. If this is a net-new process, declare it here.

```
Process type today:    [manual / semi-automated / legacy system / other -- name it]
Known pain points:     [2-3 named bottlenecks in the current process -- name the step and the failure mode;
                        e.g., "Manual PO approval queue: AP Clerk batches approvals weekly, 3-5 day delay"]
Key constraints:       [time, regulatory, or system constraints currently shaping the process]
Inertia cost:          [what it costs to leave the current process unchanged -- be specific]
```

If no as-is baseline exists: `New Process: [one sentence explaining why no current-state equivalent applies]`

---

**FIELD CONTENT RULES**

Before opening any table, read this. Every field listed here has a positive qualifier (what earns credit) and a disqualifying example (what fails). The inline rules in each section reinforce these at the point of authoring.

| Field | Section | Qualifies when... | Does NOT qualify -- example fail |
|-------|---------|-------------------|----------------------------------|
| SLA Impact | Sec 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Sec 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Sec 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Sec 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Sec 9 | See Outcome Conditions table in Section 9 | See Outcome Conditions table |
| Why Required | Sec 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Sec 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Sec 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

---

**1. Lock in your role vocabulary -- confirm and extend what LIFECYCLE CONTEXT suggested.**

Every decision gate you trace in Section 3 will cite an R-ID. Make those IDs count now. Replace any role from the LIFECYCLE CONTEXT list that does not fit this implementation. Add any roles the list missed. Do not leave generic labels anywhere in this table.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

"User", "Approver", "Admin", "Finance team" are fails, even if they came from the LIFECYCLE CONTEXT list. Every decision gate must cite an R-ID.

---

**2. Name your phases before you name any states.**

You cannot assign a state to a phase that has not been declared. List them all here first.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**3. Trace every state with entry trigger, work done, and exit trigger.**

At least 6 named states. For each: what caused this state, what happens in it, and what event moves the process forward. Do not describe a state in prose without naming it.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision points** -- at least 3. For each one: what is the question, who decides, what are all the downstream branches, and what happens if the decision cannot be made? Omitting the owner role is a partial fail.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel paths** -- find at least one fork where two activities run concurrently before rejoining. Name the join condition: what must both branches complete before the lifecycle resumes? If there are genuinely no parallel paths, say so explicitly -- do not leave this blank.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**4. Close every phase with a named exit gate.**

Include the SLA envelope here -- you will need it in Section 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**5. Catalog every exception -- what breaks the happy path, where it diverges, and where it ends.**

At least 3. For SLA Impact, you must name the phase (Ph-ID), the timing consequence, and whether the breach threshold fires. See FIELD CONTENT RULES.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" fails -- no phase, no magnitude.

---

**6. Name every terminal -- no branch can point at nothing.**

At least one success terminal and at least one failure or cancel terminal. Every S-ID and E-ID must reach a T-ID.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

---

**7. Surface the scenarios the lifecycle design ignores entirely.**

These are edge cases -- logically reachable scenarios the design has no handler for. They are not exceptions (Section 5) because no path exists for them. At least 2. For SLA Risk, name the specific threshold at risk and the directional consequence. See FIELD CONTENT RULES.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" fails -- no Ph-ID, no magnitude.

---

**8. Set up your SLA vocabulary -- Section 9 depends on it.**

If this lifecycle has SLA targets, document them here and render breach verdicts. If it does not, declare `SLA-ABSENT` now so Section 9 knows what token to carry forward.

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Section 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**Declare your SLA status before opening any table:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT`: skip Tables 8a and 8b. Carry the token to every Breach Link cell in Section 9. Do not leave those cells blank.
- If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y with a cause traceable to a specific bottleneck or exception.

---

**9. Register every bottleneck -- what stalls the process and where it shows up in the SLA data.**

At least 2. The Breach Link column has exactly four valid outcomes -- identify your SLA status from Section 8, then follow the matching row. See FIELD CONTENT RULES for Cause and Downstream Impact.

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: you have evidence and did not cite it |
| **FM-B** (fail) | No -- Section 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: you had the token and did not use it |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No -- Section 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Section 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" fails -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" fails -- no states named, no consequence type.

---

**10. Name every step the lifecycle is missing.**

At least 1 gap. Three fields required. See FIELD CONTENT RULES for Why Required and Risk if Absent -- vague entries fail both.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule), handoff precondition (name the downstream state that needs this output), or system dependency (name the system that fails without it). "Best practice" fails -- "improves audit trail" has no rule or dependency.
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" fails.

---

**11. Find where this lifecycle hands off to another process.**

At least 1 cross-lifecycle dependency. Name the trigger, the receiving process, what gets passed, and what the receiver requires to accept it.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**12. Audit your exception coverage -- don't just list exceptions, confirm nothing is uncovered.**

For every phase in Section 2: does an exception handler exist? If not, name the risk. If every phase is covered, declare it explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**13. Track every bottleneck across the process transition -- use the AS-IS ANCHOR as your baseline.**

For each bottleneck in Section 9, the As-Is State column draws directly from the pain points named in the AS-IS ANCHOR. Do not reconstruct the as-is baseline here -- reference it. If the AS-IS ANCHOR declared "New Process," write "Single-state: New Process" in every As-Is State cell. See FIELD CONTENT RULES for Net Change.

| B-ID | As-Is State (from AS-IS ANCHOR) | Target State (or "Single-state: [reason]") | Net Change |
|------|----------------------------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" fails -- no classification, no location.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Context > AS-IS Anchor > Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Before you write, confirm every item below:**
- [ ] LIFECYCLE CONTEXT completed. Lifecycle type named. Expected roles identified.
- [ ] AS-IS ANCHOR completed. Process type named. Pain points named with steps and failure modes. If new process, declared explicitly.
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Section 1: All roles are domain-qualified functional titles. No generic labels.
- [ ] Section 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Section 9: Identified SLA evidence status. No FM-A (has evidence, used general language) or FM-B (no evidence, left blank) conditions apply to any Breach Link cell.
- [ ] Section 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Section 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Section 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Section 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Section 13: As-Is State drawn from AS-IS ANCHOR. Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Section 11: At least 1 cross-lifecycle handoff.
- [ ] Section 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.
