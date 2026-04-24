---
skill: flow-lifecycle
round: 17
rubric-version: v17
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v17-2026-03-16.md
floor: flow-lifecycle-variate-R16-2026-03-16.md V-05
---

# flow-lifecycle -- Round 17 Variations (rubric v17: C-50, C-51)

Round 17 holds the R16 V-05 full floor and probes two new aspirational criteria derived from
R16 scoring evidence:

- **C-50 -- Pre-Table FM-ID Protocol Block (Dual-Encounter Defense-in-Depth)**: A named FM-ID
  Protocol block appears before the STATUS-QUO PROCESS DECLARATION table, establishing FM-ID
  enforcement at section entry as an independent encounter point. The block names: what FM-IDs
  are, that they are mandatory in the Phase Index Status-Quo Gap column downstream, and what
  "does not count" for failure mode entries. This creates two independent enforcement encounters:
  the Protocol block (section entry) and the field cell inline token (cell fill time). D-14
  (per-field anti-pattern gap) is not the only failure mode; D-16 (missing section-entry block)
  is now tracked separately. A prompt that carries per-field inline tokens without a pre-table
  block satisfies C-48 but fails C-50: the defense relies on a single encounter point, which
  can be bypassed if the author stops reading after the section header.

- **C-51 -- Leading-Clause Enforcement Token (Truncation-Safe Placement)**: Every field
  definition cell in the STATUS-QUO PROCESS DECLARATION table begins with a compact two-clause
  qualifying token ("does not count; Mandatory") as its first expression -- before the field
  name and before the content description. The token cannot be scrolled past or hidden by column
  truncation because it is the first thing a practitioner reads in the cell. A field cell that
  places enforcement vocabulary at the end of a long description satisfies C-48 (token present)
  but fails C-51 (token not in leading position): trailing-position tokens are at risk from
  display truncation and read-past in wide tables.

**Invariants across all five variations**: All variations carry the complete R16 V-05 floor:
C-27 (scan defect taxonomy with named Defect Type column), C-28 (Handler column co-locates
backward-trace authority and fail-declaration), C-29/C-31 (dual-mechanism Decision Condition
column header), C-30/C-32 (bidirectional exception-catalog gates), C-33 (Step 0 LT inventory),
C-34 (failure surface taxonomy), C-35 (non-overlapping evidence mandate), C-36 (LT-ID trace
cascade), C-42 (STEP 0A / STEP 0B sequential labeling), C-43 (Initial Phase field in LT
records), C-44 (typed SECONDARY/DERIVED escape codes), C-45 (Gate D uses "certified Handler
R-ID" language), C-46 (STATUS-QUO PROCESS DECLARATION with FM-IDs and Inertia Driver before
STEP 0A), C-47 (Phase Index Status-Quo Gap co-located with Entry Trigger; each row names FM-ID),
C-48 (every SQ Declaration field row carries inline anti-pattern token specific to that field),
C-49 (Status-Quo Gap column header names mutual-audit relationship as DESIGN PRINCIPLE).

**R17 failure modes to probe:**

| Mode | Criterion | What R16 V-05 does | What v17 requires |
|------|-----------|-------------------|------------------|
| Single-encounter FM-ID enforcement | C-50 | Per-field tokens in SQ Declaration field cells; no pre-table Protocol block | Named FM-ID Protocol block before the table creating section-entry encounter independent of field cells |
| Trailing-position enforcement token | C-51 | Inline tokens present but positioned at end of field descriptions | Token is the first expression in the cell: "does not count; Mandatory -- [field name]: [description]" |
| Preamble-block displacement (D-16) | C-50 | Field-level tokens present; section-entry block absent | Pre-table block must exist even if field-level tokens are present; each defense layer must be independent |
| Read-past truncation (D-15) | C-51 | Token buried after a long field description; visible in full-width display but truncated in narrow columns | Leading-position token is always visible regardless of column width because it is the first content in the cell |

**Round 17 hypothesis matrix:**

| Variation | C-50 (Pre-Table Protocol Block) | C-51 (Leading-Clause Token) | Axis |
|-----------|:-------------------------------:|:----------------------------:|------|
| V-01 | HOLD | TARGET | Output Format: leading-token truncation-safe placement |
| V-02 | TARGET | HOLD | Inertia Framing: pre-table section-entry Protocol block |
| V-03 | FAIL | PARTIAL | Phrasing Register: descriptive register dissolves enforcement structure |
| V-04 | PARTIAL | PARTIAL | Role Sequence + Lifecycle Emphasis: phase-first framing dilutes SQ block |
| V-05 | TARGET | TARGET | Inertia Framing + Output Format: full dual-encounter defense-in-depth |

