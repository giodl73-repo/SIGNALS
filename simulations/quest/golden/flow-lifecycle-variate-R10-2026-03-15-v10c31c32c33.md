---
skill: flow-lifecycle
round: 10
rubric-version: v10
rubric-criteria-targets: C-31, C-32, C-33
date: 2026-03-15
status: VARIATE
variations: 5
floor: flow-lifecycle-variate-R10-v10-2026-03-15.md V-05
---

# flow-lifecycle -- Round 10 / Rubric v10 (C-31, C-32, C-33)

Three new aspirational criteria extracted from Round 9 scoring patterns:

- **C-31 -- Dual-Mechanism Threshold Operationalization**: Decision Condition column header
  carries BOTH (1) a named taxonomy of ≥2 threshold type categories AND (2) a quoted concrete
  passing example with comparison operator and unit -- simultaneously, in the same column header.
  Taxonomy without example leaves format ambiguous; example without taxonomy leaves
  category-boundary ambiguous. Only the combination closes both gaps.

- **C-32 -- Bidirectional Exception-Catalog Gate Coverage**: Sequential gates guard BOTH
  exception-catalog boundary transitions -- upstream (state trace and decision table completion
  → exception catalog authoring begins) AND downstream (exception catalog completion → terminal
  declaration authoring begins). Both gates name their source section and target section.
  Together they bracket the exception catalog as a fully bounded structural node.

- **C-33 -- Pre-Schema Lifecycle Inventory Block**: A Step 0 block appears before the role
  registry and enumerates ≥3 named lifecycle entry triggers -- each with trigger source
  (system event, role action, or time condition) and initial state or phase activated. This
  grounds all downstream schema in initiation conditions before any section is authored.

**Invariants across all five variations**: C-27 (scan table + Defect Type column + gate
reference), C-28 (Handler column header: backward-trace authority rule + inline fail-language
co-located), C-29 (threshold-type taxonomy OR quoted example in Decision Condition header),
C-30 (≥1 exception-catalog boundary gate). These are not variation axes.

**Floor**: R10-v10 V-05. Includes: STATUS-QUO PROCESS DECLARATION, PQAR (PQAR-01/02/03),
CFCD (AC-14), DFI (AC-16), negative-exemplar prose guards (AC-15), PHASE DELTA BLOCKS with
enum columns, CCR + CCT, CONSTRAINT-BREAK EXCEPTIONS subsection, COVERAGE SCAN AC-01–AC-16.

**Variation axes and hypothesis matrix:**

| Variation | C-33 Step 0 | C-32 Bidir Gates | C-31 Dual Mechanism | Primary Test |
|-----------|:-----------:|:----------------:|:-------------------:|-------------|
| V-01 | TARGET | HOLD | NONE | Step 0 LIFECYCLE ENTRY INVENTORY before any section; GATE 0 locks entry to role registry |
| V-02 | NONE | TARGET | NONE | Exception Catalog reordered before Terminal Declaration; both GATE C + GATE D with explicit bracketing language |
| V-03 | NONE | NONE | TARGET | Decision Condition column header carries taxonomy list AND quoted example simultaneously |
| V-04 | TARGET | TARGET | NONE | Step 0 + bidirectional gates; structural grounding + bounded exception node together |
| V-05 | TARGET | TARGET | TARGET | Full floor + all three new criteria; maximum structural scaffolding |

---

## V-01 -- Axis: Pre-Schema Lifecycle Inventory (C-33)

**Variation axis:** Pre-schema framing. A LIFECYCLE ENTRY INVENTORY block (Step 0) is
authored before any other section. It enumerates ≥3 named lifecycle entry triggers, each
with a Trigger Source (system event, role action, or time condition) and an Initial State
or Phase activated. GATE 0 blocks entry to the Domain Role Registry until the inventory
is complete. The floor (CFCD, PQAR, DFI, CCR, Phase Delta Blocks, etc.) is unchanged.

**Hypothesis:** The existing floor defines roles, phases, and states without grounding them
in initiation conditions. A role with no path from any LT-ID is structurally unanchored --
its scope cannot be verified against real process entry. A phase whose entry trigger does
not correspond to any LT-ID may be an artifact of structural habit rather than a real
lifecycle stage. Step 0 forces the author to enumerate known entry conditions before
defining vocabulary, making role scope and phase boundary decisions traceable to initiation
paths. Expected: C-33 PASS; AC-17 confirms ≥3 LT-IDs with Trigger Source and Initial State
populated before any subsequent section is opened.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) fill the LIFECYCLE ENTRY INVENTORY (Step 0) -- do not
open any other section until GATE 0 is closed, (2) declare the status-quo process as a named
competitor, (3) declare the output acceptance criteria by ID, (4) fill the PER-ROW QUALITY
ARTIFACT REGISTRY, (5) fill the CATEGORICAL FIELD COVERAGE DECLARATION in a single pass,
(6) fill the DIMENSIONAL FIELD INVENTORY, (7) register the constraint chain. Every artifact
carries incumbent comparison fields. Phase contracts import and export named constraints by
CC-ID. Exception flows caused by constraint import failures are traced bidirectionally in a
Constraint-Break Exceptions subsection. All prose and rationale fields carry inline
negative-exemplar fail-mode instructions.

---

**STEP 0 -- LIFECYCLE ENTRY INVENTORY** *(feeds AC-17)*

> **GATE 0**: Do not open any section -- including the STATUS-QUO PROCESS DECLARATION -- until
> this inventory is complete with ≥3 LT-IDs, each carrying a populated Trigger Source and
> Initial State. This block grounds role scope and phase entry triggers before any vocabulary
> is established. A role that does not appear in any LT-ID's Initial Phase must be annotated
> as a secondary role whose scope is derived, not initiation-driven.

| LT-ID | Entry Trigger Name | Trigger Source (system event / role action / time condition -- one of these three; "process begins" does not count) | Initial State or Phase Activated (name the specific S-ID or Ph-ID this trigger opens; "processing starts" does not count) | Notes (constraints or preconditions on this trigger -- or NONE) |
|-------|-------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |
| LT-NN | | | | |

GATE 0 is CLOSED when: all rows have Trigger Source and Initial State populated; ≥3 LT-IDs
present. Proceed only after GATE 0 is CLOSED.

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | [Name of the as-is process or workflow tool currently in use] |
| Adoption context | [Who uses it and at what scale] |
| Known failure mode FM-1 | [Specific named failure] |
| Known failure mode FM-2 | [Same format] |
| Known failure mode FM-3 | [Same format] |
| Primary inertia driver | [Why this process persists despite known failure modes] |

---

**OUTPUT ACCEPTANCE CRITERIA**

