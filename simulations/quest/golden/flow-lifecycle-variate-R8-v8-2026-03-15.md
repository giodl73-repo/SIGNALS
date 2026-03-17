---
skill: flow-lifecycle
round: 8
rubric-version: 8
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v8-2026-03-15.md
---

# flow-lifecycle -- Round 8 / Rubric v8 Variations

Round 8 under the v8 rubric extends the R8 baseline (which introduced C-25 and C-26) with two new aspirational criteria extracted from the R7 excellence ceiling:

- **C-27 -- Scan-Table Defect Taxonomy**: The production gate causal mechanism is backed by a named scan-table column. The gate text references the column by name (e.g., "named in the Defect Type column") and enumerates ≥3 defect categories within it. The scan table provides a formal taxonomy that makes the gate's causal claim verifiable against a pre-built list.
- **C-28 -- Handler Authority Fail-Declaration Co-Location**: The Handler column header carries both the backward-trace authority rule (C-26) and inline fail-language naming the violation type and consequence, co-located at the same column definition. Neither element alone satisfies C-28; both must appear together in the single header cell.

**Invariants across all five variations**: All variations carry C-27 (scan table with named Defect Type column + gate sentence referencing it) and C-28 (Handler column header with `Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail`) as fixed structural elements. These are not variation axes -- they are the baseline the variation axes layer on top of.

**R8 V-04 baseline under v8**: The prior R8 V-04 (Scan Table + Handler Header) already satisfies C-27 and C-28. It is used as the structural foundation from which these five variations depart.

**Variation axes used**:
- Single-axis: V-01 (Role Sequence -- lifecycle-type-driven derivation), V-02 (Output Format -- maximum schema density), V-03 (Lifecycle Emphasis -- phase-first framing)
- Combined: V-04 (Role Sequence + Lifecycle Emphasis), V-05 (Output Format + Inertia Framing)

---

## V-01 -- Role Sequence: Lifecycle-Type-Driven Derivation

**Variation axis:** The prompt begins by requiring the author to name and classify the lifecycle type before any roles or phases are established. A `LIFECYCLE CONTEXT` block precedes Step 1 and specifies which domain roles are typical for each lifecycle class (L2O, P2P, Period Close, Case Lifecycle). The Role Registry step includes a `Lifecycle Class` field and a note requiring roles to be consistent with that class. The sequence is: Lifecycle Context declaration → Role Registry → Phase Map → remainder. The scan table (C-27) and Handler column header (C-28) are unchanged from baseline.

**Hypothesis:** Requiring authors to name the lifecycle class before any roles are registered constrains generic role titles at the earliest possible point. An author who has declared "P2P" cannot defensibly write "Approver" as a role title -- the lifecycle context has already established that this domain uses titles like "Accounts Payable Supervisor" and "Procurement Officer." The lifecycle anchor is a pre-constraint on role vocabulary that fires before any table is opened, reducing C-05 failures by narrowing the acceptable role-title space before any blank is filled.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**LIFECYCLE CONTEXT DECLARATION**

Before opening any section, complete this block:

```
Lifecycle type:    [ ] Lead-to-Order (L2O)
                   [ ] Procure-to-Pay (P2P)
                   [ ] Period Close
                   [ ] Case Lifecycle
                   [ ] Other: _______

Lifecycle class:   [one sentence naming the primary business outcome this lifecycle achieves]

Domain role vocabulary for this class (reference when completing Step 1):
  - L2O typical roles: Account Executive, Sales Operations Analyst, Revenue Recognition Specialist, Deal Desk Manager
  - P2P typical roles: Procurement Officer, Accounts Payable Supervisor, Receiving Clerk, Treasury Analyst
  - Period Close typical roles: Controller, Consolidations Accountant, External Audit Liaison, Tax Provision Analyst
  - Case Lifecycle typical roles: Case Manager, Subject Matter Expert, Compliance Officer, Escalation Coordinator
  - Other: derive from process context; generic titles (Approver, Reviewer, Admin) are always a fail
```

> **GATE 0**: Do not open Step 1 until the Lifecycle Context Declaration is complete and a lifecycle class is selected.

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

Name every domain role this lifecycle requires. Use functional titles consistent with the lifecycle class declared above -- not org-chart categories. Every decision gate in Step 3, every Handler cell in Step 5, and every owner in Steps 4, 9, and 12 references R-IDs from this table.

Every Handler (R-ID) entry in the Exception Catalog must resolve to a role carrying Exception Handler = Y in this table. Roles carrying N may not be assigned as exception handlers.

| R-ID | Role Name (domain-qualified, consistent with lifecycle class) | Domain | Decisions Owned | Exception Handler (Y/N) |
|------|---------------------------------------------------------------|--------|-----------------|------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

Role names that are inconsistent with the declared lifecycle class are a fail. Generic labels (User, Approver, Admin, Finance team) are always a fail regardless of class. Every decision gate must cite an R-ID. At least one role must carry Exception Handler = Y.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete, all role names are consistent with the declared lifecycle class, and at least one role carries Exception Handler = Y.

