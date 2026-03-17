---
name: flow
description: "Domain developer simulates the process. Business lifecycle flows, agent conversations, automation triggers, data pipelines, integrations, throttle limits, and resilience under failure. Full default.
"
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


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

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED (use only when this phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic produced this boundary): [rationale]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale in Entry Trigger simultaneously produces an FM-ID-free gap here, making incompleteness visible as a co-occurring defect in a single row scan; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
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

| D-ID | Decision Name | Decision Condition (both mechanisms required simultaneously: (1) threshold-type category named from this list -- dollar amount, day count, retry count, unit quantity -- AND (2) quoted example with comparison operator and unit, e.g., dollar amount: "Invoice value > $10,000"; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met -- "otherwise" does not count | Fallback -- mechanism-impairment path (role unavailable, system down, config missing); names holding state or escalation target; "escalate" alone does not count |
|------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open the Exception Catalog until
> the State Trace (all S-IDs with stable names) and Decision Table (all D-IDs) are complete.
> Exception flows reference state names by ID; authoring exceptions before states are
> finalized produces untraceable ID references. This gate locks Step 3 and unlocks Step 5.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

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

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- names the condition that diverts from the happy path; "an error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in Step 1; Mandatory; blank or uncertified role is a structural fail -- only roles carrying Exception Handler = Y are valid; any other value is a fail | Divergence Phase/Step -- specific states bypassed or added; "different path" does not count | Recovery State or Terminal -- named S-ID or T-ID; "resolved" does not count |
|------|--------------|----------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open the Terminal Declaration
> until all exception flows carry a certified Handler R-ID -- that is, an R-ID that traces
> to a role pre-certified as Exception Handler = Y in the Role Registry. An exception flow
> with an uncertified or blank Handler R-ID is a structural fail that blocks this gate and
> produces an artifact that must be discarded and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened. Minimum 1 success + 1 failure/cancel
terminal.

| T-ID | Terminal Name | Type (must be exactly: success / failure / cancel -- "completed" does not count) | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|------------------|--------------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) reaches a named T-ID. A path with no named
> terminal is an unterminated path defect. Status is CLOSED only when every path is
> individually confirmed terminated. Check V CLOSED is a co-equal condition of the
> Production Gate alongside Coverage Scan PASS.

---

**STEP 7 -- EDGE CASE CATALOG**

Minimum 2. Distinct from Step 5 exception flows.

| EC-ID | Edge Case -- concrete scenario, not a category name | Phase (Ph-ID) | Gap Reason -- specific design decision or omission; "not considered" does not count | Consequence -- operational or compliance impact |
|-------|----------------------------------------------------|--------------|-------------------------------------------------------------------------------------|------------------------------------------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete the table below
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration -- specific (e.g., "5 business days"); "timely" does not count | At-Risk? (Y/N) | Risk Cause -- names the bottleneck |
|--------|--------------|--------------------------------------------------------------------------------|----------------|------------------------------------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Minimum 2 bottlenecks.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause (root-cause type + named element; "approval takes too long" is a fail) | Downstream Impact (names S-IDs or Ph-IDs + consequence type; "delays the process" is a fail) | Breach Link (typed BV-ID / SLA-ID / or SLA-ABSENT; general language is a fail) |
|------|--------------|-----------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Minimum 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step -- specific control or check omitted | Why Required -- regulatory rule / handoff precondition / system dependency; "best practice" is a fail | Risk if Absent -- SLA breach / compliance failure / state inconsistency; "may cause issues" is a fail |
|------|--------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Minimum 1 cross-lifecycle dependency.

