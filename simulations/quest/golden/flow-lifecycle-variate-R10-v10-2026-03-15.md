---
skill: flow-lifecycle
round: 10
rubric-version: v10
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v10-2026-03-15.md
floor: flow-lifecycle-variate-R10-2026-03-15.md V-05
---

# flow-lifecycle -- Round 10 Variations (v10 rubric: C-28, C-29, C-30)

Round 10 (v10) holds the R10 V-05 full floor (PQAR registry + boundary scan + live update
policy + Phase Delta Block and CCT schema-AC parity) and probes the three criteria added
to the v10 rubric from R9 scoring.

**Three failure modes to probe:**

| Mode | Criterion | What R10 V-05 does | What v10 requires |
|------|-----------|-------------------|------------------|
| Incremental table coverage | C-28 | Inline guards on PQAR-01/02/03 tables only | Single-pass declaration across ALL categorical-field tables; mechanism confirms no table exempt because added in prior round |
| Positive-only prose direction | C-29 | "Generic language is a fail" in Gap Analysis prose note only | ALL prose/rationale fields carry named fail mode inline; negative exemplars named -- not just "be specific" |
| Silent categorical field gap | C-30 | Inline guards in column headers of registered artifacts | Dedicated AC enumerates specific fields by name; scan audits output values -- operational even when inline headers are absent |

Single-axis: V-01 (C-28), V-02 (C-29), V-03 (C-30).
Combined: V-04 (C-28 + C-30), V-05 (all three + full floor).

**Round 10 (v10) hypothesis matrix:**

| Variation | C-28 Single-Pass | C-29 Prose Guard | C-30 Field Inventory | Primary Test |
|-----------|:---------------:|:----------------:|:--------------------:|-------------|
| V-01 | TARGET | HOLD | NONE | CFCD section + AC-14 forces single-pass enumeration before phase authoring |
| V-02 | HOLD | TARGET | NONE | Negative-exemplar inline instructions on all prose fields; no new section |
| V-03 | HOLD | NONE | TARGET | DIMENSIONAL FIELD INVENTORY + AC-14 scans output values as detection fallback |
| V-04 | TARGET | NONE | TARGET | Both structural mechanisms; prose guards absent |
| V-05 | TARGET | TARGET | TARGET | Full v10 floor; maximum dimensional enforcement integrity |

---

## V-01 -- Axis: Lifecycle Emphasis (C-28 Single-Pass Categorical Coverage Declaration)

**Variation axis:** Lifecycle emphasis -- before any phase is authored, a mandatory
CATEGORICAL FIELD COVERAGE DECLARATION (CFCD) is filled in a single pass. This section
enumerates every table in the model that carries categorical fields, names the inline guard
form for each field, and records Status (DECLARED / MISSING). The declaration must be
authored as a single sweep -- not table-by-table as phases are filled. A new AC-14 verifies
that the declaration was authored before phase authoring and that no table with categorical
fields is exempt. The PQAR registry (PQAR-01/02/03) and all R10 V-05 floor elements are
unchanged.

**Hypothesis:** R10 V-05 applies inline guards to the three PQAR-registered artifacts but
does not guarantee that ALL tables with categorical fields received guards in a single pass.
A model may correctly guard Phase Delta Block and CCT while leaving the Terminal Declaration
`Type` field (success/failure/cancel) or an additional table introduced mid-authoring without
an inline guard -- because those tables were filled before the PQAR mechanism was considered.
The single-pass declaration forces enumeration of all categorical-field tables before any
phase is authored. Expected: C-28 PASS if declaration is complete and pre-phase; any table
omitted will fail AC-14.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including all sub-conditions, (3) fill the
PER-ROW QUALITY ARTIFACT REGISTRY, (4) fill the CATEGORICAL FIELD COVERAGE DECLARATION in a
single pass naming every table with categorical fields -- this declaration must be complete
before any phase is authored; adding a table after phase authoring begins requires an
immediate CFCD update, (5) register the constraint chain with explicit incumbent coverage
flags. Every artifact carries incumbent comparison fields. Phase contracts import and export
named constraints by CC-ID. Exception flows caused by constraint import failures are traced
bidirectionally in a dedicated Constraint-Break Exceptions subsection. The cross-axis bridge
is synthesized in a severity-rated, rationale-equipped Constraint-Incumbent Gap Analysis
verified by a five-condition acceptance check. Phase Delta Blocks and the Constraint Chain
Table carry inline column-level quality constraints. The PQAR table is the authoritative list
of per-row quality artifacts; any new artifact requires a new PQAR row before continuing.

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | [Name of the as-is process or workflow tool currently in use] |
| Adoption context | [Who uses it and at what scale] |
| Known failure mode FM-1 | [Specific named failure] |
| Known failure mode FM-2 | [Same format] |
| Known failure mode FM-3 | [Same format] |
| Primary inertia driver | [Why this process persists] |

---

**OUTPUT ACCEPTANCE CRITERIA**

