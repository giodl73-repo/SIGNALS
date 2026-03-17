---
skill: flow-lifecycle
round: 18
rubric-version: v18
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v18-2026-03-16.md
floor: flow-lifecycle-variate-R17-2026-03-16.md V-05
---

# flow-lifecycle -- Round 18 Variations (rubric v18: C-52, C-53, C-54)

Round 18 holds the R17 V-05 full floor and probes three new aspirational criteria formalized
from Round 17 scoring evidence:

- **C-52 -- Uniform Protocol Block Field Coverage**: the FM-ID PROTOCOL covers all four SQ
  Declaration fields (Incumbent Process, FM-01, FM-02, Inertia Driver) with equal specificity.
  A Protocol block that covers only failure mode fields (FM-01, FM-02) with no governance rule
  for Incumbent Process or Inertia Driver is D-17 (partial Protocol coverage) -- PARTIAL, not
  PASS. R17 V-04 was the source signal: its FM-ID NOTE covered only failure mode fields, leaving
  contextual fields unanchored at section entry.

- **C-53 -- Uniform Leading-Clause Token Distribution**: every STATUS-QUO PROCESS DECLARATION
  field definition cell begins with the "does not count; Mandatory" token as its first expression
  across all four fields. Selective application to failure mode fields only -- while contextual
  fields carry trailing tokens or plain field names -- is D-18 (selective distribution) --
  PARTIAL, not PASS. R17 V-04 was the source signal: FM-01 and FM-02 cells had leading tokens;
  Incumbent Process and Inertia Driver cells had trailing tokens.

- **C-54 -- Protocol Block Forward Sequencing Gate**: the FM-ID PROTOCOL closes with an explicit
  forward sequencing instruction naming both the section to complete (STATUS-QUO PROCESS
  DECLARATION) and the section to proceed to (STEP 0A). A downstream consequence statement
  without an explicit "Author... before proceeding to..." instruction is a fail. R17 V-05 already
  produced this gate sentence; V-04 did not. C-54 formalizes V-05's closing sentence as a
  scoreable criterion distinct from C-50 (block exists) and C-52/C-53 (field coverage and
  token distribution).

Denominator: 51 -> 54. Aspirational count: 43 -> 46.

**Variation axes explored:**

- V-01: Role sequence (pre-declaration role registry) -- single axis
- V-02: Output format (SQ Declaration as Column Contract + fill table) -- single axis
- V-03: Lifecycle emphasis (phase-first framing with named GATE SQ) -- single axis
- V-04: Phrasing register (conversational FM-ID Guidance) + role sequence -- combination
- V-05: Inertia framing + output format + role sequence -- full combination

---

## V-01 -- Role Sequence: Pre-Declaration Role Registry with Full Protocol Gate

**Variation axis:** Role sequence -- the DOMAIN ROLE REGISTRY is established before the
FM-ID PROTOCOL and STATUS-QUO PROCESS DECLARATION. All other Protocol block properties are
held at R17 V-05 floor: FM-ID PROTOCOL covers all four fields (C-52 target), all four SQ
Declaration field cells carry leading-clause tokens (C-53 target), Protocol block closes with
explicit forward sequencing gate (C-54 target). STEP 1 becomes a verification pass rather than
a creation step because the Role Registry is pre-declared.

