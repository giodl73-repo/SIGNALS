---
skill: flow-lifecycle
round: 15
rubric-version: v15
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v15-2026-03-16.md
floor: flow-lifecycle-variate-R14-2026-03-16.md V-05
---

# flow-lifecycle -- Round 15 Variations (rubric v15: C-48, C-49)

Round 15 holds the R14 V-05 full floor and probes two new aspirational criteria that extend
the STATUS-QUO PROCESS DECLARATION architecture in different directions:

- **C-48 -- Per-Field Anti-Pattern Vocabulary in SQ Declaration**: Every field definition in
  the STATUS-QUO PROCESS DECLARATION table carries at least one inline anti-pattern token
  ("does not count," "Mandatory," or "is a fail") specific to that field's content expectations.
  The anti-pattern vocabulary is embedded inside the field definition cell itself -- not in a
  preamble block before the table and not collected in a trailing rules section. A field
  definition row with no inline anti-pattern token is a per-field enforcement gap, distinct
  from D-09 (declaration absent) and D-10 (FM-ID-free), because the declaration exists and
  the FM-IDs are assigned but the field provides no point-of-use guidance about what a bad
  entry looks like.

- **C-49 -- Mutual-Audit Relationship Named as Design Principle in Status-Quo Gap Header**:
  The Status-Quo Gap column header explicitly names the mutual-audit relationship between Entry
  Trigger and Status-Quo Gap AS A DESIGN PRINCIPLE -- using language such as "mutual-audit
  design principle," "mutual-audit relationship," or an equivalent formulation that frames the
  co-auditing behavior as an intentional architectural decision rather than an incidental
  structural observation. The R14 V-02 floor carries "these two columns audit each other" in
  the column header (C-47 pass), but C-49 requires the named principle designation: the
  relationship is not merely noted -- it is declared as the design intent behind the column
  co-location.

**Invariants across all five variations**: All variations carry the complete R14 V-05 floor --
C-27 (scan defect taxonomy with named Defect Type column referenced in gate), C-28 (Handler
column co-locates backward-trace authority rule and fail-declaration), C-29/C-31 (dual-mechanism
Decision Condition column header: threshold-type category list + quoted example), C-30/C-32
(bidirectional exception-catalog gates, upstream and downstream), C-33 (Step 0 LT inventory),
C-34 (failure surface taxonomy), C-35 (non-overlapping evidence mandate), C-36 (LT-ID trace
cascade in role registry and phase index), C-42 (STEP 0A / STEP 0B sequential labeling),
C-43 (Initial Phase field in LT records), C-44 (typed escape-code vocabulary: SECONDARY and
DERIVED), C-45 (downstream exception-catalog gate uses "certified Handler R-ID" language),
C-46 (STATUS-QUO PROCESS DECLARATION before STEP 0A with >=2 FM-IDs and inertia driver),
C-47 (Phase Index carries Status-Quo Gap column co-located with Entry Trigger; each row names
a specific FM-ID from C-46).

**R15 failure modes to probe:**

| Mode | Criterion | What R14 V-05 does | What v15 requires |
|------|-----------|-------------------|------------------|
| Field-level enforcement gap | C-48 | SQ Declaration table present with FM-IDs; no per-field anti-pattern tokens inside field definitions | Every field row carries at least one inline "does not count" / "Mandatory" / "is a fail" token specific to that field |
| Missing design-principle designation | C-49 | Status-Quo Gap column header notes the auditing relationship structurally ("these two columns audit each other") | Column header names the relationship AS A DESIGN PRINCIPLE using "mutual-audit design principle" or equivalent language |
| Preamble-collected anti-pattern | C-48 | Anti-pattern rules appear in a block above the SQ Declaration table; individual field rows have no inline tokens | Each field row self-describes its failure modes inline -- a practitioner filling only that row encounters the constraint |
| Unnamed architectural intent | C-49 | Mutual-audit behavior described as a property; no designation as an intentional design decision | The word "principle" or "design intent" or "by design" appears in the header, naming the relationship as deliberate architecture |

**Round 15 hypothesis matrix:**

| Variation | C-48 (SQ Field Anti-Pattern) | C-49 (Named Design Principle) | Axis |
|-----------|:----------------------------:|:-----------------------------:|------|
| V-01 | TARGET | HOLD | Inertia Framing |
| V-02 | HOLD | TARGET | Output Format |
| V-03 | FAIL | PARTIAL | Phrasing Register |
| V-04 | PARTIAL | PARTIAL | Role Sequence + Lifecycle Emphasis |
| V-05 | TARGET | TARGET | Inertia Framing + Output Format |

---

## V-01 -- Inertia Framing: Per-Field Anti-Pattern Vocabulary Embedded in SQ Declaration

**Variation axis:** Inertia framing -- every field row in the STATUS-QUO PROCESS DECLARATION
carries inline anti-pattern vocabulary specific to that field. The field definition cell is
the enforcement unit: a practitioner filling a single row encounters the constraint for that
field without needing to recall a preamble rule. C-49 is held at the R14 V-02 floor level
(the Status-Quo Gap column header notes that "these two columns audit each other" but does not
name the relationship as a design principle). STEP 0A / STEP 0B labels satisfy C-42. Initial
Phase satisfies C-43. SECONDARY / DERIVED typed escape codes satisfy C-44. Gate D uses
"certified Handler R-ID" for C-45. C-46 and C-47 carry at full R14 floor. The new R15 probe
is C-48: every SQ Declaration field definition contains at least one "does not count" or
"is a fail" or "Mandatory" token that is specific to the content type expected in that field.