Declared before any content is authored. Post-fill scan executes these IDs -- does not restate
pass conditions.

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts have `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block schema and quality | (a) each phase has rubric-exact block before State Table; (b) every Divergence Type cell is exactly `missing`, `incorrect`, or `reversed`; (c) every Impact Severity cell is `HIGH`, `MED`, or `LOW`; HIGH/MED rows cite FM or "New gap" | Wrong column names; model-level block; wrong order; non-enumerated Divergence Type value; blank or non-enumerated Impact Severity; HIGH/MED row without FM trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Bottleneck + Gap Registers have Root Cause citing source artifact and field | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every artifact in Incumbent Coverage Mandate has required field populated | Any artifact missing its field; any blank incumbent field |
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported appears as imported in consuming phase; (b) every Handoff Strength cell is STRONG, WEAK, or ABSENT-with-justification; (c) every Incumbent Models? cell in CCT is Y, N, or ABSENT-with-justification | Any CC-ID with no consuming import; blank or invalid Handoff Strength; blank or invalid Incumbent Models? in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent or prose-only; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | Gap analysis completeness | (a) Constraint-Incumbent Gap Analysis is a named structural section; (b) every CC-ID with Incumbent Models? = N has a row; (c) each row carries Gap Severity (HIGH/MED/LOW); (d) each row carries Why As-Is Fails naming a specific process characteristic; (e) no blank Incumbent Models? cells in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; row with generic rationale; blank Incumbent Models? cell |
| AC-13 | Per-row quality artifact meta-registry | See PER-ROW QUALITY ARTIFACT REGISTRY. Coverage Scan must verify each Reg-ID individually -- bulk attestation is a fail. If any new per-row quality artifact is introduced during authoring, a new PQAR row is required before continuing | Any Reg-ID missing; per-Reg-ID verification omitted; new artifact introduced without PQAR update |
| AC-14 | Cross-table categorical coverage (single-pass) | CATEGORICAL FIELD COVERAGE DECLARATION present and authored before first phase; all tables with categorical fields listed; every listed table shows Status = DECLARED; Coverage Scan AC-14 confirms each table individually -- any table with Status = MISSING is a fail; if a new categorical-field table was introduced after CFCD was authored, it must appear as a CFCD update row | CFCD absent; any table with categorical fields not listed; declaration authored incrementally (table added after first phase); any categorical field with Status = MISSING at Coverage Scan |

These fourteen checks are the acceptance definition. AC-13 points to the PQAR. AC-14 points
to the CFCD. Coverage Scan AC-04, AC-10, AC-12, AC-13 sub-conditions must be confirmed
individually. Coverage Scan AC-14 must name each table in the CFCD and confirm Status.

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(canonical registry -- feeds AC-13)*

This table is the authoritative list of all structural artifacts in this model that carry
declared per-row quality requirements. Adding a new structural artifact with a severity
column, rationale column, or compliance flag requires inserting a new row before continuing.

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity values + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | AC-12 | (a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails per row; (e) no blank Incumbent Models? |

Coverage Scan AC-13 row must confirm PQAR-01, PQAR-02, and PQAR-03 individually by Reg-ID.

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

Author this table completely before authoring any phase. List every table in this model that
carries at least one categorical field (value enumeration or typed compliance flag). For each,
name the inline guard form and record Status. Status must be DECLARED for every row at the
Coverage Scan. If a new table with categorical fields is introduced during authoring, add a row
immediately and record the phase at which it was added.

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? (Phase) |
|------------|---------------------|-------------------|-----------------------------|-----------------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header enumerates allowed values; blank/non-enum is a fail | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header enumerates allowed values; blank is a fail | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header enumerates HIGH/MED/LOW | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard or record MISSING] | | |
| State Table | Owner (R-ID), Happy-Path Exit (labeled) | [Author: assess -- are these categorical? Add guard or record N/A] | | |
| [Any additional table discovered] | | | | |

Any row with Status = MISSING at Coverage Scan is an AC-14 fail. A categorical field without
an inline guard may use AC-only enforcement only if that AC explicitly names the field and
enumerates its allowed values -- "all fields" in aggregate is not sufficient.

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

Each lifecycle phase contains a mandatory Phase Delta Block authored BEFORE the State Table.
Quality constraints are embedded inline in each column header.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

If no divergences exist: write "No divergence" in Current Process Step.

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact name):
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-NN | ... | | |

**Status-Quo Role Comparison** *(dedicated artifact -- feeds AC-09)*

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-NN | ... | | |

---

**CONSTRAINT CHAIN REGISTRY** -- AUTHOR BEFORE ANY PHASE *(feeds AC-10, AC-12)*

| CC-ID | Constraint Name | Originating Phase (Ph-ID) | Consuming Phase(s) (Ph-ID) | Verification Method | Incumbent Models? (Y/N) |
|-------|-----------------|--------------------------|---------------------------|---------------------|------------------------|
| CC-01 | | | | | |
| CC-NN | ... | | | | |

`Incumbent Models?` rules: Y / N / ABSENT-with-justification. Blank is a hard fail for AC-12.
N entries must appear in the Constraint-Incumbent Gap Analysis.

---

**FOR EACH PHASE, IN THIS EXACT ORDER:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

---

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Entry condition | [Specific precondition] |
| Prior phase | [Ph-ID or INITIAL] |
| Active roles | [R-IDs] |
| Objects entering | [Named artifacts] |
| Exception pre-check | [Blocking conditions] |
| Imported constraints | [CC-IDs from prior phase Exit Gate -- or INITIAL if first phase] |
| Constraint verification | [How roles verify each imported CC-ID -- or N/A if first phase] |
| Incumbent entry | [How the incumbent triggers this phase -- or ABSENT] |

---

**PHASE DELTA BLOCK [Ph-ID: Phase Name]** -- AUTHOR BEFORE STATE TABLE *(feeds AC-04 / PQAR-01)*

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| DL-01 | | | | |

---

**STATE TABLE [Ph-ID: Phase Name]** -- Author AFTER Phase Delta Block *(feeds AC-01, AC-03)*

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| | | | | | | |

**Decision Table [Ph-ID: Phase Name]** *(feeds AC-05)*

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|--------------|----------|----------|----------|---------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID: Phase Name]** *(feeds AC-09)*

```
Fork (S-ID):    [branching state]
Branch A:       [named path]
Branch B:       [named path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
As-Is join:     [incumbent join behavior -- or ABSENT]
Incumbent gap:  [what breaks in the incumbent if join condition fails -- or N/A]
```

---

**PHASE EXIT GATE [Ph-ID: Phase Name]** *(feeds AC-07, AC-09, AC-10)*

| Field | Value |
|-------|-------|
| Exit condition | [What must be true for phase to complete] |
| Success transition | [Ph-ID or T-ID] |
| Failure transition | [T-ID or exception name] |
| Blocked by | [role, resource, or condition -- NONE requires explicit justification] |
| Typical duration | [Expected elapsed time] |
| Delta source | [DL-IDs explaining blocking -- or NONE] |
| Exported constraints | [CC-IDs this phase exports. Format: CC-NN: [constraint name and verified state]] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How the incumbent transitions out -- or ABSENT] |

---

*Repeat for each phase. Update CCR and PQAR if new per-row quality artifacts introduced.
Update CFCD immediately if a new categorical-field table is introduced.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification note; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

At least one STRONG Handoff Strength required. ABSENT requires inline justification.

**Constraint Gap Note:** List every ABSENT or WEAK transition with missing constraint and risk.

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) | Incumbent Terminal? (Y/N) |
|------|---------------|-----------------------------------|---------------------------------|--------------------------|
| T-01 | | | | |

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|---------------------------|----------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation. *(AC-06)*

**Incumbent Exception Gap:** List E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions** *(dedicated subsection -- required for AC-11)*

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

Bidirectional traceability: every CC-ID break has E-ID; every E-ID traces to valid CC-ID and
main catalog. Check V audits. Resolve before output.

---

**EDGE CASE CATALOG** *(feeds AC-03)*

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|---------------|---------|----------------|----------------|----------------------|---------------------------|-----------------|
| EC-01 | | | | | | | | |
| EC-02 | | | | | | | | |
| EC-03 | | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [exact cell value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [exact cell value]`

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence | Incumbent Awareness (Y/N) |
|------|---------------|-----|---------------------------|------------------------|-------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)** *(feeds AC-09 if authored)*

```
Handoff trigger:       [Event initiating handoff]
Recipient process:     [Named adjacent process]
Fields passed:         [Named data elements]
Acceptance condition:  [What recipient verifies]
As-Is gap:             [Y/N + note]
Delta source:          [DL-ID or NONE]
Exported constraint:   [CC-ID governing this handoff -- or NONE]
```

**SLA ANNOTATION (raise score)** *(feeds AC-09 if authored)*

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-14 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-04, AC-10, AC-12, AC-13
sub-conditions must be confirmed individually. AC-14 must name each table in the CFCD and
confirm Status = DECLARED.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order per phase; (b) Divergence Type values enumerated; (c) Impact Severity + FM-trace confirmed] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs checked; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [registers; Root Cause format confirmed per row] |
| AC-09 | | [per-artifact incumbent field completeness; blanks named] |
| AC-10 | | [(a) chain completeness per CC-ID; (b) Handoff Strength values -- blanks named; (c) Incumbent Models? -- blanks named] |
| AC-11 | | [subsection present? each entry has CC-ID + Ph-ID? CC-ID break coverage? E-ID validity?] |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [PQAR-01 confirmed individually; PQAR-02 confirmed individually; PQAR-03 confirmed individually; any new Reg-ID rows?] |
| AC-14 | | [CFCD present before phase authoring? Each table named in CFCD: Status = DECLARED confirmed per table; any Status = MISSING?; any categorical-field table not in CFCD?; any CFCD update rows added mid-authoring?] |

**Check V:** (a) CC-ID break coverage; (b) E-ID CC-ID validity; (c) E-ID main catalog presence.
Any FAIL must be corrected. Self-attestation is not acceptable.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs] |
| Edge cases incumbent cannot handle | [EC-IDs] |
| Terminals incumbent leaves open-ended | [T-IDs] |
| Roles absent from incumbent | [R-IDs] |
| Gaps invisible to incumbent | [G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed] |

**Constraint-Incumbent Gap Analysis** *(required when any CC-ID has `Incumbent Models? = N` -- feeds AC-12)*

One row per CC-ID where `Incumbent Models? = N`. Explicit NONE with justification if none.

Gap Severity: HIGH (critical-path or compliance) / MED (rework or escalation) / LOW (minor inefficiency).
`Why As-Is Fails` must name a specific process characteristic. Generic language is a fail.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA is second with AC-01 through AC-14 all declared
- [ ] PER-ROW QUALITY ARTIFACT REGISTRY present; PQAR-01/02/03 rows populated
- [ ] CATEGORICAL FIELD COVERAGE DECLARATION authored before first phase; all known categorical-field tables listed with Status = DECLARED
- [ ] AC-13 points to PQAR by name; AC-14 points to CFCD by name
- [ ] Phase Delta Block and CCT schema templates have inline quality bars in column headers
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank Incumbent Models? cells
- [ ] Every phase: Entry Contract with Imported constraints + Incumbent entry
- [ ] Every phase: Phase Delta Block before State Table
- [ ] Every phase: Exit Gate with Exported constraints + Incumbent exit
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column (exact name)
- [ ] If any new categorical-field table introduced mid-authoring: CFCD updated immediately
- [ ] If any new per-row quality artifact introduced: PQAR row added
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Coverage Scan: AC-01 through AC-14 + Check V; AC-14 confirms each CFCD table individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-02 -- Axis: Phrasing Register (C-29 Prose Field Negative-Exemplar Guards)