---

**STEP 2 -- PHASE MAP**

Name every lifecycle phase before writing any states. Each phase has a named entry trigger and a named completion condition.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

> **GATE B**: Do not open the State Trace until the Phase Map is complete with a named entry trigger and completion condition per phase.

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
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

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

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

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

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

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Lifecycle Context (pre-Step 1) | A lifecycle class is selected and domain role vocabulary is identified | Unanchored roles (no lifecycle class declared) | Decision gates in the artifact cite role titles not traceable to any named process domain |  |
| SC-02 | Role Registry (Step 1) | All roles are domain-qualified functional titles consistent with declared lifecycle class; no generic labels present | Generic role (e.g., "Approver") present | Decision gates in the artifact cite unresolvable owners |  |
| SC-03 | Exception Catalog (Step 5) | All Handler (R-ID) cells trace to a role carrying Exception Handler = Y in the Role Registry | Uncertified exception handler | At least one exception path in the artifact has no accountable owner |  |
| SC-04 | Terminal Declaration (Step 6) | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated path | At least one path in the artifact reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-05 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID (PM-1) or the `SLA-ABSENT` token (PM-2) | Breach analysis disconnected from SLA evidence | Bottleneck severity in the artifact cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unanchored role, a generic role, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step.

---

## V-02 -- Output Format: Maximum Schema Density

**Variation axis:** Every constraint that appears as a preamble block or field-rule note in the baseline is moved inline into the column header of the table it governs. The Field Content Rules preamble block is eliminated; instead, each column that carries a field-content rule has its constraint embedded in the header cell using "does not count," "is a fail," or "Mandatory" language at the point of use. The scan table's "Defect Type if OPEN" column header carries inline fail-language. All enforcement is concentrated in column headers; no standalone constraint blocks appear outside of the gate sentences themselves. The Lifecycle Context Declaration of V-01 is absent; role derivation is unconstrained by lifecycle class.

**Hypothesis:** When constraint language lives only in preamble blocks and field-rule notes, authors who know the schema can bypass it by reading the table headers alone. Column headers are structurally inescapable: they appear at every row entry. Moving all fail-language into column headers eliminates the bypass path -- the constraint is physically co-located with the cell that violates it. This is the point-of-use enforcement principle applied at maximum saturation. The prediction is that V-02 produces the highest C-18 and C-28 pass rate because every enforcement point is co-located with the element it constrains.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Read each table header carefully before filling rows -- all field rules are embedded in column headers at the column they govern.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

| R-ID | Role Name -- domain-qualified functional title; "Approver" / "Admin" / "User" do not count | Domain -- process area, not org unit | Decisions Owned -- cite D-IDs from Step 3; blank is a fail if role owns any decision | Exception Handler (Y/N) -- at least one Y required; roles carrying N may not appear in any Handler cell |
|------|--------------------------------------------------------------------------------------------|--------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

---

**STEP 2 -- PHASE MAP**

> **GATE B**: Do not open the State Trace until every phase has a named entry trigger and completion condition.

| Ph-ID | Phase Name | Entry Trigger -- names the event or state that opens this phase; "process begins" does not count | Completion Condition -- names the verifiable output that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "3 business days"); "as soon as possible" does not count | At-Risk Threshold -- the condition under which this SLA is breached; blank is a fail if SLA evidence applies |
|-------|------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- names the trigger or predecessor state; "after previous step" does not count | Exit Transitions -- labeled outbound paths; "then move forward" does not count | Owner (R-ID) -- must appear in Role Registry; blank is a fail |
|------|--------------|------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3:

| D-ID | Decision Name | Condition -- measurable threshold (dollar amount, day count, retry count); qualitative condition alone does not count | Owner (R-ID) -- must appear in Role Registry; blank is a fail | Branch A -- named outcome | Branch B -- named outcome; "otherwise" does not count | Fallback -- mechanism-impairment path (role unavailable, system down); "escalate" alone does not count |
|------|--------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- at least one fork-join or declare absence with rationale:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

> **GATE C**: Do not open the Terminal Declaration until all Handler cells carry a certified R-ID (Exception Handler = Y in Step 1).

At least 3 exceptions.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition that diverts from the happy path; "error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail | Deviation from Happy Path -- names the specific states bypassed or added; "different path" does not count | SLA Impact -- names Ph-ID + magnitude + breach flag; "may cause delays" is a fail | Terminal or Recovery -- T-ID or named recovery state; "resolved" does not count |
|------|--------------|----------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**STEP 6 -- TERMINAL DECLARATION**

Every S-ID and E-ID must reach a T-ID here.

| T-ID | Terminal Name | Type (success / failure / cancel) -- one of these three labels; "completed" does not count | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a fail |
|------|--------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Scenarios the lifecycle has no path for -- distinct from Step 5 exceptions. At least 2 required.