Declared before any content is authored. Post-fill scan executes these IDs.

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts carry `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block quality | (a) block before State Table per phase; (b) Divergence Type exactly missing/incorrect/reversed; (c) Impact Severity HIGH/MED/LOW; HIGH/MED requires FM trace or "New gap" | Wrong column names; wrong order; non-enumerated value; blank; HIGH/MED without trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Root Cause cites source artifact + field using required format | Missing column; format without source citation; forbidden exemplar |
| AC-09 | Incumbent field completeness | Every Incumbent Coverage Mandate artifact has required field populated | Any artifact missing its field; any blank |
| AC-10 | Constraint chain quality | (a) CC-ID chain complete; (b) Handoff Strength STRONG/WEAK/ABSENT+justification; (c) Incumbent Models? Y/N/ABSENT+justification | Gap; blank or invalid values |
| AC-11 | Constraint-break exception tagging | 5-column Constraint-Break subsection; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent; column missing; untraced break |
| AC-12 | Gap analysis completeness | (a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails specific; (e) no blank Incumbent Models? | Missing section or row; missing severity; generic rationale; blank |
| AC-13 | PQAR meta-registry | See PQAR. Verify each Reg-ID individually; new artifact requires PQAR row before continuing | Reg-ID missing; bulk attestation; new artifact without PQAR row |
| AC-14 | Cross-table categorical coverage | CFCD authored before first phase; all categorical-field tables listed; Status=DECLARED; Coverage Scan confirms per table; new table requires immediate CFCD update | CFCD absent; table omitted; Status=MISSING; incremental authoring |
| AC-15 | Prose field negative-exemplar quality | Coverage Scan AC-15 names each prose field and confirms no forbidden exemplar: Root Cause (forbidden: coordination failure, process issue, missing step, general delay); Harm from Absence (forbidden: increases risk, causes delays); Why As-Is Fails (forbidden: not implemented, lacking, insufficient) | Forbidden exemplar present; bulk attestation without per-field enumeration |
| AC-16 | Dimensional Field Inventory output audit | DFI present before first phase; ≥6 fields; Coverage Scan AC-16 names each DFI field, lists observed output values, confirms no out-of-vocabulary value | DFI absent; fewer than 6 fields; bulk attestation; out-of-vocabulary value |
| AC-17 | Lifecycle Entry Inventory | LIFECYCLE ENTRY INVENTORY (Step 0) present and GATE 0 declared before STATUS-QUO PROCESS DECLARATION; ≥3 LT-IDs; each LT-ID has Trigger Source (system event/role action/time condition) and Initial State populated; Coverage Scan confirms per LT-ID | Step 0 absent; GATE 0 absent; fewer than 3 LT-IDs; any LT-ID with blank Trigger Source or Initial State; GATE 0 declared after other sections |

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength; (c) Incumbent Models? |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific -- forbidden exemplars apply) | AC-12 | (a) section named; (b) N-tagged rows; (c) Gap Severity; (d) Why As-Is Fails + forbidden exemplar check; (e) no blank Incumbent Models? |

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

Author completely before any phase. Status = DECLARED required for every row at Coverage Scan.

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? (Phase) |
|------------|---------------------|-------------------|-----------------------------|-----------------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header enumerates allowed values; non-enum or blank is a fail | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header enumerates allowed values; blank is a fail | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header enumerates HIGH/MED/LOW; blank is a fail | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard before populating] | | |
| [Any table added during authoring] | | | | |

---

**DIMENSIONAL FIELD INVENTORY** *(output-time scope -- feeds AC-16)*

| DFI-ID | Field Name | Table | Required Values | Fail Condition | Inline Header Guard? |
|--------|------------|-------|----------------|----------------|---------------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing / incorrect / reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH / MED / LOW (HIGH/MED + trace) | blank; non-enum; HIGH/MED without trace | Y |
| DFI-03 | Handoff Strength | Constraint Chain Table | STRONG / WEAK / ABSENT+justification | blank; unrecognized | Y |
| DFI-04 | Incumbent Models? | Constraint Chain Table | Y / N / ABSENT+justification | blank | Y |
| DFI-05 | Gap Severity | Gap Analysis | HIGH / MED / LOW | blank; non-enum | Y |
| DFI-06 | Type | Terminal Declaration | success / failure / cancel | blank; "completed"; non-enum | [Author declares Y or N] |
| [DFI-NN] | [new categorical field discovered] | | | | |

---

**INCUMBENT COVERAGE MANDATE** *(feeds AC-09)*

| Artifact | Required Incumbent Field |
|----------|--------------------------|
| Status-Quo Role Comparison (dedicated) | Per-role presence (Y/N) |
| Phase Entry Contract | `Incumbent entry` |
| Phase Exit Gate | `Incumbent exit` |
| Terminal Declaration | `Incumbent Terminal? (Y/N)` |
| Exception Catalog | `As-Is Detection? (Y/N)` |
| Bottleneck Register | `Incumbent Workaround` |
| Parallel Path block | `As-Is join` + `Incumbent gap` |
| SLA Annotation | `As-Is Typical Duration` |
| Cross-Process Handoff | `As-Is gap (Y/N)` |

---

**PHASE DELTA BLOCK REQUIREMENT** *(feeds AC-04 / PQAR-01)*

Each lifecycle phase contains a mandatory Phase Delta Block authored BEFORE its State Table.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact column name):
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

> **GATE A**: Do not open the Phase Index until: all roles are domain-qualified functional titles
> (e.g., "Senior Credit Analyst", not "Approver"); at least one role carries
> Exception Handler = Y; every role that appears in any LT-ID Initial Phase is registered.

| R-ID | Role Name (domain-qualified functional title -- generic labels "Approver", "Admin", "User" do not count) | Domain (process area) | Decisions Owned (D-IDs -- blank is a fail if role owns any decision) | Exception Handler (Y/N -- at least one Y required; N-flagged roles may not appear in Handler cells) |
|------|----------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

**Status-Quo Role Comparison** *(feeds AC-09)*

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

> **GATE B**: Do not open any Phase Entry Contract until every phase has a named entry trigger
> that traces to an LT-ID from Step 0 or is annotated as a secondary phase with derivation
> rationale; every phase has a completion condition and SLA envelope.

| Ph-ID | Phase Name | Entry Trigger (must trace to LT-ID or declare derivation) | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|----------------------------------------------------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-NN | | | | | |

---

**CONSTRAINT CHAIN REGISTRY** -- AUTHOR BEFORE ANY PHASE *(feeds AC-10, AC-12)*

| CC-ID | Constraint Name | Originating Phase (Ph-ID) | Consuming Phase(s) (Ph-ID) | Verification Method | Incumbent Models? (Y/N/ABSENT -- blank is a hard fail) |
|-------|-----------------|--------------------------|---------------------------|---------------------|---------------------------------------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE, IN THIS EXACT ORDER:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

---

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Entry condition | [Specific precondition -- "process begins" does not count] |
| Prior phase | [Ph-ID or INITIAL] |
| Active roles | [R-IDs] |
| LT-ID trace | [LT-ID(s) from Step 0 that can reach this phase -- or DERIVED with rationale] |
| Imported constraints | [CC-IDs from prior phase Exit Gate -- or INITIAL if first phase] |
| Constraint verification | [How roles verify each imported CC-ID] |
| Incumbent entry | [How the incumbent triggers this phase -- or ABSENT] |

---

**PHASE DELTA BLOCK [Ph-ID: Phase Name]** -- AUTHOR BEFORE STATE TABLE *(feeds AC-04 / PQAR-01)*

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| DL-01 | | | | |

---

**STATE TABLE [Ph-ID: Phase Name]** -- Author AFTER Phase Delta Block *(feeds AC-01, AC-03)*

| S-ID | State Name | Entry Condition (names specific event or predecessor state; "after previous step" does not count) | Happy-Path Exit (labeled transition) | Exception Exit | Owner (R-ID -- must be in registry; blank is a fail) | Delta Ref (DL-ID or NONE) |
|------|------------|--------------------------------------------------------------------------------------------------|--------------------------------------|----------------|------------------------------------------------------|---------------------------|
| S-01 | | | | | | |

---

**DECISION TABLE [Ph-ID: Phase Name]** *(feeds AC-05)*

| D-ID | Decision Name | Condition (measurable threshold -- dollar amount, day count, retry count, percentage threshold; qualitative condition alone does not count) | Owner (R-ID -- must be in registry; blank is a fail) | Branch A | Branch B (must name outcome; "otherwise" does not count) | Fallback (mechanism-impairment path: role unavailable, system down, config missing; names holding state or escalation target; "escalate" alone does not count) | Delta Ref (DL-ID or NONE) |
|------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| D-01 | | | | | | | |

---

**PARALLEL PATH [Ph-ID: Phase Name]**

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path name]
Branch B:       [concurrent path name]
Join condition: [what must hold before merge -- "both complete" does not count]
Merge owner:    [R-ID]
As-Is join:     [incumbent join behavior -- or ABSENT]
Incumbent gap:  [what breaks in incumbent if join condition fails -- or N/A]
```

---

**PHASE EXIT GATE [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Exit condition | [What must be true; "work is done" does not count] |
| Success transition | [Ph-ID or T-ID] |
| Failure transition | [T-ID or named exception] |
| Blocked by | [Role, resource, or condition; NONE requires explicit justification] |
| Typical duration | [Expected elapsed time] |
| Delta source | [DL-IDs; or NONE] |
| Exported constraints | [CC-IDs this phase exports -- format: CC-NN: constraint name and verified state] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How incumbent transitions out -- or ABSENT] |

---

*Repeat Entry Contract → Phase Delta Block → State Table → Decision Table → Parallel Path →
Exit Gate for each phase. Update CFCD and DFI immediately if new categorical-field table
introduced. Update PQAR immediately if new per-row quality artifact introduced.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

**Constraint Gap Note:** List every ABSENT or WEAK transition with missing constraint and risk.

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

| T-ID | Terminal Name | Type (success / failure / cancel -- one of these three; "completed" does not count) | Reached From (list all Ph-IDs and E-IDs that arrive here; blank is a structural fail) | Incumbent Terminal? (Y/N) |
|------|---------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------|
| T-01 | | | | |
| T-02 | | | | |

At least 1 success terminal and 1 failure or cancel terminal required.

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger (names condition that diverts from happy path; "an error occurs" does not count) | Handler (R-ID -- Must trace to a role with Exception Handler = Y in Role Registry; Mandatory; blank or uncertified role is a structural fail) | Deviation from Happy Path (names specific states bypassed or added; generic language "process stops" or "workflow interrupted" is a fail) | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery (T-ID or named recovery state; "resolved" does not count) |
|------|---------------------|----------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------|-------------------------------------------------------------------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation. *(AC-06)*
**Incumbent Exception Gap:** E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions** *(dedicated subsection -- required for AC-11)*

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

---

**EDGE CASE CATALOG** *(feeds AC-03)*

| EC-ID | Edge Case (names concrete scenario, not category) | Phase (Ph-ID) | Why Unhandled (names specific design decision or omission; "not considered" does not count) | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) |
|-------|--------------------------------------------------|--------------|-------------------------------------------------------------------------------------------|----------------|----------------|----------------------|---------------------------|
| EC-01 | | | | | | | |
| EC-02 | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause (required format: "Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [exact cell value]" or "Phase Exit Gate [Ph-ID] -- Blocked by: [exact cell value]"; forbidden exemplars: coordination failure, process issue, approval bottleneck, missing step, general delay) | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap (generic "missing step" or "gap exists" is a fail -- name the specific missing condition or gated transition) | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence (generic "increases risk" or "causes delays" is a fail -- name specific downstream harm mechanism and artifact affected) | Incumbent Awareness (Y/N) |
|------|---------------|------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF** *(feeds AC-09 if authored)*

```
Handoff trigger:       [Event initiating handoff]
Recipient process:     [Named adjacent process]
Fields passed:         [Named data elements]
Acceptance condition:  [What recipient verifies]
As-Is gap:             [Y/N + note]
Delta source:          [DL-ID or NONE]
Exported constraint:   [CC-ID or NONE]
```

**SLA ANNOTATION** *(feeds AC-09 if authored)*

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-17 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-04, AC-10, AC-12, AC-13
sub-conditions must be confirmed individually. AC-14 must name each CFCD table and confirm
Status = DECLARED. AC-15 must enumerate each prose field by name and confirm no forbidden
exemplar. AC-16 must name each DFI field and list observed output values. AC-17 must confirm
each LT-ID individually.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and rows; blank cells named] |
| AC-04 | | [(a) block order per phase; (b) Divergence Type values; (c) Impact Severity + FM trace] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs; most-dense phase + DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [Root Cause format per row; forbidden exemplars checked] |
| AC-09 | | [per-artifact incumbent field; blanks named] |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength; (c) Incumbent Models?] |
| AC-11 | | [subsection present; columns; CC-ID coverage; E-ID validity] |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [PQAR-01, PQAR-02, PQAR-03 confirmed individually; new rows?] |
| AC-14 | | [CFCD present before phase? Tables: Status confirmed per table; any MISSING?; any mid-authoring additions?] |
| AC-15 | | [Root Cause: forbidden exemplars absent; Harm from Absence: forbidden exemplars absent; Why As-Is Fails: forbidden exemplars absent; each field named individually] |
| AC-16 | | [DFI fields: each named; observed output values listed; out-of-vocabulary values absent] |
| AC-17 | | [Step 0 present before STATUS-QUO? GATE 0 declared? LT-IDs: each confirmed with Trigger Source and Initial State; count ≥3?] |

**Check V:** (a) CC-ID break coverage complete; (b) E-ID CC-ID validity confirmed; (c) E-ID
main catalog presence confirmed. Any FAIL must be corrected before output.

> **ARTIFACT-LEVEL PRODUCTION GATE**: This artifact may not be written until the Coverage Scan
> shows status PASS for AC-01 through AC-17 and Check V shows CLOSED. Any scan row showing
> FAIL is a structural defect: the artifact is invalid, must be discarded, and must be
> rerun from the failed AC's source section. Violating this gate produces an incomplete
> lifecycle trace that contains at least one structural defect listed in the Defect Type
> taxonomy below.

**Scan Summary -- Defect Type Taxonomy:**