**Variation axis:** Phrasing register -- every prose/rationale field instruction in the model
is rewritten from positive-direction form ("must cite evidence", "be specific") to
negative-exemplar form: the specific fail mode for generic language is named inline, adjacent
to the field it governs. The following fields are upgraded: (1) Root Cause in BOTTLENECK
REGISTER -- inline instruction names specific forbidden exemplars; (2) Harm from Absence in
GAP REGISTER -- column header includes a named fail mode; (3) Gap in GAP REGISTER -- column
header includes a named fail mode; (4) Why As-Is Fails in Constraint-Incumbent Gap Analysis --
named exemplars added beyond "Generic language is a fail"; (5) Deviation from Happy Path in
EXCEPTION CATALOG -- inline note added. No new AC is added; instead, the Coverage Scan
guidance for AC-08 and AC-12 is upgraded to require per-field prose quality enumeration.

**Hypothesis:** R10 V-05 names "Generic language is a fail" in the Gap Analysis section but
uses positive-direction instructions elsewhere. A model can satisfy AC-08 by citing a source
artifact and field while still producing Root Cause prose like "coordination failure at approval
stage" -- which names a stage but not the specific artifact field and cell value. Negative
exemplars make the fail mode concrete and testable: the model knows exactly which phrases to
avoid. The Coverage Scan upgrade requires the scan to name specific Root Cause values and
confirm none match the named exemplars. Expected: C-29 PASS across all five prose fields;
Coverage Scan upgraded from format-check to value-check.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including all sub-conditions, (3) fill the
PER-ROW QUALITY ARTIFACT REGISTRY. Every artifact carries incumbent comparison fields. Phase
contracts import and export named constraints by CC-ID. Exception flows caused by constraint
import failures are traced bidirectionally in a dedicated Constraint-Break Exceptions subsection.
The cross-axis bridge is synthesized in a severity-rated Constraint-Incumbent Gap Analysis
with per-row rationale requirements enforced by inline negative-exemplar guards. All prose and
rationale fields in this model carry inline fail-mode instructions naming specific generic
language patterns as fail conditions -- not positive direction only.

---

**STATUS-QUO PROCESS DECLARATION**

| Field | Value |
|-------|-------|
| Incumbent process name | [Name of the as-is process or workflow tool currently in use] |
| Adoption context | [Who uses it and at what scale] |
| Known failure mode FM-1 | [Specific named failure] |
| Known failure mode FM-2 | [Same format] |
| Known failure mode FM-3 | [Same format] |
| Primary inertia driver | [Why this process persists] |

---

**OUTPUT ACCEPTANCE CRITERIA**

Declared before any content is authored. Post-fill scan executes these IDs -- does not restate
pass conditions.

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts have `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block schema and quality | (a) each phase has rubric-exact block before State Table; (b) every Divergence Type cell is exactly `missing`, `incorrect`, or `reversed`; (c) every Impact Severity cell is `HIGH`, `MED`, or `LOW`; HIGH/MED rows cite FM or "New gap" | Wrong column names; model-level block; wrong order; non-enumerated Divergence Type; blank or non-enumerated Impact Severity; HIGH/MED without FM trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability and prose quality | Bottleneck + Gap Registers have Root Cause citing source artifact and field using the exact format below; Coverage Scan names each Root Cause value and confirms none uses a forbidden exemplar (coordination failure, process issue, missing step, general delay, approval backlog) | Missing column; format without source citation; Root Cause value matches a forbidden exemplar or names a stage without citing the exact artifact field and cell value |
| AC-09 | Incumbent field completeness | Every artifact in Incumbent Coverage Mandate has required field populated | Any artifact missing its field; any blank incumbent field |
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported appears as imported in consuming phase; (b) every Handoff Strength cell is STRONG, WEAK, or ABSENT-with-justification; (c) every Incumbent Models? cell in CCT is Y, N, or ABSENT-with-justification | Any CC-ID with no consuming import; blank or invalid Handoff Strength; blank or invalid Incumbent Models? in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent or prose-only; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | Gap analysis completeness and prose quality | (a) Constraint-Incumbent Gap Analysis is a named structural section; (b) every CC-ID with Incumbent Models? = N has a row; (c) each row carries Gap Severity; (d) each row carries Why As-Is Fails naming a specific process characteristic -- Coverage Scan names each Why As-Is Fails value and confirms none uses a forbidden exemplar (not implemented, lacking this feature, insufficient, not modeled, unsupported); (e) no blank Incumbent Models? cells in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; Why As-Is Fails value matches forbidden exemplar; blank Incumbent Models? cell |
| AC-13 | Per-row quality artifact meta-registry | See PER-ROW QUALITY ARTIFACT REGISTRY. Coverage Scan must verify each Reg-ID individually. If any new per-row quality artifact is introduced, a new PQAR row is required before continuing | Any Reg-ID missing; bulk attestation; new artifact without PQAR update |

These thirteen checks are the acceptance definition. AC-08 and AC-12 Coverage Scan rows must
enumerate specific prose field values and confirm none match named exemplars -- bulk "all
rationale fields are specific" is a fail for these two ACs.

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | AC-12 | (a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails per row -- forbidden exemplars named; (e) no blank Incumbent Models? |

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

Each lifecycle phase contains a mandatory Phase Delta Block authored BEFORE the State Table.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)`:
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry** *(feeds AC-05)*

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |

**Status-Quo Role Comparison** *(dedicated artifact -- feeds AC-09)*

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |

---

**CONSTRAINT CHAIN REGISTRY** -- AUTHOR BEFORE ANY PHASE *(feeds AC-10, AC-12)*

| CC-ID | Constraint Name | Originating Phase (Ph-ID) | Consuming Phase(s) (Ph-ID) | Verification Method | Incumbent Models? (Y/N) |
|-------|-----------------|--------------------------|---------------------------|---------------------|------------------------|
| CC-01 | | | | | |

`Incumbent Models?` rules: Y / N / ABSENT-with-justification. Blank is a hard fail.

---

**FOR EACH PHASE, IN THIS EXACT ORDER:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

---

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | |
| Prior phase | |
| Active roles | |
| Objects entering | |
| Exception pre-check | |
| Imported constraints | |
| Constraint verification | |
| Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID: Phase Name]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID: Phase Name]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| | | | | | | |

**Decision Table [Ph-ID: Phase Name]**

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|--------------|----------|----------|----------|---------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID: Phase Name]**

```
Fork (S-ID):    [branching state]
Branch A:       [named path]
Branch B:       [named path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
As-Is join:     [incumbent join behavior -- or ABSENT]
Incumbent gap:  [what breaks if join condition fails -- or N/A]
```

**PHASE EXIT GATE [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | |
| Success transition | |
| Failure transition | |
| Blocked by | [NONE requires explicit justification] |
| Typical duration | |
| Delta source | |
| Exported constraints | |
| Constraint export gap | |
| Incumbent exit | |

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

**Constraint Gap Note:** List every ABSENT or WEAK transition with risk.

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) | Incumbent Terminal? (Y/N) |
|------|---------------|-----------------------------------|---------------------------------|--------------------------|
| T-01 | | | | |

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|---------------------------|----------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

Note on Deviation from Happy Path: generic language such as "process stops", "delays occur",
or "workflow interrupted" is a fail -- name the specific state or transition that is bypassed
and the specific downstream artifact that is affected.

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.

**Incumbent Exception Gap:** List E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions** *(dedicated subsection -- required for AC-11)*

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

---

**EDGE CASE CATALOG** *(feeds AC-03)*

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|---------------|---------|----------------|----------------|----------------------|---------------------------|-----------------|
| EC-01 | | | | | | | | |
| EC-02 | | | | | | | | |
| EC-03 | | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

Root Cause format (required exactly):
`Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [exact cell value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [exact cell value]`

Generic language in Root Cause is a fail. The following exemplars are forbidden -- if your
Root Cause matches one, rewrite before submitting: "coordination failure", "process issue",
"approval bottleneck", "missing step", "general delay", "communication gap", "resource
constraint". Root Cause must cite the exact source artifact, field label, and cell value --
not a stage name or generic description.

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap (generic language such as "missing step", "gap exists", or "step not performed" is a fail -- name the specific missing condition, precondition, or gated transition) | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence (generic language such as "increases risk", "causes delays", "leads to errors", or "creates problems" is a fail -- name the specific downstream harm mechanism, artifact affected, and breach condition) | Incumbent Awareness (Y/N) |
|------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)**