---

## V-01 -- Output Format: Leading-Clause Enforcement Tokens in SQ Declaration Fields

**Variation axis:** Output format -- every STATUS-QUO PROCESS DECLARATION field cell starts
with "does not count; Mandatory" as a compact two-clause leading qualifier before the field
name and content description. The enforcement token is the first expression the practitioner
reads regardless of column display width; trailing truncation cannot hide it. C-50 is held at
the R16 floor (no pre-table Protocol block -- field-cell tokens are the single enforcement
layer, satisfying C-48 but not creating a second section-entry encounter). The C-51 probe is
the leading-position token format change: "does not count; Mandatory -- [Field]: [description]"
replaces the previous "[Field] -- [description]; does not count" pattern.

**Hypothesis:** C-51 fails when a practitioner filling a narrow-column table encounters the
field name first, reads the content description, and begins filling the cell before reaching
the trailing "does not count" token -- which may be truncated or scrolled out of view. Leading-
clause placement reverses the parse order: the qualification appears before any content
instruction, making the constraint structurally prior to the task. Prediction: leading-clause
format eliminates D-15 (trailing-position token) without requiring a pre-table Protocol block
(D-16 remains open because C-50 is held at floor level). R17 V-01 ceiling probes whether
the token position change alone is sufficient to close D-15 while leaving D-16 visible as a
distinct failure mode requiring C-50.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Every field definition
cell begins with its enforcement token; read the token before reading the content instruction.

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs defined here are required fields in the Phase Index
Status-Quo Gap column. A Phase Index cell with no FM-ID from this block is structurally
unanchored and is a fail.

| SQ-Field | Content |
|----------|---------|
| does not count; Mandatory -- Incumbent Process: names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department or team alone does not count; a single-word tool name without context does not count | |
| does not count; Mandatory -- FM-01: first failure mode; names the specific condition or detection gap the incumbent fails to prevent; "error-prone," "inefficient," or "slow" does not count; a generic category name without a missing mechanism does not count; assign identifier FM-01 inline | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement, subcategory, or downstream consequence of FM-01 does not count; "same as FM-01 in a different phase" does not count; assign identifier FM-02 inline | |
| does not count; Mandatory -- Inertia Driver: names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count; a reason that would apply equally to every other legacy process does not count | |

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

Author this table completely before proceeding to Step 1.

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary; "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. All failure surfaces must be orthogonal.

> Do not proceed to Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase this role appears; if role exists outside all LT scopes write SECONDARY:[rationale naming why this role exists without any LT anchor]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID
> from the STATUS-QUO PROCESS DECLARATION.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale in Entry Trigger simultaneously exposes an FM-ID-free gap here, making incompleteness visible in a single row scan; this mutual exposure is intentional architecture, not coincidental column placement; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
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
> until all exception flows carry a **certified Handler R-ID** -- that is, an R-ID that traces
> to a role pre-certified as Exception Handler = Y in the Role Registry. An exception flow
> with an uncertified or blank Handler R-ID is a structural fail that blocks this gate and
> produces an artifact that must be discarded and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (must be exactly: success / failure / cancel -- "completed" does not count) | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
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
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration -- specific (e.g., "5 business days"); "timely" does not count | At-Risk? (Y/N) | Risk Cause -- names the bottleneck |
|--------|--------------|--------------------------------------------------------------------------------|----------------|------------------------------------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause (if Y: name the bottleneck or E-ID; "delays" alone is a fail) |
|-------|--------------|----------------------|--------------|---------------------------------------------------------------------|
| BV-01 | | | | |

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

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no
cell may share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header labeled "STEP 0A"; STEP 0B section header labeled "STEP 0B"; STEP 0A precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; block names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration block | | |
| AC-23 | Every field row in the STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token ("does not count," "Mandatory," or "is a fail") specific to that field's content type | SQ Declaration field definitions | | |
| AC-25 | Every STATUS-QUO PROCESS DECLARATION field definition cell begins with a compact two-clause qualifying token ("does not count; Mandatory") as its first expression -- before the field name and content description; a token positioned at the end of a field description does not satisfy this check | SQ Declaration field leading clauses | | |

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
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names a specific FM-ID; Status-Quo Gap column header names the mutual-audit relationship AS A DESIGN PRINCIPLE ("mutual-audit design principle" or equivalent) | Step 2 table | | |

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
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose description without FM-ID, or cell is blank | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index: Entry Trigger column carries DERIVED:rationale; no co-located Status-Quo Gap column | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index: Status-Quo Gap column present; Entry Trigger does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |
| D-14 | Per-field anti-pattern gap: SQ Declaration field row present but carries no inline anti-pattern token ("does not count," "Mandatory," or "is a fail") | C-48, AC-23 |
| D-15 | Trailing-position enforcement token: SQ Declaration field carries an inline token but the token is positioned at the end of the cell description rather than as the leading clause -- the qualifying vocabulary can be hidden by column truncation or read-past in wide display | C-51, AC-25 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, a per-field anti-pattern gap, a trailing-position enforcement token
> that risks display truncation, an unanchored status-quo gap, a DERIVED-only or gap-column-only
> Phase Index, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape
> code) -- and that artifact must be discarded and rerun from the failing step before it is
> filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-25.
> (2) Check V shows CLOSED.