| EC-ID | Edge Case -- names a concrete scenario, not a category | Phase (Ph-ID) | Why Unhandled -- names the specific design decision or omission; "not considered" does not count | SLA Risk -- names Ph-ID + directional magnitude + breach classification; "may affect timing" is a fail | Correct Handling -- names the control or path that would address this gap |
|-------|-------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; breach-link in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [reason]
```

**Table 8a -- SLA Annotations** (if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration -- specific (e.g., "5 business days"); "timely" does not count | At-Risk? (Y/N) | Risk Cause -- names the bottleneck; "volume" alone does not count |
|--------|--------------|-----------|--------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y.

**Table 8b -- Breach Verdicts** (if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold -- cite SLA-ID or state threshold explicitly | Breach (Y/N) | Cause -- if Y: names the bottleneck condition or E-ID; "delays" alone is a fail |
|-------|--------------|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y with traceable cause.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language instead of a typed ID | **Fail** |
| **FM-B** (fail) | No -- SLA-ABSENT declared | Left cell blank instead of writing `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID: BV-ID, SLA-ID, or Ph-ID + brief description | **Full credit** |
| **PM-2** (pass) | No | Wrote `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause -- root-cause type + named element; "approval takes too long" is a fail | Downstream Impact -- names S-IDs or Ph-IDs + consequence type; "delays the process" is a fail | Breach Link -- typed ID or SLA-ABSENT; general language is a fail |
|------|--------------|-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step -- names the specific control or check omitted | Why Required -- regulatory rule / handoff precondition / system dependency; "best practice" is a fail | Risk if Absent -- SLA breach exposure / compliance failure / state inconsistency; "may cause issues" is a fail |
|------|--------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process -- names the specific lifecycle, not a category | Fields Passed -- list the specific data objects | Acceptance Condition -- names what the recipient verifies before accepting |
|-----------------|-------------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID -- must appear in Step 5 and carry Exception Handler = Y in Step 1; silence is not coverage | Risk if Uncovered -- names specific consequence; "may have issues" does not count |
|-------|------------|----------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

Full coverage declaration (if all phases are covered): _______________________

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State -- names the current bottleneck condition | Target State (or "Single-state: [reason]") | Net Change -- eliminated / shifted (name location) / residual / Single-state; "improved" is a fail |
|------|-------------------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Role Registry (Step 1) | All roles are domain-qualified functional titles; no generic labels present | Generic role present | Decision gates in the artifact cite unresolvable owners |  |
| SC-02 | Exception Catalog (Step 5) | All Handler (R-ID) cells trace to a role carrying Exception Handler = Y in the Role Registry | Uncertified exception handler | At least one exception path in the artifact has no accountable owner |  |
| SC-03 | Terminal Declaration (Step 6) | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated path | At least one path in the artifact reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-04 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID (PM-1) or the `SLA-ABSENT` token (PM-2) | Breach analysis disconnected from SLA evidence | Bottleneck severity in the artifact cannot be verified against phase-level SLA thresholds |  |
| SC-05 | Gap Register (Step 10) | Every Why Required cites a specific rule, dependency, or regulation | Unverifiable gap requirement | Gap requirement in the artifact cannot be audited against a named dependency |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (a generic role, an uncertified exception handler, an unterminated path, a breach analysis disconnected from SLA evidence, or an unverifiable gap requirement) -- and that artifact must be discarded and rebuilt from the failing step.

---

## V-03 -- Lifecycle Emphasis: Phase-First Framing

**Variation axis:** The Phase Map precedes the Role Registry. The prompt opens with phase identification and SLA envelope establishment as Step 1; the Role Registry becomes Step 2. Each phase in the phase map includes an explicit "Phase Owner (R-ID)" field that is pre-populated as a forward-reference placeholder -- the author commits to a role title at phase-naming time and then must use that same title in the Role Registry. The rationale: roles are discovered through phases, not declared in advance of them. An additional SLA Risk Declaration block appears between the Phase Map and Role Registry, requiring the author to pre-identify which phases are at SLA risk before any state or decision is written. The scan table and Handler header are unchanged from baseline.

**Hypothesis:** When phases are established first -- with SLA envelopes and phase ownership committed upfront -- the Role Registry that follows is populated from a pre-constrained vocabulary: every role the author names in Step 2 was already anticipated in Step 1. This two-pass role derivation (rough phase owner → precise registry title) reduces generic placeholder risk because phase ownership requires at least a functional approximation of the role title before the registry is opened. The pre-declared SLA Risk annotation forces the author to identify at-risk phases before any state is written, improving C-10 and C-16 pass rates by front-loading SLA vocabulary establishment.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Note that this schema places the Phase Map before the Role Registry -- this is intentional. Phases are discovered before roles because role authority derives from phase responsibility. Before opening any table, read the **FIELD CONTENT RULES** block below. Step 9 establishes SLA vocabulary. Step 10 consumes those tokens via the Outcome Conditions table.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 6 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 8 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 10 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 10 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 10 | See Outcome Conditions table in Step 10 | See Outcome Conditions table |
| Why Required | Step 11 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 11 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Step 14 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

---

**STEP 1 -- PHASE MAP WITH SLA ENVELOPE**

Name every lifecycle phase before naming any roles or states. Each phase requires entry trigger, completion condition, SLA envelope, and a preliminary phase owner designation that will be validated in Step 2.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk? (Y/N) | Preliminary Phase Owner (functional title -- will become an R-ID in Step 2) |
|-------|------------|---------------|---------------------|--------------|----------------|-----------------------------------------------------------------------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| ... | | | | | | |

**SLA Risk Declaration** -- before proceeding to Step 2, identify every phase where At-Risk = Y and name the anticipated bottleneck:

| Ph-ID | Phase Name | SLA Envelope | Anticipated Bottleneck | Risk Classification (high / medium / low) |
|-------|------------|-------------|------------------------|-------------------------------------------|
| (only rows where At-Risk = Y) | | | | |

> **GATE A**: Do not open the Role Registry until the Phase Map is complete with named entry triggers and completion conditions, and the SLA Risk Declaration is complete for all At-Risk = Y phases.

---

**STEP 2 -- DOMAIN ROLE REGISTRY**

Name every domain role this lifecycle requires. All phase owners declared in Step 1 must resolve to an R-ID in this table. Every decision gate in Step 4, every Handler cell in Step 6, and every owner in Steps 5, 10, and 13 references R-IDs from this table.

Every Handler (R-ID) entry in the Exception Catalog must resolve to a role carrying Exception Handler = Y in this table. Roles carrying N may not be assigned as exception handlers.

| R-ID | Role Name (domain-qualified) | Domain | Phase Authority (Ph-IDs this role owns) | Decisions Owned | Exception Handler (Y/N) |
|------|------------------------------|--------|-----------------------------------------|-----------------|------------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| ... | | | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. Every phase declared in Step 1 must have a Phase Authority owner in this table. At least one role must carry Exception Handler = Y.

> **GATE B**: Do not open the State Trace until the Role Registry is complete, every Phase-1 owner maps to an R-ID here, and at least one role carries Exception Handler = Y.

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- trace at least one fork-join or declare absence with rationale:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope from Step 1 is repeated here for reference.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [from Step 1 -- carry forward exactly]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 6 -- EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude, and whether the breach threshold is triggered. "May cause delays" is a fail.

---

**STEP 7 -- EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for -- distinct from Step 6 exceptions. At least 2 required.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" is a fail.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

Note: At-Risk phases were pre-identified in Step 1. Use those Ph-IDs to populate Table 8a. Table 8b produces breach verdicts that Step 10 Breach Link cells cite.

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 10 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [reason]
```

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At-Risk = Y rows should align with the SLA Risk Declaration in Step 1. At least 3 rows; at least 1 At-Risk = Y.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict.

