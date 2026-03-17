---
skill: flow-lifecycle
round: 19
rubric-version: v19
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v19-2026-03-16.md
floor: flow-lifecycle-variate-R18-2026-03-16.md V-05
---

# flow-lifecycle -- Round 19 Variations (rubric v19: C-55, C-56)

Round 19 holds the R18 V-05 full floor and probes two new aspirational criteria
formalized from Round 18 scoring evidence:

- **C-55 -- Gate Defect Inline Enumeration**: the production gate sentence names >=3
  defect category names inline within the sentence itself -- not only a pointer to the
  Defect Type column ("at least one defect named in the Defect Type column above").
  Inline categories may include D-IDs parenthetically but must carry the named type
  (e.g., "an unterminated path, an uncertified exception handler, a missing or partial
  SQ Declaration"). Source signal: R18 V-05 passed (gate enumerated categories inline);
  R18 V-01 produced only the column pointer.

- **C-56 -- Escape Code Column Eligibility Operationalization**: each escape code column
  header (LT-ID Trace in Step 1; Entry Trigger in Step 2) carries both the typed escape
  code format (SECONDARY:[rationale] or DERIVED:[rationale]) AND the qualifying eligibility
  condition naming when to use the escape (e.g., "use only when role exists outside all
  LT scopes"; "use only when phase boundary results from multiple LT-IDs combining").
  A column header carrying only the typed code format without the qualifying circumstance
  is D-20 (escape-code-eligibility-absent). Source signal: R18 V-01/V-05 passed AC-05/AC-06
  (both had eligibility co-located in column headers); R18 V-02/V-03/V-04 carried only
  the code format.

Denominator: 54 -> 56. Aspirational count: 46 -> 48.

Two new defect types added to all variation taxonomies:
- **D-19**: Gate-defect-pointer-only
- **D-20**: Escape-code-eligibility-absent

Two new Coverage Scan rows added to all variations:
- **AC-29**: C-55 check
- **AC-30**: C-56 check

**Variation axes explored:**

- V-01: Role sequence (pre-declaration role registry) -- single axis.
  C-55 TARGET (gate updated to enumerate defect categories inline).
  C-56 HOLD/PASS (eligibility conditions stable from R18 V-01).

- V-02: Output format (SQ Declaration as Column Contract) -- single axis.
  C-56 TARGET (escape code column headers gain eligibility conditions).
  C-55 TARGET (gate updated to enumerate defect categories inline).

- V-03: Lifecycle emphasis (phase-first framing + GATE SQ) -- single axis.
  C-56 TARGET (escape code column headers gain eligibility conditions).
  C-55 TARGET (gate updated to enumerate defect categories inline).

- V-04: Phrasing register (conversational FM-ID Guidance) + role sequence -- combination.
  C-55 TARGET (gate enumeration in conversational register).
  C-56 TARGET (eligibility conditions in conversational column headers).

- V-05: Full combination (R18 V-05 floor). C-55 HOLD/PASS. C-56 HOLD/PASS.
  Adds AC-29/AC-30 to coverage scan and D-19/D-20 to defect taxonomy.

---

## V-01 -- Role Sequence: Pre-Declaration Role Registry + Inline Gate Enumeration

**Variation axis:** Role sequence -- DOMAIN ROLE REGISTRY precedes all other content.
All R18 V-01 structural properties held. Single change: production gate sentence updated
to enumerate >=3 named defect categories inline (C-55 TARGET). C-56 holds from R18 V-01
(escape code eligibility conditions were already present in LT-ID Trace and Entry Trigger
column headers). New AC-29/AC-30 and D-19/D-20 added.

**Hypothesis:** C-55 is format-position-independent -- inline gate enumeration is
achievable in the role-first structural arrangement without perturbing any other criterion.
The gate text change does not interact with the pre-declaration sequencing axis. Prediction:
C-55 TARGET; C-56 HOLD/PASS (AC-05/AC-06 remain PASS from R18 V-01 structure); AC-29
PASS; AC-30 PASS (stable).

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Establish the
DOMAIN ROLE REGISTRY first, then read the FM-ID PROTOCOL before filling the STATUS-QUO
PROCESS DECLARATION. Every field cell in the SQ Declaration begins with a compact
enforcement token; read the token before reading the content instruction.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Author this table completely before proceeding to FM-ID PROTOCOL.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) whose Initial State or Initial Phase this role appears in; if role exists outside all LT scopes write SECONDARY (use only when role has no LT-bound trigger, naming why this role exists without any LT anchor): [rationale]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

> Do not proceed to FM-ID PROTOCOL until every R-ID carries a domain-qualified title and
> an Exception Handler designation (Y/N). Generic placeholder titles are a fail.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION below and must appear in every Phase Index Status-Quo Gap cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround -- not a
  department and not a generic "manual" description. A single-word tool name without context
  does not count.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails to
  provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier FM-01
  inline.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement, subcategory,
  or downstream consequence of FM-01 does not count. Assign identifier FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason the
  incumbent persists despite FM-01 and FM-02. A reason that would apply to any legacy process
  does not count.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally unanchored
and is a fail. Author the STATUS-QUO PROCESS DECLARATION completely before proceeding to
STEP 0A.

---

### STATUS-QUO PROCESS DECLARATION

| SQ-Field | Content |
|----------|---------|
| does not count; Mandatory -- Incumbent Process: names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department or team alone does not count; a single-word tool name without context does not count | |
| does not count; Mandatory -- FM-01: first failure mode; names the specific detection or prevention mechanism the incumbent fails to provide; "error-prone," "inefficient," or "slow" does not count; a generic category name without a missing mechanism does not count; assign identifier FM-01 inline | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement, subcategory, or downstream consequence of FM-01 does not count; "same as FM-01 in a different phase" does not count; assign identifier FM-02 inline | |
| does not count; Mandatory -- Inertia Driver: names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count; a reason that would apply equally to any other legacy process does not count | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" or "a request is received" does not count; name the specific initiating signal | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; a generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail; if the trigger enters an existing phase mid-run, name that containing phase |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

The Role Registry was established in the Pre-Declaration Pass above. Before opening the Phase
Index, verify completeness against GATE A.

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

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or DERIVED (use only when this phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic produced this boundary): [rationale]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale in Entry Trigger simultaneously produces an FM-ID-free gap here; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
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

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 orthogonal failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | Pre-declaration Role Registry present before FM-ID PROTOCOL; every R-ID carries domain-qualified title and Exception Handler designation before SQ Declaration is authored | Pre-declaration Role Registry | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; block names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration block | | |
| AC-23 | Every field row in STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token specific to that field's content type | SQ Declaration field definitions | | |
| AC-24 | A named FM-ID PROTOCOL section appears immediately before the STATUS-QUO PROCESS DECLARATION table; block covers all four fields (Incumbent Process, FM-01, FM-02, Inertia Driver) with "does not count" guidance for each | FM-ID PROTOCOL section | | |
| AC-25 | Every STATUS-QUO PROCESS DECLARATION field definition cell begins with "does not count; Mandatory" as its first expression -- before the field name and content description | SQ Declaration field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers all four SQ Declaration fields with equal specificity | FM-ID PROTOCOL section | | |
| AC-27 | C-53: Leading-clause token present as first expression in all four SQ Declaration field cells | SQ Declaration field cells | | |
| AC-28 | C-54: FM-ID PROTOCOL closes with explicit forward sequencing instruction naming both the section to complete (STATUS-QUO PROCESS DECLARATION) and the section to proceed to (STEP 0A) | FM-ID PROTOCOL closing text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Role Registry: each role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale (not generic N/A or blank) | Step 1 table | | |
| AC-05 | Role Registry LT-ID Trace column header defines SECONDARY typed escape code WITH eligibility condition naming when to use SECONDARY (e.g., "use only when role has no LT-bound trigger") -- not just the code format alone | Step 1 column header | | |
| AC-06 | Phase Index Entry Trigger column header defines DERIVED typed escape code WITH eligibility condition naming when to use DERIVED (e.g., "use only when phase boundary results from multiple LT-IDs combining") -- not just the code format alone | Step 2 column header | | |
| AC-07 | All exception flow Handler R-IDs trace to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration (blank or uncertified is a fail) | Step 5 column header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language -- not merely "Handler R-ID assigned" | Gate D text | | |
| AC-10 | Decision Condition column header carries BOTH: (1) named threshold-type category list AND (2) quoted example with comparison operator and unit | Step 3 D-table header | | |
| AC-11 | Each phase exit gate carries "Blocked by: [C-ID]" as a named structured field | Step 4 exit gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both present, each naming source section and target section | Gate C + Gate D text | | |
| AC-13 | Check V present with OPEN/CLOSED status field; Production Gate names Check V as co-equal condition alongside Coverage Scan PASS | Step 6 + Production Gate | | |
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names a specific FM-ID; Status-Quo Gap column header names the mutual-audit relationship | Step 2 table | | |
| AC-29 | C-55: production gate sentence enumerates >=3 named defect category names inline within the gate sentence itself; a gate that only points to the Defect Type column without naming >=3 categories inline is D-19 | Production Gate text | | |
| AC-30 | C-56: LT-ID Trace column header (Step 1) AND Entry Trigger column header (Step 2) each carry both the typed escape code format AND the qualifying eligibility condition; a header carrying only "SECONDARY:[rationale]" or "DERIVED:[rationale]" without the qualifying circumstance is D-20 | Step 1 + Step 2 column headers | | |

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
| D-17 | Partial Protocol block field coverage: Protocol block present but covers only failure mode fields (FM-01, FM-02); contextual fields (Incumbent Process, Inertia Driver) absent from Protocol governance | C-52, AC-26 |
| D-18 | Selective leading-clause token distribution: leading tokens on failure mode field cells only; contextual field cells carry trailing tokens or plain field names | C-53, AC-27 |
| D-19 | Gate-defect-pointer-only: production gate identifies violation type by column pointer only ("at least one defect named in the Defect Type column above") without enumerating >=3 named defect categories inline within the gate sentence itself | C-55, AC-29 |
| D-20 | Escape-code-eligibility-absent: escape code column header (LT-ID Trace or Entry Trigger) carries the typed code format (SECONDARY or DERIVED) without the qualifying eligibility condition naming when to use the escape | C-56, AC-30 |

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), or an escape-code-eligibility-absent column header (D-20) -- and
> that artifact must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-30.
> (2) Check V shows CLOSED.

