---
skill: flow-lifecycle
round: 9
rubric-version: 9
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v9-2026-03-15.md
---

# flow-lifecycle -- Round 9 / Rubric v9 Variations

Round 9 under the v9 rubric extends the R8 baseline (which fixed C-27 and C-28 as invariants) with two new aspirational criteria extracted from the R8 excellence ceiling:

- **C-29 -- Decision Condition Threshold-Type Taxonomy**: The Decision Condition column header operationalizes the "measurable threshold" requirement inline — either by enumerating ≥2 specific threshold-type categories by name (e.g., "dollar amount, day count, retry count") or by providing a quoted passing example with a comparison operator and unit (e.g., "Order value > $25,000"). A column header that says only "(measurable threshold)" without enumeration or example does not pass, even if individual cells contain quantified values.
- **C-30 -- Exception-Catalog Boundary Gate**: A sequential gate explicitly guards ≥1 transition adjacent to the exception catalog — either the upstream boundary (state trace + decision table → exception catalog authorship begins) or the downstream boundary (exception catalog → terminal declaration authorship begins). C-20 already requires ≥3 distributed gates covering role registry, phase table, and artifact production; C-30 additionally requires at least one gate at an exception-catalog boundary.

**Invariants across all five variations**: All variations carry C-27 (scan table with named Defect Type column + gate sentence referencing it by name) and C-28 (Handler column header co-locates the backward-trace authority rule and inline fail-language). These are not variation axes — they are the baseline the variation axes layer on top of.

**R8 V-05 baseline under v9**: The prior R8 V-05 already satisfies C-27 and C-28. It is used as the structural foundation from which these five variations depart.

**Variation axes used**:
- Single-axis: V-01 (Output Format — threshold-type taxonomy via enumeration; upstream C-30 gate), V-02 (Phrasing Register — threshold-type taxonomy via passing example; downstream C-30 gate), V-03 (Lifecycle Emphasis — phase-first framing; both C-29 mechanisms; both C-30 boundary gates)
- Combined: V-04 (Role Sequence + Inertia Framing — lifecycle-class derivation + AS-IS baseline; C-29 via enumeration; upstream C-30), V-05 (Output Format + Lifecycle Emphasis + Phrasing Register — maximum schema density + phase-first + imperative register; both C-29 mechanisms; both C-30 boundary gates)

---

## V-01 -- Output Format: Threshold-Type Enumeration in Column Header; Upstream Exception-Catalog Gate

**Variation axis:** Output Format. Every constraint that governs a column is embedded inline in that column's header cell. The Field Content Rules preamble block of prior rounds is eliminated; all enforcement lives in column headers using "does not count," "is a fail," or "Mandatory" language. The Decision Condition column header enumerates the threshold-type taxonomy: `measurable threshold (dollar amount, day count, retry count, percentage threshold); qualitative condition alone does not count` — satisfying C-29 via the enumeration mechanism. GATE C guards the upstream exception-catalog boundary: the state trace and decision table must be complete before the exception catalog is opened — satisfying C-30 via the upstream boundary. GATE C text names the sections it locks and unlocks.

**Hypothesis:** When C-29 is satisfied by column-header enumeration, an author filling any Decision Condition cell sees the threshold-type categories at the exact moment they are entering a value. The enumeration acts as a vocabulary picker that prompts the author to name a specific numeric value in one of the named categories before moving to the next cell. Placing this at the column header (rather than in a preamble block) eliminates the bypass path where an author reads the preamble once and forgets it. The upstream C-30 gate is higher-leverage than the downstream boundary: an exception catalog authored before states are finalized will reference state names that may change, producing untraceable exception traces. Gate placement at the upstream boundary prevents this class of structural error.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. All field-level rules are embedded in column headers at the column they govern — read each header before filling rows. Steps that own gate declarations include the full gate text inline.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Map until the Role Registry is complete, all role names are domain-qualified functional titles, and at least one role carries Exception Handler = Y.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process area, not org unit | Decisions Owned -- cite D-IDs from Step 3; blank is a fail if this role owns any decision gate | Exception Handler (Y/N) -- at least one Y required; roles carrying N may not appear in any Handler cell in any downstream step |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |
| ... | | | | |

---

**STEP 2 -- PHASE MAP**

> **GATE B**: Do not open the State Trace until every phase has a named entry trigger, completion condition, and SLA envelope.

| Ph-ID | Phase Name | Entry Trigger -- names the event or condition that opens this phase; "process begins" does not count | Completion Condition -- names the verifiable output or state that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "3 business days", "8 business hours"); "as soon as possible" does not count | At-Risk Threshold -- the breach condition and causal bottleneck; blank is a fail if SLA evidence applies |
|-------|------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| ... | | | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Phases must aggregate ≥2 states each; a phase with exactly 1 state is a structural mismatch.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- names the specific event or predecessor state that causes entry; "after previous step" does not count | Exit Transitions -- labeled outbound paths naming the trigger and destination; "then continue" does not count | Owner (R-ID) -- must appear in Role Registry; blank is a fail |
|------|--------------|------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| S-03 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3:

| D-ID | Decision Name | Condition -- measurable threshold (dollar amount, day count, retry count, percentage threshold); qualitative condition alone does not count | Owner (R-ID) -- must appear in Role Registry; blank is a fail | Branch A -- named outcome when condition is met | Branch B -- named outcome when condition is not met; "otherwise" does not count | Fallback -- mechanism-impairment path (role unavailable, system down, config missing); names the holding state or escalation target; "escalate" alone does not count |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- at least one fork-join or declare absence with rationale:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C**: Do not open the Exception Catalog until the State Trace (all S-IDs with stable names) and Decision Table (all D-IDs) are complete. Exception flows reference state names by ID; authoring exceptions before states are finalized produces untraceable ID references. This gate locks Step 3 and unlocks Step 5.

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and consumed by the Scan Summary.

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

GATE C (Step 3) must be CLOSED before this step is opened. At least 3 exceptions.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition that diverts from the happy path; "an error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a structural fail | Deviation from Happy Path -- names the specific states bypassed or added; "different path" does not count | SLA Impact -- names Ph-ID + magnitude + breach flag (e.g., "adds 3+ days to PH-02; triggers breach threshold"); "may cause delays" is a fail | Terminal or Recovery -- T-ID or named recovery state; "resolved" does not count |
|------|--------------|----------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

> **GATE D**: Do not open the Terminal Declaration until all Exception Catalog Handler cells carry a certified R-ID (Exception Handler = Y in Step 1). This gate locks Step 5 and unlocks Step 6.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened. Every S-ID and E-ID must reach a T-ID declared here.

| T-ID | Terminal Name | Type (success / failure / cancel) -- one of these three labels; "completed" does not count | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Scenarios the lifecycle has no path for -- distinct from Step 5 exceptions. At least 2 required.