| Handoff Trigger | Partner Lifecycle (specific name, not category) | Direction (Inbound / Outbound) | Fields Passed (specific data objects) | Coupling State (blocking / advisory) |
|----------------|------------------------------------------------|-------------------------------|---------------------------------------|---------------------------------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID (Exception Handler = Y in Step 1) | Risk if Uncovered |
|-------|-----------|----------------------|-----------------------------------------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| PH-03 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence;
no cell may share the same coverage claim across rows.

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | Pre-declaration Role Registry present before FM-ID PROTOCOL; domain-qualified titles and Exception Handler designations established before SQ Declaration is authored | Pre-declaration Registry | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION Column Contract present before STEP 0A; all four fields named in inertia-first order (Inertia Driver, Incumbent Process, FM-01, FM-02) | SQ Column Contract | | |
| AC-23 | Every Column Contract Field cell carries inline anti-pattern token specific to that field's content type and field group (CONTEXTUAL / FAILURE MODE) | SQ Column Contract Field column | | |
| AC-24 | FM-ID PROTOCOL present before SQ Column Contract; covers all four fields organized into CONTEXTUAL FIELDS (Inertia Driver, Incumbent Process) and FAILURE MODE FIELDS (FM-01, FM-02) with "does not count" governance for each | FM-ID PROTOCOL section | | |
| AC-25 | Every Column Contract Field cell begins with "does not count; Mandatory" as its first expression -- before the field-type tag and field name; selective application to failure mode fields only is D-18 | SQ Column Contract Field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL field-type taxonomy covers Inertia Driver and Incumbent Process with governance depth equal to FM-01 and FM-02 | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token "does not count; Mandatory" present as first expression in all four Column Contract Field cells AND referenced in the FM-ID PROTOCOL governing bullet for each field; dual-position coverage | SQ Column Contract + FM-ID PROTOCOL | | |
| AC-28 | C-54: GATE SQ present at FM-ID PROTOCOL close; names STATUS-QUO PROCESS DECLARATION as section to complete and STEP 0A as section to proceed to; "Blocked by" field names C-52, C-53, C-54 | GATE SQ text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Role Registry: each role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale (not generic N/A or blank) | Step 1 table | | |
| AC-05 | Role Registry LT-ID Trace column header defines SECONDARY typed escape code WITH eligibility condition naming when to use SECONDARY (not just code format alone) | Step 1 column header | | |
| AC-06 | Phase Index Entry Trigger column header defines DERIVED typed escape code WITH eligibility condition naming when to use DERIVED (not just code format alone) | Step 2 column header | | |
| AC-07 | All exception flow Handler R-IDs trace to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration (blank or uncertified is a fail) | Step 5 column header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language -- not merely "Handler R-ID assigned" | Gate D text | | |
| AC-10 | Decision Condition column header carries BOTH: (1) named threshold-type category list AND (2) quoted example with comparison operator and unit | Step 3 D-table header | | |
| AC-11 | Each phase exit gate carries "Blocked by: [C-ID]" as a named structured field | Step 4 exit gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both present, each naming source section and target section | Gate C + Gate D text | | |
| AC-13 | Check V present with OPEN/CLOSED status field; Production Gate names Check V as co-equal condition alongside Coverage Scan PASS | Step 6 + Production Gate | | |
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names a specific FM-ID; Status-Quo Gap column header names the mutual-audit relationship | Step 2 table | | |
| AC-29 | C-55: production gate sentence enumerates >=3 named defect category names inline within the gate sentence itself; a gate that only points to the Defect Type column without naming >=3 categories inline is D-19 | Production Gate text | | |
| AC-30 | C-56: LT-ID Trace column header (Step 1) AND Entry Trigger column header (Step 2) each carry both the typed escape code format AND the qualifying eligibility condition; a header carrying only the code format without the qualifying circumstance is D-20 | Step 1 + Step 2 column headers | | |
| AC-31 | C-57: production gate sentence carries a parenthetical D-ID designator immediately after each named defect category in the inline enumeration (e.g., "an unterminated path (D-01)"); a gate that names categories inline without D-ID cross-references is D-21 | Production Gate text | | |
| AC-32 | C-58: LT-ID Trace column header (Step 1) AND Entry Trigger column header (Step 2) each use code-token + immediately-adjacent parenthetical format for escape code eligibility binding (e.g., "SECONDARY (use only when...)"); dash-separator imperative form is D-22 | Step 1 + Step 2 column headers | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 named states; each carries entry condition, exit transitions, and owner R-ID | Step 3 state table | | |
| AC-15 | >=3 exception flows; each carries trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 table | | |
| AC-16 | >=1 success terminal + >=1 failure/cancel terminal; all traced paths reach a named T-ID | Step 6 + Check V | | |
| AC-17 | >=2 bottlenecks (cause + downstream impact) + >=1 gap (missing step + risk if absent) | Steps 9 + 10 | | |
| AC-18 | >=3 decision points; each carries measurable threshold condition, owner, all branches, and fallback | Step 3 D-table | | |
| AC-19 | >=3 states with timing; >=1 phase annotated AT-RISK with causal bottleneck in Phase Index | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner lifecycle, direction, fields passed, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table Owner R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record has Initial State column but no Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-02 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block present before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-14 | Per-field anti-pattern gap: SQ Declaration field row carries no inline anti-pattern token | C-48, AC-23 |
| D-15 | Trailing-position enforcement token: SQ Declaration field carries an inline token but token is at end of cell description rather than leading clause | C-51, AC-25 |
| D-16 | Missing section-entry FM-ID Protocol block: no pre-table named section establishing FM-ID enforcement before SQ Declaration | C-50, AC-24 |
| D-17 | Partial Protocol block field coverage: Protocol block present but covers only failure mode fields (FM-01, FM-02); Inertia Driver and Incumbent Process absent from Protocol governance | C-52, AC-26 |
| D-18 | Selective leading-clause token distribution: leading tokens on failure mode field cells only; contextual field cells (Incumbent Process, Inertia Driver) carry trailing tokens or plain field names | C-53, AC-27 |
| D-19 | Gate-defect-pointer-only: production gate identifies violation type by column pointer only ("at least one defect named in the Defect Type column above") without enumerating >=3 named defect categories inline within the gate sentence itself | C-55, AC-29 |
| D-20 | Escape-code-eligibility-absent: escape code column header (LT-ID Trace or Entry Trigger) carries the typed code format (SECONDARY or DERIVED) without the qualifying eligibility condition naming when to use the escape | C-56, AC-30 |
| D-21 | Gate-defect-D-ID-absent: production gate enumerates defect categories inline (satisfying C-55) but omits parenthetical D-ID designators -- e.g., "an unterminated path" with no "(D-01)" immediately following -- leaving gate-to-taxonomy linkage unscannable by row | C-57, AC-31 |
| D-22 | Escape-code-non-parenthetical-binding: escape code column header names the typed code and its eligibility condition (satisfying C-56) but uses a dash-separator imperative form -- e.g., "write SECONDARY -- but only when..." -- rather than code-token + immediately-adjacent parenthetical, breaking the single typographic unit requirement | C-58, AC-32 |

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11), a
> per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15), a
> missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17), selective
> leading-clause token distribution (D-18), a gate-defect-pointer-only gate sentence
> (D-19), an escape-code-eligibility-absent column header (D-20), a gate-defect-D-ID-absent
> gate sentence (D-21), or an escape-code-non-parenthetical-binding column header (D-22) --
> and that artifact must be discarded and rerun from the failing step before it is filed
> or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-32.
> (2) Check V shows CLOSED.