---

## V-02 -- Output Format: SQ Declaration as Column Contract + Escape Code Eligibility

**Variation axis:** Output format -- STATUS-QUO PROCESS DECLARATION uses a two-part
Column Contract + Fill Table format. Single-axis change from R18 V-02: escape code column
headers (LT-ID Trace in Step 1; Entry Trigger in Step 2) are upgraded to include eligibility
conditions alongside the typed code format (C-56 TARGET). Production gate updated to
enumerate defect categories inline (C-55 TARGET). All other R18 V-02 properties held.

**Hypothesis:** Column Contract format separates field definition (Fill Requirement +
Does Not Count) from field execution (Content cell), creating structural pre-commitment
at the column-specification layer. Adding eligibility conditions to escape code column
headers tests whether the Column Contract's structural emphasis on point-of-use rule
placement (which produces D-14/D-15 coverage) generalizes to the escape-code eligibility
domain (C-56) without requiring changes to any other structural element. The eligibility
condition format in the Step 1 and Step 2 column headers is identical to R18 V-01 but
appears in a format whose other sections differ structurally -- testing whether C-56
compliance is column-header-isolated or interacts with surrounding format choices.
Prediction: C-55 TARGET (inline gate enumeration), C-56 TARGET (eligibility in Step 1
and Step 2 headers), AC-29 PASS, AC-30 PASS.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Read the
FM-ID PROTOCOL before filling the STATUS-QUO PROCESS DECLARATION. The SQ Declaration
uses a two-part format: a Column Contract defines each field, followed by a fill table.
Read the Column Contract completely before filling the Content column.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION Column Contract below and must appear in every Phase Index Status-Quo Gap
cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround -- not a
  department and not a generic "manual" description. A single-word tool name without context
  does not count.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails to
  provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier FM-01
  inline.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement, subcategory,
  or downstream consequence of FM-01 does not count. Assign identifier FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason the
  incumbent persists despite FM-01 and FM-02. A reason that would apply to any legacy process
  does not count.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally unanchored