```
Handoff trigger:       [Event initiating handoff]
Recipient process:     [Named adjacent process]
Fields passed:         [Named data elements]
Acceptance condition:  [What recipient verifies]
As-Is gap:             [Y/N + note]
Delta source:          [DL-ID or NONE]
Exported constraint:   [CC-ID governing this handoff -- or NONE]
```

**SLA ANNOTATION (raise score)**

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-13 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-08 must name each Root Cause
value and confirm none matches a forbidden exemplar. AC-12(d) must name each Why As-Is Fails
value and confirm none matches a forbidden exemplar. Bulk "all rationale is specific" is a
fail for AC-08 and AC-12(d).

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [Root Cause values enumerated per B-ID and G-ID -- each value confirmed against forbidden exemplar list; any match named] |
| AC-09 | | [per-artifact incumbent field completeness; blanks named] |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values] |
| AC-11 | | [subsection present? CC-ID+Ph-ID per entry? CC-ID break coverage? E-ID validity?] |
| AC-12 | | [(a)-(c) confirmed; (d) Why As-Is Fails values enumerated per CC-ID row -- each value confirmed against forbidden exemplar list; any match named; (e) no blank Incumbent Models?] |
| AC-13 | | [PQAR-01 confirmed individually; PQAR-02 confirmed individually; PQAR-03 confirmed individually -- forbidden exemplar check for PQAR-03(d) confirmed here] |

**Check V:** (a) CC-ID break coverage; (b) E-ID CC-ID validity; (c) E-ID main catalog presence.
Any FAIL must be corrected. Self-attestation is not acceptable.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs] |
| Edge cases incumbent cannot handle | [EC-IDs] |
| Terminals incumbent leaves open-ended | [T-IDs] |
| Roles absent from incumbent | [R-IDs] |
| Gaps invisible to incumbent | [G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed] |

**Constraint-Incumbent Gap Analysis** *(feeds AC-12)*

Gap Severity: HIGH / MED / LOW.
`Why As-Is Fails` must name a specific process characteristic. Forbidden exemplars -- if your
entry matches one, rewrite: "not implemented", "lacking this feature", "insufficient",
"not modeled", "unsupported", "does not have this". Why As-Is Fails must name the specific
mechanism: the missing state machine node, the absent role gate, the unchecked precondition,
the skipped validation artifact -- not a general capability description.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| | | | [specific named process characteristic -- forbidden exemplars apply] |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA with AC-01 through AC-13 declared
- [ ] PQAR-01/02/03 rows populated; PQAR-03(d) notes forbidden exemplar requirement
- [ ] AC-08 Coverage Scan guidance requires per-value Root Cause enumeration
- [ ] AC-12(d) Coverage Scan guidance requires per-value Why As-Is Fails enumeration
- [ ] Root Cause format inline instruction includes forbidden exemplar list
- [ ] Gap column header includes named fail mode with forbidden exemplars
- [ ] Harm from Absence column header includes named fail mode with forbidden exemplars
- [ ] Deviation from Happy Path note includes named fail mode
- [ ] Why As-Is Fails section note includes forbidden exemplar list
- [ ] Coverage Scan: AC-01 through AC-13 + Check V; AC-08 and AC-12(d) enumerate values

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-03 -- Axis: Output Format (C-30 Dimensional Field Inventory)

**Variation axis:** Output format -- a dedicated DIMENSIONAL FIELD INVENTORY (DFI) section
is added between the PQAR and the INCUMBENT COVERAGE MANDATE. The DFI enumerates every
specific field in this model that requires dimensional enforcement (value enumeration or typed
failure mode), names its required values, and names its fail condition. A new AC-14 requires
the Coverage Scan to audit each DFI field individually in the output -- confirming no
out-of-vocabulary values are present. AC-14 is the detection fallback: it is operational even
if an inline column-header guard was absent from the prompt -- the DFI defines the enforcement
scope and the Coverage Scan AC-14 row executes the audit regardless.

**Hypothesis:** R10 V-05 applies inline dimensional guards in column headers of PQAR-registered
tables. If a column header guard is omitted (author oversight, table added mid-authoring, or
a non-PQAR table with a categorical field), there is no fallback mechanism. A model can fill
a Terminal Declaration `Type` column with "completed" or "closed" without any AC catching the
violation -- because no AC enumerates the Terminal Declaration Type field. The DFI + AC-14
close this gap: even if the prompt header is absent, the Coverage Scan AC-14 row names the
specific field and audits its values. Expected: C-30 PASS; any out-of-vocabulary value in a
DFI-registered field caught by AC-14 even when the column header was silent.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including all sub-conditions and AC-14 as
the dimensional field inventory audit, (3) fill the PER-ROW QUALITY ARTIFACT REGISTRY, (4)
fill the DIMENSIONAL FIELD INVENTORY naming every categorical field in this model before any
phase is authored. Every artifact carries incumbent comparison fields. Phase contracts import
and export named constraints by CC-ID. Exception flows caused by constraint import failures
are traced bidirectionally in a dedicated Constraint-Break Exceptions subsection. The DFI
is the scope declaration for AC-14; any categorical field introduced during authoring must
be added to the DFI before continuing.

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
| AC-03 | Delta Ref completeness | All five artifacts have `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block schema and quality | (a) block order; (b) Divergence Type exactly missing/incorrect/reversed; (c) Impact Severity HIGH/MED/LOW; HIGH/MED cites FM or "New gap" | Wrong column names; non-enumerated values; blank cells; HIGH/MED without FM trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Bottleneck + Gap Registers have Root Cause citing source artifact and field | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every artifact in Incumbent Coverage Mandate has required field populated | Any artifact missing its field; any blank incumbent field |
| AC-10 | Constraint chain completeness and quality | (a) CC-ID chain complete; (b) Handoff Strength STRONG/WEAK/ABSENT+justification; (c) Incumbent Models? Y/N/ABSENT+justification | CC-ID gap; blank or invalid Handoff Strength; blank or invalid Incumbent Models? |
| AC-11 | Constraint-break exception tagging | Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent; entry missing column; CC-ID break unrepresented; E-ID invalid |
| AC-12 | Gap analysis completeness | (a) section named; (b) all N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails names specific process characteristic; (e) no blank Incumbent Models? | Section absent; missing row; missing severity; generic rationale; blank Incumbent Models? |
| AC-13 | Per-row quality artifact meta-registry | See PQAR. Coverage Scan verifies each Reg-ID individually | Any Reg-ID missing; bulk attestation; new artifact without PQAR update |
| AC-14 | Dimensional Field Inventory audit | (a) DIMENSIONAL FIELD INVENTORY section present before any phase; (b) at least the six canonical fields enumerated with Required Values and Fail Condition; (c) Coverage Scan AC-14 audits each DFI field in the output individually -- names the field, lists observed values, confirms no out-of-vocabulary value; if a field lacks an inline column-header guard, names it as a guard gap; (d) any categorical field introduced during authoring added to DFI before continuing | DFI absent; fewer than six canonical fields; Coverage Scan AC-14 bulk attestation; new categorical field introduced without DFI update; out-of-vocabulary value in any DFI field |

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | AC-12 | (a) section named; (b) N-tagged rows; (c) Gap Severity; (d) Why As-Is Fails; (e) no blank Incumbent Models? |

---

**DIMENSIONAL FIELD INVENTORY** *(scope declaration -- feeds AC-14)*

Enumerate every categorical field in this model before authoring any phase. For each field,
name its table, required value set, fail condition, and whether an inline column-header guard
is present. If a new categorical field is introduced during authoring, add a row immediately.
Coverage Scan AC-14 audits each field listed here against output values.

| DFI-ID | Field Name | Table | Required Values | Fail Condition | Inline Header Guard? |
|--------|------------|-------|----------------|----------------|---------------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing / incorrect / reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH / MED / LOW (HIGH or MED requires FM trace) | blank; non-enumerated; HIGH/MED without trace | Y |
| DFI-03 | Handoff Strength | Constraint Chain Table | STRONG / WEAK / ABSENT (ABSENT requires inline justification) | blank; unrecognized value | Y |
| DFI-04 | Incumbent Models? | Constraint Chain Table | Y / N / ABSENT-with-justification | blank | Y |
| DFI-05 | Gap Severity | Constraint-Incumbent Gap Analysis | HIGH / MED / LOW | blank; non-enumerated | Y |
| DFI-06 | Type | Terminal Declaration | success / failure / cancel | blank; non-enumerated | [Author: assess and declare Y or N] |
| [DFI-NN] | [any additional categorical field introduced during authoring] | | | | |

Fields with Inline Header Guard? = N are enforcement gaps. AC-14 Coverage Scan must name them
and confirm the field is enforced via AC sub-condition enumeration instead. A field with neither
inline guard nor dedicated AC sub-condition is a DFI fail.

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

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)`:
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |

