---
skill: flow-lifecycle
round: 13
rubric-version: v13
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v13-2026-03-15.md
floor: flow-lifecycle-variate-R12-2026-03-15.md V-05
---

# flow-lifecycle -- Round 13 Variations (rubric v13: C-42, C-43, C-44, C-45)

Round 13 holds the R12 V-05 full floor and probes the four criteria added in rubric v13,
all of which extend the Step 0 traceability architecture introduced in C-33/C-34/C-36:

- **C-42 -- Pre-Schema Dual-Block Sequential Labeling**: The two pre-schema blocks are labeled
  "STEP 0A" (LT inventory) and "STEP 0B" (failure surface taxonomy) as visible section headers
  in authorship order. The ordering enforces that LT-IDs exist before failure surfaces map to
  gate domains.
- **C-43 -- LT-ID Initial Phase Anchor Field**: Each LT-ID record in STEP 0A carries a
  dedicated "Initial Phase" column -- the bridge from the LT inventory to the Phase Index
  Entry Trigger cascade required by C-36. Distinct from "Initial State."
- **C-44 -- Step 0 Cascade Typed Escape-Code Vocabulary**: Downstream trace columns use
  section-specific typed codes -- SECONDARY:rationale (role registry, for roles outside LT
  scope) and DERIVED:rationale (phase index, for phases derived from combinations of LT paths)
  -- rather than generic "N/A" or blank.
- **C-45 -- Downstream Exception-Catalog Gate Certification Condition Naming**: The downstream
  exception-catalog gate text uses "certified Handler R-ID," not merely "Handler R-ID
  assigned," tying gate completion to the pre-certification authority designation in the
  registry's Exception Handler column.

**Invariants across all five variations**: All variations carry the complete R12 V-05 floor --
C-27 (scan defect taxonomy with named Defect Type column referenced in gate), C-28 (Handler
column co-locates backward-trace authority rule and fail-declaration), C-29/C-31
(dual-mechanism Decision Condition column header: category list + quoted example), C-30/C-32
(bidirectional exception-catalog gates, upstream and downstream), C-33 (Step 0 LT inventory),
C-34 (failure surface taxonomy), C-35 (non-overlapping evidence mandate), C-36 (LT-ID trace
cascade in role registry and phase index), C-37 (dual-mechanism failure variant taxonomy in
defect table), C-38 (Detected By column in defect taxonomy), C-39 (per-phase Blocked by C-ID
in exit gates), C-40 (Check V secondary terminal verification, named in Production Gate),
C-41 (coverage scan semantic group partitioning into >=2 named groups).

**R13 failure modes to probe:**

| Mode | Criterion | What R12 V-05 does | What v13 requires |
|------|-----------|-------------------|------------------|
| Merged pre-schema blocks | C-42 | Single unlabeled Step 0 block or prose order | STEP 0A / STEP 0B visible section headers; 0A precedes 0B |
| Three-column LT record | C-43 | Trigger Description, Trigger Source, Initial State | Fourth column: Initial Phase; bridge to Phase Index Entry Trigger backward trace |
| Generic trace escape | C-44 | LT-ID Trace = "N/A" or blank when no LT anchor | SECONDARY:rationale (role registry); DERIVED:rationale (phase index) |
| Uncertified handler gate | C-45 | Downstream gate: "all exception flows have Handler R-ID" | "certified Handler R-ID" -- ties gate to Exception Handler = Y column |

**Round 13 hypothesis matrix:**

| Variation | C-42 (0A/0B labels) | C-43 (Initial Phase) | C-44 (Typed escape codes) | C-45 (Certified gate) | Axis |
|-----------|:------------------:|:--------------------:|:------------------------:|:---------------------:|------|
| V-01 | TARGET | TARGET | HOLD | HOLD | Output Format |
| V-02 | HOLD | HOLD | TARGET | HOLD | Phrasing Register |
| V-03 | HOLD | HOLD | HOLD | TARGET | Lifecycle Emphasis |
| V-04 | TARGET | TARGET | TARGET | HOLD | Role Sequence + Output Format |
| V-05 | TARGET | TARGET | TARGET | TARGET | Lifecycle Emphasis + Phrasing Register + Inertia Framing |

---

## V-01 -- Output Format: Inline Column-Header Enforcement of STEP 0A/0B Labels and Initial Phase Field

**Variation axis:** Output format -- every field-level rule is embedded inline in its column
header using "does not count," "is a fail," or "Mandatory" language. No preamble rule blocks;
all enforcement lives at the column. The four columns of the STEP 0A table make C-43 visible
at point of entry: Trigger Description, Trigger Source, Initial State, and Initial Phase
(Mandatory; blank is a structural fail) appear as defined column headers before the first row
is filled. The STEP 0A / STEP 0B section headers satisfy C-42 directly -- they are the
section headings in the authoring document, not embedded prose annotations. The SECONDARY and
DERIVED escape codes satisfy C-44 by being defined inline in their respective column headers
in Step 1 (role registry) and Step 2 (phase index). The downstream Gate D satisfies C-45
with "certified Handler R-ID" language.

**Hypothesis:** C-43 is the criterion most at risk of silent omission. When LT-ID records are
described in a preamble ("include an Initial Phase field"), authors see the instruction once
and may fill three familiar columns (Trigger Description, Trigger Source, Initial State)
without noticing the omission. When Initial Phase appears as a defined column header -- with
"Mandatory; blank is a structural fail" in the header cell -- the blank column is visible as
an unfilled table cell, not a missing paragraph. Column-header placement converts a structural
omission into a scannable blank. The same logic applies to C-44: a typed escape code defined
in a preamble is forgotten when the author reaches Step 1 row 4 and writes "N/A"; a code
defined in the column header is read at the exact moment the author is entering a value.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read every column
header before filling rows -- column headers carry field rules inline; there are no separate
preamble rule blocks.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B. This block is the traceability
anchor for all downstream LT-ID references in Step 1 (role registry) and Step 2 (phase index).

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- the first lifecycle state activated; a generic name without lifecycle qualifier does not count | Initial Phase -- the phase boundary this trigger activates; Mandatory; blank is a structural fail; if the trigger enters an existing phase mid-run, name that containing phase |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