and is a fail. Author the STATUS-QUO PROCESS DECLARATION completely before proceeding to
STEP 0A.

---

### STATUS-QUO PROCESS DECLARATION -- Column Contract

Read this table completely before filling the Content column below.

| Field | Fill Requirement | Does Not Count |
|-------|-----------------|----------------|
| does not count; Mandatory -- Incumbent Process | names the specific named process, tool, or workaround being replaced; include the tool or process name and its operational context | "manual process" without tool name; department or team name alone; single-word tool name without context |
| does not count; Mandatory -- FM-01 | names the specific detection or prevention mechanism the incumbent fails to provide; assign identifier FM-01 inline | "error-prone," "inefficient," "slow"; generic quality attribute; category name without naming the specific missing mechanism |
| does not count; Mandatory -- FM-02 | names a second failure mode orthogonal to FM-01; assign identifier FM-02 inline | restatement of FM-01; subcategory; downstream consequence; "same as FM-01 in a different phase" |
| does not count; Mandatory -- Inertia Driver | names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02 | "familiarity"; "it works well enough"; any reason equally applicable to all legacy processes |

### STATUS-QUO PROCESS DECLARATION -- Fill Table

| SQ-Field | Content |
|----------|---------|
| Incumbent Process | |
| FM-01 | |
| FM-02 | |
| Inertia Driver | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" or "a request is received" does not count; name the specific initiating signal | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; a generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category are not orthogonal | Gate Domain -- schema section; "general" does not count | Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles
> carry domain-qualified titles, every role has an Exception Handler designation, and every
> role has an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP) | Exception Handler (Y/N) -- Mandatory; at least one Y required; blank is a fail | LT-ID Trace (LT-ID from STEP 0A; or SECONDARY (use only when role exists outside all LT scopes, naming why this role exists without any LT-bound trigger): [rationale]; generic "N/A" or blank is a fail) |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger carries
> LT-ID or DERIVED:rationale; every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or DERIVED (use only when this phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic produced this boundary): [rationale]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit pair with Entry Trigger; write FM-ID from STATUS-QUO PROCESS DECLARATION; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-------------|---------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|-----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |
| S-04 | | | | | | | |
| S-05 | | | | | | | |
| S-06 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (both mechanisms required: (1) threshold-type category from -- dollar amount, day count, retry count, unit quantity -- AND (2) quoted example with comparison operator and unit; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback -- mechanism-impairment path; names holding state or escalation target |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------|---------------------------|---------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths:**

```
Fork (S-ID):    [branching state]
Branch A/B:     [concurrent paths]
Join condition: [merge requirement]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open Exception Catalog until
> State Trace and Decision Table complete. Source: Step 3 --> Target: Step 5.
> Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output]
SLA envelope:   [duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception]
Blocked by:     [C-ID(s) -- Mandatory]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in Step 1; Mandatory; blank or uncertified role is a structural fail | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|---------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration
> until all exception flows carry a certified Handler R-ID tracing to Exception Handler = Y.
> An uncertified or blank Handler R-ID is a structural fail -- discard and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From |
|------|--------------|----------------------------------|-------------|
| T-01 | | | |
| T-02 | | | |

> **Check V** -- Status: [ OPEN / CLOSED ]
> Confirm every path reaches a named T-ID. Unterminated path = D-01. Co-equal with
> Coverage Scan PASS for Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|-----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? | Risk Cause |
|--------|--------------|----------------|---------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|-------------|---------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State |
|----------------|-----------------|----------|--------------|---------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|---------------------|-------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| PH-03 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-01 | STEP 0A >=3 LT-IDs; all four fields per row | STEP 0A | | |
| AC-02 | STEP 0B >=3 orthogonal failure surfaces | STEP 0B | | |
| AC-21 | SQ Declaration Column Contract present before STEP 0A; all four fields | SQ Column Contract | | |
| AC-23 | Every Column Contract Field cell carries inline anti-pattern token specific to that field | SQ Column Contract Field column | | |
| AC-24 | FM-ID PROTOCOL present before SQ Column Contract; covers all four fields with "does not count" guidance | FM-ID PROTOCOL | | |
| AC-25 | Every SQ Declaration Column Contract Field cell begins with "does not count; Mandatory" as first expression | SQ Column Contract Field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers Incumbent Process and Inertia Driver with governance depth equal to FM-01 and FM-02 | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token present as first expression in all four Column Contract Field cells | SQ Column Contract Field column | | |
| AC-28 | C-54: FM-ID PROTOCOL closes with explicit forward sequencing instruction naming SQ Declaration and STEP 0A | FM-ID PROTOCOL closing | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-04 | Role Registry domain-qualified titles, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | LT-ID Trace column header defines SECONDARY typed escape code WITH eligibility condition (not just code format alone) | Step 1 column header | | |
| AC-06 | Entry Trigger column header defines DERIVED typed escape code WITH eligibility condition (not just code format alone) | Step 2 column header | | |
| AC-07 | All exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition header: category list AND quoted example | Step 3 D-table header | | |
| AC-11 | Phase exit gates: "Blocked by: [C-ID]" present | Step 4 gates | | |
| AC-12 | Gate C and Gate D both present, source and target named | Gate C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 + Gate | | |
| AC-22 | Phase Index Status-Quo Gap mutual-audit principle named | Step 2 | | |
| AC-29 | C-55: production gate sentence enumerates >=3 named defect category names inline; column pointer alone is D-19 | Production Gate text | | |
| AC-30 | C-56: LT-ID Trace header AND Entry Trigger header each carry typed code format AND qualifying eligibility condition; format-only is D-20 | Step 1 + Step 2 headers | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry, exit, owner | Step 3 | | |
| AC-15 | >=3 exception flows with certified handlers | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths terminate | Steps 6 + V | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decision points with threshold, owner, branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff | Step 11 | | |

**Defect Type Taxonomy:** [D-01 through D-20 as in V-01]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), or an escape-code-eligibility-absent column header (D-20) -- and
> that artifact must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-30.
> (2) Check V shows CLOSED.

---

## V-03 -- Lifecycle Emphasis: Phase-First Framing + GATE SQ + Full C-55/C-56 Coverage

**Variation axis:** Lifecycle emphasis -- a LIFECYCLE PHASE FRAMING block precedes the
FM-ID PROTOCOL, establishing the lifecycle type, phase count, and cross-lifecycle handoffs
before the SQ Declaration is authored. Holds R18 V-03's phase-first framing axis and GATE
SQ labeled gate. Two targeted changes from R18 V-03: (1) escape code column headers for
LT-ID Trace and Entry Trigger gain eligibility conditions (C-56 TARGET); (2) production
gate updated to enumerate defect categories inline (C-55 TARGET).

**Hypothesis:** Phase-first framing does not interact with escape code eligibility
operationalization because eligibility conditions are embedded in column headers (Step 1
and Step 2) -- well after the pre-protocol Phase Framing block. The structural argument is
that C-56 is column-header-scoped: it depends only on what the column header says, not on
what precedes it. Phase-first framing displaces the FM-ID Protocol from the document's
first structural position, which tested C-52/C-53/C-54 in R18; C-56 is tested orthogonally
by whether the column headers themselves carry eligibility language regardless of their
position relative to the Phase Framing block. Prediction: C-55 TARGET, C-56 TARGET, AC-29
PASS, AC-30 PASS; phase-first framing does not displace escape code eligibility.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every numbered step in order. Establish the
lifecycle's phase structure first, then read the FM-ID PROTOCOL before filling the
STATUS-QUO PROCESS DECLARATION. Every field cell in the SQ Declaration begins with a
compact enforcement token; read the token before reading the content instruction.

---

### LIFECYCLE PHASE FRAMING

Before authoring the SQ Declaration or trigger inventory, establish the lifecycle's phase
structure. This framing determines how FM-IDs are anchored to phases downstream.

```
Lifecycle type:    [L2O / P2P / Period Close / Case Lifecycle / other -- name specifically]
Phase count:       [expected number of phases -- minimum 3]
Phase boundaries:  [name the expected phase transition points, e.g.,
                   "Order Entry -> Credit Review -> Fulfillment -> Invoicing -> Collection"]
Cross-lifecycle:   [name any handoff to a partner lifecycle; or "self-contained"]
```

Complete this framing block before proceeding to FM-ID PROTOCOL.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION below and must appear in every Phase Index Status-Quo Gap cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround. A single-
  word tool name without context does not count. The Incumbent Process should be consistent
  with the lifecycle type named in the Phase Framing above.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails to
  provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier FM-01
  inline. FM-01 should map to a gap visible within at least one phase named in the Phase
  Framing.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement, subcategory,
  or downstream consequence of FM-01 does not count. Assign identifier FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason the
  incumbent persists despite FM-01 and FM-02. "Familiarity" without specificity does not
  count. The Inertia Driver explains why the lifecycle type named in Phase Framing continues
  to operate under the incumbent.

A Phase Index Status-Quo Gap cell with no FM-ID from this block is structurally unanchored
and is a fail.

> **GATE SQ**: Author the STATUS-QUO PROCESS DECLARATION completely before proceeding to
> STEP 0A. A SQ Declaration with any blank Content cell is incomplete and blocks GATE SQ.
> Blocked by: C-52, C-53, C-54.

---

### STATUS-QUO PROCESS DECLARATION

| SQ-Field | Content |
|----------|---------|
| does not count; Mandatory -- Incumbent Process: names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department or team alone does not count; a single-word tool name without context does not count | |
| does not count; Mandatory -- FM-01: first failure mode; names the specific detection or prevention mechanism the incumbent fails to provide; "error-prone," "inefficient," or "slow" does not count; assign identifier FM-01 inline | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement, subcategory, or downstream consequence of FM-01 does not count; assign identifier FM-02 inline | |
| does not count; Mandatory -- Inertia Driver: names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" without specificity does not count; a reason that would apply equally to any other legacy process does not count | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" does not count; name the specific initiating signal | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase -- Mandatory; blank is a structural fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------------|-------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category are not orthogonal | Gate Domain -- schema section; "general" does not count | Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role
> has an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified title; generic labels do not count | Domain -- process function | Exception Handler (Y/N) -- Mandatory; at least one Y required | LT-ID Trace (LT-ID from STEP 0A; or SECONDARY (use only when role exists outside all LT scopes, naming why this role exists without any LT-bound trigger): [rationale]; generic "N/A" or blank is a fail) |
|------|------------------------------------------------------------------|--------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger carries
> LT-ID or DERIVED:rationale; every Status-Quo Gap names an FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A; or DERIVED (use only when this phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic produced this boundary): [rationale]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit pair with Entry Trigger; write FM-ID from STATUS-QUO PROCESS DECLARATION; blank is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------|-------------|---------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|-----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |
| S-04 | | | | | | | |
| S-05 | | | | | | | |
| S-06 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (threshold-type category AND quoted example with operator + unit; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Met | Branch: Not Met | Fallback |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|------------|----------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths:**

```
Fork (S-ID):    [branching state]
Branch A/B:     [concurrent paths]
Join condition: [merge requirement]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open Exception Catalog until
> State Trace and Decision Table complete. Source: Step 3 --> Target: Step 5.
> Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output]
SLA envelope:   [duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception]
Blocked by:     [C-ID(s) -- Mandatory]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) -- Must trace to Exception Handler = Y in Step 1; blank or uncertified is a structural fail | Divergence Phase/Step | Recovery or Terminal |
|------|--------------|----------------|---------|-----------------------------------------------------------------------------------------------------------|----------------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration
> until all Handler R-IDs trace to Exception Handler = Y. Uncertified or blank Handler is
> a structural fail -- discard and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From |
|------|--------------|----------------------------------|-------------|
| T-01 | | | |
| T-02 | | | |