**Status-Quo Role Comparison**

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |

---

**CONSTRAINT CHAIN REGISTRY** -- BEFORE ANY PHASE

| CC-ID | Constraint Name | Originating Phase (Ph-ID) | Consuming Phase(s) (Ph-ID) | Verification Method | Incumbent Models? (Y/N) |
|-------|-----------------|--------------------------|---------------------------|---------------------|------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID]** | Field | Value |
|-------|-------|
| Entry condition | | Prior phase | | Active roles | | Objects entering | | Exception pre-check | | Imported constraints | | Constraint verification | | Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed) | Impact Severity (HIGH / MED / LOW -- HIGH/MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| | | | | | | |

**Decision Table [Ph-ID]**

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|--------------|----------|----------|----------|---------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID]**

```
Fork (S-ID):    [branching state]
Branch A:       [named path]  Branch B:       [named path]
Join condition: [what must hold]
Merge owner:    [R-ID]
As-Is join:     [or ABSENT]
Incumbent gap:  [or N/A]
```

**PHASE EXIT GATE [Ph-ID]**

| Field | Value |
|-------|-------|
| Exit condition | | Success transition | | Failure transition | | Blocked by | [NONE requires justification] |
| Typical duration | | Delta source | | Exported constraints | | Constraint export gap | | Incumbent exit | |

*Repeat per phase. Update DFI and PQAR if new categorical fields or per-row quality artifacts introduced.*

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

---

**TERMINAL DECLARATION** *(feeds AC-02, AC-09)*

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) | Incumbent Terminal? (Y/N) |
|------|---------------|-----------------------------------|---------------------------------|--------------------------|
| T-01 | | | | |

---

**EXCEPTION CATALOG** *(feeds AC-02, AC-03, AC-06, AC-09, AC-11)*

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|---------------------------|----------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.
**Incumbent Exception Gap:** E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions**

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

---

**EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|---------------|---------|----------------|----------------|----------------------|---------------------------|-----------------|
| EC-01 | | | | | | | | |
| EC-02 | | | | | | | | |

---

**BOTTLENECK REGISTER** *(feeds AC-03, AC-08, AC-09)*

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|------------|-------------------|----------------------|
| B-01 | | | | | | |

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

---

**GAP REGISTER**

| G-ID | Phase (Ph-ID) | Gap | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence | Incumbent Awareness (Y/N) |
|------|---------------|-----|---------------------------|------------------------|-------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)**

```
Handoff trigger:      [Event]
Recipient process:    [Named adjacent process]
Fields passed:        [Named data elements]
Acceptance condition: [What recipient verifies]
As-Is gap:            [Y/N + note]
Delta source:         [DL-ID or NONE]
Exported constraint:  [CC-ID or NONE]
```

**SLA ANNOTATION (raise score)**

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-14 plus Check V)*

AC-04, AC-10, AC-12, AC-13 sub-conditions confirmed individually. AC-14 must name each DFI
field, list observed values in the output, and confirm no out-of-vocabulary value. For any
DFI field with Inline Header Guard? = N, name it explicitly and confirm enforcement mechanism.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | |
| AC-02 | | |
| AC-03 | | |
| AC-04 | | [(a) block order; (b) Divergence Type values; (c) Impact Severity + FM trace] |
| AC-05 | | |
| AC-06 | | |
| AC-07 | | |
| AC-08 | | |
| AC-09 | | |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values] |
| AC-11 | | |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [PQAR-01 individually; PQAR-02 individually; PQAR-03 individually] |
| AC-14 | | [DFI present before phase authoring? DFI-01 (Divergence Type): observed values listed -- any non-enum named; DFI-02 (Impact Severity): observed values -- any blank or non-enum named; DFI-03 (Handoff Strength): observed values -- any blank named; DFI-04 (Incumbent Models?): observed values -- any blank named; DFI-05 (Gap Severity): observed values -- any blank named; DFI-06 (Terminal Type): observed values -- any non-enum named; inline guard status per field -- any N flagged with enforcement mechanism confirmed; any DFI rows added mid-authoring named] |

**Check V:** CC-ID break coverage; E-ID CC-ID validity; E-ID main catalog presence.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs] |
| Edge cases incumbent cannot handle | [EC-IDs] |
| Terminals incumbent leaves open-ended | [T-IDs] |
| Roles absent from incumbent | [R-IDs] |
| Gaps invisible to incumbent | [G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed] |

**Constraint-Incumbent Gap Analysis** *(feeds AC-12)*

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA with AC-01 through AC-14 declared
- [ ] PQAR-01/02/03 rows populated
- [ ] DIMENSIONAL FIELD INVENTORY authored before first phase with at least DFI-01 through DFI-06
- [ ] AC-14 declared in OAC with scope pointing to DFI
- [ ] If any new categorical field introduced: DFI row added immediately before continuing
- [ ] Phase Delta Block and CCT schema have inline quality bars
- [ ] Coverage Scan AC-14 names each DFI field and lists observed output values individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-04 -- Axes: Lifecycle Emphasis + Output Format (C-28 + C-30 Combined)

**Variation axis:** Lifecycle emphasis + output format -- both the CATEGORICAL FIELD COVERAGE
DECLARATION (CFCD, from V-01) and the DIMENSIONAL FIELD INVENTORY (DFI, from V-03) are
present. AC-14 verifies single-pass coverage (C-28); AC-15 verifies output-time field audit
(C-30). No prose negative-exemplar guards (C-29) are added. The two mechanisms serve different
phases of enforcement: the CFCD fires at authoring-start (before any phase), ensuring all
categorical-field tables are identified in a single sweep. The DFI fires at Coverage Scan
(output-time), ensuring no out-of-vocabulary values appear in the final output regardless of
whether the CFCD was complete.

**Hypothesis:** C-28 alone (V-01) can fail if a table is omitted from the CFCD -- but there
is no output-time fallback to catch the resulting missing guard. C-30 alone (V-03) catches
out-of-vocabulary values but does not prevent the authoring gap (a field may never receive an
inline guard). Together, CFCD (authoring prevention) + DFI (output detection) form a closed
loop: if a categorical field exists in the output without a guard, AC-15 will catch the
out-of-vocabulary value even if AC-14 missed the table. Expected: C-28 PASS + C-30 PASS;
any gap that passes the CFCD will be caught by the DFI output-time audit.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including AC-14 (single-pass CFCD) and AC-15
(DFI output audit), (3) fill the PQAR, (4) fill the CATEGORICAL FIELD COVERAGE DECLARATION
in a single pass, (5) fill the DIMENSIONAL FIELD INVENTORY, (6) register the constraint
chain. Every artifact carries incumbent comparison fields. Phase contracts import and export
named constraints by CC-ID. Exception flows are traced bidirectionally in a Constraint-Break
Exceptions subsection. The CFCD and DFI are co-authoritative: the CFCD prevents authoring
gaps and the DFI detects output-time violations. Any categorical field introduced during
authoring requires immediate updates to both CFCD and DFI.

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
| AC-04 | Phase Delta Block quality | (a) block order; (b) Divergence Type exactly missing/incorrect/reversed; (c) Impact Severity HIGH/MED/LOW; HIGH/MED cites FM or "New gap" | Non-enumerated value; blank; wrong order |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Root Cause cites source artifact and field using required format | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every Incumbent Coverage Mandate artifact has required field | Any artifact missing its field; blank |
| AC-10 | Constraint chain quality | (a) CC-ID chain complete; (b) Handoff Strength valid; (c) Incumbent Models? valid | Gap; blank Handoff Strength; blank Incumbent Models? |
| AC-11 | Constraint-break exception tagging | 5-column Constraint-Break subsection; every CC-ID break has E-ID; every E-ID traces back | Subsection absent; missing columns; untraced break |
| AC-12 | Gap analysis completeness | (a) section named; (b) all N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails specific; (e) no blank Incumbent Models? | Section absent; missing row; missing severity; generic rationale |
| AC-13 | PQAR meta-registry | See PQAR. Verify each Reg-ID individually | Missing Reg-ID; bulk attestation; new artifact without PQAR row |
| AC-14 | Cross-table categorical coverage (single-pass) | CFCD authored before first phase; all categorical-field tables listed; every row Status = DECLARED; Coverage Scan names each table and confirms Status | CFCD absent; table omitted; Status = MISSING at scan; declaration authored incrementally |
| AC-15 | Dimensional Field Inventory output audit | DFI present before first phase; at least 6 fields enumerated; Coverage Scan AC-15 names each DFI field, lists observed output values, confirms no out-of-vocabulary value; fields with no inline header guard named and enforcement mechanism confirmed | DFI absent; fewer than 6 fields; bulk attestation; out-of-vocabulary value in any DFI field |

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type; (c) Impact Severity + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum), Incumbent Models? (enum) | AC-10 | (a) chain completeness; (b) Handoff Strength; (c) Incumbent Models? |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (enum), Why As-Is Fails (rationale) | AC-12 | (a)-(e) as declared |

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