**Hypothesis:** Role-first sequencing establishes domain-qualified vocabulary before the
Incumbent Process field is authored, reducing the probability of generic naming ("a manual
approval process") by anchoring domain-specific role titles (e.g., "Senior Credit Analyst")
in the author's working context before they encounter the SQ Declaration fields. The Protocol
block retains full four-field coverage (C-52) and gate strength (C-54) because it follows the
role registry rather than being displaced by it -- the sequencing change does not perturb the
Protocol block's structural relationship to the SQ Declaration. Leading tokens on all four
fields (C-53) are position-independent and survive the sequencing change intact. Prediction:
C-52 TARGET, C-53 TARGET, C-54 TARGET; role-first sequencing reduces D-09 (generic Incumbent
Process naming) by anchoring domain vocabulary early.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Establish the DOMAIN
ROLE REGISTRY first, then read the FM-ID PROTOCOL before filling the STATUS-QUO PROCESS
DECLARATION. Every field cell in the SQ Declaration begins with a compact enforcement token;
read the token before reading the content instruction.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Author this table completely before proceeding to FM-ID PROTOCOL.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) whose Initial State or Initial Phase this role appears in; if role exists outside all LT scopes write SECONDARY:[rationale naming why this role exists without any LT anchor]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID
> from the STATUS-QUO PROCESS DECLARATION.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale in Entry Trigger simultaneously produces an FM-ID-free gap here, making incompleteness visible as a co-occurring defect in a single row scan; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
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
> Exception flows reference state names by ID; authoring exceptions before states are finalized
> produces untraceable ID references. This gate locks Step 3 and unlocks Step 5.
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
> until all exception flows carry a certified Handler R-ID -- that is, an R-ID that traces to a
> role pre-certified as Exception Handler = Y in the Role Registry. An exception flow with an
> uncertified or blank Handler R-ID is a structural fail that blocks this gate and produces an
> artifact that must be discarded and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (must be exactly: success / failure / cancel -- "completed" does not count) | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|------------------|--------------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) reaches a named T-ID. A path with no named
> terminal is an unterminated path defect. Status is CLOSED only when every path is
> individually confirmed terminated. Check V CLOSED is a co-equal condition of the Production
> Gate alongside Coverage Scan PASS.

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
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
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
| AC-24 | A named FM-ID PROTOCOL section appears immediately before the STATUS-QUO PROCESS DECLARATION table; block covers all four fields (Incumbent Process, FM-01, FM-02, Inertia Driver) with "does not count" guidance for each; a block that covers only failure mode fields is PARTIAL, not PASS | FM-ID PROTOCOL section | | |
| AC-25 | Every STATUS-QUO PROCESS DECLARATION field definition cell begins with "does not count; Mandatory" as its first expression -- before the field name and content description; a token at the end of the description is D-15; all four fields must have leading tokens for PASS | SQ Declaration field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers all four SQ Declaration fields with equal specificity -- Incumbent Process and Inertia Driver carry "does not count" governance rules in the Protocol block with the same depth as FM-01 and FM-02; a Protocol block that enumerates failure mode governance only is D-17 | FM-ID PROTOCOL section | | |
| AC-27 | C-53: Leading-clause token ("does not count; Mandatory") appears as first expression in all four SQ Declaration field cells -- not selectively on failure mode fields only; Incumbent Process and Inertia Driver cells must begin with the token; selective application is D-18 | SQ Declaration field cells | | |
| AC-28 | C-54: FM-ID PROTOCOL closes with explicit forward sequencing instruction naming both (a) the section to complete (STATUS-QUO PROCESS DECLARATION) and (b) the section to proceed to (STEP 0A); a downstream consequence statement without this explicit gate sentence is a fail | FM-ID PROTOCOL closing text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Role Registry: each role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale (not generic N/A or blank) | Step 1 table | | |
| AC-05 | Role Registry LT-ID Trace column header defines SECONDARY typed escape code with eligibility condition | Step 1 column header | | |
| AC-06 | Phase Index Entry Trigger column header defines DERIVED typed escape code with eligibility condition | Step 2 column header | | |
| AC-07 | All exception flow Handler R-IDs trace to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration (blank or uncertified is a fail) | Step 5 column header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language -- not merely "Handler R-ID assigned" | Gate D text | | |
| AC-10 | Decision Condition column header carries BOTH: (1) named threshold-type category list AND (2) quoted example with comparison operator and unit | Step 3 D-table header | | |
| AC-11 | Each phase exit gate carries "Blocked by: [C-ID]" as a named structured field | Step 4 exit gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both present, each naming source section and target section | Gate C + Gate D text | | |
| AC-13 | Check V present with OPEN/CLOSED status field; Production Gate names Check V as co-equal condition alongside Coverage Scan PASS | Step 6 + Production Gate | | |
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names a specific FM-ID; Status-Quo Gap column header names the mutual-audit relationship as a design principle | Step 2 table | | |

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
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-03 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block present before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-14 | Per-field anti-pattern gap: SQ Declaration field row carries no inline anti-pattern token | C-48, AC-23 |
| D-15 | Trailing-position enforcement token: SQ Declaration field carries an inline token but token is at end of cell description rather than leading clause | C-51, AC-25 |
| D-16 | Missing section-entry FM-ID Protocol block: no pre-table named section establishing FM-ID enforcement before SQ Declaration | C-50, AC-24 |
| D-17 | Partial Protocol block field coverage: Protocol block present but covers only failure mode fields (FM-01, FM-02); contextual fields (Incumbent Process, Inertia Driver) absent from Protocol governance | C-52, AC-26 |
| D-18 | Selective leading-clause token distribution: leading tokens on failure mode field cells only; contextual field cells (Incumbent Process, Inertia Driver) carry trailing tokens or plain field names | C-53, AC-27 |

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above and must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-28.
> (2) Check V shows CLOSED.

---

## V-02 -- Output Format: SQ Declaration as Column Contract + Fill Table

**Variation axis:** Output format -- the STATUS-QUO PROCESS DECLARATION is restructured as a
two-part schema: a Column Contract pre-table (columns: Field | Fill Requirement | Does Not Count)
followed by a fill table (columns: SQ-Field | Content). The FM-ID PROTOCOL block precedes both
tables, covers all four fields (C-52 target), and closes with an explicit forward sequencing gate
(C-54 target). Leading-clause tokens appear in the Field column of the Column Contract -- the
field definition cell of the Column Contract is where C-53 is evaluated for this format.

