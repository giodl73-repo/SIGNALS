---
skill: flow-lifecycle
round: 14
rubric-version: v14
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v14-2026-03-16.md
floor: flow-lifecycle-variate-R13-2026-03-15.md V-05
---

# flow-lifecycle -- Round 14 Variations (rubric v14: C-46, C-47)

Round 14 holds the R13 V-05 full floor and probes two new aspirational criteria that extend the
pre-schema anchoring architecture in different directions:

- **C-46 -- Pre-Schema Incumbent-Process Anchoring**: A STATUS-QUO PROCESS DECLARATION block
  appears before STEP 0A. It names (1) the incumbent process or workaround being replaced,
  (2) >=2 named failure modes with explicit FM-IDs each naming what the incumbent fails to
  detect or prevent, and (3) an inertia driver naming why the incumbent persists. All
  downstream comparison columns must trace to named FM-IDs from this declaration. A cell that
  references no FM-ID is structurally unanchored. The declaration is a traceable reference
  structure, not decorative commentary.

- **C-47 -- Dual-Column Escape-Code Structural Pressure**: The Phase Index Entry Trigger column
  carries both the typed DERIVED:rationale escape code (satisfying C-44) AND a co-located
  Status-Quo Gap column in the same Phase Index table. The Status-Quo Gap column names, for
  each phase, the specific FM-ID from C-46 that the phase's entry trigger addresses. The two
  columns audit each other: a generic DERIVED:rationale simultaneously produces a vague
  Status-Quo Gap with no FM-ID reference -- making the incompleteness structurally visible
  without requiring a separate gate.

**Invariants across all five variations**: All variations carry the complete R13 V-05 floor --
C-27 (scan defect taxonomy with named Defect Type column referenced in gate), C-28 (Handler
column co-locates backward-trace authority rule and fail-declaration), C-29/C-31 (dual-mechanism
Decision Condition column header: threshold-type category list + quoted example), C-30/C-32
(bidirectional exception-catalog gates, upstream and downstream), C-33 (Step 0 LT inventory),
C-34 (failure surface taxonomy), C-35 (non-overlapping evidence mandate), C-36 (LT-ID trace
cascade in role registry and phase index), C-37 (dual-mechanism failure variant taxonomy in
defect table), C-38 (Detected By column in defect taxonomy), C-39 (per-phase Blocked by C-ID
in exit gates), C-40 (Check V secondary terminal verification, named in Production Gate),
C-41 (coverage scan semantic group partitioning), C-42 (STEP 0A / STEP 0B sequential labeling),
C-43 (Initial Phase field in LT records), C-44 (typed escape-code vocabulary: SECONDARY and
DERIVED), C-45 (downstream exception-catalog gate uses "certified Handler R-ID" language).

**R14 failure modes to probe:**

| Mode | Criterion | What R13 V-05 does | What v14 requires |
|------|-----------|-------------------|------------------|
| Missing SQ Declaration | C-46 | Schema begins at STEP 0A; no pre-schema incumbent comparison block | STATUS-QUO PROCESS DECLARATION before STEP 0A with >=2 FM-IDs and inertia driver |
| Decorative SQ Declaration | C-46 | Incumbent narrative present but FM-IDs never referenced downstream | Every downstream comparison column traces to a named FM-ID; cell with no FM-ID is structurally unanchored |
| Single-column Phase Index | C-47 | Phase Index has Entry Trigger with DERIVED:rationale; no Status-Quo Gap column | Phase Index has Entry Trigger AND Status-Quo Gap as adjacent co-located columns in the same table |
| Vague Status-Quo Gap | C-47 | Status-Quo Gap column present but filled with prose descriptions lacking FM-ID reference | Each Status-Quo Gap cell must name a specific FM-ID from C-46; prose without FM-ID is structurally unanchored |

**Round 14 hypothesis matrix:**

| Variation | C-46 (SQ Declaration) | C-47 (Status-Quo Gap column) | Axis |
|-----------|:---------------------:|:----------------------------:|------|
| V-01 | TARGET | HOLD | Inertia Framing |
| V-02 | HOLD | TARGET | Output Format |
| V-03 | TARGET | TARGET | Phrasing Register |
| V-04 | TARGET | HOLD | Role Sequence + Inertia Framing |
| V-05 | TARGET | TARGET | Lifecycle Emphasis + Inertia Framing + Phrasing Register |

---

## V-01 -- Inertia Framing: FM-IDs as Downstream Reference Registry

**Variation axis:** Inertia framing -- the STATUS-QUO PROCESS DECLARATION is the primary
structural spine of the entire schema. FM-IDs defined in that block are mandatory fields in
every downstream section that has a status-quo comparison dimension. Column headers in the
Phase Index carry the FM-ID reference requirement inline with "traces to no FM-ID is
structurally unanchored" language. STEP 0A / STEP 0B remain labeled via section headers
(satisfying C-42). Initial Phase satisfies C-43. SECONDARY / DERIVED typed escape codes
satisfy C-44. Gate D uses "certified Handler R-ID" for C-45. The new R14 probe is C-46:
the SQ Declaration is authored before any schema section, and its FM-IDs propagate as
mandatory trace fields into the Phase Index (satisfying C-47 at floor level).