| FS-ID | Failure Surface -- names a structural defect category (not a process exception); two rows naming the same defect category are not orthogonal and the second is a fail | Gate Domain -- names the schema section or structural boundary this surface maps to (e.g., "pre-schema entry defects," "exception-catalog structure defects," "decision quality defects"); "general" does not count | Closed By (C-ID or Gate Label) -- the specific criterion or gate that prevents this defect; blank is a fail |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
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

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows and may appear as Handler R-ID in Step 5; N = not authorized and may not appear as Handler R-ID; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) from STEP 0A whose Initial State or Initial Phase this role appears in; if role exists outside all LT scopes, write SECONDARY:[rationale naming why this role exists without any LT anchor]; generic "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete and every Entry
> Trigger carries an LT-ID or DERIVED:rationale.
> Blocked by: C-16, C-36

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]) -- generic "N/A" or blank is a fail | Completion Condition -- verifiable output or state that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK; blank where SLA evidence applies is a fail | States Contained (populated after Step 3) |
|-------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states. Minimum 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- specific event or predecessor state causing entry; "after previous step" does not count | Exit Transitions -- labeled outbound paths naming trigger and destination; "then continue" does not count | Owner (R-ID) -- must appear in Step 1; blank is a fail | Timing -- specific duration or N/A + reason | SLA Status (Normal / AT-RISK / Critical) |
|------|--------------|------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------|------------------------------------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

Minimum 3 states with timing. Minimum 1 AT-RISK.

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (measurable threshold -- qualifying types: dollar amount, day count, retry count, unit quantity; BOTH mechanisms required: (1) threshold-type category from the list above AND (2) quoted example with comparison operator and unit, e.g., "Invoice value > $10,000"; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met -- "otherwise" does not count | Fallback -- mechanism-impairment path (role unavailable, system down, config missing); names holding state or escalation target; "escalate" alone does not count |
|------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

For each phase, declare the exit gate using this structure:

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state that closes this phase]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID reached on clean exit]
Failure:        [T-ID or named exception triggered on exit failure]
Blocked by:     [C-ID(s) this gate enforces -- Mandatory; blank is a structural fail]
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
> until all exception flows are complete and every exception flow carries a **certified Handler
> R-ID** -- that is, an R-ID that traces to a role pre-certified as Exception Handler = Y in
> the Role Registry. An exception flow with an uncertified or blank Handler R-ID is a
> structural fail that blocks this gate.
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