> **Check V** -- Status: [ OPEN / CLOSED ]
> Confirm every path reaches a named T-ID. Co-equal with Coverage Scan for Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|-----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION** | **STEP 9 -- BOTTLENECK REGISTER** | **STEP 10 -- GAP REGISTER** | **STEP 11 -- CROSS-LIFECYCLE HANDOFF** | **STEP 12 -- EXCEPTION COVERAGE AUDIT**

[Same structure as V-01 Steps 8-12.]

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-01 | STEP 0A >=3 LT-IDs; all four fields per row | STEP 0A | | |
| AC-02 | STEP 0B >=3 orthogonal failure surfaces | STEP 0B | | |
| AC-21 | SQ Declaration present before STEP 0A; all four fields | SQ Declaration | | |
| AC-23 | Every SQ Declaration field cell carries inline anti-pattern token | SQ Declaration | | |
| AC-24 | FM-ID PROTOCOL present before SQ Declaration; covers all four fields; Phase Framing block precedes Protocol | FM-ID PROTOCOL | | |
| AC-25 | All four SQ Declaration field cells begin with "does not count; Mandatory" as leading clause | SQ Declaration cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers Incumbent Process and Inertia Driver with governance depth equal to FM-01/FM-02 | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token in all four SQ Declaration field cells | SQ Declaration cells | | |
| AC-28 | C-54: GATE SQ present at FM-ID PROTOCOL close; names STATUS-QUO PROCESS DECLARATION and STEP 0A; "Blocked by" field present | GATE SQ text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-04 | Role Registry domain-qualified titles, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | LT-ID Trace column header defines SECONDARY typed escape code WITH eligibility condition | Step 1 column header | | |
| AC-06 | Entry Trigger column header defines DERIVED typed escape code WITH eligibility condition | Step 2 column header | | |
| AC-07 | Exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header: backward-trace rule and fail-declaration co-located | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" | Gate D | | |
| AC-10 | Decision Condition header: category list AND quoted example | Step 3 | | |
| AC-11 | Phase exit gates: "Blocked by: [C-ID]" | Step 4 | | |
| AC-12 | Gate C and Gate D both present, source and target named | Gates C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 | | |
| AC-22 | Phase Index Status-Quo Gap mutual-audit principle named | Step 2 | | |
| AC-29 | C-55: production gate enumerates >=3 named defect categories inline; column pointer alone is D-19 | Production Gate | | |
| AC-30 | C-56: LT-ID Trace and Entry Trigger headers each carry code format AND eligibility condition; format-only is D-20 | Steps 1 + 2 headers | | |