**Hypothesis:** C-48 fails when the SQ Declaration is treated as a header block -- authors
read the preamble rule ("name the failure mode, not just a category") and then fill the
table without the rule present at the field level. When the failure-mode field definition
itself says "error-prone or inefficient does not count; name the specific missing detection
mechanism," the anti-pattern vocabulary is encountered at the exact moment the author is
deciding what to write. Per-field inline enforcement converts the constraint from a remembered
rule to a visible production requirement. Prediction: per-field embedding reduces D-10
(FM-ID-free failure mode) and its C-48 variant (present FM-ID, absent constraint signal)
more reliably than equivalent preamble language.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read every field
definition before filling that row -- field definitions carry their own enforcement vocabulary
inline; there are no separate preamble rule blocks.

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs defined here are required fields in the Phase Index
Status-Quo Gap column. A Phase Index cell with no FM-ID from this block is structurally
unanchored and is a fail.

| SQ-Field | Content |
|----------|---------|
| Incumbent Process -- names the specific named process, tool, or workaround being replaced; writing "manual process" without naming the specific tool does not count; naming a department or team without naming the process does not count; a single-word tool name without context does not count | |
| FM-01 -- first failure mode: names the specific condition or gap the incumbent fails to detect or prevent; "error-prone," "inefficient," or "slow" does not count; a generic category name without a missing detection or prevention mechanism does not count; must carry the identifier FM-01 | |
| FM-02 -- second failure mode: must be orthogonal to FM-01; a failure mode that is a restatement, subcategory, or consequence of FM-01 is a fail; must carry the identifier FM-02; "same as FM-01 in a different phase" is a fail | |
| Inertia Driver -- names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count; a reason that would also apply to every other legacy process does not count; Mandatory | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" or "a request is received" does not count; name the specific initiating signal | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; a generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail; if the trigger enters an existing phase mid-run, name that containing phase |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary] -- generic "N/A" or blank is a fail) | Status-Quo Gap (FM-ID from STATUS-QUO PROCESS DECLARATION -- names which incumbent failure mode this phase's entry trigger addresses; these two columns audit each other: a cell with no FM-ID reference is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------|
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
|------|--------------|----------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
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

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A present with >=3 LT-IDs; each row carries Trigger Description, Trigger Source, Initial State, AND Initial Phase | STEP 0A table | | |
| AC-02 | STEP 0B present with >=3 failure surfaces; each row carries Failure Surface, Gate Domain, Closed By | STEP 0B table | | |
| AC-03 | STEP 0A section header labeled "STEP 0A"; STEP 0B section header labeled "STEP 0B"; STEP 0A precedes STEP 0B in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; block names Incumbent Process, FM-01 with identifier, FM-02 with identifier, and Inertia Driver | SQ Declaration block | | |
| AC-23 | Every field row in the STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token ("does not count," "Mandatory," or "is a fail") specific to that field's content type -- a field definition with no inline anti-pattern token is a per-field enforcement gap | SQ Declaration field definitions | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no
cell may share the same coverage claim across these rows.

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
| D-14 | Per-field anti-pattern gap: SQ Declaration present with FM-IDs assigned but at least one field definition row carries no inline anti-pattern token ("does not count," "Mandatory," or "is a fail") -- the field is present but provides no point-of-use enforcement | C-48, AC-23 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, a per-field anti-pattern gap in the SQ Declaration, an unanchored
> status-quo gap, a DERIVED-only or gap-column-only Phase Index, a missing Initial Phase field,
> unlabeled pre-schema blocks, or a generic escape code in a downstream trace column) -- and
> that artifact must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-23.
> (2) Check V shows CLOSED.

---

## V-02 -- Output Format: Mutual-Audit Design Principle Named in Status-Quo Gap Header

**Variation axis:** Output format -- the Phase Index table structure is the primary carrier of
C-49 enforcement. The Status-Quo Gap column header explicitly names the mutual-audit
relationship AS A DESIGN PRINCIPLE, framing the co-auditing behavior between Entry Trigger
and Status-Quo Gap as an intentional architectural decision rather than an incidental property
of adjacent columns. The STATUS-QUO PROCESS DECLARATION is held at the R14 V-01 floor level
for C-48: the Incumbent Process and FM fields carry inline anti-pattern vocabulary but the
Inertia Driver field does not (C-48 PARTIAL -- one field enforcement gap). STEP 0A / STEP 0B
labels satisfy C-42. Initial Phase satisfies C-43. SECONDARY / DERIVED typed codes satisfy
C-44. Gate D satisfies C-45. C-46 and C-47 carry at full R14 floor.

**Hypothesis:** C-49 fails when the mutual-audit relationship is described as a structural
observation rather than a design declaration. R14 V-02 uses "these two columns audit each
other" -- which is accurate but passive: it describes what the columns do, not why they were
designed that way. When the column header names the relationship as "mutual-audit design
principle" or equivalent, it signals that the co-location is intentional architecture: the
author must honor both columns because the schema was designed so that incompleteness in one
column is structurally exposed by the other. The prediction: naming the design principle
elevates practitioner compliance beyond rule-following to intent-honoring, reducing D-11
(unanchored status-quo gap) by making the architectural motivation visible at point of use.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Column headers carry
all field rules inline.

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs defined here are required fields in the Phase Index
Status-Quo Gap column.

| Field | Content |
|-------|---------|
| Incumbent Process -- names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department alone does not count | |
| FM-01 -- first failure mode: names the specific condition the incumbent fails to detect or prevent; "error-prone" or "inefficient" does not count; must name the missing detection or prevention mechanism; assign identifier FM-01 | |
| FM-02 -- second failure mode orthogonal to FM-01; must not overlap or be a consequence of FM-01; assign identifier FM-02 | |
| Inertia Driver -- the organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02 | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