**Table 8a -- SLA Annotations** (if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Target Duration -- specific (e.g., "5 business days"); "timely" does not count | At-Risk? (Y/N) | Risk Cause -- names the bottleneck |
|--------|--------------|--------------------------------------------------------------------------------|----------------|------------------------------------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

**Table 8b -- Breach Verdicts**:

| BV-ID | Phase (Ph-ID) | SLA Threshold (cite SLA-ID) | Breach (Y/N) | Cause (if Y: name the bottleneck or E-ID; "delays" alone is a fail) |
|-------|--------------|----------------------------|--------------|--------------------------------------------------------------------|
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
|----------------|-------------------------------------------------|-------------------------------|---------------------------------------|---------------------------------------|
| | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID (Exception Handler = Y in Step 1) | Risk if Uncovered -- specific consequence |
|-------|-----------|----------------------|-----------------------------------------------|------------------------------------------|
| PH-01 | | | | |

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header labeled "STEP 0A"; STEP 0B section header labeled "STEP 0B"; STEP 0A precedes STEP 0B in document order | Section headers | | |

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

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
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
| D-01 | Unterminated path: at least one path has no named T-ID | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner: D-table Owner R-ID not in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: category enumeration present; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; no category enumeration | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of SECONDARY/DERIVED typed code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record has Initial State column but no Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or blocks merged | C-42, AC-03 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL status is a
> structural fail -- it produces a lifecycle trace containing at least one defect named in the
> Defect Type column (an unterminated path, an uncertified exception handler, a missing Initial
> Phase field, unlabeled pre-schema blocks, or a generic escape code in a downstream trace
> column) -- and that artifact must be discarded and rerun from the failing step before it is
> filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-20.
> (2) Check V shows CLOSED.

---

## V-02 -- Phrasing Register: Typed Escape Codes as Production Actions

**Variation axis:** Phrasing register -- all instructions use second-person imperative verbs
("Write", "Name", "State", "List", "Confirm") rather than modal obligation ("must", "is
required to", "should carry"). The phrasing shifts the author from compliance-check mode to
production mode. The primary new v13 target is C-44: SECONDARY and DERIVED escape codes are
framed as production actions the author takes ("write SECONDARY:[rationale] when the role
exists for reasons outside the lifecycle trigger scope") rather than validation rules applied
after the fact. STEP 0A / STEP 0B labels satisfy C-42 via imperative instructions that
sequence the two tasks ("write STEP 0A first; do not open STEP 0B until 0A is complete").
C-43 is satisfied by the explicit imperative "write an Initial Phase field for every LT-ID."
The R12 floor is maintained; Gate D uses "certified Handler R-ID" for C-45.

**Hypothesis:** C-44 is the criterion most sensitive to phrasing register. A preamble rule
("the LT-ID Trace column must use SECONDARY:rationale rather than N/A") is encountered once
and may be forgotten by the time the author reaches step 1, row 6. An imperative instruction
embedded at the step where the author is filling the column ("write SECONDARY:[rationale] for
any role that exists outside all LT-ID scopes -- not N/A, not blank") is encountered at the
exact moment the author needs it. The prediction: imperative-register prompts at point of use
reduce the generic-escape-code defect (D-06) more reliably than preamble rule blocks, because
the rule is active precisely when the authorial decision is being made.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Follow every step in writing order. Complete each step before
opening the next.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Write STEP 0A before writing STEP 0B. Name every external event, role action, or time
condition that can initiate this lifecycle. For each trigger, write four fields.

For the Trigger Source field: write exactly one of "System Event", "Role Action", or "Time
Condition." Do not invent other categories.

For the Initial Phase field: write the name of the phase this trigger activates. If the
trigger enters an already-open phase at a mid-run point, write that containing phase. Do not
leave this field blank -- a lifecycle trigger that activates no phase is undefined.

| LT-ID | Trigger Description | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase |
|-------|--------------------|------------------------------------------------------------|---------------|---------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Write minimum 3 rows. Do not open STEP 0B until this table is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Write STEP 0B after STEP 0A. For each structural defect category this schema defends against,
write one row. Name a gate domain that corresponds to a schema boundary (not a process
exception). Name the specific criterion or gate that closes the surface.

Write minimum 3 rows. Make sure no two rows describe the same defect category.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|----------------|------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Do not open Step 1 until this table is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Write the complete Role Registry before opening the Phase Index. Confirm at
> least one role carries Exception Handler = Y and every role has an LT-ID Trace value or a
> SECONDARY:rationale before proceeding.
> Blocked by: C-05, C-11, C-23, C-36

For each role this lifecycle requires, write one row. Follow these instructions per column:

- **Role Name**: Write a domain-qualified functional title -- the job title you would see on
  an org chart. Write "Senior Credit Analyst," not "Approver." Write "Procurement Manager,"
  not "Finance team."
- **Exception Handler (Y/N)**: Write Y for every role authorized to handle exception flows.
  Write N for all others. At least one Y is required. Do not leave blank.
- **LT-ID Trace**: Write the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase
  this role first appears. If the role exists for reasons outside every LT-ID's scope, write
  SECONDARY:[rationale] -- not "N/A," not blank. State the specific reason this role exists
  without an LT anchor.

| R-ID | Role Name | Domain | Exception Handler (Y/N) | LT-ID Trace (or SECONDARY:[rationale]) |
|------|----------|--------|------------------------|----------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Write minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Write the complete Phase Index before opening the State Trace. Name the entry
> trigger and completion condition for every phase. Confirm every Entry Trigger carries an
> LT-ID or DERIVED:rationale before proceeding.
> Blocked by: C-16, C-36

For each phase, write the event that opens it, the output that closes it, the SLA envelope,
and the condition under which the SLA is at risk.

For the Entry Trigger field: write the LT-ID from STEP 0A whose Initial Phase names this
phase. If the phase is derived from a combination of LT paths rather than initiated by a
single trigger, write DERIVED:[rationale naming which LT-IDs and how they combine to produce
this phase boundary]. Do not write "N/A" -- every phase has an initiation path, and the job
of this field is to name it.

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|----------------------------------------------|---------------------|-------------|----------|-----------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |

Write minimum 3 phases. Put at least 2 states per phase. Mark at least 1 phase AT-RISK.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Trace at least 6 named states across all phases. For each state, write the entry condition
(the specific event or predecessor state that causes entry -- not "after previous step"), the
exit transitions (labeled outbound paths naming trigger and destination -- not "then
continue"), the owner R-ID from Step 1, the timing, and the SLA status.

Write at least 3 states with timing values. Mark at least 1 AT-RISK.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

**Decision Points** -- write at least 3. For each decision condition, write both a named
threshold-type category (dollar amount, day count, retry count, or unit quantity) AND a quoted
example with a comparison operator and unit (e.g., "Invoice value > $10,000"). Writing only
a category name without an example is a fail. Writing only a quoted example without naming
a threshold type is a fail. Both are required simultaneously.

| D-ID | Decision Name | Condition (threshold type + quoted example, e.g., dollar amount: "Invoice value > $10,000") | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback |
|------|--------------|-------------------------------------------------------------------------------------------|-------------|----------------------|--------------------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- write at least 1 fork-join, or declare absence with a rationale:

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Confirm the State Trace and Decision
> Table are both complete and stable before opening the Exception Catalog. Exception flows
> name states and decisions by ID; state names changed after exceptions are authored produce
> untraceable references.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. Name a "Blocked by: [C-ID]" field in every gate -- leave no
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

Confirm GATE C is CLOSED. Write at least 3 exception flows. For each, write:

- **Handler R-ID**: Look up the role in Step 1. Confirm Exception Handler = Y before writing
  the R-ID. Do not write an R-ID for a role carrying N. Do not leave blank.
- **Trigger**: Name the condition that diverts from the happy path. Do not write "an error
  occurs" -- write the specific condition.
- **Divergence Phase/Step**: Name the states bypassed or added. Do not write "different path."
- **Recovery State**: Name the S-ID or T-ID the flow reaches. Do not write "resolved."

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y; blank or N-role is a structural fail) | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|---------|------------------------------------------------------------------------------|----------------------|---------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Confirm all exception flows carry a
> **certified Handler R-ID** before opening the Terminal Declaration. "Certified" means the
> R-ID traces to a role pre-certified as Exception Handler = Y in the Role Registry. A flow
> with an uncertified or blank Handler R-ID is a structural fail that blocks this gate.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

Confirm GATE D is CLOSED. Write at least 1 success terminal and 1 failure/cancel terminal.
For each terminal, list every S-ID and E-ID that reaches it -- do not leave "Reached From"
blank.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs) |
|------|--------------|----------------------------------|-------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy path + every E-ID) ends at a named T-ID. Mark CLOSED only when
> every path is individually confirmed. Check V CLOSED is required by the Production Gate
> alongside Coverage Scan PASS.

---

**STEP 7 -- EDGE CASE CATALOG**

Write at least 2 edge cases -- scenarios the lifecycle has no path for, distinct from
exceptions in Step 5. For each, name the specific scenario (not a category), the gap reason,
and the consequence.

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

Write at least 3 SLA annotation rows with specific durations. Mark at least 1 At-Risk = Y.

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|----------------|---------------|-----------|
| SLA-01 | | | | |
| SLA-02 | | | | |
| SLA-03 | | | | |

Write at least 1 breach verdict with Breach = Y and a named cause.

| BV-ID | Phase (Ph-ID) | SLA Threshold (SLA-ID) | Breach (Y/N) | Cause |
|-------|--------------|----------------------|-------------|-------|
| BV-01 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER**

Write at least 2 bottlenecks. Name the root-cause type and a specific element. Name the
downstream states or phases affected. Write a typed Breach Link (BV-ID, SLA-ID, or
SLA-ABSENT) -- do not write general language.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|----------------|-------|------------------|------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

Write at least 1 gap. Name the specific missing step, the reason it is required (regulatory
rule, handoff precondition, or system dependency -- not "best practice"), and the risk if
absent.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|-------------|---------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Write at least 1 cross-lifecycle dependency. Name the partner lifecycle specifically, the
direction, the fields passed, and the coupling state (blocking or advisory).

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State |
|----------------|------------------|----------|--------------|---------------|
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
| AC-03 | STEP 0A section header present and precedes STEP 0B section header in document order | Section order | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no row may share the same coverage claim as another row.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role in Step 1 carries LT-ID Trace or SECONDARY:[rationale] -- not N/A or blank | Step 1 table | | |
| AC-05 | Step 1 LT-ID Trace column header defines SECONDARY escape code inline | Step 1 header | | |
| AC-06 | Step 2 Entry Trigger column header defines DERIVED escape code inline | Step 2 header | | |
| AC-07 | Every exception Handler R-ID traces to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C (upstream) and Gate D (downstream) both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |

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
| D-03 | Unresolvable decision owner: D-table R-ID not present in Step 1 | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition: threshold-type category named; no quoted example with operator and unit | C-31, AC-10 |
| D-05 | Example-only decision condition: quoted example present; threshold-type category absent | C-31, AC-10 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field: LT record present without Initial Phase column | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or merged into one block | C-42, AC-03 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above -- and must be discarded and rerun from the failing step before it is filed or used.
>
> Write the artifact only when: (1) Coverage Scan PASS for AC-01 through AC-20 AND
> (2) Check V shows CLOSED.

---

## V-03 -- Lifecycle Emphasis: Phase-Primary Framing With Certification Gate Conditioning

**Variation axis:** Lifecycle emphasis -- phases are the primary scaffolding of the lifecycle
simulation. Before states, decisions, or exception flows are authored, the full phase
architecture is declared and exit gates are written with criterion-level anchors. The new v13
target for this variation is C-45: the downstream exception-catalog gate is framed as a
phase-completion condition, not merely a catalog-completeness check. The gate text reads "all
exception flows in a phase have a certified Handler R-ID before that phase's terminal
declaration is authored," making certification a per-phase closure requirement rather than a
global post-hoc scan. STEP 0A / STEP 0B labels satisfy C-42. Initial Phase in STEP 0A
satisfies C-43 by grounding the phase map before it is authored. SECONDARY/DERIVED escape
codes satisfy C-44 via phase-anchored column definitions. The full R12 floor is maintained.

**Hypothesis:** C-45 gains more structural force when it operates at phase granularity rather
than catalog granularity. A global gate ("all exception flows must have certified handlers
before terminal declarations are authored") can be satisfied by a last-minute bulk scan.
A per-phase gate ("PH-02's exception flows must carry certified Handler R-IDs before PH-02's
terminal states are authored") creates a rolling certification obligation that surfaces
uncertified handlers during phase authoring rather than at the end of the catalog. The
phase-primary axis also strengthens C-43: an Initial Phase field in STEP 0A is structurally
necessary for this variation because the phase map is authored from the LT inventory -- a
missing Initial Phase means the phase map cannot be opened.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Begin with the pre-schema framing blocks. Use phase architecture as the primary scaffold:
phases are declared before states, and each phase is completed -- including exception flows
and per-phase exit gate -- before the next phase is opened.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Enumerate every event, action, or condition that can initiate this lifecycle. Include the
phase each trigger activates -- this is the foundation for the Phase Index.

| LT-ID | Trigger Description | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase |
|-------|--------------------|------------------------------------------------------------|--------------|---------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows. Initial Phase is required for every row.

> Do not open STEP 0B until this table is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Map the structural defect categories this schema defends against to their gate domains and
closing criteria.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|----------------|------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. Failure surfaces must be orthogonal.

> Do not open Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until every role carries a domain-qualified title,
> an Exception Handler designation, and an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

| R-ID | Role Name (domain-qualified; generic labels are a fail) | Domain | Exception Handler (Y/N; at least one Y required; blank is a fail) | LT-ID Trace (name LT-ID(s) from STEP 0A, or write SECONDARY:[rationale] if role exists outside all LT scopes -- N/A and blank are fails) |
|------|--------------------------------------------------------|--------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open Phase authoring until the Phase Index is complete and every Entry
> Trigger carries an LT-ID or DERIVED:rationale.
> Blocked by: C-16, C-36

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]) | Completion Condition | SLA Envelope | SLA Risk (AT-RISK annotation required for >=1 phase) | States Contained |
|-------|-----------|----------------------------------------------|---------------------|-------------|-----------------------------------------------------|-----------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |

---

**PHASE AUTHORING -- Complete each phase in full before opening the next**

For each phase, write in this sequence:
1. Phase entry contract (states in this phase)
2. Decision points owned in this phase
3. Exception flows for this phase (Handler R-IDs must be certified before phase terminal is authored)
4. Phase exit gate with Blocked by: [C-ID]

**PHASE PH-01**

*States:*

| S-ID | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|-----------|----------------|-----------------|-------------|--------|-----------|
| S-01 | | | | | | |
| S-02 | | | | | | |

*Decisions (if any in this phase):*

| D-ID | Decision Name | Condition (threshold type + quoted example with operator and unit, e.g., "day count: PO age > 30 days"; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Met | Branch: Not Met | Fallback |
|------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------|----------------|---------|
| D-01 | | | | | | |

*Exception Flows for PH-01:*

> Certified Handler R-IDs must be assigned to all PH-01 exception flows before the
> downstream Gate D is checked for this phase.

| E-ID | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y; uncertified or blank is a structural fail) | Divergence Step | Recovery State or Terminal |
|------|--------------|---------|------------------------------------------------------------------------------------|----------------|---------------------------|
| E-01 | | | | | |

*Phase PH-01 Exit Gate:*

```
Phase:          PH-01:
Exit condition: [what must be true to close PH-01]
SLA envelope:   [from Phase Index]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [C-ID(s)]
```

---

*[Repeat the Phase Authoring structure for PH-02, PH-03, and all remaining phases]*

---

**PARALLEL PATHS** -- minimum 1 fork-join or explicit "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: All phases must have their state traces
> and decision tables complete and stable before the consolidated exception catalog is
> finalized. Per-phase exception flows may be drafted during phase authoring; finalization of
> E-IDs for cross-reference occurs here.
> Source: Phase Authoring --> Target: Consolidated Exception Catalog. Blocked by: C-30, C-32.

---

**CONSOLIDATED EXCEPTION CATALOG** (cross-phase index after all phases authored)

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- certified; Exception Handler = Y required; blank or uncertified is a structural fail) | Divergence | Recovery or Terminal |
|------|--------------|---------------|---------|------------------------------------------------------------------------------------------------------|-----------|---------------------|
| (index all E-IDs from phase authoring above) | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not author consolidated Terminal
> Declarations until every exception flow in the catalog carries a **certified Handler R-ID**
> tracing to a role with Exception Handler = Y in the Role Registry. A flow with an
> uncertified or blank Handler R-ID is a structural fail that blocks this gate.
> Source: Consolidated Exception Catalog --> Target: Terminal Declarations. Blocked by: C-32, C-45.

---

**TERMINAL DECLARATIONS**

GATE D must be CLOSED before this section is authored. Minimum 1 success + 1 failure/cancel.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs) |
|------|--------------|----------------------------------|-------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> For every traced path (happy path + every E-ID), confirm a named T-ID is the endpoint.
> CLOSED only when all paths individually confirmed. Required by Production Gate.