#### Group C -- General Schema Integrity

[Same as V-01 Group C: AC-14 through AC-20.]

**Defect Type Taxonomy:** [D-01 through D-20 as in V-01]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11),
> a per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15),
> a missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17),
> selective leading-clause token distribution (D-18), a gate-defect-pointer-only gate
> sentence (D-19), or an escape-code-eligibility-absent column header (D-20) -- and
> that artifact must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-30.
> (2) Check V shows CLOSED.

---

## V-04 -- Phrasing Register: Conversational FM-ID Guidance + Role Sequence + C-55/C-56

**Variation axis:** Phrasing register (conversational) + role sequence -- two axes combined.
The FM-ID Protocol is relabeled FM-ID GUIDANCE and uses plain-language framing throughout.
The DOMAIN ROLE REGISTRY precedes all other content (role-first axis from R18 V-04).
Targeted changes from R18 V-04: (1) escape code column headers gain eligibility conditions
in plain English (C-56 TARGET); (2) production gate enumerates defect categories inline
in conversational language (C-55 TARGET).

**Hypothesis:** Conversational register is compatible with C-55 and C-56 because both
criteria are about structural content in specific locations -- not about formal/imperative
phrasing. C-55 requires the gate to name >=3 categories inline; a conversational gate
can do this without formal D-ID codes. C-56 requires column headers to carry eligibility
conditions; these can be written in plain English ("use this when...") rather than formal
notation. The test: does conversational phrasing reduce the precision of inline enumeration
or eligibility conditions enough to produce a scoring difference? Prediction: C-55 TARGET
(conversational gate enumerates categories in plain prose), C-56 TARGET (eligibility
conditions in plain-English column headers), AC-29 PASS, AC-30 PASS.

