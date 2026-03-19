You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Establish the
DOMAIN ROLE REGISTRY first, then read the FM-ID PROTOCOL before filling the STATUS-QUO
PROCESS DECLARATION Column Contract. Every Column Contract field definition begins with a
compact enforcement token; read the token before reading the content instruction.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Author this table completely before proceeding to FM-ID PROTOCOL.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) whose Initial State or Initial Phase this role appears in; if role exists outside all LT scopes write SECONDARY (use only when role has no LT-bound trigger, naming why this role exists without any LT anchor): [rationale]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles. Domain-qualified titles are mandatory -- the Incumbent Process and Inertia
Driver fields you will fill next should reference the same domain context anchored here.

> Do not proceed to FM-ID PROTOCOL until every R-ID carries a domain-qualified title and an
> Exception Handler designation (Y/N). Generic placeholder titles block this gate.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION Column Contract below and must appear in every Phase Index Status-Quo Gap cell
downstream.

This protocol governs all four fields in the SQ Declaration, organized by field type:

**CONTEXTUAL FIELDS** -- establish the organizational setting:

- **Inertia Driver**: does not count if the entry would apply to any legacy process; must
  name the specific organizational, systemic, or economic reason this particular incumbent
  persists despite its failure modes. "Familiarity" or "switching costs" alone does not
  count without naming the specific mechanism (e.g., a named integration dependency, a
  contractual lock-in, a compliance regime that approved the incumbent). Assign the Inertia
  Driver before FM-01 and FM-02 -- the failure modes are symptoms of an incumbent that
  persists for this specific reason.

- **Incumbent Process**: does not count if it names only a department or a generic method;
  must name the specific tool, procedure, or workaround being replaced, including enough
  operational context to understand how it is used. A single-word tool name without context
  does not count. The Incumbent Process should be consistent with the Inertia Driver.

**FAILURE MODE FIELDS** -- name what the incumbent fails to provide:

- **FM-01**: does not count if it describes a quality attribute ("error-prone," "slow,"
  "inefficient"); must name the specific detection or prevention mechanism the incumbent
  fails to provide. Assign identifier FM-01 inline.

- **FM-02**: does not count if it is a restatement, subcategory, or downstream consequence
  of FM-01; must name a second orthogonal failure mode. Assign identifier FM-02 inline.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally unanchored
and is a fail. The equal governance depth for Contextual Fields and Failure Mode Fields is
intentional -- Incumbent Process and Inertia Driver cells failing their "does not count"
threshold produce the same downstream gap as a failing FM-01 or FM-02 cell.

> **GATE SQ**: Author the STATUS-QUO PROCESS DECLARATION Column Contract completely before
> proceeding to STEP 0A. Every Content cell in the Fill Table must be non-blank. A Column
> Contract with any blank Content cell is incomplete and blocks GATE SQ.
> Blocked by: C-52, C-53, C-54.

---

### STATUS-QUO PROCESS DECLARATION -- Column Contract

Read this table completely before filling the Content column in the Fill Table below.
Fields are ordered inertia-first: Inertia Driver appears before Incumbent Process to
establish organizational context before technical failure modes are named.

| Field | Fill Requirement | Does Not Count |
|-------|-----------------|----------------|
| does not count; Mandatory -- CONTEXTUAL FIELD -- Inertia Driver | names the specific organizational, systemic, or economic reason this particular incumbent process persists despite FM-01 and FM-02; explain the mechanism that makes switching costly or impossible | "familiarity"; "switching costs" without naming the specific mechanism; any reason that would apply equally to any other legacy process; blank |
| does not count; Mandatory -- CONTEXTUAL FIELD -- Incumbent Process | names the specific tool, procedure, or workaround being replaced; include the operational context that makes clear how it is used in this lifecycle | "manual process" without tool name; department or team name alone; single-word tool name without context; any entry inconsistent with the Inertia Driver named above |
| does not count; Mandatory -- FAILURE MODE FIELD -- FM-01 | names the specific detection or prevention mechanism the incumbent fails to provide; orthogonal to FM-02; assign identifier FM-01 inline | "error-prone," "inefficient," "slow"; generic quality attribute; category name without naming the specific missing mechanism |
| does not count; Mandatory -- FAILURE MODE FIELD -- FM-02 | names a second failure mode orthogonal to FM-01; assign identifier FM-02 inline | restatement of FM-01; subcategory; downstream consequence; "same as FM-01 but in a different phase"; any entry that would remain true if FM-01 were fixed |

### STATUS-QUO PROCESS DECLARATION -- Fill Table

| SQ-Field | Content |
|----------|---------|
| Inertia Driver | |
| Incumbent Process | |
| FM-01 | |
| FM-02 | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" or "a request is received" does not count; name the specific initiating signal | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Author this table completely before proceeding to STEP 1.

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary; "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. All failure surfaces must be orthogonal.

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY (Verification Pass)**