---

## V-02 -- Inertia Framing: Pre-Table FM-ID Protocol Block Creates Section-Entry Encounter Point

**Variation axis:** Inertia framing -- a named FM-ID PROTOCOL section appears immediately
before the STATUS-QUO PROCESS DECLARATION table, establishing the FM-ID enforcement contract
at section entry as an independent encounter point. The Protocol block names: what FM-IDs are,
that they must appear in the Phase Index Status-Quo Gap column downstream, and what "does not
count" for failure mode and incumbent process entries. The field cells in the SQ Declaration
table carry their existing inline tokens (C-48 floor) but in the traditional trailing position
("FM-01 -- first failure mode: ... does not count" rather than "does not count; Mandatory --
FM-01: ..."). C-51 is held at the R16 floor: tokens are present per-field but not in the
leading position. The C-50 probe is the pre-table Protocol block as a standalone named section
before the table.

**Hypothesis:** D-14 (per-field anti-pattern gap) is not the only failure mode for the SQ
Declaration; D-16 (missing section-entry block) is a distinct gap because a practitioner who
stops reading after a section header never reaches the field-cell tokens. The pre-table Protocol
block intercepts this path: even if the author skims the section header and begins filling cells,
the Protocol block forces a structural encounter before the first field row is reached. The
prediction: dual-encounter architecture (block + cell) reduces SQ Declaration errors more than
cell-only enforcement (C-48 alone), because the block provides the conceptual frame that makes
the cell tokens comprehensible rather than rote.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read the FM-ID PROTOCOL
before filling the STATUS-QUO PROCESS DECLARATION table.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers assigned in this block. They serve two functions:
(1) they classify the incumbent process's specific failure modes with traceable identifiers,
and (2) they are required fields in the Phase Index Status-Quo Gap column -- every Phase Index
row must name an FM-ID from this block in its Status-Quo Gap cell. A Phase Index row with no
FM-ID reference is structurally unanchored.

Failure mode entries must name specific detection or prevention mechanism failures. "Error-prone,"
"inefficient," or "slow" does not count. A failure mode that is a restatement or consequence
of another failure mode does not count -- FM-01 and FM-02 must be orthogonal.

The Incumbent Process field must name the specific named process, tool, or workaround being
replaced. "Manual process" without naming the specific tool does not count. A department name
without a process name does not count.

The Inertia Driver field must name the specific organizational, systemic, or economic reason
the incumbent persists despite its failure modes. A reason that would apply to any legacy
process does not count.

Author the STATUS-QUO PROCESS DECLARATION table completely before proceeding to STEP 0A.

---

### STATUS-QUO PROCESS DECLARATION

| SQ-Field | Content |
|----------|---------|
| Incumbent Process -- names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department or team alone does not count | |
| FM-01 -- first failure mode: names the specific condition or gap the incumbent fails to detect or prevent; "error-prone," "inefficient," or "slow" does not count; a generic category name without a missing detection or prevention mechanism does not count; must carry the identifier FM-01 | |
| FM-02 -- second failure mode: must be orthogonal to FM-01; a failure mode that is a restatement, subcategory, or consequence of FM-01 is a fail; must carry the identifier FM-02; "same as FM-01 in a different phase" is a fail | |
| Inertia Driver -- names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count; Mandatory | |

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

Author this table completely before proceeding to Step 1.

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary; "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows.

> Do not proceed to Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User") do not count | Domain -- process function; org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; at least one Y required; blank is a fail | LT-ID Trace -- LT-ID(s) from STEP 0A in whose Initial State or Initial Phase this role appears; if outside all LT scopes write SECONDARY:[rationale]; "N/A" or blank is a fail |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID
> from the STATUS-QUO PROCESS DECLARATION.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale simultaneously exposes an FM-ID-free gap here, making incompleteness visible as a co-occurring defect in a single row scan; this mutual exposure is intentional architecture, not incidental column placement; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration; "as soon as possible" does not count | SLA Risk -- breach condition + causal bottleneck; at least one phase AT-RISK | States Contained |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEPS 3-12** -- Same structure as V-01: STATE TRACE + DECISION TABLE + PARALLEL PATHS,
PHASE EXIT GATES, EXCEPTION CATALOG (Gate C upstream, Gate D downstream with "certified
Handler R-ID" language), TERMINAL DECLARATION (Check V), EDGE CASE CATALOG, SLA ANNOTATION,
BOTTLENECK REGISTER, GAP REGISTER, CROSS-LIFECYCLE HANDOFF, EXCEPTION COVERAGE AUDIT.
All column headers and field rules identical to V-01 Steps 3-12.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A: >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B: >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header precedes STEP 0B section header in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A with Incumbent Process, FM-01 (identifier), FM-02 (identifier), Inertia Driver | SQ Declaration block | | |
| AC-23 | Every field row in STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token specific to that field's content type | SQ Declaration field definitions | | |
| AC-24 | A named FM-ID PROTOCOL section appears immediately before the STATUS-QUO PROCESS DECLARATION table and establishes at minimum: FM-ID definition, downstream mandate (Phase Index Status-Quo Gap), and "does not count" guidance for failure mode entries; the block must be a standalone section before the table -- a preamble sentence does not satisfy this check | FM-ID PROTOCOL section | | |

#### Group B + C -- Same checks as V-01 (AC-04 through AC-22), plus AC-25 replaced by: AC-24 above

**Defect Type Taxonomy** -- same as V-01 plus:

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-16 | Missing section-entry FM-ID Protocol block: no pre-table block establishing FM-ID enforcement before the STATUS-QUO PROCESS DECLARATION table; enforcement relies on field-cell tokens only, with no independent section-entry encounter point | C-50, AC-24 |

*(D-01 through D-15 identical to V-01)*

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (including a missing section-entry FM-ID Protocol block, which means the SQ Declaration
> relies on a single encounter layer and D-14 gaps can emerge when an author reads only the
> section header) -- and that artifact must be discarded and rerun from the failing step.
>
> Both conditions required:
> (1) Coverage Scan shows PASS for AC-01 through AC-24.
> (2) Check V shows CLOSED.

---

## V-03 -- Phrasing Register: Descriptive Register Dissolves Enforcement Structure

**Variation axis:** Phrasing register -- the STATUS-QUO PROCESS DECLARATION is authored in
instructional/descriptive prose rather than imperative enforcement grammar. "You should describe
the incumbent process and identify two failure modes" replaces "does not count; Mandatory."
Anti-pattern vocabulary appears in parenthetical commentary within field descriptions rather
than as standalone inline tokens. C-50 fails because no pre-table Protocol block exists. C-51
fails because no field cell begins with a compact two-clause leading qualifier -- enforcement
tokens, where present, are embedded mid-sentence or parenthetically at the end of descriptions.

**Hypothesis:** Descriptive phrasing ("you should name a specific failure mode") produces
lower practitioner compliance than enforcement phrasing ("'error-prone' does not count") because
descriptive instructions require the practitioner to infer the negative constraint, whereas
enforcement tokens name it directly. When enforcement vocabulary is dissolved into prose, the
practitioner reads content instructions rather than fail conditions; the fail condition is only
discoverable by reconstructing what the positive instruction excludes. Prediction: C-48 partial
PASS (tokens present but not systematically per-field), C-50 FAIL, C-51 FAIL. This variation
documents the failure mode that C-50 and C-51 were designed to prevent.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Use the field
descriptions below as guidance for what content to include.

---

### STATUS-QUO PROCESS DECLARATION

Before beginning the lifecycle trace, describe the process or system currently in use and
identify its key failure modes. This section establishes the baseline against which the
new lifecycle design is measured.

| Field | Content |
|-------|---------|
| Incumbent Process -- you should name the specific process or tool currently in use. Try to be specific about what tool or workflow is being replaced rather than naming only the department or describing it as "manual." | |
| Failure Mode 1 -- identify the first significant way the incumbent process fails. You should go beyond saying it is "error-prone" or "slow" and instead describe a specific gap or missing capability. Label this FM-01. | |
| Failure Mode 2 -- identify a second failure mode that is different from the first. Try to name a gap that the first failure mode does not already cover. Label this FM-02. | |
| Inertia Driver -- explain why the incumbent process persists despite these failure modes. Consider organizational, economic, or systemic reasons. | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Enumerate the ways this lifecycle can begin. For each trigger, identify what kind of event
starts it, what initial state it activates, and what phase that corresponds to.

| LT-ID | Trigger Description | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase |
|-------|--------------------|------------------------------------------------------------|---------------|---------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Complete at least 3 rows before moving to STEP 0B.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Identify the structural defect categories that the schema is designed to prevent.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|----------------|-------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Complete at least 3 rows before moving to Step 1. Make sure each failure surface represents
a different type of defect.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Complete the Role Registry before opening the Phase Index. Each role should have
> a specific domain-qualified title, an Exception Handler designation, and a reference to the
> lifecycle trigger(s) it serves.

| R-ID | Role Name | Domain | Exception Handler (Y/N) | LT-ID Trace or SECONDARY:rationale |
|------|-----------|--------|-------------------------|-------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Complete the Phase Index before opening the State Trace.

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:rationale) | Status-Quo Gap (reference which FM-ID from the STATUS-QUO PROCESS DECLARATION this phase addresses -- the Entry Trigger and this field should reference compatible information, since a trigger that addresses a known failure mode should be traceable to its corresponding FM-ID) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|--------------|----------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**STEPS 3-12** -- Same schema structure as V-01 for STATE TRACE, DECISION TABLE, PARALLEL
PATHS, PHASE EXIT GATES, EXCEPTION CATALOG (with Gate C and Gate D), TERMINAL DECLARATION
(Check V), EDGE CASE CATALOG, SLA ANNOTATION, BOTTLENECK REGISTER, GAP REGISTER,
CROSS-LIFECYCLE HANDOFF, and EXCEPTION COVERAGE AUDIT. Decision Condition column carries
dual-mechanism threshold header (category list + quoted example) per R16 floor.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A: >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B: >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A with Incumbent Process, FM-01 (identifier), FM-02 (identifier), Inertia Driver | SQ Declaration | | |
| AC-23 | Every field row in STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token; note: parenthetical guidance embedded in a prose description does not satisfy this check if the token is not discrete and cell-adjacent | SQ Declaration field rows | | |
| AC-24 | Named FM-ID Protocol section present before the SQ Declaration table | Pre-table section | | |
| AC-25 | Every SQ Declaration field cell begins with a compact two-clause qualifying token ("does not count; Mandatory") as its first expression | SQ Declaration leading clauses | | |

#### Group B + C -- Same as V-01

**Defect Type Taxonomy** -- includes D-01 through D-16 from V-01/V-02 plus:

*(No new defect types in V-03; D-14, D-15, D-16 are the expected failures in this variation)*

---

> **PRODUCTION GATE**: Same conditions as V-01. Note that AC-23 (C-48 check) scores PARTIAL
> in this variation because descriptive parenthetical guidance does not carry discrete inline
> tokens; AC-24 (C-50 check) fails because no pre-table Protocol block exists; AC-25 (C-51
> check) fails because no field cell has a leading-clause token. All three defects must be
> resolved before artifact is filed.

---

## V-04 -- Role Sequence + Lifecycle Emphasis: Phase-First Framing Dilutes SQ Block

**Variation axis:** Role sequence + lifecycle emphasis -- a Phase Framing section appears
before the STATUS-QUO PROCESS DECLARATION, establishing the lifecycle's phase structure as the
organizing frame. The SQ Declaration follows this phase framing. An FM-ID Protocol note is
present but covers only the failure mode fields (partial C-50: block exists but does not cover
Incumbent Process or Inertia Driver fields). Field cells carry leading-clause tokens on failure
mode fields but trailing-position tokens on the Incumbent Process and Inertia Driver fields
(partial C-51: some cells have leading tokens, others do not). C-48 is fully satisfied (all
fields carry some form of inline token). C-49 is satisfied (mutual-audit design principle named
in Phase Index).

**Hypothesis:** Phase-first framing that introduces the lifecycle phase structure before the
SQ Declaration produces a partial Protocol block because the author's attention is on phase
alignment, not FM-ID enumeration. The FM-ID note becomes a secondary concern appended after
the phase context is established. Similarly, leading-clause token application is inconsistent:
fields that the author thinks of as "critical" (failure modes) get leading tokens; fields
perceived as contextual (Incumbent Process, Inertia Driver) get trailing tokens. Prediction:
C-50 PARTIAL (block present but incomplete coverage), C-51 PARTIAL (some but not all fields),
with the discrimination visible in the Coverage Scan AC-24/AC-25 rows.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order.

---

### LIFECYCLE PHASE FRAMING

Before authoring the Status-Quo Declaration or trigger inventory, establish the lifecycle's
phase structure at a high level. This framing will guide how FM-IDs are assigned to phases.

```
Lifecycle type:   [L2O / P2P / Period Close / Case Lifecycle / other -- name the specific type]
Phase count:      [expected number of phases -- minimum 3]
Phase boundaries: [name the expected phase transition points -- e.g., "Order entry -> Credit
                   review -> Fulfillment -> Invoicing -> Collection"]
Cross-lifecycle:  [name any known handoff to a partner lifecycle -- e.g., "hands off to P2P
                   at invoice receipt"]
```

Complete this framing block before proceeding to the Status-Quo Declaration.

---

### FM-ID NOTE

FM-01 and FM-02 are mandatory failure mode identifiers. They must appear in the Phase Index
Status-Quo Gap column. "Error-prone" and "inefficient" do not count as failure mode entries.

---

### STATUS-QUO PROCESS DECLARATION

| SQ-Field | Content |
|----------|---------|
| Incumbent Process -- names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; a department name alone does not count | |
| does not count; Mandatory -- FM-01: first failure mode; names the specific detection or prevention mechanism the incumbent fails to provide; "error-prone" or "slow" does not count; assign identifier FM-01 | |
| does not count; Mandatory -- FM-02: second failure mode orthogonal to FM-01; a restatement or consequence of FM-01 does not count; assign identifier FM-02 | |
| Inertia Driver -- names the specific organizational or economic reason the incumbent persists despite FM-01 and FM-02; generic reasons that would apply to any legacy process do not count; Mandatory | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

| LT-ID | Trigger Description -- names the external event, role action, or time condition; "process begins" does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition) | Initial State -- first state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary activated; Mandatory; blank is a fail |
|-------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