Author before any phase. List every table with at least one categorical field. Status must be
DECLARED for all rows at Coverage Scan.

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? |
|------------|---------------------|-------------------|-----------------------------|--------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header enumerates values; blank/non-enum is fail | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header enumerates values; blank is fail | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header enumerates HIGH/MED/LOW | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard and record DECLARED, or record MISSING] | | |
| [Additional tables] | | | | |

---

**DIMENSIONAL FIELD INVENTORY** *(output-time scope -- feeds AC-15)*

| DFI-ID | Field Name | Table | Required Values | Fail Condition | Inline Header Guard? |
|--------|------------|-------|----------------|----------------|---------------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing / incorrect / reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH / MED / LOW (HIGH/MED + FM trace) | blank; non-enum; HIGH/MED without trace | Y |
| DFI-03 | Handoff Strength | Constraint Chain Table | STRONG / WEAK / ABSENT+justification | blank; unrecognized | Y |
| DFI-04 | Incumbent Models? | Constraint Chain Table | Y / N / ABSENT+justification | blank | Y |
| DFI-05 | Gap Severity | Gap Analysis | HIGH / MED / LOW | blank; non-enum | Y |
| DFI-06 | Type | Terminal Declaration | success / failure / cancel | blank; non-enum | [Author declares] |
| [DFI-NN] | [additional] | | | | |

Fields with Inline Header Guard? = N: Coverage Scan AC-15 must name enforcement mechanism.

---

**INCUMBENT COVERAGE MANDATE**

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

**PHASE DELTA BLOCK REQUIREMENT**

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|

---

**DELTA CROSS-REFERENCE REQUIREMENT**

Five artifacts carry `Delta Ref (DL-ID or NONE)`:
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |

**Status-Quo Role Comparison**

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |

---

**CONSTRAINT CHAIN REGISTRY** -- BEFORE ANY PHASE

| CC-ID | Constraint Name | Originating Phase (Ph-ID) | Consuming Phase(s) (Ph-ID) | Verification Method | Incumbent Models? (Y/N) |
|-------|-----------------|--------------------------|---------------------------|---------------------|------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID]**

| Field | Value |
|-------|-------|
| Entry condition | | Prior phase | | Active roles | | Objects entering | | Exception pre-check | | Imported constraints | | Constraint verification | | Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed) | Impact Severity (HIGH / MED / LOW -- HIGH/MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| | | | | | | |

**Decision Table [Ph-ID]**

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|--------------|----------|----------|----------|---------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID]**

```
Fork (S-ID):    [branching state]
Branch A:       [named path]
Branch B:       [named path]
Join condition: [what must hold]
Merge owner:    [R-ID]
As-Is join:     [or ABSENT]
Incumbent gap:  [or N/A]
```

**PHASE EXIT GATE [Ph-ID]**

| Field | Value |
|-------|-------|
| Exit condition | | Success transition | | Failure transition | | Blocked by | | Typical duration | | Delta source | | Exported constraints | | Constraint export gap | | Incumbent exit | |

*Repeat per phase. If a new categorical-field table is introduced: update CFCD and DFI immediately.*

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) | Incumbent Terminal? (Y/N) |
|------|---------------|-----------------------------------|---------------------------------|--------------------------|
| T-01 | | | | |

---

**EXCEPTION CATALOG**

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|---------------------------|----------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.
**Incumbent Exception Gap:** E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions**

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

---

**EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|---------------|---------|----------------|----------------|----------------------|---------------------------|-----------------|
| EC-01 | | | | | | | | |
| EC-02 | | | | | | | | |

---

**BOTTLENECK REGISTER**

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|------------|-------------------|----------------------|
| B-01 | | | | | | |

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

---

**GAP REGISTER**

| G-ID | Phase (Ph-ID) | Gap | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence | Incumbent Awareness (Y/N) |
|------|---------------|-----|---------------------------|------------------------|-------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)**

```
Handoff trigger:      [Event]
Recipient process:    [Named adjacent process]
Fields passed:        [Named data elements]
Acceptance condition: [What recipient verifies]
As-Is gap:            [Y/N + note]
Delta source:         [DL-ID or NONE]
Exported constraint:  [CC-ID or NONE]
```

**SLA ANNOTATION (raise score)**

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-15 plus Check V)*

AC-04, AC-10, AC-12, AC-13 sub-conditions confirmed individually.
AC-14: name each CFCD table -- confirm Status = DECLARED.
AC-15: name each DFI field -- list observed output values -- confirm no out-of-vocabulary.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | |
| AC-02 | | |
| AC-03 | | |
| AC-04 | | [(a) block order; (b) Divergence Type; (c) Impact Severity + FM trace] |
| AC-05 | | |
| AC-06 | | |
| AC-07 | | |
| AC-08 | | |
| AC-09 | | |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength; (c) Incumbent Models?] |
| AC-11 | | |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [PQAR-01/02/03 confirmed individually] |
| AC-14 | | [CFCD present? Each table in CFCD named -- Status = DECLARED confirmed; any Status = MISSING?; any categorical-field table absent from CFCD?; any mid-authoring updates recorded?] |
| AC-15 | | [DFI present? DFI-01 (Divergence Type): values listed -- non-enum named; DFI-02 (Impact Severity): values listed -- blank/non-enum/missing trace named; DFI-03 (Handoff Strength): values listed; DFI-04 (Incumbent Models?): values listed; DFI-05 (Gap Severity): values listed; DFI-06 (Terminal Type): values listed -- non-enum named; fields with N inline guard: enforcement mechanism confirmed; mid-authoring DFI additions named] |

**Check V:** CC-ID break coverage; E-ID CC-ID validity; E-ID main catalog presence.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs] |
| Edge cases incumbent cannot handle | [EC-IDs] |
| Terminals incumbent leaves open-ended | [T-IDs] |
| Roles absent from incumbent | [R-IDs] |
| Gaps invisible to incumbent | [G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed] |

**Constraint-Incumbent Gap Analysis** *(feeds AC-12)*

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA with AC-01 through AC-15 declared
- [ ] PQAR-01/02/03 rows populated
- [ ] CFCD authored before first phase; all categorical-field tables listed with Status = DECLARED
- [ ] DFI authored before first phase; at least DFI-01 through DFI-06 rows present
- [ ] If new categorical-field table introduced: CFCD and DFI both updated immediately
- [ ] Phase Delta Block and CCT schema have inline quality bars
- [ ] Coverage Scan AC-14: confirms each CFCD table Status = DECLARED individually
- [ ] Coverage Scan AC-15: lists observed output values for each DFI field individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-05 -- Axes: All Three + Full Floor (C-28 + C-29 + C-30)

**Variation axis:** All three v10 criteria combined at maximum density on the R10 V-05 floor.
C-28: CFCD (single-pass categorical coverage, AC-14). C-29: negative-exemplar prose guards on
all rationale fields with AC-15 verifying prose quality in Coverage Scan. C-30: DFI output-time
audit (AC-16). The three mechanisms address orthogonal failure surfaces: CFCD prevents authoring
gaps in categorical coverage; prose guards prevent generic rationale in prose fields; DFI
detects output-time dimensional violations as a fallback. Together they close the dimensional
enforcement surface end-to-end: prevent (C-28) + constrain prose (C-29) + detect (C-30).