| Defect Type | Description | Detected By |
|-------------|-------------|------------|
| Unterminated path | A traced path (happy or exception) has no named T-ID | AC-02 |
| Uncertified exception handler | Handler cell carries R-ID without Exception Handler = Y in registry | AC-11 + C-28 |
| Unresolvable decision owner | Decision gate owner cell is blank or generic | AC-05 |
| Missing lifecycle entry trigger | Step 0 absent or fewer than 3 LT-IDs with Trigger Source and Initial State | AC-17 |
| Missing categorical guard | A categorical field has no inline column-header enumeration and no DFI enforcement | AC-14 + AC-16 |

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs where As-Is Detection? = N] |
| Edge cases incumbent cannot handle | [EC-IDs where As-Is Handled? = N] |
| Terminals incumbent leaves open-ended | [T-IDs where Incumbent Terminal? = N] |
| Roles absent from incumbent | [R-IDs where Present in Incumbent? = N] |
| Gaps invisible to incumbent | [G-IDs where Incumbent Awareness = N] |
| Known failure modes addressed | [FM-1/FM-2/FM-3: closed or open] |
| Entry triggers incumbent cannot initiate | [LT-IDs where incumbent cannot serve as trigger source] |

---

**CONSTRAINT-INCUMBENT GAP ANALYSIS** *(required for CC-IDs with Incumbent Models? = N -- feeds AC-12 / PQAR-03)*

One row per CC-ID where Incumbent Models? = N. Write NONE + justification if none qualify.

| CC-ID | Constraint Name | Gap Severity (HIGH / MED / LOW -- blank is a fail) | Why As-Is Fails (must name specific process characteristic; forbidden: not implemented, lacking this feature, insufficient, not modeled, unsupported) |
|-------|-----------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| | | | |

---

**FINAL AUTHORING CHECK**

- [ ] **LIFECYCLE ENTRY INVENTORY (Step 0)** is the FIRST section; GATE 0 declared; ≥3 LT-IDs with Trigger Source and Initial State
- [ ] STATUS-QUO PROCESS DECLARATION present after Step 0
- [ ] OUTPUT ACCEPTANCE CRITERIA declared with AC-01 through AC-17
- [ ] PER-ROW QUALITY ARTIFACT REGISTRY present; PQAR-01/02/03 rows complete
- [ ] CATEGORICAL FIELD COVERAGE DECLARATION authored before first phase; all tables Status = DECLARED
- [ ] DIMENSIONAL FIELD INVENTORY present; ≥6 DFI fields
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank Incumbent Models?
- [ ] Phase Index Phase entries trace to LT-IDs or carry derivation annotation
- [ ] Every phase: Entry Contract with LT-ID trace + Imported constraints + Incumbent entry
- [ ] Every phase: Phase Delta Block before State Table
- [ ] Every phase: Exit Gate with Exported constraints + Incumbent exit
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column (exact name)
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed CLOSED
- [ ] Coverage Scan: AC-01 through AC-17 + Check V; each AC confirmed individually
- [ ] Artifact-level production gate not violated

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---
<!-- END V-01 -->

## V-02 -- Axis: Bidirectional Exception-Catalog Gate Coverage (C-32)

**Variation axis:** Bidirectional gate coverage. The Exception Catalog is reordered to appear
BEFORE the Terminal Declaration (matching the structural dependency: terminal declarations
cannot be finalized until all exception flows are known). An UPSTREAM GATE blocks entry to
the Exception Catalog until all State Tables and Decision Tables across all phases are stable.
A DOWNSTREAM GATE blocks entry to the Terminal Declaration until all Exception Catalog E-IDs
are complete and all Handler cells are certified. Both gates use explicit bracketing language
naming the exception catalog as a bounded structural node. The floor (CFCD, PQAR, DFI,
negative-exemplar prose guards, etc.) is unchanged. No Step 0 is added; no Decision Condition
header modification.

**Hypothesis:** The existing floor places Terminal Declaration before Exception Catalog,
creating a structural incoherence: terminal "Reached From" cells list E-IDs that have not
yet been authored. This produces forward references that cannot be verified. Reordering to
Exception Catalog → Terminal Declaration restores the structural dependency. Adding the
upstream gate prevents exception flows from referencing unstable state names. Adding the
downstream gate prevents terminal declarations from being filled before exception-path
coverage is known. Together the two gates bracket the exception catalog: it cannot be
entered before state trace is stable, and it cannot be exited before exception flows are
complete. Expected: C-32 PASS; both gates present with source + target names; Terminal
Declaration Reached From cells verified against completed E-IDs.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID, (3) fill the PER-ROW QUALITY ARTIFACT
REGISTRY, (4) fill the CATEGORICAL FIELD COVERAGE DECLARATION in a single pass, (5) fill
the DIMENSIONAL FIELD INVENTORY, (6) register the constraint chain. Every artifact carries
incumbent comparison fields. Phase contracts import and export named constraints by CC-ID.
Exception flows caused by constraint import failures are traced bidirectionally in a
Constraint-Break Exceptions subsection. All prose and rationale fields carry inline
negative-exemplar fail-mode instructions. The exception catalog is a structurally bounded
node: it cannot be entered before the state trace is stable and it cannot be exited before
exception flows are complete -- two sequential gates enforce this bidirectional bracketing.

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | |
| Adoption context | |
| Known failure mode FM-1 | |
| Known failure mode FM-2 | |
| Known failure mode FM-3 | |
| Primary inertia driver | |

---

**OUTPUT ACCEPTANCE CRITERIA**

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts carry `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell |
| AC-04 | Phase Delta Block quality | (a) block order; (b) Divergence Type exactly missing/incorrect/reversed; (c) Impact Severity HIGH/MED/LOW + FM trace for HIGH/MED | Non-enumerated value; blank; wrong order; HIGH/MED without trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Root Cause cites source artifact + field using required format; forbidden exemplars absent | Missing column; forbidden exemplar present |
| AC-09 | Incumbent field completeness | Every Incumbent Coverage Mandate artifact has required field | Any artifact missing its field; blank |
| AC-10 | Constraint chain quality | (a) CC-ID chain complete; (b) Handoff Strength enum; (c) Incumbent Models? enum | Gap; blank or invalid values |
| AC-11 | Constraint-break exception tagging | 5-column Constraint-Break subsection; CC-ID breaks traced; E-IDs valid | Subsection absent; untraced break |
| AC-12 | Gap analysis completeness | (a-e) all sub-conditions including Why As-Is Fails specific and no blank Incumbent Models? | Missing section; generic rationale; blank |
| AC-13 | PQAR meta-registry | See PQAR. Verify each Reg-ID individually | Missing Reg-ID; bulk attestation |
| AC-14 | Cross-table categorical coverage | CFCD authored before first phase; Status=DECLARED per table | CFCD absent; Status=MISSING |
| AC-15 | Prose field negative-exemplar quality | Per-field confirmation; no forbidden exemplar in Root Cause, Harm from Absence, Why As-Is Fails | Forbidden exemplar present; bulk attestation |
| AC-16 | Dimensional Field Inventory output audit | DFI present; ≥6 fields; no out-of-vocabulary values | DFI absent; fewer than 6 fields; out-of-vocabulary value |
| AC-17 | Bidirectional exception-catalog gate coverage | UPSTREAM GATE present before Exception Catalog naming State Tables + Decision Tables → Exception Catalog; DOWNSTREAM GATE present before Terminal Declaration naming Exception Catalog → Terminal Declaration; each gate names source section and target section; Exception Catalog precedes Terminal Declaration in document order | Either gate absent; gate text missing source or target section name; Terminal Declaration authored before Exception Catalog |

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength; (c) Incumbent Models? |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific) | AC-12 | (a-e) all sub-conditions |

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? |
|------------|---------------------|-------------------|-----------------------------|--------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header enumerates allowed values | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header enumerates allowed values | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header enumerates HIGH/MED/LOW | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard] | | |

---

**DIMENSIONAL FIELD INVENTORY** *(feeds AC-16)*

| DFI-ID | Field Name | Table | Required Values | Fail Condition | Inline Header Guard? |
|--------|------------|-------|----------------|----------------|---------------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing / incorrect / reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH / MED / LOW + trace | blank; non-enum | Y |
| DFI-03 | Handoff Strength | Constraint Chain Table | STRONG / WEAK / ABSENT+justification | blank | Y |
| DFI-04 | Incumbent Models? | Constraint Chain Table | Y / N / ABSENT+justification | blank | Y |
| DFI-05 | Gap Severity | Gap Analysis | HIGH / MED / LOW | blank; non-enum | Y |
| DFI-06 | Type | Terminal Declaration | success / failure / cancel | blank; non-enum | [Author: Y or N] |

---

**INCUMBENT COVERAGE MANDATE** *(feeds AC-09)*

| Artifact | Required Incumbent Field |
|----------|--------------------------|
| Status-Quo Role Comparison | Per-role presence (Y/N) |
| Phase Entry Contract | `Incumbent entry` |
| Phase Exit Gate | `Incumbent exit` |
| Terminal Declaration | `Incumbent Terminal? (Y/N)` |
| Exception Catalog | `As-Is Detection? (Y/N)` |
| Bottleneck Register | `Incumbent Workaround` |
| Parallel Path block | `As-Is join` + `Incumbent gap` |
| SLA Annotation | `As-Is Typical Duration` |
| Cross-Process Handoff | `As-Is gap (Y/N)` |

---

**PHASE DELTA BLOCK REQUIREMENT** *(feeds AC-04 / PQAR-01)*

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap"; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)`:
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

> **GATE A**: Do not open the Phase Index until all roles are domain-qualified functional
> titles (e.g., "AP Supervisor", "Revenue Recognition Manager"; generic "Approver" or "Admin"
> do not count) and at least one role carries Exception Handler = Y.

| R-ID | Role Name (domain-qualified functional title; generic labels do not count) | Domain | Decisions Owned (D-IDs; blank is a fail if role owns any decision) | Exception Handler (Y/N -- at least one Y; N-flagged roles may not appear in Handler cells) |
|------|----------------------------------------------------------------------------|--------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

**Status-Quo Role Comparison** *(feeds AC-09)*

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

> **GATE B**: Do not open any Phase Entry Contract until every phase has a named entry
> trigger, completion condition, and SLA envelope.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |

---

**CONSTRAINT CHAIN REGISTRY** -- AUTHOR BEFORE ANY PHASE *(feeds AC-10, AC-12)*