**Hypothesis:** Column Contract format separates field definition (Fill Requirement + Does Not
Count) from field execution (Content cell), creating structural pre-commitment at the column
specification layer before any content is authored. C-53's leading-clause token is moved from
an inline header within the Content cell to the Field column of the Column Contract -- the
token appears at the column-definition layer, which is encountered before the fill table is
opened. This tests whether C-53's token-placement requirement survives format migration: does
"leading clause" mean leading within the field's definition cell (Column Contract Field column)
or leading within the author's fill cell (fill table Content column)? Prediction: C-52 TARGET
(all four fields in Protocol and Column Contract), C-54 TARGET (gate sentence at Protocol close),
C-53 variant (token in Column Contract Field column -- scoring will reveal whether this satisfies
the leading-clause requirement or requires the token in the fill table's SQ-Field label).

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read the FM-ID PROTOCOL
before filling the STATUS-QUO PROCESS DECLARATION. The SQ Declaration uses a two-part format:
a Column Contract defines each field, followed by a fill table. Read the Column Contract
before filling the Content column.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION Column Contract below and must appear in every Phase Index Status-Quo Gap cell
downstream.

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
| does not count; Mandatory -- FM-01 | names the specific detection or prevention mechanism the incumbent fails to provide; assign identifier FM-01 inline | "error-prone," "inefficient," "slow"; generic category without naming the missing mechanism |
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

Author this table completely before proceeding to STEP 1.

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary; "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User") do not count | Domain -- process function; org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; at least one Y required; blank is a fail | LT-ID Trace or SECONDARY:[rationale]; generic "N/A" is a fail |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]; "N/A" is a fail) | Status-Quo Gap (FM-ID from SQ Declaration; mutual-audit pair with Entry Trigger; blank is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------|-------------|---------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states. Minimum 2 states per phase.

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

**Parallel Paths** -- minimum 1 fork-join or explicit "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path name]
Branch B:       [concurrent path name]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open the Exception Catalog until
> State Trace and Decision Table are complete. Source: Step 3 --> Target: Step 5.
> Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or named exception]
Blocked by:     [C-ID(s) -- Mandatory]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) -- must trace to Exception Handler = Y in Step 1; blank or uncertified role is a structural fail | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|---------|----------------------------------------------------------------------------------------------------------------|----------------------|--------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration until
> all exception flows carry a certified Handler R-ID tracing to Exception Handler = Y.
> An uncertified or blank Handler R-ID is a structural fail -- discard and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|-------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) reaches a named T-ID. Check V CLOSED is a
> co-equal condition of the Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|-----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|----------------|---------------|-----------|
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
| AC-01 | STEP 0A present with >=3 LT-IDs; all four fields present per row | STEP 0A | | |
| AC-02 | STEP 0B present with >=3 orthogonal failure surfaces | STEP 0B | | |
| AC-21 | SQ Declaration Column Contract present with all four fields before STEP 0A | SQ Column Contract | | |
| AC-23 | Every Column Contract Field cell carries inline anti-pattern token specific to that field | SQ Column Contract Field column | | |
| AC-24 | FM-ID PROTOCOL present before SQ Declaration; covers all four fields with "does not count" guidance | FM-ID PROTOCOL | | |
| AC-25 | Every SQ Declaration field definition cell (Column Contract Field column) begins with "does not count; Mandatory" as first expression | SQ Column Contract Field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers Incumbent Process and Inertia Driver with equal governance depth as FM-01 and FM-02 | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token present as first expression in all four Column Contract Field cells | SQ Column Contract Field column | | |
| AC-28 | C-54: FM-ID PROTOCOL closes with "Author the STATUS-QUO PROCESS DECLARATION completely before proceeding to STEP 0A" | FM-ID PROTOCOL closing | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-04 | Role Registry: domain-qualified titles, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-07 | All exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition header carries category list AND quoted example | Step 3 D-table header | | |
| AC-11 | Each phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C and Gate D both present, naming source and target sections | Gate C + D | | |
| AC-13 | Check V present with OPEN/CLOSED; Production Gate names Check V as co-equal condition | Step 6 + Gate | | |
| AC-22 | Phase Index Status-Quo Gap column co-located with Entry Trigger; mutual-audit principle named | Step 2 | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 named states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exception flows with certified Handler R-ID | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths terminate | Step 6 + Check V | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decision points with measurable threshold, owner, branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff | Step 11 | | |

**Defect Type Taxonomy:** [same as V-01 above, D-01 through D-18]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail. Both conditions must be satisfied: (1) Coverage Scan PASS for AC-01
> through AC-28. (2) Check V CLOSED.

---

## V-03 -- Lifecycle Emphasis: Phase-First Framing with Named GATE SQ

**Variation axis:** Lifecycle emphasis -- a LIFECYCLE PHASE FRAMING block precedes the FM-ID
PROTOCOL, establishing the phase structure (lifecycle type, phase count, phase boundary names,
cross-lifecycle handoffs) before the SQ Declaration is authored. Unlike R17 V-04 (which had
phase-first framing but degraded the Protocol block to FM-ID NOTE covering only failure mode
fields), this variation maintains full four-field Protocol coverage (C-52 target) and leading
tokens on all four SQ Declaration fields (C-53 target). The Protocol forward sequencing gate
is labeled as GATE SQ with a "Blocked by" field (C-54 target enhanced with gate identity).

**Hypothesis:** Phase-first framing causes Protocol block degradation in R17 V-04 because the
author's attention shifts to phase alignment before encountering the SQ Declaration. This
variation tests whether the degradation is structural (caused by position) or cognitive (caused
by the absence of an explicit gate that labels the Protocol-to-SQ relationship as a named gate
node). By converting the Protocol closing sentence from an embedded prose instruction into a
named gate (GATE SQ) with a "Blocked by" field, the gate becomes visible in document scan
alongside GATE A through GATE D -- making it harder to read-past than a prose paragraph.
Prediction: C-52 TARGET, C-53 TARGET, C-54 TARGET; phase-first framing does not degrade
Protocol coverage when the forward sequencing instruction is labeled as a named gate node.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Establish the lifecycle
phase structure first, then read the FM-ID PROTOCOL before filling the STATUS-QUO PROCESS
DECLARATION. Every field cell in the SQ Declaration begins with a compact enforcement token;
read the token before reading the content instruction.

---