---

**EDGE CASE CATALOG** (minimum 2)

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence |
|-------|----------|--------------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**SLA ANNOTATION + BREACH VERDICTS** / **BOTTLENECK REGISTER** / **GAP REGISTER** /
**CROSS-LIFECYCLE HANDOFF** / **EXCEPTION COVERAGE AUDIT**

*(Carry forward identical structure from V-01 Steps 8-12)*

---

**COVERAGE SCAN** (same Group A / B / C structure as V-01 with identical AC-01 through AC-20
and Defect Type Taxonomy D-01 through D-08)

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> (an unterminated path, an uncertified exception handler, a missing Initial Phase field,
> unlabeled pre-schema blocks, or a generic escape code) -- and must be discarded and rerun
> from the failing step.
>
> Write only when: (1) Coverage Scan PASS for AC-01 through AC-20 AND (2) Check V shows CLOSED.

---

## V-04 -- Role Sequence + Output Format: Authority-First Registry with Full Inline Enforcement

**Variation axis:** Role sequence + output format (combined). Role registry with exception
handler pre-certification is the first schema section authored after STEP 0A/0B, and every
field-level rule for all four new v13 criteria is embedded inline in its column header or gate
text. The variation probes C-42 + C-43 + C-44 simultaneously: (a) STEP 0A and STEP 0B are
labeled section headers that sequence the authorship of the four-column LT inventory before
the failure surface taxonomy [C-42]; (b) the Initial Phase column header in STEP 0A carries
"Mandatory; blank is a structural fail" enforcement at point of entry [C-43]; (c) the LT-ID
Trace column header in Step 1 and the Entry Trigger column header in Step 2 each carry their
respective typed escape code definitions inline [C-44]. Gate D carries "certified Handler R-ID"
language for C-45.