| CC-ID | Constraint Name | Originating Phase | Consuming Phase(s) | Verification Method | Incumbent Models? (Y/N/ABSENT -- blank is a hard fail) |
|-------|-----------------|------------------|--------------------|---------------------|--------------------------------------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE, IN THIS EXACT ORDER:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Entry condition | [Specific precondition] |
| Prior phase | [Ph-ID or INITIAL] |
| Active roles | [R-IDs] |
| Imported constraints | [CC-IDs or INITIAL] |
| Constraint verification | [How verified] |
| Incumbent entry | [or ABSENT] |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID: Phase Name]** *(feeds AC-01, AC-03)*

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| S-01 | | | | | | |

**DECISION TABLE [Ph-ID: Phase Name]** *(feeds AC-05)*

| D-ID | Decision Name | Condition (measurable threshold -- dollar amount, day count, retry count; qualitative alone does not count) | Owner (R-ID) | Branch A | Branch B | Fallback (mechanism-impairment path) | Delta Ref (DL-ID or NONE) |
|------|--------------|-------------------------------------------------------------------------------------------------------------|--------------|----------|----------|--------------------------------------|---------------------------|
| D-01 | | | | | | | |

**PARALLEL PATH [Ph-ID]**

```
Fork (S-ID):    [branching state]
Branch A:       [named path]
Branch B:       [named path]
Join condition: [what must hold]
Merge owner:    [R-ID]
As-Is join:     [or ABSENT]
Incumbent gap:  [or N/A]
```

**PHASE EXIT GATE [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition | |
| Failure transition | |
| Blocked by | [NONE requires justification] |
| Typical duration | |
| Delta source | |
| Exported constraints | |
| Constraint export gap | |
| Incumbent exit | |

*Repeat per phase. Update CFCD/DFI if new categorical-field table. Update PQAR if new per-row quality artifact.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

---

> **UPSTREAM EXCEPTION-CATALOG GATE**: The exception catalog is a structurally bounded node
> that cannot be entered before the state trace is stable. Do not author the EXCEPTION CATALOG
> until all State Tables and Decision Tables across all phases are complete -- exception flows
> reference S-IDs and D-IDs by name; authoring exceptions before these are finalized produces
> untraceable ID references and phantom deviation paths. This gate locks the CONSTRAINT CHAIN
> TABLE and all PHASE sections; it unlocks the EXCEPTION CATALOG. Source section: State Tables
> and Decision Tables (all phases). Target section: EXCEPTION CATALOG.

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

UPSTREAM GATE must be CLOSED (all State Tables and Decision Tables complete) before this
section is opened.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger (condition that diverts; "an error occurs" does not count) | Handler (R-ID -- Must trace to a role with Exception Handler = Y in Role Registry; Mandatory; blank or uncertified role is a structural fail) | Deviation from Happy Path (names specific states bypassed; "process stops" is a fail) | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery (T-ID or named recovery state; "resolved" does not count) |
|------|---------------------|----------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------|---------------------------|-------------------------------------------------------------------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID. *(AC-06)*
**Incumbent Exception Gap:** E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions** *(required for AC-11)*

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

Bidirectional traceability: every CC-ID break has E-ID; every E-ID traces to valid CC-ID and
main catalog. Check V audits. Resolve before proceeding.

> **DOWNSTREAM EXCEPTION-CATALOG GATE**: The exception catalog is a structurally bounded node
> that cannot be exited before exception flows are complete. Do not author the TERMINAL
> DECLARATION until all E-IDs in the EXCEPTION CATALOG are fully populated -- including
> Handler cells carrying certified R-IDs and Terminal or Recovery cells naming a T-ID or
> recovery state. Terminal Declaration "Reached From" cells list E-IDs; authoring terminals
> before exception flows are complete produces Reached From entries that are unverifiable
> forward references. This gate locks the EXCEPTION CATALOG; it unlocks the TERMINAL
> DECLARATION. Source section: EXCEPTION CATALOG. Target section: TERMINAL DECLARATION.

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

DOWNSTREAM GATE must be CLOSED (all Exception Catalog E-IDs complete with certified Handlers
and named Terminal or Recovery) before this section is opened.

| T-ID | Terminal Name | Type (success / failure / cancel -- "completed" does not count) | Reached From (all Ph-IDs and E-IDs; blank is a structural fail) | Incumbent Terminal? (Y/N) |
|------|---------------|----------------------------------------------------------------|----------------------------------------------------------------|--------------------------|
| T-01 | | | | |
| T-02 | | | | |

At least 1 success terminal and 1 failure or cancel terminal required.

---

**EDGE CASE CATALOG** *(feeds AC-03)*

| EC-ID | Edge Case (concrete scenario, not category) | Phase (Ph-ID) | Why Unhandled | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) |
|-------|---------------------------------------------|--------------|---------------|----------------|----------------|----------------------|---------------------------|
| EC-01 | | | | | | | |
| EC-02 | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause (format: "Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [exact cell value]"; forbidden: coordination failure, process issue, missing step) | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap (generic "missing step" is a fail -- name specific missing condition) | Delta Ref (DL-ID or NONE) | As-Is | Harm from Absence (generic "increases risk" is a fail -- name specific downstream harm) | Incumbent Awareness (Y/N) |
|------|---------------|--------------------------------------------------------------------------|---------------------------|-------|----------------------------------------------------------------------------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF** *(optional -- feeds AC-09)*

```
Handoff trigger:       [Event]
Recipient process:     [Named adjacent process]
Fields passed:         [Named data elements]
Acceptance condition:  [What recipient verifies]
As-Is gap:             [Y/N + note]
Delta source:          [DL-ID or NONE]
Exported constraint:   [CC-ID or NONE]
```

**SLA ANNOTATION** *(optional -- feeds AC-09)*

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-17 plus Check V)*

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked] |
| AC-02 | | [paths and E-IDs; open-ended named] |
| AC-03 | | [artifacts and rows; blank cells] |
| AC-04 | | [(a) block order; (b) Divergence Type; (c) Impact Severity + FM trace] |
| AC-05 | | [decisions and state owners; generic labels] |
| AC-06 | | [E-IDs; most-dense Ph-ID + DL-ID] |
| AC-07 | | [phases; missing contract or gate] |
| AC-08 | | [Root Cause format; forbidden exemplars] |
| AC-09 | | [per-artifact incumbent field; blanks] |
| AC-10 | | [(a) chain; (b) Handoff Strength; (c) Incumbent Models?] |
| AC-11 | | [subsection; columns; CC-ID coverage; E-ID validity] |
| AC-12 | | [(a)-(e) individually] |
| AC-13 | | [PQAR-01, PQAR-02, PQAR-03 individually] |
| AC-14 | | [CFCD present before phase; each table: Status confirmed] |
| AC-15 | | [Root Cause field: values named, forbidden exemplars absent; Harm from Absence: same; Why As-Is Fails: same] |
| AC-16 | | [each DFI field named; observed values listed; out-of-vocabulary absent] |
| AC-17 | | [UPSTREAM GATE present before Exception Catalog? Source section named? Target section named? DOWNSTREAM GATE present before Terminal Declaration? Source named? Target named? Exception Catalog precedes Terminal Declaration?] |

**Check V:** (a) CC-ID break coverage; (b) E-ID CC-ID validity; (c) E-ID main catalog presence.

> **ARTIFACT-LEVEL PRODUCTION GATE**: This artifact may not be written until Coverage Scan
> shows PASS for AC-01 through AC-17 and Check V shows CLOSED. Violation produces an
> incomplete lifecycle trace -- must be discarded and rerun from the failed section.

**Scan Summary -- Defect Type Taxonomy:**

| Defect Type | Description | Detected By |
|-------------|-------------|------------|
| Unterminated path | A path (happy or exception) has no named T-ID | AC-02 |
| Uncertified exception handler | Handler cell not traced to Exception Handler = Y | AC-11 + C-28 |
| Unresolvable decision owner | Decision gate owner is blank or generic | AC-05 |
| Missing exception-catalog upstream gate | No gate blocking exception catalog entry before state trace is stable | AC-17 |
| Missing exception-catalog downstream gate | No gate blocking terminal declaration before exception catalog is complete | AC-17 |

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs where As-Is Detection? = N] |
| Edge cases incumbent cannot handle | [EC-IDs where As-Is Handled? = N] |
| Terminals incumbent leaves open-ended | [T-IDs where Incumbent Terminal? = N] |
| Roles absent from incumbent | [R-IDs where Present in Incumbent? = N] |
| Gaps invisible to incumbent | [G-IDs where Incumbent Awareness = N] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed or open] |

---

**CONSTRAINT-INCUMBENT GAP ANALYSIS** *(required for CC-IDs with Incumbent Models? = N -- feeds AC-12 / PQAR-03)*

| CC-ID | Constraint Name | Gap Severity (HIGH / MED / LOW -- blank is a fail) | Why As-Is Fails (specific process characteristic; forbidden: not implemented, lacking, insufficient) |
|-------|-----------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------|
| | | | |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA: AC-01 through AC-17 declared
- [ ] PQAR: PQAR-01/02/03 complete
- [ ] CFCD: authored before first phase; all tables Status = DECLARED
- [ ] DFI: ≥6 fields present
- [ ] CONSTRAINT CHAIN REGISTRY: before any phase; no blank Incumbent Models?
- [ ] Every phase: Entry Contract + Phase Delta Block (before State Table) + State Table + Decision Table + Parallel Path + Exit Gate
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column
- [ ] **UPSTREAM GATE present before EXCEPTION CATALOG; names State Tables + Decision Tables → Exception Catalog**
- [ ] **EXCEPTION CATALOG precedes TERMINAL DECLARATION in document order**
- [ ] **DOWNSTREAM GATE present before TERMINAL DECLARATION; names Exception Catalog → Terminal Declaration**
- [ ] Constraint-Break Exceptions: 5-column table; Check V CLOSED
- [ ] Coverage Scan: AC-01 through AC-17 + Check V; each confirmed individually
- [ ] Artifact-level production gate not violated

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---
<!-- END V-02 -->

## V-03 -- Axis: Dual-Mechanism Threshold Operationalization (C-31)

**Variation axis:** Decision Condition column header. The Condition column header in every
Decision Table across all phases carries BOTH (1) a named taxonomy of ≥2 threshold type
categories AND (2) a quoted concrete passing example with comparison operator and unit --
simultaneously in the same column header definition. The taxonomy classifies what kinds of
values qualify; the example instantiates a passing case in the required format. The floor
(CFCD, PQAR, DFI, CCR, prose guards, etc.) is unchanged. No Step 0; no gate reordering.