### LIFECYCLE PHASE FRAMING

Before authoring the SQ Declaration or trigger inventory, establish the lifecycle's phase
structure. This framing determines how FM-IDs are anchored to phases downstream.

```
Lifecycle type:    [L2O / P2P / Period Close / Case Lifecycle / other -- name the specific type]
Phase count:       [expected number of phases -- minimum 3]
Phase boundaries:  [name the expected phase transition points -- e.g.,
                   "Order Entry -> Credit Review -> Fulfillment -> Invoicing -> Collection"]
Cross-lifecycle:   [name any known handoff to a partner lifecycle -- e.g.,
                   "hands off to P2P at invoice receipt"; or "self-contained -- no cross-lifecycle"]
```

Complete this framing block before proceeding to FM-ID PROTOCOL.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION below and must appear in every Phase Index Status-Quo Gap cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround -- not a
  department and not a generic "manual" description. A single-word tool name without context
  does not count. The Incumbent Process field anchors the lifecycle type named in the Phase
  Framing above to a specific named operational reality.
- **FM-01**: must name the specific detection or prevention mechanism the incumbent fails to
  provide. "Error-prone," "inefficient," or "slow" does not count. Assign identifier FM-01
  inline. FM-01 should map to a gap visible within at least one phase named in the Phase
  Framing.
- **FM-02**: must name a second failure mode orthogonal to FM-01. A restatement, subcategory,
  or downstream consequence of FM-01 does not count. Assign identifier FM-02 inline.
- **Inertia Driver**: must name the specific organizational, systemic, or economic reason the
  incumbent persists despite FM-01 and FM-02. A reason that would apply to any legacy process
  does not count. The Inertia Driver explains why the lifecycle type named in Phase Framing
  continues to operate under the incumbent even with FM-01 and FM-02 present.

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
| does not count; Mandatory -- FM-01: first failure mode; names the specific detection or prevention mechanism the incumbent fails to provide; "error-prone," "inefficient," or "slow" does not count; a generic category name without a missing mechanism does not count; assign identifier FM-01 inline | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement, subcategory, or downstream consequence of FM-01 does not count; "same as FM-01 in a different phase" does not count; assign identifier FM-02 inline | |
| does not count; Mandatory -- Inertia Driver: names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count; a reason that would apply equally to any other legacy process does not count | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition; "process begins" does not count | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase -- Mandatory; blank is a structural fail |
|-------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------------|-------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming same category are not orthogonal | Gate Domain -- schema section; "general" does not count | Closed By (C-ID or Gate Label) -- blank is a fail |
|-------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to STEP 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified title; generic labels do not count | Domain -- process function | Exception Handler (Y/N) -- Mandatory | LT-ID Trace or SECONDARY:[rationale] |
|------|------------------------------------------------------------------|--------------------------|--------------------------------------|--------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger carries
> LT-ID or DERIVED:rationale; every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]) | Status-Quo Gap (FM-ID; mutual-audit pair with Entry Trigger; blank is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|---------------------------------------------|------------------------------------------------------------------------------|---------------------|-------------|---------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each must contain >=2 states. Phases must align with Phase Framing boundaries.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states. Minimum 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|-----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |
| S-04 | | | | | | | |
| S-05 | | | | | | | |
| S-06 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (threshold-type category AND quoted example with operator + unit) | Owner (R-ID) | Branch: Met | Branch: Not Met | Fallback |
|------|--------------|--------------------------------------------------------------------------------------|-------------|------------|----------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 or "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A/B:     [concurrent path names]
Join condition: [merge requirement]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open Exception Catalog until State
> Trace and Decision Table complete. Source: Step 3 --> Target: Step 5.
> Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output]
SLA envelope:   [duration from Step 2]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception]
Blocked by:     [C-ID(s) -- Mandatory]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y required; blank or uncertified is a structural fail) | Divergence Phase/Step | Recovery or Terminal |
|------|--------------|----------------|---------|-------------------------------------------------------------------------------------------|----------------------|--------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration until
> all Handler R-IDs trace to Exception Handler = Y. Uncertified or blank Handler is a structural
> fail -- discard and rerun from Step 5. Source: Step 5 --> Target: Step 6.
> Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From |
|------|--------------|----------------------------------|-------------|
| T-01 | | | |
| T-02 | | | |

> **Check V** -- Status: [ OPEN / CLOSED ]
> All paths must reach a named T-ID. Co-equal with Coverage Scan for Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|-----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|----------------|---------------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

| B-ID | Phase | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|-------|-----------------|-------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

