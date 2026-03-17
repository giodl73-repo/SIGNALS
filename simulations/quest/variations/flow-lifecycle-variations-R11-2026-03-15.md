|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID: Phase Name]** — Author AFTER Phase Delta Block *(feeds AC-01, AC-03)*

| S-ID | State Name | Entry Condition (names specific event; "after previous step" does not count) | Happy-Path Exit (labeled transition) | Exception Exit | Owner (R-ID; blank is a fail) | Delta Ref (DL-ID or NONE) |
|------|------------|------------------------------------------------------------------------------|--------------------------------------|----------------|-------------------------------|---------------------------|
| S-01 | | | | | | |

**DECISION TABLE [Ph-ID: Phase Name]** *(feeds AC-05, AC-19)*

| D-ID | Decision Name | Condition (measurable threshold — dollar amount, day count, retry count, percentage threshold; e.g., `"Invoice total > $5,000"`, `"Days past due > 30"`; qualitative condition alone does not count; format: [measure] [operator] [quantity+unit]) | Owner (R-ID; blank is a fail) | Branch A | Branch B ("otherwise" does not count) | Fallback (mechanism-impairment: role unavailable, system down, config missing; names holding state or escalation target) | Delta Ref (DL-ID or NONE) |
|------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|----------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------|
| D-01 | | | | | | | |

**PARALLEL PATH [Ph-ID: Phase Name]**

```
Fork (S-ID):       [branching state]
Branch A:          [concurrent path]
Branch B:          [concurrent path]
Join condition:    [specific condition; "both complete" does not count]
Merge owner:       [R-ID]
As-Is join:        [incumbent join behavior or ABSENT]
Incumbent gap:     [what breaks in incumbent if join fails or N/A]
```

**PHASE EXIT GATE [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Exit condition | [What must be true; "work is done" does not count] |
| Success transition | [Ph-ID or T-ID] |
| Failure transition | [T-ID or named exception] |
| Blocked by | [Role, resource, or condition; NONE requires explicit justification] |
| Typical duration | |
| Delta source | [DL-IDs or NONE] |
| Exported constraints | [CC-IDs: constraint name and verified state] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How incumbent transitions out — or ABSENT] |

*Repeat Entry Contract → Phase Delta Block → State Table → Decision Table → Parallel Path → Exit Gate for each phase. Update CFCD and DFI immediately if new categorical-field table introduced. Update PQAR immediately if new per-row quality artifact introduced.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases — feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT+justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT+justification; blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

**Constraint Gap Note:** List every ABSENT or WEAK transition with missing constraint and risk.

---

> **UPSTREAM EXCEPTION-CATALOG GATE**: The exception catalog is a structurally bounded node that cannot be entered before the state trace is stable. Do not author the EXCEPTION CATALOG until all State Tables and Decision Tables across all phases are complete. Exception flows reference S-IDs and D-IDs by name; authoring before finalization produces untraceable references and phantom deviation paths. Source section: State Tables and Decision Tables (all phases complete). Target section: EXCEPTION CATALOG.

---