The Role Registry was established in the Pre-Declaration Pass above. Before opening the
Phase Index, verify completeness against GATE A.

> **GATE A**: Do not open the Phase Index until all of the following are confirmed:
> (1) Every R-ID carries a domain-qualified title -- no generic placeholders.
> (2) Every R-ID has an Exception Handler designation (Y/N); blank is a fail.
> (3) Every R-ID has an LT-ID Trace or SECONDARY:rationale; generic "N/A" is a fail.
> (4) At least one R-ID carries Exception Handler = Y.
> If any gap is found, extend the Role Registry before proceeding.
> Blocked by: C-05, C-11, C-23, C-36

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry
> Trigger carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a
> specific FM-ID from the STATUS-QUO PROCESS DECLARATION.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED (use only when this phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic produced this boundary): [rationale]; generic "N/A" or blank is a fail) | Status-Quo Gap (write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration; "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states. Minimum 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- specific event or predecessor state; "after previous step" does not count | Exit Transitions -- labeled outbound paths naming trigger and destination; "then continue" does not count | Owner (R-ID) -- must appear in Step 1; blank is a fail | Timing -- specific duration or N/A + reason | SLA Status (Normal / AT-RISK / Critical) |
|------|--------------|------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------|------------------------------------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |
| S-04 | | | | | | | |
| S-05 | | | | | | | |
| S-06 | | | | | | | |

Minimum 3 states with timing. Minimum 1 AT-RISK.

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (both required: (1) threshold-type category -- dollar amount, day count, retry count, unit quantity -- AND (2) quoted example with comparison operator and unit, e.g., "Invoice value > $10,000"; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met -- "otherwise" does not count | Fallback -- mechanism-impairment path; names holding state or escalation target; "escalate" alone does not count |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 fork-join or explicit "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path name]
Branch B:       [concurrent path name]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C**: Do not open the Exception Catalog until the State Trace (all S-IDs) and
> Decision Table (all D-IDs) are complete. Exception flows reference state names by ID.
> Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. "Blocked by" is mandatory in every gate.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state that closes this phase]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID reached on clean exit]
Failure:        [T-ID or named exception triggered on exit failure]
Blocked by:     [C-ID(s) -- Mandatory; blank is a structural fail]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED before this step is opened. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition that diverts from the happy path; "an error occurs" does not count | Handler (R-ID) -- must trace to a role with Exception Handler = Y in Step 1; blank or uncertified role is a structural fail | Divergence Phase/Step -- specific states bypassed or added; "different path" does not count | Recovery State or Terminal -- named S-ID or T-ID; "resolved" does not count |
|------|--------------|----------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D**: Do not open the Terminal Declaration until all exception flows carry a
> certified Handler R-ID tracing to Exception Handler = Y in the Role Registry.
> Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (must be exactly: success / failure / cancel) | Reached From -- list all S-IDs and E-IDs; blank is a structural fail |
|------|--------------|------------------|--------------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V**: Confirm each path (happy path + every E-ID) reaches a named T-ID.
> Status: [ OPEN / CLOSED ]

---

**STEP 7 -- EDGE CASE CATALOG**

Minimum 2. Distinct from Step 5 exception flows.

| EC-ID | Edge Case -- concrete scenario, not a category name | Phase (Ph-ID) | Gap Reason -- specific design decision or omission | Consequence -- operational or compliance impact |
|-------|----------------------------------------------------|--------------|-------------------------------------------------------------------------------------|------------------------------------------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete the table below
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration -- specific; "timely" does not count | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|------------------------------------------------------|----------------|------------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Minimum 2 bottlenecks.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause (root-cause type + named element) | Downstream Impact (names S-IDs or Ph-IDs + consequence type) | Breach Link (BV-ID / SLA-ID / or SLA-ABSENT) |
|------|--------------|-----------------|------------------------------------------|--------------------------------------------------------------|-----------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Minimum 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step -- specific control or check omitted | Why Required | Risk if Absent |
|------|--------------|--------------------------------------------------|--------------|----------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Minimum 1 cross-lifecycle dependency.

| Handoff Trigger | Partner Lifecycle | Direction (Inbound / Outbound) | Fields Passed | Coupling State (blocking / advisory) |
|----------------|-------------------|-------------------------------|---------------|---------------------------------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| PH-03 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

Run all AC-01 through AC-32 checks. Any FAIL blocks the Production Gate.

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11) --
> and that artifact must be discarded and rerun from the failing step before it is filed.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for all AC items.
> (2) Check V shows CLOSED.

Write artifact to: signals/simulate/lifecycle/{{topic}}-lifecycle-{{date}}.md
If --output <path> provided: write to <path>/{topic}-{skill}-{date}.md (flat, no namespace prefix).
Include frontmatter: skill: simulate-lifecycle, topic: {{topic}}, date: {{date}}