> Do not proceed to STEP 0B until STEP 0A is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; same category twice is a fail | Gate Domain -- schema section; "general" does not count | Closed By -- specific criterion or gate; blank is a fail |
|-------|-----------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not proceed to Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until Role Registry complete with domain-qualified
> titles, Exception Handler designations, and LT-ID Traces or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified (e.g., "Senior Credit Analyst"); generic labels do not count | Domain -- process function; org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; at least one Y required | LT-ID Trace -- LT-ID(s) this role serves; if outside LT scope write SECONDARY:[rationale]; blank is a fail |
|------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open State Trace until Phase Index complete with LT-ID/DERIVED traces and
> FM-ID references in every Status-Quo Gap cell.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]; "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: this column and Entry Trigger are co-designed as a mutual-audit pair; an imprecise DERIVED:rationale simultaneously produces an FM-ID-free gap here, making both gaps visible in a single row scan; this co-exposure is intentional architectural design; write FM-ID from STATUS-QUO PROCESS DECLARATION; blank or FM-ID-free is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|--------------|----------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**STEPS 3-12** -- Same structure as V-01.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A: >=3 LT-IDs with all four fields | STEP 0A table | | |
| AC-02 | STEP 0B: >=3 failure surfaces with all three fields | STEP 0B table | | |
| AC-03 | STEP 0A precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A with all four fields | SQ Declaration | | |
| AC-23 | Every SQ Declaration field row carries at least one inline anti-pattern token specific to that field | SQ Declaration | | |
| AC-24 | Named Protocol section (FM-ID NOTE or equivalent) appears before the SQ Declaration table AND covers failure mode fields AND covers Incumbent Process and Inertia Driver; a note that covers only failure mode fields is PARTIAL, not PASS | Pre-table section | | |
| AC-25 | Every SQ Declaration field cell begins with a compact two-clause token as its first expression; cells where the token appears trailing rather than leading are a PARTIAL; all four fields must have leading tokens for PASS | SQ Declaration field cells | | |