| G-ID | Phase | Missing Step | Why Required | Risk if Absent |
|------|-------|-------------|-------------|---------------|
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
| AC-01 | STEP 0A present with >=3 LT-IDs; all four fields per row | STEP 0A | | |
| AC-02 | STEP 0B present with >=3 orthogonal failure surfaces | STEP 0B | | |
| AC-00 | LIFECYCLE PHASE FRAMING block present before FM-ID PROTOCOL; all four fields completed | Phase Framing block | | |
| AC-21 | SQ Declaration present before STEP 0A; all four fields named | SQ Declaration | | |
| AC-23 | Every SQ Declaration field carries inline anti-pattern token | SQ Declaration | | |
| AC-24 | FM-ID PROTOCOL present before SQ Declaration; covers all four fields | FM-ID PROTOCOL | | |
| AC-25 | All four SQ Declaration field cells begin with "does not count; Mandatory" as leading clause | SQ Declaration cells | | |
| AC-26 | C-52: FM-ID PROTOCOL covers Incumbent Process and Inertia Driver with equal governance depth as FM-01/FM-02 | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token present as first expression in all four SQ Declaration field cells | SQ Declaration cells | | |
| AC-28 | C-54: GATE SQ present at Protocol close; names SQ Declaration as section to complete and STEP 0A as section to proceed to; "Blocked by" field present | GATE SQ text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|-----------------|--------|---------------------|
| AC-04 | Role Registry: domain-qualified titles, Exception Handler Y/N, LT-ID Trace | Step 1 | | |
| AC-07 | Exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D | | |
| AC-10 | Decision Condition header: category list AND quoted example | Step 3 | | |
| AC-11 | Phase exit gates carry "Blocked by: [C-ID]" | Step 4 | | |
| AC-12 | Gate C and Gate D both present, naming source and target | Gates C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 | | |
| AC-22 | Phase Index Status-Quo Gap column co-located with Entry Trigger; mutual-audit principle named | Step 2 | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry, exit, owner | Step 3 | | |
| AC-15 | >=3 exception flows with certified handlers | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths terminate | Steps 6 + Check V | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decision points with threshold, owner, branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff | Step 11 | | |

**Defect Type Taxonomy:** [same as V-01, D-01 through D-18]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail. Both conditions: (1) Coverage Scan PASS for AC-00 through AC-28.
> (2) Check V CLOSED.

---

## V-04 -- Phrasing Register + Role Sequence: Conversational FM-ID Guidance with Imperative Gate

**Variation axis:** Phrasing register + role sequence -- the FM-ID block uses conversational
language throughout ("Before you fill in the Status-Quo table, here is what each field needs
to contain...") rather than the formal imperative register of the FM-ID PROTOCOL. The block
is renamed FM-ID GUIDANCE to signal the advisory register change. The DOMAIN ROLE REGISTRY
is established before FM-ID GUIDANCE (role sequence axis). Despite the register change, all
four fields are covered with equal depth (C-52 target), all four SQ Declaration field cells
carry leading-clause tokens (C-53 target), and the FM-ID GUIDANCE closes with an explicit
forward sequencing instruction using imperative language (C-54 target -- the gate sentence is
imperative even when surrounding prose is conversational).

**Hypothesis:** Conversational register reduces the cognitive friction of a formal compliance
block for non-expert authors, while maintaining structural coverage requirements. The renamed
"FM-ID GUIDANCE" (not "FM-ID PROTOCOL") makes the section feel advisory rather than regulatory
-- reducing the risk that an author mentally categorizes it as boilerplate and reads past it.
Role-first sequencing (combined axis) anchors vocabulary before the SQ Declaration is
encountered, complementing the register change by reducing the domain-gap that causes generic
field entries. The leading-clause tokens remain in formal register even though the Protocol
block is conversational -- the token's enforcement function is format-critical and register-
independent. Prediction: C-52 TARGET, C-53 TARGET, C-54 TARGET; conversational register and
role-first sequencing together address two independent failure modes (read-past and domain-gap).

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. To produce a high-quality lifecycle trace, start by establishing
who the key players are, then read the FM-ID GUIDANCE to understand what the Status-Quo fields
need to contain before you fill them in. Work through every numbered step in order.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Start by naming the domain experts involved in this lifecycle. You will use these role titles
throughout the trace, so establishing them first keeps the vocabulary consistent.

| R-ID | Role Name -- use a concrete functional title from the domain (e.g., "Senior Credit Analyst", "Accounts Payable Specialist"); generic titles like "Approver" or "Manager" are too vague | Domain -- the process function this role belongs to (e.g., "Sales -- Order Management", "Finance -- AP") | Exception Handler (Y/N) -- mark Y if this role would handle process exceptions; at least one Y is required | LT-ID Trace -- name the trigger(s) in STEP 0A where this role first appears; if the role appears outside all triggers, explain why with SECONDARY:[your rationale] |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Aim for at least 3 roles. Once every role has a domain-qualified title and an Exception Handler
designation, move on to FM-ID GUIDANCE.

---

### FM-ID GUIDANCE

Before you fill in the Status-Quo Process Declaration table, here is what each field needs to
contain. These definitions are important because the FM-IDs you assign here will appear in the
Phase Index later -- so precise entries here prevent gaps downstream.

Here is what each field requires:

- **Incumbent Process**: Name the actual process, tool, or workaround that is currently being
  used -- not just the team or department that runs it. Writing "a manual process" without
  naming the specific tool or procedure is too vague. A single-word tool name without any
  context about how it is used also does not give enough information.

- **FM-01**: Name the specific thing the incumbent process fails to detect or prevent -- not
  just a general quality issue. Saying the incumbent is "error-prone" or "inefficient" does
  not describe a specific failure mode. What is the concrete mechanism it is missing? Assign
  the label FM-01 directly in your answer so it can be referenced downstream.

- **FM-02**: Name a second failure mode that is genuinely different from FM-01 -- not a
  restatement, a subcategory, or a downstream consequence of the same problem. If FM-02 would
  still exist even if FM-01 were fixed, it is likely orthogonal. Assign label FM-02 inline.

- **Inertia Driver**: Name the specific organizational, economic, or systemic reason this
  incumbent process keeps being used despite FM-01 and FM-02. The reason should be specific
  to this process -- a reason like "people are used to it" applies to any legacy process and
  does not explain why this particular process persists.

A Phase Index entry with no FM-ID from this guidance will be structurally unanchored. Fill in
the STATUS-QUO PROCESS DECLARATION completely before moving to STEP 0A.

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

Fill in this table completely before moving to STEP 0B.

| LT-ID | Trigger Description -- what specific event, action, or condition starts the lifecycle; "process begins" is too vague | Trigger Source (exactly: System Event / Role Action / Time Condition) | Initial State -- what lifecycle state is first activated | Initial Phase -- which phase this trigger opens; leave no blanks |
|-------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

At least 3 rows. Move to STEP 0B once every row is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- a structural defect category (not a process exception); if two rows name the same defect, the second one does not count | Gate Domain -- the schema section where this defect can occur; "general" is too broad | Closed By -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

At least 3 rows, all orthogonal. Move to STEP 1 once complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY (Verification Pass)**

The Role Registry was established in the Pre-Declaration Pass. Verify completeness before
opening the Phase Index.

> **GATE A**: Do not open the Phase Index until: (1) every R-ID carries a domain-qualified
> title, (2) every R-ID has an Exception Handler designation (Y/N), (3) every R-ID has an
> LT-ID Trace or SECONDARY:rationale, (4) at least one R-ID has Exception Handler = Y.
> Blocked by: C-05, C-11, C-23, C-36

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete; every Entry Trigger has LT-ID
> or DERIVED:rationale; every Status-Quo Gap names an FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]; "N/A" is a fail) | Status-Quo Gap (FM-ID; mutual-audit pair with Entry Trigger; blank is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|--------------------------------------------------------------|------------------------------------------------------------------------------|---------------------|-------------|---------|-----------------|
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

| D-ID | Decision Name | Decision Condition (threshold-type category AND quoted example with operator + unit) | Owner (R-ID) | Branch: Met | Branch: Not Met | Fallback |
|------|--------------|--------------------------------------------------------------------------------------|-------------|------------|----------------|---------|
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

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open Exception Catalog until State
> Trace and Decision Table complete. Source: Step 3 --> Target: Step 5.
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

| E-ID | Phase | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y required; blank or uncertified is a structural fail) | Divergence | Recovery or Terminal |
|------|-------|---------------|---------|-------------------------------------------------------------------------------------------|-----------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration until
> all Handler R-IDs trace to Exception Handler = Y. Uncertified or blank Handler is a structural
> fail -- discard and rerun from Step 5. Source: Step 5 --> Target: Step 6.
> Blocked by: C-32, C-45.

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