**Hypothesis:** The existing floor uses `Condition` with no inline qualification in the
Decision Table column header. C-29 required either a taxonomy list OR a quoted example; the
R9 V-01 floor used the taxonomy-only form. Taxonomy alone leaves format ambiguous: an author
seeing "dollar amount, day count" knows the category but not how to express it in a cell.
Example alone leaves category-boundary ambiguous: is the quoted form the only valid type?
C-31 requires both simultaneously in the same column header. The combined header closes both
ambiguities at point of use, before a single decision condition cell is filled. Expected:
C-31 PASS; AC-17 confirms taxonomy ≥2 categories AND ≥1 quoted example with comparison
operator and unit in the same Condition column header; at least one decision condition cell
value is confirmed in Coverage Scan as matching a named category and the quoted-example
format.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID, (3) fill the PER-ROW QUALITY ARTIFACT
REGISTRY, (4) fill the CATEGORICAL FIELD COVERAGE DECLARATION in a single pass, (5) fill
the DIMENSIONAL FIELD INVENTORY, (6) register the constraint chain. Every artifact carries
incumbent comparison fields. Phase contracts import and export named constraints by CC-ID.
Exception flows caused by constraint import failures are traced bidirectionally in a
Constraint-Break Exceptions subsection. All prose and rationale fields carry inline
negative-exemplar fail-mode instructions. Every Decision Table Condition column header
carries both a threshold-type taxonomy AND a quoted concrete passing example.

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | |
| Adoption context | |
| Known failure mode FM-1 | |
| Known failure mode FM-2 | |
| Known failure mode FM-3 | |
| Primary inertia driver | |

---