---

**STEP 9 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 10 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. The anticipated bottlenecks from Step 1 SLA Risk Declaration should appear here.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language instead of a typed ID | **Fail** -- C-16 violation |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation |
| **PM-1** (pass) | Yes | Wrote typed ID: BV-ID, SLA-ID, or Ph-ID + description | **Full credit** |
| **PM-2** (pass) | No | Wrote `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: root-cause type + named element. "Approval takes too long" is a fail.
- **Downstream Impact**: S-ID or Ph-ID + consequence type. "Delays the process" is a fail.

---

**STEP 11 -- GAP REGISTER**

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:** same as baseline (regulatory rule / handoff precondition / system dependency required; "best practice" is a fail).

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 1, confirm handler coverage. Silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Phase Map > SLA Risk Declaration > Role Registry > State Trace > Phase Exit Gates > Terminal Declaration > Exception Catalog > Edge Case Catalog > SLA Annotation > Cross-Lifecycle Handoff > Bottleneck Register > Gap Register > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Phase Map (Step 1) | All phases have named entry triggers and completion conditions; SLA Risk Declaration complete for all At-Risk = Y rows | Unresolvable phase boundary (no entry trigger or completion condition) | The artifact's state trace cannot be verified as correctly ordered -- phase transitions are ambiguous |  |
| SC-02 | Role Registry (Step 2) | All roles are domain-qualified; all Step-1 phase owners resolve to R-IDs | Generic role or unresolved phase owner | Decision gates in the artifact cite unresolvable owners |  |
| SC-03 | Exception Catalog (Step 6) | All Handler (R-ID) cells trace to a role carrying Exception Handler = Y in the Role Registry | Uncertified exception handler | At least one exception path in the artifact has no accountable owner |  |
| SC-04 | Terminal Declaration (Step 5) | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated path | At least one path in the artifact reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-05 | Bottleneck Register (Step 10) | Every Breach Link cell contains a typed ID (PM-1) or the `SLA-ABSENT` token (PM-2) | Breach analysis disconnected from SLA evidence | Bottleneck severity in the artifact cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unresolvable phase boundary, a generic role, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step.

---

## V-04 -- Combined: Role Sequence + Lifecycle Emphasis

**Variation axes:** V-04 combines the lifecycle-type-driven role derivation of V-01 with the phase-first framing of V-03. The sequence is: Lifecycle Context Declaration → Phase Map with SLA Envelope → SLA Risk Declaration → Domain Role Registry (roles derived from lifecycle type AND phase ownership) → State Trace → remainder. The role registry step includes both the lifecycle-class constraint (from V-01) and the phase-authority mapping (from V-03). The scan table and Handler header are unchanged from baseline.

**Hypothesis:** Two-layer structural pre-certification -- (1) lifecycle class constraining role vocabulary before any phase is named, (2) phase ownership pre-committing role functional titles before the registry is opened -- creates the narrowest possible acceptable-role space at registry-fill time. The author who has declared "Period Close" and committed phase owners for "Journal Entry Review" and "Consolidation" cannot write "Approver" as a role title; the lifecycle context has already suggested "Controller" and "Consolidations Accountant," and the phase ownership commitment has locked in functional authority before the registry table opens. Prediction: V-04 produces the lowest generic-role defect rate of any variation.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. This schema places lifecycle context identification and phase mapping before role registration -- this is intentional. Roles are derived from a named lifecycle class and from pre-committed phase ownership, not declared speculatively. Read the FIELD CONTENT RULES before opening any table.

---

**LIFECYCLE CONTEXT DECLARATION**

```
Lifecycle type:    [ ] Lead-to-Order (L2O)
                   [ ] Procure-to-Pay (P2P)
                   [ ] Period Close
                   [ ] Case Lifecycle
                   [ ] Other: _______