| EC-ID | Edge Case | Phase | Gap Reason | Consequence |
|-------|-----------|-------|-----------|------------|
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

| B-ID | Phase | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|-------|-----------------|-------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

| G-ID | Phase | Missing Step | Why Required | Risk if Absent |
|------|-------|-------------|-------------|---------------|
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
| AC-03 | Pre-declaration Role Registry present before FM-ID GUIDANCE; domain-qualified titles and Exception Handler before SQ Declaration | Pre-declaration Registry | | |
| AC-21 | SQ Declaration present before STEP 0A; all four fields | SQ Declaration | | |
| AC-23 | Every SQ Declaration field cell carries inline anti-pattern token | SQ Declaration | | |
| AC-24 | FM-ID GUIDANCE present before SQ Declaration; covers all four fields with "does not count" language | FM-ID GUIDANCE | | |
| AC-25 | All four SQ Declaration field cells begin with "does not count; Mandatory" as leading clause | SQ Declaration cells | | |
| AC-26 | C-52: FM-ID GUIDANCE covers Incumbent Process and Inertia Driver with governance depth equal to FM-01/FM-02 | FM-ID GUIDANCE | | |
| AC-27 | C-53: Leading-clause token in all four SQ Declaration field cells | SQ Declaration cells | | |
| AC-28 | C-54: FM-ID GUIDANCE closes with "Fill in the STATUS-QUO PROCESS DECLARATION completely before moving to STEP 0A" (or equivalent explicit forward sequencing instruction) | FM-ID GUIDANCE closing | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-04 | Role Registry domain-qualified titles, Exception Handler Y/N, LT-ID Trace | Step 1 | | |
| AC-07 | Exception Handler R-IDs trace to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header: backward-trace rule and fail-declaration co-located | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" | Gate D | | |
| AC-10 | Decision Condition header: category list AND quoted example | Step 3 | | |
| AC-11 | Phase exit gates: "Blocked by: [C-ID]" present | Step 4 | | |
| AC-12 | Gate C and Gate D both present, source and target named | Gates C + D | | |
| AC-13 | Check V present; Production Gate names Check V as co-equal condition | Step 6 | | |
| AC-22 | Phase Index Status-Quo Gap mutual-audit principle named | Step 2 | | |

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

**Defect Type Taxonomy:** [same as V-01, D-01 through D-18]

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail. Both conditions: (1) Coverage Scan PASS AC-01 through AC-28.
> (2) Check V CLOSED.

---

## V-05 -- Combination: Inertia-First Field Ordering + Column Contract + Pre-Declaration Roles + GATE SQ