**Hypothesis:** C-46 fails most often when the SQ Declaration is present but treated as
commentary -- authors write a prose summary of the old process without assigning FM-IDs, or
they assign FM-IDs but never reference them in downstream columns. When the Phase Index
Status-Quo Gap column header uses "FM-ID from STATUS-QUO PROCESS DECLARATION -- a cell with
no FM-ID is structurally unanchored" language at the exact point where the author fills the
column, the reference chain from declaration to phase becomes a scannable blank rather than
a forgotten rule. The prediction: inline FM-ID enforcement at downstream column headers reduces
the unanchored-gap defect (D-11) more reliably than a preamble instruction to use FM-IDs.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read every column
header before filling rows -- column headers carry field rules inline; there are no separate
preamble rule blocks.

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs defined here are required fields in downstream
comparison columns. A downstream cell that references no FM-ID from this block is structurally
unanchored and is a fail.

| SQ-Field | Content -- field rules inline |
|----------|-------------------------------|
| Incumbent Process -- names the specific process, tool, or workaround being replaced; "manual process" or "spreadsheet" without qualification does not count; name the specific named process or tool | |
| FM-01 -- first failure mode: names the specific condition the incumbent fails to detect or prevent; "error-prone" or "inefficient" does not count; must name the missing detection or prevention mechanism as FM-01 | |
| FM-02 -- second failure mode: second orthogonal failure condition; identical or overlapping failure mode is a fail; must carry identifier FM-02 | |
| Inertia Driver -- names the organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B. This block is the traceability
anchor for all downstream LT-ID references in Step 1 (role registry) and Step 2 (phase index).

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail; if the trigger enters an existing phase mid-run, name that containing phase |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Author this table completely before proceeding to Step 1. Failure surface entries reference
gate domains whose scope is determined by the LT-IDs enumerated in STEP 0A -- STEP 0A must
therefore be complete before STEP 0B is authored.

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary (e.g., "pre-schema entry defects," "exception-catalog structure defects," "decision quality defects"); "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
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

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows and may appear as Handler R-ID in Step 5; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase this role appears; if role exists outside all LT scopes, write SECONDARY:[rationale naming why this role exists without any LT anchor]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary] -- generic "N/A" or blank is a fail) | Status-Quo Gap (FM-ID from STATUS-QUO PROCESS DECLARATION -- names which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID reference is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------|
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

For each phase, declare the exit gate. The "Blocked by" field is mandatory in every gate --
no gate may have a blank criterion anchor.

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
|------|--------------|----------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open the Terminal Declaration
> until all exception flows carry a **certified Handler R-ID** -- that is, an R-ID that traces
> to a role pre-certified as Exception Handler = Y in the Role Registry. An exception flow
> with an uncertified or blank Handler R-ID is a structural fail that blocks this gate.
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

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header labeled "STEP 0A"; STEP 0B section header labeled "STEP 0B"; STEP 0A precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; block names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration block | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no
cell may share the same coverage claim across rows.

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
| AC-22 | Phase Index carries Status-Quo Gap column co-located with Entry Trigger column; each Phase Index row names a specific FM-ID from STATUS-QUO PROCESS DECLARATION in the Status-Quo Gap field; no row may have a blank or FM-ID-free Status-Quo Gap cell | Step 2 table | | |

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
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose description without FM-ID from C-46, or cell is blank | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index: Entry Trigger column carries DERIVED:rationale; no co-located Status-Quo Gap column in Phase Index table | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index: Status-Quo Gap column present in Phase Index; Entry Trigger does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, an unanchored status-quo gap, a DERIVED-only or gap-column-only
> Phase Index, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape
> code in a downstream trace column) -- and that artifact must be discarded and rerun from the
> failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-22.
> (2) Check V shows CLOSED.

---

## V-02 -- Output Format: Column Co-Location Enforces Mutual Auditing for C-47

**Variation axis:** Output format -- the Phase Index table structure is the primary carrier of
C-47 enforcement. The two columns -- Entry Trigger and Status-Quo Gap -- appear as adjacent
columns in the Phase Index header with co-located enforcement language that names the auditing
relationship explicitly: "these two columns audit each other." A generic DERIVED:rationale
paired with a vague Status-Quo Gap is not two independent failures -- it is one visible
incompleteness whose dual expression is detectable in a single table scan. The STATUS-QUO
PROCESS DECLARATION is condensed (key-value rather than inline-enforcement table) since V-02
targets C-47's column co-location as the primary probe; C-46 is held at floor. STEP 0A / STEP
0B labels satisfy C-42; Initial Phase satisfies C-43; SECONDARY/DERIVED typed codes satisfy
C-44; Gate D satisfies C-45; the full R13 floor is maintained.

**Hypothesis:** C-47 fails not from missing columns but from column placement -- authors add a
Status-Quo Gap column as a separate table or as a trailing column separated from Entry Trigger
by three or four intervening columns. When the column pair is architecturally adjacent in the
table definition and the shared header uses "these two columns audit each other" language, the
mutual-verification relationship is visible as a structural property of the table rather than
as an enforcement rule discovered on a second read. The prediction: co-located column headers
with explicit auditing language reduce the vague-gap defect (D-11) and the DERIVED-only defect
(D-12) more reliably than separate column definitions.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Column headers carry
all field rules inline.

---

### STATUS-QUO PROCESS DECLARATION

| Field | Value |
|-------|-------|
| Incumbent Process | |
| FM-01 (what the incumbent fails to detect or prevent) | |
| FM-02 (second orthogonal failure; must not overlap FM-01) | |
| Inertia Driver (why the incumbent persists despite FM-01 and FM-02) | |

FM-IDs defined in this block are required fields in the Phase Index Status-Quo Gap column.
A Phase Index row with a Status-Quo Gap cell that names no FM-ID from this block is
structurally unanchored.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail; if the trigger enters an existing phase mid-run, name that containing phase |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category fail | Gate Domain -- schema section or boundary this surface maps to; "general" does not count | Closed By (C-ID or Gate Label) -- specific criterion or gate; blank is a fail |
|-------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. Failure surfaces must be orthogonal.