#### Group B + C -- Same as V-01 (AC-04 through AC-22)

---

> **PRODUCTION GATE**: Same conditions as V-01. Note that AC-24 scores PARTIAL (FM-ID NOTE
> covers failure modes only, not all fields) and AC-25 scores PARTIAL (two fields have leading
> tokens, two have trailing tokens). PARTIAL scores do not satisfy the Production Gate -- both
> must reach full PASS status before the artifact is filed.

---

## V-05 -- Inertia Framing + Output Format: Full Dual-Encounter Defense-in-Depth

**Variation axis:** Inertia framing + output format -- both C-50 and C-51 are fully implemented.
A named FM-ID PROTOCOL section appears before the STATUS-QUO PROCESS DECLARATION table (C-50:
section-entry encounter point). Every field cell in the SQ Declaration begins with a compact
two-clause "does not count; Mandatory" token as its leading clause (C-51: cell-level encounter
point). The two layers are independent: an author who reads only the Protocol block and skips
to cell fill encounters the token again at the leading clause; an author who skips the Protocol
block and reads only the cell encounters the token at the first expression in the field name.
D-14 (per-field gap) and D-15 (trailing-position token) and D-16 (missing Protocol block) are
all structurally blocked simultaneously.

**Hypothesis:** Dual-encounter architecture closes both single-encounter failure modes (D-15
from trailing token and D-16 from missing block) because it creates two structurally independent
enforcement points. The two points cannot both be missed unless the practitioner skips both
the Protocol block and the leading clause of every field cell simultaneously -- a scenario
requiring active effort rather than passive read-past. The combination is defense-in-depth for
the SQ Declaration: the Protocol block establishes the conceptual contract at section entry,
and the leading-clause token enforces it at the exact moment the practitioner decides what to
write in each field. Prediction: C-50 TARGET, C-51 TARGET, AC-24 PASS, AC-25 PASS, D-14/D-15/
D-16 all structurally closed.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read the FM-ID PROTOCOL
before filling the STATUS-QUO PROCESS DECLARATION table. Every field cell in the SQ Declaration
begins with a compact enforcement token; read the token before reading the content instruction.