| LT-ID | Trigger Description -- names the external event, role action, or time condition; "process begins" does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition) | Initial State -- first state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail |
|-------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete and every row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; two rows naming the same category are not orthogonal and the second is a fail | Gate Domain -- schema section or structural boundary; "general" does not count | Closed By (C-ID or Gate Label) -- specific criterion or gate; blank is a fail |
|-------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
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

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor"); generic labels do not count | Domain -- process function; org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; at least one Y required; blank is a fail | LT-ID Trace -- LT-ID(s) in whose Initial State or Initial Phase this role appears; if outside all LT scopes write SECONDARY:[rationale]; "N/A" or blank is a fail |
|------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete, every Entry Trigger
> carries an LT-ID or DERIVED:rationale, and every Status-Quo Gap cell names a specific FM-ID.
> Blocked by: C-16, C-36, C-47

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary]; generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: the Entry Trigger and this column are co-designed as a mutual-audit pair -- a generic DERIVED:rationale in Entry Trigger simultaneously produces a vague gap here with no FM-ID reference, making incompleteness visible as a co-occurring defect in a single row scan; this mutual exposure is the design intent, not a coincidence of column placement; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase addresses; a cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state; "work is done" does not count | SLA Envelope -- specific duration; "as soon as possible" does not count | SLA Risk -- breach condition + causal bottleneck; at least one phase must be annotated AT-RISK | States Contained |
|-------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- specific event or predecessor state; "after previous step" does not count | Exit Transitions -- labeled outbound paths naming trigger and destination | Owner (R-ID) | Timing | SLA Status (Normal / AT-RISK / Critical) |
|------|--------------|------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------|--------|------------------------------------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (both mechanisms required: (1) threshold-type category -- dollar amount, day count, retry count, unit quantity -- AND (2) quoted example with comparison operator and unit; category-only is a fail; example-only is a fail) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback -- mechanism-impairment path; names holding state or escalation target |
|------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------|--------------------------|---------------------------------------------------------------------------------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 fork-join or "No parallel paths -- [rationale]":

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

> **GATE C**: Do not open the Exception Catalog until State Trace and Decision Table are
> both complete and stable. Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [C-ID(s) -- Mandatory; blank is a structural fail]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- specific condition; "an error occurs" does not count | Handler (R-ID) -- Must trace to a role with Exception Handler = Y in Step 1; Mandatory; blank or uncertified role is a structural fail | Divergence Phase/Step | Recovery State or Terminal -- named S-ID or T-ID |
|------|--------------|----------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D**: Do not open Terminal Declaration until all exception flows carry a **certified
> Handler R-ID** tracing to Exception Handler = Y in the Role Registry.
> Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel -- "completed" does not count) | Reached From (all S-IDs and E-IDs; blank is a structural fail) |
|------|--------------|------------------------------------------------------------------|----------------------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm each path (happy + every E-ID) reaches a named T-ID. CLOSED only when every path
> is individually confirmed. Check V CLOSED is co-equal Production Gate condition.

---

**STEPS 7-12** -- Same structure as V-01: EDGE CASE CATALOG (min 2), SLA ANNOTATION,
BOTTLENECK REGISTER (min 2), GAP REGISTER (min 1), CROSS-LIFECYCLE HANDOFF (min 1),
EXCEPTION COVERAGE AUDIT. Column headers and field rules identical to V-01.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A: >=3 LT-IDs; every row carries Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B: >=3 failure surfaces; every row carries Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A header precedes STEP 0B header in document order | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION before STEP 0A; Incumbent Process, FM-01 (with identifier), FM-02 (with identifier), Inertia Driver all present | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no cell may share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role: domain-qualified title, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 table | | |
| AC-05 | LT-ID Trace column header defines SECONDARY typed escape code inline | Step 1 header | | |
| AC-06 | Entry Trigger column header defines DERIVED typed escape code inline | Step 2 header | | |
| AC-07 | Every exception Handler R-ID traces to Exception Handler = Y in Step 1 | Step 5 table | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 gates | | |
| AC-12 | Gate C and Gate D both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Phase Index Status-Quo Gap column co-located with Entry Trigger; column header names the mutual-audit relationship as a design principle; each row carries a specific FM-ID | Step 2 header + table | | |
| AC-24 | Status-Quo Gap column header uses "mutual-audit design principle" or equivalent named-principle language -- a structural observation that the columns audit each other without naming the relationship as an intentional design principle does not pass | Step 2 column header | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with threshold, owner, branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff | Step 11 | | |

**Defect Type Taxonomy:**

| Defect-ID | Defect Type | Detected By |
|-----------|-------------|-------------|
| D-01 | Unterminated path | C-03, C-14, AC-16, Check V |
| D-02 | Uncertified exception handler | C-21, C-23, AC-07 |
| D-03 | Unresolvable decision owner | C-05, C-07, AC-18 |
| D-04 | Taxonomy-only decision condition | C-31, AC-10 |
| D-05 | Example-only decision condition | C-31, AC-10 |
| D-06 | Generic escape code | C-44, AC-04, AC-05, AC-06 |
| D-07 | Missing Initial Phase field | C-43, AC-01 |
| D-08 | Unlabeled pre-schema blocks | C-42, AC-03 |
| D-09 | Missing SQ Declaration | C-46, AC-21 |
| D-10 | FM-ID-free failure mode | C-46, AC-21 |
| D-11 | Unanchored status-quo gap | C-47, AC-22 |
| D-12 | DERIVED-only Phase Index | C-47, AC-22 |
| D-13 | Gap-column-only Phase Index | C-44, C-47, AC-06, AC-22 |
| D-15 | Unnamed mutual-audit design principle: Status-Quo Gap column present and auditing relationship noted but not named as a design principle in the column header -- "these two columns audit each other" without principle designation does not pass | C-49, AC-24 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, an unnamed mutual-audit design principle, an unanchored status-quo
> gap, a DERIVED-only or gap-column-only Phase Index, a missing Initial Phase field, unlabeled
> pre-schema blocks, or a generic escape code) -- and must be discarded and rerun from the
> failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-24.
> (2) Check V shows CLOSED.