> Do not proceed to Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User") do not count | Domain -- process function; org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase this role appears; if role exists outside all LT scopes, write SECONDARY:[rationale]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete. Every Entry Trigger
> must carry an LT-ID or DERIVED:rationale. Every Status-Quo Gap must name a specific FM-ID.
> Blocked by: C-16, C-36, C-47

The Entry Trigger and Status-Quo Gap columns are adjacent and audit each other: a generic
DERIVED:rationale simultaneously produces a vague Status-Quo Gap with no FM-ID reference,
making the incompleteness visible as a co-occurring defect in a single row scan.

| Ph-ID | Phase Name | Entry Trigger -- LT-ID from STEP 0A naming this phase, OR DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail | Status-Quo Gap -- FM-ID from STATUS-QUO PROCESS DECLARATION naming the specific incumbent failure mode this phase addresses; these two columns audit each other: a cell with no FM-ID is structurally unanchored and is a fail | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration; "as soon as possible" does not count | SLA Risk -- breach condition + causal bottleneck; at least one phase must be annotated AT-RISK | States Contained |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------|
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

| D-ID | Decision Name | Decision Condition (BOTH required simultaneously: (1) threshold-type category -- dollar amount, day count, retry count, unit quantity -- AND (2) quoted example with comparison operator and unit, e.g., "Invoice value > $10,000"; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback -- mechanism-impairment path; names holding state or escalation target; "escalate" alone does not count |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------|--------------------------|----------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 fork-join or explicit "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open the Exception Catalog until
> State Trace and Decision Table are both complete and stable.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. "Blocked by: [C-ID]" is mandatory in every gate.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state that closes this phase]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID on clean exit]
Failure:        [T-ID or exception name on exit failure]
Blocked by:     [C-ID(s) -- Mandatory; blank is a structural fail]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- specific condition; "an error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in Step 1; Mandatory; blank or uncertified role is a structural fail | Divergence Phase/Step -- specific states bypassed or added | Recovery State or Terminal -- named S-ID or T-ID; "resolved" does not count |
|------|--------------|----------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration until
> all exception flows carry a **certified Handler R-ID** -- an R-ID tracing to Exception
> Handler = Y in the Role Registry.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs; blank is a fail) |
|------|--------------|----------------------------------|------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) reaches a named T-ID. Status is CLOSED only
> when every path is individually confirmed. Check V CLOSED is a co-equal Production Gate
> condition alongside Coverage Scan PASS.

---

**STEP 7 -- EDGE CASE CATALOG**

Minimum 2. Distinct from Step 5 exception flows.

| EC-ID | Edge Case -- concrete scenario | Phase (Ph-ID) | Gap Reason -- specific omission; "not considered" does not count | Consequence -- operational or compliance impact |
|-------|-------------------------------|--------------|------------------------------------------------------------------|------------------------------------------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration -- specific; "timely" does not count | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|------------------------------------------------------|---------------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause (if Y: name the bottleneck or E-ID; "delays" alone is a fail) |
|-------|--------------|----------------------|--------------|---------------------------------------------------------------------|
| BV-01 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Minimum 2 bottlenecks.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause (root-cause type + named element) | Downstream Impact (S-IDs or Ph-IDs + consequence type) | Breach Link (BV-ID / SLA-ID / SLA-ABSENT) |
|------|--------------|-----------------|----------------------------------------|-------------------------------------------------------|------------------------------------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Minimum 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required (regulatory rule / handoff precondition / system dependency; "best practice" is a fail) | Risk if Absent |
|------|--------------|-------------|-------------------------------------------------------------------------------------------------------|----------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Minimum 1.

| Handoff Trigger | Partner Lifecycle (specific name) | Direction (Inbound / Outbound) | Fields Passed (specific data objects) | Coupling State (blocking / advisory) |
|----------------|----------------------------------|-------------------------------|---------------------------------------|--------------------------------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|----------------------|-------------|------------------|
| PH-01 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A has >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B has >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A section header present and precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; names Incumbent Process, FM-01, FM-02 (each with identifier), and Inertia Driver | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no row may share the same coverage claim as another row.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale | Step 1 table | | |
| AC-05 | Step 1 LT-ID Trace column header defines SECONDARY escape code inline | Step 1 header | | |
| AC-06 | Step 2 Entry Trigger column header defines DERIVED escape code inline | Step 2 header | | |
| AC-07 | Every exception Handler R-ID traces to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Phase Index Entry Trigger and Status-Quo Gap columns are adjacent in the same table; column header names the auditing relationship; each row carries a specific FM-ID in Status-Quo Gap | Step 2 table + header | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach a named T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with measurable threshold, owner, all branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner, direction, fields, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record present without Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-03 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index: Entry Trigger carries DERIVED:rationale; no co-located Status-Quo Gap column | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index: Status-Quo Gap column present; Entry Trigger column does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, an unanchored status-quo gap, a DERIVED-only or gap-column-only
> Phase Index, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape
> code) -- and must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-22.
> (2) Check V shows CLOSED.

---

## V-03 -- Phrasing Register: Imperative FM-ID Trace as Production Action