**OUTPUT ACCEPTANCE CRITERIA**

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts carry `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell |
| AC-04 | Phase Delta Block quality | (a) block order; (b) Divergence Type enum; (c) Impact Severity enum + FM trace | Non-enum; blank; wrong order; HIGH/MED without trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Root Cause format correct; forbidden exemplars absent | Missing column; forbidden exemplar |
| AC-09 | Incumbent field completeness | Every mandate artifact has required field | Any artifact missing field; blank |
| AC-10 | Constraint chain quality | (a) chain complete; (b) Handoff Strength; (c) Incumbent Models? | Gap; blank or invalid |
| AC-11 | Constraint-break exception tagging | 5-column subsection; traced; valid | Subsection absent; untraced break |
| AC-12 | Gap analysis completeness | (a-e) all sub-conditions | Missing section; generic rationale; blank |
| AC-13 | PQAR meta-registry | Each Reg-ID individually | Missing Reg-ID; bulk attestation |
| AC-14 | Cross-table categorical coverage | CFCD before first phase; Status=DECLARED | CFCD absent; Status=MISSING |
| AC-15 | Prose field negative-exemplar quality | Per-field; forbidden exemplars absent | Forbidden exemplar; bulk attestation |
| AC-16 | Dimensional Field Inventory output audit | DFI present; ≥6 fields; no out-of-vocabulary | DFI absent; fewer than 6; out-of-vocab |
| AC-17 | Dual-mechanism Decision Condition operationalization | Every Decision Table Condition column header carries: (a) ≥2 named threshold-type categories (e.g., "dollar amount, day count, retry count"); AND (b) ≥1 quoted concrete passing example with comparison operator and unit (e.g., `"Invoice total > $5,000"`); both mechanisms present simultaneously in the same column header; Coverage Scan confirms at least one decision condition cell carries a value matching a named category and example format | Column header with taxonomy only (no quoted example); column header with example only (no taxonomy); either mechanism in preamble instead of column header; fewer than 2 named categories; example without comparison operator; example without unit |

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | AC-ID | Sub-conditions |
|--------|---------------|------------------------|-------|----------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a-c) |
| PQAR-02 | Constraint Chain Table | Handoff Strength, Incumbent Models? | AC-10 | (a-c) |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity, Why As-Is Fails | AC-12 | (a-e) |

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? |
|------------|---------------------|-------------------|-----------------------------|---------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header enumerates allowed values | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header enumerates allowed values | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header enumerates HIGH/MED/LOW | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard] | | |

---

**DIMENSIONAL FIELD INVENTORY** *(feeds AC-16)*

| DFI-ID | Field Name | Table | Required Values | Fail Condition | Inline Header Guard? |
|--------|------------|-------|----------------|----------------|---------------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing/incorrect/reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH/MED/LOW + trace | blank; non-enum | Y |
| DFI-03 | Handoff Strength | Constraint Chain Table | STRONG/WEAK/ABSENT+justification | blank | Y |
| DFI-04 | Incumbent Models? | Constraint Chain Table | Y/N/ABSENT+justification | blank | Y |
| DFI-05 | Gap Severity | Gap Analysis | HIGH/MED/LOW | blank; non-enum | Y |
| DFI-06 | Type | Terminal Declaration | success/failure/cancel | blank; non-enum | [Author: Y or N] |

---

**INCUMBENT COVERAGE MANDATE** / **PHASE DELTA BLOCK REQUIREMENT** / **DELTA CROSS-REFERENCE**

*(same as V-01 floor; five artifacts carry `Delta Ref (DL-ID or NONE)`)*

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

> **GATE A**: Domain-qualified titles only (e.g., "AP Supervisor", "Revenue Recognition Manager";
> generic "Approver" does not count); at least one role carries Exception Handler = Y.

| R-ID | Role Name (domain-qualified functional title; generic labels do not count) | Domain | Decisions Owned (D-IDs) | Exception Handler (Y/N; at least one Y; N-flagged may not appear in Handler cells) |
|------|----------------------------------------------------------------------------|--------|-------------------------|------------------------------------------------------------------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |

**Status-Quo Role Comparison**

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

> **GATE B**: Every phase has a named entry trigger, completion condition, and SLA envelope
> before any Phase Entry Contract is opened.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |

---

**CONSTRAINT CHAIN REGISTRY** -- BEFORE ANY PHASE

| CC-ID | Constraint Name | Originating Phase | Consuming Phase(s) | Verification Method | Incumbent Models? (Y/N/ABSENT -- blank is a hard fail) |
|-------|-----------------|------------------|--------------------|---------------------|--------------------------------------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | [Ph-ID or INITIAL] |
| Active roles | |
| Imported constraints | |
| Constraint verification | |
| Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH/MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| S-01 | | | | | | |

**DECISION TABLE [Ph-ID: Phase Name]** *(feeds AC-05, AC-17)*

| D-ID | Decision Name | Condition (measurable threshold -- dollar amount, day count, retry count, percentage threshold; qualitative condition alone does not count; e.g., `"Invoice total > $5,000"`, `"Days past due > 30"`; format: [measure] [operator] [quantity+unit]) | Owner (R-ID -- must be in registry; blank is a fail) | Branch A | Branch B ("otherwise" does not count) | Fallback (mechanism-impairment: role unavailable, system down, config missing; names holding state or escalation) | Delta Ref (DL-ID or NONE) |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|---------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------|
| D-01 | | | | | | | |

**PARALLEL PATH [Ph-ID]**

```
Fork (S-ID) / Branch A / Branch B / Join condition / Merge owner (R-ID) / As-Is join / Incumbent gap
```

**PHASE EXIT GATE [Ph-ID]**

| Exit condition | Success | Failure | Blocked by | Duration | Delta source | Exported constraints | Export gap | Incumbent exit |
|----------------|---------|---------|------------|----------|-------------|---------------------|-----------|----------------|
| | | | | | | | | |

*Repeat per phase. Update CFCD/DFI for new categorical tables. Update PQAR for new per-row artifacts.*

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG/WEAK/ABSENT+justification; blank is a fail) | Incumbent Models? (Y/N/ABSENT+justification; blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------|-------------------------------------------------------------------|
| CC-01 | | | | | | | | |

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

| T-ID | Terminal Name | Type (success / failure / cancel -- "completed" does not count) | Reached From (all Ph-IDs and E-IDs; blank is a structural fail) | Incumbent Terminal? (Y/N) |
|------|---------------|----------------------------------------------------------------|----------------------------------------------------------------|--------------------------|
| T-01 | | | | |

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y required; blank or uncertified is a structural fail) | Deviation from Happy Path (names specific states bypassed; "process stops" is a fail) | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Constraint-Break Exceptions**

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

---

**EDGE CASE CATALOG** / **BOTTLENECK REGISTER** / **GAP REGISTER**

*(same schema as V-01; forbidden exemplars apply)*

---

**COVERAGE SCAN** *(AC-01 through AC-17 plus Check V)*

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 through AC-16 | | [same as floor] |
| AC-17 | | [Decision Table Condition column header(s) examined: (a) threshold-type taxonomy ≥2 categories named -- list categories observed; (b) quoted example with comparison operator and unit present -- quote the example observed; (c) both mechanisms confirmed in same column header; (d) at least one decision condition cell value named and confirmed matching named category and example format] |

**Check V.**

> **ARTIFACT-LEVEL PRODUCTION GATE**: May not write until PASS on AC-01–AC-17 and Check V
> CLOSED. Violation produces incomplete lifecycle trace -- discard and rerun from failed section.

**Scan Summary -- Defect Type Taxonomy:**

| Defect Type | Description | Detected By |
|-------------|-------------|------------|
| Unterminated path | Traced path has no named T-ID | AC-02 |
| Uncertified exception handler | Handler not traced to Exception Handler = Y | AC-11 + C-28 |
| Unresolvable decision owner | Decision gate owner blank or generic | AC-05 |
| Taxonomy-only decision condition | Condition column header has type list but no quoted example | AC-17 |
| Example-only decision condition | Condition column header has quoted example but no threshold-type taxonomy | AC-17 |
| Missing categorical guard | Categorical field lacks inline column-header enumeration and DFI enforcement | AC-14 + AC-16 |

---

**INERTIA SUMMARY** / **CONSTRAINT-INCUMBENT GAP ANALYSIS**

*(same schema as V-01)*

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION present
- [ ] AC-01 through AC-17 declared
- [ ] PQAR: PQAR-01/02/03 complete
- [ ] CFCD: before first phase; all tables Status = DECLARED
- [ ] DFI: ≥6 fields
- [ ] CCR: before any phase; no blank Incumbent Models?
- [ ] Every phase: Entry Contract + Phase Delta Block (before State Table) + State Table + **Decision Table with dual-mechanism Condition column header** + Parallel Path + Exit Gate
- [ ] **Every Decision Table Condition column header carries: ≥2 threshold-type categories AND ≥1 quoted example with operator and unit -- both in same header**
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column
- [ ] Constraint-Break Exceptions: 5-column table; Check V CLOSED
- [ ] Coverage Scan: AC-01 through AC-17; AC-17 confirms both mechanisms in column header

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---
<!-- END V-03 -->

## V-04 -- Axes: Pre-Schema Inventory + Bidirectional Gates (C-33 + C-32)

**Variation axes:** C-33 (Step 0 lifecycle entry inventory before all sections) combined
with C-32 (bidirectional exception-catalog gate coverage: Exception Catalog before Terminal
Declaration, with explicit upstream and downstream gates). No Decision Condition column
header modification (C-31 not targeted).

**Hypothesis:** C-33 grounds the schema before vocabulary is established; C-32 brackets the
exception catalog as a structurally bounded node. These address orthogonal failure surfaces:
Step 0 prevents unanchored roles and phantom phases; bidirectional gates prevent untraceable
exception references (upstream) and unverifiable terminal entries (downstream). Together
they enforce structural integrity at schema entry (Step 0) and at the exception catalog node
(both boundaries). Expected: C-33 PASS (Step 0 with ≥3 LT-IDs); C-32 PASS (upstream and
downstream gates with source + target names; ordering confirmed); AC-17 and AC-18 each
enumerate distinct evidence in Coverage Scan.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) fill LIFECYCLE ENTRY INVENTORY (Step 0) -- GATE 0
must be CLOSED before any other section opens, (2) declare the status-quo process,
(3) declare output acceptance criteria, (4) fill PQAR, (5) fill CFCD in a single pass,
(6) fill DFI, (7) register the constraint chain. Every artifact carries incumbent comparison
fields. Phase contracts import and export named constraints by CC-ID. Exception flows caused
by constraint import failures are traced bidirectionally in a Constraint-Break Exceptions
subsection. All prose and rationale fields carry inline negative-exemplar fail-mode
instructions. The exception catalog is a structurally bounded node: two sequential gates
enforce bidirectional bracketing.

---

**STEP 0 -- LIFECYCLE ENTRY INVENTORY** *(feeds AC-17)*

> **GATE 0**: Do not open any section until ≥3 LT-IDs are enumerated with Trigger Source
> and Initial State populated. Every role must trace to an LT-ID or carry SECONDARY
> annotation. Every Phase entry trigger must correspond to an LT-ID or carry DERIVED
> annotation.

| LT-ID | Entry Trigger Name | Trigger Source (system event / role action / time condition; "process begins" does not count) | Initial State or Phase Activated (S-ID, Ph-ID, or named precondition; "processing starts" does not count) | Notes |
|-------|-------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | |
| Adoption context | |
| Known failure mode FM-1 | |
| Known failure mode FM-2 | |
| Known failure mode FM-3 | |
| Primary inertia driver | |

---

**OUTPUT ACCEPTANCE CRITERIA**

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 through AC-16 | *(floor criteria -- same as V-03)* | | |
| AC-17 | Lifecycle Entry Inventory | Step 0 present before STATUS-QUO; GATE 0 declared; ≥3 LT-IDs; each with Trigger Source and Initial State; Coverage Scan confirms per LT-ID | Step 0 absent; GATE 0 missing; fewer than 3 LT-IDs; blank Trigger Source or Initial State |
| AC-18 | Bidirectional exception-catalog gate coverage | UPSTREAM GATE before Exception Catalog (State Tables + Decision Tables → Exception Catalog; source and target named); DOWNSTREAM GATE before Terminal Declaration (Exception Catalog → Terminal Declaration; source and target named); Exception Catalog precedes Terminal Declaration | Either gate absent; source or target unnamed; Exception Catalog does not precede Terminal Declaration |

AC-01 through AC-16 carry the same pass and fail conditions as defined in V-03.

---

**PER-ROW QUALITY ARTIFACT REGISTRY** / **CATEGORICAL FIELD COVERAGE DECLARATION** / **DIMENSIONAL FIELD INVENTORY**

*(same as V-03 floor)*

---

**INCUMBENT COVERAGE MANDATE** / **PHASE DELTA BLOCK REQUIREMENT** / **DELTA CROSS-REFERENCE**

*(same as V-03 floor)*

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

> **GATE A**: Domain-qualified titles; ≥1 Exception Handler = Y; every role traces to an
> LT-ID or carries SECONDARY annotation.

| R-ID | Role Name (domain-qualified; generic labels do not count) | Domain | Decisions Owned | Exception Handler (Y/N; ≥1 Y) | LT-ID Trace or SECONDARY:rationale |
|------|----------------------------------------------------------|--------|-----------------|-------------------------------|-------------------------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| R-03 | | | | | |

**Status-Quo Role Comparison**

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

> **GATE B**: Every phase entry trigger traces to an LT-ID or carries DERIVED annotation;
> completion condition and SLA envelope required.

| Ph-ID | Phase Name | Entry Trigger (LT-ID trace or DERIVED:rationale) | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|--------------------------------------------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |

---

**CONSTRAINT CHAIN REGISTRY** -- BEFORE ANY PHASE

| CC-ID | Constraint Name | Originating Phase | Consuming Phase(s) | Verification Method | Incumbent Models? (Y/N/ABSENT -- blank is a hard fail) |
|-------|-----------------|------------------|--------------------|---------------------|--------------------------------------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | |
| Active roles | |
| LT-ID trace | [LT-ID(s) or DERIVED:rationale] |
| Imported constraints | |
| Constraint verification | |
| Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed) | Impact Severity (HIGH / MED / LOW -- HIGH/MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| S-01 | | | | | | |

**DECISION TABLE [Ph-ID]** *(note: C-31 not targeted; Condition column uses C-29 threshold-type taxonomy only)*

| D-ID | Decision Name | Condition (measurable threshold -- dollar amount, day count, retry count; qualitative alone does not count) | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|--------------|-------------------------------------------------------------------------------------------------------------|--------------|----------|----------|----------|---------------------------|
| D-01 | | | | | | | |

**PARALLEL PATH [Ph-ID]** / **PHASE EXIT GATE [Ph-ID]**

*(same schema as V-03)*

*Repeat per phase. Update CFCD/DFI for new categorical tables. Update PQAR for new per-row artifacts.*

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG/WEAK/ABSENT+justification; blank is a fail) | Incumbent Models? (Y/N/ABSENT+justification; blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------|-------------------------------------------------------------------|
| CC-01 | | | | | | | | |

---

> **UPSTREAM EXCEPTION-CATALOG GATE**: The exception catalog is a structurally bounded node
> that cannot be entered before the state trace is stable. Do not author the EXCEPTION CATALOG
> until all State Tables and Decision Tables across all phases are complete. Exception flows
> reference S-IDs and D-IDs by name; authoring before finalization produces untraceable
> references. Source section: State Tables and Decision Tables (all phases). Target section:
> EXCEPTION CATALOG.

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

UPSTREAM GATE must be CLOSED before opening this section.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Handler (R-ID -- Exception Handler = Y required; blank or uncertified is a structural fail) | Deviation from Happy Path (names specific states; "process stops" is a fail) | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Exception Density Note** + **Incumbent Exception Gap**

**Constraint-Break Exceptions**

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

> **DOWNSTREAM EXCEPTION-CATALOG GATE**: The exception catalog cannot be exited before
> exception flows are complete. Do not author the TERMINAL DECLARATION until all E-IDs are
> fully populated with certified Handler R-IDs and named Terminal or Recovery values.
> Source section: EXCEPTION CATALOG. Target section: TERMINAL DECLARATION.

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

DOWNSTREAM GATE must be CLOSED before opening this section.

| T-ID | Terminal Name | Type (success / failure / cancel -- "completed" does not count) | Reached From (all Ph-IDs and E-IDs; blank is a structural fail) | Incumbent Terminal? (Y/N) |
|------|---------------|----------------------------------------------------------------|----------------------------------------------------------------|--------------------------|
| T-01 | | | | |
| T-02 | | | | |

---

**EDGE CASE CATALOG** / **BOTTLENECK REGISTER** / **GAP REGISTER**

*(same schema as V-01 / V-02; forbidden exemplars apply)*

---

**COVERAGE SCAN** *(AC-01 through AC-18 plus Check V)*

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 through AC-16 | | [floor criteria] |
| AC-17 | | [Step 0 present before STATUS-QUO? GATE 0 declared? LT-IDs confirmed per row: Trigger Source and Initial State; count ≥3?] |
| AC-18 | | [UPSTREAM GATE text present before Exception Catalog? Source section named (State Tables + Decision Tables)? Target section named (Exception Catalog)? DOWNSTREAM GATE text present before Terminal Declaration? Source named (Exception Catalog)? Target named (Terminal Declaration)? Exception Catalog precedes Terminal Declaration in document order?] |

**Check V.**

> **ARTIFACT-LEVEL PRODUCTION GATE**: May not write until PASS on AC-01–AC-18 and Check V
> CLOSED. Violation produces incomplete lifecycle trace -- discard and rerun.

**Scan Summary -- Defect Type Taxonomy:**

| Defect Type | Detected By |
|-------------|------------|
| Unterminated path | AC-02 |
| Uncertified exception handler | AC-11 + C-28 |
| Missing lifecycle entry trigger | AC-17 |
| Missing exception-catalog upstream gate | AC-18 |
| Missing exception-catalog downstream gate | AC-18 |
| Missing categorical guard | AC-14 + AC-16 |

---

**INERTIA SUMMARY** / **CONSTRAINT-INCUMBENT GAP ANALYSIS**

*(same schema as V-02)*

---

**FINAL AUTHORING CHECK**

- [ ] **Step 0 LIFECYCLE ENTRY INVENTORY** first; GATE 0 declared; ≥3 LT-IDs complete
- [ ] STATUS-QUO PROCESS DECLARATION after Step 0
- [ ] AC-01 through AC-18 declared
- [ ] PQAR, CFCD (before first phase), DFI complete
- [ ] CCR before any phase; no blank Incumbent Models?
- [ ] Phase Index entries carry LT-ID trace or DERIVED annotation
- [ ] Role Registry entries carry LT-ID Trace or SECONDARY annotation
- [ ] Every phase: Entry Contract (LT-ID trace) + Delta Block + State Table + Decision Table + Parallel Path + Exit Gate
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)`
- [ ] **UPSTREAM GATE** before Exception Catalog; names State Tables + Decision Tables → Exception Catalog
- [ ] **Exception Catalog precedes Terminal Declaration**
- [ ] **DOWNSTREAM GATE** before Terminal Declaration; names Exception Catalog → Terminal Declaration
- [ ] Constraint-Break Exceptions: 5-column table; Check V CLOSED
- [ ] Coverage Scan: AC-01 through AC-18; AC-17 and AC-18 show distinct evidence

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---
<!-- END V-04 -->