Lifecycle class:   [one sentence naming the primary business outcome this lifecycle achieves]

Domain role vocabulary for this class (reference when completing Step 2):
  - L2O: Account Executive, Sales Operations Analyst, Revenue Recognition Specialist, Deal Desk Manager
  - P2P: Procurement Officer, Accounts Payable Supervisor, Receiving Clerk, Treasury Analyst
  - Period Close: Controller, Consolidations Accountant, External Audit Liaison, Tax Provision Analyst
  - Case Lifecycle: Case Manager, Subject Matter Expert, Compliance Officer, Escalation Coordinator
  - Other: derive titles from process functions; generic titles are always a fail
```

> **GATE 0**: Do not open Step 1 until the Lifecycle Context Declaration is complete.

---

**FIELD CONTENT RULES**

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude, and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), directional magnitude, and breach classification | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names root-cause type + named element | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names S-ID or Ph-ID + consequence type | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Names rule / handoff precondition / system dependency | "Best practice" is a fail |
| Risk if Absent | Step 10 | Names SLA breach exposure / compliance failure / state inconsistency | "May cause issues" is a fail |
| Net Change | Step 13 | Eliminated / shifted (location named) / residual / Single-state | "Improved" is a fail |

---

**STEP 1 -- PHASE MAP WITH SLA ENVELOPE**

Name every lifecycle phase. Include a preliminary phase owner designation consistent with the declared lifecycle class.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk? (Y/N) | Preliminary Phase Owner (consistent with declared lifecycle class) |
|-------|------------|---------------|---------------------|--------------|----------------|-------------------------------------------------------------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| ... | | | | | | |

**SLA Risk Declaration** (complete for all At-Risk = Y phases before proceeding):

| Ph-ID | SLA Envelope | Anticipated Bottleneck | Risk Classification |
|-------|-------------|------------------------|---------------------|
| | | | |

> **GATE A**: Do not open the Role Registry until the Phase Map is complete with named entry triggers, completion conditions, preliminary phase owners, and SLA Risk Declaration rows for all At-Risk = Y phases.

---

**STEP 2 -- DOMAIN ROLE REGISTRY**

Name every domain role. Roles must be: (a) consistent with the declared lifecycle class, and (b) traceable to a phase in Step 1 via the Phase Authority column. Phase owner titles from Step 1 must resolve here.

| R-ID | Role Name (domain-qualified; consistent with lifecycle class; no generic labels) | Domain | Phase Authority (Ph-IDs) | Decisions Owned | Exception Handler (Y/N) |
|------|----------------------------------------------------------------------------------|--------|--------------------------|-----------------|------------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| ... | | | | | |

Validation: Every preliminary phase owner from Step 1 must appear as a Role Name or be reconciled to an R-ID here. Generic labels are a fail regardless of lifecycle class. At least one role must carry Exception Handler = Y.

> **GATE B**: Do not open the State Trace until the Role Registry is complete, all Phase-1 owners are reconciled to R-IDs, and at least one role carries Exception Handler = Y.

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3:

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths:**

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

SLA envelopes from Step 1 are carried forward here.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [from Step 1]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:** SLA Impact names Ph-ID + magnitude + breach flag. "May cause delays" is a fail.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

At least 2 edge cases distinct from Step 5 exceptions.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

At-Risk phases from Step 1 anchor Table 8a.

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined; breach-link cannot be satisfied by design | No contractual, operational, or regulatory SLA targets. Include reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [reason]
```