**Variation axis:** Phrasing register -- all instructions use second-person imperative verbs
("Write", "Name", "State", "Confirm") rather than modal obligation ("must", "is required to",
"should carry"). C-46 and C-47 are both targeted in this variation: the SQ Declaration is
framed as a production action ("Write the incumbent process name. Write FM-01: what it fails
to detect. Write FM-02.") and the Phase Index Status-Quo Gap is framed as a production action
at the exact step where the author fills that column ("Write the FM-ID from the SQ Declaration
that this phase addresses. Do not write a description without an FM-ID reference."). STEP 0A /
STEP 0B labels satisfy C-42. Initial Phase satisfies C-43. SECONDARY/DERIVED codes satisfy
C-44. Gate D satisfies C-45. Full R13 floor is maintained.

**Hypothesis:** C-47 fails not from schema omission but from compliance-mode writing -- authors
fill the Status-Quo Gap column with prose descriptions of the problem without anchoring to a
named FM-ID, because the rule was stated once in a preamble and was not present when the
column was being filled. An imperative instruction at the step level -- "Write FM-01 or FM-02
in this field. A description without an FM-ID is a fail" -- is encountered at the exact moment
the authorial decision is being made, and converts the FM-ID trace from a remembered rule to
an active production step. The prediction: imperative register at point of use reduces D-11
(unanchored status-quo gap) more reliably than declarative enforcement at column headers,
because it frames the FM-ID as a thing being written rather than a thing being checked.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Follow every step in writing order. Complete each step before
opening the next.

---

### STATUS-QUO PROCESS DECLARATION

Write this block before writing STEP 0A.

Name the incumbent process being replaced. Do not write "manual process" -- write the specific
named process, tool, or workflow that this lifecycle replaces.

Write FM-01: name the specific condition the incumbent fails to detect or prevent. Assign the
identifier FM-01. Do not write "error-prone" or "slow" -- write the specific missing detection
or prevention mechanism.

Write FM-02: name a second failure mode, orthogonal to FM-01. Assign identifier FM-02.

Write the inertia driver: name the specific organizational, systemic, or economic reason the
incumbent persists despite FM-01 and FM-02.

| Field | Value |
|-------|-------|
| Incumbent Process | |
| FM-01 | |
| FM-02 | |
| Inertia Driver | |

The FM-01 and FM-02 identifiers from this block are required in the Phase Index Status-Quo Gap
column. Do not open STEP 0A until this block is complete.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Write STEP 0A before writing STEP 0B. For each event, role action, or time condition that can
start this lifecycle, write one row.

For the Trigger Source field: write exactly one of "System Event", "Role Action", or "Time
Condition." Do not invent other categories.

For the Initial Phase field: write the name of the phase this trigger activates. If the trigger
enters an already-open phase mid-run, write that containing phase. Do not leave this field
blank -- a lifecycle trigger that activates no phase is undefined.

| LT-ID | Trigger Description | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase |
|-------|--------------------|------------------------------------------------------------|---------------|---------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Write minimum 3 rows. Do not open STEP 0B until this table is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Write STEP 0B after STEP 0A is complete. For each structural defect category this schema
defends against, write one row. Name a gate domain that corresponds to a schema boundary --
not a process exception. Name the specific criterion or gate that closes the surface. Confirm
no two rows describe the same defect category before proceeding.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|----------------|------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Write minimum 3 rows. Do not open Step 1 until this table is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Write the complete Role Registry before opening the Phase Index. Confirm at least
> one role carries Exception Handler = Y and every role has an LT-ID Trace or SECONDARY before
> proceeding.
> Blocked by: C-05, C-11, C-23, C-36

For each role this lifecycle requires, write one row. Follow these per-column instructions:

- **Role Name**: Write a domain-qualified functional title -- what the org chart would show.
  Write "Senior Credit Analyst," not "Approver." Write "Procurement Manager," not "Finance."
- **Exception Handler (Y/N)**: Write Y for every role authorized to handle exception flows.
  Write N for all others. Write at least one Y. Do not leave blank.
- **LT-ID Trace**: Write the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase
  this role first appears. If the role exists outside every LT-ID's scope, write
  SECONDARY:[rationale] -- state the specific reason this role exists without an LT anchor.
  Do not write "N/A." Do not leave blank.

| R-ID | Role Name | Domain | Exception Handler (Y/N) | LT-ID Trace (or SECONDARY:[rationale]) |
|------|----------|--------|------------------------|----------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Write minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Write the complete Phase Index before opening the State Trace. Confirm every
> Entry Trigger carries an LT-ID or DERIVED:rationale. Confirm every Status-Quo Gap cell
> names a specific FM-ID before proceeding.
> Blocked by: C-16, C-36, C-47

For each phase, write the event that opens it. For the Entry Trigger field: write the LT-ID
from STEP 0A whose Initial Phase names this phase. If the phase is derived from a combination
of LT paths, write DERIVED:[rationale naming which LT-IDs and how they combine]. Do not write
"N/A."

For the Status-Quo Gap field: write the FM-ID from the STATUS-QUO PROCESS DECLARATION that
this phase's entry trigger addresses. Write FM-01 or FM-02 -- do not write a prose description
without an FM-ID reference. A description without an FM-ID is structurally unanchored.

Write the completion condition, SLA envelope, and SLA risk. Mark at least one phase AT-RISK.

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]) | Status-Quo Gap (FM-ID from SQ Declaration -- write FM-01 or FM-02; prose without FM-ID is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|----------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------|-------------|----------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Write minimum 3 phases. Put at least 2 states per phase.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Write at least 6 states across all phases. For each state, write the entry condition (the
specific event or predecessor state -- not "after previous step"), the exit transitions
(labeled outbound paths naming trigger and destination -- not "then continue"), the owner R-ID
from Step 1, the timing, and the SLA status. Write at least 3 states with timing values. Mark
at least 1 AT-RISK.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

Write at least 3 decision points. For each decision condition, write both a named threshold
type (dollar amount, day count, retry count, or unit quantity) AND a quoted example with
comparison operator and unit. Writing only a category is a fail. Writing only an example is
a fail. Write both.

| D-ID | Decision Name | Condition (threshold type + quoted example) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback |
|------|--------------|---------------------------------------------|-------------|----------------------|--------------------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

Write at least 1 fork-join, or state absence with a rationale:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Confirm the State Trace and Decision Table
> are complete before opening the Exception Catalog.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. Write a "Blocked by: [C-ID]" field in every gate -- leave no
gate without a criterion anchor.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to close]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID on clean exit]
Failure:        [T-ID or exception name on exit failure]
Blocked by:     [C-ID(s) -- do not leave blank]
```

---

**STEP 5 -- EXCEPTION CATALOG**

Confirm GATE C is CLOSED. Write at least 3 exception flows. For each:

- **Handler R-ID**: Look up the role in Step 1. Confirm Exception Handler = Y before writing
  the R-ID. Do not write an R-ID for a role carrying N. Do not leave blank.
- **Trigger**: Name the specific condition that diverts from the happy path. Do not write
  "an error occurs."
- **Divergence**: Name the states bypassed or added. Do not write "different path."
- **Recovery**: Name the S-ID or T-ID reached. Do not write "resolved."

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y; blank or N-role is a structural fail) | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|---------|------------------------------------------------------------------------------|----------------------|---------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Confirm all exception flows carry a
> **certified Handler R-ID** before opening Terminal Declaration. "Certified" means the R-ID
> traces to a role carrying Exception Handler = Y in the Role Registry.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

Confirm GATE D is CLOSED. Write at least 1 success terminal and 1 failure/cancel terminal.
List every S-ID and E-ID that reaches each terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs) |
|------|--------------|----------------------------------|-------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path individually (happy path + every E-ID) ends at a named T-ID. Mark CLOSED
> only when every path is confirmed. Check V CLOSED is required by the Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG**

Write at least 2 edge cases distinct from Step 5 exception flows.

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|----------------|---------------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause |
|-------|--------------|----------------------|-------------|-------|
| BV-01 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Write at least 2 bottlenecks. Name the root-cause type and a specific element. Name the
downstream impact by S-ID or Ph-ID. Write a typed Breach Link.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|----------------|-------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Write at least 1 gap. Name the specific missing step, the regulatory or structural reason it
is required, and the risk if absent.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|-------------|---------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Write at least 1 cross-lifecycle dependency.

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State |
|----------------|-----------------|----------|--------------|---------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|----------------------|-------------|------------------|
| PH-01 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A has >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B has >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A section header present and precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no row may share the same coverage claim as another row.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale | Step 1 table | | |
| AC-05 | Step 1 LT-ID Trace column header defines SECONDARY escape code inline | Step 1 header | | |
| AC-06 | Step 2 Entry Trigger column header defines DERIVED escape code inline | Step 2 header | | |
| AC-07 | Every exception Handler R-ID traces to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Phase Index carries Status-Quo Gap column; each row names a specific FM-ID from SQ Declaration; Status-Quo Gap column is adjacent to Entry Trigger in the same table | Step 2 table | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach a named T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with measurable threshold, owner, all branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner, direction, fields, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record present without Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-03 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index: Entry Trigger carries DERIVED:rationale; no co-located Status-Quo Gap column | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index: Status-Quo Gap column present; Entry Trigger does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, an unanchored status-quo gap, a DERIVED-only or gap-column-only
> Phase Index, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape
> code) -- and must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-22.
> (2) Check V shows CLOSED.

---

## V-04 -- Role Sequence + Inertia Framing: Roles Anchor Against SQ Declaration

**Variation axis:** Role sequence + Inertia framing -- the STATUS-QUO PROCESS DECLARATION
explicitly names which roles existed in the incumbent process ("Incumbent Role Scope"), and
the Role Registry gains an SQ-Scope field that classifies each role as IN (existed in the
incumbent process), NEW (introduced by this lifecycle), or SECONDARY (exists outside both LT
and SQ scope). This role-level SQ traceability makes the inertia driver testable: roles with
SQ-Scope = IN carry organizational anchors that may resist transition and can be named as
inertia contributors in the bottleneck register. C-46 is the primary target; C-47 is held at
floor level (Status-Quo Gap column in Phase Index, FM-ID mandatory). STEP 0A / STEP 0B labels
satisfy C-42. Initial Phase satisfies C-43. SECONDARY/DERIVED codes satisfy C-44. Gate D
satisfies C-45. Full R13 floor is maintained.

**Hypothesis:** C-46 fails at the inertia driver field most often -- authors name the inertia
driver as a process reason ("the old system is familiar") without operationalizing which roles
carry the inertia. When the SQ Declaration includes an Incumbent Role Scope section and the
Role Registry traces each role to IN / NEW / SECONDARY, the inertia driver becomes verifiable:
an inertia claim that names no IN-scope role is an ungrounded assertion. The role-level
anchoring also creates a downstream verifiability surface that the Phase Index FM-IDs do not
provide -- it answers which roles are structurally at risk of resisting the transition, not
only which phases address the incumbent's failure modes.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Column headers carry
all field rules inline.

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs and the Incumbent Role Scope defined here are
required fields in downstream schema sections.

**Part A -- Incumbent Failure Modes:**

| SQ-Field | Content -- field rules inline |
|----------|-------------------------------|
| Incumbent Process -- specific named process, tool, or workaround being replaced; "manual process" without qualification does not count | |
| FM-01 -- first failure mode with identifier FM-01; names what the incumbent fails to detect or prevent; "error-prone" does not count | |
| FM-02 -- second orthogonal failure mode with identifier FM-02; overlapping or identical failure mode is a fail | |
| Inertia Driver -- names the specific organizational, systemic, or economic reason the incumbent persists; must reference at least one named incumbent role; "familiarity" without specificity does not count | |

**Part B -- Incumbent Role Scope:**

List the roles that existed in the incumbent process. These roles carry SQ-Scope = IN in
Step 1 and are potential inertia carriers. Roles not listed here carry SQ-Scope = NEW or
SECONDARY in Step 1.

| SQ-R-ID | Incumbent Role Title | Reason Persists (function this role serves in the incumbent that may resist transition) |
|---------|---------------------|----------------------------------------------------------------------------------------|
| SQR-01 | | |
| SQR-02 | | |

Minimum 2 rows.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

| LT-ID | Trigger Description -- external event, role action, or time condition; "process begins" does not count | Trigger Source (System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail |
|-------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; same-category duplicate is a fail | Gate Domain -- schema section or boundary; "general" does not count | Closed By (C-ID or Gate Label); blank is a fail |
|-------|---------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows.

> Do not proceed to Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, every role has an
> LT-ID Trace or SECONDARY:rationale, and every role has an SQ-Scope value.
> Blocked by: C-05, C-11, C-23, C-36, C-46

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst"); generic labels do not count | Domain -- process function; org-unit without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; at least one Y; blank is a fail | LT-ID Trace (or SECONDARY:[rationale]; N/A or blank is a fail) | SQ-Scope -- must be exactly: IN (role existed in the incumbent process; trace to a SQR-ID from SQ Declaration Part B) / NEW (role is introduced by this lifecycle) / SECONDARY (role exists outside LT and SQ scope; write SECONDARY:[rationale]); blank is a fail |
|------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| R-03 | | | | | |

Minimum 3 roles. At least 1 IN-scope role (tracing to a SQR-ID) is required if the incumbent
process involved human roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming LT-IDs and combination logic] -- generic "N/A" or blank is a fail) | Status-Quo Gap (FM-ID from STATUS-QUO PROCESS DECLARATION Part A -- names which incumbent failure mode this phase addresses; cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output; "work is done" does not count | SLA Envelope -- specific duration; "as soon as possible" does not count | SLA Risk -- at least one phase must be AT-RISK | States Contained |
|-------|-----------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- specific event or predecessor state; "after previous step" does not count | Exit Transitions -- labeled outbound paths; "then continue" does not count | Owner (R-ID) -- must appear in Step 1; blank is a fail | Timing -- specific duration or N/A + reason | SLA Status (Normal / AT-RISK / Critical) |
|------|--------------|------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------|------------------------------------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

Minimum 3 states with timing. Minimum 1 AT-RISK.

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (BOTH required: (1) threshold-type category -- dollar amount, day count, retry count, unit quantity -- AND (2) quoted example with operator and unit; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------|--------------------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 fork-join or explicit "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open Exception Catalog until State
> Trace and Decision Table are complete.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. "Blocked by: [C-ID]" is mandatory in every gate.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID on clean exit]
Failure:        [T-ID or exception name]
Blocked by:     [C-ID(s) -- Mandatory; blank is a structural fail]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- specific condition; "an error occurs" does not count | Handler (R-ID) -- Must trace to Exception Handler = Y in Step 1; Mandatory; blank or uncertified role is a structural fail | Divergence Phase/Step | Recovery State or Terminal -- named S-ID or T-ID |
|------|--------------|----------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declaration until
> all exception flows carry a **certified Handler R-ID** tracing to Exception Handler = Y.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs; blank is a fail) |
|------|--------------|----------------------------------|------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) reaches a named T-ID. Status is CLOSED only
> when every path is individually confirmed. Check V CLOSED is a co-equal Production Gate
> condition.

---

**STEP 7 -- EDGE CASE CATALOG**

Minimum 2. Distinct from Step 5 exception flows.

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|----------------|---------------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause |
|-------|--------------|----------------------|-------------|-------|
| BV-01 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Minimum 2 bottlenecks. Where the bottleneck involves an IN-scope role from the SQ Declaration,
name the SQR-ID as a contributing inertia factor.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause (root-cause type + named element; SQR-ID if applicable) | Downstream Impact | Breach Link |
|------|--------------|-----------------|---------------------------------------------------------------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Minimum 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|-------------|---------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Minimum 1.

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State |
|----------------|-----------------|----------|--------------|---------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|----------------------|-------------|------------------|
| PH-01 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A has >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B has >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A section header present and precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; Part A names Incumbent Process, FM-01, FM-02 (each with identifier), and Inertia Driver; Part B names >=2 incumbent roles with SQR-IDs | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no row may share the same coverage claim as another row.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role carries domain-qualified title, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale, and SQ-Scope value | Step 1 table | | |
| AC-05 | Step 1 LT-ID Trace column header defines SECONDARY escape code inline | Step 1 header | | |
| AC-06 | Step 2 Entry Trigger column header defines DERIVED escape code inline | Step 2 header | | |
| AC-07 | Every exception Handler R-ID traces to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C and Gate D both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Phase Index carries Status-Quo Gap column adjacent to Entry Trigger; each row names a specific FM-ID from SQ Declaration Part A | Step 2 table | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach a named T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with measurable threshold, owner, all branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner, direction, fields, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record present without Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-03 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Phase Index Status-Quo Gap cell contains prose without FM-ID, or cell is blank | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index: Entry Trigger carries DERIVED:rationale; no co-located Status-Quo Gap column | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index: Status-Quo Gap column present; Entry Trigger does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, an unanchored status-quo gap, a DERIVED-only or gap-column-only
> Phase Index, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape
> code) -- and must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-22.
> (2) Check V shows CLOSED.

---

## V-05 -- Combined: Lifecycle Emphasis + Inertia Framing + Phrasing Register

**Variation axis:** Lifecycle emphasis + Inertia framing + Phrasing register -- phases are the
primary scaffold; each phase is modeled as a full structured block rather than a table row;
every phase block carries an FM-ID trace field linking the phase's purpose to the SQ Declaration.
All instructions use imperative verbs. This is the Round 14 floor candidate for R15.

C-46 is targeted via the STATUS-QUO PROCESS DECLARATION (full block with inline enforcement)
and via FM-ID trace fields that appear inside each phase block in the Phase Index. C-47 is
targeted by making the Status-Quo Gap a named field in the phase block structure itself --
co-located with the Entry Trigger field -- so the auditing relationship is enforced by block
architecture rather than by column adjacency alone. STEP 0A / STEP 0B labels satisfy C-42.
Initial Phase satisfies C-43. SECONDARY / DERIVED typed codes satisfy C-44. Gate D satisfies
C-45. Full R13 floor is maintained.

**Hypothesis:** C-47's dual-column pressure is strongest when the two fields appear in the
same structural block rather than as adjacent columns in a wide table. A phase contract block
contains Entry Trigger and Status-Quo Gap as named fields on sequential lines -- an author
filling "Entry Trigger: DERIVED:[rationale]" immediately sees "Status-Quo Gap: FM-?" on the
next line. The juxtaposition at block authoring time -- rather than at column scan time --
surfaces the incompleteness at the moment the generic DERIVED:rationale is written, not after
the phase table is complete. The lifecycle-emphasis axis also strengthens C-43: when each phase
is a block and the block contains an "Entry Trigger: LT-ID" field, the Initial Phase field in
STEP 0A is verified by direct cross-reference at block authoring time.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Follow each step in order. Complete each step before opening
the next. Use block format for phase definitions.

---

### STATUS-QUO PROCESS DECLARATION

Write this block before STEP 0A.

Name the incumbent process being replaced. Name it specifically -- the process name, tool
name, or workaround description that teams currently use. Do not write "manual process" alone.

Write FM-01: name the specific condition the incumbent fails to detect or prevent. Assign the
identifier FM-01 in the cell. Do not write "error-prone" -- write the specific missing check,
rule, or enforcement mechanism.

Write FM-02: name a second failure mode orthogonal to FM-01. Assign identifier FM-02. Do not
duplicate FM-01.

Write the inertia driver: name the specific reason the incumbent persists. Reference at least
one named role or system dependency.

| SQ-Field | Content -- inline rules apply |
|----------|-------------------------------|
| Incumbent Process -- specific name; "spreadsheet" or "manual process" alone does not count | |
| FM-01 -- identifier FM-01; names what the incumbent fails to detect or prevent; generic "error-prone" is a fail | |
| FM-02 -- identifier FM-02; second orthogonal failure mode; identical or overlapping is a fail | |
| Inertia Driver -- names a specific role, system, or economic anchor; "familiarity" alone does not count | |

These FM-IDs are required fields in Step 2 phase blocks. Do not open STEP 0A until this
block is complete.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Write every event, role action, or time condition that can start this lifecycle. Write four
fields per row: Trigger Description, Trigger Source, Initial State, and Initial Phase.

For Trigger Source: write exactly "System Event," "Role Action," or "Time Condition." Write
nothing else.

For Initial Phase: write the phase name this trigger activates. Do not leave blank.

| LT-ID | Trigger Description | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase |
|-------|--------------------|------------------------------------------------------------|---------------|---------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Write minimum 3 rows. Do not open STEP 0B until this table is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Write STEP 0B after STEP 0A. Name every structural defect category this schema defends against.
Name the gate domain and the closing criterion for each. Confirm no two rows describe the same
defect category.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|----------------|------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Write minimum 3 rows. Do not open Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Write the complete Role Registry before opening the Phase Index. Confirm at least
> one role carries Exception Handler = Y and every role has an LT-ID Trace value.
> Blocked by: C-05, C-11, C-23, C-36

For each role, write one row. Write a domain-qualified functional title -- the org-chart job
title, not a generic label. Write "Senior Credit Analyst," not "Approver." Write N/Y in the
Exception Handler field for every role. Write an LT-ID from STEP 0A for the LT-ID Trace; if
the role exists outside all LT scope, write SECONDARY:[rationale] -- not "N/A."

| R-ID | Role Name | Domain | Exception Handler (Y/N) -- Mandatory; at least one Y; blank is a fail | LT-ID Trace (or SECONDARY:[rationale] -- not N/A or blank) |
|------|----------|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Write minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Write all phase blocks before opening the State Trace. Confirm every phase block
> carries an LT-ID or DERIVED:rationale in the Entry Trigger field, and an FM-ID in the
> Status-Quo Gap field.
> Blocked by: C-16, C-36, C-47

Write each phase as a structured block. The Entry Trigger and Status-Quo Gap fields are
adjacent in the block -- a generic DERIVED:rationale will simultaneously produce a vague
Status-Quo Gap with no FM-ID, making the incompleteness visible within the block without a
separate scan.

```
Phase:            [Ph-ID: Phase Name]
Entry Trigger:    [LT-ID from STEP 0A naming this phase, OR DERIVED:[rationale naming which
                   LT-IDs and combination logic produced this phase boundary] -- do not write
                   "N/A"]