---

You are a business-process simulation expert. Your job is to walk through a complete
business lifecycle end to end. Start by listing the team members who own this process,
then read the FM-ID Guidance section before filling in the status-quo table. Follow every
numbered step in order.

---

### Start Here: Domain Role Registry

Fill in this table before you do anything else. Every role needs a specific job title --
not a generic label like "Approver" or "Finance team." The "Exception Handler?" column tells
you who is authorized to own exception flows later.

| R-ID | Job Title (specific domain title, e.g., "Senior Credit Analyst" or "AP Supervisor"; generic labels like "Approver" or "Admin" do not count) | Process Area (specific function, e.g., "Sales Operations" or "Finance -- AP"; a department name without a process qualifier does not count) | Exception Handler? (Y or N -- at least one Y is required; leave blank and the whole artifact is invalid) | Which Triggers Start This Role? (write the LT-ID(s) this role first appears in; if this role has no lifecycle trigger, write SECONDARY -- but only when role has no LT-bound trigger at all, and explain why it exists outside any trigger scope; "N/A" is not acceptable) |
|------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

You need at least 3 roles. Do not open the FM-ID Guidance until every row has a specific
job title and an Exception Handler answer.

---

### FM-ID Guidance

FM-IDs label the ways your current process fails. You will use these labels in the Phase
table downstream -- every phase needs to name which FM-ID its entry trigger is addressing.

Read these four rules before filling in the status-quo table:

- **What is your current process?** Name the specific tool, procedure, or workaround --
  not just "a manual process" or "the finance team." If you can't name it specifically, you
  haven't scoped the problem yet.
- **FM-01 -- First failure:** What specific thing does the current process fail to detect or
  prevent? Saying it's "error-prone" or "slow" is not a failure mode -- name the specific
  mechanism that is absent.
- **FM-02 -- Second failure (orthogonal):** A completely different failure from FM-01. If
  fixing FM-01 would also fix FM-02, they're not orthogonal -- write a genuinely different
  failure.
- **Why does it persist?** What specific organizational, contractual, or systemic reason
  keeps the current process in place despite FM-01 and FM-02? "We're used to it" is not an
  answer -- name the specific lock-in mechanism.

Once you have all four answers, fill in the status-quo table, then move on to Step 0A.

---

### Status-Quo Process Declaration

| Field | Your Answer |
|-------|-------------|
| does not count; Mandatory -- Current Process: name the specific tool or procedure being replaced; "manual process" without naming the tool does not count; a team name alone does not count | |
| does not count; Mandatory -- FM-01: the specific mechanism the current process fails to provide; "error-prone" or "slow" does not count; assign label FM-01 inline | |
| does not count; Mandatory -- FM-02: a second failure orthogonal to FM-01; a restatement or downstream consequence of FM-01 does not count; assign label FM-02 inline | |
| does not count; Mandatory -- Why It Persists (Inertia Driver): the specific organizational or systemic reason the current process stays in place despite FM-01 and FM-02; "familiarity" without a specific mechanism does not count | |

---

### Step 0A -- What Starts This Lifecycle?

List every external trigger that can kick off this process. "The process starts" is not a
trigger -- name the specific event, action, or condition.

| LT-ID | What triggers this? (name the specific event, role action, or time condition) | Source type (write exactly one: System Event / Role Action / Time Condition) | First state this trigger activates | First phase this trigger activates (required -- blank is a fail) |
|-------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------|------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

You need at least 3 rows. Do not move on until every row has all four fields.

---

### Step 0B -- Failure Surface Taxonomy

Before building the schema, name the structural ways this lifecycle document can go wrong.
These are schema defects, not process exceptions.

| FS-ID | What can go wrong structurally? (a schema defect category -- not a process exception; two rows naming the same defect are not orthogonal) | Which schema section does this affect? ("general" is too vague) | What criterion or gate prevents this? (required -- blank is a fail) |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

---

**Step 1 -- Role Registry Verification**

You set up roles at the start. Before opening the Phase Index, confirm they are complete.

> **Gate A**: Do not open the Phase Index until: every role has a specific job title (no
> generics), every role has an Exception Handler Y/N, every role has a trigger trace or
> SECONDARY:rationale, and at least one role has Exception Handler = Y.
> Blocked by: C-05, C-11, C-23, C-36

---

**Step 2 -- Phase Index**

> **Gate B**: Do not open the State Trace until the Phase Index is complete, every Entry
> Trigger has a trigger ID or DERIVED:rationale, and every Status-Quo Gap names an FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | What triggers this phase? (write the LT-ID from Step 0A; or if this phase boundary comes from combining multiple triggers, write DERIVED -- but only when the phase results from multiple LT-IDs combining, and explain which ones and how they combine; "N/A" is not valid) | Which FM-ID does this phase address? (write FM-01 or FM-02 from the Status-Quo table; this column and the trigger column form a mutual-audit pair -- a vague trigger will leave this cell blank, making the gap visible in a single row scan; blank is a structural fail) | What ends this phase? | How long should this take? | At-risk? | States (fill after Step 3) |
|-------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------|---------|---------------------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**Step 3 -- State Trace + Decision Points + Parallel Paths**

Minimum 6 states.

| S-ID | Phase | State Name | What enters this state? | How does it exit? | Who owns it? (R-ID) | How long? | SLA status |
|------|-------|-----------|------------------------|------------------|--------------------|-----------| ----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |
| S-04 | | | | | | | |
| S-05 | | | | | | | |
| S-06 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | What is the condition? (you need BOTH: (1) a threshold-type category from this list -- dollar amount, day count, retry count, unit quantity -- AND (2) a quoted example with an operator and unit, like "Invoice value > $10,000"; giving only the category name is a fail; giving only the example is a fail) | Who decides? (R-ID) | If condition is met | If condition is not met (do not write "otherwise") | What if the decision mechanism breaks? (name what happens if the decision owner is unavailable or the system is down -- "escalate" alone is not enough) |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel work (if any):**