**Variation axis:** Inertia framing + output format + role sequence -- three axes combined.
(1) DOMAIN ROLE REGISTRY precedes all other content (role sequence axis). (2) The SQ
Declaration uses a Column Contract format with a field-type taxonomy (output format axis):
fields are grouped into CONTEXTUAL FIELDS (Inertia Driver, Incumbent Process) and FAILURE
MODE FIELDS (FM-01, FM-02), with the Inertia Driver appearing first within the contextual
group (inertia-first ordering within SQ Declaration). (3) The FM-ID PROTOCOL uses a field-type
taxonomy matching the Column Contract grouping, with equal governance depth for both groups
(C-52 target). Leading-clause tokens appear in both the Column Contract Field column and the
FM-ID PROTOCOL governing bullet for each field (C-53 dual-position target). The Protocol block
closes with GATE SQ -- a labeled gate with "Blocked by" fields (C-54 enhanced target).

**Hypothesis:** Three-axis combination achieves maximum C-52/C-53/C-54 compliance through
four independent enforcement mechanisms operating at distinct structural levels: (1) role-first
sequencing anchors vocabulary before Incumbent Process and Inertia Driver are authored, reducing
generic naming; (2) field-type taxonomy in the Protocol block makes Contextual Fields and
Failure Mode Fields visually peer groups, preventing the author from treating one group as
secondary; (3) Column Contract format creates structural pre-commitment at the column-definition
layer before fill cells are opened; (4) GATE SQ labeled gate makes the forward sequencing
instruction a named node visible in document scan alongside GATE A through GATE D, reducing
read-past probability. Inertia-first field ordering within the SQ Declaration surfaces the
organizational resistance before the technical failure modes, framing FM-01/FM-02 as
consequences of the Inertia Driver rather than independent observations. Prediction: C-52
TARGET (Protocol taxonomy achieves equal-depth coverage), C-53 TARGET (dual-position tokens),
C-54 TARGET (labeled GATE SQ with Blocked by field); inertia-first ordering increases Inertia
Driver entry quality by making it the anchor field rather than the closing field.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Establish the DOMAIN
ROLE REGISTRY first, then read the FM-ID PROTOCOL before filling the STATUS-QUO PROCESS
DECLARATION Column Contract. Every Column Contract field definition begins with a compact
enforcement token; read the token before reading the content instruction.

---

### DOMAIN ROLE REGISTRY (Pre-Declaration Pass)

Author this table completely before proceeding to FM-ID PROTOCOL.

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) whose Initial State or Initial Phase this role appears in; if role exists outside all LT scopes write SECONDARY:[rationale]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

- **Inertia Driver**: does not count if the entry would apply to any legacy process; must name
  the specific organizational, systemic, or economic reason this particular incumbent persists
  despite its failure modes. "Familiarity" or "switching costs" alone does not count without
  naming the specific mechanism (e.g., a named integration dependency, a contractual lock-in,
  a compliance regime that approved the incumbent). Assign the Inertia Driver before FM-01 and
  FM-02 -- the failure modes are symptoms of an incumbent that persists for this specific reason.

- **Incumbent Process**: does not count if it names only a department or a generic method; must
  name the specific tool, procedure, or workaround being replaced, including enough operational
  context to understand how it is used. A single-word tool name without context does not count.
  The Incumbent Process should be consistent with the Inertia Driver authored above.

**FAILURE MODE FIELDS** -- name what the incumbent fails to provide:

- **FM-01**: does not count if it describes a quality attribute ("error-prone," "slow,"
  "inefficient"); must name the specific detection or prevention mechanism the incumbent fails
  to provide. Assign identifier FM-01 inline. FM-01 should represent a failure mode that the
  Inertia Driver helps explain -- why would an organization tolerate this specific gap?

- **FM-02**: does not count if it is a restatement, subcategory, or downstream consequence of
  FM-01; must name a second orthogonal failure mode. Assign identifier FM-02 inline.

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
Fields are ordered inertia-first: Inertia Driver appears before Incumbent Process to establish
organizational context before technical failure modes are named.

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

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID
> from the STATUS-QUO PROCESS DECLARATION.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale in Entry Trigger simultaneously produces an FM-ID-free gap here, making incompleteness visible as a co-occurring defect in a single row scan; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
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
> Exception flows reference state names by ID; authoring exceptions before states are finalized
> produces untraceable ID references. This gate locks Step 3 and unlocks Step 5.
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
> until all exception flows carry a certified Handler R-ID -- that is, an R-ID that traces to a
> role pre-certified as Exception Handler = Y in the Role Registry. An exception flow with an
> uncertified or blank Handler R-ID is a structural fail that blocks this gate and produces an
> artifact that must be discarded and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (must be exactly: success / failure / cancel -- "completed" does not count) | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|------------------|--------------------------------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) reaches a named T-ID. A path with no named
> terminal is an unterminated path defect. Status is CLOSED only when every path is
> individually confirmed terminated. Check V CLOSED is a co-equal condition of the Production
> Gate alongside Coverage Scan PASS.

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
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
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

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no
cell may share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | Pre-declaration Role Registry present before FM-ID PROTOCOL; domain-qualified titles and Exception Handler designations established before SQ Declaration is authored | Pre-declaration Registry | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION Column Contract present before STEP 0A; all four fields named in inertia-first order (Inertia Driver, Incumbent Process, FM-01, FM-02) | SQ Column Contract | | |
| AC-23 | Every Column Contract Field cell carries inline anti-pattern token specific to that field's content type and field group (CONTEXTUAL / FAILURE MODE) | SQ Column Contract Field column | | |
| AC-24 | FM-ID PROTOCOL present before SQ Column Contract; covers all four fields organized into CONTEXTUAL FIELDS (Inertia Driver, Incumbent Process) and FAILURE MODE FIELDS (FM-01, FM-02) with "does not count" governance for each; a Protocol block that covers only failure mode fields is D-17 | FM-ID PROTOCOL section | | |
| AC-25 | Every Column Contract Field cell begins with "does not count; Mandatory" as its first expression -- before the field-type tag and field name; selective application to failure mode fields only is D-18 | SQ Column Contract Field cells | | |
| AC-26 | C-52: FM-ID PROTOCOL field-type taxonomy covers Inertia Driver and Incumbent Process with governance depth equal to FM-01 and FM-02; equal depth is verified by presence of "does not count" language and orthogonality or specificity constraint for each of the four fields | FM-ID PROTOCOL | | |
| AC-27 | C-53: Leading-clause token "does not count; Mandatory" present as first expression in all four Column Contract Field cells AND referenced in the FM-ID PROTOCOL governing bullet for each field; dual-position coverage | SQ Column Contract + FM-ID PROTOCOL | | |
| AC-28 | C-54: GATE SQ present at FM-ID PROTOCOL close; names STATUS-QUO PROCESS DECLARATION as section to complete and STEP 0A as section to proceed to; "Blocked by" field names C-52, C-53, C-54 | GATE SQ text | | |