**Hypothesis:** V-01 prevents missing categorical-field tables; V-02 prevents generic prose
in rationale fields; V-03 detects out-of-vocabulary values at output time. Each in isolation
leaves two surfaces open. V-05 saturates all three simultaneously. The primary test is
whether the three mechanisms interact cleanly without redundancy: CFCD + DFI overlap only for
categorical fields (not prose); prose guards are orthogonal to both. The Coverage Scan has
three new rows (AC-14, AC-15, AC-16) that must each enumerate evidence independently. Expected:
C-28 PASS + C-29 PASS + C-30 PASS; Coverage Scan AC-14/15/16 demonstrate distinct evidence
with no cell sharing the same output-coverage claim.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including AC-14 (CFCD single-pass), AC-15
(prose field quality), and AC-16 (DFI output audit), (3) fill the PER-ROW QUALITY ARTIFACT
REGISTRY, (4) fill the CATEGORICAL FIELD COVERAGE DECLARATION in a single pass, (5) fill the
DIMENSIONAL FIELD INVENTORY, (6) register the constraint chain. Every artifact carries
incumbent comparison fields. Phase contracts import and export named constraints by CC-ID.
Exception flows caused by constraint import failures are traced bidirectionally in a Constraint-
Break Exceptions subsection. All prose and rationale fields carry inline negative-exemplar
fail-mode instructions. The CFCD prevents authoring gaps; the DFI detects output-time
violations; prose guards eliminate generic rationale. Any categorical field or per-row quality
artifact introduced during authoring requires immediate updates to CFCD, DFI, and PQAR.

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
| AC-08 | Root-cause traceability | Root Cause cites source artifact and field using required format | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every Incumbent Coverage Mandate artifact has required field | Any artifact missing its field; blank |
| AC-10 | Constraint chain quality | (a) CC-ID chain complete; (b) Handoff Strength STRONG/WEAK/ABSENT+justification; (c) Incumbent Models? Y/N/ABSENT+justification | Gap; blank or invalid values |
| AC-11 | Constraint-break exception tagging | 5-column Constraint-Break subsection; CC-ID breaks traced; E-IDs valid | Subsection absent; columns missing; untraced break |
| AC-12 | Gap analysis completeness | (a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity; (d) Why As-Is Fails specific; (e) no blank Incumbent Models? | Section absent; missing row; missing severity; generic rationale; blank |
| AC-13 | PQAR meta-registry | See PQAR. Verify each Reg-ID individually | Missing Reg-ID; bulk attestation; new artifact without PQAR row |
| AC-14 | Cross-table categorical coverage (single-pass) | CFCD authored before first phase; all categorical-field tables listed; Status = DECLARED per row; Coverage Scan confirms each table; if new table introduced mid-authoring: CFCD updated immediately | CFCD absent; table omitted; Status = MISSING at scan; incremental authoring |
| AC-15 | Prose field negative-exemplar quality | Coverage Scan AC-15 enumerates each prose/rationale field by name and confirms: (a) Root Cause -- no forbidden exemplar value (coordination failure, process issue, missing step, general delay, approval backlog); (b) Harm from Absence -- no forbidden exemplar (increases risk, causes delays, leads to errors); (c) Gap -- no forbidden exemplar (missing step, gap exists, step not performed); (d) Why As-Is Fails -- no forbidden exemplar (not implemented, lacking, insufficient, not modeled); (e) Deviation from Happy Path -- no stage-name-only description | Any prose field with forbidden exemplar value; bulk "all rationale is specific" without per-field enumeration |
| AC-16 | Dimensional Field Inventory output audit | DFI present before first phase; at least 6 fields enumerated; Coverage Scan AC-16 names each DFI field, lists observed output values, confirms no out-of-vocabulary value; fields with N inline guard named with enforcement mechanism | DFI absent; fewer than 6 fields; bulk attestation; out-of-vocabulary value present |

These sixteen checks are the acceptance definition. AC-14 and AC-16 provide structural
prevention + detection for categorical fields. AC-15 provides prose field quality verification.
Coverage Scan rows for AC-14, AC-15, AC-16 must each enumerate distinct evidence -- no cell
sharing the same coverage claim across these three rows.

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(feeds AC-13)*

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type; (c) Impact Severity + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength; (c) Incumbent Models? |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale -- forbidden exemplars) | AC-12 | (a) section named; (b) N-tagged rows; (c) Gap Severity; (d) Why As-Is Fails + forbidden exemplar check; (e) no blank Incumbent Models? |

---

**CATEGORICAL FIELD COVERAGE DECLARATION** *(single-pass -- feeds AC-14)*

Author before any phase in a single pass. Status = DECLARED required for every row.

| Table Name | Categorical Field(s) | Inline Guard Form | Status (DECLARED / MISSING) | Added Mid-Authoring? |
|------------|---------------------|-------------------|-----------------------------|--------------------|
| Phase Delta Block | Divergence Type, Impact Severity | Column header inline; blank/non-enum is fail | DECLARED | N/A |
| Constraint Chain Table | Handoff Strength, Incumbent Models? | Column header inline; blank is fail | DECLARED | N/A |
| Constraint-Incumbent Gap Analysis | Gap Severity | Column header inline; blank/non-enum is fail | DECLARED | N/A |
| Terminal Declaration | Type (success/failure/cancel) | [Author: add inline guard and record DECLARED] | | |
| [Additional tables identified during single-pass] | | | | |

---

**DIMENSIONAL FIELD INVENTORY** *(output-time scope -- feeds AC-16)*

| DFI-ID | Field Name | Table | Required Values | Fail Condition | Inline Header Guard? |
|--------|------------|-------|----------------|----------------|---------------------|
| DFI-01 | Divergence Type | Phase Delta Block | missing / incorrect / reversed | any other value | Y |
| DFI-02 | Impact Severity | Phase Delta Block | HIGH / MED / LOW (HIGH/MED + trace) | blank; non-enum; HIGH/MED without trace | Y |
| DFI-03 | Handoff Strength | Constraint Chain Table | STRONG / WEAK / ABSENT+justification | blank; unrecognized | Y |
| DFI-04 | Incumbent Models? | Constraint Chain Table | Y / N / ABSENT+justification | blank | Y |
| DFI-05 | Gap Severity | Gap Analysis | HIGH / MED / LOW | blank; non-enum | Y |
| DFI-06 | Type | Terminal Declaration | success / failure / cancel | blank; non-enum | [Author declares Y or N] |
| [DFI-NN] | [new categorical field] | | | | |

Fields with Inline Header Guard? = N: Coverage Scan AC-16 must name enforcement mechanism.

---

**INCUMBENT COVERAGE MANDATE**

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

**PHASE DELTA BLOCK REQUIREMENT**

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap"; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

---

**DELTA CROSS-REFERENCE REQUIREMENT**

Five artifacts carry `Delta Ref (DL-ID or NONE)`:
State Table / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

---

**SETUP**

**Domain Role Registry**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |

**Status-Quo Role Comparison**

| R-ID | Role Name | Present in Incumbent? (Y/N) | Incumbent Role Name or ABSENT | Gap if ABSENT |
|------|-----------|-----------------------------|-------------------------------|---------------|
| R-01 | | | | |

**Phase Index**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |

---

**CONSTRAINT CHAIN REGISTRY** -- BEFORE ANY PHASE

| CC-ID | Constraint Name | Originating Phase (Ph-ID) | Consuming Phase(s) (Ph-ID) | Verification Method | Incumbent Models? (Y/N) |
|-------|-----------------|--------------------------|---------------------------|---------------------|------------------------|
| CC-01 | | | | | |

---

**FOR EACH PHASE:**
Entry Contract --> Phase Delta Block --> State Table --> Decision Table --> Parallel Path --> Exit Gate

**PHASE ENTRY CONTRACT [Ph-ID]**

| Field | Value |
|-------|-------|
| Entry condition | | Prior phase | | Active roles | | Objects entering | | Exception pre-check | | Imported constraints | | Constraint verification | | Incumbent entry | |