**Hypothesis:** C-42, C-43, and C-44 form a single traceability chain: STEP 0A provides
LT-IDs --> Initial Phase fields bridge LT-IDs to the Phase Index --> the Phase Index Entry
Trigger column traces each phase to an LT-ID or carries DERIVED:rationale --> the Role
Registry LT-ID Trace column traces each role to an LT-ID or carries SECONDARY:rationale. The
full chain is only structurally visible when (a) STEP 0A is labeled and has four columns, (b)
Step 2 column header defines DERIVED:rationale, and (c) Step 1 column header defines
SECONDARY:rationale. When all three are embedded at point of use rather than in a preamble,
an author filling Step 2 row 3 sees the DERIVED escape code definition before entering a
value -- and an author filling Step 1 row 5 sees the SECONDARY escape code before entering a
value. The role-first ordering further reinforces C-44 by establishing the role registry's
traceability constraint before phases or states are authored.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Every field-level rule is embedded in the column header that
governs it. Work through every numbered step in order.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table before writing STEP 0B.

| LT-ID | Trigger Description -- names the specific event, role action, or time condition that initiates the lifecycle; "process begins" does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- the first state activated; generic name without lifecycle qualifier does not count | Initial Phase -- the phase boundary activated by this trigger; Mandatory; a blank Initial Phase cell is a structural fail regardless of how many other fields are populated |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not write STEP 0B until every STEP 0A row carries all four fields including Initial Phase.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Author this table before writing Step 1.