Status-Quo Gap:   [FM-01 or FM-02 from STATUS-QUO PROCESS DECLARATION -- write the FM-ID and
                   state specifically which incumbent failure mode this phase addresses; do not
                   write a description without an FM-ID reference; a cell with no FM-ID is
                   structurally unanchored]
Completion:       [verifiable output or state that closes this phase; "work is done" does not
                   count]
SLA Envelope:     [target duration -- e.g., "5 business days"; "as soon as possible" does not
                   count]
SLA Risk:         [breach condition + causal bottleneck; mark AT-RISK if SLA breach is likely;
                   at least one phase must be marked AT-RISK]
States Contained: [populated after Step 3]
```

Write minimum 3 phase blocks. Each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Write at least 6 states across all phases. For each state:

- Write the entry condition: the specific event or predecessor state. Do not write "after
  previous step."
- Write the exit transitions: labeled outbound paths naming trigger and destination. Do not
  write "then continue."
- Write the owner R-ID from Step 1. Do not leave blank.
- Write the timing and SLA status.

Write at least 3 states with timing values. Mark at least 1 AT-RISK.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

Write at least 3 decision points. For each decision condition, write both (1) a named threshold
type from this list -- dollar amount, day count, retry count, unit quantity -- and (2) a quoted
example with comparison operator and unit. Write both. Do not write only a category. Do not
write only a quoted example.

| D-ID | Decision Name | Condition (threshold type + quoted example; both required simultaneously) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback |
|------|--------------|---------------------------------------------------------------------------|-------------|----------------------|--------------------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

Write at least 1 fork-join, or declare absence with a rationale:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Confirm the State Trace and Decision Table
> are complete and stable before opening the Exception Catalog.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. Write a "Blocked by: [C-ID]" field in every gate.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to close]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID on clean exit]
Failure:        [T-ID or exception name on exit failure]
Blocked by:     [C-ID(s) -- do not leave blank]
```