```
Where does the fork happen? (S-ID):
Branch A:
Branch B:
What must be true before the branches can rejoin?
Who owns the join? (R-ID):
```

Or: "No parallel paths -- [reason]"

> **Gate C -- before exceptions**: Do not write exception flows until the state trace and
> all decision points have stable IDs. Exception flows reference state IDs -- writing them
> before states are final creates untraceable references.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**Step 4 -- Phase Exit Gates**

For each phase:

```
Phase:          [Ph-ID: name]
Exits when:     [what verifiable output or state closes it]
SLA target:     [from Step 2]
Clean exit to:  [next Ph-ID or T-ID]
Failed exit to: [T-ID or exception trigger]
Blocked by:     [C-ID -- required; blank fails the gate]
```

---

**Step 5 -- Exception Catalog**

Gate C must be closed first. Minimum 3 exceptions.

| E-ID | Phase | Exception Name | What triggers it? | Who handles it? (R-ID -- must have Exception Handler = Y in Step 1; blank or uncertified is a fail; only Y-designated roles qualify) | What states are bypassed or added? | Where does it land? (S-ID or T-ID) |
|------|-------|---------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **Gate D -- after exceptions**: Do not write terminal declarations until every exception
> handler has been verified as a Y-designated role. An uncertified handler means the artifact
> must be discarded and restarted from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**Step 6 -- Terminal States**

| T-ID | Terminal Name | Type (write exactly: success / failure / cancel) | Arrives from (list all S-IDs and E-IDs) |
|------|--------------|--------------------------------------------------|----------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V** -- Status: [ OPEN / CLOSED ]
> Go through every path -- happy path and every exception -- and confirm each one reaches
> a named terminal. Any path with no terminal is a D-01 defect. Mark CLOSED only when
> every path is individually confirmed. Check V CLOSED is required for the Production Gate.

---

**Steps 7 through 12** follow the same structure as V-01 (Edge Cases, SLA Annotation,
Bottleneck Register, Gap Register, Cross-Lifecycle Handoff, Exception Coverage Audit).

---

**Step 13 -- Coverage Check**

#### Group A -- Pre-Schema Blocks

| AC-ID | What to verify | Where to look | Result | Defect if fail |
|-------|----------------|--------------|--------|----------------|
| AC-01 | Step 0A has >=3 trigger rows; all four columns filled per row | Step 0A | | |
| AC-02 | Step 0B has >=3 orthogonal failure surfaces; all three columns filled | Step 0B | | |
| AC-03 | Role Registry appears before FM-ID Guidance; roles have job titles and Exception Handler Y/N before Status-Quo table is filled | Role Registry | | |
| AC-21 | Status-Quo table appears before Step 0A; all four fields present | Status-Quo table | | |
| AC-23 | Every Status-Quo field cell carries an inline anti-pattern token for that field | Status-Quo cells | | |
| AC-24 | FM-ID Guidance section appears before Status-Quo table; covers all four fields with "does not count" language | FM-ID Guidance | | |
| AC-25 | Every Status-Quo field cell begins with "does not count; Mandatory" as its first expression | Status-Quo cells | | |
| AC-26 | C-52: FM-ID Guidance covers Incumbent Process and Inertia Driver with same governance depth as FM-01/FM-02 | FM-ID Guidance | | |
| AC-27 | C-53: Leading-clause "does not count; Mandatory" token appears first in all four Status-Quo field cells | Status-Quo cells | | |
| AC-28 | C-54: FM-ID Guidance closes with instruction to complete Status-Quo table before moving to Step 0A | FM-ID Guidance close | | |

#### Group B -- Gate-Backed Criteria

| AC-ID | What to verify | Where | Result | Defect if fail |
|-------|----------------|-------|--------|----------------|
| AC-04 | Role Registry: specific job titles, Exception Handler Y/N, trigger trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | "Which Triggers Start This Role?" column header carries SECONDARY code format AND eligibility condition ("only when role has no LT-bound trigger") | Step 1 column header | | |
| AC-06 | Phase trigger column header carries DERIVED code format AND eligibility condition ("only when phase results from multiple LT-IDs combining") | Step 2 column header | | |
| AC-07 | All exception handlers trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" or equivalent | Gate D | | |
| AC-10 | Decision condition column carries both threshold-type category list and quoted example | Step 3 | | |
| AC-11 | Phase exit gates all carry "Blocked by: [C-ID]" | Step 4 | | |
| AC-12 | Gate C and Gate D both present with source and target named | Gates C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 + Gate | | |
| AC-22 | Phase Index Status-Quo Gap column present; mutual-audit principle named | Step 2 | | |
| AC-29 | C-55: Production gate names >=3 defect categories inline in the gate sentence itself | Production Gate | | |
| AC-30 | C-56: Trigger-trace column (Step 1) and phase-trigger column (Step 2) each carry both code format and eligibility condition | Steps 1 + 2 headers | | |

#### Group C -- Schema Integrity

[Same checks as V-01 Group C: AC-14 through AC-20.]

**Defect Types:** [D-01 through D-20 as in V-01]

> **Production Gate**: Writing this artifact while any Coverage Check row shows FAIL means
> the artifact has at least one structural problem -- an unterminated path, an uncertified
> exception handler, an unresolvable decision owner, a missing or partial status-quo
> declaration, an unanchored status-quo gap, a per-field anti-pattern gap, a trailing-
> position enforcement token, a missing FM-ID guidance section, partial guidance coverage,
> selective leading-clause distribution, a gate that only points to the defect list without
> naming any defects inline, or an escape code column that carries a format code but no
> eligibility condition -- and the artifact must be discarded and rerun from the failing
> step before it is filed or used.
>
> Both conditions must be met:
> (1) Coverage Check shows PASS for AC-01 through AC-30.
> (2) Check V shows CLOSED.