## V-05 -- Axes: All Three + Full Floor (C-33 + C-32 + C-31)

**Variation axes:** All three new criteria combined. C-33: Step 0 lifecycle entry inventory
grounds all downstream schema in initiation conditions. C-32: bidirectional exception-catalog
gates bracket the exception catalog as a fully bounded structural node (Exception Catalog
before Terminal Declaration; both gates with source and target names). C-31: Decision Table
Condition column header carries both threshold-type taxonomy AND quoted concrete example
simultaneously. Full floor (CFCD, PQAR, DFI, CCR, prose guards, AC-01–AC-16) preserved.

**Hypothesis:** The three mechanisms address orthogonal structural failure surfaces. C-33
prevents schema-entry defects (unanchored roles, phases with no real trigger). C-32 prevents
lifecycle-structure defects (untraceable exception references, unverifiable terminal entries).
C-31 prevents decision-quality defects (format-ambiguous thresholds, category-boundary
ambiguous conditions). None of the three overlaps. Combining them saturates all three
surfaces simultaneously. The three new ACs (AC-17/18/19) must each enumerate distinct
evidence in Coverage Scan without cell sharing. Expected: C-31, C-32, C-33 all PASS;
AC-17/18/19 all PASS with non-overlapping evidence.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) fill LIFECYCLE ENTRY INVENTORY (Step 0) -- GATE 0
must be CLOSED, (2) declare the status-quo process, (3) declare output acceptance criteria
including AC-17 (Step 0), AC-18 (bidirectional gates), and AC-19 (dual-mechanism Decision
Condition), (4) fill PQAR, (5) fill CFCD in a single pass, (6) fill DFI, (7) register the
constraint chain. Every artifact carries incumbent comparison fields. Phase contracts import
and export named constraints by CC-ID. Exception flows caused by constraint import failures
are traced bidirectionally in a Constraint-Break Exceptions subsection. All prose and
rationale fields carry inline negative-exemplar fail-mode instructions. The exception catalog
is a structurally bounded node with bidirectional gate coverage. Every Decision Table
Condition column header carries both a threshold-type taxonomy AND a quoted concrete example.

---

**STEP 0 -- LIFECYCLE ENTRY INVENTORY** *(feeds AC-17)*

> **GATE 0**: Do not open any section until ≥3 LT-IDs are enumerated with Trigger Source
> and Initial State populated. Every role must trace to an LT-ID or carry SECONDARY
> annotation. Every Phase entry trigger must correspond to an LT-ID or carry DERIVED
> annotation.

| LT-ID | Entry Trigger Name | Trigger Source (system event / role action / time condition; "process begins" does not count) | Initial State or Phase Activated (S-ID, Ph-ID, or named precondition; "processing starts" does not count) | Notes |
|-------|-------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------|
| LT-01 | | | | |
| LT-02 | | | | |
| LT-03 | | | | |

GATE 0 is CLOSED when: ≥3 LT-IDs; each has Trigger Source and Initial State populated.

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | |
| Adoption context | |
| Known failure mode FM-1 | |
| Known failure mode FM-2 | |
| Known failure mode FM-3 | |
| Primary inertia driver | |

---