---

**STEP 5 -- EXCEPTION CATALOG**

Confirm GATE C is CLOSED. Write at least 3 exception flows.

- Write the Handler R-ID: look up the role in Step 1, confirm Exception Handler = Y, then
  write the R-ID. Do not write an R-ID for a role carrying N. Do not leave blank.
- Write the Trigger: name the specific condition. Do not write "an error occurs."
- Write the Divergence: name states bypassed or added. Do not write "different path."
- Write the Recovery: name the S-ID or T-ID. Do not write "resolved."

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y; blank or N-role is a structural fail) | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|---------|------------------------------------------------------------------------------|----------------------|---------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Confirm all exception flows carry a
> **certified Handler R-ID** before opening the Terminal Declaration. "Certified" means the
> R-ID traces to a role carrying Exception Handler = Y in the Role Registry.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

Confirm GATE D is CLOSED. Write at least 1 success terminal and 1 failure/cancel terminal.
List every S-ID and E-ID that reaches each terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs; blank is a fail) |
|------|--------------|----------------------------------|------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) individually ends at a named T-ID. Mark CLOSED
> only when every path is confirmed. Check V CLOSED is a co-equal Production Gate condition
> alongside Coverage Scan PASS.

---

**STEP 7 -- EDGE CASE CATALOG**