---

## V-05 -- Full Combination: Inertia-First + Column Contract + Pre-Declaration Roles + GATE SQ + C-55/C-56 Formalization

**Variation axis:** Inertia framing + output format + role sequence -- three axes combined.
Holds R18 V-05 full floor intact. Single change: Coverage Scan extended with AC-29 (C-55)
and AC-30 (C-56) explicit verification rows; Defect Type Taxonomy extended with D-19
(gate-defect-pointer-only) and D-20 (escape-code-eligibility-absent). No structural changes
to any prompt section -- the R18 V-05 production gate already enumerates defect categories
inline (C-55 HOLD/PASS) and escape code column headers already carry eligibility conditions
(C-56 HOLD/PASS).

**Hypothesis:** The R18 V-05 full floor already satisfies C-55 and C-56 through structural
choices made for other criteria (the verbose production gate text was written to be
maximally descriptive; the escape code eligibility conditions were present in column headers
to satisfy AC-05/AC-06). Explicitly formalizing AC-29/AC-30 as Coverage Scan rows and
D-19/D-20 as defect taxonomy entries closes the gap between "the artifact passes these
criteria" and "the schema explicitly verifies them as independent named criteria." This
variation serves as the full-stack stability confirmation: if AC-29 and AC-30 both PASS
when evaluated against the existing R18 V-05 structure, the formalization is score-neutral
for V-05 and the criteria are confirmed as independently satisfiable from the full-floor
baseline. Prediction: C-55 HOLD/PASS, C-56 HOLD/PASS, AC-29 PASS (stable), AC-30 PASS
(stable); no structural changes needed; full denominator 56/56 aspirational.

---

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

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one of: an unterminated path (D-01),
> an uncertified exception handler (D-02), an unresolvable decision owner (D-03), a
> missing or partial SQ Declaration (D-09/D-10), an unanchored status-quo gap (D-11), a
> per-field anti-pattern gap (D-14), a trailing-position enforcement token (D-15), a
> missing FM-ID Protocol block (D-16), partial Protocol field coverage (D-17), selective
> leading-clause token distribution (D-18), a gate-defect-pointer-only gate sentence
> (D-19), or an escape-code-eligibility-absent column header (D-20) -- and that artifact
> must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-30.
> (2) Check V shows CLOSED.

---

## Variation Discrimination Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-52 (uniform Protocol field coverage) | PASS | PASS | PASS | PASS | PASS |
| C-53 (uniform leading-clause distribution) | PASS | PASS* | PASS | PASS | PASS |
| C-54 (Protocol forward sequencing gate) | PASS | PASS | PASS+ | PASS | PASS++ |
| C-55 (gate defect inline enumeration) | TARGET | TARGET | TARGET | TARGET | HOLD/PASS |
| C-56 (escape code eligibility) | HOLD/PASS | TARGET | TARGET | TARGET | HOLD/PASS |
| Role sequence | Pre-decl | Standard | Standard | Pre-decl (conv) | Pre-decl |
| SQ Declaration format | Row | Column Contract | Row | Row | Column Contract |
| Phase framing | None | None | Pre-Protocol | None | None |
| Phrasing register | Formal | Formal | Formal | Conversational | Formal |
| Field ordering (SQ Declaration) | Standard | Standard | Standard | Standard | Inertia-first |
| GATE SQ labeled | No | No | YES | No | YES |
| AC-29 check present | YES | YES | YES | YES | YES |
| AC-30 check present | YES | YES | YES | YES | YES |
| D-19/D-20 in taxonomy | YES | YES | YES | YES | YES |

\* C-53 in V-02: token in Column Contract Field column (definition layer). Scoring will
determine if definition-layer placement satisfies the leading-clause requirement.

\+ C-54 in V-03: GATE SQ is a labeled gate node with "Blocked by" field -- an enhancement
over the bare forward sequencing sentence in V-01.

\++ C-54 in V-05: GATE SQ with "Blocked by: C-52, C-53, C-54" and inertia-first field
ordering creating four independent enforcement mechanisms.

**Single-axis C-55 probe:** V-01 tests whether inline gate enumeration is achievable in
role-first structure without any other change. Expected: PASS; no structural interaction
with role-sequence axis.

**Single-axis C-56 probe:** V-02 tests whether Column Contract format can carry escape
code eligibility conditions (column headers are the same structural element regardless
of whether the SQ Declaration uses row or Column Contract format). Expected: PASS;
eligibility conditions are column-header-scoped and format-independent.

**Combined C-55 + C-56 probe:** V-03 tests both new criteria against the phase-first
framing axis that caused Protocol degradation in R17 but was stabilized in R18. The
hypothesis is that C-55/C-56 are position-independent from the Phase Framing block
(because the gate is at the end of Step 13, and escape code headers are at Steps 1-2,
both well after the pre-protocol framing block).

**Conversational register probe:** V-04 tests whether C-55 inline enumeration can be
expressed in plain prose (without D-ID codes) and whether C-56 eligibility conditions
can be written in natural language ("use this when...") while still satisfying the
criteria. The conversational gate text ("at least one structural problem -- an unterminated
path, an uncertified exception handler...") is predicted to satisfy C-55 because the
criterion requires named categories, not formal D-ID references.

**Full-stack formalization:** V-05 confirms that R18 V-05 already satisfies C-55 and
C-56, and that adding AC-29/AC-30/D-19/D-20 is score-neutral for the full floor --
the explicit formalization neither adds nor removes passing behavior, it only names
what was already present.