**Table 8a -- SLA Annotations:**

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; At-Risk = Y rows must align with Step 1 SLA Risk Declaration.

**Table 8b -- Breach Verdicts:**

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y) |
|-------|--------------|---------------|--------------|--------------|
| BV-01 | | | | |
| BV-02 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. Anticipated bottlenecks from Step 1 SLA Risk Declaration should appear.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Author Action | Verdict |
|------|-----------------------|---------------|---------|
| **FM-A** (fail) | Yes | General language instead of typed ID | **Fail** |
| **FM-B** (fail) | No | Blank instead of `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID + description | **Full credit** |
| **PM-2** (pass) | No | `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Phase Map > SLA Risk Declaration > Role Registry > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Lifecycle Context (pre-Step 1) | Lifecycle class declared; role vocabulary identified | Unanchored roles | Role titles in the artifact are not traceable to any named process domain |  |
| SC-02 | Phase Map (Step 1) | All phases have entry triggers, completion conditions, and At-Risk = Y rows declared | Unresolvable phase boundary | Phase transitions in the artifact cannot be verified as correctly ordered |  |
| SC-03 | Role Registry (Step 2) | All roles consistent with lifecycle class; all Phase-1 owners reconciled to R-IDs; no generic labels | Generic role or unresolved phase owner | Decision gates in the artifact cite unresolvable owners |  |
| SC-04 | Exception Catalog (Step 5) | All Handler (R-ID) cells trace to a role carrying Exception Handler = Y in the Role Registry | Uncertified exception handler | At least one exception path in the artifact has no accountable owner |  |
| SC-05 | Terminal Declaration (Step 6) | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated path | At least one path in the artifact reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-06 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID or `SLA-ABSENT` | Breach analysis disconnected from SLA evidence | Bottleneck severity in the artifact cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unanchored role, an unresolvable phase boundary, a generic role, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step.

---

## V-05 -- Combined: Output Format + Inertia Framing

**Variation axes:** V-05 combines the maximum schema density of V-02 (all constraint language in column headers) with per-section `AS-IS ANCHOR` blocks that name what a weak response looks like at each section before the schema table opens. Each section presents: (1) the AS-IS ANCHOR showing a concrete failing example for the most common miss at that section, (2) the structural table with inline column-header enforcement. The scan table column headers themselves carry fail-language. The AS-IS anchors do not appear in a preamble block -- they appear immediately before each section's table, making the failure mode concrete at point of use. The FIELD CONTENT RULES preamble block is eliminated; all dimensional constraints appear in column headers. The scan table and Handler header are unchanged from baseline.

**Hypothesis:** Schema-inline enforcement (V-02 axis) tells the author what a correct entry requires; inertia framing (AS-IS ANCHOR) shows the author what a weak entry looks like at the exact column where it would be written. The two mechanisms are complementary: the column header narrows the positive space, and the AS-IS anchor closes the most common failure mode at point of use. Authors who have internalized a schema through repetition tend to default to familiar weak patterns unless those patterns are named and blocked at the moment of cell entry. The prediction is that V-05 produces the lowest overall defect rate across all criteria categories because it combines positive constraint (column headers) with negative example (AS-IS anchors) at every structural section.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Each step opens with an **AS-IS ANCHOR** naming what a weak response at that section looks like, followed by the structural table with all constraints embedded in column headers. Read the AS-IS ANCHOR before filling any row -- it names the failure mode you must avoid.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **AS-IS ANCHOR**: A weak Step 1 response looks like this: R-01 = "Approver," R-02 = "Finance Manager," R-03 = "User." These titles are generic -- they name org-chart levels, not process functions. They do not qualify. A passing response names the process function the lifecycle actually uses: "Accounts Payable Supervisor," "Deal Desk Manager," "Tax Provision Analyst." The test: could this title appear in a job posting for a role in a completely different business process? If yes, it does not qualify.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

| R-ID | Role Name -- domain-qualified functional title; generic labels (Approver, Manager, User, Admin) are a fail | Domain -- process area, not org chart | Phase Authority (Ph-IDs from Step 2 -- fill after Step 2 is complete) | Decisions Owned (D-IDs from Step 3 -- forward-reference placeholder; complete after Step 3) | Exception Handler (Y/N) -- at least one Y required; N roles may not appear in any Handler cell |
|------|-------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| ... | | | | | |

---

**STEP 2 -- PHASE MAP**

> **AS-IS ANCHOR**: A weak Step 2 response looks like this: Entry Trigger = "Process starts," Completion Condition = "Phase is done," SLA Envelope = "ASAP." None of these qualify. A passing response names the event that triggers phase entry (e.g., "Signed purchase requisition received in ERP"), the verifiable output that closes the phase (e.g., "PO issued and vendor confirmed in system"), and a specific duration (e.g., "2 business days"). The test: could an auditor verify that this phase opened and closed on the right dates using only this entry and a system log? If not, it does not qualify.