Write at least 2 edge cases distinct from Step 5 exception flows.

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|----------------|---------------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause |
|-------|--------------|----------------------|-------------|-------|
| BV-01 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Write at least 2 bottlenecks. Name the root-cause type and a specific element. Name the
downstream states or phases affected. Write a typed Breach Link.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|----------------|-------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Write at least 1 gap. Name the specific missing step, the structural reason it is required,
and the risk if absent.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|-------------|---------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Write at least 1 cross-lifecycle dependency.

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State |
|----------------|-----------------|----------|--------------|---------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|----------------------|-------------|------------------|
| PH-01 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A has >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B has >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A section header present and precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no row may share the same coverage claim as another row.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role carries domain-qualified title, Exception Handler Y/N, and LT-ID Trace or SECONDARY:rationale | Step 1 table | | |
| AC-05 | Step 1 LT-ID Trace column header defines SECONDARY escape code inline | Step 1 header | | |
| AC-06 | Step 2 Entry Trigger field in each phase block defines DERIVED escape code | Step 2 blocks | | |
| AC-07 | Every exception Handler R-ID traces to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C and Gate D both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Every phase block in Step 2 carries a Status-Quo Gap field adjacent to the Entry Trigger field; each Status-Quo Gap field names a specific FM-ID from SQ Declaration | Step 2 blocks | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach a named T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with measurable threshold, owner, all branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff with partner, direction, fields, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record present without Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged | C-42, AC-03 |
| D-09 | Missing SQ Declaration: no STATUS-QUO PROCESS DECLARATION block present before STEP 0A | C-46, AC-21 |
| D-10 | FM-ID-free failure mode: SQ Declaration present but a failure mode entry carries no FM-ID identifier | C-46, AC-21 |
| D-11 | Unanchored status-quo gap: Status-Quo Gap field contains prose without FM-ID from C-46, or field is blank | C-47, AC-22 |
| D-12 | DERIVED-only phase definition: Entry Trigger carries DERIVED:rationale; no co-located Status-Quo Gap field in the phase block | C-47, AC-22 |
| D-13 | Gap-field-only phase definition: Status-Quo Gap field present; Entry Trigger does not carry typed DERIVED:rationale escape code | C-44, C-47, AC-06, AC-22 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, an unanchored status-quo gap, a DERIVED-only or gap-field-only phase
> definition, a missing Initial Phase field, unlabeled pre-schema blocks, or a generic escape
> code in a downstream trace column) -- and that artifact must be discarded and rerun from the
> failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-22.
> (2) Check V shows CLOSED.