---

### FM-ID PROTOCOL

FM-IDs are mandatory structural identifiers. They are defined in the STATUS-QUO PROCESS
DECLARATION below and must appear in every Phase Index Status-Quo Gap cell downstream.

This protocol governs all four fields in the SQ Declaration:

- **Incumbent Process**: must name a specific named process, tool, or workaround -- not a
  department and not a generic "manual" description. A single-word tool name without context
  does not count.
- **FM-01 and FM-02**: each must name a specific detection or prevention mechanism the
  incumbent fails to provide. "Error-prone," "inefficient," or "slow" does not count. FM-01
  and FM-02 must be orthogonal -- a failure mode that is a restatement, subcategory, or
  consequence of the other does not count.
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

Author this table completely before proceeding to Step 1.

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary; "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. All failure surfaces must be orthogonal.

> Do not proceed to Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows and may appear as Handler R-ID in Step 5; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase this role appears; if role exists outside all LT scopes write SECONDARY:[rationale naming why this role exists without any LT anchor]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID
> from the STATUS-QUO PROCESS DECLARATION.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: Entry Trigger and this column are co-designed as a mutual-audit pair -- an imprecise DERIVED:rationale in Entry Trigger simultaneously produces an FM-ID-free gap here, making incompleteness visible as a co-occurring defect in a single row scan; this mutual exposure is the design intent behind the column co-location, not a coincidence; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
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
> until all exception flows carry a **certified Handler R-ID** -- that is, an R-ID that traces
> to a role pre-certified as Exception Handler = Y in the Role Registry. An exception flow
> with an uncertified or blank Handler R-ID is a structural fail that blocks this gate and
> produces an artifact that must be discarded and rerun from Step 5.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED before this step is opened. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (must be exactly: success / failure / cancel -- "completed" does not count) | Reached From -- list all S-IDs and E-IDs that arrive here; blank is a structural fail |
|------|--------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
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
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration -- specific (e.g., "5 business days"); "timely" does not count | At-Risk? (Y/N) | Risk Cause -- names the bottleneck |
|--------|--------------|--------------------------------------------------------------------------------|----------------|------------------------------------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause (if Y: name the bottleneck or E-ID; "delays" alone is a fail) |
|-------|--------------|----------------------|--------------|---------------------------------------------------------------------|
| BV-01 | | | | |

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

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no
cell may share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header labeled "STEP 0A"; STEP 0B section header labeled "STEP 0B"; STEP 0A precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; block names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration block | | |
| AC-23 | Every field row in STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token specific to that field's content type | SQ Declaration field definitions | | |
| AC-24 | A named FM-ID PROTOCOL section appears immediately before the STATUS-QUO PROCESS DECLARATION table; block covers all four fields (Incumbent Process, FM-01, FM-02, Inertia Driver) with "does not count" guidance for each; a block that covers only failure mode fields is PARTIAL, not PASS | FM-ID PROTOCOL section | | |
| AC-25 | Every STATUS-QUO PROCESS DECLARATION field definition cell begins with "does not count; Mandatory" as its first expression -- before the field name and content description; a token at the end of the description is D-15; all four fields must have leading tokens for PASS | SQ Declaration field cells | | |

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
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names a specific FM-ID; Status-Quo Gap column header names the mutual-audit relationship AS A DESIGN PRINCIPLE | Step 2 table | | |

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
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose description without FM-ID, or cell is blank | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index: Entry Trigger column carries DERIVED:rationale; no co-located Status-Quo Gap column | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index: Status-Quo Gap column present; Entry Trigger does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |
| D-14 | Per-field anti-pattern gap: SQ Declaration field row present but carries no inline anti-pattern token ("does not count," "Mandatory," or "is a fail") | C-48, AC-23 |
| D-15 | Trailing-position enforcement token: SQ Declaration field carries an inline token but the token is positioned at the end of the cell description rather than as the leading clause -- the qualifying vocabulary can be hidden by column truncation or read-past in wide display | C-51, AC-25 |
| D-16 | Missing section-entry FM-ID Protocol block: no pre-table named section establishing FM-ID enforcement before the STATUS-QUO PROCESS DECLARATION table; enforcement relies on field-cell tokens only, with no independent section-entry encounter point | C-50, AC-24 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, a per-field anti-pattern gap, a trailing-position enforcement token
> that risks display truncation, a missing FM-ID Protocol block that leaves the SQ Declaration
> without a section-entry encounter point, an unanchored status-quo gap, a DERIVED-only or
> gap-column-only Phase Index, a missing Initial Phase field, unlabeled pre-schema blocks, or
> a generic escape code in a downstream trace column) -- and that artifact must be discarded
> and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-25.
> (2) Check V shows CLOSED.

---

## Variation Discrimination Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-48 (per-field inline tokens) | PASS | PASS | PARTIAL | PASS | PASS |
| C-49 (mutual-audit design principle) | PASS | PASS | PASS | PASS | PASS |
| C-50 (pre-table Protocol block) | FAIL | PASS | FAIL | PARTIAL | PASS |
| C-51 (leading-clause token) | PASS | FAIL | FAIL | PARTIAL | PASS |
| AC-24 status | FAIL | PASS | FAIL | PARTIAL | PASS |
| AC-25 status | PASS | FAIL | FAIL | PARTIAL | PASS |
| D-15 structurally blocked | YES | NO | NO | PARTIAL | YES |
| D-16 structurally blocked | NO | YES | NO | PARTIAL | YES |

**V-05 is the R17 ceiling.** It is the only variation that structurally blocks both D-15 and
D-16 simultaneously. V-01 blocks D-15 but leaves D-16 open. V-02 blocks D-16 but leaves D-15
open. V-03 blocks neither. V-04 partially addresses both without fully closing either. Only
V-05 achieves full dual-encounter defense-in-depth against both single-encounter failure modes.