> **GATE B**: Do not open the State Trace until every phase has a named entry trigger and completion condition.

| Ph-ID | Phase Name | Entry Trigger -- names the event or state; "process starts" does not count | Completion Condition -- names the verifiable output; "phase is done" does not count | SLA Envelope -- specific duration; "ASAP" or "timely" does not count | At-Risk? (Y/N) | At-Risk Bottleneck -- if Y: names the anticipated bottleneck; blank is a fail |
|-------|------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| ... | | | | | | |

---

**STEP 3 -- STATE TRACE**

> **AS-IS ANCHOR**: A weak Step 3 response looks like this: Entry Condition = "After step 2," Exit Transitions = "Goes to approval." These do not qualify. A passing entry condition names the specific event or predecessor state that activates this state (e.g., "Three-way match confirmed by AP system"). A passing exit transition names labeled branches (e.g., "APPROVED → S-05, REJECTED → E-02, ESCALATED → D-03"). The test: given only the entry condition and exit transitions in this table, can a process auditor reconstruct the full state diagram? If no, the entry or transition is incomplete.

> **GATE C**: Do not open the Exception Catalog until the State Trace and Decision Points are complete and all D-IDs have owners traceable to the Role Registry.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- names the trigger or predecessor; "after previous step" does not count | Exit Transitions -- labeled branches with target S-ID, E-ID, D-ID, or T-ID; "goes forward" does not count | Owner (R-ID) -- must appear in Role Registry; blank is a fail |
|------|--------------|------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3:

> **AS-IS ANCHOR for Decision Points**: A weak decision point looks like this: Condition = "Order is large," Owner = "Management," Fallback = "Escalate." None qualify. A passing condition names a measurable threshold (e.g., "Order value > $25,000"). A passing owner is an R-ID. A passing fallback names the holding state when the decision mechanism fails (e.g., "placed in S-HOLD until substitute approver designated by R-04").

| D-ID | Decision Name | Condition -- measurable threshold required; "large amount" does not count | Owner (R-ID) -- must appear in Role Registry; "Management" does not count | Branch A -- named outcome with target state | Branch B -- named outcome; "otherwise" does not count | Fallback -- mechanism impairment path; "escalate" alone does not count |
|------|--------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths:**

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

> **AS-IS ANCHOR**: A weak phase exit gate looks like this: Blocked by = "If things go wrong." This does not qualify. A passing entry names the specific role, system, or condition most likely to prevent phase exit (e.g., "R-03 Tax Provision Analyst unavailable during fiscal close window").

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition -- "if things go wrong" does not count]
```

---

**STEP 5 -- EXCEPTION CATALOG**

> **AS-IS ANCHOR**: A weak exception catalog looks like this: Handler = "Finance team," SLA Impact = "May cause delays," Terminal or Recovery = "Resolved." None qualify. A passing Handler is an R-ID with Exception Handler = Y. A passing SLA Impact names a phase (Ph-ID), a magnitude, and a breach flag. A passing Terminal or Recovery names a T-ID or a specific recovery state.

> **GATE D**: Do not open the Terminal Declaration until every Handler cell carries an R-ID with Exception Handler = Y in the Role Registry.

At least 3 exceptions.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition; "error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail | Deviation from Happy Path -- names specific states bypassed or added; "different path" does not count | SLA Impact -- names Ph-ID + magnitude + breach flag; "may cause delays" is a fail | Terminal or Recovery -- T-ID or named state; "resolved" does not count |
|------|--------------|----------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**STEP 6 -- TERMINAL DECLARATION**

> **AS-IS ANCHOR**: A weak terminal declaration looks like this: a single row with T-01 = "Completed" covering all paths. This does not qualify if failure paths are present. A passing declaration names each terminal type separately (success, failure, cancel), and the Reached From column lists every S-ID and E-ID that arrives there.

| T-ID | Terminal Name | Type -- success / failure / cancel; "completed" alone does not qualify as a type label | Reached From -- list all S-IDs and E-IDs; blank is a fail |
|------|--------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

> **AS-IS ANCHOR**: A weak edge case looks like this: Edge Case = "System outage," Why Unhandled = "Not considered," SLA Risk = "Could be a problem." None qualify. A passing edge case names a concrete scenario that the lifecycle's current design has no path for (distinct from named exceptions). SLA Risk names a specific phase threshold at risk (Ph-ID) with directional magnitude.

At least 2 edge cases.

| EC-ID | Edge Case -- concrete scenario the lifecycle has no path for; category names ("system issues") do not count | Phase (Ph-ID) | Why Unhandled -- names the design decision or omission; "not considered" does not count | SLA Risk -- names Ph-ID + directional magnitude + breach classification; "could be a problem" is a fail | Correct Handling -- names the control or path |
|-------|--------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

> **AS-IS ANCHOR**: A weak SLA annotation looks like this: SLA Status Declaration left blank, or Tables 8a/8b skipped with no SLA-ABSENT declaration. This triggers FM-B in Step 9. A passing response either completes Tables 8a and 8b with typed IDs, or declares `SLA-ABSENT: [reason]` and carries the token forward to every Breach Link cell in Step 9.

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined; breach-link cannot be satisfied by design | No contractual, operational, or regulatory SLA targets. Include reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [reason]
```