**OUTPUT ACCEPTANCE CRITERIA**

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | Blank entry condition; no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches named T-ID | Open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts carry `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell |
| AC-04 | Phase Delta Block quality | (a) block order; (b) Divergence Type enum; (c) Impact Severity enum + FM trace | Non-enum; blank; wrong order; HIGH/MED without trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase: Entry Contract + Exit Gate | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Root Cause format correct; forbidden exemplars absent | Missing column; forbidden exemplar |
| AC-09 | Incumbent field completeness | Every mandate artifact has required field | Any artifact missing field; blank |
| AC-10 | Constraint chain quality | (a) chain complete; (b) Handoff Strength; (c) Incumbent Models? | Gap; blank or invalid |
| AC-11 | Constraint-break exception tagging | 5-column subsection; traced; valid | Subsection absent; untraced break |
| AC-12 | Gap analysis completeness | (a-e) all sub-conditions | Missing section; generic rationale; blank |
| AC-13 | PQAR meta-registry | Each Reg-ID individually | Missing; bulk attestation |
| AC-14 | Cross-table categorical coverage | CFCD before first phase; Status=DECLARED | CFCD absent; Status=MISSING |
| AC-15 | Prose field negative-exemplar quality | Per-field; forbidden exemplars absent | Forbidden exemplar; bulk attestation |
| AC-16 | Dimensional Field Inventory output audit | DFI present; ≥6 fields; no out-of-vocabulary | DFI absent; fewer than 6; out-of-vocab |
| AC-17 | Lifecycle Entry Inventory | Step 0 before STATUS-QUO; GATE 0 declared; ≥3 LT-IDs with Trigger Source and Initial State; Coverage Scan confirms per LT-ID individually | Step 0 absent; GATE 0 missing; fewer than 3 LT-IDs; blank fields |
| AC-18 | Bidirectional exception-catalog gate coverage | UPSTREAM GATE before Exception Catalog (State Tables + Decision Tables → Exception Catalog; source and target named); DOWNSTREAM GATE before Terminal Declaration (Exception Catalog → Terminal Declaration; source and target named); Exception Catalog precedes Terminal Declaration | Either gate absent; source or target unnamed; ordering violated |
| AC-19 | Dual-mechanism Decision Condition operationalization | Every Decision Table Condition column header carries: (a) ≥2 named threshold-type categories (e.g., "dollar amount, day count, retry count"); AND (b) ≥1 quoted concrete passing example with comparison operator and unit (e.g., `"Invoice total > $5,000"`); both mechanisms present simultaneously in same column header; Coverage Scan names at least one decision condition cell value confirming it matches a named category and example format | Taxonomy only; example only; either mechanism in preamble; fewer than 2 categories; example missing operator; example missing unit |

AC-17, AC-18, and AC-19 Coverage Scan rows must each enumerate distinct evidence with no
cell sharing the same coverage claim across these three rows.

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | AC-ID | Sub-conditions |
|--------|---------------|------------------------|-------|----------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a-c) |
| PQAR-02 | Constraint Chain Table | Handoff Strength, Incumbent Models? | AC-10 | (a-c) |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity, Why As-Is Fails | AC-12 | (a-e) |

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? |
|------------|---------------------|-------------------|-----------------------------|---------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header enumerates allowed values | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header enumerates allowed values | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header enumerates HIGH/MED/LOW | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard before populating] | | |

---

**DIMENSIONAL FIELD INVENTORY** *(feeds AC-16)*

| DFI-ID | Field | Table | Required Values | Fail Condition | Inline Guard? |
|--------|-------|-------|----------------|----------------|--------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing/incorrect/reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH/MED/LOW + trace | blank; non-enum | Y |
| DFI-03 | Handoff Strength | CCT | STRONG/WEAK/ABSENT+justification | blank | Y |
| DFI-04 | Incumbent Models? | CCT | Y/N/ABSENT+justification | blank | Y |
| DFI-05 | Gap Severity | Gap Analysis | HIGH/MED/LOW | blank; non-enum | Y |
| DFI-06 | Type | Terminal Declaration | success/failure/cancel | blank; non-enum | [Author: Y or N] |

---

**INCUMBENT COVERAGE MANDATE** *(feeds AC-09)*

| Artifact | Required Incumbent Field |
|----------|--------------------------|
| Status-Quo Role Comparison | Per-role presence (Y/N) |
| Phase Entry Contract | `Incumbent entry` |
| Phase Exit Gate | `Incumbent exit` |
| Terminal Declaration | `Incumbent Terminal? (Y/N)` |
| Exception Catalog | `As-Is Detection? (Y/N)` |
| Bottleneck Register | `Incumbent Workaround` |
| Parallel Path block | `As-Is join` + `Incumbent gap` |
| SLA Annotation | `As-Is Typical Duration` |
| Cross-Process Handoff | `As-Is gap (Y/N)` |

**PHASE DELTA BLOCK REQUIREMENT** / **DELTA CROSS-REFERENCE REQUIREMENT**

Phase Delta Block per phase before State Table. Five artifacts carry `Delta Ref (DL-ID or NONE)`.

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

> **GATE A**: Domain-qualified titles; ≥1 Exception Handler = Y; every role traces to an
> LT-ID or carries SECONDARY annotation.

| R-ID | Role Name (domain-qualified; generic labels do not count) | Domain | Decisions Owned | Exception Handler (Y/N; ≥1 Y) | LT-ID Trace or SECONDARY:rationale |
|------|----------------------------------------------------------|--------|-----------------|-------------------------------|-------------------------------------|
| R-01 | | | | | |
| R-02 | | | | | |
| R-03 | | | | | |

**Status-Quo Role Comparison**

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

> **GATE B**: Every phase entry trigger traces to an LT-ID or carries DERIVED annotation;
> completion condition and SLA envelope required.

| Ph-ID | Phase Name | Entry Trigger (LT-ID trace or DERIVED:rationale) | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|--------------------------------------------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |

---

**CONSTRAINT CHAIN REGISTRY** -- BEFORE ANY PHASE

| CC-ID | Constraint Name | Originating Phase | Consuming Phase(s) | Verification Method | Incumbent Models? (Y/N/ABSENT -- blank is a hard fail) |
|-------|-----------------|------------------|--------------------|---------------------|--------------------------------------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | |
| Active roles | |
| LT-ID trace | [LT-ID(s) or DERIVED:rationale] |
| Imported constraints | |
| Constraint verification | |
| Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH/MED requires FM trace or "New gap"; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| S-01 | | | | | | |

**DECISION TABLE [Ph-ID: Phase Name]** *(feeds AC-05, AC-19)*

| D-ID | Decision Name | Condition (measurable threshold -- dollar amount, day count, retry count, percentage threshold; qualitative condition alone does not count; e.g., `"Invoice total > $5,000"`, `"Days past due > 30"`; format: [measure] [operator] [quantity+unit]) | Owner (R-ID; blank is a fail) | Branch A | Branch B ("otherwise" does not count) | Fallback (mechanism-impairment: role unavailable, system down, config missing) | Delta Ref (DL-ID or NONE) |
|------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|----------|---------------------------------------|--------------------------------------------------------------------------------|---------------------------|
| D-01 | | | | | | | |

**PARALLEL PATH [Ph-ID]**

```
Fork (S-ID) / Branch A / Branch B / Join condition / Merge owner (R-ID) / As-Is join / Incumbent gap
```

**PHASE EXIT GATE [Ph-ID]**

| Exit condition | Success | Failure | Blocked by | Duration | Delta source | Exported constraints | Export gap | Incumbent exit |
|----------------|---------|---------|------------|----------|-------------|---------------------|-----------|----------------|
| | | | | | | | | |

*Repeat per phase. Update CFCD/DFI for new categorical tables. Update PQAR for new per-row artifacts.*

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG/WEAK/ABSENT+justification; blank is a fail) | Incumbent Models? (Y/N/ABSENT+justification; blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------|-------------------------------------------------------------------|
| CC-01 | | | | | | | | |

---

> **UPSTREAM EXCEPTION-CATALOG GATE**: The exception catalog is a structurally bounded node
> that cannot be entered before the state trace is stable. Do not author the EXCEPTION CATALOG
> until all State Tables and Decision Tables across all phases are complete. Exception flows
> reference S-IDs and D-IDs by name; authoring before finalization produces untraceable
> references and phantom deviation paths. Source section: State Tables and Decision Tables
> (all phases complete). Target section: EXCEPTION CATALOG.

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

UPSTREAM GATE must be CLOSED before opening this section.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger (condition; "an error occurs" does not count) | Handler (R-ID -- Exception Handler = Y required; Mandatory; blank or uncertified is a structural fail) | Deviation from Happy Path (names specific states bypassed; "process stops" is a fail) | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery (T-ID or named state; "resolved" does not count) |
|------|---------------------|----------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------|---------------------------|-----------------------------------------------------------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Exception Density Note** / **Incumbent Exception Gap** (E-IDs where As-Is Detection? = N)

**Constraint-Break Exceptions** *(required for AC-11)*

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

> **DOWNSTREAM EXCEPTION-CATALOG GATE**: The exception catalog cannot be exited before
> exception flows are complete. Do not author the TERMINAL DECLARATION until all E-IDs are
> fully populated with certified Handler R-IDs and named Terminal or Recovery values. Terminal
> Declaration "Reached From" cells list E-IDs; authoring before exception flows are complete
> produces unverifiable forward references. Source section: EXCEPTION CATALOG. Target
> section: TERMINAL DECLARATION.

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

DOWNSTREAM GATE must be CLOSED before opening this section.

| T-ID | Terminal Name | Type (success / failure / cancel -- "completed" does not count) | Reached From (all Ph-IDs and E-IDs; blank is a structural fail) | Incumbent Terminal? (Y/N) |
|------|---------------|----------------------------------------------------------------|----------------------------------------------------------------|--------------------------|
| T-01 | | | | |
| T-02 | | | | |

At least 1 success terminal and 1 failure or cancel terminal required.

---

**EDGE CASE CATALOG** *(feeds AC-03)*

| EC-ID | Edge Case (concrete scenario) | Phase (Ph-ID) | Why Unhandled | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) |
|-------|-------------------------------|--------------|---------------|----------------|----------------|----------------------|---------------------------|
| EC-01 | | | | | | | |
| EC-02 | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause (format: "Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [exact cell value]"; forbidden: coordination failure, process issue, missing step, general delay) | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap (generic "missing step" is a fail -- name specific condition) | Delta Ref (DL-ID or NONE) | As-Is | Harm from Absence (generic "increases risk" is a fail -- name specific downstream harm) | Incumbent Awareness (Y/N) |
|------|---------------|------------------------------------------------------------------|---------------------------|-------|----------------------------------------------------------------------------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF** / **SLA ANNOTATION** *(optional -- feed AC-09)*

```
Handoff trigger / Recipient process / Fields passed / Acceptance condition /
As-Is gap (Y/N) / Delta source / Exported constraint
```

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(AC-01 through AC-19 plus Check V)*

Each AC confirmed individually. AC-04, AC-10, AC-12, AC-13 sub-conditions confirmed
separately. AC-14 confirms each CFCD table. AC-15 enumerates each prose field. AC-16 lists
observed values per DFI field. AC-17, AC-18, AC-19 enumerate distinct evidence -- no cell
sharing the same coverage claim.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs; failures named] |
| AC-02 | | [paths and E-IDs; open-ended named] |
| AC-03 | | [artifacts and rows; blank cells named] |
| AC-04 | | [(a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs; most-dense Ph-ID + DL-ID] |
| AC-07 | | [phases; missing contract or gate] |
| AC-08 | | [Root Cause format; forbidden exemplars confirmed absent] |
| AC-09 | | [per-artifact incumbent fields; blanks named] |
| AC-10 | | [(a) chain; (b) Handoff Strength; (c) Incumbent Models?] |
| AC-11 | | [subsection; columns; CC-ID; E-ID validity] |
| AC-12 | | [(a)-(e)] |
| AC-13 | | [PQAR-01, PQAR-02, PQAR-03 individually] |
| AC-14 | | [CFCD before phase; each table Status confirmed] |
| AC-15 | | [Root Cause values; Harm from Absence values; Why As-Is Fails values; forbidden exemplars absent from each field] |
| AC-16 | | [each DFI field; observed values listed; no out-of-vocabulary] |
| AC-17 | | [Step 0 before STATUS-QUO? GATE 0 declared? LT-IDs per row: Trigger Source confirmed; Initial State confirmed; count ≥3?] |
| AC-18 | | [UPSTREAM GATE before Exception Catalog? Source section named? Target section named? DOWNSTREAM GATE before Terminal Declaration? Source named? Target named? Ordering: Exception Catalog before Terminal Declaration confirmed?] |
| AC-19 | | [Decision Table Condition column header(s): (a) threshold-type taxonomy ≥2 categories -- categories named; (b) quoted example with comparison operator and unit -- example quoted; (c) both confirmed in same column header; (d) at least one decision condition cell value named and confirmed matching category and format] |

**Check V:** (a) CC-ID break coverage; (b) E-ID CC-ID validity; (c) E-ID main catalog presence.

> **ARTIFACT-LEVEL PRODUCTION GATE**: This artifact may not be written until Coverage Scan
> shows PASS for AC-01 through AC-19 and Check V shows CLOSED. Any scan row showing FAIL is
> a structural defect: the artifact is invalid, must be discarded, and must be rerun from
> the failed AC's source section. Violating this gate produces an incomplete lifecycle trace
> containing at least one structural defect named in the Defect Type taxonomy below.

**Scan Summary -- Defect Type Taxonomy:**

| Defect Type | Description | Detected By |
|-------------|-------------|------------|
| Unterminated path | A traced path (happy or exception) has no named T-ID | AC-02 |
| Uncertified exception handler | Handler cell not traced to Exception Handler = Y | AC-11 + C-28 |
| Unresolvable decision owner | Decision gate owner blank or generic | AC-05 |
| Missing lifecycle entry trigger | Step 0 absent or fewer than 3 LT-IDs with Trigger Source + Initial State | AC-17 |
| Missing exception-catalog upstream gate | No gate blocking exception catalog entry before state trace is stable | AC-18 |
| Missing exception-catalog downstream gate | No gate blocking terminal declaration before exception catalog complete | AC-18 |
| Taxonomy-only decision condition | Condition column header has type list but no quoted example with operator+unit | AC-19 |
| Example-only decision condition | Condition column header has quoted example but no threshold-type taxonomy | AC-19 |

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs where As-Is Detection? = N] |
| Edge cases incumbent cannot handle | [EC-IDs] |
| Terminals incumbent leaves open-ended | [T-IDs] |
| Roles absent from incumbent | [R-IDs] |
| Gaps invisible to incumbent | [G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed or open] |
| Entry triggers incumbent cannot initiate | [LT-IDs] |

---

**CONSTRAINT-INCUMBENT GAP ANALYSIS** *(required for CC-IDs with Incumbent Models? = N -- feeds AC-12 / PQAR-03)*

One row per CC-ID where Incumbent Models? = N. NONE + justification if none qualify.

| CC-ID | Constraint Name | Gap Severity (HIGH / MED / LOW -- blank is a fail) | Why As-Is Fails (specific process characteristic; forbidden: not implemented, lacking, insufficient, not modeled) |
|-------|-----------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| | | | |

---

**FINAL AUTHORING CHECK**

- [ ] **LIFECYCLE ENTRY INVENTORY (Step 0)** is the FIRST section; GATE 0 declared; ≥3 LT-IDs with Trigger Source and Initial State
- [ ] STATUS-QUO PROCESS DECLARATION after Step 0
- [ ] OUTPUT ACCEPTANCE CRITERIA: AC-01 through AC-19 declared
- [ ] PQAR: PQAR-01/02/03 complete
- [ ] CFCD: before first phase; all tables Status = DECLARED
- [ ] DFI: ≥6 fields present before first phase
- [ ] CONSTRAINT CHAIN REGISTRY: before any phase; no blank Incumbent Models?
- [ ] Phase Index: every entry carries LT-ID trace or DERIVED annotation
- [ ] Role Registry: every role carries LT-ID Trace or SECONDARY annotation
- [ ] Every phase: Entry Contract (LT-ID trace) + Phase Delta Block (before State Table) + State Table + **Decision Table with dual-mechanism Condition column header** + Parallel Path + Exit Gate
- [ ] **Every Decision Table Condition column header carries: ≥2 threshold-type categories AND ≥1 quoted example with comparison operator and unit -- both in same header simultaneously**
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column (exact name)
- [ ] **UPSTREAM GATE** present before EXCEPTION CATALOG; names State Tables + Decision Tables → Exception Catalog
- [ ] **EXCEPTION CATALOG precedes TERMINAL DECLARATION in document order**
- [ ] **DOWNSTREAM GATE** present before TERMINAL DECLARATION; names Exception Catalog → Terminal Declaration
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V CLOSED
- [ ] Coverage Scan: AC-01 through AC-19 + Check V; each confirmed individually; AC-17/18/19 show distinct evidence with no cell sharing
- [ ] Artifact-level production gate not violated

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.