| FS-ID | Failure Surface -- structural defect category (not a process exception); two rows with the same category are not orthogonal and the second is a fail | Gate Domain -- the schema section or boundary this surface maps to; "general" does not count | Closed By (C-ID or Gate Label) -- specific criterion or gate; blank is a fail |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. All surfaces orthogonal.

> Do not write Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY (authored immediately after STEP 0A/0B)**

> **GATE A**: Do not open the Phase Index until Role Registry is complete, every role carries
> a domain-qualified title, every role has an Exception Handler designation, and every row
> carries an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

This is the first schema section. Pre-certifying exception handler authority here governs all
downstream Handler R-ID assignments.

| R-ID | Role Name -- domain-qualified title visible on an org chart (e.g., "Senior Credit Analyst", "Procurement Controller"); generic labels ("Approver", "Admin", "User") do not count and produce unresolvable decision owners | Domain -- process function, not org unit | Exception Handler (Y/N) -- Mandatory; Y = may appear as Handler R-ID in exception catalog; N = may not; at least one Y required; blank is a structural fail | LT-ID Trace -- write the LT-ID(s) from STEP 0A whose Initial State or Initial Phase includes this role; if the role exists outside all LT scopes, write SECONDARY:[rationale naming why this role exists without an LT anchor] -- generic "N/A" or blank is a structural fail |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until Phase Index is complete and every Entry
> Trigger carries an LT-ID or DERIVED:rationale.
> Blocked by: C-16, C-36

| Ph-ID | Phase Name | Entry Trigger (write the LT-ID from STEP 0A whose Initial Phase names this phase; if this phase is derived from a combination of LT paths, write DERIVED:[rationale naming which LT-IDs and how they combine] -- generic "N/A" or blank is a structural fail) | Completion Condition -- verifiable output; "work is done" does not count | SLA Envelope -- specific duration; "as soon as possible" does not count | SLA Risk -- breach condition + causal bottleneck; at least one row must be annotated AT-RISK; blank where SLA applies is a fail | States Contained |
|-------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------|
| PH-01 | | | | | | |
| PH-02 | | | | | | |
| PH-03 | | | | | | |

Minimum 3 phases; each must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states; minimum 2 per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- specific event or predecessor state; "after previous step" does not count | Exit Transitions -- labeled paths naming trigger and destination; "then continue" does not count | Owner (R-ID) -- from Step 1; blank is a fail | Timing | SLA Status |
|------|--------------|------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------|--------|-----------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (qualifying threshold types: dollar amount, day count, retry count, unit quantity; BOTH required: (1) named threshold type AND (2) quoted example with comparison operator and unit, e.g., "dollar amount: Contract value > $50,000"; neither alone is sufficient) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback (mechanism impairment: role unavailable / system down / config missing; names holding state or escalation; "escalate" alone does not count) |
|------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 or explicit "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Do not open the Exception Catalog until
> State Trace and Decision Table are both complete with stable IDs. Exception flows reference
> state and decision IDs; ID changes after catalog authoring produces untraceable references.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable closure condition]
SLA envelope:   [target duration from Step 2]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [C-ID(s) -- Mandatory; blank is a structural fail]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- specific condition; "an error occurs" does not count | Handler (R-ID) -- Must trace to Exception Handler = Y in Step 1; Mandatory; blank or uncertified role is a structural fail; roles carrying N may not appear here | Divergence Phase/Step -- specific states bypassed or added; "different path" does not count | Recovery State or Terminal -- named S-ID or T-ID; "resolved" does not count |
|------|--------------|---------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open Terminal Declarations until
> every exception flow carries a **certified Handler R-ID** -- an R-ID that traces to a role
> pre-certified as Exception Handler = Y in the Role Registry. An exception flow with an
> uncertified or blank Handler R-ID is a structural fail that blocks this gate.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION + CHECK V**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel -- "completed" does not count) | Reached From (all S-IDs and E-IDs; blank is a structural fail) |
|------|--------------|----------------------------------------------------------------|----------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> For each traced path (happy path + every E-ID): confirm named T-ID is the endpoint.
> CLOSED only when every path is individually confirmed. Required by Production Gate.

---

*(STEPS 7-12: Edge Case Catalog, SLA Annotation, Bottleneck Register, Gap Register,
Cross-Lifecycle Handoff, Exception Coverage Audit -- carry forward V-01 structure)*

---

**COVERAGE SCAN** (same Group A / B / C structure as V-01 with AC-01 through AC-20 and
Defect Type Taxonomy D-01 through D-08)

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- it produces a lifecycle trace containing at least one defect named in the
> Defect Type column -- and must be discarded and rerun from the failing step before it is
> filed or used.
>
> Write only when: (1) Coverage Scan PASS for AC-01 through AC-20 AND (2) Check V shows CLOSED.

---

## V-05 -- Lifecycle Emphasis + Phrasing Register + Inertia Framing: Full v13 Floor

**Variation axis:** Lifecycle emphasis + phrasing register + inertia framing (combined). This
variation targets all four new v13 criteria simultaneously and provides the maximum-density
floor for R13. The inertia framing axis adds a STATUS-QUO PROCESS DECLARATION before STEP 0A
and embeds "Status-Quo Gap" columns in the Phase Index and Bottleneck Register, naming how
the current process fails at each phase boundary and each bottleneck. Imperative verbs
throughout. Phase-primary authoring structure with per-phase exception flow certification.
All four new criteria are layered on top of the complete R12 V-05 floor.

**Hypothesis:** The inertia framing axis augments C-44 in a specific way: when the Phase
Index Entry Trigger column carries a Status-Quo Gap field alongside the DERIVED:rationale
escape code, an author filling a phase row that cannot trace to a single LT-ID is prompted
to explain both why the phase is derived AND why the current process misses this boundary.
The combination of DERIVED:rationale (which requires an LT combination explanation) and
Status-Quo Gap (which requires an as-is failure explanation) makes generic "N/A" entries
implausible at a structural level -- the author cannot fill both fields generically without
producing an obviously incomplete row. The prediction is that V-05's dual-column pressure on
the Entry Trigger field produces higher DERIVED:rationale specificity than variations that
carry only the escape code constraint.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Before authoring any schema section, complete the Status-Quo
Process Declaration and both pre-schema blocks. Use imperative verbs throughout. Complete each
step before opening the next.