**Table 8a -- SLA Annotations:**

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration -- specific; "timely" does not count | At-Risk? (Y/N) | Risk Cause -- names the bottleneck; "volume" alone does not count |
|--------|--------------|-----------|------------------------------------------------------|----------------|-------------------------------------------------------------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

**Table 8b -- Breach Verdicts:**

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause -- if Y: names bottleneck or E-ID; "delays" alone is a fail |
|-------|--------------|---------------|--------------|-------------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

> **AS-IS ANCHOR**: A weak bottleneck register looks like this: Cause = "Too many approvals," Downstream Impact = "Delays the process," Breach Link = "See SLA section." None qualify. A passing Cause names the root-cause type (manual gate, role dependency, external system, data dependency) and the specific named element. A passing Downstream Impact names the specific S-IDs or Ph-IDs affected and the consequence type (delayed / blocked / skipped). A passing Breach Link cites a typed ID (BV-ID, SLA-ID, or Ph-ID) or the `SLA-ABSENT` token.

At least 2 bottlenecks.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Author Action | Verdict |
|------|-----------------------|---------------|---------|
| **FM-A** (fail) | Yes | General language instead of typed ID | **Fail** |
| **FM-B** (fail) | No | Blank instead of `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID + description | **Full credit** |
| **PM-2** (pass) | No | `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause -- root-cause type (manual gate / role dependency / external system / data dependency) + named element; "approval takes too long" is a fail | Downstream Impact -- S-ID or Ph-ID + consequence type (delayed / blocked / skipped); "delays the process" is a fail | Breach Link -- typed ID or SLA-ABSENT; general language is FM-A fail |
|------|--------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

> **AS-IS ANCHOR**: A weak gap register looks like this: Why Required = "Best practice," Risk if Absent = "May cause issues." Neither qualifies. A passing Why Required names a regulatory rule, a handoff precondition (the downstream state that requires this step's output), or a system dependency (the system that fails without this step). A passing Risk if Absent names a specific SLA breach exposure, compliance failure, or state inconsistency.

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step -- names the specific control or check; "better validation" does not count | Why Required -- regulatory rule / handoff precondition / system dependency; "best practice" is a fail | Risk if Absent -- SLA breach exposure / compliance failure / state inconsistency; "may cause issues" is a fail |
|------|--------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process -- specific lifecycle name, not a category | Fields Passed -- list specific data objects | Acceptance Condition -- names what the recipient verifies |
|-----------------|--------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

> **AS-IS ANCHOR**: A weak audit looks like this: all rows left blank, or a single statement "all phases covered." Silence is not coverage. A passing audit confirms each phase explicitly, names the handler R-ID for covered phases, and names the specific risk consequence for any uncovered phase.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID -- must appear in Step 5 and carry Exception Handler = Y in Step 1; blank is a fail if Y | Risk if Uncovered -- specific consequence; "may have issues" does not count |
|-------|------------|----------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

> **AS-IS ANCHOR**: A weak trajectory looks like this: Net Change = "Improved." This does not qualify. A passing Net Change classifies as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change -- eliminated / shifted (location named) / residual / Single-state; "improved" is a fail |
|------|-------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Role Registry (Step 1) | All roles are domain-qualified functional titles; no generic labels; AS-IS ANCHOR pattern absent | Generic role (e.g., "Approver") present | Decision gates in the artifact cite unresolvable owners |  |
| SC-02 | Exception Catalog (Step 5) | All Handler (R-ID) cells trace to a role carrying Exception Handler = Y in the Role Registry | Uncertified exception handler | At least one exception path in the artifact has no accountable owner |  |
| SC-03 | Terminal Declaration (Step 6) | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated path | At least one path in the artifact reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-04 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID (PM-1) or the `SLA-ABSENT` token (PM-2); no FM-A or FM-B | Breach analysis disconnected from SLA evidence | Bottleneck severity in the artifact cannot be verified against phase-level SLA thresholds |  |
| SC-05 | Gap Register (Step 10) | Every Why Required cites a rule, dependency, or regulation -- not best practice; AS-IS ANCHOR pattern absent | Unverifiable gap requirement | Gap requirement in the artifact cannot be audited against a named dependency |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (a generic role, an uncertified exception handler, an unterminated path, a breach analysis disconnected from SLA evidence, or an unverifiable gap requirement) -- and that artifact must be discarded and rebuilt from the failing step.