| EC-ID | Edge Case -- names a concrete scenario, not a category name | Phase (Ph-ID) | Why Unhandled -- names the specific design decision or omission; "not considered" does not count | SLA Risk -- names Ph-ID + directional magnitude + breach classification; "may affect timing" is a fail | Correct Handling -- names the control or path that would address this gap |
|-------|-------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined; breach-link in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Include a reason. |

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
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | General language instead of typed ID | **Fail** |
| **FM-B** (fail) | No -- SLA-ABSENT declared | Blank instead of `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID: BV-ID, SLA-ID, or Ph-ID + brief description | **Full credit** |
| **PM-2** (pass) | No | `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause -- root-cause type + named element (manual gate / role dependency / external system / data dependency); "approval takes too long" is a fail | Downstream Impact -- names S-IDs or Ph-IDs + consequence type (delayed / blocked / skipped); "delays the process" is a fail | Breach Link -- typed ID or SLA-ABSENT; general language is a fail |
|------|--------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step -- names the specific control or check omitted | Why Required -- regulatory rule (cite it) / handoff precondition (name the downstream state) / system dependency (name the system); "best practice" is a fail | Risk if Absent -- SLA breach exposure (name the phase) / compliance failure (name the regulation) / state inconsistency (name the erroneous record); "may cause issues" is a fail |
|------|--------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process -- names the specific lifecycle, not a category | Fields Passed -- lists specific data objects | Acceptance Condition -- names what the recipient verifies before accepting |
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

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change -- eliminated (state why) / shifted (name location by S-ID or Ph-ID) / residual (state why it persists) / Single-state; "improved" is a fail |
|------|-------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Role Registry (Step 1) | All roles are domain-qualified functional titles; no generic labels | Generic role | Decision gates in the artifact cite unresolvable owners |  |
| SC-02 | Decision Table (Step 3) | All Decision Condition cells name a specific measurable threshold value (dollar amount, day count, retry count, or percentage threshold) | Unquantified decision condition | Decision gates in the artifact cannot be operationally tested without further interpretation |  |
| SC-03 | Exception Catalog (Step 5) | GATE C was CLOSED before Step 5 was opened; all Handler R-IDs trace to Exception Handler = Y in Step 1 | Uncertified exception handler | At least one exception path in the artifact has no accountable owner |  |
| SC-04 | Terminal Declaration (Step 6) | GATE D was CLOSED before Step 6 was opened; every S-ID and E-ID ends at a named T-ID | Unterminated path | At least one path in the artifact reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-05 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID or the `SLA-ABSENT` token | Breach analysis disconnected from SLA evidence | Bottleneck severity cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (a generic role, an unquantified decision condition, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step before it is filed or used.

---

## V-02 -- Phrasing Register: Threshold-Type Taxonomy via Passing Example; Downstream Exception-Catalog Gate

**Variation axis:** Phrasing Register. All instructions use imperative verbs ("Write", "Name", "State", "List", "Confirm") rather than modal obligation ("must", "is required to"). The phrasing shifts responsibility from compliance to authorial action. The Decision Condition column header satisfies C-29 via the passing-example mechanism rather than enumeration: `measurable threshold -- a passing condition names a specific value with a comparison operator and unit (e.g., "Order value > $25,000"); a condition stated only as "approved if appropriate" does not pass`. The exception-catalog boundary gate (C-30) guards the downstream boundary: the exception catalog must be complete before terminal declarations are authored. GATE C in this variation locks Step 5 and unlocks Step 6 rather than locking Step 3 as in V-01.

**Hypothesis:** Imperative phrasing activates a production mode rather than a compliance-check mode. "Write the holding state or escalation path when the decision owner is unavailable" is a production instruction; "the fallback must name a holding state" is a compliance check. Authors following production instructions tend to fill cells with content directly rather than checking cell content against a rule. The prediction is that imperative-register prompts reduce "technically compliant but empty" outputs — cells that name a category but not an actual value. The downstream C-30 gate (exception catalog → terminal declarations) prevents the most consequential terminal-declaration error: terminal states whose "Reached From" fields list exception flow IDs that have not yet been finalized. An E-ID that changes after terminal declarations are written produces a terminal declaration that is unreachable by verification scan — the downstream gate prevents this forward-reference error class.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Follow every step in sequence. Write each section before opening the next. Read every column header before filling rows — column headers carry field rules inline.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Write the complete Role Registry before opening the Phase Map. Confirm at least one role carries Exception Handler = Y before proceeding.

For each role this lifecycle requires, write one row. Name a domain-specific functional title: "Senior Credit Analyst", "Procurement Manager", "Tax Provision Accountant". Do not write "Approver", "Reviewer", "Admin", or "Finance team" — these are generic labels that produce unresolvable decision owners in the artifact.

| R-ID | Role Name -- write a domain-qualified functional title; generic label ("Approver", "Admin", "User") is a fail | Domain -- write the process area (not the org unit) | Decisions Owned -- write the D-IDs this role owns; leave blank only if this role owns no decision gate | Exception Handler (Y/N) -- write Y for roles who hold exception resolution authority; write N for all others; at least one Y required |
|------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |
| ... | | | | |

---

**STEP 2 -- PHASE MAP**

> **GATE B**: Write the complete Phase Map before opening the State Trace. Name the entry trigger and completion condition for every phase before proceeding.

Name each phase. For each, write the event that opens it, the output that closes it, the SLA envelope, and the condition under which the SLA is at risk.

| Ph-ID | Phase Name | Entry Trigger -- write the event or predecessor state that opens this phase; write a specific trigger, not "process begins" | Completion Condition -- write the verifiable output or state that closes this phase; write a specific output, not "work is done" | SLA Envelope -- write a specific duration (e.g., "3 business days", "8 business hours"); do not write "as soon as possible" | At-Risk Threshold -- write the condition that triggers SLA breach; name a specific bottleneck; do not leave blank if SLA evidence applies |
|-------|------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| ... | | | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 named states. Write at least 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- write the specific event or predecessor state that causes entry; do not write "after previous step" | Exit Transitions -- write labeled outbound paths naming the trigger and destination; do not write "then continue" | Owner (R-ID) -- write the R-ID from Step 1 that owns this state; do not leave blank |
|------|--------------|------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| S-03 | | | | | |
| ... | | | | | |

**Decision Points** -- write at least 3:

| D-ID | Decision Name | Condition -- measurable threshold -- write a specific value with a comparison operator and unit (e.g., "Order value > $25,000"); a condition stated only as "approved if appropriate" does not pass | Owner (R-ID) -- write the R-ID from Step 1; do not leave blank | Branch A -- write the named outcome when the condition is met | Branch B -- write the named outcome when the condition is not met; do not write "otherwise" | Fallback -- write the holding state or escalation target when the owner is unavailable or the system is down; do not write only "escalate" |
|------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------||
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- write at least one fork-join; if none exists, write the rationale:

```
Fork (S-ID):    [write the branching state]
Branch A:       [write the concurrent path]
Branch B:       [write the concurrent path]
Join condition: [write what must hold before merge]
Merge owner:    [write the R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, write the exit gate. Name the SLA envelope for use in the Scan Summary.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [write what must be true for this phase to complete]
SLA envelope:   [write the target duration]
Success:        [write the Ph-ID or T-ID]
Failure:        [write the T-ID or exception name]
Blocked by:     [write the specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

Write at least 3 exception flows. For each, name the triggering condition, the divergence point, the handler, the deviation from the happy path, the SLA impact, and the terminal or recovery state.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- write the condition that diverts from the happy path; do not write "an error occurs" | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a structural fail | Deviation from Happy Path -- write the specific states bypassed or added; do not write "takes a different path" | SLA Impact -- write Ph-ID + magnitude + breach flag (e.g., "adds 3+ days to PH-02; triggers breach threshold"); do not write "may cause delays" | Terminal or Recovery -- write the T-ID or named recovery state; do not write "resolved" |
|------|--------------|----------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

> **GATE C**: Write the complete Exception Catalog before opening the Terminal Declaration. Confirm every Handler R-ID traces to Exception Handler = Y in Step 1 before proceeding. Terminal declarations list the paths that reach each terminal; those paths cannot be accurately listed until all exception flows are finalized. This gate locks Step 5 and unlocks Step 6.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE C must be CLOSED before this step is opened.

Write a row for each terminal state. List every S-ID and E-ID that reaches this terminal.

| T-ID | Terminal Name | Type -- write success, failure, or cancel; do not write "completed" | Reached From -- write all S-IDs and E-IDs that arrive here; do not leave blank |
|------|--------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

Write at least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Write at least 2 edge cases distinct from Step 5 exceptions.

| EC-ID | Edge Case -- write a concrete scenario, not a category name | Phase (Ph-ID) | Why Unhandled -- write the specific design decision or omission; do not write "not considered" | SLA Risk -- write Ph-ID + directional magnitude + breach classification; do not write "may affect timing" | Correct Handling -- write the control or path that would address this gap |
|-------|-------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined; breach-link in Step 9 cannot be satisfied by design | Use when no contractual, operational, or regulatory SLA targets apply. Write a reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [write reason]
```

**Table 8a -- SLA Annotations** (complete if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration -- write a specific duration; do not write "timely" | At-Risk? (Y/N) | Risk Cause -- write the bottleneck; do not write "volume" without naming the condition |
|--------|--------------|-----------|----------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

Write at least 3 rows; mark at least 1 At-Risk = Y.

**Table 8b -- Breach Verdicts** (complete if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold -- write the SLA-ID or state the threshold explicitly | Breach (Y/N) | Cause -- if Y: write the bottleneck condition or E-ID; do not write "delays" alone |
|-------|--------------|----------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

Write at least 1 breach = Y entry with a traceable cause.

---

**STEP 9 -- BOTTLENECK REGISTER**

Write at least 2 bottlenecks.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Write in Breach Link Cell | Verdict |
|------|-----------------------|---------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | General language instead of a typed ID | **Fail** |
| **FM-B** (fail) | No -- SLA-ABSENT declared | Blank instead of `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID: BV-ID, SLA-ID, or Ph-ID + brief description | **Full credit** |
| **PM-2** (pass) | No | `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause -- write the root-cause type and named element (manual gate / role dependency / external system / data dependency); do not write "approval takes too long" | Downstream Impact -- write the S-IDs or Ph-IDs affected and the consequence type (delayed / blocked / skipped); do not write "delays the process" | Breach Link -- write a typed ID or SLA-ABSENT; do not write general language |
|------|--------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Write at least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step -- write the specific control or check the lifecycle omits | Why Required -- write a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system); do not write "best practice" | Risk if Absent -- write the SLA breach exposure (name the phase), compliance failure (name the regulation), or state inconsistency (name the erroneous record); do not write "may cause issues" |
|------|--------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Write at least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process -- write the specific lifecycle name, not a category | Fields Passed -- write the specific data objects | Acceptance Condition -- write what the recipient verifies before accepting |
|-----------------|------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID -- write the R-ID from Step 5 that covers this phase; confirm Exception Handler = Y in Step 1; do not leave blank and call it covered | Risk if Uncovered -- write the specific consequence; do not write "may have issues" |
|-------|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

Write a full coverage declaration if all phases are covered: _______________________

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State -- write the current bottleneck condition | Target State -- write the intended future state (or "Single-state: [reason]") | Net Change -- write: eliminated (state why) / shifted (write new location by S-ID or Ph-ID) / residual (state why it persists) / Single-state; do not write "improved" |
|------|-------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Role Registry (Step 1) | All roles are domain-qualified functional titles; no generic labels | Generic role | Decision gates cite unresolvable owners |  |
| SC-02 | Decision Table (Step 3) | All Decision Condition cells name a specific value with a comparison operator and unit | Unquantified decision condition | Decision gates cannot be operationally tested without further interpretation |  |
| SC-03 | Exception Catalog (Step 5) | All Handler R-IDs trace to Exception Handler = Y in Step 1 | Uncertified exception handler | At least one exception path has no accountable owner |  |
| SC-04 | Terminal Declaration (Step 6) | GATE C was CLOSED before Step 6 was opened; every S-ID and E-ID ends at a named T-ID | Unterminated path | At least one path reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-05 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID or the `SLA-ABSENT` token | Breach analysis disconnected from SLA evidence | Bottleneck severity cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (a generic role, an unquantified decision condition, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step before it is filed or used.

---

## V-03 -- Lifecycle Emphasis: Phase-First Framing; Both C-29 Mechanisms; Both C-30 Boundary Gates

**Variation axis:** Lifecycle Emphasis. The Phase Map precedes the Role Registry. The schema opens by requiring phase boundaries and SLA envelopes before any roles are named. A pre-declared SLA Risk block between the Phase Map and Role Registry forces at-risk phase identification before any state is written. The Role Registry (Step 2) requires each role to declare its primary phase, creating a phase-ownership map before the state trace is opened.

The Decision Condition column header uses both C-29 mechanisms simultaneously: it enumerates threshold-type categories AND provides a quoted passing example, closing both the "what types qualify" and "what does a qualifying value look like" questions at point of use. Both C-30 boundary gates are present: GATE C guards the upstream boundary (state trace/decisions → exception catalog) and GATE D guards the downstream boundary (exception catalog → terminal declarations).

**Hypothesis:** Phase-first organization produces a fundamentally different artifact shape. When phases are established first, roles are discovered through phase responsibility rather than declared in the abstract — an author who writes "Phase 2: Credit Review, SLA 4 hours, AT-RISK: credit queue depth" has already implied a Credit Analyst role before Step 2 opens. This two-pass role derivation reduces generic placeholder risk because phase ownership requires a domain-specific title before any table is filled. The combined C-29 approach (enumeration + example in the same header) eliminates all threshold-type ambiguity simultaneously. The dual C-30 gate placement closes both structural failure modes: unstable-state-name references in exception flows (upstream gate) and forward-reference errors in terminal declarations where "Reached From" lists exception IDs that have not yet been finalized (downstream gate).

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

This schema is phase-first: phases and their SLA envelopes are established before roles, because role authority derives from phase responsibility. Work through every numbered step in sequence. Read every column header before filling rows.

---

**STEP 1 -- PHASE MAP WITH SLA ENVELOPES**

> **GATE A**: Do not open the SLA Risk Declaration or Role Registry until all phases have named entry triggers, completion conditions, SLA envelopes, and AT-RISK thresholds. Confirm ≥3 phases before proceeding.

Name every lifecycle phase. Commit to the entry trigger, completion condition, SLA envelope, at-risk threshold, and preliminary phase owner before any state or role is written. Phases must aggregate ≥2 states each in Step 3; a phase with exactly 1 state is a structural mismatch.

| Ph-ID | Phase Name | Entry Trigger -- names the event or condition that opens this phase; "process begins" does not count | Completion Condition -- names the verifiable output that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "4 business hours", "3 business days"); "ASAP" or "timely" does not count | At-Risk Threshold -- the breach condition and causal bottleneck; blank is a fail if SLA evidence applies | Preliminary Phase Owner -- names a domain-functional title that will operate this phase; will be formalized in Step 2 |
|-------|------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |
| ... | | | | | | |

**SLA Risk Declaration** -- before opening Step 2, list all AT-RISK phases with causal bottlenecks:

```
AT-RISK phases:
  PH-xx [Phase Name]: [causal bottleneck + magnitude]
  ... (list all phases flagged AT-RISK above)
```

> **GATE A CLOSE**: SLA Risk Declaration complete. At least 1 phase flagged AT-RISK with a named causal bottleneck. Proceed to Step 2.

---

**STEP 2 -- DOMAIN ROLE REGISTRY**

Name every role this lifecycle requires. Every role must trace to at least one phase in Step 1. At least one role must carry Exception Handler = Y.

> **GATE B**: Do not open the State Trace until the Role Registry is complete, all role names are domain-qualified functional titles consistent with the phases in Step 1, and at least one role carries Exception Handler = Y.

| R-ID | Role Name -- domain-qualified functional title derived from a phase in Step 1 (e.g., "Senior Credit Analyst" for a Credit Review phase); generic labels ("Approver", "Admin", "User") do not count | Primary Phase (Ph-ID) -- the phase this role primarily operates in | Decisions Owned -- cite D-IDs from Step 3; blank is a fail if role owns any decision | Exception Handler (Y/N) -- at least one Y required; roles carrying N may not appear in any Handler cell |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |
| ... | | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 named states organized within phases. Write at least 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- names the specific event or predecessor state; "after previous step" does not count | Exit Transitions -- labeled outbound paths naming trigger and destination; "then continue" does not count | Owner (R-ID) -- must appear in Step 2 registry; blank is a fail |
|------|--------------|------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| S-03 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3:

| D-ID | Decision Name | Condition -- measurable threshold: enumerate the type (dollar amount, day count, retry count, percentage threshold) and provide a specific value with comparison operator (e.g., "Invoice amount > $10,000; dollar-amount threshold"); qualitative condition alone does not count | Owner (R-ID) -- must appear in Step 2 registry; blank is a fail | Branch A | Branch B -- "otherwise" does not count | Fallback -- mechanism-impairment path; names holding state or escalation target; "escalate" alone does not count |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- at least one fork-join or explicit absence declaration:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C**: Do not open the Exception Catalog until the State Trace (all S-IDs with stable names) and Decision Table (all D-IDs) are complete. Exception flows reference state names by ID; authoring exception flows before states are finalized produces unstable ID references. This gate locks Step 3 and unlocks Step 5.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- must match Step 1 Phase Map]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED before this step is opened. At least 3 exceptions.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition that diverts from the happy path; "an error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a structural fail | Deviation from Happy Path -- names the specific states bypassed or added; "different path" does not count | SLA Impact -- names Ph-ID + magnitude + breach flag; "may cause delays" is a fail | Terminal or Recovery -- T-ID or named recovery state; "resolved" does not count |
|------|--------------|----------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

> **GATE D**: Do not open the Terminal Declaration until the Exception Catalog is complete with all Handler R-IDs certified. Terminal declarations enumerate paths that reach each terminal; those paths cannot be accurately listed until all exception flows are finalized with stable E-IDs. This gate locks Step 5 and unlocks Step 6.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened.

| T-ID | Terminal Name | Type (success / failure / cancel) -- one of these three labels; "completed" does not count | Reached From -- lists all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

At least 2 edge cases distinct from Step 5 exceptions.

| EC-ID | Edge Case -- names a concrete scenario, not a category | Phase (Ph-ID) | Why Unhandled | SLA Risk -- Ph-ID + magnitude + breach classification; "may affect timing" is a fail | Correct Handling |
|-------|-------------------------------------------------------|--------------|---------------|--------------------------------------------------------------------------------------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined; breach-link in Step 9 cannot be satisfied by design | Use when no contractual, operational, or regulatory SLA targets apply. Include a reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [reason]
```

**Table 8a -- SLA Annotations** (if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration -- specific; "timely" does not count | At-Risk? (Y/N) | Risk Cause -- references AT-RISK phases from Step 1 SLA Risk Declaration where applicable |
|--------|--------------|-----------|------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y referencing a phase flagged in the Step 1 SLA Risk Declaration.

**Table 8b -- Breach Verdicts** (if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause -- if Y: names the bottleneck condition or E-ID; "delays" alone is a fail |
|-------|--------------|---------------|--------------|---------------------------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y with traceable cause.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Author Action | Verdict |
|------|-----------------------|---------------|---------|
| **FM-A** (fail) | Yes | General language instead of typed ID | **Fail** |
| **FM-B** (fail) | No -- SLA-ABSENT | Blank instead of `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID: BV-ID, SLA-ID, or Ph-ID + description | **Full credit** |
| **PM-2** (pass) | No | `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause -- root-cause type + named element; "approval takes too long" is a fail | Downstream Impact -- names S-IDs or Ph-IDs + consequence type; "delays the process" is a fail | Breach Link -- typed ID or SLA-ABSENT; general language is a fail |
|------|--------------|-----------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

| G-ID | Phase (Ph-ID) | Missing Step | Why Required -- regulatory rule / handoff precondition / system dependency; "best practice" is a fail | Risk if Absent |
|------|--------------|-------------|------------------------------------------------------------------------------------------------------|----------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID -- must appear in Step 5 and carry Exception Handler = Y in Step 2; silence is not coverage | Risk if Uncovered |
|-------|------------|----------------------|----------------------------------------------------------------------------------------------------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

Full coverage declaration: _______________________

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change -- eliminated / shifted (name location) / residual / Single-state; "improved" is a fail |
|------|-------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Phase Map > Role Registry > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Phase Map (Step 1) | All phases have named entry triggers, completion conditions, and SLA envelopes; SLA Risk Declaration complete with ≥1 AT-RISK phase | Unenveloped phase | SLA annotation in the artifact lacks a phase anchor and cannot be verified |  |
| SC-02 | Role Registry (Step 2) | All roles are domain-qualified functional titles consistent with phases in Step 1; at least one Exception Handler = Y | Generic role | Decision gates cite unresolvable owners |  |
| SC-03 | Exception Catalog (Step 5) | GATE C was CLOSED before Step 5 was opened; all Handler R-IDs trace to Exception Handler = Y in Step 2 | Uncertified exception handler | At least one exception path has no accountable owner |  |
| SC-04 | Terminal Declaration (Step 6) | GATE D was CLOSED before Step 6 was opened; every S-ID and E-ID ends at a named T-ID | Unterminated path | At least one path reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-05 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID or the `SLA-ABSENT` token | Breach analysis disconnected from SLA evidence | Bottleneck severity cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unenveloped phase, a generic role, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step before it is filed or used.

---

## V-04 -- Role Sequence + Inertia Framing: Lifecycle-Class Derivation + AS-IS Baseline; Threshold-Type Enumeration; Upstream Exception-Catalog Gate

**Variation axis:** Role Sequence + Inertia Framing. The prompt opens with a LIFECYCLE CONTEXT DECLARATION that names the lifecycle class (L2O, P2P, Period Close, Case Lifecycle) and provides domain-typical role vocabulary for that class. This is combined with an AS-IS PROCESS SCAN that precedes the Role Registry: the author must identify the current-state process and name its failure modes before building the to-be lifecycle. The AS-IS scan makes the inertia competitor explicit — what the lifecycle is replacing or formalizing — and forces identification of real bottlenecks and gaps before the state trace is opened.

The Decision Condition column header satisfies C-29 via enumeration anchored to the lifecycle class: the header names domain-relevant threshold types for the declared class (e.g., for P2P: "invoice amount, payment terms day count, approval tier count"). The exception-catalog boundary gate (C-30) is the upstream variant: the state trace and decision table must be stable before exception flows are authored.

**Hypothesis:** The AS-IS scan creates a forcing function for bottleneck and gap identification that post-hoc analysis misses. When authors trace the existing process first — including its known failure modes — the bottlenecks they identify are operationally grounded rather than theoretically derived. The lifecycle-class declaration narrows the threshold-type taxonomy to domain-relevant categories, reducing the abstraction gap: a P2P author filling a Decision Condition cell sees "invoice amount, payment terms day count, approval tier count" rather than a generic list, and can immediately identify which category applies to their specific decision point without needing to map generic terms to domain concepts. The upstream C-30 gate prevents the most structurally damaging error class (exception flow ID references that become invalid when states are finalized after exceptions are written).

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Read every column header before filling rows. The Lifecycle Context Declaration and AS-IS scan in Step 0 are preconditions for all subsequent steps.

---

**LIFECYCLE CONTEXT DECLARATION**

Before opening any table, complete this block:

```
Lifecycle type:    [ ] Lead-to-Order (L2O)
                   [ ] Procure-to-Pay (P2P)
                   [ ] Period Close
                   [ ] Case Lifecycle
                   [ ] Other: _______

Lifecycle class:   [one sentence naming the primary business outcome this lifecycle achieves]

Domain threshold-type vocabulary for this class (reference when completing Step 3 Decision Condition column):
  - L2O:          deal value, pipeline day count, approval tier count, discount percentage
  - P2P:          invoice amount, payment terms day count, approval tier count, receipt variance percentage
  - Period Close: journal entry amount, reconciliation day count, adjustment approval tier, variance threshold percentage
  - Case Lifecycle: case age in days, escalation tier count, resolution attempt count, penalty exposure amount
  - Other:        derive from process context; name ≥2 threshold types before opening Step 3
```

> **GATE 0**: Do not open Step 0 until the Lifecycle Context Declaration is complete with a lifecycle class selected and domain threshold-type vocabulary identified.

---

**STEP 0 -- AS-IS PROCESS SCAN**

Before building the to-be lifecycle, document the current-state process and identify its failure modes. The to-be lifecycle must address every failure mode named here.

```
Current-state process name or description:
  [one sentence naming how this process is currently executed]

Current-state failure modes (name at least 2 -- become candidate bottlenecks in Step 9):
  FM-1: [failure mode name + operational consequence]
  FM-2: [failure mode name + operational consequence]

Gaps in current-state process (name at least 1 -- become candidate gaps in Step 10):
  G-1: [missing step or control + consequence if absent]

Forcing condition (name the regulatory requirement, audit finding, volume trigger, or incident):
  [one sentence]
```

> **GATE 0 CLOSE**: AS-IS scan complete with ≥2 failure modes and ≥1 gap identified. Proceed to Step 1.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Name every role this lifecycle requires. Use functional titles consistent with the lifecycle class declared above.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete, all role names are domain-qualified titles consistent with the declared lifecycle class, and at least one role carries Exception Handler = Y.

| R-ID | Role Name -- domain-qualified functional title consistent with the declared lifecycle class; generic labels ("Approver", "Admin", "User") do not count | Domain -- process area | Decisions Owned -- cite D-IDs from Step 3; blank is a fail if role owns any decision | Exception Handler (Y/N) -- at least one Y required; roles carrying N may not be assigned as exception handlers in Step 5 |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |
| ... | | | | |

---

**STEP 2 -- PHASE MAP**

> **GATE B**: Do not open the State Trace until all phases have named entry triggers, completion conditions, and SLA envelopes.

| Ph-ID | Phase Name | Entry Trigger -- names the event or condition that opens this phase; "process begins" does not count | Completion Condition -- names the verifiable output that closes this phase; "work is done" does not count | SLA Envelope -- specific duration; "ASAP" does not count | At-Risk Threshold -- names the breach condition and causal bottleneck; blank is a fail if SLA evidence applies |
|-------|------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| ... | | | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 named states. Write at least 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- names the specific trigger or predecessor; "after previous step" does not count | Exit Transitions -- labeled outbound paths naming trigger and destination; "then continue" does not count | Owner (R-ID) -- must appear in Step 1 registry; blank is a fail |
|------|--------------|------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| S-03 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Reference the domain threshold-type vocabulary from the Lifecycle Context Declaration:

| D-ID | Decision Name | Condition -- measurable threshold using a domain threshold type for this lifecycle class (e.g., for P2P: "Invoice amount > $50,000; dollar-amount threshold"); qualitative condition alone does not count | Owner (R-ID) -- must appear in Step 1 registry; blank is a fail | Branch A | Branch B -- "otherwise" does not count | Fallback -- mechanism-impairment path; names holding state or escalation target; "escalate" alone does not count |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------|----------------------------------------|------------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |
| ... | | | | | | |

**Parallel Paths:**

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C**: Do not open the Exception Catalog until the State Trace (all S-IDs with stable names) and Decision Table (all D-IDs) are complete. Exception flows reference state names and decision IDs; authoring exceptions before these are finalized produces untraceable references. This gate locks Step 3 and unlocks Step 5.

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

GATE C must be CLOSED. At least 3 exceptions. Map each exception to a failure mode in Step 0 where applicable.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition that diverts from the happy path; "an error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a structural fail | AS-IS Failure Mode (FM-ID or "new") | Deviation from Happy Path | SLA Impact -- names Ph-ID + magnitude + breach flag; "may cause delays" is a fail | Terminal or Recovery |
|------|--------------|----------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|---------------------------|-----------------------------------------------------------------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

> **GATE D**: Do not open the Terminal Declaration until the Exception Catalog is complete with all Handler R-IDs certified. This gate locks Step 5 and unlocks Step 6.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Every S-ID and E-ID must reach a named T-ID.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From -- lists all S-IDs and E-IDs; blank is a structural fail |
|------|--------------|----------------------------------|-----------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

---

**STEP 7 -- EDGE CASE CATALOG**

At least 2 edge cases distinct from Step 5 exceptions.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk -- Ph-ID + magnitude + breach classification; "may affect timing" is a fail | Correct Handling |
|-------|-----------|--------------|---------------|--------------------------------------------------------------------------------------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined | No contractual, operational, or regulatory SLA targets; include reason |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

**Table 8a** (if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

**Table 8b** (if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause |
|-------|--------------|---------------|--------------|-------|
| BV-01 | | | | |
| BV-02 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. Prioritize failure modes from the Step 0 AS-IS scan. Note the AS-IS FM-ID for each bottleneck that corresponds to a Step 0 failure mode.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Author Action | Verdict |
|------|-----------------------|---------------|---------|
| **FM-A** | Yes | General language | Fail |
| **FM-B** | No / SLA-ABSENT | Blank | Fail |
| **PM-1** | Yes | Typed ID: BV-ID / SLA-ID / Ph-ID + description | Full credit |
| **PM-2** | No / SLA-ABSENT | `SLA-ABSENT` | Earned-absence credit |

| B-ID | Phase (Ph-ID) | Bottleneck Name | AS-IS FM-ID (or "new") | Cause -- root-cause type + named element; "approval takes too long" is a fail | Downstream Impact -- names S-IDs or Ph-IDs + consequence type; "delays the process" is a fail | Breach Link |
|------|--------------|-----------------|------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Prioritize gaps from the Step 0 AS-IS scan.

| G-ID | Phase (Ph-ID) | Missing Step | AS-IS Gap-ID (or "new") | Why Required -- regulatory rule / handoff precondition / system dependency; "best practice" is a fail | Risk if Absent |
|------|--------------|-------------|-------------------------|------------------------------------------------------------------------------------------------------|----------------|
| G-01 | | | | | |

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
|------|-------------|---------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Context + AS-IS Scan > Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | AS-IS Scan (Step 0) | ≥2 failure modes and ≥1 gap identified before any to-be section is opened | Unanchored lifecycle | Bottlenecks and gaps in the artifact are theoretically derived rather than operationally grounded |  |
| SC-02 | Role Registry (Step 1) | All roles domain-qualified and consistent with lifecycle class; ≥1 Exception Handler = Y | Generic role | Decision gates cite unresolvable owners |  |
| SC-03 | Exception Catalog (Step 5) | GATE C closed before Step 5 opened; all Handler R-IDs trace to Exception Handler = Y in Step 1 | Uncertified exception handler | At least one exception path has no accountable owner |  |
| SC-04 | Terminal Declaration (Step 6) | GATE D closed before Step 6 opened; every S-ID and E-ID ends at a named T-ID | Unterminated path | At least one path reaches no named conclusion |  |
| SC-05 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID or `SLA-ABSENT` | Breach analysis disconnected from SLA evidence | Bottleneck severity cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unanchored lifecycle, a generic role, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step before it is filed or used.

---

## V-05 -- All Axes: Phase-First + Lifecycle-Class Derivation + AS-IS Anchor + Maximum Schema Density + Both C-29 Mechanisms + Both C-30 Boundary Gates

**Variation axis:** All five axes combined:

1. **Lifecycle Emphasis (phase-first)**: Phase Map is Step 1; roles are derived from phases in Step 2.
2. **Role Sequence (lifecycle-class derivation)**: A LIFECYCLE CONTEXT DECLARATION establishes class and domain vocabulary before Step 1.
3. **Inertia Framing (AS-IS anchor)**: Step 0 names the current-state process and its failure modes before the to-be lifecycle is built.
4. **Output Format (maximum schema density)**: All constraint language is embedded inline in column headers; no standalone field-rule preamble blocks exist outside of gate sentences.
5. **Phrasing Register (imperative throughout)**: All instructions use imperative verbs ("Write", "Name", "List", "Confirm").

**C-29**: The Decision Condition column header uses both mechanisms — it enumerates threshold-type categories from the declared lifecycle class AND provides a quoted passing example: `measurable threshold: write the type and a specific value with comparison operator and unit (e.g., "Invoice amount > $50,000; dollar-amount threshold"); qualitative condition alone does not count`.

**C-30**: Both exception-catalog boundary gates are present. GATE C guards the upstream boundary (state trace/decisions → exception catalog). GATE D guards the downstream boundary (exception catalog → terminal declarations). Both gates name the sections they lock and unlock and include failure consequences.

**Hypothesis:** Each axis closes a distinct failure pathway: lifecycle-class derivation prevents generic role titles; phase-first framing prevents orphaned SLA annotations; AS-IS anchoring prevents theoretically-derived bottlenecks; schema density prevents bypass of preamble-block constraints; imperative register prevents passive-compliance outputs; dual C-29 mechanisms eliminate all threshold-type ambiguity simultaneously; dual C-30 gates prevent both unstable-state-reference errors in exception flows and forward-reference errors in terminal declarations. The prediction is that V-05 produces the highest composite rubric score by closing every identified failure pathway simultaneously. The cost is higher prompt complexity, which is acceptable for instructed authors who have seen prior lifecycle examples.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

This schema is phase-first and class-anchored: establish lifecycle class and phases before roles. All field rules are inline in column headers. Read every header before filling rows. Complete every step in sequence.

---

**LIFECYCLE CONTEXT DECLARATION**

Complete this block before opening any table or step:

```
Lifecycle type:    [ ] Lead-to-Order (L2O)
                   [ ] Procure-to-Pay (P2P)
                   [ ] Period Close
                   [ ] Case Lifecycle
                   [ ] Other: _______

Lifecycle class:   [one sentence naming the primary business outcome]

Domain threshold-type vocabulary (reference when completing Decision Condition column in Step 3):
  - L2O:          deal value, pipeline day count, approval tier count, discount percentage threshold
  - P2P:          invoice amount, payment terms day count, approval tier count, receipt variance percentage
  - Period Close: journal entry amount, reconciliation day count, adjustment approval tier, variance threshold percentage
  - Case Lifecycle: case age in days, escalation tier count, resolution attempt count, penalty exposure amount
  - Other:        name ≥2 threshold types before opening Step 3
```

> **GATE 0**: Complete the Lifecycle Context Declaration before opening Step 0.

---

**STEP 0 -- AS-IS PROCESS SCAN**

Write the current-state process and its failure modes before building the to-be lifecycle. The to-be lifecycle must address every failure mode named here.

```
Current-state process:
  [one sentence naming how this process is currently executed]

AS-IS failure modes (write at least 2 -- become candidate bottlenecks in Step 9):
  FM-1: [failure mode name + operational consequence]
  FM-2: [failure mode name + operational consequence]

AS-IS gaps (write at least 1 -- becomes candidate gap in Step 10):
  G-1: [missing step or control + consequence if absent]

Forcing condition (write the regulatory requirement, audit finding, volume trigger, or incident):
  [one sentence]
```

> **GATE 0 CLOSE**: AS-IS scan complete with ≥2 failure modes and ≥1 gap. Proceed to Step 1.

---

**STEP 1 -- PHASE MAP WITH SLA ENVELOPES**

> **GATE A**: Write the complete Phase Map with SLA envelopes and AT-RISK declarations before opening the SLA Risk Declaration or Step 2. Confirm ≥3 phases and ≥1 AT-RISK designation before proceeding.

Write each phase. Name its entry trigger, completion condition, SLA envelope, AT-RISK threshold, and preliminary phase owner. Phases must aggregate ≥2 states each in Step 3.

| Ph-ID | Phase Name | Entry Trigger -- write the specific event that opens this phase; do not write "process begins" | Completion Condition -- write the verifiable output that closes this phase; do not write "work is done" | SLA Envelope -- write a specific duration (e.g., "4 business hours", "3 business days"); do not write "ASAP" or "timely" | At-Risk Threshold -- write the breach condition and causal bottleneck; do not leave blank if SLA evidence applies | Preliminary Phase Owner -- write a domain-specific functional title; will be formalized in Step 2 |
|-------|------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |
| ... | | | | | | |

**SLA Risk Declaration** -- list all AT-RISK phases before opening Step 2:

```
AT-RISK phases:
  PH-xx [Phase Name]: [causal bottleneck + magnitude]
  ...
```

---

**STEP 2 -- DOMAIN ROLE REGISTRY**

> **GATE B**: Write the complete Role Registry before opening the State Trace. Confirm all roles are domain-qualified and trace to ≥1 phase in Step 1. Confirm ≥1 role carries Exception Handler = Y before proceeding.

Write one row per role. Every R-ID must trace to ≥1 phase in Step 1.

| R-ID | Role Name -- write a domain-qualified functional title consistent with the declared lifecycle class (e.g., "AP Supervisor" for P2P, "Senior Credit Analyst" for L2O); do not write "Approver", "Admin", "User", or any generic label -- generic label is a fail | Primary Phase (Ph-ID) -- write the Ph-ID this role primarily operates in | Decisions Owned -- write D-IDs from Step 3; do not leave blank if this role owns any decision gate | Exception Handler (Y/N) -- write Y for roles with exception resolution authority; write N for all others; ≥1 Y required; roles with N may not appear in any Handler cell in Step 5 |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |
| ... | | | | |

---

**STEP 3 -- STATE TRACE**

Write at least 6 named states. Organize within phases — write ≥2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- write the specific event or predecessor state; do not write "after previous step" | Exit Transitions -- write labeled outbound paths naming trigger and destination; do not write "then continue" | Owner (R-ID) -- write the R-ID from Step 2; do not leave blank |
|------|--------------|------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| S-01 | | | | | |
| S-02 | | | | | |
| S-03 | | | | | |
| ... | | | | | |

**Decision Points** -- write at least 3. Reference the domain threshold-type vocabulary from the Lifecycle Context Declaration:

| D-ID | Decision Name | Condition -- measurable threshold: write the type and a specific value with comparison operator and unit (e.g., "Invoice amount > $50,000; dollar-amount threshold"); qualitative condition alone does not count | Owner (R-ID) -- write the R-ID from Step 2; do not leave blank | Branch A -- write the named outcome when condition is met | Branch B -- write the named outcome when condition is not met; do not write "otherwise" | Fallback -- write the holding state or escalation target when the owner is unavailable or the system is down; do not write only "escalate" |
|------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- write ≥1 fork-join or declare absence with rationale:

```
Fork (S-ID):    [write the branching state]
Branch A:       [write the concurrent path]
Branch B:       [write the concurrent path]
Join condition: [write what must hold before merge]
Merge owner:    [write the R-ID]
```

> **GATE C**: Write the complete State Trace (all S-IDs with stable names) and Decision Table (all D-IDs) before opening the Exception Catalog. Exception flows reference state names and decision IDs; authoring exceptions before these are finalized produces untraceable ID references that cannot be verified in the final artifact. This gate locks Step 3 and unlocks Step 5.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [write what must be true for this phase to complete]
SLA envelope:   [write the target duration -- must match Step 1 Phase Map]
Success:        [write Ph-ID or T-ID]
Failure:        [write T-ID or exception name]
Blocked by:     [write the specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED before this step is opened.

Write at least 3 exception flows. Map each to an AS-IS failure mode from Step 0 where applicable.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- write the specific condition that diverts from the happy path; do not write "an error occurs" | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a structural fail | AS-IS FM-ID (or "new") | Deviation from Happy Path -- write the specific states bypassed or added; do not write "different path" | SLA Impact -- write Ph-ID + magnitude + breach flag (e.g., "adds 4+ days to PH-02; triggers breach threshold"); do not write "may cause delays" | Terminal or Recovery -- write T-ID or named recovery state; do not write "resolved" |
|------|--------------|----------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

> **GATE D**: Write the complete Exception Catalog with all Handler R-IDs certified before opening the Terminal Declaration. Terminal declarations list paths that reach each terminal — those paths cannot be accurately enumerated until all exception flows are finalized with stable E-IDs and terminal assignments. This gate locks Step 5 and unlocks Step 6.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened.

Write one row per terminal state. List every S-ID and E-ID that reaches each terminal.

| T-ID | Terminal Name | Type -- write success, failure, or cancel; do not write "completed" | Reached From -- write all S-IDs and E-IDs that arrive here; do not leave blank |
|------|--------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

Write ≥1 success terminal and ≥1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Write ≥2 edge cases distinct from Step 5 exceptions.

| EC-ID | Edge Case -- write a concrete scenario, not a category name | Phase (Ph-ID) | Why Unhandled -- write the specific design decision or omission; do not write "not considered" | SLA Risk -- write Ph-ID + directional magnitude + breach classification; do not write "may affect timing" | Correct Handling -- write the control or path that would address this gap |
|-------|-------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes defined; breach-link in Step 9 cannot be satisfied by design | Use when no contractual, operational, or regulatory SLA targets apply. Write a reason. |

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [write reason]
```

**Table 8a** (complete if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration -- write a specific duration; do not write "timely" | At-Risk? (Y/N) -- reference AT-RISK phases from Step 1 SLA Risk Declaration | Risk Cause -- reference Step 1 At-Risk Threshold or Step 9 B-ID where applicable |
|--------|--------------|-----------|----------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

Write ≥3 rows; mark ≥1 At-Risk = Y.

**Table 8b** (complete if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold -- write SLA-ID or state threshold explicitly | Breach (Y/N) | Cause -- if Y: write the bottleneck condition or E-ID; do not write "delays" alone |
|-------|--------------|-------------------------------------------------------------|--------------|------------------------------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

Write ≥1 breach = Y with a traceable cause.

---

**STEP 9 -- BOTTLENECK REGISTER**

Write ≥2 bottlenecks. Prioritize AS-IS failure modes from Step 0.

**Breach Link -- Outcome Conditions:**

| Mode | SLA Evidence Present? | Write in Breach Link Cell | Verdict |
|------|-----------------------|---------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | General language instead of typed ID | **Fail** |
| **FM-B** (fail) | No -- SLA-ABSENT declared | Blank instead of `SLA-ABSENT` | **Fail** |
| **PM-1** (pass) | Yes | Typed ID: BV-ID / SLA-ID / Ph-ID + brief description | **Full credit** |
| **PM-2** (pass) | No | `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | AS-IS FM-ID (or "new") | Cause -- write root-cause type + named element (manual gate / role dependency / external system / data dependency); do not write "approval takes too long" | Downstream Impact -- write S-IDs or Ph-IDs affected + consequence type (delayed / blocked / skipped); do not write "delays the process" | Breach Link -- write typed ID or SLA-ABSENT; do not write general language |
|------|--------------|-----------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**STEP 10 -- GAP REGISTER**

Write ≥1 gap. Prioritize AS-IS gaps from Step 0.

| G-ID | Phase (Ph-ID) | Missing Step -- write the specific control or check the lifecycle omits | AS-IS Gap-ID (or "new") | Why Required -- write a regulatory rule (cite it) / handoff precondition (name the downstream state) / system dependency (name the system); do not write "best practice" | Risk if Absent -- write the SLA breach exposure (name the phase) / compliance failure (name the regulation) / state inconsistency (name the erroneous record); do not write "may cause issues" |
|------|--------------|-------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G-01 | | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Write ≥1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process -- write the specific lifecycle name | Fields Passed -- write the specific data objects | Acceptance Condition -- write what the recipient verifies before accepting |
|-----------------|-------------------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 1, confirm whether an exception handler exists.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID -- write the R-ID from Step 5; confirm Exception Handler = Y in Step 2; do not leave blank and call it covered | Risk if Uncovered -- write the specific consequence; do not write "may have issues" |
|-------|------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

Write a full coverage declaration if all phases are covered: _______________________

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State -- write the current condition from Step 0 AS-IS scan | Target State -- write the intended future state (or "Single-state: [reason]") | Net Change -- write: eliminated (state why) / shifted (write new location by S-ID or Ph-ID) / residual (state why it persists) / Single-state; do not write "improved" |
|------|-------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Lifecycle Context + AS-IS Scan > Phase Map > Role Registry > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary -- complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status (OPEN/CLOSED) |
|-------|---------|------------------------|---------------------|----------------------|----------------------|
| SC-01 | Lifecycle Context + AS-IS (Step 0) | Lifecycle class declared; ≥2 AS-IS failure modes and ≥1 gap identified before any to-be section opened | Unanchored lifecycle | Bottlenecks in the artifact are theoretically derived; lifecycle class cannot be verified |  |
| SC-02 | Phase Map (Step 1) | ≥3 phases with named entry triggers, completion conditions, and SLA envelopes; ≥1 AT-RISK designation | Unenveloped phase | SLA annotation in the artifact lacks a phase anchor and cannot be verified against a threshold |  |
| SC-03 | Role Registry (Step 2) | All roles domain-qualified and consistent with lifecycle class; all trace to ≥1 phase in Step 1; ≥1 Exception Handler = Y | Generic role | Decision gates cite unresolvable owners |  |
| SC-04 | Exception Catalog (Step 5) | GATE C closed before Step 5 opened; all Handler R-IDs trace to Exception Handler = Y in Step 2 | Uncertified exception handler | At least one exception path has no accountable owner |  |
| SC-05 | Terminal Declaration (Step 6) | GATE D closed before Step 6 opened; every S-ID and E-ID ends at a named T-ID | Unterminated path | At least one path reaches no named conclusion -- the trace is operationally incomplete |  |
| SC-06 | Bottleneck Register (Step 9) | Every Breach Link cell contains a typed ID or the `SLA-ABSENT` token | Breach analysis disconnected from SLA evidence | Bottleneck severity cannot be verified against phase-level SLA thresholds |  |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unanchored lifecycle, an unenveloped phase, a generic role, an uncertified exception handler, an unterminated path, or a breach analysis disconnected from SLA evidence) -- and that artifact must be discarded and rebuilt from the failing step before it is filed or used.