---

**STATUS-QUO PROCESS DECLARATION**

Name the current process or system that this lifecycle replaces or augments. This declaration
is used as the incumbent comparison throughout the simulation.

| Field | Value |
|-------|-------|
| Incumbent process name | [Name of the as-is workflow or system currently used] |
| Adoption context | [Who uses it and at what scale -- team, volume, or geography] |
| Known failure mode FM-1 | [Specific named failure in the current process] |
| Known failure mode FM-2 | [Specific named failure in the current process] |
| Known failure mode FM-3 | [Specific named failure in the current process] |
| Primary inertia driver | [Why this process persists despite its failure modes] |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Write STEP 0A. For each trigger that can initiate this lifecycle, write four fields. Note
where the status-quo process fails to recognize or route this trigger -- this populates the
Status-Quo Gap column.

| LT-ID | Trigger Description | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase | Status-Quo Gap (does the incumbent process handle this trigger? If not, name the gap) |
|-------|--------------------|------------------------------------------------------------|--------------|---------------|--------------------------------------------------------------------------------------|
| LT-01 | | | | | |
| LT-02 | | | | | |
| LT-03 | | | | | |

Write minimum 3 rows. Initial Phase is required for every row. Do not open STEP 0B until complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Write STEP 0B after STEP 0A. For each structural defect category, write a failure surface
that names the gate domain and the criterion that closes it.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|----------------|------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

Minimum 3 rows. All surfaces orthogonal. Do not open Step 1 until complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Confirm every role has a domain-qualified title, an Exception Handler
> designation, and an LT-ID Trace or SECONDARY:[rationale] before opening the Phase Index.
> Blocked by: C-05, C-11, C-23, C-36

Write one row per role. Use these authoring rules:

- **Role Name**: Write the specific title used on an org chart. Write "Tax Provision Manager,"
  not "Finance." Write "Customer Operations Lead," not "Support team."
- **Exception Handler**: Write Y or N. At least one Y. A blank is a fail.
- **LT-ID Trace**: Write the LT-ID(s) from STEP 0A. If the role exists outside LT scope, write
  SECONDARY:[rationale] -- state why this role exists without any LT anchor. "N/A" is a fail.
- **Incumbent Counterpart**: Write the role name in the status-quo process, or "No counterpart"
  if this role is net-new.

| R-ID | Role Name | Domain | Exception Handler (Y/N) | LT-ID Trace (or SECONDARY:[rationale]) | Incumbent Counterpart |
|------|----------|--------|-----------------------|----------------------------------------|-----------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| R-03 | | | | | |

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Confirm every Entry Trigger carries an LT-ID or DERIVED:[rationale] before
> opening Phase authoring.
> Blocked by: C-16, C-36

For each phase, write the entry trigger and status-quo gap. If the phase entry cannot trace
to a single LT-ID, write DERIVED:[rationale naming the LT-IDs and their combination logic].
Do not write "N/A" -- every phase has an initiation path.

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]) | Completion Condition | SLA Envelope | SLA Risk (>=1 AT-RISK required) | Status-Quo Gap (how the incumbent process fails at this phase boundary) | States Contained |
|-------|-----------|----------------------------------------------|---------------------|-------------|--------------------------------|-------------------------------------------------------------------------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states; minimum 2 per phase; minimum 3 with timing; minimum 1 AT-RISK.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status | Incumbent Delta (how status-quo process handles or misses this state) |
|------|--------------|------------|----------------|-----------------|-------------|--------|-----------|----------------------------------------------------------------------|
| S-01 | | | | | | | | |
| S-02 | | | | | | | | |
| S-03 | | | | | | | | |

**Decision Points** -- write at least 3. Write both a threshold-type category AND a quoted
example with comparison operator and unit. Neither alone satisfies the requirement.

| D-ID | Decision Name | Condition (threshold type: dollar amount / day count / retry count / unit quantity; AND quoted example, e.g., "day count: Age > 30 days"; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Met | Branch: Not Met | Fallback | Incumbent Equivalent (how the current process makes this decision, or "No equivalent") |
|------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------|----------------|---------|--------------------------------------------------------------------------------------|
| D-01 | | | | | | | |
| D-02 | | | | | | | |
| D-03 | | | | | | | |

**Parallel Paths** -- write at least 1 or declare absence with rationale. Note whether the
status-quo process has an equivalent parallel path:

```
Fork (S-ID):       [branching state]
Branch A:          [concurrent path]
Branch B:          [concurrent path]
Join condition:    [what must hold before merge]
Merge owner:       [R-ID]
Incumbent join:    [does the status-quo process have a join? If so, name it; if not, state the gap]
```

> **GATE C -- Upstream Exception-Catalog Boundary**: Confirm State Trace and Decision Table
> complete and stable before opening the Exception Catalog.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. Confirm "Blocked by: [C-ID]" is present in every gate.

```
Phase:              [Ph-ID: Phase Name]
Exit condition:     [verifiable closure condition]
SLA envelope:       [target duration from Step 2]
Success:            [Ph-ID or T-ID]
Failure:            [T-ID or exception name]
Blocked by:         [C-ID(s) -- Mandatory; blank is a structural fail]
Incumbent exit:     [how the status-quo process closes this phase, or "No equivalent gate"]
```

---

**STEP 5 -- EXCEPTION CATALOG**

Confirm GATE C CLOSED. Write at least 3 exception flows. For each Handler R-ID, confirm
Exception Handler = Y in Step 1 before writing the ID.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y; uncertified or blank is a structural fail) | Divergence | Recovery or Terminal | As-Is Detection? (Y/N -- does the incumbent process detect this exception?) |
|------|--------------|---------------|---------|-----------------------------------------------------------------------------------|-----------|---------------------|----------------------------------------------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Confirm every exception flow carries a
> **certified Handler R-ID** -- an R-ID tracing to a role pre-certified as Exception Handler
> = Y in the Role Registry -- before opening Terminal Declarations. An exception flow with an
> uncertified or blank Handler R-ID is a structural fail that blocks this gate.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