**EXCEPTION CATALOG** *(UPSTREAM GATE must be CLOSED — feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger (names condition that diverts from happy path; "an error occurs" does not count) | Handler (R-ID — Must trace to a role with Exception Handler = Y in Role Registry; Mandatory; blank or uncertified role is a structural fail) | Deviation from Happy Path (names specific states bypassed or added; "process stops" is a fail) | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery (T-ID or named recovery state; "resolved" does not count) |
|------|---------------------|----------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------|---------------------------|--------------------------------------------------------------------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation. *(AC-06)*
**Incumbent Exception Gap:** E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions** *(required for AC-11)*

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

> **DOWNSTREAM EXCEPTION-CATALOG GATE**: The exception catalog cannot be exited before exception flows are complete. Do not author the TERMINAL DECLARATION until all E-IDs are fully populated with certified Handler R-IDs and named Terminal or Recovery values. Terminal Declaration "Reached From" cells list E-IDs; authoring before exception flows are complete produces unverifiable forward references. Source section: EXCEPTION CATALOG. Target section: TERMINAL DECLARATION.

---

**TERMINAL DECLARATION** *(DOWNSTREAM GATE must be CLOSED — feeds AC-02, AC-09)*

| T-ID | Terminal Name | Type (success / failure / cancel — "completed" does not count) | Reached From (all Ph-IDs and E-IDs; blank is a structural fail) | Incumbent Terminal? (Y/N) |
|------|---------------|----------------------------------------------------------------|----------------------------------------------------------------|--------------------------|
| T-01 | | | | |
| T-02 | | | | |

At least 1 success terminal and 1 failure or cancel terminal required.

---

**EDGE CASE CATALOG** *(feeds AC-03)*

| EC-ID | Edge Case (concrete scenario, not category) | Phase (Ph-ID) | Why Unhandled (names specific design decision or omission; "not considered" does not count) | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) |
|-------|---------------------------------------------|--------------|-------------------------------------------------------------------------------------------|----------------|----------------|----------------------|---------------------------|
| EC-01 | | | | | | | |
| EC-02 | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause (required format: "Phase Delta [Ph-ID] [DL-ID] — Current Process Step: [exact cell value]" or "Phase Exit Gate [Ph-ID] — Blocked by: [exact cell value]"; forbidden: coordination failure, process issue, approval bottleneck, missing step, general delay) | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap (generic "missing step" or "gap exists" is a fail — name the specific missing condition or gated transition) | Delta Ref (DL-ID or NONE) | As-Is | Harm from Absence (generic "increases risk" or "causes delays" is a fail — name specific downstream harm mechanism and artifact affected) | Incumbent Awareness (Y/N) |
|------|---------------|------------------------------------------------------------------------------------------------------------------|---------------------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF / SLA ANNOTATION** *(optional — feed AC-09)*

```
Handoff trigger / Recipient process / Fields passed / Acceptance condition /
As-Is gap (Y/N) / Delta source / Exported constraint
```

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(AC-01 through AC-23 plus Check V)*

> **Non-Overlapping Evidence Mandate**: This scan table includes a `Distinct Evidence (Y/N)` column for all gate-backed aspirational criteria rows (AC-17 through AC-23). **Mandatory: no row's Evidence cell may share the same schema-element citation as another row in this group. Identical evidence language across two rows is a structural fail — mark Distinct Evidence = N and treat as a scan failure.** Each gate-backed aspirational criterion must be verified by evidence drawn from a distinct section of the schema. This column is the enforcement mechanism for AC-21 and is also verified by AC-21 itself (AC-21's Distinct Evidence cell must cite the column definition and per-row Y values as its distinct evidence — not the same element as any other row).

Each AC confirmed individually. AC-04, AC-10, AC-12, AC-13 sub-conditions confirmed separately. AC-14 confirms each CFCD table by name. AC-15 enumerates each prose field by name. AC-16 lists observed output values per DFI field. AC-22 confirms each R-ID and Ph-ID backward trace individually. Any FAIL must be corrected before output.