---

## V-03 -- Phrasing Register: Imperative Voice (C-48 FAIL, C-49 PARTIAL)

**Variation axis:** Phrasing register -- all instructions use second-person imperative verbs
("Write", "Name", "State", "Confirm", "Do not write") throughout. The STATUS-QUO PROCESS
DECLARATION is framed as prose production instructions rather than a table with inline field
definitions: the author receives verb-led directives ("Write the incumbent process name. Do
not write 'manual process' -- write the specific tool or workflow.") but the field cells
themselves carry no inline anti-pattern tokens (C-48 FAIL: prose instructions only, not
per-field embedded vocabulary). The Status-Quo Gap mutual-audit relationship is mentioned in
an introductory sentence before the Phase Index table but the column header itself does not
carry the design-principle designation (C-49 PARTIAL: relationship noted but not named as
design principle in the header).

**Hypothesis:** Imperative register reduces compliance failures caused by passive-reading drift
-- authors skim declarative rules and fill cells based on intent rather than the stated
constraint. When the instruction is a verb command encountered at the step boundary, compliance
rate increases for straightforward requirements. However, C-48 requires anti-pattern vocabulary
embedded in the field definition itself (the table cell, not the instruction block above it),
and C-49 requires the design-principle designation to appear in the column header specifically.
Imperative prose instructions do not satisfy either criterion's point-of-use placement
requirement. Prediction: V-03 shows strong compliance on C-01 through C-47 criteria (imperative
voice is effective for procedural requirements) but fails C-48 and partially satisfies C-49
because the placement constraints cannot be met through prose framing alone.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Complete each step before opening the next. Follow every imperative
instruction at the step where it appears.

---

### STATUS-QUO PROCESS DECLARATION

Write this block before writing STEP 0A.

Name the incumbent process being replaced. Do not write "manual process" -- write the specific
named process, tool, or workflow that this lifecycle replaces or improves upon.

Write FM-01: name the specific condition the incumbent fails to detect or prevent. Assign the
identifier FM-01. Do not write "error-prone" or "slow" -- name the specific missing detection
or prevention mechanism.

Write FM-02: name a second failure mode that is orthogonal to FM-01. Assign identifier FM-02.
Do not write a failure mode that is a consequence or subcategory of FM-01.

Write the inertia driver: name the specific organizational, systemic, or economic reason the
incumbent persists despite FM-01 and FM-02.

| Field | Value |
|-------|-------|
| Incumbent Process | |
| FM-01 | |
| FM-02 | |
| Inertia Driver | |

The FM-01 and FM-02 identifiers are required in the Phase Index Status-Quo Gap column. Do not
open STEP 0A until this block is complete.

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Write STEP 0A before writing STEP 0B. For each event, role action, or time condition that can
start this lifecycle, write one row. Write at least 3 rows.

For Trigger Source: write exactly "System Event", "Role Action", or "Time Condition." Do not
invent other categories.

For Initial Phase: name the phase this trigger activates. Do not leave this field blank.

| LT-ID | Trigger Description | Trigger Source | Initial State | Initial Phase |
|-------|---------------------|----------------|---------------|---------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

> Do not write STEP 0B until every STEP 0A row carries all four fields.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

Write STEP 0B before writing Step 1. Name at least 3 structural defect surfaces. Confirm each
pair is orthogonal before adding a row -- two surfaces naming the same defect category are not
orthogonal.

| FS-ID | Failure Surface | Gate Domain | Closed By |
|-------|-----------------|-------------|-----------|
| FS-01 | | | |
| FS-02 | | | |
| FS-03 | | | |

> Do not write Step 1 until STEP 0B is complete.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

> **GATE A**: Do not open the Phase Index until the Role Registry is complete, all roles carry
> domain-qualified titles, every role has an Exception Handler designation, and every role has
> an LT-ID Trace or SECONDARY:rationale.
> Blocked by: C-05, C-11, C-23, C-36

Write each role with a domain-qualified title. Do not write "Approver" or "User" -- write the
functional role name qualified by the business domain (e.g., "AR Collections Specialist").

Mark Exception Handler Y or N for every role. At least one role must carry Y.

| R-ID | Role Name | Domain | Exception Handler (Y/N) | LT-ID Trace or SECONDARY:[rationale] |
|------|-----------|--------|------------------------|---------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Write at least 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete.
> Blocked by: C-16, C-36, C-47

The Entry Trigger and Status-Quo Gap columns are designed to audit each other: a vague
DERIVED:rationale in Entry Trigger will simultaneously produce an FM-ID-free gap in the
adjacent column, making the incompleteness visible as a single row defect.

Write the Entry Trigger: name the LT-ID or DERIVED:[rationale] for this phase. Do not write
"N/A" or leave blank.

Write the Status-Quo Gap: name the FM-ID from the SQ Declaration that this phase addresses.
Do not write a prose description without an FM-ID reference.

| Ph-ID | Phase Name | Entry Trigger (LT-ID or DERIVED:[rationale]; "N/A" or blank is a fail) | Status-Quo Gap (FM-ID from SQ Declaration; prose without FM-ID is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------|-------------|----------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Write at least 3 phases. Each phase must contain at least 2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Write at least 6 states. Write at least 2 states per phase. Name every state explicitly.

For Entry Condition: name the specific event or predecessor state. Do not write "after previous
step."

For Exit Transitions: name the trigger and destination for every outbound path. Do not write
"then continue."

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|-----------------|------------------|--------------|--------|------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

Write at least 3 states with specific timing. Mark at least 1 AT-RISK.

Write at least 3 decision points. For Decision Condition: write both the threshold-type
category AND a quoted example with comparison operator and unit. Do not write only the category.
Do not write only the example.

| D-ID | Decision Name | Decision Condition (category + quoted example both required) | Owner (R-ID) | Branch: Condition Met | Branch: Condition Not Met | Fallback |
|------|--------------|--------------------------------------------------------------|--------------|----------------------|--------------------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

Write parallel paths or state "No parallel paths -- [rationale]."

> **GATE C**: Do not write the Exception Catalog until the State Trace and Decision Table are
> both complete. Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

Write one exit gate per phase. Write "Blocked by" in every gate -- do not leave it blank.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [C-ID(s)]
```

---

**STEP 5 -- EXCEPTION CATALOG**

Write the Exception Catalog only after GATE C is CLOSED. Write at least 3 exception flows.

For Trigger: name the specific condition. Do not write "an error occurs."

For Handler: write the R-ID of a role carrying Exception Handler = Y. Do not write a role
without that designation. Do not leave this blank.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- must be Exception Handler = Y) | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|---------|------------------------------------------------|----------------------|---------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D**: Do not write the Terminal Declaration until every exception flow carries a
> **certified Handler R-ID**. Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

Write Terminal Declaration only after GATE D is CLOSED. Write at least one success terminal
and at least one failure or cancel terminal.

For Type: write exactly "success", "failure", or "cancel." Do not write "completed."

For Reached From: list every S-ID and E-ID that arrives at this terminal. Do not leave blank.

| T-ID | Terminal Name | Type | Reached From |
|------|--------------|------|--------------|
| T-01 | | | |
| T-02 | | | |

> **Check V -- Terminal Path Verification**
> Status: [ OPEN / CLOSED ]
> Confirm every path (happy path + every E-ID) reaches a named T-ID. Write CLOSED only
> after every path is individually confirmed. Check V CLOSED is required before the artifact
> is written.

---

**STEPS 7-12** -- Same structure as V-01: write EDGE CASE CATALOG (min 2), SLA ANNOTATION,
BOTTLENECK REGISTER (min 2), GAP REGISTER (min 1), CROSS-LIFECYCLE HANDOFF (min 1),
EXCEPTION COVERAGE AUDIT using imperative field instructions throughout.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A: >=3 LT-IDs; every row has Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B: >=3 failure surfaces; every row has Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A header precedes STEP 0B header | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION present before STEP 0A; Incumbent Process, FM-01, FM-02, Inertia Driver all present | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no cell may share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role: domain-qualified title, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | LT-ID Trace column header defines SECONDARY escape code | Step 1 header | | |
| AC-06 | Entry Trigger column header defines DERIVED escape code | Step 2 header | | |
| AC-07 | Every Handler R-ID traces to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header carries both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 | | |
| AC-12 | Gate C and Gate D both name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Phase Index Status-Quo Gap column co-located with Entry Trigger; each row has specific FM-ID | Step 2 table | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with threshold, owner, branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff | Step 11 | | |

**Defect Type Taxonomy:** (same D-01 through D-13 as V-01, no D-14 or D-15 since C-48/C-49
are not targeted -- their failure modes would appear as AC-23/AC-24 gaps if a reviewer
scored this output against the v15 rubric)

---

> **PRODUCTION GATE**: Write the artifact only after Coverage Scan shows PASS for AC-01
> through AC-22 AND Check V shows CLOSED. An artifact written while any row shows FAIL must
> be discarded and rerun from the failing step.

---

## V-04 -- Role Sequence + Lifecycle Emphasis (C-48 PARTIAL, C-49 PARTIAL)

**Variation axis:** Combined -- role sequence (role registry anchors all downstream assignments
via a pre-registry survey step before STEP 0A) combined with lifecycle emphasis (heavy
phase-layer framing: each phase receives an explicit entry trigger rationale paragraph before
the Phase Index table is opened). C-48 is partially satisfied: FM-01 and FM-02 field
definitions in the SQ Declaration carry inline anti-pattern vocabulary but the Inertia Driver
field does not (one per-field gap). C-49 is partially satisfied: a caption before the Phase
Index table names the mutual-audit relationship but the Status-Quo Gap column header itself
does not carry the design-principle designation (relationship noted in table caption, not in
column header).

**Hypothesis:** Role-sequence emphasis and lifecycle-phase emphasis each strengthen different
criterion clusters (C-05/C-11/C-23 for roles; C-16/C-33 for phases) but neither directly
addresses the point-of-use placement requirements for C-48 and C-49. A partial SQ Declaration
with anti-pattern vocabulary on some fields but not all creates a asymmetric enforcement
surface: authors who read FM-01's field definition get the constraint signal, but authors who
read the Inertia Driver field do not. Similarly, naming the mutual-audit relationship in a
table caption rather than the column header means the signal is present before the table is
filled but absent at the cell-fill moment. Prediction: V-04 shows the structural cost of
partial placement -- strong compliance on targeted criteria but C-48 and C-49 each score 0.5.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. The schema begins with a role survey, then the STATUS-QUO
PROCESS DECLARATION, then the pre-schema blocks. Work through every numbered step in order.

---

### PRE-REGISTRY ROLE SURVEY

Before authoring any schema section, identify the primary domain roles this lifecycle involves.
List 3-5 candidate roles by domain function. This survey anchors the Role Registry in Step 1.

| Survey-ID | Candidate Role Domain | Expected Involvement |
|-----------|----------------------|---------------------|
| SR-01 | | |
| SR-02 | | |
| SR-03 | | |

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs defined here are required in the Phase Index
Status-Quo Gap column.

| SQ-Field | Content |
|----------|---------|
| Incumbent Process -- names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count | |
| FM-01 -- first failure mode: names the specific condition the incumbent fails to detect or prevent; "error-prone" or "inefficient" does not count; must name the missing mechanism; assign identifier FM-01 | |
| FM-02 -- second failure mode: must be orthogonal to FM-01; assign identifier FM-02 | |
| Inertia Driver -- the organizational or economic reason the incumbent persists despite FM-01 and FM-02 | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

| LT-ID | Trigger Description -- specific initiating event; "process begins" does not count | Trigger Source (System Event / Role Action / Time Condition) | Initial State | Initial Phase -- Mandatory; blank is a fail |
|-------|-----------------------------------------------------------------------------------|-------------------------------------------------------------|---------------|---------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

Minimum 3 rows.

> Do not proceed to STEP 0B until STEP 0A is complete.

---

### STEP 0B -- ORTHOGONAL FAILURE SURFACE TAXONOMY

| FS-ID | Failure Surface -- structural defect category; duplicate categories are a fail | Gate Domain | Closed By (C-ID or Gate Label; blank is a fail) |
|-------|--------------------------------------------------------------------------------|-------------|--------------------------------------------------|
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

Roles must correspond to survey entries in SR-01 through SR-03 or be justified by an LT scope.
No role from the pre-registry survey may be dropped without a stated reason.

| R-ID | Role Name -- domain-qualified functional title; generic labels do not count | Domain -- process function; org-unit without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; at least one Y; blank is a fail | LT-ID Trace or SECONDARY:[rationale]; "N/A" or blank is a fail |
|------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

Minimum 3 roles.

---

**STEP 2 -- PHASE INDEX**

> **GATE B**: Do not open the State Trace until the Phase Index is complete.
> Blocked by: C-16, C-36, C-47

The Entry Trigger and Status-Quo Gap columns form a mutual-audit pair: a generic
DERIVED:rationale in Entry Trigger simultaneously produces a vague gap with no FM-ID in
Status-Quo Gap, making the incompleteness visible in a single row scan.

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A, or DERIVED:[rationale]; "N/A" or blank is a fail) | Status-Quo Gap (FM-ID from STATUS-QUO PROCESS DECLARATION; cell with no FM-ID is structurally unanchored and is a fail) | Completion Condition | SLA Envelope | SLA Risk | States Contained |
|-------|-----------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------|-------------|----------|-----------------|
| PH-01 | | | | | | | |
| PH-02 | | | | | | | |
| PH-03 | | | | | | | |

Minimum 3 phases; each phase must contain >=2 states.

---

**STEP 3 -- STATE TRACE + DECISION TABLE + PARALLEL PATHS**

Minimum 6 states. Minimum 2 states per phase.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition -- specific event or predecessor; "after previous step" does not count | Exit Transitions -- labeled paths with trigger and destination | Owner (R-ID) | Timing | SLA Status |
|------|--------------|------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------|--------------|--------|------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| S-03 | | | | | | | |

**Decision Points** -- minimum 3:

| D-ID | Decision Name | Decision Condition (threshold-type category from: dollar amount, day count, retry count, unit quantity AND quoted example with operator and unit; either alone is a fail) | Owner (R-ID) | Branch: Met | Branch: Not Met | Fallback |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------|----------------|---------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** -- minimum 1 fork-join or "No parallel paths -- [rationale]."

> **GATE C**: Do not open Exception Catalog until State Trace and Decision Table are complete.
> Source: Step 3 --> Target: Step 5. Blocked by: C-30, C-32.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [verifiable output or state]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [C-ID(s) -- Mandatory]
```

---

**STEP 5 -- EXCEPTION CATALOG**

GATE C must be CLOSED. Minimum 3 exception flows.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger -- specific condition; "an error occurs" does not count | Handler (R-ID) -- Must trace to Exception Handler = Y in Step 1; Mandatory; blank or uncertified is a structural fail | Divergence Phase/Step | Recovery State or Terminal |
|------|--------------|----------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D**: Do not open Terminal Declaration until all exception flows carry a **certified
> Handler R-ID**. Source: Step 5 --> Target: Step 6. Blocked by: C-32, C-45.

---

**STEP 6 -- TERMINAL DECLARATION**

GATE D must be CLOSED. Minimum 1 success + 1 failure/cancel terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (all S-IDs and E-IDs; blank is a fail) |
|------|--------------|----------------------------------|-----------------------------------------------------|
| T-01 | | | |
| T-02 | | | |

> **Check V** -- Status: [ OPEN / CLOSED ] -- Confirm every path reaches a T-ID. CLOSED only
> when every path is individually confirmed. Co-equal Production Gate condition.

---

**STEPS 7-12** -- Same structure as V-01.

---

**STEP 13 -- COVERAGE SCAN**

#### Group A -- Pre-Schema Structural Blocks

| AC-ID | Check | Evidence Location | Status (PASS/FAIL) | Defect Type if FAIL |
|-------|-------|------------------|--------------------|---------------------|
| AC-01 | STEP 0A: >=3 LT-IDs; every row: Trigger Description, Trigger Source, Initial State, Initial Phase | STEP 0A | | |
| AC-02 | STEP 0B: >=3 failure surfaces; every row: Failure Surface, Gate Domain, Closed By | STEP 0B | | |
| AC-03 | STEP 0A header precedes STEP 0B header | Section headers | | |
| AC-21 | STATUS-QUO PROCESS DECLARATION before STEP 0A with Incumbent Process, FM-01, FM-02, Inertia Driver | SQ Declaration | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: no cell may share the same coverage claim across rows.

| AC-ID | Check | Evidence Location | Status | Defect Type if FAIL |
|-------|-------|------------------|--------|---------------------|
| AC-04 | Every role: domain-qualified title, Exception Handler Y/N, LT-ID Trace or SECONDARY:rationale | Step 1 | | |
| AC-05 | LT-ID Trace column header defines SECONDARY escape code | Step 1 header | | |
| AC-06 | Entry Trigger column header defines DERIVED escape code | Step 2 header | | |
| AC-07 | Every Handler R-ID traces to Exception Handler = Y | Step 5 | | |
| AC-08 | Handler column header co-locates backward-trace rule and fail-declaration | Step 5 header | | |
| AC-09 | Gate D uses "certified Handler R-ID" language | Gate D text | | |
| AC-10 | Decision Condition column header: both threshold-type category list and quoted example | Step 3 D-table header | | |
| AC-11 | Every phase exit gate carries "Blocked by: [C-ID]" | Step 4 | | |
| AC-12 | Gate C and Gate D name source and target sections | Gate C + D | | |
| AC-13 | Check V present; named as co-equal Production Gate condition | Step 6 + Production Gate | | |
| AC-22 | Phase Index Status-Quo Gap column co-located with Entry Trigger; each row has FM-ID | Step 2 table | | |

#### Group C -- General Schema Integrity

| AC-ID | Check | Evidence | Status | Defect Type if FAIL |
|-------|-------|---------|--------|---------------------|
| AC-14 | >=6 states with entry condition, exit transitions, owner R-ID | Step 3 | | |
| AC-15 | >=3 exceptions with trigger, certified Handler R-ID, divergence, recovery or terminal | Step 5 | | |
| AC-16 | >=1 success + >=1 failure/cancel terminal; all paths reach T-ID | Step 6 | | |
| AC-17 | >=2 bottlenecks + >=1 gap | Steps 9 + 10 | | |
| AC-18 | >=3 decisions with threshold, owner, branches, fallback | Step 3 | | |
| AC-19 | >=3 states with timing; >=1 AT-RISK phase | Steps 3 + 2 | | |
| AC-20 | >=1 cross-lifecycle handoff | Step 11 | | |

**Defect Type Taxonomy:** D-01 through D-13 as in V-01 floor.

---

> **PRODUCTION GATE**: Write the artifact only after Coverage Scan PASS for AC-01 through
> AC-22 AND Check V CLOSED. Artifact written while any row shows FAIL must be discarded and
> rerun from the failing step.

---

## V-05 -- Inertia Framing + Output Format: Full C-48 + C-49 at Maximum Strength

**Variation axis:** Combined -- inertia framing (per-field anti-pattern vocabulary in every
SQ Declaration field definition, C-48 TARGET) and output format (mutual-audit design principle
named explicitly and fully in the Status-Quo Gap column header, C-49 TARGET). This variation
is the full R15 floor: it carries all C-01 through C-47 invariants plus both new aspirational
criteria at their strongest formulation. The Coverage Scan adds AC-23 (C-48) and AC-24 (C-49)
as Group B checks. The Defect Type Taxonomy adds D-14 and D-15. The Production Gate references
both new defect types by name.

**Hypothesis:** C-48 and C-49 address two orthogonal precision gaps in the same architectural
zone. C-48 closes the field-level enforcement gap in the STATUS-QUO PROCESS DECLARATION:
every field row self-describes what a bad entry looks like, so a practitioner filling a single
row cannot miss the constraint even if they skipped the preamble. C-49 closes the design-intent
visibility gap in the Phase Index: naming the mutual-audit relationship as a design principle
(not merely describing its structural behavior) signals that the co-location was architected
to create mutual pressure, not placed for convenience. Together they form a bidirectional
integrity chain: the SQ Declaration produces FM-IDs that are precisely constrained at the
point of authorship (C-48), and the Phase Index Status-Quo Gap column names the design
principle that makes FM-ID omission structurally self-exposing (C-49). The prediction: the
combination produces the maximum suppression of D-10 (FM-ID-free failure mode), D-11
(unanchored status-quo gap), D-14 (per-field anti-pattern gap), and D-15 (unnamed design
principle) simultaneously.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal. Work through every numbered step in order. Read every field
definition and column header before filling that row -- both carry their own enforcement
vocabulary inline.

---

### STATUS-QUO PROCESS DECLARATION

Author this block before STEP 0A. FM-IDs defined here are required fields in the Phase Index
Status-Quo Gap column. A Phase Index cell with no FM-ID from this block is structurally
unanchored and is a fail.

| SQ-Field | Content |
|----------|---------|
| Incumbent Process -- names the specific named process, tool, or workaround being replaced; "manual process" without naming the specific tool does not count; naming a department or team without naming the specific process does not count; a single-word product name without workflow context does not count; Mandatory | |
| FM-01 -- first failure mode: names the specific condition or gap the incumbent fails to detect or prevent; "error-prone," "inefficient," or "slow" does not count; a generic category name without a missing detection or prevention mechanism does not count; duplicate of another FM entry is a fail; must carry the identifier FM-01 | |
| FM-02 -- second failure mode: must name a different failure category from FM-01; a failure mode that is a restatement, direct consequence, or subcategory of FM-01 is a fail; must be independently testable as absent from the incumbent; must carry the identifier FM-02 | |
| Inertia Driver -- names the specific organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02; "familiarity" or "it works well enough" without specificity does not count; a reason that applies equally to all legacy processes does not count; Mandatory | |

---

### STEP 0A -- LIFECYCLE TRIGGER INVENTORY

Author this table completely before proceeding to STEP 0B.

| LT-ID | Trigger Description -- names the external event, role action, or time condition that initiates the lifecycle; "process begins" or "a request is submitted" without naming the specific initiating signal does not count | Trigger Source (must be exactly: System Event / Role Action / Time Condition; any other value is a fail) | Initial State -- first lifecycle state activated; generic name without lifecycle qualifier does not count | Initial Phase -- phase boundary this trigger activates; Mandatory; blank is a structural fail; if the trigger enters an existing phase mid-run, name that containing phase |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

| R-ID | Role Name -- domain-qualified functional title (e.g., "Senior Credit Analyst", "AP Supervisor", "Procurement Category Manager"); generic labels ("Approver", "Admin", "User", "Finance team") do not count | Domain -- process function (e.g., Sales Operations, Finance -- AP, Procurement); org-unit name without process qualifier does not count | Exception Handler (Y/N) -- Mandatory; Y = authorized to handle exception flows and may appear as Handler R-ID in Step 5; N = not authorized; at least one Y required; blank is a fail | LT-ID Trace -- name the LT-ID(s) from STEP 0A in whose Initial State or Initial Phase this role appears; if role exists outside all LT scopes, write SECONDARY:[rationale naming why this role exists without any LT anchor]; generic "N/A" or blank is a fail |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

| Ph-ID | Phase Name | Entry Trigger (LT-ID from STEP 0A naming this phase directly, or DERIVED:[rationale naming which LT-IDs and combination logic produced this phase boundary] -- generic "N/A" or blank is a fail) | Status-Quo Gap (mutual-audit design principle: the Entry Trigger and this column are architected as a mutual-audit pair -- when Entry Trigger is specific, this column can name a precise FM-ID; when Entry Trigger is generic, this column simultaneously lacks an FM-ID anchor, making the incompleteness structurally self-exposing in a single row scan; this co-exposure is the design intent of their adjacency, not a coincidence of table layout; write the FM-ID from STATUS-QUO PROCESS DECLARATION naming which incumbent failure mode this phase's entry trigger addresses; a cell with no FM-ID reference is structurally unanchored and is a fail) | Completion Condition -- verifiable output or state that closes this phase; "work is done" does not count | SLA Envelope -- specific duration (e.g., "5 business days"); "as soon as possible" does not count | SLA Risk -- breach condition and causal bottleneck; at least one phase must be annotated AT-RISK | States Contained (populated after Step 3) |
|-------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------|
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
> finalized produces untraceable ID references.
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
|------|--------------|----------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

> **GATE D -- Downstream Exception-Catalog Boundary**: Do not open the Terminal Declaration
> until all exception flows carry a **certified Handler R-ID** -- that is, an R-ID that traces
> to a role pre-certified as Exception Handler = Y in the Role Registry. An exception flow
> with an uncertified or blank Handler R-ID is a structural fail that blocks this gate and
> produces an artifact that must be discarded and rerun from Step 5 before it is filed or used.
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
| AC-23 | Every field row in the STATUS-QUO PROCESS DECLARATION carries at least one inline anti-pattern token ("does not count," "Mandatory," or "is a fail") specific to that field's content type -- verify each field row individually; a field definition row with no inline token is a per-field enforcement gap; bulk attestation that "all fields have tokens" without naming each field is a fail | SQ Declaration field definitions (each row individually) | | |

#### Group B -- Gate-Backed Aspirational Criteria

Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no
cell may share the same coverage claim across these rows.

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
| AC-24 | Status-Quo Gap column header explicitly names the mutual-audit relationship as a design principle using "mutual-audit design principle" or equivalent named-principle language -- a structural observation that the columns audit each other without naming the relationship as an intentional design principle does not pass; verify that the header text contains language designating the co-auditing behavior as design intent, not merely describing it as a property | Step 2 column header | | |

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
| D-14 | Per-field anti-pattern gap: SQ Declaration present with FM-IDs assigned but at least one field definition row carries no inline anti-pattern token ("does not count," "Mandatory," or "is a fail") -- the field is present but provides no point-of-use enforcement; distinct from D-10 (FM-ID absent) by requiring that the FM-ID be present but the enforcement vocabulary be absent | C-48, AC-23 |
| D-15 | Unnamed mutual-audit design principle: Status-Quo Gap column present and co-located with Entry Trigger; auditing relationship noted in column header text; but the relationship is not named as a design principle using "mutual-audit design principle" or equivalent principle-designation language -- structural description without principle designation does not pass | C-49, AC-24 |

---

> **PRODUCTION GATE**: Writing this artifact while any Coverage Scan row shows FAIL is a
> structural fail -- the artifact contains at least one defect named in the Defect Type column
> above (an unterminated path, an uncertified exception handler, a missing SQ Declaration, an
> FM-ID-free failure mode, a per-field anti-pattern gap in the SQ Declaration, an unnamed
> mutual-audit design principle in the Status-Quo Gap header, an unanchored status-quo gap,
> a DERIVED-only or gap-column-only Phase Index, a missing Initial Phase field, unlabeled
> pre-schema blocks, or a generic escape code in a downstream trace column) -- and that artifact
> must be discarded and rerun from the failing step before it is filed or used.
>
> Both conditions must be satisfied before the artifact is written:
> (1) Coverage Scan shows PASS for AC-01 through AC-24.
> (2) Check V shows CLOSED.