Confirm GATE D CLOSED. Write at least 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From | Incumbent Terminal? (Y/N -- does the status-quo process have an equivalent outcome?) |
|------|--------------|----------------------------------|-------------|--------------------------------------------------------------------------------------|
| T-01 | | | | |
| T-02 | | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each traced path (happy path + every E-ID) ends at a named T-ID. Mark CLOSED only
> when every path is individually confirmed. Required by Production Gate.

---

**STEP 7 -- EDGE CASE CATALOG** (minimum 2; distinct from Step 5)

| EC-ID | Edge Case | Phase (Ph-ID) | Gap Reason | Consequence | Incumbent Handling (how current process addresses this, or "Not addressed") |
|-------|----------|--------------|-----------|------------|-----------------------------------------------------------------------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [reason]
```

**Table 8a** (minimum 3 rows; minimum 1 At-Risk = Y):

| SLA-ID | S-ID or Ph-ID | Target Duration | At-Risk? (Y/N) | Risk Cause | As-Is Typical Duration |
|--------|--------------|----------------|---------------|-----------|----------------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

**Table 8b** (minimum 1 Breach = Y with named cause):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause |
|-------|--------------|--------------|-------------|-------|
| BV-01 | | | | |

---

**STEP 9 -- BOTTLENECK REGISTER** (minimum 2)

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause (root-cause type + element) | Downstream Impact (S-IDs or Ph-IDs + consequence type) | Breach Link | Incumbent Workaround (how current process compensates for this bottleneck) |
|------|--------------|----------------|----------------------------------|-------------------------------------------------------|------------|--------------------------------------------------------------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**STEP 10 -- GAP REGISTER** (minimum 1)

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|-------------|---------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF** (minimum 1)

| Handoff Trigger | Partner Lifecycle | Direction | Fields Passed | Coupling State | As-Is gap (Y/N) |
|----------------|-----------------|----------|--------------|---------------|----------------|
| | | | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|-----------|----------------------|-------------|------------------|
| PH-01 | | | | |

---

**COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A has >=3 LT-IDs; every row carries all four fields: Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B has >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A labeled "STEP 0A" and STEP 0B labeled "STEP 0B" as visible section headers; STEP 0A precedes STEP 0B | Section headers | | |
| AC-04 | Status-Quo Process Declaration present with incumbent name, adoption context, >=3 named failure modes, and inertia driver | Declaration block | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: each row verified by distinct schema evidence; no cell may
share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-05 | Every role carries LT-ID Trace or SECONDARY:[rationale] -- not N/A or blank | Step 1 table | | |
| AC-06 | Step 1 LT-ID Trace column header defines SECONDARY escape code inline with eligibility condition | Step 1 header | | |
| AC-07 | Step 2 Entry Trigger column header defines DERIVED escape code inline with eligibility condition | Step 2 header | | |
| AC-08 | All exception Handler R-IDs trace to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-09 | Handler column header co-locates backward-trace authority rule and fail-declaration | Step 5 header | | |
| AC-10 | Gate D uses "certified Handler R-ID" language tying gate completion to registry's Exception Handler = Y | Gate D text | | |
| AC-11 | Decision Condition column header carries BOTH threshold-type category list AND quoted example | Step 3 D-table header | | |
| AC-12 | Each phase exit gate carries "Blocked by: [C-ID]" as a named structured field | Step 4 gates | | |
| AC-13 | Gate C (upstream) and Gate D (downstream) both present, each naming source and target | Gate C + D | | |
| AC-14 | Check V present with OPEN/CLOSED status; named as co-equal Production Gate condition | Step 6 + gate | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-15 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-16 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-17 | >=1 success + >=1 failure/cancel terminal; all traced paths reach named T-ID | Step 6 | | |
| AC-18 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-19 | >=3 decisions with measurable threshold, owner, all branches, fallback | Step 3 | | |
| AC-20 | >=3 states with timing; >=1 AT-RISK phase with causal bottleneck | Steps 3 + 2 | | |
| AC-21 | >=1 cross-lifecycle handoff with partner, direction, fields, coupling state | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path: at least one traced path has no named T-ID | C-03, C-14, AC-17, Check V |
| D-02 | Uncertified exception handler: Handler R-ID does not trace to Exception Handler = Y | C-21, C-23, AC-08 |
| D-03 | Unresolvable decision owner: D-table R-ID not in Step 1 | C-05, C-07, AC-19 |
| D-04 | Taxonomy-only decision condition: threshold-type category named; no quoted example with operator and unit | C-31, AC-11 |
| D-05 | Example-only decision condition: quoted example present; threshold-type category absent | C-31, AC-11 |
| D-06 | Generic escape code: LT-ID Trace or Entry Trigger uses "N/A" or blank instead of typed SECONDARY/DERIVED code | C-44, AC-05, AC-06, AC-07 |
| D-07 | Missing Initial Phase field: LT record present without Initial Phase column or with blank Initial Phase cell | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks: STEP 0A / STEP 0B section headers absent or blocks merged into one undifferentiated block | C-42, AC-03 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing Initial Phase field,
> unlabeled pre-schema blocks, a generic escape code in a downstream trace column, or a
> decision condition without both mechanisms) -- and must be discarded and rerun from the
> failing step before it is filed or used.
>
> Write only when: (1) Coverage Scan PASS for AC-01 through AC-21 AND (2) Check V shows CLOSED.