#### Group B -- Gate-Backed Aspirational Criteria

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Role Registry: each role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale (not generic N/A or blank) | Step 1 table | | |
| AC-05 | Role Registry LT-ID Trace column header defines SECONDARY typed escape code with eligibility condition | Step 1 column header | | |
| AC-06 | Phase Index Entry Trigger column header defines DERIVED typed escape code with eligibility condition | Step 2 column header | | |
| AC-07 | All exception flow Handler R-IDs trace to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration (blank or uncertified is a fail) | Step 5 column header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language -- not merely "Handler R-ID assigned" | Gate D text | | |
| AC-10 | Decision Condition column header carries BOTH: (1) named threshold-type category list AND (2) quoted example with comparison operator and unit | Step 3 D-table header | | |
| AC-11 | Each phase exit gate carries "Blocked by: [C-ID]" as a named structured field | Step 4 exit gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both present, each naming source section and target section | Gate C + Gate D text | | |
| AC-13 | Check V present with OPEN/CLOSED status field; Production Gate names Check V as co-equal condition alongside Coverage Scan PASS | Step 6 + Production Gate | | |
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names a specific FM-ID; Status-Quo Gap column header names the mutual-audit relationship as a design principle | Step 2 table | | |

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

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing or partial SQ
> Declaration, an FM-ID-free failure mode, a per-field anti-pattern gap, a trailing-position
> enforcement token, a missing or partial FM-ID Protocol block with D-17 partial coverage,
> selective leading-clause token distribution D-18, a missing GATE SQ forward sequencing
> instruction, an unanchored status-quo gap, an unlabeled pre-schema block, or a generic
> escape code in a downstream trace column) -- and that artifact must be discarded and rerun
> from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-28.
> (2) Check V shows CLOSED.

---

## Variation Discrimination Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-50 (pre-table Protocol block) | PASS | PASS | PASS | PASS | PASS |
| C-51 (leading-clause token) | PASS | PASS* | PASS | PASS | PASS |
| C-52 (uniform Protocol field coverage) | TARGET | TARGET | TARGET | TARGET | TARGET |
| C-53 (uniform leading-clause distribution) | TARGET | TARGET* | TARGET | TARGET | TARGET |
| C-54 (Protocol forward sequencing gate) | TARGET | TARGET | TARGET+ | TARGET | TARGET++ |
| Role sequence | Pre-decl | Standard | Standard | Pre-decl | Pre-decl |
| SQ Declaration format | Row | Column Contract | Row | Row | Column Contract |
| Phase framing | None | None | Pre-Protocol | None | None |
| Phrasing register | Formal | Formal | Formal | Conversational | Formal |
| Field ordering (SQ Declaration) | Standard | Standard | Standard | Standard | Inertia-first |
| GATE SQ labeled | No | No | YES | No | YES |

\* C-51/C-53 in V-02: token appears in Column Contract Field column (definition layer) rather
than SQ-Field cell of fill table. Scoring will determine whether definition-layer placement
satisfies the leading-clause requirement or requires fill-table placement.

\+ C-54 in V-03: gate is labeled GATE SQ with "Blocked by" field, converting it from prose to
a named gate node. Scoring will determine whether gate labeling strengthens the criterion or
is orthogonal to it.

++ C-54 in V-05: GATE SQ labeled with "Blocked by: C-52, C-53, C-54" and positioned after
field-type taxonomy Protocol block. Scoring will determine whether self-referential "Blocked
by" fields (gate cites its own criterion) produce evidence or a circularity defect.

**V-05 is the R18 ceiling hypothesis.** It combines all three axis changes (role-first,
Column Contract, inertia-first) with labeled GATE SQ and dual-position leading tokens
(Column Contract Field column + FM-ID PROTOCOL governing bullet). V-01 through V-04 probe
each axis in isolation or in pairs to isolate which axis produces the greatest C-52/C-53/C-54
compliance gain independently.