**PHASE DELTA BLOCK [Ph-ID]** -- BEFORE STATE TABLE

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed) | Impact Severity (HIGH / MED / LOW -- HIGH/MED requires FM trace; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------|
| DL-01 | | | | |

**STATE TABLE [Ph-ID]**

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|---------------------------|----------------|--------------|---------------------------|
| | | | | | | |

**Decision Table [Ph-ID]**

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|--------------|----------|----------|----------|---------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID]**

```
Fork (S-ID):    [branching state]
Branch A:       [named path]
Branch B:       [named path]
Join condition: [what must hold]
Merge owner:    [R-ID]
As-Is join:     [or ABSENT]
Incumbent gap:  [or N/A]
```

**PHASE EXIT GATE [Ph-ID]**

| Field | Value |
|-------|-------|
| Exit condition | | Success transition | | Failure transition | | Blocked by | [NONE requires justification] |
| Typical duration | | Delta source | | Exported constraints | | Constraint export gap | | Incumbent exit | |

*Repeat per phase. If new categorical-field table introduced: update CFCD and DFI immediately.
If new per-row quality artifact introduced: update PQAR immediately.*

---

**CONSTRAINT CHAIN TABLE** *(feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

**Constraint Gap Note:** List every ABSENT or WEAK transition with risk.

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) | Incumbent Terminal? (Y/N) |
|------|---------------|-----------------------------------|---------------------------------|--------------------------|
| T-01 | | | | |

---

**EXCEPTION CATALOG**

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | As-Is Detection? (Y/N) | Delta Ref (DL-ID or NONE) | Terminal or Recovery |
|------|---------------------|----------------|---------|---------------------------|----------------|------------------------|---------------------------|----------------------|
| E-01 | | | | | | | | |
| E-02 | | | | | | | | |
| E-03 | | | | | | | | |

Deviation from Happy Path: generic language such as "process stops" or "workflow interrupted"
is a fail -- name the specific state bypassed and the downstream artifact affected.

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.
**Incumbent Exception Gap:** E-IDs where As-Is Detection? = N.

**Constraint-Break Exceptions**

| E-ID | CC-ID Violated | Phase-of-Origin (Ph-ID) | Constraint Violated | Violation Mechanism |
|------|----------------|-------------------------|---------------------|---------------------|
| | | | | |

---

**EDGE CASE CATALOG**

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | As-Is Handled? (Y/N) | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|---------------|---------|----------------|----------------|----------------------|---------------------------|-----------------|
| EC-01 | | | | | | | | |
| EC-02 | | | | | | | | |
| EC-03 | | | | | | | | |

---

**BOTTLENECK REGISTER**

| B-ID | Phase (Ph-ID) | Bottleneck | Delta Ref (DL-ID or NONE) | Root Cause | Downstream Impact | Incumbent Workaround |
|------|---------------|------------|---------------------------|------------|-------------------|----------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

Root Cause format (required exactly):
`Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [exact cell value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [exact cell value]`

Generic language in Root Cause is a fail. Forbidden exemplars: "coordination failure",
"process issue", "approval bottleneck", "missing step", "general delay", "communication gap".
Root Cause must cite the exact source artifact, field label, and cell value.

---

**GAP REGISTER**

| G-ID | Phase (Ph-ID) | Gap (generic language such as "missing step" or "gap exists" is a fail -- name the specific missing condition or gated transition) | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence (generic language such as "increases risk" or "causes delays" is a fail -- name the specific downstream harm mechanism and artifact affected) | Incumbent Awareness (Y/N) |
|------|---------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)**

```
Handoff trigger:      [Event]
Recipient process:    [Named adjacent process]
Fields passed:        [Named data elements]
Acceptance condition: [What recipient verifies]
As-Is gap:            [Y/N + note]
Delta source:         [DL-ID or NONE]
Exported constraint:  [CC-ID or NONE]
```

**SLA ANNOTATION (raise score)**

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-16 plus Check V)*

AC-04, AC-10, AC-12, AC-13 sub-conditions confirmed individually.
AC-14, AC-15, AC-16 must each enumerate distinct evidence -- no shared output-coverage claims.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | |
| AC-02 | | |
| AC-03 | | |
| AC-04 | | [(a) block order per phase; (b) Divergence Type values -- non-enum named; (c) Impact Severity -- FM trace confirmed per HIGH/MED row] |
| AC-05 | | |
| AC-06 | | |
| AC-07 | | |
| AC-08 | | [Root Cause format confirmed per B-ID and G-ID; values enumerated] |
| AC-09 | | |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values] |
| AC-11 | | |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [PQAR-01/02/03 confirmed individually; new Reg-IDs named if added] |
| AC-14 | | [CFCD present before first phase? Each table by name: Status = DECLARED confirmed; any Status = MISSING named; any categorical-field table absent from CFCD named; mid-authoring CFCD updates recorded] |
| AC-15 | | [(a) Root Cause values listed per B-ID and G-ID -- forbidden exemplar check: any match named; (b) Harm from Absence values listed per G-ID -- forbidden exemplar check; (c) Gap values listed per G-ID -- forbidden exemplar check; (d) Why As-Is Fails values listed per CC-ID row -- forbidden exemplar check; (e) Deviation from Happy Path values checked -- stage-name-only descriptions named] |
| AC-16 | | [DFI present? DFI-01: Divergence Type values listed -- non-enum named; DFI-02: Impact Severity values -- blank/non-enum/missing trace named; DFI-03: Handoff Strength values listed; DFI-04: Incumbent Models? values listed; DFI-05: Gap Severity values listed; DFI-06: Terminal Type values -- non-enum named; any DFI field with N inline guard: enforcement mechanism confirmed; mid-authoring DFI additions named] |

**Check V:** (a) CC-ID break coverage; (b) E-ID CC-ID validity; (c) E-ID main catalog presence.
Any FAIL must be corrected before output. Self-attestation is not acceptable.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect | [E-IDs] |
| Edge cases incumbent cannot handle | [EC-IDs] |
| Terminals incumbent leaves open-ended | [T-IDs] |
| Roles absent from incumbent | [R-IDs] |
| Gaps invisible to incumbent | [G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed] |

**Constraint-Incumbent Gap Analysis** *(feeds AC-12)*

Gap Severity: HIGH / MED / LOW.
Why As-Is Fails: forbidden exemplars -- "not implemented", "lacking", "insufficient",
"not modeled", "unsupported". Must name the specific missing mechanism.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| | | | [specific named process characteristic -- forbidden exemplars apply] |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA with AC-01 through AC-16 declared
- [ ] PQAR-01/02/03 rows populated; PQAR-03(d) notes forbidden exemplar requirement
- [ ] CFCD authored before first phase in a single pass; all categorical-field tables listed
- [ ] DFI authored before first phase; DFI-01 through DFI-06 minimum rows present
- [ ] AC-14 points to CFCD; AC-15 governs prose fields; AC-16 points to DFI
- [ ] Root Cause inline instruction includes forbidden exemplar list
- [ ] Gap column header includes named fail mode with forbidden exemplars
- [ ] Harm from Absence column header includes named fail mode with forbidden exemplars
- [ ] Deviation from Happy Path note includes named fail mode
- [ ] Why As-Is Fails section includes forbidden exemplar list
- [ ] Phase Delta Block and CCT schema have inline quality bars
- [ ] If new categorical-field table introduced mid-authoring: CFCD + DFI both updated
- [ ] If new per-row quality artifact introduced: PQAR row added
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Coverage Scan: AC-01 through AC-16 + Check V; AC-14/15/16 have distinct evidence cells

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Status-Quo Process Declaration > Output Acceptance Criteria > PQAR > CFCD > DFI >
Incumbent Coverage Mandate > Phase Delta Block Requirement > Delta Cross-Reference Requirement >
Setup (Domain Role Registry + Status-Quo Role Comparison + Phase Index) > Constraint Chain
Registry > Phases (Entry Contract + Phase Delta Block + State Table + Decision Table + Parallel
Path + Exit Gate per phase) > Constraint Chain Table > Terminal Declaration > Exception Catalog
(with Constraint-Break Exceptions subsection) > Edge Case Catalog > Bottleneck Register > Gap
Register > Cross-Process Handoff (optional) > SLA Annotation (optional) > Coverage Scan
(AC-01--AC-16 + Check V) > Inertia Summary (with Constraint-Incumbent Gap Analysis).