| AC-ID | Result | Evidence or Failure Detail | Distinct Evidence (Y/N — Mandatory for AC-17 through AC-23; no row's Evidence cell may share a schema-element citation with another row in this group; N is a structural fail) |
|-------|--------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC-01 | | [S-IDs; each has Entry Condition and labeled exit; failures named] | N/A |
| AC-02 | | [paths and E-IDs enumerated; open-ended entries named] | N/A |
| AC-03 | | [five artifacts; per-row Delta Ref column present; blank cells named] | N/A |
| AC-04 | | [(a) block-before-state-table per phase confirmed; (b) Divergence Type values enumerated; (c) Impact Severity values; HIGH/MED FM traces confirmed] | N/A |
| AC-05 | | [every decision owner and state owner: R-ID cited; generic labels named] | N/A |
| AC-06 | | [E-IDs; Ph-ID per E-ID; most-dense Ph-ID named + DL-ID cited] | N/A |
| AC-07 | | [phases enumerated; Entry Contract present + Exit Gate present per phase; Blocked by populated] | N/A |
| AC-08 | | [Bottleneck Register Root Cause format per row; Gap Register Harm from Absence per row; forbidden exemplars confirmed absent] | N/A |
| AC-09 | | [per-artifact incumbent field: each artifact named individually; blank fields named] | N/A |
| AC-10 | | [(a) CC-ID chain: every exported CC-ID appears imported; (b) Handoff Strength values; (c) Incumbent Models? values; blank cells named] | N/A |
| AC-11 | | [Constraint-Break Exceptions subsection: 5-column table present; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog] | N/A |
| AC-12 | | [(a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails specific; (e) no blank Incumbent Models?] | N/A |
| AC-13 | | [PQAR-01: sub-conditions (a)–(c) confirmed; PQAR-02: sub-conditions (a)–(c) confirmed; PQAR-03: sub-conditions (a)–(e) confirmed; each Reg-ID individually] | N/A |
| AC-14 | | [CFCD authored before first phase confirmed; each table in CFCD named: Status=DECLARED confirmed per table; any MISSING tables named] | N/A |
| AC-15 | | [Root Cause field: forbidden exemplars (coordination failure, process issue, missing step, general delay) confirmed absent; Harm from Absence field: forbidden exemplars (increases risk, causes delays) confirmed absent; Why As-Is Fails field: forbidden exemplars (not implemented, lacking, insufficient) confirmed absent — each field named individually] | N/A |
| AC-16 | | [DFI present before first phase; ≥6 fields confirmed; each DFI field named; observed output values listed per field; no out-of-vocabulary values] | N/A |
| AC-17 | | [Step 0 is first section; Coverage Table present before STATUS-QUO; GATE 0 declared; LT-01: Trigger Source [value] + Initial State [value] confirmed; LT-02: confirmed; LT-03: confirmed; count ≥3 — evidence drawn exclusively from STEP 0 LIFECYCLE ENTRY INVENTORY section] | [Y / N] |
| AC-18 | | [UPSTREAM GATE text present before Exception Catalog: Source "State Tables and Decision Tables (all phases)" named, Target "EXCEPTION CATALOG" named; DOWNSTREAM GATE text present before Terminal Declaration: Source "EXCEPTION CATALOG" named, Target "TERMINAL DECLARATION" named; document ordering: Exception Catalog precedes Terminal Declaration confirmed — evidence drawn exclusively from gate text blocks] | [Y / N] |
| AC-19 | | [Decision Table Condition column header(s): (a) threshold-type categories named (dollar amount / day count / retry count — categories cited verbatim); (b) quoted concrete example with comparison operator and unit cited verbatim; (c) both mechanisms confirmed in same column header; (d) ≥1 decision condition cell value named and confirmed matching category type and example format — evidence drawn exclusively from Decision Table column header definitions and one cell value] | [Y / N] |
| AC-20 | | [ORTHOGONAL FAILURE SURFACE TAXONOMY block present; positioned after STATUS-QUO and before Domain Role Registry confirmed by document order; FS-01: all four fields populated; FS-02: all four fields populated; FS-03: all four fields populated; FS-04: all four fields populated; no two rows share defect class confirmed — evidence drawn exclusively from ORTHOGONAL FAILURE SURFACE TAXONOMY block] | [Y / N] |
| AC-21 | | [Distinct Evidence column present in Coverage Scan table (not only preamble): column header mandate text confirmed as "Mandatory; no row's Evidence cell may share a schema-element citation with another row in this group; N is a structural fail" or equivalent prohibition inline in column header; AC-17 Distinct Evidence = Y confirmed; AC-18 Distinct Evidence = Y confirmed; AC-19 Distinct Evidence = Y confirmed; AC-20 Distinct Evidence = Y confirmed; AC-22 Distinct Evidence = Y confirmed; AC-23 Distinct Evidence = Y confirmed; no two rows in AC-17/18/19/20/21/22/23 group share identical Evidence cell language — evidence drawn exclusively from this scan table's column header definition and per-row Y/N values] | [Y / N] |
| AC-22 | | [Coverage Table present before STATUS-QUO confirmed; R-01 LT-ID Scope: [LT-ID cited] verified in Coverage Table Phases Activated for R-01's domain; R-02: verified; R-03: verified; SECONDARY annotations (if any) named with rationale; PH-01 LT-ID Trace: [LT-ID cited] verified in Coverage Table Initial Phase = PH-01; PH-02: verified; DERIVED annotations (if any) named; Phase Entry Contracts: LT-ID trace fields verified per phase — evidence drawn exclusively from STEP 0 TRACEABILITY COVERAGE TABLE and Role Registry LT-ID Scope / Phase Index LT-ID Trace columns] | [Y / N] |
| AC-23 | | [Defect Type Taxonomy: Row "Taxonomy-only decision condition" present — Defect Type name confirmed, description confirms category list present + quoted example absent, Detected By AC-19/C-31 confirmed; Row "Example-only decision condition" present — Defect Type name confirmed, description confirms quoted example present + category list absent, Detected By AC-19/C-31 confirmed; two rows are distinct entries (not merged); Defect Type names differ — evidence drawn exclusively from Scan Summary Defect Type Taxonomy table rows] | [Y / N] |

**Check V:** (a) CC-ID break coverage complete; (b) E-ID CC-ID validity confirmed; (c) E-ID main catalog presence confirmed. Any FAIL must be corrected before output.

> **ARTIFACT-LEVEL PRODUCTION GATE**: This artifact may not be written until Coverage Scan shows PASS for AC-01 through AC-23 and Check V shows CLOSED. Any scan row showing FAIL is a structural defect: the artifact is invalid, must be discarded, and must be rerun from the failed AC's source section. Violating this gate produces an incomplete lifecycle trace where at least one path has no named terminal, at least one gate domain has no failure-surface mapping, or at least one dual-mechanism criterion has an untyped defect in the scan taxonomy — each a named structural defect in the Defect Type taxonomy below.

**Scan Summary — Defect Type Taxonomy:**

| Defect Type | Description | Detected By |
|-------------|-------------|------------|
| Unterminated path | A traced path (happy or exception) has no named T-ID | AC-02 |
| Uncertified exception handler | Handler cell carries R-ID without Exception Handler = Y in registry | AC-11 |
| Unresolvable decision owner | Decision gate owner cell blank or generic | AC-05 |
| Missing lifecycle entry trigger | Step 0 absent or fewer than 3 LT-IDs with Trigger Source and Initial State | AC-17 |
| Missing exception-catalog upstream gate | No gate blocking exception catalog entry before state trace is stable | AC-18 |
| Missing exception-catalog downstream gate | No gate blocking terminal declaration before exception catalog complete | AC-18 |
| **Taxonomy-only decision condition** | Condition column header carries threshold-type category enumeration (e.g., "dollar amount, day count, retry count") AND quoted concrete example with comparison operator and unit is absent — mechanism A present, mechanism B absent | AC-19 / C-31 |
| **Example-only decision condition** | Condition column header carries a quoted concrete example with comparison operator and unit (e.g., `"Invoice total > $5,000"`) AND threshold-type category enumeration is absent — mechanism B present, mechanism A absent | AC-19 / C-31 |
| Missing gate-to-failure-surface mapping | No pre-schema block mapping gates to their failure surfaces; gate purpose cannot be verified before authoring begins | AC-20 |
| Cross-row evidence sharing | Two gate-backed aspirational scan rows cite the same schema element as their evidence basis | AC-21 |
| Unanchored role | A role's LT-ID Scope cites an LT-ID not verified in the Coverage Table for that role's phases | AC-22 |
| Phantom phase LT-ID | A phase's LT-ID Trace cites an LT-ID whose Initial Phase does not match this phase in the Coverage Table | AC-22 |

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
| Gates with no failure-surface mapping in incumbent | [FS-IDs where Closed By gate has no incumbent equivalent] |

---

**CONSTRAINT-INCUMBENT GAP ANALYSIS** *(required for CC-IDs with Incumbent Models? = N — feeds AC-12 / PQAR-03)*

One row per CC-ID where Incumbent Models? = N. Write NONE + justification if none qualify.

| CC-ID | Constraint Name | Gap Severity (HIGH / MED / LOW — blank is a fail) | Why As-Is Fails (must name specific process characteristic; forbidden: not implemented, lacking this feature, insufficient, not modeled, unsupported) |
|-------|-----------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| | | | |

---

**FINAL AUTHORING CHECK**

- [ ] **LIFECYCLE ENTRY INVENTORY (Step 0)** is the FIRST section; GATE 0 declared; ≥3 LT-IDs with Trigger Source and Initial State
- [ ] **STEP 0 TRACEABILITY COVERAGE TABLE** present before STATUS-QUO PROCESS DECLARATION; every LT-ID has Phases Activated and Roles Active populated
- [ ] STATUS-QUO PROCESS DECLARATION present after Coverage Table
- [ ] **ORTHOGONAL FAILURE SURFACE TAXONOMY** present after STATUS-QUO and before Domain Role Registry; ≥3 FS-IDs (recommend ≥4); each with Failure Surface Name, Defect Category, Closed By gate/criterion, and Example Defective Artifact; no two rows share defect class
- [ ] OUTPUT ACCEPTANCE CRITERIA: AC-01 through AC-23 declared
- [ ] PQAR: PQAR-01/02/03 complete; no new artifact introduced without PQAR row
- [ ] CFCD: authored before first phase; all tables Status = DECLARED at scan
- [ ] DFI: ≥6 fields present before first phase
- [ ] CONSTRAINT CHAIN REGISTRY: authored before any phase; no blank Incumbent Models?
- [ ] Role Registry: every role carries **LT-ID Scope** column — cites Coverage Table LT-ID(s) or SECONDARY:rationale; ≥1 Exception Handler = Y
- [ ] Phase Index: every phase has separate **Entry Trigger Name** column AND **LT-ID Trace** column — LT-ID Trace cites Coverage Table LT-ID or DERIVED:rationale
- [ ] Every phase: Entry Contract (**LT-ID trace field** verified against Coverage Table) + Phase Delta Block (before State Table) + State Table + **Decision Table (Condition column header: ≥2 threshold categories AND quoted example with operator+unit — both in same header simultaneously)** + Parallel Path + Exit Gate
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column (exact name)
- [ ] **UPSTREAM GATE** present before EXCEPTION CATALOG; names "State Tables and Decision Tables (all phases)" → "EXCEPTION CATALOG"
- [ ] **EXCEPTION CATALOG precedes TERMINAL DECLARATION** in document order
- [ ] **DOWNSTREAM GATE** present before TERMINAL DECLARATION; names "EXCEPTION CATALOG" → "TERMINAL DECLARATION"
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed CLOSED
- [ ] Coverage Scan: AC-01 through AC-23 + Check V; each AC confirmed individually
- [ ] Coverage Scan includes **`Distinct Evidence (Y/N)` column** with inline mandate in column header; AC-17/18/19/20/21/22/23 each have Distinct Evidence = Y; no two rows share identical Evidence language
- [ ] Defect Type Taxonomy: **"Taxonomy-only decision condition"** and **"Example-only decision condition"** appear as **separate rows** with distinct Defect Type names and distinct Detected By entries
- [ ] Artifact-level production gate not violated

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

<!-- END V-05 -->
